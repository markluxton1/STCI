# Root descent and defects on full conductor schemes

**Scope and status.** Independently reviewed sheaf identities,
local-to-global arguments and a specified projection witness. Root adjoining can leave a punctual normalization defect even
when an actual power descends. On a reducible conductor it can also leave
a one-dimensional defect. The formulas below retain that distinction and
the actual conductor's scheme structure.

The quintic applications use the inherited degree-five A4 normalization of
the fixed characteristic-zero quartic. Their earlier smooth/integral-
conductor consequences are retained as distinct mechanisms; the
[complete Gorenstein-normalization theorem](quintic_gorenstein_normalizations.md)
uses further geometry to cover that entire quintic class. Neither result
classifies non-Gorenstein normalizations or settles unrestricted STCI.

## Exact source and claim

Let S be an integral nonnormal quintic carrier with an actual octic mate
whose intersection has sole reduced support C. Suppose its normalization
`nu:X->S` is Gorenstein. Reuse the exact conclusions of the
[quintic carrier-structure proof](../supplements/QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit):
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

## The total length

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

## Why the finite defect lies on C

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

Completion descends S2 to A' at p. By [the total-length calculation](#the-total-length), the finite birational extension
`A' subset B` differs only at closed points, so A' agrees with the
normalization in codimension one and satisfies R1. Serre's criterion
then makes A' normal at p, forcing equality with B there. This proves
the support assertion in (4).

This proof does **not** assert that A' is etale over A. The raw rank-two
algebra `A[T]/(T^2-g)` is etale off C, but its image A[q] in the common
function field is birational and can behave differently. The branch
factorization in the hypersurface, together with the finite-length
quotient, supplies the needed S2 and R1 assertions.

## General form and geometric limits

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
[local square-descent construction](square_descent_and_singular_gluing.md)
gives actual hypersurfaces with a supported local mate and
`length B/A[w^m]=(m-1)k>0`. Adjoining the root agrees with normalization
in codimension one but leaves a punctual non-S2 defect. The missing
global input is a restriction on which local defects the actual
quintic projection can realize, including the point on the A4 source.

## Generic root generation and the full cokernel

Use the accepted actual normalization quotient

    M=nu_*O_X/O_S=omega_Gamma(-1),
    L=O_Gamma(-4),   phi_q:L -> M.

Here phi_q sends a local generator to the class of q in M. It is the
class, rather than q as a function on the normalization, that may
vanish on a conductor component. With K its kernel and C_q its
cokernel there is an exact sequence

    0 -> K -> L -> M -> C_q -> 0.                        (1)

At a generic conductor point eta, C_q vanishes exactly when the class
of q generates the canonical module M_eta. For reduced Gamma this
means nonzero restriction on every component. For generically
nonreduced Gamma, mere nonvanishing is insufficient: the class must
generate its entire generic Artin canonical module. A noncyclic
canonical module cannot be generated by a single root class.

