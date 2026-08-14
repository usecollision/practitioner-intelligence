# Skill Gaps — Wave A6: Optimization Long Tail (12 skills)

Wave: A6. Date: 2026-08-15. Evidence base: syntheses/optimize-longtail.md + domains/optimize-longtail/ (4 panels: baymard, revops, utm-governance, automation). Standard: M4 per scripts/skill-upgrade-standard.md. All skills in usecollision/marketing-optimize/.

## Skills patched (12/12)

| Skill | Grounding added | Decision rules | Metrics | Sources | Confidence |
|---|---|---|---|---|---|
| funnel-analysis | Laja, Kohavi, Sullivan, MacDonald, Biddle/Cutler, Wolf (cro+analytics reuse) | 7 | stage conversion+volume, marginal impact, SRM | 7 | T1/T2 |
| landing-page-optimization | Aagaard, Wolf, Laja, MacDonald, Georgiev, MECLABS (cro+messaging reuse) | 7 | conv by source, RPU, CWV guardrails | 7 | T2 |
| signup-flow | Biddle, Cutler, Laja, MacDonald, Kaushik (cro+analytics reuse) | 7 | activation, retention, guardrails | 6 | T1/T2 |
| checkout-optimization | Baymard Institute (NEW panel), Laja/MacDonald | 7 | cart→purchase, RPU/AOV guardrails | 6 | T1 (Baymard) |
| forms-microcopy | Baymard, Laja, Aagaard, MacDonald, NN/g (cro+messaging reuse) | 7 | completion, per-field abandonment | 7 | T1/T2 |
| product-analytics | Cutler, Biddle, Kaushik, Seiden (analytics reuse) | 8 | activation, retention, taxonomy drift | 5 | T1 |
| utm-governance | McGaw, Napkyn, Usermaven, WebIQ, Improvado (NEW panel) | 8 | sprawl counts, % unassigned, compliance | 7 | T1/T2 (Improvado T3) |
| workflow-builder | Alltomate, Olostep, n8n, Zapier/Clearbit (NEW panel) | 7 | run success, error rate, time saved | 7 | T2 (n8n community T3) |
| crm-lead-ops | Oldroyd HBR, Prospeo, Ivris, RevBlack, NC Squared, OnTheFuze, Kubaru (NEW panel) | 8 | speed-to-lead, acceptance, MQL→SQL, SQL→Opp | 8 | T1 (Oldroyd) / T2 |
| crm-pipeline-attribution | Seufert, Walker, Oldroyd, OnTheFuze, McGaw (attribution layer reuse) | 7 | source fill rate, velocity, reconciliation | 7 | T1/T2 |
| attribution-model-selection | Seufert, AdMaxxer/AdSights, Metricuno, Binet & Field, Kaushik (paid-strategy reuse) | 7 | MER, blended CAC, overlap tax, iROAS | 7 | T1 consensus / T3 vendor numbers |
| experimentation-program | Vermeer, Labay, Kohavi, Georgiev, Atticus Li, Sullivan (cro reuse) | 8 | decisions-supported, win-rate band, SRM | 7 | T1 stats / T2 org |

Each patch inserts `## Practitioner Grounding`, `## Decision Rules`, `## Metrics`, `## Practitioner Failure Modes`, `## Sources` before `## Evaluation & QA` (single anchor patch per file). Frontmatter and original gates untouched; no commits (per task instructions). Verified post-patch: every file has exactly one of each section, original `## Evaluation & QA` intact, +35–48 lines each.

## Evidence quality by gap

- **Checkout (Baymard)** — STRONG, T1. Primary institute sources fetched via search excerpts: baymard.com research overview, "Reasons for Cart Abandonment – Why 70% of Do So," form-field benchmarks, cart-abandonment list. Large-sample EMPIRICAL base (272 think-aloud sessions, 11,777 survey participants, 54,000+ hours). Quantified levers (48% costs, 26% account, 12 vs 23.48 elements, 11–14% perceived-complexity lift) are directly usable as M4 thresholds. Device-split (mobile 80%) is Dynamic Yield data cited by secondaries — marked T2.
- **RevOps (crm-lead-ops)** — STRONG. Oldroyd HBR 2011 is T1 academic and independently replicated (Velocify 3.5M leads; Optifai N=939 benchmark T3). Calibration targets (2x rule, 80% acceptance, 30% MQL→SQL, <20% SQL→Opp, 5-point drift, 60–80 threshold) are operator/vendor consensus — marked HEURISTIC T2, coherent across 4+ independent vendors.
- **UTM governance** — GOOD. McGaw (UTM.io founder) is the primary practitioner voice (T1). GA4-specific mechanics (case-sensitivity → duplicates; custom mediums → Unassigned) from WebIQ/Usermaven are consistent with GA4 behavior (T2). Improvado's 7/9/11-field inflection is single-source — marked T3 in skill.
- **Automation** — MODERATE (T2). Best sources are a Zapier Platinum partner (Alltomate) and Olostep; n8n/Zapier template libraries are community content (T3). No famous-practitioner layer exists for this discipline; patterns (business-rule-first, error handling, native-first) are consensus and structural rather than numeric.

## Gaps for future waves

- Baymard premium benchmark numbers (per-site scores, full 134 guidelines) are paywalled; only headline findings verified.
- Oldroyd 100x/21x magnitudes are 2007-era and vendor-recirculated; direction replicated, exact multipliers unverified across verticals (esp. B2B SaaS vs local services).
- No public RCT on lead-scoring calibration targets (2x/80%/30%) — practitioner consensus only.
- Automation ROI/time-saved claims are vendor-marketed; no independent evidence base.
- One-page vs multi-step checkout: Baymard's own A/B showed null; the contextual guidance (AOV/mobile thresholds) is synthesis from secondary sources — mark T2.

## Verification notes

- No fabricated quotes: every attribution resolves to a panel Sources entry or the cro/analytics/paid-strategy syntheses; T3 items flagged inline (Improvado, Optifai, vendor benchmarks).
- Evidence reuse honored: 8 of 12 skills encode existing syntheses (cro.md, analytics.md, paid-strategy.md); research performed only for the 4 gaps.
- Exa MCP rate-limited (HTTP 429) during this wave; research completed via parallel_search MCP fallback (same content quality, search-excerpt based).
