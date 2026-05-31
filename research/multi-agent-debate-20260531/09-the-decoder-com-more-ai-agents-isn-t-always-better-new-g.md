---
url: "https://the-decoder.com/more-ai-agents-isnt-always-better-new-google-and-mit-study-finds/"
title: "More AI agents isn't always better, new Google and MIT study finds"
engine: google
rank: 9
published: "2025-12-13T14:53:56+00:00"
updated: "2025-12-13T14:55:00+00:00"
author: Matthias Bastian
org: The Decoder
char_count: 4138
fetched_at: "2026-05-31T20:11:21.227417+00:00"
---

**A study from Google Research, Google Deepmind, and MIT challenges the idea that more AI agents means better results. The researchers pinpoint when multi-agent systems help and when they make things worse.**
If one AI agent works well, a team of specialized agents should work even better. That was the thinking behind . But a from Google and MIT tells a different story. Multi-agent systems swung wildly in performance depending on the task—from an 81 percent boost to a 70 percent drop.
The team ran 180 controlled experiments across five architecture types and three model families: OpenAI's GPT, Google's Gemini, and Anthropic's Claude. They held prompts, tools, and token budgets constant, changing only coordination structure and model capabilities.
Financial analysis tasks that break into independent pieces saw an 80.9 percent boost with centralized multi-agent coordination. Different agents analyzed sales trends, cost structures, and market data in parallel, then merged results.
Minecraft planning tasks told the opposite story. Every multi-agent setup hurt performance by 39 to 70 percent. The problem: each crafting action changes the inventory state that later actions depend on. These sequential dependencies don't split well across agents.
Multi-agent systems (MAS) beat single-agent solutions (SAS) on parallelizable tasks like financial analysis (top right), with gains up to 81 percent. On sequential planning tasks (bottom left), they drop performance by up to 70 percent. | Image: Kim et al. (2025)
Whenever each step in a task alters the state required for subsequent steps, multi-agent systems tend to struggle. This is because important context can get lost or fragmented as information is passed between agents. In contrast, a single agent maintains a seamless understanding of the evolving situation, ensuring that no critical details are missed or compressed during the process.
Tasks with many tools, like web search, file retrieval, or coding, suffer most from multi-agent overhead. The researchers say splitting the token budget leaves individual agents too little capacity for complex tool use.
Capability saturation matters too. Once a single agent hits about 45 percent success rate, adding agents brings diminishing or negative returns. Coordination costs eat up any gains, according to the researchers.
Error accumulation is the third problem. Without information sharing, errors compound up to 17 times faster than with a single agent. Mistakes pass through unchecked. A central coordinator helps; errors "only" increase by a factor of four, but the problem doesn't go away.
The key rule of thumb: if a single agent solves more than 45 percent of a task correctly, multi-agent systems usually aren't worth it. Multiple agents only help when tasks divide cleanly. For tasks needing around 16 different tools, single agents or decentralized setups work best.
Model providers showed slight differences. OpenAI did well with hybrid architectures, Anthropic with centralized ones. Google proved most consistent across all multi-agent setups.
The researchers also built a framework that correctly predicts the best coordination strategy for 87 percent of new configurations, what they call "a quantitatively predictive principle of agentic scaling based on measurable task properties."
The researchers tracked tasks completed per token budget. Single agents averaged 67 successful tasks per 1,000 tokens. Centralized multi-agent systems managed just 21; less than a third. Hybrid teams completed only 14 tasks per 1,000 tokens.
The culprit is coordination overhead. Hybrid systems need about six times more reasoning turns than single agents. The researchers recommend three to four agents maximum when budgets are tight.
For developers, the message is simple: start with a single agent. Only switch to multi-agent systems when the task splits into independent pieces and single-agent success stays below 45 percent.
Subscribe to THE DECODER for ad-free reading, a weekly AI newsletter, our exclusive "AI Radar" frontier report six times a year, full archive access, and access to our comment section. 



