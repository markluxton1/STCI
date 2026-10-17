# Intrinsic finite root families without a split normal bundle

Date: 2026-10-15; completed 2026-10-16. Author: `intrinsic_root_finite_family`.
Status: **NEW STRUCTURAL GENERALIZATION; targeted independent review passes**.
The [independent scope audit](2026-10-15-generalization-intrinsic-finite-root-family-independent-audit.md)
checks the relative cohomology and Cartier hypotheses, Hilbert-family
boundedness, splitting-free identities, numerical empty-stage criterion,
and strict conditional CI indexing.
The accepted embedded-Cartier tower, its cohomology/functor audits, and
the accepted intrinsic nef formal-branch theorem are premises. This note
proves the new relative cohomology and bounded-family input and the new
intersection identities. It replays no accepted computation or geometric
algebraization proof.

## 1. An intrinsic finite-family theorem

Work over an algebraically closed field `k` of characteristic zero.
Let `X` be a fixed smooth threefold, let `E subset X` be an effective
Cartier divisor, and write

    J=I_E/I_E^2=O_E(-E),
    E_m=V(I_E^(m+1)),                  E_0=E.

Let `S` be a finite-type `k`-scheme, allowed to be nonreduced. Assume

    q:mathcal Z -> S,
    mathcal Z subset E x S

is a proper smooth family of geometrically connected curves and a
relative effective Cartier divisor in `E x S`. The word relative means
that the divisor quotient is flat over `S`; properness is a condition
on `q`, and **does not require `S` to be proper**. Suppose every geometric
fiber has the fixed invariants

    genus(Z_s)=g,
    A=deg N_(Z_s/E)=Z_s^2_E,
    nu=deg O_E(E)|Z_s,

and assume

    nu>max(A,0).                                           (1)

Then there are canonical closed subschemes

    S=K_0 superset K_1 superset K_2 superset ...             (2)

such that `K_m` represents embedded effective Cartier ideals in
`E_m x T`, flat in their quotient over `T`, extending the specified
root ideal for every `T -> S`. Whenever such an ideal exists it is
unique. There is a vector bundle `V_m` on `S`, of rank

    rank(V_m)=g-1-A+m*nu,                                  (3)

whose canonical obstruction section on `K_(m-1)` has zero scheme `K_m`.
For some finite integer `N`,

    K_N=K_(N+1)=K_(N+2)=...                                (4)

as schemes. The stable scheme represents compatible formal embedded
Cartier ideals with the prescribed root, on the fixed actual formal
neighborhood of `E`. Its formation as a formal ideal functor includes
arbitrary parameter base changes. Each finite quotient is flat over
the parameter base; no infinite inverse-limit flatness assertion is
needed here.

The integer `N` depends on the fixed embedding and family. It is
existential, and the result supplies neither its value nor an explicit
order at which a single observed equality in (2) is already stable.
Nothing in the theorem asserts algebraization or emptiness of the
stable scheme. No splitting of a normal bundle, rational base curve,
product presentation of `E`, or chosen root equation is assumed.

## 2. The new relative vanishing and base-change proof

The actual relative correction line bundle is

    mathcal L_m
      =N_(mathcal Z/(E x S)) tensor J^m|mathcal Z,
                         m>=1.                            (5)

This definition includes all line factors from parameterizing the
divisor. In particular, a projective coefficient parameter space would
contribute its universal coefficient line through the relative normal
bundle; it must not be removed by choosing equations locally.
On every geometric fiber,

    deg L_(m,s)=A-m*nu<0.                                  (6)

A smooth geometrically connected curve is geometrically integral, so
a negative-degree line bundle has no nonzero section. Riemann--Roch
therefore gives, for every geometric `s`,

    H0(Z_s,L_(m,s))=0,
    h1(Z_s,L_(m,s))=g-1-A+m*nu.                            (7)

For clarity, the following strengthens (7) to the relative statement
required over nilpotent parameter directions. The morphism `q` is
proper, smooth, and of finite presentation; `mathcal L_m` is an
invertible sheaf flat over `S`. Proper flat perfect cohomology gives

    C_m=Rq_*mathcal L_m

