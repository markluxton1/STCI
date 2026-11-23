# Spectral interpolation and the redundancy of opposite Chow polarizations

**Status (2026-11-23):** exact elementary consequences of the two lower-degree polarized Chow systems; **pending independent mathematical review**. No unrestricted first-moment vanishing or STCI exclusion. Characteristic zero throughout.

**Existing mathematics applied first.** The algebraic inputs are the logarithmic derivative of a split binary form, partial fractions/Hermite interpolation (equivalently the Chinese remainder theorem for coprime powers of linear factors), and the standard fact that a Cohen–Macaulay unmixed ideal contracts from an open meeting all its associated primes. The project-specific initial polarizations, their normalizations, and their global support envelopes are [owned here](weighted_chow_quadric_cubic_polarizations.md); the accepted reduced invariant-ideal and moment theorems remain [here](chow_arrangement_moments.md). The inverse-coordinate interpretation is the same classical Hermite-interpolation mechanism, **not a new form of interpolation theory**.

## 1. The two first polarizations need only one extra polynomial

Let \(\sigma=\sum_i n_i[(u_i,v_i)]\), \(m=\sum n_i\), put
\[
 \xi_i=u_i/v_i,\quad A=x_1x_2,\quad B=x_0x_3,\quad
 Q_i=A-\xi_iB,\quad H(A,B)=\prod_iQ_i^{n_i},
\]
and let \(H_i=H/Q_i\), retaining repeated components. Define the homogeneous degree-\((m-1)\) **paired interpolation form**
\[
 \tag{1}
 \boxed{K(A,B)=\sum_i\frac{n_i}{u_i}H_i(A,B).}
\]
Set
\[
 L(A,B)=\sum_i n_i\xi_i^2 H_i(A,B),\qquad
 M_1=\sum_i n_i\xi_i=-H_B(1,0).
\]
Since \(H_A=\sum_i n_iH_i\) and \(H_B=-\sum_i n_i\xi_iH_i\), the first normalized opposite cubics
\[
 E_+=\sum_i\frac{n_i}{u_i}
    (x_0^2x_2-u_ix_1^3)\,H_i,\qquad
 E_-=\sum_i n_i\xi_i^2
    (x_1x_3^2-u_i^-x_2^3)\,H_i
\]
satisfy
\[
 \tag{2}
 \boxed{
 E_+=x_0^2x_2\,K-x_1^3H_A,\qquad
 E_-=x_1x_3^2\,L-x_2^3 K.}
\]
Here \(u_i^-=1/(\xi_i^2u_i)\) as in the original note.

**The opposite spectral form is not independent.** Directly,
\[
 \tag{3}
 \boxed{
 BL=-AH_B-M_1H,\qquad
 L=-\frac{AH_B+M_1H}{B}\in k[A,B]_{m-1}.
 }
\]
Polynomial divisibility by \(B\) holds because
\(H(A,0)=A^m\), \(H_B(A,0)=-M_1 A^{m-1}\).
Thus **\(H\) and \(K\) determine both \(E_+\) and \(E_-\)**:
the entire non-spectral paired information in the *first*
opposite cubic polars is a **single** degree-\((m-1)\)
form \(K\); the quadratic moment form \(L\) depends only
on \(H\).

Moreover
\[
 A^2H_A-B^2L
 =A(AH_A+BH_B)+M_1BH
 =H(mA+M_1B),
\]
where the middle step uses Euler's homogeneous identity
\(AH_A+BH_B=mH\).
Substituting (2) recovers the earlier comparison syzygy
\[
 \tag{4}
 x_2^2E_++x_0^2E_-+
 x_1H(mA+M_1B)=0.
\]
**Important correction to the earlier research emphasis:**
this syzygy is simply a consequence of Euler's identity
and the polynomial relation (3). It holds for *all*
paired configurations, without global CI realization;
by itself it is not a new independent compatibility
equation and it cannot force \(M_1=0\).

## 2. \(K/H\) is a partial-fraction interpolation function

