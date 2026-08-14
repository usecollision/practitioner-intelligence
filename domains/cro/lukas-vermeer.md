---
practitioner: Lukas Vermeer
role: Director of Experimentation, Booking.com (ex-Microsoft)
company: Booking.com
type: practitioner|operator|educator
confidence: T1
domains:
  - experimentation
verified: 2026-08-14
sources_checked: 4
---

## Beliefs
- "Speed is not velocity": experimentation reduces product-development speed but increases product-development velocity — fewer features that don't add value, more learning about which features do [1]
- Customers "only care about things that bring value to them; they only care about your product development velocity" — ticket counts and shipped features are speed, not progress [1]
- Experimentation is a cultural and infrastructural capability that must be democratized: at Booking.com 2,000+ people run experiments on an in-house platform [3]
- Everyone who tests for data-quality problems finds them: "like coronavirus, if you don't test for it you don't have it" [3]

## Principles
- The value-investment cycle must keep turning: each turn of the flywheel justifies continued funding for the next [2]
- Statistical/data-quality literacy is the bottleneck, not tooling: SRM (Sample Ratio Mismatch) is "such a simple method to test for a wide range of data quality issues… I really see no reason for anyone not to do this" [3]
- Teach statistics through stories so non-statisticians can act [4]

## Frameworks
- **A/B Testing Flywheel** (with Fabijan, Arai, Dmitriev; Microsoft/Outreach/Booking): 5 steps of the value-investment cycle — run more A/B tests → support more decisions → [invest in processes/capabilities] → reduce the cost and increase the quality of testing → more tests…; each turn requires investment in software-development processes; track metrics per step to prove momentum [2]
- **Experimentation Evolution Model** (co-author, 2017): Crawl → Walk → Run → Fly stages of program maturity [2]
- **Org taxonomy for experimentation teams** (with Ben Labay & Nils Stotz, 2025): centralized/decentralized × product-led/feature-led quadrants — "the optimal situation described in Lucas's flywheel paper" is decentralized + product-led (Booking, Uber) [4]

## Processes
- Democratized experimentation at Booking: in-house platform ("Experiment Tool"), 2,000+ experimenters, platform group provides tooling + support; his team aligns platform roadmap with product direction [3]
- Flywheel operation: measure momentum metrics, invest in processes (tooling, role models, executive sponsorship, transitioning experts to new orgs) to keep the wheel turning [2]

## Heuristics
- Always run the SRM check on every test — it catches caching, redirect, bot, and randomization bugs [3]
- Run experiments to support decisions, not to validate decisions [2]
- More experiments is only valuable if they support decisions — the flywheel's top is "more decisions supported by tests" [2]

## Tactics
- Publicly evangelize data-quality checks (his signature talk: "one neat trick… SRM") [3]
- Grow by moving experienced experimenters (especially at exec level) into new teams [2]
- Use role-model teams to onboard newcomers [2]

## Tools
- In-house experimentation platform (Booking), standard testing stack; his publications serve as the community playbook [2,3]

## Inputs
- Program maturity stage (Crawl/Walk/Run/Fly), organizational structure, decision cadence, platform data quality status [2,3]

## Outputs
- The Flywheel model + Evolution Model papers, talks (Speed is not velocity; SRM), taxonomy paper, industry education [1,2,3,4]

## Metrics
- Decisions supported by tests, tests per team, time-to-decision, SRM/pipeline health, momentum metrics per flywheel step [2,3]

## Decision rules
- When a program stalls → invest in the flywheel step that is weakest (tooling, role models, exec sponsorship, expert movement) before adding more tests [2]
- When tests can't be trusted → add SRM + A/A checks before interpreting anything [3]
- When deciding what to build → ship only what experiments show adds value; "running into a wall faster is not a recipe for product success" [1]
- When scaling → match program design to org structure (decentralized + product-led is the ideal; use a CoE to transition feature-led orgs) [4]

## Failure modes
- Confusing speed with velocity: shipping features that don't add value [1]
- Not testing for SRM: "once people start testing for it they start finding it" — undetected data-quality failures invalidate results silently [3]
- Centralized bottleneck structures that cap throughput (his taxonomy's "Waterfall Trap") [4]
- Programs that stop investing in the flywheel and lose momentum [2]

## Contrarian beliefs
- The unit of experimentation success is decisions supported, not tests run [2]
- Statistical rigor (SRM) is a democratic, non-negotiable habit, not a data-science specialty [3]

## Examples
- Booking.com: 2,000+ experimenters, 15 years, in-house platform [3]
- Microsoft: 20,000+ A/B tests/year across products (cited in his flywheel paper) [2]
- Co-authored taxonomy with Labay — the two research streams (org design + stats) converge [4]

## Conditions
- The flywheel assumes orgs with recurring testing cadence and product teams that can invest in process [2]
- Democratization model fits large orgs (Booking/Microsoft scale); small teams need only the SRM habit [3]

## Limitations
- Flywheel metrics are process metrics; the paper is case-study-based, not quantified ROI [2]
- "2,000+ people" scale guidance doesn't transfer to startups — his SRM talk is his most portable artifact [3]

## Sources
1. Speed is not velocity | lukasvermeer.medium.com/speed-is-not-velocity-7c95bec715ef | essay | 1 | 2026-08-14
2. Flywheel to Fly: Kickstarting and Growing the A/B testing Momentum at Scale | lukasvermeer.nl/publications/papers/2021/10/27/flywheel-to-fly... | paper | 1 | 2026-08-14
3. TLC: Sample Ratio Mismatch (SRM) with Lukas Vermeer | youtube.com/watch?v=CJ9KinpJplg | talk transcript | 1 | 2026-08-14
4. Sideshow EP4 (Labay/Vermeer/Stotz taxonomy) | speero.com/post/sideshow-ep4 | podcast transcript | 1 | 2026-08-14
5. Keynote speaker page | lukasvermeer.nl/speaking/ | 1P | 1 | 2026-08-14
