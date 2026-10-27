-- Exact local negative control for the full-primary attachment module.
-- Tests this displayed polynomial ideal only; no global quartic realization.
-- The integer Hilbert--Burch identities also give the all-characteristic proof.
checkField = (kk,label) -> (
    RR := kk[t,x,y,MonomialOrder=>GRevLex];
    tt := RR_0;
    xx := RR_1;
    yy := RR_2;
    II := ideal(xx,yy);
    LL := ideal(xx^2,xx*yy+tt*yy^2);
    JJ := LL+ideal(yy^3);
    KK := ideal(xx+tt*yy,tt^2);
    HH := matrix{{yy,0},{-xx+tt*yy,-yy^2},{-tt^2,xx+tt*yy}};
    assert(codim LL == 2);
    assert(trim saturate(LL,ideal(tt)) == trim JJ);
    assert(trim(LL:JJ) == trim KK);
    assert(trim intersect(JJ,KK) == trim LL);
    assert(trim minors(2,HH) == trim JJ);
    assert((gens JJ)*HH == 0);
    CC := RR/II;
    uu := sub(tt,CC);
    Hred := sub(HH,CC);
    Hexpected := matrix{{0_CC,0_CC},{0_CC,0_CC},{-uu^2,0_CC}};
    assert(entries Hred == entries Hexpected);
    -- E = C^2 direct_sum C/(t^2), with actual equations e1,e2.
    -- Adding their two basis columns to the presentation leaves C/(t^2).
    source := map(target Hred,CC^2,{{1_CC,0_CC},{0_CC,1_CC},{0_CC,0_CC}});
    Qmod := coker (Hred|source);
    assert(trim fittingIdeal(0,Qmod) == ideal(uu^2));
    -- Actual residual intersection with the marked smooth curve.
    Kbar := sub(KK,CC);
    assert(trim Kbar == ideal(uu^2));
    assert(dim(coker gens Kbar) == 0);
    assert(degree(coker gens Kbar) == 2);
    << "PASS " << label << ": primary extraction, linkage, HB, torsion presentation, Fitt0 and attachment length 2" << endl;
    );
checkField(QQ,"characteristic zero");
checkField(ZZ/2,"characteristic two");
checkField(ZZ/3,"characteristic three");
<< "Scope: exact local ideal control; determinant of torsion-free source is a unit while torsion accounts for all attachment." << endl;
