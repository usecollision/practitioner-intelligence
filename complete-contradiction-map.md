# COMPLETE CONTRADICTION MAP — where experts disagree, with conditions

Assembled 2026-08-15. Every disagreement carries the conditions under which each side is correct.

## aeo — Disagreement
## Disagreement
1. **Is GEO a new discipline or just SEO?** Ryan Law: "GEO, LLMO, AEO… it's all just SEO" — mechanism is relevance+authority on/off site; separate GEO programs are waste. vs. Stanford group, Solis, Walsh, van Berkel: GEO is a distinct optimization layer (different retrieval, citation mechanics, no-JS rendering, unlinked mentions). **Condition**: Law is right about mechanism (relevance/authority transfer); the "delta" camp is right about surface (citation behavior, mention weight, content formats). Operationally: run one content program, but track AI-specific metrics. [OPINION vs FRAMEWORK]
2. **Does schema move AI citations?** Schema vendors (van Berkel) and 89% of SEO sources say yes; Ahrefs' controlled test of 1,885 pages adding JSON-LD found no uplift (AIO −4.6%, AI Mode +2.4%, ChatGPT +2.2%, effectively null). Schema is confounded: cited pages are 3x more likely to have schema because better sites do everything better. **Condition**: schema as *content-planning lens* (Crestodina) and *enterprise knowledge-graph infrastructure* (van Berkel) survives; schema as *quick citation lever* does not. [EMPIRICAL null vs vendor OPINION]
3. **Measurement unit**: blended "AI visibility score" (most tools) vs Indig's three-number framework (presence/portability/concentration). **Condition**: blended scores only OK when buyer uses one engine (e.g., local search dominated by AIO); otherwise misleading by construction.
4. **Citation decay**: Crestodina: AI citations decay after ~13 weeks → quarterly refreshes. Indig's longitudinal data shows slight convergence (universal overlap 2.2% → 2.7%) but no decay model published. **Condition**: freshness matters for news/trending; evergreen entity pages (Wikipedia-style) persist. [single-source EMPIRICAL vs EMPIRICAL]
5. **GEO manipulation threat level**: Stanford's 2026 GEO-Bench shows black-box content rewriting can match gradient-based attacks and evade detection on some domains → gaming is real; practitioners' consensus is that AI engines will counter (and Google/OpenAI have) and detection research is active. [EMPIRICAL]



## amazon — Disagreement
## Disagreement
1. **Negate vs lower bid on junk search terms.** Zahradnik (2020 QA podcast): some operators never negative, they lower bids; Zahradnik's agency stance favors disciplined negatives (negative products on auto was a big change); community r/AmazonFBA warns negating *retargeting* audiences kills the only lever that converts. Condition: term volume and whether the term is a category-relevant browse term vs exact junk.
2. **Auto-bidding trust.** Amazon's automated bidding (up-and-down + dynamic) drained spend in community reports ("127% ACoS on Amazon's automated bidding rules — worst placements", r/FulfillmentByAmazon 2026) vs agency claims that dynamic up-and-down scales proven campaigns. Condition: campaign maturity and margin headroom; community evidence says default automation on immature campaigns is a trap.
3. **SP/SB/SD split strictness.** Keywords.am's stage matrix (80/15/5 → 50/25/15/10) vs older "SP-only until 30–60 days" minimalism vs "SB for brand defense early" (Zagare's customer-buying-cycle/brand-halo budgeting). Condition: brand recognition and competitor behavior; when competitors bid your brand terms, SB defense is urgent regardless of stage (Keywords.am; Zagare).
4. **ACoS targets by category.** Benchmarks vary wildly by source (supplements 20–35% vs electronics 15–22% — Keywords.am; ainfluencer table ranges 10–40% ACoS / 5–30% TACoS by category). Condition: category + margin; everyone agrees the only true anchor is your own break-even, benchmarks are sanity checks. T3 for specific numbers.
5. **When DSP becomes viable** — Darkroom's $50k/month sponsored threshold vs Pathfinder's DSP-first clients at smaller scale (Viter Energy case) vs "DSP only after organic share stabilizes" (seller-community consensus). Condition: whether you have the measurement (AMC) and creative to make DSP learn; threshold is a heuristic, not physics.



