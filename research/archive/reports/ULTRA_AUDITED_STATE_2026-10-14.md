> **Historical Ultra audited-state snapshot.** Copied from [original Ultra source](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/AUDITED_STATE_2026-10-14.md). Relative links were rewritten to original-branch URLs; the mathematical text was not reconciled against current main. This snapshot is provenance, **not canonical authority**.

# Accepted research frontier — 2026-10-14

This is the continuation entry point after the October 13–14 structural
generalization batch, updated during the October 16 continuation. The
universal integral-projective-curve STCI question
and the unrestricted characteristic-zero problem for
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. No new novelty or priority claim is
made. The results below are written mathematical theorems under their
stated hypotheses, not a claim that all possible carriers are covered.

The user directed that previously verified statements be assumed correct.
Accordingly accepted proofs and certificates were used as premises; new
review was confined to new arguments, pending claims and scope bridges.
The [previous state](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/AUDITED_STATE_2026-10-07.md) preserves the inherited
proof history. This file supersedes its conflicting continuation labels.
The [October 16 continuation record](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-16-session-structural-continuation.md)
collects the latest structural scope extensions, the global quintic target
and honest terminal-process evidence in one successor entry.

## 1. Complete branch reconstruction and inherited closed lanes

The [all-branch inventory](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-evening-branch-frontier-audit.md)
and [reconciled frontier map](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-frontier-map.md)
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
- The completed [October 13 cubic-pair audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-session-nonendpoint-cubic-pair-full-independent-audit.md)
  is now accepted: the entire residual partition `3+3`, including the
  doubled-cubic case, has no mate. The stronger support obstruction
  applies only to `Jbar!=0`; at `Jbar=0` the separate all-power argument
  proves the no-mate conclusion. Older “audit pending” labels are stale.
- The actual conductor quadric and full binary octic, homogeneous gcd
  rank/cover classification, pole/line and target-fiber arguments retain
  their already accepted scopes. The integral residual is still open.

The positive-characteristic constructions and literature corrections are
inherited from the [October 13 source refresh](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-evening-literature-refresh.md).
This continuation did not repeat that search. Neither restricted monomial
or cuspidal results nor invalid affine claims resolve the universal
projective question.

Research strategy after the user's October 14 steering: parallel workers
should pursue different mathematical approaches and shared structural
mechanisms, not distribute a growing list of narrow degree, root or
multiplicity cases. The existing quintic lane remains a dedicated
completion target. Its remaining charts should be organized by their
common conductor geometry; accepted closed charts are premises.

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
[conductor theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-conductor-theorem.md).

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

Proof: [carrier framework](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-global-carrier-framework.md).
Independent audit: [smooth-normalization audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-smooth-normalization-independent-audit.md).
Extension: [Cartier-lift theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-cartier-lift-minimal-degree.md)
and [independent audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-cartier-lift-independent-audit.md).

**PROVED with independent review:** residual conductor torsion on all
three normalized models is detected by equality of entire contact
divisors on proper normalized off-diagonal pair curves, followed by
root-of-unity tests of their constant phases. In a single residual field,
contact equality already forces the constants to be roots of unity.
Every contact occurs at a transverse differential zero; leading terms
there give the phase. Full nilpotent conductor defects remain separate.
The entire degree-eight smooth-quadric projection family has sixteen
parameters: its first normal jet is an arbitrary pair of quintics with
an explicit linear inverse, and four independent parameters affect only
higher jets. This preserves a universal family rather than separate
first-jet cases.
Proof and review: [contact and phase criterion](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-projection-contact-phase-criterion.md),
[independent review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-projection-contact-phase-independent-review.md).

The actual canonical conductor and normalization differential satisfy
the pointwise identity `Z(F_1)=B|c+A`, with
`B~(a-4)H-K_S`, under the reviewed Gorenstein-normalization and smooth
Cartier-lift hypotheses. Hence total weighted conductor contact is
20 in both quadric models and 51 in the plane model. Total ordered pair
contact is at most 140 or 765 respectively. This bounds integer contact
graphs uniformly in every mate degree; split phase orders remain
unbounded. For the sublane with only single-field residual algebras, an
existing mate has minimum degree dividing 840 or 720720 respectively,
with full logarithmic defects retained. Broader non-Gorenstein claims
remain proposals unless their extension receives a written audit.
Proofs: [conductor--Jacobian bridge](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-projection-conductor-jacobian-bridge.md),
[contact budget](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-projection-conductor-contact-budget.md).
Review: [canonical budget audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-projection-conductor-budget-independent-review.md).

**PROVED with an independent family-specialization review:** each fixed
admissible projection family of these three models has a finite-type
phase map to one fixed torus after a finite parameter stratification
and finite surjective root-ordering cover. Actual normalization,
basepoint freeness, birationality, full inverse support and every
logarithmic nilpotent conductor equation are retained. A carrier has
a mate exactly when its phase tuple is torsion. Spreading monic
Noether-normalization equations before rational localization prevents
specialized conductor curves from being lost. The additive-defect locus
is closed on each rational-matrix stratum, hence constructible overall;
no globally closed nilpotent locus is asserted.

