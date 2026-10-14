# Accepted research frontier — 2026-10-14

This is the continuation entry point after the October 13–14 structural
generalization batch. The universal integral-projective-curve STCI question
and the unrestricted characteristic-zero problem for
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. No new novelty or priority claim is
made. The results below are written mathematical theorems under their
stated hypotheses, not a claim that all possible carriers are covered.

The user directed that previously verified statements be assumed correct.
Accordingly accepted proofs and certificates were used as premises; new
review was confined to new arguments, pending claims and scope bridges.
The [previous state](AUDITED_STATE_2026-10-07.md) preserves the inherited
proof history. This file supersedes its conflicting continuation labels.

## 1. Complete branch reconstruction and inherited closed lanes

The [all-branch inventory](notes/2026-10-13-evening-branch-frontier-audit.md)
and [reconciled frontier map](notes/2026-10-13-generalization-frontier-map.md)
cover every observed local/cached ref and all seven branches in the live
GitHub inventory, including four research heads absent from cached origin
refs. Twenty-five recovered sources retain exact branch, blob and path
provenance. They were archived without merging divergent authority schemes.
Remote main's older mathematical labels do not reopen accepted results.

Accepted inherited conclusions include:

- Every integral quartic carrier of fixed characteristic-zero C0 has no
  mate in any positive degree. Both degrees of a hypothetical STCI pair
  are therefore at least five.
- The genus-one quintic intrinsic endpoint projection family, coprime
  nonendpoint conormal pairs, `G=Jbar=0`, and residual partitions `2+4`
  are excluded in all mate degrees.
- The completed [October 13 cubic-pair audit](notes/2026-10-13-session-nonendpoint-cubic-pair-full-independent-audit.md)
  is now accepted: the entire residual partition `3+3`, including the
  doubled-cubic case, has no mate. The stronger support obstruction
  applies only to `Jbar!=0`; at `Jbar=0` the separate all-power argument
  proves the no-mate conclusion. Older “audit pending” labels are stale.
- The actual conductor quadric and full binary octic, homogeneous gcd
  rank/cover classification, pole/line and target-fiber arguments retain
  their already accepted scopes. The integral residual is still open.

The positive-characteristic constructions and literature corrections are
inherited from the [October 13 source refresh](notes/2026-10-13-evening-literature-refresh.md).
This continuation did not repeat that search. Neither restricted monomial
or cuspidal results nor invalid affine claims resolve the universal
projective question.

## 2. Exact fixed-carrier criterion, all branches and all characteristics

**PROVED with independent new-proof audits:** let an integral
Cohen–Macaulay projective surface have finite normalization `S`, ample
hyperplane pullback `H`, and full reduced inverse support
`Gamma_1 union ... union Gamma_s` of the integral curve C. Isolated
inverse points outside these components prohibit a mate. Otherwise define

```
Lambda = ker[ Z^(s+1) -> Cl(S) ],
(n,d) |-> sum n_j[Gamma_j] - d[H].
```

Send this lattice to the **full** conductor unit quotients at generic
conductor curves away from C, and kill the non-torsion image to obtain
`Lambda_desc`. A mate exists on the chosen hypersurface **if and only if**
this lattice contains a vector positive on every inverse branch.
Vanishing on all branches above C enters the actual conductor after a
power; Cohen–Macaulay depth promotes actual generic membership to global
descent. No almost-Cartier class for reduced C is assumed in thick cases.

The positive lattice cone has a finite support-covering criterion, with
fixed-carrier power and degree bounds once its class/unit relations are
computed. This is an abstract finite reduction, not an effective
algorithm for arbitrary surfaces and not a uniform bound across carriers.

In characteristic zero the nilpotent conductor-unit kernel is a
uniquely divisible vector group. A given unit eventually descends exactly
when its residual class is torsion **and** its logarithmic nilpotent
defect vanishes. Once eventual descent holds, nilpotents add no exponent.
A single residual field has exponent dividing its actual extension
degree. Split fields add relative root-of-unity phases whose orders can
be unbounded even with fixed ring lengths. In characteristic p the
nilpotent obstruction is killed by a further p-power, but function-field
residual ratios need not be torsion.

