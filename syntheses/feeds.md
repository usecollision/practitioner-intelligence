# SYNTHESIS — Shopping Feeds (Google Merchant Center, Shopping & PMax)

Practitioners/panel: Elite Brands agency (disapproval triage), AdTribes (WooCommerce feed tool vendor, diagnostics), GetFeeder (feed tool vendor, error taxonomy), Shoparize (CSS partner), MBA Digital Ventures agency (feed debugging), Shopify community field reports, Google Merchant Center docs (via these sources). Note: shopping feeds have no single celebrity practitioner — this is a panel-built synthesis (operator + agency + tool vendors + community). Verified 2026-08-15.

## Consensus
- **The feed is the ad.** Feed quality determines Shopping/PMax eligibility, matching, and CTR; weak feed data = weak PMax performance (existing shopping-feeds skill; MBA Digital; GetFeeder). FRAMEWORK, T1.
- **Diagnostics triage is top-down: account-level → feed-level → item-level**; within item-level: errors (disapproved, won't show) → warnings (shows but performance suffers) → notifications (informational). A "wall of issues" becomes a short prioritized list (AdTribes). HEURISTIC, T2.
- **80/20 prioritization**: ~80% of account issues are warnings/limited-performance flags on non-core products; the damage is the ~20% hard disapprovals on the products that make money. Prioritize by (severity × revenue impact) (Elite Brands). HEURISTIC, T2.
- **Account-suspension warnings are all-hands emergencies** — yellow/red bar at top of Merchant Center; address root cause immediately; it's the whole advertising operation at risk, not one product (Elite Brands). T1.
- **Fix at source, then re-fetch** — patching inside Merchant Center (or feed rules) leaves the store broken; fixes evaporate on next fetch (existing skill; AdTribes: "fix at source"). T1.
- **Data-quality issues are the fastest wins** — missing attributes, formatting, simple policy fixes resolve in hours and get fast re-approval (Shoparize). T2.
- **Price/availability mismatch between feed and landing page is the most common account-level health issue** — silent damage, account-level warnings (existing skill; Shopify community reports). T2.
- **GTIN/MPN mismatches and category-taxonomy errors are top disapproval causes** — fix at catalog level; generic/mismatched google_product_category mapping spikes disapprovals (existing skill; Shopify community thread). T2.
- **Promotional language belongs in the promotions feed, not titles/descriptions** (GetFeeder). T1 (policy).
- **Technical feed errors are mechanical**: malformed XML, missing units on shipping_weight (must be "1.5 kg"/"3 lb"), >4GB compressed feed limit (GetFeeder). FACT, T1.

## Disagreement
1. **How aggressively to clear warnings vs errors** — AdTribes: work top-down, errors first; Elite Brands: 80% of issues are warnings you can safely deprioritize if they're on non-core SKUs. Condition: account health headroom; if the account is near suspension thresholds, warnings matter more.
2. **Feed rules vs source-of-truth purity** — existing skill warns rules accumulate and obscure the source of truth; tool vendors (Feedonomics/DataFeedWatch via MBA Digital) sell rule-based transformation as the standard for large catalogs. Condition: catalog size and engineering capacity; rules are a scaling tool, but document owners and audit quarterly.
3. **Title optimization ceiling** — front-loading keywords is universal, but how much to optimize depends on channel: PMax title weighting vs Shopping CTR; hero-SKU hand-tuning vs rule-based generation for long-tail (existing skill). Condition: catalog size, hero SKU revenue share.
4. **When to use supplement feeds vs primary-feed fixes** — supplement feeds for overlays (promotions, labels, seasonal) are universal; disagreement is whether they mask root-cause problems (price/availability) — treat supplement feeds as temporary until primary is fixed (existing skill + AdTribes logic).
5. **PMax blame allocation** — when PMax underperforms, feed-first triage (existing skill) vs bid/asset optimization first (Google's own guidance emphasizes assets). Condition: diagnostics clean? If feed is clean, move to assets/audience; if dirty, feed first.

## Conditions
- **Feed-first triage applies when**: diagnostics show item-level errors/warnings on core SKUs; when ROAS dips and the feed is clean, the problem is bids/assets (existing skill).
- **Rule-based title generation applies when**: catalog > ~1,000 SKUs or no dedicated feed engineer; hero SKUs (<20% of catalog generating most revenue) still get hand-tuning.
- **Supplement feeds apply when**: you need to overlay promotions/custom labels/seasonal data without rebuilding the primary pipeline; never as the permanent home for price/availability fixes.
- **Multi-country feeds apply when**: currency/language/availability differ per target country.
- **The 80/20 triage applies when**: account is not already under suspension threat; if suspension warning is present, ALL issues become urgent.

## Evidence evaluation
- FACT: Google's error taxonomy (errors/warnings/notifications; account/feed/item levels; 4GB limit; units requirement; policy on promo language) — from multiple independent vendor sources consistent with each other and with Google docs.
- EMPIRICAL but vendor-sourced: 80/20 distribution claim (Elite Brands — agency audit experience); "data-quality fixes resolve in hours" (Shoparize); common-error rankings (AdTribes, GetFeeder) — consistent across vendors.
- HEURISTIC: feed-first triage, title front-loading, rule hygiene.
- Gaps: no public quantification of feed-error impact on ROAS; PMax's exact title/feed weighting is unpublished (Google black box) — UNVERIFIED; 2026 spec changes (MBA Digital mentions "2025 spec changes") need re-validation.

## Outliers (worth investigating)
- **"All products disapproved despite valid feed"** pattern (WordPress/WooCommerce community reports) — usually an account-level or taxonomy-level change, not per-item; check account settings before item-level debugging.
- **Category mapping as a silent disapproval multiplier** (Shopify community) — one wrong taxonomy mapping can spike disapprovals across hundreds of SKUs; audit google_product_category mapping before per-item fixes.
- **Feed tools as error-alerting infrastructure** (Feedonomics, DataFeedWatch, AdTribes) — alerting before disapproval beats post-hoc cleanup (MBA Digital).

## Failure knowledge (what repeatedly doesn't work)
- **Editing in Merchant Center instead of the store** — fixes evaporate on next fetch (existing skill; AdTribes).
- **Price/availability mismatches** — silent account-level damage, top recurring issue (existing skill).
- **Keyword-stuffed, promo-laden titles** — spam-like titles hurt CTR and can trigger policy issues (existing skill; GetFeeder).
- **Ignoring GTIN/MPN** — top disapproval cause, easy catalog-level fix (existing skill).
- **No custom labels** — PMax/Shopping run blind without margin/promo structure (existing skill).
- **Letting feed rules accumulate** — a web of rules nobody can untangle; obscures source of truth (existing skill).
- **Treating feed quality as one-time setup** — decays with every catalog change (existing skill).
- **Debugging item-level errors first when the cause is account-level** — wasted hours; go top-down (AdTribes).
- **Ignoring account-suspension warnings while fixing individual products** — the account dies while you polish items (Elite Brands).
- **Unpaced/undocumented multi-country feeds** — currency/language mismatches cascade (existing skill).

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
