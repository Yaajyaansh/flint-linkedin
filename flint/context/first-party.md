# First-Party Context — Flint (flint.com)

## 2026 repositioning (superseding note)

As of the website refresh captured 2026-09-22, Flint repositioned from a pages-only platform to two products under one platform: **Pages** (the original on-brand page generation) and **Agents**, launched as the **Google Ads Agent**. New tagline: "the first self-improving system for performance marketing." Core line: "Your tools tell you what happened. Flint tells you what to run next, then ships it." CTA banner: "Scaling Spend Shouldn't Scale Your CAC" — book a demo for a risk-free pilot, dedicated account expert, ships on your own domain, no engineering required. ICP language has sharpened to **performance marketers** specifically (heavy Google Ads spenders), not just demand gen/growth marketers broadly — see `icp.md` for the updated primary ICP. Sections below are updated with the new product and proof points; anything not mentioned here (founding story, team, older positioning) still holds.

### Google Ads Agent — what it does
Reads a connected Google Ads account (one OAuth flow, same setup as Pages) and surfaces what's costing conversions: negative keywords to add, ad groups pointed at a generic/homepage page instead of a dedicated one, underperforming pages worth swapping, and keyword clusters with no page at all. Marketer reviews and approves in chat; Flint pushes the change directly to the Google Ads account and ships/publishes any new page. Every approved or rejected recommendation feeds back into the system ("Sharpen") so future recommendations are grounded in what's already been tried — this feedback loop is the "self-improving" part of the tagline.

**The core insight behind it (useful for hooks):** marketers already know what's wrong with their account — the weekly review surfaces the negative keyword, the underperforming page, the missing page for a hot keyword cluster. The problem was never insight, it was execution time. "You could add the negative keyword yourself. You won't. Not because you're lazy. Because your weekly review produces a list that takes hours to execute, and those hours don't exist."

### New case studies / proof points (2026 refresh)
- **BoomPop:** runs six figures a month in Google Ads. The Agent flagged an H1/H2 rewrite on their top-spend campaign, matched to actual search intent. Flint shipped the variant in under an hour. 14 days later: 5.29% conversion vs. the original's 0.53% — roughly a 10x lift. Quote — Alex Alexin, Director of Demand Generation, BoomPop: "If I'm just staring at Google campaigns, I think, where do I start? Flint gives me that starting point."
- **11x:** comparison pages converted at 3x the rate of campaigns pointed at the homepage. 28 pages (20 industry + 8 comparison) built in a single session — work that used to take a quarter. Quote — Connor Nowinski, COO, 11x: "The competitive battle card is driving exceptional results, from single digit conversion to double digit conversion."
- **Forus:** tripled paid media conversions and saved 70 hours of manual website work.
- **Graphite:** cut CAC by 50% with targeted landing pages built in minutes. (Supersedes/extends the earlier "doubled conversions" proof point — both can be used, cite whichever is more relevant.)
- **LangChain:** when they rebranded, every Flint-built page updated in about 2 hours; the rest of their site took weeks.
- **Cognition** — Theo Marcu, Head of Growth: "With Flint, our pages went live within days. We were so impressed with the speed and quality that now Flint has expanded to multiple organizations beyond the growth team."
- **Modal** — Margaret Shen, Head of GTM & BizOps: "Flint took what would've taken months and turned it into live pages shipped months early. And the pages immediately ranked #1 on Google and ChatGPT."
- **CodeRabbit** — Sahil M Bansal, GTM PM: "Flint understood my goal with one prompt, upgraded our HubSpot CTA embed, and drove hundreds of leads. That's when I realized this isn't a page builder, it's a growth multiplier."
- **Anomalo** — David Ronen, Director of Growth: "Flint is the first tool I've seen that keeps the marketer's judgment in the driver's seat."

### New/expanded customer logos
Windsurf, Highbeam, Minoan, Pickle, Actively AI — in addition to the existing roster (Graphite, Cognition, LangChain, BoomPop, Glean, 11x, Amigo, Tandem, Modal, Forus, CodeRabbit, Reducto).

### New comparison pages
Flint vs Lovable, Flint vs Mutiny, Flint vs Claude Code, and Flint + Webflow (Webflow is now framed as an integration partner in this one, not a straight competitor).

### Huge new proof point (from the Performance Marketing Strategist job posting, 2026-09)
Flint just signed a **Fortune 10 customer**, and within **48 hours** their customer acquisition cost dropped **50%**. Not yet used in any published post — strong standalone-post material on its own, don't bury it as a footnote in something else.