Laurent's theorem then makes the torsion points in the actual
constructible phase image a finite union of torsion points in nonempty
open pieces of torsion cosets. Deleted admissibility boundaries remain
deleted. If only zero-dimensional cosets survive, least mate degrees
are uniformly bounded in the family. A surviving positive-dimensional
coset gives actual carriers with unbounded least mate degrees. If no
coset survives, the entire family is excluded. The torsion and mate
loci themselves need not be constructible, and the actual phase images
and cosets of the C0 families have not been computed.

The accepted canonical conductor gives concrete on-C thresholds
`M=5,5,13` for the smooth quadric, quadric cone and plane models,
including carriers generically singular along C. If the finite phase
order is E, all multiples of E at least M are mate degrees; any
additional mate degrees lie among its finitely many multiples below M.
In particular `E>=M` gives minimum mate degree exactly E. This treats
all powers at once while retaining their finite low-degree exceptions.
Proof and review: [full phase/torsion-coset reduction](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-reduction.md),
[independent family review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-projection-torsion-coset-independent-review.md).

**PROVED with an independent arithmetic and scope review:** for an
explicit rational constructible phase image `W=union(Y_i minus B_i)` in
a D-dimensional torus, Mann's theorem and Smith normal form give a
finite effective torsion-coset cover and exact boundary tests. No height
estimate or test of separate mate degrees is needed. If no positive-
dimensional coset survives, every phase order is at most
`max_i P(S_i) d_i^D`, where P(S) is the product of primes at most S,
S_i is the largest monomial-support size, and d_i>=1 is the largest
ordinary total degree after monomial shifts. This is an upper bound,
not a divisibility assertion. Least mate degrees are then at most this
bound plus 4 in the quadric models or plus 12 in the plane model.
The same finite calculation decides torsion existence from the explicit
image and detects unbounded least degrees through a surviving positive-
dimensional coset. Deleted boundaries, empty pieces and the zero-
dimensional torus convention are included.

The whole fixed projection families can be kept over Q, with all
geometric branch choices retained as variables. This does not assume
their integral parameter strata are rational. Actual phase-image
equations have not been computed, so no numerical bound or decision
for the C0 families follows from this theorem alone.
Proof and review: [effective rational phase bound](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-effective-rational-phase-bound.md),
[independent arithmetic review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-effective-rational-phase-bound-independent-review.md).

The stronger raw-input corollary also passes a separate
[October 16 scope audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-16-generalization-raw-projection-decision-independent-audit.md).
For explicit finite rational section/module data on any of the three
fixed models, with the prescribed C0 restrictions and finite constructible
parameter conditions, there is an in-principle terminating exact algorithm
which computes the admissible phase image and decides whether any carrier
in that family has any mate in any degree. It also distinguishes unbounded
least mate degrees from the bounded case and computes a uniform bound
in the latter. Finiteness of the section-ring module is established
before the birational filter, and effective homogeneous generic freeness
preserves every exceptional stratum and actual fiber image.
This is a fixed-three-model algorithm-existence theorem, not a practical
complexity bound or an algorithm run. No actual family outcome or
numerical C0 bound has been obtained.

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
  Those actual-index-at-most-four mixtures are now excluded by the
  stronger local socle theorem below. Actual index-six/twelve strata
  still survive this arithmetic reduction. The other defining
  carrier's normality and global primitivity are not inferred.

Finite local indices alone do not prove the primitive class is torsion.
Local class order is also not the ramification index of a normalized
inverse curve in a cyclic cover: the new D4 example has class order2
but two inverse branches each mapping isomorphically. The full inverse
support must be retained. A multiplicity-two A_(r-1) surface can have
a smooth curve of index r, so surface multiplicity supplies no uniform
index bound.

Proof and independent audits:
[normal-carrier torsion theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-normal-carrier-torsion.md).
Only the new finite arithmetic consequences were run in the
[integer companion](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/computations/normal_carrier_index_reduction_2026_10_14.py).

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
Review: [moving-relation cost](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-relation-gap-cost-independent-audit.md).

Proofs: [full budget](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-evening-entirely-thick-rees-progress.md),
[uniform extension](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-thick-equality-extension.md).
Audits: [socle](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-socle-independent-audit.md),
[relation obstruction](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-thick-relation-obstruction-independent-audit.md),
[pole budget](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-first-relation-pole-budget-independent-audit.md).

The independently reviewed local algebra package gives sharp uniform
Loewy and moment bounds at fixed length and initial order, together
with explicit local CI families achieving them. Consequently local
numerical restrictions alone do not rule out arbitrarily high contact.
See [higher moments](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-higher-moment-and-loewy-bounds.md).

**PROVED, independently audited:** for a moving pure-power first relation
`m^r`, the complete sole-relation obstruction bundle at correction order
r+k is `H^-k M^-(r+k+1) tensor Sym^(r-1)V`. On a balanced rational curve
with H=O(lambda), M=O(-e), all corrections before a gap g have vanishing
obstruction groups when `(r+g)e>=lambda(g-1)-1` for e<lambda. This
constructs actual finite Cohen--Macaulay thickenings of the form
`(P,I_C^(r+g))`, not STCI pairs. Thus finite first-relation tests cannot
uniformly exclude moving relations. At the first coprime next relation
of degree s, however, its evaluation divisor pays at least `(r-1)e`.
Writing g=s-r, the full defect satisfies
`Delta>=r e g(g+1)/2+delta_0+e(r-1)(g+1)`, with the actual first-relation
divisor retained. A moving pure power r>=2 cannot have an initial binary
CI with the same two generator degrees in every fiber and zero
degeneration. Neither statement excludes special-point defects or a
noncoprime next relation.
Proofs: [obstruction tower](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-power-obstruction-tower.md),
[second-relation payment](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-power-second-relation.md).
Reviews: [tower audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-purepower-tower-independent-audit.md),
[second-relation audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-purepower-second-relation-independent-audit.md).

