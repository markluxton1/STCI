-- Complete homogeneous quadratic common-factor cover for the corrected pair.
-- These exact identities do not assert a mate or exhaust conductor descent.
R0=QQ[sepD,aa,bb,gg,parD,rr,zz];
po=(gg-3*bb+2*aa)*rr^3+(6*sepD*(bb-aa)+sepD^3-3*sepD^2)*rr^2
 +(sepD^2*(6*aa-3*bb)+2*sepD^3)*rr-2*aa*sepD^3;
jo=(2*parD-3*gg+bb)*rr^3+(3*sepD*(gg-bb)+5*sepD^3-3*sepD^2)*rr^2
 +(3*bb*sepD^2+sepD^3-sepD^4)*rr-bb*sepD^3;
pn=(gg-3*bb+2*aa)*zz^3+(6*(bb-aa)+sepD^2-3*sepD)*zz^2
 +(6*aa-3*bb+2*sepD)*zz-2*aa;
jn=(2*parD-3*gg+bb)*zz^3+(3*(gg-bb)+5*sepD^2-3*sepD)*zz^2
 +(3*bb+sepD-sepD^2)*zz-bb;
assert(substitute(po,{rr=>sepD*zz})==sepD^3*pn);
print "PASS 1: literal normalized P, with every delta factor retained";
assert(substitute(jo,{rr=>sepD*zz})==sepD^3*jn);
print "PASS 2: literal normalized J, with every delta factor retained";
p0=-2*aa; p1=6*aa-3*bb+2*sepD;
p2=6*(bb-aa)+sepD^2-3*sepD; p3=gg-3*bb+2*aa;
j0=-bb; j1=3*bb+sepD-sepD^2;
j2=3*(gg-bb)+5*sepD^2-3*sepD; j3=2*parD-3*gg+bb;
assert(p1+3*p0-3*j0==2*sepD and p2-3*p0+6*j0==sepD^2-3*sepD
 and j1+3*j0==sepD-sepD^2
 and j2-3*p3-3*p0+6*j0==5*sepD^2-3*sepD);
print "PASS 3: four complete affine coefficient constraints";
assert(substitute(pn,{sepD=>-1,aa=>0,bb=>-2/3,gg=>-2})==0
 and substitute(jn,{sepD=>1,bb=>0,gg=>-2/3,parD=>-1})==0);
print "PASS 4: zero-cubic boundary signs, not part of exact h2";

Rn=QQ[del,v,w,ca,cb,cc,cd,z];
mn=matrix{{w,v+3*w,0,-3*w},{v,1-3*w,0,6*w},{0,0,w,v+3*w},{-3,-3*w,v,1+6*w}};
rhsn=del*matrix{{2},{del-3},{1-del},{5*del-3}};
vec=matrix{{ca},{cb},{cc},{cd}};
hm=z^2+v*z+w;
pairP=(ca*z+cb)*hm; pairJ=(cc*z+cd)*hm;
cons=matrix{{ca*w+cb*v+3*cb*w-3*cd*w},
 {ca*v+cb-3*cb*w+6*cd*w},
 {cc*w+cd*v+3*cd*w},
 {cc*v+cd-3*ca-3*cb*w+6*cd*w}};
assert(mn*vec==cons);
print "PASS 5: exact finite-H coefficient matrix";
quadK=v^2+2*w+6*v*w+6*w^2;
assert(det mn==(v^2-4*w)*quadK);
print "PASS 6: determinant separates repeated H and exceptional conic";
aaRec=-cb*w/2; bbRec=-cd*w; ggRec=ca+3*bbRec-2*aaRec;
ddRec=(cc+3*ggRec-bbRec)/2;
npRec=(ggRec-3*bbRec+2*aaRec)*z^3+(6*(bbRec-aaRec)+del^2-3*del)*z^2
 +(6*aaRec-3*bbRec+2*del)*z-2*aaRec;
njRec=(2*ddRec-3*ggRec+bbRec)*z^3+(3*(ggRec-bbRec)+5*del^2-3*del)*z^2
 +(3*bbRec+del-del^2)*z-bbRec;
rowDef=mn*vec-rhsn;
assert(npRec-pairP==-rowDef_(1,0)*z^2-rowDef_(0,0)*z
 and njRec-pairJ==-rowDef_(3,0)*z^2-rowDef_(2,0)*z);
