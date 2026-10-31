# Root-adjoining defect and the need for a singular conductor

Date: 2026-10-31. Status: **independently reviewed provisional conditional
exclusions and local-to-global defect formula**.
The curve is the fixed characteristic-zero quartic
`C=[s^4:s^3t:st^3:t^4]`. The hypotheses below are additional conditions
on a hypothetical quintic–octic presentation, not an exhaustive reduction
of all nonnormal carriers. No canonical promotion or STCI exclusion is
asserted outside the precise subclasses stated below.

The strongest conclusion of this note is in §8: a Gorenstein-normalized nonnormal
quintic with smooth integral conductor has no mate in any degree. In
the (5,8) case, an integral conductor must be singular at a point of C.
The complete nonnormal quintic problem and unrestricted STCI remain open.
The later [Gorenstein-normalization exclusion](2026-10-31-quintic-gorenstein-normalization-exclusion.md)
removes all conductor hypotheses. The defect calculation here remains
useful within its precise scope.

## 1. Exact source and claim

Let S be an integral nonnormal quintic carrier with an actual octic mate
whose intersection has sole reduced support C. Suppose its normalization
`nu:X->S` is Gorenstein. Reuse the exact conclusions of the
[quintic structural audit, §§4–7](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md):
X is the degree-five Gorenstein del Pezzo source with one A4 point; the
full inverse curve c maps isomorphically to C; and, with H the pulled
hyperplane class,

    div(q)=5c,   q in H^0(X,4H),
    q not in H^0(S,O_S(4)),   q^2=nu*G8.                 (1)

The last equality permits a nonzero scalar rescaling. The non-descent
uses the accepted [quartic exclusion](../results/quartic_carrier_exclusion.md).
The same structural audit gives the full conductor curve Gamma and
normalization quotient

    degree Gamma=5,   p_a(Gamma)=2,
    B/A = omega_Gamma(-1),                              (2)

where `A=O_S` and `B=nu_*O_X`. Gamma is Cohen–Macaulay as a scheme.

**Additional hypothesis in this note: Gamma is integral as a scheme.**
An integral support with a nonreduced conductor structure is insufficient.

Define the intermediate finite algebra A' by adjoining q in local
hyperplane frames:

    A'=A + image(O_S(-4) --q--> B).                      (3)

It is closed under multiplication by (1). The claim is

    length(B/A')=17,    support(B/A') is contained in C.  (4)

Thus adjoining the missing quartic root leaves precisely seventeen
units of failure of normalization, all at finitely many points of C.
This is a condition on an actual embedded carrier and actual descended
square. It is not a bound on another mate degree.

## 2. The total length

Compose multiplication by q with the quotient B/A. The conductor
annihilates B/A, so the resulting map factors through

    O_Gamma(-4) --delta(q)--> omega_Gamma(-1).            (5)

It is nonzero because q does not descend. Both sheaves are torsion-free
of rank one on integral Gamma. The map is therefore injective, is an
isomorphism at the generic point, and has zero-dimensional cokernel.
Its image is precisely A'/A.

The established Hilbert polynomial for the right side is `5n-4`.
For the left side,

    chi(O_Gamma(n-4))=5(n-4)+1-2=5n-21.

Subtracting gives length 17. Equivalently, delta(q) is a nonzero section
of the rank-one dualizing sheaf `omega_Gamma(3)`, with a cokernel of
length 17. When Gamma is smooth this is its zero divisor; singular
Gamma requires the sheaf cokernel formulation.

The image calculation depends on integrality. If Gamma has multiple
components, delta(q) can vanish on one of them. If Gamma is nonreduced,
generic torsion-free rank-one reasoning on its reduced support does not
give (5). Those cases remain outside (4).

## 3. Why the finite defect lies on C

The following local argument isolates the extra role of the hypersurface
embedding. Let p be a closed point of S outside C. Trivialize the
hyperplane bundle there. Then `g=q^2` is a unit in the local ring A,
because the actual octic has support C on S.

Complete the smooth ambient local ring at p. It is a complete regular
local UFD R, and the completed carrier is `R/(F)`. Excellence and
reducedness imply that this hypersurface is reduced. Factor

    F=unit * product_i f_i

into distinct irreducible analytic branch equations. Normalization
commutes with this completion in the present excellent finite-type
setting and is the product of the normalizations of these branches.

The unit g has a square root h in R/(F), by Hensel lifting over the
algebraically closed residue field in characteristic zero. On each
normal domain branch, `(q/h)^2=1`, so q/h is either +1 or -1. Partition
the branches by these signs, and write f_+ and f_- for the respective
products. Adjoining q is equivalent to adjoining the idempotent

    e=(1+q/h)/2.

