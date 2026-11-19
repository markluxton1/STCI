-- Candidate search for equation (8) of elliptic_double_inverse_construction.md.
-- Search F_5-valued parameters; test inverse points over its algebraic closure.
-- Reduction uses i=2. A survivor would require separate lifting and descent.
load "research/investigations/stci-equation-search/elliptic_rows.m2";
K = ZZ/5;
imagUnit = 2_K;
assert(imagUnit^2 == -1_K);
sourceRing = K[z_0..z_3];
Q0 = z_0*z_3-z_1^2;
Q1 = z_2^2-z_1*z_3+z_0*z_1;
sections = markedSections(sourceRing,imagUnit);
tested = 0;
survivors = 0;
for mu in {2,3} do (
    -- On the slice Q0=1 the lifting parameters enter as constants.
    fiberRing := sourceRing / ideal(Q0-1, Q1+mu);
    lifted := apply(sections,f -> sub(f,fiberRing));
    for num from 0 to 5^4-1 do (
        rho := apply(4,j -> (num // 5^j) % 5);
        U := apply(4,j -> lifted#j+rho#j);
        inverseIdeal := ideal(
            U#0*U#3-U#1*U#2,
            U#1^3-U#0^2*U#2,
            U#1^2*U#3-U#0*U#2^2,
            U#2^3-U#1*U#3^2
        );
        if (1_fiberRing % inverseIdeal == 0) then (
            print ("candidate",mu,rho);
            survivors = survivors + 1;
        );
        tested = tested + 1;
    );
    print ("parameters tested",tested);
);
assert(tested == 1250 and survivors == 0);
