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
[independent intrinsic audit](2026-10-21-intrinsic-ribbon-triple-independent-audit.md).

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
[general-mechanism audit](2026-10-21-z4-general-mechanism-independent-audit.md).
All new claims remain research evidence; no canonical result is promoted.