It separates exactly the two sign groups. The completed A' is therefore

    R/(f_+) times R/(f_-),                              (6)

with an empty group omitted. To see this directly, the image of R/(F)
on the normalization branches in either group has kernel the
intersection of their principal prime ideals, equal to their product.
The idempotent makes the two images independent. Each factor in (6) is
a hypersurface, hence Cohen–Macaulay and S2.

Completion descends S2 to A' at p. By §2 the finite birational extension
`A' subset B` differs only at closed points, so A' agrees with the
normalization in codimension one and satisfies R1. Serre's criterion
then makes A' normal at p, forcing equality with B there. This proves
the support assertion in (4).

This proof does **not** assert that A' is etale over A. The raw rank-two
algebra `A[T]/(T^2-g)` is etale off C, but its image A[q] in the common
function field is birational and can behave differently. The branch
factorization in the hypersurface, together with the finite-length
quotient, supplies the needed S2 and R1 assertions.

## 4. General form and geometric limits

The same length argument applies to an integral conductor curve Gamma
of degree D and arithmetic genus g on a degree-a hypersurface, whenever
the exact normalization quotient is
`B/A=omega_Gamma(-(a-4))`. If a non-descending section q of kH has square
descending to the hypersurface, and its image is generically nonzero,
then

    length B/A[q] = 2g-2 + (k-a+4)D.                   (7)

Whenever this is a finite quotient, the branch proof confines its
support to the zero set of q squared. Equation (7) alone is a length
calculation, not a nonexistence theorem. The quintic values
`(a,D,g,k)=(5,5,2,4)` give 17.

In particular, the intermediate ring must not be assumed S2 at its
remaining defect points. The
[local square-descent construction](2026-10-31-square-descent-conductor-contact.md)
gives actual hypersurfaces with a supported local mate and
`length B/A[w^m]=(m-1)k>0`. Adjoining the root agrees with normalization
in codimension one but leaves a punctual non-S2 defect. The missing
global input is a restriction on which local defects the actual
quintic projection can realize, including the point on the A4 source.

## 5. Independent review and adjudication

Reviewer: `/root/nonnormal_quintic_boundary`, October 31, 2026. The
reviewer independently reconstructed (5), the two Hilbert polynomials,
the length 17, and the branch-factor proof of support in §3. The exact
hypotheses identified by review are the integral conductor scheme,
the inherited quotient (2), the actual root and square in (1), the
hypersurface embedding, and the finite quotient proved in §2.
The general expression (7) is the same Riemann–Roch subtraction with
these invariants retained; it does not claim that arbitrary
normalizations have the displayed quotient or root.

An initial objection correctly rejected the shortcut that a unit square
makes A[q] etale or normal. Its proposed counterexample was a
codimension-two complete-intersection surface with nonreduced conductor
scheme and a codimension-one residual normalization defect. It did not
satisfy the present hypotheses. The reviewer withdrew it as a disproof
of (4), then independently checked the branch-factor repair. The
shortcut remains rejected; it has not been reinstated as an explanation
of the result.

No new computation, projection admissibility certificate, actual
quintic–octic presentation, or unrestricted STCI conclusion is supplied.
The geometric gain is a finite defect with controlled support that can
now be compared with actual local conductor gluing.

## 6. Every mate power when the full conductor is smooth

There is an all-degree extension of the defect calculation. Retain the
inherited Gorenstein A4 quintic source, and now assume **Gamma is smooth
and integral**. An arbitrary mate has degree 4N and pulls back to a
scalar multiple of q^N, where `div(q)=5c` and N>=2. This is the inherited
actual-root statement; it is not inferred solely from numerical
equivalence.

Let I be the common conductor ideal and D its scheme upstairs. The exact
conductor sequence is

    0 -> O_Gamma -> O_D -> omega_Gamma(-1) -> 0.

Its outside terms are line bundles on smooth Gamma. It follows locally
that O_D is free of rank two, so `D->Gamma` is finite flat of degree two.
Cayley–Hamilton for multiplication by q on this rank-two algebra shows
that `A+Aq` is closed under multiplication: locally lift its trace and
norm from Gamma to A; the error is in I, and `Iq subset I subset A`.
Consequently A'=A[q] is still precisely the image sheaf (3), even when
q squared itself has not been shown to descend. The same nonzero class
map (5) gives length 17.

