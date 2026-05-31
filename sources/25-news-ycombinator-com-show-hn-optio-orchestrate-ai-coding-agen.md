---
url: "https://news.ycombinator.com/item?id=47520220"
title: "Show HN: Optio – Orchestrate AI coding agents in K8s to go from ticket to PR | Hacker News"
engine: duckduckgo
rank: 25
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 16261
fetched_at: "2026-05-31T17:38:38.327942+00:00"
---

|   
 | I think like many of you, I've been jumping between many claude code/codex sessions at a time, managing multiple lines of work and worktrees in multiple repos. I wanted a way to easily manage multiple lines of work and reduce the amount of input I need to give, allowing the agents to remove me as a bottleneck from as much of the process as I can. So I built an orchestration tool for AI coding agents:Optio is an open-source orchestration system that turns tickets into merged pull requests using AI coding agents. You point it at your repos, and it handles the full lifecycle: The key idea is the feedback loop. Optio doesn't just run an agent and walk away — when CI breaks, it feeds the failure back to the agent. When a reviewer requests changes, the comments become the agent's next prompt. It keeps going until the PR merges or you tell it to stop.  |  
| --- |  
|   
 |  I’ve come to the realization that these kind of systems don’t work, and that a human in the loop is crucial for task planning; the LLM’s role being to identify issues, communicate the design / architecture, etc before it’s handed off, otherwise the LLM always ends up doing not entirely the correct thing.How is this part tackled when all that you have is GH issues? Doesn’t this work only for the most trivial issues?  |  
| --- |  
 |  
|   
 |  I've come to the opposite conclusions: The big limitation of systems like this is starting and ending with human involvement at the same level, instead of directing at a higher level. You end up quibbling over detail the agents can handle themselves with sufficient guardrails and process, instead of setting higher level requirements and reviewing higher level decisions and outcomes, and dealing with exceptions.You can afford a of extra guardrails and process to ensure sufficient quality when the result is a system that gets improved autonomously 24/7. I'm on my way home from a client, and meanwhile another project has spent the last 10 hours improving with no involvement from me. I spent a few minutes reviewing things this morning, after it's spent the whole night improving unattended.  |  
| --- |  
 |  
|   
 |  I don't believe comments like this. Sure it did work for ten hours but if you didn't review it you will sooner or later when it breaks. And it will. I run the agents all day and that's what happens - they do stuff that is unwanted but that you aren't aware of.  |  
| --- |  
 |  
|   
 |  I find that that doesn’t work in the long run. Software agents are not yet capable of maintaining a decently active repository for extended periods of time.I am all for delegating everything to AI agents, but it just becomes a mess over time if you don’t steer things often enough.  |  
| --- |  
 |  
|   
 |  Not my experience at all. If anything, they make it cheap enough to deal with tech debt that it is far easier to justify being strict.EDIT: I'll add that you can't expect it to , but you can let it manage . We don't expect e.g. a product manager to dictate how developers deliver the code, just what the acceptance criteria is, and that's where I'm headed.  |  
| --- |  
 |  
|   
 |  Had the same realization which inspired eforge (shameless plug) - planning stays in the developer’s control with all engineering (agent orchestration) handed off to eforge. This has been working well for a solo or siloed developer (me) that is free to plan independently. Allows the developer to confidently stay in the planning plane while eforge handles the rest using a methodology that in my experience works well. Of course, garbage in garbage out - thorough human planning (AI assisted, not autonomous) is key.  |  
| --- |  
 |  
|   
 |  I like the separation of planning and execution. I think the right set of artifacts to pass on to the execution will evolve but may be it's different for different types of work.From the project: "The plugin enqueues the input and a daemon picks it up - planning, building, reviewing, and validating autonomously." The part that is not clear to me (and causes most problems for me) is the "validating". It makes a mistake, or decides mocking an interface is fine, etc. declares success and moves on to the next. The bigger the project the more small mistakes compound. It sounds like the agent is doing the validation. What's the approach here for validation?  |  
| --- |  
 |  
|   
 |  To me that doesn't do enough yet in terms of up-front planning and visualization, but it's a step in the right direction. I prefer Traycer myself.  |  
| --- |  
 |  
|   
 |  Hadn’t seen Traycer, that looks really polished. An important difference is that eforge is open source (Apache 2.0). I purposefully left out planning features from eforge because I don’t want the same tool that builds my code to force me into a planning methodology. Our role as developers has shifted heavily into planning (offloading implementation), and I’m still getting comfortable with that and want to be free to explore the planning space. Maybe I’ll change my mind after my planning opinions evolve.  |  
| --- |  
 |  
