---
practitioner: Mike Blumenthal
role: Co-founder / analyst (the OG local search researcher)
company: Near Media (co-founder); blumenthals.com
type: researcher|practitioner
confidence: T2
domains:
  - Local SEO
  - Google Business Profile ecosystem
  - Reviews
verified: 2026-08-14
sources_checked: 2
---

## Beliefs
- Google's local results are assembled from an ecosystem of data suppliers — understanding the ecosystem explains why listings behave the way they do (FRAMEWORK — his foundational contribution, published 2013).
- Google picks a primary data supplier (or two) per country as "ground truth" for business listings, then layers MapMaker/Places data, leading local sites, and the web on top (FRAMEWORK — e.g., US: Acxiom and InfoUSA; France etc.: Infobel).

## Frameworks
- **Primary data supplier model**: each country has a ground-truth supplier; listing data flows Google ← supplier ← aggregators ← directories (FRAMEWORK).
- **Ecosystem forensics**: when a listing misbehaves (duplicate, wrong data, suspension), trace it to the data source, not just GBP (FRAMEWORK).

## Processes
1. Identify your country's primary data suppliers (via Google Maps Legal Notices — his documented method).
2. Ensure NAP accuracy at the suppliers themselves (the root of the citation chain).
3. Monitor reviews and reputation as core local assets (his Near Media research focus).
4. Diagnose listing problems by tracing data provenance.

## Heuristics
- Fix the data at the source supplier once, and downstream aggregators heal (HEURISTIC — corollary of the model).
- Reviews are the highest-leverage user-generated signal in local (OPINION — his research emphasis; consistent with Hawkins' review findings).

## Tactics
- Read Google Maps/API Legal Notices to identify supplier contracts (TACTIC — the actual method behind his famous posts).
- Data audits across supplier/directory tiers (TACTIC).

## Tools
- Google Maps Legal Notices (research input), Near Media research, local SEO tooling.

## Inputs
- Country-specific supplier knowledge, listing data, review data.

## Outputs
- Ecosystem maps (per country), listing forensics, reviews/reputation research.

## Metrics
- Data accuracy at supplier tier, listing consistency, review signals.

## Decision rules
- Listing data wrong → check supplier tier first (the source), not the display tier (DECISION RULE).
- Duplicate listings → identify which supplier injected the duplicate before removal campaigns (DECISION RULE).
- Reviews neglected → treat as a core local ranking + conversion input (DECISION RULE).

## Failure modes
- Fixing symptoms in GBP while the supplier tier still emits bad data — duplicates return (warned implicitly by the model).
- Assuming Google generates listing data from scratch — it doesn't (the misconception his whole body of work corrects).

## Contrarian beliefs
- "Local SEO" is largely data-ecosystem management, not website SEO — most practitioners over-index on the website side (OPINION).

## Conditions
- Applies to any market with business listings; his supplier maps are country-specific (US, UK/EU documented; others partial).

## Limitations
- His famous supplier research is from 2013 — supplier contracts change (flag as historical baseline, verify current); the ecosystem is less transparent today; his recent work focuses more on reviews/reputation.

## Sources
1. "Google's Local Primary Data Suppliers Around the World" | https://blumenthals.com/blog/2013/03/28/googles-primary-data-suppliers-worldwide/ | primary practitioner research | tier 1 | 2026-08-14
2. "About Mike Blumenthal" | https://blumenthals.com/blog/about-mike-blumenthal/ | primary bio | tier 2 | 2026-08-14
