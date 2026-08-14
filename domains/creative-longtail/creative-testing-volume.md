---
practitioner: Creative volume consensus (Denney/Shackelford/hawky/AdGenz/AdManage/Koro)
role: multi-source panel on creative testing volume, cadence, and taxonomy
company: practitioner consensus (agencies, platforms, operators)
type: practitioner|agency|analyst
confidence: T2 (Denney, Shackelford, operator consensus); T3 (vendor benchmarks)
domains: [ad-creative, creative-testing, ugc-advertising]
verified: 2026-08-15
sources_checked: 7
---
- ## Beliefs — Creative supply rate is the operating variable of modern paid social: the algorithm clusters similar creatives, so *distinct concepts* are the unit of learning, and budget determines how many you can test per week. Creative fatigue — not targeting — kills accounts (Denney). Shackelford: creative is the new targeting; his Konstant Kreative team produced 50+ videos/day at scale; structure the testing budget explicitly between proven winners and fresh creative.
- ## Frameworks
  - **Budget-scaled cadence** (Denney): $5k–30k/mo → 1 ASC campaign, 1–3 new creatives/week, cap ~10 live, iterate winner 10 ways.
  - **Concept-volume baseline** (hawky 2026): 2–4 *genuinely different* concepts/week at meaningful spend; brief from an angle matrix; equal conditions; 3–7 days or 1–2x target CPA before judgment; decision rules (winner/iterate/kill) defined pre-launch.
  - **Discovery batches** (AdGenz): 3–5 variants per concept batch; test order: hook → format → angle → offer framing (offer last, only after angle+format known).
  - **Rotation rhythm** (AdManage): top accounts rotate in new variants every 7–10 days; run tests ≥7–14 days to clear learning phase; brief cycle and test cycle run in parallel.
  - **Fatigue taxonomy** (AppsFlyer): ad fatigue = one ad overexposed; creative fatigue = same *kind* of ad feeling repetitive across the account. Different remedies: frequency caps + retire vs supply rotation + new angles.
  - **Creative taxonomy** (scalable.ad/beefed.ai/ORCA): deconstruct ads into hook/angle/visual/format; standardized naming [Platform]-[Campaign]-[Angle]-[Format]-[Version]; tag every ad; winners compound into a library.
  - **Reskin economy** (Hormozi/Shackelford): ~80% of resources on winner variations + hook splicing; scaling spend is downstream of scaling creative volume.
- ## Heuristics
  - "Thirty variations of the same concept fragment your budget and teach you nothing" (hawky).
  - 70-ads/week creative blitzes exist but require large budget + production infra (AdManage).
  - Winning signals decay: weight your creative baseline by recency; a 6-month-old winning hook may already be fatigued category-wide (hawky).
  - AI-volume claims (Koro): 20+ variants/week/product, >30% thumbstop, 20%+ ROAS lift vs control — T3, vendor-sourced, directional only.
- ## Decision rules
  - IF budget is $5k–30k/mo THEN 1–3 distinct creatives/week, cap ~10 live (Denney — EMPIRICAL, T2).
  - IF spend is meaningful (≥$10k/mo) AND production capacity exists THEN 2–4 distinct concepts/week (hawky — HEURISTIC, T3).
  - IF a creative wins THEN iterate/reskin 10 ways before new concepts (Denney — HEURISTIC, T2; Hormozi 80% reskin, T2).
  - IF testing THEN one variable per batch (hook first, offer last), equal conditions, 1–2x target CPA or 3–7 days minimum before any verdict (hawky/AdGenz — HEURISTIC, T3).
  - IF rotation stalls >7–10 days without new variants THEN production is the bottleneck, not strategy (AdManage — HEURISTIC, T3).
  - IF performance decays with rising frequency THEN treat as fatigue (retire/rotate) before blaming targeting or budget (Denney/AppsFlyer — EMPIRICAL/HEURISTIC, T2).
  - IF no creative taxonomy THEN build naming + tagging before scaling volume (ORCA/scalable.ad — HEURISTIC, T3).
- ## Metrics — supply rate (new distinct concepts/week vs budget), live-creative cap adherence, hook rate (30–50% thumb-stop good on Meta), 3s hold, CPA/CTR per creative, fatigue curve (frequency × CPA), winner-iteration yield, taxonomy coverage (% creatives tagged).
- ## Failure modes — variation-not-concept testing; underfunded/abandoned tests (joins paid-strategy.md Spike rule); killing winners on hunches; polishing instead of agitating (Denney); no taxonomy → no compounding learning; fatigue blindness; over-capping creatives at small budgets (dilutes learnings).
- ## Conditions — Meta/TikTok performance accounts with pixel + creative-level measurement; cadence scales down for lean teams (fewer concepts, longer windows) but never below 1–2x CPA per test.
- ## Limitations — all cadence numbers are operator heuristics (T2/T3), no RCTs; platform algorithm behavior shifts (2024–26 era); vendor AI-volume benchmarks unverified.
- ## Sources
  1. hawky.ai — Creative Strategy for Performance Marketing 2026 (angle matrix, 2–4 concepts/wk, mistakes) | hawky.ai/blog/creative-strategy-performance-marketing | tier 3 | 2026-08-15
  2. AdGenz — Facebook Ad Creative Testing 2026 (Discover/Validate/Scale, 3–5 variants, test order) | adgenz.ai/blog | tier 3 | 2026-08-15
  3. AdManage — Facebook Ad Creative Testing Framework (7–10 day rotation, 7–14 day tests) | admanage.ai/blog | tier 3 | 2026-08-15
  4. Denney panel — domains/messaging-longtail/dara-denney.md (1–3/wk, cap 10, iterate 10 ways) | local | tier 1 | 2026-08-15
  5. Shackelford — Open Residency Ep.08 (creative = new targeting, testing budget structure) + Konstant Kreative (50+ videos/day) | openresidency.com; x.com/iamshackelford | tier 2/3 | 2026-08-15
  6. AppsFlyer — Creative fatigue vs ad fatigue | appsflyer.com/blog/tips-strategy/creative-fatigue | tier 2 | 2026-08-15
  7. Koro — UGC best practices 2026 (AI volume metrics) | getkoro.app/blog | tier 3 (vendor) | 2026-08-15
