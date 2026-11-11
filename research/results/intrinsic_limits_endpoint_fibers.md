---
id: STCI-R-0070
type: result
title: Endpoint fibers and embedded points in the intrinsic torus limits
scope: "#scope"
statement: "#statement"
proofs:
  - name: relative-image
    at: research/arguments/torus_hilbert_boundary.md#endpoint-fibers-in-the-two-intrinsic-limits
    using: [STCI-R-0051, STCI-R-0052]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Endpoint fibers and embedded points in the intrinsic torus limits

## Scope

Let \(Z\subset\mathbf P^3\) be a pure curve with reduced support
\(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field of any
characteristic. Use the chart \([1:r:ur^3:vr^4]\) on the coordinate torus
\(\Omega\). Let \(W\) be the full closure of \(Z\cap\Omega\) in
\(\mathbf P^1_r\times\mathbf G_m^2\), and let \(B_i\), \(i=0,\infty\),
be its two embedded endpoint fibers with their named coordinates \(u,v\).
Write \(m\) for its finite flat rank and \(h=\deg(\pi_*\mathcal O_W)\).
Let \(\delta_j\) be the lengths at \(p_j\) of the cokernel of
\(\mathcal O_Z\to\rho_*\mathcal O_W\) under the finite map \(\rho:W\to Z\).
For an embedded fiber \(B\), let \(D_j(B)\) be the corresponding length
for the projective image of the constant family \(\mathbf P^1_B\).

## Statement

Let \(L_i\) be the full projective Hilbert limit with equation pullback
\(r\mapsto\lambda r\) for \(i=0\) and \(r\mapsto\lambda^{-1}r\) for
\(i=\infty\), as \(\lambda\to0\). On \(\Omega\), \(L_i\) is the constant
family of the embedded algebra \(B_i\). Its pure one-dimensional quotient
is the projective image \(Y_i\) of \(\mathbf P^1_{B_i}\). If \(T_i\) is the
kernel of \(\mathcal O_{L_i}\to\mathcal O_{Y_i}\) and \(j\) is the other
endpoint, then

\[
\operatorname{Supp}T_i\subset\{p_i,p_j\},\qquad
\ell(T_{i,p_i})=D_i(B_i)-\delta_i,\qquad
\ell(T_{i,p_j})=D_j(B_i)-\delta_j+h.
\]

At \(p_i\), \(T_{i,p_i}\) comes from the \(\lambda\)-annihilated part of the
cokernel of the relative weighted image inclusion. In particular, image
formation commutes with specialization on that chart exactly when
\(D_i(B_i)=\delta_i\).

## Limitations

The formulas determine the pure quotient and both embedded lengths. The
actual algebra at the opposite endpoint and the degree-wise generator
incidence still require the full ideal. The comparison uses the action
preserving \(C\). A transverse one-parameter subgroup moves \(C\) and
requires a different limiting support.

## Review

Independent reconstruction by the endpoint reviewer checked the pullback
on the dense torus, purity and support of the quotient, the relative image
and its parameter-torsion sequence, the generic and special ranks of its
cokernel, and the opposite-chart change to \(z=\tau u/v\). The reviewer
derived both endpoint lengths and gave a finite flat length-three example
where the image fails to commute with specialization. The review covers
the comparison for pure supported schemes and uses no computation.
