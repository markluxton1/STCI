-- Independent symbolic control of the four-parameter outer family.
-- No numerical coefficient sampling or localization of a candidate locus.
P=QQ[A,D,C,E,a,r]; R=P[w];
N=C*w^2-E; V=w*(D-A*w); K=C*D*w-A*E;
H=N^2*((8*C*D+A)*w-(8*A*E+D))+4*w*(D-A*w)*K^2;
cs=for j from 0 to 5 list sub(coefficient(w^j,H),P);
F=C*D^2-A^2*E;
assert(cs#0==-E^2*(8*A*E+D));
assert(cs#5==C^2*(8*C*D+A));
assert(sub(cs#4,{D=>-8*A*E})==-4*A*(-8*A*E)^2*C^2);
assert(sub(cs#1,{A=>-8*C*D})==4*(-8*C*D)^2*D*E^2);
assert(sum(for j from 0 to 5 list cs#j*D^j*A^(5-j))==8*F^3);
assert((H-4*C^2*w^3*(D-A*w)^3)%ideal(N)==0);
print("QUINTIC_EDGE_COEFFICIENTS_AND_BAD_ROOT_VALUES_PASS");

-- Verify rational source point and all target proportions over a fraction
-- field. The only generic denominators are r, N and V.
Q=frac P;
wr=r^2;
nr=C*wr^2-E;
vr=wr*(D-A*wr);
ar=nr/vr; dr=wr*ar; yr=r*(ar+A+C/ar);
u0=ar^2+A*ar+C;
u1=ar*yr;
u2=dr*yr;
u3=dr^2+D*dr+E;
assert(u1==r*u0);
assert(u2==r^3*u0);
assert(u3==r^4*u0);
hr=sub(H,{w=>r^2});
assert(4*nr^2*(D-A*wr)*(yr^2-ar*dr-1/4)==hr);
print("GENERIC_SOURCE_POINT_AND_SEGRE_IDENTITY_PASS");

-- Exceptional coefficient locus F=0: D=A*r^2, E=C*r^4.
aa=a/1_QQ;
ye=r*(aa+A+C/aa);
de=r^2*aa;
e0=aa^2+A*aa+C;
e3=de^2+(A*r^2)*de+C*r^4;
J=4*r^2*(A*aa+C)*(2*aa^2+A*aa+C)-aa^2;
assert(e3==r^4*e0);
assert(aa*ye==r*e0);
assert(de*ye==r^3*e0);
assert(4*aa^2*(ye^2-aa*de-1/4)==J);
print("EXCEPTIONAL_SOURCE_POINT_AND_SEGRE_IDENTITY_PASS");
print("AUDIT_FOUR_PARAMETER_OUTER_FAMILY_IDENTITIES_PASS");
