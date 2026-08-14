# WAVE A3 — MARKET & STRATEGY INTELLIGENCE: SKILL-GAP RECORD

Date: 2026-08-15. Research: syntheses/market-intel.md + 6 dossiers in domains/market-intel/.
Repo: usecollision/marketing-intelligence. NOT committed (per brief).

## Skills upgraded to M4 (7)
| Skill | Practitioner Grounding | Decision Rules | Metrics | Sources | Failure modes added | Cross-repo notes |
|---|---|---|---|---|---|---|
| market-sizing | 6 entries (a16z, Mitra, Zimt, TechCrunch, a16z/Haber, VC analysts) | 8 rules | 5 metrics | 8 sources | 6 | feeds gtm-plan, icp-builder, pricing-intelligence |
| market-map | 5 entries (Infomineo, Umbrex, industry-lens, PROOF, Dunford-reuse) | 8 rules | 5 metrics | 6 sources | 5 | feeds positioning-framework, competitor-battlecards |
| market-forecasting | 6 entries (Bass/Rogers, Bass practitioner repo, McKinsey, FP&A practice, ESG, ScienceDirect) | 8 rules | 5 metrics | 7 sources | 5 | depends on market-sizing (m); feeds growth-strategy |
| demand-analysis | 5 entries (ProofEngine, IdeaCrystal, Demand Discovery, Zimt, existing canon) | 8 rules | 5 metrics | 5 sources | 5 | feeds market-sizing, trend-detection, keyword-research |
| industry-category-analysis | 6 entries (Porter, Investopedia, Visual-Paradigm, DrinkBird, IBISWorld, AHC) | 8 rules | 5 metrics | 6 sources | 5 | feeds market-map, category-design, pricing-intelligence |
| trend-detection | 5 entries (Gartner, Rogers, Spate, Qmarkets, existing canon) | 8 rules | 5 metrics | 5 sources | 5 | feeds content-calendar, growth-strategy, market-map |
| category-design | 5 entries (Lochhead, Kellogg, Moore, Ramadan, positioning synthesis) | 8 rules | 5 metrics | 4 sources | 4 | REUSED positioning.md research; feeds gtm-plan, messaging |

## Evidence quality assessment
- **T1 (strong)**: a16z bottom-up TAM essay; Gartner Hype Cycle methodology; McKinsey scenario canon; Investopedia Five Forces pitfalls; Bass model academic canon (1969) + R-Journal; ScienceDirect search-traffic forecasting study; Kellogg category-design skepticism (reused).
- **T2 (good, practitioner-grade)**: Infomineo/Umbrex/industry-lens consulting practices; Spate and Qmarkets trend intelligence; ProofEngine/IdeaCrystal demand validation; Zimt/BridgingLocal sizing practice guides; Visual-Paradigm/DrinkBird Five Forces application; Bass practitioner repo (anonymized engagement, p/q ranges consistent with literature).
- **T3 (caution)**: demand-score cutoffs (ProofEngine 21-30 "strong"; Demand Discovery scores); Pedowitz 97% time-reduction claim; Sramana Mitra opinion; Play Bigger 76% category-economics; SOM % per vertical (planning convention only).
- **Methodology gaps in the source base**: no RCTs exist for any of these disciplines — all frameworks are practitioner convergence, not measured effect. Quantitative thresholds carry their context (stage, model, audience) in the rules.

## What changed vs prior state
- All 7 skills were already M2/M3 (gates + scoring rubrics + basic failure modes). Added the five M4 sections per the standard; every decision rule is if/then with attribution + confidence; every Practitioner Grounding entry resolves to a Sources entry.
- Category-design: no new research — encoded the positioning synthesis (Lochhead/Kellogg/Moore/Ramadan) per brief instruction.
- Notable new intelligence encoded: value-theory sizing method; 20-30% convergence band; market-structure overlay (a16z/Haber); Bass analog-selection failure + sanity checks; McKinsey scenario traps; trigger-based forecasting governance; Five Forces "company vs industry" misuse + interdependence; demand money-tests and workaround signals; fad-vs-trend shape rules (6-12 month window); category-design Kellogg gate.

## Open items / follow-ups
- No commit made (brief says do NOT commit or push). Parent orchestrator should commit with the standard convention referencing syntheses/market-intel.md.
- scripts/validate-tools.py / check-integrity.py (marketing-core) not run — scripts live in another repo; structural check done manually (frontmatter + sections verified via grep).
- Exa MCP rate-limited mid-session; switched to parallel_search MCP (worked) — future waves should expect Exa free-tier limits.
