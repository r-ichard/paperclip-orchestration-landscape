---
url: "https://news.ycombinator.com/item?id=46470702"
title: "Show HN: Runtm- open-source runtime and control plane for agent-built software | Hacker News"
engine: duckduckgo
rank: 24
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 1234
fetched_at: "2026-05-31T17:38:37.057395+00:00"
---

|   
 |   
 |  More context on what I’m building:runtm is an open-source runtime + control plane for agent-written software. It works with any AI IDE / CLI (Cursor, Claude Code, etc.), and is built around a simple belief: As agents generate more software, the bottleneck stops being writing code and becomes safely turning intent into something live, observable, and disposable, without humans babysitting infra. 
```
    uv tool install runtm
    runtm login
    runtm init backend-service
    # prompt agent to write code
    runtm deploy
    # URL generated at https://<app>.runtm.com
    runtm logs

```
What it is: 
```
    name: my-api
    template: backend-service
    runtime: python
    env_schema:
      - name: DATABASE_URL
        secret: true
        required: true

```
Validation before deploy, so failures surface before you ship a broken container. A human runs runtm approve.Secrets live in .env.local, which is auto-added to .*ignore. The agent cannot read them. Secrets are injected only at deploy time. Deploys to Fly.io Machines (Firecracker, auto-stop for cost control). Zero-config persistence via SQLite on a volume, or BYO Postgres. Provider layer is swappable (Cloud Run / AWS next).  |  
| --- |  
 |  
 |

