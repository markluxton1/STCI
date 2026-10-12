# Independent audit: nonendpoint residual factors, finite maps and excess contacts

Date: 2026-10-12. Auditor:
`oct11_endpoint_a_nonzero_support/a_nonzero_three_common_roots`.

Status: **PASS, direct independent mathematical audit.** The deductions
listed below hold under the owner's actual model and admissible finite
birational projection hypotheses. No exclusion of the entire nonendpoint
family, no bound on descending powers and no higher-contact upper bound is
proved here. No new CAS execution is claimed for this audit.

The audited owner note is
[nonendpoint residual factor and genus reduction](2026-10-12-session-nonendpoint-residual-factor-and-genus-reduction.md),
SHA-256
`d0efa3d74b5b8b59f9f5790b7323404765793905e3553b4e84f5ef865597fc44`.
This version includes its section 4a, the eight one-parameter necessary
families. An earlier read preceded that addition; this audit binds the
completed version, which was reread before acceptance. Owner, canonical
and sealed files are unchanged by the auditor.

The input is the actual normal degree-five A4 pair, its complete
anticanonical coordinates and the five projection parameters
`delta != 0,a,b,g,d`. The restriction to c is the fixed C0 with
`z=(r-delta)/r`; its A4 point p maps to z=1. A mate necessarily requires
`(nu^{-1}(C0))_red=c`. This last condition is used as a necessary condition,
not as a sufficient descent criterion.

## 1. Factor hyperplanes and all component multiplicities

Write the residual equation as

\[
F=A t^2+(Jr+E)t+(-3\delta^2-A)r^3+P_2r^2+Lr+N.
\]

Its exact pole along ell is six: in the cancellation-aware normal form
using `v=t^2-r^3`, the unique weight-six term is `-3 delta^2 r^3`.
Thus the residual excludes ell. The low-pole spaces give all prime
degree partitions `6,2+4,3+3,2+2+2`, with repetitions retained.

When `A != 0,-3 delta^2`, the quadratic discriminant in t has degree
three and nonzero leading coefficient `4A(A+3 delta^2)`. Its valuation
at infinity is odd, so it cannot be a square in k(r). A is a nonzero
constant, hence F is primitive over k[r]. Consequently F is irreducible
in k[r,t]. Closing this prime in S gives the whole residual, reduced:
there is no extra boundary prime because the only boundary is ell and
ell was excluded.

On `A=0`, the equation is `(Jr+E)t+P(r)`, with P a genuine cubic whose
leading coefficient is `-3 delta^2`.

* If J is nonzero, the coefficients have a common factor precisely when
  `rho=-E/J` and `P(rho)=0`. In that event the factors are `r-rho` and
  a graph with a nonzero quadratic coefficient in r and constant nonzero
  t coefficient. Their pole degrees are exactly two and four.
* If J=0 and E is nonzero, the equation is a single graph, hence integral.
* If J=E=0, its three linear factors in r give `2+2+2`, including repeated
  roots. P cannot vanish identically.

On `A=-3 delta^2`, the discriminant has degree at most two. A polynomial
of that degree is a square in k(r) exactly when it is a square polynomial
over k: a rational square root of a polynomial has no finite poles and
is therefore a polynomial. The factors, when present, are linear in t
and at most linear in r; their exact pole degree is three. A zero
discriminant is the doubled cubic case. This exhausts the factor cases.

## 2. Cycle equality is valid on conductor components

The Cartier intersection cycle of X and Q is the same whether computed
by the quintic equation on smooth Q or by q on the hypersurface X.
Subtracting the pushed-forward c gives

\[
\nu_*D=R,\qquad [R]=(4,2).
\]

At any target prime, normalization gives a finite inclusion of
one-dimensional local rings `A0 -> B0`, with B0 possibly semilocal.
The cokernel M is finite length. Multiplication by the nonzero local
equation is injective on A0 and B0. The kernel and cokernel of its
multiplication on M have equal length, so the resulting exact sequence
gives equal lengths of `A0/qA0` and `B0/qB0`, taken over A0. The latter
already includes all residue-field degrees. Thus the cycle equality
retains both component multiplicities and map degrees and needs no
normality assumption along the target residual.

