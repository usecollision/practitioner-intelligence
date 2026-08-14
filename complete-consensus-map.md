# COMPLETE CONSENSUS MAP — where the field agrees

Assembled 2026-08-15 from 24 discipline syntheses. Each section names the practitioners and claim confidence.

## aeo — Consensus
## Consensus
- **Being in the retrieval pool is the prerequisite for being cited.** ChatGPT cites ~88% of its URLs from the general "search" retrieval channel (Ahrefs, 1.4M prompts, Apr 2026); Reddit's dedicated feed is pulled at volume but cited only 1.93% of the time. Practical consequence: classic SEO ranking is the entry ticket to AI citations. [Law/Linehan/Guan — EMPIRICAL]
- **Quotes, statistics, and external citations in content are the strongest measured content levers.** Stanford GEO: +30-40% position-adjusted visibility from Cite Sources/Quotation/Statistics addition; up to 37% on Perplexity. [Aggarwal et al. — EMPIRICAL, controlled]
- **Third-party mentions dominate brand citations.** ~85% of AI brand citations come from third-party domains (Crestodina); Perplexity's most-cited domains are YouTube (31-32%), Reddit (13.9%), Wikipedia (7.2%) (Ahrefs, Jun 2026); unlinked brand mentions matter more for LLMs than for Google (Law). [EMPIRICAL]
- **Answer-first structure works**: question-as-heading, direct answer immediately after, self-contained chunks; 93% of 150 AI-search sources agree (Crestodina); Aleyda Solis: chunked topic clusters; HubSpot AEO docs echo. [HEURISTIC + consensus]
- **Measure per engine, never as one blended score.** Only 2.37% of cited URLs appear in all three engines; 91% in exactly one (Indig, 3.7M citations, 20k prompts). Presence/Portability/Concentration are three numbers. [Indig — EMPIRICAL]
- **Treat each AI answer as a sample, not a ranking**; aggregate at topic level (Solis). [HEURISTIC]
- **AI answers reduce clicks.** AIO presence correlates with −34.5% position-1 CTR (Law/Guan, 300k keywords); Seer Interactive: organic CTR fell from 1.41% → 0.64% on AIO queries (Jan 2025 data). Google doesn't expose AIO click data in Search Console. [EMPIRICAL]
- **Technical crawlability is table stakes**: server-side rendering, AI bot access (GPTBot, PerplexityBot, ClaudeBot, Google-Extended), llms.txt optional. [Solis, Law, Crestodina — HEURISTIC]



