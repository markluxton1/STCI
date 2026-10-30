-- Complete four-parameter moving-outer-coordinate projection family.
-- U=(a^2+A*a*Delta+C*Delta^2,a*Y,d*Y,d^2+D*d*Delta+E*Delta^2).
-- All rational coefficient identities are exact over QQ; no parameter samples.
P=QQ[A,D,C,E,z]; R=P[w];
N=C*w^2-E; V=w*(D-A*w); K=C*D*w-A*E;
H=N^2*((8*C*D+A)*w-(8*A*E+D))+4*w*(D-A*w)*K^2;
cs=for i from 0 to 5 list sub(coefficient(w^i,H),P);
F=C*D^2-A^2*E;
inv=ideal(z*(C*E*F)-1);
assert(ideal(for i from 1 to 5 list cs#i)+inv==ideal 1_P);
assert(ideal(for i from 0 to 4 list cs#i)+inv==ideal 1_P);
assert(ideal(cs#0,cs#5)+inv==ideal 1_P);
print("H_NOT_CONSTANT_OR_PURE_W5_ON_GENERIC_STRATUM");
print("LEADING_AND_CONSTANT_NOT_BOTH_ZERO_ON_GENERIC_STRATUM");
assert((H-4*C^2*w^3*(D-A*w)^3)%N==0);
assert((H-8*A*N^3)%(D-A*w)==0);
print("ALL_BAD_NONZERO_ROOTS_EXCLUDED_ON_GENERIC_STRATUM");
-- Verify construction over the generic coefficient field, with w=r^2.
S=QQ[A,D,C,E,r]; L=frac S;
n=C*r^4-E; v=r^2*(D-A*r^2);
aa=n/v; dval=r^2*aa; yy=r*(aa+A+C/aa);
u0=aa^2+A*aa+C; u1=aa*yy; u2=dval*yy; u3=dval^2+D*dval+E;
assert(u1==r*u0 and u2==r^3*u0 and u3==r^4*u0);
hval=n^2*((8*C*D+A)*r^2-(8*A*E+D))+4*r^2*(D-A*r^2)*(C*D*r^2-A*E)^2;
assert(yy^2-aa*dval-1/4==r^2*hval/(4*n^2*v));
print("GENERIC_OFF_DIAGONAL_TARGET_AND_SEGRE_IDENTITIES_PASS");
-- Exceptional stratum: D=A*w, E=C*w^2.  The auxiliary cubic has nonzero constant.
T=QQ[A,C,w,a];
J=4*w*(A*a+C)*(2*a^2+A*a+C)-a^2;
TT=frac T;
assert(sub(J,TT)/(4*a^2)==w*((a+A+C/a)^2-a^2)-1/4);
assert(sub(J,T)==8*A*w*a^3+(4*A^2*w+8*C*w-1)*a^2+8*A*C*w*a+4*C^2*w);
print("EXCEPTIONAL_STRATUM_CUBIC_IDENTITY_PASS");
-- First determinant coefficient is nonzero exactly when (A,D)!=(0,0).
U=QQ[A,D,C,E,a,Y,d,del];
UU={a^2+A*a*del+C*del^2,a*Y,d*Y,d^2+D*d*del+E*del^2};
qval=UU#0*UU#3-UU#1*UU#2;
Q=U/ideal(a*d-Y^2+del^2/4,del^2);
assert(sub(qval-a*d*del*(A*d+D*a),Q)==0);
print("FIRST_DETERMINANT_COEFFICIENT_VERIFIED");
print("ALL_FOUR_PARAMETER_LOCUS_EXCLUDED_BY_CONSTRUCTION_IN_COMPANION_NOTE");
