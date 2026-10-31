# Continuous and algebraic sections on the complement of a smooth space curve

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
see the [scoped audit](2026-10-31-complement-sections-and-topology-audit.md).
The topological and holomorphic statements are over the complex numbers.
The algebraic nonsplitting argument works over any algebraically closed
field. These are applications of standard obstruction theory and Hartogs
extension, with no claim of literature novelty.

The unrestricted characteristic-zero STCI problem for
\(C_0=[s^4:s^3t:st^3:t^4]\) remains open. The purpose here is to
identify exactly what the classical section problem on its complement
does and does not constrain, before proposing a new obstruction campaign.

## 1. A continuous section exists precisely when the top Chern class vanishes

Let \(C\subset\mathbf P^3_{\mathbf C}\) be **any smooth connected curve**,
of degree d and genus g, and let \(U=\mathbf P^3(\mathbf C)\setminus C(\mathbf C)\).
For every topological complex vector bundle E of rank two on U,
\[
E\text{ has a continuous nowhere-zero section}
\quad\Longleftrightarrow\quad c_2(E)=0\text{ in }H^4(U,\mathbf Z).
                                                                         \tag{1}
\]
In particular, for the restricted algebraic line bundles,
\[
\boxed{\ \mathcal O_U(a)\oplus\mathcal O_U(b)
\text{ has a continuous nowhere-zero section}
\quad\Longleftrightarrow\quad d\mid ab.\ }                             \tag{2}
\]
No assumption that C is STCI is used in this theorem.

Here is the complete obstruction calculation. The complex normal bundle
of C has oriented real rank four. Thom isomorphism and the pair sequence
give the integral Gysin sequence
\[
\cdots\to H^{i-4}(C,\mathbf Z)\to H^i(\mathbf P^3,\mathbf Z)
\to H^i(U,\mathbf Z)\to H^{i-3}(C,\mathbf Z)\to\cdots .
\]
The map \(H^0(C)\to H^4(\mathbf P^3)\) is multiplication by d.
The map \(H^2(C)\to H^6(\mathbf P^3)\) is an isomorphism: a
point class pushes forward to a point class. Consequently
\[
H^0(U,\mathbf Z)=\mathbf Z,\qquad H^2(U,\mathbf Z)=\mathbf Z h,
\]
\[
0\to\mathbf Z/d\to H^4(U,\mathbf Z)\to\mathbf Z^{2g}\to0,               \tag{3}
\]
and all other positive-degree integral cohomology groups vanish.
The sequence (3) splits as abelian groups, noncanonically. The class
\(h^2\), the restricted square of the hyperplane class, generates the
displayed torsion subgroup and has exact order d.

General position shows \(\pi_1(U)=0\): a loop bounds a disk in P3,
and the disk can be perturbed away from the real codimension-four
submanifold C. Removing an open tubular neighborhood of C gives a
compact six-manifold with boundary homotopy equivalent to U. Thus U
has the homotopy type of a finite CW complex of dimension at most six.

Choose a Hermitian metric on E and consider its unit-sphere bundle,
with fiber \(S^3\). The first obstruction to a section is its oriented
Euler class, which is \(c_2(E)\), in \(H^4(U,\mathbf Z)\).
The only remaining possible obstruction groups in this dimension are
\[
H^5(U,\pi_4(S^3))=H^5(U,\mathbf Z/2),\qquad
H^6(U,\pi_5(S^3))=H^6(U,\mathbf Z/2).
\]
The local coefficient systems are trivial. Both groups vanish by the
coefficient Bockstein sequence and the integral vanishings in degrees
five, six and seven. There are no higher-dimensional cells. This proves
sufficiency in (1); a nowhere-zero section implies vanishing of the
Euler class, proving necessity. Finally
\(c_2(\mathcal O(a)\oplus\mathcal O(b))=ab\,h^2\), yielding (2).

For the standard sphere-bundle obstruction framework and the Euler
class as primary obstruction, see
[Hatcher, Vector Bundles and K-Theory, §3.3](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf).
The two sphere homotopy groups used here are listed in
[Hatcher, Algebraic Topology, Chapter 4, p. 339](https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf).
The argument above also checks the higher obstruction groups; merely
computing the top Chern class would not alone establish sufficiency.

For C0, d=4 and g=0. Every degree pair permitted by the cycle equation
\(ab=4m\) therefore admits a continuous nowhere-zero section of the
specified bundle. This solves the classical continuous-section problem
uniformly, not the algebraic STCI problem. It does not exhaust geometric
or topological information involving the actual defining surfaces,
their singularities or a chosen degeneration.

## 2. Holomorphic sections retain exactly the original equation problem

