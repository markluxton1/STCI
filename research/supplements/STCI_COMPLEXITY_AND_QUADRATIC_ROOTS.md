# STCI search, obstruction depth, and quadratic root certificates

Exploratory contribution, 2026-10-31. New claims below are independently reviewed
source-level deductions, with review recorded at the end; no canonical result,
research status, navigation, or priority is changed. Source state: worktree
`9cf8/STCI`, base commit `9eb97a059ba9e06520520fce33e4ec5c092010d7`.

The complexity viewpoint is useful here because it separates auxiliary
choices from genuine compatibility, and distinguishes the cost of finding an
obstruction from the size of its certificate. It leads to a concrete result:
the entire smooth, first-compatible **diagonal** quadratic-root locus in the
fixed ambient normal coordinates fails the second lift. One scalar pairing
certifies this on each of three already classified families. A second deduction
identifies the jump in minimal syzygy degrees exactly with spectral four-torsion.
Neither statement decides the remaining smooth incidence or unrestricted STCI.
The [torsion-two continuation](QUADRATIC_ROOT_TORSION_TWO_REDUCTION.md) extends
the exclusion to every smooth root with a pure square direction and reduces
all remaining torsion-two cases to one chart using actual ambient symmetries.
It also excludes the complete linear rank-drop boundary after the second
lift and proves a scalar-selection bound on its finite first-stage algebra.
The [ideal-sheaf continuation](IDEAL_SHEAF_SPECTRAL_SEQUENCES_AND_GLOBAL_JETS.md)
identifies a separate finite linear compatibility problem: actual global
equation jets. It proves an order-\(d\) global-extension cutoff for degree
\(d\) on this quartic and computes the exact sextic cutoff as order five.
Its filtered Cech sequence locates the eleven missing quadratic symbols
in a rank-11 third differential; this does not identify that differential
with either root-lifting obstruction.
The [intrinsic review](INTRINSIC_GEOMETRY_AND_STCI_COMPLEXITY.md) extends the
pushforward splitting to every power, distinguishes embedding invariants
from elimination choices, and refines finite scalar selection by counting
closed points over the coefficient field.

## 1. Fixing the computational questions

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

## 2. Reuse a finite verification theorem before discussing hardness

The independently reviewed [finite-normal-jet argument](../synthesis/finite_normal_jets.md)
already establishes the following. Let F,G be nonzero positive-degree
homogeneous forms in I_C, d=deg C, and M=ab/d an integer. With
R=O_(P3,eta_C), maximal ideal m_C, and J=(F,G)R,

    V_+(F,G)_red=C  iff  length R/(J+m_C^(M+1))=M.

