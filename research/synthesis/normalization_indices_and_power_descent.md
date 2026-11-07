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

The [quintic carrier-structure proof](../supplements/QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit)
already proves a stronger useful reduction than the elementary denominator
[normalization-index test](#a-normalization-index-constraint-for-any-smooth-support). For a hypothetical nonnormal quintic with **Gorenstein
normalization**, the general hyperplane genus must be one. That normalization
is the degree-five del Pezzo surface with a single A4 point, `K_X=-H`;
c meets an interior A4 vertex and `5c~4H`. This is inherited evidence,
not a newly proved classification of arbitrary nonnormal quintics.

The exact marked pair and actual projection parameters are in the
[intrinsic classification](../supplements/DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#1-dp5-a4-intrinsic-pair-classification)
and [explicit-model audit](../supplements/DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#2-dp5-a4-explicit-model-independent-audit).
Its actual normalization conductor is `O_X(-2H)`. The downstairs conductor
Gamma has degree five and arithmetic genus two, and

    nu_*O_X/O_S = omega_Gamma(-H).                         (8)

No smoothness, reducedness, or globally finite-flat double-cover structure
for the conductor is inferred from those degree and genus numbers.

On the complete open affine chart `X minus ell=A2(r,T)`, the quartic root
q is exactly T^5 in the chosen H-frame. The actual four projection sections
are recorded in
[the actual target-fiber equations](../supplements/NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md).
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
[arithmetic equations and jet gaps](../supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md).
The plane-curve construction and residual-preservation identity above
locate the missing input in actual support and homogeneous section images.
