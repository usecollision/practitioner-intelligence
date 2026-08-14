---
practitioner: Peep Laja
role: Founder, CXL (CXL Institute / Speero, ex-CXL Agency)
company: CXL
type: practitioner|founder|educator
confidence: T1
domains:
  - CRO
verified: 2026-08-14
sources_checked: 5
---

## Beliefs
- CRO is a research discipline first, a testing discipline second: "after doing conversion research, what to test is never a problem (usually, you've identified 50-150 issues)" [1,2]
- Ideas derived from opinion have less chance of success than ideas derived from data — opinions are the #1 waste in CRO [3]
- The same research process works across every business model: B2B/B2C, SaaS/ecommerce/leadgen/affiliate — "industry-agnostic" [2]
- Beginners worry about what to test; the problem is never a lack of test ideas, it's lack of evidence about which ones matter [1]
- Prioritization must be objective and based on facts, not opinion, or teams waste "countless debates" on which test to run first [3]

## Principles
- Research before hypothesis: every hypothesis must trace to observed evidence [1,2]
- Triangulate: strongest hypotheses converge multiple research methods on the same friction point (analytics + recordings + survey) [1]
- Test the behavior change, not the element: bucket items by action type before prioritizing [1]
- "What to test" is downstream of research; testing lists without research are beginner traps [1]

## Frameworks
- **ResearchXL™** (his named framework): 6 data-gathering steps → master issue sheet → 5 action buckets → scoring [1,2]
  - Steps: 1) Heuristic analysis 2) Technical/analytics instrumentation check 3) Web analytics analysis 4) Mouse tracking/recordings 5) Visitor polls/surveys 6) User testing (task-based, think-aloud, full funnel)
  - Buckets: **Test** (big behavior-shift opportunities) / **Instrument** (fix tracking/tags) / **Hypothesize** (problem known, solution unclear → brainstorm test plans) / **Just Do It** (obvious low-effort fixes) / **Investigate** (needs more digging)
- **PXL prioritization** (his framework, successor to ICE/PIE): binary weighted scoring, max objectivity [3]
  - Criteria: above-the-fold? (2/0 — bigger impact) · high-traffic page? · noticeable in <5s? (2/0 — if colleagues can't see the diff in 5s, expect inconclusive) · adds/deducts value? · discovered via user testing? · via qualitative feedback/survey? · supported by heatmaps? · from digital analytics? (data-backed items weighted up)
  - Ease-of-implementation scored in bracketed estimates with the test developer in the room
- Craig Sullivan's hypothesis template (which he credits and standardized): "We believe that doing [A] for people [B] will make outcome [C] happen. We'll know this when we see data [D] and feedback [E]." [1]

## Processes
- 6-step research → categorize into 5 buckets → 1-5 star score (Ease of Implementation × Opportunity Score) → 7-column master spreadsheet → write hypotheses → prioritize with PXL → run tests [1]
- Iterate: research findings feed a rolling pipeline of hypotheses, not one-off audits [1,2]

## Heuristics
- 1-5 scoring: 1 = minor issue, 5 = critically important; the two inputs are ease of implementation and opportunity (subjective lift estimate) [1]
- If a change isn't noticeable in 5 seconds, don't expect it to change behavior [3]
- High-traffic pages with above-the-fold changes = highest expected value [3]

## Tactics
- Analytics health check before trusting any data (tagging, events, instrumentation) [1,2]
- Poll website visitors + survey existing customers (two different populations, two different answers) [1]
- Task-based user testing: specific task, broad task, full funnel [1]
- Customize PXL to the business (e.g., add SEO impact criteria if traffic is SEO-driven) [3]

## Tools
- Analytics (GA-class), session recording/heatmap tools (classic: FullStory/Crazy Egg-class), survey tools, user testing platforms, A/B platforms; PXL spreadsheet [1,2,3]

## Inputs
- Funnel drop-off data, instrumentation status, recordings, poll/survey verbatims, user-test observations — before any test design [1,2]

## Outputs
- Master issue/action sheet, prioritized test roadmap, documented hypotheses with evidence tags [1,3]

## Metrics
- Conversion rate of tested pages; wins/losses per test; but the real output metric he optimizes for is evidence-backed hypothesis quality (win rate rises when research is done) [2]

## Decision rules
- **Test** it → big opportunity to shift behavior exists [1]
- **Instrument** → the problem is missing/incorrect data, not page design [1]
- **Just Do It** → fix is easy/obvious; don't waste a test slot on no-brainers [1]
- **Hypothesize** → problem known but no clear solution: run brainstorm → test [1]
- **Prioritize** → score by ease × opportunity, then weight by data provenance and noticeability; drop opinion-only ideas [1,3]
- Do not test changes users can't notice in 5 seconds [3]

## Failure modes
- Testing from listicles ("101 things to test") instead of research — breeds random, low-value tests [1]
- Opinion-driven ideas: "you won't waste any time discussing ideas that are unfounded or based purely on opinion" [3]
- Inconclusive tests caused by unnoticeable changes [3]
- Unvalidated analytics — garbage-in: "analytics health check" is step 1 for a reason [1,2]

## Contrarian beliefs
- Most CRO "best practice" listicles are noise; structured research beats creativity [1]
- Prioritization frameworks should be quantitative and weighted, not gut rankings (ICE/PIE too crude) [3]

## Examples
- Speero/CXL Agency practice: research projects aim to "identify optimization opportunities by uncovering what really matters" before any test [3]
- His claim: ResearchXL "proven to work across industries and business models" over 3+ years of use [2]

## Conditions
- Works best with: traffic enough to test (PXL assumes testable pages), access to analytics + qualitative tools, a developer for effort estimates [1,3]
- ResearchXL is heavier than needed for a 2-person startup landing page; scale steps to budget [2]

## Limitations
- ResearchXL + PXL assume a testing program with enough traffic; on low-traffic pages the research may surface issues you cannot test (then: fix via "Just Do It" or redesign) [1]
- PXL scores are still subjective at their core (opportunity score is "subjective opinion"), just disciplined subjectivity [3]

## Sources
1. How to Create a CRO Process | cxl.com/conversion-rate-optimization/how-to-create-a-cro-process-by-peep-laja/ | article | 1 | 2026-08-14
2. How to Come Up with More Winning Tests Using Data (ResearchXL) | cxl.com/blog/how-to-come-up-with-more-winning-tests-using-data/ | article | 1 | 2026-08-14
3. PXL: A Better Way to Prioritize Your A/B Tests | cxl.com/blog/better-way-prioritize-ab-tests/ + speero.com/post/how-to-prioritize-your-a-b-tests-ideas | article | 1 | 2026-08-14
4. CRO Research: How to Find What to Test Before You Run a Single Experiment | mida.so/blog/cro-research-find-what-to-test | secondary summary of ResearchXL | 3 | 2026-08-14
