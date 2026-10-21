-- Exact unrestricted global quartic coefficient constraints; no carrier theorem.
S = QQ[x0,x1,x2,x3];
mons = flatten entries basis(4,S);
assert(#mons == 35);
T = QQ[u,X,Y];
phi = map(T,S,{1,u,u^3+Y,u^4+X});
B = QQ[t];
z = map(B,T,{t,0,0});
polys = apply(mons,m -> phi(m));
constantRows = apply(toList(0..16),j -> apply(polys,H -> coefficient(t^j,z(H))));
xRows = apply(toList(0..12),j -> apply(polys,H -> coefficient(t^j,z(diff(X,H)))));
yRows = apply(toList(0..12),j -> apply(polys,H -> coefficient(t^j,z(diff(Y,H)))));
M0 = matrix constantRows;
M1 = (matrix xRows) || (matrix yRows);
M = M0 || M1;
assert(rank M0 == 17);
assert(rank M == 34);
-- Integral basis of the entire coefficient kernel: all monomials in each
-- exponent group have identical restriction; their differences generate it.
weights = apply(polys,H -> first degree z(H));
-- Standard degree in the one-variable ring is exactly the parameter exponent.
assert(sort unique weights == toList(0..16));
chosenColumns = apply(toList(0..16),j -> position(weights,w -> w==j));
nonchosenColumns = select(toList(0..34),i -> not member(i,chosenColumns));
Id35 = id_(QQ^35);
K = matrix apply(toList(0..34),i -> apply(nonchosenColumns,j -> (
    (if i==j then 1 else 0) - (if i==chosenColumns#(weights#j) then 1 else 0))));
assert(numColumns K == 18);
assert(M0*K == 0);
assert(rank K == 18);
assert(rank(M1*K) == 17);
q = x0*x3-x1*x2;
assert(z(phi(q^2)) == 0);
assert(z(diff(X,phi(q^2))) == 0);
assert(z(diff(Y,phi(q^2))) == 0);
print "PASS: all 35 quartic monomials; 17 independent support equations";
print "PASS: full quartic ideal has an integral 18-column difference basis";
print "PASS: first normal image rank 17; combined rank 34; kernel is q^2";
print "Exact support constraints: for each j, sum of listed coefficients = 0";
scan(toList(0..16),j -> print(j,select(mons,m -> (first degree z(phi(m)))==j)));
-- The two original forms vanish identically on the fixed relative curve.
F = x1^4-x0^3*x3;
G = x2^4-x0*x3^3;
assert(z(phi(F))==0 and z(phi(G))==0);
assert(phi(F) == -X);
assert(phi(G) == 4*u^9*Y+6*u^6*Y^2+4*u^3*Y^3+Y^4-3*u^8*X-3*u^4*X^2-X^3);
print "PASS: integral normal expansions of original F and G";
print "ALL UNRESTRICTED GLOBAL QUARTIC CHECKS PASS";
-- The prescribed ribbon itself has an integral embedded lift.  Invert only
-- 3, a unit in both requested bases; no division by 2 is introduced.
Ribbon=ZZ[u,iu,Y,v,MonomialOrder=>Lex]/ideal(u*iu-1,3*v-1,Y^2);
cr=iu+iu^4*Y;
br=-3*iu^6*Y;
ar=-4*iu^7*Y;
assert(ar-4*v*cr*br==0);
assert(br^2==0);
icr=u-iu^2*Y;
assert(cr*icr==1);
assert(icr-v*icr^4*br==u);
assert(-v*icr^6*br==Y);
print "PASS: exact integral ribbon gluing (X,Y^2) and (A-4cB/3,B^2)";
print "ALL RIBBON LIFT CHECKS PASS";
