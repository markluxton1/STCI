# Order-three roots: a geometric parameterization and actual sextic lifting

**Status.** Independently reviewed mathematics, including the
completed four-parameter calculation in section 5.
All statements here are in characteristic zero. The spectral parameterization
concerns smooth (2,2) curves with their two fixed ruling coordinates. The
embedded calculation concerns only
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), in the accepted balanced
normal frame. It covers a specified four-parameter slice, including its
two-parameter parity subfamily, not every order-three root or arbitrary pairs.

The [all-power theorem](spectral_pushforward_powers.md) supplies the spectral
splitting and graded constructions; its [scheme continuation](spectral_determinant_schemes.md)
supplies the smooth reduced torsion scheme in characteristic zero.
[R-0007](../results/quadratic_root_obstruction_model.md) supplies the actual
first embedded operator. The [complete sextic source](normalization_conductor_phase2_addendum.md)
and [rank-stratified lifting formulation](rank_strata_and_sextic_lifts.md)
supply the actual degree-six symbol and cubic maps, including the free
\(q^3\) direction. Their unchanged proofs are dependencies, not new claims here.

## 1. All smooth order-three roots from four linear forms

Write \(Z=V(f)\subset\mathbf P^1\times\mathbf P^1\),
\(f=a u^2+buv+cv^2\), and
\(\eta=\mathcal O_Z(0,1)\otimes\mathcal O_Z(-1,0)\).
The coefficients \(a,b,c\) are binary quadratics on the base. Choose four
binary linear forms \(q_0,q_1,q_2,q_3\), up to common scalar, and put
\[
a=q_1q_3-q_2^2,\qquad b=q_1q_2-q_0q_3,\qquad
c=q_0q_2-q_1^2.                                               \tag{1}
\]
The two rows of
\[
H_q=\begin{pmatrix}q_0&q_1&q_2\\q_1&q_2&q_3\end{pmatrix}
\]
annihilate \((a,b,c)^t\). Equivalently, the column \(q\) lies in
the kernel of
\[
T_{f,3}=\begin{pmatrix}a&b&c&0\\0&a&b&c\end{pmatrix}.
\]

Let \(U\subset\mathbf P^7\) be the open where the coefficient matrix
of the four linear forms has rank two, its parameterized line in \(\mathbf P^3\)
avoids the twisted cubic, and the root (1) is smooth. The twisted cubic in
\(\mathbf P^3\) is the rank-one locus of the universal Hankel matrix;
avoiding it means \(H_q\) has rank two at every base point. Then (1)
gives an isomorphism
\[
U\ \simeq\ T[3]_{\rm smooth}\subset\mathbf P^8,                \tag{2}
\]
where the right side has the torsion/determinant scheme structure already
identified in the scheme continuation. In particular this entire locus is
rational of dimension seven. It is nonempty: \(q=(s,-t,0,-s)\) recovers
the negative of the existing smooth order-three root in the all-power account.
This is a parameterization in the fixed frames;
we have not divided by either ruling's automorphism group.

**Proof and coverage.** For \(q\in U\), (1) is basepoint free and the
linear syzygy is nonzero, so the coefficient map \(C_{f,3}\) has a kernel.
The all-power theorem gives \(\eta^3=\mathcal O_Z\). For a smooth
(2,2) curve \(\eta\ne\mathcal O_Z\), so its order is exactly three.

Conversely, that theorem gives
\(W_3=\mathcal O(-1)\oplus\mathcal O(-3)\), hence a unique line
of sections of \(W_3(1)\). A nonzero section is nowhere zero, so its
four linear entries define a rank-two parameterized line. Its shifted
rows cannot be dependent identically: a line cannot lie in a twisted cubic.
Their cross product is therefore nonzero and rationally proportional to
\((a,b,c)\). Because \((a,b,c)\) has no common zero, these local
proportionality functions glue to a global section of \(\mathcal O(0)\).
It is a nonzero constant. Thus the minors have no common zero, the line
avoids the twisted cubic, and (1) recovers exactly the given root.