## 3. Low-degree source curves and maps of degree greater than one

These source compactifications can be checked directly, rather than
assuming normality from an affine graph.

For `r=rho`, the anticanonical coordinate functions span `1,t,t^2`.
The projective source curve is the complete smooth plane conic. Its
intersection support with c is precisely p and `T=0,r=rho`. Their
target parameters are 1 and `(rho-delta)/rho`, or infinity for rho=0;
they are distinct because delta is nonzero.

For `t+B1 r+C1=0`, the coordinate functions span `1,r,r^2,r^3`.
The source closure is a smooth rational normal cubic. Its intersection
support with c consists of p and the roots of
`-r^2+B1 r+C1`; at least one finite root exists. In particular the
normalization has exactly one branch at p. This rules out a hidden
extra source point above the A4 point in the fiber argument.

An integral conic can have map degree two only onto a ruling line.
Such a line would contain both distinct target points above, so it
would be the trisecant ruling through C0(1). That ruling meets C0 at
the three distinct cube roots of unity. Surjectivity requires a source
point above each, whereas full support permits only the two source
points on this conic. Contradiction.

A cubic can have map degree three only onto a ruling line. The ruling
with a single C0 point cannot contain the image of its finite source
intersection with c. For the trisecant ruling, full support and the
isomorphism c -> C0 make all three fibers singleton fibers on the
smooth source cubic. A separable degree-three map P1 -> P1 would
then have three ramification contributions of two. Riemann-Hurwitz
allows total ramification four, not six. Contradiction.

It follows that conics and cubics map birationally to integral
Q-curves of classes `(1,1)` and `(2,1)` or `(1,2)`, respectively.
Each such image has arithmetic genus zero and is therefore smooth.
Repeated components change only the cycle coefficient, not this
argument about the underlying prime map.

Consequently `2+2+2` always pushes forward to class `(3,3)` and is
excluded. In `3+3`, both cubics must have class `(2,1)`, including
a doubled cubic. In `2+4`, the quartic pushforward must have class
`(3,1)`. Its graph has a nonzero quadratic coefficient in r, so its
intrinsic coordinate functions span `1,r,r^2,r^3,r^4`. Projecting this
five-dimensional span through a two-dimensional vector kernel leaves
dimension at least three, so its image is not a line. A double map
to a conic would contribute class `(2,2)`, also impossible. Thus it
maps birationally to the smooth rational curve of class `(3,1)`.

## 4. The five conic locations and eight necessary parameter families

The conic is exactly the plane section of Q by its containing plane.
Consequently its scheme intersection with C0 equals the plane section
of C0, a nonzero binary quartic. Both source intersection points must
occur in its support. For finite `zrho != 1`, it has the form
`(z-1)^m(z-zrho)^(4-m)`, with m=1,2,3. The missing z^2 coefficient
gives, respectively,

\[
3z_\rho(z_\rho+1)=0,\quad
z_\rho^2+4z_\rho+1=0,\quad
3(z_\rho+1)=0.
\]

For zrho=infinity, only m=1 survives. Translating by
`zrho=1-delta/rho` gives exactly the five owner values of rho/delta.
No multiplicity-zero endpoint can be added because both conic points
belong to c and their images are distinct.

For section 4a, set `u=a-b,w=a-g`, so A=0 gives
`d=a-u-w,B=-uw`. Direct substitution yields

\[
J=(3u+w)\delta-3\delta^3,\qquad E=-uw+\delta^4.
\]

Thus `J rho+E=0`, with `rho=tau delta`, is exactly owner equation
(8b). Substitution into `P(tau delta)/delta^4`, followed by (8b), gives
exactly (8c); only the known nonzero delta is divided out.

The conic parametrization's T coefficient is

\[
(a,b,g,d)-(2\rho^2+\rho)(1,1,1,1)
       +\delta\rho(0,1,3,4).
\]

