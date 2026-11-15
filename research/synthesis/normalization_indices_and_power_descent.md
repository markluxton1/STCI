# Normalization indices and actual power descent

**Scope and status.** Independently reviewed results and constructions,
retained from the fixed source cutoff `8e9a87a`. Work
over an algebraically closed characteristic-zero field. The normalization
index and the failure of a section to descend are separate data. The actual
affine and projective pairs below realize arbitrary index and power descent;
they do not realize the fixed quartic on a quintic carrier.

The general necessary lemma concerns an actual proper intersection with sole
smooth reduced support. The local line and global plane-curve constructions
show why its numerical conditions cannot alone be an obstruction. They also
have value as explicit supported multiple structures with singular carriers.

## A normalization-index constraint for any smooth support

Let C be any smooth integral projective curve of degree d. Suppose an integral
degree-a surface S in P3 is smooth at the generic point of C and has an actual
degree-b mate with sole reduced intersection support C. Let
`nu:X->S` be its finite normalization and `H=nu*O_S(1)`.

There is a unique inverse curve c over C, and c maps isomorphically to C.
Indeed, normalization is an isomorphism at the generic point, so c->C is
finite birational. Its integral coordinate rings inside k(C) equal those of
the normal curve C. Any other point of the full reduced inverse image would
be isolated from c. Pulling back the actual mate gives a nonzero effective
Cartier divisor on the normal surface X, whose support is pure codimension
one. Thus there are no such extra points and

    (nu^-1 C)_red=c,  div(nu*G)=m c ~ bH,
    H^2=a,  H.c=d,  m=ab/d,  c^2=d^2/a.                 (1)

The last square is the rational Cartier self-intersection: mc is Cartier.
Let r be the global Cartier index of c: the least positive integer for which
rc is Cartier, equivalently the order of [c] in Cl(X)/Pic(X), not in Cl(X). Then

    r divides m,   a/gcd(a,d^2) divides r.                (2)

For the second assertion, the Cartier divisor rc restricts to a line bundle
on the smooth curve c, so `(rc).c=r*d^2/a` is an integer. In particular,
if a does not divide d^2, the normalization must be singular at some point
of c. This argument does not assume a Gorenstein or smooth normalization.

For the fixed quartic and a quintic–octic pair, (1)–(2) become

    10c~8H,  H^2=5,  H.c=4,  c^2=16/5,  r=5 or 10.      (3)

At least one local index along c is divisible by five. This is a necessary
singularity constraint, not an exclusion. In arbitrary degree it explains
why a smooth normalization cannot be an adequate source whenever the
carrier degree fails to divide the square of the curve degree. It does not
apply to a carrier singular at the generic point of C.

## The order-two class and the conductor descent order

In (3), let `U=5c-4H` in Cl(X). The actual octic proves `2U=0`.
Unlike the normal-carrier argument, U need not be nonzero: an upstairs
quartic section need not descend to S.

If U=0, there is a regular section `q in H^0(X,4H)` with divisor 5c.
Its square is, up to a nonzero scalar, the pulled-back octic section: their
divisors agree, and their ratio is a global unit on integral projective X.
The section q cannot descend to S, since hypersurface section lifting would
then supply a forbidden ambient quartic mate. Its square must descend.

If U has order two, its nontrivial reflexive class defines a connected
normal double cover of X, etale in codimension one, on which U trivializes.
Nothing here proves that its singularities are ADE, that its smooth
resolution is minimal of general type, or that the root descends through
the original conductor. The preceding ADE surface inequalities cannot be
imported on the basis of this torsion relation alone.

Equivalently, R-0003's singleton formula has least mate degree `4tE`,
where t is the order of U and E the full-conductor descent order of its
primitive section. Existence of degree eight gives `tE|2`; the accepted
degree-four exclusion removes tE=1. Thus the two possibilities are
`(t,E)=(2,1)` and `(1,2)`. This statement uses the lower-degree exclusion
in addition to the degree formula.

This split alone restates necessary data. Its research value depends on
computing the root's failure to belong to the actual ambient section image,
or proving a restriction on that failure. It is not an additional exclusion.

### The reflexive double cover is already normal


In the exact setup of the integrated note, the reflexive algebra is already
normal; normalization is not needed. Let `L=O_X(U)`, with a chosen
isomorphism `L^[2]≅O_X`, and form

    A=O_X⊕L

using the induced reflexive multiplication. Since both summands are reflexive,
they are `S2` as `O_X`-modules. The nontrivial class remains nontrivial on the
regular locus of the normal surface, so the associated degree-two algebra
there is a connected finite étale cover. Its generic algebra is therefore a
field, making `A` a domain. The finite map `Spec(A)→X` is étale at every
codimension-one point, so `A` is regular in codimension one. The `S2` module
depth gives `S2` for this finite domain (local dimensions agree under the
integral extension), and Serre's criterion gives normality. Thus the
integrated note's claim of a connected normal quasi-étale double cover is
supported for this construction.


This construction supplies no ADE classification, minimal resolution type or
descent through the original conductor. Those are additional conditions.

## Actual supported pairs with independent index and power descent

Over an algebraically closed field of characteristic zero, choose integers
`r>=2` and `ell>=2`. Put

    A=k[a,y,z]/(a*y^ell-z^(r*ell)),
    B=k[x,y,z]/(x*y-z^r),       a=x^ell.                  (4)

The binomial defining A is primitive and linear in a, hence irreducible.
The inclusion into B is finite because x is integral with `x^ell=a`, and
birational because `x=z^r/y` in the common fraction field. B is normal:
it is the A_(r-1) hypersurface, regular off the origin and Cohen–Macaulay.
Thus B is the finite normalization of A.

The smooth curve `C=(a,z)` has full reduced inverse `c=(x,z)`, both equal
to the y-axis, and the inverse curve maps isomorphically. The full inverse
scheme can be nonreduced; it is not being identified with c. On B,
`div(x)=r c`. The local Cartier index at the origin is r. One direct local
check is that, for `1<=n<r`, the symbolic ideal of nc is `(x,z^n)`, with
two minimal generators at the origin, whereas rc is principal.

The actual ambient pair is

    (a*y^ell-z^(r*ell), a)=(a,z^(r*ell)),                  (5)

so it has sole reduced support the smooth y-axis and generic length r*ell.
The principal Cartier divisor (a) has associated cycle r*ell C; this
notation does not assert that the reduced curve C is Cartier on Spec A.

The power descent and entire conductor are exact:

    x^j belongs to A iff ell divides j,
    (A:B)=y^(ell-1)B.                                    (6)

For a direct proof, embed B into k[u,v] with
`x=u^r,y=v^r,z=uv`. Its monomials have exponents `(p,q)>=0` with
`p=q modulo r`. A is generated by `(r*ell,0),(0,r),(1,1)`. If p>=q and
`d=(p-q)/r`, membership in A is equivalent to
`q>=r*((-d) mod ell)`, with residue between zero and ell-1; when q>=p,
all the B-monomials belong to A. In particular x^j belongs exactly when
ell divides j. Every monomial with `q>=r*(ell-1)` remains in A after
multiplication by any B-monomial. If q is smaller, multiplication by a
suitable x-power makes the required residue ell-1 and violates membership.
The monomial grading also rules out cancellation for a sum. This proves
the full conductor formula, including its nonreduced structure.

Geometrically, the reduced conductor curve upstairs is `(y,z)` and its
map to the downstairs conductor is `x -> a=x^ell`. Its origin meets c,
and the normalization fiber there is a singleton. Thus a ramified
conductor map, arbitrary local index r, and descent only after the ell-th
power coexist with an actual sole-supported local complete intersection.
At `r=5,ell=2`, the index-five and square-descent phenomena required by
one quintic–octic branch are locally compatible.

This is a positive control against an obstruction based only on those
indices. It does not construct the fixed quartic or a degree-five carrier.

### An ordinary projective example with a marked line

In standard P3 with coordinates `[a:y:z:w]`, take

    F=a*y^ell*w^(r*ell-ell-1)-z^(r*ell),   G=a.           (7)

The exponent is positive for r,ell>=2. F is homogeneous of degree r*ell
and irreducible by the same primitive linear-in-a argument. The actual
intersection is `V(a,z^(r*ell))`, supported on the smooth line `a=z=0`.
The chart w=1 recovers (4)–(6) at `[0:0:0:1]`. This is a global standard
projective construction, but with carrier degree r*ell and plane mate.
For r=5,ell=2 it is a degree-ten carrier and has a line as support. Its
effect on the main question is to locate the missing constraint in the
fixed embedding and global section degrees, not in abstract index or
conductor-power compatibility.

### Global descent in an integral hyperplane twist

The line example does not require the non-descending root to belong to an
integral multiple of the hyperplane bundle. The following construction does.
Choose integers `ell>=2,n>=1,r>=n+1`, and put `s=r-n-1`. In the plane
with coordinates `[X:Y:W]`, take a smooth irreducible degree-ell*n form G
whose curve meets Y=0 transversely away from W=0 and has neither Y nor W
as a factor. For example `G=X^(ell*n)+Y^(ell*n)+W^(ell*n)` works in
characteristic zero. In ordinary P3 with coordinates `[X:Y:Z:W]`, set

    F=G*Y^ell*W^(ell*s)-Z^(r*ell).                        (7a)

This is an integral degree-r*ell surface: as a polynomial in Z, F is
Eisenstein at the prime G in k[X,Y,W]. Its intersection with the actual
degree-ell*n mate G is the scheme `V(G,Z^(r*ell))`, with sole support the
smooth plane curve `C=V(G,Z)`. The surface V(G) is smooth along C, so this
is also an actual primitive multiple curve along the entire C.

