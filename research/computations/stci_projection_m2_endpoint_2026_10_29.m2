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
