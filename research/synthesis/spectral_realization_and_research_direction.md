# Spectral realization in the wider intersection problem

This is the October 31, 2026 closeout and research assessment for the spectral
lane. The curve is the fixed characteristic-zero embedding
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Its unrestricted STCI
status remains open. The results below describe spectral curves, finite
embedded lifts, actual equation spaces and residual intersections at their
separate levels. The recommendations do not presume nonexistence.

## 1. Evidence and the boundary of this assessment

The spectral starting checkpoint is `0046beca62e36a1f1d02bdd05dbf900dd5670b56`.
The [order-three proof](order_three_roots_and_sextic_lifts.md) owns its
parameterization and exact selected-slice calculation; the
[all-power](spectral_pushforward_powers.md),
[determinant-scheme](spectral_determinant_schemes.md) and
[singular-boundary](spectral_pushforward_boundary.md) homes own the more
general spectral statements. They are reviewed provisional contributions,
not new canonical promotions.

This assessment also reads three fixed **local committed** branch inputs:

| Checkpoint | Owning source and evidence status |
| --- | --- |
| `28756229308313912eb5e98ab2b21c08d828f78c` | `research/supplements/ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md`: reviewed mathematical comparison and independently checked actual octic computation, with a proper residual pair |
| `563fa53652fcb1763427a69799b195f7a6d8e438` | `research/supplements/FROBENIUS_POWER_LIFTING_PRECISION.md`: reviewed conditional extraction radius and root-specialization defect for a prescribed arithmetic family |
| `7530d052c4ea198916e399de034ba4a16a7c74d2` | `research/notes/2026-10-31-unrestricted-strategy-assessment.md`, section 38: Chow and exceptional-cover selection closeout; its proposed Hom lemma explicitly lacks a separate independent proof audit |

These sources can be retrieved by `git show <checkpoint>:<path>`. They have
not been copied into this branch or promoted by this assessment. The source
checkpoints, rather than their branch names or navigation summaries, identify
the mathematics being used. Later uncommitted integration and toric-center
work remain with their owners and are not treated as accepted results here.

## 2. What this lane has learned

**The spectral condition has a constructive interpretation.** For every
\(n\ge2\), the coefficient determinant detects ruling-difference
\(n\)-torsion on the smooth root. Its kernel recovers a trivialization
and, for \(n>2\) in the stated convention, an abstract graded CI family.
The scheme account retains nonreduced parameter bases. This is useful
geometry independently of a global pair. Singular roots require the
full boundary classification: unbalanced reducible roots have determinant
kernels that do not provide the required units.

**The entire smooth order-three locus is accessible geometrically.** Four
linear forms determine the root by the minors of a two-row Hankel matrix.
The locus is an open of \(\mathbf P^7\), not merely a list of examples.
This gives a global parameter space for a new realization problem. It does
not permit arbitrary changes of ruling coordinates while keeping the actual
embedded obstruction operator fixed.

**First embedded compatibility is achievable.** The reviewed parity slice
has exactly six smooth order-three roots passing the complete first test.
At four, the actual sextic symbol space has no nonzero multiplier. At the
other two, actual symbols exist but their complete cubic lift fails. This
locates two different failures of sextic realization and preserves positive
finite-order objects between them. The completed four-parameter calculation
adds eighteen smooth first-compatible points, all failing the sextic symbol
test. Thus its entire smooth first-compatible locus consists of twenty-four
points, with twenty-two symbol failures and two cubic failures. All affine
parameter strata and base-coordinate infinity are covered for that slice.
Its projective closure is not covered, and most of the full
\(\mathbf P^7\) open lies outside it.

The useful reusable tool is the
[actual-source obstruction quotient](rank_strata_and_sextic_lifts.md).
It retains the entire equation source, every allowed correction and rank
boundaries. Another numerical obstruction count would add less information
than identifying the zero locus of that quotient's section or constructing
an equation in it.

## 3. A proved connection to actual octic equations

The octic checkpoint supplies a comparison previously missing between the
root and global-source accounts. Let \(U\subset\mathbf P^7\) be our
smooth order-three parameter space, and let \(K_1\) denote the first
embedded compatibility locus. The comparison applies on \(U\cap K_1\),
where the unique first Cartier lift \(\Sigma_1\) exists. It does not
apply to every point of \(U\) merely because its spectral class is torsion.

For a degree-\(d\) actual equation whose quadratic symbol is a multiple
of the root \(f\), its transformed section restricts to a canonical residue
\[
\rho_{d,f}:V_d(f)\longrightarrow
H^0\!\left(\Sigma,\mathcal O_\Sigma(4d-21,3)\right).          \tag{1}
\]
Vanishing means that this actual section contains \(\Sigma_1\).
The construction incorporates the equation units and full chart transition;
it does not divide by the leading multiplier at its zeros.

