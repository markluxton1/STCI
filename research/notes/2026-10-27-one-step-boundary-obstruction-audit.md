# Independent audit: one-step boundary and final Gorenstein obstruction

Date: 2026-10-27. Reviewer: independent `equation_budget_audit` agent.
Status: mathematical reconstruction of the [source note](2026-10-27-one-step-boundary-obstruction.md),
not canonical promotion. No new unrestricted STCI exclusion or realization
of an unclassified family is certified.

## Scope and method

The reviewer read research/INDEX.md first, then the minimal spectral and
first-normal premises. The source's final saved text was read, including
the refinement that the source determinant is automatic after full
Gorenstein admissibility and the stated cohomology vanishings.

The base setting is a smooth connected projective curve C in a smooth
threefold X over an algebraically closed field, and an embedded pure CM
lower thickening Y with sole support C and generic curvilinear length
n>=2. The arguments are characteristic independent except for the
explicit characteristic-zero conormal description of C0.

Accepted saturated pairings and the promoted first-normal bound R0019
are premises, not rerun proofs. The reviewer independently checked the
new equation-module constructions, extension argument, converse,
source criterion, and coefficientwise divisor comparison. No isolated
example or finite sample was used to infer a family statement.

## 1. The equation module and its power line

For J=I_Y, M=(J/IJ)/torsion is a rank-two vector bundle on C: the
generic ideal is a curvilinear two-generator complete intersection,
and torsion-free coherent sheaves on a smooth curve are locally free.
The first-symbol map has rank-one image R(-B_Y).

Purity proves I^n O_Y=0 from generic nilpotence. Therefore I^n subset J
and I^(n+1) subset IJ, giving Sym^n E -> M. Its generic kernel is
R Sym^(n-1)E, and this entire subbundle maps to zero because M is
torsion free. The quotient L^n maps injectively. Its saturation Ubar
is exactly the kernel of the first-symbol map, yielding the source's
sequence (1) and actual inclusion divisor A_Y.

This construction retains the embedded ideal. It is not determined
solely by the ranks and degrees of the ordinary normal layers.

## 2. One-step extensions and their exact obstruction

An extension by the O_C-line T=L^n(D), killed by I, induces a map
J/IJ -> T. Its torsion-free target makes it factor through M. Extending
the prescribed map L^n -> T first to Ubar=L^n(A_Y) is possible exactly
when A_Y<=D, and then that map is uniquely the natural inclusion.

Applying Hom(-,T) to 0 -> Ubar -> M -> V_Y -> 0 shows that extending
this inclusion to all of M is equivalent to vanishing of the pushout
of e_Y. Naturality of Ext identifies the pushout with the map

    H^1(Ubar tensor V_Y^vee)
      -> H^1(Ubar tensor V_Y^vee(D-A_Y)).

Thus the source's available repair divisor D-A_Y and its torsor
H^0(V_Y^vee tensor T) are correct. It would be incorrect to use all of D
as new repair allowance after A_Y has already been used in saturation.

For the converse, a surjective q:M -> T gives the ideal kernel of
J -> M -> T; it contains IJ. The resulting sequence
0 -> T -> O_Z -> O_Y -> 0 is CM of dimension one by the depth lemma.
The ideal T is square zero because J^2 subset IJ. Generic nonvanishing
on y^n makes the generic quotient the curvilinear extension of length
n+1. Since O_Y is pure, T is saturated in O_Z and is the final
saturated layer. The prescribed ordinary multiplication is the map
L^n -> T. This verifies the exact converse stated in section 2.
Surjectivity is automatic when D=A_Y; otherwise it is an additional
condition at the finite vanishing divisor of Ubar -> T.

## 3. The final Gorenstein step and the full converse

For a genuine final Gorenstein completion, the map q:M -> T is
generically injective on Ubar. Multiplying ambient representatives of
W_1 and W_(m-2) defines the source's map j into Ubar. Changes of lifts
give zero generically in J/IJ and hence zero in the torsion-free M;
the source's argument using q and the saturated product also verifies
the same fact without assuming a global coefficient retraction.
The composite qj is the inherited perfect top pairing. It follows that
q|Ubar is an isomorphism, and normalizing by it gives a retraction of
Ubar in M. Hence e_Y=0. Compatibility with the ordinary power maps
identifies A_Y with D_soc as an actual divisor, not merely by degree.

