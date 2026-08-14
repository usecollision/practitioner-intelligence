---
practitioner: Eric Seufert
role: Analyst/strategist, founder of Mobile Dev Memo; ex-User Growth/Strategy at Odeeo, ex-Facebook/Google
company: Mobile Dev Memo (mobiledevmemo.com)
type: analyst
confidence: T1
domains:
  - paid-strategy
  - media-planning
  - incrementality
  - attribution
  - mobile-user-acquisition
verified: 2026-08-14
sources_checked: 4
---

# Eric Seufert

The ad-economics and incrementality voice for mobile/SaaS growth. His core thesis: platform attribution gives a "veneer of control" that misleads budget allocation; the future of paid media decision-making is econometric, incrementality-based, and run by "marketing economists."

## Beliefs
- "Last-click attribution provides advertisers with a veneer of control, like a security blanket… this measurability is really an illusion: some percentage of spend obviously produces incremental revenue, but… once an advertiser extends their spend beyond a single channel, they are guaranteed to be losing money to redundant, superfluous spend" (EMPIRICAL/OPINION, 2020 essay).
- "Anything that was true in 2020 likely represents an emergency now" — signal loss (ATT, IDFA deprecation) made probabilistic measurement mandatory, not optional (OPINION, 2023).
- Media Mix Modeling (MMM) is the future of advertising measurement: top-down correlation of spend by channel → sales, with exogenous factors; sidesteps last-click, overlap, and signal-loss problems (FRAMEWORK, 2020 essay).
- Incrementality is the true question in advertising: "if you cut this spend tomorrow, how much revenue would actually disappear?" (FRAMEWORK, podcast with Garrett Johnson, 2024).
- Ad fraud is mostly mislabeled incrementality: "Most cases of ad fraud are really just cases of lack of incrementality" — marketers blame a "nefarious bogeyman" for what is overlapping, redundant spend (OPINION/EMPIRICAL, 2020).
- Unit economics must be granular and scale-aware or they are useless (EMPIRICAL, 2018 LTV/CAC essay).

## Principles
- **Measurement validity only at the macro level**: when users "swirl around within the lines of sight of various ad platforms," bottoms-up attribution can't guide spend decisions; macro frameworks (MMM, MER-style aggregates) are the only trustworthy layer (FRAMEWORK).
- **Dual-workflow operation**: cross-channel econometric models (MMM) are updated monthly/quarterly (smooth effects, capture data); within-channel campaign optimization (creative, budget splits) happens weekly or more. These operate on different cadences and must not be conflated (FRAMEWORK, 2023).
- **Automation increases, not decreases, the need for incrementality measurement** — automated systems make onboarding new channels easier, so redundant spend grows faster (OPINION, 2020).
- **Payback window, not LTV, is the strategic metric**: "If an advertiser is cash-constrained, a Day 365 LTV is irrelevant. Advertisers are better served focusing on month-to-month cash generation" (EMPIRICAL/OPINION, 2019). "Companies can go broke running marketing campaigns that are profitable over 180-day timelines" (2018).
- **LTV/CAC only actionable at campaign-targeting granularity**: "The 180-Day LTV of iOS users we acquire in the US on Facebook is $5 against a CAC of $4 on total daily spend of $80,000" — segment, time-window, and scale are all required context (EMPIRICAL, 2018).

