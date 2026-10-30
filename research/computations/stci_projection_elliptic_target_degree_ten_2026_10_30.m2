-- Reduced square-factor-degree3 chart after excluding zero middle coefficient.
-- Top coefficients force b=-3a²/4, c=(7a⁴+40)/(20a), a!=0.
-- After torus scaling t=a*y, lambda=a⁴ is the only support parameter.
R=QQ[symbol reducedLambda,symbol reducedS0,symbol reducedS1,symbol reducedS2];
P=R[symbol reducedT];
supportQ=(20*reducedLambda*reducedT^4+20*reducedLambda*reducedT^3
 -15*reducedLambda*reducedT^2+(7*reducedLambda+40)*reducedT+20);
p20=supportQ^5;
T=R[symbol reducedX];
e=apply(toList(0..2),j->sum(toList(0..6),i->sub(coefficient(reducedT^(3*i+j),p20),R)*reducedX^i));
disc=e#1^2-4*e#0*e#2;
stdio << "TOP_COEFFICIENTS=" << {coefficient(reducedX^12,disc),coefficient(reducedX^11,disc)} << endl; flush stdio;
assert(coefficient(reducedX^12,disc)==0 and coefficient(reducedX^11,disc)==0);
discCommon=0_R;
for j from 0 to 10 do discCommon=gcd(discCommon,sub(coefficient(reducedX^j,disc),R));
disc=disc//sub(discCommon,T);
stdio << "DISCRIMINANT_COMMON_PARAMETER_FACTOR=" << factor discCommon << endl; flush stdio;
squareCubic=reducedX^3+reducedS2*reducedX^2+reducedS1*reducedX+reducedS0;
remnant=disc;
for j in reverse toList(6..10) do (
 remnant=remnant-coefficient(reducedX^j,remnant)*reducedX^(j-6)*squareCubic^2;
);
I=ideal apply(toList(0..5),j->sub(coefficient(reducedX^j,remnant),R));
rdisc=sub(resultant(supportQ,diff(reducedT,supportQ),reducedT),R);
stdio << "REDUCED_DEGREE_TEN_SOURCE_BUILT" << endl; flush stdio;
J=saturate(I,ideal(reducedLambda*rdisc*discCommon*sub(coefficient(reducedX^10,disc),R)));
stdio << "SATURATED_IS_UNIT=" << (J==ideal 1_R) << endl;
stdio << "SATURATED_IDEAL=" << gens gb J << endl; flush stdio;
