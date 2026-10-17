-- INVALIDATED 2026-10-06: basis(4,I) is an ideal-generator coordinate
-- matrix, not the quartic-polynomial row. The old degree-17 coefficient
-- checks below are vacuous. Retained for provenance; use the correct tensor
-- and localcoh-incidence-2026-10-06.py instead.
error "Superseded invalid quartic-coordinate certificate; see 2026-10-06 audit";
S=QQ[x,y,z,w]; q=x*w-y*z; A=x^2*z-y^3; B=x*z^2-y^2*w; C=y*w^2-z^3; I=ideal(q,A,B,C);
M=coker gens ideal(q^4,B^4);
E=Ext^2(coker gens(I^4),S^1); f=map(coker gens(I^4),M,matrix{{1_S}}); g=Ext^2(f,S^1); h=g*basis(-7,source g);
coeffs={31/24,0,0,-11/6,0,0,0,0,12,-5/8,0,0,0,0,-7/12,0,-3/2,-1/12,0,0,0,0,0,0,-1/8,0,0,12,2,1};
h0=sum(30,j->coeffs#j*lift(h_(0,j),S));
hk=lift(h_(0,4)/4-3*h_(0,13)/4+h_(0,18),S);
f4=basis(4,I);
assert(numColumns f4==18);
ff=openOut "/Users/markluxton/Projects/STCI/research/computations/localcoh-symbol-seed-products.txt";
ff << toString ((x*z*(q*B)^3)%ideal(q^4,B^4)) << endl;
ff << toString ((y*w*(q*B)^3)%ideal(q^4,B^4)) << endl;
for j from 0 to 17 do (
 ff << toString ((f4_(0,j)*h0)%ideal(q^4,B^4)) << endl;
 ff << toString ((f4_(0,j)*hk)%ideal(q^4,B^4)) << endl;
);
close ff;
print "PASS exported seed products";
-- Every order-four ancestor with this pure top direction is in the pencil
-- k*h0 + k*hk, because the h=t top coefficient is obstructed and hk spans T3.
-- A single coefficient functional excludes each target for the full pencil.
J=ideal(q^4,B^4);
uTarget=(x*z*(q*B)^3)%J;
vTarget=(y*w*(q*B)^3)%J;
uMon=y^11*z^2*w^4;
vMon=y^10*z^3*w^4;
assert(coefficient(uMon,uTarget)==1_S);
assert(coefficient(vMon,vTarget)==1_S);
for j from 0 to 17 do (
    p0=(f4_(0,j)*h0)%J;
    pk=(f4_(0,j)*hk)%J;
    assert(coefficient(uMon,p0)==0_S and coefficient(uMon,pk)==0_S);
    assert(coefficient(vMon,p0)==0_S and coefficient(vMon,pk)==0_S);
);
print "PASS: every lift of pure cubic direction (1+t^2,t) is uniformly excluded";
