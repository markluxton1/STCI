# Canonical audited state — 2026-10-07, reconciled through 2026-10-09

This is the continuation entry point for the research session begun on
2026-10-06 and resumed on 2026-10-07 and 2026-10-08. It supersedes conflicting frontier
language in the 2026-10-06 state and older handoffs. Detailed proofs,
independent audits, exact certificates, failed checks and source scopes
remain in the linked notes. No claim of novelty is made for a result
without a separate literature assessment.

**The universal integral projective-curve STCI problem is unresolved by
this repository. The unrestricted characteristic-zero problem for
C0=[s^4:s^3t:st^3:t^4] is also unresolved.** The literature refresh found
no accepted unrestricted resolution; this is a dated search conclusion,
not a proof of absence of unindexed work.

## Evidence labels and inherited base

- **PROVED under stated hypotheses:** a supplied argument has passed a
  separate proof audit. The audit may use an independent representation.
- **EXACT CERTIFICATE / REDUCTION:** exact arithmetic verifies the specified
  identity or exhausted finite system, with its parameter scope explicit.
- **OPEN:** a surviving family, missing hypothesis or proof obligation remains.
- **SUPERSEDED / FALSE:** historical claims that must not be used as premises.

The previous [audited state](AUDITED_STATE_2026-10-06.md) remains the
historical base for unchanged results, including the characteristic-zero
(4,5) exclusion, positive-characteristic smooth-rational-quartic
constructions, finite local-cohomology bound and split-carrier reductions.
The detailed [session uniform audit](notes/2026-10-06-session-uniform-audit.md)
independently verifies the saturated BF duality used in the order-one lane.

## A. Correct scope of the e=2 quartic obstruction

**PROVED:** the e=2 branches of (4,7) and (4,8) are excluded on fixed C0.
The same primitive-fourth argument excludes larger pairs when D2=D3=0.

**OPEN:** larger e=2 pairs with early defects. The old section H phrase
"the quartic e=2 branch excluded" was too broad. Finite-flat planar local
CI models at multiplicities 9 and 12 satisfy the numerical constraints
with nonzero early defects, so those constraints cannot supply the
missing implication.

For e=2 and b=9,10,11, a survivor has D2=0, D3 equal to one point p,
and all defects supported at p. The complete necessary profiles are:

| b | (ord_p D0,...,ord_p D_(b-1)) |
|---:|---|
| 9 | (0,0,0,1,1,1,2,2,2) |
| 10 | (0,0,0,1,1,2,2,3,3,3) |
| 11 | (0,0,0,1,1,2,3,3,4,4,4) or (0,0,0,1,2,2,2,3,4,4,4) |

These are numerical profiles, not an assertion of embedded existence.
The fourth obstruction must have a degree-one annihilator in these
three degrees. Actual ambient quartic contact and this annihilator
condition must be imposed together. See the
[uniform audit](notes/2026-10-06-session-uniform-audit.md).

## B. MF6 type (e,d2,d3)=(0,4,5) — PROVED exclusion

For a hypothetical characteristic-zero (4,6) presentation on C0, the
entire e=0 type (d2,d3)=(4,5) is excluded. This includes all rank drops,
multiple divisor zeros and the infinity chart.

The proof retains the moving support coordinate through cubic order.
The total extra defect at most one supplies a homogeneous linear
annihilator. Its two-chart compatibility forces the complete triple
parameters to (A,B)=(12,4). At that point the **full** quartic space is
a fixed cubic times all ambient linear forms. Every nonzero quartic
there has a plane factor, incompatible with an STCI pair on C0.

This is a full-family proof, not an extrapolation from the generic
kernel or sampled gcds. The certificate now contains direct polynomial
membership witnesses for the boundary-minor ideal and reconstructs the
entire special quartic fiber. See the
[proof](notes/2026-10-06-session-mf6-progress.md) and
[universal verifier](computations/verify_mf6_infinity_universal.py).

