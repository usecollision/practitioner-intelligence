---
practitioner: CTV panel (measurement vendors + DSPs + platform)
role: incrementality vendors, media measurement, DSP/self-serve platform
company: Measured; WorkMagic; Prescient AI; Simulmedia; Paramount; StackAdapt
type: analyst|vendor|insider
confidence: T2
domains:
  - paid
verified: 2026-08-15
sources_checked: 9
---
# Panel — Programmatic CTV

## Experts found
- **Measured** (incrementality vendor, Aug 2025 report) — CTV campaigns over-reported incremental conversions by up to 5x in some cases and under-reported by up to 10x in others; CTV delivers strong iROAS despite minimal enterprise spend share (T2, EMPIRICAL).
- **WorkMagic** (incrementality platform; Branch/Tatari case) — geo test: CTV drove 4.18% incremental lift in Shopify orders = 20x what last-click reported; 1.46x iROAS incl. Amazon; 86% of CTV-driven orders from new customers; personal-care client: 95% of CTV impact occurred OUTSIDE Shopify (Amazon/retail) (T2, EMPIRICAL).
- **Prescient AI** — CTV sits at top of funnel "almost by definition"; click-based measurement structurally unsuited; halo lands in branded search/organic/direct/retail; MMM is the only single method capturing all downstream effects; geo incrementality measures a campaign in isolation (T2, FRAMEWORK).
- **Simulmedia** — incremental lift studies > MTA and MMM for validation; ghost bids/synthetic groups as advanced options (T2).
- **Paramount Ads Manager** (self-serve CTV seller) — pragmatic: start simple (surveys, campaign-window shifts, business benchmarks), "attribution is a spectrum, not a switch" (T2, seller-side).
- **StackAdapt** (DSP) — identity graph limits; footfall attribution as emerging offline bridge (T3, vendor).

## Beliefs
- **CTV is a no-click, lean-back medium**: no cookie/device-id path; household identity graphs, QR, promo codes, vanity URLs, surveys are all imperfect bridges (WorkMagic/ExchangeWire, CONSENSUS).
- **Platform/view-through self-attribution is unreliable in BOTH directions** (5x over to 10x under) — the single most cited measurement fact (Measured, EMPIRICAL).
- **Most CTV impact is invisible to DTC-only measurement** — 95% outside Shopify in one branded test; halo in Amazon/retail/branded search (WorkMagic/Prescient, EMPIRICAL).
- **Geo-based incrementality (matched markets, 3–4 week dark control) is the gold standard for campaign-level truth**; MMM for full-mix; both, not either (WorkMagic/Simulmedia/Prescient, CONSENSUS).
- **CTV's job is new-customer acquisition + halo** — 86% of CTV-driven orders from new customers (WorkMagic, EMPIRICAL); consistent with Binet/Sharp brand-reach findings in paid-strategy.md.
- Performance-marketing expectation mismatch: "CTV stepped into that world carrying all the weight of a traditional awareness channel while being held to digital-era accountability standards" (Prescient, OPINION).
- DSP choice matters less than measurement choice; platform-native tools can't run controlled lift tests — they only see their own channel (WorkMagic).

## Failure modes
- Judging CTV on view-through/last-click ROAS (5x over-report and 10x under-report both documented).
- DTC-only measurement — misses Amazon/retail halo.
- No matched control: confounded geo "tests" (see paid-strategy.md Metricuno warning).
- Expecting click-path accountability from a lean-back medium.
- Underfunded flight below measurement power.
- Killing CTV after one campaign window without halo measurement (branded search lag).

## Decision rules
1. IF spending on CTV THEN measure with geo-based incrementality (matched markets, 3–4 week dark control) or MMM — never platform ROAS alone (Measured/WorkMagic/Prescient, EMPIRICAL, T2).
2. IF CTV dashboard ROAS looks bad THEN check halo channels (branded search, direct, Amazon/retail) before cutting (WorkMagic/Prescient, EMPIRICAL, T2).
3. IF objective is new-customer acquisition or brand reach THEN CTV qualifies; IF pure last-click DR THEN it will look like a failure (WorkMagic/Prescient, EMPIRICAL, T2).
4. IF budget < enough for a powered geo test THEN treat CTV as brand spend with brand metrics (search lift, surveys), not performance (synthesis, HEURISTIC, T3).
5. IF running CTV + other channels THEN expect overlap/assist credit issues; apply incrementality-adjusted attribution (WorkMagic, FRAMEWORK, T2).
6. IF choosing a DSP THEN require suppression/geo capabilities for holdouts; otherwise incrementality is impossible (WorkMagic, HEURISTIC, T2).

## Sources
1. Measured, CTV incremental ROAS report (Aug 2025) | measured.com/press | tier 2 | 2026-08-15
2. BusinessWire, Measured CTV data (5x/10x over/under-report) | businesswire.com | tier 2 | 2026-08-15
3. WorkMagic, How to measure connected TV + Branch/Tatari case | workmagic.io | tier 2 | 2026-08-15
4. Prescient AI, How to measure CTV effectively | prescientai.com | tier 2 | 2026-08-15
5. Simulmedia, Measure incremental lift in CTV | simulmedia.com | tier 2 | 2026-08-15
6. Paramount Ads Manager, CTV attribution "keep it simple" | adsmanager.paramount.com | tier 2 | 2026-08-15
7. ExchangeWire, CTV measurement challenges | exchangewire.com | tier 2 | 2026-08-15