On the affine chart \(B=1\), let \(T=A/B\).
Then
\[
 \tag{5}
 \boxed{
 \frac{K(T,1)}{H(T,1)}
 =\sum_i\frac{n_i/u_i}{T-\xi_i},
 \qquad
 \frac{\partial_T H(T,1)}{H(T,1)}
 =\sum_i\frac{n_i}{T-\xi_i}.}
\]
Both rational functions have **only simple poles**,
even when \(H\) has multiple roots.

Suppose the \(\xi_i\) attached to *distinct support curves*
are pairwise distinct (each may still have arbitrary
multiplicity \(n_i\)). Then
\[
 \tag{6}
 \boxed{
 \operatorname{Res}_{T=\xi_i}
       \frac{K(T,1)}{H(T,1)}\,dT
  =\frac{n_i}{u_i}\ne0.}
\]
Consequently \(H,K\) determine **every paired
toric point and multiplicity**:
\[
 \tag{7}
 u_i=\frac{n_i}
  {\operatorname{Res}_{T=\xi_i}(K/H)\,dT},
 \qquad v_i=u_i/\xi_i .
\]
This works with nonreduced multiplicities, in
characteristic zero; it is not restricted to
squarefree \(H\).

**Exact fixed-spectral parameter space.**
If \(H(T)=\prod_{i=1}^r(T-\xi_i)^{n_i}\)
with distinct nonzero \(\xi_i\), then a degree
\(<m\) polynomial \(K\) arises from exactly
one toric point at each \(\xi_i\) if and only if
\[
 \tag{8}
 \boxed{
 K \text{ is divisible by }
  H/\operatorname{rad}(H)
   =\prod_{i=1}^r(T-\xi_i)^{n_i-1},
 \quad \operatorname{Res}_{\xi_i}(K/H)\ne0
 \text{ for every }i.}
\]
Indeed the divisibility is equivalent to
the partial fractions having only simple
poles; the residues give \(u_i\), and
the proper rational function \(K/H\)
is uniquely determined by its simple
poles and residues. Thus for fixed \(H\)
the allowed \(K\)'s form
\((\mathbf G_m)^r\) inside a
**linear subspace** of the
\(m\)-dimensional coefficient space
of degree-\((m-1)\) polynomials.
This is the classical Hermite/Chinese-remainder
interpolation description of the **paired
two-torus Chow locus on the open where
the quadric parameter separates its support**.

**Collision boundary.**
If distinct translated curves share a
quadric parameter \(\xi\) but have
different \(u_i\)'s, then
\[
 \operatorname{Res}_{T=\xi}(K/H)\,dT
 =\sum_{\xi_i=\xi}n_i/u_i,
\]
and \(H\) remembers only
\(\sum_{\xi_i=\xi}n_i\).
The first polar **cannot distinguish**
the different \(u_i\)'s. Its residue
can even vanish. The higher
\(\mu^j\)-coefficients of the full
weighted Chow polarization retain the
elementary symmetric functions
of the \(1/u_i\)'s over a fixed
\(\xi\). Therefore (8) is **not**
a faithful classification on the
spectral-collision locus; the complete
paired Chow form remains necessary there.

### The non-invariant quartic exceptional component in \((H,K)\) coordinates

The already-classified characteristic-zero
\((4,4)\) exceptional realization has
\[
 \sigma=2[(u,v)]+2[(u,-v)],
 \qquad q=u/v\ne0.
\]
Its spectral roots \(q,-q\) are **distinct**,
even though both supports are doubled.
The interpolation package is
\[
 \tag{8a}
 \boxed{
 H=(A^2-q^2B^2)^2,\qquad
 K=\frac1u\,H_A
   =\frac{4A(A^2-q^2B^2)}u,\qquad
 M_1=2q+2(-q)=0.}
\]
Hence **the spectral-separating stratum
does include non-invariant nonreduced CI
realizations**. It cannot be discarded
as the already-solved reduced/invariant
locus. The simple relation \(K=cH_A\)
on a spectral-separating stratum is
equivalent to all its component
\(u_i\)'s being equal (\(c=1/u_i\)),
because residues of \(K/H\) are
\(n_i/u_i\), whereas those of
\(H_A/H\) are \(n_i\).
This recovers the exceptional
same-\(u\) geometry from one
polynomial identity without
choosing a carrier.

