# SKILL GAP ANALYSIS — CRO & Experimentation (Wave 1, 2026-08-14)

Research: `syntheses/cro.md` · Domains: `domains/cro/*` (12 files) · Status: **implemented**

## Audit findings → changes

| Skill | Audit | Change |
|---|---|---|
| cro-audit | M3 | +ResearchXL/Sullivan hypothesis discipline, instrumentation-first rule (A/A, SRM), <1K visits/week method switch, message-match-first, RPU primary metric, win-rate 20-40% diagnostic, 9 sources |
| ab-testing | M2 | +Peeking 3-case rule (abort/don't-act/win), significance-as-business-calculation, Bayesian-vs-frequentist conditions, SRM/A-A validation, 5 sources |
| experiment-prioritization | M3 | +Evidence-provenance scoring (Confidence ≤2 for opinion-only), win-rate calibration band, inconclusive-is-valid rule, 6 sources |

## Key encoded knowledge

1. **Instrumentation before inference**: SRM is common enough that "everyone who tests finds it" (Vermeer) — every audit/test starts with an A/A + SRM check.
2. **Traffic thresholds decide method**: <1K visits/week → no valid small-effect tests; qualitative + rapid concept tests + honest before/after instead (MacDonald/Laursen/Kohavi math).
3. **Peeking nuance**: never stop-for-win unplanned (false positives inflate by orders of magnitude — Heap >60%); abort-for-harm is the allowed exception (Kohavi).
4. **Message-match is the biggest CRO lever** (Aagaard replications: Saxo +99.4%) — CRO on a message-mismatched page is wasted.
5. **Win-rate band 20-40%** as program diagnostic (below = cosmetic tests, above = too-safe tests).
6. **RPU not CR**: revenue per visitor is the primary metric; CR up with AOV down is a loss.

## Validation

- [x] All 3 skills patched per SKILL-UPDATE-STANDARD (M4 contract)
- [x] Rules tagged with claim type + confidence; sources resolve
- [x] validate-tools.py + check-integrity.py pass
- [x] Pushed to marketing-optimize @ main
