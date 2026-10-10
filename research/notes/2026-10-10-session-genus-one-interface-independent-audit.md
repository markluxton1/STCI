# Independent interface audit for the complete genus-one quartic lane

Date: 2026-10-10. Auditor: `oct10_genus_one_interfaces`.
Status: **PROVED HERE / interfaces accepted**, conditional only on the
separately assigned complete exclusions of contact partitions `[4]`,
`[3,1]`, and `[2,2]`. No canonical file is edited. This is an audit of
the hypotheses and quantifiers linking the accepted component results;
it does not substitute agreement between agents for any component proof.

## 1. Precise proposed conclusion and audit outcome

Work over an algebraically closed field of characteristic zero. Let
`X=V(F)` be an integral quartic surface in `P3` containing

    C0=[U^4:U^3V:UV^3:V^4],

and suppose the normalization sectional genus is one. The proposed
conclusion is that there exists no homogeneous polynomial `G` of any
positive degree satisfying `V(F,G)=C0` set-theoretically.

The interfaces audited below do cover **every** such hypothetical mate.
They impose no bound on its degree, no first-normal-order assumption,
no prior reducedness assumption on a conductor, and no choice of a
displayed toric family. Once the complete `[4]`, `[3,1]`, and `[2,2]`
proofs are independently accepted, together with the already accepted
squarefree and `[2,1,1]` exclusions, the proposed conclusion follows.
There is no additional geometric hypothesis needed between these steps.

The conclusion is confined to this sectional-genus-one normalization
lane for integral quartic carriers of the fixed `C0`. It says nothing
by itself about sectional genus two, higher carrier degrees, a general
smooth rational quartic projection center, positive characteristic, or
the universal projective-curve STCI problem.

## 2. Full inverse support must precede the divisor class relation

The [nonrational-normalization independent proof](2026-10-09-session-nonrational-normalization-independent-audit.md)
and its referenced automatic generic-regularity argument apply to an
integral nonnormal quartic containing any smooth rational degree-four
curve. Sectional genus one implies that the quartic is nonnormal: a
normal quartic has a general smooth plane section of genus three.
Thus those accepted hypotheses apply here.

Generic regularity along `C0` supplies exactly one integral curve `c`
above its generic point under the finite normalization `nu:S->X`.
It is finite birational over `C0`, hence isomorphic to it: on each
affine open its coordinate ring is an integral algebra contained in
the common function field, and the downstairs ring is integrally
closed. A second curve over `C0` would also dominate `C0` under the
finite map and give a second generic inverse point, which is impossible.
The strict transform `c#` on a resolution is likewise isomorphic to
`c`; a proper dominant birational map of integral curves is
quasi-finite, hence finite, and the target is normal.

Additional isolated inverse-image points may exist without a mate.
They cannot be silently removed merely because `c->C0` is an
isomorphism. Under the hypothetical mate, however, `nu*G` is a
nonzero section of the invertible sheaf `O_S(bH)`, where
`b=deg(G)` and `H=nu*O_X(1)`. Its zero support is exactly the full
inverse image of `C0`. On the normal integral surface `S`, a nonzero
Cartier section has a pure curve zero scheme; normal surfaces are
Cohen--Macaulay and quotienting by a nonzerodivisor preserves purity
in dimension one. An isolated point away from `c` would therefore
be impossible. Consequently the full support under a mate is `c`.

Write the resulting Weil divisor as `m c`. Intersection with the ample
Cartier divisor `H` gives

    4b=(bH).H=(m c).H=4m,

so `m=b`, including when `G` has high order along the curve. Thus the
actual input to the lattice step is

    div_S(nu*G)=b c,        b c ~ b H.

This establishes the coefficient and removes the isolated-point issue
before any class, double-curve, or power-descent assertion is made.

## 3. Rationality, ADE reduction, and the actual order-two double

