-- ONE genuinely new whole-h2 QQ saturation prospect.
-- Load accepted saved input; no coefficient assembly or verifier replay.
h2GlobalRunOut="research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation";
h2GlobalRunStage=label->((h2GlobalRunOut|"/stage.txt") << label << close);
h2GlobalRunStage("before-load");
load "research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2";
h2GlobalRunStage("after-load-17-equations-9-variables-over-QQ");
assert(numColumns h2GlobalEquations==17 and numgens h2GlobalRing==9);
h2GlobalRunStage("before-global-QQ-saturation-by-delta-E-Delta1-only");
h2GlobalRunSaturated=saturate(h2GlobalIdeal,ideal h2GlobalDomainUnit);
(h2GlobalRunOut|"/saturated-ideal.txt") << toString gens h2GlobalRunSaturated << close;
h2GlobalRunIsUnit=(h2GlobalRunSaturated==ideal(1_h2GlobalRing));
(h2GlobalRunOut|"/is-unit.txt") << toString h2GlobalRunIsUnit << close;
h2GlobalRunStage("saturation-complete");
print "COMPLETE whole-h2 global QQ saturation prospect; consult saved ideal and is-unit output";
print "A unit output is provisional until an exact original-generator certificate is extracted and checked.";
exit 0;