**PROVED stronger e=1 result:** no quartic STCI pair on C0 with
L=O(-6) and D2=0 exists in any mate degree. The complete primitive-triple
classification has four actual torus orbits. Its full quartic fibers are
a forbidden quadric-factor space or two-dimensional pencils. The principal
pencil has d3>=6; the two algebraic pencils have d3>=8 when both
coefficients are nonzero. The quartic-specific uniform BF bound d3<=5
leaves only four pure carriers, each with d3=5.

On x3=1, one such carrier has finite birational normalization k[u,v],
with x2=v, x1=u^2((kappa+1)v-u)/kappa and x0=u*x1, where
3*kappa^2-2*kappa+1=0. Its full C0 inverse image is the diagonal u=v.
A mate's polynomial pullback must be c(v-u)^n. The points (0,v) and
((kappa+1)v,v) have the same surface image, forcing (-kappa)^n=1.
The quadratic-field norm of kappa is 1/3, so no positive n is possible
in characteristic zero. Coordinate reversal handles the other members.
The proof uses actual normalization fibers, and applies in every mate
degree. See the [independent full primitive audit](notes/2026-10-07-session-mf6-e1-independent-audit.md),
[separate normalization audit](notes/2026-10-07-session-nonnormal-mf6-independent-audit.md)
and [independent 35-monomial verifier](computations/audit_mf6_e1_primitive_2026_10_07.py).

**Remaining (4,6) scope:** the e=0 (3,6) type has already been reduced
to regular first-normal ratio. The e=1 types (1,3),(2,2) remain open;
the (0,4) type is now excluded by the stronger all-degree theorem.
Positive D2 directions, e=0/e=2 in other degrees and higher carriers
are separate. These theorems do not exclude every (4,6) pair.

**PROVED bounded all-degree extension:** all six e=1,d2=1 endpoint
direction orbits (`a0=0` or `b1=0`) are excluded. Their complete actual
35-column quartic spaces are fixed-cubic-times-linear spaces, or one
unique quartic for each quadratic root. The latter carriers have explicit
dominant birational localized-plane maps. Their units are
`c*(u+kappa)^k`, and equality on two fibers first forces `k=-n`, then
the same impossible `(-kappa)^n=1` condition. Finiteness of this open map
is not assumed. See the [endpoint proof](notes/2026-10-07-session-mf6-e1-d1-endpoints.md).
The principal `a0*b1!=0` carrier part of the d2=1 sextic, and the d2=2 incidence,
remain open. The [intrinsic module reduction](notes/2026-10-07-session-mf6-e1-defective-structural.md)
retains the correct normalized cubic residue `delta^2*f3` and both twists.
The principal defect-one direction curve now has an exact elliptic
compression to `YE^2=XE^3+96XE-448`, with j=2048/3. Its complete
contact map is reduced on a declared open to a six-by-seven matrix and
seven maximal cofactors. The contact rank theorem and exceptional
frames are now exhausted for ancestors. The unique-carrier family has
only finitely many nonnormal parameters; their exact list remains open.
The treated complement carriers are excluded in every mate degree. See the
[October 8 checkpoint](notes/2026-10-08-session-checkpoint.md).

## C. Normal quartic carriers — full fixed-C0 exclusion

**PROVED using the checked Ishii–Nakayama classification,
Jaffe smooth-curve/ADE data, rational-resolution compression and
normal-sheaf defect inputs:** no integral normal quartic surface can be
a carrier in an STCI presentation of fixed C0 in characteristic zero,
whatever the mate degree or common singular points. The source
classification is over the complex numbers; descent to finitely many
coefficients and an embedding into the complex numbers transfer the
nonexistence statement to every algebraically closed characteristic-zero
field. The detailed note records this transfer and the antecedent results.

The smooth-passage lemma forces the strict curve to meet exactly one
exceptional prime transversely at each singular point. If t=c.E,
q=m^T A^(-1)m and d=-E^2, then

    t+q=6,  t^2<=d(6-t).

