load "/Users/markluxton/Projects/STCI/research/computations/conditional_2_12_cont2_endpoint_m4_a0unit_2026_10_21.m2";
print("CUBIC_DEGREE="|toString degree endpointCubicIdeal);
print "T_POLYNOMIAL";
print gens eliminate({q,hh4,hh5,hh10,hh11,eta,iv},endpointCubicIdeal);
tangentIdeal=endpointCubicIdeal+ideal(4*t-1);
print("TANGENT_UNIT="|toString(tangentIdeal==ideal(1_R)));
picardIdeal=endpointCubicIdeal+ideal((4*t)^12-1);
print("PICARD_UNIT="|toString(picardIdeal==ideal(1_R)));
print gens gb picardIdeal;
