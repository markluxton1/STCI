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
