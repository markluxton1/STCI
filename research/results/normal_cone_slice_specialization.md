---
id: STCI-R-0062
type: result
title: Degreewise Tor kernel and the all-degree normal-flatness criterion
scope: "#scope"
statement: "#statement"
proofs:
  - name: neighborhood Tor sequences and Artin–Rees
    at: "research/arguments/transverse_specialization.md#normal-cone-specialization"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Normal-cone specialization to a specified slice

## Scope

Let \(B\) be a DVR with uniformizer \(t\) and residue field \(k\), let \(M\)
be a Noetherian \(B\)-algebra, and let \(K\subset M\) be an ideal. Set
\(\bar M=M/tM\) and let \(\bar K\) be the image of \(K\). This applies in
arbitrary characteristic, including to intersections with residual
support. A geometric transverse slice uses a specified parameter lift
giving the \(B\)-algebra structure.

## Statement

For \(n\ge 0\) set \(N_n=M/K^n\), \(A_n=K^n/K^{n+1}\), and
\(U_n=\operatorname{Tor}_1^B(N_n,k)\). There is a natural exact sequence
\[
U_{n+1}\longrightarrow U_n\longrightarrow A_n\otimes_B k
\xrightarrow{\gamma_n}\operatorname{gr}_{\bar K}^n\bar M
\longrightarrow 0.
\]
The kernel \(E_n\) of \(\gamma_n\) is canonically the cokernel of
\(U_{n+1}\to U_n\). These identifications are compatible with graded
multiplication. The kernels form the ideal of the closed immersion of the
actual slice cone into the special fiber of the relative normal cone. The
degreewise expression under injectivity of \(t\) on \(M\) is
\[
E_n=\frac{(K^n\cap tM)+K^{n+1}}{tK^n+K^{n+1}}.
\]
With \(U_n=(K^n:_M t)/K^n\), the connecting homomorphism sends the class
of \(m\) with \(tm\in K^n\) to the class of \(tm\) in \(A_n\otimes_B k\).

If multiplication by \(t\) on \(M\) is injective and \(M/K=B\) as a
\(B\)-algebra, the following conditions are equivalent.

1. \(\gamma_n\) is an isomorphism for every \(n\ge 0\).
2. \(M/K^n\) is \(B\)-flat for every \(n\ge 1\).
3. \(K^n/K^{n+1}\) is \(B\)-flat for every \(n\ge 0\).
4. \(K^n\) is \(t\)-saturated in \(M\) for every \(n\ge 1\), meaning
   \((K^n:_M t)=K^n\).

Condition 3 is ordinary normal flatness over the marked base. The
[Tor and Artin–Rees proof](../arguments/transverse_specialization.md#normal-cone-specialization)
includes the specialization maps and the counterexamples below.
[Stacks, normal cones](https://stacks.math.columbia.edu/tag/062Z) ·
[Stacks, Artin–Rees](https://stacks.math.columbia.edu/tag/00IN)

For the classical context on normal flatness and tangent cones of fibers,
see [Lejeune-Jalabert and Teissier, *Normal cones and sheaves of relative jets* (1974)](https://www.numdam.org/item/CM_1974__28_3_305_0/).
The local criterion here has a direct Tor and Artin–Rees proof.

## Limitations

The single-degree condition \(E_n=0\) tests surjectivity of one Tor
transition. In characteristic zero, take \(B=k[[t]]\), \(I=(x,y)\) in
\(R=B[[x,y]]\), and
\[
J=(t^r x+x^2+y^2,\ t^r y+xy+y^2+x^3),\qquad r\ge 1.
\]
For \(M=R/J\) and \(K=IM\), the actual algebra is finite free over \(B\),
and \(\gamma_1:k^2\to k^2\) is an isomorphism although
\(A_1\simeq (B/(t^r))^2\).

Injectivity of \(t\) on \(M\) is essential to infer normal flatness from
all-degree agreement. In \(R=k[[t,x,y]]\), the regular sequence
\((x,ty+x^2)\) gives \(M=B[[y]]/(ty)\) and \(K=(y)M\). Both specialized
normal algebras are \(k[Y]\), yet \(A_n=B/(t)\) for every \(n\ge 1\).
The transverse comparison concerns the chosen lift of the parameter on
the marked curve.

## Review

The Phase 5 nonauthor reviewer `review_specialization` accepted the
neighborhood Tor and Artin–Rees route. The reviewer reconstructed the image
of the tensor map, the connecting homomorphism and the multiplication action
on its cokernels. They checked where injectivity of \(t\) and agreement in
every degree enter the flatness implication, and reconstructed both the
nonflat residual example and the characteristic-zero single-degree example.
The decision concerns the stated DVR criterion and its controls.

The October 24 account records independent local reconstruction of the
specialization development. The single-degree example uses the \(m=2\)
case of its characteristic-zero punctual family.
[Specialization source](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-transverse-specialization-and-normal-flatness) ·
[Punctual family](punctual_comparison_defect_family.md)
