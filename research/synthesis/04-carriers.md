# 4. Carrier surfaces, normalization, and conductor

Chapters [2](02-two-surfaces.md) and [3](03-infinitesimal-geometry.md) treat both defining equations and their transverse behavior along the curve. Here we **fix one integral carrier** \(X=V(F)\subset\mathbf P^3\) containing \(C=C_0\), and ask whether some second homogeneous equation \(G\) cuts out exactly \(C\) on \(X\).

The central issue is global: **does a divisor supported over \(C\) on the normalization of \(X\) descend to an actual hypersurface section of \(X\)?** The answer involves both divisor classes and conductor gluing.

## 4.1 Passing to the normalization

Let \(\nu:S\to X\) be the finite normalization, and put
\[
H=\nu^*\mathcal O_X(1),\qquad W=(\nu^{-1}C)_{\mathrm{red}}.
\]
The inverse image \(W\) may have several irreducible curves, some mapping to \(C\) with degree greater than one, and possibly isolated points. One must use the **full inverse support**, not just a preferred component.

If \(G\) is a mate of degree \(b\), the pulled-back section of \(bH\) has zero support exactly \(W\). If the curve components are \(\Gamma_1,\dots,\Gamma_t\), its divisor is
\[
\operatorname{div}(\nu^*G)=\sum_{i=1}^t n_i\Gamma_i,\qquad n_i>0,
\]
and hence
\[
\sum_i n_i[\Gamma_i]=b[H]\quad\text{in }\operatorname{Cl}(S).
\]
This is **necessary**. A class-group relation alone is not sufficient, because a rational section on \(S\) need not descend through the nonnormal locus of \(X\).

## 4.2 The full-conductor descent criterion

The accepted [fixed-carrier theorem, STCI-R-0003](../results/fixed_carrier_conductor_criterion.md), works for an integral Cohen–Macaulay projective surface with finite normalization and ample polarization. First, an isolated inverse-image point outside the curve components obstructs a mate. In the remaining case define the relation lattice
\[
\Lambda=\ker\left(\mathbf Z^{t+1}\longrightarrow\operatorname{Cl}(S)\right),\qquad
(n_1,\dots,n_t,b)\longmapsto\sum_i n_i[\Gamma_i]-b[H].
\]
A relation produces an upstairs rational section with the prescribed divisor. Along conductor components away from \(C\), its **full conductor-unit classes** determine whether some positive power descends. Denote by \(\Lambda_{\mathrm{desc}}\) the sublattice whose off-\(C\) unit classes are torsion in the appropriate full conductor quotients.

**Established criterion:** a positive power of the polarization has a section vanishing set-theoretically exactly on \(C\) if and only if \(\Lambda_{\mathrm{desc}}\) contains a vector with every \(n_i>0\). For a hypersurface carrier in \(\mathbf P^3\), such a section lifts to an ambient homogeneous mate.

The conductor condition is not merely matching values on the reduced double locus. Nilpotent structure may impose further gluing conditions. In characteristic zero, residual torsion of reduced phases alone does not eliminate these nilpotent defects.

This is an **exact theorem for a specified carrier**, not an effective classification of every possible carrier: its class group, inverse branches, and conductor-unit map still have to be computed.

## 4.3 The special case of one Cartier inverse curve

Suppose \(W=c\) is a single curve, \(\nu|_c:c\to C\) is an isomorphism, and \(c\) is Cartier on \(S\). These are **additional hypotheses**, not properties of an arbitrary normalization.

The accepted [singleton-lift classification, STCI-R-0002](../results/cartier_singleton_lift.md), applies **assuming a mate exists**. Its key geometry is that the mate yields a positive divisor relation
\[
m c\sim bH.
\]
Consequently \(c\) is ample, and the complete linear system \(|c|\) identifies \(S\) with a normal surface of minimal degree. The proof uses the Cartier property, regularity along \(c\), adjunction, and surface classification. The theorem is a **necessary-model classification**, not a converse construction.

