-- Independent reconstruction from the global sections, including local
-- residual contact and the full off-diagonal pulledCurveIdeal scheme.
K0=QQ[symbol jAudit]; K=toField(K0/ideal(jAudit^2+1));
R=K[a,y,d,z];
quadric=ideal(a*d-y^2+z^2/4);
sections={a^2,a*y,y*d+z*y+jAudit*z^2/4,
 d^2+z*(-10*jAudit*y-2*d)+5*z^2/2};
assert(saturate(quadric+ideal sections,ideal(a,y,d,z))==ideal 1_R);

T=K[x,t];
chart=map(T,R,{1,x,x^2-t^2/4,t});
v2=chart(sections#2)-x^3;
v3=chart(sections#3)-x^4;
H2=v2//t;
H3=v3//t;
assert(t*H2==v2 and t*H3==v3);
assert(sub(H2,{t=>0})==x);
assert(sub(H3,{t=>0})==-10*jAudit*x-2*x^2);
assert(sub(H3,{t=>0})==x*(-10*jAudit-2*x));

branchNum=-jAudit*t; branchDen=4-t;
cleared=((-2-t/2)*branchNum^2-10*jAudit*branchNum*branchDen
 +(t^3/16+t^2/2+5*t/2)*branchDen^2);
assert(cleared==t^5/16);
localResidual=saturate(ideal(H2,H3),ideal(1-t/4));
assert(dim(T/localResidual)==0 and degree(T/localResidual)==5);
projectionDet=chart((sections#0)*(sections#3)-(sections#1)*(sections#2));
assert(sub(diff(t,projectionDet),{t=>0})==-10*jAudit*x-3*x^2);
print("AUDIT_LOCAL_NORMAL_ORDER_ONE_AND_RESIDUAL_LENGTH_FIVE_PASS");

gx=sub(chart(sections#3),{x=>1});
involution=-4/(jAudit-1)-t;
deckDifference=gx-sub(gx,{t=>involution});
assert(sub(coefficient(t^3,deckDifference),K)==(3+jAudit)/2);
print("AUDIT_BIRATIONALITY_INVOLUTION_NONINVARIANCE_PASS");

u0=sections#0; u1=sections#1; u2=sections#2; u3=sections#3;
pulledCurveIdeal=quadric+ideal(z-1)+ideal(
 u0*u3-u1*u2,u1^3-u0^2*u2,
 u1^2*u3-u0*u2^2,u2^3-u1*u3^2);
assert(dim(R/pulledCurveIdeal)==0 and degree(R/pulledCurveIdeal)==8);
assert(a^2%pulledCurveIdeal==0);
leftPart=saturate(pulledCurveIdeal,ideal(2*y+1));
rightPart=saturate(pulledCurveIdeal,ideal(2*y-1));
assert(degree(R/leftPart)==4 and degree(R/rightPart)==4);
assert(intersect(leftPart,rightPart)==pulledCurveIdeal);
print("AUDIT_OFF_DIAGONAL_INVERSE_TWO_SUPPORT_POINTS_LENGTH_FOUR_EACH_PASS");
print("AUDIT_JOIN_LOCAL_CONTACT_COUNTEREXAMPLE_PASS");
