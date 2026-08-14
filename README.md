# practitioner-intelligence

The Practitioner Intelligence Layer for the UseCollision Marketing OS.

Mission: discover the best practitioners in every capability the Marketing OS has, extract how they actually think and operate, synthesize across them, and use the intelligence to make the six marketing repos materially better.

This is NOT a content scraper. No URL piles, no tweet dumps. The transformation chain is:

```
SOURCE → OBSERVATION → INSIGHT → PRINCIPLE → METHODOLOGY → OPERATING PROCEDURE → SKILL IMPROVEMENT
```

## Structure

```
practitioner-intelligence/
├── README.md              ← this file
├── inventory/
│   └── skill-inventory.md ← Cycle 1 audit: all 137 skills, maturity, gaps (deliverable A)
├── practitioners/
│   └── master-map.md      ← discipline → practitioner directory, sources, gaps (deliverable B)
├── domains/               ← per-discipline deep dives (planned, Wave 1+)
├── syntheses/             ← consensus/disagreement maps per discipline (planned)
├── skill-gaps/            ← per-skill gap analyses (planned)
├── skill-evolution/
│   ├── proposed/          ← proposed skill changes, with provenance
│   ├── accepted/          ← reviewed and accepted
│   └── rejected/          ← rejected with reasons
└── scripts/               ← inventory generators (data-driven, re-runnable)
```

## Status (full program — 2026-08-15)

| Step | Status |
|---|---|
| Repository audit (6 repos, 137 skills) | ✅ done |
| Skill inventory with maturity scoring | ✅ done |
| Practitioner master map (38 disciplines) | ✅ done |
| WAVE 1 — Paid strategy / CRO / positioning-messaging | ✅ research + implementation (10 skills → M4) |
| WAVE 2 — SEO / AI search / creative | ✅ research + implementation (11 skills → M4) |
| WAVE 3 — Customer research / outbound / email | ✅ research + implementation (7 skills → M4) |
| WAVE 4 — Social / PR / partnerships / GTM / pricing / analytics / DTC | ✅ research + implementation (27 skills → M4) |
| Adjacency sweep (thin-field honest treatment, platform ads) | ✅ 7 skills → M4 |
| Re-audit + final quality pass | ✅ 62/137 M4 · validators pass |
| Final record | ✅ backlog/final-record.md |

**62 skills upgraded to M4** · 17 syntheses · 87 practitioner dossiers · ~140 practitioners · 13 commits across 6 repos + this one. Remaining 75 skills documented in final-record.md with reasons (thin fields, near-duplicates, org-source disciplines).

## Pipeline (per spec §19)

```
REPOSITORIES → DISCOVER SKILLS → MAP SKILL→DISCIPLINE → DISCOVER PRACTITIONERS →
DISCOVER SOURCES → COLLECT MATERIAL → EXTRACT INSIGHTS → EXTRACT METHODOLOGIES →
RECONSTRUCT MODUS OPERANDI → CROSS-PRACTITIONER SYNTHESIS → EVIDENCE/CONFIDENCE SCORING →
COMPARE AGAINST CURRENT SKILL → IDENTIFY GAPS → PROPOSE SKILL CHANGES → UPDATE SKILL →
TEST SKILL → FEED RESULTS BACK
```

## Rules of engagement

1. **Proposal before implementation** (spec §34): RESEARCH → PROPOSAL → REVIEW → IMPLEMENTATION → VALIDATION. Never silently overwrite a production skill in the six repos.
2. **No orphaned claims** (spec §22): every important insight carries practitioner → source → evidence → extraction date.
3. **Confidence tiers**: T1 verified/canonical · T2 verify before deep dive · T3 caution (guru-adjacent/legacy). Insights get a confidence score (spec §12).
4. **Distinguish claim types** (spec §13): fact / empirical observation / heuristic / framework / opinion / hypothesis / tactic / experimental idea.
5. **Context or it doesn't count** (spec §17): company size, model, stage, budget, channel — a $50M SaaS tactic is not a 2-person startup tactic.
6. **Reddit and social are field intelligence** (spec §24-25), not truth.
7. **Search negative knowledge** (spec §27): failures, postmortems, things practitioners stopped doing.
8. **Ask "why" twice** (spec §28): second-order insights cross repositories — use the dependency graph in marketing-core.

## First execution outputs (spec §37)

- A. Skill Inventory → `inventory/skill-inventory.md`
- B. Practitioner Directory → `practitioners/master-map.md`
- C–L (Source Index, Methodology Library, Modus Operandi, Consensus/Contradiction Maps, Failure KB, Skill Gap Analysis, Improvement Proposals, Cross-Repo Impact, Research Backlog) → per-wave deliverables, starting with `backlog/research-backlog.md`
