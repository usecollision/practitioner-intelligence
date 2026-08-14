# SYNTHESIS — Amazon Ads & Marketplace Expansion

Practitioners: Mike Zagare (PPC Entourage founder, educator), Brent Zahradnik (AMZ Pathfinder founder, now Head of DSP at SellerPlex, Beyond PPC host), Chris McCabe (ex-Amazon Seller Performance investigator, ecommerceChris), + panel: Ash Metry (Keywords.am), AMALYZE, SalesDuo, Darkroom Agency, Perpetua, SellerStack, Pattern, Marketplace Pulse (Ben Donovan/Juozas Kaziukenas), Feedvisor, r/FulfillmentByAmazon + r/AmazonFBA field intel. Verified 2026-08-15.

## Consensus
- **Ads amplify a listing; they cannot fix a weak one.** Listing conversion (reviews at category parity, price, images, Buy Box) is the gate before scaling spend (Zagare; Pathfinder; every agency). HEURISTIC, T1.
- **Allocation beats volume.** Where SP/SB/SD budget goes matters more than how much you spend; a $3k/month correctly split outperforms $10k spread evenly (Keywords.am). 60/30/10 (SP/SB/SD) is a *starting point*, not a rule; lifecycle stage changes it: launch ≈ 80/15/5, growth ≈ 60/25/15, mature ≈ 50/25/15 (+10 DSP), brand-under-attack ≈ 40/35/25. HEURISTIC (agency consensus, Keywords.am 2026), T2.
- **ACoS is a campaign metric; TACoS is the business metric.** ACoS = ad spend / ad-attributed sales (optimize bids); TACoS = total ad spend / total sales incl. organic (steer budget and strategy). Never steer the business on ACoS alone (pcostudio; ainfluencer; Keywords.am). FRAMEWORK, T1.
- **Break-even ACoS = contribution margin %** — compute per ASIN, set stage targets from it: launch at/above break-even (buy rank), growth below break-even minus buffer, harvest well below (Zagare-consistent; EcomCalcTools; Pathfinder 9% ACoS case). HEURISTIC, T2.
- **Bidding: placement modifiers apply first, dynamic bidding compounds second** — a 900% ToS modifier + up-and-down can turn a $1 bid into $20; most sellers misjudge effective CPC (AMALYZE cascade). Up-and-down only on proven exact terms with 30+ days data; fixed for branded campaigns; down-only as the conservative default (SalesDuo; AMALYZE). EMPIRICAL/HEURISTIC, T2.
- **Amazon attribution is deterministic-but-inflated**: ad-attributed sales credit every purchase that touched an ad; NTB (new-to-brand) measures genuinely new customers; halo = organic-rank lift and cross-SKU sales never shown in the console. "When a branded campaign's ROAS looks great, distrust it" — bottom-funnel branded looks heroic while upper-funnel that grows the business gets starved (SellerStack). EMPIRICAL (mechanism), T1/T2.
- **DSP is an upper-funnel/retargeting layer, not a second PPC tool** — it makes search more efficient via a flywheel (DSP awareness → search capture → search data improves DSP audiences); premature below ~$50k/month sponsored spend with inconsistent profitability (Darkroom). HEURISTIC, T2.
- **Amazon enforcement is a business risk, not just a compliance footnote**: review-velocity flags can suspend legitimate launches; packaging inserts (even manufacturer-added) trigger review-manipulation suspensions; appeals win on documented proportionality (SellerSprite 2026 cases; Cabilly; McCabe's "think like Amazon"). EMPIRICAL, T2.
- **Marketplace economics have compressed**: 2025 saw the fewest new Amazon sellers in a decade (165k, −44%); Amazon is now ~60% services/40% retail; ads evolved "from optional to unavoidable"; new seller entry is a capital game (Marketplace Pulse 2025 Year in Review). EMPIRICAL, T1.

## Disagreement
1. **Negate vs lower bid on junk search terms.** Zahradnik (2020 QA podcast): some operators never negative, they lower bids; Zahradnik's agency stance favors disciplined negatives (negative products on auto was a big change); community r/AmazonFBA warns negating *retargeting* audiences kills the only lever that converts. Condition: term volume and whether the term is a category-relevant browse term vs exact junk.
2. **Auto-bidding trust.** Amazon's automated bidding (up-and-down + dynamic) drained spend in community reports ("127% ACoS on Amazon's automated bidding rules — worst placements", r/FulfillmentByAmazon 2026) vs agency claims that dynamic up-and-down scales proven campaigns. Condition: campaign maturity and margin headroom; community evidence says default automation on immature campaigns is a trap.
3. **SP/SB/SD split strictness.** Keywords.am's stage matrix (80/15/5 → 50/25/15/10) vs older "SP-only until 30–60 days" minimalism vs "SB for brand defense early" (Zagare's customer-buying-cycle/brand-halo budgeting). Condition: brand recognition and competitor behavior; when competitors bid your brand terms, SB defense is urgent regardless of stage (Keywords.am; Zagare).
4. **ACoS targets by category.** Benchmarks vary wildly by source (supplements 20–35% vs electronics 15–22% — Keywords.am; ainfluencer table ranges 10–40% ACoS / 5–30% TACoS by category). Condition: category + margin; everyone agrees the only true anchor is your own break-even, benchmarks are sanity checks. T3 for specific numbers.
5. **When DSP becomes viable** — Darkroom's $50k/month sponsored threshold vs Pathfinder's DSP-first clients at smaller scale (Viter Energy case) vs "DSP only after organic share stabilizes" (seller-community consensus). Condition: whether you have the measurement (AMC) and creative to make DSP learn; threshold is a heuristic, not physics.

