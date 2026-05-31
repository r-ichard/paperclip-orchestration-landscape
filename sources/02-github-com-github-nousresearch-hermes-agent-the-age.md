---
url: "https://github.com/nousresearch/hermes-agent"
title: "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"
engine: google
rank: 2
published: unknown
updated: unknown
author: unknown
org: GitHub
char_count: 4297
fetched_at: "2026-05-31T19:21:54.489859+00:00"
---

It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.  
Use any model you want — , (200+ models), (AI-native cloud for Model API, Agent Sandbox, and GPU Cloud), (Nemotron), , , , , , OpenAI, or your own endpoint. Switch with — no code changes, no lock-in.  
| Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.  |  
| --- |  
| Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. dialectic user modeling. Compatible with the open standard.  |  
| Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.  |  
| Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.  |  
| Six terminal backends — local, Docker, SSH, Singularity, Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster.  |  
> Native Windows support is . It installs and runs, but hasn't been road-tested as broadly as our Linux/macOS/WSL2 paths. Please when you hit rough edges. For the most battle-tested Windows setup today, run the Linux/macOS one-liner above inside .
The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, (MinGit, unpacked to — no admin required, completely isolated from any system Git install). Hermes uses this bundled Git Bash to run shell commands.
If you already have Git installed, the installer detects it and uses that instead. Otherwise a ~45MB MinGit download is all you need — it won't touch or interfere with any system Git.
> The tested manual path is documented in the . On Termux, Hermes installs a curated extra because the full extra currently pulls Android-incompatible voice dependencies.
> Native Windows is supported as an — the PowerShell one-liner above installs everything, but expect rough edges and please file issues when you hit them. If you'd rather use WSL2 (our most battle-tested Windows path), the Linux command works there too. Native Windows install lives under ; WSL2 installs under as on Linux. The only Hermes feature that currently needs WSL2 specifically is the browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway both run natively).

```
hermes              
hermes model        
hermes tools        
hermes config    
hermes gateway      
hermes setup        
hermes claw migrate 
hermes update       
hermes doctor       
```

Hermes works with whatever provider you want — that's not changing. But if you'd rather not collect five separate API keys for the model, web search, image generation, TTS, and a cloud browser, covers all of them under one subscription:
  * — web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI), cloud browser (Browser Use), all routed through your sub. No extra accounts.


That logs you in via OAuth, sets Nous as your provider, and turns on the Tool Gateway. Check what's wired up any time with . Full details on the .
Hermes has two entry points: start the terminal UI with , or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.  

```
hermes claw migrate              
hermes claw migrate --dry-run    
hermes claw migrate --preset user-data   
hermes claw migrate --overwrite  
```



  * 🔌 — Linux desktop-control MCP server for Hermes and other MCP hosts, with AT-SPI accessibility trees, Wayland/X11 input, screenshots, and compositor window targeting.



