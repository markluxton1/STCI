# Actual sextic search: maximal contact can force the wrong residual scheme

Started October 28; computations completed October 29, 2026. Status: new
fixed-input exact rank certificates and deductions, independently checked
at representative inputs in the [audit](2026-10-28-stci-search-experiments-audit.md).
Provisional research, with no canonical promotion or unrestricted STCI claim.

## Search question and inputs

For the fixed characteristic-zero curve
\(C=[s^4:s^3t:st^3:t^4]\), seek actual global homogeneous equations
\((F_6,G_{16})\) with reduced intersection support \(C\). Their full
intersection has degree 96, so sole support requires generic transverse
length \(m_C=24\). We start with proper intersections and retain their
residual cycle:

\[
[V(F_6,G_{16})]=m_C[C]+R,\qquad \deg R=96-4m_C.
\]

The [actual sextic construction](2026-10-25-endpoint4-actual-sextics.md)
provides global equations on a retained nodal endpoint-four chart. We use
the rational modulus \(\rho=-1\), but vary parameters that the completed
[R-0025 certificate](../results/ci_fixed_sextic_jet_rigidity.md) did not test.
Put

\[
q=x_0x_3-x_1x_2,\quad D=x_2^3-x_1x_3^2,
\]

\[
F_{t,\kappa}=-q^2x_3^2-qDx_2-tqDx_3+D^2/4+\kappa q^3.
\]

These are actual homogeneous sextics with constant coefficients, rather
than proposed function-field symbols. The seven newly tested inputs are

\[
(t,\kappa)=(0,0),(1,0),(1,1),(1,-1),(2,0),(2,1),(0,-1).
\]

The previously certified point \((0,1)\) was deliberately not replayed.
The old certificate and source family are inherited inputs; all ranks in
the table below are new calculations. The numerical row \((6,16)\) is
motivated by [R-0014](../results/movement_two_six_rows.md) under its stated
hypotheses. The fixed-carrier deductions below apply to every proper
degree-16 mate of each displayed sextic and do not assume that numerical
row's filtration or saturation hypotheses.

## A concrete candidate and its exact failure

For every member of this family, take the actual mate

\[
G_{16}=q^8.
\]

The pair is proper: \(q\) is irreducible and
\(F_{t,\kappa}\bmod q=D^2/4\ne0\), so \(\gcd(F_{t,\kappa},q)=1\).
The residual is completely visible. On the smooth quadric \(Q=V(q)\), use
Segre coordinates

\[
[x_0:x_1:x_2:x_3]=[ac:ad:bc:bd].
\]

Then

\[
D=b^2(bc^3-ad^3),\qquad
\operatorname{div}_Q(D)=2L_0+C,
\quad L_0=V(x_2,x_3).
\]

Consequently

\[
\boxed{[V(F_{t,\kappa},q^8)]=16[C]+32[L_0].}
\]

This candidate puts two thirds of the complete-intersection degree on
\(C\), but its remaining degree is a line with multiplicity 32. Increasing
the exponent of the quadric preserves that residual proportion. The search
test is whether a degree-16 perturbation can retain or improve the contact
with \(C\) while removing that residual.

## Exact score for all mates of each selected carrier

Use the actual balanced normal chart

\[
(x_0,x_1,x_2,x_3)
=(1,z,z^3+v,z^4+u+3zv/2).
\]

The quadratic normal term of \(F_{t,\kappa}\) is \(z^8f_t\), where

\[
f_t=(1+2tz+z^2)u^2+tz^2uv-z^2v^2/4.
\]

Its discriminant has square class

\[
P_t(z)=1+2tz+(1+t^2)z^2,\qquad
\operatorname{disc}_z(P_t)=-4.
\]

Thus it is nonsquare in \(k(z)\) over any algebraically closed
characteristic-zero constant field. If \(1+t^2=0\), the polynomial is
linear with a simple zero and the same conclusion holds. This fact is
independent of \(\kappa\).

