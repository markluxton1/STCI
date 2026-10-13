-- Structurally justified finite quartic/conductor incidence for Type2/3.
-- No unrestricted original-parameter elimination; delta remains arbitrary.
type2Polynomial=QQ[curveR,separation,familyRoot];
type2Ring=type2Polynomial/ideal(6*familyRoot^2-6*familyRoot+1);
tau=1/2;
uu=familyRoot*separation^2; ww=3*uu;
aa=2*uu+(separation-separation^2)/2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resE=-uu*ww+separation^4;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
resL=(-3*aa-uu)*separation^3-separation^4;
resN=aa*separation^4;
assert(resJ*rho+resE==0);
assert(-3*separation^2*rho^3+resP2*rho^2+resL*rho+resN==0);
quarticTnum=((resJ+3*separation^2)*curveR^2
 -(resP2-3*separation^2*rho)*curveR+(aa/tau)*separation^3);
normalP=((gg-3*bb+2*aa)*curveR^3
 +(6*separation*(bb-aa)+separation^3-3*separation^2)*curveR^2
 +(separation^2*(6*aa-3*bb)+2*separation^3)*curveR-2*aa*separation^3);
normalJ=((2*parD-3*gg+bb)*curveR^3
 +(3*separation*(gg-bb)+5*separation^3-3*separation^2)*curveR^2
 +(3*bb*separation^2+separation^3-separation^4)*curveR-bb*separation^3);
assert(diff(curveR,diff(curveR,diff(curveR,normalP)))==0);
assert(diff(curveR,diff(curveR,diff(curveR,normalJ)))==0);
type2Contact=saturate(ideal(normalP,normalJ,quarticTnum),ideal separation);
print "TYPE2 complete saturated finite quartic/conductor incidence";
print gens gb type2Contact;
print dim(type2Ring/type2Contact);
print degree(type2Ring/type2Contact);
print "TYPE2 normal pair and intrinsic quartic-contact polynomial";
print normalP; print normalJ; print quarticTnum;
assert(saturate(type2Contact,ideal(curveR))==type2Contact);
eta0=2*familyRoot-1;
type2Cubic=5*(separation+3*eta0)^2*(separation+3*eta0/5);
type2Linear=4*curveR-(3*eta0+2)*separation-1;
assert(type2Contact==ideal(type2Cubic,type2Linear));
print "TYPE2 exact incidence cubic and point relation";
print type2Cubic; print type2Linear;
print "PASS: Type2 factor, quadratic-degree and finite-chart incidence assertions";

type3Polynomial=QQ[curveR,separation,familyRoot,conicRoot];
type3Ring=type3Polynomial/ideal(6*conicRoot^2-6*conicRoot+1,
 3*familyRoot^2-6*conicRoot*familyRoot-1+3*conicRoot);
tau=conicRoot;
tauInverse=6*(1-tau);
assert(tau*tauInverse==1);
uu=familyRoot*separation^2; ww=3*uu;
aa=(6*tau-1)*uu+tau*separation-(3*tau-2/3)*separation^2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resE=-uu*ww+separation^4;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
resL=(-3*aa-uu)*separation^3-separation^4;
resN=aa*separation^4;
assert(resJ*rho+resE==0);
assert(-3*separation^2*rho^3+resP2*rho^2+resL*rho+resN==0);
quarticTnum=((resJ+3*separation^2)*curveR^2
 -(resP2-3*separation^2*rho)*curveR+aa*tauInverse*separation^3);
normalP=((gg-3*bb+2*aa)*curveR^3
 +(6*separation*(bb-aa)+separation^3-3*separation^2)*curveR^2
 +(separation^2*(6*aa-3*bb)+2*separation^3)*curveR-2*aa*separation^3);
normalJ=((2*parD-3*gg+bb)*curveR^3
 +(3*separation*(gg-bb)+5*separation^3-3*separation^2)*curveR^2
 +(3*bb*separation^2+separation^3-separation^4)*curveR-bb*separation^3);
assert(diff(curveR,diff(curveR,diff(curveR,normalP)))==0);
assert(diff(curveR,diff(curveR,diff(curveR,normalJ)))==0);
type3Contact=saturate(ideal(normalP,normalJ,quarticTnum),ideal separation);
print "TYPE3 complete saturated finite quartic/conductor incidence";
print gens gb type3Contact;
print dim(type3Ring/type3Contact);
print degree(type3Ring/type3Contact);
print "TYPE3 normal pair and intrinsic quartic-contact polynomial";
print normalP; print normalJ; print quarticTnum;
assert(saturate(type3Contact,ideal(curveR))==type3Contact);
type3Param=separation^2+(8*familyRoot-4*conicRoot-2)*separation+1;
assert(type3Param % type3Contact ==0);
print "TYPE3 parameter-only eliminated ideal";
polyContact=lift(type3Contact,type3Polynomial)+ideal(
 6*type3Polynomial_3^2-6*type3Polynomial_3+1,
 3*type3Polynomial_2^2-6*type3Polynomial_3*type3Polynomial_2-1+3*type3Polynomial_3);
parameterIdeal=substitute(eliminate(polyContact,{type3Polynomial_0}),type3Ring);
print gens gb parameterIdeal;
assert(parameterIdeal==ideal(type3Param));
print "PASS: Type3 factor, quadratic-degree and finite-chart incidence assertions";
