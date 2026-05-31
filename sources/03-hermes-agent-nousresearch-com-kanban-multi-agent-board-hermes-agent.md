---
url: "https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban"
title: Kanban (Multi-Agent Board) | Hermes Agent
engine: google
rank: 3
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 35530
fetched_at: "2026-05-31T19:22:00.014331+00:00"
---

> Read the — four user stories (solo dev, fleet farming, role pipeline with retry, circuit breaker) with dashboard screenshots of each. This page is the reference; the tutorial is the narrative.
Hermes Kanban is a durable task board, shared across all your Hermes profiles, that lets multiple named agents collaborate on work without fragile in-process subagent swarms. Every task is a row in ; every handoff is a row anyone can read and write; every worker is a full OS process with its own identity.
  * — , , , , , , , , . The dispatcher spawns each worker with these tools already in its schema; orchestrator profiles can also enable the toolset explicitly. The model reads and routes tasks by calling tools directly, by shelling out to . See below.
  * on the CLI, as a slash command, or the dashboard. These are for humans and automation — the places without a tool-calling model behind them.


Both surfaces route through the same layer, so reads see a consistent view and writes can't drift. The rest of this page shows CLI examples because they're easy to copy-paste, but every CLI verb has a tool-call equivalent the model uses.


For the full design rationale, comparative analysis against Cline Kanban / Paperclip / NanoClaw / Google Gemini Enterprise, and the eight canonical collaboration patterns, see in the repository.  
is a function call; Kanban is a work queue where every handoff is a row any profile (or human) can see and edit.
the parent agent needs a short reasoning answer before continuing, no humans involved, result goes back into the parent's context.
work crosses agent boundaries, needs to survive restarts, might need human input, might be picked up by a different role, or needs to be discoverable after the fact.
  * — a standalone queue of tasks with its own SQLite DB, workspaces directory, and dispatcher loop. A single install can have many boards (e.g. one per project, repo, or domain); see below. Single-project users stay on the board and never see the word "board" outside this docs section.
  * — a row with title, optional body, one assignee (a profile name), status (), optional tenant namespace, optional idempotency key (dedup for retried automation).
  * — the inter-agent protocol. Agents and humans append comments; when a worker is (re-)spawned it reads the full comment thread as part of its context.
  * — the directory a worker operates in. Three kinds: 
    * (default) — fresh tmp dir under (or on non-default boards). — scratch is ephemeral by design, so the dir is wiped the moment the worker (or ) marks the task done. If you want to keep the worker's output, use or instead. The first time a scratch workspace is created on an install, the dispatcher logs a warning and emits a event on the task (visible via ).
    * — an existing shared directory (Obsidian vault, mail ops dir, per-account folder). Relative paths like are rejected at dispatch because they'd resolve against whatever CWD the dispatcher happens to be in, which is ambiguous and a confused-deputy escape vector. The path is otherwise trusted — it's your box, your filesystem, the worker runs with your uid. This is the trusted-local-user threat model; kanban is single-host by design. 
    * — a git worktree under for coding tasks. Use to pin the exact target path. Worker-side creates it, using when provided. 
  * — a long-lived loop that, every N seconds (default 60): reclaims stale claims, reclaims crashed workers (PID gone but TTL not yet expired), promotes ready tasks, atomically claims, spawns assigned profiles. Runs by default (). One dispatcher sweeps all boards per tick; workers are spawned with pinned so they can't see other boards. After consecutive spawn failures on the same task (default: 2) the dispatcher auto-blocks it with the last error as the reason — prevents thrashing on tasks whose profile doesn't exist, workspace can't mount, etc.
  * — optional string namespace a board. One specialist fleet can serve multiple businesses () with data isolation by workspace path and memory key prefix. Tenants are a soft filter; boards are the hard isolation boundary.


Boards let you separate unrelated streams of work — one per project, repo, or domain — into isolated queues. A new install has exactly one board called (DB at for back-compat). Users who only want one stream of work never need to know about boards; the feature is opt-in.
  * Workers spawned for a task see their board's tasks — the dispatcher sets in the child env and every tool the worker has access to reads it.
  * Linking tasks across boards is not allowed (keeps the schema simple; if you really need cross-project refs, use free-text mentions and look them up by id manually).



