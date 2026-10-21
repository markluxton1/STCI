-- Bounded probe of a closed enlargement of the free-orbit necessary locus.
load "research/computations/conditional_2_12_cubic_reduction_2026_10_21.m2";
qlineClosedEnlargement=ideal join(firstEquations,symbolEquations,qlineSimpleEquations);
print "QQ_QLINE_GB_START";
qlineBasis=gb qlineClosedEnlargement;
print("QQ_QLINE_GB_DONE generators="|toString numgens gens qlineBasis);
print("QQ_QLINE_UNIT="|toString(1_R % qlineBasis == 0));
