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

The [component and contact proof on \(S_+\)](../arithmetic/positive_characteristic_constructions.md#12e-generic-multiplicities-and-contacts-among-binomial-components)
and the prescribed [\(\mu_4\) result R-0021](../../results/quartic_mu4_degeneration.md)
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
The [binomial generators of \(I_{C_0}\)](../carriers/projection_and_elliptic_gluing.md#13-the-full-fiberwise-inverse-and-descent-tests)
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

In characteristic zero the [full projective stabilizer proof](../curve/quartic_projection_and_special_geometry.md#4-full-projective-automorphism-group)
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
[ruled divisor](../arithmetic/arithmetic_four_section_family.md#2-the-flat-relative-divisor-of-four-moving-sections)
has equation \(q_{\rm rul}^4-h^4\), with sections \(q_{\rm rul}=\zeta h\)
over a splitting field of characteristic zero. Its characteristic-two
equation is \((q_{\rm rul}-h)^4\). The projective intersection has generic
length four along \(C_0\) in that fiber. The endpoint algebras of the
projective image have the separate description in R-0021 and the
[embedded quotient proof](../torus_embedded_quotients.md#the-fourth-root-image-and-its-conductor).

### 3.1. A binomial degree and a descending singleton-support power

The semigroup \(\langle3,4\rangle\) records which transverse character
equations admit the displayed homogeneous binomial compactification.
The stronger question of a mate with
sole support on this fixed carrier has the
[existing normalization criterion](../arithmetic/positive_characteristic_constructions.md#all-mate-degrees-on-a-fixed-cuspidal-quartic).
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
lengths are both three. [Ruled and projective contact comparison](../arithmetic/positive_characteristic_constructions.md#12e-generic-multiplicities-and-contacts-among-binomial-components).

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
[full supported Hilbert-limit argument](../torus_hilbert_boundary.md#closed-incidence-and-both-full-limits)
starts with \(P=I_{C_0}\) and \(P^N\subset J\subset P\).
Every intrinsic-torus translate lies in the fixed closed incidence
\(C_0\subset Y\subset V(P^N)\). Both full opposite limits retain
support \(C_0\) and the Hilbert polynomial, while possibly acquiring
embedded structure and additional minimal generators. The ideal of two
extreme forms need not be the full limit. An invariant arrangement with
residual curves supplies a control example, not a boundary of this
sole-support incidence merely by being invariant. The
[supported-boundary framework](../../frameworks/torus-supported-boundaries/index.md#directional-loci)
tests two-generation on moving ideals; their fixed limits need not be
two-generated.

**Endpoint descent.** The
[embedded quotient and endpoint account](../torus_embedded_quotients.md)
retains multiplication, homogeneous source spaces and endpoint lattices.
Finite transverse characters and jet filtrations provide comparisons in
the explicit models; abstract quotient type or contact lengths do not
determine arbitrary global homogeneous equations.

**Characteristic comparison.** The
[positive-characteristic constructions](../arithmetic/positive_characteristic_constructions.md)
explain coalescence for the prescribed binomial arrangements. Obstructions
to lifting prescribed embedded structures do not exclude unrelated
characteristic-zero STCI presentations.

The proposed invariant-carrier obstruction in the toric source is already
covered by the
[weight-homogeneous-carrier theorem](equivariant_degree_bounds.md#the-bound-and-its-exact-large-prime-minimum):
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

No affirmative answer is asserted here. In particular, the rooted contact filtration is only a comparison invariant for the displayed cyclic orbit; it does not characterize a full Hilbert limit or determine a thickening ideal.

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


## Boundary one-step obstruction and endpoint geometry

The [one-step boundary theorem](#2026-10-27-one-step-boundary-obstruction) concerns the **actual equation module**, not arbitrary formal transverse sections. Its final Gorenstein restriction and converse have distinct hypotheses. Fixed-boundary node smoothing is a separate deformation question; neither result alone excludes unrestricted STCI. [Weighted initial repair](../normal-geometry/normal_boundary_weighted_initials.md#boundary-repair-global-lifting) additionally requires a global homogeneous correction, while [coefficient valuations](coefficient_valuations.md) and [Rees residual cycles](../normal-geometry/rees_and_vertical_controls.md) supply different numerical controls.

<a id="2026-10-27-one-step-boundary-obstruction"></a>

## One-step boundary repair and the final Gorenstein obstruction

The [one-step repair theorem and its applications](../one_step_boundary_repair.md#2026-10-27-one-step-boundary-obstruction)
give the fixed-lower extension criterion in the actual equation module.

<a id="2026-10-27-one-step-boundary-obstruction-audit"></a>

## Independent audit: one-step boundary and final Gorenstein obstruction

The [independent reconstruction](../one_step_boundary_repair.md#2026-10-27-one-step-boundary-obstruction-audit)
records the checked scope, including the fixed-surface criterion.

---

<a id="2026-10-26-ci-cycle-fixed-boundary-node-smoothing-audit"></a>

## Independent final audit of node smoothing at fixed boundary

Date: 2026-10-26. Reviewer: independent cycle-notebook audit agent.
Status: exact tangent calculation and local deformation interpretation
reviewed.

This finishes review of the existing
[fixed-boundary node-smoothing calculation](../residuals/fixed_boundary_smoothing.md).
The underlying line-plus-degree-eleven curve has its separate
[geometric audit](../residuals/explicit_quartic_residuals.md).
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
[verifier](../../computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py)
was read and replayed, and its five explicit rational tangent witnesses were
checked against the combined matrix. Its
[JSON evidence](../../computations/ci_fixed_boundary_node_smoothing_2026_10_25.json)
preserves their thirty-six source coefficients and exact images.
The separate
[independent reconstruction audit](../residuals/fixed_boundary_smoothing.md)
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
The [actual-sextic construction](../carriers/endpoint_four_actual_sextics.md#every-prescribed-second-symbol-has-an-actual-sextic-lift) uses the
following completed finite input:
\[
\{G\in H^0(\mathbf P^3,\mathcal O(16)):
G_\eta\in(F_*)+\mathfrak m^{12}\}
=F_*H^0(\mathbf P^3,\mathcal O(10)).
\tag{1}
\]
The audit inspected two implementations. The Result preserves a
[maintained rank replay](../../results/ci_fixed_sextic_jet_rigidity.md#exact-evidence-and-independent-verification).

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
