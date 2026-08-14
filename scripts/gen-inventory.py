import os, re, glob, json
from collections import Counter

DISC = {
 'growth-strategy':'strategy','gtm-plan':'strategy','market-sizing':'strategy','market-map':'strategy',
 'market-forecasting':'strategy','demand-analysis':'strategy','industry-category-analysis':'strategy',
 'category-design':'strategy','pricing-packaging-strategy':'strategy','positioning-framework':'positioning',
 'benchmark-frameworks':'analytics','metrics-framework':'analytics',
 'customer-research':'research','customer-interviews':'research','survey-design':'research',
 'reddit-research':'research','review-mining':'research','social-listening':'research',
 'support-ticket-mining':'research','call-transcript-analysis':'research','personas':'research',
 'icp-builder':'research','win-loss-analysis':'research','account-intelligence':'research',
 'intent-signals':'research','technology-analysis':'research','trend-detection':'research',
 'competitor-audit':'competitive','competitor-battlecards':'competitive','pricing-intelligence':'competitive',
 'ad-library-research':'competitive',
 'keyword-research':'seo','seo-audit':'seo','technical-seo':'seo','link-building':'seo',
 'programmatic-seo':'seo','local-seo':'seo','serp-analysis':'seo','international-seo':'seo',
 'entity-optimization':'aeo','ai-search-audit':'aeo','ai-citation-acquisition':'aeo','ai-answer-tracking':'aeo',
 'social-strategy':'social','linkedin-content':'social','x-twitter-growth':'social','reddit-engagement':'social',
 'youtube-strategy':'social','instagram-tiktok-organic':'social','pinterest-threads':'social','community-strategy':'social',
 'lifecycle-sequences':'email','newsletter-operations':'email','email-deliverability':'email','content-calendar':'email',
 'cold-email-sequence':'outbound','lead-sourcing-enrichment':'outbound','multichannel-outbound':'outbound',
 'reply-classification':'outbound','domain-reputation-ops':'outbound',
 'pr-strategy':'pr','press-pitching':'pr','press-release':'pr','newsjacking':'pr',
 'product-launch-playbook':'pr','product-hunt-launch':'pr','podcast-appearances':'pr','events-webinars':'pr',
 'partnership-strategy':'partnerships','co-marketing':'partnerships','affiliate-program':'partnerships',
 'referral-program':'partnerships','influencer-marketing':'partnerships','creator-outreach':'partnerships',
 'ambassador-program':'partnerships',
 'conversion-copywriting':'copy','landing-page-copy':'copy','email-copy':'copy','ad-copy':'copy',
 'video-scripts':'copy','objection-handling':'copy','sales-deck':'copy','brand-voice':'copy',
 'messaging-hierarchy':'copy','value-proposition':'copy','customer-language-bank':'copy','offer-design':'copy',
 'localization':'copy','thought-leadership':'copy','content-repurposing':'copy','content-strategy':'copy',
 'case-study-builder':'copy',
 'paid-strategy':'paid','media-planning':'paid','performance-reporting':'paid','retail-media':'paid',
 'marketplace-expansion':'paid','shopify-marketing-audit':'paid','shopping-feeds':'paid',
 'meta-ads':'paid','google-ads':'paid','linkedin-ads':'paid','tiktok-ads':'paid','amazon-ads':'paid',
 'reddit-ads':'paid','microsoft-ads':'paid','x-ads':'paid','apple-search-ads':'paid','pinterest-ads':'paid',
 'snapchat-ads':'paid','quora-ads':'paid','spotify-ads':'paid','native-ads':'paid','programmatic-ctv':'paid',
 'podcast-newsletter-ads':'paid',
 'ad-creative-generator':'creative','hook-frameworks':'creative','creative-testing':'creative','ugc-advertising':'creative',
 'cro-audit':'cro','landing-page-optimization':'cro','signup-flow':'cro','checkout-optimization':'cro',
 'forms-microcopy':'cro','ab-testing':'cro','experiment-prioritization':'cro','experimentation-program':'cro',
 'funnel-analysis':'cro',
 'analytics-setup':'analytics','product-analytics':'analytics','dashboard-design':'analytics',
 'utm-governance':'analytics','attribution-model-selection':'analytics','mmm-incrementality':'analytics',
 'crm-pipeline-attribution':'analytics','crm-lead-ops':'analytics','workflow-builder':'analytics',
}

markers = {
  'gate': r'(?i)\bgate\b|success criteria',
  'failure': r'(?i)failure|pitfall|mistake',
  'decision': r'(?i)decision rule|if.*then.*(?:because|unless)|choose (?:when|between)',
  'metrics': r'(?i)\bmetrics?\b|KPI|\bCAC\b|\bROAS\b',
  'examples': r'(?i)example|case study|sample',
  'sources': r'(?i)source|reference|cite\b',
  'scoring': r'(?i)rubric|score',
  'priority': r'(?i)priorit|impact.*effort|ICE|RICE|PIE|PXL',
}

rows = []
for repo in sorted(os.listdir('.')):
    if not repo.startswith('marketing-'): continue
    for skill in sorted(glob.glob(os.path.join(repo, '*', 'SKILL.md'))):
        text = open(skill, encoding='utf-8', errors='replace').read()
        name = os.path.basename(os.path.dirname(skill))
        words = len(text.split())
        h = {k: bool(re.search(p, text)) for k, p in markers.items()}
        score = 1 + sum([h['metrics'], h['decision'], h['examples'], h['scoring'], h['priority']])
        mat = 'M1-structure' if score <= 2 else ('M2-operational' if score <= 4 else 'M3-decision')
        rows.append({'repo': repo.replace('marketing-',''), 'skill': name,
                     'disc': DISC.get(name, 'other'), 'words': words, 'score': score,
                     'mat': mat, 'no_metrics': not h['metrics'], 'no_decision': not h['decision'],
                     'no_sources': not h['sources']})

with open('/tmp/inventory.json','w') as f:
    json.dump(rows, f, indent=1)

print("Maturity:", dict(Counter(r['mat'] for r in rows)))
print("Disciplines:", dict(sorted(Counter(r['disc'] for r in rows).items())))
print("No decision rules:", sum(1 for r in rows if r['no_decision']), "/137")
print("No metrics:", sum(1 for r in rows if r['no_metrics']))
print("No sources:", sum(1 for r in rows if r['no_sources']))
