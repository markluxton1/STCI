# Root-of-unity arrangements and contact filtrations

**Status:** Exploratory source document; not canonical theorem authority.
**Date:** 2026-11-02
**Source:** ChatGPT mathematical exploration.
**Consolidated account:** [Toric torsion and endpoint contacts](../../synthesis/toric_torsion_and_endpoint_contacts.md)

This is a restored and corrected edition of an exploratory source, not a
verbatim transcript or a promoted result. The [received version](https://github.com/markluxton1/STCI/blob/b647c18cffa39a0897acd1d989ee779dd0e0b650/research/explorations/toric_torsion_endpoint_contacts/root_of_unity_contact_handoff.md)
already contained stripped delimiters and missing mathematical symbols; the
saved earlier versions contain the same damage. Coordinates, maps and other
recoverable formulas below have been reconstructed from the fixed embedding,
the surrounding derivation and the linked current proof homes. No intact
original was available for comparison.

## Restoration and corrections — 2026-11-02

The fixed-curve parametrization, component map, contact and character-kernel
formulas, table, genus equation and normalization quotient have been
reconstructed. The erroneous factor of three in the exponent \(a\) has been
removed. The jet convention and \(q=3\) equality case are now explicit.
Section 11 corrects the intrinsic/transverse group distinction and retains
support under the full intrinsic-torus Hilbert limit. The rejected
embedded-length formula retains its missing-definition warning; no value of
its lost parameter has been invented.

The mathematical discussion and useful failed proposals are retained, with
corrections identified explicitly. Historical research suggestions do not
override [repository governance](../../../AGENTS.md). Consult the
[consolidated account](../../synthesis/toric_torsion_and_endpoint_contacts.md)
and its current proof links before relying on a claim. No theorem is promoted
by this restoration.

---

Root-of-Unity Arrangements, Contact Filtrations, and Torus Degenerations

Mathematical synthesis for the STCI project

Status: Exploratory research note. The explicit intersection calculations are established; the jet-filtration framework is established under stated hypotheses; its application to classifying torus limits remains open.

## 1. Motivation and context

The problem is to understand set-theoretic complete-intersection presentations of the rational quartic

\[
C=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3
\]

over fields of varying characteristic, particularly characteristic zero.

The characteristic-\(p\) constructions developed in the STCI project provide binomial complete intersections whose support collapses to \(C\). In characteristic zero, corresponding binomial arrangements generally split into multiple rational curves meeting at the hyperosculating points

\[
p_0=[1:0:0:0],\qquad
p_\infty=[0:0:0:1].
\]

This characteristic-dependent splitting motivated the study of torus actions, invariant arrangements, and flat limits.

A suggestion from Claude was that the intersection multiplicities among these residual curves might exhibit an ultrametric structure, controlled by the \(p\)-adic proximity of their root-of-unity labels.

We investigated that suggestion, beginning with the four-component arrangement and then extending to arbitrary prime powers \(q=p^r\).

The resulting picture is more precise:

The explicit binomial arrangements have contact multiplicities governed by finite-group character kernels.

The rational-quartic family has at most two contact levels at \(p_0\), and only one at \(p_\infty\).

More general equivariant branch configurations can exhibit genuine hierarchical contact filtrations.

These filtrations have an intrinsic interpretation through stabilizers of embedded jets.

Their relevance to the possible flat limits of STCI presentations remains to be established.

The principal geometric object emerging from the discussion is therefore the jet-stabilizer filtration of a finite group acting on a collection of curve germs.

## 2. The binomial arrangement

Work initially over an algebraically closed field \(k\) of characteristic zero.

Consider

\[
F=x_2^4-x_0x_3^3
\]

and

\[
G=x_1^q-x_0^a x_2^b x_3^c,
\]

where

\[
3b+4c=q,\qquad a+b+c=q
\]

and \(a,b,c\) are nonnegative integers.

These conditions ensure that \(G\) is homogeneous of degree \(q\) and vanishes on \(C\).

For the displayed form with \(x_0^a\), the degree equations give

\[
a=2b+3c,
\]

after using \(q=3b+4c\); more directly, \(a=q-b-c=2b+3c\). Thus \(a\) is automatically nonnegative whenever \(b,c\) are.

On the affine chart \(x_0=1\), the equation \(F=0\) admits the parametrization

\[
x_2=u^3,\qquad x_3=u^4.
\]

Substitution into \(G\) gives

\[
x_1^q=u^q.
\]

Consequently, in characteristic zero, the complete intersection is supported on the \(q\) curves

\[
\boxed{
R_\zeta:
[s:t]\longmapsto
[s^4:\zeta s^3t:st^3:t^4],
\qquad \zeta\in\mu_q.
}
\]

The component \(R_1\) is the original quartic \(C\).

All components are smooth rational quartics. They are distinct, and their only intersections occur at \(p_0\) and \(p_\infty\).

The cyclic group \(\mu_q\) acts by scaling \(x_1\), permuting the components simply transitively.

This group action is the source of the contact symmetry studied below.

Characteristic-\(p\) interpretation

If \(q=p^r\), then over a field of characteristic \(p\),

\[
x_1^q-u^q=(x_1-u)^q.
\]

Thus the \(q\) distinct characteristic-zero branches coalesce into a nonreduced structure supported on \(C\).

The scheme-theoretic structure of that collapse requires separate analysis. In particular, a characteristic-\(p\) thickening is not determined merely by counting the characteristic-zero components.

## 3. Local intersections at the hyperosculating points

### 3.1. The point \(p_0\)

On \(x_0=1\), the component \(R_\zeta\) is parametrized by

\[
(x_1,x_2,x_3)
=(\zeta u,u^3,u^4).
\]

Taking \(x=x_1\) as a common parameter gives

\[
R_\zeta:
\begin{cases}
x_2=\zeta^{-3}x^3,\\
x_3=\zeta^{-4}x^4.
\end{cases}
\]

For two distinct labels \(\zeta,\eta\), their scheme-theoretic intersection is determined by the differences

\[
(\zeta^{-3}-\eta^{-3})x^3
\]

and

\[
(\zeta^{-4}-\eta^{-4})x^4.
\]

The local intersection multiplicity is the length of the corresponding quotient of \(k[[x]]\).

Writing \(h=\zeta/\eta\), we obtain

\[
\boxed{
I_{p_0}(R_\zeta,R_\eta)=
\begin{cases}
4,&h\ne1,\ h^3=1,\\
3,&h^3\ne1.
\end{cases}
}
\]

There is no case in which both coefficients agree for distinct labels, because \(\gcd(3,4)=1\).

Thus exceptional contact occurs precisely when

\[
h\in\mu_3\setminus\{1\}.
\]

### 3.2. The point \(p_\infty\)

On the chart \(x_3=1\), put \(v=s/t\). Then

\[
R_\zeta:
(x_0,x_1,x_2)=(v^4,\zeta v^3,v).
\]

Here \(x_2=v\) is a common parameter.

For distinct \(\zeta,\eta\), the first difference is

\[
(\zeta-\eta)v^3.
\]

Consequently,

\[
\boxed{
I_{p_\infty}(R_\zeta,R_\eta)=3
\qquad(\zeta\ne\eta).
}
\]

The two endpoints therefore exhibit different contact structures.

At \(p_0\), a subgroup of order three can produce additional contact. At \(p_\infty\), the first distinguishing character is faithful, so all distinct branches separate at order three.

## 4. The \(q=4\) case

For \(q=4\), the equations are

\[
F=x_2^4-x_0x_3^3,\qquad
G=x_1^4-x_0^3x_3.
\]

The four components are indexed by

\[
\mu_4=\{1,i,-1,-i\}.
\]

Since \(\mu_4\cap\mu_3=\{1\}\), no exceptional pairs exist.

Hence, for every distinct pair,

\[
\boxed{I_{p_0}(R_\zeta,R_\eta)=I_{p_\infty}(R_\zeta,R_\eta)=3.}
\]

All four branches have the same tangent line at each endpoint. They agree through second order and separate at third order.

In particular, opposite roots such as \(1,-1\) do not exhibit greater contact than adjacent roots such as \(1,i\).

This disproves the proposed distinction between opposite and adjacent fourth roots for this arrangement.

The result is explained by the fact that the cubing map

\[
\mu_4\longrightarrow\mu_4,\qquad
\zeta\longmapsto\zeta^3
\]

is an automorphism.

## 5. General prime powers

The component and pairwise-contact calculation in this section is in
characteristic zero. Retain the admissible exponent conditions of Section 2
when referring to the global complete intersection.

For \(q=p^r\), the preceding calculation gives a complete classification of pairwise contact.

If \(p\ne3\), the group \(\mu_q\) contains no nonidentity cube root of unity. Therefore

\[
I_{p_0}=I_{p_\infty}=3
\]

for every distinct pair.

If \(p=3\), then

\[
\mu_3\subset\mu_{3^r},
\]

and the exceptional pairs are precisely those whose labels belong to the same coset of \(\mu_3\).

Each coset contains three elements and therefore contributes three exceptional unordered pairs. There are \(q/3\) cosets, giving exactly \(q\) exceptional pairs.

| \(q\) | Contact at \(p_0\) | Contact at \(p_\infty\) | Exceptional unordered pairs |
| --- | --- | --- | --- |
| 3 | 4 | 3 | 3 |
| 4 | 3 | 3 | 0 |
| 7 | 3 | 3 | 0 |
| 8 | 3 | 3 | 0 |
| 9 | 3 or 4 | 3 | 9 |
| 16 | 3 | 3 | 0 |
| 25 | 3 | 3 | 0 |
| 27 | 3 or 4 | 3 | 27 |

For \(q=9\), the exceptional-contact graph consists of three disjoint triangles, corresponding to the cosets of \(\mu_3\).

The calculation shows that the contact structure does not acquire additional levels as \(r\) increases.

In particular, it does not distinguish roots of orders \(3,9,27,\ldots\) beyond membership in \(\mu_3\).

Conclusion: The original \(p\)-adic hierarchy conjecture is not realized by this rational-quartic binomial family.

The correct controlling structure is the kernel of the first nontrivial character appearing in the local expansion.

## 6. General contact filtrations from characters

Consider a finite cyclic group \(H=\mu_q\) acting on a collection of smooth curve germs through a fixed point.

Suppose the branches admit a common local parameter \(t\) and graph presentations

\[
R_\zeta:\qquad
y_j=\zeta^{w_j}t^{n_j},
\qquad j=1,\ldots,m,
\]

with increasing vanishing orders

\[
n_1<n_2<\cdots<n_m.
\]

Assume the characters jointly distinguish the branches.

For \(h=\zeta/\eta\), the first coordinate in which the branches differ determines their contact order:

\[
\boxed{
c(h)=\min\{n_j\mid h^{w_j}\ne1\},\qquad h\ne1.
}
\]

Define the subgroups

\[
H_k=
\{h\in H\mid h^{w_j}=1
\text{ for }1\le j\le k\}.
\]

These form a descending filtration

\[
H=H_0\supseteq H_1\supseteq
\cdots\supseteq H_m=\{1\}.
\]

The contact order is determined by the first stage at which \(h\) leaves the filtration.

Thus the hierarchy of pairwise contacts is determined by the successive stabilizers of the local coordinate jets.

Intrinsic formulation

Let \(X\) be a smooth variety, \(p\in X\) a fixed point of a finite group \(H\), and \(B\subset X\) a smooth curve germ through \(p\).

Suppose the translates (hB) are distinct and have a common tangent direction.

For each \(n\ge0\), use the embedded jet

\[
j_p^nB=V(I_B+\mathfrak m_p^{n+1})
\]

in the ambient infinitesimal neighborhood. It is not a parametrized jet.
To distinguish this order index from the preceding character-stage index,
write \(H_n^{\mathrm{jet}}\) for the intrinsic stabilizer.

Define

\[
H_n^{\mathrm{jet}}=\operatorname{Stab}_H(j_p^nB).
\]

Then

\[
H=H_0^{\mathrm{jet}}\supseteq H_1^{\mathrm{jet}}\supseteq H_2^{\mathrm{jet}}
\supseteq\cdots
\]

is a descending filtration.

Under the common-parameter graph hypotheses, the first jet order at which (hB) differs from \(B\) determines the intersection multiplicity.

This formulation is independent of the chosen coordinates. The character calculation is a computational realization of the intrinsic jet filtration.

The distinction between parametrized jets and embedded jets matters: reparametrizations of the curve must not be mistaken for geometric separation of two branches.

## 7. Recovering the rational-quartic filtration

At \(p_0\), the two distinguishing terms are

\[
x_2=\zeta^{-3}x^3,\qquad
x_3=\zeta^{-4}x^4.
\]

Their character weights are \(-3,-4\).

The corresponding filtration is

\[
\mu_q
\supseteq
\mu_q\cap\mu_3
\supseteq
\mu_q\cap\mu_3\cap\mu_4
=\{1\}.
\]

For \(q=3^r\), this becomes

\[
\boxed{
\mu_{3^r}\supseteq\mu_3\supsetneq\{1\}.
}
\]

The jet thresholds at \(p_0\) are precisely

\[
H_0^{\mathrm{jet}}=H_1^{\mathrm{jet}}=H_2^{\mathrm{jet}}=\mu_q,
\qquad H_3^{\mathrm{jet}}=\mu_{\gcd(q,3)},
\qquad H_n^{\mathrm{jet}}=\{1\}\quad(n\ge4).
\]

For \(q=3^r\) with \(r\ge2\), both displayed character-stage inclusions are
strict and the possible contacts are three and four. For \(q=3\), the first
inclusion is equality and all distinct pairs have contact four at \(p_0\).
All these branch and finite-group statements are in characteristic zero;
the prime in \(q=p^r\) labels the roots of unity, not the ground-field
characteristic.

For \(p\ne3\), the first nontrivial stage already has trivial stabilizer.

At \(p_\infty\), the coefficient \(\zeta\) occurs at order three and defines
a faithful character. The stabilizer is \(\mu_q\) for \(n\le2\) and is trivial
for \(n\ge3\).

This explains both the exceptional \(p=3\) behavior and the asymmetry between the hyperosculating points.

## 8. Possibility of deeper contact hierarchies

Although the rational-quartic arrangement has only two possible contact levels, more general equivariant germs can have several.

For example, use affine four-space with coordinates \(t,y,z,w\), and consider graph branches indexed by \(\mu_{16}\):

\[
R_\zeta:
\begin{cases}
y=\zeta^8t^2,\\
z=\zeta^4t^3,\\
w=\zeta t^5.
\end{cases}
\]

Their stabilizer filtration is

\[
\mu_{16}\supset\mu_8\supset
\mu_4\supsetneq\{1\}.
\]

The contact order is

\[
c(h)=
\begin{cases}
2,&h\notin\mu_8,\\
3,&h\in\mu_8\setminus\mu_4,\\
5,&h\in\mu_4\setminus\{1\}.
\end{cases}
\]

This produces three genuine contact levels.

The associated nested coset partitions define a rooted tree. One can encode the contact hierarchy by an ultrametric after choosing a decreasing numerical scale for increasingly high contact orders.

The resulting ultrametric structure is group-theoretic and jet-theoretic; it does not require a \(p\)-adic field.

This example establishes that deeper filtrations are possible in local equivariant geometry. It does not establish that such configurations occur among global complete intersections containing our rational quartic.

## 9. Relation to \(p\)-adic proximity

Claude's original hypothesis involved the \(p\)-adic valuation of differences of roots of unity.

For a primitive \(p^k\)-th root \(\zeta_{p^k}\), with the valuation normalized by \(v_p(p)=1\),

\[
v_p(1-\zeta_{p^k})
=\frac{1}{p^{k-1}(p-1)}.
\]

This produces a natural non-Archimedean hierarchy on roots of \(p\)-power order.

However, the existence of that hierarchy does not imply that intersection multiplicities of characteristic-zero algebraic curves follow it.

Our calculation demonstrates the distinction.

For \(q=3^r\), the \(p\)-adic distances distinguish multiple levels of roots of unity, but the contact geometry distinguishes only membership in \(\mu_3\).

The two filtrations are related through the cyclic group structure but are not identical.

The more fundamental geometric construction is the stabilizer filtration of embedded jets.

## 10. Arithmetic genus and scheme structure

An additional question arose concerning the relationship between pairwise contacts and the arithmetic genus of the complete intersection.

For a complete intersection of degrees \(4,q\) in \(\mathbf P^3\),

\[
p_a=1+\frac{4q(4+q-4)}2=\boxed{1+2q^2}.
\]

One might attempt to compute the genus of the union of the \(q\) rational curves by summing pairwise intersection multiplicities.

That argument is not valid without additional hypotheses.

For two reduced curves, the exact sequence for their union expresses the genus correction through their scheme-theoretic intersection.

For three or more components, the intersection of a new component with the union of the preceding components need not have length equal to the sum of its pairwise intersection lengths.

In particular, the formula

\[
p_a\left(\bigcup_iR_i\right)
\stackrel{?}{=}
1-q+\sum_{i<j}I(R_i,R_j)
\]

does not hold for arbitrary configurations of space curves.

This invalidates the earlier proposed embedded-length formula

\[
q(q-4+\epsilon).
\]

The source did not retain a definition of \(\epsilon\). This discarded
expression is preserved only as an identifier of the failed argument;
it is not a usable length formula.

There is a stronger observation for the present family.

The binomial complete intersection is generically reduced along its \(q\) distinct components in characteristic zero. Since it is a complete intersection, it is Cohen–Macaulay and has no embedded associated primes. Generic reducedness therefore implies that the entire scheme is reduced.

Consequently,

\[
\boxed{Z=\bigcup_{\zeta\in\mu_q}R_\zeta}
\]

scheme-theoretically in characteristic zero, and its arithmetic genus is exactly \(1+2q^2\).

There is no embedded zero-dimensional structure accounting for the discrepancy in the naive pairwise sum.

The correct local invariant for the union is the normalization defect

\[
\delta_p=
\operatorname{length}
\left(
\widetilde{\mathcal O}_{Z,p}/
\mathcal O_{Z,p}
\right).
\]

Because the normalization consists of \(q\) copies of \(\mathbf P^1\), and the components meet only at the two endpoints,

\[
\boxed{
\delta_{p_0}+\delta_{p_\infty}
=p_a(Z)+q-1
=2q^2+q.
}
\]

Determining the individual endpoint defects requires studying the local rings of the full union, rather than merely their pairwise contacts.

This is a natural place where the jet-filtration viewpoint may help, but it does not by itself determine the normalization defect.

## 11. Relation to the torus-limit stratification program

The [current attracting-strata framework](../../synthesis/torus_attracting_strata_and_generator_incidence.md)
organizes full invariant limits together with two-generation of the moving
ideals. A classification of reduced arrangements alone is not a prerequisite
and does not replace the supported Hilbert incidence. Contact filtrations
are possible local invariants for configurations already known to exist.

Suppose a torus-invariant limiting arrangement has finitely many curve components meeting at fixed points of the torus.

The connected intrinsic torus fixes each irreducible component: its action
on the finite component set is constant. Nontrivial component permutations
require an additional group preserving the arrangement. In the explicit
models this is the finite subgroup of the transverse torus scaling \(x_1\),
not the intrinsic torus of weights \(0,1,3,4\). Under that separate group
hypothesis, the action on embedded jets produces stabilizer filtrations.

Schematically,

\[
\boxed{
\text{specified ambient group action}
\longrightarrow
\text{component orbits}
\longrightarrow
\text{jet stabilizers}
\longrightarrow
\text{contact data}.
}
\]

This offers a way to organize local incidence information without beginning with explicit equations for every component.

It is also compatible with the broader program of studying attracting strata and opposite torus limits.

However, several distinctions must be maintained.

First, invariance of the support of an STCI does not imply invariance of its defining ideal or of a particular pair of equations.

Second, the flat limit of an intersection is not generally obtained by simply intersecting the independently limiting equations. The flat closure, including the appropriate saturation, is essential.

Third, for an actual sole-support ideal \(J\) with \(P=I_C\), choose
\(P^N\subset J\subset P\). Because the intrinsic torus preserves \(P\), its
full Hilbert limits stay in the closed incidence
\(C\subset Y\subset V(P^N)\). They retain reduced support \(C\) and Hilbert
polynomial, while embedded structure and extra minimal generators may
appear. This is the
[existing full-limit proof](../../synthesis/global_equations_and_constructions.md#invariant-support-and-the-full-torus-limit).
The two independently limiting equations need not generate that full ideal.

Fourth, contact filtrations classify aspects of arrangements already known to exist. They do not establish that a proposed arrangement lies in the closure of the locus of complete intersections containing \(C\).

Finally, two-generation is tested on moving ideals in the attracting loci.
Neither fixed limit is required to be two-generated. An explicit residual
arrangement is a control, not a supported boundary candidate merely because
it is invariant. Additional endpoint comparisons may be useful without
claiming a classification or coverage theorem.

## 12. Established conclusions and open questions

Established

The characteristic-zero binomial construction produces \(q\) rational-quartic components indexed by \(\mu_q\), for the admissible exponents specified above.

Their pairwise contact multiplicities are explicitly determined at both hyperosculating points.

Exceptional contact occurs only at \(p_0\), and only when the ratio of labels is a nonidentity cube root of unity.

For \(q=p^r\), exceptional pairs therefore occur only when \(p=3\).

The local contact hierarchy is controlled by kernels of characters appearing in successive embedded jets.

General equivariant branch arrangements can exhibit deeper stabilizer filtrations.

Pairwise intersection multiplicities alone do not determine the arithmetic genus of a union of several space curves.

Plausible research directions

Jet-stabilizer filtrations may provide useful invariants of torus-invariant endpoint configurations.

Such filtrations may help organize the strata of possible limiting arrangements.

Comparing jet filtrations at \(p_0\) and \(p_\infty\) may constrain which local configurations can occur together globally.

Local normalization defects may be expressible in terms of richer equivariant jet data, beyond pairwise contact orders.

Open mathematical questions

A. Realizability. Which finite-group jet filtrations can arise from components of actual intersections of surfaces containing \(C\)?

B. Global compatibility. What restrictions relate the contact filtrations at \(p_0\) and \(p_\infty\)?

C. Flat limits. Which invariant endpoint configurations occur as flat torus limits of complete intersections containing \(C\)?

D. Hilbert-scheme geometry. Can these configurations be organized into meaningful locally closed strata using equivariant deformation theory or Hilbert-scheme tangent spaces?

E. STCI relevance. After classifying realizable limiting configurations, which can occur as limits of intersections whose set-theoretic support is exactly \(C\)?

## 13. Historical next-step proposal and its scope

The original exploration preferred the geometric questions below to further
abstract ultrametric development. They remain optional comparisons, subject
to the [current research guidance](../../../AGENTS.md), not a compulsory
classification-first agenda.

Instead, we should formulate the jet-stabilizer filtration intrinsically for components of \(T\)-invariant arrangements through \(p_0,p_\infty\), and determine which filtration types are compatible with the actual torus representation on \(\mathbf P^3\).

That requires three pieces of information:

The torus weights on the tangent spaces at the two hyperosculating points.

The possible equivariant embedded jets of invariant or finite-orbit curve germs through those points.

The restrictions imposed by requiring those germs to belong to a global intersection of surfaces containing \(C\).

This keeps the investigation geometric and intrinsic, uses the explicit binomial constructions as test cases, and connects directly to the existing torus-limit stratification program.

Central conclusion: The root-of-unity arrangements reveal a natural filtration of local contact geometry by stabilizers of embedded jets. For the rational-quartic binomial family this filtration is simple, but its general formulation provides a potentially useful invariant for classifying torus-invariant arrangements and their possible degenerations. Its significance for the STCI problem depends on establishing realizability and global compatibility, not merely on computing further local examples.