|   
 |  Maybe - I do think as the model get better they'll be able to handle more and more difficult tasks. And yet, even if they can only solve the simplest issues now, why not let them so you can focus on the more important things?  |  
| --- |  
 |  
|   
 |  FWIW, a "cheaper" version of this is triggering Claude via GitHub Actions and `@claude`ing your agents like that. If you run your CI on Kubernets (ARC), it sounds pretty much the same  |  
| --- |  
 |  
|   
 |  The feedback loop is what most people miss when they build these systems. You spin up the agent, it submits a PR, CI goes red, and suddenly you're back to being the bottleneck you were trying to eliminate.One thing I ran into building something similar, agents are surprisingly good at fixing the exact error message they're given, but terrible at recognizing when they're going in circles. After the third retry on the same failing test, you're not getting a fix, you're getting increasingly creative excuses for why the test is wrong. How deep does the self-healing go? Is there a retry limit before it escalates, or does it just keep going until you manually intervene?  |  
| --- |  
 |  
|   
 |  I'm working on something a little similar but mines more a dev tool vs process automation but I love where yours is headed. The biggest issue I've run into is handling retries with agents. My current solution is I have them set checkpoints so they can revert easily and when they can't make an edit or they can't get a test passing, they just restart from earlier state. Problem is this uses up lots of tokens on retries how did you handle this issue in your app?  |  
| --- |  
 |  
|   
 |  Generally I've found agents are capable of self correcting as long as they can bash up against a guardrail and see the errors. So in optio the agent is resumed and told to fix any CI failures or fix review feedback.  |  
| --- |  
 |  
|   
 |  Looks cool, congrats on the launch. Is there any sandbox isolation from the k8s platform layer? Wondering if this is suitable for multiple tenants or customers.  |  
| --- |  
 |  
|   
 |  Oh good question, I haven't thought deeply about this.Right now nothing special happens, so claude/codex can access their normal tools and make web calls. I suppose that also means they could figure out they're running in a k8s pod and do service discovery and start calling things. What kind of features would you be interested in seeing around this? Maybe a toggle to disable internet connections or other connections outside of the container?  |  
| --- |  
 |  
|   
 |  Network policies controlling egress would be one thing. I haven't seen how you make secrets available to the agent, but I would imagine you would need to proxy calls through a mitm proxy to replace tokens with real secrets, or some other way to make sure the agent cannot access the secrets themselves. Specifically for an agent that works with code, I could imagine being able to run docker-in-docker will probably be requested at some point, which means you'll need gvisor or something.  |  
| --- |  
 |  
|   
 |  That's exactly what i did personnaly on my oss repo I want to run my agents fully isolated with headless mode. To achieve that safely you have to run a proxy  |  
| --- |  
 |  
|   
 |  The parallel execution model makes sense for independent tickets but I'm wondering what happens when agent A is halfway through a PR touching shared/utils.py and agent B gets assigned a ticket that needs the same file. Does the orchestrator do any upfront dependency analysis to detect that, or do you just let them both run and deal with the conflict at merge time?  |  
| --- |  
 |  
|   
 |  It's generally not worth it worrying about it too much other than at a very high level vs. letting them fight it out, as long as your test suite is good enough and your orchestrator is even moderately prepared to handle retries.  |  
| --- |  
 |  
|   
 |  I love k8s, but having it as a requirement for my agent setup is a non-starter. Kubernetes is one method for running, not the center piece.  |  
| --- |  
 |  
|   
 |  I wonder, based on your experience, how hard would it be to improve your system to have an AI agent review the software and suggest tickets?Like, can an AI agent use a browser, attempt to use the software, find bugs and create a ticket? Can an AI agent use a browser, try to use the software and suggest new features?  |  
| --- |  
 |  
|   
 |  I think it's more important to pin down where a human be in order for this not to become a mess. Or have we skipped that step entirely?  |  
| --- |  
 |  
|   
 |  Personally my theory is that to solve the messiness we will need some new frameworks and even languages that are designed to catch AI mistakes in large code bases. For example, AIs in the past would sometimes hallucinate methods that do not exist. But in a language with a strong type system a static type checker should be able to catch that mistake and give the AI automated feedback to fix that mistake without a human in the loop.As far as humans in the loop, the only human we ultimately cannot get rid of is the user. But I think with a combo of user feedback forms and automated metrics we can give AI a lot of feedback about how good software is just from users using the software.  |  
| --- |  
 |  
|   
 |  Yes, they can, and they do a reasonably good job at it. Hand them playwright or similar, and point them at it. The caveat is that they're often "lazy", and it takes some practice to coax them into being thorough (hot tip: have one write a list of things to probe and test, and tell it to to address each; otherwise they tend to decide very quickly it's too tedious and start taking shortcuts)  |  
