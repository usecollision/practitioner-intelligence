# COMPLETE FAILURE KNOWLEDGE BASE — what repeatedly doesn't work

Assembled 2026-08-15 from all syntheses. Negative knowledge is first-class: each item carries sources and confidence.

## aeo
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



## analytics
## Failure knowledge
- Dashboards with 30+ metrics and no targets → nobody looks, decisions happen elsewhere (Kaushik; T1).
- Celebrating metrics that don't change strategy when they drop (Cutler: "if a number goes up and the only action is a furrowed brow, it's vanity") (T1).
- Metric becomes a target → becomes vanity/gamed (Cutler: Goodhart's law in practice; "once a metric becomes a signal of doing a good/bad job, people will make sure it goes up") (T1).
- Averages masking distribution failure (Biddle; T1).
- Treating NSM as the only metric → teams wake up unable to influence it, disengage (Cutler; T1).
- GA4 setup sins (Seiden): no custom events, no registered dimensions, default attribution accepted blindly, data retention left at 2 months (T1).



## competitive
## Failure knowledge
- Harvey Balls without scoring rigor (Kellogg; T1).
- Research-for-knowledge's-sake: reports nobody reads, no plays created (Kellogg; T1).
- Positioning against phantom competitors (Dunford; T1).
- Ignoring the status quo as a competitor (Dunford: 25% no-decision stat; T1).
- Comparing features instead of sales plays and company strategy (Kellogg: competitor's "end run" example; T1).



## creative-longtail
## Failure knowledge
- Testing variations instead of concepts (hawky; Denney — "ten crops of one ad is one test").
- Opening with features/product instead of pain (Hormozi: "almost nobody scrolls past a feature list").
- Briefs too vague ("make it authentic!") OR too restrictive (17 bullet points) — both kill UGC output (ATTN).
- Over-scripting UGC until authenticity dies (Pixis UGC note; InfluenceFlow).
- Judging creatives before minimum spend / underfunded tests (AdGenz; paid-strategy.md Spike rule).
- Ignoring fatigue: ad fatigue (one ad overexposed) vs creative fatigue (same KIND of ads feel repetitive) — frequency caps + rotation, not just new targeting (AppsFlyer). Denney: accounts die from creative fatigue, not targeting.
- No creative taxonomy/tagging: without standardized naming (e.g. [Platform]-[Campaign]-[Angle]-[Format]-[Version], ORCA) you cannot learn why winners won (scalable.ad, beefed.ai).
- One message for all awareness levels (Schwartz, messaging.md) — cold vs retargeting need different hooks/claims.
- Running UGC without rights fixed in the brief/contract — takedowns, strikes, scope disputes (SideShift; ugc-advertising skill).



## dtc
## Failure knowledge
- Scaling paid on a store with weak unit economics → cash bleed that ROAS hides (Youderian: winners' edge is margin+overhead, not ads; Sharma: "invisible cash bleeds") (T1).
- Blended ROAS >1 as the only goal → breakeven-forever trap; no contribution margin, no profit (T2).
- Ignoring repeat rate → CAC payback never shortens; every order is a new acquisition (Firestone/Youderian; T2).
- Creative fatigue undiagnosed (low CPM misread as audience problem; Sharma) (T1).
- Amazon-first margin erosion (Youderian data; T1).



## email
## Failure knowledge
- **Bought lists / permissionless sending:** destroys reputation; complaints drive brand reputation at major providers (Atkins); Gmail rules now enforce consequences.
- **Ignoring recipient feedback:** "the biggest reason senders fail" (Atkins) — no unsubscribe visibility, no complaint monitoring, no engagement segmentation.
- **Sending to stale/inactive segments:** decays engagement metrics and reputation; White: qualify active audiences, winback, then re-permission or prune.
- **Time-based-only sequences:** sending advanced content to users stuck at step one (Geisler).
- **"View in browser" preheaders** and same-time-for-all-types sends (Schwedelson).
- **Hacked email infrastructure** (registrar forwarding + Gmail Send-as): breaks unpredictably; DMARC failures after migrations (Iverson, 2025 case wave).
- **Optimizing the email in isolation** while landing page/checkout friction kills conversion (Pay).
- **Email-silo marketing** — judging email success without journey context (Pay, White).
- **Over-emailing without engagement feedback:** Atkins' "scaling irrelevant communication creates more irrelevant communication."



## gtm
## Failure knowledge
- Scaling channels before PMF → wasted spend, churn (Ellis, Balfour; T1/T2).
- Forcing viral loops without product mechanic → dead loop; viral coefficient <1 means paid for every user (Balfour; FRAMEWORK).
- "Spray and pray" outbound/demand capture only → competing in 4-vendor deals at the bottom of funnel, $1M/mo Google spend with 36-month CAC payback (Walker example; T1 anecdote).
- Chasing North Star vanity metric without inputs (see analytics synthesis).
- Hiring a "growth team" with no decision rights/roadmap access (Balfour: growth must ship product changes, not just campaigns) (T2).
- GTM motion mismatch: PLG company hiring enterprise AE team too early, or sales-led product with no sales enablement (Rachitsky; T2).



## market-intel
## Failure knowledge
- "1% of a huge market" logic — investors dismiss it; it's wishful thinking, not calculation (Zimt, bridginglocal, a16z toothbrush-to-China example) (T1).
- TAM too small OR SAM as TAM — the two classic pitch-deck failures (TheVCfactory) (T2).
- Confirmation bias: starting from the desired conclusion; "everyone is our customer" fallacy; single-method reliance (Ainna) (T2).
- False precision: a single point estimate ($87.3M) invites attack; ranges/scenarios required (Zimt) (T2).
- Stale data: reports >12-18 months old poison the analysis (Zimt) (T2).
- Five Forces misuse: analyzing the company not the industry; rating without evidence; boundary too broad ("B2B SaaS"); treating forces as independent/static; averaging numeric scores into false precision (Investopedia, DrinkBird, Visual-Paradigm) (T1).
- Forecasting failures: anchoring to leadership's desired number; one method only; quietly picking the rosier method when gap >2x; point estimates; no forecast-vs-actual log (existing skill, corroborated by FP&A practice: scenarios built as reporting exercises don't influence decisions) (T2).
- Scenario traps: too many scenarios → paralysis; scenarios muddle a bold vision; discarding far-fetched scenarios too quickly — "often the most valuable ones seem the most far-fetched" (McKinsey) (T1).
- Bass failure #1: bad analog selection ("same industry" ≠ similar diffusion); skipping sanity checks (installed base, year-1 sell-through laugh test, inflection-point timing) (T2).
- Demand validation theater: no written no-go criteria → analysis always lands on "go"; validating the problem but not willingness to pay (survey "80% want it" vs 0% would pay $50/mo) (Zimt, IdeaCrystal) (T2).
- Trend traps: treating a single viral thread as a movement; reading one year of data as growth (seasonality as trend); fads concentrated in one demographic die; no kill criteria → watchlists never shrink (Spate, Qmarkets, existing skill) (T2).
- Market-map traps: mapping everything (30 attributes hides the 3 that move deals); plotting from vendor claims alone; empty quadrant ≠ opportunity without demand evidence (industry-lens, Umbrex) (T2).



## messaging
## Failure knowledge
- Writing before research (Wiebe: 99% of the time wrong; Ogilvy; Hopkins).
- Direct claims in saturated markets (Schwartz stage mismatch — the classic "we tried simple copy and it didn't work").
- One message for all awareness levels (Schwartz: retargeting vs cold traffic category error).
- Optimizing pages instead of funnels (Price).
- Copy projects without baseline analytics (Price: unmeasurable work; Hopkins: gambling).
- Discounting the main offer instead of stacking value (Hormozi).
- Polished, personality-free email (Belgray: people want relatable).
- Rollout craters from list bias (Halbert's $160k lesson).
- Generic/AI "zombified" content without voice (Kieran Drew; Belgray warns to use AI for alternatives, not authorship).
- Copy for markets where nobody is buying yet (Halbert starving crowd; Schwartz desire-channeling).



## outbound
## Failure knowledge
- **Bought/rented lists:** never; list quality > copy (all practitioners; Gmail rules make it worse).
- **Volume spikes:** "1,000 emails Monday, none Tuesday" → near-certain spam (Berman); Gmail docs: increase volume slowly, consistent rate, no sudden doubling.
- **Fake personalization:** "Curious to know…", pretending to know the business, template-personalized inserts — deleted instantly (Berman, Efti, Allred).
- **Pitching a service instead of an offer** (Berman: zero-response campaigns until entry-point offer built).
- **Over-follow-up:** >2 follow-ups within a week trains spam filters (Berman); irrelevant 11-touch stacks = interrupting 11x instead of once (Ingram).
- **Copying frameworks without the system:** most Predictable Revenue copies failed (Ross) — bolt-on cadences without architecture, data, and classification don't work.
- **Ignoring measurement:** 7% of senders don't track replies at all (Mailshake); Ross: dashboards usually wrong — fix tracking before optimizing.
- **Not classifying replies:** replies that aren't "book a meeting" (competitor mentions, referrals, "talk to X") are lost value (Ross Outbound Validation; Mailshake expert quote).



## partnerships
## Failure knowledge
- Treating affiliates as employees → stagnation, program reputation damage (Prussakov). (T1)
- Setup-phase mistakes kill programs before launch: no terms, no creatives, no tracking plan, no commission strategy (Prussakov's 8 setup mistakes, analyzed 1,000+ programs). (T1)
- Rewarding signups instead of activations → fraud + low-quality users (Viral Loops practice). (T2)
- Buying influencer reach without measurement → waste; creator content underperforming organic shouldn't be scaled (Gagliese practice). (T2)
- Launching referral with K < 0.15 and expecting a loop → disappointment; it's a channel, not a flywheel (Viral Loops math). (EMPIRICAL, T1)



## positioning
## Failure knowledge
- "The next [leader]" positioning guarantees failure (Kellogg T1 — Powerset, object DBMS, SaaS-next-Salesforce).
- Workshops as sticky-note brainstorms produce enthusiasm, not alignment; consensus docs without evidence fall apart on first use (Bare Strategy T2).
- CEO anchoring in the room kills workshops unless exec is interviewed in pre-work and disagreements return to buyer evidence (Bare Strategy T2).
- Starting from "the problem" yields vague positioning (Dunford T1).
- Staying in the market you started in (Dunford T1).
- Category design without funding/authority to mobilize (Lochhead's own preconditions T2; Kellogg T1).
- Small-market products fail regardless of positioning quality (Shah T1 — dogo/Draftsend).
- Skipping beachhead: broad launch before references exist (Moore T1).
- AI-generated competitor assumptions (Dunford T1).



## pr-launches
## Failure knowledge
- Long, formatted, exclamation-heavy pitches → deleted (Zitron). (T1)
- Pitching hundreds of reporters the same email → reputation damage, "duh that's obvious" replies. (T1)
- Newsjacking with no legitimate tie → tone-deaf coverage or none (Meerman Scott's own framing: credibility is the gate). (T2)
- Late newsjacking (24h+) → irrelevant; the story has moved. (T2)
- PH launches without pre-assembled audience + engagement plan → buried; bots/ballot rigging are policed by the community. (KWD, T2)
- Treating PR as a campaign with a preset script and timeline (old model) → "a single afternoon can blast the wheels off your narrative" (Meerman Scott). (T2)



## pricing
## Failure knowledge
- **Ramanujam's four failure patterns** (72% of new products fail financially; T1): (1) Feature shock — too many features, overpriced, no segment resonance; (2) Minivation — right product, priced too low, leaves revenue; (3) Hidden gem — product customers love but company can't monetize (no value metric); (4) Undead — "me too" product nobody asked for. Fix: WTP + feature-preference research before launch, price anchored to value metric (EMPIRICAL, T1).
- Last-minute pricing (price set after product built) — the root cause of most failures (Ramanujam; T1).
- Discounting as default: Campbell 2018 research — ~80% of SaaS companies discount ≥25% to acquire; discounting destroys the WTP curve you measured (EMPIRICAL, T1).
- Copying competitor pricing without own WTP data (Poyar, Campbell; T2).
- Usage pricing without spend visibility/control for buyers → churn and CFO resistance (Poyar 2026; T1).



## social
## Failure knowledge
- Engagement pods / DM spam / comment-and-run: detected and penalized (vDB: comment reach -35% when you ghost replies). (T2)
- Deleting underperforming posts signals instability; let them live. (vDB, T2)
- Gating content too early: free content gets 20-25x more reach. (vDB, T2)
- Reddit: scripted corporate responses get downvoted; brands absent get discussed without them (30/117 SaaS brands absent, 23 abandoned subreddits). (SEL study, EMPIRICAL T2)
- Communities die from unclear purpose and under-investment, not tool choice (Millington/Spinks/Jones consensus).
- YouTube: ignoring retention drop-off points (e.g. one client lost viewers at the word "module") burns watch time; generic "post shorts" advice without retention mechanics fails (Schmoyer).


