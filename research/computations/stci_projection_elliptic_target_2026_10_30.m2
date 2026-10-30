-- Balanced four-contact target stratum: P(t)=R(t)^5.
-- R has four distinct nonzero roots; coefficients normalized leading/constant1.
-- This file builds an exact incidence, not a completed emptiness certificate.
R=QQ[symbol pa,symbol pb,symbol pc,symbol ss0,symbol ss1,symbol ss2,symbol ss3];
P=R[symbol tt];
quartic=tt^4+pa*tt^3+pb*tt^2+pc*tt+1;
p20=quartic^5;
T=R[symbol xx];
e=apply(toList(0..2),j->sum(toList(0..6),i->sub(coefficient(tt^(3*i+j),p20),R)*xx^i));
disc=e#1^2-4*e#0*e#2;
assert(sub(coefficient(xx^12,disc),R)==-5*(4*pb+3*pa^2));
assert(sub(coefficient(xx^0,disc),R)==-5*(4*pb+3*pc^2));
squareQuartic=xx^4+ss3*xx^3+ss2*xx^2+ss1*xx+ss0;
remnant=disc;
for j in reverse toList(8..12) do (
 remnant=remnant-coefficient(xx^j,remnant)*xx^(j-8)*squareQuartic^2;
);
equations=apply(toList(0..7),j->sub(coefficient(xx^j,remnant),R));
I=ideal equations;
stdio << "BALANCED_TARGET_SOURCE_BUILT" << endl;
stdio << "TARGET_COEFFICIENT_DEGREES=" << apply(e,f->degree f) << endl;
stdio << "REMAINDER_EQUATION_COUNT=" << #equations << endl;
stdio << "REMAINDER_TOTAL_DEGREES=" << apply(equations,f->(degree f)_0) << endl;
stdio << "EQUATION_TERM_COUNTS=" << apply(equations,f->#terms f) << endl;
stdio << "SQUARE_DIVISIBILITY_INCIDENCE_READY" << endl;
flush stdio;
-- The affine monic square-quartic chart excludes a square factor at infinity.
-- The omitted lower-degree square-factor charts must be handled separately.
-- Full projection admissibility also needs primitive bidegree, normalization
-- point counts, and the extension back to four actual global source sections.