For our fixed rational quartic, after excluding degree-four carriers by [STCI-R-0001](../results/quartic_carrier_exclusion.md), three higher-degree normalization/polarization models remain within this restricted class:

| Carrier degree | Normalization | Lift and polarization |
| --- | --- | --- |
| 8 | Smooth quadric \(\mathbf P^1\times\mathbf P^1\) | \(c\sim(1,1)\), \(H\sim(2,2)\) |
| 8 | Quadric cone | \(c\) a smooth Cartier hyperplane conic, \(H\sim2c\) |
| 16 | \(\mathbf P^2\) | \(c\) a line, \(H\cong\mathcal O_{\mathbf P^2}(4)\) |

None of these rows establishes that the required projection or mate exists. Non-Cartier inverse curves, multiple inverse branches, and degree-greater-than-one maps to \(C\) are outside this classification.

## 4.4 Why projections are the next problem

To obtain a carrier in \(\mathbf P^3\) from a listed \((S,H,c)\), choose four sections of \(H\) whose restrictions to \(c\) give the fixed embedded curve \(C\). These sections must define a basepoint-free finite birational map onto an **integral hypersurface**, and the **full reduced inverse support** of \(C\) must equal \(c\).

Even if all these geometric admissibility tests pass, the conductor descent condition for a mate remains. Thus the work splits into three distinct checks:

1. **Projection admissibility:** the four sections produce the required finite birational hypersurface map.
2. **Inverse-support control:** there are no additional curve branches or isolated inverse points over \(C\).
3. **Conductor descent:** an upstairs positive divisor relation gives a descending section, possibly after a power.

The open [projection-model question, STCI-Q-0001](../questions/cartier_projection_models.md), asks whether these checks can succeed for any of the three models.

## 4.5 Phase maps and torsion cosets

The accepted [projection-family reduction, STCI-R-0004](../results/projection_phase_reduction.md), treats fixed finite-type families of admissible projections with the stated Cartier singleton hypotheses. After finite stratification and a finite surjective cover, the full-conductor descent problem is encoded by a morphism into a torus. A parameter admits a mate **if and only if** its phase tuple is torsion.

This is a significant reduction: it replaces an unbounded search over mate degrees by a structured question about the phase image and its torsion points. But the actual phase images and surviving torsion cosets for the three fixed-\(C\) models **have not been computed**. The mate locus need not itself be constructible.

In particular, the existence of a finite-type phase description is not a proof that one of the models admits a mate, nor that all three fail.

## 4.6 Interface with the simultaneous-equation geometry

These approaches study the same hypothetical pair \((F,G)\), but retain different information:

| Simultaneous \(F,G\) approach | Fixed-carrier normalization approach |
| --- | --- |
| Normal orders and common initial factors | Inverse branches of \(C\) on \(S\) |
| Exceptional directions on \(\operatorname{Bl}_C\mathbf P^3\) | Divisor classes and positive relations on \(S\) |
| Higher transverse contact and successive transforms | Gluing through the full conductor |
| Degeneration of graded second relations | Failure of a global section to descend |

There is a plausible research interface: exceptional directions and their special-point degenerations may reflect branches or conductor behavior of a chosen carrier. But **no general identification of these structures has been proved in the canonical records**. The first task is to formulate an exact comparison for a specified carrier and its normalization, not to assume that the two obstruction theories coincide.

## 4.7 What this chapter does and does not establish

**Established:** the fixed-carrier conductor criterion; the restricted Cartier singleton-lift classification; and the fixed-family torsion-coset reduction, each under its precise hypotheses.

**Open:** computation of the actual projection phase images and conductor descent for the three models, and treatment of non-Cartier, multiple-branch, or higher-degree inverse lifts.

**Provisional:** a direct geometric bridge between the common-normal-factor curve of Chapters 2–3 and the normalization/conductor data of an arbitrary carrier.

Next: [how the exclusion results assemble](05-exclusions.md), followed by the [surviving frontier](06-frontier.md).