Denominator compression removes the equality cases. The selected prime
has coefficient one when d=1, and coefficient one or two when d=2,3.
Irreducible reduced E is excluded by the harmonic ADE bound. Reduced
reducible E is a finite cycle family; two independently reconstructed
enumerations leave five numerical rows. Four compress to forbidden
quadric mates. The remaining row has six A1 passages and one A2 passage,
requiring normal-sheaf defect 10/3 while the available defect is three.

See the [proof](notes/2026-10-06-session-normal-carrier-progress.md) and
[independent reduced-cycle audit](notes/2026-10-07-session-normal-carrier-independent-audit.md).

For nonreduced E, rational-surface cohomology proves that every proper
subdivisor has H1=0. Consequently the reduced support is a tree of smooth
rational curves with simple normal crossings. The positive integral
canonical coefficient equations and total diagonal excess at most three
give a finite necessary graph problem on at most twelve vertices. Two
different exact implementations test all 381802 diagonal modifications
and retain 195 canonical cycles. After comparison with all allowed ADE
states and compressed mate exclusions up through degree five, precisely
twelve numerical rows remain, all with d=3 and t=2.

The published Type-D basis of hyperplane sections factors the three
sections through the nonrational point as section(E) times a basepoint-free
plane-coordinate system. Thus the pulled-back maximal ideal is O(-E).
Its restriction to a smooth embedded curve has order one, forcing t=1
and excluding every remaining row. The enumeration is a finite necessary
superset; no realizability assumption is used to eliminate it.

The [independent tree verifier](computations/verify_session_nonreduced_independent_audit.py)
uses rooted-child multisets, centers, integer matching characteristic
polynomials and path-forest cofactors, separately from the first verifier's
leaf growth and rational Schur elimination. Nonnormal quartic carriers,
higher-degree minimum carriers and entirely-thick presentations remain
open. No normality hypothesis is transferred to them. The older compressed
mate bounds are historical reductions now superseded within this normal
quartic lane; they were not themselves exclusions.
The [independent nonreduced proof audit](notes/2026-10-07-session-normal-nonreduced-independent-audit.md)
records the graph reconstruction, numerical-state deduplication and
Type-D maximal-ideal argument.
The additional [global adversarial audit](notes/2026-10-07-session-normal-global-adversarial.md)
checks classification coverage, including the rational Type-C reduction
to Type D, numerical pullback and field transfer. It finds no additional
geometric gap under the recorded antecedents.

## D. Quartic local cohomology — exact corner exclusion and socle reduction

**PROVED / exact certificate:** the full e=2 corner with top coefficient
h=t and r(0)=0 is excluded. The top-image equations give exactly three
primitive torus-normalized directions. For every lower-order lift in
each direction, a polynomial dual of the actual multiplication tensor
annihilates every quartic-multiplier column and takes value one on u.

**PROVED using the finite-bound and generic-length hypotheses:** a
surviving quartic ancestor defines a finite-flat CM quadruple Z and a
faithful map O_Z -> omega_Z(-3). The basepoint-free socle target pencil
forces its top BF piece E3=O_P1(-14). Thus

    deg D3=7-3e.

At e=2 the remaining defect types are exactly (d2,d3)=(0,1),(1,1).
The second is a genuine local Gorenstein CI possibility: its special
fiber can have Hilbert function (1,2,1). It must not be discarded by
assuming a primitive triple or curvilinear special fibers. The faithful
map has cokernel length 2(d3-d2); in type (1,1) it is an isomorphism.

See the [proof and countermodels](notes/2026-10-06-session-localcoh-progress.md)
and [polynomial-dual certificate](computations/session-localcoh-corners.py).
The endpoint direction classification is now complete: in addition to
the excluded corners and reversed parity family, there are four
one-parameter direction families, each retaining one lower lift parameter.
For the first rational family, an exact polynomial dual excludes every
lower lift away from finitely many parameter roots. The exceptional
factors are retained explicitly; they are not existence certificates.
See the [generic polynomial-dual verifier](computations/session-localcoh-origin-generic-dual.py).

