---
practitioner: Baymard Institute panel (checkout research)
role: UX research institute (e-commerce checkout, 14 years, 54,000+ hours, 150+ site audits, 11,777+ survey participants)
company: Baymard Institute (Christian Holst, research director/co-founder)
type: researcher
confidence: T1 (institute's own published findings) / T2 (secondary citations)
domains:
  - cro
  - checkout
verified: 2026-08-15
sources_checked: 9
---
# Panel — Baymard Institute (checkout)

## Experts found
- **Baymard Institute** (Christian Holst et al.) — the primary authority on checkout usability. Method: 1:1 moderated think-aloud testing (272 sessions in latest study; 1,202 cumulative), eye-tracking (32 participants), checkout benchmarking (850+ steps / 7,800+ weighted parameters), 9 quantitative surveys (11,777 participants), audits of 150+ leading e-commerce sites. 134 design guidelines, 718-page report. T1 for its own published articles.

## Beliefs
- Checkout design is frequently the **sole cause** of abandonment for shoppers who already added to cart: "the shopper had intent. The checkout destroyed it." Users leave in anger (friction) or because they cannot complete a field (no path forward). Both are recoverable with cheap design changes (EMPIRICAL, T1).
- Average cart abandonment ≈ 70.2% (average of 50 studies). ~42% of abandoners say they were "browsing, not ready to buy" — a largely unavoidable share; do not spend optimization budget there (EMPIRICAL, T1).
- The average checkout displays 23.48 form elements (14.88 fields) vs an achievable ~12 elements (7 fields, 2 checkboxes, 2 dropdowns, 1 radio) — a 20–60% reduction is typically possible (EMPIRICAL, T1).
- Perceived complexity beats actual complexity: a 15-field form split across 3 logical steps outperforms a 10-field single page by 11–14% completion (EMPIRICAL, T1).
- One-page vs multi-step: their A/B testing found no significant difference; flow format should be chosen by context (product complexity, AOV, mobile share), not dogma (EMPIRICAL, T1).
- Most high-impact fixes are page layout, form features, and microcopy — "don't require advanced technical implementation or deep pockets" (FRAMEWORK, T1).

## Quantified levers (Baymard consumer research 2024)
- 48% of abandoners: extra costs (shipping/taxes/fees) higher than expected — #1 cause → show costs early.
- 26%: forced account creation — #2 cause → guest checkout default; delayed account creation (offer account after purchase).
- ~1 in 5: "too long / complicated checkout process."
- 16 → 8 form fields ≈ 25–35% conversion increase (Baymard's 16-fields-to-8 article).
- Average large-scale e-commerce site: 32 unique improvements available ≈ +35% conversion potential; 50-site benchmark: 39 improvement areas per site.
- Mobile abandonment ~80% vs desktop ~66% (Dynamic Yield data cited across Baymard roundups) — a design problem, not a traffic problem.

## Failure modes
- Optimizing toward the 42% "just browsing" share (unfixable in checkout).
- Removing fields that fulfillment/shipping genuinely needs — cut fields with a consumer, not a scalpel.
- Hiding shipping cost until the payment step (feeds the #1 cause).
- Forcing account creation pre-purchase (feeds the #2 cause).
- Aggressive validation that rejects legitimate input — users leave when they can't complete a field.
- Treating one-page vs multi-step as a universal truth rather than a context decision.
- Express/wallet checkout desynced from the standard flow (discounts, taxes, shipping differ).

## Decision rules
1. IF extra costs are not shown before the payment step THEN surface them earlier (Baymard, EMPIRICAL, T1).
2. IF account creation is required to purchase THEN make guest checkout the default and offer account creation post-purchase (Baymard, EMPIRICAL, T1).
3. IF default form elements >12 THEN cut 20–60% before testing anything else (Baymard, EMPIRICAL, T1).
4. IF choosing flow format THEN one-page/accordion for AOV <$150, simple products, mobile-heavy traffic; multi-step for AOV >$200, B2B/configurable, extra info collection (Baymard A/B, EMPIRICAL, T1).
5. IF a long form must stay long THEN group into 3 logical steps — perceived simplicity wins (+11–14%) (Baymard, EMPIRICAL, T1).
6. IF abandonment is attributed to "browsing" THEN exclude that segment from checkout optimization targets (Baymard, EMPIRICAL, T1).
7. IF a checkout fix is proposed THEN prefer layout/form-feature/microcopy changes first — they are the cheapest and most frequent wins (Baymard, FRAMEWORK, T1).

## Conditions / Limitations
- Works for e-commerce (B2C/DTC primarily); B2B checkout (tax IDs, PO, multi-address) shifts the multi-step case.
- Baymard's +35% potential is for large-scale sites with many improvement areas; small sites with clean checkouts have less headroom.
- Survey-based reason percentages are self-reported (participant memory), though triangulated with usability testing.
- Premium benchmark numbers behind paywall; free articles cover headline findings (T1 for what's published free).

## Sources
1. Baymard Institute — E-Commerce Cart & Checkout Usability Research (research overview) | baymard.com/research/checkout-usability | T1 | 2026-08-15
2. Christian Holst — "Reasons for Cart Abandonment – Why 70% of Do So" | baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark | T1 | 2026-08-15
3. Baymard — Checkout flow average form fields | baymard.com/blog/checkout-flow-average-form-fields | T1 | 2026-08-15
4. Baymard — Checkout optimization from 16 fields to 8 | baymard.com/blog/checkout-optimization-from-16-fields-to-8 | T1 | 2026-08-15
5. Baymard — Cart abandonment rate list | baymard.com/lists/cart-abandonment-rate | T1 | 2026-08-15
6. Baymard (commissioned by Amazon Pay) — Optimizing Checkout to Reduce Abandonment (Scribd mirror) | scribd.com/document/793114501 | T2 | 2026-08-15
7. Growth-Engines — eCommerce Checkout Optimization (secondary synthesis citing Baymard numbers) | growth-engines.com/insights/ecommerce/ecommerce-checkout-optimization | T2 | 2026-08-15
8. EasyCommerce — What Is Cart Abandonment (secondary; adds Dynamic Yield device split) | easycommerce.dev/blog/what-is-cart-abandonment | T2 | 2026-08-15
9. Monei — Cart abandonment causes/stats (42% browsing share) | monei.com/blog/cart-abandonment | T2 | 2026-08-15
