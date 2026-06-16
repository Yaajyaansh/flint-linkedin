# Flint Content System — Michelle Lim

LinkedIn and X content system for Michelle Lim, CEO of Flint (@michlimlim). 1 post/day on LinkedIn, 8:30–9am PT.

## How to use

Open the repo in Claude Code → the orchestrator (`CLAUDE.md`) loads automatically.

## Structure

```
_system/                        ← shared writing rules (never edit per post)
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
    content-buckets.md          ← 214 top/mid/bottom funnel prompts

flint/
  context/
    icp.md                      ← who Flint sells to
    positioning.md              ← what Flint does + why they win
    pricing.md                  ← packages, tiers, pricing
    messaging.md                ← key messages, proof points, differentiators
    voice.md                    ← Michelle's tone, personality, phrases
    first-party.md              ← website, product, docs, competitors, story
    content-buckets.md          ← Michelle's specific top/mid/bottom buckets
  posts/
    published/                  ← all published posts (voice reference — never delete)
    top-posts.md                ← highest-performing posts for structure reference
  hooks/
    michelle-hook-templates.md  ← Michelle's proven hook structures
    hook-swipe-file.md          ← external hook patterns adapted for Michelle
  ideas/
    ideas-queue.md              ← generated ideas ready to write
  drafts/
    [YYYY-MM-DD]-[slug].md      ← drafts pending approval
  writing/
    patterns.md                 ← content-type templates and closing line rules
    examples.md                 ← annotated examples from published posts
    workflow.md                 ← pre-submit checklist and edge case handling

CLAUDE.md                       ← orchestrator (read this first)
```
