---
url: "https://news.ycombinator.com/item?id=47658091"
title: "Show HN: Mantyx – Agent Control Plane with Centralized MCP Management | Hacker News"
engine: duckduckgo
rank: 27
published: unknown
updated: unknown
author: unknown
org: unknown
char_count: 1581
fetched_at: "2026-05-31T17:38:38.777180+00:00"
---

|   
 |   
 |  Centralized management is one half of the problem. The other half is how agents discover which MCP servers even exist in the first place. Right now you have the official MCP Registry, a bunch of GitHub-based lists, and individual vendors maintaining their own catalogs. If you're running Google's A2A agents alongside MCP, you need a totally separate discovery path.The IETF currently has somewhere around 8 competing drafts for standardizing agent discovery -- agents.txt, ARDP, AID, AINS, and others. The original agents.txt draft actually expires April 10, so that whole space is in flux. Until there's a standard way to discover servers across protocols, any control plane is limited to whatever servers you manually configure.  |  
| --- |  
 |  
|   
 |  That is 100% true. We are currently observing those specs and how they evolve to decide which and how to implement them. At the moment we support the ability to bring agents in house via a2a as well as build agents and expose them to third party via a2a.   |  
| --- |  
 |  
|   
 |  Heads up on those drafts: agents.txt (draft-vonbodisco-agents-txt-00) expired April 10 and has not been renewed. That was the simplest one, basically robots.txt for agent capabilities. ARDP and AID go in totally different directions with no convergence in sight.The problem I keep hitting is A2A Agent Cards and MCP manifests use different schemas in different registries. If you are adding discoverability, I would build support for multiple discovery protocols now rather than bet on one draft.  |  
| --- |  
 |  
 |

