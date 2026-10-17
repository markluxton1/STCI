-- Independent Jacobian proof for the fixed monomial smooth rational quartic.
-- This reinforces RESEARCH_RECORD P-009, rather than claiming a new splitting.
R = QQ[s,t];
forms = matrix{{s^4,s^3*t,s*t^3,t^4}};
J = matrix{{4*s^3,3*s^2*t,t^3,0},{0,s^3,3*s*t^2,4*t^3}};
V = matrix{{-2*t^3,0},{3*s*t^2,t^3},{-s^3,-3*s^2*t},{0,2*s^3}};
checks = 0;
check = (b,label) -> (
    if not b then error concatenate("FAILED: ",label);
    checks = checks+1;
    print concatenate("PASS: ",label)
    );
check(J*V == 0, "both displayed cubic columns are derivative syzygies");
check(saturate(minors(2,J),ideal(s,t)) == ideal(1_R),
      "derivative matrix has rank two everywhere on P1");
check(saturate(minors(2,V),ideal(s,t)) == ideal(1_R),
      "cubic syzygy columns are independent everywhere on P1");
check((minors(2,V)) == ideal(t^6,s^2*t^4,s^3*t^3,s^4*t^2,s^6),
      "complete wedge-minor ideal is the explicitly predicted ideal");

-- Columns a0,a1,a2,b0,b1,b2,c0,c1,c2,d0,d1,d2;
-- rows are s^5,s^4t,s^3t^2,s^2t^3,st^4,t^5 in each derivative equation.
Q = matrix(QQ,{
 {4,0,0,0,0,0,0,0,0,0,0,0},
 {0,4,0,3,0,0,0,0,0,0,0,0},
 {0,0,4,0,3,0,0,0,0,0,0,0},
 {0,0,0,0,0,3,1,0,0,0,0,0},
 {0,0,0,0,0,0,0,1,0,0,0,0},
 {0,0,0,0,0,0,0,0,1,0,0,0},
 {0,0,0,1,0,0,0,0,0,0,0,0},
 {0,0,0,0,1,0,0,0,0,0,0,0},
 {0,0,0,0,0,1,3,0,0,0,0,0},
 {0,0,0,0,0,0,0,3,0,4,0,0},
 {0,0,0,0,0,0,0,0,3,0,4,0},
 {0,0,0,0,0,0,0,0,0,0,0,4}});
check(rank Q == 12, "all quadratic derivative syzygies vanish");
check(abs(det Q) == 2^15, "quadratic syzygy coefficient determinant has absolute value 2^15");
check(rank V == 2, "explicit conormal presentation has generic rank two");
check(rank J == 2, "derivative presentation has generic rank two");
print concatenate("ALL ",toString checks," EXACT CHECKS PASSED");