The forward map is a morphism because the nine quadratic coefficients
in (1) do not vanish simultaneously on \(U\). Locally on the smooth
torsion scheme, an invertible \(7\times7\) minor reduces the eight-by-eight
coefficient matrix to \(\operatorname{diag}(I_7,t)\). Its determinant
equation sets \(t=0\) scheme-theoretically. The kernel is therefore a
line subbundle defining the inverse morphism into \(\mathbf P^7\);
the geometric argument shows that it factors through \(U\).

For the first composite, the universal \(q\) line maps isomorphically
onto that kernel line, so the original projective \(q\) is recovered as
a morphism. For the other composite, choose local frames of the parameter
lines of \(q\) and \(f\). On \(\mathbf P^1\) times this parameter
open, \(H_q\) has rank two everywhere. Its minors and \((a,b,c)\)
generate the same kernel line after the degree-two twist. Their ratio is
a unit, and \(\operatorname{pr}_*\mathcal O_{\mathbf P^1\times T}
=\mathcal O_T\) makes it a unit from the parameter base. Thus the two
projective coefficient maps agree. This proves (2) scheme-theoretically,
without discarding nilpotent test parameters. We retain characteristic
zero as the scope of this account. \(\square\)

This replaces a determinant equation with a line and its minors. It also
constructs the spectral trivialization and the graded CI family through
the kernel construction already proved for all powers. It does not make
the actual ambient lifting operator invariant under arbitrary coordinate
changes in the two rulings.

## 2. A complete first-compatibility calculation on a parity slice

In the fixed affine base coordinate \(z=t/s\), take
\[
q=(1,z,B,Cz),\qquad
f_{B,C}=(Cz^2-B^2)u^2+(B-C)zuv+(B-z^2)v^2.                    \tag{3}
\]
The entries of \(q\) are homogenized to degree one; for example its first
entry is \(s\). This is a selected affine plane inside (2), not a normal
form for all embedded roots. Its smooth open is exactly
\[
BC(C-B)(C-9B)\ne0.                                           \tag{4}
\]
Indeed the direction discriminant is
\[
\Delta(z)=4Cz^4+(C^2-6BC-3B^2)z^2+4B^3,
\]
and
\[
(C^2-6BC-3B^2)^2-64B^3C=(C-B)^3(C-9B).
\]
When \(BC\ne0\), this quartic has four distinct projective roots exactly
when the other two factors are nonzero; the coefficients of \(f\) then
have no common base zero. If \(B=0\) or \(C=B\), the root has a
base fiber. If \(C=0\) and \(B\ne0\), it is singular at
\(([s:t],[u:v])=([0:1],[1:0])\): in the local coordinates
\(x=s/t,y=v/u\), its equation is
\(-B^2x^2+Bxy+(Bx^2-1)y^2\), with no linear term. The case
\(C=9B\ne0\) has a repeated branch root and is singular.

