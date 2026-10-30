-- Exact target-incidence enumeration, roots supported on {0,infinity,1,-1}.
-- This does not assert an actual marked-surface projection.
R=QQ[x];
degOrMinusOne=e->if e==0 then -1 else (degree e)_0;
oddPartDegree = f -> (
 if f==0 then return -1;
 local c; local w; local mi; local y; local z; local outDegree;
 f=f/leadCoefficient f;
 c=gcd(f,diff(x,f)); w=f//c; mi=1; outDegree=0;
 while w!=1 do (
  y=gcd(w,c); z=w//y;
  if mi%2==1 then outDegree=outDegree+(degree z)_0;
  w=y; c=c//y; mi=mi+1;
 );
 outDegree
);
assert(oddPartDegree(x^3*(x-1)^2*(x+2)^5)==2);
linearOrder = (f,rootValue) -> (
 local orderCount; local lin; orderCount=0; lin=x-rootValue;
 while f%lin==0 do (orderCount=orderCount+1;f=f//lin;);
 orderCount
);
valueAt=(f,v)->sub(f,{x=>v});
counts=new MutableHashTable; candidates={}; tested=0; primitive=0;
for mZero from 0 to 20 do for mInfinity from 0 to 20-mZero do
 for mOne from 0 to 20-mZero-mInfinity do (
  mMinus=20-mZero-mInfinity-mOne;
  p=x^mZero*(x-1)^mOne*(x+1)^mMinus;
  coeffs=apply(toList(0..2),j->sum(toList(0..6),i->coefficient(x^(3*i+j),p)*x^i));
  tested=tested+1;
  if max apply(coeffs,degOrMinusOne)==6 and coeffs#2!=0 then (
   common=gcd(gcd(coeffs#0,coeffs#1),coeffs#2);
   if (degree common)_0==0 then (
    primitive=primitive+1;
    disc=(coeffs#1)^2-4*(coeffs#0)*(coeffs#2);
    oddDegree=oddPartDegree disc;
    if counts#?oddDegree then counts#oddDegree=counts#oddDegree+1 else counts#oddDegree=1;
    if member(oddDegree,{3,4}) then (
     record={mZero,mInfinity,mOne,mMinus};
     candidates=append(candidates,record);
     print("GENUS_ONE_MULTIPLICITIES="|toString record);
     print("COEFFICIENTS="|toString coeffs);
     print("DISCRIMINANT="|toString disc);
     -- Count normalization points over the four target-C intersection points.
     pointCounts=apply({0,1,-1},bval->(
      aval=bval^3;
      leadingB=valueAt(coeffs#2,aval);
      assert(leadingB!=0);
      assert(valueAt(coeffs#1,aval)==-2*bval*leadingB);
      assert(valueAt(coeffs#0,aval)==bval^2*leadingB);
      if linearOrder(disc,aval)%2==1 then 1 else 2
     ));
     -- At (A,B)=(infinity,infinity), reverse degree-six coefficients.
     assert(degOrMinusOne(coeffs#0)==6);
     assert(degOrMinusOne(coeffs#1)<6 and degOrMinusOne(coeffs#2)<6);
     infinityDiscOrder=12-degOrMinusOne disc;
     infinityCount=if infinityDiscOrder%2==1 then 1 else 2;
     normalPointCount=sum pointCounts+infinityCount;
     assert(normalPointCount>=6);
     print("NORMALIZATION_INVERSE_POINT_COUNTS_0_1_MINUS1_INFINITY="|toString append(pointCounts,infinityCount));
     print("NORMALIZATION_INVERSE_POINT_TOTAL="|toString normalPointCount);
    );
   );
  );
 );
print("TOTAL_MULTIPLICITY_TUPLES="|toString tested);
print("PRIMITIVE_BIDEGREE_6_2_TUPLES="|toString primitive);
print("ODD_DISCRIMINANT_DEGREE_COUNTS="|toString pairs counts);
print("GENUS_ONE_CANDIDATES="|toString candidates);
assert(tested==1771 and primitive==171);
assert(candidates=={{2,2,4,12},{2,2,8,8},{2,2,12,4}});
print("SPECIAL_ROOT_TARGET_INCIDENCE_ENUMERATION_COMPLETE");
print("BIRATIONAL_ELLIPTIC_RESIDUAL_FOUR_ROOT_SPECIAL_LOCUS_EXCLUDED");
