# OUTBOUND / COLD EMAIL — Discipline Synthesis

Practitioners: Alex Berman (Experiment 27), Will Allred (Lavender), Steli Efti (Close), Morgan J. Ingram (AMP Social/ex-Cognism), Aaron Ross (Predictable Revenue), Dan Tyre (HubSpot). Benchmarks: Mailshake State of Cold Email 2025; Gmail sender guidelines 2024.

## Consensus
- **Offer/targeting > copy, in that causal order.** Berman (offer-first, "the offer is the 80/20"), Allred (targeting hypothesis before 1:1), Ross (JTBD targeting + message experiments), and the Mailshake survey (personalization + targeting = clearest lever) converge. Rule: fix offer → fix targeting → fix copy → scale infrastructure (Berman).
- **Reply rate is the north metric; opens are directional only.** Mailshake 2025: 1–4% reply is the norm, only 16% of senders exceed 5%; Berman: opens-up-replies-flat means the offer is broken; Allred optimizes total replies + pipeline.
- **Deliverability discipline is mandatory infrastructure, not optimization:** consistent daily volume caps (Berman: 15–30/mailbox/day; never Monday-bursts), avoid >2 follow-ups within a week, warm domains, monitor daily. Gmail's Feb 2024 rules (SPF or DKIM all senders; SPF+DKIM+DMARC + <0.3% spam rate + one-click unsubscribe for >5k/day) made this regulatory, not optional.
- **Multichannel beats single-channel email:** Ingram (LI + email + phone + video cadences), Tyre (4 calls + intermittent email + video), Ross ("pick up the damn phone"). Email alone is the weakest channel.
- **Persistence with structure:** 5–8+ touches (Efti: 5–8 attempts cold, follow up forever when warm; Ingram: 6–11 touches over 3–4 weeks) — but relevance per touch is the constraint (Ingram's own counterpoint: fit > frequency).
- **Human, short, specific:** 50–60 word emails (Berman), "like a friend" (Berman/Efti), specific proof/deliverables beat category descriptions (Berman, Efti's "specific value proposition", Tyre's proof-over-interest).

## Disagreement
1. **Personalization depth: 1:1 human research vs offer-first at scale.** Allred: personalization at scale is an oxymoron; real 1:1 (trigger + context) drives 682% more replies / 1900% more pipeline (vendor data). Berman: either genuinely personalize OR lead offer-first; the fake middle ground dies; a clean offer-first email beats a fake-personal one 9/10. *Resolution condition:* research capacity per prospect (Allred works with trained sellers on mid-market/enterprise; Berman's method works at volume with thin per-prospect context).
2. **Open rate value post-MPP.** Efti says spend 80% of time on subject lines (30–40% opens = 60% never see body). Chad White (email side) says MPP rewrote this — optimize clicks. Outbound reply-based sending is less MPP-affected than marketing sends; both can be true by channel.
3. **Cadence length.** Ingram: 6–11 touches enough ("most teams have 11–15"); Efti: up to 8 cold; Berman: >2 follow-ups within a week trains spam filters; Taylor (Berman-cited): one email to TAM every 60 days. *Resolution:* cadence length trades against deliverability risk and message quality; short-and-relevant beats long-and-spammy in 2025+.
4. **Cold calling's role.** Ross/Tyre/Ingram: phone is essential. Berman (implicitly) and modern cold-email stack: email-first at scale. *Resolution:* market-specific — Tyre's SMB/partner context has reachable humans; enterprise-scale email-first needs no phone.
5. **What "stopped working":** Ross: email reply-to-call decayed ~7% → ~0.7% (2011→2019); Mailshake 2025: 69% of senders report YoY decline; Berman: copy bar unchanged, systems bar risen. Some claim "cold email is dying," others (Berman) that the channel is fine and systems are broken.

## Conditions
- **Offer-first + infrastructure discipline** is correct when: B2B service/agency with a definable low-commitment deliverable; need volume (50+ emails/day); thin per-prospect research capacity.
- **1:1 human personalization** is correct when: seller has research time (trained SDR/AE), mid-market/enterprise accounts with rich context, 5–50 emails/day per seller.
- **Multichannel cadence** is correct when: prospect universe is LinkedIn-reachable, SMB/mid-market, phone numbers available.
- **Validation-first experimentation** (Ross Outbound Validation) is correct when: org has measurement infrastructure and can run 20 experiments/month; wrong for a 2-person startup without tracking.
- **Warm-calling/phone-first** (Tyre) is correct for SMB/partner channels with reachable decision-makers; wrong for 10k+ prospect universes.

## Evidence evaluation
- **EMPIRICAL (survey):** Mailshake 2025 (n≈1,000 senders, self-reported): 1–4% reply norm; 16% >5%; 69% YoY decline; personalized-every-email sends report better replies.
- **EMPIRICAL (vendor, self-reported — treat cautiously):** Allred/Lavender: 12% reply benchmark, A-emails 20%+, 1:1 emails 682% more replies/1900% pipeline; Fluint business-case personalization 6x close.
- **EMPIRICAL (practitioner-stated, unverified):** Tyre's video conversion stats (1–2% → 30–40%); Ross's 7%→0.7% decay; Berman's 1-in-400 booking rate; Ingram's 20% response cadence.
- **FACT (regulatory):** Gmail/Yahoo bulk-sender rules Feb 2024 — SPF or DKIM (all), SPF+DKIM+DMARC, PTR, TLS, <0.3% spam rate, one-click unsubscribe (bulk).
- **HEURISTIC (high convergence):** offer before copy; short emails; consistent volume; reply rate north; relevance per touch.

## Outliers
- **Berman's 60-day re-contact cycle** (one email to TAM every 60 days, 9-figure volumes) — inverse of the "more touches" consensus; worth testing for deliverability-heavy plays.
- **Allred's "personalization at scale is an oxymoron"** — directly opposes the AI-personalization-at-scale industry; bet on human craft as the durable differentiator.
- **Laura Atkins' prediction** (email side, but outbound-relevant): mailbox providers may eventually treat cold-email infrastructure and automated warm-up tools as negative trust signals — would upend the tooling layer.
- **Ingram's question-first opener** (spark question > value statement) — contrarian to value-prop-first copy doctrine.

## Failure knowledge
- **Bought/rented lists:** never; list quality > copy (all practitioners; Gmail rules make it worse).
- **Volume spikes:** "1,000 emails Monday, none Tuesday" → near-certain spam (Berman); Gmail docs: increase volume slowly, consistent rate, no sudden doubling.
- **Fake personalization:** "Curious to know…", pretending to know the business, template-personalized inserts — deleted instantly (Berman, Efti, Allred).
- **Pitching a service instead of an offer** (Berman: zero-response campaigns until entry-point offer built).
- **Over-follow-up:** >2 follow-ups within a week trains spam filters (Berman); irrelevant 11-touch stacks = interrupting 11x instead of once (Ingram).
- **Copying frameworks without the system:** most Predictable Revenue copies failed (Ross) — bolt-on cadences without architecture, data, and classification don't work.
- **Ignoring measurement:** 7% of senders don't track replies at all (Mailshake); Ross: dashboards usually wrong — fix tracking before optimizing.
- **Not classifying replies:** replies that aren't "book a meeting" (competitor mentions, referrals, "talk to X") are lost value (Ross Outbound Validation; Mailshake expert quote).

## Collision Method sketch — Outbound Discipline
- **Objective:** predictable reply → conversation → meeting pipeline from cold contacts, with positive sender reputation preserved.
- **Prerequisites:** verified deliverability stack (SPF+DKIM+DMARC, PTR, <0.3% spam rate, warm domain with consistent volume); reply tracking; reply classification taxonomy.
- **Inputs:** meetings-needed target (backwards math: meetings ÷ reply rate 1–4% ÷ open 40–60% = volume/inboxes), ICP + JTBD target map, offer statement.
- **Diagnosis (in order):** (1) Does a stranger respond to the offer with zero risk? No → rebuild offer. (2) Is targeting JTBD-precise? No → fix list. (3) Is copy ≤60 words, human, specific? No → rewrite. (4) Is deliverability clean (per-domain daily checks)? No → fix infrastructure. (5) Opens ok but replies flat → offer problem, not copy.
- **Decision tree — sequence design:** choose cadence by channel mix available: email-only (Berman-style: 2–3 touches, 60-day re-contact) vs multichannel (Ingram: 6–11 touches over 3–4 weeks, touch variety: same-thread/new-thread, voicemail/no-voicemail, video/visual). Kill criteria: <0.5–1% reply on a validated message after 200–300 sends → kill message, change offer or list; domain flagged → replace domain; spam rate rising → halt, diagnose.
- **Methodology:** offer-first copy; personalization decision: genuine 1:1 if research capacity ≥ ~2–3 min/prospect, else offer-first with honest specificity; layer personalization progressively (Ingram); escalate channels (email → LI → phone → video); end with breakup/goodbye touch; classify every reply (positive/negative/neutral/referral) and mine for learning (Ross).
- **Execution:** consistent daily caps (15–30/mailbox/day), warm before scaling, validate on small subset before broad scale (Berman, Ross).
- **Metrics:** reply rate (north), positive reply rate, meetings booked per 1,000 sends, deliverability/inbox rate, spam complaints (<0.3%), bounce rate, per-touch response contribution.
- **Stopping rules:** kill message/list/sequence at predefined thresholds; stop following up after explicit no (Efti: yes/no are answers, maybe is death); cold: max 5–8 touches unless warm.
- **Failure modes:** bought lists, volume spikes, fake personalization, service-pitch-vs-offer, over-follow-up, unmeasured sends, unclassified replies, bolt-on copying.
- **Conditions:** B2B contexts with identifiable JTBD; needs domain + list + tracking infrastructure; method scales from solo (small caps, one domain) to agency (multi-domain rotation).
- **Limitations:** reply-based metrics don't capture call-driven or channel-shift value; vendor benchmarks self-reported; Gmail AI-inbox brief-style filtering (Berman 2026) may reduce cold-email visibility regardless of technique.
- **Confidence:** T2 overall — offer-first, reply-rate-north, deliverability-discipline are T1-convergent (4+ independent practitioners + regulatory facts); specific rates (12%, 20%, 1-in-400) are T3.
- **Key sources:** alexberman.com (3 posts, 2026); Lavender LinkedIn data (2024–25); Mailshake State of Cold Email 2025; gtmnow.com Ross retrospective; predictablerevenue.com Outbound Validation; Gmail sender guidelines.
