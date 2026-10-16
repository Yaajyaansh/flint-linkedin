# Positioning — Flint (flint.com)

> Updated 2026-10. This replaces the earlier pages-only / "AI marketing site platform" framing. Source: the Google Ads agent, Learning Loop, compare/claude-code, /agencies, and /industries/dtc page copy supplied by the Flint team. If a post draft conflicts with this file, this file wins.

## One-liner

Flint is a managed Google Ads agent that also builds the landing pages. It monitors search terms, auctions, and conversion data 24/7, tests keywords, bids, and ad copy, and ships an intent-matched page for every ad group. A Google Ads strategist guides each account, and nothing ships without a person signing off.

Tagline: "The first self-improving system for performance marketing."
Core line: "Your tools tell you what happened. Flint tells you what to run next, then ships it."
Banner: "Scaling spend shouldn't scale your CAC."

## Category

AI Google Ads agent with pages in the same loop. Flint is no longer described as a page builder. The pages are one part of a system that runs and improves the whole Google Ads account.

## What it does

- **24/7 monitoring and action.** A search term eating budget overnight is paused before the morning. A winning page gets traffic that afternoon. Flint spots surging queries (the examples used are "lollapalooza outfits" and a shark bite in Australia) and buys the keyword with a matching page.
- **Learning Loop.** Flint A/B tests changes so each one informs the next. Where traffic allows, it splits 50/50 between the control and the new page and promotes the winner. Where traffic is thin, it compares pre vs post.
- **Pages in the loop.** Every ad group gets a page built for its intent, on the customer's brand and subdomain. The ad's promise carries through to the page, which helps Quality Score and can reduce lost impression share.
- **Works on every layer of the account.** Account structure, campaigns and budgets, ad groups, keywords and match types, negative keywords, ads and extensions, bidding settings, pages, and reporting.
- **Reporting drafts itself.** Flint remembers the customer's needs and preferences, so the weekly report is not rebuilt by hand.
- **Human in the loop.** A Google Ads strategist helps guide the work. Nothing ships without a person signing off, and every change is logged and reversible.

## Plans

- **Enterprise 360 (fully managed):** a Google Ads expert manages the account, with account structure audits, weekly reports and strategy, and biweekly meetings. The Flint agent covers the account 24/7. Forward-deployed engineers can integrate downstream conversions (CRM, Shopify, attribution).
- **Enterprise (advised):** Flint proposes the changes and builds the pages. The customer's team or agency reviews and approves what ships, with monthly guidance from a Client Services Manager.
- **Entry point:** a 2 to 3 week pilot. Setup takes about 30 minutes, first changes ship within days, and the first report lands the following week.
- **CTA:** "Book a demo" (sales-assisted for DTC and agencies: "Talk to sales" / "Talk to partnerships").

## Why they win

1. **Ads and pages in one loop.** Flint is the first ads agent that also has pages in its stack. Ads usually live with an agency and pages with design, so the click lands on something generic. Query to ad to page alignment improves landing page experience.
2. **The feedback loop, not just the output.** Any AI tool can generate a page. What it can't generate is which page won, against what traffic, and what to build because of it.
3. **Owns the page, deployment, and tracking.** That cuts the gap between insight and test from days to hours.
4. **Safe for the ad account.** Flint works directly with Google, and every write goes through a reviewed, rate-limited path. DIY tools and AI scripts have gotten Google Ads accounts banned (a first-hand LinkedIn account is linked on the product page).
5. **Strategist plus 24/7 agent.** The strategist advises on account strategy and the agent catches overnight opportunities.
6. **Revenue attribution.** Click ID and page variant ride into the CRM or Shopify orders, so every lead or sale traces back to the keyword and page. Flint reads Northbeam or Triple Whale without replacing them.

## Why they lose deals / limits to respect in content

- Buyers who want to keep their own repo or Shopify theme for the pages. The pages live on a subdomain because the loop only runs fast when one system finds the opportunity, publishes the page, and measures it.
- Search only today. Meta is in beta. PMax and Shopping are not managed by Flint yet.
- No self-hosting. The agent runs against Flint's customer-facing API with customer-scoped keys.
- The MCP server only generates and edits Flint pages from Claude, Cursor, or any MCP client. Ads changes and experiments are not exposed through the MCP yet.
- Exports are via Chrome extensions, so don't claim "no lock-in" more strongly than that.

## Their unique point of view

Managed agents are the only way to win Google Ads. Search demand shifts, competitors change bids, and ad performance decays every day. A weekly review produces a list that takes hours to execute, and those hours don't exist. The system that finds the opportunity should be the one that ships the page and measures it.

## How they're positioned vs. alternatives

| Alternative | What they do | Why Flint wins |
|---|---|---|
| Building it yourself with Claude Code or Cursor | Generates pages, lists, and scripts | You'd need six months of multiple senior engineers plus an ads practitioner for a v1 you'd trust with your spend, then an engineer every day and a practitioner watching the agent. A base model also can't tell you which page won, and DIY AI scripts have gotten ad accounts banned. |
| Ad agencies and in-house buyers | Manage bids and ads, review accounts a couple of times a week | Flint audits every account daily and builds the page for each recommendation. For agencies, Flint is a partner: the Advised plan lets buyers review a queue and ship, priced per client. |
| Webflow / Framer | Visual web builders | Dev-dependent, no ads layer, no learning loop |
| Instapage / Unbounce | Legacy landing page builders | Templates and manual work, no ads agent |
| Mutiny | Website personalization | Enterprise-only, no page generation or ads |
| Lovable / vibe coding | AI-assisted web dev | Generic, off-brand output with no optimization loop |

Cleanest contrast: "Anyone can generate a page. What you can't generate is the feedback."

## Segments with their own pages

- **B2B and AI companies:** performance marketers spending on Google Ads (see `icp.md`).
- **DTC and e-commerce:** orders measured in Shopify and other platforms, a page for every product intent and offer, creative-matched Meta pages (beta), AOV optimization. Pickle is the hero case study.
- **Agencies:** the Advised plan per client account. Buyers review a multi-client queue with pages attached. Proof: Camber Health built 38 pages in the first sprint with agency Bordeaux & Burgundy.

## The "aha moment"

A $24k/month campaign sending every click to the homepage. Flint flags it, builds an intent-matched page, switches the ads, and the split test converts 55% above control (live demo example). Control sat at 1% conversion, the Flint page at 2%.

## Common misconceptions about them

- **"It's a page builder."** The pages are one layer of a managed Google Ads agent.
- **"It will take over my account."** A strategist guides it, nothing ships without sign-off, and every change is logged and reversible.
- **"AI pages look AI-generated."** Pages pull from the customer's design system (Figma import and an editable brand kit) and carry their brand voice.
- **"We can just vibe code this."** See the Claude Code row above.
- **"It's only for paid ads."** Google Search is the live channel today, but pages also support ABM, comparison, and AEO use cases (see `first-party.md`).

## Older framing (pre-2026-10), kept for history

Earlier copy called Flint "the AI-powered marketing site platform that audits your website, recommends the pages you're missing, and ships fully on-brand landing pages," built around the free audit tool and the MCP/API. Don't lead with that framing in new posts.
