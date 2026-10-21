load "research/computations/conditional_2_12_cubic_reduction_2026_10_21_family.m2";
print "QQ8_GB_START";
B=gb familyIdeal;
print "QQ8_GB_DONE";
print(1_R % B == 0);
