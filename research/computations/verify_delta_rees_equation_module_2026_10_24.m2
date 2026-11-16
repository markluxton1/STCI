-- New exact samples for the equation module of the normal deformation.
-- This computes saturated ideals and the FULL syzygy module independently.
-- Run: M2 --script research/computations/verify_delta_rees_equation_module_2026_10_24.m2

sampleCount = 0;
scan({{2,4},{3,4},{2,5},{4,5}}, parameters -> (
    aa = parameters#0;
    bb = parameters#1;
    rr = bb-aa;
    ReesAmbient = QQ[deformParam,normalX,normalY];
    deformedF = normalX^aa+deformParam^rr*normalY^bb;
    deformedG = normalX*normalY;
    extraEquation = normalY^(bb+1);
    fullIdeal = ideal(deformedF,deformedG,extraEquation);
    assert(saturate(ideal(deformedF,deformedG),ideal(deformParam)) == fullIdeal);
    expectedRelations = map(source gens fullIdeal,,{{normalY,0_ReesAmbient},
        {-normalX^(aa-1),normalY^bb},
        {-deformParam^rr,-normalX}});
    assert(matrix{{deformedF,deformedG,extraEquation}}*expectedRelations == 0);
    assert(image syz gens fullIdeal == image expectedRelations);
    restrictedRelations = sub(syz gens fullIdeal,{normalX=>0,normalY=>0});
    expectedRestricted = sub(expectedRelations,{normalX=>0,normalY=>0});
    assert(image restrictedRelations == image expectedRestricted);
    -- The only restricted relation is deformParam^rr times the third generator.
    assert(image expectedRestricted == image map(target expectedRestricted,,
        {{0_ReesAmbient},{0_ReesAmbient},{deformParam^rr}}));
    assert(sub(fullIdeal,{deformParam=>0}) ==
        ideal(normalX^aa,normalX*normalY,normalY^(bb+1)));
    sampleCount = sampleCount+1;
    print("PASS full Rees ideal and equation module: a="|toString aa
        |", b="|toString bb|", torsion duration="|toString rr);
    ));

-- Labelled carrier normal cones can fail to give the actual intersection cone
-- even when the equation-module comparison has zero defect.
ReesAmbient = QQ[deformParam,normalX,normalY];
carrierIntersection = ideal(normalX,normalX+deformParam^3*normalY^4);
actualDeformation = saturate(carrierIntersection,ideal(deformParam));
assert(actualDeformation == ideal(normalX,normalY^4));
assert(sub(carrierIntersection,{deformParam=>0}) == ideal(normalX));
assert(sub(actualDeformation,{deformParam=>0}) == ideal(normalX,normalY^4));
restrictedRelations = sub(syz gens actualDeformation,{normalX=>0,normalY=>0});
assert(restrictedRelations == 0);
print("PASS labelled carrier square: non-Cartesian special square with zero Delta");
print("ALL "|toString(sampleCount+1)|" NEW EXACT REES SAMPLES PASS");
print("Boundary: finite presentations over QQ; not arbitrary-parameter proofs,");
print("sheaf gluing, integral-carrier proofs, or a global STCI statement.");
exit 0;
