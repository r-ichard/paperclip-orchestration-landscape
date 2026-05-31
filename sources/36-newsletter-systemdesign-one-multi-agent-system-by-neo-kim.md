---
url: "https://newsletter.systemdesign.one/p/multi-agent-system"
title: Multi Agent System - by Neo Kim
engine: google
rank: 36
published: "2026-04-30T09:57:47+02:00"
updated: "2026-04-30T09:57:47+02:00"
author: Neo Kim
org: The System Design Newsletter
char_count: 4674
fetched_at: "2026-05-31T17:39:35.116495+00:00"
---

is. Instead of one agent doing everything, you split the work across many agents. Each one has its own role, tools, and context.
Agents can generate code. Getting it right for your system, team conventions, and past decisions is the hard part – you end up wasting time and tokens in correction loops.
More MCPs give agents access to information, but not understanding. The teams pulling ahead use a context engine to give agents exactly what they need.


  * 

For example, Cognition’s Devin processed 5 million lines of COBOL (Common Business-Oriented Language) across 500GB of repositories with a single agent, raising its pull request merge rate from 34% to 67%.
But a single agent has three HARD limits. When your task runs into any of them, better prompts won’t help:
Past that limit, the earliest information drops out, and the agent starts losing track of its own plan. When compression
If you have four research queries that don’t depend on each other, running them one at a time wastes time. Running them across four separate agents takes roughly as long as the slowest one.


When one agent can’t hold all the tools and permissions the task needs, you give each role its own agent.
Better prompts and better tools solve most problems without adding the extra work of coordinating agents. But once you know you need many agents, the next question is what shape the system takes...
One central agent breaks a task into pieces, assigns each piece to a worker agent, and then puts the results together:


This is like an air traffic control tower that talks to every plane, while no plane talks directly to another.
A central agent running Opus 4 breaks a research query into parts and creates 2 to 10 worker agents on Sonnet 4 (sometimes more), all at the same time. The workers search the web, read documents, and gather evidence in parallel. When they finish, the central agent reads their results and writes a single research report.
It talks to workers one at a time. If each call takes 3 seconds and 20 workers are waiting, the ceiling is about 7 tasks per second. So the central agent becomes the slowest part of the system.
Each agent’s output becomes the next agent’s input, and entire sequence is set in advance. While orchestrator-worker lets the central agent decide what to do as it goes, pipeline removes that choice.
Before agents, a human reviewer had to jump between customer databases, legal sources, and support tickets to decide whether a business was safe to approve. Now their engineering team broke that work into a fixed flow of agent stages using a directed acyclic graph (
Stripe calls these contracts “rails” because they keep any single agent from spending too much time on irrelevant data. This setup cut their average handling time by 26%, and reviewers rated the agent outputs 96% helpful, with a full record of every decision at every step.
A 5-stage pipeline where each stage takes 2 seconds means a 10-second wait before any output, and adding a stage to improve quality increases the response time.
When every stage has a narrow contract, you can trace any failure back to exactly one step. That’s why regulated workflows like Stripe’s continue to use pipelines.
When the cost of being wrong is a regulator flagging your process, the extra seconds are a small price to pay.
A top-level manager agent gives work to one or more layers of manager agents below it, which then give work to individual workers.
The top-level agent holds the high-level goal and a summary from each branch, while each lower level sees only what its narrower role needs. Picture a military chain of command where orders flow down, reports flow up, and no one skips a level.
A top-level supervisor agent acts as a router and planner across 80+ pre-built domain agents for HR, sales, and procurement. Let’s say a user tries to “order new laptops for the design team”. The request reaches a Procure Equipment supervisor, who then hands the work to 
A worker produces a detailed result. The mid-level manager shortens it to one sentence. By the time it reaches the top, the detail that matters might be gone. Hierarchical structures trade detail for coverage: the higher you go, the wider the scope of each agent and the less it knows about any specific piece.
: a data store (typically Redis cache, database table, or vector store) that every agent can read from and write to. Yet there are NO direct messages between agents…
Subscribe to to keep reading this post and get 7 days of free access to the full post archives.
We use cookies to improve your experience, for analytics, and for marketing. You can accept, reject, or manage your preferences. See our .

