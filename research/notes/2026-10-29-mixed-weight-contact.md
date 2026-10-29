# Complete degree-six contact incidence for the mixed-weight sextics

October 29, 2026. Status: **independently reviewed provisional result**,
with the [independent audit](2026-10-29-mixed-weight-contact-audit.md) and
separate exact verifier. No canonical result or question is promoted.

## Exact family and bounded endpoint

Let k be an algebraically closed field of characteristic zero, let
C=[s^4:s^3t:st^3:t^4] in P3, and write

\[
q=x_0x_3-x_1x_2,\quad c_0=x_1^3-x_0^2x_2,\quad
c_2=x_2^3-x_1x_3^2.
\]

For **every** alpha,beta in k with alpha*beta nonzero, put

\[
F_{\alpha,\beta}=q^3+\alpha c_0^2+\beta c_2^2.
\tag{1}
\]

The completed incidence problem here keeps all 84 scalar coefficients
of an arbitrary actual homogeneous sextic G. It asks for a proper pair
(F,G) with generic transverse intersection length at least nine along C.
Nine is the necessary sole-support value 6*6/4. The answer is **empty**.
More precisely:

1. Every surface (1) is integral.
2. For every homogeneous sextic G with no common surface factor with F,
   the generic length along C is at most eight. Thus
   [V(F,G)]=m_C[C]+R has deg R=36-4m_C at least four whenever G contains C.
3. On either of the two formal transverse branches of F at generic C,
   a global sextic has vanishing order at least five **if and only if**
   it is a scalar multiple of F.

The numerical bound eight is an upper bound; attainment is not asserted.
This is a complete all-parameter, all-global-sextic calculation, rather
than a collection of selected carrier samples. It does not exclude
higher mate degrees, other mixed-weight carriers, or the boundary
alpha*beta=0, and it does not resolve unrestricted STCI.

## Torus normalization retains every nonzero parameter

Use the torus preserving C,

\[
\tau_\rho(x_0,x_1,x_2,x_3)
=(x_0,\rho x_1,\rho^3x_2,\rho^4x_3).
\]

The weights of q,c0,c2 are 4,3,9. Choose rho with
rho^12=-alpha/beta. Dividing F composed with tau_rho by beta*rho^18
therefore gives

\[
F_h=hq^3+c_2^2-c_0^2,\qquad
h=1/(\beta\rho^6)\ne0,\qquad h^2=-1/(\alpha\beta).
\tag{2}
\]

This is a projective automorphism and scalar rescaling. It preserves
properness, actual global coefficient spaces and generic contact.
Every nonzero alpha,beta is covered; no convenient parameter minor is
inverted. The computation uses the indeterminate `k` for h.

## Both split branches, including asymmetric contact

On x0=1 set x1=z, x2=z^3+v, and x3=z^4+q+zv. These are actual normal
coordinates over k(z). Here c0=-v, and

\[
c_2=(z^3+v)^3-z(z^4+q+zv)^2
=-2z^5q+z^6v+\text{terms of normal order at least two}.
\]

The quadratic initial form of (2) factors as

\[
(-2z^5q+(z^6-1)v)(-2z^5q+(z^6+1)v).
\tag{3}
\]

The factors are distinct over k(z), for every h, so these are two smooth
formal branches defined over k(z). This is a **split** node. Equality of
the two branch orders is not used. In particular, the earlier nonsplit
node argument for a different sextic family cannot be applied here.

Choose the branch with

\[
v_1=\frac{2z^5}{z^6+1}q.
\]

If v has been determined through degree n-1, the coefficient of the new
term v_n*q^n in F_h is -4z^5*v_n*q^(n+1). Consequently, for n=2,3,4,

\[
v_n=\frac{[q^{n+1}]F_h(q,v_{<n})}{4z^5}.
\tag{4}
\]

This constructs v modulo q^5 and makes F_h zero modulo q^6. The
coefficients are polynomial in h over
Q[z,z^-1,(z^6+1)^-1]. A global sextic with branch order at least five
has all its q^0 through q^4 coefficients zero as rational functions of z.
Their exact specialization on the two finite schemes below is therefore
a necessary condition, valid for every h and every extension of the
constant field.

The other branch is covered without assuming symmetry of G. Choose
sigma with sigma^6=-1. Then F_h composed with tau_sigma equals
-F_{-h}, and c2=+c0 and c2=-c0 are interchanged. The same all-nonzero-h
calculation therefore applies separately to each branch.

## Exact global coefficient calculation and all rank strata

The primary [Macaulay2 verifier](../computations/stci_mixed_contact_2026_10_29.m2)
and its [complete output](../computations/stci_mixed_contact_2026_10_29.txt)
work over Q[h], with no inversion of h during matrix construction.
For the first sample scheme z^18=1,

