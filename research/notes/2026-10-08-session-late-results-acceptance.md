# Root reconciliation of the late October 8 results

Date: 2026-10-08, America/New_York. Fixed C0 in characteristic zero.
The universal STCI question and unrestricted C0 question remain OPEN.
This note promotes completed proofs with their exact scopes; it does
not turn the principal ancestor exclusion into a carrier theorem.

## 1. The entire e=1,d2=1 common quartic ancestor lane

**PROVED under the accepted canonical-triple reduction and P-037.**
No common quartic ancestor of the two fixed independent targets has
e=1 and a genuine second defect of degree one.

The [independent principal completeness audit](2026-10-08-session-principal-e1-d1-independent-completeness-audit.md)
exhausts the principal chart and its projective complement. On the
declared open the complete eighteen-dimensional quartic ideal space
has first/contact rank 17. The first-normal determinant, complete
seven-column frame, all seven cofactors, resultant gcd, quadratic-field
fibre and the retained nonunit S branch are checked exactly. The
alternative killing section at infinity is reconstructed in the actual
balanced chart. All three b0=0 conjugates are retained.

The sole dimension exception is (p,r)=(2,1/2): the complete quartic
space has dimension four, with a fixed cubic times every linear form.
It is excluded by division and P-037. Every other valid principal
fibre has quartic dimension one, so cannot produce independent targets.
A uniform dimension-one assertion on the whole lane would be false.

Root rechecked the antecedents: the six nonprincipal endpoint triples
are exhausted and excluded by their complete quartic spaces in the
[endpoint ancestor proof](2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md).
At the primitive obstruction-zero point, the only correction has no
additional H0(O(-3)) freedom; multiplication by a degree-one killing
section shares its zero, so it is not a genuine finite-flat positive
defect triple. The principal and endpoint pieces therefore exhaust
the degree-one ancestor lane. The surviving e=1 ancestor degrees are
d2=2,3,4, with the separately excluded quadric and algebraic directions
still removed.

Root's isolated open-proof replay exited zero in 83.978 seconds; its
[central transcript](../validation/2026-10-07-continuation/verify_session_mf6_principal_rank_open_2026_10_08.log)
binds source SHA256
2fbefebda6723b7d721f0034c0167a2c70a3b79eed01675b99baf453453a9ac8.
The independent auditor's four own executions, source snapshots and
input closure are in the
[principal audit manifest](../validation/2026-10-08-principal-e1-d1-audit/audit-manifest.json).
The copied owner replay is not counted as an auditor execution.

## 2. Smooth quartic scrolls: reduced or locally Gorenstein conductor

**PROVED:** if an integral quartic X has smooth rational quartic-scroll
normalization and its actual downstairs conductor Gamma is reduced
or locally Gorenstein, X has no mate supported only on C0, in any
positive degree. The theorem retains arbitrary upstairs conductor D.

The actual conductor is an ACM cubic with Hilbert polynomial 3m+1;
this is a scheme-level result, not a claim about the Jacobian radical.
The [ACM audit](2026-10-08-session-scroll-acm-independent-audit.md)
and [owner proof](2026-10-08-session-scroll-degenerate-conductor.md)
derive its Hilbert--Burch presentation and the exact sequence
0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.
The reduced theorem includes the smooth twisted cubic, conic plus line,
and all three-line configurations. The concurrent three-line case is
excluded geometrically before any flat-cover assertion. See the
[conic-plus-line audit](2026-10-08-session-scroll-conic-line-independent-audit.md)
and [three-line audit](2026-10-08-session-scroll-three-lines-independent-audit.md).

For locally Gorenstein Gamma the exact sequence makes p finite flat
of rank two even when Gamma is nonreduced. A locally Gorenstein triple
line is impossible: devissage makes the degree of every invertible
sheaf divisible by three, while deg(omega_Gamma)=-2. The doubled-line
generic Artin algebra gives only the partitions (a,r)=(4,1),(2,2),
or two (2,1), with a the upstairs nilpotent length and r the residue
extension degree. The F0/F2 anticanonical classes exhaust these cases.
Disjoint paired fibres and the global prime-exchange incidence
obstruction remove the exchanged-prime configurations. In the remaining
cases the involution preserves every conductor prime. The equation
sigma(f)^n=f^n then forces sigma(f)/f=+1 or -1 in each entire generic
Artin ring, with no nilpotent correction. Cohen--Macaulay purity extends
square invariance globally, and the conductor square descends f^2 to
the forbidden quadric mate. The
[independent Gorenstein audit](2026-10-08-session-scroll-gorenstein-independent-audit.md)
accepts this scope. Root checked the thick-base partitions and the
prime-exchange qualification; reduced-fibre reasoning alone would not
justify them.

