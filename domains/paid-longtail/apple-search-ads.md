---
practitioner: Apple Search Ads panel (mobile growth operators + platform)
role: UA/monetization platform, ASA agencies, ASO specialists
company: Adapty (Victoria Kharlan); SearchAdsMaven; SEM Nexus; ASO Mobile; Admiral Media; SplitMetrics/AppRadar
type: operator|agency|insider
confidence: T2
domains:
  - paid
verified: 2026-08-15
sources_checked: 9
---
# Panel — Apple Search Ads (ASA / Apple Ads)

## Experts found
- **Adapty** (subscription monetization platform; Victoria Kharlan) — 2026 mechanics: renamed Apple Ads Apr 2025; Basic = CPI + one placement + Apple-managed; Advanced = CPT + target CPA, all 4 placements, manual/auto bidding; "neither version reports what happens after the download" (T2; platform-adjacent insider).
- **Adapty best-practices piece** — "Always work in Advanced mode. Every profitable campaign I've analyzed uses Advanced mode exclusively"; conventional "start broad, let Apple learn" wastes money; broad match burns budget (T2, OPINION/EMPIRICAL).
- **SearchAdsMaven** (ASA agency) — discovery campaign technique: high CPT + low CPA target to test lazy keywords; bid on many keywords to diversify risk (T2).
- **SEM Nexus** — 50–150 keywords at stage 1–2 (300+ for large); competitor bidding selectively (top 1–3 defensive only); automated rules as guardrails not primary (T2).
- **ASO Mobile** — TTR/CR/CPT/CPA causal chain; relevance as eligibility filter (weak page raises real CPT); campaign separation (Discovery/Brand/Competitor/General); organic uplift; cross-campaign negatives (T2).
- **Admiral Media** — $5–10k/month minimum for meaningful optimization; starts workable at $1k (T3).
- **SplitMetrics/AppRadar (Gabriel Kuriata)** — Advanced is the only reasonable choice above ~$10k/month; Basic acceptable for low-spend default-page apps (T2).

## Beliefs
- **Intent profile is the strongest in paid media** (explicit App Store search) — but the funnel ends at install; post-install revenue is invisible to Apple (Adapty, CONSENSUS).
- **The Basic trap**: Basic reports downloads only; budget decisions on download counts pause your best-subscriber keywords and scale duds — connect revenue attribution (Adapty, EMPIRICAL/HEURISTIC).
- **Keyword-level truth is the asset**: TTR measures ad-query match, CR measures page quality, CPA = CPT/CR; ASA is the only place with direct query→behavior link, usable for ASO (ASO Mobile, FRAMEWORK).
- **Auction is opaque**: second-price; "harder to tell how it works backstage" vs Google/Facebook algorithms (Moburst, OPINION).
- **Structure by campaign type** (Discovery/Brand/Competitor/General) with negatives across campaigns to stop self-competition (ASO Mobile, FRAMEWORK).
- **Organic uplift**: ASA drives organic installs indirectly (ranking via install velocity); evaluating only by CPA misses it; reduce bids when organic rankings climb on a keyword (ASO Mobile, HEURISTIC).
- Abandonment is a top failure: "You gave Apple Ads two weeks, called it broken, then watched competitors dominate your keywords for months" (Adapty).

## Failure modes
- Running ASA on a weak product page — budget burns, data unreliable (ASO Mobile).
- Broad-match-heavy "let Apple learn" setups — irrelevant traffic (Adapty).
- Judging by CPA/CPI without revenue attribution (Adapty).
- Brand/competitor keywords competing within the same account without negatives (ASO Mobile).
- Overbidding competitor brands beyond top 1–3 — high CPI, mediocre conversion (SEM Nexus).
- Quitting inside the learning period (Adapty).
- Ignoring TTR (ad-query mismatch) and CR (page quality) when costs rise.

## Decision rules
1. IF app has subscription/in-app revenue AND budget >$10k/mo THEN run Advanced only, with revenue-attribution (MMP/SKAdNetwork) — never Basic for optimization (Adapty/AppRadar, HEURISTIC, T2).
2. IF judging keywords THEN evaluate CPT→TTR→CR→CPA per keyword, then cohort revenue, never install count alone (ASO Mobile/Adapty, FRAMEWORK, T2).
3. IF building the account THEN separate Discovery/Brand/Competitor/General campaigns and add cross-campaign negatives (ASO Mobile, FRAMEWORK, T2).
4. IF bidding on competitors THEN cap at top 1–3, defensive posture (SEM Nexus, HEURISTIC, T2).
5. IF organic ranking on a keyword is climbing THEN cut the paid bid on it (ASO Mobile, HEURISTIC, T2).
6. IF a keyword underperforms THEN run a discovery test (high CPT + low CPA target) before killing it (SearchAdsMaven, HEURISTIC, T2).
7. IF launch-stage with tiny budget THEN Basic as a placeholder is acceptable — but connect revenue attribution before scaling decisions (Adapty/AppRadar, HEURISTIC, T2).

## Sources
1. Adapty, Apple Search Ads 2026: cost, placements, bidding | adapty.io/blog | tier 2 | 2026-08-15
2. Adapty, Apple Ads best practices (Advanced-only) | adapty.io/blog/apple-ads-best-practices | tier 2 | 2026-08-15
3. SearchAdsMaven, Five mistakes on Apple Search Ads | searchadsmaven.com | tier 2 | 2026-08-15
4. SEM Nexus, ASA keyword bidding strategy | semnexus.com | tier 2 | 2026-08-15
5. ASO Mobile, Apple Search Ads and ASO | asomobile.net | tier 2 | 2026-08-15
6. AppRadar/SplitMetrics, ASA Advanced guide | appradar.com | tier 2 | 2026-08-15
7. Admiral Media, ASA benchmarks | admiral.media | tier 3 | 2026-08-15
