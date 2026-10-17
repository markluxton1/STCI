-- Endpoint A4 projection only. Exact coefficient reduction, not exhaustion.
R = QQ[a,b,c,d,z,T];
aa = a*z-b;
pzero = 2*a*z^3-3*b*z^2-z+c;
pone = 3*z*aa^2-aa;
ptwo = aa^3;
rzero = 3*a*z^4-4*b*z^3-2*z^2-z+d;
rone = 6*z^2*aa^2-4*z*aa-aa+1;
rtwo = 4*z*aa^3-2*aa^2;
rthree = aa^4;
pp = pzero+pone*T+ptwo*T^2;
rr = rzero+rone*T+rtwo*T^2+rthree*T^3;
endpointH = a*z^3+z-c-1;
endpointV = aa*rzero-(aa*z-1)*pzero;
endpointE = endpointV^2-(3*z*aa-1)*endpointH*endpointV+aa*pzero*endpointH^2;
checks = 0;
endpointAssert = (label,value) -> (
  if not value then error("FAIL " | label);
  checks = checks+1;
  print("PASS " | label);
  );
endpointAssert("linear remainder",aa*rr-(aa^2*T+aa*z-1)*pp == aa^2*endpointH*T+endpointV);
endpointAssert("off-curve x2 relation",sub((z+aa*T)^3+(c-z-aa*T)*T-z^3*(1+a*T),R) == T*pp);
endpointAssert("off-curve x3 relation",sub((z+aa*T)^4+(d-2*(z+aa*T)^2-z-aa*T)*T+T^2-z^4*(1+a*T),R) == T*rr);
print("E=" | toString endpointE);
endpointCoef = (poly,j) -> (
  differentiated := poly;
  factorialInteger := 1;
  for k from 1 to j do (
    differentiated = diff(z,differentiated);
    factorialInteger = factorialInteger*k;
    );
  sub(differentiated,{z=>0})/factorialInteger
  );
endpointAssert("degree seven leading coefficient", endpointCoef(endpointE,7) == a*(a^2*c-a*b-b^3));
endpointAssert("degree six coefficient", endpointCoef(endpointE,6) == -(a^3*d-a^2*b-2*a*b^2-b^4-a^2));
endpointAssert("degree above seven vanishes", all(toList(8..10),j -> endpointCoef(endpointE,j) == 0));
print("EDEGREE=" | toString max select(toList(0..10), j -> endpointCoef(endpointE,j) != 0));
for j from 0 to 7 do print("COEFF" | toString j | "=" | toString endpointCoef(endpointE,j));
print("ETO=" | toString sub(endpointE,{a=>0,b=>0}));
endpointAssert("A0 resultant boundary",sub(endpointE,{b=>a*z}) == -sub(pzero,{b=>a*z}));
-- Numerator of 1+aT after the unique off-curve root T=-v/(A^2 h).
endpointW = aa^2*endpointH-a*endpointV;
print("BOUNDARYNUMERATOR=" | toString endpointW);
print("E_AT_V0=" | toString (endpointE % ideal(endpointV)));
print("E_AT_W0=" | toString (endpointE % ideal(endpointW)));
print("CHECKS=" | toString checks);
exit 0;
