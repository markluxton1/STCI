# Numerical pullback and the normal line

This note separates a reusable surface inequality from the numerical assumptions
of any particular carrier. Work over an algebraically closed field of
characteristic zero. The lemma below concerns an **integral projective surface**
\(S\) and a smooth integral curve \(C\subset S\), with \(S\) regular
at the generic point of \(C\). Neither normality of \(S\) nor Cartierness
of \(C\) is required. Its application to a hypothetical STCI requires the actual
carrier and its normal line, not only an abstract singularity model.

## The pullback defect

Write \(I=I_{C/S}\), let
\(L=(I/I^2)/\operatorname{torsion}\), and set \(N=L^\vee\). Since \(C\)
is smooth and \(S\) is regular at the generic point of \(C\), \(L\) is a line bundle.
Let \(S^\nu\to S\) be the finite normalization. Choose a smooth
projective resolution \(\pi:T\to S\) factoring through both \(S^\nu\)
and the blowup of \(I\), with smooth strict transform \(\widetilde C\). Then
\(\widetilde C\to C\) is an isomorphism and
\[
I\mathcal O_T=\mathcal O_T(-D),\qquad D=\widetilde C+Z,
\]
where \(Z\) is effective and exceptional for \(T\to S^\nu\). There is
only one curve \(C^\nu\) above \(C\) dominating it, by generic regularity.
The finite birational map \(C^\nu\to C\) is an isomorphism since \(C\) is
normal. Define its numerical pullback
\(C^\#=\widetilde C+R\) by \(C^\#\cdot E_i=0\) for every exceptional
curve. Then
\[
\boxed{\deg N-(C^\#)^2=(Z-R)\cdot\widetilde C\ge0.}
\]

**Proof.** The rational lift \(C\dashrightarrow T\) extends at every
point by properness and the DVR valuative criterion. It is a section over
\(C\), hence a closed immersion with image \(\widetilde C\). This
identifies \(\widetilde C\) with \(C\). Any nonexceptional divisor in
the support of \(I\mathcal O_T\) would map finitely onto \(C\) from
\(S^\nu\); generic regularity makes \(C^\nu\) its only possibility,
with coefficient one. Thus \(D=\widetilde C+Z\) as asserted. The surjection
\(\pi^*I\twoheadrightarrow\mathcal O_T(-D)\), restricted to
\(\widetilde C\), kills \(I^2\): multiplication by the local equation of
\(D\) vanishes on \(\widetilde C\). It therefore induces a surjection
\(I/I^2\twoheadrightarrow\mathcal O_T(-D)|_{\widetilde C}\). Torsion
maps to zero in a line bundle, so the induced surjection of line bundles is
an isomorphism. Consequently \(\deg N=D\cdot\widetilde C\).

Let \(M=(E_i\cdot E_j)\), \(c_i=\widetilde C\cdot E_i\), and write
\(Z=\sum z_iE_i\), \(R=\sum r_iE_i\). For \(T\to S^\nu\), the matrix \(M\) is negative
definite with nonnegative off-diagonal entries. Relative generation of
\(\mathcal O_T(-D)\) gives \(D\cdot E_i\le0\), hence
\[
c+Mz\le0,\qquad c+Mr=0.
\]
The inverse of \(-M\) is entrywise nonnegative. To see the sign without a
matrix classification, if \(Ax=b\ge0\) for a positive-definite symmetric
matrix \(A\) with nonpositive off-diagonal entries, write
\(x=x_+-x_-\) with disjoint nonnegative supports. If \(x_-\ne0\),
\(x_-^TAx=x_-^TAx_+-x_-^TAx_-<0\), contradicting \(x_-^Tb\ge0\).
Apply this to \(A=-M\) and \(-M(z-r)\ge0\); then \(z-r\ge0\).
Finally, orthogonality to \(R\) gives
\((C^\#)^2=\widetilde C^2+R\cdot\widetilde C\), proving the formula
and sign. \(\square\)

The exceptional intersection input is the classical negative-definiteness
argument in [Mumford, *The topology of normal singularities of an algebraic
surface* (1961), §1, p.6](https://www.numdam.org/item/PMIHES_1961__9__5_0.pdf).
The displayed normal-line identification and defect formula are proved above;
they are not attributed to an unchecked literature statement. Resolving and
principalizing the curve ideal is essential to that identification.

**Characteristic boundary.** Once a smooth principalizing model with the stated
exceptional intersection properties is supplied, the displayed defect identity
and its sign use no characteristic-zero argument. They therefore hold over an
algebraically closed field of any characteristic under those same model
hypotheses. This observation does not transfer a characteristic-zero surface
classification, a bound on exceptional configurations, or a particular
application's normal-bundle calculation to positive characteristic.

## What the defect measures

The integral divisor \(D\) records the actual vanishing of the curve ideal
on a resolution. The rational divisor \(C^\#\) records numerical
orthogonality. Their difference measures exceptional vanishing that cannot be
seen from the numerical pullback alone. At an ordinary double point where
\(\widetilde C\) meets the exceptional \((-2)\)-curve once, \(r=1/2\).
On the blowup principalizing the smooth branch ideal, \(z=1\); the contribution
to the displayed defect is \(1/2\).

A carrier application must still compute \(\deg N\), \((C^\#)^2\), and
the actual exceptional contacts. This lemma alone neither excludes a carrier
nor supplies a value such as \(13/5\) for its pullback square. If the
surface is singular at the generic point of \(C\), the rank-one conormal
and coefficient-one arguments fail; that case is outside this lemma.

## Cartier index does not bound the numerical correction

On the normal surface singularity \(uv=w^{2m}\), take the smooth branch
\(C: u=v=w^m\). Its strict transform meets the middle curve of the
\(A_{2m-1}\) resolution chain transversally. For the negative chain matrix,
\[
-(M^{-1})_{ij}=\frac{\min(i,j)(2m-\max(i,j))}{2m}.
\]
Thus the middle correction is \(-(M^{-1})_{mm}=m/2\). The local divisor
class of the branch has order two: in the cyclic discriminant group of the
chain it is the class \(m\in\mathbb Z/(2m)\), and the function
\(u+v-2w^m\) has divisor \(2C\). Its numerical pullback has coefficient \(1/2\) at
the first exceptional curve, so the branch is not Cartier. In the middle
resolution chart \(u=w^m x,v=w^m/x\), its strict transform is \(x=1\),
transverse to the central exceptional curve \(w=0\). In particular the Cartier index remains
two while the correction is unbounded.

This concrete family rules out an estimate of the correction using only the
local Cartier index, such as \(-(M^{-1})_{jj}\le r/4\). It does not contradict
a theorem with additional geometric or direction hypotheses. Any bounded-index
carrier argument must keep those hypotheses visible and cannot substitute
index for the full resolution data.

## Limits of numerical and generic input

The correction matrix, discrepancy divisor and actual normal derivatives are
different inputs. For arbitrary normal surface singularities, one cannot assume
the discrepancy contribution has the sign available in a crepant ADE
calculation. Nor does the Cartier index alone establish a lower bound
\(\operatorname{ord}_p(\nabla F|_C)\ge r_p-1\). A proof using either step
must establish its singularity and marked-curve hypotheses independently; the
index-two family above already rules out replacing the correction matrix by
an index-only estimate.

On a nonnormal carrier, an intersection number with the conductor counts
scheme-theoretic multiplicity, not distinct normalization points. Two plane
curves \(y=0\) and \(y=x^N\) already have one intersection point of length
\(N\). Likewise, a nonzero transverse differential does not by itself produce
a second distinct normalization sheet. The [full conductor and inverse-support
criterion](carrier_conductor_socle_interfaces.md) requires the actual finite
algebra and full inverse fiber, including nonreduced structure.

Generic curvilinearity supplies no automatic compatible primitive stage on the
whole support. In characteristic zero, the [explicit supported complete-intersection
control](../supplements/Z4_INTRINSIC_ARITHMETIC_MECHANISM.md#counterexample-c--generic-primitivity-does-not-globalize)
has equations \((x^2,y^2+tx)\) on a line-supported projective
complete intersection. It has generic length four but a special algebra
\(k[x,y]/(x^2,y^2)\) with no curvilinear length-three quotient. It therefore
prevents a generic normal model from being substituted
for an everywhere compatible primitive triple. A reduction from arbitrary
entirely thick pairs to movement-two root lifts needs its own theorem; none
follows from these numerical identities.

## Review status

The defect proof for integral surfaces generically regular along the curve,
the conormal identification and matrix sign,
and the explicit smooth-branch index-two counterexample were independently
reconstructed and accepted in this consolidation (GPT-6.1 Sol, high effort).
The example recovers useful mathematics from a retracted unrestricted proof;
no unrestricted nonexistence claim is retained. Applications that used a
conditional numerical antecedent remain conditional until that antecedent is
established for the actual carrier.

## Conditional split-sextic application

Use the hypotheses and notation of
`research/notes/2026-10-05-split-sextic.md`: the low branch is a smooth
section, the strict sextic is an integral surface regular generically along
that branch, and both selected ramified-root endpoints are ordinary nodes.
Let `delta` be the zero-divisor length of the nonzero Jacobian map

\[
 N_{\Gamma/B}\longrightarrow O_\Gamma(D)=O_{\mathbf P^1}(12).
\]

From `deg N_{Gamma/B}=2+6=8`, its saturated kernel is

\[
 N_{\Gamma/D}=O_{\mathbf P^1}(\delta-4).
\]

This degree computation uses the normal extension only through its
determinant; it does not split that extension.

P-020/P-023 force `Gamma#^2=13/5` for a mate-compatible type `d=1`.
The general inequality alone would imply `delta>=7`. The two endpoint
contributions in (4) improve it to

\[
 \delta-4-13/5\geq1,
 \qquad\boxed{\delta\geq8.}
\]

Each ordinary endpoint has Jacobian common order one. Thus the interior
Jacobian common divisor must have length at least six. In the finite
chart, away from the endpoints and after the stated trivializations, this
means

\[
 \deg\gcd(R,g)\geq6,
\]

provided `R` and `g` are the exact two Jacobian components there (as in the
split-sextic note). Since `R(0)=a_h u_0 != 0` and `g=zG` with
`deg G <= 6`, **if `G` is nonzero**, this further forces

\[
 \boxed{\deg G=6,\qquad G\mid R.}
\]

The identically-zero case is a separate stratum: the coefficient of
`z^6` in `G` can vanish even though the high factor is content-free. In
that case `gcd(R,0)=R`, so the degree-six argument does not apply. It is
handled separately in `2026-10-06-split22-finite-reduction.md`.

This is a conditional necessary restriction, not an STCI exclusion. The
reviewed lemma supplies the normal-sheaf inequality, while the asserted
13/5 pullback square, exact Jacobian components and actual-carrier hypotheses
remain separate antecedents; they were not independently recertified here.
