# Punctual extensions and actual equation columns on multiple quadrics

**Scope and status.** Independently reviewed mathematics. Let \(Q=V(q)\subset\mathbf P^3\) be a smooth split quadric and \(X_n=V(q^n)\). The finite-order Picard and punctual-extension theorems below hold over an algebraically closed field in every characteristic. The actual-pair dictionary and operation controls below also hold in every characteristic for \(C=C_0\) of class \((1,3)\). No statement settles characteristic-zero STCI. The [multiple-quadric matrix account](finite_pullback_and_matrix_obstructions.md#double-quadric-matrices-and-punctual-defects) already owns the explicit ACM endpoint matrix and its nonfactorization proof; here it is used only as a control.

## 1. Precise statements

Let k be algebraically closed, Q=V(q) a smooth split quadric in P3, and
X_n=V(q^n) for a finite integer n≥2. Identify Q with P1×P1 and write
L=O_Q(a,b). Fix any closed point z of Q.

**Picard statement.** Restriction Pic(X_n)→Pic(Q)=Z² is injective.
In characteristic zero its image is exactly the diagonal. In
characteristic p>0 its image is

\[
\{(a,b):p^e\mid a-b\},\qquad
e=\min\{j\ge0:p^j\ge n\}. \tag{1}
\]

**Punctual extension statement.** In every characteristic and for every
L there is a coherent sheaf M_n on X_n, generically free of rank one,
maximal Cohen–Macaulay at every point, and invertible away from z, such that

\[
\bigl(M_n\otimes_{\mathcal O_{X_n}}\mathcal O_Q\bigr)^{**}
\simeq L. \tag{2}
\]

The double dual in (2) is over O_Q. If L is outside the Picard image,
the nonfree locus of M_n is exactly {z}. No bound on the scheme length,
local number of generators or complexity of that defect is asserted.
If L is in the Picard image, an invertible global extension can be used.

The statements are uniform in n and in the chosen point. In particular
z may be either marked endpoint of the fixed quartic C0. They impose no
global arithmetically Cohen–Macaulay condition on M_n and supply no
two-generator homogeneous presentation or defining equation column.

## 2. The first obstruction and its characteristic-independent normalization

The ideal of Q in X_2 is J=O_Q(-2,-2)=K_Q. The square-zero units sequence
gives

\[
H^1(Q,J)\to\operatorname{Pic}(X_2)\to\operatorname{Pic}(Q)
\xrightarrow{\delta}H^2(Q,J).
\]

This is [Stacks, Lemma 37.4.1](https://stacks.math.columbia.edu/tag/0C6Q).
Künneth gives H1(J)=0 and H2(J)=k. The first restriction is injective.

Here is a direct computation of the obstruction, valid also in
characteristic two. Write the Segre coordinates as

    x0=A0B0, x1=A0B1, x2=A1B0, x3=A1B1.

For the ruling bundle O_Q(1,0), lift the transitions A1/A0 using x2/x0
on the B0 strip and x3/x1 on the B1 strip. The discrepancy around the
product-cover square is

\[
\frac{x_0x_3}{x_1x_2}=1+\frac q{x_1x_2}. \tag{3}
\]

On x0≠0 put r=x2/x0, t=x1/x0 and use q/x0² as the local frame of J.
The coefficient in (3) is 1/(rt), representing the nonzero generator
γ of H2(O_Q(-2,-2)) in product Čech cohomology. Since O_Q(1,1)
extends from P3 and δ is a group homomorphism,

\[
\delta(O_Q(a,b))=(a-b)\gamma. \tag{4}
\]

In characteristic zero this immediately gives the diagonal image.
An invariant interpretation uses

\[
0\to K_Q\to\Omega_{\mathbf P^3}|_Q\to\Omega_Q\to0.
\]

The restricted Euler sequence gives H1(ΩP3|Q)=k and H2(ΩP3|Q)=0;
the image in H1(ΩQ)=k² is the diagonal hyperplane class. Its boundary
applied to c1(L) is (4), the line-bundle Atiyah/conormal obstruction.
[Arinkin–Căldăraru, Proposition 2.10](https://arxiv.org/pdf/1007.1671)
provides that obstruction interpretation. The explicit units calculation
(3) is the argument used here in arbitrary characteristic.

## 3. Every finite order and the characteristic-p lattice

The ideal for X_j⊂X_(j+1) is O_Q(-2j,-2j). Its H1 is zero, so every
successive Picard restriction is injective. In characteristic zero,
restriction through X2 and the ambient extensions of O_Q(a,a) finish
the statement for every n.

In characteristic p, put P=p^e. If n≤P, the coordinate power map

\[
[x_0:x_1:x_2:x_3]\longmapsto[x_0^P:x_1^P:x_2^P:x_3^P]
\]

maps X_n to Q, since the target quadric equation pulls back to q^P.
Pullback of a ruling bundle gives a lift of O_Q(P,0). Together with
ambient diagonal twists, this proves sufficiency in (1).

For necessity write d=a−b≠0 as d=P u, with P=p^v and p not dividing u.
Lift transition functions of O_Q(1,0) arbitrarily through order P+1.
Their cocycle discrepancies start with 1+q c modulo q², representing γ.
Raising these transitions to P-th powers gives a genuine cocycle modulo
q^P, whose obstruction at the next order is the Frobenius image

\[
F^{v*}\gamma\in H^2(Q,O_Q(-2P,-2P)).
\]

In the product Čech description it is represented by r^(-P)t^(-P).
This monomial is nonzero: the basis ranges for H2(O(-2P,-2P)) are
r^(-i)t^(-j), with 1≤i,j≤2P−1. Raising also to the u-th power
multiplies this obstruction by the nonzero scalar u in k.

The extension to X_P is unique by the injectivity already proved.
Consequently a different choice of lift cannot evade this next
obstruction. There is no lift to X_(P+1), hence none to any X_n with
n>P. This proves (1), including p=2. The case d=0 is supplied by
ambient hyperplane powers.

The geometric contrast is exact: Frobenius kills the transition
discrepancies through a finite order, while characteristic zero already
detects every nonzero ruling imbalance at the first thickening.
This does not transport an STCI construction between characteristics.

## 4. Removing one point, then extending coherently

Set U=Q\{z}. After a product automorphism, z=(∞,∞), and

\[
U=(\mathbf A^1\times\mathbf P^1)\cup
(\mathbf P^1\times\mathbf A^1),
\]

with intersection A2. Each product open has quasi-coherent cohomological
dimension at most one by its affine projection to P1; the intersection
is affine. Mayer–Vietoris gives H2(U,F)=0 for every quasi-coherent F.
Thus every successive units obstruction on U vanishes. Any L|U lifts
to an invertible sheaf L_n on X_n\{z}, for each finite n. The punctured
lifts can be chosen compatibly as n increases.

Choose a coherent extension N_n of L_n to X_n and set

\[
M_n=\mathcal Hom_{X_n}
\bigl(\mathcal Hom_{X_n}(N_n,\mathcal O_{X_n}),\mathcal O_{X_n}\bigr).
\]

A coherent extension exists by the finite-type extension results in
[Stacks, §28.23](https://stacks.math.columbia.edu/tag/01PD).
One may take a suitable finite-type subsheaf of the quasi-coherent
pushforward from the punctured open; the pushforward itself is not
asserted coherent.

To check depth at z, let R be its two-dimensional Cohen–Macaulay local
ring on the hypersurface X_n. A finite presentation of any finite
R-module N gives

    0 → N* → R^r → R^s.

The image in R^s has depth at least one when nonzero, since a regular
element of R is regular on every submodule of a free module. The
[depth lemma](https://stacks.math.columbia.edu/tag/00LX) gives depth(N*)≥2
when the dual is nonzero; the zero-image case is immediate. Applying
this to the second dual proves M_n is MCM at z. Off z it remains the
original line bundle. Generic rank one is preserved.

The reduction of M_n has rank one and equals L off z. On the smooth
surface Q its double dual is therefore a line bundle, and it is L:
restriction Pic(Q)→Pic(Q\{z}) is an isomorphism. Finite-support torsion
in the reduction disappears under this double dual. If M_n were also
free at z, it would be a global line bundle lifting L, proving the
asserted necessity of a nonfree point when L lies outside (1) or the
characteristic-zero diagonal.

This establishes (2). It does not assert that the coherent extensions
M_n can be chosen compatibly under reduction as n varies. No formal
or algebraized infinite-thickening module is constructed.

## 5. An explicit characteristic-zero comparison with the sextic normal correction

Work in characteristic zero in this section. For the fixed C=C0=[s4:s3t:st3:t4] of class (1,3) on Q, the
[sextic source calculation](quadric_modification_and_global_corrections.md) produces
the class of 4s^11t^11 in a quotient of H0(O_C(22)) by the actual
normal-correction image. Project first to the larger correction quotient

\[
W=H^0(O_C(22))\big/
\big(s^{12}H^0(O_C(10))+t^{12}H^0(O_C(10))\big).
\]

There is an explicit comparison, not merely a numerical resemblance.
The exact Koszul sequence

\[
0\to O_C(-2)\xrightarrow{(t^{12},-s^{12})}
O_C(10)^2\xrightarrow{(s^{12},t^{12})}O_C(22)\to0
\]

identifies W with H1(O_C(-2))=H1(ω_C). On the two standard opens,
lift 4s^11t^11 using (4t^11/s,0) and (0,4s^11/t). Their difference
gives the Čech class ±4/(st).

Next use the adjunction sequence

\[
0\to K_Q\to K_Q(C)=O_Q(-1,1)\to\omega_C\to0.
\]

Its middle term is acyclic. The boundary H1(ω_C)→H2(K_Q) is therefore
an isomorphism, trace-dual to the restriction of constants from Q to C.
With compatible residue and Čech conventions, the composite carries
the displayed normal-correction class to ±4γ. For example, on the
quadric chart r=A1/A0, t=B1/B0, the curve is t³−r=0 and the residue
of dr∧dt/(t³−r) is −dt, with no factor three.

Consequently this explicit linear comparison identifies the nonzero
displayed class, up to its fixed sign convention, with the Picard
obstruction δ(O_Q(2,6))=−4γ. It does **not** identify the two deformation
problems or make a line-bundle lift equivalent to an actual defining
pair. It applies to the obstruction calculated for that specified
sextic source. No corresponding map for arbitrary pair corrections
has been asserted.


## 6. An all-order defect dictionary for a hypothetical supported pair

Assume Y=V(F_a,G_b) is a proper complete intersection with reduced
support exactly C. Choose the least N with q^N=AF+BG. Set

\[
\Phi=\begin{pmatrix}F&-B\\G&A\end{pmatrix}:
E=\mathcal O(-a-b)\oplus\mathcal O(-2N)
\longrightarrow H=\mathcal O(-b)\oplus\mathcal O(-a).
\]

Its cokernel M is the ideal I_{Y,NQ} inside O_{NQ}: the row (−G,F)
has image that ideal, kills the first column, and sends the second to
q^N. The ordinary syzygy of the regular sequence F,G proves exactness.
The presentation makes M globally ACM and locally MCM on NQ. It is
generically rank one and equals O_{NQ} outside C.

Neither F nor G is divisible by q. Otherwise its mate would cut a
balanced divisor on Q supported only on the unbalanced curve C, which
is impossible. Their common divisorial factor on Q is therefore c^r,
where c defines C and r≥1. Write

\[
\bar F=c^r f,\quad \bar G=c^r g,\qquad
f\in H^0\mathcal O_Q(a-r,a-3r),\quad
g\in H^0\mathcal O_Q(b-r,b-3r).
\]

The residual sections have no common divisor. Their finite common-zero
scheme T is supported on C, and a,b≥3r. Intersection on Q gives

\[
\ell(T)=2ab-4r(a+b)+6r^2. \tag{1}
\]

This is an intersection budget, not a new residual-degree estimate; its
r=1 instance already occurs in the
[blowup residual calculation](blowup_residual_geometry.md).

Put L=O_Q(−a−b+r,−a−b+3r). The primitive column
α=(f,g)^t:L→H|_Q is saturated and has quotient
I_T O_Q(−r,−3r). The second column of the rank-one reduction factors
through the same L. A scalar defined off T extends over T on smooth Q,
so

\[
\bar\Phi=\alpha(c^r,h),\qquad
h\in H^0\mathcal O_Q(2N-a-b+r,2N-a-b+3r). \tag{2}
\]

Here h is nonzero: if both A,B were divisible by q, minimality of N
would fail, and (2) makes either zero reduced entry force both to be
zero. Put e=min(r,ord_C h) and k=r−e. Factoring the common divisor eC
from the row gives the syzygy line

\[
\ker\bar\Phi=\det(E|_Q)\otimes L^{-1}(eC)
=\mathcal O_Q(-2N-k,-2N-3k).
\]

This remains the kernel when the divided row has a finite base scheme:
two sections without a common divisor on a smooth surface have the
usual Koszul syzygy. Restricting the presentation to Q identifies this
kernel with Tor_1(M,O_Q)=Ann_M(q)(−2). Consequently

\[
\operatorname{Ann}_M(q)=
\mathcal O_Q(2-2N-k,2-2N-3k). \tag{3}
\]

The inclusion M⊂O_{NQ} identifies (3) with a line subideal of
Ann_{O_{NQ}}(q)=O_Q(2−2N). Its effective divisor is supported on C,
and its class forces that divisor to be kC. Multiplication in the
same ideal embedding gives

\[
q^{N-1}M=I_T\mathcal O_Q(2-2N-r,2-2N-3r). \tag{4}
\]

These are actual inclusions in a fixed ideal, not merely abstract
line-bundle identifications. Combining them yields

\[
D_q:=\operatorname{Ann}_M(q)/q^{N-1}M
\simeq\mathcal O_Q(2-2N-k,2-2N-3k)
\otimes\mathcal O_Q/(c^e I_T). \tag{5}
\]

The divisorial cycle of this defect is e[C]. Its finite contribution
has length (1), by the exact sequence

\[
0\longrightarrow\mathcal O_T(-eC)
\longrightarrow\mathcal O_Q/(c^eI_T)
\longrightarrow\mathcal O_{eC}\longrightarrow0.
\]

Minimality of N forces k≥1. If k=0, the inclusion (3) contains all
q^{N−1}O_{NQ}, giving q^{N−1} in the ideal sheaf of Y. The homogeneous
complete-intersection ideal is saturated, so q^{N−1}∈(F,G), a
contradiction. In particular the formulas permit 0≤e≤r−1; they do
not assume generic freeness along C.

Nor do they assume a torsionfree reduction. The exact reduction is

\[
0\longrightarrow L/\operatorname{im}(c^r,h)
\longrightarrow M/qM
\longrightarrow I_T\mathcal O_Q(-r,-3r)\longrightarrow0. \tag{6}
\]

Geometrically, D_q measures the failure of the bottom annihilator layer
to be generated by the highest q-multiple of the ideal. That failure
may contain an entire multiple of C, as well as a finite scheme. It is
not an additional curve outside C. The formula identifies what must be
compared with a global capacity bound; it supplies no such new bound.

## 7. What an integral pole operation preserves

More generally, let P be a homogeneous two-by-two matrix between split
bundles with determinant q^d and nonzero generic rank-one reduction on
Q. Its saturated image L_P=O_Q(α,β) in the target bundle is a line
bundle: saturation gives a torsionfree quotient, and the depth lemma
on the smooth surface makes this rank-one kernel reflexive. Its fiber
inclusion may vanish at finitely many points.

If a nonzero distinguished column comes from O(−a), and its reduced
zero support on Q is exactly C, its section of L_P(a,a) has divisor
νC for some ν≥1. Hence

\[
L_P(a,a)=\mathcal O_Q(\nu,3\nu),\qquad \beta-\alpha=2\nu. \tag{7}
\]

Finite degeneracy of the inclusion outside C must also be absent.
Here ν is a column divisor order, not the intersection multiplicity
of the original surfaces. For Φ in §6, a in this general notation is
the source twist a+b, and ν=r.

Consider a homogeneous degree-zero rational target operation

\[
U=I+(h/q^j)vw,\quad v=(v_1,v_2)^t,\quad
w=(-v_2,v_1),\quad j\ge1,
\]

where q∤h and q does not divide both components of v. Since wv=0,
det U=1. Polynomiality is equivalent to q^j dividing wP: the
forward implication follows by taking a component of v of q-valuation
zero. This divisibility forces the generic reduced image of P to be
spanned by v̄. Writing wP=q^jR gives UP=P+hvR. If UP still has
nonzero generic rank-one reduction, its generic image, and therefore
its saturation, is the same L_P.

Polynomial invertible right operations preserve the image; target
bundle automorphisms preserve its isomorphism class. Thus these
operations preserve (7)'s ruling difference as long as every boundary
reduction stays in the nonzero rank-one stratum. The standard matrix
[[x0,x1],[x2,x3]] has L=O_Q(−1,0), its transpose O_Q(0,−1), and
the [endpoint-defect matrix](finite_pullback_and_matrix_obstructions.md#double-quadric-matrices-and-punctual-defects)
has L=O_Q(−1,−1). Their differences 1, −1, 0 fail (7).

## 8. Rank-zero transitions can change the saturated class

The preceding invariant does not survive a rank-zero transition. The following explicit escape prevents its use as an invariant of arbitrary matrix constructions. For the
endpoint matrix P0 in the linked note, set v=(ℓ,m)^t,
w=(−m,ℓ), J=[[0,1],[−1,0]]. Directly,

\[
P_0J^{-1}=qI-vw,\qquad (I+vw/q)(qI-vw)=qI.
\]

The reduction is now zero. Multiply by q and take
v′=(x0²,x2²)^t, w′=(−x2²,x0²). Then

\[
P'=(I+v'w'/q^2)q^2I=q^2I+v'w',\qquad\det P'=q^4.
\]

This is an actual homogeneous matrix O(−4)^2→O². On Q,
v′=v0²(u0²,u1²)^t, so its saturated image is O_Q(−2,0).
The ruling difference is now 2, as required by (7) for ν=1.
But the full column class is L(4,4)=O_Q(2,4), which is not νC
for any ν. Moreover P̄′ has common factor v0⁴ and rank zero along
the ruling v0=0, a line not contained in C. Its cokernel is nonfree
there. This construction fails the full divisor and support conditions.

Its purpose is to challenge an overly strong strategy inference, not
to launch an enumeration. It proves that changing the ruling difference
alone is an attainable but insufficient construction milestone.


## 9. What the two descriptions retain

The all-order dictionary in §6 and operation controls in §§7–8 use no division by a positive integer: smoothness of Q, unique factorization at its prime divisor, Koszul syzygies and the actual ideal embedding are their inputs. These arguments extend the stated dictionary and operation identities to every characteristic. It is compatible with positive-characteristic STCI examples because it is a dictionary and an invariant for a bounded operation class, not an exclusion.

Removing one point kills the finite-order lifting obstructions on the punctured quadric. Double duality replaces a missing line bundle by a rank-one MCM sheaf with one prescribed nonfree point. This is possible for every ruling imbalance and finite thickness; it does not bound local defect or provide a compatible system of global MCM extensions as n varies. In contrast, an actual supported pair fixes a two-column homogeneous presentation and an ideal embedding. Its normal-action quotient is the explicit object (5) of §6: a divisorial contribution on C and a finite intersection scheme can both occur. Neither is automatically an extra component downstairs.

The two statements are complementary. The punctual theorem refutes bare Picard nonlifting, even with the nonfree locus restricted to one endpoint, as an exclusion of all MCM objects. The actual-column dictionary identifies extra data available for a genuine pair; no estimate here bounds those data incompatibly. The pole-operation proof applies to any prime boundary polynomial in the stated nonzero rank-one stratum. The column-divisor argument applies to an irreducible target curve on any smooth boundary surface. Neither gives an exhaustive matrix classification: the explicit rank-zero reset demonstrates the missing stratum.

The standard [ACM/MCM presentation dictionary in Hartshorne's appendix, pp. 430–431](https://seminariomatematico.polito.it/rendiconti/64-4/419.pdf) does not add a factorization theorem. The applicability boundaries of the closest representation results matter here: [Kerner–Vinnikov's global treatment, §4.2, Definition–Proposition 4.4](https://arxiv.org/pdf/0906.3012) concerns linear representations and requires generic maximal generation for its reduced-kernel descent; arbitrary-twist, generically corank-one presentations on the repeated hypersurface \(q^N\) do not acquire those hypotheses. Their [local Corollary 3.3 and Theorem 3.4](https://arxiv.org/pdf/1009.2517) respectively require maximal generation on the smooth reduced locus and relatively prime factors; repeated copies of \(q\) do not satisfy the latter condition. The [low-rank ACM classification on a double plane](https://arxiv.org/pdf/1604.00866) has a different reduced surface and does not classify the multiple-quadric presentations above. Finally, [Cohn, §7, p. 26](https://www.numdam.org/item/PMIHES_1966__30__5_0.pdf) exhibits a determinant-one polynomial matrix over \(k[x,y]\) outside the subgroup generated by elementary matrices. This prevents treating elementary generation over general polynomial rings as automatic; it is not a theorem about \(S[q^{-1}]\) or proof that the operations of §7 exhaust matrices on that localization.

The [sextic lift account](rank_strata_and_sextic_lifts.md) treats actual allowed source directions; the cohomological comparison in §5 identifies the specified obstruction class, not the deformation problems. The [comparison and specialization argument](../arguments/transverse_specialization.md) treats a different filtered comparison defect. No map identifies its module with the normal-action quotient here.

A general conditional form of the punctual construction is useful. Let S be a smooth surface, Z a finite set, and X a finite Cohen–Macaulay thickening of S whose successive square-zero ideals are coherent sheaves on S. If \(H^2(S\setminus Z,J)=0\) for each successive ideal J, every line bundle on \(S\setminus Z\) lifts to \(X\setminus Z\). Any coherent extension followed by a double dual is MCM at the closed points of Z by the two-dimensional depth argument in §4, and its reduced reflexive hull is the original line bundle when \(\operatorname{Pic}(S)\to\operatorname{Pic}(S\setminus Z)\) is an isomorphism. The result is conditional on the displayed cohomological vanishing; no vanishing theorem for arbitrary punctured surfaces is asserted.

The constructions leave open how actual homogeneous equation columns constrain the amount and scheme structure of defect, and whether a new operation can retain both the full column divisor and sole embedded support. An unrestricted supported pair is neither constructed nor excluded.

## Independent review and scope

The finite-order Picard and punctual MCM statements, the actual-column dictionary, bounded operation invariant and rank-zero reset were independently checked against their source proofs. The characteristic-free scope of the actual-column identities and the conditional punctured-surface extension were reconstructed separately. The matrix-literature restrictions remain explicit. These statements do not provide compatible all-order global extensions or a supported pair.

The inherited mathematical inputs retain the scope and review evidence of their linked owners. No inherited CAS campaign was broadly rerun, and the unrestricted characteristic-zero STCI question remains open.
