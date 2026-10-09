# The dx=1 P-044 saturation gap is closed

Date: 2026-10-07, continuing the 2026-10-06 calculation.

Status: **PROVED by exact polynomial certificates, with independent rational expansion.** The full five-coordinate P-044 obstruction on the indicated slice has precisely the P-045 basepoint-free zero locus. The formerly proposed three-coordinate saturation is **false**, rather than merely uncomputed. Both facts are retained below. All conclusions in this note are in characteristic zero.

This closes section G's local audit gap in `AUDITED_STATE_2026-10-06.md`. It is a classification on `dx=1` in P-044's normalized cross-section, not an exhaustion of the full quotient parameter space and not a global STCI theorem. The separate universal primitive-fourth theorem has wider scope; the coordinate comparison at the end verifies that the two calculations agree.

## Exact statement and source normalization

Use P-044's normalized pair

\[
A=z^2+az+x,\qquad B=1+bz+dz^2,
\]

and impose `d=1/x`. This slice requires `x != 0`. Set

\[
u=bx-a,\qquad t=xu,\qquad \alpha=2a+1,\qquad\beta=b+2.
\]

The source resultant specializes exactly to

\[
\Delta=u^2/x.
\]

Thus the basepoint-free slice is exactly `D(t)`. No separate `u=0` boundary belongs to it. Starting with the five persisted source polynomials in
[`e2_full4_obstruction_2026-10-05.txt`](../computations/e2_full4_obstruction_2026-10-05.txt), the audit reconstructs, without copying an earlier quotient list,

\[
G_i(a,b,1/x,x)=\frac{uQ_i(a,b,x)}{x^{k_i}},
\qquad(k_1,k_2,k_3,k_4,k_5)=(1,1,2,2,3).
\]

Every division and rational identity is checked exactly. On `D(t)`, vanishing of the original five `G_i` is therefore equivalent to vanishing of all five `Q_i`. Since P-044's obstruction coordinates are `G_i/(32 Delta)`, this is also precisely fourth-obstruction vanishing. Let

\[
R=\mathbf Q[a,b,x],\qquad L=(Q_1,Q_2,Q_3,Q_4,Q_5).
\]

The result is

\[
\boxed{
V(L)\cap D(t)
=V(\alpha,\beta)\cap D(t).
}
\]

Equivalently,

\[
\boxed{
d=x^{-1},\quad\Delta\ne0,\quad P\text{-044}
\iff
a=-\tfrac12,\quad b=-2,\quad x\ne0,\tfrac14.
}
\]

The reverse implication is checked by exact substitution in every source quotient, and not inferred merely from the radical computation.

## Compact saturated ideal and both containment directions

Define the following six-generator ideal, writing its generators in the translated variables `alpha,beta`:

\[
\begin{aligned}
J=(&x\beta^2+\alpha\beta-2\alpha^2,
\;(4x+2)\alpha\beta-3\alpha^2,\\
&\beta^3,\;\alpha\beta^2,\;\alpha^2\beta,\;\alpha^3).
\end{aligned}
\]

The compact exact certificate is

\[
\boxed{tJ\subseteq L\subseteq J,\qquad J:t=J.}
\]

Consequently

\[
\boxed{L:t=L:t^\infty=J.}
\]

Here the two directions have independent arithmetic checks:

1. **`L subset J`.** SymPy over `QQ` reduces each independently reconstructed `Q_i` to zero modulo the displayed small ideal `J`.
2. **`tJ subset L`.** A saved `5 by 6` polynomial multiplier matrix `C` satisfies
   \[
   (Q_1,\ldots,Q_5)C=t(h_1,\ldots,h_6),
   \]
   where `h_j` are the displayed generators of `J`. The coefficients use the translated variables `A=alpha,B=beta`. Macaulay2 generated the matrix; a separate SymPy calculation parses every coefficient as an exact `QQ` polynomial and expands all six matrix identities. The expansion is identically zero in every column. The full multiplier record is about 512 kB; the ideal and the verifying calculation remain short.
