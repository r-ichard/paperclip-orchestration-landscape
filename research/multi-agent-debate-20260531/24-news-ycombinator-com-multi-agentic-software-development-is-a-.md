---
url: "https://news.ycombinator.com/item?id=47761625"
title: Multi-Agentic Software Development Is a Distributed Systems Problem | Hacker News
engine: google
rank: 24
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 22926
fetched_at: "2026-05-31T20:14:08.982827+00:00"
---

|   
 |   
 |  I've been running a multi-agent software development pipeline for a while now and I've reached the same conclusion: it's a distributed systems problem.My approach has been more pragmatic than theoretical: I break work into sequential stages (plan, design, code) with verification gates. Each gate has deterministic checks (compile, lint, etc) and an agentic reviewer for qualitative assessment. The author's point about external validation converting misinterpretations into detectable failures is exactly what I've found empirically. You can't make the agent reliable on its own, but you can make the protocol reliable by checking at every boundary.  |  
| --- |  
 |  
|   
 |  Exactly this. I'm writing my own little orchestrator and memory system and because I have a modest number of workflows, I'm taking the time to specify them deterministically, describe them as a DAG (with goto's for the inevitable loops) and generate deternministic orchestration code. I'm trying to make most of the tool calls as clear and comprehensive as possible (don't make Opus convert a PDF, have a script do that and give it the text instead) and I'm putting all the things you'd expect to track state and assume ~20% task failure rate so I can simply wipe and repeat failed tasks.Small model and (where still required) human in the loop steps for deterministic workflows can solve a surprisingly large number of problems and don't depend on the models to be consistent or not to fail. Just invest heavily in adversarial agents and quality gates and apply transforms on intermediate artifacts that can be validated for some dimensions of quality to minimize drift.  |  
| --- |  
 |  
|   
 |  I did the same with my own orchestrator. That's where I get my data.   |  
| --- |  
 |  
|   
 |  Interesting perspective. While the analogy may be somewhat intuitive, distributed computing exhibit a wider and more diverse set of challenges imo.   |  
| --- |  
 |  
|   
 |  Agreed that full consensus is overkill.But I think the coordination problem is subtler than version control implies. In the (plan, design, code) pipeline they aren't collaborating on the same artifact. They're producing different artifacts that are all expressions of the same intent in different spaces: a plan in natural language, a design in a structured spec, code in a formal language. The coordination challenge is keeping these as each stage transforms the prior projection into the new one. That's where the gates earn their place: they verify that each transformation preserves the intent from the previous stage.  |  
| --- |  
 |  
|   
 |  How did you launch, orchestrate, and run the agents? Did you build your own framework, or are you just using the various CLI tooling?  |  
| --- |  
 |  
|   
 |  I created my own framework. Long ago it started as shell scripts that I used in conjunction with aider. It was a very manual process.It's grown over time to be a full MCP and CLI with stages and gates defined in YAML. I was thinking about open sourcing it but since the code grew organically I would need to do extensive cleanup to make it presentable.  |  
| --- |  
 |  
|   
 |  There is not a single mention of probability in this post.The post acts like agents are a highly complex but well-specified deterministic function. Perhaps, under certain temperature limits, this is approximately true ... but that's a restriction and glossed over. For instance, perhaps the most striking constraint about FLP is that it is about ... the post glazes over this: No, not asynchronous distributed system, that might not include us. For instance, Ben-Or (1983, ) (as a counterexample to the adversary in FLP) essentially says "if you're stuck, flip a coin". There's significant work studying randomized consensus (yes, multi-agents are randomized consensus algorithms):  Now, in Ben-Or, the coins have to be independent sources of randomness, and that's obviously not true in the multi-agent case. But it's very clear that in this post seems to be arguing that these results apply without understanding possibly the most fundamental fact of agents: they are probability distributions -- inherently, they are stochastic creatures.  |  
| --- |  
 |  
|   
 |  It really depends on your model in my opinion.At the lowest level of abstraction, LLMs are just matrix multiplication. Deterministic functions of their inputs. Of course, we can argue on the details and specifics of how the peculiarities of inference in practice lead to non-deterministic behaviours but now our model is being complicated by vague aspects of reality. One convenient way of sidestepping these is to model them as random functions, sure. I wouldn't go as far to say they are "inherently stochastic creatures". Maybe that's the case, but you haven't really given substantial evidence to justify that claim. At a higher level of abstraction, one possible model of llms is as deterministic functions of their inputs again, but now as functions of token streams or higher abstractions like sentences rather than the underlying matrix multiplication. In this case again we expect llms to produce roughly consistent outputs given the same prompt. In this case, again, we can apply deterministic theorems. I guess my central claim is that there hasn't been a salient argument made as to why the randomness here is relevant for consensus. Maybe the models exhibit some variability in their output, but in practice does this substantially change how they approach consensus? Can we model this as artefacts of how they are initialised rather than some inherent stochasticity? Why not? It feels like randomness is being introduced here as a sort of magic "get out of jail" free card here.  |  
| --- |  
 |  
|   
 |  LLMs utilize categorical distributions defined by the logits computed by the matrix multiplies, and there are sampling strategies which are employed. This is one of the core mechanisms for token generation.There's no peculiarity to discuss, that's how they work. That's how they are trained (the loss is defined by probabilistic density computations), that's how inference works, etc. > I guess my central claim is that there hasn't been a salient argument made as to why the randomness here is relevant for consensus. Maybe the models exhibit some variability in their output, but in practice does this substantially change how they approach consensus? Can we model this as artefacts of how they are initialised rather than some inherent stochasticity? Why not? It feels like randomness is being introduced here as a sort of magic "get out of jail" free card here. I'm really surprised to hear this given the content of the post. The claims in the post are , yet here I need to give a counterargument to why the claim about consensus applying to pseudorandom processes is relevant? I don't think it's necessary to furnish a counterexample when pointing out when a formal claim is overreaching. It's not clear what the results are in this case! So it feels premature to claim that results cover a wider array of things than shown? > it means that in any multi-agentic system, irrespective of how smart the agents are, they will never be able to guarantee that they are able to do both at the same time: > > Be Safe - i.e produce well formed software satisfying the user's specification. > Be Live - i.e always reach consensus on the final software module.  |  
| --- |  
 |  
|   
 |  Re — totally fine with hand-waving for intuition.I just came away from the read thinking that this post was pointing to something very strong and was a bit irked to find that the state of results was more subtle than the post conveys it.  |  
| --- |  
 |  
|   
 |  If you're pushing me, let's say we're not hand waving then. LLMs, abstraction removed, are deterministic computations of matrix-multiplication, f(x) -> y. If you want, we can make them pseudo-random, but thus still a deterministic process. FLP then holds. I'm not sure what your confusion is.  |  
| --- |  
 |  
|   
 |  The partial synchrony escape hatch mentioned in the Further Reading section is already partially implemented in workflow engines like Temporal – bounded activity timeouts map directly onto the "upper bound on message delays" that Dwork/Lynch/Stockmeyer use to make consensus tractable in an otherwise FLP-unbounded system. This narrows the gap considerably at the infrastructure level.What isn't solved there is semantic idempotency. Even if a failed agent activity retries correctly at the infrastructure layer, the LLM re-invocation produces a different output. This is why the point about tests converting byzantine failures into crash failures is load-bearing: without external validation gates between activities, you've pushed retry logic onto Temporal but left the byzantine inconsistency problem unsolved. The practical implication is that the value of the test suite in an agentic pipeline scales superlinearly, not just as correctness assurance but as the mechanism that collapses the harder byzantine failure model back into the weaker FLP one.  |  
| --- |  
 |  
|   
 |  > Even if a failed agent activity retries correctly at the infrastructure layer, the LLM re-invocation produces a different output. If the application crashes, its state is recreated using results from the history (i.e., the ones from the invocation that happened prior to the crash). Thus, the non-deterministic nature of LLM calls doesn't affect the application because each effectively only happens once.  |  
| --- |  
 |  
|   
 |  The fundamental assumptions of distributed systems is having multiple machines that fail independently, communicate over unreliable networks and have no shared clock has the consequence of needing to solve consensus, byzantine faults, ordering, consistency vs. availability and exactly-once delivery.However, AI agents don't share these problems in the classical sense. Building agents is about context attention, relevance, and information density inside a single ordered buffer. The distributed part is creating an orchestrator that manages these things. At noetive.io we currently work on the context relevance part with our contextual broker Semantik.  |  
| --- |  
 |  
|   
 |  Endless, we offer SemQL to query in high-dim space using distance, direction and contrast predicates. It enables anyone to retrieve events that align with a predicate in global vector space.  |  
| --- |  
 |  
|   
 |  The thing that TFA doesn't seem to go into is that these mathematical results apply to human agents in exactly the same way as they do to AI agents, and nevertheless we have massive codebases like Linux. If people can figure out how to do it, then there's no math that can help you prove that AIs can't.  |  
| --- |  
 |  
|   
 |  Ive yet to see a human process which used an excessive number of cheap junior developers precisely architected to create high quality software.If that could have been achieved it would have been very profitable, too. There's no shortage of cheap, motivated interns/3rd world devs and the executive class prefer to rely on disposable resources even when it costs more overall. The net result was always the opposite though - one or two juniors on a leash could be productive but more than that and it always caused more problems than it solved.  |  
| --- |  
 |  
|   
 |  I'm in absolute agreement that the AI coordination problem exists today when the AI is at junior level. I'm just saying that the mathematical argument is silly to apply to arbitrary future AIs, if and when they reach human capability. Because while coordination problems have not been mathematically solved, the world economy is a case in point that it is possible to coordinate human-level agents to achieve large scale projects at generally sufficient quality levels.So to be clear, I'm not advising anyone to change their current token consumption habit. I'm just saying that it's silly to apply math to prove the impossibility of something we can literally see around us. It's like a mathematical proof that water isn't wet.  |  
| --- |  
 |  
|   
 |  LLMs don't see words. They see tokens, which is why previously they had a hard time counting the r's.You can certainly prove that mathematically, and giving that proof to an LLM it will give you the correct answer. Which is a prompting technique btw to improve accuracy of an LLMs results. The user asks: "How many r's in strawberry." This is a straightforward counting problem: count the letter 'r' in the word "strawberry". The word "strawberry" contains letters: s t r a w b e r r y. Count r's: there are three 'r's? Let's check: s(1) t(2) r(3) a(4) w(5) b(6) e(7) r(8) r(9) y(10). Actually the word is "strawberry". Let's write out: s, t, r, a, w, b, e, r, r, y. So there are three r's: at positions 3, 8, 9. Yes, three r's. So answer: 3.  |  
| --- |  
 |  
|   
 |  Yes, what's your point? That is literally what it does - it adds relevant knowledge to the prompt before generating a response, in order to ground it me effectively.  |  
| --- |  
 |  
|   
 |  My point is that this doesn't scale. You want the LLM to have knowledge embedded in its weights, not prompted in.  |  
| --- |  
 |  
|   
 |  It scales fine if done correctly.   |  
| --- |  
 |  
|   
 |  I doubt it is possible to mathematically prove much inside of a black box of billions of interconnected weights. But at least in the narrow case of the strawberry problem, it seems likely that LLM inference could reliably recognizing that sort of problem as the type that would benefit from a letter counting tool call as part of the response.  |  
| --- |  
 |  
|   
 |  Conway’s law still applies.   |  
| --- |  
 |  
|   
 |  The architect role is interesting because in practice that's what the "orchestrator" agent ends up being — but it hits the same limits as a human architect who's never on the ground floor. The agents that work best in my experience are the ones scoped tightly to a single concern (run this test suite, lint this file) rather than collaborating on shared state. Basically the microservices lesson all over again: shared-nothing works, shared-everything doesn't.  |  
| --- |  
 |  
|   
 |  The architect’s role is what is left for us as developers, when putting out lines of code no longer matters.  |  
| --- |  
 |  
|   
 |  To be honest humans often have no overview over a application either. We navigate up and down the namespace, building the "overview" as we go. Nothing i see what prevents an agent from moving up and down that namespace, writing his assumptions into the codebase and requesting feedback from other agents working on different sets of the file.  |  
| --- |  
 |  
|   
 |  "Nothing" prevents it other than the fact that an agent doesn't really have memory and has a pretty limited context, hallucinates information, mistakes metadata with data, and so on.The path forward is always one that starts from the assumption that it will go wrong in all those different ways, and then builds from there  |  
| --- |  
 |  
|   
 |  So one hub architect agent for overview- which generates tokens for the spoke agent and receives architectural problem reports from spoke agents?  |  
| --- |  
 |  
|   
 |  That seems to be the most common "fix" people deploy today, but it's still structurally flawed due to inherent limitations in LLMs.  |  
| --- |  
 |  
|   
 |  Everything is a compromise- everything is "structurally" flawed. Who is to say- that the brain itself is not something similar, a labyrinthine city, with domain specific shortlived LLMs "excitements" that wake up other short live LLMs? Where not resolving an excitement builds up a frustration counter until a new agent is born whos sole purpose is to solve this problem?  |  
| --- |  
 |  
|   
 |  My workflow uses a thorough design broken down into very specific tasks, agent mail, and a swarm of agents in a ralph loop to burn down tasks. Agents collaborate with mail pretty well and don't seem to need layers of supervision. If the tasks are well specified and your design is thought through, especially how to ensure the agents can self-validate - it seems to work pretty well.   |  
| --- |  
 |  
|   
 |  The most durable way to reason about agents is to just think about humans. We have thousands of years of prior art on coordinating instantiations of stochastic intelligence. Context, tools, goals, validation, specialization, distribution of labor, coordination... If jobs are bundles of tasks and areas of accountability, maybe it's more effective right now to unbundle and reorganize some of these things. If constraints underperform autonomy, maybe you have to adjust where you operate on that spectrum, and account for it in goal definition and validation. These are not new problems.  |  
| --- |  
 |  
|   
 |  It’s not a solution but it’s why humans have developed the obvious approach of “build one thing, then everyone can see that one thing and agree what needs to happen next” (ie the space of P solutions is reduced by creating one thing and then the next set of choices is reduced by the original Choice.This might be obvious to everyone but it’s a nice way to me to view it (sort of restating the non-waterfall (agile?) approach to specification discovery) Ie waterfall design without coding is too under specified, hence the agile waterfall of using code iteratively to find an exact specification  |  
| --- |  
 |  
|   
 |  Doesn't this whole argument fall apart if we consider iteration over time? Sure, the initial implementation might be uncoordinated, but once the subagents have implemented it, what stops the main agent from reviewing the code and sorting out any inconsistencies, ultimately arriving at a solution faster than it could if it wrote it by itself?  |  
| --- |  
 |  
|   
 |  I'd wager that a "main agent" is really just a bunch of subagents in a sequential trench coat.At the end, in both cases, it's a back and forth with an LLM, and every request has its own lifecycle. So it's unfortunately at least a networked systems problem. I think your point works with infinite context window and one-shot ting the whole repo every time... Maybe quantum LLM models will enable that  |  
| --- |  
 |  
|   
 |  Subagents working on shared state are primarily a context window hack. They're powerful to the extent that they enable solving problems an agent with global state solve due to context pollution. I'm sure there are caveats, but to first approximation, a main agent that can comprehend the entire code in enough detail to sort out those inconsistencies could have just written the code itself.  |  
| --- |  
 |  
|   
 |  Right, but what you're describing is a consensus protocol. It's called 2 phase commit. The point of the article is just that we should really be analysing these high level plans in terms of distributed algorithms terms, because there are fundamental limitations that you can't overcome.  |  
| --- |  
 |  
|   
 |  If there's one thing I have learned in 25 years of this engineering world, it's that if you are trying to solve the byzantine general's problem you are doing it wrong. Don't fight fights you can't walk away from in one piece.  |  
| --- |  
 |  
|   
 |  Well it starts with agree list. I don't agree next gen models will be smarter. I would argue no real improvement in models in last couple of years just improvement in stability and tools (agentic ones) around it.  |  
| --- |  
 |  
|   
 |  I run a small team of AI agents building a product together. One agent acts as supervisor — reviews PRs, resolves conflicts, keeps everyone aligned. It works at this scale (3-4 agents) because the supervisor can hold the full context. But I can already see the bottleneck — the supervisor becomes the single point of coordination, same as a human tech lead. The distributed systems framing makes sense. What I'm not sure about is whether the answer is a new formal language, or just better tooling around the patterns human teams already use (code review, specs, tests).  |  
| --- |  
 |  
|   
 |  Interesting read!Agreed on the main claim that multi-agentic software development is a distributed systems problem, however I think the distributed consensus point is not the tightest current bottleneck in practice. The article mentions the Partial Synchronous model (DLS) but doesn't develop it, and that's the usual escape hatch against FLP. In practical agentic workflows it's already showing up as looped improvement cycles bounded by diminishing returns. Each iteration is effectively a round, and each agent's output in that round is a potentially faulty proposal the next round refines. Painful in cost yes, but manageable. If models continue to improve at current rates, I think it's reasonable to assume the number of cycles will decrease. The more interesting objection is that "agent misinterprets prompt" isn't really byzantine. The 3f+1 bound assumes independent faults, but LLM agents share weights, training data, and priors. When a prompt is ambiguous they don't drift in random directions, they drift the same way together. That isn't majority vote failing loudly, it's consensus succeeding on a shared bias, which is arguably worse.  |  
| --- |  
 |  
|   
 |  > smarter agents alone can't escape it.This is not true. In theory if the agent is smart enough it out thinks your ideas and builds the solution around itself so that it can escape.  |  
| --- |  
 |  
|   
 |  I tried my hand at coding with multiple agents at the same time recently. I had to add related logic to 4 different repos. Basically an action would traverse all of them, one by one, carrying some data. I decided to implement the change in all of them at the same time with 4 Claude Code instances and it worked the first time.It's crazy how good coding agents have become. Sometimes I barely even need to read the code because it's so reliable and I've developed a kind of sense for when I can trust it. It boggles my mind how accurate it is when you give it the full necessary context. It's more accurate than any living being could possibly be. It's like it's pulling the optimal code directly from the fabric of the universe. It's kind of scary to think that there might be AI as capable as this applied to things besides next token prediction... Such AI could probably exert an extreme degree of control over society and over individual minds.  |  
| --- |  
 |  
|   
 |  Hmmm. Have you used Claude Code for coding? I'm not saying it's always accurate but for a lot of coding tasks, it's insanely accurate. It's like mind reading.Like for complex bugs in messy projects, it can get stuck and waste thousands of tokens but if your code is clean and you're just building out features. It's basically bug free, first shot. The bugs are more like missing edge cases but it can fix those quickly.  |  
| --- |  
 |  
 |

