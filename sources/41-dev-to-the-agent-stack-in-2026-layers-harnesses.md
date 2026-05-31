---
url: "https://dev.to/hieu_tran_80c388add84c060/the-agent-stack-in-2026-layers-harnesses-and-where-you-actually-build-2e5g"
title: "The Agent Stack in 2026: Layers, Harnesses, and Where You Actually Build - DEV Community"
engine: brave
rank: 41
published: "2026-04-14T15:36:46Z"
updated: "2026-04-14T15:37:32Z"
author: Hieu TRAN
org: DEV Community
char_count: 13092
fetched_at: "2026-05-31T17:40:05.536492+00:00"
---

Two releases in early April 2026 sparked a lot of strong takes: Anthropic's (public beta, April 8) and LangChain's (a few weeks earlier). Some people called it a fundamental shift in agent development. Others called it framework churn in a trench coat.
Before arguing either way, it's worth stepping back to ask a simpler question: And where in that stack are these new platforms fitting in?
This post maps that stack — including what Anthropic's own research says about architectural complexity — and tries to give an honest account of what changed and what didn't.
Before the Managed Agents release, Anthropic published — a practical guide that describes a clear progression of architectural complexity:
The foundation. A single LLM enhanced with retrieval, tools, and memory. Most agents that are "working well" live here — a well-prompted model with the right tools is often sufficient, and genuinely hard to beat on simplicity.


Systems where LLMs dynamically direct their own processes and tool usage. The LLM decides what to do next, not predefined code paths.
The key principle Anthropic emphasizes: This is worth keeping in mind when evaluating new platforms that default to "full agent" architectures.
_(What follows is a mental model for thinking about the ecosystem — not an established industry standard or official taxonomy. The "layers" below aren't clean boundaries; they're positions on a spectrum of how much you build versus how much you configure.)_
You're calling LLM APIs, wiring tool execution, managing state, and handling retries in code you own. Every decision about routing, memory, and error handling is explicit in your codebase.
_Example: You write a LangGraph graph in Python — nodes for each step, edges for routing, explicit state management. Full control, full responsibility._
The framework provides abstractions (agents, chains, memory) and manages the LLM call loop. You focus on tool configuration and agent logic, not raw API bookkeeping. Still code-heavy, but with guardrails.
You describe — its role, skills, and knowledge — in structured files. The platform handles deployment, memory, sandboxing, credential isolation, and protocol support. What used to take a week of infrastructure work becomes a single command.
_Example (Deep Agents Deploy): You write (identity and behavior in plain markdown) and files (domain knowledge loaded on demand). Run . The platform handles memory, sandboxing, and serves MCP + A2A + Agent Protocol endpoints._
_Example (Claude Managed Agents): You configure what the agent does. Anthropic's infrastructure separates the Brain (Claude + control logic) from the Hands (execution sandbox with no credential access). An append-only session log acts as durable external memory — if the Brain crashes mid-task, a new instance resumes from the last event._
A well-prompted model with the right tools. No custom orchestration, no deployment pipeline — just a system prompt and a tool list.
The two April releases — Managed Agents and Deep Agents Deploy — sit in the "upper middle" range. They're not eliminating code entirely. But they pull a substantial chunk of work (memory management, credential isolation, multi-protocol support, sandboxing) out of application code and into platform infrastructure.
Before 2026, building the equivalent of "credential-isolated sandbox + append-only session log + MCP/A2A/Agent Protocol server" would take a week of infrastructure setup. These platforms make it the default.


Run , and the framework handles memory (filesystem-backed, per-session), sandboxing (Daytona, Runloop, Modal), and a production server with MCP + A2A + Agent Protocol support.
  * — an append-only event log that the agent's external memory. If the Brain crashes, a new instance picks up from the last event.


These platforms are real and the architecture is coherent. The question is whether they're the right tool for a given problem — and the honest answer depends on what you're building.
Alongside the Managed Agents release, Anthropic's engineering blog published — a detailed account of how they built a three-agent harness for generating full applications:


The Planner/Generator/Evaluator loop produced high-quality output — but the more interesting finding is what happened as the underlying model improved from Claude Opus 4.5 to 4.6.
> _"Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."_
As Claude 4.6 got better at longer coherent work, Anthropic simplified the harness: removed sprint decomposition, shifted the evaluator from per-sprint to end-of-run assessment. The orchestration got less complex, not more — because the model could handle more directly.
This cuts both ways. It's a caution against premature context harness adoption just as much as it's a caution against over-engineering your own orchestration. If the problem fits a well-prompted single agent (Level 1), adding workflow patterns or a full harness platform is probably overhead, not value.



