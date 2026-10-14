-- New compact discriminant and coefficient-drop analysis on regular L2.
outdir="research/validation/2026-10-13-generalization-quintic-l2";
save=(label,f)->((outdir|"/"|label|".txt") << toString f << close);
orig=QQ[delta,a,B,G,J,p,q,kappa,tt];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
Gs=-(6*B+delta^2-3*delta)*q-(3*a-3*B+2*delta)*q^2+2*a*q^3;
Js=(-Gs*(1+3*q)-(6*B+5*delta^2-3*delta)*q-(3*a+3*B+delta-delta^2)*q^2+(a+B)*q^3)/2;
Fs=sub(sub(F,{G=>Gs,J=>Js,p=>q+tt}),{B=>kappa-a*q});
fs=apply(2..5,n->(sum select(terms Fs,mon->((exponents mon)#0)#8==n))//tt^n);
L2=(3*q*(q-1)*(2*delta*(q-1)+q*(q-2))*kappa^2-6*delta*q*(q-1)*(delta^2+delta*(3*q-4)+q*(q-2))*kappa+delta^5*q+3*delta^4*(q-1)*(3*q-2)+6*delta^3*q*(q-1)*(2*q-3)+3*delta^2*q^2*(q-1)*(q-2));
disc=(diff(kappa,L2))^2-4*(diff(kappa,diff(kappa,L2))/2)*L2;
print("L2 discriminant="|toString factor disc);save("L2-discriminant",disc);
small=QQ[dp,qp]; sf=frac small; K=sf[kp,ap];
phi=map(K,orig,{sub(dp,K),ap,0_K,0_K,0_K,0_K,sub(qp,K),kp,0_K});
ell=phi L2;
fc=apply(fs,f->phi f); aa=diff(ap,fc#0); ac=sub(fc#0,{ap=>0});
L1=phi(3*kappa*(q-1)^2*(q^2-6*q+6)+delta*q*(3-2*q)*(q^2-6*q+6)-3*delta^2*(q-1)^2*(q-3));
redA=aa%ell; symProduct=(L1*diff(kp,ell))%ell;
ratio=lift(diff(kp,redA),sf)/lift(diff(kp,symProduct),sf);
assert(redA==ratio*symProduct);
print("A mod L2 equals ratio L1 L2_k; ratio="|toString factor ratio);
save("A-L1-L2prime-ratio",ratio);
print("Res A L2="|toString factor resultant(aa,ell,kp));
-- Discriminant-zero cover away from q=2: m=0, k=d E/D.
qv=sub(qp,sf); Pc=qv^2-6*qv+6;
dv=(qv-2)*Pc/(qv*(qv-1));
kv=dv*(dv^2+dv*(3*qv-4)+qv*(qv-2))/(2*dv*(qv-1)+qv*(qv-2));
dropmap=map(sf,orig,{dv,0_sf,0_sf,0_sf,0_sf,0_sf,qv,kv,0_sf});
print("m0 f2="|toString factor dropmap sub(fs#0,{a=>0}));
print("m0 L1="|toString factor dropmap(3*kappa*(q-1)^2*(q^2-6*q+6)+delta*q*(3-2*q)*(q^2-6*q+6)-3*delta^2*(q-1)^2*(q-3)));
save("m0-f2",dropmap sub(fs#0,{a=>0}));
-- Leading coefficient D=0: solve d=-q(q-2)/(2(q-1)).
dv2=-qv*(qv-2)/(2*(qv-1));
dropcalc=sf[kdrop,adrop];
drop2=map(dropcalc,orig,{dv2,adrop,0_dropcalc,0_dropcalc,0_dropcalc,0_dropcalc,qv,kdrop,0_dropcalc});
ell2=drop2 L2;
print("D0 L2="|toString factor ell2);
kv2=-lift(sub(ell2,{kdrop=>0}),sf)/lift(diff(kdrop,ell2),sf);
print("D0 k="|toString factor kv2);
fa2=sub(drop2(fs#0),{kdrop=>kv2});
aval2=-lift(sub(fa2,{adrop=>0}),sf)/lift(diff(adrop,fa2),sf);
print("D0 f2 A="|toString factor diff(adrop,fa2));
scan(1..3,ii->(
    val=lift(sub(drop2(fs#ii),{kdrop=>kv2,adrop=>aval2}),sf);
    print("D0 f"|toString(ii+2)|" after f2 solve="|toString factor val);
    save("D0-f"|toString(ii+2),val)));
print "COMPLETE coefficient-drop analysis";
