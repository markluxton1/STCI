# October 24 ideal-filtration reconciliation (provisional)

**Status:** reviewed research evidence, **not** a promoted STCI theorem. Source notes: [investigation](notes/2026-10-23-ideal-filtrations-independent-investigation.md), [independent review](notes/2026-10-23-ideal-filtrations-independent-review.md), [continuation](notes/2026-10-24-delta-singular-locus-continuation.md), [continuation review](notes/2026-10-24-delta-singular-locus-review.md). Keep the original notes and computational certificates intact.

## Definitions and scope

Locally let (R=\mathcal O_{\mathbf P^3,p}), (I=I_C\), (J=(f,g)=I_Z\subset I\), (S=\operatorname{gr}_I R\), (H=\operatorname{in}_I(J)\subset S\), and (S_+=\bigoplus_{n>0}S_n\). Set (Q=H/S_+H\), (D=J/IJ\), and (F^nD=((J\cap I^n)+IJ)/IJ\). The comparison defect is (\Delta_n=\operatorname{in}_I(IJ)_n/(S_+H)_n\). Under the source hypotheses, there is an exact sequence (0\to\Delta_n\to Q_n\to\operatorname{gr}_F^nD\to0\).

## Evidence-supported takeaways, subject to canonical promotion audit

- The full embedding diagram retains the actual quotient (R/J\); its associated-graded shadow alone need not determine the filtered algebra. Preserve the Rees/extension information.
- Under the regular local ambient and complete-intersection hypotheses in the notes, the defect vanishes wherever either carrier is smooth along (C\). Thus (\operatorname{Supp}\Delta\subset C\cap\operatorname{Sing}(X)\cap\operatorname{Sing}(Y)\). This does **not** assert that the simultaneous singular locus is nonempty.
- The Koszul filtration yields a spectral sequence with (E_1^{i,n}=\operatorname{Tor}_i^S(S/H,R/I)_n\); higher differentials entering degree one account for the defect, subject to the filtration/convergence conventions stated in the continuation. At the generic point, in the specified finite-length complete-intersection setting, (\dim_{k(C)}\Delta_\eta=\mu(H_\eta)-2\).
- In the prescribed characteristic-two (4,4) example the source reports (\Delta=0\), with (\ker(D\to I/I^2)\simeq Q_4\simeq\mathcal O_{\mathbf P^1}(-24)\). The same equations in characteristic zero have a different component configuration. These example-specific conclusions do not imply a general STCI obstruction.
- Counterexamples with residual support **cannot** be cited as counterexamples under (\sqrt J=I\). Torsion of (Q\) alone does not imply nonzero (\Delta\).

## Outstanding checks before promoting individual results

1. Independently rerun the checked scripts, compare their outputs with the recorded certificates, and verify the claimed spectral-sequence indexing and convergence conventions.
2. Check all global sheafification, twisting, and transition-map assertions separately from local computations.
3. Distinguish the support-only hypothesis (\sqrt J=I\) from merely (C\subset V(J)_{\rm red}\). Determine whether a punctual nonzero defect is possible when (\sqrt J=I\) and (\Delta_\eta=0\).
4. Check that the hypotheses of any proposed promoted statement are no broader than those of its proof and independent review. Only then add an ID-bearing result record under the normal promotion process.

**No change** to the unrestricted characteristic-zero STCI status, the accepted quartic-carrier exclusion, or the standing prohibition on assuming simultaneous singularities.