For a singleton branch and a carrier generically regular along C, put
`a=H^2`, `c=H.Gamma`, `g=gcd(a,c)`. If the primitive class
`(a/g)[Gamma]-(c/g)[H]` has order t and its base section has conductor
class order E, then the mate degrees are **exactly**
`k t E c/g`, `k>=1`; a mate exists precisely when both orders are finite.
For torsion-free `Cl(S)`, the upstairs base degree is `c/g<=c`,
independent of the carrier degree. For degree-four C0 with a degree-one
lift, these base degrees are `1,2,4`.

Proof and audit record:
[conductor theorem](notes/2026-10-13-generalization-conductor-theorem.md).

## 3. All-degree classification with a Cartier singleton lift

**PROVED, independently audited:** for a smooth rational degree-d curve,
a mate on a carrier with normal finite normalization S and full singleton
inverse curve `c` mapping isomorphically to C, **Cartier on S**, forces
`(S,c)` to be a normal minimal-degree surface with its hyperplane section.
The smooth-normalization theorem is the earlier special case. The complete
possibilities are:

| Normalization and lift | Pullback H | Carrier degree |
|---|---|---:|
| P2, c a line | O(d) | d^2 |
| P2, c a conic, d even | O(d/2) | d^2/4 |
| Smooth rational normal scroll of degree n dividing d, c its hyperplane section | (d/n)c | d^2/n |
| Rational-normal cone of degree n dividing d, c its smooth Cartier hyperplane section | (d/n)c | d^2/n |

For C0, accepted quartic exclusion leaves exactly three higher models:
`a=8, S=P1 x P1, H=(2,2), c=(1,1)` and
`a=8, S a quadric cone, H=2c, c a Cartier conic`, and
`a=16, S=P2, H=O(4), c a line`. Their actual projection parameters,
full inverse support and conductor descent remain to be solved.
Generic regularity is sufficient for the singleton hypothesis but is
not required once that hypothesis is supplied. Non-Cartier lifts,
multiple lifts and lifts of degree greater than one remain outside this
classification. Thus every other mate-admitting generically regular
C0 carrier must have a non-Cartier point upstairs; no bound on its
Cartier index has been supplied.

Proof: [carrier framework](notes/2026-10-13-generalization-global-carrier-framework.md).
Independent audit: [smooth-normalization audit](notes/2026-10-13-generalization-smooth-normalization-independent-audit.md).
Extension: [Cartier-lift theorem](notes/2026-10-14-generalization-cartier-lift-minimal-degree.md)
and [independent audit](notes/2026-10-14-generalization-cartier-lift-independent-audit.md).

**PROVED in every characteristic:** if a smooth degree-d genus-g curve
is Cartier on an integral hypersurface carrier admitting a mate, that
carrier is normal and
`a | d^2`, `2g-2=d^2/a+(a-4)d`. Hence
`a<4+(2g-2)/d`, a finite bound within this Cartier-downstairs lane.
For a smooth rational curve the only possibilities are a plane line
or conic, or a quadric conic. Every smooth rational curve of degree
at least three therefore must be non-Cartier on every integral
mate-admitting carrier. Cartier upstairs on a nonnormal carrier is
a different condition and is allowed in the three C0 models above.

### Normal carriers: torsion and bounded local index

**PROVED, independently audited:** every normal C0 carrier with
torsion-free Weil class group is excluded in every degree. In general,
if a mate exists and R is the least common multiple of the actual
local Cartier indices of C0 along the normal carrier, put
`g=gcd(a,4)`. Then the primitive class has exact order and minimum mate
degree

```
t=R/gcd(R,a/g),   b_min=(4/g)t,   a |16R.
```

A self-contained cyclic-cover theorem detects all torsion along an
ample smooth rational curve; a separate hypersurface Picard theorem
extends the formula to arbitrary integral support. For every integral
degree-e curve on a normal characteristic-zero hypersurface admitting a
mate, with `g=gcd(a,e)`, one has
`b_min=(e/g)R/gcd(R,a/g)` and `a | e^2 R`. If all actual local indices
divide a fixed common exponent L, then `a | e^2 L` and `b_min<=e L`.
This is a finite reduction across all carrier and mate degrees within
that index class; no universal index bound has been proved.

For C0 the following complete all-degree consequences are accepted:

- Every normal carrier with only ordinary nodes along C0 is excluded.
  Normal singularities away from C0 may be arbitrary.
- Every normal carrier whose on-curve indices divide 2,3,4 or6 is
  excluded.
