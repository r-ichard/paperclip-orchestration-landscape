#!/usr/bin/env python3
"""Wrapper to run SERP with Google time-bounded filters."""
import sys, asyncio, json
sys.path.insert(0, "/Users/richardraduly/.claude/plugins/cache/r-ichard/ultra-research/0.1.2/skills/research/scripts")
from lib import ENGINES, serp_candidates

# Patch Google template with time filter + date sort
if len(sys.argv) < 3:
    print("Usage: python3 _serp_time.py <tbs> <query>")
    sys.exit(1)

tbs = sys.argv[1]
query = sys.argv[2]
ENGINES["google"] = f"https://www.google.com/search?q={{q}}&hl=en&num=20&tbs={tbs}"

result = asyncio.run(serp_candidates("google", query))
if result["blocked"]:
    print(f"# ⚠️  google BLOCKED: {result['blocked']}")
    print(f"#    ({result['final_url']})")
    sys.exit(0)

links = result["links"]
print(f"# {len(links)} candidate links from google for: {query}  (tbs={tbs})\n")
for i, l in enumerate(links, 1):
    print(f"{i:>2}. {l['text'] or '(no anchor text)'}")
    print(f"    {l['href']}")
    if l["context"]:
        print(f"    ↳ {l['context']}")
