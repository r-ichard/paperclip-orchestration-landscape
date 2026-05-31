---
url: "https://news.ycombinator.com/item?id=47367169"
title: "Show HN: Diraigent – Self-hosted orchestration for AI coding agents | Hacker News"
engine: duckduckgo
rank: 26
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 863
fetched_at: "2026-05-31T17:38:41.448970+00:00"
---

|   
 |   
 |  I built a platform for running AI coding agents (currently Claude Code) through structured, repeatable pipelines — fully self-hosted.The core idea: define multi-step playbooks (implement → review → merge), and let an orchestrator spawn agents in isolated git worktrees for each task. Every step is logged, every action auditable. Key design decisions: - Agents run in isolated git worktrees, so parallel tasks don't interfere - Configurable git strategies (merge to default, branch-only, etc.) - Agents build up a persistent knowledge base, decision log, and observations across runs - Human review gates at any pipeline step - Your code, your infra, your API keys — nothing leaves your environment The platform has been running my own workflow for a while now — most of it was built through its own pipelines at this point.  |  
| --- |  
 |  
 |

