# SKILL GAPS — GTM / Pricing / Analytics / Competitive / DTC (Wave 4b)

Wave 4b upgrade record. Research + implementation completed 2026-08-15.

## What changed

| Skill | Repo | Upgrade |
|---|---|---|
| growth-strategy | marketing-intelligence | M4: 7 decision rules (PMF gate, loops, retention, motion selection) + Metrics + Sources |
| gtm-plan | marketing-intelligence | M4: 6 decision rules (first-10-customers, PMF gate, motion, capture-vs-creation, budget focus) + Metrics + Sources |
| pricing-packaging-strategy | marketing-intelligence | M4: 8 decision rules (WTP survey, GBB, usage/hybrid, 4 failure patterns, discounting, A/B-test avoidance) + Metrics + Sources |
| competitor-audit | marketing-intelligence | M4: 7 decision rules (win-deals goal, alternatives, phantom competitors, status quo, scoring rigor, win rate) + Metrics + Sources |
| metrics-framework | marketing-optimize | M4: 7 decision rules (vanity test, proxy thresholds, NSM inputs, targets) + Metrics + Sources |
| analytics-setup | marketing-optimize | M4: 6 decision rules (GA4 setup checklist, retention window, attribution choice) + Metrics + Sources |
| dashboard-design | marketing-optimize | M4: 7 decision rules (KPI-only, ~6 per exec, 3σ outliers, vanity flags) + Metrics + Sources |
| shopify-marketing-audit | marketing-paid | M4: 8 decision rules (margin gate, MER, organic-first, milestones, CPM/CTR diagnosis, repeat rate) + Metrics + Sources |

All patches: inserted `## Practitioner Grounding & Decision Rules` + `## Metrics` + `## Sources` before the existing `## Evaluation & QA` anchor. Each addition is 30-50 lines, every claim tagged (FACT/EMPIRICAL/HEURISTIC/FRAMEWORK/OPINION/TACTIC) with confidence tier (T1/T2/T3), all sources resolve to syntheses + domain files below.

## New research artifacts (practitioner-intelligence/)

- syntheses/gtm.md, syntheses/pricing.md, syntheses/analytics.md, syntheses/competitive.md, syntheses/dtc.md
- domains/gtm/{balfour,ellis,rachitsky,walker}.md
- domains/pricing/{poyar,campbell,ramanujam}.md
- domains/analytics/{kaushik,cutler,biddle}.md
- domains/competitive/{kellogg,dunford}.md
- domains/dtc/{sharma,youderian,firestone}.md

## Known gaps / honesty notes

1. **Competitive intelligence has a thin individual layer** — Kellogg + Dunford are the only strong named practitioners; program methodology comes from vendors (Klue/Crayon, T2). OS should source win/loss + field intel from org sources (Clozd, Gartner) and Reddit field threads per master-map §4. Do not inflate individual practitioner confidence here.
2. **Casey Winters, Dave Gerhardt, Jason Lemkin, Dan Balcauski, Michele Kiss, Chris Mercer, Kurt Elster** were NOT deep-researched this wave (budget) — they appear in syntheses via well-known positions (T2), but no primary fetch this session. Re-verify before quoting them in future skill content.
3. **Quantitative thresholds are context-dependent**: Ellis 40%, Youderian 50% gross margin, Firestone MER targets, Sharma $5k/day — all carry company-size/stage/model conditions; skills must keep those conditions attached (done in the rules).
4. **Firestone material is promotional** (course sales) — T2 at best; his MER/golden-ratio concept is corroborated by Shopify's own MER primer.
5. **Attribution/MMM skipped** per brief (upgraded in Wave 1).
6. **Not verified this session**: Klue/Crayon blog specifics, SaaStr/GLG primary quotes, Winters' essays, eCommerceFuel full report numbers beyond the fetched summary. UNVERIFIED markers in domain files where applicable.

## Cross-repo impact

- pricing-packaging-strategy additions affect marketing-intelligence/pricing-intelligence (future wave: add WTP-survey decision rules there).
- metrics-framework/dashboard-design additions affect marketing-optimize/benchmark-frameworks and utm-governance (alignment of target+benchmark discipline).
- gtm-plan additions affect marketing-intelligence/market-sizing and demand-analysis (stage-gating logic).
- shopify-marketing-audit additions affect marketing-paid/performance-reporting and marketing-optimize/checkout-optimization (MER as the macro metric).
