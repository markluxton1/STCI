-- One updated candidate, perturbing both middle coordinates after the endpoint failure.
-- Segre coordinates on S: ad=bc; Delta=b-c. All Ui are quadrics on S.
R=QQ[a,b,c,d];
delta=b-c;
U={a^2+delta^2,a*b+delta^2,d*c+2*delta^2,d^2+3*delta^2};
S=ideal(a*d-b*c);
-- Basepoints off the diagonal, in the projective chart Delta=1.
BP=S+ideal(delta-1)+ideal U;
assert(BP==ideal 1_R);
-- Along Delta=0, Ui restrict to the known basepoint-free quartic parametrization.
-- Pull back all four homogeneous ideal generators of C0.
J=S+ideal(delta-1)+ideal(
 U_0*U_3-U_1*U_2,
 U_0^2*U_2-U_1^3,
 U_0*U_2^2-U_1^2*U_3,
 U_2^3-U_1*U_3^2);
J0=J;
print("BASEPOINT_FREE_VERIFIED");
print("OFF_DIAGONAL_INVERSE_DIMENSION="|toString dim(R/J0));
print("OFF_DIAGONAL_INVERSE_DEGREE="|toString degree(R/J0));
print("OFF_DIAGONAL_INVERSE_GROEBNER_BASIS="|toString gens gb J0);
assert(dim(R/J0)==0 and degree(R/J0)==16);
