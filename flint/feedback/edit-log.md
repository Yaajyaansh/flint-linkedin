# Edit Log — Original Drafts vs. Michelle's Edits

This is a running record of every time Michelle takes a Claude draft and edits it herself. It is a **log, not a rulebook** — the actual rules extracted from these edits live in their canonical files (`_system/forbidden/*.md`, `flint/context/voice.md`, `flint/writing/patterns.md`, `flint/hooks/michelle-hook-templates.md`). This file exists so we can trace *why* a rule was added and *when*, and so patterns that show up more than once get caught even if no single edit looked like a rule on its own.

Never delete entries. Append only.

---

## How entries get created

1. Human provides original draft + Michelle's edited/final version of the same post.
2. Diff the two, line by line.
3. Classify each meaningful change (see categories below).
4. Log the entry using the template below.
5. Route generalizable changes to the correct canonical file immediately — don't just log and stop.
6. One-off factual corrections or unrepeatable stylistic swaps get logged but don't generate a new rule. If the same one-off shows up a second time across different posts, it's no longer one-off — promote it to a rule.

## Categories and where they route

| Category | Routes to |
|---|---|
| Single banned word or exact phrase | `_system/forbidden/phrases.md` |
| Sentence-level structure (reversal framing, rhetorical question, anaphora, asyndeton, "Most X" openers) | `_system/forbidden/sentence-structures.md` |
| Broader AI-pattern (cliché opening, filler adverb, artificial symmetry, generic transition) | `_system/forbidden/writing-patterns.md` |
| Voice/tone shift ("I" vs "we", a reference she adds/removes, a phrase she reaches for, something she'd "never say") | `flint/context/voice.md` |
| Structural/template preference (how she opens or closes a specific post type, formatting choice) | `flint/writing/patterns.md` |
| Hook-specific change | `flint/hooks/michelle-hook-templates.md` |

---

## Entry template

```
## [YYYY-MM-DD] — [post slug or short topic label]

**Original (Claude draft):**
> ...

**Michelle's edit:**
> ...

**What changed:** [one line — what she cut, added, or rewrote]
**Category:** [from table above]
**Generalizable:** yes/no — [if no, why this is a one-off]
**Routed to:** [file] — [exact rule added, or "none — logged only"]
```

---

## Entries

## 2026-07-03 — 11x-connor-feedback-post

**Original (Claude draft):**
> Best feedback we've gotten in a while:
>
> "it was so easy to make a landing page i thought i was doing something wrong"
>
> That's what AI for marketing should feel like. Something that just handles it.
>
> With Flint it happens because you can ship landing pages without having to think about design, brand, or engineering.
>
> We spent a long time making it feel that simple.

**Michelle's edit:**
> Best feedback we've gotten in a while - came in over Slack from @Connor at 11x.
>
> He was showing Flint to someone and they were building a paid search landing page together.
>
> Their reaction: "it was so easy to make a landing page i thought i was doing something wrong."
>
> All brand context was already loaded into Flint. The page (matched to his brand + his ads) was two prompts away. What would've taken weeks to build before took minutes.
>
> And their conversions tripled.
>
> We spent a long time making it feel that simple.

Michelle's overall note: "this is a super generic / vague post. nothing here is likeable about this. make posts more specific (ask Viktor - our AI knowledge slack bot for context)."

### (a) No named source, no scene, no channel
**What changed:** Added "came in over Slack from @Connor at 11x" and a one-line scene of what he and the prospect were doing.
**Category:** Structural/template preference (testimonial posts need attribution as a structural element)
**Generalizable:** yes — this is the core complaint ("super generic/vague," "nothing likeable")
**Routed to:** `flint/writing/patterns.md` — added a "Customer feedback / testimonial" template requiring named source (person + company + channel), a scene, the quote, mechanism, and a number.

### (b) Generic thesis statement cut
**What changed:** Cut "That's what AI for marketing should feel like. Something that just handles it." entirely — no replacement.
**Category:** Broader AI-pattern (generic category claim / thesis-states before earning it)
**Generalizable:** yes
**Routed to:** `_system/forbidden/writing-patterns.md` — new "Abstract Category Explanations" section, bullet on "X should feel like" claims.

### (c) Vague mechanism replaced with concrete detail
**What changed:** "you can ship landing pages without having to think about design, brand, or engineering" → "All brand context was already loaded into Flint. The page (matched to his brand + his ads) was two prompts away. What would've taken weeks to build before took minutes."
**Category:** Broader AI-pattern (abstract category listing standing in for the real mechanism)
**Generalizable:** yes — same failure mode as (b), listing categories instead of naming the artifact/action
**Routed to:** `_system/forbidden/writing-patterns.md` — same new section, bullet on "without having to think about X, Y, or Z" constructions.

### (d) Missing quantified result added
**What changed:** Added "And their conversions tripled." — no result of any kind existed in the original.
**Category:** Structural/template preference (testimonial/case-study posts need a hard number, not just the anecdote)
**Generalizable:** yes
**Routed to:** `flint/writing/patterns.md` — folded into the same new testimonial template (fifth required element: quantified result).

### (e) Resource for specificity: Viktor
**What changed:** N/A (operational note from Michelle, not a text edit) — she pointed to Viktor, Flint's internal AI knowledge Slack bot, as the source to check when a draft is too generic.
**Category:** Workflow/resource, not a voice or forbidden-pattern rule
**Generalizable:** yes
**Routed to:** `flint/writing/workflow.md` (Edge cases — new entry for generic/vague drafts) and `flint/writing/patterns.md` (testimonial template) and `_system/forbidden/writing-patterns.md` (pointer in the new section).

### (f) New first-party fact captured
**What changed:** Connor/11x anecdote (quote, mechanism, tripled conversions) wasn't in `flint/context/first-party.md` before this post.
**Category:** First-party fact, not a rule
**Generalizable:** n/a — factual grounding
**Routed to:** `flint/context/first-party.md` — added as a new line under Results & Proof Points.

---

## 2026-07-03 — katie-goldstein-origin-story

**Original (Claude draft):**
> Flint wouldn't exist without @Katie Goldstein.
>
> Story time: I met her at a Christmas party in 2024 and liked her energy so much that I tracked down her number through multiple people just to stay in touch.
>
> She thought Max and I would get along and that our values aligned, so she intro-ed us.
>
> Max and I met on Christmas eve. I was already heads down building and he was also locked in, so we met at a bar, and decided to do a work trial for a week.
>
> That was the start of Flint.
>
> Katie still comes by the office just to hang and help. This is her stopping by just last week on a whim. Just someone who believed in us before there was anything to believe in.

**Michelle's edit:**
> [same opening through "That was the start of Flint."]
>
> Fast forward to today: we're a team of 8, building the agentic website platform for lean marketing teams.
>
> Katie still comes by the office just to hang and help. This is her stopping by just last week on a whim. Just someone who believed in us before there was anything to believe in.
>
> If you want to join us, head over to flint(dot)com/careers.

Michelle's note: "this is fine given its a team post and it will do okay. but the thing is that it doesn't talk about flint. try to find indirect ways to talk about flint / mention what flint does."

### (a) Indirect product bridge line + careers CTA added to a personal/team story
**What changed:** Inserted "Fast forward to today: we're a team of 8, building the agentic website platform for lean marketing teams." before the closer, and added a careers CTA at the very end.
**Category:** Structural/template preference — but **flagged as a contradiction** first: `flint/writing/workflow.md` currently says Friday/Sunday personal posts get "no product push." This edit adds exactly that to a personal/team-origin post. Precedent exists in published posts too (e.g. "PS: we're hiring. Come work in the office you just watched.").
**Generalizable:** Asked human directly — answer: **case-by-case, no blanket rule.** Do not change the "no product push" rule in `workflow.md` or `voice.md`.
**Routed to:** Not routed to a canonical file. Logged here only, per human decision. When a personal/team-origin post shows up again, consider (don't default to) an indirect one-line bridge to what Flint does today + a soft CTA if the post is fundamentally about the team/company (not a pure personal milestone or observation) — but this is a judgment call each time, not a standing requirement.

---

## 2026-07-07 — google-ads-agent-launch

**Original (Claude draft):**
> For months, I've told our engineers we're building one thing: a machine where a founder puts a dollar into ads and gets ten back out.
>
> Today we're launching it:
>
> [product explanation, customer proof — Boompop 10x in 14 days, negative keywords for Forus, ad group fixes for 11x]
>
> Connect your Google Ads account at flint.com. 14-day free trial.

**Michelle's edit:**
> [same hook, same body] ... For Boompop, we helped their one dollar stretch as far as their ten used to. Closer to my dream of the machine.
>
> Connect your Google Ads account at flint.com. 14-day free trial.

Human's note: "make sure hooks have a proper closing (ideally they should tie back in later during the post)... originally this post just had the hook and then no sentence like [the machine payoff line]."

**What changed:** Added one sentence right before the CTA that returns to the exact "dollar in, ten out / machine" image from the hook, resolved against the named Boompop result.
**Category:** Structural/template preference (how a post closes)
**Generalizable:** yes — this is a standing principle (hook makes a specific claim/image → post must return to it before closing), not a one-off swap
**Routed to:** `flint/writing/patterns.md` — added new "Hook payoff (tie the close back to the hook)" section, placed directly before "Closing lines."

---

## 2026-09-22 — hackthenorth-judging-post

**Original (Claude draft closer):**
> Had a lot of fun judging alongside some incredible people too:

**Michelle's note:** "but this has so many filler shit that doesnt say anything like. 'Had a lot of fun judging alongside' some incredible people too: A lot of words that say nothing."

### (a) Explicit new banned words
**What changed:** Founder directly requested "honestly," "genuinely," and "probably" be added to the forbidden words list, then separately added "actually." "Genuinely" was already banned; added "honestly," "probably," and "actually."
**Category:** Single banned word or exact phrase
**Generalizable:** yes — explicit standing instruction, not post-specific
**Routed to:** `_system/forbidden/phrases.md` — added "honestly, probably, actually" to Banned Words. Note: the HackTheNorth redraft above used "actually" three times before this rule was added — needs a re-pass now that it's banned.

### (b) Empty gratitude/closer filler
**What changed:** "Had a lot of fun judging alongside some incredible people too:" flagged as saying nothing — no name, no specific moment, just a vibe statement functioning as a transition into a tag list.
**Category:** Broader AI-pattern (generic transition / filler that carries no information)
**Generalizable:** yes — same failure mode as other flagged filler (compliment-openers, hospitality phrasing already banned)
**Routed to:** `_system/forbidden/writing-patterns.md` — new bullet under "Generic AI Patterns."

### (c) Raw material upgrade: the judging question
**What changed:** Founder supplied a sharper, more specific detail mid-feedback — the question she actually asks every team ("what's difficult about your project beyond stitching a bunch of APIs together?") and the pattern in the best answers (new algorithms, serialization, architecture design). This is stronger and more specific than the original three-project list alone.
**Category:** First-party fact / raw material, not a rule
**Generalizable:** n/a — factual grounding for this post
**Routed to:** Used directly in the redraft; not added to a canonical file (too post-specific to generalize beyond "ask what's hard beneath the surface" as a general interviewing instinct, which is already implicit in her voice).

### (d) Promotion: "find a way to talk about Flint" is now a standing rule
**What changed:** Founder dropped the Flint pivot from the HackTheNorth post and, separately, said to add an instruction to actively find creative ways to mention Flint — giving two concrete techniques as examples: probe for a personal-history parallel ("how did you used to do hackathons at Yale?"), or find a Flint-culture mirror ("Flint also has a big hackathon culture"). This is the same note Michelle gave on 2026-07-03 (katie-goldstein-origin-story, entry (a) above: "try to find indirect ways to talk about flint / mention what flint does"), which was logged only at the time because it was a single occurrence and the human explicitly said no blanket rule.
**Category:** Structural/template preference (how the Writer finds a product tie-in)
**Generalizable:** yes — second occurrence across separate posts promotes this from a one-off to a rule, per the promotion criterion in this file's header.
**Routed to:** `CLAUDE.md` — new "Finding the Flint angle" subsection under the Writer sub-agent, with the two techniques (personal-history parallel, Flint-culture mirror). Also cross-referenced in `flint/writing/workflow.md` Edge cases. Does not override the Friday/Sunday "no product push" default — applies only when a Flint tie-in is actually required (Monday, or on request) and isn't obvious.
