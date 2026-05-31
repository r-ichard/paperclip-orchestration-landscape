---
url: "https://github.com/paperclipai/paperclip"
title: "GitHub - paperclipai/paperclip: The open-source app everyone uses to manage agents at work · GitHub"
engine: google
rank: 2
published: unknown
updated: unknown
author: unknown
org: GitHub
char_count: 6821
fetched_at: "2026-05-31T17:20:34.242912+00:00"
---

|   |  
| --- |  
Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. Bring your own agents, assign goals, and track work and costs from one dashboard.  

  
 |  
|  |  
 |  
 |  
| ❌ You have 20 Claude Code tabs open and can't track which one does what. On reboot you lose everything.  |  
| --- |  
| ✅ Context flows from the task up through the project and company goals — your agent always knows what to do and why.  |  
| ✅ Paperclip gives you org charts, ticketing, delegation, and governance out of the box — so you run a company, not a pile of scripts.  |  
 |  
 |  
| ❌ You have an idea, you have to find your repo, fire up Claude Code, keep a tab open, and babysit it.  |  
Paperclip is a full control plane, not a wrapper. Before you build any of this yourself, know that it already exists:

```
┌──────────────────────────────────────────────────────────────┐
│                       PAPERCLIP SERVER                       │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │Identity & │  │  Work &   │  │ Heartbeat │  │Governance │  │
│  │  Access   │  │   Tasks   │  │ Execution │  │& Approvals│  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │ Org Chart │  │Workspaces │  │  Plugins  │  │  Budget   │  │
│  │ & Agents  │  │ & Runtime │  │           │  │ & Costs   │  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │ Routines  │  │ Secrets & │  │ Activity  │  │  Company  │  │
│  │& Schedules│  │  Storage  │  │ & Events  │  │Portability│  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
└──────────────────────────────────────────────────────────────┘
         ▲              ▲              ▲              ▲
   ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
   │  Claude   │  │   Codex   │  │   CLI     │  │ HTTP/web  │
   │   Code    │  │           │  │  agents   │  │   bots    │
   └───────────┘  └───────────┘  └───────────┘  └───────────┘

```
  
|  — Two deployment modes (trusted local or authenticated), board users, agent API keys, short-lived run JWTs, company memberships, invite flows, and OpenClaw onboarding. Every mutating request is traced to an actor.  |  — Agents have roles, titles, reporting lines, permissions, and budgets. Adapter examples match the diagram: Claude Code, Codex, CLI agents such as Cursor/Gemini/bash, HTTP/webhook bots such as OpenClaw, and external adapter plugins. If it can receive a heartbeat, it's hired.  |  
| --- | --- |  
|  — Issues carry company/project/goal/parent links, atomic checkout with execution locks, first-class blocker dependencies, comments, documents, attachments, work products, labels, and inbox state. No double-work, no lost context.  |  — DB-backed wakeup queue with coalescing, budget checks, workspace resolution, secret injection, skill loading, and adapter invocation. Runs produce structured logs, cost events, session state, and audit trails. Recovery handles orphaned runs automatically.  |  
|  — Project workspaces, isolated execution workspaces (git worktrees, operator branches), and runtime services (dev servers, preview URLs). Agents work in the right directory with the right context every time.  |  — Board approval workflows, execution policies with review/approval stages, decision tracking, budget hard-stops, agent pause/resume/terminate, and full audit logging. Nothing ships without your sign-off.  |  
|  — Token and cost tracking by company, agent, project, goal, issue, provider, and model. Scoped budget policies with warning thresholds and hard stops. Overspend pauses agents and cancels queued work automatically.  |  — Recurring tasks with cron, webhook, and API triggers. Concurrency and catch-up policies. Each routine execution creates a tracked issue and wakes the assigned agent — no manual kick-offs needed.  |  
|  — Instance-wide plugin system with out-of-process workers, capability-gated host services, job scheduling, tool exposure, and UI contributions. Extend Paperclip without forking it.  |  — Instance and company secrets, encrypted local storage, provider-backed object storage, attachments, and work products. Sensitive values stay out of prompts unless a scoped run explicitly needs them.  |  
|  — Mutating actions, heartbeat state changes, cost events, approvals, comments, and work products are recorded as durable activity so operators can audit what happened and why.  |  — Export and import entire organizations — agents, skills, projects, routines, and issues — with secret scrubbing and collision handling. One deployment, many companies, complete data isolation.  |  
 |  
|  |  
| This is for teams. If you have one agent, you probably don't need Paperclip. If you have twenty — you definitely do.  |  
That quickstart path now defaults to trusted local loopback mode for the fastest first run. To start in authenticated/private mode instead, choose a bind preset explicitly:
Locally, a single Node.js process manages an embedded Postgres and local file storage. For production, point it at your own Postgres and deploy however you like. Configure projects, agents, and goals — the agents take care of the rest.
If you're a solo entrepreneur you can use Tailscale to access Paperclip on the go. Then later you can deploy to e.g. Vercel when you need it.
Paperclip those agents. It orchestrates them into a company — with org charts, budgets, goals, governance, and accountability.
Agent orchestration has subtleties in how you coordinate who has work checked out, how to maintain sessions, monitoring costs, establishing governance - Paperclip does this for you.
By default, agents run on scheduled heartbeats and event-based triggers (task assignment, @-mentions). You can also hook in continuous agents like OpenClaw. You bring your agent and Paperclip coordinates.

```
pnpm dev              
pnpm dev:once         
pnpm dev:server       
pnpm build            
pnpm typecheck        
pnpm              
pnpm test:watch       
pnpm test:e2e         
pnpm db:generate      
pnpm db:migrate       
```

does not run Playwright. Browser suites stay separate and are typically run only when working on those flows or in CI.


Paperclip collects anonymous usage telemetry to help us understand how the product is used and improve it. No personal information, issue content, prompts, file paths, or secrets are ever collected. Private repository references are hashed with a per-install salt before being sent.

