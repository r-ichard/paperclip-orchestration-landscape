---
url: "https://simonwillison.net/guides/agentic-engineering-patterns/subagents/"
title: "Subagents - Agentic Engineering Patterns - Simon Willison's Weblog"
engine: google
rank: 31
published: unknown
updated: 1773750748
author: Simon Willison
org: Simon Willison’s Weblog
char_count: 3763
fetched_at: "2026-05-31T20:18:30.862268+00:00"
---

The AI App and Agent Factory — Microsoft Foundry is the enterprise Al platform where intelligence and trust ship with every agent. 
LLMs are restricted by their - how many tokens they can fit in their working memory at any given time. These values have not increased much over the past two years even as the LLMs themselves have seen dramatic improvements in their abilities - they generally top out at around 1,000,000, and benchmarks frequently report better quality results below 200,000.
Carefully managing the context such that it fits within those limits is critical to getting great results out of a model.
provide a simple but effective way to handle larger tasks without burning through too much of the coding agent’s valuable top-level context.
When a coding agent uses a subagent it effectively dispatches a fresh copy of itself to achieve a specified goal, with a new context window that starts with a fresh prompt.
Claude Code uses subagents extensively as part of its standard way of working. Let's use that as an illustrative example.
Any time you start a new task against an existing repo Claude Code first needs to explore that repo to figure out its general shape and find relevant information needed to achieve that task.
It does this by constructing a prompt and dispatching a subagent to perform that exploration and return a description of what it finds.
> Make the chapter diffs also show which characters have changed in this diff view with a darker color of red or green for the individually changed segments of text within the line
> 

Subagents work similar to any other tool call: the parent agent dispatches them just as they would any other tool and waits for the response. It's interesting to see models prompt themselves in this way - they generally have good taste in prompting strategies.
> I found the complete implementation of the diff view for chapters in this Django blog. Here are the key components:
The full subagent response included all of the details the parent agent needed in order to start editing the code to address my original request.
This Explore subagent is the simplest example of how subagents can work, with the parent agent pausing while the subagent runs. The principle advantage of this kind of subagent is that it can work with a fresh context in a way that avoids spending tokens from the parent’s available limit.
Subagents can also provide a significant performance boost by having the parent agent run multiple subagents at the same time, potentially also using faster and cheaper models such as Claude Haiku to accelerate those tasks.
For tasks that involve editing several files - and where those files are not dependent on each other - this can offer a significant speed boost. 
Some coding agents allow subagents to run with further customizations, often in the form of a custom system prompt or custom tools or both, which allow those subagents to take on a different role.
  * A agent can run the test. This is particularly worthwhile if your test suite is large and verbose, as the subagent can hide the full test output from the main coding agent and report back with just details of any failures.
  * A agent can specialize in debugging problems, spending its token allowance reasoning though the codebase and running snippets of code to help isolate steps to reproduce and determine the root cause of a bug.


While it can be tempting to go overboard breaking up tasks across dozens of different specialist subagents, it's important to remember that the main value of subagents is in preserving that valuable root context and managing token-heavy operations. Your root coding agent is perfectly capable of debugging or reviewing its own output provided it has the tokens to spare.
  1. 


