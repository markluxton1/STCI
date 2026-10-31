# Independent audit: globally ADE quintic exclusion

Date: 2026-10-31. Reviewer: continuing independent mathematical-review
subagent; no nested delegation.

**Disposition: accepted as independently reviewed provisional mathematics.
No unresolved material finding. No canonical promotion.**

## Exact reviewed claim and state

Reviewed all seven sections of
[the focused note](2026-10-31-quintic-octic-ade-exclusion.md), including
its displayed local covers, five replacement types, four-row reduction,
actual symbolic-triple calculation and endpoint obstruction. The accepted
claim concerns the fixed characteristic-zero quartic
`C=[s^4:s^3t:st^3:t^4]`: a proper degree-(5,8) intersection with sole
reduced support C cannot have a quintic with only rational double points
everywhere. Reducedness of either first-symbol divisor is not assumed.
No singularity hypothesis on the octic is added.
The final review includes the explicit section 3 connectedness/Serre
normality clarification, the preceding note's revised section 8 linking
this stronger result, and the short INDEX navigation entry. Those scope
updates correctly distinguish the additional proof from the original
rank/even-set stage and preserve the open status of the entire degree pair.

The earlier
[fixed-singularity note](2026-10-31-quintic-octic-fixed-singularities.md)
and [audit](2026-10-31-quintic-octic-fixed-singularities-audit.md) supply
reviewed conormal, genus, first-symbol and quintic-resolution inputs.
R-0001 and its factor/lower-degree reduction, R-0020, and those reviewed
inputs remain accepted premises; their inherited proofs were not rerun.
I inspected the source local tables and the precise embedded-triple
calculation described below. The former reduced-symbol hypothesis is
removed by the new argument, rather than silently omitted from its old
proof.

## Cover existence, singularities and invariants

The actual Cartier relation `10C~8H` implies that `T=5C-4H` has order
dividing two in the Weil class group. Its order is exactly two: a trivial
class would produce an effective `5C~4H`, and the hypersurface sequence
lifts its section to an ambient quartic mate, contradicting the accepted
low-degree exclusion.

The reflexive algebra `O_S direct_sum O_S(T)` uses the reflexive product
and the chosen trivialization of `O_S(2T)`. After rational trivialization,
its function-field equation is a square root of a function with divisor
twice a representative of T. A square would make T principal, so its
generic extension has degree two and is connected. This also explains
connectedness independently of a local table. The algebra is already
normal: its reflexive summands are S2 on the normal surface, and it is
étale in codimension one, hence R1. Serre's criterion applies. Equivalently
one can normalize the cyclic field extension and identify its two
eigensummands with these reflexive sheaves. Thus normalization adds no
unaccounted branch divisor or component.

At a locally trivial class the cover splits analytically into two copies.
At a nontrivial class the displayed covers are ADE. Independently checked
the A cover as `XY=z^(N/2)`, with base coordinates `x=X^2,y=Y^2,z=z`;
the deck involution negates X and Y. The vector-D, even-spin-D and E7
normalizations in section 4 follow by the stated square-root substitutions
and cancellation of the common square. The resulting normal hypersurfaces
are respectively `A_(2n-5)`, `D_(n/2+1)` and E6. Their involutions have
only the origin fixed. These are the correct order-two characters of the
marked curve classes, not arbitrary double covers of the same surface.

Canonical pullback is valid because the finite cover is quasi-étale and
both surfaces are Gorenstein; the ADE resolution is crepant. Hence its
smooth resolution W has nef and big canonical divisor and `K_W^2=10`.
This proves minimality and general type, rather than presuming them.

