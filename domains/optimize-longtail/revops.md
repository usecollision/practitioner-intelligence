---
practitioner: RevOps panel (lead scoring, routing, lifecycle)
role: RevOps/SalesOps operators, scoring tool vendors, CRM platform ecosystem, academic speed-to-lead research
company: Oldroyd/McElheran/Elkington (HBR); Prospeo; Ivris Tech; RevBlack; NC Squared; Kubaru; OnTheFuze (HubSpot partner); Calendly; Zapier
type: operator|researcher|insider
confidence: T1 (Oldroyd HBR) / T2 (operator consensus)
domains:
  - crm
  - revops
verified: 2026-08-15
sources_checked: 10
---
# Panel — RevOps: lead scoring, routing, lifecycle

## Experts found
- **James Oldroyd, Kristina McElheran, David Elkington** — "The Short Life of Online Sales Leads," HBR 2011 (MIT/InsideSales.com study, 15,000+ leads, 100,000+ call attempts). The canonical speed-to-lead evidence (T1, academic).
- **Prospeo** — three-layer scoring framework (ICP fit gate → intent filter → engagement warmth); "never let engagement override bad fit"; demo requests override the model; data hygiene as prerequisite (T2, vendor playbook).
- **Ivris Tech** — scored-model calibration: above-threshold leads should convert ≥2x; sales acceptance ≥80%; negative scoring and decay examples; scoring curiosity vs buying intent failure case (T2).
- **RevBlack** (via Prospeo) — MQL→SQL ~30% benchmark; weekly review first month then quarterly; recalibrate on >5-point drift (T2/T3).
- **NC Squared** — MQL threshold 60–80 points typical (enterprise 75–100); hybrid human-judgment models; quarterly recalibration (T2/T3, vendor).
- **OnTheFuze (HubSpot Elite Partner)** — 8 lifecycle stages; lifecycle = achievement (macro) vs lead status = rep activity (micro); BANT for SQL verification; SQL→Opportunity <20% = definition too loose; definitions signed by both teams, review quarterly year 1 (T2).
- **Kubaru / Calendly / GrowInTandem** — routing practices: territory/load/specialization signals, sub-5-minute speed-to-lead targets (Ooma case: 20% faster response, +10% conversions), reassignment safeguards (T2/T3, vendors).

## Beliefs
- Speed-to-lead is the biggest single conversion lever: responding within 5 minutes vs 30 minutes → ~100x more likely to connect, ~21x more likely to qualify; ~78% of buyers buy from the first responder; average B2B response time 42–47 hours; ~38% of online leads never get any reply (Oldroyd, EMPIRICAL, T1; replicated: Velocify 3.5M leads 2018; Optifai N=939: 5-min SLA → +41% qualified pipeline in 90 days, close rate 34% @1min → 28% @10min).
- Scoring is three layers in strict order: fit (gate) → intent (filter) → engagement (warmth). Engagement must never override bad fit (Prospeo, HEURISTIC, T2).
- The most common scoring failure is measuring curiosity, not buying intent (Ivris case: 89-point grad student; scrapping the model and qualifying on problem/budget/decision-maker tripled close rate) (EMPIRICAL case, T2).
- Scoring needs negative signals (disqualifiers, competitors, careers-page visits) and time decay (30/60/90 days); a lead engaged 6 months ago is not engaged now (Ivris, HEURISTIC, T2).
- Lifecycle Stage is a macro property of what a contact has *achieved*; Lead Status is micro (what a rep did). Using lifecycle stage to track rep activity inflates pipeline fiction (OnTheFuze, FRAMEWORK, T2).
- Stage transitions have owners: Subscriber→MQL = marketing automation only; MQL→SQL = sales, only after BANT logged in a required field (OnTheFuze, FRAMEWORK, T2).
- Routing needs safeguards: unavailable reps, reassignment of unworked leads, load balancing, and logs (Kubaru/Calendly, HEURISTIC, T2).

## Calibration targets (operator consensus, HEURISTIC/T2)
- MQL→SQL ≈ 30% (400 MQLs → ~120 SQLs) — significantly below = scoring passes unqualified leads.
- Above-threshold leads convert ≥2x below-threshold leads.
- Sales acceptance rate ≥80%.
- SQL→Opportunity ≥20% after 60–90 days (below = too loose).
- MQL threshold 60–80 points (enterprise 75–100).
- Recalibrate weekly first month, then quarterly; adjust when MQL→SQL drifts >5 points.
- Speed-to-lead: <5 minutes ideal; sub-1-hour SLA minimum; 5-min SLA → +41% qualified pipeline (Optifai).

