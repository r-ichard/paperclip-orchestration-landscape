---
url: "https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/"
title: "Why Your Multi-Agent System is Failing: Escaping the 17x Error Trap of the “Bag of Agents” | Towards Data Science"
engine: google
rank: 11
published: "2026-01-30T15:00:00+00:00"
updated: "2026-02-21T20:05:23+00:00"
author: Sean Moran
org: Towards Data Science
char_count: 33614
fetched_at: "2026-05-31T20:13:58.680095+00:00"
---

We use cookies to enhance your browsing experience, serve personalised ads or content, and analyse our traffic. By clicking "Accept All", you consent to our use of cookies.
We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.
The cookies that are categorised as "Necessary" are stored on your browser as they are essential for enabling the basic functionalities of the site. ... 
Necessary cookies are required to enable the basic features of this site, such as providing secure log-in or adjusting your consent preferences. These cookies do not store any personally identifiable data.
  * Cloudflare sets this cookie to track users across sessions to optimize user experience by maintaining session consistency and providing personalized services


  * This cookie is set by Hubspot whenever it changes the session cookie. The __hssrc cookie set to 1 indicates that the user has restarted the browser, and if the cookie does not exist, it is assumed to be a new session.


  * HubSpot sets this cookie to keep track of sessions and to determine if HubSpot should increment the session number and timestamps in the __hstc cookie.


  * WordPress sets this cookie when a user interacts with emojis on a WordPress site. It helps determine if the user's browser can display emojis properly.


  * This cookie is native to PHP applications. The cookie stores and identifies a user's unique session ID to manage user sessions on the website. The cookie is a session cookie and will be deleted when all the browser windows are closed.


  * The cookietest cookie is typically used to determine whether the user's browser accepts cookies, essential for website functionality and user experience.


  * Stripe sets this cookie for fraud prevention purposes. It identifies the device used to access the website, allowing the website to be formatted accordingly.


  * Marketo sets this cookie to collect information about the user's online activity and build a profile about their interests to provide advertisements relevant to the user. 


  * CookieYes sets this cookie to remember users' consent preferences so that their preferences are respected on subsequent visits to this site. It does not collect or store any personal information about the site visitors.


Functional cookies help perform certain functionalities like sharing the content of the website on social media platforms, collecting feedback, and other third-party features.
  * A cookie set by YouTube to measure bandwidth that determines whether the user gets the new or old player interface.


  * The cookie ytidb::LAST_RESULT_ENTRY_KEY is used by YouTube to store the last search result entry that was clicked by the user. This information is used to improve the user experience by providing more relevant search results in the future.


  * The yt-remote-session-app cookie is used by YouTube to store user preferences and information about the interface of the embedded YouTube video player.


  * The yt-remote-cast-available cookie is used to store the user's preferences regarding whether casting is available on their YouTube video player.


  * This cookie is set by the Reddit. The cookie enables the sharing of content from the website onto the social media platform.


Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics such as the number of visitors, bounce rate, traffic source, etc.
  * Hubspot set this main cookie for tracking visitors. It contains the domain, initial timestamp (first visit), last timestamp (last visit), current timestamp (this visit), and session number (increments for each subsequent session).


  * HubSpot sets this cookie to keep track of the visitors to the website. This cookie is passed to HubSpot on form submission and used when deduplicating contacts.


  * Google Analytics sets this cookie to calculate visitor, session and campaign data and track site usage for the site's analytics report. The cookie stores information anonymously and assigns a randomly generated number to recognise unique visitors.


  * GitHub sets this cookie for temporary application and framework state between pages like what step the user is on in a multiple step form.


  * This cookie is set by Segment to count the number of people who visit a certain site by tracking if they have visited before.



Performance cookies are used to understand and analyse the key performance indexes of the website which helps in delivering a better user experience for the visitors.


Advertisement cookies are used to provide visitors with customised advertisements based on the pages you visited previously and to analyse the effectiveness of the ad campaigns.


  * Twitter sets this cookie to integrate and share features for social media and also store information about how the user uses the website, for tracking and targeting.


  * Twitter sets this cookie to identify and track the website visitor. It registers if a user is signed in to the Twitter platform and collects information about ad preferences.


  * YouTube sets this cookie to manage feature rollout and experimentation. It helps Google control which new features or interface changes are shown to users as part of testing and staged rollouts, ensuring consistent experience for a given user during an experiment.


  * YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen.


  * YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen.


  * This cookie is set by the Reddit. This cookie is used to identify trusted web traffic. It also helps in adverstising on the website.


  * Reddit sets this cookie to save the information about a log-on Reddit user, for the purpose of advertisement recommendations and updating the content.



