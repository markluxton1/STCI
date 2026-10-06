-- Exact characteristic-zero finite-principal-part computation for C0.
-- Run: M2 --script research/computations/verify_localcoh_finite_principal_parts.m2
-- Ext^2(S/I^n,S) is the canonical module whose sheaf is T_n.
-- The canonical module has depth at least two, so its graded piece of
-- degree -7 equals H^0(P^3,T_n(-7)).  All dimensions here are over QQ.

S=QQ[x,y,z,w];
q=x*w-y*z;
A=x^2*z-y^3;
B=x*z^2-y^2*w;
C=y*w^2-z^3;
I=ideal(q,A,B,C);

expected={0,0,1,30,105};
for n from 1 to 5 do (
    E=Ext^2(coker gens(I^n),S^1);
    dimension=numColumns basis(-7,E);
    assert(dimension==expected#(n-1));
    print("dim H^0(T_"|toString n|"(-7)) = "|toString dimension);
);

E3=Ext^2(coker gens(I^3),S^1);
a3=basis(-7,E3);
K=annihilator image a3;
L=K:I;
socleMultipliers=basis(4,L);
assert(numColumns socleMultipliers==1);
assert(q^2 % L == 0);
print("PASS: unique order-three section has quartic socle multipliers k*q^2");

-- A fixed diagonal Cech stage realizes all order-four sections.  This is
-- useful for a finite bilinear incidence problem, without any stage scan.
MI4=coker gens(I^4);
MJ4=coker gens ideal(q^4,B^4);
quotientMap=map(MI4,MJ4,matrix{{1_S}});
dualMap=Ext^2(quotientMap,S^1);
assert(numColumns basis(-7,source dualMap)==30);
assert(numRows gens target dualMap==1);
assert(degrees target dualMap=={{-20}});
numerators=dualMap*basis(-7,source dualMap);
assert(numColumns numerators==30);
assert(numRows numerators==1);
assert(numColumns basis(-7,kernel dualMap)==0);
print("PASS: all 30 order-four sections inject into diagonal Cech stage N=4");
print("Their numerators have homogeneous degree 13 modulo (q^4,B^4).");
