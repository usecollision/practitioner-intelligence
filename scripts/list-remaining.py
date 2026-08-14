import os, re, glob

rows = []
for repo in sorted(os.listdir('.')):
    if not repo.startswith('marketing-'): continue
    for skill in sorted(glob.glob(os.path.join(repo, '*', 'SKILL.md'))):
        t = open(skill, encoding='utf-8', errors='replace').read()
        name = os.path.basename(os.path.dirname(skill))
        words = len(t.split())
        m4 = bool(re.search(r'## Practitioner Grounding', t)) and bool(re.search(r'## Sources', t))
        has_met = bool(re.search(r'## Metrics', t))
        has_dec = bool(re.search(r'## Decision Rules', t) or re.search(r'## Practitioner Grounding.*Decision Rules', t, re.S))
        m = re.match(r'^---\s*\n(.*?)\n---', t, re.S)
        desc = ''
        if m:
            for line in m.group(1).splitlines():
                if line.startswith('description:'):
                    desc = line.split(':', 1)[1].strip()[:70]
        rows.append({'repo': repo.replace('marketing-', ''), 'skill': name, 'words': words,
                     'm4': m4, 'metrics': has_met, 'decision': has_dec, 'desc': desc})

remaining = [r for r in rows if not r['m4']]
print(f"TOTAL: {len(rows)} | M4: {sum(1 for r in rows if r['m4'])} | REMAINING: {len(remaining)}")
print(f"\n{'repo':<13}{'skill':<30}{'W':>5}  {'met':>4}{'dec':>4}  desc")
for r in sorted(remaining, key=lambda x: (x['repo'], x['skill'])):
    print(f"{r['repo']:<13}{r['skill']:<30}{r['words']:>5}  {str(r['metrics']):>4}{str(r['decision']):>4}  {r['desc']}")