### TechCrunch-quotable Sandberg story
From a TechCrunch piece: Michelle told Sandberg how it took her team "five teams, three months to build one A/B test just to increase conversion by 10% on our Google ad." Sandberg's response: "Michelle, it was 140 people at Meta who had to do this." Real, attributed, citable — matches the "when Sheryl Sandberg invested" hook pattern already in `voice.md`.

### Dan Levine (Accel) quote
"One of the most talent-dense AI startups... each member of the early Flint team has a track record, and as a team, they perform like athletes. Amazing to watch."

### Updated co-founder backgrounds
**Michelle Lim:** Engineer #1 turned Head of Growth *and Product* at Warp (Product is a new addition to her documented bio).
**Max Levenson (CTO/Co-founder):** engineering leadership at Nuro (autonomous vehicle startup), then Engineer #2 at Vooma (YCS23) — before Flint. (Supersedes the vaguer "owns all engineering decisions" line — keep both, this is the specific career path.)
**Team alumni of:** Netflix, Scale, and Shepherd (YC W21), in addition to previously documented Figma/Reddit/Meta backgrounds. Office described as "historic Jackson Square."

### New role: Performance Marketing Strategist (San Francisco, on-site, Client Services)
Reports to the **Chief Revenue Officer** (first documented mention of a CRO at Flint). Owns Google Ads performance for a portfolio of brands/agency partners (Meta Ads joining soon). Explicitly **not** a generic performance-marketer grind role — the JD's own framing: uses Flint in live customer accounts to work faster and catch problems manual review misses, spends time on optimization judgment/strategy/customer communication rather than manual search-term combing, and feeds recurring problems back to product/engineering. This role is the live example of the "automate the grunt work, hire for judgment" philosophy — useful for any post connecting Flint's hiring practice to that thesis.

---

## The Company

**Name:** Flint (formerly Flint AI, was tryflint.com → now flint.com)
**Founded:** ~early 2024
**Stage:** Series A (raised $5M, backed by Accel + Sheryl Sandberg)
**Team size:** ~10 people
**HQ:** Jackson Square, San Francisco

**What they do (one sentence):**
Flint is the AI marketing site platform that audits your website, recommends the pages you're missing, and ships on-brand landing pages for ads, ABM, SEO, and AEO — without engineering.

**What they do (full explanation):**
Flint starts by ingesting your website and cloning your design system (takes 1-2 hours). It then runs a full audit: audits your paid ads, competitive landscape, industry coverage, and AEO readiness to surface the specific pages you should build. You select the ones you want and get fully on-brand pages ready to publish. Every page is hosted on your domain, connected to your analytics and forms, and continuously A/B tested. The MCP and API mean Flint can be triggered from Claude, Clay, Relay, Zapier, or any workflow tool — enabling fully autonomous page generation.

---

## Website & Positioning

**Website:** https://flint.com (also https://app.tryflint.com for signup)

**Headline / hero copy:**
"Your ads are running. Your pages aren't keeping up."
"Flint analyzes your site, recommends what to build, and ships on-brand landing pages, so every ad gets a page that converts."

**Key pages:**
- Homepage: AI-powered audit + page generation, social proof from Graphite/Cognition/LangChain etc., free trial CTA
- Pricing: Free ($0, 160 credits/mo) → Starter ($96/mo annual, 12K credits/yr) → Pro ($400/mo annual, 60K credits/yr) → Enterprise (custom)
- Product: MCP/API integration showcase (Claude, Clay, Zapier)
- Customers: Graphite, Cognition, 11x, Amigo, BoomPop, Windsurf, LangChain, Tandem, Glean, Modal, Forus, CodeRabbit, Reducto, Actively AI
- Blog: Mix of SEO-targeting stats articles and strategic thought leadership

---

## Product / Service

**Core offering:**
AI platform that clones your design system and generates on-brand landing pages at scale, with a strategy layer that tells you what pages to build.

**Key features / deliverables:**
- Website audit: surfaces missing pages (comparison, industry, ABM, AEO, paid ads)
- Design system import: one-click, clones your visual identity from your live site
- Page generation: AI creates pages from your design system + market research
- Hosting: pages live on your domain (root domain on Pro: yoursite.com/pages)
- MCP + API: trigger page generation from Claude, Clay, Zapier, Relay
- A/B testing: continuous optimization built in
- Pre-launch QA: checks for broken links, missing analytics tags, 404s, missing OG images
- Logo wall: auto-pulls from CRM, all logos normalized to black-on-transparent

**What makes it different:**
- Actually on-brand (not template-based) — design system cloning is a solved research problem at Flint
- Strategy layer — not just a builder, it tells you what to build
- Infrastructure play — MCP/API means it's load-bearing in the marketing stack
- Autonomous loop — pages A/B test themselves, logo wall updates from CRM, case studies auto-generated

