# Independent audit: ruling imbalance on finite multiple quadrics

Date: October 31, 2026. Reviewer: `punctual_quadric_lift_review`,
independent of the proposing agent. Status: **PASS for the precise
finite-thickening statements below; independently reviewed provisional
results, no canonical promotion or STCI conclusion**. This audit
independently reconstructs the obstruction, its characteristic dependence,
the punctured lifting, and the Cohen--Macaulay extension. No local module
classification, degree campaign, or inherited computation was run.

## 1. Exact hypotheses and approved claims

Let k be algebraically closed, let
\[
q=x_0x_3-x_1x_2,\quad Q=V(q)\subset\mathbf P^3_k,
\quad X_n=V(q^n),\quad n\ge2,
\]
and identify Q with the Segre product by
\[
(x_0,x_1,x_2,x_3)
=(A_0B_0,A_0B_1,A_1B_0,A_1B_1).
\]
Let z be **any** point of Q and let L=O_Q(a,b), with a,b arbitrary
integers. The curve is not needed for these statements. In the STCI
application one may choose z on the fixed rational quartic C0, of type
(1,3), over a characteristic-zero field.

The approved statements are:

1. Restriction Pic(X_n) -> Pic(Q)=Z^2 is injective. In characteristic
   zero its image is the diagonal. In characteristic ell>0 its image is
   \[
   \{(a,b):\ell^e\mid a-b\},\qquad
   e=\min\{j\ge0:\ell^j\ge n\}.
   \tag{1}
   \]
2. In every characteristic, L restricted to U=Q\{z} lifts to an
   invertible sheaf on X_n\{z}. Such punctured lifts can be chosen
   compatibly through successive finite thickenings.
3. For each fixed finite n there exists a coherent sheaf M_n on X_n,
   generically free of rank one, maximal Cohen--Macaulay at every point,
   and locally free of rank one away from z, such that
   \[
   (M_n\otimes_{O_{X_n}}O_Q)^{**}\simeq L.
   \tag{2}
   \]
   Here the double dual in (2) is over the smooth surface Q. If L is
   outside the image in claim 1, the nonfree locus of M_n is exactly
   {z}.

No compatibility of the global M_n under reduction from X_(n+1) to X_n
is claimed. No global ACM condition, split resolution by two line-bundle
sums, two-generator presentation, or actual equation column supported on
C0 is claimed.

## 2. The first obstruction, including characteristic two

