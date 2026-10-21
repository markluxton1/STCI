# Conditional (2,12;6,16;2): quadric contact and a forced norm multiplier

Date: 2026-10-20. Author: `incidence_audit` worker.

Status: **new conditional proposal; sections 1--4 independently
reviewed PASS by the `surface_bound` worker; not promoted**.
This note concerns only an actual global pair with degrees `6,16`,
sole reduced support `C0`, FULL generic coprime ordinary initial CI
`(2,12)`, and ACTUAL saturated movement-two first relation. It does
not assert such a pair exists or that the structured incidence is
empty. No accepted computation is rerun, and no canonical record is
edited.

## 1. Inputs and notation

Use [R-0010](../results/saturated_first_relation_normal_flatness.md),
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md),
and the newly reviewed finite bridge in
[the singular-root note](2026-10-20-conditional-2-12-singular-gluing.md).
In particular, on the blowup `B=Bl_C0(P3)`, with exceptional divisor
`E`, the common order-two transforms of an actual pair have local
ideal `(p,t^10)` at each full root point. The root is reduced of
class `(2,2)`, integral or two distinct `(1,1)` components. The
characteristic is zero and the field is algebraically closed.

Let `Q=(q=0)`, where `q=x0*x3-x1*x2`, be the smooth quadric. Identify
its rulings so that `C0` has class `(1,3)` and the cubic map

    pi3:C0 -> P1_ruling,          z -> z^3

is the first ruling. In the accepted balanced coordinates the
quadric's first normal equation is

    q1=u+(1/2)zv.

For `f=a(z)u^2+b(z)uv+c(z)v^2`, write

    tau(z)=f(-z/2,1)=(z^2/4)a(z)-(z/2)b(z)+c(z).

This is the homogeneous degree-four restriction of the `(2,2)`
root equation to the quadric direction section of class `(1,1)`.
The sextic symbol is `alpha*f`, with `alpha` homogeneous of degree
eight on `C0`.

## 2. The quadric direction cannot be a root component

An actual supported pair cannot have `Q` as a component of `F6`.
Otherwise `G16|Q` is a nonzero effective Cartier divisor with sole
reduced support `C0`: `G` cannot contain `Q`, since the global pair
has no common hypersurface factor. Such a divisor would be `m*C0`,
whereas its class is `(16,16)` and `C0` has class `(1,3)`. No
integer `m` gives these two classes.

Consequently `tau` is not identically zero. Indeed if `tau=0`,
then the restriction `F6|Q` has order at least three on `C0`.
The remainder would have class

    (6,6)-3(1,3)=(3,-3),

which is not effective on the smooth quadric. Hence `F6|Q` would
vanish identically, forcing the already excluded quadric factor.

Thus an actual global pair satisfies the additional open condition

    q1 does not divide f,             tau != 0.

This removes a permitted reduced two-component spectral stratum.
Whether an earlier global lifting test already removes it is a
separate implication, not assumed here.

## 3. Residual divisors on Q and exact local contacts

The restrictions are

    div(F6|Q)=2C0+R,      R of class (4,0),
    div(G16|Q)=2C0+T,     T of class (14,10).

Both multiplicities along `C0` are exactly two, since their generic
symbols restrict to nonzero multiples of `tau`. The residual
divisor `R` is a sum of ruling fibers, with their actual positive
multiplicities. The divisors `R,T` have no common component and no
common point outside `C0`, by sole reduced support of the original
pair. In particular

    R.T=40.

The strict transform `Q'` is isomorphic to `Q`: blowing up a
Cartier divisor `C0` on the smooth quadric does not change that
surface. Under this isomorphism, `E|Q'=C0`, and restriction of the
common order-two transforms gives precisely the divisors `R,T`.