The plane polynomial H has H(1)=0. Its vanishing on this coefficient
is therefore precisely `(8a)`, including the term
`delta rho H'(1)`. The constant and quadratic coefficients already
vanish by the two plane-section points and H(1)=0.

The reductions in the owner note follow without dropping lift strata:

* tau=0 gives u=0 and a=0, then E=delta^4, impossible.
* tau=1 gives u=delta^2, then `J delta+E=delta^4`, impossible.
* tau=1/2 with contact pattern (1,3) gives
  `3w=u+4delta^2`, then `u=x delta^2` with
  `2x^2-2x-1=0`, and
  `a=(u+w+delta-delta^2)/2`.
* tau=1/2 with contact pattern (3,1) gives w=3u,
  `6x^2-6x+1=0`, and the same a formula.
* For `6tau^2-6tau+1=0`, the double-double contact gives w=3u,
  `3x^2-6tau x-1+3tau=0`, and
  `a=(6tau-1)u+tau delta-(3tau-2/3)delta^2`.

The last quadratic discriminant is six; the first two are twelve.
All are nonzero in characteristic zero. Hence there are exactly the
eight listed necessary branches, each retaining arbitrary nonzero delta.
The required J is automatically nonzero on each branch. In the first
branch it is `delta^3(10x-5)/3`; in the other branches it is
`delta^3(6x-3)`. The value x=1/2 satisfies none of their quadratics.
These calculations do not prove center avoidance or successful full
support of the quartic, let alone conductor descent.

## 5. The actual integral residual is an arithmetic-genus-one curve

Off the two hyperplanes, `y=2At+Jr+E` realizes the affine residual
as `y^2=Delta(r)` with a genuine cubic right side. Its projective
plane cubic is integral and has one smooth point at infinity. A
repeated finite root of Delta gives a singular affine curve, still
of arithmetic genus one; its geometric genus may be zero.

At infinity, r and t have pole orders two and three. The leading
relation is `t^2/r^3 -> kappa=(A+3delta^2)/A`, with both kappa and
kappa-1 nonzero, so v has pole six. The anticanonical functions
`v,rt,t,r^2,r,1` extend in the frame O(6p_infinity), with v nonzero
there and no base point. They have pole orders 6,5,3,4,2,0.
The morphism is the original affine embedding and hence finite
birational onto the actual residual closure.

In the Z0=1 chart, `a0=rt/v,b0=t/v,c0=r^2/v` have orders 1,3,2.
The first is a uniformizer. The finite map's completed image ring
therefore contains the full source DVR k[[a0]], proving it is an
isomorphism near infinity; it is already an isomorphism on the whole
affine chart. Thus the actual reduced curve D is this plane cubic,
not its normalization, and `pa(D)=1`. It is smooth at the A4 point p.

## 6. A double map is excluded at p for every allowed lift parameter

Cycle equality permits only generic map degrees one or two. In the
degree-two case the image has class `(2,1)`, hence is smooth.

The owner's tangent argument can be checked in the actual coordinates
without a generic derivative assumption. Near p,

\[
U_4=1-a_0,\quad U_3=-a_0,\quad h=b_0+c_0.
\]

Since b0,c0 have orders at least two on D, the actual projection sections
satisfy

\[
X_0=1-a_0+O(a_0^2),\quad
X_1=1+(\delta-1)a_0+O(a_0^2),\quad
X_1/X_0=1+\delta a_0+O(a_0^2).
\]

The derivative is the known nonzero delta, independently of a,b,g,d.
Thus the map to its smooth image is unramified at p. Finite torsion-free
modules over the image DVR are free of generic rank two, so the fiber
has total length two. Its local contribution at the smooth source p
is one, forcing another source point over C0(1). Full support and the
isomorphism c -> C0 allow only p. This excludes degree two.

Therefore D maps finite birationally to the integral R of class `(4,2)`.
It has `pa(R)=3`, so the actual curve-model quotient
`nu_*O_D/O_R` has length `3-1=2`. That quotient length is not a contact
bound and is not used as one.

