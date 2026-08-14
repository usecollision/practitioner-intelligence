---
practitioner: Martin Goodson
role: Data scientist / experimentation statistician (VWO SmartStats inventor; later Deliveroo); author of "Smooth Bayesian A/B Testing"
company: VWO (formerly); independent (UNKNOWN current)
type: researcher
confidence: T2
domains:
  - experimentation statistics (Bayesian)
verified: 2026-08-14
sources_checked: 3
---

## Beliefs
- Frequentist NHST cannot answer the question practitioners actually ask ("what is the probability B is better than A?") — it answers a different question (p-value) that is routinely misinterpreted as that probability [1]
- A/B testing "did not evolve keeping conversion rate optimization in mind"; statistical methods should be customized to the conversion workflow, including when to stop and how much uncertainty remains [2]
- Decisions under uncertainty should be framed as expected loss, not binary significance: stop when the expected loss of choosing the current best variant drops below a "threshold of caring" [1]

## Principles
- Quantify uncertainty continuously: report a conversion-rate range (credible interval) that narrows as data accumulates, not a single point estimate [2]
- Use exact distributions (beta-binomial), not normal approximations, so results are valid at small sample sizes [1]
- Guard against "fishing": tooling must warn on mid-test goal changes and keep an audit log, because goal-switching after results is a real false-positive factory [1]
- Preserve the testing process (hypothesis → run → decide); Bayesian stats "just cuts down your waiting time, drastically" [1]

## Frameworks
- **Smooth Bayesian A/B testing** (Goodson & Bishop, 2016; arXiv): independent beta-binomial models per variant with flat/non-informative priors; decision metrics:
  - **Probability of being best** (chance to beat all variants) — declare winner when ≥95% (PBB)
  - **Expected loss / potential loss** — expected lift foregone if the recommended variant is wrong; declare a decision only when potential loss < **Threshold of Caring (TOC)** ≈ baseline metric × certainty mode × 10% [1,3]
  - **Probability to beat baseline (PTBA)** — secondary decision metric (≥95%)
- **Optional stopping stance**: Bayesian posterior inference remains valid under continuous monitoring (his papers argue the posterior is valid for inference about the parameter given the data; industry debate — Microsoft's "Continuous Monitoring of A/B Tests without Pain" proves validity under *proper* stopping rules and flags improper ones) [2,4]
- **Sequential extension** (VWO enhanced SmartStats): monitoring probabilities with maximum-sample-size adjustments to control peeking bias; multiple-variation correction by widening confidence intervals rather than Bonferroni threshold shifts [3]

## Heuristics
- Minimum test conditions at VWO: 25 conversions per variation, 1,500 visitors, at least one week [2]
- Declare winner when PBB ≥ 95% AND potential loss < TOC; disable a variant when its chance of success < 5% [3]
- Feed the posterior of one experiment as the prior of the next (iterative learning) [5]

## Tactics
- Report improvement as a credible interval ("median improvement expected; 99% interval of plausible improvement") instead of p-value [2]
- Use 7M-sample Monte Carlo comparisons between posterior distributions for PBB/PTBA [2]
- Stop early when the decision metric is satisfied (his exit-intent banner case: control declared winner at ~1,000 visitors) [5]

## Tools
- VWO SmartStats (he designed the original statistics engine; Chris Stucchio wrote the technical whitepaper), the `abtest` R package lineage (Kass & Vaidyanathan approach) [1,2]

## Inputs
- Conversion counts per variant, traffic rate, business "threshold of caring" (what loss is tolerable), prior knowledge (optional) [1,3]

## Outputs
- SmartStats engine, "Smooth Bayesian A/B Testing" paper, "Bayesian A/B testing at VWO" blog series (the canon for Bayesian A/B in CRO), educational writing [1,5]

## Metrics
- PBB, PTBA, expected/potential loss, credible intervals, time-to-decision [1,2,3]

## Decision rules
- When the question is "which variant do I ship?" → decide on PBB ≥95% + potential loss < TOC, not p < 0.05 [1,3]
- When a variant's chance of success drops below 5% → disable it (futility) [3]
- When you want to keep monitoring without a fixed horizon → Bayesian optional stopping (with proper stopping rules; contested by frequentists) [4]
- When prior knowledge exists from historical tests → empirical-Bayes priors (learned from past experiments) rather than subjective priors [4]

## Failure modes
- Interpreting p-values as "probability B beats A" — the field's most common misinterpretation (his founding motivation) [1]
- Fishing: choosing the goal after seeing results; tooling must log goal changes [1]
- Subjective/informed priors used to validate a favored outcome — "Bayesian hacking"; priors should be empirically learned [4]
- Stopping without a proper stopping rule invalidates even Bayesian claims [4]

## Contrarian beliefs
- Peeking is not inherently invalid under Bayesian optional stopping (the controversy that made him famous; Microsoft's paper formally proved it valid under proper stopping rules, and flagged improper ones) [4]
- Optimization for speed (more tests per unit time) can be worth trading stricter error control — SmartStats explicitly accepts more false positives "that won't hurt the bottom line" [1]
- Stop thinking "testing for truth", start thinking "maximizing expected value" [1]

## Examples
- VWO exit-intent banner test: control declared winner at ~1,000 visitors via Bayesian monitoring vs p=0.042 frequentist conclusion — both agreed, Bayesian reached it faster with continuous monitoring [5]
- SmartStats: "cuts down your waiting time, drastically… you can run more tests, learn faster" [1]

## Conditions
- Bayesian methods shine when: decisions are continuous, traffic is limited, and the business can articulate a threshold of caring [1,2]
- His "truth vs revenue" framing applies where test volume and opportunity cost dominate pure statistical rigor [1]

## Limitations
- The frequentist school (Georgiev, Kohavi) argues Bayesian optional stopping claims were oversold; unbiased estimates after stopping remain hard; posterior claims under sequential monitoring need proper stopping rules (verified via Microsoft's paper) [4]
- Threshold of caring is a business judgment; mis-set TOC produces confident wrong decisions [1,3]

## Sources
1. VWO SmartStats technical whitepaper (Stucchio; the engine Goodson designed) | vwo.com/downloads/VWO_SmartStats_technical_whitepaper.pdf | whitepaper | 1 | 2026-08-14
2. How VWO Calculates a Winning Variation | help.vwo.com/hc/en-us/articles/360033471874 | docs | 1 | 2026-08-14
3. VWO's enhanced SmartStats (2024) | vwo.com/product-updates/enhanced-vwo-smartstats/ + vwo.com/why-us/technology/statistics/ | docs | 1 | 2026-08-14
4. Continuous Monitoring of A/B Tests without Pain: Optional Stopping in Bayesian Testing (Microsoft Research; validates/caveats the Goodson school) | microsoft.com/en-us/research/publication/continuous-monitoring-of-a-b-tests-without-pain-optional-stopping-in-bayesian-testing/ | paper | 2 | 2026-08-14
5. What is a Bayesian statistical engine in A/B testing? | vwo.com/blog/bayesian-a-b-testing-a-powerful-reasoning-model/ | article | 2 | 2026-08-14
NOTE: "Smooth Bayesian A/B Testing" (Goodson & Bishop, 2016) is his canonical paper — title/venue verified via domain knowledge; content claims in this file beyond the sources above are T2.
