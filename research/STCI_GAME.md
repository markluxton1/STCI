# The STCI existence and non-existence research game

Started October 30, 2026. This is a working strategy and claim ledger,
not theorem authority. Use [the research map](MAP.md) and individual
canonical records for accepted statements; use linked source notes and
independent audits for reviewed provisional contributions.

The shared question is whether the fixed
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3
\]
is a set-theoretic complete intersection over an algebraically closed
characteristic-zero field. **Open.** The source/evidence directory is
[STCI_SEARCH.md](STCI_SEARCH.md).

**Closed out October 31:** the [consolidated report](notes/2026-10-31-stci-package-closeout.md)
records final independent verdicts, geometric meaning and exact unfinished
endpoints. This ledger preserves the completed exchange and surviving
interfaces; it does not initiate another open-ended cycle. All new
mathematics remains reviewed provisional.

## 1. Each side has an independent research program

The existence side seeks actual homogeneous equations with proper
intersection and reduced support exactly \(C_0\). It should propose the
best construction justified by everything currently known, state its
actual global coefficient space, and identify the first test capable
of producing or rejecting it. It may do independent side research,
including asymptotics, new geometric models and positive-characteristic
constructions.

The non-existence side aims to exclude as much as possible and find
general principles behind every new theorem and example. Refuting the
other side's current construction is one duty, not its boundary.
It should independently enlarge excluded classes, strip away
unnecessary hypotheses, seek reusable invariants and identify the
missing step toward a statement about **all** possible equations.
It has the same freedom to use all research and pursue side questions.

The referee checks scopes, actual global realizability, properness,
residual support, and dependencies. A successful formal model, a large
parameter count or an empty finite family changes the game state only
by its proved implication. Neither side may declare victory from it.

For every proper containing pair retain
\[
[V(F_a,G_b)]=m_C[C_0]+R,\qquad ab=4m_C+\deg R.
\]
An existence win needs an actual pair with \(R=0\) and full support
verification. A non-existence win needs a separately audited argument
covering all actual pairs. Local, generic, fixed-carrier and
normalization hypotheses cannot silently become universal.

## 2. Geometric meaning is part of every move and review

Each side must identify the actual scheme, divisor, morphism, linear
system, attachment, or deformation it is studying. A calculation must
explain what its kernel, rank, discriminant, degree or parameter condition
measures about that object. Each result must then change the geometric
picture of a possible STCI, rather than merely add an algebraic exclusion.
The referee independently checks that interpretation.

For example:

- The line obstruction is an attachment graph on a normalization.
  Restricting a hypothetical mate to actual lines forces branch
  multiplicities incompatible with its global hyperplane degree.
- The fixed-quadric residual is a base curve that every allowed
  higher-order correction vanishes on. Large fibers of the lifting map
  therefore cannot move that part of the intersection.
- The missing-middle-coefficient elliptic support theorem excludes
  **coplanar marked four-point divisors on \(C_0\)**. The coefficient
  condition is a coordinate expression for that intrinsic failure of
  projective position, and the proof uses incompatible degree-two pencils.
- An arithmetic jet gap is a failure of functions on the normalization
  to descend through a thickened conductor boundary. Frobenius changes
  which jets survive; its effect is more than a divisibility pattern.
- A jet-matrix kernel measures an actual global linear system with
  prescribed contact. Its rank alone does not explain why contact fails.
  The search should seek the curve, divisor, gluing condition or other
  geometry responsible, as the later line argument did for the seed.

If the geometry is not understood, state the exact algebraic fact and the
missing geometric question. Do not manufacture an interpretation.
Neither a compelling picture nor an exact finite certificate replaces
the remaining global implication.

## 3. What the current results change

