# Geometric closeout review: the objects, the gates, and the remaining implications

October 31, 2026. Independent reviewer: `geometric_review`, separate from
the obstruction, existence and projection audit lanes. **Status: reviewed
provisional geometric interpretation; no canonical promotion.** The curve
throughout is
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), with \(k\)
algebraically closed of characteristic zero. The unrestricted STCI
question remains open.

This review reads the source arguments as geometry, challenges the scope
bridges between them, and uses already reviewed results as premises. It
does not rerun inherited proofs or large computations. It is a bounded
closeout, not a proposal for another search cycle.

## 1. Inputs and authority

Promoted premises used here are the [quartic-carrier and factor
boundary](../results/quartic_carrier_exclusion.md), the [fixed-carrier
conductor criterion](../results/fixed_carrier_conductor_criterion.md),
and the exact limitations of the [smooth movement-two formal-root
theorem](../results/smooth_root_formal_obstruction.md) and its
[actual-CI bridge](../results/actual_ci_smooth_root_bridge.md). Their
inherited proofs are not reopened. In particular both defining degrees
of a hypothetical characteristic-zero presentation are at least five;
the general higher-degree problem is not closed.

The October 30 obstruction and existence arguments are provisional source
notes. The prior [geometric review](2026-10-30-stci-game-geometry-review.md)
independently checked the critical-degree ordinary-root case, the deck
action and coplanarity interpretation. Its Section 6 explicitly left the
all-degree extension for a further audit. The closeout
[obstruction audit](2026-10-31-stci-closeout-obstruction-audit.md),
[existence audit](2026-10-31-stci-closeout-existence-audit.md), and
[projection audit](2026-10-31-stci-closeout-projection-audit.md)
record the final claim-level verdicts; their evidence, rather than the
date or prominence of a source note, determines completion status.

## 2. The strongest geometric mechanisms, with literal coverage

