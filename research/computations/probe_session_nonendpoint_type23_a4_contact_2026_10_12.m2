-- Actual A4 quartic contact, including the degree-drop stratum.
type2Polynomial=QQ[jetVariable,separation,familyRoot];
type2Ring=type2Polynomial/ideal(6*familyRoot^2-6*familyRoot+1);
tau=1/2; uu=familyRoot*separation^2; ww=3*uu;
aa=2*uu+(separation-separation^2)/2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
middleNumerator=-(resP2-3*separation^2*rho);
constantNumerator=(aa/tau)*separation^3;
qK=3*separation^2;
tnum=qK+middleNumerator*jetVariable+constantNumerator*jetVariable^2;
Tnum=tnum+resJ;
z0=(resJ^2-resJ*(2+jetVariable)*Tnum+Tnum^2+aa*resJ*Tnum*jetVariable^2);
u3=(resJ^2*jetVariable-resJ*Tnum*jetVariable);
z1=z0-separation*u3+(bb-aa)*resJ*Tnum*jetVariable^2;
z2=(z0-3*separation*u3+3*separation^2*resJ^2*jetVariable^2
 -separation^3*resJ^2*jetVariable^3+(gg-aa)*resJ*Tnum*jetVariable^2);
z3=(z0-4*separation*u3+6*separation^2*resJ^2*jetVariable^2
 -4*separation^3*resJ^2*jetVariable^3+separation^4*resJ^2*jetVariable^4
 +(parD-aa)*resJ*Tnum*jetVariable^2);
assert(z0*z3-z1*z2==0);
assert(substitute(z0,{jetVariable=>0})==9*separation^4);
actualC=z0^2*z2-z1^3;
jet0=substitute(actualC,{jetVariable=>0});
jet1=substitute(diff(jetVariable,actualC),{jetVariable=>0});
jet2=substitute(diff(jetVariable,diff(jetVariable,actualC)),{jetVariable=>0})/2;
jet3=substitute(diff(jetVariable,diff(jetVariable,diff(jetVariable,actualC))),{jetVariable=>0})/6;
jet4=substitute(diff(jetVariable,diff(jetVariable,diff(jetVariable,diff(jetVariable,actualC)))),{jetVariable=>0})/24;
assert(jet0==0 and jet1==0 and jet2==0);
assert(jet3==54*separation^9*resJ^2*(resJ+3*separation^2));
dropIdeal=saturate(ideal(resJ+3*separation^2),ideal separation);
print "TYPE2 A4 degree-drop relation and possible next coefficient degeneration";
print gens gb dropIdeal;
print gens gb (dropIdeal+ideal middleNumerator);
assert(dropIdeal+ideal middleNumerator==ideal(1_type2Ring));
assert((jet4+2*separation^3*resJ^5*middleNumerator) % dropIdeal ==0);
print "PASS: Type2 A4 target contact 3 when degree T=2; 4 when degree T=1; no degree<=0 T";

type3Polynomial=QQ[jetVariable,separation,familyRoot,conicRoot];
type3Ring=type3Polynomial/ideal(6*conicRoot^2-6*conicRoot+1,
 3*familyRoot^2-6*conicRoot*familyRoot-1+3*conicRoot);
tau=conicRoot; tauInverse=6*(1-tau);
uu=familyRoot*separation^2; ww=3*uu;
aa=(6*tau-1)*uu+tau*separation-(3*tau-2/3)*separation^2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
middleNumerator=-(resP2-3*separation^2*rho);
constantNumerator=aa*tauInverse*separation^3;
qK=3*separation^2;
tnum=qK+middleNumerator*jetVariable+constantNumerator*jetVariable^2;
Tnum=tnum+resJ;
z0=(resJ^2-resJ*(2+jetVariable)*Tnum+Tnum^2+aa*resJ*Tnum*jetVariable^2);
u3=(resJ^2*jetVariable-resJ*Tnum*jetVariable);
z1=z0-separation*u3+(bb-aa)*resJ*Tnum*jetVariable^2;
z2=(z0-3*separation*u3+3*separation^2*resJ^2*jetVariable^2
 -separation^3*resJ^2*jetVariable^3+(gg-aa)*resJ*Tnum*jetVariable^2);
z3=(z0-4*separation*u3+6*separation^2*resJ^2*jetVariable^2
 -4*separation^3*resJ^2*jetVariable^3+separation^4*resJ^2*jetVariable^4
 +(parD-aa)*resJ*Tnum*jetVariable^2);
assert(z0*z3-z1*z2==0);
assert(substitute(z0,{jetVariable=>0})==9*separation^4);
actualC=z0^2*z2-z1^3;
jet0=substitute(actualC,{jetVariable=>0});
jet1=substitute(diff(jetVariable,actualC),{jetVariable=>0});
jet2=substitute(diff(jetVariable,diff(jetVariable,actualC)),{jetVariable=>0})/2;
jet3=substitute(diff(jetVariable,diff(jetVariable,diff(jetVariable,actualC))),{jetVariable=>0})/6;
jet4=substitute(diff(jetVariable,diff(jetVariable,diff(jetVariable,diff(jetVariable,actualC)))),{jetVariable=>0})/24;
assert(jet0==0 and jet1==0 and jet2==0);
assert(jet3==54*separation^9*resJ^2*(resJ+3*separation^2));
dropIdeal=saturate(ideal(resJ+3*separation^2),ideal separation);
print "TYPE3 A4 degree-drop relation and possible next coefficient degeneration";
print gens gb dropIdeal;
print gens gb (dropIdeal+ideal middleNumerator);
assert(dropIdeal+ideal middleNumerator==ideal(1_type3Ring));
assert((jet4+2*separation^3*resJ^5*middleNumerator) % dropIdeal ==0);
print "PASS: Type3 A4 target contact 3 when degree T=2; 4 when degree T=1; no degree<=0 T";
