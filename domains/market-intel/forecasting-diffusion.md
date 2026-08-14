---
practitioner: Bass diffusion / McKinsey scenario-planning practice
role: strategy-consultant diffusion forecasting + McKinsey scenario planning canon
company: Frank Bass (academic, 1969), Everett Rogers (1962), McKinsey & Co., FP&A practice (Gartner 2025), Entertainment Strategy Guy
type: researcher|classic|insider
confidence: T1
domains:
  - market-forecasting
verified: 2026-08-15
sources_checked: 8
---

## Beliefs
- When a product has no direct sales history (new category, regulatory-cleared device, platform), regression fails — diffusion modeling via analogous cases is the workhorse (Bass practitioner repo, strategy engagement) (T2).
- Forecasts exist to support decisions; scenarios must be decision-ready, with trigger points, not reporting exercises (FP&A practice; McKinsey) (T1/T2).
- A forecast that can't hindcast shouldn't forecast; error review is how forecasting improves (existing skill; FP&A rolling practice) (T2).

## Principles
- Adoption = innovation (p: external influence) + imitation (q: word of mouth) + market potential (m) (Bass 1969) (T1).
- The forecast is only as good as your analogs: select on regulatory pathway, buyer persona, switching cost, category maturity — not "same industry" (T2; "bad analog selection is the #1 way Bass forecasts go wrong").
- m (market potential) must be sized separately via TAM; getting m wrong changes absolute numbers but not curve shape (T2).
- Scenario traps (McKinsey, 2009 "The use and abuse of scenarios"): too many scenarios → paralysis; scenarios muddling a bold vision; discarding far-fetched scenarios too quickly — "often the most valuable ones are those that seem the most far-fetched" (T1).

## Frameworks
- Bass diffusion model: N(t) with m, p, q; typical fitted values p≈0.003-0.016 (regulated→viral), q≈0.4-0.5 (published meta-analyses) (T2).
- Rogers S-curve: innovators → early adopters → early/late majority → laggards; phases introduction/growth/maturity/decline (T1).
- Scenario planning: 3-5 coherent named scenarios + sensitivity + critical assumption; trigger-based governance; rolling quarterly refresh (McKinsey + FP&A practice) (T2).
- Analogical forecasting with search traffic: search trends precede adoption and track full life-cycles across countries/languages (ScienceDirect 2017) (T1/T2).

## Processes
1. Write the decision, horizon, unit, scope before modeling (existing skill; McKinsey discipline) (T2).
2. No history → select 3+ analogs matched on diffusion-relevant dimensions; weight by similarity (T2).
3. Fit Bass parameters per analog (nonlinear least squares); scenario band = slowest↔fastest analog (T2).
4. Sanity checks: installed-base benchmarks; implied year-1 sell-through "laugh test"; inflection point should align with when word-of-mouth kicks in (second derivative) (T2).
5. Cross-check against top-down category growth; reconcile methods (gap >2x = assumption error) (T2).
6. Publish range + scenarios + named critical assumption; set decision triggers; log forecast vs actual quarterly (T1/T2).

## Heuristics
- p≈0.003-0.016, q≈0.4-0.5 as starting priors; adjust by friction/regulation (T2).
- If actual sales slow before the modeled inflection, your m was too high — treat early misses as sizing errors, not execution problems (Entertainment Strategy Guy) (T2).
- Horizon >5 years: scenarios, not numbers (existing skill; McKinsey) (T2).
- Flash/rolling cadence: refresh assumptions quarterly, review triggers monthly (FP&A practice) (T2).

## Inputs
Historical data (if any), analog cases, TAM (m), growth drivers, decision context, leadership risk appetite.

## Outputs
Forecast model, scenario set (3-5), sensitivity table, critical-assumption monitor, forecast-vs-actual log.

## Metrics
Forecast error vs actual (logged per cycle); scenario trigger hit-rate; % scenarios with named triggers; sensitivity swing of critical assumption.

## Decision rules
- IF no direct history AND analogs exist THEN Bass with similarity-weighted analogs (T2).
- IF forecast horizon >5 years THEN deliver scenarios, not point numbers (McKinsey, T1).
- IF top-down and bottom-up diverge >2x THEN fix assumptions; never quietly pick the rosier (existing + practice, T2).
- IF leadership demands one number THEN refuse: range + scenarios + critical assumption (McKinsey, T1).
- IF scenario set exceeds 5 THEN cut to 3-5 and name them vividly (McKinsey, T1).
- IF uncertainty is high THEN define measurable decision triggers before conditions change; review monthly/quarterly (FP&A practice, T2).
- IF actuals miss the model early THEN re-check market potential m before blaming execution (Bass practitioner, T2).

## Failure modes
- Anchoring to leadership's desired number; fake precision (12.4% CAGR); point estimates (existing skill + McKinsey) (T2).
- Analogs picked by industry label rather than diffusion mechanics (T2).
- Scenarios built as reporting exercises — analytically robust, operationally unused; by the time finance answers, the decision is made (FP&A practice via Gartner 2025: only 3% of orgs align strategic/operational/financial planning) (T2).
- Discarding the "impossible" scenario (McKinsey) (T1).
- Never logging forecast vs actual (existing skill) (T2).

## Contrarian beliefs
- Sales slowdown is often a sizing error, not an execution failure (T2).
- The most valuable scenarios are usually the far-fetched ones (McKinsey) (T1).

## Conditions
Bass: new category, analogs available, TAM sizeable separately. Scenarios: high uncertainty, committed leadership, decision triggers defined. Both fail under fake certainty or when used to avoid decisions.

## Limitations
Diffusion models predict curve shape and peak timing better than absolute levels; scenario planning can't assign probabilities honestly when none exist; model outputs inherit TAM error.

## Sources
1. Bass practitioner repo — Bass Diffusion Model (analog selection, p/q ranges, sanity checks) | github.com/ziah-lin/bass-diffusion-model | T2 | 2026-08-15
2. McKinsey — The use and abuse of scenarios (2009) | mckinsey.com (Classics) | T1 | 2026-08-15
3. R Journal — Metapopulation Bass Diffusion (model mechanics, peak-timing value) | journal.r-project.org/articles/RJ-2017-006 | T1 | 2026-08-15
4. Entertainment Strategy Guy — Bass Diffusion Model Explained (m as error source) | entertainmentstrategyguy.com/2019/09/11 | T2 | 2026-08-15
5. ScienceDirect — Search-traffic analogical forecasting | sciencedirect.com/science/article/abs/pii/S0040162514002297 | T1 | 2026-08-15
6. Ntegra — S-Curve model (Rogers) phases and strategy | ntegra.com/insights/navigating-the-adoption-process-of-technologyinnovation | T3 | 2026-08-15
7. UVID — Scenario planning in FP&A (triggers, rolling planning, Gartner 2025 stat) | uvidconsulting.com/blogs/scenario-planning-fpa | T2 | 2026-08-15
8. Wikipedia — Bass diffusion model | en.wikipedia.org/wiki/Bass_diffusion_model | T2 | 2026-08-15
