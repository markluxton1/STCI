-- Exact local-excess coefficients for the displayed endpoint projection.
-- This checker supplies polynomial/rational identities; the accompanying
-- note supplies full-support and local-intersection quantifiers.
localCheck=(label,condition)->(
    assert(condition);
    print("PASS "|label);
);

globalCoeffs=QQ[qa,qb,qg,qd];
globalFraction=frac globalCoeffs;
globalRing=globalFraction[qr,qT];
globalK=(qa*(qr^4-(2*qr^2+qr)*qT+qT^2)-qb*(qr^3-qr*qT)
    -qr^2-(1+qg)*qr+qd+(1+qa*qd-qb*qg)*qT);
globalU=qg-qr-3*qb*qr^2+2*qa*qr^3;
globalE=(globalU+qT*(qa^2*qr^3+2*qa*(qg-qr)-3*qb^2*qr)
    +qT^2*(qa^2*(qg-qr)-qb^3));
globalRes=resultant(globalK,globalE,qT);
globalH=globalRes//((qa*qr-qb)^2);
localCheck("global-resultant-division",globalRes==globalH*(qa*qr-qb)^2);
localCheck("global-H-degree-seven",globalH==sum(0..7,j->coefficient(qr^j,globalH)*qr^j)
    and coefficient(qr^7,globalH)==-qa^4);

localCoeffs=QQ[la,lw,lz];
localFraction=frac localCoeffs;
localRing=localFraction[lh,lT];
localB=la*lz-lw;
localR=lz+lh;
localG=lz+3*localB*lz^2-2*la*lz^3;
localD=lz+2*lz^2+4*localB*lz^3-3*la*lz^4;
localK=(la*(localR^4-(2*localR^2+localR)*lT+lT^2)
    -localB*(localR^3-localR*lT)-localR^2-(1+localG)*localR
    +localD+(1+la*localD-localB*localG)*lT);
localU=localG-localR-3*localB*localR^2+2*la*localR^3;
localE=(localU+lT*(la^2*localR^3+2*la*(localG-localR)-3*localB^2*localR)
    +lT^2*(la^2*(localG-localR)-localB^3));
localRes=resultant(localK,localE,lT);
localH=localRes//((la*localR-localB)^2);
localS1=1+3*lw*lz^2*(3*la*lz-lw);
localS2=1-6*lw*lz+3*lw^2*lz*(2*lz+1);
localM=1-3*lz^2*lw^2;
localP1=-3*lz*lw^2;
localP2=-lw^2*(3*la*lz-lw);
localCheck("local-H-linear-coefficient",coefficient(lh,localH)==-lw*localS1*localS2);
localCheck("endpoint-avoidance-L",la^2*localG-la*localB-localB^3
    ==lw*(la+lw^2-3*la*lw*lz));
localCheck("second-T-root",la*localP1-localM*localP2==-lw^3*localS1);

paramBase=QQ[q];
fracBase=frac paramBase;
AA=fracBase[a];
BB=AA[h,T];
ww=2-2*q-1/(3*q);
zz=q/ww;
bbpar=a*zz-ww;
rr=zz+h;
gg=zz+3*bbpar*zz^2-2*a*zz^3;
delpar=zz+2*zz^2+4*bbpar*zz^3-3*a*zz^4;
K=(a*(rr^4-(2*rr^2+rr)*T+T^2)-bbpar*(rr^3-rr*T)
    -rr^2-(1+gg)*rr+delpar+(1+a*delpar-bbpar*gg)*T);
UU=gg-rr-3*bbpar*rr^2+2*a*rr^3;
E=(UU+T*(a^2*rr^3+2*a*(gg-rr)-3*bbpar^2*rr)
    +T^2*(a^2*(gg-rr)-bbpar^3));
Res=resultant(K,E,T);
hhPoly=Res//((a*rr-bbpar)^2);
localCheck("S2-parametrization",1-6*ww*zz+3*ww^2*zz*(2*zz+1)==0);
localCheck("param-H-linear-coefficient",coefficient(h,hhPoly)==0);
ccTwo=sub(coefficient(h^2,hhPoly),AA);
ccThree=sub(coefficient(h^3,hhPoly),AA);
ccFour=sub(coefficient(h^4,hhPoly),AA);
sOne=1+3*ww*zz^2*(3*a*zz-ww);
ccTwoReduced=ccTwo//sOne;
localCheck("param-H-quadratic-factor",ccTwoReduced*sOne==ccTwo);
localCheck("special-q-one-third",substitute(ccTwoReduced,{q=>1/3})==-1/27);
aaContact=(-sub(coefficient(1_AA,ccTwoReduced),fracBase)
    /sub(coefficient(a,ccTwoReduced),fracBase));
discPoly=6*q^2-6*q+1;
quarticPoly=54*q^4-72*q^3+15*q^2-3*q+1;
localCheck("high-contact-a",aaContact==-discPoly^2*quarticPoly/(27*q^3*(3*q-1)^2));
contactEval=map(fracBase,AA,{aaContact});
threeAtContact=contactEval ccThree;
fourAtContact=contactEval ccFour;
nSix=162*q^6-216*q^5+72*q^4-27*q^3-3*q^2+6*q-1;
nNine=(8748*q^9-20412*q^8+18954*q^7-8262*q^6+1458*q^5
    -252*q^4+180*q^3-66*q^2+12*q-1);
localCheck("high-contact-cubic-coefficient",threeAtContact
    ==discPoly^3*nSix*nNine/(2187*q^7*(3*q-1)^4));
localCheck("S1-high-contact",contactEval sOne==-nSix/(3*q-1)^2);
use BB;
uRem=UU//h;
wRem=sub(K,{T=>0})//h;
moreContact=contactEval sub(resultant(uRem,wRem,h),AA);
localCheck("high-contact-order-at-most-four",gcd(numerator threeAtContact,numerator fourAtContact)==discPoly^3);
localCheck("order-four-no-other-common-root",gcd(numerator threeAtContact,numerator moreContact)==discPoly^3);
use paramBase;
exportThree=sub(numerator threeAtContact,paramBase);
exportFour=sub(numerator fourAtContact,paramBase);
exportMore=sub(numerator moreContact,paramBase);
print("COEFF3="|toString apply(0..(first degree exportThree),j->coefficient(q^j,exportThree)));
print("COEFF4="|toString apply(0..(first degree exportFour),j->coefficient(q^j,exportFour)));
print("COEFFMORE="|toString apply(0..(first degree exportMore),j->coefficient(q^j,exportMore)));
print "PASS all fourteen endpoint local-excess identity checks";