**PROVED with an independent new-proof audit:** an arbitrary saturated
binary first relation determines a finite flat root divisor Z over C.
A fiberwise coprime quotient second generator of degree s exists
exactly when `O_Z(s)` descends from C. This is torsion in
`Pic(Z)/pi^*Pic(C)`, including the nonreduced root scheme. Moving roots
force a nonsplit second-generator extension; assuming a global second
polynomial line would discard valid graded families. Smooth elliptic
(2,2) root curves supply arbitrarily large second degrees and can meet
the full numerical socle constraints. They are abstract graded
families, not ambient constructions. The actual ambient obstruction
is the exceptional-neighborhood extension class contracted with df;
for the whole (2,2) family it lies in one four-dimensional quotient
`H1(O(-5,3))/f H1(O(-7,1))`. This turns the next problem into one
geometric lifting incidence rather than a list of projective degrees.
Proof and audit: [root-curve criterion](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-spectral-root-curve-relations.md),
[spectral audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-spectral-root-curve-independent-audit.md).

**PROVED with independent reviews of the new first and second classes:**
the entire basepoint-free `(2,2)` root family has a single first
compatibility scheme in P8, given by a `16 by 13` rank incidence. Its
`16 by 12` multiplication submatrix is injective throughout this open,
including singular and nonreduced root divisors. The smooth seed
`(z^2+4)u^2+(z^2-8)v^2` lies on a smooth four-dimensional component of
this compatibility scheme and has ruling difference of exact order two.
Thus the first ambient class and the spectral torsion condition can
both vanish; neither test alone exhausts the moving-relation problem.

The first compatible principal ideal is unique. Its actual second
obstruction is therefore a canonical section of a rank-sixteen bundle
over that first compatibility scheme. At the same smooth seed, a
sparse Serre-dual functional evaluates to exactly `1/8`, proving this
second class nonzero. Consequently the generic point of the
four-dimensional component through that seed fails the second lifting
step. This is a family-level exclusion, not a list of failed examples.
The second zero locus, other components and their torsion intersections
remain unresolved. For actual CIs this necessity requires the accepted
blowup bridge hypotheses and next-relation degree `s>4`; `s=4` has a
different target and is not excluded by this calculation.
Proofs: [universal incidence](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-universal-incidence.md),
[second ambient obstruction](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-second-obstruction.md).
Reviews: [first-class audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit.md),
[second-class audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quadratic-root-second-obstruction-independent-audit.md).

The reviewed [global second-dual compression](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression.md)
and [full model audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit.md)
now give twenty-five exact scalar pairings equivalent to the entire
rank-sixteen second obstruction over the whole basepoint-free family,
without coefficient charts or thirty-nine quartic unit variables.
The exported global model has sixteen first equations, twenty-five
second equations and one inverse for the homogeneous branch discriminant.
That discriminant covers the entire smooth family, including infinity,
and implies basepoint freeness. The one M2 launch yielded no elimination
result because its RSS supervisor failed; its PID was later confirmed
absent. This supplies neither an empty stage nor an explicit N.

**PROVED with separate cohomological and functorial reviews:** for a
fixed balanced rational formal neighborhood with conormal
`O(-lambda)^2`, first normal order r and movement epsilon, the sufficient
condition `lambda>3 epsilon` makes every Cartier-root correction space
vanish in degree zero. The obstruction ranks are
`m(r lambda-epsilon)-(r epsilon+r+epsilon)`. Thus the entire tower is a
descending chain of closed schemes on one fixed finite-type coefficient
open, including singular/nonreduced roots and nonreduced parameter
bases. It eventually stabilizes as schemes at a finite existential N;
the stable locus represents compatible formal Cartier ideals. One
adjacent equality does not certify that N has been reached.

Within the accepted actual-CI bridge, stages are necessary only for
`m<s-r`. Hence `s>r+N` forces the root into this single stable formal
stratum; outside it the gap is bounded by N. This is a structural
alternative across all second-relation degrees. The tower theorem alone
computes no N and supplies neither algebraization nor emptiness. For a balanced
rational degree-e curve the sufficient criterion is `3epsilon<2e-1`,
independent of r; the coefficient family and N still depend on r.
Proof: [uniform finite obstruction frontier](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-uniform-root-tower-finite-determinacy.md).
Reviews: [cohomology](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-uniform-root-tower-cohomology-independent-audit.md),
[embedded-ideal functor and stabilization](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-uniform-root-tower-functor-independent-audit.md).

**PROVED with a full independent primary-source and geometric audit:**
for every balanced smooth rational curve of degree e>=4 in P3 over an
algebraically closed characteristic-zero field, and every r>=2, a smooth
root divisor of class `(2,r)` has no all-orders embedded Cartier lift.
This excludes an entire movement degree simultaneously across all first
normal orders; it does not enumerate hypersurface degrees.

