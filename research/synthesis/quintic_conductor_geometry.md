# Quintic conductor cones, singleton fibers and projection geometry

These are independently reviewed proofs for the actual
admissible nonendpoint degree-five A4 del Pezzo projections in
characteristic zero, with delta nonzero. They retain the whole
scheme-theoretic conductor. The
[Gorenstein-normalization theorem](quintic_gorenstein_normalizations.md)
closes mate existence in that carrier class; the identities, necessary
embedded families and constructive local/global controls here remain
useful geometry. No classification of arbitrary nonnormal quintics is
asserted.

## Mathematical organization and scope

All arguments are over an algebraically closed field of characteristic zero unless a subsection states otherwise. The fixed curve is \(C_0=[s^4:s^3t:st^3:t^4]\). In the nonendpoint chapters, \(S\) is the normal anticanonical degree-five \(A_4\) del Pezzo surface, \(c\subset S\) maps isomorphically to \(C_0\), and \(\delta\ne0\). An admissible center is disjoint from \(S\), so its projection is finite and birational. The **full inverse-support condition** (SUP) is \((\nu^{-1}C_0)_{\mathrm{red}}=c\); it forbids isolated extra inverse points as well as extra components. A hypothetical mate implies SUP, but satisfying a necessary conductor or contact condition does not construct a mate.

The exposition separates four logically different tasks:

