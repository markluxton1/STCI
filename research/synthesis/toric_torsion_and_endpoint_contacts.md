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

The family is defined over \(\mathbf Z\). Successive division by the
monic equations in \(x_2\) and \(x_1\) gives a free
\(\mathbf Z[x_0,x_3]\)-basis \(x_2^j x_1^i\), with
\(0\le j<4\) and \(0\le i<q\). This proves flatness over
\(\mathbf Z\), also after homogeneous localization and taking its
degree-zero summand to form the projective scheme. The monic equations form
a regular sequence over every field. Each fiber is a pure
Cohen–Macaulay complete intersection of degree \(4q\).

The dense torus of \(S_-\) is parametrized by
\((u,z)\mapsto[1:zu:u^3:u^4]\), on which \(G=u^q(z^q-1)\).
On \(S_+\) the reversed mate is \(x_2^q-x_0^cx_1^bx_3^a\).
The weights of its monomials differ by \((0,q)\), and its restriction is
\(u^{3q}(z^q-1)\). Thus on either carrier the dense intersection scheme is
\(\mathbf G_{m,u}\times\mu_q\), cut out by the \(q\)-th power of the
transverse character equaling one.

When the characteristic does not divide \(q\), the intersection decomposes into \(q\) distinct rational quartics indexed by \(\mu_q\):
\[
R_\zeta=[s^4:\zeta s^3t:st^3:t^4],
\qquad \zeta\in\mu_q.
\]

The diagonal translates are smooth and distinct on the dense torus.
Their only meetings are the two distinguished endpoints.

On \(x_0=1\), normalizing the cusp \(x_2^4=x_3^3\) gives
\((x_2,x_3)=(u^3,u^4)\), and the mate becomes \(x_1^q=u^q\).
This gives the displayed components and generic reducedness when
\(q\) is invertible. The boundary \(x_0=0\) leaves only
\(p_\infty=[0:0:0:1]\); in the affine chart the only point with
\(u=0\) is \(p_0=[1:0:0:0]\). A proper complete intersection has no
embedded associated primes, so generic reducedness gives the reduced
union, including the endpoints. This is the opposite-carrier version of
the linked component proof.

In characteristic \(p>0\), write \(q=p^r m\) with \(p\nmid m\).
The same boundary check leaves the \(m\) translates indexed by \(\mu_m\),
each with generic transverse length \(p^r\). The cycle is
\(p^r\sum_{\zeta^m=1}[R_\zeta]\), and the residual cycle after
subtracting \(p^r[C_0]\) has degree \(4(q-p^r)\). For \(q=p^r\)
the reduced support is \(C_0\). In the \((4,4)\) case the
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

### 4.1. Attachment of the whole residual union

Assume \(q\) is invertible in the ground field, and let
\(R=\bigcup_{\zeta\ne1}R_\zeta\) with its reduced scheme structure on \(S_-\).
The regular sequence \((-F,G)\) defines the reduced union of the \(q\)
components by Section 3. Consequently \(((-F,G):I_{C_0})\) defines \(R\).
Its restriction to \(C_0\) defines the effective Cartier divisor
\[
C_0\cap R=(q+5)p_0+(3q-3)p_\infty.
\]

For the local linkage calculation, let \(A\) be the regular ambient local
ring, \(I=(Y,Z)\) the ideal of the curve, and \(J=(f,g)\subset I\) the
complete-intersection ideal. Write \((f,g)^t=M(Y,Z)^t\). Adjugation
gives \(\det M\in J:I\). The Koszul comparison on the two regular
sequences has top map \(\det M\). Under the complete-intersection
change of rings
\[
\operatorname{Ext}^2_A(A/I,A)\simeq
\operatorname{Hom}_{A/J}(A/I,A/J),
\]
this map sends the generator of the left side to \(\det M\bmod J\).
The right side identifies with \((J:I)/J\). Thus \(J:I=(J,\det M)\),
and the determinant alone defines the residual attachment on \(C_0\).

On \(x_0=1\), use \(u=x_1,\ Y=x_2-u^3,\ Z=x_3-u^4\).
The first-normal matrix for \((-F,G)\) is
\[
\begin{pmatrix}
-4u^9&3u^8\\
-bu^{q-3}&-cu^{q-4}
\end{pmatrix}.
\]
Omit terms with zero coefficient, including the \(c=0\) term when
\(q=3\). Its determinant is \(q u^{q+5}\) since \(3b+4c=q\).
On \(x_3=1\), take \(v=x_2,\ X=x_0-v^4,\ Y=x_1-v^3\). Here
\(-F=X\) and \(G=(v^3+Y)^q-(v^4+X)^a v^b\), so the determinant is
\(q v^{3q-3}\). The two charts cover \(C_0\) and give total length
\(4q+2\). Reversal exchanges the two multiplicities on \(S_+\).

For \(q=7\) in characteristic zero, the six pairwise lengths at \(p_0\)
sum to \(18\), while the attachment to the union there has length \(12\).
At \(p_\infty\) the carrier is smooth and both lengths are \(18\).
The attachment divisor measures the intersection on \(C_0\). The residual
singularities and gluing require the residual algebra. If the characteristic
divides \(q\), the determinant vanishes identically on \(C_0\), and the
full torus equation gives the generic multiplicity in Section 3.

