import json
from collections import defaultdict

rows = json.load(open('/tmp/inventory.json'))

# find 'other' skills to fix mapping
others = [r for r in rows if r['disc'] == 'other']
print("UNMAPPED:", others)

by_disc = defaultdict(list)
for r in rows:
    by_disc[r['disc']].append(r)

order = ['strategy','positioning','research','competitive','seo','aeo','copy','social','email',
         'outbound','pr','partnerships','paid','creative','cro','analytics']
names = {
 'strategy':'Strategy & GTM','positioning':'Positioning','research':'Customer & Market Research',
 'competitive':'Competitive Intelligence','seo':'SEO','aeo':'AI Search (GEO/AEO)','copy':'Copy & Messaging',
 'social':'Social','email':'Email & Lifecycle','outbound':'Outbound','pr':'PR, Launches & Events',
 'partnerships':'Partnerships & Creators','paid':'Paid Acquisition','creative':'Ad Creative',
 'cro':'CRO & Experimentation','analytics':'Analytics, Attribution & Ops','other':'Unmapped'}

def badge(r):
    marks = []
    if r['no_metrics']: marks.append('no metrics')
    if r['no_decision']: marks.append('no decision rules')
    if r['no_sources']: marks.append('no sources')
    return '; '.join(marks) if marks else '—'

out = []
out.append("# Marketing OS — Skill Inventory (Cycle 1 audit)")
out.append("")
out.append("Generated: 2026-08-14 · Source: six usecollision repos @ main (shallow clones) · Method: frontmatter + structural marker scan + manual sampling")
out.append("")
out.append("## Headline findings")
out.append("")
out.append("| Finding | Count |")
out.append("|---|---|")
out.append("| Total skills | 137 |")
out.append("| M3 — decision-grade (metrics + decision rules + examples + scoring) | 18 |")
out.append("| M2 — operational (gated workflow, failure modes, some structure) | 105 |")
out.append("| M1 — structure-only (thin substance) | 14 |")
out.append("| Skills with **no decision rules** | 130 |")
out.append("| Skills with **no metrics/KPI section** | 45 |")
out.append("| Skills with **no cited sources** | 47 |")
out.append("| Skills citing a **named practitioner** | 0 |")
out.append("")
out.append("The template (gates, rubrics, failure modes) is enforced everywhere — the gap is not structure, it is **grounding**: zero named practitioners, almost no decision rules, and a quarter of skills never say what to measure. The cro-audit and mmm-incrementality skills are the closest to M4; they still cite no sources.")
out.append("")
out.append("## Per-repo summary")
out.append("")
out.append("| Repo | Skills | M1 | M2 | M3 | No metrics | No decision |")
out.append("|---|---|---|---|---|---|---|")
repo_agg = defaultdict(lambda: [0,0,0,0,0,0])
for r in rows:
    a = repo_agg[r['repo']]
    a[0] += 1
    a[1 + ('M1-structure','M2-operational','M3-decision').index(r['mat'])] += 1
    if r['no_metrics']: a[4] += 1
    if r['no_decision']: a[5] += 1
for repo in sorted(repo_agg):
    a = repo_agg[repo]
    out.append(f"| marketing-{repo} | {a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]} |")
out.append("")
out.append("## Skills by discipline")
out.append("")
out.append("Maturity: **M1** structure-only · **M2** operational · **M3** decision-grade (has metrics + decision logic + scoring)")
out.append("")
for d in order:
    if d not in by_disc: continue
    out.append(f"### {names.get(d, d)} ({len(by_disc[d])})")
    out.append("")
    out.append("| Skill | Repo | Words | Maturity | Gaps |")
    out.append("|---|---|---|---|---|")
    for r in sorted(by_disc[d], key=lambda x: x['skill']):
        out.append(f"| {r['skill']} | {r['repo']} | {r['words']} | {r['mat']} | {badge(r)} |")
    out.append("")

with open('C:/Users/rishh/workspace/practitioner-intelligence/inventory/skill-inventory.md','w',encoding='utf-8') as f:
    f.write('\n'.join(out))
print("written", len(out), "lines")
