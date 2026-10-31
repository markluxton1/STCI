# Independent review: tropical model, endpoint normals and characteristic

Date: 2026-10-31. Reviewer: `boundary_literature` subagent, independently
of the source author. Scope: the exact state of
[the tropical-model note](2026-10-31-tropical-model-characteristic.md)
reviewed with equations (1)–(8) and its four sections. Outcome:
**no material correction found; reviewed provisional deductions, no promotion**.

## Independent reconstruction

The curve is the fixed smooth quartic
`[s^4:s^3t:st^3:t^4]`. The explicit toric calculations below work over an
algebraically closed field in every characteristic; the general schön-open
existence statement is restricted to characteristic zero.

- The inverse torus-coordinate formulas have exponent determinant one.
  In those coordinates the closure is precisely
  `P1 × {(1,1)}` in `P1 × Gm²`, and its ideal is `(u−1,v−1)`.
  After replacing the source coordinate by `z'=a·z`, multiplication is
  projection with fiber `Gm`; it is smooth and surjective. Properness of
  this curve and this map verify Tevelev's definition directly, without
  assuming that the ambient is proper.
- Both formulas (2) agree on the overlap and have no undefined point,
  since `u,v` are units. The dense torus map is an isomorphism. The two
  boundary fibers are exactly `Gm²`, so the ambient morphism is not
  proper. Its restriction to the curve is the specified embedding.
- At zero, pulling back the two generators of the target conormal ideal
  gives exactly `t³U,t⁴V`. At infinity, expanding
  `τ⁴(v⁻¹−u⁴v⁻⁴)` and `τ³(v⁻¹−u³v⁻³)` gives respectively
  `τ⁴(−4U+3V)` and `τ³(−3U+2V)` modulo `(U,V)²`.
  The displayed matrix is the **normal** map from source normal vectors
  to target normal vectors. The matrix of conormal pullback, in column
  coefficient conventions, is its transpose; no reversal of the bundle
  map in the note is needed.
- The infinity determinant is `τ⁷`. The ideal of matrix entries is
  `(τ³)`, since the bottom row constants `−3,2` generate the unit ideal
  over every field. The Smith exponents are therefore exactly `(3,4)`
  in all characteristics, including two and three. The zero matrix has
  the same exponents. A generically invertible map from a locally free
  sheaf on the integral curve is injective. Its two torsion cokernels
  consequently have total length fourteen. The assertion about splitting
  is correctly attributed only to promoted
  [R-0020](../results/quartic_conormal_characteristic_jump.md); the local
  invariant factors alone do not establish that splitting.
- Clearing denominators in the particular two tropical equations gives
  the curve on `x0≠0` and the entire line `x0=x1=0` on its complement.
  This is an actual projective residual curve for that pair. The note
  correctly makes no universal claim about all possible descents.

## Characteristic and trace checks

For a hypothetical supported proper CI, Cohen–Macaulay purity makes a
lift of a parameter of the smooth support a nonzerodivisor. The completed
local algebra is finite free over that parameter ring, of rank the
generic thickness `m`. Over its fraction field, filtration by powers of
the nilradical proves `Tr(h)=m·h_bar`; equality extends by torsion
freeness. Under finite CI duality the relative Jacobian represents this
trace functional. If `p|m`, it is zero. If `m` is invertible, dualizing
the quotient onto the reduced parameter ring identifies its trace
element with a generator of the annihilator of the nilradical. This
checks the local paragraph independently; it does not assume the pending
characteristic-zero contact/Jacobian proposal has been accepted.

In characteristic seven, eliminating `x3=x1⁴` on `x0=1` in (8) gives
exactly `(x2−x1³)⁷`. On `x0=0` the sole support point is `pInfinity`.
There is therefore no common surface component, and the proper CI has
only the stated curve as reduced support and generic multiplicity seven.
The derivative `G_x2` is zero, so `M12=0`. Coordinate reversal sends
the pair, up to the sign of the quartic, to the `b=c=1,a=5` instance of
the existing P-028 construction in
[RESEARCH_RECORD.md](../RESEARCH_RECORD.md). This is reused evidence,
not a new family. Separately, the reduced fourth-power map is separable
and tame in every odd characteristic and purely inseparable of degree
four in characteristic two. These checks support the note's distinction
between inseparability of the reduced cover and vanishing of
multiplicity-weighted trace on its thickening.

## General scope, geometry and verification boundary

The primary-source statements of Tevelev and Luxton–Qu were checked in
the reviewer's preceding bounded literature task and reused here.
They establish the stated characteristic-zero schön-open and local
regular-embedding conclusions. They do not establish a general global
Cartier-divisor STCI theorem. The note preserves that gap explicitly.

Geometrically, the torsion cokernel measures the degeneration of the
two actual transverse coordinates under the toric morphism at the
endpoints. It neither counts residual components nor controls higher
neighborhoods. The construction proves scheme CI existence in this
tropical ambient; its displayed projective descent has residual support.
Neither fact settles arbitrary projective defining pairs. The
characteristic-seven example independently shows why tame reduced
ramification is compatible with positive-characteristic STCI existence.

All new checks above were independent hand reconstruction. No computer
algebra calculation, inherited certificate rerun, or canonical metadata
promotion was performed. The stronger general reembedding statement and
the unrestricted characteristic-zero STCI question remain open here.
