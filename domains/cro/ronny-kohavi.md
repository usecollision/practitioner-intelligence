---
practitioner: Ronny Kohavi
role: Technical Fellow / VP, Microsoft (ex-Amazon); founder of the EXP experimentation platform
company: Microsoft (retired from Amazon; exp-platform.com)
type: researcher
confidence: T1
domains:
  - online controlled experiments
verified: 2026-08-14
sources_checked: 4
---

## Beliefs
- Controlled experiments are "the best scientific way to prove causality" and the gold standard for product decisions; organizations that embrace them with clear evaluation criteria evolve faster [3]
- Listen to customers, not the HiPPO: "Listen to your customers not to the Highest Paid Person's Opinion" [3]
- Data trumps intuition, and intuition is usually wrong: ~90% of ideas fail to improve the metric (his 5%/80%/15% ML rule; the 80% that "works" often doesn't help) [2,3]
- "Triple your experiment rate and you triple your success (and failure) rate. Fail fast & often in order to succeed. Accelerate innovation by lowering the cost of experimenting." [2]

## Principles
- Decide the OEC (Overall Evaluation Criterion) before the test: "the biggest issue with teams that start to experiment is… agree what they are optimizing for; agree on measurable short-term metrics that predict the long-term value (and hard to game)" [2]
- Run experiments on (almost) all users: 50/50 splits maximize power; only the world's biggest sites run 10-20% (with overlap/full-factorial) [4]
- There are never enough users: sample size ∝ σ²/Δ² — as sites mature you must detect smaller deltas, needing 10-100x more users [4]
- Trust the system, verify everything: "Getting numbers is easy; getting numbers you can trust is hard" [2]

## Frameworks
- **OEC framework**: primary metric + guardrail metrics; short-term proxies predictive of long-term value [2]
- **Pitfalls canon** (2009, 2017 papers): failing to agree on OEC; incorrect CI computation for percent effects; standard variance formulas failing on metric families (use bootstrap); Simpson's paradox in ramp-up; robots; audits/instrumentation/controlling all differences [2,5]
- **Sample size formula**: n ≈ (4σ/Δ)² (95% confidence, 90% power). Worked example: e-commerce detecting 5% revenue change → 1.6M users; 5% conversion change → 500K; 20% conversion change → 30,400; checkout-triggered analysis (10% initiate, 50% complete) → 256K site users [3]
- **Variance reduction toolkit**: triggering (analyze exposed users only), lower-variance metrics (Boolean conversion > revenue), CUPED (pre-experiment period), pre-experiment A/A balance checks with automated seed-finding [4]

## Processes
- Experiment platform lifecycle at Microsoft: design templates + pre-experiment gates → seedfinder (hundreds of candidate splits evaluated on last week's data) → low-percentage start → abort in 15 minutes if cheap metric is bad → auto-shutdown if guardrails crossed → ramp to target (e.g., 20% per variant) → daily thousand-metric alerts [2]
- A/A test discipline: p-value distribution over 1,000 A/A tests must be uniform; SRM check: a 50.2/49.8 split has p=1.8e-6 — "SRMs happens to us every week!" [2]

## Heuristics
- 90% of eligible users in experiments, 10% global holdout changed yearly (Bing) [4]
- Cap outliers: trim revenue at the 99th percentile — one library buyer can skew an experiment [2]
- If the pre-experiment split isn't balanced, re-randomize (multiple seeds) [4]
- Run equal-probability variants for fastest exposure [4]

## Tactics
- Run A/A tests when the system is new or suspicious [2]
- Analyze only triggered users (complement users must look like A/A) [4]
- Use bootstrap for families of metrics [5]
- Plan peeking explicitly: curiosity peeking is fine; abort-for-harm peeking is fine; stopping for wins requires group-sequential/always-valid designs [1]

## Tools
- Internal experimentation platforms at scale (Microsoft EXP, Amazon); he co-authored the canonical texts (Trustworthy Online Controlled Experiments, 2020; Practical Guide, 2009/2007) [2,3,4]

## Inputs
- OEC + guardrails agreed by stakeholders, power calculation (σ, Δ), instrumentation validity (A/A, SRM checks), pre-experiment data [2,3,4]

## Outputs
- Papers, the EXP platform methodology, books, the pitfalls canon; ~300 experiment treatments/week at Bing during his tenure [2,4]

## Metrics
- OEC (e.g., sessions/user, revenue/user); guardrail metrics; p-values only from pre-planned analyses; A/A distributions; SRM [2,3,4]

## Decision rules
- Ship a treatment only when the pre-registered analysis says significant AND no guardrail is crossed AND the effect clears the "worth it" bar (business impact ≠ statistical significance) [2,4]
- Peek freely when you will NOT act on the result; peek and abort when you see bugs or harm; NEVER stop for a win without a planned sequential design [1]
- Don't ship underpowered tests: "A common mistake is to run experiments that are underpowered" — compute the minimum sample size and duration before launch [3]
- When metrics are noisy → reduce variance (triggering, CUPED, Boolean metrics) before buying more users [4]
- When a system reports suspicious precision → A/A test it; when splits mismatch → stop analyzing until fixed [2]

## Failure modes
- Peeking/early stopping (his #1 practical failure; "the single most common way teams ship false winners" per practitioners citing him) [1]
- Sample Ratio Mismatch ignored [2]
- Outlier skew (uncapped revenue) [2]
- Simpson's paradox when ramping without analysis windows [5]
- Robots inflating metrics [5]
- Underpowered experiments: "running an experiment that can only detect 1% change when a 1% change = tens of millions/year" [4]
- Metrics with high variance (revenue/user) needing impossible samples [4]

## Contrarian beliefs
- Peeking is not always wrong — the nuance most courses miss (planned vs unplanned peeking) [1]
- Don't shrink traffic to minimize risk: run 50/50 (with ramp-up for safety) — small treatment percentages waste power [3,4]
- Novice belief that more users = the answer; variance reduction is often the better lever [4]

## Examples
- Bing: 300 treatments/week, 15 concurrent experiments per user → 5^15 ≈ 30 billion variants; detecting 0.1% revenue change needs ~80M users [4]
- Amazon: one outlier library buyer ≈ the entire expected lift [2]
- Heap-style false-positive disasters (peeking → >60% false positive rate) are the canonical failure his rules prevent [6]

## Conditions
- His methods assume high-traffic products (100K+ users per variant), engineering support, and mature instrumentation [3,4]
- His variance-reduction toolkit is overkill for low-traffic sites (where CRO practitioners correctly use qualitative research instead) [3]

## Limitations
- 50/50 and 100K-user guidance does not transfer to small-traffic sites — the field's consensus (Goodson/Georgiev/practitioners) is that low-traffic pages should not be tested with these designs [3]
- Even with correct statistics, "controlled experiments are not the panacea for everything" (external validity, long-term effects) [2]

## Sources
1. Peeking at live A/B tests: when is it OK? | linkedin.com/posts/ronnyk_peeking-at-live-ab-tests... | post | 1 | 2026-08-14
2. Trustworthy A/B Tests: Pitfalls (eMetrics 2017) | exp-platform.com/Documents/2017-05-17EmetricsControlledExperimentsPitfallsKohaviNR.pdf | deck/paper | 1 | 2026-08-14
3. Practical Guide to Controlled Experiments on the Web (Kohavi, Henne, Sommerfield) | ai.stanford.edu/~ronnyk/GuideControlledExperiments.pdf | paper | 1 | 2026-08-14
4. Online Controlled Experiments: Lessons from Running A/B/n Tests for 12 Years (KDD keynote) | exp-platform.com/Documents/2015-08OnlineControlledExperimentsKDDKeynoteNR.pdf | paper | 1 | 2026-08-14
5. Seven Pitfalls to Avoid when Running Controlled Experiments | ai.stanford.edu/~ronnyk/2009-ExPpitfalls.pdf | paper | 1 | 2026-08-14
6. 5 Real-World A/B Test Failures (Heap case) | statology.org/5-real-world-a-b-test-failures-and-what-went-wrong/ | secondary | 3 | 2026-08-14
