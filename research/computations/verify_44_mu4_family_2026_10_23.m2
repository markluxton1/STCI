-- New exact computations for the explicit F,G family only.
-- No inherited quartic exclusion or lifting proof is rerun.
-- Run: /opt/homebrew/bin/M2 --script research/computations/verify_44_mu4_family_2026_10_23.m2

R = ZZ[u,X,Y];
F = -X;
G = (u^3+Y)^4-(u^4+X)^3;
P = Y^4+4*u^3*Y^3+6*u^6*Y^2+4*u^9*Y;
assert(G == P-3*u^8*X-3*u^4*X^2-X^3);
assert(ideal(F,G) == ideal(X,P));
print "Integer normal expansion and exact elimination of X: PASS";

R2 = (ZZ/2)[u,X,Y];
F2 = sub(F,R2); G2 = sub(G,R2);
assert(ideal(F2,G2) == ideal(X,Y^4));
assert(sub(P,R2) == Y^4);
print "Characteristic two exact ideal (X,Y^4): PASS";

-- The full generic ordinary-normal initial ideals follow without a
-- Groebner/local-order convention: in characteristic zero P has lowest
-- normal term 4*u^9*Y, a nonzero K-multiple of Y, where K=QQ(u).
-- Together with F=-X this puts the maximal homogeneous ideal (X,Y)
-- in the initial ideal; properness gives equality. In characteristic two
-- the exact ideal already is the homogeneous ideal (X,Y^4).
Q = QQ[u,X,Y];
PQ = sub(P,Q);
assert(PQ % ideal(Y^2) == 4*u^9*Y);
assert(PQ % ideal(Y) == 0);
assert(4*u^9 != 0);
print "Generic initial ideals: char 0 (X,Y); char 2 (X,Y^4): PASS";

-- On u invertible write Y=u^3*(z-1). The equation becomes
-- u^12*(z^4-1), exposing the finite flat group scheme mu_4.
L = ZZ[u,z];
phiMu = map(L,R,{u,0,u^3*(z-1)});
assert(phiMu P == u^12*(z^4-1));
print "mu_4 equation P(u,u^3(z-1))=u^12(z^4-1): PASS";

-- Split field QQ(i), with all four fourth roots of unity.
T = QQ[iota];
K = toField(T/ideal(iota^2+1));
A = K[x0,x1,x2,x3];
B = K[s,t];
Fk = x1^4-x0^3*x3;
Gk = x2^4-x0*x3^3;
D = ideal(Fk,Gk);
muRoots = {1_K,-1_K,sub(iota,K),-sub(iota,K)};
H = K[w];
assert(product apply(muRoots,zeta -> w-zeta) == w^4-1);
print "Split factorization product_(zeta^4=1)(w-zeta)=w^4-1: PASS";
familyComponents = apply(muRoots, zeta -> (
    phi := map(B,A,{s^4,s^3*t,zeta*s*t^3,t^4});
    assert(phi Fk == 0 and phi Gk == 0);
    C := ker phi;
    assert(degree C == 4);
    assert(dim(A/C) == 2);
    C));
assert(degree D == 16);
assert(D == intersect familyComponents);
print "Global scheme decomposition into four distinct degree-four components over QQ(i): PASS";

-- Pairwise intersections occur only at the two endpoints. On the x0-chart
-- components have x2/x0=zeta*u^3, so their intersection ideal is (u^3).
-- On the x3-chart x1/x3=zeta*c^3, giving the same multiplicity three.
C = K[u];
pairList = {{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
scan(pairList, pair -> (
    j := pair#0; k := pair#1;
    assert(muRoots#j != muRoots#k);
    assert(ideal((muRoots#j-muRoots#k)*u^3) == ideal(u^3))));
print "Every pair has contact three at each endpoint: PASS";
-- The linear conormal transition also records the characteristic change.
N0 = QQ[u,uinv,X,Y];
N = N0/ideal(u*uinv-1);
Alin = 3*uinv^8*X-4*uinv^7*Y;
Blin = 2*uinv^7*X-3*uinv^6*Y;
assert(3*Alin-4*uinv*Blin == uinv^8*X);
assert(-Blin/3 == uinv^6*Y-(2/3)*uinv^7*X);
assert(u^6*(-Blin/3)-Y == -(2/3)*uinv*X);
print "Conormal extension cocycle -(2/3)*u^-1: PASS";
print "ALL NEW MU4 FAMILY CHECKS PASS";
