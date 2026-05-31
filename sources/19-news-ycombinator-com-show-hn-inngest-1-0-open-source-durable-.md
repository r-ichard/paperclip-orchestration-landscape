---
url: "https://news.ycombinator.com/item?id=41604042"
title: "Show HN: Inngest 1.0 – Open-source durable workflows on every platform | Hacker News"
engine: google
rank: 19
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 15790
fetched_at: "2026-05-31T17:38:07.284432+00:00"
---

|   
 | Hi HN! I’m Tony, one of the co-founders of Inngest ()Inngest is an open-source durable workflow platform that works on any cloud. Durable workflows are stateful, long running step functions written in code, which automatically retry on failure. It abstracts everything about queues, event streams and state for you, letting you focus on code. Some examples of uses: managing stateful AI chained step functions; managing search/rag indexes and data pipelines; integrations and webhooks; billing and payment flows. Technical details: unlike other solutions, we put lots of effort into designing our SDK’s step.run APIs to make them extremely easy to use — developer experience is the most important thing for us. We had to design and build our own queueing system to work with multi-tenancy, batching, and debouncing, and we’re iterating on this as we move to FoundationDB. It’s largely all Go in the backend, with a bunch of caching, clickhouse, event streams, and coordination on our behalf. Workers are shared nothing, and run based off of the queue and execution state. We did a post last year as we iterated on our TS SDK. The product has changed a lot since then and wanted to show the community what’s changed as we reach 1.0: 
```
    * Golang, Java, and Python SDKs with cross-language function invocation (across clouds, too)

    * Multi-tenant aware flow control (concurrency, throttling, debounce)

    * Batching, grouping many events into a single function call

    * Much improved dashboard, with tracing and metrics built in

    * Advanced recovery tools like function replay, temporary pausing,  bulk cancellation (with optional expressions).  No more dead letter queues!

    * Branch deploys built in, with staging env support out of the box

    * Full local testing with production parity


```
There's a ton on the roadmap, with more launching next week. We’re hiring systems & infra engineers, too — it’s a fun job with lots of challenges!   |  
| --- |  
|   
 |  Looking at the License - This is not Open Source, but rather Source Available software.   |  
| --- |  
 |  
|   
 |  And it seems their misnomer is practically everywhere, not just in the Show HN: their website also mislabels their links as "Open Source" - I guess trying to capitalize on SEO Seems they had a change of heart around 2022: but they actually only started lying about the license in this go-around because their previous Show HN <> not only didn't mislabel things but they even said "we're gonna open source in the future" but I guess the future isn't here yet  |  
| --- |  
 |  
|   
 |  And the production infra for running isn't even available, just a pared down "development server" via SSPL. This is a long way from OSS.  |  
| --- |  
 |  
|   
 |  There might be a bit of misunderstanding on what's in that git repo here. It actually contains the executor, state store, queue, and our production UI, plus the syncing, registration, and logic for functions.Earlier this year we didn't want folks to roll their own production cloud due to queueing migrations. It would make your life hard. We're entirely responsible for that right now, as we discouraged self hosting. That's actually coming to a close, and we'll make it easy to spin up prod clusters using this code and eg. MemoryDB, Dragonfly, or what have you.  |  
| --- |  
 |  
|   
 |  Let me know when you do! I like the pattern and APIs you've designed for the SDKs—and would probably rely on a managed coordination layer like you've got. But, in order to build confidence in any product like this, we have to know that if something happened to the co, or you went another direction, we could fork the core and continue on.  |  
| --- |  
 |  
|   
 |  Well, my experience has been closer to the "more eyes make for shallow bugs" school of thought, so opening the source to contributions would actually help that process, not hinder itI've written of CI for projects because it's something I believe in and am willing to roll up my sleeves to get done (as a concrete example). I believe strongly that being able to reference the canonical CI build helps contributors since they can see how it's built for different systems and also ensure they don't submit "works on my machine" patches  |  
| --- |  
 |  
|   
 |  We'll roll out a change that releases source as GPL after 3-4 years next week, actually. I do appreciate these comments and points.  |  
| --- |  
 |  
|   
 |  So "eventually OSS"? That's certainly better, especially so for some use cases (company goes under), but it isn't OSS either.  |  
| --- |  
 |  
|   
 |  Is there any guarantee ("don't take promise from a company") the license won't be changed to something more closed some time afterwards?  |  
| --- |  
 |  
|   
 |  Why is it necessary to wait? You've already seen the feedback, if you're going to change the license, why promise to do it later?  |  
| --- |  
 |  
