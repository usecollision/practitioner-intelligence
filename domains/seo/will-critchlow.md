---
practitioner: Will Critchlow
role: Founder / CEO
company: SearchPilot (and Distilled legacy)
type: practitioner|founder|researcher
confidence: T1
domains:
  - SEO experimentation
  - Technical SEO
  - Causal measurement
verified: 2026-08-14
sources_checked: 3
---

## Beliefs
- SEO can and should be measured causally: controlled experiments with genuine control groups are the only way to isolate a change's effect from updates, seasonality, and competitors (FRAMEWORK).
- "Often professional SEOs are not much better than chance at being able to tell whether a change is going to be positive or negative" (EMPIRICAL, from SearchPilot's test database — his strongest claim).
- Best-practice changes can actively hurt; small negative effects go unnoticed without testing (EMPIRICAL).

## Frameworks
- **Controlled bucketed A/B testing for SEO**: split pages into statistically similar control and variant groups; both run concurrently; compare variant against control's live performance plus pre-test historical relationship (FRAMEWORK — SearchPilot method).
- **Credible intervals over point estimates**: report most-likely effect size, plausible range, and uncertainty; decisions made with confidence levels, not p-hacked wins (FRAMEWORK).
- **Split Optimizer (2019)**: purpose-built neural model estimating the counterfactual (what would have happened without the change); replaced general-purpose Causal Impact which produced too many inconclusive tests on layered seasonal SEO data (FRAMEWORK).

## Processes
1. Formulate testable SEO change (title tags, boilerplate removal, schema, internal links, content).
2. Bucket eligible pages into statistically similar control/variant groups (randomization per-user doesn't work — crawlers are single visitors; pages carry their own traffic history/seasonality).
3. Run both groups concurrently; let external shocks hit both equally.
4. Estimate effect with credible interval; decide rollout vs rollback vs rerun.
5. Revisit past tests when Google/industry changes — invalidated tests should be rerun.

## Heuristics
- CRO statistics don't transfer to SEO — different data conditions (HEURISTIC).
- A 3% drop can hide in seasonality/updates/competitor moves; without controls you may never notice and never undo it (HEURISTIC).
- "If your competitors are not testing, never rolling out a negative change is a superpower" (HEURISTIC).

## Tactics
- Run negative tests deliberately — learning what NOT to deploy is as valuable as wins (TACTIC).
- Test "best practice" changes before mass rollout (TACTIC).
- Remove boilerplate/content blocks only after testing — a "terrible" boilerplate block on e-commerce category pages tested NEGATIVE when removed (it was adding value) (TACTIC + EXAMPLE).

## Tools
- SearchPilot platform; Causal Impact (origin); Split Optimizer (current); GSC + analytics data feeds.

## Inputs
- Traffic data with history; clearly defined change; enough eligible pages to bucket; concurrent control group.

## Outputs
- Credible-interval impact estimates per test; rollout decisions; a cumulative test database (their "library of what works").

## Metrics
- Organic traffic (and downstream conversions where measurable) on variant vs control; credible interval width; inconclusive-test rate.

## Decision rules
- Expected value (effect size × probability) positive and interval excludes zero → roll out (DECISION RULE).
- Interval includes zero → don't roll out; treat as inconclusive, not failure (DECISION RULE).
- Change touches a template/category shared across many pages → test it before shipping (DECISION RULE).
- Google announces an algorithm change → recheck past tests for invalidation (DECISION RULE).

## Failure modes
- Deploying best-practice changes untested: e.g., a "sensible" title-tag change driven by keyword research caused −27% organic traffic (EXAMPLE — documented by SearchPilot).
- Removing "obviously bad" boilerplate that was actually ranking-relevant (−impact) (EXAMPLE).
- Applying CRO stats to SEO data — invalid inference (warned against).
- Short observation windows that conflate update effects with change effects (warned against).

## Contrarian beliefs
- SEO best practices are priors, not laws — they "won't always hold true depending on the website, industry, and query intent"; test them (OPINION/EMPIRICAL).
- Keyword-research-driven changes are not safe by construction (EMPIRICAL).

## Conditions
- Requires sites with many similar pages (e-commerce, large publishers, programmatic) and meaningful traffic; needs engineering to bucket and deploy. Fails on tiny sites and single-page changes with no comparables.

## Limitations
- Not all changes are testable (site-wide redesigns, domain moves); control groups degrade when pages interlink and leak effects; long-tail traffic is noisy → high inconclusive rates; requires ongoing investment.

## Sources
1. "The Math Behind SearchPilot: How SEO A/B Testing Actually Works" | https://www.searchpilot.com/resources/blog/the-math-behind-searchpilot-how-seo-a/b-testing-actually-works | primary practitioner blog | tier 1 | 2026-08-14
2. "What we can learn from losing SEO tests" | https://www.searchpilot.com/resources/blog/will-critchlow-what-we-can-learn-from-losing-seo-tests | primary practitioner blog | tier 1 | 2026-08-14
3. "Learning From Negative Tests — Will Critchlow, Voices of Search" | https://voicesofsearch.com/episode/seo-testing-101-will-critchlow-searchpilot/learning-from-negative-tests-will-critchlow-searchpilot/ | podcast interview | tier 2 | 2026-08-14
