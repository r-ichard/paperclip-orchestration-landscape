# Agent-Orchestration Landscape

An evidence-grounded interactive research map exploring how open-source projects solve the problem **Paperclip** solves: coordinating many heterogeneous AI agents toward a goal.

**Live site:** [https://paperclip-alternatives.netlify.app](https://paperclip-alternatives.netlify.app)

## What's inside

- **Landscape Map** — Position every tool on two axes: single-agent vs multi-agent, and library vs managed control plane.
- **Tool Cards** — Filterable cards with license, closeness score, dimension chips, and source count.
- **Comparison Matrix** — Capability matrix vs. Paperclip's seven pillars (Orchestration, Governance, Budget, Hierarchy, Heterogeneity, Scheduling, Durable State).
- **The Architecture Debate** — Three preserved positions on whether to build multi-agents at all.
- **Coordination Patterns** — 13 recurring topologies underlying the tools above.

## Methodology

Built strictly from **51 captured web sources** (4 Paperclip's own docs/site + 47 alternative/approach sources), filtered to open-source / self-hosted projects and practitioner/vendor/academic discussion. Every claim traces to a captured source; nothing is invented.

- Tool positions and closeness scores are **editorial synthesis**, grounded in source descriptions — interpretive, not measured.
- A blank matrix cell means **the captured sources did not address that dimension** — it is not a claim the capability is absent.
- Purely commercial products were out of scope per the open-source filter.
- 3 candidate sources were dropped during collection (1 SEO-thin, 1 Cloudflare-blocked, 1 off-topic).

## Evidence locker

The full set of captured source files lives in [`sources/`](./sources/). Each file is named by origin domain and date of capture.

## Baseline

- [paperclip.ing](https://paperclip.ing/)
- [github.com/paperclipai/paperclip](https://github.com/paperclipai/paperclip)

## Deploy

This is a static HTML site. It deploys automatically to Netlify from the `main` branch.

```
npx netlify-cli deploy --prod --dir .
```

Or connect the repo at [netlify.app](https://app.netlify.com/) → Add new site → Import from Git → pick this repo.

## License

The research HTML and this README are shared as-is for reference. Source files retain their original authors' rights.
