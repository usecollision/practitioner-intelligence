---
practitioner: Andy Crestodina
role: Co-founder & CMO, Orbit Media Studios
company: Orbit Media Studios
type: practitioner
confidence: T1
domains:
  - ai-search / AEO / content strategy
verified: 2026-08-15
sources_checked: 3
---

## Beliefs
- Most AI-search advice is consensus echo: FAQs/answer-first content (93% of 150 sources surveyed), schema markup (89%), and PR/third-party citations (87%) are the standard package — and it's incomplete. ("What SEOs Get Wrong About AI Search," Apr 2026) — EMPIRICAL (survey of sources) + OPINION
- The most cited content in AI answers is off-site: ~85% of AI brand citations come from third-party domains, not the brand's own site. — EMPIRICAL (his dataset, cited in the article)
- AI citations decay: content stops being cited roughly 13 weeks after publishing unless maintained. — EMPIRICAL (his analysis)
- Schema's real value is as a CONTENT PLANNING lens, not post-hoc markup: use Schema.org properties to find content gaps. This is the "more effective method" that none of his 150 surveyed sources recommended. — OPINION/TACTIC
- "It's easier for a machine to understand a page if the content elements are tagged... Crawlers, including GoogleBot and GPTBot, can use these tags" — but content quality and coverage are the actual mechanism. — HEURISTIC

## Principles
- Content that wins for humans wins for AI; AI optimization is mostly better content + signals.
- Build answer-first structure: Q&A headers, extractable answer blocks, dedicated FAQ sections.
- Earn mentions where AI engines actually look: Reddit, YouTube, Wikipedia, review sites, analyst reports.
- Update cornerstone content quarterly and publish original research to counter citation decay.

## Frameworks
- "Schema-to-Content Opportunities": a prompted process (LLM as content strategist) — identify page's Schema.org type(s), check what AI engines surface for the page's queries, review type properties (step, areaServed, review, offers, knowsAbout, mentions, mainEntity) as content-gap inventory, output prioritized content additions per property. Includes guardrail: confirm the Schema.org property exists before recommending. — FRAMEWORK/TACTIC
- Consensus-vs-effective split: what "everyone says" (FAQ/schema/PR) vs what works (structure + third-party footprint + freshness).

## Processes
- For each priority page: (1) define primary topic + relevant Schema.org types; (2) check current AI answers for the page's queries and note what cited/competing pages include that yours lacks; (3) map missing schema properties to content gaps; (4) prioritize by visitor impact; (5) add content, markup optional. — PROCESS

## Heuristics
- AI engines cite what they can parse and verify: clear headings, direct answers, community proof.
- Most common AI citations are Reddit, YouTube, Wikipedia — presence there is presence in AI answers.
- If content doesn't answer a real visitor question, don't add it even if schema suggests it.

## Tactics
- Add FAQ sections with the exact question as H2/H3 and the answer immediately following.
- JSON-LD Article/HowTo/Organization/Product schema; llms.txt + robots.txt for AI crawler access.
- Quarterly cornerstone refreshes; original research cadence; topic clusters.
- Build authentic Reddit/YouTube/LinkedIn/review-site presence (AI engines verify brand claims against community conversation).

## Tools
- Orbit Media's AI-search consensus dataset (150 sources); LLM prompts for content auditing; Schema.org reference.

## Inputs
- Current AI engine answers for target queries; competitor/cited page content; schema type inventory for the page's topic.

## Outputs
- AEO guides and audits; content gap lists; the Schema-to-Content Opportunities prompt.

## Metrics
- Citation presence per engine; citation decay rate over time; third-party vs owned citation ratio.

## Decision rules
- If a page isn't cited but ranks → restructure to answer-first + close schema-property content gaps before adding more content.
- If citations decay (~13 weeks) → refresh cornerstone content quarterly rather than publishing new.
- If brand is absent from AI answers entirely → prioritize third-party citation footprint (Reddit, Wikipedia, PR) over on-page tweaks, because 85% of citations are off-domain.

## Failure modes
- Adding schema markup to weak content (markup without content = no citations).
- Publishing once and never refreshing (decay).
- Ignoring off-site presence — the single biggest gap he names in consensus advice.

## Contrarian beliefs
- Schema as a content-planning tool, not a technical SEO checklist item (he explicitly says none of 150 sources recommended the more effective method).
- Consensus AI-search advice (FAQ+schema+PR) is necessary but not sufficient; the field overrates markup and underrates off-site citation footprint.

## Examples
- Orbit Media's own content program; his dataset of 150 AI-search articles showing 93/89/87% consensus on FAQ/schema/PR.

## Conditions
- Works for content-driven B2B sites with editorial resources; answer-first structure matters most for informational/commercial-investigation queries.
- Schema-as-lens requires LLM access and content team capacity.

## Limitations
- His citation-decay and 85% figures are his own analysis, not independently replicated — mark EMPIRICAL-but-single-source.
- Schema-for-AI-citations is contested: Ahrefs' controlled experiment (1,885 pages adding schema) found no citation uplift (see synthesis). Crestodina's framing (planning lens) survives that result better than "markup boosts citations" claims.

## Sources
1. What SEOs Get Wrong About AI Search | https://www.orbitmedia.com/blog/what-seos-get-wrong-about-ai-search/ | article | 1 | 2026-08-15
2. Orbit Media AEO guides | https://www.orbitmedia.com/blog/ | article series | 2 | 2026-08-15
3. Ahrefs schema experiment (counter-evidence) | https://ahrefs.com/blog/schema-ai-citations/ | study | 1 | 2026-08-15
