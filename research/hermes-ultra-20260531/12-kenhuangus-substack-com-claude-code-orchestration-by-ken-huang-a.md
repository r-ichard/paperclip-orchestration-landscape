---
url: "https://kenhuangus.substack.com/p/claude-code-orchestration-dynamic"
title: CLAUDE CODE ORCHESTRATION - by Ken Huang - Agentic AI
engine: google
rank: 12
published: "2026-05-29T05:06:35+02:00"
updated: "2026-05-29T05:06:35+02:00"
author: Ken Huang
org: Agentic AI
char_count: 7519
fetched_at: "2026-05-31T19:22:38.860156+00:00"
---

For years, the developer’s relationship with AI followed a single pattern: chat and wait. Each task required constant human steering — babysitting the model through every intermediate step while watching the context window bloat with each turn. As conversations grew longer, focus degraded, and the session became a graveyard of volatile, non-repeatable logic.
Claude Code’s orchestration model shatters this constraint. With three distinct collaboration primitives — Dynamic Workflows, Subagents, and Agent Teams — developers can now match the execution model to the actual structure of the problem. Choosing the right primitive is no longer a nice-to-have; at enterprise scale it is a cost and quality decision.
The question is no longer “How do I prompt Claude for this?” — it is “What execution model best fits the structure of this problem?” Dynamic Workflows, Subagents, and Agent Teams solve different problems. Using the wrong one wastes tokens, time, and trust.
This guide covers three things: what each primitive is, where it differs from the others, and how to pick the right one for your situation. It concludes with a scenario decision matrix you can use as a day-to-day reference.
are Claude Code’s new orchestration layer for problems that are too big for a single agent pass. The feature is available on Max, Team, and Enterprise plans across the Claude Code CLI, VS Code extension, Desktop app, and the Claude API (including Amazon Bedrock and Vertex AI).
The core mechanism: when you include the word “workflow” in a prompt, or when the /effort ultracode setting is active, Claude does not simply respond. Instead, it generates a JavaScript orchestration script on the fly. That script holds all loops, branching logic, and intermediate variables. Claude then runs the script, which fans work out across tens to hundreds of parallel subagents, has adversarial agents attempt to refute findings, iterates until answers converge, and returns only the verified result.
In standard Claude Code, Claude IS the orchestrator — making turn-by-turn decisions whose intermediate results accumulate in the context window. In Dynamic Workflows, a generated JavaScript script IS the orchestrator. Claude’s context window holds only the final verified answer, not the exhaust of every intermediate step.
  * Convergence-driven iteration: the workflow keeps spawning agents and iterating until answers stabilize — the number of passes is determined by the work, not preset by the user
  * Caching-backed resumability: if a run is paused or interrupted, completed agents return cached results instantly on resume; no work is repeated


The /deep-research command is the premier bundled workflow. Unlike standard search tools that accept the first plausible answer, /deep-research is explicitly designed to disprove its own findings. It fans searches across multiple angles, cross-checks sources against one another, holds an internal vote on each claim, and includes only claims that survive adversarial scrutiny. The output is a cited research report with a higher reliability bar than a single-pass AI search.
Setting effort to ultracode activates automatic workflow orchestration. In this mode Claude evaluates each request and decides on its own whether the task warrants a workflow. When it does, Claude plans an understand-change-verify loop: one subagent cluster to map the architecture, a second to execute changes, a third to verify results. This loop runs automatically. Token cost and time are higher than a standard prompt, but success rates on multi-stage engineering tasks are substantially better.
Use Dynamic Workflows when three conditions are present together: the task is too large for a single context window, the split strategy is unknown in advance, and result quality is more important than token economy. Canonical use cases include:


Avoid Dynamic Workflows for repeatable, well-defined tasks with predictable token budgets. If you already know the exact workflow and want consistent, cost-predictable execution, a custom Subagent is more efficient. Dynamic Workflows are also overkill for small, bounded tasks where a single agent pass is sufficient.
Subagents are temporary worker instances launched from the current session. Each subagent receives its own isolated context window, executes its task, and returns only a summary of the result. The calling session never absorbs the subagent’s intermediate logs or raw output — only the final answer. This keeps the orchestrating session clean and its context focused.


When built-in types are insufficient, you can define custom subagents as Markdown files with YAML front matter. Store them in .claude/agents/ (project-scoped) or ~/.claude/agents/ (user-scoped, available across all projects). The key configuration fields are:
  * description: the primary trigger signal — Claude reads this to decide when to invoke the subagent automatically; precision here determines reliability


The description field deserves emphasis. Claude uses it as an automatic invocation trigger — the more precisely it describes both the task and the right moment to invoke the subagent, the more reliably it fires without explicit user prompting.
With a standard subagent, you — or Claude’s turn-by-turn reasoning — decide which subagent to spawn, when, and how to aggregate results. The orchestration logic lives in your head or in the session. Subagents are the execution units; the coordination is human-directed.
With Dynamic Workflows, Claude generates the orchestration script itself. The script decides how many subagents to spawn, how to partition the work, when to run adversarial verification passes, and when results have converged sufficiently to stop. The orchestration burden shifts from human to machine. Dynamic Workflows can also internally spin up subagents as part of the workflow — so the two mechanisms are composable, not exclusive.


Agent Teams launched as a research preview in February 2026 (Claude Code v2.1.32). They enable multiple Claude instances to work in parallel on different subtasks while coordinating through a git-based shared workspace. Unlike manual multi-instance setups where you orchestrate separate Claude sessions by hand, Agent Teams provide built-in coordination — agents claim tasks, merge changes continuously, and resolve conflicts automatically.
The key requirement is Opus 4.6 minimum. Agent Teams are designed for complex, interdependent work where multiple specialists must produce output that is eventually unified into a single coherent artifact — typically a codebase.
Each member of an agent team is a fully independent Claude session with its own context, its own tool access, and its own area of responsibility. Coordination happens through a shared git repository:


This coordination model means agents are not just parallel workers — they are aware of each other’s progress and output. A backend agent knows when the API contract it must conform to has been updated by a frontend agent.
The critical difference from Subagents is the coordination model. Subagents are independent — they do not communicate with each other or share state. They receive a task, complete it, return a result, and disappear. Agent Teams are collaborative — members share a working environment, observe each other’s changes, and coordinate around a common artifact over time.
We use cookies to improve your experience, for analytics, and for marketing. You can accept, reject, or manage your preferences. See our .