For octics, quotient by all corrections from the actual source
\(V_{8,3}=qV_{6,2}\). The induced map is
\[
\kappa_f:H^0(\mathbf P^1,\mathcal O(16))\longrightarrow Q_f,
\qquad \dim Q_f=6+h_f,\qquad 0\le h_f\le3,                   \tag{2}
\]
where
\[
H_f=\{\beta\in H^0(\mathcal O(8)):\beta f
          \text{ is an actual sextic quadratic symbol}\},\quad
h_f=\dim H_f.
\]
Thus every smooth first-compatible root admits **individual actual octics**
of exact normal order two that contain its first lift. Two whose multipliers
jointly generate the root require a further common-zero calculation. A large
kernel can still have a fixed divisor.

Our first-compatible roots now have an immediate positive application. For
the twenty-two points with \(h_f=0\),
\(\dim\ker\kappa_f\ge17-6=11\). For the two with \(h_f=1\),
\(\dim\ker\kappa_f\ge17-7=10\). Their sextic failures therefore
do not obstruct first-compatible individual octics. These are lower bounds,
not computed octic ranks or a basepoint-freeness theorem for our roots.

The separate octic seed in checkpoint `2875622` goes further: it has a
ten-dimensional multiplier space with no common zero and a verified proper
pair satisfying
\[
[V(F_8,G_8)]=8[C_0]+R,\qquad \deg R=32.                      \tag{3}
\]
That root has an already nonzero second obstruction. Its pair is a positive
construction of a containing intersection, not an STCI candidate. The cycle
is actual residual support downstairs, not an exceptional vertical curve.
Our parameterization and first-compatible roots supply different inputs for
the same intrinsic construction.

When the root varies, both \(h_f\) and the rank of \(\kappa_f\) may
change. Determinantal strata or an incidence retaining actual equation
coefficients are needed; (2) does not give a constant-rank bundle on all
\(U\cap K_1\).

## 4. Root extension and equation membership are separate towers

The same octic source proves a conditional statement for any degree \(d\).
If compatible Cartier root lifts \(\Sigma_j\) already exist, the next
membership test for an actual equation has target
\[
H^0\!\left(\Sigma,
  \mathcal O_\Sigma(4d-14-7j,2+j)\right),\qquad
\deg=8d-24-12j.                                               \tag{4}
\]
This is a test of an equation on a supplied root lift. It is not the
obstruction to constructing that lift.

**Conditional sextic membership lemma.** Suppose a smooth root with
\(\eta^4\ne\mathcal O\) has a first-compatible actual sextic. At
\(d=6,j=2\), (4) is
\(H^0(\Sigma,\mathcal O_\Sigma(-4,4))=H^0(\Sigma,\eta^4)\).
This group vanishes, and all later targets have negative degree and vanish.
Consequently, whenever further compatible root lifts exist, that sextic
automatically contains them. No new equation-membership condition remains
after the first one in this setting. Exact order three is an application:
\(\eta^4=\eta\ne\mathcal O\). This consolidates all smooth roots
with nontrivial fourth power rather than repeating an argument for each
torsion order.

This does not produce the sextic or the next root lift. Our covered slice
already fails the first sextic condition. Elsewhere, a successful sextic
would still leave the root obstruction tower, a mate, properness and support
to settle. The distinction explains why treating each higher coefficient as
another independent global-source search can duplicate work.

For the saturated, jointly generated, smooth full-root, full generic coprime
CI setting, [R-0013](../results/saturated_actual_generator_movement.md),
[R-0014](../results/movement_two_six_rows.md) and
[R-0006](../results/actual_ci_smooth_root_bridge.md) retain
\((r,s;a,b)=(2,12;6,16)\) for exact order three. An octic residual
construction is valuable for the broader intersection problem; it does not
replace the sextic required by this particular sole-support row.

## 5. What the other lanes change

The arithmetic checkpoint supplies a precise conditional globalization
mechanism. A sufficiently accurate **ambient** lower root, with approximation
order \(s>E/(p-1)\) on the same lifted carrier, permits power extraction.
Ramifying a fixed approximation scales both sides and does not improve that
inequality. Alternatively, the flat closure of the generic lower root has
a special-fiber sequence
\[
0\to T\to\mathcal O_{D_0}\to\mathcal O_{Z_0}\to0.
\]
Vanishing of this finite embedded-point defect produces a Cartier root and
an actual lower-degree equation. For the prescribed powered-quartic family,
quartic exclusion forces \(T\ne0\) at the two parameter endpoints. This
is a statement about that arithmetic family, not an obstruction to every
characteristic-zero spectral root. No map identifies \(T\) with our
residue quotient, the quadratic-cover conductor boundary, or R-0030's
relative comparison defect.

The Chow/exceptional-cover closeout reinforces a source requirement.
Arbitrary determinantal representations of Chow powers do not have the
required equation-bundle types. Its sharper proposed Hom identification
is unreviewed and is not used as a theorem here. Rational support and generic
ruledness likewise do not supply a smooth exceptional bundle or a bound on
all cover genera. These observations do not block new constructions through
actual sources such as (1); they explain why another equivalent determinant
or another local degeneration alone is insufficient.