|   
 |  It's already planned, and rushing out a legal change on a Friday night ahead of plans is less than ideal.  |  
| --- |  
 |  
|   
 |  BSL Is also not Open Source, it is another kind of Source Available issue.Of course you're free chose the license what is right of your business, but trying to use Open Source name in deceptive marketing is the problem.  |  
| --- |  
 |  
|   
 |  don't let that stop you from using it marketing though.. if you're misleading with your marketing it makes me wonder what else is not as it is claimed.  |  
| --- |  
 |  
|   
 |   |  
| --- |  
 |  
|   
 |  I opened the comments before the website as I was sure this would be another of those sources available clickbait. Why is this kind of disingenuous move not enforced in the title guidelines of HN is beyond me.  |  
| --- |  
 |  
|   
 |  Congrats, definitely an area we're always examining toolsAfaict, this seems like a more restrictively licensed & less capable alternative to Dagster and Prefect. However, there may be some specific areas it is ahead -- the multitenancy bullet point sounds interesting, for example. Maybe you can share a comparative description?  |  
| --- |  
 |  
|   
 |  I implemented Inngest to handle our video migration queues that help move videos off of other platforms into Mux -- complete breeze. Loved the balance between the amount of complexity that's abstracted away, but still enough of a surface API exposed to do some pretty custom domain-specific work. Also the support was top notch, that goes a long way. A++, would use again, genuinely a fan.  |  
| --- |  
 |  
|   
 |  Wow, I had no idea you weren’t at 1.0 yet lol. I’ve been using Inngest for a few years(!) and it’s always felt really polished and complete to me.Congrats on the big one-oh. Question: I’ve been using Rust a lot more lately — does Inngest work natively with Rust? Is there an SDK or another way to use it?  |  
| --- |  
 |  
|   
 |  Used this for a short while and the dev experience was great (the console in particular which allowed for copying events to reproduce them locally). The typescript integration was good.My only issue was that the execution of an inngest function wasn't completely intuitive, at least in TS, and you have to think in terms of inngest or, more precisely, the abstraction it is providing. Is it an actor, a step function, an event consumer, a saga? or a combination of some? When you get used to it it's nice, less overhead than building your own actor model or your own event sources, and really good visibility into what is happening.  |  
| --- |  
 |  
|   
 |  > My only issue was that the execution of an inngest function wasn't completely intuitive, at least in TS, and you have to think in terms of inngest or, more precisely, the abstraction it is providing. Is it an actor, a step function, an event consumer, a saga? or a combination of some?I'm personally curious about this. I'm not saying you don't, but why would you need to understand what kind of abstraction it is beyond it just being Inngest"? I like to think I've been able to use it effectively without this having ever crossed my mind. But I also just might be dumb. Hence the curiosity!  |  
| --- |  
 |  
|   
 |  Because code doesn't execute as you might think it does, which is why Inngest has docs describing best practices.You have to be careful about how you structure effectful code and how you might share data between steps, and you have to understand when that code might be executed, so the more you know about that, the better. Inngest itself, at least with Vercel, doesn't do its own compute. Inngest, as far as I know, does not do its own compute, it piggybacks on your own, so if you're not careful you can go hard with inngest but you'll see the impact on your hosting bill; especially with Vercel. Inngest is a breath of fresh air but, you know, you have to audit your dependencies whether they're SaaS or not. Know how they work, know how to debug them, know how much they'll cost you.  |  
| --- |  
 |  
|   
 |  > Inngest, as far as I know, does not do its own compute, it piggybacks on your own, so if you're not careful you can go hard with inngest but you'll see the impact on your hosting bill; especially with Vercel. DBOS provides compute and we don't charge for CPU wait time, so bills are a lot cheaper with our solution.  |  
| --- |  
 |  
|   
 |  Really great product, I'm using inngest since 2-3 months and it definitely solved our problem. We needed a scheduling, queue, trigger solution. The docs are fairly good and it worked after some fiddling with our setup. I can quickly see every morning if all the jobs went through, we also starting to use them for webhooks now. Very happy, wrote at least 10 different functions in typescript so far  |  
| --- |  
 |  
|   
 |  Congrats! I used Inngest when I wrote a video processing pipeline here   |  
| --- |  
 |  
|   
 |   |  
| --- |  
 |  
|   
 |  Thanks! There are a few things at play. High level, it's important to note we provide infra for — so our multi-tenancy supports many tenants for every user.In general, fairness means distributing work evenly amongst all accounts. This largely means partitioned queues. Firstly, every functions have their own queues. We have queues of queues: queues of functions available. And then we have queues of accounts. And so on. It's like nesting dolls all the way down. There are lots of really fine details to get right: continuations, step parallelism, `connect()` with long running workers all mess with fairness, as do batching, debounce, throttling. We wrote about it in some detail here: . We'll probably do some deeper dives on this next year, too!  |  
