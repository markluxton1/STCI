# Positive-normal algebraization excludes every smooth movement-two formal root

Date: 2026-10-15. Author: `formal_algebraization_route`.
Status: **NEW GEOMETRIC THEOREM; independent review requested**.
Accepted conormal, blowup, actual-CI bridge, and formal-root functor statements
are inputs. No accepted computation or proof was rerun. A distinct worker
reviewed the branch-normalization and ruled-surface intersection steps while
this note was written; a full independent audit is still required.

## 1. The result concerns all normal orders together

Let `C` be a smooth rational curve of degree `e>=4` in `P3` over an
algebraically closed field of characteristic zero. Assume its normal bundle
is balanced, so

    N_C=O_C(2e-1) tensor V,       dim V=2.

Put `B=Bl_C(P3)` and identify

    E=P1_base x P1_direction,
    O_E(-E)=O_E(-(2e-1),1).

**Theorem.** For every `r>=2`, a smooth root divisor

    Z in |O_E(2,r)|

does not extend to a compatible embedded effective Cartier divisor on all
the exceptional neighborhoods of `E` in the actual blowup `B`.

In particular, for the repository curve `C0`, this excludes an infinite
formal first-principal-ideal lift for every smooth movement-two relation,
independently of its first normal order. The quadratic case `(2,2)` is one
instance. This is not a proof that the first or second obstruction alone
is nonzero everywhere, nor an explicit bound on the finite order at which
lifting must fail.

The proof first algebraizes the formal surface **as a branch**. It retains
all other algebraic branches and all other exceptional intersection
components, and bounds the degree of the algebraic closure anyway. It does
not assume that a formal line bundle comes from `Pic(B)`.

## 2. A reusable numerical criterion

The same argument gives a criterion beyond movement degree two. Let `C`
have degree `e` and balanced normal bundle `O_C(lambda)^2`, and let
`Z in |O_E(epsilon,r)|` be smooth and connected, finite over `C` of degree
`r`. Define

    g=(epsilon-1)(r-1),
    nu=lambda*r-epsilon,
    h=e*r.

Assume

    nu>4g+5.                                             (1)

If an all-orders Cartier lift exists, then there is a positive integer
`d`, the degree of an integral surface in `P3`, such that

    d <= max_(a integer, a>=1) [2*a*h-nu*a^2],            (2)

and

    (d-1)(d-2) >= e*r*(r-1).                            (3)

Consequently, incompatibility of (2) and (3) excludes the entire formal
lifting problem without a calculation of its obstruction sections.
When `nu>=h`, the maximum in (2) is attained at `a=1`, so the upper bound
simplifies to `d<=2h-nu`.

For a balanced rational space curve, `lambda=2e-1`. Formula (1) then
becomes

    ((2e+3)-4epsilon)*r+3epsilon-9>0.

The criterion is sufficient; no assertion is made on parameters that fail
it. Singular, nonreduced, or disconnected roots require separate arguments.

## 3. The compatible Cartier ideal defines a smooth formal surface

Write `E_m=V(I_E^(m+1))`. The exact functor used here is the one in the
[uniform formal-root tower note](2026-10-15-generalization-uniform-root-tower-finite-determinacy.md):
compatible invertible embedded ideals `I_m subset O_(E_m)` restricting to
`I_(Z/E)`. Their local equations glue using the full equation units. Their
inverse limit is an effective Cartier divisor `Vhat` on the completion of
`B` along `E`, with reduction exactly `Z`.

Locally at a point of `Z`, let `u` cut out `E` and let `g` be a local formal
equation of `Vhat`. The reduction `g mod u` cuts out the smooth Cartier curve
`Z` in the smooth surface `E`. Its differential on `E` is nonzero. Hence
the formal surface `Vhat` is regular along its whole reduced scheme of
definition `Z`; `u` cuts out `Z` as a reduced Cartier divisor on `Vhat`.
The exceptional-adic topology on `Vhat` is exactly this `Z`-adic topology.

It follows that

    N_(Z/Vhat)=O_Z(E)=O_Z(lambda,-1),
    deg N_(Z/Vhat)=lambda*r-epsilon=nu.                 (4)

The first quantity in (1) is positive, so (4) is ample. This step only
uses the embedded Cartier ideal and smoothness of the full root divisor;
no choice of a global defining function is made.

## 4. Algebraize the branch and preserve it under normalization

The formal algebraicity theorem of Andreotti--Hartshorne, in the explicit
form [Bost, *Algebraic leaves of algebraic foliations over number fields*,
Theorem 3.5 and Corollary 3.8, pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf),
applies to the smooth proper formal surface `Vhat` with ample normal line
(4). Its Zariski closure is an integral algebraic surface `W subset B`, and
`Vhat` is a branch of `W` along `Z`. This conclusion permits other branches;
it does not identify the entire formal completion of `W` with `Vhat`.

For clarity, the branch does give a smooth algebraic neighborhood after
normalizing. At a closed point `z in Z`, the completion of `O_(W,z)` has
the regular two-dimensional quotient given by the chosen smooth formal
branch. It is a minimal branch: both the algebraic surface and the formal
surface have dimension two. Algebraic local rings here are excellent, so
their finite normalization commutes with completion, decomposing into the
normalizations of the completed branches. The selected regular branch is
already normal. It is therefore one of the completed local factors of
the normalization `Wnu`, and the corresponding point of `Wnu` is regular.

These factors are selected compatibly by the globally given formal
branch. They glue to a curve `Znu subset Wnu` mapping isomorphically to
`Z`; its completed surface neighborhood is `Vhat`. This is the same
normalization/completion argument explicitly used by Bost immediately
before Theorem 3.5, p. 186. The local decomposition is also detailed in
[Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C27).