## Frameworks
- **MMM (Media Mix Modeling)** — top-down econometric mapping of spend → conversions with exogenous factors; the measurement backbone (FRAMEWORK).
- **Incrementality measurement** — ghost ads (randomized auction-level holdouts, from Garrett Johnson's research), geo holdouts, conversion lift studies (FRAMEWORK, podcast 2024).
- **Marketing economist role** — the modern growth team is staffed by analysts/engineers/data scientists who run econometric models, not media buyers (FRAMEWORK, 2020/2023).
- **Payback-window / cash-flow framework** — cohort daily revenues compounding to daily P&L vs cash in bank; determines how aggressively you can buy (FRAMEWORK, 2018).

## Processes
- For measurement: build the MMM; validate channels at macro level; run incrementality tests (ghost ads, geo holdouts, lift studies) for channels where incrementality is suspect; feed results into budget allocation; run weekly within-channel optimization; re-run macro models monthly/quarterly (FRAMEWORK, 2020+2023 essays).
- For UA strategy: decompose LTV curves by platform/segment/geo/time-window; set the payback window by cash position; compute CAC at that window; scale only within cash-flow constraints (FRAMEWORK, 2018).

## Heuristics
- "Once you extend spend beyond a single channel you are guaranteed to be losing money to redundant spend" — overlap is certain; the question is how much (EMPIRICAL/OPINION).
- Attribution-based reporting overstates incrementality; MMM/MER understates channel-level detail — both needed, at different cadences (FRAMEWORK).
- If a metric can't be tied to a campaign-targetable segment and a time window, it isn't decision-grade (EMPIRICAL).

## Tactics
- Stand up MMM before scaling multi-channel spend; pair it with an incrementality testing program (FRAMEWORK).
- Hire/assign a "marketing economist" function rather than more media buyers (OPINION/FRAMEWORK).
- Test channels that platforms self-attribute (e.g., branded search, retargeting) with holdouts — these are where reported ROAS diverges most from true incrementality (FRAMEWORK, podcast).

## Tools
- MMM platforms/models, incrementality testing (ghost ads via Google/Meta, geo holdouts), cohort/LTV analytics, cash-flow modeling. (He interviews the vendors; no proprietary tool.)

## Inputs
- Spend by channel, conversion/sales data, exogenous factors (seasonality, competitor spend, launches), cash position and payback-window tolerance, LTV curves by segment, incrementality test results.

## Outputs
- Budget allocation recommendations (channel level), measurement infrastructure guidance, UA team design, weekly/monthly analysis (Mobile Dev Memo essays and podcast).

## Metrics
- Incremental ROAS, MMM channel contributions, payback window, cohort LTV at window (Day 30/90/180), MER-style macro ratios (implicit), CAC by segment; cash-flow schedule (EMPIRICAL set).

## Decision rules
- **Allocate budget against incremental contribution, not attributed ROAS**: when channel reported ROAS and iROAS diverge, budget against iROAS (FRAMEWORK).
- **Choose the payback window by cash position, not by product potential**: cash-constrained → shorter window, less aggressive scaling (EMPIRICAL).
- **Run macro (MMM) and micro (campaign) decisions on different cadences** — monthly/quarterly reallocation, weekly optimization (FRAMEWORK).
- **Do not trust a channel you cannot incrementality-test** — measure the suspect channels (self-attributing, retargeting, brand search) first (FRAMEWORK).

## Failure modes
- **Attribution-driven misallocation**: last-click/platform attribution over-credits redundant channels; advertisers "guaranteed" to lose money on superfluous spend once multi-channel (EMPIRICAL/OPINION).
- **Scaling on unit economics without scale context**: profitable-looking per-cohort economics at small spend, then CAC inflation as targeting broadens (EMPIRICAL, 2018).
- **Cash-flow blindness**: running campaigns profitable over 180-day timelines while going broke (EMPIRICAL).
- **Calling incrementality problems "fraud"**: misdiagnosis leads to fraud tooling instead of fixing overlap/redundancy (OPINION).
- **Treating attribution as sufficient after signal loss**: the "veneer of control" cracks without IDFA; teams that didn't move to MMM lost their measurement floor (OPINION).

## Contrarian beliefs
- Bottom-up, click-based attribution is "an anachronistic performance assessment methodology" — even for direct-response channels (OPINION, 2020).
- Marketing teams of the future are data-science teams; media buying is being automated away (OPINION).
- LTV as a concept should be retired in favor of payback windows and cash-flow management (OPINION, 2019).

## Examples
- Uber's ad fraud case: "more an example of fraud powered by social engineering… than systemic fraud" — i.e., incrementality misread as fraud (EMPIRICAL, cited in 2020 essay).
- The 2020→2023 trajectory: MMM predictions ("anything true in 2020 is an emergency now") validated by ATT-era signal loss (OPINION).

## Conditions
- Applies most directly to: mobile apps, digital-first/SaaS products, performance-dominated spend, teams with data capability, multi-channel advertisers with overlap risk.
- MMM requires data volume and modeling capability — under-resourced teams may be better served by simpler macro ratios (MER) (OPINION; see synthesis).

## Limitations
- Mobile/app-centric; less direct guidance for brand media, TV, or offline (FRAMEWORK gap).
- MMM is expensive, hard to maintain, and can't plug into campaign workflows directly (his own 2023 essay admits econometric models "cannot be connected to marketing workflow or plugged into reporting infrastructure" — hence the dual-workflow answer).
- No position on brand-vs-activation split (the Binet/Field question) — his layer is measurement/allocation within paid, not long/short balance (FRAMEWORK gap). Complements rather than contradicts Binet/Field.

## Sources
1. Eric Seufert, "Media mix models are the future of mobile advertising" | mobiledevmemo.com | tier 1 | 2026-08-14
2. Eric Seufert, "The emerging marketing economist" | mobiledevmemo.com | tier 1 | 2026-08-14
3. Eric Seufert, "How does LTV/CAC fit into a growth strategy?" | mobiledevmemo.com | tier 1 | 2026-08-14
4. Eric Seufert, "It's time to retire the LTV metric" | mobiledevmemo.com | tier 1 | 2026-08-14
5. Mobile Dev Memo podcast, "What is advertising incrementality? (with Garrett Johnson)" | mobiledevmemo.com | tier 1 | 2026-08-14