- If the on-curve indices divide12, the only surviving arithmetic rows
  are `(a,R,t,b_min)=(6,12,4,8)` and `(8,12,6,6)`. These give the single
  unordered defining degree pair `(6,8)`, with generic length12. This
  includes D/E rational double points and A1,A2,A3 mixtures along C0.
  At least one carrier has the normal/index hypotheses; the other
  carrier's normality and global primitivity are not inferred.

Finite local indices alone do not prove the primitive class is torsion.
Local class order is also not the ramification index of a normalized
inverse curve in a cyclic cover: the new D4 example has class order2
but two inverse branches each mapping isomorphically. The full inverse
support must be retained. A multiplicity-two A_(r-1) surface can have
a smooth curve of index r, so surface multiplicity supplies no uniform
index bound.

Proof and independent audits:
[normal-carrier torsion theorem](notes/2026-10-14-generalization-normal-carrier-torsion.md).
Only the new finite arithmetic consequences were run in the
[integer companion](computations/normal_carrier_index_reduction_2026_10_14.py).

## 4. Full conormal algebra, socle and strict C0 boundary

**PROVED, independently audited:** for any smooth support C, the entire
complete-intersection thickening has actual socle
`omega_C tensor O_C(4-a-b)`. Its generic Loewy index is a global
nilpotency bound. Retaining all torsion of all normal layers gives the
exact identity

```
n(lambda d - L) = lambda Asym + 2 Delta,
L=deg(C)(a+b-4)-(2g(C)-2),
Asym=nd-2 sum j h_j >=0,  Delta>=0.
```

The slope/quotient bound on the normal bundle is explicit in the proof.
For C0, lambda=7, n=ab/4 and

```
mu=7d+14-4(a+b),    n mu=7 Asym+2 Delta.
```

The equality algebra is a globally constant graded Gorenstein algebra,
compatibly with the actual symmetric conormal map. Its two homogeneous
initial generators give a canonical filtration of the actual generator
bundle; arbitrary higher cancellation of the chosen equations remains
allowed. A new factor-extraction argument in the quadratic ambient
transition requires every factor of the lowest constant binary relation
to have zero primitive-triple obstruction. The accepted C0 direction
classes are all nonzero. Equality arithmetic forces a generator gap at
least two, so **every C0 equality model is excluded, in every degree**:

```
mu>0,  d >= ceil((4(a+b)-13)/7).
```

For the thick `(6,8)` example this improves d>=6 to d>=7. This is a
Loewy-bound improvement, not an exclusion of `(6,8)`.

More generally a unique first relation with no new next-order relation
must pay `Delta_r>=1`. If its generic binary direction is constant
and its entire divisor defect has degree delta, the divisor must
annihilate the obstruction of **every factor**. Thus delta<=1 is
impossible; delta<=3 forces a power of a single direction with the
specified endpoint/mixed annihilator; two distinct factors require
delta>=4. Moving first relations and adjacent new relations remain open.

**PROVED moving-relation cost:** if the saturated unique first binary
relation has direction-map degree epsilon, effective saturation defect
delta, and the next independent generic relation occurs at s>r, then
`Delta>=epsilon(s-r)(s-r+1)/2+delta`. Hence
`n mu>=7 Asym+epsilon(s-r)(s-r+1)+2delta` for C0. This charges moving
directions rather than discarding them. The same saturation argument
works for any smooth support with balanced split normal bundle.
Constant-direction pole bounds require s>=r+2; the gap-cost identity
itself permits s=r+1.
Review: [moving-relation cost](notes/2026-10-14-generalization-moving-relation-gap-cost-independent-audit.md).

Proofs: [full budget](notes/2026-10-13-evening-entirely-thick-rees-progress.md),
[uniform extension](notes/2026-10-13-generalization-thick-equality-extension.md).
Audits: [socle](notes/2026-10-13-generalization-socle-independent-audit.md),
[relation obstruction](notes/2026-10-13-generalization-thick-relation-obstruction-independent-audit.md),
[pole budget](notes/2026-10-14-generalization-first-relation-pole-budget-independent-audit.md).

The independently reviewed local algebra package gives sharp uniform
Loewy and moment bounds at fixed length and initial order, together
with explicit local CI families achieving them. Consequently local
numerical restrictions alone do not rule out arbitrarily high contact.
See [higher moments](notes/2026-10-13-generalization-higher-moment-and-loewy-bounds.md).

