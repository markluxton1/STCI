-- Bounded independent checks of statements not asserted by the owner's
-- seventeen-identity checker. No parameter-space exhaustion is claimed.
gapCheck=(label,condition)->(assert(condition);print("PASS "|label));
R=QQ[delta,a,Bc,Gc,Jc,p,r,u];
Z=Gc*p*(2-p)+Jc*(3-p);
Ac=Z+3*delta^2*p*(2-p);
N=delta^2*(p*r-delta)*(3*(2-p)*r-delta*(3-p));
M=delta^2*(3*Jc*r^2+delta*(2*Gc-Jc)*r-delta^2*Gc);
Psi=p^2*Z^2*r^4+p^2*Z*(2*r^2+r-a)*N+p^2*N^2-M*Z;
C3=Psi//(p*r-delta);
gapCheck("regular-cubic-leading-coefficient",coefficient(r^3,C3)==p*Ac^2);
gapCheck("finite-ell-quadric",(u-1)*(u-1+4*delta)-(u-1+delta)*(u-1+3*delta)==-3*delta^2);
P6=p^2-3*p+3;
Pc=p^2-6*p+6;
Vp=p*(3-p)^2*P6-9*delta*(2-p);
gapCheck("pure-monic-degree-five-and-next-coefficient",coefficient(p^5,Vp)==1 and coefficient(p^4,Vp)==-9);
gapCheck("pure-remainder-mod-Pc",Vp%Pc==9*((5*p-6)-delta*(2-p)));
gapCheck("pure-remainder-mod-P6",Vp%P6==-9*delta*(2-p));
gapCheck("pure-forced-root-not-Pc",sub(Pc,{p=>9/5})==-39/25);
gapCheck("pure-Mobius-determinant",det matrix{{5,-6},{-1,2}}==4);
Pinf=-delta^2*r^2+(Bc^2-delta*Bc+a*delta^2)*r+a*delta*Bc;
Qinf=(3*delta^2+Gc)*r^2+(3*delta*Bc-delta^3)*r-delta^2*Bc;
-- Clear the denominator in delta*Pinf(-Bc/delta) before substitution.
gapCheck("endpoint-no-denominator-root",-delta*Bc^2-(Bc^2-delta*Bc+a*delta^2)*Bc+a*delta^2*Bc==-Bc^3);
gapCheck("endpoint-B-zero-factorization",sub(Pinf,{Bc=>0})==delta^2*r*(a-r) and sub(Qinf,{Bc=>0})==r*((3*delta^2+Gc)*r-delta^3));
gapCheck("open-GJzero-infinity-factor",sub(Qinf,{Gc=>0})==delta*(delta*r+Bc)*(3*r-delta));
Vlead=delta^5+6*delta^3*Bc-9*delta^2*Bc^2+9*delta*Bc^2-18*Bc^3;
-- Pforced is delta^2*Pinf after a=2*Bc^2/delta^2-Bc/delta.
Pforced=-delta^4*r^2+delta^2*(3*Bc^2-2*delta*Bc)*r+2*delta*Bc^3-delta^2*Bc^2;
gapCheck("open-GJzero-leading-coefficient-infinity-bridge",9*sub(Pforced,{r=>delta/3})==-delta*Vlead);
print "PASS all eleven bounded independent proof-gap checks";