The October 27 independent audit reconstructed integral flatness, boundary
completeness and the cycle, and the above linkage and attachment formula with
\(q\) invertible. It executed the sparse Python determinant and lattice
checks and the separate Macaulay2 global colon and union-ideal checks for
\(q=3,4,7\) over \(\mathbf Q\). The general formulas use the written
arguments. [Original proof](https://github.com/markluxton1/STCI/blob/b271fc5bf20a6920b1540cabd57f095139d8d7a5/research/notes/2026-10-27-positive-characteristic-construction-interface.md#4-where-the-residual-curves-attach-and-what-normal-data-sees) ·
[Independent review and commands](https://github.com/markluxton1/STCI/blob/b271fc5bf20a6920b1540cabd57f095139d8d7a5/research/notes/2026-10-27-positive-characteristic-interface-audit.md#3-attachment-divisor-and-linkage-reconstructed) ·
[Python source](https://github.com/markluxton1/STCI/blob/b271fc5bf20a6920b1540cabd57f095139d8d7a5/research/computations/verify_mu_q_residual_interface_2026_10_27.py) ·
[Macaulay2 source](https://github.com/markluxton1/STCI/blob/b271fc5bf20a6920b1540cabd57f095139d8d7a5/research/computations/verify_mu_q_residual_linkage_2026_10_27.m2)

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


## Consolidated historical source: `research/supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md`

Original mathematical content and qualifications retained verbatim. Historical relative links may require repair.

# Boundary obstruction and endpoint scope investigations

## Integration guide: one-step obstructions and global endpoint tests

The [one-step boundary obstruction](#2026-10-27-one-step-boundary-obstruction) treats extensions in the **actual equation module**, not arbitrary formal transverse sections. Its independent audit keeps the Gorenstein final-step restrictions and the precise converse separate. The accompanying fixed-boundary smoothing audit concerns a different deformation problem and must not be read as a universal STCI obstruction.

Compare [global repair and weighted initials](normal_filtration_boundary_obstructions.md#boundary-repair-global-lifting): a repair divisor is useful only when the required correction belongs to the image of the global homogeneous source. [Intrinsic valuations](../synthesis/coefficient_valuations.md) supplies normal/coefficent valuation distinctions but not the missing global lift. [Rees and residual cycles](../synthesis/rees_and_vertical_controls.md) supplies cycle budgets but cannot substitute for this module-level test.

**Logical boundary:** one-step obstruction, final socle obstruction, and global residual-support exclusion are three different assertions. Retain the separate hypotheses and counterexamples in their source sections.

---

Full historical mathematics retained, including independently reviewed limits.

---

<a id="2026-10-27-one-step-boundary-obstruction"></a>

## One-step boundary repair and the final Gorenstein obstruction

Date: 2026-10-27. Status: new research deduction, with
[independent audit](#2026-10-27-one-step-boundary-obstruction-audit).
No unrestricted STCI exclusion or literature novelty
claim is made. The argument treats whole classes of embedded multiple
curves; no sampled pair is used.

### 1. Scope and the actual equation module

Let C be a smooth connected projective curve over an algebraically closed
field, regularly embedded in a smooth threefold X. Let I=I_C and E=I/I^2.
Let Y be an embedded pure Cohen--Macaulay thickening with sole support C
and generic transverse algebra k(C)[y]/(y^n), n>=2. Put J=I_Y and

    L=((I O_Y)/(I O_Y)^2)/torsion, R=ker(E -> L),
    M_Y=(J/IJ)/torsion.

All torsion is over O_C. The module M_Y is a rank-two vector bundle:
generically Y has ideal (x,y^n), and a torsion-free coherent sheaf on C
is locally free. Its first-symbol map has image R(-B_Y), with B_Y effective.

Purity implies I^n O_Y=0 and hence I^n subset J and I^(n+1) subset IJ.
Therefore there is a canonical map

    Sym^n E=I^n/I^(n+1) -> J/IJ -> M_Y.

It kills R Sym^(n-1)E: this holds generically and its target is torsion
free. Thus it factors as an injection u_Y:L^n -> M_Y. Let U_Y be its
image and let Ubar_Y be its saturation. Both have generic rank one,
and Ubar_Y is the kernel of the first-symbol map. There is a canonical
effective divisor A_Y with

    U_Y=L^n, Ubar_Y=L^n(A_Y),
    0 -> Ubar_Y -> M_Y -> V_Y=R(-B_Y) -> 0.              (1)

Write

    e_Y in Ext^1_C(V_Y,Ubar_Y)=H^1(C,Ubar_Y tensor V_Y^vee)

for the extension class of (1). This class depends on the actual embedded
lower thickening, rather than only the degrees of its normal layers.
The triple version of this equation-module construction is inherited
reviewed evidence in the
[intrinsic cubic-contact note](../synthesis/quartic_pair_obstruction.md).
The argument here uses the power-relation line for arbitrary n.

### 2. Exact one-step repair theorem

Fix an effective divisor D and the proposed next saturated layer

    T=L^n(D),

with its prescribed multiplication inclusion i_D:L^n -> T. Consider
embedded extensions Z of Y for which J/I_Z=T is killed by I and the
normal multiplication is i_D.

**Theorem.** Such an extension necessarily has A_Y<=D. Once that
inequality holds, extending i_D to a map M_Y -> T is equivalent to

    image(e_Y)=0 in
    H^1(C,Ubar_Y tensor V_Y^vee(D-A_Y)).                 (2)

The maps extending i_D, if any, form a torsor under H^0(V_Y^vee tensor T).
Among them, the surjective maps correspond to actual embedded pure CM
extensions with the specified layer and generic length n+1. Surjectivity
is an additional condition, automatic when D=A_Y.

Proof. An actual extension gives a surjection

    J/IJ -> J/I_Z=T,

since IJ subset I_Z. It factors through M_Y because T is torsion free.
On U_Y its restriction is the prescribed i_D. To extend this map to the
saturation Ubar_Y=L^n(A_Y), the necessary and sufficient regularity
condition is A_Y<=D; then the extension there is uniquely the inclusion

    gamma: Ubar_Y -> T=Ubar_Y(D-A_Y).

Apply Hom_C(-,T) to (1). The obstruction to extending gamma to M_Y is
the pushout of the extension class e_Y along gamma. Functoriality of
Ext identifies it with (2). The kernel of the restriction map is
Hom_C(V_Y,T), giving the stated torsor of global solutions.

Conversely, compose a surjective solution q:M_Y -> T with J -> M_Y
and let I_Z be its kernel. It is an ideal, contains IJ, and gives

    0 -> T -> O_Z -> O_Y -> 0.

Both the left and right terms are CM of dimension one, so O_Z is pure
CM as well. The extension is square-zero since J^2 subset IJ. At the
generic point, q is nonzero on the relation y^n, and the kernel has
ideal (x-c y^n,y^(n+1)) after a change of parameters; the generic length
is n+1. The quotient O_Z/T=O_Y is pure, so T is saturated, and it is
the last saturated normal layer. Normal multiplication is i_D by
construction. When D=A_Y, gamma is an isomorphism, so every extending
q is surjective. Otherwise surjectivity needs testing only at the
finite zero divisor D-A_Y of gamma. This proves the theorem. No global
retraction of Y or Z to C has been used. Square-zero here refers to the
extension ideal T; it does not assert that the whole nilradical squares
to zero.

This proves a controlled-modification comparison for a FIXED lower
embedding. The exact available repair divisor is D-A_Y, rather than D.
The lower embedding, its A_Y and its e_Y must be varied together in a
family; one cannot vary the boundary while freezing unrelated obstruction
data from a different lower scheme.

### 3. Applying the socle budget

Suppose Y occurs as a saturated truncation of a solely supported,
generically curvilinear Gorenstein multiple curve Z_full of length m.
Write its saturated layers as W_i=L^i(D_i), and D_soc=D_(m-1).
Use the inherited perfect pairings and effectivity in their stated
quasiprimitive scope:

    W_i tensor W_(m-1-i) -> W_(m-1) is perfect,
    D_i+D_(m-1-i)=D_soc, D_0=D_1=0.

In particular 0<=D_i<=D_soc. If the next layer after Y is W_n, theorem
(2) requires e_Y to die after the exact twist D_n-A_Y, and hence after
the possibly larger twist D_soc-A_Y. This is now a proven necessary
repair bound, with coefficient one, for this particular lifting class.
It does not assert that all ambient obstruction problems share this
target or the same twist.

The [principal-parts and multiplication-kernel criterion](normal_filtration_boundary_obstructions.md#boundary-repair-global-lifting)
can be applied to the actual bundle Ubar_Y tensor V_Y^vee. On P1 this
is a line bundle, and all possible effective repair divisors can be
tested by one multiplication matrix. The actual divisor must also
satisfy its prescribed linear system and all paired-layer constraints.
Passing a relaxed pole test is not sufficient for a Gorenstein or CI
extension.

### 4. The final Gorenstein step has no extra repair allowance

**Corollary (necessary splitting).** Let Z_full be as in section 3 with
m>=3, and let P_i be its saturated normal ideals. Take

    Y=Z_full/P_(m-1), n=m-1, T=P_(m-1)=W_(m-1).

Then

    Ubar_Y=T, A_Y=D_soc, e_Y=0,                         (3)
    M_Y=Ubar_Y direct_sum V_Y.

The splitting is a necessary condition for a Gorenstein completion of
this fixed penultimate embedded thickening. A nonzero e_Y excludes
EVERY such completion, regardless of the total socle-divisor degree.

Proof. The actual extension gives q:M_Y -> T. Its restriction to
Ubar_Y is nonzero generically and hence injective between line bundles.
There is an intrinsic product map

    j:W_1 tensor W_(m-2) -> M_Y.

Lift the two factors to ambient functions in I and multiply. Their
product belongs to J=I_Y and has zero first normal symbol, so its class
lands in Ubar_Y. Changing a lift of W_(m-2) by P_(m-1) changes this
class by IJ. Changing a lift of W_1 by P_2 gives a class with zero
image under q, because P_2 P_(m-2) subset P_m=0, and also zero first
symbol, because the ambient product lies in I^2. It is therefore zero
in the torsion-free M_Y, since q is injective on Ubar_Y. Changes of
ambient representatives vanish modulo IJ; the same argument verifies
O_C-bilinearity without a global coefficient-field splitting.

The composite q j is the perfect Gorenstein pairing

    W_1 tensor W_(m-2) -> W_(m-1)=T.

It is an isomorphism. Since j lands in Ubar_Y, q|Ubar_Y is consequently
an isomorphism. Thus q supplies a retraction of the inclusion Ubar_Y
in M_Y, and (1) splits. Comparison of the canonical multiplication
L^(m-1) -> T with u_Y identifies their actual zero divisors, giving
A_Y=D_soc. This proves (3).

The restriction m>=3 is essential: when m=2 the lower scheme is C
itself, and E -> L need not split. Under the actual Gorenstein
hypothesis, the first-symbol divisors of Y and Z_full do agree: the
perfect pairing gives P_1 P_(m-2)=P_(m-1) subset K^2, so quotienting by
P_(m-1) adds no new first-order relation. This equality is a consequence
of the pairing, not an identification made for arbitrary lower schemes.

This is a class-wide obstruction on embedded lower thickenings. It
does not state the converse: splitting M_Y need not yield a Gorenstein
completion, and gives no two global carrier equations on its own.

#### Full one-step Gorenstein criterion for a fixed lower Y

The missing converse has an exact additional condition. Let W_i be the
saturated normal layers of Y, 0<=i<n, with W_i=L^i(D_i). Ambient
multiplication gives canonical maps

    j_i:W_i tensor W_(n-i) -> Ubar_Y, 1<=i<n.

Indeed products lie in J. Changes of representatives vanish generically
in IJ, hence vanish in the torsion-free M_Y; this also proves O_C-linearity.
Their images lie in the kernel of the first-symbol map. Compatibility
with ordinary powers gives the actual divisor

    div(j_i)=A_Y-D_i-D_(n-i)>=0.

**Theorem.** Y admits an embedded Gorenstein curvilinear completion of
generic length n+1, preserving this lower embedding, iff

    e_Y=0 and A_Y=D_i+D_(n-i) for every 1<=i<n.          (3a)

Necessity is the preceding corollary and the perfect top pairings.
For sufficiency choose a retraction q:M_Y -> Ubar_Y and construct Z by
section 2 with T=Ubar_Y. It is pure CM, with the old saturated lower
layers and new top Ubar_Y. Its top multiplication pairings are q j_i,
which are perfect by (3a). Complete at a point and choose a local curve
parameter D=k[[t]]. The CM algebra is finite free over D. A basis
adapted to its saturated flag has a Frobenius Gram matrix with zero
entries beyond the antidiagonal and unit antidiagonal, by these perfect
pairings. A functional taking the coefficient of the top basis element
therefore gives a perfect D-pairing. Hence Z is Gorenstein.

The completions, when they exist, form a torsor under
H^0(V_Y^vee tensor Ubar_Y). This is an embedded Gorenstein extension
criterion. It does not produce two global homogeneous equations of
specified degrees. The numerical divisor equalities alone are insufficient:
the extension class e_Y is part of the actual embedded data.

### 5. An exact universal contact test for the actual global source

Keep the fixed embedded lower thickening Y of length n>=2. Let C have
degree d, choose a,b with ab=(n+1)d, and take actual forms

    F in H^0(P3,J(a)), G in H^0(P3,J(b)).

Their classes induce

    rho_(F,G): O_C(-a) direct_sum O_C(-b) -> M_Y,
    theta_Y(F,G)=wedge^2 rho_(F,G)
        in H^0(C,det M_Y tensor O_C(a+b)).

**Theorem (exact fixed-lower-source test).** On the open locus where F,G
are a proper pair, their intersection W has sole reduced support C iff
theta_Y(F,G)=0. If theta_Y(F,G) is nonzero, the generic multiplicity
along C is exactly n and the residual degree is d.

Proof. At eta_C the ideal J_eta has two minimal generators, because
Y_eta is curvilinear. Removing O_C-torsion does not change that generic
fiber, so (M_Y)_eta=J_eta/m J_eta. The determinant is nonzero iff the
classes of F,G span that two-dimensional space. Nakayama then gives
(F,G)_eta=J_eta, and the generic length is n.

If the determinant is zero, the containment (F,G)_eta subset J_eta is
strict, so the generic transverse length of W is at least n+1. It is
finite by properness. Bezout bounds it by ab/d=n+1. Equality therefore
holds and exhausts the total degree; purity of a proper complete
intersection leaves neither a residual curve nor an embedded component.
Conversely sole support gives length n+1 by degree, hence strict
containment and zero determinant. A section of the determinant line
is zero iff its generic value is zero, which makes this a global test.

Thus this stage involves the entire source map

    Theta_(Y;a,b): H^0(J(a)) tensor H^0(J(b))
        -> H^0(C,det M_Y tensor O_C(a+b)).                (4)

For a=b, it is alternating and factors through wedge^2 H^0(J(a)). The
zero pencils are the Plucker linear section

    Gr(2,H^0(J(a))) intersect P(ker Theta),

with the common-surface-factor locus removed. For a!=b use the Segre
product P H^0(J(a)) times P H^0(J(b)) intersect P(ker Theta), again on
the proper-pair open set. All coefficients are actual global constants.
This is not a sampled example or a symbolic-section surrogate.

For an arbitrary admissible family of lower thickenings, these maps
vary on cohomology/rank strata. A theorem that every decomposable
kernel point is improper excludes the whole family. A proper kernel
point gives actual existence at the specified degrees. Showing only
that the generic source has nonzero determinant leaves the special
kernel locus unresolved. Classifying all admissible lower embeddings
and computing their actual source maps remain substantive work.

The triple case is the intrinsic cubic-contact construction cited above.
This argument gives its determinant/degree-exhaustion meaning for every
curvilinear lower length n; it does not replay the accepted quartic
classification or prove its nonvanishing by formal target degree.

#### Uniformly small target for the fixed rational quartic

Before testing a prospective degree-(a,b) completion, its penultimate Y
must satisfy the top-line adjunction requirement

    Ubar_Y=omega_C tensor O_C(4-a-b).

Using V_Y=R(-B_Y) and det E=R tensor L=omega_C^(-1) tensor O_C(-4),
the determinant target simplifies to

    det M_Y tensor O_C(a+b)=L^(-1)(-B_Y).               (4a)

This is a line-bundle identification on the admissible locus; it is
not assumed for an arbitrary lower Y unrelated to those carrier degrees.
For the fixed characteristic-zero rational quartic, L=O(-q) with
1<=q<=7 in the sole-support curvilinear CI setting. Thus the target
in (4) has dimension max(q-deg B_Y+1,0)<=8. For every admissible fixed
penultimate Y, the whole actual-source contact test requires at most
eight bilinear equations, or eight Plucker-linear equations when a=b.
This does not classify those Y or prove that their proper kernel loci
are empty. The following simplification is essential: on the fully
Gorenstein-admissible locus these equations are automatic in the main
rational-quartic degree range, so their small number must not be sold
as an additional nontrivial obstruction there.

There is also a conditional class-wide dimension test. Let P be the
Segre source product (or the Grassmannian for equal degrees), and let
r be the rank of Theta as a linear map on the ambient tensor/wedge
space. Its zero locus on P is a projective linear section of codimension
at most r. If dim P>=r and the improper-pair locus has codimension >r
inside P, projective dimension theory forces a proper zero point.
By the exact source theorem this proves fixed-degree existence. Thus
an exclusion on such a source family must account for a sufficiently
large improper locus, a failure of the lower admissibility conditions,
or a genuinely small source. No generic codimension estimate for that
improper locus is asserted here.

#### Exact fixed-surface criterion when the top layer has no source sections

Assume Y satisfies the full Gorenstein-completion criterion (3a), and
the top line Ubar_Y is identified with T=omega_C tensor O_C(4-a-b).
Choose a retraction q:M_Y -> T and let Z be its completion. For an
actual degree-a section F through Y, the image q(F) is a global section
of T(a); similarly q(G) belongs to H^0(T(b)). Therefore, if

    H^0(C,omega_C tensor O_C(4-b))=0,
    H^0(C,omega_C tensor O_C(4-a))=0,                    (4b)

ALL degree-a and degree-b forms through Y also vanish on Z. Equivalently
the exact ideal sequence 0 -> I_Z -> I_Y -> i_*T -> 0 has identical
global section spaces in those degrees. Consequently Theta is
identically zero for these sources, not just zero on selected pairs.

For C0, omega_C=O_P1(-2) and O_C(1)=O_P1(4). The two bundles in (4b)
are O(14-4b) and O(14-4a), so (4b) always holds when a,b>=4.

The automatic source vanishing itself is more general than the rank-two
curvilinear construction. For any Gorenstein multiple structure Z with
smooth sole support C, its socle T=Ann_(O_Z)(I_C O_Z) is the line
omega_C tensor (omega_Z|C)^(-1), and the quotient Y=Z/T is pure.
If omega_Z|C=O_C(s) and C is rational, then H^0(T(d))=0 for d<=s.
Hence H^0(I_Y(d))=H^0(I_Z(d)) throughout that degree range. For a
degree-(a,b) CI, s=a+b-4, so both carrier degrees lie in this range
when a,b>=4. This explains the source collapse without requiring a
particular generic transverse Hilbert function. Constructing the
admissible Y and its Gorenstein completions by the rank-two method
above still requires generic curvilinearity.

There is a simple exact properness criterion for the whole source.
Let H_a=H^0(P3,I_Y(a)) and H_b=H^0(P3,I_Y(b)), both nonzero. Over the
infinite field k, a coprime pair F in H_a, G in H_b exists iff no
irreducible surface divides EVERY section of BOTH spaces. To prove
the nontrivial direction, first choose F avoiding the finitely many
irreducible factors of the fixed gcd of H_b. Each avoidance excludes
a proper linear subspace of H_a. Then choose G avoiding the finitely
many factors of F, again outside a finite union of proper subspaces.
The converse is immediate.

**Exact realization criterion in this range.** Fix a,b with
ab=(n+1)deg C and (4b). A fixed lower Y is the penultimate level of a
sole-support degree-(a,b) CI iff:

1. It satisfies (3a), so an embedded Gorenstein completion exists.
2. Its saturated power line is Ubar_Y=omega_C tensor O_C(4-a-b).
3. Both actual source spaces H_a,H_b are nonzero and they have no
   common fixed surface component.

For sufficiency, construct one completion Z using (1)--(2), choose
the coprime global source pair from condition 3, and use (4b) to see
that both equations vanish on Z. Its degree is ab, so a proper CI
containing it has the same cycle and is equal to Z: the kernel of
O_CI -> O_Z would be a punctual subsheaf of the pure O_CI. Necessity
follows from sections 4--5 and CI adjunction. In that direction generic
curvilinearity is automatic: the Artin Gorenstein generic CI algebra
has a length-one ideal as the kernel of its map to Y, hence that ideal
is its socle. In length at least three the socle lies in the square of
the maximal ideal, so its quotient has the same embedding dimension.
The quotient Y is curvilinear. Purity identifies Y with the saturated
penultimate truncation. This is a criterion for a FIXED actual lower
embedding. Classifying all such Y is still open.

Thus, for C0 and a,b>=4, there is no further source-determinant
nonvanishing problem on the fully admissible splitting locus. The
global obstruction there is exactly a missing source space or a common
fixed surface in the two actual linear systems. For other curves or
degrees where (4b) fails, the universal bilinear/Plucker test remains
necessary to examine.

There is an additional necessary rigidity condition in this range:

    H^0(C,V_Y^vee tensor Ubar_Y)=0                     (4c)

for any Y that actually occurs as the penultimate level of that global
CI. Otherwise (3a) supplies more than one distinct embedded Gorenstein
completion. By (4b), every degree-a and degree-b form through Y vanishes
on every completion. A single proper degree-(a,b) pair would contain
all of them, and degree exhaustion would make all completions equal,
contradicting their distinct normalized retractions. Thus a positive-
dimensional completion torsor forces failure of the global source test.
On P1, (4c) is simply deg Ubar_Y<deg V_Y. It is a useful preliminary
filter; it is not sufficient for a CI realization.

### 6. A separate budget on the actual two-equation module

Now assume Z_full=V(F_a,G_b) is a proper CI with sole support C and
generic transverse length m>=2. For its ideal J_full put

    D_eq=J_full/IJ_full=O_C(-a) direct_sum O_C(-b),
    F^r D_eq=((J_full intersect I^r)+IJ_full)/IJ_full.

Let B_full be the first-symbol divisor, so the image in E is R(-B_full).
There are canonical endpoints

    F^2 D_eq=ker(D_eq -> E)=K_eq,
    F^m D_eq=L^m, F^(m+1) D_eq=0.

The top inclusion has ACTUAL divisor

    div(F^m D_eq -> K_eq)=D_soc+B_full.                 (5)

One must not infer (5) merely by equating determinant line bundles.
A local multiplicative Tor comparison proves its coefficientwise form.
Choose integral normal parameters x,y with X spanning R and Y mapping
to L. The top equation y^m gives the normal Koszul cycle (0,y^(m-1)).
An equation f=A x+B y gives (A,B). Their Tor product is

    +/- (A|C) y^(m-1) e_X wedge e_Y.

The carrier Koszul resolution identifies the product with the exterior
product in D_eq, while normal Tor_2 is Ann_(O_Z)(I O_Z) tensor det E.
Thus the wedge map L^m tensor R(-B_full) -> det D_eq factors as the
top-power inclusion of divisor D_soc and the first-symbol inclusion
of divisor B_full. Their divisors add, proving (5).

Every intermediate F^r is a rank-one subsheaf between these endpoints.
Writing G_r=F^r/F^(r+1), telescoping gives

    sum_(r=2)^(m-1) div(G_r)=D_soc+B_full<=2 D_soc.      (6)

The inequality uses the first-normal bound in [R0019](../results/quasiprimitive_residual_cycles.md), in its specified
finite-flat/saturated scope. This is an equation-module cost, distinct
from the structure-sheaf torsion (m/2)D_soc.

For the reviewed spectral comparison, write

    Q=in_I(J_full)/S_+ in_I(J_full),
    0 -> Delta_r -> Q_r -> G_r -> 0.

Generic curvilinearity gives Delta_eta=0. The torsion comparison yields

    sum_r div(tors Q_r)
      =D_soc+B_full+sum_r div Delta_r.                  (7)

Hence (6) is NOT a bound on all raw initial-equation torsion unless
Delta=0. Higher spectral cancellations must be retained. See the
[normal Koszul comparison](../results/normal_koszul_comparison_defect.md)
for the spectral argument and the
[open sole-support question](../FRONTIER.md#punctual-relative-defect-under-sole-support)
for the remaining existence problem.

### 7. What has been gained and what remains

The proposed boundary-repair comparison is now proved for the specific
one-step obstruction e_Y in (1). The final Gorenstein step sharpens it
to exact vanishing: its top divisor is already fully used in saturating
the power relation and cannot be counted again as new repair allowance.
The actual-source determinant test (4) is exact after properness and
degree exhaustion; the CI equation module has the separate cost (5)--(7).

These results make the next family-level questions definite:

- Determine the zero locus of e_Y for admissible embedded lower
  thickenings; a nonzero class excludes all final Gorenstein completions.
- On its zero locus, impose local Gorenstein/pairing conditions and the
  top adjunction line. For C0 with a,b>=4, then test the two actual
  source spaces and their common fixed surfaces; the source determinant
  is automatic there. In degree ranges where (4b) fails, retain the
  full source determinant test.
- In earlier stages, use the exact remaining divisor D_n-A_Y and the
  common-divisor principal-parts test; total degrees alone discard this
  information.

The source-sensitive jet images and finite fixed-degree endpoint remain
those in the preceding repair note. No whole admissible family has
been proved to have e_Y nonzero here, so no new STCI exclusion follows.

### 8. Literature and provenance boundary

The perfect-pairing characterization of Gorenstein multiple structures
belongs to the established theory. The inspected primary source
Manolache, [Gorenstein Multiple Structures on Smooth Algebraic Varieties](https://arxiv.org/pdf/0706.2204),
section 2 and remark 2, treats canonical filtrations and their duality,
and identifies the quasiprimitive specialization. That paper supports
the classical background; the fixed-lower equation-module extension and
actual-source determinant arguments used here are proved in this note.
No claim is made that these reformulations are new in the literature.
The source and its four pages were inspected on October 27; no broader
literature-exhaustion claim is made. Accepted source-level filtration
inputs and result scopes are retained rather than re-certified.

---

<a id="2026-10-27-one-step-boundary-obstruction-audit"></a>

## Independent audit: one-step boundary and final Gorenstein obstruction

Date: 2026-10-27. Reviewer: independent `equation_budget_audit` agent.
Status: mathematical reconstruction of the [source note](#2026-10-27-one-step-boundary-obstruction),
No new unrestricted STCI exclusion or realization
of an unclassified family is certified.

### Scope and method

The reviewer read research/INDEX.md first, then the minimal spectral and
first-normal premises. The source's final saved text was read, including
the refinement that the source determinant is automatic after full
Gorenstein admissibility and the stated cohomology vanishings.

The base setting is a smooth connected projective curve C in a smooth
threefold X over an algebraically closed field, and an embedded pure CM
lower thickening Y with sole support C and generic curvilinear length
n>=2. The arguments are characteristic independent except for the
explicit characteristic-zero conormal description of C0.

Accepted saturated pairings and the first-normal bound R0019
are premises, not rerun proofs. The reviewer independently checked the
new equation-module constructions, extension argument, converse,
source criterion, and coefficientwise divisor comparison. No isolated
example or finite sample was used to infer a family statement.

### 1. The equation module and its power line

For J=I_Y, M=(J/IJ)/torsion is a rank-two vector bundle on C: the
generic ideal is a curvilinear two-generator complete intersection,
and torsion-free coherent sheaves on a smooth curve are locally free.
The first-symbol map has rank-one image R(-B_Y).

Purity proves I^n O_Y=0 from generic nilpotence. Therefore I^n subset J
and I^(n+1) subset IJ, giving Sym^n E -> M. Its generic kernel is
R Sym^(n-1)E, and this entire subbundle maps to zero because M is
torsion free. The quotient L^n maps injectively. Its saturation Ubar
is exactly the kernel of the first-symbol map, yielding the source's
sequence (1) and actual inclusion divisor A_Y.

This construction retains the embedded ideal. It is not determined
solely by the ranks and degrees of the ordinary normal layers.

### 2. One-step extensions and their exact obstruction

An extension by the O_C-line T=L^n(D), killed by I, induces a map
J/IJ -> T. Its torsion-free target makes it factor through M. Extending
the prescribed map L^n -> T first to Ubar=L^n(A_Y) is possible exactly
when A_Y<=D, and then that map is uniquely the natural inclusion.

Applying Hom(-,T) to 0 -> Ubar -> M -> V_Y -> 0 shows that extending
this inclusion to all of M is equivalent to vanishing of the pushout
of e_Y. Naturality of Ext identifies the pushout with the map

    H^1(Ubar tensor V_Y^vee)
      -> H^1(Ubar tensor V_Y^vee(D-A_Y)).

Thus the source's available repair divisor D-A_Y and its torsor
H^0(V_Y^vee tensor T) are correct. It would be incorrect to use all of D
as new repair allowance after A_Y has already been used in saturation.

For the converse, a surjective q:M -> T gives the ideal kernel of
J -> M -> T; it contains IJ. The resulting sequence
0 -> T -> O_Z -> O_Y -> 0 is CM of dimension one by the depth lemma.
The ideal T is square zero because J^2 subset IJ. Generic nonvanishing
on y^n makes the generic quotient the curvilinear extension of length
n+1. Since O_Y is pure, T is saturated in O_Z and is the final
saturated layer. The prescribed ordinary multiplication is the map
L^n -> T. This verifies the exact converse stated in section 2.
Surjectivity is automatic when D=A_Y; otherwise it is an additional
condition at the finite vanishing divisor of Ubar -> T.

### 3. The final Gorenstein step and the full converse

For a genuine final Gorenstein completion, the map q:M -> T is
generically injective on Ubar. Multiplying ambient representatives of
W_1 and W_(m-2) defines the source's map j into Ubar. Changes of lifts
give zero generically in J/IJ and hence zero in the torsion-free M;
the source's argument using q and the saturated product also verifies
the same fact without assuming a global coefficient retraction.
The composite qj is the inherited perfect top pairing. It follows that
q|Ubar is an isomorphism, and normalizing by it gives a retraction of
Ubar in M. Hence e_Y=0. Compatibility with the ordinary power maps
identifies A_Y with D_soc as an actual divisor, not merely by degree.

For arbitrary fixed lower Y, the maps

    j_i:W_i tensor W_(n-i) -> Ubar, 1<=i<n,

are indeed canonical. Products vanish generically in O_Y, so purity
puts them in J. Changes of representatives lie generically in IJ;
their classes therefore vanish in M. This also proves O_C-linearity.
The products have zero first symbol and thus land in Ubar. Composing
with the ordinary maps from L^i and L^(n-i) yields the degree-n power
map, proving the ACTUAL divisor formula

    div(j_i)=A_Y-D_i-D_(n-i).

Necessity of e_Y=0 and zero divisors of every j_i follows from a
Gorenstein completion. Conversely, a retraction q constructs a pure CM
completion with top Ubar, and the old saturated lower layers are
preserved. If every j_i is an isomorphism, its top pairings are perfect.
Locally over a lifted parameter DVR, a basis adapted to the saturated
flag gives a Frobenius Gram matrix: entries beyond the antidiagonal
are zero and antidiagonal entries are units. A top-coefficient
functional is therefore perfect, proving the completion Gorenstein.
This independently verifies the source's iff criterion (3a).

The m>=3 restriction is correct. When the lower scheme is C itself,
its conormal E need not split; that case is outside the rank-one
first-symbol setup used here. Under the final Gorenstein pairing,
the top ideal is contained in K^2, so passing to the penultimate level
does not add first-order relations. The equality of the two first-symbol
divisors is therefore justified in this scope.

### 4. Exact actual-source determinant and its limits

At eta_C, J has two minimal generators and M_eta=J_eta/m J_eta.
The determinant of two actual carrier sections is nonzero exactly when
their classes span this space, which by Nakayama is equivalent to
generating J_eta. Their generic length is then n. If the determinant
vanishes, their ideal is strictly smaller, so a proper pair has generic
length at least n+1. Under ab=(n+1)deg C, Bezout makes this equality
and exhausts degree; purity leaves no residual curve or embedded point.
This proves the exact source criterion, including the residual degree d
when the determinant is nonzero.

The Segre/Grassmannian description uses actual global section spaces,
so its unknowns are constants in k. No generic formal-symbol surrogate
has been substituted. A generic nonzero determinant does not exclude
its exceptional zero locus, as the source explicitly records.

The conditional dimension assertion is valid for the nonempty Segre or
Grassmannian source: a section by r ambient linear equations is
nonempty when dim P>=r, and has dimension at least dim P-r. A closed
improper locus of larger codimension cannot contain it. The source
makes no unjustified general estimate of that improper locus.

### 5. Small target and the essential automatic-vanishing refinement

On the top-adjunction-admissible locus, det M=Ubar tensor R(-B_Y)
and Ubar=omega_C O_C(4-a-b) give exactly

    det M tensor O_C(a+b)=L^(-1)(-B_Y).

For C0 in characteristic zero, 1<=q<=7 gives the claimed target
dimension at most eight. This is an upper bound on the source contact
equations, not automatically a set of eight nontrivial conditions.

The source's later refinement is necessary and correct. Once a global
retraction q:M -> T exists, the quotient of any actual degree-a
section through Y is a section of T(a)=omega_C O_C(4-b), and similarly
for degree b. If both cohomology spaces vanish, every such section
already vanishes on the completion. Therefore Theta is identically
zero on this source, with no further determinant obstruction.
For C0 and a,b>=4 the bundles have degrees 14-4b and 14-4a, so the
vanishings hold. This statement is also valid for any smooth curve
satisfying the source's two displayed cohomology vanishings.

For two nonzero section spaces over an infinite field, existence of
a coprime pair is equivalent to absence of a common fixed irreducible
surface. The finite-union-of-proper-linear-subspaces argument in the
source proves the nontrivial direction exactly: choose F avoiding all
fixed factors of H_b, then G avoiding every irreducible factor of F.

Consequently the exact fixed-lower realization criterion is valid in
the stated range. For sufficiency the constructed completion has degree
ab, and all source sections vanish on it. A proper CI containing it
has the same cycle; its kernel over the completion is a punctual
submodule of a pure CI structure sheaf and is zero. Thus the schemes
are equal. This does not classify all admissible Y or supply a proper
pair in an unclassified family.

#### Final source refinements: socle quotients, curvilinearity, and rigidity

The final saved source contains three further consequences, which the
reviewer independently checked. They do not require a sampled example.

First, for any Gorenstein multiple structure Z with smooth sole support,
its socle Ann_(O_Z)K is the O_C-line omega_C tensor (omega_Z|C)^(-1)
by finite duality. It is saturated: locally a lifted curve parameter t
is a nonzerodivisor, and tb in Ann K implies t(bK)=0 and hence bK=0.
The quotient by this socle is therefore pure CM. For rational C and
omega_Z|C=O_C(s), the line T(d)=omega_C O_C(d-s) has negative degree
whenever d<=s. Its H^0 vanishes, so the ideal exact sequence proves
H^0(I_Y(d))=H^0(I_Z(d)). This source collapse does not use generic
curvilinearity. The rank-two classification of its possible completions
does still use that separate hypothesis.

Second, in the necessity direction of the exact realization criterion,
a generic Artin Gorenstein CI algebra mapping onto the curvilinear
length-one-shorter algebra has a length-one kernel. Such an ideal is
the socle. In length at least three that socle lies in the square of
the maximal ideal: if m^2=0 and the length were at least three, the
socle would have dimension at least two; otherwise the last nonzero
power m^s, s>=2, is already the unique socle. Quotienting by it
preserves embedding dimension. Since the quotient is curvilinear,
the original algebra is curvilinear too. Purity then identifies the
lower Y with the saturated penultimate truncation.

Finally, the completion torsor has distinct embedded ideals for
distinct normalized retractions. Indeed two surjections with the same
kernel differ by an automorphism of the target line, and their
restrictions equal the identity on Ubar, forcing that automorphism
to be the identity. Under (4b), all actual degree-a and degree-b
sections through Y vanish on every such completion. A single proper
pair would contain every completion; equal degree and purity would
make all of them the same scheme. Thus an actual CI in this range
requires H^0(V_Y^vee tensor Ubar_Y)=0. On P1 this is equivalently
deg Ubar_Y<deg V_Y, exactly as in (4c). It is only a necessary
rigidity condition, and the source does not assert sufficiency.

All three final refinements pass audit with their stated hypotheses.

### 6. Actual equation-module and spectral divisor accounts

For an actual CI of generic curvilinear length m, purity gives
I^m subset J_full and I^(m+1) subset IJ_full. The same power-line
argument yields F^m D_eq=L^m and F^(m+1)=0. Also F^2 is the line
kernel of the first-symbol map D_eq -> R(-B_full).

The coefficientwise inclusion divisor needs the source's multiplicative
Tor argument; determinant line-bundle isomorphisms alone give only a
class or linear equivalence. The reviewer independently reconstructed
that argument. A normal Koszul cycle for y^m is (0,y^(m-1)), while
f=Ax+By gives (A,B). Their product is, up to sign,
(A|C)y^(m-1) times the normal determinant frame, because the top power
annihilates the nilradical. Carrier Tor identifies this with the wedge
in D_eq, and normal Tor_2 is the socle times det E. Thus the actual
zero divisor is D_soc+B_full.

Intermediate equation quotients are torsion, and telescoping gives
sum div G_r=D_soc+B_full. The R0019 first-normal divisor is the image
of the TOTAL ideal of the multiple structure, hence equals B_full;
its bound applies here without the auxiliary-surface hypotheses of
its separate residual-cycle assertion. This verifies the bound by
2 D_soc in the specified finite-flat/saturated setting.

Generic curvilinearity makes Delta generically zero, so the reviewed
torsion comparison gives the source's equality

    sum div tors Q_r=D_soc+B_full+sum div Delta_r.

The 2 D_soc bound does not apply to raw initial-equation torsion
without subtracting Delta. The source preserves the unresolved
punctual-Delta question and does not claim to settle it.

### Outcome

**PASS for the inspected source, including the automatic-source refinement.**
No substantive correction is required. The explicit one-step lifting
comparison and its final Gorenstein sharpening are independently
reconstructed. The exact contact criterion and fixed-surface reduction
apply to a whole fixed lower embedding, without sampled examples.
The source does not prove that the admissible lower-embedding family
has a proper source point or that its fixed-surface condition always
fails. Those remain the global classification question.

All new claims remain reviewed research evidence. The
audit does not reopen an accepted exclusion. No inherited certificate or proof was replayed.

---

<a id="2026-10-26-ci-cycle-fixed-boundary-node-smoothing-audit"></a>

## Independent final audit of node smoothing at fixed boundary

Date: 2026-10-26. Reviewer: independent cycle-notebook audit agent.
Status: exact tangent calculation and local deformation interpretation
reviewed.

This finishes review of the existing
[fixed-boundary node-smoothing calculation](../synthesis/fixed_boundary_smoothing.md).
The underlying line-plus-degree-eleven curve has its separate
[geometric audit](../synthesis/explicit_quartic_residuals.md).
No new investigation is started here.

**Outcome.** The ranks \(19,5,24\) are correct for the actual global quartic
source. The fixed-boundary fiber is locally smooth of dimension fourteen,
and its five residual node parameters have independent differentials.
After splitting and labelling the geometric nodes, its complete local ring
can be written \(k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]]\), with the
attachment divisor on the marked \(C\) exactly fixed. This is a local formal
existence statement, with the local algebraic interpretation in section 4;
it is not a displayed polynomial path or an all-pairs result.

### 1. Independent reconstruction from the global source

The reviewer rebuilt the calculation in a separate standard-library Python
program. It enumerates the thirty-five degree-four monomials, groups them
by \(w=m_1+3m_2+4m_3\), and uses the **last** monomial in each group as its
reference, rather than the verifier's first. The resulting eighteen
differences form another basis of the actual global kernel
\(H^0(I_C(4))\). All coefficients remain rational constants.

For a monomial difference of common weight \(w\), the first-normal
coefficients in \(X=x_3-u^4,Y=x_2-u^3\) are
\[
(m_3-m'_3)u^{w-4},\qquad
(m_2-m'_2)u^{w-3}.
\]
The base-pair symbols were reconstructed directly from the actual
\((a,b)=(1,1)\) forms:
\[
\sigma_f=(h_0-1)X+(-uh_0-1)Y,
\]
\[
\sigma_g=(h_1-3u^8-2u^9)X+
               (4u^9+3u^{10}-uh_1)Y,
\]
where \(h_0,h_1\) are the restrictions of the documented quadrics.
The affine boundary derivative is
\[
D(h,k)=\det(\sigma_h,\sigma_g)+\det(\sigma_f,\sigma_k).
\]
Every one of these thirty-six polynomial directions has degree at most
eighteen **before** extraction of its nineteen coefficients. Thus the matrix
representation does not silently discard a higher coefficient.

On the line \([-r:r:-1:1]\), the same global monomial restricts to
\((-1)^{m_0+m_2}r^{m_0+m_1}\). Reduction modulo
\[
P=4r^5-2r^4+9r^3+2r^2+3r+2
\]
gives the five-dimensional rational node algebra. Squarefreeness is sufficient;
the calculation does not need to assume this algebra is a field or to choose
five rational roots.

Using the independently reconstructed first symbols and a different echelon
elimination gives
\[
\operatorname{rank}D=19,\qquad
\operatorname{rank}S=5,\qquad
\operatorname{rank}(D,S)=24.
\]
The independent output also records highest boundary degree eighteen.
The durable
[verifier](../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py)
was read and replayed, and its five explicit rational tangent witnesses were
checked against the combined matrix. Its
[JSON evidence](../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json)
preserves their thirty-six source coefficients and exact images.
The separate
[independent reconstruction audit](../synthesis/fixed_boundary_smoothing.md)
records another reconstruction and the same quotient calculation.

### 2. Why the five-dimensional functional is the node map

The two relevant normal derivatives along the line are
\[
F_1=-r(r+1)(r+2),\qquad G_1=-4r^3+2r^2-9r-1.
\]
\(F_1\) is a unit modulo \(P\). At each node the complete gradient rows
are proportional with ratio \(G_1/F_1\). Eliminating the smooth first
carrier equation therefore gives the first-order smoothing constant
\[
k|_L-(G_1/F_1)h|_L.
\]
Multiplication by the unit \(F_1\) gives exactly
\[
S(h,k)=F_1k|_L-G_1h|_L\pmod P.
\]
This proves that the five-dimensional output is the direct sum of the five
geometric \(T^1\) directions, with harmless invertible scalings after base
extension. It is not merely a chosen list of polynomial evaluations.

The combined rank implies
\[
\operatorname{rank}(S|_{\ker D})=24-19=5.
\]
The displayed tangent witnesses satisfy \(D=0\) exactly and span that output.
Selecting just one labelled geometric node can require a splitting field;
surjectivity over the rational étale algebra is the appropriate rational
statement.

### 3. The Grassmannian quotient does not change the conclusion

The ordered source has dimension thirty-six. Its four-dimensional
infinitesimal change-of-basis space consists of
\[
(\alpha f+\beta g,\gamma f+\delta g).
\]
Every such direction has \(S=0\), since \(f\) and \(g\) vanish at each node.
Its boundary derivative is
\((\alpha+\delta)\Delta\), where \(\Delta\ne0\) is the base determinant.
Thus the trace part accounts for the scalar determinant direction.

Let \(D^{-1}(k\Delta)\) be the tangent space preserving the *projective*
boundary. It has dimension \(36-19+1=18\). Quotient by the four-dimensional
basis-change space gives the fourteen-dimensional tangent space to the
boundary fiber in \(\operatorname{Gr}(2,18)\).
Any member of \(D^{-1}(k\Delta)\) can be adjusted by a trace direction to lie
in \(\ker D\), without changing \(S\). The node output is therefore still
surjective on the Grassmannian fiber. Its common tangent kernel has dimension
\(14-5=9\).

This explicitly checks the distinction between zero affine derivative and
zero projective boundary derivative. Neither an extra node direction nor a
lost node direction comes from scaling the two equations.

### 4. The formal conclusion and its additional hypotheses

The proper-pencil parameter space is smooth of dimension thirty-two.
Surjective \(d\beta\) makes its boundary fiber smooth locally at the checked
point, of dimension fourteen. Work over an algebraically closed
characteristic-zero field, or first extend to split and label the five nodes.

The proper flat residual family required for the local node description
can be obtained on \(\operatorname{Bl}_C\mathbf P^3\): the two strict-transform
divisors of class \(4H-\mathcal E\) meet properly, and their relative regular
sequence is flat near the checked member. At the eighteen simple attachments
to \(C\), the residual blowdown is an isomorphism; these conditions remain
open. This is the family bridge reviewed in the line-degeneration audit,
not an inference from matrix rank alone.

For each split residual node the completed local family has equation
\(xy-\tau_i=0\). The relevant standard input is
[Stacks, Lemma 53.20.11](https://stacks.math.columbia.edu/tag/0CBX), with the
[étale counterpart](https://stacks.math.columbia.edu/tag/0CBY).
The differential \(d\tau_i\) is the node functional above up to a unit.
Consequently the five \(d\tau_i\) on the fixed-boundary fiber are independent.
They can be extended to a regular system of formal parameters, giving
\[
\widehat{\mathcal O}_{\beta^{-1}(\beta_0),[f,g]}
\simeq k[[\tau_1,\ldots,\tau_5,z_1,\ldots,z_9]].
\]

Hence one may prescribe the five node smoothing parameters independently in
this completed neighborhood while retaining the exact boundary value
\(\beta_0\). This uses regularity and the formal inverse-function argument,
in addition to the finite calculation. In particular the rank statement
does more than merely suggest possible independent smoothings.

The additional étale local algebraic interpretation in the contribution is
also valid. After one common étale base change supplying the five labelled
node charts, their parameters are regular functions. The map from the
fixed-boundary fiber to \(\mathbf A^5\) given by these parameters is smooth
near the marked point. Pulling back a pattern \(\tau_i=c_it\) gives a smooth
morphism over a neighborhood of zero on \(\mathbf A^1\). A smooth morphism
with the chosen rational point in its fiber admits a section after an
étale change of that base. This yields a local algebraic curve of pencils
with exactly fixed boundary and the prescribed smoothing pattern. It is
an existence deduction, not an explicit list of global quartic coefficients.

It does not mean that the first-order tangent witnesses themselves define
constant-boundary linear paths: the determinant has quadratic and higher
changes along \(f+th,g+tk\). Correcting higher coefficients or producing a
specific polynomial/rational path is an additional construction, expressly
not supplied by this result.

### 5. Final scope and completion

The local inference applies to the checked pencil and its marked boundary
fiber. It does not classify the entire fiber, determine all global topology
strata, or prove a residual component for every homogeneous pair. The
interpretation of partial smoothing by contraction of edges in the residual
dual graph is useful local geometry; an explicitly computed algebraic
subfamily remains a different deliverable.

The exact ranks, rational witnesses, quotient dimensions, and formal
fixed-boundary conclusion pass final independent review. No remaining defect
was found in the current calculation.

---

<a id="2026-10-26-endpoint4-nonsplit-node-scope-audit"></a>

## Scope audit: the selected endpoint-four carrier has a nonsplit generic node

Date: 2026-10-26. Reviewer: `pencil_geometry`, independently reconstructing
the local-to-global implication. **Completed fixed-carrier scope bridge,
with two exact finite certificates; research.** The local node lemma and the modular-to-characteristic-zero
argument are distinct from the finite rank computations. This final audit
starts no new computation or research lane.

### Validated jet-kernel input and independent finite evidence

The selected rational sextic is
\[
F_*=-q^2x_3^2-qDx_2+D^2/4+q^3,
\quad q=x_0x_3-x_1x_2,\quad D=x_2^3-x_1x_3^2.
\]
The [actual-sextic construction](toric_sextic_residuals_and_limits.md#every-prescribed-second-symbol-has-an-actual-sextic-lift) uses the
following completed finite input:
\[
\{G\in H^0(\mathbf P^3,\mathcal O(16)):
G_\eta\in(F_*)+\mathfrak m^{12}\}
=F_*H^0(\mathbf P^3,\mathcal O(10)).
\tag{1}
\]
The audit inspected two implementations. The Result preserves a
[maintained rank replay](../results/ci_fixed_sextic_jet_rigidity.md#exact-evidence-and-independent-verification).

* The [Macaulay2 certificate](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_m2_2026_10_25.m2),
  its [execution metadata](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_m2_2026_10_25.json),
  and [log](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_m2_2026_10_25.txt) record a
  \(690\times969\) matrix of rank 683 over \(\mathbf F_{65521}\),
  rank 286 for the known degree-ten multiples, and rank zero for their
  product with the jet matrix.
* The primary's [independent explicit normal-division implementation](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_jet_independent_2026_10_26.py)
  and [output](https://github.com/markluxton1/STCI/blob/f11123c0ab9fc4231ed0e5b21fc14a1b5fdecef7/research/computations/endpoint4_fixed_jet_independent_2026_10_26.json)
  construct the quotient coordinates separately, recover rank 683,
  and annihilate all 286 known multiples at every sample.

A failed intermediate annihilation check was traced to a multiline
Macaulay2 assignment that included only the first two terms of the global
carrier. Parenthesizing the whole assignment restored all four terms;
the corrected checks above pass, and the implementation correction is
preserved in the metadata. The failed check is not evidence for (1).

Here is the rank-lifting argument, separately from the computations. Over
\[
B=\mathbf Z[1/2,z,z^{-1},(1+z^2)^{-1}],
\]
the coefficient \(z^8(1+z^2)\) of the quadratic \(u^2\) term is a unit.
Explicit normal division modulo \(\mathfrak m^{12}\) gives the free
23-element basis
\[
1,v,\ldots,v^{11},\quad u,uv,\ldots,uv^{10}
\]
for \(B[u,v]/(F_*,\mathfrak m^{12})\). Its rule replaces \(u^2\)
by a multiple of \(v^2\) plus higher-total-degree terms; higher terms
terminate at degree twelve. More explicitly, the 78 truncated monomials
have 55 relations given by \(F_*\) times monomials of degree at most
nine. Ordering first by increasing total degree and then by decreasing
\(u\)-exponent makes their 55 pivot coefficients units; the nonpivot
monomials are exactly the displayed 23. Thus the remainder maps of all 969 global
monomials have coefficients in \(B\). A generic formal compatibility
identity makes that rational remainder identically zero and therefore
zero under each good specialization. The samples \(z=1,\ldots,30\)
are good modulo 65521: neither \(z\) nor \(1+z^2\) vanishes there.

The modular rank 683 is consequently a lower bound for the rational
specialized matrix rank. Its kernel has dimension at most 286. The 286
global multiples are independent, lie in the generic compatible kernel,
and are killed by every sample map, so both the sample kernel and the
generic compatible kernel are exactly this known space. This proves
(1); the constant rational coefficient maps and their ranks persist
under every characteristic-zero extension of the coefficient field.
Neither implementation substitutes free \(k(z)\)-coefficients for the
constant global source. This audit reads the persisted finite evidence
and independently reconstructs its scope bridge; it does not rerun those
completed rank computations.

Let \(k\) be a characteristic-zero coefficient field, \(K=k(z)\), and
\(A=K[[u,v]]\), with \(\mathfrak m=(u,v)\), in the actual balanced chart
\[
(x_0,x_1,x_2,x_3)=(1,z,z^3+v,z^4+u+\tfrac32zv).
\]
The quadratic term of \(F_*\) is
\[
z^8\bigl((1+z^2)u^2-z^2v^2/4\bigr).
\tag{2}
\]
The discriminant square class is \(1+z^2\). This is nonsquare in \(K\):
over an algebraic closure of the constant field the polynomial has two
simple zeros, whereas a rational square has even valuations. Thus the
nonsplit property persists under every characteristic-zero extension of
the constant field. Extending the function field to its algebraic closure
would lose precisely the Galois constraint used below and is not the
allowed global coefficient operation.

### The nonsplit-node lemma, with finite-length hypotheses

Suppose \(G\in\mathfrak m\) and \(A/(F_*,G)\) has finite length. Then there
is an integer \(n\ge1\) such that
\[
\operatorname{length}_A A/(F_*,G)=2n,
\qquad G\in(F_*)+\mathfrak m^n.
\tag{3}
\]
More precisely, the largest power in this membership condition is \(n\).
Here finite length is essential: if \(G\) vanished identically on a
formal branch after splitting, intersection length would not be finite.

To reconstruct the assertion, pass to the finite separable quadratic
field
\[
L=K(\sqrt{1+z^2}).
\]
Weierstrass preparation in \(u\) is available because the coefficient
of \(u^2\) in (2) is a unit of \(K\). Its monic quadratic has discriminant
\(v^2\) times a unit whose leading coefficient becomes a square in \(L\).
The square root of the remaining unit, normalized to have constant term
one, exists by the formal Hensel recursion in characteristic zero.
Consequently \(F_*\) factors over \(L[[u,v]]\), up to a unit, as
\[
(u-\phi_+(v))(u-\phi_-(v)),\qquad
\phi_\pm(v)=\pm\frac{z}{2\sqrt{1+z^2}}v+O(v^2).
\]
The two smooth branches are transverse, and their formal series are
exchanged by the nontrivial element of \(\operatorname{Gal}(L/K)\).
Since \(G\) is defined over \(K\), its branch restrictions are Galois
conjugate. Their finite orders are therefore the same integer \(n\).

Intersection length is the sum of these branch orders. For an elementary
way to see this without discarding the node's gluing, the prepared
quadratic quotient is free of rank two over \(L[[v]]\). The determinant
of multiplication by \(G\) is the product of its two branch restrictions;
the length of its cokernel is the \(v\)-order of that determinant, hence
\(2n\). Scalar extension from \(K\) to \(L\) leaves the numerical Artinian
length unchanged, when measured over the respective residue fields.

Membership can also be checked directly. Divide \(G\) by the prepared
quadratic, leaving a remainder \(a(v)u+b(v)\). The difference of the two
branch restrictions is
\(a(v)(\phi_+(v)-\phi_-(v))\). Both restrictions have order at least \(n\),
and the parenthesized factor has order one, so
\(a(v)\in(v^{n-1})\). It follows that \(b(v)\in(v^n)\). The remainder is
therefore in \((u,v)^n\). Conversely every element of \((u,v)^n\) has
order at least \(n\) on each smooth branch. This establishes the precise
membership equivalence after splitting. Faithfully flat field extension
descends the membership to \(A\); alternatively the unique prepared
remainder is already defined over \(K[[v]]\).

This argument tests the potentially delicate edges: it uses actual
Galois-conjugate branches, finite intersection length, both branch orders,
and membership for the *whole formal ideal*. It does not infer a complete
initial ideal from the two individual leading symbols.

### Consequence for every proper degree-sixteen mate on this selected carrier

Let \(G\) be any homogeneous degree-sixteen form over \(k\) such that
\(W=V(F_*,G)\) is a proper complete intersection and contains the fixed
reduced quartic \(C\). Properness ensures finite generic transverse
length along \(C\). Completion preserves this length, and (3) says its
cycle coefficient is \(m_C(W)=2n\).

If \(n\ge12\), membership in (3) implies
\(G_\eta\in(F_*)+\mathfrak m^{12}\). The validated kernel equality (1),
which persists under characteristic-zero coefficient-field extension,
forces the global equality \(G=F_*H_{10}\). That pair is not proper.
Hence every proper pair in this precise fixed-carrier, fixed-degree scope has
\[
\boxed{m_C(W)=2n\le22.}
\]
Bézout gives \(\deg W=6\cdot16=96\). Its residual fundamental cycle
therefore has degree
\[
\boxed{\deg\bigl([W]-m_C(W)[C]\bigr)=96-8n\ge8.}
\tag{4}
\]
In particular, the residual cycle is nonzero. Equivalently, sole support
\(C\) would require \(m_C=96/4=24\), so \(n=12\), which (1) excludes.
Complete-intersection purity rules out hiding degree in isolated embedded
components instead of a positive-dimensional residual cycle.

This implication needs **neither** the full generic initial-CI type
\((2,12)\), saturated first relation, movement-two classification, nor
any assertion about other endpoint-four carrier parameters. Those
hypotheses explain the origin of \(F_*\), but its nonsplit generic node
and the validated fixed-carrier jet kernel suffice for (4). The
conclusion covers one selected sextic and degree-sixteen mates only.
The rest of the endpoint-four family and unrestricted STCI questions remain unchanged.
The bound is not claimed to be attained. The completed finite test and
this independently reconstructed scope bridge do not exclude any larger family.