| --- |  
 |  
|   
 |  There are similarities with "durable workflows" but, honestly, a completely different approach. Lots of respect for them. * You also get a powerful event-based API in functions: `step.waitForEvent`. This lets you do a of things: human in the loop flows, coordination — and you don't have to learn complex APIs, worry about state, can handle timeouts easily. * Because of this, you can pause individual functions, then redrive events through specific functions - as events are stored for you in an OLAP event store for your workspace. * You don't have to register individual activities and workflows. Steps are lambdas. It's easy to work with * Every step (activity) has an ID, which means versioning, replay, determinism is easier to reason about and see in our model. * We also run on servers as well as serverless. It's actually quite nice bringing state and retries to serverless functions - they're good for (some) bursty workloads Overall, both replace queueing systems. I think that's a good thing: you shouldn't really have to think about the specifics of your underlying infra when you're writing application code.  |  
| --- |  
 |  
|   
 |  Foremost, thank you for the detailed answer. It's always helpful to have competitive analysis from the sourceWhile the edit window on your comment is still open, you may want to consider removing the leading whitespace from your bullet points (since they're already newline delimited) because on HN those leading spaces make it pre-formatted and that means folks on mobile have to horizontally scroll to see your whole sentence  |  
| --- |  
 |  
|   
 |   |  
| --- |  
 |  
|   
 |  Restate.dev seems to offer a different implementation of the same feature set, and I think I might like their durable execution syntax more.  |  
| --- |  
 |  
|   
 |  Their syntax does look strikingly similar to the API we launched with a couple of years ago: `ctx.run("id", () => {})` vs `step.run("id", () => {})`.It's good to see the ecosystem form around the APIs we've developed. From feedback we've received, they're easy to use.  |  
| --- |  
 |  
|   
 |  Congrats this is huge! I've been in the market looking for a tool like this and was curious to know how this compares against toolings such as Temporal () or Trigger.dev() ?  |  
| --- |  
 |  
|   
 |  Answered this in depth here: The TL;DR is both us and Temporal help with durable execution. We layer on events and a differing DX to make things easier, faster, and to also work on serverless if people need. I can't speak to Trigger, as they've changed a lot since I last looked. It doesn't look like they do durable execution, workflows, steps, or events — it looks like they're an alternative to Lambda + SQS for TS only, so very different — more for your simple "run one thing in the background", from what I can gather. Take this with a grain of salt, though!  |  
| --- |  
 |  
|   
 |  I've been looking into this space since I learned about Temporal recently, and I wonder if it would be better to have this integrated in my application, as a library, instead of an external dependency. This way, all the state would be in the same DB.  |  
| --- |  
 |  
|   
 |  it depends on your load really. there are background job frameworks in other languages like Oban in Elixir that utilizes postgres.if scale is low, it's not an issue. but once you have high usage, what typically people do is they move it to a separate database, otherwise you're saturating the resources and it starts impacting the application itself. also another thing about databases is their ACID transactions can only handle up to certain amount of load. again, if you don't hit that limit, it's totally fine. once you do, which usually means outages, severe delays, etc, and it'll be a shit show.  |  
| --- |  
 |  
|   
 |   |  
| --- |  
 |  
|   
 |  No, they don't. They work just like Temporal and the others, which send the durable state to a separate store. I totally understand that this is good for the tool business model, since many users will end up paying for the separate store, instead of keeping it in the same DB where the application already is, without needing to pay extra for it. After all, the amount of data for keeping that state should be relativly small, so no one would provision a separate DB for it if the SDK didn't force them to.  |  
| --- |  
 |  
|   
 |  My bad, I had misunderstood that. You're right, and thank you for sharing it. That is a great differentiator. I see you have Python and JS/TS libraries, but my team is working with Go right now, so I'll have to pass. However, I'll keep it on my radar. Being able to handle wrap DB commands in the same transactions as the workflow store is awesome! [2]   |  
| --- |  
 |  
|   
 |  Congrats on 1.0 -- we've been using inngest in our product quite a bit and it's been reliable with a generous free-tier that allows us to leech off staying serverless forever :)  |  
| --- |  
 |  
|   
 |  Our launch week starts on Monday. There's something coming, with a full roadmap for differing DBs, multi-node setups, and metrics :)  |  
| --- |  
 |  
 |

