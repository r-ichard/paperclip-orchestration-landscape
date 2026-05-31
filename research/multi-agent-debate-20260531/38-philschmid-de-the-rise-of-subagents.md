---
url: "https://www.philschmid.de/the-rise-of-subagents"
title: The Rise of Subagents
engine: brave
rank: 38
published: 2025-09-15
updated: 2025-09-15
author: Philipp Schmid
org: Philipp Schmid
char_count: 3431
fetched_at: "2026-05-31T20:20:41.946197+00:00"
---

There is an increasing use of Subagents to reliably handle specific user goals. We can see this in tools like Claude Code and . A subagent is a specialized Agent that is purpose-built for a single, well-defined task. Subagents can be explicit, where a user or model defines them for reuse or implicit and dynamically defined. This addresses a key limitation of monolithic AI agents context pollution. When a single, big and complex agent handles many tasks, its context window, number of tools, can become cluttered and less reliable.
Subagents are specialized AI agents. They are most of the time used in combination with an orchestrator, which delegates tasks to them. A subagent is just like a normal agent and has the same components. This includes a name for identification, a description of its capabilities, system instructions and a set of tools to interact with environments. It also has its own isolated context window.

```












┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐



        ▼                       ▼                  ▼


│- Own Context   │    │- Own Context   │    │- Own Context   │
│- Own Tools     │    │- Own Tools     │    │- Own Tools     │
│- Solves Task A │    │- Solves Task B │    │- Solves Task C │

        │                       │                  │












```

Explicit, User-defined Subagents are a permanent team of reusable specialists. Subagent can be defined in a static file or directly in code and the orchestrator uses them trough their name or when a prompt matches its . Claude Code uses this method. The tools are manually listed in the definition, and the agent is stateless, meaning it starts fresh on every run.




```





You are an expert security code reviewer. Your purpose is to analyze code and identify vulnerabilities. Provide feedback in a numbered list.

```

Implicit, On-the-Fly Subagents can be created temporary by an orchestrator to handle tasks as they come up. The orchestrator uses a tool () to create and interact with the agent. The system dynamically assigns tools based on the user's natural language request from pre-defined pool which are needed to solve the task. Poke.com uses this method to created unlimited agents for specific user request. A key feature is that these agents can be stateful, e.g. keep context from previous runs when called with the same .

```









    - IMPORTANT: Analyze my last 5 sent emails to the 'marketing-team@' mailing list to match my typical writing style, greeting, and sign-off.





    - End with a clear call to action: ask the team to review the full report and send their feedback for the Q4 planning session by EOD Friday.


```

  *   * 

Both predefined and on-the-fly subagents will see increased usage. Dynamic agents might find more adoption in general B2C applications. Predefined agents are a great fit for more structured and repeatable enterprise workflows.
. The key to success is giving the LLM the right information and tools at the right time. Using Subagents allows us to create a focused environment for the LLM with a clear, isolated context, specific system instructions, and a limited set of tools for the task. This improves performance and can reduce the cost of reaching the goal.
But even with a subagent architecture, for agentic systems, breaking down a complex task into smaller subagent functions can make them easier to test and evaluate in isolation.