**PROVED complete first rational family exclusion:** all four primitive
exception factors Q2,Q1,Q3,Q13 are excluded at every geometric root and
for every lower lift. These account for all 23 admissible exceptional
points of the generic dual. The exact number-field polynomial duals
annihilate all 18 actual tensor columns and have value one on u.
The independent [completeness audit](notes/2026-10-08-session-first-endpoint-completeness-audit.md)
checks the exhaustive denominator partition, rational-source field
coefficients, complete affine lift fibers, irreducibility, primitivity
and the omitted nonprimitive parameter at infinity. Thus no parameter
exception remains in this first family.

**PROVED generic second rational family exclusion:** its complete
polynomial dual excludes every lower lift away from five explicitly
retained factors of degrees 2,2,3,4,15. These are 26 primitive geometric
parameter points in its original denominator partition. Both quadratic
factors are now excluded at all four geometric roots and for every
lower parameter. Their exact polynomial duals annihilate all eighteen
actual columns and evaluate to one on the target. A separate field
implementation, complete affine-fibre check, isolated source replay
and fresh literal reconstruction of all 540 products and both targets
accept these exclusions. The remaining 22 points have factors of
degrees 3,4,15, each with its entire lower lift line OPEN. No retained
point is asserted to support a rank jump or an incidence survivor. See the
[second-family proof and exact exception list](notes/2026-10-08-session-localcoh-family2-generic.md).
The [two-quadratic proof](notes/2026-10-08-session-localcoh-family2-quadratics.md)
and [independent audit](notes/2026-10-08-session-localcoh-family2-quadratic-independent-audit.md)
give the current surviving subset.
The two `p(0)=0` boundary families and nonendpoint top-zero strata remain open.

**PROVED under the socle and complete primitive-triple inputs:** no common
quartic ancestor has `e=1,D2=0`. This is a separate simultaneous-target
argument, not a transfer of the STCI carrier theorem. The correct socle
equations are `f_i=h_i*a-T_i*tau`, where the normalized target pencil
is `span(1,z^2)` and `tau` is a global section of O(4). In the principal
orbit, evaluating the eliminated equation at z=1/2 and -1/2 forces both
targets to vanish there. In the two algebraic orbits, the O(4) degree
bound forces both target images to be zero. The quadric-factor orbit
reduces to the already excluded quadratic-multiplier ancestor problem.
See the [corrected proof](notes/2026-10-07-session-localcoh-e1-simultaneous.md)
and [independent frame audit](notes/2026-10-07-session-socle-bridge-adversarial-audit.md).
The [failed earlier argument](notes/2026-10-07-session-localcoh-mf6-bridge.md)
is prominently retracted: it incorrectly treated a nonzero socle image
as annihilation and must not be used as a premise.

**PROVED additional ancestor boundaries:** the same six e=1,d2=1
endpoint triples admit no common quartic ancestor: a one-dimensional
quartic space cannot produce independent targets, and a common cubic
factor reduces to the forbidden linear-multiplier problem. This uses
the actual quartic spaces, not the carrier mate obstruction. The unique
quadric quotient direction is likewise excluded for every second defect,
including d2=4: restriction of a quartic to the quadric would contain
2C of class (2,6), leaving the ineffective class (2,-2), so both forms
have the quadric factor and reduce to P-037. See the
[endpoint ancestor proof](notes/2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md)
and [all-defect quadric direction proof](notes/2026-10-08-session-localcoh-quadric-direction.md).

