# Degenerating a (4,4) curve: cycles, gluing, and nilpotent genus

Date: 2026-10-26. Status: exploratory synthesis and new elementary deductions; independent review is recorded in the [audit](2026-10-26-44-degeneration-genus-budgets-audit.md). No canonical promotion.

## 1. Question and scope

What can a smooth complete-intersection curve of type (4,4) in projective three-space degenerate into, and what does the fixed Hilbert polynomial actually constrain? First allow all proper pairs; then retain the marked curve
\[
C=[s^4:s^3t:st^3:t^4].
\]
The field is algebraically closed of characteristic zero; statements about ordinary topology use the associated complex curve. A proper pair has no common surface component. Throughout, a cycle means the fundamental effective one-cycle of an actual scheme, not the full scheme structure.

Completion of this move means deriving the genus and componentwise boundary constraints, giving actual smoothable examples at several extremes, and isolating the additional information needed when a component acquires multiplicity. It does not mean classifying all degree partitions or all embedded limits.

Promoted inputs are [R0021](../results/quartic_mu4_degeneration.md), for the prescribed four-quartic configuration, and the precise scope of [R0022](../results/quartic_44_filtered_exclusion.md), for the already established fixed-curve (4,4) exclusion. Neither exclusion proof is rerun. The [previous cycle notebook](2026-10-25-ci-cycle-geometry-notebook.md) and [conductor/topology note](2026-10-25-ci-cycle-conductor-topology.md), with their linked audits, supply reviewed but unpromoted geometry. The smooth-carrier dichotomy in section 7 is a new elementary deduction, independently reconstructed during this move.

## 2. What is conserved

The Koszul resolution of a proper pair of degrees (a,b) gives
\[
P_W(n)=abn-\frac{ab(a+b-4)}2,\qquad
p_a(W)=1+\frac{ab(a+b-4)}2.
\]
Adjunction gives the additional, stronger constraint
\[
\omega_W\simeq\mathcal O_W(a+b-4).
\]
These assertions hold for nonreduced complete intersections too. Such a curve is pure, Cohen--Macaulay, and Gorenstein; the Koszul resolution also gives \(H^0(\mathcal O_W)=k\), hence connectedness and \(h^1(\mathcal O_W)=p_a(W)\).

For (4,4), these become
\[
\deg W=16,\quad P_W(n)=16n-32,\quad p_a(W)=33,
\quad\omega_W=\mathcal O_W(4).
\]
The open locus of proper pencils in \(\operatorname{Gr}(2,H^0(\mathcal O_{\mathbf P^3}(4)))\) carries a flat universal complete-intersection family, and smooth members form a dense open subset. Every proper pair discussed here can therefore be smoothed by a general perturbation. A specialization acquiring a common surface leaves this open locus: its two specialized equations need not describe the flat curve limit.

