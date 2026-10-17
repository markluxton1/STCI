#!/usr/bin/env python3
"""Generate attempt02: small rational elimination, then exact degree15 specialization.

This fresh attempt follows a missing initial field handle and a separate symbolic
syntax failure. Explicit flush markers distinguish each mathematical stage.
"""
from pathlib import Path
import re
D=Path(__file__).resolve().parent
old=D/'general-localcoh-family2-degree15-corank-one-2026-10-14.log'
(D/'general-localcoh-family2-degree15-corank-one-2026-10-14-attempt01.log').write_bytes(old.read_bytes())
(D/'general-localcoh-family2-degree15-corank-one-2026-10-14-attempt01-lineage.txt').write_text('Initial field attempt: unified exec session6052, later Unknown process id; original log empty. No mathematical output or claim. The 30KB symbolic fallback session21868 reached canonical construction then failed at unparenthesized assert syntax. Its separate original log is retained. Attempt02 uses generic rational elimination, exact denominator-unit specialization into the degree15 quotient field, and explicit progress flushes.\n')
script=(D/'general-localcoh-family2-symbolic-corank-one-2026-10-14.m2').read_text()
script=script[:script.index('ff=openOut')]
script=re.sub(r'assert ([^;]*);',r'assert(\1);',script)
script=script.replace('P=QQ[k]; K=frac P; k=sub(k,K);','P=QQ[k]; K=frac P; k=sub(k,K); print("attempt02: loading rational source matrix"); flush stdio;')
script=script.replace('print("canonical full-slope matrix constructed");','print("attempt02: canonical rational pencil constructed"); flush stdio;')
script=script.replace('print("PROVED exact rank B17, rank[B;BA]18, bottom target compatible over degree15 field");','print("attempt02: generic rank B17, observability18, bottom compatibility completed"); flush stdio;')
script+='''
D0=transpose((transpose(id_(K^q)-h*Fh))//BT);
assert(D0*B==id_(K^q)-h*Fh);
print("attempt02: generic complement inverse and dual coefficient data computed"); flush stdio;
Q0=QQ[z];f=243*z^15+810*z^14+2646*z^13+990*z^12-9465*z^11-54222*z^10-114414*z^9-166406*z^8-34359*z^7+301686*z^6+897946*z^5+1296458*z^4+1345117*z^3+811630*z^2+285598*z-610;
K15=toField(Q0/ideal(f));
phi=map(K15,P,{sub(z,K15)});
units=0;
cv=e->(nn=numerator e;dd=denominator e;dd15=phi(dd);if dd15==0 then error "nonunit rational pivot at degree15 factor";units=units+1;phi(nn)/dd15);
cm=M->matrix apply(numRows M,i->apply(numColumns M,j->cv(M_(i,j))));
A=cm A; B=cm B; v=cm v; w=cm w;
h=cm h; a=cm a; c=cm c; Fh=cm Fh; Fa=cm Fa; D0=cm D0;
linN0=apply(linN0,cm);linN1=apply(linN1,cm);gN0=cm gN0;gN1=cm gN1;gN2=cm gN2;
assert(B*h==0 and Fh*h==matrix{{1_K15}});
assert(D0*B==id_(K15^q)-h*Fh);
assert(a==A*h and Fa*h==0 and Fa*a==matrix{{1_K15}});
assert(B*c==w);
print("attempt02: EXACT degree15 rank17/observable18/compatible target via specialized inverse, checked coefficient inversions="|toString units); flush stdio;
R=K15[lambda];LL=(lambda*id_(R^q)+sub(A,R))||sub(B,R);UU=sub(v||w,R);
ns=apply(toList(0..#linN0-1),j->sub(linN0#j,R)+lambda*sub(linN1#j,R));
ls=apply(ns,nn->(transpose nn*UU)_(0,0));
ng=sub(gN0,R)+lambda*sub(gN1,R)+lambda^2*sub(gN2,R);
gg=(transpose ng*UU)_(0,0);
assert(all(ns,nn->transpose nn*LL==0));
assert(transpose ng*LL==0);
print("attempt02: sixteen linear and one quadratic obstruction built"); flush stdio;
J=ideal(join(ls,{gg})); print gens gb J; flush stdio;
assert(J==ideal(1_R));
NN=0;
for ii from 0 to #ls-1 do if NN===0 then (aa=sub(ls#ii,{lambda=>0_R}); bb=sub((ls#ii-aa)/lambda,K15); if bb==0 and aa!=0 then NN=ns#ii/aa);
first=position(ls,ll->ll!=0_R);
if NN===0 and first===null then (assert(degree gg=={0}); NN=ng/gg);
if NN===0 then (
 ll=ls#first;aa=sub(ll,{lambda=>0_R});bb=sub((ll-aa)/lambda,K15); assert(bb!=0); alpha=-sub(aa,K15)/bb;
 for ii from 0 to #ls-1 do if NN===0 then (at=sub(ls#ii,{lambda=>sub(alpha,R)}); if at!=0 then (bi=sub((ls#ii-sub(ls#ii,{lambda=>0_R}))/lambda,K15); NN=(ns#ii-(bi/bb)*ns#first)/at));
 if NN===0 then (at=sub(gg,{lambda=>sub(alpha,R)}); assert(at!=0); coeff=(gg-at)//ll; assert(coeff*ll==gg-at); NN=(ng-coeff*ns#first)/at)
 );
assert(transpose NN*LL==0);
assert(transpose NN*UU==matrix{{1_R}});
T=T_MATRIX;
Norig=transpose sub(T,R)*NN;
assert(Norig_(72,0)==1_R);
print("attempt02: normalized degree<=2 dual constructed in original tensor coordinates"); flush stdio;
ff=openOut "research/computations/BASE-dual.txt";
for row from 0 to 73 do ff << row << " " << toString Norig_(row,0) << endl;
close ff;
ff=openOut "research/computations/BASE-obstructions.txt";
for row from 0 to #ls-1 do ff << row << " " << toString ls#row << endl;
ff << "quadratic " << toString gg << endl;
close ff;
print("PASS attempt02: degree15 full-fiber corank-one exclusion certificate saved"); flush stdio;
exit 0;
'''
# T is coefficientwise rational; reconstruct from the original field source text,
# converting only its numeric coefficients into the new field.
orig=(D/'general-localcoh-family2-degree15-corank-one-2026-10-14.m2').read_text()
tline=next(x for x in orig.splitlines()if x.startswith('T='))
tmat=tline[2:-1].replace(',K)',',K15)')
base='general-localcoh-family2-degree15-corank-one-2026-10-14-attempt02'
script=script.replace('T_MATRIX',tmat).replace('BASE',base)
(D/(base+'.m2')).write_text(script)
print('GENERATED attempt02 rational-to-degree15 source',len(script),flush=True)