Let \(d_f\) be the first Cech obstruction from R-0007, with target
coefficients \(z^{-4},\ldots,z^{-1}\) in each cubic direction monomial.
Let \(A_f\) send the twelve Laurent coefficients of
\(h=h_u(z)u+h_v(z)v\), supported on \(z^{-6},\ldots,z^{-1}\), to
the same middle coefficients of \(fh\). First compatibility means
\(A_fh=d_f\). This is the operator used for the failed fixed example
in the [preceding account](spectral_pushforward_powers.md#6-testing-this-example-in-the-actual-embedding).

The whole four-dimensional dual obstruction space on (4) has the basis
\(q,zq,z^2q,r\), where
\[
r=(-z^3,\ B^2-2Bz^2,\ B(C-B)z-Cz^3,\ B^3+C(C-3B)z^2).         \tag{5}
\]
To verify completeness, both \(q\) and \(r\) are syzygies of
\(T_{f,3}\), and their six wedge coordinates are
\[
(c^2,-bc,b^2-ac,ac,-ab,a^2).
\]
These never vanish simultaneously on a basepoint-free root. Hence they
give the splitting \(W_3=\mathcal O(-1)\oplus\mathcal O(-3)\),
and the displayed four sections form a basis of \(H^0(W_3(3))\).
The pairing is the coefficient of \(z^{-1}\) in the scalar product.
Thus this is the full cokernel dual, not a selection of necessary tests.

Put
\[
\begin{aligned}
P_1&=(B-2)(3B^2+11B+C+12),\\
E_2&=9B^4+3B^3C-12B^2C-60B^2-16BC-72B+4C^2+72C,\\
R&=-9B^4+9B^3C-30B^3-8B^2C+2BC^2-24BC+72B+24C.
\end{aligned}
\]
The four pairings with \(d_f\) are
\[
(0,P_1/4,0,R/8),\qquad R-E_2=-2(3B-C)P_1.                    \tag{6}
\]
Consequently first compatibility on (4) is exactly \(P_1=E_2=0\).

There are precisely six geometric points:

* \((B,C)=(2,6)\) and \((2,-10)\);
* the four roots of
  \(P(B)=3B^4-22B^3-92B^2-88B+48\), with
  \(C=-3B^2-11B-12\).

For coverage, when \(B=2\) one has \(E_2=4(C-6)(C+10)\).
On the other factor of \(P_1\),
\(E_2=-3(B+2)P(B)\). The point \(B=-2,C=-2\) is outside
(4). The exact gcd checks \(\gcd(P,P')=1\) and
\(\gcd(P,BC(C-B)(C-9B))=1\), after substituting for \(C\),
give four distinct smooth points. None has \(B=2\).

These are positive first-lifting examples with exact order-three spectral
class. Under the accepted operator they define embedded Cartier lifts through
the first tested order. They do not assert all-orders lifting or any global
equation. The two rational points, in particular, are
\[
\begin{aligned}
f_{2,6}&=(6z^2-4)u^2-4zuv+(2-z^2)v^2,\\
f_{2,-10}&=(-10z^2-4)u^2+12zuv+(2-z^2)v^2.
\end{aligned}
\]

## 3. What the complete actual sextic source realizes

Use the accepted 23-dimensional source \(V=H^0(\mathcal I_{C_0}^2(6))\)
(sheaf powers) with matrices
\[
M:V\to k^{33},\qquad N:V\to k^{40},\qquad J:k^{33}\to k^{11}.
\]
Here \(M\) is the quadratic symbol, \(N\) its cubic layer, and
\(\ker J=\operatorname{im}M\). Their exact bases and rational entries
are in the [accepted source data](../computations/conditional_2_12_symbol_map_2026_10_20.json).
The source includes the kernel direction \(q^3\) of \(M\), where this
\(q\) denotes the ambient quadric equation, not the syzygy vector above.

For a root (3), an actual sextic with nonzero leading multiplier must have
symbol \(\alpha f\), with \(0\ne\alpha\in H^0(\mathcal O(8))\).
Let \(A(f):k^9\to k^{33}\) be multiplication by \(f\). The symbol
condition is \(JA(f)\alpha=0\).

For the four quartic-parameter points, a nine-row minor of \(JA(f)\),
on rows \(0,1,2,3,4,5,6,8,10\) using zero-based source indexing, is
\[
32B^3(B-2)(B+2)(3B^2+11B+12)
(49B^4+348B^3+1012B^2+1392B+784)^2.                           \tag{7}
\]
Its gcd with \(P(B)\) is one. Thus at every one of these four points
the symbol map has rank nine and permits no nonzero \(\alpha\).

At the two rational points the rank is eight. The unique nonzero multiplier
up to scalar is respectively
\[
\alpha_+=16-12z^4+9z^8,\qquad
\alpha_-=16+64z^2+276z^4-80z^6+25z^8.                         \tag{8}
\]
Thus actual sextic symbols do exist here. The remaining failure occurs in
the cubic layer and cannot be inferred from the symbol alone.

The unique first correction \(h\) gives the accepted normalized local
cubic corrections
\[
\begin{aligned}
G_+&=-\tfrac94u^3-\tfrac98zu^2v-\tfrac{27}8uv^2+\tfrac3{16}zv^3,\\
G_-&=-\tfrac{25}4u^3-\tfrac{225}8zu^2v+\tfrac{325}8uv^2-\tfrac{45}{16}zv^3.
\end{aligned}                                                \tag{9}
\]
These are extracted from the full embedded transition in the
[accepted second-model generator](../computations/generalization_quadratic_root_global_second_model.py),
not chosen as independent cubic targets. All permitted cubic modifications
are retained by the multiplication map
\(\mu_f:H^0(\mathcal O(7))^2\to k^{40}\), and the full actual
lifting system is
\[
L=\begin{pmatrix}M&0\\N&-\mu_f\end{pmatrix},\qquad
L\binom{x}{\ell}=t=\binom{\alpha f}{\alpha G_\pm}.             \tag{10}
\]
It has 73 rows and 39 columns. In particular no choice of the free ambient
quadric cube has been discarded.

Here are complete left certificates for inconsistency. Only nonzero entries
of each row vector \(\lambda\) are listed, as \(\text{row}:\text{value}\):

```
C=6:
4:108, 8:-36, 10:24, 16:-108, 20:108,
33:81, 37:-36, 39:-24, 41:-16, 44:-108, 55:108
lambda L=0; lambda t=-2916.

C=-10:
2:625, 6:-125, 8:-50, 10:-20, 14:-625, 18:125, 20:150,
35:125, 37:-50, 39:20, 41:-8, 53:625
lambda L=0; lambda t=-86250.
```

Indices are zero-based: the first 33 rows list the three quadratic direction
coefficients with base degrees 0 through 10; the next 40 list the four
cubic direction coefficients with base degrees 0 through 9. The multipliers
are normalized as in (8). The nonzero values exclude every nonzero scalar
multiple as well. Hence none of the six smooth first-compatible points in
this slice has an actual sextic compatible through this cubic stage.

## 4. Scope, constructive use, and next question

The intrinsic torsion condition, the first embedded lift, the actual sextic
symbol, and its cubic lift are distinct conditions with concrete geometric
objects between them. The slice constructs six roots at the second stage
and two realizable symbols at the third. Its final failure does not erase
those objects, nor does it establish failure everywhere on the rational
seven-dimensional parameter space (2).

Under all the actual saturation, movement-two, joint-generation and full
generic coprime-CI hypotheses in [R-0013](../results/saturated_actual_generator_movement.md),
[R-0014](../results/movement_two_six_rows.md) and
[R-0006](../results/actual_ci_smooth_root_bridge.md), exact order three
retains only the numerical row \((r,s;a,b)=(2,12;6,16)\).
Our slice cannot supply its required compatible sextic. No assertion is
made about roots outside the slice, singular roots, nonsaturated patterns,
other generator patterns, or arbitrary pairs. These tests also do not
produce a degree-sixteen mate or decide properness or residual support.

Section 5 closes the larger selected slice \(q=(1,z,Az+B,Cz+D)\),
including its omitted parameter boundaries. Further selected slices would
still leave most of (2) uncovered. The [research selection guide](../RESEARCH_DECISION_GUIDE.md)
therefore recommends actual octic constructions on first-compatible roots
and, separately, a full-parameter sextic incidence. Independently, (2)
describes graded (2,3), (2,6) and (2,12) families without requiring a
global STCI application.

## 5. Completion of the four-parameter slice

Restore the mixed coefficients and write
\[
q=(1,z,Az+B,Cz+D),\quad
\begin{aligned}
a&=(C-A^2)z^2+(D-2AB)z-B^2,\\
b&=Az^2+(B-C)z-D,\\
c&=Az+B-z^2.
\end{aligned}                                                 \tag{11}
\]
This is an affine four-dimensional slice of the seven-dimensional space (2),
not a normal form modulo allowed ambient symmetries.

**Claim.** On the smooth-root open of (11), exactly twenty-four geometric
points pass the first embedded test. Six are the parity points above;
eighteen have \(A\ne0\). None has an actual compatible sextic: twenty-two
fail the symbol test, and the two rational parity points fail cubic lifting.
This is a statement about geometric points; no intersection multiplicity
or scheme length is asserted.

Put
\[
r=(0,c^2,-bc,b^2-ac)-z^3q.
\]
Every entry of \(r\) has degree at most three, and \(q\wedge r\) again
equals the six Plucker coordinates in section 2. Thus
\(q,zq,z^2q,r\) give the complete first-obstruction dual basis on the
smooth open. Denote their pairings with the accepted \(d_f\) by
\(F_0,F_1,F_2,F_3\). In particular
\[
\begin{aligned}
8F_0={}&18AB^2+16AB+6AC-12A-9BD+6CD-16D,\\
8F_1={}&16A^2+10AD+6B^3+10B^2+2BC-20B-4C+3D^2-48,\\
4F_2={}&20AB+36A+(3B-2)D.
\end{aligned}                                                 \tag{12}
\]
The [exact verifier](../computations/order_three_four_parameter_slice.py)
derives all four pairings directly from the accepted operator, including
\(F_3\), and checks the following elimination identities.

For \(A\ne0\), \(F_2=0\) excludes \(B=2/3\) and forces
\(D=D_B=-4A(5B+9)/(3B-2)\). Set
\[
\begin{aligned}
N&=9B^3+32B^2+96B+100,& Q&=93B^2+431B+584,\\
H&=60B^3+333B^2+718B+556,& C_B&=N/(17B+38),\\
X&=-\frac{(B-2)(3B-2)^2H}{4(17B+38)Q}.&&
\end{aligned}
\]
Then
\[
F_0|_{D=D_B}=\frac{3A(N-(17B+38)C)}{4(3B-2)},\qquad
F_1|_{D=D_B,C=C_B}=\frac{Q(A^2-X)}{(3B-2)^2}.                 \tag{13}
\]
At \(B=-38/17\), \(N=-271284/4913\ne0\), so the next division
loses no solution. At \(Q=0\), the remaining numerator cannot vanish,
because \(\gcd(Q,(B-2)(3B-2)^2H)=1\). Hence (13) forces
\(C=C_B\) and \(A^2=X\), with all denominators nonzero.

Define
```
P9(B) = 15849 B^9 + 144531 B^8 + 341525 B^7 - 1138436 B^6
        - 8388388 B^5 - 16074040 B^4 + 8264096 B^3
        + 80572544 B^2 + 119321280 B + 58870912.
```
The final residue becomes
\[
F_3|_{D=D_B,C=C_B,A^2=X}
 =\frac{3P_9(B)}{8(17B+38)^2Q}.                              \tag{14}
\]
Exact gcds show that \(P_9\) is squarefree and is coprime to
\((B-2)(3B-2)(17B+38)QH\). Its nine distinct roots therefore give
exactly eighteen points, two nonzero square roots of \(X\) at each.
Conversely (13)--(14) and \(F_2=0\) verify all four equations at each point.
They give distinct projective roots: the fixed coefficient \(c_2=-1\)
fixes the scalar, while \(c_0=B,c_1=A\) distinguish the points.

The branch \(A=0,D\ne0\) gives \(B=2/3,C=11/3\) from
\(F_2,F_0\), after which
\[
F_1=(27D^2-584)/72,\qquad F_3=(21D^2+244)/24.
\]
Their numerators are coprime, so this branch is empty. The remaining
\(A=D=0\) branch is exactly the already reviewed parity slice.

For smoothness, the direction discriminant \(\Delta=b^2-4ac\) satisfies
\[
\operatorname{disc}_z\Delta=-256\mathcal U^3\mathcal V,
\]
where
\[
\begin{aligned}
\mathcal U={}&A^3D-A^2BC+3ABD-ACD+B^3-2B^2C+BC^2-D^2,\\
\mathcal V={}&27A^3D-27A^2BC+81ABD-27ACD
              -81B^2C+18BC^2-C^3-27D^2.
\end{aligned}
\]
After the substitutions above, these are rational functions of \(B\).
Their numerators and denominators are coprime to \(P_9\), as are those
of the leading coefficient \(4C_B-3X\). Thus every one of the eighteen
points has four distinct finite branch points and no missing infinity
case. A common base zero of \(a,b,c\) would give a repeated discriminant
zero; none occurs. The resulting finite flat double cover is smooth.
The parameterization in section 1 then gives exact order three.

Finally form the same multiplier matrix \(JA(f)\) used in section 3.
Take its nine-row minor on rows \(0,1,2,3,4,5,6,8,10\). The verifier
computes this determinant in
\[
\mathbf Q(B)[A]/(A^2-X),\qquad C=C_B,\ D=D_B,
\]
using division-free characteristic-polynomial arithmetic, without assuming
this quadratic algebra is a field. The determinant is independent of \(A\),
with a degree-32 numerator and denominator \((17B+38)^6Q^5\). Both are
coprime to \(P_9\). Thus the minor is nonzero at **all eighteen** points,
so no nonzero sextic multiplier exists there. The old six-point certificates
complete the stated twenty-two symbol failures and two cubic failures.

The interrupted investigation is therefore closed at its declared first-lift
and actual-sextic level. No cubic calculation is needed for the eighteen new
points, and no second-root obstruction or degree-sixteen mate is computed.

## Evidence and independent review

The compact [exact verifier](../computations/order_three_sextic_slice.py)
reuses the accepted operator and source matrices without their output-writing
footers. It verifies the dual basis identities, all first-compatibility
equations, complete slice factorization and smoothness gcds, the minor (7),
the multipliers, the actual corrections (9), and both all-lifts witnesses.
It is not a search log or a replacement for the coverage proof above.

Independent review on 2026-10-31 by `review_order_three_geometry`
(GPT-6.1 Sol, high reasoning) reconstructed section 1 from the spectral
sequences, checked the converse's basepoint and twisted-cubic boundaries,
and supplied the relative inverse argument retaining nilpotent parameters.
The final written section passed after two wording clarifications. No
computation was needed for that review.

Independent review by `review_order_three_slice` (GPT-6.1 Sol, high reasoning)
reconstructed the residue pairings directly, checked the complete smooth
slice and all source conditions, inspected and executed the verifier using
SymPy 1.14.0, and independently checked the source ranks and the retained
ambient quadric-cube column. It found and corrected the earlier boundary
description at \(C=0,B\ne0\): that curve is singular and integral, not
reducible. The corrected boundary explanation and exact certificates passed.
The verifier reports the complete slice count, four symbol failures, and
the two nonzero all-lifts pairings displayed above.

The existing sources' geometric identifications and full-source coverage are
reused; checking their matrices here does not rederive that coverage. The
status of R-0006, R-0007 and the numerical restrictions is unchanged,
and this contribution itself retains the review scope stated here.

For section 5, `review_order_three_slice` independently reconstructed all four
residues from the ambient vector field, solved the elimination, checked every
affine denominator stratum and base infinity, and reviewed the written
twenty-four-point claim and new checker. The review passed without a material
correction. It also recomputed the decisive source minor by signed subset
expansion over \(\mathbf F_{65521}[B]/(P_9)[A]/(A^2-X)\), independent
of the producer's characteristic-polynomial arithmetic. All denominators
were units and the determinant was a unit, corroborating the exact rational
gcd certificate. This does not assert coverage of the projective closure of
the selected affine slice or a scheme-theoretic intersection length.

The lead and reviewer executed `order_three_four_parameter_slice.py` with
SymPy 1.14.0 successfully. The lead also reran `order_three_sextic_slice.py`;
all parity certificates passed. The temporary interpreter was recreated with
the existing pinned dependency after the earlier temporary environment had
expired; no repository dependency was added. Record validation,
local Markdown links including anchors, and whitespace checks passed at
closeout. No second-root or mate computation is reported.
