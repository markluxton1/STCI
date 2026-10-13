-- Actual corrected conormal-cubic homogeneous gcd classification.
-- Work in characteristic zero with sepD nonzero.
R=QQ[sepD,vv,ww];
matH=matrix{{sepD*ww,sepD*vv+3*ww,0,-3*ww},
 {sepD^2*vv,sepD^2-3*ww,0,6*ww},
 {0,0,sepD*ww,sepD*vv+3*ww},
 {-3*sepD^3,-3*ww,sepD^2*vv,sepD^2+6*ww}};
print factor det matH;
print factor det submatrix(matH,{0,1,3},{0,1,3});
