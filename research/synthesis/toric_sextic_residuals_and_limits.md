# Invariant sextic geometry: orbit closures, residual boundaries, and Hilbert limits

Fix the quartic \(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed
field \(k\) and the torus of integer weights \((0,1,3,4)\). On the dense
coordinate torus write \(x=(1,t,t^3u,t^4v)\), with \(t,u,v\) units.

This chapter keeps the sextic source-space and pencil calculations used
to study supported Hilbert loci. The proofs for proper sextic intersections
and their full torus limits are in
[A-0002](../arguments/torus_sextic_residuals.md). The
[embedded quotient argument](../arguments/torus_embedded_quotients.md)
owns the constant-family image and endpoint calculations.

## Proofs of orbit multiplicities and full limits

<a id="1-orbit-families-and-the-residual-boundary"></a>
<a id="5-the-geometry-of-invariant-curve-strata"></a>

- [Orbit curves and finite quotient degree](../arguments/torus_sextic_residuals.md#orbit-curves-and-finite-quotient-degree)
  gives the degree of an orbit closure and the degree accounted for by the
  dense-torus quotient.

<a id="11-eight-quotient-points-and-a-quadruple-residual-line"></a>
<a id="12-six-quotient-points-and-a-twelvefold-residual-line"></a>
<a id="13-a-noncurvilinear-quotient-of-the-same-length"></a>

- [Eigenpair residual controls](../arguments/torus_sextic_residuals.md#eigenpair-residual-controls)
  keeps the length-eight and both length-six examples with their local
  multiplicities and characteristic-dependent quotient algebras.

<a id="2-fixed-point-incidence-forces-residual-boundary-for-eigenpairs"></a>

- [The sharp sextic eigenpair bound](../arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound)
  concerns actual proper sextic eigenpairs and holds in every characteristic.

<a id="3-residual-curves-move-before-they-acquire-boundary-support"></a>
<a id="31-specializing-divisors-not-attracting-individual-points"></a>

- [Moving residual curves and their full limit](../arguments/torus_sextic_residuals.md#moving-residual-curves-and-their-full-limit)
  gives the divisor limits and residual cycle.

<a id="32-absorption-changes-the-decomposition-into-marked-and-residual-cycles"></a>

- [Residual absorption](../arguments/torus_sextic_residuals.md#residual-absorption-in-a-proper-flat-family)
  gives the explicit transfer of multiplicity onto the marked curve.

<a id="4-the-hilbert-scheme-limit-remembers-relations-between-equations"></a>
<a id="41-how-the-boundary-cycle-changes-in-the-full-limit"></a>

- [The saturated three-generator full limit](../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit)
  keeps the extra generator, Hilbert series, and
  [boundary cycle and endpoint schemes](../arguments/torus_sextic_residuals.md#cycles-and-endpoint-schemes-of-the-three-generator-limit).

## 6. From invariant examples to the supported-CI Hilbert locus

The [full supported Hilbert boundaries](../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits)
preserve the Hilbert polynomial and sole reduced support \(C\). The moving
ideals still have to pass the
[generator test](../arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test).
Actual sextic source spaces and conormal restrictions are inputs to that
test. The residual examples in A-0002 illustrate the behavior of full limits
outside the sole-supported locus. The characteristic-zero STCI question
remains open.

First, the full degree-six polynomial source consists of the 84 ambient
monomials. In the torus coordinates above write each such monomial as
\(t^w u^i v^j\), with constant coefficient \(c_{w,i,j}\). Vanishing
to order at least two along \(C\) is equivalent, separately in every
integer weight, to
\[
 \sum_{i,j}c_{w,i,j}=0,\qquad
 \sum_{i,j}i c_{w,i,j}=0,\qquad
 \sum_{i,j}j c_{w,i,j}=0.                            \tag{35}
\]
These are the value and two first normal coefficient conditions at
\((u,v)=(1,1)\). They define a global sheaf-power condition: the first
infinitesimal neighborhood has a filtration with locally free quotients
on \(C\), so a section vanishing on its dense open vanishes everywhere.
No endpoint torsion is discarded.
The weight dimensions in weights six through eighteen are
\[
 (1,1,2,2,2,2,3,2,2,2,2,1,1),
\]
with total 23. This is an explicit coefficient presentation of the
already reviewed characteristic-free source
\(H^0(\mathcal I_C^2(6))\), not a new ambient classification; its
full proof and higher-degree formulas are owned by
[actual homogeneous equation spaces](../supplements/ACTUAL_EQUATION_SPACES.md).
The [exact verifier](../investigations/torus-residual-controls/verify.py)
supplies a finite implementation check of (35).

Set \(q=x_0x_3-x_1x_2\), \(A=x_0^2x_2-x_1^3\),
\(B_3=x_0x_2^2-x_1^2x_3\), and \(D_3=x_2^3-x_1x_3^2\).
In the dense torus chart these become
\[
 q=t^4(v-u),\quad A=t^3(u-1),\quad
 B_3=t^6(u^2-v),\quad D_3=t^9(u^3-v^2).
\]
On \(Q=V(q)\), where \(v=u\), every degree-six double section restricts
in this chart to
\[
 t^6(u-1)^2R(t^3u),\qquad \deg R\le4.                \tag{36}
\]
In Segre coordinates \(x=(ac,ad,bc,bd)\), the equation of \(C\) on \(Q\)
is \(D=bc^3-ad^3\). The displayed restriction is \(D^2\) times a section
of \(\mathcal O_Q(4,0)\). It links quotient coefficients to a global
quadric linear system; it does not make higher embedded lifts automatic.
The [actual-source rank and unique-lift account](rank_strata_and_sextic_lifts.md)
retains the additional cubic matching conditions and its own reviewed
characteristic-zero hypotheses.

Second, the existing [sole-support sextic reduction](../supplements/SEXTIC_PAIR_REDUCTION.md)
is independently reviewed evidence in characteristic zero or
\(p\ge7\). For **every** proper \((6,6)\) pair with reduced support
\(C\), its proof obtains generic curvilinear length nine and the full
necessary divisor profiles. Neither statement is reproved here or
inferred from a constant quotient algebra. The
[noncurvilinear length-six example](../arguments/torus_sextic_residuals.md#eigenpair-residual-controls)
has residual support. The sole-support reduction uses the global quadric
restriction, the balanced-normal-bundle graph bound and actual saturated
duality.

The [endpoint Smith orders](../arguments/torus_embedded_quotients.md#embedded-quotients-and-characteristic-dependent-endpoints)
three and four are characteristic free. They do not determine the conormal splitting:
[R-0020](../results/quartic_conormal_characteristic_jump.md) proves the
actual characteristic-two jump from \(\mathcal O(-7)^2\) to
\(\mathcal O(-8)\oplus\mathcal O(-6)\) through its extension class.
Endpoint lattice orders, quotient lengths, full projective ideals and
conormal extension classes retain different information. No comparison
proved here identifies them or excludes all mixed sextic pairs.

## 7. Parameter spaces: pencils, fixed loci, and deformation strata

A Grassmannian of equation pencils and a Hilbert scheme of their
intersection schemes answer different geometric questions. The former
retains a chosen two-dimensional space of equations; the latter
retains the full ideal through degeneration. The dimension counts
below locate specific linear conditions on pencils, but do not
compute codimensions of arbitrary Hilbert-scheme boundary strata
or of all increased-multiplicity loci.

For equal degrees the symmetric space of pencils is
\(\operatorname{Gr}(2,H^0(\mathcal I_C(d)))\). Since the embedded quartic
has Hilbert function \(4d+1\) for \(d\ge2\),
\[
 h^0(\mathcal I_C(4))=18,\qquad h^0(\mathcal I_C(6))=59.
\]
The two Grassmannians therefore have dimensions 32 and 114, respectively.
The 23-dimensional double-sextic source cuts out the closed sub-Grassmannian
\(\operatorname{Gr}(2,23)\), of dimension 42 and codimension 72 in
\(\operatorname{Gr}(2,59)\). This is exactly the condition that the entire
pencil consists of double sextics. It is not a computation of the
codimension of every locus with increased generic multiplicity along \(C\):
dependence of first normal symbols over \(k(C)\) need not come from a
constant linear combination of the two equations.

The existing [quartic root pencil](root_pencil_geometry.md#3-three-ways-the-pencil-leaves-the-open-arrangement)
has polynomial \(z^4-\eta z+\eta-1\) and discriminant
\[
 (\eta-4)^2(-27\eta^2+40\eta-16)
\]
in characteristic zero. Its marked-root collision, residual-root collision,
root escaping the quotient torus at \(\eta=1\), and boundary at
\(\eta=\infty\) are different codimension-one events in that parameter line.
The root at zero is separable, so the discriminant does not detect that
embedded boundary. These slice calculations give no ambient classification
or codimension of general conductor, quotient-type or residual strata.

The [source review](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md#L625-L631)
records the scope of the original residual and full-limit checks. The
inherited source-space, sole-support reduction and conormal results retain
their linked proof and review scopes.
