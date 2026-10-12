-- Exact G=J=0 target-fiber reduction and all 21 root-profile certificates.
-- The companion note supplies the full-support and projective-fiber arguments.
profileCheck=(label,condition)->(assert(condition);print("PASS "|label));
R0=QQ[k,del][p];
F0=frac R0;
Bc=k*del^2;
af=2*k^2*del^2-k*del;
Es=del^2*(3-p)+3*Bc*(2-p);
Elinear=(1+3*k)*p-3-6*k;
P6=p^2-3*p+3;
Pc=p^2-6*p+6;
rs=del*(3-p)/(3*(2-p));
ls=del^4/(3*p^2*(2-p)^2);
ts=-del^4*P6*Pc/(9*p*(2-p)^2*Es);
W=(p*P6*Elinear^2-9*del*(p-2)*(k*p^2-2*k*p-1)*(2*k^2*p^2-6*k^2*p+k*p^2+6*k^2-4*k*p+6*k+1));
Lc=(1+3*k)^2-9*del*k^2*(1+2*k);
profileCheck("forced-a-rank-one-c-fiber",(-1/k)*af+Bc-del-del^2/(-1/k)==0);
profileCheck("off-branch-three-exact-target-constraints",del*rs^3-(del*rs+Bc)*ts-p*ls==0 and 3*del^2*rs^2-del^3*rs-p^2*(3-p)*ls==0 and del^4-2*del^3*rs+p^3*(2-p)*ls==0);
profileCheck("actual-normalization-quintic",rs^4-(2*rs^2+rs-af)*ts+ts^2-ls==del^3*Pc*W/(27*p^2*(2-p)^3*Elinear^2));
profileCheck("branch-denominator-and-c-collision",Es==-del^2*Elinear and p*(3-p)-3*(2-p)==-Pc);
W=sub(W,R0);
Lc=sub(Lc,R0);
Elinear=sub(Elinear,R0);
P6=sub(P6,R0);
Pc=sub(Pc,R0);
use R0;
profileCheck("leading-coefficient-and-p-two",sub(coefficient(p^5,W),R0)==Lc and sub(W,{p=>2})==2);
use R0;
profileCheck("denominator-zero-root-control",(3*(2-p)*W-del*P6^2*Pc)%ideal(Elinear)==0);
-- At P6=0 the two expressions for the exceptional source r agree;
-- Elinear=0 then makes delta*r+B=0, hence H12=H13=0.
profileCheck("cube-root-exceptional-rank-one",(del*(3-p)*(3-p)-3*del*(2-p))%ideal(P6)==0 and ((3-p)+3*k*(2-p))==-Elinear);
-- Qinf has roots -k*delta and delta/3 after G=0.  The first
-- is the forbidden Dr=0 value and cannot satisfy Pinf for k!=0.
R1=QQ[kk,dd,rr];
aa=2*kk^2*dd^2-kk*dd;
bb=kk*dd^2;
Linf=(1+3*kk)^2-9*dd*kk^2*(1+2*kk);
Pinf=-dd^2*rr^2+(bb^2-dd*bb+aa*dd^2)*rr+aa*dd*bb;
Qinf=3*dd^2*rr^2+(3*dd*bb-dd^3)*rr-dd^2*bb;
profileCheck("target-infinity-factor",Qinf==3*dd^2*(rr+kk*dd)*(rr-dd/3));
profileCheck("target-infinity-leading-drop-obstruction",sub(Pinf,{rr=>dd/3})==-dd^4*Linf/9 and sub(Pinf,{rr=>-kk*dd})==-kk^3*dd^5);
profileCheck("infinity-denominator-boundary",sub(Linf,{kk=>-1/3})==-dd/3);

-- All 21 coefficient systems admit polynomial Bezout identities 1=sum f_i*c_i.
-- No saturation, parameter denominator, generic rank, or numerical sampling.
S=QQ[s];
K=toField(S/ideal(s^2-3));
A=K[k,del];
R=A[p];
Elinear=(1+3*k)*p-3-6*k;
W=(p*(p^2-3*p+3)*Elinear^2-9*del*(p-2)*(k*p^2-2*k*p-1)*(2*k^2*p^2-6*k^2*p+k*p^2+6*k^2-4*k*p+6*k+1));
cc=apply(0..5,t->sub(coefficient(p^t,W),A));
leadC=last cc;
caseCount=0;
for i from 0 to 5 do for j from 0 to 5-i do (
    h=5-i-j;
    casePolynomial=p^i*(p-(3+s))^j*(p-(3-s))^h;
    hc=apply(0..4,t->sub(coefficient(p^t,casePolynomial),A));
    gg=toList(apply(0..4,t->cc#t-leadC*hc#t));
    mg=matrix{gg};
    unity=matrix{{1_A}};
    cert=unity//mg;
    assert(mg*cert==unity);
    print("PASS profile "|toString(i,j,h));
    print("CERTIFICATE "|toString(i,j,h)|" "|toString cert);
    caseCount=caseCount+1;
);
assert(caseCount==21);
print "PASS all ten structural checks and twenty-one polynomial Bezout certificates";