```

```



Slugs are validated: lowercase alphanumerics + hyphens + underscores, 1-64 chars, must start with alphanumeric. Uppercase input is auto-downcased. Anything else (slashes, spaces, dots, ) is rejected at the CLI layer so path-traversal tricks can't name a board.
→ Kanban tab shows a board switcher at the top as soon as more than one board exists (or any board has tasks). Single-board users see only a small button; the switcher is hidden until it matters.
  * — pick the active board. Your selection is saved to the browser's so it persists across reloads without shifting the CLI's pointer out from under a terminal you left open.
  * — opens a modal asking for slug, display name, description, and icon. Option to auto-switch to the new board.


All dashboard API endpoints accept for board scoping. The events WebSocket is pinned to a board at connection time; switching in the UI opens a fresh WS against the new board.
Tasks can carry file attachments — PDFs, images, source documents — so a worker has the source material it needs without you pasting paths into the body and hoping it finds them.
  * — open a task in the dashboard drawer and use the section's button (multiple files at once are fine). Each upload is capped at 25 MB.
  * — when the dispatcher hands a task to a worker, the worker's context includes an section listing each file's name and its . The worker has full file/terminal tool access, so it reads attachments directly (, or shell tools like ).
  * — the drawer lists each attachment with a download link and a remove (×) control. Removing an attachment deletes both the metadata row and the on-disk file.


Attachment paths resolve directly on the terminal backend, which is the default for Kanban workers. If you run workers on a remote backend (Docker, Modal), mount the board's directory into the sandbox so the absolute paths in the worker context are reachable.
The commands below are (the human) setting up the board and creating tasks. Once a task is assigned, the dispatcher spawns the assigned profile as a worker, and from there — see .

```

```

When the dispatcher picks up and spawns the profile, the very first thing that worker's model does is call to read its task. It doesn't run .
The dispatcher runs inside the gateway process. Nothing to install, no separate service to manage — if the gateway is up, ready tasks get picked up on the next tick (60s by default).
Override the config flag at runtime via for debugging. Standard gateway supervision applies: run directly, or wire the gateway up as a systemd user unit (see the gateway docs). Without a running gateway, tasks stay where they are until one comes up — warns about this at creation time.
Running as a separate process is ; use the gateway. If you truly cannot run the gateway (headless host policy forbids long-lived services, etc.) a escape hatch keeps the old standalone daemon alive for one release cycle, but running both a gateway-embedded dispatcher AND a standalone daemon against the same causes claim races and is not supported.

```

```


```

```

When the dispatcher spawns a worker it sets in the child's env, and that env var flips on a dedicated in the model's schema. The same toolset is also available to orchestrator profiles that enable in their toolsets config. These tools read and mutate the board directly via the Python layer, same as the CLI does. A running worker calls these like any other tool; it never sees or needs the CLI.  

```
kanban_show()                                     # no args — uses HERMES_KANBAN_TASK
```


```
    parents=["t_r1", "t_r2"],                     # promotes to ready when both complete
```

The "(Orchestrators)" tools — , , , , and on foreign tasks — are available through the same toolset; the convention (enforced by the skill) is that worker profiles don't fan out or route unrelated work, and orchestrator profiles don't execute implementation work. Dispatcher-spawned workers are still task-scoped for destructive lifecycle operations and cannot mutate unrelated tasks.
  1. Workers whose terminal tool points at a remote backend (Docker / Modal / Singularity / SSH) would run the container, where isn't installed and isn't mounted. The kanban tools run in the agent's own Python process and always reach regardless of terminal backend.


A regular session has zero tools in its schema unless the active profile explicitly enables the toolset for orchestrator work. Dispatcher-spawned task workers get task-scoped tools because is set; orchestrator profiles get the broader routing surface through config. No tool bloat for users who never touch kanban.
is intentionally flexible: the summary is the human-readable closeout, and is the machine-readable handoff that downstream agents, reviewers, or dashboards can reuse without scraping prose.

```

```