A first-moment theorem on the
spectrally separated nonreduced
incidence would therefore go
beyond the accepted
reduced/eigenform theorem;
it is still unknown in
unbounded degrees. The
quartic example checks the
interpolation formulas and
shows that the new parameter
reduction does not by itself
force invariant ideals.

## 3. Opposite chain membership is redundant for a full-support CI

Let \(h=x_0x_1x_2x_3\). In the
[lower-degree Chow-polarization argument](weighted_chow_quadric_cubic_polarizations.md#2-a-degree-2mldots3m-full-paired-chow-system),
the two coefficient ideals satisfy
\[
 \tag{9}
 (\mathfrak T_\sigma^+)_h
 =(\mathfrak T_\sigma^-)_h
 =\Bigl(\bigcap_iI_{C_i}^{n_i}\Bigr)_h .
\]

**Proposition (one-side suffices after nonzerodivisor saturation).**
Let \(J=(F_a,G_b)\) be a proper homogeneous
CI with no component in the coordinate
boundary \(V(h)\), equivalently \(h\)
is a nonzerodivisor on \(S/J\).
Then
\[
 \tag{10}
 \boxed{
 \mathfrak T_\sigma^+\subset J
 \iff \mathfrak T_\sigma^-\subset J.}
\]
Proof: take \(g\in\mathfrak T_\sigma^-\).
By (9), \(h^Ng\in\mathfrak T_\sigma^+\subset J\)
for some \(N\). Since \(h\) is regular modulo
\(J\), \(g\in J\). The reverse implication is
symmetric. A proper CI is unmixed, and for
the *full translated-cycle support* hypothesis
all its associated primes are the translated
curve primes, none of which contains any
coordinate variable, so the nonzerodivisor
hypothesis is **automatic**.

There is a simpler first-polar version:
from (4), if \(H,E_+\in J\) and \(x_0\)
is regular modulo \(J\), then \(E_-\in J\).
This proves **directly** that the
\(M_1\)-comparison syzygy and the
opposite first-polar membership are
*not independent conditions* on
the actual full translated-CI incidence.

**One-sided exact recognition with a boundary condition.**
For a proper degree-\((a,b)\) CI \(J\)
with \(ab=4m\) and \(h\) regular on
\(S/J\), the following are equivalent:
\[
 \tag{11}
 [V(J)]=\sigma
 \iff
 \mathfrak T_\sigma^+\subset J
 \quad\text{and}\quad
 \operatorname{Nm}_{\mathcal A_J/k[t^{\pm1}]}
 (X+uY+vZ)=\mathcal C_\sigma(X,Y,Z).
\]
The plus ideal's zero set is
\(\bigcup C_i\cup L_{01}\);
the regularity of \(h\) excludes
its residual coordinate line.
The norm then recovers the generic
multiplicity partition.
This sharpens the former
two-chain recognition formulation
but does **not** eliminate the
two actual surface equations,
their required properness,
or the moving nilpotent algebra.
It is not a new UM1 proof.

## 4. Revised research consequence

The earlier idea that the *two*
opposite polars create an additional
global cofactor **compatibility
gate** is too strong. Once one
full chain is in a CI ideal
supported off the coordinate
boundary, the other follows by
saturation; the special first-polar
syzygy is a version of Euler's
identity. The two chains remain
useful for **detecting and removing
boundary components** in an
unrestricted candidate ideal, but
provide **no independent
new restriction** on \(M_1\)
for an already-full translated CI.

On the spectral-separating stratum,
the genuinely smaller data is the
pair \(H,K\): the complete
two-dimensional toric arrangement
is encoded by a spectral divisor
and the residues of one rational
function \(K/H\). On spectral
collision strata, the higher
cubic polar coefficients encode
the missing fiberwise elementary
symmetric functions.

**The unsolved step is not a syzygy
identity between the opposite
polarizations.** It is to show that
a single weighted Chow-polarization
envelope admits **no proper
two-generator homogeneous CI
quotient with the prescribed
finite-flat norm** when the
spectral divisor has nonzero
centroid \(M_1=-H_B(1,0)\),
including the collision strata.
The accepted invariant/eigenform
and reduced-cycle theorems already
cover their stated cases; this
remaining non-invariant nonreduced
claim is still open.
