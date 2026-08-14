# Wave A4 — Customer & Audience Intelligence: Skill Gap Analysis & Changes

Date: 2026-08-15. Base: syntheses/audience-intel.md (new) + reuse of syntheses/research.md (survey bias, NPS, win/loss, interviews) and syntheses/positioning.md (battlecards).

## Skills upgraded to M4 (13 patches in marketing-intelligence)

| Skill | M4 additions | Primary grounding | Evidence quality |
|---|---|---|---|
| survey-design | Krosnick satisficing/order effects; NPS closed loop (<48h detractor follow-up, 3x promoters claim T3); response-rate guardrails | Krosnick (Stanford handbook, T1); CustomerGauge (T2); SurveyMonkey (T2) | T1 for questionnaire effects; T2/T3 for loop claims |
| reddit-research | Subreddit signal check (10k–500k members, 7-day posts, 10+ comments); comments-before-posts; confirmation-bias guard; F5Bot/site: tools | Reddinbox (T2); HubSpot (T2); PainOnSocial (T3) | T2 (practitioner consensus) |
| review-mining | 3-layer taxonomy (15–25 themes); Feature-Pain-Outcome triples; segment-split detection; recency weighting; source-bias caveats | Noisely (T2); Usercall (T3); BigSentiment (T3); Miro/Intercom examples (T3) | T2 method, T3 vendor examples |
| social-listening | Listening vs monitoring; define objectives before tool purchase; tool-tier ladder; query design; alert → action loop | Emplifi (T2); Sprinklr (T3); Brandwatch (T3) | T2 method; T3 tool marketing claims |
| support-ticket-mining | ≥500 tickets/3–6mo; hand-read 50–100; 8–15 categories; freeze after 1 revision; 5–10% threshold; 4 biases; revenue weighting; 90-day cadence | Kromatic (T1); Koji (T2); Pelin (T2 vendor); Intercom/Airbnb cases (T2) | T1 for bias/threshold method; T2 vendor cases |
| call-transcript-analysis | Two-pass mining; 5 Ms framework; aggregate queries in first 90 days; compliance first; quote-verification rule | Rework (T2); Adam Corey/PMA (T2); Gong (T2 vendor) | T2 (method consensus), T3 vendor benchmarks |
| customer-research | M4 sections anchored on existing research.md synthesis (no new research needed): saturation counts, past-behavior rules, persona evidence; adds loop-routing to sibling skills | Fitzpatrick/Revella/Moesta/Blank/ziellab (T1 via research.md) | T1 |
| win-loss-analysis | M4 sections anchored on Clozd rules: neutral interviewer, ≥20/segment, won+lost+no-decision, record+transcribe; adds action-item closure metric | Clozd (T1 via research.md) | T1 |
| account-intelligence | 5 data types; data shelf-life failure; FIRE scoring; freshness cadence (weekly/quarterly); intent-without-fit = noise | HG Insights (T2); ITSMA FIRE (T3); HockeyStack/Landbase (T2 vendor) | T2 method; T3 vendor claims |
| intent-signals | 4-party taxonomy; decay windows (0–7/8–30/>30); evidence-not-proof framing; job-change triggers; vendor claims marked T3 | Demandbase/G2/Bombora (T2); Prospeo (T3); Clay (T2); Amplemarket (T3) | T2 framing; T3 benchmarks — honest T3 where vendor-sourced |
| technology-analysis | 3 collection methods (source code, job postings, databases); refresh cadence; stack-maturity segmentation; displacement/gap plays; HubSpot 27%/34% marked T3 UNVERIFIED | Derrick (T3); StackWho (T3); BuiltWith (T2 vendor); Coresignal (T3) | T2 tool facts; T3 ROI claims |
| competitor-battlecards | M4 sections anchored on positioning.md (Dunford alternatives, Kellogg skepticism) + technographic battlecard technique (Derrick) + G2-review competitive reads (Noisely) | Dunford/Kellogg (T1 via positioning.md); Derrick (T3) | T1 for positioning core |
| ad-library-research | Free-first ladder (Meta Ad Library → spy tools); 4-way search expansion; creative-theme strategy read; performance-proxy caveat; analysis-before-copying rule | AdsUploader (T2); PrimeSpy (T3); Shopify (T2) | T2 method; T3 tool claims |

## Evidence quality notes
- **T1**: Krosnick questionnaire design (peer-reviewed); Kromatic ticket-mining biases (methodological, evidence-based); reuse of research.md consensus (Fitzpatrick/Clozd/saturation).
- **T2**: practitioner method guides (Reddinbox, Noisely, Rework, Corey, AdsUploader, Emplifi) — single-source but detailed and internally consistent with adjacent sources.
- **T3 (flagged in skills)**: all intent-data lift claims (6sense $50–100K/yr positioning, Amplemarket scoring, Bombora accuracy), technographic ROI stats (HubSpot 27%/34% via Derrick), CustomerGauge "3x promoters", Intercom 2x multiplier, Figma 23% retention example — vendor-sourced, marked T3/UNVERIFIED in the skills.

## Gaps not researched (deferred)
- Social-listening benchmark accuracy studies (sentiment model precision rates) — vendors don't publish; needs independent testing.
- Ad-library historical performance data (Meta removed spend/impression details from the public library; third-party archives unverifiable).
- Account-intelligence ROI benchmarks (ABM lift studies are vendor-funded).
- Survey response-rate benchmarks per channel (only vendor lists found).

## Cross-repo effects
- marketing-messaging: messaging skills should consume review-mining/transcript language output (customer language rule). Follow-up commit recommended.
- marketing-core: validate-tools.py / check-integrity.py should pass; no tool schema changes.
- marketing-channels: social-listening overlaps social/ engagement skills — listening insights should route to social channel skills as inputs.
