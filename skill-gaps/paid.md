# SKILL GAP ANALYSIS — Paid Strategy & Media Planning (Wave 1, 2026-08-14)

Research: `syntheses/paid-strategy.md` · Domains: `domains/paid/*` · Status: **implemented**

## What the audit found

| Skill | Audit maturity | Core gap |
|---|---|---|
| paid-strategy | M2 | No brand/activation layer; allocation rules were stage-agnostic; no attribution-vs-incrementality discipline |
| media-planning | M2 | No effectiveness evidence (Binet/Sharp absent); no context decision tree; no incrementality test menu |
| performance-reporting | M1 (marker scan) | No overlap-tax diagnostic; MER was named but not operationalized with a target formula |
| mmm-incrementality | M3 | No iROAS benchmarks; no ghost-ads method; no test-design minimums |

## Gaps found → changes made

1. **Brand:activation decision tree missing entirely** → added to paid-strategy + media-planning: 62:38 baseline (Binet & Field), rational-categories-need-more-brand counterintuitive rule, stage-based ceilings (Francois), B2B variants (46:54 / Walker model), annual review guardrail.
2. **Platform ROAS treated as truth** → added overlap-tax diagnostic (>35% = fiction), MER target formula (1.3 ÷ contribution margin), iROAS divergence benchmarks (brand search 0.10-0.25x, retargeting 0.20-0.35x), never-cut-prospecting-on-ROAS rule.
3. **No incrementality method menu** → ghost ads added to mmm-incrementality; test-design minimums (5-15k users/arm, 6-8 matched geos, pre-test baseline); "confounded holdout worse than no test" guardrail.
4. **No sources anywhere** → 4 skills now carry Practitioner Grounding + Sources sections with tier tags.

## Left for later (documented, not blocked)

- Binet/Field findings pre-date full AI-bidding era — re-verify ratio validity when AI-bidding studies publish (evidence gap).
- MMM vs MER accuracy at small budgets has no public evidence — encode as uncertainty, not fact.
- Cross-link to a brand-assets playbook for sub-threshold budgets — depends on brand-strategy content existing (marketing-messaging thought-leadership/brand-voice).

## Validation

- [x] SKILL-TEMPLATE structure intact (frontmatter, gates)
- [x] Every decision rule tagged claim-type + confidence
- [x] Sources resolve to research files in practitioner-intelligence
- [x] Cross-repo: media-planning/performance-reporting/mmm-incrementality cross-links verified
- [x] validate-tools.py + check-integrity.py pass (marketing-core)
- [x] Commits pushed: marketing-paid (3 skills), marketing-optimize (1 skill)
