#!/usr/bin/env python3
"""Optional exact polynomial rescaling design; no rank or exclusion verifier."""
from fractions import Fraction as F
from pathlib import Path
import ast,json,math,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research/validation/2026-10-14-localcoh-degree15-polynomial-scaling-design'
OUT.mkdir(exist_ok=True)
S=ROOT/'research/computations/general-localcoh-family2-degree15-corank-one-2026-10-14-attempt03.m2'
D=json.loads((ROOT/'research/computations/general-localcoh-degree15-sparse-block-2026-10-14-diagnostic.json').read_text())
META={'design_source':str(Path(__file__).relative_to(ROOT)), 'design_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'rational_source_sha256':hashlib.sha256(S.read_bytes()).hexdigest()}
def tr(p):
 while len(p)>1 and not p[-1]: p.pop()
 return p
def add(a,b):return tr([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return tr(c)
def powp(a,n):
 b=[F(1)]
 for _ in range(n):b=mul(b,a)
 return b
def div(a,b):
 a=a[:];q=[F(0)]*max(1,len(a)-len(b)+1)
 while len(a)>=len(b) and a!=[0]:
  d=len(a)-len(b);v=a[-1]/b[-1];q[d]=v
  for i,x in enumerate(b):a[i+d]-=v*x
  tr(a)
 assert a==[0],(a,b)
 return tr(q)
def pp(n):
 if isinstance(n,ast.Constant):return[F(n.value)]
 if isinstance(n,ast.Name):assert n.id=='k';return[F(0),F(1)]
 if isinstance(n,ast.UnaryOp):return neg(pp(n.operand))
 if isinstance(n.op,ast.Add):return add(pp(n.left),pp(n.right))
 if isinstance(n.op,ast.Sub):return sub(pp(n.left),pp(n.right))
 if isinstance(n.op,ast.Mult):return mul(pp(n.left),pp(n.right))
 if isinstance(n.op,ast.Pow):return powp(pp(n.left),n.right.value)
 raise ValueError(ast.dump(n))
DM=powp([F(-1),F(1)],9);DP=powp([F(1),F(1)],9);DEN=mul(DM,DP)
z={}
for l in S.read_text().splitlines():
 if l.startswith('z') and '=sub' in l:
  key,expr=l.split('=sub((',1);expr=expr.rsplit('),K);',1)[0];n=ast.parse(expr.replace('^','**'),mode='eval').body
  if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Div):z[key]=mul(pp(n.left),div(DEN,pp(n.right)))
  else:z[key]=mul(pp(n),DEN)
def lin(n):
 if isinstance(n,ast.Name):return{n.id:F(1)}
 if isinstance(n,ast.Constant):return{'const':F(n.value)}
 if isinstance(n,ast.UnaryOp):return{k:-v for k,v in lin(n.operand).items()}
 a,b=lin(n.left),lin(n.right)
 if isinstance(n.op,(ast.Add,ast.Sub)):
  s=F(-1) if isinstance(n.op,ast.Sub) else F(1)
  c=a.copy()
  for k,v in b.items():c[k]=c.get(k,0)+s*v
  return c
 if isinstance(n.op,ast.Mult):
  if set(a)=={'const'}:return{k:a['const']*v for k,v in b.items()}
  if set(b)=={'const'}:return{k:b['const']*v for k,v in a.items()}
 if isinstance(n.op,ast.Div) and set(b)=={'const'}:return{k:v/b['const'] for k,v in a.items()}
 raise ValueError(ast.dump(n))
def ev(n):
 c=[F(0)]
 for k,v in lin(n).items():c=add(c,[v*x for x in (DEN if k=='const' else z[k])])
 return c
def val(p,a):
 if p==[0]:return 999
 count=0
 while len(p)>1:
  x=sum(c*a**i for i,c in enumerate(p))
  if x:break
  p=div(p,[F(-a),F(1)]);count+=1
 return count
l=next(l for l in S.read_text().splitlines() if l.startswith('B=matrix'))
B=ast.parse(l[len('B=matrix'):].rstrip(';').replace('{','[').replace('}',']').replace('0_K','0').replace('^','**'),mode='eval').body
P=[[ev(B.elts[r].elts[c]) for c in D['selected_columns']] for r in D['selected_rows']]
M=[[9-val(p,1) if p!=[0] else None for p in row] for row in P]
Q=[[9-val(p,-1) if p!=[0] else None for p in row] for row in P]
# Hungarian potentials for min-cost perfect matching, nonedges cost huge.
def hung(weights):
 n=len(weights);u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
 cost=[[100000 if x is None else -x for x in row] for row in weights]
 for i in range(1,n+1):
  p[0]=i;j0=0;minv=[1000000]*(n+1);used=[False]*(n+1)
  while True:
   used[j0]=True;i0=p[j0];delta=1000000;j1=0
   for j in range(1,n+1):
    if not used[j]:
     cur=cost[i0-1][j-1]-u[i0]-v[j]
     if cur<minv[j]:minv[j]=cur;way[j]=j0
     if minv[j]<delta:delta=minv[j];j1=j
   for j in range(n+1):
    if used[j]:u[p[j]]+=delta;v[j]-=delta
    else:minv[j]-=delta
   j0=j1
   if p[j0]==0:break
  while True:
   j1=way[j0];p[j0]=p[j1];j0=j1
   if j0==0:break
 U=[-x for x in u[1:]];V=[-x for x in v[1:]]
 assert all(x is None or U[i]+V[j]>=x for i,row in enumerate(weights) for j,x in enumerate(row))
 # Normalize rows to nonnegative, permitting column negative only if favorable.
 shift=-min(U);U=[x+shift for x in U];V=[x-shift for x in V]
 return U,V
um,vm=hung(M);up,vp=hung(Q)
polys=[]
for i,row in enumerate(P):
 rr=[]
 for j,p in enumerate(row):
  if p==[0]:rr.append([0]);continue
  ee=um[i]+vm[j]-9;ff=up[i]+vp[j]-9
  x=p
  if ee>=0:x=mul(x,powp([F(-1),F(1)],ee))
  else:x=div(x,powp([F(-1),F(1)],-ee))
  if ff>=0:x=mul(x,powp([F(1),F(1)],ff))
  else:x=div(x,powp([F(1),F(1)],-ff))
  rr.append(x)
 polys.append(rr)
# Row-wise integer denominator clearing (no polynomial common scaling).
rowIntegerScale=[];outpoly=[]
for row in polys:
 lcm=math.lcm(*(x.denominator for p in row for x in p));rowIntegerScale.append(lcm)
 outpoly.append([[int(x*lcm) for x in p] for p in row])
res={**META,'scope':'New exact source-polynomial rescaling design only. Does not establish block invertibility or an exclusion.','source':str(S.relative_to(ROOT)),'selected_rows':D['selected_rows'],'selected_columns':D['selected_columns'],'row_k_minus_1':um,'column_k_minus_1':vm,'row_k_plus_1':up,'column_k_plus_1':vp,'row_integer_scale':rowIntegerScale,'total_k_minus_1_scaling_degree':sum(um)+sum(vm),'total_k_plus_1_scaling_degree':sum(up)+sum(vp),'max_entry_polynomial_degree':max(len(p)-1 for row in outpoly for p in row),'sum_row_max_degrees':sum(max(len(p)-1 for p in row) for row in outpoly),'nonzero_entries':sum(p!=[0] for row in outpoly for p in row),'polynomial_matrix':outpoly}
(OUT/'selected-block-scaled-polynomials.json').write_text(json.dumps(res))
print(json.dumps({k:v for k,v in res.items() if k!='polynomial_matrix'},indent=2))
print('row maxdegrees',[max(len(p)-1 for p in row) for row in outpoly])
print('globalD entrymaxdegree',max(len(p)-1 for row in P for p in row))
# Constant-row peeling uses exact rational identities in the newly selected block.
def const(p):
 if p==[0]:return F(0)
 if len(p)!=len(DEN):return None
 c=p[-1]/DEN[-1]
 return c if p==[c*x for x in DEN] else None
X=[[p[:] for p in row]for row in P];ri=list(range(17));ci=list(range(17));peeled=[]
while True:
 found=None
 for i in ri:
  cc=[const(X[i][j]) for j in ci]
  if all(c is not None for c in cc) and any(cc):
   # Pick least fill column.
   j=min((j for j,c in zip(ci,cc) if c),key=lambda j:sum(X[ii][j]!=[0] for ii in ri))
   found=i,j;break
 if found is None:break
 i,j=found;piv=const(X[i][j]);rowc={jj:const(X[i][jj])/piv for jj in ci if jj!=j}
 for ii in ri:
  if ii==i:continue
  pc=X[ii][j]
  for jj,c in rowc.items():
   if c:X[ii][jj]=sub(X[ii][jj],[c*x for x in pc])
  X[ii][j]=[F(0)]
 peeled.append([D['selected_rows'][i],D['selected_columns'][j],str(piv),{str(D['selected_columns'][jj]):str(c)for jj,c in rowc.items()if c}]);ri.remove(i);ci.remove(j)
print('constant rows peeled',peeled)
print('remaining dimension',len(ri))
(OUT/'constant-row-peel.json').write_text(json.dumps({**META,'peeled':peeled,'remaining_rows':[D['selected_rows'][i]for i in ri],'remaining_columns':[D['selected_columns'][j]for j in ci]}))
