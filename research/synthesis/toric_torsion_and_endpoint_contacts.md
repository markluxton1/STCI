# Toric torsion, opposite carriers, and endpoint contact filtrations

**Scope:** synthesis of exploratory mathematical work; review scopes are stated below.

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

The [existing component and contact proof](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#exact-two-binomial-reduced-support-and-endpoint-contacts)
and the prescribed [mu4 result R-0021](../results/quartic_mu4_degeneration.md)
are the relevant mathematical inputs. The source explorations in Section 11
are restored editions of damaged transcriptions, with explicit correction
notices; they do not supersede those proof homes.

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

For \(a\in k^\times\), the associated families of rational quartics are
\[
C_a^+=[s^4:s^3t:a\,st^3:t^4],
\]
and
\[
C_a^-=[s^4:a\,s^3t:st^3:t^4].
\]

The involution exchanges these families, with the corresponding exchange of endpoint geometry.

This provides a symmetry principle for transporting verified local calculations between the two carriers.

There are distinct intrinsic and transverse actions. The intrinsic torus
of weights \((0,1,3,4)\) preserves each member of either family. Scaling
\(x_2\) moves the parameter of \(C_a^+\), while scaling \(x_1\) moves
the parameter of \(C_a^-\). The finite transverse subgroup permutes the
root-of-unity components below. It is not a finite subgroup of the
intrinsic torus acting nontrivially on its own invariant component set:
a connected torus fixes each irreducible component of a finite invariant
arrangement.

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
with \(q>0\) and nonnegative integral exponents. These conditions imply
\(a+b+c=q\), so \(G\) is homogeneous of degree \(q\).

In characteristic zero, the intersection decomposes into \(q\) distinct rational quartics indexed by \(\mu_q\):
\[
R_\zeta=[s^4:\zeta s^3t:st^3:t^4],
\qquad \zeta\in\mu_q.
\]

These components meet at the distinguished endpoints.

On \(x_0=1\), normalizing the cusp \(x_2^4=x_3^3\) gives
\((x_2,x_3)=(u^3,u^4)\), and the mate becomes \(x_1^q=u^q\).
This gives the displayed components and generic reducedness in
characteristic zero. The boundary \(x_0=0\) leaves only
\(p_\infty=[0:0:0:1]\); in the affine chart the only point with
\(u=0\) is \(p_0=[1:0:0:0]\). A proper complete intersection has no
embedded associated primes, so generic reducedness gives the reduced
union, including the endpoints. This is the opposite-carrier version of
the linked component proof.

In characteristic \(p>0\), when \(q=p^r\), the group scheme \(\mu_q\) is nonreduced and has a single geometric point. Correspondingly, the characteristic-zero arrangement coalesces set-theoretically to the fixed quartic.

This is a concrete geometric manifestation of the distinction between reduced support and nonreduced scheme structure in positive characteristic.

The construction does not imply that an arbitrary characteristic-zero supported intersection is obtained by lifting one of these arrangements.

### 3.1. A binomial degree and a descending singleton-support power

The semigroup \(\langle3,4\rangle\) first records the admissible
degrees of the displayed binomial. The stronger question of a mate with
sole support on this fixed carrier has the
[existing normalization criterion](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic).
In the normalization coordinates of \(S_-\), put
\[
R=k[s^4,st^3,t^4],\qquad \phi=z-s^3t.
\]
A degree-\(N\) sole-support mate pulls back to a scalar multiple of
\(\phi^N\). In characteristic \(p>0\), the exact criterion is
\[
\phi^N\in R[z]\quad\Longleftrightarrow\quad
p^{v_p(N)}\in\langle3,4\rangle.
\]
In characteristic zero no positive power descends: the coefficient
\(-N s^3t\) at \(z^{N-1}\) is nonzero and does not belong to \(R\).
Thus \(N\in\langle3,4\rangle\) alone is not a characteristic-free
criterion for singleton support. These statements concern the specified
carrier, not a minimum or obstruction over all carriers.

## 4. Pairwise endpoint contact

Work in characteristic zero throughout this section. For distinct
\(\zeta,\eta\in\mu_q\), the local intersection length is
\(\operatorname{length}\mathcal O_{\mathbf P^3,p}/(I_{R_\zeta}+I_{R_\eta})\).
The explored family has the following values:

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

For \(q=p^r\), exceptional pairs occur only when \(p=3\). Here \(p\)
labels a prime-power order of roots of unity in characteristic zero;
it is not the ground-field characteristic in this contact calculation.

In particular, increasing \(r\) does not produce an indefinitely deep \(p\)-adic hierarchy of contact orders in this family.

## 5. Intrinsic interpretation by jet stabilizers

Work in characteristic zero. Let a finite group \(H\) act on a smooth
ambient germ \((X,p)\), fixing \(p\), and let \(B\subset X\) be a
smooth curve germ whose translates are being compared. Use embedded jets
with the convention
\[
j_p^nB=V(I_B+\mathfrak m_p^{n+1}),\qquad n\ge0.
\]

Define
\[
H_n=\operatorname{Stab}_H(j_p^nB).
\]

Under the common-parameter graph hypotheses of the source calculation,
the first jet order distinguishing two translates is their local
intersection length. Reparametrizing one curve does not change its
embedded jet.

This gives an intrinsic interpretation of the root-of-unity calculations.

For the transverse group \(H=\mu_q\) and the family above, write
\(H_n^0\) and \(H_n^\infty\) for the stabilizers at the two endpoints.
The graph equations at \(p_0\) are
\[
x_2=\zeta^{-3}x_1^3,\qquad x_3=\zeta^{-4}x_1^4.
\]
Consequently
\[
H_0^0=H_1^0=H_2^0=\mu_q,\qquad
H_3^0=\mu_{\gcd(q,3)},\qquad H_n^0=\{1\}\ (n\ge4).
\]
At the opposite endpoint, the common parameter is \(x_2\), and the
first distinguishing term is \(x_1=\zeta x_2^3\). Thus
\[
H_0^\infty=H_1^\infty=H_2^\infty=\mu_q,\qquad
H_n^\infty=\{1\}\ (n\ge3).
\]

For \(q=3^r\), the character-stage chain is
\(\mu_{3^r}\supseteq\mu_3\supsetneq\{1\}\). Both inclusions are
strict when \(r\ge2\); for \(q=3\) the first is equality, and every
distinct pair has contact four at \(p_0\). In characteristic \(p\),
the geometric branches for \(q=p^r\) have coalesced. A stabilizer
analysis for that nonreduced group scheme is a separate question.

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

**Torus-limit stratification.** The
[full supported Hilbert-limit argument](global_equations_and_constructions.md#invariant-support-and-the-full-torus-limit)
starts with \(P=I_{C_0}\) and \(P^N\subset J\subset P\).
Every intrinsic-torus translate lies in the fixed closed incidence
\(C_0\subset Y\subset V(P^N)\). Both full opposite limits retain
support \(C_0\) and the Hilbert polynomial, while possibly acquiring
embedded structure and additional minimal generators. The ideal of two
extreme forms need not be the full limit. An invariant arrangement with
residual curves supplies a control example, not a boundary of this
sole-support incidence merely by being invariant. The
[attracting-strata framework](torus_attracting_strata_and_generator_incidence.md)
tests two-generation on moving ideals; their fixed limits need not be
two-generated.

**Endpoint descent.** The
[embedded quotient and endpoint account](../arguments/torus_embedded_quotients.md)
retains multiplication, homogeneous source spaces and endpoint lattices.
Finite transverse characters and jet filtrations provide comparisons in
the explicit models; abstract quotient type or contact lengths do not
determine arbitrary global homogeneous equations.

**Characteristic comparison.** The
[positive-characteristic constructions](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md)
explain coalescence for the prescribed binomial arrangements. Obstructions
to lifting prescribed embedded structures do not exclude unrelated
characteristic-zero STCI presentations.

The proposed invariant-carrier obstruction in the toric source is already
covered by the
[weight-homogeneous-carrier theorem](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md#the-bound-and-its-exact-large-prime-minimum):
in characteristic zero, one weight-homogeneous equation cannot have an
arbitrary sole-support mate. An invariant integral hypersurface has a
weight-homogeneous defining equation. That theorem is independently
reviewed work. The surviving
general question concerns unrestricted moving ideals and their actual
homogeneous equations, rather than a new proof of this invariant-carrier
exclusion.

## 8. Unresolved mathematical implications

The following remain questions rather than conclusions:

- Which pairs of endpoint jet-stabilizer filtrations are realizable by actual invariant curve arrangements in \(\mathbf P^3\)?
- Can the endpoint contact and normalization-defect calculations be expressed uniformly through finite modifications or conductor modules?
- Which transverse-character comparisons remain useful for invariant nontoric carriers in intersections with residual support or in positive characteristic?
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

This document is a synthesis of exploratory mathematical work.
The November 2, 2026 correction reconciles the source explorations with
their linked current proofs, restores the exponent and notation errors,
and specifies the embedded-jet convention and characteristic-zero scope.

Its explicit formulas and calculations should be independently checked against the source explorations and existing records before relying on them.

It introduces no new theorem, changes no STCI status, and establishes no new compulsory research direction.

## 11. Source explorations

- [Toric carriers, transverse torsion, and involution](../explorations/toric_torsion_endpoint_contacts/toric_involution_handoff.md)
- [Root-of-unity arrangements and contact filtrations](../explorations/toric_torsion_endpoint_contacts/root_of_unity_contact_handoff.md)

These are restored exploratory source documents, not verbatim transcripts
or result records. Their correction notices identify reconstructed
notation and superseded research suggestions.
The synthesis organizes their mathematical content and identifies
connections with existing work. New claims require independent review
before relying on the claim.
