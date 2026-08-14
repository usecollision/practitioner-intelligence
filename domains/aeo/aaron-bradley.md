---
practitioner: Aaron Bradley
role: Independent knowledge-graph & schema semantics expert (ex-Electronic Arts, ex-IBM iX)
company: Independent
type: practitioner|analyst
confidence: T2
domains:
  - knowledge graphs / entity optimization / schema
verified: 2026-08-15
sources_checked: 2
---

## Beliefs
- Search engines evolved "from strings to things": from indexes of documents to indexes of things and facts related to those things — the Knowledge Graph era reframed SEO around entities. (Schema App interview, 2018) — FRAMEWORK
- You can't have a web of things without linked-data technologies: ontologies, schemas, taxonomies (SKOS), RDF-based standards. — FRAMEWORK
- Schema.org is "a de facto ontology": like other ontologies it provides precise descriptions of things and their relationships; properties like schema.org/name are themselves relationships that create a graph. — FRAMEWORK
- Personalization at scale requires knowing two things: something about the user and something about the content; the richer both models, the better the relevance. — HEURISTIC

## Principles
- Precision of meaning (ontologies, de-referenceable URIs) is what lets machines and humans agree on what a thing is.
- Entity modeling is data work, not markup work: schema is the vocabulary for expressing an entity model.
- Machine understanding compounds: connected entities → graph → better disambiguation and personalization.

## Frameworks
- Strings-to-things / web-of-things framing of search evolution.
- Ontology → taxonomy → schema.org layering (ontologies define classes/relations; SKOS taxonomies organize concepts; schema.org provides the practical vocabulary).

## Processes
- Model entities and relationships precisely; express via schema.org; ensure URIs are de-referenceable; connect to the broader graph (Wikidata/Wikipedia sameAs).

## Heuristics
- If a brand's facts (who/what/where) aren't expressed as entities with relationships, both Google's KG and AI retrieval systems must guess — and they'll guess differently per engine.
- Every schema property is a relationship; markup is graph-building, not tagging.

## Tactics
- Define entity models before schema implementation (people, products, services, locations, their relations).
- Use consistent naming and URI strategy across the site and external profiles (sameAs to Wikidata/Wikipedia).
- Treat structured data as enterprise data governance, not SEO checklist items.

## Tools
- Schema.org, Wikidata, SKOS/RDF tooling, knowledge-graph platforms (his consulting work spans schema design and KG strategy).

## Inputs
- Entity inventory, content model, controlled vocabulary decisions, existing graph connections.

## Outputs
- Schema designs, knowledge-graph strategies, talks, interviews, essays on schema semantics.

## Metrics
- (Not publicly documented; his work is design/governance-side) — mark measurement guidance UNVERIFIED.

## Decision rules
- If AI engines misattribute or can't identify your brand → audit entity definition + consistency across your site and external profiles before touching content.
- If you're choosing between more content and cleaner entity structure → prefer entity clarity when brand ambiguity is the observed problem (aligns with Indig's portability-as-entity-definition finding).

## Failure modes
- Schema implemented without an entity model (markup that doesn't express relationships = noise).
- Duplicate/conflicting entity representations across pages (fragments identity).
- Treating the Knowledge Graph as a ranking lever rather than an interpretation layer (his consistent warning against "KG SEO" hype).

## Contrarian beliefs
- Most SEO schema work is technically valid but semantically shallow — it doesn't build a graph; it decorates pages.
- Entity optimization is not a "trick" for citations; it's the substrate for consistent machine interpretation — a slower-burn view than GEO vendors sell.

## Examples
- His enterprise schema/KG work (Electronic Arts era; Schema App interview details the strings-to-things shift and ontology layering).

## Conditions
- Most relevant for brands with complex entity structures (many products/people/locations), international footprint, or AI misattribution problems.
- His principles are evergreen (data modeling), but his public work predates the LLM-citation era — apply with 2025-26 evidence (Ahrefs schema null result) in mind.

## Limitations
- Interview is from 2018 (pre-LLM search era) — recent positions on LLM citations UNVERIFIED; confidence T2.
- No published measurement method for AI visibility impact of knowledge graphs.

## Sources
1. Interview with Aaron Bradley — Schema Markup & the Enterprise (Schema App) | https://www.schemaapp.com/schema-app-news/interview-aaron-bradley-schema-markup-enterprise/ | interview | 2 | 2026-08-15
2. Entity-first SEO playbook (Search Engine Land, Barry Schwartz — same school of thought, corroborates entity framing) | https://searchengineland.com/guide/entity-first-content-optimization | guide | 2 | 2026-08-15
