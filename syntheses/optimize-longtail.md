# SYNTHESIS — Optimization Long Tail (funnels, checkout, forms, activation, UTM, automation, RevOps, attribution ops, experimentation programs)

Reuses: syntheses/cro.md, syntheses/analytics.md, syntheses/paid-strategy.md. New research panels: Baymard (checkout), RevOps (lead ops), UTM governance, automation workflows (domains/optimize-longtail/). Verified 2026-08-15.

## 1. Funnel diagnosis (funnel-analysis) — from cro.md
- **Consensus**: diagnose before testing (Laja ResearchXL, Sullivan, Massey); report volume with rates — "a 20% drop on 12 users is noise" (Kohavi sample-size math); marginal impact beats biggest drop-off (Laja, DRIP); segment leaks before theorizing (Laja, Wolf); internal baseline before external benchmarks (Massey, Kiss). FRAMEWORK/EMPIRICAL, T1.
- **Disagreement**: emotional/customer-first diagnosis (Wolf: analytics shows a leak, not why) vs data-first (Laja/Kohavi: hypotheses from observed behavior). CONDITION: message-level problems need qualitative; funnel mechanics with traffic need data.
- **Failure**: optimizing the biggest drop-off instead of biggest upside (DRIP RPU); mix-shift mistaken for funnel breakage (fix with cohorts — Biddle); benchmarks from a different model; rates without volumes.
- **Collision Method**: diagnosis order = 1) tracking health (SRM/A-A) 2) funnel table with volumes 3) cohort view (mix vs breakage) 4) segmented leak analysis 5) message-match audit 6) ranked action plan by volume × upside × evidence. Rules:
  1. IF tracking has SRM/known gaps THEN fix instrumentation before any diagnosis (Kohavi, EMPIRICAL, T1).
  2. IF a stage drop is <1K visits/week THEN do not treat it as testable signal; use qualitative + evidence stacking (MacDonald/Laursen, HEURISTIC, T2).
  3. IF choosing a stage to fix THEN rank by marginal impact (Δ overall = step rate × lift × volume), not drop-off size (Laja, FRAMEWORK, T2).
  4. IF a leak is confined to one source/device/segment THEN diagnose that segment, not the funnel (Laja, TACTIC, T2).
  5. IF benchmark comparisons are needed THEN use internal baseline first; external ranges labeled heuristic (Kiss/Massey, HEURISTIC, T2).
  6. IF cohort conversion shifted permanently at a date THEN look for product/market events before blaming pages (Biddle, TACTIC, T2).