Fix positive integers a,b. Every holomorphic section of
\(\mathcal O_U(a)\oplus\mathcal O_U(b)\) extends uniquely across C.
Locally trivialize the bundles and apply analytic Hartogs extension
across the complex codimension-two subset to each component; uniqueness
glues the local extensions. Global holomorphic sections on P3 are the
usual homogeneous polynomials of the indicated degrees.

Therefore a holomorphic nowhere-zero section on U is precisely a pair
of degree-a and degree-b homogeneous polynomials with no common zero
outside C. Their projective intersection is nonempty, since both degrees
are positive, and has no surface component since none can be contained
in C. It is a proper curve intersection supported on the irreducible C,
so its reduced support is exactly C. Conversely a supported pair plainly
gives such a holomorphic section. Thus
\[
\text{holomorphic nowhere-zero section of }
\mathcal O_U(a)\oplus\mathcal O_U(b)
\quad\Longleftrightarrow\quad
\text{STCI equations of degrees }(a,b).                                \tag{4}
\]
The missing step is continuous-to-holomorphic realization with the
specified bundle. There is no separate analytic-versus-algebraic gap
for these sections, and no Oka principle on U is asserted.

## 3. The algebraic extension associated to successful equations cannot split

For a supported pair F,G of positive degrees a,b, the section on U
fits into an exact sequence
\[
0\to\mathcal O_U\xrightarrow{(F,G)}
\mathcal O_U(a)\oplus\mathcal O_U(b)
\xrightarrow{(-G,F)}\mathcal O_U(a+b)\to0.                             \tag{5}
\]
It is **necessarily nonsplit as an algebraic extension**. Algebraic
Hartogs extension gives
\[
\operatorname{Hom}_U(\mathcal O_U(a)\oplus\mathcal O_U(b),\mathcal O_U)
=H^0(\mathbf P^3,\mathcal O(-a))\oplus
 H^0(\mathbf P^3,\mathcal O(-b))=0.
\]
A splitting would give a nonzero retraction, a contradiction.
The same conclusion holds holomorphically. In the continuous category,
by contrast, a Hermitian metric supplies a complementary subbundle.

On the actual affine cover \(D_+(F)\cup D_+(G)=U\), local right
inverses to the final arrow are \((0,1/F)\) and \((-1/G,0)\).
Their difference is \((F,G)/(FG)\). Thus the extension class is
represented up to sign by
\[
\xi_{F,G}=[1/(FG)]\in H^1(U,\mathcal O_U(-a-b)),\qquad\xi_{F,G}\ne0.
                                                                         \tag{6}
\]
A nonzero extension class is compatible with successful equations;
it is required by them. The desired trivial line subbundle is not
an algebraic direct summand. This distinction is already familiar
from the Euler sequence on P1 and is not evidence against existence.

## 4. What the affine motivic theorems do and do not supply

The complement U is not affine: Hartogs gives \(H^0(U,\mathcal O_U)=\mathbf C\),
although U has dimension three. The rank-two case of
[Asok–Bachmann–Hopkins, Theorem 7.1.1](https://arxiv.org/pdf/2306.04631)
concerns a smooth **affine** threefold over an algebraically closed
field of characteristic zero. It
characterizes splitting off a trivial direct summand by top-Chern-class
vanishing in the Chow group. On an affine scheme a nowhere-zero section
with vector-bundle quotient does split, so the two predicates coincide
there. On our U they do not: (5) must be nonsplit.

The affine representability comparisons in
[Asok–Hoyois–Wendt, Introduction and Theorem 4.2.10](https://msp.org/gt/2018/22-2/gt-v22-n2-p11-s.pdf)
retain the smooth affine source and the stated target hypotheses when
comparing naive A1-homotopy classes of morphisms with motivic homotopy
classes. A Jouanolou affine replacement does not
automatically descend an actual section of the pulled-back bundle.
Moreover a positive-rank affine-space torsor over U has dimension
greater than three while the bundle still has rank two, so the
rank-equals-dimension-minus-one theorem cannot simply be reapplied.

This does not invalidate motivic obstruction theory or exclude an
appropriately formulated descent construction. The checked theorems
do not provide that construction on this nonaffine complement.

## 5. Effect on strategy

The concrete gain is a complete classical topological section criterion
for every smooth connected complex space curve, together with the
necessary nonsplitting of the algebraic extension for a supported pair.
The former gives no condition beyond degree divisibility for the split
bundles relevant here. The latter prevents treating affine direct-summand
theorems as section-existence theorems on U.

Do not launch a computation of further classical section obstructions
for these bundles: (1) has already disposed of them. Do not infer that
all enriched motivic or carrier-dependent information is exhausted.
A new complement proposal needs a specified construction of actual
holomorphic/algebraic sections, a strict descent mechanism, or a new
algebraic obstruction retaining their required global data. Asking for
the appropriate extension with the desired middle bundle is an exact
reformulation until such an input is supplied. The present work supplies
neither those sections nor an unrestricted obstruction; C0 may be STCI.