The completed carrier has two conjugate smooth transverse branches over
the quadratic extension of \(k(z)\). A global mate has the same finite
order \(n\) on both branches, so

\[
m_C=2n,\qquad
G\in(F_{t,\kappa})+(u,v)^n.
\]

For the membership assertion, prepare \(F\) as a monic quadratic in \(u\)
and write the mate's remainder as \(a(v)u+b(v)\). Restricting to the two
branches and subtracting shows \(\operatorname{ord}_v a\ge n-1\), then
\(\operatorname{ord}_v b\ge n\). Hence the remainder has normal degree
at least \(n\). Properness ensures finite intersection length. This is the
same local lemma used in R-0025; its hypotheses are verified here for the
new inputs.

Let

\[
\mathcal K_j(F)=
\{G\in H^0(\mathbf P^3,\mathcal O(16)):
G\in(F)+(u,v)^j\text{ over }k(z)[[u,v]]\}.
\]

The source has dimension 969. The 286 independent global multiples
\(F H^0(\mathcal O(10))\) always lie in \(\mathcal K_j\). At cutoff eight,
\(q^8\) supplies one further direction, independent of the multiples.

The script evaluates actual degree-16 source monomials in the truncated
normal quotient at 80 good base points modulo 65521. It checks all 286
actual multiples at every point. The table gives modular ranks, which are
lower bounds on the characteristic-zero ranks.

| Selected \((t,\kappa)\) | Rank at cutoff 8 | Rank at cutoff 9 | Rank at cutoff 10 | Consequence for every proper \(G_{16}\) |
|---|---:|---:|---:|---|
| \((0,0),(1,0),(2,0)\) | 642 | 672 | 683 | \(m_C\le18\), \(\deg R\ge24\) |
| \((1,1),(1,-1),(2,1),(0,-1)\) | 682 | 683 | 683 | Exact maximum \(m_C=16\), sharp minimum \(\deg R=32\) |

All seven have rank 683 at cutoffs eleven and twelve as well. These are
certificates about all degree-16 global mates of the selected inputs,
rather than seven proposed mates or random local coefficients.

For the four displayed nonzero-\(\kappa\) inputs the rank at cutoff eight
is already as large as possible, because the known 287-dimensional space
of multiples plus \(q^8\) is in its kernel. Therefore

\[
\boxed{\mathcal K_8(F)=F H^0(\mathcal O(10))\oplus kq^8,\qquad
\mathcal K_9(F)=F H^0(\mathcal O(10)).}
\]

It follows that \(m_C\le16\), with equality attained by the concrete pair
above. More strongly, every proper mate attaining this maximal contact is
\(G=FH+cq^8\), \(c\ne0\), and consequently

\[
\boxed{(F,G)=(F,q^8).}
\]

Thus the entire full complete-intersection scheme is rigid at maximal
contact for these inputs. A perturbation preserving maximal contact cannot
remove the residual line; it only changes the presentation of the same
ideal. This explains their failure more precisely than saying that an
obstruction matrix has large rank.

At the three selected \(\kappa=0\) inputs, the ranks only give upper bounds
41 and 11 on proper source directions at cutoffs eight and nine. They do
not prove that any of these extra characteristic-zero directions exist.
The cutoff-ten kernel equality is decisive, so \(m_C\le18\), but attainment
of 18 and a sharp residual bound have not been established.

## Why finite-field rank proves a characteristic-zero failure here

The leading \(u^2\) coefficient is
\(z^8(1+2tz+z^2)\). Every sampled point makes it a unit modulo 65521.
Recursive normal division has denominators generated by this coefficient
and 2. It therefore defines a rational remainder matrix with good
specialization at the chosen prime. A nonzero modular minor is a nonzero
characteristic-zero minor. Conversely the known global multiples, and at
cutoff eight the explicit \(q^8\), give characteristic-zero kernel lower
bounds. Matching these bounds proves the displayed kernel equalities and
their persistence under constant-field extension.

