# finite root families and smooth obstructions

Permanent complete mathematical dossier with hypotheses, proofs, characteristic scope, exceptional cases and limitations preserved.

---

## 2026-10-15-generalization-intrinsic-finite-root-family

# Intrinsic finite root families without a split normal bundle

Date: 2026-10-15; completed 2026-10-16. Author: `intrinsic_root_finite_family`.
Status: **NEW STRUCTURAL GENERALIZATION; targeted independent review passes**.
The [independent scope audit](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-intrinsic-finite-root-family-independent-audit)
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
[relative functor audit](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-functor-independent-audit).
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
[characteristic scope addendum](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-characteristic-scope-addendum)
addresses the formal geometric inputs separately.

Singular or nonreduced roots are outside the negative-degree argument
proved here. The hypotheses do not assert that every actual normal
bundle splits, that every smooth root satisfies (1) or (17), or that
every numerical class satisfies (20). No cutoff value is computed.
The universal STCI problem and unrestricted `C0` remain open. No
canonical index, commit, or memory was changed by this note.


---

## 2026-10-15-generalization-intrinsic-finite-root-family-independent-audit

# Independent audit: intrinsic finite root families and nonsplit ruled numerics

Date: 2026-10-15. Reviewed: 2026-10-16.
Reviewer: `relative_scope_audit`.

**Verdict: PASS for the stated relative finite-family generalization,
bounded Hilbert-family construction, splitting-free intersection identities,
and conditional finite empty-stage consequence.** The completed
[owner note](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-intrinsic-finite-root-family)
was read in full. The accepted embedded-Cartier lifting functor, its
noetherian stabilization argument, and the accepted intrinsic nef
formal-branch and plane-multiplicity theorems are premises. This audit
checks their new relative hypotheses and numerical inputs; it does not
replay those accepted proofs or any accepted computation. No CAS or
accepted verifier was run.

## 1. Relative negativity really yields a vector bundle over a nonreduced base

Write `q:mathcal Z -> S` for the proper smooth family with geometrically
connected one-dimensional fibers, and put

    mathcal L_m=N_(mathcal Z/(E x S)) tensor O_E(-mE)|mathcal Z.

The actual relative normal bundle in this definition is necessary: it
retains any universal coefficient line from the parameter space. Its
restriction to a geometric fiber has degree `A-m*nu`. Under
`nu>max(A,0)`, this is negative for every `m>=1`. A smooth geometrically
connected curve is geometrically integral, so negative degree gives
`H0=0`. Riemann--Roch then gives

    h1(Z_s,L_(m,s))=g-1-A+m*nu.

This numerical argument deliberately uses smooth, geometrically connected
fibers. Total negative degree would not imply the same vanishing on an
arbitrary reducible or nonreduced root.

