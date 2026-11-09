# Toric torsion, opposite carriers, and endpoint contact filtrations

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

The [component and contact proof on \(S_+\)](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#12e-generic-multiplicities-and-contacts-among-binomial-components)
and the prescribed [\(\mu_4\) result R-0021](../results/quartic_mu4_degeneration.md)
give the projective intersection and its characteristic-two specialization.

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
The tangent weights in the projective charts \(x_0=1\) and \(x_3=1\)
are respectively \((1,3,4)\) and \((-4,-3,-1)\) in coordinate order.
The [binomial generators of \(I_{C_0}\)](projection_and_elliptic_gluing.md#13-the-full-fiberwise-inverse-and-descent-tests)
use the same fixed embedding.

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

In characteristic zero the [full projective stabilizer proof](../supplements/QUARTIC_PROJECTION_AND_SPECIAL_GEOMETRY.md#4-full-projective-automorphism-group)
gives \(\mathbf G_m\rtimes\langle\iota\rangle\). Thus the projective
orbit of \(C_0\) has dimension \(15-1=14\). The two transverse families
are one-dimensional orbits within it. Reversal normalizes the ambient
diagonal torus and exchanges the two transverse scalings.

There are distinct intrinsic and transverse actions. The intrinsic torus
of weights \((0,1,3,4)\) preserves each member of either family. Scaling
\(x_2\) moves the parameter of \(C_a^+\), while scaling \(x_1\) moves
the parameter of \(C_a^-\). The finite transverse subgroup permutes the
root-of-unity components below simply transitively. The connected intrinsic
torus fixes each irreducible component of the finite arrangement.

On the dense torus of \(S_+\), write \((u,z)\mapsto[1:u:zu^3:u^4]\).
The projective coordinate characters relative to \(x_0\) have weights
\((0,0),(1,0),(3,1),(4,0)\). The character relation \(4(1,0)=(4,0)\)
gives the carrier equation, and the slices \(z=a\) close up to \(C_a^+\).

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

The dense torus of \(S_-\) is parametrized by
\((u,z)\mapsto[1:zu:u^3:u^4]\), on which \(G=u^q(z^q-1)\).
On \(S_+\) the reversed mate is \(x_2^q-x_0^cx_1^bx_3^a\).
The weights of its monomials differ by \((0,q)\), and its restriction is
\(u^{3q}(z^q-1)\). Thus on either carrier the dense intersection scheme is
\(\mathbf G_{m,u}\times\mu_q\), cut out by the \(q\)-th power of the
transverse character equaling one.

In characteristic zero, the intersection decomposes into \(q\) distinct rational quartics indexed by \(\mu_q\):
\[
R_\zeta=[s^4:\zeta s^3t:st^3:t^4],
\qquad \zeta\in\mu_q.
\]

The diagonal translates are smooth and distinct on the dense torus.
Their only meetings are the two distinguished endpoints.

On \(x_0=1\), normalizing the cusp \(x_2^4=x_3^3\) gives
\((x_2,x_3)=(u^3,u^4)\), and the mate becomes \(x_1^q=u^q\).
This gives the displayed components and generic reducedness in
characteristic zero. The boundary \(x_0=0\) leaves only
\(p_\infty=[0:0:0:1]\); in the affine chart the only point with
\(u=0\) is \(p_0=[1:0:0:0]\). A proper complete intersection has no
embedded associated primes, so generic reducedness gives the reduced
union, including the endpoints. This is the opposite-carrier version of
the linked component proof.

In characteristic \(p>0\), write \(q=p^r m\) with \(p\nmid m\).
The same boundary check leaves the \(m\) translates indexed by \(\mu_m\),
each with generic transverse length \(p^r\). For \(q=p^r\) the reduced
support is \(C_0\). In the \((4,4)\) case the
[ruled divisor](../supplements/ARITHMETIC_FOUR_SECTION_FAMILY.md#2-the-flat-relative-divisor-of-four-moving-sections)
has equation \(q_{\rm rul}^4-h^4\), with sections \(q_{\rm rul}=\zeta h\)
over a splitting field of characteristic zero. Its characteristic-two
equation is \((q_{\rm rul}-h)^4\). The projective intersection has generic
length four along \(C_0\) in that fiber. The endpoint algebras of the
projective image have the separate description in R-0021 and the
[embedded quotient proof](../arguments/torus_embedded_quotients.md#the-fourth-root-image-and-its-conductor).

### 3.1. A binomial degree and a descending singleton-support power

The semigroup \(\langle3,4\rangle\) records which transverse character
equations admit the displayed homogeneous binomial compactification.
The stronger question of a mate with
sole support on this fixed carrier has the
[existing normalization criterion](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic).
The normalization of \(S_-\) is
\(\nu:\mathbf P(1,1,4)\to S_-\), \([s:t:Z]\mapsto[s^4:Z:st^3:t^4]\).
In its weighted coordinates the carrier subring and the inverse-image
equation are
\[
R[Z]=k[s^4,st^3,t^4,Z],\qquad \phi=Z-s^3t.
\]
A degree-\(N\) sole-support mate pulls back to a scalar multiple of
\(\phi^N\). In characteristic \(p>0\), the exact criterion is
\[
\phi^N\in R[Z]\quad\Longleftrightarrow\quad
p^{v_p(N)}\in\langle3,4\rangle.
\]
In characteristic zero no positive power descends, since the coefficient
\(-N s^3t\) at \(Z^{N-1}\) is nonzero and does not belong to \(R\).
Thus \(N\in\langle3,4\rangle\) alone is not a characteristic-free
criterion for singleton support. Reversal transports the result to \(S_+\).
The criteria and minima concern these fixed carriers.

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

Indeed, at \(p_0\) in \(x_0=1\) take \(x=x_1\). The two graph
equations have right-hand sides \(\zeta^{-3}x^3,\zeta^{-4}x^4\).
The intersection ring is \(k[[x]]\) modulo the differences of these
right-hand sides for \(\zeta,\eta\). Equal cubes force unequal fourth
powers for distinct labels. At \(p_\infty\) in \(x_3=1\), take
\(v=x_2\). The graph is \(x_0=v^4,\ x_1=\zeta v^3\), so the ideal
of differences is \((v^3)\). The resulting lengths are for the projective
curves. For the \(C_a^+\) four-section arrangement the contact divisor
upstairs on \(\mathbf F_4\) is \(3p_0+p_\infty\), whereas the projective
lengths are both three. [Ruled and projective contact comparison](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#12e-generic-multiplicities-and-contacts-among-binomial-components).

For \(q=p^r\), exceptional pairs occur only when \(p=3\). Here \(p\)
labels a prime-power order of roots of unity in characteristic zero;
it is not the ground-field characteristic in this contact calculation.
More generally, when \(3\mid q\), the exceptional unordered pairs are
the three pairs in each coset of \(\mu_3\), giving \(q\) pairs in total.
For \(q=4\), opposite and adjacent labels both have contact three at each
endpoint. A primitive \(p^j\)-th root in \(\overline{\mathbf Q}_p\) has
\(v_p(1-\zeta)=1/(p^{j-1}(p-1))\) for \(v_p(p)=1\), by taking the
product of its conjugate differences using \(\Phi_{p^j}(1)=p\).
These valuations have further levels as \(j\) grows. The quartic
contact calculation distinguishes only the indicated character kernel.

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

For branches that are graphs over the same ambient parameter \(t\), the
quotient by the sum of their ideals is \(k[[t]]\) modulo the differences
of the graph functions. Its length is the least order of a nonzero
difference. That is also the first order \(n\) at which the embedded jets
differ, since the graph functions for an \(n\)-jet are read modulo
\(t^{n+1}\). Reparametrization preserves the embedded jet.

In particular, for the cyclic orbit of graphs
\(y_j=\zeta^{w_j}t^{n_j}\) with strictly increasing positive \(n_j\)
and jointly faithful characters on \(H=\mu_q\), one has
\[
H_n=\bigcap_{n_j\le n}\ker(h\mapsto h^{w_j}),\qquad
c(\zeta,\eta)=\min\{n_j:(\zeta/\eta)^{w_j}\ne1\}.
\]
The nested coset partitions give a rooted tree. For distinct labels the
distance \(\rho^{c(\zeta,\eta)}\) with \(0<\rho<1\) is an ultrametric,
since agreement through a given jet order is transitive.

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

### A local graph with three contact orders

Over an algebraically closed field of characteristic zero, take the graphs
in \(\mathbf A^4_{t,y,z,w}\)
\[
R_\zeta:\quad (y,z,w)=(\zeta^8t^2,\zeta^4t^3,\zeta t^5),
\qquad \zeta\in\mu_{16}.
\]
The group acts by scaling \(y,z,w\) with weights \(8,4,1\), fixing \(t\).
The graph differences for \(h=\zeta/\eta\) have orders \(2,3,5\)
in the coordinates where their coefficients are nonzero. The jet
stabilizers are \(\mu_{16}\) for \(n\le 1\), \(\mu_8\) for \(n=2\),
\(\mu_4\) for \(n=3,4\), and \(\{1\}\) for \(n\ge 5\). Thus the
intersection length is two for \(h\notin\mu_8\), three for
\(h\in\mu_8\setminus\mu_4\), and five for \(h\in\mu_4\setminus\{1\}\).
This control concerns local graphs in affine four-space. Realization in
a global intersection through the fixed quartic remains a separate question.

## 6. Arithmetic genus and normalization defects

For the complete intersection of degrees \((4,q)\),
\[
p_a=1+2q^2.
\]

In the characteristic-zero arrangement, the normalization is a disjoint
union of \(q\) copies of \(\mathbf P^1\). The cokernel of
\(\mathcal O_Z\to\nu_*\mathcal O_{\widetilde Z}\) is supported at the two
endpoints by the disjointness and smoothness away from them. Taking Euler
characteristics gives the total normalization defect
\[
\delta_{p_0}+\delta_{p_\infty}
=p_a+q-1
=2q^2+q,
\]
Here the union sequence for adding a new component uses its intersection
with the whole preceding union. For example, at \(q=8\) the sum over
pairs of the two projective contact lengths is \(6\binom{8}{2}=168\),
while the total normalization defect is \(136\). The full union is reduced
and has no embedded points by the complete intersection and generic
reducedness in Section 3. The discrepancy therefore supplies no embedded
length. In the historical proposal \(q(q-4+\epsilon)\), the definition
of \(\epsilon\) is missing. The failed pairwise sum gives no basis for
using that expression.

## 7. Relation to the existing STCI program

These explorations connect to three established research interfaces.

**Torus-limit stratification.** The
[full supported Hilbert-limit argument](../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits)
starts with \(P=I_{C_0}\) and \(P^N\subset J\subset P\).
Every intrinsic-torus translate lies in the fixed closed incidence
\(C_0\subset Y\subset V(P^N)\). Both full opposite limits retain
support \(C_0\) and the Hilbert polynomial, while possibly acquiring
embedded structure and additional minimal generators. The ideal of two
extreme forms need not be the full limit. An invariant arrangement with
residual curves supplies a control example, not a boundary of this
sole-support incidence merely by being invariant. The
[supported-boundary framework](../frameworks/torus_supported_boundaries.md#directional-loci)
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
- Which invariant endpoint configurations occur in full Hilbert limits of actual complete intersections containing \(C_0\)? Can equivariant deformation theory organize the realizable configurations into locally closed loci, and which can occur under sole support?
- For integral equivariant carriers, how do normalization and boundary affect the transverse character descent semigroup? Do the two opposite carriers sit in a larger configuration under the normalizer of the intrinsic torus? These questions concern geometry beyond the reviewed invariant-carrier exclusion.

No affirmative answer is asserted here.

## 9. Logical safeguards

The following distinctions must be maintained throughout subsequent work:

1. Invariance of reduced support is not invariance of the defining ideal.
2. A flat limit of a complete intersection is not generally the intersection of the separate limits of its equations.
3. An invariant flat limit need not remain two-generated.
4. A construction on one toric carrier does not classify arbitrary invariant carriers.
5. Positive-characteristic coalescence of a prescribed family does not prove a characteristic-zero obstruction.
6. Endpoint pairwise contacts do not independently determine multi-branch normalization defects.

## 10. Source corrections and proof scope

The November 2 restoration reconstructed missing formulas from the fixed
embedding, surviving derivations and linked proofs. No intact transcript
was available. The correction notices record the exponent correction,
the jet convention and the restricted scope of the fourth-power ruled
equation. Consult the proofs above for the projective statements and their
characteristic hypotheses.

- [Restoration and correction diff from PR #107](https://github.com/markluxton1/STCI/commit/167484025a43fd07127fd9ac1c331327584c6304)
- [Corrected toric involution handoff](https://github.com/markluxton1/STCI/blob/e4e10f8d8b525285bed3ec016f0e97adb67a0bdc/research/explorations/toric_torsion_endpoint_contacts/toric_involution_handoff.md)
- [Corrected root-of-unity contact handoff](https://github.com/markluxton1/STCI/blob/e4e10f8d8b525285bed3ec016f0e97adb67a0bdc/research/explorations/toric_torsion_endpoint_contacts/root_of_unity_contact_handoff.md)

The November 9 consolidation received a nonauthor check of the explicit
family calculations. The reviewer reconstructed the transverse character
restrictions, projective support and generic lengths, graph contact lengths
including the \(\mu_{16}\) control, and the normalization-defect comparison
at \(q=8\). They checked the fixed-carrier descent and linked proof scopes
against the restored passages. The review concerns these explicit families
and the transfer of their proofs and qualifications.
