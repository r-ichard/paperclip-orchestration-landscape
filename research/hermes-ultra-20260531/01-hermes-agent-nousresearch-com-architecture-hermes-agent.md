---
url: "https://hermes-agent.nousresearch.com/docs/developer-guide/architecture"
title: Architecture | Hermes Agent
engine: google
rank: 1
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 6448
fetched_at: "2026-05-31T19:21:47.984432+00:00"
---

This page is the top-level map of Hermes Agent internals. Use it to orient yourself in the codebase, then dive into subsystem-specific docs for implementation details.

```
│                        Entry Points                                  ││                                                                      ││  Batch Runner    API Server                  Python Library          │           │              │                       │           ▼              ▼                       ▼│                     AIAgent (run_agent.py)                          ││                                                                     ││  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               ││  │ Prompt       │  │ Provider     │  │ Tool         │               ││  │ Builder      │  │ Resolution   │  │ Dispatch     │               ││  │ (prompt_     │  │ (runtime_    │  │ (model_      │               ││  │  builder.py) │  │  provider.py)│  │  tools.py)   │               ││  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘               ││         │                 │                 │                       ││  ┌──────┴───────┐  ┌──────┴───────┐  ┌──────┴───────┐               ││  │ Compression  │  │ 3 API Modes  │  │ Tool Registry│               ││  │ & Caching    │  │ chat_compl.  │  │ (registry.py)│               ││  │              │  │ codex_resp.  │  │ 70+ tools    │               ││  │              │  │ anthropic    │  │ 28 toolsets  │               ││  └──────────────┘  └──────────────┘  └──────────────┘               │           │                                    │           ▼                                    ▼│ Session Storage   │              │ Tool Backends         ││ (SQLite + FTS5)   │              │ Terminal (6 backends) ││ hermes_state.py   │              │ Browser (5 backends)  ││ gateway/session.py│              │ Web (4 backends)      │└───────────────────┘              │ MCP (dynamic)         │
```


```
├── run_agent.py              # AIAgent — core conversation loop (large file)├── cli.py                    # HermesCLI — interactive terminal UI (large file)├── toolsets.py               # Tool groupings and platform presets├── agent/                    # Agent internals│   ├── display.py            # KawaiiSpinner, tool preview formatting├── hermes_cli/               # CLI subcommands and setup│   ├── main.py               # Entry point — all `hermes` subcommands (large file)│   ├── config.py             # DEFAULT_CONFIG, OPTIONAL_ENV_VARS, migration│   ├── commands.py           # COMMAND_REGISTRY — central slash command definitions│   ├── auth.py               # PROVIDER_REGISTRY, credential resolution│   ├── models.py             # Model catalog, provider model lists│   ├── setup.py              # Interactive setup wizard (large file)│   ├── plugins.py            # PluginManager — discovery, loading, hooks│   ├── callbacks.py          # Terminal callbacks (clarify, sudo, approval)│   └── gateway.py            # hermes gateway start/stop├── tools/                    # Tool implementations (one file per tool)│   ├── mcp_tool.py           # MCP client (large file)│   └── environments/         # Terminal backends (local, docker, ssh, modal, daytona, singularity)├── gateway/                  # Messaging platform gateway│   ├── run.py                # GatewayRunner — message dispatch (large file)│   ├── session.py            # SessionStore — conversation persistence│   ├── pairing.py            # DM pairing authorization│   ├── hooks.py              # Hook discovery and lifecycle events│   ├── mirror.py             # Cross-session message mirroring│   ├── status.py             # Token locks, profile-scoped process tracking│   ├── builtin_hooks/        # Extension point for always-registered hooks (none shipped)│   └── platforms/            # 20 adapters: telegram, discord, slack, whatsapp,│                             #   signal, matrix, mattermost, email, sms,│                             #   dingtalk, feishu, wecom, wecom_callback, weixin,│                             #   bluebubbles, qqbot, homeassistant, webhook, api_server,│                             #   yuanbao├── acp_adapter/              # ACP server (VS Code / Zed / JetBrains)├── cron/                     # Scheduler (jobs.py, scheduler.py)├── skills/                   # Bundled skills (always available)├── website/                  # Docusaurus documentation site└── tests/                    # Pytest suite (~25,000 tests across ~1,250 files)
```


```

```


```

```


```

```



The synchronous orchestration engine ( in ). Handles provider selection, prompt construction, tool execution, retries, fallback, callbacks, compression, and persistence. Supports three API modes for different provider backends.


A shared runtime resolver used by CLI, gateway, cron, ACP, and auxiliary calls. Maps tuples to . Handles 18+ providers, OAuth flows, credential pools, and alias resolution.
Central tool registry () with 70+ registered tools across ~28 toolsets. Each tool file self-registers at import time. The registry handles schema collection, dispatch, availability checking, and error wrapping. Terminal tools support 6 backends (local, Docker, SSH, Daytona, Modal, Singularity).
SQLite-based session storage with FTS5 full-text search. Sessions have lineage tracking (parent/child across compressions), per-platform isolation, and atomic writes with contention handling.
Long-running process with 20 platform adapters, unified session routing, user authorization (allowlists + DM pairing), slash command dispatch, hook system, cron ticking, and background maintenance.
Three discovery sources: (user), (project), and pip entry points. Plugins register tools, hooks, and CLI commands through a context API. Two specialized plugin types exist: memory providers () and context engines (). Both are single-select — only one of each can be active at a time, configured via or .
First-class agent tasks (not shell tasks). Jobs store in JSON, support multiple schedule formats, can attach skills and scripts, and deliver to any platform.  
 |  
|  |  
| One AIAgent class serves CLI, gateway, ACP, batch, and API server. Platform differences live in the entry point, not the agent.  |  
 |  

```

```

This chain means tool registration happens at import time, before any agent instance is created. Any file with a top-level call is auto-discovered — no manual import list needed.



