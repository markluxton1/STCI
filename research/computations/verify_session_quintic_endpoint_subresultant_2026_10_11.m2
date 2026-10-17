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
auditH=a*z^3+z-c-1;
auditV=aa*rr0-(aa*z-1)*pp0;
auditE=auditV^2-(3*z*aa-1)*auditH*auditV+aa*pp0*auditH^2;
auditJ=aa^2*auditH-a*auditV;
ccBoundary=a^2*c-a*b-b^3;
ddBoundary=a^3*d-a^2*b-2*a*b^2-b^4-a^2;

auditCheck("h simplifies the linear remainder",3*z^2*aa-1-pp0==auditH);
auditCheck("v expanded",auditV==aa^2*z^3+2*aa*z^2-aa*(c+1)*z+aa*d-a*z^3-z+c);
auditCheck("v alternate low-degree identity",auditV==aa*(d+z^2-b*z^3)+(aa*z-1)*auditH-1);
auditCheck("division without inverting A",aa*polyR-(aa^2*T+aa*z-1)*polyP==aa^2*auditH*T+auditV);

-- This is the fixed bidegree-(2,3) Sylvester matrix, with three P rows.
auditSylvester=matrix {
    {pp2,pp1,pp0,0,0},
    {0,pp2,pp1,pp0,0},
    {0,0,pp2,pp1,pp0},
    {rr3,rr2,rr1,rr0,0},
    {0,rr3,rr2,rr1,rr0}
};
auditCheck("fixed-degree resultant A^7 E",det auditSylvester==aa^7*auditE);
auditLinearResultant=pp2*auditV^2-pp1*aa^2*auditH*auditV+pp0*aa^4*auditH^2;
auditCheck("quadratic-linear resultant A^3 E",auditLinearResultant==aa^3*auditE);
auditCheck("cleared P at recovered finite root",pp2*auditV^2-pp1*aa^2*auditH*auditV+pp0*aa^4*auditH^2==aa^3*auditE);
auditCheck("denominator numerator at recovered root",aa^2*auditH-a*auditV==auditJ);

auditCheck("A=0 P has degree zero",sub(polyP,{b=>a*z})==-a*z^3-z+c);
auditCheck("A=0 R has degree one",sub(polyR,{b=>a*z})==T-a*z^4-2*z^2-z+d);
auditCheck("A=0 E is minus the constant P",sub(auditE,{b=>a*z})==a*z^3+z-c);
auditCheck("A=0 is not a generic common finite root",sub(auditE,{b=>a*z})!=0);
auditCheck("h=0 E specializes to v squared",sub(auditE-auditV^2,{c=>a*z^3+z-1})==0);

auditCheck("T=0 P evaluation",sub(polyP,{T=>0})==pp0);
auditCheck("T=0 R evaluation",sub(polyR,{T=>0})==rr0);
auditCheck("denominator P evaluation",a^2*pp0-a*pp1+pp2==ccBoundary);
auditCheck("denominator R evaluation",a^3*rr0-a^2*rr1+a*rr2-rr3==ddBoundary);
auditCheck("T=0 common-root specialization of E",sub(auditE,{c=>-2*a*z^3+3*b*z^2+z,d=>-3*a*z^4+4*b*z^3+2*z^2+z})==0);

print("PASS independent endpoint subresultant identities: "|toString auditChecks|" checks");
print("Resultant = (a*z-b)^7 * E, with E=v^2-(3*z*A-1)*h*v+A*p0*h^2");
print("Boundary P: "|toString ccBoundary);
print("Boundary R: "|toString ddBoundary);
