# Nonnormal quintics with Gorenstein normalization and integral conductor

Date: 2026-10-31. Status: **independently reviewed provisional all-mate
carrier-class exclusion**. The curve is the fixed
`C0=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of
characteristic zero. No canonical promotion is made.

The later [Gorenstein-normalization exclusion](2026-10-31-quintic-gorenstein-normalization-exclusion.md)
removes the integral-conductor hypothesis. The proof below remains
the integral-conductor input to that stronger, independently reviewed
provisional theorem.

## 1. The precise theorem

An integral nonnormal quintic surface containing C0 has **no
sole-supported mate of any positive degree** if both of the following
hold:

1. Its normalization is Gorenstein.
2. Its full scheme-theoretic conductor curve downstairs is integral.

An integral reduced support with a nonreduced conductor structure does
not satisfy hypothesis 2. The theorem does not cover normal quintics,
non-Gorenstein normalizations, or reducible/nonreduced conductor schemes.
It does not exclude every quintic carrier or settle unrestricted STCI.

The geometric contradiction is

    8 = total full-conductor contact with c
      <= 2 * total normal-differential vanishing on c
      <= 6.                                               (1)

The middle comparison is established locally at the actual gluing
points, including a separate calculation at the singular conductor
vertex. It is not an assumed upper bound obtained from a first-normal
zero or an objection to a large numerical genus or torsion total.

## 2. Inherited source reduction, for any mate degree

Write `nu:X->S` for normalization of a hypothetical carrier and H for
the pulled-back hyperplane class. The
[quintic structural audit, §§4–6](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
applies to any mate under hypothesis 1 and nonnormality. The Cartier
canonical divisor restricts the sectional genus to one or six;
nonnormality excludes six. The resulting X is the degree-five A4
del Pezzo source, with its marked curve c mapping isomorphically to
C0 and with full reduced inverse support exactly c.

There is an actual section q of 4H with divisor 5c. Every possible
mate has degree 4N and pulls back, up to scalar, to q^N. The accepted
[quartic-carrier exclusion](../results/quartic_carrier_exclusion.md)
rules out N=1 and proves that q itself does not descend. No conclusion
here is based solely on numerical equivalence of these divisors.

The full conductor upstairs is a Cartier divisor D in |2H|, so

    D.c=8.                                                (2)

Downstairs its scheme Gamma is Cohen–Macaulay of degree five and
arithmetic genus two, with `nu_*O_X/O_S=omega_Gamma(-1)`.
Under integrality, the nonzero class of q in this torsion-free rank-one
sheaf is generically nonzero. This supplies the precise local
non-descent hypothesis used at the marked A4 point below.

The [intrinsic pair classification, §5](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
exhausts the relative projection centers into endpoint and nonendpoint
lanes. The
[accepted endpoint exclusions](2026-10-11-session-quintic-continuation-results-acceptance.md)
already cover every mate degree. Retain the nonendpoint family with
delta!=0; the argument below closes that remaining lane under
hypothesis 2.

## 3. The actual conductor and normal differential

The reviewed [conductor-cone identity and geometry, §§1–3](2026-10-31-quintic-conductor-cone.md)
show that the actual conductor quadric has rank at most three for
every admissible nonendpoint projection. Integrality of Gamma forces
rank three and makes Gamma rational with a unique singular point,
the cone vertex v. This is a statement about the actual conductor
ideal of degrees (2,3,3), not just a quadric containing its support.

On every smooth source point of c the actual projection normal
differential is represented, up to invertible local changes of frame,
by the two corrected homogeneous cubics P_h,J_h in the
[conormal/conductor audit, §2](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md).
The opposite target chart is included. They are not both zero, and
their homogeneous common-zero divisor has degree at most three.
Thus, for any set of smooth-source contact points,

    sum_p h_p <= 3,                                      (3)

where h_p is the actual differential vanishing order. It is not the
first-symbol order of the quintic carrier equation.

At a smooth normalization point above a smooth point of Gamma, the
[local supported-section comparison, §12](2026-10-31-square-descent-conductor-contact.md#12-smooth-conductor-contact-is-bounded-by-the-actual-normal-differential)
gives `b_p<=2h_p`, where b_p is the full Cartier conductor contact.
It uses the actual pulled-back mate locally, with arbitrary positive
multiplicity. Smooth Gamma and the actual conductor canonical sequence
supply the rank-two conductor algebra required by that lemma.

The marked A4 point cannot meet the conductor over a smooth point of
Gamma for any descended q^N, by the
[all-power A4 calculation](2026-10-31-quintic-root-normalization-defect.md#7-the-marked-a4-point-cannot-lie-over-a-smooth-conductor-point).
Its hypotheses include the actual marked pair, full singleton inverse,
rank-two conductor algebra, and generic non-descent of q, all retained
here.

## 4. The vertex cannot escape the comparison

If v is not on C0, every conductor contact with C0 is a smooth point
of Gamma. The A4 calculation excludes a contact at the only singular
normalization point. Every remaining contact therefore satisfies
`b_p<=2h_p`. Equations (2)–(3) give the contradiction (1).
Consequently any hypothetical mate must put v on C0. This conclusion
holds for every mate degree; it does not use the square-specific
root-adjoining defect of length 17.

The argument in the [cone note, §6](2026-10-31-quintic-conductor-cone.md#6-the-singleton-vertex-fiber-gives-a-two-parameter-necessary-family)
now applies without a restriction on N. The actual normalization
fiber over v has scheme length three, since the minimal local
Hilbert–Burch resolution gives two generators of omega_Gamma and
the unit adds one generator of nu_*O_X. Full inverse support makes
it a singleton fiber. The inherited A4 fiber computations and
accepted all-mate exceptional-lane exclusions put its supporting
point at a smooth point of c. The actual normal differential vanishes
there, so h_v>=1.

The curvilinear fiber and its plane span give the two-parameter
necessary family (18)–(19) of that note, retaining every boundary
case. The new [exact vertex-contact certificate](../computations/quintic_vertex_conductor_contact.py)
computes the order of the **entire conductor** on c there. In the
coordinates rho,L, with

    sigma=1-2rho, pi=1-6rho+6rho^2,
    delta=sigma*pi/[rho(1-rho)],
    kappa=(2-L)/(3delta sigma^3),

clear the nonzero parameter denominator
`6561rho^2(rho-1)^2(2rho-1)^7 pi^3` from the actual universal
conductor quadric and restrict to
`[z^4:z^3(z-1):z(z-1)^3:(z-1)^4]`. At z=rho the constant and
linear terms vanish, while the quadratic coefficient is exactly

    9rho^4(rho-1)^4(2rho-1)pi^5.                         (4)

Every factor in (4) is nonzero in the retained family. There is no
division by L, so the entire J=0 stratum remains covered. Hence

    b_v=2<=2h_v.                                        (5)

All other conductor contacts are smooth points of Gamma; the marked
A4 point is excluded there as before, and the local comparison
applies. Summing (5) and the other local bounds proves (1). This
excludes the nonendpoint lane, completing the theorem with the
accepted endpoint result.

## 5. Evidence and independent review

The local comparison was independently reconstructed by
`/root/square_descent_contact_test`, including its strengthening to
an arbitrary actual supported section, without oddness or a
non-descending root assumption at smooth conductor points.

The vertex-contact certificate received independent static review and
native execution by `/root/conductor_incidence_code_review`. Reviewed
SHA-256: `b111e54da6f19fa01ecd87908ef344b441283aa335356410b36578af4854974e`.
The command

    PYTHONPATH=/private/tmp/stci-symbolic python3 research/computations/quintic_vertex_conductor_contact.py

exited zero using SymPy 1.14.0 and gave the exact Taylor coefficients
in (4). The review checked all family substitutions, local divisor
frames, the recorded denominator and specialization at every retained
parameter value. The imported universal determinant retains its
previous independent review and source identity.

Reviewer `/root/nonnormal_quintic_boundary` independently reconstructed
the global sum, the definitions and frame invariance of h_p, every
A4 boundary, and the extension to all mate degrees. It also checked
the original structural and relative-center sources before accepting
the broader nonnormal-Gorenstein-normalization scope and the combination
with the endpoint exclusions. The new component reviews discharge
the two conditional inputs in that global review. No material issue
remained under the theorem's exact hypotheses.

The earlier symbolic support exploration was diagnostic. No generic
gcd computation or unfinished parameter elimination is used as an
emptiness certificate. The proof instead combines an actual local
contact bound, a uniform nonzero Taylor coefficient, and the global
degree-three differential divisor.

## 6. Effect on the unrestricted problem

Any hypothetical nonnormal quintic carrier for C0 must have a
non-Gorenstein normalization or a nonintegral full conductor scheme.
This is an all-mate-degree restriction on that carrier class. It
does not alter the separate scope of the globally ADE (5,8) exclusion
or eliminate normal quintics with worse singularities.

The local contact comparison applies to actual supported intersections
in other degrees and does not require a globally chosen root. Its
extension to smooth conductor points on reducible conductor schemes
is local, but singular conductor points and nonreduced structures
still require their actual algebra. The positive local singular-A4
construction and the failed hypersurface gluing control remain in
the linked local note; neither is erased by this global exclusion.

## 7. A reduced conductor needs another singular contact on C0

There is a further necessary condition when the full conductor Gamma
is **reduced**, without assuming it is integral. Under the same
nonnormal quintic and Gorenstein-normalization hypotheses, an actual
mate would require

    (Sing(Gamma) minus {v}) intersect C0 != empty,        (6)

where v is the vertex of its actual rank-three conductor quadric.
Thus the cone vertex alone cannot account for the required contact.
This is a necessary incidence condition, not an exclusion of every
reduced conductor. Nonreduced conductors remain outside this assertion.

### 7.1. The actual A4 conductor has a restricted first jet

The [componentwise controls](2026-10-31-componentwise-conductor-root-defect.md#5-the-marked-a4-point-can-meet-a-smooth-conductor-when-q-descends)
show that an abstract A4 normalization can have a smooth conductor
contact if q already descends locally. Consequently the generic
non-descent assumption in §3's inherited local lemma cannot simply
be deleted. The actual quintic embedding supplies a stronger input.

In the source chart Z0=1 put x=Z1, y=Z2, z=Z3. The equations give

    Z4=xy-z^2,  Z5=y^2-xyz+z^3,
    y(z-x^2)+xz^2=0.

The exact coordinate change `u=z-x^2, w=y+xz+x^3` turns this into
`u w+x^5=0`. For J=0, the
[uniform first-jet certificate](../computations/quintic_a4_conductor_first_jet.py)
pulls back the actual conductor quadric and gives constant zero and
linear coefficients

    (alpha,beta,gamma) = L/(81delta^9) *
       (2G(G+3delta^2)^2,
        -G R,
        -(G+3delta^2)[R+6Bdelta(G+3delta^2)]),
    L=2B+G+delta^2,  R=delta(G+3delta^2)^2-2G^2.         (7)

Only powers of delta occur in the denominators. These are coefficients
in the full cotangent space of the source, not in a reduced tangent
direction. A target hyperplane frame changes the local equation by
a unit of value one and leaves this first jet unchanged.

The inherited all-mate exclusions remove J=G=0 and
`J=0,G=-3delta^2`. If J is nonzero, the accepted cotangent/fiber
calculation keeps the A4 point off the conductor of an actual mate.
Retain `J=0,G(G+3delta^2)!=0`. If L is nonzero, alpha is nonzero.
Eliminating x from the conductor equation in the A4 ring gives a
node with tangent directions u,w. The exact marked pair gives q
orders three and two on its two normalized branches. A positive
descended power over a smooth downstairs conductor would have equal
orders there, a contradiction. This argument does not require q
to be generically non-descending.

If L=0, all three first-order coefficients vanish. The upstairs
conductor curve then has embedding dimension three. A smooth
downstairs conductor would make it a finite flat quadratic algebra
over a complete DVR, which has embedding dimension at most two.
This is again impossible. Hence **the actual quintic's A4 point
cannot be a smooth-conductor contact for any mate**, including on
components where q descends generically.

### 7.2. Rechecking the vertex argument for reduced reducible Gamma

The [reduced-conductor degree argument](2026-10-31-componentwise-conductor-root-defect.md#6-one-actual-geometric-restriction-on-the-reduced-case)
forces Q to have rank three: a reduced degree-five singular curve
of an integral quintic cannot lie in at most two planes, each of
which has reduced singular-curve degree at most two. The vertex v
belongs to Gamma and has embedding dimension three by the same
actual Hilbert–Burch equations as in §3. Other singularities of
Gamma are permitted and are not classified.

Suppose (6) fails. Contacts with C0 away from v are smooth points
of Gamma, and §7.1 excludes the A4 point among them. If v is off
C0, every contact therefore satisfies b_p<=2h_p, contradicting (1).

If v is on C0, the vertex argument must be checked at this broader
scope: the cone note's §6 originally assumed integral Gamma. The
minimal Hilbert–Burch resolution at v still gives two generators of
omega_Gamma; the unit and the normalization exact sequence give a
fiber of length three. Full support makes it a singleton. The
accepted A4 fiber calculations exclude that point, so its preimage
is smooth on c and has h_v>=1. The curve maps isomorphically to C0,
so the length-three fiber is curvilinear and transverse to c. Its
span is a plane: a line meeting the quadratic source in this length
three would lie in the source and contradict finiteness of projection.

These are precisely the inputs for the jet equations (16)–(19) in
the cone note. Their derivation does not otherwise use integrality
of Gamma. The resulting necessary family therefore remains valid,
and its reviewed full-conductor certificate gives b_v=2. Together
with every other smooth-contact bound it again gives 8<=6, proving
(6).

### 7.3. Review and geometric consequence

The first-jet certificate received independent static review and one
native execution by `/root/conductor_incidence_code_review`:

    PYTHONPATH=/private/tmp/stci-symbolic python3 research/computations/quintic_a4_conductor_first_jet.py

It exited zero with SymPy 1.14.0. Reviewed SHA-256:
`efc18af739ce98971eef0d5264b38e184753b38c2dda5edba9432bb6346dc7c2`.
The review checked the actual chart, target sections, local frames,
chain rule and parameter denominators. Reviewer
`/root/nonnormal_quintic_boundary` independently checked the node
orders, the embedding-dimension alternative, inherited exceptional
lanes, and the reduced-conductor incidence argument. It explicitly
rechecked the vertex fiber and jet construction after dropping
integrality; no unique-singularity assertion is made in this extension.

Geometrically, any surviving reduced conductor must supply additional
singular gluing along C0, away from the compulsory cone vertex. The
local controls show that such gluing can supply more conductor
contact per unit of transverse differential vanishing. Whether the
actual projection and mate realize it remains open. This is a
new incidence restriction on actual carriers, not a reason to assume
all singular conductor contributions are impossible.
