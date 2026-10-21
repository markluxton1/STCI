#!/usr/bin/env python3
"""Independent exact specialization of the full global-sextic cubic test."""
import ast,json
from pathlib import Path
from fractions import Fraction as Q
HERE=Path(__file__).resolve().parent
old=HERE/'conditional_2_12_elimination_2026_10_20.py'
tree=ast.parse(old.read_text());stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='fmtlist' for t in n.targets))
e={'__file__':str(old),'__name__':'independent_full_cubic_family_specialization'};exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(old),'exec'),e)
ca,cm,cs,cp,var,const=(e[x] for x in ['ca','cm','cs','cp','var','const'])
h,t,eta=[var(i) for i in range(3)]
repl={1:{},2:ca(cs(t,16),cs(h,-12)),3:{},5:{},6:ca(cs(h,6),cs(t,-4)),7:{},8:t,13:cs(h,-2),14:{},15:{},16:h,21:eta}
def specialize(p):
 out={}
 for m,v in e['normalized'](p).items():
  term=const(v)
  for j in m:
   assert j in repl,j
   term=cm(term,repl[j])
  out=ca(out,term)
 return out
cubic=[specialize(p) for p in e['cubic']];cubic=[p for p in cubic if p]
# Remove duplicate scalar equations without changing the ideal.
unique=[];seen=set()
for p in cubic:
 lead=next(v for m,v in sorted(p.items()))
 p=cs(p,1/lead);key=tuple(sorted(p.items()))
 if key not in seen:seen.add(key);unique.append(p)
def show(p):
 out=[]
 for m,v in sorted(p.items(),key=lambda x:(len(x[0]),x[0])):
  mon='*'.join(('h','t','eta')[i]+('^'+str(m.count(i)) if m.count(i)!=1 else '') for i in sorted(set(m)))
  out.append('('+str(v)+')'+('*'+mon if mon else ''))
 return '+'.join(out) or '0'
stem=HERE/'conditional_2_12_full_cubic_family_audit_2026_10_21'
lines=['-- Independent full48-syzygy specialization at the exact degree-four root family.','R=QQ[h,t,eta,MonomialOrder=>GRevLex];','familyEquations={24*t*h-1,648*h^4+45*h^2-4};','fullCubicEquations={'+','.join(show(p) for p in unique)+'};','fullCubicIdeal=ideal join(familyEquations,fullCubicEquations);','fullCubicGB=gb fullCubicIdeal;','print("FULL_CUBIC_UNIT="|toString(fullCubicIdeal==ideal(1_R)));','print gens fullCubicGB;']
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
stem.with_suffix('.json').write_text(json.dumps({'status':'new independent full-cubic specialization; no result asserted until M2 run','original_full_cubic_equations':len(e['cubic']),'nonzero_after_specialization':len(cubic),'distinct_up_to_scalar':len(unique),'coefficient_field':'QQ','family':'d1=d3=0,d2=16t-12h,y0=y2=0,y1=6h-4t,y3=t,h4=-2h,h5=h6=0,h7=h,24th=1,648h^4+45h^2-4=0'},indent=2)+'\n')
print(json.dumps({'nonzero':len(cubic),'distinct':len(unique),'model':str(stem.with_suffix('.m2'))}))
