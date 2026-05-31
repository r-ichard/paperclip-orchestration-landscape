---
url: "https://www.reddit.com/r/ClaudeAI/comments/1tq9ofy/introducing_dynamic_workflows_in_claude_code/?solution=9587c63c8ed8513a9587c63c8ed8513a&js_challenge=1&token=7afd7253fec22262ff1c52b1703fe9ec1e89f4c3f2a050a7f8e9ef441d9b5c6f&jsc_orig_r="
title: "Introducing dynamic workflows in Claude Code : r/ClaudeAI"
engine: google
rank: 13
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 6709
fetched_at: "2026-05-31T19:23:04.094996+00:00"
---

Today we're introducing dynamic workflows in Claude Code. Claude now writes its own orchestration scripts, fans work out across tens to hundreds of parallel subagents in a single session, and verifies its own results before anything reaches you. Work you'd normally plan in quarters can finish in days. 
Built for the tasks a single pass can't handle: codebase-wide bug hunts, security and optimization audits, large migrations and language ports, and high-stakes work where you want adversarial agents trying to break the answer before you see it. Progress is checkpointed, so long runs survive interruption. 
One early example: Jarred Sumner used dynamic workflows to port Bun from Zig to Rust. Roughly 750,000 lines, 11 days from first commit to merge, 99.8% of the test suite passing. 
Available today in research preview on Max, Team, and Enterprise (admin-enabled) plans, plus the Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry. Turn on auto mode and either ask Claude to create a workflow or flip on the new setting. 
While the idea of dynamic workflows is cool, the community is overwhelmingly concerned that this is a "token black hole" designed to burn through usage limits and API credits at a terrifying speed. 
  * Users are calling this "ultra-token-consumption mode" and "dynamic bills," with some reporting they've torched over . The general feeling is this feature is for enterprises with huge budgets, not for individual subscribers. 
  * A top-voted comment completely debunks the "Bun port" example from the announcement, citing evidence that the resulting code was dangerously "unsound" and full of errors. 
  * A few users are complaining that the feature kicks in automatically on large contexts, hijacking their workflow and silently draining their usage. One person's company admin even found it was enabled by default. 


I have a team premium plan, single prompt was 7.2 million tokens when it spun up 22 agents to do a deep review of a 24k LOC vibe coded personal project. Brand new session, near zero context used. Claude ultracode used 100% of my session and 20% of my weekly limit in under 10 minutes. And it didnt even finish... 
I tried a smaller genuine work related task and while I still need to test the result, some of the things it found and conclusions it made were quite astounding. But this also vaporized about 40% of session and had to wait for next session to finish. It's just not worth it even if it does pan out. 
I've only ever reached my session limits perhaps twice in the past 8 months. Never got above 50% of weekly limit. And I'm a fairly heavy user - usage stats for my account showing over 100k LOC this month, and I'm explicitly aiming to minimize lines of code in general. This new version and ultracode seem very intriguing but who is really going to spend that kind of money to get a task done? And what happens in that roughly 30% of the time when Claude misses the mark? It's frustrating when you've only wasted a few percentage points of a session limit and time - but if it blows out your limit AND fails at the task, you'll just never use it again. 
I need to do some config tuning for the agents it uses, maybe limit the number and the models if possible. But I don't really have the time or desire when this seems explicitly set up to burn crazy tokens out of the box? Incredibly lame trust busting grift move if you ask me. And I really like Claude. Anthropic needs to do better or be more honest about their strategy because they way it looks now is I need to at least consider alternatives for the day when we get priced out of their highest tier plan. 
PS. We're still in 2x weekly limits promotion from Anthropic, so just imagine how this plays out mid July when that ends... 
Just to be clear: you mean , right? The one that made the front page of Hacker News two weeks ago because it failed even the most basic miri checks and allowed for undefined behavior? The one AwesomeQubic is referring to when they write: "As a rust developer I must say this is one of the most unsound codebases I have ever seen"? The one Architector4 was talking about when he catalogued "thirteen thousand two hundred and fifty five lines without comments with the word 'unsafe' in them in Rust code files across this rewrite"? port? 
That last 0.2%? Absolutely impossible, the AI can't solve it and now no human on earth understands the code enough to fix it. 
I know you jest, but it's important to point out that test coverage ≠ code quality. A codebase can be fully covered by unit tests, can even pass a rigorous integration test suite, and still be full of bugs and errors. Most of the time those errors are subtle and hard to detect, but in this case they're glaringly obvious to anyone with even a basic proficiency in Rust. 
Unified backend for AI apps: Postgres, RAG, agent orchestration with tools, and n8n-like workflows. Fine-tuned for use by coding agents. Build and launch an AI app in one day.
Tbh I’ve been waiting for a feature like this. It’s not for all use cases of course but I’ve got a project that I wanted to test this on for a long time and I’m currently doing exactly that. Haven’t checked the output in detail yet but the speed and autonomy seems to be what I was hoping for. 
EDIT: So, it seems it launches plan agents and implement agents and does a review in the end and suggests next steps based on the outcome. Basically what I’ve been doing manually. Not bad. 
Feel like I would need a large team to just review the output a workflow generates. Then again maybe that’s who this feature is meant for. 
This is a really dicey feature the way it's been implemented. If you get past 50% context, it will start to spawn out the work with workflow mode and subagents. If you happen to be doing something where you want to use your context and want it to keep writing, this will happen silently, creating problems for you. 
I get that when you ship fast and drop updates to claude code and new models stuff like this will happen. But I don't want to fight with claude over how the work gets done. I don't want the behavior to change suddenly halfway through, and that just happened on a very expensive coding run. 
Please allow the user to control the behavior if the behavior is going to have significant effects on the context and processing of the work being performed. 
The part I’m most curious about is the failure boundary: when a dynamic workflow decides it needs human review, what signals are you using to stop the subagents from continuing past a bad branch? 
If you choose “Reject Optional Cookies” we won’t use cookies for these additional uses. You can update your cookie preference from your settings.