An infinite lift would be a smooth formal surface along the root Z,
whose genus and normal degree are `r-1` and `(2e-1)r-2`. Ample-normal
algebraicity produces an algebraic surface branch. Normalization preserves
the whole smooth root; other branches and exceptional components remain
allowed. Hartshorne's high-self-intersection theorem gives a ruled model
isomorphic near Z. Its hyperplane intersections force the image surface
degree `d<=r+2`, while a general plane section forces
`(d-1)(d-2)>=e r(r-1)`. These inequalities contradict each other for all
e>=4,r>=2. No formal Picard algebraization is assumed.

Combining this theorem with the accepted tower gives, for each fixed r
and actual embedding, a uniform finite empty stage `K_N` on the entire
smooth movement-two open. In the actual-CI bridge the precise consequence
is `s-r<=N`, since a gap g supplies only stage g-1. This is an existential
bound, not a computed cutoff or an exclusion of every finite-gap CI.
Singular/nonreduced roots and failures of the bridge remain outside it.

More generally, for a smooth connected finite root of class `(epsilon,r)`,
put `g=(epsilon-1)(r-1)`, `nu=(2e-1)r-epsilon`, `h=e r`. If
`nu>4g+5`, any infinite lift requires an integer d satisfying
`d<=max_(a>=1 integer)(2ah-nu a^2)` and the same plane-genus lower bound.
When also nu>=h, this implies
`(e-1)r^2-(e+2epsilon-3)r-(epsilon-1)(epsilon-2)<=0`.
Thus, for fixed epsilon with `2e-1>4(epsilon-1)`, only finitely many
first orders can admit a smooth infinite formal root. These are formal
root bounds, not unrestricted first-order bounds for actual CIs.
Proof and full review: [smooth-root formal nonexistence](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-smooth-root-formal-nonexistence.md),
[independent global audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md).
The proof also preserves the failed finite-Hilbert-count shortcut:
containing a long primitive jet need not produce a smooth algebraic branch.

The [characteristic-scope addendum](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md)
independently extends this formal theorem and its finite empty tower to
every algebraically closed characteristic, retaining the explicit
balanced normal bundle and full smooth root. Total degree, including
inseparable degree, enters the intersection formulas. This does not
assume the literal C0 has the same normal splitting in every characteristic.
The separate [inseparable-root bridge](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge.md)
now passes both a [local-algebra review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-local-algebra-review.md)
and a [full new-scope audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit.md).
It extends the actual-CI bridge to every characteristic under its literal
saturated first-line, jointly generating leading sections, full generic
initial regular sequence `(f_r,g_s)`, gap at least two, and smooth full
root hypotheses. At the actual root prime, reducedness means exponent
one even for an inseparable residue field. The uncompleted standard-basis
argument gives the ideal `(h,u^(s-r))`; the local smooth surface and UFD
argument globalize it without saturating away vertical components.
Thus `s-r<=N` now holds in this same literal lane in every characteristic.
The proof explicitly rejects a compatible residue-field splitting in
the wild example; no inseparable coefficient-field assumption is hidden.

**PROVED with a targeted new-scope audit:** the same geometric argument
has an intrinsic form on any smooth projective threefold. For a smooth
formal surface along a smooth curve Z of genus g, normal degree
nu>4g+5, and nef ambient class A with positive surface square d, it
requires `d<=max_(a>=1 integer)(2a(A.Z)-nu a^2)`. Positivity of d is
essential for a merely nef class.

For a smooth space curve of degree e and genus gamma with the actual
bundle isomorphism `N_C=L direct_sum L`, put epsilon=deg M for a smooth
connected finite root in `|M boxtimes O(r)|`. Then
`g_Z=r gamma+(epsilon-1)(r-1)`,
`nu=(2e+gamma-1)r-epsilon`, and `h=e r`.
Under nu>4g_Z+5 and nu>=h, any infinite lift requires an integer
`1<=d<=(1-gamma)r+epsilon` and
`(d-1)(d-2)>=e r(r-1)`. Thus positive genus strengthens the same
opposing degree bounds. Numerical balance alone does not imply the
bundle hypothesis. No higher-genus finite-tower theorem or arbitrary
actual-CI exclusion is asserted by this extension, whose stated scope
is characteristic zero.
Proof and targeted review: [nef formal branches over arbitrary bases](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-nef-formal-branch-arbitrary-base.md),
[new-scope audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-nef-formal-branch-arbitrary-base-independent-audit.md).

The same numerical criterion also classifies smooth movement-one formal
roots for balanced rational curves. For e>=3,r>=2, none has an all-orders
lift. For r=1,e>=4, all-orders lifts are exactly the strict-transform
germs of quadrics containing C and smooth along it. The degree estimate
is now d<=r+1; at r=1, equality of the entire exceptional intersection
removes the extra-branch ambiguity. This is an all-orders classification,
not a replacement for the stronger accepted finite-jet C0 result.
Targeted review: [movement-one formal-root audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-movement-one-formal-roots-independent-audit.md).

