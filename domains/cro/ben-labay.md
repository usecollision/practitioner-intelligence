---
practitioner: Ben Labay
role: CEO, Speero (ex-CXL Agency leadership)
company: Speero
type: practitioner|founder|operator
confidence: T1
domains:
  - experimentation
  - CRO
verified: 2026-08-14
sources_checked: 4
---

## Beliefs
- Experimentation is "a superior operating system for growing a business. It's not just a tool; it's a way of working" [4]
- Experimentation is the tool for testing opportunities and ideas — "not the end goal in itself"; the goal is business outcomes [3]
- Program maturity is an organizational-structure question, not a tooling question: "The maturity of your program isn't just about the tools you use; it's about how your organization is structured and how teams work together" [4]
- The best programs combine testing with deep observational data + UX research/customer feedback — data to action, not test-count [3]

## Principles
- Define every step, owner, and decision point in the testing program or it slows down [1]
- Gates are one-way streets: once a decision passes a gate, no going back — "This is how you enforce discipline and speed up decision-making" [1]
- Standardize acceptance criteria per gate/phase, or "you'll have complete chaos" [2]
- Capture and share knowledge systematically or learnings die (Zapier → Slack "growth-insights"; Airtable repository) [2]
- Scale experimentation to match org structure — GM, functional, product, project models each need different plays [2]

## Frameworks
- **Test Phase Gate Framework** (Speero's flagship blueprint): 5 phases, each with critical questions + required deliverables + a Gate (one-way decision point) [1]
  1. Collecting Data & Insights — "What are we learning?"
  2. Turning Insights into Business Cases — "Is this worth testing?"
  3. Turning Business Cases into Study Designs — "How will we test it?"
  4. Planning & Building — "Are we ready to launch?"
  5. Testing, Launching & Reporting — "What did we conclude?"
  - A strong test plan answers: What will you do? Why? Who owns what? What is the undeniable conclusion?
- **XOS (Experimentation Operating System)**: knowledge-management artifact (Airtable/Effective Experiments/Jira worst case) + rituals; core ritual = **"Data to Action" workshop** — a monthly loop that sets a (typically 3-month) roadmap focused on moving (typically behavioral) metrics around a core customer problem: "bet taking. And strategy. And velocity." [1,3]
- **Org taxonomy for experimentation teams** (paper with Nils Stotz & Lukas Vermeer, 2025): 4 quadrants [4]
  - Centralized × Product-led = "Default Startup" (fine while small)
  - Decentralized × Product-led = "Hyper-Growth Ideal" (Booking, Uber — teams experiment autonomously within the product lifecycle)
  - Centralized × Feature-led = "Waterfall Trap" (validation theater — experimentation used to rubber-stamp decided builds)
  - Decentralized × Feature-led = "Wild West" (disconnected tests, no unifying model, no learning)
  - **CoE (Center of Excellence)** = bridge from bottom to top-right; needs a "cheerleader" and an "operator"; risks being seen as elitist ("tells you how to experiment")

## Processes
- Monthly Data-to-Action loop: pick a core customer problem → set 3-month behavioral-metric roadmap → run tests → review → reset [3]
- Gate-based pipeline: insight → business case → study design → build → launch/report, with owners and deliverables at each gate [1]
- Org-model-specific scaling playbooks (GM: align units, share knowledge, manage resources; Functional: cross-functional collaboration, integrated platforms; Product: unify frameworks; Project: retain knowledge, coordinate resources) [2]

## Heuristics
- "Velocity vs complexity" balance: more tests is not better if complexity eats trust [2]
- GM model risks "local maxima" — business-unit-optimized, company-suboptimal tests [2]
- If you can't ship wins, you're not building momentum, you're building frustration (production capacity is a first-class constraint) [2]

## Tactics
- Automate test-result broadcasting (Zapier → Slack channel) so everyone sees and comments on insights [2]
- Keep a standardized, searchable insight repository (Airtable) [2]
- Interview-led taxonomy placement: map your org before designing the program [4]
- Define acceptance criteria per gate as core standards [2]

## Tools
- Airtable/Effective Experiments-class KMS, Zapier automation, experimentation platforms, Miro (his taxonomy work started as a "massive Miro board") [2,4]

## Inputs
- Org structure (centralized/decentralized), operating model (product-led/feature-led), current test pipeline state, customer problem definition [1,2,4]

## Outputs
- Phase-gate blueprints, XOS artifacts, program roadmaps, org taxonomy placement + transition plans, papers/blueprints (Speero library) [1,4]

## Metrics
- Test velocity, decision quality per gate, insights captured/shared, behavioral metric movement per roadmap, implementation rate [1,2,3]

## Decision rules
- Gate 1→2: proceed only when data/insights answer "is this worth testing?" with a business case [1]
- Gate 2→3: proceed only when the business case has a study design [1]
- Gate 3→4: proceed only when ready to launch (QA, owners set) [1]
- Once a gate is passed, do not revisit the decision (one-way street) [1]
- If org is feature-led → install a CoE before scaling volume [4]
- If teams are siloed by function → integrate platforms + cross-functional squads before scaling [2]

## Failure modes
- Misaligned teams: "experiments slowing down because your team is misaligned" — the gap the Phase Gate framework exists to close [1]
- Feature-factory mode (centralized + feature-led): experimentation as validation theater [4]
- Corporate feudalism (decentralized + feature-led): redundant, conflicting experiments [2]
- Communicating "we ran X tests so that was a success" — test count as success metric muddles the message [3]
- CoE as an elitist gatekeeper → resistance [4]

## Contrarian beliefs
- Maturity models (Crawl/Walk/Run/Fly) ask the wrong question; ask "how does org structure influence experimentation" instead [4]
- Velocity and quality are not a trade — the monthly Data-to-Action roadmap "eats our cake (velocity) and has it (quality) too" [3]

## Examples
- Clients: Cisco, Wellhub/Gympass, Tipalti, MongoDB, Miro, ClickUp, P&G, ADP; Decathlon transition from GM model to functional CoE model over 3+ years [2]
- Background: 6 years as research scientist, University of Texas at Austin (data modeling) [2]

## Conditions
- Phase Gate fits orgs running 10+ tests/quarter with multiple stakeholders; XOS fits teams that can commit to monthly rituals [1,3]
- Taxonomy is descriptive, not prescriptive: placement depends on org size, culture (process vs application cultures — CoE language differs US vs Europe) [4]

## Limitations
- The taxonomy paper is interview-based ("the next step is to quantify what we've seen and get more data to validate") — framework, not evidence [4]
- Speero blueprints are partially marketing artifacts (lead magnets) [1]

## Sources
1. Test Phase Gate Framework post | linkedin.com/posts/benlabay_are-your-experiments-slowing-down-because-activity-7414270767959474176 | post | 1 | 2026-08-14
2. How to Scale Experimentation in Different Structures | speero.com/post/how-to-scale-experimentation-in-different-structures... | article | 1 | 2026-08-14
3. 'Data to Action' workshop post | linkedin.com/posts/benlabay_ive-finally-figured-out-the-lynchpin-ritual-activity-7239604523357323264 | post | 1 | 2026-08-14
4. Sideshow EP4: org structure and experimentation (taxonomy paper w/ Stotz & Vermeer) | speero.com/post/sideshow-ep4 | podcast transcript | 1 | 2026-08-14
5. Cadence for Experimentation Meetings blueprint | speero.com/blueprints/cadence-for-experimentation-meetings | blueprint | 1 | 2026-08-14
