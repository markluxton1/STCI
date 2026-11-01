# Torus residual arrangements and the meaning of absorption

**Status.** Reviewed provisional geometric deductions; independent
reconstruction is recorded below. No canonical result is promoted.

Fix an algebraically closed field k and
\[
 C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
 \qquad T:\lambda\cdot x=(x_0,\lambda x_1,\lambda^3x_2,\lambda^4x_3).
\]
The statements below hold in every characteristic unless stated otherwise.
Weights are integer characters, not integers reduced modulo the
characteristic. Write e_i for the coordinate points and L_ij for their
joining lines. The two fixed points of C are e_0 and e_3.

The question is first about arbitrary proper intersections containing C:
\[
 Y=V(F_a,G_b),\qquad [Y]=m[C]+R,\qquad ab=4m+\deg R,
\]
where R is effective and has no C component. Sole support is the further
condition R=0. These arguments organize residual geometry; they neither
construct a characteristic-zero sole-support pair nor exclude all such
pairs. Their proofs are intrinsic geometric arguments, with one explicit
Cartier-divisor counterexample; no numerical computation is needed.

## 1. Specialization can increase the marked multiplicity

Let A be a discrete valuation ring with fraction field K and residue field
k. Suppose a projective flat family of curves \(\mathcal Y\subset
\mathbf P^3_A\) contains the constant marked curve \(C_A\), and its generic
fundamental cycle is
\[
 [Y_K]=m[C_K]+R_K,
\]
with R_K effective and having no C_K component. Suppose the family has
constant degree D, as a flat projective family does. Then
\[
 [Y_k]=m[C]+\operatorname{sp}(R_K).
 \tag{1}
\]
In particular, if \([Y_k]=m'[C]+R_k\) is its decomposition with no C
component in R_k, then
\[
 m'=m+\operatorname{coeff}_C\operatorname{sp}(R_K)\ge m,
 \qquad
 \deg R_k=D-4m',
\]
and
\[
 \operatorname{sp}(R_K)=(m'-m)[C]+R_k.
 \tag{2}
\]
Thus removing the full C-primary cycle does not generally commute with
specialization.

For the proof, specialization sends an integral generic curve to the
fundamental cycle of its scheme-theoretic closure's special fiber; it is
linear and sends effective cycles to effective cycles. Flatness identifies
the specialization of the whole generic fundamental cycle with the
special fundamental cycle. Apply these facts to the displayed generic
decomposition. The required flat-cycle statement, including generic
lengths rather than just degrees, is
[Stacks, Lemma 62.4.2](https://stacks.math.columbia.edu/tag/0H4H).
Embedded zero-dimensional structure is invisible to (1); the assertion
does not identify ideals, primary components, or Hilbert polynomials from
their cycles.

This applies to the **full Hilbert-scheme T-limit** of every proper
containing pair. It is the limit of the whole ideal and its relations,
not generally the intersection of the two extreme equation forms. A
residual projective curve cannot become a cycle of points: its degree is
retained in the specialized one-cycle, possibly as extra multiplicity on
C. More generally, replace 4 by the degree of any fixed integral marked
curve preserved by the action. The multiplicity inequality itself needs
no torus action and no complete-intersection hypothesis.

## 2. All invariant irreducible curves are explicit orbit closures

For a diagonal one-dimensional torus action on projective space with
pairwise distinct integer weights w_0,...,w_n, every reduced irreducible
invariant curve D is the closure of a nonconstant orbit. Indeed, the fixed
locus consists of the coordinate points. Choose any nonfixed point of D;
its orbit has dimension one, so its irreducible closure is D.

Let I be its nonzero coordinate support, let c_i be its nonzero coordinates,
and put
\[
 w_- =\min_{i\in I}w_i,\qquad w_+=\max_{i\in I}w_i,
 \qquad g=\gcd_{i\in I}(w_i-w_-).
\]
Then D has the parametrization
\[
 D=\overline{\{[c_i z^{w_i}]_{i\in I}:z\in\mathbf G_m\}},
 \qquad
 \deg D=(w_+-w_-)/g.
 \tag{3}
\]
Its normalization is P1, and its two boundary points are the coordinate
points of minimum and maximum weight in I. To verify both assertions in
arbitrary characteristic, set d=(w_+-w_-)/g and
\(a_i=(w_i-w_-)/g\). The homogeneous monomials
\(c_i s^{d-a_i}t^{a_i}\) give a basepoint-free map from P1. The a_i
have greatest common divisor one, so the rational function field generated
by their ratios is k(t/s), by an integer Bezout relation. The map is
birational onto D and pulls back O(1) to O(d), proving (3). This argument
also handles a nonreduced finite stabilizer in positive characteristic.
Repeated weights are excluded: they give positive-dimensional fixed
linear spaces and the orbit-closure assertion would fail there.

For weights (0,1,3,4), this gives the complete list of possible reduced
irreducible supports:

| Coordinate support | Curve degree | Boundary points |
| --- | --- | --- |
| Any two indices i,j | 1; the line L_ij | e_i,e_j |
| 012 or 123 | 3 | e_0,e_2 or e_1,e_3 |
| 013 or 023 | 4 | e_0,e_3 |
| 0123 | 4 | e_0,e_3 |

For support of size at least three, the nonzero coefficients c_i matter.
In particular the full-support quartics form a two-parameter family after
dividing coefficient choices by common projective rescaling and the
one-dimensional torus. The fixed-curve list is not a finite list of
monomial ideals or isolated Hilbert points. Arbitrary generic lengths,
embedded structures and Hilbert polynomials are additional data.

Every irreducible component of an invariant reduced support is individually
invariant, since the connected torus cannot permute a finite set
nontrivially. Therefore (3) applies to every curve component of a full
T-limit, even when its ideal requires additional generators.

## 3. Endpoint attachment has exactly one possible curve exception

If D is an invariant irreducible curve different from C, then
\[
 D\cap C\subset\{e_0,e_3\}
 \quad\text{set-theoretically}.
 \tag{4}
\]
Indeed, the intersection is a finite invariant subset of C; its nonfixed
points have infinite orbits. By (3), every D whose coordinate support
contains index 0 or index 3 contains the corresponding endpoint of C.
The only possible coordinate support with neither index is {1,2}.
Consequently
\[
 D\cap C=\varnothing\quad\Longleftrightarrow\quad D=L_{12}.
 \tag{5}
\]
This classifies reduced irreducible supports, not the scheme-theoretic
attachment lengths at the endpoints.

A proper complete intersection Y is connected: its Koszul resolution,
together with the vanishing of intermediate cohomology of line bundles
on P3, gives \(H^0(Y,O_Y)=k\). Thus each residual curve component is
joined to C by a chain of irreducible curve components. Direct intersection
of every component with C does not follow from connectedness.

The full projective flat T-limit remains connected as well. Here is a
separate justification that does not assume preservation of ACMness or
unmixedness. Work over the DVR of the limit parameter and let f denote
the projective flat family. Its generic fiber is a translate of the CI,
so \(H^0(Y_K,O_{Y_K})=K\). Properness makes
\(B=H^0(\mathcal Y,O_{\mathcal Y})\) finite over A. Flatness makes
the restriction B→K injective. Since A is integrally closed and B is
integral over A, A⊂B⊂K implies B=A. Stein factorization therefore gives
connected geometric fibers; see
[Stacks, Theorem 37.53.4](https://stacks.math.columbia.edu/tag/03H0).

The limit has a linear Hilbert polynomial, so its support has dimension
one. Connectedness excludes a separate isolated point of its topological
support. Its irreducible curve-component incidence graph is therefore
connected. This does **not** exclude embedded associated points on those
curves, prove local Cohen–Macaulayness, or say that its saturated ideal is
two-generated. For an invariant limit, L12 can consequently occur only
with other curve components linking it to C; those other components meet
C at the endpoints by (4)–(5).

## 4. A proper invariant CI with a residual line disjoint from C

Put
\[
 q=x_0x_3-x_1x_2,\qquad A=x_0^2x_2-x_1^3,
 \qquad F=x_0q,\qquad G=x_3A.
\]
Both forms vanish on C; their degrees are 3 and 4 and their T-weights
are 4 and 7. The polynomial q is irreducible, q does not divide A,
and x0 divides neither x3 nor A. Hence F,G have no common factor and
define a proper invariant complete intersection of degree 12.

Its fundamental cycle is
\[
 [V(F,G)]=[C]+5[L_{23}]+[L_{02}]+[L_{01}]+[L_{12}].
 \tag{6}
\]
For a proof by effective Cartier-divisor intersections in smooth P3,
distribute the two factored divisors. All four resulting intersections
are proper, and their fundamental cycles are as follows:

| Factor intersection | Fundamental cycle |
| --- | --- |
| V(x0,x3) | L12 |
| V(x0,A) | 3 L23, since A restricted to x0=0 is −x1 cubed |
| V(q,x3) | L02 + L01, since q restricted to x3=0 is −x1 x2 |
| V(q,A) | C + 2 L23 |

For the last row use the smooth Segre quadric Q=V(q), with
\[
 (x_0,x_1,x_2,x_3)=(ac,ad,bc,bd),\qquad
 A|_Q=a^2(bc^3-ad^3).
\]
The factor a=0 is L23. The divisor bc cubed −ad cubed=0 is the
graph [a:b]=[c cubed:d cubed]; under the Segre embedding it is exactly
C, with generic multiplicity one. These identities and multiplicities
are valid in every characteristic. Divisor additivity yields (6), with
degree check 4+5+1+1+1=12.

The line L12={x0=x3=0} is disjoint from C: x0=0 meets C only at e3,
and x3=0 meets C only at e0. It connects to C through residual curves,
for example
\[
 C\;\text{—}_{e_0}\;L_{01}
 \;\text{—}_{e_1}\;L_{12}
 \;\text{—}_{e_2}\;L_{23}
 \;\text{—}_{e_3}\;C.
\]
Every curve in this arrangement is already invariant. The full ideal
(F,G) is invariant too, so both T-limits are the same CI. This rules out
a universal picture in which every residual curve is pushed onto an
endpoint of C or becomes directly attached to C. All curves here are
actual projective residual components downstairs; no exceptional vertical
curve on a blowup enters the example.

## 5. What further absorption would require

Once an embedded scheme is T-fixed, applying the same T again, in either
direction or with a reparametrized one-parameter subgroup, leaves it
unchanged. The same holds separately for each invariant curve in its
cycle. Thus another T-translation cannot absorb the residual arrangement
(6). A deformation transverse to the T-orbits, or a different permitted
group degeneration preserving the marked C, is additional geometric data.

### 5.1 Invariant quartics move and can be absorbed at cycle level

T-fixedness does not imply rigidity among invariant curves. Every invariant
reduced full-coordinate-support quartic D is a diagonal translate of C:
its orbit presentation is
\[
 D=[c_0s^4:c_1s^3t:c_2st^3:c_3t^4],\qquad c_i\in k^*.
\]
After projective rescaling and changing the orbit parameter, the unique
normalized representative is
\[
 [s^4:s^3t:\epsilon st^3:\zeta t^4],\qquad
 \epsilon=c_2c_0^2/c_1^3,\quad \zeta=c_3c_0^3/c_1^4.
 \tag{7}
\]
Thus these reduced orbit quartics form an irreducible two-dimensional
torus family. More intrinsically, the projective diagonal torus has
dimension three and its stabilizer of C is exactly the given
one-dimensional T; their quotient is a two-dimensional torus. These are
statements about the family of reduced embedded curves, not arbitrary
nonreduced fixed Hilbert points.

There is an explicit flat interpolation to any such D in every
characteristic. Set
\[
 c_i(u)=1+u(c_i-1),\qquad
 U=\mathbf A^1\setminus\bigcup_i V(c_i(u)).
\]
Only finitely many points are removed, and both 0 and 1 belong to U.
The diagonal automorphisms \(\operatorname{diag}(c_i(u))\) send the
constant family C×U to a flat family of invariant reduced curves D_u,
with D_0=C and D_1=D. If D differs from C, generic D_u differs from C:
the equality locus is closed by separatedness of the Hilbert scheme and
does not contain 1. Consequently the effective cycle family
\[
 m[C]+[D_u]\quad\rightsquigarrow\quad(m+1)[C]
 \qquad(u\to0)
 \tag{8}
\]
has genuine cycle-level absorption. This follows equally from the sum of
the constant relative cycle m[C×U] and the flat relative cycle [D_u];
it does not claim that their scheme-theoretic union is flat at 0 or
has any prescribed complete-intersection Hilbert polynomial.

The diagonal interpolation commutes with T but generally does not
preserve C at intermediate parameters. In (8) the marked C remains fixed
as a separate summand; D_u alone is moved. Extending this cycle motion
to the whole embedded intersection, with its generic lengths, endpoint
structure, fixed Hilbert polynomial and two actual homogeneous equation
generators, is an additional realization problem. In particular an
invariant quartic residual is not rigid at cycle level, while its
absorption inside a prescribed complete intersection is not supplied by
(8).

In any actual flat family preserving C, absorption is precisely the
appearance of a C component in the specialized residual cycle, as in
(2). Its degree transfer is a multiple of 4. A degree-one curve alone
or a degree-three curve alone cannot flatly specialize to a positive
multiple of C; collections of residual components may specialize
together, and residual degree need not stay constant after extracting
the full marked multiplicity. These
necessary cycle conditions provide neither the actual deformation nor
its global equation generators.

The existing [marked absorption account](marked_deformation_and_absorption.md)
constructs partial transfer by actual containing pairs and distinguishes
a flat lower marked witness from a generally nonflat full primary
component. The [toric sextic account](toric_sextic_residuals_and_limits.md#32-absorption-changes-the-decomposition-into-marked-and-residual-cycles)
also gives actual torus transfer of residual quartics onto C while leaving
a residual line. These examples do not establish iteration to sole support.

For a bounded degree pair the useful boundary object is consequently the
full invariant ideal together with its orbit-curve arrangement, generic
lengths, endpoint and possible embedded structure, and Hilbert polynomial.
The moving ideal must separately belong to the actual two-equation
incidence; see [surface-pair VGIT and the full-limit graph](vgit_surface_pairs_and_full_limits.md).
The elementary support classification above covers arbitrary containing
pairs' full T-limits. It supplies no classification of their nonreduced
fixed ideals or of deformations that absorb the entire residual cycle.

## Evidence, review and remaining scope

The new claims are (1)–(5), the connectedness argument with its stated
qualifications, the proper-CI counterexample (6), and the invariant-quartic
family and cycle-level absorption (7)–(8). Their proofs are
written above. The specialization and connectedness inputs are the linked
primary Stacks references; no unverified computational reduction is used.
A bounded independent check reconstructed the factor-intersection and
Segre calculations for (6), including the characteristic-free scope;
the final collected multiplicities were also checked directly against the
four summands. Independent reconstruction on 2026-11-01 then accepted
the specialization, orbit-degree, unique L12 exception, flat-limit
connectedness and counterexample arguments in every characteristic.
It also reconstructed the two-parameter diagonal family and its cycle
absorption, preserving the distinction from a prescribed embedded CI
family and keeping the marked curve separate. No canonical theorem scope
or status has changed. The unresolved step is actual residual-absorption incidence in
families of global equations, including whether sole support occurs in
characteristic zero.
