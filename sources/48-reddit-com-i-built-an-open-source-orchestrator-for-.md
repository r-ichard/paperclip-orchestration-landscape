---
url: "https://www.reddit.com/r/ClaudeAI/comments/1rl11b4/i_built_an_opensource_orchestrator_for_running/?solution=e21863548d1a113fe21863548d1a113f&js_challenge=1&token=7afd7253fec22262ff1c52b1703fe9ec198443f8589c5ae637d6aebaa058bdb4&jsc_orig_r="
title: "I built an open-source orchestrator for running multiple Claude Code agents in parallel with automatic dispatch, isolated worktrees, auto-merge, and handoffs when context runs out : r/ClaudeAI"
engine: brave
rank: 48
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 5143
fetched_at: "2026-05-31T17:40:37.124891+00:00"
---

I built an open-source orchestrator for running multiple Claude Code agents in parallel with automatic dispatch, isolated worktrees, auto-merge, and handoffs when context runs out : r/ClaudeAI
#  I built an open-source orchestrator for running multiple Claude Code agents in parallel with automatic dispatch, isolated worktrees, auto-merge, and handoffs when context runs out 

```
I've been running multiple Claude Code instances on the same codebase for a while and kept hitting the same problems: repeating the same setup over and over for each agent session, context windows degrading silently, burning out from constantly context switching between agent terminals.


So I built Stoneforge. It's open-source (Apache 2.0) and handles the coordination layer so you can run 5-10+ agents without babysitting them.

I built it using Claude Code, and it's designed to orchestrate Claude Code agents (along with Codex and OpenCode).

How it works:


You talk to a Director agent that breaks your goal into prioritized tasks with dependencies. A dispatch daemon assigns tasks to idle workers when available. Each worker runs in its own git worktree with a separate branch and separate directory, so there are no no file conflicts. When a task is done, a steward runs your tests, reviews the code, and if everything looks good, squash-merges to a target branch.


When a worker approaches its context limit, it commits its progress, writes structured handoff notes, and exits cleanly. The next worker picks up on the same branch with a fresh context window and full history of what was tried. Instead of context decaying with each compaction, memory survives across agent sessions.


How it compares to Agent Teams:


Agent Teams stores state in ephemeral file-based task lists. Stoneforge event-sources everything to SQLite + JSONL, so state survives restarts with a full audit trail. Agent Teams is terminal-only, while Stoneforge gives you a web dashboard with live agent output, kanban boards, and task management. Merging in Agent Teams is manual. In Stoneforge, stewards handle it automatically.


Stoneforge also works with Codex and OpenCode, not just Claude Code. You can split agents across multiple MAX plans to increase your throughput.


Caveats:


This is early-stage software. Running multiple agents burns through tokens fast. There are no approval gates by default. Agents read, write, and push code without asking. I ship daily and docs sometimes lag behind the code. If one Claude Code instance handles your workload today, you probably don't need this.


GitHub: https://github.com/stoneforge-ai/stoneforge

It's completely free and open-source (Apache 2.0). Install with `npm install -g @stoneforge/smithy` and run `sf init` in any project.


I also wrote a detailed technical post covering the dispatch daemon, merge flow, handoff mechanism, dual storage model, and every design tradeoff: https://stoneforge.ai/blog/introducing-stoneforge/


Happy to answer questions about the architecture or how I use it.
```

This is great. I am going to give it a try. I see that currently it supports Claude Code, Open Code and Codex CLI natively. However, if I need to use Gemini CLI (or a local llm using opencode), does it need to be configured via Opencode? Will try it out anyway, but just checking if you have a quick answer 
Hmm.. I didn't realize anyone used Gemini CLI for coding. What's the use case? Otherwise, you can open a PR for a custom agent provider. 
I was thinking to use Gemini 3.1 Pro especially for planning, and code reviews since it has good reasoning abilities. Let me do some tests before on this aspect. Claude + Opencode is a excellent combo already. 
Hey, thank you for your work. Im quite new on this with no advanced dev experience and I have been building an app only through Claude Desktop but want to explore agents to have a more structured approach. I found your topic while looking for tutorials to have Claude as the orchestrator with agents using specific open source models to limit the cost and not have full reliance on Claude. Is there any way to do this with your tool? Thanks. 
Yes, you can use OpenCode with Nvidia's free build credits. You can grab an API key here: and get access to near unlimited GLM 5.1, MiniMax 2.7, etc. which are very capable models. Here's a guide to setting it up: 
We are solving the same problem from a different angle. Stoneforge handles the orchestration layer (dispatch, worktrees, auto-merge). We focused on the coordination state: what does each agent know about what other agents are doing? 
Our approach is a shared HTTP API that agents call into. Task board with claim/release, presence (active/idle/stuck), team chat. Any agent framework can POST to it. Runs locally, single binary. 
The context window degradation problem is real. We found that giving each agent a narrow defined role with explicit boundaries reduces context bloat significantly because they stop trying to understand the whole codebase. 
If you choose “Reject Optional Cookies” we won’t use cookies for these additional uses. You can update your cookie preference from your settings.

