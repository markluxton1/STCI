load "/Users/markluxton/Projects/STCI/research/computations/conditional_2_12_elimination_2026_10_20.m2";
G=gb cubicIdeal;
print "CUBIC_GB_COMPLETE";
print("UNIT="|toString(cubicIdeal==ideal(1_R)));
print("DIM="|toString dim cubicIdeal);
print gens G;
