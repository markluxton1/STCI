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
2. **Carrier structure and normalization restrictions** ([structural proofs](quintic_conormal_and_factor_geometry.md#1-quintic-conormal-and-delpezzo-audit), [endpoint factor/contact proof](quintic_conormal_and_factor_geometry.md#2-quintic-endpoint-factor-independent-audit), and [low-pole spaces](quintic_conormal_and_factor_geometry.md#5-a4-low-pole-spaces)): necessary reductions, with their independent hypotheses and unresolved cases. These are not by themselves mate-existence results.
3. **Actual target fibers and inverse support** ([fiber equations](quintic_nonendpoint_support.md#complete-actual-target-fiber-equations), [the G=J=0 exclusion](quintic_nonendpoint_support.md#full-inverse-support-exclusion-when-gj0), and [projective boundary analysis](quintic_nonendpoint_support.md#projective-coverage-and-exact-boundary-directions)): source-chart coverage, denominator-free equations, exceptional fibers, and the limits of each exclusion.
4. **Residual-divisor exclusions** ([the eight 2+4 families](nonendpoint_cubic_contact.md#nonendpoint-conic-plus-quartic-residuals-all-eight-families) and [the 3+3 cubic-pair proof](nonendpoint_cubic_pairs.md#nonendpoint-residual-cubic-pairs-complete-contact-and-coefficient-proof)): conditional on the accepted residual classification and SUP, with actual jets, coefficient matching, and exceptional strata retained in full.

The historical proof texts below are arranged by mathematical dependency, not by date. Their equations, proof steps, explicit counterexamples, exceptional loci, and qualifications remain in place. The standalone certificate transcriptions are preserved as archival evidence; no archived computation is represented as rerun. The headings identifying their former supplement paths are retained as stable link destinations.

## Characteristic scope shared by the nonendpoint exclusions

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier).

The exact hypotheses and exceptions of each exclusion remain in its proof; this common restriction does not extend any theorem beyond its stated admissible nonendpoint family.

## 1. Exact source and conclusions

Use the accepted degree-five normal anticanonical surface in P5 and
the four projection sections parameterized by `(delta,a,B,G,J)` in
the [restricted-conductor note, §5](nonendpoint_conormal_and_conductor_modules.md#2-nonendpoint-restricted-conductor-determinant).
The [independent module audit, §§4–5](nonendpoint_conormal_and_conductor_modules.md#4-conductor-quadric-module-independent-audit)
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

The new [exact certificate](../../computations/quintic_conductor_cone_identity.py)
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
[incidence program](../../computations/quintic_conductor_singular_incidence.py)
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
[universal identity](#2-a-universal-identity-rather-than-a-parameter-sample) gives rank
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
The inherited [actual cotangent calculation](nonendpoint_conormal_and_conductor_modules.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit)
gives length one if J!=0. If J=0 and `G(G+3delta^2)!=0`, the
[local fiber and phase audit](nonendpoint_conormal_and_conductor_modules.md#7-jbar-zero-conductor-phase-independent-audit)
gives length two. The exceptions are the already excluded G=J=0
family and the already excluded entire-line family G=-3delta^2,J=0;
their exact all-mate exclusions are retained in the
[G=J=0 proof](quintic_nonendpoint_support.md#full-inverse-support-exclusion-when-gj0) and the [full-line conormal bound](nonendpoint_conormal_and_conductor_modules.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit).
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

The retained exact programs are the [cone identity](../../computations/quintic_conductor_cone_identity.py) and [rational conductor incidence](../../computations/quintic_conductor_singular_incidence.py). The vertex example and uniform contact certificates have been retired after their mathematical statements and exact parameters were preserved above; their historical implementations remain in Git history.

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

## Related proof developments

- [Quintic carrier conormal and factors](quintic_conormal_and_factor_geometry.md)
- [Nonendpoint target fibers and support](quintic_nonendpoint_support.md)
- [Nonendpoint cubic contact families](nonendpoint_cubic_contact.md)
- [Completion of nonendpoint cubic pairs](nonendpoint_cubic_pairs.md)
