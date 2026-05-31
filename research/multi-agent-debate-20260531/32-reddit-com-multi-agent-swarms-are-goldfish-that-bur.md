---
url: "https://www.reddit.com/r/AI_Agents/comments/1t3hmjz/multiagent_swarms_are_goldfish_that_burn_your/?solution=9d77c6ac2596fd079d77c6ac2596fd07&js_challenge=1&token=7afd7253fec22262ff1c52b1703fe9ecd128eae80abda15cc6c3133d916dfe36&jsc_orig_r="
title: "Multi-agent swarms are goldfish that burn your context window. So I built a free OS layer to fix it. : r/AI_Agents"
engine: google
rank: 32
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 2925
fetched_at: "2026-05-31T20:18:53.800576+00:00"
---

Multi-agent swarms are goldfish that burn your context window. So I built a free OS layer to fix it. : r/AI_Agents
First, agents are basically goldfish. Agent A spends 10 minutes solving a complex edge case. Later, Agent B spawns in a new session, has no idea it happened, and makes the exact same expensive mistake. 
Second, passing heavy generated data (like massive JSONs, SVGs, or PDFs) between agents burns hundreds of thousands of tokens and immediately kills the context window. 
So I built Neonia Cloud OS - a shared infrastructure layer for agent swarms, exposed entirely via a single MCP endpoint. The core system layer is completely free to use. 
  * Pass-by-Reference (Token Arbitrage): Stop forcing LLMs to read raw files. Neonia's internal Wasm tools save heavy data on the backend and return a lightweight URI. Agent A generates a massive file, passes the neo://resource/123 pointer to Agent B, who hands it to a Validator tool. The orchestrating LLMs never see the raw data. A 150K token pipeline drops to ~1K. 
  * Dual-Memory (The Hive-Mind): We decoupled memory. Agents use a memory_lesson tool to save structural rules globally (Root Cause -> Fix). If one agent touches a hot stove, it logs a lesson. Future isolated agents instantly inherit this rule. The swarm self-immunizes and gets smarter. 
  * Zero-Idle IPC Queues: Native atomic push/pop queues. Agents don’t sit in brittle while loops polling for tasks (which burns API credits). You can spin up concurrent swarms that pull tasks asynchronously without stepping on each other. 


It’s designed specifically to make agents work as an evolving, adaptive Hive-Mind rather than a bunch of isolated chat scripts patched together with environment variables. 
Thank you for your submission, for any questions regarding AI, please check out our wiki at (this is currently in test and we are actively adding to the wiki) 
Spot on. "Burning tokens on session-passing is a sign the agent boundaries are wrong" is exactly right when it comes to reasoning/conversational context. 
  1. The Shared Facts Layer: The LLM's context window is the ephemeral scratch-pad (which gets discarded). We use explicit MCP tools (like neo_sys_memory_lesson) to force agents to distill insights into hard rules written to the persistent "shared facts" OS layer before their session dies. 
  2. The Artifact Problem: Even with perfect agent boundaries, you still hit a wall when Agent A (e.g., a Data Fetcher) needs to hand off a massive computational artifact (like a 5MB JSON payload or generated CAD file) to Agent B (e.g., a Validator). No amount of good boundary design shrinks the physical payload. 


Basically, I built the OS layer so devs don't have to hack together that exact memory hierarchy from scratch every time. 
If you choose “Reject Optional Cookies” we won’t use cookies for these additional uses. You can update your cookie preference from your settings.