Thus the integral length-17 conclusion requires generic generation on
every conductor component. The supported-power hypothesis alone
does not give it, as [the componentwise square construction](square_descent_and_singular_gluing.md#an-actual-supported-square-with-componentwise-descent)
demonstrates in an actual hypersurface local ring. Neither that control nor (1) decides the actual projection locus.

## Exact finite defect when Gamma is reduced

Here allow an integral hypersurface carrier S of degree a and a
normalization quotient `M=omega_Gamma(-(a-4))`, with Gamma a reduced
projective Cohen–Macaulay curve. Let q be a section of kH on the
normalization. Suppose q squared is an actual descended section
supported on C. Partition Gamma into reduced unions of components:
E is where the class of q vanishes generically, and F is where it
does not. Take F nonempty. The following assertion is about the
whole scheme and its dualizing module, including intersections
between E and F.

The map phi_q factors canonically as an injection

    O_F(-k) -> omega_F(-(a-4)) -> omega_Gamma(-(a-4)).    (2)

Its first cokernel T is finite and has length

    length T = 2p_a(F)-2+(k-a+4)deg(F).                 (3)

For the quintic quartic-root problem this becomes
`2p_a(F)-2+3deg(F)`. The convention is `p_a(F)=1-chi(O_F)`,
also when F is disconnected. When F=Gamma, its degree five and
arithmetic genus two recover 17.

More precisely, T is the maximal zero-dimensional subsheaf of C_q.
The quotient C_q/T is pure one-dimensional on E, unless E is empty,
and

    Supp(T) subset C intersect F.                       (4)

To prove (2), let I_F be the ideal of F in Gamma. Multiplying the
root class by I_F gives zero at every generic point: on F the ideal
vanishes and on E the root class vanishes. The canonical module is
torsion-free on the reduced CM curve, so the product is zero
everywhere. Same-dimensional duality identifies
`Hom(O_F,omega_Gamma)=omega_F`. The resulting map from O_F(-k)
is generically nonzero on every component, hence injective, with
finite cokernel.

Dualizing `0->I_F->O_Gamma->O_F->0` gives

    0 -> omega_F -> omega_Gamma -> Hom(I_F,omega_Gamma) -> 0.

At a closed point O_F is a one-dimensional CM module. Local duality
therefore gives `Ext^1(O_F,omega_Gamma)=0`, justifying exactness on
the right. The last Hom is pure one-dimensional: I_F is CM by the
depth lemma, and a nonzerodivisor of the canonical module acts
injectively on the Hom. After twisting, the resulting sequence

    0 -> T -> C_q -> Hom(I_F,omega_Gamma)(-(a-4)) -> 0    (5)

proves the maximal-zero-dimensional assertion. Taking Euler
characteristics in the first map of (2), with duality on F, gives
(3).

For (4), the square assumption makes A+Aq the algebra A[q] in every
local frame. Away from C the descended square is a unit. In the
completed hypersurface ring choose a square root of that unit and
partition its analytic branches by the two signs of q. Adjoining
q separates the sign groups into hypersurface branch-unions, each
Cohen–Macaulay. The normalization is also CM; their quotient has
depth at least one. Thus it has no finite submodule there. This is
the same actual branch argument as in the
[hypersurface branch proof](root_descent_and_conductor_defects.md#why-the-finite-defect-lies-on-c),
now retaining its possible one-dimensional quotient instead of
assuming that quotient is finite.

This formula is a necessary accounting identity. A restriction needs
the actual components, their genus and degree, and the local zeros
of (2). Intersections E intersect F are already encoded by the
embedded dualizing submodule and (5); no separate unproved attachment
length may be added. The support assertion has not been extended to
general q^N here: A+Aq need not be the algebra A[q] when Gamma is
not Gorenstein. The decomposition and formula likewise do not extend
to nonreduced Gamma merely by passing to its reduced support.

## Every mate power when the full conductor is smooth

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
Consequently the algebra is still

    A'=A[q]=A+image(O_S(-4) --q--> B),

even when q squared itself has not been shown to descend. The nonzero
root-class map

    O_Gamma(-4) --delta(q)--> omega_Gamma(-1)

is injective with finite cokernel, and its Euler-characteristic difference
gives length 17, as in the integral calculation above.

Off C, q^N is a unit. In the [completed branch proof](#why-the-finite-defect-lies-on-c) choose an
N-th root h of that unit. On each normal branch, q/h is a constant
N-th root of unity. Lagrange interpolation supplies idempotents
separating the groups with the same value. Thus A' is again a product
of hypersurface branch unions after completion; S2 and codimension-one
agreement with B prove normality off C. The conclusion is therefore

    length(B/A[q])=17,   support(B/A[q]) subset C           (8)

for every possible mate degree 4N under the smooth-integral-conductor
hypothesis. This is not an assertion that the image algebra is etale.


## The marked A4 point cannot lie over a smooth conductor point

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


## Global consequence, including all mate degrees

The preceding components give two conditional exclusions.

**(a) A quintic–octic presentation with Gorenstein normalization and an
integral conductor scheme must have a singular point of that conductor
on C.** Equivalently, it is impossible for Gamma to be smooth at every
point of Gamma intersect C under those hypotheses. Singularities of
Gamma away from C do not discharge this condition.

The [integral-conductor calculation](#the-total-length) and
[branch proof](#why-the-finite-defect-lies-on-c) give a root-adjoining defect of length 17 supported on C,
and it is also supported on Gamma. If Gamma were smooth at these
points, [the marked A4 lemma](#the-marked-a4-point-cannot-lie-over-a-smooth-conductor-point) would keep the A4 point off the conductor. The normalization
is smooth at every remaining contact point. The
[general local formula](square_descent_and_singular_gluing.md#a-general-local-formula-when-the-conductor-downstairs-is-smooth)
then gives local length `2b_p`, where b_p is the full Cartier conductor
contact with c. The entire conductor upstairs has class 2H; hence

    sum b_p=(2H).c=8,
    length(B/A[q])=sum 2b_p=16,                          (10)

contrary to 17.

**(b) A quintic carrier with Gorenstein normalization and smooth
integral conductor scheme cannot have a sole-supported mate of any
degree.** Every hypothetical mate has degree 4N with N>=2. [The all-power extension](#every-mate-power-when-the-full-conductor-is-smooth)
supplies the same length-17 defect and support statement for that N;
the local formula and the marked A4 lemma also hold for every descended power. The
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


## An actual nonintegral-conductor projection witness

The [exact replay](../computations/quintic_component_root_witness.py)
uses `(delta,a,B,G,J)=(1,0,0,-2,1)`. Center rank three and the accepted
ample-degree argument make this an actual finite birational projection
with integral quintic image. The calculation verifies a polynomial
quartic representative P of q by the full source ideal, then obtains

    q=A4(X)+B3(X)h+C3(X)z

modulo that same ideal. Here h,z are the two omitted linear sections.
The actual residual quadratic relations are
`ai+bi h+ci z=0`; at a generic conductor component where a residual
row is nonzero, `ci B3-bi C3` tests the root class. The conductor
annihilator and Nakayama's lemma ensure that its module has a
nonzero fiber there, so the relation rank is exactly one. A nonzero
determinant proves nonvanishing of the actual root class even in the
presence of generic nilpotent structure.

On the open set `X0=1, 2X1-X2+5!=0`, put x=X1,y=X2. The actual
conductor quadric eliminates X3 as

    X3=-(6x^2-13xy+5x+6y^2-10y)/(2x-y+5).

The common curve factor of the other two conductor minors is

    (x-y) * (56x^3-96x^2y+56x^2+42xy^2-32xy-50x
             -y^3-15y^2+65y-25).

These distinct support factors make this an actual nonintegral
conductor. The word cubic describes the residual polynomial in this
affine chart, not the projective degree of its image in P3. Its
irreducibility was not checked. The root class is generically
nonzero on the line and on every irreducible factor of the residual
polynomial in this open set. The computation does not rule out
additional components on the excluded boundary, prove full inverse
support C, or give a family-wide generic-generation result.

This is a negative test for a component-selective-descent witness,
and a verified method for evaluating the actual root class. It is
not an exclusion of all nonintegral conductors. The calculation was
bounded to this witness; no parameter enumeration or uniform
emptiness computation was performed.

It also supplies an actual failure of every root power on this
specified carrier. On the line x=y, the root-direction numerator
is

    54(y+5)^3 P3(y),  P3=8y^3-29y^2+36y-16.

The residual factor restricts there to `(y-1)(y+5)^2`. The line
meets C0 in this chart only at y=0 and y=1, and its chart pole is
y=-5. The exact certificate checks that P3 vanishes at none of
these three values. Thus any root of P3 gives a smooth point of
the actual line conductor outside C0 and away from the residual
component. Smoothness follows from the smooth quadric chart and
the CM conductor's multiplicity-one sole component there.

At that point M is free rank one over the conductor DVR. The root
class vanishes in its fiber but is generically nonzero along the
line, so `B/(A+Aq)` has finite positive local length. The rank-two
conductor algebra and Cayley–Hamilton make A+Aq the algebra A[q],
even without assuming square descent. If any q^N descended, it
would be a unit here. The completed root-of-unity branch argument
would make A[q] Cohen–Macaulay; its finite normalization defect
would then force A[q]=B. This contradicts the positive length.

Consequently **no positive power of q descends on this actual
carrier**, and it has no mate. This conclusion is local at the
displayed points, so it does not require an irreducibility decision
or analysis of the omitted chart boundary. It does not extend to
the whole projection family.

## Exact support, characteristic and review

The projective witness is supported by the retained exact source
[quintic_component_root_witness.py](../computations/quintic_component_root_witness.py),
whose frozen reviewed SHA256 is
`5b84a8b765aa21bade00e3ed325eccf658ada88d801a17871b1df77395b98b87`.
Its independent review checked full-source ideal reductions, root and
module representatives, terminating reductions, actual conductor-module
interpretation, nonzero-direction gcds and every displayed chart boundary;
it also executed that exact source before this consolidation. The later
all-power consequence was separately reconstructed at the actual defect
points. No replay or parameter enumeration is claimed here.

The formula for reduced components includes their intersections through
canonical submodules. It may not be extended by reducing a nonreduced
conductor, by adding an unproved attachment term, or by replacing generic
canonical generation with nonvanishing. The integral square case and the
smooth-conductor all-power extension have different algebra-closure
hypotheses, as their proofs state. Characteristic zero is retained for the
root-of-unity branch and parity arguments. Review reconstructed the
integral length/support formula, reduced-component purity, marked A4
cases and the 17-versus-16 comparison. The actual positive controls in
[square descent and singular gluing](square_descent_and_singular_gluing.md)
show why generic generation, conductor smoothness and normalization
smoothness cannot be silently inferred.

The reduced-conductor rank-three result and its projective application
have their full proof in
[quintic conductor geometry](quintic_conductor_geometry.md#reduced-conductors-force-the-same-cone).
No claim of residual-factor irreducibility, coverage of omitted chart
components or generic generation for a whole projection family is added.

One geometric test must retain the actual conductor ideal: a multiple root
of its restriction to C can also arise from tangency of a smooth conductor.
It is not a test for `Sing(Gamma) intersect C`. The comparison with ordinary
surface singularities likewise keeps those hypotheses separate; the
[local almost-Cartier discussion](../supplements/TORSION_CONSTRUCTIONS_AND_PINCHING_LIMITS.md)
records the precise scope of that different framework.

The separate exact support
[quintic_a4_conductor_first_jet.py](../computations/quintic_a4_conductor_first_jet.py)
computes actual uniform conductor jets on the marked A4 chart. It depends
on [the conductor-quadric identity](../computations/quintic_conductor_cone_identity.py);
its first-jet and quadratic-contact consequences are applied in
[quintic conductor geometry](quintic_conductor_geometry.md) and the
[quintic assembly](quintic_gorenstein_normalizations.md). The script itself
does not establish projection admissibility, smoothness or mate descent.