## analytics — Disagreement
## Disagreement
- **"North Star metric" terminology** (Biddle explicitly avoids the phrase — "rarely that simple," exec teams prioritize engagement 2nd or 3rd so the NSM creates confusion) vs Cutler's North Star Workshops (embrace NSM but keep it "a bit out of reach" and pair with inputs). Both agree on the mechanism; they disagree on naming/centrality (OPINION, T1).
- **Actionability test**: Cutler warns teams over-apply "actionability" — a metric can be meaningful but not directly actionable, or exploratory; forcing every metric to be actionable produces "safe" vanity metrics that convey good news (T1). Kaushik's rule (kill anything without a target) is stricter; condition: Kaushik = exec reporting, Cutler = product teams.
- **GA4 vs alternatives**: Mercer pragmatic on GA4's limitations (data-driven attribution default, sampling, 14-month retention); Kiss adds "measure what matters, not what's easy." No real disagreement — both say tool is secondary to question (T2/T3).



## audience-intel — Disagreement
## Disagreement

1. **AI vs manual coding of unstructured data.** Vendor camp (Pelin, Koji, Enterpret): AI taxonomy at scale beats manual. Kromatic: AI drafts taxonomy but human must hand-read 50–100 in parallel — "relying on the model alone bakes in its training biases." Condition: AI for clustering/sentiment at scale, human read for taxonomy design and final theme confirmation.
2. **Intent data value.** Vendors (Bombora, 6sense, Intentsify): intent is the earliest in-market signal, worth big budget ($50–100K/yr for 6sense). Practitioners (Demandbase's own framing): intent is "evidence to investigate, not proof of purchase"; Amplemarket's comparison rates ZoomInfo intent 12/30. Condition: intent works only layered on fit (HG Insights: "intent with fit produces a ranked list worth working"); treat all vendor benchmarks as T3.
3. **How many interviews/themes count as signal.** Interview school: 3+ mentions = theme (existing research.md). Ticket school: 5–10% of sample (Koji). Review school: themes across multiple segments (Noisely). Condition: the more heterogeneous the population, the higher the threshold.
4. **G2 vs App Store vs Trustpilot weighting.** G2 reviewers write for other buyers and skew positive (verified-business bias); Trustpilot skews negative ("where people go when something goes wrong" — CheckThat). Condition: treat each channel as its own biased sample; never blend scores across channels without caveat (BigSentiment source-bias rule).
5. **Reddit: engagement vs research.** Marketing camp: engagement for brand (HubSpot mistakes list). Research camp: lurk-only, comments-before-posts, never promote (Reddinbox). Condition: research mode = no engagement; if you engage, follow subreddit rules and provide value first.



## creative-longtail — Disagreement
## Disagreement
1. **Creative blitzes vs controlled volume.** Some teams launch 70 ads/week to find angles fast (AdManage); hawky/Denney say budget-fragmented variation teaches nothing. Resolution: blitzes work only with large budget + production infra; the *number of distinct concepts* scales with budget, and within a concept, 3–5 variants is the ceiling (AdGenz).
2. **Scripts in UGC briefs.** InfluenceFlow/ATTN: avoid full scripts, preserve creator voice; some operators (Hustler Marketing) ship scripts. Resolution: script when compliance/demo precision is mandatory (claims rules, product demo steps); angle+beats when authenticity is the conversion driver — most UGC.
3. **UGC vs studio.** Consensus direction: UGC wins cold/prospecting, studio wins retargeting/brand search (hawky; ugc-advertising skill heuristic) — but category/offer changes the answer; test matched, per account.
4. **"Video always wins" is false.** Clean static with bold text beats polished video for some direct-response offers (AdGenz). Test format as a variable before optimizing within format.
5. **AI-generated UGC volume.** Koro-type vendors: 50+ AI shorts/day, 20+ variants/week/product, >30% thumbstop, 20%+ ROAS lift vs control (T3 vendor benchmarks, self-serving). Agency consensus (Moburst, Lauren Labeled): human creator fit + simplicity outperform volume of synthetic content. Treat AI-volume numbers as directional, unverified.



## cro — Disagreement
## Disagreement (with conditions)
1. **Bayesian vs frequentist statistics** — Goodson/VWO: probability-of-being-best + expected loss + optional stopping is valid and faster ("testing for truth vs maximizing revenue"); Georgiev/Kohavi (frequentist school): unplanned peeking invalidates inference; sequential requires pre-specified spending functions; Microsoft's paper proves Bayesian optional stopping valid only under proper stopping rules. CONDITION: Bayesian monitoring is a legitimate tool for *decisions with a stated threshold of caring*; fixed-horizon frequentist (or pre-planned sequential) when the analysis must be auditable.
2. **Emotional/customer-first CRO vs data-first CRO** — Wolf: research the customer's emotional drivers before looking at data; the data school (Laja, Kohavi, Aagaard): hypotheses must come from observed behavior/analytics. CONDITION: Wolf's approach is strongest for messaging/positioning-level problems (where analytics shows a leak but not why); the data approach is strongest for funnel mechanics with traffic. Both agree testing validates; they disagree on what generates hypotheses.
3. **Element-level testing vs strategy-level testing** — Aagaard (single-factor, clean attribution) vs Wolf (test whole strategies — "results of single-element tests are hard to analyze, understand and scale") vs Martijn Scheijbeler (big-change tests then decompose). CONDITION: element testing needs traffic; strategy testing when effect sizes must be big enough to detect (piperocket: "test big swings or don't test"). Also MECLABS: prefer factorial/multi-factor when traffic allows.
4. **When to redesign vs test** — Blanks/MacDonald: some pages need rebuilding around customer truth (CRO as "becoming the company"); Sullivan/Kohavi school: iterate with tests. CONDITION: redesign when the page is fundamentally misaligned (message mismatch, broken value prop — Saxo case), test when the page is sound and the question is incremental. MacDonald's rule: test when ≥1K visits/week + reversible + high stakes; otherwise rapid-test or ship.
5. **Significance thresholds** — Georgiev: 95% is not sacred; choose threshold by risk/reward. Kohavi/industry: 95% default, higher for big bets. Goodson: 95% PBB + loss threshold. CONDITION: lower thresholds justified when tests are cheap and opportunity cost high; keep strict thresholds for irreversible or high-stakes changes.



## dtc — Disagreement
## Disagreement
- **Paid-first vs organic-first**: Sharma is explicit (first 1,000 customers organic; milestones before scaling paid); Firestone is a paid-funnel maximalist (his whole method is profitable Facebook funnels) but both converge on: paid must be profitable per unit at the margin, not "growth at any cost." Condition: Sharma = brand-building DTC; Firestone = offer-led ecom where ad creative IS the product (T1/T2).
- **ROAS vs MER**: Firestone/Youderian push MER as the headline; direct-response advertisers still live on ROAS for campaign tuning. Consensus resolution: MER for allocation decisions, ROAS for creative/audience iteration (T2).
- **Amazon vs DTC**: Youderian data — DTC-primary grows 65% faster (30.2% vs 18.3%), higher GM (52.7% vs 41.9%), 91% of DTC operators love it vs 17% for Amazon. Contrarian to the "just sell on Amazon" advice; condition: brand control + margin vs marketplace reach (EMPIRICAL, T1).



## email — Disagreement
## Disagreement
1. **Frequency.** Geisler: "email more often than you think you should" (relevance is the issue, not volume). Atkins: "more isn't always better — there are consequences to sending too much or to the wrong people." *Resolution:* frequency is safe when engagement is high and list is permissioned; Geisler's context is onboarding (high-intent), Atkins' is reputation risk at scale.
2. **Open rates post-MPP.** Schwedelson still optimizes opens (subject/send-time; +15–28% lifts) vs White's "opens are obscured — optimize clicks/engagement." *Resolution:* opens remain usable as relative/directional signal for programs with high Apple-Mail mix... actually the split is: B2B/promotional mixes (Gmail/Outlook) retain signal; consumer/Apple-heavy lists lose it. Both agree engagement is the goal.
3. **Creative vs strategy emphasis.** Pay/White: strategy (journey, lifecycle, deliverability) >> creative tweaks. Schwedelson: tactical mechanics (subject lines, timing) are the highest-leverage cheap wins. *Resolution:* strategy is the ceiling; mechanics are the floor — do both in that order.
4. **Newsletter philosophy.** Oshinsky: launch fast, reader-owned, monetization one-trick-per-year, hyperscale-or-hyperniche. Schwedelson (implicitly): data-optimized sends. No direct conflict, but different decision grammars: editorial judgment vs dataset benchmarks.
5. **Inbox-placement tooling reliability.** Atkins: seed-test tools increasingly unreliable (saw 100% spam reports vs 30% real opens); personalization of placement per user. Iverson/White still use placement monitoring as a core practice. *Resolution:* use seed tools for regression detection, not absolute truth; trust real engagement metrics.



## feeds — Disagreement
## Disagreement
1. **How aggressively to clear warnings vs errors** — AdTribes: work top-down, errors first; Elite Brands: 80% of issues are warnings you can safely deprioritize if they're on non-core SKUs. Condition: account health headroom; if the account is near suspension thresholds, warnings matter more.
2. **Feed rules vs source-of-truth purity** — existing skill warns rules accumulate and obscure the source of truth; tool vendors (Feedonomics/DataFeedWatch via MBA Digital) sell rule-based transformation as the standard for large catalogs. Condition: catalog size and engineering capacity; rules are a scaling tool, but document owners and audit quarterly.
3. **Title optimization ceiling** — front-loading keywords is universal, but how much to optimize depends on channel: PMax title weighting vs Shopping CTR; hero-SKU hand-tuning vs rule-based generation for long-tail (existing skill). Condition: catalog size, hero SKU revenue share.
4. **When to use supplement feeds vs primary-feed fixes** — supplement feeds for overlays (promotions, labels, seasonal) are universal; disagreement is whether they mask root-cause problems (price/availability) — treat supplement feeds as temporary until primary is fixed (existing skill + AdTribes logic).
5. **PMax blame allocation** — when PMax underperforms, feed-first triage (existing skill) vs bid/asset optimization first (Google's own guidance emphasizes assets). Condition: diagnostics clean? If feed is clean, move to assets/audience; if dirty, feed first.



## gtm — Disagreement
## Disagreement
- **Demand creation vs capture allocation**: Walker argues most teams over-invest in capture (he says marketing should be ~"90% create, 10% capture" at scale for category leaders); Gerhardt agrees brand/community-first for founder-led GTM; Lemkin is more pragmatic — "do whatever gets revenue this quarter," capture is fine when cash matters. Condition: Walker's model suits funded category-creation plays; Lemkin's suits early revenue survival (OPINION, T2).
- **PLG vs sales-led vs partner-led GTM** (Rachitsky GTM motions data, Winters): no consensus on "best"; consensus is *pick one primary motion aligned to product complexity + ACV*. High-ACV/complex → sales-led; low-ACV/self-serve → PLG (EMPIRICAL, T2).
- **Virality expectations**: Chen (network effects are a *result* of PMF, not a strategy) vs naive loop-hunting. Balfour agrees: loops amplify what already works (T1/T2).



## market-intel — Disagreement
## Disagreement
1. **TAM size vs market structure as the investment filter** (a16z/Haber: "market structure is the new TAM" — a $2B fragmented niche beats a $600B TAM with one dominant system-of-record; vs. classic VC: "the bigger the number, the easier the pitch"). Condition: structure-first applies in AI/vertical software where incumbents own data/distribution; classic TAM-first still governs conventional categories (T2, OPINION).
2. **Top-down vs bottom-up as *primary***: a16z and most VCs prefer bottom-up; TechTarget/analyst firms treat analyst reports as the starting point; Sramana Mitra: bottom-up TAM is "the only version that matters." Disagreement is really about stage/audience: investor deck → bottom-up leads; board narrative → top-down leads (T2).
3. **SOM horizon**: some define SOM as "today's obtainable with current resources" (Carta), others as a 3-year planning target (bridginglocal). Use-case dependent: current-year capacity vs 3-year plan — state which (T3, definitions vary).
4. **Bass diffusion precision**: the model is accepted for curve *shape* and peak timing (R-Journal: good predictions of sales peak timing); practitioners disagree on whether absolute levels are reliable — consensus: m (market potential) must be sized separately, analog selection is the #1 error source (T1/T2).
5. **Scenario count**: McKinsey warns too many scenarios cause paralysis (use a few, named, vivid); FP&A practice wants a scenario catalog with trigger points. Resolve: 3-5 scenarios + trigger catalog is compatible — scenarios for strategy, triggers for operations (T2).
6. **Hype Cycle as predictive vs descriptive**: Gartner itself frames it as a maturity/risk lens, not a forecast; critics treat it as self-fulfilling/descriptive. Use for risk framing, not prediction (T2).



## messaging — Disagreement
## Disagreement
1. **Voice/personality vs research-first conversion** (Belgray/Handley/Cattoni: personality, story, and voice are the conversion engine; Wiebe/Price: research and match are the engine). Resolution: they operate at different layers — research supplies WHAT to say; voice supplies HOW. Both needed; the disagreement is about which is the bottleneck (voice in commoditized inboxes, message in unfamiliar categories).
2. **Simple/clear vs sophistication-calibrated** (Handley: simplicity is safety, T1; Schwartz: direct claims fail in sophisticated markets — "simple clear copy" advice is stage-1 logic applied to stage-3+ markets). This is the field's most important conditional: clarity of language ≠ directness of claim.
3. **Story vs direct pitch** (Chaperon: soap-opera open loops; Belgray: stories beat perfect copy; vs Hormozi/Halbert: lead with the offer and desire). Conditions: relationship/list context favors story; cold acquisition favors offer-first.
4. **A/B testing necessity** (Hopkins: test everything; Wiebe: you cannot A/B test everything — validate with five-second tests; Price: only test when traffic supports conclusive tests).
5. **Evergreen sequences vs launches** (Chaperon: evergreen assets compound; modern email consensus favors launches+broadcasts). Chaperon's conditions: evergreen product + story skill.



## outbound — Disagreement
## Disagreement
1. **Personalization depth: 1:1 human research vs offer-first at scale.** Allred: personalization at scale is an oxymoron; real 1:1 (trigger + context) drives 682% more replies / 1900% more pipeline (vendor data). Berman: either genuinely personalize OR lead offer-first; the fake middle ground dies; a clean offer-first email beats a fake-personal one 9/10. *Resolution condition:* research capacity per prospect (Allred works with trained sellers on mid-market/enterprise; Berman's method works at volume with thin per-prospect context).
2. **Open rate value post-MPP.** Efti says spend 80% of time on subject lines (30–40% opens = 60% never see body). Chad White (email side) says MPP rewrote this — optimize clicks. Outbound reply-based sending is less MPP-affected than marketing sends; both can be true by channel.
3. **Cadence length.** Ingram: 6–11 touches enough ("most teams have 11–15"); Efti: up to 8 cold; Berman: >2 follow-ups within a week trains spam filters; Taylor (Berman-cited): one email to TAM every 60 days. *Resolution:* cadence length trades against deliverability risk and message quality; short-and-relevant beats long-and-spammy in 2025+.
4. **Cold calling's role.** Ross/Tyre/Ingram: phone is essential. Berman (implicitly) and modern cold-email stack: email-first at scale. *Resolution:* market-specific — Tyre's SMB/partner context has reachable humans; enterprise-scale email-first needs no phone.
5. **What "stopped working":** Ross: email reply-to-call decayed ~7% → ~0.7% (2011→2019); Mailshake 2025: 69% of senders report YoY decline; Berman: copy bar unchanged, systems bar risen. Some claim "cold email is dying," others (Berman) that the channel is fine and systems are broken.



## paid-longtail — Disagreement
## Disagreement
1. **Auto-bidding trust**: Schwartz (native) warns max-conversion bidding burns budget pre-data; Lejnieks (Reddit Max) and CTC (Snap DPA) embrace platform automation when structure + volume exist. Resolution: automation is conditional on conversion volume + structure, not a feature choice (both sides' rules converge).
2. **ASA Basic vs Advanced**: Adapty says "Advanced exclusively"; AppRadar says Basic acceptable below $10k/mo and for default-page apps. Resolution: budget/capability dependent; both agree revenue attribution is mandatory.
3. **Bing vs Google universality**: Mackey's "Bing beats Google" is explicitly "not true for every client" — a base rate, not a guarantee; LSEO treats Bing as needing per-platform calibration. Resolution: test per account; the audience argument is structural, the performance argument is empirical.
4. **CTV measurement hierarchy**: Simulmedia says incremental lift > MMM; Prescient says MMM is the only complete method; WorkMagic says geo test + attribution. Resolution: geo lift = campaign-level truth; MMM = portfolio-level; use both at scale (aligns with Seufert dual-workflow in paid-strategy.md).
5. **Reddit Max vs manual**: Lejnieks runs both — automation for scaled winners, manual for spicy/specific creatives. Not either/or.



## paid-strategy — Disagreement
## Disagreement
1. **Is 60/40 universal?** Binet & Field themselves say NO (aggregate sweet spot now 62:38; sector range wide; IPA blog: "no universal best practice ratio"). Growth-stage practitioners (Francois, Stackmatix) say 60/40 is "roughly wrong" for early stage — closer to 30/70–20/80. Resolution: the ratio is context-dependent; the *direction* of adjustment is counterintuitive and evidence-based (high-consideration → more brand), while stage-based adjustments are practitioner heuristic.
2. **Double-duty vs two-speed executions** — Ritson (Zealot) argues separate brand and activation campaigns; the Double-Duty Squad argues one execution can do both (cheaper, attention is scarce). Ritson cites Binet/Field data favoring two-speed; Binet/Field themselves note double-duty can work. Condition: budget size and creative quality.
3. **Can brand ROI be measured?** Ritson: stop trying (ridiculous dollar estimates). Seufert: econometric measurement (MMM/incrementality) is exactly how you measure the un-attributable. Condition: data volume + modeling capability; both agree last-click can't do it.
4. **Reach vs efficiency under small budgets** — Sharp: even with limited budgets, don't think small/low-reach (not a recipe for growth or maintenance). Lean-team practitioners (Spike): concentrate spend above minimum viable thresholds, possibly 90/10 on one channel — which for a tiny budget means almost no brand reach. Condition: budget size; below a threshold the brand job shifts to cheap brand assets (founder narrative, content, distinctiveness) rather than paid reach (Stackmatix; Walker).
5. **B2B specifics** — Binet/Field data: B2B optimum ≈ 46% brand / 54% activation. Walker/Refine Labs: Brand 20–30% / Demand 50–60% / Expand 10–20% as a working B2B model. Condition: sales-cycle length, whether the sales team covers the activation job, and whether "brand" includes founder-led organic content (which Walker counts as brand at low cost).



## partnerships — Disagreement
## Disagreement
1. **Commission design**: flat-rate simplicity vs tiered incentives. Prussakov: motivation isn't only money (intrinsic motivation matters, top affiliates want tools/relationships); practitioners split on tiering — condition: tier for mature programs with volume data, flat for new programs.
2. **Fraud posture**: Prussakov: assuming all affiliates are fraudulent is deadly (paranoia kills recruitment); ops reality: fraud policies + tracking hygiene needed. Both are right at different stages — screen on onboarding, don't presume guilt.
3. **Influencer scale**: mega-creator reach vs micro/nano engagement. Gagliese's agency runs both; decision rule is cost-per-outcome and audience fit, not follower count.
4. **Referral reward timing**: dual-sided immediate vs delayed (e.g., reward after referee activates). Viral Loops practice: reward on activation (not signup) to prevent gaming; some programs reward instantly for share-rate optimization. Condition: activation-gated for SaaS, instant for impulse DTC.



## positioning — Disagreement
## Disagreement
1. **Narrative-first vs evidence-first**: Raskin leads with the big change + Promised Land (change-driven urgency); Dunford/Kellogg lead with competitive reality and market frames. Raskin's method presumes a shift to name; Dunford's works in stable markets. (Conditions: shifting market → Raskin; stable → Dunford.)
2. **Category design: designed vs emerged** (Lochhead: you can design and own a category, capture 76%; Kellogg 2026-08-13: categories emerge from a "rugby scrum" and "category design is mostly bunk"). Middle ground: Moore's lifecycle (define→develop→dominate) treats it as influence over an emergent process.
3. **Product-led vs sales-led positioning** (Bush: activation-led, in-product; vs the narrative school: pitch-led). Conditions: self-serve PLG product → Bush; high-ACV enterprise → narrative/market-frame school.
4. **Positioning before PMF** (Pierri: yes, position without PMF; Shah: fit first — most "positioning problems" are fit problems).
5. **Feature lists vs story** (Pierri/Raskin: narrative not feature lists; Moore adds: make comparison easy for pragmatists — features-as-evidence have a role at the whole-product stage).



## pr-launches — Disagreement
## Disagreement
1. **Press release: dead vs alive.** Classic PR still ships releases; Zitron/Meerman Scott treat the release as a low-value artifact unless it IS the newsjacked second paragraph. Condition: releases work for regulatory/financial news and as owned records; they don't generate coverage by themselves.
2. **Timing: newsjacking vs planned campaigns.** Meerman Scott: abandon long-lead campaigns; Dietrich: PESO still needs a calendar — the synthesis: keep the system, leave reaction slots (newsjacking lanes) inside it.
3. **Volume vs targeting in pitching.** Spray-and-pray (hundreds of reporters) still common; Zitron: it's the top reason pitches fail. Conditions: some long-tail outlets accept volume; tier-1 requires individualization.
4. **PH: launch-day tactics vs long-term community.** Some PH guides optimize the 24h (voting mechanics); KWD/Chris Messina emphasize community + product quality; voting-rigging is watched for and punished by the community.



## pricing — Disagreement
## Disagreement
- **Seats vs usage vs hybrid**: Campbell historically favored value metrics/usage for expansion; Poyar's 2025-26 data shows pure usage creates CFO forecasting pain and pure seats leaves expansion money on the table → hybrid (seat base + usage expansion) is the emerging consensus for AI/SaaS (EMPIRICAL, T1). Balcauski: operations-first — pick the model you can actually bill, forecast and support (HEURISTIC, T3).
- **How often to change price**: Campbell says quarterly review; Poyar cautions churn-inducing instability (3.6 pricing changes/company in 2025 = loss of confidence). Condition: review quarterly, *ship* changes only when value is demonstrably re-communicated (T1/T2).
- **Grandfathering/legacy pricing**: no consensus; Poyar notes most 2025 changes included grandfathering or usage caps; treat as negotiation, not pricing (T2).



## research — Disagreement
## Disagreement

1. **Story-first vs outcome-first JTBD.** Moesta/Klement: reconstruct the story/timeline; forces emerge from events; never ask about metrics. Ulwick: needs are undefinable; define outcomes with strict syntax; customers can't articulate needs. Resolution condition: story-first when the purchase is emotional/rare (B2C, big-ticket); outcome-first when the job is operational and measurable (B2B tools, engineering workflows). Klement explicitly rejects Ulwick-style taxonomies; Ulwick dismisses vague "needs first" approaches.
2. **What customers can tell you.** Fitzpatrick/Alvarez/Moesta: customers CAN give you truth (about their past). Ulwick: customers cannot articulate needs at all (must be shown outcome statements). Condition: customers are reliable about facts of their past behavior; unreliable about abstract wants/needs. Both are right about different question types.
3. **Interview count.** JTBD school: 5–8 interviews suffice for a job (pattern repetition). Academic saturation review: 9–17; Griffin & Hauser: 20–30 for 90–95% of needs. Win/loss: 20+/segment. Condition: the narrower the job and more homogeneous the population, the fewer interviews; the more you need to *size* or *prioritize*, the more (or switch to quant).
4. **NPS as the one number.** Reichheld: NPS drives growth, use as a system. MIT Sloan/Keiningham et al.: no empirical superiority over other satisfaction metrics; untestable as a system. Condition: NPS is directionally fine as a benchmark + loop-trigger; never use it as the sole decision metric or a compensation base.
5. **Persona structure.** Revella: role-agnostic 5-rings personas built from buyer interviews. ziellab: one persona per buying-committee role (champion, economic buyer, technical evaluator, end user, blocker), half a page each. Condition: Revella for message/marketing strategy; role-based for sales enablement and outbound. Both reject demographic personas.
6. **Who runs discovery.** Blank/Torres: founders/teams must do it themselves. Enterprise practice: dedicated research teams. Condition: team-led for speed and empathy when access is easy; specialist-led for scale, rigor, and win/loss neutrality (Clozd: people who sold the deal must not run the win/loss interviews).



## retail-media — Disagreement
## Disagreement
1. **DSP entry threshold**: Darkroom says <$50k/month sponsored spend with inconsistent profitability = DSP premature; agencies that sell DSP (Pathfinder, Sequence) show DSP case studies at smaller scales (Viter Energy). Condition: whether AMC measurement + creative exist; treat threshold as heuristic. T3 for the number.
2. **Instacart maturity**: Perpetua (2021) called Instacart "less expensive than mature marketplaces" with room to grow; by 2024-2026 retail media consolidation and higher CPCs are widely reported (UNVERIFIED specific numbers; Adverity notes measurement difficulty). Condition: category and whether you're vendor (retailer-owned data) vs marketplace seller.
3. **On-site cannibalization severity**: some agencies treat on-site sponsored as purely incremental (search placement wins vs competitors); SellerStack/paid-strategy synthesis warn branded-term on-site ads largely displace organic (test the difference; existing skill). Condition: share of voice you already own organically.
4. **Closed-loop vs MMM attribution of in-store halo**: Walmart Connect sells omnichannel store+online attribution; most brands can't verify store halo claims without retailer data access (Feedvisor vendor survey self-reports 7x ROAS — tier 3, treat as directional). Condition: data access through retailer partnership.
5. **Segment trust**: retailer-defined audiences (lapsed buyers, category buyers) are refreshed on retailer schedules and definitions are opaque — ask how segments are built before trusting them (existing skill; Eva Commerce advises multivariate testing with Walmart data). Condition: retailer relationship depth.



## seo — Disagreement
## Disagreement
1. **Topical authority vs audience-first brevity (Gubur vs Law)** — Gubur: exhaustive entity/topical-graph coverage (deep, structured, encyclopedic). Law: short, opinionated, audience-problem content; volume ignored. *Condition:* Gubur's method wins in competitive informational niches where depth = differentiation and you can't outlink incumbents; Law's wins in B2B/SaaS where buyers don't search generic topics and distribution happens off-SERP. Both agree intent discipline matters (Gubur's "canonical intent" ≈ Law's "answer the question").
2. **Link building as priority (Moogan/Milligan/Dean) vs product-led SEO (E. Schwartz)** — Schwartz: build the searchable asset; links follow. Link school: assets without link acquisition stall. *Condition:* product-led wins when the product itself can serve bottom-funnel queries (SaaS, marketplaces, e-commerce); link-first wins for content/media businesses with no product surface.
3. **Crawl budget importance (Mueller: mostly a non-issue; Stox: ignore noise) vs audit-industry emphasis** — mainstream tooling over-sells crawl budget; the practitioner consensus is to manage inventory (params, orphans, soft 404s) and stop there.
4. **Content depth/word count (Gubur: coverage) vs brevity (Law) vs intent-based (Dean 2.0, Eli Schwartz: SERP decides)** — the resolution: the SERP/query decides the right format; neither depth nor brevity is universally right.
5. **Testing culture (Critchlow: test everything, best practices are priors) vs long-game remediation (Gabe: core-update recovery can't be tested short-term)** — both true at different levels: page-level changes are testable; site-level quality re-rating is not.
6. **Metrics: rankings/traffic (classic) vs demos/revenue (Dunning, Law) vs AI citations (Indig)** — stage-dependent: content-stage companies track rankings, growth-stage track demos, AI-sensitive verticals track citations.



## social — Disagreement
## Disagreement
1. **Links in posts**: old consensus "never post links" vs vDB 2026 data: 3+ outbound links perform 20% better than 1 (clustering signals depth). Conditions: link-rich posts work when they're genuinely resource-dense, not link spam. (T2, single-researcher EMPIRICAL)
2. **Hashtags**: common advice "use 3-5" vs vDB 2026: no-hashtag posts outperform by 5-10%. Platform moves; trust data over habit.
3. **Post length**: "punchy two-liners" vs vDB: text under 600 chars underperforms sharply. But Cole/Drew preach brevity (50% rule). Resolution: brevity = sentence-level economy; 600+ chars = enough substance to read. They're about different units.
4. **LinkedIn reach model**: "network proximity era over" (vDB: Interest Graph, 2026) — old playbooks (engage pods, connection farming) are now actively penalized; engagement pods detected at 97% accuracy.
5. **X follower counts**: survivorship-biased; treat follower-count claims LOW CONFIDENCE, prefer systems evidence (Drew's teardowns, Cole's volume math).


