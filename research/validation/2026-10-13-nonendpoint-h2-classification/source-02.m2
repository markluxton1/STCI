-- Actual corrected conormal-cubic homogeneous gcd classification.
-- Work in characteristic zero with sepD nonzero.
R=QQ[sepD,vv,ww];
matH=matrix{{sepD*ww,sepD*vv+3*ww,0,-3*ww},
 {sepD^2*vv,sepD^2-3*ww,0,6*ww},
 {0,0,sepD*ww,sepD*vv+3*ww},
 {-3*sepD^3,-3*ww,sepD^2*vv,sepD^2+6*ww}};
assert(det matH==sepD^4*(vv^2-4*ww)*(sepD^2*vv^2+2*sepD^2*ww+6*sepD*vv*ww+6*ww^2));
print "PASS 1: finite quadratic factor coefficient matrix determinant";
Rn=QQ[del,v,w];
mn=matrix{{w,v+3*w,0,-3*w},{v,1-3*w,0,6*w},{0,0,w,v+3*w},{-3,-3*w,v,1+6*w}};
rhsn=matrix{{2},{del-3},{1-del},{5*del-3}};
assert(det mn==(v^2-4*w)*(v^2+2*w+6*v*w+6*w^2));
print "PASS 2: normalized finite quadratic determinant";
aug=mn|rhsn;
for k from 0 to 3 do (
 cols=select(toList(0..4),j->j!=k);
 print (k,factor substitute(det submatrix(aug,{0,1,2,3},cols),{w=>v^2/4}));
 );
print "rank matrices at H=z2 and H=(z-1)2:";
print substitute(mn,{v=>0,w=>0});
print substitute(mn,{v=>-2,w=>1});