**PROVED with an independent new-scope audit, without a split normal
bundle:** let a fixed finite-type parameter scheme carry a proper smooth
family of geometrically connected Cartier roots in an actual divisor E.
Write `g=genus Z`, `A=Z^2_E`, and `nu=deg O_E(E)|Z`, fixed on this family.
If `nu>max(A,0)`, every correction line has degree `A-m nu<0`.
Relative perfect cohomology gives obstruction bundles of rank
`g-1-A+m nu`, with zero degree-zero pushforward after every base change,
including nilpotent parameters. The accepted embedded-ideal argument
therefore gives a canonical closed eventually stable formal-lift locus
on this same finite-type parameter space. The parameter space need not
be proper; its universal curve is proper over it.

For ANY fixed smooth space curve of degree e and genus gamma with its
actual normal bundle, the exceptional ruled surface satisfies

```
A=(4e+2gamma-2)r^2-2r nu,
A=2g_Z-2+4er-2nu,
```

where r is the full degree of a smooth connected root over C. Fixed
`(r,nu)` fixes its numerical divisor class and Hilbert polynomial. A
single finite-type smooth Cartier Hilbert open thus covers every such
root of that fixed class, with the numerical strata retained. No
semistability, projective triviality or rational-base hypothesis enters.

If also `nu>4g_Z+5` and there is no positive integer d obeying both
`d<=max_(a>=1 integer)(2aer-nu a^2)` and
`(d-1)(d-2)>=e r(r-1)`, the stable locus is empty. One finite empty stage
N is then uniform over the entire fixed family. Under a valid actual-CI
bridge, `s-r<=N`. This gives one intersection-theoretic mechanism across
arbitrary actual normal bundles; it does not bound all numerical classes,
supply an explicit N, or cover singular/nonreduced roots. The new
intrinsic proof and its targeted audit state characteristic-zero scope.
Proof and review: [intrinsic finite root families](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-intrinsic-finite-root-family.md),
[splitting-free family audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-intrinsic-finite-root-family-independent-audit.md).

The independently reviewed torsion geometry also gives a concrete cubic
equation for exact order two on the smooth `(2,2)` root open: the
determinant of the three-by-three coefficient matrix is zero. It meets
the four-dimensional compatibility component transversely at the accepted
seed, giving a specified three-dimensional component D. The second
obstruction is nonzero there, so its zero scheme, and the stable formal
locus, have support of dimension at most two inside D. Other torsion
components/orders are not covered by this dimension bound.
Proof and review: [torsion/second-zero geometry](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry.md),
[independent torsion audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quadratic-root-torsion-second-zero-independent-audit.md).

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

Proof: [symbolic-ribbon criterion](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-ribbon-numerical-criterion.md).
Review: [ribbon review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-ribbon-independent-review.md).

## 6. Complete finite-pencil replacement for ancestor computations

**PROVED, independently reviewed:** over any field, an affine pencil
`(lambda I_q+A; B)` with `rank B=q-1` and `rank(B;BA)=q` has full-fiber
target exclusion exactly when a normalized polynomial left dual of
degree at most two exists. The incidence reduces to q-2 linear
polynomials and one quadratic. At q=18 this is sixteen linears and one
quadratic. Rank drops have a separate exact rule; parameter-ring and
determinantal fallbacks retain every exceptional stratum.

Proof: [polynomial-dual theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/generalization-localcoh-dual-lemma.md).
Review: [pencil review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-localcoh-pencil-independent-review.md).
This does not certify the exact rank locus of every ancestor family.
The entire family-two finite exceptional set is now closed: the seven
accepted cubic/quartic roots plus all fifteen roots of f15. A new
fraction-free integer-polynomial inverse, followed by one scalar inverse
modulo f15, produced a normalized polynomial dual of actual lambda degree
one. An independent standard-library verifier checked all eighteen
original-tensor columns modulo the entire degree-fifteen polynomial.
All three new execution stages exited zero with empty stderr. No accepted
tensor interpretation, rank/top check or seven-root verifier was rerun.
Retired attempts three/four/five retain their exact interruption/failure
lineage and are not certificates. Proof, reusable method and source
bindings: [fraction-free certificate](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-localcoh-degree15-fractionfree-certificate.md).

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
by root-count and finite multiplicity-partition incidences. The final
main h3 3+2 pattern now has a completed literal original-six-generator
identity `M6 W=(V c5)^2`, with captured exit zero and empty stderr.
Together with the previously reviewed infinity and other support
patterns, **the entire homogeneous gcd-three lane is excluded in all
mate degrees**, including zero-cubic and proportional families.
The large witness is preserved as an archive with an exact integrity
binding; its verified product was not replayed.
Acceptance: [complete h3 record](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-h3-results-acceptance.md).

Proofs: [quintic continuation](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-quintic-continuation.md)
and [regular L2](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-quintic-l2.md).
Independent audit: [new quintic review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-new-independent-audit.md).
The singular qZ=0 targets, intrinsic A4 point, target infinity in the
sole-root lane, Jbar=0 and other common-root incidences remain outside
that regular-chart closure. Other quintic normalizations remain open.

The common-quartic-ancestor problem is distinct from an actual quartic
mate. All twenty-two finite family-two exception roots are now excluded
with original-tensor duals. Boundary three/four, nonendpoint top zeros,
the other family and positive-D2 directions retain their precise
recorded scope. A failed large module run is not a negative certificate.

The dedicated quintic continuation now uses one shared Hamiltonian
support condition. Its [independent proof review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-logarithmic-support-independent-audit.md)
accepts `support(F) subset support(H) iff F divides D_H F` over
characteristic-zero fields, retaining infinity, multiplicities and the
Jbar=0 intrinsic A4 allowance. It is not an assertion about arbitrary
nonreduced parameter bases.