\[
(z^6+1)^{-1}=(z^{12}-z^6+1)/2,\qquad z^{-5}=z^{13}.
\]

The 18 points are distinct in characteristic zero, and none is a pole of
(4). Simultaneous reduction in Q[h,z,q]/(z^18-1,q^6) makes all calculations
exact. Evaluating all 84 degree-six monomials and retaining q-degrees
zero through four gives a 90 by 84 matrix M over Q[h]. Its columns are
actual global monomials; they are never allowed arbitrary k(z) source
coefficients.

The subgroup mu6 splits the matrix into six blocks. A monomial with
weight w=e1+3e2+4e3 has its q^j coefficient supported in z-exponents
congruent to w-4j modulo six. Therefore the blocks have 15 rows and,
respectively, 16,13,14,14,14,13 columns. For each block we compute the
presentation of the cokernel of its transpose over the PID Q[h].

| Weight mod 6 | Nonzero torsion invariant factors from z^18=1 | Free rank |
| --- | --- | --- |
| 0 | h, h, h^2 P7(h) | 1 |
| 1 | h, h, h | 0 |
| 2 | h, h, h^2 | 0 |
| 3 | h, h, h, h^2 | 0 |
| 4 | h, h, h^2 | 0 |
| 5 | h, h, h | 0 |

Here

\[
\begin{aligned}
P_7(h)={}&1215h^7+183834h^6+16985880h^5+1305652552h^4\\
&+56634503616h^3+1412125752640h^2\\
&+14480360156160h-16148528394240.
\end{aligned}
\]

The first finite test alone leaves the roots of P7 as exceptional
parameters. They are **not discarded**. Add a second sample scheme
z^18=8 in the weight-zero block. In this quotient,

\[
(z^6+1)^{-1}=(z^{12}-z^6+1)/9,\qquad z^{-5}=z^{13}/8.
\]

Its 18 points are also distinct and avoid every pole. The combined
30 by 16 weight-zero block has torsion invariant factors h,h,h^2 and
free rank one. Equivalently, the independent verifier computes a second
degree-seven exceptional factor Q7 and checks gcd(P7,Q7)=1 over Q[h].
Thus every nonzero h, including every root of P7, has total matrix rank
83. The displayed excluded value h=0 corresponds to the factored carrier
c2^2-c0^2; it lies outside (2).

The primary script additionally checks that the actual ambient vector
of F_h is annihilated and has a coefficient equal to one. Hence F_h
specializes to a nonzero kernel vector at **every** parameter. Rank 83
proves the kernel is exactly its scalar span. Its assertions check the
ranks and that all torsion away from h=0 vanishes, using the annihilator
of Ext^1 over Q[h]. These checks retain the full one-parameter rank
locus; they are not modular sample-rank extrapolations.

A rational-function branch identity must pass these finite necessary
tests. Since their kernel already equals the actual carrier span, the
same holds for the full global branch-contact incidence. Conversely,
F_h itself vanishes identically on the branch, so this identifies the
kernel exactly.

## Integrality and residual consequences

Suppose F_h had a proper homogeneous factor H vanishing identically on
the chosen formal branch. At least one factor would do so, since the
branch evaluation has integral target k(z)[[q]]. Its degree d is at most
five, and

\[
H\cdot H^0(\mathbf P^3,\mathcal O(6-d))
\]

would give at least four independent actual sextics in the branch-contact
kernel. Multiplication by H is injective in the polynomial ring. This
contradicts its proved dimension one. Thus F_h is integral; this argument
uses the completed global calculation and does not assume integrality
while computing it.

For any proper sextic G, the two finite branch orders n+ and n- are
therefore each at most four. The transverse local intersection length
is their sum, at most eight. A sole-support (6,6) complete intersection
would need length nine by Bezout. Therefore the required global-contact
incidence is empty, and every proper containing pair in this family has
a genuine residual curve of degree at least four. No exceptional vertical
cycle is counted as a residual curve.

## Evidence, review, and next interface

The [independent audit](2026-10-29-mixed-weight-contact-audit.md)
reconstructs the torus normalization, split branches, recurrence,
mu6 decomposition, both finite sample schemes and exceptional-factor
coprimality. Its independent
[verifier](../computations/stci_mixed_contact_audit_2026_10_29.m2) and
[output](../computations/stci_mixed_contact_audit_2026_10_29.txt) use the
same exact mathematical endpoint with separately assembled code.

The seed was proposed in
[the candidate-source note](2026-10-28-stci-search-candidates.md), not
previously certified as integral or excluded. Accepted low-degree and
freedom results are background motivation only; no inherited proof was
replayed to obtain this new family calculation. The exact new source
has been exhausted at mate degree six. For mate degree sixteen the
required total contact is 24; because the branches split, that further
test must retain asymmetric distributions or prove a branch-order bound.
The degree-six certificate does not supply that missing calculation.
