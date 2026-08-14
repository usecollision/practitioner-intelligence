---
practitioner: Martha van Berkel
role: CEO & Co-founder, Schema App
company: Schema App
type: practitioner|founder
confidence: T1
domains:
  - ai-search / entity optimization / structured data
verified: 2026-08-15
sources_checked: 2
---

## Beliefs
- "In this new era of search... context, not content, is king": AI tools need entity and relationship context to understand content. ("Structured Data's Role in AI and AI Search Visibility," SEJ, Sep 2025) — OPINION/FRAMEWORK
- Schema markup at scale builds a "content knowledge graph" — a machine-readable data layer defining what your brand is, what it offers, how it should be understood. — FRAMEWORK
- Structured data "can contribute to visibility and discovery across Google, ChatGPT, Bing, and other AI platforms" via grounding — and prepares web data for internal AI initiatives. — OPINION (vendor-aligned; causal claims contested — see Ahrefs counter-evidence)
- Structured data is an "enhancer," not a standalone guarantee: it defines entities, establishes relationships, and "can reduce hallucinations when LLMs are grounded in structured data through retrieval systems or knowledge graphs." — HEURISTIC

## Principles
- Entity governance: shared definitions and taxonomies across marketing, SEO, content, and product teams.
- Content readiness: content must be comprehensive, relevant, and representative of the topics you want to be known for, and connected to the content knowledge graph.
- Technical capability: cross-functional tools/processes to manage schema at scale and keep it accurate across thousands of pages.
- Mark up consistently and connect entities across pages; one main page defines each entity ("entity home").

## Frameworks
- Content Knowledge Graph: schema markup data layer connecting brand entities (people, products, services, locations) and their relationships across the site and beyond.
- Enterprise schema maturity model: (1) define/map key entities; (2) ensure consistent markup incl. entity home pages; (3) build/expand the content knowledge graph by connecting related entities; (4) govern via entity taxonomies.

## Processes
- Map your brand's key entities (products, services, people, core topics) → identify the entity home page for each → ensure consistent Schema.org markup → connect related entities with relationship properties → govern taxonomies across teams → monitor accuracy at scale.

## Heuristics
- If a page's entities aren't defined and linked, AI systems have no stable reference for your brand.
- Schema's value compounds at scale (single-page markup = rich result; site-wide connected markup = knowledge graph).
- Grounding with structured data matters most where retrieval systems can consume it (knowledge-graph-backed RAG), not just for crawling.

## Tactics
- Enterprise-scale JSON-LD with relationship properties (sameAs, mainEntity, offers, etc.).
- Entity home pages per product/service/person.
- Cross-team entity taxonomies and governance.
- Use schema to define brand facts (what you are, what you offer, where) consistently across every page.

## Tools
- Schema App platform (end-to-end schema markup management); Schema.org vocabulary; knowledge-graph tooling.

## Inputs
- Enterprise content inventory, entity lists, taxonomy agreements, technical CMS constraints.

## Outputs
- Enterprise schema implementations, CMO guides (e.g., "CMO Guide To Schema"), SEJ columns, conference talks.

## Metrics
- Schema coverage/accuracy; entity definition completeness; (claimed) AI visibility contribution — causal measurement not published at page level.

## Decision rules
- If you're an enterprise with thousands of pages and AI/RAG ambitions → build a content knowledge graph; single-page schema won't move AI visibility.
- If you're a small site → prioritize content quality + crawlability first; schema is lower leverage (see Ahrefs null result).
- If AI answers misrepresent your brand → check whether your key entities are defined and marked up consistently; entity ambiguity is a plausible cause (aligns with Indig's portability/entity-definition hypothesis).

## Failure modes
- Schema as a rich-result checklist instead of a connected entity layer (she explicitly pushes against this).
- Inconsistent markup across pages/sites (fragmented entity identity).
- Expecting schema alone to boost citations (her own framing is "enhancer," but vendor marketing oversells; controlled evidence shows no near-term citation lift).

## Contrarian beliefs
- SEO teams should elevate structured data from "rich result eligibility" to "managing a content knowledge graph" — an enterprise-infrastructure view most SEOs resist.

## Examples
- Schema App enterprise implementations (referenced in her SEJ article); her interview series with practitioners like Aaron Bradley.

## Conditions
- Works at enterprise scale with cross-team governance; strongest where brands also run internal AI/RAG initiatives.
- Most defensible as entity-definition infrastructure; least defensible as a direct citation-ranking lever (per Ahrefs 1,885-page controlled test: AIO −4.6%, AI Mode +2.4%, ChatGPT +2.2% — no meaningful uplift).

## Limitations
- Vendor position: causal claims ("contributes to visibility") lack controlled public evidence; tag claims as OPINION until replicated.
- Little public data on citation outcomes from content knowledge graphs specifically (UNVERIFIED).

## Sources
1. Structured Data's Role In AI And AI Search Visibility (SEJ) | https://www.searchenginejournal.com/structured-datas-role-in-ai-and-ai-search-visibility/553175/ | article | 1 | 2026-08-15
2. Ahrefs schema experiment (counter-evidence) | https://ahrefs.com/blog/schema-ai-citations/ | study | 1 | 2026-08-15
