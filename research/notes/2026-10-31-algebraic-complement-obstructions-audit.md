# Algebraic complement classes: independent proof and strategy review

Date: 2026-10-31. Source:
[Algebraic Euler classes on complements](2026-10-31-algebraic-complement-obstructions.md).
Status: **scoped PASS, provisional**. No canonical promotion.

## Scope and independence

Two bounded scouts worked without inherited turns or nested delegation:

- /root/holomorphic_realization_literature, requested
  gpt-6-astra/xhigh: actual non-Stein Oka and q-convex realization
  theorems, with their exact source and conclusion requirements.
- /root/algebraic_section_realization_selection, requested
  gpt-6.1-sol/high: algebraic extension and characteristic-class
  literature; supplied the initial Chow–Witt comparison derivation.

The parent extracted its generalization from C0 to every smooth
connected space curve. A fresh independent reviewer,
/root/algebraic_complement_independent_challenge, requested
gpt-6-astra/xhigh with no inherited turns and no nested delegation,
challenged both the recommended bounded test and its proof. These
requests identify the selected routes, not independently measured
model performance.

The reviewer first approved the bounded uniform comparison as a useful
test with an explicit stop at the primary Euler detector. The parent
reported that recommendation and stopping rule before writing the proof.
The reviewer then independently reconstructed the mathematics and checked
the actual final source. All three assignments are complete.

Reviewed final source SHA-256:
4909cb4370d3d6870bcf302755daf33b23a560c34c52065013bac00ea3aeb733.

## Reconstruction and material failure modes

1. **Field, curve and twist.** The proof works for any smooth connected
   closed curve in P3 over an algebraically closed field of characteristic
   different from two. Rationality and genus zero are not used.
   Asok–Fasel Proposition 5.1 gives I4(L)=0; the quotient identifies
   I3(L) with K3-Milnor mod two for every line bundle L. There is no
   unmentioned square-root or orientation hypothesis.
2. **The nonaffine step.** The reviewer checked the actual Bloch–Ogus
   edges, not just the statement of the affine Proposition 5.2.
   No differential reaches or leaves (2,3) or (3,3); rows and columns
   outside the three-dimensional range vanish. The retained surjection
   from H5-etale and isomorphism from H6-etale are valid without affineness.
   In this case the former can also be strengthened to an isomorphism,
   but that strengthening is unnecessary and not used.
3. **Point pushforward.** In the purity sequence, H2(C,mu2) to
   H6(P3,mu2-tensor3) maps a degree-one point to the point generator.
   It is an isomorphism, irrespective of d or g. Confusing it with
   the separate H0(C) to H4(P3) map would break the argument.
   This supplies exactly the two cohomology vanishings needed instead
   of the affine vanishing theorem.
4. **Conclusion, not representability.** The exact Milnor–Witt sheaf
   sequence proves that the twisted Chow–Witt forgetful map is an
   isomorphism. The characteristic Euler class forgets to c2. The
   reviewer retained determinant dual as its twist and did not import
   the oriented comparison theorem as a general nonaffine splitting
   theorem. No algebraic section or direct-summand sufficiency follows.
5. **Integral K-theory.** Localization and Hilbert polynomials give
   [O_C]=d t2+(1-g-d)t3 and the quotient by (d t2,t3).
   The t3 coefficient is not the Chern-character H3 coefficient.
   The necessary virtual extension defect is exactly -ab t2.
   Genus and degree-zero Picard classes do not survive pushforward here.
6. **Realization controls.** The (1,d) bundle for a nonplanar curve
   passes the characteristic-class and continuous tests but cannot
   have a holomorphic nowhere-zero section. Hartogs forces an actual
   linear equation containing the curve. This refutes an unqualified
   realization principle without excluding successful pairs in other
   degrees.

The actual-source pass found three missing LaTeX thin-space backslashes
in the K-theory display and prose. They were corrected; the algebra had
not changed. The review also supplied the direct Milne purity/trace
reference, which was added. No material mathematical correction remained.

## Literature and strategy adjudication

The reviewer checked the exact analytic theorem boundaries. Stopar's
section theorem requires a 1-convex source, excluded here by Hartogs and
proper Remmert reduction. Fornæss–Sibony–Wold provides two positive
Levi directions with corners, short of the three required by its
line-bundle extension theorem in dimension three; that theorem also
does not supply the specified rank-two section. Forstnerič's
subellipticity result concerns U as a target for Stein sources.

The independent challenge found no concrete construction in those
checked sources that the recommendation overlooked. This is a bounded
literature conclusion, not proof that no suitable realization theorem
or construction exists.

The review supports closing ordinary Chow, this virtual K-class
condition, and the twisted characteristic Euler detector. It does
not support closing all motivic, singularity-dependent, or carrier
geometry. A future experiment needs an actual section/descent operation
or a specified further obstruction with an independently evaluable
formula and an implication for arbitrary pairs. No such next experiment
was selected. The result is compatible with C0 being STCI.
