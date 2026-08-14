---
practitioner: Ryan Law
role: Director of Content Marketing, Ahrefs (formerly Animalz)
company: Ahrefs
type: practitioner|operator
confidence: T1
domains:
  - ai-search / GEO / content strategy / SEO
verified: 2026-08-15
sources_checked: 4
---

## Beliefs
- "GEO, LLMO, AEO… It's All Just SEO" (Ahrefs blog, Apr 2025): LLM visibility is a byproduct of SEO. "If you want to increase your presence in LLM output, hire an SEO." — OPINION/FRAMEWORK
- Core mechanism for LLM visibility = "creating relevant content on topics your brand wants to be associated with, both on and off your website." — FRAMEWORK
- GEO will likely CONVERGE further with SEO as search engines integrate generative AI and LLMs ground output in "traditional" search indexes — not diverge. — OPINION/HYPOTHESIS
- AI Overviews reduce clicks despite Google's claims: "Google says AI Overviews increase clicks. Cold, hard logic disagrees, and so does our research." — EMPIRICAL
- Google hides AIO click data: "It seems that Google doesn't want us to see the clickthrough rate for AI Overviews" (no way to disambiguate AIO clicks in Search Console). — EMPIRICAL/OBSERVATION

## Principles
- Relevance + authority on and off your site is the shared mechanism of SEO and GEO; don't build separate "GEO content."
- Measurement before claims; correlation work with controlled samples where possible (his studies use matched keyword sets and GSC aggregates).
- Content people treat as second-class (PDFs, documents) matters for LLMs — "they routinely cite them."

## Frameworks
- "GEO is SEO with six deltas" (his list of how GEO is slightly different):
  1. Unlinked brand mentions matter more (LLMs learn authority from words/co-occurrence, not just links).
  2. Off-topic links and rankings matter less.
  3. Different content types impact visibility (core pages — homepage, pricing, about — get cited; documents/PDFs cited routinely).
  4. LLMs benefit from unique document structures.
  5. LLMs train on data that doesn't impact SEO.
  6. LLMs don't render JavaScript.
- AIO CTR effect model: forecast position-1 CTR without AIO from informational-keyword trend, compare to actual AIO-keyword CTR.

## Processes
- Controlled observational studies: 300k keywords (150k with AIO, 150k informational without), matched on intent, GSC click data, pre/post rollout comparison (Mar 2024 vs Mar 2025). Re-ran for 2026.
- Brand Radar methodology: track brand mentions in AI outputs by topic; impressions, share of voice, cited URLs.

## Heuristics
- If a query triggers an AI Overview, expect position-1 CTR ~34.5% lower than an equivalent non-AIO query (Apr 2025 study; 2026 re-run referenced). — EMPIRICAL
- LLMs decouple information from its source, so proving authenticity in-content (quotes, data, clarity) is extra important for citations.
- Cite-ability: pages need to be parseable as whole documents; JavaScript-rendered content is invisible to LLMs.

## Tactics
- Publish core entity pages (home/pricing/about) with full information — these are LLM citation magnets even when they're weak SEO pages.
- Make unlinked brand mentions happen (PR, mentions in third-party content) — bigger GEO lever than links.
- Keep PDFs and documents as first-class, indexable content.
- Track brand share of voice in AI answers via Brand Radar-style tools.

## Tools
- Ahrefs Brand Radar (AI mention tracking: impressions, SOV, outputs by topic); Ahrefs Keywords Explorer + GSC for CTR studies.

## Inputs
- Keyword-level GSC click data; AI answer samples; brand mention data across engines.

## Outputs
- Studies ("AI Overviews Reduce Clicks by 34.5%", "Why ChatGPT Cites One Page Over Another" co-published with Ahrefs data science, "GEO, LLMO, AEO… It's All Just SEO"), Brand Radar tool.

## Metrics
- Position-1 CTR with/without AIO; AI brand mentions; share of voice per topic; citation volume by page type.

## Decision rules
- If brand wants LLM visibility → do SEO (relevance, authority, crawlability), not a separate GEO program.
- If a page is a core entity page (home/pricing/about) → keep it complete and current; LLM citation value is high even when search rankings are modest.
- If measuring AIO impact → compare matched keyword sets pre/post rollout; don't trust vendor or Google aggregate claims without controls.
- If content is JS-rendered → server-render before any AI optimization effort.

## Failure modes
- Building "GEO-only" content programs separate from SEO (wasted effort — mechanism is the same).
- Believing Google's claim that AIO links get more clicks (his study says the opposite).
- Ignoring documents/PDFs and core pages for LLM visibility.
- Treating unlinked mentions as worthless (SEO-trained reflex that's wrong for LLMs).

## Contrarian beliefs
- Against the GEO-as-new-discipline industry (Stanford's GEO framing, GEO tool vendors): the mechanism is SEO; differences are deltas, not a new field.
- Against Google's AIO click narrative with public data.

## Examples
- 34.5% CTR study (Apr 2025, re-run 2026); ChatGPT citation pipeline study (1.4M prompts, Apr 2026) showing 88.46% of cited URLs come from the "search" retrieval channel — i.e., "to be cited by ChatGPT you need to rank" (co-published with Louise Linehan & Xibeijia Guan).

## Conditions
- His convergence thesis holds while LLMs ground in web search indexes (current state); if engines move to fully agentic/realtime pipelines with different retrieval, deltas widen.
- Content-quality brand positions (SaaS/B2B) benefit most; transactional/long-tail SEO still behaves like classic SEO.

## Limitations
- The 34.5% figure is correlation (matched keywords, not RCT); 2026 re-run numbers not fully published in fetched material (referenced).
- "It's all just SEO" is partly normative — he's Ahrefs' content lead, so the position aligns with his product (Brand Radar, SEO suite). Tag OPINION.

## Sources
1. GEO, LLMO, AEO… It's All Just SEO | https://ahrefs.com/blog/geo-is-just-seo/ | article | 1 | 2026-08-15
2. AI Overviews Reduce Clicks by 34.5% | https://ahrefs.com/blog/ai-overviews-reduce-clicks/ | study | 1 | 2026-08-15
3. Why ChatGPT Cites One Page Over Another (1.4M prompts) | https://ahrefs.com/blog/why-chatgpt-cites-pages/ | study | 1 | 2026-08-15
4. The 50 Most-Cited Websites in Perplexity | https://ahrefs.com/blog/most-cited-domains-perplexity/ | study | 1 | 2026-08-15
