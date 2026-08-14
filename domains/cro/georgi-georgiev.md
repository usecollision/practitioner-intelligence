---
practitioner: Georgi Georgiev
role: Founder, Analytics ToolKit (analytics-toolkit.com / abtestingstats.com); author of "Statistical Methods in Online A/B Testing"
company: Analytics ToolKit
type: researcher
confidence: T1
domains:
  - experimentation statistics
verified: 2026-08-14
sources_checked: 4
---

## Beliefs
- The A/B testing industry routinely misapplies statistics: "I was noticing significant issues with how statistics were applied in the A/B testing practice" and built tools to fix what he critiqued [4]
- Peeking ("unaccounted peeking with intent to stop") is a severe validity threat: with just a few looks, "the actual significance can be orders of magnitude larger than the nominal" [2]
- Fixed-sample tests are "inefficient and impractical" for business: they force you to keep running even when a variant looks disastrous or fantastic; sequential testing retains rigorous error control while allowing early stopping [4]
- Business experiments should be optimized for business risk/reward, not ritual 95% confidence: "testing with 50% confidence threshold?" is a legitimate chapter, not heresy [3]

## Principles
- Sample size is a planning-time decision determined by 4 factors: significance threshold, power, minimum effect of interest (MEI), and variance [1]
- MEI ≠ MDE: the minimum effect you care about (business decision) is not the minimum detectable effect (statistical property); confusing them is a systematic error [3]
- Sequential testing requires pre-specification: interim analyses must be specified in advance to an extent; "significant departures from these specifications can lead to the test ending without a definite conclusion" [1]
- After a sequential stop, the observed lift is biased — "the best guess no longer matches the observed lift"; use bias-corrected estimates [4]

## Frameworks
- **AGILE sequential testing** (his implementation): alpha-spending (efficacy boundary) + beta-spending (futility boundary); stop for efficacy (winner) or futility (no point continuing); error levels spread across interim analyses so overall type I ≤ 5% regardless of stop time [4]
- **A/B/n multiple-comparison corrections**: pair-wise analysis of A/B/n tests without correction inflates false positives; his calculator applies multiple-comparisons adjustments [4]
- **Risk/reward optimal thresholds**: define success as a business trade-off (costs, benefits, risks, rewards, distribution of expected effect sizes); compute risk/reward ratios and the optimal significance threshold per test — including deliberately low thresholds when tests are cheap and opportunity cost is high [3]
- **External validity framework**: generalizability of results (seasonality, representative samples, concurrent tests) as a first-class concern [3]

## Heuristics
- Sequential tests cut sample size/duration 20-80% in theory; real-world average is ~30% shorter than fixed-sample equivalents [4]
- Sequential testing needs "a couple dozen users per variant" minimum — suitable even for low-traffic businesses [4]
- Inconclusive is a real outcome; futility boundaries formalize "stop and call it null" [4]
- Don't test "the perfect shade of blue" — a chapter title mocking cosmetic tests [3]

## Tactics
- Run A/A tests to assess statistical adequacy of instrumentation [3]
- Pre-specify number and timing of interim analyses; use spending functions that tolerate deviation from the schedule [1,4]
- Use bias-corrected lift estimates after sequential stopping [4]
- Prefer one-sided tests where direction is clear; consider non-inferiority tests for equivalence questions [3]

## Tools
- Analytics ToolKit (significance calculator with multiple-comparisons adjustments, A/B test lab incl. SRM, sample size, sequential testing), AGILE, his free book [1,3,4]

## Inputs
- Baseline conversion rate, variance, MEI (business input), acceptable error rates, number/timing of planned analyses, traffic forecast [1,4]

## Outputs
- The most comprehensive public reference on A/B testing statistics (free book, ~300 pages incl. power, sample size, sequential, Bayesian, bandits), calculators, white papers [3]

## Metrics
- Type I / type II error control, expected sample size & efficiency gain, risk/reward ratios, estimated (bias-corrected) lift [3,4]

## Decision rules
- When you expect to want to stop early (for winners or losers) → use sequential testing with pre-specified spending, not fixed-sample with peeking [4]
- When the required sample is unreachable → reduce MEI ambitions, aggregate, or don't run (underpowered tests are a waste) [1,3]
- When the test's expected value is small relative to opportunity cost → lower the significance threshold deliberately (his risk/reward chapter) [3]
- When running A/B/n → use multiple-comparisons-adjusted analysis [4]
- When interpreting a sequential result → report bias-corrected lift, not observed lift [4]

## Failure modes
- Peeking with intent to stop → uncontrolled type I inflation ("orders of magnitude") [2]
- Pair-wise analysis of A/B/n tests [4]
- Confusing statistical significance with business impact and with power [3]
- Underpowered AND overpowered tests (waste of traffic) [3]
- Ignoring external validity: results from a promo-period or non-representative sample don't generalize [3]

## Contrarian beliefs
- 95% confidence is not sacred; the right threshold is a risk/reward business decision [3]
- Sequential testing is not just for big companies — small-traffic businesses benefit most from early stopping [4]
- Bayesian methods have a place but are not strictly superior (his book covers them with caveats) [3]

## Examples
- Real-world data: "the average test duration of sequential tests is close to 30% shorter than an equivalent fixed-sample test" [4]
- His calculator was the first widely available A/B/n tool with multiple-comparisons control ("at a time where pretty much no other tool offered it") [4]

## Conditions
- Sequential testing fits any business that can pre-specify analyses; biggest economic benefit where tests are costly or decisions urgent [4]
- Risk/reward threshold optimization requires estimating costs and effect-size distributions — needs more input data than a simple calculator [3]

## Limitations
- Sequential methods add complexity (stopping time is a random variable; bias correction) — his own caveat [4]
- Business-side inputs (costs, effect distributions) are estimates; "limitations of Risk/Reward calculations" acknowledged in the book [3]

## Sources
1. What is Sample Size? (glossary) | analytics-toolkit.com/glossary/sample-size/ | glossary | 1 | 2026-08-14
2. What is Peeking (optional stopping)? (glossary) | analytics-toolkit.com/glossary/peeking/ | glossary | 1 | 2026-08-14
3. Statistical Methods in Online A/B Testing (book) | abtestingstats.com/Statistical-Methods-in-Online-A-B-Testing-pdf.pdf | book | 1 | 2026-08-14
4. Q&A on Sequential Statistics in A/B Testing | blog.analytics-toolkit.com/2023/qa-on-sequential-statistics-in-a-b-testing/ | interview/Q&A | 1 | 2026-08-14
5. What is Sequential Testing? (glossary) | analytics-toolkit.com/glossary/sequential-testing/ | glossary | 1 | 2026-08-14