The [accepted rationality proof](2026-10-09-session-nonrational-normalization-independent-audit.md)
needs no mate. Its multiplicity bound `0<=m_i<=a` is proved at every
successive blowup, including infinitely near centers. The ruled-surface
identity contradicts the degree-four rational curve whenever the
normalization is nonrational. It applies to this lane and gives a
rational normalization.

The [independent genus-one ADE proof](2026-10-09-session-rational-genus-one-ADE-independent-audit.md)
then applies to its minimal resolution `sigma:M->S`, with
`L=sigma*H`. It proves the actual linear equivalences `K_M~-L` and
`K_S~-H`, and a compatible crepant equality, before invoking the
Du Val criterion. The intermediate effective adjoint divisor is
exceptional and vanishes by negative definiteness; the argument
does not assume rational singularities or Gorensteinness prematurely.
It follows that `M` is weak del Pezzo of degree four and `S` is a
Gorenstein ADE del Pezzo surface with ample anticanonical divisor `H`.

The [independent D5 proof](2026-10-09-session-delpezzo-D5-root-independent-audit.md)
uses the actual class `Z=L-c#` in the free Picard group of rational
`M`. Adjunction and `L.c#=4` give `c#^2=2`, hence `Z^2=-2`.
The pullback of the effective Cartier divisor `b c` gives
`b Z` in the exceptional lattice `R`. The downstairs smoothness
of `c` proves `Z` is not in `R`: otherwise `c~H` would be Cartier,
the surface would be regular along `c`, and the exceptional correction
would be zero. The signed-coordinate saturation proof covers every
exceptional subsystem in the integral `D5` lattice and leaves only
`4A1` and `A3+2A1`. In both survivors `sat(R)/R` has order two.

Thus `b` is even and `2Z` belongs to `R`. Using
`Cl(S)=Pic(M)/R` gives the genuine linear equivalence of Weil divisors

    2c ~ 2H.

In particular `2c` is Cartier, not merely numerically equivalent to
a Cartier divisor. Since it is effective, there is an actual nonzero
section `Q` of `O_S(2H)` with entire divisor exactly `2c`. The quotient
of two sections with that same divisor is a global constant unit on
the normal projective integral surface. Consequently a hypothetical
mate of degree `2n` has pullback equal to a scalar multiple of `Q^n`.
This assertion covers all positive `n`; it does not presume that `Q`
itself descends to `X`.

## 4. Complete anticanonical embedding and the fixed missing coordinate

The primary input was checked directly in the author's hosted
[Dolgachev, Classical Algebraic Geometry](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf),
Theorem 8.3.2(iii), Theorem 8.3.4, and Theorem 8.6.2. For a degree-four
weak del Pezzo resolution, the complete anticanonical map contracts
exactly the zero-degree curves and produces a normal anticanonical
model. This model is projectively normal and is an intersection of
two quadrics in `P4`, including the singular del Pezzo cases.
These are classical input theorems, not results newly proved here.

To identify that model with this particular `S`, note that
`H0(M,L)=H0(S,H)` by `sigma*O_M=O_S`. Its dimension is five; it also
follows from Riemann--Roch and vanishing on `M`. The morphism induced
by `|H|` on `S` is finite because `H` is ample and is birational
because the four original sections already give the birational
normalization map to `X`. Its image is the normal model in the cited
theorem. A finite birational map to a normal target is an isomorphism.
Thus this `S` itself is embedded as the normal integral two-quadric
complete intersection in `P4`; there is no unproved identification
of two possibly different normalizations.

The restriction `H0(S,H)->H0(c,O_P1(4))` has zero kernel. A hyperplane
divisor containing `c` would have degree four, equal to `H.c`, so
ampleness forces its entire divisor to be `c`. Then `c` would be
Cartier. A smooth Cartier curve on a two-dimensional local surface
ring forces the surface ring to be regular there: lift a generator
of the curve maximal ideal and adjoin the one Cartier equation;
these generate the maximal ideal of dimension two. The curve would
avoid all exceptional images, forcing the nonzero `D5` correction
to vanish. This contradiction proves injectivity. Both spaces have
dimension five, so restriction is an isomorphism and `c` is the
complete rational normal quartic in this embedding.

