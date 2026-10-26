-- Exact characteristic-zero benchmark: a smooth residual curve through the fixed C.
-- Run: /opt/homebrew/bin/M2 --script research/computations/verify_ci_smooth_residual_example_2026_10_25.m2
-- This checks one documented homogeneous QQ pair, not a genericity theorem or
-- a classification. There is no random choice and no finite-field lifting step.

R=QQ[x0,x1,x2,x3];
curveIdeal=ideal(x0*x3-x1*x2,x1^3-x0^2*x2,
    x0*x2^2-x1^2*x3,x2^3-x1*x3^2);
quadric=x0*x3-x1*x2;
cubicLeft=x1^3-x0^2*x2;
cubicRight=x2^3-x1*x3^2;
fixedFirst=x1^4-x0^3*x3;
fixedSecond=x2^4-x0*x3^3;
perturbFirst=x0^2+x1^2+x2^2+x3^2+x0*x2+2*x1*x3;
perturbSecond=2*x0^2+3*x1^2+5*x2^2+7*x3^2+
    x0*x1+x0*x3+x1*x2+3*x2*x3;
f=fixedFirst+quadric*perturbFirst+2*x0*cubicLeft;
g=fixedSecond+quadric*perturbSecond+3*x3*cubicRight;
totalIdeal=ideal(f,g);
assert(f%curveIdeal==0 and g%curveIdeal==0);
assert(codim totalIdeal==2);
print "Actual homogeneous quartics vanish on C; proper (4,4) intersection: PASS";

time residualIdeal=saturate(totalIdeal:curveIdeal);
assert(dim(R/residualIdeal)==2);
assert(degree(R/residualIdeal)==12);
-- M2 uses P_0(n)=1 and P_1(n)=n+1, so -27P_0+12P_1=12n-15.
expectedPolynomial=-27*hilbertPolynomial(R/ideal(x0,x1,x2))+
    12*hilbertPolynomial(R/ideal(x0,x1));
assert(hilbertPolynomial(R/residualIdeal)==expectedPolynomial);
assert(intersect(curveIdeal,residualIdeal)==totalIdeal);
print "Residual degree 12, Hilbert polynomial 12n-15, exact scheme union C union D: PASS";
print("Residual generators: ",degrees source gens residualIdeal);

time residualSingularIdeal=saturate(residualIdeal+
    minors(2,jacobian gens residualIdeal));
assert(residualSingularIdeal==ideal(1_R));
print "Residual projective Jacobian singular scheme empty over QQ: PASS";

time attachmentIdeal=saturate(residualIdeal+curveIdeal);
assert(dim(R/attachmentIdeal)==1);
assert(degree(R/attachmentIdeal)==18);
time attachmentSingularIdeal=saturate(attachmentIdeal+
    minors(3,jacobian gens attachmentIdeal));
assert(attachmentSingularIdeal==ideal(1_R));
assert(saturate(attachmentIdeal+ideal(x1,x2,x3))==ideal(1_R));
assert(saturate(attachmentIdeal+ideal(x0,x1,x2))==ideal(1_R));
print "Attachment has 18 geometric reduced points; neither distinguished endpoint occurs: PASS";

time residualSections=HH^0 sheaf(R/residualIdeal);
assert(ring residualSections===QQ);
assert(rank residualSections==1);
-- dim residualSections is Krull dimension 0, not its QQ-vector-space dimension.
print "H0(O_D)=QQ: rank 1 over QQ: PASS";
print "By geometric smoothness and H0 base change, D is geometrically integral.";
print "EXACT QQ SMOOTH RESIDUAL BENCHMARK PASSED";