## 2. Landing page & message match — cro.md + messaging
- **Consensus**: message-match is the biggest copy lever (Aagaard Saxo +99.4%, Bettingexpert +31.5%; Wolf messaging-audit-first); value clarity before cosmetics; research before hypothesis; traffic thresholds decide method (MacDonald 1K visits/week rule; Kohavi n ∝ σ²/Δ²); cosmetic tests are the field's #1 waste (Georgiev, DRIP). EMPIRICAL (Aagaard replications), T1/T2.
- **Disagreement**: element-level vs strategy-level testing (Aagaard single-factor vs Wolf big-swing; Scheijbeler decompose-after). CONDITION: traffic; big swings when effect must be detectable.
- **Failure**: redesign before diagnosing; testing button colors while message mismatch is the leak; optimizing for one source while traffic comes from another; heatmaps as verdicts (they generate hypotheses only); trust-element additions untested (Aagaard privacy policy −18.7%).
- **Rules**:
  1. IF ad/SERP promise ≠ page headline THEN fix message match before any other test (Aagaard, EMPIRICAL, T2).
  2. IF page <1K visits/week THEN skip small-effect A/B; run rapid concept tests or ship reversible changes with honest before/after (MacDonald, HEURISTIC, T2).
  3. IF hypotheses are opinion-only THEN score them (Evidence/Impact/Effort/Traffic/ROI or PXL) and drop the bottom (Massey/Laja, FRAMEWORK, T2).
  4. IF a change is invisible to users (button color, microcopy on low-traffic pages) THEN don't test it — spend the slot elsewhere (Georgiev, EMPIRICAL, T2).
  5. IF value prop unclear THEN run messaging research (customer language, Wolf's emotional-gap questions) before layout tests (Wolf, FRAMEWORK, T2).
  6. IF mobile >50% of traffic AND mobile conversion lags THEN fix mobile environment before message (universal, HEURISTIC, T2).

## 3. Checkout optimization — Baymard panel (NEW)
- **Consensus**: checkout design is frequently the *sole* cause of abandonment for users who added to cart (Baymard, 14 yrs, 54,000+ hrs testing; 2,700+ issues found); average cart abandonment 70.2% (50 studies); ~42% of abandonment is "browsing, not ready to buy" — largely unavoidable, don't chase it; most high-impact fixes are layout/microcopy — cheap (Baymard). EMPIRICAL (large-scale qualitative + quant: 272 think-aloud sessions, 11,777 survey participants), T1 for Baymard's own published findings.
- **Key quantified levers** (Baymard): extra costs higher than expected = 48% of abandoners (top cause); forced account creation = 26% (second); average checkout 23.48 form elements vs 12 achievable (7 fields) — 20–60% reduction possible; 16→8 fields ≈ 25–35% conversion lift; ~1 in 5 abandon as "too long/complicated"; average large site has 32–39 improvement areas, ~35% conversion potential.
- **Disagreement/conditions**: one-page vs multi-step — Baymard's own A/B found no significant difference; the decision is context: one-page wins for low-complexity, AOV <$150, mobile-heavy (70%+), 1–3 items; multi-step wins for AOV >$200, B2B/configurable, info-gathering beyond shipping+payment. **Perceived** field count beats actual: 15 fields across 3 logical steps outperforms 10 fields on one page by 11–14% completion. Mobile abandonment ~80% vs desktop ~66% (Dynamic Yield via Baymard) — a design problem, not a traffic problem.
- **Failure**: chasing the 42% browsing share; cutting fields that fulfillment needs; hiding costs until payment step; forcing accounts; express checkout desynced on discounts; recovery emails to empty carts.
- **Rules**:
  1. IF shipping/taxes/fees are not shown before the payment step THEN surface them earlier — top abandonment cause at 48% (Baymard, EMPIRICAL, T1).
  2. IF checkout requires account creation THEN make guest checkout the default; offer account after purchase (26% cause; Baymard delayed-account-creation, EMPIRICAL, T1).
  3. IF default form elements >12 THEN cut 20–60% before testing anything else (Baymard benchmark, EMPIRICAL, T1).
  4. IF choosing flow format THEN pick by context — AOV <$150/simple/mobile-heavy → one-page or accordion; AOV >$200/complex → multi-step; do NOT pick by page-count dogma (Baymard A/B, EMPIRICAL, T1).
  5. IF a 15-field form feels long THEN split into 3 logical steps rather than hiding fields on one page (+11–14% completion) (Baymard, EMPIRICAL, T1).
  6. IF abandonment cause data says "browsing" THEN exclude that share from optimization targets — it's not fixable in checkout (Baymard, EMPIRICAL, T1).

## 4. Forms & microcopy — cro.md + messaging + Baymard
- **Consensus**: field reduction is the highest-leverage form change (Baymard 16→8 fields 25–35%; Laja friction-first); every unnecessary field costs measurable completion; error copy must say cause + fix; labels persist, placeholders exemplify (NN/g-consistent); button copy = outcome + matches the pre-form promise (Aagaard Get/My replications; message match).
- **Failure**: placeholder-as-label; aggressive validation rejecting legitimate input (Baymard: users leave when they can't complete a field); adding fields back "for segmentation"; polishing microcopy while the submit handler is broken; hide-required-fields-behind-expanders (Baymard).
- **Rules**:
  1. IF a field has no current consumer THEN kill it or defer to post-conversion (Baymard/Laja, EMPIRICAL, T2).
  2. IF an error message lacks cause+fix THEN rewrite inline ("card number looks short — check for missing digits") (universal, HEURISTIC, T2).
  3. IF button copy describes the mechanism ("Submit") THEN change to the outcome promised pre-form (Aagaard, EMPIRICAL, T2).
  4. IF validation rejects formats users naturally type THEN forgive (spaces, dashes, lowercase) (Baymard, EMPIRICAL, T2).
  5. IF microcopy tests are planned on a <1K-visits/week form THEN run one big copy swing or ship + honest before/after, not a long A/B (MacDonald, HEURISTIC, T2).

## 5. Signup & activation — cro.md + analytics.md (Cutler/Biddle)
- **Consensus**: activation = the earliest action that predicts retention, defined as "% of [segment] who do ≥[threshold] by [time]" (Biddle Netflix 15-min example); never "logged in" (Cutler); data not vibes — correlation on historical cohorts; field reduction; one test per stage. T1 (Cutler/Biddle primary).
- **Disagreement**: North Star naming (Biddle avoids "NSM"; Cutler runs NSM workshops) — both agree on mechanism: NSM + input/proxy metrics.
- **Failure**: optimizing signup completion while activation stays broken; activation metric by opinion; averages masking distribution (use cohorts); onboarding teaching features instead of driving to aha.
- **Rules**:
  1. IF activation metric undefined THEN define as "% of [segment] doing ≥[threshold] by [time]" and validate against retention before freezing (Biddle, FRAMEWORK, T1).
  2. IF "logged in" or "account created" is proposed as activation THEN reject — it doesn't predict retention (Cutler, FRAMEWORK, T1).
  3. IF signup completion is optimized while activation is flat THEN shift focus — signups without activation are vanity (Cutler, HEURISTIC, T2).
  4. IF a signup flow change is tested AND page traffic <1K visits/week THEN use the low-traffic path (rapid/concept/ship-reversible) (MacDonald, HEURISTIC, T2).
  5. IF the aha moment is unknown THEN test candidate milestones against week-4/8 retention on historical cohorts before choosing (Cutler/Biddle, EMPIRICAL, T2).

## 6. Product analytics — analytics.md
- **Consensus**: dashboards for decisions (Kaushik); vanity-metric test = context/intent/actionability (Cutler); proxy metrics for NSM (Biddle); averages hide distribution (Biddle); outlier escalation >3σ (Kaushik); object-action event taxonomy, one identity strategy (Cutler/Seiden). T1.
- **Rules**:
  1. IF a metric lacks context/intent/actionability THEN mark vanity and replace (Cutler, T1).
  2. IF defining activation/NSM inputs THEN use threshold-cohort form "% of X doing ≥Y by Z" (Biddle, T1).
  3. IF reporting averages THEN add distribution/cohort view (Biddle, T1).
  4. IF an event name is generic (clicked_button) THEN rename object_action (invite_sent) (Cutler, TACTIC, T2).
  5. IF identity merges are unhandled THEN fix before trusting any per-user report (Cutler/Seiden, EMPIRICAL, T2).
  6. IF a KPI deviates >3σ THEN escalate with hypothesis, not blame (Kaushik, HEURISTIC, T1).

## 7. UTM governance — UTM panel (NEW)
- **Consensus**: UTM mistakes are permanent — you cannot edit analytics history; fix forward, merge at the analytics layer (McGaw/UTM.io, Funnel); lowercase + hyphens only, GA4 treats values as case-sensitive (WebIQ, McGaw); medium values must match GA4 channel groupings or traffic lands "Unassigned" (WebIQ, UTM.io); never tag internal links (overwrites source/attribution — utmbuilder, McGaw); every external link needs at minimum source+medium+campaign; governance owner + living doc + monthly drift review (Napkyn, Usermaven); taxonomy layers are distinct — taxonomy (what we measure), naming convention (format), campaign name (instance) (Improvado); >9 fields needs a formal governance committee + owner, else stay at 7 (Improvado).
- **Failure**: no owner (nobody enforces); too-strict taxonomy → people bypass and tag nothing; syntax errors (ampersand on bare URL → 404; double ?); vague campaign names; auto-tagging + manual mixed without mapping; changing conventions mid-year and blaming the market; cleaning history by editing links.
- **Rules**:
  1. IF a new UTM value is proposed THEN require lowercase, hyphens, and a source/medium pair from the canonical table (McGaw, TACTIC, T2).
  2. IF medium ≠ GA4 default channel value THEN change it — custom mediums become Unassigned (WebIQ, EMPIRICAL, T2).
  3. IF tagging internal links THEN stop — it overwrites the real source (utmbuilder/McGaw, EMPIRICAL, T2).
  4. IF no single owner exists THEN appoint one; governance without an owner fails (Napkyn/Usermaven, HEURISTIC, T2).
  5. IF taxonomy needs >9 fields AND no governance committee THEN stay at 7 — enforcement beats granularity (Improvado, HEURISTIC, T3).
  6. IF historical UTM values are messy THEN merge at the analytics layer; never edit old links (McGaw, EMPIRICAL, T2).

## 8. Automation workflows — automation panel (NEW)
- **Consensus**: "Send form submission to CRM" is not a workflow — the business rule is the automation: filters to block bad records, paths to route cases, multi-step updates, error handling so the team knows when automation needs attention (Alltomate, Zapier Platinum partner); use native in-app automation first when the flow starts and ends in one tool (data never leaves the ecosystem — Olostep); low-code connectors (Zapier/Make/n8n) are middleware for cross-tool flows; choose tooling by complexity, event scale, governance needs, data origin (Olostep); common patterns: lead intake with enrichment+scoring, behavior-based follow-up, ops handoff, competitive monitoring, scheduled reporting (Alltomate, n8n template library 3,400+ marketing workflows, Zapier).
- **Failure**: automating a broken process; silent failures (no error triggers/retries/alerting — n8n error-handling guides; Zapier Xero find-or-create failures); no filters → garbage into CRM; undocumented automations (bus factor 1); automation debt (repeating the same manual process weekly); no relevance review (workflows outlive their purpose).
- **Rules**:
  1. IF the process is broken manually THEN fix the process before automating it (Alltomate/universal, HEURISTIC, T2).
  2. IF a workflow has no error path THEN add error trigger + retry + alert before enabling (n8n/Alltomate, EMPIRICAL, T2).
  3. IF the flow lives entirely in one tool THEN use that tool's native automation, not a connector (Olostep, HEURISTIC, T2).
  4. IF automating lead intake THEN include filters for bad records and required-field checks — unvalidated intake corrupts the CRM (Alltomate, EMPIRICAL, T2).
  5. IF prioritizing what to automate THEN pick high-frequency × high-impact × currently-manual (universal, HEURISTIC, T2).
  6. IF a workflow runs silently without documentation THEN document + name an owner, or it dies with its builder (Zapier/universal, HEURISTIC, T2).

## 9. CRM lead ops (RevOps) — RevOps panel (NEW)
- **Consensus**: speed-to-lead is the single biggest conversion lever: 5-minute response = ~100x more likely to connect and ~21x more likely to qualify vs 30 min; 78% buy from the first responder; average B2B response 42–47 hours (Oldroyd/McElheran/Elkington, HBR 2011, 15,000+ leads — EMPIRICAL, T1; replicated by Velocify 3.5M leads, Optifai N=939: 5-min SLA → +41% qualified pipeline). Scoring: three layers — ICP fit as gate, intent as filter, engagement as warmth; never let engagement override bad fit; demo requests override the model (Prospeo, HEURISTIC, T2). Negative signals and decay (30/60/90 days) mandatory (Ivris, T2). Lifecycle stage = what a contact has *achieved* (macro); lead status = rep activity (micro); never use lifecycle to track activity (OnTheFuze/HubSpot, FRAMEWORK, T2). MQL/SQL definitions written, owned by revenue leadership, signed by both teams; review quarterly year 1 (OnTheFuze, T2).
- **Quantified calibration rules** (HEURISTIC, T2, operator consensus): MQL→SQL ≈ 30% benchmark; scored-above-threshold leads should convert ≥2x below-threshold leads; sales acceptance rate target ≥80%; recalibrate when MQL→SQL drifts >5 points; SQL→Opportunity <20% = SQL definition too loose; typical MQL threshold 60–80 points (enterprise 75–100); review weekly first month then quarterly.
- **Failure**: scoring curiosity not buying intent (Ivris case: 89-point grad student; close rate tripled after scrapping the model); premature handoff (pricing-download → SQL) erodes marketing-sales trust; routing to empty territories with no reassignment rule; scoring on dirty data (bounced emails, wrong titles); no recycle rule for rejected leads.
- **Rules**:
  1. IF an inbound lead is high-intent (demo request, MQL threshold crossed) THEN route within 5 minutes — response time is the biggest lever (Oldroyd HBR, EMPIRICAL, T1).
  2. IF scoring a lead THEN fit gates first, intent second, engagement last — engagement must never override bad fit (Prospeo, HEURISTIC, T2).
  3. IF a lead requests a demo THEN override the score and route immediately (Prospeo, HEURISTIC, T2).
  4. IF above-threshold leads don't convert ≥2x below-threshold leads THEN recalibrate the model (Ivris, HEURISTIC, T2).
  5. IF sales acceptance <80% OR MQL→SQL <~30% OR drifts >5 points THEN tighten fit criteria before touching engagement weights (RevBlack/Ivris, HEURISTIC, T2).
  6. IF SQL→Opportunity <20% after 60–90 days THEN the SQL definition is too loose — raise the bar (OnTheFuze, HEURISTIC, T2).
  7. IF a lead is rejected by sales THEN route to recycle/nurture with a coded reason — no silent graveyard (OnTheFuze/HubSpot, FRAMEWORK, T2).

## 10. CRM pipeline attribution — paid-strategy attribution layer
- **Consensus**: platform/marketing attribution overstates performance; the CRM lead-to-revenue layer is the truth layer for B2B (Seufert: last-click veneer; Walker: "your budget tells the truth" — map revenue to real source); preserve first-touch and last-touch separately; source fields must survive merges; reconcile CRM attribution vs platform ROAS — they will disagree, explain not hide (Seufert overlap tax 1.4–1.8x; brand search iROAS ~10–25% of reported). T1/T2.
- **Rules**:
  1. IF source fields can be overwritten by "most recent" THEN store first-touch and last-touch separately (Seufert/Walker, EMPIRICAL, T2).
  2. IF CRM attribution and platform ROAS disagree THEN reconcile and explain — the gap is the overlap tax, not an error (Seufert/AdMaxxer, EMPIRICAL, T2).
  3. IF deals have no source THEN surface them in an "unknown" bucket; ignoring them biases every conclusion (universal, HEURISTIC, T2).
  4. IF MQL/SQL definitions are contested THEN fix ownership at revenue leadership (OnTheFuze, FRAMEWORK, T2).
  5. IF a stage has high exit-to-lost THEN treat as leakage (different fix) vs slowness (velocity) (universal, HEURISTIC, T2).
  6. IF handoff has no SLA THEN add response-time + recycle + feedback terms before reporting pipeline quality (Oldroyd, EMPIRICAL, T1).

## 11. Attribution model selection — paid-strategy + analytics
- **Consensus**: model by maturity, not fashion (level 1 last-touch → level 4 MMM/incrementality); different metrics for different decisions (Binet & Field principle 10); MER at P&L level (target ≈ 1.3/contribution margin — AdMaxxer); iROAS for budget decisions, platform ROAS only for creative; overlap tax >35% gap = platform ROAS fiction; MMM only with data volume (~$50–100k+/mo) and capability; incrementality tests need valid design (≥6–8 geo pairs, pre-test baseline) — "spending €40k on a confounded holdout is worse than not testing" (Metricuno). T1 consensus layer, T2 numbers.
- **Rules**:
  1. IF <3 channels AND <~$20k/mo THEN last/first-touch comparison is enough — do not build multi-touch (paid-strategy maturity ladder, HEURISTIC, T2).
  2. IF budget decisions rely on platform ROAS THEN compute MER and overlap tax first; act on iROAS not reported ROAS (Seufert/AdMaxxer, EMPIRICAL, T2).
  3. IF suspecting a channel (brand search, retargeting) THEN run a valid incrementality test before cutting (AdSights/Metricuno, EMPIRICAL, T2).
  4. IF evaluating MMM THEN require data volume + capability; below threshold use MER + lift tests (Seufert, OPINION, T2).
  5. IF a metric must move budget THEN attach it to a decision and a cadence; metrics without decisions are decoration (Kaushik, HEURISTIC, T1).

## 12. Experimentation program — cro.md
- **Consensus**: program metric = decisions supported + cumulative shipped impact, not test count (Vermeer); win-rate band 20–40% as hypothesis-quality diagnostic (below = cosmetic/researchless, above = too safe); 3–5x backlog coverage for decision throughput; guardrails pre-committed and checked at ship time; fixed-horizon or pre-planned sequential stopping (Kohavi/Georgiev: peeking for abort ok, never for win); losses mandatory in the learning library (Labay Phase Gate; Vermeer flywheel); org structure decides gates (CoE vs decentralized — Labay/Vermeer); stakeholder override kills programs (Atticus Li, adasight). T1 stats, T2 org frameworks.
- **Rules**:
  1. IF the program KPI is tests-run THEN replace with decisions-supported + cumulative impact (Vermeer, FRAMEWORK, T2).
  2. IF win rate <20% THEN hypothesis quality is the problem — more research, fewer cosmetic tests; if >40%, tests are too safe (DRIP/growwithba band, HEURISTIC, T2).
  3. IF a test looks like a win early THEN do not stop for significance; peek only to abort harm (Kohavi/Georgiev, EMPIRICAL, T1).
  4. IF a winner degrades a pre-committed guardrail THEN it does not ship (Kohavi OEC/Labay, FRAMEWORK, T1).
  5. IF a test is closed THEN require a mechanism-level learning — losses included (Sullivan/Labay, FRAMEWORK, T2).
  6. IF a stakeholder overrides a decision without data THEN escalate — override culture is the #1 program killer (Atticus Li/adasight, EMPIRICAL, T2).
  7. IF deciding test vs ship vs redesign THEN apply the traffic/message-match rules from §1–2 first (cro.md decision tree, FRAMEWORK, T2).

## Confidence summary
- T1: Oldroyd HBR speed-to-lead; Baymard institute's own published findings; Kohavi/Georgiev stats; Cutler/Biddle/Kaushik; McGaw on UTM permanence (primary practitioner).
- T2: operator/vendor consensus numbers (RevOps calibration targets, UTM governance practices, automation patterns, overlap tax) — consistent across multiple independent vendors but commercial sources.
- T3: single-source heuristics (Improvado 9-field inflection, Optifai close-rate decay curve, vendor ROI claims).

## Key sources
1. Oldroyd, McElheran & Elkington — "The Short Life of Online Sales Leads" | hbr.org/2011/03/the-short-life-of-online-sales-leads | T1 | 2026-08-15
2. Baymard Institute — Checkout Usability research + "Reasons for Cart Abandonment" | baymard.com/research/checkout-usability, baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark | T1 | 2026-08-15
3. Dan McGaw (UTM.io/Funnel.io) — UTM convention best practices + 21-point checklist | funnel.io/blog/utm-and-utm-convention-best-practices, web.utm.io/blog/utm-parameters-best-practices | T1/T2 | 2026-08-15
4. WebIQ/UTM Guard — UTM best practices 2026 (GA4 case-sensitivity, custom mediums) | webiq.app/blog/utm-best-practices-2026 | T2 | 2026-08-15
5. Improvado — Marketing Campaign Taxonomy Guide (layers, 7/9/11-field inflection) | improvado.io/blog/marketing-campaign-taxonomy | T2 | 2026-08-15
6. Alltomate (Zapier Platinum partner) — Zapier Workflow Examples: 4 patterns | alltomate.com/blogs/zapier-workflow-examples | T2 | 2026-08-15
7. Olostep — Workflow Automation: examples, tools & best practices (native-first) | olostep.com/blog/workflow-automation | T2 | 2026-08-15
8. OnTheFuze — HubSpot Lifecycle Stages Explained (8 stages, BANT SQL, <20% rule) | onthefuze.com/hubspot-insights-blog/hubspot-lifecycle-stages-explained | T2 | 2026-08-15
9. Prospeo / Ivris / RevBlack — lead scoring playbooks (three-layer model, 2x rule, 30% MQL→SQL) | prospeo.io/s/lead-scoring-best-practices, ivristech.com/lead-scoring-best-practices | T2 | 2026-08-15
10. Syntheses reused: cro.md (Kohavi, Georgiev, Laja, Sullivan, Aagaard, MacDonald, Labay, Vermeer, Atticus Li), analytics.md (Cutler, Biddle, Kaushik, Seiden), paid-strategy.md (Seufert, Binet & Field, AdMaxxer, Metricuno, Walker) | practitioner-intelligence/syntheses/ | T1/T2 | 2026-08-15
