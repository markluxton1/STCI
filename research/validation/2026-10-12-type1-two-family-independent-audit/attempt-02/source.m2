-- Independently reconstructed Type1 audit using eta^2=3, not familyRoot.
-- Direct r,T evaluation of projection sections, not owner's cleared Zi formulas.
checks=0;
type1Assert=(label,value)->(assert value; checks=checks+1; print("PASS "|toString checks|": "|label));
base=QQ[auditR,auditD,auditEta];
coeff=base/ideal(auditEta^2-3);
x=(auditEta+1)/2;
u=x*auditD^2;
w=(u+4*auditD^2)/3;
liftA=(u+w+auditD-auditD^2)/2;
liftB=liftA-u; liftG=liftA-w; liftD=liftA-u-w;
rho=auditD/2;
graphJ=(3*u+w)*auditD-3*auditD^3;
poly2=-u*w+(3*liftA+3*u)*auditD^2+3*auditD^3;
graphT=(graphJ+3*auditD^2)*auditR^2-(poly2-3*auditD^2*rho)*auditR+2*liftA*auditD^3;
resE=-u*w+auditD^4;
residualPoly=-3*auditD^2*auditR^3+poly2*auditR^2+((-3*liftA-u)*auditD^3-auditD^4)*auditR+liftA*auditD^4;
type1Assert("conic factor coefficient",graphJ*rho+resE==0);
type1Assert("residual factor reconstruction", residualPoly==(auditR-rho)*(-3*auditD^2*auditR^2+(poly2-3*auditD^2*rho)*auditR-2*liftA*auditD^3));
type1Assert("graph coefficient is nonzero on delta-open",graphJ==(5/3)*auditEta*auditD^3);
type1Assert("nonidentically zero graph T",sub(diff(auditR,graphT),{auditR=>rho})==-2*auditD^4);
L0=liftA-2*auditR^2-auditR;
L1=liftB-2*auditR^2-auditR+auditD*auditR;
L2=liftG-2*auditR^2-auditR+3*auditD*auditR;
L3=liftD-2*auditR^2-auditR+4*auditD*auditR;
normalP=auditR^3*L2-3*auditR*(auditR-auditD)^2*L1+2*(auditR-auditD)^3*L0;
normalJ=2*auditR^3*L3-3*auditR^2*(auditR-auditD)*L2+(auditR-auditD)^3*L1;
type1Assert("A4 tangent determinant factor",liftD-2*liftG+2*liftB-liftA==-(4/3)*auditEta*auditD^2);
type1Assert("P has conic root",sub(normalP,{auditR=>rho})==0);
type1Assert("J has conic root",sub(normalJ,{auditR=>rho})==0);
qP=normalP//(auditR-rho); qJ=normalJ//(auditR-rho);
type1Assert("P quotient reconstruction",normalP==(auditR-rho)*qP);
type1Assert("J quotient reconstruction",normalJ==(auditR-rho)*qJ);
K=5*auditD^3+9*auditEta*auditD^2+45*auditD+9*auditEta;
sigmaL=2*(auditEta*auditD+3);
sigmaN=auditD*((auditEta+2)*auditD+3);
type1Assert("sum of quadratic quotients",qP+qJ==-auditD^2*(sigmaL*auditR-sigmaN));
type1Assert("linear contact T",sub(graphT,{auditR=>rho})==auditD^4*(auditEta*auditD+1)/4);
actualIncidence=saturate(ideal(normalP,normalJ,graphT),ideal auditD);
expectedIncidence=intersect(ideal(auditR-rho,auditEta*auditD+1),ideal(K,sigmaL*auditR-sigmaN));
type1Assert("complete saturated incidence equality",actualIncidence==expectedIncidence);
type1Assert("linear/cubic strata disjoint",sub(K,{auditD=>-auditEta/3})==-32*auditEta/9);
type1Assert("sigma denominator cannot vanish on cubic stratum",sub(K,{auditD=>-auditEta})==-24*auditEta);
type1Assert("sigma differs from rho on delta-open",sub(sigmaL*auditR-sigmaN,{auditR=>rho})==-2*auditD^2);
type1Assert("cubic squarefree on eta branches",discriminant(K,auditD)==-746496);

-- Actual sections Xi(r,T); on c they are [r4,r3(r-d),r(r-d)3,(r-d)4].
actualSections=(r,t,delta,a,b,g,d)->(
    f0=r^4-(2*r^2+r)*t+t^2+a*t;
    f1=r^4-(2*r^2+r)*t+t^2-delta*(r^3-r*t)+b*t;
    f2=r^4-(2*r^2+r)*t+t^2-3*delta*(r^3-r*t)+3*delta^2*r^2-delta^3*r+g*t;
    f3=r^4-(2*r^2+r)*t+t^2-4*delta*(r^3-r*t)+6*delta^2*r^2-4*delta^3*r+delta^4+d*t;
    {f0,f1,f2,f3});

-- Finite coefficient algebras retain both eta branches and every K-root.
jetBase=QQ[auditJet,jetD,jetEta,inverseJ,inverseL];
jetX=(jetEta+1)/2;
jetU=jetX*jetD^2; jetW=(jetU+4*jetD^2)/3;
jetA=(jetU+jetW+jetD-jetD^2)/2;
jetB=jetA-jetU; jetG=jetA-jetW; jetLiftD=jetA-jetU-jetW;
jetJ=(3*jetU+jetW)*jetD-3*jetD^3;
jetP2=-jetU*jetW+(3*jetA+3*jetU)*jetD^2+3*jetD^3;
jetK=5*jetD^3+9*jetEta*jetD^2+45*jetD+9*jetEta;
jetL=2*(jetEta*jetD+3);
jetN=jetD*((jetEta+2)*jetD+3);

auditStratum=(label,eq,rootExpr,inverseLEq)->(
    ringS=jetBase/ideal(jetEta^2-3,eq,jetJ*inverseJ-1,inverseLEq);
    toS=map(ringS,jetBase);
    rr=toS(rootExpr)+auditJet;
    dd=toS(jetD); aa=toS(jetA); bb=toS(jetB); gg=toS(jetG); ddd=toS(jetLiftD);
    jj=toS(jetJ); pp=toS(jetP2);
    tt=((jj+3*dd^2)*rr^2-(pp-3*dd^3/2)*rr+2*aa*dd^3)*inverseJ;
    fs=actualSections(rr,tt,dd,aa,bb,gg,ddd);
    type1Assert(label|" actual Q equation",fs#0*fs#3-fs#1*fs#2==0);
    type1Assert(label|" intrinsic point lies on c",sub(tt,{auditJet=>0})==0);
    z0=sub(fs#0,{auditJet=>0});
    type1Assert(label|" x0 denominator unit",ideal(z0)==ideal(1_ringS));
    contact=(fs#0)^2*fs#2-(fs#1)^3;
    c0=sub(contact,{auditJet=>0});
    c1=sub(diff(auditJet,contact),{auditJet=>0});
    c2=sub(diff(auditJet,diff(auditJet,contact)),{auditJet=>0})/2;
    type1Assert(label|" constant coefficient zero",c0==0);
    type1Assert(label|" linear coefficient zero",c1==0);
    type1Assert(label|" quadratic coefficient unit",ideal(c2)==ideal(1_ringS));
    print(label|" independently evaluated quadratic coefficient:"); print c2;
    );
auditStratum("linear",jetEta*jetD+1,jetD/2,inverseL-1);
auditStratum("cubic",jetK,jetN*inverseL,jetL*inverseL-1);
print("TOTAL PASS CONDITIONS: "|toString checks);
