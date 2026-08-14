# COMPLETE METHODOLOGY LIBRARY — Collision Methods

Assembled 2026-08-15 from the Collision Method sketches in every synthesis. These are the synthesized operating procedures of the Marketing OS.

## aeo
## Collision Method sketch — AI Search Visibility (AEO/GEO) for the Marketing OS
- **Objective**: maximize brand citation share (presence + portability) in AI answers for the prompt library that maps to the buyer journey; accept citations ≠ clicks, pair with brand-query lift measurement.
- **Prerequisites**: (1) prompt library from sales/support transcripts + review/community language (not keyword tools); (2) per-engine baseline: 50-200 prompts × {ChatGPT, Perplexity, Google AIO} at topic level; (3) ranking baseline for the same queries in classic search (the retrieval-pool prerequisite); (4) list of current third-party citers (PR, Wikipedia, Reddit, analyst reports).
- **Diagnosis**: compute Presence (share of prompts where domain appears per engine), Portability (share of cited URLs appearing in 2+ engines), Concentration (share from one engine). Gap-analysis: for cited competitor/other answers, diff content elements (quotes, statistics, named entities, answer blocks, third-party sources).
- **Decision tree**:
  - Not ranking for seed queries → fix SEO/crawlability first (search channel = 88% of ChatGPT citations). No GEO spend.
  - Ranking but absent from answers → add third-party footprint (PR, Reddit/Wikipedia presence, unlinked mentions) + quotes/stats/external citations in content (Stanford levers).
  - Present but not cited / misrepresented → answer-first restructure (question-H2 → immediate answer), entity clarity (consistent naming, entity home pages), schema as content-planning lens.
  - Cited but concentrated in one engine → portability work: entity disambiguation, Wikipedia/analyst coverage, reduce diffuse brand facets.
  - Cited but no business impact → stop optimizing citations; measure brand-search lift and consider the answer itself as the conversion surface (value-based clicks, Walsh).
- **Execution**: per-engine content scoring quarterly; 4-6 week cycles; third-party citation acquisition in parallel with content.
- **Metrics**: presence %, portability %, concentration %, SOV per prompt topic, citation decay half-life, position-1 CTR delta vs AIO-free peers, brand-query GSC lift.
- **Stopping rules**: stop schema-only initiatives (null result); stop single-engine optimization when concentration >~80% without portability plan; stop if no presence movement after 2 content cycles (~26 weeks) → revisit ranking baseline; stop prompt-level optimization on sample noise — aggregate to topic.
- **Failure modes**: blended scores; single-answer sampling; gaming attempts (detectable, unstable); JS rendering; ignoring third-party footprint; vendor case-study optimism (single-arm).
- **Conditions**: strongest for informational/comparative B2B content; weakest for local/transactional (training-data + reviews dominate) and for brands without ranking baseline.
- **Limitations**: field is <2 years old; citation mechanics change with engine updates; no RCT-level evidence for full programs; most quantitative claims are observational.
- **Confidence**: mechanisms (quotes/stats/citations, retrieval-pool prerequisite, per-engine fragmentation, CTR decline) = high (multiple independent sources); schema effects = null-to-low; vendor GEO ROI claims = low.
- **Key sources**: arXiv 2311.09735 (GEO, KDD 2024); arXiv 2605.29107 (GEO-Bench); growth-memo.com/p/the-consensus-gap (Indig); ahrefs.com/blog/why-chatgpt-cites-pages; ahrefs.com/blog/schema-ai-citations; ahrefs.com/blog/ai-overviews-reduce-clicks; ahrefs.com/blog/most-cited-domains-perplexity; orbitmedia.com/blog/what-seos-get-wrong-about-ai-search; aleydasolis.com/en/ai-search/ai-search-optimization-checklist; searchenginejournal.com (Walsh ×2, van Berkel).

## amazon
## Collision Method sketch — "Amazon Channel Plan" (what the Marketing OS should encode)
- **Objective**: decide whether/how to enter or scale on Amazon (and which additional marketplaces), set the ad architecture, and govern it with the right metrics.
- **Prerequisites**: listing conversion at category parity (reviews, price, images, Buy Box), per-ASIN margin model incl. FBA + referral + ad allocation, capital runway for 8–12 weeks of break-even ACoS, compliance audit of packaging/communications (McCabe/SellerSprite).
- **Inputs**: margin per ASIN, category ACoS benchmark, competitor review depth, search-term report (post-launch), TACoS trend, branded search volume, remarketing pool size.
- **Decision rules** (the 5-8 the OS should encode):
  1. IF listing doesn't convert organically at parity THEN fix listing before scaling ads (Zagare; universal, HEURISTIC, T1).
  2. IF <$1.5k/month ad budget THEN SP-only, 80%+ of budget, single-keyword campaigns for top 5 high-volume terms (Zagare; Keywords.am, HEURISTIC, T2).
  3. IF stage=launch THEN ACoS target ≥ break-even, TACoS expected 20%+ declining after 8–12 weeks; do NOT cut on ACoS alone (pcostudio, HEURISTIC, T2).
  4. IF stage=growth & 100+ reviews & branded search volume THEN move to ~60/25/15 split and enable SD retargeting (Keywords.am, HEURISTIC, T2).
  5. IF competitors bid your brand terms THEN SB brand defense > efficiency (Keywords.am, HEURISTIC, T2).
  6. IF using up-and-down bidding THEN only on proven exact terms with 30+ days data; else down-only; always compute placement × dynamic compounding before setting modifiers (AMALYZE/SalesDuo, EMPIRICAL, T2).
  7. IF branded campaign ROAS looks great THEN distrust it; check NTB and organic rank movement before scaling (SellerStack, EMPIRICAL, T1).
  8. IF sponsored spend < ~$50k/month or profitability inconsistent THEN no DSP; revisit at scale with AMC measurement (Darkroom, HEURISTIC, T2).
  9. IF review velocity spikes THEN prepare proportionality documentation (sales data + campaign records) proactively (SellerSprite, EMPIRICAL, T2).
  10. IF TACoS flat/rising while ACoS stable THEN organic rank isn't following — listing conversion is the problem, not bids (pcostudio; existing skill, HEURISTIC, T2).