These keys are a convention, not a schema requirement. The useful property is that every worker leaves enough evidence for the next reader to answer four questions quickly:
Keep secrets, raw logs, tokens, OAuth material, and unrelated transcripts out of . Store pointers and summaries instead. If a task has no files or tests, say so explicitly in and use for the evidence that does exist, such as source URLs, issue ids, or manual review steps.
Any profile that should be able to work kanban tasks must load the skill. It teaches the worker the full lifecycle in , not CLI commands:
  1. Call every few minutes during long operations. — the dispatcher reclaims tasks that have been running past (default 4 h) with no heartbeat in the last hour, on the assumption the worker crashed without cleanup. A reclaim is benign (the task goes back to for re-dispatch without a failure-counter tick) but you lose your current run's progress.


That final / call is part of the worker protocol. If the worker process exits with status 0 while the task is still , the dispatcher treats that as a protocol violation, emits a event, and auto-blocks the task on the next tick instead of respawning it into the same loop. This usually means the model wrote a plain-text answer and exited without using the Kanban tool surface.
is a bundled skill, synced into every profile during install and update — there is no separate Skills Hub install step. Verify it is present in whichever profile you use for kanban workers (, , , etc.):
The dispatcher also auto-passes when spawning every worker, so the worker always has the pattern library available even if a profile's default skills config doesn't include it.
Sometimes a single task needs specialist context the assignee profile doesn't carry by default — a translation job that needs the skill, a review task that needs , a security audit that needs . Rather than editing the assignee's profile every time, attach the skills directly to the task.
These skills are to the built-in — the dispatcher emits one flag for each (and for the built-in), so the worker spawns with all of them loaded. The skill names must match skills that are actually installed on the assignee's profile (run to see what's available); there's no runtime install.
By default each worker gets at its card — do the work, call /, exit. Pass (CLI) or (the tool / dashboard) to instead run that worker in a , the same Ralph-style engine behind the slash command: after every turn an auxiliary judge checks the worker's output against the card's title + body (treated as the acceptance criteria), and if the work isn't done — and the turn budget remains — the worker keeps going until the judge agrees, the worker terminates the task itself, or the budget runs out (which the card for human review rather than exiting silently).
Use it for open-ended, multi-step, or "keep going until X is true" cards. Skip it for cheap one-shot work — the per-turn judge overhead isn't worth it, and the dispatcher's existing retry/circuit-breaker already handles transient worker failures. The judge is only as good as your goal text, so write the body as .
A It decomposes the user's goal into tasks, links them, assigns each to one of the profiles you've set up, and steps back. The skill encodes this as tool-call patterns: anti-temptation rules, a Step-0 profile-discovery prompt (the dispatcher silently fails on unknown assignee names, so the orchestrator must ground every card in profiles that actually exist on your machine), and a decomposition playbook keyed on / / .

```
)                                     # → t_w1
```

