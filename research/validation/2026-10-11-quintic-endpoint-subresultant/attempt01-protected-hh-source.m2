-- Independent exact subresultant audit for the endpoint A4 projection chart.
-- Scope: the literal fixed C0 endpoint placement and the supplied P,R.
-- This proves polynomial identities, not a projection or STCI exclusion.
AuditRing=QQ[a,b,c,d,z,T];
auditChecks=0;
auditCheck=(label,condition)->(
    if not condition then error("FAIL: "|label);
    auditChecks=auditChecks+1;
);
aa=a*z-b;
pp0=2*a*z^3-3*b*z^2-z+c;
pp1=3*z*aa^2-aa;
pp2=aa^3;
rr0=3*a*z^4-4*b*z^3-2*z^2-z+d;
rr1=6*z^2*aa^2-4*z*aa-aa+1;
rr2=4*z*aa^3-2*aa^2;
rr3=aa^4;
polyP=pp0+pp1*T+pp2*T^2;
polyR=rr0+rr1*T+rr2*T^2+rr3*T^3;
hh=a*z^3+z-c-1;
vv=aa*rr0-(aa*z-1)*pp0;
ee=vv^2-(3*z*aa-1)*hh*vv+aa*pp0*hh^2;
jj=aa^2*hh-a*vv;
ccBoundary=a^2*c-a*b-b^3;
ddBoundary=a^3*d-a^2*b-2*a*b^2-b^4-a^2;

auditCheck("h simplifies the linear remainder",3*z^2*aa-1-pp0==hh);
auditCheck("v expanded",vv==aa^2*z^3+2*aa*z^2-aa*(c+1)*z+aa*d-a*z^3-z+c);
auditCheck("v alternate low-degree identity",vv==aa*(d+z^2-b*z^3)+(aa*z-1)*hh-1);
auditCheck("division without inverting A",aa*polyR-(aa^2*T+aa*z-1)*polyP==aa^2*hh*T+vv);

-- This is the fixed bidegree-(2,3) Sylvester matrix, with three P rows.
auditSylvester=matrix {
    {pp2,pp1,pp0,0,0},
    {0,pp2,pp1,pp0,0},
    {0,0,pp2,pp1,pp0},
    {rr3,rr2,rr1,rr0,0},
    {0,rr3,rr2,rr1,rr0}
};
auditCheck("fixed-degree resultant A^7 E",det auditSylvester==aa^7*ee);
auditLinearResultant=pp2*vv^2-pp1*aa^2*hh*vv+pp0*aa^4*hh^2;
auditCheck("quadratic-linear resultant A^3 E",auditLinearResultant==aa^3*ee);
auditCheck("cleared P at recovered finite root",pp2*vv^2-pp1*aa^2*hh*vv+pp0*aa^4*hh^2==aa^3*ee);
auditCheck("denominator numerator at recovered root",aa^2*hh-a*vv==jj);

auditCheck("A=0 P has degree zero",sub(polyP,{b=>a*z})==-a*z^3-z+c);
auditCheck("A=0 R has degree one",sub(polyR,{b=>a*z})==T-a*z^4-2*z^2-z+d);
auditCheck("A=0 E is minus the constant P",sub(ee,{b=>a*z})==a*z^3+z-c);
auditCheck("A=0 is not a generic common finite root",sub(ee,{b=>a*z})!=0);
auditCheck("h=0 E specializes to v squared",sub(ee-vv^2,{c=>a*z^3+z-1})==0);

auditCheck("T=0 P evaluation",sub(polyP,{T=>0})==pp0);
auditCheck("T=0 R evaluation",sub(polyR,{T=>0})==rr0);
auditCheck("denominator P evaluation",a^2*pp0-a*pp1+pp2==ccBoundary);
auditCheck("denominator R evaluation",a^3*rr0-a^2*rr1+a*rr2-rr3==ddBoundary);
auditCheck("T=0 common-root specialization of E",sub(ee,{c=>-2*a*z^3+3*b*z^2+z,d=>-3*a*z^4+4*b*z^3+2*z^2+z})==0);

print("PASS independent endpoint subresultant identities: "|toString auditChecks|" checks");
print("Resultant = (a*z-b)^7 * E, with E=v^2-(3*z*A-1)*h*v+A*p0*h^2");
print("Boundary P: "|toString ccBoundary);
print("Boundary R: "|toString ddBoundary);
