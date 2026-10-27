# Complete-intersection cycle exploration: continuation checkpoints

Date: 2026-10-25, America/New_York. This is a working handoff, not theorem authority.

**October 26 instruction update:** the user reopened the usage window and asked to finish the investigations already underway, push the work, and stop. This supersedes the earlier instruction to keep selecting new items until the usage limit. The final current items are the line degeneration, fixed-boundary node smoothing, and endpoint-four actual sextic/fixed-carrier jet test.

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

## Publication record

Checkpoint 1 was pushed as a4420cb5d01ca27f09f4e07c0ee8289b8cb14c48. The exact remote branch ref was verified and the checkout was clean immediately after the push.

## Checkpoint 2: exact global smooth residual benchmark

The generic existence argument in the [deformation laboratory](2026-10-25-ci-cycle-deformation-laboratory.md) is now accompanied by a [fully explicit rational pair](2026-10-25-ci-cycle-smooth-residual-example.md) and [independent audit](2026-10-25-ci-cycle-smooth-residual-audit.md). The actual saturated colon ideal has degree twelve and arithmetic genus sixteen. Exact rational Jacobian calculations show it is smooth; its space of global functions is \(\mathbf Q\), so base change gives geometric connectedness and hence geometric integrality. Its attachment scheme has eighteen geometric reduced points and avoids both distinguished endpoints.

The independent standard-library boundary calculation gives a squarefree polynomial of degree eighteen with constant coefficient four and leading coefficient three. The Macaulay2 and Python scripts, JSON, and captured rational output are retained. No finite-field lifting argument is needed.

A preliminary coefficient choice forced the line \(L=V(x_0+x_1,x_2+x_3)\). Its residual has five singular points on that line. This is the next intrinsic geometry item: isolate the degree-eleven component, check its genus and smoothness, and understand the genus redistribution when the line is absorbed in a nearby smooth residual.

The separate [frontier reconnaissance](2026-10-25-valuative-frontier-next-experiments.md) identifies two genuinely open STCI followups after that geometry checkpoint: the single-defect nonsaturated degree-\((6,12)\) slice, and an endpoint-four nodal chart of the conditional degree-\((6,16)\) lane. Their exact hypotheses and unresolved global-realization requirements remain explicit. Do not reopen accepted exclusions or treat these candidate experiments as existence/nonexistence results.

Checkpoint 2 was pushed as d856d78078b75ec78d38c8782b9da3a6f9b1c9ab, with the exact remote ref verified.

## Checkpoint 3: line absorption and independent smoothing at fixed boundary

The [line degeneration](2026-10-25-ci-cycle-line-degeneration.md) and its [audit](2026-10-25-ci-cycle-line-degeneration-audit.md) certify a residual \(L\cup E\), where \(E\) is smooth geometrically integral of degree eleven and genus twelve. There are five simple \(L\)-\(E\) nodes, seventeen \(C\)-\(E\) attachments, and one \(C\)-\(L\) attachment, with no triple points. The moving ruling-line stratum is \(ab=1\) near the chosen parameter. Each node-smoothing parameter is a unit times \(ab-1\); the order-five assertion concerns their product, not every scheme structure called a discriminant.

The [fixed-boundary calculation](2026-10-25-ci-cycle-fixed-boundary-node-smoothing.md), its [independent reconstruction](2026-10-25-ci-cycle-fixed-boundary-node-smoothing-audit.md), and the [October 26 final audit](2026-10-26-ci-cycle-fixed-boundary-node-smoothing-audit.md) give affine ranks \(19,5,24\). On the pencil Grassmannian the exact-boundary fiber has dimension fourteen and maps smoothly to the five marked node parameters, with nine further formal coordinates. The formal/étale local existence statement is reviewed; an explicit polynomial coefficient arc is not claimed.

These two geometric investigations are complete at their stated exploratory scope. Checkpoint 3 was pushed as 15b1806cc174737806fa4b9e2a57f70eab0de374, with the remote ref verified.

## Final checkpoint: actual endpoint-four sextics and a fixed-carrier residual certificate

The [actual-sextic note](2026-10-25-endpoint4-actual-sextics.md) completes the prescribed second-symbol lifting problem on the retained endpoint-four chart, preserving all actual global coefficient constraints and the one-dimensional kernel. It justifies the \(a_0=1\) gauge using the actual \(C\)-preserving torus and its recorded square-root cover. This family construction alone is not a mate-existence or chart-emptiness statement.

For the selected carrier
\[
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3,
\quad q=x_0x_3-x_1x_2,\quad D=x_2^3-x_1x_3^2,
\]
the fixed-carrier M2 certificate and the independent normal-division implementation both pass: the \(690\times969\) matrix has rank \(683\), and all \(286\) actual global multiples \(F_*H_{10}\) are annihilated. The known-multiple guard caught an M2 multiline-assignment error during development; that error was corrected before the final certificates passed. The failure mechanism and final source/output hashes are retained.

The [independent nonsplit-node audit](2026-10-26-endpoint4-nonsplit-node-scope-audit.md) supplies the bridge from that jet kernel to **every proper degree-sixteen mate** on the selected carrier. The two conjugate generic branches have equal vanishing orders \(n\); finite intersection length is \(m_C=2n\), and \(n\ge12\) would force a global multiple of \(F_*\). Thus \(m_C\le22\), and the residual cycle has degree at least eight. This requires no prescribed full initial ideal or saturation hypothesis. It remains a new unpromoted fixed-carrier result, not an exclusion of the entire endpoint-four chart or the unrestricted characteristic-zero problem.

The exact scripts, data, output, geometric bridges, and limitations are saved. All investigations underway at the user's October 26 instruction have now reached their stated endpoints. No additional research item is being started; finish validation and push this final checkpoint, then stop.
