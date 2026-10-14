-- New regular-L2 higher-coefficient elimination from the accepted octic.
-- No inherited theorem or supporting checker is rerun.
outdir="research/validation/2026-10-13-generalization-quintic-l2";
save=(label,f)->((outdir|"/"|label|".txt") << toString f << close);
base=QQ[delta,a,B,G,J,p,q,kappa,tt];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
Gs=-(6*B+delta^2-3*delta)*q-(3*a-3*B+2*delta)*q^2+2*a*q^3;
Js=(-Gs*(1+3*q)-(6*B+5*delta^2-3*delta)*q-(3*a+3*B+delta-delta^2)*q^2+(a+B)*q^3)/2;
Fs=sub(sub(F,{G=>Gs,J=>Js,p=>q+tt}),{B=>kappa-a*q});
coeffs=apply(2..5,n->(sum select(terms Fs,mon->((exponents mon)#0)#8==n))//tt^n);
params=QQ[qpar,mpar]; paramField=frac params; calc=paramField[apar];
qp=sub(qpar,paramField); mp=sub(mpar,paramField);
Pc=qp^2-6*qp+6;
dv=3*(qp-2)*Pc/(qp*(qp-1)*(3-mp^2));
Dv=2*dv*(qp-1)+qp*(qp-2);
Ev=dv^2+dv*(3*qp-4)+qp*(qp-2);
kv=dv*(Ev+mp*dv^2/3)/Dv;
phi=map(calc,base,{dv,apar,0_calc,0_calc,0_calc,0_calc,qp,kv,0_calc});
fcover=apply(coeffs,f->phi f);
A=lift(diff(apar,fcover#0),paramField);
C=lift(sub(fcover#0,{apar=>0}),paramField);
av=-C/A;
save("cover-delta",dv); save("cover-kappa",kv); save("cover-a",av);
save("cover-f2-A",A); save("cover-f2-C",C);
numCoeffs=apply(1..3,ii->numerator lift(sub(fcover#ii,{apar=>av}),paramField));
scan(0..2,ii->(
    nn=numCoeffs#ii;
    save("cover-f"|toString(ii+3)|"-numerator",nn);
    print("f"|toString(ii+3)|" numerator degree="|toString degree nn);
    print("f"|toString(ii+3)|" factors="|toString factor nn)));
L1=3*kv*(qp-1)^2*Pc+dv*qp*(3-2*qp)*Pc-3*dv^2*(qp-1)^2*(qp-3);
allowed=qp*(qp-1)*(qp-2)*Pc*mp*(mp^2-3)*(qp*mp+3*qp-6)*numerator L1;
allowedNum=numerator allowed;
print("SATURATED COMPUTATION START");
I=saturate(ideal numCoeffs,ideal allowedNum);
save("generic-cover-saturated-ideal",I);
print("generic cover saturated ideal="|toString I);
print "COMPLETE regular L2 generic cover elimination";
