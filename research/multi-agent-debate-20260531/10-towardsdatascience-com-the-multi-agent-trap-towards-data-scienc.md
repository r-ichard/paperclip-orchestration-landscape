---
url: "https://towardsdatascience.com/the-multi-agent-trap/"
title: The Multi-Agent Trap | Towards Data Science
engine: google
rank: 10
published: "2026-03-14T15:00:00+00:00"
updated: unknown
author: Kaushik Rajan
org: Towards Data Science
char_count: 19098
fetched_at: "2026-05-31T20:11:28.575242+00:00"
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



Adding more AI agents makes most systems worse. Three architecture patterns separate the $60M wins from the 40% that get canceled. 
has handled . That’s the workload of 700 full-time human agents. Resolution time dropped from 11 minutes to under 2. Repeat inquiries fell 25%. Customer satisfaction scores climbed 47%. Cost per service transaction: $0.32 down to $0.19. Total savings through late 2025: roughly .
Here’s the other side. by the end of 2027. Not scaled back. Not paused. Canceled. Escalating costs, unclear business value, and inadequate risk controls.
If you’re building a multi-agent system (or evaluating whether you should), the gap between these two stories contains everything you need to know. This playbook covers three architecture patterns that work in production, the five failure modes that kill projects, and a framework comparison to help you choose the right tool. You’ll walk away with a pattern selection guide and a pre-deployment checklist you can use on Monday morning.
The intuition feels solid. Split complex tasks across specialized agents, let each one handle what it’s best at. Divide and conquer.
In December 2025, a Google DeepMind team led by Yubin Kim . They ran 180 configurations across 5 agent architectures and 3 Large Language Model (LLM) families. The finding should be taped above every AI team’s monitor:
When agents are thrown together without structured topology (what the paper calls a “bag of agents”), each agent’s output becomes the next agent’s input. Errors don’t cancel. They cascade.
Picture a pipeline where Agent 1 extracts customer intent from a support ticket. It misreads “billing dispute” as “billing inquiry” (subtle, right?). Agent 2 pulls the wrong response template. Agent 3 generates a reply that addresses the wrong problem entirely. Agent 4 sends it. The customer responds, angrier now. The system processes the angry reply through the same broken chain. Each loop amplifies the original misinterpretation. That’s the 17x effect in practice: not a catastrophic failure, but a quiet compounding of small errors that produces confident nonsense.
The same study found a saturation threshold: coordination gains plateau beyond 4 agents. Below that number, adding agents to a structured system helps. Above it, coordination overhead consumes the benefits.
This isn’t an isolated finding. The study, published in March 2025, analyzed 1,642 execution traces across 7 open-source frameworks. Failure rates ranged from 41% to 86.7%. The largest failure category: coordination breakdowns at 36.9% of all failures.
The obvious counter-argument: these failure rates reflect immature tooling, not a fundamental architecture problem. As models improve, the compound reliability issue shrinks. There’s truth in this. Between January 2025 and January 2026, single-agent task completion rates improved significantly ( showed the best agents reaching 24% on complex office tasks, up from near-zero). But even at 99% per-step reliability, the compound math still applies. Better models shift the curve. They don’t eliminate the compound effect. Architecture still determines whether you land in the 60% or the 40%.
> You started with agents that succeed 19 out of 20 times. You ended with a system that fails nearly two-thirds of the time.
Token costs compound too. A document analysis workflow consuming 10,000 tokens with a single agent requires 35,000 tokens across a 4-agent implementation. That’s a 3.5x cost multiplier before you account for retries, error handling, and coordination messages.
Flip the question. Instead of asking “how many agents do I need?”, ask: “how would I definitely fail at multi-agent AI?” The research answers clearly. By chaining agents without structure. By ignoring coordination overhead. By treating every problem as a multi-agent problem when a single well-prompted agent would suffice.
A capable model creates the complete plan. Cheaper, faster models execute each step. The planner handles reasoning; the executors handle doing.
This is close to what Klarna runs. A frontier model analyzes the customer’s intent and maps resolution steps. Smaller models execute each step: pulling account data, processing refunds, generating responses. The planning model touches the task once. Execution models handle the volume.
The cost impact: routing planning to one capable model and execution to cheaper models compared to using frontier models for everything.
Environments that change mid-execution. If the original plan becomes invalid halfway through, you need re-planning checkpoints or a different pattern entirely. This is a one-way door if your task environment is volatile.
A supervisor agent manages routing and decisions. Worker agents handle specialized subtasks. The supervisor breaks down requests, delegates, monitors progress, and consolidates outputs.
Google DeepMind’s research validates this directly. A centralized control plane suppresses the 17x error amplification that “bag of agents” networks produce. The supervisor acts as a single coordination point, preventing the failure mode where (for example) a support agent approves a refund while a compliance agent simultaneously blocks it.
Heterogeneous tasks requiring different specializations. Customer support with escalation paths, content pipelines with review stages, financial analysis combining multiple data sources.
When the supervisor becomes a bottleneck. If every decision routes through one agent, you’ve recreated the monolith you were trying to escape. The fix: give workers bounded autonomy on decisions within their domain, escalate only edge cases.
No supervisor. Agents hand off to each other based on context. Agent A handles intake, determines this is a billing issue, and passes to Agent B (billing specialist). Agent B resolves it or passes to Agent C (escalation) if needed.
OpenAI’s original Swarm framework was educational only (they said so explicitly in the README). Their production-ready Agents Software Development Kit (SDK), released in March 2025, implements this pattern with guardrails: each agent declares its handoff targets, and the framework enforces that handoffs follow declared paths.
High-volume, well-defined workflows where routing logic is embedded in the task itself. Chat-based customer support, multi-step onboarding, triage systems.
Complex handoff graphs. Without a supervisor, debugging “why did the user end up at Agent F instead of Agent D?” requires production-grade observability tools. If you don’t have distributed tracing, don’t use this pattern.
uses graph-based state machines. . Typed state schemas enable precise checkpointing and inspection. This is what Klarna runs in production. Best for stateful workflows where you need human-in-the-loop intervention, branching logic, and durable execution. The trade-off: steeper learning curve than alternatives.
organizes agents as role-based teams. 44,300 GitHub stars and growing. Lowest barrier to entry: define agent roles, assign tasks, and the framework handles coordination. Deploys teams roughly for straightforward use cases. The trade-off: limited support for cycles and complex state management.
provides lightweight primitives (Agents, Handoffs, Guardrails). The only major framework with equal Python and TypeScript/JavaScript support. Clean abstraction for the Swarm pattern. The trade-off: tighter coupling to OpenAI’s models.
Downloads don’t tell the whole story (CrewAI has more GitHub stars), but they’re the best proxy for production adoption. Image by the author.
One protocol worth knowing: has become the de facto interoperability standard for agent tooling. Anthropic donated it to the Linux Foundation in December 2025 (co-founded by Anthropic, Block, and OpenAI under the Agentic AI Foundation). Over 10,000 active public MCP servers exist. All three frameworks above support it. If you’re evaluating tools, MCP compatibility is table stakes.
If you’re unsure, start with Plan-and-Execute on LangGraph. It’s the most battle-tested combination. It handles the widest range of use cases. And switching patterns later is a reversible decision (a two-way door, in decision theory terms). Don’t over-architect on day one.
The MAST study identified 14 failure modes across 3 categories. The five below account for the majority of production failures. Each includes a specific prevention measure you can implement before your next deployment.
  1. Calculate your end-to-end reliability before you ship. Multiply per-step success rates across your full chain. If the number drops below 80%, reduce the chain length or add verification checkpoints. Keep chains under 5 sequential steps. Insert a verification agent at step 3 and step 5 that checks output quality before passing downstream. If verification fails, route to a human or a fallback path (not a retry of the same chain).
  2. When two agents receive ambiguous instructions, they interpret them differently. A support agent approves a refund; a compliance agent blocks it. The user receives contradictory signals. Explicit input/output contracts between every agent pair. Define the data schema at every boundary and validate it. No implicit shared state. If Agent A’s output feeds Agent B, both agents must agree on the format before deployment, not at runtime.
  3. Token costs multiply across agents (3.5x in documented cases). Retry loops can burn through $40 or more in Application Programming Interface (API) fees within minutes, with no useful output to show for it. Set hard per-agent and per-workflow token budgets. Implement circuit breakers: if an agent exceeds its budget, halt the workflow and surface an error rather than retrying. Log cost per completed workflow to catch regressions early.
  4. The Open Worldwide Application Security Project (OWASP) Top 10 for LLM Applications found prompt injection vulnerabilities in . In multi-agent systems, a compromised agent can propagate malicious instructions to every downstream agent. Input sanitization at every agent boundary, not just the entry point. Treat inter-agent messages with the same suspicion you’d apply to external user input. Run a red-team exercise against your agent chain before production launch.
  5. Agent A fails. It retries. Fails again. In multi-agent systems, Agent A’s failure triggers Agent B’s error handler, which calls Agent A again. The loop runs until your budget runs out. Maximum 3 retries per agent per workflow execution. Exponential backoff between retries. Dead-letter queues for tasks that fail past the retry limit. And one absolute rule: never let one agent trigger another without a cycle check in the orchestration layer.


