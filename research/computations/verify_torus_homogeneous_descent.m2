-- Exact controls for synthesis/torus_homogeneous_descent.md.
-- Run: M2 --script research/computations/verify_torus_homogeneous_descent.m2
-- These computations check the displayed examples, not the quartic conjecture.

S = QQ[v,x,y,z];
J = ideal(x^2,x*y+z^2);
K = ideal(x^2,x*y,x*z^2,z^4);
assert(codim J == 2);
assert(saturate J == J);
assert(radical J == ideal(x,z));
assert(saturate K == K);
assert(radical K == ideal(x,z));
assert(numerator hilbertSeries(S/J) == numerator hilbertSeries(S/K));
assert(numgens source gens trim K == 4);
assert(sort degrees source gens trim K == {{2},{2},{3},{4}});
assert(K == intersect(ideal(x,z^4),ideal(x^2,y,z^2)));
assert(saturate(K,ideal y) == ideal(x,z^4));
assert(hilbertPolynomial(S/K) == hilbertPolynomial(S/J));
assert(degree(S/K) == 4);
assert(degree(ideal(x,z^4)/K) == 2);
print "PASS: supported line limit, Hilbert series, saturation and embedded length two";
print "Betti table of the original quotient:";
print betti res coker gens J;
print "Betti table of the limiting quotient:";
print betti res coker gens K;
print "Limiting resolution shifts:";
rk = res coker gens K;
shiftsK = apply(toList(0..3), i -> degrees rk_i);
assert(shiftsK == {{{0}},{{2},{2},{3},{4}},{{3},{4},{4},{5}},{{5}}});
print shiftsK;

-- For w(v,x,y,z)=(0,1,4,3), minimum weights give xy+h*z^2.
A = QQ[h,v,x,y,z,Degrees=>{0,1,1,1,1}];
raw = ideal(x^2,x*y+h*z^2);
full = saturate(raw,ideal h);
assert(full == ideal(x^2,x*y+h*z^2,x*z^2,z^4));
toS = map(S,A,{0,S_0,S_1,S_2,S_3});
assert(toS full == K);
opp = saturate(ideal(x^2,z^2+h*x*y),ideal h);
assert(toS opp == ideal(S_1^2,S_3^2));
print "PASS: full parameter saturation in both torus directions";

-- Clean cancellation: u=x, v=y, H=z, D=y^3-x^3.
-- This tests the global colon sequence and complete-intersection series.
-- It is an algebraic control, not a family for the specified quartic weights.
use S;
H = z;
U = ideal(x,y);
D = y^3-x^3;
Kclean = H*U+ideal D;
assert(Kclean : ideal H == U);
assert(Kclean+ideal H == ideal(H,D));
assert(numerator hilbertSeries(S/Kclean) == numerator hilbertSeries(S/J));
assert(numgens source gens trim Kclean == 3);
print "PASS: clean cancellation colon identity and CI(2,2) Hilbert series";

-- The local finite-length formula can be checked in k[x,y]; localization
-- at (x,y) does not change these finite dimensions.
B = QQ[r,s];
U = ideal(r,s^2);
H = r;
D = s^2;
assert(dim(B/U) == 0);
assert(degree(B/(H*U+ideal D)) == 4);
assert(degree(B/U)+degree(B/ideal(H,D)) == 4);
-- Without D in U the proposed uncorrected identity is false: 2 != 2+1.
D = s;
assert(degree(B/(H*U+ideal D)) == 2);
assert(degree(B/U)+degree(B/ideal(H,D)) == 3);
assert(degree(B/(U+ideal D))+degree(B/ideal(H,D)) == 2);
print "PASS: finite-length identity and missing-membership counterexample";

-- Twisted cubic positive control, with weights (0,1,2,3).
Q = QQ[c_0..c_3];
Itw = ideal(c_0*c_2-c_1^2,c_0*c_3-c_1*c_2,c_1*c_3-c_2^2);
Jtw = ideal(c_0*c_2-c_1^2,c_2^3-2*c_1*c_2*c_3+c_0*c_3^2);
assert(codim Jtw == 2);
assert(radical Jtw == Itw);
assert(degree(Q/Jtw) == 6);
print "PASS: eigenform (2,3) STCI of the twisted cubic";

-- A genuine failure of weaker descent for a rank-two torus.
-- The all-degree obstruction is the restriction proof in the report.
use S;
star = ideal(x*y,x*z,y*z);
Jstar = ideal(x*y,z*(x+y));
assert(radical Jstar == star);
assert(codim Jstar == 2);
use A;
fullstar = saturate(ideal(x*y,x*z+h*y*z),ideal h);
assert(fullstar == ideal(x*y,x*z+h*y*z,y^2*z));
Kstar = toS fullstar;
use S;
assert(radical Kstar == star);
assert(saturate Kstar == Kstar);
assert(numgens source gens trim Kstar == 3);
assert(numerator hilbertSeries(S/Kstar) == numerator hilbertSeries(S/Jstar));
assert(radical ideal(x*y,z*(x^2+y*z)) == star);
print "PASS: rank-two torus counterexample's ordinary homogeneous STCI pair";

C = QQ[u_0..u_3];
qC = u_0*u_3-u_1*u_2;
aC = u_1^3-u_0^2*u_2;
bC = u_1^2*u_3-u_0*u_2^2;
dC = u_2^3-u_1*u_3^2;
P = ideal(qC,aC,bC,dC);
assert(radical ideal(qC,aC,dC) == P);
print "PASS: three eigenforms cut out the fixed quartic";

print "ALL EXACT CONTROLS PASSED; no unrestricted quartic STCI conclusion";
