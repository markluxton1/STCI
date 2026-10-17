-- Actual target C-contact jets on the complete Type2 and Type3 incidence.
-- Every finite incidence and denominator stratum remains in the quotient.
type2Polynomial=QQ[jetVariable,curveR,separation,familyRoot];
type2Family=ideal(6*familyRoot^2-6*familyRoot+1);
type2Ring=type2Polynomial/type2Family;
tau=1/2; uu=familyRoot*separation^2; ww=3*uu;
aa=2*uu+(separation-separation^2)/2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
quarticTnum=((resJ+3*separation^2)*curveR^2
 -(resP2-3*separation^2*rho)*curveR+(aa/tau)*separation^3);
normalP=((gg-3*bb+2*aa)*curveR^3
 +(6*separation*(bb-aa)+separation^3-3*separation^2)*curveR^2
 +(separation^2*(6*aa-3*bb)+2*separation^3)*curveR-2*aa*separation^3);
normalJ=((2*parD-3*gg+bb)*curveR^3
 +(3*separation*(gg-bb)+5*separation^3-3*separation^2)*curveR^2
 +(3*bb*separation^2+separation^3-separation^4)*curveR-bb*separation^3);
contactIdeal=saturate(ideal(normalP,normalJ,quarticTnum),ideal separation);
jetRelations=type2Family+lift(contactIdeal,type2Polynomial);
jetRing=type2Polynomial/jetRelations;
tau=1/2; uu=familyRoot*separation^2; ww=3*uu;
aa=2*uu+(separation-separation^2)/2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
assert(ideal(separation)==ideal(1_jetRing));
assert(ideal(curveR)==ideal(1_jetRing));
assert(ideal(resJ)==ideal(1_jetRing));
nr=curveR+jetVariable;
tnum=((resJ+3*separation^2)*nr^2
 -(resP2-3*separation^2*rho)*nr+(aa/tau)*separation^3);
z0=(resJ^2*nr^4-resJ*(2*nr^2+nr)*tnum+tnum^2+aa*resJ*tnum);
u3=(resJ^2*nr^3-resJ*nr*tnum);
z1=z0-separation*u3+(bb-aa)*resJ*tnum;
z2=(z0-3*separation*u3+3*separation^2*resJ^2*nr^2
 -separation^3*resJ^2*nr+(gg-aa)*resJ*tnum);
z3=(z0-4*separation*u3+6*separation^2*resJ^2*nr^2
 -4*separation^3*resJ^2*nr+separation^4*resJ^2+(parD-aa)*resJ*tnum);
assert(z0*z3-z1*z2==0);
assert(substitute(tnum,{jetVariable=>0})==0);
assert(ideal(substitute(z0,{jetVariable=>0}))==ideal(1_jetRing));
actualC=z0^2*z2-z1^3;
jet0=substitute(actualC,{jetVariable=>0});
jet1=substitute(diff(jetVariable,actualC),{jetVariable=>0});
jet2=substitute(diff(jetVariable,diff(jetVariable,actualC)),{jetVariable=>0})/2;
jet3=substitute(diff(jetVariable,diff(jetVariable,diff(jetVariable,actualC))),{jetVariable=>0})/6;
assert(jet0==0 and jet1==0);
print "TYPE2 complete-incidence jet2 is unit"; print(ideal(jet2)==ideal(1_jetRing));
print "TYPE2 complete-incidence joint jet2/jet3 ideal"; print gens gb ideal(jet2,jet3);
assert(ideal(jet2,jet3)==ideal(1_jetRing));
print "PASS: Type2 actual target contact is between two and three on complete incidence";

type3Polynomial=QQ[jetVariable,curveR,separation,familyRoot,conicRoot];
type3Family=ideal(6*conicRoot^2-6*conicRoot+1,
 3*familyRoot^2-6*conicRoot*familyRoot-1+3*conicRoot);
type3Ring=type3Polynomial/type3Family;
tau=conicRoot; tauInverse=6*(1-tau);
uu=familyRoot*separation^2; ww=3*uu;
aa=(6*tau-1)*uu+tau*separation-(3*tau-2/3)*separation^2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
quarticTnum=((resJ+3*separation^2)*curveR^2
 -(resP2-3*separation^2*rho)*curveR+aa*tauInverse*separation^3);
normalP=((gg-3*bb+2*aa)*curveR^3
 +(6*separation*(bb-aa)+separation^3-3*separation^2)*curveR^2
 +(separation^2*(6*aa-3*bb)+2*separation^3)*curveR-2*aa*separation^3);
normalJ=((2*parD-3*gg+bb)*curveR^3
 +(3*separation*(gg-bb)+5*separation^3-3*separation^2)*curveR^2
 +(3*bb*separation^2+separation^3-separation^4)*curveR-bb*separation^3);
contactIdeal=saturate(ideal(normalP,normalJ,quarticTnum),ideal separation);
jetRelations=type3Family+lift(contactIdeal,type3Polynomial);
jetRing=type3Polynomial/jetRelations;
tau=conicRoot; tauInverse=6*(1-tau);
uu=familyRoot*separation^2; ww=3*uu;
aa=(6*tau-1)*uu+tau*separation-(3*tau-2/3)*separation^2;
bb=aa-uu; gg=aa-ww; parD=aa-uu-ww;
rho=tau*separation;
resJ=(3*uu+ww)*separation-3*separation^3;
resP2=-uu*ww+(3*aa+3*uu)*separation^2+3*separation^3;
assert(ideal(separation)==ideal(1_jetRing));
assert(ideal(curveR)==ideal(1_jetRing));
assert(ideal(resJ)==ideal(1_jetRing));
nr=curveR+jetVariable;
tnum=((resJ+3*separation^2)*nr^2
 -(resP2-3*separation^2*rho)*nr+aa*tauInverse*separation^3);
z0=(resJ^2*nr^4-resJ*(2*nr^2+nr)*tnum+tnum^2+aa*resJ*tnum);
u3=(resJ^2*nr^3-resJ*nr*tnum);
z1=z0-separation*u3+(bb-aa)*resJ*tnum;
z2=(z0-3*separation*u3+3*separation^2*resJ^2*nr^2
 -separation^3*resJ^2*nr+(gg-aa)*resJ*tnum);
z3=(z0-4*separation*u3+6*separation^2*resJ^2*nr^2
 -4*separation^3*resJ^2*nr+separation^4*resJ^2+(parD-aa)*resJ*tnum);
assert(z0*z3-z1*z2==0);
assert(substitute(tnum,{jetVariable=>0})==0);
assert(ideal(substitute(z0,{jetVariable=>0}))==ideal(1_jetRing));
actualC=z0^2*z2-z1^3;
jet0=substitute(actualC,{jetVariable=>0});
jet1=substitute(diff(jetVariable,actualC),{jetVariable=>0});
jet2=substitute(diff(jetVariable,diff(jetVariable,actualC)),{jetVariable=>0})/2;
jet3=substitute(diff(jetVariable,diff(jetVariable,diff(jetVariable,actualC))),{jetVariable=>0})/6;
assert(jet0==0 and jet1==0);
print "TYPE3 complete-incidence jet2 is unit"; print(ideal(jet2)==ideal(1_jetRing));
print "TYPE3 complete-incidence joint jet2/jet3 ideal"; print gens gb ideal(jet2,jet3);
assert(ideal(jet2,jet3)==ideal(1_jetRing));
print "PASS: Type3 actual target contact is between two and three on complete incidence";
