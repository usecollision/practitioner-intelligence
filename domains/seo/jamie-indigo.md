---
practitioner: Jamie Indigo
role: Technical SEO consultant / speaker
company: Independent (ex-Lumar/Deepcrawl)
type: practitioner
confidence: T2
domains:
  - Technical SEO
  - Site architecture
  - JavaScript/rendering
verified: 2026-08-14
sources_checked: 2
---

## Beliefs
- "Good data makes good decisions" — evidence-first technical SEO (OPINION, stated self-description).
- Technical SEO is a marketing-dev hybrid discipline: requirements, QA, and go-live support are part of the job, not adjacent to it (OPINION — from their role history: facilitating launches and redesigns).
- The best site is one that "meets the users' needs through a cross-device experience that makes them feel smart and empowered" (OPINION — human-centric framing; "100% Human Technical SEO").

## Frameworks
- **Rendering strategy analysis**: examine how JS frameworks deliver content to crawlers vs users; CWV audits tied to rendering (FRAMEWORK).
- **Index coverage forensics**: diagnose coverage by combining server logs, information architecture, technical signals, and technical parity (geo, mobile vs desktop) (FRAMEWORK).

## Processes
1. Audit rendering strategy and JS execution for enterprise sites (e-commerce, publishing).
2. Vet findings with solution engineers and data scientists before reporting (validation step).
3. Produce developer-ready tickets (they specialize in "actionable tickets ready for developer refinement").
4. Support launch/migration/redesign QA and go-live as SME.
5. For dynamically generated content: examine server logs + IA + technical parity to correct index coverage.

## Heuristics
- Dynamically generated content sites (JS-heavy) hide indexation problems in the gap between server output and rendered DOM (HEURISTIC).
- Technical parity issues (geo-serving, mobile vs desktop divergence) are common coverage culprits (HEURISTIC).

## Tactics
- Pair CWV findings with engineering feasibility before shipping tickets (TACTIC).
- Log analysis for crawl behavior on JS sites (TACTIC).
- Speak in requirements and acceptance criteria to engineering (TACTIC).

## Tools
- Enterprise crawlers (Lumar/Deepcrawl — their former employer), server log analysis, CWV field data (CrUX).

## Inputs
- Business objectives, project life-cycles, resource availability, application stack (they explicitly incorporate these).

## Outputs
- Technical SEO requirements, QA checklists, developer tickets, go-live support.

## Metrics
- Index coverage, rendering parity, CWV field metrics, crawl behavior from logs.

## Decision rules
- JS-rendered site + coverage issues → log analysis + rendering audit before content fixes (DECISION RULE).
- Migration/redesign happening → bake SEO requirements into the project lifecycle, don't audit after launch (DECISION RULE).
- CWV issue found → validate with engineers/data scientists whether it's worth fixing before shipping the ticket (DECISION RULE).

## Failure modes
- Auditing JS sites without logs/rendering data — conclusions rest on guesses (implied).
- SEO as afterthought in launches/redesigns — the failure their go-live SME role exists to prevent (warned).

## Contrarian beliefs
- Technical SEO is a human discipline: "100% Human Technical SEO" — pushback against AI-generated audit dumps (OPINION — their public stance).

## Conditions
- Enterprise sites with JS frameworks, e-commerce, publishing; teams with engineering access; migrations/redesigns.

## Limitations
- Evidence on their specific frameworks comes from LinkedIn/profile material (T2); their visibility is lower than Stox/Solis so cross-verification is thinner; heavily enterprise-contextualized.

## Sources
1. Jamie Indigo LinkedIn profile | https://linkedin.com/in/jamie-indigo | primary profile | tier 2 | 2026-08-14
2. Google Webmaster MythBuster / SEO Fairytales series participation (referenced) | tier 2 | 2026-08-14
