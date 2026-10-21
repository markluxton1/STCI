-- Lightweight exact rational certificate: free-orbit global sextic exclusion.
-- This checks ideal equality by rational normal forms, then a raw polynomial
-- unit identity. The archived 23MB lift matrices are not needed for replay.
load "research/computations/conditional_2_12_cubic_reduction_2026_10_21_family.m2";
candidateTriangularIdeal=ideal(
    h6,h5,h4+2*h7,d3,d1,
    y3-27/4*h7^3-15/32*h7,
    d2-108*h7^3+9/2*h7,
    648*h7^4+45*h7^2-4);
BI=gb familyIdeal;
BJ=gb candidateTriangularIdeal;
assert(all(flatten entries((gens candidateTriangularIdeal)%BI),p->p==0));
assert(all(flatten entries((gens familyIdeal)%BJ),p->p==0));
assert(dim candidateTriangularIdeal==0);
assert(degree candidateTriangularIdeal==4);
print "FREE_ORBIT_EXACT_IDEAL_EQUALITY_DIM0_DEG4_PASS";
load "research/computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.m2";
E4=3/4*eta+369/16*h-891/2*h^3;
E8=1/8*eta+27/32*h-81/4*h^3;
assert(E4==cubicEquations#3);
assert(E8==cubicEquations#7);
assert(E4-6*E8==18*h-324*h^3);
assert((162*h^2-1)/4*candidatePolynomial+(81*h^3+77/8*h)*(E4-6*E8)==1);
print "FREE_ORBIT_FULL_GLOBAL_C3_RAW_UNIT_IDENTITY_PASS";