**PROVED with an independent new-proof audit:** the whole homogeneous
h2 conormal gcd divides the actual conductor octic. The conductor
annihilates the relative differential module, giving all finite root
multiplicities; the accepted A4 value completes the possible simple
infinity factor. Thus the actual support condition reduces to one
homogeneous sextic Q=F/H and the simultaneous system

```
D_(H*s) Q=L_1 Q,     j D_H Q=mu Q,
```

with the intrinsic A4 point s=0 retained. This is a single shared
incidence, not separate multiplicity partitions. The corrected exact
source-coordinate capture and the reduced sextic capture both exited
zero with empty stderr. The earlier attempt04 used p=1-z instead of
p=1/z and remains a rejected geometric binding; its algebraic output
is preserved as a failed bridge, not a certificate.
Proof and review: [conductor quotient](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-h2-conductor-quotient.md),
[h2 factor audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-h2-conductor-factor-independent-audit.md).
Coordinate and coefficient bindings: [corrected sextic incidence](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence.md).
**PROVED with an independent new coefficient and geometric review:**
every surviving `j=0` mate candidate has intrinsic A4 conductor contact
at most two. The exact first coefficient is
`-2 G (delta^2+2B+G)(3delta^2+G)^2`; SUP makes the middle factor a unit
after the accepted `G=j=0` exclusion. On the remaining possible
first-coefficient zero locus the second coefficient is nonzero.
This is one all-parameter contact argument, independent of gcd degree.

On h2 the allowed A4 point is outside H for every surviving candidate.
If `Res(H,Q6)` were nonzero, the `j=0` support condition would force
`Q6` to be the sixth power of the A4 linear form, contradicting that
contact bound. The `j!=0` condition already forces a shared root.
Hence **every remaining h2 candidate satisfies the single condition
`Res(H,Q6)=0`**, for both values of j and without dividing by a
discriminant. The two small norm factors on the declared inverse-map
chart are genuine necessary incidences, not forbidden projection
factors. The homogeneous sextic incidence is not yet proved empty;
repeated roots and projective boundaries remain in its shared system.
Proof and review: [intrinsic A4 contact bound](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-intrinsic-a4-contact-bound.md),
[independent A4 contact audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-quintic-intrinsic-a4-contact-independent-audit.md).

**PROVED with independent determinantal review:** on the monic finite-H
chart and the accepted necessary candidate open `D(q5) union D(q6)`,
the seventy-seven sextic rank minors define exactly the same ideal
sheaf as twelve fixed generators. The identity
`D_(sH)Q=(3/2)s D_HQ-3H_tQ` removes the expanded cubic action column;
eleven selected cubic minors and one retained-j minor suffice. The
equality includes nonreduced coefficient bases and does not divide by j.
Neither the global unsaturated ideal equality nor emptiness follows.
The shared norm product can be appended with its declared inverse-map
unit conditions; its factors remain together in this program.
Proof and review: [twelve-generator system](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quintic-h2-twelve-generator-support-system.md),
[independent ideal-sheaf audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit.md).

The next reviewed common-open argument proves Delta1 nonzero on every
remaining mate candidate, using the accepted A4 fiber and closed-lane
premises for both values of j. The actual capture has the exact binding
`delta^4 q6=-3 Jnum Delta1num`. On the declared finite inverse-map chart,
this makes q6 a unit times j without cancelling j; the twelfth generator
is redundant. Moreover `(q5,q6)` is already the unit ideal on this
localized ring, so its separate saturation is unnecessary.

On the same declared chart, the entire shared support incidence is
equivalently the eight coefficient equations of
`(z^2+vz+w)q'(z)=(d z+u)q(z)` with unique witness scalars d,u.
The derived equations `(d-5)(d-6)=0` and `j(d-6)=0` retain both A4
alternatives in one ideal. The equivalent ODE presentation has much
lower degree than the expanded cubic minors. It is not an emptiness
certificate. The inverse-map determinant and its repeated-root/cover
boundary are still outside that rational chart; the Delta1 necessity
is global, whereas those original inverse-map units are not.
Proofs and reviews: [A4 unit and eleven generators](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quintic-h2-a4-unit-and-eleven-generators.md),
[unit audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quintic-h2-eleven-generator-unit-independent-audit.md),
[automatic open and ODE](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quintic-h2-automatic-open-and-ODE.md),
[ODE audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit.md).

**PROVED with an independent global-cover and artifact audit:** the
[global monic ODE model](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md)
and [October 16 review](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit.md)
replace that rational chart by one necessary incidence for EVERY remaining
h2 mate candidate in this fixed genus-one A4 family. Its seventeen
equations in nine original/cofactor/action variables consist of four
conormal remainders, two correctly reversed actual-conductor remainders,
eight ODE coefficients and three derived accelerators. Only
`delta*E*Delta1` is inverted, where E is the exact-h2 cofactor resultant.
Neither the H discriminant nor the old cover factor K is inverted;
repeated roots and the rational inverse-map boundary remain present.
Source zero is also retained. The actual conductor factor is imposed by
its two remainder equations, without promoting a field-valued geometric
factor theorem to a family scheme identity.

