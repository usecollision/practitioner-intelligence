# Research Backlog — Wave 1

Prioritization formula (spec §32): Impact × Current Skill Weakness × Practitioner Evidence Density × Frequency of Use × Business Importance.

## Wave 1 — highest leverage (start here)

### 1. CRO + Experimentation → M4 (proposal against marketing-optimize)
- **Why**: cro-audit/ab-testing/mmm-incrementality are already the OS's strongest skills (M3). Practitioner layer converts them into the template others copy. Highest evidence density in marketing.
- **Practitioners**: Peep Laja, Jon MacDonald, Craig Sullivan, Talia Wolf, Michael Aagaard, Ben Labay, Karl Blanks (legacy), Ronny Kohavi, Lukas Vermeer, Georgi Georgiev, Martin Goodson.
- **What to extract**: decision rules (when to test vs redesign, prioritization with PXL/ICE, when to kill a test), failure modes, experiment velocity ops.
- **Deliverable**: skill-gaps/cro.md → proposal: add "Decision Rules" + "Sources" sections to cro-audit, ab-testing, experiment-prioritization.

### 2. Positioning + Messaging → M3 (proposal against marketing-intelligence/messaging)
- **Why**: feeds every downstream repo per the dependency graph; the OS already cites April Dunford but has no source layer; messaging skills are M1/M2.
- **Practitioners**: Dunford, Raskin, Pierri, Moore, Schwartz (market sophistication), Wiebe, Price, Hormozi (T3, conditions).
- **What to extract**: the research-before-copy pipeline, market sophistication decision rule, positioning validation method.
- **Deliverable**: skill-gaps/positioning.md → proposals for positioning-framework, conversion-copywriting, offer-design.

### 3. Paid strategy + Media planning (add the Binet/Sharp layer)
- **Why**: paid-strategy/media-planning lack the effectiveness evidence entirely — the most cited finding in marketing (long/short, brand vs activation) is absent.
- **Practitioners**: Binet & Field, Byron Sharp, Mark Ritson, Eric Seufert.
- **What to extract**: budget-allocation decision rules (when brand %, when activation %), frequency laws, payback horizon.
- **Deliverable**: skill-gaps/paid.md → proposal for paid-strategy, media-planning, performance-reporting.

## Wave 2

### 4. SEO + AI Search (proposal against marketing-channels)
- **Why**: technical-seo/keyword-research are M2 with zero sources; ai-search skills are the OS's differentiator and the field is young enough that practitioner synthesis is still novel.
- **Practitioners**: Gabe, Ray, Stox, Indig, Solis, Gübür, Dunning, + GEO set (Walsh, Crestodina, Aggarwal et al.).
- **Deliverable**: skill-gaps/seo.md, skill-gaps/ai-search.md.

### 5. Ad creative + hooks
- **Why**: hook-frameworks/ad-copy are M1/M2; creative is the highest-leverage paid variable; dense practitioner field (Denney, Shackelford, Chappell).
- **Deliverable**: skill-gaps/creative.md.

## Wave 3

### 6. Research/interview skills chain (ICP → personas → messaging)
- **Why**: customer-interviews/personas/icp-builder are M2 with no Mom Test influence encoded; upgrades ripple through messaging and channels.
- **Practitioners**: Fitzpatrick, Blank, Alvarez, Revella, Torres, Moesta, Klement, Ulwick.
- **Deliverable**: skill-gaps/research.md.

### 7. Outbound + email lifecycle
- **Deliverable**: skill-gaps/outbound.md (Berman, Allred, Ingram, Ross) + skill-gaps/email.md (White, Geisler, Schwedelson, Pay, Iverson).

## Wave 4 — low priority, mostly org-source encoding

- Reddit growth, X growth, IG/TikTok organic, co-marketing, automation/RevOps, local SEO — thin practitioner fields; encode platform docs + community intel, keep confidence low. (Map §14-16, §36.)

## Operational notes

1. **Proposal flow**: each wave produces `skill-gaps/<discipline>.md` + a concrete diff proposal against the target repo (RESEARCH → PROPOSAL → REVIEW → IMPLEMENTATION → VALIDATION). Proposals are PRs; nothing merges without review.
2. **Provenance**: every extracted principle carries practitioner → source URL → extraction date → claim type → confidence.
3. **Verification first**: T2/T3 practitioners get re-verified (current role, canonical artifact) before their content enters a proposal.
4. **Repo hygiene**: marketing-core's context/product-marketing.md is an EMPTY TEMPLATE — the real product context lives locally. Fix in Wave 1 (move the real file in or link it).
5. **Decide**: does practitioner-intelligence become a 7th org repo, or live inside marketing-intelligence? Recommendation: 7th repo — it is a meta-layer over all six, and its review workflow (proposals as PRs) maps cleanly to repo boundaries.
