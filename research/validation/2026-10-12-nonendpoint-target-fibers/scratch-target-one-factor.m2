R=QQ[delta,Bc,Gc,Jc,r];
Pzero=Jc*r^3-delta^2*(delta*r+Bc)*(2*r-delta);
Qzero=Jc*(3*r^2-delta*r)+Gc*delta*(2*r-delta);
print toString factor resultant(Pzero,Qzero,r);
