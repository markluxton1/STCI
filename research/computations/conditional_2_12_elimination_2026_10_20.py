#!/usr/bin/env python3
"""New compact generic-mu3-orbit chart, preserving exceptional boundaries.
No inherited proof is rerun, and this exporter performs no Groebner calculation.
"""
import ast,json
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from functools import reduce

HERE=Path(__file__).resolve().parent
src=HERE/'generalization_quadratic_root_global_second_model.py'
tree=ast.parse(src.read_text());stop=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='G1P' for t in n.targets))
# Reuse only the accepted coefficient-construction prefix needed for FIRST/G0;
# omit its consistency asserts, the second-obstruction proof checks and footer.
prefix=[n for n in tree.body[:stop] if not isinstance(n,ast.Assert)]
e={'__file__':str(src),'__name__':'new_elimination_export'};exec(compile(ast.Module(body=prefix,type_ignores=[]),str(src),'exec'),e)
ca,cm,cs,cp,var,const=(e[x] for x in ['ca','cm','cs','cp','var','const'])
names=[f'd{i}' for i in range(5)]+[f'y{i}' for i in range(4)]+[f'h{i}' for i in range(12)]+['eta'];e['NAMES'][:]=names
D=[var(i) for i in range(5)];Y=[var(i) for i in range(5,9)];H=[var(i) for i in range(9,21)]
# y0=b0,y1=b1,y2=b2,y3=c2. D=z²a-2zb+4c.
f=[ca(D[2],cs(Y[1],2),cs(Y[3],-4)),ca(D[3],cs(Y[2],2)),D[4],Y[0],Y[1],Y[2],cs(D[0],Q(1,4)),ca(cs(D[1],Q(1,4)),cs(Y[0],Q(1,2))),Y[3]]
replacement=f+H

def sub(p):
 return ca(*(cs(reduce(cm,(replacement[j] for j in m),const(1)),v) for m,v in p.items()))
def pzadd(*p):
 out={}
 for x in p:
  for j,v in x.items():out[j]=ca(out.get(j,{}),v)
 return {j:v for j,v in out.items() if v}
def pzscale(p,c):return {j:cs(v,c) for j,v in p.items() if cs(v,c)}
def pzmul(p,q):
 out={}
 for i,a in p.items():
  for j,b in q.items():out[i+j]=ca(out.get(i+j,{}),cm(a,b))
 return {j:v for j,v in out.items() if v}
U={0:D[0],3:D[3]};V={1:D[1],4:D[4]};W={2:D[2]}
alpha=pzadd(pzmul(U,U),pzmul(V,V),pzmul(W,W),pzscale(pzmul(U,V),-1),pzscale(pzmul(U,W),-1),pzscale(pzmul(V,W),-1))
norm=pzmul({i:d for i,d in enumerate(D)},alpha)
assert set(norm)<=set(range(0,13,3))
data=json.loads((HERE/'conditional_2_12_symbol_map_2026_10_20.json').read_text())
Af=[pzmul(alpha,{j:f[3*i+j] for j in range(3)}) for i in range(3)]
afv=[Af[i].get(j,{}) for i in range(3) for j in range(11)]
symbol=[ca(*(cs(v,Q(k)) for v,k in zip(afv,row) if Q(k))) for row in data['annihilator_11_by_33']]
assert [i for i,p in enumerate(symbol) if p]==[3,6,9]
# The fixed 22x22 image minor is an inherited exact linear presentation.
rows=data['image_rank_certificate']['minor_rows_zero_based'];labels=data['source_basis_labels'];cols=[labels.index(x) for x in data['image_basis_labels']]
A=[[Q(data['symbol_matrix_33_by_23'][i][j]) for j in cols] for i in rows]
aug=[row+[Q(int(i==j)) for j in range(22)] for i,row in enumerate(A)]
for j in range(22):
 p=next(i for i in range(j,22) if aug[i][j]);aug[j],aug[p]=aug[p],aug[j];a=aug[j][j];aug[j]=[x/a for x in aug[j]]
 for i in range(22):
  if i!=j and aug[i][j]:
   a=aug[i][j];aug[i]=[x-a*y for x,y in zip(aug[i],aug[j])]
