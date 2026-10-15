-- NEW bounded quotient-algebra norm reduction, not incidence elimination.
-- Accepted old proofs are premises; authoritative NEW attempt06 Q is reused.
outDir="research/validation/2026-10-14-quintic-h2-quotient-norm/attempt-01";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
par=QQ[deltaPar,vPar,wPar];
sourceRing=par[x];
Q=value get "research/validation/2026-10-14-quintic-logarithmic-support/attempt-06-sextic-quotient/Q-sextic.txt";
H=x^2+vPar*x+wPar;
remQ=Q%H;
r0=lift(coefficient(x^0,remQ),par);
r1=lift(coefficient(x^1,remQ),par);
rrContent=gcd(r0,r1);
detM=(vPar^2-4*wPar)*(vPar^2+6*vPar*wPar+6*wPar^2+2*wPar);
assert(rrContent==detM);
a0=r0//rrContent; a1=r1//rrContent;
primitiveNorm=a0^2-vPar*a0*a1+wPar*a1^2;
assert(r0^2-vPar*r0*r1+wPar*r1^2==detM^2*primitiveNorm);
normFactorization=factor primitiveNorm;
normPairs=toList normFactorization;
assert(#normPairs==2);
assert(sort apply(normPairs,pair->first degree pair#0)=={12,18});
assert(all(normPairs,pair->pair#1==1));
assert(product(normPairs,pair->(pair#0)^(pair#1))==primitiveNorm);
scan(normPairs,pair->save("norm-factor-degree-"|toString first degree pair#0,pair#0));
save("primitive-norm",primitiveNorm);
save("primitive-norm-factorization",normFactorization);
save("remainder-content",rrContent);
save("primitive-remainder-coefficients",matrix{{a0,a1}});
print "PASS exact norm product: Res(H,Q)=detM^2*N12*N18; both factors have exponent one";
-- Compare the two factors to the actual h2 cofactor and conductor open factors.
Kpar=frac par;
dv=sub(deltaPar,Kpar); vv=sub(vPar,Kpar); wv=sub(wPar,Kpar);
M=matrix{{wv,vv+3*wv,0_Kpar,-3*wv},{vv,1-3*wv,0_Kpar,6*wv},{0_Kpar,0_Kpar,wv,vv+3*wv},{-3_Kpar,-3*wv,vv,1+6*wv}};
rhs=matrix{{2*dv},{dv^2-3*dv},{dv-dv^2},{5*dv^2-3*dv}};
cofs=flatten entries(M^-1*rhs);
aa=-cofs#1*wv/2; bb=-cofs#3*wv; gg=cofs#0+3*bb-2*aa; ddVal=(cofs#2+3*gg-bb)/2;
actualJ=ddVal-2*gg+2*bb-aa; actualG=gg-3*bb+2*aa; actualB=bb-aa;
cofactorDet=cofs#0*cofs#3-cofs#1*cofs#2;
actualDelta1=actualG*(actualG+3*dv^2)*(actualG+dv^2+2*actualB)+actualJ*((dv^2-5*actualB)*actualG-3*actualB*(dv^2+3*actualB))-actualB*actualJ^2;
scan({{"cofactor-determinant",cofactorDet},{"Jbar",actualJ},{"G",actualG},{"Delta1",actualDelta1}},pair->(
 numVal=lift(numerator pair#1,par);
 commonFactor=gcd(numVal,primitiveNorm);
 assert(commonFactor==1);
 save(pair#0|"-numerator",numVal);
 save(pair#0|"-norm-gcd",commonFactor);
 print("PASS gcd(primitive norm,"|pair#0|" numerator)=1");
 ));
print "COMPLETE bounded quotient-algebra norm reduction; no elimination or quintic exclusion";
exit 0;