Off C, q^N is a unit. In the completed branch proof of §3 choose an
N-th root h of that unit. On each normal branch, q/h is a constant
N-th root of unity. Lagrange interpolation supplies idempotents
separating the groups with the same value. Thus A' is again a product
of hypersurface branch unions after completion; S2 and codimension-one
agreement with B prove normality off C. The conclusion is therefore

    length(B/A[q])=17,   support(B/A[q]) subset C           (8)

for every possible mate degree 4N under the smooth-integral-conductor
hypothesis. This is not an assertion that the image algebra is etale.

Independent reviewer `/root/nonnormal_quintic_boundary` reconstructed
this extension, specifically its rank-two conductor sequence,
Cayley–Hamilton closure and root-of-unity branch decomposition. The
review does not extend the all-N algebra-closure assertion to singular
or nonreduced Gamma. The square case in §§1–3 still permits singular
integral Gamma, because its closure follows directly from q squared
descending.

## 7. The marked A4 point cannot lie over a smooth conductor point

At the unique singular point of the inherited normalization, use the
marked analytic pair

    B=k[[x,y,z]]/(xy-z^5),
    c: x=z^2, y=z^3,
    q=unit*(x-z^2)^5/x^2.                               (9)

The third expression is regular: expanding it gives
`x^3-5x^2z^2+10xz^4-10z^6+5yz^3-y^2`, up to a unit.
This is the interior A4 smooth-curve pair from the inherited marked
normalization classification. Exchanging x and y gives the other
interior convention without changing the argument.

Suppose the conductor passes through this point and Gamma is smooth at
its image. Its local algebra D is finite free of rank two over the
smooth conductor parameter ring R, by the conductor sequence. The
full inverse of the image point is the one marked point. The class of
q in D/R is generically nonzero: globally it is a nonzero section of
a torsion-free rank-one sheaf on integral Gamma. Suppose a positive
power of q descends to R.

Write the Cartier conductor in B as (f). It does not contain c, so all
orders below are finite. There are four possibilities for the linear
part of f.

1. **A nonzero z coefficient.** Eliminating z gives an ordinary nodal
   D, with tangent directions x and y. On the two normalized branches,
   q has orders 3 and 2. For example, on the x-tangent branch x has
   order one and z has order at least one, so `(x-z^2)^5/x^2` has order
   three. On the other branch `ord(x)=5 ord(z)-1` and the order is
   two. The coordinate-line branches at z=0 give the same orders from
   the expanded regular expression. Each branch has degree one over
   R. Any descended power would have equal orders on them, impossible.

2. **No z coefficient and both x,y coefficients nonzero.** Write
   `f=alpha*x+beta*y+delta*z^2+...`. Elimination and Weierstrass
   preparation give a quadratic in x whose constant term has order
   five in z. If delta is nonzero, its linear coefficient has order
   two, and the discriminant has order four. The two smooth branches
   have x-orders two and three. Their q-orders are respectively
   `6+5r` for some r>=0 and 4. The first order increases only when
   its leading x coefficient agrees with that of the marked curve;
   it can never equal four. Thus no positive power descends. This
   retains all higher contact cancellations rather than assuming a
   bound on conductor contact.

   If delta is zero, the discriminant has order five, giving the A4
   cusp. On its normalization `ord(z)=2, ord(x)=5`, so q has order
   ten. A quadratic extension of the fraction field of R has an
   involution tau. If q^N is in R and q is not in its fraction field,
   `tau(q)/q` is a constant root of unity whose square is one, hence
   equals -1. Every such anti-invariant function has odd valuation
   in the ramified quadratic extension. The even order ten is
   impossible. If q were in the base fraction field, integrality
   over the DVR would put it in R, contradicting generic non-descent.

3. **Exactly one x,y coefficient and no z coefficient.** Eliminating
   that variable gives a plane curve of multiplicity at least three.
   This is impossible for a finite flat double cover of a smooth
   curve: its parameter gives a quotient of length two, so its
   Hilbert–Samuel multiplicity is at most two.

4. **No linear term.** D has embedding dimension three, whereas a
   local rank-two finite flat algebra over a complete DVR has a
   quadratic presentation and embedding dimension at most two.

These cases exhaust f. Therefore the marked A4 point cannot be on
the conductor above a point where Gamma is smooth when any power of
q descends. Units in (9) preserve the branch valuations; the quadratic
field argument uses q itself. No bound of one or two on conductor
contact, special projection parameter, or first-symbol reducedness
is required.

Independent reviewer `/root/cyclic_conductor_local_model` reconstructed
this local argument, including the split A3 case, the special increased
contact on its marked branch, the cusp case and the two impossible
embedding/multiplicity cases. The proof uses the full rank-two
conductor algebra, not the reduced support alone.

