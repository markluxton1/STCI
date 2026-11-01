# Fixed-degree equation verification and finite obstruction certificates

The finite existence locus, the cost of one chosen algorithm and the least
possible witness degree are different questions. This account retains the
source-reviewed exact certificate and parameter-coverage arguments from
`aad349d1c413e0de511dd6b62c2194faf706fda9`. It supplies no complexity lower
bound, uniform witness bound, general jet solver or unrestricted STCI decision.
The [global equation-jet filtration](global_equation_jets.md) owns finite
source realization and the actual sextic/octic illustrations.

## Fixing the computational questions

Work over Q with geometric existence over Qbar. An input curve is specified
by finite homogeneous polynomial generators with rational coefficients; in the
single-component discussion it is promised geometrically integral. Degrees,
coefficient bit lengths, and dense versus sparse encoding must be specified in
any asymptotic claim. Algebraic witnesses may require a finite number field,
represented by defining polynomials and exact coordinates. Restricting the
search to rational witnesses changes the existence question.

| Task | Exact finite formulation | Missing ingredient for an unrestricted search |
| --- | --- | --- |
| Verify a given homogeneous pair F,G | Radical identities, or the finite generic-jet test below | None for termination on this specified input |
| Decide existence at bounded degrees | Finite polynomial equations and inequations in actual global coefficients | No complexity estimate follows merely from finiteness |
| Find a pair or exclude the bounded family | Algebraic point with support certificate, or identities covering every empty branch | Generic failure or nonvanishing at one seed is insufficient |
| Bound witness size or obstruction depth as C varies | A theorem for a specified input family and parameter | The finite bounded problems supply no upper bound on necessary degrees |

For a proper pair of degrees a,b supported on an integral degree-d curve,
the transverse length is m=ab/d. This measures the chosen presentation.
For example the same line V(x,y) has presentations (x,y) and (x^n,y^m),
whose lengths are respectively 1 and nm. Arbitrarily large presentation
length does not force a difficult curve or a large minimum witness.

Similarly, in K[[u,v]], the displayed generators (u,u+v^n) have identical
first symbols; subtraction reveals the indispensable generator v^n of
the full initial ideal (u,v^n). Hiding v^n is a presentation issue, while
the colength n is an invariant of this ideal. Neither is an invariant
of the reduced curve alone. Changing generators, changing the supported
thickening, and changing the curve are three different comparisons.

## Reuse a finite verification theorem before discussing hardness

The independently reviewed [finite-normal-jet argument](finite_normal_jets.md)
already establishes the following. Let F,G be nonzero positive-degree
homogeneous forms in I_C, d=deg C, and M=ab/d an integer. With
R=O_(P3,eta_C), maximal ideal m_C, and J=(F,G)R,

    V_+(F,G)_red=C  iff  length R/(J+m_C^(M+1))=M.

This equality also checks properness. The complete proof, the sharp M+1
cutoff without properness, the improved M cutoff with properness, singular
integral curves and weighted reducible extension remain in that linked owner.

In compatible generic normal coordinates the matrix acts on
A_N=K[u,v]/(u,v)^N, K=Qbar(C), N=M+1. Its D=N(N+1)/2 rows encode
the map A_N^2 -> A_N, (p,q) -> pF+qG. The criterion is rank D-M.
All monomial multiples are needed; the two initial jet vectors alone
do not generate the whole truncated ideal. This is an O(M^2)-row
description, with ordinary elimination requiring O(M^6) field operations
once the matrix is supplied. This is an arithmetic upper bound for this
dense matrix algorithm, not a bit bound for constructing the jets or for
function-field arithmetic. The theorem and its proof are reused here;
no new general jet solver was implemented.

At fixed degrees, coefficients of F and G range over bases of I_C(a),
I_C(b) as **constant-field** scalars. Replacing them by arbitrary elements
of K would permit non-global equations and change the problem. Clearing
function-field denominators and using its actual algebraic relations turns
the rank test into finitely many polynomial equalities and inequations
over Q. Their finite disjunction gives a decision procedure in principle.
Even though ambient P3 has fixed dimension, the number of surface
coefficients can grow like binomial(a+3,3)+binomial(b+3,3). Generic
hardness constructions in growing ambient dimension do not automatically
apply to this family.