| Mechanism and actual objects | What is measured and why it obstructs | Exact scope and remaining implication |
| --- | --- | --- |
| The quadric flag \(C\subset Q\subset\mathbf P^3\) | Restriction of an actual order-\(m\), degree-\(a\) equation to \(Q\) is \(mC+T\), with \([T]=(a-m,a-3m)\). A negative second ruling degree forces a quadric factor; above that boundary, \(T\) is an actual curve on the carrier. | The sheaf-power source is \(H^0(\mathcal I_C^m(a))\). It is not a classification of a pair's higher contact. |
| The ordinary horizontal normal cover \(\Gamma\to C\), its normalization surface, and the actual quadric residual \(T\) | A sole-support mate pulls back to \(r\Gamma\). The hyperplane degree requires \(ab=4mr\); simple actual attachments to \(T\) require \(b(2a-4m)=r(4a-6m)\). These would make the inverse curve proportional to the hyperplane polarization despite incompatible intersection data. | **PASS** in the [all-degree audit](2026-10-31-stci-closeout-obstruction-audit.md), for every \(a\ge3m\), every positive mate degree, and a nonempty dense open of each full actual source. The full first root is horizontal, reduced and irreducible; \(T\) and every used attachment are reduced/transverse/regular as in the source. This is never an all-carrier exclusion. |
| Reducible ordinary horizontal roots \(\Gamma_j\) | The same two actual degree equations weight the branch multiplicities \(r_j\). They force \(\sum d_jr_j/\sum e_jr_j=7-16m/a\), where \(e_j\) is cover degree and \(d_j\) direction degree. | The absence of vertical parts and ordinary attachment hypotheses remain essential. The required low-slope component is a necessary condition; it is not evidence that such a component descends to an actual supported pair. |
| Fixed global cubic \(H_3\), its residual rulings \(R_{H_3}\), and higher-order lifting fibers | In the reviewed common-cubic family, all corrections vanish on \(Q\), so the actual scheme \(V(q,H_3^m)\) remains inside every proper pair and retains \(mR_{H_3}\). | The [reviewed fixed-boundary theorem](2026-10-30-stci-game-quadric-boundary.md) covers its literal family in every mate degree. The large lifting dimension does not move a restriction on which the whole lifting kernel vanishes. No conclusion about all higher-order corrections in all degree margins is implied. |
| Actual test lines in the weighted subalgebra | Lines on the carrier attach to inverse branches; restriction of the hypothetical mate to each line gives additional divisor-degree equations. | The [reviewed theorem](2026-10-30-weighted-subalgebra-line-obstruction.md) is uniform in degree but retains its squarefree, axis-free binary boundary. Repeated or axis roots change the actual attachments. |
| The elliptic marked curve \(\Gamma\subset S_\mu\) and its degree-two map to \(C\) | \(\Gamma\sim H\) on the smooth quadric source, so \(b\Gamma\sim bH\) is numerically and linearly possible upstairs. The order-four torsion data supplies four actual global quadratic coordinate sections. | This is the [literal five-parameter family](2026-10-30-stci-game-existence.md), not an exhaustion of all elliptic inverse curves. Its inverse map has degree two, so the old degree-one classification and symmetry exclusion do not automatically apply. |
| Extra inverse scheme of the fixed elliptic member | The length-24 affine \(Q_0=1\) scheme is a free degree-two cover of a projective length-12 scheme off \(\Gamma\). A nonzero Cartier zero divisor on a smooth source cannot have these isolated points as extra support. | This rejects that fixed image in every positive mate degree. It does not exclude the five-parameter family, does not assert twelve distinct reduced points, and does not depend on birationality. |
| The full first-normal divisor of that degree-eight image | Class \((18,2)\) splits into a degree-12 vertical divisor and an integral horizontal root of class \((6,2)\). Its elliptic normalization has genus one while its arithmetic genus is five. | This is defective first-normal data, outside the ordinary full horizontal-root locus. Pullback vanishing of the vertical polynomial on the extra scheme detects containment; it does not identify schemes or multiplicities. |
| The primitive elliptic target \(C'\subset Q\), normalized by \(D\) | Its discriminant measures ramification of the degree-two target ruling, not ramification of the original surface map. Its four marked contacts and degree-twenty cover consume the Riemann--Hurwitz budget. | Target incidence alone does not construct the marked source embedding, four global sections, or descent. Genus one and four target support points alone do not give exactly four points on the normalization. |
| Coplanar marked four-point divisors on \(C\) | A binary support quartic has zero \(s^2t^2\) coefficient exactly when the four marked images lie in one plane. The actual source Picard identities and degree-two interpolation then force its two source ruling pencils to coincide. | The [reviewed extension theorem](2026-10-30-projection-elliptic-target-incidence.md) excludes that entire order-two support stratum, for every contact distribution. It preserves the genuine elliptic target example and identifies its failure as source extension. |

For the ordinary irreducible-root obstruction the positive expression is
\[
2a^2-7am+8m^2
=2(a-7m/4)^2+15m^2/8>0.
\]
Its force comes from two intersections on actual curves, rather than
from the polynomial in isolation. If the normalization is regular along
the whole inverse curve, this is the nonzero determinant of the
intersection matrix for \(H,\Gamma\). The residual-curve argument needs
regularity only at the attachments it uses and therefore should not be
silently narrowed to globally smooth normalization.

At a generic-cover stage alone, isolated inverse points over special
points of \(C\) cannot be discarded. Under a hypothetical mate they are
already impossible by the Cartier support argument. The absence of such
points must come from the full source geometry or the support test,
rather than merely from the degree of the generic tangent cover.

## 3. Why the elliptic construction is a real boundary test

The fixed elliptic example is not a counterexample to the ordinary-root
obstruction. At \((a,m)=(8,2)\), the required component slope is
\(7-16m/a=3\). Its horizontal data give \(d/e=6/2=3\), while the
missing coefficient degree is carried by the vertical degree-12 part.
Deleting that part when comparing slopes would compare different
geometric objects. The full first-normal divisor is the relevant object
for the ordinary-root hypotheses.

Likewise a smooth elliptic normalization is not a smooth full root of
movement two. The root here has class \((6,2)\) and total delta invariant
four, before the vertical divisor is restored. The promoted formal-root
theorem [R-0005](../results/smooth_root_formal_obstruction.md) cannot be
applied by genus alone; [R-0006](../results/actual_ci_smooth_root_bridge.md)
also asks for saturation, global joint generation, the full initial
ideal and its gap. None follows from a normalization curve or a torsion
identity.

The deck involution is genuine on the elliptic curve and extends linearly
to its embedding projective space. Its action on the ambient quadric
pencil is \(\mu\mapsto-1/\mu\), so it preserves only \(\mu=\pm i\).
It does not preserve the tested smooth quadric \(S_2\). Thus one must
check the actual surface map's generic degree, as the fixed-member image
calculation does. An involution on a marked curve does not on its own
factor the map of every containing source surface.

The vertical polynomial's pullback vanishing on the entire extra inverse
scheme is useful boundary detection. A missing geometric question remains:
what are the local normalization and conductor modules at each image of
that scheme, and with what lengths do they contribute to the first-symbol
coefficient divisor? Equality of total degree twelve does not answer it.
In particular vertical exceptional fibers may contract to points on
\(C\); they are not thereby residual curves downstairs.

The strongest construction still justified is the full actual
five-parameter lift of this elliptic degree-two inverse, followed first
by absorption of all extra inverse support and then by descent. Raising
the mate degree on the fixed rejected member cannot help. The
degree-five filter may be used only after verifying irreducibility of
the actual quadratic first normal form on the parameter stratum in
question; it does not discard degenerate-leading strata.

## 4. Four logically distinct gates in a projection construction

1. **Target incidence.** Construct the integral curve \(C'\subset Q\),
   its normalization, and the exact four marked normalized preimages of
   \(C'\cap C\), with contact multiplicities. The palindromic elliptic
   example passes this gate.
2. **Actual source extension.** Realize that marked curve inside the
   required smooth source with its two ruling pencils and extend to four
   global coordinate sections with the prescribed restriction. The
   coplanar-support example fails here. The Picard equality
   \(L^2\simeq\mathcal O_D(Z)\) is not equality of \(Z\) with the actual
   ramification divisor of \(A\).
3. **Full inverse support and finite birationality.** Check basepoints,
   the degree of the actual surface map, and the entire scheme inverse
   of \(C\). Isolated extra support is already fatal, even if all generic
   branch and divisor computations pass.
4. **Conductor descent.** Prove actual coordinate-ring membership of a
   pure power of the marked inverse equation. In the two concrete sources
   the identities are respectively
   \(\Delta^{2b}\in\langle U^\alpha:|\alpha|=b\rangle\) and
   \(Q_0^b\in\langle U^\alpha:|\alpha|=b\rangle\).
   These are exact global section identities. The nilpotent conductor
   gluing is not replaced by a line-bundle equality or reduced residue
   computation.

An actual pure-power identity on a basepoint-free source is stronger than
the separate support test: it excludes any extra inverse point over
\(C\), since its left side is nonzero there and every monomial expression
of an ambient mate must vanish. In a search, screening support first is
an efficient necessary test, not a further hypothesis of that implication.

## 5. Ranked unresolved interfaces already present in this package

These are continuation specifications for existing questions, not new
directions launched by the closeout. The coefficient rings, saturations,
excluded boundaries and completed outputs are given in the corresponding
claim-level closeout audits.

1. **Full inverse support in the actual five-parameter elliptic lift.**
   Over \(\mathbf Q(i)[\mu,\rho_0,\rho_1,\rho_3,\rho_4]\), the first
   unresolved condition is the fiberwise unit-ideal condition
   \[
   (Q_1+\mu Q_0,\ Q_0-1,\ I_C(U))=(1).
   \]
   Retain smoothness, basepoint freedom and birationality, rather than
   assuming they survive a support-absorbing specialization. If a stratum
   survives, the next equation is the pure-power membership
   \(Q_0^b\in\langle U^\alpha\rangle\). The required implication is from
   special vertical boundary data to an actual finite map with no extra
   inverse support, then to a descending equation.
2. **Primitive elliptic target with noncoplanar marking and actual
   extension.** For every four-part partition \(\sum n_i=20\), set
   \(P(t)=\prod(t-t_i)^{n_i}\), regroup uniquely as
   \(e_0(t^3)+te_1(t^3)+t^2e_2(t^3)\), and require the discriminant's
   normalized double cover to have genus one and exactly four marked
   preimages. Then impose the two actual source degree-two pencils,
   \(L^2=\mathcal O_D(Z)\), \(M=L^3\), and the four coordinate-section
   extension. The completed degree-ten chart is a finite target exclusion;
   the degree-twelve chart and other contact distributions remain separate.
3. **Order-one marked projection locus.** In the existing complete
   sixteen-parameter \((2,2)\) source, impose determinant order exactly
   one and compute the saturated full-inverse ideal away from the
   diagonal on each retained boundary chart. The first missing implication
   is an actual admissible source stratum; a formal coefficient count or
   target curve does not supply it.
4. **The special complement to ordinary horizontal-root exclusions.**
   Any universal exclusion must control vertical/repeated root structure,
   low-slope horizontal components, or nonordinary attachments in actual
   global pairs. The next geometric implication is an accurate replacement
   for \(b\deg T=\sum r_j(\widetilde T\cdot\Gamma_j)\) including the
   local defects, not an assumed identification of those defects with
   residual degree. The present dense-open result does not settle that
   replacement.
5. **Descent after an admissible source exists.** Compute the actual
   coordinate-ring/pure-power identity or the full-conductor descent
   lattice for a surviving member. A target incidence, a large space of
   sections, or a compatible formal model alone leaves this last gate
   unresolved. There is no admissible member in this package for which
   this remaining computation has produced a characteristic-zero STCI.

The non-existence program therefore has a broad independent result to
retain—the actual-residual test on its ordinary locus—and a precise
universal gap. The existence program has an actual higher-degree inverse
model, a diagnosed fixed-member failure, and a literal remaining support
equation. Neither program is reduced to waiting for the other's next
example. Neither has a proof resolving all homogeneous pairs.

## 6. Review limits and computation status

No new large algebra computation was launched by this geometry lane, and
no inherited accepted proof was rerun. The review does not infer finished
classification from source prose; the projection lane checks the saved
resultant/number-field final marker and preserves the stopped
degree-twelve chart. Mathematical status is claim-level: reviewed
provisional, exact reduction with unfinished execution, or explicit open
interface. No canonical result or question record is modified here.

The final obstruction audit was cross-read: its residual restriction
surjectivity is the actual cubic-product construction, while its symbol
argument uses basepoint freedom, universal incidence in characteristic
zero and connectedness, without assuming surjectivity onto all abstract
symbols. Its local graph proves the precise attachment order used in
the degree equations. This review agrees with its scoped PASS.

The final existence continuation was also cross-read. Its smooth-source
factor \(\mu(\mu^2-1)\), specialized basepoint saturation, fiberwise
\(Q_0=1\) unit ideal and all-rank-strata descent matrices describe the
actual source. The degree-\(2b\) quotient basis with \(Z_2\)-exponent
at most one has \((2b+1)^2\) elements, giving the stated degree-six
and degree-eight matrix sizes. None of those matrices has been
universally executed; the first unresolved support-unit locus is
preserved as open.

The new [small palindromic control output](../computations/stci_closeout_palindromic_independent_2026_10_31.txt)
was inspected and ends with
`PALINDROMIC_TARGET_CLOSEOUT_CONTROL_COMPLETE`, followed by
`EXIT_CODE=0`. Its geometric meaning remains the target-incidence gate
above; the explicit example still fails marked source extension.

The final projection audit was then cross-read. **PASS for its reported
geometric implications and chart scopes.** The independently reconstructed
degree-ten chart excludes elliptic normalization: a squarefree degree-ten
discriminant gives genus four, while its retained exceptional parameters
have eight odd branch points and genus three. Odd affine discriminant
degrees are incompatible with the inherited unramified first-ruling
endpoints. This closes exactly the balanced nonzero-middle degree-ten
target chart; the stopped degree-twelve remainder ideal does not acquire
a completion verdict from it. Requiring its quotient quartic to be
separable and avoid the endpoints, primitive actual bidegree, normalized
boundary divisors and exactly four normalized inverse points correctly
keeps discriminant factorization from becoming a false existence claim.

The continuation specifications also retain the actual source. The
order-one condition is a union of seven principal coefficient opens,
rather than the smaller open obtained by inverting their product.
Setting the degree-one source diagonal equation to one covers its entire
projective complement, so the displayed off-diagonal inverse ideal has
no missing projective chart. Its fiberwise unit condition also rejects
basepoints, while finite birationality and pure-power descent remain
separate gates. The general-contact target specification retains each
contact distribution, binary square-factor-at-infinity charts and actual
normalization counts. No degree-ten exclusion is transferred to a
different contact distribution or to the elliptic double-lift source.

Finally, the consolidated closeout report and current game/search
closeout passages were cross-read against all three final claim audits.
**PASS for faithful consolidation of scope and geometric meaning.**
They preserve the dense-open/all-carrier distinction, the full-root
ordinary hypotheses, containment without image-scheme equality, the
fixed-member/full-family distinction, and the completed degree-ten versus
stopped degree-twelve endpoints. The first unresolved conditions remain
actual fiberwise support ideals and source-extension equations, followed
by descent; no finite reduction is reported as an executed endpoint.
No mathematical correction to those consolidation passages was required.
