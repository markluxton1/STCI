-- New exact dimensions for the candidate-search restart, not a replay of
-- a canonical exclusion.  Run from the repository root with:
-- M2 --script research/computations/stci_search_freedom_2026_10_28.m2
-- The ideal sheaf power is computed by homogeneous saturation, not by
-- silently identifying symbolic and unsaturated homogeneous powers.
R = QQ[x,y,z,w];
Q = x*w-y*z;
I = ideal(Q,x^2*z-y^3,x*z^2-y^2*w,z^3-y*w^2);
B = ideal vars R;
J = new MutableList from apply(0..7,m -> if m == 0 then ideal(1_R) else saturate(I^m,B));
dimensionFormula = (d,m) -> (
    if d < 2*m then 0
    else if d < 3*m then (
        u := d-2*m;
        (5*u^3+15*u^2+16*u+6)//6
        )
    else binomial(d+3,3)-m*(m+1)*(4*d+1)//2+7*m*(m^2-1)//3
    );
dimSource = (d,m) -> binomial(d+3,3)-hilbertFunction(d,R/J#m);
rows = {};
for m from 1 to 6 do (
    for d from 0 to 3*m+2 do (
        actual := dimSource(d,m);
        assert(actual == dimensionFormula(d,m));
        if d >= 2*m and d < 3*m then (
            -- Every degree-d section is divisible by the stated fixed Q power.
            v := basis(d,J#m);
            assert(v % gens ideal(Q^(3*m-d)) == 0);
            );
        );
    for d from 3*m to 3*m+2 do (
        image := dimSource(d,m)-dimSource(d,m+1);
        target := (m+1)*(4*d-7*m+1);
        defect := if d == 3*m then 6*m-1 else if d == 3*m+1 then 2*m+1 else 0;
        assert(target-image == defect);
        rows = append(rows, "{\"order\":" | toString m |
            ",\"degree\":" | toString d |
            ",\"source_dimension\":" | toString dimSource(d,m) |
            ",\"symbol_image_dimension\":" | toString image |
            ",\"symbol_target_dimension\":" | toString target | "}");
        );
    );
print("{\"field\":\"QQ\",\"max_order\":6,\"dimensions_and_fixed_factors_pass\":true,\"symbol_rows\":[" |
    concatenate between(",",rows) | "]}");
