# Acceptance: the entire nonendpoint homogeneous gcd-three lane is excluded

Date: 2026-10-14. Root integration. Status: **PROVED in the stated
characteristic-zero nonendpoint genus-one quintic A4 normalization
model, with every positive mate degree**. The universal STCI question,
unrestricted C0 question and other quintic normalization lanes remain open.

This accepts the final obligation of the
[owner continuation](2026-10-13-generalization-quintic-continuation.md)
after the earlier [independent geometric audit](2026-10-14-generalization-quintic-new-independent-audit.md).
The completed literal membership identity is an input; it is not
re-expanded here at the user's direction. The new root review matches
that final identity to the already reviewed six-generator geometry and
complete homogeneous support cover.

## 1. Exact coverage and inherited premises

Keep the actual center-avoidance, finite birational projection and
delta nonzero hypotheses of the accepted A4 model. The complete
homogeneous gcd-three classification is an accepted input. It covers
the zero-conormal-cubic charts and all nonzero proportional pairs,
including the entire lambda=1 boundary. Those zero and lambda-one
charts already have completed independent all-mate support exclusions.

In the remaining main proportional family, the accepted full inverse
support/conductor theorem forces the roots of the complete nonzero
binary octic to lie on the homogeneous cubic H3. Its factorization is
`F=constant H3 S5`. The allowed main parameters make

```
V=delta lambda(lambda-1)(lambda^2-4lambda+1)
  ((lambda+1)delta+lambda-1)
```

nonzero. The earlier review retains all Jbar-zero exclusions before
using support concentration. No Jbar-zero parameter is removed by
an unmentioned saturation.

The homogeneous leading-drop argument excludes infinity support in
this main family. Thus `c5=LC(S5)` is nonzero on any hypothetical
survivor, and all remaining roots of S5 are finite. The independently
audited support lemma gives a complete alternative:

1. At least three distinct roots force H3 squarefree and H3 dividing S5.
2. At most two roots have multiplicities 5, 4+1, or 3+2.

The first alternative and multiplicity at least four already have
literal original-generator witnesses and accepted independent geometry.
Repeated roots and all homogeneous leading drops remain covered.

## 2. The final original-generator identity

For multiplicities 3+2, choose x to be the triple root. The actual
six-generator row M6 comprises

```
S5(x), S5'(x), S5''(x),
c4^2-4c3 c5-6x c4 c5-15x^2 c5^2,
H3(x), (2c5)^3 H3(-(c4+3x c5)/(2c5)).
```

These are polynomial equations after the stated denominator clearing.
The second root is uniquely the double root of the residual quadratic;
2c5 is a unit. Thus every actual 3+2 support configuration satisfies
all six equations. Coalescence into a fifth root is also retained.

The completed source
[support32 witness](../computations/generalization_quintic_h3_support32_witness.m2)
loads those **original six generators**, finds exponent two, constructs
the column W, and asserts the exact identity

```
M6 W=(V c5)^2.
```

The [captured execution](../validation/2026-10-13-generalization-quintic-h3/support32-witness-attempt-01/execution-record.json)
records source SHA256
`2f8741c5cd8b7e1c97cc60d12ab0bad6409b6a7bc3121dcc09722a12b6b6c55a`,
exit zero and empty stderr. Its output explicitly reports exponent two
and the literal original-six-generator product pass. The source retains
the final product assertion before writing the witness.

At a simultaneous zero of M6 with Vc5 nonzero, this identity says
`0=(Vc5)^2`, impossible. This closes the last support pattern without
interpreting a leading resultant factor as an actual inverse point,
replacing full conductor multiplicity by a first symbol, or relying
only on a printed saturated unit ideal.

## 3. Archive and continuation bindings

The [exact witness archive](../validation/2026-10-13-generalization-quintic-h3/support32-witness.txt.gz)
contains 107657203 uncompressed bytes, SHA256
`65feb2e88ea19fd28d67512628a28915d05d1c7a44bd657fe7e99ada2910905b`.
Its gzip size is 50074835 bytes. The
[archive manifest](../validation/2026-10-13-generalization-quintic-h3/support32-archive-manifest.json)
checks archival identity only, not a new mathematical product.
The completed subset extraction, padded back to the original six
generators and verified there, has identical uncompressed witness
content. Both attempt records are preserved.

To inspect the large matrix, decompress to a temporary directory;
do not replace the repository archive by a greater-than-100MB raw file.
The original owner and independent audit's “3+2 pending” labels are
historical and are superseded by this completed certificate binding.

## 4. Accepted conclusion and exact open boundary

Every admissible nonendpoint genus-one quintic A4 projection whose
corrected conormal cubics have homogeneous gcd degree three is
excluded in every mate degree, including zero-cubic and proportional
families. This is the complete h=3 lane, not every genus-one quintic.

The remaining nonendpoint work retains homogeneous gcd degree two,
its repeated/two-root supports, and degree-one singular target-fiber
charts `qZ=0`, intrinsic A4/infinity and allowed Jbar-zero contributions.
Actual full conductor power descent on any surviving support locus
is still required. Other quintic genera, normal quintics, higher
carriers and entirely thick presentations remain separately open.
