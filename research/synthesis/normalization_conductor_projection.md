# Normalization, conductor descent, and projection of singular carriers

This dossier consolidates the **fixed-carrier** and **Cartier singleton-lift** questions for the rational quartic
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3.
\]
It is an explanatory investigation, **not a new theorem authority**. Exact scopes and proofs remain in the linked canonical records. This first batch directly compares R-0002, R-0003, R-0004, R-0017, R-0034–R-0036 and Q-0001; additional historical sources remain to be integrated.

## 1. Two logically different problems

Fix an integral hypersurface \(X\subset\mathbf P^3\) containing \(C\), its finite normalization \(\nu:S\to X\), and \(H=\nu^*\mathcal O_X(1)\).

**Fixed carrier:** Does there exist a homogeneous form \(G\) whose restriction to \(X\) has zero support precisely \(C\)? This is a problem of descending an upstairs section through the *actual conductor*, not merely finding a divisor class on \(S\).

**Varying carrier:** Which normalizations \((S,H)\), inverse curves, and four-dimensional linear systems can actually produce such an \(X\)? Classification of numerical models is only necessary; it does not construct a projection, establish full inverse support, or solve conductor descent.

The distinction is decisive: a formally possible \(bH\sim\sum n_i\Gamma_i\) need not arise from a section of \(\mathcal O_X(b)\).

## 2. Full inverse support and the fixed-carrier criterion (R-0003)

Let \(X\) be integral Cohen–Macaulay projective, \(L\) ample, \(S\) its finite normalization, \(H=\nu^*L\), and \(W=(\nu^{-1}C)_{\mathrm{red}}\). An isolated inverse-image point outside the curve components of \(W\) already prevents a section with zero support exactly \(C\): its pullback would have a zero at an isolated point, whereas a nonzero Cartier section on the normal surface has pure codimension-one zero support.

Assume instead \(W=\Gamma_1\cup\cdots\cup\Gamma_s\), with no such isolated points. The candidate divisor classes form
\[
\Lambda=\ker\bigl[\mathbf Z^{s+1}\longrightarrow\mathrm{Cl}(S)\bigr],
\quad
(n_1,\ldots,n_s,b)\mapsto\sum n_i[\Gamma_i]-b[H].
\]
A lattice point determines a rational upstairs section with prescribed divisor. At each generic conductor curve away from \(C\), descent is controlled by the **full unit quotient** \(B_\eta^*/A_\eta^*\), not merely its reduced residue-field quotient. Write \(\Lambda_{\mathrm{desc}}\) for the kernel of the conductor-unit map after quotienting its target by torsion.

**Established fixed-carrier criterion (R-0003).** A positive power of \(L\) has a section with zero support exactly \(C\) if and only if \(\Lambda_{\mathrm{desc}}\) contains a vector with every \(n_i>0\). For a hypersurface of \(\mathbf P^3\), such sections lift to homogeneous forms.

**Why sufficiency is nontrivial.** The lattice relation constructs the upstairs divisor; torsion of off-\(C\) conductor classes allows a common power to descend there. Positivity along every inverse branch allows a further power to enter the actual conductor along \(C\). The normality/depth hypotheses are then used to pass from generic conductor control to global descent. Omitting either the nilpotent conductor units or the full inverse support breaks this argument.

In the singleton, generically regular case set \(a=H^2\), \(c=H\cdot\Gamma\), \(g=\gcd(a,c)\). If \(t\) is the order of \((a/g)[\Gamma]-(c/g)[H]\) and \(E\) the full conductor-unit order of the primitive upstairs section, a mate exists exactly when both orders are finite; its degrees are positive multiples of \(tEc/g\). This formula is **not** available without the singleton and generic-regularity hypotheses.

[Canonical R-0003](../results/fixed_carrier_conductor_criterion.md) · [source proof](../notes/2026-10-13-generalization-conductor-theorem.md)

## 3. Cartier singleton classification: necessity, not existence (R-0002)

Suppose characteristic zero, \(C\subset\mathbf P^3\) is smooth rational of degree \(d\), an **actual** STCI mate exists on integral \(X\) of degree \(a\), and the full reduced inverse support is a single smooth curve \(c\) mapping isomorphically to \(C\). Require \(c\) Cartier on \(S\). The mate yields \(mc\sim bH\), so \(c\) is ample and
\[
c^2=d^2/a.
\]
Regularity along the Cartier smooth curve, adjunction, surface classification, and the Cartier restriction sequence give \(h^0(S,\mathcal O_S(c))=c^2+2\) and a basepoint-free system. Thus \(|c|\) identifies \(S\) with a normal minimal-degree surface. The possibilities are:

