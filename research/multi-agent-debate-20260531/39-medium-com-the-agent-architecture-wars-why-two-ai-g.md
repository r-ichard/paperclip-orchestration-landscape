---
url: "https://medium.com/@maureesewilliams/the-agent-architecture-wars-why-two-ai-giants-completely-disagree-on-multi-agent-systems-d19a53364200"
title: "The Agent Architecture Wars: Why Two AI Giants Completely Disagree on Multi-Agent Systems | by Maureese Williams | Medium"
engine: brave
rank: 39
published: "2025-06-17T16:43:12Z"
updated: "2025-06-17T16:43:12Z"
author: Maureese Williams
org: Medium
char_count: 6890
fetched_at: "2026-05-31T20:20:49.186885+00:00"
---

The AI community just witnessed something fascinating: two of the most respected teams in agentic AI published completely contradictory philosophies on the same day. Cognition, the team behind Devin, declared “Don’t Build Multi-Agents” while Anthropic detailed their sophisticated multi-agent research system that outperforms single agents by 90%.
This isn’t just an academic disagreement. These are battle-tested insights from teams shipping production agent systems to millions of users. So who’s right? Well, both actually — and understanding why reveals something profound about where agentic AI is heading.
Both teams converge on one critical insight: . As Walden Yan from Cognition puts it, “At the core of reliability is Context Engineering.” The Anthropic team echoes this, noting that “rapid growth in coordination complexity” becomes the primary challenge in multi-agent systems.
The Cognition team has learned some hard lessons. Their core principle is deceptively simple: . When they experimented with multi-agent systems for their Flappy Bird example, they discovered something troubling:
> _“Subagent 1 actually mistook your subtask and started building a background that looks like Super Mario Bros. Subagent 2 built you a bird, but it doesn’t look like a game asset and it moves nothing like the one in Flappy Bird.”_
This led to their second principle: . When agents work in isolation, they make assumptions that don’t align, creating integration nightmares that no amount of post-processing can fix.
Their solution? A single-threaded linear agent architecture that maintains continuous context. It’s not just about simplicity — it’s about reliability. As they put it, “You should by default rule out any agent architectures that don’t abide by these principles.”
Meanwhile, the Anthropic team took a different path. They recognized that research work involves “open-ended problems where it’s very difficult to predict the required steps in advance.” Their solution? An orchestrator-worker pattern with a lead agent coordinating specialized subagents.
Their results speak for themselves: over single-agent systems on research tasks. When tasked with identifying board members of all S&P 500 Information Technology companies, their multi-agent system succeeded where single agents failed.
The key insight from their team: . In their analysis, token usage alone explained 80% of performance variance. Multi-agent architectures effectively scale token usage for tasks that exceed single agent limits.

```
 :     ():        .lead_agent = LeadResearcher()        .subagents = []             ():        strategy = .lead_agent.plan(query)                         subtask  strategy.            agent = SubResearcher(                task=subtask,                tools=strategy.tools_for_task(subtask),                context=strategy.shared_context            )            .subagents.append(agent)                            results = await asyncio.gather(*[            agent.execute()  agent  .subagents        ])                 .lead_agent.synthesize(results)
```

Here’s where it gets interesting. Both teams acknowledge the economic reality: . Anthropic’s data shows agents use 4x more tokens than chat, and multi-agent systems use 15x more tokens than chats.
But this creates a natural selection pressure. Multi-agent systems only make sense when the value of the task justifies the increased cost. As the Anthropic team notes, “multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance.”
This economic lens explains why both approaches can coexist. For coding tasks where dependencies are tight and context sharing is critical, Cognition’s linear approach makes perfect sense. For research tasks involving heavy parallelization and information that exceeds single context windows, Anthropic’s orchestrated approach delivers superior results.
Both teams learned brutal lessons about production deployment. The Anthropic team discovered that “minor changes cascade into large behavioral changes,” while Cognition found that multi-agent coordination introduces fragility that compounds over time.
Cognition’s experience with Claude Code illustrates their philosophy perfectly. As of June 2025, Claude Code spawns subtasks but never does parallel work. Why? Because “the subtask agent lacks context from the main agent that would otherwise be needed to do anything beyond answering a well-defined question.”
Meanwhile, Anthropic built sophisticated systems for context compression, rainbow deployments, and graceful error handling specifically to make multi-agent systems production-ready.
This divergence reveals something profound about the maturation of agentic AI. We’re moving beyond one-size-fits-all solutions toward .



The most interesting insight? Both teams emphasize that for steering agent behavior. As Anthropic notes, “Since each agent is steered by a prompt, prompt engineering was our primary lever for improving these behaviors.”
This isn’t just about technical architecture. It’s about the fundamental question of how intelligence scales. As Anthropic observes, “Even generally-intelligent agents face limits when operating as individuals; groups of agents can accomplish far more.”
But Cognition’s counter-argument is equally compelling: coordination overhead can destroy the benefits of parallelization if the task structure doesn’t support it.
Both teams are probably building toward the same future — where systems automatically choose between linear and multi-agent approaches based on task characteristics. The question isn’t whether to build single or multi-agent systems. It’s how to build systems smart enough to know which approach to use when.
This evolution mirrors human organizations. Sometimes you need a focused individual contributor. Sometimes you need a coordinated team. The key is knowing which situation you’re in and having the tools to execute both approaches effectively.
The agent architecture wars aren’t really wars at all. They’re different solutions to different problems, and the future likely belongs to systems that can seamlessly transition between both approaches as the task demands.
As we continue to push the boundaries of what’s possible with agentic AI, these insights from teams shipping at scale become invaluable guideposts. Whether you’re building the next generation of coding assistants or research tools, the lessons are clear: understand your problem domain, respect the economics of intelligence, and never underestimate the complexity of making these systems reliable in production.
_Special thanks to Walden Yan and the Cognition team, as well as Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford and the broader Anthropic engineering team for sharing their insights from building production agent systems at scale._

