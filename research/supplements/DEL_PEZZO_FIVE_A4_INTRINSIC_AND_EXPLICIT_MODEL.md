# Degree-five del Pezzo A4 model: intrinsic classification and explicit equations

Complete mathematical analyses with precise projection-center distinctions and conditional scope. Computational scripts remain in their original executable locations.

---

## 1. dp5 a4 intrinsic pair classification

# The entire degree-five A4 intrinsic pair, and the missing projection-center parameter

Date: 2026-10-11. Owner: `oct11_a4_intrinsic_model`.

Status: **DIRECT GEOMETRIC PROOF; EXACT SUPPORTING IDENTITIES**. The
contraction argument and the conic orbit argument were independently
obtained by `oct11_quintic_structural_frontier/quintic_conormal_audit`.
This note classifies the intrinsic pair in the genus-one quintic lane;
it does not exclude quintic mates, classify all conductor schemes, or
bound a descending power. Frozen records and the earlier evidence seal
were left untouched.

Hypotheses throughout: an algebraically closed field of characteristic
zero; the genus-one normalization S and smooth lifted quartic c in
[the frozen quintic frontier](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-quintic-structural-frontiermd),
with its independently checked
[A4 and unique-line reductions](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md).
Thus S is a normal degree-five anticanonical del Pezzo surface, its only
singularity is A4, `5c~4H`, and its unique degree-one line ell satisfies
`5ell~H`, `c+ell~H`. The resolution has a four-prime A4 chain, c meets
one interior vertex transversely, and ell meets the opposite interior
vertex transversely.

## 1. An intrinsic contraction proves that the plane marking is exhaustive

Let M be the minimal resolution. Label its exceptional chain

    R1--R2--R3--R4,

so that the strict c meets R2 and the strict ell meets R3. Both contact
points are nonnodes: each strict transform meets precisely one prime,
once transversely. The strict ell is a smooth (-1)-curve. Contract,
in order,

    ell#, R3, R2, R1.                              (1)

After ell# is contracted, R3 becomes a smooth (-1)-curve. After R3 is
contracted, R2 becomes a smooth (-1)-curve. After R2 is contracted,
R1 becomes a smooth (-1)-curve. The original distinct transverse
intersection directions ensure that each intermediate contraction is
the ordinary contraction of a smooth (-1)-prime, and that all the
remaining named primes remain smooth. No contraction of an entire
singular surface or an unproved simultaneous graph operation is used.

The self-intersection of R4 evolves as follows:

| Stage | Initial | After ell# | After R3 | After R2 | After R1 |
| --- | --- | --- | --- | --- | --- |
| Square of the remaining R4 | -2 | -2 | -1 | 0 | 1 |

The final surface is smooth rational with canonical square nine. The
classification of smooth minimal rational surfaces makes it P2: a
nonminimal rational surface has canonical square at most eight, and
the minimal ruled rational surfaces have square eight. The image of
R4, now a smooth rational curve of square one, is a plane line.

Reverse (1). The first center is on this line; the second is its
intersection with the first exceptional; the third is its intersection
with the second exceptional. The fourth is a point of the third
exceptional away from both its neighboring exceptional and the strict
line. These exclusions follow from the nonnode contact of ell# with
R3. They retain the entire possible family of fourth centers.

Choose plane coordinates [x:y:z], let p1=[0:0:1], and let the line be
y=0. In the affine chart z=1 the four-point cluster is

    (y-lambda x^3, x^4), lambda!=0.               (2)

The first two zero jets express the first three centers on the line;
the nonzero third jet expresses the free fourth center. A diagonal
projective change normalizes lambda to one. Therefore the familiar
plane model with local cluster `(y-x^3,x^4)` is **every intrinsic pair
under the stated hypotheses**, rather than only an example.

In the total-transform basis h,e1,e2,e3,e4,

    L=3h-e1-e2-e3-e4,
    R1=e1-e2, R2=e2-e3, R3=e3-e4,
    R4=h-e1-e2-e3, ell#=e4.                    (3)

The correction vector `(3,6,4,2)` for c gives

    c#=(4L-3R1-6R2-4R3-2R4)/5=2h-e1-e2.       (4)

