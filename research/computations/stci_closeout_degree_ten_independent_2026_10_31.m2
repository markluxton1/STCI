R=QQ[symbol ll]; P=R[symbol tt];
qq=20*ll*tt^4+20*ll*tt^3-15*ll*tt^2+(7*ll+40)*tt+20;
pp=qq^5; S=R[symbol xx];
ee=apply(toList(0..2),j->sum(toList(0..6),i->sub(coefficient(tt^(3*i+j),pp),R)*xx^i));
indDisc=ee#1^2-4*ee#0*ee#2;
indRes=sub(resultant(indDisc,diff(xx,indDisc),xx),R);
indFactors=toList factor indRes;
print("RESULTANT_FACTOR_DEGREES",apply(indFactors,z->(degree z#0)_0)); flush stdio;
indDeg=f->if f==0 then -1 else (degree f)_0;
indRem=(f,g,z)->(local h;h=f;while h!=0 and indDeg(h)>=indDeg(g) do h=h-leadCoefficient(h)/leadCoefficient(g)*z^(indDeg(h)-indDeg(g))*g;h);
indGcd=(f,g,z)->(local h;while g!=0 do (h=indRem(f,g,z);f=g;g=h;);f);
for ff in indFactors do if (degree ff#0)_0>0 then (
 K=toField(R/ideal ff#0); SX=K[symbol zz]; indH=(map(SX,S,{zz})) indDisc;
 if sub(ll,SX)!=0 and coefficient(zz^10,indH)!=0 then (
  indOdd=0; indSign=1; indSeq={indDeg(indH)};
  while indDeg(indH)>0 do (
   indG=indGcd(indH,diff(zz,indH),zz); indOdd=indOdd+indSign*(indDeg(indH)-indDeg(indG));indSign=-indSign;indH=indG;indSeq=append(indSeq,indDeg(indH));
  );
  print("FIELD_FACTOR_DEGREE",(degree ff#0)_0,"GCD_DEGREE_SEQUENCE",indSeq,"ODD_DEGREE",indOdd);flush stdio;
 );
);
print "INDEPENDENT_GCD_LAYER_CONTROL_COMPLETE";
