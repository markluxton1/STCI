-- Exact global residual-ideal checks for three new mu_q attachment examples.
-- Finite examples corroborate the universal chart proof in the companion note.
-- Run: M2 --script research/computations/verify_mu_q_residual_linkage_2026_10_27.m2
R=QQ[x0,x1,x2,x3];
B=QQ[s,t];
param=map(B,R,{s^4,s^3*t,s*t^3,t^4});
curveIdeal=ker param;
fixedSurface=x0*x3^3-x2^4;
scan({{3,1,0},{4,0,1},{7,1,1}}, data -> (
    q:=data#0; b:=data#1; c:=data#2; a:=2*b+3*c;
    mate:=x1^q-x0^a*x2^b*x3^c;
    totalIdeal:=ideal(fixedSurface,mate);
    residualIdeal:=saturate(totalIdeal:curveIdeal);
    assert(degree residualIdeal==4*(q-1));
    assert(intersect(curveIdeal,residualIdeal)==totalIdeal);
    attachment:=saturate(curveIdeal+residualIdeal);
    assert(degree attachment==4*q+2);
    restricted:=flatten entries(param gens residualIdeal);
    common:=gcd restricted;
    expected:=s^(3*q-3)*t^(q+5);
    assert(ideal(common)==ideal(expected));
    print("PASS: q=",q," residual degree ",degree residualIdeal,
        "; attachment divisor ",(q+5)," p0 + ",(3*q-3)," pinfinity");
));
print "Scope: exact characteristic-zero q=3,4,7 residual schemes only";
