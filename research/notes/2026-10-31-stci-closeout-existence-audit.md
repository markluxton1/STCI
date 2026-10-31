# Closeout audit: the elliptic double-lift construction

October 31, 2026. Independent reviewer: `existence_audit`.
Status: **PASS for the fixed construction and its rejection; the full
five-parameter support and descent loci remain OPEN.** Reviewed provisional
work, with no canonical promotion. The curve is
\(C_0=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field of
characteristic zero.

This audit reconstructs the geometric implications and inspects the
exact source and saved final output. It does not rerun inherited accepted
proofs. The principal evidence is the
[existence proposal](2026-10-30-stci-game-existence.md), its
[exact script](../computations/stci_game_existence_2026_10_30.m2), and its
[complete output](../computations/stci_game_existence_2026_10_30.txt).
The earlier [geometry review, section 4](2026-10-30-stci-game-geometry-review.md)
already independently checks the ambient involution and pencil action;
those checked identities are used as premises. The balanced conormal
splitting is promoted [R-0020](../results/quartic_conormal_characteristic_jump.md).
The [freedom formula and forced-quadric theorem](2026-10-28-stci-search-freedom.md)
have their separate independent audit and are used within their stated
sheaf-power scope.

## 1. Final verdicts and evidence of completion

| Claim | Verdict and literal scope | What establishes it |
| --- | --- | --- |
| Order-four torsion and global coordinate sections | **PASS.** The specified \(E,T,L,M\) give actual quadratic lifts of four sections, not just rational normal data. | Divisor calculation below; four exact section-identity solves and `EXACT_QUADRATIC_LIFTS_OF_ELLIPTIC_DEGREE_TWO_SOURCE_PASS`. |
| The fixed member \(\mu=2,\rho_j=0\) is smooth, basepoint free, finite, and birational to an integral degree-eight image | **PASS.** This is a single actual carrier. | Projective saturation is the unit ideal; source smoothness assertion; one implicit generator of degree eight and `FIXED_INPUT_IMAGE_DEGREE_TEST_COMPLETED`. |
| Extra inverse scheme | **PASS.** Affine \(Q_0=1\) length 24 corresponds to projective off-\(\Gamma\) length 12. Neither distinctness nor reducedness is asserted. | Dimension zero, degree 24, and terminal fixed-support marker. |
| No mate for that fixed carrier in any positive degree | **PASS.** An effective Cartier divisor on its smooth normalization cannot have isolated zero support away from its curve support. | Full inverse scheme and the divisor argument in section 3. |
| Normal order two; degree-twelve vertical first-symbol divisor; horizontal class \((6,2)\) | **PASS for the same fixed carrier.** No full-family assertion. | Both normal charts are inspected in the script; saved output gives order 2, finite gcd degree 12, infinity order 0. |
| Irreducible horizontal root with elliptic normalization | **PASS for the same fixed carrier.** The root has arithmetic genus 5 and normalization genus 1. | Saved squarefree odd discriminant part has degree 4; no identification of singular root and its normalization. |
| Images of the entire extra inverse scheme lie in the vertical divisor | **PASS as scheme-theoretic containment.** Equality of image schemes, twelve distinct images, and multiplicity one are not proved. | The homogenized vertical polynomial is zero in the full extra-scheme quotient and \(U_0\) is invertible there. |
| Deck involution excludes every smooth source member | **REJECTED implication.** It acts on the ambient pencil by \(\mu\mapsto-1/\mu\); only \(\mu=\pm i\) are invariant. | Independent exact matrix identities in the earlier geometry review. |
| Degree-five mate filter | **PASS on the verified normal-order-two, irreducible-quadratic locus only.** It applies to the fixed member but is not an untested full-family filter. | The forced-quadric theorem plus generic local intersection length. |
| Five-parameter support locus is empty, or has a descending power | **OPEN.** Neither calculation has been completed. | The saved computation fixes all five parameters before forming the inverse ideal. Section 6 gives the precise remaining problem. |

The saved output ends with
`EXISTENCE_SOURCE_FIXED_INPUT_AND_NORMAL_GEOMETRY_EXACT_CHECKS_PASS`.
It follows all image, symbol, discriminant, and scheme-containment stages.
Thus these stages are completed calculations rather than inferred agent
intent. Conversely there is no family-wide output marker or universal
parameter elimination in the script. Its fixed specialization cannot
be promoted to an empty five-parameter locus.

## 2. Why the torsion construction gives an actual map

Write
\[
 E:y^2=x^3-x,\quad T=(i,1-i),\quad P=(0,0),\quad
 M=\mathcal O_E(4O),\quad L=\mathcal O_E(O+T).
\]
The curve is smooth. The tangent slope at \(T\) is \(-1-i\), and its
line is \(y+(1+i)x=0\). Its third intersection is \(P\), so
\(2T=P\); since \(P\ne O\) has order two, \(T\) has order four.
In \(\operatorname{Pic}^0(E)\), the discrepancy
\(L^2M^{-1}\) is the nonzero class \(2T\). Hence
\(L^4=M^2\) and \(L^2\ne M\).

The degree-two function
\[
 A=(y+1-i)/(x-i)
\]
has simple poles at \(O,T\); its apparent pole at \(-T\) cancels.
For
\[
 \phi=(y+(1+i)x)^2/x
       =x^2+2ix-1+2(1+i)y
\]
the tangent divisor is \(2T+P-3O\), while
\(\operatorname{div}(x)=2P-2O\). Therefore
\(\operatorname{div}(\phi)=4T-4O\). The four functions
\(\phi A^j\), \(j=0,1,3,4\), have no poles outside \(O\), and
their pole orders at \(O\) are at most eight. They are actual sections
of \(M^2\). At \(T\) their orders are \(4-j\); at \(O\), as
sections of \(8O\), their orders are also \(4-j\). There is no common
zero. Their ratios give \([1:A:A^3:A^4]\), including the two pole
points after changing local frame. Thus the marked map is a degree-two
morphism onto \(C_0\).

The embedding by \(M\) has coordinates \(Z=(1:x:y:x^2)\) and ideal
\[
 Q_0=Z_0Z_3-Z_1^2,\qquad
 Q_1=Z_2^2-Z_1Z_3+Z_0Z_1.
\]
The script solves each identity
\(f_j(x,y)(x-i)^j=\phi(y+1-i)^j\) modulo
\(y^2-x^3+x\) in the eight-dimensional basis of \(H^0(E,8O)\).
Each solve has an exact assertion, and the displayed coefficient rows
in the proposal agree with the printed global quadrics. This is the
geometric role of the linear algebra: it constructs sections of the
embedding bundle and then genuine ambient quadrics. It makes no
conductor-descent claim.

On a smooth member \(S_\mu=V(Q_1+\mu Q_0)\), set
\(\Gamma=E\) and \(H=\mathcal O_{S_\mu}(2)\). Over the algebraic
closure \(S_\mu\simeq\mathbf P^1\times\mathbf P^1\), and
\(\Gamma\sim H=(2,2)\). Every lift of the four fixed restricted
sections to this surface is \(U_j=V_j+\rho_jQ_0\): the kernel of
restriction on quadrics modulo \(Q_1+\mu Q_0\) is the one-dimensional
span of \(Q_0\). This proves completeness of the four affine lifting
parameters for these fixed sections and this pencil; it does not
classify all elliptic sources. Promoted
[R-0002](../results/cartier_singleton_lift.md) requires an inverse curve
mapping isomorphically to \(C_0\), so it does not classify this degree-two
inverse model.

## 3. The fixed finite normalization and its decisive failure

At \(\mu=2,\rho_j=0\), the script saturates the source-plus-coordinate
ideal by the irrelevant ideal and obtains \((1)\). The coordinate
sections therefore define a morphism. Its pullback of the target
hyperplane bundle is \(H\), which is ample. A positive-dimensional
fiber would contain a curve on which \(H\) has degree zero, impossible;
the projective morphism is finite. The source is smooth and integral.

The kernel of the target ring map is prime because its image is a
subring of the integral source ring. The saved kernel computation has
one generator of degree eight. Since \(H^2=8\), the degree formula
\(8=\deg(f)\deg(f(S_2))\) gives generic degree one. Consequently the
smooth source is the normalization of this actual integral octic.
These statements are logically separate from the inverse-support test.

The latter test uses all four standard generators of \(I_{C_0}\), not
just the containing quadric. Its affine ideal is
\[
 J_2=(Q_1+2Q_0,Q_0-1,I_{C_0}(V))\subset\mathbf Q(i)[Z_0,Z_1,Z_2,Z_3].
\]
The saved quotient is zero-dimensional of length 24. On the complement
of \(\Gamma\), imposing \(Q_0=1\) on the affine cone gives a finite
étale \(\mu_2\)-torsor over the projective complement: every scalar
orbit has two representatives, and characteristic zero makes the
action free and étale. Length therefore divides by two, even for
nonreduced schemes. The projective extra inverse scheme has length 12.

If an ambient mate \(G_b\) existed, its nonzero pullback would be a
section of \(bH\) with zero support exactly the full inverse image of
\(C_0\). This support contains \(\Gamma\) and the isolated extra
scheme. A principal nonzerodivisor on the smooth surface defines an
effective Cartier divisor with pure codimension-one support. It cannot
have those isolated zero points. This excludes every positive mate
degree on this image. It neither requires birationality for the
contradiction nor excludes any other parameter choice.

Geometrically, the fixed construction succeeds at producing the desired
elliptic double inverse on a genuine normalization, but also produces
additional sheets over finitely many target points. Increasing the mate
degree cannot cure the inverse support of an already fixed morphism.

## 4. What the first-normal calculation measures

The implicit octic is substituted in the finite chart
\((x_0,x_1,x_2,x_3)=(1,t,t^3+n,t^4+m)\). The least total
\((n,m)\)-degree is two. The three quadratic coefficients have a gcd
of degree twelve in \(t\). The separate infinity chart
\((s^4+m,s^3+n,s,1)\) has coefficient-gcd order zero at \(s=0\).
Thus the vertical saturation divisor on the whole \(C_0\simeq\mathbf P^1\)
has degree twelve. This is an actual common divisor of the coefficient
sections, independent of a locally invertible change of normal frame.

By R-0020 the full quadratic symbol is of class \((18,2)\) on the
balanced exceptional \(\mathbf P^1\times\mathbf P^1\). Removing the
vertical divisor leaves a saturated horizontal root of class \((6,2)\).
The coefficient gcd and the horizontal root are different geometric
objects. The latter has arithmetic genus \((6-1)(2-1)=5\).

The exact characteristic-zero squarefree decomposition of its
discriminant has odd part of degree four. Over the algebraically closed
ground field this part is squarefree, and the resulting quadratic
function-field extension is branched at four points of the base
\(\mathbf P^1\), with no additional odd branch at infinity. It is
irreducible and has normalization genus one by Riemann--Hurwitz. The
singular horizontal root therefore has total delta invariant four.
The calculation is not a smooth-root assertion: its vertical defect and
horizontal singularities must be retained in any application of a
root obstruction.

Let \(h(t)\) be the printed monic vertical gcd and
\(\widetilde h(W_0,W_1)=W_0^{12}h(W_1/W_0)\). The script checks
\(J_2+(V_0)=(1)\) and then checks
\(\widetilde h(V_0,V_1)=0\) in the full quotient by \(J_2\).
Because \(V_0\) is invertible there, this proves that the morphism from
the entire extra inverse scheme to the affine target curve factors
through the divisor \(h=0\). The factorization descends through the
free \(\mu_2\)-cover. It is **scheme-theoretic containment** of its
target image in the vertical divisor. Matching the two degrees twelve
does not show equality: several source points can have the same image,
and image lengths and multiplicities have not been computed.

This containment is a useful diagnostic for the independent obstruction
program: on this example the unwanted inverse sheets are detected by
the first-symbol boundary. It is not a theorem that every vertical
coefficient divisor produces a residual curve or isolated inverse
support, and it supplies no universal residual floor.

## 5. Symmetry and the scoped degree-five filter

The deck involution is \(P\mapsto T-P\). It preserves \(M\), since
\(4T\sim4O\), so it extends linearly to the ambient projective space.
The independently reviewed matrix satisfies
\[
 \mathsf M^2=8I,\qquad Q_0(\mathsf M Z)=8iQ_1(Z),\qquad
 Q_1(\mathsf M Z)=-8iQ_0(Z).
\]
It sends \(S_\mu\) to \(S_{-1/\mu}\). Only \(\mu=\pm i\) are
fixed. In particular the deck action on \(E\) does not preserve \(S_2\).
The old argument in which a degree-one inverse-curve symmetry forces
a global source involution therefore has a failed hypothesis here.
Even on an invariant pencil member, invariance of the actual four
coordinate sections would need its own check before deducing the map's
generic degree.

Suppose an actual degree-eight member has exact normal order two with
irreducible quadratic first form over \(k(C_0)\). A degree-five mate has
normal order at least one. If its order is one, its linear initial form
is coprime to that quadratic, giving generic local intersection length
two. Sole support would require \(8\cdot5/4=10\), impossible. If its
order is at least two, the reviewed global freedom theorem forces a
factor of the unique containing quadric \(q\), because \(5<3\cdot2\).
That factor also forbids sole support: on \(q\simeq\mathbf P^1\times\mathbf P^1\)
the octic has class \((8,8)\), which cannot be supported on multiples
of \(C_0\) of class \((1,3)\). There is genuine residual support in
its intersection with \(q\). Thus the filter is valid on this verified
normal-form locus. The saved fixed member satisfies it, but is already
rejected by the stronger full-support failure.

This reasoning does not remove the degenerate-leading loci of the
five-parameter family. Two normalization branches can share a tangent,
and the implicit carrier's order or quadratic factorization can change.
One must compute the actual first form on a proposed stratum before
applying this degree-five filter. The first-degree arithmetic test is
necessary, not a substitute for support or descent.

## 6. Continuation-ready endpoint for the surviving family

No new large calculation was launched for this audit. The saved exact
fixed-member calculation already reaches its endpoint; the universal
five-parameter elimination has not been executed. In particular there
is no claim that a generic rank or a finite specialization exhausts it.

The literal family is over
\[
 B=\mathbf Q(i)[\mu,\rho_0,\rho_1,\rho_3,\rho_4],\qquad
 R=B[Z_0,Z_1,Z_2,Z_3],\qquad
 U_j=V_j+\rho_jQ_0,
\]
with the four \(V_j\) given in the proposal and exact script. The
determinant of a symmetric matrix for \(Q_1+\mu Q_0\) is a nonzero
scalar multiple of \(\mu(\mu^2-1)\); invert
\(\delta=\mu(\mu^2-1)\) to retain smooth source quadrics. The pencil's
member at infinity is singular and is outside this smooth-source
problem.

For each geometric parameter point \(p\), the admissibility conditions
and first unresolved test are precisely:

1. **Basepoint freedom:**
   \(\big((Q_1+\mu Q_0,U_0,U_1,U_3,U_4):
   (Z_0,Z_1,Z_2,Z_3)^\infty\big)_p=(1)\), with saturation computed
   in the specialized projective fiber. The resulting morphism is finite
   by ampleness.
2. **Birational octic image:** the kernel of
   \(k[W_0,W_1,W_2,W_3]\to
   k[Z]/(Q_1+\mu Q_0)\), \(W\mapsto(U_0,U_1,U_3,U_4)\), has
   degree-eight image. Then the finite map has degree one. Other image
   degrees are excluded from this octic-normalization subproblem, rather
   than silently reclassified as octics.
3. **Full inverse support, still unresolved:** in the specialized affine
   ring require
   \[
   J_p=(Q_1+\mu Q_0,Q_0-1,
   U_0U_4-U_1U_3,
   U_1^3-U_0^2U_3,
   U_1^2U_4-U_0U_3^2,
   U_3^3-U_1U_4^2)_p=(1).
   \]
   This is exactly the absence of inverse points outside \(\Gamma\),
   including nonreduced points. There is no need for a further saturation
   by \(Q_0\) in this chart. Equivalently use the projective homogeneous
   inverse ideal saturated by \(Q_0^\infty\) and by the irrelevant
   ideal. An elimination computed over the fraction field of \(B\)
   would only decide the generic fiber and may miss special absorption
   loci; retain fiberwise constructible rank/support strata.
4. **Descending mate on a surviving stratum:** for \(b>0\), require
   \[
   Q_0^b\in\operatorname{span}_k
   \{U_0^{e_0}U_1^{e_1}U_3^{e_3}U_4^{e_4}:\sum e_j=b\}
   \quad\text{in }k[Z]/(Q_1+\mu Q_0).
   \]
   This is an exact global equation test, including conductor descent.
   It constructs an actual mate if it holds; it also forces the absence
   of extra inverse support, because its pullback zeros are exactly
   \(b\Gamma\). The equivalence for an admissible sole-support mate
   follows from \(\Gamma\sim H\) and \(H^2>0\): a zero divisor
   supported on \(\Gamma\) and linearly equivalent to \(bH\) must be
   \(b\Gamma\).

The descent matrix is completely finite at a chosen degree. Reduce
degree-\(2b\) forms by the monic rule
\[
 Z_2^2=Z_1Z_3-Z_0Z_1-\mu(Z_0Z_3-Z_1^2).
\]
The monomials of degree \(2b\) with \(Z_2\)-exponent at most one form
a basis of size \((2b+1)^2\). Use the above monomials in the \(U_j\)
as columns and append the coefficient column of \(Q_0^b\). For
\(b=6\) this is a \(169\times84\) matrix and a
\(169\times85\) augmented matrix; for \(b=8\), sizes are
\(289\times165\) and \(289\times166\). The exact membership
condition is equality of their ranks. Retain every rank stratum: on
rank \(s\), impose the augmented \((s+1)\)-minors and invert at least
one \(s\)-minor of the original matrix. Inverting one convenient
maximal minor is not an exhaustive test.

The completed output is only \(p=(2,0,0,0,0)\), with \(J_p\) length
24 in the affine cover and the diagnostics above. The first unresolved
condition is whether the support-unit locus in item 3 meets the smooth,
basepoint-free, birational locus. No degree-six or degree-eight universal
descent matrix has been executed. A continuation should first bound its
resources explicitly (for example one exact fiber or one prescribed
parameter slice, with fixed wall-clock and memory limits), save partial
output, and stop without calling a truncated elimination an endpoint.

## 7. The completed adversarial exchange and its remaining implication

The existence side's strongest justified proposal changes the inverse
curve itself: a degree-two elliptic cover with a controlled nontrivial
two-torsion discrepancy. It has genuine global coordinate lifts and an
actual smooth normalization model. The fixed member then fails before
descent, by isolated extra inverse support. The non-existence side
correctly accepts that this does not fall under the degree-one inverse
classification, and that a defect-free ordinary-root argument cannot
discard the observed vertical first-symbol divisor.

The constructive challenge is to absorb the extra inverse support into
\(\Gamma\) while preserving a morphism and birational octic image,
then obtain the descending pure power. It is not to increase the mate
degree on the rejected fixed carrier. The independent obstruction
challenge is to prove a uniform incompatibility for that whole family,
or a reusable theorem linking vertical first-symbol defects and full
inverse support. The proposed quotient/join-of-two-conics picture is
an uncomputed geometric interface: no residual inverse curve class,
saturation, or universal positive residual degree has been established
there. Keep that missing implication explicit.

This source shows that nonisomorphic inverse lifts are concrete rather
than merely formal exceptions. Its failure also shows that correct
Picard ratios, a finite birational map, and the right marked restriction
do not imply full inverse support or descent. No actual STCI pair is
constructed, and no unrestricted characteristic-zero nonexistence
theorem follows. The general question remains open.
