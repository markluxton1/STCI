---
id: STCI-R-0025
title: "Fixed sextic jet rigidity and residual-degree obstruction"
kind: theorem
scope:
  characteristic: "0"
  curve: "fixed C0"
  hypotheses:
    - "The selected sextic Fstar and proper degree-sixteen mates"
statement: "For the selected Fstar, the degree-sixteen order-twelve jet kernel is Fstar times degree-ten forms; every proper degree-sixteen mate has generic multiplicity at most 22 and residual cycle degree at least eight."
dependencies: []
evidence:
  - "research/results/ci_fixed_sextic_jet_rigidity.md"
  - "research/computations/endpoint4_fixed_m2_2026_10_25.m2"
  - "research/computations/endpoint4_fixed_m2_2026_10_25.json"
  - "research/computations/endpoint4_fixed_jet_independent_2026_10_26.py"
  - "research/computations/endpoint4_fixed_jet_independent_2026_10_26.json"
independent_audits:
  - "research/results/ci_fixed_sextic_jet_rigidity.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Only one selected sextic and degree-sixteen mates"
  - "Saved certificates were source-inspected; independent normal-division replay passed in GitHub Actions run 40434021004 (2026-10-26). Macaulay2 was not rerun in that workflow."
  - "Bound not claimed sharp"
---
# Fixed sextic jet rigidity

## Statement
Put q=x0*x3-x1*x2 and D=x2^3-x1*x3^2, and define Fstar=-q^2*x3^2-q*D*x2+D^2/4+q^3. For a degree-sixteen global G, membership of its generic normal jet in (Fstar)+(u,v)^12 forces G=Fstar*H10. For every proper degree-sixteen complete intersection (Fstar,G) containing C0, its generic multiplicity is even and at most 22; its residual fundamental cycle has degree at least eight.

## Hypotheses and quantifiers
Algebraically closed characteristic-zero base field, this particular Fstar, and degree-sixteen mates only.

## Proof

Write \(K=k(z)=k(C)\). At the generic point use the actual ambient chart
\[
x=(1,z,z^3+v,z^4+u+3zv/2).
\]
Its two transverse parameters generate the marked ideal. Direct substitution
into the displayed four-term carrier gives quadratic term
\[
z^8\bigl((1+z^2)u^2-z^2v^2/4\bigr).
\]
The discriminant class \(1+z^2\) is nonsquare in \(K\): it has simple
zeros at \(z=\pm i\) even though \(k\) is algebraically closed. Thus the
ordinary double point splits into two smooth transverse branches over the
separable quadratic extension \(K(\sqrt{1+z^2})\), exchanged by its Galois
automorphism. Extending the **constant** field does not split this function-field
quadratic class.

For any actual \(G\) meeting the carrier properly, its orders along those
two conjugate branches are equal, say \(n\). Over the splitting extension,
formal transverse coordinates \(U,V\) make the node \((UV)\). The residue of
\(G\) modulo \(UV\) is the sum of a one-variable series of order \(n\)
in \(U\) and one of order \(n\) in \(V\). Its intersection length is
\(2n\): equivalently apply the normalization exact sequence of the node,
whose finite conductor quotient has multiplication kernel and cokernel of
equal length, and sum the two branch orders. The same expression proves
\[
G\in(F_*)+(u,v)^n,\qquad G\notin(F_*)+(u,v)^{n+1}.
\]
Formal coordinate changes preserve maximal-ideal powers and membership
descends through the faithfully flat splitting field. Finite length is
essential; a mate with a carrier factor is excluded by properness.

It remains to prove the **global constant-coefficient** jet-kernel identity.
The source has dimension \(\binom{19}{3}=969\). Over
\[
B=\mathbf Z[1/2,z,z^{-1},(1+z^2)^{-1}],
\]
the coefficient of \(u^2\) in the carrier is a unit. Reducing modulo
\((F_*,(u,v)^{12})\) leaves the 23 normal monomials
\[
1,v,\ldots,v^{11},u,uv,\ldots,uv^{10}.
\]
The relation replaces \(u^2\) by its quadratic \(v^2\) term plus terms
of higher total normal degree. Order these substitutions first by total
degree and within a degree by the \(u\)-exponent. They terminate after
truncation, give a free rank-23 quotient, and reduce every actual degree-16
ambient monomial. This constructs a map from the **969-dimensional constant
coefficient** global source into \(B^{23}\); it does not permit arbitrary
\(k(z)\)-coefficients on those source monomials.

