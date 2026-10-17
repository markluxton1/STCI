-- Targeted one-parameter family probe; no unrestricted parameter elimination.
numberRing=QQ[familyRoot];
numberField=toField(numberRing/ideal(2*familyRoot^2-2*familyRoot-1));
parameterRing=numberField[separation];
parameterField=frac parameterRing;
curveRing=parameterField[curveR];
uu=familyRoot*separation^2;
ww=(uu+4*separation^2)/3;
aa=(uu+ww+separation-separation^2)/2;
bb=aa-uu;
gg=aa-ww;
parD=aa-uu-ww;
rho=separation/2;
resJ=(3*uu+ww)*separation-3*separation^3;
resE=-uu*ww+separation^4;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
resL=(-3*aa-uu)*separation^3-separation^4;
resN=aa*separation^4;
assert(resJ*rho+resE==0);
assert(-3*separation^2*rho^3+resP2*rho^2+resL*rho+resN==0);
quarticT=(1+3*separation^2/resJ)*curveR^2
 -(resP2-3*separation^2*rho)*curveR/resJ+resN/(rho*resJ);
normalP=((gg-3*bb+2*aa)*curveR^3
 +(6*separation*(bb-aa)+separation^3-3*separation^2)*curveR^2
 +(separation^2*(6*aa-3*bb)+2*separation^3)*curveR-2*aa*separation^3);
normalJ=((2*parD-3*gg+bb)*curveR^3
 +(3*separation*(gg-bb)+5*separation^3-3*separation^2)*curveR^2
 +(3*bb*separation^2+separation^3-separation^4)*curveR-bb*separation^3);
print "TYPE 1 P,J generic gcd";
print gcd(normalP,normalJ);
print "TYPE 1 quartic-c contact at conic rho";
print substitute(quarticT,{curveR=>rho});
print "TYPE 1 normal P factor";
print factor normalP;
print "TYPE 1 normal J factor";
print factor normalJ;
print "TYPE 1 quartic-c contact polynomial";
print quarticT;
print "PASS: two exact factor-family assertions";