> Prompt injection was found in 73% of production LLM deployments assessed during security audits. In multi-agent systems, one compromised agent can propagate the attack downstream.
In February 2026, the surveying nearly 6,000 executives across the US, UK, Germany, and Australia. The finding: 89% of firms reported zero change in productivity from AI. Ninety percent of managers said AI had no impact on employment. These firms averaged 1.5 hours per week of AI use per executive.
a resurrection of Robert Solow’s 1987 paradox: “You can see the computer age everywhere but in the productivity statistics.” History is repeating, forty years later, with a different technology and the same pattern.
The contrast with Klarna isn’t about better models or bigger compute budgets. It’s a structural choice. The 90% treated AI as a copilot: a tool that assists a human in a loop, used 1.5 hours per week. The companies seeing real returns (Klarna, Ramp, Reddit via Salesforce Agentforce) treated AI as a workforce: autonomous agents executing structured workflows with human oversight at decision boundaries, not at every step.
That’s not a technology gap. It’s an architecture gap. The opportunity cost is staggering: the same engineering budget producing zero Return on Investment (ROI) versus $60 million in savings. The variable isn’t spend. It’s structure.
Forty percent of agentic AI projects will be canceled by 2027. The other sixty percent will ship. The difference won’t be which LLM they chose or how much they spent on compute. It will be whether they understood three patterns, ran the compound reliability math, and built their system to survive the five failure modes that kill everything else.
Klarna didn’t deploy 700 agents to replace 700 humans. They built a structured multi-agent system where a smart planner routes work to cheap executors, where every handoff has an explicit contract, and where the architecture was designed to fail gracefully rather than cascade.
You have the same patterns, the same frameworks, and the same failure data. The playbook is open. What you build with it is the only remaining variable.


Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.
  *   *   *   *   *   *   * 

Some areas of this page may shift around if you resize the browser window. Be sure to check heading and document order.