For general flat projective families, constancy of Euler characteristics of twists follows from [Stacks, Lemma 36.32.2](https://stacks.math.columbia.edu/tag/0B9T), applied to the structure sheaf and its twists. This is coherent Euler characteristic, not ordinary topological Euler characteristic. A cycle alone does not have a specified arithmetic genus: the gluing and nilpotent structure are essential.

## 3. The reduced genus budget and the graph

Let W be reduced, with r integral components, normalization genera \(g_i\), and local delta invariants \(\delta_p\). The normalization exact sequence gives
\[
33=\sum_i g_i+\delta(W)-r+1,
\qquad \delta(W)=\sum_p\delta_p.
\]
Thus \(\delta=32+r-\sum g_i\). For definitions and finite normalization quotients see [Stacks, delta invariant](https://stacks.math.columbia.edu/tag/0C3Q).

For nodal curves this is the familiar graph identity
\[
33=\sum_i g_i+b_1(\Gamma).
\]
For arbitrary reduced curves, use the bipartite graph of normalized components and singular points, with an edge for each local branch. If \(r_p\) is the number of branches at p, put
\[
b=\sum_p(r_p-1)-r+1,\qquad
u=\delta-\sum_p(r_p-1).
\]
Then
\[
33=\sum_i g_i+b+u.
\]
Here b counts graph loops, while u measures gluing beyond identifying the branch origins. In characteristic zero these are the abelian, toric, and unipotent dimensions of the generalized Jacobian, as explained in the earlier conductor/topology note. In particular, tangencies can contribute arithmetic genus without adding the same number of topological loops.

For the complex reduced curve,
\[
b_1(W)=2\sum_i g_i+b,\quad b_2(W)=r,
\quad\chi_{\rm top}(W)=2r-2\sum_i g_i-\sum_p(r_p-1).
\]
The smooth fiber has Euler characteristic -64. The local complete-intersection Milnor formula
\(\mu_p=2\delta_p-r_p+1\) gives
\[
\chi_{\rm top}(W)=-64+\sum_p\mu_p.
\]
The local formula is [Dimca--Greuel, Theorem 2.1(1), p. 115](https://www.journalofsing.org/volume18/dimca-greuel.pdf), attributing it to Buchweitz--Greuel. These reduced isolated-singularity formulas do not apply by simply reducing a generically nonreduced fiber.

## 4. Actual reduced configurations

### Sixteen lines: all genus in graph loops

Choose eight planes \(A_i,B_j\), \(1\le i,j\le4\), in general linear position and set
\[
F=\prod_i A_i,\qquad G=\prod_j B_j.
\]
The sixteen lines \(L_{ij}=V(A_i,B_j)\) meet precisely when they share a row or column. General position rules out fourfold plane intersections and hence triple points of the curve. There are
\[
4\binom42+4\binom42=48
\]
ordinary nodes, so the rook graph has \(48-16+1=33\) loops. Each line has six attachments. This is a complete intersection with genus allocation \((\sum g_i,b,u)=(0,33,0)\).

It also gives the sharp upper bound for total delta among reduced (4,4) curves:
\[
\delta=32+r-\sum_i g_i\le48,
\]
since \(r\le16\). This comparison allows all proper pairs, without retaining the fixed quartic.

### Four plane quartics

Keep F a product of four general planes but choose G a general smooth quartic surface. Each plane section is smooth of genus three. Every pair meets at four points, giving twenty-four nodes in total. Thus
\[
33=4\cdot3+24-4+1=12+21.
\]

### Retaining the fixed rational quartic

The reviewed provisional notebook supplies a general member
\[
W=C\cup D,\qquad \deg D=12,\quad g(D)=16,
\quad\operatorname{length}(C\cap D)=18,
\]
with D smooth and eighteen ordinary attachments. The allocation is \((16,17,0)\).

At the promoted prescribed pair
\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3,
\]
there are four smooth rational quartics, with pairwise contact three at each of two endpoints. Each endpoint has four branches, delta eighteen, and Milnor number thirty-three. Therefore
\[
33=0+36-4+1=0+3+30.
\]
Its ordinary Betti numbers are \((b_0,b_1,b_2)=(1,3,4)\), and its Euler characteristic is two. The two endpoints account for the change \(-64+66=2\) under smoothing. Its delta thirty-six is not maximal, even in the marked-C class: the earlier notebook contains an independently checked eight-rational-component example with delta forty.

## 5. Adjunction gives a constraint on each component

On the normalization of a component of degree e and genus g, with map \(\nu_i:\widetilde C_i\to W\), its conductor divisor \(B_i\) satisfies
\[
\nu_i^*\omega_W=\omega_{\widetilde C_i}(B_i),\qquad
\deg B_i=(a+b-4)e-2g+2.
\]
This concerns reduced Gorenstein curves. For a smooth component in a reduced union, \(B_i\) measures its scheme-theoretic attachment to the rest. In a nodal curve it counts the marked branches of nodes; a self-node contributes twice on its normalized component.

For (4,4), a proposed component of degree e and normalization genus g must carry conductor degree \(4e-2g+2\). In particular, a rational line has six units, a smooth plane quartic has twelve, and a rational quartic has eighteen. These are stronger constraints than the total genus equation alone, though they still do not imply global realizability.

For \(W=C\cup D\) reduced and C smooth of degree e and genus g, put \(s=a+b-4\). The attachment and residual formulas are
\[
\operatorname{length}(C\cap D)=se-2g+2,
\quad\deg D=ab-e,
\quad p_a(D)=g+\frac{s(ab-2e)}2.
\]
They follow from duality on C and the union exact sequence. For the fixed rational quartic in degree (d,d), they specialize to
\[
\deg D=d^2-4,\quad p_a(D)=(d-2)(d^2-8),
\quad\operatorname{length}(C\cap D)=8d-14.
\]
The residual genus is arithmetic; smoothness and irreducibility require separate existence arguments. At d=4 the reviewed notebook supplies those arguments. At other degrees these formulas alone do not supply them.

## 6. Nonreduced limits: an explicit nilpotent calculation

Take independent linear forms L,M and
\[
W=V(L^4,M^4).
\]
This is a proper complete intersection with cycle \(16[V(L,M)]\). A complementary choice of coordinates gives a finite projection to the support line and
\[
\pi_*\mathcal O_W=\bigoplus_{0\le i,j\le3}
\mathcal O_{\mathbf P^1}(-i-j).
\]
Consequently
\[
P_W(n)=\sum_{i,j}(n-i-j+1)=16(n+1)-48=16n-32.
\]
Its reduced topology is a sphere, while the twisted nilpotent layers account for arithmetic genus thirty-three. There are no additional residual components.

Even a pure multiplicity-four degree-four support occurs in characteristic zero: \(V(L^4,G_4)\) has cycle \(4[D]\) when \(D=V(L,G_4)\) is a smooth plane quartic. Its four layers \(\mathcal O_D(-j)\), \(0\le j\le3\), have polynomials \(4n-4j-2\), whose sum is again \(16n-32\).

These examples show that fixed Hilbert polynomial, arithmetic genus, subcanonical duality, and smoothability permit pure multiple cycles, including rational support. The excluded fixed cycle \(4[C]\) needs the actual rational-quartic embedding; its exclusion is the scope of promoted R0022, not a consequence of the general topology budget.

## 7. A sharper marked-curve deduction when a carrier is smooth along C

**Proposed lemma.** Suppose a proper quartic pencil contains C and has a member F smooth at every point of C. If its generic intersection multiplicity along C is at least two, then the pencil contains \(q^2\), where \(q=x_0x_3-x_1x_2\). More precisely,
\[
W=V(F,q^2),\qquad [W]=2[C]+2[C'],
\]
where C' is the residual divisor of type (3,1) to C of type (1,3) on the smooth quadric Q. The divisor C' has no C component. Thus the generic multiplicity of C is exactly two. The residual divisor C' need not be irreducible or reduced for a special F.

**Proof.** The first normal symbols f,g of F,G are sections of \(N^*_{C/\mathbf P^3}(4)\). Generic multiplicity at least two forces their wedge to vanish generically, hence everywhere. Smoothness of F along all of C makes f nowhere zero, so it defines a subbundle \(\mathcal O_C\). The symbol g belongs to this subbundle, giving \(g=\lambda f\) with \(\lambda\in H^0(\mathcal O_C)=k\). Thus
\[
G-\lambda F\in H^0(\mathcal I_C^2(4)).
\]
Here the square is the ideal-sheaf square, so saturation issues are not suppressed. The known elementary quartic calculation gives this space as \(kq^2\): restriction of a twice-vanishing quartic to Q would have residual type (2,-2), so is zero; after division by q, its quadratic factor must be the unique quadric through C. Properness makes \(G-\lambda F\) nonzero. Finally, C' has type (3,1); subtracting C leaves type (2,-2), so C' cannot contain C. This proves the stated cycle and multiplicity.

For an explicit smooth example take the displayed F,G from section 4 and \(S=V(F+G)\). Its partial derivatives show S smooth in characteristic zero. Under Segre coordinates \((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\),
\[
(F+G)|_Q=(ad^3-bc^3)(a^3d-b^3c).
\]
Both factors define smooth rational quartics C,C', with ten transverse intersections (the endpoints and eight other points). Hence
\[
V(F+G,q^2)\quad\hbox{has cycle }2C+2C'.
\]
Its reduced support D is the (2,4) curve \(C\cup C'\), of genus nine. On S, W is the double Cartier divisor 2D. The sequence
\[
0\longrightarrow\mathcal O_D(-2)\longrightarrow
\mathcal O_{2D}\longrightarrow\mathcal O_D\longrightarrow0
\]
gives polynomials \((8n-24)+(8n-8)=16n-32\).

There is also an actual flat pencil retaining C between the four-quartic member and this double member:
\[
W_{[u:v]}=V(F+G,\ uF+vq^2).
\]
No nonzero combination \(uF+vq^2\) is a multiple of F+G, so every parameter is a proper complete intersection on S. At [1:0] it is the four-quartic arrangement; at [0:1] it is 2D. No assertion that the other members of this particular pencil have smooth residual curves is needed.

On any smooth quartic carrier the same calculation is compatible with the K3 intersection lattice:
\[
H^2=4,\quad H\cdot C=4,\quad C^2=-2,
\quad C'=2H-C,\quad C\cdot C'=10.
\]
This explains why reduced quartics in a (4,4) arrangement carry eighteen attachment units, while the support quartics in the doubled (2,4) member carry ten. Reduction has changed the adjunction problem.

For general equal degree d and any smooth connected projective marked curve, the first part of the argument still applies: if one carrier is smooth everywhere along C and the multiplicity is at least two, a constant change of the two generators produces a nonzero member of \(H^0(\mathcal I_C^2(d))\). At d=4 its one-dimensionality makes the conclusion especially rigid. In higher degrees this source space grows, and its image on the smooth carrier must be studied rather than assumed to consist of a single square.

## 8. General patterns and the remaining question

For (d,d),
\[
P_W(n)=d^2n-d^2(d-2),\qquad g=1+d^2(d-2).
\]
Products of d general planes on each side yield \(d^2\) lines with \(d^2(d-1)\) nodes, so all genus becomes graph loops. The opposite example \(V(L^d,M^d)\) has cycle \(d^2[L\cap M]\) and layers \(\mathcal O_L(-i-j)\), \(0\le i,j<d\), yielding the same polynomial. For (a,b), the corresponding grid has ab lines and \(a\binom b2+b\binom a2\) nodes, whose graph genus is exactly \(1+ab(a+b-4)/2\).

The most useful classification data therefore consist of component degrees and multiplicities, normalization genera, incidence and branch contacts, componentwise conductor divisors in the reduced case, and nilpotent filtrations in the nonreduced case. Numerical conditions are necessary; an actual pair of global forms remains an additional realization requirement.

For the fixed quartic, the new smooth-carrier dichotomy isolates a precise difficult stratum: multiplicity at least three requires that every pencil member be singular somewhere on C. It does not assert a common singular point for all members, and does not classify that stratum. In higher degrees, studying \(H^0(\mathcal I_C^2(d))\) on a smooth carrier is a concrete continuation of the same question. No unrestricted STCI conclusion or new canonical record is claimed.

## 9. Evidence and review boundary

All new product examples, genus allocations, nilpotent calculations, and the smooth-carrier lemma have elementary proofs above and independent agent reconstruction in the linked audit. No inherited certificate was rerun. External sources were inspected for flat-family coherent Euler characteristic, the delta definition, and the local Milnor formula, at the precise links above; no literature novelty claim is made. The unresolved work is a classification or realization theorem beyond these examples and the stated smooth-carrier stratum.