The original four sections restrict to the four literal monomials of
the fixed `C0`. Choose the unique fifth section restricting to
`U^2V^2`. The complete coordinates can therefore be chosen exactly as

    (Y0,Y1,Y2,Y3,Y4)=(U^4,U^3V,U^2V^2,UV^3,V^4) on c,

with the original projection deleting `Y2`. Its center misses `S`,
because the original four sections generate the pullback line bundle
everywhere. No general `PGL2` parameter change is needed. Diagonal
parameter changes and reversal used later preserve this particular
center; arbitrary parameter changes must not be treated as doing so.

## 5. Entire conductor and sign conventions

The [entire-conductor proof](2026-10-09-session-genus-one-entire-conductor.md)
and [independent algebra audit](2026-10-09-session-genus-one-entire-conductor-algebra-independent-audit.md)
have all their conditional geometric hypotheses established by section 4.
One pencil member has nonzero `z^2` coefficient because the center
misses `S`; cancel that coefficient from the other. Its remaining
linear coefficient `L` cannot vanish identically, since otherwise
the image would lie on a nonzero quadric, contradicting its integral
quartic degree. Restriction of a linear form to `c` is injective,
so `L_C` is also nonzero. It has degree four and cannot vanish along
the entire lifted curve.

In the conductor note's convention the equations are

    Q1=z^2-Az-R1,        Q2=Lz+R,
    F=R^2+ALR-R1 L^2.

It proves the injection `A_X->B`, regularity of the sequence `L,R`,
and exact equality `B/A_X=(T/(L,R))(-1)` before taking annihilators.
Thus `(L,R)` is the entire conductor ideal, and the upstairs conductor
is the actual Cartier divisor `L=0`. Its algebra is finite flat of
rank two over the entire plane conic, including two lines and double
lines. Normality plus the two-quadric complete-intersection model
also makes the homogeneous coordinate ring normal; a vertex module
or an omitted finite-length conductor correction is not being assumed
away.

The uniform projection note uses the alternative convention
`Q1=z^2+A'z+R1'`. These are identical after `A'=-A`, `R1'=-R1`.
The singleton condition is `A_C-2z_C=0` in the conductor convention
and `A'_C+2z_C=0` in the uniform convention. This harmless change
must be carried through a literal checker; it is not an additional
geometric assumption.

At each zero of `L_C`, the complete projective projection fiber has
the two roots of this monic equation. No point with all retained
coordinates zero is available, since the center is outside `S`.
The full-support argument from section 2 therefore forces the roots
to coincide. In the six-quadric coefficient convention this says

    rad(L_C) divides D_Q1,

where `D_Q1` is the omitted-coordinate derivative restricted to `c`.
Only support divisibility is used. This condition is valid at smooth
or singular source points and does not invoke the invalid assertion
that every isolated rank-one point must be singular on `S`.

## 6. Cartier double, full ribbon net, and all direction charts

The [independent ribbon-net proof](2026-10-09-session-genus-one-ribbon-net-independent-audit.md)
has precisely the three inputs established above: the normal
two-quadric `S`, embedded smooth rational normal `c`, and `Q` with
entire divisor `2c`. Its local proof applies at every point of `c`,
including every ADE point at which `c` is non-Cartier. The quotient
by `Q` is one-dimensional Cohen--Macaulay, its reduction is a DVR,
and its generic length is two. The injection into the localization
at its unique minimal prime forces the nilideal square to vanish;
the nilideal is then a torsion-free rank-one module over the DVR.
Hence this actual Cartier double is a ribbon globally. This argument
does not replace the symbolic double by the ordinary square of the
curve ideal; that replacement would be false at the displayed ADE
local models.