More generally, the negative tests across the branches are not independent
votes for non-STCI. Some are consequences of the same budget; some exclude
only a chosen source; some diagnose a missing map. The positive results now
include graded families, embedded first lifts, actual equation spaces and
proper residual pairs. The global sole-support problem remains a stricter
question than any one of these.

There is one additional **uncommitted, unreviewed** construction lead in the
four-streams worktree. The three programs
`research/computations/quintic_toric_finite_centers.py`,
`quintic_toric_boundary_centers.py` and
`quintic_toric_exception_centers.py`, with the finite-centers JSON, report
reducing the genus-two toric quintic source's relative projection-center
problem to a remaining quartic locus \(M=0\). Generic finite centers,
the infinity boundary and three other exceptional factors are reported
excluded by full-inverse-support tests. The programs do not resolve \(M=0\)
or supply section descent. A read-only inspection found no accompanying
independent audit; the JSON names a temporary script rather than establishing
the exact execution state of these repository files. This is a useful
potentially finite continuation, not a theorem used in this synthesis.

## 6. Recommended next work, in order

1. **Construct and describe actual octic intersections from the order-three
   first-lift locus.** Start with the exact roots already available and the
   intrinsic map (2), retaining all corrections. Determine the multiplier
   spaces and their common-zero divisors; if they jointly generate, extract
   actual proper pairs and compute their generic contact and residual cycles.
   Then identify the constant-rank locus on which the construction varies.
   The endpoint is an actual family with a proved domain, or a precisely
   described fixed-divisor obstruction for the tested domain. This has
   constructive value even when residual degree stays positive. It is not
   a search for an octic STCI with exact-order-three root.

2. **For the conditional sole-support lane, replace further arbitrary slices
   with the full smooth order-three incidence.** Use the open-P7
   parameterization, impose \(K_1\), and apply the complete actual sextic
   source and cubic quotient. Retain multiplier zeros, the free \(q^3\)
   direction and every rank boundary. A useful endpoint is a nonzero actual
   compatible sextic with its next root test identified, a covered component
   calculation, or a coverage-certified exclusion of this exact smooth-root
   class. Even full exclusion here would leave singular roots, nonsaturated
   relations and other initial ideals. The first calculation should establish
   the parameter/incidence geometry and a proved cover, not assume expected
   codimensions or launch another unstructured point search.

3. **Keep an intrinsic geometry question independent of the STCI outcome.**
   Determine the determinant scheme and kernel-family behavior along a
   specified singular spectral boundary. The existing classification already
   distinguishes integral, balanced reducible, doubled and unbalanced roots;
   repeating their fiber ranks is unnecessary. A local scheme description
   including how the unit condition degenerates would be a genuine extension.
   Any passage to the actual embedded neighborhood would require a separate
   comparison, and is not part of that task's success criterion.

For the wider construction program, the toric-source owner has a separate
concrete candidate: first verify the reported reduction, then resolve the
remaining \(M=0\) center locus with the required finite-projection and
inverse-support opens retained. If a center survives, test actual section
descent there. If the locus is empty, that closes the specified toric source,
not all normalizations. This is a more focused parallel assignment than
reopening Chow representations or unconstrained exceptional-cover examples;
it does not redirect the owner's ongoing work through this assessment.

These are recommendations, not a new computation campaign initiated by this
closeout. The main allocation change is to make actual containing-pair
construction the next step, while keeping the global sextic incidence as a
distinct, clearly bounded existence-or-exclusion problem.

## Review and remaining limits

Independent review on October 31 by `review_order_three_geometry`
(GPT-6.1 Sol, high reasoning) checked the new octic kernel bounds from the
same sextic symbol space, the supplied-root restriction on the family
comparison, and the conditional sextic lemma, including its general scope
\(\eta^4\ne\mathcal O\). The review passed; it did not compute
octic ranks or multiplier base divisors. The four-parameter proof's reviewed
symbol ranks extend the same bound from the original four \(h_f=0\)
points to all twenty-two.

`constructive_strategy` independently reviewed the written cross-branch
assessment. It found no material false implication or scope error, and
confirmed the distinction between constructive octic residual pairs and the
conditional sextic sole-support row. It also checked that the unreviewed
Chow and toric leads retain their evidence limitations and that these
recommendations do not redirect other owners' queues. The mathematical
closeout of the four-parameter calculation has its separate review in the
companion proof. The recommendation to complete that already interrupted
calculation was the lead's choice; the strategic reviewer favored moving
directly from the earlier diagnostic to full-locus/source work. Its finite
completion is retained here, and no further selected slice is recommended.

The unchanged source results retain their own review status. No arithmetic
trait, new octic pair, all-root sextic elimination or singular determinant
scheme is computed by this synthesis. It gives new consequences of reviewed
inputs and research recommendations, with no canonical promotion.