The [runnable global input](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
passed a load-only check. The single next mathematical target is
`h2GlobalIdeal : h2GlobalDomainUnit^infinity`. A unit-ideal certificate
would close all remaining h2 mate candidates in this family; a proper
ideal would still require actual projection admissibility, full fibers
and conductor descent. This does not close the retained h1 exceptions,
other quintic normalizations or the whole quintic problem.

One new whole-h2 global QQ saturation prospect was run under a validated
CPU/wall/memory guard. It reached the saturation stage, then crossed its
polled 1536-MiB RSS threshold after 58.564 seconds. The actual exit was
-15; PID39519 was reaped and its private group was absent. It produced
no completed ideal or unit certificate. This is a memory interruption,
not a mathematical exclusion or an observation timeout. Record:
[global QQ attempt06](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/execution-record.json).

## 8. Local power-socle compatibility and new all-degree normal exclusion

**PROVED, independently reconstructed:** for a normal carrier with a
smooth curve C, suppose a mate cuts nC. At an on-curve point with actual
local Cartier index r dividing n, put k=n/r. If A_F,P is the carrier's
first-normal-symbol vanishing order and D_r,P is the actual top-power/
socle defect of its local Cartier multiple rC, then

```
D_n,P=(k-1)A_F,P+kD_r,P.
```

This retains the full embedded algebra and higher jets. The proof uses
normality for a colon identity and the regularity of z^r/h; a relative
Jacobian generates the actual socle over k[[t]], by the Artinian CI
Jacobian theorem and finite Gorenstein base change. The ordinary free
normal layers are powers of the first quotient, and the exact pointwise
Frobenius-lattice identity is
`2 sum_i length(T_i)_P=nD_n,P`. This is distinct from a saturated BF
filtration; none of its defects are silently set to zero.

For C0, a pointwise upper bound s on actual local curve indices gives

```
s >= (4a-7)/(7-16/a),
4a^2-(7s+7)a+16s <= 0.
```

Thus normal carrier degree is bounded linearly within every such index
class, independent of the number or higher complexity of singular points.
No universal curve-index bound is proved. A balanced smooth rational
curve of degree e has the analogous bound
` s >= (ea-(2e-1))/((2e-1)-e^2/a)` with its stated edge conditions.

**Every normal C0 carrier whose actual on-curve local indices are at
most four is now excluded in every carrier and mate degree.** This
includes arbitrary D/E and A1,A2,A3 mixtures. The accepted arithmetic
reduction gives (6,8), n=12. The local formula excludes a normal octic
and forces a normal sextic to have first slope ell=7 and total slack
one. It eliminates index-two points and forces zero primitive local
socle defect at every index-three/four point. The whole symbolic triple
is consequently primitive with constant first direction, contradicting
the accepted nonzero P-010 obstruction. The other carrier need not be
normal, and no primitive initial presentation is assumed.

Actual index-six and index-twelve points in the broader common-exponent-
twelve class remain open, including index-twelve first-symbol poles.
Proof and scope: [local index-socle theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-normal-index-socle-theorem.md).
Full independent proof: [filtered compatibility audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-index12-filtered-compatibility.md).
The [ordinary-curvilinear precursor](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-curvilinear-torsion-and-index12.md)
retains the earlier route; its pending labels are superseded by these
accepted records.

### Intrinsic comparison and a theorem for all balanced rational degrees

**PROVED with a separate new-proof audit:** for a smooth Q-Cartier curve
C on a normal Cartier surface in any smooth projective threefold, the
surviving conormal line B admits an intrinsic map
`B^R -> O_S(-RC)|C`. Its zero divisor is R times the effective rational
divisor

```
E_ray=sum_P (A_F,P+D_r,P)/r_P [P],
deg E_ray=ell-C^2.
```

This exists before any mate does. For a degree-e curve in P3 admitting
a mate on degree-a S, every mate power is governed by the single exact
budget `ell-e^2/a=sum_P(A_F,P+D_r,P)/r_P`. Full line-bundle identities
are retained, including in positive genus. If `nu=4e+2g-2` and eta bounds
normal line-subbundle degrees, a pointwise index bound s forces

```
e a^2-[nu+(s-1)eta]a+s e^2<=0.
```

For every balanced smooth rational degree-e curve, e>=3, this forces
an actual on-curve index at least e-1, independently of both defining
degrees. At the threshold all singular indices are exactly e-1, all
primitive local defects vanish, and the first direction is constant.
In characteristic zero the minimal unordered degree pair is (e-1,e),
and its actual complete intersection is a primitive (e-1)-fold curve.
For e>=4 a proved obstruction to every constant-direction primitive
triple strengthens the threshold to at least e. That obstruction is
curve-specific; it is accepted for C0 and is not assumed for every
balanced rational curve.

The intrinsic comparison and scalar/local threshold results also hold
in characteristic p when every actual local index is prime to p; the
mate length itself need not be prime to p. The global minimal-pair
statement remains characteristic zero. Wild indices and nonsmooth
support remain outside this new local theorem.
Proof: [general normal-index scope](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-normal-index-general-scope.md).
Review: [independent general-scope audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-normal-index-general-scope-independent-audit.md).

### An unrestricted normal C0 defect certificate

**PROVED, with a separate comparison audit:** primitive local Cartier
multiples of actual lengths two or three are automatically primitive,
so D_2=D_3=0. In the ell=7 constant-direction branch, let T be the
first-layer torsion divisor of the global symbolic triple. The accepted
pole obstruction forces `deg T>=2`. At index two one has exactly
`T_P=A_F,P`; at index three T_P=0; at indices at least four the exact
relation-module comparison gives `T_P<=r_P D_r,P/2`. Hence

```
2<=deg T<=sum_(r=2) A_F,P + (1/2)sum_(r>=4) r_P D_r,P.
```

Every constant-direction candidate must pay through index-two contact
or a positive full primitive local defect of index at least four.
The actual divisor must also satisfy the accepted apolar support
condition, not merely this degree bound. Odd-index positive defects
are even. Combining the certificate with the intrinsic reciprocal
budget improves the C0 scalar bound to

```
4a^2-(7s+6)a+16s<=0,   a>=5, s>=3,
```

for every first slope; the ell<=6 branch already has a stronger bound.
This is new progress on unrestricted normal carriers, not an exclusion
of unbounded indices or of sufficiently large defect contributions.
Proof: [symbolic-triple certificate](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-normal-carrier-symbolic-triple-certificate.md).
Review: [torsion comparison audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-symbolic-triple-torsion-comparison-audit.md).

The independently reviewed
[transverse-differential socle theorem](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-transverse-socle-independent-audit.md)
is accepted. It identifies the actual first layer on a generically
regular singleton Cartier lift and proves
`(n-1)deg A>=deg(C)(a-4)+deg(C)^2/a-(2g(C)-2)`.
For C0, degree8 projections require
`1<=deg A<=5`, `(2b-1)deg A>=20`; degree16 projections require
`1<=deg A<=6`, `(4b-1)deg A>=51`. Thus all transverse-coprime
projections in this lane are excluded across all mate degrees.
The proof does not cover rank-two first layers or non-Cartier lifts.

**PROVED with independent new coefficient and geometric reviews:** an
everywhere primitive C0 multiple of length N>=4 with conormal O(-6)
is contained in the actual quadric. The new cubic calculation leaves
only the quadric's degree-one moving relation, and vanishing H0 of the
later correction bundles makes its finite principal ideal unique at
every length. Hence a normal degree-a carrier with such an entire
symbolic multiple must satisfy N<a/2; equality would construct a
forbidden actual quadric mate. In particular the whole symbolic
quadruple on a normal octic cannot be primitive with that conormal.
This is stronger than a generic first-symbol assertion and does not
discard special-point torsion.
Proofs and reviews: [cubic classification](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-moving-linear-cubic-compatibility.md),
[independent cubic expansion](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-moving-linear-cubic-independent-audit.md),
[ideal rigidity and carrier consequence](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-moving-linear-ideal-rigidity-independent-audit.md).

**PROVED with independent geometric review:** the
[strict-transform bridge](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-blowup-root-curve-primitive-bridge.md)
connects actual supported CIs to the spectral ambient obstruction.
With the literal saturated first-relation, joint leading basepoint-free,
smooth root divisor and generic initial CI(r,s) hypotheses, the strict
intersection is an actual primitive (s-r)-fold root curve for s-r>=2.
Locally one strict surface is smooth; inside it the other cuts the
power of the smooth root curve. This splits the conormal sequence and
forces the actual `kappa(df)=0`. Joint leading base points cannot be
saturated away: the audit preserves an explicit family producing an
entire vertical exceptional fiber there.
Review: [blowup bridge audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-blowup-root-curve-bridge-independent-audit.md).
The bridge supplies necessity, not an unproved value/nonvanishing of
that obstruction.

**PROVED, independently audited:** on a generically regular carrier with
full singleton smooth Cartier lift c, the actual conductor/socle comparison
is pointwise:

```
D_n=(n-1)A-B|c.
```

Here B is the actual conductor near c and A the full transverse zero
divisor. This refines the accepted total-degree bound to every point,
including its full embedded top-power defect. The proof retains the
finite cokernel of the pulled-back normalized thickening and proves
that the relative Jacobian is an actual socle generator.
Review and full proof: [pointwise conductor--socle comparison](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-pointwise-conductor-socle-independent-audit.md).
The same reviewed lattice comparison gives the exact pointwise
colength `2 delta_n=n B|c` of the actual CI inside its pullback
thickening on the carrier normalization. Thus odd n requires every
coefficient of `B|c` to be even, and actual lengths two or three force
`B|c=(n-1)A`. This pullback thickening is not called a normalization
of the nonreduced CI. These statements retain the characteristic-zero
and smooth singleton Cartier-lift hypotheses of the proof.
Residual phases, logarithmic defects and arbitrary non-Cartier or
multibranch lifts remain separate conditions.

## 9. Global unresolved obligations

The structural results now organize the work by normalization branches,
Cartier relations, conductor torsion and complete filtered normal
algebras. They do not provide:

1. an unconditional minimum-carrier degree bound or a theorem forcing
   smooth singleton normalization;
2. a full singular-normalization or multibranch class-group/descent
   classification;
3. unrestricted control of moving first binary relations, adjacent new
   relations, positive global defects or arbitrary higher contact;
4. complete quintic, split-sextic or common-ancestor exclusions;
5. an affirmative universal construction or a characteristic-zero
   counterexample.

Continuation instructions: [dated handoff](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/SUCCESSOR_HANDOFF_2026-10-14.md).
