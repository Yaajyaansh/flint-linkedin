# LinkedIn Content System

Multi-agent LinkedIn content system. One repo, one Claude Code session per client.

## How to use

1. Duplicate `clients/_template/` → rename to `clients/[client-name]/`
2. Fill in all files in `clients/[client-name]/context/`
3. Run the orchestrator: `claude` → point it at `CLAUDE.md`

## Repo structure

```
_system/                        ← shared across ALL clients (never edit per-client)
  forbidden/
    phrases.md                  ← never use these exact phrases
    sentence-structures.md      ← never use these patterns
    writing-patterns.md         ← never use these habits
  hooks/
    hook-writing-101.md         ← the full hook methodology
    hook-examples.md            ← 150 real top-performing hooks + templates
  writing/
    human-writing-prompt.md     ← master prompt for writing like a human
    formatting-rules.md         ← how to format posts (→, 1/, —, CAPS etc)
    content-buckets.md          ← top/mid/bottom funnel buckets + prompts

clients/
  _template/                    ← copy this for every new client
    context/
      icp.md                    ← who they sell to
      positioning.md            ← what they do + why they win
      pricing.md                ← packages, tiers, pricing
      messaging.md              ← key messages, proof points, differentiators
      voice.md                  ← tone, personality, things they say / don't say
      first-party.md            ← website, product, docs, competitors, their story
      content-buckets.md        ← their specific top/mid/bottom buckets
    posts/
      published/                ← past posts (for voice learning)
    ideas/
      ideas-queue.md            ← generated ideas ready to write
    drafts/
      [YYYY-MM-DD]-[slug].md    ← drafts pending approval

CLAUDE.md                       ← orchestrator system prompt (read this first)
```
