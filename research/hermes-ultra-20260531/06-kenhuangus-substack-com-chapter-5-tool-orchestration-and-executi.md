---
url: "https://kenhuangus.substack.com/p/chapter-5-tool-orchestration-and"
title: "Chapter 5: Tool Orchestration and Execution (Claude Code vs. Hermes Agent)"
engine: google
rank: 6
published: "2026-04-22T15:59:47+02:00"
updated: "2026-04-22T15:59:47+02:00"
author: Ken Huang
org: Agentic AI
char_count: 9315
fetched_at: "2026-05-31T19:23:17.666652+00:00"
---

Tool orchestration is the layer between "the model wants to call 5 tools" and "those 5 tools actually execute safely and efficiently." It decides which tools can run in parallel, which must run serially, and what happens when a tool fails mid-batch. Without it, an agent either serializes everything (slow) or parallelizes everything (dangerous) — orchestration is the logic that threads the needle between those two failure modes, and it's what separates a production harness from a weekend prototype.
and is built around a single key insight: group tool calls into batches by concurrency safety, then run each batch either fully parallel or fully serial.
on each tool's parsed input. Adjacent safe tools get merged into the same batch; any unsafe tool starts a new serial batch.

```
// src/services/tools/toolOrchestration.ts
// Groups tool_use blocks into concurrent or serial batches.
// Conservative: if parsing fails or isConcurrencySafe() throws, defaults to serial.
function partitionToolCalls(
  toolUseMessages: ToolUseBlock[],
  toolUseContext: ToolUseContext,
): Batch[] {
  return toolUseMessages.reduce((acc: Batch[], toolUse) => {
    const tool = findToolByName(toolUseContext.options.tools, toolUse.name)
    const parsedInput = tool?.inputSchema.safeParse(toolUse.input)

    const isConcurrencySafe = parsedInput?.success
      ? (() => {
          try { return Boolean(tool?.isConcurrencySafe(parsedInput.data)) }
          catch { return false }
        })()
      : false

    // Merge into the last batch if it's also concurrent; otherwise start a new one
    if (isConcurrencySafe && acc[acc.length - 1]?.isConcurrencySafe) {
      acc[acc.length - 1]!.blocks.push(toolUse)
    } else {
      acc.push({ isConcurrencySafe, blocks: [toolUse] })
    }
    return acc
  }, [])
}
```

async generator that yields results out-of-order as they complete — so a 1-second tool doesn't wait behind a 5-second tool.

```
// src/services/tools/toolOrchestration.ts
// Runs all tools in the batch simultaneously, up to CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY workers.
// Results stream out as each tool finishes, not in input order.
async function* runToolsConcurrently(
  toolUseMessages: ToolUseBlock[],
  assistantMessages: AssistantMessage[],
  canUseTool: CanUseToolFn,
  toolUseContext: ToolUseContext,
): AsyncGenerator<MessageUpdateLazy, void> {
  yield* all(
    toolUseMessages.map(async function* (toolUse) {
      // Mark as in-progress for UI tracking
      toolUseContext.setInProgressToolUseIDs(prev => new Set(prev).add(toolUse.id))
      yield* runToolUse(toolUse, /* ... */, canUseTool, toolUseContext)
      markToolUseAsComplete(toolUseContext, toolUse.id)
    }),
    getMaxToolUseConcurrency(), // reads CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY, default 10
  )
}
```

Serial batches apply context modifiers immediately after each tool, so the next tool sees the updated state (e.g., a changed working directory).

```
// src/services/tools/toolOrchestration.ts
// Runs tools one at a time. Context changes (like cwd updates) apply before the next tool.
async function* runToolsSerially(/* ... */): AsyncGenerator<MessageUpdate, void> {
  let currentContext = toolUseContext
  for (const toolUse of toolUseMessages) {
    for await (const update of runToolUse(toolUse, /* ... */, currentContext)) {
      if (update.contextModifier) {
        // Apply immediately — next tool in the loop sees this change
        currentContext = update.contextModifier.modifyContext(currentContext)
      }
      yield { message: update.message, newContext: currentContext }
    }
  }
}
```

starts executing tools as their blocks arrive during streaming, rather than waiting for the full response. When the user interrupts mid-execution, 

```
// src/query.ts
// Generates error tool_results for any tool_use that was interrupted before completing.
// Without this, the model would see orphaned tool_use blocks and get confused.
function* yieldMissingToolResultBlocks(
  assistantMessages: AssistantMessage[],
  errorMessage: string,
) {
  for (const assistantMessage of assistantMessages) {
    const toolUseBlocks = /* filter content for tool_use blocks */
    for (const toolUse of toolUseBlocks) {
      yield createUserMessage({
        content: [{
          type: 'tool_result',
          content: errorMessage,  // e.g. "Interrupted by user"
          is_error: true,
          tool_use_id: toolUse.id,
        }],
      })
    }
  }
}
```

