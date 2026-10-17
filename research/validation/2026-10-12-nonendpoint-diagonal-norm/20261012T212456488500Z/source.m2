-- Literal auxiliary identities; no conductor identification is inferred from
-- matching degrees. The separate owner must justify the determinant's geometry.
diagCheck=(label,condition)->(assert(condition);print("PASS "|label));
diagBase=QQ[delta,a,B,G,J,p];
diagRing=diagBase[r];
Z=G*p*(2-p)+J*(3-p);
Ac=(3*delta^2+G)*p*(2-p)+J*(3-p);
q1=delta*(delta^2*p*(p-3)+3*B*p*(2-p)+G*(2-p)-J);
q0=delta^2*(B*p*(p-3)-G);
Q2=Ac*r^2+q1*r+q0;
N=delta^2*(p*r-delta)*(3*(2-p)*r-delta*(3-p));
M=delta^2*(3*J*r^2+delta*(2*G-J)*r-delta^2*G);
Psi=p^2*Z^2*r^4+p^2*Z*(2*r^2+r-a)*N+p^2*N^2-M*Z;
C3=Psi//(p*r-delta);
diagCheck("literal cubic residual and cubic coefficient",Psi==(p*r-delta)*C3 and coefficient(r^3,C3)==p*Ac^2);

Pc=p^2-6*p+6;
V=(3-2*p)*J+p*(4-3*p)*G+p*(delta^2+B*p)*Pc;
W=3*J*(2-p)+2*G*p*(3-2*p)+p*(2*delta^2+delta*p-a*p^2)*Pc;
Pcub=G*r^3+(6*delta*B+delta^3-3*delta^2)*r^2+(3*delta^2*(a-B)+2*delta^3)*r-2*a*delta^3;
Jcub=(G+2*J)*r^3+(3*delta*(2*B+G)+5*delta^3-3*delta^2)*r^2+(3*(a+B)*delta^2+delta^3-delta^4)*r-(a+B)*delta^3;
Pt=G+(6*B+delta^2-3*delta)*p+(3*a-3*B+2*delta)*p^2-2*a*p^3;
Jt=G+2*J+(6*B+3*G+5*delta^2-3*delta)*p+(3*a+3*B+delta-delta^2)*p^2-(a+B)*p^3;
diagCheck("diagonal conormal matrix",2*V==-(3-p)*Pt+(3-2*p)*Jt and 2*W==(p^2-3*p-6)*Pt+3*(2-p)*Jt);
diagCheck("diagonal conormal determinant",det matrix{{-(3-p),3-2*p},{p^2-3*p-6,3*(2-p)}}==2*p*Pc);
H12d=G+(3-p)*(delta^2+B*p);
H13d=J-p*(2-p)*(delta^2+B*p);
diagCheck("exceptional conormal determinant remains on Z boundary",(3-p)*V-(3-2*p)*Z==p*Pc*H12d and (2-p)*V-(4-3*p)*Z==-Pc*H13d);

c2=coefficient(r^2,C3); c1=coefficient(r,C3); c0=sub(C3,{r=>0});
Kc=c2-p*Ac*q1; Ec=c1-p*Ac*q0;
linU=Ac*Ec-Kc*q1; linV=Ac*c0-Kc*q0;
diagCheck("compact linear subresultant",Ac*C3-(p*Ac^2*r+Kc)*Q2==linU*r+linV);
Norm=Ac*q0*Ec^2-q1*Kc*q0*Ec-Ac*q1*Ec*c0+q1^2*Kc*c0+Ac^2*c0^2-2*Ac*Kc*q0*c0+Kc^2*q0^2;
diagCheck("fixed degree Sylvester factor",resultant(Q2,C3,r)==Ac*Norm);
nlLead=3*delta^2*p*(2-p); nlMid=-delta^3*(6-p^2);
diagCheck("cubic degree drop coefficient",c2==Ac*(p*(2*nlMid+nlLead)+delta*Ac)-p*nlLead^2);
dropDifference=Norm-c2*(c2*q0^2-c1*q1*q0+c0*q1^2);
dropQuot=dropDifference//Ac;
diagCheck("leading drop normalized resultant",dropDifference==Ac*dropQuot);

F=Norm//(p^2*delta^6*Z^2);
diagCheck("primitive norm exact factor",Norm==p^2*delta^6*Z^2*F);
Fb=lift(F,diagBase);
Delta1=G*(G+3*delta^2)*(G+delta^2+2*B)+J*((delta^2-5*B)*G-3*B*(delta^2+3*B))-B*J^2;
diagCheck("primitive degree eight and A4 value",max apply(exponents Fb,ee->ee#5)==8 and sub(Fb,{p=>0})==-3*J*Delta1);
leadF=(sum select(terms Fb,tt->((exponents tt)#0)#5==8))//p^8;
Pinf=-delta^2*r^2+(B^2-delta*B+a*delta^2)*r+a*delta*B;
Qinf=(3*delta^2+G)*r^2+(3*delta*B-delta^3)*r-delta^2*B;
diagCheck("endpoint infinity leading coefficient",resultant(Pinf,Qinf,r)==B^2*delta^2*leadF and sub(leadF,{B=>0})==a*G*((3*delta^2+G)*a-delta^3));

-- Independent literal restriction of the accepted five quadrics, with two
-- omitted projection variables. This checks the identity, not its geometric
-- status as an actual conductor equation.
diagField=frac diagBase;
evalDiag=map(diagField,diagRing,{delta/p});
diagCheck("diagonal quadratic evaluation",p^2*evalDiag(Q2)==delta^2*V);
diagCheck("diagonal cubic evaluation",p^2*evalDiag(C3)==delta^3*Z*W);
diagCheck("normalized actual conormal cubic pair",p^3*evalDiag(Pcub)==delta^3*Pt and p^3*evalDiag(Jcub)==delta^3*Jt);
ctrRing=diagField[ctrH,ctrZ];
xx0=1_ctrRing; xx1=1-p; xx2=(1-p)^3; xx3=(1-p)^4;
uu3=(xx0-xx1+B*ctrH)/delta;
uu2=(xx2-3*xx1+2*xx0-G*ctrH+delta^3*ctrZ)/(3*delta^2);
uu0=(xx3-2*xx2+2*xx1-xx0-J*ctrH+2*delta^3*ctrZ)/delta^4;
zz0=xx0-a*ctrH-uu3; zz1=-uu3; zz2=ctrH-uu2;
zz3=uu2; zz4=ctrZ; zz5=uu0;
qq={zz4^2-zz3*zz5,zz2*zz4-zz1*zz5,zz2*zz3-zz1*zz4,zz2^2-zz3*zz4-zz0*zz5,zz1*zz2-zz3^2-zz0*zz4};
coeffFive=matrix apply(qq,qqi->{coefficient(ctrH^2,qqi),coefficient(ctrH*ctrZ,qqi),coefficient(ctrZ^2,qqi),coefficient(ctrH,qqi),coefficient(ctrZ,qqi)});
Dc=det coeffFive;
diagCheck("literal five by five determinant restriction",sub(Fb,diagField)==81*delta^10*Dc);
"/private/tmp/nonendpoint_verified_primitive_norm_2026_10_12.txt" << toString Fb << close;
print "PASS all fifteen auxiliary diagonal and norm checks";