Thus c becomes a plane conic tangent to y=0 at p1, whose nonzero
second-order coefficient ensures that it does not pass through p3.

## 2. All possible smooth conics form one orbit

The entire conic system in (4) is

    A yz+B x^2+C xy+D y^2=0.                    (5)

It gives the required smooth c precisely when `A B!=0`.
Indeed A=0 makes p1 singular or the conic reducible; B=0 makes the
conic reducible with y as a factor. For A B!=0 the conic determinant
is nonzero, its tangent at p1 is y=0, and its second-order coefficient
is nonzero. It passes through the first two centers and no later
center. This explicitly proves that smooth c do exist in the A4
surface; its divisor classes alone do not yield an impossibility.

Every plane projective automorphism preserving the cluster (2), with
lambda=1, has, after setting its z coefficient to one, the form

    x'=a x+b y,
    y'=a^3 y,
    z'=z+g x+d y,       a!=0.                  (6)

Origin and tangent-line preservation force the triangular shape;
preservation of the third jet gives `y'-scale=(x'-scale)^3`.
Conversely these matrices preserve the complete length-four cluster.
The exact transformation of the reference conic is

    y'z'+x'^2 =
      a^3 yz+a^2 x^2+(a^3 g+2ab)xy+(a^3 d+b^2)y^2.  (7)

After scaling (5) to A=1, choose `a=1/B`, and then choose g,d to
realize C,D; b can be arbitrary. Hence the cluster stabilizer acts
transitively on **all** the smooth conics (5). In particular the
intrinsic pair `(S,c)` is unique up to polarized isomorphism, and may
always be written with

    c_plane: yz+x^2=0.                           (8)

This is an exhaustion proof: the contraction first produces every
possible marking, then (7) treats every conic in that marking.

## 3. The exact residual automorphism group is a translation group

It is essential to retain the smaller automorphism group after c has
been normalized. An automorphism of S lifts to its minimal resolution,
preserves the unique line ell, and hence preserves R3. The A4 graph
then fixes every vertex. Consequently it preserves the sequence (1)
and descends to a plane automorphism of the cluster. There is no
unaccounted diagram reversal or Cremona transformation in this pair.

In (7), preserving the standard conic up to scalar forces

    a=1, g=-2b, d=-b^2.

Thus **the full automorphism group of the intrinsic pair is Ga**,
represented by

    x'=x+b y, y'=y, z'=z-2b x-b^2 y.             (9)

Parametrize (8) by `[x:y:z]=[st:t^2:-s^2]`. Equation (9) acts as
`[s:t]->[s+bt:t]`, namely translation of r=s/t. It fixes the point
t=0, which is the A4 point on c, and has no remaining scaling
parameter on the affine r-line.

## 4. Complete anticanonical formulas and actual Cartier sections

The entire anticanonical cubic system through the cluster has basis

    Z0=yz^2-x^3, Z1=xyz, Z2=y^2z,
    Z3=x^2y,     Z4=xy^2, Z5=y^3.              (10)

The four jet conditions on ten plane cubics give exactly these six
independent forms. On the smooth blowup this system is nef and big:
for a plane curve of degree m distinct from y=0, Bezout with y=0
gives `m>=m1+m2+m3`, while `m4<=m`. Hence its anticanonical
degree is `3m-sum mi>=m>0`. The strict y=0 and the first three
exceptional differences have degree zero and form precisely A4;
the fourth exceptional has degree one. The usual anticanonical
construction of a weak del Pezzo surface contracts exactly that
A4 chain. This is the same anticanonical embedding input already
verified in the frozen structural reduction, not a new claim that
an arbitrary rational surface is anticanonically embedded.

Use coordinates

    U0=Z5, U1=Z4, U2=Z3, U3=-Z1, U4=Z0-Z1,
    hsec=Z2+Z3.

Restrict (10) to `[st:t^2:-s^2]` and remove the common factor t^2.
Then

    c=[t^4:st^3:s^2t^2:s^3t:s^4:0].             (11)