At a point of the full root meeting the quadric direction section,
restrict the actual transformed ideal `(p,t^10)` to `Q'`. Since
`tau` is nonzero, `(p,t)` on the smooth surface `Q'` has finite
colength, equal to the root/quadric-direction intersection
multiplicity `nu` there. The regular-sequence filtration gives

    length O_(Q',x)/(p,t^10)
      =10*length O_(Q',x)/(p,t)=10*nu.                    (1)

This does not require `p=0` to be smooth. Away from the full root,
the transformed ideal is the unit ideal near `E`, so there are no
other residual intersection points on `C0`.

Summing (1) gives exactly

    R.T=10*(Z . Q_direction)=10*4=40.                    (2)

Thus the elementary quadric degree budget saturates; it gives no
numerical contradiction. It also identifies all contacts and their
scheme lengths rather than treating a vertical exceptional curve
as a residual component downstairs.

## 4. A forced norm identity, including degenerate orbit strata

The local formula implies more than the total equality (2). Write
`R=sum m_y L_y` as a divisor of ruling fibers. Since `T.L_y=10`,
and `T` has no component `L_y`, restriction to that fiber gives

    10*m_y
       =sum_(x in C0 intersect L_y) i_x(R,T)
       =10*sum_(x in pi3^-1(y)) ord_x(tau).

Hence the actual divisors satisfy

    R=pi3_* div(tau).                                    (3)

On the affine quadric chart the equation of `C0` is `v=b-z^3`,
and `F6|Q=v^2 R4(b)`. Comparing its second symbol with `alpha*f`
gives `alpha(z)*tau(z)=R4(z^3)`. Together with (3), this yields

    div(alpha)=pi3^* pi3_* div(tau)-div(tau).              (4)

Thus the actual degree-eight multiplier is uniquely determined
projectively by `tau`, including branch points and repeated roots.
If `zeta` is a primitive cube root of unity, an explicit formula is

    alpha(z) proportional to tau(zeta*z)*tau(zeta^2*z).    (5)

Formula (5) is a polynomial construction; there is no division by
`alpha` or by a function vanishing on `C0`. If
`tau=sum_(j=0)^4 t_j z^j`, the coefficient of `z^m` in the right
side is

    sum_(2j=m) t_j^2
      +sum_(j<k, j+k=m) e_(j,k)*t_j*t_k,

where `e_(j,k)=2` if `j=k mod 3`, and `e_(j,k)=-1` otherwise.
So the same map is defined over QQ without adjoining `zeta`.
Its homogeneous version is nowhere zero for every nonzero `tau`.

Explicitly the coefficient vector is

    A0=t0^2,
    A1=-t0*t1,
    A2=t1^2-t0*t2,
    A3=2*t0*t3-t1*t2,
    A4=t2^2-t0*t4-t1*t3,
    A5=2*t1*t4-t2*t3,
    A6=t3^2-t2*t4,
    A7=-t3*t4,
    A8=t4^2,

where

    t0=c0,
    t1=c1-b0/2,
    t2=c2-b1/2+a0/4,
    t3=-b2/2+a1/4,
    t4=a2/4.

One may impose `alpha_i*A_j-alpha_j*A_i=0` for all `i<j`, with
`alpha!=0` and `tau!=0`, or eliminate the projective multiplier by
substituting `[alpha_0:...:alpha_8]=[A0:...:A8]`. The latter makes
the eleven global-symbol equations homogeneous cubics in the nine
coefficients of `f`; it does not alter the actual root coordinates
or erase any norm ramification stratum.

All ramification multiplicities are retained in this argument.
At zero or infinity the map `pi3` has ramification index three:
if `tau` has order `m` there, its norm divisor has order `m`, its
pulled-back norm has order `3m`, and (4) gives order `2m` for
`alpha`. In an unramified orbit, with orders `m_0,m_1,m_2` for
`tau`, (4) gives orders `m_1+m_2,m_2+m_0,m_0+m_1` for `alpha`.
Thus repeated roots, collisions within an orbit and the two branch
fibers are covered without a genericity exception.

This supplies an exact additional necessary global-pair condition
on the low-order scheme: impose the projective equality in (5),
or substitute its quadratic coefficient vector for `alpha`, on
the open `tau!=0`. When the four roots of `tau` lie in distinct
unramified `pi3` fibers, the sextic symbol restriction on Q already
forces this multiplier. On collision and branch strata that
restriction can leave other choices; (3)-(5) retain the one forced
by the ACTUAL supported pair and its gap-ten contact ideal. No
claim that this condition is new on every component of the earlier
incidence is made.

As a consistency check, at the saved smooth seed

    tau=z^4/4+2z^2-8,

the coefficient vector in (5), multiplied by 16, is

    z^8-8z^6+96z^4+256z^2+1024,

the previously computed projective multiplier. This algebraic
identity does not make that already obstructed seed a survivor.

## 5. Surface singularity route: promising but incomplete

The strict sextic divisor has class `D=6H-2E`. A smooth member has
`c2=28`, `K^2=-4`, and `chi(O)=2`. Near a smooth root point where
`alpha|Z` has a simple zero, the actual equation has form

    A*p+t^10 B,         A|Z=alpha|Z.

At a simple zero on a smooth root this is an `A9` surface
singularity. Here `B` is automatically a unit: the second original
coefficient `beta` is nonzero at the zero of `alpha`, and the
invertible actual generator matrix forces its off-diagonal entry
`B` to be nonzero. There are sixteen zeros counted on the
degree-two cover `Z -> C0`. This suggests an exceptionally strong
vanishing-cycle obstruction on the normal isolated-singularity
locus. At a zero of multiplicity `m`, the special model
`(t+z^m)p+t^10` gives type `A_(10m-1)`.

These observations are **not a completed exclusion**. One must
handle nonnormal strict surfaces or singular curves, singular root
points and repeated zeros, and justify the precise
global vanishing-cycle bound. Irreducibility of a carrier is not
normality of its strict transform. The actual supported-pair
condition alone does not forbid singular curves outside `E` or
singular exceptional fibers. No Milnor-number argument in this
note discards those strata or claims that the conditional problem
is solved.

The proposed advance of this note is the exact contact identity and
forced multiplier (3)-(5), with independent review PASS. It can
reduce the structured incidence without starting an unstructured
search over global equations; whether the resulting incidence is
empty remains unresolved here.

## 6. Independent review of the norm argument

The separate `surface_bound` worker reconstructed sections 1--4
and reported **PASS**, including collision and branch multiplicities.
The review checked equality of the restricted actual ideal on
`Q'`, regularity from `tau!=0`, exclusion of a component of `T`
on each ruling fiber, the direct affine comparison
`F6|Q=v^2 R4(b)`, and the homogeneous/root-of-unity and QQ formulas.
This is recorded review of the new conditional lemma, not canonical
promotion or an emptiness certificate. The review also supplied
the automatic-unit observation for `B` incorporated in section 5.