as a perfect complex compatible with arbitrary derived base change.
One precise primary input is
[Stacks Project, Lemma 36.30.1, tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H),
applied with the invertible sheaf and `G=O_mathcal Z`.
Every derived geometric fiber of `C_m` has cohomology only in degree
one, by (7) and the fact that the fibers are curves. Locally, the
perfect-complex amplitude criterion therefore gives a
two-term vector-bundle representative

    [P^0 --d--> P^1]

in degrees zero and one. The reduction of `d` at every geometric
point is injective. A maximal minor is consequently a unit locally at
each point, making `d` a split inclusion over that neighborhood.
Its cokernel `V_m` is a vector bundle, including when `S` has nilpotents.
It follows that

    Rq_*mathcal L_m=V_m[-1],
    q_*mathcal L_m=0,
    R1 q_*mathcal L_m=V_m.                                 (8)

The rank is (3). Derived base change in (8), followed by local
freeness of `V_m`, gives the same statement for **every** `T -> S`,
including nonflat maps and nonreduced `T`. Thus uniqueness in the
family is not inferred from uniqueness at closed points or from a
bare constant-dimension assertion.

No claim that every negative-degree line bundle on an arbitrary
reducible or nonreduced curve has `H0=0` is being used. Smoothness and
geometric connectedness of the root fibers are essential to this
particular intrinsic numerical argument.

## 3. Why the accepted ideal tower now applies