For arbitrary fixed lower Y, the maps

    j_i:W_i tensor W_(n-i) -> Ubar, 1<=i<n,

are indeed canonical. Products vanish generically in O_Y, so purity
puts them in J. Changes of representatives lie generically in IJ;
their classes therefore vanish in M. This also proves O_C-linearity.
The products have zero first symbol and thus land in Ubar. Composing
with the ordinary maps from L^i and L^(n-i) yields the degree-n power
map, proving the ACTUAL divisor formula

    div(j_i)=A_Y-D_i-D_(n-i).

Necessity of e_Y=0 and zero divisors of every j_i follows from a
Gorenstein completion. Conversely, a retraction q constructs a pure CM
completion with top Ubar, and the old saturated lower layers are
preserved. If every j_i is an isomorphism, its top pairings are perfect.
Locally over a lifted parameter DVR, a basis adapted to the saturated
flag gives a Frobenius Gram matrix: entries beyond the antidiagonal
are zero and antidiagonal entries are units. A top-coefficient
functional is therefore perfect, proving the completion Gorenstein.
This independently verifies the source's iff criterion (3a).

The m>=3 restriction is correct. When the lower scheme is C itself,
its conormal E need not split; that case is outside the rank-one
first-symbol setup used here. Under the final Gorenstein pairing,
the top ideal is contained in K^2, so passing to the penultimate level
does not add first-order relations. The equality of the two first-symbol
divisors is therefore justified in this scope.

## 4. Exact actual-source determinant and its limits

At eta_C, J has two minimal generators and M_eta=J_eta/m J_eta.
The determinant of two actual carrier sections is nonzero exactly when
their classes span this space, which by Nakayama is equivalent to
generating J_eta. Their generic length is then n. If the determinant
vanishes, their ideal is strictly smaller, so a proper pair has generic
length at least n+1. Under ab=(n+1)deg C, Bezout makes this equality
and exhausts degree; purity leaves no residual curve or embedded point.
This proves the exact source criterion, including the residual degree d
when the determinant is nonzero.

The Segre/Grassmannian description uses actual global section spaces,
so its unknowns are constants in k. No generic formal-symbol surrogate
has been substituted. A generic nonzero determinant does not exclude
its exceptional zero locus, as the source explicitly records.

The conditional dimension assertion is valid for the nonempty Segre or
Grassmannian source: a section by r ambient linear equations is
nonempty when dim P>=r, and has dimension at least dim P-r. A closed
improper locus of larger codimension cannot contain it. The source
makes no unjustified general estimate of that improper locus.

## 5. Small target and the essential automatic-vanishing refinement

On the top-adjunction-admissible locus, det M=Ubar tensor R(-B_Y)
and Ubar=omega_C O_C(4-a-b) give exactly

    det M tensor O_C(a+b)=L^(-1)(-B_Y).

For C0 in characteristic zero, 1<=q<=7 gives the claimed target
dimension at most eight. This is an upper bound on the source contact
equations, not automatically a set of eight nontrivial conditions.

The source's later refinement is necessary and correct. Once a global
retraction q:M -> T exists, the quotient of any actual degree-a
section through Y is a section of T(a)=omega_C O_C(4-b), and similarly
for degree b. If both cohomology spaces vanish, every such section
already vanishes on the completion. Therefore Theta is identically
zero on this source, with no further determinant obstruction.
For C0 and a,b>=4 the bundles have degrees 14-4b and 14-4a, so the
vanishings hold. This statement is also valid for any smooth curve
satisfying the source's two displayed cohomology vanishings.

For two nonzero section spaces over an infinite field, existence of
a coprime pair is equivalent to absence of a common fixed irreducible
surface. The finite-union-of-proper-linear-subspaces argument in the
source proves the nontrivial direction exactly: choose F avoiding all
fixed factors of H_b, then G avoiding every irreducible factor of F.

Consequently the exact fixed-lower realization criterion is valid in
the stated range. For sufficiency the constructed completion has degree
ab, and all source sections vanish on it. A proper CI containing it
has the same cycle; its kernel over the completion is a punctual
submodule of a pure CI structure sheaf and is zero. Thus the schemes
are equal. This does not classify all admissible Y or supply a proper
pair in an unclassified family.

### Final source refinements: socle quotients, curvilinearity, and rigidity

