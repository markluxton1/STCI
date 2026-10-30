# October 9 historical mathematics

Full original source text preserved. Hypotheses, counterexamples, unsuccessful arguments, and open questions retain their source status; no new independent audit or theorem promotion.

---

## Source: 2026-10-09-session-results-acceptance.md

# October 9 root acceptance and continuation frontier

Date: 2026-10-09. This record supersedes the open-normalization
language in the October 8 acceptance/checkpoint where stated below.
The universal integral-curve STCI problem and the unrestricted
characteristic-zero problem for fixed C0 remain **OPEN**. No novelty
claim is made without a separate literature assessment.

All mathematical statements in sections 1--5 are over an algebraically
closed field of characteristic zero and concern the fixed smooth
rational quartic C0=[s^4:s^3t:st^3:t^4], unless explicitly broadened.
The new results concern integral quartic carriers. They do not impose
an upper bound on the carrier degrees of an unrestricted presentation.

## 1. The entire sectional-genus-zero and smooth-normalization lanes close

**PROVED HERE / independently accepted.** Every integral quartic
whose normalization has sectional genus zero is excluded as a mate
carrier for C0 in every mate degree. Consequently every integral
quartic with smooth normalization is excluded in every mate degree.

The [owner proof](2026-10-09-session-normalization-sectional-genus-zero.md)
and [independent audit](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-normalization-genus-zero-independent-auditmd)
give an exhaustive classification from nef-big vanishing and
Riemann--Roch: h0(H)=6, so the complete polarized normalization is a
degree-four minimal-degree surface in P5. The possibilities are
F0, F2, the Veronese surface, and the rational-normal-quartic cone.
The earlier entire-scroll and Veronese proofs exclude the first
three; the newly proved cone argument excludes the fourth using
torsion-free class group, full normalization fibers, and the
unit-factor differential lemma.

There is no remaining "other smooth polarization" quartic lane
under a mate: a lift avoiding the singular locus forces sectional
genus zero, and this classification is exhaustive. The cone argument
uses no reducedness hypothesis on a conductor.

Root also proved, and the independent audit accepted, that an
integral quartic containing this smooth degree-four curve is
automatically regular at its generic point. Otherwise a general
integral plane quartic would have four distinct singular points,
contrary to arithmetic genus three. Thus no order-one qualifier
remains in the new integral-quartic conclusions.

## 2. All nonnormal quartics containing C0 have rational normalization

**PROVED HERE / independently accepted, without a mate hypothesis.**
Every integral nonnormal quartic containing C0 has a rational
normalization. Extra isolated points over C0 need not be excluded
for this theorem. The same argument applies to any smooth rational
degree-four curve in a nonnormal integral quartic.

See the [owner proof](2026-10-09-session-nonrational-quartic-normalizations.md)
and [independent audit](2026-10-09-session-nonrational-normalization-independent-audit.md).
For a smooth resolution M and L the pulled-back hyperplane,
L^2=4, K_M.L=2pi-6<0, and 0<=pi<=2. A nonrational resolution is
ruled over a curve of positive genus. Pushing the nef L through
point blowdowns gives actual multiplicities 0<=m_i<=a, including
infinitely near centers, where a is its ruling-fiber degree. The
exact total-transform intersection identity is

    4=(2g-2)a^2+(6-2pi)a+sum m_i(a-m_i).

It forces a<=2. The strict lifted P1 of C0 must be a fiber
component and has degree four, giving 4<=a<=2. This contradiction
uses only the existence of C0, not a mate or full inverse support.
The nonnormal hypothesis is material: normal quartics have pi=3
and are covered by the earlier separate normal-carrier exclusion.

## 3. The genus-one lane reduces to two singularity patterns

**PROVED HERE / independently accepted.** Every genus-one
normalization of an integral nonnormal quartic containing C0 is a
normal Gorenstein del Pezzo surface of degree four with only ADE
singularities. Its minimal resolution is a weak del Pezzo surface
with L=-K_M. No mate hypothesis is needed for this classification
reduction.

