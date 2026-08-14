# SYNTHESIS — AI SEARCH OPTIMIZATION (GEO / AEO / LLMO)

Verified: 2026-08-15. Practitioners: Shelley Walsh, Andy Crestodina, Kevin Indig, Aleyda Solis, Ryan Law, Stanford GEO group (Aggarwal et al.), Martha van Berkel, Aaron Bradley + org/topic evidence (Ahrefs studies, Seer Interactive).

## Consensus
- **Being in the retrieval pool is the prerequisite for being cited.** ChatGPT cites ~88% of its URLs from the general "search" retrieval channel (Ahrefs, 1.4M prompts, Apr 2026); Reddit's dedicated feed is pulled at volume but cited only 1.93% of the time. Practical consequence: classic SEO ranking is the entry ticket to AI citations. [Law/Linehan/Guan — EMPIRICAL]
- **Quotes, statistics, and external citations in content are the strongest measured content levers.** Stanford GEO: +30-40% position-adjusted visibility from Cite Sources/Quotation/Statistics addition; up to 37% on Perplexity. [Aggarwal et al. — EMPIRICAL, controlled]
- **Third-party mentions dominate brand citations.** ~85% of AI brand citations come from third-party domains (Crestodina); Perplexity's most-cited domains are YouTube (31-32%), Reddit (13.9%), Wikipedia (7.2%) (Ahrefs, Jun 2026); unlinked brand mentions matter more for LLMs than for Google (Law). [EMPIRICAL]
- **Answer-first structure works**: question-as-heading, direct answer immediately after, self-contained chunks; 93% of 150 AI-search sources agree (Crestodina); Aleyda Solis: chunked topic clusters; HubSpot AEO docs echo. [HEURISTIC + consensus]
- **Measure per engine, never as one blended score.** Only 2.37% of cited URLs appear in all three engines; 91% in exactly one (Indig, 3.7M citations, 20k prompts). Presence/Portability/Concentration are three numbers. [Indig — EMPIRICAL]
- **Treat each AI answer as a sample, not a ranking**; aggregate at topic level (Solis). [HEURISTIC]
- **AI answers reduce clicks.** AIO presence correlates with −34.5% position-1 CTR (Law/Guan, 300k keywords); Seer Interactive: organic CTR fell from 1.41% → 0.64% on AIO queries (Jan 2025 data). Google doesn't expose AIO click data in Search Console. [EMPIRICAL]
- **Technical crawlability is table stakes**: server-side rendering, AI bot access (GPTBot, PerplexityBot, ClaudeBot, Google-Extended), llms.txt optional. [Solis, Law, Crestodina — HEURISTIC]

## Disagreement
1. **Is GEO a new discipline or just SEO?** Ryan Law: "GEO, LLMO, AEO… it's all just SEO" — mechanism is relevance+authority on/off site; separate GEO programs are waste. vs. Stanford group, Solis, Walsh, van Berkel: GEO is a distinct optimization layer (different retrieval, citation mechanics, no-JS rendering, unlinked mentions). **Condition**: Law is right about mechanism (relevance/authority transfer); the "delta" camp is right about surface (citation behavior, mention weight, content formats). Operationally: run one content program, but track AI-specific metrics. [OPINION vs FRAMEWORK]
2. **Does schema move AI citations?** Schema vendors (van Berkel) and 89% of SEO sources say yes; Ahrefs' controlled test of 1,885 pages adding JSON-LD found no uplift (AIO −4.6%, AI Mode +2.4%, ChatGPT +2.2%, effectively null). Schema is confounded: cited pages are 3x more likely to have schema because better sites do everything better. **Condition**: schema as *content-planning lens* (Crestodina) and *enterprise knowledge-graph infrastructure* (van Berkel) survives; schema as *quick citation lever* does not. [EMPIRICAL null vs vendor OPINION]
3. **Measurement unit**: blended "AI visibility score" (most tools) vs Indig's three-number framework (presence/portability/concentration). **Condition**: blended scores only OK when buyer uses one engine (e.g., local search dominated by AIO); otherwise misleading by construction.
4. **Citation decay**: Crestodina: AI citations decay after ~13 weeks → quarterly refreshes. Indig's longitudinal data shows slight convergence (universal overlap 2.2% → 2.7%) but no decay model published. **Condition**: freshness matters for news/trending; evergreen entity pages (Wikipedia-style) persist. [single-source EMPIRICAL vs EMPIRICAL]
5. **GEO manipulation threat level**: Stanford's 2026 GEO-Bench shows black-box content rewriting can match gradient-based attacks and evade detection on some domains → gaming is real; practitioners' consensus is that AI engines will counter (and Google/OpenAI have) and detection research is active. [EMPIRICAL]