Hermes takes a heuristic approach: instead of per-tool declarations, it maintains global sets of known-safe and known-unsafe tool names, then adds path-overlap detection for file tools.

```
# hermes-agent/run_agent.py

# Tools that must never run concurrently — interactive or user-facing.
_NEVER_PARALLEL_TOOLS = frozenset({"clarify"})

# Read-only tools with no shared mutable session state — safe to parallelize.
_PARALLEL_SAFE_TOOLS = frozenset({
    "ha_get_state", "ha_list_entities", "ha_list_services",
    "read_file", "search_files", "session_search", "skill_view",
    "skills_list", "vision_analyze", "web_extract", "web_search",
})

# File tools that can run concurrently only when targeting independent paths.
_PATH_SCOPED_TOOLS = frozenset({"read_file", "write_file", "patch"})

# Hard cap on concurrent worker threads.
_MAX_TOOL_WORKERS = 8

def _should_parallelize_tool_batch(tool_calls) -> bool:
    """Return True when a tool-call batch is safe to run concurrently."""
    if len(tool_calls) <= 1:
        return False  # No point parallelizing a single tool

    tool_names = [tc.function.name for tc in tool_calls]

    # Any never-parallel tool in the batch forces serial execution
    if any(name in _NEVER_PARALLEL_TOOLS for name in tool_names):
        return False

    reserved_paths: list[Path] = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        try:
            function_args = json.loads(tool_call.function.arguments)
        except Exception:
            return False  # Unparseable args → default to serial (safe)

        if tool_name in _PATH_SCOPED_TOOLS:
            scoped_path = _extract_parallel_scope_path(tool_name, function_args)
            if scoped_path is None:
                return False
            # Reject if this path overlaps with any already-reserved path
            if any(_paths_overlap(scoped_path, existing) for existing in reserved_paths):
                return False
            reserved_paths.append(scoped_path)
            continue

        if tool_name not in _PARALLEL_SAFE_TOOLS:
            return False  # Unknown tool → serial

    return True
```

```
# hermes-agent/run_agent.py
# Prevents two file tools from running concurrently if one path is a prefix of the other.
# e.g., read_file("/etc") and read_file("/etc/passwd") would overlap.
def _paths_overlap(left: Path, right: Path) -> bool:
    """Return True when two paths may refer to the same subtree."""
    left_parts = left.parts
    right_parts = right.parts
    common_len = min(len(left_parts), len(right_parts))
    # If one path is a prefix of the other, they overlap
    return left_parts[:common_len] == right_parts[:common_len]
```

```
# hermes-agent/run_agent.py
# Parallel execution path — all tools in the batch run simultaneously.
max_workers = min(num_tools, _MAX_TOOL_WORKERS)  # Never exceed 8 workers
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = []
    for i, (tc, name, args) in enumerate(parsed_calls):
        # Each tool call is submitted as an independent future
        f = executor.submit(_run_tool, i, tc, name, args)
        futures.append(f)
    # Block until all tools complete (errors captured inside _run_tool)
    concurrent.futures.wait(futures)
# Results are collected in order after all futures finish
```

```
# hermes-agent/tools/process_registry.py
# Global registry — thread-safe, survives across agent turns.
class ProcessRegistry:
    """In-memory registry of running and finished background processes.
    
    Provides: output buffering (200KB rolling window), status polling,
    blocking wait with interrupt support, kill, and crash recovery via
    JSON checkpoint file.
    """
    def __init__(self):
        self._running: Dict[str, ProcessSession] = {}
        self._finished: Dict[str, ProcessSession] = {}
        self._lock = threading.Lock()
        # Processes with notify_on_complete push here on exit,
        # triggering a new agent turn automatically.
        self.completion_queue: queue.Queue = queue.Queue()

    def spawn_local(self, command: str, ...) -> ProcessSession:
        # Spawns via subprocess.Popen with a reader thread for live output
        ...

    def poll(self, session_id: str) -> dict:
        # Non-blocking status check — returns output preview + exit code
        ...

    def wait(self, session_id: str, timeout: int = None) -> dict:
        # Blocking wait with interrupt support (checks _interrupt_event)
        ...
```

is particularly useful for long-running background tasks: when a process exits, it pushes a completion event that the CLI loop drains to auto-trigger a new agent turn with the results.
We use cookies to improve your experience, for analytics, and for marketing. You can accept, reject, or manage your preferences. See our .

