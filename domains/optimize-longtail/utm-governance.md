---
practitioner: UTM governance panel (taxonomy standards)
role: analytics consultants, UTM tool founders, GA4 specialists, data-engineering vendors
company: Dan McGaw (UTM.io/Funnel.io); Napkyn; Usermaven; WebIQ/UTM Guard; Improvado; DecisionFoundry; ZAG Interactive; utmbuilder
type: practitioner|founder|insider
confidence: T1 (McGaw primary) / T2 (consultant/vendor consensus)
domains:
  - analytics
  - attribution
verified: 2026-08-15
sources_checked: 8
---
# Panel — UTM taxonomy & governance

## Experts found
- **Dan McGaw** (founder UTM.io; ex-Kissmetrics head of marketing; "godfather of martech") — the closest thing to a UTM authority; UTM.io used by Shopify, Unilever, Taxjar. Core claims: UTM mistakes are permanent (you can't alter analytics parameters after the fact); lowercase only, dashes not spaces; match medium to analytics channel groupings; never tag internal links; document and enforce a team convention; keep parameters simple (T1 primary).
- **Monika Boldak / Napkyn** (GA4 analytics consultancy) — governance process: living UTM guide (accepted values, naming patterns, tracking rules, ownership), monthly review of tagged links, onboarding new team members to the standard (T2).
- **Usermaven** — 19 common UTM mistakes: missing source/medium/campaign minimum, no governance owner, syntax errors (ampersand on a URL with no query string → 404; double `?`), vague campaign names (`launch`, `promo1`), case drift (T2).
- **WebIQ / UTM Guard** — GA4 treats UTM values as case-sensitive → duplicate reports; custom utm_medium values end up Unassigned/miscategorized; stick to GA4 default channel values; enforce with URL builders/validation tools (T2).
- **Improvado** — campaign taxonomy: three distinct layers (taxonomy = what we measure / naming convention = format / campaign name = instance); 7-field standard for most teams; 9–11 fields only with formal governance committee + dedicated owner; "additional granularity without enforcement creates more chaos than no taxonomy at all" (T2/T3).

## Beliefs
- Tagging is a system, not a task: "UTM creation as an individual task rather than a team-wide standard" is a top mistake (Usermaven, T2).
- Every external link needs at least source + medium + campaign; content/term are reserved for ad variants and keywords (Usermaven, T2).
- Internal links must never carry UTMs — they overwrite the original source and ruin attribution (utmbuilder/McGaw, EMPIRICAL, T2).
- Auto-tagging (Google/Meta) is fine within a platform; manual tagging works everywhere — pick a mapping and document it, never mix unmapped (utmbuilder/McGaw, T2).
- Analytics-layer fixes (regex, merges, channel grouping rebuilds) are the only way to clean history; editing historical links corrupts the past (McGaw/Funnel, EMPIRICAL, T2).

## Failure modes
- No owner → governance doc read once, enforced never (all sources).
- Taxonomy so strict it's bypassed → people tag nothing (skill-consistent; Usermaven's "path of least resistance" argument).
- Case drift (`Email` vs `email`) → GA4 fragments reports (WebIQ).
- Custom mediums (`utm_medium=summer-promo`) → Unassigned traffic (WebIQ).
- Syntax errors → 404s or parameters ignored (Usermaven).
- Vague campaign names → 3 months later nobody knows what `promo1` was (Usermaven).
- Changing conventions mid-year → attribution changes blamed on the market (skill-consistent).
- UTM sprawl leaking into CRM source fields because form capture was never connected (skill-consistent; McGaw's portability point).

## Decision rules
1. IF a new UTM value is proposed THEN require lowercase + hyphens and a canonical source/medium pair (McGaw, TACTIC, T2).
2. IF utm_medium ≠ GA4 default channel value THEN change it — custom mediums become Unassigned (WebIQ, EMPIRICAL, T2).
3. IF tagging an internal link THEN don't — it overwrites the true source; use events instead (utmbuilder/McGaw, EMPIRICAL, T2).
4. IF an external link lacks source/medium/campaign THEN it doesn't ship (Usermaven, HEURISTIC, T2).
5. IF there is no single taxonomy owner THEN appoint one before writing any more rules (Napkyn/Usermaven, HEURISTIC, T2).
6. IF taxonomy design exceeds 9 fields AND no governance committee exists THEN stay at 7 — enforcement beats granularity (Improvado, HEURISTIC, T3).
7. IF historical values are messy THEN merge at the analytics layer; never edit old links (McGaw, EMPIRICAL, T2).
8. IF reviewing UTM health THEN re-run the inventory: distinct-value counts, % unassigned, % missing — sprawl should shrink quarterly (Napkyn/McGaw, HEURISTIC, T2).

## Conditions / Limitations
- GA4-centric guidance; other platforms (Amplitude, Mixpanel, custom warehouse) accept same principles but different channel-grouping definitions.
- Enforcement tooling claims (UTM Guard, UTM.io, Usermaven builder) are vendor-marketed; the underlying practices are consensus.
- Improvado's 7/9/11-field inflection is a single-source heuristic (T3).
- Small teams can govern with a documented convention + monthly check; the full committee model is for enterprise.

## Sources
1. Dan McGaw — UTM and UTM convention best practices | funnel.io/blog/utm-and-utm-convention-best-practices | T1 | 2026-08-15
2. Dan McGaw — UTM Parameters Best Practices: 21-Point Checklist | web.utm.io/blog/utm-parameters-best-practices | T1 | 2026-08-15
3. Napkyn (Monika Boldak) — Best Practices for Using UTM Parameters in Marketing Campaigns | napkyn.com/blog/best-practices-for-using-utm-parameters-in-marketing-campaigns | T2 | 2026-08-15
4. Usermaven — 19 Common UTM Mistakes (and How to Fix Them) | usermaven.com/blog/critical-utm-mistakes | T2 | 2026-08-15
5. WebIQ/UTM Guard — UTM Parameter Best Practices for 2026 | webiq.app/blog/utm-best-practices-2026 | T2 | 2026-08-15
6. Improvado — Marketing Campaign Taxonomy Guide 2026 | improvado.io/blog/marketing-campaign-taxonomy | T2 | 2026-08-15
7. utmbuilder — Master UTM Naming Conventions | utmbuilder.com/utm-conventions | T2 | 2026-08-15
8. ZAG Interactive — Common Mistakes with UTM Tracking Codes | zaginteractive.com/insights/articles/february-2021/common-errors-in-utm-tracking | T3 | 2026-08-15