A positive certificate can instead list, for generators p_i of the prime
homogeneous cone ideal I_C, identities

    F,G in I_C,       p_i^e_i=A_i F+B_i G  for every i.

These prove radical equality. Conversely sole projective support implies
equality of affine cone supports (the origin is included), so such identities
exist by the [Nullstellensatz](https://stacks.math.columbia.edu/tag/00FS).
An empty bounded branch P_1=...=P_s=0, Q!=0 can be certified by

    1=sum A_i P_i + B(wQ-1).

Every branch, including degree drops and exceptional strata, must be covered.
These are finite verifiable certificates, with no asserted polynomial bound
on their size in the original curve encoding. Enumerating degree bounds
terminates on positive instances, but the finite verification theorem gives
no bound on the degree where a positive witness must appear, nor a stopping
rule for every negative instance. No hardness or undecidability claim is made.

## The exact bounded laboratory and its remaining nonlinear variables

Fix C0=[s^4:s^3t:st^3:t^4], in characteristic zero, and its accepted
actual embedded normal coordinates. The first root is

    f=a(z)u^2+b(z)uv+c(z)v^2,

with a,b,c homogeneous base quadratics without a common base zero. Their
projective coefficients form U in P8. The canonical
[R-0007](../results/quadratic_root_obstruction_model.md) supplies an everywhere
injective 16-by-12 matrix A_f and vector d_f, both linear in f, and

    K1={f in U : A_f h=d_f for some h}.

The correction h is unique. Thus K1 is already a rank-four quotient
obstruction on eight projective root parameters; the twelve h variables
are not twelve independent geometric choices. On a chart where a
12-by-12 row minor Delta_p is nonzero, solve h=A_p^-1 d_p and retain
only the four residual rows. This is an exact scheme-theoretic elimination.
All such minor charts cover U; one convenient chart is not full coverage.
After denominator clearing the four equations have degree at most 13.

On K1 the second obstruction is a rank-sixteen section. Its accepted
[global presentation](../supplements/QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#2026-10-15-generalization-quadratic-root-global-second-dual-compression)
uses 25 scalar pairings and no second correction variables. Smoothness is
Disc_binary-quartic(b^2-4ac)!=0, which keeps a simple branch point at infinity.
The affine model has nine root coefficients, twelve first corrections,
and one discriminant-inverse variable. It is not an asymptotic family by itself.

Eliminating h does not make the root problem linear. The second polynomials
have f-degree four and h-degree at most two. Substituting Cramer's rule and
clearing Delta_p^2 can raise their degree to 28. Fewer unknowns can therefore
cost higher degrees and extra charts. The global 25 tests have nine moving
linear dependencies; selecting 16 fixed rows everywhere is not justified.
No runtime improvement is inferred from these counts.

The accepted seed f0=(z^2+4)u^2+(z^2-8)v^2 is a smooth point of a
four-dimensional projective component of K1, with exact spectral torsion
two and a nonzero second obstruction. That proves generic failure on this
component, not emptiness of its zero locus or of other components.

The connection to actual supported complete intersections requires **all**
the [R-0006 bridge hypotheses](../results/actual_ci_smooth_root_bridge.md):
saturated first relation, both actual equations of generic order two,
their symbols generating the first line everywhere, full generic initial
ideal a coprime binary CI (f_2,g_s), and the full root smooth. The second
test is necessary in this setting only for s>4; at s=4 the next relation
changes its target. Local or graded compatibility does not supply global
surfaces, properness, or sole support.

## Scalar selection on a finite algebra

Let \(B\) be a nonzero finite commutative unital algebra over an infinite
field \(k\), with \(c\) maximal ideals. If \(s_0,\ldots,s_{m-1}\)
generate its unit ideal, at most \((m-1)c\) values \(t\in k\) make
\(\sum_jt^js_j\) a nonunit. In each residue field the corresponding
polynomial is nonzero and has at most \(m-1\) roots in \(k\). A unit is
exactly an element nonzero in every residue field; nilpotents do not alter
this criterion.

Over \(\mathbf Q\), one of the integers \(0,\ldots,(m-1)c\) therefore
works. Since c≤dim_k B, the coarse length-based bound (m−1)dim_k B also
holds. Counting closed points can be much sharper than counting geometric
embeddings or nilpotent length. The [torsion-two application](quadratic_root_torsion_two_lifting.md#scalar-compression-on-the-finite-rank-drop-stage)
uses this lemma to improve0..1140 to0..120 from the actual two finite algebras;
its number-field irreducibility and dimensions are essential inputs. No
successful scalar or inverse is supplied by the bound alone.

This controls scalar selection, not certificate bit size. Residue-field
degrees still affect arithmetic and storage; the ordered generating list
still affects \(m\). Over a finite field the entire set of choices can be
bad: in \(B=\mathbf F_q^q\), the elements \(s_1=1\) and \(s_0(x)=-x\)
generate the unit ideal, yet \(s_0+ts_1\) has a zero factor for every
\(t\in\mathbf F_q\).

## What to measure in the next calculation

The useful parameters describe different tasks:

| Task | Geometric quantity | Algorithm-dependent quantity or missing bound |
| --- | --- | --- |
| Recover fixed-degree global sources | Surjective and bijective realization depths; the [intrinsic source-filtration ranks](global_equation_jets.md#the-source-deficit-is-a-canonical-filtration-not-a-matrix-size) | Constructing the connecting maps and recognizing the final depth |
| Solve linear compatibility | Actual source and correction dimensions; the [flag obstruction quotient](global_equation_jets.md#the-correction-recursion-is-an-exact-sequence-of-obstruction-spaces) | Basis density, denominators, and coefficient growth |
| Solve nonlinear compatibility | The specified root/contact incidence and its rank strata | Elimination order, chosen projection, and coverage of exceptional charts |
| Verify a supplied proper pair | Generic transverse length \(ab/\deg C\) | Constructing its actual normal jets and exact function-field arithmetic |
| Compress a finite exclusion | Closed support, residue fields, and the ideal generated by obstruction sections | Selecting a scalar, producing its inverse, and storing a certificate |
| Decide unrestricted STCI | The least possible witness degrees, if a witness exists | No uniform witness bound is proved here |

For example, the nineteen-point exceptional base is a determinantal locus
of the **specified** elimination map and projection. It is invariant under
compatible changes of bases of that map, but a different projection or
linear subsystem can produce another locus. Its nineteen points and the
length-76 fibers are not invariants of the abstract spectral curve.

Once the finite connecting matrices are supplied, their kernel and image
calculations are ordinary linear algebra. If their dimensions and all
intermediate compatible-section dimensions are bounded by \(D\), processing
\(N\) stages by dense elimination takes at most \(O(ND^3)\) field operations.
This excludes construction of the matrices and growth of exact coefficients;
it is not an end-to-end bit bound. Precomputing the actual homogeneous
source may avoid constructing much larger formal jet spaces altogether.

In families, fixed bundle ranks and base-change compatibility must be checked
before treating the images as vector bundles or transferring fiber ranks.
A flat family of curves alone does not establish the required behavior of
every higher-page differential. Similarly, intrinsic nonlinear parameter
dimension is not itself a runtime bound.

Applying the flag recursion to an actual root-lifting incidence requires a
specified rank stratum and comparison maps retaining all correction freedoms.
A larger unified complex alone establishes no such comparison.

## Scope and review

The fixed-degree verification theorem is reused at its full hypotheses from
[finite normal jets](finite_normal_jets.md), without another proof copy. The
source's `report_math_review` checked the13/28degree controls and
verification/search distinctions; `root_complexity_generalization_review`
and `global_jet_bound_review` independently checked the finite-algebra scalar
lemma, closed-point versus embedding count and its finite-field counterexample.
`intrinsic_filtration_review` checked the conditional O(ND³) field-operation
cost, excluding matrix construction and coefficient growth.

The all-power spectral proof belongs to [spectral pushforwards](spectral_pushforward_powers.md);
the n=4 application is [syzygy splitting](spectral_torsion_and_syzygy_splitting.md).
The [torsion-two actual lifting account](quadratic_root_torsion_two_lifting.md)
owns completed diagonal/pure-square/rank-drop exclusions and the exact finite
scalar application. Those are bounded source-level results, not emptiness of
the remaining full root incidence. The smooth formal-root theorem supplies
an existential finite empty stage only at its own fixed-root-order hypotheses,
not a numerical stage or a bound on arbitrary STCI equation degrees. No
arbitrary-PGL2 operator symmetry is inferred from abstract spectral geometry.