| Normalization and inverse curve | Polarization \(H\) | Degree \(a\) |
|---|---|---|
| \(\mathbf P^2\), line | \(\mathcal O(d)\) | \(d^2\) |
| \(\mathbf P^2\), conic (\(d\) even) | \(\mathcal O(d/2)\) | \(d^2/4\) |
| Smooth scroll of degree \(n\ge2\), hyperplane section, \(n\mid d\) | \((d/n)c\) | \(d^2/n\) |
| Rational-normal cone of degree \(n\ge2\), smooth Cartier hyperplane section, \(n\mid d\) | \((d/n)c\) | \(d^2/n\) |

For \(d=4\), the integral-quartic exclusion R-0001 removes the degree-four cases. Three **necessary** higher-degree possibilities survive: a degree-eight smooth quadric \((c,H)=((1,1),(2,2))\); a degree-eight quadric cone with \(H=2c\); and a degree-sixteen plane with \(c\) a line, \(H=\mathcal O(4)\). None is thereby shown realizable.

Non-Cartier inverse curves, multiple inverse branches, and higher-degree maps \(c\to C\) are not classified by this theorem.

[Canonical R-0002](../results/cartier_singleton_lift.md) · [open Q-0001](../questions/cartier_projection_models.md)

## 4. Projection admissibility and full conductor phase (R-0004)

A four-section subsystem of \(H^0(S,H)\) must first be basepoint-free and induce a **finite birational** map to an integral hypersurface. Next the full reduced inverse support of \(C\) must be precisely \(c\), with no isolated extra points. Only then is the fixed-carrier conductor question applicable.

In characteristic zero, for a fixed normal \(S\), smooth ample Cartier \(c\), a section \(Q\in H^0(S,H)\) with \(\mathrm{div}(Q)=mc\), and a finite-type family of four-section projections restricting to the fixed embedded curve, R-0004 gives a finite stratification and finite surjective cover \(Z\to T_0\) with a phase morphism
\[
z:Z\to(\mathbf G_m)^D.
\]
An admissible carrier has a mate precisely when its **full-conductor** phase tuple is torsion. Finite Artinian calculations keep nilpotent conductor equations; flattening and monic normalization equations prevent loss of generic conductor components on specialization. The torsion image has a finite torsion-coset envelope, but the mate locus need not be constructible.

For the three quartic singleton families, the on-curve conductor thresholds are respectively \(M=5,5,13\). If the phase order is \(E\), every positive multiple of \(E\) at least \(M\) is a mate degree; any additional mate degrees must be smaller multiples. The actual admissible phase images and torsion cosets **have not been computed**. A finite-type reduction is not a completed elimination.

[Canonical R-0004](../results/projection_phase_reduction.md)

## 5. Explicit negative example: degree-sixteen plane projection (R-0017)

Consider the four quartics on \(\mathbf P^2\) with coordinates \([s:t:z]\):
\[
[s^4:s^3t:st^3+\alpha z^4:t^4+zP_3(s,t,z)],\qquad \alpha\ne0.
\]
For the stated birational open condition (the \(A_3\) or \(C_1\) coefficient of \(P_3\) nonzero), the map is basepoint-free, finite birational onto an integral degree-sixteen surface, and has full reduced inverse support of \(C_0\) exactly \(z=0\).

**Nevertheless, no positive-degree homogeneous mate exists for this family.** The all-degree derivative contradiction detects a first-order nilpotent conductor obstruction invisible in the reduced inverse support. A broader two-fixed-coordinate full-singleton sublane has the same exclusion.

This refutes the implication “singleton reduced inverse support + a suitable upstairs divisor implies a mate.” It does **not** eliminate all degree-sixteen plane projections, much less all Cartier singleton models. The exact derivative calculation and its assumptions remain in the source proof and independent reconstruction.

[Canonical R-0017](../results/singleton_plane_conductor_descent.md) · [underlying calculation](../notes/2026-10-19-singleton-projection-investigation.md)

## 6. Normal carrier indices and socle compatibility (R-0034–R-0036)

