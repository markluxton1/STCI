load "/Users/markluxton/Projects/STCI/research/computations/conditional_2_12_elimination_2026_10_20.m2";
print("START_CUBIC_GB");
G=gb cubicIdeal;
print("GB_COMPLETE");
print gens G;
print("UNIT="|toString(cubicIdeal==ideal(1_R)));
print("DIM="|toString dim cubicIdeal);
