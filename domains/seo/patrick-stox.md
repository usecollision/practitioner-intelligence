---
practitioner: Patrick Stox
role: Product Advisor / Technical SEO (ex-Ahrefs)
company: Ahrefs (formerly); independent (patrickstox.com)
type: practitioner|educator
confidence: T1
domains:
  - Technical SEO
  - Site architecture
  - Crawlers
verified: 2026-08-14
sources_checked: 2
---

## Beliefs
- An enterprise SEO audit is not a bigger checklist — it's a different job: scoping, segmentation, and stakeholder alignment dominate (OPINION/FRAMEWORK).
- You can't audit everything; "No major site is technically perfect. To get there would be a waste of money" (OPINION).
- Prioritize by business impact and feasibility; the deliverable is 5-10 fixes in developer-ticket format, not a 300-slide deck (FRAMEWORK).
- The hardest part of SEO is organizational, not technical — getting engineering/content/legal to agree and act (OPINION).

## Frameworks
- **Impact/effort matrix with business-value translation**: crawl/index issues first (they gate everything downstream), then on-page at scale, then link work (FRAMEWORK).
- **Templates, not pages**: one bad canonical template hits hundreds of thousands of URLs — think in template units (FRAMEWORK).
- **Governance wrap**: fixes must be protected from regression by process, not just shipped (FRAMEWORK).

## Processes (enterprise audit)
1. Stakeholder interviews — find the real pain points (traffic drop, launch, redesign, compliance, migration); map owners (engineering owns templates/CDN, content owns copy, legal can veto).
2. Segment the site by page type, region, language, or platform — unsegmented full crawls of 40M+ URLs produce unusable data and take 48-72h.
3. Scope ruthlessly: audit only segments with traffic/revenue/pain. Focused segment audit ~10h; full enterprise audit 50-70h.
4. Start with indexing (GSC Page Indexing report) before content or links.
5. Produce 5-10 prioritized issues, each with: plain-language problem, quantified business impact, developer-ticket implementation steps (acceptance criteria, reproduction steps).
6. Wrap governance around fixes.

## Heuristics
- Crawl waste (parameter combos, faceted URLs, infinite spaces) is the first thing to kill (HEURISTIC).
- Rendering gaps between server output and what Googlebot sees are common and under-detected (HEURISTIC).
- If a fix can't be expressed as a ticket with acceptance criteria, it won't ship (HEURISTIC).

## Tactics
- Fix indexation problems first: orphaned pages, noindex mistakes, canonical conflicts (TACTIC).
- Kill redirect chains/loops and broken internal links; fix internal linking that buries important pages (TACTIC).
- Only fix Core Web Vitals issues that are "actually worth fixing" (TACTIC — anti-CWV-alarmism stance).
- Use site-structure reports and custom filters for segmentation (TACTIC).

## Tools
- Sitebulb (he built one of the industry's most popular website auditors — Sitebulb), Google Search Console, enterprise crawlers.

## Inputs
- Stakeholder pain points; site segments; GSC index data; crawl data; template/CMS inventory.

## Outputs
- Prioritized engineering-ready fix lists; enterprise audit roadmaps (12-month); governance documentation.

## Metrics
- Business impact per fix (traffic/revenue gated); index coverage; crawl efficiency.

## Decision rules
- Index/crawl issues first, on-page at scale second, links third — because indexing gates everything (DECISION RULE).
- Impact high + effort low → ship now; impact low + effort high → drop; everything else → pipeline (DECISION RULE, matches Aleyda Solis' matrix).
- When a single template is broken, fix the template not the pages (DECISION RULE).
- Audit only segments with traffic, revenue, or known pain (DECISION RULE).

## Failure modes
- The 300-slide deck that sits in a folder — "the best audit in the world is worthless if it sits in a folder" (warned against).
- Auditing everything → expensive, wasted time, unusable output.
- Unsegmented full-site crawls at enterprise scale (48-72h, data nobody can use).
- Fixes without governance → regression (his stated reason for wrapping audits in governance).

## Contrarian beliefs
- Crawl budget is mostly noise at small/medium scale — the interesting problems are templates, rendering, and index coverage (OPINION, consistent with Mueller's guidance that perceived inventory is the controllable factor).

## Examples
- Audited 1M+ websites with his auditor; enterprise clients with 40M-URL sites (EXAMPLE).

## Conditions
- Enterprise/multi-CMS/multi-region sites benefit most; the impact/effort matrix works at any scale.
- Requires engineering stakeholder access — fails in orgs without a dev relationship.

## Limitations
- Template-first thinking under-weights unique high-value pages; stakeholder-interview-driven scoping can miss silent issues; audit quality depends on crawl + GSC data accuracy.

## Sources
1. "Technical SEO Audits: Prioritized, Engineering-Ready Fixes" | https://patrickstox.com/services/technical-seo-audits/ | primary practitioner site | tier 1 | 2026-08-14
2. "Enterprise SEO Audit" | https://patrickstox.com/enterprise-seo/audits-and-governance/enterprise-seo-audit/ | primary practitioner site | tier 1 | 2026-08-14
