# Scope audit of the raw projection-family decision corollary

Date: 2026-10-16. Reviewer: `phase_family_audit`.
Status: **PASS for the precise explicit rational fixed-model input below.**

Reviewed only [Section 9 of the effective phase-bound note](2026-10-15-generalization-effective-rational-phase-bound.md)
and [Section 8 of its independent review](2026-10-15-generalization-effective-rational-phase-bound-independent-review.md),
including the newly added admissibility paragraph. The accepted finite-phase
theorem and explicit-`W` Mann/SNF/boundary theorem are premises; their proofs
were not replayed. No actual phase image, CAS computation, or family decision
was attempted.

## Reviewed claim and input

The corollary is an **algorithm-existence and termination theorem** from an
explicit projection-family presentation, without a separately supplied phase
image. Input consists of one of the three specified fixed rational normal
graded source rings, its prescribed `H,c,Q`, four sections with polynomial
parameter coefficients over `Q`, and finite `Q`-constructible parameter
restrictions. The prescribed restrictions of the sections to `c` must hold
or be imposed by their finite coefficient equations. Arithmetic, ideal and
module presentations, and zero tests are consequently effective.

Within this scope, the composite procedure constructs a rational phase-image
presentation and applies the accepted explicit-`W` decision procedure. It
decides whether the input family contains a mate-admitting carrier, whether
least mate degrees are unbounded, and computes a valid uniform bound in the
bounded case. This does not assert those outputs have already been computed.

## Why the new raw-input bridge passes

The admissibility paragraph supplies a genuine effective step. Basepoint
incidence and extra inverse points outside `c` are polynomial formulas on
finitely many projective affine charts, so effective algebraically closed
field quantifier elimination computes their parameter conditions. Once
basepoint free, the accepted ampleness argument makes the source map finite
before birationality is tested. Thus the image algebra `A subset B` and its
finite quotient module `B/A` are available without first assuming degree one.
For an explicit certificate, these source rings are standard graded in the
`H`-grading: basepoint freeness makes `B/(f_0,...,f_3)` finite-dimensional,
and a computable finite monomial basis lifts to `A`-module generators of `B`
by induction on degree. Flattening `B/A` preserves the actual fibre image.
A homogeneous monic Groebner basis of the image ideal preserves its leading
monomials and Hilbert polynomial on a computed open. The degree formula then
filters the degree-one locus. All closed complements are revisited, including
those of opens where the generic map has degree greater than one. Actual
integral surface images in `P3` are hypersurfaces. There is no circular
admissibility oracle in this step.

After this filter, finite-module syzygies and annihilators compute generic
common conductors. The searches for Noether coordinates, finite module
generators, bases, and separable primitive elements have finite certificates
checkable over the computably presented fields `Frac(R)` and `Frac(R)(x)`.
The accepted geometric existence results guarantee search termination; a
parameter piece need not be a rational variety.

The module generic-freeness proof is sufficient: retain both generation
directions for a monic module Groebner basis and its Buchberger reductions,
then invert their coefficient denominators. Standard module monomials give
a free localized parameter module, possibly of infinite rank. Applying this
to the relevant cokernels preserves fibre kernels and inclusions. The
[Derksen--Kemper primary source, Theorem 2.13 and Algorithm 2.14](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.28.pdf)
supports the related domain-ring method; the note correctly supplies its
own module argument rather than attributing that extension to the source.
Monic finiteness certificates for entire conductor quotients are retained
before rational-function localization.

On each `Q`-integral affine parameter piece, a computed nonzero localization
element leaves a closed complement with finitely many computable prime
components of strictly smaller dimension. The resulting finite recursion
retains all exceptional strata. Effective quantifier elimination finally
computes the actual constructible phase image, including inequalities and
deleted boundaries, so the accepted explicit-`W` procedure applies.

## Corrections and limits

This audit made three clarifications in Section 9: prescribed restrictions
to `c` are explicit input conditions; image Hilbert data are preserved using
a homogeneous monic basis; and the source ring is called *finitely
presented*, rather than ambiguously *finite*, as a graded algebra.

No unresolved algorithmic gap was found for this input. The PASS does not
extend to arbitrary unspecified normalizations, noncomputable coefficients,
or unpresented parameter restrictions. It gives no implementation, practical
complexity estimate, actual phase equations, numerical bound for the whole
three families, or decision which outcome holds for them. The independently
accepted explicit-`W` theorem is unchanged. The unrestricted fixed-C0 and
universal projective-curve STCI questions remain open.
