---
url: "https://www.cio.com/article/4143420/true-multi-agent-collaboration-doesnt-work.html"
title: True multi-agent collaboration doesn’t work | CIO
engine: google
rank: 5
published: March 17, 2026
updated: unknown
author: Grant Gross
org: CIO
char_count: 8629
fetched_at: "2026-05-31T20:10:34.416906+00:00"
---



##  Individual AI agents can be super reliable, but when grouped together they only appear to work well in concert, producing high failure rates. Chained orchestration may be the answer. 
Some AI advocates are selling a vision in which dozens of agents to solve complex problems with little to no human intervention. So far, that scenario is a myth.
AI agents can be effective when working one-by-one on separate tasks, but when grouped together to complete complex assignments, they fail most of the time, according to a .
Advocates envision a multi-agent future that will lead to huge efficiency gains and major cost savings, thanks to taking over many of the complex tasks human employees currently perform.
But most organizations deploying multiple agents for a single workflow actually separate them into individual agent silos assigned for specific tasks, handing off their work to an before another agent takes over.
True doesn’t work because agents suffer from the same organizational problems humans do, says organizational systems researcher and author . Agents ignore instructions from other agents, redo work others have already done, fail to delegate, and get stuck in planning paralysis, he says.
“AI systems fail for the same structural reasons as human organizations, despite the removal of every human-specific causal factor,” he writes in his recent research paper. “No career incentives. No ego. No politics. No fatigue. No cultural norms. No status competition. The agents were language models executing prompts. The dysfunction emerged anyway.”
Perhaps not surprisingly, the more agents are added to the mix and the more complex the organizational structure of the agents is, the more often they fail to deliver on their assigned tasks, says , head of engineering at luxury vacation rental service Wander.
McEntire tested agent outputs based on four organizational structures. When using a single agent to produce the outcome, the agents succeeded in 28 out of 28 attempts. Multiple agents in a hierarchical organization, with one agent assigning tasks to others, failed to deliver the correct outcome 36% of the time.
A approach, with agents working in a self-organized swarm, failed 68% of the time, and an 11-stage gated pipeline, or , never produced a good outcome. In fact, the gated pipeline consumed its entire budget for the project on five planning stages without producing a single line of implementation code.
“Every single experiment that I ran failed counterintuitively in exactly the way that it’s supposedly ostensibly designed not to,” McEntire says. “The pipeline went in circles. The hierarchy failed to delegate. The stigmergic system failed to coordinate, which is the whole point of stigmergy. The only one that succeeded reliably and consistently was the single agent.”
Long-standing organizational problems don’t go away when human shift work to AI agents, McEntire says. “The same patterns of failure that characterize human organizations — review thrashing, preference-based gatekeeping, governance conflicts, budget exhaustion through coordination failure — emerge in multi-agent AI systems with identical mathematical signatures,” he writes in his paper. “The substrate changes; the physics of coordination at scale remains constant.”
While it might be tempting to dismiss McEntire as a lone voice crying in the wilderness, several AI experts say they see similar results.
While building an AI agent platform at a former job, observed similar problems with agents working together. Single agents working on discrete, well-scoped tasks are reliable, but often fails, says Sanyal, now principal engineer at cybersecurity vendor CrowdStrike.
“Failure rates climb fast as complexity increases, exactly as the study found,” he adds. “The coordination overhead, context passing, and error propagation between agents mirrors human organizational dysfunction at scale.”
“Threat detection, alert enrichment, and automated containment work best as discrete, well-scoped modules chained via orchestration layers,” he says. “It looks like multi-agent cooperation from the outside but architecturally, it’s sequential specialization with deterministic handoffs and human checkpoints built in.”
Visions of dozens of agents autonomously collaborating without human intervention isn’t happening yet, he adds. “The real value of AI agents today is automating repetitive, well-defined tasks at scale — augmenting human analysts with rapid data processing and consistent outputs,” Sanyal says. “Not emergent collective intelligence.”
McEntire’s paper shows how common human communication problems transfer to multi-agent environments, says , principal engineer and platform architect working on multi-agent coordination and agentic system design at Cisco.
“Every handoff between systems is a place where meaning gets lost, context gets compressed, and assumptions get made,” he says. “Humans deal with this in organizations by walking over to someone’s desk and saying, ‘Wait, what did you actually mean by that?’ Agents don’t have hallway conversations.”
IT leaders deploying agents should focus on single agents focused on well-scoped tasks, which create “stunningly reliable” results, Kale adds.
“The marketing pitch of ‘dozens of agents working together autonomously’ is selling a fantasy that violates information theory,” he says. “You don’t let agents collaborate. You let agents deliver to a spec, and you let a thin orchestration layer assemble the results.”
Multi-agent systems should start with either a single, highly structured agent working on a specialized task, or multiple agents operating within strict boundaries, shared context models, and evaluation controls, adds , CEO at AI-based app building vendor Empromptu.ai.
“The idea that dozens of agents can spontaneously collaborate without supervision or boundaries is as crazy as humans doing it,” she says. “The value of AI agents is real, but it’s not in autonomous swarm behavior. It’s in controlled specialization.”
Workforce orchestration vendor Asymbl has deployed more than 150 agents, but their interactions with one another are highly controlled, says , chief digital labor and technology officer at the company.
“Our 150-plus digital workers interact, hand off work, and collectively deliver outcomes we’ve designed around them, and they are coordinating with each other and their human teammates because we built an orchestration layer around them,” he says. “Before two AI agents interact, we have mapped the handoff — what data passes between them, in what format, under what conditions, what triggers a human review and why.”
An orchestration model controlling agents and defining each agent’s role before deployment are key pieces of the puzzle, he adds.
“We have AI agents specifically for discrete tasks and agents with shared memory and shared task lists to keep track of what the other agents are doing,” Devinarayanan says. “The key in both cases: clarity of role before deployment. What is this digital worker responsible for, where does the work come from, where does it go, and when does a human need to make a call?”
McEntire’s study confirms what Asymbl has seen, that the failure of multi-agent systems is an organizational and orchestration problem, not a technological one, he adds.
“The study found that agents suffer from the same coordination failures humans do when working together,” Devinarayanan says. “Agents are modeled on human reasoning. They inherit human organizational failure modes when the organizational design is weak.”
Vendors or AI advocates championing dozens of agents working together without human intervention are pushing the wrong vision, he adds.
“The right mental model is a hybrid workforce: digital workers with clear roles, human workers with oversight and judgment, and an orchestration layer connecting both,” Devinarayanan says.
Grant Gross, a senior writer at CIO, is a long-time IT journalist who has focused on AI, enterprise technology, and tech policy. He previously served as Washington, D.C., correspondent and later senior editor at IDG News Service. Earlier in his career, he was managing editor at Linux.com and news editor at tech careers site Techies.com. As a tech policy expert, he has appeared on C-SPAN and the giant NTN24 Spanish-language cable news network. In the distant past, he worked as a reporter and editor at newspapers in Minnesota and the Dakotas. A finalist for Best Range of Work by a Single Author for both the Eddie Awards and the Neal Awards, Grant was recently recognized with an ASBPE Regional Silver award for his article “.” 