**PROVED complete e=1,d2=1 ancestor exclusion:** the principal chart
and every genuine projective boundary are now exhausted. On the declared
open the complete first/contact map has rank 17 in the eighteen actual
quartic ideal forms. Exact frame determinants, all seven cofactors,
resultant gcds and field-fibre calculations retain the nonunit S branch.
All other genuine principal fibres have quartic dimension one, except
the node (p,r)=(2,1/2), whose dimension-four space is a fixed cubic times
every linear form and reduces to P-037. The actual infinity correction
is flat, and all three b0=0 conjugates are checked. Combining this with
the six endpoint exclusions and the primitive-point finite-flat
obstruction closes the whole e=1,d2=1 common-quartic-ancestor lane.
The surviving e=1 ancestor degrees are d2=2,3,4. This does not exclude
a unique quartic carrier's mate of another degree. See the
[independent completeness audit](notes/2026-10-08-session-principal-e1-d1-independent-completeness-audit.md)
and [root reconciliation](notes/2026-10-08-session-late-results-acceptance.md).

**PROVED necessary generator-bundle splitting:** writing
`V=(J/(I_C J))/torsion` for the canonical triple ideal, the two target
sections make `V -> E3` surjective. Its degree and vanishing extension
group force `V(4)=O(2) direct-sum O(2e+2)`. For e=1,d2=1,2,3,4 the
intrinsic Hankel connecting matrices must have exact ranks 3,2,1,0,
respectively. In particular d2=4 requires the zero extension; it remains
a genuine Gorenstein possibility outside the excluded direction. For
e=2 the ranks are 1 at d2=0 and 0 at d2=1. These are necessary conditions;
the actual ambient class and quartic target image must still be imposed.
See the [splitting proof](notes/2026-10-07-session-localcoh-conormal-splitting.md).

The full quartic incidence, surviving e=1 positive-D2 ancestor strata,
second-family exceptions, the two endpoint boundary families and
top-zero points outside the endpoints remain open.

**PROVED further defect-four boundary:** in both algebraic directions
`A=r*z,B=1,12r^2+4r+3=0`, every genuine e=1,d2=4 triple has at most
one independent containing quartic, so cannot produce the two ancestor
targets. The complete 35-column calculation gives a seven-dimensional
double-quartic space. Its containment operator is seven by five. Four
explicit minors cover the opens d0!=0, d4!=0, and the boundary opens
d1!=0, d3!=0; the last boundary has five pairwise distinct diagonal
constants and rank at least four. Repeated and infinity defect roots
are retained. See the [proof](notes/2026-10-08-session-localcoh-e1-d4-algebraic.md)
and [root acceptance audit](notes/2026-10-08-session-new-results-acceptance.md).
The principal obstruction-zero direction and obstruction-nonzero
directions at d2=4 remain open.

## E. The dx=1/P-044 gap — exact closure

The five-coordinate obstruction ideal on the dx=1 resultant-open
chart has reduced locus a=-1/2,b=-2. The exact localized ideal is
nonreduced; ordinary ideal membership must not replace a radical claim.

The formerly suggested three-equation saturation is **not** the unit
ideal. Its subsystem has residual solutions, and an independent rational
interval certificate exhibits one. The full five-coordinate system
does have the required saturation certificate. Its coordinates also
agree exactly with the universal fourth-obstruction implementation.

See the [complete proof and coordinate comparison](notes/2026-10-07-dx1-saturation-audit.md),
[the compact certificate](computations/session_dx1_compact_certificate_2026_10_06.m2)
and [independent expansion](computations/verify_session_dx1_independent_2026_10_06.py).
The original boundary verifier was repaired to state and saturate its
x!=0 chart explicitly. This closes a local classification gap; it does
not add a global arbitrary-degree STCI exclusion.

## F. Uniform entirely-thick and general conductor progress

**PROVED necessary inequality:** for a smooth rational quartic in
characteristic zero, an STCI pair of degrees a,b and exact generic
normal orders p,q has

    a>=3p, b>=3q,
    7ab+28pq>=16(aq+bp).

The proof uses the effective complete intersection of the strict
transforms on the smooth curve blowup. It retains the full curve cycle,
including vertical components and arbitrarily high tangent contact.
In particular a=3p forces b>=4q. At equality, the intersection is
supported on constant normal-direction sections, giving a repeated-root
restriction on the quadric residual. The high-ratio region is open.
See the [independent blowup audit](notes/2026-10-06-session-thick-independent-audit.md).

