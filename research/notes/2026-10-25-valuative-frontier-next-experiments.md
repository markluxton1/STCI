# Two focused frontier experiments after the valuative continuation

Date: 2026-10-25. Reconnaissance for choosing the next experiment; no canonical promotion.

Retrieval followed [INDEX](../INDEX.md), the relevant portions of [FRONTIER](../FRONTIER.md) and [STATE](../STATE.md), then the records and evidence below. The older intrinsic-geometry pause is a research preference, not mathematical closure; the present continuation is explicitly authorized to consider open STCI items. No quartic-carrier case is reopened.

The new [valuative multiplicity note](2026-10-25-ci-cycle-valuative-multiplicity.md) supplies an exploratory bridge: for an actual proper pair, the generic transverse ideal is a parameter ideal, so its multiplicity is determined by its complete adapted valuation data. The experiments here concern the extra global twisting and actual-generator restrictions that this local computation does not supply.

## Candidate A: a single nonsaturated first-relation defect in degree (6,12)

**Focused question.** Can an actual homogeneous pair of degrees \((6,12)\), with sole reduced support the fixed characteristic-zero quartic, have full generic ordinary initial CI \((2,9)\), with a first-relation saturation defect of length one and saturated movement one?

This is a deliberately narrow slice of the open nonsaturated-first-relation frontier. It does not claim to be the first possible pair in a global ordering, or to exhaust nonsaturated cases.

**Current authority.** [STCI-R-0016](../results/nonsaturated_first_relation_resultant.md) is promoted and proves a defect/resultant budget under actual lci, sole smooth support, and a full generic binary-CI initial algebra. It does not exclude nonsaturated first relations. [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) assumes saturation, and [STCI-R-0013](../results/saturated_actual_generator_movement.md) excludes movement one only in that saturated class. Consequently R0013 cannot dispose of the proposed slice. The general non-CI-initial-ideal cases remain separate; this candidate still assumes a full generic CI.

The exact identities used next are in the accepted evidence for R0016, [first-relation defect investigation](2026-10-19-first-relation-defect-investigation.md), sections 3–5. Its historical provisional label does not independently promote its contents, but R0016 explicitly links the proof and its independent audits. The new numerical application below is provisional.

Let \(R_{\mathrm{sat}}=\mathcal O(-14-\epsilon)\), let \(D\) have length \(\delta\), and use the evidence notation \(c_j\) for saturated generation defects. The socle line of an actual degree-\((a,b)\) CI has degree \(\ell=14-4(a+b)\). With \((a,b;r,s)=(6,12;2,9)\), its degree identity gives

\[
2(-58)=2(8)(-14)-7(-14-\epsilon)+c_8,
\qquad c_8=10-7\epsilon.
\]

Effectivity and \(\epsilon\ge0\) leave \((\epsilon,c_8)=(0,10)\) or \((1,3)\). In the second case the resultant equation gives

\[
\deg\Delta=c_8-2c_9=3-2c_9,
\qquad c_9=0\text{ or }1.
\]

Thus its resultant degree is three or one. For \(\delta=1\), the general bound \(c_8\le\binom72\delta\) does not contradict either value. These are necessary arithmetic possibilities, not existence evidence.

**One fresh experiment.** Use the actual sextic second-symbol image, already computed with rank 22 and kernel \(kq^3\) in the independently reviewed [sextic symbol map](2026-10-20-conditional-2-12-symbol-map.md). Its symbol calculation is reusable independently of the saturated \((2,12)\) application advertised in that note.

Parameterize a full movement-one quadratic root

\[
f=(A_0+A_1z)U^2+(B_0+B_1z)UV+(C_0+C_1z)V^2,
\]

with homogeneous endpoint charts retained, and a point \(p\) supporting \(D\). Impose that the second symbols of actual global \(F_6,G_{12}\) are multiples of \(f\), with common multiplier divisor exactly \(p\), so that their actual first kernel is \(R_{\mathrm{sat}}(-p)\). The raw multiplier degrees are nine and 33; after removing their common linear factor, the degrees are eight and 32 and the remaining two sections must have no common zero.

Next divide the truncated normal expansion of \(G_{12}\) by the actual \(F_6\) over \(k(C)\), retaining all global coefficients as constants in \(k\). Force the remainder through normal degree eight to vanish and test that its degree-nine term is coprime to \(f\). For each supplied sextic this is a finite linear test on the actual degree-twelve source. The unknown sextic/root parameters make the total incidence nonlinear, but finite.