## amazon — Consensus
## Consensus
- **Ads amplify a listing; they cannot fix a weak one.** Listing conversion (reviews at category parity, price, images, Buy Box) is the gate before scaling spend (Zagare; Pathfinder; every agency). HEURISTIC, T1.
- **Allocation beats volume.** Where SP/SB/SD budget goes matters more than how much you spend; a $3k/month correctly split outperforms $10k spread evenly (Keywords.am). 60/30/10 (SP/SB/SD) is a *starting point*, not a rule; lifecycle stage changes it: launch ≈ 80/15/5, growth ≈ 60/25/15, mature ≈ 50/25/15 (+10 DSP), brand-under-attack ≈ 40/35/25. HEURISTIC (agency consensus, Keywords.am 2026), T2.
- **ACoS is a campaign metric; TACoS is the business metric.** ACoS = ad spend / ad-attributed sales (optimize bids); TACoS = total ad spend / total sales incl. organic (steer budget and strategy). Never steer the business on ACoS alone (pcostudio; ainfluencer; Keywords.am). FRAMEWORK, T1.
- **Break-even ACoS = contribution margin %** — compute per ASIN, set stage targets from it: launch at/above break-even (buy rank), growth below break-even minus buffer, harvest well below (Zagare-consistent; EcomCalcTools; Pathfinder 9% ACoS case). HEURISTIC, T2.
- **Bidding: placement modifiers apply first, dynamic bidding compounds second** — a 900% ToS modifier + up-and-down can turn a $1 bid into $20; most sellers misjudge effective CPC (AMALYZE cascade). Up-and-down only on proven exact terms with 30+ days data; fixed for branded campaigns; down-only as the conservative default (SalesDuo; AMALYZE). EMPIRICAL/HEURISTIC, T2.
- **Amazon attribution is deterministic-but-inflated**: ad-attributed sales credit every purchase that touched an ad; NTB (new-to-brand) measures genuinely new customers; halo = organic-rank lift and cross-SKU sales never shown in the console. "When a branded campaign's ROAS looks great, distrust it" — bottom-funnel branded looks heroic while upper-funnel that grows the business gets starved (SellerStack). EMPIRICAL (mechanism), T1/T2.
- **DSP is an upper-funnel/retargeting layer, not a second PPC tool** — it makes search more efficient via a flywheel (DSP awareness → search capture → search data improves DSP audiences); premature below ~$50k/month sponsored spend with inconsistent profitability (Darkroom). HEURISTIC, T2.
- **Amazon enforcement is a business risk, not just a compliance footnote**: review-velocity flags can suspend legitimate launches; packaging inserts (even manufacturer-added) trigger review-manipulation suspensions; appeals win on documented proportionality (SellerSprite 2026 cases; Cabilly; McCabe's "think like Amazon"). EMPIRICAL, T2.
- **Marketplace economics have compressed**: 2025 saw the fewest new Amazon sellers in a decade (165k, −44%); Amazon is now ~60% services/40% retail; ads evolved "from optional to unavoidable"; new seller entry is a capital game (Marketplace Pulse 2025 Year in Review). EMPIRICAL, T1.



## analytics — Consensus
## Consensus
- **Dashboards are for decisions, not data display** (Kaushik, Kiss, Mercer): "slay the data-puking dragon." Every metric on a dashboard must have a pre-assigned target and a decision attached; else it's noise (FRAMEWORK, T1).
- **KPI hierarchy, not flat metric soup** (Kaushik): ~6 KPIs for the CEO, ~6 for the CMO, each with target + benchmark; micro-diagnostics belong in analysis views, not dashboards (HEURISTIC, T1).
- **Focus on outliers** (Kaushik): dashboards should surface KPIs 3 standard deviations from the mean — the abnormal needs attention, the normal doesn't (HEURISTIC, T1).
- **Metrics need context, intent, and actionability** (Cutler's Vanity Metric Test): a metric is vanity if it (1) lacks context ("compared to", "as input into", "balanced by"), (2) has unclear intent (why is this the measure of success?), (3) doesn't guide action/learning (FRAMEWORK, T1).
- **North Star needs inputs/proxy metrics, not just a single number** (Biddle, Cutler): the NSM is a lagging multi-year outcome; teams need *proxy metrics* — leading indicators defined as "% of users who do at least X by Y time" (Biddle's Netflix example: % of new customers watching ≥15 min streaming in first month) (FRAMEWORK, T1).
- **Averages hide the distribution** (Biddle): prefer threshold/cohort metrics over averages; average engagement can rise while most users get worse (EMPIRICAL, T1).
- **Measurement setup is a discipline** (Seiden): GA4 setup best practice = config via GTM, enhanced measurement, register custom dimensions/metrics, set data retention (14mo free/50mo 360), choose attribution model explicitly (TACTIC, T1).



## competitive — Consensus
## Consensus
- **CI's goal is winning deals, not producing research** (Kellogg): competitive analysts who define their job as product comparison ("Harvey Balls") fail; the function must convert research into sales plays (FRAMEWORK, T1).
- **Competition is defined by the buyer's alternatives, not your feature matrix** (Dunford): competitive alternatives = "what would the customer do if your offering didn't exist?" — status quo/do-nothing, manual process, spreadsheet, inaction. Enterprise loses ~25% of deals to "no decision" — position against the status quo too (FRAMEWORK, T1).
- **Phantom competitors dilute positioning** (Dunford): don't position against companies that could compete but never appear in your deals; you weaken positioning and waste effort (T1).
- **Scoring must be documented** (Kellogg): if you use comparison charts, footnote the scoring basis or they're subjective wallpaper (T1).
- **Win rate is the CI metric** (Kellogg): head-to-head win rate vs chosen competitors — "competitive's job is not to produce reports; it's to increase win rate" (HEURISTIC, T1).



## creative-longtail — Consensus
## Consensus
- **Creative is the highest-leverage paid variable; targeting is automated.** Industry analyses attribute 70–80% of paid-social performance to creative (hawky, ORCA, Wieldr — T3 vendor consensus, directionally consistent with Denney T2, Shackelford T2, Hormozi T2). Shackelford: "creative is the new targeting." Denney: test creatives, not audiences. Hormozi: ads are won on creative, not media buying.
- **Angles precede assets.** An angle is the strategic claim (pain/desire × proof point); a hook is the 1–3s opener; ONE angle generates 20+ hook variations. Angle selection — not asset production — is the decision with most upside (hawky, T2). Build an angle matrix: top pains/desires × proof points; score each angle on evidence, saturation (check Meta Ad Library/Google Transparency for competitor-owned angles), and proof. (FRAMEWORK)
- **Failed ads die at the hook, not the offer.** Hormozi Hook-Meat-CTA: hook names the buyer's pain in 3–4 words; "write fifty hooks before you write one ad"; the hook is the shortest part of the ad and the only part that decides whether the rest is seen (Hormozi via Gavel, T2). The 1.5–3s window: 50–70% loss in first 1–2s; layered hooks (visual+audio+text) ~3x; thumb-stop 30–50% = good on Meta (ORCA, T3); strongest formulas stack 2+ triggers and mirror the spoken hook with on-screen caption (vexub H-A-P, T3).
- **Creative supply rate is budget-scaled, and volume means DISTINCT concepts, not variants.** Denney at $5k–30k/mo: 1–3 new creatives/week, cap ~10 live. 2026 consensus at meaningful spend: 2–4 genuinely different concepts/week (hawky). Discovery batches: 3–5 variants per concept (AdGenz). Top accounts rotate new variants every 7–10 days ahead of fatigue (AdManage). Meta's algorithm clusters near-identical creatives — "30 variations of the same concept is one test" (hawky). Hormozi: 80% of resources reskin winners; hook-splicing = isolate first 3s of top 5–10% of ads, graft onto 100+ ads → 10–50x creative per proven hook (T2).
- **Test discipline:** one variable per test, equal budget/duration/audience, minimum 1–2x target CPA or 3–7 days before judging, kill/iterate/scale criteria defined BEFORE launch (hawky, AdGenz, Pixis — T2/T3 consensus; joins Denney 10-iterations-on-winner rule).
- **UGC: brief quality = output quality.** Moburst #1 practice: "invest in the brief, not just the creator." ATTN: skincare brand +340% after brief restructure (2,000+ creator relationships analyzed); InfluenceFlow: detailed briefs = 73% faster completions. Strong brief = 1–2 pages, ~400–1,200 words, <5 min read: audience, objective, product facts + honest limitations, pain points, 2–3 angles with example hooks, reference videos (a 5s video ref > 200 words of description), red flags/content to avoid, deliverables, revision limits, compensation + usage rights (ATTN, Moburst, InfluenceFlow, SideShift). Brief the angle and emotional beat, not a script — scripted UGC loses the native quality (Pixis; InfluenceFlow: give 3–5 example phrases, not full scripts).



## dtc — Consensus
## Consensus
- **Unit economics drive everything** (all four): gross margin, AOV, contribution margin, retention/repeat rate, MER — paid is a lever on a healthy business model, not the business itself (FRAMEWORK, T1/T2).
- **MER (marketing efficiency ratio = revenue / total ad spend) is the macro health metric; ROAS is the micro/campaign metric** (Firestone's "golden ratio" / dollar-in-dollar-out; Shopify's MER primer): MER is the blended truth across channels and time; ROAS alone misleads when spend shifts between platforms (FRAMEWORK, T1/T2).
- **The P&L anatomy beats the ad account** (Youderian 2026 eCommerceFuel data, 300+ stores, $3.5B): brands "great at paid" don't have the best ROAS — average 2.5x vs 4.0x survey-wide — they have fat gross margins (63.7%) and lean overhead (16.6%). The edge lives in COGS/overhead, not the ad account (EMPIRICAL, T1).
- **Find PMF/messaging before scaling paid** (Sharma): "get the first thousand customers without paid methods"; use paid to amplify content/offers already proven organic. Milestones: $5k/day revenue before scaling paid aggressively (HEURISTIC, T1).
- **Organic-to-paid pipeline** (Sharma, Firestone): test content/creative organically first; low CPM = platform doesn't like the creative; CTR tells you if people like the message (TACTIC, T1).
- **Retention/repeat purchase is the DTC profit engine** (Firestone: email/back-end marketing, upsells; Sharma; Youderian: repeat rate in survey data) (EMPIRICAL, T2).



## email — Consensus
## Consensus
- **Lifecycle beats campaigns.** White (six subscriber-lifecycle stages), Geisler (onboarding = churn reduction; trial→paid then retention), Pay (journey-based automation) all converge: structure email around the subscriber's stage, not the calendar (FRAMEWORK — T1 convergence).
- **Deliverability is infrastructure, not optimization; recipient-first is the philosophy.** Atkins ("the email belongs to the subscriber," reputation from recipient behavior), Iverson (authentication = identity, not delivery), White (seven reputation factors) — consent, engagement, and complaint control decide long-term deliverability (FACT/EMPIRICAL).
- **Authentication baseline is now mandated:** SPF or DKIM for all senders; SPF+DKIM+DMARC, PTR, TLS, one-click unsubscribe, <0.3% Gmail spam rate for bulk (>5k/day) since Feb 2024 (FACT — Gmail docs; Iverson/Atkins confirm it formalized best practice).
- **Behavior-based sending beats time-based-only sending.** Geisler (branch on activation state — "don't serve dessert to someone still on the appetizer"), White (qualify active mailable audiences; clicks over opens post-MPP), Pay (optimize whole journey) (FRAMEWORK — T1 convergence).
- **Send-time and subject-line mechanics still move opens measurably.** Schwedelson: off-hour sends +~15% opens; time-commitment subject lines +28% opens / +19% preheader; type-specific timing (newsletters morning, offers midday) (EMPIRICAL — his aggregate data).
- **Human/personal voice wins.** Geisler (welcome email from a named founder with story; customer-language copy), Oshinsky (reader-owned channel, job-of-newsletter) (PRINCIPLE).



## feeds — Consensus
## Consensus
- **The feed is the ad.** Feed quality determines Shopping/PMax eligibility, matching, and CTR; weak feed data = weak PMax performance (existing shopping-feeds skill; MBA Digital; GetFeeder). FRAMEWORK, T1.
- **Diagnostics triage is top-down: account-level → feed-level → item-level**; within item-level: errors (disapproved, won't show) → warnings (shows but performance suffers) → notifications (informational). A "wall of issues" becomes a short prioritized list (AdTribes). HEURISTIC, T2.
- **80/20 prioritization**: ~80% of account issues are warnings/limited-performance flags on non-core products; the damage is the ~20% hard disapprovals on the products that make money. Prioritize by (severity × revenue impact) (Elite Brands). HEURISTIC, T2.
- **Account-suspension warnings are all-hands emergencies** — yellow/red bar at top of Merchant Center; address root cause immediately; it's the whole advertising operation at risk, not one product (Elite Brands). T1.
- **Fix at source, then re-fetch** — patching inside Merchant Center (or feed rules) leaves the store broken; fixes evaporate on next fetch (existing skill; AdTribes: "fix at source"). T1.
- **Data-quality issues are the fastest wins** — missing attributes, formatting, simple policy fixes resolve in hours and get fast re-approval (Shoparize). T2.
- **Price/availability mismatch between feed and landing page is the most common account-level health issue** — silent damage, account-level warnings (existing skill; Shopify community reports). T2.
- **GTIN/MPN mismatches and category-taxonomy errors are top disapproval causes** — fix at catalog level; generic/mismatched google_product_category mapping spikes disapprovals (existing skill; Shopify community thread). T2.
- **Promotional language belongs in the promotions feed, not titles/descriptions** (GetFeeder). T1 (policy).
- **Technical feed errors are mechanical**: malformed XML, missing units on shipping_weight (must be "1.5 kg"/"3 lb"), >4GB compressed feed limit (GetFeeder). FACT, T1.



## gtm — Consensus
## Consensus
- **Stage determines strategy** (Balfour, Winters, Lemkin, Rachitsky): there is no universal growth playbook. Pre-PMF your job is learning, not scaling; post-PMF it's compounding loops. Balfour: the model must match the stage — you cannot bolt a growth team onto a product without PMF (HEURISTIC, T2).
- **Loops beat funnels when there is an inherent sharing/network mechanic** (Balfour 2018 "Growth Loops are the New Funnels", Chen *Cold Start Problem*): every loop is Trigger → Action → Output → Input back to Trigger; the output of one cycle feeds the next. If no natural loop mechanic exists, forcing virality fails — use paid/content loops instead (FRAMEWORK, T1).
- **PMF must be measured, not felt**: Sean Ellis 40% "very disappointed" survey on *recent active users* (last 2 weeks), min ~30 responses, confident at 100+; follow-ups on main benefit + who benefits most + why (FRAMEWORK/EMPIRICAL, T1). Asymmetric: <40% is a reliable warning; ≥40% is encouraging, not conclusive (T2).
- **First customers come from non-scalable channels** (Rachitsky, Lemkin): network, strategic cold outbound, investor intros, communities (add value first), content. "None of these scale. That's why they work" (HEURISTIC, T1).
- **Demand creation ≠ demand capture** (Walker, Gerhardt): if attribution/KPIs only reward capture (search, retargeting, intent data), marketing optimizes to the 3-5% of market in-market and hits diminishing returns. Win higher in the funnel (FRAMEWORK/OPINION, T1 — Walker's core thesis).
- **Retention is the growth lever that compounds** (Ellis, Balfour, Winters, Chen): cohort retention curve shape determines whether spend scales. If retention is flat, paid growth = leaking bucket (EMPIRICAL, T2).



## messaging — Consensus
## Consensus
1. **Copy comes from research, not creativity** (Wiebe T1 — "research and discovery is everything"; Price T2 — analytics gatekeeping; Ogilvy T1 — "helpless without research"; Hopkins T1 — test-measure-refine; Halbert T1 — study what people DO buy). 5 independent practitioners across 100 years agree. The strongest consensus in the entire field.
2. **Use the customer's language verbatim** (Wiebe's "slightly revise" T1; Shah's PMF-language-for-copy on the positioning side; Belgray: human/specific/real T2).
3. **The offer/market precedes the copy** (Halbert T1 — starving crowd; Hormozi T2 — Market > Offer > Persuasion; Schwartz T1-canonical — desire cannot be created, only channeled). Copy amplifies existing demand; it does not manufacture it.
4. **Headlines/hooks are a volume game, chosen against criteria** (Ogilvy T1 — 20 headlines per ad; Cattoni T2 — 99 hook templates; Wiebe T1 — five-second test for clarity).
5. **Measurement discipline**: test cheaply, keep winners, kill losers (Hopkins T1 — TMR loop; Price T2 — baseline analytics before copy; Wiebe T1 — validation phase).
6. **Message must match the buyer's state** (Schwartz awareness levels T1-canonical; Wiebe message-match T1; Price funnel position T2).



## outbound — Consensus
## Consensus
- **Offer/targeting > copy, in that causal order.** Berman (offer-first, "the offer is the 80/20"), Allred (targeting hypothesis before 1:1), Ross (JTBD targeting + message experiments), and the Mailshake survey (personalization + targeting = clearest lever) converge. Rule: fix offer → fix targeting → fix copy → scale infrastructure (Berman).
- **Reply rate is the north metric; opens are directional only.** Mailshake 2025: 1–4% reply is the norm, only 16% of senders exceed 5%; Berman: opens-up-replies-flat means the offer is broken; Allred optimizes total replies + pipeline.
- **Deliverability discipline is mandatory infrastructure, not optimization:** consistent daily volume caps (Berman: 15–30/mailbox/day; never Monday-bursts), avoid >2 follow-ups within a week, warm domains, monitor daily. Gmail's Feb 2024 rules (SPF or DKIM all senders; SPF+DKIM+DMARC + <0.3% spam rate + one-click unsubscribe for >5k/day) made this regulatory, not optional.
- **Multichannel beats single-channel email:** Ingram (LI + email + phone + video cadences), Tyre (4 calls + intermittent email + video), Ross ("pick up the damn phone"). Email alone is the weakest channel.
- **Persistence with structure:** 5–8+ touches (Efti: 5–8 attempts cold, follow up forever when warm; Ingram: 6–11 touches over 3–4 weeks) — but relevance per touch is the constraint (Ingram's own counterpoint: fit > frequency).
- **Human, short, specific:** 50–60 word emails (Berman), "like a friend" (Berman/Efti), specific proof/deliverables beat category descriptions (Berman, Efti's "specific value proposition", Tyre's proof-over-interest).



## paid-strategy — Consensus
## Consensus
- **Brand and activation are complementary, not substitutes** — "brand sets up the sale, activation closes the sale" (Ritson); efficiency gains from activation require brand (Binet & Field); performance alone cannot create demand that does not already exist (Walker/Francois). Binet & Field, Sharp, Ritson, and Walker all independently identify **under-investment in brand as the dominant paid-media failure** (EMPIRICAL for Binet/Sharp; OPINION/EMPIRICAL for Walker).
- **Reach beats targeting for the brand job**: whole-market/category-buyer reach grows brands; loyalty-targeted or existing-customer campaigns underperform (Binet & Field: 3x large effects; Sharp: penetration is the growth lever; Ritson: don't target customers who'd buy anyway). EMPIRICAL (Binet, Sharp).
- **Platform attribution overstates performance**: last-click/self-attributed ROAS inflates channel contribution; macro-level metrics (MER/MMM/incrementality) are the truth layer (Seufert; AdMaxxer/AdSights topic evidence: overlap tax 1.4–1.8x; iROAS on brand search ~10–25% of reported). EMPIRICAL/OPINION (multiple independent sources).
- **Different metrics for different decisions**: short-term/activation measured with ROI; long-term/brand with brand effects (Binet & Field principle 10; Ritson: "stop measuring brand with dollar estimates"; Seufert: MMM macro + campaign micro on separate cadences). FRAMEWORK.
- **Holding a split for years beats quarterly rebalancing on ROI swings** (Ritson: hold ~10 years; Francois: review annually, not quarterly; Binet: long-term effects only visible over 3+ years). HEURISTIC/EMPIRICAL.
- **Creativity + consistency compound**: emotional, distinctive-asset-consistent creative outperforms rational benefit-led persuasion (Binet: emotional 2x; Sharp: DBAs + memory refresh). EMPIRICAL.



## partnerships — Consensus
## Consensus
- **Partners are independent marketers, not employees.** Prussakov: "you can manage a program, not affiliates" — treat affiliates as partners; control by incentives + communication, not threats. (FRAMEWORK, T1)
- **Referral economics are math you can model before launch.** K-factor = invites per user × conversion rate; consumer-internet benchmarks: 0.15-0.25 good, 0.4 great, 0.7 outstanding. (EMPIRICAL, T1 from Viral Loops)
- **The referral funnel has 5 measurable stages.** K-factor, participant conversion rate, participant share rate, invitation CTR, invitation conversion rate — diagnose which stage leaks before redesigning the reward. (FRAMEWORK, T1)
- **Influencer marketing must be measured against paid benchmarks.** Gagliese/Viral Nation: compare creator CPM/CPC/ROAS vs paid; run lift studies with exposed vs unexposed groups; treat reach/follower claims as low confidence. (FRAMEWORK, T2)
- **Loops beat campaigns only when the product has inherent virality** (Ellis/Balfour canon; master-map §34). If the product isn't share-worthy, referral programs become discounts. (FRAMEWORK, T2)



## positioning — Consensus
## Consensus
1. **Positioning is a choice against competitive alternatives, not a feature description** (Dunford T1, Pierri T2, Kellogg T1, Moore T1, Neumeier T1). 5+ independent practitioners converge.
2. **Evidence precedes positioning**: workshops must be fed by customer language, shortlists, win/loss data before anyone writes a word (Dunford T1, Hiten Shah T1, Bare Strategy T2, Ogilvy's process mirrors this on the copy side). A claim without proof ("case study, metric, customer quote") is aspiration, not positioning.
3. **The market frame of reference is a choice, and usually a different market than you started in** (Dunford T1 — IBM database→BI example; Moore T1 — beachhead selection; Kellogg T1 — position on the buyer's job). Consistent: 4 practitioners.
4. **Narrow beats broad**: beachhead (Moore), best-fit prospect (Dunford), onlyness (Neumeier), use-case narrowing (Pierri). "Positioning for everyone positions you for no one" (Bare Strategy T2).
5. **Positioning is a company-wide alignment artifact, not a marketing deliverable** (Dunford workshop T1, Raskin "everyone tells the story" T1, Lochhead mobilization T2).
6. **Message language comes from customers** (Hiten Shah PMF survey T1 — "use their words for copy"; Raskin harvest stakes language T1).
7. **Category creation is expensive and rare**: only works when you can fund the education (Lochhead's own preconditions T2; Kellogg's critique T1; master map consensus).



## pr-launches — Consensus
## Consensus
- **PR is an integrated system, not a press-release function.** PESO (Paid/Earned/Shared/Owned) — Dietrich's model (2014): owned content is the foundation, shared distributes, earned validates, paid amplifies what's already working; design the handoffs before the calendar. (FRAMEWORK, T1)
- **Speed is the new power.** Meerman Scott: newsjacking requires "now means now" — react in hours, provide credible second-paragraph content journalists can lift while researching a breaking story. (FRAMEWORK, T1)
- **Journalists want brevity and relevance.** Zitron: 450-word pitches get ignored; no funky formatting/bold/colors; no exclamation-spam; explain why THIS reporter cares. (HEURISTIC, T1)
- **Product Hunt is a 24-hour game with a community that rewards preparation and authenticity.** KWD: B2B launches Mon-Thu; community is empathetic, pile-ons rare; reach out to top hunters 2-3 weeks ahead; the window is the 24h after launch. (HEURISTIC, T2)
- **Earned media is becoming AI-citation currency.** Dietrich's 2026 framing: >95% of links AI engines surface come from earned, shared, and organic owned content — PR now feeds AI visibility. (EMPIRICAL as reported, T2)



## pricing — Consensus
## Consensus
- **Price off value, not cost** (all four): value metric must track what the customer gets (usage, outcomes, seats-as-gateway), not what you spend. Ramanujam: "design the product around the price" (FRAMEWORK, T1).
- **Package to sell — Good/Better/Best** (Poyar, Campbell, Ramanujam): 3 tiers at minimum; the middle tier anchors; no single flat plan (HEURISTIC, T1/T2).
- **Willingness-to-pay (WTP) data beats guessing**: Campbell's 4-point economic survey — "too expensive / getting expensive / a good deal / too cheap to trust the quality" — open-ended price answers, surveyed across 3 groups: current customers, prospects who know you, target customers who've never heard of you (they give different answers; brand lifts WTP) (FRAMEWORK, T1).
- **Survey, don't A/B test, for pricing** (Campbell): pricing A/B tests need >30,000 users for a 10% lift; customers find them disingenuous. Ask instead (EMPIRICAL, T1).
- **Revisit pricing regularly** (Campbell: quarterly; Poyar: 2025 data shows market moving constantly): "unchanged prices mean years of lost revenue" (HEURISTIC, T1).
- **Usage/outcome-based pricing wins when it matches value, but adds forecasting burden** (Poyar 2026): credit models exploded +126% YoY in 2025 among top 500 SaaS/AI, then the pendulum swings back to simplicity — 2026 trend is re-bundling and hybrid (EMPIRICAL, T1).
- **Pricing problems are value-clarity problems** (Poyar): if customers don't understand what they pay for, no model feels right (OPINION/EMPIRICAL, T1).



## retail-media — Consensus
## Consensus
- **Retail media's pitch is closed-loop measurement + first-party purchase data, not reach** — deterministic attribution (ad view/click → purchase) is the differentiator vs open web (Instacart; Walmart Connect; Amazon DSP). FRAMEWORK, T1.
- **On-site sponsored placements are the performance layer; off-site (DSP, offsite media) is the brand/upper-funnel layer — never run one with the other's expectations** (Darkroom; Walmart Connect's own small-business vs enterprise solution split; existing retail-media skill). HEURISTIC, T1.
- **The flywheel**: DSP builds awareness → search captures demand → search data informs more efficient DSP audiences; "DSP is the upper-funnel and retargeting layer that makes search campaigns more efficient", not a replacement for SP/SB (Darkroom). FRAMEWORK, T2.
- **Incrementality is the only truth layer**: platform ROAS credits purchases that would have happened anyway; on-site sponsored ads on your own branded terms can just tax organic sales (SellerStack; existing skill; Instacart's published 3-level incrementality methodology: advertiser, system, experiment). EMPIRICAL (mechanism), T1.
- **Holdout-based tests belong on upper-funnel spend** (DSP/OTT), where "you're not betting the quarter on it"; brands rarely stomach going dark on search (SellerStack). HEURISTIC, T2.
- **New-to-brand (NTB) is the key CPG acquisition metric**; SB/DSP campaigns can report very high NTB (88% NTB attributed orders in one AMZ Pathfinder SB client case). EMPIRICAL (case), T2.
- **Start where the shopper is; one network done well beats three done thinly** — minimums, fee layers (platform + managed service), and learning curves are real (existing skill; Eva Commerce; Perpetua). HEURISTIC, T2.
- **Never advertise out-of-stock SKUs** — retail media amplifies supply problems (existing skill; universal). T1.
- **Trade coordination is structural**: retail media budgets often come from trade marketing, and JBP with the retailer unlocks credits/placement/data (existing skill; Walmart Connect partner model). HEURISTIC, T2.



## social — Consensus
## Consensus
- **Reach is a distribution system, not a content lottery.** van der Blom's 1.3M-post dataset: reach ≈ 50% your baseline norm + 29.5% this post's performance + 20.5% luck; posts 4x better than your own norm get +639% reach. Justin Welsh, Cole, Drew, Schmoyer all run systems (volume + formats + iteration), not virality bets. (EMPIRICAL, T1 for vDB data as reported)
- **Comments/depth > likes everywhere.** LinkedIn: saves/DM-sends now beat likes (vDB); comment threads weighted, individual comments now rated. X: reply value > like. YouTube: retention depth > CTR alone. (EMPIRICAL/HEURISTIC)
- **Write for one person, one idea** (Drew's Rule of One; Cole's 4A frameworks; Welsh's "1 idea → 7 formats"). (HEURISTIC, 3+ independent)
- **Consistency + format rotation beats single-post optimization.** Welsh posts 20-30x/day systemically; Cole: succeed on ONE platform first, then republish. vDB: two text posts back-to-back costs -25% reach on second — rotate formats. (EMPIRICAL/HEURISTIC)
- **Community: purpose before platform; activity ≠ value** (Millington: activity-boosting tactics raise costs more than value; 6 specific behaviors drive loyalty). (FRAMEWORK, T1)
- **YouTube: packaging (thumbnail+title) decides whether retention ever gets a chance** (Schmoyer/Eves); retention graphs are the diagnostic tool. (HEURISTIC, T2)