inv=[row[22:] for row in aug]
C=[[Q(row[j]) for j in cols] for row in data['cubic_layer_matrix_40_by_23']]
K=[[sum(C[i][k]*inv[k][j] for k in range(22)) for j in range(22)] for i in range(40)]
G=[{j:sub(e['G0'].get((3-i,i,j),{})) for j in range(2)} for i in range(4)]
T=[]
for i in range(4):
 t={j:ca(*(cs(afv[rows[k]],K[10*i+j][k]) for k in range(22) if K[10*i+j][k])) for j in range(10)}
 t=pzadd(t,pzscale(pzmul(alpha,G[i]),-1))
 # exact q^3 cubic layer=(u+z*v/2)^3
 q3=[Q(1),Q(3,2),Q(3,4),Q(1,8)][i]
 t=pzadd(t,{i:cs(var(21),q3)})
 T.append(t)
a,b,c=[{j:f[3*i+j] for j in range(3)} for i in range(3)]
a2,b2,c2,ab,ac,bc=[pzmul(x,y) for x,y in [(a,a),(b,b),(c,c),(a,b),(a,c),(b,c)]]
syz=[pzadd(pzmul(pzadd(b2,pzscale(ac,-1)),T[0]),pzscale(pzmul(ab,T[1]),-1),pzmul(a2,T[2])),pzadd(pzmul(bc,T[0]),pzscale(pzmul(ac,T[1]),-1),pzmul(a2,T[3])),pzadd(pzmul(c2,T[0]),pzscale(pzmul(ac,T[2]),-1),pzmul(ab,T[3])),pzadd(pzmul(c2,T[1]),pzscale(pzmul(bc,T[2]),-1),pzmul(pzadd(b2,pzscale(ac,-1)),T[3]))]
cubic=[p for x in syz for j,p in sorted(x.items()) if p]
first=[sub(p) for p in e['FIRST']];fmt=e['fmt']
# Torus+projective finite cover on d0*d4 !=0, setting d0=d4=1.
collapsedH=list(H)
collapsedH[3]=ca(cs(cm(f[0],H[5]),-1),cs(cm(f[1],H[4]),-1))
collapsedH[2]=ca(const(-3),cs(cm(f[0],H[4]),-1),cs(cm(f[1],collapsedH[3]),-1))
collapsedH[1]=ca(cs(f[1],-4),cs(f[5],3),cs(cm(f[0],collapsedH[3]),-1),cs(cm(f[1],collapsedH[2]),-1))
collapsedH[0]=ca(cs(f[0],-5),cs(f[4],3),cs(cm(f[0],collapsedH[2]),-1),cs(cm(f[1],collapsedH[1]),-1))
collapsedH[8]=ca(cs(cm(f[7],H[7]),-4),cs(cm(f[8],H[6]),-4))
collapsedH[9]=ca(const(Q(-9,2)),cs(cm(f[7],collapsedH[8]),-4),cs(cm(f[8],H[7]),-4))
collapsedH[10]=ca(cs(f[3],Q(-3,2)),cs(f[7],-16),cs(cm(f[7],collapsedH[9]),-4),cs(cm(f[8],collapsedH[8]),-4))
collapsedH[11]=ca(cs(f[4],Q(-3,2)),cs(f[8],-14),cs(cm(f[7],collapsedH[10]),-4),cs(cm(f[8],collapsedH[9]),-4))
def normalized(p):
 out={}
 for m,v in p.items():
  if not any(9<=i<=20 for i in m):
   mm=tuple(i for i in m if i not in (0,4));out[mm]=out.get(mm,Q(0))+v
  else:
   term=const(v)
   for i in m:
    if i in (0,4):continue
    term=cm(term,collapsedH[i-9] if 9<=i<=20 else var(i))
   out=ca(out,term)
 return {m:v for m,v in out.items() if v}
normalizedFirst=[normalized(p) for p in first]
assert [i for i,p in enumerate(normalizedFirst) if p]==list(range(4,12))
retainedIndices=[1,2,3,5,6,7,8,13,14,15,16,21]
fmtlist=lambda ps:'{'+','.join(fmt(p) for p in ps)+'}'
stem=HERE/'conditional_2_12_elimination_2026_10_20'
def zzpoly(p):
 return '+'.join('('+fmt(normalized(v))+')*zz^'+str(j) for j,v in sorted(p.items()) if normalized(v)) or '0'