1. **Conductor-cone geometry and the singleton-fiber test** (the first part of this document): the universal rank bound, the integral/reduced conductor consequences, the conditional vertex-incidence restriction, a necessary two-parameter family, and a concrete singleton fiber that nevertheless violates SUP. The rational sample table is not a classification.
2. **Carrier structure and normalization restrictions** ([structural proofs](#1-quintic-conormal-and-delpezzo-audit), [endpoint factor/contact proof](#2-quintic-endpoint-factor-independent-audit), and [low-pole spaces](#5-a4-low-pole-spaces)): necessary reductions, with their independent hypotheses and unresolved cases. These are not by themselves mate-existence results.
3. **Actual target fibers and inverse support** ([fiber equations](#complete-actual-target-fiber-equations), [the G=J=0 exclusion](#full-inverse-support-exclusion-when-gj0), and [projective boundary analysis](#projective-coverage-and-exact-boundary-directions)): source-chart coverage, denominator-free equations, exceptional fibers, and the limits of each exclusion.
4. **Residual-divisor exclusions** ([the eight 2+4 families](#nonendpoint-conic-plus-quartic-residuals-all-eight-families) and [the 3+3 cubic-pair proof](#nonendpoint-residual-cubic-pairs-complete-contact-and-coefficient-proof)): conditional on the accepted residual classification and SUP, with actual jets, coefficient matching, and exceptional strata retained in full.

The historical proof texts below are arranged by mathematical dependency, not by date. Their equations, proof steps, explicit counterexamples, exceptional loci, and qualifications remain in place. The standalone certificate transcriptions are preserved as archival evidence; no archived computation is represented as rerun. The headings identifying their former supplement paths are retained as stable link destinations.

## Characteristic scope shared by the nonendpoint exclusions

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).

The exact hypotheses and exceptions of each exclusion remain in its proof; this common restriction does not extend any theorem beyond its stated admissible nonendpoint family.

## 1. Exact source and conclusions

Use the accepted degree-five normal anticanonical surface in P5 and
the four projection sections parameterized by `(delta,a,B,G,J)` in
the [restricted-conductor note, §5](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#2-nonendpoint-restricted-conductor-determinant).
The [independent module audit, §§4–5](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#4-conductor-quadric-module-independent-audit)
identifies the full downstairs conductor ideal with the three minors
of a matrix whose rows have degrees 2,1,1:

    [ a1  a2 ]
    [ b1  b2 ]
    [ c1  c2 ].

In particular its unique quadratic generator is `Q=b1 c2-b2 c1`;
the other generators are cubic. The conductor Gamma is Cohen–Macaulay,
has degree five and arithmetic genus two. These are properties of the
actual conductor scheme, including any multiplicities, not of a chosen
reduced double curve.

The conclusions are:

1. For every admissible projection in this family, Q has rank at most
   three, with no generic-parameter exception inside delta!=0.
2. If Gamma is integral as a scheme, Q has rank exactly three. Gamma
   is rational and has a unique singular point, at the vertex v of Q.
   Its local embedding dimension is three and its delta invariant is two.
3. If this integral-conductor carrier occurs in an actual (5,8) STCI
   presentation, then **v belongs to C0**.

The third assertion combines the second with the reviewed
[root-adjoining defect theorem, §8(a)](root_descent_and_conductor_defects.md).
It is a necessary incidence condition, not a sufficient descent test
or an exclusion of every carrier in this family.

## 2. A universal identity rather than a parameter sample

After the accepted inverse coordinate substitution, let M be the 5-by-3
matrix of coefficients of h^2,hz,z^2 in the five source quadrics. Let
L be their 5-by-2 matrix of coefficients of h,z. The latter entries
are linear forms in the target coordinates X0,...,X3. The accepted
audit proves that on every center-rank-three chart

    Q_univ=det[M | L]

is a nonzero scalar multiple of the actual conductor quadric. This
avoids choosing a single minor and discarding the other center charts.

The new [exact certificate](../computations/quintic_conductor_cone_identity.py)
forms this determinant by its ten-term Laplace expansion and computes

    det Hessian_X(Q_univ) = 0

over `QQ(delta,a,B,G,J)`. The expression before evaluation lies in
`QQ[a,B,G,J,delta,delta^-1][X0,X1,X2,X3]`: only powers of delta
have been inverted. The identity therefore specializes at every
delta!=0, including parameter values where an internal symbolic pivot
would vanish. In characteristic zero the Hessian is twice the symmetric
matrix of the quadric. This proves assertion 1.

The argument does not infer a symmetric minimal presentation merely from
abstract self-duality. Such a shortcut would need an additional
chain-level symmetry theorem. The exact identity supplies the needed
rank statement directly for this actual family.

## 3. Why an integral conductor has only the vertex singularity

If Q had rank at most two, it would factor into planes, possibly the
same plane twice. Integrality would force Gamma into one plane. An
integral plane quintic has arithmetic genus six, contradicting genus
two. Thus Q has rank three.

The four linear entries b1,b2,c1,c2 span exactly three independent
linear forms. If they spanned four, their determinant would be the
nondegenerate 2-by-2 determinant quadric; if they spanned at most two,
Q would have rank at most two. Their common zero is consequently the
unique vertex v. All three conductor minors vanish at v, so v lies
on the actual conductor and therefore on the quintic image.

The two quadratic relations on the normalization are

    a1+b1 h+c1 z=0,   a2+b2 h+c2 z=0.

Choose a point over v, which exists by finite surjectivity, and a
nonzero target hyperplane frame there. Evaluating gives a1(v)=a2(v)=0.
All three conductor equations therefore vanish to order at least two
at v. Since they generate the actual ideal, Gamma has embedding
dimension three there.

For completeness, the local delta bound can be seen directly. In a
reduced curve local ring R of embedding dimension e, choose a general
linear parameter l having minimum valuation on every normalized branch.
Then `length R/lR` is its multiplicity m. The Artin quotient R/lR
has embedding dimension at least e-1, so its length is at least
`1+(e-1)=e`. In the normalization Rbar, every element of the maximal ideal of R belongs
to l Rbar. Hence `Rbar/(R+l Rbar)` has length m-1 and is a quotient
of Rbar/R. Thus delta>=m-1>=e-1. Here delta_v>=2.

Finally

    2=p_a(Gamma)=g(Gamma_normalized)+sum_p delta_p.

It follows that delta_v=2, the normalized genus is zero, and no other
point is singular. This proves the integral-conductor conclusion. The stated(5,8) incidence follows
because the root-adjoining theorem requires `Sing(Gamma) intersect C0`
to be nonempty for a (5,8) presentation under the integral-conductor
hypothesis.

## 4. Exact specialized incidence and its limits

The complementary standard-library
[incidence program](../computations/quintic_conductor_singular_incidence.py)
uses exact rational arithmetic and adaptive row reduction on M. For
rank three it computes the actual conductor minors, their 3-by-4
homogeneous Jacobian, and all eighteen 2-by-2 Jacobian minors. It
restricts these equations to C0 and computes the saturated common-zero
divisor on P1, retaining the point s=0. This tests the actual singular
scheme of Gamma, not merely repeated zeros of Q restricted to C0.

Native executions gave the following intersection-scheme lengths. Each
row had center rank three and `length(Gamma intersect C0)=8`.

| delta | a | B | G | J | length(Sing(Gamma) intersect C0) |
|---|---|---|---|---|---|
| 11 | 2 | 3 | 5 | 7 | 0 |
| 1 | 1/8 | 3/8 | -5/4 | -1/8 | 0 |
| 1 | 5/24 | 7/12 | -31/48 | -15/32 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 0 |

In the three nonempty rows the affine gcd is t-1 in the s=1 chart,
with no point at infinity. These are scheme lengths rather than counts
of distinct geometric points. No row certifies conductor integrality
or mate descent. In particular the already-excluded G=J=0 source is
used only as an incidence control; its old exclusion is not reopened.

For these coordinates, center rank three itself ensures finite
birationality. The inverse linear change is invertible for delta!=0,
so the four target sections are independent. The five restricted
quadrics span all binary quadrics, so their center misses the source.
The resulting morphism pulls O(1) back to the ample anticanonical H;
it is therefore finite. Its degree times the image degree is H^2=5,
and independence excludes a plane image. Primality of five forces a
birational quintic image, whose normalization is the accepted normal
source. This does not prove the full singleton inverse condition on C0.

## Reduced conductors force the same cone

For the actual admissible nonendpoint A4 quintic projections, a
reduced full conductor Gamma forces the unique conductor quadric Q
to have rank three, even when Gamma is reducible. The
[universal identity](quintic_conductor_geometry.md) gives rank
at most three. If its rank were at most two, Gamma would lie in
at most two planes.

Every reduced conductor component is a singular curve of the
integral quintic S. In either plane Pi, each such curve occurs in
`F5|Pi` with multiplicity at least two: all tangential derivatives
vanish generically along it, and characteristic is zero. The plane
is not a component of the integral S, so this degree-five plane
section contains reduced singular-curve degree at most two. Across
two planes the total is at most four, contradicting deg Gamma=5.

This forces the actual reduced conductor onto the rank-three cone.
It does not prove irreducibility, describe the root class on its
components, or extend the integral-conductor vertex argument to
every reduced scheme.

The delta argument above deliberately uses the normalization quotient.
The plane-curve formula summing pairwise branch intersections does not
hold for arbitrary space curves: three coordinate axes have delta two,
not three. Also, the(2,3,3) Hilbert–Burch format alone does not force a
cone; a smooth-quadric curve of type(2,3) has the same degree and genus.
The rank bound is additional information from the actual projection.

## 6. The singleton vertex fiber gives a two-parameter necessary family

Retain the hypothetical (5,8) presentation and integral conductor.
The scheme fiber over the vertex has length three. Indeed all entries
of the conductor Hilbert–Burch matrix vanish at v, so the local
resolution is minimal and the dualizing module of Gamma has two
minimal generators. Tensor the actual sequence

    0 -> A -> B -> omega_Gamma(-1) -> 0

with the residue field at v. The unit 1 survives in B/m_A B, so the
map from the one-dimensional residue field is injective; the resulting
quotient has dimension two. Therefore `dim B/m_A B=3`.

Full inverse support makes this length-three fiber supported at the
single point of c mapping to v. This point cannot be the A4 point.
The inherited [actual cotangent calculation](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit)
gives length one if J!=0. If J=0 and `G(G+3delta^2)!=0`, the
[local fiber and phase audit](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#7-jbar-zero-conductor-phase-independent-audit)
gives length two. The exceptions are the already excluded G=J=0
family and the already excluded entire-line family G=-3delta^2,J=0;
their exact all-mate exclusions are retained in the
[G=J=0 proof](#full-inverse-support-exclusion-when-gj0) and the [full-line conormal bound](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit).
These accepted lanes are reused, not reopened.

At the remaining smooth source point, c maps immersively onto C0.
Consequently the local fiber has embedding dimension at most one, and
its tangent cannot be tangent to c. In the actual chart

    (U0,U1,U2,U3,U4,h)
       =(1,r,r^2,r^3-rT,r^4-(2r^2+r)T+T^2,T),
    c:T=0,

write its length-three jet as

    T=epsilon, r=r0+alpha epsilon+beta epsilon^2,
    epsilon^3=0.                                         (16)

This covers every length-three local fiber at a smooth c-point under
the immersion hypothesis. It is not an assumption that every length-three
scheme in a surface is curvilinear.

The jet spans a plane. Otherwise it would be collinear, and every
source quadric would vanish identically on that line, since a quadratic
on P1 cannot vanish on a length-three subscheme without vanishing
identically. The line would lie in the source. A center avoiding the
source projects that line isomorphically, contradicting its contained
length-three fiber.

The projection center meets the hyperplane h=0 at the fixed point

    P=(2/delta,1,delta/3,0,0,0).

Expand the displayed source coordinates in (16) as
`phi0+epsilon phi1+epsilon^2 phi2`. The intersection of their plane
with h=0 is spanned by phi0,phi2. Thus
`P=(2/delta)phi0+lambda phi2`. Comparing its U1,...,U4 coordinates
gives

    lambda beta=1-2r0/delta,
    lambda alpha^2=delta/3-2r0+2r0^2/delta,
    lambda alpha=r0(delta-r0)(delta-2r0)/delta,
    lambda=r0(delta-r0)[2r0(delta-r0)+delta-2r0]/delta.

The original equations rule out lambda=0 and r0=0,delta. Put
`rho=r0/delta`. Eliminating alpha and lambda yields the necessary
equation

    delta rho(1-rho)=(1-2rho)(1-6rho+6rho^2).             (17)

Conversely its solutions with delta!=0 and rho!=0,1 retain all the
nonzero factors used above. They determine

    delta=(1-2rho)(1-6rho+6rho^2)/(rho(1-rho)),
    r0=delta rho,
    alpha=1/[3(1-2rho)^2],
    lambda=3delta^2 rho(1-rho)(1-2rho)^3,
    beta=(1-2rho)/lambda.                               (18)

In particular rho=1/2 and the roots of 1-6rho+6rho^2 are excluded by
delta!=0, rather than silently divided out.

Every possible center line in this jet plane has form
`span(P,phi1+kappa phi0)`, modulo adding a multiple of P. The one
line lying entirely in h=0 contains the source point and is inadmissible.
Matching the U1=0 representative of the other center generator to
the actual projection coordinates gives

    a=-4r0^3 alpha+2r0^2+r0-kappa r0^4,
    B=delta(3r0^2 alpha-r0+kappa r0^3),
    G=-3delta^2[alpha(2r0-delta/3)
               +kappa(r0^2-r0 delta/3)],
    J=delta^4[2alpha/delta+kappa(2r0/delta-1)].            (19)

Thus the five-parameter nonendpoint source has been reduced, under the
stated STCI and integral-conductor hypotheses, to the two parameters
rho,kappa. Center avoidance, integral conductor, full inverse support
away from the vertex, and actual octic descent still have to be imposed.
Equations (18)–(19) do not assert that all these candidates satisfy
those conditions.

## 7. A genuine singleton vertex fiber and a global support failure

Take rho=2/3 and kappa=0 in §6. The resulting parameters are

    (delta,a,B,G,J)=(1/2,1/9,1/3,-9/8,3/4).

The exact rational example in this section
uses the accepted source sections and reviewed rational conductor
builder. It finds center rank three, so §4 gives an actual finite
birational normalization of an integral quintic. The conductor quadric
has rank three and its gradient vanishes at

    v=[1:-1/2:-1/8:1/16] in C0.

The scheme fiber over v in the smooth source chart is exactly

    (r-1/3-3T-54T^2, T^3).                             (20)

This is the entire projective fiber. The source boundary U0=0 has
underlying support the line Z2=Z3=Z4=Z5=0, as follows directly from
the five quadrics. Its image satisfies X2-3X1+2X0=0, while this
linear form has value 27/8 at v. There is therefore no omitted
boundary point. Equation (20) is a curvilinear triple fiber supported
at the one smooth c-point r=1/3,T=0. It shows concretely why a
length-three fiber is not itself a contradiction to singleton support.

The rest of the curve does fail the full inverse condition. The
corrected conormal cubics have homogeneous gcd r-1/3 and no common
root at infinity; J=3/4 also makes the A4 cotangent map surjective.
Meanwhile the actual conductor quadric restricts to C0, in u=t/s,
as a nonzero scalar multiple of

    (2u+1)^2(32u^6-8u^5+22u^3-u^2+9).                 (21)

The sextic is nonzero at -1/2 and the full contact form has degree
eight, so it gives a residual contact divisor of degree six away
from the sole smooth-source rank-drop point. Multiplicities are
retained; six distinct points are not asserted.

At each residual contact the marked point has a surjective target
cotangent map. If it were the only inverse point, the accepted finite
local cotangent lemma would identify the normalization and carrier
local rings, contradicting conductor contact there. Thus there are
actual additional inverse points outside c over C0. The necessary
full reduced inverse support condition fails. **This particular
quintic has no mate of any positive degree.** No inference from a
vertical exceptional cycle or just a numerical deficit is involved.

The example does not test conductor integrality, and is not a
realization of all hypotheses in the conditional family. It constructs
the desired local vertex behavior in an actual finite projection and
then locates the separate global failure. No uniform failure of
(18)–(19), or new STCI construction, follows from this one example.



## Exact support and limits of construction

The universal identity is computed in QQ[a,B,G,J,delta,delta^-1] using
ten Laplace terms, so its specialization proof includes every delta!=0
parameter, without relying on one symbolic pivot. The rational-incidence
program retains every row-reduction chart and the projective point at
infinity. Its displayed sample rows are controls, not an integrality or
emptiness certificate. The singleton-vertex example retains its full
projective boundary proof and exact fiber ideal; it constructs a real
finite birational quintic projection while failing full inverse support.

The retained exact programs are the [cone identity](../computations/quintic_conductor_cone_identity.py) and [rational conductor incidence](../computations/quintic_conductor_singular_incidence.py). The vertex example and uniform contact certificates have been retired after their mathematical statements and exact parameters were preserved above; their historical implementations remain in Git history.

The contact certificate on the full two-parameter family gives contact
exactly two, rather than merely repeated vanishing of a first symbol.
The [integral-conductor proof](quintic_gorenstein_normalizations.md#integral-conductor-full-contact-exceeds-the-differential-degree)
combines it with every smooth-contact bound to obtain8<=6, and makes
the vertex compulsory for every mate degree. The broader assembly uses
the same jet construction at any singleton smooth length-three conductor
fiber, with no additional cone-rank hypothesis. The actual code point
r0=delta*rho maps to the target curve at v=rho, whose standard C0
parameter is(rho-1)/rho. This keeps the generalized contact interpretation
bound to the certificate's coordinates.

These statements retain characteristic zero. In particular, the Hessian
rank interpretation needs two invertible; the retained projection charts
and exact nonzero Taylor factors have their own rational denominators.
Reducing one polynomial identity does not transfer source normality,
full-support arguments or the resulting carrier exclusion to all primes.
This integration has independent mathematical preservation and scope review; its conclusions retain the review scopes stated here.

## Historical L2 elimination: exact conditional formulas

The three retired Macaulay2 elimination scripts `generalization_quintic_l2_{drops,cover,boundaries}.m2` used the inherited primitive octic from the 2026-10-12 nonendpoint diagonal-norm calculation. Their conclusions are **conditional on that primitive polynomial and on the upstream support theorem**, and the historical computations are not new independent geometric proofs. In the following, `q` is the script's affine contact parameter (not the fixed quadric), `d=delta`, `k=kappa`, and all formulas are in characteristic zero. The substitutions preceding the coefficient test were

```
G=-(6B+d^2-3d)q-(3a-3B+2d)q^2+2aq^3,
J=(-G(1+3q)-(6B+5d^2-3d)q
   -(3a+3B+d-d^2)q^2+(a+B)q^3)/2,
B=k-aq, p=q+t.
```

Writing the resulting primitive octic as `F(t)=sum f_i t^i`, the tests impose `f_2=f_3=f_4=f_5=0`. The L2 quadratic in `k` was

```
L2=3q(q-1)(2d(q-1)+q(q-2))k^2
 -6dq(q-1)(d^2+d(3q-4)+q(q-2))k
 +d^5 q+3d^4(q-1)(3q-2)
 +6d^3 q(q-1)(2q-3)+3d^2 q^2(q-1)(q-2).
```

Put `P=q^2-6q+6`, `D=2d(q-1)+q(q-2)`, `E=d^2+d(3q-4)+q(q-2)`, and

```
L1=3k(q-1)^2 P+dq(3-2q)P-3d^2(q-1)^2(q-3).
```

The coefficient-drop computation establishes, modulo `L2`, a proportionality of the coefficient of `a` in `f_2` to `L1 * (partial L2/partial k)`; its scalar was computed exactly in the historical script but is not reproduced as a separately evaluated formula. This is a **coefficient identity**, not permission to divide on the `L1=0` or discriminant loci.

On the regular quadratic cover the scripts parameterized

```
d=3(q-2)P/[q(q-1)(3-m^2)],
k=d(E+m*d^2/3)/D,
a=-(f_2 at a=0)/(coefficient of a in f_2).
```

They substituted these expressions into `f_3,f_4,f_5`, took numerator ideals over `QQ(q,m)`, and saturated by the explicit excluded-factor product

```
q(q-1)(q-2)P*m*(m^2-3)*(q*m+3q-6)*numerator(L1).
```

The discriminant-zero subcase away from `q=2` was parameterized by `m=0`, `d=(q-2)P/[q(q-1)]`, `k=dE/D`. The leading-coefficient drop `D=0` instead gives `d=-q(q-2)/[2(q-1)]`, after which `L2` is linear in `k`; solving `f_2` for `a`, the historical elimination found `gcd(numerator(f_3),numerator(f_4))=q^4`, excluding the stipulated `q!=0` domain. At `q=2`, the remaining cover has `m^2=3`, `k=d+(3+m)d^2/6`; a Bézout certificate for `f_2,...,f_5` together with the inverted `d(d+2m/3)` support factor gave the unit ideal. These last two exclusions are **recorded exact computer-algebra conclusions under the inherited premises**, not assertions of an unrestricted quintic-carrier exclusion.

The scripts' stored intermediate factor files and Bézout coefficient vector are historical verification artifacts, not retained mathematical inputs. Their exact computational algorithm, equations, exceptional strata, and conclusion scopes are preserved here.


### Archived exact certificate: `research/computations/verify_typea45.py`

The following is the original computational certificate, preserved verbatim. Its stated scope and caveats remain in force; archiving does not independently validate or broaden its claims.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""Reconstruct every type-A (4,5) quotient chart and the terminal obstruction.

Characteristic-zero exact arithmetic. This independently derives the quotient
rank equations, excludes the two exceptional quotient lines by triple
flatness, and reconstructs the unique remaining triple/quadruple route from
the moving ambient coordinate W. It computes the final H^1(O(-9)) class rather
than merely testing the numerical vector recorded in P-025.

The mathematical justification for interpreting the calculations as
Banica--Forster extension obstructions is in
research/notes/2026-10-05-typea-audit.md.
"""

import sympy as sp

z = sp.symbols("z", nonzero=True)
theta = sp.symbols("theta")
MAX_NORMAL_DEGREE = 4


def clean(poly):
    result = {}
    for ij, coefficient in poly.items():
        if sum(ij) <= MAX_NORMAL_DEGREE:
            coefficient = sp.cancel(coefficient)
            if coefficient != 0:
                result[ij] = coefficient
    return result


def add(left, right):
    result = dict(left)
    for ij, coefficient in right.items():
        result[ij] = result.get(ij, 0) + coefficient
    return clean(result)


def scale(coefficient, poly):
    return clean({ij: coefficient * value for ij, value in poly.items()})


def multiply(left, right):
    result = {}
    for (i, j), left_coefficient in left.items():
        for (k, ell), right_coefficient in right.items():
            index = (i + k, j + ell)
            if sum(index) <= MAX_NORMAL_DEGREE:
                result[index] = result.get(index, 0) + left_coefficient * right_coefficient
    return clean(result)


def power(poly, exponent):
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def constant(value):
    return {(0, 0): sp.sympify(value)}


M = {(1, 0): sp.Integer(1)}
ELL = {(0, 1): sp.Integer(1)}


def exact_transition(u, v):
    """Return the moving coordinate W and exact split conormal jets."""
    a = v
    b = add(u, scale(sp.Rational(3, 2) * z, v))
    normalized_b = scale(z**-4, b)
    inverse_denominator = constant(0)
    for degree in range(MAX_NORMAL_DEGREE + 1):
        inverse_denominator = add(
            inverse_denominator,
            scale((-1) ** degree * z**-4, power(normalized_b, degree)),
        )
    W = multiply(add(constant(z**3), a), inverse_denominator)
    a_prime = add(scale(z, inverse_denominator), scale(-1, power(W, 3)))
    b_prime = add(inverse_denominator, scale(-1, power(W, 4)))
    u_prime = scale(sp.Rational(1, 2), a_prime)
    v_prime = add(scale(-3, multiply(W, a_prime)), scale(2, b_prime))
    return W, u_prime, v_prime


# Reconstruct the finite quotient chart and the genuinely missing chart.
MAX_NORMAL_DEGREE = 2
_, u_prime, v_prime = exact_transition(add(M, scale(-theta, ELL)), ELL)
m_prime = add(u_prime, scale(theta, v_prime))
h2 = sp.expand(m_prime[(0, 2)] * z**7)
assert sp.simplify(h2 - 3 * (
    theta**3 / z**5 - theta**2 / (2 * z**4)
    + theta / (4 * z**3) - 1 / (8 * z**2)
)) == 0

# Multiplication by delta in H^0(O(3)) must kill H^1(O(-7)) in H^1(O(-4)).
d0, d1, d2, d3 = sp.symbols("d0 d1 d2 d3")
delta = d0 + d1 * z + d2 * z**2 + d3 * z**3
kill_equations = [sp.expand(delta * h2).coeff(z, -index) for index in range(1, 4)]
rank_matrix = sp.Matrix([
    [sp.diff(equation, variable) for variable in (d0, d1, d2, d3)]
    for equation in kill_equations
]) * sp.Rational(8, 3)
assert rank_matrix == sp.Matrix([
    [0, -1, 2 * theta, -4 * theta**2],
    [-1, 2 * theta, -4 * theta**2, 8 * theta**3],
    [2 * theta, -4 * theta**2, 8 * theta**3, 0],
])
assert rank_matrix[:, [0, 1, 3]].det() == -16 * theta**4
assert rank_matrix * sp.Matrix([0, 2 * theta, 1, 0]) == sp.zeros(3, 1)
assert rank_matrix.subs(theta, 0).rank() == 2
assert sp.expand(z * (z + 2 * theta) * h2) == 6 * theta**4 / z**4 - sp.Rational(3, 8)

# At theta=0, delta=z^2(d2+d3*z), gamma_U=3(d2+d3*z)/8,
# gamma_V=0. The additional projective linear factor is a common zero.
assert sp.expand((d2 * z**2 + d3 * z**3) * h2.subs(theta, 0)) == -sp.Rational(3, 8) * (d2 + d3 * z)
_, u_infinity, v_infinity = exact_transition(ELL, M)
h_infinity = sp.expand(v_infinity[(0, 2)] * z**7)
assert h_infinity == 3 / z**5
assert [sp.expand(delta * h_infinity).coeff(z, -index) for index in range(1, 4)] == [0, 3 * d3, 3 * d2]

# The ambient diagonal torus carries every nonzero theta to theta=1.
MAX_NORMAL_DEGREE = 4
W, u_prime, v_prime = exact_transition(add(M, scale(-1, ELL)), ELL)
m_v = add(u_prime, v_prime)
ell_v = v_prime
delta_u = z * (z + 2)
gamma_u = sp.Rational(3, 8)
delta_v = add(W, scale(2, power(W, 2)))
gamma_v = sp.Integer(6)
A_u = add(scale(delta_u, M), scale(-gamma_u, power(ELL, 2)))
A_v = add(multiply(delta_v, m_v), scale(-gamma_v, power(ell_v, 2)))
p3 = sp.cancel(A_v[(1, 0)] / delta_u)
assert p3 == z**-10
remainder = add(A_v, scale(-p3, A_u))
assert remainder.get((0, 2), 0) == 0
q_b = remainder.get((1, 1), 0)
q_d = remainder.get((0, 3), 0)
h3 = sp.expand(sp.cancel((q_b * gamma_u * delta_u + q_d * delta_u**2) / p3))
assert h3 == z / 16 + sp.Rational(1, 4) + 8 / z**5 - 64 / z**6 - 144 / z**7
assert all(h3.coeff(z, -index) == 0 for index in range(1, 5))
rho_u = -(z + 4) / 16
rho_v_at_w = 8 - 64 / z - 144 / z**2
assert sp.simplify(h3 + rho_u - z**-5 * rho_v_at_w) == 0
assert sp.gcd(delta_u, rho_u) == 1
w = sp.symbols("w")
assert sp.gcd(w + 2 * w**2, 8 - 64 * w - 144 * w**2) == 1
rho_v = add(add(constant(8), scale(-64, W)), scale(-144, power(W, 2)))

# Exact quadruple generators. Both gamma charts are units, and (delta,rho)=1.
E_u = add(scale(delta_u, A_u), scale(-rho_u / gamma_u, multiply(M, ELL)))
E_v = add(multiply(delta_v, A_v), scale(-1 / gamma_v, multiply(rho_v, multiply(m_v, ell_v))))
H_u = add(scale(delta_u, multiply(M, ELL)), scale(-gamma_u, power(ELL, 3)))
H_v = add(multiply(delta_v, multiply(m_v, ell_v)), scale(-gamma_v, power(ell_v, 3)))
p4 = sp.cancel(E_v[(1, 0)] / delta_u**2)
assert p4 == z**-13

# Generic primitive coordinates evaluate the conormal maps. Every assigned
# generator image is regular; relations extend across delta=0 by torsion-free
# target descent. See the note for that justification.
ell = sp.symbols("ell")
m_order3 = gamma_u / delta_u * ell**2 + rho_u / delta_u**3 * ell**3
m_order4 = m_order3 + rho_u**2 / (gamma_u * delta_u**5) * ell**4


def evaluate_layer(poly, order, replacement):
    expression = 0
    for (i, j), coefficient in poly.items():
        if 2 * i + j <= order:
            expression += coefficient * replacement**i * ell**j
    return sp.cancel(sp.expand(expression).coeff(ell, order) * delta_u**2)


phi3 = lambda poly: evaluate_layer(poly, 3, m_order3)
phi4 = lambda poly: evaluate_layer(poly, 4, m_order4)
assert sp.simplify(phi3(A_v) - z**-15 * rho_v_at_w) == 0
assert sp.simplify(phi3(multiply(m_v, ell_v)) - z**-15 * gamma_v * (1 / z + 2 / z**2)) == 0
assert phi3(power(m_v, 2)) == 0
assert sp.simplify(phi3(power(ell_v, 3)) - z**-15 * (1 / z + 2 / z**2)**2) == 0

assert phi4(E_u) == 0
assert phi4(power(M, 2)) == gamma_u**2
assert phi4(H_u) == rho_u
assert sp.simplify(phi4(power(ELL, 4)) - delta_u**2) == 0
assert sp.simplify(phi4(power(m_v, 2)) - z**-22 * gamma_v**2) == 0
assert sp.simplify(phi4(H_v) - z**-22 * rho_v_at_w) == 0
assert sp.simplify(phi4(power(ell_v, 4)) - z**-22 * (1 / z + 2 / z**2)**2) == 0
h4 = sp.expand(sp.cancel(phi4(E_v) / p4))
expected_h4 = (
    -sp.Rational(5, 384) - sp.Rational(5, 64) / z
    - sp.Rational(5, 96) / z**2 + sp.Rational(5, 48) / z**3
    - sp.Rational(5, 24) / z**4 + sp.Rational(5, 12) / z**5
    - sp.Rational(5, 6) / z**6 + sp.Rational(5, 3) / z**7
    + 10 / z**8 - sp.Rational(124, 3) / z**9
    + 168 / z**10 + 432 / z**11
)
assert sp.expand(h4 - expected_h4) == 0
coordinates = tuple(h4.coeff(z, -index) for index in range(1, 9))
recorded_coordinates = (
    -sp.Rational(15, 512), -sp.Rational(5, 256), sp.Rational(5, 128),
    -sp.Rational(5, 64), sp.Rational(5, 32), -sp.Rational(5, 16),
    sp.Rational(5, 8), sp.Rational(15, 4),
)
assert coordinates == tuple(sp.Rational(8, 3) * value for value in recorded_coordinates)
assert coordinates[0] != 0
print("PASS: all type-A quotient strata, unique quadruple route, and terminal obstruction reconstructed")
print("H^1(O(-9)) coordinates:", coordinates)
print("The vector is 8/3 times the vector previously recorded in P-025.")
```
</details>


### Archived exact certificate: `research/computations/verify_typeb45_corner.py`

The following is the original computational certificate, preserved verbatim. Its stated scope and caveats remain in force; archiving does not independently validate or broaden its claims.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""Verify the remaining rank-zero type-B (4,5) corner calculation.

This exact moving-coordinate calculation treats a0=b1=0, b0=1, a1=t.
It identifies the three characteristic-zero rank-zero parameters and checks
that the next gluing datum has gamma=0.  The final length-four fiber is the
explicit local Bănică--Forster flatness obstruction.
"""

import sympy as sp


t, z = sp.symbols("t z", nonzero=True)
MAX_NORMAL_DEGREE = 4


def clean(poly):
    return {
        ij: sp.cancel(coefficient)
        for ij, coefficient in poly.items()
        if coefficient != 0 and sum(ij) <= MAX_NORMAL_DEGREE
    }


def add(left, right):
    result = dict(left)
    for ij, coefficient in right.items():
        result[ij] = result.get(ij, 0) + coefficient
    return clean(result)


def scale(coefficient, poly):
    return clean({ij: coefficient * value for ij, value in poly.items()})


def multiply(left, right):
    result = {}
    for (i, j), left_coefficient in left.items():
        for (k, ell), right_coefficient in right.items():
            if i + j + k + ell <= MAX_NORMAL_DEGREE:
                index = (i + k, j + ell)
                result[index] = (
                    result.get(index, 0) + left_coefficient * right_coefficient
                )
    return clean(result)


def power(poly, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def constant(value):
    return {(0, 0): sp.sympify(value)}


M = {(1, 0): sp.Integer(1)}
ELL = {(0, 1): sp.Integer(1)}

# m=t*z*v-u, ell=v; the ambient split frame is u=b-(3/2)za, v=a.
u = add(scale(-1, M), scale(t * z, ELL))
v = ELL
a = v
b = add(u, scale(sp.Rational(3, 2) * z, v))

normalized_b = scale(z**-4, b)
inverse_denominator = scale(
    z**-4,
    add(
        add(constant(1), scale(-1, normalized_b)),
        add(
            power(normalized_b, 2),
            add(scale(-1, power(normalized_b, 3)), power(normalized_b, 4)),
        ),
    ),
)
W = multiply(add(constant(z**3), a), inverse_denominator)
a_prime = add(scale(z, inverse_denominator), scale(-1, power(W, 3)))
b_prime = add(inverse_denominator, scale(-1, power(W, 4)))
u_prime = scale(sp.Rational(1, 2), a_prime)
v_prime = add(scale(-3, multiply(W, a_prime)), scale(2, b_prime))
m_v = add(scale(t, v_prime), scale(-1, multiply(W, u_prime)))
ell_v = scale(1 / t, u_prime)

linear_m = sp.factor(m_v[(1, 0)])
linear_ell = sp.factor(ell_v[(0, 1)])
h2 = sp.factor(m_v[(0, 2)] / linear_m)
assert linear_m == z**-8
assert linear_ell == z**-6

c1 = sp.factor(sp.expand(h2).coeff(z, -1))
c2 = sp.factor(sp.expand(h2).coeff(z, -2))
c3 = sp.factor(sp.expand(h2).coeff(z, -3))
expected_c2 = (2 * t + 1) * (12 * t**2 + 4 * t + 3) / 8
assert c1 == 0 and c3 == 0
assert sp.simplify(c2 - expected_c2) == 0

rank_zero_polynomial = sp.factor((2 * t + 1) * (12 * t**2 + 4 * t + 3))
assert sp.degree(rank_zero_polynomial, t) == 3

# When rank_zero_polynomial=0, the raw h2 is identically zero.  For a general
# delta in H^0(O(1)), gluing requires gamma_U=z^-3 gamma_V.  Since O(-3) has
# no global section, all coefficients of gamma vanish.
assert sp.rem(sp.together(h2 * z**2).as_numer_denom()[0], rank_zero_polynomial, t) == 0

w = sp.symbols("w")
d0, d1 = sp.symbols("d0 d1")
delta_u = d0 + d1 * z
delta_v = d0 * w + d1
assert sp.simplify(delta_v.subs(w, 1 / z) - delta_u / z) == 0

gamma_u_coefficients = sp.symbols("gU0:3")
gamma_v_coefficients = sp.symbols("gV0:3")
gamma_u = sum(gamma_u_coefficients[index] * z**index for index in range(3))
gamma_v = sum(gamma_v_coefficients[index] * w**index for index in range(3))
gluing = sp.expand(gamma_u - z**-3 * gamma_v.subs(w, 1 / z))
equations = [gluing.coeff(z, exponent) for exponent in range(-5, 3)]
solution = sp.linsolve(
    equations, (*gamma_u_coefficients, *gamma_v_coefficients)
)
assert solution == sp.FiniteSet((0, 0, 0, 0, 0, 0))

# At the zero of every nonzero delta, the proposed triple fiber ideal is
# (m*ell,m^2,ell^3); its standard monomials are 1,m,ell,ell^2, so its length
# is four instead of the required three.
standard_monomials = ((0, 0), (1, 0), (0, 1), (0, 2))
assert len(standard_monomials) == 4

print("PASS: all three type-B corner points fail the triple flatness test")
```
</details>


### Archived exact certificate: `research/computations/nodal_cubic_quintic_lattice.py`

The following is the original computational certificate, preserved verbatim. Its stated scope and caveats remain in force; archiving does not independently validate or broaden its claims.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""Finite E6 check used in ARTIFACT-20260821-019 (standard library only).

For a degree-three weak del Pezzo resolution with one A1 root alpha, enumerate
all numerical classes D having H.D=5, D^2=3, D.alpha=0, and nonnegative
intersection with the 15 simple lines (the -1 curves orthogonal to alpha).
The Cauchy bound restricts the leading coefficient to 2,...,8.  The script
verifies that every such class has exactly three simple lines disjoint from it.
"""
from itertools import product

def dot(x, y):
    return x[0] * y[0] - sum(a * b for a, b in zip(x[1:], y[1:]))

H = (3, 1, 1, 1, 1, 1, 1)
alpha = (0, -1, 1, 0, 0, 0, 0)  # a representative E6 root
lines = []
for i in range(6):
    b = [0] * 6
    b[i] = -1
    lines.append(("E" + str(i + 1), (0, *b)))
for i in range(6):
    for j in range(i + 1, 6):
        b = [0] * 6
        b[i] = b[j] = 1
        lines.append(("L%d%d" % (i + 1, j + 1), (1, *b)))
for i in range(6):
    b = [1] * 6
    b[i] = 0
    lines.append(("Q" + str(i + 1), (2, *b)))

simple = [(name, line) for name, line in lines if dot(alpha, line) == 0]
assert len(simple) == 15
classes = []
for a in range(2, 9):  # Cauchy: (3a-5)^2 <= 6(a^2-3)
    target_sum, target_square = 3 * a - 5, a * a - 3
    bound = int(target_square ** 0.5)
    for b in product(range(-bound, bound + 1), repeat=6):
        if sum(b) != target_sum or sum(x * x for x in b) != target_square:
            continue
        D = (a, *b)
        if dot(D, alpha) != 0 or any(dot(D, line) < 0 for _, line in simple):
            continue
        classes.append(D)

assert len(classes) == 120
zero_counts = [sum(dot(D, line) == 0 for _, line in simple) for D in classes]
assert set(zero_counts) == {3}
print("simple lines:", len(simple))
print("admissible quintic classes:", len(classes))
print("disjoint simple-line count:", sorted(set(zero_counts)))
```
</details>


### Archived exact certificate: `research/computations/explore_session_endpoint_a_nonzero_multiplicity_2026_10_11.m2`

Original source preserved verbatim, including its limitations and external dependencies.

<details><summary>Historical source</summary>

```macaulay2
-- Rational one-parameter analysis of exact target septic contact order.
OriginalRing=QQ[a,b,g,d,z,rho];
targetA=a*z-b;
targetU=2*a*z^3-3*b*z^2-z+g;
targetV=3*a*z^4-4*b*z^3-2*z^2-z+d;
targetH=a*z^3+z-g-1;
targetJ=targetA*targetV-(targetA*z-1)*targetU;
targetE=targetJ^2-(3*z*targetA-1)*targetH*targetJ+targetA*targetU*targetH^2;
targetCoef=(poly,j)->(
  derived:=poly; denominator:=1;
  for i from 1 to j do (derived=diff(z,derived); denominator=denominator*i);
  sub(derived,{z=>rho})/denominator
);
ParameterRing=QQ[q];
ParameterField=frac ParameterRing;
OrderRing=ParameterField[alpha];
parameterK=2-2*q-1/(3*q);
parameterRho=q/parameterK;
contactMap=map(OrderRing,OriginalRing,{
 alpha,alpha*parameterRho-parameterK,
 alpha*parameterRho^3-3*parameterK*parameterRho^2+parameterRho,
 alpha*parameterRho^4-4*parameterK*parameterRho^3+2*parameterRho^2+parameterRho,
 parameterRho,parameterRho
});
contactCoeffs=apply(toList(1..7),j->contactMap(targetCoef(targetE,j)));
print("COEFF1="|toString contactCoeffs#0);
print("COEFF2="|toString factor contactCoeffs#1);
linearA=lift(diff(alpha,contactCoeffs#1),ParameterField);
linearB=lift(sub(contactCoeffs#1,{alpha=>0}),ParameterField);
print("A2="|toString linearA);
print("B2="|toString linearB);
solvedA=-linearB/linearA;
print("SOLVEDA="|toString solvedA);
for j from 2 to 6 do print("SOLVEDCOEF"|toString (j+1)|"="|toString factor sub(contactCoeffs#j,{alpha=>solvedA}));
thirdNumerator=numerator lift(sub(contactCoeffs#2,{alpha=>solvedA}),ParameterField);
fourthNumerator=numerator lift(sub(contactCoeffs#3,{alpha=>solvedA}),ParameterField);
print("NUMERATORGCD="|toString factor gcd(thirdNumerator,fourthNumerator));
otherBeta=solvedA*parameterRho-parameterK;
qu2=2*solvedA;
qu1=2*solvedA*parameterRho-3*otherBeta;
qu0=2*solvedA*parameterRho^2-3*otherBeta*parameterRho-1;
qv3=3*solvedA;
qv2=3*solvedA*parameterRho-4*otherBeta;
qv1=3*solvedA*parameterRho^2-4*otherBeta*parameterRho-2;
qv0=3*solvedA*parameterRho^3-4*otherBeta*parameterRho^2-2*parameterRho-1;
otherSylvester=matrix {
 {qu2,qu1,qu0,0,0},
 {0,qu2,qu1,qu0,0},
 {0,0,qu2,qu1,qu0},
 {qv3,qv2,qv1,qv0,0},
 {0,qv3,qv2,qv1,qv0}
};
otherResultant=det otherSylvester;
print("OTHERRESULTANT="|toString factor otherResultant);
print("OTHERGCD="|toString factor gcd(thirdNumerator,numerator otherResultant));
print("DONE EXACT RATIONAL CONTACT EXPLORATION");
exit 0;
```
</details>



## Consolidated historical supplement: `research/supplements/QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md`

Original mathematical content and its qualifications are retained verbatim. Relative links refer to the source's original supplement location.

# Quintic carriers: conormal, factorization, residual divisors and low-pole spaces

## Integration guide: carrier structure is not mate existence

The conormal, factorization, residual-divisor, and low-pole-space analyses impose **necessary restrictions on a quintic carrier**. They do not automatically produce or exclude a homogeneous mate. The [endpoint jet/power-descent proofs](QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md), [endpoint residual-support calculations](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md), and [intrinsic A4 conductor/sextic incidence](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md) test additional compatibility conditions. The normalization, factorization, and mate-existence steps have distinct hypotheses; retain their separate computations and counterexamples.

---


Permanent mathematical supplement. The following five complete analyses retain their exact hypotheses, arguments, computations, limitations and corrections. Their constituent proofs are organized by subject rather than by chronological authority.

---

## 1. quintic conormal and delpezzo audit

# Quintic carriers: conormal, Gorenstein and genus-one structural audit

Date: 2026-10-11. Author: `quintic_conormal_audit`, delegated by
`oct11_quintic_structural_frontier`.

Status: **DIRECT PROOF AUDIT; NECESSARY STRUCTURAL REDUCTIONS**. No
quintic-carrier exclusion is claimed. No frontier file was edited.
The scope is the fixed smooth curve

    C=C0=[s^4:s^3t:st^3:t^4] in P3,

over an algebraically closed field of characteristic zero. We use the
accepted conormal calculation `N_C^*=O_P1(-7)^2`, the [P-005 smooth-carrier
obstruction](../synthesis/global_equations_and_constructions.md#p-005-a-smooth-carrier-obstruction),
the [P-006 formal-normal resultant theorem](../synthesis/formal-normal-intersection.md#p-006),
the [P-011 normal-order bound](../synthesis/formal-normal-intersection.md#low-degree-surfaces-singular-along-the-whole-quartic),
and the [P-015 fixed-carrier descent theorem](FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#canonical-compression-on-a-minimum-actual-carrier). Where
explicitly stated, we also use the [integral quartic carrier exclusion](../results/quartic_carrier_exclusion.md). The
unrestricted C0 and universal STCI questions remain open.

## 1. Generic order, compressed degree and the missing double divisor

Let X be an integral quintic occurring in a defining pair, and let the
other equation have degree b. P-011 proves that X has generic normal order
one along C; otherwise its equation is divisible by the unique quadric and
cannot be a successful carrier. The complete intersection has generic
multiplicity `r=5b/4`, so `b=4k` and `r=5k` for an integer k>0.

If the all-quartic exclusion is accepted, k=1 is impossible. Thus b>=8,
and the first degree pair to investigate is `(5,8)`, with multiplicity ten.
If X is a minimum integral carrier in a hypothetical presentation,
P-015 gives an actual compressed relation `eC~nH` on X, with

    5 divides e,   n=4e/5>=5,   e>=25/4.

Consequently e>=10 and n>=8. This does not prove that every quintic mate
compresses to degree eight: local Cartier orders and conductor descent can
force a larger value.

Let nu:S->X be the normalization and H=nu^*O_X(1). The unique prime c
over the generic point of C maps isomorphically to the entire smooth C.
Indeed c->C is finite birational, and its coordinate rings are integral
subalgebras of k(C) over the integrally closed rings of C. Hence they equal
those rings. We have `H^2=5` and `H.c=4`.

There is no actual relation `2c~mH` with integer m: intersecting with H
would give `8=5m`. More generally `jc~mH` requires `5|j` and `m=4j/5`.
The quartic normalization double-ribbon construction therefore cannot be
copied literally to degree five. Added resolution exceptional curves have
H-degree zero and do not repair the equation `8=5m`.

### Direct quintic normalization and global source constraints

The quintic carrier is regular at the generic point of C0. Otherwise restriction to the unique smooth quadric, where C0 has class(1,3), would contain twice C0 and leave residual class(3,−1), which is not effective. The quintic equation would have the quadric as a factor, contradicting integrality. This uses the saturated sheaf square, not an unsaturated ordinary ideal square.

Under a mate, full inverse support is the unique degree-one lift c≅C0. Its pullback divisor satisfies

    H²=5, H.c=4, b=4k, div(nu*G)=5k c~4k H,
    c_num=(4/5)H, c_num²=16/5.

Consequently c cannot be Cartier; a smooth normalization, or a lift avoiding its singular locus, is excluded in this lane. Any Cartier multiple r c requires5|r. These are normalization-index constraints, not conductor sufficiency.

The actual global quintic source has dimension dim I_C0(5)=35: sums of five weights from{0,1,3,4} cover0,...,20, proving surjective restriction of quintics to the binary degree-twenty space. The accepted first-normal map has image H0(O(13))² and kernel q I_C0(3), dimension7. These dimensions are not a parameter exhaustion or an all-power descent test.

## 2. A ribbon obstruction that survives singularities, and its limit

Suppose more generally that a normal surface S carries an actual effective
Cartier divisor R with Weil divisor 2c, where c is smooth. Normal surfaces
are Cohen--Macaulay, so R is a CM curve. Its nilradical J has generic rank
one, and J^2 vanishes generically. The latter is a finite-support subsheaf
of O_R and must be zero by Cohen--Macaulayness. The same argument removes
torsion in J. Thus R is an entire ribbon, including every singular point
of S, and J is a line bundle on c.

If R->P3 reduces to the embedding of C and is an immersion at the generic
point, the pullback of I_C induces a generically nonzero map

    N_C^* -> J.

Therefore `deg J>=-7`; for `deg J<-7` the Hom space is zero. Global
immersion of R is unnecessary. This is the direct proof used in the
accepted [quartic weighted-ribbon audit](GENUS_TWO_BISECTION_PROOF.md).

If S is Gorenstein in a neighborhood of R, Cartier adjunction and ribbon
duality give

    deg J=-2-deg((omega_S tensor O_S(R))|c).

Consequently a generically immersed Cartier double would require
`deg(omega_S|c)+R.c<=5`. The use of an actual Cartier double is essential.
For arbitrary S, neither its dualizing sheaf nor a numerical double class
may be silently treated as an invertible sheaf. In the quintic relation
`2c~mH` considered in Section 1, degree already prohibits the hypothesis.

For the standard Cartier adjunction interface, this audit freshly checked
the primary [Stacks effective-Cartier duality section](https://stacks.math.columbia.edu/tag/0B4C)
and [Gorenstein criterion](https://stacks.math.columbia.edu/tag/0DW9).
The ribbon and generic conormal deductions above are written out directly.

## 3. Multiplicity ten without global primitivity or a regular ratio

The separately delegated [multiplicity-ten filtration audit](MULTIPLICITY_MIXED46_AND_MF6.md#source-2026-10-11-session-multiplicity-ten-filtration-auditmd)
supplies a direct finite-flat Frobenius proof, read and checked by this
auditor. A hypothetical CI(5,8) is generically curvilinear by Section 1.
Its saturated graded pieces E_i are line bundles, even at nonprimitive
points, and their actual multiplication gives

    E_i tensor E_(9-i) = E_9,
    E_i=L^i(D_i),   D_0=D_1=0,
    D_i+D_j<=D_(i+j),   D_i+D_(9-i)=D_9.

Complete-intersection duality gives `E_9=O_P1(-38)`. The first quotient
`N_C^* ->> L` therefore leaves exactly

| deg L | direction degree deg L+7 | deg D_9 |
| --- | --- | --- |
| -7 | 0 | 25 |
| -6 | 1 | 16 |
| -5 | 2 | 7 |

An everywhere primitive multiplicity-ten structure is numerically
impossible: it would require `9 deg L=-38`. Genus gives the same socle
equation, not an additional independent restriction.

Writing A=D_2, B=D_3, C'=D_4 and T=D_9, all necessary defect data reduce to

    (0,0,A,B,C',T-C',T-B,T-A,T,T),

    0<=A<=B<=C', 2A<=C', 2C'<=T,
    A+B+C'<=T, 3B<=T.

All inequalities hold coefficientwise at every support point. P-010 also
forces A>0 when deg L=-7. The exact standard-library enumeration in the
linked child record leaves 198/97/13 necessary degree triples, 308 total.
Those are not 308 structures or a classification of higher normal jets.
This auditor did not execute a second copy of that enumeration and adds
no new execution count.

After replacing G8 by G8+HF5, with an ambient cubic H whose restriction to
C is nonzero, one may arrange that both equations have generic normal
order one without changing their ideal. Their saturated common kernel is
represented by a basepoint-free binary pair of degree e=deg L+7. In the
balanced frame their first normal forms can thus be written

    f_1=h ell,  deg h=13-e,
    g_1=k ell,  deg k=25-e.

This does not prove h divides k. The completed local pair

    F=t u+v^10,   G=u

has radical (u,v), is finite flat of rank ten over k[[t]], and has
first-normal ratio 1/t. It preserves the exact pole shield from P-026.
Nor may D_9 be equated with the first-normal Fitting divisor: the child's
rank-ten model `(t x-y^2,x^5)` has respective lengths four and one.

## 4. A global Gorenstein sectional-genus filter

Let pi be the genus of a general pulled-back hyperplane on S. Bertini
avoids the isolated singularities of normal S, and its image is a plane
quintic, so `0<=pi<=6`. A mate supplies `rc~bH`, hence
`c=(4/5)H` numerically as a rational Cartier divisor.

If K_S is Cartier, its intersection with the smooth c is an integer.
Adjunction on the general hyperplane gives `K_S.H=2pi-7`, so

    K_S.c=(4/5)(2pi-7) is an integer.

Thus `pi=1 or 6`. If X is nonnormal, its hypersurface S2 property makes
the nonnormal locus a nonempty curve. A general plane meets that curve,
and normalization reduces the plane-quintic arithmetic genus, so pi<=5.
In that case a Gorenstein normalization under a mate must have pi=1.

More generally, if a global Cartier index t for K_S is known, this gives
`5 divides t(2pi-7)`. No such filter is asserted when K_S is not known to
be rationally Cartier. Rational singularities alone do not supply the
Cartier hypothesis.

## 5. Low sectional genus: the ruled argument audited

Under the established normalization and actual rational-lift hypotheses above, a minimal resolution \(\sigma:M\to S\) has nef and big \(L=\sigma^*H\), with
\[
 L^2=5,\qquad K_ML=2\pi-7,\qquad L\widetilde c=4.
\]
The [characteristic-free ruled-surface criterion and integral gap](../synthesis/ruled_surface_degree_criterion.md) give a common proof of rationality for \(\pi\le3\).

For \(\pi\le2\), \(A=-K_ML=7-2\pi\ge3\), so \(A\cdot4>5\). At \(\pi=3\), the ordinary strict inequality fails, but
\[
 0<5-1\cdot4=1<4-1.
\]
This is the forbidden positive integral gap on a nonrational ruled birational class. The gap proof uses the actual fiber and integer blowup multiplicities, including infinitely near centers; it supplies the divisibility argument when the correction sum is zero.

Thus \(M\) is rational throughout \(\pi\le3\). This is the existing geometric reduction in a general form, not a carrier exclusion. The common surface criterion works in every characteristic once these actual lift and numerical inputs are established. The other quintic arguments retain their own characteristic and normalization hypotheses.

## 6. Sectional genus one forces a single A4 normalization

At pi=1, rationality and surface Riemann--Roch produce an effective divisor
E linearly equivalent to K_M+L with L.E=0. For existence it is enough
that chi(K_M+L)=1 and h2(K_M+L)=h0(-L)=0. E is sigma-exceptional. Minimal
resolution has no exceptional smooth rational (-1) prime, and every
exceptional prime P has `K_M.P=2p_a(P)-2-P^2>=0`. Thus

    E^2=sum coeff_P(E) K_M.P>=0,

contradicting negative definiteness unless E=0. Consequently

    K_M=-L,  K_M^2=5.

The contraction is crepant, with ADE singularities, and S is a degree-five
Gorenstein del Pezzo surface with `K_S=-H`. This uses the same minimality
and negative-definiteness proof as the accepted
[genus-one quartic reduction](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd).

In a rational degree-five del Pezzo marking, Pic(M) has basis h,e1,...,e4,
with L=3h-sum e_i. The roots P with L.P=0 and P^2=-2 are exactly
`e_i-e_j` and `+/- (h-e_i-e_j-e_k)`, 20 roots. Indeed writing
P=a h-sum b_i e_i gives sum b_i=3a, sum b_i^2=a^2+2; Cauchy forces
a=0,+/-1, and these equations give exactly the displayed list. Their root
system is A4. Its proper root subsystems are products of A_(r-1), where
the corresponding blocks partition five coordinates; none has a Cartan
matrix denominator divisible by five.

The smooth lift has `c#^2=2`. Write the pulled mate relation as

    c#+Z=(4/5)L,

where Z is its effective rational exceptional correction. Then
`-Z^2=6/5`. The exceptional intersection solution has denominator five,
so its graph must be the full A4, giving exactly one A4 singularity. Its
inverse Cartan matrix has diagonal `(4,6,6,4)/5`; a nonnegative integral
contact vector with norm6/5 is exactly the second or third unit vector.
Every contact vector with at least two positive entries has norm>=2.
Thus c# meets exactly vertex j=2 or3 once and transversely. For j=2,

    5Z=3E1+6E2+4E3+2E4;

the j=3 formula reverses the chain.

Because M is rational, numerical equality of divisor classes is linear
equality. The effective divisor `5c#+5Z` is therefore linearly equivalent
to 4L. Its section descends through `sigma_*O_M=O_S` to an actual section

    Q in H0(S,4H),  div(Q)=5c.

This proves the Cartier equivalence `5c~4H` by descent of an actual section;
it does not merely infer it from a rational numerical relation. Q cannot
be ambient if the quartic-carrier exclusion is accepted. Every mate of
degree b=4k pulls back to scalar Q^k: the actual divisor is 5kc, and the
quotient of two sections with that divisor is a global unit on normal
proper S. The unresolved question is whether any Q^k, k>=2, descends
through the entire conductor to X. No finite bound on k is proved.

## 7. The entire conductor in this genus-one quintic lane

Here `omega_X=O_X(H)` and `omega_S=O_S(-H)`. Finite duality identifies
the actual conductor ideal on S as

    I_S=O_S(-2H).

This is its actual invertible ideal in O_S, not only a numerical class;
its zero divisor D is Cartier in |2H|, with degree ten and arithmetic
genus six. Both reducible and nonreduced D are retained.

The respective Euler polynomials are

    chi(O_X(mH))=(5/2)m^2-(5/2)m+5,
    chi(O_S(mH))=(5/2)m^2+(5/2)m+1,
    chi(I_X(mH))=chi(O_S((m-2)H))
                 =(5/2)m^2-(15/2)m+6.

Consequently the entire downstairs conductor scheme Gamma satisfies

    chi(O_Gamma(mH))=5m-1,

so it has degree five and arithmetic genus two. I_X is MCM over the
Gorenstein hypersurface X, and the sequence
`0->I_X->O_X->O_Gamma->0` makes Gamma CM with no embedded or isolated
zero-dimensional components. MCM biduality gives
`Hom_X(I_X,O_X)=nu_*O_S`; dualizing that sequence therefore gives

    nu_*O_S/O_X=omega_Gamma(-H),

whose Euler polynomial is 5m-4. This retains the actual conductor scheme.
The degree comparison ten versus five does not establish that D->Gamma
is globally finite flat of rank two, or that Gamma is smooth or Gorenstein.
No replacement by a conductor line, branch polynomial, or reduced cover
has been made.

## 8. The unique line, complete restriction and tangent contact

In this degree-five del Pezzo setting the full anticanonical system embeds
S in P5, including its ADE points. On M, Riemann--Roch and characteristic-zero
Kawamata--Viehweg vanishing give h0(H)=6. The restriction to
`H0(c,O_P1(4))`, of dimension five, has a nonzero kernel.

The zero divisor of any kernel section is c+ell: the residual has H-degree
one, so ampleness makes it one reduced integral degree-one curve. Its
anticanonical image is a line, and hence ell is a smooth P1. Its strict lift
has self-intersection minus one by `K_M.ell#=-1` and adjunction. Numerically
`ell=(1/5)H`, so its exceptional correction again has norm6/5 and meets
A4 vertex2 or3 once.

Two distinct degree-one curves would have strict intersection
`1/5-(A4 inverse-Cartan cross entry)`. For these two allowed vertices,
the cross entry is at least4/5, making that intersection negative. There
is therefore exactly one degree-one curve ell on S. All kernel sections
have the same actual divisor c+ell, so their ratios are global units.
The restriction kernel has dimension one, and restriction to c is the
complete five-dimensional degree-four linear system.

The strict c and ell must meet opposite vertices: a common vertex gives
strict intersection `4/5-6/5<0`, while opposite vertices give
`4/5-4/5=0`. They are disjoint on M. The actual Cartier hyperplane divisor
c+ell is generically reduced and CM, hence reduced everywhere. Its
arithmetic genus is one. The union exact sequence gives

    0=chi(O_(c union ell))=1+1-length(c intersection ell),

so the entire intersection has length two, supported at the unique A4
point. Under the full anticanonical embedding, c spans a P4 as a rational
normal quartic, and ell is its tangent line at that point. This audit
does not infer a classification of all projections, uniqueness of the
carrier equation, or any power-descent obstruction from the tangent line.

The unique line satisfies5ell~H, by subtracting5c~4H from5(c+ell)~5H. If h is the section with divisor c+ell and u has divisor5ell, then Q=h^5/u is a regular section of4H with divisor5c. This is an actual intrinsic section identity, not a claim that either h,u or Q descends to the chosen four-coordinate projection. With a fixed marked center in the span of c, four lifts differ by the one-dimensional restriction kernel; the [intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md) retains the additional nonendpoint marking parameter and prevents treating the endpoint four-parameter subfamily as all projections.

## 9. The sectional-genus-zero exclusion also passes

Section 5 already proves rationality at pi=0. Restriction to a smooth
general hyperplane P1 of H-degree five gives h0(S,H)=7, since
h1(O_S)=h1(O_M)=0 and the section sequence has constants as its kernel.
The full system maps S finitely and birationally to a nondegenerate
degree-five surface in P6: finiteness follows from ampleness, and
birationality follows because the original four-dimensional subsystem
already maps birationally to X. Its image is a surface of minimal degree.
The surface classification in degree five gives exactly the scrolls
S(2,3), S(1,4), and the cone S(0,5). These normal images make the finite
birational complete map an isomorphism.

The two smooth scrolls contradict a mate because the smooth curve c is
Cartier while its numerical square must equal16/5. Resolve the cone by
F5, with negative section E and L=E+5f. A hypothetical lifted integral
curve of H-degree four has class aE+4f, with a>=0. If a=0, an integral
fiber component is a ruling of degree one. If a>=1, its intersection
with E is4-5a<0, forcing E as a component. A strict transform is not E,
so neither case permits this smooth quartic. The cone therefore cannot
contain the lift even before assuming a mate. This proves the pi=0
quintic-carrier exclusion in every mate degree, using the standard
minimal-degree classification already audited in the
[quartic genus-zero record](SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md).

## 10. Continuation boundary

The highest-value concrete genus-one quintic target is thus the actual
A4 del Pezzo normalization, its anticanonical projection to P3, the smooth
quartic meeting A4 vertex2/3, and descent of powers of its distinguished
nonambient quartic section through the CM degree-five genus-two conductor.
The general `(5,8)` target has three first-quotient directions and the
four-divisor filtration above, with nonregular-ratio strata retained.

Neither target is closed by this note. Higher sectional genera with
non-Gorenstein normalization, normal quintics, higher mate degrees,
carriers of degree at least six, and wholly thick presentations remain
outside any claimed exclusion here.


---

## 2. quintic endpoint factor independent audit

# Independent audit: the endpoint quintic quadric-factor and contact reduction

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit`.
Status: **DIRECT STRUCTURAL REDUCTION ACCEPTED**, under the actual
normalization and endpoint-projection hypotheses below. This is not a
quintic-carrier exclusion. No frozen note, record or existing
integrity seal is edited by this audit.

The owner source is the [endpoint quadric-factor reduction](#2-quintic-endpoint-factor-independent-audit).
The geometric inputs are the [quintic structural frontier](#1-quintic-conormal-and-delpezzo-audit),
its [independent conormal/del Pezzo audit](#1-quintic-conormal-and-delpezzo-audit),
and the [explicit model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
The [intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
separately records the required distinction between endpoint and nonendpoint
projection centers. The present statement applies to the displayed endpoint
projection; it does not replace that distinction by a four-parameter global
exhaustion of all quintic carriers.

Work over an algebraically closed field of characteristic zero. Thus S is
the normal degree-five anticanonical del Pezzo model, its sole singular
point is A4, and the actual smooth lifted quartic c and unique line ell
satisfy

    H~c+ell~5ell,       5c~4H,       H^2=5,       H.c=4.

Its actual six anticanonical coordinates restrict on the dense U0-chart as

    U0=1, U1=r, U2=r^2, U3=r^3-rT,
    U4=r^4-(2r^2+r)T+T^2, h=T.

Here `div(h)=c+ell`, c is T=0 on this chart, ell is at infinity, and
the A4 point on ell is `[U3:U4]=[0:1]`. The endpoint projection is

    X0=U0+a h, X1=U1+b h, X2=U3+g h, X3=U4+d h,

with center disjoint from S. Sections 3--7 below additionally assume a!=0.

## 1. Finiteness, image degree and the actual factor

The four sections are independent: their restrictions to c are the four
independent literal monomials of C0. Center avoidance makes them globally
generated. A curve in a projection fiber would have H-degree zero, contrary
to ampleness. Hence the actual map pi:S->P3 is finite onto its integral
two-dimensional image X. Its degree times deg(X) is H^2=5. Generic degree
five would make X a plane and impose a nonzero linear relation between the
four sections; independence excludes that. Therefore pi is finite
birational and X is an integral degree-five hypersurface. Since S is normal,
it is the actual finite normalization of X.

On ell only U3,U4 are nonzero, so pi maps it isomorphically to
`ell'=V(X0,X1)`. This is the tangent trisecant ruling line at the parameter
infinity of the literal C0 and lies on the unique smooth quadric
`q=X0 X3-X1 X2`. In the convention `[C0]=(1,3)` it has class `(1,0)`.

An exact homogeneous identity on S is

    pi*q = h K,
    K=a U4-b U3-U2-(1+g)U1+d U0+(1+ad-bg)h.

For direct verification, `U0 U4-U1 U3=h(-U2-U1+h)`; expanding the four
projection sections gives the displayed formula. An identity on the dense
U0-chart is an identity of the actual sections on integral S. Alternatively
q vanishes on c and ell, so division by the actual Cartier divisor c+ell
has nonnegative valuation at every prime divisor; normality extends the
quotient to a regular section of H. Neither argument performs division
only at the level of numerical classes.

This factorization is special to the endpoint placement. The tangent line
at a nonendpoint of the literal C0 is not contained in q; the same division
cannot be imported to the extra nonendpoint-center parameter.

## 2. The index-five class-group argument, explicitly reconstructed

Use the actual smooth four-point blowup marking from the model audit:

    Pic(M)=Z h_plane + Z e1 + Z e2 + Z e3 + Z e4,
    L=3h_plane-e1-e2-e3-e4,
    E1=e1-e2, E2=e2-e3, E3=e3-e4,
    E0=h_plane-e1-e2-e3, ell#=e4.

The four E's are the entire exceptional A4 chain. Removing them identifies
the remaining open of M with S minus its singular point. Weil localization
therefore gives `Cl(S)=Pic(M)/sum Z E_i`. In this quotient the explicit
relations are

    e1=e2=e3=e4=ell,       h_plane=3ell.

There is no residual torsion relation. Thus

    Cl(S)=Z ell,       [H]=5ell.

For a Cartier divisor downstairs, its pullback is orthogonal to all four
exceptional roots. Write its integral pullback class as
`A h_plane+sum B_i e_i`. Orthogonality to the three differences gives
`B1=B2=B3=B4=B`; orthogonality to E0 gives `A+3B=0`. The pullback is
therefore `-B L`. Conversely every integral multiple of L is the pullback
of the corresponding multiple of H. Consequently the Cartier classes in
Cl(S) form exactly `5Z ell`, generated by H.

This proves the index-five assertion by actual integral relations; no
numerical cancellation or unspecified lattice saturation is needed. In
particular every effective prime avoiding A4 is Cartier everywhere and has
strictly positive H-degree divisible by five.

## 3. The residual divisor is integral, with arithmetic genus one

At A4 every coordinate except U4 vanishes, so `K(A4)=a U4`. If a!=0,
the effective Cartier divisor D=V_S(K) avoids the sole singular point.
Each prime in it is therefore Cartier. Write D as a sum of primes with
positive integral multiplicities. Each has positive H-degree at least five,
while `H.D=H^2=5`. There is exactly one prime, with multiplicity one. Since
D is a Cartier divisor on a Cohen--Macaulay surface, it has no embedded
points. It is integral and reduced.

Cartier adjunction on the Gorenstein S gives

    p_a(D)=1+(H.(H+K_S))/2=1.

This is arithmetic genus one, not a proof of smoothness or geometric genus
one. D can be singular even though the ambient S is smooth along it.

## 4. The restriction is birational and its image has Q-type (3,2)

The actual restricted map D->R=pi(D) is finite. Its degree times deg(R)
is `H.D=5`. Generic degree five would make R a line. But the restriction
kernel of `H0(S,H)->H0(D,H|D)` is exactly `k K`: this follows from
`0->O_S->O_S(H)->O_D(H)->0` and `H0(O_S)=k`. The four projection sections
therefore retain rank at least three on D, so their image cannot be a line.
Thus D->R is finite birational and R is integral of degree five.

Because pi*q=hK, R lies on Q. The actual quintic section X intersect Q
contains the distinct integral curves C0, ell' and R, of degrees four,
one and five. These account for all of its degree ten. As X does not
contain the quadric surface, its restriction is a Cartier divisor on smooth
Q. It is consequently exactly their sum with multiplicity one. Therefore

    [R]=(5,5)-(1,3)-(1,0)=(3,2),       p_a(R)=2.

The exact injection of integral curve rings globalizes to

    0 -> O_R -> pi_*O_D -> F -> 0.

Its cokernel has finite support because the curve map is finite birational.
Arithmetic genera give

    length(F)=chi(O_D)-chi(O_R)=0-(-1)=1.

This is the difference between these two actual curve models. If D is
singular, it is not its normalization, so length(F)=1 is not being called
the entire normalization defect of R.

## 5. The local intersection-length comparison survives singular curves

Let p belong to R intersect C0. Choose a local Cartier equation phi of
C0 on smooth Q at p. It is nonzero in the domain `A=O_(R,p)`, because R
and C0 are distinct integral curves. For the finite semilocal module
`B=(pi_*O_D)_p`, multiplication by its pullback is also injective. Indeed D
is integral and maps dominantly to R, so this function is nonzero in its
function field. Neither smoothness of R nor smoothness of D is required.

Apply multiplication by phi to `0->A->B->F_p->0`. The resulting exact
length comparison is

    0 -> ker(phi:F_p->F_p) -> A/phi A -> B/phi B
      -> coker(phi:F_p->F_p) -> 0.

On any finite-length module the kernel and cokernel of an endomorphism
have equal length. Hence

    length(A/phi A)=length(B/phi B).

Over the algebraically closed field the latter is the sum of the local
intersection lengths at all D-points over p. The phrase nonzerodivisor
belongs to the two integral curve rings A and B. It must not be interpreted
as injectivity on F_p: for example phi can annihilate F_p. The allowed
kernel is precisely what cancels the cokernel length. The owner has
clarified this wording while this bounded audit was in progress.

Summing over p proves that the total zero length of the pulled local
C0-equations on D is the actual intersection product

    R.C0=(3,2).(1,3)=11.

## 6. Scheme divisibility proves exactly seven excess lengths under a mate

Now additionally assume the actual full inverse-support condition of a
hypothetical mate, `(pi^(-1)(C0))_red=c`. Every D-point above R intersect C0
must then belong to D intersect c. Since D avoids A4 and A4 is the unique
c-point above the endpoint, R cannot pass through that endpoint. All
contacts under discussion are therefore on the smooth finite r-chart.

At a contact P in D intersect c, the ambient S is smooth and c has an
actual local Cartier equation t_c. Lift phi from Q to a regular function
on an ambient P3 chart. Its pullback to S vanishes scheme-theoretically on
c, since the actual restriction pi|c is the given embedding into C0.
Thus it belongs to `(t_c)` in O_(S,P), and on D it factors as

    phi|D = (t_c|D) v_P.

Two lifts of phi differ by the local equation q times a regular function;
on D its pullback is zero by `pi*q=hK`. Thus the induced function on D is
well-defined independently of the lift. Divisibility is supplied by this
scheme-theoretic morphism, not merely by set support.

Both factors in the displayed product are nonzero in the local integral
curve ring O_(D,P). They define finite-length quotients. The exact sequence

    0 -> O_D/(v_P) -- multiplication by t_c -->
      O_D/(t_c v_P) -> O_D/(t_c) -> 0

shows that the pulled contact length is the actual D-c intersection length
plus the nonnegative excess `length(O_D/(v_P))`. Full inverse support puts
all its zeros at the actual contacts; there are no other support points.
Since D is Cartier of class H and avoids the only surface singularity,
its ordinary local intersection lengths with c sum to `H.c=4`. Therefore

    sum_P length(O_D/(v_P))=11-4=7.

This establishes the owner's seven-excess reduction in full scheme length,
including singular D and singular R. The difference module of length one
does not bound these excess contacts: its kernel/cokernel contribution
has already canceled in Section 5. High contact between the two different
image curves can occur even when each image branch is smooth.

## 7. Projective scaling and a bounded first-normal support consequence

The actual affine projection coordinates are

    X0=1+aT, X1=r+bT,
    X2=r^3+(g-r)T, X3=r^4+(d-r-2r^2)T+T^2.

In the target X0-chart one must divide by X0. The target parameter along
C0 is `X1/X0=r+(b-ar)T+O(T^2)`. Subtracting its cube and fourth power from
X2/X0 and X3/X0 gives the first-normal coefficients

    U=g-r-3br^2+2ar^3,
    V=d-r-2r^2-4br^3+3ar^4.

This calculation includes projective scaling and agrees with the owner.
The cubic equation of C0 on Q in this chart is
`phi=(X0^2 X2-X1^3)/X0^3`. Its exact numerator pulls back as

    X0^2 X2-X1^3=T*(U+T P1+T^2 P2),
    P1=a^2 r^3+2a(g-r)-3b^2 r,
    P2=a^2(g-r)-b^3.

The restriction of K to c is

    W=a r^4-b r^3-r^2-(1+g)r+d=V-rU.

At every finite contact X0 is a unit, because X0|c=1. If U(r) is nonzero
at a root of W, the second factor in the exact numerator is a unit at that
contact, so the excess there is zero. Thus positive excess can occur only
at common roots of W and U. This is a necessary support condition, not a
bound on the order of the excess at a common root, a first-normal proof of
higher contact behavior, or a parameter exhaustion.

Since a!=0, U has degree three, so at most three finite points can carry the excess. In particular, coprime U,V exclude a mate under the full-support hypothesis in this endpoint a!=0 lane. Seven is a total scheme length, so comparing it with three distinct points is not a contradiction. Repeated roots, singular D, tangential intersection and higher projection terms remain relevant.

The divisibility used in the exact local length argument comes from the actual morphism c→C0, not from equality of reduced support. For example, t=z² and phi=z in k[[z]] have identical zero support, but phi is not divisible by t. This control explains why the scheme-theoretic ideal containment is an essential step.

## 8. Exact evidence and remaining boundary

The delegated standard-library [sparse-polynomial checker](../validation/2026-10-11-quintic-endpoint-factor-audit/verify_polynomials.py)
supplies seven exact identities over `Z[r,T,a,b,g,d]`: q=hK, both first-normal
coefficients, W=K|c, W=V-rU, the full cubic residual factor and its relation
to the normalized quadric residual numerator. Its source SHA-256 is
`871099f080b3a69c58f15e6a6bd6a9475fd5cdfbba03008482ff7f23070de8ec`.

The delegated [algebra/contact audit](#2-quintic-endpoint-factor-independent-audit)
independently reconstructed both length exact sequences and the projective
scaling calculation. Its final SHA-256 is
`f4e86e9c5e0b88e1bfb9d145e72e5226f884184463abee9928cbdda3bb37cca6`.
Its bounded corollary excludes coprime U,V under the same full-support and
a!=0 hypotheses; it does not bound excess lengths at a common root.

The direct geometric arguments above establish the class-group, integrality,
finite-birationality and intersection-length claims. Passing polynomial
identities do not establish those claims or any universal STCI quantifier.

This audit accepts the factor and, for a!=0, the integral arithmetic-genus-one
residual, Q-type (3,2), length-one curve-model difference and exact seven-excess
necessity. It supplies no contradiction to that necessary condition. The
a=0 boundary, all remaining endpoint contact and conductor jets, the extra
nonendpoint projection-center parameter, other normalization genera, normal
quintics and the unrestricted fixed-C0 and universal STCI questions retain
their separate status. No higher-degree result is inferred from the completed
quartic-carrier theorem.


---

## 5. a4 low pole spaces

# Exact low pole spaces on the degree-five A4 normalization

Date: 2026-10-11. Owner: `oct11_nonendpoint_quadric_structure/nonendpoint_pole_spaces`.

Status: **DIRECT PROOF; PARENT REVIEW PENDING**. No mathematical CAS run is
claimed or required for the proof below. This note supplies the entire pole
filtration, its section spaces through degree six, and the possible degree
partitions of a residual divisor. It does not exclude any remaining projection
family or bound higher contact multiplicities.

Work over an algebraically closed field of characteristic zero. The normal
anticanonical degree-five surface S, its unique line ell, the complete smooth
quartic c, and the plane model are those of the
[intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
In particular H is ample, `H~5ell`, `c~4ell`, and the actual section U0 of H has
divisor 5ell. The
[explicit-model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
verifies the global model and its chart `U0!=0`.

## 1. The entire reflexive section filtration

The complement `S\ell={U0!=0}` is the affine plane with coordinates

    r=x/y, t=z/y=T-r^2.

All functions regular on this complement are consequently `k[r,t]`. Introduce

    v=t^2-r^3=Z0/U0.

At the generic point of ell, use the fourth blowup chart with coordinates
`x,u`, and set `A=1+xu`. The six anticanonical cubics, after the common base
factor has been removed, are exactly

    [Z0:Z1:Z2:Z3:Z4:Z5]
      =[u:A:x^2 A^2:x A:x^3 A^2:x^5 A^3].

Therefore the following are identities in the function field, not merely
first-order approximations:

    r=x^(-2) A^(-1),
    t=x^(-3) A^(-1),
    v=u x^(-5) A^(-3).                         (1)

In particular their exact pole orders along ell are 2,3,5. The last equality
follows from `t^2-r^3=x^(-6) A^(-3)(A-1)`. It records the cancellation that
a weight assignment to r and T alone would miss.

Every polynomial in `k[r,t]` has a unique expression as a finite k-linear
combination of monomials

    r^i t^j v^k,   i,k>=0, j in {0,1}.         (2)

Indeed the presentation

    k[r,t]=k[r,v,t]/(t^2-r^3-v)

is free with basis 1,t over `k[r,v]`, because its relation is monic quadratic
in t. The substitutions in (1) give exact pole weight

    w(i,j,k)=2i+3j+5k                         (3)

and leading coefficient `u^k`. In a sum of terms of maximal weight w, there
is at most one monomial with any fixed k: the equation
`2i+3j=w-5k`, with j equal to 0 or 1, determines j by parity and then i.
Consequently that sum has leading coefficient a nonzero polynomial
`sum a_k u^k` in the residue field k(u). No cancellation of the highest pole
weight is possible. Thus (3) computes the exact ell-valuation of every
polynomial written in its unique normal form (2).

For all n>=0, including n for which nell is not Cartier,

    H0(S,O_S(nell))
      = span_k{r^i t^j v^k : j in {0,1}, 2i+3j+5k<=n}.           (4)

Here `O_S(nell)` is the reflexive divisorial sheaf. To justify the global
equality, a section is a rational function f with `div(f)+nell>=0`. It is
regular on `S\ell`, hence lies in `k[r,t]`; conversely a polynomial with
ell-order at least -n has no negative coefficient at any prime divisor.
On a normal surface those codimension-one conditions are exactly the
definition of the reflexive divisorial sheaf. The A4 point on ell creates
no additional codimension-two extension condition.

## 2. The complete spaces through degree six

| n | Basis of H0(S,O_S(nell)) | Dimension |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | 1 | 1 |
| 2 | 1,r | 2 |
| 3 | 1,r,t | 3 |
| 4 | 1,r,t,r^2 | 4 |
| 5 | 1,r,t,r^2,rt,v | 6 |
| 6 | 1,r,t,r^2,rt,v,r^3 | 7 |

For comparison with the intrinsic anticanonical coordinates,

    U1/U0=r, U2/U0=r^2, U3/U0=-rt,
    U4/U0=v-rt, hsec/U0=r^2+t.                (5)

Thus the n=5 row recovers all six anticanonical sections, and the n=4 row
contains the function `T=r^2+t` defining c off ell.

## 3. Class group and possible residual component degrees

The localization sequence for Weil divisor classes gives

    Z[ell] -> Cl(S) -> Cl(S\ell)=Cl(A2)=0.

There is no nonzero relation on ell. If m ell were principal, intersection
with the ample Cartier divisor H would give `m(H.ell)=m=0`. Hence

    Cl(S)=Z[ell].                             (6)

For an integral prime P, write `[P]=m[ell]`. Then `H.P=m`, so m is its
positive projective degree. If m=1, P is linearly equivalent to ell and is
the divisor of a section of `O_S(ell)`. Since the n=1 row is one dimensional,
the only such effective prime is ell itself. Every other integral prime
therefore has degree at least two. This also directly proves uniqueness of
the degree-one prime from the pole calculation.

Suppose an actual quadric section q has

    div(q)=c+D, and ell is not a component of D.

Its residual divisor D has class `2H-c=6ell` and degree six. Formula (6)
and positivity restrict the multiset of prime degrees, with multiplicities,
to exactly

    6; 4+2; 3+3; 2+2+2.                     (7)

These are possible partitions, not assertions that every projection realizes
each partition. Multiplicities and coincidences remain included; for example
3+3 can be twice the same cubic prime, and 2+2+2 can contain repeated conics.
The assumption excluding ell must be checked for the projection under study.

The residual section has a particularly small exact normal form. Since
`div(hsec)=c+ell` and `div(U0)=5ell`, the rational function

    f=q/(hsec U0)

has divisor `D-6ell`. It belongs to the n=6 row and has exact pole order six
because D does not contain ell. Accordingly

    f=alpha r^3+beta v+gamma rt+delta r^2+epsilon t+zeta r+eta,
    alpha!=0.                               (8)

Equivalently, as a polynomial on the affine plane,

    f=beta t^2+gamma rt+epsilon t
        +(alpha-beta)r^3+delta r^2+zeta r+eta. (9)

The coefficient alpha, rather than either coefficient of t^2 or r^3 taken
separately, detects pole order six. This follows from the cancellation in
(1), and is essential on parameter strata where `alpha=beta`.

## 4. Exact forms of the low-degree prime components

The same normal form gives a useful exhaustive list for degrees two through
four. A prime of degree m other than ell is the closure of the affine zero
divisor of a polynomial with exact pole order m. There are no prime divisors
hidden solely at the singular point.

* Degree two: after scalar normalization the polynomial is `r-r0`. Its affine
  zero curve is a line in A2, integral and reduced, so its closure is the
  degree-two prime.
* Degree three: its polynomial is `t+B r+C`, again after scalar normalization.
  It is a graph, integral and reduced, and has exact pole order three.
* Degree four: its polynomial is `r^2+B t+C r+D`, after scalar normalization.
  It is an integral degree-four prime precisely when B is nonzero: then it is
  a graph over r. If B is zero, it factors over the algebraically closed field
  as a product of two polynomials `r-r0`, with repetition allowed, so is a sum
  of degree-two divisors instead.

Thus factoring the seven-dimensional form (8) decides the partitions in (7)
without treating either r or T as independent weighted variables. It supplies
no higher-contact bound at the singular point or at projection ramification
points.


## Consolidated historical supplement: `research/supplements/NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md`

Original mathematical content and its qualifications are retained verbatim. Relative links refer to the source's original supplement location.

# Nonendpoint actual target fibers and full inverse support

The common nonendpoint hypotheses, the meaning of SUP, and the characteristic-zero restriction are fixed in [Mathematical organization and scope](#mathematical-organization-and-scope). The intrinsic pair is established in the [A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md), and the actual projection and boundary equations appear in [Complete actual target-fiber equations](#complete-actual-target-fiber-equations). This chapter owns the literal target-fiber equations, denominator-free rank alternatives, all target endpoints, and the G=J=0 and equal-lift full-support exclusions. A resultant zero alone never replaces the actual off-c equations.

<a id="4-nonendpoint-target-fiber-reduction-and-bounded-exclusions"></a>
<a id="5-nonendpoint-target-fiber-independent-proof-audit"></a>

## Complete actual target-fiber equations

### 1. Actual pair, modulus and convenient lift parameters

Use the actual sections and chart in the
[pole-filtration and line-jet note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#3-nonendpoint-pole-filtration-and-line-jet-independent-audit),
with delta!=0 over an algebraically closed field of characteristic zero.
The accepted normalization pair and its complete open S minus ell=A2(r,T)
are supplied by the [intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
and [explicit model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
Assume the projection center avoids S whenever using an actual finite
normalization projection. Delta is retained as a modulus throughout.

Put

    B=b-a, G=g-3b+2a, J=d-2g+2b-a.

Then b=a+B, g=a+3B+G, d=a+4B+2G+J. The actual sections are

    U3=r^3-rT, U4=r^4-(2r^2+r)T+T^2,
    X0=U4+aT,
    X1=U4-delta U3+(a+B)T,
    X2=U4-3delta U3+3delta^2r^2-delta^3r+(a+3B+G)T,
    X3=U4-4delta U3+6delta^2r^2-4delta^3r+delta^4
       +(a+4B+2G+J)T.

On c:T=0 they give fixed C0 with target parameter z=(r-delta)/r.
The intrinsic A4 point maps to z=1, which is a nonendpoint of C0.

### 2. All off-c inverse points lie in this affine source chart

On the finite fourth-chart parameter u of ell, the four sections restrict to

    (u-1,u-1+delta,u-1+3delta,u-1+4delta).

Their quadric value is -3delta^2, so none of these finite ell-points maps
to C0. The missing ell-point is the intrinsic A4 point; it belongs to c
and maps to [1:1:1:1], i.e. z=1. Therefore every off-c point mapping to
C0 occurs in the actual complete open A2(r,T), with T!=0.

The following target-chart analysis consequently retains source infinity:
it does not mistake the A4 point for an affine point, or silently omit a
second source chart that could contain off-c inverse support.

### 3. Three linear target constraints and one actual normalization equation

For finite target z let p=1-z and let lambda=X0 be its projective scalar.
The three combinations of the actual coordinates give

    F1=delta r^3-(delta r+B)T-p lambda,
    F2=3delta^2r^2-delta^3r+G T-p^2(3-p)lambda,
    F3=delta^4-2delta^3r+J T+p^3(2-p)lambda.

Indeed X0-X1=p lambda, X2-3X1+2X0=p^2(3-p)lambda,
and X3-2X2+2X1-X0=-p^3(2-p)lambda for
lambda*(1,z,z^3,z^4). The combinations are invertible once X0 is
specified. Thus the full finite-target fiber is exactly

    F1=F2=F3=0, X0=lambda.

Under center avoidance any actual solution has lambda!=0: otherwise all
four actual sections vanish. All transverse terms, including T^2 in X0,
are retained. This is an exact fiber description rather than a first-jet
or tangent approximation.

### 4. A denominator-free reduction for every p!=0

Define

    H12=G+p(3-p)(delta r+B),
    H13=J-p^2(2-p)(delta r+B),
    R2=-delta r(pr-delta)*((3-p)r-delta),
    R3=delta(pr-delta)*(p(2-p)r^2+delta(2-p)r-delta^2),
    J0=pT^2+[delta r+B-p(2r^2+r-a)]T+r^3(pr-delta).

Eliminating only lambda, by division by the stated nonzero p, gives the
exact equivalent system

    H12 T+R2=0, H13 T+R3=0, J0=0.

Here lambda=(delta r^3-(delta r+B)T)/p. The equivalence follows from
F2-p(3-p)F1 and F3+p^2(2-p)F1, with J0=p(X0-lambda).
Consequently every leading-coefficient or minor degeneracy is retained.
If H12!=0 or H13!=0, solve the corresponding linear T equation and
substitute into the other equation and J0. If both vanish, Section 6
gives the complete compatibility analysis. No generic-rank hypothesis
replaces this case distinction.

### 5. A quadratic/cubic residual system on the specified regular chart

Put

    Z=Gp(2-p)+J(3-p),
    A=(3delta^2+G)p(2-p)+J(3-p),
    A2=A r^2+delta[delta^2p(p-3)+3Bp(2-p)+G(2-p)-J]r
       +delta^2[Bp(p-3)-G],
    N=delta^2(pr-delta)*[3(2-p)r-delta(3-p)],
    M=delta^2[3Jr^2+delta(2G-J)r-delta^2G].

The determinant of the three linear equations in (T,lambda,constant) is

    delta*p*(pr-delta)*A2.

Equivalently H12 R3-H13 R2=delta(pr-delta)A2. On the exact open
pZ!=0, Cramer's rule in F2,F3 gives

    T=-N/Z, lambda=M/(p^2Z).

The remaining normalization equation is

    Psi=p^2Z^2r^4+p^2Z(2r^2+r-a)N+p^2N^2-MZ
        =(pr-delta)C3,

where C3 is a polynomial of degree at most three in r. Its leading
cubic coefficient is pA^2. This statement allows A=0 and degree drop.
The quotient is an actual polynomial identity, not division by a curve
class or deletion of a fiber.

For r!=delta/p, the exact residual equations are therefore

    A2(r,p)=C3(r,p)=0.

Conversely every such solution on pZ!=0 reconstructs an off-c point.
If its T were zero, the four coordinate constraints and X0=lambda!=0
would say that the actual c-point r maps to z=1-p; its embedded target
parameter forces r=delta/p, a contradiction. If lambda were zero,
the actual projection would have a base point. Thus no additional scalar
or T artifact is discarded under the stated center-avoidance hypothesis.

Full inverse support consequently forces all common roots of this
quadratic/cubic pair to lie at r=delta/p on this chart. This is a compact
structural reduction; it does not prove that condition impossible for
all parameters. The locus Z=0 is governed by Section 4, not omitted.

### 6. All rank-one compatible fibers for p!=0

Suppose H12=H13=0. Compatibility requires R2=R3=0. The solutions are
exactly either

    r=delta/p,

or

    p^2-3p+3=0, r=delta/(3-p).

For completeness, r=0 makes R3=delta^4!=0. Otherwise, away from
pr=delta, R2 forces (3-p)r=delta; p=3 is impossible, and substituting
this value into the remaining quadratic gives
-delta^2(p^2-3p+3)/(3-p)^2. At either root of that p-polynomial,
r is nonzero and pr-delta!=0. These targets are the primitive cube
roots z=1-p, and are explicitly retained.

In the second case J0 is a quadratic in T with leading coefficient p!=0
and constant r^3(pr-delta)!=0. It has a nonzero root over the algebraically
closed field. Center avoidance makes its scalar lambda nonzero. Hence it
gives an actual off-c inverse point and excludes every mate degree.
Equivalently this excludes the precisely specified strata

    p^2-3p+3=0, r=delta/(3-p),
    G=-p(3-p)(delta r+B),
    J=p^2(2-p)(delta r+B),

for every a, subject to center avoidance.

In the first case J0 is

    T*[pT+pa+B-delta-delta^2/p].

Full support forces pa+B-delta-delta^2/p=0; otherwise the second T-root
is a genuine off-c point. With that coefficient zero the affine fiber
has only T=0, with its actual doubled structure retained. The rank-one
condition itself is

    G=-(3-p)(delta^2+Bp),
    J=p(2-p)(delta^2+Bp).

This gives a necessary exceptional-parameter condition, not an exclusion
of the allowed doubled fiber.

### 7. The intrinsic A4 target z=1, i.e. p=0

There is no affine c-point above this target. The exact off-c affine
equations are

    delta r^3-(delta r+B)T=0,
    3delta^2r^2-delta^3r+GT=0,
    delta^4-2delta^3r+JT=0.

Any common affine point has T!=0, since the first equation at T=0
forces r=0 while the third is then nonzero. Center avoidance supplies
X0!=0, so every such point is an actual off-c inverse point.

If J!=0, solve T=(2delta^3r-delta^4)/J. The remaining equations are
the cubic and quadratic

    P1=Jr^3-delta^2(delta r+B)(2r-delta),
    Q1=J(3r^2-delta r)+Gdelta(2r-delta).

Their leading coefficients J and 3J are nonzero. Their exact resultant is

    Res_r(P1,Q1)=-J^2 delta^6 Delta1,
    Delta1=G(G+3delta^2)(G+delta^2+2B)
           +J[(delta^2-5B)G-3B(delta^2+3B)]-BJ^2.

Thus J!=0,Delta1=0 excludes a mate in every degree; full support on
J!=0 requires Delta1!=0. No affine root at infinity or zero T is hidden
by this resultant because both leading coefficients remain nonzero and
T=0 was excluded directly.

If J=0, the third equation forces r=delta/2. Put D0=delta^2/2+B.
The first two equations are delta^4/8-D0T=0 and delta^4/4+GT=0.
An affine inverse point exists exactly when D0!=0 and G=-2D0, then
T=delta^4/(8D0). If D0=0 there is no point, even when G=0.
The J=0 case must not be inferred from the vanishing of the specialized
cubic/quadratic resultant.

### 8. The target endpoint z=infinity

The target equations are X0=X1=X2=0. In the source they are exactly

    delta r^3-(delta r+B)T=0,
    3delta^2r^2-delta^3r+GT=0,
    X0=0.

T=0 gives the unique affine c-point r=0. For off-c points with r=0,
the first two equations force B=G=0 and X0=T(T+a); thus such a point
exists precisely when a!=0,B=G=0, with T=-a. It maps to the endpoint
unless it is a forbidden projection base point.

For r!=0 the denominator Dr=delta r+B cannot vanish, by the first
equation. Solve T=delta r^3/Dr. The other equations reduce to

    Qinf=(3delta^2+G)r^2+(3delta B-delta^3)r-delta^2B,
    Pinf=-delta^2r^2+(B^2-delta B+a delta^2)r+a delta B.

If B!=0, a common root is automatically nonzero. Also Pinf(-B/delta)
=-B^3/delta!=0, so no denominator-zero root enters. Since Pinf has
nonzero quadratic leading coefficient, no common projective root at
r=infinity is introduced when Qinf drops degree. Consequently on B!=0
an off-c endpoint inverse point exists exactly when Res_r(Pinf,Qinf)=0.
This is another all-mate-degree excluded stratum.

If B=0, the r!=0 roots give r=a, a!=0 and
(3delta^2+G)a=delta^3. Together with the r=0 branch, the complete B=0
condition for an off-c affine endpoint inverse point is

    a!=0 and [G=0 or (3delta^2+G)a=delta^3].

If a=0 there is no off-c affine point above this endpoint. The endpoint
analysis and Sections 3--7 cover all projective target points of C0.

### 9. A complete subfamily exclusion: a=b=g=d

For a=b=g=d, B=G=J=0. This entire subfamily is base-point free.
On the affine open, a hypothetical base point would make all three
coordinate combinations zero. The third would force r=delta/2,
but the second would then equal delta^4/4, a contradiction. The complete projective-source boundary analysis below
rules out every boundary base point. These maps have pullback polarization H, which is ample. A positive-dimensional projective fiber would contain a curve of H-degree zero, so no curve is contracted and the proper map is finite. The four sections are linearly independent, hence the surface image is nondegenerate and cannot be a plane. The degree formula

    5=H^2=degree(map)*degree(image)

therefore gives degree(map)=1 and a degree-five integral image. Since S is normal, this finite birational map is its normalization. Thus the base-point-free calculation produces actual admissible quintic projections throughout this subfamily, before their full-support rejection.



This subfamily is B=G=J=0. If a!=0, (r,T)=(0,-a) has image
[0:0:0:delta^4], so it is an actual off-c endpoint point, with no base
point alternative.

It remains to take a=0. For p!=0,2,3 put

    r_s=delta(3-p)/(3(2-p)),
    lambda_s=delta^4/[3p^2(2-p)^2],
    P6=p^2-3p+3, Pc=p^2-6p+6,
    T_s=-delta^2 P6 Pc/[9p(2-p)^2(3-p)].

Direct substitution satisfies all three target constraints. The remaining
actual normalization equation is

    X0-lambda_s=delta^3 Pc V(p)/[27p^2(2-p)^3(3-p)^2],
    V(p)=p(3-p)^2 P6-9delta(2-p).

V is monic of degree five with p^4 coefficient -9. It has no roots
p=0,2,3: its values there are -18delta,2,9delta. At a root of P6,
V=-9delta(2-p)!=0. We claim V has a root outside Pc=0.

If all its roots were among the two distinct Pc-roots, evaluate at such
a root rho. Using rho^2=6rho-6 gives

    V(rho)=9[(5rho-6)-delta(2-rho)].

The two ratios (5rho-6)/(2-rho) are distinct: this fractional linear
map has nonzero determinant. Hence for any fixed delta, at most one
Pc-root is a V-root. All five roots would therefore be that one rho,
forcing V=(p-rho)^5. Comparing the p^4 coefficient gives rho=9/5,
but Pc(9/5)=-39/25!=0. This contradiction proves the claim.

Choose the asserted V-root outside Pc. The preceding value checks make
all denominators nonzero and P6!=0. Then T_s!=0, lambda_s!=0,
and X0=lambda_s, giving an actual off-c inverse point. This proves
every displayed projection with a=b=g=d has no mate in any degree,
for every nonzero delta. It is a bounded subfamily, distinct from the
entire-line ramification locus G=-3delta^2,J=0.

### 10. Why the endpoint septic proof does not transfer verbatim

The endpoint quadric divided into two anticanonical sections and left an
integral degree-five residual curve avoiding A4. In this nonendpoint
family the actual residual is the degree-six Weil divisor from the
pole-filtration note, with possible prime partitions 6,2+4,3+3,2+2+2;
there is no anticanonical quotient avoiding A4. The target z=1 is the
intrinsic A4 image, and its affine equations lose their scalar column.
The regular-chart denominator Z may also vanish identically, e.g. G=J=0.
These are actual structural differences rather than permissible generic
exceptions to drop.

The equations here preserve these differences. They yield finite systems
of degree at most two and three on the specified regular chart, explicit
rank-one fibers, and exact exceptional-target obstructions. They do not
bound all higher contact lengths in the remaining families or certify
full parameter exhaustion.

For the bounded reduction within G=J=0 and B!=0, the rank-one c-fiber forces
a=2B^2/delta^2-B/delta. The off-c branch still has the displayed r_s and
lambda_s, with

    E_s=delta^2(3-p)+3B(2-p),
    T_s=-delta^4 P6 Pc/[9p(2-p)^2 E_s].

The exact polynomial reduction factors the remaining normalization
numerator as delta^2 Pc times a degree-at-most-five polynomial V_B.
Under full support its leading coefficient is nonzero by the target-
infinity test, and V_B(2)=2delta^5. Its potential roots at p=0 are real
intrinsic-A4 pole strata; they cannot be discarded using the endpoint
root-count proof. This bounded reduction is used by the complete G=J=0 support exclusion below; by itself the displayed factorization is not that full exclusion.


<a id="1-nonendpoint-conductor-infinity-coefficient"></a>

## A simple conductor root at target infinity

Let `F(p)` be the exact polynomial bound in that note and put `a=B=0`.
Direct coefficient extraction gives, for every `delta,G,J`,

    coefficient_(p^8) F=0,
    coefficient_(p^7) F=delta^7.                    (1)

Since `delta!=0`, homogenization of `F` to degree eight has exactly a
simple zero at `p=infinity`. This uses the literal section, not an
upper bound inferred from its first-normal zero locus.

The [new coefficient checker](../computations/verify_session_nonendpoint_conductor_infinity_coefficient_2026_10_12.py)
reads the frozen 344-monomial primitive polynomial, validates its exact
SHA-256, and reconstructs it through elementary integer polynomial
arithmetic using Python's standard library. It performs no `eval`, uses
no CAS dependency, and does not replay the fifteen-check M2 source.

The following geometric consequence depends on the separate
[restricted-conductor determinant argument](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#2-nonendpoint-restricted-conductor-determinant).
Its independent mathematical audit is ongoing at this note's freeze.
Once that argument identifies `F` with a unit multiple of the actual
degree-eight conductor restriction, its zero at target infinity has
exactly length one on every admissible projection with `a=B=0`.
The conormal cubics already have a common root at that endpoint, because
their constants vanish there (`a=b=0`). Under full inverse support all
other conductor zeros must be supported at another common conormal
root, or at the A4 point if `J=0`.

In particular, with `J!=0`, a parameter value for which the sole common
conormal root is target infinity cannot have full inverse support:
that point has length one while the total conductor restriction has
degree eight. This is conditional on the actual-conductor geometric
bridge, rather than inferred solely from a polynomial degree match.
It is not a full common-root incidence exclusion or a universal STCI
statement.


---


<a id="2-nonendpoint-GJ-zero-full-support-exclusion"></a>
<a id="2-nonendpoint-gj-zero-full-support-exclusion"></a>
<a id="3-nonendpoint-GJ-zero-full-support-independent-audit"></a>
<a id="3-nonendpoint-gj-zero-full-support-independent-audit"></a>

## Full inverse-support exclusion when G=J=0

### 1. Claim and actual geometric scope

Work over an algebraically closed field of characteristic zero. Use the
actual intrinsic pair and nonendpoint sections in the
[target-fiber reduction](#complete-actual-target-fiber-equations),
Sections 1--3. That note is frozen during its separate audit; this is a
new continuation beyond its explicitly open G=J=0 lead.

On the complete open S minus ell=A2(r,T), put

    U3=r^3-rT,
    U4=r^4-(2r^2+r)T+T^2,
    B=b-a, G=g-3b+2a, J=d-2g+2b-a.

The nonzero modulus delta is retained. In the subfamily G=J=0 the actual
four sections are

    X0=U4+aT,
    X1=U4-delta U3+(a+B)T,
    X2=U4-3delta U3+3delta^2r^2-delta^3r+(a+3B)T,
    X3=U4-4delta U3+6delta^2r^2-4delta^3r+delta^4+(a+4B)T.

Assume that the projection center is disjoint from S. The lifted curve
c is T=0; its target is fixed C0=[1:z:z^3:z^4], with
z=(r-delta)/r. The intrinsic A4 point is the missing c-point r=infinity
and has target z=1. Every off-c point mapping to C0 lies in the displayed
affine chart: finite ell-points have quadric value -3delta^2 and the
remaining ell-point is A4 on c. These are the verified projective-chart
facts from the preceding reduction, Section 2.

**Claim.** For every a,B and nonzero delta in this subfamily, under center
avoidance there is an actual point off c mapping to C0. Hence
(pi^{-1}(C0))_red=c cannot hold. The full-support theorem imported in the
[quintic structural frontier](#1-quintic-conormal-and-delpezzo-audit),
Section 1, makes that equality necessary for a mate, so this is an
all-mate-degree exclusion in the stated normalization/projection lane.

If B=0, the claim is already proved in Section 9 of the frozen reduction:
it is the complete a=b=g=d subfamily. Thus it remains to prove the claim
for B!=0. No division by B in this note silently discards that case.

### 2. The doubled c-fiber forces a unique lift parameter

Suppose for contradiction that the projection has full inverse support.
Set

    k=B/delta^2,                     k!=0.

Use p=1-z for finite targets. The exact three linear target constraints
and actual normalization equation are

    F1=delta r^3-(delta r+B)T-p lambda=0,
    F2=3delta^2r^2-delta^3r-p^2(3-p)lambda=0,
    F3=delta^4-2delta^3r+p^3(2-p)lambda=0,
    X0=lambda.

For p!=0, eliminating only lambda gives the denominator-free system in
Section 4 of the frozen reduction. Its final equation is

    J0=pT^2+[delta r+B-p(2r^2+r-a)]T+r^3(pr-delta)=0.

At the actual c-point

    p_c=-1/k,       r_c=delta/p_c=-k delta,

the two linear T-coefficients H12,H13 vanish, as do their constant terms.
The remaining equation is exactly

    T*[p_c T+p_c a+B-delta-delta^2/p_c]=0.

If the bracket's constant coefficient is nonzero, its second root gives
an actual off-c point above that finite target; center avoidance forbids
lambda=0. Thus full support forces

    a=2k^2 delta^2-k delta
     =2B^2/delta^2-B/delta.                  (1)

With (1), this exceptional c-fiber is the doubled T=0 fiber. It is
retained, rather than erroneously excluded by a first-normal argument.

### 3. Target infinity forbids a quintic degree drop

The target z=infinity requires X0=X1=X2=0. For a nonzero r, solving the
first actual coordinate difference gives

    T=delta r^3/(delta r+B).

The remaining equations are the exact polynomials from Section 8 of the
frozen reduction,

    Pinf=-delta^2r^2+(B^2-delta B+a delta^2)r+a delta B,
    Qinf=3delta^2r^2+(3delta B-delta^3)r-delta^2 B.

After substituting B=k delta^2 and (1), they satisfy

    Qinf=3delta^2(r+k delta)(r-delta/3),
    Pinf(-k delta)=-k^3 delta^5!=0,
    Pinf(delta/3)=-delta^4 L/9,
    L=(1+3k)^2-9delta k^2(1+2k).             (2)

The r=-k delta value has denominator zero and is explicitly impossible.
At r=delta/3 the denominator is delta^2(k+1/3). If it vanished,
k=-1/3 and L=-delta/3!=0. Therefore L=0 gives r=delta/3 with a nonzero
denominator, and its T is nonzero. It is an actual off-c inverse point
at infinity; center avoidance supplies X3!=0. Consequently a hypothetical
full-support projection must satisfy

    L!=0.                                  (3)

This handles the projective leading-coefficient boundary before any
root-count argument. It is not an assumed generic degree condition.

### 4. A compact actual off-c branch and its quintic equation

For p!=0,2 define

    P6=p^2-3p+3,        Pc=p^2-6p+6,
    E=(1+3k)p-3-6k,
    E_s=delta^2(3-p)+3B(2-p)=-delta^2 E,
    r_s=delta(3-p)/(3(2-p)),
    lambda_s=delta^4/[3p^2(2-p)^2].

If E!=0, define

    T_s=delta^2 P6 Pc/[9p(2-p)^2 E]
       =-delta^4 P6 Pc/[9p(2-p)^2 E_s].

Direct substitution in the actual F1,F2,F3 gives zero identically. The
remaining normalization equation, retaining T^2 and the actual forced a,
is the exact identity

    X0(r_s,T_s)-lambda_s
       =delta^3 Pc W(p)/[27p^2(2-p)^3 E^2],                 (4)

where the compact degree-at-most-five polynomial is

    W(p)=p P6 E^2
          -9delta(p-2)(k p^2-2kp-1)
             *(2k^2p^2-6k^2p+kp^2+6k^2-4kp+6k+1).       (5)

Its leading coefficient is exactly L from (2), and W(2)=2. Thus (3)
makes W a polynomial of degree exactly five. The exact source verifies
the actual three constraints and (4), rather than merely a formal
elimination numerator or a first transverse jet.

### 5. Every W-root lies among three retained exceptional targets

We prove that full support forces every W-root into

    {0,rho_plus,rho_minus},
    rho_plus=3+sqrt(3), rho_minus=3-sqrt(3).                (6)

These are p=0 and the two distinct Pc-roots. The p=0 value is the actual
intrinsic-A4 target z=1 and is deliberately retained. We do not assert
that all three targets are individually allowed; an enlarged necessary
root set suffices for the contradiction below.

Let p0 be a root of W outside (6). It is not 2, by W(2)=2. First suppose
E(p0)!=0. Then (4) gives X0=lambda_s. If P6(p0)!=0, the displayed T_s
is nonzero, while lambda_s is also nonzero, so this is an actual off-c
inverse point and contradicts full support.

If P6(p0)=0 instead, T_s=0. Since Pc(p0)!=0, the exact identity

    p(3-p)-3(2-p)=-Pc

shows r_s!=delta/p. Yet the three constraints and X0=lambda_s!=0 would
make that actual c-point r_s map to z=1-p. The embedded curve c has
the injective target parameter z=(r-delta)/r, forcing r_s=delta/p.
This is a contradiction. Thus a P6-root with E!=0 cannot be a W-root.

It remains to retain, rather than divide away, E(p0)=0. The polynomial
identity

    3(2-p)W-delta P6^2 Pc is divisible by E                 (7)

is checked exactly. Since p0!=2, delta!=0 and Pc(p0)!=0, (7) and
W(p0)=0 force P6(p0)=0. At a P6-root the displayed r_s is also

    r_s=delta/(3-p).

Moreover delta r_s+B=E_s/[3(2-p)]=0, so H12=H13=0 at that actual
point. Both remaining linear-equation constants vanish: this is the
second rank-one compatible fiber from Section 6 of the frozen reduction.
It is distinct from r=delta/p because Pc and P6 have no common root.
The actual J0 equation there is a quadratic in T with leading p!=0
and constant r_s^3(pr_s-delta)!=0. It has a nonzero T-root in the
algebraically closed field. Center avoidance makes the reconstructed
lambda nonzero. This is another actual off-c inverse point.

Every E-zero W-root outside (6) has therefore been settled by its actual
fiber, and no exceptional denominator remains. This proves (6). The
argument also allows p=3 and k=-1/3 whenever their actual formulas do;
neither is deleted by an auxiliary saturation.

### 6. Twenty-one complete coefficient profiles have polynomial unit certificates

Over the algebraically closed characteristic-zero field choose s with
s^2=3 and set rho_plus=3+s,rho_minus=3-s. From degree five, leading
coefficient L!=0 and (6), there are nonnegative integers i,j,h such that

    i+j+h=5,
    W(p)=L p^i(p-(3+s))^j(p-(3-s))^h.                     (8)

There are exactly twenty-one such triples. All multiplicities, including
every possible order at p=0, are retained. Write c_t=[p^t]W and let
q_t^{i,j,h} be the corresponding coefficient of the monic profile on
the right of (8). Its leading coefficient is one, so (8) is exactly the
following five coefficient equations, with no missing sixth equation:

    f_t^{i,j,h}=c_t-L q_t^{i,j,h}=0,       t=0,1,2,3,4.   (9)

For each of the twenty-one triples the captured exact source constructs
five polynomials b_t^{i,j,h} in QQ(s)[k,delta] satisfying

    sum_(t=0)^4 f_t^{i,j,h} b_t^{i,j,h}=1.                (10)

The source multiplies the five-generator row by its certificate column
and asserts equality to the actual constant matrix {{1}} in each case.
Every certificate is printed in full in the
[certificate artifact](../validation/2026-10-12-nonendpoint-GJ-zero-normalized-lead/twenty-one-polynomial-bezout-certificates.txt).
The final identities require no saturation or inverse parameter. They
are polynomial identities in k,delta, with only constant coefficients
in the number field QQ(s), and therefore remain true after embedding
that field into any algebraically closed characteristic-zero field.
Swapping the choice of s merely swaps j,h in the exhaustive list.

For example, the profile (i,j,h)=(0,0,5) has certificate

    (s/9+1/2, 2s/9+1, 4s/9+2, 2s/3+4, 2s/3+8).

The five symmetric exceptional profiles also have explicit polynomial
certificates, not solely unit Groebner-basis output. For (5,0,0) one is

    b0=-32k delta^2/9-26delta^2/9+44k/9+34delta/9+49/18,
    b1=-52delta^2/9+16k/3+8delta/3+37/9,
    b2=-8delta^2+8k/3+4delta/3+10/3,
    b3=-16delta^2/3+4/3,       b4=0.

Thus every one of (9)'s systems is impossible. This contradicts the
root factorization (8), proving that full support is impossible for
B!=0,G=J=0. Together with the previously proved B=0 case, it proves
the stated complete G=J=0 subfamily exclusion.


## Projective coverage and exact boundary directions

### 2. Complete projective source boundary

In the anticanonical coordinates, the reduced complement of Z5!=0 is
exactly

    ell={Z2=Z3=Z4=Z5=0}.

The chart Z5=1 is the complete A2(r,T) used by the owner. On ell with
Z1=1, put u=Z0. Its four projection sections are exactly

    (u-1,u-1+delta,u-1+3delta,u-1+4delta).

Their pulled quadric value is -3delta^2. Hence no finite u point maps
to C0, which lies on that quadric. These points are also never base
points, because the first two sections differ by the nonzero delta.

The unique omitted point of ell is

    P0=[1:0:0:0:0:0].

It is the intrinsic A4 point and belongs to c. At P0 the actual
sections are (1,1,1,1), so it is not a base point and maps to target
z=1. There is no further off-c source boundary above C0. In particular,
source r=infinity is this intrinsic point on c, while target z=infinity
comes from the affine c-point r=0. These two infinities cannot be
identified.

Consequently every off-c inverse point above C0 occurs in A2(r,T) with
T!=0. All subsequent affine equations retain the full off-c source
support once this boundary argument has been supplied.

### 3. Independent checks on the finite-fiber reduction

The exact equations and all rank alternatives are stated and proved in
[Complete actual target-fiber equations](#complete-actual-target-fiber-equations),
§§3–6. The independent projective-coverage audit verifies the same
elimination without dropping the quadratic term in X0 or assuming generic
linear rank. For finite z, p=1-z, the target is
lambda*(1,z,z^3,z^4), lambda!=0. The triangular combinations defining
F1,F2,F3 are invertible after X0 is specified. Hence F1=F2=F3=0
and X0=lambda are the *actual* fiber equations; a reconstructed
lambda=0 would be a base point, excluded by center avoidance.

The audit separately checked the coefficient [r^3]C3=p*A^2, which was
not established by the original identity checker. This retains the A=0
degree-drop locus. A projective resultant of A2 and C3 cannot treat a
common homogeneous root at infinity as an affine off-c inverse point.
The reduction remains restricted to pZ!=0; Z=0 is controlled by the
denominator-free equations. The independent rank-one check covers the
primitive cube roots z^2+z+1=0 and the allowable doubled T=0 fiber,
exactly as in [the complete rank-one analysis](#6-all-rank-one-compatible-fibers-for-p0).

### 4. Independent checks at z=1 and target infinity

The complete equations, the J=0 specialization, and the Delta1
resultant are in [the z=1 proof](#7-the-intrinsic-a4-target-z1-ie-p0).
The independent check confirms that P1,Q1 have fixed leading
coefficients J,3J when J!=0, so no projective degree-drop root is
mistaken for an affine point. In particular Delta1!=0 merely avoids
this obstruction; it is **not** a sufficient full-support condition.
The J=0 branch is handled directly by D0=delta^2/2+B, and is not
obtained by specializing the J!=0 resultant.

At target infinity the full calculation and B=0 alternatives are in
[the endpoint-fiber proof](#8-the-target-endpoint-zinfinity). The
independent check adds the explicit projective tests

    Qinf(0)=-delta^2*B,
    Pinf(-B/delta)=-B^3/delta,
    [r^2]Pinf=-delta^2.

For B!=0 these exclude respectively r=0, a denominator-zero root,
and a spurious common projective root at infinity even if Qinf drops
degree. For B=0 the independent factorization is

    Pinf=delta^2*r*(a-r),
    Qinf=r*((3delta^2+G)*r-delta^3).

It recovers the separate r=0 branch and the condition
a!=0 and [G=0 or (3delta^2+G)*a=delta^3] without dividing by B.
The independent boundary proof in §2 above excludes additional source
points outside the affine chart; no claim is made without center
avoidance. These checks are retained as distinct verification of the
primary proof, not as a second statement of its full derivation.


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_session_nonendpoint_conductor_infinity_coefficient_2026_10_12.py](../computations/verify_session_nonendpoint_conductor_infinity_coefficient_2026_10_12.py), [verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2](../computations/verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2), [verify_fraction_certificates.py](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/verify_fraction_certificates.py), [verify_session_nonendpoint_target_fibers_2026_10_12.m2](../computations/verify_session_nonendpoint_target_fibers_2026_10_12.m2), [verify_proof_gaps.m2](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/verify_proof_gaps.m2). No inherited computation was rerun for this consolidation.

The characteristic and admissibility restrictions are those in [Characteristic scope shared by the nonendpoint exclusions](#characteristic-scope-shared-by-the-nonendpoint-exclusions); the independent calculations and exceptional cases above remain part of this proof.




## Consolidated historical supplement: `research/supplements/NONENDPOINT_CUBIC_CONTACT_AND_FAMILIES.md`

Original mathematical content and its qualifications are retained verbatim. Relative links refer to the source's original supplement location.

# Nonendpoint conic-plus-quartic residuals: all eight families

The common nonendpoint hypotheses, the meaning of SUP, and the characteristic-zero restriction are fixed in [Mathematical organization and scope](#mathematical-organization-and-scope). The intrinsic pair is established in the [A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md), and the actual projection and boundary equations appear in [Complete actual target-fiber equations](#complete-actual-target-fiber-equations). The [residual divisor proof](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md) gives eight necessary 2+4 families. The two Type 1 branches and six Type 2/3 branches below are excluded by full curve ideals and actual higher jets. The separate [3+3 cubic-pair proof](#the-full-33-no-mate-theorem) owns the heptic classification and coefficient matching; it is not inferred from these conic-plus-quartic calculations.

<a id="3-nonendpoint-type1-two-family-exclusion"></a>
<a id="4-nonendpoint-type1-two-family-independent-audit"></a>

## Both Type 1 families

### 1. Inputs, retained parameters and the exact conditional setting

The missing z^2 coefficient in the conic plane section leaves exactly eight
necessary one-parameter families; the present audit covers the two branches
with contact pattern (1,3) at z=(1,-1).

Replace the owner's x by eta=2x-1, so eta^2=3, and retain arbitrary
delta!=0. Then

    u=(eta+1)delta^2/2,
    w=(u+4delta^2)/3,
    a=(u+w+delta-delta^2)/2,
    b=a-u, g=a-w, d=a-u-w, rho=delta/2.

No square-root branch is selected. Both algebraic branches are retained by
the coefficient algebra eta^2=3. No nonzero delta is omitted.

Admissibility means that the actual line center avoids S and the actual
projection is finite birational onto its integral quintic image X. The
accepted intrinsic pair and its projection formulas then give c->C0 an
isomorphism. A hypothetical mate of any positive degree forces the complete
reduced inverse support (SUP): (nu^-1 C0)_red=c, including absence of isolated
extra points. All geometric steps below are made under these hypotheses.
Inadmissible centers do not provide candidates and need not be classified.

### 2. The actual graph is a smooth rational quartic, even at the A4 point

Let j=(3u+w)delta-3delta^3=(5/3)eta delta^3. It is nonzero on the full
parameter domain. The literal residual polynomial factors into r-rho and
a graph component with

    t=[3delta^2 r^2-(p2-3delta^2 rho)r+2a delta^3]/j,
    p2=-uw+(3a+3u)delta^2+3delta^3,
    T=r^2+t=N4(r)/j.

The quadratic leading coefficient of t is 3delta^2/j, always nonzero.
The intrinsic coordinate restrictions therefore span 1,r,r^2,r^3,r^4:
the cubic coordinate -rt has nonzero cubic leading coefficient, and the
quartic coordinate v-rt, with v=t^2-r^3, has nonzero quartic leading
coefficient. Their projective closure is the degree-four rational normal
curve D4. It is smooth at infinity even though that point p is singular on
the ambient surface S. The nonzero cubic and quartic coefficients do not
depend on the leading coefficient of T, so a degree drop of T changes
neither the smoothness nor this argument.

The upstream map-degree argument gives a birational map to the integral
Q-curve R4 of class (3,1). Such an integral Q-curve has arithmetic genus
zero and is smooth. The finite birational curve map D4->R4 is consequently
an isomorphism. No source singularity or hidden multiplicity is inserted
by using this curve isomorphism.

### 3. Intrinsic length four and target length ten

On the finite A2 chart, I_c|D4=(T). At infinity the accepted A4 chart has
alpha=rt/v, beta=t/v, chi=r^2/v, and the actual curve ideal is generated by

    beta+chi=T/v,
    (1-alpha)chi-alpha^2=-r^3 T/v^2.

The second generator divided by the first equals -r^3/v, regular and
vanishing at infinity because v has pole four. Thus T/v generates the
restricted ideal at p. The independent identity N4'(rho)=-2delta^4 proves
T is nonzero. If deg T=m, its finite zero length is m and the infinity
length is 4-m. This proves

    length O_D4/(I_c|D4)=4

for every retained delta, including every repeated zero and every degree
drop. It is an exact ideal calculation on the smooth source curve.

Meanwhile C0.R4=(1,3).(3,1)=10. Via the curve isomorphism, the actual target
Cartier equation has zero divisor of degree ten on D4. Under (SUP), every
such zero lies on c. Its pullback ideal is contained in I_c|D4, so each
local target length is at least the intrinsic length. The total difference
would have to be six.

### 4. Every possible place of excess is retained

The corrected [conormal reduction](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#1-nonendpoint-conormal-cubic-reduction),
and reconstructed its P,J from the unexpanded quotient-differentiation
expressions using the actual four T derivatives. At each finite point of
c, including r=0 in the opposite frame, a nonzero P or J gives cotangent
surjectivity. Under (SUP), the fiber has one point and equal residue field.
The finite local algebra lemma in the
[all-mate conormal/conductor audit](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit),
then gives equality of local surface rings. Such points contribute exactly
zero excess; this is stronger than a first-normal estimate.

At p, the full singular cotangent determinant is -3delta^3 Jbar, and

    Jbar=d-2g+2b-a=w-3u=-(4/3)eta delta^2 !=0.

Thus the same local-isomorphism conclusion holds at p, with its full
three-dimensional cotangent space. No excess is available there.

Every possible finite excess point is therefore a common zero of P,J,N4.
The independently reconstructed exact ideal equality in
QQ[eta,delta,r]/(eta^2-3), saturated only by the known nonzero delta, is

    (P,J,N4):delta^infinity
      = (r-rho,eta delta+1) intersect (K,L r-N),
    K=5delta^3+9eta delta^2+45delta+9eta,
    L=2(eta delta+3), N=delta[(eta+2)delta+3].

This is the complete finite incidence, not a generic resultant test. The
checks additionally give

    K(-1/eta)=-32eta/9 !=0,
    K(-3/eta)=-24eta !=0,
    (L r-N)|r=rho=-2delta^2 !=0.

Hence the two parameter strata are disjoint; L cannot vanish on K=0;
sigma=N/L differs from rho. The classical discriminant of K is -746496.
For each fixed eta,delta there is at most one possible excess point: rho
on eta delta+1=0 or sigma on K=0. This exhausts all finite contact points,
including parameter specializations and source intersection multiplicities.

### 5. Direct actual jets bound the sole possible excess

The independent checker evaluates the actual Xi(r,T) on the graph, using
the local curve parameter e=r-r0. It does not copy the owner's cleared
Zi expressions or use first symbols to bound later contact.

For the linear stratum r0=rho, it uses the full coefficient algebra
eta^2=3, eta delta+1=0. For the cubic stratum r0=N/L, it uses the full
coefficient algebra eta^2=3,K=0, with inverses of j and L adjoined.
These are genuine nonzero algebras; the already proved denominator units
mean adjoining the inverses loses no parameter point or branch.

In both algebras the checks prove Xi lie on Q, T(r0)=0, X0(r0) is a unit,
and for the actual contact numerator

    f=X0^2 X2-X1^3

the constant and linear coefficients are zero while the quadratic
coefficient is a unit. In the linear stratum the independently evaluated
unscaled coefficient is exactly -eta/19440. In the cubic stratum its full
coefficient-algebra ideal equals the unit ideal. Since X0 is a unit,
division by X0^3 does not alter the order. The actual target Cartier
contact length is therefore exactly two at every point of both complete
strata.

The intrinsic length at this point is at least one; thus the sole possible
excess is at most one. All other points, including p, give zero excess.
This contradicts the required six. Both Type 1 branches have no mate in
any positive degree.


<a id="5-nonendpoint-type23-six-family-exclusion"></a>
<a id="6-nonendpoint-type23-six-family-independent-audit"></a>

## All six Type 2 and Type 3 families

### 1. Exact scope and independent algebraic branch coordinates

Work over an algebraically closed field of characteristic zero, on the
accepted degree-five A4 normalization pair (S,c) with c mapping isomorphically
to C0. Retain every nonzero delta. Under an admissible normalization projection
and a hypothetical mate in any degree, full inverse support (SUP) holds:
the reduced inverse image of C0 is exactly c, without isolated extra points.

The present families have u=x delta^2, w=3u, b=a-u, g=a-3u, d=a-4u.

The independent checker uses different algebraic coordinates from the owner:

    Type 2: epsilon^2=3, x=(epsilon+3)/6, tau=1/2,
            a=2u+(delta-delta^2)/2.
    Type 3: theta^2=3, zeta^2=6,
            tau=(theta+3)/6, x=(theta+zeta+3)/6,
            a=(6tau-1)u+tau delta-(3tau-2/3)delta^2.

For Type 2 this is equivalent to 6x^2-6x+1=0. For Type 3 the substitution
is equivalent to 6tau^2-6tau+1=0 and
3x^2-6tau x-1+3tau=0: the latter says (x-tau)^2=1/6.
Thus the reduced coefficient algebras retain all two or four branches over
an algebraically closed field; no numerical square root or selected root is
used. The tau inverse is exactly 2 for Type 2 and 6(1-tau) for Type 3.

The graph denominator is

    j=3(2x-1)delta^3.

In the independent coordinates it equals epsilon delta^3 for Type 2 and
(theta+zeta)delta^3 for Type 3. Epsilon^2=3, while
(theta+zeta)(theta-zeta)=-3. Thus j has no root for delta!=0 in any branch.
Adjoining its inverse in the checker loses no candidate, and center
avoidance is never assumed generically in place of checking an exceptional
parameter: the argument applies to any admissible center with these values.

### 2. Source curve, intrinsic contact and target contact

The actual factor reconstruction gives D=D2+D4, where

    t=(3delta^2 r^2+M r+N)/j,
    M=-(p2-3delta^2 rho), rho=tau delta,
    p2=-3u^2+(3a+3u)delta^2+3delta^3,
    N=(a/tau)delta^3,
    T=[(j+3delta^2)r^2+Mr+N]/j.

Its nonzero t quadratic coefficient makes D4 a smooth intrinsic rational
normal quartic, including its point p at infinity on the singular A4
surface. This statement is unaffected by a degree drop of T. Under (SUP),
the upstream map-degree proof gives D4 a finite birational map to the
smooth Q-curve R4 of class (3,1), hence a curve isomorphism.

At finite r the actual restricted curve ideal is (T). At p its accepted
A4 generators restrict to T/v and -r^3 T/v^2, where v=t^2-r^3 has pole four.
The ratio -r^3/v is regular and vanishes at p, so T/v generates there.
The checker proves degree T is always two or one, with all drop parameters
retained. Therefore finite intrinsic lengths total deg T, the infinity
length is 4-deg T, and total intrinsic length is exactly four.

The actual target intersection degree is C0.R4=(1,3).(3,1)=10. Under
(SUP), all ten local target lengths occur over c. The pullback of the
target ideal is contained in the reduced source ideal I_c; thus each
target length is at least its corresponding intrinsic length. The total
excess required is six. The next two sections prove the excess is at most
three without imposing a degree bound on the hypothetical mate.

### 3. Every possible finite excess and its actual higher jets

The actual P,J are reconstructed directly from the unexpanded conormal expressions and
the actual projection derivatives. Their cubic terms vanish on these six
families; their quadratic coefficients differ by 4delta^3. Hence they
cannot both vanish identically at any retained parameter, and have at most
two common finite points for a fixed parameter.

At a finite c point with P or J nonzero, the actual target cotangent map is
surjective, including r=0 in the reversed frame. Under (SUP) the fiber is a
single point with equal residue field. The finite local Nakayama argument
in the [conormal/conductor audit](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit)
makes the surface projection a local isomorphism. The actual reduced curve
ideals then agree, so such a point contributes zero excess. First symbols
are used here to prove a local ring equality, not to bound later contact.

All possible finite excess belongs to the complete incidence

    I=(P,J,N4):delta^infinity,
    N4=(j+3delta^2)r^2+Mr+N.

The independent Type 2 identity is

    I=(5(delta+epsilon)^2(delta+epsilon/5),
           4r-(epsilon+2)delta-1).

The scheme has length six across both branches, including the doubled
parameter component. For each fixed delta its support has at most one
point. The independent Type 3 parameter-only eliminated ideal is exactly

    (delta^2+(2theta+4zeta)delta/3+1),

equivalent to the owner's H3. The full source incidence has length twelve
across all four branches. The actual incidence, rather than just this
parameter polynomial, is retained throughout the finite jet check.

Both independent finite algebras are explicitly checked nonzero. Only
delta and the already proved j units are inverted. On the full incidence,
r=0 is absent and X0 at the point is a unit; therefore the finite target
chart covers every possible exceptional point, without losing an opposite
frame. The actual sections Xi are directly evaluated at r=r0+e and the
graph T(r). Their Q equation holds identically, and T(r0)=0. Write

    f(e)=X0(e)^2 X2(e)-X1(e)^3.

Its constant and linear coefficients are zero in both full incidence
algebras. In Type 2 the independent exact ideal equalities are

    ([e^2]f)=(delta+epsilon),
    ([e^2]f,[e^3]f)=(1).

The intrinsic first T coefficient together with [e^2]f also generates
the unit ideal. Thus on delta=-epsilon the target order is exactly three,
the intrinsic order exactly one, and the excess exactly two. At the other
retained value delta=-epsilon/5 the target order is exactly two and excess
at most one. The second coefficient is genuinely not a unit on the whole
Type 2 incidence; its degeneration is retained, including the nonreduced
parameter component.

For Type 3, [e^2]f is a unit on the entire incidence. The actual target
order is exactly two at every exceptional finite point, hence the excess
is at most one per point. The at-most-two common-root bound gives at most
two finite excess lengths. Because X0 is a unit, dividing f by X0^3 to
obtain the actual Cartier equation of C0 on Q does not change any order.

### 4. Infinity: actual third and fourth jets retain the degree drop

Put q=1/r and W=q^2 T. Independently homogenizing the actual affine
sections gives Fi=q^4 Xi(1/q,W/q^2), with

    F0=1-2W+W^2-qW+a q^2 W,
    F1=F0-delta q(1-W)+(b-a)q^2 W,
    F2=F0-3delta q(1-W)+3delta^2 q^2-delta^3 q^3+(g-a)q^2 W,
    F3=F0-4delta q(1-W)+6delta^2 q^2-4delta^3 q^3+delta^4 q^4
          +(d-a)q^2 W.

This uses actual sections, independently of the owner's j^2-scaled
expressions. The complete delta-open coefficient algebras are explicitly
checked nonzero. F0(0)=9delta^4/j^2 is a unit, and the Q equation holds.
Let f_inf=F0^2 F2-F1^3. Its first three coefficients, through q^2, vanish.
The independently reconstructed cubic coefficient identity is

    [q^3]f_inf=54delta^9(j+3delta^2)/j^4.

Outside j+3delta^2=0 this is nonzero. T has degree two, so intrinsic order
at p is two and actual target order is three: excess one.

The complete degree-drop ideal in the delta-open algebra is

    Type 2: (delta+epsilon),
    Type 3: (delta+zeta-theta).

These are exactly the owner's delta+6x-3 and delta+6x-12tau+3 relations.
On each complete ideal the middle numerator M is a unit; no constant or
zero T stratum exists. The independent actual fourth coefficient satisfies

    [q^4]f_inf=-2delta^3 M/j
          modulo (j+3delta^2),

and is a unit there. Thus T has degree one, intrinsic order at p is three,
and actual target order is four. The excess is again exactly one. These
third/fourth-jet identities cover every nonzero delta and all six algebraic
branches; the zero cotangent determinant at p is never turned into an
unsupported later-contact bound.
### 5. Contradiction, source bindings and preserved failures

For Type 2 the complete incidence gives at most one finite excess point,
with excess at most two. For Type 3 there are at most two finite excess
points, with excess at most one each. The infinity excess is always one.
Every other intersection is at a local-isomorphism point and gives zero
excess. Total excess is therefore at most three, contradicting the six
required by the exact intrinsic and target lengths. This proves no mate
in any degree on all six families. Combining this with the Type 1 proof above excludes all eight necessary 2+4 families and therefore the
entire 2+4 residual partition in this nonendpoint normalization family.


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_session_nonendpoint_cubic_contact_2026_10_12.m2](../computations/verify_session_nonendpoint_cubic_contact_2026_10_12.m2), [verify_session_sparse_heptic_cubic_pairs_2026_10_12.m2](../computations/verify_session_sparse_heptic_cubic_pairs_2026_10_12.m2), [probe_session_nonendpoint_2plus4_families_2026_10_12.m2](../computations/probe_session_nonendpoint_2plus4_families_2026_10_12.m2), [probe_session_nonendpoint_type1_contact_jets_2026_10_12.m2](../computations/probe_session_nonendpoint_type1_contact_jets_2026_10_12.m2), [probe_session_nonendpoint_type1_linear_contact_jets_2026_10_12.m2](../computations/probe_session_nonendpoint_type1_linear_contact_jets_2026_10_12.m2), [verify_type1.m2](../validation/2026-10-12-type1-two-family-independent-audit/verify_type1.m2), [probe_session_nonendpoint_type23_incidence_2026_10_12.m2](../computations/probe_session_nonendpoint_type23_incidence_2026_10_12.m2), [probe_session_nonendpoint_type23_full_contact_jets_2026_10_12.m2](../computations/probe_session_nonendpoint_type23_full_contact_jets_2026_10_12.m2), [probe_session_nonendpoint_type23_a4_contact_2026_10_12.m2](../computations/probe_session_nonendpoint_type23_a4_contact_2026_10_12.m2), [verify_type23.m2](../validation/2026-10-12-type23-six-family-independent-audit/verify_type23.m2). No inherited computation was rerun for this consolidation.

The characteristic and admissibility restrictions are those in [Characteristic scope shared by the nonendpoint exclusions](#characteristic-scope-shared-by-the-nonendpoint-exclusions); the independent calculations and exceptional cases above remain part of this proof.




## Consolidated historical supplement: `research/supplements/NONENDPOINT_CUBIC_PAIR_COMPLETION.md`

Original mathematical content and its qualifications are retained verbatim. Relative links refer to the source's original supplement location.

# Nonendpoint residual cubic pairs: complete contact and coefficient proof

The common nonendpoint hypotheses, the meaning of SUP, and the characteristic-zero restriction are fixed in [Mathematical organization and scope](#mathematical-organization-and-scope). The intrinsic pair is established in the [A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md), and the actual projection and boundary equations appear in [Complete actual target-fiber equations](#complete-actual-target-fiber-equations).

<a id="2026-10-13-session-nonendpoint-cubic-pair-full-independent-audit"></a>
<a id="2026-10-13-session-cubic-pair-theorem-scope-qualification"></a>
<a id="1-nonendpoint-cubic-pair-contact-reduction"></a>

## The full 3+3 no-mate theorem

### 1. Correct theorem, actual setting and retained exceptions

Work over an algebraically closed field of characteristic zero, for the fixed
C0 and the accepted degree-five A4 normalization pair. Retain delta!=0 and
every actual center avoiding the surface. The induced projection is finite
birational, and c maps isomorphically to C0. A hypothetical mate implies the
complete inverse-support condition SUP, including no isolated extra point.

Use B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a, so A=a+d-b-g=G+Jbar. The 3+3
partition lies on A=-3delta^2. The upstream
[residual audit](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#2-nonendpoint-residual-factor-and-genus-independent-audit),
SHA `db72f936486253cf91e82645de9c3b6b23562dac9da49eee6ee31f0cb94b5322`,
proves under SUP that every prime cubic is a smooth rational normal cubic
with equation t+m r+n=0, and maps isomorphically to a smooth Q-curve of class
(2,1). The pushforward cycle retains multiplicity; a doubled source cubic
is permitted. The line-cover and ruling-degree-drop alternatives are already
excluded in that upstream proof, rather than discarded by selecting a minor.

The precise conclusions accepted here are:

* If Jbar!=0, no such projection satisfies SUP, including distinct or doubled
  residual cubics.
* If Jbar=0, no such carrier has a mate, by the separate all-power obstruction;
  failure of SUP is not claimed.
* Thus the entire residual 3+3 lane has no mate in any degree.

### 2. Actual contact at infinity and the complete heptic

On a source cubic put T=r^2-mr-n. Its four actual coordinate sections are
cubic polynomials with leading coefficient -1, so their homogeneous values
at r=infinity are all nonzero. The smooth source and target cubic are
isomorphic; epsilon=1/r is therefore an actual smooth curve parameter there.
For the actual Q-chart equation eta-zeta^3 of C0, where
eta=X2/X0 and zeta=X1/X0, direct expansion gives first coefficient Jbar.
My fresh checker independently verifies that the numerator X0^2 X2-X1^3,
after homogenizing each Xi to epsilon^3 Xi, has first coefficient -Jbar.
Its denominator has constant value (-1)^3, giving the same Jbar. Hence
the contact is exactly one when Jbar!=0. No first-normal estimate of a
later contact order is used.

The primitive Segre factorization of the degree-three curve map is

    (X0,X1,X2,X3)=(L0 Q0,L0 Q1,L1 Q0,L1 Q1),

with homogeneous L_i of degree one and Q_i of degree two, both pairs
basepoint-free. Each factor is nonzero at infinity since all Xi are nonzero
there. Normalize L_i to have affine leading coefficient one and Q_i to have
leading coefficient -1. Then L1-L0=kappa is constant. It is nonzero: if it
vanished, the first Segre projection would be constant, whereas a smooth
(2,1) curve has that projection of degree one. Thus every division by
kappa in the owner's formulas is justified on the full admissible class,
without assuming a generic center minor.

Comparing X2-X0 gives kappa=a-g+3delta m-3delta^2 and

    Q0=(X2-X0)/kappa
       =-r^2-[3delta n+delta^3+(g-a)m]r/kappa-(g-a)n/kappa.

The actual divisor's r^2 coefficient condition gives
kappa(B-delta m)=3delta^2(m-delta). Together with X3-X1-X2+X0 this gives
the exact Q1-Q0 formula in the owner. The r^2 coefficient of X0 determines
L0=r-(m^2+m+a-q), hence all four factor formulas follow from the primitive
factorization and actual coordinate comparison.

The complete contact form is the binary heptic

    K=L1 Q0^3-L0 Q1^3.

The exact ambient identities, independently checked afresh, are

    X0^2 X2-X1^3=L0^2 K,
    X2^3-X1 X3^2=L1^2 K.

Consequently the extra ambient ruling factors are removed, and no common
root is lost because L0,L1 are coprime. This includes target X0=0 and all
other Segre-chart endpoints. The affine leading term of degree seven
cancels; its degree-six coefficient is
-kappa-3(B-delta m)=-Jbar. Thus K has exactly one binary zero at infinity
and six finite contact lengths.

Both ambient cubic restrictions are divisible by the actual polynomial T:
before restriction their expressions are divisible by the affine ideal
generator T of c. Substituting T(r) preserves that exact divisibility even
when T has a repeated root. The two coprime L_i then imply T divides K
with full multiplicity. Under SUP every finite root of K is a root of T;
the binary root at infinity is already accounted for. This is the precise
interpretation of the owner's affine-support statement.

The intrinsic restricted curve ideal has finite length two and infinity
length one. At infinity h=T/v belongs to the actual ideal of c and has
expansion -epsilon+O(epsilon^2), since v=t^2-r^3 has pole three. Hence the
intrinsic total length is three, whereas C0.(2,1)=7. The contact classification
below uses the entire target intersection divisor to control the four
excess lengths, rather than a bound from tangent data.

### 3. Complete homogeneous classification, including all endpoints

A (2,1) target curve has equation P2(U,V)W0+Q2(U,V)W1. Restricting to
C0, where the Segre coordinates are (1:z^3) and (1:z), gives the binary
heptic with possible affine exponents 0,1,3,4,6,7. The two missing
coefficients are z^2,z^5. This restriction is injective because these six
monomials are distinct. Coprimality of the two binary quadratics is exactly
the irreducibility filter: a shared homogeneous root yields a ruling
component, while coprime quadratics give a smooth graph over their first
coordinate line. A four-by-four homogeneous Sylvester resultant includes
the common root at infinity and every leading-degree drop.

For each finite source T-root r=delta u, the target root is represented by
u z1+(1-u)z0. This is defined at u=0 (target infinity) and u=1 (target zero),
and never vanishes at z=1. Distinct roots have profiles (1,5),(2,4),(3,3),
up to exchanging labels; repeated T must have the separate profile (6).

I constructed the binary coefficients afresh as finite binomial sums, not
by replaying the owner's expanded-polynomial coefficient extraction.
The resulting exact sparse ideals, saturated only by root distinction and
the binary resultant, equal

    15: (u-11v+5, 21v^2-21v+5),
    24: (u-42v^3+63v^2-42v+10,
             63v^4-126v^3+111v^2-48v+8),
    33: (u+v-1, 7v^4-14v^3+12v^2-5v+1).

All three are zero-dimensional, reduced, and disjoint from both the
saturated bad locus and u v(u-1)(v-1)=0. Thus zero and infinity are retained
before the exact ruling-factor filter, rather than omitted by a denominator.
The ordered counts are 2,4,4. The last identifies exchanged root labels,
leaving two contact quadratics. For type 24, h=s-1 separates the four
solutions: v=1/2+h/(21h^2+1), and its denominator cannot vanish on
63h^4-30h^2-1=0. Hence the list has exactly eight source T quadratics.

The repeated-root sparse ideal is exactly (u(u-1)); both surviving endpoints
have zero binary resultant, and saturation by that resultant is the unit
ideal. No irreducible cubic has a repeated-root T in this contact setting.
This excludes repeated roots of T only; it does not remove a repeated
cubic component of the residual divisor.

The independently verified invariant equations are

    15: h^2=12/7, p=8/21+h/2;
    24: 63h^4-30h^2-1=0, p=5/12+h/2-h^2/4;
    33: h=0, 7p^2-5p+1=0,

with s=1+h and p=uv. These necessary equations retain all algebraic branches.

### Actual coefficient matching closes the classification

The full primitive factor formulas, all coefficient equations and the six pair contradictions are proved below. They retain coincident factors and both signs of every algebraic branch. They contradict each possible pair on Jbar!=0. On Jbar=0 the separate entire-line all-power argument closes the no-mate theorem without asserting failure of SUP.

<a id="2-nonendpoint-cubic-contact-symbolics"></a>

## Actual primitive Segre factors and complete matching equations

### 1. Actual restriction and complete cubic-divisor equations

Consider a prime cubic with affine equation t+m r+n=0. Its normalization is
P1 with affine coordinate r. Put

    T_c=r^2-m r-n.

The four actual projected sections restrict to cubic polynomials f_i:

    f0=-r^3+(m^2+m+a)r^2+[n(2m+1)-a m]r+n^2-a n,
    f1=-r^3+(m^2+m-delta m+b)r^2
             +[n(2m+1-delta)-b m]r+n^2-b n,
    f2=-r^3+(m^2+m-3delta m+3delta^2+g)r^2
             +[n(2m+1-3delta)-delta^3-g m]r+n^2-g n,
    f3=-r^3+(m^2+m-4delta m+6delta^2+d)r^2
             +[n(2m+1-4delta)-4delta^3-d m]r+n^2-d n+delta^4.

Let

    A=a+d-b-g, Bprod=ad-bg,
    C=(4a-3b-g)delta-3delta^3-A,
    E=Bprod+delta^4,
    P2=Bprod+(6a-3b)delta^2+3delta^3,
    L=(-4a+b)delta^3-delta^4, N=a delta^4.

The exact restricted quadric is

    f0 f3-f1 f2=T_c F(r,-m r-n),
    F=A t^2+(C r+E)t+(-3delta^2-A)r^3+P2 r^2+L r+N.

For the 3+3 residual partition A=-3delta^2. The cubic divides F exactly if

    D2=-3delta^2 m^2-C m+P2=0,
    D1=-6delta^2 m n-C n-E m+L=0,
    D0=-3delta^2 n^2-E n+N=0.                         (1)

These are complete conditions for this factor. They do not divide by n,
m, a root difference, or a discriminant. The other factor is

    t+m' r+n', m'=C/A-m, n'=E/A-n.

Consequently the conditions retain the doubled cubic m'=m,n'=n.

### 2. Actual linear/quadratic factorization on the class (2,1) image

Assume the actual projected cubic is a basepoint-free image of class (2,1),
as required by the cycle and fiber arguments in the residual-factor note.
On the Segre quadric the matrix [[f0,f1],[f2,f3]] has rank one. A primitive
factorization therefore has the form

    (f0,f1,f2,f3)=(L0 Q0,L0 Q1,L1 Q0,L1 Q1),

where the L_i are homogeneous linear forms and the Q_i are homogeneous
quadratic forms. The two pairs have no common zero. Since every f_i has
leading coefficient -1, the affine factors can be normalized so that
both L_i have leading coefficient 1 and both Q_i have leading coefficient -1.
Thus L1-L0 is a constant. It must be nonzero: otherwise the first Segre
coordinate would be constant and the image would not have class (2,1).

Define

    B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a,
    kappa=a-g+3delta m-3delta^2.

The constant L1-L0 is exactly kappa, obtained by comparing the r^2 term
of f2-f0. In particular kappa!=0 on this class (2,1) locus. The factors are
explicit:

    Q0=-r^2+q r+w,
    q=-(3delta n+delta^3+(g-a)m)/kappa,
    w=-(g-a)n/kappa,
    D=Q1-Q0=(delta^2/kappa)[3(m-delta)r+delta^2+3n],
    u=m^2+m+a-q,
    L0=r-u, L1=r-u+kappa.                             (2)

These formulas come from Q0=(f2-f0)/kappa and
Q1=(f3-f1)/kappa, followed by the r^2 coefficient of f0=L0 Q0.
They are justified by the primitive factorization, rather than by an
unchecked division of a specialized polynomial.

The first equation of (1) gives the useful exact identity

    kappa(B-delta m)-3delta^2(m-delta)=D2.             (3)

Hence the linear coefficient of D is B-delta m on the actual divisor
locus. No conclusion is asserted for kappa=0 beyond its incompatibility
with the stated class (2,1) assumption.

### 3. Degree-seven contact and the exact quartic excess factor

The fixed curve C0 on the Segre quadric has equation

    L1 Q0^3-L0 Q1^3=0.

Pulling it back to this cubic gives the binary form of degree seven

    K=L1 Q0^3-L0 Q1^3
      =kappa Q0^3-L0 D(3Q0^2+3Q0 D+D^2).             (4)

The r^7 coefficient cancels. Its r^6 coefficient is

    -kappa-3(B-delta m)=-Jbar,                       (5)

since A=G+Jbar=-3delta^2. Therefore the contact at the parameter infinity
is exactly one whenever Jbar!=0. This is the actual full contact form,
not a bound obtained from a first conormal symbol.

There is scheme-theoretic division by T_c, including a repeated root.
The actual cubic equations of C0 pull back as

    f0^2 f2-f1^3=L0^2 K,
    f2^3-f1 f3^2=L1^2 K.

Before restriction they are multiples of the actual affine equation T of
c. Thus both displayed polynomials are divisible by T_c. Since
L1-L0=kappa!=0, gcd(L0,L1)=1, and the divisibility at each irreducible
factor of T_c forces T_c|K with its full multiplicity. Write

    K=T_c H.                                       (6)

On Jbar!=0 the polynomial H has degree exactly four and leading
coefficient -Jbar. Full inverse support forces every root of H to be a
root of T_c: the cubic intersects c only at the finite T_c roots and
the shared infinity point, while (5) already accounts for exactly the
single contact at infinity. All endpoints, including a root r=0 or
r=delta, are retained by the polynomial formulation.

If T_c has distinct roots alpha,beta, full inverse support therefore
requires

    K=-Jbar(r-alpha)^N(r-beta)^P,
    N+P=6, N>=1, P>=1.

If T_c=(r-alpha)^2, it requires

    K=-Jbar(r-alpha)^6, H=-Jbar(r-alpha)^4.

These are necessary contact profiles, not realizations or exclusions.

For a fully explicit coefficient division, write K=sum(k_i r^i,i=0..6).
The coefficients of H from r^4 through r^0 are

    h4=k6,
    h3=k5+m k6,
    h2=k4+m k5+(m^2+n)k6,
    h1=k3+m k4+(m^2+n)k5+(m^3+2mn)k6,
    h0=k2+m k3+(m^2+n)k4+(m^3+2mn)k5
                              +(m^4+3m^2 n+n^2)k6.

The supporting checker verifies this division with the two exact
remainder expressions; their vanishing on the actual class (2,1)
divisor follows from the preceding coprime-factor proof.

<a id="2026-10-13-session-nonendpoint-cubic-pair-coefficient-independent-subaudit"></a>

## Exact coefficient reconstruction and the six pair contradictions

### 2. Direct reconstruction from the actual residual polynomial

To avoid the distinct uses of B and J in older notes, use

    B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a,
    beta=ad-bg, A=G+Jbar.

Then

    b=a+B, g=a+3B+G, d=a+4B+2G+Jbar,
    beta=a*A-3B^2-B*G.

On the cubic-pair hyperplane `A=-3delta^2`, the actual F is

    F=-3delta^2*t^2+(C*r+E)*t+P2*r^2+L*r+N,
    C=(-6B-G)*delta-3delta^3+3delta^2,
    E=-3a*delta^2-3B^2-B*G+delta^4,
    P2=-3B^2-B*G-3B*delta^2+3delta^3,
    L=(-3a+B)*delta^3-delta^4,
    N=a*delta^4.

Let `S=s1+s2`, `Sprod=s1*s2`, `P=p1+p2`,
`Pprod=p1*p2`, `Cross=s1*p2+s2*p1`, and `x=B/delta^2`.
The product with the fixed leading coefficient expands as

    -3delta^2*(t+delta*s1*r-delta^2*p1)
               *(t+delta*s2*r-delta^2*p2)
      =-3delta^2*t^2-3delta^3*S*r*t+3delta^4*P*t
        -3delta^4*Sprod*r^2+3delta^5*Cross*r-3delta^6*Pprod.

The constant and rt comparisons give exactly

    a=-3delta^2*Pprod,
    G=3delta^2*(S-1)-6x*delta^2+3delta.

After these substitutions define the following polynomials, with no
inverse parameter in their definitions:

    Q2=delta*(Sprod+x^2-x*S)-x+1,
    Q0=delta*(x-Sprod+1/3-P+3Pprod)-1,
    Q1=delta*(x+9Pprod-3Cross)-1.

The full residual difference is the literal identity

    F-(-3delta^2*factor1*factor2)
       =3delta^3*Q2*r^2+3delta^3*(Q0+Q2)*t+delta^4*Q1*r.

This verifies all coefficients, including the absent r-cubed term.
Because `delta!=0`, factorization is equivalent to `Q2=Q0=Q1=0`
after the first two comparisons. Their subtraction gives the identity

    Q1-Q0=delta*(Sprod-3Cross+P+6Pprod-1/3).

Thus the owner's modulus-free PAIR equation is necessary:

    Epair=Sprod-3Cross+P+6Pprod-1/3=0.                 (PAIR)

The same three coefficient equations give both displayed expressions
for `1/delta` and the owner's r-squared relation. Only delta is divided
by. The reconstruction applies without change to identical factors.

The unused additional equation in the companion is also correct.
Set `zeta=x-Sprod+1/3-P+3Pprod`. Both

    x^2-x*(S-1)-x*zeta+3Pprod+1/3-P,
    x^2-x*S+(1-x)*zeta+Sprod

are identically

    x*(2/3-S+Sprod+P-3Pprod)+1/3-P+3Pprod.

This coefficient must be retained for sufficiency; PAIR alone is only
necessary. The exclusion below only needs that necessary equation to
fail. We impose no inverse on the coefficient of x in the extra equation.

The equivalent inverse-separation expression is zeta=1/delta with

    zeta=x+9Pprod-3Cross=x-Sprod+1/3-P+3Pprod.

Together with PAIR, the retained extra coefficient equation, the a,G formulas and delta!=0, these are complete matching conditions. The coefficient of x in the extra equation is never divided out.

### 3. The supplied root rows give the stated invariant equations

I reconstructed the `u,v` to `s,p,h` conversion directly, where
`s=u+v`, `p=u*v`, `h=s-1`.

For type 15, reduction by `21v^2-21v+5=0` with `u=11v-5` gives

    7h^2-12=0, p=s/2-5/42.

For type 24, reduction by
`63v^4-126v^3+111v^2-48v+8=0` with
`u=42v^3-63v^2+42v-10` gives

    63h^4-30h^2-1=0, p=5/12+h/2-h^2/4.

For type 33, `u=1-v` gives `s=1`; its supplied v quartic is
exactly `7p^2-5p+1=0` after substituting `p=v(1-v)`.

These are necessary consequences of the supplied rows, rather than a
claim here that the rows exhaust homogeneous contact profiles. Exhaustion,
endpoint treatment, ruling-factor removal and the geometric support
bridge belong to the parent's independent audit.

### 4. Complete six-pair contradictions, including diagonal pairs

For each type the polynomial PAIR is symmetric in the two cubics. The
three types therefore have exactly six unordered pairings. Direct
substitution produces the following identities, before using their field
equations.

| Pair | Exact expression for Epair |
| --- | --- |
| 15 / 15 | `2/147-h1*h2/2` |
| 15 / 24 | `(1-3h2^2-21h1*h2)/42` |
| 15 / 33 | `(2/7)*(q-1/3)` |
| 24 / 24 | `((1-3h1^2)*(1-3h2^2)-12h1*h2)/24` |
| 24 / 33 | `(3h1^2-1)*(1-3q)/6` |
| 33 / 33 | `(2/3)*(1-3p)*(1-3q)` |

For **15 / 15**, `h1*h2=12/7` or `-12/7`; Epair equals
`-124/147` or `128/147`. Both are nonzero.

For **15 / 33**, Epair zero would require `q=1/3`, but
`7q^2-5q+1` has value `1/9` there.

For **24 / 33**, put `e=h1^2`. The field polynomial
`63e^2-30e-1` has value `-4` at `e=1/3`, and the type-33
polynomial has value `1/9` at `q=1/3`. Neither factor can vanish.

For **33 / 33**, neither p nor q is `1/3`, by the same field
polynomial evaluation. The displayed product is nonzero.

For **15 / 24**, put `e=h2^2`. Epair zero gives
`1-3e=21h1*h2`; squaring and using `h1^2=12/7` yields
`9e^2-762e+1=0`. Subtract seven times this equation from
`63e^2-30e-1=0` to obtain `5304e-8=0`, so `e=1/663`.
The latter field polynomial has the nonzero value
`-459396/439569` there.

For **24 / 24**, put `ei=hi^2`. If e1,e2 are distinct roots of
`63e^2-30e-1`, their sum is `10/21` and product is `-1/63`.
Then `(1-3e1)*(1-3e2)=-4/7`. Equality to `12h1*h2`
would imply the false rational identity `16/49=-16/7` after
squaring. If `e1=e2=e`, the product `h1*h2` is e or -e.
In the first case Epair zero gives `9e^2-18e+1=0`;
comparison with the field polynomial gives `e=1/12`, where the
field polynomial is `-49/16`. In the second case Epair zero
gives `(3e+1)^2=0`; then `e=-1/3`, where the field
polynomial is 16. Every value is retained, including both signs of h.

No part of this reasoning divides by `h1-h2`, `e1-e2`, or a
cubic-factor difference. A repeated cubic is an explicit diagonal pair
within the 15 / 15, 24 / 24 or 33 / 33 case and is excluded.


<a id="2026-10-13-session-nonendpoint-homogeneous-gcd-rank-and-cover-independent-audit"></a>

## Full homogeneous gcd rank and parameter cover

### 1. Correct normalization and special zero cubics

Work over an algebraically closed field of characteristic zero, with
`delta != 0`. Put `z=r/delta`. The correctly scaled polynomials are

    P(delta*z)/delta^3 = (g-3b+2a)z^3
      + [6(b-a)+delta^2-3delta]z^2
      + [6a-3b+2delta]z - 2a,
    J(delta*z)/delta^3 = (2d-3g+b)z^3
      + [3(g-b)+5delta^2-3delta]z^2
      + [3b+delta-delta^2]z - b.

Write these degree-three homogenizations as `P,J` again. The coordinate
change is invertible, so it preserves homogeneous gcd degree, including
infinity and repeated roots. In particular the normalized coefficient
`2delta`, and the terms `delta^2-3delta` and `5delta^2-3delta`, must not
be replaced by their delta-one values.

The exact zero-polynomial strata are

    P=0: delta=-1, a=0, b=-2/3, g=-2, d arbitrary;
    J=0: delta= 1, b=0, g=-2/3, d=-1, a arbitrary.

For the first, the other cubic is

    J=(2d+16/3)z^3+4z^2-4z+2/3,

which is nonzero. For the second, it is

    P=(2a-2/3)z^3+(-6a-2)z^2+(6a+2)z-2a,

which is nonzero. These are the homogeneous-gcd-degree-three strata,
even when the nonzero affine polynomial has degree less than three.
The two cubics are never both identically zero.

An early message derivation by this auditor lost a delta factor during
scaling and consequently gave the wrong sign for the zero-P stratum.
Those substitutions were explicitly discarded. The formulas here are
checked directly against the literal original polynomials.

### 2. Exact homogeneous Bezout and syzygy criteria

Let

    P(u,v)=p0*u^3+p1*u^2*v+p2*u*v^2+p3*v^3,
    J(u,v)=j0*u^3+j1*u^2*v+j2*u*v^2+j3*v^3,
    wij=pi*jj-pj*ji, i<j.

The intrinsic cubic Bezout matrix is

    B = [ w01  w02       w03 ]
        [ w02  w03+w12   w13 ]
        [ w03  w13       w23 ].

It satisfies the literal identity

    P(u,v)J(s,t)-J(u,v)P(s,t)
      = (ut-vs)*(u^2,uv,v^2)*B*(s^2,st,t^2)^transpose.

If `h=degree(gcd_homogeneous(P,J))`, then

    rank(B)=3-h.

Here is a proof that also covers multiple roots and infinity. Factor
`P=H*A`, `J=H*C`, with `degree H=h` and coprime homogeneous residual
forms of degree `m=3-h`. The Bezout biform factors as the product
`H(u,v)H(s,t)` and the residual Bezout biform. Multiplication by H is
injective, so the coefficient matrix has the form `T*Bm*T^transpose`,
with T of full column rank. For `m>0`, change projective coordinates
so A has affine degree m. In `k[x]/(A)`, the residual Bezout biform
equals multiplication by the unit C times the divided difference of A.
The latter matrix is anti-triangular with nonzero antidiagonal, hence
invertible. Thus Bm is invertible and B has rank m. For `m=0`, the
biform is zero. If one cubic is zero, the other is the homogeneous
gcd and this last case applies.

Therefore `h>=2` is exactly the following six equations:

    w01*(w03+w12)-w02^2 = 0,
    w01*w13-w02*w03 = 0,
    w01*w23-w03^2 = 0,
    w02*w13-w03*(w03+w12) = 0,
    w02*w23-w03*w13 = 0,
    (w03+w12)*w23-w13^2 = 0.

These are all the two-by-two minors of the symmetric matrix. The
third and fourth coincide on the coefficient-pair locus, by the
Plucker identity `w01*w23-w02*w13+w03*w12=0`. Exact degree two also
requires `B != 0`; exact degree three requires `B=0`, equivalently all
six wij vanish. No affine-leading-coefficient nonvanishing is assumed.

The universal degree-one syzygy map has the five-by-four matrix

    S = [ p0  0   j0  0  ]
        [ p1  p0  j1  j0 ]
        [ p2  p1  j2  j1 ]
        [ p3  p2  j3  j2 ]
        [ 0   p3  0   j3 ].

UFD divisibility of the coprime residual pair gives

    dimension(kernel S)=max(h-1,0),
    rank(S)=4 if h<=1; 3 if h=2; 2 if h=3.

For h=2 the kernel is the unique scalar line generated by
`(J/H,-P/H)`. These are independent linear forms. Conversely independent
linear cofactors after dividing by a quadratic force h=2. The matrix S
is naturally five-by-four; the separate actual coefficient matrix in
section 3 is four-by-four and has a different purpose.

If `H=h0*u^2+h1*u*v+h2*v^2` and
`P=H*(l0*u+l1*v)`, `J=H*(m0*u+m1*v)`, then

    B=(l0*m1-l1*m0)*(h0,h1,h2)^transpose*(h0,h1,h2).

Consequently any nonzero column of a rank-one B recovers H projectively.
For example `P=uv^2,J=v^3` retains the double common root at infinity:
its Bezout matrix is diagonal with entries `(0,0,1)`.

### 3. Finite monic quadratic common factor

Let `H=z^2+v*z+w`, and write

    P=(A*z+B)*H, J=(C*z+D)*H.

The actual parameters are recovered without any additional division by
cofactor coefficients:

    a=-B*w/2, b=-D*w,
    g=A+3b-2a, d=(C+3g-b)/2.

The four remaining actual coefficient relations are exactly

    M*(A,B,C,D)^transpose
      = delta*(2,delta-3,1-delta,5delta-3)^transpose,

where

    M = [ w   v+3w    0   -3w  ]
        [ v   1-3w    0    6w  ]
        [ 0   0       w    v+3w]
        [-3  -3w      v    1+6w].

Direct expansion gives

    det(M)=(v^2-4w)*K,
    K=v^2+2w+6vw+6w^2.

Thus outside these two factors, M is invertible and gives the complete
unique coefficient pair for each `(delta,v,w)`. Exact gcd degree two
requires the additional open condition `A*D-B*C != 0`.

### 3a. The exceptional K locus has no solutions

If `K=0,w=0`, then `v=0`, and the first equation is `0=2delta`,
impossible. If `w!=0`, put `t=v/w` and `S=t^2+6t+6`. Then

    S != 0, w=-2/S, v=-2t/S.

The augmented four-by-four minor using columns `(A,C,D,rhs)` is

    -24*delta*(t+2)/S^2.

It is nonzero except `t=-2`. At that last value `H=(z-1)^2`.
The second coefficient equation is minus twice the first, requiring
`delta=-1`. The fourth is minus three times the first minus twice the
third, requiring `delta=-5/3`. These cannot hold simultaneously. Hence
the entire K locus is inconsistent, including its intersections with
the repeated-factor locus.

### 3b. Repeated finite common factor

For `H=(z-rho)^2`, so `v=-2rho,w=rho^2`, the case `rho=0` is already
impossible by the first equation, and `rho=1` is impossible by section 3a.
For `rho!=0,1`, M has rank three: its first three rows and columns have
minor `-3*rho^4*(rho-1)^2`. A left-kernel vector is

    (-(2rho+1),-rho*(rho+2),2rho,rho^2).

Its pairing with the actual right-hand side is

    2delta*[2delta*rho*(rho-1)+2rho-1].

Therefore the necessary and sufficient compatibility condition is

    2delta*rho*(rho-1)+2rho-1=0.

When this holds there is one free cofactor coefficient. Again retain
`A*D-B*C != 0` for exactly h=2. The requirement `delta!=0` also removes
`rho=1/2`; no additional unstated root condition is introduced.

### 4. Common quadratic containing infinity

A common factor with infinity once is `H=v*(u-rho*v)`. Then the
affine cubics have leading coefficients zero, so

    g=3b-2a, d=4b-3a.

The remaining common-root equations in a,b are

    [ -6rho^2+6rho-2   6rho^2-3rho   ] [a]
    [ -6rho^2         6rho^2+3rho-1 ] [b]

    = -delta*[ (delta-3)rho^2+2rho,
               (5delta-3)rho^2+(1-delta)rho ]^transpose.

The determinant is `2*T`, where `T=6rho^2-6rho+1`. For every rho,
including T=0, a particular solution is

    a0=delta*rho*(2delta*rho+1),
    b0=delta*rho*(2delta*rho-delta+1).

For `T!=0` this is the unique solution. For `T=0`, the coefficient
matrix has rank one and the compatibility is automatic. All solutions
are `(a,b)=(a0,b0)+eta*(m12,-m11)`, where m11,m12 are its first-row
entries. They cannot both vanish when T=0. Recover the linear
cofactors of P,J and retain their nonzero determinant for exactly h=2.

Double infinity would require both affine degrees at most one. After
the leading cubic coefficients vanish, the quadratic coefficients
differ by `4delta^2`, so they cannot both vanish. This case is impossible.

The finite monic cover, infinity-once cover, and impossible double
infinity case exhaust all projective quadratic factors, including
repeated factors. No actual projection admissibility is asserted.

### 5. Complete proportional locus, including the zero cubics

For `P!=0`, homogeneous gcd degree three is exactly `J=kappa*P` for
a scalar kappa. Comparing the literal corrected coefficients gives

    b=2kappa*a,
    6kappa^2*a=delta*(delta+2kappa-1),
    g=4kappa^2*a+(kappa-5)*delta^2/3+(1-kappa)*delta,
    d=(kappa+3)*g/2-3kappa^2*a,
    delta!=0.

These conditions are necessary and sufficient: after substituting b,g,d,
the literal difference is

    J-kappa*P = -[delta*(delta+2kappa-1)-6kappa^2*a]*z.

For `kappa!=0` this expresses a rationally in `(delta,kappa)`. For
`kappa=0` it gives `delta=1`, a free, and precisely the zero-J stratum.
The separate zero-P stratum in section 1 supplies the missing
projective-ratio chart. Thus no zero polynomial or proportional pair
is silently removed from the full h>=2 classification.


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_binary_contact.m2](../validation/2026-10-13-cubic-pair-full-independent-audit/verify_binary_contact.m2), [verify_session_cubic_pair_coefficient_subaudit_2026_10_13.m2](../computations/verify_session_cubic_pair_coefficient_subaudit_2026_10_13.m2), [verify_session_nonendpoint_homogeneous_gcd_rank_2026_10_13.m2](../computations/verify_session_nonendpoint_homogeneous_gcd_rank_2026_10_13.m2), [verify_session_nonendpoint_h2_cover_audit_2026_10_13.m2](../computations/verify_session_nonendpoint_h2_cover_audit_2026_10_13.m2). No inherited computation was rerun for this consolidation.

The characteristic and admissibility restrictions are those in [Characteristic scope shared by the nonendpoint exclusions](#characteristic-scope-shared-by-the-nonendpoint-exclusions); the independent calculations and exceptional cases above remain part of this proof.



