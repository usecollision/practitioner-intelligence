---
practitioner: John Mueller
role: Search Advocate (Google insider)
company: Google
type: insider
confidence: T1
domains:
  - SEO (indexation, crawling, quality)
verified: 2026-08-14
sources_checked: 2
---

## Beliefs
- Most SEO "crawl budget" anxiety is misplaced: capacity limits auto-adjust with site health, and demand is driven by perceived inventory, popularity, and staleness — the factor sites control is inventory quality (FACT, from Google's own crawl budget documentation which he maintains/represents).
- Google evaluates sites overall (content, UX, ads, presentation, sources) in quality assessments — the ground truth behind Gabe's kitchen-sink approach (FACT, cited in Gabe's post).
- 404/410 for removed content is a strong signal; blocking via robots.txt leaves URLs in the crawl queue longer (FACT).

## Frameworks
- **Crawl budget = crawl capacity limit × crawl demand**: capacity = server health/hostload (latency, TTFB, 5xx, 429s); demand = perceived inventory, popularity, staleness (FRAMEWORK — Google's official model).
- **Perceived inventory management**: guide Google on what to crawl rather than trying to force crawling (FRAMEWORK).

## Processes (per Google guidance)
1. Keep server responses stable and fast — capacity limit rises with health, falls with 5xx/429/latency.
2. Eliminate duplicate/parameter URLs; block unimportant ones (sort orders, infinite-scroll dupes) with robots.txt.
3. Return 404/410 for permanently removed pages (keeps them out of queues).
4. Eliminate soft 404s (they keep getting crawled).
5. Keep sitemaps up to date with lastmod.
6. Return 304 Not Modified where applicable.

## Heuristics
- Every site starts with the same conservative crawl capacity; it grows only with demonstrated health (FACT).
- Popular URLs get crawled more often (freshness of popular content matters) (FACT).
- Site moves (migrations) trigger increased crawl demand — plan for reprocessing (FACT).

## Tactics
- Prefer consolidation (canonical/merge) over blocking; block only when consolidation is impossible (TACTIC).
- Treat crawl health as an ops concern: stable TTFB, no 5xx storms, no rate-limit spikes (TACTIC).

## Tools
- Google Search Console (Page Indexing report, sitemaps), robots.txt tester.

## Inputs
- Server logs (response codes, latency), GSC index coverage, URL inventory.

## Outputs
- Crawl/inventory guidance; indexation diagnostics.

## Metrics
- Crawl stats, index coverage, soft-404 counts, server error rates.

## Decision rules
- Perceived inventory is the factor you control most → manage URL inventory before touching crawl rate knobs (DECISION RULE).
- Page removed permanently → 410/404, never robots.txt (DECISION RULE).
- URLs duplicated by parameters/sorting → consolidate; only block when you can't consolidate (DECISION RULE).
- 5xx/429s rising → fix server health first; crawl capacity will follow (DECISION RULE).

## Failure modes
- Treating crawl budget as a lever to force more crawling (it's mostly a function of demand and health).
- Blocking important content in robots.txt to "save budget" — blocks indexation (warned against implicitly by the model).
- Letting soft 404s and stale sitemaps persist — waste and staleness (FACT).

## Contrarian beliefs
- For most sites, crawl budget simply doesn't matter — the doc explicitly notes limits exist but demand is the binding constraint for typical sites (OPINION consistent with his Office Hours statements; matches Patrick Stox's "ignore the noise").

## Conditions
- The model matters for: large sites, sites with parameter-heavy URLs, sites with 5xx problems, sites whose pages change often, migrations.

## Limitations
- Google's official line is deliberately non-exhaustive (it doesn't reveal ranking weights); Office Hours answers are situational; guidance changes as Google's infrastructure changes (e.g., rendering changes over time).

## Sources
1. "Crawl Budget Management — Google Crawling Infrastructure" | https://developers.google.com/crawling/docs/crawl-budget | official Google documentation | tier 1 | 2026-08-14
2. Mueller's statement on site-wide quality evaluation cited in Glenn Gabe's core update post | https://www.gsqi.com/marketing-blog/google-broad-core-updates-important-points-and-frequently-answered-questions/ | tier 1 (secondary citation of primary statement) | 2026-08-14