This exact equality also checks properness. The proof uses the no-gap
property of the maximal-ideal filtration: a quotient of length at most M
after M+1 layers has already terminated, by Nakayama. A common global
surface factor would then reduce the available intersection degree while
preserving the generic length, an impossibility; degree exhaustion excludes
residual curves. The generic-length convention is the
[associated-cycle definition](https://stacks.math.columbia.edu/tag/02QV),
and the local termination step is [Nakayama's lemma](https://stacks.math.columbia.edu/tag/00DV).

If properness is independently known, the actual length is at most M and
the cutoff M suffices. Without properness that cutoff fails: for the line
C=V(x,y), the pair (xz^(M-1),x) gives truncated length M modulo m_C^M but
has a common plane. The extra layer detects length M+1 instead.

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

## 3. The exact bounded laboratory and its remaining nonlinear variables

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
[global presentation](QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md#2026-10-15-generalization-quadratic-root-global-second-dual-compression)
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

## 4. A geometric classification of the minimal second syzygies

Let Z=(f=0) be smooth, pi:Z->P1 the base projection,
A=O_Z(1,0), B=O_Z(0,1), and eta=B tensor A^-1. Define

    T_f = [ a b c 0 0 ; 0 a b c 0 ; 0 0 a b c ],
    W=ker[O^5 -> O(2)^3].

This is the accepted dual obstruction bundle; H0(W(10)) has dimension 16.
There is an exact splitting classification:

    W = O(-3) + O(-3)     if eta^4 is nontrivial;
    W = O(-2) + O(-4)     if eta^4 is trivial.

Here and below splitting is on the base P1 at the specified geometric root.
To prove it, push the divisor sequence
0->O(-2,2)->O(0,4)->O_Z(0,4)->0 to the base. It gives
E:=pi_*B^4=coker[O(-2)^3->O^5]=W^*=W(6).
Thus E is globally generated of rank two and degree six. The splitting
theorem for bundles on P1 (see [Grothendieck, Theorem 2.1](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf))
writes E=O(e1)+O(e2) with e_i>=0, e1+e2=6.

Now H0(E(-4))=H0(Z,eta^4), of dimension one exactly when eta^4 is
trivial and zero otherwise: a nonzero section of a degree-zero line bundle
on an integral projective curve has no zeros and trivializes it. Also
H0(E(-5))=0 since the corresponding line bundle upstairs has degree -2.
Therefore e_i<=4, leaving only (3,3) and (2,4); the previous dimension
test distinguishes them. Smooth (2,2) roots have eta nontrivial, so the
jump consists of exact orders two and four, rather than order one.

This can be detected without constructing the elliptic group law. Form
the coefficient-convolution matrix

    B_f: H0(O(2))^5 -> H0(O(4))^3,       q -> T_f q.

It is 15-by-15 with entries linear in f. Its kernel is H0(W(2)),
so on the smooth locus its rank is 15 off T[4] and 14 on T[4]. Hence
det B_f=0 detects T[4] set-theoretically there. No assertion about the
determinant's multiplicities or its singular-root locus is needed.

Off T[4], two degree-three syzygy generators give 8+8=16 pairings after
multiplication by base monomials. On T[4], degrees two and four give
9+7=16. Suitable bases can be chosen locally on the respective strata.
The obstruction dimension never jumps; the degrees of its generators do.
The 25 global tests retain value because they avoid these basis choices
and also cover singular and nonreduced roots. This splitting result does
not prove that replacing that global model is cheaper.

## 5. One scalar excludes the complete smooth diagonal locus

Impose b=0 **in the fixed actual ambient coordinates**. The independently
reviewed [diagonal classification](QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md#2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit)
reduces first compatibility to four explicit quadrics in the six coefficients
of a,c. For smooth roots these force c2!=0. Normalize only the scalar
of f so c2=1. Its three exhaustive families are as follows, with t!=0:

| Family | a(z) | c(z) | Second scalar |
| --- | --- | --- | --- |
| plus | 4+t z^2 | -8/t+z^2 | -16 |
| minus | -4+t z^2 | 32/t+z^2 | -640 |
| mixed | -4+t z-(5t^2/44)z^2 | 880/t^2+(44/t)z+z^2 | 1648 |

For clarity, the coverage does not use a change of the two rulings.
The inherited classification says a0=4c2 or -4c2. In the first case
a1=c1=0 and a2*c0=-8c2^2. In the second case either a1=c1=0 and
a2*c0=32c2^2, or a2*c0=-100c2^2, a2*c1=-5c2*a1,
a1^2=-(44/5)a2*c2. Taking t=a2 in the even cases and t=a1 in the
last case gives exactly the table after c2=1. Its denominator t is
nonzero in every smooth case; this discards no smooth boundary.

Let R4=sum r_i u^(4-i)v^i be the accepted actual second Cech
representative, after inserting the unique first correction h. Use

    q=(0,-c^3,0,a*c^2,0),
    Lambda(f)=coefficient_(z^-1)(-c^3*r1+a*c^2*r3).

The identity T_f q=0 is immediate for b=0, and q has base degree at
most six, hence is a valid section of W(10). It is the first column
of the accepted complementary-minor matrix. Consequently Lambda is
insensitive to Cech coboundaries and to the unknown next equation unit.
It tests the actual quartic correction, including the nonlinear base
coordinate substitution and the product of the first unit with its correction.

The [standard-library exact checker](../computations/quadratic_root_diagonal_certificate.py)
reuses the accepted chart generator through R4, substitutes the three
families and explicit first corrections, verifies all sixteen first
equations identically, and evaluates this single residue in Q[t,t^-1].
It obtains the table's constants. Restoring scalar c2=C multiplies each
constant by C^4: h is unchanged, R4 has f-degree one, and q has f-degree
three. Since C!=0, all three values remain nonzero in characteristic zero.

Thus the second-zero locus has empty intersection with the smooth
first-compatible b=0 locus. This is an exact negative certificate for
that bounded subfamily; it is stronger than testing its seed or generic
points. It is not an exclusion of the entire spectral torsion-two locus.
An arbitrary direction-coordinate PGL2 transformation diagonalizes an
abstract smooth torsion-two root, but need not preserve the actual
embedded obstruction operator. The distinction is essential to coverage.

## 6. What complexity has explained and what remains

The first lift contributes no extra search parameters; its difficulty is
the rank-four compatibility of actual roots. The second obstruction has
fixed dimension sixteen, but its minimal generators reflect genuine
spectral geometry through T[4]. Its displayed equation count also reflects
the choice between global generators and local bases. On the diagonal
locus, the nonlinear search collapses to three classified families and
one nonzero scalar each. This is a reduction in certificate content and
an avoided elimination, not a benchmark or inherent-hardness theorem.

The full initial ideal, its generator degrees, and relation gap retain
information absent from first symbols. Punctual defects and actual global
jet images can impose additional constraints; no complete invariant or
parameterized algorithm is claimed from this list. The accepted
[R-0005 formal-root theorem](../results/smooth_root_formal_obstruction.md)
and its finite-tower consequence supply an existential finite empty stage
for each fixed root order in their smooth balanced setting. They give
no numerical stage here and no degree bound for arbitrary STCI equations.
The fixed-pair length bound, a bounded-family empty-stage statement,
and a uniform witness bound as the curve varies are distinct quantifiers.

The proposed next investigation was undertaken in the
[torsion-two continuation](QUADRATIC_ROOT_TORSION_TWO_REDUCTION.md).
It retains the pencil's orientation relative to the actual ambient operator,
constructs a complete degree-two/four dual basis, and gives additional exact
exclusions and a single chart for the remaining mixed directions. That note
records the completed and incomplete calculations and the next unresolved
test. The formula q=(0,-c^3,0,a*c^2,0) remains only a diagonal specialization;
it is not a syzygy for arbitrary b. Neither continuation nor diagonalization
supplies an arbitrary PGL2 symmetry of the embedded obstruction operator.

## Review and executed evidence

- Inherited promoted statements: R-0005--R-0008 at their exact scopes.
  The diagonal classification and finite-jet theorem are independently
  reviewed source-level mathematics, not newly promoted records.
- New deductions: the smooth T[4] splitting/rank classification and
  the complete smooth diagonal second-obstruction certificate.
  Both passed independent review on 2026-10-31 and remain unpromoted.
- The `diagonal_review` reviewer independently reconstructed the complete
  diagonal classification, normalization/scaling, and dual-functional
  validity; statically reviewed the retained checker and its reuse of R4;
  then ran it successfully with all three exact constants above. The
  accepted embedded chart remained an explicit inherited premise.
- The separate `report_math_review` reviewer reconstructed the smooth
  splitting proof, the 15-by-15 rank detector, the local 16-test counts,
  the degree bounds 13/28, and the verification/search distinctions.
  It reused the separate diagonal/code review. Its next-step correction
  was incorporated: the displayed diagonal q must be replaced by a valid
  universal or moving syzygy when b!=0. No material finding remains open
  within these stated claims.
- Exploratory calculation actually run: symbolic substitution over Q(t)
  using SymPy 1.14.0, confirming the first equations and displayed residues.
  Reproduction of the final exact certificate uses only the standard library:

      python3 research/computations/quadratic_root_diagonal_certificate.py

  It prints the constants -16, -640, 1648 and a scoped PASS. Local proof and
  computation links and whitespace were checked; canonical metadata was
  unchanged, so its validator was not rerun.
- Not run in this initial exploration: a global Groebner basis,
  determination of every K1 or K2 component, a global 16-equation atlas,
  or a search for actual surfaces. Later torsion-two calculations are recorded
  in the linked continuation with their exact scopes.
  No claim of global second-zero emptiness or unrestricted STCI exclusion.
