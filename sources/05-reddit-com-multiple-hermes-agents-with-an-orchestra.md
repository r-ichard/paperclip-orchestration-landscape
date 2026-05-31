---
url: "https://www.reddit.com/r/hermesagent/comments/1t1dx9t/multiple_hermes_agents_with_an_orchestrator/?solution=69ac64eb56b386cb69ac64eb56b386cb&js_challenge=1&token=7afd7253fec22262ff1c52b1703fe9ec120a885c082d3c93c8193bd08ed6badf&jsc_orig_r="
title: "Multiple hermes agents with an orchestrator? : r/hermesagent"
engine: google
rank: 5
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 5885
fetched_at: "2026-05-31T19:22:59.021008+00:00"
---

I have multiple different areas of focus that are not related to each other, and I'd like to have multiple hermes agents, one for each area of focus. And then ideally an orchestrator that can take action items and break them up and delegate them to the appropriate sub agents. 
Yes, and while they are powerful, I do need a little more cross communication and handoffs. Profiles are entirely siloed, which is great for single action plans. 
On my use case I have one are of focus that has 3 agents, 1 running product research, 1 running exom operations/processing orders, and 1 handling customer service. These need to have some level of context overlap while still have their defined roles. 
I have many projects myself, and I assign a profile to a project. The skills are shared across the profiles, you can just add a singular skills folder in the config.yaml. I like this approach because the profile knows everything about my project and self learns. So if I want to do some research or social media, that profile knows everything about my project. I liked this approach over having to send context to a ‘researcher’ agent or ‘coder’ agent. 
There aren’t any good orchestrators yet. Openclaw was supposed to be it, but it sucks ass. I’m building one, but it’s not ready yet. 
Yep, it’s unpredictable and sloppy. I’m sure it will get better, but I decided to make my own to speed up the process. 
I think what you're looking for is shared folders and files with correct constraints applied. So each profile has its own working environment with overlapping working environment and constraints on what it can read and write from other working environments. 
I basically just used my projects folder to do this and have logs from one profile output into another profile so I can have the specialised profile check the logs for me as it knows what it needs to look for. 
I also do the same with research, researcher does web research, outputs to me files and distill it to the specs that it was given. File gets created which the original profile is looking out for and will process once it's there or you can setup something like below: 
If you tell Hermes you want one profile to be able to access another's information through a file system it'll do this. If you ask it to check X file every 5 seconds for updates then start a new process or a new window to work on it, it'll set that up too. If you setup the prompt properly, the researcher will 'hand' the file back to the other profile in a new window and process it, you just need to ask it to and clarify it and the skills it creates so it does it reliably. 
I'm waiting for Workspace to get a bit more mature. I spend more time debugging than using it... But once that happens, it should be great. 
Yesterday, I tried out the new kanban system, but it didn’t work out well. I ended up spending half of my weekly token allowance and having nothing to show for it. 
During an update, I noticed the skills and thought it would be a great way to try out the agent teams idea. So, I created a repository, recommended profiles from the kanban skill, and a simple task to bootstrap a local BI setup - PostgreSQL, SQLMesh, and Metabase. 
The most problematic aspects were the review loop and worktrees. Reviews kept blocking, and the orchestrator would create new tasks to incorporate reviewer’s feedback without properly linking them to existing tasks further down in the graph. This resulted in tasks like implementation starting before planning for them was complete. 
Regarding worktrees, sometimes they weren’t used, and other times tasks would time out without killing the again and restart, causing now two agents to mess around with the same work tree. 
I’m sure part of the issue is how I used it, but it’s also not entirely clear to me how to use it properly. 
I'm glad to read this comment because I had the exact same experience. I thought I was doing something wrong, but I think the agents just don't understand how to use the Kanban fully yet. 
They mess up the parent-child relationships and the reviewers will block, like you mentioned. Either way, the workflows come to a halt, and nothing tries to resolve it until I step in. 
I have the same thoughts. I did this with openclaw first and the whole thing collapsed on itself. Tried to build it all at once. Then I tried again. Building each agent out and not moving to the next until each one was working in a consistent manner. That only lasted for so long. I wound up at Hermes, worked great out of the box and still works. However, I also have a wide scope and I’m afraid I’m taxing that original Hermes instance to much. I do have two others going now and they both do their jobs well but they don’t work together. I am almost wondering if a Hermes agent managing a team of openclaw agents is the way to go 
Paperclip works well with Hermes- and you can treat each instance as a separate agent as far as I know 
We dont know what your problem is but you probably dont need to do this. You can set the skills or soul or specific bot intake to whatever context you need. iF you really want this, you can you use any messaging platform/webhook/terminal input for hermes as the output from your orchestrator. 
Paperclip, I have all my ceo agents report to a top level executive which is essentially my personal agent. I plan tasks with it and it comes up with how to delegate the responsibilities to the hermes CEO agents that delegates tasks to openclaw agents. I also configured it so my Hermes agents do context work in congee,honcho, and the lang stack before it’s processed by a major llm to save on tokens. Only thing Hermes should be using the expensive tokens for is finding out things it doesn’t know already. 
If you choose “Reject Optional Cookies” we won’t use cookies for these additional uses. You can update your cookie preference from your settings.

