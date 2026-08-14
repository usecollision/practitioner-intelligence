---
practitioner: Craig Sullivan
role: Experimentation Consultant, Optimise Or Die (ex-Optimal Visit "Optimiser in Chief", ex-Belron Group eBusiness Manager)
company: Optimise Or Die Ltd (UK)
type: practitioner|educator
confidence: T1
domains:
  - CRO
  - experimentation
verified: 2026-08-14
sources_checked: 5
---

## Beliefs
- Most CRO failure is process failure: wrong analytics setup, wrong inputs, badly designed tests, self-stopped tests, missing QA [2,5]
- "Less bullshit, more truth in meetings" — decisions come from mined data, not opinions [2]
- Testing is a scientific method for optimizing "growth or delight"; he claims 500+ people trained and £100M of "lost revenue" found with one lightweight research technique (Belron) [5]
- Mass experimentation raises real ethical questions; democratized A/B tooling means "hundreds of millions of experiments run on people" without ethical training — the industry has an "ethical gap" [3]

## Principles
- Research before testing, always: analytics health checks and user research inform where to test [2,5]
- Test for at least two business/purchase cycles (whichever is longer); continue to the predetermined end date regardless of early results [2,4]
- Decide on error-bar separation and sample size, not confidence percentages; "putting too much faith in confidence values" is a top mistake [2,4]
- QA everything, every device: "pre-flight checks to avoid broken tests" [2,4]
- Steal proven patterns: use published form/UX pattern libraries instead of rediscovering form truths ("steal off the internets") [1]

## Frameworks
- **Hypothesis format** (his, adopted industry-wide — credited by Peep Laja and cited in CXL curriculum and by agencies): "We believe that doing [A] for people [B] will make outcome [C] happen. We'll know this when we see data [D] and feedback [E]." [1]
- **"18 Simple Ways to F\*\*\* up Your AB Testing"** (Measurecamp 2014): the negative-knowledge canon — analytics health check first, understand device/traffic mix, research before testing, prioritize high-opportunity/low-cost tests with a "money model", pre-flight QA, don't self-stop, run full cycles, judge on error bars + sample size [2]
- **Pizza analogy**: explaining testing ROI to senior management/budget holders [2]
- Belron methodology (enterprise CRO at scale) + a CRO maturity model [2,5]

## Processes
- Analytics health check → mine GA for funnel blocks/device issues (multi-dimensional segmented funnels, his grid tool) → lightweight research (surveys, interviews, usability) → prioritize high-opportunity tests → pre-flight QA → run full cycles → decide on error bars → document [2,4,5]
- Form teardowns as a repeatable public practice: error messages, field necessity, mobile keyboard types, paste-disabled fields, "Title" fields, overlaid errors, errors persisting after fix [1]

## Heuristics
- "Confirm email (with paste disabled) is unnecessary" [1]
- Remove unnecessary fields/options; fix mobile input types (phone field must open number keyboard) [1]
- Stop a test only at the predetermined end; early "wins" at arbitrary confidence are illusions [2,4]
- If an error message pattern is broken, users blame the form, not the typo [1]

## Tactics
- Run A/A tests to validate tools and instrumentation before trusting results [5]
- Mine session replays for "emotion, frustration, friction" that analytics misses [2]
- Cross-channel optimization (web + contact centers) [2]
- Use pattern libraries for forms (Baymard-class research) [1]

## Tools
- Google Analytics (heavy GA mining, custom grids), session replay/recording tools, user testing services, A/B platforms [2,5]

## Inputs
- Instrumentation status, device/traffic mix, funnel data, qualitative research, business-cycle calendar (purchase cycles) [2,4,5]

## Outputs
- Teardowns ("Form Teardown of the Week"), conference talks/decks, training (500+ people), public failure-mode lists [1,2,5]

## Metrics
- Conversion rates, funnel step completions per segment/device, error-bar separation as the decision statistic [2,4]

## Decision rules
- Don't test until analytics is healthy and you know the device mix [2,4]
- Prioritize by opportunity × cost, backed by a "money model" (what is a conversion worth) [2]
- When a test looks significant early → keep running to the predetermined end date [2,4]
- When results are ambiguous → decide on error-bar separation and sample size, not confidence % [2,4]
- When you can't test (low traffic) → use lightweight research + pattern libraries instead [2]

## Failure modes
- Stopping tests early at arbitrary confidence levels [2,4]
- Trusting confidence values over error bars/sample sizes [2,4]
- Testing without analytics health check (broken instrumentation) [2,5]
- Copying competitors instead of testing informed by your own analytics [4]
- No QA across devices → browser/device-specific bugs invalidate results [2,4]
- Sequential before/after "tests" polluted by history effects [4]
- Testing individual channels in isolation [2]

## Contrarian beliefs
- The industry's statistical literacy is dangerously low; most "significant" results in practice are not [2,4]
- Experimentation without ethics is manipulation; north-star metrics can be a problem, not a solution [3]

## Examples
- Belron: global optimization program, hundreds of tests, £100M lost-revenue figure from one measurement technique [5]
- Hyperoptic form teardown (2024) — public teardown series showing his criteria in action [1]

## Conditions
- His method assumes mid/large-traffic sites (his practice was enterprise: Belron, utilities, broadband) [1,5]
- The full-cycle rule assumes you can identify your business cycles [2]

## Limitations
- His teardown heuristics are judgment calls, not tested evidence (they're framed as "what we'd check", not "proven lifts") [1]
- Two-cycle minimums are expensive for low-traffic sites; he implicitly accepts that by directing low-traffic teams to research instead [2]

## Sources
1. Hyperoptic form teardown + Crimes of UX #10 | linkedin.com/posts/craigsullivan_* (2 posts) | teardowns | 1 | 2026-08-14
2. 18 Simple Ways to F\*\*\* up Your AB Testing | slideshare.net/slideshow/measurecamp-18-simple-ways-to-f-u/32891967 | deck | 1 | 2026-08-14
3. #280 Ethical experimentation | uxpodcast.com/280-experimentation-ethics-craig-sullivan/ | podcast | 2 | 2026-08-14
4. Myths, Lies and Illusions of AB and Split Testing | slideshare.net/slideshow/myths-lies-and-illusions-of-ab-and-split-testing/43774494 | deck | 1 | 2026-08-14
5. NUX6 "AB Testing and UX — a love story" description | slideshare (NUX6 talk) | deck description | 1 | 2026-08-14
