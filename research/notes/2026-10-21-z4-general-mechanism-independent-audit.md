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
[intrinsic independent audit](2026-10-21-intrinsic-ribbon-triple-independent-audit.md).
The general intrinsic construction is reviewed evidence, not a promoted
canonical result. The previously audited quartic Laurent polynomial is
an imported input; this review does not reconstruct its rational ambient
chart expansion.

The new targets are the
[characteristic-zero report](2026-10-21-z4-characteristic-zero-stci-consequences.md),
the [arithmetic-mechanism report](2026-10-21-z4-intrinsic-divided-power-mechanism.md),
and the [quadratic-gluing comparison](2026-10-21-z4-quadratic-gluing-comparison.md).
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
[comparison supplement](2026-10-21-z4-quadratic-gluing-comparison.md).
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
