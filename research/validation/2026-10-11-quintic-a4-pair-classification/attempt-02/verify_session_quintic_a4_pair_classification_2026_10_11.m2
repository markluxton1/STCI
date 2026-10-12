-- Exact identities supporting the all-pair geometric contraction proof.
-- This is not an exhaustion of quintic projection/conductor parameters.
R = QQ[x,y,z,aa,bb,gg,hh,ss,tt,bet,bet2,delta];
checks = 0;
assertExact = (b,label) -> (
    if not b then error concatenate("FAILED: ",label);
    checks = checks+1;
    print concatenate("PASS: ",label)
    );
xp = aa*x+bb*y;
yp = aa^3*y;
zp = z+gg*x+hh*y;
assertExact(det matrix{{aa,bb,0},{0,aa^3,0},{gg,hh,1}} == aa^4,
    "cluster stabilizer is invertible for aa nonzero");
assertExact(yp*zp+xp^2 == aa^3*y*z+aa^2*x^2+(aa^3*gg+2*aa*bb)*x*y+(aa^3*hh+bb^2)*y^2,
    "full tangent-conic transformation formula");
jet = sub(yp*zp^2-xp^3,{y=>x^3,z=>1});
assertExact(jet % x^4 == 0,
    "every displayed transformation preserves the complete length-four cluster");
xb = x+bet*y;
yb = y;
zb = z-2*bet*x-bet^2*y;
assertExact(yb*zb+xb^2 == y*z+x^2,
    "residual pair automorphism preserves the standard conic");
assertExact((xb+bet2*yb == x+(bet+bet2)*y) and
 (zb-2*bet2*xb-bet2^2*yb == z-2*(bet+bet2)*x-(bet+bet2)^2*y),
    "residual pair transformations compose by addition");
assertExact(sub(xb,{x=>ss*tt,y=>tt^2,z=>-ss^2}) == (ss+bet*tt)*tt and
 sub(zb,{x=>ss*tt,y=>tt^2,z=>-ss^2}) == -(ss+bet*tt)^2,
    "residual action on the conic parameter is translation");
forms = {y*z^2-x^3,x*y*z,y^2*z,x^2*y,x*y^2,y^3};
restricted = apply(forms,f->sub(f,{x=>ss*tt,y=>tt^2,z=>-ss^2}));
rn = {restricted#5,restricted#4,restricted#3,-restricted#1,restricted#0-restricted#1};
assertExact(rn == apply({tt^4,ss*tt^3,ss^2*tt^2,ss^3*tt,ss^4},f->tt^2*f),
    "the strict conic is the complete smooth rational normal quartic");
assertExact(restricted#2+restricted#3 == 0,
    "the conic spans precisely its anticanonical hyperplane");
assertExact((y*(y*z+x^2))^5 == y^3*(y^2*(y*z+x^2)^5),
    "the distinguished intrinsic quartic section is h^5 divided by y^3");
-- Picard columns use h,e1,e2,e3,e4, with quadratic form (1,-1,-1,-1,-1).
J = diagonalMatrix {1_QQ,-1_QQ,-1_QQ,-1_QQ,-1_QQ};
roots = matrix(QQ,{{0,0,0,1},{1,0,0,-1},{-1,1,0,-1},{0,-1,1,-1},{0,0,-1,0}});
anti = matrix(QQ,{{3},{-1},{-1},{-1},{-1}});
curve = matrix(QQ,{{2},{-1},{-1},{0},{0}});
line = matrix(QQ,{{0},{0},{0},{0},{1}});
assertExact(transpose roots*J*roots == matrix(QQ,{{-2,1,0,0},{1,-2,1,0},{0,1,-2,1},{0,0,1,-2}}),
    "the four retained exceptional primes form the full A4 chain");
assertExact(4*anti-5*curve == roots*matrix(QQ,{{3},{6},{4},{2}}),
    "actual quartic c correction has coefficients three six four two");
assertExact(anti-5*line == roots*matrix(QQ,{{2},{4},{6},{3}}),
    "actual anticanonical line correction has coefficients two four six three");
assertExact(transpose curve*J*curve == matrix{{2_QQ}} and
 transpose curve*J*anti == matrix{{4_QQ}} and
 transpose curve*J*roots == matrix{{0_QQ,1,0,0}},
    "the smooth conic has square two degree four and sole second-root contact");
assertExact(transpose line*J*line == matrix{{-1_QQ}} and
 transpose line*J*anti == matrix{{1_QQ}} and
 transpose line*J*roots == matrix{{0_QQ,0,1,0}},
    "the unique line has square minus one degree one and sole third-root contact");
-- The SL2-equivariant point-to-binary-quartic identification sends RN(r)
-- to (Z-r)^4; the finite-root center representative is therefore exact.
binaryCenter = z^4-6*(delta^2/3)*z^2+delta^4;
assertExact(binaryCenter == (z-delta)^2*(z+delta)^2,
    "nonendpoint centers retain the nonzero root-separation parameter");
print concatenate("ALL ",toString checks," EXACT CHECKS PASSED");
