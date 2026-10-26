-- Exploratory exact QQ line-plus-smooth-curve degeneration, 2026-10-25.
-- This checks this pair and its finite schemes, not all quartic pairs.
R=QQ[x0,x1,x2,x3];
curveIdeal=ideal(x0*x3-x1*x2,x1^3-x0^2*x2,
    x0*x2^2-x1^2*x3,x2^3-x1*x3^2);
lineIdeal=ideal(x0+x1,x2+x3);
quadric=x0*x3-x1*x2;
cubicLeft=x1^3-x0^2*x2;
cubicRight=x2^3-x1*x3^2;
fixedFirst=x1^4-x0^3*x3;
fixedSecond=x2^4-x0*x3^3;
perturbFirst=x0^2+x1^2+x2^2+x3^2+x0*x2+2*x1*x3;
perturbSecond=2*x0^2+3*x1^2+5*x2^2+7*x3^2+
    x0*x1+x0*x3+x1*x2+3*x2*x3;
f=fixedFirst+quadric*perturbFirst+x0*cubicLeft;
g=fixedSecond+quadric*perturbSecond+x3*cubicRight;
totalIdeal=ideal(f,g);
assert(codim totalIdeal==2);
assert(f%curveIdeal==0 and g%curveIdeal==0 and f%lineIdeal==0 and g%lineIdeal==0);
time residualIdeal=saturate(totalIdeal:curveIdeal);
time remainingIdeal=saturate(residualIdeal:lineIdeal);
assert(degree(R/residualIdeal)==12);
assert(degree(R/remainingIdeal)==11);
expectedPolynomial=-22*hilbertPolynomial(R/ideal(x0,x1,x2))+
    11*hilbertPolynomial(R/ideal(x0,x1));
assert(hilbertPolynomial(R/remainingIdeal)==expectedPolynomial);
assert(intersect(lineIdeal,remainingIdeal)==residualIdeal);
assert(intersect(curveIdeal,residualIdeal)==totalIdeal);
print "Residual D = L union E scheme-theoretically; degree(E)=11, p_a(E)=12: PASS";

time singularRemaining=saturate(remainingIdeal+minors(2,jacobian gens remainingIdeal));
assert(singularRemaining==ideal(1_R));
time remainingSections=HH^0 sheaf(R/remainingIdeal);
assert(ring remainingSections===QQ and rank remainingSections==1);
print "E projectively smooth over QQ, H0(O_E)=QQ; hence geometrically integral: PASS";

time lineAttachment=saturate(lineIdeal+remainingIdeal);
assert(dim(R/lineAttachment)==1 and degree(R/lineAttachment)==5);
assert(saturate(lineAttachment+minors(3,jacobian gens lineAttachment))==ideal(1_R));
time curveAttachment=saturate(curveIdeal+remainingIdeal);
assert(dim(R/curveAttachment)==1 and degree(R/curveAttachment)==17);
assert(saturate(curveAttachment+minors(3,jacobian gens curveAttachment))==ideal(1_R));
assert(degree(R/saturate(curveIdeal+lineIdeal))==1);
assert(saturate(curveIdeal+lineIdeal+remainingIdeal)==ideal(1_R));
print "L meets E in5 simple points, C meets E in17 simple points, C meets L in1 point; no triple: PASS";

-- Independent degree-five equation of L intersection E in line coordinates [-r:r:-s:s].
T=QQ[r,s];
lineMap=map(T,R,{-r,r,-s,s});
quintic=4*r^5-2*r^4*s+9*r^3*s^2+2*r^2*s^3+3*r*s^4+2*s^5;
assert(saturate(lineMap(lineAttachment),ideal(r,s))==ideal(quintic));
assert(saturate(ideal(quintic,diff(r,quintic),diff(s,quintic)),ideal(r,s))==ideal(1_T));
assert(sub(quintic,{r=>-1,s=>1})==-14);
print "Quintic intersection equation, geometric squarefreeness, no shared C point: PASS";

-- First-normal matrix to L and its six-point attachment determinant.
normalF0=lineMap(diff(x0,f)); normalF1=lineMap(diff(x2,f));
normalG0=lineMap(diff(x0,g)); normalG1=lineMap(diff(x2,g));
normalMatrix=matrix{{normalF0,normalF1},{normalG0,normalG1}};
print("First-normal matrix on L: ",normalMatrix);
lineDet=det normalMatrix;
print("Line determinant: ",factor lineDet);
assert(lineDet==-(r+s)*quintic);
assert(lineMap(fixedFirst+x0*cubicLeft)==0);
assert(lineMap(fixedSecond+x3*cubicRight)==0);
print "L occurs exactly at parameter(a,b)=(1,1); normal determinant=-(r+s)*quintic: PASS";
-- The two normal parameter directions induce the same local smoothing class
-- at every one of the five residual nodes, up to a nonzero scalar.
assert(-normalG1*r^3==r*quintic+normalF1*s^3);
assert(saturate(ideal(quintic,normalF1),ideal(r,s))==ideal(1_T));
assert(saturate(ideal(quintic,r*s*(r+s)*(r+2*s)),ideal(r,s))==ideal(1_T));
print "All five residual nodes have nonzero first smoothing class proportional to da+db: PASS";
print "EXACT QQ LINE DEGENERATION CHECKS PASSED";
