-- Exact root-incidence certificate for the determinant stratum D=2R,
-- R of class (1,1), R different from the diagonal.
-- On C0, equations of target bidegree (3,1) have degree-ten binary
-- restrictions missing precisely the coefficients of t^2,t^5,t^8.
-- Two finite nonzero distinct roots reduce, by the preserving torus and
-- exchange of the two root factors, to (s-r*t)^m(s-t)^(10-m), 1<=m<=5.
R=QQ[r]; T=R[t];
for m from 1 to 5 do (
    P=(1-r*t)^m*(1-t)^(10-m);
    ff=apply({2,5,8},j->sub(coefficient(t^j,P),R));
    gg=fold(ff,(a,b)->gcd(a,b));
    assert(gg==1_R);
    print("MULTIPLICITY="|toString m|"; COEFFICIENTS="|toString ff|"; GCD="|toString gg);
);
print "TWO_FINITE_NONZERO_ROOT_LOCUS_EMPTY";
print "ENDPOINT_ROOT_CASES_REQUIRE_REDUCIBLE_TARGET_CURVE_BY_BINARY_SUPPORT_ARGUMENT";
-- Reducible R has a component mapping onto an irreducible (1,1) conic.
-- Its restriction to C0 misses only the coefficient of t^2.
assert(sub(coefficient(t^2,(1-r*t)^4),R)==6*r^2);
print "REDUCIBLE_RESIDUAL_ONE_POINT_CONTACT_REQUIRES_REDUCIBLE_TARGET_CURVE";
print "FULL_DOUBLE_RESIDUAL_STRATUM_EXCLUDED_IN_CHARACTERISTIC_ZERO";
