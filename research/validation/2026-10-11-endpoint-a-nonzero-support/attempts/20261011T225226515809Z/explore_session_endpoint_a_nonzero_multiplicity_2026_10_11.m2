-- Rational one-parameter analysis of exact target septic contact order.
OriginalRing=QQ[a,b,g,d,z,rho];
targetA=a*z-b;
targetU=2*a*z^3-3*b*z^2-z+g;
targetV=3*a*z^4-4*b*z^3-2*z^2-z+d;
targetH=a*z^3+z-g-1;
targetJ=targetA*targetV-(targetA*z-1)*targetU;
targetE=targetJ^2-(3*z*targetA-1)*targetH*targetJ+targetA*targetU*targetH^2;
targetCoef=(poly,j)->(
  derived:=poly; denominator:=1;
  for i from 1 to j do (derived=diff(z,derived); denominator=denominator*i);
  sub(derived,{z=>rho})/denominator
);
ParameterRing=QQ[q];
ParameterField=frac ParameterRing;
OrderRing=ParameterField[alpha];
parameterK=2-2*q-1/(3*q);
parameterRho=q/parameterK;
contactMap=map(OrderRing,OriginalRing,{
 alpha,alpha*parameterRho-parameterK,
 alpha*parameterRho^3-3*parameterK*parameterRho^2+parameterRho,
 alpha*parameterRho^4-4*parameterK*parameterRho^3+2*parameterRho^2+parameterRho,
 parameterRho,parameterRho
});
contactCoeffs=apply(toList(1..7),j->contactMap(targetCoef(targetE,j)));
print("COEFF1="|toString contactCoeffs#0);
print("COEFF2="|toString factor contactCoeffs#1);
linearA=lift(diff(alpha,contactCoeffs#1),ParameterField);
linearB=lift(sub(contactCoeffs#1,{alpha=>0}),ParameterField);
print("A2="|toString linearA);
print("B2="|toString linearB);
solvedA=-linearB/linearA;
print("SOLVEDA="|toString solvedA);
for j from 2 to 6 do print("SOLVEDCOEF"|toString (j+1)|"="|toString factor sub(contactCoeffs#j,{alpha=>solvedA}));
print("DONE EXACT RATIONAL CONTACT EXPLORATION");
exit 0;