print "PASS 7: recovering actual a,b,g,d loses no coefficient constraint";
aug=mn|rhsn;
assert(substitute(det submatrix(mn,{0,1,2},{0,1,2}),{w=>v^2/4})
 ==-3*v^4*(v+2)^2/64);
print "PASS 8: repeated-H rank is three away from roots zero and one";
repComp=del*v^2+2*del*v-2*v-2;
assert(substitute(det submatrix(aug,{0,1,2,3},{0,2,3,4}),{w=>v^2/4})
 ==-3*del*v^3*(v+2)*repComp/8);
assert(substitute(quadK,{w=>v^2/4})==3*v^2*(v+2)^2/8);
print "PASS 9: repeated-H compatibility and exceptional-conic intersection";
badZero=substitute(mn,{v=>0,w=>0});
badOne=substitute(mn,{v=>-2,w=>1});
assert(submatrix(badZero,{0},{0,1,2,3})==matrix{{0_Rn,0_Rn,0_Rn,0_Rn}});
assert(submatrix(badOne,{1},{0,1,2,3})==-2*submatrix(badOne,{0},{0,1,2,3})
 and submatrix(badOne,{3},{0,1,2,3})==-3*submatrix(badOne,{0},{0,1,2,3})
 -2*submatrix(badOne,{2},{0,1,2,3}));
print "PASS 10: bad double-root charts have the stated incompatible row relations";

Kp=QQ[delK,tpar]; Fk=frac Kp; denK=tpar^2+6*tpar+6;
toK=map(Fk,Rn,{delK,-2*tpar/denK,-2/denK,0,0,0,0,0});
assert(toK quadK==0);
assert(det submatrix(toK aug,{0,1,2,3},{0,2,3,4})==-24*delK*(tpar+2)/denK^2);
print "PASS 11: the complete exceptional conic has no consistent factor pair";

Ri=QQ[delI,rhoI,ai,bi,zi];
mi=matrix{{-6*rhoI^2+6*rhoI-2,6*rhoI^2-3*rhoI},
 {-6*rhoI^2,6*rhoI^2+3*rhoI-1}};
rhsi=-delI*matrix{{(delI-3)*rhoI^2+2*rhoI},
 {(5*delI-3)*rhoI^2+(1-delI)*rhoI}};
infT=6*rhoI^2-6*rhoI+1;
assert(det mi==2*infT);
print "PASS 12: infinity-plus-finite matrix determinant";
augi=mi|rhsi;
assert(det submatrix(augi,{0,1},{1,2})==-2*rhoI*delI*infT*(2*delI*rhoI+1)
 and det submatrix(augi,{0,1},{0,2})==2*rhoI*delI*infT*(2*delI*rhoI-delI+1));
print "PASS 13: Cramer numerators retain the two exceptional infinity roots";
ai0=delI*rhoI*(2*delI*rhoI+1);
bi0=delI*rhoI*(2*delI*rhoI-delI+1);
assert(mi*matrix{{ai0},{bi0}}==rhsi);
print "PASS 14: exact particular solution in every infinity chart";
assert((mi*matrix{{3*rhoI-1},{1}})%ideal(infT)==0);
assert(mi_(0,0)%ideal(infT)==-1_Ri);
print "PASS 15: exceptional infinity charts have a one-dimensional solution fiber";
pq=(6*(bi-ai)+delI^2-3*delI)*zi^2+(6*ai-3*bi+2*delI)*zi-2*ai;
jq=(6*(bi-ai)+5*delI^2-3*delI)*zi^2+(3*bi+delI-delI^2)*zi-bi;
assert((6*(bi-ai)+5*delI^2-3*delI)-(6*(bi-ai)+delI^2-3*delI)==4*delI^2);
print "PASS 16: a double root at infinity is impossible for nonzero delta";
assert(substitute(pq,{ai=>ai0,bi=>bi0,zi=>rhoI})==0
 and substitute(jq,{ai=>ai0,bi=>bi0,zi=>rhoI})==0);
print "PASS 17: both literal quadratic restrictions vanish at the claimed finite root";
print "PASS ALL: 17 exact structural identities; conductor-support incidence remains necessary only";