The passage to families is valid with all parameter nilpotents retained.
The morphism `q` is flat, proper, and of finite presentation, and
`mathcal L_m` is invertible and flat over `S`. The owner's cited
[Stacks Project, Lemma 36.30.1, tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
applies with the perfect object `mathcal L_m` and the flat sheaf
`O_mathcal Z`; its conclusion is perfect derived pushforward compatible
with arbitrary base change. Equivalently, one can apply the relative
perfect version,
[Stacks Project, Lemma 36.35.10, tag 0DJT](https://stacks.math.columbia.edu/tag/0DJT).

Locally represent this perfect complex in degrees zero and one. Its
differential is injective after every geometric residue-field pullback.
At each point, a maximal minor of this differential is a unit on some
neighborhood; elementary elimination makes it a split inclusion there.
The cokernel is consequently locally free even over a nonreduced local
ring. Thus, canonically in the derived category,

    Rq_*mathcal L_m=V_m[-1],
    rank V_m=g-1-A+m*nu.

After every `T -> S`, the pulled-back complex is `V_m|T[-1]`. This proves
the universal zero `H0` and the required base-change assertion for
`R1`, including nonflat maps from nonreduced parameter schemes. The
argument does not substitute a bare constant-dimension assertion for
perfect cohomology.

Properness here is a property of `q`; the parameter scheme need not be
proper. No global projectivity of the original intrinsic `X` is used
for this part of the statement.

## 2. The Cartier hypotheses supply the accepted lifting machinery

The root is an effective Cartier divisor and its quotient is flat over
`S`. It therefore remains Cartier after arbitrary base change, by
[Stacks Project, Lemma 31.19.1](https://stacks.math.columbia.edu/tag/056P).
Multiplication by its local equation is regular on every invertible
graded layer `J^i`. Lifting that equation to an exceptional thickening
preserves regularity by the finite nilpotent filtration. The resulting
quotient has layers `J^i|Z_T`, all flat over `T`, so its finite quotient
is flat over `T` as required.

These are the local regularity and quotient-flatness hypotheses used by
the accepted embedded-ideal torsor argument. Its difference sheaf is
precisely `mathcal L_m`, and the relative vanishing just proved applies
after every parameter base change. Therefore the accepted argument gives
the canonical obstruction section on the previous lifting locus, its
closed zero scheme, and uniqueness of the next embedded ideal. There is
no additional equation-unit parameter.

No global smoothness of `E` is silently required. The tower itself only
uses its Cartier embedding and the stated Cartier root. For a geometric
root where a smooth formal surface is needed later, smoothness of the
Cartier curve `Z subset E subset X` forces `E` to be smooth along `Z`:
locally `Z` is cut out in the regular three-dimensional ambient ring by
the two equations for `E` and for its Cartier root; smoothness of their
curve quotient makes their two cotangent classes independent. Thus the
resulting formal root surface has the required smooth transverse germ.

All stages lie over the same finite-type noetherian `S`. Hence the
accepted ideal-sheaf ascending-chain argument gives eventual
scheme-theoretic stabilization and the compatible formal Cartier ideal.
The note correctly retains the limitations: there is no numerical
cutoff, no inference from one adjacent equality, no algebraization
claim from the tower alone, and no assertion of flatness of an infinite
inverse-limit module.

## 3. The Hilbert construction is a bounded family with its scheme structure

For projective `E`, a chosen polarization and one Hilbert polynomial
give a projective finite-type Hilbert scheme with a flat universal
subscheme proper over the parameter space. The stated smooth,
geometrically connected, one-dimensional Cartier locus is open.

For the Cartier assertion, the ambient `E x Hilb` is flat and finitely
presented over `Hilb`, and the universal subscheme is flat and finitely
presented. The fiber criterion in
[Stacks Project, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/056P)
identifies the relative Cartier property near every point where the
fiber has that property. Its complement is closed; properness of the
ambient projective family makes the image of that complement closed.
Restricting to the complementary parameter open gives Cartier fibers
everywhere and a relative effective Cartier universal divisor.

The locus where the entire proper flat fiber is smooth is open. After
restriction to nonempty smooth one-dimensional fibers, geometric
`h0(O_Z)` equals the number of connected components. The value-one
locus is open by upper semicontinuity, since this number is at least
one. These constructions restrict the existing Hilbert scheme; they
do not replace it by a reduced parameter scheme.

For a relative line bundle `M` on this proper smooth family,

    deg M_s=chi(M_s)-chi(O_(Z_s))

is locally constant. Applying this to the actual relative normal bundle
and the fixed exceptional line bundle gives the claimed local
constancy of `A` and `nu`; genus is also locally constant. A finite-type
scheme has finitely many connected components, so the desired numerical
loci are finite unions of open-and-closed strata. Each such stratum is
a legitimate finite-type `S`, even though it generally is not proper.

The distinction in the note is necessary and correct: on a general
surface, fixing only `g,A,nu` is not by itself a boundedness theorem,
and fixing a Hilbert polynomial does not automatically fix every
intersection invariant. The explicit numerical stratification supplies
the needed fixed-invariant families. An infinite union over Hilbert
polynomials supplies no single finite-type parameter scheme or uniform
stabilization integer.

## 4. The nonsplit blowup identities have consistent signs

Let `n=deg N_(C/P3)=4e+2gamma-2`. With the explicit line convention
`E=P_lines(N)` and `eta=c1 O_E(E)`, one has

    eta.f=-1,                     eta^2=-n.

This is equivalently the quotient convention `P_quot(N^*)`; the
duality matters. A numerical divisor of fiber degree `r` has the form

    Z == -r*eta+p^*D.

Intersecting with `eta` gives `deg D=rn-nu`; squaring gives

    A=Z^2=r^2*n-2r*nu.

Independently, the blowup canonical class and adjunction give

    K_E=(-4H+2E)|E,
    2g_Z-2=A-4er+2nu,
    A=2g_Z-2+4er-2nu.

Consequently

    2g_Z-2=n*r^2-4er-2(r-1)*nu.

The signs, the factor `r` in the quadratic formula, and the factor
`r-1` in the last identity are correct. At `r=1` the last formula
recovers `g_Z=gamma`. These calculations use only the actual ruled
bundle, not a splitting or product replacement.

The displayed equivalent uniqueness tests also follow exactly:

    nu>max(A,0)
    iff nu>0 and (2r+1)*nu>n*r^2
    iff nu>0 and 3nu>2g_Z-2+4er.

For the fixed ruled exceptional divisor, `(r,nu)` fixes the numerical
divisor class. It therefore fixes its degree in every chosen ample
polarization, and the adjunction identity fixes its genus. All smooth
connected roots of that fixed class lie in one fixed Hilbert scheme,
with polynomial `(Q.Z)t+1-g_Z`. The `r` and `nu` functions are degrees
of fixed relative line bundles and hence give an open-and-closed
stratum there.

A positive `r` excludes a vertical integral curve. Its proper
nonconstant map to `C` is finite, and a finite map between smooth
integral curves is flat. The optional family assertion in the note is
also valid: `mathcal Z -> C x S` is proper with finite geometric fibers,
thus finite; flatness follows from `S`-flatness and the fiberwise flatness
criterion. Its rank is the fixed degree `r`.

## 5. Numerical incompatibility implies an empty stable scheme and finite order

For a smooth formal root in the blowup, the accepted transverse-branch
construction has normal degree `nu` and hyperplane degree `h=er`.
Under `nu>4g_Z+5`, the imported nef formal-branch and plane-multiplicity
arguments apply with exactly the proposed inputs. They require an
integer `d>=1` such that

    d<=M(h,nu),
    M(h,nu)=max_(a integer,a>=1)(2ah-nu*a^2),
    (d-1)(d-2)>=er(r-1).

The maximum is finite and integral because `nu>0`; replacing it by the
real quadratic maximum would weaken the stated test. Since
`P(d)=(d-1)(d-2)` is nondecreasing on positive integers, with
`P(1)=P(2)=0`, absence of such an integer `d` is equivalent to

    M<1, or M>=1 and (M-1)(M-2)<er(r-1).

This handles the degree-one and degree-two boundaries, including
`r=1`. The note correctly presents this as an emptiness criterion
under the high-normal-degree and all-order uniqueness hypotheses.

If every geometric root in the family is numerically forbidden, the
stable closed scheme has no geometric point. A nonempty finite-type
scheme over an algebraically closed field has a geometric point, so
the stable scheme is empty, with all its possible nilpotents. Eventual
scheme-theoretic stabilization then gives one finite empty stage for
the chosen whole family. No explicit value for that stage has been
deduced from the numerical argument.

## 6. The actual-CI application keeps its bridge condition and strict indexing

This audit accepts the actual-CI bridge only when its full independent
hypotheses hold. If it supplies the strict local ideal
`(h,u^(s-r))`, its first principal relation survives through exceptional
stage `m` precisely in the asserted range `m<s-r`. Thus an empty stage
`K_N` forces `s-r<=N`. At equality only stage `N-1` is provided, so
there is no off-by-one strengthening.

This is a necessary bound on the generic normal-order gap in that
bridge lane. It is not a projective hypersurface-degree bound and
does not make formal compatibility sufficient for an actual complete
intersection. Singular and nonreduced roots remain outside this
intrinsic negative-degree proof. The unrestricted characteristic-zero
`C0` question and the universal STCI question remain open.

The review produced only this audit file. It changed no accepted
verifier, canonical record, index, commit, or memory.


---

## 2026-10-15-generalization-smooth-root-formal-nonexistence

# Positive-normal algebraization excludes every smooth movement-two formal root

Date: 2026-10-15. Author: `formal_algebraization_route`.
Status: **GEOMETRIC THEOREM; independently audited in characteristic zero**.
Accepted conormal, blowup, actual-CI bridge, and formal-root functor statements
are inputs. No accepted computation or proof was rerun. A distinct worker
reviewed the [branch-normalization and ruled-surface intersection steps](OCT15_20_PROJECTION_ROOT_AND_SURFACE_FRONTIERS.md#source-2026-10-15-formal-branch-ruled-model-degree-bound-reviewmd),
and the [full independent audit](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit)
passes Sections 1--8, including the general criterion and finite-stage/gap
consequences. Section 9 preserves an ineffective finite-jet attempt.
The [characteristic-scope addendum](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-characteristic-scope-addendum)
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
[uniform formal-root tower note](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-finite-determinacy):
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


---

## 2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit

# Independent audit of smooth-root formal nonexistence

Date: 2026-10-15. Author: `new_logarithmic_review`.

Status: **PASS: the smooth movement-two nonexistence theorem holds for
every balanced smooth rational space curve of degree e>=4 and every
r>=2, with the stated embedded-Cartier interpretation.** The generalized
numerical criterion and its new quadratic consequence also pass, with
the rational-base and numerical hypotheses retained. Combined with the
accepted finite tower, this gives an existential uniform finite empty
stage for each fixed r on the entire smooth-root open, and the precise
bounded-gap consequence below. It does not exclude all actual complete
intersections in that open.

The target is the live
[formal-nonexistence note](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-formal-nonexistence),
including the clarification of connectedness, the whole-curve gluing
argument, the direct plane-adjunction argument, and equation (3a) added
during review. This audit inspected the primary algebraicity and
high-self-intersection sources. Accepted root-functor, finite-tower,
actual-CI bridge, and prior CAS/class computations are premises and were
not replayed. The existing
[focused branch/ruled review](OCT15_20_PROJECTION_ROOT_AND_SURFACE_FRONTIERS.md#source-2026-10-15-formal-branch-ruled-model-degree-bound-reviewmd)
is an input; the additional work here checks the algebraicity hypotheses,
global branch selection, multiplicity/genus passage, all-r numerical
scope, and the finite-cutoff conclusion.

## 1. Exact formal object and the whole smooth root

Throughout, C is a smooth rational curve embedded in P3 over an
algebraically closed field k of characteristic zero. Its balanced normal
bundle is O_(P1)(lambda)^2, with lambda=2e-1 and deg C=e. The accepted
blowup convention gives

    B=Bl_C(P3), E=P1 x P1,
    O_E(-E)=O_E(-lambda,1).

For the general numerical criterion, Z is a smooth connected divisor of
class (epsilon,r), finite over C of degree r. The elementary product
intersection and adjunction formulas give

    g(Z)=(epsilon-1)(r-1),
    deg O_Z(a,b)=a*r+b*epsilon.

For epsilon=2 and r>=2, connectedness and finiteness do not need to be
added as hidden hypotheses to the main theorem. The divisor exact
sequence and Kunneth give H^1(E,O_E(-2,-r))=0, hence H^0(Z,O_Z)=k.
A smooth proper curve with this property is connected, and its smooth
irreducible components cannot meet. Thus it is integral. An integral
curve of class (2,r) is not a fiber of E->C; its proper nonconstant map
to C is finite, of degree r. The generalized criterion retains
connectedness and finiteness explicitly for other classes.

The accepted inverse-limit functor supplies an embedded effective
Cartier formal divisor Vhat in B-hat_E, reducing to exactly Z. Locally
let E=(u), let a lift f cut out Z modulo u, and write its formal
equation as g=f+u a. Smoothness of Z means that f has nonzero
differential on E. Consequently the full completed local ring of Vhat
at every point of Z is k[[t,u]], and u is a regular parameter transverse
to Z. In particular Vhat is a smooth formal surface along its entire
scheme of definition, not only at the generic point of Z.

There is also a needed change-of-completion check. Inside Vhat,

    I_Z O_Vhat=(u,f)O_Vhat=(u)=I_E O_Vhat.

Its exceptional topology is therefore already the induced Z-adic
topology. Completion transitivity gives a closed formal immersion
Vhat -> B-hat_Z, as required by the algebraicity theorem. No global
equation, formal line-bundle descent, or algebraic surface is assumed
at this stage.

The normal line of Z in this formal surface is

    N_(Z/Vhat)=O_Z(E)=O_Z(lambda,-1),
    deg N_(Z/Vhat)=lambda*r-epsilon=nu.                 (A)

Under nu>4g+5 it is ample, since an invertible sheaf on a smooth proper
curve is ample exactly when its degree is positive.

## 2. Primary algebraicity theorem: all hypotheses match

[Bost, Theorem 3.5 and Corollary 3.8, printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27)
apply here with quasiprojective ambient variety, smooth connected
projective center, smooth formal subscheme admitting that center as
scheme of definition, and ample normal bundle. The conclusion is an
algebraic subvariety of the same dimension containing the formal
subscheme along the whole center; the closure is integral. The printed
dimension hypothesis is **at least one**, despite the web extraction's
apparent greater-than-one sign. These geometric results impose no
arithmetic or convergence hypothesis.

Here the data are X=B, center Z, formal dimension two, and the positive
normal line (A). Thus the Zariski closure W is an integral algebraic
surface in B, and Vhat is an embedded formal branch of W along all of Z.
This gives formal containment, not equality with every branch of
W-hat_Z. Other branches and other components of W cap E are allowed.

The directly verified attribution is Bost's geometric algebraicity
theorem, obtained there from Hartshorne's formal-function results.
The proof does not depend on a broader historical attribution.

## 3. Why the selected branch glues on the normalization

The focused review establishes the local normalization/completion
mechanism. Here its input follows from the primary algebraicity
conclusion: B is smooth of dimension three, W is an integral Cartier
surface, and the chosen full completed quotient at every z in Z is a
regular two-dimensional ring. It is consequently a minimal completed
branch. Excellence makes normalization finite and identifies the
completed normal factors with the normalizations of the completed
branches. The selected factor is already regular and normal. See
[Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C2E).

Local factor selection alone should not substitute for the global
argument. That argument is available here. On a normal-domain formal
chart Spf R over an affine Spec A in W, the map A->R is injective:
locally it maps into a minimal completed branch, whose contraction to
the algebraic domain is zero. Map the finite integral closure Abar
first into Frac(R). Its elements are integral over R, so they belong
to R because R is normal. These maps are unique and agree on overlaps.
They define a morphism Vhat->Wnu to the algebraic normalization.

Reducing this morphism modulo the ideal of definition gives a closed
immersion Z->Wnu over the original Z->W. Its image Znu is isomorphic
to Z. At every point of Znu, the full local completion of Wnu is
the regular selected branch. Hence Wnu is regular along Znu. The
lifted closed immersion Vhat->(Wnu)-hat_Znu is an isomorphism: its
coherent kernel is zero after faithfully flat full local completion
at every point of Znu. This proves the whole-curve formal-neighborhood
identification needed below. It does not identify the other branches
of W with this neighborhood.

Bost's printed p. 186 normalization observation concerns point germs.
It is an appropriate illustration of the local mechanism; the unique
normal-ring lift just given supplies the additional whole-curve gluing.

Take a projective resolution T->Wnu preserving this regular open set.
The same smooth curve Z in T then has

    Z^2=nu, genus(Z)=g.                                  (B)

This is the normal-bundle degree of the selected algebraic branch,
unchanged by resolution away from Z.

## 4. Ruled model and numerical degree: correct for general g,nu,h

The exact primary theorem is
[Hartshorne, Theorem 4.1, printed p. 122, with the definition on p. 111](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=13).
For a smooth curve on a smooth proper surface, the strict inequality
Z^2>4g+5 gives equivalence to a section of a geometrically ruled
surface. In this paper equivalence is a birational map that is an
isomorphism on an open neighborhood of the curve. The result applies
for every genus here, and the strict inequality avoids its boundary
exception. It is stronger than merely being birationally ruled.

The algebraic closure W is not E: on Vhat the exceptional parameter u
is nonzero and regular. Let S be its image in P3. It is an integral
surface, and W is its strict transform because B->P3 is an isomorphism
off E. The morphism T->S is birational. If H is the pullback of a
hyperplane and d=deg S, then

    H is nef, H^2=d>0, H.Z=deg O_C(1)*deg(Z->C)=e*r=h.   (C)

No isomorphism from a neighborhood of Z to P3 is used; the map
Z->C usually has degree r. The neighborhood isomorphism used in the
degree argument is the one to the ruled model.

The focused review's intersection argument extends without change
from (g,nu,h)=(1,12,8) to (B)--(C). On a common resolution outside the
curve neighborhoods, push the nef pullback of H to a divisor D on
the ruled surface R. Negative definiteness gives d<=D^2, and D is
nef. Numerically D=a Z0+b f, where a=D.f is a nonnegative integer.
The case a=0 would give D^2=0, so a>=1. From D.Z0=h and Z0^2=nu,

    b=h-a*nu,
    d<=D^2=2ah-nu*a^2.

Thus the generalized upper bound is valid:

    d<=M:=max_(a integer,a>=1)(2ah-nu*a^2).              (D)

The maximum exists because nu>0. If nu>=h, the successive difference
2h-nu*(2a+1) is negative for every a>=1, so M=2h-nu. These conclusions
do not require descending the formal divisor or its line bundle to B.

## 5. Other branches do not weaken the actual multiplicity bound

Let m be the generic I_C-adic order of the equation of S. The strict
transform W is an effective Cartier divisor distinct from E. Its
restriction W|E is therefore an effective Cartier divisor. Over the
generic point of C, the ordinary blowup of the two-dimensional regular
normal local ring shows that W|E has degree m on the exceptional P1.
Equivalently, W is linearly equivalent to dH-mE, whose restriction has
direction degree m.

The crucial containment is embedded, not an abstract identification
with a formal surface. Vhat being a branch of W implies, on reducing
the formal containment modulo u,

    Z subset W|E

scheme-theoretically. On the smooth surface E, this says W|E-Z is
effective. Intersecting with the generic fiber of E->C gives

    m>=r.                                               (E)

Extra branches can contribute additional copies of Z or additional
effective components. They cannot subtract its degree. No equality
W|E=Z or equality m=r has been assumed.

## 6. General planes, integral sections, and the genus inequality

Choose a plane P general in the full dual projective space. Bertini
irreducibility applies to the integral surface S, even if S is
nonnormal. General reducedness follows by applying smooth Bertini
on the dense regular locus; the possible singular-locus intersection
is finite, and a plane hypersurface has no embedded components.
Thus Gamma=S cap P is integral. The relevant primary formulations are
[Stacks, Bertini irreducibility](https://stacks.math.columbia.edu/tag/0G4C)
and [smooth Bertini](https://stacks.math.columbia.edu/tag/0FD4).

The plane may simultaneously meet the smooth C transversely in e
distinct points q_i and avoid the finite complement of the dense open
where the equation of S lies in I_C^m. These are compatible nonempty
open conditions on the plane. At q_i, the restriction of I_C to the
transverse plane is its maximal ideal. Therefore the equation of
Gamma belongs to that maximal ideal to power m, and its actual
plane multiplicity n_i satisfies n_i>=m.

There is no need to assert that these singularities are ordinary.
Blow up P at the e distinct q_i. The integral strict transform of
Gamma has class d l-sum n_i E_i. Adjunction on this smooth plane
blowup gives

    p_a(Gamma')=((d-1)(d-2)-sum n_i(n_i-1))/2.

An integral proper curve has nonnegative arithmetic genus. Hence

    (d-1)(d-2)>=sum n_i(n_i-1)
                 >=e*m*(m-1)>=e*r*(r-1).               (F)

This is an independent proof of the lower bound, with arbitrary
higher contacts and all plane-curve branch types retained.

## 7. Movement two: every r>=2 contradicts (D)--(F)

For epsilon=2 and lambda=2e-1,

    g=r-1, nu=(2e-1)r-2, h=e*r,
    nu-(4g+5)=(2e-5)r-3>0,
    nu-h=(e-1)r-2>0

for e>=4 and r>=2. Thus both algebraicity positivity and the ruled
threshold hold, and (D) gives

    1<=d<=2h-nu=r+2.

For positive integers d<=r+2, (d-1)(d-2)<=r(r+1). Combining with
(F) would give r+1>=e(r-1). But

    e(r-1)-(r+1)=(e-1)r-e-1>=e-3>0.

This contradiction proves the main theorem for every normal order r
in one argument. For e=4,r=2 it specializes to the impossible pair
d<=4 and (d-1)(d-2)>=8, as claimed.

## 8. General numerical criterion and its finite-r corollary

The criterion (D)--(F) passes whenever the smooth rational-base setup,
smooth connected finite root, and nu>4g+5 all hold. For the actual
balanced rational curve in P3, lambda=2e-1. Its threshold is exactly

    (2e+3-4epsilon)r+3epsilon-9>0.

If also (e-1)r>=epsilon, then nu>=h and d<=r+epsilon. Substituting
this upper bound in (F) and expanding gives precisely

    (e-1)r^2-(e+2epsilon-3)r
      -(epsilon-1)(epsilon-2)<=0.                       (G)

For fixed epsilon with 2e-1>4(epsilon-1), the two preceding threshold
conditions hold for all sufficiently large r. The coefficient of r^2
in (G) is positive. Therefore only finitely many first normal orders
can support such a smooth all-orders root. This is a sufficient
structural exclusion; it says nothing about a root failing a threshold
or about singular/nonreduced/disconnected roots. The formula for g
here uses the rational base. It is not asserted for an arbitrary curve
with a balanced normal bundle.

## 9. Uniform finite empty stage and the exact actual-CI gap bound

Fix the actual embedding C subset P3 and r. On the accepted coefficient
open U for (epsilon,r)=(2,r), lambda=2e-1>=7>3epsilon. The
[accepted finite tower](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-finite-determinacy)
therefore supplies closed schemes K_m on this single finite-type U,
all-order uniqueness, and a finite index N with K_N=K_(N+1)=... .
Its stable scheme represents compatible formal embedded Cartier ideals.
Let U_sm be its smooth-root open.

The theorem above eliminates every geometric point of K_N cap U_sm.
A nonempty finite-type scheme over k has a geometric point, so

    K_N cap U_sm is the empty scheme.                   (H)

Nilpotents do not evade this conclusion. This N is a uniform finite
failure stage over the entire smooth-root family for the fixed r and
actual embedding. No explicit value, uniformity as r varies, or
emptiness on the singular-root boundary follows.

Finally retain every hypothesis of the accepted actual-CI bridge,
including its smooth actual root, saturated first relation, and jointly
generating leading symbols. If the generic normal initial regular
sequence has degrees (r,s), s>r, its strict ideal is locally
(h,u^(s-r)). With E_m=V(u^(m+1)), it gives the Cartier ideal (h) at
exactly the stages guaranteed by m<s-r. Thus the root lies in
K_(s-r-1). Equation (H) forces

    s-r<=N, equivalently s<=r+N.                        (I)

At equality s-r=N, the bridge only provides stage N-1; it does not
provide stage N. A gap N+1 would provide the empty stage N and is
excluded. This proves the requested existential bound on the actual
bridge gap, while preserving its strict indexing.

The accepted
[functor audit](UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md#2026-10-15-generalization-uniform-root-tower-functor-independent-audit)
already fixes this indexing and all-order compatibility; those proofs
were not replayed. Finite-gap actual pairs can introduce their second
relation before the empty stage, so (I) is not their exclusion.

## Disposition and remaining scope

The main theorem, the generalized criterion, equation (3a)/(G), and the
finite-cutoff/gap consequences (H)--(I) pass this audit. The owner
incorporated the smooth-root connectedness, whole-curve normalization,
and direct plane-adjunction clarifications during review. These clarify
existing valid steps rather than repair a counterexample.

This result excludes infinite embedded smooth movement-two formal
first-principal-ideal lifts. It gives neither an explicit N nor a claim
that K_1 or K_2 is empty. It does not apply automatically to singular or
nonreduced roots, coefficient base points, unsaturated first relations,
or actual complete intersections outside the accepted bridge. It does
not settle the unrestricted C0 or universal STCI problem.

No accepted verifier, first/second class computation, or CAS elimination
was replayed. No commit or memory write was performed.


---

## 2026-10-15-generalization-smooth-root-characteristic-scope-addendum

# Characteristic-only addendum for the smooth-root theorem

Date: 2026-10-15. Reviewer: `new_logarithmic_review`.

Status: **PASS for the characteristic-free formal geometric theorem,
its numerical criterion, and the finite embedded-Cartier tower under
their explicit hypotheses. The actual-CI gap conclusion remains
conditional on the actual bridge being valid in the chosen
characteristic.**

This reviews only Section 10 of the
[owner note](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-formal-nonexistence).
The completed
[characteristic-zero geometry audit](FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md#2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit)
is a premise; its arguments and accepted computations were not replayed.
No characteristic-zero logarithmic argument, P010 calculation, or
normal-bundle splitting of the literal repository curve is imported.

## 1. The geometric inputs permit arbitrary algebraically closed k

- [Bost, geometric Theorem 3.5 and Corollary 3.8](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27)
  are stated over a field k without a characteristic restriction.
  Their smooth formal branch, complete positive-dimensional center,
  and ample-normal hypotheses remain exactly the ones already checked.
- [Hartshorne, Section 1 and Theorem 4.1](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=3)
  explicitly work over an algebraically closed field of arbitrary
  characteristic. The neighborhood-equivalence conclusion used in
  the accepted degree argument has that scope.
- Finite-type local rings over a field are excellent in every
  characteristic. Finite normalization and its completed-branch
  decomposition retain their hypotheses; see
  [Stacks, Lemma 15.110.8](https://stacks.math.columbia.edu/tag/0C2E).
- Algebraic surface resolution is available in every characteristic:
  [Stacks, Lipman's Theorem 54.14.5](https://stacks.math.columbia.edu/tag/0BGP)
  applies to finite-type surfaces over a field, as explained in the
  [chapter introduction](https://stacks.math.columbia.edu/tag/0ADX).
  The construction uses normalized point blowups over singular points,
  so it can preserve the regular neighborhood of the selected curve;
  see [Lemma 54.6.5](https://stacks.math.columbia.edu/tag/0BFZ).
  These modifications are projective here. Since an algebraically
  closed field is perfect, the resolved regular surface is smooth.

Normality, uniqueness of the normalization lift, surface intersection,
and adjunction do not require characteristic-zero division. The
formal surface is smooth because the **full** root divisor is smooth;
no nonvanishing fiber derivative or separability of its projection
is needed for this step.

## 2. Embedded hyperplanes avoid the inseparable-linear-system issue

For an integral S in P3 over algebraically closed k of any
characteristic, [Stacks, Lemma 37.32.3](https://stacks.math.columbia.edu/tag/0G4C)
gives an irreducible general hyperplane section. The smooth locus of
S is dense, and its immersion in P3 satisfies
[smooth Bertini, Lemma 33.47.3](https://stacks.math.columbia.edu/tag/0FD4)
in arbitrary characteristic. Thus a general section is generically
reduced. Being a plane hypersurface, it has no embedded components;
it is consequently integral. No arbitrary inseparable linear system
on a separate source is being used.

General planes meet the smooth embedded C transversely in e distinct
points in every characteristic. Indeed planes containing a tangent
line to C form an incidence image of dimension at most two in the
three-dimensional dual projective space. A general plane also avoids
the finite nongeneric-multiplicity locus on C. Wild ramification or
inseparability of another map does not change this incidence argument.

If Z->C is inseparable, its total degree is still r, and

    H.Z=deg pullback(O_C(1))=e*r.

The formula uses total field degree, including inseparable degree.
Likewise, W|E>=Z gives m>=r by intersection lengths on an exceptional
fiber. Neither calculation counts distinct geometric points in a
fiber of Z->C. Plane blowup adjunction and nonnegative arithmetic
genus then give the accepted lower bound in every characteristic.
No separable Puiseux expansion or ordinary-singularity assumption
enters that calculation.

## 3. Characteristic-free formal theorem and finite cutoff

The main formal theorem therefore holds over arbitrary algebraically
closed k: for a smooth rational C of degree e>=4 with the **explicit**
balanced normal bundle O_(P1)(2e-1)^2, every smooth Z of class (2,r),
r>=2, fails to extend as an embedded Cartier divisor through all
exceptional neighborhoods. The general numerical criterion and its
quadratic consequence retain the same rational-base, smoothness,
finiteness, and numerical assumptions.

The Euler and tangent sequence degree calculation is characteristic
free, so balance, when it actually holds, gives lambda=2e-1. This does
not establish balance for any particular curve in an exceptional
characteristic, or transfer an earlier splitting calculation.

The accepted tower's cohomological and functor proofs introduce no
characteristic restriction. Their inputs are the divisor sequence
on P1 x P1, multiplication by a nonzero fiber polynomial, vector-bundle
splitting and cohomology on P1, square-zero embedded-ideal lifting,
equation units, Nakayama, and noetherian stabilization. None divides
by a degree or factorial, takes a logarithm, or assumes a separable
root polynomial. Multiplication remains injective even when the
characteristic divides r, and the relative arguments include
nonreduced roots and parameter bases.

Thus lambda>3epsilon still supplies all-order uniqueness and the fixed
finite-type closed tower in any characteristic. For epsilon=2,e>=4,
lambda>=7>6. For each fixed actual embedding and r, combining this
tower with the formal theorem gives a finite N with

    K_N intersect U_smooth = empty

as a scheme. The cutoff is existential and is not uniform as r or
the actual embedding varies.

## 4. Positive-characteristic actual-CI consequence is conditional

The existing
[actual-CI bridge audit](QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md#2026-10-14-generalization-blowup-root-curve-bridge-independent-audit)
is explicitly stated in characteristic zero. Its generic-root argument
uses generic separability. In characteristic p, smoothness of the
whole root does not by itself imply this: the local equation
v^p-t=0 is smooth over k but its projection to the t-line is
inseparable. The formal nonexistence theorem above needs no such
separability, but it must not silently extend that earlier bridge.

Whenever a valid bridge in the chosen characteristic supplies the
local strict ideal

    (h,u^(s-r)),

with all its other actual hypotheses, the indexing argument is purely
algebraic. It supplies every stage m<s-r. The
empty stage N therefore forces

    s-r<=N, equivalently s<=r+N.

At equality only stage N-1 is supplied. The addendum does not assert
that arbitrary positive-characteristic actual CIs satisfy this local
bridge, nor that they are excluded. A separate bridge extension may
use additional hypotheses or a direct local proof; it is outside
this characteristic-only review.

No accepted verifier, CAS calculation, first/second class computation,
commit, or memory write was performed. Singular or nonreduced roots,
unbalanced normal bundles, and unrestricted STCI remain outside this
conclusion.


---

## 2026-10-15-generalization-movement-one-formal-roots-independent-audit

# Independent targeted audit: movement-one formal roots

Date: 2026-10-15. Reviewer: `g3_branch_uniqueness`.

**Verdict: PASS for Section 5 in its stated characteristic-zero scope.** The imported intrinsic nef criterion, branch/ruled-surface argument, and plane-adjunction inequality are premises. Only the new movement-one corollary was reviewed; accepted Sections 1--4 and prior CAS certificates were not re-audited.

Reviewed artifact: [Section 5 of nef formal branches over arbitrary bases](2026-10-15-generalization-nef-formal-branch-arbitrary-base.md).

Reviewed whole-file SHA-256:

`4d73bbb45ba2689a0f0fb33e88a32d2c3687b004371f06b5afc603ef3864a01e`.

For a smooth root of class `(1,r)` on the exceptional product of a balanced smooth rational degree-`e` curve, the new substitutions are correct:

`g=0`, `nu=(2e-1)r-1`, `h=er`.

When `e>=3` and `r>=2`, `nu>5` and `nu-h=(e-1)r-1>0`. The accepted criterion therefore gives an integral surface degree `1<=d<=r+1`. The function `(d-1)(d-2)` is nondecreasing on the positive integers, so the plane-adjunction lower bound would require

`e*r*(r-1) <= (d-1)(d-2) <= r*(r-1)`.

This is impossible. The all-orders exclusion for every `r>=2` is correct, with no claimed finite cutoff.

For `r=1` and `e>=4`, `nu=2e-2>5` and `nu>=h`; hence `d<=2`. A smooth rational plane curve has degree one or two by plane adjunction. Thus the given curve cannot lie in a plane, and the integral algebraic surface closure is a quadric `Q`.

The generic normal order `m` of `Q` along `C` is positive. Applying the imported plane inequality with `d=2` gives `0>=e*m*(m-1)`, hence `m=1`. The strict transform is therefore Cartier of class `2H-E`, whose restriction to `E` is `(1,1)`. This restriction is effective and contains the given integral `(1,1)` root `Z`. Their difference is an effective linearly trivial divisor on `P1 x P1`, hence zero: a global section of its trivial associated line bundle is a nonzero constant. Consequently `W|E=Z` as Cartier divisors, not only as supports.

At every point of `Z`, reduction of a local equation of `W` modulo an equation of `E` is a regular local parameter of the smooth surface `E`. Thus `W` is smooth and transverse to `E` there. Its smooth completed germ has only that one branch, so the original formal Cartier ideal equals the strict-transform ideal near `Z`; both ideals are units away from `Z` on `E`. This justifies the asserted equality on the whole completion along `E`.

The remaining smoothness and converse statements also pass. The ordinary first symbol of `Q` defines the normal derivative map

`N_C -> O_C(2)`.

Under `N_C=O_P1(2e-1)^2`, its two coefficients are sections of `O_P1(1)`. A simultaneous zero would give an entire exceptional fiber in `W|E`, impossible because `Z` is finite over `C`. They are therefore nowhere simultaneously zero, which is equivalent to `Q` being smooth along `C`.

Conversely, if a quadric contains `C` and is smooth along it, these two coefficients have no simultaneous zero. Two such degree-one sections are linearly independent, and their fiberwise linear zero locus is the smooth graph of a degree-one map `P1 -> P1`, of class `(1,1)`. The strict transform gives its compatible Cartier ideals on every exceptional neighborhood. Thus the converse supplies exactly the roots claimed in Section 5.

The degree boundaries are correctly retained: the `r>=2` exclusion assumes `e>=3`, whereas the `r=1` classification assumes `e>=4`. No conclusion for the omitted degree-three, order-one case is inferred. This audit does not import finite-jet rigidity for `C0`, enlarge the actual-CI bridge, or establish any finite cutoff.
