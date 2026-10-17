-- INVALIDATED 2026-10-06: f4=basis(4,I) supplies generator coordinates.
-- The old product checks below do not multiply by quartic polynomials.
-- Retained for provenance; actual parity incidence is exported by
-- localcoh-parity-incidence-2026-10-06.py using the correct 74-row tensor.
error "Superseded invalid parity coefficient certificate; see 2026-10-06 audit";
-- Exact uniform exclusion for the full degree-two parity pure-top family.
-- Run after localcoh-symbol-export.m2, localcoh-symbol-top.py,
-- localcoh-symbol-parity.py. Each parameter coefficient of a lifted seed
-- is checked separately, so the assertions are uniform in a0,a2,b1 and
-- the lower-order T3 coordinate. There are no generic-parameter assumptions.
S=QQ[x,y,z,w]; q=x*w-y*z; A=x^2*z-y^3; B=x*z^2-y^2*w; C=y*w^2-z^3; I=ideal(q,A,B,C);
J=ideal(q^4,B^4); M=coker gens J;
f=map(coker gens(I^4),M,matrix{{1_S}});
g=Ext^2(f,S^1); h=g*basis(-7,source g);
assert(numColumns h==30 and numRows h==1);
load "research/computations/localcoh-symbol-parity-coordinates.m2";
assert(#parityCoeffs==10);
seeds=apply(parityCoeffs, coeffs -> sum(30,j->coeffs#j*lift(h_(0,j),S)));
hk=lift(h_(0,4)/4-3*h_(0,13)/4+h_(0,18),S);
f4=basis(4,I);
assert(numColumns f4==18);
uMon=y^11*z^2*w^4; vMon=y^10*z^3*w^4;
uTarget=(x*z*(q*B)^3)%J; vTarget=(y*w*(q*B)^3)%J;
assert(coefficient(uMon,uTarget)==1_S);
assert(coefficient(vMon,vTarget)==1_S);
for ancestor in append(seeds,hk) do (
    for j from 0 to 17 do (
        product=(f4_(0,j)*ancestor)%J;
        assert(coefficient(uMon,product)==0_S);
        assert(coefficient(vMon,product)==0_S);
    );
);
print "PASS: full pure-cubic parity family (a0+a2*t^2,b1*t) has no quartic ancestor";
print "Two fixed coefficient functionals kill all 198 products and detect the target numerators";
