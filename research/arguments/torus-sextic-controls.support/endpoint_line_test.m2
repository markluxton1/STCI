-- Use endpointLineTest(F,G,"min") or endpointLineTest(F,G,"max").
-- The input ring is QQ[x0,x1,x2,x3] in that order, with standard grading.
-- kappaL is the generic length of the first-layer kernel along L.
endpointLineTest = (F,G,direction) -> (
    S := ring F;
    if ring G =!= S or not isPolynomialRing S or coefficientRing S =!= QQ or numgens S != 4 then
        error "expected two polynomials in the same four-variable ring over QQ";
    if degrees S != {{1},{1},{1},{1}} then
        error "expected the standard grading";
    if F == 0 or G == 0 or not isHomogeneous F or not isHomogeneous G then
        error "expected nonzero homogeneous equations";
    if direction != "min" and direction != "max" then
        error "direction must be min or max";
    if not isUnit gcd(F,G) then error "expected coprime equations";

    parametrizationRing := QQ[endpointS,endpointT];
    s := parametrizationRing_0;
    t := parametrizationRing_1;
    parametrization := map(parametrizationRing,S,{s^4,s^3*t,s*t^3,t^4});
    if parametrization F != 0 or parametrization G != 0 then
        error "both equations must contain the marked quartic";

    torusWeights := if direction == "min" then {0,1,3,4} else {0,-1,-3,-4};
    weightedTerms := polynomial -> (
        weight := term -> (
            powers := first exponents term;
            sum(4,i -> torusWeights#i * powers#i)
        );
        monomials := terms polynomial;
        weights := apply(monomials,weight);
        lowest := min weights;
        apply(#monomials,i -> (monomials#i,weights#i-lowest))
    );
    extreme := pairs -> sum apply(select(pairs,pair -> pair#1 == 0),first);
    fTerms := weightedTerms F;
    gTerms := weightedTerms G;
    f0 := extreme fTerms;
    g0 := extreme gTerms;
    H := gcd(f0,g0);
    U := f0 // H;
    V := g0 // H;

    K := frac(QQ[endpointY,endpointZ]);
    A := K[endpointX,endpointW];
    x := A_0;
    w := A_1;
    atLine := map(A,S,{x,promote(endpointY,A),promote(endpointZ,A),w});
    m := ideal(x,w);
    localU := atLine U;
    localV := atLine V;
    localH := atLine H;
    eitherRestrictionNonzero := localU % m != 0 or localV % m != 0;
    gcdRestrictionNonzero := localH % m != 0;
    localLength := J -> (
        if not isSubset(J,m) then return 0;
        power := m;
        currentLength := degree(A/(J + power));
        nextLength := degree(A/(J + power*m));
        -- The inputs have finite length at the origin. Equal consecutive
        -- lengths force m^n=0 in the local quotient by Nakayama.
        while currentLength != nextLength do (
            currentLength = nextLength;
            power = power*m;
            nextLength = degree(A/(J + power*m))
        );
        currentLength
    );
    lineLength := localLength ideal(localU,localV);

    -- If H is a unit at the generic point of L, the specializations
    -- form a regular sequence there whenever the line length is positive.
    -- The localized raw family is then flat and contributes that length
    -- to the limit cycle.
    kappa := 0;
    flatMultiplicity := lineLength;
    if not gcdRestrictionNonzero then (
        familyRing := K[endpointX,endpointW,endpointParameter];
        parameter := familyRing_2;
        genericLineCoordinates := map(familyRing,S,
            {familyRing_0,promote(endpointY,familyRing),
                promote(endpointZ,familyRing),familyRing_1});
        orbitEquation := pairs -> sum apply(pairs,pair ->
            genericLineCoordinates(pair#0) * parameter^(pair#1));
        orbitIdeal := ideal(orbitEquation fTerms,orbitEquation gTerms);
        flatFamily := saturate(orbitIdeal,ideal parameter);
        specialize := map(A,familyRing,{x,w,0});
        flatSpecial := specialize flatFamily;
        flatMultiplicity = localLength flatSpecial;
        -- Multiplication by H maps S/(U,V) into the raw special fiber.
        -- Its image in the flat fiber has annihilator J_0:H.
        kappa = lineLength - localLength(flatSpecial : ideal localH)
    );
    new HashTable from {
        "eL" => lineLength,
        "eitherStrippedRestrictionNonzero" => eitherRestrictionNonzero,
        "gcdRestrictionNonzero" => gcdRestrictionNonzero,
        "kappaL" => kappa,
        "multFlatL" => flatMultiplicity,
        "residualDegreeLowerBound" => flatMultiplicity
    }
);

endpointLineTestSmokeCheck = () -> (
    S := QQ[endpointX0,endpointX1,endpointX2,endpointX3];
    (x,y,z,w) := (S_0,S_1,S_2,S_3);
    q := x*w-y*z;
    A := x^2*z-y^3;
    sextics := endpointLineTest(x^2*w*A+q^3,x^3*z*q,"min");
    assert(sextics#"eL" == 1);
    assert(not sextics#"eitherStrippedRestrictionNonzero");
    assert(not sextics#"gcdRestrictionNonzero");
    assert(sextics#"kappaL" == 1);
    assert(sextics#"multFlatL" == 0);
    assert(sextics#"residualDegreeLowerBound" == 0);
    -- The same extreme forms as W_0 can leave a length-six flat fiber.
    retainedMember := x^2*w*A+w^2*q^2;
    retainedLine := endpointLineTest(retainedMember,x^3*z*q,"min");
    assert(retainedLine#"eL" == 1);
    assert(not retainedLine#"eitherStrippedRestrictionNonzero");
    assert(not retainedLine#"gcdRestrictionNonzero");
    assert(retainedLine#"kappaL" == 0);
    assert(retainedLine#"multFlatL" == 6);
    assert(retainedLine#"residualDegreeLowerBound" == 6);
    reverseCoordinates := map(S,S,{w,z,y,x});
    opposite := endpointLineTest(reverseCoordinates retainedMember,
        reverseCoordinates(x^3*z*q),"max");
    scan(keys retainedLine,key -> assert(opposite#key == retainedLine#key));
    eigenpair := endpointLineTest(x*q,w*A,"min");
    assert(eigenpair#"eL" == 1);
    assert(not eigenpair#"eitherStrippedRestrictionNonzero");
    assert(eigenpair#"gcdRestrictionNonzero");
    assert(eigenpair#"kappaL" == 0);
    assert(eigenpair#"multFlatL" == 1);
    assert(eigenpair#"residualDegreeLowerBound" == 1);
    -- L occurs only after specialization in this mixed-weight example.
    movingCubic := x*q + z^3-y*w^2;
    powers := endpointLineTest(movingCubic^2,(w*A)^2,"min");
    assert(powers#"eL" == 4);
    assert(not powers#"eitherStrippedRestrictionNonzero");
    assert(powers#"gcdRestrictionNonzero");
    assert(powers#"kappaL" == 0);
    assert(powers#"multFlatL" == 4);
    assert(powers#"residualDegreeLowerBound" == 4);
    commonFactor := endpointLineTest(x*q,w*(q^2+x*A),"max");
    assert(commonFactor#"eL" == 1);
    assert(not commonFactor#"eitherStrippedRestrictionNonzero");
    assert(commonFactor#"gcdRestrictionNonzero");
    assert(commonFactor#"kappaL" == 0);
    assert(commonFactor#"multFlatL" == 1);
    assert(commonFactor#"residualDegreeLowerBound" == 1);
    unit := endpointLineTest(q,x^2*q+x*A,"max");
    assert(unit#"eL" == 0);
    assert(unit#"eitherStrippedRestrictionNonzero");
    assert(unit#"gcdRestrictionNonzero");
    assert(unit#"kappaL" == 0);
    assert(unit#"multFlatL" == 0);
    assert(unit#"residualDegreeLowerBound" == 0);
    print "PASS: endpoint line lengths and residual bounds over QQ"
);
endpointLineTestSmokeCheck();
