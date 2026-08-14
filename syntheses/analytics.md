# SYNTHESIS — Analytics, Dashboards & Product Metrics

Practitioners: Avinash Kaushik, Krista Seiden, Michele Kiss, Chris Mercer, John Cutler, Gibson Biddle. Verified 2026-08-15.

## Consensus
- **Dashboards are for decisions, not data display** (Kaushik, Kiss, Mercer): "slay the data-puking dragon." Every metric on a dashboard must have a pre-assigned target and a decision attached; else it's noise (FRAMEWORK, T1).
- **KPI hierarchy, not flat metric soup** (Kaushik): ~6 KPIs for the CEO, ~6 for the CMO, each with target + benchmark; micro-diagnostics belong in analysis views, not dashboards (HEURISTIC, T1).
- **Focus on outliers** (Kaushik): dashboards should surface KPIs 3 standard deviations from the mean — the abnormal needs attention, the normal doesn't (HEURISTIC, T1).
- **Metrics need context, intent, and actionability** (Cutler's Vanity Metric Test): a metric is vanity if it (1) lacks context ("compared to", "as input into", "balanced by"), (2) has unclear intent (why is this the measure of success?), (3) doesn't guide action/learning (FRAMEWORK, T1).
- **North Star needs inputs/proxy metrics, not just a single number** (Biddle, Cutler): the NSM is a lagging multi-year outcome; teams need *proxy metrics* — leading indicators defined as "% of users who do at least X by Y time" (Biddle's Netflix example: % of new customers watching ≥15 min streaming in first month) (FRAMEWORK, T1).
- **Averages hide the distribution** (Biddle): prefer threshold/cohort metrics over averages; average engagement can rise while most users get worse (EMPIRICAL, T1).
- **Measurement setup is a discipline** (Seiden): GA4 setup best practice = config via GTM, enhanced measurement, register custom dimensions/metrics, set data retention (14mo free/50mo 360), choose attribution model explicitly (TACTIC, T1).

## Disagreement
- **"North Star metric" terminology** (Biddle explicitly avoids the phrase — "rarely that simple," exec teams prioritize engagement 2nd or 3rd so the NSM creates confusion) vs Cutler's North Star Workshops (embrace NSM but keep it "a bit out of reach" and pair with inputs). Both agree on the mechanism; they disagree on naming/centrality (OPINION, T1).
- **Actionability test**: Cutler warns teams over-apply "actionability" — a metric can be meaningful but not directly actionable, or exploratory; forcing every metric to be actionable produces "safe" vanity metrics that convey good news (T1). Kaushik's rule (kill anything without a target) is stricter; condition: Kaushik = exec reporting, Cutler = product teams.
- **GA4 vs alternatives**: Mercer pragmatic on GA4's limitations (data-driven attribution default, sampling, 14-month retention); Kiss adds "measure what matters, not what's easy." No real disagreement — both say tool is secondary to question (T2/T3).

## Conditions
- Kaushik dashboard rules: orgs with real exec reporting cadence and targets; fails where no targets exist yet (then step 1 is setting targets) (T1).
- Cutler vanity test: product teams with instrumentation; works pre- and post-PMF (T1).
- Biddle proxy metrics: subscription/retention products with defined value moment (T1).
- Seiden GA4 setup: any GA4 property; Google-specific (T1).

## Failure knowledge
- Dashboards with 30+ metrics and no targets → nobody looks, decisions happen elsewhere (Kaushik; T1).
- Celebrating metrics that don't change strategy when they drop (Cutler: "if a number goes up and the only action is a furrowed brow, it's vanity") (T1).
- Metric becomes a target → becomes vanity/gamed (Cutler: Goodhart's law in practice; "once a metric becomes a signal of doing a good/bad job, people will make sure it goes up") (T1).
- Averages masking distribution failure (Biddle; T1).
- Treating NSM as the only metric → teams wake up unable to influence it, disengage (Cutler; T1).
- GA4 setup sins (Seiden): no custom events, no registered dimensions, default attribution accepted blindly, data retention left at 2 months (T1).

## Collision Method sketch — Analytics & Dashboards
- **Objective**: turn raw analytics into a decision-support system: KPI hierarchy → dashboard with targets → proxy metrics for the NSM → outlier alerting.
- **Prerequisites**: measurement plan (events + dimensions), analytics access, exec team able to set targets.
- **Diagnosis**: (1) audit existing dashboard metrics — count those with targets; (2) apply Cutler's vanity test to each; (3) identify the business's high-level engagement metric (Biddle) or NSM; (4) define 1-3 proxy metrics with threshold definitions.
- **Decision rules**:
  1. IF a dashboard metric has no target AND no decision attached THEN remove it (Kaushik, T1).
  2. IF a metric lacks context/intent/actionability THEN mark vanity and replace (Cutler, T1).
  3. IF NSM is defined THEN define proxy metrics as "% of [segment] who do ≥[threshold] by [time]" (Biddle, T1).
  4. IF reporting averages THEN add distribution/cohort view alongside (Biddle, T1).
  5. IF KPI deviates >3σ from its own mean THEN escalate to exec with hypothesis (Kaushik, T1).
  6. IF a metric moves but no tactic changes THEN drop it from the dashboard (Cutler, T1).
  7. IF GA4 property is new THEN set retention ≥14mo, register custom dims, choose attribution model explicitly (Seiden, T1).
  8. IF the team can't influence the NSM directly THEN add input metrics, keep NSM as compass (Cutler/Biddle, T1).
- **Metrics**: % of dashboards with targets, vanity-metric count, proxy-metric correlation to NSM (causal where possible), outlier alerts per period, dashboard usage (who opens, what they act on).
- **Stopping rules**: stop adding metrics when every existing one has a target and an owner; stop a proxy metric if it shows no correlation to the NSM after 2 quarters.
- **Failure modes**: data puking, target-less dashboards, gamed targets (sandbagging — Kaushik warns), average-masking, NSM paralysis.
- **Confidence**: T1 for Kaushik/Cutler/Biddle/Seiden (primary sources fetched); T2 for Mercer/Kiss (secondary).

## Sources
1. Avinash Kaushik — Five Strategies for Slaying the Data Puking Dragon | kaushik.net/avinash/slaying-data-puking-dragon-effective-dashboards | T1 | 2026-08-15
2. John Cutler — What Are Vanity Metrics and How to Stop Using Them | amplitude.com/blog/vanity-metrics | T1 | 2026-08-15
3. Gibson Biddle — How do you establish product metrics to evaluate success? | askgib.substack.com/p/how-do-you-establish-product-metrics | T1 | 2026-08-15
4. Krista Seiden — Ultimate Guide to Setting up a GA4 Property | kristaseiden.com/the-ultimate-guide-for-setting-up-a-google-analytics-4-property | T1 | 2026-08-15
5. Michele Kiss — analytics/dashboard writing (secondary) | T2
6. Chris Mercer — GA4/MeasureSchool (secondary) | T2
