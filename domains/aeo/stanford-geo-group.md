---
practitioner: Stanford GEO Research Group (Aggarwal et al.)
role: Academic researchers (Princeton + IIT Delhi); authors of the GEO paper
company: Princeton University / IIT Delhi
type: researcher
confidence: T1
domains:
  - ai-search / GEO (research foundation)
verified: 2026-08-15
sources_checked: 2
---

## Beliefs
- Generative engines (GEs) are replacing traditional search as a primary information layer; content creators have "little to no control over when and how their content is displayed" in black-box GEs — the creator economy needs optimization methods. (GEO paper, KDD 2024, arXiv 2311.09735) — FRAMEWORK
- Content visibility in GE answers can be improved via a "flexible black-box optimization framework" with user-defined visibility metrics. — FRAMEWORK
- Optimization methods are domain-sensitive: "efficacy of these strategies varies across domains, underscoring the need for domain-specific optimization methods." — EMPIRICAL

## Principles
- Define visibility formally (position-adjusted word count; subjective impression) before optimizing.
- Minimal-change content interventions can produce large visibility gains (quotes, stats, citations).
- Evaluate on real engines (Perplexity) as well as simulated ones.

## Frameworks
- GEO (Generative Engine Optimization): the named paradigm + GEO-bench (10k queries, diverse domains, with source corpora).
- Visibility metrics: Position-Adjusted Word Count (citation word count weighted by position) and Subjective Impression (multi-factor quality impression).
- Follow-up (GEO-Bench, arXiv 2605.29107, 2026): unified benchmark of GEO manipulation ATTACKS — black-box prompt-based (TAP, Zero-Shot), white-box gradient-based (STS, RAF, StealthRank), and ten white-hat C-SEO strategies — scored on effectiveness (NRG, Success@α, Promote@α) and stealth (keyword violation rate, perplexity ratio).

## Processes
- (1) Curate query set; (2) run baseline GE answers; (3) apply content intervention (e.g., add statistics/quotes/citations); (4) re-run and compare visibility metrics vs baseline; (5) validate on a real engine.
- GEO-bench protocol: five datasets, fixed open-weight ranker (Llama-3.1-8B), joint effectiveness+stealth scoring.

## Heuristics
- Adding relevant statistics, credible quotes, and citations to existing content boosts visibility 30-40% (position-adjusted word count) and 15-30% (subjective impression) vs baseline. — EMPIRICAL (controlled, lab)
- On Perplexity: quotation addition performed best on position-adjusted word count; visibility improvements up to 37% on real-engine tests. — EMPIRICAL
- Effectiveness and stealth trade off across adversarial attacks; white-hat content rewriting can match gradient attacks on rank promotion while evading keyword- and perplexity-based detection on some domains. — EMPIRICAL (2026 benchmark)

## Tactics
- "Cite Sources": include citations from reliable sources in content.
- "Quotation Addition": embed credible quotes.
- "Statistics Addition": add relevant statistics.
- (Benchmark-scoped) adversarial variants: prompt-injection-style rewriting, token appendices, retrieval-aware rewriting — documented as manipulation risks, NOT recommended practice.

## Tools
- GEO-bench code/data (generative-engines.com/GEO, github.com/glad-lab/geobench); Perplexity as real-engine testbed.

## Inputs
- Query benchmark, candidate source corpora, GE outputs, metric definitions.

## Outputs
- Peer-reviewed GEO paper (KDD 2024), GEO-bench benchmark, follow-up manipulation-detection work, code/data.

## Metrics
- Visibility: position-adjusted word count, subjective impression; attack benchmarks: NRG, Success@α, Promote@α, keyword violation rate, perplexity ratio.

## Decision rules
- If content lacks data/quotes/external citations → add them before any structural rewrite (cheapest, highest measured lift).
- If optimizing for Perplexity specifically → quotation addition is the strongest measured lever.
- If a domain is niche → don't copy generic GEO tactics; evaluate per-domain (efficacy varies by domain).

## Failure modes
- Treating lab results as guarantees: GEO-bench is a simulated/benchmark environment; real engines change fast.
- Ignoring detectability: manipulation-style GEO (gradient/prompt attacks) trades off with stealth and is the subject of active detection research — gaming is a documented risk, not a stable tactic.
- Domain-blind optimization: strategies that work for product recommendations may fail for Q&A.

## Contrarian beliefs
- Visibility is optimizable via content alone (vs. Law's "it's just SEO" — the group's framing is optimization-agnostic and content-intervention-focused; they don't argue against SEO, they formalize a parallel black-box optimization layer).
- GEO manipulation is a research-grade threat: black-box content rewriting can evade current detection — the field needs detection standards (their 2026 benchmark).

## Examples
- Up to 40% visibility boost on GEO-bench; up to 37% on Perplexity; the C-SEO Bench prior work evaluating ten white-hat strategies across six domains.

## Conditions
- Lab/benchmark setting with controlled queries; transfer to production engines partially validated (Perplexity only).
- Applies to informational + product-recommendation content; weak evidence for local/transactional verticals.

## Limitations
- Simulated engines for most evaluations; small real-engine surface (Perplexity).
- "Up to 40%" is best-case; average/domain-level gains vary — don't plan budgets on the ceiling.
- Manipulation-attack results document risk, not a playbook for safe practice.

## Sources
1. GEO: Generative Engine Optimization (KDD 2024) | https://arxiv.org/html/2311.09735v2 | paper | 1 | 2026-08-15
2. GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization | https://arxiv.org/html/2605.29107v2 | paper | 1 | 2026-08-15
