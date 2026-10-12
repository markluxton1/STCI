-- Full actual contact jets on the finite Type1 linear parameter stratum.
jetPolynomialRing=QQ[jetVariable,separation,familyRoot];
eta0=2*familyRoot-1;
paramCubic=eta0*separation+1;
jetRing=jetPolynomialRing/ideal(2*familyRoot^2-2*familyRoot-1,paramCubic);
eta0=2*familyRoot-1;
uu=familyRoot*separation^2;
ww=(uu+4*separation^2)/3;
aa=(uu+ww+separation-separation^2)/2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=separation/2;
resJ=(3*uu+ww)*separation-3*separation^3;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
resN=aa*separation^4;
sigmaN=separation;
sigmaL=2_jetRing;
assert(ideal(separation)==ideal(1_jetRing));
assert(ideal(sigmaL)==ideal(1_jetRing));
assert(ideal(resJ)==ideal(1_jetRing));
nr=sigmaN+jetVariable*sigmaL; denr=sigmaL;
tnum=((resJ+3*separation^2)*nr^2
 -(resP2-3*separation^2*rho)*nr*denr+2*aa*separation^3*denr^2);
z0=(resJ^2*nr^4-resJ*(2*nr^2+nr*denr)*tnum+tnum^2+aa*resJ*tnum*denr^2);
u3=(resJ^2*nr^3*denr-resJ*nr*tnum*denr);
z1=z0-separation*u3+(bb-aa)*resJ*tnum*denr^2;
z2=(z0-3*separation*u3+3*separation^2*resJ^2*nr^2*denr^2
 -separation^3*resJ^2*nr*denr^3+(gg-aa)*resJ*tnum*denr^2);
z3=(z0-4*separation*u3+6*separation^2*resJ^2*nr^2*denr^2
 -4*separation^3*resJ^2*nr*denr^3+separation^4*resJ^2*denr^4
 +(parD-aa)*resJ*tnum*denr^2);
assert(z0*z3-z1*z2==0);
assert(substitute(tnum,{jetVariable=>0})==0);
assert(ideal(substitute(z0,{jetVariable=>0}))==ideal(1_jetRing));
actualC=z0^2*z2-z1^3;
jet0=substitute(actualC,{jetVariable=>0});
jet1=substitute(diff(jetVariable,actualC),{jetVariable=>0});
jet2=substitute(diff(jetVariable,diff(jetVariable,actualC)),{jetVariable=>0})/2;
assert(jet0==0 and jet1==0);
print "TYPE 1 linear stratum actual contact second coefficient";
print jet2;
assert(ideal(jet2)==ideal(1_jetRing));
print "PASS: eight conditions; full actual contact order exactly two on entire linear stratum";
