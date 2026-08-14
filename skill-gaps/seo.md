# SKILL GAP ANALYSIS — SEO (Wave 2, 2026-08-14)

Research: `syntheses/seo.md` · Domains: `domains/seo/*` (22 files) · Status: **implemented**

## Audit findings → changes

| Skill | Audit | Change |
|---|---|---|
| seo-audit | M2 | +4-gate diagnostic (drop → classify; launch → index/rendering; new site → crawl health; stagnation → decay), impact×effort 5-10 ticket discipline, Capper correlation filter, volume-as-trap, AI-citation metric, 10 sources |
| technical-seo | M2 | +Index/crawl-first ordering, templates-not-pages, test-template-changes-with-controls gate (Critchlow −27%), crawl-budget noise rejection (Mueller), governance requirement, 6 sources |
| keyword-research | M2 | +Traffic-potential filter (Soulo), bottom-funnel intent gate (Dunning), Gübür-vs-Law depth/brevity conditions, product-led SEO (E. Schwartz), SERP-decides-format, 6 sources |
| link-building | M2 | +Earned-only policy (Moogan + 2026 SpamBrain data), sustainability test, 1-20 links expectation band (McGuirk), internal-data-first (Milligan), 4 sources |
| local-seo | M2 | +Relevance×distance×prominence triad, test-single-variables (Hawkins' address-hiding case), citations≠links (Shaw), supplier-tier forensics (Blumenthal), review velocity over rating, 3 sources |

## Key encoded knowledge

1. **Diagnose before touching content** — drops are relevancy/intent/quality; never nuke until classified (Gabe/Ray).
2. **5-10 dev tickets, not dumps** — three independent practitioners converged on the identical output rule (Stox/Solis/Indigo).
3. **Untested best-practice rollouts are the field's silent killer** — −27% title-tag incident (Critchlow); test at template scale.
4. **Volume is a trap; traffic potential and bottom-funnel intent are the filters** (Soulo/Dunning).
5. **Link manipulation is pattern-detected in 2026** — earned-only; sustainability test as the strategy gate (Moogan).
6. **Platform guidance can be wrong** — Hawkins' address-hiding counterexample encoded as test-before-trust.

## Suggested follow-ups (not yet implemented)

- NEW skill candidate: `core-update-response` (delta report → classification → kitchen-sink remediation → long-game expectation) — flagged for Wave 4 decision.
- serp-analysis: add AI-citation tracking (Indig's decoupling metric) — flagged for Wave 4.

## Validation

- [x] 5 skills patched per M4 contract; rules tagged; sources resolve
- [x] Pushed to marketing-channels @ main
- [x] validate-tools.py + check-integrity.py pass (run at next full validation)