## 7. The eight-excess condition is a scheme-length equality

The exact intrinsic ideal of c at p, in the A4 surface chart, is

\[
(b_0+c_0,\ (1-a_0)c_0-a_0^2).
\]

Indeed setting b0=-c0 in the surface equation
`b0(c0-a0^2)+a0 c0^2=0` gives the union of ell and c, and the second
generator selects c scheme-theoretically. On D,

\[
c_0/a_0^2=v/t^2\longrightarrow
\frac{3\delta^2}{A+3\delta^2},\qquad b_0/a_0^2\longrightarrow0.
\]

The first limit is nonzero and different from one. Both ideal
generators consequently have exact order two, and the restricted
ideal is `(a0^2)`, of colength two.

On the affine chart, S is smooth and the ideal of c is `(T)`.
The quotient of D by T is `k[r]/F(r,-r^2)`. Its polynomial has degree
exactly four because its leading coefficient is A, so its total length
is four, including all repeated roots and singular affine points.
Thus the intrinsic restricted ideal is locally principal everywhere
on D, generated by a nonzerodivisor, and defines a Cartier zero scheme
of total length six.

The Cartier equation of C0 on smooth Q pulls back to a nonzerodivisor
phi on D of total zero length `C0.R=14`. The same kernel-cokernel
calculation as section 2 verifies the length under the birational curve
map; equivalently this is the degree of the pulled-back Cartier divisor.
Full support puts all those zeros on c. Scheme-theoretic vanishing on
c ensures `phi` lies in the restricted intrinsic ideal. Locally
`phi=tau*w`, with tau its nonzerodivisor generator and w regular.

For any one-dimensional integral local ring, multiplication gives
an exact sequence

\[
0\to O_D/(\tau)\xrightarrow{\ \cdot w\ }
O_D/(\tau w)\to O_D/(w)\to0.
\]

This uses nonzerodivisors, not smoothness. It remains valid at every
singular affine branch. Summing its lengths proves exactly

\[
\sum_{x\in D\cap c}\operatorname{length}(O_{D,x}/(w_x))=14-6=8.
\]

The lengths are nonnegative. No claim restricts their size via the
number of first-normal roots, the geometric genus, or the length-two
curve-model quotient. The factor hyperplanes are outside this equality.

## 8. Verdict, repairs and input bindings

All audited deductions pass. No mathematical repair of the owner note
is required. This audit makes explicit three supporting points that
were compressed there: the smooth compactifications of the low-degree
source primes, the nonzero actual derivative delta at p, and the
nonzerodivisor exact sequence at singular affine points. It also verifies
the subsequently added section 4a and its eight necessary branches.

The completed results are the two factor hyperplanes, exclusion of
`2+2+2`, the map-degree restrictions in `2+4` and `3+3`, the eight
necessary conic-plus-quartic parameter families, and the exact
eight-excess requirement for integral D off the two hyperplanes.
The integral genus-one residual cases, the eight quartic-contact cases,
the cubic-pair conductor cases and unbounded full descent remain open.

Additional read input versions:

* [nonendpoint pole filtration and line jet](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md),
  SHA-256 `ad4459de5a95b12e26a162419082d7b32745323a6781716efdf6cca72767c2a2`.
* [exact low-pole spaces](2026-10-11-session-a4-low-pole-spaces.md),
  SHA-256 `929f8165fd0f484175c819011cdf2eefaf6766e3c88735d556903241a2177f5a`.
* [explicit A4 model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md),
  SHA-256 `f19ae25848ba77a5c59f3a9ce53819b24258c03b5d90f234b31ec7581306f8bd`.
* [intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md),
  SHA-256 `537e341fb79632997648209efb7728c64229d7bd648cc2721285e8ab04cf0e0f`.

The source `verify_session_nonendpoint_target_fibers_2026_10_12.m2` was also
read as context; its separate execution is neither repeated nor counted
as a new certificate by this written proof audit.
