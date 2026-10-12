-- Exact identities supporting the independently audited 2B+2F endpoint proof.
-- No finite search or exhaustive parameter-space claim is made by this script.
checks=0;
proofCheck=(label,condition)->(
    if not condition then error("FAIL: "|label);
    checks=checks+1;
    print("PASS "|label);
);
R=QQ[aDH,bDH,yDH,cDH,ADH,BDH,CDH,dDH,eDH,rDH,tDH,vDH,wDH,hDH];
F=(-cDH*aDH^2*bDH^2
  +yDH*((bDH-aDH)*(ADH+BDH*bDH+CDH*bDH^2)+cDH*aDH-aDH*bDH^2*(dDH+eDH*bDH))
  +yDH^2*(dDH+eDH*bDH));
proofCheck("actual lifted curve identity",sub(F,{aDH=>rDH,bDH=>rDH,yDH=>rDH^3})==0);
proofCheck("entire exceptional divisor 2B plus 2F",sub(F,{yDH=>0})==-cDH*aDH^2*bDH^2);
proofCheck("normal coefficient on the horizontal curve",sub(diff(yDH,F),{aDH=>0,yDH=>0})==bDH*(ADH+BDH*bDH+CDH*bDH^2));
proofCheck("normality excludes A=c on whole vertical curve",sub(diff(yDH,F),{bDH=>0,yDH=>0})==aDH*(cDH-ADH));
proofCheck("other first derivatives vanish on that vertical curve",sub(diff(aDH,F),{bDH=>0,yDH=>0})==0 and sub(diff(bDH,F),{bDH=>0,yDH=>0})==0);
proofCheck("homogeneous normal coefficient in infinity chart",sub(ADH*tDH^2+BDH*tDH+CDH,{tDH=>0})==CDH);
proofCheck("nonzero simple-contact quartic kernel coefficient",sub(F,{aDH=>ADH*tDH,bDH=>(ADH-cDH)*tDH,yDH=>0})==-cDH*ADH^2*(ADH-cDH)^2*tDH^4);
Ffactor=-cDH*bDH^2*aDH^2+(wDH-cDH*bDH^2*vDH)*aDH*yDH+hDH*yDH+vDH*wDH*yDH^2;
XX=aDH+vDH*yDH;
YY=-cDH*bDH^2*aDH+wDH*yDH;
ss=wDH+cDH*bDH^2*vDH;
proofCheck("exact binary quadratic factorization",Ffactor==XX*YY+hDH*yDH);
proofCheck("inverse coordinate denominator",YY+cDH*bDH^2*XX==ss*yDH);
proofCheck("translated A-type equation with denominators cleared",ss^2*Ffactor==(ss*XX+hDH)*(ss*YY+cDH*bDH^2*hDH)-cDH*bDH^2*hDH^2);
proofCheck("horizontal valuations after translation",sub(ss*XX+hDH,{aDH=>0,yDH=>0})==hDH and sub(ss*YY+cDH*bDH^2*hDH,{aDH=>0,yDH=>0})==cDH*bDH^2*hDH);
cartanA=(nn)->matrix apply(toList(1..nn),ii->apply(toList(1..nn),jj->if ii==jj then 2_QQ else if abs(ii-jj)==1 then -1_QQ else 0_QQ));
G3=inverse cartanA(3);
G5=inverse cartanA(5);
G7=inverse cartanA(7);
proofCheck("A3 same endpoint contact budget",G3_(0,0)+G3_(0,0)==3/2);
proofCheck("A5 internal-node contact budget",G5_(1,1)==4/3 and G5_(1,4)==2/3 and G5_(1,1)+G5_(1,4)==2);
proofCheck("A7 internal-node contact budget",G7_(2,2)==15/8 and G7_(2,6)==5/8 and G7_(2,2)+G7_(2,6)==5/2);
assert(checks==14);
print("PASS genus-two double-horizontal endpoint identities: "|toString checks|" checks");
