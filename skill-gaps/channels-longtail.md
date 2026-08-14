# SKILL GAP ANALYSIS — Channels Long Tail (Wave A7, 2026-08-15)

Research: `syntheses/channels-longtail.md` · Domains: `domains/channels-longtail/` (4 panels) · Status: **implemented**

## Audit findings → changes

| Skill | Audit | Change |
|---|---|---|
| content-calendar | M2 | +Promise-first rule (Oshinsky), cadence-as-commitment, one-trick-per-year, winback→re-permission→prune (White), distribution cascade (3-5+ derivatives), velocity-vs-capacity metric, 7 decision rules, 6 sources |
| newsletter-operations | M2 | +Launch-fast + one-sentence promise (Oshinsky), engagement-over-opens post-MPP (White), Schwedelson send-time windows (Mon-Wed 5-8am / Thu-Sun 8-11am, never on the hour), one-revenue-stream-per-year, active-subscriber north star, 7 rules, 6 sources |
| reply-classification | M2 | +Reply-rate north metric (Mailshake), classification-as-lost-value (Ross: referrals/competitor/"talk to X" are pipeline), never-act-on-1-2-points rule (n≥10-20/monthly), yes/no-are-answers (Efti), objections-feed-copy loop, 7 rules, 5 sources |
| domain-reputation-ops | M2 | +Auth-is-not-delivery (Iverson), 15-30/mailbox/day caps + no-doubling (Berman/Gmail), degraded-volume→rest→retire ladder, warm-up-automation T3 risk (Atkins), spare-domain failover, bounce thresholds (2/5/10%), 7 rules, 5 sources |
| lead-sourcing-enrichment | M2 | +Bought-list ban (all), provider-claims-are-hypotheses with 2026 field benchmarks (Apollo 78% vs ZoomInfo 84% vs ~96% waterfall), data decay 22.5%/yr + quarterly re-verify, cost-per-usable-record, provider interrogation questions (SMTP method/refresh/feedback loop), 7 rules, 6 sources |
| pinterest-threads | M2 | FULL RESEARCH GAP FILLED: platform panel (600M MAU, purchase-intent stats, dead-tactics list, SEO mechanics, saves/closeups/CTR analytics decision rules, Threads algorithm factors, 70/20/10, cross-posting rules), 7 rules, 9 sources |
| product-launch-playbook | M2 | +PESO order (Dietrich), pre-PMF founder-led gate (Rachitsky), Zitron pitch discipline (≤150 words), newsjacking lanes (Meerman Scott), journalist-reply-rate ≥5% kill rule, AI-citation metric, 7 rules, 6 sources |
| programmatic-seo | M2 | +Uniqueness floor (Indig + enforcement collapses), waves + indexation monitoring (~10% slice), Critchlow template-testing gate (≥100 pages, −27% incident), diagnose-before-nuking (Gabe/Ray), decay + pruning, 6 rules, 5 sources |
| serp-analysis | M2 | +Capper correlation filter, AI-citation tracking addition (Indig decoupling: presence/portability/concentration per engine — flagged in wave-2 gaps, now closed), topic-level aggregation (Solis), AIO CTR compression (Law/Guan −34.5%), 6 rules, 6 sources |
| international-seo | M2 | +Solis process (local-language demand first, hreflang generator), architecture default subdirectory/ccTLD conditions, hreflang completeness facts (bidirectional/self-ref/x-default/one mechanism), material-localization bar, seoClarity failure data, 6 rules, 5 sources |

## Key encoded knowledge

1. **Cadence is a commitment, not a wish** — publish less, consistently; gaps train readers to forget you (Oshinsky/White, T1).
2. **One trick per year** — one new format/monetization stream per year, matched to audience and proof (Oshinsky, T2).
3. **Unclassified replies are the lost-value trap** — referrals/competitor mentions/"talk to X" are pipeline (Ross, T1); never act on 1-2 data points.
4. **Consistent volume is the reputation governor** — 15-30/mailbox/day, no Monday bursts, no doubling; bounce >5% yellow / >10% red (Berman/Gmail, T1).
5. **Provider accuracy claims are hypotheses** — 2026 field benchmarks: 78% Apollo / 84% ZoomInfo / ~96% waterfall (vendor tests, T3); test on your own list; data decays 22.5%/yr (T2).
6. **Pinterest = visual search engine with purchase intent** — SEO mechanics + saves/outbound-click metrics; old repin playbook dead (T2/T3).
7. **Threads = conversation feed** — engagement velocity in first 30 min, links deprioritized, 70/20/10 mix (T3).
8. **Programmatic: uniqueness floor, waves, test template changes** — enforcement collapses + −27% incident (Indig/Critchlow, T1).
9. **SERP analysis now includes AI citations** — presence/portability/concentration per engine, never blended (Indig, T1).
10. **International: local-language demand first; hreflang complete or nothing** — failures compound silently (Solis/Google, T1).

## Evidence quality

- T1 (multi-source/practitioner convergence): cadence discipline, reply-rate north, volume caps, uniqueness floor, Capper filter, hreflang facts, PESO order.
- T2: Schwedelson % lifts, Oshinsky monetization, Solis international process, Pinterest SEO mechanics (multi-vendor convergence), data decay.
- T3 (single-source/vendor/aggregator — flagged in skill text): provider accuracy benchmarks (Cleanlist vendor tests), Threads algorithm specifics + engagement-rate claims (agency guides), seoClarity 20-300% hreflang lift, Tailwind top-1% study, Crescitaly analytics thresholds.
- NOT verified: Threads MAU consistency (175M→500M across dates/methods), any Pinterest ROI case numbers, provider claims of 91-98% accuracy.

## Cross-repo notes

- email-deliverability (already M4, email wave) and domain-reputation-ops now share Iverson/Atkins/Berman grounding — no conflicts; domain-reputation-ops adds the outbound scaling layer.
- serp-analysis closes the wave-2 flagged follow-up ("add AI-citation tracking — Indig decoupling").
- newsletter-operations ↔ lifecycle-sequences share White/Geisler rules; content-calendar ↔ marketing-messaging/content-strategy share cascade rules.
- Suggested follow-up: `pinterest-ads` in marketing-paid could reuse the pin-CTR/save decision rules when that repo is upgraded.

## Validation

- [x] 10 skills patched per M4 contract (Practitioner Grounding + Decision Rules ≥5 each, Metrics, Practitioner-Sourced Failure Modes, Sources — all before Evaluation & QA)
- [x] All claims tagged (FACT/EMPIRICAL/HEURISTIC/FRAMEWORK/OPINION/HYPOTHESIS) with T1-T3 confidence
- [x] Every Practitioner Grounding attribution resolves to a Sources entry
- [x] No commits per wave instructions (files staged in working tree)
