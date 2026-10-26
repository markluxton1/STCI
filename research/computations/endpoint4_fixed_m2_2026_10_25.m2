-- New fixed-carrier jet probe. No all-parameter or unrestricted STCI claim.
-- Actual 969 constant global coefficients, evaluated at rational base points.
primeValue=65521;
jetField=ZZ/primeValue;
jetRing=jetField[u,v,MonomialOrder=>GRevLex];
degree16Exponents={};
for aa from 0 to 16 do for bb from 0 to 16-aa do
  for cc from 0 to 16-aa-bb do
    degree16Exponents=append(degree16Exponents,{aa,bb,cc,16-aa-bb-cc});
assert(#degree16Exponents==969);

pointJetMatrix=(pointValue)->(
  use jetRing;
  zz=sub(pointValue,jetRing);
  assert(zz!=0);
  assert(1+zz^2!=0);
  imageX2=zz^3+v;
  imageX3=zz^4+u+(3/2)*zz*v;
  imageQuadric=imageX3-zz*imageX2;
  imageCubic=imageX2^3-zz*imageX3^2;
  imageCarrier=-imageQuadric^2*imageX3^2-imageQuadric*imageCubic*imageX2+(1/4)*imageCubic^2+imageQuadric^3;
  jetIdeal=ideal(imageCarrier)+(ideal(u,v))^12;
  jetQuotient=jetRing/jetIdeal;
  assert(numcols basis jetQuotient==23);
  quotientBasis=lift(basis jetQuotient,jetRing);
  ambientImages=matrix{apply(degree16Exponents,ee->(
      zz^(ee#1)*imageX2^(ee#2)*imageX3^(ee#3))%jetIdeal)};
  imageExpansion=coefficients(ambientImages,Monomials=>quotientBasis);
  imageCoordinates=last imageExpansion;
  assert(entries((first imageExpansion)*imageCoordinates)==entries ambientImages);
  assert(numrows imageCoordinates==23);
  assert(numcols imageCoordinates==969);
  sub(imageCoordinates,jetField)
  );

stackedJets=map(jetField^0,jetField^969,0);
for samplePoint from 1 to 40 do (
  nextBlock=pointJetMatrix(samplePoint);
  stackedJets=stackedJets||nextBlock;
  sampleRank=rank stackedJets;
  print("POINT="|toString(samplePoint)|" ROWS="|toString(numrows stackedJets)|" RANK="|toString(sampleRank));
  if sampleRank==683 then break;
  );
print("FINAL_RANK="|toString(rank stackedJets));
assert(rank stackedJets==683);
assert(numrows stackedJets==690);

-- Independently construct all 286 global degree-ten multiples, retaining
-- exactly the degree-sixteen column order used above.
globalRing=jetField[x0,x1,x2,x3];
globalQuadric=x0*x3-x1*x2;
globalCubicD=x2^3-x1*x3^2;
globalCarrier=(-globalQuadric^2*x3^2-globalQuadric*globalCubicD*x2
  +(1/4)*globalCubicD^2+globalQuadric^3);
degree10Exponents={};
for aa from 0 to 10 do for bb from 0 to 10-aa do
  for cc from 0 to 10-aa-bb do
    degree10Exponents=append(degree10Exponents,{aa,bb,cc,10-aa-bb-cc});
assert(#degree10Exponents==286);
monomial16=matrix{apply(degree16Exponents,ee->
  x0^(ee#0)*x1^(ee#1)*x2^(ee#2)*x3^(ee#3))};
monomial10=matrix{apply(degree10Exponents,ee->
  x0^(ee#0)*x1^(ee#1)*x2^(ee#2)*x3^(ee#3))};
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
productFailure=stackedJets*multipleCoefficients;
print("MULTIPLE_PRODUCT_RANK="|toString(rank productFailure));
assert(all(flatten entries productFailure,cc->cc==0));
print("ALL_30_SAMPLES_NONZERO_WITH_1_PLUS_Z_SQUARED_UNIT: PASS");
print("GLOBAL_MULTIPLES_RANK_286: PASS");
print("STACK_ANNIHILATES_ALL_286_GLOBAL_MULTIPLES: PASS");
print("FIXED_CARRIER_JET_KERNEL_EQUALS_MULTIPLES: PASS");
