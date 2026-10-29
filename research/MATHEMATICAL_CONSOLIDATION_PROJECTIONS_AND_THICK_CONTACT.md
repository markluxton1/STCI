# Mathematical consolidation: normalization models, projection phases, and entirely-thick intersections

**Status:** explanatory synthesis, not theorem promotion. Source review: R-0002, R-0004, R-0017, legacy `results/entirely_thick.md`, `open/entirely_thick.md`, and principal projection notes.

## A sequence of different mathematical questions

1. **Necessary normalization models (R-0002).** Assuming an actual mate, finite normalization, full reduced singleton inverse support c mapping isomorphically to C, and Cartier c upstairs, the normalization is a normal surface of minimal degree. For C0, after the low-degree carrier exclusion, possible models are a degree-eight smooth quadric, degree-eight quadric cone, and degree-sixteen plane normalization. Necessary models are not constructions.
2. **Existence of an admissible projection.** One must construct a basepoint-free finite birational map with full inverse support exactly c, including no isolated inverse points. This is separate from the abstract normalization classification.
3. **Descent of a positive divisor (R-0003).** A mate exists precisely when the full conductor descent lattice contains a strictly positive vector on every inverse branch, under its stated fixed-carrier hypotheses. Reduced support alone is insufficient.
4. **Family phase reduction (R-0004).** For admissible Cartier singleton projection families, full nilpotent conductor equations are retained through stratification and finite cover, and mate existence becomes torsion of a phase tuple in a torus. A finite torsion-coset envelope is structural; actual phase images and torsion cosets are not computed. Mate loci need not be constructible.
5. **Explicit obstruction (R-0017).** A specified degree-sixteen plane projection family has finite birational normalization, exact singleton inverse support, but no mate in any degree. The failure is a first-order nilpotent conductor term invisible to reduced residue data. The result does not exclude every degree-sixteen plane projection.

## Concrete geometric example

The source `notes/2026-10-19-singleton-projection-investigation.md` uses four quartics on P2:
`[s^4:s^3t:st^3+z^4:t^4+s^3z]`.
On s≠0, with x=t/s and n=z/s, the map is `(x,x^3+n^4,x^4+n)`, hence birational there. The image is an integral degree-sixteen hypersurface; the normalization is P2. The full inverse support of C0 is z=0, but conductor descent fails for every positive power. The example should be kept as a **counterexample to the tempting sufficiency of inverse-support conditions**, not buried as an incidental computation.

## Entirely-thick is a different branch

The legacy `results/entirely_thick.md` and `open/entirely_thick.md` study pairs whose **both** equations have generic normal orders p,q≥2 along C0. Blowup and quadric restrictions yield necessary inequalities
`ab≥4pq`, `7ab+28pq≥16(aq+bp)`, `a≥3p`, `b≥3q`.
The normalized (3,3) boundary is excluded; the (3,4) equality boundary forces repeated-root geometry. These do **not** exclude the branch: fixed first tangent forms permit arbitrarily high transverse contact, requiring higher valuation/Rees information.

This is not another carrier-normalization model. It is an **equation-side** decomposition of possibilities and belongs with the filtered/normal-thickening chapter, cross-linked to carrier arguments where relevant.

## Equality rigidity on the quadric and the open ambient lift

Let \(Q\cong\mathbf P^1\times\mathbf P^1\) be the unique smooth quadric containing \(C_0\), with \([C_0]=(1,3)\), and let \(h\) cut out \(C_0\) on \(Q\). If a degree-\(3p\) ambient form \(F\) has generic normal order \(p\) along \(C_0\), then
\[
F|_Q=h^pR_F,\qquad R_F\in H^0(Q,\mathcal O_Q(2p,0)).
\]
This has **exact** order \(p\) along \(C_0\): divisibility of \(R_F\) by \(h\) would require a nonzero section of \(\mathcal O_Q(2p-1,-3)\), which does not exist. Every effective divisor of type \((2p,0)\) is a sum of ruling fibers, so \(R_F=\lambda\prod_i\ell_i^{M_i}\), with \(\sum M_i=2p\). For a hypothetical entirely-thick STCI equality pair of degrees \((3p,4q)\), the **separate exceptional-cycle argument** bounds the number \(r\) of distinct fibers by \(r\le\min(p,q)\). This is a necessary consequence, not a converse or an existence result.

Crucially, these are **restrictions on \(Q\)**, not factorizations of the ambient form \(F\). Choosing an ambient lift \(H_p\) of \(h^pR_F\), any form with that restriction is \(F=H_p+q_QK\), with \(\deg K=3p-2\), but the required ambient normal-order condition is additionally \(F\in I_{C_0}^p\). The unresolved lifting problem is to determine the image and kernel of
\[
H^0(\mathbf P^3,I_{C_0}^p(3p))\longrightarrow
H^0(Q,\mathcal O_Q(3p,3p))
\]
and the associated first-symbol map to \(H^0(C_0,\operatorname{Sym}^pN_{C_0}^\vee(3p))\). In characteristic zero the latter bundle is \(\mathcal O_{\mathbf P^1}(5p)^{\oplus(p+1)}\). The quadric direction constrains only one slice of the normal symbol; it does not determine all ambient coefficients. No reducibility, power structure, nonnormality, or STCI exclusion follows without this lifting analysis. Source: [equality rigidity and ambient-lifting formulation](notes/2026-10-07-thick-boundary-carrier-rigidity.md).

## Architectural implications

- Keep the carrier chapter ordered by **logical dependency**, not date: fixed-carrier descent -> singleton classification -> admissible projections -> phase reduction -> explicit no-mate example.
- Give R-0017 an explanatory counterexample subsection with the first-order conductor mechanism.
- Keep the entirely-thick inequalities as a scoped lemma and open interface in the **normal-relations/filtered-thickenings chapter**. Do not imply the inequalities solve higher normal contact.
- Retain canonical R records as authoritative scoped statements, with notes as detailed proofs/audits. Consolidate explanatory duplication only after preserving hypotheses and failed-shortcut explanations.
- No file deletions or status promotions in this pass.

## Next mathematical review

Examine the **geometry of residual cycles versus exceptional normal-cone data** (R-0019, R-0023, R-0024, R-0025 and recent CI-cycle notebooks). The key organizational question: which observations are statements about genuine residual components downstairs, and which are only about blowup or infinitesimal contact?
