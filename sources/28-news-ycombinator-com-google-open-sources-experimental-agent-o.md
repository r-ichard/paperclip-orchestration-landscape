---
url: "https://news.ycombinator.com/item?id=47675213"
title: Google open-sources experimental agent orchestration testbed Scion | Hacker News
engine: duckduckgo
rank: 28
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 19698
fetched_at: "2026-05-31T17:39:02.724970+00:00"
---

|   
 |   
 |  I'm looking forward to trying this. I've had a positive but high-variance experience with Gastown[1], which is in the same genre. I hope that Scion does better.My main complaints with Gastown are that (1) it's expensive, partly because (2) it refuses to use anything but Claude models, in spite of my configuration attempts, (3) I can't figure out how to back up or add a remote to its beads/dolt bug database, which makes me afraid to touch the installation, and (4) upgrading it often causes yak shaving and lost context. These might all be my own skill issues, but I do RTFM. But wow, Gastown gets results. There's something magic about the dialogue and coordination between the mayor and the polecats that leads to an even better experience than Claude Code alone.  |  
| --- |  
 |  
|   
 |  As someone who hasn't yet jumped into working with multiple agents simultaneously, where does a tool like gastown help you the most?  |  
| --- |  
 |  
|   
 |  I'm trialing it on very silly things, like a economic simulator game in Rust/Bevy. I put in an entire road map document with inline specs and goals, wild milestones, with tasks like "working bid/ask spread when factories buy or sell on the market to make pricing dynamic and realistic", "political entities can set work conditions", "international trade has pricing dynamics that take into account currency interchange and tariff rates", "infrastructure for trade improves as trade volumes increase across given tiles".Out the other end over about 3-4 five-hour-sessions comes about 85% functional code for . I'd guess you'd be looking at a team for months, give or take, without the automation. Total cost was around $50 in VM time (not counting claude since I would be subscribed anyway) I'm not letting that thing anywhere near a computer I care about and rust compiles are resource intensive, so I paid for a nice VM that I could smash the abort button on if it started looking at me funny. So I liken it to buying an enormous bulldozer. If you're a skilled operator you can move mountains, but there'll still be a lot of manual work and planning involved. It's very clearly directionally where the industry will go once the models are improved and the harnesses and orchestration are more mature than "30% of the development effort is fixing the harness and orchestration itself", plus an additional "20% of your personal time will be knocking two robots heads together and getting them to actually do work" Edit: some more details of other knock on work - I asked for a complexity metadata field to automatically dispatch work to cheaper/faster models, set up harnesses to make opencode and codex work similarly to how claude works, troubleshot some bugs in the underlying gastown system. Gastown fork is public if you'd like to have a look.  |  
| --- |  
 |  
|   
 |  Does it deliver on the "realistic" part? My experience with most models is they make something that technically fulfills the ask, but often in a way that doesn't really capture my intent (this is with regular Claude Code though).  |  
| --- |  
 |  
|   
 |  Yep, garbage in garbage out, I had some additional specs beyond the summary above, everything requires refinement as well, but honestly I never thought I was going to have a simcity/civlike clone in a couple weekends that's reasonably playable.  |  
| --- |  
 |  
|   
 |  We ended up adding workflows with deterministic paths, that can use RAW API calls, CLIs, and agents. I think that was a big differential.We also added pi-mono, and started using more and more other models for different tasks (Gemini, K2.5, GLM-5, you name it). I think the problem is that most are building solutions that rely in one provider, instead of focusing self learning capabilities on improving the cost-quality-speed ratio.  |  
| --- |  
 |  
