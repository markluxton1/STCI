# Nonnormal quintic carriers with Gorenstein normalization

Over an algebraically closed field of characteristic zero, an integral
nonnormal quintic containing the fixed embedded
C0=[s^4:s^3t:st^3:t^4] has no sole-supported mate of any positive degree
if its normalization is Gorenstein. This is independently reviewed
provisional mathematics, without canonical promotion. Normal quintics
and non-Gorenstein normalizations are outside the theorem.

The proof retains all conductor multiplicities. An integral conductor
is excluded by a full-contact/differential comparison. With several
components, a marked A4 contact makes the quartic root descend. A
conductor supported on one line has two generic canonical types,
with different module and quotient-cover endings. These are three
actual geometric mechanisms, not a reduction to reduced support.

## Source geometry and the actual marked A4 contact

Write nu:X->S for the finite normalization of a hypothetical quintic carrier.

The [structural audit, §§4–6](../supplements/QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit)
and [relative pair classification](../supplements/DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#1-dp5-a4-intrinsic-pair-classification)
give the actual normal degree-five A4 del Pezzo source X, with unique
singular point p0, and a smooth curve c mapping isomorphically to C0.
An actual mate forces its full reduced inverse to be c alone. Write
H for the anticanonical hyperplane bundle. There is an actual section

    q in H0(X,4H),   div(q)=5c,   5c~4H.

Every mate pulls back to a scalar multiple of q^N, N>=2. The
promoted [quartic-carrier exclusion](../results/quartic_carrier_exclusion.md)
prohibits descent of q itself. The full conductor upstairs is a
Cartier divisor D~2H, with D.c=8. Its downstairs scheme Gamma is
CM of degree five and arithmetic genus two, and

    M=nu_*O_X/O_S=omega_Gamma(-1).

The [actual module audit](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#4-conductor-quadric-module-independent-audit)
gives two generators h,z for M and the full conductor ideal of
degrees (2,3,3). The pullback of its actual quadric Q is the entire
Cartier conductor D. The actual projection differential on smooth
points of c is represented by the corrected homogeneous cubics,
whose total common-zero order is at most three.

The [endpoint residual-support proofs](../supplements/QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md) and [power-descent proof](../supplements/QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md) cover every endpoint lane. In the retained nonendpoint
coordinates `(delta,a,B,G,J)`, delta is nonzero. Under full support,
J!=0 makes normalization an isomorphism at p0. The exceptional lanes
J=G=0 and `J=0,G=-3delta^2` already have all-mate exclusions. In the
remaining J=0 lane the local normalization fiber at p0 has length
two; see the [A4 fiber audit](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#7-jbar-zero-conductor-phase-independent-audit).

Suppose p0 lies in D. At its image y0, let R be the completed
downstairs conductor ring and U the upstairs conductor algebra.
The canonical sequence is `0->R->U->omega_R->0`, up to an irrelevant
local line-bundle frame. Its unit survives in the residue fiber,
so that fiber has dimension `1+mu(omega_R)`. The normalization fiber
has length two. Thus R has canonical type one, is Gorenstein, and
U is a free quadratic R-algebra.

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
        -G R_jet,
        -(G+3delta^2)[R_jet+6Bdelta(G+3delta^2)]),
    L=2B+G+delta^2,  R_jet=delta(G+3delta^2)^2-2G^2.         (A4-jet)

Only powers of delta occur in the denominators. These are coefficients
in the full cotangent space of the source, not in a reduced tangent
direction. A target hyperplane frame changes the local equation by
a unit of value one and leaves this first jet unchanged.

The reviewed [first-jet certificate](../computations/quintic_a4_conductor_first_jet.py)
shows that a mate with p0 in D must satisfy

    J=0,   L=2B+G+delta^2=0.                             (A4-locus)

Here is the extra argument needed without assuming R smooth. When
L!=0 the actual upstairs conductor is a node. A free quadratic
algebra over R has a trace involution. If it swaps the two node
branches, the invariant ring R is smooth. If it preserves them,
generic rank two on each base branch requires sign -1 on both
branch parameters, making the anti-invariant module require two
generators. That contradicts its being free of rank one over R.
Thus R is smooth. The marked root has orders three and two on the
two branches, so no positive power descends. This rules out L!=0.

On (A4-locus), set

    K=-G^2+4Ga-2Gdelta^2-2Gdelta-delta^4.

The exact certificate shows that K divides every coefficient of
Q_univ, after the nonzero scalar `648delta^10` is cleared.
Admissibility and the nonzero actual conductor quadric force K!=0.
At p0 the full source first jet vanishes, and the quadratic coefficient
on the marked curve is

    -(G+3delta^2)^2 K/(81delta^8),                        (A4-quadratic)

which is nonzero in the retained lane. Consequently a local generator
f of the full conductor in the marked A4 ring satisfies

    f in m_(X,p0)^2,   ord_c(f)=2.                       (A4-contact)

The certificate uses the exact marked equations
`b_local=-a_local^2/(1-a_local)`,
`c_local=a_local^2/(1-a_local)`. Their difference from the source
tangent line begins in order two, so the vanishing full first jet
justifies using the same coefficient (A4-quadratic). This is full conductor
contact, with every multiplicity, rather than a first-symbol order.

The actual first jet also rules out a smooth downstairs conductor at
p0, including a component on which q descends generically. If L!=0,
the node orders three and two above already contradict descent of
any positive power over a smooth conductor. If L=0, all three
first-order coefficients vanish, so the upstairs conductor has
embedding dimension three. A free quadratic algebra over a complete
DVR has embedding dimension at most two. Thus the actual quintic's
A4 point cannot be a smooth-conductor contact for a mate. This is
stronger than the inherited lemma that assumes generic non-descent.

## A contact-two A4 descent lemma

Let

    Bhat=k[[x,y,z]]/(xy-z^5),  c: x=z^2,y=z^3,
    q=unit*(x-z^2)^5/x^2.

The displayed root is regular. Let the divisor of f not contain c
as a component and let f satisfy (A4-contact). Put
U=Bhat/(f), and suppose the actual conductor algebra is free quadratic
over a Gorenstein R, with its canonical inclusion R subset U. If
q^N belongs to R for any positive N, then **q itself belongs to R**.

The curve U is a one-dimensional complete intersection of embedding
dimension three. Its quadratic initial relations span `xy,f2`.
Since x,y,z have orders 2,3,1 on c, condition (A4-contact) forces a nonzero
z^2 coefficient in f2. Thus those two quadrics are independent and
their common tangent directions avoid the z-axis.

Let tau be the quadratic trace involution. Its anti-invariant module
is free and faithful of rank one over R. Its anti-invariant cotangent
space has dimension at most one and is nonzero: a finite-order
automorphism with trivial tangent action is trivial in characteristic
zero. Choose exact eigenparameters S,T,V in a minimal formal ambient
presentation, with V generating the anti-module. The kernel is
stable under the linear reflection V->-V.

There is no anti-invariant quadratic initial relation. An exact
anti-invariant lift has form `V a(S,T,V^2)`. Its vanishing in U
forces a to vanish by faithfulness of the anti-module. Its nonzero
linear part would then be an ambient linear relation, contradicting
minimality. Hence the trace action fixes the entire quadratic
relation plane, in particular the rank-two form xy.

A reflection preserving xy either fixes the first jets of x,y and
has its anti-axis in the radical direction, or exchanges the two
isotropic tangent planes. On a branch of U_red tangent to the
x-side, q has order 3r, where r is the branch multiplicity: x has
order r, z has order at least r, and y has order at least 4r.
On a branch tangent to the y-side its order is 2r. The root's unit
does not change these statements. Exchanging the tangent planes
preserves r and would change that order, contradicting invariance
of q^N.

In the remaining case the x,y first jets are fixed. On every branch
the ratio tau(q)/q consequently has leading value one. It is an
Nth root of unity in the generic Artin total quotient of U; q is
invertible there because the conductor does not contain c as a
component. Characteristic zero forces
that ratio to be exactly one, including its nilpotent part. Since
the one-dimensional complete intersection U has no finite-length
torsion, tau(q)=q everywhere. Its invariant ring is R, as claimed.

This lemma does not forbid the earlier local positive controls:
one had conductor contact four, and the smooth-conductor control
where q descends had a nonzero conductor linear term. Both fail
one of the specific conditions (A4-contact) imposed by the actual embedding.

## Integral conductor: full contact exceeds the differential degree

Assume the full downstairs conductor Gamma is integral. Then the nonzero
class of q in M(4)=omega_Gamma(3), a torsion-free rank-one sheaf, is
generically nonzero. This is the generic non-descent premise in the inherited marked-A4
smooth-conductor lemma. The separate argument here compares the full
contact D.c=8 with the actual normal-differential divisor of degree at most3.

The reviewed [conductor-cone identity and geometry, §§1–3](quintic_conductor_geometry.md)
show that the actual conductor quadric has rank at most three for
every admissible nonendpoint projection. Integrality of Gamma forces
rank three and makes Gamma rational with a unique singular point,
the cone vertex v. This is a statement about the actual conductor
ideal of degrees (2,3,3), not just a quadric containing its support.

On every smooth source point of c the actual projection normal
differential is represented, up to invertible local changes of frame,
by the two corrected homogeneous cubics P_h,J_h in the
[actual conormal/differential proof](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#5-nonendpoint-all-mate-conormal-conductor-independent-audit).
The opposite target chart is included. They are not both zero, and
their homogeneous common-zero divisor has degree at most three.
Thus, for any set of smooth-source contact points,

    sum_p h_p <= 3,                                      (Differential)

where h_p is the actual differential vanishing order. It is not the
first-symbol order of the quintic carrier equation.

At a smooth normalization point above a smooth point of Gamma, the
[local supported-section comparison](square_descent_and_singular_gluing.md)
gives `b_p<=2h_p`, where b_p is the full Cartier conductor contact.
It uses the actual pulled-back mate locally, with arbitrary positive
multiplicity. Smooth Gamma and the actual conductor canonical sequence
supply the rank-two conductor algebra required by that lemma.

The marked A4 point cannot meet the conductor over a smooth point of
Gamma for any descended q^N, by the
[all-power A4 calculation](root_descent_and_conductor_defects.md).
Its hypotheses include the actual marked pair, full singleton inverse,
rank-two conductor algebra, and generic non-descent of q, all retained
here.

### The vertex cannot escape the comparison

If v is not on C0, every conductor contact with C0 is a smooth point
of Gamma. The A4 calculation excludes a contact at the only singular
normalization point. Every remaining contact therefore satisfies
`b_p<=2h_p`. The total contact D.c=8 and (Differential) give the impossible inequality 8<=6.
Consequently any hypothetical mate must put v on C0. This conclusion
holds for every mate degree; it does not use the square-specific
root-adjoining defect of length 17.

The argument in the [singleton-fiber jet proof](quintic_conductor_geometry.md#6-the-singleton-vertex-fiber-gives-a-two-parameter-necessary-family)
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

    9rho^4(rho-1)^4(2rho-1)pi^5.                         (Vertex-quadratic)

Every factor in (Vertex-quadratic) is nonzero in the retained family. There is no
division by L, so the entire J=0 stratum remains covered. Hence

    b_v=2<=2h_v.                                        (Vertex-contact)

All other conductor contacts are smooth points of Gamma; the marked
A4 point is excluded there as before, and the local comparison
applies. Summing (Vertex-contact) and the other local bounds proves the impossible inequality 8<=6. This
excludes the nonendpoint lane, completing the theorem with the
accepted endpoint result.

## Several conductor components force quartic descent

For an associated curve component E of Gamma let m_E be its generic
scheme multiplicity, and let D_E be the part of the upstairs
conductor-divisor cycle lying over E. The canonical sequence gives
generic length 2m_E upstairs, so

    nu_*D_E=2m_E[E],   H.D_E=2m_E deg(E).

If D_E avoided p0, the divisor c would be Cartier near it. Its
intersection with D_E would be an integer, whereas `5c~4H` gives

    c.D_E=8m_E deg(E)/5.

Thus 5 would divide m_E deg(E). The weighted component degrees
sum to five. When there is more than one component, each weighted
degree is less than five, so every D_E must meet p0 and every E
passes through y0=nu(p0).

The actual marked A4 contact argument above applies and gives (A4-contact) and the free quadratic conductor
algebra. The actual descended mate gives q^N in R, so the contact-two lemma makes q
descend in the completion at y0. Faithful flatness of completion
makes its class zero in the original local ring as well. Its class
in the pure one-dimensional sheaf M(4) therefore vanishes at every generic component, including all
nilpotent layers there. It is zero globally. Thus q descends to S
and lifts to an ambient quartic, contradicting R-0001. This excludes
all conductors with several associated components, without a
reducedness assumption.

## A single conductor line with multiplicity five

If Gamma has one component, its generic multiplicity times its
support degree is five. Multiplicity one makes the CM scheme reduced
and integral, already excluded. The remaining case has a line E
as reduced support and generic multiplicity five. The generic
canonical type is at most two, since M has two generators.

### 5.1. Generic canonical type two

The type is then two at every closed point of E by upper
semicontinuity and the two-generator presentation. The unit and
canonical sequence make every normalization fiber there have length
three. At a contact with C0, full support makes it a singleton;
the accepted A4 fiber lengths and exceptional-lane exclusions place
it at a smooth point of c.

The curvilinear triple-fiber jet construction in the
[cone note, §6](quintic_conductor_geometry.md#6-the-singleton-vertex-fiber-gives-a-two-parameter-necessary-family)
uses only this fiber length, the isomorphism c->C0, the quadratic
source ideal and the fixed relative projection center. A rank-three
conductor quadric is not an additional input once those conditions
are supplied. The same necessary family therefore applies, and its
[full-conductor contact certificate](../computations/quintic_vertex_conductor_contact.py)
gives contact exactly two at every such point. Each has differential
order at least one. Explicitly, its source point is r0=delta*rho
and the code evaluates the target curve at v=rho, whose standard
C0 parameter is `(rho-1)/rho`. Thus the code's historically named
vertex coefficient is the contact at this general triple-fiber
point. No vertex or quadric-rank assumption is used in this application.
Total contact eight would again give
`8<=2 sum h_p<=6`, a contradiction.

### 5.2. Generic canonical type one

At the generic point of E the upstairs conductor algebra is free
of rank two over an Artin Gorenstein ring R_eta of length five.
Its local factors are truncated discrete valuation rings. Each is
a finite projective R_eta-summand, of rank one or two.

A rank-one factor is R_eta itself and has length five. For a
rank-two local factor with residue-field degree r, its fiber over
the maximal ideal has length `e r=2`; its total length is `n r=10`,
where n is the exponent of its uniformizer in the conductor.
Thus r is one or two and n is ten or five. Every upstairs divisor
coefficient is consequently divisible by five:

    D=5D',   H.D'=2.

The divisor D' must meet p0, since otherwise `c.D'=8/5` would be
an integer. The actual marked A4 contact argument again forces (A4-contact). On the A4 uniformizing
cover

    x=u^5, y=v^5, z=uv,

which is unramified in codimension one, the pullback of f has all
divisor multiplicities divisible by five. The complete regular
power-series ring is a UFD and units have fifth roots, so that
pullback equals g^5. The reduced inverse of c has parametrization
`u=t^2,v=t^3`, with z=t^5. Contact two gives

    ord_t g(t^2,t^3)=2.

Hence g has a nonzero linear u term. It is semi-invariant under
the order-five action, since g^5 is invariant, so no linear v term
occurs. The invariant g^5 has a nonzero x term modulo m_Bhat^2.
This contradicts f in m_Bhat^2 in (A4-contact).

Together with the integral-conductor theorem and the several-component argument, these cases
prove the theorem.

## A separate reduced-conductor incidence diagnostic

The following contact argument is useful before the all-component
assembly above. It preserves a distinct necessary incidence test;
it does not leave a reduced Gorenstein-normalization mate case open.

There is a further necessary condition when the full conductor Gamma
is **reduced**, without assuming it is integral. Under the same
nonnormal quintic and Gorenstein-normalization hypotheses, an actual
mate would require

    (Sing(Gamma) minus {v}) intersect C0 != empty,        (Reduced-incidence)

where v is the vertex of its actual rank-three conductor quadric.
Thus the cone vertex alone cannot account for the required contact.
This is a necessary incidence condition, not an exclusion of every
reduced conductor. Nonreduced conductors remain outside this assertion.

The [reduced-conductor degree argument](quintic_conductor_geometry.md#reduced-conductors-force-the-same-cone)
forces Q to have rank three: a reduced degree-five singular curve
of an integral quintic cannot lie in at most two planes, each of
which has reduced singular-curve degree at most two. The vertex v
belongs to Gamma and has embedding dimension three by the same
actual Hilbert–Burch equations in the cone proof. Other singularities of
Gamma are permitted and are not classified.

Suppose (Reduced-incidence) fails. Contacts with C0 away from v are smooth points
of Gamma, and the actual A4 first-jet argument above excludes the A4 point among them. If v is off
C0, every contact therefore satisfies b_p<=2h_p, giving the impossible inequality 8<=6.

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
(Reduced-incidence).

## Proof status, characteristic and remaining geometry

The source's integral-conductor proof and the final all-component
assembly received separate independent mathematical reviews. Those
reviews cover the actual A4 fiber/type argument, the reflection proof
with its nonreduced Artin algebra, all weighted component multiplicities,
the generalized triple-fiber application and the order-five quotient-cover
ending. The first-jet and vertex-contact code had independent
implementation review and successful exact execution in the frozen source.
Their unchanged code is retained; this transfer performs no new execution.
This integration has independent mathematical preservation and scope review; its conclusions remain provisional, without canonical promotion.

This theorem is stated in characteristic zero. The quadratic trace and
reflection arguments require two invertible; the root-rigidity arguments
require the actual power exponent invertible. The A4 uniformizing cover
uses the tame order-five action and the unit-root step. The inherited
surface classification, rationality and source identification keep their
own characteristic-zero hypotheses. Exact polynomial identities may be
reduced only after their denominators and necessary nonzero factors are
checked; the theorem is not asserted in positive characteristic.

Local positive descent models remain in the
[full singular-gluing account](square_descent_and_singular_gluing.md),
including the contact-four model and the smooth-conductor model in which
the root already descends. They do not satisfy the actual first-jet and
contact-two hypotheses used here. The general
[conductor/differential comparison](carrier_conductor_differential_comparison.md)
and [componentwise root-defect formula](root_descent_and_conductor_defects.md)
retain their other-curve and other-degree applications.

Any surviving nonnormal quintic mate must therefore have a non-Gorenstein
normalization. The [toric source](quintic_non_gorenstein_toric_sources.md)
constructs one such marked normalization and an actual quartic root,
and excludes one projection by extra inverse points. Its remaining
relative centers are open. This is separate from the
[globally ADE(5,8) theorem](quintic_octic_surface_constraints.md), which
has its own normality, singularity and degree hypotheses. Neither
result is an unrestricted STCI theorem.