The final saved source contains three further consequences, which the
reviewer independently checked. They do not require a sampled example.

First, for any Gorenstein multiple structure Z with smooth sole support,
its socle Ann_(O_Z)K is the O_C-line omega_C tensor (omega_Z|C)^(-1)
by finite duality. It is saturated: locally a lifted curve parameter t
is a nonzerodivisor, and tb in Ann K implies t(bK)=0 and hence bK=0.
The quotient by this socle is therefore pure CM. For rational C and
omega_Z|C=O_C(s), the line T(d)=omega_C O_C(d-s) has negative degree
whenever d<=s. Its H^0 vanishes, so the ideal exact sequence proves
H^0(I_Y(d))=H^0(I_Z(d)). This source collapse does not use generic
curvilinearity. The rank-two classification of its possible completions
does still use that separate hypothesis.

Second, in the necessity direction of the exact realization criterion,
a generic Artin Gorenstein CI algebra mapping onto the curvilinear
length-one-shorter algebra has a length-one kernel. Such an ideal is
the socle. In length at least three that socle lies in the square of
the maximal ideal: if m^2=0 and the length were at least three, the
socle would have dimension at least two; otherwise the last nonzero
power m^s, s>=2, is already the unique socle. Quotienting by it
preserves embedding dimension. Since the quotient is curvilinear,
the original algebra is curvilinear too. Purity then identifies the
lower Y with the saturated penultimate truncation.

Finally, the completion torsor has distinct embedded ideals for
distinct normalized retractions. Indeed two surjections with the same
kernel differ by an automorphism of the target line, and their
restrictions equal the identity on Ubar, forcing that automorphism
to be the identity. Under (4b), all actual degree-a and degree-b
sections through Y vanish on every such completion. A single proper
pair would contain every completion; equal degree and purity would
make all of them the same scheme. Thus an actual CI in this range
requires H^0(V_Y^vee tensor Ubar_Y)=0. On P1 this is equivalently
deg Ubar_Y<deg V_Y, exactly as in (4c). It is only a necessary
rigidity condition, and the source does not assert sufficiency.

All three final refinements pass audit with their stated hypotheses.

## 6. Actual equation-module and spectral divisor accounts

For an actual CI of generic curvilinear length m, purity gives
I^m subset J_full and I^(m+1) subset IJ_full. The same power-line
argument yields F^m D_eq=L^m and F^(m+1)=0. Also F^2 is the line
kernel of the first-symbol map D_eq -> R(-B_full).

The coefficientwise inclusion divisor needs the source's multiplicative
Tor argument; determinant line-bundle isomorphisms alone give only a
class or linear equivalence. The reviewer independently reconstructed
that argument. A normal Koszul cycle for y^m is (0,y^(m-1)), while
f=Ax+By gives (A,B). Their product is, up to sign,
(A|C)y^(m-1) times the normal determinant frame, because the top power
annihilates the nilradical. Carrier Tor identifies this with the wedge
in D_eq, and normal Tor_2 is the socle times det E. Thus the actual
zero divisor is D_soc+B_full.

Intermediate equation quotients are torsion, and telescoping gives
sum div G_r=D_soc+B_full. The R0019 first-normal divisor is the image
of the TOTAL ideal of the multiple structure, hence equals B_full;
its bound applies here without the auxiliary-surface hypotheses of
its separate residual-cycle assertion. This verifies the bound by
2 D_soc in the specified finite-flat/saturated setting.

Generic curvilinearity makes Delta generically zero, so the reviewed
torsion comparison gives the source's equality

    sum div tors Q_r=D_soc+B_full+sum div Delta_r.

The 2 D_soc bound does not apply to raw initial-equation torsion
without subtracting Delta. The source preserves the unresolved
punctual-Delta question and does not claim to settle it.

## Outcome

**PASS for the inspected source, including the automatic-source refinement.**
No substantive correction is required. The explicit one-step lifting
comparison and its final Gorenstein sharpening are independently
reconstructed. The exact contact criterion and fixed-surface reduction
apply to a whole fixed lower embedding, without sampled examples.
The source does not prove that the admissible lower-embedding family
has a proper source point or that its fixed-surface condition always
fails. Those remain the global classification question.

All new claims remain reviewed provisional research evidence. The
audit does not promote a canonical result or reopen an accepted
exclusion. No inherited certificate or proof was replayed.