**PROVED general conditional criterion in every characteristic:** for an
integral carrier X with normalization nu:S->X, a mate requires the
**full** inverse image of C to be pure one-dimensional. Isolated inverse-
image points exclude every mate on that carrier. If all normalization
defect is supported on C, positive Cartier support A with full inverse-
image support and O_S(A)=nu*O_X(b) is sufficient for a mate of some
degree: a high canonical-section power lies in the conductor and descends.
The positive Cartier divisor and linear equivalence remain required.
See the [conductor theorem](notes/2026-10-06-session-conductor-support.md).

**PROVED conditional nonnormal reductions:** if an order-one quartic
carrier's full lifted curve lies in the smooth locus of its normalization,
a mate forces normalization sectional genus zero. For an ADE normalization
the necessary exceptional correction instead satisfies q=2*pi. Ordinary
projected scrolls with smooth elliptic conductor and four ordinary pinches
are excluded in every mate degree. Ordinary projected Veronese surfaces
with reduced height-two differential-minor ramification are likewise
excluded, by a six-point Hilbert--Burch no-conic obstruction. The explicit
standard Roman surface has an independent six-point certificate.
See the [structural proof](notes/2026-10-07-session-nonnormal-structural-progress.md).
These are conditional exclusions. A smooth image with full inverse support
at a degenerate pinch need not contain the ramification scheme; conductor
contact can be arbitrarily large. Degenerate, singular-normalization and
non-slc strata cannot be removed by ordinary pinch counting.

**PROVED stronger Veronese theorem:** every integral quartic whose finite
normalization is `(P2,O(2))` is excluded as a carrier of any smooth
rational degree-four curve in characteristic zero, in every mate degree.
No semi-log-canonical hypothesis is required. A symmetric-matrix center
pencil has no rank-one member. The regular pencils exhaust Roman,
Jordan2 and Jordan3; every-member-singular pencils have degree-two
quadric image and cannot be quartic normalizations. A mate requires one
smooth lifted conic with full inverse support and pullback `constant*f^b`.
Roman requires six points lying on no conic. Jordan2 offers only one
allowed transverse point on a conductor line. Jordan3's actual first
conductor jet fixes the original ring and makes every conic power fail
descent in characteristic zero. See the
[complete classification and proof](notes/2026-10-07-session-veronese-pencil-classification.md)
and [independent all-degree audit](notes/2026-10-08-session-veronese-allmate-independent-audit.md).
Other normalizations are not excluded by this theorem.

**PROVED smooth twisted-cubic class theorem:** every integral quartic
singular along a smooth twisted cubic is excluded as a carrier of fixed
C0 in characteristic zero, in every mate degree. No slc hypothesis is
used. All such quartics are quadratic expressions in the three quadrics
of the twisted cubic; a complete 40-by-35 derivative restriction and
an independently rebuilt minor prove this equation-space statement.
Integrality makes the resulting plane conic smooth. Its inverse image
in the smooth P1-bundle blowup is a smooth rational quartic scroll and
maps finitely to the quartic, giving its normalization.