**Retained boundary at this intermediate acceptance:** an actual conductor that is
both nonreduced and not locally Gorenstein. Classification and an
actual differential obstruction are being independently audited; the
proposed extension is not a premise of the theorem accepted here.
Singular normalizations and higher carrier degrees remain separate.

## 3. The principal exceptional quartic (p,r)=(8,1/2)

**PROVED all-mate exclusion of this fixed carrier.** Its explicit
normalization is F0. In invertibly changed coordinates the equation is
(xL-8yz)^2-x^3(x-8y), L=96w+x-8y+4z. The entire downstairs conductor
is (x^2,xy,xL-8yz), a double line plus a line; its upstairs divisor is
2{U=0}+2{b=0}. The actual nonreduced conductor is locally Gorenstein,
so its complete finite flat algebra, including nilpotents, gives the
square compression in section 2.

The [owner proof](2026-10-08-session-mf6-rhalf-scroll-conductor.md)
and [independent audit](2026-10-08-session-mf6-rhalf-scroll-independent-audit.md)
bind this equation to the unique actual boundary quartic. Root
independently derived the normalization-ring closure and all six
annihilator identities. Hilbert--Burch and the actual conductor Hilbert
polynomial prove equality of the entire ideal sheaves, not just their
support. A fresh isolated root replay of the
[checker](../computations/verify_session_mf6_rhalf_scroll_2026_10_08.py)
passed in 0.591 seconds, source SHA256
9d532c25c9f50f206e0d57c5ce7f35b9feb54707bf1b630fd622c0c473028aa2.
Its [transcript](../validation/2026-10-07-continuation/verify_session_mf6_rhalf_scroll_2026_10_08.log)
retains the command and source/log hashes.

The other complement carriers were already excluded as normal quartics
or quartics singular along smooth twisted cubics. The generic principal
carrier problem remains distinct. Its nonnormal locus is a proper
closed finite subset of the geometrically integral direction curve:
the unique quartic kernel gives a regular projective family away from
the treated node, and a normal b0=0 fibre makes the closed
positive-dimensional Jacobian-fibre locus proper. The exact finite
subset is not yet enumerated. See section 6 of the
[boundary proof](2026-10-08-session-mf6-principal-boundary-audit.md).

## 4. Execution and continuation state

The original usage-limit interruption was followed by successful
resumptions. A later 7:59 PM reset was independently checked at
2026-10-09 01:01:59 UTC; current usage allowed ordinary work, and the
assigned agents resumed. An earlier root poll could not access another
agent's process 60266; its owner subsequently observed that process
terminal with exit zero. An unavailable root handle is not evidence
that the owner's observation failed. No root process is claimed live
from a source file or an intended command.

The [reconciled index](../validation/2026-10-08-continuation-index/index.json)
currently includes 91 distinct latest-PASS top-level sources and 103
explicitly indexed executions, including the four actual independent
principal executions. The baseline was retained. Earlier failed checks
and the superseded Veronese source-byte retention limitation remain
explicit. These counts establish provenance and execution scope; they
do not substitute for the geometric proofs.

## 5. Final accepted extension: every smooth rational quartic scroll

**PROVED:** let X be an integral quartic with finite normalization S=F0,
H=C+2f, or S=F2,H=C+3f, over an algebraically closed characteristic-zero
field. No hypersurface of any positive degree has intersection with X
supported exactly on the fixed C0. Both actual conductor schemes are
unrestricted. This supersedes the intermediate conductor boundary in
section 2, while retaining singular normalizations and other polarized
normalization classes as separate work.

The [nongorenstein classification](2026-10-08-session-scroll-nongorenstein-cubic-classification.md)
uses the actual three-by-two linear Hilbert--Burch matrix. Its projective
rank-zero locus is a point or a line. The point case is a cone over a
noncollinear length-three scheme in P2; saturation and absence of linear
ideal forms, not merely h0(O_Z(1))=3, prove noncollinearity. The residual
nonreduced nongorenstein ideals are the double-line-plus-line,
curvilinear triple-line, and fat triple-line ideals. The locally
Gorenstein cases were already covered in section 2.

