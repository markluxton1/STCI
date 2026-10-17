-- Independent first-symbol identities, not a full STCI parameter exhaustion.
R=QQ[aa,bb,gg,parD,sepD,rr];
l0=aa-2*rr^2-rr;
l1=bb-2*rr^2-rr+sepD*rr;
l2=gg-2*rr^2-rr+3*sepD*rr;
l3=parD-2*rr^2-rr+4*sepD*rr;
pv=rr^3*l2-3*rr*(rr-sepD)^2*l1+2*(rr-sepD)^3*l0;
ju=2*rr^3*l3-3*rr^2*(rr-sepD)*l2+(rr-sepD)^3*l1;
pvExpected=((gg-3*bb+2*aa)*rr^3
 +(6*sepD*(bb-aa)+sepD^3-3*sepD^2)*rr^2
 +(sepD^2*(6*aa-3*bb)+2*sepD^3)*rr-2*aa*sepD^3);
juExpected=((2*parD-3*gg+bb)*rr^3
 +(3*sepD*(gg-bb)+5*sepD^3-3*sepD^2)*rr^2
 +(3*bb*sepD^2+sepD^3-sepD^4)*rr-bb*sepD^3);
assert(pv==pvExpected);
print "PASS 1: V first-symbol numerator is the displayed cubic";
assert(ju==juExpected);
print "PASS 2: twice U first-symbol numerator is the displayed cubic";
assert(substitute(pv,{rr=>0})==-2*aa*sepD^3
 and substitute(ju,{rr=>0})==-bb*sepD^3);
print "PASS 3: target-infinity homogeneous common-root condition";
assert(substitute(pv,{aa=>0,bb=>0})==(gg*rr^3+(sepD^3-3*sepD^2)*rr^2+2*sepD^3*rr));
print "PASS 4: both cubics cannot vanish identically at nonzero separation";
assert(substitute(pv,{sepD=>1,aa=>1,bb=>0,gg=>0,parD=>0})==2*(rr^3-4*rr^2+4*rr-1));
assert(substitute(ju,{sepD=>1,aa=>1,bb=>0,gg=>0,parD=>0})==2*rr^2);
assert(substitute(pv,{sepD=>1,aa=>1,bb=>0,gg=>0,parD=>0,rr=>1/2})==1/4);
print "PASS 5: explicit coprime homogeneous-cubic example (no admissibility claim for this point)";
-- Derive the actual target frame transition with rational functions.
S=QQ[zz,nuU,nuV]; K=frac S;
zK=substitute(zz,K); uK=substitute(nuU,K); vK=substitute(nuV,K);
targetX3=zK^4+uK+(3/2)*zK*vK;
oppBase=(zK^3+vK)/targetX3;
oppVraw=zK/targetX3-oppBase^3;
oppUraw=1/targetX3-oppBase^4-(3/2)*oppBase*oppVraw;
zeroNormal=f->substitute(f,{nuU=>0,nuV=>0});
assert(zeroNormal(diff(nuU,oppVraw)/2)==zK^(-7)
 and zeroNormal(diff(nuV,oppVraw)/2)==0);
print "PASS 6: U opposite-frame linear transition";
assert(zeroNormal(2*diff(nuU,oppUraw))==0
 and zeroNormal(2*diff(nuV,oppUraw))==zK^(-7));
print "PASS 7: V opposite-frame linear transition";
print "PASS ALL: 7 exact supporting conditions; no degree-eight locus exhaustion";