The order-12 remainder basis is
\(1,v,\ldots,v^{11},u,uv,\ldots,uv^{10}\). Lower cutoff matrices are
obtained by retaining rows of smaller normal degree: division by the
carrier never lowers total normal degree, so this restriction commutes
with truncation. The independent M2 implementation instead forms the
truncated quotient directly.

An early 40-point trial had cutoff-eight rank 600, exactly its row count,
and nonzero-\(\kappa\) cutoff-nine rank 680, again the row count. Those
values did not measure actual freedom. Expanding to 80 points resolved
this sampling limitation and gave the sharp statements above. No
characteristic-zero candidate was inferred from a modular kernel.

## How this changes the search

1. These seven carriers cannot have a degree-16 STCI mate. At four of them
   the best possible contact is attained by a completely explicit pair,
   and every best-contact perturbation retains exactly its wrong residual
   scheme. We should not spend another run optimizing mates at those inputs.
2. The relevant next search is a rank-drop locus in the actual carrier
   parameter space. The present certificates show a nonempty open set
   where \(\mathcal K_9=F H^0(\mathcal O(10))\), and any survivor in that
   neighborhood must lie on the closed determinantal exceptional locus.
   They do not compute or exclude that locus. A fixed nonzero minor can
   become a polynomial filter for subsequent candidate generation.
3. The selected \(\kappa=0\) boundary retains a larger possible source, but
   it still loses every proper mate two normal orders before the required
   cutoff twelve. Its cutoff-nine kernel should be computed over the
   rationals before treating the apparent extra directions as candidates.
   Specializing toward a boundary only helps if the actual global mate
   space gains enough contact to reach the required length.
4. The general characteristic-zero STCI question and other degree pairs
   remain open. The modulus \(\rho=-1\), other endpoint charts, other roots
   of unity, singular roots outside this family, and other carrier models
   have not been exhausted. A generic-open failure does not eliminate a
   special-locus construction.

For a geometric explanation of the \(\kappa=0\) boundary, introduce the
rational degree-one variable \(W=D/(2q)\). The carrier is the projection of
the equations

\[
D=2qW,\qquad
W^2-2(x_2+tx_3)W-x_3^2+\kappa q=0
\]

in \(\mathbf P^4\). The latter quadric has rank three when \(\kappa=0\)
and rank five when \(\kappa\ne0\). This is a genuine geometric change in
the auxiliary model. Identifying its sections with the additional
cutoff-nine mate directions is a possible explanation, not a proved
identification or a classification of the normalization.

## Evidence and reproduction

- [New parameterized Python engine](../computations/stci_search_sextic_jets_2026_10_28.py)
  and [seven-input JSON](../computations/stci_search_sextic_jets_2026_10_28.json).
  The JSON retains parameters, actual ambient sextics modulo the prime,
  good sample points, cutoff ranks, all-multiple checks and matrix hashes.
- [Independent audit and its M2 evidence](2026-10-28-stci-search-experiments-audit.md).
- Inherited construction and hypotheses:
  [actual sextic family](2026-10-25-endpoint4-actual-sextics.md),
  [R-0014](../results/movement_two_six_rows.md), and
  [R-0025](../results/ci_fixed_sextic_jet_rigidity.md).
- Arithmetic comparison uses the separately reviewed
  [positive-characteristic construction interface](2026-10-27-positive-characteristic-construction-interface.md)
  as a premise. Its known Frobenius controls were not replayed here.

Run:

```text
python3 research/computations/stci_search_sextic_jets_2026_10_28.py
```

The script uses Python's standard library and an available C++17 compiler.
It imports arithmetic and elimination routines from the independently
reviewed October 26 script, without running that script's carrier test.
The new JSON records hashes of both sources. The independent M2 check
uses different quotient coordinates. No canonical mathematical file is
changed by this experiment.
