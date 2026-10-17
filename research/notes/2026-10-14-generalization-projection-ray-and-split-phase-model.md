# Projection rays, a global five-coordinate lead, and an exact split-phase shield

Date: 2026-10-14. Owner: `global_structure`. Status: **EXACT REFORMULATION
AND NEW LOCAL EXAMPLE; GLOBAL EXCLUSION OPEN**. Accepted classification
and conductor results are used without reruns.

## 1. The finite-dimensional projection spaces

The [Cartier-lift theorem](2026-10-14-generalization-cartier-lift-minimal-degree.md)
leaves three fixed-C0 models after accepted quartic exclusion:

    smooth quadric, H=(2,2), c=(1,1);
    quadric cone, H=2c, c smooth Cartier conic;
    plane, H=4h, c a line.

All have a primitive normalized section `Q in H0(S,H)` with divisor
`2c` or `4c`, respectively. The normal mate ray is precisely `Q^b`.
This is already a reduction of all mate degrees to one distinguished
section, but descent of its powers remains a global problem.

Fix the isomorphism of `c` with the literal C0 parametrization, and
write `W=span(s^4,s^3t,st^3,t^4)` in `H0(c,O(4))`. For a smooth
quadric, restriction

    H0(S,O(2,2)) -> H0(c,O(4))

is surjective and has kernel `H0(O(1,1))`, of dimension four. For
the plane with `H=4h`, its kernel is `ell H0(O(3))`, of dimension
ten, where `ell=0` is `c`. The same cone dimension is four, obtained
from its Cartier sequence. Once a splitting of restriction is fixed,
every four-coordinate subspace mapping isomorphically to `W` is the
graph of a linear map from `W` to this kernel. Thus the parameter
spaces before quotienting surface symmetries have affine dimensions
16 for either degree-eight model and 40 for the degree-sixteen model.

Four sections must have no base point. Since `H` is ample, their
resulting morphism is automatically finite: a positive-dimensional
fiber would have zero `H` degree. Birationality onto the image is an
additional condition. On that locus the model is the actual finite
normalization, and the image degrees are eight or sixteen.

The full support condition is exact and finite-dimensional: pull back
the actual generators of `I_C0` through the four sections and require
the radical of their sheaf ideal on `S` to be `I_c`. This retains every
extra isolated inverse point and every extra prime. It is not implied
by the fixed restriction to `c`.

## 2. Exact section-ring condition and what it does not bound

Let

    B=direct_sum_(b>=0) H0(S,bH),
    R=k[U0,U1,U2,U3] subset B,

where the four actual projection sections generate `R`. The carrier
is a hypersurface in P3, so its ambient degree-`b` forms supply all
sections of `O_X(b)`, by `H1(P3,O(b-a))=0`. Consequently

    a mate of degree b exists iff Q^b belongs to R_b.        (1)

When the projection is finite birational, `B` is a finite graded
module over `R` (it is the section module of the finite coherent
normalization algebra), and `Q` lies in the common fraction field.
The intermediate algebra `R[Q]` is finite birational. Thus (1) is an
actual power-membership condition in one finite ambient module,
equivalently the full conductor descent of one primitive ray.

The conductor theorem compresses single-field residual algebras.
Split residual products instead retain scalar root-of-unity phases.
Finite-dimensional parameter spaces or a finite normalization module
do not by themselves bound the orders of those phases. The exact
example below preserves full support and a smooth degree-one lift,
so these hypotheses cannot silently remove the phase problem.

## 3. An entire split-conductor affine example with unbounded phase order

Choose nonzero distinct `alpha,beta` in an algebraically closed
characteristic-zero field. Set `lambda=alpha+beta`, `mu=alpha beta`,

    B=k[u,v],
    y=v^2-lambda u v,
    h=y+mu u^2=(v-alpha u)(v-beta u),
    z=v h,
    A=k[u,y,z] subset B.

Put `R0=k[u,y]`. The equation `v^2-lambda u v-y=0` makes `B`
finite free of rank two over `R0`, and

    B=R0 direct_sum R0 v,
    A=R0 direct_sum h R0 v.

