---
practitioner: Al Iverson
role: Industry Research & Community Engagement Lead, Valimail; ex-Director of Deliverability at AWeber, Kickbox, Salesforce Marketing Cloud; runs Spam Resource
company: Valimail
type: researcher
confidence: T1
domains:
  - deliverability
  - authentication
  - DMARC
verified: 2026-08-15
sources_checked: 3
---

## Beliefs
- Email authentication (SPF/DKIM/DMARC) is table stakes — but it does NOT guarantee inbox delivery; engagement and other signals still decide placement (FACT/EMPIRICAL).
- "Authentication is the first layer of defense" — filters combine authentication, reputation, and behavior (PRINCIPLE).

## Principles
- DKIM alignment alone is sufficient for DMARC compliance in most setups — SPF alignment failures with an ESP are not a crisis (EMPIRICAL).
- Don't hack email infrastructure (registrar forwarding + Gmail "Send as"): use real email hosting with proper authentication or things will keep breaking (PRINCIPLE).
- Know the difference: SPF alignment = Return-Path/envelope domain; DKIM = signing domain; DMARC requires either to align with From (FACT).

## Frameworks
- MAGY sender compliance guide (his canonical sender-compliance checklist) (FRAMEWORK).
- Authentication hierarchy: SPF or DKIM (all senders) → SPF+DKIM+DMARC (bulk senders, Gmail/Yahoo 2024 rules) (FRAMEWORK, FACT).

## Processes
- Configure real email hosting → publish SPF + DKIM → publish DMARC record (enforcement can start at none) → monitor via Postmaster Tools → investigate placement issues via headers (PROCESS).

## Heuristics
- SPF alignment failure + DKIM aligned = fine, don't panic (HEURISTIC).
- "Everything passed but it's still in spam" — authentication is not the only signal; user engagement and similarity-to-spam matter (HEURISTIC).
- When something breaks after a registrar/DNS migration → check whether DKIM records survived (HEURISTIC).

## Tactics
- Read full headers before blaming authentication (TACTIC).
- Monitor Gmail Postmaster Tools spam rate (threshold 0.30% for bulk) (TACTIC).
- Use Google Workspace/Microsoft 365/Fastmail-class hosting rather than forwarding hacks (TACTIC).

## Tools
- Postmaster Tools (Gmail), Valimail (DMARC), header analyzers, Spam Resource tooling (TOOLS).

## Inputs
- Authentication records state (SPF/DKIM/DMARC), bounce/spam-rate data, headers of problem messages (INPUTS).

## Outputs
- Deliverability diagnosis, compliance guides (MAGY), educational content on Spam Resource (OUTPUTS).

## Metrics
- DMARC pass rate, spam rate (<0.3% for Gmail bulk), inbox placement, bounce rate (METRICS).

## Decision rules
- If DMARC fails and DKIM is aligned → SPF is not the problem; look elsewhere (DECISION RULE).
- If mail lands in spam despite full authentication → investigate engagement/reputation/content, not auth config (DECISION RULE).
- If using forwarding hacks → migrate to real hosting before debugging anything else (DECISION RULE).

## Failure modes
- Registrar-forwarding + "Send as SMTP" hacks: DKIM records lost in migrations (Squarespace transfer case), DMARC failures, recurring breakage (FAILURE).
- Assuming authentication = delivery (FAILURE).
- Treating SPF alignment failures as emergencies when DKIM is fine (FAILURE).

## Contrarian beliefs
- The April 2025 wave of "my DMARC broke" reports was mostly self-inflicted infrastructure hacks, not provider changes (OPINION).

## Examples
- His own bank's legit notification landed in Gmail spam with SPF pass, DKIM pass, DMARC pass — proof auth alone doesn't guarantee inbox (EXAMPLE, 2025).
- Google Domains → Squarespace migration broke DKIM signing for users who relied on registrar forwarding (EXAMPLE).

## Conditions
- Any sender, any scale; most critical for bulk (5k+/day) senders subject to Gmail/Yahoo sender requirements (CONDITIONS).

## Limitations
- Focus is technical/infrastructure; doesn't cover creative/messaging strategy; some guidance is US/Gmail-centric (LIMITATIONS).

## Sources
1. SPF Alignment Failures: Don't Panic! | https://www.spamresource.com/2025/02/spf-alignment-failures-dont-panic.html | blog | 1 | 2026-08-15
2. Email Hosting Hacks: No longer working? | https://www.spamresource.com/2025/05/email-hosting-hacks-no-longer-working.html | blog | 1 | 2026-08-15
3. "Everything passed, why spam?" (LinkedIn) | https://www.linkedin.com/posts/aliverson_email-authentication-deliverability-activity-7329918587547144192-kW9S | social post | 1 | 2026-08-15
4. Gmail Email sender guidelines (authoritative baseline) | https://support.google.com/mail/answer/81126 | docs | 2 | 2026-08-15
