-- Uniform identities for the entire five-parameter order-two slice.
-- No parameter is specialized, inverted, or sampled.
P=QQ[gamma,h0,h1,h2,h3];
S=P[a,y,d,z];
relation=ideal(a*d-y^2+z^2/4);
U={a^2+h0*z^2,
   a*(y+gamma*z)+h1*z^2,
   d*(y-gamma*z)+h2*z^2,
   d^2+h3*z^2};
residual=((gamma^2-1/4)*a*d+h3*a^2+h0*d^2
          -h2*a*(y+gamma*z)-h1*d*(y-gamma*z)
          +(h0*h3-h1*h2)*z^2);
assert((U#0*U#3-U#1*U#2-z^2*residual)%relation==0);
print "FIVE_PARAMETER_DETERMINANT_IDENTITY_PASS";

T=P[Y,Z];
-- First-normal coefficient along the entire a=1 diagonal chart.
chart0=map(T,S,{1,Y,Y^2-Z^2/4,Z});
Uchart=apply(U,u->chart0 u);
curveCubic0=(Uchart#0)^2*(Uchart#2)-(Uchart#1)^3;
assert(coefficient(Z,curveCubic0)==-4*gamma*Y^2);
print "FIRST_NORMAL_COEFFICIENT_IS_MINUS_FOUR_GAMMA_Y_SQUARED";

-- At p0, h3=0. Nonzero h2 is forced separately by endpoint fibers.
-- These congruences prove smoothness and exact contact when h2 is nonzero.
r0=sub(chart0 residual,{h3=>0});
c0=sub(curveCubic0,{h3=>0});
maximal=ideal(Y,Z);
assert((r0+h2*(Y+gamma*Z))%(maximal^2)==0);
assert((c0-h2*Z^2)%(maximal^3)==0);
print "P0_RESIDUAL_TANGENT_AND_EXACT_CONTACT_TWO_PASS";

-- At pInfinity, h0=0 and nonzero h1 is forced by endpoint fibers.
chartInfinity=map(T,S,{Y^2-Z^2/4,Y,1,Z});
Uinfinity=apply(U,u->chartInfinity u);
curveCubicInfinity=(Uinfinity#2)^3-(Uinfinity#1)*(Uinfinity#3)^2;
rInfinity=sub(chartInfinity residual,{h0=>0});
cInfinity=sub(curveCubicInfinity,{h0=>0});
assert((rInfinity+h1*(Y-gamma*Z))%(maximal^2)==0);
assert((cInfinity+h1*Z^2)%(maximal^3)==0);
print "P_INFINITY_RESIDUAL_TANGENT_AND_EXACT_CONTACT_TWO_PASS";

-- The endpoint fiber coefficients cannot both vanish: their difference is one.
assert((gamma+1/2)-(gamma-1/2)==1);
assert((1/2-gamma)-(-1/2-gamma)==1);
print "ALL_ENDPOINT_FIBER_COEFFICIENT_STRATA_RETAINED";
print "FIVE_PARAMETER_SLICE_IDENTITIES_PASS_NO_NUMERICAL_SAMPLING";
