---
practitioner: Laura Atkins
role: Deliverability consultant; co-founder, Word to the Wise; co-founder Women of Email; former chair, IETF DKIM Working Group (works on DKIM2)
company: Word to the Wise
type: researcher
confidence: T1
domains:
  - deliverability
  - reputation
  - authentication
verified: 2026-08-15
sources_checked: 2
---

## Beliefs
- "Authentication establishes identity; reputation is built through recipient behavior" — deliverability is about the end user, not technical checks (FRAMEWORK).
- Deliverability is the conscience of the company: the job that tells marketing "no" — too much volume to the wrong people has consequences (OPINION/PRINCIPLE).
- Filters exist to stop spam after it's sent; deliverability professionals stop spam before it's sent (PRINCIPLE).

## Principles
- The email belongs to the subscriber — their mailbox, their decision (PRINCIPLE).
- Reputation only exists on top of verified identity; authentication is the baseline, not the advantage (PRINCIPLE).
- Scaling irrelevant communication doesn't solve problems — it creates more irrelevant communication (PRINCIPLE).

## Frameworks
- Identity → reputation → user-specific filtering: IP reputation (early days) → authenticated domain identity → per-recipient behavioral placement (FRAMEWORK).
- Recipient-first philosophy: senders succeed when they send email people genuinely want (FRAMEWORK).

## Processes
- Authenticate (SPF/DKIM/DMARC) → build reputation through consistent positive recipient behavior → monitor engagement feedback per provider → adjust volume/audience based on that feedback (PROCESS).

## Heuristics
- Traditional inbox-placement test tools are becoming unreliable — test mailboxes don't behave like real people; she's seen tools report 100% inbox or 100% spam while campaigns got 30% opens (EMPIRICAL).
- Mailbox providers increasingly personalize placement per user: same campaign can hit one person's inbox and another's spam (EMPIRICAL).
- Google observes more behavior via its own apps than via Apple Mail — placement weighting differs (EMPIRICAL).

## Tactics
- Watch for backscatter (bounces from spoofed sends) as a signal (TACTIC).
- Treat Gmail/Yahoo 2024 sender requirements as a win for deliverability practice — they formalized existing best practices with consequences (OPINION).

## Tools
- Authentication tooling (DKIM/DMARC), M3AAWG/IETF standards work, blocklist monitoring (TOOLS).

## Inputs
- Engagement behavior per recipient, provider mix of audience, complaint/blocklist data, authentication status (INPUTS).

## Outputs
- Deliverability consulting, standards contributions (DKIM2), education via Word to the Wise (OUTPUTS).

## Metrics
- Recipient engagement (opens/clicks/forwards), complaints, blocklist status, inbox placement, per-provider delivery (METRICS).

## Decision rules
- If recipients don't want the mail → no technical fix saves you; change audience or content (DECISION RULE).
- If inbox testing tools disagree with real engagement → trust real campaign metrics, not seed tests (DECISION RULE).
- If using cold-email infrastructure/warm-up automation at scale → expect providers to potentially treat it as negative trust signal (HYPOTHESIS/OPINION — her 2026 forecast) (DECISION RULE).

## Failure modes
- Not paying attention to recipient feedback (the biggest reason senders fail) (FAILURE).
- Sending to bought/unwanted lists — "the people get to block and report; at many providers these drive brand reputation" (FAILURE).
- Relying on inbox-placement seed tests as truth (FAILURE).

## Contrarian beliefs
- The future belongs to senders whose emails people want, not senders with perfect auth configs; authentication may even become a "red herring" for practitioners over-focusing on it (OPINION).
- Predicts mailbox providers may eventually treat cold-email infrastructure/warm-up tools as negative trust signals (HYPOTHESIS).

## Examples
- Client case: inbox-placement tools reported 100% spam while campaigns generated 30% opens — seed tools misread reality (EXAMPLE).
- Gmail/Yahoo Feb 2024 sender rules: mostly formalized existing best practices; gave deliverability teams enforcement leverage ("we will block your mail") (EXAMPLE).

## Conditions
- Any sender scale; reputation-first thinking matters most for ongoing programs with long-lived domains (CONDITIONS).

## Limitations
- Reputation signals are provider-specific and opaque; her forward-looking claims (cold-email infra as negative signal) are predictions, not established fact (LIMITATIONS).

## Sources
1. The future of deliverability with Laura Atkins (Stripo interview) | https://stripo.email/blog/the-future-of-deliverability-with-laura-atkins-why-reputation-will-matter-more-than-authentication/ | interview | 1 | 2026-08-15
2. Why Deliverability Matters | https://www.wordtothewise.com/2024/06/why-deliverability-matters/ | blog | 1 | 2026-08-15
