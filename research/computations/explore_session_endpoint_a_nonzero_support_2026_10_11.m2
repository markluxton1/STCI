-- Exact exploratory coefficient strata; no universal parameter exhaustion claimed.
SupportRing=QQ[a,b,g,d,z,rho,k];
supA=a*z-b;
supU=2*a*z^3-3*b*z^2-z+g;
supV=3*a*z^4-4*b*z^3-2*z^2-z+d;
supH=a*z^3+z-g-1;
supJ=supA*supV-(supA*z-1)*supU;
supE=supJ^2-(3*z*supA-1)*supH*supJ+supA*supU*supH^2;
supAtRoot={g=>-2*a*rho^3+3*b*rho^2+rho,d=>-3*a*rho^4+4*b*rho^3+2*rho^2+rho};
supCoef=(poly,j)->(
  derived:=poly; denominator:=1;
  for i from 1 to j do (derived=diff(z,derived); denominator=denominator*i);
  sub(derived,{z=>rho})/denominator
);
for j from 1 to 7 do (
  cc=sub(supCoef(supE,j),supAtRoot);
  print("ROOTCOEF"|toString j|"="|toString factor cc);
  print("KROOTCOEF"|toString j|"="|toString factor sub(cc,{b=>a*rho-k}));
);
print("CUBICQUARTICDIV="|toString (supV % ideal supU));
print("SEPTICMODU="|toString (supE % ideal supU));
print("DEGENERATE="|toString factor sub(supE,{b=>a-1/3,g=>a,d=>a+5/3}));
exit 0;
