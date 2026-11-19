-- Search all algebraic values of the fourth lift coordinate with mu=2,
-- rho_0=rho_1=rho_3=0, in characteristic zero. Run from the repository root.
load "research/investigations/stci-equation-search/elliptic_rows.m2";
K = toField(QQ[imag]/ideal(imag^2+1));
S = K[z_0..z_3,p,MonomialOrder=>Eliminate 4];
Q0 = z_0*z_3-z_1^2;
Q1 = z_2^2-z_1*z_3+z_0*z_1;
quadric = Q1+2*Q0;
V = markedSections(S,sub(imag,K));
U = {V#0,V#1,V#2,V#3+p*Q0};
q = U#0*U#3-U#1*U#2;
firstCubic = U#0^2*U#2-U#1^3;
lastCubic = U#2^3-U#1*U#3^2;
sourceQuadrics = matrix{{Q0,quadric}};
dividedSections = apply({q,firstCubic,lastCubic},f -> (
    liftMatrix := matrix{{f}} // sourceQuadrics;
    divided := liftMatrix_(0,0);
    assert((f-Q0*divided) % ideal(quadric) == 0);
    divided
));

-- A basepoint-free full-support fiber must have at least one point of
-- the length-twelve scheme on E. Compute its parameter image in all charts.
zvars = {z_0,z_1,z_2,z_3};
hits = ideal(Q0,Q1)+ideal(dividedSections);
images = apply(zvars,x -> eliminate(zvars,hits+ideal(x-1)));
hitIdeal = intersect images;
hitPolys = flatten entries gens gb hitIdeal;
assert(#hitPolys == 1);
parameterPolynomial = first hitPolys;
assert(first degree parameterPolynomial == 6);
assert(1_S % ideal(parameterPolynomial,diff(p,parameterPolynomial)) == 0);

-- Over this finite parameter scheme the elimination image is closed.
-- Retain all four defining equations to test the whole off-E inverse.
offCurve = ideal(quadric,Q0-1,q,firstCubic,
    U#1^2*U#3-U#0*U#2^2,lastCubic,parameterPolynomial);
actualImage = eliminate(zvars,offCurve);
assert(actualImage == hitIdeal);
-- Basepoints cannot occur on E, where (2) is a morphism. This leaves
-- only the off-E chart on which to distinguish inverse points from basepoints.
basepoints = ideal(quadric,Q0-1,parameterPolynomial)+ideal(U);
assert(1_S % basepoints == 0);
print ("degree of candidate polynomial", first degree parameterPolynomial);
print "All six candidates are basepoint-free and have an extra inverse point.";