## 5. Symbolic ribbons beyond an actual Cartier double

**PROVED, independently reviewed:** on a normal surface with a smooth
degree-one inverse curve c, every symbolic divisorial layer
`O(-ic)/O(-(i+1)c)` is a line bundle, including at surface singularities.
An actual Cartier relation `rc~bH` yields periodicity, an exact Euler
sum and conormal inequalities. If q is the first surviving valuation of
the pulled-back ambient curve ideal and M bounds normal line-subbundle
degrees, then `q deg(C)^2<=deg(X) M`. The first-layer inequality
requires q=1; it is not silently used on thick charts.

For a balanced rational degree-d curve on a degree-d carrier, an actual
Cartier double is excluded when `2pi>d-1`. The criterion is a uniform
theorem; it supplies no uniform Cartier-index bound. The quintic
genus-one example retains the allowed symbolic-ribbon interval and is
not excluded by this argument.

Proof: [symbolic-ribbon criterion](notes/2026-10-13-generalization-ribbon-numerical-criterion.md).
Review: [ribbon review](notes/2026-10-14-generalization-ribbon-independent-review.md).

## 6. Complete finite-pencil replacement for ancestor computations

**PROVED, independently reviewed:** over any field, an affine pencil
`(lambda I_q+A; B)` with `rank B=q-1` and `rank(B;BA)=q` has full-fiber
target exclusion exactly when a normalized polynomial left dual of
degree at most two exists. The incidence reduces to q-2 linear
polynomials and one quadratic. At q=18 this is sixteen linears and one
quadratic. Rank drops have a separate exact rule; parameter-ring and
determinantal fallbacks retain every exceptional stratum.

Proof: [polynomial-dual theorem](notes/generalization-localcoh-dual-lemma.md).
Review: [pencil review](notes/2026-10-14-generalization-localcoh-pencil-independent-review.md).
This does not certify the exact rank locus of every ancestor family.
The remaining degree-fifteen exceptional-field application is under
active new computation; no old tensor verifier was repeated.

## 7. Continuing quintic and ancestor research

**PROVED, independently audited:** in the fixed nonendpoint genus-one
quintic A4 model, the zero-conormal-cubic and lambda=1 proportional
charts have no mate. Every regular finite sole homogeneous common-root
chart with Jbar nonzero is also excluded in all mate degrees. The
previously pending L1 quotient-fiber geometry now has a separate
review; the complete L2 discriminant cover, leading drop and q=2
boundaries have literal original-generator witnesses. All projection
center and complete homogeneous-root hypotheses survive these statements.

The general support lemma replaces a large power-divisibility condition
by root-count and finite multiplicity-partition incidences. In the main
h3 chart, homogeneous infinity, at-least-three-root support and
multiplicity-at-least-four alternatives are accepted. The remaining
3+2 multiplicity pattern has a computed saturated unit ideal but its
literal original six-generator witness is still pending. The whole
h3 claim therefore remains open at that exact certificate boundary.

Proofs: [quintic continuation](notes/2026-10-13-generalization-quintic-continuation.md)
and [regular L2](notes/2026-10-13-generalization-quintic-l2.md).
Independent audit: [new quintic review](notes/2026-10-14-generalization-quintic-new-independent-audit.md).
The singular qZ=0 targets, intrinsic A4 point, target infinity in the
sole-root lane, Jbar=0 and other common-root incidences remain outside
that regular-chart closure. Other quintic normalizations remain open.

The common-quartic-ancestor problem is distinct from an actual quartic
mate. Family-two cubic/quartic field dual outputs, the remaining
degree-fifteen field, boundary three/four, nonendpoint top zeros and
positive-D2 directions retain their precise recorded scope. A failed
large module run is not a negative certificate.

## 8. Global unresolved obligations

The structural results now organize the work by normalization branches,
Cartier relations, conductor torsion and complete filtered normal
algebras. They do not provide:

1. a minimum-carrier degree bound or a theorem forcing smooth singleton
   normalization;
2. a full singular-normalization or multibranch class-group/descent
   classification;
3. control of moving first binary relations, adjacent new relations,
   positive global defects or arbitrary higher contact;
4. complete quintic, split-sextic or common-ancestor exclusions;
5. an affirmative universal construction or a characteristic-zero
   counterexample.

Continuation instructions: [dated handoff](SUCCESSOR_HANDOFF_2026-10-14.md).
