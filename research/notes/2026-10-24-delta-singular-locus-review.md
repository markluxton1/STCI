# Review record: singular-locus Delta continuation

Date: 2026-10-24.

Target: [continuation report](2026-10-24-delta-singular-locus-continuation.md).

Status: **independent mathematical reconstruction completed for the claims identified below; provisional research, not canonical acceptance**.

## Review method and actual assignments

These are independent agent investigations followed by primary-agent synthesis. They are not human referee reports. The review distinguishes general proofs, exact finite calculations, and unresolved questions.

| Task | Independently reconstructed material |
|---|---|
| lifting_audit | \(Q=\operatorname{Tor}_1\); filtered normal Koszul complex; exact induced filtration on \(J/IJ\); accumulated differential description; degree bounds; generic count; DVR torsion length formula |
| diagrams_derived | Generic generator excess; negative consecutive cancellations; recursive family, Hilbert–Burch shifts and explicit page; integral perturbation upgrade |
| diagrams_derived/family_singular | Independent recursive-family recurrence, full initial ideal by resultant/colength, defect degrees, and integral-carrier upgrade; subsequent cross-check of sections 3–6, including the Tor filtration, DVR formula, punctual family and cancellation page |
| singular_family | Punctual family of arbitrary degree and length; elementary complete symbol-syzygy calculation and exact lifts; special-fibre distinctions; actual residual support |
| completeness | Independent Rees-saturation replay of the punctual family for three thickness parameters; symbolic lifted identities; degree-four module calculation; actual finite-flat rank and residual distinction |
| Primary agent | Separate derivations of the Tor edge and torsion formula; generalization of the punctual family to degree three; irreducibility arguments; supported quadruple and its full graded modules; inspection and replay of saved computations |

The normal Koszul complex is \(K_{R/J}(x,y)\), not the earlier carrier Koszul complex \(K_R(f,g)\). The distinction was checked explicitly, including both first pages.

## Substantive checks and qualifications

### 1. The relative homological theorem

Applying Tor to \(0\to H\to S\to S/H\to0\) identifies \(Q\) with \(\operatorname{Tor}_1^S(S/H,B)\). Filtering the normal Koszul complex with generator weight one gives
\[
E_1^{i,n}=\operatorname{Tor}_i^S(S/H,B)_n.
\]
The connecting map sends a filtered cycle \((a,b)\) to \(ax+by\in J\cap I^n\), proving that the target filtration is exactly the earlier intrinsic filtration. This is a reconstruction, not an appeal to a spectral-sequence existence statement with unspecified target filtration.

Homological-degree-zero Tor is supported only in internal degree zero. Thus no outgoing differential removes a positive-degree class of \(Q\). The kernel of its edge map is precisely the cumulative incoming differential images from homological degree two. The report gives a filtration by those images and does not claim a canonical splitting or preferred individual pairing.

The complete/noetherian/good-filtration convergence boundary is stated. The primary agent added the explicit bounded strictness estimate from Artin–Rees and its correction of approximate cycles. No assertion about arbitrary filtered complexes is made.

### 2. Generic counts and special-point torsion

The formula \(\dim_L\Delta=\mu(H)-2\) follows by summing the intrinsic comparison and using \(\dim_LJ/IJ=2\). It is not inferred merely from the inequality between Betti numbers.

Over a DVR, generic vanishing gives equal generic ranks in \(Q_n\to G_n\). The induced map of free quotients is surjective of equal rank and hence invertible. This proves the exact sequence of torsion modules and the subtraction in the length formula.

The distinction matters: a torsion-free \(Q\) excludes punctual defect under generic vanishing, whereas torsion in \(Q\) by itself does not imply defect.

### 3. Punctual family

For \(a=t^r\), \(m\ge2\), the two symbol syzygies of
\((aX,aY,XY^m-Y^{m+1})\) were determined completely, including reduction modulo the nonreduced ring \(D/(a)\). Nonzerodivisibility of \(Y^m(X-Y)\) there follows from its monic factors, not from a false assertion that \(D/(a)\) is a domain.

Both symbol syzygies lift exactly with strictly higher normal corrections. The resulting standard-basis proof establishes the full relative initial ideal for all parameters. The injective first conormal matrix is \(\operatorname{diag}(t^r,t^r)\), of generic rank two. It was not confused with a rank-one map.

The degree-three case has a regular quadratic actual closed-fibre initial ideal and zero fibre defect. It requires separate treatment from higher degrees. Thus the report does not claim defect formation commutes with base change.

The actual finite-flat rank is \(m+2\), whereas the marked component has generic length one. The residual rank \(m+1\) is therefore real geometric support. This family is not presented as a supported multiple curve.

### 4. Recursive family and actual carrier hypotheses

Two independent derivations checked the recurrence, full initial ideal, quotient colength, and
\[
\Delta=\bigoplus_{i=2}^nL(-[n+(q-1)i]).
\]
The matrix containing units is nonminimal over the local ring. Its associated graded matrix, which drops those units, is minimal. The report retains this distinction.

The condition \(q\ge3\) is essential: at \(q=2\), the dropped entries have the same weight and the displayed initial ideal argument fails. For \(q\ge3\), every canceled pair has gap \(q-2\). The generic unbounded-rank assertion is not deduced from the punctual torsion family.

The recursive generators themselves need not be integral. The high-order, primitive linear-in-\(t\) perturbations were separately proved irreducible and shown to preserve the completed local ideal by an identity-modulo-\(I\) generator change. The global projective upgrade permits residual support and concerns a marked line, not the fixed rational quartic.

### 5. Supported control example

The primary agent derived the supported quadruple independently from the free \(D\)-basis \(1,x,y,xy\), then verified both full initial ideals by Rees saturation. This example has nonzero torsion in \(Q_2,Q_3\), but that torsion survives in \(G_2,G_3\); hence \(\Delta=0\).

This calculation is separately labelled from the independently derived family theorems. It supplies no vanishing theorem for every supported multiple curve. The possibility of a nonzero punctual defect with \(\sqrt J=I_C\) and \(\Delta_\eta=0\) remains explicitly open in this report.

## Computation scope and development repairs

The [validation directory](../validation/delta-singular-locus-2026-10-24/README.md) preserves the final successful outputs.

The Python and Macaulay2 implementations are independent. Python expands complete products before extracting initials. Macaulay2 forms the full Rees-saturated initial ideals, not just the initials of the supplied equations.

During script construction, the primary agent corrected a reserved Macaulay2 variable name, converted interval sequences to lists for matrix construction, and parenthesized an ideal before exponentiation. These were syntax repairs; the final script completed all assertions. No failed syntax run is treated as mathematical evidence.

The computations do not establish arbitrary-parameter theorems, irreducibility, spectral-sequence convergence, or global STCI conclusions by sampling. Those require the proofs and precise hypotheses in the report.

## Authority and remaining dependency

The predecessor is a reviewed proposal on the same branch, not a canonical result record. This continuation uses its exact comparison and smooth-carrier proposition within their original scope. The new propositions remain proposals with proofs and independent reconstruction. Canonical results and questions have not been edited.

The main unresolved implication is now the supported, generically defect-free, isolated-point case. The residual family must not be substituted for a solution of that problem.
