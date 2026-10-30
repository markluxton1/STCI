load "research/computations/stci_projection_elliptic_target_2026_10_30.m2";
rdisc=sub(resultant(quartic,diff(tt,quartic),tt),R);
stdio << "QUARTIC_DISCRIMINANT_COMPUTED" << endl; flush stdio;
J=saturate(I,ideal rdisc);
stdio << "DISTINCT_ROOT_SATURATION_DONE" << endl;
stdio << "SATURATED_INCIDENCE_DIMENSION=" << dim(R/J) << endl;
stdio << "SATURATED_IDEAL=" << gens gb J << endl;
flush stdio;
