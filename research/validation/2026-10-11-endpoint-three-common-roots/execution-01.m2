-- Exact algebra for the endpoint family U | V, with parameter b nonzero.
-- This script checks univariate support; it does not alone prove geometry.
ThreeParameterRing=QQ[bb];
ThreeField=frac ThreeParameterRing;
ThreeRing=ThreeField[xx];
threeA=-3*bb^2/2;
threeG=1/(9*bb)-2/3;
threeD=1/(54*bb^2)-1/(9*bb);
threeZ=(xx-1)/(3*bb);
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
print("gcd generic = "|toString gcd(threeS,threeU));
print("discriminant U = "|toString discriminant(threeU,xx));
