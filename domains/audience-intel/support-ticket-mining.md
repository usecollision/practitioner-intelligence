---
practitioner: Kromatic (Real Startup Book) + Koji + Pelin + Intercom + Airbnb engineering
role: support-data mining methods and case studies
type: researcher|practitioner|vendor
confidence: T1 (Kromatic method) / T2 (vendor claims)
domains: [support-ticket-mining]
verified: 2026-08-15
sources_checked: 6
---
# Support Ticket Mining — Panel

## Beliefs
- "Every customer support ticket is a free research interview your team has already paid for" (Koji).
- The goal is to discover what customers actually struggle with, not test a hypothesis you already hold — findings often challenge internal assumptions (Kromatic).
- Support data is one input, not the whole picture: it only captures existing customers of the existing product; novel pains and churned-customer reasons rarely appear (Kromatic).

## Processes (Kromatic)
1. Export ≥500 interactions over 3–6 months with metadata (date, segment, product area, resolution time, satisfaction).
2. Hand-read 50–100 tickets; draft 8–15 top-level categories (billing, onboarding, feature requests, bugs, how-to, account access, performance). Treat existing platform tags as a starting point, not truth. Reconcile AI-drafted taxonomy with your own read.
3. Classify the full sample (AI-assisted); allow ONE taxonomy revision halfway, then freeze (taxonomy drift delays decisions).
4. Build frequency × severity × ARR matrix; weight by unique-customer count and account value, not ticket count.
5. Output top-5 categories as prioritized hypotheses (frequency, severity, root cause); decide fix type: product / documentation / onboarding.

## Case evidence
- Airbnb: Elasticsearch trend dashboard, Fourier-smoothed scoring caught a search-hiding regression, reduced ticket volume ~3% (T2, Airbnb engineering).
- Intercom: cross-functional "swarms" mine conversation data → operational tools and product features (T2).
- Productboard: 5-step tag → consolidate → categorize → analyze → align, used by 600+ orgs (T2).
- Pelin: iOS crash fix cut support volume 60%; billing confusion → near-zero tickets post-fix (T2, vendor).

## Decision rules
- IF fewer than ~500 tickets in window THEN skip mining; interview instead (insufficient signal).
- IF a theme appears in <5–10% of tickets THEN do not treat as priority (Koji threshold).
- IF a ticket is a how-to question THEN classify operational; IF it's "why is X buried/confusing" THEN classify product insight. Never conflate (Koji).
- IF a single category dominates volume THEN make it the next focus area and decide product vs docs vs onboarding fix.
- IF one enterprise customer screams about an issue THEN log it, but wait for the 5–10% pattern before acting (loudest-customer trap).
- IF mining multiple channels THEN decide merge vs separate; Twitter complainers rarely file tickets — single-channel reads miss whole complaint modes (Kromatic).

## Failure modes / biases (Kromatic, T1)
- Squeaky-wheel bias: weight by unique customers, not ticket count.
- Agent interpretation bias: re-classify with your own taxonomy.
- Recency bias: sample evenly across the window.
- Survivor bias: cross-check with exit surveys/cancellation reasons.
- No tagging system / support isolated from product / reacting to one-off requests / ignoring qualitative context (Pelin mistakes).

## Cadence (Koji 90-day rhythm)
Weekly 15-min top-5 tag scan; monthly 1-hour thematic analysis → top 3 themes to leadership; quarterly half-day full analysis for roadmap; annual multi-year theme tracking.

## Sources
1. Kromatic — Customer Support Analysis | https://kromatic.com/real-startup-book/1-generative-market-research/data-mining/customer-support-analysis | tier 1 | 2026-08-15
2. Koji — Support Ticket Analysis | https://www.koji.so/docs/support-ticket-research-analysis | tier 2 | 2026-08-15
3. Pelin — Zendesk Product Insights | https://www.pelin.ai/blog/zendesk-product-insights | tier 2 (vendor) | 2026-08-15
4. Intercom — From swarms to product | https://www.intercom.com/blog/from-swarms-to-product-turning-customer-signals-into-scalable-features/ | tier 2 | 2026-08-15
5. Airbnb Engineering — Monitoring customer issues at scale | https://medium.com/airbnb-engineering/how-airbnb-manages-to-monitor-customer-issues-at-scale-b883301ca461 | tier 2 | 2026-08-15
