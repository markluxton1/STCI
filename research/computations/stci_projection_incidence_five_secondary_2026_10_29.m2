-- Independent secondary control of the five-parameter marked-quadric slice.
-- Parameters remain indeterminate; this is not a sample-rank argument.
P=QQ[C,h0,h1,h2,h3];
S=P[y,z];
v=y^2-z^2/4;
-- a=1, d=v. Target endpoint p0, and generic first-normal coefficient.
U0=1+h0*z^2;
U1=y+C*z+h1*z^2;
U2=v*(y-C*z)+h2*z^2;
U3=v^2+h3*z^2;
R0=h3+(C^2-1/4)*v-h2*(y+C*z)-h1*v*(y-C*z)
   +h0*v^2+(h0*h3-h1*h2)*z^2;
H0=U0^2*U2-U1^3;
assert(U0*U3-U1*U2==z^2*R0);
assert(coefficient(z,H0)==-4*C*y^2);
I2=ideal(y,z)^2;I3=ideal(y,z)^3;
assert((R0-h3+h2*(y+C*z))%I2==0);
assert((H0-h2*z^2)%I3==0);
-- d=1, a=v. Target endpoint p_infinity, with h0=0 when on residual.
V0=v^2+h0*z^2;
V1=v*(y+C*z)+h1*z^2;
V2=y-C*z+h2*z^2;
V3=1+h3*z^2;
Rinf=h0+(C^2-1/4)*v-h2*v*(y+C*z)-h1*(y-C*z)
     +h3*v^2+(h0*h3-h1*h2)*z^2;
Hinf=V2^3-V1*V3^2;
assert(V0*V3-V1*V2==z^2*Rinf);
assert((Rinf-h0+h1*(y-C*z))%I2==0);
assert((Hinf+h1*z^2)%I3==0);
-- At each endpoint at least one ruling coefficient is nonzero,
-- including C=+/-1/2, since their difference is one.
assert((C+1/2)-(C-1/2)==1);
print "SECONDARY_FIVE_PARAMETER_ENDPOINT_JETS_PASS";
