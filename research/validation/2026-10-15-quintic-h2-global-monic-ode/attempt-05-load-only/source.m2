-- Runnable/loadable input for the complete GLOBAL remaining monic h2 model.
-- Only saved exact equations are loaded. No construction, GB or saturation.
-- Objects retained for a future calculation:
-- h2GlobalRing, h2GlobalEquations, h2GlobalIdeal, h2GlobalDomainUnit.
h2GlobalRing=QQ[delta,a,B,G,J,vH2,wH2,h2DGlobal,h2EtaGlobal];
h2GlobalData="research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-04-completion";
h2GlobalEquations=value get(h2GlobalData|"/global-seventeen-equations.txt");
h2GlobalDomainUnit=value get(h2GlobalData|"/global-domain-unit.txt");
assert(numgens h2GlobalRing==9);
assert(numRows h2GlobalEquations==1 and numColumns h2GlobalEquations==17);
assert(ring h2GlobalEquations===h2GlobalRing);
assert(h2GlobalDomainUnit!=0_h2GlobalRing);
h2GlobalIdeal=ideal h2GlobalEquations;
print "LOADED exact global h2 input over QQ: 17 equations, 9 variables, delta*cofactor*Delta1 domain";
print "No cover determinant, discriminant, q coefficient, or Jbar is inverted. No GB/saturation executed.";