Most complex Multi-Agent Systems (MAS) can be decomposed into 10 fundamental archetypes. The secret to building robust, performant systems is the Topology of Coordination and not simply adding more agents to the task. By arranging these agents into functional planes, we transform a noisy “bag of agents” into a closed-loop system that suppresses error amplification. 
landed on arXiv just before Christmas 2025, very much an early present from the team at Google DeepMind, with the title I found this paper to be a genuinely useful read for engineers and data scientists. It’s peppered with concrete, measurement-driven advice, and packed with takeaways you can apply immediately. The authors run a large multi-factorial study, facilitated by the tremendous compute available at these frontier labs, to systematically varying key design parameters in order to really understand what drives performance in agentic systems.
Like many industry AI practitioners, I spend a lot of time building Multi-Agent Systems (MAS). This involves a taking complex, multi-step workflow and dividing it across a set of agents, each specialised for a specific task. While the dominant paradigm for AI chatbots is zero-shot, request-response interaction, Multi-Agent Systems (MAS) offer a more compelling promise: the ability to autonomously “divide and conquer” complex tasks. By parallelizing research, reasoning, and tool use, these systems significantly boost effectiveness over monolithic models.
To move beyond simple interactions, the DeepMind research highlights that MAS performance is determined by the interplay of four factors:


The suggests that MAS performance success is found at the intersection of . If we get the balance wrong we end up scaling noise rather than the results. This post will help you find that secret sauce for your own tasks in a way that will reliably help you build a performant and robust MAS that will impress your stakeholders.
A compelling recent success story of where an optimal balance was found for a complex task comes from , the AI-powered software development company behind a popular IDE. They describe using large numbers of agents working in concert to automate complex tasks over extended runs, including generating substantial amounts of code to build a web browser (you can see the code ) and translating codebases (e.g., from Solid to React). Their write-up on scaling agentic AI to difficult tasks over weeks of computation is a fascinating read.
Cursor report that prompt engineering is critical to performance, and the specific agent coordination architecture is key. In particular, they report better results with a structured planner–worker decomposition than with a flat swarm (or bag) of agents. The role of coordination is particularly interesting, and it’s an aspect of MAS design we’ll return to in this article. Much like real-world teams benefit from a manager, the Cursor team found that a hierarchical setup, with a planner in control, was essential. This worked far better than a free-for-all in which agents picked tasks at will. The planner enabled controlled delegation and accountability, ensuring worker agents tackled the right sub-tasks and delivered concrete project progress. Interestingly they also find that it’s important to match the right model to the right, finding that GPT-5.2 is the best planner and worker agent compared to Claude Opus 4.5.
However, despite this early glimpse of success from the Cursor team, Multi-Agent System development in the real world continues to be at the boundary of scientific knowledge and therefore a challenging task. Multi-Agent Systems can be messy with unreliable outputs, token budgets lost to coordination chatter, and performance that drifts, sometimes worsening instead of improving. Careful thought is required into the design, mapping it to the particulars of a given use-case.
> When developing a MAS, I kept coming back to the same questions: when should I split a step across multiple agents, and what criteria should drive that decision? What coordination architecture should I choose? With so many permutations of decomposition and agent roles, it’s easy to end up overwhelmed. Furthermore, how should I be thinking about the type of Agents available and their roles?
That gap between promise and reality is what makes developing a MAS such a compelling engineering and data science problem. Getting these systems to work reliably, and to deliver tangible business value, still involves a lot of trial, error, and hard-won intuition. In many ways, the field can feel like you’re operating off the beaten path, currently without enough shared theory or standard practice.
This paper by the DeepMind team helps a lot. It brings structure to the space and, importantly, proposes a quantitative way to predict when a given agent architecture is likely to shine and when it’s more likely to underperform.
> In the rush to build complex AI, most developers fall into the rap by throwing more LLMs at a problem and hoping for emergent intelligence. But as the recent research by DeepMind shows, a bag of agents isn’t an effective team, rather it can be a source of 17.2x error amplification. Without the and of a formal topology to constrain the agentic interaction, we end up scaling noise rather than an intelligent capability that is likely to solve a business task.
I’ve no doubt that mastering the standardised build-out of Multi-Agent Systems is the next great technical moat. Companies that can quickly bridge the gap between ‘messy’ autonomous agents and rigorous, plane-based topologies will reap the dividends of extreme efficiency and high-fidelity output at scale, bringing massive competitive advantages within their market.
> According to the DeepMind scaling research, multi-agent coordination yields the highest returns when a single-agent baseline is below 45%. If your base model is already hitting 80%, adding more agents might actually introduce more noise than value.
In this post I distill nuggets like the above into a playbook that provides you with the right mental map to build the best Multi-Agent Systems. You will find golden rules for constructing a Multi-Agent System for a given task, touching on what agents to build and how they should be coordinated. Further, I’ll define a set of ten core agent archetypes to help you map the landscape of capabilities and make it easier to choose the right setup for your use-case. I’ll then draw out the main design lessons from the DeepMind paper, using them to show how to configure and coordinate these agents effectively for different kinds of work.
In this section we will map out the design space of Agents, focusing on the overarching types available for solving complex tasks. Its useful to distill the types of Agents down into 10 basic types, following closely the definitions in the : , , , , and In my experience, almost all useful Multi-Agent Systems can be designed by using a mixture of these Agents connected together into a specific topology.
So far we have a loose collection of different agent types, it is useful if we have an associated mental reference point for how they can be grouped and applied. We can organize these agents through two complementary lenses: a static architecture of and a dynamic runtime cycle of . The way to think of this is that the control planes provide the structure, while the runtime cycle drives the workflow:
  * The Orchestrator (Control Plane) defines the high-level objective and constraints. It delegates to the Planner, which decomposes the objective into a task graph — mapping dependencies, priorities, and steps. As new information surfaces, the Orchestrator sequences and revises this plan dynamically.
  * The Executor translates abstract tasks into tangible outputs (artifacts, code changes, decisions). To ensure this work is grounded and efficient, the Retriever (Context Plane) supplies the Executor with just-in-time context, such as relevant files, documentation, or prior evidence.
  * This is the quality gate. The Evaluator validates outputs against objective acceptance criteria, while the Critic probes for subjective weaknesses like edge cases or hidden assumptions. Feedback loops back to the Planner for iteration. Simultaneously, the Monitor watches for systemic health — tracking drift, stalls, or budget spikes — ready to trigger a reset if the cycle degrades.

