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
hh = a*z^3+z-c-1;
vv = aa*rzero-(aa*z-1)*pzero;
ee = vv^2-(3*z*aa-1)*hh*vv+aa*pzero*hh^2;
checks = 0;
check = (label,value) -> (
  if not value then error("FAIL " | label);
  checks = checks+1;
  print("PASS " | label);
  );
check("linear remainder",aa*rr-(aa^2*T+aa*z-1)*pp == aa^2*hh*T+vv);
check("off-curve x2 relation",sub((z+aa*T)^3+(c-z-aa*T)*T-z^3*(1+a*T),R) == T*pp);
check("off-curve x3 relation",sub((z+aa*T)^4+(d-2*(z+aa*T)^2-z-aa*T)*T+T^2-z^4*(1+a*T),R) == T*rr);
print("E=" | toString ee);
print("EDEGREE=" | toString degree(z,ee));
for j from 0 to 10 do print("COEFF" | toString j | "=" | toString coefficient(z^j,ee));
print("ETO=" | toString sub(ee,{a=>0,b=>0}));
check("A0 resultant boundary",sub(ee,{b=>a*z}) == -sub(pzero,{b=>a*z}));
-- Numerator of 1+aT after the unique off-curve root T=-v/(A^2 h).
ww = aa^2*hh-a*vv;
print("BOUNDARYNUMERATOR=" | toString ww);
print("E_AT_V0=" | toString (ee % ideal(vv)));
print("E_AT_W0=" | toString (ee % ideal(ww)));
print("CHECKS=" | toString checks);
exit 0;
