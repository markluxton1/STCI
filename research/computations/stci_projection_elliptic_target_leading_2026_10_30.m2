load "research/computations/stci_projection_elliptic_target_2026_10_30.m2";
for jj in {12,11,10} do print(jj,sub(coefficient(xx^jj,disc),R));
Jtop=ideal apply({12,11},jj->sub(coefficient(xx^jj,disc),R));
print gens gb Jtop;