This diagram represents a . Instead of asking one AI to “do everything,” this design splits the cognitive load into specialised roles (archetypes), similar to how a software engineering team works. image by author.
As illustrated in our (Figure 2), these specialised agents are situated within , which group capabilities by functional responsibility. This structure transforms a chaotic “Bag of Agents” into a high-fidelity system by compartmentalising information flow.
  * Think of this as the Project Manager. It holds the high-level objective. It does not write code or search the web; its job is to delegate. It decides does next.
  * This is the “Health & Safety” officer. It watches the Orchestrator. If the agent gets stuck in a loop, burns too much money (tokens), or drifts away from the original goal, the Monitor pulls the emergency brake or triggers an alert.


  * This is the “To-Do List.” It is dynamic — as the agent learns new things, steps might be added or removed. The Planner constantly updates this graph so the Orchestrator knows the candidate next steps.


  * The Archivist. Not everything needs to be remembered. This role summarizes (compresses) what happened and decides what is important enough to store in the for the long term.


  * The Editor. The Executor’s output might be messy or too verbose. The Synthesiser cleans it up and formats it into a clear result for the Orchestrator to review.


  * Checks for subjective risks or edge cases. (e.g., “This code runs, but it has a security vulnerability,” or “This logic is flawed.”)
  * Notice the dotted lines going back up to the Planner in Figure 2. If the Assurance layer fails the work, the agent updates the plan to fix the specific errors found.


  * Sometimes the Evaluator says “Pass” but the Critic says “Fail.” Or perhaps the Planner wants to do something the Monitor flags as risky. The Mediator acts as the tie-breaker to prevent the system from freezing in a deadlock.

Moving beyond a “Bag of Agents” requires a structured division of labor. This taxonomy maps 10 core archetypes into functional planes (Control, Planning, Context, Execution, Assurance, and Mediation). Each role acts as a specific “Architecture Defense” against the common failure modes of scaling, such as error amplification, logic drift, and tool-coordination overhead. table by author.
To see these archetypes in action, we can trace a single request through the system. Imagine we submit the following objective: The request doesn’t just go to a “worker”; it triggers a choreographed sequence across the functional planes.
The Orchestrator receives the objective. It checks its “guardrails” (e.g., “Do we have permission to scrape? What is the budget?”).
  * starts a “stopwatch” and a “token counter” to ensure the agent doesn’t spend $50 trying to scrape a $5 site.


