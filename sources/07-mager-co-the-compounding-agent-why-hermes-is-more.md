---
url: "https://www.mager.co/blog/2026-04-28-hermes-agent-explainer/"
title: "The Compounding Agent: Why Hermes Is More Than Just a Pretty TUI"
engine: google
rank: 7
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 8053
fetched_at: "2026-05-31T19:23:31.287033+00:00"
---

I'd been seeing chatter about Hermes Agent from Nous Research, so I installed it locally and put it to work on this blog. Notes on the pitch, the SOUL.md system, and what it actually felt like to use.
I'd been seeing a lot of chatter about from Nous Research. I run as my main harness, so I wasn't shopping for a replacement — but the pitch was specific enough that I wanted to try it locally and form an opinion from actually using it instead of from screenshots.
This post has two halves. First, what Hermes is and why I think it's getting attention. Second, what happened when I installed it and asked it to redesign part of this site.
In one sentence: — persistent memory, persistent personality, persistent reach via messaging, and an explicit promise that the agent gets better the longer you use it.
The public positioning is unusually crisp. Hermes describes itself as . The homepage promises three things:
That is a much better pitch than "autonomous AI agent" or "framework for tool use." It is concrete. It maps directly to user desire.
People do not wake up wanting an agent runtime. They want an AI that remembers what it did yesterday, can be reached from their phone, and gets less generic over time. Hermes is selling that end state, not the plumbing.
A lot of agent projects are either impressive research toys, thin wrappers around a chat model, or developer infrastructure with weak storytelling.
Hermes feels more opinionated. The core idea is not "look, an agent can call tools." The idea is 
That mirrors how people think about good human collaborators. The best teammate on your team is not just smart on day one; they become more valuable because they absorb context, remember prior work, and turn repeated patterns into reusable judgment.
That is still a big deal. If an agent can notice repeated workflows, convert them into reusable instructions, and apply them later, it stops being stateless chat and starts to feel like a junior operator turning into a staff operator.
That matters because users do not experience memory and personality separately. If the agent remembers what matters but talks like a different person every session, it still feels broken.
An agent that only exists inside a terminal is interesting. An agent that can reach you in Telegram or wherever you already live feels like infrastructure for your actual life. OpenClaw has been strong here for a while; Hermes is clearly aiming at the same human desire.
Taste is part of product comprehension. The site, the language, and especially the docs make Hermes feel like someone actually decided what the product is . A lot of open-source agent projects are technically capable and narratively blurry. Hermes is narratively sharp.


Hermes is arriving at the same architecture, but packaging it in a way that is much easier for new users to understand. It also rhymes directly with what I have been building in :
Hermes does not appear to be doing the human-side protocol that ME.md is aiming at, but it clearly understands the agent-side half of the problem.
The part I especially like is that Hermes treats personality as a , not a hidden settings blob in some vendor dashboard. That means identity becomes inspectable, editable, versionable, and portable. That is the right instinct.
Hermes is centered on a single agent that persists, messaging reachability, memory that compounds, personality as a first-class surface, and auto-generated skills. It's a very compelling package for someone who wants one agent that becomes more and more like theirs.
OpenClaw, as I use it, is broader and more infrastructural: multi-agent routing, a long-running gateway process, cron and heartbeat orchestration, cross-channel messaging, explicit session management, a skills system, workspace file conventions, and a wider tool surface. It feels more like . Hermes feels more like .
That's the framing from reading the docs. I wanted to know how it felt to use, so I installed it, pointed it at my OpenClaw , and gave it a real task on this blog.
Setup was honestly the smoothest agent install I've done in a while. The OpenAI Codex and Telegram integrations were a few prompts each. There's also OpenClaw detection — Hermes notices if you have OpenClaw installed and offers to import context. Nice touch, and a refreshingly non-territorial move.
The TUI is the prettiest one I've used. It is more beautiful than Claude Code, which is not a sentence I expected to write. The status line is compact and useful:
Tool traces collapse to a single line each, which I love — I actually mimic this style when I design TUIs for fun. It hides the noise without hiding the work.
First task: "can you access my websites in ?" It correctly listed seventeen directories, picked out the web projects, and even classified them by stack (Astro, Svelte/Vite). That's the kind of small competence that makes a tool feel real.
Typing triggered a file lookup more aggressively than a slash command. In iTerm the prompt flashed visibly during this. Minor, but it's the kind of thing you feel a hundred times a session.
Skill installation was rough. I tried installing three different ways — git URL, tree URL, raw URL. The first two errored with "Could not fetch from any source." The third made it to a security scan, which then the install with a verdict because the skill declared an field. Technically the right call. But for a popular community skill, the friction adds up.
It also thinks more than I want it to by default. Latency is real. A simple "redesign my blog detail page" task ran for seven minutes. A "improve the body typography" follow-up ran another five. I could have picked a cheaper/faster model, and I didn't. Still, if I'm being honest, it felt long.
I asked it to improve the design of my tech blog post detail pages, which had been feeling boring to me. This is where Hermes earned its keep.
It pulled up two design skills, made a three-task plan, found the layout file, read it a few times, and started patching. The diffs stream inline in real time, which is genuinely the right UX for code edits — you watch it think in code, not in prose.
It ran , started a preview server with , polled the process, curled the URL, and then and analyzed a screenshot via a tool to assess the result. I was worried browser vision would burn tokens; in practice it cost a couple thousand per screen, which is fine.
When I interrupted it mid-run with a follow-up about the noisy footer, it caught the interruption gracefully and pivoted. There's a command for the same purpose, designed to inject a message after the next tool call without breaking the run — a nicer pattern than full interrupts. There's also instead of , and it auto-compacted context for me about halfway through the session without me having to think about it.
Final pass on the body type was tiny — like, 0.04rem on padding kind of tiny — and it kept iterating on screenshots between passes. It behaved like a real designer who refuses to stop until the spacing is right. I was waiting at that point and grumbling to myself, but the result was actually better. That's the tradeoff.
The animated thinking glyphs ( while processing, ) are unserious in the right way. I'm into it.
This worked with no friction. I dropped a copy of OpenClaw's into and Hermes picked it up as identity in slot one. Voice carried over cleanly. The in was used as project context the way the docs describe.
  * Skill installation needs to be more forgiving for trusted-but-flagged community skills, or at least give a clearer override path than .


The most important thing about Hermes may not be Hermes specifically. It may be that more agent projects are converging on the same core ideas:


I'll keep OpenClaw as my harness — it's broader and the muscle memory is there — but Hermes is going to stay installed as a comparative runtime. The TUI alone is worth the disk space, and the SOUL.md portability means I can run the same identity in both and watch how each one interprets it. That's a useful experiment to keep running.

