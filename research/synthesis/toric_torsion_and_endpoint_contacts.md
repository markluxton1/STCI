# Toric torsion, opposite carriers, and endpoint contact filtrations

**Status:** Provisional mathematical synthesis; not a promoted result.

**Scope:** The fixed rational quartic
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3
\]
over an algebraically closed field, with characteristic hypotheses stated separately.

## 1. Purpose

This note reconciles two related explorations:

1. Toric carriers, finite transverse characters, and characteristic-\(p\) coalescence.
2. Root-of-unity arrangements, local contact multiplicities, jet-stabilizer filtrations, and the involution exchanging opposite carriers.

These constructions provide explicit geometric models relevant to the existing torus-limit and endpoint-descent framework. They do not establish a classification of arbitrary \(T\)-invariant intersections, nor an unrestricted STCI obstruction in characteristic zero.

## 2. The torus action and opposite carriers

The fixed curve is preserved by the one-dimensional torus acting with coordinate weights
\[
(0,1,3,4).
\]

The projective involution
\[
\iota([x_0:x_1:x_2:x_3])
=[x_3:x_2:x_1:x_0]
\]
preserves \(C_0\), exchanges its distinguished endpoints \(p_0,p_\infty\), and conjugates the torus action by inversion.

Consider the two quartic surfaces
\[
S_+=V(x_1^4-x_0^3x_3),\qquad
S_-=V(x_2^4-x_0x_3^3).
\]

They are exchanged by \(\iota\).

The associated families of rational quartics are
\[
C_a^+=[s^4:s^3t:a\,st^3:t^4],
\]
and
\[
C_a^-=[s^4:a\,s^3t:st^3:t^4].
\]

The involution exchanges these families, with the corresponding exchange of endpoint geometry.

This provides a symmetry principle for transporting verified local calculations between the two carriers.

## 3. Root-of-unity arrangements

On \(S_-\), consider
\[
F=x_2^4-x_0x_3^3,
\]
and
\[
G=x_1^q-x_0^a x_2^b x_3^c,
\]
where
\[
3b+4c=q,\qquad a=2b+3c,
\]
with nonnegative integral exponents.

In characteristic zero, the intersection decomposes into \(q\) distinct rational quartics indexed by \(\mu_q\):
\[
R_\zeta=[s^4:\zeta s^3t:st^3:t^4],
\qquad \zeta\in\mu_q.
\]

These components meet at the distinguished endpoints.

In characteristic \(p>0\), when \(q=p^r\), the group scheme \(\mu_q\) is nonreduced and has a single geometric point. Correspondingly, the characteristic-zero arrangement coalesces set-theoretically to the fixed quartic.

This is a concrete geometric manifestation of the distinction between reduced support and nonreduced scheme structure in positive characteristic.

The construction does not imply that an arbitrary characteristic-zero supported intersection is obtained by lifting one of these arrangements.

## 4. Pairwise endpoint contact

For distinct \(\zeta,\eta\in\mu_q\), the explored family has the following local intersection multiplicities:

At \(p_0\),
\[
I_{p_0}(R_\zeta,R_\eta)=
\begin{cases}
4,&\zeta/\eta\in\mu_3\setminus\{1\},\\
3,&\text{otherwise}.
\end{cases}
\]

At \(p_\infty\),
\[
I_{p_\infty}(R_\zeta,R_\eta)=3.
\]

Under the involution, the exceptional contact behavior moves to the opposite endpoint for the corresponding \(C_a^+\) arrangement.

For \(q=p^r\), exceptional pairs occur only when \(p=3\).

In particular, increasing \(r\) does not produce an indefinitely deep \(p\)-adic hierarchy of contact orders in this family.

## 5. Intrinsic interpretation by jet stabilizers

Let a finite group \(H\) act on an embedded curve germ \(B\) at a point \(p\).

Define
\[
H_n=\operatorname{Stab}_H(j_p^nB).
\]

