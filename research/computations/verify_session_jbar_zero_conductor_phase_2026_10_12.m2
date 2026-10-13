-- Exact supporting identities for a written conductor proof.
-- This does not calculate the conductor or prove geometric coverage.
R=QQ[aa,bb,gg,parD,sepD,al,be,ch,wh,rr];
localH=be+ch;
localDZ=al*be-ch^2;
localEZ=be^2-al*be*ch+ch^3;
localRel=be*(al^2-ch)-al*ch^2;
proj0=1-al+aa*localH;
proj1=1+(sepD-1)*al+bb*localH;
proj2=1+(3*sepD-1)*al+3*sepD^2*ch-sepD^3*localDZ+gg*localH;
proj3=1+(4*sepD-1)*al+6*sepD^2*ch-4*sepD^3*localDZ+sepD^4*localEZ+parD*localH;
ee=gg-3*bb+2*aa;
jb=parD-2*gg+2*bb-aa;
assert(proj1-proj0==sepD*al+(bb-aa)*localH);
assert(proj2-3*proj1+2*proj0==ee*localH+3*sepD^2*ch-sepD^3*localDZ);
assert(proj3-2*proj2+2*proj1-proj0==jb*localH+sepD^4*localEZ-2*sepD^3*localDZ);
print "PASS 1: three exact target ideal row operations";
linearKernel={al=>-3*sepD*(bb-aa)*wh,be=>(ee+3*sepD^2)*wh,ch=>-ee*wh};
assert(substitute(sepD*al+(bb-aa)*localH,linearKernel)==0);
assert(substitute(ee*localH+3*sepD^2*ch,linearKernel)==0);
assert(substitute(localH,linearKernel)==3*sepD^2*wh);
print "PASS 2: the exact linear kernel with nonzero scaled h coordinate";
kernelRelation=substitute(localRel,linearKernel);
assert(kernelRelation % ideal(wh^3)==ee*(ee+3*sepD^2)*wh^2);
assert(substitute(localDZ,linearKernel) % ideal(wh^2)==0);
assert(substitute(localEZ,linearKernel) % ideal(wh^2)==0);
print "PASS 3: actual A4 quadratic coefficient and no third-generator linear term";
pv=((gg-3*bb+2*aa)*rr^3
 +(6*sepD*(bb-aa)+sepD^3-3*sepD^2)*rr^2
 +(sepD^2*(6*aa-3*bb)+2*sepD^3)*rr-2*aa*sepD^3);
ju=((2*parD-3*gg+bb)*rr^3
 +(3*sepD*(gg-bb)+5*sepD^3-3*sepD^2)*rr^2
 +(3*bb*sepD^2+sepD^3-sepD^4)*rr-bb*sepD^3);
assert(coefficient(rr^3,pv)==ee);
assert(substitute(coefficient(rr^3,ju),{parD=>2*gg-2*bb+aa})==ee);
print "PASS 4: both cubic leading coefficients equal E on Jbar zero";
lineR1=gg+3*sepD^2+2*aa-3*bb;
lineR2=parD+6*sepD^2+3*aa-4*bb;
assert(lineR1==ee+3*sepD^2);
assert(substitute(lineR2,{parD=>2*gg-2*bb+aa})==2*(ee+3*sepD^2));
print "PASS 5: exceptional E value is exactly both line rank-drop equations";
L=QQ[cA,cB,cC,cD,cF,cG,curveR,curveT,curveV];
lowPolynomial=cA*curveV+cB*curveR*curveT+cC*curveR^2+cD*curveT+cF*curveR+cG;
lowRestriction=substitute(lowPolynomial,{curveT=>-curveR^2,curveV=>curveR^4-curveR^3});
assert(lowRestriction==cA*curveR^4+(-cA-cB)*curveR^3+(cC-cD)*curveR^2+cF*curveR+cG);
assert(substitute(lowPolynomial,{cA=>0,cB=>0,cF=>0,cC=>cD})==cD*(curveT+curveR^2)+cG);
print "PASS 6: exhaustive low-pole basis restriction and constant-restriction kernel";
exampleP=substitute(pv,{sepD=>1,aa=>1,bb=>0,gg=>0,parD=>1});
exampleJ=substitute(ju,{sepD=>1,aa=>1,bb=>0,gg=>0,parD=>1});
assert(exampleP==2*(rr^3-4*rr^2+4*rr-1));
assert(exampleJ==2*rr^2*(rr+1));
assert(substitute(exampleP,{rr=>0})==-2 and substitute(exampleP,{rr=>-1})==-20);
assert(substitute(jb,{aa=>1,bb=>0,gg=>0,parD=>1})==0);
assert(substitute(ee,{aa=>1,bb=>0,gg=>0,parD=>1})==2);
print "PASS 7: coprime homogeneous-cubic example on Jbar zero (no admissibility assertion)";
print "PASS ALL: seven supporting exact conditions; no parameter-space exhaustion";