Finite duality and the depth lemma show that the actual downstairs
conductor is a pure CM curve with polynomial 3m+1. Smooth twisted-cubic
support forces exactly that reduced scheme, and the upstairs conductor
is finite flat of rank two. An integral upstairs conductor compresses
a mate to degree two; a reducible conductor is excluded by contact of
its two branches; a nonreduced conductor forces degree-one descent by
its nilpotent power coefficient. These are entire-scheme descent proofs,
not ordinary-pinch counts. See the [applicability proof](notes/2026-10-08-session-scroll-conductor-applicability.md),
[all-conductor-type criterion](notes/2026-10-08-session-irreducible-conductor-compression.md),
[independent audit](notes/2026-10-08-session-scroll-conductor-adversarial.md)
and [root acceptance](notes/2026-10-08-session-new-results-acceptance.md).
**PROVED complete smooth-scroll theorem:** every integral quartic whose
finite normalization is a smooth rational quartic scroll F0 with
H=C+2f or F2 with H=C+3f is excluded for fixed C0 in every mate degree.
There is no reducedness or Gorenstein assumption on its actual entire
downstairs conductor or upstairs conductor. The actual conductor is an
ACM cubic with polynomial 3m+1. The reduced theorem covers all
twisted-cubic, conic-plus-line and three-line schemes. Hilbert--Burch
rank loci classify the remaining nongorenstein nonreduced cubic ideals.
The exact generic canonical sequence excludes the curvilinear triple
line and forces an even upstairs divisor for the fat triple line.
The differential obstruction uses the entire equation nu*G=lambda f^n
to prohibit generic rank-one conductor primes meeting the smooth lift.
It removes the cuspidal residual cases. Anticanonical divisor classes,
Riemann--Hurwitz and full singleton fibres exclude every remaining
pattern. The nonreduced proof uses actual Artin rings and no global
trace involution over nongorenstein points. See the
[owner proof](notes/2026-10-08-session-scroll-degenerate-conductor.md),
[ACM audit](notes/2026-10-08-session-scroll-acm-independent-audit.md),
[Gorenstein audit](notes/2026-10-08-session-scroll-gorenstein-independent-audit.md)
and the stronger [nongorenstein classification](notes/2026-10-08-session-scroll-nongorenstein-cubic-classification.md),
[exact Artin audit](notes/2026-10-08-session-scroll-artin-independent-audit.md),
[full independent audit](notes/2026-10-08-session-scroll-nongorenstein-independent-audit.md),
[differential audit](notes/2026-10-08-session-normalization-differential-independent-audit.md)
and [root reconciliation](notes/2026-10-08-session-late-results-acceptance.md).

In particular the principal exceptional quartic (p,r)=(8,1/2) is
excluded in every mate degree. Its explicit F0 normalization has entire
conductor (x^2,xy,xL-8yz), a double line plus a line, and upstairs
divisor 2{U=0}+2{b=0}. Its locally Gorenstein structure is proved;
no reduced-conductor theorem is transferred to this scheme. See the
[specific proof](notes/2026-10-08-session-mf6-rhalf-scroll-conductor.md)
and [independent audit](notes/2026-10-08-session-mf6-rhalf-scroll-independent-audit.md).
The remaining principal nonnormal carriers form a finite proper closed
subset of the integral direction curve; its exact list is open.
Singular normalizations, other smooth polarized normalization classes
and other carrier degrees remain separate open lanes. The scroll
theorem does not classify every nonnormal quartic normalization.

## G. Literature corrections and global continuation

The source audit found an unsupported negative-resolution preprint and
an exact proof failure in a broad affine preprint. Neither resolves the
projective problem. The primary Robbiano–Valla theorem checked here is
for **ACM monomial curves**; the broader arbitrary-ACM assertion remains
unverified from the cited original source chain. The arbitrary-degree
cone-carrier exclusion for smooth rational quartics is author-reported
in Jaffe's primary paper, with its original proof not rederived here.
See the [literature audit](notes/2026-10-06-session-literature-refresh.md).

The global decomposition remains order-one versus entirely thick.
There is no upper bound on general defining degrees. Finite degree-pair
exclusions, finite parameter reductions, standalone local CI models and
successful certificate runs do not settle the universal question.

The [October 8 checkpoint](notes/2026-10-08-session-checkpoint.md) records
accepted additions, interrupted structural work and process limitations.
The [reconciled validation index](validation/2026-10-08-continuation-index/index.json)
has 91 distinct top-level sources with latest PASS records and 103
explicitly indexed executions. Its scope is
execution/provenance integrity, not proof of unrecorded hypotheses. It
preserves failed runs and explicitly records the lost source bytes of a
superseded Veronese checker revision; the current stronger revision has
a separate hash-matching snapshot and fresh PASS.