Under suitable common-parameter and graph hypotheses, the first jet order distinguishing two translates determines their local contact order.

This gives an intrinsic interpretation of the root-of-unity calculations.

For the family above, the exceptional contact filtration at \(p_0\) is governed by
\[
\mu_{3^r}\supset\mu_3\supset\{1\}
\]
when \(p=3\), with the corresponding indexing understood at the relevant jet thresholds.

At the opposite endpoint, the filtration separates all distinct branches at contact order three.

The construction suggests studying pairs of endpoint filtrations modulo the involution, but no classification of realizable pairs has been established.

## 6. Arithmetic genus and normalization defects

For the complete intersection of degrees \((4,q)\),
\[
p_a=1+2q^2.
\]

When the characteristic-zero intersection is reduced and consists of the \(q\) rational quartic components described above, its normalization is a disjoint union of \(q\) copies of \(\mathbf P^1\).

Consequently, the total normalization defect is
\[
\delta_{p_0}+\delta_{p_\infty}
=p_a+q-1
=2q^2+q,
\]
provided these endpoints account for the entire nonnormal locus.

The individual endpoint defects are not obtained merely by summing pairwise intersection multiplicities. Multi-branch space-curve singularities require examination of their full local rings.

Thus the pairwise contact calculation and the total normalization-defect calculation are distinct pieces of information.

## 7. Relation to the existing STCI program

These explorations connect to three established research interfaces.

**Torus-limit stratification.** Root-of-unity arrangements provide explicit examples of invariant carriers and structured residual components. They do not establish that every supported intersection admits a limit of this form.

**Endpoint descent.** Finite transverse characters, local semigroup constraints, and endpoint jet filtrations may provide a geometric language for source-image and descent obstructions. Results proved for specific toric carriers must not be extended to arbitrary \(T\)-invariant surfaces without additional arguments.

**Characteristic comparison.** Nonreduced group schemes explain the coalescence of these particular positive-characteristic arrangements. Obstructions to lifting prescribed embedded structures do not exclude unrelated characteristic-zero STCI presentations.

## 8. Unresolved mathematical implications

The following remain questions rather than conclusions:

- Which pairs of endpoint jet-stabilizer filtrations are realizable by actual invariant curve arrangements in \(\mathbf P^3\)?
- Can the endpoint contact and normalization-defect calculations be expressed uniformly through finite modifications or conductor modules?
- Which restrictions arising from transverse character lattices survive when the carrier is invariant but not toric?
- Can these explicit arrangements contribute to a stratification of the full supported Hilbert locus, rather than only particular binomial families?

No affirmative answer is asserted here.

## 9. Logical safeguards

The following distinctions must be maintained throughout subsequent work:

1. Invariance of reduced support is not invariance of the defining ideal.
2. A flat limit of a complete intersection is not generally the intersection of the separate limits of its equations.
3. An invariant flat limit need not remain two-generated.
4. A construction on one toric carrier does not classify arbitrary invariant carriers.
5. Positive-characteristic coalescence of a prescribed family does not prove a characteristic-zero obstruction.
6. Endpoint pairwise contacts do not independently determine multi-branch normalization defects.

## 10. Status and integration

This document is a provisional synthesis of exploratory mathematical work.

Its explicit formulas and calculations should be independently checked against the source explorations and existing canonical records before any new result is promoted.

It introduces no new canonical theorem, changes no STCI status, and establishes no new compulsory research direction.

## 11. Source explorations

- [Toric carriers, transverse torsion, and involution](../explorations/toric_torsion_endpoint_contacts/toric_involution_handoff.md)
- [Root-of-unity arrangements and contact filtrations](../explorations/toric_torsion_endpoint_contacts/root_of_unity_contact_handoff.md)

These are exploratory source documents, not canonical result records.
The synthesis organizes their mathematical content and identifies
connections with existing work. New claims require independent review
before promotion.