## Conditions
- **Harvesting/rank-buying PPC works when**: listing converts at category parity (reviews, price, images); you can tolerate break-even ACoS for 8–12 weeks; keyword volume supports it (Zagare: high-volume keywords get single-keyword campaigns; group 5–10 mid; 10–15 max per campaign).
- **Stage splits apply when**: launch = SP-heavy discovery; growth = SB/SD enter as branded search volume and remarketing pool appear (SD viable after ~1,000+ remarketing impressions); mature = brand defense + DSP (Keywords.am).
- **TACoS decline as the growth signal applies when**: you have organic rank data; TACoS should fall 8–12 weeks post-launch as organic share rises; ACoS rising while TACoS falls = healthy launch, not a problem (pcostudio scenarios).
- **Incrementality layer (AMC, holdouts) applies when**: spend is meaningful enough to fund dark control groups — mostly upper-funnel DSP, "where they're not betting the quarter on it" (SellerStack).
- **Marketplace entry gates**: capital reserves to absorb fee increases/tariffs, 1–2 marketplaces max at a time, per-marketplace landed-margin model before entry (marketplace-expansion skill; Marketplace Pulse consolidation data).

## Evidence evaluation
- EMPIRICAL (strong): Marketplace Pulse seller/GMV data; Amazon's mechanics (placement × dynamic compounding — AMALYZE); review-enforcement cases (SellerSprite, Cabilly — attorney/consultant documented cases); Instacart's published incrementality methodology.
- EMPIRICAL but vendor-sourced: 60/30/10 splits, ACoS-by-category tables, $50k DSP threshold, "127% ACoS" community case — consistent across vendors but each sells tools (T2/T3).
- HEURISTIC: break-even ACoS framing (universal), stage targets, negate-vs-bid, seesaw technique (lower base bid + raise ToS multiplier).
- OPINION: "ACoS is dead" hot takes; DSP-only growth paths.
- Gaps: no RCT-grade evidence on splits; Amazon changes UI/defaults frequently (SD off-Amazon opt-in default; auto-bid defaults) so 2020-2022 advice needs re-validation (UNVERIFIED recency risk).

## Outliers (worth investigating)
- **"Great Compression" as entry-gate data** — fewer sellers + record GMV concentration means paid acquisition is now table stakes; the Collision OS should treat Amazon entry as a capital-requiring channel, not a test channel (Marketplace Pulse).
- **Seesaw bidding** (lower base, raise ToS multiplier) as a budget-concentration technique (SalesDuo).
- **Off-Amazon placements silently enabled** (community complaint) — a default-settings audit is cheap and high-value.
- **NTB as the bridge metric** between Amazon and web: SB campaigns reported 88% NTB orders in one Pathfinder client case — NTB is the closest Amazon gets to web-style acquisition measurement.

## Failure knowledge (what repeatedly doesn't work)
- **Optimizing every keyword to one ACoS** regardless of margin/stage (existing skill; universal).
- **Pausing profitable high-reach keywords to lower ACoS** — campaign looks better, business shrinks (pcostudio). ACoS-only steering.
- **Judging launches by ACoS** and pulling PPC prematurely at week 4–6 (ainfluencer; Zahradnik QA podcast: 4-month-old brand at <90% ACoS wanting to "grow fast" — the answer is stage targets, not panic).
- **Trusting dynamic up-and-down on unproven campaigns** — automation spends into the worst placements (r/FBA "127% ACoS" thread).
- **Ignoring the placement×dynamic compounding math** — effective CPC surprises kill margin (AMALYZE).
- **Fake reviews / review inserts / review swapping** — instant or near-instant suspension; Amazon tracks account relationships, shared IPs/payments; funds frozen ($28k case) (SellerSprite; Cabilly; McCabe).
- **Thin-listing myth**: AI-copied thin listings *can* win with aggressive pricing (community thread) — but thin listings without price advantage die; review depth at parity is the durable moat.
- **Scaling spend before listing conversion proven** (universal).
- **Judging DSP on direct ROAS** (universal).
- **Rank manipulation / inflated ranking services** — detected via velocity patterns; documented proportionality is the only defense (SellerSprite).

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
