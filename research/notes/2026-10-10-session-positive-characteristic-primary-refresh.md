# Positive-characteristic primary-source refresh, 2026-10-10

Status: bounded literature verification. This supplements the [2026-10-06 audit](2026-10-06-positive-characteristic-literature-audit.md). It adds a precise later toric extension, independently rechecks Moh's official abstract, and records the continuing full-text access limit for Hartshorne. It asserts no universal projective STCI theorem and no new theorem proved in this repository.

## Moh: the official abstract and the exact projection hypotheses

T. T. Moh, *Set-theoretic complete intersections*, Proc. Amer. Math. Soc. **94** (1985), 217–220, DOI [10.1090/S0002-9939-1985-0784166-1](https://doi.org/10.1090/S0002-9939-1985-0784166-1).

The [official AMS abstract](https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/) explicitly states:

1. Every projective monomial curve in `P^n_k` is an STCI when `char(k)=p>0`. The abstract does not require `k` to be algebraically closed for this monomial assertion.
2. Over an algebraically closed field of characteristic `p>0`, a projective curve `C` is an STCI if it admits a linear projection to `P^2` whose center misses `C`, whose image is birational to `C`, and whose plane image has only cusps as singularities.

Access provenance: direct browser opens of the AMS article and its PDF variants failed; the final direct article retry returned HTTP 403. A browser **search** for `"Set-theoretic complete intersections" "Moh" "cusps"` returned the AMS page itself with its complete official abstract and bibliography. The verification therefore uses indexed text from the publisher's own abstract, not an aggregator's paraphrase and not the full proof. No theorem numbering, proof details, or specialized meaning of "cusp" beyond that official abstract has been independently verified here.

The first statement applies to the literal monomial quartic `C0=[s^4:s^3t:st^3:t^4]` in every positive characteristic, by membership in that stated family. This is a direct family application, not a transfer from an affine theorem. The second statement does **not** assert that every projective curve admits such a projection. In particular, a generic nodal plane projection does not satisfy its displayed singularity hypothesis.

## Later constructive toric extension: retain full parametrization

Margherita Barile, Marcel Morales, and Apostolos Thoma, *On Simplicial Toric Varieties Which Are Set-Theoretic Complete Intersections*, J. Algebra **226** (2000), 880–892, DOI [10.1006/jabr.1999.8195](https://doi.org/10.1006/jabr.1999.8195).

The [primary publisher abstract](https://www.sciencedirect.com/science/article/pii/S0021869399981954) states that every simplicial affine **or projective** toric variety **with full parametrization** is an STCI in positive characteristic. It also describes the proofs as constructive and the resulting equations as binomial. Its other abstract statements give almost-STCI results in arbitrary characteristic; those are weaker than STCI and must remain separate.

Access provenance: a browser search for `"Set-theoretic complete intersections" "Moh" filetype:pdf` returned the ScienceDirect primary page with this abstract. A subsequent direct page open failed. This refresh verifies the abstract-level assertion, not the paper's detailed definition of full parametrization or numbered theorem statements. Neither "simplicial" nor "with full parametrization" may be dropped. This statement supplies a toric extension of the monomial result; it provides no result for arbitrary integral projective curves.

## Hartshorne: bibliographic record, continued proof-access boundary

Robin Hartshorne, *Complete intersections in characteristic p>0*, Amer. J. Math. **101** (1979), 380–383, DOI [10.2307/2373984](https://doi.org/10.2307/2373984), [JSTOR primary record](https://www.jstor.org/stable/2373984).

The record and Moh's primary bibliography confirm this reference. Direct opens of the JSTOR PDF and DOI destination did not return its full text. Consequently this refresh does not claim to have inspected Hartshorne's original equations, theorem number, or proof for the Macaulay/Cremona quartic. The later author-hosted research paper Singh–Walther, *Local cohomology and pure morphisms*, [PDF](https://www.math.utah.edu/~singh/publications/singh_walther_pure.pdf), Example 3.5, printed pp. 294–295, explicitly attributes the characteristic-`p` STCI result for the kernel of `k[w,x,y,z] -> k[s^4,s^3t,st^3,t^4]` to Hartshorne. The author PDF opened successfully and its text at this example was directly inspected. That is corroborating historical attribution, not a substitute for reading Hartshorne's proof. The quartic's positive-characteristic **projective** STCI status is independently covered by Moh's verified monomial-family assertion above.

## Bounded contemporary search and continuation scope

Searches included combinations of `projective curves`, `set-theoretic complete intersections`, `positive characteristic`, `algebraic closure of a finite field`, and `2025`/`2026`. No checked primary statement from this bounded search establishes STCI for every integral curve in `P^3` over `Fpbar`, or over an arbitrary algebraically closed field of positive characteristic. This is a search result, not a proof that no such theorem exists.

The recent [Mandal–Zinna publisher abstract](https://www.sciencedirect.com/science/article/abs/pii/S0021869325006295), J. Algebra **690** (15 March 2026), 101–113, DOI 10.1016/j.jalgebra.2025.10.042, concerns affine threefolds over characteristic-zero `C1` fields, with trivial conormal and a torsion Grothendieck-class hypothesis. It supplies no positive-characteristic projective transfer. Its abstract must not be merged with the different 2025 preprint audited in the earlier note.

The earlier affine/projective, lci-at-the-cone-vertex, and SCIP distinctions remain in force. No canonical repository file was changed by this refresh.
