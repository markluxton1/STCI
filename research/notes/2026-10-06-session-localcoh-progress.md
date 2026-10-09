# A finite corner exclusion and the inverse-system defect boundary

Session started 2026-10-06; checkpoint completed 2026-10-07. Scope: the
characteristic-zero monomial rational quartic C0 and its two fixed
local-cohomology targets. This is an exact family exclusion and a structural
reduction. The full quartic incidence and the universal STCI question remain
open.

## 1. Three complete zero-at-origin corner families are excluded

Use the balanced normal-dual direction

\[
p=1+a_1t+a_2t^2,\qquad r=b_0+b_1t+b_2t^2
\]

and the order-four pure cubic symbol
\(c_i=t p^i r^{3-i}\), \(i=0,1,2,3\). Thus its top coefficient has
its single zero at t=0. This section treats the complete corner b0=0;
primitivity then guarantees p(0) nonzero, so its normalization to one loses
no candidate.

The three exact top-image annihilators from the audited 32-by-30 matrix,
after b0=0, give

\[
b_1=-6(a_1^2+a_2),\qquad a_2(a_2+a_1^2)=0.
\]

On a2=0 the remaining equation is

\[
(b_2-18a_1^3)(b_2+6a_1^3)=0;
\]

on a2=-a1^2 it is

\[
(b_2-2a_1^3)(b_2-10a_1^3)=0.
\]

If a1=0, the direction is not primitive as a homogeneous quadratic pair.
The a2=0, b2=-6a1^3 branch is also nonprimitive: both forms contain
1+a1*t. Every other branch is primitive. The actual ambient torus
automorphism of C0 transforms a normal-dual pair by

\[
(p(t),r(t))\longmapsto(l^4p(t/l),l^3r(t/l)).
\]

After dividing by l4 and choosing l=a1, every primitive direction in this
corner is one of exactly three normalized directions:

| Name | p | r |
| --- | --- | --- |
| corner18 | 1+t | -6t+18t² |
| corner2 | 1+t-t² | 2t² |
| corner10 | 1+t-t² | 10t² |

The coefficient h=t remains a nonzero scalar multiple of t, absorbed by
scaling the ancestor. Each target is a torus eigenvector, so existence of
the two multiplier equations is preserved by this normalization.

For each of the three symbols the fixed top map has a unique affine line of
lifts a=a*+lambda*k. The one-dimensional kernel k is the retained T3(-7)
section. Using the **actual** audited 74-by-18 quartic multiplication tensor,
the companion calculation finds a polynomial row n(lambda) satisfying

\[
n(\lambda)^T L(a^*+\lambda k)=0,\qquad n(\lambda)^T e_{72}=1.
\]

These identities exclude even the single target u for every lambda over
every characteristic-zero field extension. Hence all quartic common
ancestors with h=t and r(0)=0 are excluded. This assertion includes every
lower-order correction; it is not a sampled parameter computation.

Reproduce the saved identities using only Python's standard library:

    python3 research/computations/session-localcoh-corners.py

Regenerate the rational lifts and one-variable Macaulay2 module duals:

    /private/tmp/stci-cas-venv/bin/python research/computations/session-localcoh-corners.py --regenerate

The JSON certificate stores the three rational seeds, common kernel and
complete polynomial duals. The verifier checks the coordinate hashes,
target columns, all 18 polynomial identities, and each exact pure cubic
top. The generator and the three .m2 and dual-text files are retained. The
top-image branch classification is the displayed exact algebra, with no
numerical inference.

## 2. The socle pencil forces the top divisor to be an actual defect

The following derivation uses the already proved finite bound and generic
length theorem. The parent research agent independently audited the sheaf,
duality, endpoint normalization and Euler-characteristic arguments on
2026-10-07. This is a proved structural reduction under those antecedents.

Suppose a common quartic ancestor alpha survives. Its saturated annihilator
defines a pure Cohen--Macaulay quadruple Z supported on C0. Indeed its cyclic
module embeds in the finite inverse-system sheaf, which has no torsion at
closed curve points; at the generic point its length is exactly four and
its Hilbert function is (1,1,1,1). Write its saturated filtration pieces

\[
E_0=O_C,\quad E_1=L=O_C(e-7),\quad
E_2=L^2(D_2),\quad E_3=L^3(D_3),\qquad 0\le D_2\le D_3.
\]

The deepest piece E3 is the saturated socle. Multiplication by alpha gives
a faithful map

\[
O_Z\hookrightarrow\omega_Z(-3).
\]

Here local duality identifies the inverse-system sheaf supported on Z with
omegaZ(4), and alpha has ambient twist -7. Since I_C annihilates E3, the
restriction lands in

\[
\operatorname{Hom}_{O_Z}(O_C,\omega_Z)(-3)
\simeq\omega_C(-3)=O_{\mathbf P^1}(-14).
\]