Take a projective resolution `T->Wnu` which is an isomorphism on the
regular neighborhood of `Znu`. We henceforth write `Z` for its unchanged
lift to the smooth projective surface `T`. Then

    Z^2=nu,
    genus(Z)=g.                                         (5)

The image `S` of `W` under `B->P3` is an integral surface. Indeed `W` is
not contained in `E`, since its formal branch has nonzero exceptional
parameter `u`. The blowup is an isomorphism off `E`, so `W->S` is birational.
Let `H` be the pullback of the hyperplane bundle to `T`, and let `d=deg S`.
It is nef and satisfies

    H^2=d>0,
    H.Z=e*r=h.                                          (6)

The latter equality uses the actual degree-`r` map `Z->C` and the degree
`e` hyperplane bundle on `C`. Other branches or conductor components do
not alter (5) or (6).

## 5. High self-intersection forces a ruled-surface degree bound

By (1) and (5), [Hartshorne, *Curves with high self-intersection on algebraic
surfaces*, Theorem 4.1, p. 122](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf)
makes the embedding `Z subset T` equivalent to a section `Z0` of a
geometrically ruled surface `R->Z`. The word "equivalent" has a precise
definition in Section 0, p. 111: the birational map is an isomorphism on
an open neighborhood of the curve. Thus

    Z0^2=nu.

In particular, this is stronger than an arbitrary birationally ruled
classification. Elementary transformations at the curve would change
the calculation and are not being used.

Resolve the graph of this equivalence:

    T <-q- U -p-> R.

Both birational morphisms can be resolved with centers outside the
respective curve neighborhoods. Let `L=q^*H` and `D=p_*L`. Then `L` is nef,
`L^2=d`, and

    D.Z0=L.Z=h.                                         (7)

The exceptional subspace for `p` is negative definite and perpendicular
to pullbacks, so

    d=L^2<=D^2.                                         (8)

For example, in the orthogonal basis of total exceptional transforms,
`L=p^*D-sum b_i E_i` gives `L^2=D^2-sum b_i^2`.
Moreover `D` is nef: for a curve `A` on `R`, its total transform `p^*A`
is effective, and `D.A=L.p^*A>=0`.

Numerically write

    D=a Z0+b f,

where `f` is a fiber. Nefness gives the integer `a=D.f>=0`. If `a=0`,
then `D^2=0`, contradicting (8) and `d>0`. Thus `a>=1`. From (7),

    a*nu+b=h,
    D^2=a^2*nu+2ab=2ah-nu*a^2.

Together with (8), this proves (2). It did not require full descent of the
formal divisor or its line bundle to `B`.

## 6. Plane sections give the opposing degree bound

Let `m` be the generic multiplicity of the integral surface `S` along
`C`. Its strict transform is `W`. The actual intersection divisor
`W|E` has fiber degree `m`. Since the chosen formal branch of `W`
contains `Z`, the effective divisor `W|E` contains `Z`; therefore

    m>=r.                                               (9)

This allows any residual exceptional components. In the balanced
coordinates, its class is `O_E(e*d-lambda*m,m)`, but no equality of that
class with the class of `Z` is needed.

A general plane meets `C` transversely in `e` distinct points of its
generic multiplicity-`m` locus. Its intersection with `S` is an integral
plane curve of degree `d`. At each of these points the plane curve has
multiplicity at least `m`, so its delta invariant is at least
`m(m-1)/2`. Its geometric genus is nonnegative, and its arithmetic genus
is `(d-1)(d-2)/2`. Consequently

    (d-1)(d-2) >= e*m*(m-1) >= e*r*(r-1),

which is (3). For the principal `(2,2)` case, merely four distinct
singular points already contradict degree at most four.

## 7. Apply the criterion to every smooth movement-two root

Take `epsilon=2`, `lambda=2e-1`, `e>=4`, and `r>=2`. Then

    g=r-1,
    nu=(2e-1)*r-2,
    h=e*r.

We have

    nu-(4g+5)=(2e-5)*r-3>0,
    nu-h=(e-1)*r-2>0.

Thus the maximum in (2) occurs at `a=1` and gives

    d<=2h-nu=r+2.                                      (10)

The genus bound (3) and (10) force

    r(r+1) >= e*r(r-1),
    r+1 >= e*(r-1).

But `e>=4` and `r>=2` give `e*(r-1)>r+1`. This contradiction proves the
theorem for every `r>=2` at once.

For `C0` and `r=2`, the numerical chain is

    genus(Z)=1,   Z^2=12,   H.Z=8,
    d<=16a-12a^2<=4,
    plane genus requires (d-1)(d-2)>=8.

There is no such integral surface, even allowing all additional
algebraic branches or exceptional components.

## 8. Finite towers and the boundary of the conclusion

The accepted uniform tower proves uniqueness and gives descending closed
schemes `K_m` on a fixed finite-type coefficient open. On its smooth
movement-two locus, the present theorem says that their stable geometric
support is empty. Combining these two results yields an existential
finite uniform cutoff on that smooth locus for each fixed `r`. It does
not supply a numerical cutoff or prove that `K_2` is empty.

In the accepted actual-CI-to-root bridge, an actual pair gives a Cartier
lift through exceptional order strictly below its first/second normal
relation gap. The new theorem, together with finite stabilization, bounds
that gap existentially on this smooth movement-two family. It does not
exclude every finite-gap actual pair, and it does not address singular
or nonreduced root divisors, unsaturated first relations, joint leading
base points, or other movement degrees automatically.

The universal STCI question and unrestricted `C0` problem remain open.
No commit, accepted verifier replay, or memory write was performed.