kmatrix='matrix(R,{'+','.join('{'+','.join(str(v) for v in row)+'}' for row in K)+'})'
lines=[
 '-- Compact chart; d0=d4=1 is a finite torus/projective cover only over d0*d4 !=0.',
 '-- alpha_can is imposed; its necessity on all actual pairs uses the separately reviewed quadric-intersection norm argument.',
 'R=QQ['+','.join(names[i] for i in retainedIndices)+',smoothInverse,MonomialOrder=>GRevLex];',
 'firstEquations='+fmtlist([p for p in normalizedFirst if p])+';',
 'symbolEquations='+fmtlist([normalized(symbol[i]) for i in [3,6,9]])+';',
 'S=R[zz];',
 'aa=d2+2*y1-4*y3+(d3+2*y2)*zz+zz^2;',
 'bb=y0+y1*zz+y2*zz^2;',
 'cc=1/4+(d1/4+y0/2)*zz+y3*zz^2;',
 'uu=1+d3*zz^3; vv=d1*zz+zz^4; ww=d2*zz^2;',
 'alphaCanonical=uu^2+vv^2+ww^2-uu*vv-uu*ww-vv*ww;',
 'coeffR=(p,j)->sub(coefficient(zz^j,p),R);',
 'delta=bb^2-4*aa*cc;',
 'compactDeltaCoeffs=apply(5,j->coeffR(delta,j));',
 'compactInvI=12*(compactDeltaCoeffs#4)*(compactDeltaCoeffs#0)-3*(compactDeltaCoeffs#3)*(compactDeltaCoeffs#1)+(compactDeltaCoeffs#2)^2;',
 'compactInvJ=72*(compactDeltaCoeffs#4)*(compactDeltaCoeffs#2)*(compactDeltaCoeffs#0)+9*(compactDeltaCoeffs#3)*(compactDeltaCoeffs#2)*(compactDeltaCoeffs#1)-27*(compactDeltaCoeffs#4)*(compactDeltaCoeffs#1)^2-27*(compactDeltaCoeffs#3)^2*(compactDeltaCoeffs#0)-2*(compactDeltaCoeffs#2)^3;',
 'smoothDiscriminant=(4*compactInvI^3-compactInvJ^2)/27;',
 'baseIdeal=ideal join(firstEquations,symbolEquations,{smoothInverse*smoothDiscriminant-1});',
 'print "COMPACT_BASE_MODEL_READY";',
 'afVector=flatten apply({aa,bb,cc},p->apply(11,j->coeffR(alphaCanonical*p,j)));',
 'splitCubicMatrix='+kmatrix+';',
 'splitCubicVector=flatten entries(splitCubicMatrix*transpose matrix{apply({'+','.join(map(str,rows))+'},j->afVector#j)});',
 'gg={'+','.join(zzpoly(p) for p in G)+'};',
 'tt=apply(4,i->sum(10,j->(splitCubicVector#(10*i+j))*zz^j)-alphaCanonical*gg#i+eta*({1,3/2,3/4,1/8}#i)*zz^i);',
 'syzygyPolynomials={(bb^2-aa*cc)*tt#0-aa*bb*tt#1+aa^2*tt#2,bb*cc*tt#0-aa*cc*tt#1+aa^2*tt#3,cc^2*tt#0-aa*cc*tt#2+aa*bb*tt#3,cc^2*tt#1-bb*cc*tt#2+(bb^2-aa*cc)*tt#3};',
 'cubicEquations=select(flatten apply(syzygyPolynomials,p->apply(14,j->coeffR(p,j))),p->p!=0);',
 'cubicIdeal=baseIdeal+ideal cubicEquations;',
 'print("COMPACT_CUBIC_EQUATIONS="|toString(#cubicEquations));',
 '-- A unit certificate here excludes only this chart; d0*d4=0 strata remain.',
 ]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
meta={'status':'new compact chart, not an emptiness claim','chart':'d0=d4=1 finite cover of nonzero endpoints under projective scaling and C0 torus','f_coordinates':'a=(d2+2y1-4y3,d3+2y2,d4); b=(y0,y1,y2); c=(d0/4,d1/4+y0/2,y3)','alpha':'U^2+V^2+W^2-UV-UW-VW; U=d0+d3*z^3,V=d1*z+d4*z^4,W=d2*z^2','validity':'alpha_can imposed. The quadric-intersection norm argument is a separate proof obligation for its necessity on every actual pair; the elementary factorization proves necessity on four distinct free mu3-orbits.','symbol_nonzero_rows_zero_based':[3,6,9],'cubic_syzygy_equation_count':len(cubic),'ambient_variables_after_normalization_and_h_collapse':len(retainedIndices)+1,'base_equations':8+3+1,'retained_h_variables':['h4','h5','h6','h7'],'eliminated_first_equations_verified_zero':[0,1,2,3,12,13,14,15],'inherited_generator_sha256':sha256(src.read_bytes()).hexdigest(),'no_groebner_in_exporter':True}
stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))
