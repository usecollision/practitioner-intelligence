import os, re, glob

rows = []
for repo in sorted(os.listdir('.')):
    if not repo.startswith('marketing-'): continue
    for skill in sorted(glob.glob(os.path.join(repo, '*', 'SKILL.md'))):
        t = open(skill, encoding='utf-8', errors='replace').read()
        name = os.path.basename(os.path.dirname(skill))
        has_grounding = bool(re.search(r'## Practitioner Grounding', t))
        has_dec = bool(re.search(r'## Practitioner Grounding.*Decision Rules|## Decision Rules', t, re.S))
        has_met = bool(re.search(r'## Metrics', t))
        has_sources = bool(re.search(r'## Sources', t))
        rows.append((repo.replace('marketing-', ''), name, has_grounding, has_dec, has_met, has_sources))

m4 = [r for r in rows if all(r[2:])]
print(f"TOTAL: {len(rows)}")
print(f"M4-complete (grounding+decisions+metrics+sources): {len(m4)}")
print(f"Practitioner Grounding: {sum(1 for r in rows if r[2])}")
print(f"Decision Rules: {sum(1 for r in rows if r[3])}")
print(f"Metrics section: {sum(1 for r in rows if r[4])}")
print(f"Sources section: {sum(1 for r in rows if r[5])}")
print("\nM4-complete skills:")
for r in sorted(m4):
    print(f"  {r[0]}/{r[1]}")
print("\nWith grounding but missing metrics:")
for r in sorted([x for x in rows if x[2] and not x[4]]):
    print(f"  {r[0]}/{r[1]}")
