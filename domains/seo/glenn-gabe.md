---
practitioner: Glenn Gabe
role: Founder / SEO Consultant
company: G-Squared Interactive
type: practitioner|analyst
confidence: T1
domains:
  - SEO
  - Algorithm forensics
verified: 2026-08-14
sources_checked: 3
---

## Beliefs
- Drops from broad core updates are NOT always quality problems — they split into three causes: relevancy adjustments, intent shifts, and site-level quality problems, often in combination (FACT, his core taxonomy).
- Google evaluates a site *overall* (content, UX, ads, affiliate setup, technical quality), not just content quality — he has argued this since the Panda era (OPINION backed by Mueller's 2021 statement).
- There is never one smoking gun in a core update drop — "there's typically a battery of them" (EMPIRICAL, from large-scale client work).

## Principles
- Diagnose before acting: never nuke content or revamp the site until you know the cause of the drop (HEURISTIC).
- Control what you can: relevancy adjustments and intent shifts are largely outside your control; site quality is not (FRAMEWORK).
- Recovery is a long game: heavy quality-driven drops typically only recover at the next broad core update, sometimes several updates / a year+ (EMPIRICAL, he's seen year-long recoveries).

## Frameworks
- **Delta Report**: compare queries/landing pages before vs after the update to see what actually dropped (FRAMEWORK — automatable via Search Console API + Analytics Edge).
- **Relevancy Adjustment / Intent Shift / Quality Problem triage**: the cause-classification for any core update drop (FRAMEWORK).
- **Kitchen Sink remediation**: surface ALL potential quality problems and fix as many as possible — no cherry-picking (FRAMEWORK).

## Processes
1. Run a delta report to identify the queries and landing pages with the biggest drops.
2. Classify each cluster: relevancy adjustment (content no longer relevant), intent shift (SERP now rewards a different content type), or quality problem (important queries + relevant content still losing).
3. If quality: objectively audit the whole site through the lens of the update; build a plan covering content, UX, ads, affiliate setup, technical issues.
4. Implement the right changes for users and KEEP them in place long-term. No short-term whack-a-mole testing.
5. Optionally run user studies to understand quality issues from the user's perspective.

## Heuristics
- If the losing queries are unimportant to the business, a relevancy adjustment may be a non-event (HEURISTIC).
- If queries dropping are important AND you have relevant content → suspect quality problems (HEURISTIC).
- Recent changes (1-2 weeks before the update) are almost never the cause — updates evaluate extended periods (FACT from Google + his experience).
- Short-term tests of specific changes will fail to show recovery; that doesn't mean the changes were wrong (HEURISTIC).

## Tactics
- Automate delta reports via Search Console API (TACTIC).
- Surface every quality issue including UX barriers, aggressive ads, deceptive affiliate setups, popups (TACTIC).
- Run user studies through the lens of broad core updates (TACTIC — he notes most sites say they'll do this and never do).

## Tools
- Google Search Console (API), Analytics Edge, custom delta-report scripts.

## Inputs
- Pre/post update traffic and ranking data by query and landing page.
- Knowledge of update dates and scope (he tracks rollouts precisely).

## Outputs
- Cause-classified drop analyses; remediation plans; blog post documentation of cases (e.g., March 2024 Core Update case study).

## Metrics
- Traffic and clicks by query/landing page before vs after update; recovery timing vs subsequent core updates.

## Decision rules
- Drop + losing queries irrelevant to business → likely relevancy adjustment → minimal action (maybe create more relevant content) (DECISION RULE).
- Drop + SERP now shows different content types for your queries → intent shift → check if you have content for the new intent; build proactive multi-intent coverage (DECISION RULE).
- Drop + important queries + relevant content → quality problem → kitchen-sink remediation, expect recovery only at a future core update (DECISION RULE).
- Do NOT roll back good changes after a few weeks because no recovery yet — Google evaluates long-term (DECISION RULE).

## Failure modes
- Cherry-picking fixes — sites stay in Google's "gray area" and never recover (warned against).
- Treating every drop as a quality problem — unnecessary site destruction.
- Short-term testing of broad-core-update recovery — impossible by design; whack-a-mole behavior.
- Expecting immediate recovery — recovery requires another update rollout, or several.

## Contrarian beliefs
- Core update drops are often NOT your fault or your site's fault (relevancy/intent shifts) — against the industry default of self-blame and content deletion (OPINION).

## Examples
- "A tale of four tremors, reversals" March 2024 Core Update case study (EXAMPLE).
- Celebrity article from 2-3 years ago dropping on relevance (EXAMPLE); review sites losing to ecommerce sites on intent shift (EXAMPLE).
- Client sites taking over a year to recover after significant improvements across content/UX/ads/affiliates/technical (EXAMPLE).

## Conditions
- Works for content/publishing/media sites with meaningful organic footprint; anywhere delta reports are possible via GSC.
- Applies when the site owner can wait for the long game (recovery windows of months).

## Limitations
- Cannot predict recovery timing; cannot test changes in isolation against core updates; diagnosis is probabilistic even with delta reports.
- Delta reports need sufficient traffic volume to be meaningful (small sites lack signal).

## Sources
1. "Google's Broad Core Updates And The Difference Between Relevancy Adjustments, Intent Shifts, And Overall Site Quality Problems" | https://www.gsqi.com/marketing-blog/google-broad-core-updates-difference-between-relevancy-adjustments-intent-shifts-overall-site-quality/ | primary practitioner blog | tier 1 | 2026-08-14
2. "Google's Broad Core Algorithm Updates: Important Points And Frequently Answered Questions" | https://www.gsqi.com/marketing-blog/google-broad-core-updates-important-points-and-frequently-answered-questions/ | primary practitioner blog | tier 1 | 2026-08-14
3. "Google March 2024 Core Update Case Study: A tale of four tremors, reversals..." | gsqi.com (referenced in search results) | primary practitioner blog | tier 1 | 2026-08-14
