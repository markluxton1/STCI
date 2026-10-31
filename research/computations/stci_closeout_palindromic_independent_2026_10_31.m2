-- Independent closeout control over the exact quadratic number field.
-- Bound: one run, 60 s maximum externally; degrees at most 20, no parameter GB.
F=QQ[eta]; K=toField(F/ideal(5*eta^2+4));
egcd=(f,g)->(while g!=0 do (h:=f%g; f=g; g=h;); if f==0 then f else f//leadCoefficient f);
R=K[t];
r=t^4+eta*t^3+eta*t+1;
assert(egcd(r,diff(t,r))==1_R);
coeffs=apply(toList(0..20),i->sub(coefficient(t^i,r^5),K));
T=K[x];
e=apply(toList(0..2),j->sum(toList(0..6),i->coeffs#(3*i+j)*x^i));
-- i=6,j=2 accesses coefficient 20, hence the complete target coefficient triple.
assert(degree(e#0)=={6} and degree(e#2)=={6});
assert(egcd(egcd(e#0,e#1),e#2)==1_T);
targetDisc=e#1^2-4*e#0*e#2;
sq=(eta*x+1)*(x+eta)*(x^2-7*eta*x+1);
ell=5*x^4+(28/5)*eta*x^3+(102/25)*x^2+(28/5)*eta*x+5;
assert(targetDisc==-3*sq^2*ell);
assert(egcd(ell,diff(x,ell))==1_T);
assert(egcd(sq,ell)==1_T);
-- Four smooth normalized target intersections, each contact five.
assert(egcd(r,sub(targetDisc,{x=>t^3}))==1_R);
assert(sub(e#0,{x=>t^3})+t*sub(e#1,{x=>t^3})+t^2*sub(e#2,{x=>t^3})==r^5);
-- Ruling B boundaries: squarefree decomposition detects the two nodal fibers.
znode=-1/eta; pnode=-eta;
zres=e#0//(eta*x+1)^2; pres=e#2//(x+eta)^2;
assert(e#0==zres*(eta*x+1)^2 and e#2==pres*(x+eta)^2);
assert(degree(zres)=={4} and degree(pres)=={4});
assert(egcd(zres,diff(x,zres))==1_T and egcd(pres,diff(x,pres))==1_T);
assert(egcd(zres,e#1)==1_T and egcd(pres,e#1)==1_T);
assert(sub(zres,{x=>znode})!=0 and sub(pres,{x=>pnode})!=0);
assert(sub(e#2,{x=>znode})!=0 and sub(e#0,{x=>pnode})!=0);
assert(sub(ell,{x=>znode})!=0 and sub(ell,{x=>pnode})!=0);
assert(sub(sq//(eta*x+1),{x=>znode})!=0);
assert(sub(sq//(x+eta),{x=>pnode})!=0);
-- The local tangent quadratics have two distinct nonzero slopes.
assert(sub(e#1,{x=>znode})==0 and sub(e#1,{x=>pnode})==0);
assert(sub((diff(x,e#1))^2-2*e#2*diff(x,diff(x,e#0)),{x=>znode})!=0);
assert(sub((diff(x,e#1))^2-2*e#0*diff(x,diff(x,e#2)),{x=>pnode})!=0);
-- A=0 and A=infinity are unramified and avoid all B boundary values.
assert(sub(ell,{x=>0})!=0 and sub(e#0,{x=>0})!=0 and sub(e#2,{x=>0})!=0);
assert(sub(coefficient(x^4,ell),K)!=0);
assert(sub(coefficient(x^6,e#0),K)!=0 and sub(coefficient(x^6,e#2),K)!=0);
print "INDEPENDENT_QUADRATIC_FIELD_DISCRIMINANT_AND_NORMALIZED_BOUNDARY_PASS";
print "PALINDROMIC_TARGET_CLOSEOUT_CONTROL_COMPLETE";
