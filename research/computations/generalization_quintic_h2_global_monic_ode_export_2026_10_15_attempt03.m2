-- Postprocess all completed NEW model outputs from attempt02.
-- Its quotient/cofactor assertions passed; only final count printing failed.
-- No actual conductor input is reread and no model construction is rerun.
base=QQ[delta,a,B,G,J,vH2,wH2,h2DGlobal,h2EtaGlobal];
inDir="research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-02-name-repair";
outDir="research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-03-completion";
globalMatrix=value get(inDir|"/global-seventeen-equations.txt");
qMatrix=value get(inDir|"/actual-Q-coefficients.txt");
assert(numRows globalMatrix==1 and numColumns globalMatrix==17);
assert(numRows qMatrix==1 and numColumns qMatrix==7);
assert(numColumns(value get(inDir|"/cover-four-equations.txt"))==4);
assert(numColumns(value get(inDir|"/conductor-two-remainders.txt"))==2);
assert(numColumns(value get(inDir|"/ODE-eight-equations.txt"))==8);
assert(numColumns(value get(inDir|"/derived-three-accelerators.txt"))==3);
(outDir|"/global-seventeen-equations.txt") << toString globalMatrix << close;
(outDir|"/global-domain-unit.txt") << get(inDir|"/global-domain-unit.txt") << close;
print "PASS complete global input shape: four cover, two conductor remainders, eight ODE, three derived equations";
print "COMPLETE GLOBAL denominator-free monic h2 incidence: 17 equations, delta*cofactor*Delta1 unit; no cover determinant inverted";
exit 0;
