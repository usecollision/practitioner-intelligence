# SKILL GAP ANALYSIS — Outbound & Email (Wave 3, 2026-08-15)

Research: `syntheses/outbound.md`, `syntheses/email.md` · Domains: `domains/outbound/*`, `domains/email/*` · Status: **implemented**

## Changes

| Skill | Change |
|---|---|
| cold-email-sequence | +Offer>targeting>copy>infrastructure causal order (Berman), reply-rate north metric (1-4% norm, Mailshake 2025), opens-up-replies-flat=offer diagnosis, 15-30/mailbox/day caps, ≤2 follow-ups/week, kill criteria (<0.5-1% after 200-300 sends), fake-personalization ban, 60-day re-contact option, 7 sources |
| multichannel-outbound | +Multichannel-beats-email, fit>frequency, 6-11 touch variety norms, explicit-no stop rule, small-subset validation at scale, 4 sources |
| lifecycle-sequences | +Lifecycle-beats-campaigns, behavior-branching (Geisler), winback→re-permission→prune, MPP open-rate conditions, onboarding-as-churn-reduction, 5 sources |
| email-deliverability | +Auth-is-identity-not-delivery (Iverson), Gmail Feb-2024 mandated baseline, seed-tool limits (Atkins), recipient-first philosophy, migration DMARC wave, warm-up-tools risk hypothesis (T3), 4 sources |

## Key encoded knowledge

1. **The offer is the 80/20** — the #1 convergence in outbound; copy rewrites on a broken offer are wasted.
2. **Reply rate is the north metric**; opens are directional; 1-4% is the norm — kill criteria are now numeric.
3. **Gmail 2024 made deliverability regulatory** — SPF/DKIM/DMARC, <0.3% spam, one-click unsubscribe for bulk.
4. **Lifecycle over campaigns + behavior branching** — "don't serve dessert to someone still on the appetizer" (Geisler).
5. **Auth passing ≠ inbox** — reputation from recipient behavior (Iverson's bank-notification case).

## Validation

- [x] 4 skills patched per M4 contract; pushed to marketing-channels @ main