The images of F and G in O_Z are in E3: they are socle elements generically,
and the lower filtration quotients are torsion free, so socle membership
propagates to every curve point. Their alpha-images are the fixed socle
sections u,v. The raw numerators xz and yw must not themselves be used as
a basepoint-free pencil: their curve restrictions have common endpoint
factors. On x=1, writing t=y, the first-normal determinant of (q,B) relative
to the balanced frame (U,V) is t³. The residues of xz=t³ and yw=t⁵ therefore
normalize to 1 and t². On the other affine chart these glue to the
homogeneous pencil (s²,t²) in H0(O_P1(2)), which has no common projective
zero. Thus, after twisting by O(4), the restriction of alpha to E3 is everywhere
surjective. It is a morphism of line bundles and hence an isomorphism:

\[
\boxed{E_3=O(-14),\qquad \deg D_3=7-3e.}
\]

The pure top coefficient h consequently has exactly divisor D3. A zero of h
cannot simply be discarded as an irrelevant degeneration. For e=2 this
gives deg D3=1 and leaves only

\[
(\deg D_2,\deg D_3)=(0,1)\quad\text{or}\quad(1,1).
\]

The first triple is primitive in the first case. In the second it has a
defective fiber at the one top-zero point. There is no implication that the
fourth structure is primitive in either case.

For completeness, chi(OZ)=4+6*deg L+deg D2+deg D3. Serre duality gives
chi(omegaZ(-3))=-chi(OZ)-48. The faithful alpha map has finite cokernel of
length

\[
2(\deg D_3-\deg D_2).
\]

Thus the (1,1) e=2 case makes alpha an isomorphism
OZ=omegaZ(-3): Z is Gorenstein and omegaZ=OZ(3). This numerical and
duality condition is necessary; it does not prove an ambient realization
or an STCI presentation.

## 3. Both e=2 local defect types are possible

Let D=k[[c]], R=D[[U,V]], and eij=U^(-i-1)V^(-j-1) in the transverse
inverse-monomial module. The counterexample

\[
\alpha=c e_{03}+e_{11}
\]

has exact annihilator

\[
\operatorname{Ann}(\alpha)=(U^2,V^2-cU).
\]

Its quotient is free of rank four over D with basis 1,V,U,UV. Generically
U=V²/c and the algebra is curvilinear. At c=0 it is the Gorenstein complete
intersection (U²,V²), with Hilbert function (1,2,1). Saturated powers have
E1 generated by V, E2 by U, E3 by UV. The relations V²=cU and V³=cUV give
D2=D3=(c=0). Nevertheless UV*alpha=e00, so the socle image is a unit at
the top-zero point. This proves the defective (1,1) case cannot be removed
by the relative Gorenstein argument or by the basepoint-free target pencil.

The other model

\[
\alpha=c e_{03}+e_{10},\qquad
\operatorname{Ann}(\alpha)=(U^2,UV,V^3-cU)
\]

has rank-four flat quotient with basis 1,V,V²,U. Here D2=0, D3=(c=0),
and U*alpha=e00. Its special abstract fiber has two-dimensional socle; the
cyclic inclusion into the inverse system does not remain injective on that
fiber. This is the retained generic-length countermodel. These local
examples distinguish the primitive triple from the defective triple and
preserve the failed shortcut against assuming every fiber is curvilinear.

## 4. Exact rational normalization when both endpoint coordinates are nonzero

The corner exclusions close h=t, r(0)=0. On h=t, p(0)*r(0) nonzero, the actual
torus and common direction scaling normalize p(0)=r(0)=1. The equations give

\[
b_1=-6(a_1^2+a_2)-2a_1-\tfrac32,
\]

\[
16a_2^2+(16a_1^2+12)a_2+12a_1^2+4a_1+3=0.
\]

The latter quadratic has discriminant
16(2a1+1)³(2a1-3). Its rational normalization is

\[
a_1=\frac{k^2+3}{2(1-k^2)},\quad
a_2=-\frac{k^2+2k+3}{2(k+1)^2},\quad
b_1=\frac{(k-3)(k^2+2k+3)}{(k-1)^2(k+1)}.
\]

Put qk=k²+2k+3. The final quadratic factors exactly into these two choices:

\[
\boxed{
b_2=-\frac{2(k^2-4k+5)q_k^2}{(k-1)^3(k+1)^3}
\quad\text{or}\quad
b_2=-\frac{2(k^2+1)(k^2-2k-1)q_k}{(k-1)^3(k+1)^3}.
}
\]

The homogeneous resultants are, respectively,

\[
\frac{8q_k^2(9k^4-21k^3+5k^2-31k+134)}{(k-1)^6(k+1)^6},
\]

\[
-\frac{8q_k(3k^4-2k^3-6k^2-18k-9)}{(k-1)^5(k+1)^6}.
\]

Primitivity retains exactly k≠1,-1 and the corresponding nonzero resultant.
The only point of the original finite chart omitted by finite k is
a1=a2=-1/2, b1=1,b2=-2. It is nonprimitive: its pair is
(1-t)(1+t/2),(1-t)(1+2t). Consequently these two rational families cover
**every primitive direction in the h=t endpoint chart with p(0)*r(0) nonzero**.