The relative Cartier condition ensures that the root equation remains
regular after any `T -> S`. This is the universal base-change property
of a flat effective Cartier divisor; see
[Stacks Project, Section 31.19, tag 056P](https://stacks.math.columbia.edu/tag/056P).
For a local lift of the root equation to `E_m x T`, regularity on every
invertible graded ambient layer `J^i x T` makes the lift a
nonzerodivisor. Its quotient has layers

    J^i|Z_T,                     0<=i<=m,

which are flat over `T`; hence the finite filtered quotient is flat.
This verifies the flatness input to the accepted lifting machinery in
the present family, without assuming a retraction
`E_m -> E_(m-1)`. The relevant map of ambient schemes is the closed
immersion `E_(m-1) subset E_m`.

The accepted embedded-ideal argument identifies the square-zero
difference sheaf at step `m` with (5), independently of the product
presentation used in its original application. Equation (8) is
exactly the new hypothesis needed there. Thus the obstruction is a
canonical section of `V_m|K_(m-1)`; its zero scheme represents the
unique next embedded ideal. Equation units are already divided out
by the embedded-ideal functor, so they add no moduli. The accepted
noetherian argument applies to this one fixed finite-type `S`, proving
(2)--(4) and the regular locally principal formal inverse limit.

These uses of the already audited machinery are recorded in the
[relative functor audit](2026-10-15-generalization-uniform-root-tower-functor-independent-audit.md).
The new content is the intrinsic degree criterion and the relative
perfect-cohomology proof replacing the product splitting calculation.

Global smoothness of `E` is not a hidden hypothesis. At a point of a
geometric root, the local equations of `E` and of its Cartier root
cut out the smooth curve in the smooth threefold. Their two cotangent
classes are therefore independent, so `E` is smooth along that root.
This also supplies the smooth transverse local setting whenever the
formal-branch theorem is subsequently applied.

## 4. A genuine bounded parameter space, with its boundary retained

The theorem starts with a finite-type family; fixed integers `g,A,nu`
on an arbitrary ambient divisor are not asserted by themselves to
bound every possible root curve. Here is a standard construction when
`E` is projective, as in the blowup application.

Choose an ample polarization `Q` on `E` and a fixed Hilbert polynomial
`P`. The projective finite-type scheme `Hilb^P(E)` has its universal
flat proper subscheme. There is an open locus whose geometric fibers
are smooth, connected, one-dimensional effective Cartier divisors.
Over this locus the universal family is smooth, proper, and a
relative effective Cartier divisor.

The openness and scheme structure can be seen as follows. The
fiberwise Cartier condition is open near a fiber in a flat finitely
presented family, by the fiber criterion in
[Stacks, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/056P).
More explicitly, the universal ideal is flat over the Hilbert scheme
because the ambient structure sheaf and divisor quotient are flat.
The fiber criterion makes this ideal invertible on a neighborhood of
each point of a Cartier fiber; off that fiber's divisor it is the
unit ideal. The noninvertibility locus is closed. Properness of
`E x Hilb^P(E)` over the Hilbert scheme makes its image closed, so
the complement parameterizes precisely the relative Cartier fibers.
Smoothness of the entire fiber is open by properness
of the universal family and openness of its smooth locus; compare
[Stacks, Lemma 109.16.1, tag 0DZZ](https://stacks.math.columbia.edu/tag/0DZZ).
One restricts to pure relative dimension one. On this proper smooth
locus the dimension of geometric `H0(O_Z)` is the number of connected
components. Upper semicontinuity makes its value-one locus open.
The universal flatness and fiberwise Cartier condition imply the
relative Cartier assertion, retaining the original possibly
nonreduced parameter scheme structure.

All required numerical degrees are locally constant on this open.
For any relative line bundle `M`, the degree on a smooth curve is

    deg M_s=chi(M_s)-chi(O_(Z_s));

both Euler characteristics are locally constant in a proper flat
family. Apply this to the actual relative normal bundle and to
`O_E(E)|mathcal Z`. The genus is likewise locally constant.
Consequently the smooth Cartier open is a finite disjoint union of
open-and-closed numerical strata with fixed `g,A,nu`; a finite-type
scheme has only finitely many connected components. The strata
satisfying (1) are legitimate choices of `S`.

The smooth-root parameter locus usually is **not proper**, despite
being open in a projective Hilbert scheme. Its universal curve still
is proper over it. Noetherian stabilization needs its finite type,
not a proper parameter space, so no singular or nonreduced boundary
point needs to be reintroduced in order to apply the theorem.

A fixed Hilbert polynomial in one polarization must not simply be
declared to fix all the desired intersection invariants on a general
surface. The line-bundle degree argument supplies the explicit
numerical stratification instead. Varying over infinitely many
Hilbert polynomials does not give one finite-type family or one `N`.

## 5. Arbitrary actual normal bundles in a space-curve blowup

Let `C subset P3` be any fixed smooth connected curve, of degree `e`
and genus `gamma`, and put

    B=Bl_C(P3),            p:E -> C,
    H=pullback O_(P3)(1),
    n=deg N_(C/P3)=4e+2gamma-2.                            (9)

No splitting, semistability, or triviality of the projective normal
bundle is assumed. To fix signs, use the line convention

    E=P_lines(N_(C/P3)),
    O_E(E)=O_E(-1),
    eta=c1 O_E(E).

Equivalently use the quotient convention `P_quot(N_(C/P3)^*)`.
If `f` is a fiber of `p`, the ruled-surface intersections are

    eta.f=-1,             eta^2=-n.                       (10)

Let `Z subset E` be a smooth connected root finite over `C` of degree
`r>=1`; write `g_Z=genus(Z)`, and define

    nu=E.Z=deg O_E(E)|Z,
    A=Z^2_E,
    h=H.Z=e*r.                                            (11)

The smooth connected curve `Z` is integral. Its finite map to the
smooth base curve is flat; these intersections use its total degree.
The numerical class can be written

    Z == -r*eta+p^*D,
    deg D=r*n-nu.

Squaring with (10) gives the first new intrinsic identity

    A=r^2*n-2r*nu
      =(4e+2gamma-2)*r^2-2r*nu.                            (12)

Also `K_B=-4H+E`, so adjunction on `E` gives

    K_E=(-4H+2E)|E,
    2g_Z-2=A-4e*r+2nu,
    A=2g_Z-2+4e*r-2nu.                                    (13)

Equivalently,

    2g_Z-2=n*r^2-4e*r-2(r-1)*nu.                          (14)

These identities follow from the actual ruled bundle and contain no
replacement of it by a product. At `r=1`, (14) gives `g_Z=gamma`, as
it must for a degree-one map of smooth curves.

In particular the all-order uniqueness assumption (1) can be checked
without a splitting as

    nu>0,
    (2r+1)*nu>n*r^2,                                      (15)

or, equivalently using (13),

    nu>0,
    3nu>2g_Z-2+4e*r.                                      (16)

For a product arising from `N=L direct_sum L` and a root of class
`M boxtimes O(r)`, these recover `A=2r*deg M` and
`nu=r*deg L-deg M`, but no such presentation is used in the theorem.

For this fixed ruled `E`, fixing `(r,nu)` fixes the numerical divisor
class, so it fixes `Q.Z` for every chosen ample `Q`, and (14) fixes
the arithmetic genus. Thus **all** smooth connected roots with these
fixed invariants have one fixed Hilbert polynomial

    P_Z(t)=(Q.Z)*t+1-g_Z.

They lie in the smooth Cartier open of a single finite-type Hilbert
scheme. Taking the open-and-closed `(r,nu)` stratum gives a family
covering every such smooth root. A positive fixed `r` excludes fiber
curves; each map `Z -> C` is then nonconstant and finite. If desired,
the universal map to `C x S` is finite flat of degree `r`: it is proper
with finite geometric fibers, and relative flatness follows from the
flat family over `S` and the flat degree-`r` fiber maps. This is a
bounded-family assertion for fixed actual `C` and fixed numerical
root class, not for unbounded root order or varying embeddings.

## 6. Geometric emptiness produces a finite obstruction order

Continue with (9)--(11), a fixed finite-type family as above, and the
uniqueness condition (1). A compatible formal Cartier root gives the
accepted smooth formal surface branch transverse to `E`, with

    deg N_(Z/Vhat)=nu.

Suppose also

    nu>4g_Z+5.                                            (17)

The accepted
[intrinsic nef formal-branch criterion](2026-10-15-generalization-nef-formal-branch-arbitrary-base.md)
then supplies an integral surface in `P3` of some integer degree
`d>=1` satisfying

    d<=M(h,nu),
    M(h,nu)=max_(a integer,a>=1)(2a*h-nu*a^2),             (18)
    (d-1)(d-2)>=e*r*(r-1).                                (19)

The maximum is finite because `nu>0`. The exact maximum is the
appropriate integer maximum, rather than the real quadratic maximum.
The surface degree is positive because the chosen branch is
transverse to `E` and its algebraic closure maps birationally to an
integral surface in `P3`. The root contributes degree `r` to the
exceptional intersection, so the accepted plane-multiplicity argument
has exactly the right side of (19).

If there is **no integer `d>=1` satisfying (18)--(19)**, every formal
root in the family is forbidden. For an integer expression of the
same condition, since `M=M(h,nu)` is an integer, it suffices and is
equivalent to

    M<1,  or
    M>=1 and (M-1)(M-2)<e*r*(r-1).                         (20)

Indeed `(d-1)(d-2)` is nondecreasing on positive integers, with the
same value zero at `d=1,2`. This also handles `r=1` correctly.

Under (1), (17), and (20), the stable scheme in (4) has no geometric
point and is therefore empty as a scheme. Hence for this one fixed
family there is a finite exceptional order with

    K_N=empty.                                            (21)

For a nonempty family one may take `N>=1`. In particular, (21) is
uniform over **all** smooth connected roots of a fixed numerical
class on the actual ruled exceptional divisor, when they satisfy
these numerical hypotheses. This simultaneously removes the former
rational-base and split-normal-bundle restrictions from this scoped
finite-obstruction conclusion.

For the broad intrinsic formulation one can instead take a nef line
bundle on a smooth projective threefold with degree `h` on the roots,
retain the accepted positive-surface-square hypothesis, and impose
any independently justified numerical incompatibility with (18).
The plane inequality (19) belongs specifically to the space-curve
blowup application.

## 7. Conditional consequence for an actual complete intersection

This step still requires a **valid actual-CI-to-root bridge** in its
precise stated scope. If the bridge supplies a root in this family,
ordinary generic initial relation degrees `(r,s)` with `s>r`, and the
local strict ideal

    (h,u^(s-r)),

then it supplies the first Cartier relation exactly through stages

    m<s-r.

Thus (21) forces

    s-r<=N.                                               (22)

At equality only stage `N-1` is supplied. The result bounds the
generic normal-order gap for this bridge lane; it does not assert a
bound on projective hypersurface degrees or turn formal compatibility
into a complete-intersection construction.

The relative finite-family argument and the intersection identities
use no characteristic-zero division. This note nevertheless fixes
characteristic zero throughout; extending the final CI consequence
requires the chosen bridge in the chosen characteristic. The accepted
[characteristic scope addendum](2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md)
addresses the formal geometric inputs separately.

Singular or nonreduced roots are outside the negative-degree argument
proved here. The hypotheses do not assert that every actual normal
bundle splits, that every smooth root satisfies (1) or (17), or that
every numerical class satisfies (20). No cutoff value is computed.
The universal STCI problem and unrestricted `C0` remain open. No
canonical index, commit, or memory was changed by this note.