3. **`J:t=J`.** Macaulay2 checks the colon equality exactly. The following elementary module argument verifies it without another saturation computation.

The multiplier matrix is in
[`session_dx1_shifted_membership_2026_10_07.txt`](../computations/session_dx1_shifted_membership_2026_10_07.txt); its generator is
[`session_dx1_shifted_membership_2026_10_07.m2`](../computations/session_dx1_shifted_membership_2026_10_07.m2).

## An elementary saturation and radical proof

In `R/J`, put

\[
\gamma=\beta^2-\frac83\alpha\beta.
\]

The first two displayed relations give

\[
\alpha\beta=3x\gamma,\qquad
\alpha^2=x(4x+2)\gamma,\qquad
\beta^2=(8x+1)\gamma.
\]

All products of total `alpha,beta` degree at least three are zero, so

\[
\alpha\gamma=\beta\gamma=\gamma^2=0.
\]

These equations show that `R/J` is generated over `Q[x]` by

\[
1,\alpha,\beta,\gamma.
\]

They are also independent: define the free `Q[x]` module on these four symbols with the multiplication table just displayed. It is associative because every product of three elements of its nilpotent ideal vanishes. Its generators satisfy all six relations of `J`, while the equations above reduce every polynomial to this module. The resulting mutually inverse maps identify `R/J` with this free rank-four `Q[x]` algebra.

Now

\[
t=x\left(\tfrac12-2x+x\beta-\tfrac12\alpha\right).
\]

With respect to the degree filtration `1; alpha,beta; gamma`, multiplication by `t` has all four diagonal entries equal to

\[
\lambda=x(\tfrac12-2x).
\]

Its determinant is `lambda^4`, a nonzero element of the integral domain `Q[x]`. The multiplication map is injective on this free module. This proves `J:t=J`. Together with `tJ subset L subset J`, it proves the stated saturation equality in both directions.

Finally, `alpha^3,beta^3` belong to `J`, and every generator of `J` belongs to the prime ideal `(alpha,beta)`. Therefore

\[
\boxed{\sqrt J=(\alpha,\beta).}
\]

Base change to any algebraically closed characteristic-zero field preserves these rational identities. The quotient algebra is nonreduced; no reduced obstruction-scheme assertion is made. The free rank-four calculation describes that nilpotent structure explicitly.

## Boundary audit and exhaustion of the slice

The single saturation by `t=x(bx-a)` handles the whole allowed slice, so the proof does not depend on separating the two divisors `alpha=0` and `beta=0`. They nevertheless give useful independent checks. Direct specialization of all five source quotients gives

\[
\begin{aligned}
\left.L\right|_{a=-1/2}:
\bigl(x(bx+1/2)\bigr)^\infty&=((b+2)^2),\\
\left.L\right|_{b=-2}:
\bigl(x(-2x-a)\bigr)^\infty&=((2a+1)^2).
\end{aligned}
\]

Their radicals are `(b+2)` and `(2a+1)`, respectively. These identities are verified in the fresh companion from the original five source polynomials. They agree with the repaired `verify_dx1_a_half_boundary.py`, whose earlier undivided ordinary-ideal membership assertion retained an extraneous `x=0` component and whose rational reduction also required an explicit `QQ` domain.

Within this cross-section, `x=0` is impossible on `dx=1`, and `u=0` is exactly the resultant-zero locus. No omitted chart is claimed covered outside the normalized `A_2 B_0 != 0` cross-section. On `alpha=beta=0`, the allowed open condition becomes `x(1/2-2x) != 0`, giving precisely the stated exclusions `x=0,1/4`.

## Why the formerly requested three-equation certificate is false

The residual factors satisfy

\[
Q_2=\alpha R_2,\qquad Q_4=2\beta R_4.
\]

The earlier diagnostic kept only `(R2,R4,Q5)` on `D(t alpha beta)`. Its saturated ideal is **not** the unit ideal: the direct `QQ` Macaulay2 calculation gives dimension zero and degree 29. This is stronger than the original warning about multivariate resultant coprimality.