|   
 |  I made one similar harness, mine does lightweight sandboxing with Seatbelt on Mac and Bubblewrap on Linux. I initially used Docker too, but abandoned it. I like how these 2 sandboxes allow me to make all the file system r/o except the project folder which is r/w (and a few other config folders). This means my code runs inside the sandbox like outside, same paths hold, same file system. The .git folder is also r/o inside sandbox, only outside agent can commit. Sandboxing was intended to enable --yolo mode, I wanted to maximize autonomous time.Work is divided into individual tasks. I could have used Plan Mode or TodoWriter tool to implement tasks - all agents have them nowadays. But instead I chose to plan in task.md files because they can be edited iteratively, start as a user request, develop into a plan with checkbox-able steps, the plan is reviewed by judge agent (in yolo mode, and fresh context), then worker agent solves gates. The gates enforce a workflow of testing soon, testing extensively. There is another implementation judge again in yolo mode. And at the end we update the memory/bootstrap document. Task files go into the git repo. I also log all user messages and implement intent validation with the judge agents. The judges validate intent along the chain "chat -> task -> plan -> code -> tests". Nothing is lost, the project remembers and understands its history. In fact I like to run retrospective tasks where a task.md 'eats' previous tasks and produces a general project perspective not visible locally. In my system everything is a md file, logged and versioned on git. You have no issue extracting your memories, in fact I made reflection on past work a primitive operation of this harness. I am using it for coding primarily, but it is just as good for deep research, literature reviews, organizing subject matter and tutoring me on topics, investment planning and orchestrating agent experiment loops like autoresearch. That is because the task.md is just a generic programming pipeline, gates are instructions in natural language, you can use it for any cognitive work. Longest task.md I ran was 700 steps, took hours to complete, but worked reliably.  |  
| --- |  
 |  
|   
 |  Scion looks interesting, as a “hypervisor for agents”. It has Kubernetes influences, and a substrate for agent execution is a useful primitive.Gastown goes further than Scion in that it chains agents together into an ecosystem. My sense is that Gastown or similar could be built as a layer on top of Scion. Dan Shapiro helped shape my thinking on the two most important capabilities for agent orchestration as concurrency and loops. Scion provides concurrency only at present, and Gastown is also more concurrency-oriented than loops. Fabro is a new OSS project I am working on which attempts to do both loops and concurrency well: (Maybe someday it should be built on top of Scion.)  |  
| --- |  
 |  
|   
 |  Really interesting to see Google's approach to this. Recently I shared my approach, Optio, which is also an Agent Orchestration platform: I was much more focused on integrating with ticketing systems (Notion, Github Issues, Jira, Linear), and then having coding agents specifically work towards merging a PR. Scion's support for long running agents and inter-container communication looks really interesting though. I think I'll have to go plan some features around that. Some of their concepts, make less sense to me, I chose to build on top of k8s whereas they seem to be trying to make something that recreates the control plane. Somewhat skeptical that the recreation and grove/hub are needed, but maybe they'll make more sense once I see them in action the first time.  |  
| --- |  
 |  
|   
 |  The documentation mentions OAuth configuration, but doesn't list Claude Code as a harness that supports this. Just to confirm my understanding, does this mean that the only authentication and therefore billing method for Claude is API key, which means you get billed at the API rate, not toward your subscription usage?  |  
| --- |  
 |  
|   
 |  The "isolation over constraints" framing is interesting. Scion enforces safety at the infrastructure layer, letting agents operate freely inside containers while controlling what they can reach on the outside. That is a runtime approach.We have been exploring a different layer for the same problem. ARIA (aria-ir.org) is an intermediate representation designed for AI-authored code. Instead of constraining the agent at runtime, it constrains what the agent produces at the representation level. Functions must declare effects, intent annotations are mandatory and verifiable, and the compiler enforces memory safety at compile time before anything executes. The two approaches are not mutually exclusive. Scion handles what the agent can reach. ARIA handles what the agent generates. A system that uses both would have safety at the output layer and safety at the execution layer. Curious whether the Scion team has thought about what properties the code an agent produces should have, independent of how that agent is isolated.  |  
| --- |  
 |  
|   
 |  Exactly, I actually starred this in late March and hadn't made my way back to it yet. Glad somebody posted, looks very interesting.  |  
| --- |  
 |  
|   
 |  Isolation over constraints sounds like the right philosophy. Containers give you a boundary but not vis into what ran inside them. Curious how much execution context Scion surfaces, w/o that you're still in a position similar to the LiteLLM attack where something can run and cause damage before you know it happened.  |  
| --- |  
 |  
|   
 |  [primary author and architect of scion here] There are several layers of state and telemetry - first is provided by the hook system available in most harnesses, then for those that provide OpenTelemetry -that is normalized and forwarded raw (preserving both) to a cloud collector. Finally - some activities are "self reported" by agents using a built-in toolset that can be reflected in the control plane  |  
