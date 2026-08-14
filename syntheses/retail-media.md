# SYNTHESIS — Retail Media (Amazon DSP, Walmart Connect, Instacart)

Practitioners/panel: Brent Zahradnik (AMZ Pathfinder/SellerPlex — DSP), Darkroom Agency (Amazon & retail media practice), Perpetua (Instacart/Walmart/Amazon tool vendor + agency), Instacart engineering (incrementality methodology), Walmart Connect resources/case studies, Feedvisor (Walmart Connect agency), Eva Commerce (Walmart Connect agency guide), SellerStack (AMC/incrementality), Pattern (halo). Verified 2026-08-15.

## Consensus
- **Retail media's pitch is closed-loop measurement + first-party purchase data, not reach** — deterministic attribution (ad view/click → purchase) is the differentiator vs open web (Instacart; Walmart Connect; Amazon DSP). FRAMEWORK, T1.
- **On-site sponsored placements are the performance layer; off-site (DSP, offsite media) is the brand/upper-funnel layer — never run one with the other's expectations** (Darkroom; Walmart Connect's own small-business vs enterprise solution split; existing retail-media skill). HEURISTIC, T1.
- **The flywheel**: DSP builds awareness → search captures demand → search data informs more efficient DSP audiences; "DSP is the upper-funnel and retargeting layer that makes search campaigns more efficient", not a replacement for SP/SB (Darkroom). FRAMEWORK, T2.
- **Incrementality is the only truth layer**: platform ROAS credits purchases that would have happened anyway; on-site sponsored ads on your own branded terms can just tax organic sales (SellerStack; existing skill; Instacart's published 3-level incrementality methodology: advertiser, system, experiment). EMPIRICAL (mechanism), T1.
- **Holdout-based tests belong on upper-funnel spend** (DSP/OTT), where "you're not betting the quarter on it"; brands rarely stomach going dark on search (SellerStack). HEURISTIC, T2.
- **New-to-brand (NTB) is the key CPG acquisition metric**; SB/DSP campaigns can report very high NTB (88% NTB attributed orders in one AMZ Pathfinder SB client case). EMPIRICAL (case), T2.
- **Start where the shopper is; one network done well beats three done thinly** — minimums, fee layers (platform + managed service), and learning curves are real (existing skill; Eva Commerce; Perpetua). HEURISTIC, T2.
- **Never advertise out-of-stock SKUs** — retail media amplifies supply problems (existing skill; universal). T1.
- **Trade coordination is structural**: retail media budgets often come from trade marketing, and JBP with the retailer unlocks credits/placement/data (existing skill; Walmart Connect partner model). HEURISTIC, T2.

## Disagreement
1. **DSP entry threshold**: Darkroom says <$50k/month sponsored spend with inconsistent profitability = DSP premature; agencies that sell DSP (Pathfinder, Sequence) show DSP case studies at smaller scales (Viter Energy). Condition: whether AMC measurement + creative exist; treat threshold as heuristic. T3 for the number.
2. **Instacart maturity**: Perpetua (2021) called Instacart "less expensive than mature marketplaces" with room to grow; by 2024-2026 retail media consolidation and higher CPCs are widely reported (UNVERIFIED specific numbers; Adverity notes measurement difficulty). Condition: category and whether you're vendor (retailer-owned data) vs marketplace seller.
3. **On-site cannibalization severity**: some agencies treat on-site sponsored as purely incremental (search placement wins vs competitors); SellerStack/paid-strategy synthesis warn branded-term on-site ads largely displace organic (test the difference; existing skill). Condition: share of voice you already own organically.
4. **Closed-loop vs MMM attribution of in-store halo**: Walmart Connect sells omnichannel store+online attribution; most brands can't verify store halo claims without retailer data access (Feedvisor vendor survey self-reports 7x ROAS — tier 3, treat as directional). Condition: data access through retailer partnership.
5. **Segment trust**: retailer-defined audiences (lapsed buyers, category buyers) are refreshed on retailer schedules and definitions are opaque — ask how segments are built before trusting them (existing skill; Eva Commerce advises multivariate testing with Walmart data). Condition: retailer relationship depth.

## Conditions
- **Retail media fits when**: product is actually sold at the retailer (CPG/consumables strongest), first-party purchase data is the differentiator, and you can measure beyond dashboard ROAS (existing skill; Adverity: CPG wholesale data is retailer-owned, so retail media is often the *only* clean data source).
- **DSP makes sense when**: search infrastructure is solid (ads convert), catalog is mature, spend ≥ ~$50k/month sponsored, NTB growth is a priority, and AMC/holdout measurement is available (Darkroom; SellerStack; existing skill).
- **Walmart Connect fits when**: you have Walmart Marketplace or vendor presence, price-competitive catalog (Walmart's EDLP promise), WFS or fast shipping for two-day badges, and omnichannel (store+online) story matters (Eva Commerce; Walmart Connect resources).
- **Instacart fits when**: grocery/CPG with retail partner listings; note 14-day attribution window for sponsored products (weekly cart filling → checkout), automatic serving into new stores (budget pacing required) (Perpetua).
- **Incrementality tests apply when**: upper-funnel budget exists to fund dark control; otherwise use AMC analyses and NTB trends.

## Evidence evaluation
- EMPIRICAL (strong): Instacart's published incrementality methodology (3 levels, ongoing measurement); Amazon's attribution mechanics (SellerStack, Pattern); halo elements list (Pattern: out-of-window sales, cart adds, wishlists, retargeting, BSR lift, branded-search defense, off-Amazon price-check sales).
- EMPIRICAL but vendor/self-reported: 88% NTB case (Pathfinder), 7x ROAS survey (Feedvisor 2022, Zogby-conducted, n=1,000+ — but commissioned by a vendor), Walmart case studies (+60% sales Mr.Brands).
- HEURISTIC: $50k DSP threshold, one-network-at-a-time, continuous flighting over bursty, on-site weekly / off-site monthly optimization cadence.
- Gaps: no public RCT-grade proof of retail media incrementality at brand level (Instacart publishes methodology, not results); in-store halo quantification requires retailer data (UNVERIFIED for most brands); DSP benchmarks (CPM, CTR, NTB%) are agency-held and not public.

## Outliers (worth investigating)
- **Retail media as the cure for CPG data blindness** — when retailers own sales data, retail media dashboards may be the most complete view a brand has (Adverity) — an argument for spending on data access, not just sales.
- **AMC's 5-year purchase-signal lookback** (2025-2026) enables upper-funnel → downstream incrementality analysis at fidelity web platforms can't match (SellerStack).
- **Store-level targeting granularity on Instacart** (geography/regions/stores) — ads auto-serve into new stores; spend spikes without pacing (Perpetua).
- **Caper Carts / AI discovery placements** as emerging Instacart inventory beyond sponsored products (Sequence).

## Failure knowledge (what repeatedly doesn't work)
- **Judging retail media on platform ROAS alone** — baseline sales inflate the read; branded on-site ads tax organic (existing skill; SellerStack).
- **Running off-site brand campaigns with on-site performance expectations** (existing skill; Darkroom's "not a quick-win channel").
- **Advertising out-of-stock SKUs** (universal).
- **No incrementality or holdout design** — the entire measurement story is missing (existing skill).
- **Buying audiences without asking how segments are built/refreshed** (existing skill).
- **DSP without search infrastructure** — DSP traffic has nowhere to convert; "not a self-service platform where novices deploy capital" (Darkroom).
- **Bursty flighting** — continuous flighting beats bursty dips for retail data learning (existing skill).
- **Ignoring the trade team** — retail media lives inside retailer relationships; JBP unlocks credits (existing skill; Walmart Connect partner model).
- **Unpaced Instacart budgets** — auto-serving into new stores causes unexpected spend spikes (Perpetua).

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