This is the complete smooth rational normal quartic, including
t=0. The unique line ell is its tangent line at t=0, spanned by
the U3 and U4 coordinate directions. The hyperplane `hsec=0`
has actual divisor c+ell; the section U0 has actual divisor 5ell.
The latter can also be read from the fourth exceptional valuation
of y^3: order nine minus base order four equals five. Its remaining
plane support is y=0, which contracts to the A4 point. Finally

    Q=hsec^5/U0=y^2(yz+x^2)^5                   (12)

is an actual regular section of 4H with divisor 5c. On the plane,
the right side is a degree-twelve form and satisfies the required
fourfold cluster conditions; the divisor relation also proves its
regularity intrinsically. Neither U0, hsec, nor Q is assumed to
descend to any chosen four-coordinate projection.

The coordinate/model auditor is preparing
[a separate explicit-model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
Its global ideal and local A4 certificates are independent of the
geometric contraction exhaustion here.

## 5. Relative C0 projection centers have two lanes, one with a modulus

The fixed space-curve C0 is the projection of the complete rational
normal quartic from its deleted-middle-coordinate point. Under the
SL2-equivariant identification of points in its P4 span with binary
quartics, that center has two distinct double roots. Conversely any
such center is PGL2-equivalent to the deleted-middle center and
projects the curve to a projective equivalent of C0.

For explicit signs and binomial factors, in the affine coordinate r
of (11), send a point `p=(p0,...,p4)` to

    Phi_p(Z)=p0 Z^4-4p1 Z^3+6p2 Z^2-4p3 Z+p4.  (13)

The rational-normal point `(1,r,r^2,r^3,r^4)` maps to `(Z-r)^4`.
The deleted-middle point maps to `6Z^2` (the two roots are zero
and infinity, each of multiplicity two).

The actual intrinsic pair automorphisms (9) permit only translations.
Therefore the C0 projection centers divide as follows:

* **Endpoint lane:** one double root equals the fixed A4 point at
  infinity. Translate the other root to zero. There is one such orbit,
  represented by the deleted-middle point `(0,0,1,0,0)`.
* **Nonendpoint lane:** both double roots are finite. Translate their
  midpoint to zero and write them as `delta,-delta`, with
  `delta!=0`, modulo `delta->-delta`. A center representative is

      p_delta=(1,0,-delta^2/3,0,delta^4),
      Phi_p=(Z-delta)^2(Z+delta)^2.              (14)

There is **no residual scaling automorphism of `(S,c)`** that can
normalize arbitrary nonzero delta to one. Thus the deleted-middle
center exhausts the endpoint lane only. Investigating its four
projection-lift parameters alone cannot exclude all genus-one
quintic carriers.

The original projection to P3 has a line center in P5. It meets the
hyperplane span of c at p. Once p is fixed, the line extensions
outside that hyperplane form a four-parameter space. The nonendpoint
lane therefore retains delta as well as those four parameters.
Avoidance of S, finiteness, birationality, and the full inverse-support
condition are still required in both lanes. These orbit statements
concern the intrinsic curve projection only; they do not assert that
every line extension is an admissible normalization map.

## 6. Exact check record and remaining mathematical boundary

The supporting source
[verify_session_quintic_a4_pair_classification_2026_10_11.m2](../computations/verify_session_quintic_a4_pair_classification_2026_10_11.m2)
passes **15 exact checks**: the cluster and conic transformations,
translation group, full rational-normal restriction, actual section
identity, A4 lattice and corrections, and the nonendpoint center
formula. Source SHA256:

    e710635b396707a6414fb142472db1ead3b17cfd06c1cb1ee18c4f64318108f2

The successful execution is
[attempt 05](../validation/2026-10-11-quintic-a4-pair-classification/attempt-05/execution-record.json).
Attempts 01--04 are retained in the same validation folder, including
their source snapshots and raw streams. They failed from Macaulay2
namespace collisions (`hh`, then `roots`), rather than mathematical
assertion failures. Attempt 02 changed a suspected name without curing
the collision; the full history is not hidden. Source snapshots are
copies and are not counted as independent certificates.

The exhaustion argument is the written contraction proof in section 1,
not the fifteen symbolic checks. The quintic STCI question remains
open. The next actual task is the entire conductor descent of Q^k,
with k unbounded, in **both** projection-center lanes. All higher
normalization genera and normal quintics remain outside this note.


---

## 2. dp5 a4 explicit model independent audit

# An explicit degree-five A4 del Pezzo pair: independent coordinate audit

Date: 2026-10-11. Author: `quintic_conormal_audit`.
Status: **EXACT CONSTRUCTION AND INDEPENDENT GEOMETRIC AUDIT**.

This note verifies the anticanonical model and pair arising in the
sectional-genus-one quintic reduction. It does not exclude that lane or
establish an ambient mate. Earlier frozen audit notes are unchanged.
Work over an algebraically closed field of characteristic zero.

The inputs concerning a hypothetical mate are in the separately frozen
[quintic structural audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md):
the normalization is a degree-five del Pezzo surface with one A4 point;
the smooth quartic meets an interior A4 vertex; the unique degree-one
curve meets the opposite interior vertex. The coordinates below verify
the abstract model and pair. Placement of the subsequent P3 projection
center is a further parameter and is treated explicitly in Section 8.

## 1. The complete system and its length-four base cluster

Use plane coordinates [x:y:z], and put

    Z0=yz^2-x^3, Z1=xyz, Z2=y^2z,
    Z3=x^2y, Z4=xy^2, Z5=y^3.

There are no base points on z=0: Z0 forces x=0 there, and Z5 then
forces y=0. In the affine z=1 chart the common ideal is exactly

    (y-x^3,x^4).

Indeed xy becomes x^4 modulo y-x^3, and the remaining monomials are
in the resulting ideal. The base scheme is curvilinear of length four.
A plane cubic belongs to it precisely when its coefficients of 1,x,x^2
vanish and its x^3 and y coefficients sum to zero. Thus the six displayed
cubics are an actual basis of the complete cubic system through the
cluster, rather than a subsystem selected by a generic rank computation.

## 2. Four explicit simple blowups resolve the system

The successive main charts, after dividing by the exceptional factor at
each step, are:

| step | substitution | section vector |
| --- | --- | --- |
| 1 | y=xu1 | `(u1-x^2, xu1, xu1^2, x^2u1, x^2u1^2, x^2u1^3)` |
| 2 | u1=xu2 | `(u2-x, xu2, x^2u2^2, x^2u2, x^3u2^2, x^4u2^3)` |
| 3 | u2=xu3 | `(u3-1, xu3, x^3u3^2, x^2u3, x^4u3^2, x^6u3^3)` |
| 4 | u3=1+xu4 | `(u4, 1+xu4, x^2(1+xu4)^2, x(1+xu4), x^3(1+xu4)^2, x^5(1+xu4)^3)` |

The first three centers have coordinates (0,0); the fourth is
`(x,u3)=(0,1)`. In each alternate chart the transformed Z0 is a unit
on the exceptional divisor away from the indicated next center. At the
third step its unique remaining zero is u3=1, and at the fourth step
the transformed Z1 is a unit along the main exceptional chart. Thus
there are exactly four simple base points and no unresolved base scheme.

Let M be the resulting smooth four-point blowup, with total exceptional
classes e1,...,e4 and plane line class h. The complete polarization is

    L=3h-e1-e2-e3-e4=-K_M, L^2=5.

It is basepoint free. The map is birational: on y!=0 the ratios
`Z4/Z5=x/y` and `Z2/Z5=z/y` recover the plane coordinates. Its image
therefore has degree five.

The four contracted prime curves are

    E1=e1-e2, E2=e2-e3, E3=e3-e4,
    E0=h-e1-e2-e3.

They form the chain E1--E2--E3--E0, each with square minus two. The
first three centers lie successively on the strict line y=0; the fourth
lies on the third exceptional curve away from that line. E0 is the strict
line y=0. All four map to P0=[1:0:0:0:0:0]. The fourth exceptional
curve ell#=e4 is not contracted: its image is

    ell={Z2=Z3=Z4=Z5=0},

with parametrization [u4:1:0:0:0:0] in the main chart.

## 3. Five exact defining quadrics

In P5 the image ideal is generated by

    Z4^2-Z3 Z5,
    Z2 Z4-Z1 Z5,
    Z2 Z3-Z1 Z4,
    Z2^2-Z3 Z4-Z0 Z5,
    Z1 Z2-Z3^2-Z0 Z4.

The delegated Macaulay2 audit computed the exact elimination kernel,
not merely the ideal generated by quadrics that happen to vanish.
Its coordinate ring has dimension three, degree five and Hilbert series

    (1-5t^2+5t^3-t^5)/(1-t)^6.

There is also a direct cover proof of integrality and normality. In the
chart Z5=1 the equations solve exactly as

    Z4=r, Z3=r^2, Z2=t, Z1=rt, Z0=t^2-r^3.

That chart is A2. On the complement Z5=0 the reduced support of the
equations is ell. At a point of ell with Z1!=0, set Z1=1 and write
a=Z0,b=Z2,c=Z3. The equations give

    b(1-ac)=c^2, Z4=bc, Z5=b^2c.

Near ell the factor 1-ac is a unit. This solves the local ring as a
localization of k[a,c], so the surface is smooth at every point of
ell other than P0. The remaining P0 chart is handled exactly below.
These covers also rule out embedded boundary components.

## 4. The formal and algebraic A4 chart

Set Z0=1 and write a=Z1,b=Z2,c=Z3. The last two quadrics eliminate

    Z4=ab-c^2, Z5=b^2-c(ab-c^2).

The remaining ideal is generated by

    b(c-a^2)+ac^2.

The triangular polynomial change

    u=c-a^2, v=b+ac+a^3

has a polynomial inverse, and the equation becomes

    uv+a^5=0.

This is an exact affine coordinate-ring isomorphism, hence also an
isomorphism of completed local rings. In characteristic zero its only
singular point is a=u=v=0. The image has exactly one A4 singularity,
at P0. The four explicit (-2) curves above give its minimal resolution;
crepancy follows from K_M=-L and K_S=-H. In particular the full
anticanonical model, its normality and its singularity are checked
directly, without assuming them from the name "del Pezzo".

The saturated projective Jacobian scheme is nonreduced of degree four.
The delegated exact computation obtains its ideal

    (Z5,Z4,Z3^2,Z2 Z3,Z2^2,Z1 Z2,
     Z0 Z2+2Z1 Z3,Z1^2-Z0 Z3),

whose radical is (Z1,Z2,Z3,Z4,Z5). The nonreduced Jacobian scheme is
retained; its degree is not a count of four singular points.

## 5. The smooth quartic and tangent line

Choose the smooth plane conic

    yz+x^2=0.

It passes through the first two cluster centers but not the third.
Its strict transform has class c#=2h-e1-e2, square two, and L-degree
four. It meets E2 once away from the chain nodes. Thus its image c
meets A4 vertex two, while ell# meets vertex three.

The conic parametrization `[x:y:z]=[st:s^2:-t^2]` gives, after
removing the common factor s^2, the image

    c=[t^4-st^3 : -st^3 : -s^2t^2 : s^2t^2 : s^3t : s^4].

The five independent quartic monomials show directly that c is a
rational normal quartic in the hyperplane Z2+Z3=0. The delegated
kernel calculation additionally checks the exact scheme identity

    I_S+(Z2+Z3)=I_c intersect I_ell.

The saturated intersection ideal is

    I_(c intersection ell)=(Z2,Z3,Z4,Z5,Z1^2).

It has length two, supported at P0. Thus ell is exactly the tangent
line to c at the A4 point, rather than a second secant obtained only
by numerical intersection theory.

## 6. The distinguished section and useful affine coordinates

Put h0=Z2+Z3. On S its actual divisor is c+ell. The section Z5 has
actual divisor 5ell. This is visible on the fourth blowup chart:
Z5 has order five along e4, and its other plane zero components are
contracted. Therefore

    Q=h0^5/Z5 in H0(S,4H), div(Q)=5c.

The normality of S and the absence of poles make this a regular entire
section. In plane coordinates it is the homogeneous degree-twelve
polynomial `y^2(yz+x^2)^5`; its class is four times L. It is not being
asserted to be a polynomial in the four coordinates of a P3 projection.

The invertible linear change

    U0=Z5, U1=Z4, U2=Z3, U3=-Z1,
    U4=Z0-Z1, H0=Z2+Z3

puts the y!=0 chart, with r=x/y and T=z/y+r^2, in the form

    [U0:U1:U2:U3:U4:H0]
      =[1:r:r^2:r^3-rT:r^4-(2r^2+r)T+T^2:T].

Here c is T=0, ell is the line U0=U1=U2=H0=0, the A4 point is the
point r=infinity on c, and Q=T^5 in this trivialization. These affine
identities do not replace the omitted boundary or conductor checks.

## 7. The abstract pair is exhaustive after the marking audit

The separate intrinsic-model agent independently confirmed the following
classification argument; its dedicated note records that proof. Starting
from the accepted unique line, label the roots so c# meets E2 and ell#
meets E3. Contract successively

    ell#, E3, E2, E1.

Each is a smooth (-1) curve at its turn. The remaining root E0 has
self-intersection sequence -2,-2,-1,0,1. The resulting smooth rational
surface has Picard rank one and K^2=9, so is P2 with E0 a line. Reversing
the four contractions gives exactly three successive centers on that
line and a fourth free center on the third exceptional divisor, away
from its two chain nodes. Plane coordinates therefore give the cluster
`(y-lambda x^3,x^4)`, lambda!=0; scaling normalizes lambda to one.
The quartic strict transform becomes a smooth conic through the first
two centers, with equation

    yz+alpha x^2+beta xy+gamma y^2=0, alpha!=0.

All such conics are equivalent under the cluster stabilizer. Indeed
the projective substitution

    x'=a x+b y, y'=d y, z'=e x+f y+g z,
    d g^2=a^3

preserves the length-four cluster. Choose
`g=1,a=1/alpha,d=1/alpha^3,b=0,e=beta,f=gamma`.
Then `y'z'+x'^2=alpha^(-3)(yz+alpha x^2+beta xy+gamma y^2)`.
This verifies the orbit calculation directly. Thus the displayed model
exhausts the abstract admissible (S,c) pair, conditional on the accepted
upstream A4 and unique-line reduction. It does not yet exhaust the
chosen P3 projections of that pair.

## 8. Projection-center scope: a required additional distinction

The coordinates in Section 6 fix the intrinsic A4 point at r=infinity.
Choosing restriction space `span(1,r,r^3,r^4)` puts the P4 center at
the omitted-middle-coordinate point. Its binary quartic has two double
roots at zero and infinity. Relative to the A4 point, this is the
endpoint placement of the fixed C0 projection.

For the entire fixed-C0 quintic lane, the center must instead be allowed
to range through the PGL2 orbit of this two-double-root binary quartic.
The automorphisms of the pair preserve the A4 point. In the plane model
their action on c is translation r->r+a; the conic-preserving projective
substitution can be chosen as

    x'=x+a y, y'=y, z'=z-2a x-a^2 y,

which fixes T. A pair of finite double-root points therefore has a
remaining separation parameter up to interchange, whereas a pair
containing infinity has a single translation orbit. The independent
intrinsic-model note owns the full automorphism and center-orbit proof.

Consequently four coefficients for lifting the fixed space
`span(1,r,r^3,r^4)` through the one-dimensional restriction kernel are
only the endpoint projection sublane. They must not be advertised as
an exhaustion of all A4 quintic carriers. The nonendpoint placement,
center avoidance, finite birationality, full inverse support and descent
of every possible Q^k remain separate requirements.

## 9. Evidence and continuation

The independent global-kernel and local-chart Macaulay2 agents preserve
their exact sources, raw output, failed scaffolds and execution records
under distinct new October 11 paths. This note records direct geometric
proofs and does not count a child execution again as a new verifier.
The exact logs distinguish degree four of the Jacobian scheme, length
two of the curve-line intersection, and degree five of S.

The next mate question is genuinely global: whether a permitted P3
projection can make any Q^k descend through its entire conductor while
retaining full inverse support over C0. Neither a successful local A4
chart nor the unique abstract pair supplies that descent or bounds k.
