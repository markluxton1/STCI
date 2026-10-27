# Mathematical consolidation: characteristic jumps, four-sheet geometry, and arithmetic nonlifting

**Status:** thematic synthesis, not a new theorem. Sources: canonical R-0012, R-0020, R-0021, R-0029, R-0031 and their cited audits.

## Four distinct mechanisms

1. **Conormal extension (R-0020).** For the fixed rational quartic, 0→O(-8)→N^*→O(-6)→0 has extension class a nonzero scalar multiple of 2 in H^1(O(-2)). Thus N^*=O(-7)^2 when 2 is invertible, but O(-8)⊕O(-6) in characteristic two. This is an embedded-bundle fact, not an STCI obstruction.
2. **Group-scheme coalescence (R-0021).** For F=x1^4-x0^3x3 and G=x2^4-x0x3^3, the intersection is flat over Z. On its dense torus it is G_m×mu4. Characteristic zero has four distinct rational quartic components; characteristic two has sole reduced support C0 and generic transverse algebra K[Y]/Y^4. Flatness of the total family does not imply support stays on C0.
3. **Actual fourth equation (R-0031).** For that char-two pair the first conormal image is O(-8), cokernel O(-6), and filtered equation-module kernel O(-24). The full initial ideal has a minimal degree-four normal generator Q4=O(-24), canonically identified with the equation-module kernel with zero comparison defect. This is an explicit case where two first symbols fail to generate the full initial ideal; it is not universal.
4. **Arithmetic support-preserving nonlifting (R-0012).** No flat embedded lift of the *prescribed special fiber* over Z_(2) or Z_2 has generic reduced support the fixed relative quartic. The obstruction is a primitive-triple class in H^1(P1_R,O(-4)), with middle Laurent coefficient congruent to 2 mod 4. This does not rule out arbitrary ramified DVRs, the ribbon alone, arbitrary characteristic-zero quadruple thickenings, or characteristic-zero STCI in general.

## Ruled geometry clarifies the endpoint issue (R-0029)

For the fixed arithmetic cone, normalization is weighted P(1,1,4), with ruled resolution F4. The four-section divisor is finite flat of degree four over P1, but scheme image can fail to commute with endpoint restriction, and normalization of the total reduced arithmetic family differs from normalization of the reduced special fiber. The distinction explains why an attractive four-branch drawing does not automatically describe the embedded special fiber at the marked endpoints. All statements concern this prescribed model.

## Failed shortcuts to preserve

- **'Flat over Z means a support-preserving lift.'** False: the flat integral pair develops three additional characteristic-zero quartic components.
- **'The conormal bundle splits, so a fourth equation exists globally.'** Not a valid implication; the actual equations and overlap compatibility are essential.
- **'The two first normal symbols generate the initial ideal.'** False for the prescribed characteristic-two pair; cancellation creates the fourth-order relation.
- **'Nonlifting over the two unramified bases proves nonlifting over every mixed-characteristic base.'** Not established.
- **'The characteristic-two model is representative of all characteristic-two STCI constructions.'** Not established; the canonical results concern this fixed pair.
- **'Specialization and normalization commute at the endpoints.'** R-0029 gives explicit contrary behavior.

## Architectural recommendation

Use one **Characteristic and arithmetic geometry** chapter with four distinct sections: embedded conormal extension; mu4 coalescence and actual initial ideals; ruled endpoint/normalization geometry; support-preserving arithmetic nonlifting. Place the concrete integral pair at the beginning and return to it at each level. Keep R-0012 and R-0020/21/29/31 as separate scoped theorem authorities, since the implications between them are not equivalences. Cross-link to the normal-filtration chapter and to residual-cycle geometry (the extra characteristic-zero quartics are genuine residual components downstairs).

## Next content review

Review intrinsic projective/dual/ruled geometry (R-0026–R-0028, special planes and lines, automorphisms and bitangents). Determine which geometry is a reusable foundation for STCI work and which is a special calculation or speculative obstruction. Preserve the geometric interpretation without treating every incidence identity as an STCI constraint.