The generic cluster energy would then be \(2\cdot9=18\), spending all degree \(72\) on \(C\). A proper global solution would therefore be highly consequential and needs independent audit; there is no asserted solution. A useful negative result could show that every solution factors through \(F_6\), violates the one-point defect condition, or has a forced extra initial relation. Failure to solve the incidence proves nothing.

The simplest local warning remains the accepted source family \((txy+x^3+y^4,xy^2)\): it is finite-flat with constant length ten while the first relation degenerates. Its generic complete-ideal cluster has energy \(4+3+3\), whereas the special cluster has energy \(9+1\). This elementary new cluster reading illustrates that constant energy permits substantial redistribution. The local \((2,5)\) model is a benchmark, not a surviving global degree row.

## Candidate B: the retained endpoint-four nodal chart in degree (6,16)

**Focused question.** Does the endpoint-root normal form \(\tau=z^4\), in the conditional \((r,s;a,b;\epsilon)=(2,12;6,16;2)\) lane, admit the next actual global homogeneous lifts at any of its retained nodal torsion parameters?

**Current authority.** [STCI-R-0014](../results/movement_two_six_rows.md) gives six necessary rows in the saturated/full generic binary-CI class, including this row. It is a promoted arithmetic reduction, not a construction or emptiness theorem. [STCI-R-0018](../results/regular_singular_root_formal_obstruction.md) excludes all-orders lifts whose entire formal surface is regular along the reduced movement-two root; singular formal surfaces remain outside its conclusion.

The [October 21 conductor/chart independent review](2026-10-21-conditional-2-12-conductor-and-chart-independent-review.md), sections 5–6, gives reviewed but **unpromoted** endpoint reductions. It leaves the normal forms \(\tau=z^3(1+z)\) and \(\tau=z^4\), plus a distinct nonzero-endpoint orbit-collision chart. On the fourth-order chart a retained root is integral nodal and its actual Picard gluing modulus satisfies

\[
\rho^{12}=1,\qquad \rho\ne1.
\]

This is a necessary torsion equation, not an exclusion of its intersection with higher ambient lifts. The review explicitly says repeated multiplier zeros and multiplier zeros at root nodes remain unresolved. The failed file [conditional certificate audit metadata](../computations/conditional_2_12_certificate_audit_cont2_2026_10_21.json) records return code one and an assertion failure at line 23 of its companion M2 input. No conclusion here relies on it.

**One fresh experiment.** Normalize projective root scale by \(a_0=1\) and use the reviewed root coefficients

\[
a=1+2b_2z+z^2,\qquad
b=\tfrac{\rho+1}{2}z+b_2z^2,\qquad
c=\tfrac\rho4z^2,
\qquad f=aU^2+bUV+cV^2.
\]

Treat every nontrivial twelfth root \(\rho\) over its exact cyclotomic field; retain the nodal and finite-ruling opens. Determine actual sextics with second symbol \(z^8f\), using the saved rank-22 image and the one-dimensional \(q^3\) lift freedom. Then impose that the remainder of an actual global \(G_{16}\), after division by that sextic, vanishes through normal degree eleven and has a coprime degree-twelve term.

This gives a fresh exact matrix/incidence problem on \(b_2\), the \(q^3\) lift parameter, and actual degree-sixteen coefficients. Retain the saturated actual-generator condition: the second-symbol multiplier of \(G_{16}\) must be nonzero at the endpoint where the sextic multiplier \(z^8\) vanishes, and the pair of multipliers must generate the actual first-relation line everywhere. The endpoint specialization may shrink the incidence substantially. Track the adapted valuation cluster along both node branches, but retain their conductor identification: normalization alone loses the modulus \(\rho\). Do not assume a regular formal surface, which would simply place the problem back in the already excluded R0018 class.

The source defines \(\tau\) and its multiplier up to a nonzero scalar; any normalization must be propagated through the actual symbol equation rather than silently reusing incompatible coordinates. A completed unit ideal or an independently checked obstruction on this exact open would close a genuine small chart. It would leave the other endpoint and collision charts, the other movement rows, and unrestricted STCI untouched.

## Recommendation

Candidate A is the more direct test of whether adaptive cluster geometry can interact with **global first-relation defects** beyond the saturated theory. Candidate B has a smaller, more concrete inherited parameter space and could produce a useful completed chart first. Both require actual homogeneous coefficient spaces and complete local cancellation data; neither can be settled by allowing arbitrary \(k(C)\)-coefficients or by counting exceptional components as downstairs residual curves.