The Planner realises this is actually four sub-tasks: (1) Research the site structure, (2) Write the scraper, (3) Map the data schema, (4) Write the DB ingestion logic.
  * It populates the Task Graph / Backlog with these steps and identifies dependencies (e.g., you can’t map the schema until you’ve researched the site).



  * The Synthesiser might take that raw code and wrap it in a “Status Update” for the Orchestrator, saying 


  * runs the code. It fails because of a error (anti-scraping bot). It sends a Dotted Arrow back to the Planner: 
  * looks at the code and sees that the database password is hardcoded. It sends a Dotted Arrow to the Planner: 


Imagine the Planner tries to fix the Critic’s security concern, but the Evaluator says the new code now breaks the DB connection. They are stuck in a loop.
  * The Mediator steps in, looks at the two conflicting “opinions,” and decides:  _“Prioritize the security fix; I will instruct the Planner to add a specific step for Debugging the DB Connection specifically.”_


  * The Memory Keeper summarises the “403 Forbidden” encounter and stores it in the Context Store so that next time the agent is asked to scrape a site, it remembers to use header-rotation from the start.


In the same way we defined common Agent archetypes, we can undertake a similar exercise for their tools. Tool archetypes define how that work is grounded, executed, and verified and which failure modes are contained as the system scales.
Ten tool archetypes that underpin reliable multi-agent systems, grouped by functional plane (Context, Planning, Control, Execution, Assurance). Each tool type acts as an “architecture defence,” containing common scaling failure modes such as hallucination, thrashing, runaway cost, unsafe actions, and silent correctness errors. image by author.
As we cover in Figure 5 above, retrieval tools can prevent hallucination by forcing evidence; schema validators and test harnesses prevent silent failures by making correctness machine-checkable; budget meters and observability prevent runaway loops by exposing (and constraining) token burn and drift; and permission gates plus sandboxes prevent unsafe side effects by limiting what agents can do in the real world.
Before exploring the Scaling Laws of Agency, it is instructive to define the currently stalling most agentic AI deployments and that we aim to improve upon: the “Bag of Agents.” In this naive setup, developers throw multiple LLMs at a problem without a formal topology, resulting in a system that typically exhibits three fatal characteristics:
  * Every agent has an open line to every other agent. There is no hierarchy, no gatekeeper, and no specialized planes to compartmentalize information flow.
  * Without an Orchestrator, agents descend into circular logic or “hallucination loops,” where they echo and validate each other’s mistakes rather than correcting them.
  * Information flows unchecked through the group. There is no dedicated Assurance Plane (Evaluators or Critics) to verify data before it reaches the next stage of the workflow.


To use a workplace analogy: the jump from a “Bag” to a “System” is the same leap a startup makes when it hires its first manager. Early-stage teams quickly realize that headcount does not equal output without an organizational structure to contain it. As Brooks put it in The Mythical Man-Month, “Adding manpower to a late software project makes it later.”
The answer lies in the from the DeepMind paper. This research uncovers the precise mathematical trade-offs between adding more LLM “brains” and the growing friction of their coordination.
The Science of Scaling Agent Systems’ paper’s core discovery is that cranking up the agent quantity is not a silver bullet for higher performance. Rather there exists a rigorous trade-off between coordination overhead and task complexity. Without a deliberate topology, adding agents is like adding engineers to a project without an orchestrating manager: you typically don’t get more valuable output; you will likely just get more meetings, undirected and potentially wastful work and noisy chatter.
Comparative analysis of Single-Agent Systems (SAS) versus Centralized and Decentralized Multi-Agent Systems (MAS). The data illustrates the “Coordination Tax” where accuracy gains begin to saturate or fluctuate as agent quantity increases. This highlights the necessity of a structured topology to maintain performance beyond the 4-agent threshold. Kim, Y., et al. (2025). “ arXiv preprint.
The DeepMind team evaluated their Multi-Agent Systems across four task suites and tested the agent designs across very different workloads to avoid tying the conclusions to a specific tasks or benchmark:
  * Web browsing / information retrieval, framed as multi-website information location — a test of search, navigation, and evidence gathering.
  * Planning and tool selection for common business activities — tests whether agents can pick tools/actions and execute practical workflows.


