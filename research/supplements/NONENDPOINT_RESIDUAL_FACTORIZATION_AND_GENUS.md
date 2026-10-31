# Nonendpoint residual divisors, pole filtration and actual fiber norms

Fix the embedded curve \(C_0=[s^4:s^3t:st^3:t^4]\), an algebraically closed characteristic-zero field, and the accepted anticanonical degree-five A4 pair \((S,c)\). Retain arbitrary \(\delta\ne0\), the four lift parameters \(a,b,g,d\), and an actual line center disjoint from \(S\), giving a finite birational projection \(\nu:S\to X\) onto an integral quintic. The restriction \(c\to C_0\) is an isomorphism. A hypothetical mate forces **full** reduced inverse support \((\nu^{-1}C_0)_{red}=c\), denoted SUP; it excludes isolated extra inverse points as well as extra curves. The proofs below concern this exact family, not every quintic carrier. The intrinsic pair is proved in [the A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md); actual projection coordinates and every target boundary are in [the target-fiber chapter](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md).

## Exact residual equation and parameters

Put `t=T-r^2`, `v=t^2-r^3`, and define coefficients

    A=a+d-b-g, B=ad-bg,
    J=(4a-3b-g)delta-3delta^3-A,
    E=B+delta^4,
    P2=B+(6a-3b)delta^2+3delta^3,
    L=(-4a+b)delta^3-delta^4, N=a delta^4.

The residual D is the actual Weil divisor `div(F)+6ell`, where

    F=A t^2+(J r+E)t+(-3delta^2-A)r^3+P2 r^2+L r+N.          (1)

It excludes ell. Its only possible prime-degree partitions, including
multiplicities, are 6,2+4,3+3,2+2+2.


<a id="1-nonendpoint-residual-factor-and-genus-reduction"></a>
<a id="2-nonendpoint-residual-factor-and-genus-independent-audit"></a>

## Factorization, finite curve maps and eight excess contacts

### 1. Factor hyperplanes and all component multiplicities

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

### 2. Cycle equality is valid on conductor components

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

### 3. Low-degree source curves and maps of degree greater than one

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

### 4. The five conic locations and eight necessary parameter families

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

### 5. The actual integral residual is an arithmetic-genus-one curve

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

### 6. A double map is excluded at p for every allowed lift parameter

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

### 7. The eight-excess condition is a scheme-length equality

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


<a id="3-nonendpoint-pole-filtration-and-line-jet-independent-audit"></a>

## Complete pole filtration and entire-line power obstruction

### 1. Accepted inputs, parameters and admissibility

