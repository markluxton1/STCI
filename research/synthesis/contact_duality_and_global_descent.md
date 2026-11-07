# Contact duality and global descent

The fixed embedded quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) remains an open
characteristic-zero existence problem: can two homogeneous equations
have exactly this reduced support? This account studies necessary
structure of an arbitrary hypothetical proper pair and explicit controls
showing why several proposed shortcuts do not answer that question.
For an intersection containing residual curves, the sole-support conclusions
below require separate justification on its primary part.

**Review status (2026-10-31).** Independent mathematical and preservation review reconstructed this replacement and its explicit characteristic extensions. The varying-Hilbert-function local control, degree-four defect notation, and ribbon section calculation were checked in their corrected homes. No material finding remains unresolved within the stated scopes. These remain reviewed deductions; no computation or inherited certificate rerun was needed.

All deductions in the four linked proof chapters retain **independently
reviewed** status. Their source proofs and corrections were
reviewed on the source branch. Inputs, including the conormal splitting and
full-socle formula, remain governed by their result records. Every displayed
calculation below has a complete algebraic proof in its owning chapter;
no recorded rank or unperformed computation substitutes for one.

## The approaches and their exact reach

| Approach | Object retained | What is established | What remains missing |
|---|---|---|---|
| [Jacobian/contact](contact_jacobians_and_hamiltonian_actions.md) | Actual CI ideal and actual socle line | All six Jacobians recover tangent sextics; exact different/colon and involutive ideal | Quartic-specific incompatibility, or a pair satisfying the global identities |
| [Full tropical modification](tropical_thickenings_and_endpoint_duality.md) | Entire saturated finite family \(W\to\mathbf P^1\), its two contracted subalgebras and conductor schemes | Every characteristic-zero pair forces positive embedded movement and no two global Cartier equations upstairs | Whether its image can have two compatible homogeneous equations downstairs |
| [Polarization root](polarization_roots_and_section_defects.md) | Full nilpotent root algebra, its grading and reduced vertex defect | A unique ample fourth root; Gorenstein full algebra; exact invariant defect and restrictions on reduced section images | A theorem forcing forbidden sections or a construction of the requisite fourth Veronese |
| [Embedded-neighborhood and Rees controls](section_defects_and_exceptional_cover_controls.md) | Specified section-lifting class; actual normalized exceptional cover | First-order obstruction persists; exceptional covers can be branched with unbounded genus | A proved link to actual residual support using the fixed quartic's equation spaces |

The [foundation account](global_equations_and_constructions.md) supplies related
actual-equation and affine-descent formulations when available; these are
not replacements for the full objects above. The difference between the
rank-\(m=ab/4\) tropical projection and the degree-\(ab\) pencil
\([x_0:x_3]\) is essential. The first uses the parameter of the reduced
curve itself; the second reduces to its fourfold cyclic cover.

## Characteristic is part of each mechanism