The Euler calculation is exact. Resolving a rank-r ADE point replaces one
point by a tree of Euler number `r+1`. A nontrivial local cover has one
point above it, whereas a locally split cover has two. Consequently the
loss from twice the resolved base Euler number is `2r-r'+1`, and

    chi(O_W) = 10 - sum((2r-r'+1)/12) = 10-w/4.

The local weights are `N/2` for a nontrivial A cover, two for vector D,
`n/2` for even spin D, and three for E7. Trivial local covers have weight
zero. T is locally Cartier off C, so every off-C ADE point cancels from
this cover calculation. Such points can still consume base exceptional
rank; the proof correctly allows for that.

## The canonical-map bound is stronger than Noether alone

Invariant canonical forms descend on the smooth étale locus and extend
reflexively across the finite ADE locus. This identifies their space with
the four-dimensional canonical space of the quintic. Ratios of those
sections generate `k(S)` because the canonical system of the quintic is
its given hyperplane embedding. If `p_g(W)>4`, an anti-invariant section
divided by a nonzero invariant section is a noninvariant rational function.
It generates the quadratic extension, so the full canonical map is
birational. This is a function-field argument and does not require its
image to be smooth.

For the birational case Debarre's Proposition 3.1 with `L=K_W`, and the
bicanonical formula for a minimal general-type surface, give

    4*p_g-6 <= h0(2K) = K^2+chi,
    3*p_g+q_irr <= 17.

Thus `p_g<=5`. The case `p_g<=4` already satisfies this bound. Since
`chi=1-q_irr+p_g<=6`, it follows that `w>=16`. No vanishing of the
irregularity is imposed. This step supplies real additional evidence:
for example the local numerical tuple `3A1^1+7A4^1+A9^3` passes the
basic base budgets and Noether-only cover test with w=8, but fails this
canonical-map bound. A Noether-only uniform exclusion would be invalid.

## Classification, domination and four survivors

Checked the primary text of
[Jaffe's paper](https://arxiv.org/pdf/alg-geom/9410008): Theorem 4.1
classifies the smooth-curve ADE pairs; Propositions 5.2, 5.3 and 5.7 give
the first orders, indices and pullback corrections used here. These inputs
concern every smooth curve germ in the stated ADE scope. They do not
justify restricting to end-marked A points alone. The explicit D/E cover
derivations are new local checks in this proof, not attributed to Jaffe's
tables. D4's equivalent arms are correctly counted through the vector row.

Since the curve index divides ten, the A pairs have index two, five or
ten. Writing `N=rc,k=ac` gives exactly the five families in the note.
For each family I verified preservation of s, Delta and w under replacing
it by c base copies, and the rank excess `c-1`. The D/E replacements
also preserve all required quantities and have strictly positive rank
excess. No replacement is asserted to be a deformation or a realization.

The global budgets are `sum Delta=46/5`, `sum s=q+6`, and actual root
rank at most 44. With the five base counts, direct elimination gives

    u=3(x+v)+4z-8q+44,
    R0=244-36q+12(x+v)+16z,
    w=x+5(u+v).

Independently checked the elementary enumeration, including an ephemeral
integer-arithmetic cross-check with no saved code artifact. There is no
q=5 row. The sole q=6 rank-compatible row is `(0,10,1,0,0)`, of weight
zero. For q=7, imposing `w>=16` gives exactly rows I–IV as displayed.
Each has at most one base A1, excluding every pre-replacement D/E pair.
Rank-44 rows cannot have any positive rank excess. In rank-40 rows only
the stated coalescences of A4^1 or A9^3 blocks remain; their integer
partitions and any off-C rank consumption are all covered by the next
calculation. No assumption of equality between replacement and actual
rank was used.

## Actual symbolic triple and obstruction

The symbolic triple is intrinsic to the actual quintic: the equation of
`10C` belongs to `I_C^(3)`, so it contains `C_3`. The symbolic ideal is
the contraction of the generic third power, not the ordinary third power.
Its quotient is the actual pure Cohen–Macaulay triple. Its saturated first
line is the same L, since its generic direction and saturated conormal
kernel agree with those of Y.

For the marked A equation, the generic expansion is precisely

    v = -t^(N-2k)*u + t^(N-3k)*u^2 modulo u^3.

The exact image of the completed local ring in `k((t))[u]/(u^3)` is
generated by this v and u. Because `N-2k>=0`, its lattice has basis
`1,u,t^min(0,N-3k)*u^2`: the generator
`v+t^(N-2k)*u` supplies the second possible last-layer coefficient,
and no word supplies an additional denominator. Thus the calculation is
the full image algebra, not a chosen sublattice. The canonical
multiplication from `L^2` has vanishing order `max(0,3k-N)`.

This is the saturated-layer divisor D2; it is not ordinary torsion,
the first-symbol divisor, or the bookkeeping number d. It gives the four
total degrees `1,0,2,1` even after every allowed rank-40 coalescence.
In row III the two contributions arise at distinct A1 and A4^2 points;
they cannot coalesce without forbidden rank excess.

I inspected section 2 of the
[MF6 further audit](2026-10-05-mf6-further-audit.md) and its referenced
verifier source, and independently reconstructed the low-degree killing
matrices from the displayed cocycle. The inherited moving-chart cocycle
is reused at its exact constant-direction scope; no inherited executable
certificate was rerun. Its finite-direction `z^-2` coefficient excludes
degree zero. The stated two-row determinant is `-9/64` for degree one;
the degree-two three-row determinant is `-27*theta^4/32`. The only
remaining kernels are the pure-direction sections with a double zero at
one endpoint, including the missing direction's double zero at infinity.
These necessities apply to nonprimitive and non-lci embedded triples.
The flat endpoint triples are retained, not falsely excluded.

All four rows have q=7, hence a constant saturated conormal kernel. Rows
I, II and IV violate the degree-zero/one necessity. Row III instead has
two distinct simple defect points, incompatible with the necessary double
endpoint. No assertion that all degree-two triples are impossible, and
no quartic-specific membership calculation or `deg D2>=3` theorem, was
imported. R-0033 alone would not supply this positive-defect exclusion.

## Sources, findings and final scope

Checked the actual
[Debarre paper](https://www.numdam.org/item/10.24033/bsmf.1965.pdf),
Proposition 3.1 and the bicanonical application leading to Theorem 3.2,
printed pp. 325–326. The stronger irregular theorem addressed by the
[1983 addendum](https://www.numdam.org/item/10.24033/bsmf.1990.pdf) is
unused. The source qualification in the focused note is correct.
Characteristic-zero descent of the hypothetical pair and finite defining
data permits the complex analytic and Hodge arguments; no uncountability
assumption or new ground-field restriction is needed.

No material mathematical correction remains. The lead adopted the
recommended connectedness and normality clarification for the reflexive
cover algebra, and I checked the final wording; the argument above also
supplies those steps independently. The final chain
excludes every globally ADE quintic under the fixed (5,8) sole-support
hypothesis, including repeated first-symbol zeros. This is stronger than
the previous reduced-symbol result and uses additional independently
checked evidence. It does not exclude a quintic with a non-ADE
singularity, prove that such a carrier exists, address neighboring
degrees, or settle unrestricted STCI. No canonical record is promoted.
