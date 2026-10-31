# Independent audit: canonical elliptic extension and mechanism selection

October 31, 2026. Reviewer: `canonical_mechanism_review`, independent of
both mechanism producers; no nested delegation.

**Verdict: PASS for the conditional reconstruction and sufficiency theorem,
and support the proposed single fixed-target construction experiment.**
No material mathematical correction was identified in the reviewed
[canonical-extension proposal](2026-10-31-elliptic-canonical-extension.md),
Sections 1–7, or in the allocation premises of
[the strategy assessment, Section 6](2026-10-31-unrestricted-strategy-assessment.md#6-executed-comparison-canonical-gluing-versus-duality-specialization).
This is independent review of a provisional contribution, not canonical
promotion. The target replay and its component-polarization, gluing and
determinant tests were **not run**. No actual carrier or mate is established.

## Scope and inherited evidence

The curve is the literal smooth rational quartic
\(C_0=[s^4:s^3t:st^3:t^4]\subset Q\subset\mathbf P^3\), over an
algebraically closed field of characteristic zero. The proposal starts
with a smooth elliptic curve \(E\), four distinct points \(P_i\), a map
\(h_E:E\to Q\) birational onto an integral \(C'\ne C_0\), complete
reduced inverse support \(h_E^{-1}(C_0)_{\rm red}=Z=\sum P_i\), distinct
finite nonzero markings \(t_i\), and
\(h_E^*\mathcal O_Q(1,1)\simeq\mathcal O_E(2Z)\).
All are hypotheses, rather than conclusions of an abstract passport.

I followed INDEX then MAP, checked the exact permitted cone model and
limitations in [R-0002](../results/cartier_singleton_lift.md) and
[Q-0001](../questions/cartier_projection_models.md), and read the
[survivor record](2026-10-30-projection-order-two-survivor.md),
[support argument](2026-10-30-projection-elliptic-target-incidence.md),
[its audit](2026-10-30-projection-elliptic-target-incidence-audit.md),
and [palindromic target record](2026-10-30-projection-elliptic-target-palindromic.md).
Their previously reviewed boundary classification is inherited evidence;
I did not reopen it or replay its computations. I independently checked
the Picard cancellation and interpolation argument where the new proposal
uses them. The target's individual exact construction still lacks its
separate independent computational replay.

## Reconstruction of the global source

For \(Y=E\cup_{P_i\sim t_i}\mathbf P^1\), normalization gives arithmetic
genus \(1+0+4-2+1=4\). The dualizing restrictions are
\(\omega_E(Z)\) and \(\omega_{\mathbf P^1}(\sum t_i)\).
Restriction of the four canonical sections to \(E\) is an isomorphism:
its kernel is \(H^0(\omega_{\mathbf P^1})=0\). On the rational component
restriction has a one-dimensional kernel \(H^0(\omega_E)\), so gives the
complete conic series. Degree-four Riemann–Roch on \(E\) separates every
length-two subscheme. The kernel section defining the conic's plane has
simple zero divisor exactly \(Z\) on \(E\). Thus the components meet
only in the prescribed four reduced points, their tangent lines there
are distinct, and the canonical map embeds the actual nodal union.
This checks the reducible curve directly.

The restriction of the pencil of quadrics through the elliptic normal
quartic to its four-point hyperplane section is an isomorphism onto the
pencil of conics through those points. The relevant \(H^1\) vanishes by
linear normality. No three of the four points are collinear, by the
degree-one remainder in elliptic Riemann–Roch. Hence the embedded conic
selects exactly one quadric. An integral nonplanar curve cannot be
contained in a union of two planes or a double plane. Therefore this
quadric is integral, including the possible rank-three case.

The cone case is essential and is correctly retained. A second quadric
through \(E\) cuts it scheme-theoretically: the complete intersection
is unmixed of degree four and already contains the integral degree-four
curve. Thus \(E\) is Cartier of class \(\mathcal O_S(2)\). A cone vertex
on it would make the two-quadric Jacobian rank at most one and contradict
smoothness. The plane of the smooth conic also avoids the vertex. Both
components, their transverse nodes, and the Cartier sum
\(Y\in|\mathcal O_S(3)|\) are therefore legitimate on either quadric.
There is no unexamined basepoint at the singular vertex later in the proof.

Geometrically, the source quadric and its ruling pencil(s) are fixed by
the marked nodal curve. There is no independent choice of elliptic
source pencils left after this reconstruction. On a smooth source the
two pencils recover the \((2,2)\) embedding; on a cone the two-pencil
description is replaced by its single ruling.

## Component polarization, actual gluing, and section recovery

Component compatibility and gluing are distinct. Only after the input
hyperplane identity holds does
\(\mathcal H\otimes\omega_Y^{-2}\) have trivial restrictions to both
components. Its gluing class then lies in \((k^*)^4/k^*\): the four
node scalars have one common rescaling. Agreement of the two maps to
\(Q\) at the nodes does not trivialize this class.

I checked the residue representative algebraically. With
\(R(t)=\prod(t-t_i)\), the section \((dt)^2/R(t)^2\) has divisor
\(4\infty\) in \(\omega_{\mathbf P^1}^2(2\sum t_i)\), matching the
coordinate section \(x_0\). Its quadratic residue at \(t_i\) is
\(1/R'(t_i)^2\). The local dualizing generator at a node is
\((du/u,-dv/v)\); squaring removes the sign. Consequently a common
rescaling matches the two components exactly when
\[
r_iR'(t_i)^2\quad (i=1,\ldots,4)
\]
are all equal. These entries are nonzero. Their equality gives precisely
the three torus gluing conditions, and makes the other coordinates match
because their ratios to \(x_0\) already agree at the nodes. This verifies
the proposal's formula without importing an analytic deformation theorem.

Once gluing vanishes, adjunction on the Gorenstein quadric gives
\(\omega_Y=\mathcal O_S(1)|_Y\). The restriction sequence
\[
0\to\mathcal O_S(-1)\to\mathcal O_S(2)\to\omega_Y^2\to0
\]
and \(H^0=H^1=0\) for its left term give the asserted unique extension
of all four target sections. Projective-space cohomology proves this on
the cone as well as on the smooth quadric. Thus section recovery has no
remaining free coefficient space for this fixed target and gluing.

The determinant vanishes on the Cartier union \(c+D\), so
\(q(U)=\Delta d_Dr\), with \(r\) a hyperplane section. The additional
condition \(r=\lambda\Delta\), \(\lambda\ne0\), is exactly the stated
divisor \(2c+D\). The zero case must be excluded, as the proposal does.
Three coordinates of \(r|_c\) vanish; this is not evidence that the target
incidence supplies three independent adjustable parameters.

## Sufficiency, multiplicities, and full inverse support

A common zero of the four recovered sections lies on \(q(U)=0\), whose
reduced support is \(c\cup D\). Their prescribed restrictions are a
morphism there, excluding every such zero. In particular the vertex,
which lies outside that support, cannot be a basepoint. The ample
pullback \(\mathcal O_S(2)\) prevents positive-dimensional fibers, so
the proper map is finite onto its integral surface image \(X\).

For generic degree \(e\), projection of the actual Cartier pullback of
the target quadric gives
\[
e[X\cap Q]=2[C_0]+[C'].
\]
The coefficient one at the distinct curve \(C'\), using the assumed
birational restriction on \(E\), forces \(e=1\). This establishes surface
birationality without assuming it in the construction. The degree is
\(\mathcal O_S(2)^2=8\). Every inverse point of \(C_0\) belongs to
\(c\cup D\); the full-support input on \(D\) puts all of its such
points in \(Z\subset c\). This covers isolated inverse points as well
as divisorial support. Since \(S\) is normal, the resulting finite
birational map is its image's normalization.

The converse is also correctly scoped: it recovers the reviewed smooth
order-two stratum and cone members with the stated smooth Cartier
primitive residual and transverse four-point intersection. It says
nothing about other cone residuals or arbitrary defining pairs. Actual
mate descent on \(X\) remains a separate requirement. Reduced nodal
gluing is not a substitute for the full conductor condition.

## Fixed candidate and stopping rules

The earlier target ramification argument gives
\(M=L\otimes\mathcal O_E(Z)\). It obtains
\(L^2=\mathcal O_E(Z)\) only after using actual-source polarization
\(LM=\mathcal O_E(2Z)\). The proposal correctly avoids reversing this
implication for the palindromic abstract target. Its component-polarization
test is a genuine unevaluated first gate. No identification of \(Z\)
with the branch divisor of the degree-two map \(A\) is needed or valid
from these Picard identities alone.

Conditional on that gate, the palindromic Möbius marking and the checked
degree-two interpolation lemma exclude a smooth canonical quadric:
each source ruling would equal the same degree-two function on \(E\).
The integral canonical quadric must then be a cone. This does not assert
that the gate passes, and the earlier smooth-source exclusion does not
exclude this cone case. R-0002 explicitly retains it as a necessary
normalization model, without promising a projection or a mate.

I support precisely this bounded sequence:

1. Independently replay the existing fixed target and its full normalized
   inverse support. Stop if its required target properties fail.
2. Evaluate \(L^2\simeq\mathcal O_E(Z)\). Stop this candidate if it fails.
3. Compute the four quadratic residues and test their common-scale
   equality. Stop if the gluing class is nontrivial.
4. Recover the unique source sections and test the nonzero determinant
   condition. Stop if it fails.
5. Only after success address the actual surface's full conductor and
   mate descent separately.

This is a constructive experiment on one already available incidence,
with a sufficient global success certificate. It is not another arbitrary
local exclusion: success produces an actual carrier in an explicitly
allowed model. A successful mate would settle existence without an
exhaustive reduction. Failure yields the exact polarization, gluing or
contact obstruction for this target and is not authorization for a serial
enumeration of further covers.

## Independent comparison with duality specialization

I checked the formal premises used for the allocation in assessment
Section 6. For the full flat family in \(\mathbf P^3_R\), codimension
two and \(R\)-flatness leave sheaf Ext in degrees two and three.
Derived reduction modulo \(\tau\) gives
\[
0\to\Omega/\tau\Omega\to\omega_H\to\mathcal E[\tau]\to0,
\qquad \mathcal E/\tau\mathcal E=T^D.
\]
Indeed the special curve has Ext\(^{2}\) equal to \(\omega_H\), since
its finite-length torsion contributes only to Ext\(^{3}\); its Ext\(^{3}\)
is \(T^D\). The preceding base-change term shows \(\Omega\) is
\(R\)-torsion-free. The \(\tau\)-torsion sheaf \(\mathcal E\) is
supported at the special endpoints, so its kernel and cokernel under
\(\tau\) have equal length there.

The primitive global canonical generator reduces to a nonzero section,
but need not generate the canonical module of the nonreduced transverse
algebra. If generic invertibility is additionally known, its cokernel in
\(\omega_H\) has length \(2\ell\): this follows already from Serre
duality, twisting by \(s=a+b-4\), and
\(\chi(\mathcal O_H)=\chi(\mathcal O_Z)-\ell\). The Ext sequence accounts
for one half, leaving the other half. Hence these are not two independent
numerical constraints.

I also checked the displayed line calibration against the retained
[full-limit proof](2026-10-30-four-streams-degeneration.md), Section 3.
On \(A_\tau\ne0\), modulo \(h\) one has
\(g=(-\tau/A_\tau)^d k\), and \(f=A_\tau h\), so the determinant is
\((-1)^d\tau^dA_\tau^{1-d}\). The saturation relations kill its quotient
by \(\tau^d\), and the localized presentation makes the exponent minimal.
Adjunction consequently yields the stated limiting coefficient
\(Z^{(d-1)^2}\), and the opposite one with \(W\). On the plane hull
\(V(Y,X^{d^2})\), its zero length is \(d^2(d-1)^2=2\ell\).
Thus this genuine supported CI accommodates the corrected twist and
opposite defects. The optional paper-specific perfect-pairing discussion
and other possible canonical-lattice calculations are not additional
premises of this verdict and were not independently audited here.

The allocation conclusion is supported: duality accurately describes
defect data but presently supplies no new bound or incompatibility using
the fixed quartic. A standalone duality campaign would require additional
quartic geometry. This does not exclude future uses of degeneration.

## Primary-source checks, generalization, and frontier impact

I inspected [Stacks 0ECH](https://stacks.math.columbia.edu/tag/0ECH): its
pushout hypotheses apply to the two closed immersions of the finite node
scheme. [Stacks 0C4S](https://stacks.math.columbia.edu/tag/0C4S) supplies
the Cartier ideal/invertible-sheaf framework, and
[Stacks 01XS](https://stacks.math.columbia.edu/tag/01XS) gives the
projective-space vanishings used above. In
[Wolpert, Section 2](https://arxiv.org/pdf/1204.3680), the nodal dualizing
and quadratic-residue interpretation agrees with the local algebraic
calculation; no complex-analytic deformation conclusion is transferred.
[Stacks 0E6N](https://stacks.math.columbia.edu/tag/0E6N) and
[0E5W](https://stacks.math.columbia.edu/tag/0E5W) confirm why the relative
dualizing complex, rather than presumed invertibility on a non-CM special
fiber, is the appropriate degeneration object.

These ingredients are classical. The reviewed contribution is their
specific synthesis into an intrinsic source reconstruction, a computable
gluing obstruction, unique global section recovery, and a sufficient
contact certificate for an actual singleton carrier. No literature
priority claim has been established. The theorem itself does not need
the degree-twenty passport or balanced contact; those belong to finding
an input target. Its reusable content is the separation of component
polarization, node gluing, and first-normal contact, together with the
fact that those exact gates imply several global admissibility properties
at once. No family-level vanishing, flexibility, or dominance theorem
for the gates follows.

No computation was executed in this review. No canonical record,
producer note, or navigation file was edited. The unrestricted
characteristic-zero STCI question remains open; the bounded next
experiment is now mathematically precise, with its success implication
and its stopping conditions independently checked.
