-- Sparse (2,1) quadric-cubic contact classification and six pair certificates.
-- Characteristic zero.  u=1/(1-alpha), v=1/(1-beta); u=0 retains alpha=infinity.
-- These are exact identities / ideal equalities, not numerical samples.
spBase=QQ[spU,spV,MonomialOrder=>Lex]; spPoly=spBase[spZ];
spCandidates={
 ideal(21*spV^2-21*spV+5,spU-11*spV+5),
 ideal(63*spV^4-126*spV^3+111*spV^2-48*spV+8,
       spU-42*spV^3+63*spV^2-42*spV+10),
 ideal(7*spV^4-14*spV^3+12*spV^2-5*spV+1,spU+spV-1)
};
spCounts={2,4,4};
for spN in {1,2,3} do (
 spH=(spZ-1)*(spU*spZ+1-spU)^spN*(spV*spZ+1-spV)^(6-spN);
 spC=apply(8,spIndex->coefficient(spZ^spIndex,spH));
 -- Binary resultant of P2(X)=h6 X^2+h3 X Y+h0 Y^2 and
 -- Q2(X)=h7 X^2+h4 X Y+h1 Y^2, including their root at infinity.
 spRes=det matrix{{spC#6,spC#3,spC#0,0},{0,spC#6,spC#3,spC#0},
                  {spC#7,spC#4,spC#1,0},{0,spC#7,spC#4,spC#1}};
 spSparse=ideal(spC#2,spC#5);
 spGood=saturate(spSparse,ideal((spU-spV)*spRes));
 spExpected=spCandidates#(spN-1);
 assert(isSubset(spGood,spExpected) and isSubset(spExpected,spGood));
 assert(dim spGood==0 and degree spGood==spCounts#(spN-1));
 assert(1_spBase % (spGood+ideal(spU*spV*(spU-1)*(spV-1)))==0);
 spSum=spU+spV; spProduct=spU*spV; spShift=spSum-1;
 if spN==1 then (
  assert((spShift^2-12/7)%spGood==0);
  assert((spProduct-spSum/2+5/42)%spGood==0)
 );
 if spN==2 then (
  assert((63*spShift^4-30*spShift^2-1)%spGood==0);
  assert((spProduct-5/12-spShift/2+spShift^2/4)%spGood==0)
 );
 if spN==3 then (
  assert((spSum-1)%spGood==0);
  assert((7*spProduct^2-5*spProduct+1)%spGood==0)
 );
 print("PASS exact sparse / irreducible classification "|toString(spN,6-spN));
 print("CANDIDATE_IDEAL "|toString(spN,6-spN)|" "|toString gens gb spGood);
);
spH=(spZ-1)*(spU*spZ+1-spU)^6;
spC=apply(8,spIndex->coefficient(spZ^spIndex,spH));
spRes=det matrix{{spC#6,spC#3,spC#0,0},{0,spC#6,spC#3,spC#0},
                 {spC#7,spC#4,spC#1,0},{0,spC#7,spC#4,spC#1}};
spDouble=ideal(spC#2,spC#5);
assert(isSubset(spDouble,ideal(spU*(spU-1))) and isSubset(ideal(spU*(spU-1)),spDouble));
assert(1_spBase % saturate(spDouble,ideal(spRes))==0);
print "PASS sixfold single-root contact is always reducible";

-- Pair test using the three invariant candidate types.
spPair=QQ[spH1,spP1,spH2,spP2];
spTypes1={
 ideal(spH1^2-12/7,spP1-8/21-spH1/2),
 ideal(63*spH1^4-30*spH1^2-1,spP1-5/12-spH1/2+spH1^2/4),
 ideal(spH1,7*spP1^2-5*spP1+1)};
spTypes2={
 ideal(spH2^2-12/7,spP2-8/21-spH2/2),
 ideal(63*spH2^4-30*spH2^2-1,spP2-5/12-spH2/2+spH2^2/4),
 ideal(spH2,7*spP2^2-5*spP2+1)};
spS1=1+spH1; spS2=1+spH2;
spE=spS1*spS2-3*spS1*spP2-3*spS2*spP1+spP1+spP2+6*spP1*spP2-1/3;
spSimple={
 {2/147-spH1*spH2/2,(1-3*spH2^2-21*spH1*spH2)/42,2/7*(spP2-1/3)},
 {0,((1-3*spH1^2)*(1-3*spH2^2)-12*spH1*spH2)/24,
       (3*spH1^2-1)*(1-3*spP2)/6},
 {0,0,2/3*(1-3*spP1)*(1-3*spP2)}};
spCertCount=0;
for spI from 0 to 2 do for spJ from spI to 2 do (
 spConditions=spTypes1#spI+spTypes2#spJ;
 assert((spE-(spSimple#spI)#spJ)%spConditions==0);
 spGenerators=gens(spConditions+ideal(spE));
 spUnity=matrix{{1_spPair}};
 spCertificate=spUnity//spGenerators;
 assert(spGenerators*spCertificate==spUnity);
 print("PASS pair identity and polynomial Bezout certificate "|toString(spI+1,spJ+1));
 print("GENERATORS "|toString(spI+1,spJ+1)|" "|toString spGenerators);
 print("CERTIFICATE "|toString(spI+1,spJ+1)|" "|toString spCertificate);
 spCertCount=spCertCount+1;
);
assert(spCertCount==6);
print "PASS all four classification blocks and six exact pair certificates";
