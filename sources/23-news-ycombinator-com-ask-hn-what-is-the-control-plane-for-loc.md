---
url: "https://news.ycombinator.com/item?id=47242849"
title: "Ask HN: What is the \"Control Plane\" for local AI agents? | Hacker News"
engine: duckduckgo
rank: 23
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 5216
fetched_at: "2026-05-31T17:38:34.925321+00:00"
---

|   
 | <a href="https://ibb.co/v6QLjdBY"><img src="https://i.ibb.co/S4dV3mxr/Agents-Orchestration.png" alt="Agents-Orchestration" border="0"></a>I’ve been running an increasing number of local coding agents (Claude Code, Codex CLI, OpenCode, etc.) and I’ve hit a wall: orchestration and state visibility. When you have multiple agents working on different sub-tasks in a single repo, terminal logs become unmanageable. I find myself needing a "Mission Control" — a centralized tracking system that acts as a bridge between my local terminal sessions and a high-level UI. Human-in-the-loop: I can reply to the issue from my phone/web, and the local CLI picks up the comment to continue or pivot. The Problem: GitHub Issues (and Jira/Trello) weren't built for the high-frequency event loop of an AI agent. The UX feels sluggish, and there’s no native concept of a "streaming session" or "agent heartbeats." If you’re managing 5+ agents working on a codebase simultaneously, how do you track their progress and intervene without context-switching between 5 terminal tabs? I’ve sketched out a flow where GitHub Issues acts as the hub (linking Codex, Claude Code, and OpenClaw), but I’m looking for something more purpose-built.  |  
| --- |  
|   
 |  I solve this exact problem running OpenClaw (24/7 agent orchestrator). Here's what actually works after months of iteration: Architecture: 1. HEARTBEAT.md — Every agent reads this before acting. Routes to current priorities, cascades work through a defined sequence (not random agent picking a task) 2. TODO.md — Single source of truth with sections: "DO NOW" (unblocked), "BLOCKED" (waiting), "DONE" (completed). Agents read this, not chat history or logs 3. active-tasks.md — Breadcrumbs from interrupted runs. If an agent crashes, the next session reads what was interrupted and resumes 4. Sub-agent output files (qa-status.md, conversion-tracker.md, etc) — Each specialized agent writes structured results. Prevents re-running the same analysis. The key: State files are deterministic. No "what was I thinking?" after a crash. The next agent reads the same input, same structure, same decision rules. Terminal log management: - Each agent logs its own session ID (e.g., [agent-001-mar05-0430]) - Output files are prefixed by agent type (qa-, scout-, coo-) - Logs are sent to daily files (memory/2026-03-05.md) for searchability Deployment: I run ~8 agents on cron (QA watchdog, scout, content factory, conversion tracker, etc). They wake up, read their input files, write results, die. No persistent terminal. No state collision. The problem you're hitting is probably: agents don't know what other agents already did. Solution is just: everything runs through a shared TODO.md and writes results to named files.  |  
| --- |  
 |  
|   
 |  I ended up building my own for this. SQLite backend, breaks work into stages with gates between them. A gate checks each handoff before the next stage starts. Does the code match the spec, did the tests pass, that kind of thing.I've been running it with Claude Code for about four months now. What I didn't expect was how much the gates matter relative to the model itself. Most of the failures I see aren't hallucinations, they're omissions, and a structured check catches those easily. I wrote up how I did it and how to start building one yourself from markdown and a shell script:   |  
| --- |  
 |  
|   
 |  I'm building something that I called control plane for agents, but it's only solving half of the problem you're mentioning. Basically it allows me to connect to my agents remotely from anywhere, so I have one running on my server and several running on my home PC. I generally just use something like notion or beads for issue tracking.Another thing I do is I have a custom Claude skill that runs every night and goes through all my repositories and Claude conversations and then updates my dashboard and tasks in notion with progress.  |  
| --- |  
 |  
|   
 |  Works fine for a one-man pet project, but the second you hit a real codebase and dozens of commits a day, that nightly job is just gonna choke on the context window or slam into Anthropic's rate limits. You really need to be streaming agent state into a DB on the fly via WebSockets, not piecing it together once every 24 hours  |  
| --- |  
 |  
|   
 |  There's no off-the-shelf "Jira for AI" product out there right now tbh. Most sane teams are either hacking together thin SQLite + WebSockets dashboards, or just sucking it up and staring at raw stdout across 5 tmux panes. If you need a self-hosted setup with tracing, Langfuse should do the trick and cover like 90% of your pain points. Honestly, if you actually polish this control plane concept and open-source it, the demand will be massive  |  
| --- |  
 |  
|   
 |  It's not for your use case per se, but at Tacnode we're building what we call a "context lake" that's essentially a living, queryable context layer. It's got way more horsepower than you're describing. Built instead for enterprise-scale needs.   |  
| --- |  
 |  
|   
 |  I’m building this right now, in a little beyond the POC, but would love your feedback. I have the framework down.  |  
| --- |  
 |  
 |

