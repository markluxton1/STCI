-- Independent identities for the endpoint a-nonzero inverse-support argument.
-- This source verifies polynomial identities; the projective support implication
-- and exhaustive common-root counting are proved in the accompanying audit.
CoefficientRing=QQ[a,b,g,d];
GeometryRing=CoefficientRing[z,T,r];
auditChecks=0;
auditCheck=(label,condition)->(
  if not condition then error("FAIL "|label);
  auditChecks=auditChecks+1;
  print("PASS "|label)
);
auditA=a*z-b;
auditU=2*a*z^3-3*b*z^2-z+g;
auditV=3*a*z^4-4*b*z^3-2*z^2-z+d;
auditH=a*z^3+z-g-1;
auditJ=auditA*auditV-(auditA*z-1)*auditU;
auditE=auditJ^2-(3*z*auditA-1)*auditH*auditJ+auditA*auditU*auditH^2;
auditCb=a^2*g-a*b-b^3;
auditDb=a^3*d-b^4-2*a*b^2-a^2*b-a^2;
auditX0=1+a*T;
auditX1=r+b*T;
auditX2=r^3+(g-r)*T;
auditX3=r^4+(d-r-2*r^2)*T+T^2;
auditP=auditU+auditA*(3*z*auditA-1)*T+auditA^3*T^2;
auditR=auditV+(6*z^2*auditA^2-4*z*auditA-auditA+1)*T
 +(4*z*auditA^3-2*auditA^2)*T^2+auditA^4*T^3;
auditCheck("target parameter equation",sub(auditX1-z*auditX0,{r=>z+auditA*T})==0);
auditCheck("target cube residual",sub(auditX2-z^3*auditX0,{r=>z+auditA*T})==T*auditP);
auditCheck("target fourth residual",sub(auditX3-z^4*auditX0,{r=>z+auditA*T})==T*auditR);
auditCheck("linear elimination identity",auditA*auditR-(auditA^2*T+auditA*z-1)*auditP==auditJ+auditA^2*auditH*T);
auditCheck("septic remainder identity",auditA*auditH^2*auditP-auditE==(auditA^2*auditH*T+auditJ)*(auditA^2*auditH*T-auditJ+(3*z*auditA-1)*auditH));
UnivariateRing=CoefficientRing[z];
univariateMap=map(UnivariateRing,GeometryRing,{z,0,0});
auditCheck("septic degree exactly seven generically",first degree univariateMap(auditE)==7);
auditCheck("septic leading coefficient a Cb",leadCoefficient univariateMap(auditE)==a*(a^2*g-a*b-b^3));
AuditFractionRing=(frac CoefficientRing)[z,T,r];
fractionMap=map(AuditFractionRing,GeometryRing,{z,T,r});
auditCheck("A-zero septic nonzero when Cb nonzero",sub(fractionMap(auditE),{z=>b/a})==-fractionMap(auditCb)/a^2);
auditCheck("X0-zero P excludes extraneous finite target",sub(fractionMap(auditP),{T=>-1/a})==fractionMap(auditCb)/a^2);
auditCheck("Cb-zero source endpoint X2",sub(fractionMap(auditX2),{r=>b/a,T=>-1/a})==-fractionMap(auditCb)/a^3);
auditCheck("Cb-zero source endpoint X3",sub(fractionMap(auditX3),{r=>b/a,T=>-1/a})==-fractionMap(auditDb)/a^4);
auditSpecial=sub(univariateMap(auditE),{b=>a-1/3,g=>a,d=>a+5/3});
auditCheck("special H-zero point septic divisible by square",auditSpecial % ideal(z-1)^2==0);
auditCheck("special H-zero point septic order exactly two",sub((auditSpecial // (z-1)^2),{z=>1})==1/9);
auditCheck("common-root H identity",auditH-(3*z^2*auditA-1)==-auditU);
auditCheck("A-zero U H identity",sub(fractionMap(auditU+auditH),{z=>b/a})==-1);
print("TOTAL "|toString auditChecks);
exit 0;
