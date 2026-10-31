# Nonnormal quintic carriers with Gorenstein normalization

Date: 2026-10-31. Status: **independently reviewed provisional
all-mate carrier-class exclusion**. The curve is
`C0=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of
characteristic zero. The component and integrated reviews below do not constitute
canonical promotion.

## 1. Exact theorem and geometric mechanism

An integral nonnormal quintic containing C0, whose normalization is
Gorenstein, has no sole-supported mate of any positive degree.

This removes the integral-conductor hypothesis of the
[preceding exclusion](2026-10-31-quintic-integral-conductor-exclusion.md).
It does not cover normal quintics, non-Gorenstein normalizations, or
arbitrary carrier degrees. In particular it is not an unrestricted
STCI theorem or a complete (5,8) exclusion.

The full conductor has degree five downstairs. An integral conductor
is covered by the preceding theorem. With several components, each
must pass through the marked A4 point, where the actual embedding
forces contact two. The local quadratic conductor algebra then forces
the quartic root itself to descend, contradicting the quartic-carrier
exclusion. The final possible conductor has one line as support and
generic multiplicity five; its two canonical-module types are treated
separately below. All conductor multiplicities are retained.

## 2. Accepted source and the actual A4 contact

The [structural audit, §§4–6](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
and [relative pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
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

The [actual module audit](2026-10-12-session-conductor-quadric-module-independent-audit.md)
gives two generators h,z for M and the full conductor ideal of
degrees (2,3,3). The pullback of its actual quadric Q is the entire
Cartier conductor D. The actual projection differential on smooth
points of c is represented by the corrected homogeneous cubics,
whose total common-zero order is at most three.

The accepted endpoint lanes have no mate. In the retained nonendpoint
coordinates `(delta,a,B,G,J)`, delta is nonzero. Under full support,
J!=0 makes normalization an isomorphism at p0. The exceptional lanes
J=G=0 and `J=0,G=-3delta^2` already have all-mate exclusions. In the
remaining J=0 lane the local normalization fiber at p0 has length
two; see the [A4 fiber audit](2026-10-12-session-jbar-zero-conductor-phase-independent-audit.md).

Suppose p0 lies in D. At its image y0, let R be the completed
downstairs conductor ring and U the upstairs conductor algebra.
The canonical sequence is `0->R->U->omega_R->0`, up to an irrelevant
local line-bundle frame. Its unit survives in the residue fiber,
so that fiber has dimension `1+mu(omega_R)`. The normalization fiber
has length two. Thus R has canonical type one, is Gorenstein, and
U is a free quadratic R-algebra.

The reviewed [first-jet certificate](../computations/quintic_a4_conductor_first_jet.py)
shows that a mate with p0 in D must satisfy

    J=0,   L=2B+G+delta^2=0.                             (1)

Here is the extra argument needed without assuming R smooth. When
L!=0 the actual upstairs conductor is a node. A free quadratic
algebra over R has a trace involution. If it swaps the two node
branches, the invariant ring R is smooth. If it preserves them,
generic rank two on each base branch requires sign -1 on both
branch parameters, making the anti-invariant module require two
generators. That contradicts its being free of rank one over R.
Thus R is smooth. The marked root has orders three and two on the
two branches, so no positive power descends. This rules out L!=0.

On (1), set

    K=-G^2+4Ga-2Gdelta^2-2Gdelta-delta^4.

The exact certificate shows that K divides every coefficient of
Q_univ, after the nonzero scalar `648delta^10` is cleared.
Admissibility and the nonzero actual conductor quadric force K!=0.
At p0 the full source first jet vanishes, and the quadratic coefficient
on the marked curve is

    -(G+3delta^2)^2 K/(81delta^8),                        (2)

which is nonzero in the retained lane. Consequently a local generator
f of the full conductor in the marked A4 ring satisfies

    f in m_(X,p0)^2,   ord_c(f)=2.                       (3)

The certificate uses the exact marked equations
`b_local=-a_local^2/(1-a_local)`,
`c_local=a_local^2/(1-a_local)`. Their difference from the source
tangent line begins in order two, so the vanishing full first jet
justifies using the same coefficient (2). This is full conductor
contact, with every multiplicity, rather than a first-symbol order.

## 3. A local contact-two lemma at A4

Let

    Bhat=k[[x,y,z]]/(xy-z^5),  c: x=z^2,y=z^3,
    q=unit*(x-z^2)^5/x^2.

The displayed root is regular. Let the divisor of f not contain c
as a component and let f satisfy (3). Put
U=Bhat/(f), and suppose the actual conductor algebra is free quadratic
over a Gorenstein R, with its canonical inclusion R subset U. If
q^N belongs to R for any positive N, then **q itself belongs to R**.

The curve U is a one-dimensional complete intersection of embedding
dimension three. Its quadratic initial relations span `xy,f2`.
Since x,y,z have orders 2,3,1 on c, condition (3) forces a nonzero
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
one of the specific conditions (3) imposed by the actual embedding.

## 4. Several conductor components are impossible

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

Section 2 now applies and gives (3) and the free quadratic conductor
algebra. The actual descended mate gives q^N in R, so §3 makes q
descend in the completion at y0. Faithful flatness of completion
makes its class zero in the original local ring as well. Its class
in the pure one-dimensional module
M therefore vanishes at every generic component, including all
nilpotent layers there. It is zero globally. Thus q descends to S
and lifts to an ambient quartic, contradicting R-0001. This excludes
all conductors with several associated components, without a
reducedness assumption.

## 5. A conductor supported on one line

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
[cone note, §6](2026-10-31-quintic-conductor-cone.md#6-the-singleton-vertex-fiber-gives-a-two-parameter-necessary-family)
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
an integer. Section 2 again forces (3). On the A4 uniformizing
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
This contradicts f in m_Bhat^2 in (3).

Together with the integral-conductor theorem and §4, these cases
prove the theorem.

## 6. Independent review and effect on the unrestricted question

The inherited source, endpoint exclusions, divisor and full-conductor
identities retain their cited accepted scopes. The integral-conductor
exclusion has its independent component and global reviews. The
new A4 first-jet and quadratic-coefficient certificate was reviewed
and executed by `/root/conductor_incidence_code_review`; current
SHA-256 is
`efc18af739ce98971eef0d5264b38e184753b38c2dda5edba9432bb6346dc7c2`.
The source code identifies the nonzero parameter factors and checks
identities before any specialization. No generic pivot is discarded.

Reviewer `/root/nonnormal_quintic_boundary` checked the component
degree argument, the Gorenstein conductor conclusion from the A4
fiber, the node involution argument, the necessary parameter locus
and the full-contact interpretation. Reviewer
`/root/square_descent_contact_test` independently reconstructed the
contact-two lemma, including its reflection lift, quadratic initial
relations, unit factors and nonreduced generic algebra.

Reviewer `/root/nonnormal_quintic_boundary` then reconstructed the
single-line type split and independently reviewed this complete
written proof. It accepted the exact theorem scope, the exhaustion
of conductor cases, all weighted multiplicities, the full Artin-module
descents, purity in the multiple-component case, the generalized
triple-fiber use of the certificate, and the A4 quotient-cover
contradiction. Its two exposition recommendations were incorporated:
the general-fiber point is identified with the code parameter above,
and the conductor is stated not to contain c as a component rather
than to be disjoint from it. No material issue remained. Inherited
proofs and certificates were not rerun by that mathematical reviewer;
the separate current-state implementation reviews provide the exact
certificate evidence.

The theorem says that any hypothetical **nonnormal**
quintic carrier must have non-Gorenstein normalization. It does not
eliminate normal quintics with worse singularities, which are outside
the separate globally ADE (5,8) result. The general
[conductor/differential criterion](2026-10-31-carrier-conductor-differential-bound.md)
retains its all-degree and other-curve applications. Local positive
descent controls remain relevant; the obstruction here is their
incompatibility with the actual quintic embedding and divisor classes.
