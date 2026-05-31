---
url: "https://www.reddit.com/r/ExperiencedDevs/comments/1t5tbk1/trying_to_wrap_my_head_agentic_swarms/?solution=f7b1aa61a14a9d01f7b1aa61a14a9d01&js_challenge=1&token=7afd7253fec22262ff1c52b1703fe9ec02f22ff5f3b300f052c850c7d35cd5bd&jsc_orig_r="
title: "Trying to Wrap My Head Agentic Swarms : r/ExperiencedDevs"
engine: google
rank: 33
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 8012
fetched_at: "2026-05-31T20:18:58.648726+00:00"
---

A guy at my company gave a talk about agentic swarms the other day. He talked about how different AI agents get different jobs assigned and work together on some big task. He mentioned how we might end up firing up the swarm in the evening and then checking everything thoroughly the next day. To me, this sounds nutty for the following reasons: 
I want to be in a tight loop with the AI. I want to either think about a task and feed the AI a list of things that need to be done or I want to explore the problem space together with the AI. In either case, I'll progress stepwise. Each step I can easily verify. Step size varies according to what I'm working on; Frontend code with a lot of boilerplate to position components and manage completely orthogonal state? Up to 500 lines before I feel like I have to check everything and get on top of the code. On the other hand, if I'm generating code for a C++ 3D data converter that loads 3D data from one format via an SDK and saves it in a different format with a different SDK, I'll advance slower. Maybe in steps of 50-100 lines with a lot of checking and logging to make sure everything is going as expected. 
I cannot wrap my head around letting any AI (swarm or not) run loose on a complex task without any checking/readjusting whatsoever for multiple hours. 
So did the guy at your company give a concrete example, or was he just pitching dreams to C-suite to try and give himself more visibility? 
It was the latter. But then again, his job title contains "AI", so he probably felt like it was his duty to update us underlings about the latest news in AI. Nevertheless, a bit more skepticism towards the claims and a concrete sample feature to test it and then share the results with us would've been nice. 
There was no concrete example. The talk was more about the concept of an agentic AI swarm then of what actually happens when you use it. The person giving the talk basically has "keeping us up to date about AI news" in his job description. He probably felt like he had to do it. 
I agree though that a concrete example with all the points where it went well and where it failed would've been more insightful. 
Don't diss my ant homies like that, they are extremely organized, follow the same correct process that was validated for millions of years, if they were like ai agents then you would have tons of ant "death circles", and once in a while every ant goes "hey, this is a death circle! I should change my route, this will get us the food we want!" and immediately change to another death circle. 
I think the whole special role agent thing is just to get around the , which is essentially the bigger the context, the worse they do and the more tokens it cost. So the idea is to scope down what they "know" to try controll that. You also have that agent ready on the shelf for when you need it and you dont have to prep it up. The idea of just letting agents talk to each other all night long just sounds like a way to burn serious money in tokens from them running amok without any real oversight. My stupid burned 50k tokens yesterday looking at the references back and forth between two small files. It just kept going back and forth... I was washing the dishes. 
I get a lot of value out of sitting on top of an agent, describing concisely its context and task, and reviewing each file it changes as we go. Even then, about 30% the time it just heads off on some crazy path and needs redirected back. This works out because about as fast as I can think of real solutions to problems, they can code up the last thing I asked. I can't imagine the infinite loops they'd make without direction. Tokens cost money! 
It's simpler than that. It's a ploy for this guy to be visible to upper leadership because he gave a talk on some fancy AI high-tech bull shit. To management/execs he's obviously a super innovator and a guy we definitely can't lose in our next round of layoffs. 
This is exactly how it feels in my org now. Some coworkers climbing over each other to signal how AI forward they are 
This is science fiction. Maybe it can be invented for specific tasks in such a way as to minimize llm costs, but complex is overwhelmingly likely to be incorrect. 
Agents managing agents is something that works ok for anything you wouldn't need it for, and completely falls apart for anything that you'd actually use it for. 
It's basically the equivalent of having a manager give you instruction, agree to your design, you build upon it for days getting positive feedback the entire time. 
And then your bosses boss checks in at the end of it all and says "What the fuck have you been building, none of this makes sense". 
Basically the TLDR: The result of agent swarms is not all that different from the result of just running ralph loops, so it's basically additional complexity for no benefit. 
Yeah I've heard so many people telling wild stories about this but usually it's not the people who build features. I've yet to see a single solid demo of this working well for a bigger task. 
SimonW blogged about the pattern that StrongDM is trying to follow with a small team/product. As he wrote, "It felt like a glimpse of one potential future of software development, where software engineers move from building the code to building and then semi-monitoring the systems that build the code". 
Notably StrongDM was burning $1000 on tokens per engineer per day ... that certainly won't scale as you work on larger more complex apps with larger teams. 
So the other side of that question is: token are expensive and they're only getting more expensive. If you feed an agent a problem, depending upon which model, what context window, what knowledge bases/graphs, etc. will give you a different quality of answer with widely different token usage costs. So if you're scaling agentic engineering across a larger organization, and you break your agentic workflows into smaller domain-specific parts, you're essentially doing CostOps on token spend. Getting to better quality answers with less $. 
All of this is still mostly theory crafting right now but I think for me the main lesson is that agents give better results the more constrained the task/context window/skill/question. And coming from a background of ops and compute efficiency, unobserved and undisciplined AI token usage costs can get pretty stupid high even with all the AI shops offering way below cost token pricing. 
This is what I found as well. And what I also found is that you spend all that money and you don't end up going in the right direction. 
Like my company would be burning through 23-25k/month/engineer and those engineers are not operating more efficiently than those burning through 3-5k/month/engineer. 
Which said another way: It's just wasted effort. Even if they're producing more outputs, the bottlenecks in the process seem to be elsewhere. 
And if you pay me a fee for every try, I can assure I'll make sure it takes exactly as many tries as you are able to pay for. I'll find the sweet-spot. 
  * There is no penalty (financial, at least) when AIs do a task wrong, so going hands off and just checking the output makes sense (at worst, you can just rerun the prompt tomorrow). 


All this will end, as will most of the AI companies themselves, when they have to charge what it actually costs them to run. 
20 bucks he shipped nothing with it, but he only tested it by himself to make a small thing anyone competent could've made better for a fraction of the time and cost 
"Agent 1, please read the code base and find where function saveReport() is called","Agent 2, please learn how our clients want to prepare the report","Agent 3, prepare a cost analysis" 
All of them will generate a final report. And the main orchestrator will only read 3-5KB of data instead of wasting hundreds of thousands of tokens. 
If you choose “Reject Optional Cookies” we won’t use cookies for these additional uses. You can update your cookie preference from your settings.