Let nu be the finite normalization of V(F), with pulled hyperplane H.
The carrier is smooth at the generic point of C. The purity argument of
[the full inverse-support lemma](#a-normalization-index-constraint-for-any-smooth-support)
therefore supplies the full singleton inverse curve c isomorphic to C,
including the projective boundary. The rational section

    q=Z^r/(Y*W^s) of nH,       q^ell=nu*G,                (7b)

is regular on the normalization. In every local H-frame its coefficient
satisfies a monic equation with regular coefficients, so normality removes
all apparent denominator poles, including those at W=0. Thus
`div(q)=r c` and rc is Cartier globally.

At any transverse point C intersect Y=0 with W nonzero, the local
coordinates `(a=G,y=Y,z=Z)` identify this construction with (4), up to
an invertible factor removed by an ell-th root. The local normalization
index is exactly r, hence the global index of c is exactly r. The same
local calculation gives q^j non-descending whenever ell does not divide j;
when ell divides j, it is a power of the actual ambient section G. Therefore

    q^j descends globally iff ell divides j.              (7c)

For `ell=2,n=1,r=5`, this gives the explicit pair

    G=X^2+Y^2+W^2,
    F=(X^2+Y^2+W^2)*Y^2*W^6-Z^10.

It has a smooth conic as sole support, an integral degree-ten carrier,
normalization index five, and a regular section `q in H^0(H)` whose square
is the ambient quadratic mate but which does not itself descend. This
demonstrates the global square-descent mechanism in an integral hyperplane
twist. The support is a conic and the pair has degrees (10,2); it is not a
fixed-quartic or quintic–octic construction.

There is an exact limitation on using this pattern to absorb residual
components. For arbitrary forms F0,G,A with the required equal degrees,

    (G*A^ell-F0^(r*ell), G)=(F0^(r*ell),G),
    radical(G*A^ell-F0^(r*ell),G)=radical(F0,G).           (7d)

Consequently this operation retains every pre-existing residual component.
It can manufacture useful singular carriers for a curve already cut out
set-theoretically, but it cannot turn a containing pair into sole support
by changing the carrier in this way. No irreducibility assertion is needed
for this ideal identity.

## An actual section-image condition on the marked quintic source

The [quintic carrier-structure proof](quintic_conductor_geometry.md#1-quintic-conormal-and-delpezzo-audit)
already proves a stronger useful reduction than the elementary denominator
[normalization-index test](#a-normalization-index-constraint-for-any-smooth-support). For a hypothetical nonnormal quintic with **Gorenstein
normalization**, the general hyperplane genus must be one. That normalization
is the degree-five del Pezzo surface with a single A4 point, `K_X=-H`;
c meets an interior A4 vertex and `5c~4H`. This is inherited evidence,
not a newly proved classification of arbitrary nonnormal quintics.

The exact marked pair and actual projection parameters are in the
[intrinsic classification](quintic_octic_ade_cover_and_triple.md#1-dp5-a4-intrinsic-pair-classification)
and [explicit-model audit](quintic_octic_ade_cover_and_triple.md#2-dp5-a4-explicit-model-independent-audit).
Its actual normalization conductor is `O_X(-2H)`. The downstairs conductor
Gamma has degree five and arithmetic genus two, and

    nu_*O_X/O_S = omega_Gamma(-H).                         (8)

No smoothness, reducedness, or globally finite-flat double-cover structure
for the conductor is inferred from those degree and genus numbers.

On the complete open affine chart `X minus ell=A2(r,T)`, the quartic root
q is exactly T^5 in the chosen H-frame. The actual four projection sections
are recorded in
[the actual target-fiber equations](quintic_conductor_geometry.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions).
Thus a degree-eight mate would require the **exact section-image condition**

    T^10 in span_k{ X0^i0 X1^i1 X2^i2 X3^i3 : sum ij=8 }. (9)

Under an actual basepoint-free finite birational degree-five projection,
(9) is equivalent to the square q^2 descending as an ambient octic. If
its divisor is 10c, surjectivity of normalization then proves sole support
C downstairs. Checking a rational chart polynomial identity is sufficient
for equality of the global sections in question; projection admissibility
still must be checked separately.


The exact section-image test retains center avoidance and finite birationality.
It is not inferred from the divisor numbers alone. The later
[complete Gorenstein-normalization quintic theorem](quintic_gorenstein_normalizations.md)
closes that source using additional conductor geometry, not an unfinished
section-image computation. Other normalizations and other embedded supports
are not classified by these examples.

## Characteristic and review boundary

The constructions and the reflexive-cover statement here retain their
characteristic-zero hypotheses. In particular their chosen roots of unity,
root extraction and quasi-etale double-cover discussion are not asserted
unchanged in wild characteristic. The normalization/index proof assumes
smooth support and generic regularity of the carrier; generic singularity
along the support lies outside it.

The frozen independent audit reconstructed the full inverse-support and
index argument, the torsion-versus-descent alternatives, monomial conductor
calculation, actual local and projective intersections, and the integral-
hyperplane-twist extension including its residual-preservation identity.
The double-cover argument above incorporates that audit's complete
normality proof. The Gorenstein A4 source remains an inherited scoped input.
No new computation or projective fixed-quartic construction is claimed.

These examples do not globalize to the fixed quartic by choosing only a
binomial carrier: the characteristic-zero one-binomial obstruction for
that embedding retains its separate scope in
[arithmetic equations and jet gaps](arithmetic_root_collision.md#arithmetic-degree-bounds-missing-jets-and-actual-non-binomial-equations).
The plane-curve construction and residual-preservation identity above
locate the missing input in actual support and homogeneous section images.


## Consolidated historical supplement: `research/supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md`

Proofs and qualifications are retained here, with cross-references where the full filtered compatibility audit supplies the same argument.

# Normal carriers: class-group torsion, symbolic triples and local indices

## Integration guide: class-group torsion, index bounds, and the mate problem

The [carrier torsion investigation](#2026-10-14-generalization-normal-carrier-torsion) distinguishes Cartier and Weil divisor information on possibly singular normal surfaces. The [symbolic-triple certificate](#2026-10-14-generalization-normal-carrier-symbolic-triple-certificate) adds a specific primitive structure and first torsion divisor; its [comparison audit](#2026-10-14-generalization-symbolic-triple-torsion-comparison-audit) tracks the cases of different Cartier indices and the scope of strengthened bounds.

The related [normal-index and socle dossier](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-normal-index-general-scope) records inequalities that do not presuppose a second equation. The [Rees cycle dossier](../synthesis/rees_and_vertical_controls.md) makes clear why a global degree budget alone does not control every filtered defect.

The three proof responsibilities are separate. Global Pic/Cl detection
identifies torsion orders through actual local indices using a connected
cyclic cover. The symbolic-triple arguments compare a pure symbolic
quotient with actual Cartier multiples, without assuming that quotient is
a complete intersection. The ordinary-lattice and filtered-compatibility
arguments use free layers and Frobenius duality on the actual local CI
algebras; their pointwise costs feed the bounded-index exclusions. These
full arguments are retained in their respective sections, rather than
replaced by the neighboring normal-index budget.

A normal carrier's symbolic divisor data is **not** by itself a construction of a set-theoretic complete intersection. The local index, actual homogeneous lifting, and residual-support questions remain distinct.

---

Permanent mathematical dossier. Complete source arguments are preserved with their precise hypotheses, conditional scope, calculations, failed approaches, and unresolved boundaries.

---

<a id="2026-10-14-generalization-normal-carrier-torsion"></a>
## Normal carriers: global torsion is exactly the local index obstruction

Date: 2026-10-14. Author: `conductor_general`.
Status: **NEW PROVED STRUCTURAL RESULTS AND CONDITIONAL ALL-DEGREE
EXCLUSIONS; independent new-proof audits recorded below.**

Accepted input, not recomputed: the fixed characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]` has no integral carrier of degree at most four
with a mate of any positive degree. The
[Cartier-ray theorem](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md)
is also an accepted input for this continuation. No claim is made
that all normal carrier classes have now been excluded.

### 1. Immediate torsion-free class-group exclusion

Let `X subset P^3` be a normal integral surface of degree `a`, containing
`C0`, over an algebraically closed characteristic-zero field. Put

```
g = gcd(a,4),  mu = a/g,  v = 4/g,
Delta_0 = mu[C0] - v[H] in Cl(X).
```

Normality makes the carrier generically regular along `C0`, so a mate
of degree `b` has divisor `m C0` and intersection gives `4m=ab`.
Thus every possible pair is `(m,b)=k(mu,v)`. A mate exists on `X`
if and only if `Delta_0` is torsion; if its exact order is `t`, the
mate degrees on `X` are exactly

```
b = k t v,  k=1,2,3,... .
```

There is no normalization/conductor factor, since `X` is normal.
The effective divisor realizing the first relation gives a section
of `O_X(tv)`, which lifts to an ambient form by the hypersurface
sequence and `H^1(P^3,O(tv-a))=0`.

If `Cl(X)` is torsion-free, then `Delta_0=0`; it gives a mate of
degree `v<=4`. That mate is itself an integral carrier of `C0` only
after passing to an irreducible factor: some factor of its defining
form vanishes on the integral curve, and its degree is at most four.
Its intersection with `X` still has support exactly `C0`, because
the factor's intersection is contained in the full mate's support.
The factor cannot divide the equation of the distinct integral
carrier `X`; hence it gives an STCI presentation with an integral
carrier of degree at most four. This contradicts the accepted input.

**Therefore no normal integral carrier with torsion-free `Cl(X)` can
occur, in any carrier degree.** The same factor argument excludes
any mate of degree at most four, regardless of the degree of `X`.

Every normal survivor must have nonzero torsion `Delta_0`, with

```
t >= 2 if g=1;  t >= 3 if g=2;  t >= 5 if g=4.
```

These are exclusions based on an existing hypothetical mate, not a
claim that a torsion class exists on arbitrary normal hypersurfaces.

### 2. A self-contained rational-ample local detection theorem

**Theorem.** Let `X` be a normal integral projective surface over an
algebraically closed field of characteristic zero. Let `C subset X`
be a smooth rational prime curve for which some positive multiple
`m C` is an ample Cartier divisor. Then localization gives an
injection

```
Tor Cl(X) -> product_{P in C} Cl(O_X,P).
```

More precisely, the order of any torsion Weil class `T` is exactly
the least common multiple of its local class orders at points of
`C`. Only finitely many singular points can contribute.

The hypothesis on `C` is satisfied by a mate: if `div(G)=m C` on a
projective hypersurface, then `O_X(m C)=O_X(b)` is ample. No claim
that reduced `C` itself is Cartier is used.

#### Proof by a connected cyclic cover

First suppose a torsion class `T` is Cartier at every point of `C`,
and let its exact order be `t>1`. Choose a representing Weil divisor
`D` and a rational function `f` with `div(f)=tD`. Form the cyclic
cover associated with a `t`-th root of `f`, taking the normalization
in that function-field extension.

The extension has degree exactly `t`. Indeed, since the ground
field contains all roots of unity, a reducible Kummer polynomial
`Z^t-f` would make `f` a `p`-th power for some prime `p|t`. The
equality of divisors would then make `(t/p)D` principal, contradicting
the exact order of `T`. Thus the resulting finite normal projective
surface `Y` is integral and connected. Finiteness of normalization
holds for varieties over a field.

Equivalently, this is the standard reflexive cyclic algebra built
from the powers of `O_X(D)`. In codimension one it is an unramified
Kummer cover: the valuations of `f` are divisible by `t` and `t` is
invertible. Thus it is quasi-etale. Wherever `D` is Cartier, the
reflexive sheaf is an actual line bundle and its torsion
trivialization defines a finite etale `mu_t`-torsor. Since `D` is
Cartier at all points of `C`, the cover is finite etale on a
neighborhood of `C`.

Its restriction over `C=P^1` is a finite etale cover of degree `t`.
Such a cover is the disjoint union of `t` copies of `P^1`: for each
connected component, Riemann--Hurwitz for an unramified separable
cover gives `2g-2=-2d`, forcing `d=1`. Therefore the support of
`pi^*(m C)` is disconnected.

On the other hand, `pi^*(m C)` is an ample effective Cartier divisor
on the normal integral projective surface `Y`. Its support must be
connected. Here is a direct proof retaining the possibly singular
surface. A normal surface is Cohen--Macaulay and has a dualizing
sheaf. For an ample effective Cartier divisor `A`, Serre duality
and Serre vanishing give, for all sufficiently large `n`,

```
H^1(Y,O_Y(-nA)) = H^1(Y,omega_Y(nA))^* = 0.
```

Since `H^0(Y,O_Y)=k` and `H^0(Y,O_Y(-nA))=0`, the exact sequence
of `nA` gives `H^0(nA,O_{nA})=k`. Disconnected support would give a
nontrivial idempotent and at least two independent global sections,
a contradiction.

Hence a torsion class Cartier along `C` must be zero. Now let `T`
have order `t`, and let `h` be the least common multiple of its local
orders along `C`. Each local order divides `t`, so `h|t`. The class
`hT` is Cartier at every point of `C`; Cartierness is open, so it is
Cartier on a neighborhood of `C`. It is torsion and therefore zero
by the preceding argument. Thus `t|h`, and `t=h`.

This proof does not use simple connectedness of the entire surface,
the Picard group of a hypersurface, or smoothness of `Y`. In positive
characteristic the same proof applies to torsion of order prime to
the characteristic. No assertion about wild `p`-torsion follows.

### 3. Exact index formula on every normal `C0` carrier

Assume a mate on a normal degree-`a` carrier exists. For
`P in C0 intersect Sing(X)`, put

```
r_P = order([C0] in Cl(O_X,P)),
R   = lcm_P r_P,
```

with an empty least common multiple equal to one. These local
Cartier indices are finite, because the mate makes a positive
multiple of `C0` Cartier. The local class of `Delta_0` is
`mu[C0]`, since `H` is Cartier. Consequently its local order is

```
q_P = r_P/gcd(r_P,mu).
```

The theorem of section 2 applies because the hypothetical mate makes
a multiple of `C0` ample. It therefore gives

```
t = lcm_P q_P = R/gcd(R,mu),
b_min = v R/gcd(R,mu).
```

The equality between the least common multiple and the last quotient
follows prime by prime: the valuation is
`max(0,max_P ord_l(r_P)-ord_l(mu))`.

**There is no additional invisible global torsion factor.** The
entire order of the primitive normal-carrier class is detected by
the Cartier indices of the smooth curve at the singular points it
actually meets.

This is a necessary formula under existence of a mate. Finite local
indices alone do **not** prove that `Delta_0` is globally torsion:
its residual Cartier class can still have infinite order. One must
not invert this implication without a separate global relation.

### 4. Cartier-index integrality and new all-degree exclusions

The global Cartier index of `C0` is exactly `R`: a Weil divisor on
a normal surface is Cartier if and only if it is Cartier at every
point, and its local classes are already zero at the regular points
and away from its support. Hence `R C0` is an actual Cartier divisor.
Under a hypothetical mate, `C0` is numerically `(4/a)H` and

```
C0^2=16/a,
deg(O_X(R C0)|C0) = 16R/a in Z.
```

The latter degree is integral because `O_X(R C0)` is an actual line
bundle restricted to the smooth projective curve. Therefore

```
a divides 16R.
```

This is separate from the torsion order `t` of `Delta_0`: the global
Cartier index of the curve is `R`, whereas `t=R/gcd(R,mu)`. Keeping
those two integers distinct avoids a false divisibility claim.

#### Index-dividing-degree exclusion

If every local Cartier index of `C0` divides the carrier degree
`a`, then `R|a=g mu`, hence

```
R/gcd(R,mu) divides g.
```

Under a hypothetical mate, the exact index formula gives
`b_min = (4/g)t <=4`, contradicting section 1. Therefore:

**No normal integral carrier of any degree can admit a mate if all
local Cartier indices of `C0` divide its degree.**

It suffices that the actual indices divide `a`; the full local
class groups need not be finite or have exponent dividing `a`.

#### Ordinary nodes along `C0`

At an ordinary double point in characteristic zero, the completed
surface local ring is `k[[x,y,z]]/(xy-z^2)`, whose class group is
`Z/2`. Thus the local index of any Weil curve divides two. The same
bound holds in the algebraic local ring: if the completed reflexive
module becomes invertible, faithful flat descent makes the original
module invertible. This concerns points on `C0`; singularities
elsewhere do not enter the index formula.

For even `a`, every contributing index divides `2|a`. The preceding
all-degree theorem therefore proves:

**Every even-degree normal carrier whose singular points on `C0`
are ordinary nodes is excluded.** Its singularities away from `C0`
can be arbitrary normal surface singularities.

For odd `a`, `g=1` and `mu` is odd. The exact order divides two.
Before using integrality, its only possible nontrivial torsion order
is two and its first mate degree would be eight. But `R<=2` gives

```
a divides 16R divides 32.
```

No odd `a>=5` divides 32, and the smaller carrier degrees are already
excluded. Combining this with the even-degree argument proves:

**Every normal carrier whose singular points on `C0` are ordinary
nodes is excluded, in every carrier degree and every mate degree.**
Its normal surface singularities away from `C0` remain unrestricted.
This is a new structural closure; it is not a rerun of an old
degree-by-degree nodal certificate.

#### A bounded-index carrier class

More generally, if all local indices divide a fixed integer `L`,
then under a mate

```
t divides L/gcd(L,mu),
b_min <= (4/g) L/gcd(L,mu).
R divides L,  a divides 16R,  hence a divides 16L.
```

Thus a carrier class with bounded local index exponent has both a
uniform mate-degree bound and a **finite list of possible carrier
degrees**. Retain only divisor pairs

```
R|L,  a|16R,  a>=5,
(4/g) R/gcd(R,a/g) > 4.
```

Elementary exact divisor arithmetic gives:

| Common bound `L` on local indices | Surviving `(a,R,t,b_min)` |
| --- | --- |
| 2 | none |
| 3 | none |
| 4 | none |
| 6 | none |
| 12 | `(6,12,4,8)` and `(8,12,6,6)` |

For `L=12`, the possible `R` are `1,2,3,4,6,12`. The first five
give no survivor. For `R=12`, the carrier degrees at least five
dividing 192 are
`6,8,12,16,24,32,48,64,96,192`; their respective first mate degrees
are `8,6,4,3,2,3,1,3,1,1`. Only the first two exceed four.
The corresponding elementary calculation is preserved in
`research/computations/normal_carrier_index_reduction_2026_10_14.py`.

Consequently all normal carrier classes with on-curve local indices
dividing `2`, `3`, `4` or `6` are excluded across all degrees.
For indices dividing 12, all degrees reduce to just the carrier/mate
pairs `(6,8)` and `(8,6)`, with actual global curve index `R=12`.
The first mate degree refers to the minimal mate on that chosen
carrier; no existence of either pair is asserted.

The two rows give the **same unordered defining degree pair `(6,8)`**.
A minimal mate form is integral: if it had a proper irreducible
factor vanishing on the integral curve, that factor would be a mate
on the same carrier of smaller degree, contradicting minimality.
The resulting complete-intersection scheme has generic multiplicity

```
(6*8)/deg(C0)=12
```

along `C0`. Thus the entire normal-carrier class with on-curve
indices dividing 12 collapses to this one degree pair and one
generic multiplicity, retaining the true possibility of simultaneous
singular points and nonprimitive structures. At least one defining
surface has the normality and index hypotheses; normality of the
other defining surface is not inferred.

For context, the detailed primary class-group tables in
Brevik--Nollet, Sections 4.1.1--4.1.3, give exponents two or four for
`D_n`, three for `E6`, two for `E7`, and one for `E8`. Thus all
`D/E` rational-double-point singularities along `C0` have indices
dividing 12 and lie in this two-pair reduction. So do mixtures with
`A1,A2,A3`. Primary source:
[*Local Picard Groups*](https://arxiv.org/pdf/1110.1867).
Use its detailed subsections: the introductory Section 4 summary
contains parity and `E6/E7` assignment errors which the detailed
subsections correct.

#### General integral curves, not just the rational quartic

The hypersurface Picard route in section 5 removes the rationality
hypothesis from the index formulas. Let `C` be **any integral**
degree-`e` projective curve on a normal degree-`a` hypersurface in
`P^3` over an algebraically closed characteristic-zero field, and
suppose it has a mate on that carrier. Put `g=gcd(a,e)` and let
`R` be the least common multiple of the actual local Cartier indices
of `C`. All those indices are finite by the mate. Then

```
Delta_0 = (a/g)[C] - (e/g)[H],
t = order(Delta_0) = R/gcd(R,a/g),
b_min = (e/g) R/gcd(R,a/g),
a divides e^2 R.
```

The first two formulas use the torsion-free Picard group and the
localization kernel; the last uses the integer degree of the actual
line bundle `O_X(RC)` restricted to the integral curve. Its numerical
degree is `R C^2=R e^2/a`. Degree of a line bundle remains an integer
on a possibly singular integral projective curve.

Consequently, if the actual on-curve Cartier indices all divide
`L`, then

```
a divides e^2 L.
```

Thus **a bound on local curve indices gives a finite carrier-degree
reduction for all integral curves**, in every mate degree. This does
not impose or prove such an index bound for unrestricted carriers;
it identifies precisely the new geometric invariant whose control
would turn the normal branch into a finite carrier problem.

### 5. Primary literature and the Pic/Cl distinction

The exact literature input inspected for projective hypersurfaces is
SGA 2, Expose XII, Corollary 3.5, printed page 120, PDF page 128 in
the recomposed edition. Applied to the ample hypersurface section
inside the regular threefold `P^3`, it identifies its etale
fundamental group with that of `P^3`. In characteristic zero the
Kummer sequence, and divisibility of the constant units, then give
`Pic(X)[n]=0` for every `n`. Thus **Pic(X) is torsion-free**.
Primary source: [SGA 2](https://wstein.org/sga/circle/SGA2.pdf).

For a normal surface, an elementary localization sequence has kernel
`Pic(X)` in

```
Cl(X) -> product_{P in Sing(X)} Cl(O_X,P).
```

Indeed a Weil class is locally trivial at all singular points
exactly when its reflexive sheaf is everywhere invertible. Hence,
with the preceding Picard theorem, localization is injective on
`Tor Cl(X)`. The class `Delta_0` is already Cartier away from `C0`,
so only singular points on `C0` contribute. This is an independent
standard-input route to the index formula. The relevant class-group
sequence is also present in Hartshorne--Polini, Proposition 2.2(c),
specialized to a normal surface; see
[*Divisors class groups of singular surfaces*](https://arxiv.org/html/1301.3222).

The new rational-ample cyclic proof in section 2 gives a broader
statement without assuming the Picard group of the whole surface
is torsion-free. It also makes the localization mechanism geometric.

Torsion-free `Pic(X)` does **not** mean torsion-free `Cl(X)`. A
Kummer quartic is the quotient of an abelian surface by its sign
involution, with sixteen isolated nodes. The connected double cover
is etale over the smooth locus. Its nontrivial order-two eigensheaf
there gives nonzero order-two torsion in `Pic(X_reg)=Cl(X)`; if the
eigensheaf were trivial, the cover would split, since units on the
smooth locus extend to constants on the normal projective surface.
The quotient description is documented, for example, in the primary
paper
[*Birational Geometry of Blow-ups of Projective Spaces Along Points
and Lines*](https://academic.oup.com/imrn/article/2021/9/6442/5930818).
This is a failure shield for the blanket assertion that normal
hypersurface class groups have no torsion. It does not supply a
counterexample to the accepted `C0` exclusions.

### 6. What the cyclic cover does and does not control

For a hypothetical `Delta_0` of exact order `t`, its cyclic cover is
quasi-etale, connected and must fail to be etale somewhere on `C0`.
Its degree is now determined exactly by the local index formula.
The pullback of the primitive relation becomes trivial:

```
mu pi^*C0 ~ v pi^*H.
```

This yields an upstairs section in degree `v<=4`, but the covering
surface maps to `X` with degree `t` and is not itself an embedded
surface in `P^3`. The accepted low-degree carrier exclusion cannot
be applied directly to this upstairs section. Its norm recovers a
degree-`tv` mate on `X`.

No contradiction follows merely from `K_Y=pi^*K_X`: for `a>=5`,
the covering surface can have ample canonical divisor just as the
base does. Likewise a cover can pull back the rational curve to
several components meeting over singular points. Local class order
is not automatically the ramification index of the normalization
of one curve component. A Riemann--Hurwitz argument must retain
that distinction.

There is also no bound on local index from smoothness of `C0` or
surface multiplicity alone. The local normal hypersurface

```
xy-z^r=0,   C=(x,z)=0
```

has multiplicity two, contains a smooth curve, and that curve's
local divisor class has order `r`. One may see this using the quotient
map `x=u^r,y=v^r,z=uv` from the smooth plane by
`(u,v)->(zeta u,zeta^(-1)v)`: the curve corresponds to the character
of exact order `r`. Its indices are arbitrarily large. This is a
local failure shield, not a constructed global `C0` carrier.

### 7. Audit record and successor target

The new rational-ample local detection proof was independently
reconstructed by `cyclic_cover_structure`, including Kummer
connectedness, etaleness near Cartier points, and ample-divisor
connectedness on a normal surface. `normal_torsion_primary`
independently inspected the exact SGA 2 hypersurface theorem and
the local class-group route, and audited the local-index and nodal
arithmetic corollaries. It also independently audited
`a|16R` and the full bounded-index divisor table. The new elementary
arithmetic script ran successfully and checked precisely the rows
displayed above. These audits concern new deductions, not a rerun
of accepted low-degree exclusions. The auxiliary proof records are
[normal cyclic-cover torsion detection](spectral_pushforward_powers.md#2026-10-14-normal-cyclic-cover-torsion-detection)
and [primary Picard/local-torsion inputs](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md#source-2026-10-14-normal-carrier-picard-local-torsion-primarymd).

The remaining normal-carrier target is now sharp: show that the
specific class `Delta_0` cannot be torsion with the required local
indices, or exclude the resulting finite cyclic cover geometry.
The nodal class is now closed across all degrees. More broadly,
on-curve local index exponents dividing `2,3,4,6` are closed, and
exponent 12 leaves only the unordered defining pair `(6,8)`, with
generic intersection length 12. The next exact target in this class
is compatibility of that full local length with the actual index
three/four contributions at the singular points; no primitive-pair
assumption may be imposed, and higher jets must be retained when a
`D_n` curve has index four but large singularity corrections. For
general normal carriers, one needs actual Cartier indices of the
smooth curve at the singular points it meets; multiplicity and the
carrier's Picard group alone are insufficient. All nonnormal and
entirely thick carrier lanes retain their separate conductor and
branch-lattice issues.

---

<a id="2026-10-14-generalization-normal-carrier-symbolic-triple-certificate"></a>
## A symbolic-triple defect certificate for unrestricted normal carriers

Date: 2026-10-14. Author: `socle_audit`.
Status: **PROVED NEW NECESSARY CARRIER-WIDE CERTIFICATE AND STRONGER
POINTWISE-INDEX/DEGREE BOUND.** The all-index-at-most-four exclusion and
the exact local power-socle formula are accepted inputs; they are not
reverified here. The present result does not exclude all normal C0
carriers or resolve C0's STCI status.

Accepted inputs: `2026-10-14-generalization-index12-filtered-compatibility.md`
for the ordinary-layer and local power-socle theorems; the existing
constant-direction pole obstruction for a first relation and its next
normal layer; the already verified C0 apolar kernels and their absence
of degree-zero/one annihilators; and N_C0^* = O(-7)^2. No old symbolic
calculation or accepted nonvanishing statement is rerun.

### 1. Carrier data and an intrinsic normalized budget

Let X = V(F_a) be a normal integral carrier of C0 in characteristic zero,
and suppose a mate G_b exists. Put n = ab/4. The generic CI algebra is
curvilinear. Let B_1 = O(-ell) be the torsion-free first ordinary normal
layer, equivalently the canonical quotient of N_C0^* by the saturated
first-symbol direction of F. Then ell <= 7. Let A_P be the carrier's
first-symbol vanishing order in that saturated line, and let r_P be
the actual local Cartier index of C0 on X. For a local equation h_P
with divisor r_P C0, write D_P^(r) for the full top-power/socle defect
of W_(r_P) = X/(h_P).

These are intrinsic carrier/curve data. Multiplication of h_P by a unit
does not change its local thickening or D_P^(r). Under the hypothetical
mate, r_P divides n, and the accepted exact local formula is

    D_P^(n) = (n/r_P-1)A_P + (n/r_P)D_P^(r).   (1)

The global degrees satisfy

    A = sum A_P = 4a-14+ell,
    D = sum D_P^(n) = (n-1)ell-4(a+b)+14,
    D+A = n(ell-16/a).

Adding A_P to (1), dividing by n, and summing gives the exact
mate-independent necessary relation

    Q := ell-16/a
       = sum_P (A_P+D_P^(r))/r_P.              (2)

In particular the normalized primitive-index defect is

    sum_P D_P^(r)/r_P
       = ell-16/a - sum_P A_P/r_P >= 0.        (3)

This is one simultaneous weighted budget. It neither replaces all
indices by their maximum nor treats distinct singular points as
independent hypothetical presentations.

### 2. Cartier multiples of length two or three are automatically primitive

There is a new useful general fact. A one-dimensional CI supported on
a smooth curve, finite free of generic rank r <= 3 over R = k[[t]],
with curvilinear generic algebra, is primitive everywhere locally.

Its special fiber is a local Artinian CI of length r. An Artinian CI
of embedding dimension two has both defining orders at least two,
and therefore length at least four. Thus the length-two/three special
fiber is curvilinear. Lift a generator z of its maximal ideal. Nakayama
shows that the relative nilradical J is generated by z; purity gives
J^r = 0. The induced surjection R[z]/(z^r) -> A is a map between finite
free R-modules of rank r and is an isomorphism.

Consequently, for actual indices two or three,

    W_r = R[z]/(z^r),
    D_P^(r) = 0.                              (4)

For r=1 the carrier is smooth at P and the same conclusion holds with
the reduced-curve conventions. Thus positive primitive-index defects
can occur only at actual indices at least four. This fact uses lengths
and a relative algebra argument, not a list of Hilbert profiles.

### 3. The global symbolic triple and its first torsion divisor

Suppose ell = 7. The saturated carrier direction is then constant:
the quotient O(-7)^2 -> O(-7) has constant coefficients. Let m be its
fixed first relation and let

    Z_3 = O_X / I_(C0/X)^(3)

be the global symbolic triple. It is pure of dimension one: the
divisorial symbolic ideal is reflexive on the normal surface and has
depth two, so its quotient has depth one. Its generic length is three,
and its ordinary free first layer is the same saturated O(-7).

Let E be the effective divisor measuring its first ordinary layer
torsion. The first actual initial-relation sheaf is

    K_1(Z_3) = O(-7)(-E) tensor k m.           (5)

Its degree-two relation sheaf has rank two and generic span mV. It is
contained in the saturated constant bundle O(-14) tensor mV by generic
vanishing in the torsion-free ambient quotient. Thus precisely the
hypotheses of the accepted constant-direction relation/pole obstruction
apply: rank K_1 = 1, rank K_2 = 2, constant generic first relation, with
the entire divisor E retained.

The resulting necessary condition is

    h_E h_m = 0 in H1(O(deg E-7)).             (6)

The accepted apolar kernels have no nonzero annihilator of degree zero
or one. Therefore

    deg E >= 2.                               (7)

No lci or Gorenstein assumption is placed on Z_3. Those hypotheses are
needed for the local W_r Frobenius identity used below, not for the
first-relation obstruction. In particular the symbolic triple at an
index-two point is generally not a complete intersection.

### 4. Exact index-two periodicity and comparison at higher indices

At an index-two point choose h with divisor 2C. Normal divisorial
valuations give the exact symbolic periodicity

    I_C^(j+2) = h I_C^(j),
    in particular I_C^(3) = h I_C.             (8)

An ambient lift of h belongs to I_C. Hence h I_C has zero first normal
symbols. The symbolic triple's first relation module is exactly the
carrier image R F_1. Its saturation is the fixed line R m. Therefore

    E_P = length(Rm / R F_1) = A_P,  r_P=2.    (9)

This equality retains the actual first-symbol vanishing order A_P and
all higher carrier complexity. From (4), its length-n defect is also
exactly D_P^(n) = (n/2-1)A_P.

For r_P >= 3, the local Cartier multiple W_r surjects onto Z_3 because
h belongs to I_C^(3). Their first relation modules in the same ambient
conormal module V = R^2 satisfy

    M_r subset M_3 subset V.

Both saturate to the same generic carrier relation line L subset V.
Their first-layer torsion modules are consequently L/M_r and L/M_3,
and the first maps onto the second. The accepted pointwise Frobenius
identity for the actual CI W_r gives

    0 <= E_P <= length T_1(W_r)_P
             <= (r_P/2)D_P^(r).              (10)

This direct quotient-of-relation-modules proof avoids any assumption
that the symbolic triple is lci. At r=3, (4) improves (10) to E_P=0.
At r=1 the carrier is smooth and E_P=0 as well.

Combining (7), (9), and (10) gives the new simultaneous certificate

    2 <= deg E
      <= sum_(r_P=2) A_P
          + (1/2) sum_(r_P>=4) r_P D_P^(r).    (11)

Thus every constant-direction normal carrier must have either index-two
contributions or nonzero full primitive-index socle defects at indices
at least four. Index-three contributions are automatically primitive
and cannot clear this first symbolic-triple obstruction.

If no index-two point occurs, at least one D_P^(r)>0. This is also seen
geometrically: if all the W_r were primitive, the symbolic triple would
be primitive everywhere by saturation, with constant first direction,
contradicting the accepted quadratic obstruction.

### 5. Weighted and parity-sensitive forms

The accepted pointwise Frobenius identity gives

    r_P D_P^(r) = 2 sum_i length T_i(W_r)_P.

Thus positive D_P^(r) is at least one for even r_P, and at least two
for odd r_P. If index two is absent, (3) and (11) force

    sum_P D_P^(r)/r_P
      >= min_(actual r_P>=4)
           { 1/r_P if r_P even; 2/r_P if r_P odd }.  (12)

Equivalently, with k_P = n/r_P,

    sum_P k_P D_P^(r)
      >= min_(actual r_P>=4)
           { k_P if r_P even; 2k_P if r_P odd }.     (13)

The more precise first-torsion comparison is

    sum_(r_P>=4) (2n/r_P^2) E_P
       <= sum_P (n/r_P)D_P^(r).               (14)

For an index bound s and no index-two points, (12) is at least 1/s
when s is even and at least 1/(s-1) when s is odd >=5. If all indices
are odd, it is at least 2/s. The s<=3/no-index-two case is impossible
because all Cartier multiples are primitive by Section 2; it is not
a surviving model with a small positive defect.

These are carrier-wide rational and integral certificates. They retain
each r_P and its full D_P^(r), including high D_n corrections at fixed
index. The actual positive term cannot be manufactured by tangent-only
multiplicity reasoning.

### 6. A stronger all-carrier-degree index bound

Let s >= 3 be a bound on every actual on-curve local index. For ell=7,
put A = 4a-7. From (2),

    Q-A/s
      = sum_P A_P(1/r_P-1/s)
          + sum_P D_P^(r)/r_P.                (15)

If any primitive-index defect is positive, the second sum is at least
1/s. If all such defects vanish, (11) forces
A_2 := sum_(r_P=2)A_P >= 2. Then the first sum is at least

    A_2(1/2-1/s) >= (s-2)/s >= 1/s.

Both cases therefore give

    s(7-16/a) >= 4a-6,
    4a^2-(7s+6)a+16s <= 0.                    (16)

This improves the previous coefficient-seven bound by a full unit,
even when index-two points are present. For ell <= 6, the earlier
accepted slope/index inequality is already stronger: monotonicity in
ell yields

    4a^2-(6s+8)a+16s <= 0.

Subtracting (s-2)a shows that it implies (16) for s>=2. Thus (16)
holds for every hypothetical normal C0 carrier of degree a>=5, with
actual indices bounded by s>=3, regardless of ell or mate degree.

In the constant-direction branch with no index-two point, (12) can
improve (16) further by replacing the one-unit payment with s times
the parity-sensitive lower bound. For all odd indices, for example,

    4a^2-(7s+5)a+16s <= 0.                    (17)

The already accepted s<=4 closure is not reverified here. Equations
(16)--(17) are new structural consequences for larger index classes,
and do not themselves exclude unbounded indices.

### 7. Apolar support constraints, not only a scalar payment

The actual divisor E must satisfy (6), not merely have degree at least
two. The accepted apolar kernel description therefore also gives:

* If deg E=2, the constant direction is an endpoint and E is its
  corresponding doubled endpoint divisor.
* If deg E=3, a mixed direction has its unique divisor
  [0]+[-2theta]+[infinity]; an endpoint has its doubled endpoint plus
  one additional point.

The support of E is, by (9)--(10), contained in index-two points or
higher-index points with positive primitive-index defect. Consequently
small-degree E forces these exceptional points to occupy the specific
apolar support positions, simultaneously. A degree-three mixed model
must pay at three distinct curve points; an endpoint model requires
the appropriate doubled point. These are necessary support constraints,
not existence claims for their embedded higher lifts.

### 8. Scope and independent review

The exact normalized budget (2) holds in all normal mate-bearing C0
carriers. The symbolic-triple obstruction needs the constant-direction
branch ell=7; the final scalar bound applies also to ell<=6 because
the previous index inequality is stronger there. Nonconstant directions,
large enough pole divisors, index-two contributions, and positive
higher-index defects remain legitimate continuation strata.

The quotient-of-relation-modules comparison and the coefficient-six
arithmetic were independently reviewed by `higher_moments` in
`2026-10-14-generalization-symbolic-triple-torsion-comparison-audit.md`.
The root independently reconstructed the length-two/three primitive
Cartier-multiple argument and the improved scalar inequality. The
present note supplies the actual proofs; agent agreement is not used
as a substitute for them.

---

<a id="2026-10-14-generalization-symbolic-triple-torsion-comparison-audit"></a>
## Symbolic triple torsion comparison: independent structural audit

Date: 2026-10-14. Worker: `socle_audit/higher_moments`.
Status: **PROVED NEW COMPARISON AND ARITHMETIC CONSEQUENCE, CONDITIONAL
ONLY ON THE EXPLICIT ACCEPTED INPUTS BELOW.**

Accepted inputs, not reverified: the fixed C0 normal/conormal coefficients;
the ordinary curvilinear CI free-layer and pointwise Frobenius theorem;
the local power-socle identity; and the fixed constant-direction pole
obstruction forcing `deg E>=2` for the symbolic triple. This assessment
audits the quotient comparison and its new implications, rather than
assuming the symbolic triple is a complete intersection.

Let X be a normal integral carrier of C0, of degree a, with a mate.
At P let r be the actual local Cartier index of C0. A regular local
function h has divisor rC, and `W_r=O_X/(h)` is a local complete
intersection of generic length r. Set

    Z_3 = O_X / I_C^(3),
    L_1(Z_3) = I_C / (I_C^2 + I_C^(3)),
    E_P = length torsion L_1(Z_3).

The symbolic quotient is pure and has generic length three. Its
first-layer relation line has the common saturated F_1 direction;
in the constant-direction branch ell=7 it is
`K_1=O(-7)(-E)`. None of these statements requires Z_3 to be lci.

### 1. Comparison at r>=3

The valuation description of the symbolic power gives
`(h) subset I_C^(3)` when r>=3, and hence a quotient `W_r -> Z_3`.
Complete along the smooth curve parameter and use `R=k[[t]]`.
Let V be the ambient first conormal module, free of rank two over R.
Write

    M_r = kernel(V -> L_1(W_r)),
    M_3 = kernel(V -> L_1(Z_3)).

Then `M_r subset M_3`. Their generic rank-one relation space is the
same F_1 direction, so their R-saturations equal a common line L in V.
Therefore

    torsion L_1(W_r) = L/M_r,
    torsion L_1(Z_3) = L/M_3,

and the map of torsion modules is surjective. In particular

    E_P <= length T_1(W_r)_P
        <= sum_i length T_i(W_r)_P
        = r D_r,P / 2.                         (1)

The perfect Frobenius pairing is used on the actual complete
intersection W_r. It is never used on Z_3. Thus no hidden lci or
Gorenstein assumption on the symbolic triple enters (1).

### 2. Comparison at r=2 and r=1

For r=2, normality and the height-one valuation description give

    I_C^(3) = h I_C.

Indeed division by h subtracts exactly two units of curve valuation
and no valuation at any other prime. The ambient first symbols of
`h I_C` vanish: both factors lie in the ambient curve ideal. Thus
the only first-symbol relation is the carrier F_1, and

    E_P = A_F,P.                               (2)

For r=1, the smooth curve is Cartier on the normal surface; the
surface is smooth there, so `E_P=A_F,P=0`. This is the accepted
smooth-Cartier case, not a new general primitive hypothesis.

Subsequent strengthening, independently reconstructed by `socle_audit`
and the root: the relative CI W_r is automatically primitive when
r<=3. Its special Artinian CI fiber has length below four, hence cannot
have embedding dimension two; Nakayama then makes the whole finite
free algebra R[z]/(z^r). Thus D_2=D_3=0 and E_P=0 for r=3. The full
proof is recorded in
`2026-10-14-generalization-normal-carrier-symbolic-triple-certificate.md`,
Section 2. In (3)--(4), positive defects may therefore be restricted to
r>=4. The s=3/no-index-two case in (5) is impossible; the displayed
2/3 bound is an earlier necessary conditional inequality, not evidence
for a surviving positive-defect index-three model.

Summing (1)--(2), the accepted fixed-direction obstruction gives

    2 <= deg E
      <= sum_(r=2) A_F,P + (1/2) sum_(r>=3) r D_r,P.       (3)

### 3. Positive defects and parity

If there are no index-two points, (3) forces at least one positive
`D_r,P` with r>=3. The pointwise Frobenius identity implies
`r D_r,P` is even; consequently odd r forces `D_r,P>=2` whenever
positive, while even r forces at least one. Thus

    sum_P D_r,P/r >= min_(actual r>=3) delta_r/r,
    delta_r = 1 for r even, 2 for r odd.         (4)

If only r<=s is known and index two is absent, this minimum can be
bounded uniformly by

    eta_3 = 2/3,
    eta_s = 1/s       for even s>=4,
    eta_s = 1/(s-1)   for odd s>=5.              (5)

With no r>=3 available, (3) already contradicts the absence of
index two. The weaker universal estimate from (4) is `1/s`.

### 4. A one-unit improvement of the normal index bound

Let `A=sum_P A_F,P`, `A_2=sum_(r=2) A_F,P`, and retain the accepted
identity

    Q = ell-16/a = sum_P (A_F,P+D_r,P)/r.

Suppose s>=3 bounds all actual indices and ell=7, so the accepted
constant-direction pole obstruction supplies (3). Then

    Q - A/s >= 1/s.                            (6)

There are two exhaustive cases. If a `D_r,P` is positive, it is an
integer at least one and r<=s, so its contribution is at least `1/s`.
If every `D_r,P=0`, equation (3) forces `A_2>=2`, and

    Q-A/s >= A_2(1/2-1/s)
            >= (s-2)/s >= 1/s.

Thus index-two points do not prevent the weaker improvement (6).
In the ell=7 branch, `A=4a-7`, and therefore

    s(7-16/a) >= 4a-6,
    4a^2-(7s+6)a+16s <= 0.                     (7)

When index two is absent, replace `1/s` in (6) by the sharper
`eta_s` of (5), or use the actual-index minimum in (4).

The integer branch ell<=6 is also compatible with (7). The accepted
original bound and its monotonicity in ell give

    4a^2-(6s+8)a+16s <= 0.

For s>=2 the left side in (7) is smaller by `(s-2)a`, so this implies
(7). Hence, after accepting the fixed-direction pole obstruction,
(7) can be used for all ell<=7 with s>=3. The case s<=2 is already
covered by the accepted bounded-index exclusion, and is not inferred
from the new constant-direction argument.

### 5. Scope

The comparison applies to a pure symbolic triple even if it has
special-point non-lci structure. It uses the actual local index and
full CI defect of W_r; surface multiplicity, first-jet smoothness, or
index lcm does not replace those data. This is a stronger necessary
index/degree inequality, not an exclusion of unrestricted normal
carriers, nonnormal carriers, or all STCI presentations of C0.

---

<a id="2026-10-14-generalization-curvilinear-torsion-and-index12"></a>
## Curvilinear ordinary normal layers and local index compatibility

Date: 2026-10-14. Root continuation from the `socle_audit` worker's
index-twelve program. This precursor's new proofs are now independently
accepted in the [full filtered compatibility audit](#2026-10-14-generalization-index12-filtered-compatibility).
The [current theorem and scope record](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-normal-index-socle-theorem)
adds the local power-socle formula, a linear index/degree bound and the
all-degree exclusion of normal C0 carriers with actual on-curve indices
at most four. The sections below retain the earlier intermediate route;
their former pending labels and final next-task language are historical,
superseded by those two accepted records. The unrestricted problem and
actual index-six/twelve strata remain open. Accepted inputs were not
recomputed.

### 1. A theorem for the ordinary nilradical filtration

The [free-layer proof](#1-ordinary-free-layers-are-powers-even-in-the-presence-of-torsion)
gives the powers of the first free layer and the global torsion budget
for the ordinary nilradical filtration. The ordinary filtration retains
torsion in each layer and a possible defect at the inclusion of its top
ideal into the actual socle.

### 2. A pointwise strengthening by a Frobenius lattice

The [pointwise proof](#2-the-frobenius-identity-is-pointwise) uses the
lattice of powers of a generator of the first free quotient and the
perfect relative Frobenius pairing. In particular, odd generic length
forces every local top-socle multiplicity to be even. This proof retains
all jets and local lattice changes. Surface class order and ramification
of a normalized inverse curve enter through separate hypotheses.

### 3. The forced length-twelve pair

The accepted bounded-index normal-carrier theorem reduces all C0
carriers whose local indices divide12 to the unordered pair(6,8).
At least one carrier is normal, so its generic normal order is one;
the generic algebra of the CI is curvilinear of length12. Its Loewy
index is eleven, and

```
deg D=11ell-42,
sum_i length T_i=6(11ell-42).
```

The conormal quotient of `O(-7)^2` gives ell<=7, and D effective
gives ell>=4. Thus the four initially necessary global alternatives
are

| ell | degree of the first direction 7-ell | deg D | total layer torsion |
|---:|---:|---:|---:|
|4|3|2|12|
|5|2|13|78|
|6|1|24|144|
|7|0|35|210|

These are consequences of one full filtered-algebra theorem, not
independent profile enumeration or assertions of existence.

### 4. Local class index controls poles in the first-symbol ratio

Let F define the normal carrier, and let a point P on C have local
Cartier index r_P dividing n. If r_P<n, choose a regular local
function h with divisor r_P C on the normal carrier. A mate's local
divisor is n C, hence its restriction is

```
G=u h^(n/r_P),  u a unit.
```

Normality proves u is a unit: its divisor and the divisor of its
inverse are zero at all height-one primes. Lift h into the ambient
curve ideal and u into ambient local units. Since n/r_P>=2,

```
G=tilde(u) tilde(h)^(n/r_P)+F H,
G_1=(H|C) F_1.
```

Thus the meromorphic first-symbol ratio G_1/F_1 is regular at P.
Any poles are supported at actual local index n points. This keeps
the precise index rather than substituting surface multiplicity.

For C0, the carrier first symbols are two binary forms of degree
4a-7. Their saturated direction has degree 7-ell, so their common
zero divisor has degree

```
deg A_F=4a-14+ell.
```

If no local index12 occurs, the ratio is regular everywhere. The
joint first-symbol image is then exactly the F_1 image. Hence
`length T_1=deg A_F`. In the ell=4 row this exceeds the *total*
torsion twelve: it is fourteen for a=6 and twenty-two for a=8.
Therefore ell=4 is excluded under the no-local-index12 hypothesis.
The remaining first-direction degrees are at most two.

This covers D/E and A1,A2,A3 mixtures, whose individual indices are
at most four; their common exponent can still be twelve. The full
bounded-index12 class also permits an actual index12 point, which
is explicitly outside this last exclusion.

If P is the pole divisor of the first-symbol ratio, the general
formula is `length T_1=deg A_F-deg P`. Thus the ell=4 row could only
survive with `deg P>=2` on a normal sextic carrier or `deg P>=10`
on a normal octic, all supported at genuine local index12 points.
This is necessary pole accounting, not an exclusion of that stratum.

### 5. Global cancellation without dropping simultaneous singularities

When all local indices are less than12, the ratio is a global
section of `O_C(b-a)`. For a normal octic with a sextic mate,
this line bundle has negative degree, so the mate's first symbol
is identically zero. For a normal sextic with an octic mate, the
ratio is a section of `O_C(2)`; the accepted quadratic restriction
surjectivity gives an ambient quadric Q with that restriction.
Replacing G by G-QF makes its first symbol zero and preserves the
entire defining ideal.

Thus this whole index class can be represented with a normal
order-one carrier and a mate of generic normal order at least two.
The replacement remains nonzero; no common surface component is
introduced. This does not make the structure primitive or assume
the two carriers are simultaneously smooth. At D-type points high
jets remain relevant even when the class index is small.

The next task is compatibility of these torsion and pole budgets
with the actual higher local ideals, especially the index-three
and index-four contributions. No exclusion of the positive rows,
the mixed order-one/thick pair, or the unrestricted STCI problem
is established here. An independent review should check the
pointwise Frobenius-lattice argument before relying on the conclusion.

---

<a id="2026-10-14-generalization-index12-filtered-compatibility"></a>
## Full filtered compatibility with local Cartier indices

Date: 2026-10-14. Author: `socle_audit`, including an independent
reconstruction of the root's new Jacobian/index argument.
Status: **PROVED NEW STRUCTURAL THEOREMS AND ALL-DEGREE EXCLUSION FOR
NORMAL C0 CARRIERS WITH ACTUAL ON-CURVE LOCAL INDICES AT MOST FOUR.**
Accepted inputs are the normal-carrier torsion/index reduction in
`2026-10-14-generalization-normal-carrier-torsion.md`, the full socle
duality/budget, the splitting N_C0^* = O(-7)^2, the exclusion of integral
carriers of degree at most four, and P-010's nonzero quadratic obstruction
for every constant first direction. Those inputs were not reverified.
Only the new filtered/index compatibility and its consequences are
proved and audited here. No state file is edited.

### 1. Ordinary free layers are powers, even in the presence of torsion

Let Y be a complete-intersection thickening of a smooth integral curve C,
whose generic transverse algebra is curvilinear of length n >= 2. Put

    J = I_C O_Y,
    L_i = J^i/J^(i+1),
    T_i = torsion(L_i),
    B_i = L_i/T_i,
    B = B_1.

Purity gives J^n = 0 everywhere. Every B_i for 0 <= i < n is a line
bundle. The direct sum of the T_i is a graded ideal: the product of a
torsion section with any normal-layer section is torsion. The ordinary
associated graded algebra is generated in degree one, hence so is its
torsion-free graded quotient. Therefore multiplication surjects

    B^i -> B_i.

A surjection between line bundles is an isomorphism. This proves

    B_i = B^i,  including J^(n-1) = B^(n-1).    (1)

This concerns the ordinary J-adic filtration. A saturated BF filtration
is a different filtration and may have nonzero multiplication divisors.
There is no conflict with earlier BF defect calculations.

Write deg B = -ell and J^(n-1) = Soc(Y)(-D), with D effective. The
accepted actual socle line gives

    deg D = (n-1)ell + (2g-2) + e(4-a-b),      (2)

where e = deg C and a,b are the defining hypersurface degrees. The
ordinary Euler-characteristic budget, together with (1), yields

    2 sum_i length T_i = n deg D.              (3)

No primitive hypothesis on Y, torsion-free layer hypothesis, or global
retraction to C is used.

### 2. The Frobenius identity is pointwise

Complete at P in C and choose a lift t of its curve parameter. The
local algebra A of Y is finite free of rank n over R = k[[t]]. Indeed
normal variables are nilpotent, and Cohen--Macaulay purity makes t a
nonzerodivisor. It is a relative complete intersection, so A^vee =
Hom_R(A,R) is free rank one as an A-module.

Choose z in J whose first symbol generates B locally. Its powers
generate each B_i by (1). Thus

    A_0 = R[z]/(z^n) subset A

is a full lattice. Its induced J-filtration is strict: the least
nonzero z-power in a polynomial has nonzero image in the corresponding
free normal layer. Comparing its graded pieces with L_i gives

    length_R(A/A_0) = sum_i length_R(T_i)_P.    (4)

Choose an A-module generator lambda of A^vee. The multiplication
pairing lambda(xy) is perfect over R. Finite duality identifies the
actual socle Ann_A(J) with R via lambda: explicitly,

    Hom_A(R,A^vee) = Hom_R(R,R) = R.

If s generates the socle, lambda(s) is a unit. Write
z^(n-1) = t^(D_P) u s, u a unit. The Gram matrix on
1,z,...,z^(n-1) is anti-triangular and has determinant a unit times
lambda(z^(n-1))^n. Its valuation is n D_P. The perfect Gram determinant
on an R-basis of A is a unit; passage to a full sublattice doubles its
index in the determinant. Therefore (4) proves the stronger identity

    2 sum_i length_R(T_i)_P = n D_P.           (5)

The independent reconstruction checks both the strict filtration and
the socle identification; no trace pairing on a nonreduced algebra is
mistaken for a perfect pairing.

### 3. The local normal-index theorem

Work in the complete regular ambient ring

    T = k[[t,x,y]],  I = (x,y),
    S = T/(F),

where S is a normal surface domain and C is the smooth curve defined
by I. Suppose a mate has divisor n C on S. Let r be the actual local
Cartier index of C, so r divides n, and put k = n/r. Choose h in S with
div(h) = r C; normality makes such a rational principal representative
regular. The mate is u h^k for a unit u in S. Units do not change its
ideal, so the two relevant local complete intersections are

    W_r = S/(h),  W_n = S/(h^k).

Let A_F,P denote the vanishing order on C of the carrier's first normal
symbol after saturating its rank-one direction. In local normal
coordinates one may write

    F_1 = t^(A_F,P) u_0 y,  u_0 a unit,         (6)

with z = x generating the free first normal quotient. For r >= 2,
W_r and W_n have the same free first-normal quotient: their generic
kernel is the direction of F_1, and taking the torsion-free quotient
saturates that same rank-one direction. Thus this z works for both.

Let D_r,P and D_n,P be their actual top-power/socle defects. The exact
compatibility theorem is

    D_n,P = (k-1) A_F,P + k D_r,P.             (7)

Its proof retains the full embedded algebra, not only the tangent cone.

#### 3.1 Normality gives the colon comparison

For the ideal I in S,

    (h^k : I) = h^(k-1)(h : I).               (8)

To check the nontrivial inclusion, if c I is contained in (h^k), choose
a normal parameter z whose valuation at C is one. Then val_C(c) >=
kr-1. The rational function c/h^(k-1) has C-valuation at least r-1,
and nonnegative valuation at every other height-one prime, because
h has divisor only r C. It is regular by normality. Dividing the
containment by h^(k-1) gives its membership in (h:I).

Modulo h^k, (8) gives the isomorphism of actual socle lines

    Soc(W_n) = h^(k-1) Soc(W_r).              (9)

Also

    w = z^r/h in Frac(S)

is regular: z has C-valuation one, and the divisor of z has only
nonnegative coefficients at other primes. Its restriction to C is
generically nonzero. Writing v = ord_C,P(w), one obtains from
z^(n-1) = h^(k-1) w^(k-1) z^(r-1) and (9)

    D_n,P = D_r,P + (k-1)v.                   (10)

#### 3.2 The relative Jacobian is an actual socle generator

The key standard input is the formal Artinian CI Jacobian theorem:
over a field of characteristic zero, the determinant of the defining
Jacobian generates the socle. A primary formulation, valid more
generally when the characteristic does not divide the length, is
Eisenbud--Ulrich, *Duality and socle generators for residual
intersections*, [Theorem 8.5, PDF pages 50--51](https://arxiv.org/pdf/1309.2050).
This applies to nonhomogeneous formal CI equations, not just graded
ones.

Here W_r is finite free of rank r over R: its generic transverse length
is r and it is a pure one-dimensional CI. Let

    j_r = det(partial(F,h)/partial(z,y)).

Generically j_r belongs to the socle by the standard theorem; purity
therefore shows j_r I = 0 globally. Its reduction modulo t is the
Jacobian of the length-r Artinian CI fiber, and generates that fiber's
socle in characteristic zero.

The actual socle is base-change-compatible in this situation. An
A-module generator of Hom_R(A,R) identifies Hom_A(R,A) with R;
after reduction modulo t it identifies the reduced line with
Hom_(A/tA)(k,A/tA), since the augmentation dual is the socle of the
dual algebra. Consequently j_r generates the actual R-socle by
Nakayama. This is the needed global-over-R justification; being a
generic socle generator alone would not suffice.

#### 3.3 Differentiation identifies the extra defect

In S the exact identity z^r = h w holds. Lift it to T, differentiate
with respect to z,y, wedge with dF, and reduce modulo (F,h). The term
h dw vanishes, and terms from the lifted multiple of F disappear.
One obtains in the actual socle of W_r

    w j_r = r z^(r-1) det(partial(F,z)/partial(z,y)).

The top power z^(r-1) is annihilated by I. Thus the last factor reduces
to its restriction on C, which is a unit times t^(A_F,P) by (6).
Since j_r generates the socle and z^(r-1) generates its top-power
subline, this proves

    ord_C,P(w) = A_F,P + D_r,P.                (11)

Combining (10) and (11) proves (7).

If r=1, then C is Cartier on the normal hypersurface and is smooth.
The hypersurface is smooth at P: a principal quotient by C is a regular
one-dimensional local ring, so the ambient surface has embedding
dimension at most two and is regular. Thus A_F,P = D_r,P = 0, and
(7) remains valid with the evident conventions.

The class index r does not bound A_F,P or D_r,P. For example index-four
D_n singularities may have large higher corrections. Formula (7)
charges those corrections rather than suppressing them.

### 4. A pointwise index bound gives a linear carrier-degree bound

For C0 let F have degree a, let the mate have degree b, and put
n = ab/4. A normal carrier makes the generic CI algebra curvilinear.
The ordinary first free layer is O(-ell), with ell <= 7. Equations
(1)--(2) give

    deg D = (n-1)ell - 4(a+b) + 14,
    deg A_F = 4a - 14 + ell,
    deg D + deg A_F = n(ell-16/a).             (12)

Let s be an upper bound on the actual local Cartier indices of C0
at points on F. Since k = n/r >= n/s, summing (7) gives

    deg D >= (n/s-1) deg A_F,
    s(ell-16/a) >= 4a-14+ell.                  (13)

For a >= 5, the right side is positive under a hypothetical mate;
therefore ell-16/a > 0. The ratio

    (4a-14+ell)/(ell-16/a)

decreases in ell because its derivative has numerator
14-4a-16/a < 0. Using ell <= 7 in (13) yields the uniform bound

    s >= (4a-7)/(7-16/a),
    4a^2-(7s+7)a+16s <= 0.                    (14)

Thus a pointwise bound on actual curve indices bounds carrier degree
linearly; it is stronger than merely bounding the least common multiple
of many indices and using a | 16R. It imposes no bound on the number of
singular points or their D_n higher-jet complexity.

For s <= 4, (14) forces integer a <= 6. Accepted low-degree exclusions
leave only a=5,6. The actual indices divide12, hence the accepted
Cartier integrality gives a | 192 and eliminates a=5. The accepted
index/torsion theorem then gives the minimal degree pair (a,b)=(6,8),
with R=12 and n=12. Equivalently one can use the accepted index12
reduction first and apply the sharper local formula below.

For a smooth rational degree-e curve with balanced normal bundle
O(2e-1)^2, put lambda = 2e-1. The same proof gives

    deg A_F = ea-2lambda+ell,
    deg D + deg A_F = n(ell-e^2/a),
    s >= (ea-lambda)/(lambda-e^2/a),           (15)

when deg A_F > 0 and the denominator is positive. These conditions are
forced by the preceding inequality for a genuinely non-Cartier carrier
point. The ratio decreases in ell when
ea+e^2/a >= 2lambda; this holds for integer e,a in the balanced rational
setting (strictly for e>=3 by AM--GM). Degenerate smooth line cases
with zero numerator and denominator are outside the non-Cartier
application. The characteristic-zero Jacobian hypothesis remains in
force.

### 5. Closing the entire actual-index-at-most-four class

Apply the accepted index12 reduction: a minimal mate yields the same
unordered pair (6,8), length12. The other defining surface is not
assumed normal. The four initially possible first-layer slopes are

    ell = 4,5,6,7,
    deg D = 2,13,24,35.

At every point with local index at most four, k = 12/r >= 3. Formula
(7) gives D_P >= 2 A_F,P. For a normal octic,

    deg D - 2 deg A_F = 9ell-78 < 0

for every ell <= 7. Hence the normal octic carrier is impossible.

For a normal sextic,

    deg D - 2 deg A_F = 9ell-62.

Effectivity forces ell=7, deg D=35, deg A_F=17, with total slack one.
Pointwise the exact slack is

    D_P - 2 A_F,P = (k-3)A_F,P + k D_r,P.      (16)

An index-two point has k=6 and A_F,P >= 1, costing at least three; it
is impossible. An index-three point has k=4 and costs
A_F,P+4D_r,P. An index-four point has k=3 and costs 3D_r,P.
Since R=12 requires an index-three and an index-four contribution,
the total slack one forces

    D_r,P = 0 at every index-three/four point,
    sum_(r=3) A_F,P = 1,
    no index-two points.                      (17)

In particular there is exactly one index-three point with first-symbol
vanishing order one. Simultaneous index-four points are all retained;
their total first-symbol vanishing order is sixteen. No classification
or independent bound on their higher local jets has been used.

### 6. Primitive symbolic triple contradiction

For each index-three/four point, (5) applied to W_r and (17) give zero
ordinary layer torsion. The R[z]/(z^r) lattice is therefore the entire
algebra:

    W_r = R[z]/(z^r).

For j <= r, the image of the symbolic ideal I_(C/X)^(j) is (z^j) in
this algebra. To check this without assuming a primitive hypothesis,
the two ideals agree after inverting t by their C-valuations. The
quotient R[z]/(z^j) is R-torsion-free, so the ordinary ideal (z^j) is
already saturated and equality descends. Consequently the symbolic
triple is locally R[z]/(z^3) at every index-three/four point.

At all remaining points the curve has index one, and the carrier is
smooth by the argument in Section 3; its symbolic triple is likewise
primitive. Thus the global symbolic triple defined by O_X(-3C) is an
embedded primitive triple everywhere along C0. This is a conclusion
from the full filtered compatibility, not an imposed primitive-pair
assumption.

Its free first conormal quotient is the same saturated carrier
direction as B_1 of the length-twelve thickening, namely O(-7).
The map O(-7)^2 -> O(-7) has constant coefficients on P1, so its first
initial relation is a fixed linear form m. Primitivity makes the next
relation space exactly mV. The accepted P-010 quadratic obstruction
for this constant embedded primitive triple is nonzero in every
direction. This is a contradiction.

Therefore:

**No normal integral carrier of C0 in characteristic zero can admit a
mate if every actual local Cartier index of C0 at points of that carrier
is at most four. This is an all-carrier-degree and all-mate-degree
exclusion.**

It includes arbitrary simultaneous D/E rational-double-point
singularities and A1,A2,A3 mixtures along C0, using the accepted class
index bounds. Singularities away from C0 are irrelevant. No normality
of the other defining hypersurface, primitive initial presentation, or
D_n complexity bound is required.

### 7. What survives

The complete class with indices dividing12 still permits actual
index-six or index-twelve points. Those points have k=2 or k=1 in
the length-twelve formula and are not closed by Section 5. In
particular an index-twelve point can support a pole in the first-symbol
ratio and evade the stronger first-layer comparison. The local theorem
now gives the exact simultaneous system

    D_P = (12/r_P-1)A_F,P + (12/r_P)D_(r_P),P,
    2 sum_i length(T_i)_P = 12D_P,
    sum_P D_P = 11ell-42,
    sum_P A_F,P = 4a-14+ell,
    ell in {4,5,6,7},
    lcm_P r_P = 12.

These equations retain all higher primitive-index socle defects and
simultaneous support points. They do not claim that any remaining
system lifts to a global pair or that C0 is non-STCI. The unrestricted
normal, nonnormal, and entirely thick branches remain open.

### 8. Audit provenance

The ordinary free-layer theorem was first proposed by `socle_audit`
and independently reconstructed by the root and the
`index12_multiplication` worker. The root then proposed the pointwise
Frobenius identity, the local Jacobian/index formula, and the resulting
symbolic-triple contradiction. This note independently reconstructs
all of those new steps, explicitly checking the socle's base change,
the normal-domain colon argument, the shared free normal generator,
and the saturation identifying symbolic triples.

The primary Jacobian theorem was inspected for this new bridge; no
previously accepted repository calculation was rerun. Parallel agent
agreement is not the proof: Sections 1--6 contain the actual arguments.




## Consolidated historical supplement: `research/supplements/OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md`

# Principal triple incidence, normalization and conductor boundaries

Full original source text is preserved below, including calculations, qualifications, counterexamples, and unresolved questions. This compilation does not independently audit claims.

---

<a id="source-2026-10-08-session-mf6-principal-boundary-auditmd"></a>

## Principal e=1,d2=1: complete frame complements and carrier boundaries

Date: 2026-10-08. Fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, over an algebraically closed characteristic-zero
field. This note complements the
[independent open-chart rank proof](#source-2026-10-08-session-mf6-principal-rank-open-independent-auditmd).
It uses actual complete quartic spaces at every exceptional frame, rather
than specializing a generic nullspace basis. No records were
edited. The unrestricted C0 and universal STCI problems remain open.

**PROVED, conditional on the accepted ancestor reduction and P-037:**
every principal e=1,d2=1 common quartic ancestor is excluded. The open
chart has exactly one quartic at every point; the complete complement
has exactly one quartic except at one point, where every quartic is a
fixed cubic times a linear form. These two alternatives exclude a common
quartic ancestor by proportionality and by division to a forbidden
degree-one ancestor, respectively. This ancestor conclusion does not
assert that every quartic carrier has no higher-degree STCI mate.

**PROVED carrier exclusions on the complement:** the three b0=0
carriers are normal and hence excluded by the repository's accepted
all-normal-quartic theorem. The rational S=0 carrier and the two
infinity-defect carriers are integral quartics singular along smooth
twisted cubics and hence excluded by the accepted all-degree
twisted-cubic theorem. The node fiber consists of reducible quartics
and is excluded in every mate degree. The remaining complement carrier
at (p,r)=(8,1/2) is integral and nonnormal; its actual conductor/mate
obstruction remains open at the time this note was written.

### 1. Direction curve and complete chart coverage

On the principal locus a0*b1!=0 and b0!=0, quotient scaling and the
actual torus give

    A=1+r*z, B=1+p*z, p!=0, p-r!=0.

The condition p-r!=0 is the basepoint-free determinant, not a removable
computational frame restriction. The degree-six invariant direction
equation is

    H=8p^3-(64r^2+128r+16)p^2
      +(96r^4+512r^3+592r^2+128r+6)p
      -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9).

Its geometrically integral genus-one normalization and explicit
Weierstrass model `YE^2=XE^3+96XE-448` are checked in the
[curve source](https://github.com/markluxton1/STCI/blob/1fccec5c7afabb4e3f83ccd9c717692c07f0b338/research/computations/verify_mf6_e1_d1_principal_curve_2026_10_08.py)
and the [checkpoint](normal_filtration_boundary_obstructions.md#the-principal-direction-sextic-has-an-elliptic-normalization). The corrected
fiber is H(p,-1/2)=8p(p+2)^2.

Set

    P=2p+12r^2+16r+9,
    Q=8p+12r^2+4r+3,
    T=2p-4r^2-4r-1,
    S=p-2r-1.

The quadratic cocycle coefficients are c1=-pP/8,
c2=-(2r+1)Q/8 and c3=-(2p+36r^2+16r+3)/4, with
H=64(c1*c3-c2^2). On pP!=0 the unique killing section and the finite
correction are

    delta=(2r+1)Q-pP*z,
    Gamma=nonnegative Laurent part of delta*h2.

The exact identity Res_z(delta,Gamma)=p^4*P^4/8 proves flatness at its
finite zero. Delta has nonzero leading coefficient, so it has no
infinity zero. The independent contact frame is valid on
pP(p-r)(2r-1)T!=0. Its rank is six everywhere, including the retained
S=0 rational point; S was never assumed to be a unit.

The complement is exhausted as follows.

- p=0 is outside the principal locus; p-r=0 violates basepoint freeness.
- At r=1/2, H=8(p-8)(p-2)^2, giving exactly p=2 and p=8.
- At T=0, H=-9(2r-1)^2(2r+1)^4. The r=1/2 point is p=2
  and is already included. The other possibilities are p=0 or the
  primitive point (p,r)=(-2,-1/2).
- On P=0, H=-9(2r+1)^2*Q^2. The nonprimitive possibilities are
  p=2r+1 with 12r^2+20r+11=0. They have c1=c2=0,c3!=0,
  and require the actual alternative section delta=1, whose zero is
  infinity. The primitive point (-2,-1/2) has zero quadratic cocycle;
  the accepted uniqueness argument H0(O(-3))=0 makes a genuine
  degree-one defect nonflat there. It is not a missing flat triple.
- On S=0,
  H=-(2r-1)^2(2r+1)(6r+1)(12r^2+20r+11). The only additional
  valid point is (p,r)=(2/3,-1/6); the quadratic points belong to P=0,
  and the other points were already included or excluded above.
- On the projective b0=0 chart, a1!=0 follows from H and p!=0.
  Normalizing a0=a1=1 gives A=1+z,B=pz and
  p^3-8p^2+12p-72=0. This polynomial is irreducible over Q and has
  nonzero discriminant -160704. One exact cubic-field calculation
  therefore covers all three distinct geometric conjugates. Its roots
  are nonzero and the determinant p is nonzero.

This is a full chart-complement argument. It makes no assertion about
other e, other defect degrees, or directions with a0*b1=0; the latter
defect-one endpoint directions were treated separately in the
[endpoint proof](normal_filtration_boundary_obstructions.md#source-2026-10-07-session-mf6-e1-d1-endpointsmd).

### 2. Fresh ambient quartic spaces

The [boundary verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08.py)
rebuilds all 35 degree-four monomials. It imposes restriction to C0,
vanishing of the first quotient-normal coefficient, and the actual
quadratic-contact equation delta*Qquad-Gamma*h=0. It computes over Q,
Q(sqrt(-2)), or the irreducible cubic field. No generic seven-column
kernel is evaluated at a bad point.

| Fiber | Number of geometric points | Full 35-column rank | Quartic space |
|---|---:|---:|---|
| (p,r)=(2,1/2) | 1 | 31 | Cstar times all four linear forms |
| (p,r)=(8,1/2) | 1 | 34 | one quartic |
| (p,r)=(2/3,-1/6) | 1 | 34 | one quartic |
| p=2r+1, 12r^2+20r+11=0 | 2 | 34 | one quartic at each conjugate |
| b0=0, p^3-8p^2+12p-72=0 | 3 | 34 | one quartic at each conjugate |

All literal quartics are preserved in the three hash-bearing JSON
records adjacent to the source, with suffixes `_rational`, `_quadratic`
and `_infinity`. The fixed cubic is

    Cstar=x0^2*x2-x0^2*x3+x0*x1*x2-x0*x1*x3
      -2*x0*x2^2+x0*x2*x3+x0*x3^2-x1^3+x1^2*x2+2*x1^2*x3
      -x1*x2^2-x1*x2*x3-x1*x3^2+x2^3.

The displayed complete basis is Cstar times
`x0,x1,x0+x1/2+x2/2,x3`, so it is the entire linear system
Cstar*H0(O_P3(1)). For a carrier F=Cstar*L, every positive-degree
mate intersects the plane L=0 in a curve or contains the plane; its
support cannot be solely C0. For a common quartic ancestor, dividing
F and G by Cstar gives a common degree-one ancestor, forbidden by
accepted P-037. At every other fiber, F and G are proportional;
they cannot produce the two independent fixed local-cohomology targets.

### 3. The infinity-defect frame is flat

For the quadratic roots write a^2=-2 and

    r=(-5+2a)/6, p=2r+1, c3=-4/3+10a/3.

The finite correction is
Gamma=(-5-a)z/9+(-2+5a)/9 and delta=1. Flatness cannot be inferred
from an affine resultant with constant delta, so the actual second
chart was rebuilt:

    x3=1, x2=w, x1=w^3+2U, x0=w^4+V/2+3wU,
    A_inf=r+w, B_inf=p+w,
    Bezout=(-1/(p-r),1/(p-r)), delta_inf=w.

The unique quartic has

    h_inf=-w^3*(w-1)^3*(w^2+w-1/3+a/3),
    Gamma_inf=3w^2+(-6+3a)w+4/3-10a/3.

This is obtained by exact polynomial division
Gamma_inf=delta_inf*Qquad_inf/h_inf, with zero remainder.
Its constant is -c3, of norm 24, and is nonzero at both geometric
roots. Thus the infinity defect is genuinely flat. The
[literal-form two-chart verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_mf6_e1_d1_principal_boundary_residues_2026_10_08.py)
checks the full actual-frame calculation.

### 4. Geometry and mate scope of the unique boundary carriers

The [self-contained M2 certificate](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_mf6_e1_d1_principal_boundary_geometry_2026_10_08.m2)
contains the literal quartics, number-field equations and explicit
curve ideals. It checks the following exact facts.

The b0=0 quartic has a Jacobian cone of dimension one. Thus its
projective singular locus is finite, after every extension of the
constant field. A reducible or nonreduced projective hypersurface
would have a positive-dimensional singular locus. The surface is
therefore geometrically integral, and the hypersurface Cohen–Macaulay
property plus regularity in codimension one makes it normal. The
[accepted normal-carrier theorem](../synthesis/quartic_carrier_proof.md#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing)
excludes all three carriers in every mate degree.

The S=0 rational quartic and both infinity-defect quartics have Jacobian
cones of dimension two and degree three. The certificate supplies an
ideal Tc of three quadratic generators, with dimension two, degree
three and a free resolution of length two. It verifies that the
projective curve Tc is geometrically smooth and that all derivatives
of F vanish on it. This is a nondegenerate ACM smooth degree-three
curve, hence a smooth twisted cubic.

These quartics are geometrically integral. Their singular scheme has
degree three and already contains the twisted cubic of degree three,
so it has no other curve component. A nonreduced surface would have
a surface component in its singular locus. A reducible quartic has a
factor partition of degrees (1,3) or (2,2); the factor intersection is
a complete-intersection curve of degree three or four, supported in
the singular locus. The degree-three alternative is planar and
cannot be supported on a twisted cubic. The degree-four alternative
cannot have sole reduced support of degree three, because its generic
multiplicity there would have to be an integer. This proves
integrality, including over an algebraic closure. The
[accepted applicability proof](../supplements/QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md)
and [adversarial audit](../supplements/QUARTIC_SCROLL_REDUCED_CONDUCTORS.md)
then exclude every mate degree.

At (p,r)=(8,1/2), the Jacobian cone has dimension two and degree five.
Its reduced curve support consists of the two rational lines

    L1=(x1-4*x2,x0-16*x3),
    L2=(x1-12*x2-16*x3,x0+32*x2+48*x3).

Equivalently it is the plane conic

    x0+4*x1-16*x2-16*x3=0,
    (x1-4*x2)*(x1-12*x2-16*x3)=0.

Their intersection [16:-8:-2:1] is C0 at z=-1/2; L1 also meets
C0 at z=1/2. This reduced support is not the actual conductor scheme.
No reduced-conductor theorem is transferred to it.

This quartic is geometrically integral. A quadratic factor containing
C0 would be its unique quadric q, which the source checks is not a
factor. For a plane*cubic factorization, the cubic contains C0 and
the plane's restriction to C0 divides
h=(2z-1)^3*(2z+1)^5. There is no infinity root. A plane restriction
lies in span(1,z,z^3,z^4); among divisors of degree four supported at
z=1/2,-1/2, its missing z^2 coefficient forces multiplicities (1,3)
or (3,1). The only candidate planes are
x0+4x1-16x2-16x3 and x0-4x1+16x2-16x3. The certificate checks that
neither divides F. Every reducible degree-four factorization has a
factor of degree one or two, so this excludes all factorizations over
an algebraic closure. Its conductor and all-mate exclusion were passed
to the degenerate-scroll-conductor lane as an explicit remaining target.

### 5. Cubic residue bounds and continuation

The residue verifier uses S=h/delta and T=Gamma*E-delta*K in the
actual local expansion h*m+Qquad*y^2+E*m*y+K*y^3. The normalized
cubic residue is T/S up to sign. Its finite pole divisor and its
infinity pole order are checked in both actual charts.

| Carrier | Finite excess | Infinity excess | Necessary degree D3 |
|---|---:|---:|---:|
| p=8,r=1/2 | 2 | 0 | at least 3 |
| p=2/3,r=-1/6 | 1 | 3 | at least 5 |
| two infinity-defect roots | 3 | 1 | at least 5 |

The last two rows cannot realize MF6 type (d2,d3)=(1,3), but the
all-degree carrier exclusions above use the stronger geometric
theorems. The p8 row meets the MF6 cubic budget exactly; the cubic
bound does not remove it. A generic quartic or a higher-degree mate
on the remaining elliptic direction curve remains a distinct problem
from the now-complete principal common-ancestor incidence.

Saved source-byte outputs are adjacent to the three verifiers. The
boundary Python source is frozen for independent isolated replay.
The exact M2 and residue verifiers both passed with their literal
forms. A derivation attempt using `radical` directly over a number
field failed because M2 supplied no applicable strategy; the final
certificate instead verifies explicit twisted-cubic ideals. Two M2
API corrections (`isCM` and resolution of a quotient ring) were
replaced by the checked length-two resolution of `coker gens Tc`.
These execution repairs changed no mathematical assertion.

### 6. A structural finite reduction for principal STCI carriers

There is a further consequence that does not require computing a large
Jacobian elimination ideal. Let U be the valid flat principal direction
curve with the fixed-cubic node removed. The zero-cocycle primitive
point and the determinant/nonprincipal loci are already outside U.
The independent open-chart proof and the complete complementary ranks
show that the quartic contact kernel has constant dimension one on U.

The unique defect line and correction are intrinsic. Their local
algebraic formulas on the finite and infinity charts glue because the
correction is unique (H0(O(-3))=0). Thus the actual contact matrices
define a kernel line bundle on U and a regular morphism

    U -> P(H0(P3,O(4))).

Equivalently this can be constructed on the genus-one normalization;
the finitely many deleted or singular direction points have already
been treated separately. The universal projective Jacobian locus of
this quartic family is closed in U times P3, and its projection to U
is proper. Upper semicontinuity of fiber dimension makes

    {u in U : the quartic has a positive-dimensional singular locus}

a closed subset of U. It is proper: all three b0=0 fibers have finite
singular loci. Since U is an integral curve of finite type, this subset
is finite. Outside it, every quartic is geometrically integral and
normal by the argument of section 4, and the accepted normal-carrier
theorem excludes every mate.

**PROVED finite reduction, not an exception-list computation:** only
finitely many nonnormal quartics in the principal defect-one family
can remain STCI carriers. The exact finite nonnormal parameter ideal
has not been computed in this note. The rational S=0 point and the two
infinity-defect points belong to that finite set and are already
excluded by the twisted-cubic theorem. The p8,rhalf point is another
member and has been assigned an explicit nonreduced-conductor proof.
Further nonnormal points on the independent contact open remain to
be identified or excluded structurally. Neither finiteness nor the
complete common-ancestor conclusion is presented as a universal STCI
theorem.

---

<a id="source-2026-10-08-session-mf6-principal-rank-open-independent-auditmd"></a>

## Principal e=1,d2=1 quartic rank: independent open-chart audit

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]`, characteristic
zero. Status: **PROVED HERE, exact polynomial certificate on the stated
open**. This does not exclude a quartic with a higher-degree mate.
The chart complement is separately owned by the principal-boundary audit.

For the quotient direction `A=1+r z`, `B=1+p z`, write

```
H = 8p^3 -(64r^2+128r+16)p^2
    +(96r^4+512r^3+592r^2+128r+6)p
    -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9),
P = 2p+12r^2+16r+9,
T = 2p-4r^2-4r-1,
S = p-2r-1,
Q = 12r^2+20r+11.
```

The theorem is that the complete vector space of ambient quartic forms
containing the associated genuine triple has dimension exactly one on

```
U = {H=0, p P (p-r) (2r-1) T != 0}.
```

Thus this entire open cannot supply two independent quartic ancestors.
A unique quartic can still serve as one carrier in an STCI pair; that
question is not settled by this calculation.

### 1. Complete ambient first-normal space and the exact frame

The standalone verifier
[`verify_session_mf6_principal_rank_open_2026_10_08.py`](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_mf6_principal_rank_open_2026_10_08.py)
reconstructs the first and second normal equations from eighteen
independent actual quartic forms. Their coefficient rank is eighteen,
and all vanish on `C0`; the thirty-five quartic monomials restrict to
all seventeen powers `z^0,...,z^16`. Consequently these forms constitute
the entire degree-four ideal space, rather than a sampled subspace.

Using the normal chart

```
x0=1, x1=z, x2=z^3+V, x3=z^4+U+(3/2)zV,
U= -r m/(p-r)+(1+rz)y,
V= -p m/(p-r)+(1+pz)y,
```

the first normal matrix `M1` has shape `11 x 18`. Its columns
`0,1,2,3,4,5,6,11,12,14,15` have determinant

```
p^4(p-r)(2r-1)T^2 / 256.
```

It therefore has rank eleven everywhere on `U`. The seven columns
`N` saved in the reconstruction, after dividing each by its separately
recorded polynomial gcd, lie in `ker(M1)`. The free rows
`7,8,9,10,13,16,17` are diagonal, with diagonal entries

```
-(2r-1)T^2/256,
-(2r-1)T/128,
-(2r-1)T^2/256,
-1/32,
-p(2r-1)T^2/256,
-p^3(2r-1)T^2/256,
-p^4(2r-1)T^2/256.
```

Their determinant is `-p^8(2r-1)^6T^11/2^52`, a unit on `U`.
Thus these seven columns form the complete first-normal kernel in
every fiber of this open, with no generic-only frame assumption.

Let `h2` be the accepted quadratic cocycle,

```
h2 = -(2A+zB)(12A^2+3z^2B^2+4z^2(A'B-AB'))/(8z^5).
```

Its three negative Laurent coefficients satisfy `64(c1c3-c2^2)=H`.
Choose

```
delta = -8c2+8c1z = (2r+1)(8p+12r^2+4r+3)-pPz,
Gamma = polynomial part of delta*h2.
```

The exact identity `Res_z(delta,Gamma)=p^4P^4/8` gives triple flatness
on this chart. If a quartic's first normal coefficient in `m` is `h`
and its quadratic coefficient in `y` is `q2`, the second contact
condition is `delta*q2-Gamma*h=0`. Multiplying by the unit `p-r`
produces the saved complete matrix `M2`.

On `H=0`, the product `M2*N` has its last five rows zero; its seventh
row is a multiple of `H`. Divide the first six rows by
`p-r,p-r,p-r,p-r,p(p-r),p^2(p-r)`, respectively. The resulting
`6 x 7` polynomial matrix is denoted `D`. Every row division is by a
unit on `U`. Its rank is the actual contact rank of the complete
first-normal kernel.

### 2. Factor before reduction; only two residual norms are needed

The independent raw-factor computation retained all seven actual
cofactors, instead of reducing matrix entries modulo `H` before taking
determinants. The latter operation produces degree-fifty expressions,
although it is algebraically correct. For cofactors obtained by omitting
columns six and five, respectively, the exact factorization is

```
M6 = (27/2^51) p^5(2r-1)^4(2r+1)^3 S^3 T^7 R6,
M5 = (27/2^51) p^5(2r-1)^4(2r+1)^3 S^3 T^7 R5.
```

`R6` and `R5` are the completely recorded residual polynomials of
total degrees twenty and twenty-one in
[`audit-mf6-e1-principal-raw-minors-2026-10-08.json`](https://github.com/markluxton1/STCI/blob/6880e35bb6c7ec13c2ba18cc1a0cce328e1d795f/research/scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.json).
The verifier independently recomputes every cofactor, checks these
factor identities and all five others, and compares their reductions
with the previously saved seven-cofactor remainders.

The factor `2r+1` is a unit on `U`, for the precise reason

```
H(p,-1/2)=8p(p+2)^2,
P(p,-1/2)=2(p+2).
```

Both possible points violate `pP!=0`. An earlier informal message
incorrectly gave `H(p,-1/2)=8(p+2)^3`; the corrected identity above is
checked directly by the verifier and is the one used in the proof.

On `S!=0`, every displayed prefactor of `M6,M5` is a unit. If their
residuals vanish simultaneously at a point of `H`, then both exact
resultants in `p` vanish at its `r` coordinate. Their gcd is

```
const * (2r-1)^16(2r+1)^26 Q^5,
const = 175495605123022848.
```

The full factorizations are

```
Res_p(H,R6) = const * (2r-1)^16(2r+1)^26 Q^6 F12,
Res_p(H,R5) = -8const * (2r-1)^16(2r+1)^27 Q^5 F16,
```

where

```
F12 = 626688r^12+2113536r^11+7473152r^10+9351168r^9
      +16506624r^8+15984640r^7+7622400r^6+3220992r^5
      +1515632r^4+554304r^3+123528r^2+14832r+801,

F16 = 518455296r^16-3247570944r^15-13217169408r^14
      -31615975424r^13-48489316352r^12-51974971392r^11
      -40950489088r^10-25317873664r^9-13339307520r^8
      -6235899392r^7-2459068928r^6-740795520r^5
      -157172544r^4-21102432r^3-1591200r^2-59976r-8577.
```

The verifier checks the exact resultant gcd, including all possible
cross-factor common roots; this is stronger than separate informal
coprimality assertions about `F12,F16`.

The roots `r=+/-1/2` have already been removed on `U`. At a root of
`Q`, use `K=QQ(sqrt(-2))` and
`r=(-5+2sqrt(-2))/6`. Direct Euclidean division in `K[p]` yields

```
gcd(H,R6,R5)=p-(2r+1).
```

The checker verifies an extended-Euclidean identity and divisibility,
so this is a complete exact fiber calculation. Its conjugate covers
the other root of `Q`. But `p=2r+1` on `Q=0` implies `P=0`.
Therefore neither quadratic fiber contains a common residual zero
on `U`. This proves that the two cofactors cannot vanish simultaneously
on `U` intersected with `S!=0`.

### 3. Retain and cover the nonunit factor S

`S` is not a unit and was never silently cancelled. Its entire fiber
on `H` is given by

```
H(2r+1,r)=-(2r-1)^2(2r+1)(6r+1)Q,
P(2r+1,r)=Q.
```

The roots `r=+/-1/2` and `Q=0` violate the defining open conditions.
The sole remaining point is `r=-1/6,p=2/3`, with `P=8`.
At that point, the actual cofactor omitting column four is

```
1073741824 / 36472996377170786403 != 0.
```

This independently covers the retained `S=0` branch. Consequently
`rank(D)=6` everywhere on all of `U`. Since `rank(M1)=11` and the
first-normal kernel has dimension seven, the complete quartic matrix
has rank seventeen and its kernel has dimension one.

### 4. Evidence and exact remaining scope

The [exact rank checker](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_mf6_principal_rank_open_2026_10_08.py)
reconstructs the ambient maps and verifies the retained
[contact matrix and frame](../scratch/session-mf6-e1-principal-contact-2026-10-08.json),
[normalized contact data](https://github.com/markluxton1/STCI/blob/6880e35bb6c7ec13c2ba18cc1a0cce328e1d795f/research/scratch/session-mf6-e1-principal-minors-2026-10-08.json),
and [raw cofactors](https://github.com/markluxton1/STCI/blob/6880e35bb6c7ec13c2ba18cc1a0cce328e1d795f/research/scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.json).
The free determinant denominator is `2^52`, not `2^53`; cofactor and
specialization comparisons require expanded polynomial equality rather
than structural SymPy equality.

This theorem covers only the displayed principal flat chart with
`a0=b0=1`, including every parameter of that chart, rather than merely
a generic rank computation. The `P=0` alternate-killing-section fibers,
`r=1/2` frame degenerations, `b0=0`, and the earlier endpoint orbits
must still be reconciled by their complete ambient quartic calculations
before asserting a theorem for the whole principal triple incidence.
The existence or nonexistence of an STCI mate for the remaining unique
quartic carriers is a separate problem and is not claimed here.

---

<a id="source-2026-10-08-session-mf6-rhalf-scroll-conductormd"></a>

## The principal MF6 boundary (p,r)=(8,1/2): an entire-conductor proof

Date: 2026-10-08. Status: **PROVED all-mate exclusion**, with exact
normalization/conductor identities and a completed
[independent audit](#source-2026-10-08-session-mf6-rhalf-scroll-independent-auditmd).
This is a fixed member of the principal
e=1,d2=1 quartic family, not an exclusion of every member of that family.

### 1. Carrier binding and a finite smooth normalization

The complete quartic space at this boundary has dimension one. The
source quartic is the `rhalf_unique` row of the
[exact principal-boundary record](https://github.com/markluxton1/STCI/blob/6880e35bb6c7ec13c2ba18cc1a0cce328e1d795f/research/computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08_rational.json).
Make the invertible linear coordinate change

    x=x0+4x1-16x2-16x3,
    y=x1-4x2,
    z=x1-12x2-16x3,
    w=x3.

Set

    L=96w+x-8y+4z, chi=x-8y, G=xL-8yz.

The original quartic, in these coordinates, satisfies the exact identity

    -64 F=G^2-x^3 chi.

Thus its discriminant as a quadratic polynomial in w is
9x^5(x-8y). If instead one uses the rational coordinate T=xw, its
discriminant is 9x^3(x-8y); these are the same nonsquare obstruction.
The coefficients of F as a polynomial in w have gcd one. The
discriminant is nonsquare in k(x,y,z), so Gauss's lemma proves F is
irreducible over every characteristic-zero algebraically closed field.

Let S=P1_[a:b] times P1_[U:V] and H=O_S(2,1). Define a morphism
nu:S->P3 by the four sections

    x=U b^2,
    y=U(b^2-a^2)/8,
    z=V b^2,
    w=(U(ab-a^2)-V(a^2+3b^2))/96.

They have no common zero. For b!=0, x=z=0 would force U=V=0.
For b=0, a!=0, y=w=0 again forces U=V=0. Their substitution into F
is zero. The pullback of O_P3(1) is the ample H. A positive-dimensional
fiber would contain a curve on which H has degree zero, impossible;
therefore the proper morphism is finite onto its image.

The generic base parameter a/b is recovered from the image by

    a/b=G/x^2,

and the remaining parameter U/V is recovered as x/z. Thus nu is
birational. Its image is the integral quartic F, and S is its smooth
normalization. Its polarization is the smooth rational quartic scroll
F0 with H^2=4 and K_S.H=-6.

### 2. The complete normalization ring and the entire conductor ideal

Two additional degree-one sections are

    v=Uab, u=Vab.

Together with x,y,z,w they span the complete six-dimensional section
space H0(S,H), since they recover the six monomials
Ub^2,Uab,Ua^2,Vb^2,Vab,Va^2. The corresponding full section ring B is
the normal, projectively normal quartic-scroll ring. Let A be the
quartic hypersurface ring generated by x,y,z,w. Exact identities give

    xv=G, xu=zv, Lv-8yu=x chi,
    v^2=x chi, uv=z chi,
    u^2=zv-z chi-3z^2-96zw.

The A-module A+Av+Au is closed under multiplication, hence equals B.
The displayed monic quadratic equations also show B finite over A.
For the ideal

    J=(x^2,xy,G),

one has the six exact ambient cubic identities

    Jv=(xG, yG, x^2 chi),
    Ju=(zG, (LG-x^2 chi)/8, xz chi).

Therefore J annihilates B/A, so J is contained in the actual conductor
ideal I. Its Hilbert--Burch matrix is

    [ x,  0  ],
    [-z,  x  ],
    [ L, -8y ].

The maximal minors generate J. Its support is x=0,yz=0, so it has
height two, and the Hilbert--Burch resolution makes its projective
curve an ACM cubic with Hilbert polynomial 3m+1. The entire actual
conductor of this smooth quartic-scroll normalization also has
polynomial 3m+1 by the duality calculation in the
[applicability note](../supplements/QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md).
The inclusion J subset I gives a coherent quotient I/J. Its Hilbert
polynomial is zero; a nonzero coherent sheaf on projective space has a
nonzero Hilbert polynomial. Hence the conductor ideal sheaves agree:

    I=J, Gamma=V(x^2,xy,G).

This identifies the entire scheme, rather than just its Jacobian or
reduced singular support. Gamma is a double line x=y=0 together with
a reduced line x=z=0. Pulling J to S gives

    x^2=U^2 b^4,
    xy=U^2 b^2(b^2-a^2)/8,
    G=U^2 a b^3.

After the common factor U^2b^2, the residual sections
b^2,(b^2-a^2)/8,ab have no common zero on P1. Therefore the entire
upstairs conductor is

    D=2E+2T, E={U=0}, T={b=0}.

No isolated conductor defect is left implicit.

### 3. The nonreduced downstairs conductor is Gorenstein and the cover flat

The entries of the Hilbert--Burch matrix cannot all vanish at a
projective point: x=y=z=0 would make L=96w, forcing w=0. At every
point of Gamma at least one matrix entry is a unit, so its localized
grade-two ideal has two generators and is a complete intersection.
Thus the actual nonreduced Gamma is locally Gorenstein.

The conductor duality exact sequence is

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,
    p=nu|D.

Its quotient omega_Gamma is invertible, so the sequence locally splits
as modules. Consequently p_*O_D is locally free of rank two over
Gamma, including its double-line points and the line intersection.
This is the reason flatness holds; Cohen--Macaulayness alone would
not suffice. Trace in characteristic zero gives the global algebra
involution sigma with fixed algebra exactly O_Gamma.

At the generic point of the double line, E is the unique reduced
upstairs component, and its reduced map has degree two:

    w/z=-(a^2+3b^2)/(96b^2).

Thus sigma preserves E and acts by a/b -> -a/b on its reduced function
field. At the generic point of the other line, T maps isomorphically
to that line and is doubled upstairs. Its generic algebra is the
dual-number algebra over the reduced line's function field, and sigma
acts trivially on the reduced field. In particular sigma preserves
both minimal associated primes of D. This statement retains the
generic nilpotent scheme structure.

### 4. Every descended power compresses to a descended square

Suppose F had a mate of positive degree n presenting C0 set
theoretically. The full-support argument for a smooth scroll gives a
unique c isomorphic to C0, c~H, and

    nu*G_mate=lambda f^n, div(f)=c.

The quotient is a global constant. Since the mate descends from X,
sigma(f|D)^n=(f|D)^n. The restricted section f is generically nonzero
on both conductor primes, hence invertible in each generic Artin ring
of D. The ratio h=sigma(f)/f satisfies h^n=1 there.

In a characteristic-zero Artin ring, any root of T^n-1 is one of the
constant roots of unity after choosing its reduced field root: the
derivative nT^(n-1) is a unit, so its nilpotent correction is zero.
On E the reduced field contains the algebraically closed constants,
and h is a constant root zeta. Applying sigma twice, while sigma
preserves this generic prime, gives zeta^2=1. On T the reduced action
of sigma is the identity, so the reduced ratio is one and h=1.
It follows that f^2 is sigma invariant in both generic Artin rings.

The Cartier conductor D on smooth S is Cohen--Macaulay and has no
embedded associated primes. A section of its invertible restricted
line bundle that vanishes in all generic localizations is therefore
zero globally. Hence f^2|D is sigma invariant everywhere, including
at the intersection and through all nilpotent jets. Since the fixed
algebra is O_Gamma, it is a section pulled back from O_Gamma(2).

The entire conductor square now glues f^2 with that downstairs
section to O_X(2). The quartic hypersurface sequence lifts it to an
ambient quadric Q, with

    (X intersect V(Q))_red=C0.

The sole quadric through C0 is q=x0x3-x1x2, smooth. On this quadric
C0 has bidegree (1,3), while the restriction of the integral quartic
F has divisor class (4,4). It cannot be supported only on C0.
This contradiction excludes a mate in every positive degree.

### 5. Exact evidence and retained limits

The standalone
[verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_mf6_rhalf_scroll_2026_10_08.py)
reconstructs every parameterization coefficient, checks the carrier
binding to the recorded MF6 member, verifies the three quadratic
closure identities and all six conductor annihilator certificates,
and checks the entire pullback conductor ideal. Its
[JSON evidence](https://github.com/markluxton1/STCI/blob/6880e35bb6c7ec13c2ba18cc1a0cce328e1d795f/research/computations/verify_session_mf6_rhalf_scroll_2026_10_08.json)
records the source and input hashes. The all-mate conclusion is the
structural proof in sections 3--4, not a bounded numerical test.

During checker development, one assertion used the discriminant in
T=xw while labeling it as the discriminant in w; the exponent was
corrected from x^3 to x^5. A second assertion compared an expanded
polynomial with an unexpanded syntactic expression; it was replaced
by an exact difference check. Neither change alters the normalized
identities. Both earlier failures preceded the accepted PASS.

This example demonstrates that some nonreduced downstairs conductors
are tractable through actual finite flat algebras. It does not prove
every nonreduced ACM cubic conductor Gorenstein or every generic deck
action preserves its conductor primes. Those hypotheses must be
checked for another carrier. The unrestricted STCI problem and the
remaining principal-family strata are unchanged by this fixed-member
exclusion.

---

<a id="source-2026-10-08-session-mf6-rhalf-scroll-independent-auditmd"></a>

## Independent audit: the principal MF6 (p,r)=(8,1/2) carrier

Date: 2026-10-08. Status: **ACCEPTED all-mate exclusion** of this
fixed characteristic-zero member of the principal e=1,d2=1 family.
The audit does not exclude the entire principal family. In particular
the reduced-downstairs-conductor theorem is not applied: the actual
conductor here contains a double line.

Audited owner proof:
`2026-10-08-session-mf6-rhalf-scroll-conductor.md`.
Audited exact source:
`../computations/verify_session_mf6_rhalf_scroll_2026_10_08.py`.
The source was freshly replayed in this audit and returned PASS with
SHA-256 `9d532c25c9f50f206e0d57c5ce7f35b9feb54707bf1b630fd622c0c473028aa2`.
Its JSON binds the independently parametrized carrier to the saved
`rhalf_unique` quartic row and records its input hash. The computations
verify algebraic identities; the arbitrary-degree conclusion is the
structural argument checked below.

### 1. The carrier and finite normalization

The invertible coordinate change in the owner note gives

    L=96w+x-8y+4z, chi=x-8y, G=xL-8yz,
    -64F=G^2-x^3*chi.

As a quadratic in w, the discriminant is 9x^5*chi. It is not a
square in k(x,y,z), and the coefficients are primitive. Thus F is
irreducible by Gauss's lemma over every algebraically closed
characteristic-zero field. Using T=xw instead changes the displayed
discriminant by a square; confusing those two polynomial variables
does not change irreducibility, but the recorded w exponent five is
the correct one.

On S=P1_[a:b] times P1_[U:V], the four proposed sections have class
H=O(2,1):

    x=Ub^2, y=U(b^2-a^2)/8, z=Vb^2,
    w=[U(ab-a^2)-V(a^2+3b^2)]/96.

They have no common zero. At b!=0 the equations x=z=0 would force
U=V=0; at b=0, y=w=0 likewise forces U=V=0. Consequently their
morphism pulls O_P3(1) back to the ample H. A positive-dimensional
fiber on the projective S would contain a curve of H-degree zero,
impossible. The morphism is therefore finite onto its image.
The generic ratios G/x^2=a/b and x/z=U/V recover both parameters,
so it is birational. Substitution vanishes on F; irreducibility makes
its image the whole carrier. The smooth S is its normalization.

### 2. The complete normalization module and actual conductor

The extra sections v=Uab and u=Vab recover, together with the four
ambient sections, the complete six-dimensional space H0(S,H).
The O(2,1) section ring is generated in degree one: every monomial
of bidegree (2m,m) decomposes into m monomials of bidegree (2,1).
It is the normal quartic-scroll section ring B. The hypersurface
ring A is generated by x,y,z,w.

The exact relations in the owner note show that A+Av+Au is closed
under multiplication and contains the six degree-one generators.
Hence B=A+Av+Au, as a finite A-module. The two monic quadratic
relations for u and v also give finiteness directly. The six cubic
identities show that J=(x^2,xy,G) annihilates B/A; they prove
J subset I, not merely vanishing on the normalization defect support.

The Hilbert--Burch matrix

    [x,0; -z,x; L,-8y]

has maximal minors generating J, which has height two and support
x=0,yz=0. Its resolution gives Hilbert polynomial 3m+1. The entire
actual conductor I of this smooth-scroll normalization has the same
polynomial by finite duality and Riemann--Roch. Thus the coherent
quotient I/J has polynomial zero and is zero: every nonzero coherent
sheaf on projective space has nonzero Hilbert polynomial, since high
twists are generated by nonzero global sections and have no higher
cohomology. This proves equality of the projective conductor ideal
sheaves I=J; no Jacobian or reduced-support substitution occurs.

Pulling J back gives the common factor U^2b^2 times
b^2,(b^2-a^2)/8,ab. Those residual sections have no common zero on
P1. Therefore the actual upstairs conductor is exactly

    D=2E+2T,  E={U=0}, T={b=0},

with no isolated remainder. It is the anticanonical Cartier divisor
on S. Downstairs its support is two lines, one doubled.

### 3. Gorenstein center and rank-two trace on a nonreduced base

At every projective point some entry of the Hilbert--Burch matrix is
a unit: if x=y=z=0 then L=96w, and their simultaneous vanishing is
only the irrelevant affine origin. Row and column operations with
that unit reduce the localized grade-two ideal to two generators,
so Gamma=V(J) is a local complete intersection and Gorenstein.

The previously proved whole-conductor sequence

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0

makes p_*O_D locally free of rank two because omega_Gamma is
invertible. This argument is valid over the nonreduced Gamma and
does not assert flatness from Cohen--Macaulayness alone.

For any rank-two locally free algebra over a ring with 2 invertible,
trace splits it as R plus a tracefree invertible module. Locally a
tracefree generator eta has eta^2=Delta in R by Cayley--Hamilton;
the map eta->-eta is the canonical involution sigma, with fixed
algebra exactly R. These assertions remain true when R is
nonreduced. The hyperplane line bundle on D is pulled back from
Gamma and therefore has its canonical sigma action.

The unique reduced conductor component above the doubled base line
is E. Its reduced map has degree two, with parameter a/b determined
by its square. The unique reduced component above the other line
is T, mapping isomorphically. Thus sigma preserves each minimal
prime of D: it cannot exchange components lying over different
base primes. On the reduced E function field it is the quadratic
deck action a/b->-a/b; on T it is the identity. Preservation of
these primes, rather than a presumed involution on the whole
surface S, is the fact required by the next step.

### 4. Roots of unity retain every generic nilpotent jet

The mate hypothesis gives the full inverse support c isomorphic to
C0, with c~H and nu*G_mate=lambda*f^n, div(f)=c. The divisor c is
different from E and T, so f is a unit after restricting its line
bundle to either generic local Artin ring of D. Choose a local
line-bundle frame pulled back from Gamma. The ratio

    h=sigma(f)/f

is then an element of that Artin ring, with h^n=1 because the mate
power descends.

The polynomial T^n-1 factors into distinct linear factors T-zeta
with zeta in the algebraically closed constant field. In a *local*
Artin ring the reduction of h selects one such zeta. Every other
factor h-zeta' is a unit, so the product being zero forces
h-zeta=0 exactly. Thus there is no surviving nilpotent correction.
This factor argument is stronger and more explicit than checking
only a reduced field ratio. Characteristic zero is essential.

At E, sigma preserves the generic local ring and fixes constants.
Applying it twice to sigma(f)=zeta*f gives zeta^2=1. At T its
reduced field action is the identity, so the selected zeta is one.
Therefore f^2 is invariant in both generic Artin localizations.
This includes the generic nilpotent directions above the double line.

### 5. Extension and line-bundle descent

D is Cartier on the smooth surface S, hence Cohen--Macaulay and
without embedded associated primes. An invertible sheaf on D has
the same associated primes. A section vanishing at every generic
localization cannot have finite-support residue; it is zero globally.
Thus sigma(f^2)-f^2 vanishes everywhere on D, including its intersection
and all nilpotent jets there.

Since the fixed algebra of the trace involution is O_Gamma, the
canonical pullback line-bundle action identifies f^2|D with a section
of O_Gamma(2). The *entire* conductor square glues it with f^2 on S
to a section of O_X(2). The hypersurface restriction sequence lifts
that section to an ambient quadric. Finiteness shows its zero support
on X is exactly C0.

That is impossible: C0 lies on its unique smooth quadric with class
(1,3), while the carrier restricts to class (4,4). No positive
multiple of (1,3) equals (4,4). Therefore this fixed MF6 carrier
has no mate in any degree.

### 6. Audit decision and scope

The normalization, whole conductor equality, local Gorensteinness,
nonreduced-base trace algebra, prime preservation and generic-to-global
extension all pass this independent audit. The proof is accepted for
the specified p=8,r=1/2 principal member. It does not infer reducedness
of Gamma and does not apply a reduced-center theorem to this scheme.
Other principal parameters, other conductor schemes, and the
unrestricted STCI problem remain separate.

---

<a id="source-2026-10-08-session-new-results-acceptancemd"></a>

## Root acceptance of the October 8 scroll and defect-four results

Date: 2026-10-08. Fixed curve C0=[s^4:s^3t:st^3:t^4], over an
algebraically closed characteristic-zero field. This records proof
review, not a universal STCI resolution or a novelty claim.

This is the intermediate acceptance record. Its statements of pending
audit and the remaining reducible/nonreduced conductor boundary describe
that stage of the work. The
[late reconciliation](contact_duality_and_global_descent.md#source-2026-10-08-session-late-results-acceptancemd)
records the completed independent audits, full smooth-scroll exclusion,
principal ancestor closure and current remaining strata.

### 1. Every integral quartic singular along a smooth twisted cubic

**Accepted:** such a quartic has no mate cutting out C0 set-theoretically,
in any positive degree. The [applicability proof](../supplements/QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md)
and [conductor criterion](contact_duality_and_global_descent.md#source-2026-10-08-session-irreducible-conductor-compressionmd)
together supply the argument. The [independent adversarial audit](../supplements/QUARTIC_SCROLL_REDUCED_CONDUCTORS.md)
checks the criterion and the entire-conductor Hilbert/CM calculation.

The complete derivative restriction on all 35 quartic monomials has
rank 29. Six independent products of the three twisted-cubic quadrics
span the kernel. The independent [literal-minor source](https://github.com/markluxton1/STCI/blob/088b0c191e470b032fff0ef0cfac1d830607800b/research/computations/audit_scroll_twisted_cubic_equation_space_2026_10_08.py)
rebuilds derivatives by substitution and computes the stated determinant
104509440 by Fraction elimination. Root replay passed in the isolated
continuation snapshot. Thus F=Q(xi1,xi2,xi3) holds for the entire
equation space, without an slc assumption. If Q factored, F would factor
into nonzero quadratic factors; hence integral F gives a smooth conic Q.

The two syzygies define a rank-two matrix at every point of P2. Their
incidence variety is therefore a smooth P1 bundle, agreeing with the
blowup of the smooth twisted cubic. The inverse image S of Q is a smooth
P1 bundle over a smooth conic. The exceptional fiber over each point of
the twisted cubic maps to a line in P2, which a smooth conic cannot
contain. Every fiber of S->X is finite, including tangencies, so this
proper birational map is finite and is the normalization. Off the cubic
it is an isomorphism. A normal local ring on the cubic would also make
it an isomorphism there; since S is smooth and X is singular there,
this is impossible. The whole nonnormal support is exactly the cubic.

Adjunction gives K_S=-E|S, H^2=4 and K_S.H=-6. Finiteness makes H ample,
and H has ruling degree one. On F_e this implies H=C_min+a f,
2a-e=4 and a>e, hence e=0 or 2. These verify the smooth quartic-scroll
hypotheses used by the criterion.

Finite absolute duality identifies the conductor with nu_*omega_S,
not with a relative formula requiring nu to be flat. It is maximal CM
over the quartic surface. Its quotient is a pure CM curve with Hilbert
polynomial 3m+1. Degree three and the smooth degree-three support force
generic multiplicity one. Any nilradical would then be supported at
finitely many points, prohibited by depth one. Thus the actual downstairs
scheme is the reduced smooth twisted cubic. The upstairs conductor is
Cartier and CM, finite over the smooth curve, and torsionfree over each
local DVR; it is flat, of rank H.D/3=2.

The root reviewed all three rank-two conductor cases. For integral
reduced D, invariance of f^n gives sigma(f)/f=+1 or -1, and f^2 descends
through the full conductor square. For reducible D, its algebra is
O+O(-2) with eta^2=q_2^2. Unequal branch factors force both restrictions
to be scalar multiples of q_2 times a linear section. Singleton fibers
put that section's zero at a branch intersection; a smooth lifted curve
cannot have contact greater than the mutual branch contact with both
branches. For nonreduced D, eta^2=0, and the all-n coefficient
n*a^(n-1)*b forces b=0, so f itself descends. The resulting quadric or
hyperplane mates are impossible for C0. The argument uses global
constant units, whole conductor schemes and full inverse support.

The primary equation/blowup presentation was checked in
[Ducat, section 5.7](https://d-nb.info/1317691679/34). The independent
equation certificate removes reliance on extending that paper's slc
classification. The absolute-duality input was checked against
[Stacks 0AX0](https://stacks.math.columbia.edu/tag/0AX0) and
[the CM concentration lemma](https://stacks.math.columbia.edu/tag/0AWQ).

**Boundary:** reducible/nonreduced downstairs conductors, singular
normalizations, other quartic classes and higher carrier degrees remain
outside this theorem.

### 2. Both algebraic e=1,d2=4 ancestor directions

**Accepted:** for A=r*z,B=1,12r^2+4r+3=0, every genuine defect-four
triple has at most one containing quartic. Hence it cannot supply two
independent quartic multiplier equations for the fixed ancestor targets.
This is the narrow [defect-four proof](contact_duality_and_global_descent.md#source-2026-10-08-session-localcoh-e1-d4-algebraicmd),
not an STCI mate theorem.

The root checked the explicit seven ambient forms, their complete
35-column double conditions, and their normalized h/E coefficients.
Rank 28 of the complete double matrix and independence of the seven
forms establish completeness. Arithmetic in the quadratic field covers
both embeddings. The two free primitive h coefficients uniquely match
the constant and eighth coefficients of delta*E, so the quartic fiber
is exactly the kernel of the remaining seven-by-five operator.

The minors d0^4 and d4^4 give rank at least four on those two opens.
On d0=d4=0, the minors d1^5 and d3^5 give rank five when either is
nonzero. The final delta=d2*z^2 matrix has five pairwise distinct
diagonal constants, so at most one diagonal entry vanishes. This covers
all homogeneous delta, including repeated and infinity roots, and
proves kernel dimension at most one everywhere.

For theta=0, the local ideal (delta*m,my,m^2,y^3) leaves
R/(delta)*m torsion at every defect zero. A nonzero section of O(4)
has such a projective zero, so this is not a valid finite-flat triple.
Every genuine triple therefore has theta!=0, which is normalized to
one by scaling the equation. This discards no valid theta=0 boundary.

The self-contained
[algebraic checker](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_localcoh_e1_d4_algebraic_2026_10_08.py)
reconstructs the ambient space and verifies the minor and diagonal
identities. The theta-zero torsion argument above supplies its separate
finite-flatness implication.

**Boundary:** the principal obstruction-zero direction and directions
with nonzero primitive quadratic obstruction remain open at positive
D2. This does not exclude every defect-four Gorenstein quadruple.

---

<a id="source-2026-10-08-session-nonimmersion-prime-independent-auditmd"></a>

## Independent audit: the generic nonimmersion-prime obstruction

Date: 2026-10-08. Auditor: `verification`. Status: **PROVED HERE**, independently audited from the full power identity. This note does not classify all nonnormal quartic surfaces.

### Exact statement

Let k be algebraically closed, let S be a smooth projective surface, and let nu:S -> X subset P^N be finite and birational. Write H=nu^*O_X(1). Suppose a smooth integral curve c on S satisfies c~H, there is f in H^0(S,O_S(H)) with divisor c, and an ambient homogeneous polynomial G of positive degree n satisfies

    nu^*G=lambda f^n, lambda in k^*.

Suppose that nu|c is an immersion into P^N. Assume n is nonzero in k; in particular the statement applies in characteristic zero. If E is any integral curve distinct from c with H.E>0, then dnu has generic rank two along E.

Neither smoothness of E nor a conductor hypothesis on E is required. A finite normalization of a smooth rational quartic scroll has H ample, so every actual conductor prime satisfies the positive-intersection hypothesis. The previously audited full-support mate reduction supplies exactly c, f, and the power identity in that application.

### Proof, including singular E and the point f=0

Because c.E=H.E>0 and E is distinct from c, choose a closed point P in c intersect E. Suppose that dnu has generic rank at most one along E. On any local chart, every two-by-two minor of its derivative matrix vanishes in k(E). The entries are regular and E is integral, so those minors vanish modulo the prime ideal of E. Hence the rank of dnu at P is at most one. Rank zero would already contradict immersion of c; its rank is therefore exactly one.

Choose an ambient hyperplane section h nonzero at nu(P). Its pullback trivializes H near P, and the target is in the affine chart h!=0. Trivialize the smooth source tangent bundle near P. Let q_1,...,q_N be the pulled-back affine target coordinates, and write a derivative row as (a,b), with at least one entry a unit at P. The regular vector field

    V=(-b,a)

in this tangent frame is nonzero at P. It kills that row identically. Its pairing with every other derivative row is a two-by-two minor, up to sign, so

    V(q_i)=0 modulo I_E for every i.

This is the required kernel construction. It works over the singular ring O_E: a unit pivot and vanishing minors suffice. There is no need to regard E as a smooth curve, to extend an a priori kernel line bundle, or to assume a global involution.

Put g=f/(nu^*h) and A=G/h^n. These are respectively a source regular function and a target affine regular function, with

    nu^*A=lambda g^n.

The chain rule gives V(nu^*A)=0 modulo I_E, and differentiation gives

    n lambda g^(n-1) V(g)=0 in O_E.

The image of g in the local domain O_E is nonzero: its divisor on S is c, distinct from E. Cancel its nonzero power in that domain, using n lambda!=0, to obtain V(g)=0 in O_E. The resulting equality is regular at P, so dg_P(V(P))=0. This cancellation takes place before specializing at g(P)=0; it does not divide by g(P).

Since c is smooth, dg_P is nonzero and its kernel is the one-dimensional tangent line T_Pc. The nonzero vector V(P) both lies in that tangent line and is killed by dnu_P. This contradicts immersion of nu|c. Thus the assumed generic rank deficiency is impossible.

### A local-unit variant and exact limits

The same cancellation argument even permits a local identity nu^*A=u g^n for a regular unit u, provided that A is an ambient function. Differentiation modulo I_E gives

    g^(n-1) (n u V(g)+g V(u))=0.

After cancelling in O_E and evaluating at P, where g(P)=0, one again obtains V(g)(P)=0. The global constant-power identity available in the scroll application is stronger than needed for this local argument.

The proof does not apply to an isolated rank-drop point on a prime which is generically immersive. It does not infer rank deficiency merely from an upstairs conductor multiplicity. A claim that a concrete conductor branch is excluded must establish its generic derivative rank from the actual normalization morphism or from a valid transverse singularity argument. In characteristic dividing n, the derivative of g^n loses the necessary information.

### Relation to the current frontier

This independently agrees with the separate [normal-global audit](#source-2026-10-08-session-normalization-differential-independent-auditmd), whose proof uses the equivalent constant-rank kernel over O_E. Agreement is not the proof: the unit-pivot argument above independently establishes the extension across singular E and across c intersect E.

For an integral quartic with smooth rational quartic-scroll normalization, any mate of the fixed smooth rational quartic C0 must therefore leave the normalization generically immersive along every actual conductor prime. The generic Artin classification or geometric transverse branch classification still has to establish which conductor possibilities have that property; the obstruction alone is not a closure of that carrier class.

No frontier file was changed by this audit.

---

<a id="source-2026-10-08-session-normalization-differential-independent-auditmd"></a>

## Independent audit: a rank-deficient normalization prime obstructs a mate

Date: 2026-10-08. Auditor: `normal_global_adversarial`. Status: **PROVED HERE,
independently accepted**, with the hypotheses below. No claim about all
nonnormal quartics is made by this lemma alone.

### Statement

Let k be an algebraically closed field of characteristic zero. Let
nu:S->X subset P^N be a finite birational morphism from a smooth projective
surface. Put H=nu^*O_X(1). Suppose there is a smooth integral curve c on S,
a section f of O_S(H) with div(f)=c, and a homogeneous polynomial G of
degree n>0 such that

    nu^*G=lambda f^n,       lambda in k^*,

as sections of O_S(nH). Suppose also that nu|c maps isomorphically to a
smooth embedded curve in P^N. Let E be an integral curve on S distinct
from c, with H.E>0. Then the differential

    dnu:T_S|E -> nu^*T_(P^N)|E

has generic rank two.

Equivalently, a prime E of generic differential rank at most one and
positive H-degree contradicts this collection of hypotheses. The curve
E need not be smooth, and E need not be a conductor prime. In the
application, E is an actual conductor prime and c~H, with H ample.
The characteristic assumption can be weakened to n nonzero in k.

### Proof with the extension at f=0 retained

Since c.E=H.E>0, choose a closed point P in c intersect E. The immersion
nu|c into P^N implies that dnu_P is nonzero on the tangent line T_P c.
In particular its rank is at least one.

Assume that dnu has generic rank at most one on E. Every two-by-two
minor of a local matrix for dnu is then zero in the function field of
the integral curve E, hence zero in O_E wherever that matrix is defined.
Consequently the rank at every point of E is at most one. At P it is
exactly one. After shrinking an open neighbourhood of P in E, an entry
of the matrix is a unit, so the map has constant rank one on that
neighbourhood. Its kernel K is therefore a line subbundle of T_S|E.
This elementary constant-rank assertion holds over O_E even when E is
singular: use the unit entry to perform row and column operations; all
remaining matrix entries vanish because its two-by-two minors do.

Choose an ambient hyperplane section h with h(nu(P)) nonzero, and shrink
the neighbourhood in S so that nu^*h is a unit frame for O_S(H). Write

    f=g nu^*h,        A=G/h^n on the ambient affine chart.

The global equality of sections becomes the equality of regular
functions

    nu^*A=lambda g^n.

For any local generator v of K, the differential of every ambient
function annihilates v, so

    0=d(nu^*A)(v)=lambda n g^(n-1) dg(v) in O_E.

The section g is nonzero at the generic point of E because E is
distinct from div(f)=c. The local ring O_E is a domain. Since n is
invertible, cancellation in this domain gives dg(v)=0 as a regular
section along E, including at P. This is the precise extension step:
no division by the value g(P)=0 is made.

At P, g is a local defining equation of the smooth curve c. Thus dg_P
is nonzero and ker(dg_P)=T_P c. The nonzero line K_P lies in this
kernel; both are one-dimensional, so

    T_P c=K_P=ker(dnu_P).

This contradicts the immersion of nu|c. Hence the generic rank on E
is two.

If the generic rank on E were zero, all matrix entries would vanish
on E and already contradict the immersion at P. The proof therefore
also handles the rank-zero case.

### Applicability to the scroll frontier

The previously audited mate reduction supplies exactly the required
data when S is a smooth rational quartic-scroll normalization of an
integral quartic carrying C0: the full inverse image of C0 is a single
smooth curve c isomorphic to C0, div(nu^*G)=n c, the torsion-free Picard
group gives c~H, and a section f with div(f)=c satisfies the full power
identity up to a constant. Finiteness makes H ample, so H.E>0 for
every conductor prime E.

Therefore every surviving smooth-scroll mate must have differential
rank two at the generic point of every actual upstairs conductor
prime. In particular a generically cuspidal normalization branch,
where one tangent direction is killed by the normalization map, is
excluded if that rank-one statement is verified for the actual
surface morphism. A conductor multiplicity by itself does not verify
that statement; the local normalization or transverse singularity
must still be identified.

For the proposed residual F2 divisor D=4F+2C_min, the implication is
conditional only on the local geometric identification of F as a
rank-deficient cuspidal branch. Once that identification is proved,
the lemma excludes it without any Gorenstein assumption on the
downstairs conductor and without extending a trace involution through
a nongorenstein point.

### Adversarial checks

- The argument differentiates the entire power identity, not its first
  normal coefficient or a chosen jet truncation.
- It uses a hyperplane frame pulled back from the ambient space; a
  general local frame could have a nonzero derivative on K.
- It cancels g only in the domain O_E before specialization, then
  specializes the regular equality dg(v)=0 at P.
- A local kernel generator need only be defined along E. A lift to a
  vector field on a neighbourhood of S is unnecessary: differentials
  restricted to E already pair with T_S|E.
- Singular E is harmless because a unit matrix entry and vanishing
  two-by-two minors give a locally free kernel near P.
- The positive intersection and the smooth embedded image are
  essential. Without either, the tangency contradiction need not
  arise. Characteristic dividing n invalidates the cancellation.

This is a structural obstruction. It does not by itself classify the
remaining nonreduced nongorenstein ACM cubic conductors.

### 2026-10-09 addendum: the local unit factor is harmless

Status: **PROVED HERE, independently accepted**. This is a stronger
local version. It does not require a global root section, a constant
factor, rationality of S, or a prescribed carrier degree.

Let nu:S->X subset P^N be a morphism, let P belong to a smooth integral
curve c on S, and suppose S is smooth on an open neighbourhood of P.
Assume nu|c is an immersion at P. Let E be an integral curve through P,
distinct from c, and suppose dnu has generic rank at most one on E.
If an ambient regular function A has pullback

    nu^*A=u f^m

near P, where f is a local defining equation of c, u is a regular unit,
m>0, and m is nonzero in the ground field, these hypotheses contradict
one another.

Indeed, the zero-minor argument in the original proof works on the
integral E near P. Rank zero at P already contradicts immersion; if
rank one, its kernel has a regular line generator V near P on E.
Pairing the differential of the entire equality with V gives

    0=f^m du(V)+m u f^(m-1) df(V) in O_E.

Since E is distinct from c, f is nonzero in the domain O_E. Cancel
f^(m-1) in that domain, obtaining the regular equality

    f du(V)+m u df(V)=0 in O_E.

Now specialize at P. The first summand vanishes because f(P)=0;
m and u(P) are nonzero, so df(V)_P=0. Smoothness of c identifies
ker(df_P) with its tangent line, and the nonzero kernel line of dnu_P
is precisely this line. This contradicts the immersion of nu|c.

Here V need only be a section of T_S|E. Pairing differentials with V
defines a derivation from O_S to O_E with the usual Leibniz rule; no
vector-field extension off E and no intrinsic derivation of O_E are
needed. The unit need not be a pullback from the ambient space.
The argument does not claim df(V)=0 at every generic point: for a
nonconstant unit, its regular relation with du(V), followed by
specialization at P, is what proves the contradiction.

#### Consequence for an arbitrary finite smooth normalization

Let nu:S->X subset P^N now be finite with S smooth projective, and put
H=nu^*O_X(1). Suppose an ambient form G of degree b>0 has the entire
pullback divisor

    div(nu^*G)=m c,

where c is smooth integral, m>0 is nonzero in the ground field, and
nu|c is an immersion. On an affine chart obtained by dividing by a
nonvanishing ambient hyperplane to degree b, the pulled-back form is
u f^m with u a regular unit: equality of Cartier divisors on the
regular local ring at P provides this factorization.

The divisor identity gives m c~bH. Since H is ample, c is ample as
well (an invertible sheaf is ample if a positive tensor power is).
Consequently c meets every integral curve E distinct from c. Applying
the local lemma at such an intersection shows that dnu has generic
rank two on every such E. This includes every conductor prime
distinct from c, without requiring c~H, Picard-group torsion-freeness,
a global section cutting out c, or a globally constant power factor.

#### Exact boundaries of the strengthening

- The distinction E!=c is essential. If E=c, the restriction of f to
  E is zero and the cancellation in its domain is unavailable.
  Ampleness ensures intersections with other primes; it does not
  remove this exception.
- The entire local pullback divisor must be m c near the chosen P.
  If another component of div(nu^*G) passes through P, its factor is
  not a unit and the specialization need not force df(V)_P=0.
- Immersion of nu|c at P is a separate hypothesis. A single smooth
  inverse-image curve alone does not establish it.
- Only smoothness of S near the selected P is needed, but the argument
  gives no conclusion when that intersection lies in the singular
  locus of a normalization. The singular-normalization boundary
  therefore remains.
- Characteristic dividing m invalidates this proof. Characteristic
  zero makes the relevant multiplicity automatically invertible.

No new classification of nonnormal carriers follows solely from this
local strengthening. The earlier historical nongorenstein-scroll
boundary was subsequently closed by the separate
[complete scroll audit](../supplements/QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md).

---

<a id="source-2026-10-08-session-principal-e1-d1-independent-completeness-auditmd"></a>

## Independent completeness audit of principal e1,d2=1 quartic ancestors

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]`, characteristic zero.
Scope: the principal `a0*b1!=0` direction lane for a genuine second defect
of degree one, in the accepted canonical-triple reduction for common
quartic ancestors. This audit combines the complete open-frame proof
with fresh all-35-column boundary calculations. No frontier
file is edited.

**ACCEPTED, with the recorded antecedents:** no quartic common ancestor
for the independent fixed targets u,v has such a canonical triple. The
complete quartic fibre has dimension one throughout the declared open
and at its remaining genuine boundary points, except the node
`(p,r)=(2,1/2)`. The node has dimension four with a fixed cubic factor
and is excluded for ancestors by P-037. A literal uniform dimension-one
claim on the entire principal lane would be false.

This is an ancestor exclusion. A dimension-one containing-quartic space
does not by itself prohibit that single quartic from having an STCI mate
of some other degree. No all-mate carrier theorem is inferred here.
Other e-strata, second-defect degrees, higher multipliers, positive
characteristic, and the universal problem retain their separate scopes.

### 1. Parameter and triple coverage

For `b0!=0`, common direction scaling and the actual ambient torus give
the representative

```text
A=1+r*z, B=1+p*z,
p!=0, p-r!=0,
H=8p^3-(64r^2+128r+16)p^2
 +(96r^4+512r^3+592r^2+128r+6)p
 -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9)=0.
```

Here p nonzero is the principal condition and p-r nonzero is basepoint
freedom of the homogeneous linear direction pair. No arbitrary change
of the support coordinate or conormal frame is used to normalize it.
The accepted quadratic cocycle has coordinates c1,c2,c3 with
`H=64(c1*c3-c2^2)`. Its linear killing-section matrix is
`[[c1,c2],[c2,c3]]`.

Away from c1 zero the unique defect section is

```text
delta=-8c2+8c1*z=(2r+1)(8p+12r^2+4r+3)-p*P*z,
P=2p+12r^2+16r+9,
Gamma=the polynomial part of delta*h2.
```

The correction is unique because `H0(O(-4+d2))=H0(O(-3))=0`.
On pP nonzero, the z coefficient of delta is nonzero, so its homogeneous
degree-one section has no infinity zero. The exact resultant
`Res_z(delta,Gamma)=p^4*P^4/8` proves flatness at its finite zero.
Repeated-root assumptions do not enter this argument.

If c1=c2=0 and c3 nonzero, the correct alternative killing section is
`delta=1` in the finite chart, a homogeneous section with its zero at
infinity. It must not be replaced by the identically zero expression
`-8c2+8c1*z`. The boundary source explicitly makes this switch. The
surviving c3 gives the nonzero opposite-chart correction at that zero;
its negative has norm 24 over the quadratic field on the two affected
fibres. Thus these fibres are retained rather than deleted by the
generic choice of killing section.

The actual projective coordinate change was independently checked.
The raw reversed-chart normals have linear transition
`(Uraw_inf,Vraw_inf)=z^-7*(V/2,2U)`. Taking
`Uop=Vraw_inf/2,Vop=2Uraw_inf` gives the balanced opposite chart
`x3=1,x2=w,x1=w^3+2Uop,x0=w^4+Vop/2+3wUop` and the direction
`A_inf=r+w,B_inf=p+w`. The literal-form companion uses exactly this
chart. It computes `Gamma_inf=3w^2+(-6+3a)w+4/3-10a/3`, with
`a^2=-2`, by exact zero-remainder division of the actual quadratic
coefficient; its constant is `-c3`, of norm 24. This verifies genuine
flatness at infinity in the actual frame, beyond a finite-chart
resultant with constant delta.

The `b0=0` chart is also retained. Its weighted H equation specializes,
after scaling r to one, to
`p^3-8p^2+12p-72=0`. Before that scaling, r zero would force p zero,
contradicting the principal condition. These are exactly three geometric
points. The cubic has no root modulo five: its values at 0,1,2,3,4 are
`3,3,3,4,2`. Hence it is irreducible over QQ; its discriminant is
`-160704`, so the three characteristic-zero embeddings are distinct.
One exact cubic-field calculation therefore covers all three points.

### 2. Complete frame on the open

Put

```text
T=2p-4r^2-4r-1, S=p-2r-1, Q=12r^2+20r+11,
U={H=0, p*P*(p-r)*(2r-1)*T!=0}.
```

The audited open source reconstructs eighteen independent actual
quartics vanishing on C0. These forms contain no direction parameters;
their only free symbols are the four ambient coordinates. All 35
ambient quartic monomials restrict to
the seventeen distinct powers `z^0,...,z^16`; consequently the curve
restriction has rank 17 and these eighteen forms span the full ideal
space in degree four.

The actual first-normal matrix M1 has shape `11x18`. Its columns

```text
0,1,2,3,4,5,6,11,12,14,15
```

have the exact determinant

```text
D=p^4*(p-r)*(2r-1)*T^2/256.
```

The raw saved seven-column kernel N satisfies `M1*N=0`, and its rows
`7,8,9,10,13,16,17` are precisely the diagonal matrix `-D*I7`.
Thus M1 has rank eleven and N has rank seven in **every** fibre of U;
rank-nullity proves N is the complete kernel there. This statement
does not assume a generic nullspace specializes correctly. The new
independent countercheck reconstructs M1 from the actual quartic jets
and recomputes the determinant and the raw diagonal identities.

The source divides the seven columns by their recorded polynomial gcds.
Every divisor is a unit on U. Its normalized free determinant is
`-p^8*(2r-1)^6*T^11/2^52`. It then reconstructs the second contact map
from the exact condition `delta*q2-Gamma*h=0`. On H zero all but six
contact rows vanish, with the seventh row a multiple of H. The six
recorded row divisions use only p and p-r, also units on U. The resulting
`6x7` matrix is therefore the contact operator on the complete
first-normal kernel, without omitted quartics.

### 3. Two cofactors, their exact norms, and the nonunit S branch

The open verifier recomputes all seven actual maximal cofactors before
reducing modulo H, and checks their retained factorizations. The
cofactors omitting columns six and five have the shared prefactor

```text
(27/2^51)*p^5*(2r-1)^4*(2r+1)^3*S^3*T^7,
```

times the recorded residuals R6 and R5. The factor 2r+1 is also a unit
on U: `H(p,-1/2)=8p(p+2)^2` and `P(p,-1/2)=2(p+2)`, so every point
there violates pP nonzero. S is **not** a unit and is handled separately.

On S nonzero, if both cofactors vanished at a point of H, R6 and R5
would vanish. Their two resultants in p would both vanish at its r
coordinate. The exact resultant gcd is, up to a nonzero rational scalar,

```text
(2r-1)^16*(2r+1)^26*Q^5.
```

The r-half fibres have already been removed on U. Q has discriminant
`-128`, so it defines a quadratic field. Exact Euclidean polynomial
division at one root, together with an extended-Euclidean identity,
gives `gcd(H,R6,R5)=p-(2r+1)`; conjugation covers its other root.
But `P(2r+1,r)=Q`, so this common root violates P nonzero. Therefore
the two cofactors cannot vanish simultaneously on this part of U.
Leading-coefficient specializations of a resultant can only add
possible exceptional r values; they cannot conceal a finite common
root. The exact gcd and field-fibre calculation remove those possible
extras rather than assuming generic resultant sufficiency.

The entire S-zero branch is retained using

```text
H(2r+1,r)=-(2r-1)^2*(2r+1)*(6r+1)*Q,
P(2r+1,r)=Q.
```

Only `r=-1/6,p=2/3` survives the U conditions. Its actual cofactor
omitting column four is
`1073741824/36472996377170786403`, nonzero. The independent countercheck
also verifies the full first/contact matrix in the eighteen-dimensional
ideal space has rank 17 there. Consequently the contact rank is six
everywhere on U, and the complete containing-quartic space has dimension
`18-11-6=1`.

### 4. Exhaustive complement and fresh ambient boundary evidence

The independent countercheck verifies the precise polynomial identities

```text
H|P=0=-9*(2r+1)^2*Q^2,
H|T=0=-9*(2r-1)^2*(2r+1)^4,
H(p,1/2)=8*(p-8)*(p-2)^2,
H(p,-1/2)=8*p*(p+2)^2.
```

Thus the entire valid complement of U in the b0-nonzero principal chart
consists of the two r-half points and the two Q-root points with
`p=2r+1`, together with the primitive point `p=-2,r=-1/2`. The p-zero
case is nonprincipal; p=r violates basepoint freedom. At the primitive
point all c_i vanish. Its unique primitive correction multiplied by
any degree-one defect shares the zero of that defect, and there is no
additional `H0(O(-3))` correction. It cannot be a genuine positive-defect
finite-flat triple, as in the accepted defective-triple module argument.

The boundary verifier recomputes all 35 ambient monomial columns from
scratch, imposing curve restriction, first normal vanishing, and the
quadratic contact condition in the appropriate exact field. It does
not specialize N at a frame boundary. It asserts the expected ranks
and verifies the complete nullspace, not just a supplied form.

| Genuine parameter fibre | Full 35-column rank | Quartic dimension |
|---|---:|---:|
| `r=1/2,p=2` | 31 | 4, fixed cubic times every linear form |
| `r=1/2,p=8` | 34 | 1 |
| `Q=0,p=2r+1`, both roots, `delta=1` | 34 | 1 |
| `b0=0`, all three cubic-field points | 34 | 1 |
| `r=-1/6,p=2/3` within U, independent frame cross-check | 34 | 1 |

At the node, the four normalized quotient linear forms after dividing
the common cubic C are `x0,x1,x0+x1/2+x2/2,x3`. They span the complete
four-dimensional linear space. If `F*alpha=u,G*alpha=v`, then
`F=C*L,G=C*M` would yield a common ancestor `C*alpha` with linear
multipliers L,M. It is nonzero because u is nonzero, contradicting the
all-stage P-037 theorem. Elsewhere the two quartics would be proportional
in their dimension-one space, contradicting target independence.

These arguments exhaust the principal direction lane for the stated
ancestor problem. They neither decide a higher-degree mate for one
unique carrier nor use an STCI-only second-defect bound.

### 5. Exact support and scope

The rank-open argument and its hypotheses are given in
[the detailed proof](#source-2026-10-08-session-mf6-principal-rank-open-independent-auditmd)
and
[`verify_session_mf6_principal_rank_open_2026_10_08.py`](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_mf6_principal_rank_open_2026_10_08.py).
The source uses the corrected free-determinant denominator `2^52` and
exact expanded polynomial differences for its coefficient comparisons.

The independent
[`coverage-countercheck.py`](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/validation/2026-10-08-principal-e1-d1-audit/coverage-countercheck.py)
checks the determinant, diagonal, complement identities,
opposite-correction norm, cubic irreducibility and S-zero rank from the
actual contact input. It invokes no existing verifier and regenerates no
proof inputs.

The all-35-column
[boundary source](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08.py)
and its retained
[complete field data](https://github.com/markluxton1/STCI/blob/6880e35bb6c7ec13c2ba18cc1a0cce328e1d795f/research/validation/2026-10-08-principal-e1-d1-audit/research/computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08_all.json)
supply the boundary calculations. The actual two-chart
[residue source](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_mf6_e1_d1_principal_boundary_residues_2026_10_08.py)
and independent
[`residue-input-comparison.py`](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/validation/2026-10-08-principal-e1-d1-audit/residue-input-comparison.py)
bind the three literal quartics, direction parameters, cocycles,
defect sections and finite corrections to that complete-35-column data.
The comparison also derives the raw normal transition from the actual
coordinate change. The companion's cubic-pole conclusions are separate
necessary bounds; they do not strengthen this audit into an all-mate
carrier exclusion.
