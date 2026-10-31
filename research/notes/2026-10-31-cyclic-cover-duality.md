# The different and the contact identity for an arbitrary supported pair

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
see the [state-specific audit](2026-10-31-cyclic-cover-duality-audit.md).
No canonical promotion or unrestricted STCI conclusion.

Work over an algebraically closed field \(k\) of characteristic zero. Put

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\quad p_0=[1:0:0:0],\quad p_\infty=[0:0:0:1].
\]

Let \(Z=V(F_a,G_b)\) be a proper complete intersection with

\[
Z_{\mathrm{red}}=C,\qquad m=ab/4,\qquad d=a+b.
\tag{1}
\]

The statements below concern **every** such pair. Neither a smooth carrier,
a saturated first normal relation, normal flatness, nor a retraction
\(Z\to C\) is assumed.

## 1. Input, sources, and the distinction from the existing socle budget

The [finite-cover construction](2026-10-30-fixed-surface-configuration.md),
Sections 4–6, gives a finite flat map

\[
\pi:Z\longrightarrow B=\mathbf P^1,
\qquad [x]\longmapsto[x_0:x_3],
\]

whose restriction \(f:C\to B\) is \([s:t]\mapsto[s^4:t^4]\).
The [promoted socle theorem R-0032](../results/full_conormal_socle_budget.md)
already identifies

\[
\mathcal S:=\operatorname{Ann}_{\mathcal O_Z}
  (\mathcal I_C\mathcal O_Z)
\simeq\omega_C\otimes\omega_Z^{-1}|_C
\simeq\mathcal O_C(14-4d).
\tag{2}
\]

Degrees in \(\mathcal O_C(r)\) in this note mean degrees on the
normalization \(C\simeq\mathbf P^1\); thus the ambient twist
\(\mathcal O_Z(1)|_C\) is \(\mathcal O_C(4)\).

The relative Jacobian already appears as an actual socle generator in
the [pointwise conductor audit](2026-10-14-generalization-pointwise-conductor-socle-independent-audit.md),
Section 3, and the [index compatibility proof](2026-10-14-generalization-index12-filtered-compatibility.md),
Section 3.2. Their finite-free/special-fiber argument does not require
normal flatness. That generator fact and the degree of (2) are reused,
not new obstructions. The additional application here compares **all**
ambient Jacobians, obtains their exact ramification sections, and derives
membership of the actual Poisson bracket in the two-generator ideal.

