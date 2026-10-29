R=QQ[a,h,d,z,A,B,C,D,E,k0,k1,k2,k3];
I=ideal(a*d-h^2+z^2/4);
L0=A*a+B*h; L1=C*a+A*h+B*d; L2=D*a+E*h-C*d; L3=D*h+E*d;
U0=a^2+z*L0+k0*z^2; U1=a*h+z*L1+k1*z^2; U2=h*d+z*L2+k2*z^2; U3=d^2+z*L3+k3*z^2;
rDet=(k3-C*D)*a^2+(-k2-C*E)*a*h+(C^2-1/4)*a*d+(-k1+A*C)*h*d+(k0+B*C)*d^2+z*((A*k3-C*k2-D*k1-E/4)*a+(B*k3+D*k0-A*k2-E*k1)*h+(E*k0-B*k2+C*k1-A/4)*d)+z^2*((B*D-A*E)/4+k0*k3-k1*k2);
assert((U0*U3-U1*U2-z^2*rDet)%I==0);
print "M2_NINE_PARAMETER_DETERMINANT_IDENTITY_PASS";