The latter is closed under multiplication because
`(hv)^2=yh^2+lambda u h(hv)`. Away from `h=0`, `v=z/h`, so the
extension `A subset B` is finite birational; normal `B` is its
normalization. The actual integral affine carrier is the hypersurface

    z^2-lambda u h z-y h^2=0,    h=y+mu u^2.                 (2)

Its conductor is exactly `hB`. To see this, an element `a+bv` belongs
to `A` exactly when `b in hR0`; requiring its product with `v` to
belong to `A` then forces `a+b lambda u in hR0`, hence `a in hR0`.
Thus the entire conductor square is

    A/hB=k[u],
    B/hB=k[u,v]/((v-alpha u)(v-beta u)),

with downstairs ideal `(h,z)` and upstairs divisor the two actual
lines `v=alpha u` and `v=beta u`. The upstairs curve is reducible,
with the two lines meeting at `(0,0)`; no nilpotent or intersection
data is dropped. Their maps to the downstairs line agree in the
coordinate `u`.

Let `C` downstairs be `y=z=0`. Its full reduced inverse image is
exactly the smooth line `c:v=0`, mapped isomorphically by `u`.
Indeed if `v!=0`, the first equation forces `v=lambda u`, and the
second then forces `mu u^2=0`, contradicting `mu!=0` and `v!=0`.
At `u=0` the only inverse point is still `v=0`; no isolated extra
normalization point appears.

For any fixed positive integer `q`, put `Q=v^q`. Modulo the entire
conductor its two restrictions are

    alpha^q u^q,   beta^q u^q.

Therefore the exact full-ring criterion is

    Q^n in A iff alpha^(q n)=beta^(q n).                      (3)

For sufficiency, if the two constants agree, the conductor residue
is the diagonal polynomial `alpha^(qn)u^(qn)` in `k[u]`; subtracting
it leaves an element of `hB subset A`. Necessity is immediate from
the two generic restrictions. Thus (3) includes the intersection
point and the entire conductor, not just a generic unit test.

Choose `alpha/beta` to be a root of unity of order `N`, with
`gcd(N,q)=1`. Then the smallest descending positive power is exactly
`n=N`, which is unbounded while the formulas (2) have fixed degrees
and the smooth singleton lift is unchanged. The primitive-like
orders `q=2` or four therefore do not bound split phases locally.

This is an affine example with a line support. It is **not** a
projective fixed-C0 carrier or a counterexample to any accepted
projective theorem. It proves that a proposed global argument must
use global projectivity, polarization or the actual fixed-C0
projection geometry in addition to these local support conditions.

## 4. Five-coordinate viewpoint: a concrete global lead

Adjoin `Q` to the four projection sections. Since the original four
generate `H`, the five also do, and their map has a finite image

    Y subset P4,  coordinates [U0:U1:U2:U3:Q].

Projection from the fifth-coordinate point is finite birational
`Y->X`. The hyperplane `Q=0` has scheme pullback `2c` or `4c`, and
the reduced curve there is the prescribed fixed C0.

For any scalar `zeta`, let `T_zeta` scale just the fifth coordinate.
At a split conductor identification where the `U_i` agree and the
two `Q` values have ratio `zeta`, the corresponding branch curves
are contained in `Y intersect T_zeta(Y)`. A mate requires these
phase ratios to be constant roots of unity and requires full
Artinian conductor membership as well.

This is a geometric reformulation, **not a proved exclusion**.
The shared hyperplane curve occurs for every `zeta`, so a naive
intersection-degree count must first separate that forced common
component from the additional branch curve. The local example above
shows why neither low coordinate degree nor isolated ramification
alone makes all `zeta` have bounded order. A useful new theorem
would have to couple the extra common curves to the actual
hyperplane multiplicity, global canonical/conductor divisor, or
prescribed C0 parametrization.

The separately written [transverse differential/socle theorem](2026-10-14-generalization-transverse-differential-socle-bound.md)
already supplies one global coupling: on a generically regular
carrier, every surviving projection requires a nonzero common-zero
divisor of the transverse differential, with bounded degree five
or six and a quantitative conductor-contact budget. Classifying
those root strata while preserving the split phase model is the
next structural target. No mate-power search has been started.
