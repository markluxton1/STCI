#!/usr/bin/env python3
"""Generate a fresh corank-one reduction for the unresolved degree-15 factor.

Uses accepted source data but does not invoke any accepted verifier. Run this
script from any directory, then run the generated M2 source from repository
root. The abstract completeness theorem is recorded in the accompanying note.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
D=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('prior',D/'evening_localcoh_family2_exception_fields_2026_10_13.py'); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
a=mod.Audit('degree15');s,alpha,ker,p,r=a.source();L=a.matrix(alpha)
F0=[[e.get(0,a.zero) for e in row] for row in L]
F1=[[e.get(1,a.zero)[0] for e in row] for row in L]
assert all(e.get(1,a.zero)==a.field([e.get(1,a.zero)[0]]) for row in L for e in row)
q=18;m=74
E=[F1[i]+[Q(i==j) for j in range(m)]for i in range(m)]
for j in range(q):
 z=next(i for i in range(j,m)if E[i][j]);E[z],E[j]=E[j],E[z]
 d=E[j][j];E[j]=[v/d for v in E[j]]
 for i in range(m):
  if i!=j and E[i][j]:
   d=E[i][j];E[i]=[x-d*y for x,y in zip(E[i],E[j])]
assert all(E[i][j]==Q(i==j) for i in range(m)for j in range(q))
T=[row[q:]for row in E]
C=[]
for tr in T:
 row=[]
 for j in range(q):
  vec=[Q(0)]*a.n
  for i,coef in enumerate(tr):
   if coef:
    for d,x in enumerate(F0[i][j]):vec[d]+=coef*x
  row.append(tuple(vec))
 C.append(row)
U=[[a.field([T[i][72]])]for i in range(m)]
def fe(v):return 'sub(('+a.fstring(v)+'),K)'
def mat(M):return 'matrix{'+','.join('{'+','.join(fe(v)for v in row)+'}'for row in M)+'}'
base='general-localcoh-family2-degree15-corank-one-2026-10-14'
script='''P=QQ[k]; f=MODULUS; K=toField(P/ideal(f));
A=AMATRIX;
B=BMATRIX;
v=VMATRIX;
w=WMATRIX;
T=TMATRIX;
q=18; p=56;
print("canonical full-slope matrix constructed");
assert rank B==q-1;
assert rank(B||B*A)==q;
assert rank(B|w)==q-1;
print("PROVED exact rank B17, rank[B;BA]18, bottom target compatible over degree15 field");
h=gens kernel B;
assert numColumns h==1;
a=A*h;
assert rank(h|a)==2;
i=0;j=0;delta=0_K;
for ii from 0 to q-2 do for jj from ii+1 to q-1 do if delta==0 then (dd=h_(ii,0)*a_(jj,0)-h_(jj,0)*a_(ii,0); if dd!=0 then (i=ii;j=jj;delta=dd));
assert delta!=0;
ei=matrix{apply(q,kk->if kk==i then 1_K else 0_K)};
ej=matrix{apply(q,kk->if kk==j then 1_K else 0_K)};
Fh=(a_(j,0)*ei-a_(i,0)*ej)/delta;
Fa=(-h_(j,0)*ei+h_(i,0)*ej)/delta;
assert Fh*h==matrix{{1_K}} and Fh*a==0;
assert Fa*h==0 and Fa*a==matrix{{1_K}};
c=w//B;c=c-h*(Fh*c);
assert B*c==w and Fh*c==0;
pp=v-A*c;
linrows=apply(select(toList(0..q-1),jj->jj!=i and jj!=j),jj->(matrix{apply(q,kk->if kk==jj then 1_K else 0_K)}-h_(jj,0)*Fh-a_(jj,0)*Fa));
assert all(linrows,rr->rr*h==0 and rr*a==0);
BT=transpose B;
linN0=apply(linrows,rr->(transpose rr)||((-transpose(rr*A))//BT));
linN1=apply(linrows,rr->(matrix(q,1,(ii,jj)->0_K))||((-transpose rr)//BT));
gN0=(transpose Fh)||((-transpose(Fh*A))//BT);
gN1=(-transpose Fa)||((transpose(Fa*A-Fh))//BT);
gN2=matrix(q,1,(ii,jj)->0_K)||((transpose Fa)//BT);
R=K[lambda];LL=(lambda*id_(R^q)+sub(A,R))||sub(B,R);UU=sub(v||w,R);
ns=apply(toList(0..#linrows-1),j->sub(linN0#j,R)+lambda*sub(linN1#j,R));
ls=apply(ns,nn->(transpose nn*UU)_(0,0));
ng=sub(gN0,R)+lambda*sub(gN1,R)+lambda^2*sub(gN2,R);
gg=(transpose ng*UU)_(0,0);
assert all(ns,nn->transpose nn*LL==0);
assert transpose ng*LL==0;
print("complete obstruction: sixteen linear polynomials plus one quadratic");
J=ideal(join(ls,{gg})); print gens gb J;
assert J==ideal(1_R);
NN=0;
for ii from 0 to #ls-1 do if NN===0 then (aa=sub(ls#ii,{lambda=>0_R}); bb=sub((ls#ii-aa)/lambda,K); if bb==0 and aa!=0 then NN=ns#ii/aa);
first=position(ls,ll->ll!=0_R);
if NN===0 and first===null then (assert degree gg=={0}; NN=ng/gg);
if NN===0 then (
 ll=ls#first;aa=sub(ll,{lambda=>0_R});bb=sub((ll-aa)/lambda,K); assert bb!=0; alpha=-sub(aa,K)/bb;
 for ii from 0 to #ls-1 do if NN===0 then (at=sub(ls#ii,{lambda=>sub(alpha,R)}); if at!=0 then (bi=sub((ls#ii-sub(ls#ii,{lambda=>0_R}))/lambda,K); NN=(ns#ii-(bi/bb)*ns#first)/at));
 if NN===0 then (at=sub(gg,{lambda=>sub(alpha,R)}); assert at!=0; coeff=(gg-at)//ll; assert coeff*ll==gg-at; NN=(ng-coeff*ns#first)/at)
 );
assert transpose NN*LL==0;
assert transpose NN*UU==matrix{{1_R}};
Norig=transpose sub(T,R)*NN;
assert Norig_(72,0)==1_R;
print("constructed normalized dual of degree <=2");
ff=openOut "research/computations/STEM-dual.txt";
for row from 0 to 73 do ff << row << " " << toString Norig_(row,0) << endl;
close ff;
ff=openOut "research/computations/STEM-obstructions.txt";
for row from 0 to #ls-1 do ff << row << " " << toString ls#row << endl;
ff << "quadratic " << toString gg << endl;
close ff;
print("PASS structural degree15 full-fiber reduction and normalized dual saved");
exit 0;
'''
script=script.replace('MODULUS',a.fstring(a.mod)).replace('AMATRIX',mat(C[:q])).replace('BMATRIX',mat(C[q:])).replace('VMATRIX',mat(U[:q])).replace('WMATRIX',mat(U[q:])).replace('TMATRIX',mat([[a.field([x])for x in row]for row in T])).replace('STEM',base)
(D/(base+'.m2')).write_text(script)
print('GENERATED',D/(base+'.m2'), 'bytes',len(script),flush=True)
