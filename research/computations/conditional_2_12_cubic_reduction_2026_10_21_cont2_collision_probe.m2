load "research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_collision.m2";
print "COLLISION_GB_START";
B=gb collisionIdeal;
print "COLLISION_GB_DONE";
print(1_R % B == 0);
print dim collisionIdeal;
print gens B;
