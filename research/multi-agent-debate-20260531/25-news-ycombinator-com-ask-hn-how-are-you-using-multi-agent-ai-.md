---
url: "https://news.ycombinator.com/item?id=47270020"
title: "Ask HN: How are you using multi-agent AI systems in your daily workflow? | Hacker News"
engine: google
rank: 25
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 4472
fetched_at: "2026-05-31T20:14:13.814540+00:00"
---

|   
 | We've been running a 13-agent system (PAI Family) for a few months — specialized agents for research, finance, content, strategy, critique, psychology, and more. They collaborate, argue, and occasionally bet against each other on our prediction market.   |  
| --- |  
|   
 |  From my experience building multi-agent systems: the biggest underappreciated problem is state coordination.Frameworks handle individual agent capabilities well. What they don't handle: preventing two agents from silently overwriting each other's work on shared state. It's a classic race condition but in AI systems the output looks reasonable, so you don't notice it until production.  |  
| --- |  
 |  
|   
 |  What fails spectacularly in our setup: agents that share a conversation thread and try to resolve conflicts in real time. They race to add the last word, produce verbose non-decisions, and eventually one agent just agrees with whatever was said last. Consensus is a bad protocol for async, unequal agents.What works: role clarity + veto rights. One agent can only block, never propose. One agent makes calls, others can raise flags. You stop the chatbot parliament problem and actually get decisions. The other pattern worth stealing from production systems: treat inbound events (emails, webhooks, form submissions) as the task boundary, not the conversation turn. An agent that owns a mailbox and processes messages one at a time is dramatically more auditable than one that's always-on and decides what to react to. You can replay it, diff its outputs, and understand why it did what it did.  |  
| --- |  
 |  
|   
 |  Built my own custom solution that is completely spec-driven. Have concepts of specs, plans, and then a kanban board to monitor all agents as it progressesIt takes a plan, breaks it into dependent tasks, has human-in-the-loop for approval, and then is fire-and-forget after the plan is started with parallel agent workers. Has complete code review loops and testing loops for accuracy and quality. Idempotent retries and restarts...Completely frontend-driven so I don't have to deal with dumb terminals like claude code...  |  
| --- |  
 |  
|   
 |  I've been running a multi-agent setup for quite a while to do software development. I set up a workflow with agents at each stage, spec->plan->design->code->review. The key thing I learned was that the arrangement of the checks between agents matters more than which model you pick for any one step. Most failures were omissions that a gate between stages catches.  |  
| --- |  
 |  
|   
 |  I've set a fully async patern. blobs chunked into sqlite shards.   |  
| --- |  
 |  
|   
 |  The "job as library" pattern is simple: instead of wiring jobs into main or a framework, you split into 3 things. Your worker is another struct that loops on the queue and dispatches to handlers registered via RegisterHandler("type", fn). Your handlers are pure functions (ctx,payload) → (result, error) carried by a dependency struct. Main just assembles: open DB, create queue, create worker, register handlers, call worker.Start(ctx). Result: each handler is unit-testable without the worker or network, the worker is reusable across any pipeline, and lifecycle is controlled by a simple context.Cancel(). The whole "framework" is 500 lines of readable Go, not an opaque DSL. TL;DR: every service is a library with New() + Start(ctx), the binary is just an assembler. The "all in connectivity" pattern means every capability in your system — embeddings, document extraction, replication, MCP tools — is called through one interface: router.Call(ctx,"service", payload). The router looks up a SQLite routes table to decide how to fulfill that call: in-memory function (local), HTTP POST (http), QUIC stream (quic), MCP tool (mcp), vector embedding (embed), DB replication (dbsync), or silent no-op (noop). You code everything as local function calls — monolith. When you need to split a service out, you UPDATE one row in the routes table, the watcher picks it up via PRAGMA data_version, and the next call goes remote. That's the "job as library" pattern: the boundary between monolith and microservices is a config row, not an architecture decision.  |  
| --- |  
 |  
|   
 |  Following.   |  
| --- |  
 |  
|   
 |  We built a messaging platform for exactly this use case and instruct claws to check in with each other or share context with each other at regular intervals.   |  
| --- |  
 |  
 |