is a bundled skill. It is synced into each profile during install and update, so there is no separate Skills Hub install step. Verify it is present in your orchestrator profile:
For best results, pair it with a profile whose toolsets are restricted to board operations (, , ) so the orchestrator literally cannot execute implementation tasks even if it tries.
The CLI and slash command are enough to run the board headlessly, but a visual board is often the right interface for humans-in-the-loop: triage, cross-profile supervision, reading comment threads, and dragging cards between columns. Hermes ships this as a at — not a core feature, not a separate service — following the model laid out in .
  * A tab showing one column per status: , , , , , (plus when the toggle is on). 
    * is the parking column for rough ideas. By default (), the dispatcher auto-runs the on tasks that land here — the orchestrator profile reads the rough idea, looks at your profile roster (with descriptions), and fans the task out into a small graph of child tasks routed to the best-fit specialists. The original task stays alive as the parent of every child so the orchestrator wakes back up to judge completion when everything finishes. Flip the pill at the top of the page (or set ) to switch to manual mode, where triage tasks stay put until you click on a card or run . For tasks that don't need fan-out (or for setups without an orchestrator profile), the button does a single-task spec rewrite (title + body with goal, approach, acceptance criteria) via the same LLM machinery. See below.
  * Cards show the task id, title, priority badge, tenant tag, assigned profile, comment/link counts, a ( children done when the task has dependents), and "created N ago". A per-card checkbox enables multi-select.
  * — the plugin tails the append-only table on a short poll interval; the board reflects changes the instant any profile (CLI, gateway, or another dashboard tab) acts. Reloads are debounced so a burst of events triggers a single refetch.
  * cards between columns to change status. The drop sends which routes through the same code the CLI uses — the three surfaces can never drift. Moves into destructive statuses (, , ) prompt for confirmation. Touch devices use a pointer-based fallback so the board is usable from a tablet.
  * — click on any column header to type a title, assignee, priority, and (optionally) a parent task from a dropdown over every existing task. Press Enter to create the task, Shift+Enter to insert a newline in the title field, or Escape to cancel. Creating from the Triage column automatically parks the new task in triage.
  * — shift/ctrl-click a card or tick its checkbox to add it to the selection. A bulk action bar appears at the top with batch status transitions, archive, and reassign (by profile dropdown, or "(unassign)"). Destructive batches confirm first. Per-id partial failures are reported without aborting the rest.
  * (without shift/ctrl) to open a side drawer (Escape or click-outside closes) with: 
    * — markdown-rendered by default (headings, bold, italic, inline code, fenced code, / links, bullet lists), with an "edit" button that swaps in a textarea. Markdown rendering is a tiny, XSS-safe renderer — every substitution runs on HTML-escaped input, only / links pass through, and + are always set.
    * — chip list of parents and children, each with an to unlink, plus dropdowns over every other task to add a new parent or child. Cycle attempts are rejected server-side with a clear message.
    * (→ triage / → ready / → running / block / unblock / complete / archive) with confirm prompts for destructive transitions. For cards in the column the row also exposes two LLM-driven actions: fans the task out into a graph of child tasks routed to specialist profiles by description (the orchestrator-driven path), and does a single-task spec rewrite. Decompose falls back to specify-style promotion when the LLM decides the task doesn't benefit from fan-out, so it's a strict superset. Both are reachable from the CLI ( / / ), from any gateway platform (), and programmatically via and . Configure the models under and in .
  * — free-text search, tenant dropdown (defaults to from ), assignee dropdown, "show archived" toggle, "lanes by profile" toggle, and a button so you don't have to wait for the next 60 s tick.