| --- |  
 |  
|   
 |  perhaps we can give the AI a bit of money, make it the customer, then we can all safely get off the computer and go outside :)  |  
| --- |  
 |  
|   
 |  AI agents can absolutely use web browsers to do these things, but the hard part is accurately defining the acceptance criteria.  |  
| --- |  
 |  
|   
 |  One pod is an instance of a repo, you can set the number of instances of each agent/task that can be running on a pod at a time. For >1, each agent should be using it's own worktree.  |  
| --- |  
 |  
|   
 |  I prefer to have my agents review my agents output and progress, and have them improve the prompts for future runs.  |  
| --- |  
 |  
|   
 |  Yeah, I think that's the most important part in these new types of processes. Although it is tempting to just let an agent run with it for a while.  |  
| --- |  
 |  
|   
 |  Recently I used to to finish up my re-implementation of curl/libcurl in rust (). At first I started by trying to have a single claude code session run in an iterative loop, but eventually I found it was way to slow.I started tasking subagents for each remaining chunk of work, and then found I was really just repeating the need for a normal sprint tasking cycle but where subagents completed the tasks with the unit tests as exit criteria. So optio came to my mind, where I asked an agent to run the test suite, see what was failing, and make tickets for each group of remaining failures. Then I use optio to manage instances of agents working on and closing out each ticket.  |  
| --- |  
 |  
|   
 |  > To make error is human. To propagate error to all server in automatic way is #devopsI am not sure how AI agent variation of that joke would look like. Every now and then some blog posts lands on HN asking "Where are all new apps created thanks to LLM productivity boost"?. I am more surprised there are no news about some serious fuck-ups that can be traced back to LLM usage in code.  |  
| --- |  
 |  
|   
 |  There are a few things:a) you can create CI/build checks that run in github and the agents will make sure pass before it merges anything b) you can configure a review agent with any prompt you'd like to make sure any specific rules you have are followed  |  
| --- |  
 |  
|   
 |  > to make sureyou've really got to be careful with absolute language like this in reference to LLMs. A review agent provides no guarantees whatsoever, just shifts the distribution of acceptable responses, hopefully in a direction the user prefers.  |  
| --- |  
 |  
|   
 |  Fair, it's something like a semantic enforcement rather than a hard one. I think current AI agents are good enough that if you tell it, "Review this PR and request changes anytime a user uses a variable name that is a color", it will do a pretty good job. But for complex things I can still see them falling short.  |  
| --- |  
 |  
|   
 |  Yep, I was gastowning some draft PRs to get a prototype built quickly. The polecat FE PR managed to request a review from @claude (normal ok), and then given that in isolation the PR was fine due to having hardcoded draft schemas (though it was deliberately only ever going to work against a PR deployed version of the API that was also draft), decided to enable auto-merge, such that the PR actually merged and luckily I caught the CI/CD run and locked deployments, however, it would have taken down the site and pointed it to staging.  |  
| --- |  
 |  
|   
 |  I mean, having unit tests and not allowing PRs in unless they all pass is pretty easy (or requiring human review to remove a test!).A software engineer takes a spec which "shifts the distribution of acceptable responses" for their output. If they're 100% accurate (), how good does an LLM have to be for you to accept its review as reasonable?  |  
| --- |  
 |  
|   
 |  We've seen public examples of where LLMs literally disable or remove tests in order to pass. I'm not sure having tests and asking LLMs to not merge things before passing them being "easy" matters much when the failure modes here are so plentiful and broad in nature.  |  
| --- |  
 |  
|   
 |  You'd want to have the tests run as a github action and then fail the check if the tests don't pass. Optio will resume agents when the actions fail and tell them to fix the failures.  |  
| --- |  
 |  
|   
 |  So... add another presubmit test that fails when a test is removed. Require human reviews.It's not like a human being always pushes correct code, my risk assessment for an LLM reading a small bug and just making a PR is that thinking too hard is a waste of time. My risk assessment for a human is very similar, because actually catching issues during code review is best done by tests anyways. If the tests can't tell you if your code is good or not then it really doesn't matter if it's a human or an LLM, you're mostly just guessing if things are going to work and you WILL push bad code that gets caught in prod.  |  
| --- |  
 |  
|   
 |  Yup. MCP can be configured on a repo level. At task execution time, enabled MCP servers are written as a .mcp.json file into the agent's worktree. Enabled skills are written as .claude/commands/{name}.md files in the worktree, making them available as slash commands to the agent  |  
| --- |  
 |  
|   
 |  the misaligned columns in the claude made ASCII diagrams on the README really throw me off, why not fix them?   |  
| --- |  
 |  
 |

