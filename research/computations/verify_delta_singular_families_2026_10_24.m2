-- Exact samples for the singular-locus Delta continuation.
-- Rees saturation computes the FULL I-adic initial ideal over QQ[t].
-- These finite samples support, but do not replace, the parameter-family proofs.
-- Run: M2 --script research/computations/verify_delta_singular_families_2026_10_24.m2

R = QQ[t,x,y,s,MonomialOrder=>Eliminate 1];
initialAlongI = (L) -> trim sub(
    saturate(sub(L,{x=>s*x,y=>s*y}),ideal(s)),
    {s=>0}
    );

punctualCount = 0;
scan({2,3,4,5}, mm -> scan({1,2,3}, rr -> (
    nn = mm+1;
    aa = t^rr;
    ff = aa*x+x^2+y^mm;
    gg = aa*y+x*y+y^mm+x^nn;
    cancellationElement = x*gg-y*ff;
    qq = x*y^mm-y^(mm+1);
    assert(cancellationElement == qq+x^(nn+1));
    assert(y*ff-x*gg+cancellationElement == 0);
    assert((-y^mm-x^nn)*ff+y^mm*gg+(aa+x)*cancellationElement == 0);
    actualH = initialAlongI ideal(ff,gg);
    actualB = initialAlongI(ideal(x,y)*ideal(ff,gg));
    assert(actualH == ideal(aa*x,aa*y,qq));
    assert(actualB == ideal(aa*x^2,aa*x*y,aa*y^2,qq));
    fibreH = initialAlongI sub(ideal(ff,gg),{t=>0});
    expectedFibre = if mm==2 then ideal(x^2+y^2,x*y+y^2)
        else ideal(x^2,x*y,y^(mm+1));
    assert(fibreH == expectedFibre);
    punctualCount = punctualCount+1;
    print("PASS punctual family: degree="|toString(mm+1)
        |", local length="|toString rr);
    )));

recursiveCount = 0;
scan({2,3,4,5}, nn -> scan({3,4,5}, qq -> (
    recurrence = {1_R,x};
    scan(2..nn, jj -> (
        recurrence = append(recurrence,
            x*recurrence#(jj-1)-y^qq*recurrence#(jj-2));
        ));
    hs = toList apply(0..nn, ii -> y^(qq*ii)*recurrence#(nn-ii));
    jjIdeal = ideal(hs#0,hs#1);
    assert(ideal hs == jjIdeal);
    scan(1..nn, ii -> (
        nextH = if ii<nn then hs#(ii+1) else 0_R;
        assert(y^qq*hs#(ii-1)-x*hs#ii+nextH == 0);
        ));
    expectedH = ideal apply(0..nn, ii -> x^(nn-ii)*y^(qq*ii));
    expectedB = ideal(x,y)*expectedH
        + ideal apply(2..nn, ii -> x^(nn-ii)*y^(qq*ii));
    assert(initialAlongI jjIdeal == expectedH);
    assert(initialAlongI(ideal(x,y)*jjIdeal) == expectedB);
    assert(dim(R/(jjIdeal+ideal(t,s))) == 0);
    assert(degree(R/(jjIdeal+ideal(t,s))) == qq*nn*(nn+1)//2);
    highOrder = qq*nn+1;
    assert(isSubset(ideal(y^highOrder,x^highOrder+y^highOrder),
        ideal(x,y)*jjIdeal));
    -- The nonminimal lifted Hilbert--Burch matrix has only the indicated
    -- unit entries left after tensoring with the transverse residue field.
    matrixEntries = toList apply(0..nn, row -> toList apply(1..nn, col ->
        if row==col-1 then y^qq
        else if row==col then -x
        else if row==col+1 then 1_R else 0_R));
    liftedHB = matrix matrixEntries;
    assert(matrix{hs}*liftedHB == 0);
    assert(rank sub(liftedHB,{x=>0,y=>0}) == nn-1);
    recursiveCount = recursiveCount+1;
    print("PASS recursive family: n="|toString nn|", q="|toString qq
        |", defect dimension="|toString(nn-1)
        |", cancellation page="|toString(qq-2));
    )));

-- A supported quadruple with torsion in Q, but no Delta.
supportedJ = ideal(x^2,y^2+t*x);
supportedH = ideal(t*x,x^2,x*y^2,y^4);
assert(initialAlongI supportedJ == supportedH);
assert(initialAlongI(ideal(x,y)*supportedJ) == ideal(x,y)*supportedH);
assert(isSubset((ideal(x,y))^4,supportedJ));
print("PASS supported quadruple: torsion in Q does not force Delta");
print("ALL "|toString(punctualCount+recursiveCount+1)|" EXACT FAMILY SAMPLES PASS");
print("Boundary: finite samples, not a proof for arbitrary parameters, integrality,");
print("spectral-sequence convergence, sheaf descent, or global STCI claims.");
exit 0;
