# Positive-normal algebraization excludes every smooth movement-two formal root

Date: 2026-10-15. Author: `formal_algebraization_route`.
Status: **GEOMETRIC THEOREM; independently audited in characteristic zero**.
Accepted conormal, blowup, actual-CI bridge, and formal-root functor statements
are inputs. No accepted computation or proof was rerun. A distinct worker
reviewed the [branch-normalization and ruled-surface intersection steps](2026-10-15-formal-branch-ruled-model-degree-bound-review.md),
and the [full independent audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md)
passes Sections 1--8, including the general criterion and finite-stage/gap
consequences. Section 9 preserves an ineffective finite-jet attempt.
The [characteristic-scope addendum](2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md)
also passes the formal geometric theorem and finite smooth-root cutoff
in Section 10 over arbitrary algebraically closed fields, retaining the
explicit normal-bundle hypothesis and the actual-CI bridge boundary.

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
Here a smooth divisor in this ample class is connected, hence integral;
it has no fiber component and its map to `C` is finite of degree `r`.

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
be a smooth rational curve as above, of degree `e` with balanced normal
bundle `O_C(lambda)^2`, and let
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

Whenever this condition and `(e-1)r>=epsilon` hold, (2)--(3) imply the
single quadratic constraint

    (e-1)r^2-(e+2epsilon-3)r
      -(epsilon-1)(epsilon-2) <= 0.                     (3a)

Thus for fixed `epsilon` with `2e-1>4(epsilon-1)`, only finitely many
first normal orders can admit a smooth all-orders formal root: the
two auxiliary conditions hold for all sufficiently large `r`, while
the positive quadratic term in (3a) eventually forbids lifting. This is
a structural bound in `r`, rather than a list of root-degree profiles.

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

Bost's geometric formal algebraicity theorem, derived there from
Hartshorne's formal-function theorem, in [*Algebraic leaves of algebraic
foliations over number fields*,
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
local normalization/completion mechanism explicitly used by Bost
immediately before Theorem 3.5, p. 186. Whole-curve gluing here follows
from uniqueness: each integral element of the finite normalization must
map to its unique element in the fraction field of the normal branch,
so the local maps agree on every overlap. Reduction of this formal map
modulo the ideal of definition gives the algebraic curve `Znu`.
The local decomposition is also detailed in
[Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C2E).

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
plane curve of degree `d`, by Bertini irreducibility in characteristic zero.
At each of these points the plane curve has
multiplicity at least `m`, so its delta invariant is at least
`m(m-1)/2`. Its geometric genus is nonnegative, and its arithmetic genus
is `(d-1)(d-2)/2`. Consequently

    (d-1)(d-2) >= e*m*(m-1) >= e*r*(r-1),

which is (3). For the principal `(2,2)` case, merely four distinct
singular points already contradict degree at most four.
Equivalently, blow up these plane points with their actual multiplicities
`m_i>=m`. Adjunction gives arithmetic genus
`[(d-1)(d-2)-sum m_i(m_i-1)]/2` for the integral strict transform, which
is nonnegative. This proves the same bound without a local singularity
classification.

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
that gap existentially on this smooth movement-two family. Precisely, if
the empty stage is `K_N`, a gap `s-r` supplies `K_(s-r-1)`, so

    s-r<=N, equivalently s<=r+N.

Equality supplies only stage `N-1` and is not excluded. The result does not
exclude every finite-gap actual pair, and it does not address singular
or nonreduced root divisors, unsaturated first relations, joint leading
base points, or other movement degrees automatically.

The universal STCI question and unrestricted `C0` problem remain open.
No commit, accepted verifier replay, or memory write was performed.

## 9. Failure shield for an attempted effective finite-jet bound

A Hilbert-section count on a finite primitive root multiple `V_k` may
produce an actual surface containing `V_k`. This alone does not supply
the smooth algebraic branch used in Sections 4--5. In local coordinates
`(t,u,g)` with `E=(u)`, `Z=(u,g)`, and

    V_k=(g,u^k),

the actual surface

    S_alpha,k=(g^alpha+u^k),       alpha,k>=2,

contains `V_k`. For example, take coprime `alpha,k` in characteristic zero.
This has an irreducible singular transverse plane-curve branch, rather
than the required regular branch with parameter `u`; its normalization
ramifies that parameter. Thus a high order of agreement of a multiple
equation with the primitive jet does not preserve `N_(Z/V)=O_Z(E)` on
normalization. The selected regular completed factor in Section 4 is
provided by a **full** smooth formal lift, not by this finite containment.

An effective numerical cutoff from this route would need an additional
argument forcing a simple root factor or actual smooth branch, or an
effective factorization theorem with the necessary global unit and line
bundle data. Neither is established here. The Hilbert count therefore
does not turn the existential finite cutoff into a claimed explicit one.

## 10. Characteristic scope: a separately recorded extension

**Extension independently audited.** The geometric theorem and
the numerical criterion in this note also apply over an algebraically
closed field of arbitrary characteristic, provided the smooth rational
curve has the stated balanced normal bundle and the full root divisor is
smooth. No conclusion about the normal-bundle splitting of the literal
repository curve in exceptional characteristics is inserted here.

The characteristic check is as follows.

- Bost's geometric Theorem 3.5 and Corollary 3.8 are stated over a field
  `k`, without a characteristic-zero restriction. Their hypotheses
  concern the smooth proper formal germ and positive normal bundle;
  none of the arithmetic hypotheses in earlier parts of that paper is
  imported.
- Hartshorne explicitly fixes an algebraically closed base field of
  arbitrary characteristic in Section 1, printed p. 112, of the cited
  paper. Theorem 4.1 is proved in that scope.
- Resolution of a projective normal surface, preserving its regular
  open locus, exists over a field in every characteristic. See
  [Stacks, Resolution of Surfaces, Section 54.1](https://stacks.math.columbia.edu/tag/0ADX).
  No resolution theorem for higher-dimensional varieties is needed.
- The plane-section step uses irreducibility, rather than a
  characteristic-zero Bertini theorem for an arbitrary linear system.
  [Stacks, Section 37.32](https://stacks.math.columbia.edu/tag/0G4C)
  proves geometric irreducibility of general hyperplane sections in
  arbitrary characteristic. Applying immersion Bertini to the nonempty
  smooth locus of the integral surface makes the section generically
  reduced. A plane hypersurface is Cohen--Macaulay; geometric
  irreducibility and generic reducedness therefore make it integral.
  General planes also meet the smooth embedded curve `C` transversely
  in `e` distinct points. Plane blowup adjunction then proves (3) in
  every characteristic.
- Excellence, finite normalization, its compatibility with completion,
  surface point-blowup intersection formulas, and the normal-bundle
  degree calculation use no characteristic-zero division. For a
  smooth rational embedded curve, balanced splitting has degree
  `2e-1` in every characteristic by the Euler and tangent sequences.

This extension concerns the formal geometric obstruction only. It does
not transfer characteristic-zero logarithmic conductor arguments or
other accepted characteristic-zero repository conclusions to positive
characteristic. The accepted finite embedded-Cartier tower also uses no
characteristic-zero operation, so its existential empty smooth-root stage
extends with the same explicit hypotheses.

The actual-CI bridge used in Section 8 is separately stated in
characteristic zero. A smooth root divisor can project inseparably in
positive characteristic, as in `v^p-t=0`; smoothness alone therefore does
not extend its generic separability step. The finite-gap bound in a
different characteristic is conditional on a valid actual bridge giving
the local ideal `(h,u^(s-r))`, with every other bridge hypothesis retained.
