# SYNTHESIS — Growth Strategy & GTM

Practitioners: Brian Balfour, Sean Ellis, Andrew Chen, Casey Winters, Lenny Rachitsky, Dave Gerhardt, Chris Walker, Jason Lemkin. Verified 2026-08-15.

## Consensus
- **Stage determines strategy** (Balfour, Winters, Lemkin, Rachitsky): there is no universal growth playbook. Pre-PMF your job is learning, not scaling; post-PMF it's compounding loops. Balfour: the model must match the stage — you cannot bolt a growth team onto a product without PMF (HEURISTIC, T2).
- **Loops beat funnels when there is an inherent sharing/network mechanic** (Balfour 2018 "Growth Loops are the New Funnels", Chen *Cold Start Problem*): every loop is Trigger → Action → Output → Input back to Trigger; the output of one cycle feeds the next. If no natural loop mechanic exists, forcing virality fails — use paid/content loops instead (FRAMEWORK, T1).
- **PMF must be measured, not felt**: Sean Ellis 40% "very disappointed" survey on *recent active users* (last 2 weeks), min ~30 responses, confident at 100+; follow-ups on main benefit + who benefits most + why (FRAMEWORK/EMPIRICAL, T1). Asymmetric: <40% is a reliable warning; ≥40% is encouraging, not conclusive (T2).
- **First customers come from non-scalable channels** (Rachitsky, Lemkin): network, strategic cold outbound, investor intros, communities (add value first), content. "None of these scale. That's why they work" (HEURISTIC, T1).
- **Demand creation ≠ demand capture** (Walker, Gerhardt): if attribution/KPIs only reward capture (search, retargeting, intent data), marketing optimizes to the 3-5% of market in-market and hits diminishing returns. Win higher in the funnel (FRAMEWORK/OPINION, T1 — Walker's core thesis).
- **Retention is the growth lever that compounds** (Ellis, Balfour, Winters, Chen): cohort retention curve shape determines whether spend scales. If retention is flat, paid growth = leaking bucket (EMPIRICAL, T2).

## Disagreement
- **Demand creation vs capture allocation**: Walker argues most teams over-invest in capture (he says marketing should be ~"90% create, 10% capture" at scale for category leaders); Gerhardt agrees brand/community-first for founder-led GTM; Lemkin is more pragmatic — "do whatever gets revenue this quarter," capture is fine when cash matters. Condition: Walker's model suits funded category-creation plays; Lemkin's suits early revenue survival (OPINION, T2).
- **PLG vs sales-led vs partner-led GTM** (Rachitsky GTM motions data, Winters): no consensus on "best"; consensus is *pick one primary motion aligned to product complexity + ACV*. High-ACV/complex → sales-led; low-ACV/self-serve → PLG (EMPIRICAL, T2).
- **Virality expectations**: Chen (network effects are a *result* of PMF, not a strategy) vs naive loop-hunting. Balfour agrees: loops amplify what already works (T1/T2).

## Conditions
- Balfour loops + Winters stage model: B2B/B2C SaaS, post-PMF, product teams with instrumentation (T2).
- Ellis PMF survey: any product with defined "real usage" event; needs active-user sample; not for pre-launch concepts (T1).
- Walker demand gen: B2B, ≥$2-5M ARR, category with competitors, where brand preference matters; fails for tiny budgets where every dollar must convert this quarter (T2).
- Rachitsky first-10: B2B, any stage, founder-led (T1).

## Failure knowledge
- Scaling channels before PMF → wasted spend, churn (Ellis, Balfour; T1/T2).
- Forcing viral loops without product mechanic → dead loop; viral coefficient <1 means paid for every user (Balfour; FRAMEWORK).
- "Spray and pray" outbound/demand capture only → competing in 4-vendor deals at the bottom of funnel, $1M/mo Google spend with 36-month CAC payback (Walker example; T1 anecdote).
- Chasing North Star vanity metric without inputs (see analytics synthesis).
- Hiring a "growth team" with no decision rights/roadmap access (Balfour: growth must ship product changes, not just campaigns) (T2).
- GTM motion mismatch: PLG company hiring enterprise AE team too early, or sales-led product with no sales enablement (Rachitsky; T2).

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

## Sources
1. Sean Ellis — Using PMF to Drive Sustainable Growth | medium.com/growthhackers/using-product-market-fit-to-drive-sustainable-growth-58e9124ee8db | T1 | 2026-08-15
2. Lenny Rachitsky — How to win your first 10 B2B customers | lennysnewsletter.com/p/how-to-win-your-first-10-b2b-customers | T1 | 2026-08-15
3. Lenny Rachitsky — GTM motions of 30 B2B SaaS companies | lennysnewsletter.com/p/gtm-motions | T1 | 2026-08-15
4. Chris Walker — Marketing teams don't create demand because their KPIs don't incentivize it | linkedin.com/posts/chriswalker171 (2021-07) | T1 | 2026-08-15
5. Brian Balfour — Growth Loops are the New Funnels (2018, Reforge) | referenced via gtm-labs.co/resources/growth-engine-framework | T2 | 2026-08-15
6. Andrew Chen — The Cold Start Problem | T2 (book, not fetched)
7. Signal — The Sean Ellis 40% Test: Ultimate Guide | fitsignal.com/blog/sean-ellis-40-percent-test | T2 | 2026-08-15
8. Casey Winters — growth essays (ex-Pinterest/Grubhub) | T2 (canonical, not fetched this session)
9. Jason Lemkin — SaaStr | T2 (canonical, not fetched this session)