| Evidence | Existence response | Independent obstruction program | General-question limit |
| --- | --- | --- | --- |
| [R-0001](results/quartic_carrier_exclusion.md), including its accepted factor reduction | Seek defining degrees at least five | Do not reopen quartic mate cases; find mechanisms for higher degrees | Higher degrees remain open |
| [Global equation freedom](notes/2026-10-28-stci-search-freedom.md): fixed quadric factors below \(d=3m\), large sources afterward, symbol surjectivity at \(d\ge3m+2\) | Use actual source images and correlate the pair, rather than random independent leading forms | Study joint/global constraints and high-contact cancellation; a dimension count does not supply them | Individual-equation freedom does not decide paired support |
| [All-degree mixed-seed line obstruction](notes/2026-10-30-mixed-weight-line-obstruction.md) | Increasing the mate degree on this seed cannot help | Reuse actual curve attachment and divisor-degree balance on other carriers | Other sextic families are not excluded |
| [Uniform weighted-subalgebra theorem](notes/2026-10-30-weighted-subalgebra-line-obstruction.md) | Enter repeated/axis binary boundaries or leave the constant-coefficient \(k[q,c_0,c_2]\) source | Enlarge the incidence principle; attack the degenerate boundary independently | This source has asymptotically vanishing relative dimension in the full fixed-order space |
| [Quadric-boundary theorem and global row filter](notes/2026-10-30-stci-game-quadric-boundary.md), independently audited | Change the common cubic boundary or use corrections that can change its restriction on \(Q\) | Extend the fixed-residual principle beyond this large family; test global polynomial cancellation independently of the opponent's proposal | The family has asymptotically full relative dimension in its fixed-order source but is not exhaustive; its residual floor is not universal |
| [All-degree actual-residual obstruction](notes/2026-10-30-stci-game-obstruction.md), [final independent audit](notes/2026-10-31-stci-closeout-obstruction-audit.md) | Seek a special normal-cover or attachment locus; increasing degree alone does not help a carrier in the ordinary open class | Actual \(T\subset Q\) supplies a second degree equation incompatible with a single ordinary inverse curve; component slopes give a necessary balance on the reduced horizontal locus | Excludes a nonempty dense open in every full \(V_{a,m}\), \(a\ge3m\), in all mate degrees; special vertical/repeated/low-slope/nonordinary loci remain |
| [Elliptic degree-two inverse construction](notes/2026-10-30-stci-game-existence.md), [final independent audit](notes/2026-10-31-stci-closeout-existence-audit.md) | Preserve \(\Gamma\sim H\), absorb extra inverse support in the actual five parameters, then test a descending power | The fixed finite birational member has isolated inverse length twelve and is excluded in every mate degree; a uniform family obstruction is not proved | Degree-twelve vertical first-symbol defect changes the ordinary balance; numerical compatibility upstairs is not full support or descent |
| [Projection boundary exclusion](notes/2026-10-29-projection-m2-boundary.md), [smooth residual conditions](notes/2026-10-30-projection-order-two-survivor.md), [global extension obstruction](notes/2026-10-30-projection-elliptic-target-incidence.md) | A primitive elliptic target must also extend to the actual marked source; use nonzero middle support coefficient | Solve the remaining primitive elliptic and order-one incidence, or derive a stronger extension principle | The full sixteen-parameter admissible and descent loci remain uncomputed; other normalization models remain separate |
| [Arithmetic higher-jet gap](notes/2026-10-29-arithmetic-beyond-binomial.md), attained by explicit two-non-binomial \((16,p)\) pairs | Fixed-degree persistence in infinitely many primes would matter; degree-\(p\) constructions do not provide it | Extend the jet mechanism beyond the specified 23-parameter source, or find another uniform all-pairs mechanism | The restricted minimum \(p\) does not bound the all-pairs \(\delta(p)\) below |
| [Residual constructions](notes/2026-10-28-containing-intersections-synthesis.md) and [quantitative bounds](notes/2026-10-28-residual-degree-synthesis.md) | Test whether actual linked families and attachment flexibility can absorb residual support while retaining equations | Identify which bounds are strictly positive on the proposed global family and which equality mechanisms survive | Flexible attachment is not increasing thickness; conditional positive bounds are not universal |

Every new result should update at least one entry here: remove a
construction, create a usable source, enlarge an exclusion, expose a
missing implication, or change the next decisive test. A theorem's
number of parameters or all-degree wording is not a measure of universal
coverage by itself.

## 4. First exchange: actual lifting freedom and its global boundary

The first opening moves below were root-drafted when the original
advocates were interrupted. Their saved evidence and subsequent
independent reviews now determine their final statuses. The
fixed-quadric obstruction is reviewed; E2 remains a source proposal, and
the actual E3 exchange is closed out in Section 5. The
[quadric-boundary note](notes/2026-10-30-stci-game-quadric-boundary.md)
contains the literal coefficient spaces, proposed proofs and limits.

**Existence move E1.** At \(d=3m+2\), use a cubic \(H\) through \(C_0\),
different quadratic coefficients \(f_2,g_2\), and all actual higher-order
lifts:
\[
F=f_2H^m+K,\qquad G=g_2H^m+L,\qquad
K,L\in H^0(\mathcal I_C^{m+1}(d)).
\]
This deliberately correlates leading roots, allows a nonconstant
coefficient ratio on \(C\), and keeps substantial genuine global freedom.

**Obstruction move N1 — reviewed theorem.** Every such higher-order correction has a factor
\(q\). The whole source lies in \((q,H^m)\), so both equations retain
the residual ruling divisor of \(V(q,H)=C_0+R_H\). Every proper pair
has the scheme \(V(q,H^m)\) inside it, and therefore
\[
R\ge mR_H,\qquad \deg R\ge2m.
\]
The [independent audit](notes/2026-10-30-stci-game-quadric-boundary-audit.md)
checks all parameters, including doubled residual rulings. The correction
parameters cannot remove a boundary on which all corrections vanish.
The proper-pair locus is nonempty and the leading coefficient ratio
can be nonconstant, so the failure is not explained by an improper
pair or a scalar-pencil cancellation.

