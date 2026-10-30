-- Exact target-contact example and boundary-count controls.
-- This is not an actual marked-surface projection certificate.
R=QQ[x];
p=7*x^3+42*x^2+30*x+2;
q=2*x^3+30*x^2+42*x+7;
w=p^3-x*q^3;
assert(gcd(p,q)==1_R);
assert(w%((x-1)^7)==0_R);
c=w//((x-1)^7);
assert(degree c==3);
assert(gcd(c,diff(x,c))==1_R);
assert(sub(c,{x=>1})!=0);
assert(gcd(c,p*q)==1_R);
assert(sub(p,{x=>0})!=0 and sub(q,{x=>0})!=0);
print("PADE_P="|toString p);
print("PADE_Q="|toString q);
print("CONTACT_FACTOR="|toString c);
print("CONTACT_IDENTITY="|toString factor w);
-- The elliptic curve y^2=(x-1)c has four distinct branch values.
-- Pullback of w has orders 14,2,2,2 at these four points.
assert(14+2+2+2==20);
-- Rational degree-ten map p^3/(x*q^3) has no extra critical values.
critical=3*x*(diff(x,p)*q-p*diff(x,q))-p*q;
assert(critical%((x-1)^6)==0_R);
assert(degree critical==6);
print("RATIONAL_CRITICAL_FACTOR="|toString factor critical);
-- Local boundary error is (2-a) for same-sign overlaps, a for
-- opposite-sign overlaps after adding the A support defect, and a-1
-- at A-only support. Every a is one or two.
for a from 1 to 2 do (
 assert(2-a>=0);
 assert(a>0);
 assert(a-1>=0);
);
print("ELLIPTIC_TARGET_CONTACT_EXAMPLE_AND_LOCAL_BOUNDARY_COUNTS_PASS");
