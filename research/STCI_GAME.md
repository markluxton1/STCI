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

## 2. What the current results change

| Evidence | Existence response | Independent obstruction program | General-question limit |
| --- | --- | --- | --- |
| [R-0001](results/quartic_carrier_exclusion.md), including its accepted factor reduction | Seek defining degrees at least five | Do not reopen quartic mate cases; find mechanisms for higher degrees | Higher degrees remain open |
| [Global equation freedom](notes/2026-10-28-stci-search-freedom.md): fixed quadric factors below \(d=3m\), large sources afterward, symbol surjectivity at \(d\ge3m+2\) | Use actual source images and correlate the pair, rather than random independent leading forms | Study joint/global constraints and high-contact cancellation; a dimension count does not supply them | Individual-equation freedom does not decide paired support |
| [All-degree mixed-seed line obstruction](notes/2026-10-30-mixed-weight-line-obstruction.md) | Increasing the mate degree on this seed cannot help | Reuse actual curve attachment and divisor-degree balance on other carriers | Other sextic families are not excluded |
| [Uniform weighted-subalgebra theorem](notes/2026-10-30-weighted-subalgebra-line-obstruction.md) | Enter repeated/axis binary boundaries or leave the constant-coefficient \(k[q,c_0,c_2]\) source | Enlarge the incidence principle; attack the degenerate boundary independently | This source has asymptotically vanishing relative dimension in the full fixed-order space |
| [Quadric-boundary theorem and global row filter](notes/2026-10-30-stci-game-quadric-boundary.md), independently audited | Change the common cubic boundary or use corrections that can change its restriction on \(Q\) | Extend the fixed-residual principle beyond this large family; test global polynomial cancellation independently of the opponent's proposal | The family has asymptotically full relative dimension in its fixed-order source but is not exhaustive; its residual floor is not universal |
| [Projection boundary exclusion](notes/2026-10-29-projection-m2-boundary.md), [smooth residual conditions](notes/2026-10-30-projection-order-two-survivor.md), [global extension obstruction](notes/2026-10-30-projection-elliptic-target-incidence.md) | A primitive elliptic target must also extend to the actual marked source; use nonzero middle support coefficient | Solve the remaining primitive elliptic and order-one incidence, or derive a stronger extension principle | The full sixteen-parameter admissible and descent loci remain uncomputed; other normalization models remain separate |
| [Arithmetic higher-jet gap](notes/2026-10-29-arithmetic-beyond-binomial.md), attained by explicit two-non-binomial \((16,p)\) pairs | Fixed-degree persistence in infinitely many primes would matter; degree-\(p\) constructions do not provide it | Extend the jet mechanism beyond the specified 23-parameter source, or find another uniform all-pairs mechanism | The restricted minimum \(p\) does not bound the all-pairs \(\delta(p)\) below |
| [Residual constructions](notes/2026-10-28-containing-intersections-synthesis.md) and [quantitative bounds](notes/2026-10-28-residual-degree-synthesis.md) | Test whether actual linked families and attachment flexibility can absorb residual support while retaining equations | Identify which bounds are strictly positive on the proposed global family and which equality mechanisms survive | Flexible attachment is not increasing thickness; conditional positive bounds are not universal |

Every new result should update at least one entry here: remove a
construction, create a usable source, enlarge an exclusion, expose a
missing implication, or change the next decisive test. A theorem's
number of parameters or all-degree wording is not a measure of universal
coverage by itself.

## 3. First exchange: actual lifting freedom and its global boundary

The independently assigned advocates were interrupted by an account
usage limit before completing their first exchange. The following
opening moves are therefore **root-drafted strategies**, not attributed
team conclusions. The obstruction theorem has now received a separate
independent audit; the revised existence construction remains a proposal. The
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

## 4. Current independent research obligations

The existence side should return an actual revised global family and
its full endpoint test, or a construction from a different geometry.
It is free to challenge an obstruction by finding a case outside its
hypotheses or an actual counterexample.

The non-existence side should return both its strongest enlargement
theorem and its critique of the current construction. Useful programs
include extending the test-curve degree balance, resolving repeated or
axis-root boundaries, controlling global row cancellation, and
enlarging arithmetic jet gaps. The opponent's proposal does not set
the allowed scope of this work.

One reusable principle is to find actual curves on a carrier whose
attachments to the inverse branches are known. A hypothetical mate
must satisfy their divisor-degree equations as well as the hyperplane
degree equation. An inconsistency excludes the entire carrier family.
The work is to construct those curves and prove their attachments
uniformly; a generic normal symbol alone does not supply them. This is
a concrete use of the broader fixed-carrier divisor framework, not a
claim that the abstract framework has already been computed everywhere.

The referee should record which moves survive and update the common
state. No strategy note or uncompleted computation is promoted into a
canonical result. The unfinished projection calculation remains an
explicit live subproblem; the game is not restricted to it.