These are **different** restrictions from the preceding nonnormal-conductor problem.

**Local Cartier index (R-0034).** For a normal integral carrier, an actual mate with divisor \(nC\), actual local Cartier index \(r\mid n\), \(k=n/r\), and a curvilinear generic transverse complete intersection, the pointwise top ordinary-power socle defects satisfy
\[
D_{n,P}=(k-1)A_{F,P}+kD_{r,P},
\qquad
2\sum_i\operatorname{length}(T_i)_P=nD_{n,P}.
\]
The *actual local Cartier index* cannot be replaced by surface multiplicity. The equations impose compatibility, not an unconditional exclusion.

**Bounded-index exclusion (R-0035).** In characteristic zero, for the fixed \(C_0\), a normal integral hypersurface carrier satisfying the inherited normal-carrier torsion reduction and quadratic-direction obstruction and with every actual on-curve Cartier index at most four cannot admit a mate in any degree. Indices six, twelve and higher, and nonnormal or entirely-thick presentations, are not excluded by this result.

**Pointwise conductor–socle identity (R-0036).** In characteristic zero, for an actual supported complete intersection, integral carrier generically regular along \(C\), full singleton smooth Cartier inverse curve \(c\cong C\), normalization smooth along \(c\), and invertible conductor \(\mathcal O(-B)\) without a \(c\)-component, the transverse differential zero divisor \(A\) and the top socle defect satisfy
\[
D_n=(n-1)A-B|_c.
\]
This is an equality of actual divisors, not just degrees. It is not established for multiple branches, non-Cartier lifts, singular normalization along \(c\), or a generically singular carrier; its Jacobian proof does not automatically extend to characteristic dividing \(n\).

[Local index R-0034](../results/normal_carrier_index_socle.md) · [bounded index R-0035](../results/normal_carrier_bounded_index_exclusion.md) · [pointwise identity R-0036](../results/pointwise_conductor_socle_defect.md)

## 7. What the methods do and do not prove

- **Numerical equivalence upstairs** gives candidate divisors, not descent.
- **Reduced conductor residues** can miss nilpotent first-order obstructions; R-0017 provides an actual failure.
- **Finite-type phase reduction** does not calculate admissible phase images or torsion cosets.
- **A normal bounded-index exclusion** cannot be extended to all nonnormal carriers or arbitrary indices.
- **A smooth singleton Cartier lift** is a strong hypothesis, not an automatic consequence of STCI.
- **Generic formal or function-field equations** are not necessarily global homogeneous equations. The separate finite normal-jet/global-coefficient investigation supplies the appropriate realization tests and counterexamples; its full content belongs in another dossier.

## 8. Concrete frontier

1. For each of the degree-eight smooth quadric, degree-eight cone, and degree-sixteen plane models, parameterize admissible four-section projections; test basepoints, finiteness, birationality, and **full** inverse support before computing phases.
2. Compute actual conductor algebras (including nilpotent structure) and phase maps on each admissible stratum. Determine whether their images contain torsion points, not just whether the ambient torus does.
3. Extend the fixed-carrier analysis to non-Cartier inverse curves, multiple branches, and nonisomorphic inverse maps without assuming the singleton lattice formula.
4. Investigate actual local Cartier indices above four and determine whether the socle identities yield additional exclusions.
5. Seek explicit cuspidal and ruled-cubic conductor calculations and identify precisely which descent step fails. These historical examples are **not yet source-reconciled in this batch**.
6. Compare any surviving conductor model against actual global homogeneous section constraints and the separate finite-jet criteria.

## 9. Source-preservation boundary of this batch

**Directly examined:** R-0002, R-0003, R-0004, R-0017, R-0034, R-0035, R-0036, Q-0001, and the current MAP/FRONTIER navigation. Their principal mathematical statements, assumptions, proof mechanisms and counterexample setup are incorporated above; their full source proofs remain linked and should not be deleted.

**Still to compare directly:** the historical Ultra source proofs and audits linked from these records, detailed local conductor calculations (including cuspidal/ruled-cubic examples), relevant scratch scripts, projection and singular-carrier historical investigations, and other mathematical source material not enumerated by Phase 1. No completeness or redundancy certificate is asserted for these sources.

**Deletion policy:** no original mathematical source is removed in this batch. Ordinary correction chronology should not be imported into the final exposition; substantive failed mathematical mechanisms should.
