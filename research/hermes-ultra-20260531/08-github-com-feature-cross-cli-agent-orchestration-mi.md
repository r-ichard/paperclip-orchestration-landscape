---
url: "https://github.com/NousResearch/hermes-agent/issues/413"
title: "Feature: Cross-CLI Agent Orchestration — Mixed Workflows with External Agent CLIs (inspired by AgentWorkforce/relay) · Issue #413 · NousResearch/hermes-agent"
engine: google
rank: 8
published: "2026-03-05T04:03:53.000Z"
updated: unknown
author: teknium1
org: GitHub
char_count: 3584
fetched_at: "2026-05-31T19:23:36.539695+00:00"
---

Today, Hermes Agent's spawns in-process children — clones of the Hermes agent runtime with restricted toolsets. This is powerful for tasks that benefit from Hermes's tool ecosystem (terminal, file ops, web, skills), but it means .
takes a fundamentally different approach: it orchestrates (Claude Code, Codex CLI, Gemini CLI, Aider, Goose, OpenCode) by wrapping them in PTY sessions, injecting messages as stdin, and capturing stdout. This means a single workflow can have Claude Code writing backend code, Codex CLI writing tests, and Gemini CLI handling documentation — each using their native tool ecosystem.
Hermes already has skills for spawning individual external agents (, , ), but these are — one agent at a time, no inter-agent communication, no shared workflow context. This issue proposes extending our multi-agent architecture to support where Hermes subagents and external CLI agents coexist and collaborate.
  1. Messages are written to PTY stdin as formatted text. The broker applies human cooldown (3s) and message coalescing (500ms window) to mimic natural interaction timing.


  
A workflow that leverages the right agent for each step would produce better results than one-size-fits-all Hermes subagents for everything.

```
Step 1: Hermes subagent researches the API (web tools, arxiv)
Step 2: Claude Code implements the backend (deep codebase context)
Step 3: Codex CLI writes tests (fast, sandboxed execution)
Step 4: Hermes subagent reviews and integrates (skills, memory, git workflow)

```




  * Apply the orchestration patterns from (fan-out, pipeline, debate) to external agents


This is a extending to support external agent backends. It needs custom Python logic for PTY management, process lifecycle, output parsing, and integration with the workflow DAG engine from . This is a , not a skill — skills can't manage concurrent PTY sessions with inter-agent routing.



```
(
    [
        {: , : ,
         : },  
        {: , : ,
         : [],
         : ,  
         : },
        {: , : ,
         : [],
         : ,  
         : },
        {: , : ,
         : [, ]}  
    ]
)
```






  * — External agents use their own tools, not ours. We can't see what files they edited, what commands they ran, etc. (only their stdout).
  * — When an external agent fails, we only see its stdout. No structured error data, no tool call logs.


  1. The and skills already know how to invoke these CLIs. Could the workflow engine invoke skills as steps rather than building a separate PTY layer?
  2. Options: (a) capture all stdout and let the parent LLM parse it, (b) structured output parsing per CLI, (c) require external agents to write results to a file that we read. Option (c) is most reliable but least flexible.
  3. External CLIs don't have our parameter. Options: include context in the task prompt text, write context to a file the CLI can read, or use CLI-specific mechanisms (Claude's , Codex's flag).
  4. **Should external agents be able to write to our shared memory ()?** They'd need a mechanism to do so (file-based bridge?), or we accept they're output-only participants.
  5. Should we check for installed CLIs at workflow parse time (fail fast) or at step execution time (allow partial workflows)?
  6. We're orchestrating, not importing. The CLIs are user-installed tools. No license concerns for our codebase, but users need valid subscriptions to each service.


  * — Adversarial Debate Mode (could include external agents as participants)
  * — Shared Memory Pools (context sharing with external agents is an open question)







