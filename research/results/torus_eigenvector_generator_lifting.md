---
id: STCI-R-0038
type: result
title: Equivariant lifting of graded minimal ideal generators
status: provisional
scope: "#scope"
statement: "#statement"
proofs:
  - name: weight-decomposition-and-graded-nakayama
    at: "research/arguments/torus_hilbert_boundary.md#equivariant-minimal-generator-lifting"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Equivariant lifting of graded minimal ideal generators

## Scope

Let \(k\) be any field, \(S=k[x_0,\ldots,x_n]\) with its ordinary
standard grading and irrelevant ideal \(S_+\), and let a split algebraic
torus \(T\) act rationally on \(S\) by grading-preserving
\(k\)-algebra automorphisms. Let \(J\subset S\) be a homogeneous
\(T\)-stable ideal. There is no characteristic restriction. Stability
of the ideal, rather than only of its radical or its support, is required.

## Statement

The finite-dimensional graded minimal-generator module
\[
M(J)=J/S_+J
\]
admits a basis homogeneous for ordinary degree and for the character
grading of \(T\). Every such basis has lifts to ordinary homogeneous
\(T\)-eigenvectors in \(J\) of the same degrees and characters. These
lifts form a minimal homogeneous generating set of the entire ideal
\(J\).

In particular, if a \(T\)-stable homogeneous ideal has precisely two
minimal generators with ordinary-degree multiset \(\{a,b\}\), then it
has two eigenform generators with the same ordinary-degree multiset,
including when \(a=b\). Applied to the torus of weights
\((0,1,3,4)\), the characters are integer weights in every
characteristic; they are not weights reduced modulo the characteristic.

## Evidence

The direct proof in
[STCI-A-0001](../arguments/torus_hilbert_boundary.md#equivariant-minimal-generator-lifting)
constructs the weight lifts and proves generation by induction in
ordinary degree. It does not use a trace obstruction, a claim about
deformation of a fixed ideal, or any computation.

The source application is the minimal-generator paragraph in
[positive movement and the global presentation barrier](../synthesis/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier),
which states the diagonalization step in every characteristic. The
present proof isolates that step from the finite-modification and trace
arguments surrounding it.

## Limitations

Invariant reduced support does not imply \(T\)-stability of \(J\),
so the conclusion does not apply to an arbitrary supported thickening.
It produces eigenform generators only for an already invariant ideal;
it neither makes a moving ideal invariant nor says its invariant limit
has the same number of generators. It gives no sole-support exclusion
without a separate theorem concerning actual eigenform equations.
The torus is split; no assertion about diagonalizing a nonsplit torus
over its ground field is made.

## Review

Independent reconstruction review accepted the rational split-torus
character decomposition, equivariant weight lifts, and ordinary-degree
induction proving generation and minimality in every characteristic.
The reviewer reconstructed the proof, compared the declared source,
and found no blocking mathematical correction or lost contribution.
No mathematical computation was needed. This acceptance concerns an
already invariant ideal, not invariant support or the behavior of a
moving ideal's limit. The Result remains provisional.

Separately, the source retains its October 31, 2026 independently
reviewed provisional status, including its characteristic extensions.
That inherited source review is distinct from the reconstruction
decision above. The composite trace corollary STCI-R-0040 has a separate
reconstruction decision recorded in its own Result.
