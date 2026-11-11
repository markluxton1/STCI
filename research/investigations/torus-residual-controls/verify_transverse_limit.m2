-- Exact replay for the transverse length-two sextic control.
R = QQ[x0,x1,x2,x3,lambda, Degrees => {1,1,1,1,0}];
quadric = x0*x3 - lambda*x1*x2;
cubic = lambda*x0^2*x2 - x1^3;
sextics = ideal(x0^4*quadric, cubic^2);
assert(saturate(sextics, ideal lambda) == sextics);

curveEquations = ideal(quadric, cubic, lambda^2*x0*x2^2 - x1^2*x3,
    lambda^3*x2^3 - x1*x3^2);
curveFamily = saturate(curveEquations, ideal lambda);

S = QQ[a,b,c,d];
specialize = map(S, R, {a,b,c,d,0});
specialSextics = ideal(a^5*d, b^6);
specialCurve = ideal(a*d, b^3, b^2*d, b*d^2);
assert(specialize(sextics) == specialSextics);
assert(specialize(curveFamily) == specialCurve);
assert(saturate(specialSextics, ideal vars S) == specialSextics);
assert(saturate(specialCurve, ideal vars S) == specialCurve);

pureCurve = intersect(ideal(d,b^3), ideal(a,b));
assert(pureCurve == specialCurve + ideal(b*d));
assert((specialCurve : ideal(b*d)) == ideal(a,b,d));
assert(hilbertPolynomial(S/specialCurve) ==
    new ProjectiveHilbertPolynomial from {0=>-3,1=>4});
assert(hilbertPolynomial(S/specialSextics) ==
    new ProjectiveHilbertPolynomial from {0=>-180,1=>36});

originalCurve = ideal(a*d-b*c, a^2*c-b^3, a*c^2-b^2*d, c^3-b*d^2);
assert(numerator hilbertSeries(S/specialCurve) == numerator hilbertSeries(S/originalCurve));
assert(numerator hilbertSeries(S/specialSextics) == numerator hilbertSeries(S/ideal(a^6,b^6)));
originalSextics = ideal(a^4*(a*d-b*c), (a^2*c-b^3)^2);
assert(codim originalSextics == 2);
assert(saturate(originalSextics, ideal vars S) == originalSextics);
assert(numerator hilbertSeries(S/originalSextics) == numerator hilbertSeries(S/specialSextics));
T = QQ[U,V];
assert(degree(T/ideal(V-U,U^2)) == 2);
print "PASS: full transverse curve and sextic limits over QQ";
