-- Exact support for the restricted balanced-discriminant calculations.
-- Lower charts have inherited execution evidence. Degree ten now has separate
-- independent review/control; this comment edit is not a rerun. Degree twelve is OPEN.
-- Balanced four-contact target stratum: P(t)=R(t)^5.
-- R has four distinct nonzero roots; coefficients normalized leading/constant1.
-- This file builds an exact incidence, not a completed emptiness certificate.
R=QQ[symbol pa,symbol pb,symbol pc,symbol ss0,symbol ss1,symbol ss2,symbol ss3];
P=R[symbol tt];
quartic=tt^4+pa*tt^3+pb*tt^2+pc*tt+1;
p20=quartic^5;
T=R[symbol xx];
e=apply(toList(0..2),j->sum(toList(0..6),i->sub(coefficient(tt^(3*i+j),p20),R)*xx^i));
disc=e#1^2-4*e#0*e#2;
assert(sub(coefficient(xx^12,disc),R)==-5*(4*pb+3*pa^2));
assert(sub(coefficient(xx^0,disc),R)==-5*(4*pb+3*pc^2));
squareQuartic=xx^4+ss3*xx^3+ss2*xx^2+ss1*xx+ss0;
remnant=disc;
for j in reverse toList(8..12) do (
 remnant=remnant-coefficient(xx^j,remnant)*xx^(j-8)*squareQuartic^2;
);
equations=apply(toList(0..7),j->sub(coefficient(xx^j,remnant),R));
I=ideal equations;
stdio << "BALANCED_TARGET_SOURCE_BUILT" << endl;
stdio << "TARGET_COEFFICIENT_DEGREES=" << apply(e,f->degree f) << endl;
stdio << "REMAINDER_EQUATION_COUNT=" << #equations << endl;
stdio << "REMAINDER_TOTAL_DEGREES=" << apply(equations,f->(degree f)_0) << endl;
stdio << "EQUATION_TERM_COUNTS=" << apply(equations,f->#terms f) << endl;
stdio << "SQUARE_DIVISIBILITY_INCIDENCE_READY" << endl;
flush stdio;
-- The affine monic square-quartic chart excludes a square factor at infinity.
-- The omitted lower-degree square-factor charts must be handled separately.
-- Full projection admissibility also needs primitive bidegree, normalization
-- point counts, and the extension back to four actual global source sections.

rdisc=sub(resultant(quartic,diff(tt,quartic),tt),R);
svars={ss0,ss1,ss2,ss3};
for kk from 0 to 2 do (
 local sq; local residual; local eq; local targetDegree; local jj;
 sq=xx^kk+sum(toList(0..kk-1),i->svars#i*xx^i);
 targetDegree=4+2*kk;
 residual=sum(toList(0..targetDegree),i->coefficient(xx^i,disc)*xx^i);
 eq=apply(toList(targetDegree+1..12),i->sub(coefficient(xx^i,disc),R));
 if kk>0 then (
  for jj in reverse toList(2*kk..targetDegree) do (
   residual=residual-coefficient(xx^jj,residual)*xx^(jj-2*kk)*sq^2;
  );
  eq=join(eq,apply(toList(0..2*kk-1),i->sub(coefficient(xx^i,residual),R)));
 );
 stdio << "SQUARE_FACTOR_AFFINE_DEGREE=" << kk << endl; flush stdio;
 J=saturate(ideal eq,ideal rdisc);
 stdio << "SATURATED_IS_UNIT=" << (J==ideal 1_R) << endl;
 stdio << "SATURATED_DIMENSION=" << dim(R/J) << endl;
 stdio << "SATURATED_GROEBNER=" << gens gb J << endl; flush stdio;
);
print "LOWER_SQUARE_FACTOR_CHARTS_COMPLETED";
-- Exact one-parameter discriminant classification on affine degree10 chart.
R=QQ[symbol chartLambda]; P=R[symbol chartT];
supportQ=(20*chartLambda*chartT^4+20*chartLambda*chartT^3
 -15*chartLambda*chartT^2+(7*chartLambda+40)*chartT+20);
p20=supportQ^5;
T=R[symbol chartX];
e=apply(toList(0..2),j->sum(toList(0..6),i->sub(coefficient(chartT^(3*i+j),p20),R)*chartX^i));
disc=e#1^2-4*e#0*e#2;
assert(coefficient(chartX^12,disc)==0 and coefficient(chartX^11,disc)==0);
rdisc=sub(resultant(supportQ,diff(chartT,supportQ),chartT),R);
stdio << "RESULTANT_START" << endl; flush stdio;
discRes=sub(resultant(disc,diff(chartX,disc),chartX),R);
resFactors=toList factor discRes;
stdio << "REPEATED_ROOT_PARAMETER_FACTORS=" << resFactors << endl; flush stdio;
degreeUF=ff->if ff==0 then -1 else (degree ff)_0;
divideUF=(ff,gg,variable)->(
 local remainderUF; local quotientUF; local shiftUF; local multiplierUF;
 remainderUF=ff; quotientUF=0_(ring ff);
 while remainderUF!=0 and degreeUF(remainderUF)>=degreeUF(gg) do (
  shiftUF=degreeUF(remainderUF)-degreeUF(gg);
  multiplierUF=leadCoefficient(remainderUF)/leadCoefficient(gg)*variable^shiftUF;
  quotientUF=quotientUF+multiplierUF;
  remainderUF=remainderUF-multiplierUF*gg;
 );
 {quotientUF,remainderUF}
);
gcdUF=(ff,gg,variable)->(
 local rr; local aa; local bb;
 aa=ff;bb=gg;
 while bb!=0 do (rr=(divideUF(aa,bb,variable))#1;aa=bb;bb=rr;);
 if aa==0 then aa else aa*sub((1_(coefficientRing ring aa))/(leadCoefficient aa),ring aa)
);
oddPartDegree = (ff,variable) -> (
 if ff==0 then return -1;
 local cf; local wf; local mi; local yf; local zf; local outDegree;
 ff=ff*sub((1_(coefficientRing ring ff))/(leadCoefficient ff),ring ff);
 cf=gcdUF(ff,diff(variable,ff),variable); wf=(divideUF(ff,cf,variable))#0; mi=1; outDegree=0;
 while wf!=1 do (
  yf=gcdUF(wf,cf,variable); zf=(divideUF(wf,yf,variable))#0;
  if mi%2==1 then outDegree=outDegree+(degree zf)_0;
  wf=yf; cf=(divideUF(cf,yf,variable))#0; mi=mi+1;
 );
 outDegree
);
for pairF in resFactors do if (degree pairF#0)_0>0 then (
 fParam=pairF#0;
 K=toField(R/ideal fParam);
 KX=K[symbol fieldX];
 dK=(map(KX,T,{fieldX})) disc;
 rK=sub(rdisc,KX);
 if sub(chartLambda,KX)!=0 and rK!=0 and coefficient(fieldX^10,dK)!=0 then (
  od=oddPartDegree(dK,fieldX);
  stdio << "ADMISSIBLE_SUPPORT_FACTOR=" << fParam << " ODD_PART_DEGREE=" << od << endl; flush stdio;
 ) else (
  stdio << "DEGENERATE_OR_LOWER_DEGREE_FACTOR=" << fParam << endl; flush stdio;
 );
);
print "DEGREE_TEN_PARAMETER_CLASSIFICATION_COMPLETE";
