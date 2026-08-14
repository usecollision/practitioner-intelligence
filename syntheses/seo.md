# SEO — Discipline Synthesis

Coverage: 22 practitioners (technical: Stox, Indigo, Solis, Mueller, Critchlow; algorithm forensics: Gabe, Ray, Schwartz; analysis: Capper; content/topical: Gubur, Indig, Law, Soulo, Dunning, E. Schwartz; links: Moogan, Milligan, McGuirk, Dean; local: Hawkins, Shaw, Blumenthal). Verified 2026-08-14.

## Consensus (strong independent agreement)
1. **Diagnose before acting on traffic drops** — Gabe (delta report + cause classification) and Ray (site-wide pattern list) independently converge: classify drops as relevancy adjustment / intent shift / quality problem before touching content. (EMPIRICAL/FRAMEWORK, T1)
2. **Indexing and crawl issues gate everything** — Stox ("crawl/index issues come first... they gate everything downstream"), Mueller (perceived inventory is the only strongly controllable crawl factor), Indig (technical hygiene = update insurance). (FACT/HEURISTIC, T1)
3. **Prioritize technical fixes by impact × effort, ship 5-10 fixes, not dumps** — Stox (5-10 dev tickets), Solis (impact/effort matrix, drop low-impact/high-effort), Indigo (actionable tickets). Three independent practitioners, identical rule. (FRAMEWORK, T1)
4. **Recovery from quality-driven core-update hits is a long game (next update, often several)** — Gabe (year+ recoveries seen), Ray (long-term quality remediation). (EMPIRICAL, T1)
5. **Search volume is a trap; traffic potential and intent are the real filters** — Soulo (Traffic Potential), Dunning (bottom-funnel demo intent over volume), Law (audience pain over volume), Ahrefs intent framework. (EMPIRICAL/FRAMEWORK, T1)
6. **Link building: manipulation is dead, editorial/earned is alive** — Moogan (Penguin ended the numbers game), Milligan (original research), McGuirk (consistency over virality, 1-20 links per campaign is normal), 2026 field data (SpamBrain 3.0 pattern evaluation). (EMPIRICAL, T1/T2)
7. **Mass-produced low-value pages are the recurring liability** — Ray (copious low-grade local landing pages), Hawkins (filler-word landing pages), 2024-26 scaled-content enforcement (AI programmatic sites tanking), Indig (programmatic needs a quality floor). (EMPIRICAL, T1)
8. **Local SEO = relevance × distance × prominence (Google's triad), operationalized via GBP + reviews + landing page + data-ecosystem hygiene** — Hawkins, Shaw, Blumenthal converge on the same stack. (FACT/FRAMEWORK, T1)
9. **Correlational ranking-factor claims are hypotheses, not facts** — Capper's four-explanation taxonomy; Critchlow's evidence that expert prediction ≈ chance. (EMPIRICAL, T1)
10. **Content must serve a defined buyer, and citable structure matters for AI search** — Law (audience-first), Dunning (answer-up-front + unique data for LLM extraction), Indig (AI citation tracking). (OPINION/HEURISTIC, T2)

## Disagreement
1. **Topical authority vs audience-first brevity (Gubur vs Law)** — Gubur: exhaustive entity/topical-graph coverage (deep, structured, encyclopedic). Law: short, opinionated, audience-problem content; volume ignored. *Condition:* Gubur's method wins in competitive informational niches where depth = differentiation and you can't outlink incumbents; Law's wins in B2B/SaaS where buyers don't search generic topics and distribution happens off-SERP. Both agree intent discipline matters (Gubur's "canonical intent" ≈ Law's "answer the question").
2. **Link building as priority (Moogan/Milligan/Dean) vs product-led SEO (E. Schwartz)** — Schwartz: build the searchable asset; links follow. Link school: assets without link acquisition stall. *Condition:* product-led wins when the product itself can serve bottom-funnel queries (SaaS, marketplaces, e-commerce); link-first wins for content/media businesses with no product surface.
3. **Crawl budget importance (Mueller: mostly a non-issue; Stox: ignore noise) vs audit-industry emphasis** — mainstream tooling over-sells crawl budget; the practitioner consensus is to manage inventory (params, orphans, soft 404s) and stop there.
4. **Content depth/word count (Gubur: coverage) vs brevity (Law) vs intent-based (Dean 2.0, Eli Schwartz: SERP decides)** — the resolution: the SERP/query decides the right format; neither depth nor brevity is universally right.
5. **Testing culture (Critchlow: test everything, best practices are priors) vs long-game remediation (Gabe: core-update recovery can't be tested short-term)** — both true at different levels: page-level changes are testable; site-level quality re-rating is not.
6. **Metrics: rankings/traffic (classic) vs demos/revenue (Dunning, Law) vs AI citations (Indig)** — stage-dependent: content-stage companies track rankings, growth-stage track demos, AI-sensitive verticals track citations.

## Conditions (when each methodology is correct)
- **Gabe/Ray core-update forensics**: sites with meaningful GSC signal volume; publishing/media/commerce; requires multi-month patience.
- **Stox enterprise technical audit**: multi-CMS/regional sites with engineering stakeholders; template-scale problems.
- **Critchlow A/B testing**: 100+ similar pages (e-commerce, programmatic, large publishers); engineering capacity; fails on tiny sites.
- **Gubur topical authority**: informational niches; new sites without link equity; teams with research discipline; high content-production budgets.
- **Dunning bottom-funnel SaaS**: B2B with sales demos as the KPI; competitor-rich markets.
- **Milligan/McGuirk digital PR**: brands with real data/stories; consumer or data-rich B2B; budget for newsroom operations.
- **Hawkins/Shaw/Blumenthal local stack**: local businesses; multi-location; US-centric data for Hawkins' study specifics.
- **Indig programmatic SEO**: page-matrix businesses (locations, features, comparisons) with template engineering; only with a quality floor per template.

## Evidence evaluation
- **FACT (Google-documented)**: crawl budget model, local triad, 404/410 handling (Mueller/Hawkins).
- **EMPIRICAL (large-N or replicated)**: Critchlow's test database (SEOs ≈ chance at predicting change outcomes; −27% title-tag incident; boilerplate-removal negative test); Hawkins' 8,186-business near-me study (address hiding correlation); McGuirk's 1-20 links-per-campaign distribution; Soulo's volume-vs-traffic-potential data; Milligan's 40k-link program; 2024-26 scaled-content enforcement cases.
- **HEURISTIC (practitioner consensus)**: impact×effort prioritization; kitchen-sink remediation; review velocity over average rating; content decay treadmill.
- **HYPOTHESIS/OPINION**: Gubur's patent-derived topical authority mechanics (self-reported 0→128k clicks case, UNVERIFIED); Koray's no-backlinks claim; AI-search citation dynamics (Indig's observational studies); "ChatGPT pulls from Google" (Dunning).

## Outliers (worth investigating)
- **Gubur's claim that topical authority can rank without backlinks** — contradicts the link consensus; his case studies are the only evidence (T3, self-published). Conditions where this works would be a genuinely valuable OS rule.
- **Hawkins' address-hiding counterexample** — platform guidance (hide address for SABs) empirically hurt a client's rankings; one of the few documented cases of platform advice being wrong for rankings.
- **Critchlow's "negative tests as superpower"** — the field's only systematic negative-knowledge program; if competitors don't test, avoiding −27% events compounds.
- **Indig's AI-citation decoupling from rankings** — classic SERP #1 with zero AI citations; a new metric class (AI citation share) that most SEO dashboards lack.
- **Moogan's sustainability test** — "if links stop when outreach stops, it's not a strategy": a generalizable test for any marketing channel, not just links.

## Failure knowledge (what repeatedly doesn't work — with sources)
1. Mass templated programmatic content without differentiation — 2024-26 scaled-content enforcement collapses (Search Engine Land 2025 case; Indig; Ray's local-landing-page pattern).
2. Publish-and-forget content — decay treadmill (Indig, G2 interview).
3. Untested best-practice changes — −27% title-tag incident; boilerplate removal negative (Critchlow/SearchPilot).
4. Pre-2012 link tactics (directories, spun content, web 2.0) — dead post-Penguin (Moogan); 2026: mass guest posts, PBNs, paid links, link exchanges pattern-detected by SpamBrain 3.0 (Optiseon 2026 field report).
5. Short-term testing of core-update recovery; cherry-picking remediation; rolling back good changes — whack-a-mole (Gabe).
6. Checklist dumps / 300-slide audits with no goal linkage — sit in folders (Stox, Solis).
7. High-volume keywords that convert no one; keyword volume as truth (Soulo; Dunning's weekly-observed mistake list).
8. Chasing virality in digital PR — distorts expectations; 1-20 links is normal (McGuirk).
9. Fixing GBP symptoms while supplier tier emits bad data — duplicates recur (Blumenthal's ecosystem model).
10. Crawl-budget obsession — mostly noise vs inventory management (Mueller, Stox).

## Collision Method sketch — "SEO Operating System"
- **Objective**: grow qualified organic demand (traffic → demos/revenue per stage) while minimizing core-update and scaled-content enforcement risk; track classic SERP + AI citations.
- **Prerequisites**: GSC access with ≥3 months data; crawl/log access; engineering relationship; business KPIs (not just rankings).
- **Inputs**: GSC (queries/pages/index coverage), crawl data, SERP landscape, competitor + AI-citation snapshot, update calendar (Barry Schwartz layer), business goal list.
- **Diagnosis** (gate everything): (1) If traffic drop: delta report → classify relevancy/intent/quality (Gabe+Ray); never remediate before classification. (2) If launch/migration: index coverage + rendering parity audit (Indigo). (3) If new site/stagnation: index/crawl health first (Mueller inventory rules, Stox order).
- **Decision tree**:
  - Technical: index/crawl issues → templates-not-pages → impact×effort matrix → 5-10 dev tickets + governance (Stox/Solis). Test template-level changes with controls when ≥100 similar pages (Critchlow); never deploy untested best-practice at scale.
  - Content: bottom-funnel intent filter (Dunning) → traffic-potential filter (Soulo) → topical coverage where link capacity is low (Gubur, conditioned) → audience-pain selection where buyers don't search (Law). Citable structure (answer-up-front, unique data) always (Dunning/Indig).
  - Programmatic: build template → validate uniqueness floor per page → ship waves → monitor indexation + volatility → kill or differentiate templates that duplicate (Indig + enforcement lessons).
  - Links: earned-only policy (editorial/data-driven PR; value trades) — Moogan's sustainability test; McGuirk's expectation calibration (1-20 links); Milligan's internal-data-first research; Dean's skyscraper as legacy option with intent-first overlay.
  - Local: GBP + relevance/distance/prominence triad; test single variables on real profiles (Hawkins); citations as consistency not links, supplier-tier-first (Shaw/Blumenthal); landing pages with real words; review velocity.
- **Execution**: developer-ticket format with acceptance criteria; SEO requirements baked into launch lifecycles (Indigo); velocity (keyword→publish in days, not months — Dunning).
- **Metrics**: primary = demos/revenue attributed to organic (B2B), or conversions (commerce); secondary = traffic, AI citation share (Indig), index coverage, core-update volatility exposure, referring domains from earned sources. Rankings are diagnostic, not the goal.
- **Stopping rules**: kill templates/pages that duplicate or produce zero engagement; stop tactics that fail Moogan's sustainability test; stop chasing keywords with volume but no traffic potential; stop short-term testing of site-level quality recovery.
- **Failure modes**: content decay; programmatic without quality floor; untested scale rollouts; volume-first selection; virality-chasing PR; single-cause attribution of drops.
- **Conditions**: applies broadly; depth of each sub-method depends on site type (e-commerce → testing + product-led; B2B SaaS → bottom-funnel + AI citations; local → GBP stack; media → topical authority + digital PR).
- **Limitations**: all non-Google practitioner claims are inference; local study data US-centric and time-bound; AI-search behavior changes monthly; correlation vs causation everywhere (Capper's filter).
- **Confidence**: T1 for the 10 consensus rules (multi-practitioner); T2 for sub-methods; T3 for Gubur's linkless ranking claims and AI-search specifics.
- **Key sources**: see per-practitioner files; top primary sources listed in the research summary.

## Field gaps
- Programmatic SEO's current success/failure rates lack public large-N data (Indig's paywalled work is the closest).
- AI-search citation methodology is young (Indig's studies; no standard metric yet).
- Local algorithm evidence is US-centric; GBP behavior changes fast.
- Post-2024 link value (SpamBrain-era) has vendor data but little independent research.