Five coordination topologies are examined in : a Single-Agent System (SAS)and four Multi-Agent System (MAS) designs — Independent, Decentralised, Centralised, and Hybrid. Topology matters because it determines whether adding agents buys useful parallel work or just buys more communication.
  * Many agents work in parallel, then outputs are synthesised into a final answer. Strong for breadth (research, ideation), weaker for tightly coupled reasoning chains.
  * Agents debate over multiple rounds and decide via majority vote. This can improve robustness, but communication grows quickly and errors can compound through repeated cross-talk.
  * A single Orchestrator coordinates specialist sub-agents. This “manager + team” design is typically more stable at scale because it constrains chatter and contains failure modes.
  * Central orchestration plus targeted peer-to-peer exchange. More flexible, but also the most complex to manage and the easiest to overbuild.

A visual comparison of the architectures studied in Single-Agent (SAS), Independent MAS (parallel workers + synthesis), Decentralized MAS (multi-round debate + majority vote), Centralized MAS (orchestrator coordinating specialist sub-agents), and Hybrid MAS (orchestrator plus targeted peer-to-peer messaging). The key takeaway is that topology determines whether scaling agents increases useful parallel work or mainly increases coordination overhead and error propagation.. image by author via GPT-5.2.
This framing also clarifies why unstructured “bag of agents” designs can be very dangerous. Kim et al. report up to 17.2× error amplification in poorly coordinated networks, while centralised coordination contains this to ~4.4× by acting as a circuit breaker.
  * On (highly decomposable financial reasoning), MAS delivers the biggest gains — Centralised +80.8%, Decentralised +74.5%, Hybrid +73.1% over SAS — because agents can split the work into parallel analytic threads and then synthesise.
  * On (dynamic web navigation and synthesis), improvements are modest and topology-sensitive: Decentralised performs best (+9.2%), while Centralised is essentially flat (+0.2%) and Independent can collapse (−35%) due to unchecked propagation and noisy cross-talk.
  * sits in the middle, showing only marginal movement (~−11% to +6% overall; Decentralised +5.7%), suggesting a near-balance between orchestration benefit and coordination tax.
  * And on (strictly sequential, state-dependent planning), every MAS variant degrades performance (~−39% to −70%), because coordination overhead consumes budget without providing real parallel advantage.


> The practical antidote is to impose some structure in your MAS by mapping agents into functional planes and using central control to suppress error propagation and coordination sprawl.
  * Unstructured networks amplify errors exponentially. Our Centralized Control Plane (the Orchestrator) suppresses this by acting as a single point of verification.
  * More tools require more grounding. Our Context Plane (Retriever) ensures agents don’t “guess” how to use tools, reducing the noise that leads to overhead.
  * Agent coordination yields the highest returns when single-agent performance is low. As models get smarter, we must lean on the Monitor Agent to simplify the topology and avoid unnecessary complexity.

The Agent architecture design space as a series of filters. Without them, the system is (errors escape). With them, the system is (errors are recycled into improvements). table by author.
In my experience the Assurance layer is often the biggest differentiator to improving MAS performance. The “Assurance → Planner” loop transforms our MAS from an Open-Loop (fire and forget) system to a Closed-Loop (self-correcting) system that contains error propagation and allowing intelligence to scale to more complex tasks.
The DeepMind team explicitly test heterogeneous teams, in other words a different base LLM for the Orchestrator than for the sub-agents, and mixing capabilities in decentralised debate. The lessons here are very interesting from a practical standapoint. They report three main findings (shown on BrowseComp-Plus task/dataset):


a weak orchestrator can become a bottleneck in some families, even if the workers are strong (because it’s the routing/synthesis chokepoint).
  * Mixed-capability decentralised debate is near-optimal or sometimes better than homogeneous high-capability baselines (they give examples: OpenAI 0.53 vs 0.50; Anthropic 0.47 vs 0.37; Gemini 0.42 vs 0.43).


The practical overall key message from the DeepMind team is that if you’re spending money selectively, spend it on the workers (the agents producing the substance), not necessarily on the manager but validate on your model family because the “cheap orchestrator + strong workers” pattern did not generalise uniformly.
A frequently asked question is how to define the cost of a MAS i.e., the token budget that ultimately translates into dollars. Topology determines whether adding agents buys parallel work or simply buys more communication. To make cost concrete, we can model it with a small set of knobs:


  * is driven by rounds × fan-out, i.e. how many times we re-coordinate (r, d, p) multiplied by how many messages are exchanged (n, m) — plus the hidden tax of agents having to all that extra context.