At a curvilinear triple line A=K[epsilon]/epsilon^3, B is free of rank
two. Multiplication by epsilon has K-rank four. Its truncated-DVR
factors have ranks bounded by two thirds of their lengths, so equality
forces every actual upstairs multiplicity divisible by three. This
contradicts the coefficient two of C in D=-K_S.

For a fat triple line A=K+N,N^2=0,dim N=2, the exact quotient B/A=omega_A
gives dim NB=3 and dim B=6. The finite product of truncated DVR factors
is Frobenius over K. Since (NB)^2=0, NB=Ann_B(NB); consequently every
conductor multiplicity is even. Thus D=2E with E=C+f on F0 or C+2f
on F2. A prime E has degree three over the supporting line and would
need three transverse totally ramified intersection points with c;
Riemann--Hurwitz permits at most two. A horizontal degree-two component
plus a degree-one fibre forces a double zero at one ramification point,
contradicting transversality of the smooth image. Distinct fibres give
two different normalization points above the same required zero. The
only remaining class is D=2C_min+4F on F2.

That final pattern has NB_F=(t^2) in its length-four factor. Ambient
normal coordinates to the support line therefore vanish to order at
least two along F, making d nu generically rank one there. The
[independent differential lemma](2026-10-08-session-normalization-differential-independent-audit.md)
excludes it. Root checked the lemma directly: a unit Jacobian pivot
gives a regular kernel vector modulo the prime ideal of the conductor
component. Differentiating the full power identity in an ambient-unit
trivialization yields n f^(n-1)V(f)=0 on that integral component.
Cancellation takes place generically, followed by extension in the
domain; it does not divide by f at its zero. At an intersection with
the smooth c, its tangent is the kernel, contradicting immersion of
nu|c. The lemma also permits singular conductor primes. An isolated
differential rank-drop point does not satisfy its hypothesis.

Finally, the [exact Artin audit](2026-10-08-session-scroll-artin-independent-audit.md)
completes double-line-plus-line conductors directly, including the
nongorenstein junction. Above the doubled line, free rank two over
K[epsilon]/epsilon^2 gives only (a,r)=(4,1),(2,2), or two (2,1).
Above the reduced line the patterns are (2,1),(1,2), or two (1,1).
The (4,1) and (2,1) single-prime cases have generic rank-one differential
and are excluded. On F0 the remaining doubled horizontal prime leaves
two distinct paired fibres. On F2 the remaining doubled minimal section
and fibre likewise leave paired fibres, or two doubled fibres leave an
impossible reduced-line component class. Every pattern is therefore
excluded. No global trace through a nongorenstein point is asserted.

This proof uses entire Artin rings and the whole mate equation. The
alternative transversal-plane delta argument is retained as a proposed
secondary route; it is not needed for the accepted theorem. The
independent Artin audit, differential audit, the
[complete independent scroll audit](2026-10-08-session-scroll-nongorenstein-independent-audit.md)
and root verification supply the promoted scope. No broad classification of all nonnormal quartic
surfaces is inferred from the classification of these ACM cubics.

## 6. Accepted second-family quadratic exceptions

Both factors k^2+1 and k^2-2k-1 are excluded at all four geometric roots
and for every lower parameter lambda. The
[owner proof](2026-10-08-session-localcoh-family2-quadratics.md)
and [independent audit](2026-10-08-session-localcoh-family2-quadratic-independent-audit.md)
check polynomial duals with n^T L=0 and n^T u=1 on all eighteen actual
quartic columns. Separate exact-field arithmetic rederives the seeds,
directions, slopes, rank-29 top map and complete affine lift fibre.
A fresh Macaulay2 reconstruction binds all 540 products and both target
columns literally and proves equality with the complete next-stage Ext
image. The [aggregate manifest](../validation/2026-10-08-family2-quadratic-audit/audit-manifest.json)
retains all input/source hashes, isolated replay, countercheck and tensor
execution history, including two preparatory failures.

The remaining second-family locus is 22 geometric points from factors
of degrees 3,4,15, each retaining its entire lambda fibre OPEN. No
survivor or rank jump is inferred from being an exception to the old
generic dual. Other endpoint families and nonendpoint top zeros remain
open.
