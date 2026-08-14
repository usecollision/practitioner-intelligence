# SKILL GAP ANALYSIS — Amazon Ads, Retail Media, Shopping Feeds & Marketplace Expansion (Wave A1, 2026-08-15)

Research: `syntheses/amazon.md`, `syntheses/retail-media.md`, `syntheses/feeds.md` · Domains: `domains/amazon/*` (zagare, mccabe, zahradnik, panel-note) · Status: **implemented**

## What the audit found

| Skill | Audit maturity | Core gap |
|---|---|---|
| amazon-ads | M2 | No quantitative budget-split or bidding decision rules (stage splits, placement×dynamic compounding); ACoS/TACoS steering logic implicit; no attribution/NTB/halo layer; no compliance-risk guardrails; no sources |
| retail-media | M2 | No DSP go/no-go threshold; incrementality/measurement logic present but unquantified; no NTB targets; no network-specific mechanics (Instacart 14-day window, auto-serving); no sources |
| shopping-feeds | M2 | Diagnostics triage (account→feed→item) and 80/20 prioritization missing; error taxonomy vague; no suspension-warning emergency rule; no sources |
| marketplace-expansion | M2 | No capital-gate for entry (Great Compression data); compliance risk (review inserts, suspensions) absent; no break-even timeline rule; no sources |

## Gaps found → changes made

1. **No stage-based budget split rules** → amazon-ads now carries the 60/30/10 baseline + lifecycle matrix (launch 80/15/5 → mature 50/25/15/10-DSP → brand-under-attack 40/35/25) as executable IF/THEN rules (Keywords.am; HEURISTIC, T2).
2. **Bidding rules were generic** → added placement-modifier-first / dynamic-bidding-second compounding math (AMALYZE), up-and-down-only-on-proven-exact-terms (SalesDuo), 30-day data minimum, 14-day post-switch evaluation.
3. **ACoS/TACoS misuse not flagged** → added the three-scenario framework (ACoS up/TACoS down = healthy launch; pausing high-reach keywords to cut ACoS = shrinking business) as decision rules + failure modes (pcostudio).
4. **Attribution layer absent** → added NTB% and halo (organic-rank lift, cross-SKU) as guardrail metrics; "distrust great branded ROAS" rule (SellerStack; Pattern).
5. **DSP go/no-go unquantified** → added ~$50k/month sponsored-spend threshold + AMC/holdout measurement requirement (Darkroom); NTB-priority rule for acquisition (Zahradnik/Pathfinder).
6. **Feed triage missing** → shopping-feeds now has top-down triage (account→feed→item; errors→warnings→notifications), 80/20 revenue-weighted prioritization, suspension-warning emergency rule, and mechanical error fixes (units, XML, 4GB, promo-language-in-promotions-feed) (AdTribes; Elite Brands; GetFeeder).
7. **Marketplace entry had no capital gate** → added Great Compression data (165k new sellers −44%, 60/40 services/retail, ads "optional→unavoidable") as entry-condition evidence; landed-margin + 2-quarter break-even kill rule; compliance-risk rule from McCabe/SellerSprite (review inserts suspend accounts with funds frozen).
8. **No sources anywhere** → all 4 skills now carry Practitioner Grounding (8/7/7/5 attributions) + Sources sections (12/11/8/9 entries) with tiers and access dates; every rule resolves to a synthesis or dossier.

## Left for later (documented, not blocked)

- Category ACoS/TACoS benchmark tables conflict across vendors (ainfluencer vs Keywords.am) — encoded as T3; break-even math is the truth anchor.
- Zagare/Zahradnik 2020-2021 content pre-dates current AI-bidding defaults — re-validate bid-strategy rules when Amazon changes defaults (recency risk, UNVERIFIED).
- Feed-error → ROAS impact quantification is unpublished (UNVERIFIED) — triage rules rest on agency consensus.
- Instacart/Walmart Connect fee minimums change frequently — pull current schedules at use time (existing skill convention).
- DSP mid-market counterexamples (Pathfinder Viter Energy) vs Darkroom $50k threshold — encoded as conditional disagreement, not fact.

## Validation

- [x] SKILL-TEMPLATE structure intact (frontmatter, gates) — verified via patch diffs
- [x] Every decision rule tagged claim-type + confidence (T1/T2/T3)
- [x] Sources resolve to research files in practitioner-intelligence (syntheses/amazon.md, retail-media.md, feeds.md; domains/amazon/*)
- [x] Cross-repo: amazon-ads ↔ retail-media ↔ marketplace-expansion ↔ shopping-feeds cross-links present; retail-media references paid-strategy synthesis (incrementality)
- [x] Not committed/pushed per wave instructions (parent agent handles commits)
- [ ] validate-tools.py + check-integrity.py (marketing-core) — to run by parent at commit time
