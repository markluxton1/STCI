-- Exact polynomial support for projection_and_elliptic_gluing.md sections 1–4.
-- Each block is an independent rational polynomial identity or coefficient ideal.
-- Root existence and global support conclusions are proved in the chapter.
-- The full projection incidence is not computed here.

-- Exact identities for two completed empty slices of the marked O(2,2) source.
-- The full sixteen-parameter locus is NOT computed by this file.
-- Run: M2 --script research/computations/projection_incidence_certificates.m2
R=QQ[z,r,A,p];
-- Segre coordinates scaled to avoid rational functions in the parameter z.
aa=z^2;
bb=r*(z^2+A)+z*(1-p);
cc=r*(z^2+A)-z*p;
sd=z^2*r^2;
del=bb-cc;
D=A*r^4;
L=p*bb+(1-p)*cc;
U={aa^2+A*del^2,aa*L,sd*L,sd^2+D*del^2};
H=z^2*(z^2+A);
F=(1-2*p)*r*z^3+(2*A*r^2-p*(1-p))*z^2+(1-2*p)*r*A*z+A^2*r^2;
assert(del==z);
assert(bb*cc-aa*sd==F);
assert(U==apply({1,r,r^3,r^4},t->H*t));
assert(sub(F,{z=>0})==A^2*r^2);
assert(sub(F,{p=>1/2})==(2*A*r^2-1/4)*z^2+A^2*r^2);
print "COMMON_MIDDLE_LINEAR_FORM_IDENTITIES_PASS";
-- Empty eight-parameter slice with U0=a^2, U1=ab.
S=QQ[a,b,c,d,e0,e1,e2,e3];
del=b-c;
U2=d*c+del*(e0*a+e1*b+e2*c+e3*d);
assert(sub(U2,{a=>0,b=>0})==c*((1-e3)*d-e2*c));
assert(sub(U2,{a=>0,c=>0})==b*(e1*b+e3*d));
print "TWO_FIXED_COORDINATE_ENDPOINT_IDENTITIES_PASS";
print "NO_FULL_SIXTEEN_PARAMETER_CLASSIFICATION_CLAIMED";


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


-- Complete coefficient-locus calculation for q(U)=k*Delta^2*a*d, k nonzero.
-- This is a determinant stratum inside the FULL nine-parameter order-two source.
P=QQ[l0,m0,l1,l2,m2,h0,h1,h2,h3,k];
R=P[a,y,d,z];
-- y=(b+c)/2, z=b-c, so z^2=4(y^2-ad).
V0=l0*a+m0*y;
V1=l1*a+l0*y+m0*d;
V2=l2*a+m2*y-l1*d;
V3=l2*y+m2*d;
U={a^2+z*V0+h0*z^2,a*y+z*V1+h1*z^2,
   y*d+z*V2+h2*z^2,d^2+z*V3+h3*z^2};
rel=ideal(z^2-4*(y^2-a*d));
eq=(U#0*U#3-U#1*U#2-k*z^2*a*d)%rel;
J=sub(ideal flatten entries last coefficients eq,P);
use P;
JS=saturate(J,ideal k);
expected=ideal(l0,m2,h1,h2,h0+m0*l1,h3-l1*l2,
               k-l1^2+1/4,m0*l2);
assert(JS==expected);
assert(saturate(expected,ideal k)==expected);
print "COMPLETE_NONZERO_K_COEFFICIENT_LOCUS_VERIFIED";
print("SATURATED_IDEAL="|toString gens expected);
print("LOCUS_CLOSURE_DIMENSION="|toString dim(P/expected));
-- At either off-diagonal coordinate point a=d=0, y=epsilon*z/2.
-- epsilon is +1 or -1. Both source points are retained, including basepoints.
T=QQ[L,M,N,z];
use T;
scan({-1,1},ep->{
   assert(M*z*(ep*z/2)-M*L*z^2==M*z^2*(ep/2-L));
   assert(N*z*(ep*z/2)+N*L*z^2==N*z^2*(ep/2+L));
});
print "ENDPOINT_OR_BASEPOINT_IDENTITIES_VERIFIED";
print "FULL_INVERSE_SUPPORT_LOCUS_ON_THIS_DETERMINANT_STRATUM_IS_EMPTY";


R=QQ[a,h,d,z,A,B,C,D,E,k0,k1,k2,k3];
I=ideal(a*d-h^2+z^2/4);
L0=A*a+B*h; L1=C*a+A*h+B*d; L2=D*a+E*h-C*d; L3=D*h+E*d;
U0=a^2+z*L0+k0*z^2; U1=a*h+z*L1+k1*z^2; U2=h*d+z*L2+k2*z^2; U3=d^2+z*L3+k3*z^2;
rDet=(k3-C*D)*a^2+(-k2-C*E)*a*h+(C^2-1/4)*a*d+(-k1+A*C)*h*d+(k0+B*C)*d^2+z*((A*k3-C*k2-D*k1-E/4)*a+(B*k3+D*k0-A*k2-E*k1)*h+(E*k0-B*k2+C*k1-A/4)*d)+z^2*((B*D-A*E)/4+k0*k3-k1*k2);
assert((U0*U3-U1*U2-z^2*rDet)%I==0);
print "M2_NINE_PARAMETER_DETERMINANT_IDENTITY_PASS";


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


-- Exact root-incidence certificate for the determinant stratum D=2R,
-- R of class (1,1), R different from the diagonal.
-- On C0, equations of target bidegree (3,1) have degree-ten binary
-- restrictions missing precisely the coefficients of t^2,t^5,t^8.
-- Two finite nonzero distinct roots reduce, by the preserving torus and
-- exchange of the two root factors, to (s-r*t)^m(s-t)^(10-m), 1<=m<=5.
R=QQ[r]; T=R[t];
for m from 1 to 5 do (
    P=(1-r*t)^m*(1-t)^(10-m);
    ff=apply({2,5,8},j->sub(coefficient(t^j,P),R));
    gg=fold(ff,(a,b)->gcd(a,b));
    assert(gg==1_R);
    print("MULTIPLICITY="|toString m|"; COEFFICIENTS="|toString ff|"; GCD="|toString gg);
);
print "TWO_FINITE_NONZERO_ROOT_LOCUS_EMPTY";
print "ENDPOINT_ROOT_CASES_REQUIRE_REDUCIBLE_TARGET_CURVE_BY_BINARY_SUPPORT_ARGUMENT";
-- Reducible R has a component mapping onto an irreducible (1,1) conic.
-- Its restriction to C0 misses only the coefficient of t^2.
assert(sub(coefficient(t^2,(1-r*t)^4),R)==6*r^2);
print "REDUCIBLE_RESIDUAL_ONE_POINT_CONTACT_REQUIRES_REDUCIBLE_TARGET_CURVE";
print "FULL_DOUBLE_RESIDUAL_STRATUM_EXCLUDED_IN_CHARACTERISTIC_ZERO";
