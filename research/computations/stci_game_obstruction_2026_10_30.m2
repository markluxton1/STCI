-- Geometric control for an x-dependent sextic outside k[q,c0,c2].
-- No inherited fixed-carrier or jet certificate is rerun.
R=QQ[symbol t,symbol u,symbol q];
cc0=-u;
cc2=(t^3+u)^3-t*(t^4+t*u+q)^2;
ff=cc0^2+cc2^2+q*cc0;
f2=4*t^10*q^2+(-4*t^11-1)*q*u+(1+t^12)*u^2;
assert(all(terms(ff-f2),term->(
    termExponent=first exponents term;
    termExponent#1+termExponent#2>=3)));
discActual=(-4*t^11-1)^2-16*t^10*(1+t^12);
assert(discActual==1+8*t^11-16*t^10);
assert(first degree discActual==11);
assert(gcd(4*t^11+1,t^12+1)==1_R);
print "NONSPLIT_GENERIC_NORMAL_COVER_AND_ORDINARY_ATTACHMENTS_PASS";
T=QQ[symbol lt,symbol w,symbol lq];
mapAffine=map(T,R,{lt,w-lt^3,lq});
assert(sub(mapAffine ff,{lq=>0})==(w-lt^3)^2*(w^4+1));
Z0=QQ[symbol zt,symbol zz,symbol zq];
Z=Z0/ideal(zz^4+1);
mapLine=map(Z,T,{zt,zz,zq});
assert(sub(mapLine mapAffine ff,{zq=>0})==0);
assert(sub(mapLine diff(w,sub(mapAffine ff,{lq=>0})),{zq=>0})
       ==4*zz^3*(zz-zt^3)^2);
print "ACTUAL_QUADRIC_RESIDUAL_LINES_AND_GENERIC_SMOOTHNESS_PASS";
assert(2*(3)^2-7*3+8==5);
print "TEST_CURVE_DEGREE_GAP_IDENTITIES_PASS";
print "GAME_OBSTRUCTION_GEOMETRIC_CONTROLS_PASS";