The literature was checked before selecting this mechanism. The necessary
finite-duality inputs are the trace element, the complete-intersection
Jacobian formula, and its canonical determinant-of-cotangent-complex
interpretation: [Stacks, Sections 49.4](https://stacks.math.columbia.edu/tag/0BSY),
[49.12, especially Lemma 49.12.4](https://stacks.math.columbia.edu/tag/0BWB),
and [49.13, the Tate map](https://stacks.math.columbia.edu/tag/0FKB).
The projection-change proof below uses the already established
relative-Jacobian socle generator and an algebraic parameter argument;
it does not require comparison of chosen Tate frames for two different
projections. The absolute class map is described in
[Stacks, Lemma 48.29.2](https://stacks.math.columbia.edu/tag/0E9Z), but its
exact multiplicity normalization is not asserted or needed here.

For contact geometry, [Buczyński, *Properties of Legendrian subvarieties
of projective space*](https://arxiv.org/pdf/math/0503528), Sections 3–5,
provides the rational monomial examples, the contact/conormal dictionary,
and the Poisson characterization of a **reduced** Legendrian ideal.
Theorem 4.9 concerns irreducible normal complete intersections. It cannot
be applied to the nonreduced \(Z\) in (1).

## 2. The local Jacobian lemma, including a change of projection

We use the following characteristic-zero local fact.

**Lemma.** Let a complete-intersection curve \(W=(h_1,h_2)\) in a smooth
threefold have smooth reduced support \(D\) and generic multiplicity \(m\).
Choose algebraic étale coordinates \((z,u,v)\) on a neighborhood, with
\(D=(u,v)\) and \(z|_D\) étale over the affine line. Write

\[
J_{uv}=h_{1,u}h_{2,v}-h_{1,v}h_{2,u},
\]

and define \(J_{zu},J_{zv}\) similarly. Then in \(\mathcal O_W\),

\[
J_{zu}=J_{zv}=0,
\qquad (J_{uv})=\operatorname{Ann}_{\mathcal O_W}(u,v).
\tag{3}
\]

The same identities consequently hold in completed local coordinates.

**Proof.** First recall the relative-Jacobian socle-generator fact from
the [pointwise conductor audit](2026-10-14-generalization-pointwise-conductor-socle-independent-audit.md),
Section 3. At every closed point of \(D\), complete the local rings.
The completed ring \(A\) of \(W\) is finite free of rank \(m\) over
\(R=k[[z-z(p)]]\): its reduction is \(R\), its nilradical is nilpotent,
and the parameter is a nonzerodivisor by Cohen–Macaulay purity.
The generic Artinian complete-intersection Jacobian theorem puts
\(j=J_{uv}\) in its socle after inverting the parameter. Torsion freeness
puts \(j\) in the actual relative socle \(\Sigma=\operatorname{Ann}_A(u,v)\).

The rank-one \(R\)-module \(\Sigma\) is saturated in \(A\): if a parameter
multiple of an element annihilates \(u,v\), so does the element.
Consequently \(\Sigma/\mathfrak m_R\Sigma\) injects into
\(A/\mathfrak m_RA\). The latter is an Artinian complete intersection of
length \(m\), and its Jacobian is a nonzero socle generator in
characteristic zero. Nakayama's lemma now gives \(\Sigma=Rj\).
Faithful flatness of completion gives the same generator statement in
the algebraic local ring. This argument applies to every local
projection whose restriction to \(D\) is étale. The Artinian Jacobian
input is stated for formal, not necessarily homogeneous equations in
[Eisenbud–Ulrich, *Duality and socle generators for residual
intersections*, Theorem 8.5](https://arxiv.org/pdf/1309.2050).

Return to the **algebraic neighborhood**, so that the following argument
ranges over all its closed points. Replacing \(z\) by \(z'=z+u\)
preserves its restriction to \(D\). The relative Jacobian at fixed \(z'\)
is \(j-J_{zv}\); it too generates the socle line \(\mathcal S_W\).
Thus \(J_{zv}\) belongs to \(\mathcal S_W\). Since \(j\) generates that
line, write \(J_{zv}=g j\) for a regular function \(g\) on \(D\).

Suppose \(g(p)\ne0\) at a closed point \(p\), and choose the constant
\(\lambda=1/g(p)\in k\). The parameter \(z_\lambda=z+\lambda u\)
still restricts to \(z\) on \(D\), but its relative Jacobian is

\[
j_\lambda=j-\lambda J_{zv}=(1-\lambda g)j.
\tag{4}
\]

At \(p\), this fails to generate the socle line, contradicting the
generator statement. Therefore \(g\) vanishes at every closed point of
the reduced finite-type curve \(D\), and \(g=0\). Hence \(J_{zv}=0\).

The substitutions \(z+\lambda v\) give relative Jacobians
\(j+\lambda J_{zu}\). The same argument gives \(J_{zu}=0\), completing
(3). No normal-filtration flatness or global retraction enters the
proof. \(\square\)

Working on an algebraic neighborhood matters: vanishing at the sole
closed point of a completed local curve would not show that a formal
power series is zero. Completion is used above only to establish the
relative-socle generator at each algebraic closed point.

This comparison does not assert an exact multiplicity-normalized
fundamental-class formula. The stronger formula is unnecessary here;
(3) determines the direction and nonvanishing of the Jacobian tuple
needed below.

## 3. All six ambient minors recover the tangent sextics

Set

\[
M_{ij}=F_{x_i}G_{x_j}-F_{x_j}G_{x_i}\quad(0\le i<j\le3).
\]

**Proposition.** Their classes are sections of
\(\mathcal S(d-2)\simeq\mathcal O_C(6)\). For one choice of the scalar
in this line-bundle isomorphism, their tuple is a common nonzero scalar
multiple of

\[
(M_{01},M_{02},M_{03},M_{12},M_{13},M_{23})
\longleftrightarrow
(t^6,-3s^2t^4,2s^3t^3,4s^3t^3,-3s^4t^2,s^6).
\tag{6}
\]

In particular their ideal sheaf in \(\mathcal O_Z\) is precisely
\(\mathcal S\), and

\[
M_{12}-2M_{03}\in(F,G)
\quad\text{in }k[x_0,x_1,x_2,x_3].
\tag{7}
\]

**Proof.** The local lemma says that the Jacobian tuple is a nowhere
vanishing socle multiple of the tangent direction of the reduced curve.
In homogeneous coordinates, Euler's identities give
\(\sum x_iF_{x_i}=aF\) and \(\sum x_iG_{x_i}=bG\). Hence modulo
\((F,G)\), the exterior product of the two gradients corresponds, by
complementary minors, to the tangent two-plane of the affine cone.

For \(\phi(s,t)=(s^4,s^3t,st^3,t^4)\), direct differentiation gives the
six tangent Plücker coordinates, after division by the common scalar
four,

\[
(s^6,3s^4t^2,4s^3t^3,2s^3t^3,3s^2t^4,t^6).
\]

Taking complementary minors with the ambient volume orientation
\(dx_0\wedge dx_1\wedge dx_2\wedge dx_3\) gives the tuple in (6).
The twist is exact:
\(\mathcal S(d-2)=\mathcal O_C(14-4d+4d-8)=\mathcal O_C(6)\).
The local lemma says that the actual tuple and this tangent tuple have
the same pointwise ratios and no common zero. They therefore differ by
an automorphism of \(\mathcal O_C(6)\), a common nonzero constant.
The first and last displayed sections have no common zero, so the minors
generate the socle ideal sheaf. Relation (7) holds as a sheaf relation.
The homogeneous complete-intersection ideal \((F,G)\) is saturated, so
it holds in the homogeneous polynomial ring as stated. \(\square\)

Thus there exist homogeneous polynomials \(A_{b-2},B_{a-2}\) with

\[
M_{12}-2M_{03}=A_{b-2}F+B_{a-2}G.
\tag{8}
\]

This retains the actual defining ideal, rather than asserting only
vanishing on \(C\).

## 4. The precise different of the cyclic projection

For the map \(\pi\), the relative Jacobian is \(M_{12}\). Formula (6)
therefore gives its exact zero divisor **as a section of the socle line
with its indicated twist**:

\[
\operatorname{div}_C(M_{12})=3p_0+3p_\infty=:R_f.
\tag{9}
\]

Equivalently, its different ideal is

\[
\mathfrak D_\pi=\mathcal S(-R_f)\subset\mathcal O_Z.
\tag{10}
\]

This also follows directly from
\(\operatorname{Tr}_{Z/B}=m\operatorname{Tr}_{C/B}\circ
(\mathcal O_Z\twoheadrightarrow\mathcal O_C)\) and the relative
duality injection \(\omega_{C/B}\hookrightarrow\omega_{Z/B}\).
The reduced trace has ramification divisor \(R_f\), since locally the
cover is \(z\mapsto z^4\), with derivative \(4z^3\).

The different in (10) is generally a nilpotent ideal on \(Z\). It is
**not** an effective Cartier ramification divisor on the nonreduced
curve. Formula (9) refers to a nonzero section on its smooth support.
In particular, it does not say that \(\pi\) is étale away from the two
endpoints: only its reduction is étale there.

Because \(\mathcal S\) is a line bundle on \(C\) and multiplication by a
nonzero section on \(C\) is injective, one also obtains

\[
\operatorname{Ann}_{\mathcal O_Z}(M_{12})
=\mathcal I_C\mathcal O_Z,
\qquad (F,G):M_{12}=I_C.
\tag{11}
\]

The second equality uses saturation as in (7).

## 5. Geometric meaning and the remaining bridge

The affine cone over \(C\) is Lagrangian for

\[
\omega=dx_0\wedge dx_3-2\,dx_1\wedge dx_2.
\]

Indeed its two tangent vectors have
\(W_{03}-2W_{12}=0\). Up to an overall sign, the associated Poisson
bracket is

\[
\{H,K\}=H_{x_0}K_{x_3}-H_{x_3}K_{x_0}
-\tfrac12(H_{x_1}K_{x_2}-H_{x_2}K_{x_1}).
\]

Equation (7) is exactly

\[
\{F,G\}\in(F,G),\qquad
\{(F,G),(F,G)\}\subset(F,G).
\tag{12}
\]

So any hypothetical pair defines an involutive complete-intersection
**scheme**, not just a reduced Legendrian support. The stronger membership
in (12) follows from the actual-socle and projection-change calculation,
not from the usual reduced-ideal Poisson criterion alone.

This is a uniform compatibility condition on the arbitrary homogeneous
equations. It can reject a containing pair whose bracket is nonzero in
its quotient, and (11) identifies its reduction through an actual
Jacobian colon. Neither condition constructs a pair or proves that all
possible pairs fail. A new obstruction would have to show that these
identities, the actual two-generator presentation, and the quartic's
global geometry are incompatible; that implication is not established.

There is a useful control against a general nonexistence inference from
contact geometry. The twisted cubic
\(T=[s^3:s^2t:st^2:t^3]\) is the reduced support of the proper pair

\[
F=x_0x_2-x_1^2,\qquad
G=x_2^3-2x_1x_2x_3+x_0x_3^2.
\]

On \(x_0=1\), elimination gives
\(x_2=x_1^2\) and \(G=(x_3-x_1^3)^2\); on \(x_0=0\), the sole
common point is \([0:0:0:1]\). Thus this is an actual supported
complete intersection, generically double on \(T\).
The cubic is Legendrian for
\(dx_0\wedge dx_3-3\,dx_1\wedge dx_2\), and direct differentiation gives

\[
M_{12}-3M_{03}=-4x_3F.
\]

It satisfies the analogous exact involutivity identity. Consequently
involutivity alone cannot exclude supported complete intersections on
all smooth nonlinear Legendrian curves; further use of the fixed
quartic is essential.

For orientation, \(q=x_0x_3-x_1x_2\) is a Hamiltonian for the existing
torus: \(\{q,-\}\) has coordinate weights
\((-1,-\tfrac12,\tfrac12,1)\), proportional to
\((0,1,3,4)-(2,2,2,2)\). But \(q\) lies only in
\(\sqrt{(F,G)}\), so (12) does **not** imply
\(\{q,(F,G)\}\subset(F,G)\), torus invariance, or an equivariant
algebra splitting.

The earlier missing-coordinate obstruction and the existing socle-degree
budget remain unchanged. The unique lifting of the étale reduced algebra
over \(B\setminus\{0,\infty\}\) is not an extension over the endpoints;
(9) is compatible with such failure and does not provide a global
retraction. The unrestricted characteristic-zero STCI question remains
open.

## 6. Verification boundary

No computational reduction was substituted for a completed calculation;
no inherited proof or certificate was rerun. The displayed sextics are
obtained by direct differentiation. Independent review identified a source
compatibility gap in the original absolute trace-normalization argument.
The revised algebraic-neighborhood proof in Section 2 removes that
dependency and the unnecessary stronger assertion. The audit reconstructs
the revised local proof, homogeneous complementary minors, signs and
twists, the nilpotent different, the colon equality, and the twisted-cubic
control. No material finding remains unresolved in the revised statements.
The discarded stronger normalization assertion is outside that coverage.

The [tropical and characteristic comparison](2026-10-31-tropical-model-characteristic.md)
explains two separate changes in positive characteristic: inseparability
of the reduced fourfold projection in characteristic two, and vanishing
of the multiplicity-weighted trace when the characteristic divides m,
including examples where the reduced cover remains tame.