The complete-intersection resolution gives surjectivity from ambient
quadrics to `H0(S,2H)`. Lift `Q` to a third ambient quadric. It is
independent of the two surface equations and is a nonzerodivisor in
their integral quotient. The double is therefore a `(2,2,2)` complete
intersection of genus five. The ribbon exact sequence then gives
nilideal `O_P1(-6)`.

Its nilideal square-zero property gives `I_c^2` contained in `I_D`.
Its embedding therefore defines the everywhere-surjective quotient
`I_c/I_c^2 -> I_c/I_D`, and `I_c/I_D` is precisely this nilideal.
Conversely `I_D` is the inverse image of the quotient's kernel, so
this quotient determines every actual embedded ribbon here. The direct conormal computation
in the ribbon audit gives `I_c/I_c^2=O_P1(-6)^3` and **every** quotient
as a nonzero direction `eta=(eta0,eta1,eta2)`. The associated net is
exactly

    M(d) eta=0,
    M(d)=[[d0,d1,d2],[d1,d2+d3,d4],[d2,d4,d5]].

The matrix equations have rank three at every nonzero direction.
Since the actual double is a three-quadric complete intersection,
its defining quadrics span this entire kernel net, and the original
surface pencil is a two-plane in it. Thus using this net loses no
double or surface pencil arising from a mate.

The direction condition `eta1^2 != eta0 eta2` is necessary: the
complementary orbit has a cubic surface as the common net base locus,
and every pair of quadrics in it contains that surface. Such a pair
cannot define the assumed integral degree-four surface. The use of
general parameter automorphisms to prove this intrinsic orbit
statement is legitimate because degree, containment, and integrality
are preserved. The subsequent fixed-projection calculations keep
the original center and use only its stabilizing diagonal changes
and reversal. These are distinct uses of the parameter action.

## 7. Squarefree and [2,1,1] coverage

The omitted-coordinate derivative map on the six quadric space is

    D_d=d0 U^4-d1 U^3V-2d3 U^2V^2-d4 UV^3+d5 V^4.

Its only kernel is the quadric `E2`. The matrix `M(E2)` is invertible,
so that kernel misses every net above. Thus the two independent
surface quadrics have independent derivatives. Choose one with
`d3=0`; its derivative is the nonzero quartic `L_C`, whose middle
coefficient vanishes. The other has `d3!=0`, so its derivative has
nonzero middle coefficient. If `L_C` is squarefree, singleton support
would force these two degree-four forms to be proportional. Their
middle coefficients contradict that. This uniformly excludes the
partition `[1,1,1,1]`.

The [complete [2,1,1] proof](2026-10-09-session-ribbon-211-projection-independent-audit.md)
then uses the exact three-dimensional derivative space. The direction
chart `eta0!=0` and its reversal cover every direction except
`(0,1,0)`, which is explicitly treated. On the main chart the three
forms `G0,G1,G2` have common basepoint only when
`eta=(1,u,u^2/4)` with `u!=0`; that basepoint is simple and unique.
Off this locus, every geometric fiber of the derivative map contains
at most two points, as seen from its degree-at-most-two coordinate
ratio and its `G2=0` fiber. Therefore the three distinct zeros of a
`[2,1,1]` quartic cannot all satisfy the singleton requirement.

On the unique basepoint locus, a center-preserving diagonal change
sets `u=1`. Removing its common linear factor gives a basepoint-free
cubic map. Infinity has no finite companion; exact cross products
show its only double fiber is the pair defined by
`t^2+t/4+1/4`. For three distinct singleton-contact zeros, one must
be the basepoint and the other two this double fiber. The zero-center
coefficient condition and divisibility by that quadratic force one
unique candidate `L_C`, and it has a fourth distinct zero outside
that fiber. Thus it fails singleton support. The proof retains the
whole net rather than dropping the derivative-invisible `E2` term,
and covers every endpoint and direction-coordinate boundary.

## 8. Exact remaining obligation and conditional closure

A nonzero binary quartic over the algebraically closed field has one
of the five multiplicity partitions

    [1,1,1,1], [2,1,1], [2,2], [3,1], [4].