To convert this into dollars, first use the knobs () to estimate total input/output tokens generated and consumed, then multiply by your model’s per-token price:
This is why decentralised and hybrid topologies can get expensive very fast: debate and peer messaging inflate both message volume context length, so we pay twice as agents generate more text, and everyone has to read more text. In practice, once agents begin broadly communicating with each other, coordination can start to feel closer to an n² effect.
> The key takeaway is that agent scaling is only helpful if the task gains more from parallelism than it loses to coordination overhead. We should use more agents when the work can be cleanly parallelised (research, search, independent solution attempts). Conversely we should be cautious when the task is sequential and tightly coupled (multi-step reasoning, long dependency chains), because extra rounds and cross-talk can break the logic chain and turn “more agents” into “more noise.”
A natural question is whether multi-agent systems have “architecture scaling laws,” analogous to the empirical scaling laws for LLM parameters. Kim et al. argue the answer is yes. To tackle the combinatorial search problem — topology × agent count × rounds × model family — they evaluated 180 configurations across four benchmarks, then trained a predictive model on coordination traces (e.g., efficiency vs. overhead, error amplification, redundancy). The model can forecast which topology is likely to perform best, reaching R² ≈ 0.513 and selecting the best coordination strategy for ~87% of held-out configurations. The practical shift is from “try everything” to running a small set of short probe configurations (much cheaper and faster), measure early coordination dynamics, and only then commit full budget to the architectures the model predicts will win.
In this post, we reviewed DeepMind’s Towards a Science of Scaling Agent Systems and distilled the most practical lessons for building higher-performing multi-agent systems. These design rules helps us avoid poking around in the dark and hoping for the best. The headline takeaway is that more agents is not a guaranteed path to better results. Agent scaling involves real trade-offs, governed by measurable scaling laws, and the “right” number of agents depends on task difficulty, the base model’s capability, and how the system is organised.
  * Adding agents does not produce indefinite gains. In many experiments, performance rises initially, then plateaus — often around ~4 agents — after which additional agents contribute little.
  * Extra agents help most when the base model performs poorly on the task (below ~45%). When the base model is already strong, adding agents can trigger capability saturation, where performance stagnates or becomes noisy rather than improving.
  * More agents shine on parallelisable tasks (e.g., broad research), where they can materially increase coverage and throughput. But for sequential reasoning, adding agents can degrade performance as the “logic chain” weakens when passed through too many steps.
  * Every additional agent adds overhead. More messages, more latency, more opportunities for drift. If the task isn’t complex enough to justify that overhead, coordination costs outweigh the benefits of extra LLM “brains”.


With these in mind, I want to end by wishing you the best in your MAS build-out. Multi-Agent Systems sit right at the frontier of current applied AI, primed to bring the next level of business value in 2026 — and they come with the kinds of technical trade-offs that make this work genuinely interesting: balancing capability, coordination, and design to get reliable performance. In building your own MAS you will undoubtedly discover Golden Rules of your own that expand our knowledge over this uncharted territory.
A final thought on DeepMind’s “45%” threshold: multi-agent systems are, in many ways, a workaround for the limits of today’s LLMs. As base models become more capable, fewer tasks will sit in the low-accuracy regime where extra agents add real value. Over time, we may need less decomposition and coordination, and more problems may be solvable by a single model end-to-end, as we move toward artificial general intelligence (AGI).
  * — A large controlled study deriving quantitative scaling principles for agent systems across multiple coordination topologies, model families, and benchmarks (including saturation effects and coordination overhead).
  * — A comprehensive survey that maps the agent design space (planning, memory, tools, interaction patterns), useful for grounding your 10-archetype taxonomy in prior literature.
  * — A framework paper on programming multi-agent conversations and interaction patterns, with empirical results across tasks and agent configurations.
  * — A clean template for closed-loop improvement: agents reflect on feedback and store “lessons learned” in memory to improve subsequent attempts without weight updates.
  * — Practical documentation covering common multi-agent patterns and how to structure interaction so you can avoid uncontrolled “bag of agents” chatter.
  * — A focused overview of orchestration features that matter for real systems (durable execution, human-in-the-loop, streaming, and control-flow).
  * — The reference implementation for a graph-based orchestration layer, useful if readers want to inspect concrete design choices and primitives for stateful agents.
  * — The classic coordination lesson (Brooks’s Law) that translates surprisingly well to agent systems: adding more “workers” can increase overhead and slow progress without the right structure.


Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.
  *   *   *   *   *   *   * 

Some areas of this page may shift around if you resize the browser window. Be sure to check heading and document order.