- **Metrics**: ACoS (per campaign), TACoS (business), NTB%, organic share of sales, break-even ACoS per ASIN, TACoS trend 8–12 weeks post-launch. Guardrail: ACoS > break-even for 12+ consecutive weeks on a non-launch ASIN = cut.
- **Stopping rules**: negative landed margin per SKU (marketplace math) = kill SKU; ACoS-only culture = metric governance failure; suspension risk (review velocity, insert complaints) = stop and document before scaling.
- **Confidence**: T1 for mechanics and enforcement cases; T2 for split/bid tables; T3 for category benchmarks and the $50k DSP threshold.
- **Key sources**: Keywords.am budget split 2026; AMALYZE placement modifiers + bid strategies; SalesDuo bidding guide; pcostudio ACoS/TACoS; SellerStack incrementality/halo; Darkroom DSP; SellerSprite review enforcement; Marketplace Pulse 2025 year in review; Zagare (PPC Entourage blog, ZonGuru interviews); Zahradnik (QA Selling Online podcasts, AMZ Pathfinder); McCabe (ecommerceChris, AMPM podcast #379); Perpetua Instacart guide.

## analytics
## Collision Method sketch — Analytics & Dashboards
- **Objective**: turn raw analytics into a decision-support system: KPI hierarchy → dashboard with targets → proxy metrics for the NSM → outlier alerting.
- **Prerequisites**: measurement plan (events + dimensions), analytics access, exec team able to set targets.
- **Diagnosis**: (1) audit existing dashboard metrics — count those with targets; (2) apply Cutler's vanity test to each; (3) identify the business's high-level engagement metric (Biddle) or NSM; (4) define 1-3 proxy metrics with threshold definitions.
- **Decision rules**:
  1. IF a dashboard metric has no target AND no decision attached THEN remove it (Kaushik, T1).
  2. IF a metric lacks context/intent/actionability THEN mark vanity and replace (Cutler, T1).
  3. IF NSM is defined THEN define proxy metrics as "% of [segment] who do ≥[threshold] by [time]" (Biddle, T1).
  4. IF reporting averages THEN add distribution/cohort view alongside (Biddle, T1).
  5. IF KPI deviates >3σ from its own mean THEN escalate to exec with hypothesis (Kaushik, T1).
  6. IF a metric moves but no tactic changes THEN drop it from the dashboard (Cutler, T1).
  7. IF GA4 property is new THEN set retention ≥14mo, register custom dims, choose attribution model explicitly (Seiden, T1).
  8. IF the team can't influence the NSM directly THEN add input metrics, keep NSM as compass (Cutler/Biddle, T1).
- **Metrics**: % of dashboards with targets, vanity-metric count, proxy-metric correlation to NSM (causal where possible), outlier alerts per period, dashboard usage (who opens, what they act on).
- **Stopping rules**: stop adding metrics when every existing one has a target and an owner; stop a proxy metric if it shows no correlation to the NSM after 2 quarters.
- **Failure modes**: data puking, target-less dashboards, gamed targets (sandbagging — Kaushik warns), average-masking, NSM paralysis.
- **Confidence**: T1 for Kaushik/Cutler/Biddle/Seiden (primary sources fetched); T2 for Mercer/Kiss (secondary).

## audience-intel
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

## competitive
## Collision Method sketch — Competitive Intelligence
- **Objective**: produce decision-grade CI: alternatives map → head-to-head win-rate metric → sales plays + positioning inputs.
- **Prerequisites**: deal-loss data (or access to win/loss interviews), sales team feedback channel, competitor set from actual deals (not internet research).
- **Diagnosis**: (1) list competitive alternatives from lost deals + win/loss interviews (status quo included); (2) tag phantom competitors (appear in <X deals, never lost to); (3) document scoring basis for any comparison; (4) identify competitor sales plays + company strategy.
- **Decision rules**:
  1. IF a competitor appears in deals but you never lose to them THEN stop positioning against them; monitor only (Dunford, T1).
  2. IF >25% of deals end in no-decision THEN treat status quo as the primary competitor in positioning (Dunford, EMPIRICAL T1).
  3. IF a comparison chart lacks documented scoring THEN fix scoring or remove chart (Kellogg, T1).
  4. IF CI output has no sales play attached THEN it's research for knowledge's sake — convert to play or cut (Kellogg, T1).
  5. IF win/loss data is unavailable THEN run 5-10 lost-deal interviews before building CI (Kellogg/org, T2).
  6. IF a competitor changes pricing/positioning THEN re-run the alternatives map, don't just update the feature matrix (org methodology, T2).
- **Metrics**: head-to-head win rate vs each chosen competitor, % of CI artifacts converted into plays, deal-loss reason coverage.
- **Stopping rules**: stop expanding the competitor list when >2-3 competitors are never encountered in deals.
- **Failure modes**: feature-matrix theater, phantom positioning, no-decision blindness, report-padding.
- **Confidence**: T1 (Kellogg, Dunford primary sources fetched); T2 (vendor methodology via public content).

## creative-longtail
## Collision Method sketch — "Creative Engine" (ad creative + hooks + UGC)
- **Objective**: produce a tested, replenishing creative system: angle matrix → hook-led concepts → platform-native assets (studio/UGC) → testing cadence → winner iteration/fatigue management.
- **Prerequisites**: angle evidence (VOC, competitor saturation map), budget floor ($5k/mo for meaningful testing), measurement (pixel + creative-level CTR/CPA/hook rate), awareness segmentation per audience (Schwartz).
- **Inputs**: pains/desires × proof-point matrix; competitor ad-library scan; winning control creative + its metrics; platform format specs; UGC roster + brief template; rights docs.
- **Decision rules**:
  1. IF no angle matrix THEN build pains×proofs + competitor saturation before producing any asset (hawky, FRAMEWORK, T2).
  2. IF budget $5k–30k/mo THEN test 1–3 distinct creatives/week, cap ~10 live (Denney, EMPIRICAL, T2); IF ≥$10k/mo AND production capacity THEN 2–4 distinct concepts/week (hawky, HEURISTIC, T3).
  3. IF writing hooks THEN open with buyer's pain in ≤4 words, generate 50 hook options, ship top 3 per angle (Hormozi, HEURISTIC, T2); for video, layer visual+audio+text and mirror the spoken hook in captions (social.md + vexub, EMPIRICAL/HEURISTIC, T2/T3).
  4. IF testing THEN one variable per test, equal conditions, ≥1–2x target CPA or 3–7 days before judgment, decision criteria pre-defined (hawky/AdGenz, HEURISTIC, T3).
  5. IF a creative wins THEN iterate it 10 ways / reskin before new concepts (Denney, HEURISTIC, T2; Hormozi 80% reskin, T2); splice winning first-3s onto new bodies at scale (Hormozi, TACTIC, T3).
  6. IF UGC THEN brief angle + emotional beats + 3–5 example phrases (not scripts), 1–2 pages, rights + revision limits in the brief (ATTN/Moburst/InfluenceFlow, HEURISTIC, T2/T3).
  7. IF judging UGC vs studio THEN matched test; expect UGC to win prospecting, studio retargeting — verify per account (hawky; skill consensus, HEURISTIC, T2).
  8. IF CTR/CPA decays as frequency rises THEN refresh hooks/rotate (7–10 day cadence) before touching targeting or budget (Denney; AdManage; AppsFlyer, EMPIRICAL/HEURISTIC, T2).
- **Metrics**: hook rate/thumb-stop (30–50% good on Meta, T3), 3s hold %, CTR, CPA, creative-level ROAS, fatigue curve (frequency × performance), supply rate vs budget, UGC brief-to-approved-asset turnaround.
- **Stopping rules**: kill creative below breakeven after valid spend; stop testing a variable when two consecutive batches show no delta (Pixis matrix logic); stop UGC wave if brief compliance drops (QA failure) — fix brief before more volume.
- **Failure modes**: variation-not-concept testing, feature-first hooks, vague/over-restrictive UGC briefs, scripted UGC, premature judgment, fatigue blindness, no taxonomy, no rights.
- **Conditions**: performance-led paid social (Meta/TikTok); scales down to $5k/mo, requires production infra above ~$30k/mo.
- **Limitations**: most volume/cadence numbers are operator heuristic (T2/T3); vendor AI-UGC benchmarks unverified; platform algorithms shift (Denney's Meta hooks 2024–25 era); Schwartz mapping here is exegesis (T2).
- **Confidence**: T1 none (no RCTs); T2 for Denney/Shackelford/Hormozi doctrine + brief-quality consensus (5 independent sources agree); T3 for numeric benchmarks (thumb-stop, +340%, 73%, 20%+ lift).
- **Key sources**: see domains/creative-longtail/*.md and messaging-longtail/dara-denney.md + short-form-hook-retention.md.

## cro
## Collision Method sketch (what the Marketing OS should encode)
**Objective**: increase revenue per visitor (RPU/ARPU — DRIP's primary metric) through evidence-ranked, correctly-statted experiments; decide test vs redesign vs ship.
**Prerequisites**: clean tracking (A/A-validated), ability to define primary metric + guardrails, minimum traffic per testable page, stakeholder pre-commitment to decision rules.
**Inputs**: baseline conversion + variance per funnel step, traffic forecast, business cost/benefit inputs (for threshold math), customer research (pains/language/emotions), instrumentation health (SRM).
**Diagnosis** (order): 1) instrumentation check (A/A, SRM) 2) funnel analytics (leak location) 3) qualitative (recordings, surveys, user tests — triangulate ≥2 sources) 4) message/value-prop audit (Aagaard/Saxo lens + Wolf's emotional gap analysis).
**Decision tree**:
- Tracking broken → fix, do not test.
- Page <1K visits/week → no small-effect tests: rapid-test concepts (MacDonald) or evidence-based reversible changes with honest before/after.
- Message mismatch or value prop unclear → fix messaging (copy research, Aagaard/Wolf methods), test the fix as a big swing.
- Friction at a step with traffic → ResearchXL-style research → hypothesis (Sullivan format) → PXL/Evidence-Impact-Effort-Traffic-ROI score → run.
- Testable → pre-register: OEC, MEI (business), sample size (n=(4σ/Δ)² at 95/90, or sequential design), duration ≥ full business cycle, stopping rule.
**Execution**: single primary metric + guardrails; A/A validation; SRM on every test; run to end (or planned sequential boundaries, e.g., AGILE alpha/beta spending).
**Stopping rules**: significance at pre-planned analysis; futility boundary → declare null; harm/guardrail breach → abort (peeking allowed for abort, never for win); inconclusive is a valid outcome.
**Metrics**: RPU primary; win rate 20-40% band as hypothesis-quality diagnostic (below → cosmetic/researchless; above → too safe); decisions-supported per quarter; implementation rate.
**Failure modes to monitor**: peeking wins, SRM, cosmetic tests, metric ≠ revenue, stakeholder override, output-KPI programs, unshipped wins.
**Conditions**: this is the mid/high-traffic method; low-traffic segments use the qualitative path; org structure determines whether a CoE/gate process is needed (Labay/Vermeer).
**Confidence**: T1 for stats rules (Kohavi, Georgiev, Goodson-Microsoft), T1/T2 for process frameworks (Laja, Sullivan, Labay), T2 for copy/message heuristics (Aagaard replications), T3 for agency ROI claims.
**Key sources**: Kohavi pitfalls papers; Georgiev's book; Goodson/VWO SmartStats + Microsoft optional-stopping paper; Laja ResearchXL/PXL; Sullivan hypothesis + failure decks; Aagaard case studies; growthlayer MDE rule; adasight/Atticus Li program failures; Labay/Vermeer org taxonomy.

## dtc
## Collision Method sketch — DTC / Shopify Marketing Audit
- **Objective**: audit a Shopify store's marketing health: unit economics → MER/ROAS → retention → paid allocation → fixes.
- **Prerequisites**: P&L (COGS, overhead, ad spend), store analytics (AOV, conversion rate), cohort/repeat data, ad account structure.
- **Diagnosis**: (1) compute contribution margin after COGS+overhead; (2) compute MER (blended, trailing 30/90 days) and per-channel ROAS; (3) compute repeat purchase rate + CAC payback; (4) check organic content→paid amplification pipeline; (5) benchmark vs Youderian medians.
- **Decision rules**:
  1. IF gross margin < ~50% THEN fix COGS/pricing before scaling ad spend (Youderian, EMPIRICAL T1).
  2. IF MER < 2.0 (blended, breakeven-dependent) THEN cut spend until unit economics improve; MER below target = allocate down (Firestone/Youderian, HEURISTIC T2 — target varies by margin).
  3. IF first 1,000 customers weren't earned organically THEN re-anchor messaging via organic content before scaling paid (Sharma, T1).
  4. IF repeat purchase rate < ~20-25% THEN invest in email/retention before acquisition (Firestone, HEURISTIC T3).
  5. IF CPM is low but CTR is low THEN creative/message problem, not audience problem (Sharma, T1).
  6. IF a channel's ROAS is high but MER is flat THEN spend is shifting, not growing — check attribution and incrementality (MER logic, T2).
  7. IF paid revenue hasn't hit $5k/day milestone THEN keep paid experimental, not scaled (Sharma, HEURISTIC T1).
  8. IF contribution margin per order <0 THEN pause paid entirely (Youderian, FACT T1).
- **Metrics**: MER (30/90d), per-channel ROAS, AOV, gross margin %, contribution margin, repeat rate, CAC payback, email revenue %.
- **Stopping rules**: stop scaling any channel whose marginal MER contribution < blended MER; pause paid if contribution margin < 0 for 2 consecutive months.
- **Failure modes**: ROAS-only thinking, breakeven-forever, margin blindness, Amazon-first erosion, creative fatigue misdiagnosis.
- **Confidence**: T1 for Sharma/Youderian/Kellogg-adjacent primary sources; T2 for Firestone (course material, promotional); T3 for specific numeric targets (context-dependent).

## email
## Collision Method sketch — Email & Lifecycle Discipline
- **Objective:** maximize subscriber lifetime value and inbox presence through stage-appropriate, permission-respecting, engagement-optimized email.
- **Prerequisites:** permissioned list with source capture; ESP with behavior tracking + segmentation; authentication (SPF+DKIM+DMARC) and PTR/TLS; Postmaster Tools / complaint monitoring; one-click unsubscribe (if bulk).
- **Inputs:** subscriber lifecycle stage definitions, activation milestones, customer-interview language (JTBD — Geisler), engagement history, audience provider mix, email-type taxonomy (newsletter/offer/transactional — Schwedelson).
- **Diagnosis (in order):** (1) Is permission + onboarding sound? No → fix acquisition/promises (White: permission moment determines months). (2) Are segments engagement-qualified? No → winback/re-permission/prune. (3) Is deliverability clean (spam rate, bounces, auth)? No → infrastructure before creative. (4) Where does conversion break: open → click → landing? (Pay's 3-step: fix after-click first). (5) Is copy customer-language (features→benefits)? No → rewrite from interviews.
- **Decision tree — sequence design:** onboarding (Geisler): time-based skeleton paced by trial length → behavior branches (moving-along / stuck / ahead) → vary CTA by state; engagement: escalate content only when prior step completed; declining engagement → winback (different frame: benefit, not features) → re-permission → prune. Newsletter (Oshinsky): audience + job defined → launch fast → iterate on reader response → one new revenue stream/year; choose hyperscale vs hyperniche.
- **Send mechanics (Schwedelson):** bucket email types; newsletters Mon–Wed 5–8am / Thu–Sun 8–11am; offers 10am–2pm or tested off-hours; never on the hour; time-commitment framing in subject/preheader; use per-recipient send-time optimization when available.
- **Metrics:** engagement (clicks primary post-MPP), open rate (directional), deliverability rate + spam rate (<0.3%), complaints, bounce, unsubscribe per step, conversion per journey stage, trial→paid, retention/churn, list growth vs prune balance.
- **Stopping rules:** stop emailing a segment when winback + re-permission fails (prune); pause sends if spam rate or complaints spike; kill a sequence step that underperforms its branch alternatives; never email without unsubscribe.
- **Failure modes:** bought lists, permissionless sends, stale-segment mailing, time-only sequences, email-silo optimization, hack infrastructure, ignored feedback signals.
- **Conditions:** applies to any program with a list > a few hundred and an ESP; depth of lifecycle machinery scales with list size and data infrastructure.
- **Limitations:** MPP/AI-summary-era signal erosion; provider policies shift (2021–2026 wave); vendor data self-reported; personalization of placement makes absolute benchmarks unreliable.
- **Confidence:** T1 for lifecycle-over-campaigns, recipient-first reputation, auth baseline, behavior branching (convergent across 4–7 practitioners + regulatory facts); T2 for Schwedelson's specific % lifts; T3 for Atkins' cold-infrastructure prediction.
- **Key sources:** emailmarketingrules.com (White ×4); Intercom podcast w/ Geisler; jayschwedelson.com EP63 + MarketingProfs 2024; holisticeemailmarketing.com; inboxcollective.com 25 rules; spamresource.com (Iverson ×2); stripo.email Atkins interview + wordtothewise.com; support.google.com/mail/answer/81126.

## feeds
## Collision Method sketch — "Feed Health & Optimization" (what the Marketing OS should encode)
- **Objective**: keep the product feed healthy (eligible, compliant) and optimized for Shopping/PMax performance, with prioritized remediation.
- **Prerequisites**: one source of truth (store/platform export), scheduled fetch, diagnostics access, margin data for custom labels.
- **Inputs**: Merchant Center diagnostics (account/feed/item), recent ROAS by campaign, search-term/query data, catalog changes log, Google taxonomy mapping.
- **Decision rules**:
  1. IF account-suspension warning present THEN stop all other work; remediate root cause immediately (Elite Brands, FACT/HEURISTIC, T1).
  2. THEN resolve account-level issues → feed-level → item-level; within items: errors before warnings before notifications (AdTribes, HEURISTIC, T2).
  3. IF item errors exist on core revenue SKUs THEN fix those before high-volume non-core warnings (80/20) (Elite Brands, HEURISTIC, T2).
  4. IF price/availability/GTIN mismatch THEN fix at catalog source, never in Merchant Center or supplement feed (existing skill + AdTribes, T1/T2).
  5. IF ROAS dips THEN check diagnostics before touching bids; only move to bid/asset optimization when the feed is clean (existing skill, HEURISTIC, T2).
  6. IF catalog > ~1,000 SKUs THEN rule-based title generation + hand-tuned hero SKUs; document rules with owners and audit quarterly (existing skill + MBA Digital, HEURISTIC, T2).
  7. IF >100 products suddenly disapproved at once THEN suspect account/taxonomy-level change, not per-item issues (community reports, T3).
  8. IF using promotions THEN put promo language in the promotions feed, not titles/descriptions (GetFeeder, FACT, T1).
- **Metrics**: % of items disapproved (core SKUs weighted), account health (warnings count), re-approval latency, CTR on Shopping (title/image proxy), ROAS by custom label. Target: 0 errors on core SKUs; weekly diagnostics review.
- **Stopping rules**: if a fix is re-fetched away (edited in MC), stop and fix source; if rule count > 20 undocumented, halt and consolidate.
- **Conditions**: applies to any Merchant Center account; scaled-down (weekly diagnostics + hero-SKU titles) for small catalogs.
- **Confidence**: T1 for Google mechanics/policy; T2 for triage heuristics; T3 for community-reported edge cases.
- **Key sources**: Elite Brands disapproval triage; AdTribes diagnostics guide; GetFeeder error taxonomy; Shoparize fix guide; MBA Digital debugging guide; Shopify community disapproval thread; existing shopping-feeds skill (validated against sources).

## gtm
## Collision Method sketch — Growth Strategy & GTM
- **Objective**: produce a stage-gated growth strategy: PMF status → primary motion → 1-3 loops → channel mix → metrics.
- **Prerequisites**: product usage data (or survey access), 4-week cohort retention, current CAC/LTV, competitive set.
- **Diagnosis**: (1) run Ellis PMF survey (n≥30 active users) → gate; (2) plot 4-week cohort retention shape; (3) inventory current channels with spend/ROI; (4) identify existing loop mechanics (sharing, content, referrals, usage expansion).
- **Decision rules**:
  1. IF PMF score <40% THEN no paid scale; spend on interviews + activation fixes (Ellis, T1).
  2. IF 4-week cohort retention < ~20-25% (B2C) or <60-70% (B2B SaaS, rough) THEN fix activation/retention before acquisition (Ellis/Balfour, HEURISTIC T3).
  3. IF a natural loop mechanic exists (output feeds input) THEN design loop, set target cycle time & conversion per stage; ELSE use paid/content loops (Balfour, T1).
  4. IF ACV > $25-50k AND complex sale THEN sales-led GTM, marketing = demand creation + sales enablement (Rachitsky/Winters, HEURISTIC T3).
  5. IF ACV < $5k AND self-serve IF product can activate without help THEN PLG (Rachitsky, HEURISTIC T3).
  6. IF first 10 customers not acquired THEN founder-led non-scalable channels only (Rachitsky, T1).
  7. IF attribution model rewards only capture THEN add brand/awareness KPIs (share of search, branded search lift, unprompted awareness) before scaling capture (Walker, T2).
  8. IF growth spend grows faster than retention curve THEN stop and fix retention (Ellis, T2).
- **Metrics**: PMF score, W1/W4/W8 retention, loop cycle time + per-stage conversion, CAC payback, branded search volume, pipeline influenced by non-capture touchpoints.
- **Stopping rules**: stop channel when marginal CAC > LTV (or payback > board threshold); stop loop when cycle conversion < 1.0 without paid input for 2 consecutive quarters.
- **Failure modes**: stage misdiagnosis (scaling pre-PMF), motion mismatch, vanity metrics, capture-only incentive structure.
- **Confidence**: T1 for Ellis/Rachitsky/Balfour framework content; T2 for Walker/Gerhardt opinions; T3 for quantitative retention thresholds (context-dependent).

## market-intel
## Collision Method sketch — Market Intelligence Engine
- **Objective**: produce decision-grade market intelligence — sized, mapped, forecast, demand-validated, industry-staged, trend-ranked — or a documented "insufficient evidence" verdict with the cheapest next test.
- **Prerequisites**: product context, ICP (or ICP hypothesis), pricing intent, competitive set from win/loss shortlists (never AI-generated), 3+ years of any available time-series.
- **Diagnosis**: (1) stage (pre-seed→scale) and data availability decide method depth; (2) category new vs established decides sizing method (bottom-up/value vs top-down+bottom-up); (3) uncertainty level decides forecast method (Bass analogs vs scenario planning); (4) industry vs category lens decides whether Five Forces or market-map leads.
- **Decision rules per discipline**:
  - Market sizing: IF category has countable buyers AND pricing exists THEN bottom-up leads, top-down sanity-checks (a16z, T1). IF brand-new category with no buyer population THEN value method + analog categories (TechTarget/TechCrunch, T2). IF methods diverge >10x THEN return to definitions, not numbers (consensus, T1). IF deck audience is investors THEN lead with bottom-up (VC consensus, T2). IF market has one dominant incumbent THEN add market-shape overlay before trusting TAM (a16z/Haber, T2). IF SOM can't be backed by named accounts THEN shrink SOM (existing + Zimt, T2). IF data older than 18 months THEN re-source before using (Zimt, T2).
  - Market map: IF board-level stakes THEN add 8-12 expert interviews (Infomineo, T2). IF >30 attributes candidate THEN cut to the 2-3 buyers decide on (industry-lens, T2). IF competitor list ≠ win/loss names THEN rebuild from won/lost notes, 5-8 names (industry-lens, T2). IF quadrant empty THEN demand-test before calling whitespace (existing + Umbrex, T2). IF fast-moving category THEN quarterly refresh + event triggers (Infomineo, T2). IF map has no methodology note THEN add one (strategic question + sources + dates) (Infomineo, T2).
  - Market forecasting: IF no direct sales history THEN Bass with 3+ similarity-matched analogs (T2). IF forecast horizon >5 years THEN scenarios, not numbers (existing + McKinsey, T1). IF methods diverge >2x THEN fix assumptions, don't pick the rosier (existing, T2). IF leadership wants one number THEN refuse; deliver range + scenarios + critical assumption (McKinsey, T1). IF actuals miss model early THEN re-check market potential m before blaming execution (Bass practitioner, T2). IF scenario set >5 THEN cut; name them vividly (McKinsey, T1). IF uncertainty high THEN define decision triggers, review quarterly (FP&A practice, T2).
  - Demand analysis: IF no written go/no-go criteria THEN write them first (IdeaCrystal, T2). IF single signal says go THEN require 2+ independent signals converging (IdeaCrystal/ProofEngine, T2). IF search volume high but transactional % <10% THEN awareness≠demand; test willingness to pay (ProofEngine, T2). IF workarounds widespread THEN strong latent demand — escalate to money test (ProofEngine, T2). IF stated interest only THEN cheapest money test (pre-sale/LOI/landing page) before build (ProofEngine, T2). IF one year of Trends shows a spike THEN read 3+ years; spike+decline = fad (existing + Spate, T2).
  - Industry analysis: IF analysis describes the company not the industry THEN restart (Investopedia, T1). IF boundary is "we're in X broadly" THEN pin to substitutes for the customer's job (DrinkBird, T2). IF forces scored without evidence THEN every score needs named evidence or it's labeling (Visual-Paradigm, T2). IF market converging/regulatory-shifting THEN re-run annually or on force-shifting events (DrinkBird, T2). IF force scores numerically averaged THEN discard; qualitative judgment with interaction notes (Visual-Paradigm, T2).
  - Trend detection: IF spike without 6-12 month sustained growth THEN classify fad (Spate, T2). IF single source only THEN hypothesis, not trend; require 2+ independent (Qmarkets/existing, T2). IF confined to one category/demographic THEN low durability (Spate, T2). IF hype signals (vendor count, conference panels) rising fast THEN treat as contrarian entry signal (existing + Gartner, T2). IF no counter-evidence found THEN you haven't looked (existing, T2). IF no kill criteria THEN add kill dates or the watchlist grows forever (existing + Qmarkets, T2).
  - Category design (from positioning.md): IF problem buyers can't name + visibly different solution + budget for multi-year education THEN category design path (Lochhead, T2). IF existing category merely crowded THEN reposition, don't design (Kellogg, T1). IF can't influence the ecosystem THEN abandon category design (Kellogg gate, T1). IF no CEO evangelism/funding THEN category design is fiction (Lochhead preconditions, T2). Measure name adoption, not pipeline (existing, T2).
- **Metrics**: method-gap ratios (top-down/bottom-up), assumption log completeness, scenario trigger hit-rate, forecast-vs-actual error logged quarterly, % claims with dates+sources, trend kill-rate, whitespace win-rate after entry.
- **Stopping rules**: stop when evidence can't move the decision (analysis theater); stop trend watch when velocity stalls at 3-month re-check; stop sizing when assumptions can't be sourced; kill demand validation without a "no" path.
- **Confidence**: T1 for framework consensus (bottom-up/triangulation, Five Forces misuse, McKinsey scenario traps); T2 for quantitative heuristics (SOM %, convergence bands, interview counts); T3 for vendor-claimed thresholds.

## messaging
## Collision Method sketch — Messaging Engine
- **Objective**: produce research-grounded, sophistication-calibrated copy (and offers) for a given funnel position, with validation and iteration.
- **Prerequisites**: (1) funnel + baseline analytics exist (else fix measurement first — Price); (2) buyer language accessible (else run customer research first — Wiebe); (3) market sophistication + awareness-level assessment done (Schwartz).
- **Inputs**: VOC data (tickets, calls, surveys, reviews, sales notes), funnel analytics (drop-off per stage), competitor copy inventory (Ogilvy: 20 years → modern: top-20 competitor pages/ads), offer structure, awareness segmentation per channel.
- **Diagnosis**: Market sophistication stage 1-5 → determines claim type (direct → differentiated → mechanism → named mechanism → identity). Awareness level per audience → determines entry point. Funnel stage (Price) → determines which page gets the treatment. Offer strength (Hormozi: can prospects compare you to alternatives? if yes, stack first).
- **Decision tree**: no baseline analytics → measurement setup before copy. No VOC access → research phase (surveys, ticket mining) before copy. Stage 3+ market → lead with mechanism/proof, not outcome claims. Cold traffic → problem-aware entry; warm/retargeting → offer/close entry. Personality-differentiated category (inboxes, social) → voice-led treatment; unfamiliar category → message-match treatment. Testable traffic → A/B; else five-second tests + observation (Wiebe).
- **Methodology**: research phase (immerse in VOC; synthesize messaging hierarchy) → write phase (research on one screen, copy on other; slightly revise customer language; hook volume: 20 headlines/options per asset; Ogilvy problem-definition sign-off for client work) → validation phase (five-second test clarity; funnel observation; test where possible) → sequence design (Chaperon open loops + behavior branches for email).
- **Execution**: funnel-anchored page treatments; awareness-segmented ad sets; voice-guide + message-match paired; offer stacking when commodity.
- **Metrics**: baseline conversion rate and funnel drop-off deltas; response per variant (Hopkins); clarity pass-rate (five-second tests); open/click/reply for email; cost per acquisition per message variant.
- **Stopping rules**: stop copy work if no buyer language exists and research can't reach customers; stop testing if traffic can't reach conclusive sample (Price); stop if offer is the bottleneck (Hormozi: fix offer before more copy).
- **Failure modes**: research-skipping; sophistication mismatch; awareness mismatch; page-not-funnel optimization; unmeasurable projects; discounting; voiceless AI content.
- **Conditions**: conversion contexts with measurable funnels; email with story-tolerant lists; sophistication framework applies everywhere claims accumulate.
- **Limitations**: voice/results claims often self-reported; Schwartz exegesis here is T2 (secondary source) though canonical; digital formats compress but don't invalidate the frameworks.
- **Confidence**: T1 consensus on research-first (5 practitioners); T2 on individual frameworks; T3 on Hormozi/Chaperon/Cattoni self-reported results.
- **Key sources**: Wiebe 3-part process; Schwartz exegesis (themarketingjuice); Price TCC podcast #17; Halbert starving crowd letter; Ogilvy 11 rules (awai.com); Hopkins TMR (analyticstrategy.com); Chaperon interviews; Hormozi $100M Offers summary.

## outbound
## Collision Method sketch — Outbound Discipline
- **Objective:** predictable reply → conversation → meeting pipeline from cold contacts, with positive sender reputation preserved.
- **Prerequisites:** verified deliverability stack (SPF+DKIM+DMARC, PTR, <0.3% spam rate, warm domain with consistent volume); reply tracking; reply classification taxonomy.
- **Inputs:** meetings-needed target (backwards math: meetings ÷ reply rate 1–4% ÷ open 40–60% = volume/inboxes), ICP + JTBD target map, offer statement.
- **Diagnosis (in order):** (1) Does a stranger respond to the offer with zero risk? No → rebuild offer. (2) Is targeting JTBD-precise? No → fix list. (3) Is copy ≤60 words, human, specific? No → rewrite. (4) Is deliverability clean (per-domain daily checks)? No → fix infrastructure. (5) Opens ok but replies flat → offer problem, not copy.
- **Decision tree — sequence design:** choose cadence by channel mix available: email-only (Berman-style: 2–3 touches, 60-day re-contact) vs multichannel (Ingram: 6–11 touches over 3–4 weeks, touch variety: same-thread/new-thread, voicemail/no-voicemail, video/visual). Kill criteria: <0.5–1% reply on a validated message after 200–300 sends → kill message, change offer or list; domain flagged → replace domain; spam rate rising → halt, diagnose.
- **Methodology:** offer-first copy; personalization decision: genuine 1:1 if research capacity ≥ ~2–3 min/prospect, else offer-first with honest specificity; layer personalization progressively (Ingram); escalate channels (email → LI → phone → video); end with breakup/goodbye touch; classify every reply (positive/negative/neutral/referral) and mine for learning (Ross).
- **Execution:** consistent daily caps (15–30/mailbox/day), warm before scaling, validate on small subset before broad scale (Berman, Ross).
- **Metrics:** reply rate (north), positive reply rate, meetings booked per 1,000 sends, deliverability/inbox rate, spam complaints (<0.3%), bounce rate, per-touch response contribution.
- **Stopping rules:** kill message/list/sequence at predefined thresholds; stop following up after explicit no (Efti: yes/no are answers, maybe is death); cold: max 5–8 touches unless warm.
- **Failure modes:** bought lists, volume spikes, fake personalization, service-pitch-vs-offer, over-follow-up, unmeasured sends, unclassified replies, bolt-on copying.
- **Conditions:** B2B contexts with identifiable JTBD; needs domain + list + tracking infrastructure; method scales from solo (small caps, one domain) to agency (multi-domain rotation).
- **Limitations:** reply-based metrics don't capture call-driven or channel-shift value; vendor benchmarks self-reported; Gmail AI-inbox brief-style filtering (Berman 2026) may reduce cold-email visibility regardless of technique.
- **Confidence:** T2 overall — offer-first, reply-rate-north, deliverability-discipline are T1-convergent (4+ independent practitioners + regulatory facts); specific rates (12%, 20%, 1-in-400) are T3.
- **Key sources:** alexberman.com (3 posts, 2026); Lavender LinkedIn data (2024–25); Mailshake State of Cold Email 2025; gtmnow.com Ross retrospective; predictablerevenue.com Outbound Validation; Gmail sender guidelines.

## paid-strategy
## Collision Method sketch — "Paid Strategy & Media Plan" (what the Marketing OS should encode)

- **Objective**: produce and govern a paid-media strategy: budget size, brand:activation split, channel plan, and measurement/reallocation loop for a given business context.
- **Prerequisites**: stage (pre-seed→scale), category + consideration level, brand age, online/offline mix, channel validation status, measurement infrastructure, cash position/payback tolerance, last-12-months revenue by real source.
- **Inputs**: revenue and spend by channel (MER-able), platform ROAS, segment data (size/value/share), funnel conversion rates, sector benchmark ratio (Binet/Field ready-reckoner style), previous plan results.
- **Diagnosis**: (1) maturity audit (Francois): validated channels? defensible positioning? measurement infra? (2) budget-truth audit (Walker): map inbound revenue to real source vs budget split; (3) overlap tax check (AdMaxxer): sum(platform ROAS×spend)/revenue − 1; (4) penetration vs loyalty gap (Sharp) where brand data exists.
- **Decision tree**:
  1. If pre-PMF / cash-constrained / <12 mo runway → 20–30% brand ceiling, performance-led, payback window set by cash (Seufert; Francois).
  2. Else if established B2C → start 62:38; if high-consideration/rational or online-first → raise brand share; if low-consideration/emotional or travel-like → lower (Binet & Field).
  3. Else if B2B → 46:54 baseline (Binet/Field), or 20–30% brand motion with founder-led organic counted as brand (Walker); demand 50–60%; expand 10–20%.
  4. Then: brand stream targets whole market/category buyers (Sharp), activation stream targets selected segments (Ritson); hold split ~annually, not quarterly.
- **Methodology**: Ritson's plan structure (12-month increment; diagnosis→strategy→tactics; segmentation→targeting arms→positioning→pointy objectives→tactics with costs); Sharp's reach/DBAs for creative; Binet's long/short principles as the ratio engine.
- **Execution**: two-speed streams where budget allows; lean teams: 60–70% primary channel / 20–30% compounding / ≤10% experiments, all above minimum viable spend thresholds (Spike).
- **Metrics**: MER at P&L level (target ≈ 1.3/contribution margin); platform ROAS only for creative/optimization; iROAS for budget decisions; MMM quarterly if scale supports; brand effects (mental availability/CEPs, share of search, branded query volume) for the brand stream.
- **Reallocation loop**: monthly: MER drift (>10% jump = overlap/retargeting problem); quarterly: incrementality tests on suspect channels (brand search, retargeting, PMax — test first per AdSights); annual: split review vs stage (Francois).
- **Stopping rules**: cut channel if iROAS < contribution-margin breakeven after a valid test; kill criteria 3-of-4 (conversion volume, CAC > 2x target, declining marginal returns, team-time drain — Spike); never cut prospecting on reported ROAS alone (AdSights: 1.3x prospecting can feed 4.5x MER); stop brand-measurement-via-ROI debates — use brand metrics.
- **Failure modes (guardrails)**: bottom-funnel over-scaling (Walker/Seufert), brand starvation via 12-month trap (Ritson/Binet), overlap tax >35% (AdMaxxer), underfunded tests (Spike), loyalty-targeted brand plans (Sharp), confounded holdouts (Metricuno), fixed splits (Francois).
- **Conditions**: full method for established multi-channel businesses; scaled-down (MER + platform lift tests, no MMM; cheap brand assets instead of paid reach) for small teams.
- **Limitations**: correlational evidence base for ratios; no public evidence at small-budget scale; B2B ratios are practitioner-consensus, not databank-grade.
- **Confidence**: T1 for consensus layer (Binet/Sharp/Seufert primary sources); T2 for ratio numbers and vendor benchmarks; T3 for stage-by-stage percentage tables.
- **Key sources**: Binet & Field *Effectiveness in Context* (2022) + *Long and the Short of It* (2013); Sharp *How Brands Grow* + Ehrenberg-Bass essays; Ritson Marketing Week columns (2021–2022); Seufert Mobile Dev Memo (2018–2024); AdMaxxer/AdSights MER-vs-ROAS; Metricuno incrementality guide; Refine Labs budget article; Spike lean-team framework.

## partnerships
## Collision Method sketch — PARTNERSHIPS
- **Objective**: profitable incremental acquisition via partners (affiliates, referrers, creators) measured per-partner CAC vs paid CAC.
- **Prerequisites**: product with retention (for referral) or commissionable margin (for affiliate); tracking infra (links, cookies/attribution, payout rules); fraud policy.
- **Diagnosis**: which channel fits? Referral if high retention/NPS; affiliate if margin + affiliate supply exists; influencer if brand-audience gap and budget for measurement.
- **Decision tree**:
  1. IF NPS < ~30 or retention weak THEN fix product before referral (Ellis). 
  2. IF K < 0.15 THEN treat referral as assist channel, don't staff for virality.
  3. IF launching affiliate THEN write terms/creatives/tracking first (Prussakov setup rule); recruit 10-20 quality affiliates before scaling.
  4. IF influencer THEN require measurement plan (lift or paid-benchmark comparison) before spend.
  5. IF affiliate fraud appears THEN policy + tracking fix, not program shutdown.
- **Methodology**: 5-metric referral funnel diagnosis; partner-as-partner management (communication, tools, recognition > money); creator briefs with clear outcomes.
- **Metrics**: K-factor, share rate, invite CTR, invite conversion, per-affiliate EPC and CAC, influencer CPM/ROAS vs paid, activated-referral rate, fraud rate.
- **Stopping rules**: IF per-partner CAC > paid CAC for 2 quarters THEN cut partner channel or re-price commission; IF share rate < 5% after reward redesign THEN channel mismatch — stop pushing referral; IF influencer underperforms paid benchmarks after re-brief THEN terminate.
- **Failure modes**: employee-treatment of affiliates, signup rewards, no tracking, unmeasured influencers, fraud paranoia, launch-before-setup.
- **Confidence**: T1 = Prussakov essays, Viral Loops metric docs; T2 = Gagliese/Viral Nation case material, Ellis loops (canon, T2); T3 = any specific ROI percentages from vendor marketing.

## positioning
## Collision Method sketch — Positioning Engine
- **Objective**: produce a defensible, evidence-backed positioning (frame + best-fit segment + differentiation claims) that aligns sales and marketing, or a documented decision NOT to reposition.
- **Prerequisites**: ≥10 closed deals with repeatable pattern (else: run Shah's PMF survey first); access to sales team; win/loss data; customer language.
- **Inputs**: customer shortlists (who we win/lose against), unique attributes inventory, customer-value evidence, ICP characteristics, market shifts (for narrative option).
- **Diagnosis**: (1) Is it a positioning problem or execution/fit problem? (message≠pitch → positioning; losing to inferior products → positioning; no repeatable wins → PMF, not positioning). (2) Is there a credible big change to name? → decides Raskin vs Dunford path. (3) Is the product self-serve? → Bush path.
- **Decision tree**: no PMF → PMF survey (40% very disappointed) before positioning. Stable market → Dunford 5-step (competitive alternatives → uniqueness → value → who cares → frame choice; validate frame with the alternatives question from PMF survey). Shifting market + stakes → Raskin 5 elements. Me-too brand → Neumeier onlyness test (if a competitor could claim it, it's not a position). Whitespace + budget + CEO willingness → category design (Lochhead), gated by Kellogg's skepticism (can we influence the rugby scrum?).
- **Methodology**: pre-work interviews (exec, sales, customers) → evidence pack (shortlists, win/loss, customer language) → structured workshop (diagnostic, not brainstorm; agenda visible; data/opinion separated; CEO managed via pre-interview) → ranked differentiation claims each with proof → position statement + chosen frame → pressure test against sales reality.
- **Execution**: positioning brief (statement, ranked claims, ICP, proof points, explicitly-rejected claims) stored permanently; translate to sales narrative (Raskin structure if urgency exists); refresh every 6-12 months.
- **Metrics**: win rate vs inferior competitors; message/sales consistency; internal alignment; % of claims with named proof; switch-trigger presence ("why now").
- **Stopping rules**: stop workshop if ICP argument reveals product serves multiple significantly different segments (product problem, not positioning); stop category-design path if budget for strikes < what the whitespace requires; stop if claims can't be proven in the room.
- **Failure modes**: brainstorm-workshops; CEO anchoring; evidence-free claims; "the next X"; starting from problem statements; AI-generated competitor sets.
- **Conditions**: B2B SaaS/enterprise with shortlist data; PLG variant for self-serve products; category design only with funding.
- **Limitations**: methods are practitioner frameworks, not RCTs; category-design evidence thin/self-referential.
- **Confidence**: T1 for consensus rules (4+ practitioners), T2 for individual frameworks, T3 for category-design economics claims.
- **Key sources**: Dunford product-positioning exercise; Raskin Greatest Sales Deck; Kellogg categories essay; Shah PMF thread; Bare Strategy workshop playbook; Play Bigger category design; Moore positioning page.

## pr-launches
## Collision Method sketch — PR & LAUNCHES
- **Objective**: third-party validation (earned) + AI-citation visibility + launch-day momentum, measured in coverage quality and downstream pipeline, not AVE.
- **Prerequisites**: owned content foundation (PESO), journalist target list (not 100s), monitoring (Google Alerts + X + trade press) for both personal sphere and global sphere (Meerman Scott).
- **Diagnosis**: which PESO channels exist today? (gap = usually earned); is there internal speed to publish in <4h?
- **Decision tree**:
  1. IF owned/shared don't exist THEN build them before pitching (PESO handoff rule).
  2. IF story breaks in your market and you have a credible tie THEN newsjack within hours (second-paragraph content), else skip.
  3. IF pitching a specific journalist THEN ≤150 words, plain text, one relevant reason; IF tier-3/long-tail THEN volume acceptable.
  4. IF launch on PH THEN B2B Mon-Thu, hunter contacted 2-3 weeks out, community assembled, 24h comment engagement staffed.
- **Methodology**: PESO system with handoffs; newsjacking lanes; pitch discipline (short, plain, relevant).
- **Execution**: monitor → react (newsjack) or plan (campaign) → pitch individually → amplify earned via shared + paid.
- **Metrics**: coverage count/quality, journalist reply rate, share of voice, AI-citation mentions, PH rank + day-1 signups + comments depth; guardrail: no AVE/vanity.
- **Stopping rules**: IF reply rate <5% after 20 individualized pitches THEN rewrite pitch template, don't send more; IF newsjacking attempts get 0 pickups 3x THEN no legitimate tie — stop forcing it; IF PH launch day-1 signups < threshold THEN fix activation before next launch.
- **Failure modes**: release-only PR, spray-and-pray, no monitoring, slow approvals, launch-day ghosting.
- **Confidence**: T1 = Zitron pitch rules, Meerman Scott newsjacking (primary docs); T2 = PESO outcomes claims, KWD PH guidance; T3 = Chris Messina specifics (not fetched this session).

## pricing
## Collision Method sketch — Pricing & Packaging
- **Objective**: set or revise pricing/packaging with measured WTP, not imitation.
- **Prerequisites**: defined buyer personas, feature list, usage instrumentation, ≥20-30 customers + prospect access, competitive price points.
- **Diagnosis**: (1) map current plan structure + revenue concentration by plan; (2) run 4-point WTP survey across 3 segments; (3) run forced-choice feature-preference survey (most/least important); (4) compute price elasticity + relative feature value; (5) identify the value metric via "what does the customer get more of as they succeed".
- **Decision rules**:
  1. IF no WTP data THEN do survey before any price change (Campbell, T1).
  2. IF plan is flat/single THEN add Good-Better-Best tiers; price middle at median WTP, top at +50-100% with the value metric as gate (Poyar/Campbell, HEURISTIC T2).
  3. IF usage can be instrumented AND usage correlates with customer success THEN use usage/hybrid pricing with base + overage; ELSE seat or flat (Ramanujam/Poyar, T1/T2).
  4. IF a segment's WTP differs >~30% from another THEN create separate tier/packaging for it (Campbell, HEURISTIC T3).
  5. IF a feature is loved but not monetized (hidden gem) THEN create premium edition or add-on around it (Ramanujam, T1).
  6. IF pricing hasn't been reviewed in 6+ months THEN schedule review within the quarter (Campbell, T1).
  7. IF customers can't explain what they pay for THEN simplify: fewer credit types, clear docs, spend visibility (Poyar 2026, T1).
  8. IF discounting >25% is common THEN stop; fix packaging/WTP instead (Campbell, EMPIRICAL T1).
- **Metrics**: WTP distribution per segment, % revenue by tier, expansion rate (NRR), discount depth, price-change churn, forecast accuracy (usage plans).
- **Stopping rules**: stop a price change if churn in the affected cohort exceeds pre-change baseline by >1.5x for 2 months; stop usage pricing if forecast error >30% for 2 quarters.
- **Failure modes**: feature shock, minivation, hidden gem, undead; last-minute pricing; copying competitors; discount addiction.
- **Confidence**: T1 for Campbell/Ramanujam/Poyar core claims; T2-3 for thresholds (segment-specific).

## research
## Collision Method sketch — the Marketing OS should encode:

- **Objective**: produce decision-grade customer evidence for ICP, personas, messaging, positioning, and win/loss — without fabricating segments.
- **Prerequisites**: CRM with closed-won/lost deals (if B2B); customer/buyer access; recording capability; one trained interviewer (anyone can learn, but skills matter: "bad interviewers get opinions, not events" — Moesta).
- **Inputs**: existing won/lost data; support tickets; sales call recordings; funnel analytics (Momoko: baseline conversion + traffic or don't start); a list of jobs/segments under question.
- **Diagnosis**: if no won deals exist → discovery mode (Mom Test + switch interviews on adjacent categories). If deals exist → persona/ICP mode (20–30 closed-won analysis → interviews per role). If deals are being won/lost at scale → win/loss mode (≥20 interviews/segment, neutral interviewer).
- **Decision tree**:
  1. Can we recruit people who recently switched or decided (30–90 days)? → switch-style interviews. Else → Mom Test with current-customer proxies.
  2. Do we need prioritization/market size, not just direction? → add survey/quant phase (Ulwick-style outcome statements or simple frequency/priority questions).
  3. Are we building personas? → one per buying-committee role; data from won AND lost buyers; half a page: trigger, metric they answer for, first objection, line that moves them; refresh quarterly.
  4. Are we building ICP? → mine closed-won for common attributes → interview top customers (≥10) for language → cluster firmographic+technographic+behavioral signals → score fit and intent separately → refresh quarterly.
  5. Win/loss program? → leadership/sales buy-in first; third-party interviewer; record+transcribe; tag themes; ≥20 interviews per segment; present findings with action items; tie into persona refresh.
- **Methodology**: interview rules — past facts not future opinions; specifics not generalizations; their language verbatim; deflect pitches; recruit both sides (won/lost, switched/almost-switched); 45–90 min (switch), 20–30 min (Mom Test); record everything; stop at saturation (pattern repetition; 9–17 for homogeneous groups; 20–30 if you want 90%+ of needs; 20+/segment for win/loss themes).
- **Execution**: small continuous batches (Torres/Alvarez) rather than one giant study; pair interviews (one drives, one listens — Moesta); transcribe and tag; synthesize into timeline/forces or 5-ring or role-persona format depending on goal.
- **Metrics**: saturation reached (not quota); % interviews yielding new facts; % quotes usable in copy; persona/ICP refresh recency; win/loss: theme frequency per segment, action items closed.
- **Stopping rules**: stop interviewing when stories/patterns repeat (Moesta's "could direct the actor", Blank's convergence); stop when a hypothesis is validated/invalidated enough to act; win/loss: stop per segment at 20 interviews or when themes stabilize; kill survey work if baseline analytics absent (Price).
- **Failure modes (encode as guards)**: leading questions; pitching; compliment-data; demographic personas; happy-customer-only samples; survey-for-discovery; NPS-as-score; rep-run win/loss; acting on 1–2 interviews; AI personas trained on generic internet content (AI is fine on YOUR transcripts, never as persona oracle — ziellab).
- **Conditions**: method scales from 2-person startup (Mom Test + 5–8 interviews) to enterprise (ODI-scale quant + continuous discovery + win/loss programs); the binding constraint is always honest access to recent deciders.
- **Limitations**: no method yields market size without quant; saturation ≠ representativeness; JTBD/job framing requires an existing switching category; win/loss needs deal volume.
- **Confidence**: consensus rules T1 (multiple independent sources); thresholds and counts T2 (single-source or company-internal).
- **Key sources**: jobstobedone.org/switch-interview; momtestbook.com; steveblank.com manifesto; clozd.com win-loss program guide; sloanreview.mit.edu NPS; Krosnick questionnaire design (Stanford PDF); nngroup.com interview sample size; PubMed saturation review; ziellab persona-fiction guide; github.com/cindyalvarez/customerdevelopment; agiledata.io Ulwick interview.

## retail-media
## Collision Method sketch — "Retail Media Plan" (what the Marketing OS should encode)
- **Objective**: decide which retail media network(s) to use, architect campaigns, and measure incrementally for a CPG/consumer brand.
- **Prerequisites**: product sold at the retailer; availability (no OOS); margin model incl. ad allocation; measurement requirement agreed with finance before launch; trade calendar.
- **Inputs**: retailer presence + data access, budgets (trade vs digital), audience segment definitions, promo calendar, category seasonality, previous incrementality results.
- **Decision rules**:
  1. IF product not sold at the retailer THEN don't run retail media there (existing skill, HEURISTIC, T1).
  2. IF any SKU is out of stock THEN pause its ads before spending (universal, HEURISTIC, T1).
  3. IF sponsored search spend < ~$50k/month or profitability inconsistent THEN skip DSP; invest in on-site first (Darkroom, HEURISTIC, T2).
  4. IF goal = new customer acquisition THEN prioritize NTB-reporting formats (SB video, DSP NTB-optimized) and set NTB% targets (Pathfinder case; SellerStack, HEURISTIC, T2).
  5. IF branded on-site terms have high organic share THEN test cannibalization with holdout before scaling (SellerStack; paid-strategy synthesis, EMPIRICAL, T2).
  6. IF network offers audience segments THEN verify segment definitions/refresh cadence before trusting them (existing skill, HEURISTIC, T2).
  7. IF budget > ~$100k/month retail media THEN require AMC/MMM incrementality read, not dashboard ROAS (synthesis inference; SellerStack, HEURISTIC, T3).
  8. IF trade budget funds media THEN coordinate with JBP/promo calendar; continuous flighting (existing skill, HEURISTIC, T2).
- **Metrics**: platform ROAS (directional only), NTB%, incrementality lift (holdout/AMC), halo sales, TACoS-equivalent (total ad spend / total retailer sales), category share. Guardrail: NTB% < 10% on acquisition campaigns = audience too small/lapsed-heavy.
- **Stopping rules**: cut network if valid holdout shows iROAS below contribution-margin breakeven; stop DSP if search efficiency doesn't improve within 2 quarters (flywheel not spinning).
- **Conditions**: full method for CPG at scale; scaled-down (on-site only + NTB tracking, no DSP) for small budgets.
- **Confidence**: T1 mechanics; T2 heuristics; T3 vendor benchmarks.
- **Key sources**: Darkroom DSP explainer; SellerStack incrementality/halo; Instacart incrementality methodology (company.instacart.com); Perpetua Instacart guide; Eva Commerce Walmart Connect guide; Walmart Connect resources; AMZ Pathfinder DSP/SB case studies; Feedvisor 2022 brand survey; Adverity Instacart metrics.

## seo
## Collision Method sketch — "SEO Operating System"
- **Objective**: grow qualified organic demand (traffic → demos/revenue per stage) while minimizing core-update and scaled-content enforcement risk; track classic SERP + AI citations.
- **Prerequisites**: GSC access with ≥3 months data; crawl/log access; engineering relationship; business KPIs (not just rankings).
- **Inputs**: GSC (queries/pages/index coverage), crawl data, SERP landscape, competitor + AI-citation snapshot, update calendar (Barry Schwartz layer), business goal list.
- **Diagnosis** (gate everything): (1) If traffic drop: delta report → classify relevancy/intent/quality (Gabe+Ray); never remediate before classification. (2) If launch/migration: index coverage + rendering parity audit (Indigo). (3) If new site/stagnation: index/crawl health first (Mueller inventory rules, Stox order).
- **Decision tree**:
  - Technical: index/crawl issues → templates-not-pages → impact×effort matrix → 5-10 dev tickets + governance (Stox/Solis). Test template-level changes with controls when ≥100 similar pages (Critchlow); never deploy untested best-practice at scale.
  - Content: bottom-funnel intent filter (Dunning) → traffic-potential filter (Soulo) → topical coverage where link capacity is low (Gubur, conditioned) → audience-pain selection where buyers don't search (Law). Citable structure (answer-up-front, unique data) always (Dunning/Indig).
  - Programmatic: build template → validate uniqueness floor per page → ship waves → monitor indexation + volatility → kill or differentiate templates that duplicate (Indig + enforcement lessons).
  - Links: earned-only policy (editorial/data-driven PR; value trades) — Moogan's sustainability test; McGuirk's expectation calibration (1-20 links); Milligan's internal-data-first research; Dean's skyscraper as legacy option with intent-first overlay.
  - Local: GBP + relevance/distance/prominence triad; test single variables on real profiles (Hawkins); citations as consistency not links, supplier-tier-first (Shaw/Blumenthal); landing pages with real words; review velocity.
- **Execution**: developer-ticket format with acceptance criteria; SEO requirements baked into launch lifecycles (Indigo); velocity (keyword→publish in days, not months — Dunning).
- **Metrics**: primary = demos/revenue attributed to organic (B2B), or conversions (commerce); secondary = traffic, AI citation share (Indig), index coverage, core-update volatility exposure, referring domains from earned sources. Rankings are diagnostic, not the goal.
- **Stopping rules**: kill templates/pages that duplicate or produce zero engagement; stop tactics that fail Moogan's sustainability test; stop chasing keywords with volume but no traffic potential; stop short-term testing of site-level quality recovery.
- **Failure modes**: content decay; programmatic without quality floor; untested scale rollouts; volume-first selection; virality-chasing PR; single-cause attribution of drops.
- **Conditions**: applies broadly; depth of each sub-method depends on site type (e-commerce → testing + product-led; B2B SaaS → bottom-funnel + AI citations; local → GBP stack; media → topical authority + digital PR).
- **Limitations**: all non-Google practitioner claims are inference; local study data US-centric and time-bound; AI-search behavior changes monthly; correlation vs causation everywhere (Capper's filter).
- **Confidence**: T1 for the 10 consensus rules (multi-practitioner); T2 for sub-methods; T3 for Gubur's linkless ranking claims and AI-search specifics.
- **Key sources**: see per-practitioner files; top primary sources listed in the research summary.

## social
## Collision Method sketch — SOCIAL
- **Objective**: build an owned audience that converts (leads/community), not vanity reach.
- **Prerequisites**: 1 platform chosen as primary (Cole); clear audience + purpose (Bloom/Millington); 30-60 day runway for baseline.
- **Diagnosis**: measure own baseline norm (vDB: reach is 50% baseline) → set "abnormally good for you" bar = 4x norm.
- **Decision tree**:
  1. IF no primary platform THEN pick one by audience location, not trend (Cole).
  2. IF goal = new audience THEN formats that skew out-of-network (images, long-form, articles) (vDB); IF goal = deepen existing THEN polls/reposts/live.
  3. IF B2B/ICP on LinkedIn THEN LinkedIn first (Welsh); IF developer/technical THEN Reddit presence is non-optional (SEL).
  4. IF community build THEN define purpose + 3 value behaviors before tools (Millington).
  5. IF YouTube THEN packaging test (2 thumbnails) before full production (Eves/Schmoyer).
- **Methodology**: volume system (Welsh ContentOS: curate → templatize → create → distribute); 1 idea → 7 formats; write meat first then trailer (Welsh); rule of one + 50% cut (Drew); republish to secondary platforms (Cole).
- **Execution**: post daily minimum; rotate formats; reply to every comment thread (vDB penalty for ghosting); DM-send worthy content.
- **Metrics**: baseline reach, 4x-norm rate, saves/DM-sends per 1000 impressions, comment-thread depth, follows-per-impression; YouTube: retention % at 30s/50%, CTR, suggested-traffic share; community: 6 value behaviors + retention lift.
- **Stopping rules**: IF 60 days no post exceeds 4x own norm AND format rotation done THEN re-examine topic-market fit, not tactics; IF community activity rises but value behaviors flat for 2 quarters THEN cut engagement-boosting tactics (Millington).
- **Failure modes**: pods, deletion habit, gating, corporate tone, chasing platforms, no baseline.
- **Confidence**: T1 = van der Blom dataset as reported; T2 = Welsh/Cole/Drew/Schmoyer systems; T3 = Reddit/IG-TikTok claims (thin field).