## Conditions
- **Citation levers (quotes/stats/citations) work best** when: content is informational/comparative, brand already ranks, queries are well-served by the web. Weak for local/transactional where engines pull reviews/GBP/training data (Indig's local-brand analysis).
- **Third-party footprint is the biggest lever when**: brand is absent from answers entirely; own-site content is thin; competitor analysis shows Reddit/Wikipedia/YouTube dominate your vertical's answers (Perplexity's mix is a preview: YouTube 31%).
- **Entity/graph work pays when**: enterprise scale, misattribution observed, multi-engine portability wanted. Not when: small site, no ranking baseline.
- **Per-engine optimization is correct when**: buyers concentrate on one engine; **portability work is correct when**: buyers span engines and brand identity is diffuse (Indig's "entity definition problem").

## Evidence evaluation
- **EMPIRICAL (controlled)**: Stanford GEO lab experiments (+30-40%); Ahrefs schema experiment (null); Ahrefs ChatGPT pipeline (1.4M prompts).
- **EMPIRICAL (observational)**: Indig 3.7M citations; Law/Guan CTR −34.5% (matched keywords); Ahrefs Perplexity citation mix; Seer AIO CTR trend; Crestodina 85% third-party + 13-week decay (single-source).
- **HEURISTIC/consensus**: answer-first structure, FAQ sections, prompt libraries from transcripts, freshness cadence.
- **OPINION/vendor**: schema-causes-visibility claims (van Berkel); "GEO is just SEO" (Law, normative); "context not content is king" (van Berkel).
- **Field-wide caveat**: no public RCT of a full GEO program on real traffic; most "GEO case studies" are vendor single-arm — treat as T3.

## Outliers
- **Indig's portability metric** as an entity-definition diagnostic — reframes "am I optimized for AI?" into "have I made myself unambiguous to three different retrieval systems?" Worth encoding as a standard OS metric.
- **Crestodina's Schema-to-Content Opportunities**: using schema properties as a content-gap vocabulary (validated by the null-result evidence — schema helps planning, not ranking).
- **Stanford's "cite sources from reliable sources"** — adding citations *in your content* boosts *your* visibility (the content that cites others gets cited).
- **Law's "hire an SEO"** — anti-GEO-industry stance; useful as a budget-allocation decision rule.
- **Wikipedia/Reddit paradox** (Indig): highest-volume citation sources are the least portable (Wikipedia 1.3% universal, Reddit 0.1%) — volume chasing is a trap.

## Failure knowledge
- **Schema-only fixes don't move citations** (Ahrefs controlled experiment, 2026). [EMPIRICAL]
- **Blended AI-visibility scores hide single-engine concentration** — 91% of citations live in exactly one engine; a "strong" composite is compatible with invisibility in 2 of 3 engines. [Indig — EMPIRICAL]
- **Binary "mentioned/not mentioned" measurement is insufficient** — presence ≠ recommendation ≠ own-domain citation (Solis). [HEURISTIC]
- **Gaming is documented but unstable**: adversarial GEO (prompt/gradient attacks) trades effectiveness against stealth; white-hat rewriting can evade current detection; detection research is active (GEO-Bench 2026). Unverifiable claims and prompt-injection content get you penalized or ignored. [EMPIRICAL]
- **Treating AI as an external event** (Walsh's #1 publisher mistake) — strategic denial is the biggest failure, not technique. [OPINION]
- **Reddit-volume chasing**: ChatGPT retrieves Reddit massively but cites it at 1.93%; Reddit presence ≠ Reddit citations. [EMPIRICAL]
- **Believing Google's AIO click claims**: Google says AIO links get more clicks; Law/Guan measured −34.5% position-1 CTR; no Search Console disaggregation exists to verify Google's claim. [EMPIRICAL]
- **JS-rendered content is invisible** to LLM crawlers; client-side rendering nullifies everything else. [Law/Solis — EMPIRICAL-adjacent]
- **Keyword-tool-only prompt libraries** miss conversational/task queries that dominate AI platforms (Solis). [HEURISTIC]

## Collision Method sketch — AI Search Visibility (AEO/GEO) for the Marketing OS
- **Objective**: maximize brand citation share (presence + portability) in AI answers for the prompt library that maps to the buyer journey; accept citations ≠ clicks, pair with brand-query lift measurement.
- **Prerequisites**: (1) prompt library from sales/support transcripts + review/community language (not keyword tools); (2) per-engine baseline: 50-200 prompts × {ChatGPT, Perplexity, Google AIO} at topic level; (3) ranking baseline for the same queries in classic search (the retrieval-pool prerequisite); (4) list of current third-party citers (PR, Wikipedia, Reddit, analyst reports).
- **Diagnosis**: compute Presence (share of prompts where domain appears per engine), Portability (share of cited URLs appearing in 2+ engines), Concentration (share from one engine). Gap-analysis: for cited competitor/other answers, diff content elements (quotes, statistics, named entities, answer blocks, third-party sources).
- **Decision tree**:
  - Not ranking for seed queries → fix SEO/crawlability first (search channel = 88% of ChatGPT citations). No GEO spend.
  - Ranking but absent from answers → add third-party footprint (PR, Reddit/Wikipedia presence, unlinked mentions) + quotes/stats/external citations in content (Stanford levers).
  - Present but not cited / misrepresented → answer-first restructure (question-H2 → immediate answer), entity clarity (consistent naming, entity home pages), schema as content-planning lens.
  - Cited but concentrated in one engine → portability work: entity disambiguation, Wikipedia/analyst coverage, reduce diffuse brand facets.
  - Cited but no business impact → stop optimizing citations; measure brand-search lift and consider the answer itself as the conversion surface (value-based clicks, Walsh).
- **Execution**: per-engine content scoring quarterly; 4-6 week cycles; third-party citation acquisition in parallel with content.
- **Metrics**: presence %, portability %, concentration %, SOV per prompt topic, citation decay half-life, position-1 CTR delta vs AIO-free peers, brand-query GSC lift.
- **Stopping rules**: stop schema-only initiatives (null result); stop single-engine optimization when concentration >~80% without portability plan; stop if no presence movement after 2 content cycles (~26 weeks) → revisit ranking baseline; stop prompt-level optimization on sample noise — aggregate to topic.
- **Failure modes**: blended scores; single-answer sampling; gaming attempts (detectable, unstable); JS rendering; ignoring third-party footprint; vendor case-study optimism (single-arm).
- **Conditions**: strongest for informational/comparative B2B content; weakest for local/transactional (training-data + reviews dominate) and for brands without ranking baseline.
- **Limitations**: field is <2 years old; citation mechanics change with engine updates; no RCT-level evidence for full programs; most quantitative claims are observational.
- **Confidence**: mechanisms (quotes/stats/citations, retrieval-pool prerequisite, per-engine fragmentation, CTR decline) = high (multiple independent sources); schema effects = null-to-low; vendor GEO ROI claims = low.
- **Key sources**: arXiv 2311.09735 (GEO, KDD 2024); arXiv 2605.29107 (GEO-Bench); growth-memo.com/p/the-consensus-gap (Indig); ahrefs.com/blog/why-chatgpt-cites-pages; ahrefs.com/blog/schema-ai-citations; ahrefs.com/blog/ai-overviews-reduce-clicks; ahrefs.com/blog/most-cited-domains-perplexity; orbitmedia.com/blog/what-seos-get-wrong-about-ai-search; aleydasolis.com/en/ai-search/ai-search-optimization-checklist; searchenginejournal.com (Walsh ×2, van Berkel).
