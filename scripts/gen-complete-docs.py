"""Assemble the complete-* aggregate documents from syntheses/ and domains/."""
import os, re, glob, json
from collections import defaultdict

ROOT = 'C:/Users/rishh/workspace/practitioner-intelligence'

def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()

syntheses = sorted(glob.glob(os.path.join(ROOT, 'syntheses', '*.md')))
domains = sorted(glob.glob(os.path.join(ROOT, 'domains', '*', '*.md')))

def section(text, headers):
    """Extract section(s) by header regex; return list of (header, body)."""
    out = []
    for h in headers:
        m = re.search(rf'^##\s+{h}\s*$.*?(?=^##|\Z)', text, re.M | re.S)
        if m:
            body = m.group(0)
            out.append((h, body))
    return out

# 1. CONSENSUS MAP
lines = ['# COMPLETE CONSENSUS MAP — where the field agrees', '',
         'Assembled 2026-08-15 from 24 discipline syntheses. Each section names the practitioners and claim confidence.',
         '']
for s in syntheses:
    name = os.path.basename(s).replace('.md', '')
    for h, body in section(read(s), ['Consensus']):
        lines.append(f'## {name} — Consensus')
        lines.append(body)
        lines.append('')
open(os.path.join(ROOT, 'complete-consensus-map.md'), 'w', encoding='utf-8').write('\n'.join(lines))

# 2. CONTRADICTION MAP
lines = ['# COMPLETE CONTRADICTION MAP — where experts disagree, with conditions', '',
         'Assembled 2026-08-15. Every disagreement carries the conditions under which each side is correct.',
         '']
for s in syntheses:
    name = os.path.basename(s).replace('.md', '')
    for h, body in section(read(s), ['Disagreement', r'Disagreements? \(with conditions\)']):
        lines.append(f'## {name} — Disagreement')
        lines.append(body)
        lines.append('')
open(os.path.join(ROOT, 'complete-contradiction-map.md'), 'w', encoding='utf-8').write('\n'.join(lines))

# 3. FAILURE KNOWLEDGE BASE
lines = ['# COMPLETE FAILURE KNOWLEDGE BASE — what repeatedly doesn\'t work', '',
         'Assembled 2026-08-15 from all syntheses. Negative knowledge is first-class: each item carries sources and confidence.',
         '']
for s in syntheses:
    name = os.path.basename(s).replace('.md', '')
    for h, body in section(read(s), ['Failure knowledge', r'Failure Knowledge']):
        lines.append(f'## {name}')
        lines.append(body)
        lines.append('')
open(os.path.join(ROOT, 'complete-failure-knowledge-base.md'), 'w', encoding='utf-8').write('\n'.join(lines))

# 4. EXPERT MAP
lines = ['# COMPLETE EXPERT MAP — every practitioner in the intelligence layer', '',
         'Assembled 2026-08-15 from domain dossiers. Type + confidence per expert; confidence = verification tier at dossier time.',
         '']
experts = []
for d in domains:
    rel = os.path.relpath(d, ROOT)
    txt = read(d)
    disc = os.path.basename(os.path.dirname(d))
    m = re.search(r'^---\s*\n(.*?)\n---', txt, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()
    name = fm.get('practitioner', os.path.basename(d).replace('.md', '').replace('-', ' ').title())
    experts.append((disc, name, fm.get('role', ''), fm.get('type', ''), fm.get('confidence', 'T2')))
by_disc = defaultdict(list)
for disc, n, r, t, c in experts:
    by_disc[disc].append((n, r, t, c))
for disc in sorted(by_disc):
    lines.append(f'## {disc} ({len(by_disc[disc])})')
    for n, r, t, c in sorted(by_disc[disc]):
        lines.append(f'- **{n}** — {r} [{t} | {c}]')
    lines.append('')
lines.append(f'Total experts indexed: {len(experts)}')
open(os.path.join(ROOT, 'complete-expert-map.md'), 'w', encoding='utf-8').write('\n'.join(lines))

# 5. SOURCE INDEX
lines = ['# COMPLETE SOURCE INDEX — every cited source', '',
         'Assembled 2026-08-15 from domain dossiers and skill Sources sections.', '']
src_lines = set()
for d in domains:
    txt = read(d)
    for m in re.finditer(r'^\d+\.\s+(.+)$', txt, re.M):
        src_lines.add(m.group(1).strip())
for s in sorted(src_lines):
    lines.append(f'- {s}')
lines.append('')
lines.append(f'Unique source entries: {len(src_lines)}')
open(os.path.join(ROOT, 'complete-source-index.md'), 'w', encoding='utf-8').write('\n'.join(lines))

# 6. METHODOLOGY LIBRARY (Collision Method sketches)
lines = ['# COMPLETE METHODOLOGY LIBRARY — Collision Methods', '',
         'Assembled 2026-08-15 from the Collision Method sketches in every synthesis. These are the synthesized operating procedures of the Marketing OS.',
         '']
for s in syntheses:
    name = os.path.basename(s).replace('.md', '')
    txt = read(s)
    m = re.search(r'## Collision Method sketch.*?(?=^##|\Z)', txt, re.M | re.S)
    if m:
        lines.append(f'## {name}')
        lines.append(m.group(0).strip())
        lines.append('')
open(os.path.join(ROOT, 'complete-methodology-library.md'), 'w', encoding='utf-8').write('\n'.join(lines))

print(f"Syntheses: {len(syntheses)} | Domains: {len(domains)} | Experts: {len(experts)} | Sources: {len(src_lines)}")
for f in ['complete-consensus-map.md', 'complete-contradiction-map.md', 'complete-failure-knowledge-base.md',
          'complete-expert-map.md', 'complete-source-index.md', 'complete-methodology-library.md']:
    p = os.path.join(ROOT, f)
    print(f"{f}: {os.path.getsize(p)//1024} KB")