There is an independently certified real zero of this insufficient subsystem near

\[
(a,u,x)=(-0.199499192681611878608445711923,
\;0.190901045508013354512168855298,
\;-0.366729879371914138346593229175).
\]

The displayed numbers specify an exact rational cube center. A cube of radius `10^-10` has an exact rational Newton contraction bound below `10^-4` and is mapped into a cube of radius below `10^-14`. Thus it contains a unique real zero. All four open factors `x,u,2a+1,a+u+2x` are bounded away from zero throughout the cube. The omitted `Q1,Q3` numerators are also bounded away from zero there, so this zero is not a P-044 zero.

The exact interval proof, independent expansion of the older `s^2=sum Q_i C_i` certificate, and their rerunnable output are retained in
[`verify_session_dx1_independent_2026_10_06.py`](../computations/verify_session_dx1_independent_2026_10_06.py) and
[`verify_session_dx1_independent_2026_10_06.out`](../computations/verify_session_dx1_independent_2026_10_06.out).

Accordingly, the earlier note's proposed equivalence with emptiness of the three-equation open set must not be reused. The correct repair uses the full five obstruction coordinates. The old resultants remain exact identities but have no emptiness implication by coprimality alone.

## Comparison with the universal linear locus

The retained universal computation uses

\[
A=a_0+a_1z+a_2z^2,\qquad B=b_0+b_1z+b_2z^2,
\]

and its linear fourth-zero locus is

\[
K=(2a_1+b_0,\;2a_2+b_1).
\]

Our coordinate identification is exactly

\[
(a_0,a_1,a_2,b_0,b_1,b_2)=(x,a,1,1,b,d).
\]

The fresh audit compares every polynomial, rather than samples: if `U_i` are the five universal numerators, then

\[
\boxed{U_i(x,a,1,1,b,d)=G_{6-i}(a,b,d,x)/32.}
\]

The universal resultant also specializes exactly to the source P-044 resultant. The reversal of coordinate order and the scalar `1/32` are explicit and harmless to the zero locus. Hence `K` restricts to `(alpha,beta)` already before imposing `dx=1`. Restricting the verified universal theorem therefore gives a shorter comparison proof of the same set-theoretic classification. The standalone saturation proof above does not depend on that theorem.

For provenance, the comparison currently reads the explicitly identified isolated validation snapshot
`research/validation/2026-10-06-session/isolated/research/scratch/primitive47universal/equations.json`. Its SHA256, the original obstruction source SHA256, and the multiplier-file SHA256 are saved in the fresh JSON audit record. The mathematical saturation result is computed from the original persisted four-parameter polynomials, not from this snapshot.

## Consequence and continuation instructions

The classified basepoint-free family is exactly P-045. Its independently audited cubic-factor theorem implies that no characteristic-zero quartic carrier can arise from this `dx=1` slice. This closes the local no-carrier statement previously left conditional on residual saturation. It does not create an STCI pair or exclude every curve or every remaining carrier type.

The primary rerunnable record is
[`audit_dx1_saturation_2026_10_07.py`](../computations/audit_dx1_saturation_2026_10_07.py). It reconstructs every quotient from source, checks all source identities and independent multiplier expansions, writes the compact standalone
[`verify_dx1_saturation_2026_10_07.m2`](../computations/verify_dx1_saturation_2026_10_07.m2), and saves inspectable
[`dx1_saturation_audit_2026_10_07.json`](../computations/dx1_saturation_audit_2026_10_07.json) and
[`verify_dx1_saturation_2026_10_07.out`](../computations/verify_dx1_saturation_2026_10_07.out).

Rerun from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/audit_dx1_saturation_2026_10_07.py
/opt/homebrew/bin/M2 --script research/computations/verify_dx1_saturation_2026_10_07.m2
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_session_dx1_independent_2026_10_06.py
```

All three pass. A direct large-ideal SymPy Groebner attempt was interrupted after slow progress; no result from that attempt is asserted. Exact polynomial multiplication and the small-ideal reductions provide its independent replacement.
