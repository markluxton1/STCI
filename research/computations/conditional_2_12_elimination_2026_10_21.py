#!/usr/bin/env python3
"""Oct21 exact Schur presentation on explicit determinant charts; no GB run."""
import ast,json,itertools
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
HERE=Path(__file__).resolve().parent
old=HERE/'conditional_2_12_elimination_2026_10_20.py'
tree=ast.parse(old.read_text());stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='fmtlist' for t in n.targets))
e={'__file__':str(old),'__name__':'new_oct21_schur_prefix'};exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(old),'exec'),e)
ca,cm,cs,cp,var,const=(e[x] for x in ['ca','cm','cs','cp','var','const'])
padd,pscale,pmul=(e[x] for x in ['pzadd','pzscale','pzmul']);norm=e['normalized'];fmt=e['fmt']
D=[const(1),var(1),var(2),var(3),const(1)]
alpha={i:norm(v) for i,v in e['alpha'].items()}
N={i:norm(v) for i,v in e['norm'].items()}
Np={i-3:cs(v,Q(i,3)) for i,v in N.items() if i}
G={}
for i,p in enumerate(e['G']):
 for j,v in p.items():G[j+3-i]=ca(G.get(j+3-i,{}),cs(norm(v),Q(-1,2)**(3-i)))
W=padd(Np,pscale(pmul(alpha,G),-4))
for j in range(max(W,default=0),3,-1):
 v=W.pop(j,{})
 for k in range(4):
  jj=j-4+k;W[jj]=ca(W.get(jj,{}),cs(cm(v,D[k]),-1))
qlineAll=[W.get(i,{}) for i in range(4)]
# On symbolDet !=0, det(m_alpha)=81*symbolDet^2 and z is a
# unit mod D (D(0)=1). Thus the smaller differentiated test is equivalent.
W=padd({i-1:cs(v,i) for i,v in enumerate(D) if i},
        {i+2:cs(v,-12) for i,v in G.items()})
for j in range(max(W,default=0),3,-1):
 v=W.pop(j,{})
 for k in range(4):
  jj=j-4+k;W[jj]=ca(W.get(jj,{}),cs(cm(v,D[k]),-1))
qline=[W.get(i,{}) for i in range(4)]
rows=[p for p in e['normalizedFirst'] if p]+qline
hindices=[13,14,15,16]
M=[]
for p in rows:
 line=[{} for _ in range(5)]
 for m,v in p.items():
  hs=[j for j in m if j in hindices];assert len(hs)<=1
  col=hindices.index(hs[0]) if hs else 4
  mm=tuple(j for j in m if j not in hindices)
  line[col]=ca(line[col],{mm:v})
 M.append(line)
d1,d2,d3=[var(i) for i in (1,2,3)]
J=[[ca(d2,cs(cp(d1,2),-1)),cs(d1,-1),const(1)], [ca(cs(d1,-2),cm(d2,d3)),ca(cp(d2,2),cs(cm(d1,d3),-1),const(-1)),ca(cs(d3,2),cs(cm(d1,d2),-1))], [const(-1),cs(d3,-1),ca(cp(d3,2),cs(d2,-1))]]
b=[cs(ca(d3,cs(cm(d1,d2),-1),cs(cp(d1,3),-1)),Q(1,4)),cs(ca(cs(d2,-1),cs(cp(d1,2),-1),cp(d3,2),cs(cm(cm(d1,d2),d3),-1),cp(d2,3)),Q(1,2)),cs(ca(cs(d1,-1),cs(cm(d2,d3),-3),cp(d3,3)),Q(1,4))]
def det(A):
 out={}
 for p in itertools.permutations(range(len(A))):
  inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
  v=const((-1)**inv)
  for i,j in enumerate(p):v=cm(v,A[i][j])
  out=ca(out,v)
 return out
delta=det(J);nums=[]
for c in range(3):
 A=[[cs(b[i],-1) if j==c else J[i][j] for j in range(3)] for i in range(3)];nums.append(det(A))
for n,d,factor in zip(nums,(d1,d2,d3),(Q(1,4),Q(1,2),Q(1,4))):
 assert not ca(n,cs(cm(d,delta),factor))
# Cramer numerators cancel delta identically; no denominator occurs here.
repl={5:'-d1/4',6:'4*t-d2/2',7:'-d3/4',8:'t',1:'d1',2:'d2',3:'d3'}
def clearing(p,L):
 terms=[]
 for m,v in sorted(p.items(),key=lambda x:(len(x[0]),x[0])):
  factors=[]
  for j in sorted(set(m)):
   assert j in repl,j
   n=m.count(j);f='('+repl[j]+')';factors.append(f if n==1 else f+'^'+str(n))
  terms.append('('+str(v)+')'+(' * '+'*'.join(factors) if factors else ''))
 return '+'.join(terms) or '0'
newrows=[]
for row in M:
 L=max((sum(j in (5,6,7) for j in m) for p in row for m in p),default=0)
 newrows.append([clearing(p,L) for p in row])
stem=HERE/'conditional_2_12_elimination_2026_10_21'
base=[0,1,4,5]
lines=['-- Exact necessary Schur conditions, on symbolDet*pivotDet !=0 only.', 'R=QQ[d1,d2,d3,t,symbolInverse,pivotInverse,MonomialOrder=>GRevLex];','symbolDet='+fmt(delta)+';']
lines += ['-- Exact Cramer cancellation: y0=-d1/4,y1=4*t-d2/2,y2=-d3/4.']
lines += ['augmented=matrix{'+','.join('{'+','.join(row)+'}' for row in newrows)+'};', 'pivotRows={'+','.join(map(str,base))+'};','pivotDet=det submatrix(augmented,pivotRows,{0,1,2,3});','schurMinors=apply(select(toList(0..11),j->not member(j,pivotRows)),j->det submatrix(augmented,join(pivotRows,{j}),toList(0..4)));','chartIdeal=ideal join(schurMinors,{symbolInverse*symbolDet-1,pivotInverse*pivotDet-1});','print("SCHUR_READY: 4 root parameters,8 compatibility determinants,2 explicit chart inverses");','-- This is a necessary incidence without K2 or torsion; no emptiness claimed.']
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
meta={'status':'new exact necessary Schur chart; no computation completion claimed','coefficient_field':'QQ','root_parameters':['d1','d2','d3','t=c2'],'endpoint_chart':'d0=d4=1','inverted_new_determinants':['symbolDet','pivotDet'],'pivot_rows':base,'matrix_shape':[12,5],'rows':'8 first-incidence equations,4 exact all-strata quadric-cubic remainder equations','quadric_condition':'rem_D(N_T_prime(z^3)-4alpha*G)=0, N(z^3)=Dalpha','denominators':'each entire row multiplied by a sufficient power of symbolDet before extracting matrix; exact on symbolDet !=0','unresolved_boundaries':['d0*d4=0','symbolDet=0','pivotDet=0'],'no_K2_or_torsion_imposed':True,'old_export_sha256':sha256(old.read_bytes()).hexdigest(),'qline_term_counts':[len(p) for p in qline]}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))
