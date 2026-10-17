-- Exact identities supporting the independently audited 2B+2F endpoint proof.
-- No finite search or exhaustive parameter-space claim is made by this script.
checks=0;
proofCheck=(label,condition)->(
    if not condition then error("FAIL: "|label);
    checks=checks+1;
    print("PASS "|label);
);
R=QQ[aa,bb,yy,cc,pA,pB,pC,dd,ee,rr,tt,vv,ww,hh];
F=-cc*aa^2*bb^2
  +yy*((bb-aa)*(pA+pB*bb+pC*bb^2)+cc*aa-aa*bb^2*(dd+ee*bb))
  +yy^2*(dd+ee*bb);
proofCheck("actual lifted curve identity",sub(F,{aa=>rr,bb=>rr,yy=>rr^3})==0);
proofCheck("entire exceptional divisor 2B plus 2F",sub(F,{yy=>0})==-cc*aa^2*bb^2);
proofCheck("normal coefficient on the horizontal curve",sub(diff(yy,F),{aa=>0,yy=>0})==bb*(pA+pB*bb+pC*bb^2));
proofCheck("normality excludes A=c on whole vertical curve",sub(diff(yy,F),{bb=>0,yy=>0})==aa*(cc-pA));
proofCheck("other first derivatives vanish on that vertical curve",sub(diff(aa,F),{bb=>0,yy=>0})==0 and sub(diff(bb,F),{bb=>0,yy=>0})==0);
proofCheck("homogeneous normal coefficient in infinity chart",sub(pA*tt^2+pB*tt+pC,{tt=>0})==pC);
proofCheck("nonzero simple-contact quartic kernel coefficient",sub(F,{aa=>pA*tt,bb=>(pA-cc)*tt,yy=>0})==-cc*pA^2*(pA-cc)^2*tt^4);
Ffactor=-cc*bb^2*aa^2+(ww-cc*bb^2*vv)*aa*yy+hh*yy+vv*ww*yy^2;
XX=aa+vv*yy;
YY=-cc*bb^2*aa+ww*yy;
ss=ww+cc*bb^2*vv;
proofCheck("exact binary quadratic factorization",Ffactor==XX*YY+hh*yy);
proofCheck("inverse coordinate denominator",YY+cc*bb^2*XX==ss*yy);
proofCheck("translated A-type equation with denominators cleared",ss^2*Ffactor==(ss*XX+hh)*(ss*YY+cc*bb^2*hh)-cc*bb^2*hh^2);
proofCheck("horizontal valuations after translation",sub(ss*XX+hh,{aa=>0,yy=>0})==hh and sub(ss*YY+cc*bb^2*hh,{aa=>0,yy=>0})==cc*bb^2*hh);
cartanA=(nn)->matrix apply(1..nn,ii->apply(1..nn,jj->if ii==jj then 2_QQ else if abs(ii-jj)==1 then -1_QQ else 0_QQ));
G3=inverse cartanA(3);
G5=inverse cartanA(5);
G7=inverse cartanA(7);
proofCheck("A3 same endpoint contact budget",G3_(0,0)+G3_(0,0)==3/2);
proofCheck("A5 internal-node contact budget",G5_(1,1)==4/3 and G5_(1,4)==2/3 and G5_(1,1)+G5_(1,4)==2);
proofCheck("A7 internal-node contact budget",G7_(2,2)==15/8 and G7_(2,6)==5/8 and G7_(2,2)+G7_(2,6)==5/2);
assert(checks==14);
print("PASS genus-two double-horizontal endpoint identities: "|toString checks|" checks");