handles the portability concern better than Managed Agents: it runs on any model (OpenAI, Anthropic, Google, Ollama), deploys self-hosted or cloud, and the / format is MIT-licensed. Switching cost is low. Managed Agents provides tighter infrastructure integration at the cost of lock-in.
In a coupled design, code that an agent generates or executes runs in the same process space as its credentials. A successful prompt injection in that scenario doesn't just compromise one task — it potentially exposes everything that agent can access.
Credential isolation addresses this directly. It's not a new concept: service meshes, secret managers like Vault, and per-service IAM roles have applied this principle for years. The pattern is well understood — limit what any given execution context can reach.
Managed Agents' Brain/Hands separation applies this principle to agent architecture: the sandbox where generated code runs has no access to authentication tokens. Deep Agents Deploy enforces similar isolation through its sandbox provider abstraction.
You can achieve the same isolation when building your own harness — the pattern is architectural, not proprietary. Teams that already take security seriously in their own infra do this. The difference is packaging: context harness platforms make credential isolation the default rather than a deliberate design decision. That's a real convenience benefit, not a claim that self-built systems are inherently less secure.
The honest trade-off: build your own harness and you get full control over the security model, at the cost of designing and maintaining it yourself. Use a platform harness and you get a tested default, at the cost of depending on the platform's security assumptions. Neither is strictly better — they're different bets on where to spend the effort.
Both Managed Agents and Deep Agents Deploy share a core concept: define the agent at the context level — identity, skills, and knowledge in structured files, not in code. OpenClaw, a community-driven agent framework, arrived at the same architectural conclusion independently.
OpenClaw defines agents the same way: an agent is an identity plus a set of skills loaded from ClawHub, its community skills registry. The concept maps directly onto + or Managed Agents' Brain configuration. Same idea, different execution context.
In February 2026, a supply chain attack targeting ClawHub (dubbed "ClawHavoc") was disclosed. Attackers had compromised 12 publisher accounts and published 1,184 malicious skills. Once loaded into an agent's context, these skills could exfiltrate credentials, redirect tool calls, or poison the agent's reasoning. The attack had been active for an undisclosed period before discovery.
Security research from Snyk reinforced the scope of the problem: their ToxicSkills report found that 36.8% of ClawHub skills contained some form of vulnerability, with 13.4% rated critical severity.
This isn't a criticism of OpenClaw's architectural concept — defining agents at the context level is sound. It's evidence of what the concept requires to be viable in production: a trust model for the skill supply chain, credential isolation so loaded skills can't reach authentication tokens, and audit infrastructure that logs what ran and when.  
ClawHavoc is a useful grounding for the security argument above: context-level agent definition isn't inherently a security risk. The risk is loading skills from an unaudited community registry into an execution context that has credential access. The architectural pattern is separable from the security failure — but only if the infrastructure underneath it takes the threat seriously.
Map this to Managed Agents: Brain ≈ Agent Scheduler + Context Manager. Session ≈ Memory Manager + Storage Manager. Hands ≈ Tool Manager + Access Manager. The convergence is not coincidental — two separate research and industry paths arrived at the same architectural conclusions because they're solving the same underlying resource-management problems.
AIOS demonstrates 2.1x faster execution when serving multiple agents compared to naive approaches — the primitives have real performance implications.
The (co-located with ASPLOS 2026) signals academia is treating this as serious systems research: OS-level mechanisms for AI-agent workloads, isolation models, scheduling techniques. The same rigor that produced virtual memory and process scheduling is now being applied to agent infrastructure.



Anthropic's progression — Augmented LLM → Workflows → Agents — describes agent , not platform choice. A managed platform can run a Level 1 agent. A custom LangGraph harness can implement Level 3 patterns. The two axes are orthogonal.
The default answer on this axis: Most problems that seem to need multi-agent workflows can be handled by a single well-prompted model with the right tools. Adding Level 2 workflow patterns or Level 3 autonomous control is only worth it when performance measurably improves — regardless of which platform you're on.
custom execution logic on LangGraph, fronted by a harness-compatible deployment format. Deep Agents Deploy already supports this — can front a custom LangGraph backend while providing standard endpoints and memory management. You get opinionated deployment without giving up orchestration control.
The Brain is still Claude. A well-designed harness on a weak model underperforms a poorly-designed one on a strong model. The harness multiplies what the model can do — it doesn't replace what the model doesn't know.
No platform handles ambiguous or underspecified tasks automatically. The agent's instructions still need to be clear about what "done" looks like. is only as useful as the thinking that went into writing it.
Managed Agents produces session logs. Deep Agents integrates with LangSmith. But deciding whether the agent did the right thing — and diagnosing silent failures — is still on you.
As Anthropic's own harness engineering work shows: when the model gets better, the right response is usually to simplify the harness, not keep the old constraints in place.
The agent ecosystem is stratifying into distinct layers, which is a healthy sign of maturation — the same way web infrastructure stratified from raw TCP into HTTP, then web frameworks, then deployment platforms.
The low-level frameworks (LangGraph, Claude Agent SDK) aren't being replaced. They're becoming the substrate that context harness platforms run on — the way TCP/IP didn't disappear when HTTP arrived. But for most production deployments, the question is increasingly: at which layer of this stack does my problem belong?
Managed Agents and Deep Agents Deploy are real platforms with real value for specific use cases. They're also new, vendor-specific in different ways, and add constraints that some workloads won't want. That's a normal trade-off, not a revelation.
The more durable insight from both releases, and from Anthropic's harness engineering research, is architectural: **the agent's identity and capability belong in a portable, readable definition layer; the execution, memory, security, and deployment machinery belongs in infrastructure below it.** Whether you get there via a managed platform or build it yourself, that separation is worth targeting.


In support of our mission to accelerate the developer journey on Google Cloud, we built Dev Signal — a multi-agent system designed to transform raw community signals into reliable technical guidance by automating the path from discovery to expert creation.
In support of our mission to accelerate the developer journey on Google Cloud, we built Dev Signal — a multi-agent system designed to transform raw community signals into reliable technical guidance by automating the path from discovery to expert creation.
Explore this insightful write-up embraced by the inclusive DEV Community. can contribute insights and expand our shared knowledge.
At DEV, and forges stronger connections. If this piece resonated with you, a brief note of thanks goes a long way.

