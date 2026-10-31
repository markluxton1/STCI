# The actual quintic conductor cone and its required vertex incidence

Date: 2026-10-31. Status: **independently reviewed provisional exact
identity, geometric restriction and necessary projection family**. The curve is
`C0=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of
characteristic zero. This note concerns the inherited admissible
nonendpoint A4 del Pezzo projection family, with delta nonzero. It is
not an exhaustive classification of arbitrary nonnormal quintics.

The subsequent [Gorenstein-normalization exclusion](2026-10-31-quintic-gorenstein-normalization-exclusion.md)
closes the carrier class for every conductor scheme and mate degree.
The identities and projection geometry below are retained as its
evidence, with their original hypotheses.

## 1. Exact source and conclusions

Use the accepted degree-five normal anticanonical surface in P5 and
the four projection sections parameterized by `(delta,a,B,G,J)` in
the [restricted-conductor note, §5](2026-10-12-session-nonendpoint-restricted-conductor-determinant.md).
The [independent module audit, §§4–5](2026-10-12-session-conductor-quadric-module-independent-audit.md)
identifies the full downstairs conductor ideal with the three minors
of a matrix whose rows have degrees 2,1,1:

    [ a1  a2 ]
    [ b1  b2 ]
    [ c1  c2 ].

In particular its unique quadratic generator is `Q=b1 c2-b2 c1`;
the other generators are cubic. The conductor Gamma is Cohen–Macaulay,
has degree five and arithmetic genus two. These are properties of the
actual conductor scheme, including any multiplicities, not of a chosen
reduced double curve.

The new conclusions are:

1. For every admissible projection in this family, Q has rank at most
   three, with no generic-parameter exception inside delta!=0.
2. If Gamma is integral as a scheme, Q has rank exactly three. Gamma
   is rational and has a unique singular point, at the vertex v of Q.
   Its local embedding dimension is three and its delta invariant is two.
3. If this integral-conductor carrier occurs in an actual (5,8) STCI
   presentation, then **v belongs to C0**.

The third assertion combines the second with the reviewed
[root-adjoining defect theorem, §8(a)](2026-10-31-quintic-root-normalization-defect.md).
It is a necessary incidence condition, not a sufficient descent test
or an exclusion of every carrier in this family.

## 2. A universal identity rather than a parameter sample

After the accepted inverse coordinate substitution, let M be the 5-by-3
matrix of coefficients of h^2,hz,z^2 in the five source quadrics. Let
L be their 5-by-2 matrix of coefficients of h,z. The latter entries
are linear forms in the target coordinates X0,...,X3. The accepted
audit proves that on every center-rank-three chart

    Q_univ=det[M | L]

is a nonzero scalar multiple of the actual conductor quadric. This
avoids choosing a single minor and discarding the other center charts.

The new [exact certificate](../computations/quintic_conductor_cone_identity.py)
forms this determinant by its ten-term Laplace expansion and computes

    det Hessian_X(Q_univ) = 0

over `QQ(delta,a,B,G,J)`. The expression before evaluation lies in
`QQ[a,B,G,J,delta,delta^-1][X0,X1,X2,X3]`: only powers of delta
have been inverted. The identity therefore specializes at every
delta!=0, including parameter values where an internal symbolic pivot
would vanish. In characteristic zero the Hessian is twice the symmetric
matrix of the quadric. This proves assertion 1.

The argument does not infer a symmetric minimal presentation merely from
abstract self-duality. Such a shortcut would need an additional
chain-level symmetry theorem. The exact identity supplies the needed
rank statement directly for this actual family.

## 3. Why an integral conductor has only the vertex singularity

If Q had rank at most two, it would factor into planes, possibly the
same plane twice. Integrality would force Gamma into one plane. An
integral plane quintic has arithmetic genus six, contradicting genus
two. Thus Q has rank three.

The four linear entries b1,b2,c1,c2 span exactly three independent
linear forms. If they spanned four, their determinant would be the
nondegenerate 2-by-2 determinant quadric; if they spanned at most two,
Q would have rank at most two. Their common zero is consequently the
unique vertex v. All three conductor minors vanish at v, so v lies
on the actual conductor and therefore on the quintic image.

The two quadratic relations on the normalization are

    a1+b1 h+c1 z=0,   a2+b2 h+c2 z=0.

Choose a point over v, which exists by finite surjectivity, and a
nonzero target hyperplane frame there. Evaluating gives a1(v)=a2(v)=0.
All three conductor equations therefore vanish to order at least two
at v. Since they generate the actual ideal, Gamma has embedding
dimension three there.

For completeness, the local delta bound can be seen directly. In a
reduced curve local ring R of embedding dimension e, choose a general
linear parameter l having minimum valuation on every normalized branch.
Then `length R/lR` is its multiplicity m. The Artin quotient R/lR
has embedding dimension at least e-1, so its length is at least
`1+(e-1)=e`. In the normalization Rbar, every element of the maximal ideal of R belongs
to l Rbar. Hence `Rbar/(R+l Rbar)` has length m-1 and is a quotient
of Rbar/R. Thus delta>=m-1>=e-1. Here delta_v>=2.

Finally

    2=p_a(Gamma)=g(Gamma_normalized)+sum_p delta_p.

It follows that delta_v=2, the normalized genus is zero, and no other
point is singular. This proves assertion 2. Assertion 3 now follows
because the root-adjoining theorem requires `Sing(Gamma) intersect C0`
to be nonempty for a (5,8) presentation under the integral-conductor
hypothesis.

## 4. Exact specialized incidence and its limits

The complementary standard-library
[incidence program](../computations/quintic_conductor_singular_incidence.py)
uses exact rational arithmetic and adaptive row reduction on M. For
rank three it computes the actual conductor minors, their 3-by-4
homogeneous Jacobian, and all eighteen 2-by-2 Jacobian minors. It
restricts these equations to C0 and computes the saturated common-zero
divisor on P1, retaining the point s=0. This tests the actual singular
scheme of Gamma, not merely repeated zeros of Q restricted to C0.

Native executions gave the following intersection-scheme lengths. Each
row had center rank three and `length(Gamma intersect C0)=8`.

| delta | a | B | G | J | length(Sing(Gamma) intersect C0) |
|---|---|---|---|---|---|
| 11 | 2 | 3 | 5 | 7 | 0 |
| 1 | 1/8 | 3/8 | -5/4 | -1/8 | 0 |
| 1 | 5/24 | 7/12 | -31/48 | -15/32 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 0 |

In the three nonempty rows the affine gcd is t-1 in the s=1 chart,
with no point at infinity. These are scheme lengths rather than counts
of distinct geometric points. No row certifies conductor integrality
or mate descent. In particular the already-excluded G=J=0 source is
used only as an incidence control; its old exclusion is not reopened.

For these coordinates, center rank three itself ensures finite
birationality. The inverse linear change is invertible for delta!=0,
so the four target sections are independent. The five restricted
quadrics span all binary quadrics, so their center misses the source.
The resulting morphism pulls O(1) back to the ample anticanonical H;
it is therefore finite. Its degree times the image degree is H^2=5,
and independence excludes a plane image. Primality of five forces a
birational quintic image, whose normalization is the accepted normal
source. This does not prove the full singleton inverse condition on C0.

## 5. Review, execution and geometric next question

Independent implementation reviewer `/root/conductor_incidence_code_review`
accepted the incidence program at SHA-256
`6feafccae7de3debe416ae72a2410b9d9a1b6e7e88923333a0e594d5f945624a`.
The review checked the source substitution, all row-reduction charts,
conductor signs and generators, Jacobian criterion, nonrational roots,
and multiplicities at infinity. It also reconstructed the preceding
finite-birationality lemma. That review was static; the native sample
executions in §4 were performed by the lead.

The same independent reviewer reviewed and executed the universal
certificate at SHA-256
`88206c6907bb6c03304c3b71cd710e40c3cb8c490d62cf4811cc542ed17e9cdc`.
The command was

    PYTHONPATH=/private/tmp/stci-symbolic python3 research/computations/quintic_conductor_cone_identity.py

with SymPy 1.14.0 installed only in that temporary dependency directory.
It exited zero and reported ten quadratic monomials and Hessian
determinant exactly zero. The review checked the specialization argument
and the inherited identification on all admissible center charts. No
inherited normality or full-model proof was rerun.

Reviewer `/root/nonnormal_quintic_boundary` independently accepted the
geometric implication in §3 conditional on the rank bound. The exact
certificate supplies that bound on the stated nonendpoint family.
Its final review also checked the displayed local delta proof. An
earlier reviewer argument summing pairwise branch intersections was
withdrawn: that plane-curve formula is not valid for arbitrary space
curves (three coordinate axes have delta two, not three). The
normalization-quotient proof in §3 is the accepted replacement.
No rank-four conductor is excluded merely by the generic (2,3,3)
Hilbert–Burch format: a smooth-quadric curve of type (2,3) has compatible
degree and genus. The new information comes from the actual projection.

The remaining question is whether the cone vertex can lie on C0 with
full inverse support along the whole curve and actual octic descent.
A length-three projection fiber cannot simply be assumed to consist of
three distinct points. Sections 6–7 retain the curvilinear possibility
and test it in an actual projection; the global conditions remain distinct.

## 6. The singleton vertex fiber gives a two-parameter necessary family

Retain the hypothetical (5,8) presentation and integral conductor.
The scheme fiber over the vertex has length three. Indeed all entries
of the conductor Hilbert–Burch matrix vanish at v, so the local
resolution is minimal and the dualizing module of Gamma has two
minimal generators. Tensor the actual sequence

    0 -> A -> B -> omega_Gamma(-1) -> 0

with the residue field at v. The unit 1 survives in B/m_A B, so the
map from the one-dimensional residue field is injective; the resulting
quotient has dimension two. Therefore `dim B/m_A B=3`.

Full inverse support makes this length-three fiber supported at the
single point of c mapping to v. This point cannot be the A4 point.
The inherited [actual cotangent calculation](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md#3-the-actual-a4-cotangent-matrix-including-its-full-embedding-dimension)
gives length one if J!=0. If J=0 and `G(G+3delta^2)!=0`, the
[local fiber and phase audit](2026-10-12-session-jbar-zero-conductor-phase-independent-audit.md)
gives length two. The exceptions are the already excluded G=J=0
family and the already excluded entire-line family G=-3delta^2,J=0;
their exact all-mate exclusions are retained in the
[October 12 acceptance, §§1–2](2026-10-12-session-nonendpoint-results-acceptance.md).
These accepted lanes are reused, not reopened.

At the remaining smooth source point, c maps immersively onto C0.
Consequently the local fiber has embedding dimension at most one, and
its tangent cannot be tangent to c. In the actual chart

    (U0,U1,U2,U3,U4,h)
       =(1,r,r^2,r^3-rT,r^4-(2r^2+r)T+T^2,T),
    c:T=0,

write its length-three jet as

    T=epsilon, r=r0+alpha epsilon+beta epsilon^2,
    epsilon^3=0.                                         (16)

This covers every length-three local fiber at a smooth c-point under
the immersion hypothesis. It is not an assumption that every length-three
scheme in a surface is curvilinear.

The jet spans a plane. Otherwise it would be collinear, and every
source quadric would vanish identically on that line, since a quadratic
on P1 cannot vanish on a length-three subscheme without vanishing
identically. The line would lie in the source. A center avoiding the
source projects that line isomorphically, contradicting its contained
length-three fiber.

The projection center meets the hyperplane h=0 at the fixed point

    P=(2/delta,1,delta/3,0,0,0).

Expand the displayed source coordinates in (16) as
`phi0+epsilon phi1+epsilon^2 phi2`. The intersection of their plane
with h=0 is spanned by phi0,phi2. Thus
`P=(2/delta)phi0+lambda phi2`. Comparing its U1,...,U4 coordinates
gives

    lambda beta=1-2r0/delta,
    lambda alpha^2=delta/3-2r0+2r0^2/delta,
    lambda alpha=r0(delta-r0)(delta-2r0)/delta,
    lambda=r0(delta-r0)[2r0(delta-r0)+delta-2r0]/delta.

The original equations rule out lambda=0 and r0=0,delta. Put
`rho=r0/delta`. Eliminating alpha and lambda yields the necessary
equation

    delta rho(1-rho)=(1-2rho)(1-6rho+6rho^2).             (17)

Conversely its solutions with delta!=0 and rho!=0,1 retain all the
nonzero factors used above. They determine

    delta=(1-2rho)(1-6rho+6rho^2)/(rho(1-rho)),
    r0=delta rho,
    alpha=1/[3(1-2rho)^2],
    lambda=3delta^2 rho(1-rho)(1-2rho)^3,
    beta=(1-2rho)/lambda.                               (18)

In particular rho=1/2 and the roots of 1-6rho+6rho^2 are excluded by
delta!=0, rather than silently divided out.

Every possible center line in this jet plane has form
`span(P,phi1+kappa phi0)`, modulo adding a multiple of P. The one
line lying entirely in h=0 contains the source point and is inadmissible.
Matching the U1=0 representative of the other center generator to
the actual projection coordinates gives

    a=-4r0^3 alpha+2r0^2+r0-kappa r0^4,
    B=delta(3r0^2 alpha-r0+kappa r0^3),
    G=-3delta^2[alpha(2r0-delta/3)
               +kappa(r0^2-r0 delta/3)],
    J=delta^4[2alpha/delta+kappa(2r0/delta-1)].            (19)

Thus the five-parameter nonendpoint source has been reduced, under the
stated STCI and integral-conductor hypotheses, to the two parameters
rho,kappa. Center avoidance, integral conductor, full inverse support
away from the vertex, and actual octic descent still have to be imposed.
Equations (18)–(19) do not assert that all these candidates satisfy
those conditions.

Independent reviewer `/root/nonnormal_quintic_boundary` reconstructed
the fiber length via the dualizing module, the A4 boundary using the
accepted exclusions, the curvilinear/plane argument, every jet equation,
the retained zero-denominator boundaries, and the center-line
parameterization. No material issue remained at this necessary-family
scope. This is a reduction to an actual geometric family, not a
completed emptiness or section-image computation.

## 7. A genuine singleton vertex fiber and a global support failure

Take rho=2/3 and kappa=0 in §6. The resulting parameters are

    (delta,a,B,G,J)=(1/2,1/9,1/3,-9/8,3/4).

The [exact example certificate](../computations/quintic_conductor_vertex_example.py)
uses the accepted source sections and reviewed rational conductor
builder. It finds center rank three, so §4 gives an actual finite
birational normalization of an integral quintic. The conductor quadric
has rank three and its gradient vanishes at

    v=[1:-1/2:-1/8:1/16] in C0.

The scheme fiber over v in the smooth source chart is exactly

    (r-1/3-3T-54T^2, T^3).                             (20)

This is the entire projective fiber. The source boundary U0=0 has
underlying support the line Z2=Z3=Z4=Z5=0, as follows directly from
the five quadrics. Its image satisfies X2-3X1+2X0=0, while this
linear form has value 27/8 at v. There is therefore no omitted
boundary point. Equation (20) is a curvilinear triple fiber supported
at the one smooth c-point r=1/3,T=0. It shows concretely why a
length-three fiber is not itself a contradiction to singleton support.

The rest of the curve does fail the full inverse condition. The
corrected conormal cubics have homogeneous gcd r-1/3 and no common
root at infinity; J=3/4 also makes the A4 cotangent map surjective.
Meanwhile the actual conductor quadric restricts to C0, in u=t/s,
as a nonzero scalar multiple of

    (2u+1)^2(32u^6-8u^5+22u^3-u^2+9).                 (21)

The sextic is nonzero at -1/2 and the full contact form has degree
eight, so it gives a residual contact divisor of degree six away
from the sole smooth-source rank-drop point. Multiplicities are
retained; six distinct points are not asserted.

At each residual contact the marked point has a surjective target
cotangent map. If it were the only inverse point, the accepted finite
local cotangent lemma would identify the normalization and carrier
local rings, contradicting conductor contact there. Thus there are
actual additional inverse points outside c over C0. The necessary
full reduced inverse support condition fails. **This particular
quintic has no mate of any positive degree.** No inference from a
vertical exceptional cycle or just a numerical deficit is involved.

The example does not test conductor integrality, and is not a
realization of all hypotheses in the conditional family. It constructs
the desired local vertex behavior in an actual finite projection and
then locates the separate global failure. No uniform failure of
(18)–(19), or new STCI construction, follows from this one example.

Independent reviewer `/root/conductor_incidence_code_review` checked
the actual sections, corrected conormal conversion, boundary support,
full fiber ideal, rank and gradient of the actual quadric, contact
polynomial, and the finite-local-algebra interpretation. It executed
the final certificate with

    PYTHONPATH=/private/tmp/stci-symbolic python3 research/computations/quintic_conductor_vertex_example.py

using SymPy 1.14.0. Exit status was zero. Final reviewed SHA-256:
`a033bef67f6a5affae088a6b687c87557ea7325e1643b96263e0f7c56fcf284e`.
The earlier version's lack of an explicit vertex test was corrected
by adding the actual gradient/rank calculation; the changed code
was independently reviewed and executed. No material issue remained.

## 8. Direction challenge, bounded test and its resolution

An independent strategy challenge by `/root/nonnormal_strategy_challenge`
accepted a uniform actual-conductor-support test on (18)–(19) as the
next step. This was an incidence on a necessary embedded family,
not an expansion of local singularity lists. The existing full-support
condition requires the entire conductor octic to be supported on the
corrected homogeneous conormal common-zero divisor, with the A4 point
retained when J=0; the
[accepted determinant incidence](2026-10-12-session-nonendpoint-results-acceptance.md#4-actual-conductor-quadric-octic-and-finite-necessary-incidence)
keeps every contact multiplicity and projective boundary.

The bounded outcomes considered were: a complete empty admissible locus, which
would exclude only this integral-conductor (5,8) source; an exact
residual locus on which to test the actual T^10 section image; or a
proof that this support condition adds nothing, in which case proceed
directly to that section-image question. More parameter samples do
not establish any of these outcomes. Broader local phase classification
was deferred unless a surviving actual contact stratum required it.

The reusable mechanism is the passage from an actual root-adjoining
defect with controlled support to conductor incidence and then to an
embedded normalization family. The rank identity and the explicit
two-parameter formulas are specific to this quintic source. The local
singular-conductor construction in the
[control note, §10](2026-10-31-square-descent-conductor-contact.md#10-an-actual-singular-conductor-model-at-the-marked-a4-point)
shows that singular gluing can support actual square descent; its
different defect and embedding explain why it is not a construction
of this projective carrier.

The subsequent
[integral-conductor exclusion](2026-10-31-quintic-integral-conductor-exclusion.md)
resolves the required test without a parameter-ideal elimination.
The full conductor has contact exactly two at the vertex for every
retained member of (18)–(19). At every smooth conductor contact the
actual supported-section lemma gives contact at most twice the
normal-differential order. The global total would therefore satisfy
8<=6. Its argument also forces vertex incidence in every mate degree,
so the completed result excludes all mates under Gorenstein
normalization and integral full conductor, including the accepted
endpoint lanes. The necessary family and the local triple-fiber
example above remain useful geometry; their compatibility does not
supply global support. No canonical promotion or unrestricted
conclusion follows.
