load "/Users/markluxton/Projects/STCI/research/computations/generalization_quadratic_root_global_second_model.m2";
print("GB_START_QQ_FULL_SMOOTH_FAMILY");
globalBasis=gb globalSecondIdeal;
globalRemainder=1_R % globalBasis;
print("GB_COMPLETE");
print("BASIS_COLUMNS="+toString numColumns gens globalBasis);
print("UNIT_REMAINDER="+toString globalRemainder);
if globalRemainder==0 then print("EXACT_QQ_UNIT_IDEAL") else print("EXACT_QQ_NONUNIT_IDEAL");