| --- |  
 |  
|   
 |  The failure mode most underrepresented in agent testbeds is cascading failure, what happens when individually correct agents interact in ways that produce collectively incorrect outcomes. Most testing focuses on individual agent behaviour.Does the testbed have a model for multi-agent state conflicts, can you simulate two agents concurrently modifying the same resource and observe the resolution behaviour?  |  
| --- |  
 |  
|   
 |  This looks really promising, I am curious about the choice to use containers as the isolation layer though. If the goal is to treat agents as untrusted and isolate them fully I feel like microVMs would be a better option.If it supports OCI runtimes though then maybe kata containers can be plugged in, I'll have to dig in after work and see.  |  
| --- |  
 |  
|   
 |  This seems to be in the direction of Gas Town but missing some of the core features. Having formulas has been game changing.  |  
| --- |  
 |  
|   
 |  [primary author and architect of scion here] The missing features are mostly by design - this is closer to what the gastown plans as "gascity" - bring your own orchestration characters and definition.   |  
| --- |  
 |  
|   
 |  I'm glad to see other projects like this. I did switch over to using Gascity, but it does still seem to have quite a few troubles. Does scion have a beads like concept using formulas for work?  |  
| --- |  
 |  
|   
 |  Oh Google, I love you guys, but it seems they alway launch these half baked things without the support they deserve behind it.ADK was (and is) exceptional, but nobody is actually making noise and pushing for it as they should. It feels like Microsoft .net back in the day.  |  
| --- |  
 |  
|   
 |  > This project is early and experimental. Core concepts are settled, but expect rough edges. Local mode: relatively stable - Hub-based workflows: ~80% verified - Kubernetes runtime: early with known rough edges   |  
| --- |  
 |  
|   
 |  I want to experiment more with agents but my employer only pays for Claude Code, and TOS disallows using the subscription API for other purposes. Anyone else in the same boat? Token based pricing also gets expensive fast.  |  
| --- |  
 |  
|   
 |  Look, a Google project that is actually using Go, although compiling everything from source all the time isn't really appealing.  |  
| --- |  
 |  
|   
 |  Their agent tooling is shaping up to be the well known issue of product cancellation. They have how many different takes on this now? (gemini-cli, antigravity, AI studio, this, Gemini app)I've not been impressed with any of them. I do use their ADK in my custom agent stack for the core runtime. That one I think is good and has legs for longevity. The main enterprise problem here is getting the various agent frameworks to play nice. How should one have shared runtimes, session clones, sandboxes, memory, etc between the tooling and/or employees?  |  
| --- |  
 |  
|   
 |  Not if you go custom, you have unlimited latitude, examples...I modified file_read/write/edit to put the contents in the system prompt. This saves context space, i.e. when it rereads a file after failed edit, even though it has the most recent contents. It also does not need to infer modified content from read+edits. It still sees the edits as messages, but the current actual contents are always there. My AGENTS.md loader. The agent does not decide, it's deterministic based on what other files/dirs it has interacted with. It can still ask to read them, but it rarely does this now. I've also backed the agents environment or sandbox with Dagger, which brings a number of capabilities like being able to drop into a shell in the same environment, make changes, and have those propagate back to the session. Time travel, clone/fork, and a VS Code virtual FS are some others. I can go into a shell at any point in the session history. If my agent deletes a file it shouldn't, I can undo it with the click of a button. I can also interact with the same session, at the same time, from VS Code, the TUI, or the API. Different modalities are ideal for different tasks (e.g. VS Code multi-diff for code review / edits; TUI for session management / cleanup).  |  
| --- |  
 |  
|   
 |  [primary author and architect of scion here] Actually - there are two other big parts: a CLI and a control plane  |  
| --- |  
 |  
|   
 |  I swore to not be burned by google ever again after TensorFlow. This looks cool, and I will give this to my Codex to chew on and explain if it fits (or could fit what I am building right now -- the msx.dev) and then move on. I don't trust Google with maintaining the tools I rely on.  |  
| --- |  
 |  
|   
 |  Agent orchestration is one side of the problem. The other side is: where does the data go?
