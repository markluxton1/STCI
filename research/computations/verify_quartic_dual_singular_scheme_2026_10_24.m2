-- Exact characteristic-zero algebra for the new singular-scheme calculation.
-- Run from the repository root:
-- M2 --script research/computations/verify_quartic_dual_singular_scheme_2026_10_24.m2
-- This does not rerun the accepted normal splitting or any STCI argument.

S=QQ[A,B,C,D];
L=B*C-4*A*D;
K=A*C^2+B^2*D;
Delta=-4*L^3-27*K^2;
J=ideal(diff(A,Delta),diff(B,Delta),diff(C,Delta),diff(D,Delta));
h=(B*C+8*A*D)*K;
U=J+ideal h;
Pzero=ideal(A,B,C);
Pinfty=ideal(B,C,D);
pointUnion=ideal(B,C,A*D);

assert(J==saturate J);
print "PASS homogeneous Jacobian ideal is saturated";
assert(J:ideal h==pointUnion);
assert(U==saturate(saturate(J,Pzero),Pinfty));
assert(ann(U/J)==pointUnion);
print "PASS U=J+(h), J:h=(B,C,AD), and U is the endpoint saturation";

assert(B*h==-2*A*diff(B,Delta)/27-C*diff(D,Delta)/54);
assert(C*h==-B*diff(A,Delta)/54-2*D*diff(C,Delta)/27);
assert(A*D*h==-A*C*diff(B,Delta)/216-B*D*diff(C,Delta)/24+C^2*diff(D,Delta)/108);
assert(h%J!=0);
print "PASS three explicit endpoint-socle syzygies and h nonmembership";

lineZero=ideal(A,B^2);
lineInfty=ideal(D,C^2);
oscPrime=ideal(B*C-4*A*D,C^3+4*B*D^2,A*C^2+B^2*D,B^3+4*A^2*C);
oscPrimary=ideal(K,C^4+8*B*C*D^2-16*A*D^3,L^2,B^4+8*A^2*B*C-16*A^3*D);
bitPrime=ideal(B*C+8*A*D,C^3+8*B*D^2,A*C^2-B^2*D,B^3+8*A^2*C);
assert(U==intersect(lineZero,lineInfty,oscPrimary,bitPrime));
assert(radical oscPrimary==oscPrime);
actualU=associatedPrimes U;
actualJ=associatedPrimes J;
expectedU={ideal(A,B),ideal(C,D),oscPrime,bitPrime};
expectedJ=expectedU|{Pzero,Pinfty};
assert(#actualU==#expectedU and all(actualU,pp->any(expectedU,qq->pp==qq)));
assert(#actualJ==#expectedJ and all(actualJ,pp->any(expectedJ,qq->pp==qq)));
print "PASS four unmixed components and exactly two embedded point primes";
assert(degree(S/J)==16);
assert(hilbertPolynomial(S/J)==new ProjectiveHilbertPolynomial from {0=>-43,1=>16});
assert(hilbertPolynomial(S/U)==new ProjectiveHilbertPolynomial from {0=>-45,1=>16});
assert(hilbertPolynomial(U/J)==new ProjectiveHilbertPolynomial from {0=>2});
print "PASS singular degree 16; Hilbert polynomials 16n-43, 16n-45, and correction 2";

T=QQ[a,b,c];
f=256*a^3-192*a^2*b*c-27*a^2*c^4-6*a*b^2*c^2-27*b^4-4*b^3*c^3;
gA=-diff(a,f)/6;
gB=-diff(b,f)/12;
gC=-diff(c,f)/12;
hLocal=(b*c+8*a)*(a*c^2+b^2);
Mat=matrix{{-b,-a*c,a*c^2},{0,-8*a-b*c,-a*c+b*c^2},{-8,c^2,-9*b-c^3},{9*c,9*b,18*a}};
gg={gA,gB,gC,hLocal};
scan(0..3,i->assert((-1)^i*det(submatrix(Mat,toList(set(0..3)-set{i}),{0,1,2}))==9*gg#i));
assert((matrix{gg})*Mat==0);
assert(ideal(gA,gB,gC,hLocal)==minors(3,Mat));
assert(codim ideal(gA,gB,gC,hLocal)==2);
assert(ann(ideal(gA,gB,gC,hLocal)/ideal(gA,gB,gC))==ideal(a,b,c));
print "PASS endpoint Hilbert-Burch minors, height two, and one-dimensional socle correction";
print "PASS all new singular-scheme checks completed over QQ";
