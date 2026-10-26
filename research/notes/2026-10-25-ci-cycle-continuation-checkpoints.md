# Complete-intersection cycle exploration: continuation checkpoints

Date: 2026-10-25, America/New_York. This is a working handoff, not theorem authority.

## Authorized continuation

The user asked to continue the exploration, then proceed through substantive STCI or other repository items until the five-hour usage limit stops the run. The user also authorized pushing commits at each checkpoint. Publication authorization applies to checkpoint commits; no merge or canonical promotion is inferred.

The active branch is codex/ci-cycle-valuations-2026-10-25, based on commit 59c703c71c1fbac97fc1dc0ddbabadd9ff583a6f. That earlier checkpoint, containing the original cycle notebook and adaptive valuation framework, was already present on the remote branch codex/quartic-flag-duality-2026-10-24 when continuation resumed.

## Checkpoint 1: adaptive valuations and the arithmetic root-collision tree

The [adaptive notebook](2026-10-25-ci-cycle-adaptive-valuative-notebook.md) now states the clarified all-pairs residual-cycle goal and permits the measuring data to depend on the pair. Its reviewed local bridges are:

- Generic transverse colength equals Hilbert–Samuel multiplicity for the actual two-generator parameter ideal, so sufficiently complete adaptive valuation data recover the coefficient of \(C\).
- Residual existence is equivalent to a pointwise multiplicity jump somewhere on \(C\), using complete-intersection connectedness.
- Normalized residual-branch valuations define a contact divisor, with point-multiplicity excess below it and a cubic degree bound above it.
- This contact divisor is distinct from the conductor boundary in nonplanar germs.

The [root-collision notebook](2026-10-25-ci-cycle-root-collision-valuations.md) is the completed concrete continuation. It gives thresholds \(3v(2)/2\) and \(5v(2)/2\), residue-sensitive refinement at the second threshold, and the cross-ratio/elliptic valuation consistency check. The stdlib script and JSON record fifty finite checks. The primary independently reconstructed these calculations; a separate additional audit of this later experiment is not claimed.

The earlier [valuative audit](2026-10-25-ci-cycle-valuative-audit.md) was preserved and its mathematical formatting cleaned. Accepted results and their proofs were not changed or rerun. No universal residual positivity has been proved.

## Next item: an explicit global smooth residual benchmark

Checkpoint 1 was pushed as a4420cb5d01ca27f09f4e07c0ee8289b8cb14c48. The exact remote branch ref was verified and the checkout was clean immediately after the push.

## Checkpoint 2: exact global smooth residual benchmark

The generic existence argument in the [deformation laboratory](2026-10-25-ci-cycle-deformation-laboratory.md) is now accompanied by a [fully explicit rational pair](2026-10-25-ci-cycle-smooth-residual-example.md) and [independent audit](2026-10-25-ci-cycle-smooth-residual-audit.md). The actual saturated colon ideal has degree twelve and arithmetic genus sixteen. Exact rational Jacobian calculations show it is smooth; its space of global functions is \(\mathbf Q\), so base change gives geometric connectedness and hence geometric integrality. Its attachment scheme has eighteen geometric reduced points and avoids both distinguished endpoints.

The independent standard-library boundary calculation gives a squarefree polynomial of degree eighteen with constant coefficient four and leading coefficient three. The Macaulay2 and Python scripts, JSON, and captured rational output are retained. No finite-field lifting argument is needed.

A preliminary coefficient choice forced the line \(L=V(x_0+x_1,x_2+x_3)\). Its residual has five singular points on that line. This is the next intrinsic geometry item: isolate the degree-eleven component, check its genus and smoothness, and understand the genus redistribution when the line is absorbed in a nearby smooth residual.

The separate [frontier reconnaissance](2026-10-25-valuative-frontier-next-experiments.md) identifies two genuinely open STCI followups after that geometry checkpoint: the single-defect nonsaturated degree-\((6,12)\) slice, and an endpoint-four nodal chart of the conditional degree-\((6,16)\) lane. Their exact hypotheses and unresolved global-realization requirements remain explicit. Do not reopen accepted exclusions or treat these candidate experiments as existence/nonexistence results.
