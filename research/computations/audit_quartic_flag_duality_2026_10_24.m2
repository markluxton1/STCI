-- Independent reconstruction for the provisional flag/duality package.
-- Run: M2 --script research/computations/audit_quartic_flag_duality_2026_10_24.m2
-- No inherited normal-bundle or carrier proofs are rerun.
S=QQ[A,B,C,D];
K=A*C^2+B^2*D;
L=B*C-4*A*D;
M=A*D-B*C;
N=A*C^2-B^2*D;
delta=(256*A^3*D^3-192*A^2*B*C*D^2-27*A^2*C^4
      -6*A*B^2*C^2*D-27*B^4*D^2-4*B^3*C^3);
assert(delta == -4*L^3-27*K^2);
assert(delta == 4*M*(8*A*D+B*C)^2-27*N^2);
assert(ideal(K,delta)==ideal(K,L^3));
assert(ideal(M,delta)==ideal(M,N^2));
print "PASS: two discriminant identities and both full intersection ideals";

J=saturate(ideal jacobian matrix{{delta}});
auditAss=associatedPrimes J;
auditPO=ideal(B*C-4*A*D,C^3+4*B*D^2,A*C^2+B^2*D,B^3+4*A^2*C);
auditPB=ideal(B*C+8*A*D,C^3+8*B*D^2,A*C^2-B^2*D,B^3+8*A^2*C);
auditExpected={ideal(A,B),ideal(C,D),auditPO,auditPB,ideal(A,B,C),ideal(B,C,D)};
assert(#auditAss==6);
assert all(auditExpected,p->any(auditAss,q->p==q));
assert(degree(S/J)==16);
assert(hilbertPolynomial(S/J)==new ProjectiveHilbertPolynomial from {0=>-43,1=>16});
auditPD=primaryDecomposition J;
auditTop=select(auditPD,q->dim(S/q)==2);
auditUnmixed=intersect auditTop;
assert(hilbertPolynomial(S/auditUnmixed)==new ProjectiveHilbertPolynomial from {0=>-45,1=>16});
assert(hilbertPolynomial(auditUnmixed/J)==new ProjectiveHilbertPolynomial from {0=>2});
assert(ann(auditUnmixed/J)==ideal(B,C,A*D));
print "PASS: six associated primes, degree16, HP16n-43, endpoint correction HP2";
print("JacobianHP="|toString hilbertPolynomial(S/J));
print("unmixedHP="|toString hilbertPolynomial(S/auditUnmixed));
print("endpointCorrectionAnnihilator="|toString ann(auditUnmixed/J));

T=QQ[a,b,c];
affDelta=sub(delta,{A=>a,B=>b,C=>c,D=>1_T});
gA=-diff(a,affDelta)/6;
gB=-diff(b,affDelta)/12;
gC=-diff(c,affDelta)/12;
h=(b*c+8*a)*(a*c^2+b^2);
auditHB=matrix{{-b,-a*c,a*c^2},{0,-8*a-b*c,-a*c+b*c^2},
               {-8,c^2,-9*b-c^3},{9*c,9*b,18*a}};
auditGen={gA,gB,gC,h};
auditRows=toList(0..3);
auditCols=toList(0..2);
auditMinors=apply(auditRows,i->(-1)^i*det submatrix(auditHB,select(auditRows,j->j!=i),auditCols));
assert all(auditRows,i->auditMinors#i==9*auditGen#i);
assert(matrix{auditGen}*auditHB==0);
assert all({a,b,c},x->(x*h) % ideal(gA,gB,gC)==0);
assert(h % ideal(gA,gB,gC)!=0);
assert(4*a*diff(a,affDelta)+3*b*diff(b,affDelta)+c*diff(c,affDelta)==12*affDelta);
print "PASS: Hilbert-Burch minors, syzygies, nonzero length-one endpoint class, weighted Euler";
print "ALL INDEPENDENT AUDIT CHECKS PASSED";
