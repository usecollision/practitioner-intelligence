---
practitioner: Trend-intelligence practice (Gartner Hype Cycle, Spate, Qmarkets)
role: institutional trend analysts and trend-intelligence platforms
company: Gartner (Jackie Fenn, 1995); Spate (consumer search-trend intelligence); Qmarkets (innovation management)
type: analyst|insider|researcher
confidence: T2
domains:
  - trend-detection
verified: 2026-08-15
sources_checked: 6
---

## Beliefs
- Hype is a feature of every emerging technology: the Hype Cycle exists because publicity peaks before commercial viability (Gartner methodology; Jackie Fenn 1995) (T1).
- Trends can be distinguished from fads by data shape, not instinct: fads are single peaks followed by rapid decline; durable trends show sustained upward movement (Spate) (T2).
- "Validation means confirming that a signal shows up in more than one place and that it is gaining momentum rather than holding flat. A single data point or one loud voice is rarely enough" (Qmarkets) (T2).
- Trend analysis is an ongoing capability, not a one-time exercise: annual reports are outdated within months (Qmarkets) (T2).

## Principles
- Durable trends develop gradually and spread: cross-category adoption, multiple demographics, platform diversity (Spate) (T2).
- Fads stay concentrated in one niche or demographic; if a concept can't branch into other categories, "eventually that fad will die" (Spate) (T2).
- Driver test: trends driven by durable forces (demographics, regulation, enabling technology, cost curves) persist; viral-moment and single-algorithm drivers fade (existing skill; Spate) (T2).
- Search volume is a ratio, not a census: use trajectory and relative interest (existing skill) (T2).

## Frameworks
- Gartner Hype Cycle: Innovation Trigger → Peak of Inflated Expectations → Trough of Disillusionment → Slope of Enlightenment → Plateau of Productivity; used as a risk/appetite lens (Gartner) (T1).
- Rogers adoption curve: innovators → early adopters → early/late majority → laggards — determines whether a trend is investable for your buyers (existing skill; Rogers) (T1).
- STEEP + horizon scanning: Social/Technological/Economic/Environmental/Political grouping to catch change before it appears in mainstream data (Qmarkets) (T2).
- Trend scoring: relevance, potential impact, uncertainty, likely timing — comparable criteria across candidates (Qmarkets) (T2).

## Processes
1. Classify: fad (months) / trend (1-3 years) / shift (5+ years, structural) (existing skill) (T2).
2. Multi-source scan: Google Trends (5-year view, rising related queries, geography), Reddit, GitHub/HN for tech, VC funding, job postings with new titles, conference agendas, analyst categories (existing skill) (T2).
3. Require 2+ independent sources before escalating a candidate (existing skill; Qmarkets) (T2).
4. Durability analysis: driver test + JTBD durability (old job + new solution = durable) + counter-signals; if you can't find the bear case, you haven't looked (existing skill) (T2).
5. Validate shape over 6-12 months: sustained growth, cross-category spread, seasonality consistent across years (Spate) (T2).
6. Map to opportunity: ICP fit filter, timing choice (first-mover vs fast-follower), rough size; output trend cards with actions ignore/watch/experiment/invest + kill criteria (existing skill) (T2).
7. Re-check protocol: monthly radar, quarterly deep-dive, 3-month re-check with kill on stalled velocity (existing skill; Qmarkets cadence) (T2).

## Heuristics
- Spike + rising related queries = broadening interest; flat line = niche; spike + decline = fad (existing skill; Spate) (T2).
- Hype signals (news volume, conference panels, vendor count) grow fastest near the peak — treat hype as a contrarian entry-timing signal (existing skill + Gartner) (T2).
- Job titles that didn't exist are a strong early signal (existing skill) (T2).
- Examine related-search depth and question types: practical-intent queries indicate real exploration vs novelty (Spate) (T2).

## Inputs
Topic area, time horizon, business context, access to Trends/Reddit/GitHub/funding/job data, prior trend log.

## Outputs
Trend radar, trend cards (definition/evidence/driver/durability/ICP fit/action), durability assessments, watchlist with kill criteria, re-check dates.

## Metrics
Source-count per candidate (2+ rule), kill rate, re-check adherence, % candidates with driver+counter-evidence, time from first signal to action.

## Decision rules
- IF a candidate shows a spike without 6-12 months of sustained growth THEN classify fad; do not invest (Spate, T2).
- IF evidence comes from one source only THEN treat as hypothesis; require 2+ independent source types (Qmarkets/existing, T2).
- IF a concept stays confined to one category or demographic THEN expect low durability (Spate, T2).
- IF hype signals are rising fast (vendor count, panels, news) THEN treat as a contrarian timing signal for entry (Gartner/existing, T2).
- IF no counter-evidence can be found THEN the bear case hasn't been hunted — search harder before adopting (existing, T2).
- IF a watched trend stalls at the 3-month re-check THEN kill it and log the kill (existing, T2).
- IF the trend touches no ICP job THEN output "watch," not "invest," regardless of size (existing, T2).

## Failure modes
- Confusing fad with shift — every hype peak looks structural at the peak (existing skill) (T2).
- Single-source confirmation: one viral thread treated as a movement (existing skill; Qmarkets) (T2).
- Investing on a single ingredient/viral spike while interest cools (snail mucin example — Spate) (T2).
- One-time trend reports that go stale; no ownership; no kill criteria (Qmarkets) (T2).
- Applying consumer hype to B2B ICPs without a fit check (existing skill) (T2).

## Contrarian beliefs
- The biggest risk is not missing trends but "chasing noise": weak signals consume attention but offer little strategic value (Qmarkets) (T2).

## Conditions
Works when there is a time series to observe and a defined ICP; the 6-12 month validation window is too slow for fast-fashion-style decision cycles — those need velocity-based heuristics instead.

## Limitations
Hype Cycle is descriptive/risk-framing, not a forecast; search data misses non-search behavior (B2B, offline); durability judgments are probabilistic, not certain.

## Sources
1. Gartner — Hype Cycle Research Methodology | gartner.com/en/research/methodologies/gartner-hype-cycle | T1 | 2026-08-15
2. Spate — How to Tell if a Trend is a Fad or Long-Term | spate.nyc/blog/how-to-interpret-trend-signals | T2 | 2026-08-15
3. Qmarkets — Trend Analysis: A Practical Guide (pattern recognition, STEEP, scoring) | qmarkets.net/resources/article/trend-analysis | T2 | 2026-08-15
4. Productfolio — Hype Cycle explainer (Jackie Fenn 1995, 100+ cycles/year) | productfolio.com/gartner-hype-cycle | T3 | 2026-08-15
5. The Code Forest — Early trend detection (leading indicators, pattern shapes) | thecodeforest.github.io/post/early_trend_detection.html | T3 | 2026-08-15
6. TrendScouters — Trend research methods guide | trendscouters.com/trend-research-methods-the-ultimate-guide-to-spotting-validating-and-acting-on-emerging-trends | T3 | 2026-08-15
