# SYNTHESIS — CRO & ONLINE EXPERIMENTATION

Practitioners: Peep Laja, Jon MacDonald, Craig Sullivan, Talia Wolf, Michael Aagaard, Brian Massey, Ben Labay, Karl Blanks, Ronny Kohavi, Lukas Vermeer, Georgi Georgiev, Martin Goodson.

## Consensus (what strong practitioners independently agree on)
1. **Research before hypothesis, hypothesis before test** — Laja (ResearchXL: 6 methods → 5 buckets), Sullivan (hypothesis format + analytics health checks), Massey (5-step process), Kohavi (pre-register OEC), Labay (Phase Gate phase 1 = data & insights), Aagaard (research + psychology). The Sullivan hypothesis format ("We believe [A] for people [B] will cause [C]; we'll know via [D]/[E]") is the industry standard, credited by Laja, used by CXL, Speero, Conversion Sciences, Scheijbeler. CLAIM TYPE: FRAMEWORK, near-universal.
2. **Prioritize by objective scoring before building** — PXL (Laja: binary weighted, data-provenance weighted), Massey's Evidence/Impact/Effort/Traffic/ROI 1-5, ICE/PIE as field baseline. Principle: score before debate; drop opinion-only ideas. FRAMEWORK.
3. **Never stop a fixed-horizon test early because it looks good** — Sullivan (run ≥2 business cycles, judge on error bars), Kohavi (peeking nuance: fine to peek, never stop-for-win without sequential design), Georgiev (peeking inflates type I error by orders of magnitude), HubSpot/DRIP/croforce/statology (Heap case: >60% false positive rate from peeking). EMPIRICAL, universal.
4. **Agree the primary metric (and guardrails) before launch** — Kohavi (OEC), Labay (undeniably-concluded test plans), adasight (no shared metric = no clean decision), Atticus Li (trace metric to revenue). EMPIRICAL.
5. **Test data quality before trusting results: A/A tests + SRM checks** — Kohavi (A/A p-distribution uniform; SRM p=1.8e-6 at 50.2/49.8), Vermeer ("one neat trick" — everyone who tests finds it), Georgiev (A/A adequacy), HubSpot (faulty tooling). EMPIRICAL.
6. **Message-match and value clarity are the biggest copy levers** — Aagaard (Saxo +99.4%, Bettingexpert +31.5%), Unbounce glossary, Talia Wolf (messaging audit first), Laja (copy from research). EMPIRICAL (multiple documented case studies).
7. **Cosmetic tests (button color, micro-copy on low-traffic pages) are the field's #1 waste** — Georgiev's "perfect shade of blue" chapter, DRIP ("cockroach of CRO"), piperocket (can't reach significance), Wolf (test strategies not elements), Kohavi (changes must be noticeable). EMPIRICAL + HEURISTIC.
8. **Low-traffic pages should not be A/B tested for small effects** — Kohavi (n ∝ σ²/Δ²; 5% revenue change = 1.6M users), growthlayer (MDE math: test invalid as designed), Jon MacDonald (rapid testing or ship reversibly below 1K visits/week), Niels Laursen (evidence accumulation instead). FRAMEWORK/EMPIRICAL.
9. **The most expensive failures are organizational, not statistical** — Atticus Li (stakeholder override kills programs), adasight/Simon Jackson (output vs outcomes, feature factory, territorial pushback, production bottlenecks), Labay (misalignment, one-way gates), Vermeer (flywheel investment), Kohavi (HiPPO). EMPIRICAL (case-based).
10. **Velocity is a goal in itself** — Kohavi (triple test rate), Vermeer (flywheel: more tests → more decisions), adasight (returns live in the tails; too few tests = no outsized wins), Labay (Data-to-Action cadence). EMPIRICAL at scale; condition: trustworthiness must scale with volume.

## Disagreement (with conditions)
1. **Bayesian vs frequentist statistics** — Goodson/VWO: probability-of-being-best + expected loss + optional stopping is valid and faster ("testing for truth vs maximizing revenue"); Georgiev/Kohavi (frequentist school): unplanned peeking invalidates inference; sequential requires pre-specified spending functions; Microsoft's paper proves Bayesian optional stopping valid only under proper stopping rules. CONDITION: Bayesian monitoring is a legitimate tool for *decisions with a stated threshold of caring*; fixed-horizon frequentist (or pre-planned sequential) when the analysis must be auditable.
2. **Emotional/customer-first CRO vs data-first CRO** — Wolf: research the customer's emotional drivers before looking at data; the data school (Laja, Kohavi, Aagaard): hypotheses must come from observed behavior/analytics. CONDITION: Wolf's approach is strongest for messaging/positioning-level problems (where analytics shows a leak but not why); the data approach is strongest for funnel mechanics with traffic. Both agree testing validates; they disagree on what generates hypotheses.
3. **Element-level testing vs strategy-level testing** — Aagaard (single-factor, clean attribution) vs Wolf (test whole strategies — "results of single-element tests are hard to analyze, understand and scale") vs Martijn Scheijbeler (big-change tests then decompose). CONDITION: element testing needs traffic; strategy testing when effect sizes must be big enough to detect (piperocket: "test big swings or don't test"). Also MECLABS: prefer factorial/multi-factor when traffic allows.
4. **When to redesign vs test** — Blanks/MacDonald: some pages need rebuilding around customer truth (CRO as "becoming the company"); Sullivan/Kohavi school: iterate with tests. CONDITION: redesign when the page is fundamentally misaligned (message mismatch, broken value prop — Saxo case), test when the page is sound and the question is incremental. MacDonald's rule: test when ≥1K visits/week + reversible + high stakes; otherwise rapid-test or ship.
5. **Significance thresholds** — Georgiev: 95% is not sacred; choose threshold by risk/reward. Kohavi/industry: 95% default, higher for big bets. Goodson: 95% PBB + loss threshold. CONDITION: lower thresholds justified when tests are cheap and opportunity cost high; keep strict thresholds for irreversible or high-stakes changes.

## Conditions (when each methodology is correct)
- **High-traffic product (100K+/variant)**: Kohavi's full toolkit (50/50, CUPED, guardrails, ramp-up) — correct and necessary; his sample-size math is the gate.
- **Mid-traffic (1K-100K/week)**: CRO agency process (Laja ResearchXL → PXL, Massey, Sullivan cycles, Aagaard copy tests) — research-first + prioritization is the right shape.
- **Low-traffic (<1K/week to page)**: no valid small-effect tests possible. Use: qualitative research + evidence stacking (Laursen), rapid testing of concepts (MacDonald), big-swing tests only (piperocket), or ship reversible changes with before/after measurement honestly labeled (MacDonald, Laursen).
- **Org scaling**: Labay/Vermeer taxonomy — decentralized × product-led is the target; CoE bridges feature-led orgs; gates and acceptance criteria are the anti-chaos device.
- **Message-level problems**: Wolf's emotional targeting (research customer language/pains first) — analytics alone cannot tell you why.

## Evidence evaluation
- EMPIRICAL (replicated, documented): peeking inflates false positives (Heap; statistics); SRM prevalence (Kohavi, Vermeer); ~1 in 7-9 tests wins at best (NN/g; DRIP's 20-35% win rates; growwithba's 5-10% vs 30-40% discipline split — HEURISTIC); copy levers (Aagaard's documented multi-site replications of Get/My patterns); low-traffic MDE math (statistical fact).
- FRAMEWORK (widely used, weakly validated): ResearchXL, PXL, LIFT (Widener), ICE/PIE/RICE, MECLABS heuristics, Phase Gate, Flywheel, Emotional Targeting. All are organizing devices; none has published comparative win-rate evidence.
- OPINION/AGENCY CLAIMS (treat as such): Talia Wolf's 10-20X lifts; The Good's 16:1 ROI / 100%+ revenue; CRE's 2-5x; Speero client outcomes. No public methodology behind them.
- HYPOTHESIS: emotional targeting outperforms data-only CRO (Wolf's core claim, untested against control); Bayesian speed advantage (20-80% efficiency claims: Georgiev's ~30% real-world average is the best-documented figure).

## Outliers (worth investigating)
- **Georgiev's risk/reward thresholds**: optimal significance threshold as a business calculation — the industry's 95% ritual is explicitly questioned with math. If the OS can encode cost/benefit inputs, it can compute per-test thresholds.
- **Kohavi's peeking nuance**: "peeking is fine if you won't act on it / to abort harm" — a precision most courses lack; OS should encode the 3-case rule, not "never peek".
- **Wolf's interview questions** ("what problem does our solution eliminate/lessen") — directly reusable by the OS customer-research skills; bridges CRO and JTBD.
- **Labay's Data-to-Action monthly ritual** — the operating model for an experimentation program: 3-month behavioral-metric roadmap per core customer problem.
- **Vermeer's "decisions supported" as the program metric** — counters test-count KPI worship.

## Failure knowledge (what repeatedly doesn't work)
1. Early stopping on significance — #1 cited failure across ALL sources (HubSpot, croforce, statology/Heap, growwithba, DRIP, Sullivan, Kohavi, Georgiev). [HEURISTIC/EMPIRICAL]
2. Cosmetic tests and best-practice cargo culting — button colors, un-researched "best practices" applied cross-context (DRIP newsletter-bar case; SNOCKS 350+ tests). [EMPIRICAL]
3. Opinion/HiPPO-driven changes — overrides destroy program credibility; "experimentation theater" (Atticus Li, adasight, Kohavi). [EMPIRICAL]
4. Optimizing low-traffic/low-leverage pages — tests that cannot resolve (growthlayer MDE rule; Niels Laursen "feeling of rigor without the conditions for rigor"). [EMPIRICAL]
5. Measuring output (tests run, features shipped) instead of outcomes — feature factory; wins that don't ship are "just stories" (adasight, Simon Jackson). [EMPIRICAL]
6. Wrong primary metric — optimizing CTR while revenue flat (Atticus Li); CR up but AOV down (DRIP: optimize RPU). [EMPIRICAL]
7. Skipping tracking QA / SRM — broken instrumentation invalidates everything (Kohavi, Vermeer, croforce). [EMPIRICAL]
8. Discount-first CRO (MacDonald) and trust-element additions without testing (Aagaard privacy policy -18.7%). [EMPIRICAL case studies]
9. Redesigning instead of iterating — full redesigns reset learning and dip conversion for weeks (growwithba). [HEURISTIC]
10. Before/after "tests" without concurrent control — history effects (MECLABS, Scheijbeler). [FRAMEWORK/EMPIRICAL]

## Collision Method sketch (what the Marketing OS should encode)
**Objective**: increase revenue per visitor (RPU/ARPU — DRIP's primary metric) through evidence-ranked, correctly-statted experiments; decide test vs redesign vs ship.
**Prerequisites**: clean tracking (A/A-validated), ability to define primary metric + guardrails, minimum traffic per testable page, stakeholder pre-commitment to decision rules.
**Inputs**: baseline conversion + variance per funnel step, traffic forecast, business cost/benefit inputs (for threshold math), customer research (pains/language/emotions), instrumentation health (SRM).
**Diagnosis** (order): 1) instrumentation check (A/A, SRM) 2) funnel analytics (leak location) 3) qualitative (recordings, surveys, user tests — triangulate ≥2 sources) 4) message/value-prop audit (Aagaard/Saxo lens + Wolf's emotional gap analysis).
**Decision tree**:
- Tracking broken → fix, do not test.
- Page <1K visits/week → no small-effect tests: rapid-test concepts (MacDonald) or evidence-based reversible changes with honest before/after.
- Message mismatch or value prop unclear → fix messaging (copy research, Aagaard/Wolf methods), test the fix as a big swing.
- Friction at a step with traffic → ResearchXL-style research → hypothesis (Sullivan format) → PXL/Evidence-Impact-Effort-Traffic-ROI score → run.
- Testable → pre-register: OEC, MEI (business), sample size (n=(4σ/Δ)² at 95/90, or sequential design), duration ≥ full business cycle, stopping rule.
**Execution**: single primary metric + guardrails; A/A validation; SRM on every test; run to end (or planned sequential boundaries, e.g., AGILE alpha/beta spending).
**Stopping rules**: significance at pre-planned analysis; futility boundary → declare null; harm/guardrail breach → abort (peeking allowed for abort, never for win); inconclusive is a valid outcome.
**Metrics**: RPU primary; win rate 20-40% band as hypothesis-quality diagnostic (below → cosmetic/researchless; above → too safe); decisions-supported per quarter; implementation rate.
**Failure modes to monitor**: peeking wins, SRM, cosmetic tests, metric ≠ revenue, stakeholder override, output-KPI programs, unshipped wins.
**Conditions**: this is the mid/high-traffic method; low-traffic segments use the qualitative path; org structure determines whether a CoE/gate process is needed (Labay/Vermeer).
**Confidence**: T1 for stats rules (Kohavi, Georgiev, Goodson-Microsoft), T1/T2 for process frameworks (Laja, Sullivan, Labay), T2 for copy/message heuristics (Aagaard replications), T3 for agency ROI claims.
**Key sources**: Kohavi pitfalls papers; Georgiev's book; Goodson/VWO SmartStats + Microsoft optional-stopping paper; Laja ResearchXL/PXL; Sullivan hypothesis + failure decks; Aagaard case studies; growthlayer MDE rule; adasight/Atticus Li program failures; Labay/Vermeer org taxonomy.