## Failure modes
- Scoring curiosity as intent (whitepaper downloads ≠ buying) — the #1 scoring failure (Ivris, Prospeo).
- Premature handoff: pricing-guide download → SQL; the rep finds a student; marketing-sales trust erodes (OnTheFuze).
- Routing to empty territories with no reassignment — leads sit for weeks (Kubaru).
- Scoring on dirty data (bounced emails, wrong titles) — the model inherits the rot (Prospeo).
- Lifecycle stages defined by vibes; no exit criteria; no timestamps — velocity math impossible (OnTheFuze, skill-consistent).
- Marketing optimizing MQL volume while sales ignores the leads (no acceptance-rate feedback loop).
- Rejected leads with no recycle rule — they die silently instead of returning to nurture (OnTheFuze).

## Decision rules
1. IF an inbound lead is high-intent THEN route within 5 minutes; response time is the biggest lever (Oldroyd, EMPIRICAL, T1).
2. IF scoring THEN fit gate → intent filter → engagement warmth, in that order (Prospeo, HEURISTIC, T2).
3. IF a demo request comes in THEN override the score and route immediately (Prospeo, HEURISTIC, T2).
4. IF above-threshold leads don't convert ≥2x below-threshold leads THEN recalibrate the model (Ivris, HEURISTIC, T2).
5. IF sales acceptance <80% OR MQL→SQL <30% OR drifts >5 points THEN tighten fit criteria before touching engagement weights (RevBlack/Ivris, HEURISTIC, T2).
6. IF SQL→Opportunity <20% after 60–90 days THEN raise the SQL bar (OnTheFuze, HEURISTIC, T2).
7. IF a lead is rejected by sales THEN recycle to nurture with a coded reason (OnTheFuze, FRAMEWORK, T2).
8. IF scoring a lead with old activity THEN apply decay — engagement from 6+ months ago is not engagement (Ivris, HEURISTIC, T2).

## Conditions / Limitations
- Speed-to-lead research is strongest for high-intent inbound (forms, demo requests, local-service leads); outbound/prospecting follow-up timing is a different problem.
- Calibration numbers are vendor/operator consensus, not peer-reviewed; treat as starting points, not laws (T2/T3).
- Oldroyd's 100x figure is cited everywhere but the underlying study is 2007-era; direction is replicated (Velocify, Optifai), magnitude varies by vertical.
- Rules-based scoring is sufficient until data volume supports predictive scoring; even then keep overrides (Prospeo).

## Sources
1. Oldroyd, McElheran & Elkington — "The Short Life of Online Sales Leads" | hbr.org/2011/03/the-short-life-of-online-sales-leads (also hbs.edu/faculty/Pages/item.aspx?num=39955) | T1 | 2026-08-15
2. Casey Response — Lead Response Time Statistics (compilation incl. Velocify, HBR/MIT figures) | caseyresponse.com/blog/lead-response-time-statistics | T2 | 2026-08-15
3. Optifai — Speed to Lead: 5-Minute Response = 21x Higher Qualification (N=939 benchmark) | optifai.ai/learn/questions/speed-to-lead-statistics | T3 | 2026-08-15
4. Prospeo — Lead Scoring Best Practices for 2026 (three-layer model, demo override, data hygiene) | prospeo.io/s/lead-scoring-best-practices | T2 | 2026-08-15
5. Ivris Tech — Lead Scoring Best Practices: B2B Guide (calibration rules, negative scoring, decay) | ivristech.com/lead-scoring-best-practices | T2 | 2026-08-15
6. RevBlack — RevOps Lead Scoring Playbook (MQL→SQL 30%) | revblack.com/guides/revops-lead-scoring-playbook (via Prospeo) | T2/T3 | 2026-08-15
7. NC Squared — Lead Scoring: Definition, Models, Best Practices (60–80 threshold) | nc-squared.com/blog/article/what-is-lead-scoring | T2 | 2026-08-15
8. OnTheFuze — HubSpot Lifecycle Stages Explained (8 stages, BANT SQL, <20% rule) | onthefuze.com/hubspot-insights-blog/hubspot-lifecycle-stages-explained | T2 | 2026-08-15
9. Kubaru — 7 Lead Routing Best Practices (criteria, safeguards, Ooma case) | kubaru.io/blog/lead-routing-best-practices | T2 | 2026-08-15
10. Calendly — Lead routing 101: examples, best practices, automation tips | calendly.com/blog/lead-routing | T2 | 2026-08-15
