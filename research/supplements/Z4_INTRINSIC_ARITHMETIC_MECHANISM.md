# z4 intrinsic arithmetic mechanism

## Proof-dependency map: intrinsic mechanism and its failure shields

Start with the [general synthesis](#2026-10-21-z4-general-mechanism-synthesis), then compare the [quadratic-gluing calculation](#2026-10-21-z4-quadratic-gluing-comparison) with its [independent audit](#2026-10-21-z4-general-mechanism-independent-audit). The [divided-power mechanism](#2026-10-21-z4-intrinsic-divided-power-mechanism) and [persistent arithmetic obstruction](#2026-10-21-z4-persistent-arithmetic-obstruction) analyze what remains after coordinate changes and reductions. The [characteristic-zero consequences](#2026-10-21-z4-characteristic-zero-stci-consequences) retain their stated conditional status.

The underlying [explicit Z4 quartic obstruction](Z4_LIFTING_AND_DEFORMATION.md#2026-10-20-z4-quartic-obstruction) and [independent lifting audit](Z4_LIFTING_AND_DEFORMATION.md#2026-10-20-z4-lift-independent-audit) are narrower: they concern a prescribed model. The [coordinate-invariance counterexample](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-z4-coordinate-invariance-counterexamplemd) is an essential failure shield against interpreting an arbitrary Laurent representative as an intrinsic class. The [ribbon/triple audit](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-21-intrinsic-ribbon-triple-independent-auditmd) checks a distinct gluing issue.

**Status separation:** an explicit obstruction class for one family, an invariant interpretation under additional choices, and a universal characteristic-zero STCI exclusion are three different claims. No such universal conclusion is promoted here.

---


Permanent mathematical dossier preserving complete proofs, computations, exact characteristic hypotheses, obstruction classes, counterexamples and conditional implications. No new theorem promotion is implied.

---

## 2026-10-21-z4-general-mechanism-synthesis

# Z4 arithmetic mechanism and characteristic-zero STCI: synthesis

Date: 2026-10-21. Status: **new research evidence, independently reviewed in
the companion audit; unpromoted**. No canonical theorem record is modified.
Base: `research/z4-arithmetic-obstruction-consolidated-2026-10-21`, fetched
at `c1af2e466c4b2251622ee70116613a3b2afb1391`.

The two investigations reached definite outcomes: a defect-sensitive
necessary condition for generically curvilinear STCI presentations, an
embedded obstruction hierarchy, and counterexamples to the unrestricted
bridges suggested by the arithmetic analogy. They do not exclude arbitrary
characteristic-zero STCI presentations of the fixed rational quartic C0.

## 1. New characteristic-zero restriction

Let C be a smooth curve regularly embedded in a smooth threefold, with
ideal I, and let J define a supported complete intersection whose generic
transverse algebra is curvilinear of length m≥3. Saturate its first-normal
image as

    (J+I²)/I² = M(−D) ⊂ M ⊂ E=I/I²,
    q:E→L=E/M,

where D is effective and M,L are line bundles. Put H=M∨⊗L².
The [characteristic-zero report](#2026-10-21-z4-characteristic-zero-stci-consequences)
proves the necessary condition

    image of o_X(q) in H¹(C,H(D)) is zero.               (A)

The proof uses the image of J inside the canonical extension module:
it projects isomorphically to M(−D) and therefore splits the pulled-back
extension. It does not require an everywhere primitive triple inside the
complete intersection. Equivalently the obstruction must be supplied by
principal parts supported on the *actual* first-normal defect divisor.

For the distinguished marked quotient of C0 with L=O(−6), M=O(−8),
and o=−6[u⁻²], condition (A) implies:

- deg D≥2;
- if deg D=2, a defining binary quadratic for D has zero st coefficient
  in the fixed marking;
- if deg D≥3, this first obstruction alone imposes no further condition.

These statements include nonreduced effective divisors. They concern an
actual pair inducing this q. Other quotients of the same degree can have
zero obstruction: the audited polynomial family has the surjective example
a=h=0, b=d=1. More generally, for the accepted conormal E=O(−7)²,
L=O(ε−7) gives H=O(3ε−7), so the first obstruction group vanishes
for ε≥2. There is no unrestricted new exclusion of surface degrees.

The structural limitation is also proved. A supported lci may be
curvilinear generically and fail to contain any globally primitive triple.
The family J=(x²,y²+t x), free of rank four over k[t], has generic algebra
k(t)[y]/(y⁴) and special algebra k[x,y]/(x²,y²). The latter has no
curvilinear length-three quotient. An ambient triple extending a ribbon
can exist while failing to be contained in J. Thus vanishing of o_X(q)
is weaker than compatibility with a specified complete intersection.

## 2. Does divided Frobenius produce the intrinsic class?

No unconditional identification is proved. The
[intrinsic arithmetic report](#2026-10-21-z4-intrinsic-divided-power-mechanism)
does recover the accepted full class −6[u⁻²] and the divided variation

    λ(α,β,γ)=γ[u⁻¹]+[u⁻²]+α[u⁻³],
    D(α,β,γ)=γ[u⁻¹]+α[u⁻³].

This uses the full embedded Yoneda extension and the previously audited
Laurent polynomials. It does not isolate a normal-coordinate summand or
derive the full class from a binomial coefficient. The nonzero image in
coker D is intrinsic for the specified marked integral problem.

There is a genuine conditional comparison, with an explicit source and
target. If two quadratic neighborhoods are locally isomorphic over the
same marked first neighborhood A₁ and B=Sym²E, their difference is a
class β in H¹(Der_S(A₁,B)). The canonical sheaf map

    ρ_q:Der_S(A₁,Sym²E)→Hom(M,L²)

restricts a derivation to M and projects by Sym²q. It carries β to
the difference of the Yoneda obstruction classes. The
[quadratic-gluing comparison](#2026-10-21-z4-quadratic-gluing-comparison)
proves the statement and its coordinate functoriality. The missing arithmetic
bridge is a natural derivation-valued gluing class carrying the full normal
and moving-base data. A divided-power polynomial does not furnish it.

## 3. Strongest general characteristic-p conclusion

For every fixed embedded primitive n-fold J_n, n≥2, with inherited q,
there is a canonical exact sequence

    0→L^n→J_n/(I J_n+I^(n+1))→M→0.                    (B)

Its splittings classify compatible primitive (n+1)-fold embedded ideals.
Thus the obstruction is in H¹(M∨⊗L^n), and when it vanishes the choices
form a torsor under H⁰(M∨⊗L^n). This works in arbitrary characteristic
under the regular-immersion and primitive-stage hypotheses. The fixed
stage J_n and the ambient neighborhood are essential data.

The universal p^r binomial arithmetic predicts the least normal order of
its own cross-effect, p^(r−1) when one argument is a unit and the other
is normal. It does not predict the first nonzero class in hierarchy (B).
Explicit triangular gluing gives the same conormal bundle and the same
lower primitive stages but an arbitrary nonzero next-stage class; the split
vector-bundle model admits every stage even though the arithmetic polynomial
is nonzero. Varying an integral gluing coefficient πc gives identical full
special ambient fibers but different divided obstruction classes.

The relative persistent-cokernel theorem is correct when the obstruction
module is locally free, reduction and cohomology comparisons apply, and the
leading section on the marked lift torsor is affine-linear with difference
map D. At higher divided orders, affine linearity is additional content:
the example o(q)=4+q², q=2t gives o/4=1+t² modulo two, with zero ordinary
differential and a cancelling lift. A cokernel of the ordinary differential
cannot replace the nonlinear obstruction image in general.

## 4. Specialization boundary and status

Support-preserving spreading is possible after localization, using finite
ideal containments I^N⊂J⊂I and generic flatness. This produces an open set
of good specializations; it need not include residue characteristic two.
It forces neither the marked quotient nor the prescribed Z4 integral
deformation class. For C0, the accepted lower-carrier exclusions and Bézout
give m=de/4≥9, whereas the prescribed Z4 has m=4. Flat direct specialization
to that whole quadruple is therefore incompatible even with the degree.
Extracting a separate quadruple would be a further theorem.

| Conclusion | Status and boundary |
| --- | --- |
| Defect-twisted necessary condition (A) | Proved here; independently reconstructed; generic curvilinear branch, m≥3 |
| Distinguished q0 defect bound | Proved corollary, with fixed marking; no classification of all quotients |
| Generic curvilinear lci need not contain a primitive triple | Explicit counterexample; no assertion that it occurs on C0 |
| Primitive-stage obstruction hierarchy (B) | Proved here and independently reconstructed; fixed embedded primitive stage |
| Quadratic-gluing comparison | Proved under explicit marked local-isomorphism hypotheses |
| Relative divided obstruction in coker D | Conditional general theorem; Z4 instance imported from the corrected independent audit |
| Conormal/arithmetic data alone determine the obstruction | False, by explicit smooth ambient gluing examples |
| Natural divided-Frobenius identification for the full Z4 class | Open; no nonexistence theorem for every richer possible comparison is claimed |
| Unrestricted characteristic-zero STCI for C0 | Open |

## 5. Single next mathematical step

Test (A) against the *actual global first-normal symbol image* of STCI
surface pairs, beginning with the ε=1 quotient locus and its low-degree
defect divisors. Construct the incidence requiring that the two homogeneous
surface symbols have common saturated line M, actual common divisor D,
and o(q) annihilate H⁰(ω_C⊗H⁻¹(−D)). The symbols must come from global
k-coefficient forms, not arbitrary k(C)-linear choices. Use already accepted
carrier and defect budgets as premises; do not reopen excluded quartics.

The stopping rule is exact emptiness for a stated finite locus, or an
explicit surviving pair of symbols together with its first unresolved lift
condition. This is the next direct use of the new STCI condition. A survivor
does not constitute actual surfaces with exhausted support; cases with both
generic normal orders at least two remain in their separate accepted
blow-up/normal-filtration lanes.

## Verification and review

The two new scripts, the independent audit, and their exact scope are linked
from the reports. They check polynomial/Laurent arithmetic, coordinate
transformations, defect cancellation, local counterexample algebras, and
small-prime illustrations. The structural arguments above are proofs, not
inferences from those finite tests. The inherited carrier exclusions and
accepted full ambient cocycle were used as premises, not re-proved.

The companion [independent audit](#2026-10-21-z4-general-mechanism-independent-audit)
records reconstruction of the new implications and the cross-investigation
scope checks. All new results remain unpromoted research evidence.


---

## 2026-10-21-z4-quadratic-gluing-comparison

# Comparing quadratic neighborhoods with the embedded Yoneda obstruction

Date: 2026-10-21. Status: **proved here under explicit comparison hypotheses;
independently reconstructed by the structural audit worker; unpromoted**.
This is evidence for Investigation B, not a theorem about unrestricted STCI.

## Statement and source

Work over a base scheme S. Let C have two marked quadratic ambient
neighborhoods A₂ and A₂′ with a common first neighborhood A₁, common
conormal E, and identified square-zero kernels

    0 → B → A₂ → A₁ → 0,       B = Sym²(E),
    0 → B → A₂′ → A₁ → 0.

Here A₂ denotes O_X/I³, A₁ denotes O_X/I², and the action on B
factors through O_C. The neighborhoods come from regular codimension-two
immersions, so multiplication identifies I²/I³ with Sym²(E).
Fix q:E→L, a line quotient with line kernel M.

**Comparison hypothesis:** A₂ and A₂′ are locally isomorphic as
S-algebras by isomorphisms inducing the specified identity on A₁ and B.
This is a hypothesis, not a consequence asserted for arbitrary regular
immersions. All classes below use these markings.

Define the sheaf of O_C-modules

    D₂ = Der_S(A₁,B).

There is a canonical O_C-linear map

    ρ_q:D₂ → Hom(M,L²),
    ρ_q(δ) = (Sym²(q)) ∘ (δ restricted to M).

The local isomorphisms define a difference class
β(A₂′,A₂) in H¹(C,D₂). With the overlap orientation specified in the
proof, the canonical embedded obstruction classes satisfy

    o_(A₂′)(q) − o_(A₂)(q) = H¹(ρ_q)(β(A₂′,A₂)).       (1)

Thus a genuine arithmetic *gluing-defect cocycle*, if independently
constructed in D₂ with the stated compatibility, has a natural comparison
to the Yoneda obstruction. A binomial cross-effect by itself does not
supply β or a map into D₂.

The general square-zero derivation principle is described in the
[Stacks Project, Lemma 91.2.1](https://stacks.math.columbia.edu/tag/08S3).
Formula (1) is proved directly below; it is not quoted from that source.
The target obstruction is the corrected canonical extension of the
[independent intrinsic audit](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-21-intrinsic-ribbon-triple-independent-auditmd).

## Proof

An automorphism f of A₂ inducing the identity on A₁ and B has
f−id valued in B. Since this difference vanishes on B, it factors uniquely as
δ:A₁→B. Multiplicativity and B²=0 give the Leibniz identity.
Conversely, writing π:A₂→A₁ for the projection, id+δπ is an
automorphism with inverse id−δπ. Composition adds derivations.
This identifies the automorphism sheaf with the additive sheaf D₂.

For e,e′ in the square-zero ideal E of A₁,

    δ(ee′) = e δ(e′) + e′ δ(e) = 0.

For a local section a of O_C, the identity
δ(ae)=aδ(e)+eδ(a)=aδ(e) shows that δ restricted to E is
O_C-linear, independently of a choice of lift of a. Restricting to M
and projecting B to L² defines ρ_q canonically. The same identity
shows this is a morphism of O_C-modules.

Choose local isomorphisms φ_i:A₂′→A₂ on an affine trivializing cover.
Define δ_ij by

    φ_i φ_j⁻¹ = 1 + δ_ij.

The δ_ij are a Čech cocycle since automorphisms add. Replacing φ_i
by (1+ε_i)φ_i changes δ_ij by ε_i−ε_j, so their cohomology
class is independent of the local isomorphisms. We take this orientation
as the definition of β(A₂′,A₂).

Each φ_i induces an isomorphism of the canonical module extensions

    Q = J₂/(I J₂+I³),       0→L²→Q→M→0,

and its counterpart Q′, inducing identity on the end terms. On Q the
automorphism 1+δ_ij acts by adding ρ_q(δ_ij) to a lift of M:
δ kills quadratic terms, and the quotient of B in Q is precisely L².
Choose local splittings s_i of Q→M and transport to Q′ by
t_i=φ_i⁻¹s_i. Then, transporting differences back via φ_i,

    t_j−t_i  corresponds to  (s_j−s_i)+ρ_q(δ_ij).

The two splitting cocycles therefore differ by ρ_q(δ_ij).
The corrected intrinsic audit identifies those splitting cocycles with
the Yoneda classes. This proves (1).

## Coordinate changes, base movement, and arithmetic scope

No normal-coordinate decomposition was used. Isomorphisms of the full
marked data transport A₁, B, D₂, ρ_q, and (1). Derivations in D₂ may
move base functions into B. Restricting them to chosen normal variables
without carrying the full A₁ structure would lose this functoriality.
The comparison fixes A₁; a coordinate change with a first-order base
displacement must first be transported to the common marked A₁.

Over a DVR with uniformizer π, if the difference cocycle is divisible
by π, its leading reduction can be sent through the reduction of ρ_q,
provided the relevant sheaves, cohomology modules, and base-change maps
have the flatness/exactness needed for division. It then computes the
leading *difference* of embedded obstruction classes. A claim about a
persistent cokernel further needs a specified quotient-lift torsor and
its divided variation map D. These conditions are not consequences of
the arithmetic polynomial Δ_(p^r).

This comparison is useful because it names the exact missing datum:
a coordinate-equivariant arithmetic class in the sheaf of quadratic
gluing derivations, rather than an isolated coefficient of a transition.
It does not identify divided Frobenius with that class, and it imposes
no additional condition on arbitrary characteristic-zero STCI pairs.

## Independent reconstruction and limits

The structural audit worker independently reconstructed the automorphism
identification, O_C-linearity of restriction, and the Čech comparison.
It explicitly required the local-isomorphism hypothesis and a consistent
overlap orientation. Its audit is recorded in the companion
[general-mechanism audit](#2026-10-21-z4-general-mechanism-independent-audit).
All new claims remain research evidence; no canonical result is promoted.


---

## 2026-10-21-z4-general-mechanism-independent-audit

# Independent audit: general mechanism and characteristic-zero consequences

Date: 2026-10-21. Reviewer: independent structural-audit worker in the
current research task. Status: **independently reconstructed research
claims; unpromoted**. This review does not amend a canonical theorem,
reopen an accepted carrier exclusion, or settle characteristic-zero STCI.

## Scope, dependencies, and method

The review follows `research/INDEX.md` and `research/AUTHORITY.md`.
Its accepted inputs are the exact order-one scope in
[`results/order_one.md`](../results/order_one.md), the prescribed
unramified arithmetic nonlifting theorem
[R0012](../results/prescribed_z4_arithmetic_nonlifting.md), and the
corrected canonical module extension in the
[intrinsic independent audit](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-21-intrinsic-ribbon-triple-independent-auditmd).
The general intrinsic construction is reviewed evidence, not a promoted
canonical result. The previously audited quartic Laurent polynomial is
an imported input; this review does not reconstruct its rational ambient
chart expansion.

The new targets are the
[characteristic-zero report](#2026-10-21-z4-characteristic-zero-stci-consequences),
the [arithmetic-mechanism report](#2026-10-21-z4-intrinsic-divided-power-mechanism),
and the [quadratic-gluing comparison](#2026-10-21-z4-quadratic-gluing-comparison).
The arguments below were reconstructed directly, with particular attention
to generic versus everywhere assertions, compatibility with an existing
complete intersection, and the scope of arithmetic nonvanishing.

## 1. Generic primitiveness does not force a primitive triple

Work over a characteristic-zero field, and use projective coordinates
`[t:x:y:w]`. The homogeneous ideal

    J = (x², y²+t x)

is a regular sequence and has radical `(x,y)`. Thus its projective zero
scheme is a genuine `(2,2)` complete intersection with reduced support the
smooth line `C=V(x,y)`. The two equations may both be chosen integral:

    F=x²+y²+t x,       G=x²+2y²+2t x.

They generate `J`, and each is a rank-three irreducible quadric in
characteristic zero. Both are singular at `[0:0:0:1]`.

On `w=1`, the quotient is obtained by adjoining `x` with the monic
relation `x²=0`, then `y` with the monic relation `y²+t x=0`. It is free
of rank four over `k[t]`, with basis `1,x,y,xy`. After inverting `t`,

    J=(x+y²/t, y⁴),

so the generic transverse algebra is curvilinear of length four and
one equation has generic normal order one. At `t=0` the transverse algebra
is instead

    k[x,y]/(x²,y²).

This algebra has no curvilinear length-three quotient. Indeed, in any
surjection to `k[z]/(z³)`, write

    x=a z+b z²,       y=c z+d z².

The square relations imply `a²=c²=0`, hence `a=c=0`; the images cannot
generate the class of `z`. A primitive triple embedded along `C` inside
the complete intersection would, on completing at the displayed point,
be finite flat of rank three over `k[[t]]`, with special quotient
`k[z]/(z³)`. This is impossible. This proves a projective counterexample,
not merely a generic-point algebra example.

There is an additional distinction. The ribbon `V(x,y²)` lies inside
this complete intersection. Its ambient primitive triple `V(x,y³)`
exists, since for the associated quotient on the line

    E=O(-1)⊕O(-1),   M=L=O(-1),
    H¹(Hom(M,L²))=H¹(O(-1))=0.

But `V(x,y³)` is not contained in `V(J)`: the image of `y²+t x` is the
nonzero class `y²`. Thus even vanishing of the ambient ribbon-to-triple
obstruction does not assert compatibility with a prescribed multiple
scheme. The generic compatible equation `x+y²/t` has a pole at the
nonprimitive point.

**Verdict:** the proposed general implication fails even for projective
complete intersections with smooth support and integral defining surfaces.
The example concerns a line, so it does not exclude a separate theorem
using special rational-quartic hypotheses. No such scope bridge has been
proved here.

## 2. The defect-twisted necessary vanishing is valid

Let `C` be a smooth integral curve regularly embedded in codimension two,
with ideal `I` and conormal `E=I/I²`. Let `J⊂I` define a multiple scheme
with generic transverse algebra curvilinear of length `m≥3`. Put

    N=image(J→E),    M=saturation of N in E,
    N=M(-D),        q:E→L=E/M,

where `D` is effective and `M,L` are line bundles. Rank-one saturation
is a subbundle because the base is a smooth curve. Let

    Q=J₂/(I J₂+I³),       0→L²→Q→M→0

be the canonical extension for `q`. Since `J⊂J₂` and `I` annihilates
`Q`, its image `P=image(J→Q)` is an `O_C`-module and maps onto `N`.
At the generic point, choose adapted parameters with
`J=(f,y^m)`. Modulo the defining ideal of `Q`, the image of `J` is a
single graph line projecting isomorphically to `M`: the second generator
has order at least three. Therefore the kernel of `P→N`, a subsheaf
of the line bundle `L²`, is generically zero. It is consequently zero
everywhere. This argument does not discard a possible torsion module:
a subsheaf of `L²` is torsion-free.

Hence `P≅N`, and its inclusion in `Q` canonically splits the extension
pulled back along `N→M`. Equivalently,

    o_X(q) maps to zero in H¹(M^∨⊗L²(D)).

The hypothesis `m≥3` is necessary for this proof: for `m=2`, the
second generic generator has nonzero image in `L²`. For `D=0`, the
conclusion is ambient primitive-triple existence. For general `D`, it is
a bounded-pole or principal-parts condition, and it does not assert a
primitive triple inside the given scheme.

This is a direct characteristic-zero necessary condition once the
first-normal direction and its defect divisor have been obtained from an
actual pair. It is not a restriction on all arbitrary line quotients,
nor does it cover the entirely-thick branch.

### The fixed quartic quotient

For the distinguished quotient `L=O(-6)`, `M=O(-8)` on the prescribed
rational quartic, the imported class is `-6[u^-2]` in `H¹(O(-4))`.
In characteristic zero, Serre duality identifies it with a nonzero
multiple of the middle-coefficient functional

    A s²+B st+C t² ↦ B.

Its image in `H¹(O(-4)(D))` vanishes precisely when this functional
annihilates `H⁰(O(2)(-D))`.

For `deg D=1`, the latter space is the kernel of evaluation at a point
`[a:b]`. Evaluation has coefficient vector `[a²:ab:b²]`, which cannot
be proportional to `[0:1:0]`. Thus no divisor of degree zero or one
kills the class. For `deg D=2`, if the defining quadratic is
`Q_D=A s²+B st+C t²`, vanishing holds exactly when `B=0`; this
includes nonreduced divisors. For `deg D≥3`, the target cohomology group
is zero. These are exact tests for killing this class, and only
necessary conditions for existence of a complete-intersection pair.

## 3. The compatible higher-stage extension is correct

Fix an actual embedded primitive stage `J_n`, `n≥2`, locally
`J_n=(z,y^n)` with `I=(z,y)`. Its first quotient gives the fixed
`q:E→L` with line kernel `M`. Set

    K_n=I J_n+I^(n+1).

Locally `K_n=(z²,zy,y^(n+1))`. Consequently `J_n/K_n` is annihilated
by `I`, its image in `E` is `M`, and its kernel is the multiplication
image of `I^n`. That image is canonically

    Sym^n(E)/(M Sym^(n-1)(E)) = L^n.

There is therefore an exact sequence of genuine `O_C`-modules

    0→L^n→J_n/K_n→M→0.

A splitting has inverse-image ideal locally
`(z-a y^n,y^(n+1))`. This is an embedded primitive stage `J_(n+1)`
with `J_n=J_(n+1)+I^n`. Conversely this compatibility forces
`K_n⊂J_(n+1)`, since

    I J_n=I J_(n+1)+I^(n+1).

The resulting quotient of `J_(n+1)` maps isomorphically to `M`, giving
the inverse construction. The obstruction is in `H¹(Hom(M,L^n))`,
and the set of compatible extensions, if nonempty, is a torsor under
`H⁰(Hom(M,L^n))`.

**Verdict:** valid for a fixed embedded primitive stage. It does not
produce that stage from generic curvilinearity, prove an infinite tower,
or make a higher obstruction independent of previous choices. Its data
include the next ambient neighborhood and the actual `J_n`.

## 4. Quadratic-gluing comparison, including its sign

Use the exact local-isomorphism and marking hypotheses of the
[comparison supplement](#2026-10-21-z4-quadratic-gluing-comparison).
Write `A₁=O_X/I²`, `B=Sym²E`, and
`D₂=Der_S(A₁,B)`, with `B` acted on through `O_C`.

An automorphism of `A₂` inducing identity on `A₁` and `B` is uniquely
`id+δπ`, where `π:A₂→A₁` and `δ∈D₂`. The Leibniz identity follows
from multiplicativity; products of two differences vanish in `B`.
The inverse is `id-δπ`, and composition adds derivations. For
`e∈E` and any lift `a` of a base function,

    δ(ae)=aδ(e)+eδ(a)=aδ(e).

Thus `δ|E` is `O_C`-linear independently of the lift. It follows that

    ρ_q(δ)=Sym²(q)∘δ|M

is a canonical `O_C`-linear morphism to `Hom(M,L²)`.

Choose local marked isomorphisms `φ_i:A₂′→A₂` and define
`φ_i φ_j^-1=id+δ_ij`. Composition proves the cocycle identity.
If `s_i` split the unprimed canonical extension, put
`t_i=φ_i^-1 s_i`. Applying `φ_i` to their difference gives

    φ_i(t_j-t_i)=(s_j-s_i)+ρ_q(δ_ij).

The difference of the two Yoneda cocycles has the **plus** sign in the
supplement with this overlap orientation. Changing local isomorphisms
changes `δ_ij` by a coboundary. Therefore

    o_(A₂′)(q)-o_(A₂)(q)=H¹(ρ_q)(β(A₂′,A₂)).

The proof includes derivations of base functions. It does not choose a
retraction to the reduced curve or isolate a normal-coordinate summand.
A coordinate change that moves base functions at first normal order
must first transport the marking of `A₁`. Local isomorphism over the
marked `A₁` is essential; arbitrary regular immersions are not asserted
to meet it.

**Verdict:** the comparison theorem is correct under its stated
hypotheses. It concerns a genuine derivation-valued gluing class.
No argument identifies a divided-power polynomial with that class.

## 5. Arithmetic boundaries and independent calculations

The supplied divided-power congruences are arithmetic identities.
Their normal order depends on how their inputs meet the ideal of `C`:
one tangential unit and one normal input can have leading order
`p^(r-1)`, while two normal inputs give total normal order `p^r`.
Neither statement implies that an embedded obstruction is nonzero.

Split normal bundles with their standard zero sections have all
primitive stages despite nonzero universal divided cross-effects.
Conversely, triangular quadratic or higher transition terms can realize
nonzero obstruction classes with the same split conormal and the same
lower marked neighborhood. These examples establish insufficiency of
the lower data and failure of a universal nonvanishing implication.
They do not prove nonexistence of every possible natural comparison
with richer geometric input.

The independent reviewer ran

    /private/tmp/stci-z4-env/bin/python research/computations/verify_z4_general_mechanism_2026_10_21.py

and obtained all six `PASS` groups. The runtime supplies SymPy 1.14.0;
the system Python and the bundled desktop Python do not have SymPy.
The checks cover the imported Laurent polynomial's leading reduction,
adapted quadratic changes including base movement, integral
coboundaries, finite samples of nonsplit higher gluing, low-prime
binomial identities, and the higher divided-order nonlinear example.
These are reproducible checks of the new interfaces. They do not
recompute the original quartic ambient Laurent cocycle or prove the
general structural theorems by finite sampling.

In particular, at higher divided order a tangent cokernel can miss
nonlinear cancellation. The elementary family `o(q)=4+q²`, `q=2t`,
has divided reduction `1+t²` in characteristic two, with zero
differential but a zero at `t=1`. A persistent-cokernel theorem at a
higher stage therefore needs a proved affine-linear law, not merely a
computed differential.

## Overall assessment

The defect-twisted vanishing is a valid necessary condition for actual
generic order-one pairs. The projective degeneration is a valid
counterexample to a general forced-primitive-stage argument. The fixed
stage hierarchy and marked quadratic comparison are valid with their
explicit hypotheses. The arithmetic identities do not furnish the
missing geometric gluing class. All new conclusions remain unpromoted
research evidence; the unrestricted characteristic-zero rational-quartic
STCI problem remains open.


---

## 2026-10-21-z4-intrinsic-divided-power-mechanism

# Embedded primitive towers, divided leading obstructions, and the arithmetic comparison gap

Date: 2026-10-21. Investigation B. **New results below are proved research
proposals, submitted for independent audit, and unpromoted.**
No canonical result record is changed. The claim concerns a fixed regular
codimension-two embedding and marked conormal quotient; it does not establish
an obstruction to arbitrary characteristic-zero STCI presentations.

The definite outcomes are an embedded primitive-stage obstruction hierarchy,
a precise relative leading-class theorem, a natural comparison from quadratic
gluing derivations, and smooth algebraic counterexamples to recovery from
conormal or special-fiber data alone. These results do **not** identify the
quartic obstruction with divided Frobenius.

## 1. Scope and inherited premises

The motivating quartic is

\[
C\subset\mathbf P^3,\qquad
[s:t]\longmapsto[s^4:s^3t:st^3:t^4].
\]

For its specified characteristic-two quadruple problem, the marked integral
ambient is over \(R=\mathbf Z_{(2)}\) or \(\mathbf Z_2\). The prescribed
special quotient has \(L=\mathcal O(-6)\), \(M=\mathcal O(-8)\).
The following are inherited premises, not proofs rerun here:

* The [corrected intrinsic audit](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-21-intrinsic-ribbon-triple-independent-auditmd)
  gives the canonical extension and identifies its splitting torsor with
  embedded primitive triples in the fixed ambient.
* The [persistent relative audit](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-z4-persistent-independent-auditmd)
  supplies the relative Ext construction, the full integral Laurent
  coefficient polynomials, and the exhaustiveness of the marked quotient
  family. Its class is relative to the fixed marked integral problem.
* The [coordinate-summand counterexample](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-z4-coordinate-invariance-counterexamplemd)
  invalidates assigning intrinsic meaning to one quadratic transition
  summand. The full extension remains intrinsic.
* The [arithmetic precursor](Z4_LIFTING_AND_DEFORMATION.md#2026-10-21-z4-divided-frobenius-origin) and
  [Investigation 4](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-21-investigation-4-general-pr-mechanism-preliminarymd)
  supply the binomial valuation and divided cross-effect identities.

The [consolidation dossier](../Z4_ARITHMETIC_CONSOLIDATION_2026-10-21.md)
is navigation, not additional theorem authority. The
[literature assessment](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-z4-intrinsic-obstruction-literaturemd)
does not identify a verified divided-Frobenius map to this obstruction.
No novelty claim about general deformation theory is made here.

For a regular immersion \(C\hookrightarrow X\), let \(I\) be its ideal,
\(E=I/I^2\), and fix \(q:E\twoheadrightarrow L\) with invertible kernel
\(M\). Put \(J_2=\ker(I\to L)\). The canonical extension is

\[
0\longrightarrow L^2\longrightarrow
Q_2:=J_2/(IJ_2+I^3)\longrightarrow M\longrightarrow0.       \tag{1}
\]

Its Yoneda class is
\(o_X(q)\in H^1(C,M^\vee L^2)\); it vanishes exactly when this fixed
embedded ribbon admits a primitive triple. In particular, \(I/I^3\) must
not be substituted for \(Q_2\) as an allegedly canonical
\(\mathcal O_C\)-module. Multiplication by \(I\) annihilates \(Q_2\),
which makes (1) a literal module extension.

## 2. A primitive-stage hierarchy

**Proved proposal B1.** Let \(C\hookrightarrow X\) be a regular immersion
of codimension two, in any characteristic. Fix an embedded primitive
\(n\)-fold structure \(Z_n\), \(n\ge2\), with ideal \(J_n\), having
local form

\[
I=(z,y),\qquad J_n=(z,y^n).
\]

Its ribbon quotient has conormal line \(L\), with kernel \(M\subset E\).
There is a canonical exact sequence

\[
0\longrightarrow L^n\longrightarrow
Q_n:=J_n/(IJ_n+I^{n+1})\longrightarrow M\longrightarrow0.     \tag{2}
\]

Its splittings correspond precisely to primitive embedded
\((n+1)\)-fold ideals \(J_{n+1}\) with

\[
I^{n+1}\subset J_{n+1}\subset J_n,\qquad
J_{n+1}+I^n=J_n.                                          \tag{3}
\]

The obstruction is

\[
o_n(X,Z_n)=[Q_n]\in
\operatorname{Ext}^1(M,L^n)=H^1(C,M^\vee L^n).               \tag{4}
\]

If it vanishes, the set of compatible global extensions is a torsor under
\(H^0(C,M^\vee L^n)\).

**Proof.** In the displayed local form,

\[
IJ_n+I^{n+1}=(z^2,zy,y^{n+1}),
\]

so \(Q_n\) is freely generated over \(\mathcal O_C\) by the classes
of \(z,y^n\). The map to \(E\) has image \(M\), generated by the
linear class of \(z\), and kernel generated by \(y^n\). The image of
\(I^n\) is this kernel. The induced map from
\(\operatorname{Sym}^n E\) factors through
\(\operatorname{Sym}^n E/(M\operatorname{Sym}^{n-1}E)=L^n\),
and is an isomorphism onto the kernel. This constructs the injection
canonically rather than by a chosen frame.

A local splitting of (2) has image generated by \(z-a y^n\). Its
inverse image in \(J_n\) is

\[
(z-a y^n,y^{n+1}).                                        \tag{5}
\]

It is an ambient ideal since the action on \(Q_n\) factors through
\(\mathcal O_C\); (5) has the required primitive local form and
satisfies (3). Conversely any ideal satisfying the primitive form and
(3) gives such a splitting. Differences of splittings are exactly
\(\mathcal O_C\)-linear maps \(M\to L^n\), so the standard splitting
cocycle is the Yoneda class (4). This proves all assertions.

The construction depends only on \(\mathcal O_X/I^{n+1}\) and the
specified \(J_n\) in that neighborhood. For \(n=2\) it is the
inherited corrected theorem. For \(n>2\) it gives a useful explicit
embedded hierarchy. It does not say that varying all lower structures is
a single linear problem: each torsor is defined **after fixing** \(Z_n\).

The hierarchy is functorial under isomorphisms carrying the whole
embedded data to one another. Flat pullback preserves the constructions;
other base changes require the relevant ideals, products, and exact
sequences to remain compatible. It does not identify cohomology groups
across arbitrary base changes.

## 3. The relative divided leading-class theorem

**Proved proposal B2, with explicit relative hypotheses.** Fix a DVR
\(R\) with a chosen uniformizer \(\pi\) and residue field \(k\).
Fix an integral marked embedded lifting problem and a special quotient
\(\bar q\). Suppose:

1. The admissible lifts modulo \(\pi^2\), including the specified gauge
   normalization, form a nonempty torsor \(P\) under a \(k\)-vector
   space \(T\).
2. The canonical embedded extensions give a relative obstruction bundle
   \(\mathcal H\), locally free over the relevant parameter space.
   Its reductions at all points of \(P\) identify canonically with the
   same \(H=\operatorname{Ext}^1(M_k,L_k^2)\). These identifications
   require the asserted relative cohomology and base-change properties.
3. Each integral obstruction \(o(q)\) reduces to zero modulo \(\pi\).
   Consequently the leading reduction
   \[
   \lambda(q)=\frac{o(q)}\pi\bmod\pi\in H                 \tag{6}
   \]
   is defined using
   \(\pi\mathcal H/\pi^2\mathcal H\simeq\mathcal H/\pi\mathcal H\).
4. The leading section is affine-linear: for one, hence every, base
   point \(q_0\in P\),
   \[
   \lambda(q_0+t)=\lambda(q_0)+D(t)
   \]
   with \(D:T\to H\) \(k\)-linear.

Then \(D\) is independent of \(q_0\), and

\[
\mathfrak o(P):=[\lambda(q_0)]\in\operatorname{coker}D        \tag{7}
\]

is independent of every base-point choice and every compatible integral
trivialization. It is natural under isomorphisms of the marked integral
problem. If \(\mathfrak o(P)\ne0\), no admissible lift in \(P\)
has zero leading obstruction, so no integral primitive triple in the
specified family exists. If the class is zero, the leading obstruction
can be cancelled within this torsor, but higher precision or later
primitive stages may still obstruct.

**Proof.** Freeness makes multiplication by \(\pi\) an isomorphism
\(\mathcal H/\pi\mathcal H\to\pi\mathcal H/\pi^2\mathcal H\),
so (6) is unambiguous in the canonically reduced fiber. A frame change
\(F=F_0+\pi F_1\) changes the leading vector by \(F_0\) only:
\((F\pi v)/\pi\equiv F_0v\pmod\pi\). In particular, changes of
integral kernel frames reducing to the identity have no effect.
Replacing \(q_0\) by \(q_0+t_0\) replaces its leading vector by
\(\lambda(q_0)+D(t_0)\), and
\(\lambda(q_0+t_0+t)-\lambda(q_0+t_0)=D(t)\).
This proves base-point independence and (7). The relative extension
and reduction are functorial; under a compatible change of tangent and
obstruction frames, \(D\) changes by the corresponding source and
target isomorphisms, so its cokernel and (7) transport naturally.
Nonvanishing follows directly from the affine equation.

This proof is elementary once the relative hypotheses are established.
It does not assume that unrelated integral Ext fibers can be compared
before reduction. It also does not infer affine linearity from the word
"obstruction." A smooth first-order lift problem and a regular section
often give affine linearity by the square-zero Taylor rule, but the
admissible parameterization, gauge quotient, and base-change comparison
must still be established in the actual embedded problem.

The relevant \(D\) is the variation of the **divided first-order**
section on the marked congruence torsor. We do not identify it
unqualifiedly with the ordinary differential of the undivided section
on a reduced congruence special fiber. A uniformizer change rescales
(6) by its residue unit; vanishing is preserved, while a numerical
normalization depends on the chosen uniformizer. The formal statement
works with \(\pi\) over a ramified DVR when its hypotheses hold;
division by \(p\) then has a different valuation. The audited quartic
calculation is not thereby extended to all ramified DVRs.

## 4. A genuine comparison map, with the arithmetic datum still missing

The companion [quadratic gluing comparison](#2026-10-21-z4-quadratic-gluing-comparison)
proves the following precise statement. Let two marked quadratic
neighborhoods \(A_2,A_2'\) have the same first neighborhood
\(A_1=\mathcal O_X/I^2\) and the same kernel
\(B=\operatorname{Sym}^2 E\). Assume they are locally isomorphic as
algebras inducing the specified identities on \(A_1,B\). Define

\[
\mathcal D_2=\operatorname{Der}_S(A_1,B),\qquad
\rho_q:\mathcal D_2\longrightarrow\operatorname{Hom}(M,L^2),
\quad \rho_q(\delta)=\operatorname{Sym}^2(q)\circ\delta|_M.  \tag{8}
\]

The restriction to \(M\) is \(\mathcal O_C\)-linear: multiplication
by the square-zero ideal \(E\) kills \(B\), so the Leibniz rule
gives \(\delta(ae)=a\delta(e)\). The overlap differences of local
isomorphisms give a class
\(\beta(A_2',A_2)\in H^1(C,\mathcal D_2)\), and, with the
orientation in that proof,

\[
o_{A_2'}(q)-o_{A_2}(q)=H^1(\rho_q)(\beta(A_2',A_2)).        \tag{9}
\]

This is a natural map with a specified source and target, rather than a
projection onto one normal-coordinate summand. It allows derivations
moving base functions into \(B\). Changes of coordinates transporting
the marked first neighborhood transport (8) and (9); an order-one
movement of a base coordinate must first be carried to the common
\(A_1\). Changing \(q\) changes \(\rho_q\) and its target as part
of the relative family. There is no canonical identification of targets
for arbitrary unrelated quotients.

A sufficient **conditional arithmetic comparison** is now exact. An
arithmetic construction must provide a coordinate-equivariant sheaf
map \(\chi:\mathcal A\to\mathcal D_2\) and a cocycle
\(a\in H^1(C,\mathcal A)\) whose image is the actual gluing
difference \(\beta\). Its image in the embedded obstruction is then
\(H^1(\rho_q\chi)(a)\), by (9). If the cocycle is divisible by
\(\pi\), compatible flatness and base change allow leading division;
if B2's affine hypotheses hold, one may then pass to the persistent
cokernel.

The universal polynomial

\[
\Delta_{p^r}(a,b)=\frac{(a+b)^{p^r}-a^{p^r}-b^{p^r}}p
\]

supplies neither \(\chi\) nor the gluing class \(\beta\).
Its additive polynomial cocycle identity is not the descent condition
for the full embedded quadratic neighborhood. No such arithmetic
\(\chi\) has been constructed here for the quartic. This names a
precise missing lemma rather than treating a numerical coefficient as
an operation in deformation theory.

The derivation source has the usual cotangent-complex interpretation
\(\operatorname{Hom}(\mathbb L_{A_1/S},B)\) in degree zero.
This does not identify the embedded group with an arbitrary
Frobenius-lifting or Witt-vector obstruction group. Those deformation
problems require their own source objects and comparison maps.

## 5. Recovery of the quartic class and its persistence

Use the accepted full Laurent coefficients, with the fixed marked
frames of the persistent audit:

\[
\begin{aligned}
C_1&=h(ah+3b^2-5bd+3d^2),\\
C_2&=(b-d)(4ah+3b^2-8bd+6d^2),\\
C_3&=a(ah+9b^2-23bd+15d^2).
\end{aligned}                                             \tag{10}
\]

The full canonical class is represented by
\(C_1[u^{-1}]+C_2[u^{-2}]+C_3[u^{-3}]\) in
\(H^1(\mathbf P^1_R,\mathcal O(-4))\).
At \(a=b=h=0,d=1\), (10) gives exactly

\[
o_X(q_0)=-6[u^{-2}].                                      \tag{11}
\]

Substitute \(a=2\alpha,b=2\beta,h=2\gamma,d=1+2\delta\).
Dividing the full coefficients by two and reducing modulo two gives

\[
\lambda(\alpha,\beta,\gamma)
=\gamma[u^{-1}]+[u^{-2}]+\alpha[u^{-3}],\qquad
D(\alpha,\beta,\gamma)
=\gamma[u^{-1}]+\alpha[u^{-3}].                            \tag{12}
\]

Here \(\delta\) is quotient-frame gauge. The inherited exhaustiveness
and surjectivity proof supplies the full admissible torsor. The image
of \(D\) has dimension two, its kernel is the \(\beta\)-direction,
and the image of \(\lambda\) in its one-dimensional cokernel is
\([u^{-2}]\ne0\). B2 explains exactly the lift independence and
relative functoriality of this cokernel class. This recovers the
known value through the full extension cocycle; it does not construct
a divided-Frobenius preimage of (11).

Coordinate invariance can be tested without isolating a raw summand.
In adapted normal coordinates an embedded triple is
\((x-a(t)y^2,y^3)\). Under an integral change with units
\(\alpha,\delta\) on \(C\),

\[
\begin{aligned}
x'&=\alpha(t)x+C(t)y^2+A(t)xy+B(t)x^2,\\
y'&=\beta(t)x+\delta(t)y+D(t)y^2+E(t)xy+F(t)x^2,
\end{aligned}
\]

its new coefficient is

\[
a'=\frac{\alpha a+C}{\delta^2}\quad\bmod I.               \tag{13}
\]

A base change \(t'=t+e(t)y+f(t)x+O(I^2)\) changes coefficients
only in order \(I\); multiplication by \(y^2\) pushes that effect
to \(I^3\). Formula (13) therefore includes moving-base changes.
For two splittings, \(a'-b'=(\alpha/\delta^2)(a-b)\), exactly
the transition of \(\operatorname{Hom}(M,L^2)\). The complete
cocycle and the relative leading class transport; its individual
coordinate summands need not.

For a nontrivial chartwise nonlinear change of the local splitting
representatives by \(1+u\) and \(v+v^2\), the normalized Laurent
representative changes by

\[
-(1+u)+u^{-4}(u^{-1}+u^{-2}),                               \tag{14}
\]

an integral Čech coboundary in \(\mathcal O(-4)\). Thus the
representative \(-6u^{-2}\) and its leading cokernel class are
unchanged. The new script verifies (13) including nonconstant base
coefficients and moving-base displacement, and (14). This is a check
of the full splitting-cocycle rule, not a fresh re-expansion of the
previously audited ambient rational chart divisions or of the
user-reported Laurent supplement.

## 6. Same conormal, different geometric obstruction

**Counterexample B3.** Work over any field \(k\). On the standard
charts of \(C=\mathbf P^1_k\), glue two copies of \(\mathbf A^2\)
by the triangular polynomial isomorphism

\[
v=u^{-1},\qquad
y_\infty=u^{-6}y_0,\qquad
x_\infty=u^{-8}x_0+c u^{-10}y_0^2.                         \tag{15}
\]

This gives an actual smooth algebraic threefold \(X_c\to C\),
affine over \(C\), with zero section \(C\). The inverse transition
is polynomial in the normal variables over \(k[u,u^{-1}]\).
For every \(c\), the conormal and quotient are identically

\[
E=M\oplus L=\mathcal O(-8)\oplus\mathcal O(-6),\qquad
q(x)=0,\quad q(y)=y.
\]

The ribbon ideal \((x_i,y_i^2)\) glues. In (1) its two local
generators are \(x_i,y_i^2\), and (15) gives normalized extension
cocycle

\[
\frac{c u^{-10}}{u^{-8}}=c u^{-2}.
\]

Since

\[
H^1(\mathbf P^1_k,\mathcal O(-4))
=\frac{k[u,u^{-1}]}{k[u]+u^{-4}k[u^{-1}]},
\]

\(o_{X_c}(q)=c[u^{-2}]\) with the chosen Čech sign. It is nonzero
if \(c\ne0\). For \(c=0\), every ideal \((x_i,y_i^n)\) glues,
so all primitive multiplicities exist compatibly.

Consequently there is no rule depending only on the identified pair
\((E,q)\), or only on functorial symmetric or divided powers of it,
whose value equals the embedded obstruction for every regular
embedding. The two examples have the **same globally split conormal**;
only the split ambient model has the asserted tower. This does not
disprove the existence of zero maps or of a more sophisticated
arithmetic comparison retaining the full neighborhood.

It also makes the distinction between symmetric and divided powers
concrete. The regular-immersion graded algebra is
\(\operatorname{gr}_I\mathcal O_X=\operatorname{Sym}E\).
The functor \(\Gamma(E)\) is determined by the same bundle and is
identical for both models. It does not supply a divided-power
structure on the ambient ideal. The divided-power identity
\(n!\gamma_n(x)=x^n\) is
[Stacks Project, Lemma 23.2.2](https://stacks.math.columbia.edu/tag/07GK).
Over an integral DVR, a nonzero
ordinary normal generator \(x\) in a polynomial algebra cannot
generally satisfy \(p!\gamma_p(x)=x^p\), since \(x^p\) is not
divisible by \(p!\) in that algebra. A divided-power envelope or a
chosen Frobenius lift is additional data, not a consequence of having
a conormal bundle.

## 7. Same special fiber, different divided obstruction

**Counterexample B4.** Over \(R=\mathbf Z_{(p)}\) or
\(\mathbf Z_p\), replace the coefficient in (15) by \(p^h c\),
where \(h\ge1\). Then

\[
o_{X_{p^h c}}(q)=p^h c[u^{-2}]
\in H^1(\mathbf P^1_R,\mathcal O(-4))\simeq R^3.            \tag{16}
\]

All these smooth integral ambients have literally the same split
special fiber, with the same \(C_k,E_k,q_k\) and the same special
neighborhoods of every order. Nevertheless the first nonzero
\(p^h\)-divided obstruction in (16) is \(\bar c[u^{-2}]\);
the split integral lift has zero obstruction. If \(h>1\), division
by \(p\) alone still gives zero modulo \(p\), as it should.

There is an equally explicit persistence statement for \(h=1\).
For the split integral ambient, every quotient \(E\twoheadrightarrow L\)
extends to a compatible primitive tower: the surjection of symmetric
algebras \(\operatorname{Sym}E\to\operatorname{Sym}L\) constructs
the embedded line subbundle, whose zero-section powers give the tower.
Its obstruction section is therefore identically zero. The difference
from this split ambient in (15) is \(p\) times a gluing derivation.
If \(q'=q+p t\) is any admissible first-order quotient lift reducing
to the same special \(q\), both restriction to its kernel and
\(\operatorname{Sym}^2(q')\) have the same reduction as for \(q\).
Formula (9) consequently gives

\[
\lambda(q')=\bar c[u^{-2}],\qquad D=0.                     \tag{17}
\]

The compatible special-fiber Ext identification is the one in B2;
here the line bundles on \(\mathbf P^1_R\) have the displayed
free cohomology modules. Thus these integral lifts can have different
persistent cokernel classes even though their entire special
geometries agree. The marked integral lift is an essential argument
of any general comparison theorem, not optional provenance.

## 8. Characteristic \(p\), normal order, and arbitrary failure stages

The inherited arithmetic identity is

\[
v_p\binom{p^r}{j}=r-v_p(j),\qquad
\Delta_{p^r}(a,b)\equiv
\sum_{k=1}^{p-1}\frac{(-1)^{k-1}}k
a^{(p-k)p^{r-1}}b^{kp^{r-1}}\pmod p.                       \tag{18}
\]

If \(a\) is a unit along \(C\) and \(b\) has normal order one,
the least normal order displayed in (18) is \(p^{r-1}\).
If **both** arguments have normal order one, every monomial instead
has total normal order \(p^r\). This distinction must be retained
when applying the polynomial to ambient coordinates.

| \(p,r\) | \(\Delta_{p^r}\bmod p\) | least order if \(a\) is a unit, \(b\) normal |
| --- | --- | --- |
| \(2,1\) | \(ab\) | 1 |
| \(2,2\) | \(a^2b^2\) | 2 |
| \(2,3\) | \(a^4b^4\) | 4 |
| \(3,1\) | \(a^2b+ab^2\) | 1 |
| \(3,2\) | \(a^6b^3+a^3b^6\) | 3 |
| \(5,1\) | \(a^4b+2a^3b^2+2a^2b^3+ab^4\) | 1 |
| \(5,2\) | \(a^{20}b^5+2a^{15}b^{10}+2a^{10}b^{15}+a^5b^{20}\) | 5 |

For example, a particular unit-versus-normal term of degree three
is invisible modulo \(I^3\). That observation does not determine
the first geometric obstruction: other transition terms, quotient
changes, or lower-order compositions may contribute. Even a visible
arithmetic term can project to zero, be a Čech coboundary, or be
cancelled by quotient variation. The split model in B3 has all
primitive powers while every polynomial in (18) is nonzero as a
universal polynomial.

There is a stronger geometric independence. For any \(n\ge2\),
replace (15) by

\[
y_\infty=u^{-6}y_0,\qquad
x_\infty=u^{-8}x_0+c u^{-10}y_0^n.                         \tag{19}
\]

The prescribed structures \((x_i,y_i^j)\) glue for every \(j\le n\).
The stage-\(n\) extension (2) has normalized cocycle

\[
c[u^{-2}]\in H^1(\mathbf P^1_k,\mathcal O(8-6n)),           \tag{20}
\]

which is nonzero for \(c\ne0\), since \(8-6n\le-4\). Equivalently,
a compatible extension would require polynomials
\(b_0\in k[u]\), \(b_\infty\in k[u^{-1}]\) solving

\[
b_0-u^{8-6n}b_\infty=-c u^{-2},
\]

which is impossible by the Laurent quotient. Hence the first failure
of this specified primitive tower can occur at an arbitrary chosen
stage over **every** characteristic. It is not predicted solely by
\(p\) or \(p^r\). This is an actual smooth ambient construction,
not a formal analogy or a generic-point calculation.

At each fixed higher stage (2), a relative analogue of B2 can be
applied if its Ext module is locally free and its divided leading
section is affine on the specified lift torsor. Those hypotheses
are substantive. At higher precision the leading section can be
nonlinear. For the elementary section \(o(q)=4+q^2\) over
\(\mathbf Z_{(2)}\), restrict to \(q=2t\). It is divisible by four,
and

\[
\frac{o(2t)}4\bmod2=1+t^2.
\]

Its ordinary differential is zero, yet it vanishes at \(t=1\).
Quotienting by the image of that differential would incorrectly
declare a persistent nonzero class at \(t=0\). This is a counterexample
to an unrestricted higher-order linear-cokernel recipe, not a claimed
geometric realization of that elementary section. The fixed-stage
torsor theorem remains valid; the family of earlier choices need not
be affine-linear in a higher divided obstruction.

## 9. Verification and definite boundary

The new script is
[verify_z4_general_mechanism_2026_10_21.py](../computations/verify_z4_general_mechanism_2026_10_21.py).
It was run successfully on 2026-10-21 with

```text
/private/tmp/stci-z4-env/bin/python research/computations/verify_z4_general_mechanism_2026_10_21.py
```

The existing environment provides SymPy. The system and bundled
\(\texttt{python3}\) executables tested here lack SymPy; no package
installation or runtime mutation was needed. All six check groups passed:

* the accepted full Laurent polynomials give (11), (12), and rank two;
* a nonlinear adapted change with moving base coefficients obeys (13);
* nontrivial integral chartwise changes add only the coboundary (14);
* the new stage models have the nonzero normalized class for stages 2–8;
* \(p=2,3,5\), \(r=1,2,3\) illustrate the arithmetic and normal-order regimes;
* the higher divided-section example has zero differential and a cancelling lift.

The arbitrary-stage and general theorems are proved above, rather than
inferred from these finite checks. The old ambient rational-chart
calculation and already accepted carrier exclusions were not rerun.

**Proved:** the hierarchy (2), the relative leading-class theorem under
its stated hypotheses, the geometric gluing comparison (8)–(9), and
the smooth counterexamples B3–B4 and (19).
**Conditional:** a divided-Frobenius interpretation after supplying a
coordinate-equivariant arithmetic source cocycle and map \(\chi\)
that reproduce the actual gluing difference.
**Open:** constructing that additional arithmetic datum for the
marked quartic, or proving a sharper impossibility result even with
the full integral lift retained. There is no general recovery from
conormal or special-fiber data, no universal arithmetic nonvanishing
theorem, and no deduction here about an arbitrary characteristic-zero
STCI pair without the bridge analyzed in Investigation A.

The [independent general-mechanism audit](#2026-10-21-z4-general-mechanism-independent-audit)
records independent checks and any scope corrections. The separate
[synthesis](#2026-10-21-z4-general-mechanism-synthesis) compares these
results with Investigation A. All claims remain unpromoted research
evidence.


---

## 2026-10-21-z4-persistent-arithmetic-obstruction

# Investigation 3: persistent leading arithmetic obstruction for the prescribed Z4

Date: 2026-10-21. **Status: new research proposal; requires independent audit; not canonical promotion.**
Branch: `research/z4-persistent-arithmetic-obstruction-2026-10-21`.
Scope: fixed embedded relative rational quartic over R=Z_(2), fixed special conormal quotient, and the full family of integral quotients lifting it. No general STCI conclusion.

## Verdict: B (relative to the fixed embedded deformation problem)

The variation subspace of the leading Yoneda obstruction is intrinsically the image of the first-order variation map and has dimension two. Its cokernel is one-dimensional and the persistent class is nonzero. This **does not** establish a canonical divided-Frobenius realization. In particular the distinguished middle Laurent coefficient is a *calculation* of the intrinsic quotient, not its definition.

### Source and authority

Read AGENTS.md, research/INDEX.md, research/STATE.md, research/FRONTIER.md; corrected independent Yoneda audit at `research/intrinsic-ribbon-triple-audit-2026-10-21:research/notes/2026-10-21-intrinsic-ribbon-triple-independent-audit.md`; counterexample at `research/z4-divided-frobenius-2026-10-21:research/notes/2026-10-21-z4-coordinate-invariance-counterexample.md`; and the five 2026-10-20 Z4 reports on main. The quartic cocycle formula and its identification with the canonical Yoneda extension are imported from the independently audited sources; the mod-4 reduction and variation/cokernel conclusions are checked here. The earlier normal-coordinate summand is explicitly *not* invariant.

## 1. Exact family of admissible quotients

Let E=I/I², L=O(-6), M=O(-8), and fix the reduction \bar q:E_k -> L_k of the distinguished quotient. Define Q as the set of surjections q:E_R -> L_R whose reduction equals \bar q, **modulo automorphisms of L_R reducing to the identity**. The last quotient only removes scalar presentation gauge; keeping framed quotients instead gives the same obstruction and variation.

Using the audited U/V conormal transition, every homomorphism E -> L has exactly the form
```
p=a+bu+3hu², q=d+2hu;
P=3ac²+(3b-4d)c+h, Q=2ac+2b-3d
```
with a,b,h,d in R. Fixing the reduction imposes a,b,h in 2R and d in 1+2R. **Every such choice is surjective**: on U, q=d+2hu reduces to 1; on V, Q=2ac+2b-3d reduces to 1 in F2[c]. A cokernel of a map of finite locally free sheaves supported away from the closed fiber on the proper R-curve is empty (equivalently, on these two affine charts one of the two displayed components is a unit, since d is odd and 2h is even, and Q has odd constant and even other coefficients). Thus no extra realizability constraint occurs.

More precisely the displayed U component q=d+2hu is a unit in R[u] **only when h=0**; surjectivity is instead by the pair (p,q) and the properness/closed-fiber argument above, not by claiming q is a unit in the polynomial ring. This distinction matters.

The parameter space of framed lifts is the congruence fiber in the rank-four R-module Hom(E,L); after quotienting by scalar units 1+2R it is a formal neighborhood of the distinguished point in the open scheme of quotients. Its mod-4 first-order tangent space is
T = H⁰(C_k,Hom(M_k,L_k)) = H⁰(P¹_k,O(2)), dimension 3.
Indeed the four parameters (α,β,γ,δ) modulo 2 have the scalar direction δ, leaving (α,β,γ). The special-fiber quotient is fixed and the variation is first-order over R/4; no assertion is made that the whole integral congruence fiber is a vector space.

## 2. The intrinsic variation map

For each q in Q, let J₂(q)=ker(I -> E -> L), K(q)=I J₂(q)+I³ and
E_q=J₂(q)/K(q). The corrected audit proves a canonical extension
0 -> L² -> E_q -> M -> 0
and its class o(q) in A=Ext¹(M,L²)=H¹(O(-4)).
The fixed special quotient supplies fixed special L_k and M_k, so all classes reduce into the same A_k=A/2A. The audited calculation gives o(q) in 2A for every q in Q. Define λ(q)=(o(q)/2) mod 2.

For t in T choose any lift q_t congruent to q₀+2t modulo 4 (a local choice of quotient frame is harmless). Define
D(t)=λ(q_t)-λ(q₀) in A_k.
The formula depends only on t, not on the lift modulo 4: the audited obstruction is polynomial in a,b,h,d with integral coefficients, and differences of parameters in 4R give differences in 4A. Its first-order Taylor expansion is linear because products of two 2-adic perturbations vanish modulo 4. Scalar presentation gauge acts trivially on the extension class. This gives a canonical k-linear map D:T -> A_k, with functoriality under automorphisms of the fixed embedded deformation problem. It is **not** a canonical map from an unmarked abstract P¹ without its embedded quotient.

With a=2α,b=2β,h=2γ,d=1+2δ, exact polynomial reduction yields
(C₁,C₂,C₃)=(2γ,2,2α) mod 4.
Consequently in the audited Laurent basis (u^-1,u^-2,u^-3),
λ(q)=γ[u^-1]+[u^-2]+α[u^-3],
D(α,β,γ)=γ[u^-1]+α[u^-3].
All α,γ in F2 occur for actual surjections (previous section); hence
**V=im(D)=span{[u^-1],[u^-3]}**, dim V=2.
The β-direction is the kernel of D, and δ is presentation gauge. Thus the span of all pairwise differences is exactly im(D), not merely contained in it.

The coordinate-free definition of V is im(D), not the displayed span. The canonical extension, reduction and first-order difference construction commute with isomorphisms of (X_R,C_R,\bar q) preserving the specified integral deformation problem; therefore such isomorphisms transport V and the quotient class. Changing adapted normal coordinates, including quadratic corrections and moving-base terms, changes representatives and local splittings but not Yoneda classes. The counterexample for A'=A+B shows why a singled-out quadratic contribution cannot replace the full extension.

## 3. Persistent class and dual interpretation

Define \bar λ to be the common image of λ(q) in A_k/V. This is independent of q because all differences lie in V. Since dim A_k=3 and dim V=2, dim(A_k/V)=1. The displayed calculation gives \bar λ equal to the nonzero image of [u^-2]. Therefore no admissible integral quotient admits an embedded primitive triple: its Yoneda class has nonzero leading component.

By Serre duality A_k^∨=H⁰(P¹_k,O(2)). The annihilator V^⊥ is an **intrinsically defined line**, namely ker(D^∨). In the standard u=s/t chart, residue pairing identifies [u^-1],[u^-2],[u^-3] with the coefficient functionals on 1,u,u², respectively. Thus V^⊥ is spanned by u, i.e. the homogeneous quadratic st. This is a **geometric characterization relative to the embedded deformation problem**: the line is the annihilator of its obstruction variation, not an arbitrary declaration that the monomial st is canonical on an unmarked P¹. The pairing of λ with any nonzero element of V^⊥ is nonzero (over F2 it equals 1 with the indicated normalization). There is no claimed absolute preferred generator under all automorphisms of an unmarked curve.

This is also the cokernel of the linearized Yoneda obstruction map. Its interpretation needs no new noncanonical splitting of the reduced extension.

## 4. Divided fourth powers: boundary of the theorem

D₄(a,b)=((a+b)^4-a^4-b^4)/2 = 2a³b+3a²b²+2ab³, so D₄ mod 2=a²b². This is a natural polynomial cross-effect for *specified elements* a,b of an integral algebra; it is not additive in each input and does not by itself define a sheaf-linear morphism into Ext¹(M,L²). In particular replacing adapted normal coordinates by A'=A+B changes an isolated quadratic contribution by 9[u^-1], nonzero modulo 2, while the total Yoneda class is fixed (source counterexample). This variation lies in V for this example, but that coincidence **does not prove** that arbitrary divided-power coordinate defects land in V or that D₄ descends to A_k/V.

No canonical natural transformation from the filtered quadratic neighborhood or a PD/Frobenius-lift structure to A_k/V is constructed here. Additional choices would at minimum require a functorial way to evaluate the fourth-power cross-effect on the embedded conormal filtration and a proof that all coordinate/gauge defects map into V. Consequently the arithmetic leading class and its persistence are proved, while a divided-Frobenius identification remains unproved.

## 5. Reproducibility and scope

Run `python3 research/computations/verify_z4_persistent_obstruction_2026_10_21.py` (SymPy) for exact coefficient identities and linear rank. The script checks polynomial identities, not the source geometric conormal parameterization or the general Yoneda theorem; those are proved in the cited audits. Example actual lifts: (a,b,h,d)=(0,0,0,1), (2,0,0,1), (0,0,2,1), (2,0,2,1), yielding divided coordinates (0,1,0),(0,1,1),(1,1,0),(1,1,1).

**Investigation 4 handoff (no investigation performed):** for a proposed p^r analog first establish a flat integral embedding and a fixed special quotient, compute its canonical Yoneda obstruction, prove divisibility by p in a p-torsion-free Ext group, identify the actual mod-p quotient-deformation tangent and the image of its leading obstruction differential, and only then test whether divided p-power cross-effects descend to the intrinsic cokernel. The p=2 quartic result alone proves no general p^r statement.


---

## 2026-10-21-z4-characteristic-zero-stci-consequences

# Characteristic-zero STCI consequences of the intrinsic obstruction

Date: 2026-10-21. **Status: new research proposal with proofs and an independent mathematical check of the principal new implications; no canonical promotion.** The unrestricted characteristic-zero STCI question for the fixed quartic remains open.

The main positive result below is a necessary condition that incorporates the *actual first-normal defect divisor* of a generically curvilinear complete intersection. The obstruction need not vanish globally: it must vanish after allowing poles bounded by that divisor. For the distinguished quotient from the arithmetic problem this forces a divisor of degree at least two, with a precise condition in degree two. This is a restriction on a specified normal direction, not an exclusion of arbitrary characteristic-zero STCI presentations.

The principal negative results are also definite. A global complete intersection with smooth support can be generically primitive and still contain no global primitive triple; this remains true with integral projective defining surfaces. Spreading a characteristic-zero pair preserves support after spreading finite ideal identities, but cannot force residue characteristic two, the specified marking, or the prescribed special scheme. Direct flat specialization of a hypothetical surviving quartic STCI intersection to the multiplicity-four scheme Z4 is already impossible by degree.

## 1. Exact setup, inherited claims, and authority

Unless a statement specifies otherwise, k is an algebraically closed field of characteristic zero,

\[
C=C_0=\{[s^4:s^3t:st^3:t^4]\}\subset X=\mathbf P^3_k,
\qquad I=I_C.
\]

Let F,G be homogeneous forms of degrees d,e, with no common surface component, and put J=(F,G), Z=V(J). First one may consider only C contained in the reduced intersection; then the fundamental cycle is m[C]+R with R effective and not containing C. The STCI hypothesis used here is the stronger equality Supp(Z)=C, equivalently R=0 together with the asserted set-theoretic support. Exceptional curves above points of C on a blow-up are not additional curves downstairs.

The following are inherited premises, rather than computations repeated in this report.

* [STCI-R-0001](../results/quartic_carrier_exclusion.md), with its accepted lower-degree and factor reduction, gives d,e at least five for any characteristic-zero STCI presentation of this C. Its complete quartic-carrier exclusion is not reopened here.
* The fixed normal bundle is N=O(7) squared, hence E=I/I²=O(-7) squared. The basic generic local intersection and blow-up restrictions are recorded in [the simultaneous-surfaces synthesis](../synthesis/02-two-surfaces.md); the entirely-thick inequalities are not asserted to exclude that branch.
* [STCI-R-0012](../results/prescribed_z4_arithmetic_nonlifting.md) rules out the prescribed flat embedded Z4 lift over exactly Z_(2) and Z_2. It does not exclude arbitrary characteristic-zero STCI presentations or arbitrary ramified bases.
* The [corrected independent ribbon-to-triple audit](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-21-intrinsic-ribbon-triple-independent-auditmd) constructs, for a line quotient q:E onto L with kernel M, the canonical extension

  \[
  0\longrightarrow L^2\longrightarrow B_q
  :=J_2/(I J_2+I^3)\longrightarrow M\longrightarrow0,
  \qquad J_2=\ker(I\to L).
  \tag{1}
  \]

  Its Yoneda class o_X(q) in H¹(M dual tensor L²) vanishes precisely when the fixed embedded ribbon admits an ambient embedded primitive triple. This is independently audited evidence, not a new promoted canonical record. The distinction matters: the ambient triple need not be contained in a given Z.
* The [persistent independent audit](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-z4-persistent-independent-auditmd) proves the fixed marked integral first-order calculation and its precise relative meaning. In particular, every admissible integral quotient reducing to the specified q0 has a middle obstruction coefficient 2 modulo 4. This additional relative conclusion is audited evidence, rather than a broader restatement of R0012.

The [existing literature assessment](OCT21_VALUATIONS_RESIDUAL_CYCLES_AND_Z4.md#source-2026-10-21-z4-intrinsic-obstruction-literaturemd) has been consulted. Its distinction between abstract multiple curves and fixed-ambient embedded extension is retained. No claim of priority over the multiple-curve literature is made for the elementary consequences proved here. The reports and the present proofs establish the stated scope; a familiar analogy with abstract extension or divided Frobenius is not being used as a theorem.

## 2. What an actual STCI presentation forces

### 2.1 Complete intersection, purity, and generic length — proved

The two equations have height two. Thus Z is a one-dimensional local complete intersection and is Cohen–Macaulay, Gorenstein, and unmixed. In the STCI situation its only associated support component is C; it has neither a residual curve nor an isolated embedded component.

At the generic point eta of C, the completed transverse regular local ring is K[[u,v]], K=k(C), and

\[
A_\eta=K[[u,v]]/(F,G)
\]

is a zero-dimensional complete intersection of length

\[
m=de/4\in\mathbf Z_{>0}.
\tag{2}
\]

The equality uses the full STCI support condition. With residual curves one only has de=4m+deg(R). If r,s are the normal orders of the displayed equations, m is at least rs; equality holds when their initial binary forms are coprime. Their first symbols need not generate the full initial ideal: (u²,u²+v³)=(u²,v³) is the basic cancellation example.

The maximal ideal of a local Artin algebra of length m has m-th power zero. Since O_Z injects into its localization at the unique generic associated point, this gives, sheaf-theoretically,

\[
I^m\subset J\subset I.
\tag{3}
\]

The injection follows from unmixedness: every function outside the prime of C is a nonzerodivisor. It is not inferred merely from equality of cycles. A larger finite power also suffices for every spreading argument below.

### 2.2 First-normal information and its exact limitations — proved

Write N1=image(J to E). If at least one equation has generic normal order one, N1 has generic rank one and A_eta is curvilinear, isomorphic to K[z]/(z^m). The saturation M of N1 in E is a line subbundle; its quotient L=E/M is invertible. On the smooth curve there is a unique effective divisor D such that

\[
N1=M(-D).
\tag{4}
\]

Here D is the common zero divisor of the *actual two first-normal symbols*, measured in their saturated line. It is not one of the divisors D_i of a saturated quasiprimitive order filtration. In particular it should not be silently substituted into [R0019](../results/quasiprimitive_residual_cycles.md).

If L=O(epsilon-7), then M=O(-7-epsilon), epsilon is nonnegative, and the two symbols are sections of

\[
M(4d)=O(4d-7-epsilon),\qquad
M(4e)=O(4e-7-epsilon).
\tag{5}
\]

One symbol can be zero identically. Where both vanish, both surfaces are singular along C in their normal directions. Saturation extends the generic direction, but does not supply a primitive triple in Z.

If both generic orders are at least two, N1=0; there is no preferred line quotient of E forced by the pair. The higher first relation, horizontal common-direction curve, and full initial ideal then require the additional hypotheses in such results as [R0006](../results/actual_ci_smooth_root_bridge.md). Neither the arithmetic Z4 result nor the construction (1) fills those interfaces.

## 3. A new necessary condition: defect-twisted obstruction vanishing

### Proposition A — proved

Let C be a smooth integral curve regularly embedded with codimension two in a smooth threefold, over any field. Let J be an ideal with support C, whose generic transverse algebra is curvilinear of length m at least three. Assume its first-normal image has rank one, and define M,L,D by (4). Set H=M dual tensor L². Then

\[
o_X(q)\longmapsto0
\quad\text{under}\quad
H^1(C,H)\longrightarrow H^1(C,H(D)).
\tag{6}
\]

Equivalently,

\[
o_X(q)\in
\operatorname{im}\bigl[H^0(C,H(D)/H)\longrightarrow H^1(C,H)\bigr].
\tag{7}
\]

Thus the ambient extension may have a nonzero obstruction, but the actual pair supplies a meromorphic splitting with poles bounded by its first-normal defect divisor. This assertion does not claim that the corresponding triple is globally contained in Z.

**Proof.** Since the first symbols of J lie in M, one has J contained in J2. Map J into B_q in (1), and let P be its image. This is an O_C-module: multiplication by I kills B_q. Its image under B_q to M is exactly N1=M(-D).

At eta choose adapted transverse parameters f,y with J_eta=(f,y^m); the existence of f with nonzero linear part follows from generic curvilinearity. For m at least three, y^m maps to zero in B_q because I³ is killed. The image of f spans a line that projects isomorphically to M_eta. Hence P_eta meets L²_eta trivially.

The kernel of P to M is a subsheaf of the line bundle L². It has generic rank zero, so it is zero on the integral curve. Consequently P is isomorphic to N1. Its inclusion in B_q is a lift of N1 to B_q and therefore a splitting of the pullback of (1) along N1 to M. Pullback of extensions induces the map

\[
\operatorname{Ext}^1(M,L^2)\to
\operatorname{Ext}^1(M(-D),L^2)
=H^1(H(D)),
\]

which proves (6). The long exact sequence of 0 to H to H(D) to H(D)/H to 0 proves (7). All images here are sheaf images; no unproved flatness of an ordinary associated graded is used. The proof fails for m=2 because the second generator y² survives in L². End of proof.

For projective C, Serre duality gives the equivalent incidence condition

\[
\langle o_X(q),V\rangle=0
\quad\text{for every}\quad
V\in H^0(C,\omega_C\otimes H^{-1}(-D)).
\tag{8}
\]

This form makes explicit which divisor data would have to be imposed on the actual homogeneous first symbols.

### Concrete corollary for the distinguished q0 — proved, restricted direction

For the fixed quartic and the distinguished marked characteristic-zero quotient q0 from the integral calculation,

\[
L=O(-6),\quad M=O(-8),\quad H=O(-4),\qquad
o_X(q0)=-6[u^{-2}].
\]

If a characteristic-zero STCI pair has generic normal order one and its saturated quotient is this q0, then its divisor D in (4) satisfies

\[
\deg D\ge2.
\tag{9}
\]

If deg D=2, write its defining binary quadratic in the marked coordinates as

\[
Q_D=A s^2+B st+C t^2.
\]

Then a further necessary condition is B=0. For deg D at least three the first obstruction in (6) is automatically killed, so this argument gives no further restriction.

**Proof.** Under the audited Laurent/Serre pairing, [u^-2] is the functional extracting the middle coefficient of a binary quadratic. For D=0 it is nonzero. For D=P a point, H0(O(2)(-P)) is the kernel of evaluation at P. A nonzero functional annihilates this kernel exactly if it is proportional to evaluation at P. The evaluation functionals have coordinates [a²:ab:b²]; none equals [0:1:0] in characteristic zero. Thus degree one cannot work. In degree two, H0(O(2)(-D)) is spanned by Q_D and (8) is exactly B=0, including nonreduced divisors. In degree at least three H¹(O(-4+D))=0. End of proof.

This is a condition on actual surface singularity/common-zero data. It does not assert that any such pair exists, or that the incidence condition suffices to lift all later stages. The q0 label includes the chosen integral embedding and marking; it is not assigned to every quotient of degree -6.

### Size of the unrestricted first obstruction — proved

For any line quotient of E=O(-7) squared with L=O(epsilon-7),

\[
H=M^\vee\otimes L^2=O(3epsilon-7),\qquad
h^1(H)=\max(0,6-3epsilon).
\tag{10}
\]

Therefore the first embedded ribbon-to-triple obstruction vanishes for **every** such quotient when epsilon is at least two. All those ribbons have ambient embedded primitive triples, irrespective of whether a particular STCI scheme contains them. In the accepted order-one range 0 at most epsilon at most 6, only epsilon=0 or 1 can be detected at this first stage.

Even epsilon=1 does not uniformly obstruct. The inherited full cubic coefficient formulas are

\[
\begin{aligned}
C_1&=h(ah+3b^2-5bd+3d^2),\\
C_2&=(b-d)(4ah+3b^2-8bd+6d^2),\\
C_3&=a(ah+9b^2-23bd+15d^2).
\end{aligned}
\tag{11}
\]

The distinguished parameters (a,b,d,h)=(0,0,1,0) give (0,-6,0). By contrast (0,1,1,0) gives (0,0,0). The latter quotient is surjective on both charts: its local pairs are (p,q)=(u,1) and (P,Q)=(-c,-1). Thus there is an actual unobstructed quotient of the same degree. It does not reduce to the prescribed q0 modulo two, so there is no conflict with the marked integral obstruction.

## 4. Exactly when an actual pair supplies a primitive triple

### Proposition B — proved: an all-points sufficient condition

Suppose locally at **every** point of C there is f in J with nonzero linear normal coefficient, and

\[
J\subset(f)+I^3.
\tag{12}
\]

Then J3=J+I³ is a globally defined embedded primitive triple, contained in Z. Its local ideal is (f,y³) for I=(f,y); its ribbon is induced by the first-normal image, and its obstruction (1) vanishes.

Indeed (12) and f in J give J+I³=(f)+I³=(f,y³). These local expressions concern one global ideal J+I³, so no extra gluing choice is being assumed. The condition is pointwise, rather than merely generic.

In particular, if Z is an actual local complete intersection with support exactly C, generic multiplicity m at least three, and its first-normal image is a line subbundle of E **everywhere** (D=0), then it is locally a primitive m-fold structure and Proposition B applies. To prove this, choose f in J generating the first-normal image at a given point. The surface W=(f) is smooth there and C is Cartier on W, say with equation y. The remaining equation has zero support exactly C on W. The regular local ring of W is factorial, so that equation is a unit times y^m. Its exponent is the generic multiplicity. Thus J=(f,y^m), and (12) follows. The same proof works relatively over a DVR for a smooth relative setup with this everywhere rank-one condition and the asserted total support.

Proposition A recovers ambient vanishing when D=0; the local support argument in this paragraph additionally proves containment of the primitive triple in Z.

### Counterexample C — generic primitivity does not globalize

Let C be the line V(x,y) in projective three-space with coordinates [t:x:y:w], and consider the complete intersection

\[
Y=V(x^2,y^2+t x).
\tag{13}
\]

Its support is exactly C. The two *integral* quadrics

\[
F=x^2+y^2+t x,\qquad G=x^2+2y^2+2t x
\tag{14}
\]

generate the same ideal, since 2F-G=x² and G-F=y²+t x. Each has rank three in characteristic zero, hence is irreducible even over the algebraic closure.

On w=1 the algebra is free over k[t] with basis 1,x,y,xy: it is a monic quadratic extension of k[t][x]/(x²). Where t is invertible,

\[
(x^2,y^2+t x)=(x+y^2/t,y^4),
\]

so Y is generically primitive of multiplicity four. At the point t=0, however, its transverse algebra is k[x,y]/(x²,y²). There is no surjection from this algebra to k[z]/(z³). Any such map sends x to az+bz² and y to cz+dz²; squaring forces a=c=0, so the images cannot generate z. A primitive triple inside Y near that point would be finite flat of rank three over the local t-axis and would give exactly this forbidden quotient after setting t=0. Hence no global primitive triple is contained in Y.

There is nevertheless a global embedded ribbon V(x,y²) contained in Y. Its quotient has M=L=O_C(-1), so its *ambient* obstruction lies in H¹(O(-1))=0. The ambient primitive triple V(x,y³) exists, but is not contained in Y: y²+t x maps to y². Thus even an actual induced ribbon and a vanishing ambient Yoneda class do not establish the missing containment implication. The generic triple kernel x+y²/t displays the unavoidable pole.

This example disproves the general implication using a smooth projective support and integral defining surfaces. Its support is a line, not C0. It does not disprove a possible special theorem using extra geometry of C0. Such a theorem must supply that additional argument; generic local complete intersection or generic curvilinearity is insufficient.

For completeness, even generic primitivity itself need not hold for a complete intersection: (u²,v²) in K[[u,v]] has embedding dimension two and no curvilinear length-three quotient by the same argument. Its Gorenstein property does not change this fact.

## 5. Spreading out: what survives, and what does not

### Proposition D — proved: support-preserving finite-type spread

For a characteristic-zero STCI pair of the fixed C there is a finite-type integral Z-algebra A contained in k and forms F_A,G_A of the same degrees such that

\[
I_A^N\subset(F_A,G_A)\subset I_A
\tag{15}
\]

as ideals, for some finite N, and every field fiber has reduced support exactly C. One may arrange that Z_A is a flat relative complete intersection of type (d,e).

**Proof.** Projective support equality gives height two for (F,G). Its homogeneous quotient is Cohen–Macaulay of depth two, so (F,G) is saturated. Hence its homogeneous radical is I_C and some homogeneous power I_C^N lies in (F,G). This explains the passage from sheaf support to homogeneous polynomial identities.

The fixed integral model of C can be given by

\[
\begin{aligned}
q&=x_0x_3-x_1x_2,& f&=x_1^3-x_0^2x_2,\\
h&=x_1^2x_3-x_0x_2^2,& g&=x_2^3-x_1x_3^2.
\end{aligned}
\]

It is the standard relative P¹: on x0 nonzero the chart is A[u] with coordinates (1,u,u³,u⁴), and on x3 nonzero it is the analogous chart A[c]. These charts cover the projective scheme, since x0=x3=0 forces x1=x2=0 at every homogeneous prime.

Choose finite membership identities expressing F,G in this ideal and each monomial generator of its N-th power in (F,G). Adjoin to Z every coefficient in those identities and in F,G. The resulting domain A is finite type, and the identities hold over A and after **every** base change. Thus every field fiber has the prescribed radical. This argument does not assume that tensor product preserves injections.

Every field fiber is then a height-two intersection of the same two positive-degree forms, hence a regular sequence. The fiberwise regular-sequence flatness criterion gives A-flatness of O_Z and the relative regular sequence; see [Stacks, Lemma 10.99.3, tag 00MG](https://stacks.math.columbia.edu/tag/00MG). Alternatively, generic flatness followed by a principal-open shrink suffices, and leaves the identities intact. End of proof.

The fixed Hilbert polynomial is

\[
P_Z(n)=de\,n+de(4-d-e)/2.
\tag{16}
\]

Generically defined conormal quotients can also be spread after enlarging A and shrinking: descend the morphism to O(l) on P¹_A, then remove the proper image of its nonsurjectivity locus. Properness of C_A makes that image closed, and the kernel is then a line bundle. This is an existence statement after localization; it gives no control over which residue characteristics survive. A primitive triple that actually exists over k can similarly be spread, but that does not mean its flat closure is primitive over every originally chosen special point.

Over a general finite-type integral Z-algebra, the locus removed by shrinking is a proper closed locus, **not necessarily finitely many points or rational primes**. In particular, A[1/2] is always another valid spread of the same characteristic-zero data. Therefore no existence theorem for a spread can force a characteristic-two fiber. Nor does a finite-type coefficient ring supply a map to Z_(2) or Z_2: coefficient fields, transcendental parameters, residue fields, and possible ramification all matter.

### Direct reduction to Z4 is numerically impossible for a surviving pair

By R0001 and its accepted lower-degree/factor consequences, d,e are at least five; by (2), four divides de. The smallest possible product is 36, from (6,6), so

\[
m\ge9.
\tag{17}
\]

The prescribed Z4 has degree 16 and generic multiplicity four. A flat complete-intersection family of degrees (d,e) specializing to it must satisfy equality of (16) with 16n-32. This forces de=16 and d+e=8, hence d=e=4. Thus the **whole** intersection scheme of a hypothetical surviving STCI pair cannot specialize flatly to Z4. This degree obstruction is independent of its arithmetic nonlifting.

Extracting a degree-16 intermediate structure would avoid that particular degree mismatch, but requires a global primitive fourth stage, a compatible integral extension of that stage, and the exact marked special fiber. None is forced by an arbitrary STCI. Counterexample C shows why generic primitive stages are not enough.

### Conditional arithmetic corollary — proved under explicit model hypotheses

Suppose a hypothetical characteristic-zero pair admits a model over R=Z_(2) or Z_2, in the fixed relative quartic embedding, such that the total support is C_R, the family is flat, its first-normal image is a line subbundle at every point of C_R, its generic multiplicity is at least three, and its induced quotient reduces to the distinguished q0 of the marked arithmetic problem. Then this model cannot exist.

Indeed Proposition B gives a relative primitive triple. Its canonical extension (1) must split over R. The audited full admissible-quotient calculation gives middle coefficient 2 modulo 4 for every integral quotient reducing to q0, contradicting such a splitting. This rules out a particular kind of *good marked reduction*, for any multiplicity at least three. It does not assert that a hypothetical characteristic-zero STCI must possess such a model. For a total special fiber equal to prescribed Z4, the independently stronger full nonlifting statement is precisely the promoted R0012, with its two-DVR limitation.

Flatness cannot be omitted in descent arguments. Over a DVR, generic containments extend to the total scheme when the target quotients O_Z and O_C are torsionfree, but quotient flatness is what also identifies the base-changed ideal with the actual special-fiber ideal via Tor vanishing. An ideal itself is torsionfree without its quotient being flat: (2x,x²) in Z_2[x] is an elementary counterexample.

## 6. Outcome, audit boundary, and the next mathematical target

**Proved in this report:** the defect-twisted necessary condition (6); the q0 common-zero divisor restriction (9) and its exact degree-two incidence; automatic first-stage vanishing for epsilon at least two; the all-points sufficient bridge to a triple contained in Z; the projective integral-surface counterexample to generic globalization; and the support-preserving spreading/degree statements.

**Conditional:** the arithmetic exclusion of an everywhere rank-one model over either exact unramified base with the specified marked ribbon reduction. It uses the audited relative coefficient calculation and supplies no such model for an arbitrary characteristic-zero pair.

**Open:** whether the actual homogeneous surface symbols of any surviving pair force a direction and divisor violating (6); whether C0-specific geometry forces stronger global intermediate stages despite Counterexample C; all entirely-thick interfaces not covered by existing scoped results; and the unrestricted characteristic-zero STCI question. No new unconditional carrier-degree exclusion is claimed.

The most focused next step on the order-one branch is to impose (6) on the *actual first-normal symbols* (5), together with their global lift conditions, rather than classify arbitrary ribbons. For epsilon=1 this is a finite-dimensional incidence between the quotient q, the common-zero divisor D of those symbols, and the Serre-dual functional (11). A proof that all actual surviving pairs violate that incidence would be an exclusion. The present report establishes the incidence as necessary and gives one exact restricted-direction obstruction; it does not establish the missing actual-pair classification. For epsilon at least two, the first Yoneda stage is identically insufficient, so a later-stage or independent geometric condition is required.

Independent checks were supplied during this investigation by the structural-audit worker for Propositions A/B, the projective counterexample, and the q0 Serre-dual bound; a separate spreading-audit worker reconstructed Proposition D and checked the fiberwise flatness reference. These checks do not promote the report. The independent audit's stable path should be consulted when attached by the coordinating report.

Reproducible calculation:

```text
python3 research/computations/verify_z4_stci_consequences_2026_10_21.py
```

This standard-library script checks the exact q0/q1 cubic values, the evaluation-conic determinant, obstruction-group dimensions, the integral-quadric ideal identities and ranks, nilpotence in the degeneration example, and the finite minimum/CI Hilbert-polynomial arithmetic. The geometric proofs above carry the global statements; a script PASS is not a substitute for them.