The exact companion `session-localcoh-origin-parametrize.py` checks all three
top-image identities, the quadratic discriminant, the final factorization,
both resultants and the omitted boundary. The two rational families are
stored in `session-localcoh-origin-families.json`. After retaining lambda,
the remaining endpoint incidence has only two parameters. A generic module
exporter `session-localcoh-origin-family-module.py` contracts the complete
actual tensor over QQ(k)[lambda]; any generic dual it finds still requires
an audit of every exceptional denominator/root locus.

## 5. The other endpoint boundary is retained completely

If p(0)=0, primitivity gives r(0) nonzero. Normalize r(0)=1 and write
p=a1*t+a2*t², r=1+b1*t+b2*t². The three top-image equations reduce exactly
to b1=8*a1²*a2 and

\[
4a_2(2a_1+1)
\left((2a_1+1)^2b_2+
2a_2^2(2a_1-1)(16a_1^4+8a_1^2+5)\right)=0.
\]

On a2=0, primitivity means a1*b2 nonzero. The torus normalizes b2=1,
giving (a1*t,1+t²). The actual ambient coordinate-reversing involution sends
normal-dual directions to (t²*r(1/t)/2,2*t²*p(1/t)), as follows from the
independently audited quartic symbol reversal formula. It also reverses the
linear top coefficient. Thus this direction with h=t becomes normalized
parity (1+t²,4*a1*t) with constant h. The existing exact parity certificate
excludes it, transporting the two target eigenclasses by their exchange.

On a2 nonzero, the torus normalizes a2=1 without changing a1. There are
exactly two remaining one-parameter families:

\[
p=k t+t^2,\qquad
r=1+8k^2t-
\frac{2(2k-1)(16k^4+8k^2+5)}{(2k+1)^2}t^2,
\qquad k\ne-\tfrac12,
\]

with resultant

\[
-\frac{(2k-1)(32k^6+32k^4+24k^3+26k^2+6k+1)}{(2k+1)^2},
\]

and the exceptional family

\[
p=-\tfrac12t+t^2,\qquad r=1+2t+b t^2,
\qquad \operatorname{Res}(p,r)=(b+8)/4\ne0.
\]

The exceptional family must be retained: the top equations vanish there for
every b. `session-localcoh-origin-boundary.py` verifies this split and its
resultants and saves the family JSON. Taken with Sections 1 and 4, this is a
complete direction classification for primitive e=2 top coefficient h=t:
the three finite corner families and the reversed parity family are
excluded; four one-parameter direction families remain for the actual
quartic multiplier incidence, each with the single lower coefficient lambda.

## 6. Computation status and continuation

For the **first** rational family of Section 4, a Macaulay2 calculation over
QQ(k)[lambda] returned a dual n with n^T L=0 and n^T u=1. The complete dual,
not merely its existence, is saved. Clearing its coefficient denominators
gives a polynomial dual, independently verified against all actual tensor
columns by `session-localcoh-origin-generic-dual.py` using Python's standard
library. This proves exclusion for **every lambda** outside a finite
exceptional k locus.

The cleared ancestor denominator is 120(k-1)^9(k+1)^9, and the dual's target
evaluation is the nonzero constant 89514547200 times

\[
(k-1)^{14}(k+1)^{11}(k^2-4k+5)^5(k^2+2k+3)^8
\]

times the four polynomials

\[
3k^4-9k^3-19k^2-43k-4,
\quad 9k^4-21k^3+5k^2-31k+134,
\quad 13k^4+26k^3+34k^2+6k-7,
\]

\[
729k^{13}+1620k^{12}+2889k^{11}-11268k^{10}-26574k^9
-39642k^8+94014k^7+272968k^6+454897k^5+62256k^4
-571463k^3-1210068k^2-966908k-379834.
\]

The factors k±1 are outside the chart. The factor k²+2k+3 and the middle
quartic are outside the primitive resultant-open locus. An independent
2026-10-07 audit has now **excluded the quadratic locus k²−4k+5=0 at both
roots for every lambda**, using the complete saved number-field dual and
a new standard-library verifier against all 18 actual tensor columns.
The two remaining quartics and degree-thirteen polynomial are finite
**unresolved exception loci** of this particular dual; no existence follows
from their vanishing. They are square-free, pairwise coprime and inside the
primitive chart, leaving 21 geometric direction parameters, each with its
full lambda fibre. See
[`2026-10-07-session-localcoh-independent-audit.md`](2026-10-07-session-localcoh-independent-audit.md)
for the complete coverage and denominator audit and
`verify_session_localcoh_q2_dual_2026_10_07.py` for the quadratic certificate.
The first family remains an exact open family exclusion rather than a
complete exclusion.

Run the independent identity verifier:

    python3 research/computations/session-localcoh-origin-generic-dual.py

The polynomial JSON, raw rational dual, rational seed, field-module exporter
and .m2 script are durable. They preserve all parameter denominators and
scope. The other three direction families of Sections 4 and 5 still need
the actual multiplier incidence.

The earlier five-variable quotient-module calculation was interrupted
after a bounded run before a kernel/evaluation result. Its script and chart
JSON remain inspectable; no exclusion follows from the unfinished run.
Top-zero points outside the endpoints need their own torus-normalized
chart. Neither the two rational-family parametrization nor the completed
corner certificate resolves these remaining incidence problems.
