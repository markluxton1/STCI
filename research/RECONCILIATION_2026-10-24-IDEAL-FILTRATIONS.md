# October 24 ideal-filtration reconciliation (provisional)

**Status:** reviewed research evidence, **not** a promoted STCI theorem. Source notes: [investigation](notes/2026-10-23-ideal-filtrations-independent-investigation.md), [independent review](notes/2026-10-23-ideal-filtrations-independent-review.md), [continuation](notes/2026-10-24-delta-singular-locus-continuation.md), [continuation review](notes/2026-10-24-delta-singular-locus-review.md). Keep the original notes and computational certificates intact.

## Definitions and scope

At a point \(p\in C\), put \(R=\mathcal O_{\mathbf P^3,p}\),
\(I=I_C\), \(J=(f,g)=I_Z\subset I\),
\(S=\operatorname{gr}_I R\), \(H=\operatorname{in}_I(J)\subset S\),
and \(S_+=\bigoplus_{n>0}S_n\). Set
\(Q=H/S_+H\), \(D=J/IJ\), and
\(F^nD=((J\cap I^n)+IJ)/IJ\).
The comparison defect is
\(\Delta_n=\operatorname{in}_I(IJ)_n/(S_+H)_n\).
With the induced filtration there is an exact sequence
\[
0\longrightarrow\Delta_n\longrightarrow Q_n
\longrightarrow\operatorname{gr}_F^nD\longrightarrow0.
\]
Here the image of \(IJ\) in the graded construction must use the **full initial ideal** \(\operatorname{in}_I(IJ)\), not the initials of a chosen generating list.


## Evidence-supported takeaways, subject to canonical promotion audit

- The full embedding diagram retains the actual quotient $R/J$; its associated-graded shadow alone need not determine the filtered algebra. Preserve the Rees/extension information.
- Under the regular local ambient and complete-intersection hypotheses in the notes, the defect vanishes wherever either carrier is smooth along $C$. Thus $\operatorname{Supp}\Delta\subset C\cap\operatorname{Sing}(X)\cap\operatorname{Sing}(Y)$. This does **not** assert that the simultaneous singular locus is nonempty.
- The Koszul filtration yields a spectral sequence with $E_1^{i,n}=\operatorname{Tor}_i^S(S/H,R/I)_n$; higher differentials entering degree one account for the defect, subject to the filtration/convergence conventions stated in the continuation. At the generic point, in the specified finite-length complete-intersection setting, $\dim_{k(C)}\Delta_\eta=\mu(H_\eta)-2$.
- In the prescribed characteristic-two (4,4) example the source reports $\Delta=0$, with $\ker(D\to I/I^2)\simeq Q_4\simeq\mathcal O_{\mathbf P^1}(-24)$. The same equations in characteristic zero have a different component configuration. These example-specific conclusions do not imply a general STCI obstruction.
- Counterexamples with residual support **cannot** be cited as counterexamples under $\sqrt J=I$. Torsion of $Q$ alone does not imply nonzero $\Delta$.

## Outstanding checks before promoting individual results

1. The source branch reports independent reviews and successful script runs (see both validation READMEs). These are **inherited checks**, not newly replayed by this reconciliation. A fresh independent replay and comparison against recorded logs is still required for a new certification. Verify spectral-sequence indexing and convergence conventions against the continuation proof.
2. Check all global sheafification, twisting, and transition-map assertions separately from local computations.
3. Distinguish the support-only hypothesis $\sqrt J=I$ from merely $C\subset V(J)_{\rm red}$. Determine whether a punctual nonzero defect is possible when $\sqrt J=I$ and $\Delta_\eta=0$.
4. Check that the hypotheses of any proposed promoted statement are no broader than those of its proof and independent review. Only then add an ID-bearing result record under the normal promotion process.

**No change** to the unrestricted characteristic-zero STCI status, the accepted quartic-carrier exclusion, or the standing prohibition on assuming simultaneous singularities.


## Evidence inventory and maintenance

- [October 23 exact checks](validation/ideal-filtrations-2026-10-23/README.md): three standard-library Python scripts and canonical metadata validation; recorded successful runs.
- [October 24 exact checks](validation/delta-singular-locus-2026-10-24/README.md): Python polynomial checks, Macaulay2 Rees checks, and canonical metadata validation; recorded successful runs.
- [October 23 review](notes/2026-10-23-ideal-filtrations-independent-review.md) explicitly checks the comparison direction, denominator, chart transitions, and smooth-carrier support theorem.
- [October 24 review](notes/2026-10-24-delta-singular-locus-review.md) explicitly checks the normal Koszul complex (not the carrier Koszul complex), Tor identification, edge filtration, convergence qualifications, generic count, and DVR torsion formula.

**Audit status of this integration:** documentary cross-check completed; fresh executable replay not performed here. The source branch's independent-agent reviews and logged PASS results must not be represented as a new independent verification. No result-ID promotion is authorized by this integration alone.
