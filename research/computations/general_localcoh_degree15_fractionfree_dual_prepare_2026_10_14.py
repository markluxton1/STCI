#!/usr/bin/env python3
"""Serialize accepted rational pencil/row transform for new FLINT dual arithmetic."""
from general_localcoh_degree15_fractionfree_prepare_2026_10_14 import *
def qstr(a):return str(len(a))+'  '+' '.join(map(str,a))
def main():
 s=SOURCE.read_text();env={'k':RF([Q(0),Q(1)])}
 for l in s.splitlines():
  m=re.fullmatch(r'(seedDenominator\d+)=sub\(\((.*)\),K\);',l)
  if m:env[m[1]]=expr(m[2],env)
  m=re.fullmatch(r'(z\d+)=sub\(\((.*)\),K\)(?:/(seedDenominator\d+))?;',l)
  if m:
   value=expr(m[2],env);env[m[1]]=value/env[m[3]] if m[3] else value
 names=['A','B','v','w','T'];out=[];records={}
 for name in names:
  l=next(l for l in s.splitlines() if l.startswith(name+'=matrix'))
  l=re.sub(r'sub\(\((.*?)\),K\)',r'(\1)',l)
  rows=l[len(name+'=matrix{{'):-len('}};')].split('},{')
  M=[[expr(e,env) for e in row.split(',')] for row in rows]
  assert all(len(r)==len(M[0]) for r in M)
  out.append(f'{len(M)} {len(M[0])}')
  for row in M:
   for x in row:out.extend([qstr(x.n),qstr(x.d)])
  records[name]=[len(M),len(M[0])]
 text='\n'.join(out)+'\n';OUT.joinpath('dual-input.txt').write_text(text)
 r={'scope':'Accepted rational pencil and row transform serialized exactly; no inherited verifier rerun.','matrices':records,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'preparer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dual_input_sha256':hashlib.sha256(text.encode()).hexdigest()}
 OUT.joinpath('dual-input-lineage.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
if __name__=='__main__':main()
