-- Exact failed-candidate test for the degree-eight smooth-quadric model.
-- The family is only a candidate source; no birationality is assumed.
-- Run: /opt/homebrew/bin/M2 --script research/computations/stci_search_quadric_endpoint_2026_10_28.m2
R=QQ[lam,u,v];
delta=v-u;
U={1+delta^2,v,u^2*v,u^2*v^2+lam*delta^2};
-- Diagonal restriction is exactly [1:u:u^3:u^4].
assert(apply(U,f->sub(f,{v=>u}))=={1_R,u,u^3,u^4});
-- u^2+1=0, v=0 is a reduced, degree-two subscheme off the diagonal.
J=ideal(v,u^2+1);
assert(U_0%J==0_R and U_1%J==0_R and U_2%J==0_R);
assert((U_3+lam)%J==0_R);
assert((delta^2+1)%J==0_R);
-- Thus lam != 0 maps both geometric points to [0:0:0:1] in C;
-- for lam=0 both points are basepoints instead.
assert(apply(U,f->(sub(f,{lam=>0_R}))%J)=={0_R,0_R,0_R,0_R});
print "DIAGONAL_RESTRICTION_VERIFIED";
print "OFF_DIAGONAL_ENDPOINT_WITNESS_VERIFIED";
print "NONZERO_LAMBDA_EXTRA_INVERSE_POINTS_ZERO_LAMBDA_BASEPOINTS";