Work over an algebraically closed field `k` of characteristic zero. The
accepted intrinsic genus-one pair consists of the normal degree-five
anticanonical del Pezzo surface `S`, its smooth lifted quartic `c`, and its
unique line `ell`. Its only singular point is A4, on ell. The accepted
[pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#1-dp5-a4-intrinsic-pair-classification)
and [coordinate audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#2-dp5-a4-explicit-model-independent-audit)
give the actual divisor identities

    div(U0)=5ell, div(h)=c+ell, H~5ell, c~4ell,
    Q=h^5/U0 in H0(S,4H), div(Q)=5c.

They also give the complete affine complement `S\ell=A2`, with coordinates
`r,t`, and

    T=t+r^2, v=t^2-r^3,
    U0=1, U1=r, U2=r^2, U3=-rt, U4=v-rt, h=T

in the `U0` frame. These are actual coordinates, not a tangent approximation.
The unique residual pair automorphism acts by translation in `r`. Thus two
finite center roots can be translated to `0,delta`, with `delta!=0`; their
difference is a retained parameter. It is twice the signed half-separation
in the midpoint convention, and there is no scaling normalization to one.

For arbitrary constants `a,b,g,d`, the four sections in the owner note
restrict to

    r^4, r^3(r-delta), r(r-delta)^3, (r-delta)^4

on c. They are linearly independent for every `delta!=0` and give the fixed
curve C0 with parameter `z=(r-delta)/r`. The A4 point `r=infinity` maps to
the nonendpoint `z=1`.

The section calculation below holds before imposing center avoidance. Its
interpretation as a normalization projection requires the line center to
avoid `S`. This condition makes the four sections basepoint free and gives
a morphism with pullback polarization `H`. The morphism is finite: a
positive-dimensional projective fiber would contain a curve on which the
ample H has degree zero. Its image spans P3, because the four sections are
independent. Since `H^2=5`, the product of its generic degree and the image
degree is five. The nondegenerate surface image cannot be a plane, so the
generic degree is one and the image is an integral quintic. Normality of S
then identifies this finite birational map with the normalization.

The all-power conclusion also uses the accepted
[quintic structural frontier](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit):
any hypothetical mate has degree `4k` and pulls back to a nonzero scalar
multiple of `Q^k`. That input is not inferred from the pole calculation.

### 2. The pole filtration is exhaustive, including cancellation strata

On the genuine fourth blowup chart write `B=1+xu`. The accepted section
vector after the common base factor is removed is

    (Z0,Z1,Z2,Z3,Z4,Z5)
      =(u,B,x^2 B^2,xB,x^3 B^2,x^5 B^3).

At the generic point of ell, `x=0` is a uniformizer and `u` is the
transcendental coordinate in the residue field `k(u)`. The resolution is
an isomorphism over this smooth generic point. In particular

    r=Z4/Z5=x^(-2) B^(-1),
    t=Z2/Z5=x^(-3) B^(-1),
    v=Z0/Z5=u x^(-5) B^(-3).

The last expression also follows directly from
`t^2-r^3=x^(-6)B^(-3)(B-1)`. Thus the exact pole orders are `2,3,5`.

The polynomial presentation

    k[r,t]=k[r,v,t]/(t^2-r^3-v)

is free with basis `1,t` over `k[r,v]`, since the relation is monic in t.
Consequently every polynomial has a unique normal form as a finite linear
combination of `r^i t^j v^m`, with `i,m>=0` and `j=0,1`. Such a monomial
has exact pole weight `2i+3j+5m` and leading coefficient `u^m`.

At a fixed maximal weight, there is at most one monomial for each m:
`2i+3j=weight-5m` determines j by parity and then determines i. Its leading
coefficients therefore form distinct powers of u. A nonzero linear
combination cannot cancel all of them in `k(u)`. This treats the actual
cancellation in `t^2-r^3`; assigning independent weights to r and T would
not give an exhaustive argument.

For every `n>=0`, the resulting global section space is exactly

    H0(S,O_S(nell))
      =span_k{r^i t^j v^m : j=0,1 and 2i+3j+5m<=n}.

Indeed any divisorial section has no codimension-one pole on `S\ell=A2`
and is therefore a polynomial there. Conversely a polynomial satisfying
the ell bound has no negative divisor coefficient anywhere else. On the
normal S these are precisely the conditions for the reflexive Weil-divisor
sheaf. There is no additional codimension-two condition at A4. In particular

    H0(S,O_S(6ell))=span{1,r,t,r^2,rt,v,r^3}.

This also independently confirms the written
[low-pole-spaces proof](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#5-a4-low-pole-spaces). Neither
6ell nor its sheaf is being asserted to be Cartier.

### 3. The residual divisor is actual and has exactly the stated partitions

For a direct reconstruction set

    p=v-rt, A=a+d-b-g, Bpar=ad-bg,
    L1=delta rt,
    L2=3delta rt+3delta^2 r^2-delta^3 r,
    L3=4delta rt+6delta^2 r^2-4delta^3 r+delta^4.

Then `X0=p+aT`, `X1=p+L1+bT`, `X2=p+L2+gT`,
`X3=p+L3+dT`, and direct multiplication gives

    q=p(L3-L1-L2)-L1 L2
      +T*(A p+aL3-bL2-gL1)+Bpar*T^2.

The first two terms are exactly

    T*(-3delta^2 r^3-3delta^3 rt+3delta^3 r^2
        +delta^4 t-delta^4 r).

This reconstructs the owner's full formula `q/U0^2=T F` without appealing
to the previous checker. Here

    F=A v-3delta^2 r^3
      +((4a-3b-g)delta-3delta^3-A)rt
      +(Bpar+(6a-3b)delta^2+3delta^3)r^2
      +(Bpar+delta^4)t
      +((-4a+b)delta^3-delta^4)r+a delta^4.

Its only normal-form weight-six monomial is `-3delta^2 r^3`. It has exact
pole order six, including the parameter strata where the coefficient of
`r^3` after expanding v into `t^2-r^3` happens to vanish.

The rational function `T=h/U0` has divisor `c-4ell`. Since the actual
Cartier section q of `2H` is represented by `TF` in the U0 frame,

    div(q)=div(T)+div(F)+2div(U0)=c+D,
    D=div(F)+6ell.

This D is an effective Weil divisor of degree six. Its ell coefficient is
zero, because the F pole has exact order six. The raw fourth-chart section
restriction also gives

    q|_(x=0)=(u-1)(u-1+4delta)
             -(u-1+delta)(u-1+3delta)=-3delta^2.

This is nonzero in the affine fourth-chart frame and at the generic point
of ell. It proves that ell is not a component, not that q has no point
intersection with ell at the omitted A4 point. No point-disjointness is
used in the argument.

For completeness, the localization sequence and `Cl(A2)=0` show that
`Cl(S)` is generated by ell. There is no relation: intersecting a
principal multiple `m ell` with the ample Cartier H gives `m=0`, because
`H.ell=1`. Hence `Cl(S)=Z[ell]`, and the class of any prime has coefficient
equal to its positive integral H-degree. The pole-filtration space for
`O_S(ell)` consists only of constants, so ell is the sole degree-one prime.
All prime components of D thus have degree at least two, and a total of
six permits exactly

    6; 4+2; 3+3; 2+2+2.

These are numerical partitions with multiplicities, not realization or
genus statements. D may contain c as the degree-four member; no assumption
that D is reduced or disjoint from c is required or established.

### 4. The rank-one equations exhaust entire-line ramification

In the same fourth chart, the four section values on ell are

    s=(u-1,u-1+delta,u-1+3delta,u-1+4delta),

their u derivatives are `(1,1,1,1)`, and their x derivatives are

    e=(a-u, b-u+delta u,
       g-u+3delta u+3delta^2,
       d-u+4delta u+6delta^2).

Set

    R2=g+3delta^2+2a-3b,
    R3=d+6delta^2+3a-4b.

Subtracting the first column from the others in the matrix with rows
`s,(1,1,1,1),e` gives its four ordered three-column determinants as

    -delta R2, -delta R3,
    delta(4R2-3R3), delta(3R2-2R3).

Thus their ideal is exactly `(delta R2,delta R3)`. The first two rows
are independent because `delta!=0`, so the projective differential has
rank at least one. Its rank at the generic point of ell is one exactly
when `R2=R3=0`; it otherwise has rank two. This is an exhaustion for
the stated entire-line rank condition, not for isolated ramification.

### 5. Frame-correct derivation and the obstruction to every positive power

Assume `R2=R3=0` and put `lambda=(b-a)/delta`. Define the polynomial

    C(u)=u^2+lambda u-lambda-a.

The needed derivation is the k-derivation from the local ring at the generic
point of ell into its residue field given by

    D(f)=[partial_x f+C(u) partial_u f]_(x=0).

It is transverse: `D(x)=1`. It is therefore not a derivation of the
residue field itself, and need not kill the target functions away from ell.
In the patch `X0!=0`, which contains the generic point since
`X0|ell=u-1`, direct quotient differentiation gives

    D(X1/X0)=0,
    D(X2/X0)=R2/(u-1),
    D(X3/X0)=R3/(u-1).

Hence all three values vanish on the retained rank-one locus. Chain and
quotient rules make D vanish on any downstairs local function pulled
back to this point. For the mate argument it already suffices that it
vanish on every polynomial in the three affine ratios.

The raw actual section Q in the fourth-chart H-frame is

    Qraw=(1+xu)^2(1+x+x^2u)^5.

It is a unit at generic ell, with value one and x derivative `2u+5`.
The normalized function

    q0=Qraw/X0raw^4

is invariant under changing the local H-frame. Its value is `(u-1)^(-4)`.
Also

    D(X0raw)/X0raw=(a-u+C(u))/(u-1)=u+lambda.

The quotient rule therefore yields

    D(q0)/q0=5-2u-4lambda,
    D(q0^k)=k*q0^k|ell*(5-2u-4lambda), for every k>=1.

The last value is nonzero in `k(u)`, since k has characteristic zero,
u is transcendental, and its linear coefficient is `-2k`. No analytic
logarithm, conductor flatness or reduced-branch assumption is involved.

If an ambient mate of degree `4k` existed, the accepted normalization
divisor argument would make its pulled section a nonzero scalar times
`Q^k`. Dividing by the actual pulled target frame `X0^(4k)` would express
that scalar times `q0^k` as a polynomial in the target affine ratios.
Its D value would then vanish, contradicting the preceding formula.
This proves the claimed exclusion for every positive k on this precise
admissible ramified-line subfamily.


<a id="4-nonendpoint-diagonal-norm-identity"></a>

## Diagonal conormal identities and the degree-eight norm

We work over an algebraically closed field of characteristic zero, with
`delta!=0`. The five actual parameters are `delta,a,B,G,J`, where

    B=b-a, G=g-3b+2a, J=d-2g+2b-a.

Here `J` is the parameter denoted `Jbar` in the conormal note; it is not
the conormal cubic. The actual source, projection-center avoidance and
finite-target equations are those of the
[target-fiber reduction](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions).
The corrected cubics and their two-chart interpretation come from the
[conormal reduction](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#1-nonendpoint-conormal-cubic-reduction).
All common-root interpretations below require the stated actual center
avoidance. Literal polynomial identities do not require that open condition.

### 1. Compact diagonal evaluations

Write

    Z=Gp(2-p)+J(3-p),
    A=(3delta^2+G)p(2-p)+J(3-p),
    b2=delta[delta^2p(p-3)+3Bp(2-p)+G(2-p)-J],
    c2=delta^2[Bp(p-3)-G],
    A2=Ar^2+b2 r+c2,
    N=delta^2(pr-delta)[3(2-p)r-delta(3-p)],
    M=delta^2[3Jr^2+delta(2G-J)r-delta^2G],
    Psi=p^2Z^2r^4+p^2Z(2r^2+r-a)N+p^2N^2-MZ
        =(pr-delta)C3.

These are literal polynomials; in particular `C3` is the exact polynomial
quotient, not a saturation or a discarded geometric component. Its
coefficient of `r^3` is `pA^2`.

For `p!=0`, set `r0=delta/p` and `Pc=p^2-6p+6`. Define

    V=(3-2p)J+p(4-3p)G+p(delta^2+Bp)Pc,
    W=3J(2-p)+2Gp(3-2p)+p(2delta^2+delta p-ap^2)Pc.

The exact diagonal identities are

    p^2 A2(r0,p)=delta^2 V,
    p^2 C3(r0,p)=delta^3 ZW.                         (1)

For the cubic identity, differentiate `Psi=(pr-delta)C3` in `r`, with
`p` fixed. On the diagonal,

    N(r0)=0,
    N_r(r0)=delta^3 Pc,
    M_r(r0)=delta^3[(6/p-1)J+2G],
    C3(r0)=Psi_r(r0)/p.

Substituting these three expressions gives (1). Differentiating once
more gives `C3_r(r0)=Psi_rr(r0)/(2p)`; this is a product-rule identity,
with no assertion about actual conductor length or a higher-contact bound.

### 2. Exact relation to the corrected conormal cubics

Denote the corrected conormal cubics by `P(r)` and `Jcub(r)`. In the
parameters used here they are

    P=Gr^3+[6delta B+delta^3-3delta^2]r^2
      +[3delta^2(a-B)+2delta^3]r-2a delta^3,
    Jcub=(G+2J)r^3+[3delta(2B+G)+5delta^3-3delta^2]r^2
      +[3(a+B)delta^2+delta^3-delta^4]r-(a+B)delta^3.

Normalize their finite-target evaluations by

    Pt=p^3 P(delta/p)/delta^3
      =G+(6B+delta^2-3delta)p+(3a-3B+2delta)p^2-2ap^3,
    Jt=p^3 Jcub(delta/p)/delta^3
      =G+2J+(6B+3G+5delta^2-3delta)p
        +(3a+3B+delta-delta^2)p^2-(a+B)p^3.

Then

    2V=-(3-p)Pt+(3-2p)Jt,
    2W=(p^2-3p-6)Pt+3(2-p)Jt.                       (2)

The determinant of the displayed two-by-two coefficient matrix is
`2p Pc`. Its possible degeneration at `Pc=0` does not produce an extra
diagonal root on the regular fiber chart `pZ!=0`. Indeed, put

    H12d=G+(3-p)(delta^2+Bp),
    H13d=J-p(2-p)(delta^2+Bp).

The additional exact identities are

    (3-p)V-(3-2p)Z=p Pc H12d,
    (2-p)V-(4-3p)Z=-Pc H13d.                        (3)

At a root of `Pc`, neither `3-p` nor `3-2p` vanishes. Thus `V=0`
forces `Z=0`, outside the stated regular chart. Equations (1)--(3)
therefore prove, everywhere on `pZ!=0`,

    A2(delta/p,p)=C3(delta/p,p)=0
      if and only if P(delta/p)=Jcub(delta/p)=0.      (4)

This includes all possible degree drops of the cubics and quadratic;
there is no normalization `delta=1` and no omission of `p=2` or `p=3`.
The targets `p=0`, `p=infinity` and the locus `Z=0` are retained separately.

### 3. A small Sylvester identity and its false leading-drop factor

Write the exact cubic as

    C3=pA^2 r^3+d2 r^2+e2 r+f2,
    K=d2-pA b2, E=e2-pA c2,
    u=A E-K b2, v=A f2-K c2.

Polynomial subtraction gives

    A C3-(pA^2 r+K)A2=u r+v.                        (5)

Consequently the fixed-degree `(2,3)` Sylvester determinant is

    Res_r(A2,C3)=c2 u^2-b2 uv+A v^2=A Rn,

where the compact polynomial is

    Rn=A c2 E^2-b2 K c2 E-A b2 E f2+b2^2 K f2
       +A^2 f2^2-2A K c2 f2+K^2 c2^2.               (6)

For example, when `A!=0`, evaluate (5) at the two roots of `A2`:
the two factors of `A` in `A C3` cancel the corresponding difference
between the cubic and linear resultant degrees. This proves the first
equality on the dense open `A!=0`, hence as a polynomial identity.
Expanding that first equality proves its factor `A` and (6).

The factor `A` really is a false common-root signal from simultaneous
leading drops, and must be divided before using this determinant on the
affine source chart. To check its removal without discarding a stratum,
put

    L=3delta^2p(2-p), n1=-delta^3(6-p^2).

The exact cubic coefficient identity is

    d2=A[p(2n1+L)+delta A]-pL^2.                    (7)

On `A=0` within `pZ!=0`, we have `Z=-L!=0`, hence `d2=-pL^2!=0`.
Thus `C3` becomes a genuine quadratic. Equation (6) specializes to

    Rn=d2*(d2 c2^2-e2 b2 c2+f2 b2^2).              (8)

If `b2!=0`, the expression in parentheses is the actual resultant of
the linear `b2 r+c2` and this quadratic. If `b2=0,c2!=0`, it is
`d2 c2^2!=0`, correctly recording no common root. If `b2=c2=0`,
the quadratic has a finite root over the algebraically closed field and
the expression vanishes, correctly retaining that case too.
Thus `Rn=0` detects actual affine common roots throughout `pZ!=0`.

Evaluating (5) on the diagonal also gives a denominator-free identity
combining the subresultant and conormal equations:

    p delta u+p^2 v
      =delta^2[A delta ZW-(delta A^2+K)V].           (9)

None of (5)--(9) bounds higher contact by first-normal data.

### 4. The primitive degree-eight polynomial

There is the exact factorization

    Rn=p^2 delta^6 Z^2 F(p),
    Res_r(A2,C3)=A p^2 delta^6 Z^2 F(p).            (10)

Here `F` is a polynomial in `QQ[delta,a,B,G,J,p]`, of formal degree
eight in `p`, with 344 monomials. Equation (6), together with (10), is a
compact definition of it; the exact divisibility is checked, not assumed.
After specialization the degree may drop. Homogenization to degree eight
retains the corresponding root at target infinity.

Since `p,delta,Z` are units on the stated chart, `F(p)=0` is equivalent
there to the existence of an affine common root of `A2,C3`, including
`A=0`. Combining this with (4), full inverse support forces every such
root to be diagonal and consequently a common conormal zero. Conversely,
a common conormal zero can coexist with an additional root. We do not
assert that a diagonal common root ensures full inverse support.

At `p=0`, let `Delta1` be the exact target-`z=1` polynomial from the
target-fiber note:

    Delta1=G(G+3delta^2)(G+delta^2+2B)
      +J[(delta^2-5B)G-3B(delta^2+3B)]-BJ^2.

The exact boundary value is

    F(0)=-3J Delta1.                               (11)

At target infinity, write `F8` for the coefficient of `p^8`. With the
actual two endpoint polynomials

    Pinf=-delta^2r^2+(B^2-delta B+a delta^2)r+a delta B,
    Qinf=(3delta^2+G)r^2+(3delta B-delta^3)r-delta^2B,

we have

    Res_r(Pinf,Qinf)=B^2 delta^2 F8,
    F8|_(B=0)=aG[(3delta^2+G)a-delta^3].            (12)

The first expression's `B^2` factor cannot be interpreted as an actual
off-c inverse point when `B=0`. The endpoint fiber analysis must be used
there: its off-c condition is `a!=0` together with `G=0` or
`(3delta^2+G)a=delta^3`. The case `a=B=0` is also a common conormal zero
at the endpoint. Likewise (11) does not replace the complete `p=0`
fiber analysis when `J=0`. No zero-locus claim for `Z=0` follows solely
from the removed factor `Z^2`; the denominator-free rank equations in
the target-fiber note remain authoritative for that locus.

### 5. Literal identity with the five-quadric determinant

The [accepted model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#2-dp5-a4-explicit-model-independent-audit)
gives the actual five quadrics

    Z4^2-Z3 Z5, Z2 Z4-Z1 Z5, Z2 Z3-Z1 Z4,
    Z2^2-Z3 Z4-Z0 Z5, Z1 Z2-Z3^2-Z0 Z4.

Set the target coordinates to `(1,1-p,(1-p)^3,(1-p)^4)` and retain
the two omitted projection variables `h,z`. Use the exact linear inverse

    U3=(X0-X1+B h)/delta,
    U2=(X2-3X1+2X0-G h+delta^3 z)/(3delta^2),
    U0=(X3-2X2+2X1-X0-J h+2delta^3 z)/delta^4,
    Z0=X0-a h-U3, Z1=-U3, Z2=h-U2, Z3=U2, Z4=z, Z5=U0.

For each transformed quadric, take the coefficients of
`h^2,hz,z^2,h,z`, in that order, and place them in one row of a
five-by-five matrix. Denote its determinant, before target substitution,
by `D(X)`. The exact identity checked independently here is

    F(p)=81delta^10 D(1,1-p,(1-p)^3,(1-p)^4).        (13)

The displayed linear inverse follows directly from the actual projection
coordinates. Equation (13) is a literal polynomial identity over
`QQ[delta,a,B,G,J,delta^(-1)]`; it is independent of any presumed
conductor interpretation. The parent research lane is proving that
`D(X)` is the actual conductor quadric via the Cohen--Macaulay
presentation of the projected normalization. That proof, rather than
the degree-eight match, is the required geometric bridge.


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_session_nonendpoint_diagonal_norm_2026_10_12.m2](../computations/verify_session_nonendpoint_diagonal_norm_2026_10_12.m2). No inherited computation was rerun for this consolidation.

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
