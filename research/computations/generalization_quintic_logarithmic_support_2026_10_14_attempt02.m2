-- New logarithmic support condition. Accepted actual octic and h2 cover are inputs.
outdir="research/validation/2026-10-14-quintic-logarithmic-support/attempt-02";
save=(label,f)->((outdir|"/"|label|".txt") << toString f << close);
base=QQ[delta,a,B,G,J,p];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
par=QQ[deltaPar,vPar,wPar]; KF=frac par; calc=KF[zPar];
dv=sub(deltaPar,KF); vv=sub(vPar,KF); wv=sub(wPar,KF);
M=matrix{{wv,vv+3*wv,0_KF,-3*wv},{vv,1-3*wv,0_KF,6*wv},{0_KF,0_KF,wv,vv+3*wv},{-3_KF,-3*wv,vv,1+6*wv}};
rhs=matrix{{2*dv},{dv^2-3*dv},{dv-dv^2},{5*dv^2-3*dv}};
print "CONSTRUCT finite h2 actual coefficient map";
cofs=flatten entries(M^-1*rhs);
aa=-cofs#1*wv/2; bb=-cofs#3*wv; gg=cofs#0+3*bb-2*aa; ddv=(cofs#2+3*gg-bb)/2;
phi=map(calc,base,{dv,aa,bb-aa,gg-3*bb+2*aa,ddv-2*gg+2*bb-aa,1-zPar});
Fh=phi F;
print "CONDUCTOR constructed";
cc=apply(0..8,ii->lift(coefficient(zPar^ii,Fh),KF));
commonDen=lcm apply(cc,c->denominator c);
nums=apply(cc,c->lift(commonDen*c,par));
coeffContent=gcd nums;
fn=apply(nums,c->c//coeffContent);
print("coefficient denominator degree "|toString degree commonDen);
print("common coefficient coeffContent "|toString factor coeffContent);
scan(0..8,ii->save("F-coefficient-"|toString ii,fn#ii));
save("common-denominator",commonDen);save("common-coeffContent",coeffContent);
R=par[zPar];
Fr=sum(0..8,ii->sub(fn#ii,R)*zPar^ii);
Hr=zPar^2+vPar*zPar+wPar;
-- Homogeneous Hamiltonian action: all coefficients retained, no leading inversion.
eigenImage=8*(vPar+2*zPar)*Fr-2*Hr*diff(zPar,Fr);
assert(degree(zPar,eigenImage)<=8);
eigenCoefficients=apply(0..8,ii->lift(coefficient(zPar^ii,eigenImage),par));
save("support-eigenvector-matrix",transpose matrix{fn,eigenCoefficients});
save("support-eigenvector-image",matrix{eigenCoefficients});
-- The nonzero F locus and commonDen!=0 are mandatory; this is only coefficient capture.
print("homogeneous eigenvector incidence captured; degrees "|toString apply(eigenCoefficients,degree));
print "COMPLETE new h2 shared logarithmic incidence capture";
exit 0;
