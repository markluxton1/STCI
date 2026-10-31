-- Independent quotient-coordinate audit of the NEW (t,kappa)=(1,0) sextic.
-- Actual 969 constant degree-sixteen coefficients, no k(C) source freedom.
-- Normal cutoffs eight, nine and ten test the sharpened contact bounds.
-- This does not replay the inherited R-0025 carrier (t,kappa)=(0,1).
primeValue=65521;
jetField=ZZ/primeValue;
jetRing=jetField[u,v,MonomialOrder=>GRevLex];
degree16Exponents={};
for aa from 0 to 16 do for bb from 0 to 16-aa do
  for cc from 0 to 16-aa-bb do
    degree16Exponents=append(degree16Exponents,{aa,bb,cc,16-aa-bb-cc});
assert(#degree16Exponents==969);

pointJetMatrix=(pointValue,kappaValue,cutoffValue)->(
  use jetRing;
  zz=sub(pointValue,jetRing);
  assert(zz!=0);
  assert(1+2*zz+zz^2!=0);
  assert(1+2*zz+2*zz^2!=0);
  imageX2=zz^3+v;
  imageX3=zz^4+u+(3/2)*zz*v;
  imageQuadric=imageX3-zz*imageX2;
  imageCubic=imageX2^3-zz*imageX3^2;
  imageCarrier=(-imageQuadric^2*imageX3^2
    -imageQuadric*imageCubic*imageX2-imageQuadric*imageCubic*imageX3
    +(1/4)*imageCubic^2+kappaValue*imageQuadric^3);
  jetIdeal=ideal(imageCarrier)+(ideal(u,v))^cutoffValue;
  jetQuotient=jetRing/jetIdeal;
  assert(numcols basis jetQuotient==2*cutoffValue-1);
  quotientBasis=lift(basis jetQuotient,jetRing);
  ambientImages=matrix{apply(degree16Exponents,ee->(
      zz^(ee#1)*imageX2^(ee#2)*imageX3^(ee#3))%jetIdeal)};
  imageExpansion=coefficients(ambientImages,Monomials=>quotientBasis);
  imageCoordinates=last imageExpansion;
  assert(entries((first imageExpansion)*imageCoordinates)==entries ambientImages);
  assert(numrows imageCoordinates==2*cutoffValue-1);
  assert(numcols imageCoordinates==969);
  sub(imageCoordinates,jetField)
  );

-- Independent global assembly and coefficient-order reconstruction.
globalRing=jetField[x0,x1,x2,x3];
globalQuadric=x0*x3-x1*x2;
globalCubicD=x2^3-x1*x3^2;
degree10Exponents={};
for aa from 0 to 10 do for bb from 0 to 10-aa do
  for cc from 0 to 10-aa-bb do
    degree10Exponents=append(degree10Exponents,{aa,bb,cc,10-aa-bb-cc});
assert(#degree10Exponents==286);
monomial16=matrix{apply(degree16Exponents,ee->
  x0^(ee#0)*x1^(ee#1)*x2^(ee#2)*x3^(ee#3))};
monomial10=matrix{apply(degree10Exponents,ee->
  x0^(ee#0)*x1^(ee#1)*x2^(ee#2)*x3^(ee#3))};
globalMultiples=(kappaValue)->(
  use globalRing;
  globalCarrier=(-globalQuadric^2*x3^2-globalQuadric*globalCubicD*x2
    -globalQuadric*globalCubicD*x3+(1/4)*globalCubicD^2
    +kappaValue*globalQuadric^3);
  multipleExpansion=coefficients(globalCarrier*monomial10,Monomials=>monomial16);
  returnedMonomials=flatten entries(first multipleExpansion);
  inputMonomials=flatten entries monomial16;
  rowPermutation=apply(inputMonomials,mm->position(returnedMonomials,nn->nn==mm));
  assert(all(rowPermutation,ii->ii=!=null));
  multipleCoefficients=sub((last multipleExpansion)^rowPermutation,jetField);
  assert(numrows multipleCoefficients==969);
  assert(numcols multipleCoefficients==286);
  assert(rank multipleCoefficients==286);
  assert(entries(monomial16*sub(multipleCoefficients,globalRing))
    ==entries(globalCarrier*monomial10));
  multipleCoefficients
  );

-- The kappa=0 cutoff-nine case is deliberately NONDECISIVE.
-- An initial attempt to demand rank683 there found672 instead; this
-- negative finding prevents an unproved exclusion at cutoff nine.
for caseData in {{0,9,672},{0,10,683},{1,8,682},{1,9,683}} do (
  kappaValue=caseData#0;
  cutoffValue=caseData#1;
  expectedRank=caseData#2;
  stackedJets=map(jetField^0,jetField^969,0);
  for samplePoint from 1 to 80 do (
    stackedJets=stackedJets||pointJetMatrix(samplePoint,kappaValue,cutoffValue);
    if samplePoint%20==0 then
      print("KAPPA="|toString(kappaValue)|" CUTOFF="|toString(cutoffValue)
        |" POINT="|toString(samplePoint)|" RANK="|toString(rank stackedJets));
    );
  finalRank=rank stackedJets;
  assert(finalRank==expectedRank);
  assert(numrows stackedJets==80*(2*cutoffValue-1));
  multipleCoefficients=globalMultiples(kappaValue);
  productFailure=stackedJets*multipleCoefficients;
  assert(all(flatten entries productFailure,cc->cc==0));
  print("FINAL KAPPA="|toString(kappaValue)|" CUTOFF="|toString(cutoffValue)
    |" ROWS="|toString(numrows stackedJets)|" COLS=969 RANK="|toString(finalRank)
    |" MULTIPLES_RANK=286 MULTIPLE_PRODUCT_RANK="|toString(rank productFailure));
  if finalRank==683 then print("KERNEL_EQUALS_MULTIPLES: PASS")
    else print("KERNEL_EXCESS_PRESENT_MOD_P: retain scope; no automatic rational construction");
  );
print("NEW_T1_SEXTIC_INDEPENDENT_QUOTIENT_AUDIT: PASS");
