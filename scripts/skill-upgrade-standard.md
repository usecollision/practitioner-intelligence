# SKILL UPGRADE STANDARD — M4 (Practitioner-Informed Decision System)

Every skill upgrade in this program follows this contract. Upgrades land in the six marketing repos as SKILL.md edits, each with a commit message referencing the research it came from.

## What an M4 skill must answer (spec §14)

```
WHAT?          — what the skill does (already exists)
WHY?           — the mechanism, with named practitioner/research grounding
WHEN?          — activation conditions (already exists, tighten)
WHEN NOT?      — explicit conditions where the skill should NOT be used
HOW?           — the workflow (already exists)
HOW MUCH?      — quantitative decision thresholds (budgets, sample sizes, frequencies)
WHAT IF IT FAILS? — failure modes + recovery (exists; add practitioner-sourced ones)
WHAT SHOULD I MEASURE? — metrics section with targets and methods
WHEN SHOULD I STOP?    — stopping rules / kill criteria
WHAT SHOULD I DO NEXT? — next-step routing via related_skills + dependency graph
WHAT EVIDENCE SUPPORTS IT? — Sources section with provenance
WHO DEMONSTRATED IT?    — practitioner attributions
WHAT CONDITIONS IT REQUIRES — context requirements
WHAT OTHER SKILLS IT AFFECTS — cross-repo impact notes
```

## Standard section additions (in order, appended before "Evaluation & QA" or after as marked)

### 1. `## Practitioner Grounding` (new section after Workflow)
- 3-8 named practitioners with one-line attribution each: what their method contributes
- Confidence tier per claim: T1 verified / T2 known / T3 caution
- Every claim tagged: FACT | EMPIRICAL | HEURISTIC | FRAMEWORK | OPINION | HYPOTHESIS | TACTIC

### 2. `## Decision Rules` (new section)
The heart of M4. Must be executable if/then rules:
```
IF <condition> THEN <action> (source: <practitioner>, <claim type>, <confidence>)
```
Minimum 5 rules per upgraded skill. Rules come from the synthesis files — consensus becomes rules, disagreement becomes conditional rules.

### 3. `## Metrics` (new or upgraded section)
- Primary metric + target + measurement method
- Guardrail metrics
- Timebox for evaluation
- "When to re-measure" rule

### 4. `## Sources` (new section at end, before Evaluation & QA)
- Numbered list: practitioner | artifact | URL | tier | accessed YYYY-MM-DD
- Only sources actually used by the skill's content
- No orphan claims: every Practitioner Grounding attribution must resolve to a Sources entry

### 5. Failure modes additions (append to existing Common Failure Modes)
- Practitioner-sourced failure modes with attribution
- Negative knowledge: "this repeatedly fails because..."

## Quality gates before commit

1. Skill still fits the SKILL-TEMPLATE structure (frontmatter intact, gates present)
2. No claim without a source or a T3/UNVERIFIED tag
3. Decision rules are concrete — no "consider", "maybe", "evaluate"
4. Context preserved: any quantitative threshold carries its conditions (company size, model, stage, budget)
5. Cross-repo check: if the change affects another skill, that skill is patched in the same wave or a follow-up commit referencing it
6. `scripts/validate-tools.py` and `scripts/check-integrity.py` from marketing-core pass after edits

## Commit convention

```
<repo>: <skill> → M4 upgrade (<discipline> practitioner synthesis)

- Added: Practitioner Grounding (N sources)
- Added: Decision Rules (N rules)
- Added: Metrics section
- Failure modes extended (N)
- Sources: syntheses/<discipline>.md in practitioner-intelligence
```

## Maturity rubric (for the re-audit)

- M4 = has all five sections above, decision rules verified against synthesis, sources resolve
- M3 = has metrics + decision logic + scoring, missing sources
- M2 = operational with gates + failure modes
- M1 = structure only
