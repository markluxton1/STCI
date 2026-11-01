# Carrier conductor contact and the actual transverse differential

**Scope and status.** Independently reviewed provisional comparison, with
an application to the fixed characteristic-zero quartic; no canonical
promotion. The theorem concerns actual supported pairs on generically
regular integral carriers. It describes the gluing regimes left available
for realizing such intersections, not a presumption of nonexistence.

The full surface-normalization conductor is the object here. It is not
the conductor of the quadratic separation of a nonreduced intersection.
The actual transverse differential likewise differs from the carrier
hypersurface's first normal symbol. The
[local supported-section theorem](square_descent_and_singular_gluing.md#smooth-conductor-contact-is-bounded-by-the-actual-normal-differential)
supplies the precise comparison; its constructive singular controls explain
why smooth-contact hypotheses cannot be dropped.

## Exact statement

Let S be an integral hypersurface of degree a>=5 containing C0,
generically regular along C0, and let `nu:X->S` be its normalization.
Suppose that S has a proper sole-supported mate of some positive
degree. Then the following two conditions cannot both hold:

1. X is smooth along the reduced inverse curve c over C0.
2. The full scheme-theoretic conductor downstairs is smooth at every
   point where it meets C0.

The mate and generic regularity force the full reduced inverse to be
the single curve c, mapping isomorphically to C0. Thus these are
conditions on the actual normalization and its actual gluing scheme.
There is no global Gorenstein-normalization assumption, no assumption
that the conductor is integral, and no restriction on the mate degree.

Consequently a hypothetical carrier in this generic-regularity regime
must have a normalization singularity on c or a singular conductor
contact on C0. Carriers singular generically along C0 are outside the
statement. Smoothness of the reduced support of a nonreduced conductor
does not satisfy condition 2.

## Divisor and conductor degrees

Write b for the mate degree and H for the pulled-back hyperplane
class. Its actual section has a Cartier zero divisor supported on
the full inverse of C0. This divisor has no isolated components on
the normal surface. Generic regularity of S along C0 gives just one
prime over its generic point, of degree one. Hence the reduced inverse
is c alone. A finite birational map from an integral curve to the
normal curve C0 is an isomorphism, so `c~=C0~=P1`.

Assume condition 1. The curve c is Cartier: this holds along c since
X is smooth there, and away from c its ideal is the unit ideal. For
some positive integer m the actual divisor relation is

    m c ~ b H,   H^2=a,   H.c=4.

Intersecting with H and c gives

    4m=ab,   c^2=16/a.                                   (1)

In particular c^2 is integral, but that divisibility is not needed
for the contradiction below.

Let I be the full conductor ideal on X. Finite duality, together with
the hypersurface identity `omega_S=O_S(a-4)`, gives near c

    I ~= omega_X tensor nu^*(omega_S)^(-1).

Indeed `Hom_A(B,A)` is the conductor for a finite birational
normalization A subset B, and duality identifies
`Hom_A(B,omega_A)` with `omega_B`. The relative-duality identification
is [Stacks, Lemma 49.15.1](https://stacks.math.columbia.edu/tag/0BUL),
with the finite-ring module described in
[§49.2](https://stacks.math.columbia.edu/tag/0BUK).
Smoothness near c makes I invertible there. Write I=O_X(-D) on that
neighborhood. Generic regularity means D does not contain c, so its
restriction is an effective finite contact divisor on c.

Adjunction on the smooth neighborhood of c gives
`K_X.c=-2-c^2`. Thus the total full-conductor contact is

    Btot = D.c = 4(a-4)-K_X.c
         = 4a-14+16/a.                                  (2)

These degrees are degrees of line bundles restricted to c; no globally
Cartier canonical divisor on X is being assumed.

## The actual differential has a smaller zero divisor

The promoted conormal splitting
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md)
gives `N^*_(C0/P3)=O_P1(-7)^2`. The actual normalization morphism,
followed by the inclusion of S in P3, induces

    O_P1(-7)^2 -> N^*_(c/X)=O_P1(-c^2).                  (3)

This map is generically nonzero because normalization is an
isomorphism at the generic point of C0. Its two components are
sections of O_P1(7-c^2). Their common zero divisor therefore has
degree at most `7-c^2`. Let h_p be its local order. Then

    sum_p h_p <= 7-16/a.                                (4)

This is the differential of the actual finite map in the transverse
direction along c. It is not the first-symbol divisor of a chosen
hypersurface equation.

Assume condition 2 as well. At every conductor contact, the actual
conductor sequence for a hypersurface is locally

    0 -> R -> B/I -> omega_R -> 0,

where R is the downstairs conductor ring. Smooth R is a discrete
valuation ring and omega_R is free of rank one. Consequently B/I
is a free quadratic R-algebra. The pulled-back mate is an actual
element of the carrier ring with divisor m c. The
[local supported-section comparison](square_descent_and_singular_gluing.md#smooth-conductor-contact-is-bounded-by-the-actual-normal-differential)
therefore applies and gives

    b_p <= 2 h_p,                                       (5)

where b_p is the full conductor contact at that point. This local
statement permits every positive m and does not require a separate
root, parity assumption, or generic non-descent of a root.

Summing (5) and using (2), (4) gives

    4a-14+16/a <= 14-32/a,
    4a^2-28a+48 <= 0,
    (a-3)(a-4) <= 0.                                    (6)

This is impossible for a>=5. A normal carrier smooth along C0 is
also covered: its conductor contact is zero, already contradicting
the positive value in (2).

## Geometric content and boundaries

The hypersurface dualizing sheaf and adjunction specify how much
conductor gluing the actual supported divisor needs along c. The
balanced ambient conormal bundle limits how much the normalization
map can lose rank there. Smooth conductor gluing converts each unit
of differential vanishing into at most two units of conductor
contact. The required and available totals are incompatible.

This extends the contact mechanism beyond the quintic source and
beyond (5,8), without classifying its singularities. It does not give
an unrestricted nonexistence theorem: singular normalization points,
singular conductor contacts and generic singularity along C0 are
precisely missing local regimes. An actual construction could use one
of those regimes. Numerical compatibility or an abstract gluing model
still does not provide its projective embedding and mate.

The separate
[quintic integral-conductor exclusion](quintic_gorenstein_normalizations.md)
handles one singular-normalization source and its unique singular
conductor vertex by additional actual geometry. Neither theorem
subsumes the other's hypotheses.

### The amount singular conductor contacts must supply

Keep the smooth-normalization hypothesis, but allow the full conductor
to be singular where it meets C0. Let Bad be those singular contacts.
The other contacts contribute `b_p-2h_p<=0`, so the same degree
calculation gives the necessary inequality

    sum_(p in Bad) (b_p-2h_p) >= 4a-28+48/a.             (7)

Since c is Cartier, (1) also gives a|16. For a>=5, the possibilities
are a=8 and a=16, with required excess in (7) at least 10 and 39,
respectively. This quantifies the missing local contribution; it does
not bound it from above or exclude either degree. Singular conductor
gluing can exceed the smooth-contact bound, as the actual local
controls in the [componentwise square control](square_descent_and_singular_gluing.md#an-actual-supported-square-with-componentwise-descent)
demonstrate.

### A criterion for other smooth space curves

Let C be any smooth connected space curve of degree d and genus g,
under the same carrier, mate, generic-regularity, smooth-normalization
and smooth-conductor-contact hypotheses. Define ell(N) to be the
maximum degree of a line subbundle of `N=N_(C/P3)`; this definition
does not use the maximum slope of subbundles of arbitrary rank.
Then a necessary condition is

    d(a-4)+2-2g+3d^2/a <= 2 ell(N).                     (8)

The proof retains the same actual geometric objects. The mate gives
`c^2=d^2/a`; adjunction gives
`D.c=d(a-4)+2-2g+c^2`. Dualizing the actual transverse differential
and saturating its image gives a line subbundle

    N_(c/X)(H_diff) subset N_(C/P3),
    c^2+deg H_diff <= ell(N).

The local comparison bounds D.c by twice deg H_diff, yielding (8).
For a rational curve with normal splitting O(n1) plus O(n2),
ell(N)=max(n1,n2). The fixed quartic has ell(N)=7 and g=0, recovering
(6). This is a reusable necessary criterion, with no claim that its
local hypotheses cover all STCI carriers or that the inequality is
sufficient for constructing one.

Characteristic zero is used in the local supported-section lemma,
including separability of a positive power in the generic quadratic
conductor algebra. The balanced splitting also changes in
characteristic two. This proof makes no assertion about that case
and does not conflict with its known STCI construction.

## Characteristic, applications and review

The proof is characteristic zero: the local section lemma uses
separability of every positive power and absorption of units, not only
invertibility of two. The conormal splitting also has its separate
characteristic-two jump. No unchanged positive-characteristic carrier
exclusion is asserted; the actual
[every-positive-characteristic quartic construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md)
remains available.

The normalization-index mechanism and explicit projective controls are in
[normalization indices and power descent](normalization_indices_and_power_descent.md).
The distinct resolved-fiber-degree comparison has its full application in
[the toric normalization account](quintic_non_gorenstein_toric_sources.md).
The Gorenstein-normalized quintic theorem handles a specified singular
normalization regime by extra actual geometry; neither theorem subsumes
the other's hypotheses. An actual construction can seek singular
normalization along the inverse curve, singular conductor gluing, or a
carrier generically singular along its support. The inequality alone is
not sufficient for realizing any of those alternatives.

Independent frozen-source review reconstructed full inverse support,
Cartier relations, conductor duality near the curve, adjunction, the
actual differential and the local-to-global comparison. It also checked
the singular-contact excess and the general line-subbundle criterion,
including the saturation direction and the a=8 or16 consequence. No
quintic root, global Gorenstein normalization, ADE hypothesis, new
computation or unrestricted STCI conclusion enters this general proof.