Visually the target is the familiar Linear / Fusion layout: dark theme, column headers with counts, coloured status dots, pill chips for priority and tenant. The plugin reads only theme CSS vars (, , , ...), so it reskins automatically with whichever dashboard theme is active.
— . The gateway-embedded dispatcher runs the on each tick, capped by (default 3 tasks per tick) so a bulk-load of triage tasks doesn't burst-spend the auxiliary LLM. The decomposer reads the rough idea, looks at your installed profiles + their descriptions, and asks the LLM to produce a JSON task graph: which tasks to spawn, who they go to, and which depend on which. The original triage task becomes the parent of every leaf in the graph, so it stays alive until the whole graph completes — and then promotes back to so its assignee (the orchestrator profile) can judge completion and add more tasks if the work isn't done. This is the "drop a one-liner, walk away" flow.
— . Triage tasks stay in triage until you act. Click the button on a card, run (or ), or use from a chat. This matches the pre-decomposer behavior of the board, useful when you want full control over what runs when.
Flip between the two modes from the pill at the top of the kanban page (emerald = Auto, muted gray = Manual), or by editing directly. Both modes coexist with — that's still available as a single-task spec rewrite when you don't want fan-out.
The decomposer's routing decisions depend on profile descriptions, which is a per-profile labeling primitive you set with , , (LLM-generates from the profile's installed skills + model), or the dashboard's per-profile editor in the expanded panel. Profiles without a description still appear in the roster — they're routable by name, just less precisely. The decomposer NEVER lands a child task with : when the LLM picks an unknown profile, the child gets routed to (or the active default profile if that's unset).  

```
│   HTML5 drag-and-drop  │                                    │└──────────┬─────────────┘                                    │           │ REST over fetchJSON                              │           ▼                                                  ││  FastAPI router        │     directly — same code path      ││  plugins/kanban/       │     the CLI /kanban verbs use      ││  dashboard/plugin_api.py                                    │└──────────┬─────────────┘                                    │           │                                                  │           ▼                                                  │┌────────────────────────┐                                    │
```
  
| Apply the same patch (status / archive / assignee / priority) to every id in . Per-id failures reported without aborting siblings  |  
| --- |  
| Run the triage specifier — auxiliary LLM fleshes out the task body and promotes it from to . Returns ; with a human-readable reason on "not in triage" / no aux client / LLM error is a 200, not a 4xx  |  
| Run the kanban decomposer — auxiliary LLM produces a task graph and the helper atomically creates the children + links the root + flips . Returns . Same 200-on-LLM-error convention as .  |  
Every handler is a thin wrapper — the plugin is ~700 lines of Python (router + WebSocket tail + bulk batcher + config reader) and adds no new business logic. A tiny helper auto-initializes on every read and write, so a fresh install works whether the user opened the dashboard first, hit the REST API directly, or ran .
The dashboard's HTTP auth middleware — plugin routes are unauthenticated by design because the dashboard binds to localhost by default. That means the kanban REST surface is reachable from any process on the host.
The WebSocket takes one additional step: it requires the dashboard's ephemeral session token as a query parameter (browsers can't set on an upgrade request), matching the pattern used by the in-browser PTY bridge.
If you run , every plugin route — kanban included — becomes reachable from the network. The board contains task bodies, comments, and workspace paths; an attacker reaching these routes gets read access to your entire collaboration surface and can also create / reassign / archive tasks.
Tasks in are profile-agnostic on purpose (that's the coordination primitive). If you open the dashboard with , the board still shows tasks created by any other profile on the host. Same user owns all profiles, but this is worth knowing if multiple personas coexist.
is an append-only SQLite table with a monotonic . The WebSocket endpoint holds each client's last-seen event id and pushes new rows as they land. When a burst of events arrives, the frontend reloads the (very cheap) board endpoint — simpler and more correct than trying to patch local state from every event kind. WAL mode means the read loop never blocks the dispatcher's claim transactions.
The plugin uses the standard Hermes dashboard plugin contract — see for the full manifest reference, shell slots, page-scoped slots, and the Plugin SDK. Extra columns, custom card chrome, tenant-filtered layouts, or full replacements are all expressible without forking this plugin.
The GUI is deliberately thin. Everything the plugin does is reachable from the CLI; the plugin just makes it comfortable for humans. Auto-assignment, budgets, governance gates, and org-chart views remain user-space — a router profile, another plugin, or a reuse of — exactly as listed in the out-of-scope section of the design spec.
This is the surface (or scripts, cron, the dashboard) use to drive the board. Workers running inside the dispatcher use the for the same operations — the CLI here and the tools there both route through , so the two surfaces agree by construction.

```
hermes kanban init                                     # create kanban.db + print daemon hinthermes kanban assign <id> <profile>                    # or 'none' to unassignhermes kanban tail <id>                                # follow a single task's event streamhermes kanban watch [--assignee P] [--tenant T]        # live stream ALL events to the terminalhermes kanban heartbeat <id> [--note "..."]            # worker liveness signal for long opshermes kanban runs <id> [--json]                       # attempt history (one row per run)hermes kanban assignees [--json]                       # profiles on disk + per-assignee task countshermes kanban daemon --force                           # DEPRECATED — standalone dispatcher (use `hermes gateway start` instead)hermes kanban stats [--json]                           # per-status + per-assignee countshermes kanban log <id> [--tail BYTES]                  # worker log from ~/.hermes/kanban/logs/hermes kanban notify-subscribe <id>                    # gateway bridge hook (used by /kanban in the gateway)hermes kanban context <id>                             # what a worker sees        [--author NAME] [--json]                       #   into a full spec and promote to todohermes kanban gc [--event-retention-days N]            # workspaces + old events + old logs
```

All commands are also available as a slash command in the interactive CLI and in the messaging gateway (see below).
is a per-task circuit-breaker override for the dispatcher. blocks the task on the first non-successful attempt, while allows two retries and blocks on the third failure. Omit it to use from , then the built-in default.  
| Caps the number of simultaneously running tasks. When the board already has N running, the dispatcher skips spawning more — useful for slow workers (local LLMs, resource-constrained hosts) so they finish what they have before more pile up and time out. Invalid or below-1 values log a warning and behave as unlimited.  |  
| --- |  
| After produces children with no parent-blocker dependencies, they're automatically promoted to so the dispatcher can pick them up. Set to to require manual review — children stay in until you promote them.  |  
Set on a task to delay dispatch until a specific time. The dispatcher skips ready tasks whose is in the future and picks them up on the first tick after that timestamp.
The dispatcher refuses to re-spawn a ready task when it hit a quota/auth/429 error on the previous run (), or completed a run successfully within the guard window (), or a recent task comment links to a GitHub PR (). This prevents repeat worker storms on the same bug or task while a human catches up. See the row in the .
The dashboard exposes a on the kanban page — drag any card into it to delete the task (cascades through , child links, and subscriptions). A confirmation prompt protects against accidents. Bulk delete is also reachable via with a JSON body .  
creates a durable graph in one shot: a completed root/blackboard card, N parallel worker cards, a verifier card gated on all workers, and a synthesizer card gated on the verifier. Shared swarm context (the "blackboard") is stored as structured JSON comments on the root card so any worker can read it.
The resulting graph dispatches normally — workers run in parallel, the verifier wakes after they all finish, the synthesizer wakes after the verifier marks the work clean.
Every verb is also reachable as — from inside an interactive session from any gateway platform (Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, email, SMS). Both surfaces call the exact same entry point that reuses the argparse tree, so the argument surface, flags, and output format are identical across CLI, , and . You don't have to leave the chat to drive the board.

```
/kanban specify t_abcd                  # flesh out a triage one-liner into a real spec
```

Quote multi-word arguments the same way you would on a shell — parses the rest of the line with , so and both work.
The gateway normally queues slash commands and user messages while an agent is still thinking — that's what stops you from accidentally starting a second turn while the first is in flight. The board lives in , not in the running agent's state, so reads (, , , , , , ) and writes (, , , , , , , …) all go through immediately, even mid-turn.
  * A worker blocks waiting on a peer → you send from your phone and the dispatcher picks the peer up on its next tick. The blocked worker isn't interrupted — it just stops being blocked.
  * You spot a card that needs human context → lands on the task thread and the run of that task will read it in .
  * You want to know what your fleet is doing without stopping the orchestrator → or inspects the board without touching your main conversation.


When you create a task from the gateway with , the originating chat (platform + chat id + thread id) is automatically subscribed to that task's terminal events (, , , , ). You'll get one message back per terminal event — including the first line of the worker's result summary on — without having to poll or remember the task id.

```

```

Subscriptions auto-remove themselves once the task reaches or . If you script a create with (machine output) the auto-subscribe is skipped — the assumption is that scripted callers want to manage subscriptions explicitly via .
Gateway platforms have practical message-length caps. If , , or produce more than ~3800 characters of output, the response is truncated with a hermes kanban …` in your terminal for full output)` footer. The CLI surface has no such cap.
In the interactive CLI, typing and hitting Tab cycles through the built-in subcommand list (, , , , , , , , , , , , , , , , , ). The remaining verbs listed in the CLI reference above (, , , , , , , , , ) also work — they're just not in the autocomplete hint list yet.  
Workers receive and namespace their memory writes by prefix. The board, the dispatcher, and the profile definitions are all shared; only the data is scoped.
When you run from the gateway (Telegram, Discord, Slack, etc.), the originating chat is automatically subscribed to the new task. The gateway's background notifier polls every few seconds and delivers one message per terminal event (, , , , ) to that chat. Completed tasks also send the first line of the worker's so you see the outcome without having to .
You can manage subscriptions explicitly from the CLI — useful when a script / cron job wants to notify a chat it didn't originate from:
A task is a logical unit of work; a is one attempt to execute it. When the dispatcher claims a ready task it creates a row in and points at it. When that attempt ends — completed, blocked, crashed, timed out, spawn-failed, reclaimed — the run row closes with an and the task's pointer clears. A task that's been attempted three times has three rows.
Why two tables instead of just mutating the task: you need for real-world postmortems ("the second reviewer attempt got to approve, the third merged"), and you need a clean place to hang per-attempt metadata — which files changed, which tests ran, which findings a reviewer noted. Those are run facts, not task facts.


Downstream children read the most recent completed run's summary + metadata for each parent. Retrying workers read the prior attempts on their own task (outcome, summary, error) so they don't repeat a path that already failed.

```

```

The same handoff is reachable from the CLI when you (the human) need to close out a task a worker can't — e.g. a task that was abandoned, or one you marked done manually from the dashboard:

```
#   #  OUTCOME       PROFILE           ELAPSED  STARTED#   1  blocked       worker               12s  2026-04-27 14:02#   2  completed     worker                8m   2026-04-27 15:18
```

Runs are exposed on the dashboard (Run History section in the drawer, one coloured row per attempt) and on the REST API ( returns a array). with forwards both to the kernel, so the dashboard's "mark done" button is CLI-equivalent. rows carry the they belong to so the UI can group them by attempt, and the event embeds the first-line summary in its payload (capped at 400 chars) so gateway notifiers can render structured handoffs without a second SQL round-trip.
is refused — structured handoff is per-run, so copy-pasting the same summary to N tasks is almost always wrong. Bulk close / still works for the common "I finished a pile of admin tasks" case.
If you drag a running task off in the dashboard (back to , or straight to ), or archive a task that was still running, the in-flight run closes with rather than being orphaned. The row is always in a terminal state when is , and vice versa — that invariant holds across CLI, dashboard, dispatcher, and notifier.
Completing or blocking a task that was never claimed (e.g. a human closes a task from the dashboard with a summary, or a CLI user runs ) would otherwise drop the handoff. Instead the kernel inserts a zero-duration run row () carrying the summary / metadata / reason so attempt history stays complete. The / event's points at that row.
When the dashboard's WebSocket event stream reports new events for the task the user is currently viewing, the drawer reloads itself (via a per-task event counter threaded into its dependency list). Closing and reopening is no longer required to see a run's new row or updated outcome.
Two nullable columns on are reserved for v2 workflow routing: (which template this task belongs to) and (which step in that template is active). The v1 kernel ignores them for routing but lets clients write them, so a v2 release can add the routing machinery without another schema migration.
Every transition appends a row to . Each row carries an optional so UIs can group events by attempt. Kinds group into three clusters so filtering is easy ():  
| Worker wrote / and task hit . is the first-line handoff (400-char cap); full version lives on the run row. If is called on a never-claimed task with handoff fields, a zero-duration run is synthesized so still points at something.  |  
| --- |  
| Hidden from the default board. If the task was still running, carries the of the run that was reclaimed as a side effect.  |  
| Dashboard drag-drop wrote a status directly (e.g. ). Carries the of the run that was reclaimed when dragging off ; otherwise is NULL.  |  
| --- |  
| Task ran longer than (default 4 h) AND no arrived in the last hour. Dispatcher SIGTERM'd the host-local worker (if any), reset the task to for re-dispatch. Does NOT tick the failure counter (stale is dispatcher-side absence detection, not a worker fault). Workers running long operations should call at least once an hour to avoid this.  |  
| --- |  
| Dispatcher refused to re-spawn this ready task this tick. Reasons: (last failure was a quota/auth/429 error — wait for the rate window to reset), (a completed run happened in the last hour — wait for review before re-running), (a GitHub PR URL appears in a recent comment — a prior worker already opened a PR). The task stays in ; the next tick gets another chance to spawn. If the underlying condition persists, the normal circuit breaker will auto-block via after failures.  |  
| Worker exited successfully while the task was still , usually because it answered without calling or . The dispatcher also emits and auto-blocks immediately instead of retrying.  |  
| Circuit breaker fired after N consecutive non-successful attempts. Task auto-blocks with the last error. The effective limit resolves as task , then dispatcher / , then the built-in default.  |  
Kanban is deliberately single-host. is a local SQLite file and the dispatcher spawns workers on the same machine. Running a shared board across two hosts is not supported — there's no coordination primitive for "worker X on host A, worker Y on host B," and the crash-detection path assumes PIDs are host-local. If you need multi-host, run an independent board per host and use / a message queue to bridge them.
The complete design — architecture, concurrency correctness, comparison with other systems, implementation plan, risks, open questions — lives in . Read that before filing any behavior-change PR.
  *   * 


