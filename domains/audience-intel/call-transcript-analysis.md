---
practitioner: Gong + Rework (AI Sales Ops library) + Adam Corey (Product Marketing Alliance)
role: conversation-intelligence vendors and transcript-mining method guides
type: practitioner|vendor
confidence: T1 (method consensus) / T2 (vendor benchmarks)
domains: [call-transcript-analysis]
verified: 2026-08-15
sources_checked: 5
---
# Call Transcript Analysis — Panel

## Beliefs
- "In B2B sales, the truth about deals, pipeline, and customer needs lives in conversations — not in CRM fields" (Gong).
- Transcripts are raw, real, unfiltered; "where prospects tell you explicitly what they care about, what they're confused by, what's missing" (Corey).
- Most tools are built for sales, not marketers: "before you grab transcripts and throw them into ChatGPT, there are considerations" (Corey).

## Frameworks
- **The 5 Ms** (Rework): Macro Patterns (team aggregates: talk ratio, question frequency, win rate by discovery method) / Micro Moments (specific coaching instances) / Mentions (competitor/feature/timeline/budget references) / Misses (questions not asked, commitments not logged) / Momentum (buyer sentiment arc). Macro → coaching programs; Micro → individual coaching; Mentions/Misses/Momentum → deal management.
- **Two-pass mining** (Corey): pass 1 enumerate all objections/themes; pass 2 pull specific quotes for the ones you care about.
- **Objection analysis at scale** (Gong): analyzed 67,149 calls to find how best salespeople handle objections (T2, vendor corpus).

## Processes
1. Filter transcripts first (team, CRM filters, call type, mentions) — "make the haystack smaller" (Corey).
2. Analyze for structured signals: objections, competitor mentions, next-step commitments, pricing-discussion timing, question frequency, sentiment arc (Rework signal table).
3. Aggregate across calls — the underused win: "which competitor was mentioned in deals lost in the last 90 days" was previously a quarterly survey + rep memory; build aggregate queries in the FIRST 90 days of deployment (Rework).
4. Feed a recurring loop: insights → messaging/content updates → monitor next wave of calls for adoption and response (Corey: "not a one-and-done project").
5. Compliance first: consent flows before recording; retention policies; "recording without consent creates legal exposure that negates the operational value" (Rework).

## Decision rules
- IF deal stalled >30 days THEN query transcripts for the objections raised in that cohort (stall-objection signal).
- IF a competitor is named in late-stage losses THEN surface to competitive intel within the week (Rework).
- IF buyer sentiment drops in the second half of a call THEN flag deal risk (Rework).
- IF pricing is discussed before discovery is complete THEN flag methodology violation (too early = bad).
- IF an insight has no verbatim quote + speaker attribution THEN treat it as unverified; ask the model to cite (Corey).
- IF mining for objections THEN two passes: enumerate first, quote second — never one pass.

## Failure modes
- Dumping transcripts into an LLM without filtering or verification (Corey).
- One-and-done projects; insights never revisited; no feedback loop.
- Never building the aggregate intelligence workflow (competitive/objection queries) — the most underutilized output (Rework).
- Ignoring privacy/compliance (Rework).
- Rep-filtered CRM notes as the only record — knowledge walks out the door with the rep (Rework).

## Tools
Gong (enterprise analytics leader), Chorus/ZoomInfo (mid-market), Fireflies (budget); models: GPT-4o/Claude for nuance + long context, Gemini/Mistral for volume (Corey).

## Sources
1. Rework — Sales Call Recording and Transcript Analysis (Meeting Intelligence pattern) | https://resources.rework.com/libraries/ai-for-sales-operations/sales-call-recording-and-transcript-analysis | tier 2 | 2026-08-15
2. Product Marketing Alliance (Adam Corey) — 5 tips for marketers mining sales calls | https://www.productmarketingalliance.com/5-tips-for-marketers-mining-sales-calls-for-insights | tier 2 | 2026-08-15
3. Gong — Conversation Intelligence | https://www.gong.io/conversation-intelligence | tier 2 (vendor) | 2026-08-15
4. Gong — Objection Handling (67,149-call analysis) | https://www.gong.io/resources/guides/objection-handling-for-sales | tier 2 (vendor) | 2026-08-15
