-- Supporting local identities; finite normalization and conductor logic is proved in the note.
R=QQ[aa,bb,gg,parD,sepD,alp,bet,chi];
dZ=alp*bet-chi^2;
eZ=bet^2-alp*bet*chi+chi^3;
hZ=bet+chi;
x0=1-alp+aa*hZ;
x1=1+(sepD-1)*alp+bb*hZ;
x2=1+(3*sepD-1)*alp+3*sepD^2*chi-sepD^3*dZ+gg*hZ;
x3=1+(4*sepD-1)*alp+6*sepD^2*chi-4*sepD^3*dZ+sepD^4*eZ+parD*hZ;
atOrigin=f->substitute(f,{alp=>0,bet=>0,chi=>0});
assert(apply({x0,x1,x2,x3},atOrigin)=={1,1,1,1});
print "PASS 1: actual A4 image point and target frame";
cotangent=matrix apply({x1-x0,x2-x0,x3-x0},f->apply({alp,bet,chi},v->atOrigin(diff(v,f))));
expected=matrix{{sepD,bb-aa,bb-aa},
 {3*sepD,gg-aa,gg-aa+3*sepD^2},
 {4*sepD,parD-aa,parD-aa+6*sepD^2}};
assert(cotangent==expected);
print "PASS 2: all three target-ratio linear jets at A4";
assert(det cotangent==-3*sepD^3*(parD-2*gg+2*bb-aa));
print "PASS 3: exact A4 cotangent determinant";
print "PASS ALL: 3 exact identities; no conductor scheme or parameter exhaustion computed";
