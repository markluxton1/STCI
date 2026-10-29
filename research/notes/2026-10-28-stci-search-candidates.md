# Finding equations: candidate sources and informative failures

Started October 28, completed October 29, 2026. Status: **provisional search
synthesis**, with accepted inputs identified below and one independently
checked new failed-candidate test. No canonical status changes.

## 1. Exact search problem and evidence boundary

Fix \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), with \(k\)
algebraically closed of characteristic zero. We seek actual homogeneous
forms \(F_a,G_b\) with scalar coefficients, no common surface factor, and
\(V(F_a,G_b)_{\rm red}=C_0\). For every proper containing pair first retain
\([V(F,G)]=m[C_0]+R\) and \(ab=4m+\deg R\); the candidate succeeds when
\(R=0\), rather than when a selected normal symbol looks plausible.

[R-0001](../results/quartic_carrier_exclusion.md) and its accepted factor
reduction allow the two equations in a minimum presentation to be taken
irreducible, both of degree at least five. Properness and degree exhaustion
force \(4\mid ab\). These are necessary conditions. They do not reduce
every witness to one of the conditional root rows below.

The [finite-search logic audit](2026-10-28-stci-search-logic-audit.md)
gives a complete fixed-degree test with actual global coefficient spaces:
at the generic point of \(C_0\), the transverse length must equal
\(ab/4\). A truncated multiplication matrix including **all** normal
monomial multiples tests this exactly at order \(ab/4+1\), restricted
to proper pairs. For fixed \(F\), solve the resulting actual global
\(G_b\) condition and remove the subspace \(F\cdot S_{b-a}\).
Nonzero kernel consisting only of those multiples is a failed mate search,
not a candidate.

## 2. Cheap restrictions that change which equations to generate