## 8. Global consequence, including all mate degrees

The preceding components give two conditional exclusions.

**(a) A quintic–octic presentation with Gorenstein normalization and an
integral conductor scheme must have a singular point of that conductor
on C.** Equivalently, it is impossible for Gamma to be smooth at every
point of Gamma intersect C under those hypotheses. Singularities of
Gamma away from C do not discharge this condition.

Indeed, §§1–3 give a root-adjoining defect of length 17 supported on C,
and it is also supported on Gamma. If Gamma were smooth at these
points, §7 would keep the A4 point off the conductor. The normalization
is smooth at every remaining contact point. The
[general local formula](2026-10-31-square-descent-conductor-contact.md#8-a-general-local-formula-when-the-conductor-downstairs-is-smooth)
then gives local length `2b_p`, where b_p is the full Cartier conductor
contact with c. The entire conductor upstairs has class 2H; hence

    sum b_p=(2H).c=8,
    length(B/A[q])=sum 2b_p=16,                          (10)

contrary to 17.

**(b) A quintic carrier with Gorenstein normalization and smooth
integral conductor scheme cannot have a sole-supported mate of any
degree.** Every hypothetical mate has degree 4N with N>=2. Section 6
supplies the same length-17 defect and support statement for that N;
the local formula and §7 also hold for every descended power. The
same contradiction (10) follows.

These statements exclude a geometrically specified class of actual
nonnormal carriers. They do not exclude all integral conductor curves:
singular Gamma can contribute differently. Reducible or nonreduced
conductor schemes and non-Gorenstein normalizations are also outside
these arguments. In particular no nonnormal quintic or unrestricted
STCI theorem is claimed.

The mechanism is the failure to account for one unit of normalization
defect. Smooth conductor gluing at smooth source points contributes
twice its contact with c, while the actual global root requires total
17. The marked non-Cartier A4 point cannot repair that discrepancy
through a smooth conductor, by its unequal branch orders or parity.
This supplies a location requirement on the gluing singularities,
rather than an objection to a large numerical torsion total.

## 9. Comparison and next geometric test

[Hartshorne–Polini, §7](https://arxiv.org/html/1301.3222#S7)
relates smooth supported curves to local almost-Cartier torsion; for
surfaces with ordinary singularities it restricts their intersections
with the singular locus to pinch points and obtains self-linkage.
The present calculation is not an application of that ordinary-surface
classification: it retains the A4 normalization point and arbitrary
conductor contacts under the specified smoothness assumptions. Its
finite defect is computed from the actual root and full conductor.

A separate strategy challenge correctly required the local work to
connect back to actual embeddings. The exclusions in §8 meet that
requirement by imposing a condition on the conductor of any actual
carrier, without first requiring a linear condition on projection
parameters. The proposed requirement that only such a linear condition
could be useful was not adopted. The remaining warning is retained:
do not expand local singularity lists merely to list more survivors.

For the surviving integral-conductor (5,8) source, the next concrete
test is the incidence `Sing(Gamma) intersect C`, together with the
actual octic section image on the inherited A4 projection. Gamma has
the already-reviewed homogeneous ideal of degrees (2,3,3), so this
incidence concerns the singularities of that actual ideal. It cannot
be replaced by a multiple root of the restricted conductor octic:
tangency of a smooth Gamma to C can also give a multiple root. A
successful continuation must produce a new parameter restriction or
an admissible descending section, and must retain all projection
and sole-support hypotheses. The subsequent
[conductor-cone investigation](2026-10-31-quintic-conductor-cone.md)
now proves a uniform quadric-rank identity on the nonendpoint family,
places the unique singularity of an integral conductor at its vertex,
and reduces its required singleton fiber to two projection parameters.
The subsequent
[integral-conductor theorem](2026-10-31-quintic-integral-conductor-exclusion.md)
closes that family in every mate degree by comparing full conductor
contact with the actual normalization differential, including a uniform
vertex-contact calculation. This stronger conclusion uses that separate
argument; it does not extend the square-specific length calculation
here to arbitrary singular or nonreduced conductors.

Final integrated review: `/root/nonnormal_quintic_boundary` independently
reconstructed §§6–8 and their local inputs, then accepted the two exact
scope statements on October 31, 2026. The review checked the
all-mate-degree reduction, generic non-descent, singleton fibers,
rank-two algebra closure, support away from C, the marked A4 cases,
and the comparison of local total 16 with global length 17. No material
issue remained. The separate component reviews in §§5–7 and the linked
local note remain the evidence for their respective arguments.
