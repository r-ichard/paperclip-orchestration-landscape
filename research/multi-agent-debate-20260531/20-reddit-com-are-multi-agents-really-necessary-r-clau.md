---
url: "https://www.reddit.com/r/ClaudeCode/comments/1qnmbw2/are_multi_agents_really_necessary/?solution=0552bc88d374706b0552bc88d374706b&js_challenge=1&token=7afd7253fec22262ff1c52b1703fe9ec110cd61285722a106b1de69a426ba5be&jsc_orig_r="
title: "Are Multi Agents Really Necessary? : r/ClaudeCode"
engine: google
rank: 20
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 8162
fetched_at: "2026-05-31T20:13:14.938785+00:00"
---

I've seen/read so many posts about people using multiple agents to simulate a developer team from Claude agents. Mostly, they have a pm, a planner, a developer, a reviewer, etc. I tried to mimic their implementation and ended up with a working "Developer team" that follows my TDD. An agent first plans what to do, an agent creates tests as the red phase, one agent develops the feature, and another agent reviews it, and if it is rejected, sends it back to the developer. 
It works, and it feels cool ngl. However, it uses a lot of tokens since each agent starts with an empty context. 
So I’m wondering: is this actually a better way to develop with Claude, or just a fancy abstraction? I feel like I could ask a single agent to do all of this and get similar results. 
I think there is some advantage to code review by a sub-agent who is prompted to do it, as then it's not defending it's own implementation. I'll occasionally tell that code-review agent that a 'untrustworthy junior developer' did the work which seems to cause more criticism to surface. 
I ran a Ralph loop last night against a fairly narrow (in features) but reasonably complex implementation. The resulting branch has over 18,000 changes in it. I wanted to review it against the plan for completeness, test coverage, etc. I also wanted Claude to do it, because this is a personal side project and I'm not reading all that code. But, if I try to one-shot it in one agent? Yeah that review will likely be trash. 
> We've done a number of enhancements, there is a PRD and plan in ]@docs/plans/2026-01-26-chat-threading-design.md and @docs/plans/2026-01-26-chat-threading-prd.md I want to do a comprehensive code review of all changes against the plans. However, the PR is huge! Ralph was very busy! so you'll need to break this review into parts and have subagents do the work. We want the highest quality code possible. 
It broke 8 sub-review tasks, spawned 8 parallel agents to do the review. Which came back and found that 7 out of 10 parts of the PRD it passed as complete without issues. Two had minor issues, one had a significant issue. 
Each sub agent burned >80-100k tokens doing the task, I don't think the result would have been as strong if I hadn't had it break them up. Now I have a set of beads to pass back into Ralph to fix the issues. But, also pretty good confidence that it didn't completely go off the rails overnight I let the loop run ~50 times unattended until it exited on it's own when it decided it was out of work. 
  1. a clean context window (cost optimization, breaking the problem down, or an evaluation of an existing solution unbiased by the current context window) 


For instance, using an agent who searches logs or documentation and only returns the specific error messages is a great way to avoid polluting your orchestrator with unrelated logs and extending your main thread's context window. 
It makes sense! I'm convinced that one of the best use case is using subagents whenever the task would pollute the main context. Creating dumber agents for basic jobs is also sounds great as cost optimization technique. 
What are y'all building with that setup? I work on a very complex( complex business logic, not tech) greenfield project, and I can't seem to find value in those kinds of setups. 
I usually start the task by giving Claude as much info as possible, and ask him to ask me questions about task. We go back and forth, while he defines task.md where every decision is outlined and plan is made, with code snippets. 
Second part, I usually start the new session asking him to take a look at task.md and research all relevant parts of code and give me a review of plan, and to check if some edge cases are not covered. 
These two parts can go on for a whole day, because sometimes I really need to think a lot to give an answer to a question, and sometimes we hit a wall and we need to start over with a plan or tear down some part of plan. 
Then, the third part, I ask him to create testing.md file where he outlines each test and what should be tested in it. It can get messy here, so this also takes few hours. 
Then, when I tell him to implement everything, very rarely do I need to change anything. And I don't see where do I need multiple agents and where would they fit. 
I think it only benefits those who straight up vibe code the dog shit out of their apps with blindfolds on. I mean if you don't give two fucks about the code base, why not send 20 coding agents out to build it. 
May I dm you about your working style (with Claude)? I really love your workflow and have follow up questions 
Absolutely not necessary. I built things for the longest time and didnt even know multi-agents was a thing. Once I started using multi-agents it changed absolutely nothing. Ok cool so there are 7 new problems for me to fix instead of just 1. 
My take is you can probably get 90% of the same results with one agent and a clear workflow. The TDD loop works because you defined the process well, not because it's four agents tbh. 
I'd start with one agent and your specs. Break it apart later if you hit context limits. And prompts like "act as a senior reviewer" just produce fluff. See if "check if this handles null inputs" actually gets you somewhere. 
Not necessary, but sometimes having a dedicated subagent with a fresh context can help; especially if it's something that you repeat often (like linting or typechecking). 
Depends what you’re doing. If you’re making software for yourself or for your own business, then sure. But if you’re writing custom software for a client with clear requirements and UI wireframes, it’s better to stick to a more granular approach. 
If you're problem is simple and there's only one solution, and you don't mind waiting - then no. Sometimes there are a few ways to solve something and it's worth asking a few people to make sure you don't miss something though 
I’m toying with the idea, a lot of brainstorming but nothing in action yet. I go down rabbit holes then don’t get my main project tasks completed…. 
All I want to do is just have the "ai" pay for itself and return a profit so then I can't actually experiment to see what all cool things I can do with it without really having to worry too much about api costs 
Clearing the context is the equivalent of having a separate agent. And that's absolutely something you should do after research, planning, implementation etc.Multi Agents come in play when you want to work on multiple tasks in parallel, but then you it's not about having a separate planning and implementation agent, but runnig mulriple planning/implementation agents in parallel.Another case for multi agent setup when the general purpose agent is not what you need, and you'd like to customize the system prompt. 
I've build workflow for my needs but I have one doubt. Is it better (but works longer) to have many smaller agents [coder-be, code-fe, tester-be, tester-fe, reviewer-fe/be, db-reviewer, commiter] or fewer larger agents [coder-tester-commiter] (less context transfer)? 
As far as I tried, multi-agent is only better when independent tasks are processed with different branches to circumvent the context window limit. Single-agent is far better at any single task within the context window limit. Conversely, in a long-term view point, the multi-agent is not optional to process a large project. 
I still don’t trust Claude on its design decisions . There will be duplicated code , bad directory structures , inadequate testing ..I guess I could write up a lot of assertions.. but really still only trust myself 
I don't claim to be an expert at this, but I regularly run 3-4 agents and they will spin up additional agents. 
I'm also working on a project to help people improve at this by creating an AI coding report. IT includes, among other things, a live dashboard of how many concurrent agents you have and a historical view of how you've been doing over time. If you check it out, LMK if you have any feedback: 
If you choose “Reject Optional Cookies” we won’t use cookies for these additional uses. You can update your cookie preference from your settings.