The first two are excluded by section 7. The other three are the
explicit scope of the independently assigned remaining-partition
audit. Its required conclusion must cover every derivative-invisible
quadric coefficient and direction boundary, not just an example
pencil or a numerical root. The [owner's completed reconstruction](2026-10-09-session-ribbon-repeated-partitions-complete.md)
states such coverage, and the root's separate `[4]` and bounded
`[2,2]` arguments support two parts; their mathematical acceptance
is being handled outside the present interface task.

If that remaining coverage is accepted, every hypothetical mate has
been contradicted: its normalization and Cartier double necessarily
enter the audited fixed-center net, its nonzero `L_C` necessarily
belongs to one of the five partitions, and every partition is
excluded. No assumption that the displayed toric families exhaust
marked curve/projection pairs is needed. No genus-one conductor
smoothness hypothesis is left outstanding: the entire conductor
formula retains all schemes until a particular surviving pencil
itself forces a smooth conic, if that is used by its final proof.

At this note's writing the **interfaces are accepted**, while
promotion of the entire genus-one no-mate theorem remains conditional
on the separately audited remaining-partition coverage. This is a
logical dependency boundary, not an identified gap in the application
of the accepted rationality, ADE, D5, anticanonical, conductor, ribbon,
squarefree, or `[2,1,1]` results.

## 9. Evidence scope

This audit read the cited repository proofs in full and checked the
primary anticanonical model statements directly. The exact conormal
and derivative formulas, Hilbert-series identities, and local ribbon
arguments are reproduced or traced above; no new black-box finite
enumeration is used to establish this logical interface result.
The previous execution and record-integrity seals retain their
original scopes and do not count this later note as a rerun.

A delegated read-only microaudit by `ribbon_interface_microaudit`
independently accepted the local ribbon argument, the kernel-net
exhaustiveness, the intrinsic off-conic obstruction, and every `[2,1,1]`
direction/basepoint chart. Its separate exact checks used standard-library
rational polynomial arithmetic and confirmed the displayed kernels,
derivatives, both cross products, elimination, unique double fiber,
remainder matrix, rank witness, candidate kernel, final factorization,
and distinct extra image. Its mathematical finding agrees with the
arguments above and identifies no additional hypothesis.

It did identify an evidence-attribution error in the older `[2,1,1]`
note, section 5. That note says the current
`verify_session_genus_one_projection_2026_10_09.py` checks the divided
cubic, cross products, remainder matrix and candidate factorization.
Reading the entire current source shows that it checks the uniform
projection and an `A3+2A1` displayed family instead. The separate
`derive_session_rnc_ribbon_net_2026_10_09.py` contains the net basis,
derivatives and common-basepoint gcd, but also lacks the full divided
cubic calculation. Thus their existing passing executions must not
be attributed to those missing checks. This is a provenance correction,
not a failure of the written `[2,1,1]` proof.

The new independent [Macaulay2 companion](../computations/verify_session_genus_one_211_interfaces_2026_10_10.m2)
supplies 42 exact identities over `QQ`, covering the rank-three net
minors, derivative injectivity, all three actual basis kernels and
derivatives, simple basepoint and its division, two cross products,
third cross product on the unique candidate, exact remainder matrix,
rank-two witness and kernel, the four-root factorization, and the
extra distinct derivative image. Its observed terminal execution
returned exit zero and `PASS` in `0.521622041` seconds on 2026-10-10.
The first scaffold run was terminal with exit one because `net` is
a protected Macaulay2 global name; renaming it `netCoefficients`
resolved that implementation error without altering any identity.
Both attempts and the actual passing source hash are recorded in
[the execution record](../validation/2026-10-10-genus-one-interfaces/execution-record.json).

The formerly used temporary Python environment was rechecked and
currently lacks SymPy; the desktop-bundled Python does as well. Those
observations are retained in the execution record. They do not turn
the historical Python passes into current passes, and the new
companion uses the currently verified Macaulay2 `1.26.06` runtime.
