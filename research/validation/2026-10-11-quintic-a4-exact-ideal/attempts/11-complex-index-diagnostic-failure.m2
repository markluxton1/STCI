-- Exact audit of the candidate degree-five A4 anticanonical model.
-- All ideal equalities, saturations, and chart identities are over QQ.
-- The script certifies this literal model, not every quintic projection.
checks = 0;
ck = (label,condition) -> (
    if not condition then error("FAIL " | label);
    checks = checks+1;
    );
zeroCheck = (label,value) -> ck(label,value == 0);

R = QQ[z0,z1,z2,z3,z4,z5];
T = QQ[x,y,z];
parametrization = {y*z^2-x^3,x*y*z,y^2*z,x^2*y,x*y^2,y^3};
phi = map(T,R,parametrization);
kernelIdeal = ker phi;
quadrics = {
    z4^2-z3*z5,
    z2*z4-z1*z5,
    z2*z3-z1*z4,
    z2^2-z3*z4-z0*z5,
    z1*z2-z3^2-z0*z4
    };
I = ideal quadrics;
scan(quadrics,q -> zeroCheck("quadratic vanishes in parametrization",phi q));
ck("five quadrics equal full elimination kernel",I == kernelIdeal);
ck("surface homogeneous dimension",dim(R/I) == 3);
ck("surface degree",degree(R/I) == 5);
ck("surface projectively saturated",saturate(I,ideal vars R) == I);
scan(0..8,n -> ck("degree-five genus-one Hilbert function",
    hilbertFunction(n,R/I) == 1+5*n*(n+1)//2));
modelResolution = res coker gens I;
ck("resolution length",length modelResolution == 3);
print modelResolution; print keys modelResolution; print(modelResolution#0); exit 0;