The [root proof](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
and [independent audit](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-rational-genus-one-ade-independent-auditmd)
derive h0(K_M+L)=1. Its unique effective divisor is exceptional;
minimality gives nonnegative canonical intersection with every
exceptional prime. Negative definiteness then forces that divisor
to be zero. Compatible canonical differentials give an actual
crepant equality and K_S=-H. The primary crepant/Du Val and weak
del Pezzo marking inputs are explicitly checked in the notes.

**PROVED necessary filter, with root's separate proof reconstruction.**
If such a genus-one carrier has a mate, its complete exceptional
type is exactly one of 4A1 or A3+2A1, and its mate degree is even.
All other ADE types in this lane are excluded. See the
[owner D5 proof](OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd)
and [root independent audit](OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-root-independent-auditmd).

The missing integral root Z=L-c# has square -2 and belongs to
sat(R) minus R. Downstairs smoothness is needed to exclude Z in R.
In the signed-coordinate D5 model, a missing root can join only
two full D blocks. Five coordinates allow only block sizes (2,2)
or (2,3), giving the two types above and index two. The effective
corrections are

| Type | Effective exceptional correction Z | Strict curve intersections |
|---|---|---|
| 4A1 | Half the sum of the four exceptional curves | One with each |
| A3+2A1 | Middle A3 curve plus half its ends and the two A1 curves | One with the middle and each A1; zero with the ends |

The owner reflection/HNF checker and root's different signed-partition
checker both completed isolated terminal PASS. They check all 428
embedded root subsystems; precisely fifteen 4A1 embeddings and ten
A3+2A1 embeddings are nonprimitive. The written signed-component
argument proves completeness; program agreement alone is not the
proof. A further worker audit was interrupted at the weekly quota
before a final written record and is not counted as completed.

## 4. A uniform four-A1 family is excluded in every mate degree

**PROVED HERE / independently accepted.** On the parameter open

    alpha beta gamma delta (alpha delta-beta gamma) != 0,

the [displayed family](#source-2026-10-09-session-singular-delpezzo-four-a1-familymd)
has normalization S=V(ae-c^2,bd-c^2) in P4, a smooth lifted rational
normal quartic with 2c~2H, and projection to the exact fixed C0.
Nevertheless every carrier in that family is excluded in every
mate degree. The [independent audit](#source-2026-10-09-session-singular-delpezzo-four-a1-family-independent-auditmd)
proves the actual finite birational normalization and entire parameter
coverage, including repeated roots and the special cancellation loci.

Every zero of the nonzero binary quartic L_C lies away from the
two endpoints. It gives both z=+U^2V^2 and z=-U^2V^2 above the
same C0 point; the negative lift is not on the rational normal
quartic. A pulled-back mate cannot vanish at an isolated extra
point without a height-one zero component through it. Full inverse
support therefore fails. The root's fresh isolated owner replay
passed in 0.603 seconds, in addition to the independent auditor's
owner and countercheck replays. The final
[audit manifest](../validation/2026-10-09-four-A1-family-audit/audit-manifest.json)
preserves the actual source and proof hashes.

This is not the entire four-A1 projection class. In particular this
construction places two of its singularity passages at the fixed
C0 parameter endpoints. Other positions and the singular coordinate
transformation boundary are not silently included.

## 5. Principal MF6 carriers have an explicit finite necessary locus

**PROVED necessary finite reduction / separately accepted algebra
and geometry.** On the declared principal contact open, every
nonnormal carrier having a mate lies in a fixed binary-gradient
Sylvester determinant's zero locus. It contains at most **630 distinct
principal weighted parameter points**. The exact zero list remains
uncomputed, and this locus is not asserted to equal the nonnormal
parameter locus or the locus of actual mates.

The [owner proof](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-mf6-principal-weighted-candidatemd),
[independent geometry audit](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-mf6-weighted-candidate-geometric-auditmd)
and [independent algebra audit](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-mf6-weighted-candidate-algebra-independent-auditmd)
bind eighteen actual quartic forms, three polynomial syzygies of
weighted degrees 9,9,10, and the actual first-normal binary octic.
The fixed 14-by-14 determinant has weighted degree 210 and retains
zero-generator fibers and infinity multiple roots. At a good point
modulo 101 its determinant is 22, proving characteristic-zero
nonvanishing by the primitive integer sextic and powers-of-two
denominator/Gauss argument. The finite ordinary-plane cover gives
Bezout bound 1260, with two distinct lifts per principal point,
and hence 630.

Root's full isolated source replay passed in 25.463 seconds; a
new bounded independent coefficient/matrix/infinity countercheck
passed in 7.909 seconds. The input closure and final
[audit manifest](../validation/2026-10-09-mf6-weighted-candidate-audit/audit-manifest.json)
are retained. Completeness of the whole kernel module at every
exceptional fiber is not needed: one checked syzygy and the accepted
pointwise rank-one theorem suffice, while zero syzygy fibers remain
in the determinant's zero locus.

The r=0 lead from modulo-13/23 multiple-root samples was false in
characteristic zero. Exact cubic-field computation gives squarefree
normal coefficients and a zero-dimensional projective Jacobian
locus, so all three r=0 conjugates are normal and excluded by the
normal theorem. The owner note retains those bad-reduction leads;
they must not be promoted as nonnormal examples.

## 6. Current surviving frontier and evidence record

For an integral quartic mate carrier for fixed C0, the normal lane,
sectional-genus-zero lane, every smooth normalization and every
nonrational normalization are now excluded. A survivor requires a
rational singular normalization and a smooth non-Cartier lift through
its singular locus. In genus one, only 4A1 and A3+2A1 remain and the
mate degree is even. Genus-two rational normalizations remain OPEN.

Other four-A1 projections, A3+2A1 conductor descent, and genus-two
geometry are the next structural targets. The finite principal MF6
candidate list still needs its actual carriers and conductor jets
classified. The remaining 22 second endpoint-family points of
degrees 3,4,15, their full lower lift lines, e=1 ancestor degrees
2,3,4, early e=2 defects, higher minimum carrier degrees, entirely
thick presentations and the split-sextic totally ramified boundary
also remain OPEN.

The reconciled [execution index](../validation/2026-10-08-continuation-index/index.json)
now contains **97 distinct top-level sources with latest PASS records
and 110 explicitly indexed executions**. The original 55-source/61-run
baseline was retained. The earlier 91/103 and 95/108 index bytes are
preserved separately. Imported helpers and unindexed discovery runs
are not inflated into independent checks. Old failure logs and the
disclosed lost bytes of one superseded Veronese revision remain.

Live Git inspection found branch research/ultra-resume-2026-10-06
at HEAD e7c9c9594795271ff2c1b0a9026955523975e7d7, with commit title
"2026-10-09 morning limit reached". The inherited October 6 snapshot
3ffda7548a863387429adab61eefe02575e86297 is historical. Root did not
perform this Git mutation; the newly observed checkout is authoritative.

Several workers subsequently terminated at the weekly account limit
with reset message October 14, 8:24 AM local. Their saved completed
proofs and exact runs remain evidence; unfinished assignments, the
conditional smooth-conic conductor proposal, and absent final worker
audits remain leads. Root completed the separate D5 audit and
record reconciliation. No account reset credit was used. No process
is claimed live from a saved input alone, and the global goal is
not marked complete or narrowed to this batch.


---

## Source: 2026-10-09-session-singular-delpezzo-four-A1-family-independent-audit.md

# Independent audit of the projected four-A1 family

Date: 2026-10-09. Auditor: `family2_quadratic_independent_audit`, independent of the construction owner. This bounded audit used no child agents and edited no original source or canonical frontier document.

## Verdict and exact scope

**PROVED HERE:** over an algebraically closed field of characteristic zero, every quartic in the displayed family with

```text
alpha*beta*gamma*delta*(alpha*delta-beta*gamma) != 0
```

fails to admit a mate of any degree whose set-theoretic intersection is the exact fixed curve `C0=[U^4:U^3V:UV^3:V^4]`.

The [owner proof](#source-2026-10-09-session-singular-delpezzo-four-a1-familymd) is accepted at this scope. The universal coordinate identities are checked by a separate implementation and isolated replays. The mathematical proof is the algebra and geometry below, not agreement between agents or a numerical parameter sample. The singular surface, smooth lifted curve, finite birational quartic image, and extra normalization point are bound to the actual fixed coordinates.

This family is not asserted to exhaust all four-A1 embeddings or projections, all genus-one singular normalizations, genus-two normalizations, or the unrestricted STCI problem. The parameter boundary where the displayed transformation becomes singular is outside this construction and outside this theorem.

## 1. The standard surface is integral and normal

Put `S=V(ae-c^2,bd-c^2)` in `P4[a:b:c:d:e]`. Here is a direct domain proof supplementing the owner's quotient-cover argument. In lexicographic order `a>b>c>d>e`, the leading monomials are `ae` and `bd`, which are relatively prime. The two equations therefore form a Groebner basis. Map their quotient ring to a Laurent polynomial ring in independent `r,s,t` by

```text
a -> r, b -> s, c -> t, d -> t^2/s, e -> t^2/r.
```

A standard monomial `a^i b^j c^k d^l e^h` has `i*h=j*l=0`, and maps to `r^(i-h)s^(j-l)t^(k+2l+2h)`. Its Laurent exponents recover `i,h` and `j,l` uniquely, and then recover `k`. Distinct standard monomials have distinct images. The homomorphism is consequently injective, so the quotient is a domain. It has dimension three: it contains algebraically independent `a,b,c` and embeds in their fraction field. The two equations form a height-two complete intersection, and the projective surface is integral of degree four.

The two gradient rows are

```text
(e,0,-2c,0,a),   (0,d,-2c,b,0).
```

Their rank drops exactly at the four projective coordinate vertices with nonzero `a,b,d,e`. The independent source forms all ten minors and verifies that their ideal with the two quadrics contains `c^3`, `(ae)^2`, `(bd)^2`, and the other four cross products in `a,b,d,e`. Conversely every generator vanishes at all four vertices. Its radical is therefore the four-axis ideal. Equivalently, if `c!=0` the minors force all other coordinates to vanish, contradicting a surface equation; with `c=0`, all six cross products vanish and only the four vertices remain.

In the `a=1` chart, eliminate `e=c^2`; the remaining local equation is `bd-c^2=0`. The other three vertices have the same A1 model. The complete intersection is Cohen-Macaulay, hence S2, and its singularities are isolated, hence it is R1. Serre's criterion gives normality. For `H=O_S(1)`, complete-intersection adjunction gives `K_S=-H`, `H^2=4`, and sectional genus one.

## 2. The curve and the coordinate transformation are correctly bound

Write `Delta=alpha*delta-beta*gamma`, `m=alpha*delta+beta*gamma`, and `n=alpha*beta*gamma*delta`. The owner's five-by-five transformation from `Y0,...,Y4` to `a,b,c,d,e` has determinant `n*Delta^3`. It is invertible on the entire specified parameter open. Thus the image of `Y_i=U^(4-i)*V^i`, `i=0,...,4`, is a smooth embedded rational normal quartic, denoted `c_S`. It is a projective change of coordinates of the standard RNC, not a merely generic parametrization. Its actual formulas are

```text
a=UV*(gamma U+delta V)^2,
b=-U^2*(alpha U+beta V)*(gamma U+delta V),
c=-UV*(alpha U+beta V)*(gamma U+delta V),
d=-V^2*(alpha U+beta V)*(gamma U+delta V),
e=UV*(alpha U+beta V)^2.
```

Both surface quadrics vanish identically. The curve passes through all four A1 vertices at four distinct parameters:

| Vertex | Parameter `[U:V]` | Nonzero coordinate value |
|---|---|---|
| `b` | `[1:0]` | `-alpha*gamma` |
| `d` | `[0:1]` | `-beta*delta` |
| `a` | `[beta:-alpha]` | `-alpha*beta*Delta^2` |
| `e` | `[delta:-gamma]` | `-gamma*delta*Delta^2` |

All values are nonzero under exactly the stated hypotheses. Deleting `Y2` gives the exact curve `C0` in the exact retained coordinates. This parametrization is an embedding: on `U!=0`, `x1/x0=V/U`, and on `V!=0`, `x2/x3=U/V`. These two affine charts prove smoothness and injectivity at the endpoints as well.

## 3. The projected image is an integral quartic with this normalization

Put `(x0,x1,x2,x3,z)=(Y0,Y1,Y3,Y4,Y2)`. The complete uniform identities are

```text
Q1=Delta^2*(x1*x2-z^2),
Q2=((m^2-n)/Delta^2)*Q1+z*L+R,

L=alpha^2*gamma^2*x0-alpha*gamma*m*x1
  -beta*delta*m*x2+beta^2*delta^2*x3,

R=alpha*gamma*m*x0*x2+n*x0*x3-alpha^2*gamma^2*x1^2
  -n*x1*x2+beta*delta*m*x1*x3-beta^2*delta^2*x2^2.
```

The independent checker verifies the second identity after clearing only `Delta^2`. Neither `m` nor `m^2-n` is inverted, so their zero loci are included.

The projection center `P=[0:0:1:0:0]` is outside `S`, since `Q1(P)=-Delta^2!=0`. Projection is a morphism. Every fibre is finite: on its projective line, the nonzero quadratic coefficient `-Delta^2` in `z` bounds the fibre by two points, including multiplicities. Properness makes the morphism finite.

On `L!=0`, the inverse is `z=-R/L`, or homogeneously

```text
[x0:x1:x2:x3] -> [L*x0:L*x1:-R:L*x2:L*x3].
```

This is an isomorphism on that open of the image. The open is nonempty because the restriction of `L` to `c_S` has nonzero endpoint values. The map is therefore birational. Its hyperplane pullback is `H`, so the finite degree-one image has degree `H^2=4`. The image `X` is integral, and `S->X` is its normalization since `S` is normal.

The polynomial `F=R^2-x1*x2*L^2` vanishes on the image. Its `x0^2*x3^2` coefficient is `n^2!=0`, so it is a nonzero quartic in every allowed specialization. The integral hypersurface image has degree four, hence `F`, up to a nonzero scalar, is its actual irreducible equation. The exact identity `Res_z(Q1,Q2)=Delta^4*F` is checked separately; irreducibility and birationality do not follow from that resultant alone.

## 4. The extra normalization point excludes every mate

On the exact curve, the independent source verifies

```text
L_C=alpha^2*gamma^2*U^4-alpha*gamma*m*U^3*V
    -beta*delta*m*U*V^3+beta^2*delta^2*V^4,
R_C=-U^2*V^2*L_C.
```

Both endpoint coefficients are nonzero. Over the algebraically closed field this homogeneous quartic has a root `[U:V]`, and every root has `UV!=0`. No squarefreeness is assumed: repeated-root subloci are covered.

At any such root, both points

```text
y_plus =[U^4:U^3V:+U^2V^2:UV^3:V^4],
y_minus=[U^4:U^3V:-U^2V^2:UV^3:V^4]
```

lie on `S` and project to the same point of `C0`. Indeed `Q1` vanishes on both and `Q2(y_minus)=-2U^2V^2*L_C=0`. They are distinct since characteristic zero and `UV!=0` give `2U^2V^2!=0`.

The negative point is outside `c_S`: the quadratic `Y0*Y2-Y1^2` vanishes on the entire RNC, but its value at `y_minus` is `-2U^6V^2!=0`. This excludes membership through a different parameter as well.

Here is the full-support argument without presupposing a singleton-fibre rule. Because the map is finite and is an isomorphism on `L!=0`, every curve in the inverse image of `C0` must dominate `C0` and equal `c_S`: its generic point lies over the generic point where `L_C!=0` and the inverse is unique. Additional points can only lie over the finite zero set of `L_C`.

Suppose a mate `G` of any degree satisfied `V_X(G)_red=C0`. Its pullback is a nonzero section of `O_S(deg G)`, since otherwise `G` would vanish on all of `X`. It vanishes at `y_minus`, which maps into `C0`. Locally trivialize the line bundle there. A nonzero nonunit in the integral surface's local ring has a height-one zero prime by the principal ideal theorem. Hence a curve in the pullback zero support passes through `y_minus`. Its finite image is contained in `C0`, so that curve must equal `c_S`. This contradicts `y_minus` being outside `c_S`.

This excludes every mate degree simultaneously. It requires neither a conductor calculation nor a bound on the mate degree nor cancellation of a multiple curve divisor on a singular surface.

## 5. The auxiliary double-curve and non-Cartier claims also hold

The owner uses the finite quotient cover from `P1xP1` given by its five invariant `(2,2)` sections. They are basepoint free and their torus function field has index two under `(t,u)->(-t,-u)`. For its odd `(2,2)` section, setting `r=t/u` gives

```text
u^2=-(alpha+beta*r)/(r*(gamma+delta*r)).
```

The four branch points `0,infinity,-alpha/beta,-gamma/delta` are distinct under precisely the hypotheses. The double cover is connected and has genus one. No boundary coordinate fibre is a component, because all four coefficients are nonzero. Its integral `(2,2)` closure has arithmetic genus one, so it has no singular defect.

The stated quadric section `Q` pulls back exactly to the square of this odd section. The independent checker verifies that identity and `Q` vanishing on the actual RNC. The odd curve is irreducible, so its finite image is the entire support of `Q`; since the RNC is contained in that support, the image is exactly `c_S`. The cover is unramified at the generic point, as the involution has only four fixed points. Thus the divisor of `Q` is exactly `2c_S`, giving `2c_S~2H`.

At each A1 vertex the curve is non-Cartier. Its curve local ring is regular of dimension one, whereas the surface local ring has embedding dimension three. Quotient by one element could decrease embedding dimension by at most one, leaving at least two; the curve ideal therefore cannot be principal. Together with the Cartier divisor `2c_S`, its nonzero local class has order two. On the minimal resolution the smooth curve meets each exceptional `(-2)` curve once: its three A1 chart coordinates vanish to first order, so its tangent direction lifts to one transverse point on the exceptional conic. The correction is half the sum of the four exceptional curves, of square `-2`. This validates the auxiliary identity `q=2pi=2`. The exclusion itself is already proved in section 4.

## 6. Frozen evidence and reproduction

The independent [countercheck](../validation/2026-10-09-four-A1-family-audit/countercheck.py) uses universal parameters, not a sample. It verifies the coordinate, cancellation, resultant, actual curve, singular-locus, local A1, cover-square, branch-equation, and extra-point identities. Its SHA256 is

```text
9412835cf6ef3df5f0e1b9c9f3d5208a7bc89ed4e0d1bf904f0d1f0f7386317c
```

Its terminal result is in [countercheck-result.json](../validation/2026-10-09-four-A1-family-audit/countercheck-result.json). Both the frozen owner checker and this checker ran in an isolated snapshot with terminal exit code zero. Their deterministic reports were byte-identical to the corresponding saved repository reports, and snapshot inputs stayed unchanged. The owner replay took 0.580 seconds; the independent replay took 0.651 seconds. The [isolated replay manifest](../validation/2026-10-09-four-A1-family-audit/isolated-replay-manifest.json) preserves the execution record.

The original source is actually at [computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py](../../computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py), with SHA256 `0e72ced585c9e1135648b5e9a278c09964c6677009f50554aac46a68d3b6cef4`. Its root-level computation path is preserved rather than silently rewritten.

Reproduce the independent controls:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-09-four-A1-family-audit/countercheck.py
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-09-four-A1-family-audit/isolated-replay.py
```

The frozen snapshot includes the owner proof as inspected, both exact sources, and both reports. The [aggregate audit manifest](../validation/2026-10-09-four-A1-family-audit/audit-manifest.json) binds this independent note and all evidence files. No process from this bounded audit remains running. The global question and singular-normalization strata outside the explicit family remain open.


---

## Source: 2026-10-09-session-singular-delpezzo-four-A1-family.md

# A genus-one four-A1 normalization family for fixed C0

Date: 2026-10-09. Owner: `singular_normalization_next_frontier`.
Status: **PROVED HERE, submitted for independent audit**. Uniform
exclusion of the displayed family in every mate degree; no assertion
that this family exhausts all singular normalizations of genus one.

This note follows the [sectional-genus reduction](2026-10-09-session-normalization-sectional-genus-zero.md).
The remaining quartic normalization lane has pi=1 or pi=2 and a
non-Cartier smooth lifted curve passing through Sing(S). The example
here realizes the genus-one numerical and torsion conditions with
the actual fixed C0, then excludes its projected quartics by their
full inverse-image fibers. Thus existence of those numerical and
torsion conditions is weaker than existence of a mate.

Throughout k is algebraically closed of characteristic zero. Set

    C0=[U^4:U^3 V:U V^3:V^4] subset P3.

## 1. The singular del Pezzo normalization

In P4[a:b:c:d:e], let

    S:  a e=c^2,       b d=c^2.

This is an integral degree-four complete intersection. One direct
description is the quotient of P1[u0:u1] times P1[v0:v1] by the
involution (u1,v1)->(-u1,-v1), with invariant sections of O(2,2)

    a=u0^2 v0^2, b=u0^2 v1^2, c=u0u1v0v1,
    d=u1^2v0^2, e=u1^2v1^2.

They have no common zero, and the resulting map is generically of
degree two: on the torus its invariant function field is
k((u1/u0)^2,(v1/v0)^2,(u1/u0)(v1/v0)). The image is integral of
degree (2,2)^2/2=4 and is contained in the two independent quadrics.
Those quadrics form a codimension-two complete intersection of
degree four, so their scheme is this integral image. Equivalently
one can use the toric ring with relations a e=c^2=b d; its dense
torus and the reduced coordinate boundary give the same conclusion.

The singular points of S are exactly the four coordinate vertices
with nonzero a,b,d, or e. In the a!=0 chart, eliminating e gives
b d=c^2, the A1 surface singularity at its origin; the other three
charts have the same local equation. All other points have independent
quadric gradients. The surface is S2 by the complete-intersection
property and R1 by its isolated singularities, hence normal.

Write H=O_S(1). Adjunction gives K_S=-H and H^2=4. A general
hyperplane section therefore has genus one. This is a singular
normalization outside the accepted smooth F0/F2/P2 lanes.

## 2. A smooth rational quartic with 2c linearly equivalent to 2H

Choose parameters alpha,beta,gamma,delta satisfying

    alpha beta gamma delta Delta != 0,
    Delta=alpha delta-beta gamma,     M=alpha delta+beta gamma.

The odd (2,2) section on the quotient cover is

    f=alpha u0^2v0v1 + beta u0u1v0^2
      + gamma u0u1v1^2 + delta u1^2v0v1.

Its curve is smooth elliptic. For instance, on the torus put
t=u1/u0, u=v1/v0, and r=t/u. Dividing f by u gives

    u^2=-(alpha+beta r)/(r(gamma+delta r)).

The four branch points 0, infinity, -alpha/beta, -gamma/delta
are distinct on the stated parameter open. The connected degree-two
cover has genus one; the integral (2,2) closure already has arithmetic
genus one, so it has no singular defect. Its quotient is a smooth P1.

More concretely, introduce the standard rational normal quartic
coordinates

    Y_i=U^(4-i)V^i,       i=0,...,4.

Its image in S is obtained by the linear transformation

    a=gamma^2 Y1+2 gamma delta Y2+delta^2 Y3,
    b=-alpha gamma Y0-M Y1-beta delta Y2,
    c=-alpha gamma Y1-M Y2-beta delta Y3,
    d=-alpha gamma Y2-M Y3-beta delta Y4,
    e=alpha^2 Y1+2 alpha beta Y2+beta^2 Y3.

The determinant of this transformation is

    alpha beta gamma delta Delta^3.

It is therefore a projective change of coordinates on the whole
parameter open. Substituting the binary quartics into the two equations
of S gives zero. Its image, denoted c, is a smooth rational normal
quartic of degree four passing through all four A1 vertices, at the
four distinct branch parameters recorded above.

The square of the odd section is the invariant quadric section

    Q=alpha^2 a b+beta^2 a d+gamma^2 b e+delta^2 d e
      +2c(alpha beta a+alpha gamma b+beta delta d+gamma delta e)
      +2(alpha delta+beta gamma)c^2.

Its pullback is exactly f^2. On S its divisor is exactly 2c, because
the quotient map is finite and generically unramified over that curve.
Consequently 2c~2H. The curve c is non-Cartier at the four A1 points;
its local class has order two, as in the
[local lift countershield](#source-2026-10-09-session-singular-local-liftmd).
On the minimal resolution the correction is half the sum of the four
disjoint (-2) curves, so q=-Z^2=2. This realizes the surviving identity
q=2pi for pi=1. No descent of Q to a projected quartic is assumed.

## 3. Projection gives integral quartics containing the exact fixed C0

Use the inverse coordinates Y0,...,Y4 of section 2 and project by
deleting Y2. Put

    (x0,x1,x2,x3,z)=(Y0,Y1,Y3,Y4,Y2).

The image of c is exactly the displayed C0. Let Q1=a e-c^2 and
Q2=b d-c^2, now expressed in these coordinates. Their complete
identities are

    Q1=Delta^2(x1 x2-z^2),
    Q2=-A2(x1 x2-z^2)+L z+R,
    A2=-(alpha^2delta^2+alpha beta gamma delta+beta^2gamma^2),

where

    L=alpha^2gamma^2 x0-alpha gamma M x1
      -beta delta M x2+beta^2delta^2 x3,

    R=alpha gamma M x0x2+alpha beta gamma delta x0x3
      -alpha^2gamma^2 x1^2-alpha beta gamma delta x1x2
      +beta delta M x1x3-beta^2delta^2 x2^2.

The center P=(Y0,Y1,Y2,Y3,Y4)=(0,0,1,0,0) has Q1(P)=-Delta^2,
so it is disjoint from S. The projection is a morphism, and is finite
because its pullback O(1)=H is ample. The coefficient of x0 in L
is alpha^2gamma^2!=0. On the dense open L!=0 the equation L z+R=0
recovers z=-R/L. Thus the map S->X subset P3 is birational, not a
degree-two projection onto a quadric.

Since S is normal and the map is finite birational, it is the
normalization of its image X. The image has degree four and is integral.
Its equation, up to a nonzero scalar, is

    F=R^2-x1 x2 L^2.

Indeed eliminating z gives

    resultant_z(Q1,Q2)=Delta^4 F.

The geometric finite-birational degree calculation proves that F is
the actual integral quartic equation; an uncancelled resultant alone
would not suffice to prove that statement. There is no nonzero scalar
specialization in this parameter open that destroys the argument.

## 4. Uniform full-fiber obstruction to every mate

The lifted c is the rational normal quartic with

    (x0,x1,x2,x3,z)
       =(U^4,U^3V,UV^3,V^4,U^2V^2).

The pullback of L to C0 is the nonzero binary quartic

    L_C=alpha^2gamma^2 U^4-alpha gamma M U^3V
        -beta delta M UV^3+beta^2delta^2 V^4.

Its endpoint values are

    L_C(U,0)=alpha^2gamma^2 U^4,
    L_C(0,V)=beta^2delta^2 V^4.

Therefore it has a zero [U:V] over k and every zero has U V!=0.
Repeated roots and special parameter values are allowed here; the
proof does not assume L_C squarefree. At any such zero,

    R_C=-U^2V^2 L_C=0,
    z^2=x1x2=U^4V^4 != 0.

The two distinct points

    [U^4:U^3V:+U^2V^2:UV^3:V^4],
    [U^4:U^3V:-U^2V^2:UV^3:V^4]

both lie on S and project to the same point of C0. Only the plus
point belongs to c. The C0 parametrization is an embedding, so the
four retained coordinates determine [U:V] uniquely; they cannot be
the retained coordinates of a different parameter on c. Characteristic
zero and U V!=0 make the two points distinct.

Thus the entire inverse image of C0 has an additional point outside
its unique curve lift c. A mate would require its entire support to
be exactly c and nu|c to be an isomorphism. Equivalently this
normalization fiber would have to be a singleton. The two explicit
points contradict that necessary condition.

**Theorem.** Every quartic X in the entire parameter open of section
2 is excluded as a carrier of a mate for fixed C0, in every mate
degree. This includes all repeated-root subloci of L_C in that open.

## 5. Exact controls and independent records

The [uniform exact checker](../../computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py)
reconstructs the actual five-by-five transformation, its determinant,
the two quadratic equations, the elimination identity and its scalar,
the C0 coordinate restriction, both normalization points over every
L_C zero, and the quotient-cover equality q*Q=f^2. Its identities
are over Q[alpha,beta,gamma,delta]; it does not replace parameter
coverage by a finite sample. The geometry and proof of the full-fiber
obstruction are the text above.

The first source run was terminal exit zero with PASS in 0.47 seconds.
Source SHA256:

    0e72ced585c9e1135648b5e9a278c09964c6677009f50554aac46a68d3b6cef4

The [report](../scratch/session-singular-delpezzo-four-A1-family-2026-10-09.json)
retains the uniform parameter open and disclaims an unrestricted STCI
claim. An independent auditor is reviewing the family proof and a
separate child reconstruction checks the exact alpha=beta=gamma=1,
delta=2 example, including its actual conductor.

For that example,

    L=x0-3x1-6x2+4x3,
    R=-x1^2-2x1x2+6x1x3-4x2^2+3x0x2+2x0x3,
    L_C=(U^2-4UV+2V^2)(U^2+UV+2V^2).

All its conductor intersections likewise have U V!=0. The actual
conductor calculation is useful evidence but is not needed by the
uniform support proof, which already uses the actual finite
normalization and two distinct fiber points.

## 6. Scope of the progress

The construction proves that pi=1, non-Cartier c through isolated
normalization singularities, b c~bH, and even 2c~2H can occur on
actual integral quartic carriers of the fixed C0. Those facts alone
do not justify a minimal-degree reduction. The complete normalization
fiber condition excludes the displayed family.

Parameters with alpha beta gamma delta Delta=0 make the displayed
five-coordinate transformation singular. They are not part of this
normalization construction, and no claim about quartic carriers
obtained by another construction at those degenerations is made.
Other four-A1 projections, the A3+2A1 torsion configuration, other
genus-one singular normalizations, and genus-two normalizations still
require a structural argument or an exhaustive correctly scoped
classification. No canonical frontier file has been edited by this
owner note.


---

## Source: 2026-10-09-session-singular-local-lift-independent-audit.md

# Independent audit of the singular local lift

**Accepted, with the scheme-versus-support distinction below.** This is a
countershield in characteristic different from 2, using a smooth conic, not the
fixed degree-four curve `C0`. The universal STCI question remains open.

The proposed rings are
`B=k[x,g,v]/(v^2-4*x*g)` and
`A=k[x,g,w]/((w+(x-g)^2)^2-4*(x+g)^2*w)`, with
`w=(x+g+v)^2`. The quadratic discriminant in `w` is
`64*x*g*(x+g)^2`, nonsquare in `k(x,g)`, so `A` is a domain.
`B` is finite over `A`, generated by `1,v`; the rational expression
`v=(w-x^2-6*x*g-g^2)/(2*(x+g))` proves equality of fraction fields.
The quadric cone `B` is Cohen--Macaulay with an isolated singularity, hence
normal. Therefore it is the normalization of `A`.

The smooth prime divisor `c=(g,v)` maps isomorphically onto the smooth curve
`C=(g,w-x^2)`. Its divisor satisfies `div_B(g)=2*c`. At the cone vertex its
ideal has two minimal generators, so `c` is non-Cartier there and has exact
local divisor-class order two. The derivative identity
`F_g|C=-16*x^3` verifies generic order one of the quartic carrier.

The essential correction is

\[
I_C B=(g,xv),\qquad \sqrt{I_C B}=(g,v).
\]

Thus the inverse image has exactly `c` as its **full support**, but its scheme
is `k[x,v]/(v^2,xv)` and contains a nilpotent supported at the origin. An
argument requiring a reduced scheme-theoretic inverse image cannot use this
example unchanged.

Homogenizing yields an integral quartic whose plane section `g=0` is exactly
`(wt-x^2)^2`, a double smooth conic. This supplies a projective STCI
countershield to a blanket exclusion of singular normalization points along
smooth curves. No claim about the inverse-image scheme at infinity is needed
or made here.

The independent audit directly checked all polynomial identities with SymPy.
The owner's self-contained checker is
[verify_singular_local_lift_countershield_2026_10_09.py](../../computations/verify_singular_local_lift_countershield_2026_10_09.py),
reported terminal `PASS`; the main note is
[2026-10-09-session-singular-local-lift.md](#source-2026-10-09-session-singular-local-liftmd).
A longer independent proof is preserved in
[2026-10-09-singular-normalization-local-countershield-audit.md](#source-2026-10-09-singular-normalization-local-countershield-auditmd).


---

## Source: 2026-10-09-session-singular-local-lift.md

# Smooth lifted curves can meet singular normalization points

Date: 2026-10-09. Author: `singular_local_lift`, subagent of
`singular_normalization_next_frontier`.

Status: **PROVED HERE**, by the explicit algebra below. The universal
STCI problem and the fixed rational quartic C0 problem remain open.
This note provides a local countershield and a surviving local class
group criterion. It makes no classification claim about quartic
normalizations.

## 1. Precise surviving criterion

Let (R,m) be a normal Noetherian local ring of dimension two, and let
P be a height-one prime such that R/P is regular of dimension one.
Thus the reduced curve c defined by P is smooth at the closed point.

**The curve c is Cartier at that point if and only if R is regular.**

For the forward implication, write P=(f). The maximal ideal of R/P
has one generator. Lift that generator to a in m. Then m=(a,f), so
the embedding dimension of R is at most two. Since dim R=2, R is
regular. Conversely a regular local ring of dimension two is a UFD,
so P is principal.

Suppose a mate reduction gives b c Cartier, for an integer b>0. At a
singular point of c, the local divisor class [c] is consequently a
nonzero torsion class, of order dividing b. In particular, if the
local class group is torsion free, c cannot pass through that point.
The same conclusion holds for a locally factorial normalization.

The relation bH=b c in the Weil divisor class group only proves that
[c-H] is killed by b. Without an argument controlling torsion, it does
not prove c is Cartier, c~H, or the existence of a section f with
div(f)=c. This is the exact limitation relevant to the remaining
singular-normalization frontier.

## 2. An affine quartic with isolated singular normalization

Work over an algebraically closed field k of characteristic zero.
Put

    B = k[x,g,v]/(v^2-4xg),
    y = x+g+v,
    w = y^2,
    F = (w+(x-g)^2)^2-4(x+g)^2 w,
    A = k[x,g,w]/(F).

The assignments x->x, g->g, w->(x+g+v)^2 identify A with a subring
of B. To see that the displayed hypersurface is integral, regard F as
a monic quadratic in w over k(x,g). Its discriminant is

    64 x g (x+g)^2,

which is not a square in k(x,g). Gauss's lemma makes F irreducible in
k[x,g,w]. Its image vanishes in B. Since x,g are algebraically
independent in B, the image has dimension two, so its defining prime
ideal is exactly (F).

In B the element y satisfies both

    y^2=w,
    y^2-2(x+g)y+(x-g)^2=0.

Thus B=A[y] is finite over A, with v=y-x-g. Moreover

    y = (w+(x-g)^2)/(2(x+g))

in the fraction field. The denominator is a nonzero element of A,
so Frac(A)=Frac(B): the map is birational.

The ring B is normal. The hypersurface equation v^2-4xg has gradient
(-4g,-4x,2v), so the only singular point is the origin. A hypersurface
is Cohen--Macaulay; here it is regular in codimension one. Serre's
criterion therefore proves normality. Its embedding dimension at the
origin is three and its dimension is two, so that point is singular.
This is the ordinary A1 surface singularity. Since B is normal,
integral over A, and has the same fraction field, it is the full
integral closure of A: an element of Frac(A) integral over A is also
integral over B and hence belongs to B.

Therefore Spec B is the finite birational normalization of the
integral affine quartic Spec A.

## 3. The smooth curve, full support, and mate

Let

    c = V(g,v) in Spec B,
    C = V(g,w-x^2) in Spec A.

Both coordinate rings are k[x], and the restriction of normalization
is the identity on x. Thus c and C are smooth, c->C is an
isomorphism, and C is an embedded smooth parabola in affine
three-space. At the origin its parametrization (x,g,w)=(t,0,t^2)
has nonzero derivative (1,0,0).

The full reduced inverse image of C is c. Indeed v^2=4xg gives
v in sqrt((g)), and

    w-x^2 = 2xv + g(6x+g+2v) in B.

Consequently sqrt((g,w-x^2)B)=(g,v). There is no second normalization
branch lying above C.

The scheme-theoretic inverse image is not asserted to be reduced:
its ideal is (g,xv). Modulo g its coordinate ring is
k[x,v]/(v^2,xv), which retains a nilpotent supported at the origin.
The support assertion and the isomorphism of reduced curves are the
precise statements used here.

The Weil divisor of g in Spec B is exactly 2c. Its zero set has only
the prime (g,v). At that prime x is a unit and v is a uniformizer:
g=v^2/(4x). Hence the valuation is exactly two.

Downstairs the plane g=0 is a mate, since

    F(x,0,w)=(w-x^2)^2.

The surface is smooth at the generic point of C. Substituting g=0,
w=x^2 into the gradient of F gives

    (F_x,F_g,F_w)|C = (0,-16x^3,0).

Thus this example also has carrier order one at the generic point of
C. It does not rely on C being a component of a generic nonnormal
locus. Nevertheless c meets the isolated singular point of the
normalization and its ambient image remains smooth and immersed.

Finally c is not Cartier at the origin. The prime ideal (g,v) needs
two generators there: their independent degree-one classes survive
modulo m(g,v), whose homogeneous terms start in degree two. A
principal ideal in a local ring has at most one generator. Therefore
the local class [c] is nonzero. The relation div(g)=2c shows that
its order is exactly two.

## 4. Projective quartic countershield, with degree explicitly retained

The homogenization in P3 with coordinates [x:g:w:t] is

    F_h = (wt+(x-g)^2)^2-4(x+g)^2 wt.

It is an integral quartic: its affine chart t=1 is integral by the
argument above, and t is not a factor of F_h. The plane g=0 cuts

    F_h|g=0 = (wt-x^2)^2.

The reduced intersection is the smooth projective conic
g=0, wt=x^2. Its gradient on that plane is (-2x,t,w), which never
vanishes at a projective point. The normalization of this projective
quartic restricts on t=1 to Spec B, so the lifted conic certainly
passes through the isolated singular normalization point established
above, while mapping isomorphically in its affine neighbourhood.

The curve here has degree **two**, not degree four. In particular this
is not a mate for the fixed rational quartic C0. We do not assert that
the projective full inverse image of the conic has a single smooth
component at the point t=0; the verified local countershield already
invalidates a local smooth-lift avoidance claim. The explicit plane
mate for the projective conic is, however, an actual global STCI.

## 5. Consequence for the continuation frontier

The implication

    smooth lifted curve + embedded smooth image + full mate support
    + order-one generic carrier  =>  avoidance of Sing(normalization)

is false as a local statement, even for an affine quartic. An
argument specifically using degree four for C0, its global divisor
class, or a classification of the possible normalization singularities
may still exclude the remaining cases. It must supply that additional
input explicitly. The accepted smooth F0/F2 normalization results do
not acquire a singular-normalization extension from this local step.

## 6. Exact verification and sources

The paired checker
`computations/verify_singular_local_lift_countershield_2026_10_09.py`
verifies the literal normalization relations, birational recovery
identity, discriminant, pulled-back curve equation, mate restriction,
generic gradient and projective homogenization. The geometric proofs
above supply normality, finiteness, divisor valuation and the local
Cartier criterion; the script does not label those conclusions proved
merely because a polynomial identity passed.

Terminal replay on 2026-10-09 returned exit 0 and `status: PASS` with
the isolated exact runtime `/private/tmp/stci-cas-venv/bin/python`.
The output is
`research/scratch/session-singular-local-lift-countershield-2026-10-09.json`.
Source SHA256:
`edb3a209b026fd2cbde4a11335087fce7430b291e6380b4774f62ca2415aa503`.
Output SHA256:
`fbc741cde69ab4b33b808711a228b6381fbe7ff2210872dcdec8a4c363475c9b`.
The separate adversarial proof is saved in
`research/notes/2026-10-09-singular-normalization-local-countershield-audit.md`;
it accepts the example and explicitly checks the nonreduced inverse
image scheme. Independent agreement is additional audit evidence;
the mathematical proof remains the explicit argument above.

Normality uses the primary
[Stacks Project, Serre's criterion](https://stacks.math.columbia.edu/tag/031S).
The normalization identification also uses the definition of a normal
domain as integrally closed in its fraction field in the
[Stacks Project, normal rings](https://stacks.math.columbia.edu/tag/037B). All other
algebra in the countershield is explicit in this note. No novelty claim
is made.


---

## Source: 2026-10-09-singular-normalization-local-countershield-audit.md

# Singular-normalization countershield: independent audit

Status: **PROVED**, for an algebraically closed field of characteristic different
from 2. This example concerns a smooth degree-two curve, not the fixed rational
quartic `C0`. It prevents a general argument from excluding a singular point of
the normalization merely because the downstairs curve is smooth and has a
set-theoretic complete-intersection mate.

Let

\[
B=k[x,g,v]/(v^2-4xg),\qquad y=x+g+v,\qquad w=y^2,
\]

and put

\[
F=(w+(x-g)^2)^2-4(x+g)^2w,
\qquad A=k[x,g,w]/(F).
\]

The discriminant of `F`, viewed as a monic quadratic in `w`, is
`64*x*g*(x+g)^2`. It is not a square in `k(x,g)`: the valuations at the prime
elements `x` and `g` are odd. Thus `F` is irreducible, and substitution of
`w=(x+g+v)^2` embeds `A` in `B`. The kernel has height one and contains the
irreducible polynomial `F`, so it equals `(F)`.

The ring `B` is finite over `A`, generated as an `A`-module by `1,v`, since
`v^2=4xg`. It has the same fraction field because

\[
v=\frac{w-x^2-6xg-g^2}{2(x+g)}.
\]

The quadric cone `B` is normal: it is a hypersurface, hence Cohen--Macaulay,
and its singular locus consists only of the origin in this two-dimensional
surface. Therefore it satisfies Serre's `S2` and `R1` conditions. Consequently
`B` is exactly the finite birational normalization of `A`.

The prime divisor `c=(g,v)` has coordinate ring `k[x]`. Its image is
`C=(g,w-x^2)`, also with coordinate ring `k[x]`, and the restricted map is an
isomorphism. At the generic point of `c`, `x` is invertible and
`g=v^2/(4x)`, so `div_B(g)=2c`. At the origin the ideal `(g,v)` has two
independent generators modulo the maximal ideal times this ideal; it is not
principal. Hence `c` is non-Cartier at that point, and its local divisor class
has exact order two.

The **scheme-theoretic** inverse image of `C` is

\[
(g,w-x^2)B=(g,xv).
\]

Its radical is `(g,v)`, so its full support is precisely `c`. Its quotient is
`k[x,v]/(v^2,xv)`; the nilpotent `v` is supported at the origin. The claim is
about support, not equality with the reduced inverse-image scheme.

Differentiation gives `F_g|C=-16*x^3`. Thus `F` has order one along the generic
point of `C`, although the normalization is singular at the point over its
origin and the lifted curve is non-Cartier there.

Homogenize with coordinates `[x:g:w:t]`:

\[
F_h=(wt+(x-g)^2)^2-4(x+g)^2wt.
\]

The homogenization is irreducible because its dehomogenization is irreducible
and it is not divisible by `t`. Its plane section is exactly

\[
F_h\vert_{g=0}=(wt-x^2)^2.
\]

The conic `g=0, wt=x^2` is smooth, and the intersection scheme of the integral
quartic surface with the plane `g=0` is its double. The normalization over the
chart `t=1` is `Spec B`, so it really has a singular point above this smooth
conic. This gives a projective set-theoretic complete-intersection example,
with generic multiplicity two, rather than only a formal local model.

An independent SymPy calculation on 2026-10-09 verified the normalization
substitution modulo `v^2-4*x*g`, the displayed discriminant, the rational
inverse identity, `F_g|C`, and the squared conic plane section. All remainders
were zero where required. These calculations check identities; the arguments
above establish normality, finiteness, irreducibility, and divisor behavior.

No conclusion about the fixed degree-four curve `C0`, or the universal STCI
problem, follows from this example.