**Existence response E2.** Leave the common global cubic source. One
candidate is to prescribe only a common moving factor of the two leading
normal forms, with distinct remaining factors, in the full actual source
\(H^0(\mathcal I_C^m(d))\). The reviewed symbol-surjectivity result gives
individual global lifts at \(d\ge3m+2\); it does not give a jointly
supported pair. Another option is to increase the degree margin until
next-order corrections can change the restriction on \(Q\).

The first tests are properness, absence of a fixed residual curve on
\(Q\), and then the complete actual-global contact incidence. For
example the \((8,8)\) target is generic contact sixteen, not just shared
quadratic normal roots. No such candidate is asserted successful here.

**Independent obstruction response N2.** Develop the quadric-boundary
restriction for arbitrary actual pairs, not just E1. Remove common
residual components, then study how the full residual intersection on
\(Q\) could concentrate on \(C\). Independently test whether high contact
forces an actual polynomial row representative into a forbidden
normal-order range. Formal cancellation over \(k(C)\) is not that
global representative.

This exchange already corrects two tempting asymptotic readings. The
weighted source excluded in every degree occupies a fraction of vector
space dimension tending to zero. Conversely E1's fixed-\(H\) family
occupies a fraction tending to one in its individual source, yet
retains an unavoidable global residual. Neither conclusion is generic
existence or universal non-existence.

## 5. Completed E3/N3 exchange and the surviving challenge

**Independent obstruction N3 — final scoped PASS.** For exact normal
order \(m\) and \(a\ge3m\), the actual quadric residual is
\(T\sim(a-m,a-3m)\). A reduced irreducible horizontal full normal root,
reduced transverse \(T\cap C\), and simple regular attachments give
one inverse curve \(\Gamma\to C\) of degree \(m\). A mate would force
\(bH\sim r\Gamma\), hence
\[
ab=4mr,\qquad b(2a-4m)=r(4a-6m).
\]
These require \(2a^2-7am+8m^2=0\), whereas that quadratic is positive.
The [final audit](notes/2026-10-31-stci-closeout-obstruction-audit.md)
checks that the hypotheses hold on a nonempty dense open of every full
actual source, without assuming full symbol surjectivity. On the
ordinary reducible-horizontal locus the mate-weighted slope must be
\(7-16m/a\), so at least one component has slope at most that value.
This independently broadens the non-existence program beyond E1/E2.

**Existence E3 — actual source, failed fixed member.** The
[elliptic double-lift](notes/2026-10-30-stci-game-existence.md) uses
\(E:y^2=x^3-x\), order-four torsion \(T=(i,1-i)\), and four actual
quadratic sections on a smooth quadric \(S_\mu\). Its marked elliptic
curve \(\Gamma\sim H=(2,2)\) maps with degree two to \(C_0\).
The saved fixed member \((\mu,\rho)=(2,0)\) is basepoint free and finite
birational onto a degree-eight surface. It fails: the affine
\(Q_0=1\) inverse scheme has length 24, giving projective isolated
inverse length 12. Those isolated points exclude every mate degree.

The same fixed image has normal order two, vertical first-symbol
degree twelve, and saturated horizontal class \((6,2)\) with elliptic
normalization. Its horizontal slope \(6/2=3\) equals
\(7-16m/a\) at \((a,m)=(8,2)\). This is an actual special-boundary
escape from the ordinary hypotheses, not an STCI construction.
The extra inverse scheme maps scheme-theoretically into the vertical
divisor; no equality, reducedness or multiplicity-one claim follows.

**Adversarial verdict.** N3 does not exclude E3's full five-parameter
source. E3 accepts the fixed-member failure and the need to absorb its
extra inverse support while preserving the actual map, then achieve
descent. The old degree-one inverse involution exclusion does not
automatically apply: the elliptic deck action sends
\(\mu\mapsto-1/\mu\), so it need not preserve the source surface.
The degree-five mate filter applies only where the actual quadratic
first normal form is verified irreducible. No higher mate search on
the failed fixed carrier remains justified.

The [projection closeout audit](notes/2026-10-31-stci-closeout-projection-audit.md)
separately accepts the degree-ten resultant/number-field classification
and preserves the explicit elliptic target that fails marked source
extension. The degree-twelve chart has no completed certificate. The
remaining primitive elliptic and order-one incidences are specified,
not computed.

## 6. Final interfaces, not new assignments

The [closeout report](notes/2026-10-31-stci-package-closeout.md) ranks
four unresolved interfaces and gives the exact next equations: full
inverse support then power descent in E3; primitive elliptic target
incidence then source extension; order-one marked projections; and
coverage of vertical/repeated/low-slope/nonordinary carrier loci.
The [independent geometric closeout review](notes/2026-10-31-stci-closeout-geometric-review.md)
checks the distinctions between these gates. No finite computation,
generic exclusion or numerical divisor compatibility closes the
unrestricted characteristic-zero question.
