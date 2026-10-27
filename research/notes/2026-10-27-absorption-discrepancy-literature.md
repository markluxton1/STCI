# Complete-intersection discrepancy: exact scope for residual absorption

Date: 2026-10-27. Literature reviewer: discrepancy-scope subagent. Status:
**primary-source scope check plus a proposed synthesis**, not canonical
promotion or a novelty claim. Retrieval followed [INDEX](../INDEX.md),
[MAP](../MAP.md) and the contribution protocol; no existing entry for these
authors was located in the literature ledger. No accepted computation was
rerun.

## 1. Paper I applies to nonreduced primary components

Primary text inspected: Benguş-Lasnier and Rangachev, with an appendix by
Chardin, [The complete intersection discrepancy of a curve I: Numerical
Invariants, arXiv:2504.09362v3, September 1, 2026](https://arxiv.org/html/2504.09362v3).

The introduction assumes a CM curve \(X\) contained in a CI \(Z\), with
equality at each generic point of \(X\). It does **not** assume reducedness
throughout. Proposition 2.1 gives the adjunction/linkage identity from a
CM component and its residual in a Gorenstein scheme. Theorem B(1), proved
in §5.2, states the genus formula for CM projective curves that are
generically complete intersections; §5 explicitly requires no
characteristic restriction.

Thus for the full \(C\)-primary component \(T\) of an actual proper
\((a,b)\) pair \(Y\subset\mathbf P^3\), and its linked residual \(D\),
the standard formula is

\[
I(T,D)=(a+b-4)\deg T-2p_a(T)+2.                 \tag{1}
\]

Here \(I(T,D)\) is the length of the scheme-theoretic intersection of the
**full** schemes. It is not the length of \(C_{\rm red}\cap D\).
The Jacobian/Milnor/normalization results, such as Theorem A and
Theorem 3.9, impose reducedness and additional tame hypotheses where
stated; those formulas must not be transferred to a generically nonreduced
primary component after discarding its nilpotents.

## 2. Paper II has a general flatness theorem inside a reduced-family paper

Primary text inspected: Benguş-Lasnier, Gaffney and Rangachev,
[The complete intersection discrepancy of a curve II: Families of curves,
arXiv:2310.16558v4, February 22, 2026](https://arxiv.org/html/2310.16558v4).

The principal equisingularity setup in §1 concerns reduced complex
analytic curves. Theorem 1.2 relates a change in Jacobian multiplicity minus
discrepancy to a relative polar degree. Those reduced-family invariants do
not directly describe a thickness-changing fiber.

However **Theorem 3.1 in §3 is more general than that setup**. Its
stated hypotheses are: no embedded point at the curve origin; a flat
embedded deformation \(X\to B\) over smooth complex \(B\); a flat
curve family \(Z\to B\) with Gorenstein total space containing \(X\); and \(X_b\) a union
of components of \(Z_b\) in every fiber. The proof uses the full primary
decomposition, so this component condition retains induced generic scheme
structures. It concludes that the residual specializes fiberwise and
the finite intersection family is flat, hence has locally constant total
length. Corollary 3.2 adds a smoothing hypothesis for a Jacobian
computation.

This is a precise comparison theorem for *compatible flat component
families*. It does not make extraction of a full primary component commute
with an arbitrary CI specialization. If that component's multiplicity
increases, its degree increases; it cannot be a flat projective family of
fixed Hilbert polynomial. A fixed lower witness may also cease to be a
full component in the special fiber, violating the component hypothesis.

## 3. A useful bridge to the proposed attachment module

This paragraph is a proposed integration deduction, not attributed to
either paper. Use the notation of the [attachment-module proposal](2026-10-27-absorption-attachment-module.md):
\(J=I_T\subset I=I_C\), \(K=I_D\). There is a direct exact sequence

\[
0\longrightarrow (I+K)/(J+K)
\longrightarrow\mathcal O/(J+K)
\longrightarrow\mathcal O/(I+K)\longrightarrow0.
\]

Consequently

\[
I(T,D)=\operatorname{length}(C\cap D)+\epsilon_{\rm nil},
\quad
\epsilon_{\rm nil}:=\operatorname{length}
I_C\mathcal O_{T\cap D}\ge0.                         \tag{2}
\]

The first term measures attachment on the marked reduction; the second
retains the additional nilpotent gluing in the full intersection.
Conditional on the independently audited attachment-module identity,
(1)–(2) combine to

\[
\boxed{
\deg\operatorname{div}(\operatorname{tors}\mathcal E_T)
+\deg\operatorname{div}(\det\bar\rho)
+\epsilon_{\rm nil}
=(a+b-4)\deg T-2p_a(T)+2.\ }                         \tag{3}
\]

This is an arbitrary-degree consistency relation for each actual fiber,
including noncurvilinear \(T\). It is not an absorption construction or
a theorem that any of these three terms is positive. Its family use
requires separately checking flatness/base change; Theorem 3.1 cannot be
invoked after those hypotheses fail.

## 4. Impact on the current investigation

The standard genus/discrepancy formula and compatible-residual
specialization are already in the literature and should be cited as such.
The unresolved task is to understand actual equation deformations across
the boundary where the selected primary component outgrows a flat lower
witness. The proposed equation-module comparison keeps marked attachment,
non-lci torsion and nilpotent gluing separate at that boundary. No
Milnor-number or reduced-support computation substitutes for those data.
