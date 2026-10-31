-- Independent target-septic local contact audit; characteristic zero.
-- No global geometric interpretation is asserted by this source.
OriginalRing=QQ[a,b,g,d,z,rho];
targetA=a*z-b;
targetU=2*a*z^3-3*b*z^2-z+g;
targetV=3*a*z^4-4*b*z^3-2*z^2-z+d;
targetH=a*z^3+z-g-1;
targetJ=targetA*targetV-(targetA*z-1)*targetU;
targetE=targetJ^2-(3*z*targetA-1)*targetH*targetJ+targetA*targetU*targetH^2;
targetCb=a^2*g-a*b-b^3;
checkCount=0;
checkExact=(truth,label)->(
  if not truth then error ("FAIL: "|label);
  checkCount=checkCount+1;
  print("PASS: "|label)
);
coefficientAt=(poly,j)->(
  derivative:=poly; denominator:=1;
  for i from 1 to j do (derivative=diff(z,derivative); denominator=denominator*i);
  sub(derivative,{z=>rho})/denominator
);
checkExact(coefficientAt(targetE,8)==0 and coefficientAt(targetE,7)==a*targetCb,"target septic has leading coefficient a Cb");
LocalRing=QQ[alpha,w,p];
commonMap=map(LocalRing,OriginalRing,{
 alpha,alpha*p-w,alpha*p^3-3*w*p^2+p,
 alpha*p^4-4*w*p^3+2*p^2+p,p,p
});
localH=3*w*p^2-1;
localS2=6*w^2*p^2-6*w*p+1+3*w^2*p;
checkExact(commonMap(targetU)==0 and commonMap(targetV)==0,"common root parameterization");
checkExact(commonMap(targetCb)==w*(alpha*(1-3*w*p)+w^2),"Cb at common root");
checkExact(commonMap(coefficientAt(targetE,1))==-localH*localS2,"target septic first coefficient");
-- At z=p the target residual equations have F=w*T*(-1+3wp+w^2T).
FiberRing=frac(LocalRing)[tt];
fiberF=w*tt*(-1+3*w*p+w^2*tt);
fiberG=tt*((6*w^2*p^2-4*w*p-w+1)+(4*p*w^3-2*w^2)*tt+w^4*tt^2);
extraT=(1-3*w*p)/w^2;
checkExact(sub(fiberF,{tt=>extraT})==0,"exceptional H fiber satisfies F");
checkExact(sub(fiberG,{tt=>extraT})==extraT*w*localH,"exceptional H fiber satisfies G exactly when H vanishes");
specialMap=map(QQ[alpha],LocalRing,{alpha,1/3,1});
checkExact(specialMap(commonMap(coefficientAt(targetE,2)))==1/9,"q=1/3 exceptional contact has order two");
ParameterRing=QQ[q];
ParameterField=frac ParameterRing;
OrderRing=ParameterField[alpha];
discQ=6*q^2-6*q+1;
parameterW=-discQ/(3*q);
parameterRho=q/parameterW;
contactMap=map(OrderRing,OriginalRing,{
 alpha,alpha*parameterRho-parameterW,
 alpha*parameterRho^3-3*parameterW*parameterRho^2+parameterRho,
 alpha*parameterRho^4-4*parameterW*parameterRho^3+2*parameterRho^2+parameterRho,
 parameterRho,parameterRho
});
contactCoeffs=apply(toList(1..7),j->contactMap(coefficientAt(targetE,j)));
checkExact(contactCoeffs#0==0,"rational parameterization sets first coefficient to zero");
linearA=lift(diff(alpha,contactCoeffs#1),ParameterField);
linearB=lift(sub(contactCoeffs#1,{alpha=>0}),ParameterField);
checkExact(linearA!=0 and diff(alpha,diff(alpha,contactCoeffs#1))==0,"second coefficient is nonconstant linear in a");
checkExact(linearA==-3*q*(3*q-1)^2*(3*q^2+3*q-1)/discQ^2,"second coefficient a slope vanishes only on excluded or order-two strata");
solvedA=-linearB/linearA;
quarticQ=54*q^4-72*q^3+15*q^2-3*q+1;
checkExact(solvedA==-discQ^2*quarticQ/(27*q^3*(3*q-1)^2),"exact solved a at contact order at least three");
solvedCoeffs=apply(contactCoeffs,c->lift(sub(c,{alpha=>solvedA}),ParameterField));
checkExact(solvedCoeffs#1==0,"solved a kills second coefficient");
thirdNumerator=numerator solvedCoeffs#2;
fourthNumerator=numerator solvedCoeffs#3;
thirdFourthGcd=gcd(thirdNumerator,fourthNumerator);
checkExact(degree thirdFourthGcd=={2} and discQ%thirdFourthGcd==0,"third and fourth coefficient common zeros occur only at D=0");
-- Sylvester determinant for the two quotients U/(z-rho), V/(z-rho).
otherB=solvedA*parameterRho-parameterW;
qu2=2*solvedA;
qu1=2*solvedA*parameterRho-3*otherB;
qu0=2*solvedA*parameterRho^2-3*otherB*parameterRho-1;
qv3=3*solvedA;
qv2=3*solvedA*parameterRho-4*otherB;
qv1=3*solvedA*parameterRho^2-4*otherB*parameterRho-2;
qv0=3*solvedA*parameterRho^3-4*otherB*parameterRho^2-2*parameterRho-1;
otherSylvester=matrix {
 {qu2,qu1,qu0,0,0}, {0,qu2,qu1,qu0,0}, {0,0,qu2,qu1,qu0},
 {qv3,qv2,qv1,qv0,0}, {0,qv3,qv2,qv1,qv0}
};
otherResultant=det otherSylvester;
otherGcd=gcd(thirdNumerator,numerator otherResultant);
checkExact(degree otherGcd=={2} and discQ%otherGcd==0,"order-four contact permits no additional common root, including a repeated root");
print("THIRD_NUMERATOR="|toString factor thirdNumerator);
print("FOURTH_NUMERATOR="|toString factor fourthNumerator);
print("THIRD_COEFFICIENT="|toString factor solvedCoeffs#2);
print("FOURTH_COEFFICIENT="|toString factor solvedCoeffs#3);
print("OTHER_RESULTANT="|toString factor otherResultant);
print("PASS_COUNT="|toString checkCount);
exit 0;