The fixed curve has an STCI with a quartic carrier in
[every positive characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
The characteristic-free parts of this account are therefore compatibility
conditions that such equations may satisfy, not hidden nonexistence claims.
The full tropical closure, conductor modules/pairings, endpoint indices and
constant-family two-divisor lemma do not require separability or an inverse
multiplicity. Strict movement uses characteristic-zero Hellus–Hübl and
fails for the explicit characteristic-seven constant family. Actual
Jacobian socle recovery instead needs the multiplicity \(m\) invertible;
its displayed symplectic/tame-cover interpretation additionally needs two
invertible. The root construction and perfect degree-four torsor pairing
extend when four is invertible, while its degree-one image restriction
also needs six invertible. The smooth-cubic moving control requires
\(p\ne2,3\); the exceptional cyclic-cover control requires \(p\nmid re\).
Each owning proof states precisely which assertions extend and which
steps fail. No exponential action or complex-analytic deformation theorem
is transferred to characteristic \(p\) merely from a formal identity.

## Duality supplies a module before it supplies a number

For a hypothetical pair \(Z=V(F_a,G_b)\), the actual socle is
\(\mathcal S=\mathcal O_{\mathbf P^1}(14-4a-4b)\). The local
projection-change lemma proves that its relative Jacobian is a generator
for every local parameter étale on the smooth support. Comparing algebraic
parameters \(z+\lambda u\) forces the mixed minors to vanish. This is the
intrinsic mechanism behind the tangent sextic tuple and exact contact
identity: the complete-intersection differential has one surviving direction
in its socle, fixed by the reduced tangent geometry. The proof requires no
normal flatness and no absolute trace normalization across different
projections.

The conductor of the full tropical modification is another dualizing
module, now on \(W\):

\[
\omega_W=\mathfrak c\otimes\rho^*\omega_Z,\qquad
\pi_*\mathfrak c=\mathcal B^\vee\otimes\mathcal O(14-4a-4b).
\]

This is an actual module identification. Its local quotient retains an
Artinian Gorenstein algebra \(D\) and a half-length self-orthogonal
**subalgebra** \(E\subset D\), with \(A=B\times_D E\). Replacing this by
its determinant forgets multiplication and descent; it gives only the
already-known genus equation. Replacing it by a scalar is worse: the
explicit length-four local example has non-Gorenstein \(B\) and a
nonprincipal conductor, although the downstairs algebra is CI and its
finite conductor quotient is Gorenstein.

The root algebra uses duality in a third way. Its fourth-power torsor has
an actual trace pairing perfect off the vertex; the full section modules'
depth two extends that pairing across the vertex. Hence the full root
algebra is Gorenstein. Its reduction can still have a finite vertex defect.
A Gorenstein statement about the nilpotent cover therefore cannot be
substituted for normality or CM of its reduced cover.

These are proved applications of finite/closed-immersion duality to three
different objects. They are a shared mechanism, **not** theorem arrows
identifying those objects or their defects.

## Lifting and descent have to retain the marked equation data

The missing coordinate \(s^2t^2\) has a rank-two first-order obstruction
represented by the graph-normal extension
\(0\to\mathcal O(-3)^2\to\mathcal O(-2)^3\to\mathcal O\to0\).
This identifies the actual section, not an arbitrary extension with matching
degrees. Every entirely thick torus translate and both full Hilbert limits,
including their pure hulls, contain this same first neighborhood. Thus the
obstruction survives there automatically; asking it to vanish would already
contradict a fixed embedded neighborhood. Torus-invariant Gorenstein
quadric multiples independently have exactly four linear sections while
failing ACM in higher twists.

The tropical family measures a different lifting failure. Its Plücker degree
is positive because degree zero would make the whole embedded quotient
constant, force torus invariance of the actual CI ideal, and contradict
Hellus–Hübl's extreme-component theorem for this exact quartic. Positivity
also rules out **every** global two-Cartier-divisor presentation upstairs
by adjunction. It does not rule out a homogeneous CI image after contraction.
For every \(m\ge2\), the explicit smooth-cubic multiple \(mC\) has a moving
curvilinear family and both primitive Gorenstein contractions. Its two affine
pieces are themselves genuine scheme CIs, yet every homogenization of
an affine generating pair introduces a residual curve, because the common
projective thickening cannot be a homogeneous CI. Thus local equations and
local Gorensteinness fail to retain the required global twists and gluing.

For roots the analogous retained datum is equivariant: the reduced root
algebra has \(D_4=k\cdot s^2t^2\), while its other fourth-divisible defects vanish.
A known twisted-cubic CI has a Gorenstein root algebra with nonnormal
reduction and an ample root without sections, but zero invariant defect.
It controls general root-based inferences without disposing of the quartic's
specific invariant defect. Taking normalization or affinizing the reduced
puncture erases precisely the data one hopes to use.

## From a defect to actual residual support: the missing implication

For a proper pair with
\([V(F,G)]=m[C]+R\), one has \(ab=4m+\deg R\). To use any defect above
as a positive cost in this equality, one must prove that it cannot be
absorbed into the \(C\)-primary thickening and must create a curve component
outside \(C\). The following distinctions block an automatic inference:

* Endpoint lattice indices measure functions gained by a finite modification;
  they are not degrees of residual curves.
* Conductor schemes are finite boundary pinching schemes; their length identity
  is the genus identity, not an additional residual budget.
* Root defects occur at a cone vertex and measure failure of section extension
  through nilpotents. They are not established attachment lengths.
* Ramification of normalized exceptional covers can consist of whole
  pencil-direction curves mapping to points on the support. The explicit
  line-support CI has such branched covers of unbounded genus and no residual
  curve downstairs.
* Hamiltonian actions in the entirely thick branch move only nilpotent
  transverse structure, kill the whole socle, and force cofactors in \(I_C\).
  Their large kernel prevents direct use of reduced constant-kernel deformation
  theory; failure of that theory's hypotheses is not nonexistence.

A sufficient constructive bridge would be a moving finite family with two
compatible endpoint pinching algebras whose projective image has a saturated
ideal generated by two forms with prescribed twists. A sufficient obstructive
bridge would show that every such candidate violates that actual presentation,
or would bound allowed primary concentration so that a positive residual cycle
is unavoidable. No such universal bridge is proved here. The displayed moving
family and the twisted-cubic/contact/Rees controls explain which weaker
conditions are insufficient.

## Literature and bounded stopping points

The primary literature is integrated where its hypotheses are checked:
CI Jacobian/different formulas and finite duality; the reduced Legendrian
and Lagrangian deformation settings; Tevelev and Luxton–Qu's tropical
compactification guarantees; Hellus–Hübl's exact fixed-quartic theorem;
primitive multiple-curve geometry; affine Serre construction and
Quillen–Suslin; canonical-ribbon examples; and Jaffe's scope restrictions
on iterated curve blowups. None is cited as an unrestricted STCI theorem
for this embedding. No literature-priority claim is made.

The bounded synthesis isolates actual algebraic/geometric objects and
removes three unsupported upgrades: different-relative-map normalization,
scalar replacement of a canonical conductor module, and normalization of
a reduced root model without its vertex defect. It also separates proved
implications from common mechanisms. Further work requires the stated
homogeneous-realization or residual-support theorem; repeating local tests,
genus identities, or abstract cover normalizations alone cannot supply it.
