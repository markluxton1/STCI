# One-lift sextics: conormal zeros and Du Val corrections

**Theorem.** Work in characteristic zero with the fixed smooth quadratic
cover \(X=V(z^2-r)\), \(r=2x_1x_2-x_0x_3\), of the rational quartic
\(C=[s^4:s^3t:st^3:t^4]\). Let \(F=P^2-rQ^2\) be an integral sextic,
with \(\deg P=3\), \(\deg Q=2\) and \(Q|_C\ne0\). Orient its signed
cubic to contain \(D\) and not its conjugate \(D'\). If that signed cubic
has only smooth or Du Val points along \(D\), there is no mate of any
positive degree with sole reduced support \(C\). No hypothesis on
singularities away from \(D\) is required.

Write \(q=x_0x_3-x_1x_2\) for the unique quadric through \(C\),
as distinct from the norm coefficient \(Q\).

**Proof map.** The [one-lift conductor theorem](split_carrier_norm_and_conductor.md#split-carrier-the-conductor-is-an-actual-complete-intersection)
forces the binary-monomial restriction used below. The
[conormal transition and first correction estimates](#one-lift-sextics-the-conormal-zero-budget)
give derivative degrees \((8,6)\), the required correction \(14/3\), and
the \(A_n\) rank budget. [All Du Val types](#the-same-length-budget-controls-all-du-val-types)
fit the same strict bound \(114/25<14/3\) when the degree-six component
is nonzero. The [vanishing-component endpoint calculation](#the-identically-vanishing-degree-six-derivative-forces-a-non-du-val-hit)
forces a non-Du-Val point and finishes the theorem.

**Scope.** This proof treats the smooth/Du Val locus along the lift.
The [separate normalization proof](signed_cubic_normalization_and_cartier_defect.md)
excludes the unique generically singular signed cubic. The surviving
one-lift sector is generically regular along the lift and non-Du-Val
somewhere on it; if normal near the lift, it also satisfies the intrinsic
Cartier-defect restriction in that proof.
It is independent of the [two-lift theorem](two_lift_sextic_exclusion.md),
and “split” throughout means splitting in the fixed quadratic cover,
not splitting of the first normal cone.
The numerical pullback and isolated K3 smoothing argument used below are
proved in the [two-lift intersection account](two_lift_sextic_exclusion.md#transverse-residual-sextics-higher-a_n-do-not-suffice).

**Review provenance.** The relocated proofs retain the scopes assessed in the
[consolidated review of PR #167](https://github.com/markluxton1/STCI/pull/167#issuecomment-7043663699),
reviewed head `4d1b03cdf4671a7b1e987cb641a3509de23e9a5c`. The present
organization separates those existing arguments; it does not extend their
source hypotheses or claim a fresh rerun of historical computations.

## One-lift sextics: the conormal zero budget

Consider instead an integral one-lift split sextic in
characteristic zero. Orient the signed cubic \(S\subset X\)
so it contains \(D\), not \(D'\). The one-lift conductor
formula implies that for any actual mate the nonzero
restriction \(Q|_C\) is a binary monomial of degree eight.
Assume first that \(S\) is generically smooth along \(D\).
The normal derivative of the signed equation then has a
zero divisor on \(D\), supported at the actual singular
points along it. We describe the degree and multiplicity
budget of those zeros before applying numerical pullback.

In the first chart take \(t=x_1/x_0\),
\(u=z/x_0-t^2\), \(v=x_2/x_0-t^3\). The cover equation
gives \(x_3/x_0=t^4+2tv-2t^2u-u^2\). At the other
endpoint take \(T=x_2/x_3\), \(U=z/x_3-T^2\),
\(V=x_1/x_3-T^3\). Modulo the square of the ideal of \(D\),
\[
U=-t^{-4}u,\qquad V=t^{-6}v-4t^{-5}u,
\qquad V-4TU=t^{-6}v .
\]
Thus the conormal splits into degrees \(-4,-6\), with
the indicated generators. Twisting by the cubic degree
adds twelve on \(D\), giving derivative components of
degrees eight and six. If the degree-six component is
nonzero, the common zero divisor has length at most six,
including multiplicities.

If that component vanishes identically, the degree-eight
component has a constrained source. Write
\(Q|_C=s^{8-i}t^i\), up to nonzero scalar, with
\(0\le i\le8\), in binary coordinates. The signed restriction
fixes \(P|_C=-s^{10-i}t^{i+2}\) with the same scalar.
Choose monomial lifts for an initial signed cubic of
weight \(i+2\) under the torus preserving \(D\); the
weights of \(x_0,x_1,x_2,x_3,z\) are \(0,1,3,4,2\).
All variations at fixed restrictions are \(q\) times
the four downstairs coordinates, \(zq\), and the
three cubics
\[
x_0^2x_2-x_1^3,\qquad x_0x_2^2-x_1^2x_3,\qquad
x_1x_3^2-x_2^3 .
\]
Indeed the seven downstairs variations have distinct weights,
and restriction of cubic forms
downstairs achieves all thirteen binary weights, so
they span its kernel. Degree-two restriction downstairs
has only the kernel spanned by \(q\).
The coefficient of \(v\) for these variations is
\(t,t^2,t^4,t^5\) from the four \(q\) multiples,
\(t^3\) from \(zq\), and \(1,0,t^6\) from the
three cubics. This follows from \(q=tv-2t^2u\) to first
order; the middle cubic has \(u\)-coefficient \(2t^4\).
Thus one can cancel the degree-six component in its
initial weight, and the remaining freedom is only
the middle cubic. The degree-eight component is
of the form \(\alpha t^i+\beta t^4\) on this chart,
homogenized to degree eight. If nonzero, it has
at most five distinct zeros on the parameter line:
when \(i=0,8\) there are at most four torus roots
and one endpoint, and otherwise at most three torus
roots and two endpoints. A monomial has at most two
distinct zeros. This proves the bound of six distinct
singular points in all generically smooth cases,
without assuming that the zeros are simple.

If the singularities along \(D\) are Du Val, intersecting
a hypothetical mate with its inverse curve on the
normalization gives a precise correction demand.
The mate has cycle \(\lambda D\), with
\(\lambda=3b/2\) by hyperplane degree. Adjunction on a
resolution crepant along \(D\) gives
\(\widetilde D^2=-2\), by the canonical form of the
\((2,3)\) complete intersection. Thus numerical pullback
would need
\[
\sum_{p\in D\cap\operatorname{Sing}S}\operatorname{corr}_p
=2+\frac{4b}{\lambda}=\frac{14}{3}.
\]
The calculation is local along \(D\), so no normality
assumption is needed elsewhere. In particular if every
hit is \(A_1\) or \(A_2\), its correction is at most
\(2/3\); six such points give at most four. This rules
out every mate degree in the mild sector, even when
the degree-six component vanishes.

A stronger comparison uses the length rather than the
number of derivative zeros. Suppose all singular points
on \(D\) are \(A_n\) and the degree-six component is nonzero.
At a hit of type \(A_n\) write its local equation
as \(xy=z^{n+1}\). The strict smooth lift meets just one
exceptional component once, by the [smooth-curve incidence argument](two_lift_sextic_exclusion.md#nodal-signed-cubics-the-correction-is-insufficient). If this is vertex
\(j\), let \(r=\min(j,n+1-j)\). Along that component
the orders of \(x,y,z\) are \(j,n+1-j,1\), respectively,
from the toric resolution. Their restrictions to the
lift have at least those orders. The Jacobian ideal
\((x,y,z^n)\) thus vanishes along the lift to order at
least \(r\); this is a lower bound on the common conormal
zero order because differentiation along the lift itself
is zero. Its inverse Cartan correction is
\(r-r^2/(n+1)\). Consequently \(M=\sum r\le6\), and if
there are \(k\) hits then \(k\le M\). The K3 smoothing
bound on the marked \(A_n\) configurations gives
\(\sum n\le19\) without an assumption away from the lift.
Cauchy–Schwarz now bounds the total correction by
\[
M-\sum\frac{r^2}{n+1}\le
M-\frac{M^2}{19+k}\le\frac{114}{25}<\frac{14}{3};
\]
the second bound uses \(k\le M\le6\).
This rules out all \(A_n\) singularity sizes on this
conormal stratum, including multiple derivative zeros.

If the common derivative zeros are reduced, one can
apply the same estimate without assuming the local
types or a nonzero degree-six component. At a simple
zero the Hessian pairs the tangent of \(D\) with a
nonzero normal direction. A singularity with such
rank is a node or has the fixed rank-two splitting
\(xy+f(w)\); if \(f=0\) the lift cannot lie in the
singular curve, since it is generically smooth on
the original surface. The other formal sheet then
violates inverse support on the actual mate,
including at a marked endpoint: the one-lift signed
complete intersection has sole curve support \(D\).
Thus it must be \(A_n\), with the lift outside the
Hessian radical and meeting an end. The at most six
simple hits have \(M=k\le6\) and obey the same bound.

The preceding \(A_n\) and simple-zero lemmas alone do not settle
non-\(A_n\) corrections at multiple zeros or the identically vanishing
degree-six component. The next two lemmas settle both under the
smooth/Du Val hypothesis of the theorem. A signed cubic generically
singular along \(D\) is handled by the separate
[normalization argument](signed_cubic_normalization_and_cartier_defect.md#finite-normalization-and-full-inverse-support).

### The same length budget controls all Du Val types

For a one-lift sextic with nonzero degree-six derivative
component, the \(A_n\) length argument also covers
\(D\) and \(E\) singularities along \(D\). For any such
hit with Dynkin rank \(n\), let \(g\) be the common order
of vanishing of the two conormal components there.
There is a positive integer \(r\le g\) for which the
local self-correction is at most
\[
r-\frac{r^2}{n+1}.
\]
The \(A_n\) case is the preceding chain computation.
The local identification with a conormal defect is also supplied by
[Morrison, *The Birational Geometry of Surfaces with Rational Double Points*,
Theorem 3.1, p.424 and Table 2.2, p.421](https://web.math.ucsb.edu/~drm/papers/birgeoRDP.pdf).
Indeed, in the smooth ambient threefold choose local equations \(D=(x,y)\) and
\(F=a(t)x+b(t)y\bmod(x,y)^2\). Then
\[
 (I_{D/S}/I_{D/S}^2)\simeq k[[t]]^2/k[[t]](a,b),\qquad
 \ell\bigl((I_{D/S}/I_{D/S}^2)_{\rm tors}\bigr)
 =\min(\operatorname{ord}a,\operatorname{ord}b)=g.
\]
Thus the table's local defect is exactly the common derivative-zero
order used here, including multiplicity. The \(E_7\) value is three;
the argument below only needs the weaker lower bound two. This use is
local along the curve and invokes Theorem 3.1, not Theorem 3.2 with its
stronger ambient canonical-bundle hypothesis. The direct local estimates
below retain an explicit proof of the inequalities needed here.

For the other types, a smooth marked curve meets just
one exceptional component with fundamental-cycle
coefficient one: the intersection with that cycle
is the multiplicity of the downstairs curve. Use
[the resolution and admissible vertices of Brevik and Nollet, §§4.1.2–4.1.4](https://arxiv.org/pdf/1110.1867).
The relevant inverse Cartan diagonal is one at the
long tip of \(D_n\), \(n/4\) at either short tip,
\(4/3\) at either admissible \(E_6\) tip, and \(3/2\)
at the admissible \(E_7\) tip. There is no admissible
\(E_8\) vertex.

For \(D_4\) all tips have correction one. At \(D_4\),
at the long tip of any \(D_n\), and at \(E_6,E_7\),
one may take \(r=2\). Indeed a smooth arc on the
rank-one equation has its squared variable vanishing
to order at least two, and the other derivatives
have order at least two. The displayed corrections
are then below or equal to \(2-4/(n+1)\).

For a short tip of \(D_n\) with \(n\ge5\), use
\(x^2+y^2z+z^{n-1}=0\). A smooth arc has \(x\) of
order at least two and cannot have both \(y,z\) of
order one, by the cubic term. If \(y\) has order
one it goes to the long-tip node in the first
\(y\)-chart \(X^2+yZ+y^{n-3}Z^{n-1}=0\), with
\(x=yX,z=yZ\). Thus at a short tip \(z\) has order
one. The other two terms have opposite parity
of their orders, so neither can have order below
\(n-1\) and cancel the other. It follows that
\(\operatorname{ord}x\ge\lfloor n/2\rfloor\),
\(\operatorname{ord}(yz)\ge\lfloor n/2\rfloor\), and
the remaining derivative \(y^2+(n-1)z^{n-2}\)
vanishes to at least that order too. We can take
\(r=\lfloor n/2\rfloor\), for which
\(n/4\le r-r^2/(n+1)\).

Thus \(\sum r\le6\) by the degree-six derivative,
and the marked Du Val Milnor lattices, of total
rank at most 19 by the same embedded K3 smoothing,
give exactly the previous Cauchy bound \(114/25\).
It is below the required \(14/3\). This excludes
every mate when the degree-six derivative is nonzero
and the signed cubic is at worst Du Val along its
marked quartic, regardless of singularities elsewhere.
The [identically vanishing degree-six component](#the-identically-vanishing-degree-six-derivative-forces-a-non-du-val-hit)
requires the separate argument below.

### The identically vanishing degree-six derivative forces a non-Du-Val hit

The exceptional derivative stratum can also be eliminated
when the signed cubic is at worst Du Val along \(D\).
Write
\[
U_0=x_0z-x_1^2,\qquad M=x_0x_2^2-x_1^2x_3
\]
in the covering coordinate ring. After scaling the equation,
the signed cubic with vanishing degree-six component is
one of the following, plus \(kM\):
\[
\begin{array}{c|ccccc}
i&0&1&2&3&4\\ \hline
H_i&x_0U_0&x_1U_0&-zU_0&x_2U_0&x_3U_0 .
\end{array}
\]
Indeed each displayed form has first normal part only
in \(u\) on the first chart, and its coefficient of \(z\)
in the covering-ring decomposition restricts to the
prescribed weight-\(i\) monomial on \(C\). In the third
entry, use \(-zU_0=x_1^2z-x_0r\). The one-dimensional
kernel for fixed restrictions proved above gives
precisely the remaining \(kM\). Reversing the original
coordinates exchanges \(i\) and \(8-i\), preserves the
degree-six vanishing (by the diagonal conormal transition),
and so reduces to the displayed half.

For \(i<4\), use the last affine chart and write \(t,U,V\)
for its coordinates along and normal to \(D\). There
\(M=-V^2-2t^4U-t^2U^2\) exactly, and the quadratic
part of \(U_0\) is \(-V^2\). The quadratic part of
\(H_i+kM\) is therefore \(-kV^2\), and its cubic part
for \(i=0,1,2,3\) respectively is
\[
0,\quad -V^3,\quad UV^2,\quad -tV^2.
\]
If \(k=0\) the equation has multiplicity at least
three, so this singular point is not Du Val.
If \(k\ne0\), formally split the nondegenerate
square in \(V\). The remaining plane germ has
zero cubic part: the critical shift starts at
order two, and the cubic part on \(V=0\) vanishes.
This is incompatible with the rank-one Du Val
forms \(D,E\), whose plane cubic part is nonzero.

For \(i=4\), the first chart gives the exact equation
\[
k v^2+2tuv+(k-2)t^2u^2-u^3+(1+2k)t^4u .
\]
For \(k=0\) the first endpoint has multiplicity at
least three; for \(k=-1\) the last endpoint does,
as follows from the last-chart quadratic of both
\(M\) and \(U_0\). Otherwise complete the square
in \(v\) by setting \(v'=v+tu/k\). The equation is
weighted homogeneous of degree six for weights
\((1,2,3)\) on \((t,u,v')\). Its exceptional curve
on the corresponding weighted blowup is integral:
in the weight-one chart the quadratic in \(v'/t^3\)
has discriminant cubic in \(u/t^2\) with nonzero
cubic coefficient, so is irreducible, and there
is no component wholly in \(t=0\) on the weighted
projective plane. At a general point of this
exceptional curve the strict surface is smooth.
The canonical residue has a simple pole there:
the ambient volume gains \(t^5\) and the equation
contributes \(t^6\). The resulting discrepancy
\(-1\) is incompatible with a Du Val point,
which is canonical. Thus the identically vanishing
degree-six derivative cannot occur with only smooth
or Du Val points along \(D\).

Together the nonzero-component correction bound and
this endpoint test exclude **every one-lift split
sextic whose signed cubic has only smooth or Du
Val points along \(D\)**, in every mate degree in
characteristic zero. No assumption on singularities
away from \(D\) is required. Together with the
[generically singular exclusion](signed_cubic_normalization_and_cartier_defect.md),
this leaves a one-lift surface generically regular along \(D\), with
non-Du-Val behavior somewhere on it. In the normal-near-\(D\) sector,
the intrinsic defect condition is necessary, not a further exclusion.
