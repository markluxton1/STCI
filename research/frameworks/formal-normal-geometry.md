# Formal normal geometry of intersections containing the rational quartic

Use the [evidence and review rules](../MODEL.md#evidence-and-review) and the
[frontier](../FRONTIER.md) to assess and select the open questions below.

## Fixed setup

Let k be algebraically closed of characteristic zero and
\[
C=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
Use the [characteristic-zero conormal splitting](../results/quartic_conormal_characteristic_jump.md)
to obtain \(N_{C/\mathbf P^3}\simeq\mathcal O_{\mathbf P^1}(7)^{\oplus2}\).

Let \(F,G\) define distinct integral surfaces containing \(C\), and set \(Z=V(F,G)\). **Do not assume** \(Z_{\mathrm{red}}=C\). The eventual STCI condition is a constraint to detect, not a standing hypothesis. In particular, a component of \(Z\) different from \(C\) may meet \(C\) at finitely many points, and the formal completion along \(C\) need not record its full global geometry.

## Simultaneous realization and compatibility problems

The organizing problem is **not** merely to classify ideals in a two-dimensional regular local ring and then seek equations. We must study several realization problems *simultaneously*, together with the maps that make them compatible.

At the generic point of C, choose a finite-colength ideal \(J_\eta\subset K[[X,Y]]\), where \(K=k(C)\), representing a candidate generic thickening \(T_\eta=\operatorname{Spec}(K[[X,Y]]/J_\eta)\). For the actual intersection, \(J_\eta=(F,G)K[[X,Y]]\) when this quotient has finite length. More generally, ask whether a candidate \(J_\eta\) can arise from a coherent ideal sheaf \(\mathcal J\subset\mathcal O_{\mathbf P^3}\) with \(\mathcal J\subset I_C\), whose generic completion is \(J_\eta\). Such a global realization can have extra components or special-point structure; no purity or STCI hypothesis is implicit.

There are **four interdependent tests**, not a sequential list of independent classifications:

1. **Abstract/generic thickening:** what finite-length \(K[[X,Y]]\)-algebras (with specified embedding in the formal normal plane) can occur, and what intrinsic invariants and deformations do they possess?
2. **Realization inside each carrier:** for integral surfaces \(X_F=V(F)\) and \(X_G=V(G)\) containing C, can the same thickening be embedded as a closed subscheme of each? In ideals, this requires \((F)\subset\mathcal J\) and \((G)\subset\mathcal J\) (and the corresponding containments after completion). Separate embeddings into unrelated abstract surfaces do not suffice.
3. **Ambient realization:** does the candidate thickening and its chosen normal embedding extend to a coherent closed subscheme of \(\mathbf P^3\) with the prescribed restrictions along C? This imposes global section, gluing, degree and normal-bundle constraints not visible over K alone.
4. **Joint compatibility and actual intersection:** can the *same ambient embedding* and the *same pair of global integral surface equations* realize all of the preceding data with \(\mathcal J=(F,G)\)? Merely having \((F,G)\subset\mathcal J\) shows the candidate thickening lies in the intersection; equality is stronger. To obtain an STCI, one must additionally prove \(V(F,G)_{\mathrm{red}}=C\), excluding extra components globally.

Thus the question is not only whether \(T\) lies in \(X_F\), in \(X_G\), and in \(\mathbf P^3\) separately, but whether these are **the same closed immersion and compatible factorisations**
\[
T\hookrightarrow X_F\hookrightarrow\mathbf P^3,
\qquad
T\hookrightarrow X_G\hookrightarrow\mathbf P^3,
\]
with the additional equality \(I_T=(F,G)\) when T is meant to be the full intersection scheme.

Seek a proved obstruction or lifting criterion connecting at least two of
these levels. Treat the two carriers symmetrically and specify what is
formal, algebraic, or projective. A useful comparison explains which
compatibilities the filtration or successive exceptional schemes detect.

## Three distinct constructions

Write \(J=I_C\subset\mathcal O_{\mathbf P^3}\) and \(I=(F,G)\subset J\). Distinguish:

1. The \(J\)-adic completion of \(\mathcal O_Z=\mathcal O_{\mathbf P^3}/I\), with its induced filtration.
2. The normal cone \(\operatorname{Spec}_C\operatorname{gr}_{J\mathcal O_Z}\mathcal O_Z\), and its projectivization (which can lose information).
3. The scheme-theoretic intersection of the **strict transforms** of the two surfaces on \(E=\mathbf P(N_{C/\mathbf P^3})\subset\operatorname{Bl}_C\mathbf P^3\).

These are related, but generally not identical. In particular, the intersection on E is described by the leading normal forms of the individual surfaces, while the initial ideal of (F,G) may contain additional initial forms arising from combinations of generators. Saturation and higher relations matter.

Determine the exact ideals, saturations, and maps comparing these
constructions. Specify which data depend only on the intersection ideal and
which depend on its chosen generators or carriers. For proved local comparisons
of full initial ideals and actual equations, see
[R-0030](../results/local_filtration_comparison_defect.md).

At the generic point \(\eta_C\), after a choice of formal parameters, study \(I\subset K[[X,Y]]\), \(K=k(C)\simeq k(t)\). Orders \(r=\operatorname{ord}_C F\), \(s=\operatorname{ord}_C G\) and the leading forms provide the first layer, not a complete invariant. When \(C\) is an isolated generic component of the intersection, the length \(\ell_{K[[X,Y]]}(K[[X,Y]]/I)\) measures its generic multiplicity. The identity \(de/4\) for this length requires that C be the only one-dimensional component of the global complete intersection; it must not be imposed in the broader setup.

## Exceptional geometry and components downstairs

Separate horizontal components over C (dominating C) from vertical components over special points of C. Study their scheme structures and behavior under successive blowups. An exceptional component does **not** by itself prove that Z has another component downstairs: it may encode higher contact, a special fiber, or excess intersection. Conversely, if another global component meets C, its formal trace can influence the exceptional scheme. Establish precise implications rather than equating these phenomena.

Generic completion over \(K\) misses distinct residual curves, including
those meeting \(C\) at special points. Seek necessary or sufficient conditions
for an additional curve downstairs from the exceptional schemes over all
points. See the [cycle and visibility analysis](../synthesis/02-two-surfaces.md#25-actual-sources-finite-jets-and-formal-visibility).

The normal cone, strict-transform intersection, and scheme-theoretic total transform should be compared through their defining graded/Rees constructions. Keep track of whether a claimed direction or component is intrinsic to the ideal or depends on the chosen pair of surfaces.

## Valuations and tropical perspective

The function field K is not itself a Laurent-series field. A chosen point of C gives a completion \(k((t))\) after a local parameter choice; in characteristic zero, Puiseux-type extensions can be used in an algebraic closure of that completion. Passing instead to \(\overline K\) is a different operation. State which field and valuation are being used.

Use weighted initial ideals, valuations and tropical geometry **conceptually** to organize successive normal directions, degenerations and cancellation. Cancellation should be interpreted through intrinsic initial ideals and relations, not reduced to a search through polynomial examples. In particular, the tropicalizations of two principal equations need not determine the tropicalization of their ideal.

The key question is whether these methods yield structural criteria for allowable formal thickenings and their global realizations, and whether specializations along C force additional components or obstructions.
The [valuation and specialization questions](../synthesis/formal-normal-intersection.md#5-focused-theorem-level-questions-all-open)
give more specific comparisons.

## Multiplicity two as a test

For generic intersection length two, describe the possible local
complete-intersection structures and their behavior under blowup, allowing
residual components in the global intersection. Check compatibility of the
two generic normal orders with length two. Separate the local conclusions
from the conditions for an ambient realization and for sole reduced support.

## Research discipline

- Keep C fixed unless a general statement is cheaper or materially clarifies the argument.
- Identify the proved inputs and state their hypotheses alongside any conjectural extension.
- Prioritize geometric proofs, invariant constructions and necessary/sufficient criteria over computational case studies.
- Do not use an unverified general assertion that two STCI defining surfaces share a singular point on C.
- Check the repository and literature before claiming novelty. For excluded
  integral quartic carriers in the fixed embedding, use
  [R-0001](../results/quartic_carrier_exclusion.md).
