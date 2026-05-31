---
url: "https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/"
title: "Towards a science of scaling agent systems: When and why agent systems work"
engine: google
rank: 4
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 7086
fetched_at: "2026-05-31T20:10:28.499281+00:00"
---

Through a controlled evaluation of 180 agent configurations, we derive the first quantitative scaling principles for AI agent systems, revealing that multi-agent coordination dramatically improves performance on parallelizable tasks but degrades it on sequential ones; we also introduce a predictive model that identifies the optimal architecture for 87% of unseen tasks.
AI agents — systems capable of reasoning, planning, and acting — are becoming a common paradigm for real-world AI applications. From to , the industry is shifting from single-shot question answering to sustained, multi-step interactions. While researchers have long utilized established metrics to optimize the accuracy of traditional machine learning models, agents introduce a new layer of complexity. Unlike isolated predictions, agents must navigate sustained, multi-step interactions where a single error can cascade throughout a workflow. This shift compels us to look beyond standard accuracy and ask: How do we actually design these systems for optimal performance?
Practitioners often rely on heuristics, such as the assumption that "", believing that adding specialized agents will consistently improve results. For example, "" reported that LLM performance scales with agent count, while found that multi-agent collaboration "...often surpasses each individual through collective reasoning."
In our new paper, “”, we challenge this assumption. Through a large-scale controlled evaluation of 180 agent configurations, we derive the first quantitative scaling principles for agent systems, revealing that the "more agents" approach often hits a ceiling, and can even degrade performance if not aligned with the specific properties of the task.
To understand how agents scale, we first defined what makes a task "agentic". Traditional static benchmarks measure a model's knowledge, but they don't capture the complexities of deployment. We argue that tasks require three specific properties:
We evaluated five canonical architectures: one single-agent system (SAS) and four multi-agent variants (independent, centralized, decentralized, and hybrid) across four diverse benchmarks, including (financial reasoning), (web navigation), (planning), and (tool use). The agent architectures are defined as follow:


_Summary of the five canonical agent architectures evaluated in this study, including their computational complexity, communication overhead, and coordination mechanisms._ k n r d p m _= average peer requests per round. Communication overhead counts inter-agent message exchanges. Independent offers maximal parallelization with minimal coordination. Decentralized uses sequential debate rounds. Hybrid combined orchestrator control with directed peer communication._
To quantify the impact of model capabilities on agent performance, we evaluated our architectures across three leading model families: OpenAI GPT, Google Gemini, and Anthropic Claude. The results reveal a complex relationship between model capabilities and coordination strategy. As shown in the figure below, while performance generally trends upward with more capable models, multi-agent systems are not a universal solution — they can either significantly boost or unexpectedly degrade performance depending on the specific configuration.
_Performance comparison across three major model families (OpenAI GPT, Google Gemini, Anthropic Claude) showing how different agent architectures scale with model intelligence, where multi-agent systems can either boost or degrade performance depending on the configuration._
The results below compare the performance of the five architectures across different domains, such as web browsing and financial analysis. The box plots represent the accuracy distribution for each approach, while the percentages indicate the relative improvement (or decline) of multi-agent teams compared to the single-agent baseline. This data highlights that while adding agents can drive massive gains in parallelizable tasks, it can often lead to diminishing returns — or even performance drops — in more sequential workflows.
_Task-specific performance showing that multi-agent coordination yields substantial gains on parallelizable tasks like Finance-Agent (+81%) while degrading performance on sequential tasks like PlanCraft (-70%)._
On parallelizable tasks like financial reasoning (e.g., distinct agents can simultaneously analyze revenue trends, cost structures, and market comparisons), centralized coordination improved performance by 80.9% over a single agent. The ability to decompose complex problems into sub-tasks allowed agents to work more effectively.
Conversely, on tasks requiring strict sequential reasoning (like planning in PlanCraft), every multi-agent variant we tested degraded performance by 39-70%. In these scenarios, the overhead of communication fragmented the reasoning process, leaving insufficient "cognitive budget" for the actual task.
We identified a "tool-coordination trade-off". As tasks require more tools (e.g., a coding agent with access to 16+ tools), the "tax" of coordinating multiple agents increases disproportionately.
Perhaps most important for real-world deployment, we found a relationship between architecture and reliability. We measured , the rate at which a mistake by one agent propagates to the final result.
_Comprehensive metrics across architectures reveal that centralized systems achieve the best balance between success rate and error containment, while independent multi-agent systems amplify errors by up to 17.2x._
We found that independent multi-agent systems (agents working in parallel without talking) amplified errors by 17.2x. Without a mechanism to check each other's work, errors cascaded unchecked. Centralized systems (with an orchestrator) contained this amplification to just 4.4x. The orchestrator effectively acts as a "validation bottleneck", catching errors before they propagate.
Moving beyond retrospection, we developed a predictive model (^2 = 0.513) that uses measurable task properties like tool count and decomposability to predict which architecture will perform best. This model correctly identifies the optimal coordination strategy for 87% of unseen task configurations.
This suggests we are moving toward a new science of agent scaling. Instead of guessing whether to use a swarm of agents or a single powerful model, developers can now look at the properties of their task, specifically its sequential dependencies and tool density, to make principled engineering decisions.
As foundational models like Gemini continue to advance, our research suggests that smarter models don't replace the need for multi-agent systems, they accelerate it, but only when the architecture is right. By moving from heuristics to quantitative principles, we can build the next generation of AI agents that are not just more numerous, but smarter, safer, and more efficient.
_We would like to thank our co-authors and collaborators from Google Research, Google DeepMind, and academia for their contributions to this work._
  * 


