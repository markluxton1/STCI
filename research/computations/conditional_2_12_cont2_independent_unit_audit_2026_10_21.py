#!/usr/bin/env python3
"""New pure-rational audit: full cubic residual provenance and tiny unit identity."""
import ast,json
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
HERE=Path(__file__).resolve().parent
src=HERE/'conditional_2_12_full_cubic_family_audit_2026_10_21.py'
tree=ast.parse(src.read_text());stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='stem' for t in n.targets))
e={'__file__':str(src),'__name__':'cont2_pure_rational_unit_audit'};exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(src),'exec'),e)
ca,cm,cs,cp,var,const=(e[x] for x in ['ca','cm','cs','cp','var','const'])
h,eta=var(0),var(1)
t=ca(cs(cp(h,3),Q(27,4)),cs(h,Q(15,32)))
def reduceH(p):
 d={}
 for m,v in p.items():
  k=(m.count(0),m.count(1));d[k]=d.get(k,Q(0))+v
 for j in range(max((k[0] for k in d),default=0),3,-1):
  for k in [k for k in d if k[0]==j]:
   v=d.pop(k)
   for a,c in ((j-2,Q(-5,72)),(j-4,Q(1,162))):
    kk=(a,k[1]);d[kk]=d.get(kk,Q(0))+v*c
 return {(0,)*a+(1,)*b:v for (a,b),v in d.items() if v}
def fromThree(p):
 out={}
 for m,v in p.items():
  term=const(v)
  for j in m:term=cm(term,(h,t,eta)[j])
  out=ca(out,term)
 return reduceH(out)
def normalize(p):
 p={m:v for m,v in p.items() if v}
 if not p:return ()
 a=next(v for m,v in sorted(p.items()))
 return tuple(sorted(cs(p,1/a).items()))
def parse(s):
 def rec(n):
  if isinstance(n,ast.Constant):return const(Q(n.value))
  if isinstance(n,ast.Name):return {'h':h,'eta':eta}[n.id]
  if isinstance(n,ast.UnaryOp):return cs(rec(n.operand),-1 if isinstance(n.op,ast.USub) else 1)
  if isinstance(n,ast.BinOp):
   a,b=rec(n.left),rec(n.right)
   if isinstance(n.op,ast.Add):return ca(a,b)
   if isinstance(n.op,ast.Sub):return ca(a,cs(b,-1))
   if isinstance(n.op,ast.Mult):return cm(a,b)
   if isinstance(n.op,ast.Div):assert set(b)=={()};return cs(a,1/b[()])
   if isinstance(n.op,ast.Pow):assert set(b)=={()};return cp(a,int(b[()]))
  raise ValueError(ast.dump(n))
 return rec(ast.parse(s.replace('^','**'),mode='eval').body)
ours={normalize(fromThree(p)) for p in e['cubic']};ours.discard(())
worker_path=HERE/'conditional_2_12_cubic_reduction_2026_10_21_candidates.json'
worker=json.loads(worker_path.read_text());theirs={normalize(parse(s)) for s in worker['unique_nonzero_full_cubic_equations']}
assert ours==theirs,(len(ours),len(theirs),ours-theirs,theirs-ours)
P=ca(cs(cp(h,4),648),cs(cp(h,2),45),const(-4))
E4=parse(worker['unique_nonzero_full_cubic_equations'][3]);E8=parse(worker['unique_nonzero_full_cubic_equations'][7])
B=ca(E4,cs(E8,-6));assert B==ca(cs(h,18),cs(cp(h,3),-324))
A=cs(ca(cs(cp(h,2),162),const(-1)),Q(1,4));C=ca(cs(cp(h,3),81),cs(h,Q(77,8)))
assert ca(cm(A,P),cm(C,B))==const(1)
out={'status':'PASS: exact rational residual-set comparison and explicit polynomial unit identity','coefficient_field':'QQ','residual_sets_equal_up_to_nonzero_rational_scalar':True,'distinct_residuals':len(ours),'tiny_identity':'1=((162h^2-1)/4)*(648h^4+45h^2-4)+(81h^3+77h/8)*(E4-6E8)','E4':'3eta/4+369h/16-891h^3/2','E8':'eta/8+27h/32-81h^3/4','source_specialization_sha256':sha256(src.read_bytes()).hexdigest(),'worker_candidates_sha256':sha256(worker_path.read_bytes()).hexdigest(),'uses_groebner_for_unit_check':False,'scope':'degree-four first+quadric-cubic family on d0*d4*detJ!=0 only; endpoint and orbitcollision strata retained'}
stem=Path(__file__).with_suffix('');stem.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
