# Formal normal geometry of intersections containing the rational quartic

**Status:** provisional research framework; not a canonical result or proof.
**Scope:** fixed rational quartic in characteristic zero. Read [authority policy](../AUTHORITY.md) and [current frontier](../FRONTIER.md) before using claims.

## Fixed setup

Let k be algebraically closed of characteristic zero and
\[
C=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
We use the established splitting \(N_{C/\mathbf P^3}\simeq\mathcal O_{\mathbf P^1}(7)^{\oplus2}\) without re-proving it.

Let \(F,G\) define distinct integral surfaces containing \(C\), and set \(Z=V(F,G)\). **Do not assume** \(Z_{\mathrm{red}}=C\). The eventual STCI condition is a constraint to detect, not a standing hypothesis. In particular, a component of \(Z\) different from \(C\) may meet \(C\) at finitely many points, and the formal completion along \(C\) need not record its full global geometry.

## Three distinct constructions

Write \(J=I_C\subset\mathcal O_{\mathbf P^3}\) and \(I=(F,G)\subset J\). Distinguish:

1. The \(J\)-adic completion of \(\mathcal O_Z=\mathcal O_{\mathbf P^3}/I\), with its induced filtration.
2. The normal cone \(\operatorname{Spec}_C\operatorname{gr}_{J\mathcal O_Z}\mathcal O_Z\), and its projectivization (which can lose information).
3. The scheme-theoretic intersection of the **strict transforms** of the two surfaces on \(E=\mathbf P(N_{C/\mathbf P^3})\subset\operatorname{Bl}_C\mathbf P^3\).

These are related, but generally not identical. In particular, the intersection on E is described by the leading normal forms of the individual surfaces, while the initial ideal of (F,G) may contain additional initial forms arising from combinations of generators. Saturation and higher relations matter.

At the generic point \(\eta_C\), after a choice of formal parameters, study \(I\subset K[[X,Y]]\), \(K=k(C)\simeq k(t)\). Orders \(r=\operatorname{ord}_C F\), \(s=\operatorname{ord}_C G\) and the leading forms provide the first layer, not a complete invariant. When \(C\) is an isolated generic component of the intersection, the length \(\ell_{K[[X,Y]]}(K[[X,Y]]/I)\) measures its generic multiplicity. The identity \(de/4\) for this length requires that C be the only one-dimensional component of the global complete intersection; it must not be imposed in the broader setup.

## Exceptional geometry and components downstairs

Separate horizontal components over C (dominating C) from vertical components over special points of C. Study their scheme structures and behavior under successive blowups. An exceptional component does **not** by itself prove that Z has another component downstairs: it may encode higher contact, a special fiber, or excess intersection. Conversely, if another global component meets C, its formal trace can influence the exceptional scheme. Establish precise implications rather than equating these phenomena.

The normal cone, strict-transform intersection, and scheme-theoretic total transform should be compared through their defining graded/Rees constructions. Keep track of whether a claimed direction or component is intrinsic to the ideal or depends on the chosen pair of surfaces.

## Valuations and tropical perspective

The function field K is not itself a Laurent-series field. A chosen point of C gives a completion \(k((t))\) after a local parameter choice; in characteristic zero, Puiseux-type extensions can be used in an algebraic closure of that completion. Passing instead to \(\overline K\) is a different operation. State which field and valuation are being used.

Use weighted initial ideals, valuations and tropical geometry **conceptually** to organize successive normal directions, degenerations and cancellation. Cancellation should be interpreted through intrinsic initial ideals and relations, not reduced to a search through polynomial examples. In particular, the tropicalizations of two principal equations need not determine the tropicalization of their ideal.

The key question is whether these methods yield structural criteria for allowable formal thickenings and their global realizations, and whether specializations along C force additional components or obstructions.

## Research discipline

- Keep C fixed unless a general statement is cheaper or materially clarifies the argument.
- Distinguish established repository theorems from this provisional formulation and from new conjectures.
- Prioritize geometric proofs, invariant constructions and necessary/sufficient criteria over computational case studies.
- Use the multiplicity-two situation as a test case, without assuming arbitrary local orders are compatible with multiplicity two.
- Do not use an unverified general assertion that two STCI defining surfaces share a singular point on C.
- Do not reopen excluded integral quartic carriers as live STCI candidates; see the accepted canonical results and their precise hypotheses.
