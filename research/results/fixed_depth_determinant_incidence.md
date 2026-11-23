---
id: STCI-R-0080
type: result
title: Fixed-depth incidence products and actual residual cancellation
scope: "#scope"
statement: "#statement"
proofs:
  - name: universal center jets and finite Laurent trace matching
    at: "research/arguments/equations/fixed_depth_determinant_incidence.md#1-the-common-finite-jet-source"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Fixed-depth incidence products and actual residual cancellation

## Scope

Use the fixed quartic \(C=[s^4:s^3t:st^3:t^4]\), center ideal
\(P=(x_0,x_3)\), and the open of ordered homogeneous equation pairs whose
binary restrictions to \(V_+(P)\) have nonzero resultant. These pairs are
proper and give the finite-flat plane-pencil algebra.

## Statement

**Incidence geometry over any field.** For a finite collection of
characteristic coefficients \(\eta_j(H)\) with \(\deg(H)j\le L\), and
\(a,b\ge L+3\), the unrestricted source is noncanonically the product
of the source through \(C\) with \(\mathbf A^{4(a+b)+2}\), compatibly
with the coefficient map. The same product description holds for the
inverse image of every target subscheme, including a nonreduced one.
It retains the scheme-theoretic image and incidence geometry, not merely
field-valued attainable tuples. [FD1–FD3](../arguments/equations/fixed_depth_determinant_incidence.md#2-scheme-theoretic-determinant-incidence).

**Actual residual controls in characteristic zero.** For every \(L\ge1\),
\(p\ge1\), and \(b\ge L+3\), the explicit proper pair of degrees
\((2p,b)\) in FD6 contains \(C\), has residual curves, and satisfies
\[
 \eta_j(H)=0\quad\text{for every homogeneous }H\in I_C
 \text{ with }\deg(H)j\le L.
\]
This includes equal-degree mixed characteristic coefficients. Thus paired
quartic determinant coefficients can vanish through every fixed order, as
can both fixed quadric/cubic towers, on actual residual pairs.
[Construction and proof](../arguments/equations/fixed_depth_determinant_incidence.md#3-explicit-finite-laurent-trace-matching).

**Reduced controls with normal integral carriers.** Over an algebraically
closed field of characteristic zero, for every \(L\ge1\), even
\(a\ge L+4\), and \(b\ge L+4\), the same vanishings occur on a reduced
proper CI whose two carriers are normal and integral and smooth along
\(C\). The intersection has generic multiplicity one along \(C\) and
residual degree \(ab-4\). This follows by perturbing the explicit pair
within fixed-center-jet cosets and using conormal generation and Bertini.
[FD8 and its geometric proof](../arguments/equations/fixed_depth_determinant_incidence.md#5-the-controls-also-admit-normal-integral-carriers).

## Limitations

The affine-product result uses universal characteristic coefficients and
linear splittings; it does not infer scheme structure from geometric points.
The residual controls use generalized rational binomial coefficients, finite
Laurent Newton sums, and explicit high-center-order corrections. Their
characteristic-zero restriction is separate from the any-field incidence
statement. Conditions involving full support, deeper source coefficients or
additional carrier strata do not automatically factor through these jets.
Normality, integrality and reducedness alone do not repair the bounded
tests, but the controls do not supply minimal sole-support pairs or full
translated-cycle realizations.
Neither result proves unrestricted STCI existence or nonexistence.

## Review

On November 23, 2026, distinct generalizations and research-picture reviewers
supplied the incidence strengthening and actual cancellation mechanism.
The correctness reviewer and bounded technical reviewers independently
reconstructed FD1–FD7 in the written owner: universal factorization over
nonreduced coefficient rings, the homogeneous target, Laurent traces at
both ends, all residue classes of the mate degree, and residual support.
The literature follow-up checked the scope and classical inputs. No
computational sample is used as evidence for the general assertions.

The geometric strengthening in §5 was independently reconstructed by both
the correctness and geometry reviewers, including both degree bounds,
affine-coset Bertini, conormal generation at every point, normality,
integrality, generic transversality and reducedness of the full CI. Its
scope is algebraically closed characteristic zero and is distinct from
the any-field incidence result.