**What it is NOT:**
- Not a general-purpose website builder (not competing with Webflow for full site builds)
- Not a copywriting tool
- Not a design tool (your design system is the input)
- Not a CMS replacement (it's a parallel layer, though the long-term vision replaces CMS)

---

## Results & Proof Points

- **LangChain:** $0 → 6 figures pipeline in 6 weeks. 17 pages built in <2 hours. Paid search spend doubled. "We went from zero pipeline to 6 figures with Flint pages."
- **Graphite:** doubled conversions. 7 figures ARR influenced.
- **Tandem:** tripled conversions
- **BoomPop:** 4x conversion rate. 85% lower cost per conversion. 50+ pages built.
- **BoomPop Google Ads:** 10 conversions in 3 days (was 0). Quality Score improved significantly.
- **11x comparison page:** ranked #1 on Google within minutes of going live. Cited in Claude + Google AI Overview. 3x homepage conversions.
- **Cognition:** doubled conversions
- **Amigo:** 3 million patient encounters, zero safety incidents (healthcare customer)
- **Kargo:** prospect took call same-day from cold outbound email with pre-built page attached. Verbally committed by end of call.
- **Connor (11x):** was showing Flint to a prospect, building a paid search landing page together live. Reaction: "it was so easy to make a landing page i thought i was doing something wrong." Brand context was already loaded; the page (matched to his brand + his ads) was two prompts away. Conversions tripled. Fed back over Slack.

---

## Competitors

| Competitor | What they do | Flint's differentiation |
|---|---|---|
| Webflow | Visual web builder | Dev-dependent, not AI-native, no strategy layer |
| Framer | Design-forward web builder | Dev-adjacent, template-based for landing pages |
| Instapage / Unbounce | Legacy landing page builders | Manual, template-based, no on-brand AI generation |
| Mutiny | Website personalization | Enterprise-only, no generation, complex implementation |
| Lovable / Claude Code | AI-assisted vibe coding | Off-brand outputs, no marketing layer, no optimization loop |
| Folloze / Uberflip | ABM content hubs | Content experiences, not conversion-optimized landing pages |

**How Flint talks about competitors:**
Names them in comparison pages (SEO/AEO strategy) and in Michelle's posts when making a specific contrast point. Doesn't trash; makes the functional difference clear. "Anyone can vibe code a landing page. Productizing it is the hard part."

---

## Founding Story

Michelle Lim grew up in Singapore, won a national science award at 17, got into Singapore's top medical school — and turned it down to attend Yale. There, she took her first CS class on a whim and fell in love with coding. After Meta (FBU), Robinhood, Slack, and Robinhood internships, she joined Warp as the first engineer and Head of Growth. At Warp she scaled the product to 500K weekly active developers. She left to start Flint after watching marketing and engineering teams consistently talk past each other: great campaigns landing on wrong pages, every landing page blocked by a dev queue. She spent weeks talking to 100 people, ran two-week interview sprints, and narrowed in on the marketing site (CMS layer) as the highest-retention, highest-value thing to rebuild with AI. Flint was incorporated, raised from Accel and Sheryl Sandberg, and launched publicly in Feb 2025. Acquired flint.com in May 2026.

---

## Key People

**Michelle Lim (CEO / Co-founder)**
Background: Yale CS, Meta/FBU, Robinhood, Slack, Warp (first engineer + Head of Growth)
LinkedIn: linkedin.com/in/michlimlim
Known for: Founder-led content (100 posts in 3 months), SF marketing community events (Devil Wears Prada screenings, pottery nights), running a 10-person AI company that ships like 100

**Max Levenson (CTO / Co-founder)**
Background: Engineering lead. Owns all engineering decisions. Clear split with Michelle (she owns growth).

**Leona H. (Founding Designer)**
Former Head of Growth Design at Netflix. Ships multiple PRs/week despite no prior coding background. "One of the most thoughtful people I know."

**Naomi Jung (Senior Staff Engineer)**
Former Senior Staff Engineer at Figma. Led rebuild of Figma's component instance architecture used by millions.

**Erica Yoon (Founding Marketer)**
12 years experience: Meta, Reddit, BuildOps. Manages dozens of AI marketing agents.

**Ed Farraye (Growth Advisor)**
Growth advisor for Linear, Reddit, LangChain, Warp. Investor in Flint. Growth consultant.

---

## Docs / Resources

- Docs: flint.com/docs
- Blog: flint.com/blog
- Case studies: flint.com/customers
- Pricing: flint.com/pricing
- Free audit tool: flint.com (homepage) — no login, 90-second audit
