# The intrinsic quadric spectrum: Segre, normal directions, contact geometry, and opposite projections

**Status:** geometric comparison of established sources and elementary specializations, **not** a universal first-moment theorem. Characteristic zero. This note is subordinate to [the universal-moment corpus synthesis](universal_first_moment_corpus_review.md), [the exact first-moment theorem](chow_arrangement_moments.md), and [the actual spectral equation](chow_realization_moment_separation.md#11-the-two-extreme-mixed-coefficients-of-the-quadric-spectrum-equation).

## 1. The original embedding is induced from the quadric

Let \(Q_1=V(x_1x_2-x_0x_3)=\mathbf P^1_A\times\mathbf P^1_B\)
with the Segre embedding \(\mathcal O_Q(1,1)\). The graph
\[
 [s:t]\longmapsto([s^3:t^3],[s:t])
\]
is a divisor \(C\in|\mathcal O_Q(1,3)|\); the ambient system is the
restriction of the Segre polarization. The complete system
\(|\mathcal O_Q(1,3)|\) has projective dimension seven; the torus
translates form a smaller special family. The two totally ramified
points of the cubic graph are \(p_0,p_\infty\) and determine the two
hyperosculating planes.

Put \(A=x_1x_2,B=x_0x_3\). Every translated curve
\(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\) lies on precisely the smooth
quadric \(Q_q=V(A-qB)\) where \(q=u/v\). On a fixed \(Q_q\),
\[
  [x_0:x_1:x_2:x_3]=[ac:ad:bc:bd/q],\quad
  C_{u,u/q}:\quad [a:b]=[s^3:u t^3],\ [c:d]=[s:t].
\]
Thus varying \(u\) at fixed \(q\) changes the cubic graph inside a
fixed quadric, and varying \(q\) changes the containing quadric.

The normal exact sequence on \(C\) is
\[
  0\to N_{C/Q}=\mathcal O_{\mathbf P^1}(6)
   \to N_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(7)^2
   \to\mathcal O_{\mathbf P^1}(8)\to0.
\]
For \(u=v=1+\epsilon\alpha\), the inside-quadric first-order
variation is \(s^3t^3\) (up to scalar), a section of \(\mathcal O(6)\)
with divisor \(3p_0+3p_\infty\). More generally, if
\(u=1+\epsilon\alpha,v=1+\epsilon\beta\), the image of the transverse
normal variation in \(\mathcal O(8)\) equals
\((\alpha-\beta)s^4t^4\): differentiating
\(A-(u/v)B\) gives this directly. The *different* vanishing orders
of these two normal sections are consequences of the geometry
of the graph and containing quadric. They do **not** by themselves
force the global first moment of an arbitrary cycle to vanish.

## 2. The spectral form is the unique divisor equation on the quadric pencil

For a cycle \(\sigma=\sum_i n_i[C_{u_i,v_i}]\), let
\(D_\sigma=\sum_i n_i[q_i]\) on the pencil parameter line, with
\(q_i=u_i/v_i\). Its Cartier equation in the distinguished
\((A,B)\) coordinates is
\[
 H_\sigma(A,B)=\prod_i(A-q_iB)^{n_i}.
\]
It is unique up to scalar as an equation of this **effective divisor**;
the coefficient of \(A^m\) fixes the scalar on the torus chart.
This is a projection of the **cycle**: it forgets the one-dimensional
movement \(u\) of each translated curve inside its smooth \(Q_q\).
It is not the full Chow form of the cycle on \(\operatorname{Gr}(2,4)\),
which does retain the individual curves.

The actual-ideal membership
\[
  H_\sigma(x_1x_2,x_0x_3)\in(F_a,G_b)
\]
for every proper CI with that entire translated cycle follows from
generic local Artin lengths and Cohen--Macaulay unmixedness
([PR #173 proof](chow_realization_moment_separation.md#11-the-two-extreme-mixed-coefficients-of-the-quadric-spectrum-equation)).
It does not assert that \(H_\sigma\) is the **unique element** of
the homogeneous ideal in degree \(2m\), nor the minimal annihilator
of \(A/B\) on the nilpotent structure. In a finite local algebra of
length \(n\), the nilpotence index of an individual normal coordinate
can be strictly smaller than \(n\). The full characteristic
polynomial, as a relative rank-\(4m\) algebra, is \(H_\sigma(T,1)^4\);
its first coefficient gives the multiplicity-weighted trace.

There is also a classical geometric pushforward description.
Blow up the base ideal \((A,B)\) of the rational pencil map
\([A:B]:\mathbf P^3\dashrightarrow\mathbf P^1\) (Stacks,
[blowup universal property](https://stacks.math.columbia.edu/tag/0806)).
The resolved map sends the strict transform of each \(C_{u,v}\)
to the point \(q\). A generic pulled-back hyperplane cuts the
strict transform in four points; pushing the resulting zero-cycle
to the pencil gives \(4\sum_i n_i[q_i]=4D_\sigma\).
This is a **cycle-level** construction, not a scheme-level
identification with the actual nonreduced CI. Ordinary rational
equivalence of zero-cycles on \(\mathbf P^1\) retains only the
degree and therefore does not by itself detect \(M_1\).

## 3. The second projection has degree two after blowup

The disjoint center \(L_+=V(x_0,x_3)\) gives the basepoint-free
projection \([x_0:x_3]\), restricting to
\([s^4:v t^4]\) of degree four on \(C_{u,v}\). It induces a finite
flat degree-\(ab=4m\) cover of a Chow-matched proper CI, with
\(\operatorname{Tr}(x_1x_2)=4M_1x_0x_3\).

The opposite center \(L_-=V(x_1,x_2)\) meets every translate at
\(p_0,p_\infty\). Its rational projection restricts to
\[
 [x_1:x_2]=[s^3t:u st^3]=[s^2:u t^2]
\]
after canceling the base divisor \(p_0+p_\infty\).
The blowup \(\operatorname{Bl}_{L_-}\mathbf P^3\) resolves the ambient
map; each strict-transformed curve maps with degree **two**.
The contrasting degrees \(4\) and \(2\) are exactly the
quadruple versus \(3+1\) endpoint contact of the two pairs
of distinguished planes. For a thick CI, identifying the full
strict-transformed algebra and exceptional corrections is an
additional theorem, not automatic from this reduced-curve
calculation. The opposite first spectral coefficient need not
vanish: [PR #173](chow_realization_moment_separation.md#11-the-two-extreme-mixed-coefficients-of-the-quadric-spectrum-equation)
already gives invariant \((4,4)\) CIs with nonzero reciprocal trace.
Do not propose symmetric moment vanishing.

## 4. The same q parameter also selects a contact structure

The [existing Jacobian/Hamiltonian work on main](contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity)
shows that the affine cone over \(C=C_{1,1}\) is Lagrangian for
\[
 \omega_1=dx_0\wedge dx_3-2\,dx_1\wedge dx_2
\]
and, for a hypothetical CI supported only on \(C\),
the **actual ideal** satisfies the associated Poisson-bracket
involutivity, under the source's hypotheses.

For each nonzero \(q\), use the nondegenerate alternating form
\[
 \boxed{\omega_q=dx_0\wedge dx_3-\frac{2}{q}dx_1\wedge dx_2.}
\]
The affine cone over \(C_{u,v}\) is Lagrangian for \(\omega_q\)
**exactly when \(q=u/v\)**: the two tangent pairings are
\(16v s^3t^3\) and \(8u s^3t^3\).
In the Segre graph chart of \(Q_q\), a general degree-three graph
has \([a:b]\) and \(r=t/s\). Its Legendrian condition
\(\omega_q(x,x')=0\) is
\[
 r(a'b-ab')+3ab=0.
\]
Putting \(f=b/a\) reduces it to \(r f'=3f\). In characteristic
zero its nonconstant degree-three solutions are precisely
\(f=\lambda r^3\). **Within the marked graph locus on a fixed
\(Q_q\), the translated curves are exactly the Legendrian
graphs for \(\omega_q\)**. This is an elementary specialization,
not a new classification: Nikita Kalinin,
[*Legendrian curves in \(\mathbf{CP}^3\): cubics and curves on a
quadric surface*](https://arxiv.org/abs/1607.07486v2),
Theorem 4.3 in both arXiv v2 and the printed
2018 paper, classifies algebraic Legendrian curves on smooth
quadrics over \(\mathbf C\). Our calculation identifies the
specified marked torus subfamily within that established
picture.

Thus the projected coordinate \(q\) records **both a quadric and
an associated contact form**. Unlike an arbitrary \((1,3)\) member,
our torus translate is Legendrian for that form. The spectral
divisor is also a multiset of this marked pair of geometric
structures. The Hamiltonian/socle identity for sole support is a
substantive existing comparison to revisit at the common
six-layer trace, but no proof currently derives \(M_1=0\)
from the contact structure or the Poisson ideal.

## The computed Jacobian/residue bridge

The [companion first-jet proof](spectral_jacobian_first_jet_bridge.md)
identifies the second quotient character
\(\eta=x_0x_2^2/(x_1^2x_3)\) with the cubic pencil
\(R_\eta=V(x_0x_2^2-\eta x_1^2x_3)\), and proves
\(Q_\xi\cap R_\eta=C_{\eta/\xi,\eta/\xi^2}+L_{01}+L_{23}\)
as actual intersection cycles. For every proper translated-cycle
CI, its Jacobian minors satisfy
\(x_1x_2M_{12}-2x_0x_3M_{03}\in(F,G)\), without
requiring invariance. The exact Grothendieck residue calculation then
gives \(2M_1=\operatorname{Res}_{f_0,g_0}(p s-q r)\),
where the four polynomials are the two actual first normal jets
of \(F,G\) along the disjoint line \(L=V(x_0,x_3)\).
Graded Gorenstein duality makes this a perfect alternating pairing
on \((k[x_1,x_2]/(f_0,g_0))_{a-1}\oplus
(k[x_1,x_2]/(f_0,g_0))_{b-1}\).
This connects the spectral trace to the existing Jacobian/socle theorem
in a way that removes the higher projection-line layers **after**
the translated support hypothesis is imposed. It does not prove
the two first jets are isotropic for all actual CI realizations.

## The chosen bridge, not a new agenda

Compare (i) the canonical spectral equation and its actual Koszul
membership, (ii) the six-layer trace of the basepoint-free projection,
and (iii) the **existing** Jacobian/Poisson identity on the affine cone.
A useful next lemma must show a specific identity of actual
equations implying that mixed trace is zero, and must survive the
non-invariant exceptional quartic control and the nonzero
reciprocal-moment examples. Resolving the opposite line is useful
as an explanatory contact/endpoint comparison, not presently a
new independent obstruction. No STCI claim follows.
