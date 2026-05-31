---
url: "https://code.claude.com/docs/en/workflows"
title: Orchestrate subagents at scale with dynamic workflows - Claude Code Docs
engine: google
rank: 10
published: unknown
updated: unknown
author: unknown
org: Claude Code Docs
char_count: 7817
fetched_at: "2026-05-31T19:22:27.816337+00:00"
---

Dynamic workflows are in research preview. They require Claude Code v2.1.154 or later and are available on all paid plans, with Anthropic API access, and on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry. On Pro, turn them on from the Dynamic workflows row in .
A dynamic workflow is a JavaScript script that orchestrates at scale. Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive. Reach for a workflow when a task needs more agents than one conversation can coordinate, or when you want the orchestration codified as a script you can read and rerun. Examples include a codebase-wide bug sweep, a 500-file migration, a research question that needs sources cross-checked against each other, and a hard plan worth drafting from several independent angles before you commit to one.

  
A workflow moves the plan into code. With subagents and skills, Claude is the orchestrator: it decides turn by turn what to spawn next, and every result lands in Claude’s context. A workflow script holds the loop, the branching, and the intermediate results itself, so Claude’s context holds only the final answer. Moving the plan into code also lets a workflow apply a repeatable quality pattern, not just run more agents: it can have independent agents adversarially review each other’s findings before they’re reported, or draft a plan from several angles and weigh them against each other, so you get a more trustworthy result than a single pass. The quickest way to see a workflow in action is to run , the Claude Code includes for investigating a question across many sources. You’ll see agents work through a set of phases in the background while your session stays free, and get one report at the end instead of a turn-by-turn transcript.
Run with a question you want investigated. It fans out web searches across several angles, fetches and cross-checks the sources it finds, and synthesizes a cited report.
Claude Code asks whether to allow the workflow. Select to continue. The exact prompt depends on your permission mode. See for the per-mode options.
The run starts in the background. Run , use the arrow keys to select the run, and press Enter to open its progress view: The view shows each phase with its agent count, token total, and elapsed time. Drill into any phase to see its agents and what each one found. See for the full set of controls.You can also watch from the task panel below the input box: a one-line progress summary appears there while the run is going. Press the down arrow to focus it, then Enter to expand.
When the run finishes, the report lands in your session. It cites the sources each claim came from, with claims that didn’t survive cross-checking already filtered out.
To run a workflow for your own task, , and once a run does what you wanted you can as a command of your own.  
| Fans out web searches on a question across several angles, fetches and cross-checks the sources it finds, votes on each claim, and returns a cited report with claims that didn’t survive cross-checking filtered out. Requires the to be available  |  
| --- |  
Workflows run in the background, so the session stays responsive while agents work. Run at any time to list running and completed workflows, then select one to open its progress view. The progress view shows each phase with its agent counts, token totals, and elapsed time. The footer lists the key for each action:  

To run a single task as a workflow without changing the session’s effort level, include the word anywhere in your prompt. Claude Code highlights the word in your input and Claude writes a workflow script for the task instead of working through it turn by turn. If Claude Code highlights the word when you didn’t mean to trigger one, press to ignore it for this prompt, or press backspace while the cursor is right after the highlighted word. To stop the word from triggering at all, turn off Workflow keyword trigger in . Ultracode is a Claude Code setting that combines with automatic workflow orchestration. With it on, Claude plans a workflow for each substantive task instead of waiting for you to ask. With ultracode on, Claude decides when a task warrants a workflow. A single request can turn into several workflows in a row: one to understand the code, one to make the change, and one to verify it. This applies to every task in the session, so each request uses more tokens and takes longer than at lower effort levels. Ultracode lasts for the current session and resets when you start a new one. Drop back with when you return to routine work. It’s available on models that support ; on other models the menu doesn’t offer it.
  * : start, and skip this prompt for this workflow in this project from now on

  
| First launch only. Any records consent in your user settings, and later launches start without prompting. Skipped entirely when ultracode is on  |  
| --- |  
In the Desktop app, an approval card shows the workflow name, the phase list, and a token-usage caution, with , , and actions. The progress view appears in the Background tasks side pane. Your permission mode controls only the launch prompt above. The subagents the workflow spawns always run in mode and inherit your , regardless of your session’s mode. File edits are auto-approved. Shell commands, web fetches, and MCP tools that aren’t in your allowlist can still prompt you mid-run. To avoid this on a long run, add the commands the agents need to your allowlist before starting. In and the Agent SDK there is no one to prompt, so tool calls follow your configured permission rules without interactive confirmation. When Claude writes a workflow for a task you’ll repeat, you can save that run’s script as a command. A process like a review you run on every branch then runs the same orchestration each time. Run , select the run you want to keep, and press . In the save dialog, Tab toggles between the two save locations:

The workflow runtime executes the script in an isolated environment, separate from your conversation. Intermediate results stay in script variables instead of landing in Claude’s context.  
 |  
|  |  
 |  
Once a run starts, you manage it from the view, or by expanding its progress line in the task panel below the input box. If you stop a run, you can resume it: agents that already completed return their cached results, and the rest run live. Resume a paused run from by selecting it and pressing , or ask Claude to relaunch the workflow with the same script. Resume works within the same Claude Code session. If you exit Claude Code while a workflow is running, the next session starts the workflow fresh. A workflow spawns many agents, so a single run can use meaningfully more tokens than working through the same task in conversation. Runs count toward your plan’s usage and rate limits like any other session. You can stop a running workflow from at any time without losing completed work. Every agent in a workflow uses your session’s model unless the script routes a stage to a different one. To control the model cost:
  * Ask Claude to use a smaller model for stages that don’t need the strongest one when you describe the task

Workflows are available in the CLI, the Desktop app, the IDE extensions, with , and the . The same disable settings apply on every surface.

To turn workflows off for your whole organization, set in , or use the toggle on the page. When workflows are disabled, the bundled workflow commands are unavailable, the keyword no longer triggers a run, and is removed from the menu.


We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy .

