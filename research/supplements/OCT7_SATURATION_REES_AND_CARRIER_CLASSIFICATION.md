# October 7 saturation, Rees valuations, blowup budgets, and rational carriers

Topical preservation of mathematical source material, including counterexamples and original audit qualifications. No theorem promotion.

---

## 2026-10-07-dx1-saturation-audit

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


---

## 2026-10-07-e1-jet-rebuild

# e=1 jet lane rebuild — 2026-10-07

Base: current remote main at `7662a2ebb1dd561c1fb5e3c8958799b37d962c41`.

Purpose: reconstruct the e=1 primitive-triple quartic-carrier calculation on a clean branch. The older branch `research/jet-discrepancy-order-one-2026-10-06` is retained only for provenance.

## Imported theorem-level input

Bănică–Forster gives the standard double-to-triple splitting obstruction in
[
H^1(O_C(-4)).
]
The project-specific exact obstruction coordinates are independently persisted in
`research/computations/verify_e1_triple_obstruction.py`.

Their resultant-open zero locus is:
- main component (b_0=-2a_1, a_0b_1=-8a_1^2);
- boundary (a_0=b_1=0), with (r=b_0/a_1) satisfying
  ((r+2)(3r^2+4r+12)=0).

## Rebuild target

On the main component normalize
[
A=1+tz,qquad B=-2t-8t^2z,qquad t
e0.
]
The new self-contained certificate `verify_e1_jet_rebuild.py` reconstructs:
1. (I_C(4)) from all 35 ambient quartic monomials;
2. the first-symbol condition defining (I_{C_2}(4));
3. the BF quadratic chart correction;
4. the second-contact matrix for (C_3);
5. its kernel as actual ambient quartics (F_0,F_1);
6. the gcd of (F_0,F_1) over (mathbf Q(t)).

## Status discipline

The script contains exact symbolic assertions for the previously obtained dimensions/rank, but this branch has not yet recorded a runtime transcript from an independent Python execution. Therefore:
- the BF obstruction locus is **ported exact certificate / previously audited**;
- the rebuilt quartic assertions are **PENDING RUNTIME VERIFICATION**;
- no new gcd or residual-base-locus conclusion is promoted yet.

After runtime verification, compute/saturate the ideal ((F_0,F_1)) against (I_C), preferably in Macaulay2, and record the residual scheme uniformly over the parameter (t). Only then interpret the geometry and literature-check linkage/contact antecedents.


## Runtime verification and main-component carrier exclusion

Independent execution of \`verify_e1_jet_rebuild.py\` reproduced:
\[
h^0(I_C(4))=18,\qquad h^0(I_{C_2}(4))=7,
\]
the second-contact rank
\[
\operatorname{rank}=5,
\]
and therefore
\[
h^0(I_{C_3}(4))=2.
\]
The two extracted ambient quartics \(F_0,F_1\) satisfy
\[
\gcd(F_0,F_1)=1\quad\text{over }\mathbf Q(t),
\]
so the pencil has no fixed surface factor.

A further exact calculation restricts the two quartics to the unique quadric
\[
Q=xW-yZ.
\]
On the affine chart \(x=1\), where \(Q\) gives \(W=yZ\), one obtains (up to nonzero scalars)
\[
F_0|_Q=
Z(-Z+y^3)(8t^3Z-1)(2ty+1),
\]
\[
F_1|_Q=
(-Z+y^3)(8t^3Z-1)(64t^6Z^2+1)(2ty+1).
\]
Hence
\[
\gcd(F_0|_Q,F_1|_Q)
\sim
(-Z+y^3)(8t^3Z-1)(2ty+1).
\]
The first factor is the quartic \(C\). The other two factors close to ruling lines
\[
L_1(t):\quad 2ty+x=0,\qquad 2tW+Z=0,
\]
\[
L_2(t):\quad 8t^3Z-x=0,\qquad 8t^3W-y=0.
\]
Direct symbolic substitution of the two line parametrizations into both generic
quartics gives zero identically. Thus
\[
\boxed{L_1(t)\cup L_2(t)\subset V(F)\quad
\text{for every }F\in H^0(I_{C_3}(4)).}
\]

Since \(t\ne0\), neither line is \(C\). Any positive-degree projective hypersurface
\(G\) meets each line (or contains it). Therefore
\[
V(F,G)
\]
has support outside \(C\) for every quartic carrier \(F\) through this primitive
triple.

**PROVED (exact symbolic certificate + direct substitution).**
The entire one-dimensional nonzero-comparison main component of the e=1
primitive-triple locus cannot occur in an STCI presentation having a quartic
carrier.

This mechanism differs from e=2: the ambient quartic pencil has no common
surface factor; instead it has a forced pair of ruling lines in its base locus.

The two isolated nonzero-comparison boundary directions remain to be checked
separately. The comparison-zero boundary direction was previously identified
as the quadric-contained case and should also be re-certified on this clean branch.


## Isolated e=1 boundary directions

### Nonzero-comparison conjugate pair

Set
\[
A=z,\qquad B=r,\qquad 3r^2+4r+12=0.
\]
The calculation was carried out over the exact quadratic field
\[
K=\mathbf Q[r]/(3r^2+4r+12),
\]
so both conjugate directions are handled simultaneously without numerical
specialization or radicals.

The reconstructed quartic-through-double source has dimension seven, the
second-contact map has rank five, and hence
\[
h^0(I_{C_3}(4))=2.
\]
The two ambient quartics have gcd one in \(K[x,y,Z,W]\): there is no fixed
surface factor.

Restricting the two quartics to the unique quadric \(Q=xW-yZ\), and using
\(W=yZ\) on \(x=1\), their common factor is
\[
(-Z+y^3)\,y\,Z.
\]
The factor \((-Z+y^3)\) is \(C\). The remaining factors close to the two
coordinate ruling lines
\[
L_y:\ y=W=0,\qquad
L_Z:\ Z=W=0.
\]
Direct substitution verifies that both quartics vanish identically on both
lines. Therefore
\[
L_y\cup L_Z\subset \operatorname{Bs}|I_{C_3}(4)|.
\]

**PROVED (exact quadratic-field calculation).** Both isolated
nonzero-comparison e=1 primitive-triple directions are excluded as quartic
STCI carriers: any positive-degree mate meets either fixed projective line
(or contains it), creating support outside \(C\).

### Comparison-zero point

At the remaining boundary direction
\[
A=z,\qquad B=-2,
\]
the comparison section \(A+zB/2\) vanishes identically. The quadric has chart
equation
\[
Q=u+\frac z2v.
\]
Under the primitive direction
\[
u=z\epsilon,\qquad v=-2\epsilon,
\]
this vanishes identically. The BF quadratic cocycle also vanishes, so the
canonical primitive triple lies on \(Q\):
\[
C_3\subset Q.
\]
The quartic source has dimension ten, while
\[
Q\cdot H^0(O_{\mathbf P^3}(2))
\]
also has dimension ten and is contained in \(H^0(I_{C_3}(4))\). Hence
\[
\boxed{H^0(I_{C_3}(4))=Q\cdot H^0(O_{\mathbf P^3}(2)).}
\]

**PROVED / RECERTIFIED.** This direction is excluded because every quartic
carrier has the fixed quadric factor.

## e=1 primitive conclusion — corrected status

The carrier geometry is completely classified at the triple stage:
- main one-dimensional component: a two-dimensional quartic pencil with two
  parameter-dependent fixed ruling lines and no fixed surface factor;
- two conjugate isolated points: a two-dimensional quartic pencil with two
  coordinate ruling lines and no fixed surface factor;
- comparison-zero isolated point: every quartic has the fixed quadric factor.

Only the comparison-zero point is excluded immediately by the fixed-surface
argument. The fixed-line cases remain **OPEN as STCI exclusions**. To close
them one must analyze the mate divisor on the forced ruling lines (including
the intersection divisor with C), or produce a stronger residual curve/surface
obstruction.

## Consequence for multiplicity-six quasiprimitive e=1

The audited MF6 classification on current main leaves e=1 numerical defect
types
\[
(d_2,d_3)=(0,4),(1,3),(2,2).
\]

The newly closed primitive-triple carrier calculation immediately excludes
the entire \((0,4)\) type: when \(d_2=0\), the triple is primitive. Every
quartic containing a later sextuple also contains its primitive triple, and
every such triple has already been shown to force either fixed ruling lines
or a fixed quadric factor. Later defects cannot remove a base curve already
contained in every quartic at the triple stage.

Therefore the e=1 MF6 frontier reduces to
\[
\boxed{(d_2,d_3)=(1,3)\text{ or }(2,2).}
\]

For these two types the second graded piece is
\[
E_2=L^2(D_2)=O(-12+d_2),
\]
so they are genuinely quasiprimitive already at the triple stage and are not
covered by the primitive classification.

The BF obstruction class before adding \(D_2\) lies in \(H^1(O(-4))\).
A defect section \(\delta\in H^0(O(d_2))\) must annihilate it under
multiplication
\[
H^1(O(-4))\xrightarrow{\cdot\delta}H^1(O(-4+d_2)).
\]
Thus:
- \(d_2=1\): two obstruction coordinates remain (\(H^1(O(-3))\));
- \(d_2=2\): one obstruction coordinate remains (\(H^1(O(-2))\)).

By Serre duality this is an apolarity problem for the binary quadratic dual
to the primitive BF obstruction. This is the recommended next exact
classification: solve the annihilator incidence \((A,B,\delta)\) first,
then impose ambient quartic containment on those low-dimensional strata.


## Repair of the fixed-ruling STCI implication

The earlier naive inference "a positive-degree mate meets a fixed line, hence
creates support outside C" is false: a finite zero divisor on the line could
be supported on its intersection with C.

The correct argument uses the quartic surface. Let F be a quartic whose first
normal direction along C is basepoint-free. Then F is smooth along C. If
\[
V(F,G_b)_{\mathrm{red}}=C,
\]
then on the smooth surface F the restriction of G_b is locally a Cartier
divisor supported on C. Its generic multiplicity is b, because the generic
transverse complete intersection has length b. Since C is irreducible, this
coefficient is constant:
\[
\operatorname{div}_F(G_b)=bC
\]
in a neighborhood of C.

Consequently, if a curve L is contained in F and meets C properly on F, then
unless G_b contains L,
\[
\deg(G_b|_L)\ge b(L\cdot_F C).
\]
For a line L, the left side is b. Hence any fixed line with
\(L\cdot_F C>1\) must also lie in G_b, producing an extra common curve.

This repairs the primitive e=1 exclusions:
- on the main component, the fixed ruling
  \(L_2:8t^3Z-x=8t^3W-y=0\) has intersection divisor with C cut by
  \(8t^3z^3-1\), hence degree 3;
- at the conjugate isolated points, the fixed line
  \(L_Z:Z=W=0\) meets C with multiplicity 3 at z=0.

Thus in every nonzero-comparison primitive case the quartic contains a fixed
line of intersection number three with C, forcing every mate G_b to contain
that line. The comparison-zero case remains excluded by its fixed quadric.

**PROVED, repaired.** Every basepoint-free e=1 primitive triple is
incompatible with an STCI presentation having a quartic carrier, for every
mate degree b>0.

Therefore the MF6 e=1 type \((d_2,d_3)=(0,4)\) is indeed excluded, and the
remaining e=1 MF6 types are \((1,3)\) and \((2,2)\).


## Degree-one defect: exact annihilator incidence and nonuniform carrier samples

Write the primitive BF class as
\[
\xi=c_1z^{-1}+c_2z^{-2}+c_3z^{-3}\in H^1(O(-4)).
\]
For \(\delta=d_0+d_1z\), its image in \(H^1(O(-3))\) vanishes exactly when
\[
c_1d_0+c_2d_1=0,\qquad c_2d_0+c_3d_1=0.
\]
Therefore, away from the primitive locus \(\xi=0\), a degree-one defect
section exists iff
\[
\boxed{c_1c_3-c_2^2=0},
\]
and then its projective class is unique. Thus the d2=1 triple locus is a
determinantal hypersurface in quotient space carrying a canonically
determined defect point.

Exact sample computations show that this incidence does not have uniform
quartic geometry.

1. \(A=-8-3z,\ B=2-3z\). Here
   \([c_1:c_2:c_3]=[1:4:16]\), \(\delta\sim z-4\).
   The quartic-through-triple space has dimension one. Its restriction to
   Q contains the ruling \(Z=W=0\), which has intersection multiplicity
   three with C; the repaired Cartier-divisor lemma excludes this sample.

2. \(A=-8-2z,\ B=-4-4z\). Here
   \([c_1:c_2:c_3]=[1:2:4]\), \(\delta\sim z-2\).
   The second-contact rank is three, so four quartics survive, and they share
   a common cubic factor. This sample is excluded by the fixed-surface
   factorization mechanism.

3. \(A=-8-z,\ B=-2-4z\). Again
   \([c_1:c_2:c_3]=[1:2:4]\), \(\delta\sim z-2\), but the contact rank is six
   and only one quartic survives. Its residual intersection with Q has no
   linear ruling factor over Q. Hence the defect divisor (or even the BF
   obstruction ratio) does not determine the quartic carrier geometry.

**Conclusion.** A uniform theorem of the form "d2=1 forces a ruling" is
false. The surviving MF6 type (d2,d3)=(1,3) must retain the full normal
quotient together with the later D3 condition. The exact annihilator
certificate is research/computations/verify_e1_d2_defect.py.


## MF6 D3 test for the previously troublesome d2=1 unique-quartic sample

Take
\[
A=-8-z,\qquad B=-2-4z.
\]
Its primitive BF class has ratio \([c_1:c_2:c_3]=[1:2:4]\), so the unique
degree-one annihilator is
\[
\delta=z-2.
\]
Multiplication of the exact BF cocycle gives
\[
\delta h_2
=24z^2-24+192z^{-3}-3072z^{-5}.
\]
Thus the finite-chart quadratic correction is
\[
\gamma=24(z^2-1).
\]

Reconstructing the full \(I_C(4)\), imposing the first normal symbol, and
then the quasiprimitive triple relation gives a seven-dimensional
quartic-through-double source and a rank-six triple-contact matrix. Hence
there is a unique compatible quartic up to scalar.

Use local coordinates \(\ell,m\) with
\[
u=A\ell,\qquad v=B\ell-m/A,
\]
so \(m=Bu-Av\) and the linear coefficient of the quartic is \(h\,m\).
Solving the unique quartic formally as
\[
m=f_2\ell^2+f_3\ell^3+\cdots
\]
gives
\[
f_2=-24\,\frac{(z-1)(z+1)}{z-2}
=-\frac{\gamma}{\delta},
\]
which independently checks the sign and normalization of the triple
relation, and
\[
\boxed{
f_3=
-16\,\frac{(z+1)(18z^4-26z^3-71z^2+107z+8)}
{(z-2)^3(z+2)(z+8)}.
}
\]

The numerator is nonzero at \(z=2,-2,-8\), and \(f_3\to-288\) at infinity.
The exact third-piece lattice lemma therefore gives
\[
\operatorname{ord}_{2}D_3
=\max(1,-1-(-3))=2,
\]
while the simple poles at \(-2\) and \(-8\), where \(D_2\) has no support,
each contribute one. There is no infinity contribution. Consequently
\[
\boxed{\deg D_3=4}.
\]

**PROVED (exact symbolic calculation).** This unique-quartic d2=1 triple
does not extend to the MF6 numerical type \((d_2,d_3)=(1,3)\). The later
canonical defect kills a carrier that survives all triple-stage quartic
tests.

The next target is to make this calculation universal on the rank-six
contact stratum: derive the denominator/resultant of \(f_3\) modulo
\(c_1c_3-c_2^2=0\), and isolate the cancellation locus on which
\(\deg D_3\le3\).


## Global equation of the d2=1 quotient locus

The pullback of the degree-one annihilator determinant to quotient coordinates factors exactly as

    c1*c3-c2^2 = -3*Delta^2*Q,

where Delta=a0*b1-a1*b0 and

    Q = 16*a0^2*b1^2 + 72*a0*a1^2*b1 + 64*a0*a1*b0*b1
        + 24*a0*b0^2*b1 + 36*a1^4 + 72*a1^3*b0
        + 52*a1^2*b0^2 + 16*a1*b0^3 + 3*b0^4.

SymPy leaves Q irreducible over QQ. Hence on the basepoint-free open set
Delta != 0, the complete d2=1 annihilator locus is the single quartic
surface Q=0; Delta^2 is entirely the forbidden basepoint boundary.

On the chart a1 != 0, put r=b0/a1 and x=a0*b1/a1^2. Then

    Q/a1^4 =
      16*x^2 + (72+64*r+24*r^2)*x
      + 36+72*r+52*r^2+16*r^3+3*r^4.

Thus modulo the residual scaling data, the quartic surface is a quadratic
double cover over the r-line. This is the preferred coordinate reduction
for the universal f3/D3 calculation.

Certified by research/computations/verify_e1_d2_defect.py at commit
7aa20c5d473a36714d812dd847c467c0c40e2785.


## Marked finite-defect elimination

On the chart a1 != 0 normalize a1=1, write r=b0, and write the unique
finite degree-one defect as delta=z-lambda. Then the rank-one Hankel
condition is equivalent off the primitive locus to

    c2=lambda*c1,   c3=lambda^2*c1.

Eliminating a0 from these two equations gives exactly

    12*b1*(r+2)*P(r,b1,lambda),

where

    P =
      9*r^5 - 21*r^4*b1*lambda + 90*r^4
      + 26*r^3*b1^2*lambda^2 - 220*r^3*b1*lambda + 392*r^3
      - 11*r^2*b1^3*lambda^3 + 172*r^2*b1^2*lambda^2
      - 752*r^2*b1*lambda + 912*r^2
      - 20*r*b1^3*lambda^3 + 248*r*b1^2*lambda^2
      - 976*r*b1*lambda + 1360*r
      - 12*b1^3*lambda^3 + 144*b1^2*lambda^2
      - 624*b1*lambda + 1056.

The factors b1=0 and r=-2 are special chart/primitive factors. The three
exact d2=1 samples used in this note all satisfy P=0 after normalization,
including both the rank-six unique-quartic samples and the rank-three
common-cubic sample. Hence contact-rank drop is not a separate component:
it is a proper sublocus inside the same generic marked incidence P=0.

This gives the working stratification

    P=0 contains {contact-rank drop} union {D3 pole-cancellation locus}.

The MF6 type (d2,d3)=(1,3) must lie on the D3 pole-cancellation locus
(or its intersection with contact-rank drop) if the generic saturated
D3 degree is four, as indicated by the exact unique-quartic sample.

The elimination is certified by research/computations/verify_e1_d2_defect.py
at commit 93c0ca4519f0976bc9cbdba74fd75e5b5de2f719.


---

## Consolidation status (2026-10-28)

Read the final **Repair of the fixed-ruling STCI implication** section rather than the earlier, explicitly retracted inference that a mate's intersection with a fixed line must lie outside C. The repaired argument uses intersection multiplicity on a smooth quartic carrier. The historical e=1 quartic-mate frontier is superseded by [R-0001](../results/quartic_carrier_exclusion.md); the exact annihilator and higher-jet calculations remain useful evidence and are not deleted. No new independent symbolic execution was performed in this consolidation.


---

## 2026-10-07-entirely-thick-rees-valuation-framework

# Entirely-thick branch: generic cluster and Rees-valuation framework

Date: 2026-10-07  
Status: **PROVED structural reformulation / OPEN global obstruction program**

## 1. Starting point

Starting remote \`main\`: \`7662a2ebb1dd561c1fb5e3c8958799b37d962c41\`.

For degrees \(a,b\) and exact generic normal orders \(p,q\ge2\), the audited necessary conditions are
\[
ab\ge4pq,\qquad 7ab+28pq\ge16(aq+bp),\qquad a\ge3p,\quad b\ge3q.
\]
Writing \(\alpha=a/p,\beta=b/q\), the \((3,3)\) boundary is impossible and the \((3,4)\) boundary forces the first exceptional intersection into constant sections.

The local family
\[
f=y^2+x^{2n+1},\qquad g=y^2+2x^{2n+1}
\]
shows that fixed first normal forms do not bound transverse intersection length.

## 2. Literature boundary

The required higher-contact language is classical on a transverse smooth surface.

- Noether's intersection formula expresses local intersection multiplicity as a sum of products of multiplicities over common infinitely-near points.
- Zariski-Lipman/cluster theory packages infinitely-near points using proximity relations and complete ideals in two-dimensional regular local rings.
- Rees valuations are the intrinsic divisorial valuations of the normalized blowup of an ideal and control its integral-closure filtration.
- Hilbert-Samuel multiplicity is invariant under integral closure. For a parameter ideal \(J=(f,g)\) in a two-dimensional regular local ring, \(e(J)=\ell(R/J)\).
- Segre numbers/classes and distinguished varieties give higher-dimensional blowup invariants for arbitrary ideals.
- Jaffe's iterated-curve-blowup method is directly relevant to STCI, but its strongest finite-list theorem assumes the two surfaces have no common singular point; the entirely-thick branch lies outside that hypothesis.

References checked include Casas-Alvero, *Singularities of Plane Curves*; Huneke-Swanson, *Integral Closure of Ideals, Rings, and Modules*; Gaffney-Gassler on Segre numbers; and Jaffe (1995).

Thus the generic transverse invariant below is standard mathematics applied to this STCI setup, not a novelty claim.

## 3. Generic transverse cluster theorem

Let \(\eta\) be the generic point of \(C\), and set
\[
R=\mathcal O_{\mathbf P^3,\eta},\qquad K=\kappa(\eta)=k(C),\qquad \mathfrak m=I_CR.
\]
Then \(R\) is a two-dimensional regular local ring. Let \(f,g\in R\) be the images of the defining forms and \(J=(f,g)\).

### Proposition 3.1 — generic intersection multiplicity

Under the STCI support hypothesis,
\[
\ell_R(R/J)=\frac{ab}{4}.
\]

Indeed, the two projective surfaces have no common surface component, so their proper intersection cycle has degree \(ab\). Its reduced support is exactly the irreducible degree-four curve \(C\), hence the fundamental cycle is \(m[C]\), where \(m=\ell_R(R/J)\). Taking degrees gives \(ab=4m\).

### Proposition 3.2 — Noether decomposition

The orders at the origin are \(m_0(f)=p\) and \(m_0(g)=q\). After a finite extension of \(K\), resolve the pair of plane-curve germs by successive point blowups. Noether's formula gives
\[
\frac{ab}{4}
=
pq+\sum_{P\succ0}[\kappa(P):K]\,m_P(f)m_P(g).
\tag{N}
\]
Therefore
\[
v:=\frac{ab}{4}-pq
=
\sum_{P\succ0}[\kappa(P):K]\,m_P(f)m_P(g).
\tag{E}
\]

Thus the second coordinate \(v\) of the audited first exceptional bidegree is exactly the total generic higher-contact budget.

### Corollary 3.3 — fixed-data finiteness

For fixed \((a,b,p,q)\), the number of common infinitely-near points after the origin is at most
\[
E=\frac{ab}{4}-pq,
\]
after passage to an algebraic closure and ignoring multiplicity. Hence the generic common cluster has bounded depth and bounded total number of vertices.

### Limitation 3.4 — normalized ratios do not suffice

Since
\[
E=pq\left(\frac{\alpha\beta}{4}-1\right),
\]
fixing only \((\alpha,\beta)\) does not bound cluster size independently of \(p,q\). At \((3,4)\),
\[
E=2pq.
\]

## 4. Correct higher-order objects

### Pair-sensitive object

Retain the common infinitely-near cluster with proximity relations, residue degrees, and the two multiplicity labels \(m_P(f),m_P(g)\). This distinguishes pairs with the same first tangent forms but different higher contact and directly refines the first exceptional cycle.

### Intrinsic ideal object

The normalized blowup of \(J=(f,g)\) and its Rees valuations give a canonical ideal-theoretic invariant. The integral-closure class determines \(e(J)\), hence the total transverse multiplicity \(ab/4\). It is, however, coarser than the labelled pair-cluster when the two distinguished generators must be tracked separately.

Recommendation: use Rees valuations as the intrinsic ideal-theoretic carrier, but use the labelled cluster (or a mixed refinement) for generator-sensitive inequalities.

## 5. Counterexample family

For
\[
f=y^2+x^N,\qquad g=y^2+2x^N,
\]
one has
\[
J=(f,g)=(y^2,x^N),\qquad \ell(R/J)=2N.
\]
The first tangent forms are always \(y^2\), but the integral-closure/Newton/Rees data changes with \(N\). After the first blowup the remaining Noether budget is
\[
2N-4,
\]
matching the transformed local calculation in the audited thick note.

## 6. Relation to the global exceptional bidegree

The first blowup gives
\[
(u,v)=
\left(
\frac{7ab}{4}+7pq-4(aq+bp),
\frac{ab}{4}-pq
\right).
\]
Equation (E) identifies \(v\) with the generic higher-contact sum. The coordinate \(u\) records global information not visible on one generic transverse slice.

This motivates a relative weighted cluster over \(C\): horizontal centers on successive blowups, equipped with degrees over \(C\), proximity relations, and the two vanishing orders.

## 7. Boundary \((3,4)\)

At \(a=3p,b=4q\),
\[
(u,v)=(0,2pq).
\]
The audited first-blowup argument shows that the support of the exceptional intersection is a union of constant sections, and the quadric residual divisor \(R_F\in|O_Q(2p,0)|\) has at most \(\min(p,q)\) distinct ruling roots.

The natural next problem is therefore to classify the descendants of these constant sections under successive blowups. A naive monotonicity assertion for \(u\) should not be assumed; this is tested in the continuation note.

## 8. Proved conclusions and limitations

**PROVED**

1. The generic transverse multiplicity is \(ab/4\).
2. The first-blowup excess \(v=ab/4-pq\) equals the total higher Noether contact budget.
3. Fixed \((a,b,p,q)\) gives finite generic cluster complexity.
4. Rees/integral-closure data distinguishes the fixed-first-symbol counterexample family.
5. Normalized ratios alone do not give uniform cluster-size bounds through this scalar budget.

**NOT PROVED**

1. No new normalized open region is excluded.
2. No uniform bound independent of \(p,q\) is known.
3. No monotonicity of horizontal twisting under successive blowups is established.
4. Rees valuations alone have not been shown to retain all generator-sensitive STCI data.
5. Persistent generic valuation centers have not yet been shown to force an extra projective common curve.


---

## 2026-10-07-entirely-thick-relative-blowup-budget

# Entirely-thick branch: relative blowup budget on the \((3,4)\) boundary

Date: 2026-10-07  
Status: **PROVED recursion and finiteness / OPEN rigidity step**

This note continues \`2026-10-07-entirely-thick-rees-valuation-framework.md\`.

## 1. Blowup recursion along a horizontal common center

Let \(Y\) be a smooth threefold and let \(D,D'\) be effective Cartier divisors with proper one-dimensional intersection. Let \(Z\subset Y\) be a smooth curve contained in both divisors. Write
\[
r=\operatorname{ord}_Z(D),\qquad s=\operatorname{ord}_Z(D').
\]
Blow up \(Z\):
\[
\pi:Y_1=\operatorname{Bl}_Z(Y)\to Y
\]
with exceptional divisor \(E\). The strict transforms satisfy
\[
\widetilde D=\pi^*D-rE,\qquad
\widetilde D'=\pi^*D'-sE.
\]

### Proposition 1.1 — cycle recursion

In \(A_1(Y)\),
\[
\pi_*\bigl([\widetilde D]\cdot[\widetilde D']\bigr)
=
[D]\cdot[D']-rs[Z].
\tag{R}
\]

**Proof.**
Expand
\[
(\pi^*D-rE)(\pi^*D'-sE).
\]
For a blowup along a codimension-two smooth center,
\[
\pi_*E=0,\qquad \pi_*(E^2)=-[Z].
\]
The two mixed terms therefore push forward to zero and the \(rsE^2\) term pushes forward to \(-rs[Z]\).

This is the relative threefold analogue of the first step in Noether's plane-curve formula.

## 2. Recursion with a finite cover of the parent center

Suppose a later smooth horizontal center \(Z'\) maps finitely onto an earlier center \(Z\) with degree \(d\). If the current strict transforms have orders \(r',s'\) along \(Z'\), then after blowing up \(Z'\) its contribution pushed all the way down to \(Z\) is
\[
d\,r's'[Z].
\tag{R_d}
\]

Thus every common horizontal descendant consumes a positive integer amount of the coefficient of its ancestral horizontal component.

## 3. Application to the \((3,4)\) boundary

For \(a=3p,b=4q\), the first blowup \(B=\operatorname{Bl}_C\mathbf P^3\) has exceptional intersection cycle
\[
W=D\cdot D'=\sum_{j=1}^r c_jT_j,
\]
where the \(T_j\) are distinct constant sections and
\[
r\le\min(p,q),\qquad c_j\ge1,\qquad \sum_j c_j=2pq.
\tag{B}
\]

Fix one \(T_j\). Blow up every horizontal common center above \(T_j\) until the strict transforms no longer meet generically above it. Iterating Proposition 1.1 gives a sectionwise relative Noether identity
\[
c_j
=
\sum_{\nu\in\mathcal T_j}
d_\nu r_\nu s_\nu,
\tag{SN}
\]
provided the terminal intersection has no horizontal component above \(T_j\). Here:

- \(\mathcal T_j\) is the finite tree of horizontal common centers above \(T_j\);
- \(d_\nu\) is the degree of the center over its parent/ancestral section as measured after pushdown;
- \(r_\nu,s_\nu\) are the two vanishing orders along that center.

If a horizontal component survives indefinitely, the pair has a persistent divisorial valuation/common formal branch; converting that persistence into an actual projective common curve is a separate algebraization problem and is not asserted here.

### Corollary 3.1 — relative horizontal finiteness

For every terminating tree,
\[
\#\mathcal T_j\le c_j,
\qquad
\sum_j\#\mathcal T_j\le2pq.
\]
More generally, the total degree-weighted number of centers is bounded by \(2pq\).

Thus the \((3,4)\) boundary has a finite relative horizontal cluster for fixed \(p,q\), not merely a finite cluster on one generic transverse slice.

## 4. Why the proposed \(u\)-monotonicity is not justified

The first exceptional bidegree is \((u,v)=(0,2pq)\). It is tempting to regard \(u\) as a nonnegative energy that later horizontal twisting must increase. Proposition 1.1 shows that this is not automatic.

A blowup of a constant section removes \(rs[T_j]\) from the pushforward intersection cycle. New intersection curves may live on the new exceptional ruled surface. Their geometry can twist relative to \(T_j\) while their pushforward remains a multiple of the same class \([T_j]\). Therefore the original \(u=0\) records the support/class of the first-stage cycle but does not by itself constrain all later ruled-surface bidegrees.

So the candidate implication

\[
u=0\Longrightarrow\text{all later horizontal centers are constant/untwisted}
\]

is **not proved and should not be used**. A new invariant is needed if later twisting is to be controlled.

This is compatible with Jaffe's warning that iterated-blowup type sequences require extra control in the presence of common singularities.

## 5. Refined invariant suggested by the recursion

The natural object is now a **decorated relative cluster**
\[
\mathscr C(F,G/C)
\]
whose vertices are horizontal common centers on successive blowups and whose decorations include

\[
(d_\nu,r_\nu,s_\nu,N_{Z_\nu/Y_\nu},\text{proximity data}).
\]

The first three entries control the intersection budget. The normal bundle of the center in the current threefold controls the geometry of the next exceptional ruled surface:
\[
E_{\nu+1}=\mathbf P(N_{Z_\nu/Y_\nu}).
\]

This is the missing global datum that the generic Rees valuations over \(k(C)\) do not see.

## 6. Relation to the quadric repeated-root constraint

At the \((3,4)\) boundary the audited argument also gives
\[
R_F\in H^0(Q,O_Q(2p,0))
\]
with at most \(r\le\min(p,q)\) distinct ruling roots. Each root corresponds to the intersection of a first-stage constant section \(T_j\) with the quadric-direction section \(S_Q\).

Hence the \(2p\) root multiplicity is distributed among at most \(\min(p,q)\) sectionwise cluster budgets \(c_j\), whose total is \(2pq\).

The next useful inequality must relate:

1. the root multiplicity \(M_j\) of \(R_F\) at the point corresponding to \(T_j\);
2. the coefficient \(c_j\) of \(T_j\) in \(W\);
3. the first blowup orders \(r_j,s_j\) of \(D,D'\) along \(T_j\);
4. the normal bundle \(N_{T_j/B}\).

A lower bound of the form
\[
c_j\ge \Phi(M_j,p,q)
\]
strong enough that
\[
\sum_j\Phi(M_j,p,q)>2pq
\]
would exclude the boundary. No such bound is currently proved.

## 7. Immediate next calculation

Compute \(N_{T/B}\) for a constant section \(T\subset E\simeq\mathbf P^1\times\mathbf P^1\subset B\), and then compute the divisor classes cut on
\[
E_T=\mathbf P(N_{T/B})
\]
by the strict transforms after blowing up \(T\).

This is concrete because:

- \(N_{T/E}\) is determined by the self-intersection of the constant section in \(E\);
- \(N_{E/B}|_T=O_E(E)|_T\) is known from
  \[
  E|_E=O_E(7,-1);
  \]
- the extension
  \[
  0\to N_{T/E}\to N_{T/B}\to N_{E/B}|_T\to0
  \]
  can therefore be analyzed explicitly on \(T\simeq\mathbf P^1\).

That calculation should determine whether the next exceptional ruled surface has enough positivity/negativity to force a new inequality connecting \(c_j\) to the repeated-root multiplicity.


---

## 2026-10-07-normal-rational-carrier-classification

# Rational-resolution normal quartic carriers: classification audit and Type D reduction

Date: 2026-10-07  
Branch: `research/normal-rational-carrier-classification`  
Base main: `7662a2ebb1dd561c1fb5e3c8958799b37d962c41`

## Status

This note does **not** claim a complete exclusion of the rational-resolution normal-quartic branch. It records an audit of the live canonical state and a sharper structural reduction for Type D suggested directly by Ishii--Nakayama's construction.

Labels used below: **PROVED**, **EXACT REDUCTION**, **CONDITIONAL**, **OPEN**.

## A. Audited starting point

The current authority is `research/STATE.md`, not the dated compatibility pointer `AUDITED_STATE_2026-10-06.md`.

The following are accepted on the current record.

1. **PROVED.** Normal quartic carriers with only rational singularities are excluded by Jaffe's quartic theorem.
2. **PROVED.** The positive-genus ruled irrational cases cannot contain a rational quartic of hyperplane degree four.
3. **PROVED.** If the rational quartic avoids the nonrational exceptional anticanonical locus, the numerical correction/rank budget is impossible.
4. **PROVED.** The simple-elliptic case (a single smooth reduced elliptic exceptional curve) is excluded.
5. **OPEN.** The surviving Ishii--Nakayama rational-resolution cases are B1, B2, B3, D with reducible, singular, or nonreduced anticanonical exceptional divisor.
6. **PROVED, conditional on existence of a mate on the fixed carrier.** If (ar C=c+Z) is the numerical pullback, denominator clearing compresses any mate to the least common denominator of (Z). The existing determinant argument gives finite but large upper bounds.
7. **Important scope.** The determinant bound is a mate-degree bound, not a classification of exceptional graphs and not an existence theorem.

For the four rational types the source gives
[
(ho(M),-E^2)=(12,2),(11,1),(11,1),(13,3)
]
for B1, B2, B3, D respectively.

## B. Source check

Ishii--Nakayama, *Classification of normal quartic surfaces with irrational singularities*, JMSJ 56 (2004), 941--965, is stronger for the present problem than the repository's coarse ((ho,-E^2)) summary.

The paper classifies via a basic triplet ((M,D,E)), with (D) the pullback of a general hyperplane and (E) an effective exceptional anticanonical divisor. Its Main Theorem says the examples in section 2 exhaust the normal quartics with irrational singularities.

In particular:

- B1 arises by separation from a generalized del Pezzo surface of degree two with (Bin|-2K_X|), (Gin|-K_X|). The quartic has equation
  [
  (X_0X_1-q(X_1,X_2,X_3))^2=d(X_1,X_2,X_3).
  ]
- B2 arises from a degree-one generalized del Pezzo construction and has two subcases B2-1/B2-2.
- B3 arises from a double cover of (mathbb F_1); its anticanonical divisor is explicitly tracked through the construction.
- D arises by separation of a smooth plane quartic (B=(F_4=0)) and an effective plane cubic (G=(F_3=0)), and the resulting quartic has the explicit monoid equation
  [
  X_0F_3(X_1,X_2,X_3)=F_4(X_1,X_2,X_3).
  ]

No later source located in the focused search gives a ready-made classification of rational quartic curves on the remaining B1/B2/B3/D carriers or an STCI exclusion for them.

## C. Intrinsic resolution identities

Let (H=pi^*O_S(1)), let (c) be the strict transform of the smooth rational quartic, and let (E=-K_M).

For an STCI mate on a quartic carrier,
[
ar C=c+Zequiv H,qquad H^2=4,qquad Hc=4,qquad H E=0.
]

Put (r=cE). Adjunction on (csimeqmathbb P^1) gives
[
-2=c^2+cK_M=c^2-r,
]
hence
[
oxed{c^2=r-2.}
]

Since (Har C=4) and (ar C^2=H^2=4), orthogonality of the numerical pullback to exceptional curves gives
[
Z^2=c^2-4=r-6,
]
so
[
oxed{-Z^2=6-r.}
]

Thus the former all-ADE correction (6) is only the special case (r=0). Any surviving nonrational passage consumes anticanonical intersection and lowers the total numerical correction.

If (E=sum a_iE_i) and (m_i=cE_i), then
[
r=sum a_im_i,qquad Z=A^{-1}m
]
for (A_{ij}=-E_iE_j), and therefore
[
oxed{m^TA^{-1}m=6-sum_i a_im_i.}
]
This is the central finite-lattice equation once the actual exceptional graph is known. It must be combined with (m_ige0), effectivity/integrality, the first-normal zero budget, and the denominator/Cartier condition.

## D. New structural reduction for Type D

**PROVED from the cited classification.** Every Type D quartic can be written, after choosing coordinates with its irrational point at (p=(1:0:0:0)), as
[
S:quad X_0F_3(X_1,X_2,X_3)=F_4(X_1,X_2,X_3),
]
where (F_4=0) is a smooth plane quartic and (F_3=0) is an effective plane cubic. The resolution is the separation of these two plane divisors.

Consequently a rational quartic (Csubset S) through (p) is controlled by projection from (p). Let
[

u:mathbb P^1	o C,qquad gamma=operatorname{pr}_pcirc
u:mathbb P^1	omathbb P^2.
]
Away from the preimage of (p), containment is exactly
[
X_0circ
u=rac{F_4circgamma}{F_3circgamma}.
]

Therefore:

> **EXACT REDUCTION (Type D).** Classifying Type D carriers containing the fixed rational quartic is equivalent to classifying plane cubic/quartic pairs ((F_3,F_4)), with (F_4) smooth and satisfying the Ishii--Nakayama separation hypotheses, for which the missing projective coordinate of (C) descends as (F_4/F_3) along the projected rational plane cubic.

This converts Type D from an unspecified exceptional-graph problem into a concrete conductor/descent problem on the projected cubic.

For the endpoint (p=[1:0:0:0]) of
[
C_0=[s^4:s^3t:st^3:t^4],
]
projection is the rational cubic
[
[s:t]longmapsto[s^3:st^2:t^3].
]
Writing (A=s^3,B=st^2,C=t^3), the Type D containment equation is
[
s^4F_3(A,B,C)=t,F_4(A,B,C)
]
after removing the common powers contributed by the projection coordinates. This is a finite exact linear condition on the coefficients of (F_3,F_4).

An exact scratch linear-algebra check gives ranks
[
operatorname{rank}(operatorname{res}_3)=9,qquad
operatorname{rank}(operatorname{res}_4)=12,
]
and an 11-dimensional kernel for the combined coefficient equation before quotienting by equations vanishing identically on the projected cubic. This shows that **containment alone does not immediately eliminate Type D**. The next issue is the smoothness/separation condition on (F_4), followed by the Cartier/mate condition.

This scratch calculation is not yet promoted as a repository certificate.

## E. Type-by-type status after this audit

| Type | Source structure | Current status |
|---|---|---|
| B1 | degree-2 generalized del Pezzo; explicit double-cover quartic equation | OPEN; should be attacked through the explicit equation, not arbitrary graph enumeration |
| B2 | degree-1 generalized del Pezzo; B2-1/B2-2 | OPEN |
| B3 | double cover of (mathbb F_1); explicit anticanonical construction | OPEN |
| D | separation of plane quartic/cubic; monoid equation (X_0F_3=F_4) | EXACT REDUCTION to projected-cubic descent plus mate condition |

## F. What is not proved

- No B1/B2/B3/D type is excluded in full by this note.
- The exceptional intersection vector (m=(cE_i)) is not yet classified.
- The exact local Cartier index of (C) at the irrational point is not yet computed.
- The Type D coefficient calculation above establishes only the size of the linear containment incidence at one distinguished point of (C_0); it does not establish normality, the precise Ishii--Nakayama subtype conditions, or existence of an STCI mate.
- Numerical equivalence has not been silently upgraded to linear equivalence except where the existing rational-resolution denominator-compression theorem supplies that implication under a mate hypothesis.

## G. Recommended next attack

Do **not** begin with a free enumeration of negative-definite graphs.

1. Finish Type D first using the explicit monoid model. Compute the projected-cubic conductor condition for a general point (pin C_0), impose smoothness of (F_4), and identify the separation data met by the strict transform of the projected cubic.
2. From that separation, compute (m=(cE_i)), (Z=A^{-1}m), and the exact denominator. If the denominator is (<6), the existing compression theorem immediately contradicts the known mate-degree lower bound.
3. If Type D survives, impose the mate divisor directly on the separated plane model; this should be substantially smaller than searching mate forms in (mathbb P^3).
4. Treat B1 next through its explicit double-cover equation. B2/B3 should remain behind these because their source models are less immediately rigid.

The key conceptual change is that Ishii--Nakayama supplies **birational models with explicit separation data**, not merely four values of ((ho,-E^2)). The remaining classification should exploit those models before lattice enumeration.


## H. Type D separation arithmetic: a rigid multiplicity sequence

Ishii--Nakayama define separation by repeatedly blowing up a point of the current intersection of the transforms of B and G. At each step the intersection number B.G drops by one. Type D starts with a smooth plane quartic B and an effective plane cubic G, so B.G=12. Hence the separation consists of exactly twelve blowup steps, allowing infinitely-near centers.

Use the total-transform basis L,e_1,...,e_12 for Pic(M). Since B is smooth and every separation center lies on its current strict transform, the hyperplane pullback is

    H=D=4L-sum e_i.

The anticanonical exceptional divisor is

    E=3L-sum e_i=-K_M.

Let p be the Type D irrational point on the smooth rational quartic C. Projection from p has degree three, so its plane image R is a cubic. If n_i is the multiplicity of the successive strict transform of R at the i-th separation center, then

    c=3L-sum n_i e_i.

Because H.c=deg C=4,

    12-sum n_i=4,

hence

    sum n_i=8.                                      (D1)

Also

    c.E=9-sum n_i=1.                               (D2)

This already proves:

> **PROVED (Type D anticanonical passage).** Any smooth rational quartic of degree four through the Type D irrational point has strict transform meeting the exceptional anticanonical divisor with total intersection c.E=1.

Adjunction gives

    -2=c.(c+K_M)=c^2-c.E,

so c^2=-1. On the other hand

    c^2=9-sum n_i^2.

Therefore

    sum n_i^2=10.                                  (D3)

Subtracting (D1) from (D3),

    sum n_i(n_i-1)=2.

All n_i are nonnegative integers. Thus exactly one n_i equals 2, no n_i exceeds 2, and the remaining positive n_i are six 1's. Therefore:

> **PROVED (Type D multiplicity theorem).** In the twelve-step separation cluster, the projected cubic R meets exactly seven centers (counting infinitely-near centers): one with multiplicity two and six with multiplicity one. Equivalently the nonzero multiplicity sequence is
>
>     (2,1,1,1,1,1,1)
>
> up to order.

For the endpoint p=[1:0:0:0] of C0, the projected cubic is

    R: y^3=x z^2,

parametrized by [s:t] -> [s^3:s t^2:t^3]. Its unique double point is the image of t=0, i.e. the point corresponding to p. Thus in this endpoint model the multiplicity-two separation center must be that cusp if the separation cluster contains it. The containment identity

    s^4 Phi_3(s^3,s t^2,t^3)
      = t Phi_4(s^3,s t^2,t^3)

indeed forces Phi_3 restricted to R to vanish at t=0, so the cusp belongs to the B/G separation support. Hence the double center is the cusp.

Since E is effective and c.E=1, if E=sum a_j E_j in prime components, then c can meet only coefficient-one components, and the weighted total intersection is one. In particular c meets exactly one coefficient-one component transversely provided c is not itself contained in E (it is not, since H.c=4 while H.E=0).

### Consequence for the numerical correction

The universal intrinsic equation specializes in Type D to

    -Z^2=6-c.E=5,

or, for m_j=c.E_j and A=(-E_i.E_j),

    m^T A^(-1)m=5.

Write the exceptional locus as the disjoint union of the block over the irrational monoid point and the blocks over any rational double points met by c. The equality c.E=1 constrains only the irrational block. It implies that inside Supp(E), c meets exactly one coefficient-one component once. It does NOT imply that the full exceptional intersection vector m is supported there: c may also meet coefficient-zero exceptional curves over Du Val singularities. Accordingly the total correction 5 splits as

    delta_p + delta_ADE = 5,

where delta_p is the correction at the monoid point. The earlier draft's stronger assertion (A^(-1))_{jj}=5 for the irrational block alone was false and is superseded by this block decomposition.

### Scope

The calculation uses only the Type D separation construction, degree of the projected curve, H.c=4, K_M=-E, and adjunction. It does not assume B and G meet transversely, does not assume twelve distinct proper points, and does not yet determine the proximity graph of the twelve centers. That proximity graph is precisely what is needed to compute A^(-1)e_j and finish the Cartier-index test.


## I. Type D: literature compression and first-normal split

### I.1 External classification of quartic monoids

Johansen--Løberg--Piene, *Monoid hypersurfaces*, classify the complex tangent cubic of a quartic monoid into nine types: nodal cubic, cuspidal cubic, conic plus chord, conic plus tangent line, three general lines, three concurrent lines, double line plus line, triple line, and smooth cubic. Their Theorem 9 also gives the complete possibilities for singularities away from the monoid point. In every case those additional singularities are of type A_n, with n determined by residual intersection multiplicities of the tangent cubic and quartic.

Thus for Type D the rational exceptional blocks relevant to c are A-type only. This is stronger than the generic ADE allowance used in the earlier budget.

### I.2 Local expansion at the endpoint of C0

Take p=[1:0:0:0] and q=t/s. Near p,

    C0(q)=[1:q:q^3:q^4].

Put plane coordinates [x:y:z]=[X1:X2:X3]. Projection from p is

    [x:y:z]=[1:q^2:q^3]

after dividing by q. Let

    g(q)=Phi_3(1,q^2,q^3),
    b(q)=Phi_4(1,q^2,q^3).

The monoid containment equation X0 Phi_3=Phi_4 becomes

    g(q)=q b(q).                                    (D4)

Since g has no q^1 term, (D4) forces b(0)=0. Hence the smooth plane quartic B passes through the cusp point [1:0:0] of the projected cubic.

Because B is smooth there, its restriction b(q) has order either 2 or 3 according as its linear term contains y or only z. Consequently g(q) has order respectively 3 or at least 4.

In affine coordinates (u,v,w)=(X1/X0,X2/X0,X3/X0)=(q,q^3,q^4), the carrier equation is

    f(u,v,w)=Phi_3(u,v,w)-Phi_4(u,v,w).

If ord b=2, the identity permits an x^2 z term in Phi_3; then partial f/partial w can have order 2 along C0. If ord b>=3, all first partials have order at least 3 along C0. Therefore:

> **PROVED (endpoint first-normal split).** The Type D monoid point consumes first-normal order at least 2. It consumes at least 3 unless the smooth quartic B has order exactly 2 on the projected cusp.

The global quartic first-normal budget is at most 9 (or 9-e in the refined order-one notation). Thus the A-type singularities away from p have total first-normal budget at most 7 in the order-2 subcase and at most 6 in the order-at-least-3 subcase.

### I.3 Correction at the irrational block

Let A_p be the negative intersection matrix of the exceptional block over p and write E=sum a_i E_i there. Since c.E=1, c meets a unique component E_j with a_j=1, once, and no other component of Supp(E). Thus

    delta_p=(A_p^(-1))_{jj}.

The component met by c is the component reached by the tangent direction of the projected cubic after separation. At the initial cusp center it comes from a reduced local branch of the tangent cubic. For a coefficient-one strict-transform component R of plane degree d=1,2,3, adjunction/separation gives -E.R=K_M.R>=1. Since

    A_p a = (-E.E_i)_i >=0

and its j-th entry is at least one, positivity of A_p^(-1) gives

    A_p^(-1)e_j <= a

componentwise. In particular

    delta_p <= a_j=1.

This comparison is valid when the component met by c is such a reduced strict-transform component. The remaining possibility that the tangent direction terminates on a coefficient-one (-2)-component created by a nonreduced/infinitely-near separation needs a separate check; it is not silently included.

### I.4 Harmonic consequence

Let N be the total A-root rank away from p and P their total first-normal order. Since rho(M)=13 and the irrational block has positive rank,

    N<=11.

The existing harmonic estimate gives

    delta_A <= N P/(N+P).

In the order-at-least-3 subcase, P<=6, hence

    delta_A <= 66/17 < 4.

If delta_p<=1 as in I.3, the mate relation requires

    delta_A=5-delta_p >=4,

a contradiction, with exact gap at least 2/17.

Therefore:

> **CONDITIONAL EXCLUSION.** Type D is excluded whenever (i) the endpoint monoid passage has first-normal order at least 3 and (ii) c meets a reduced coefficient-one strict-transform component of the tangent cubic.

The only endpoint configurations still requiring analysis are:
- the first-normal-order-2 case (ord b=2), where the coarse harmonic bound with P<=7 is not by itself contradictory; and
- any nonreduced/infinitely-near configuration in which the component met by c is a coefficient-one (-2)-curve, for which delta_p<=1 has not yet been justified.

This is now a small local problem. The monoid classification suggests treating it case-by-case through the nine tangent-cubic types rather than enumerating arbitrary negative-definite graphs.


## J. Type D: sharp Bezout correction bound

For a normalized quartic monoid, every isolated singularity away from the monoid point is A-type. If the tangent cubic G and quartic B have local intersection multiplicity m at the corresponding base point, the singularity is A_{m-1}. Hence for the off-vertex singularities met by c,

    sum (n_i+1) <= B.G = 12.

For Jaffe's A_n^k pair,

    delta(n,k)=k(n+1-k)/(n+1) <= (n+1)/4.

Therefore

    delta_off <= 3.                                (D5)

Since the total correction is 5,

    delta_p = 5-delta_off >= 2.                    (D6)

Thus every Type D STCI survivor must have correction at least two at the irrational monoid point.

### Endpoint order-two passage

In the endpoint notation, the first-normal-order-two case has ord b=2 and ord g=3 on the projected cusp (y,z)=(q^2,q^3). Smoothness of B makes its linear term a nonzero y-term, while the order-three identity makes G have a nonzero z-linear term. Thus B and G are smooth and transverse at the cusp, so their separation has exactly one blowup there.

The projected cusp is tangent to G. After the blowup, its strict transform still meets the reduced coefficient-one strict transform of G once. Hence the anticanonical comparison of I.3 applies and gives delta_p<=1, contradicting (D6).

> **PROVED (endpoint order-two exclusion).** No Type D STCI candidate with the irrational point at the endpoint [1:0:0:0] can lie in the first-normal-order-two branch.

Every endpoint survivor must therefore have first-normal order at least three and, by (D6), local irrational correction at least two. The remaining finite question is whether the cusp-following separation for one of the nine tangent-cubic types can land c on a coefficient-one exceptional component with inverse-matrix diagonal at least two. If such a component exists, its inverse column also gives the exact Cartier denominator for the compression test.


## K. Type D endpoint exclusion completed

This section finishes the Type D analysis when the irrational triple point is the endpoint p=[1:0:0:0] of C0.

### K.1 Exact local shape in the remaining branch

In the order-at-least-three branch of I.2, B is smooth at the projected cusp a and its restriction to R has order exactly three. Indeed the y-linear coefficient must vanish, while the z-linear coefficient is nonzero by smoothness. Thus

    ord_R(B)=3,
    ord_R(G)=4

by the containment identity g=q b.

In local cusp coordinates (y,z)=(q^2,q^3), order four for a cubic G means that its first nonzero term is a nonzero multiple of y^2. Hence G has multiplicity exactly two at a and has double tangent y=0. In particular the multiplicity-three tangent-cubic configurations (triple line, or the intersection point of a double line with another component) cannot occur at a.

The possible local forms are therefore:
1. an irreducible cuspidal branch;
2. two reduced tangent branches (the conic-plus-tangent-line type);
3. a smooth point of a double line.

### K.2 The separation over a

Ishii--Nakayama separation uses

    B_{j+1}=rho^* B_j - Gamma,
    G_{j+1}=rho^* G_j - Gamma,

not merely the strict transform of G. Consequently B_j.G_j drops by exactly one at each blowup. Since B is transverse to the double tangent direction of G, I_a(B,G)=2. Exactly two separation blowups occur over a.

After the first blowup,

    G_1 = G_strict + F_1

in the reduced multiplicity-two cases. B_1 meets F_1 at the B tangent direction, while the strict transform of the projected cusp meets F_1 at the distinct G tangent direction. The second blowup is therefore at B_1 cap F_1 and misses c. After it, the component met by c is the coefficient-one curve F with

    F^2=-2.

Thus the exceptional (-2)-curve found in the previous section is real, but its correction can be computed explicitly from the adjacent strict transform(s) of G.

### K.3 Local correction in the three cases

**Irreducible cusp.** The strict transform Q of the cubic loses 2^2 at a and one square for each of the remaining ten units of B.G, hence

    Q^2 = 9-4-10 = -5.

Moreover Q.F=2. The relevant block is

    A = [[5,-2],[-2,2]],

so

    delta_p = (A^{-1})_{FF}=5/6.

**Two reduced tangent branches.** The branches are a line and a conic. The previous draft incorrectly asserted that adding negative-definite attachments could only decrease the diagonal Green value at F. That monotonicity statement is false and is superseded here.

Let r and s be the remaining separation lengths assigned to the line and conic branches after the two cusp blowups. Since the residual B.G intersection is ten, r+s=10. In the total-transform calculation the relevant three-vertex Schur block has diagonal entries r, s-3, 2 and F meets each branch once. Negative definiteness leaves r=1,...,6. Direct inversion gives respectively

    delta_p = 6/5, 10/13, 12/17, 12/17, 10/13, 6/5.

Thus in every admissible allocation

    delta_p <= 6/5 < 2.

This finite calculation replaces the false monotonicity argument. Infinitely-near distribution along a fixed branch does not change the Schur-complement value: successive separation curves contract back to the same effective self-intersection contribution determined by the total separation length on that branch.

**Double line.** At a smooth point of the doubled line, F meets the line once. The line strict transform has square at most -3. The two-vertex comparison gives

    delta_p <= ([[3,-1],[-1,2]]^{-1})_{FF}=3/5.

The other line does not pass through a (otherwise mult_a G=3); including its attachment to the doubled line does not approach the required value two.

Thus every admissible local multiplicity-two form satisfies

    delta_p <= 6/5 < 2.

But J.1 gives the necessary inequality delta_p>=2. Therefore:

> **PROVED (Type D endpoint exclusion).** No Type D normal quartic STCI carrier can have its irrational triple point at the endpoint p=[1:0:0:0] of C0.

The remaining Type D question is whether an arbitrary point p in C0 reduces to the same local pattern after projection, or whether interior points produce a nodal rather than cuspidal projected cubic and require a separate calculation.


## L. Type D at a general point of C0: nodal projection and contact tradeoff

Let p=C0(a) with a nonzero finite parameter, so

    C0(u)=[1:u:u^3:u^4].

Projection from p can be represented by the three linear forms

    X1-a X0,  X2-a^3 X0,  X3-a^4 X0.

After cancelling u-a, the projected cubic R has parametrization

    [1 : u^2+a u+a^2 : (u+a)(u^2+a^2)].

The two distinct parameters

    u=a omega,  u=a omega^2,   omega^3=1, omega!=1,

have the same image. Thus for a!=0,infinity the projected cubic is nodal. The marked image r of p itself is smooth: its parameter value u=a has no second preimage.

### L.1 Local monoid identity at the marked smooth point

Put q=u-a. In projection coordinates the normalization near r is

    [1 : 3a^2+3a q+q^2 : 4a^3+6a^2 q+4a q^2+q^3].

The coordinate along the line through p has a simple pole in q. Hence the Type D equation again restricts to

    g(q)=q b(q),                                   (D7)

where b=B|_R and g=G|_R.

Unlike the endpoint cusp, the local ring of R at r is regular, so there is no semigroup gap forcing b(0)=0.

If b(0)!=0, then g has a simple zero. Thus G is smooth and transverse to R at r, while B misses r. No B/G separation blowup occurs over r. The strict transform c meets a reduced coefficient-one component of the anticanonical divisor directly, so the anticanonical comparison gives

    delta_p<=1.

This contradicts the universal Type D necessity delta_p>=2 from (D6). Therefore every general-point survivor must satisfy

    b(0)=0.

### L.2 Local normal form and contact accounting

Because R is smooth at r, choose local coordinates with R=(y=0), x=q. Since B is smooth, after a local coordinate normalization write

    B = y + beta(x),

where h=ord_x beta>=1 is the contact order I_r(B,R).

Equation (D7) says G(x,0)=x beta(x). Therefore locally

    G = x B + y A

for some local function A (after absorbing units/signs). In particular

    I_r(R,G)=h+1.                                  (D8)

Since deg R=deg G=3,

    R.G=9,

so

    1<=h<=8.                                       (D9)

This is the correct finite parameter for the general-point Type D problem.

There is also a compensation with the off-vertex correction. Let mu=I_r(B,G), i.e. the number of Ishii--Nakayama separation steps over r. Then only 12-mu units of the global B.G=12 intersection remain available away from r. The monoid A-type estimate sharpens from (D5) to

    delta_off <= (12-mu)/4.                        (D10)

Hence the mate relation forces

    delta_p >= 5-(12-mu)/4 = 2+mu/4.              (D11)

So increasing the local B/G contact makes the required irrational correction grow linearly. The remaining task is to bound the actual local Green value delta_p from above in terms of the same separation length mu (or the contact h). If one proves

    delta_p < 2+mu/4

for every 1<=h<=8 and every cubic local form compatible with G=xB+yA, Type D is excluded for every point of C0.

This is now a finite local inequality rather than a global quartic-carrier classification problem.

### L.3 Audit note

Earlier conversational exploration incorrectly suggested that (D7) forces B through r in the nodal case. It does not; that conclusion used the cusp semigroup at the endpoint. The present note records the corrected distinction explicitly.


## M. General-point Type D: local separation algebra

Continue with the local normal form

    R=(y=0),
    B=y+beta(x),    ord beta=h>=1,
    G=xB+yA.

Restricting G to B gives

    G|_B = -beta(x) A(x,-beta(x)).

Hence, provided B is not a component of G,

    mu=I_r(B,G)=h+alpha,                            (D12)

where

    alpha=ord_x A(x,-beta(x))>=0.

This identifies the separation length directly from the two local contacts.

### M.1 Reduced one-branch case

Suppose the component of G followed by c is reduced and locally irreducible at r, and the B/G separation over r does not branch. Successive separation blowups then give a linear chain attached to the strict transform Q of that component. After contracting the portions of the chain not met by c, the negative intersection matrix is represented by the continued fraction with initial diagonal at least 3 and mu successive 2's.

The largest possible Green value occurs for initial diagonal 3. Direct inversion gives

    delta_p <= (2 mu+1)/(2 mu+3) < 1.              (D13)

For mu=1,...,8 the values are

    3/5, 5/7, 7/9, 9/11, 11/13, 13/15, 15/17, 17/19.

But the global Bezout tradeoff (D11) requires

    delta_p >= 2+mu/4 >2.

Therefore:

> **PROVED (general-point, unbranched reduced local form).** No Type D STCI candidate can have the marked smooth point r lying on a locally irreducible reduced branch of G whose B/G separation tree over r is linear.

This includes the generic smooth-G situation and any reduced singular branch once its resolution/separation path followed by c is unbranched.

### M.2 Remaining local configurations

A general-point Type D survivor must therefore make the anticanonical separation tree branch at r. For a plane cubic this means that, locally at r, G is one of:

- two reduced branches (node or two components);
- three reduced branches;
- a double component plus another branch;
- a triple component.

The marked curve R itself is smooth at r. Equation I_r(R,G)=h+1 and the cubic degree constrain the sum of contacts of these branches with R. Together with (D12), this leaves a finite list of contact partitions.

The next computation should enumerate those partitions, build the corresponding star/chain negative matrices, and compare each exact diagonal Green value with 2+mu/4. This is substantially smaller than the nine global tangent-cubic types because only the local branch multiplicities at r matter.


## N. General-point branching bound

This section closes the local branching alternatives left in M.2, subject to the matrix interpretation stated there.

Because R is not a component of G, I_r(R,G) is finite. If mult_r(G)=3, then a plane cubic has no terms of degree below three at r; its local equation is its cubic tangent cone. Restriction to the smooth branch R=(y=0) therefore has order exactly three unless y divides G, which would make R a component. Hence

    h+1=3, so h=2.                                 (D14)

Thus multiplicity-three local forms do not generate arbitrarily long contact sequences.

### N.1 Reduced branching

Suppose the coefficient-one (-2)-curve F met by c is adjacent to k reduced branches of G. A reduced cubic branch, after the full B/G separation, contributes an effective negative diagonal at least 3 at the attachment. The Green value at F is therefore bounded by the corresponding star Schur complement.

For two branches,

    delta_p <= 1/(2-1/3-1/3)=3/4.

For three branches,

    delta_p <= 1/(2-1/3-1/3-1/3)=1.

The endpoint finite calculation shows how further separation along a branch is absorbed into its effective diagonal; with fixed cubic self-intersection and the B.G budget it does not make a reduced branch contribution exceed the extremal 1/3 used above.

Hence every reduced branching configuration has

    delta_p<=1.                                    (D15)

### N.2 Nonreduced adjacency

If F is adjacent to a doubled component, the corresponding intersection entry can have magnitude two. The worst negative-definite two-vertex block is

    A=[[3,-2],[-2,2]],

whose inverse has

    (A^{-1})_{FF}=3/2.

Larger branch diagonal only decreases this value. Thus

    delta_p<=3/2                                   (D16)

for doubled adjacency before any further constraints are imposed.

A triple adjacency would require an off-diagonal magnitude three. With F^2=-2 and a cubic-component diagonal in the available range, the corresponding principal minor fails negative definiteness; it cannot occur as such an exceptional block. Multiplicity-three cubic configurations are in any case constrained by (D14).

### N.3 Consequence

Combining the unbranched reduced estimate (D13), reduced branching (D15), and nonreduced estimate (D16), every general-point local configuration satisfies

    delta_p<=3/2.

But the global B/G Bezout tradeoff requires

    delta_p>=2+mu/4>2.

Therefore:

> **PROVED, subject to independent audit of the branch-effective-diagonal lemma.** No Type D normal quartic STCI carrier can have its irrational point at an interior point p=C0(a), a!=0,infinity.

Together with the endpoint exclusion, this would remove Type D completely for C0. Before promoting this to the canonical STATE, the branch-effective-diagonal assertion used in N.1 should be checked directly from the Ishii--Nakayama proximity basis (or by a small exhaustive proximity-matrix certificate). That check is preferable to relying on electrical-network intuition.

### N.4 Next audit target

Build an exact certificate enumerating the admissible separation/proximity matrices for a degree-three G with total B.G=12, marking the component reached by c, and verify:
1. negative definiteness;
2. E=-K coefficient vector;
3. the relevant diagonal of A^{-1};
4. the maximum is at most 3/2 in the general-point cases and at most 6/5 in the endpoint cases.

A successful certificate would promote the Type D exclusion from branch-level geometric proof to independently checked PROVED status.


## O. Audit of the general-point bound: blowup coefficients and a corrected target

The proposed proximity enumeration in N.4 can be constrained much more strongly by tracking the anticanonical divisor itself.

If rho:M'->M blows up a separation center q with exceptional curve F, then

    -K_{M'} = rho^*(-K_M) - F.

Writing E=-K_M, if the total multiplicity of E at q is s, the coefficient of F in the new anticanonical divisor is

    a_F=s-1.                                       (D17)

Thus:
- a smooth point of a coefficient-one component (s=1) creates a coefficient-zero exceptional;
- an anticanonical multiplicity-two center creates a coefficient-one exceptional;
- a multiplicity-three center creates a coefficient-two exceptional.

This corrects the informal picture used in parts of M--N. In particular, because c.E=1, the component met by c must have coefficient one. It cannot be an exceptional created directly at a multiplicity-three center. A triple-point local form can contribute only if the c-direction subsequently reaches a multiplicity-two center.

### O.1 Intrinsic lattice constraints

For the irrational block let A be the negative intersection matrix and a the positive coefficient vector of E. Type D has

    E^2=-3,

hence

    a^T A a=3.                                     (D18)

Moreover

    A a = (-E.E_i)_i >=0                           (D19)

on the exceptional anticanonical block, and if c meets E_j then

    a_j=1,
    delta_p=(A^{-1})_{jj}.                          (D20)

Equations (D18)--(D20), together with the blowup recursion (D17), are the correct constraints for an exact certificate. They are substantially stronger than arbitrary negative definiteness.

### O.2 Status correction

The numerical star estimates in N remain useful evidence, but the claimed universal bound delta_p<=3/2 has not yet been independently proved: arbitrary graph enumeration is too broad, while the earlier effective-diagonal argument omitted the coefficient recursion (D17).

Accordingly the general-point Type D exclusion should remain

> **CONDITIONAL.** It follows once one proves, for anticanonical cycles obtainable from the degree-three separation process and satisfying (D17)--(D20), that the coefficient-one vertex reached by c has delta_p<2+mu/4.

The endpoint exclusion in K is unaffected; it was computed from its explicit finite separation configurations.

### O.3 Sharper next certificate

A correct exhaustive certificate need only generate separation states carrying:
1. the strict-transform components of the degree-three plane divisor G and their multiplicities;
2. exceptional components with coefficients generated by a_F=s-1;
3. self-intersections/proximities under at most twelve B/G separation blowups;
4. the marked tangent direction followed by c.

At each terminal state one checks (D18)--(D20) and computes the exact rational value (A^{-1})_{jj}. This is a finite state space and avoids enumerating arbitrary negative-definite trees.


## P. Intrinsic reduction of the remaining general-point certificate

The blowup recursion can be compressed further using the anticanonical equations themselves.

Let F=E_j be the component met by c. Since a_j=1,

    1 = a_j = sum_i (A^{-1})_{ji} b_i,

where b=Aa and b_i=-E.E_i>=0. The inverse of the connected negative intersection M-matrix is entrywise nonnegative. Therefore, if b_j>=1,

    delta_p=(A^{-1})_{jj} <= 1.

Such a component cannot survive (D11). Hence every survivor must satisfy

    b_j=-E.F=0.

Adjunction then identifies F as a rational (-2)-curve.

### P.1 Weighted-adjacency dichotomy

Because F has coefficient one and F^2=-2,

    0=E.F=-2 + sum_{D adjacent F} a_D (F.D).

Thus the weighted adjacency sum is exactly two. There are only two local boundary patterns:

(A) F meets one coefficient-two component transversely once; or

(B) F meets two coefficient-one components transversely once each,

with the equivalent possibility of total intersection multiplicity two with one coefficient-one component.

This is intrinsic and replaces the arbitrary star enumeration in N.

### P.2 Pattern B

For the minimal three-vertex block with coefficient vector (1,1,1), F central, E^2=-3 and Aa>=0 force the neighboring negative self-intersections to be (2,3) up to order. Exact inversion gives

    delta_p=6/7.

Further anticanonical attachments must preserve Aa>=0 and total energy a^T A a=3; they cannot be inserted freely. A complete proof that they do not raise delta_p above the threshold should follow by pruning coefficient-one leaves using the same adjunction equations. This is now a much smaller lattice lemma.

### P.3 Pattern A

The minimal two-vertex block with coefficient vector (1,2) cannot satisfy E^2=-3 and Aa>=0 for any integral neighbor self-intersection. Hence pattern A necessarily contains additional anticanonical structure.

Geometrically the coefficient-two neighbor can only be produced by a blowup at anticanonical multiplicity three. Since c.E=1, the marked direction cannot terminate there. To reach F it must subsequently pass through a multiplicity-two center, which creates the coefficient-one (-2)-curve F. Thus any pattern-A survivor contains a forced two-stage proximity motif:

    multiplicity 3 center -> coefficient 2 component
    followed along c by
    multiplicity 2 center -> coefficient 1 (-2) component F.

The remaining certificate has therefore collapsed to two tiny tasks:
1. prove the pruning lemma for pattern B;
2. enumerate the degree-three multiplicity-three centers compatible with the forced pattern-A motif.

No enumeration of all twelve-step proximity matrices is required.


## P. Potential-theoretic reduction and an adjunction caveat

Let F=E_j be the coefficient-one component met by c and put

    b=Aa=(-E.E_i)_i.

Since a=A^{-1}b and a_j=1,

    1 = sum_i (A^{-1})_{ji} b_i.                  (D21)

If b_j>=1, positivity of A^{-1} immediately gives

    delta_p=(A^{-1})_{jj}<=1.

Hence every possible survivor has b_j=0. For a blowup-created smooth rational component F, adjunction then gives F^2=-2. The anticanonical equation E.F=0 and a_F=1 forces the weighted neighboring coefficient sum to equal two. Thus only the local motifs

    1+1   or   2

can occur at F.

If z=A^{-1}e_j, then on any chain of blowup-created coefficient-one (-2)-curves with b=0,

    2 z_i = z_{i-1}+z_{i+1}.

Thus z is affine along such zero-charge chains. Equation (D21) says that the boundary values are normalized by the total anticanonical charge:

    sum_i z_i b_i=1.

This is the correct discrete-potential formulation of the remaining Type D problem.

### P.1 Important adjunction caveat

One must not replace b_i by (-E_i^2-2) on every vertex of the irrational block. The strict transforms of components of the plane cubic G can themselves be singular (for example nodal or cuspidal), and G can be nonreduced. The smooth-rational adjunction formula applies without qualification only to the exceptional curves created by blowups (and to strict-transform components separately known to be smooth rational).

A brute-force search that imposes b_i=d_i-2 on the entire block therefore searches the wrong class and can even return an empty state space. Such a failed search is not evidence for exclusion.

### P.2 Correct proof architecture

Separate the irrational block into:
1. the blowup-created rational tree T, on which the zero-charge (-2) potential recurrence is exact; and
2. the strict transforms of the original components of G, treated as boundary vertices with coefficients and intersection data inherited from the plane cubic.

The marked vertex F lies in T in the only unresolved cases. The desired bound delta_p<2+mu/4 can therefore be proved by eliminating T via continued fractions/Schur complements and checking the finite list of possible cubic boundary types. This is smaller and safer than enumerating arbitrary proximity matrices.

The next calculation should compute the effective conductance from F through T to each original G component for the local multiplicity-three configurations and the 2-to-1 coefficient transition. No canonical-state promotion should occur before that boundary calculation is complete.


## Q. Exact elimination of blowup-created (-2)-chains

The conditional Type D audit can be compressed further by eliminating every zero-charge rational (-2)-chain exactly.

Let F be the coefficient-one (-2)-component met by c. Suppose a chain of r blowup-created (-2)-curves lies between F and a boundary component D. The A_r Cartan block has inverse

    (A_r^{-1})_{ij}=min(i,j)(r+1-max(i,j))/(r+1).

Schur elimination therefore subtracts

    r/(r+1)

from each endpoint diagonal and replaces the path by an effective off-diagonal

    -1/(r+1).                                      (D21)

This corrects another unsafe monotonicity heuristic: a longer (-2)-tail can lower the effective diagonal at F and hence increase its Green value. Extra separation blowups cannot simply be discarded.

### Q.1 Anticanonical coefficients restrict the chain lengths

On a zero-charge (-2)-chain, Aa=b with b_i=0 gives

    2a_i=a_{i-1}+a_{i+1}.                          (D22)

Thus the positive integral anticanonical coefficients are affine along the chain.

Starting at a_F=1 and ending at a boundary coefficient m, a chain with r internal vertices has

    a_k=1+k(m-1)/(r+1).

Consequently integrality gives:

- m=1: arbitrary r is arithmetically possible, with every internal coefficient equal to 1;
- m=2: no nonempty zero-charge (-2)-chain is possible;
- m=3: the only nonempty possibility has r=1 and coefficient sequence 1--2--3.

So a coefficient-two original/boundary component must be directly adjacent to F. A coefficient-three boundary can be separated from F by at most one zero-charge (-2)-vertex. The only potentially long tails are constant coefficient-one chains.

### Q.2 Remaining obstruction is coefficient-one tails

This isolates the genuine unresolved case. A long coefficient-one (-2)-chain can connect F to a coefficient-one boundary component without violating (D22). Its Schur contribution approaches one as its length grows, so an abstract lattice argument alone does not yet give delta_p<2.

The plane-cubic geometry must now be used precisely once: determine whether such a constant coefficient-one chain can occur along the marked tangent direction in the Ishii--Nakayama B/G separation process, and if so bound its length/contact by I_r(R,G)=h+1 and the local separation multiplicity mu.

Thus the certificate no longer needs arbitrary proximity trees. It needs only:
1. direct coefficient-2 attachments;
2. the unique 1--2--3 short chain;
3. constant coefficient-one (-2)-chains, whose lengths are controlled by the local plane-curve contact data.

This is the smallest audited formulation reached so far.


## Q. Two-arm coefficient-one tails: exact comparison

The remaining dangerous lattice motif is a coefficient-one (-2)-curve F met by c with two coefficient-one zero-charge arms. Pure lattice theory alone does not bound its Green value below 2: two sufficiently long arms can make (A^{-1})_{FF}>2. Thus the B/G separation budget is essential.

Collapse an arm of r coefficient-one (-2)-curves terminating at a boundary with effective diagonal d>=3. In the extremal case d=3 its Schur load at F is

    lambda_r=(2r+1)/(2r+3).

Hence for two arms of lengths r,s the worst Green value is

    delta_F
      =1/(2-lambda_r-lambda_s)
      =((2r+3)(2s+3))/(4(r+s+3)).                 (D21)

Put t=r+s. By AM-GM,

    (2r+3)(2s+3) <= (r+s+3)^2=(t+3)^2,

so

    delta_F <= (t+3)/4.                            (D22)

Each zero-charge arm vertex arises from a B/G separation blowup, so the local separation length satisfies

    mu >= r+s=t.                                   (D23)

The global Bezout tradeoff requires

    delta_p >= 2+mu/4 >= (t+8)/4.                  (D24)

Comparing (D22) and (D24) leaves a uniform gap 5/4. Therefore no two-arm coefficient-one tail can survive, provided the terminal effective boundary on each arm has diagonal at least 3.

This is stronger than a finite mu<=12 check: it holds for arbitrary arm lengths.

### Q.1 Exact remaining audit point

The only unproved input in this reduction is the terminal-response assertion

    d_eff >= 3.                                    (D25)

It must be verified for the finite list of original degree-three G boundary germs allowed by the Ishii--Nakayama Type D separation process. It should not be assumed from rational-component adjunction, because an original cubic component can be singular or nonreduced.

Thus the general-point Type D exclusion is now conditional on one finite boundary calculation: prove (D25) for each original cubic boundary type reached by a coefficient-one arm. Once (D25) is established, (D21)--(D24) eliminate the last 1+1 motif, while the direct coefficient-two motifs are handled separately by the coefficient recursion.


---

## 2026-10-07-rational-quartic-power-saturation

# Powers of the rational quartic ideal: saturation from degree 3m

Date: 2026-10-07
Status: PROVED

Let C be the smooth rational quartic in P3, Q its unique smooth quadric, and I its homogeneous ideal / ideal sheaf as context dictates. On Q, C has class (1,3).

The homogeneous ideal is generated by Q in degree 2 and three cubics. Modulo Q, the cubic generators span H^0(Q,O_Q(2,0)) after factoring the equation h of C on Q.

## Theorem

For every m>=0 and every d>=3m,
\[
H^0(P^3,\mathcal I_C^m(d))=(I_C^m)_d.
\]
Moreover
\[
H^1(P^3,\mathcal I_C^m(d))=0
\]
for every d>=3m.

Equivalently, the saturation/symbolic defect
\[
I_C^{(m)}/I_C^m
\]
has no graded component in degree >=3m.

## 1. Exact sequence through the quadric

Because C is Cartier on Q and locally I_C=(Q,h), for every m>=1 there is an exact sequence
\[
0\to\mathcal I_C^{m-1}(-2)
\xrightarrow{\cdot Q}
\mathcal I_C^m
\to O_Q(-mC)\to0.
\]
After twisting by d:
\[
0\to\mathcal I_C^{m-1}(d-2)
\to\mathcal I_C^m(d)
\to O_Q(d-m,d-3m)\to0.                 (*)
\]

The kernel statement also follows from the previously proved sheaf colon identity
\[
(\mathcal I_C^m:Q)=\mathcal I_C^{m-1}.
\]

## 2. H1 vanishing

Assume d>=3m. Then
\[
d-m>=2m>=0,\qquad d-3m>=0,
\]
so
\[
H^1(Q,O_Q(d-m,d-3m))=0.
\]

Also
\[
d-2 >= 3m-2 = 3(m-1)+1 >=3(m-1).
\]
Induction on m, starting from m=0, therefore gives
\[
H^1(P^3,\mathcal I_C^{m-1}(d-2))=0.
\]
The long exact sequence of (*) yields
\[
H^1(P^3,\mathcal I_C^m(d))=0.
\]

Thus restriction in (*) is surjective on H0.

## 3. Ordinary powers already surject onto the quadric quotient

Write e=d-3m>=0. The quotient is
\[
O_Q(2m+e,e).
\]

Products of m cubic equations of C restrict, after factoring h^m, onto
\[
H^0(Q,O_Q(2m,0)),
\]
because Sym^m H^0(P1,O(2)) -> H^0(P1,O(2m)) is surjective.

Multiply these products by arbitrary ambient forms of degree e. The restriction
\[
H^0(P^3,O(e))\to H^0(Q,O_Q(e,e))
\]
is surjective, and multiplication
\[
H^0(O_Q(2m,0))\otimes H^0(O_Q(e,e))
\to H^0(O_Q(2m+e,e))
\]
is surjective.

Hence the ordinary homogeneous power (I_C^m)_d already maps onto the full right-hand H0 term of (*).

## 4. Induction for saturation

Take any
\[
F\in H^0(\mathcal I_C^m(d)).
\]
Choose
\[
F_0\in(I_C^m)_d
\]
with the same restriction to the quotient O_Q(d-m,d-3m). Then
\[
F-F_0=QK
\]
with
\[
K\in H^0(\mathcal I_C^{m-1}(d-2)).
\]

Since d-2>=3(m-1), induction gives
\[
K\in(I_C^{m-1})_{d-2}.
\]
Therefore
\[
QK\in(I_C^m)_d,
\]
and hence F lies in the ordinary power.

This proves the theorem.

## 5. Boundary colon recursion

Set m=p-1. Since
\[
3p-2=3m+1>=3m,
\]
the theorem gives
\[
H^0(\mathcal I^{p-1}(3p-2))
=(I^{p-1})_{3p-2}.
\]

Combining this with the sheaf colon identity proves the homogeneous degree-specific colon identity
\[
\boxed{(I^p:Q)_{3p-2}=(I^{p-1})_{3p-2}.}
\]

Consequently
\[
(I^p)_{3p}\cap(Q)
=
Q\,(I^{p-1})_{3p-2}.
\]

## 6. Exact recursive description of degree-3p carriers

The previous quotient calculation gives
\[
(I^p)_{3p}/Q(I^{p-1})_{3p-2}
\simeq H^0(Q,O_Q(2p,0)).
\]

Thus every degree-3p carrier of order at least p can be written
\[
F=F_{\rm cub}+QK,
\]
where F_cub is a linear combination of products of p cubic equations of C and
\[
K\in(I^{p-1})_{3p-2}.
\]

For an equality-boundary STCI pair, the image of F_cub modulo Q is further constrained to a binary form of degree 2p with at most min(p,q) distinct roots.

## 7. Strategic meaning

The entire degree-3p F-carrier space is now recursively understood at the level of ordinary powers. There is no hidden symbolic/saturation correction at or above degree 3p.

This does not classify singularities or normalization of F, because the kernel Q(I^{p-1})_{3p-2} remains large. But it removes the previously open Rees/saturation ambiguity and gives an exact algebraic parameterization suitable for singularity or mate-compatibility analysis.
