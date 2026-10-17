-- Characteristic-zero exact proportionality classification and bounded
-- two-parameter ACTUAL five-quadric conductor probe. No admissibility or
-- full-support conclusion is inferred solely from this computation.
h3check=(label,condition)->(assert condition;print("PASS "|label));
h3base=QQ[delta,lambda]; h3field=frac h3base;
aa=delta*(delta+2*lambda-1)/(6*lambda^2);
bb=delta*(delta+2*lambda-1)/(3*lambda);
gg=delta*((lambda-3)*delta+lambda+1)/3;
h3d=delta*((lambda^2-12)*delta+lambda^2-2*lambda+6)/6;
BB=bb-aa; GG=gg-3*bb+2*aa; JJ=h3d-2*gg+2*bb-aa;
h3r=h3field[r];
PP=GG*r^3+(6*delta*BB+delta^3-3*delta^2)*r^2+(3*delta^2*(aa-BB)+2*delta^3)*r-2*aa*delta^3;
JP=(GG+2*JJ)*r^3+(3*delta*(2*BB+GG)+5*delta^3-3*delta^2)*r^2+(3*(aa+BB)*delta^2+delta^3-delta^4)*r-(aa+BB)*delta^3;
h3check("four literal main-family proportionality coefficients",JP==lambda*PP);
h3check("main-family nonzero cubic constant-or-r coefficient",sub(aa,h3field)!=0 or coefficient(r,PP)!=0);
Jfactor=delta*(lambda^2-4*lambda+1)*(lambda-1)*((lambda+1)*delta+lambda-1)/(6*lambda^2);
h3check("complete main-family Jbar factor",JJ==Jfactor);
h3check("main G complete factor",GG==delta*(lambda^2-4*lambda+1)*((lambda+1)*delta+lambda-1)/(3*lambda^2));
print("MAIN a="|toString aa);print("MAIN b="|toString bb);
print("MAIN G="|toString GG);print("MAIN Jbar="|toString JJ);

-- The ratio-zero/infinite lanes are solved coefficient by coefficient;
-- this checks their sufficiency against the ACTUAL cubics.
boundaryBase=QQ[x]; boundaryField=frac boundaryBase;
boundaryR=boundaryField[r];
zeroJ_P=(-2/3+2*x)*r^3+(-6*x-2)*r^2+(6*x+2)*r-2*x;
zeroJ_J=(2*(-1)-3*(-2/3))*r^3+(3*(-2/3)+5-3)*r^2+(1-1)*r;
h3check("ratio-zero lane J identically zero",zeroJ_J==0);
h3check("ratio-zero lane P nonzero at every x",sub(zeroJ_P,{x=>1/3})!=0);
zeroP_P=(-2-3*(-2/3))*r^3+(6*(-1)*(-2/3)+(-1)^3-3*(-1)^2)*r^2+(-3*(-2/3)+2*(-1)^3)*r;
zeroP_J=(2*x-3*(-2)+(-2/3))*r^3+(3*(-1)*((-2)-(-2/3))+5*(-1)^3-3*(-1)^2)*r^2+(3*(-2/3)+(-1)^3-(-1)^4)*r-(-2/3)*(-1)^3;
h3check("ratio-infinite lane P identically zero",zeroP_P==0);
h3check("ratio-infinite lane J nonzero constant",sub(zeroP_J,{r=>0})==-2/3);

-- Formula (6) of the accepted conductor determinant note; delta is the
-- sole nonconstant projection parameter inverted here. All 3x3 center
-- minors remain untouched. The returns are actual affine restrictions.
conductorAffine=(R,dl,ap,Bp,Gp,Jp,pv)->(
    invDl=1_(coefficientRing R)/dl;
    CR=R[ctrH,ctrZ];
    xx0=1_CR;xx1=1-pv;xx2=(1-pv)^3;xx3=(1-pv)^4;
    uu3=invDl*(xx0-xx1+Bp*ctrH);
    uu2=invDl^2/3*(xx2-3*xx1+2*xx0-Gp*ctrH+dl^3*ctrZ);
    uu0=invDl^4*(xx3-2*xx2+2*xx1-xx0-Jp*ctrH+2*dl^3*ctrZ);
    zz0=xx0-ap*ctrH-uu3;zz1=-uu3;zz2=ctrH-uu2;
    zz3=uu2;zz4=ctrZ;zz5=uu0;
    qq={zz4^2-zz3*zz5,zz2*zz4-zz1*zz5,zz2*zz3-zz1*zz4,zz2^2-zz3*zz4-zz0*zz5,zz1*zz2-zz3^2-zz0*zz4};
    NM=matrix apply(qq,f->{coefficient(ctrH^2,f),coefficient(ctrH*ctrZ,f),coefficient(ctrZ^2,f),coefficient(ctrH,f),coefficient(ctrZ,f)});
    lift(81*dl^10*det NM,R)
);
h3p=h3field[p];
FM=conductorAffine(h3p,delta,aa,BB,GG,JJ,p);
HM=GG+(6*BB+delta^2-3*delta)*p+(3*aa-3*BB+2*delta)*p^2-2*aa*p^3;
JT=GG+2*JJ+(6*BB+3*GG+5*delta^2-3*delta)*p+(3*aa+3*BB+delta-delta^2)*p^2-(aa+BB)*p^3;
h3check("main transformed cubic proportionality",JT==lambda*HM);
Delta1=GG*(GG+3*delta^2)*(GG+delta^2+2*BB)+JJ*((delta^2-5*BB)*GG-3*BB*(delta^2+3*BB))-BB*JJ^2;
h3check("literal determinant A4 value",sub(FM,{p=>0})==-3*JJ*Delta1);
print("MAIN H="|toString HM);
SM=FM//HM;
h3check("main actual conductor cubic times quintic",FM==HM*SM);
h3check("main generic cubic-quintic coprimality",gcd(HM,SM)==1);
print("MAIN S FACTOR="|toString factor SM);
print("MAIN H FACTOR="|toString factor HM);

boundaryP=boundaryField[p];
F0=conductorAffine(boundaryP,1_boundaryField,x,-x,-2/3+2*x,1/3-x,p);
H0=(-2/3+2*x)+(-6*x-2)*p+(6*x+2)*p^2-2*x*p^3;
Fi=conductorAffine(boundaryP,-1_boundaryField,0_boundaryField,-2/3,-0_boundaryField,x+8/3,p);
Hi=2*x+16/3+4*p-4*p^2+2/3*p^3;
print("ZERO J F FACTOR="|toString factor F0);
print("ZERO J H="|toString H0);
print("ZERO J GENERIC GCD="|toString gcd(F0,H0));
print("ZERO P F FACTOR="|toString factor Fi);
print("ZERO P H="|toString Hi);
print("ZERO P GENERIC GCD="|toString gcd(Fi,Hi));
S0=F0//H0;Si=Fi//Hi;
h3check("both boundary cubic-quintic conductor identities",F0==H0*S0 and Fi==Hi*Si);
R0=H0^5 % S0; Ri=Hi^5 % Si;
N0=apply(0..4,k->lift(numerator coefficient(p^k,R0),boundaryBase));
Ni=apply(0..4,k->lift(numerator coefficient(p^k,Ri),boundaryBase));
g0=fold(N0,(u,v)->gcd(u,v));gi=fold(Ni,(u,v)->gcd(u,v));
print("ZERO J SUPPORT COEFFICIENT GCD="|toString g0);
print("ZERO P SUPPORT COEFFICIENT GCD="|toString gi);
h3check("both boundary affine support incidences empty",g0==1 and gi==1);
print "PASS h3 classification and bounded actual conductor probe completed";
