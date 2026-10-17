-- Exact algebra for the endpoint family U | V, with parameter b nonzero.
-- This script checks univariate support; it does not alone prove geometry.
ThreeParameterRing=QQ[bb];
ThreeField=frac ThreeParameterRing;
threeInverseB=1/bb;
threeA=3*bb^2/2;
threeG=threeInverseB/9-2/3;
threeD=threeInverseB^2/54-threeInverseB/9;
ThreeRing=ThreeField[xx];
threeZ=(xx+1)*threeInverseB/3;
threeU=2*threeA*threeZ^3-3*bb*threeZ^2-threeZ+threeG;
threeV=3*threeA*threeZ^4-4*bb*threeZ^3-2*threeZ^2-threeZ+threeD;
threeLin=threeA*threeZ-bb;
threeH=threeA*threeZ^3+threeZ-threeG-1;
threeJ=threeLin*threeV-(threeLin*threeZ-1)*threeU;
threeE=threeJ^2-(3*threeZ*threeLin-1)*threeH*threeJ+threeLin*threeU*threeH^2;
threeS=threeE//threeU;
assert(threeV%threeU==0);
assert(threeE%threeU==0);
print("U = "|toString threeU);
print("V/U = "|toString(threeV//threeU));
print("S = "|toString threeS);
print("scaled S = "|toString(216*bb*threeS));
print("Cb = "|toString(threeA^2*threeG-threeA*bb-bb^3));
print("remainder S mod U = "|toString(threeS%threeU));
assert(432*bb*threeS==-(4*bb+6)*xx^4-(14*bb+9)*xx^3-48*bb*xx^2+(24*bb^2-26*bb+15)*xx-24*bb^2-340*bb);
-- Independent resultant computation after x = 3*b*z - 1.
ThreeIntegralBase=QQ[bp];
ThreeIntegralRing=ThreeIntegralBase[xp];
threeP=xp^3-6*xp-6*bp-4;
threeQ=-(4*bp+6)*xp^4-(14*bp+9)*xp^3-48*bp*xp^2+(24*bp^2-26*bp+15)*xp-24*bp^2-340*bp;
threeSylvester=(ff,gg,nn,mm,vv)->det matrix apply(nn+mm,rr->apply(nn+mm,cc->(
    if rr<mm then (
        kk:=nn-cc+rr;
        if kk<0 or kk>nn then 0_ThreeIntegralRing else coefficient(vv^kk,ff)
    ) else (
        kk:=mm-cc+rr-mm;
        if kk<0 or kk>mm then 0_ThreeIntegralRing else coefficient(vv^kk,gg)
    )
)));
threeResultant=threeSylvester(threeP,threeQ,3,4,xp);
threeDerivativeResultant=threeSylvester(threeQ,diff(xp,threeQ),4,3,xp);
threeR=(12*bp^2+116*bp+3)*(72*bp^4+252*bp^3+1126*bp^2+513*bp+54);
threeDpoly=(2*bp+3)*(2*bp^2+9*bp+15)^2*(9216*bp^6-208896*bp^5-2002096*bp^4-2800992*bp^3-117672*bp^2+72*bp+45);
print("resultant shifted U,S = "|toString factor threeResultant);
print("resultant shifted S,S' = "|toString factor threeDerivativeResultant);
print("quotient resultant / R = "|toString(threeResultant//threeR));
print("quotient derivative resultant / D = "|toString(threeDerivativeResultant//threeDpoly));
assert(threeResultant%threeR==0);
assert(threeDerivativeResultant%threeDpoly==0);
assert(gcd(lift(threeR,ThreeIntegralBase),lift(threeDpoly,ThreeIntegralBase))==1);
print("PASS corrected U|V family: resultant parameter factors have gcd 1; no allowed full-support parameter.");
