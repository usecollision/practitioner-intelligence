# SYNTHESIS — Pricing & Packaging

Practitioners: Kyle Poyar, Patrick Campbell, Madhavan Ramanujam, Dan Balcauski. Verified 2026-08-15.

## Consensus
- **Price off value, not cost** (all four): value metric must track what the customer gets (usage, outcomes, seats-as-gateway), not what you spend. Ramanujam: "design the product around the price" (FRAMEWORK, T1).
- **Package to sell — Good/Better/Best** (Poyar, Campbell, Ramanujam): 3 tiers at minimum; the middle tier anchors; no single flat plan (HEURISTIC, T1/T2).
- **Willingness-to-pay (WTP) data beats guessing**: Campbell's 4-point economic survey — "too expensive / getting expensive / a good deal / too cheap to trust the quality" — open-ended price answers, surveyed across 3 groups: current customers, prospects who know you, target customers who've never heard of you (they give different answers; brand lifts WTP) (FRAMEWORK, T1).
- **Survey, don't A/B test, for pricing** (Campbell): pricing A/B tests need >30,000 users for a 10% lift; customers find them disingenuous. Ask instead (EMPIRICAL, T1).
- **Revisit pricing regularly** (Campbell: quarterly; Poyar: 2025 data shows market moving constantly): "unchanged prices mean years of lost revenue" (HEURISTIC, T1).
- **Usage/outcome-based pricing wins when it matches value, but adds forecasting burden** (Poyar 2026): credit models exploded +126% YoY in 2025 among top 500 SaaS/AI, then the pendulum swings back to simplicity — 2026 trend is re-bundling and hybrid (EMPIRICAL, T1).
- **Pricing problems are value-clarity problems** (Poyar): if customers don't understand what they pay for, no model feels right (OPINION/EMPIRICAL, T1).

## Disagreement
- **Seats vs usage vs hybrid**: Campbell historically favored value metrics/usage for expansion; Poyar's 2025-26 data shows pure usage creates CFO forecasting pain and pure seats leaves expansion money on the table → hybrid (seat base + usage expansion) is the emerging consensus for AI/SaaS (EMPIRICAL, T1). Balcauski: operations-first — pick the model you can actually bill, forecast and support (HEURISTIC, T3).
- **How often to change price**: Campbell says quarterly review; Poyar cautions churn-inducing instability (3.6 pricing changes/company in 2025 = loss of confidence). Condition: review quarterly, *ship* changes only when value is demonstrably re-communicated (T1/T2).
- **Grandfathering/legacy pricing**: no consensus; Poyar notes most 2025 changes included grandfathering or usage caps; treat as negotiation, not pricing (T2).

## Conditions
- WTP survey: works with any customer base ≥ ~100 customers/prospects for statistical comfort; minimum viable at 20-30 responses per segment (T2).
- Van Westendorp price-sensitivity: B2C/self-serve, where price perception drives conversion; weak for complex B2B enterprise negotiations (T3, practitioner consensus).
- Value-metric pricing: needs product instrumentation on usage; fails if usage ≠ value received (e.g., admin tools) (Ramanujam, T2).
- Poyar trend data: top-500 SaaS/AI with transparent pricing; may not hold for mid-market private companies (EMPIRICAL, T1 for the dataset).

## Failure knowledge
- **Ramanujam's four failure patterns** (72% of new products fail financially; T1): (1) Feature shock — too many features, overpriced, no segment resonance; (2) Minivation — right product, priced too low, leaves revenue; (3) Hidden gem — product customers love but company can't monetize (no value metric); (4) Undead — "me too" product nobody asked for. Fix: WTP + feature-preference research before launch, price anchored to value metric (EMPIRICAL, T1).
- Last-minute pricing (price set after product built) — the root cause of most failures (Ramanujam; T1).
- Discounting as default: Campbell 2018 research — ~80% of SaaS companies discount ≥25% to acquire; discounting destroys the WTP curve you measured (EMPIRICAL, T1).
- Copying competitor pricing without own WTP data (Poyar, Campbell; T2).
- Usage pricing without spend visibility/control for buyers → churn and CFO resistance (Poyar 2026; T1).

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

## Sources
1. Kyle Poyar — 2025 pricing year in review / 2026 trends | substack.com/@kylepoyar/note/c-196463953 | T1 | 2026-08-15
2. Kyle Poyar — Top B2B pricing challenges (230+ companies) | linkedin.com/posts/kyle-poyar (2026-05) | T1 | 2026-08-15
3. Patrick Campbell — The Five Biggest Pricing Mistakes | saasmag.com/five-biggest-saas-pricing-mistakes | T1 | 2026-08-15
4. Patrick Campbell — Step-by-Step Framework for SaaS Pricing (podcast) | saasclub.io/podcast/saas-pricing-patrick-campbell-price-intelligently | T1 | 2026-08-15
5. Madhavan Ramanujam & Georg Tacke — Monetizing Innovation (book) | oreilly.com/library/view/monetizing-innovation/9781119240860/c03.xhtml | T1 | 2026-08-15
6. Ramanujam interview | marketingjournal.org/monetizinginnovation | T1 | 2026-08-15
7. Dan Balcauski — Pricing Ops (pricing operations for SaaS) | pricingops.com | T3 (not fetched this session)
