R=QQ[delta,a,Bc,Gc,r];
Qinf=(3*delta^2+Gc)*r^2+(3*delta*Bc-delta^3)*r-delta^2*Bc;
Pinf=-delta^2*r^2+(Bc^2-delta*Bc+a*delta^2)*r+a*delta*Bc;
print toString factor resultant(Pinf,Qinf,r);