**Binomial carriers are already excluded, even with an arbitrary mate.**
Thoma, *Monomial Space Curves in P3 as Binomial Set Theoretic Complete
Intersections* (1989), Theorem 3.1, proves that the twisted cubic is the
only smooth monomial curve with such a characteristic-zero presentation.
Its definition requires only one equation to be binomial. The
[existing literature note](2026-10-05-literature-new-routes.md), Section 1,
records the theorem and checked
[author-uploaded primary text](https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections)
([DOI](https://doi.org/10.1090/S0002-9939-1989-0976361-7)). Reviewer
`toric_candidate_audit` freshly checked its definition and theorem in this run.
Therefore a search restricted to binomial \(F\), even with a general \(G\),
cannot succeed for this curve in characteristic zero.

**Both extremal weight pairs impose stronger filters.** In the weights
\(w=(4,3,1,0)\), Hellus--Huebl Theorem 1.2 requires that
\((F_{\min},G_{\min})\) and \((F_{\max},G_{\max})\) each be principal
up to radical, and that both extremal gcds lie in \(I_{C_0}\).
The reviewer checked the [institutional primary PDF](https://epub.uni-regensburg.de/29780/1/24-2013.pdf),
printed pages 1--4. A nonconstant gcd alone is weaker than the condition.
These are tests of the pair; a carrier can guide which extremal mate
components to generate before a larger jet calculation.

This also rules out a torus-weight-homogeneous irreducible carrier. Indeed,
its gcd with an extremal component of a prospective mate must be the
carrier itself. Subtract that carrier multiple from the mate, preserving
homogeneity in ordinary degree and shrinking its weight support. Choosing
a representative modulo \(F\) with minimal weight support gives a
contradiction unless the mate lies in \((F)\), violating properness.
Factor reduction extends the observation to such reducible carriers.
This deduction uses the literal characteristic-zero extremal theorem;
it does not assert anything about every mixed-weight surface.

For example, put
\[
q=x_0x_3-x_1x_2,\quad
c_0=x_1^3-x_0^2x_2,\quad
c_1=x_1^2x_3-x_0x_2^2,\quad
c_2=x_2^3-x_1x_3^2.
\]
The seemingly varied family \(q^3+c_0c_2+\lambda c_1^2\) has only weight
12 and should not consume a fresh mate search. In contrast,
\[
F_{\alpha,\beta}=q^3+\alpha c_0^2+\beta c_2^2,
\qquad\alpha\beta\ne0,
\tag{1}
\]
mixes weights 12,18,6. It is a **proposed seed**, not a certified survivor:
check integrality, normal-root restrictions and common factors first.
For an irreducible member, the extremal theorem forces corresponding
mate extremes to have factors \(c_0,c_2\). A torus degeneration cannot
exclude arbitrary mixed-weight carriers: initial equations can acquire a
common factor or extra initial generators.

## 3. Three concrete global sources and their exact limitations

| Source | What is already available | What a new test must actually do |
|---|---|---|
| Direct homogeneous pairs in \(H^0(I_C(a))\times H^0(I_C(b))\), with mixed weights | Exhaustive at each fixed degree pair; first necessary possibilities include \((5,8),(6,6),(6,8),(7,8)\) | Find a proper point of the full rank locus or prove that locus empty; generic random pairs with small thickness are controls, not serious endpoint candidates |
| Actual sextics with a prescribed second symbol, including the endpoint-four family | Complete actual-global sextic lifting formula and selected fixed-carrier mate obstruction | Vary still-unsearched global carrier parameters, solve for actual \(G\), and record contact score and residual budget; do not relabel one fixed-carrier certificate universal |
| The three Cartier singleton normalization models | Complete necessary list within explicit hypotheses; global finite-type projection sources and an exact positive membership test | Find admissible projections and actual descending powers; retain basepoints, all inverse points and full conductor, including nilpotents |

The second source comes from the conditional numerical row
\((r,s;a,b;\epsilon)=(2,12;6,16;2)\). Its actual sextics include
\[
F=(2b_1-a_0)q^2x_3^2+(b_1-a_0)qDx_2-b_2qDx_3+D^2/4+\kappa q^3,
\quad D=x_2^3-x_1x_3^2.
\tag{2}
\]
The [actual-sextic construction](2026-10-25-endpoint4-actual-sextics.md)
gives the precise symbol, nodal/torsion open and parameter normalization.
[R-0025](../results/ci_fixed_sextic_jet_rigidity.md) excludes only its
selected \(F_*\) against degree-sixteen mates. The other displayed global
members are legitimate things to test, subject to their own restrictions.

[R-0014](../results/movement_two_six_rows.md) provides the six rows
\((2,8;8,8),(2,12;6,16),(6,21;18,28),(14,42;48,49),
(15,45;50,54),(20,60;64,75)\). All inherit saturated actual first
relation and full generic binary-CI assumptions from R-0013. They are
**not** an exhaustive list of characteristic-zero STCI degrees. The
[chart review](2026-10-21-conditional-2-12-conductor-and-chart-independent-review.md)
also retains endpoint, orbit-collision, repeated-base-zero and node
boundaries; excluding one open chart does not close this row.

The third source is [R-0002](../results/cartier_singleton_lift.md):
degree-eight smooth-quadric and quadric-cone normalizations, and a
degree-sixteen plane normalization. These require a full singleton inverse
curve mapping isomorphically to \(C_0\), Cartier upstairs. The accepted
[R-0004](../results/projection_phase_reduction.md) reduces admissible
families to full-conductor torsion phases, but those phase images have
not been computed. [R-0017](../results/singleton_plane_conductor_descent.md)
already excludes a substantial two-fixed-coordinate plane subfamily;
repeating its derivatives with a different symbol is not new progress.
[R-0035](../results/normal_carrier_bounded_index_exclusion.md) prunes only
normal carriers satisfying its inherited assumptions and actual local
indices at most four. Higher-index, nonnormal and entirely-thick cases
remain distinct candidate sources.

## 4. An explicit sixteen-parameter source for the degree-eight model

On \(S=\mathbf P^1\times\mathbf P^1\), set
\(\Delta=u_0v_1-u_1v_0\), with diagonal \(c\). Choose
\[
B=(u_0^2v_0^2,\ u_0^2v_0v_1,\ u_0u_1v_1^2,\ u_1^2v_1^2),
\qquad U_i=B_i+\Delta A_i,
\tag{3}
\]
where each \(A_i\) is an arbitrary bidegree-\((1,1)\) form. This is
the **entire** affine family of four \((2,2)\) sections having these fixed
restrictions to the diagonal: the restriction exact sequence has kernel
\(\Delta H^0(\mathcal O(1,1))\), dimension four per coordinate.
It has sixteen scalar parameters. It does not impose basepoint freedom,
generic degree one, or full inverse support.

If the sections have no common zero, the map to its integral image is
finite, because their line bundle \(\mathcal O(2,2)\) is ample. Its image
has degree eight when the map is birational. A degree-\(b\) mate for an
admissible map exists exactly when
\[
\Delta^{2b}\in\operatorname{span}_k
\{U_0^{e_0}U_1^{e_1}U_2^{e_2}U_3^{e_3}:\sum e_i=b\}.
\tag{4}
\]
This is a finite **linear membership test with global coefficients**:
all terms are bidegree \((2b,2b)\) polynomials. A solution supplies the
ambient \(G_b\) itself. Necessity follows because a sole-support pullback
has divisor \(2b c\); two sections with that divisor differ by a scalar.
Sufficiency follows by pulling back its zero set through the finite map.
In particular a successful membership equation itself forces the absence
of extra inverse points over \(C_0\). Screening those points first is a
cheap rejection step, not an additional requirement on a positive equation.

For an actual search, saturate the pulled-back ideal of \(C_0\) by
\(\Delta\), retaining the two projective irrelevant ideals, to test
full inverse support. Reject basepoints first. Membership (4) is a useful
positive search even when the complete conductor phase calculation is
unavailable. Failure for finitely many \(b\) does not prove no mate in
all degrees: phases may have large torsion order.

## 5. Two completed candidate tests and the updated search

The [new quadric test](2026-10-28-stci-search-quadric-test.md) tries
\[
U=(a^2+\Delta^2,ab,dc',d^2+\lambda\Delta^2),
\quad a=u_0v_0,\ b=u_0v_1,\ c'=u_1v_0,\ d=u_1v_1.
\]
Every nonzero \(\lambda\) has two extra inverse points over
\([0:0:0:1]\), while \(\lambda=0\) has basepoints. Thus this entire
pencil is rejected **before** a mate-degree scan. The reason is concrete:
the two fixed middle coordinates vanish together along an endpoint fiber,
and a zero of the perturbed outer coordinate then maps off-diagonal points
to that endpoint. The exact verifier passed, and `search_logic_audit`
independently reconstructed both parameter cases.

The next iteration perturbed both middle coordinates as well:
\(U=(a^2+\Delta^2,ab+\Delta^2,dc'+2\Delta^2,d^2+3\Delta^2)\).
It is basepoint free, but the exact inverse scheme off \(\Delta=0\)
has dimension zero and length sixteen, again rejecting full singleton
inverse support. The [same test note](2026-10-28-stci-search-quadric-test.md)
gives the proof, script and saved Groebner basis. The independent audit
replayed the calculation and confirmed quotient-vector-space length
sixteen. Distinctness of the sixteen geometric points is not claimed.
In fact this actual finite image has no mate in any degree: its inverse
curve support has isolated off-diagonal points, whereas the pullback of
a nonzero mate section on smooth \(S\) would have a Cartier zero divisor
and therefore no isolated zero points. This is an all-degree rejection
of this candidate image, rather than a rejection of the entire source.

The next search should solve the full-inverse conditions in (3),
then use (4) at
small mate degrees or compute the conductor phases of a surviving tuple.
This is preferable to repeatedly increasing mate degree on an inadmissible
projection. In parallel, the actual-carrier jet engine should test new
members of (2) and mixed-weight seeds such as (1), keeping the last
nontrivial proper-kernel/contact level rather than only pass/fail.

**Priorities are provisional research judgments.** The best immediate
interface is an actual-global family plus an exact endpoint test and an
explicit rejection reason. A family that survives the first test earns
the next expensive calculation. A degree-specific failure should change
the parameter generator or expose an invariant covering a larger family;
it should not silently become a nonexistence theorem. The unrestricted
characteristic-zero problem remains open.