For the successive square-zero extensions the ideal is
\[
J_j=(q^j)/(q^{j+1})=O_Q(-2j,-2j).
\]
The units exact sequence gives the Picard lifting obstruction in
H^2(Q,J_j). This is [Stacks, Lemma 37.4.1](https://stacks.math.columbia.edu/tag/0C6Q).
Kunneth gives H^1(Q,J_j)=0 for every j>=1 in every characteristic.
Consequently Pic(X_(j+1)) -> Pic(X_j) is injective. In particular an
extension to any given finite order, if it exists, is unique up to
isomorphism.

Here is a direct Cech calculation of the obstruction gamma to extending
O_Q(1,0) to X_2. It avoids an assumption on the characteristic in the
Atiyah-class comparison. Use the four Segre charts D(x_i). On the two
B-strips the transitions from the A0 frame to the A1 frame can be lifted
as
\[
v_0=x_2/x_0,\qquad v_1=x_3/x_1.
\]
The horizontal transitions between the two B-charts, with the A-frame
fixed, are 1. The square discrepancy of these four chosen transition
lifts is
\[
v_1/v_0=x_0x_3/(x_1x_2)=1+q/(x_1x_2).
\tag{3}
\]
All these ratios are units on their required intersections in X_2:
invertibility modulo the nilpotent ideal suffices. On the Q-torus put
r=x_2/x_0=A1/A0 and s=x_1/x_0=B1/B0. Trivializing J_1 on D(x_0) by
q/x_0^2 identifies the coefficient in (3) with
\[
r^{-1}s^{-1}.
\tag{4}
\]
In the product Cech complex for P1 x P1 this is the generator of
H^2(O_Q(-2,-2))=k. Equivalently, after trivializing by A0^(-m)B0^(-m),
the classes
\[
r^{-i}s^{-j},\qquad 1\le i,j\le m-1,
\tag{5}
\]
form a basis of H^2(O_Q(-m,-m)), for m>=2. The square formula is the
degree-(1,1) product Cech representative; choosing additional diagonal
edge transitions gives the same class in the ordinary four-chart Cech
complex. Changing the orientation changes its sign only.

Thus gamma is nonzero in every characteristic, including ell=2. The
obstruction map is additive. Since O_Q(1,1) extends from P3, it follows
with this normalization that
\[
\delta_2(O_Q(a,b))=(a-b)\,\gamma.
\tag{6}
\]
In characteristic zero this proves the diagonal image. Every diagonal
class extends from P3 to every X_n, so the same image holds for all n.

As an independent characteristic-zero cross-check, the conormal sequence
\[
0\to O_Q(-2,-2)\to\Omega_{P3}|_Q\to\Omega_Q\to0
\]
has cohomology segment k -> k^2 -> k -> 0. The restricted Euler
sequence identifies the first image with the diagonal hyperplane class.
The boundary of c1(L) is the extension obstruction: see
[Arinkin--Caldararu, Proposition 2.10, PDF p. 19](https://arxiv.org/pdf/1007.1671).
The direct calculation above, rather than a characteristic-dependent
version of that reference, establishes the all-characteristic assertion.

## 3. The exact finite-order lattice in positive characteristic

Assume char(k)=ell>0. Let P=ell^v. Choose arbitrary unit lifts g_ij of
transition functions of O_Q(1,0) on the affine chart intersections to
X_(P+1). Such lifts exist because these are affine nilpotent thickenings.
On triple intersections write their multiplicative defect as
\[
g_{ij}g_{jk}g_{ki}=1+\eta_{ijk},\qquad \eta_{ijk}\in(q).
\]
Its first normal coefficient is a Cech representative of gamma. In
characteristic ell, raising to P gives exactly
\[
(1+\eta_{ijk})^P=1+\eta_{ijk}^P.
\tag{7}
\]
Hence g_ij^P are cocycle transitions on X_P. Their obstruction at the
next layer X_(P+1) is the P-th Frobenius image of gamma in
H^2(Q,J_P). Terms of normal order at least two in eta contribute only
from order 2P onward, and 2P>=P+1. By (4)--(5), this obstruction has
representative
\[
r^{-P}s^{-P}\in H^2(Q,O_Q(-2P,-2P))
\tag{8}
\]
and is nonzero. This assertion does not confuse scalar linearity with
Frobenius semilinearity; the displayed representative has coefficient 1.

To obtain necessity in (1), subtract the ambient diagonal class (b,b)
and put d=a-b. If d is nonzero write d=P u with ell not dividing u.
The transitions g_ij^(P u) define an extension of O_Q(d,0) to X_P,
and its obstruction at X_(P+1) is
\[
u\,F^v(\gamma)\ne0.
\tag{9}
\]
This includes negative u, because integer tensor powers act additively
on the square-zero obstruction. Uniqueness of the extension to X_P,
proved in section 2, prevents replacing it by another extension with a
different next obstruction. Thus O_Q(d,0) cannot extend to any X_n
with n>P. The case P=1 is already (6).

For sufficiency, if P>=n, the coordinate Frobenius morphism
\[
X_n\longrightarrow Q,\qquad [x_i]\longmapsto[x_i^P],
\tag{10}
\]
is defined: q(x_i^P)=q(x_i)^P vanishes on X_n. Its pullback of
O_Q(1,0) restricts to O_Q(P,0). Tensoring with ambient diagonal classes
produces every class in the claimed lattice. The case d=0 is supplied
directly by ambient line bundles. Combining necessity and sufficiency
proves (1), without separate prime cases or a classification of modules.

## 4. Punctured lifting and the actual MCM extension

Automorphisms of Q allow z=(infinity,infinity). Then
\[
U=(A1\times P1)\cup(P1\times A1),
\qquad (A1\times P1)\cap(P1\times A1)=A2.
\]
Each member has quasi-coherent cohomological dimension at most one:
its projection to P1 is affine. The intersection is affine.
Mayer--Vietoris therefore gives H^2(U,F)=0 for every quasi-coherent F.
Apply the units sequence successively to J_j|U. Every punctured lift
extends through the next finite layer, in every characteristic.

Fix n and a punctured line bundle L_n. It has a coherent extension E_n
to X_n. For precision, j_*L_n is quasi-coherent; take a finite-type
quasi-coherent subsheaf restricting to all of L_n, using
[Stacks, Lemmas 28.23.1--2](https://stacks.math.columbia.edu/tag/01PD).
It is coherent since X_n is Noetherian. Coherence of j_*L_n itself is
not assumed. Put M_n=E_n** over O_(X_n).

At the omitted point R=O_(X_n,z) is a two-dimensional Cohen--Macaulay
local ring, being a hypersurface. For any finite R-module N, a finite
presentation gives 0 -> N* -> R^r -> R^s. The image in R^s has depth
at least one whenever it is nonzero: a regular element of R acts
injectively on that submodule. The depth lemma gives depth(N*)>=2
whenever N* is nonzero; if the image is zero, N* is free and the same
conclusion holds. Apply this to N=E_n* to obtain depth(M_n)=2.
The depth lemma used is
[Stacks, Lemma 10.72.6](https://stacks.math.columbia.edu/tag/00LX).
Away from z the double dual agrees with L_n. Thus M_n is MCM everywhere
and generically free of rank one. An omega_(X_n)-double dual gives the
same sheaf because the dualizing sheaf is invertible. This proof does
not invoke a reflexive-equals-CM theorem with unverified reducedness
hypotheses.

The reduction M_n tensor O_Q agrees with L off z. All its torsion is
therefore supported at z and is killed by its Q-double dual. On a smooth
surface the resulting rank-one reflexive hull is a line bundle. It is L:
line bundles on the regular surface Q are determined by their restriction
after removing a codimension-two subset. If M_n were also free at z,
its reduction would give a global invertible extension of L, contradicting
section 2 or 3 when L lies outside the stated image. This proves (2)
and the exact nonfree-locus assertion.

## 5. Geometric interpretation, limitations, and stopping decision

The construction is an actual positive operation on every finite
multiple quadric. In characteristic zero any prescribed ruling imbalance
can be retained as the reduced hull of a rank-one MCM sheaf whose entire
nonfree locus is a chosen single point. Taking that point on C0 also
satisfies the necessary condition that the nonfree locus lie on C0.
In positive characteristic the Frobenius morphism explains precisely
which imbalances instead extend as line bundles to a given finite order:
the successive nonzero obstructions occur at layers ell^v+1.

This blocks an exclusion based solely on the Picard imbalance plus a
punctual defect supported on C0. It does not produce global equation
columns. In particular, it neither constructs nor excludes an STCI.
The missing bridge retains global cohomology, the required presentation
and twists, and an actual column whose common support is exactly C0.

The existing
[double-quadric matrix counterexample](2026-10-31-simultaneous-equation-geometry.md)
has a balanced reduced hull and an explicit ACM two-generator
presentation. The present theorem provides arbitrary reduced hulls but
does not supply those presentation properties. These are complementary
statements, not interchangeable examples.

For L=O_Q(2,6), (6) gives -4 gamma in characteristic zero under the
chosen normalization. The following additional comparison, proposed
during the audit and independently checked here, supplies an explicit
cohomological map from the normal-correction calculation in the
[sextic modification note](2026-10-31-quadric-modification.md).

On C=P1 the basepoint-free pair (s^12,t^12) gives the Koszul sequence
\[
0\to O_C(-2)\xrightarrow{(t^{12},-s^{12})}O_C(10)^2
\xrightarrow{(s^{12},t^{12})}O_C(22)\to0.
\tag{11}
\]
The connecting homomorphism identifies the enlarged normal-correction
quotient H^0(O_C(22))/(s^12 H^0(O_C(10))+t^12 H^0(O_C(10))) with
H^1(O_C(-2)). For w=4s^11t^11, the respective local lifts on s!=0 and
t!=0 are (4t^11/s,0) and (0,4s^11/t). Their difference is
\[
(4t^{11}/s,-4s^{11}/t)
=\frac{4}{st}(t^{12},-s^{12}).
\tag{12}
\]
Thus the boundary of w is plus or minus 4/(st), according to the Cech
orientation. Identify O_C(-2) with omega_C using s dt-t ds. On Q use
the adjunction residue sequence
\[
0\to K_Q\to K_Q(C)=O_Q(-1,1)\to\omega_C\to0.
\tag{13}
\]
Its middle term is acyclic, so H^1(omega_C) -> H^2(K_Q) is an
isomorphism. Under Serre duality its transpose is the restriction
H^0(O_Q) -> H^0(O_C), which sends 1 to 1. Therefore the boundary sends
the standard trace-normalized Laurent generator to the corresponding
generator of H^2(K_Q), up to the boundary sign. To compare with section
2, fix J_1=K_Q by mapping q/x0^2 to dr wedge ds on the x0-chart. These
are the standard trivializations; the gamma in (4) then has trace 1.
There is no degree-three scale factor from the parametrization: on this
chart C is s^3-r=0 and
\[
\operatorname{Res}_C\frac{dr\wedge ds}{s^3-r}=-ds.
\tag{14}
\]
The actual correction space of the sextic note is a subspace of the
enlarged correction space in (11), so its quotient maps to this enlarged
quotient. Compose that map with (11), the chosen omega_C identification,
(13), and J_1=K_Q. This is an explicit linear cohomological comparison
sending the displayed normal-correction obstruction to plus or minus
4 gamma. Hence it agrees with the Picard obstruction for O_Q(2,6) up to
the fixed orientation sign. This is stronger than matching dimensions
or integer coefficients alone. It does **not** establish an equivalence
between the two underlying lifting problems, identify their complete
deformation functors, or extend the sextic exclusion to arbitrary pairs.

The finite-n theorem and exact characteristic-p lattice are approved
as reviewed provisional claims. Global compatibility of the M_n, global
ACM behavior, a two-generator split presentation, and an actual supported
column were not proved and are not part of this PASS. The explicit
linear cohomological comparison (11)--(14) is approved in its stated
scope; equivalence of the lifting problems is not claimed. Stop this bounded test here: no
local classification, larger-degree sequence, or prime-by-prime campaign
is required. The unrestricted characteristic-zero question for C0
remains open.

## 6. Final source and strategy review

Final-state review on October 31, 2026: **PASS** for the written
[source note](2026-10-31-punctual-quadric-lifting.md), including its
finite-order characteristic-p statement and section 5 comparison, the
new [strategy assessment, section 18](2026-10-31-unrestricted-strategy-assessment.md#18-intrinsic-normal-obstruction-finite-thickening-picard-groups-and-punctual-extension),
and the comparison crosslink added to section 4 of the
[preceding sextic note](2026-10-31-quadric-modification.md).
The reviewed source-note SHA-256 is
`2e64aa54372a214e3562983712824042d606123a8f00746eb90a5a9ba94d5267`.

The final wording correctly distinguishes a single support point from
the unmeasured length or amount of defect, local MCM from global ACM,
and punctured compatibility from unproved compatibility of global
extensions. The characteristic-p exponent is correct for X_n=V(q^n):
the least p-power P at least n is sufficient, and a class of exact
p-adic divisibility P fails at X_(P+1). No n-versus-n+1 shift was found.
The comparison is stated as a linear cohomological map on the specified
source obstruction, without equating realization problems. The strategy
recommendation stops the bare Picard argument and identifies the actual
global presentation, normal action, equation column, or quantitative
defect constraint as missing input. It selects no classification or
enumeration and makes no unrestricted conclusion.

No mathematical correction to these final texts was required. Only this
audit was edited by the reviewer; no new research or computation was
performed during final-state review.
