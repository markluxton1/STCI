-- Run: M2 --script research/notes/2026-10-05-quadric-powers.m2
-- Exact consistency checks; the uniform theorem is proved in the companion note.
S=QQ[x,y,z,w];
q=x*w-y*z;
A=x^2*z-y^3; B=x*z^2-y^2*w; D=z^3-y*w^2;
I4=ideal(q,A,B,D);
I5=ideal(q,x^3*z-y^4,x^2*z^2-y^3*w,x*z^3-y^2*w^2,z^4-y*w^3);
-- On Q, with x=su,y=sv,z=tu,w=tv, these are f*s^2,f*st,f*t^2,
-- where f=s^2*u^4+s*t*v^4+t^2*u^3*v+t^2*u*v^3 has bidegree (2,4).
J24=ideal(q,
 x^4+y^3*w+x^2*z*w+x*y*w^2,
 x^3*z+y^2*w^2+x*z^2*w+x*w^3,
 x^2*z^2+y*w^3+z^3*w+z*w^3);
hQ=(u,v)->if u<0 or v<0 then 0 else (u+1)*(v+1);
hFormula=(a,b,m,d)->(
 n:=d-2*m;
 value:=if n<0 then 0 else binomial(n+3,3);
 value+sum(1..m,j->hQ(d-2*m+(2-a)*j,d-2*m+(2-b)*j))
 );
checkPowers=(label,I,a,b,limit)->(
 for m from 1 to limit do (
  J:=I^m;
  assert(J==saturate J);
  assert(degree(S/J)==(a+b)*binomial(m+1,2));
  for d from 0 to b*m+6 do
   assert(hilbertFunction(d,S)-hilbertFunction(d,S/J)==hFormula(a,b,m,d));
  R:=res J;
  assert(rank R_0==1);
  assert(rank R_1==1+m+(b-a)*m*(m+1)//2);
  assert(rank R_2==(b-a)*m*(m+1));
  assert(rank R_3==(b-a)*m*(m+1)//2-m);
  print(label,m,"saturated; Hilbert formula and Betti totals exact");
  );
 );
assert(A*D-B^2+y*z*q^2==0);
checkPowers("C0 type (1,3)",I4,1,3,6);
checkPowers("monomial quintic type (1,4)",I5,1,4,4);
checkPowers("nonmonomial divisor type (2,4)",J24,2,4,4);
print "ALL QUADRIC-POWER CONSISTENCY CHECKS PASSED";