```
  When agents process EU user data (names, emails, IBANs) and
  route it to US model providers, that's a GDPR violation.

  I open sourced a routing layer that detects PII in prompts and
  forces EU-only inference when personal data is found:
  https://github.com/mahadillahm4di-cyber/mh-gdpr-ai.eu
```
 |  
| --- |  
 |  
|   
 |  It's super neat! Just like Kubernetes is also super neat at what it can do. It's super neat primarily because consuming it is so , provided you already have all the same abstraction layers in place in your infra.You... have all the same abstraction layers, right? No? Oh. Well, don't worry, Google/Amazon/Microsoft can sell you those if you don't want to pay your IT staff to prop it up for you. Look, snark aside, yours is the correct take. Google's solutions are , but they're also built for an organization as large and complex as Google. Time will tell if this is an industry-standard abstraction (a la S3 APIs) or just a Google product for Google-like orgs/functions (a la K8s).  |  
| --- |  
 |  
|   
 |  [primary author and architect of scion here] Part of this will be pushing that cognitive overhead increasingly onto agents. By how much and when is what Scion is here to explore.  |  
| --- |  
 |  
|   
 |  I think most of the legacy companies that can benefit from Kubernetes don't use it, while most of the companies that are using it are startups doing it for the résumé.  |  
| --- |  
 |  
|   
 |  This is the exact opposite of my experience. Maybe it was true 10 years ago when K8s was new and trendy so many engineers wanted to try it out. Now it's just boring tech at large orgs.  |  
| --- |  
 |  
|   
 |  I'm proud to say I retired more k8s clusters than I created. And I've created 5 production ones, still in production.One that I retired was used for serving ftp(among other transfer stuff), ftp of all things, it needs to have ports open and routed back from the client. And for extra points they had the pods capped at 1 cpu. And I had to explain the thing to the perpetrator and their boss, madness.  |  
| --- |  
 |  
|   
 |  > One that I retired was used for serving ftp   |  
| --- |  
 |  
|   
 |  It's also much easier to bring online these days with managed offerings like GKE, EKS, and AKS.   |  
| --- |  
 |  
|   
 |  Slightly trailing off from your focus, but hopefully within the same sentiment (that k8s was good, albeit an exception)I would place Google ADK in alignment with Kubernetes more than this project, for the well designed abstractions, the controlplane, and handling the boring parts that every alternative will at maturity. I can see the agent framework ignorance to the container analogy about what's running inside. ADK lacks the ability to run any agent tool, but you can build most of this projects controlplane on top of it with minimal effort, most of the bookkeeping is there already. It's more about what experience you want to have.  |  
| --- |  
 |  
|   
 |  k8s is simple because it offload some key tasks to 3rd party like network and storage; it is not easy to: a) setup and maintain a k8s cluster with all necessary components from at least a dozen different sources b) design your application to be k8s native  |  
| --- |  
 |  
|   
 |  This. K8s is easy to consume, and a real PITA to actually setup and support from an IT perspective.If someone wants production K8s, I'm steering them (and their budget) to a managed control plane from one of the major cloud providers. Trying to prop it up locally when it hates having to work directly with bare metal does not spark joy.  |  
| --- |  
 |  
|   
 |  The same way linux isn't. It's easy to start, all the base modifications/configurations are fairly simple, and if you find yourself deep into custom ways of using it, it's open source and fairly well documented with a large community.  |  
| --- |  
 |  
|   
 |  [primary author and architect of scion here] The reason this is a testbed is because this is a new and emerging area of replacing things like codified graphs in tools like langraph with pure agent instruction where agents manage agents with a lot more autonomy. These patterns are not well explored, and are not ready for production in most cases. The goal of a testbed is to have an easy and quick way to try out N of these patterns.  |  
| --- |  
 |  
|   
 |  Anyone at the frontier is switching to jj. Btw your question is kind of offensive, as if there is a universal truth "who matters" and everyone else can be dismissed. Companies do not matter for sure, if that was your premise.  |  
| --- |  
 |  
|   
 |  jj will not achieve meaningful adoption until git interop is improved and there is a big enough win to change a core work tool. Lack of git-lfs is a blocker where I work and asking all the devs to change their git habits for a shop that doesn't use rebase (as I understand the main issue jj aims to make better)... the ROI just doesn't appear to be there.  |  
| --- |  
 |  
 |