Evaluate its entries at \(z=1,\ldots,30\) modulo \(65521\). All values
are good: \(z\) and \(1+z^2\) are nonzero. Stacking the maps gives the
690-by-969 matrix in the retained exact programs. Its certified rank is 683.
Therefore some 683-minor is nonzero at a good specialization and the
characteristic-zero constant-source map has rank at least 683. Conversely
all 286 independent forms \(F_*H_{10}\) vanish **identically** in this
quotient. Multiplication by nonzero \(F_*\) is injective and
\(h^0(\mathcal O(10))=\binom{13}{3}=286\); hence the rank is at most
\(969-286=683\). It follows that
\[
\ker\bigl(H^0(\mathcal O(16))\longrightarrow
 K[[u,v]]/(F_*,(u,v)^{12})\bigr)
 =F_*H^0(\mathcal O(10)).
\]
The good samples provide a lower rank bound; the identity on all carrier
multiples provides the opposite bound. A recorded rank without this source
identification and kernel inclusion would not prove the statement.

If \(n\ge12\), the kernel identity forces \(G=F_*H_{10}\), contrary
to properness. Thus \(m_C=2n\le22\). The actual complete-intersection
cycle gives \(\deg R=96-4m_C\ge8\). This bounds residual degree without
inferring any residual component from exceptional vertical geometry.

## Exact evidence and independent verification

The two retained implementations have different quotient constructions:
[the Macaulay2 source](../computations/endpoint4_fixed_m2_2026_10_25.m2)
uses quotient-ring coefficients; [the Python/C++ normal-division source](../computations/endpoint4_fixed_jet_independent_2026_10_26.py)
constructs the carrier independently from its four terms and recursively
reduces its jets. Both report rank 683 and annihilation of all 286 multiples.
The M2 source also checks independent rank 286 for the coefficient matrix of
those multiples in the fixed 969-row ambient monomial order. The saved
[metadata](../computations/endpoint4_fixed_m2_2026_10_25.json) and
[independent output](../computations/endpoint4_fixed_jet_independent_2026_10_26.json)
identify the modulus, sample points, and matrix hash.

The original source inspection did not execute either program. Subsequently
GitHub Actions [run 40434021004](https://github.com/markluxton1/STCI/actions/runs/40434021004),
job `replay-r0025`, freshly reconstructed the matrix by Python/C++, passed
rank 683, nullity 286, all-multiples annihilation, and exact SHA-256 match
`a3e546424d11200e1d8075c7f9d5d342787bd925a303901bd2b33b2661f56445`.
Its output was uploaded as a workflow artifact. The Macaulay2 implementation
was not rerun there, and there is no separately archived nonzero maximal minor.
This consolidation transfers the proof bridge and records that replay;
it performs no new inherited computation.

## Characteristic boundary of the argument

The statement above is in characteristic zero. The local nonsplit-node
lemma works in every characteristic different from two, provided its separable
quadratic and finite-length hypotheses hold. For this carrier, the class
\(1+z^2\) is nonsquare over \(k(z)\) in every odd characteristic, since
its two roots are simple. The displayed carrier is undefined as written in
characteristic two because of its coefficient \(1/4\).

There is a concrete additional scoped deduction from the retained certificate:
**the same fixed-carrier degree-sixteen conclusion holds in characteristic
65521.** The exact matrix was constructed in that characteristic, all thirty
samples are good, and its rank 683 together with the 286 global carrier
multiples proves the kernel identity directly there. The separable-node
argument then gives \(m_C\le22\) and residual degree at least eight, exactly
as above. Independent consolidation review accepted this extension as a separate scoped deduction; it does not extend the theorem to all odd primes. More
generally a nonzero rational maximal minor gives the same result away from
finitely many primes after spreading out, but no complete exceptional-prime
list is certified here.

This is compatible with an STCI using a quartic carrier in every positive
characteristic: it concerns a different, single fixed sextic and one mate
degree. The general positive-characteristic construction is owned by
[the curve and characteristic account](../synthesis/01-problem-and-curve.md).

## Consequences
No proper degree-sixteen mate for this selected sextic has sole reduced support C0.

## Limitations
No general sextic or unrestricted STCI theorem.

## Review state

The exact computation and local-length bridge remain within the selected-carrier/degree scope. Their full mathematical bridge and actual independent CI replay are retained directly above. Independent consolidation review accepted the transferred proof bridge, its actual-source/specialization interpretation, the characteristic-65521 consequence and the cofinite-prime existence statement. The new deductions remain separately identified; the characteristic-zero scope is unchanged. No fresh CAS execution was performed.
