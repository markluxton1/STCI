-- Targeted one-parameter family probe; no unrestricted parameter elimination.
polynomialRing=QQ[curveR,separation,familyRoot];
curveRing=polynomialRing/ideal(2*familyRoot^2-2*familyRoot-1);
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
quarticTnum=((resJ+3*separation^2)*curveR^2
 -(resP2-3*separation^2*rho)*curveR+2*aa*separation^3);
normalP=((gg-3*bb+2*aa)*curveR^3
 +(6*separation*(bb-aa)+separation^3-3*separation^2)*curveR^2
 +(separation^2*(6*aa-3*bb)+2*separation^3)*curveR-2*aa*separation^3);
normalJ=((2*parD-3*gg+bb)*curveR^3
 +(3*separation*(gg-bb)+5*separation^3-3*separation^2)*curveR^2
 +(3*bb*separation^2+separation^3-separation^4)*curveR-bb*separation^3);
assert(substitute(normalP,{curveR=>rho})==0);
assert(substitute(normalJ,{curveR=>rho})==0);
pq=normalP//(curveR-rho);
jq=normalJ//(curveR-rho);
assert(normalP==(curveR-rho)*pq);
assert(normalJ==(curveR-rho)*jq);
cp2=substitute(diff(curveR,diff(curveR,pq)),{curveR=>0})/2;
cp1=substitute(diff(curveR,pq),{curveR=>0});
cp0=substitute(pq,{curveR=>0});
cj2=substitute(diff(curveR,diff(curveR,jq)),{curveR=>0})/2;
cj1=substitute(diff(curveR,jq),{curveR=>0});
cj0=substitute(jq,{curveR=>0});
assert(pq==cp2*curveR^2+cp1*curveR+cp0);
assert(jq==cj2*curveR^2+cj1*curveR+cj0);
quadraticRes=det matrix{{cp2,cp1,cp0,0},{0,cp2,cp1,cp0},
 {cj2,cj1,cj0,0},{0,cj2,cj1,cj0}};
print "TYPE 1 residual homogeneous quadratic resultant";
print quadraticRes;
print "TYPE 1 quartic-c contact at conic rho";
print substitute(quarticTnum,{curveR=>rho});
print "TYPE 1 normal P quotient";
print pq;
print "TYPE 1 normal J quotient";
print jq;
print "TYPE 1 quartic-c contact polynomial";
print quarticTnum;
print "PASS: eight exact factor-family, common-root, and coefficient assertions";
