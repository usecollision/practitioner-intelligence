---
practitioner: Demand-validation operators (ProofEngine, IdeaCrystal, Demand Discovery)
role: startup demand-validation practitioners and platforms
company: ProofEngine Studio; IdeaCrystal; Demand Discovery (AI validation platform)
type: practitioner|operator|analyst
confidence: T2
domains:
  - demand-analysis
verified: 2026-08-15
sources_checked: 5
---

## Beliefs
- "Interest is cheap, and stated intent is unreliable" — real demand validation is a cross-check of multiple signals pointing the same direction (IdeaCrystal) (T2).
- Behavior over opinion: search behavior, competitor traction, pricing evidence, and customer voice beat surveys and "would you use this?" questions (IdeaCrystal; Demand Discovery) (T2).
- Money-on-the-table is the strongest demand signal: pre-sale, LOI, deposit, pilot (ProofEngine) (T2).
- Validation is about making it difficult to say yes without evidence (IdeaCrystal) (T2).

## Principles
- Signals are only meaningful in combination: strong search + weak buyer intent ≠ same market as low search + high contract value (IdeaCrystal) (T2).
- Workarounds are the classic latent-demand signal: spreadsheet-based DIY solutions mean people feel the pain and pay with time (ProofEngine) (T2).
- Escalate cost with confidence: start with free signals (search, reviews, communities), spend money only when cheap signals converge (IdeaCrystal) (T2).
- Parallel experiments beat sequential: three independent data points are much harder to explain away than one (ProofEngine) (T2).

## Frameworks
- 7-signal demand framework: search demand, founder discussions (Reddit/HN/Indie Hackers), startup launches (Product Hunt/YC), hiring signals (job postings), developer ecosystem (GitHub/npm/API), buyer outreach responses, landing page conversion (Demand Discovery) (T3).
- Intent classification: informational vs investigational vs transactional queries — high transactional+investigational = strong signal; high informational + low transactional = awareness without purchase intent (ProofEngine) (T2).
- Demand scoring: search volume, trend direction, competitor review complaints, social mention frequency, workaround prevalence, transactional % — scored low/med/high, summed (ProofEngine) (T2 heuristic; cutoffs T3).
- Validation experiment ladder: landing page/waitlist → pre-sale/LOI → concierge MVP → crowdfunding → competitor-audience ads (ProofEngine) (T2).

## Processes
1. Write go/no-go criteria BEFORE gathering data (existing skill; IdeaCrystal) (T2).
2. Search demand: keyword set, 2+ volume tools (ratios not absolutes), intent split, 3-year direction (existing skill; ProofEngine) (T2).
3. Proxy signals: review velocity on G2/Capterra/App Store (normalized by product age), job postings, community growth, workaround prevalence (existing skill; ProofEngine) (T2).
4. Behavioral depth: what questions people ask, context of mentions, platform diversity (Spate-adjacent practice) (T2).
5. Confidence-weight the verdict; define the no-go evidence explicitly (existing skill) (T2).
6. Cheapest de-risking test for the biggest unknown: usually a pre-sale or landing page with pricing (ProofEngine) (T2).

## Heuristics
- Crowdfunding: funded in first 48h = extremely strong demand (audience covers goal); funded by day 15-20 = solid cold demand (ProofEngine) (T2).
- 2-star/3-star reviews of competitors are your target customer list (ProofEngine) (T2).
- Competitor marketing spend ≠ customer demand — don't confuse them (existing skill) (T2).

## Inputs
Product concept, target market, competitor list, keyword set, access to volume tools, review sites, communities.

## Outputs
Demand estimate, evidence table with confidence levels, go/no-go verdict, cheapest-next-test recommendation, re-check date.

## Metrics
Signal convergence count; transactional % of search; review velocity slope; pre-sale/LOI conversion; landing page conversion with pricing shown.

## Decision rules
- IF no written go/no-go criteria THEN write them before any data gathering (IdeaCrystal, T2).
- IF only one signal says go THEN require 2+ independent signals converging (IdeaCrystal/ProofEngine, T2).
- IF transactional/investigational share <10% of volume THEN treat as awareness, not demand; test willingness to pay (ProofEngine, T2).
- IF workarounds are widespread THEN latent demand is strong — escalate to a money test (ProofEngine, T2).
- IF evidence is only stated interest THEN run the cheapest money test (pre-sale/LOI/landing page with price) before build (ProofEngine, T2).
- IF signals conflict THEN dig into the specific conflict rather than averaging (IdeaCrystal, T2).
- IF validation cannot produce a "no" THEN the process is theater — add kill criteria (existing skill + IdeaCrystal, T2).

## Failure modes
- Asking people whether they'd use it and calling that proof (IdeaCrystal) (T2).
- Validating the problem but not willingness to pay (Zimt: "80% want it" vs 0% pay $50/mo) (T2).
- Reading one year of Trends as growth (seasonality as demand) (existing skill) (T2).
- Sequential experiments that take as long as building (ProofEngine) (T2).
- Cherry-picking the signal that confirms bias (ProofEngine scoring exists to prevent this) (T2).

## Contrarian beliefs
- Landing page conversion matters more when paired with quality traffic and a clear paid action; ad CTRs only matter if the economics behind them work (IdeaCrystal) (T2).

## Conditions
Works pre-build and pre-PMF; fails when there is no channel to observe (brand-new behavior with no search vocabulary — then use problem-language mining in communities and interviews).

## Limitations
All volume tools are models with error (ratios over absolutes); review velocity undercounts; demand scores are heuristics, not measurements.

## Sources
1. ProofEngine — 7 Demand Validation Experiments | blog.proofengine.studio/demand-validation-experiments | T2 | 2026-08-15
2. IdeaCrystal — How to Validate Startup Demand the Right Way | ideacrystal.com/en/blog/how-to-validate-startup-demand | T2 | 2026-08-15
3. Demand Discovery — platform framework (7 signals, demand scoring) | demanddiscovery.ai | T3 | 2026-08-15
4. UnbuiltLab — Demand Signal Mining framework | unbuiltlab.com/blog/how-to-validate-startup-ideas-complete-2024-framework.html | T3 | 2026-08-15
5. IdeasDB — signal feed practice (Reddit pain points, keyword trends) | getideasdb.com | T3 | 2026-08-15
