# CUSTOMER & AUDIENCE INTELLIGENCE — Discipline Synthesis (Wave A4)

Covers: survey-design, reddit-research, review-mining, social-listening, support-ticket-mining, call-transcript-analysis, customer-research, win-loss-analysis, account-intelligence, intent-signals, technology-analysis, competitor-battlecards, ad-library-research.
Reuses: syntheses/research.md (interview rules, saturation, NPS, win/loss) and syntheses/positioning.md (battlecards, competitive alternatives).
Verified: 2026-08-15. Evidence base: 10 multi-query web searches (parallel_search), ~50 fetched sources; vendor marketing pages tagged T3.

## Consensus (independent agreement, 2+ sources per rule)

1. **Existing-voice data (tickets, reviews, transcripts, social, Reddit) is discovery-grade, not proof.** Every data-mining method finds patterns in *current customers / vocal users* — it misses silent majority, churned, and non-buyers. Kromatic (tickets: survivor + squeaky-wheel bias), Noisely (reviews: written for other buyers), Reddinbox (Reddit: confirmation-bias trap), Rework (transcripts: rep-filtered CRM notes hide truth). Corollary: pair with interviews for depth, surveys for quantification. (PRINCIPLE, T1)
2. **Taxonomy is the unit of analysis: build it from a hand-read sample, keep it shallow, freeze it.** Kromatic: hand-read 50–100 tickets, 8–15 top-level categories, one revision then freeze. Noisely/Miro: 15–25 themes in 3 layers (product area / experience quality / outcome). Pelin: tag from day one, train agents with a tagging guide. (FRAMEWORK, T1)
3. **Weight by customer/account value, never by raw count.** Koji: theme in 5 tickets from $100K accounts > 50 tickets from $50/mo accounts; weight by unique-customer count not ticket count (Kromatic); HG Insights: intent without fit = noise. (DECISION RULE, T1)
4. **Frequency threshold before acting: ~3+ mentions (interviews), 5–10% of sample (tickets), repeated themes across segments (reviews).** One loud customer is not a theme (Koji, Pelin, Clozd's "don't act on 1–2 data points"). (DECISION RULE, T2)
5. **Recency matters everywhere.** Intent decays: 0–7 days hot, 8–30 moderate (Prospeo). Reviews: recent themes outweigh stale (BigSentiment). Ticket mining: sample evenly across the window (Kromatic). ABM lists go stale within a quarter (HG Insights). Refresh cadence: top accounts weekly, pipeline monthly, full database quarterly (Derrick). (DECISION RULE, T2)
6. **Structure the output as decision artifacts, not reports.** Monthly G2 report answering 5 fixed questions (Noisely); weekly support sync with top-5 agenda (Pelin); battlecards updated from win/loss (existing); aggregate transcript queries built in first 90 days (Rework). Reports nobody acts on are the graveyard of research (win/loss existing). (TACTIC, T1)
7. **Free tier first, upgrade on bottleneck.** Meta Ad Library → paid spy tools (PrimeSpy); Reddit native search + F5Bot → paid (Reddinbox); Mention/Brand24 before Brandwatch (Sprinklr). (TACTIC, T2)
8. **All AI analysis must be traceable to source quotes** — every insight linked to a real review/ticket/transcript; verify LLM claims against data (PMA, ParseMyApp, Kromatic "reconcile AI taxonomy with your own read"). (PRINCIPLE, T1)

## Disagreement

1. **AI vs manual coding of unstructured data.** Vendor camp (Pelin, Koji, Enterpret): AI taxonomy at scale beats manual. Kromatic: AI drafts taxonomy but human must hand-read 50–100 in parallel — "relying on the model alone bakes in its training biases." Condition: AI for clustering/sentiment at scale, human read for taxonomy design and final theme confirmation.
2. **Intent data value.** Vendors (Bombora, 6sense, Intentsify): intent is the earliest in-market signal, worth big budget ($50–100K/yr for 6sense). Practitioners (Demandbase's own framing): intent is "evidence to investigate, not proof of purchase"; Amplemarket's comparison rates ZoomInfo intent 12/30. Condition: intent works only layered on fit (HG Insights: "intent with fit produces a ranked list worth working"); treat all vendor benchmarks as T3.
3. **How many interviews/themes count as signal.** Interview school: 3+ mentions = theme (existing research.md). Ticket school: 5–10% of sample (Koji). Review school: themes across multiple segments (Noisely). Condition: the more heterogeneous the population, the higher the threshold.
4. **G2 vs App Store vs Trustpilot weighting.** G2 reviewers write for other buyers and skew positive (verified-business bias); Trustpilot skews negative ("where people go when something goes wrong" — CheckThat). Condition: treat each channel as its own biased sample; never blend scores across channels without caveat (BigSentiment source-bias rule).
5. **Reddit: engagement vs research.** Marketing camp: engagement for brand (HubSpot mistakes list). Research camp: lurk-only, comments-before-posts, never promote (Reddinbox). Condition: research mode = no engagement; if you engage, follow subreddit rules and provide value first.

## Conditions — when each method is correct

- **Survey**: hypotheses exist, population defined, decision + required precision stated first (Krosnick); useless pre-PMF without baseline analytics (Price, existing).
- **Reddit**: category where buyers discuss openly; 10k–500k member subreddits with posts <7 days old and 10+ comments (Reddinbox); fails for enterprise buyers who don't post.
- **Review mining**: public review volume exists (G2, stores); best for product roadmap + competitive positioning; cohort-split by segment required (Noisely).
- **Social listening**: brand/competitor conversation volume exists; monitoring (what) ≠ listening (why) — pick tool tier by team size (Sprinklr/Emplifi).
- **Ticket mining**: ≥500 tickets over 3–6 months (Kromatic); fails for early-stage products with tiny support volume.
- **Call transcripts**: sales team records calls; B2B; compliance/consent solved first (Rework); needs ≥90 days of transcripts for aggregate queries.
- **Account intelligence**: B2B ABM with defined ICP; data freshness is the binding constraint (HG Insights).
- **Intent signals**: accounts researching category publicly; pair with fit scoring; decay window 0–30 days.
- **Technology analysis**: prospect/competitor websites fingerprintable; job postings as fresh signal; client-side only limitation.
- **Ad library**: paid social category; Meta Ad Library free tier for active ads only (no historical performance); paid tools for archives (PrimeSpy et al.).

## Failure knowledge (what repeatedly doesn't work)

1. Confirmation-bias research: searching for threads/reviews/tickets that confirm the belief and screenshotting (Reddinbox: "self-deception with extra steps"; Clozd: rep-run win/loss).
2. Acting on one loud customer/one-off request (Koji, Pelin, Clozd).
3. Trusting existing tags/agent categorization instead of re-classifying (Kromatic agent-interpretation bias; Pelin's "no tagging system").
4. Vanity dashboards: mention volume/sentiment without decision connection; tools bought before objectives defined (Emplifi: "brands jump in with a tool before they've identified what they'll do with the insights").
5. NPS collected without closing the loop — reduces trust and future participation (CustomerGauge, Meegle); NPS as bare score (existing research.md).
6. Reddit: promotion/ghosting/ignoring subreddit rules — destroyed credibility (HubSpot).
7. Ad research as creative shopping: copying competitors instead of understanding customer motivation (PrimeSpy); spy tools can't prove profitability.
8. Transcript mining as one-and-done: insights don't compound, no feedback loop (PMA); aggregate intelligence never built (Rework).
9. Stale ABM lists: "a target list built in January is misleading by June" (HG Insights).
10. LLM analysis without verification: unverified claims/hallucinated quotes (PMA; ParseMyApp traceability).

## Collision Method sketch — Audience Intelligence Engine

- **Objective**: turn existing customer-voice data (tickets, reviews, transcripts, social, Reddit) + account-level data (firmographic/technographic/intent) into decision-grade audience intelligence, without fabricating segments.
- **Prerequisites**: one data source with enough volume (≥500 tickets, ≥90 days transcripts, active ads, etc.); export access; a defined decision; taxonomy capacity.
- **Inputs**: tickets/chat exports with metadata (date, segment, product area, ARR); review exports (G2/stores); transcript corpus; ad library search; CRM/enrichment data; intent feed if budget allows.
- **Diagnosis**: (1) Which channel holds the most signal for the question? Discovery questions → Reddit/reviews/social; product-friction questions → tickets; win/message questions → transcripts + win/loss; targeting questions → account/technographic/intent. (2) Is volume sufficient for the threshold? If not, interview instead.
- **Decision tree**:
  1. Question = what do customers struggle with? → ticket mining (hand-read 50–100 → 8–15 category taxonomy → classify ≥500 → frequency×severity×ARR matrix → top-5 hypotheses).
  2. Question = how are we/competitors perceived? → review mining (cohort-split by segment, Feature-Pain-Outcome triples, recency-weighted) + social listening.
  3. Question = what do buyers say when deciding? → transcript mining (two-pass: enumerate objections → pull quotes; 5-Ms framework) + win/loss (existing Clozd rules).
  4. Question = who to target? → account intelligence: firmographic fit → technographic displacement/gap plays → intent recency layer (0–7/8–30 days) → FIRE-style scoring.
  5. Question = what creative works? → ad library: direct → regional → reverse-creative → category search; read themes (price vs margin defense); treat as customer research, not creative shopping.
- **Execution**: weekly scans (top-5 tags, anomalies), monthly thematic reports (5 fixed questions), quarterly deep synthesis into personas/battlecards/roadmap; AI-assisted classification with human taxonomy ownership and quote traceability.
- **Metrics**: % insights with source quotes; themes with ≥5–10% frequency; action items closed per cycle; freshness of account data (install-change alerts); reply/win-rate deltas from technographic personalization.
- **Stopping rules**: stop when themes repeat at threshold across segments (no new categories in a fresh 100-item sample); freeze taxonomy after one revision; stop ticket mining if <500 tickets (go interview); kill intent spend if fit-scoring absent; stop ad research when it produces no testable hypothesis.
- **Failure modes (guards)**: confirmation-bias sampling; single-loud-customer actions; trusting existing tags; report-only outputs; stale data; untraceable AI claims; copying creative.
- **Conditions**: B2B SaaS/consumer both work; volume-gated; the binding constraint is honest, recent, traceable data.
- **Limitations**: all channels are biased samples of current/vocal users; no channel yields market size; intent and technographic benchmarks are vendor-sourced (T3).
- **Confidence**: T1 for consensus rules (2+ independent sources), T2 for thresholds (single-source or vendor-adjacent), T3 for vendor benchmarks (intent lift, technographic ROI claims: "27% shorter sales cycle, 34% better conversion" — HubSpot-via-Derrick, unverified).

## Key sources
kromatic.com/real-startup-book (ticket mining method); noise.ly/blog/g2-reviews-analysis-product-insights; reddinbox.com/blog/how-to-use-reddit-for-market-research; blog.hubspot.com/marketing/reddit-marketing-mistakes; resources.rework.com (meeting intelligence, 5 Ms); productmarketingalliance.com/5-tips-for-marketers-mining-sales-calls-for-insights; koji.so/docs/support-ticket-research-analysis; pelin.ai/blog/zendesk-product-insights; hginsights.com/blog (ABM data shelf life); businessbrainz.com FIRE methodology; prospeo.io/s/b2b-intent-data; demandbase.com/blog/buyer-intent (evidence not proof); derrick-app.com technographic guide; stackwho.com website technology profiling; adsuploader.com/blog/meta-ads-library; primespy.net (ad spy tool guide); emplifi.io social listening guide; sprinklr.com/blog/social-listening-tools; customergauge.com (NPS closed loop); web.stanford.edu Krosnick handbook.
