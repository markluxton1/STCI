# Independent audit: all-degree obstruction in the weighted subalgebra

October 30, 2026. Reviewer: line_audit. The local branch and coefficient
claims were also reconstructed independently by the child reviewer
weighted_family_local_check.

**Verdict: PASS for every integer \(m\ge1\), every coefficient choice
specified below, and every positive mate degree.** No irreducibility
assumption on the carrier form is needed. This is review of a provisional
research contribution, not canonical promotion.

The audited proposal is
[the weighted-subalgebra line obstruction](2026-10-30-weighted-subalgebra-line-obstruction.md).
The earlier [four-line argument](2026-10-30-mixed-weight-line-obstruction.md)
is its \(m=2\) specialization. This audit reconstructs the more general
proof without using or rerunning the earlier integrality certificate.

## Literal family and hypotheses

Let \(k\) be an algebraically closed field of characteristic zero. Fix
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,\qquad
q=x_0x_3-x_1x_2,\quad
c_0=x_1^3-x_0^2x_2,\quad c_2=x_2^3-x_1x_3^2.
\]
Fix \(m\ge1\) and take actual homogeneous binary forms \(B_j(U,V)\)
of degree \(j\), with scalar coefficients, in
\[
F=\sum_{i=0}^{\lfloor m/2\rfloor}
q^{3i}B_{m-2i}(c_0,c_2).
\tag{1}
\]
Assume that \(B_m\) is squarefree and has no root on either coordinate
axis. Equivalently,
\[
B_m(U,V)=a\prod_{j=1}^{m}(V-\lambda_jU),
\qquad a\ne0,
\]
with all \(\lambda_j\in k^*\) distinct. No condition is imposed on
the lower binary forms. Every summand has ordinary degree \(3m\).

The conclusion is that no homogeneous form \(G_b\), \(b>0\), satisfies
\(V(F,G_b)_{\mathrm{red}}=C_0\). The mate may itself be reducible or
nonreduced. The carrier form \(F\) is allowed to be reducible.

## The actual coefficient family

The forms \(q,c_0,c_2\) are algebraically independent in characteristic
zero. On the coordinate hyperplane \(x_0=0\) they become
\[
(-x_1x_2,\ x_1^3,\ x_2^3-x_1x_3^2).
\]
Their Jacobian determinant with respect to \(x_1,x_2,x_3\) is
\(-6x_1^4x_3\ne0\), so already this restriction is algebraically
independent. Consequently the monomials in (1) are linearly independent;
the coefficient count is an actual global source dimension, not an
abstract symbol count:
\[
\dim=
\begin{cases}
(k+1)^2,&m=2k,\\
(k+1)(k+2),&m=2k+1.
\end{cases}
\]
The hypothesis on the top boundary is a nonempty open condition in this
coefficient space. It is not a genericity assumption on the lower forms.

## Uniform local reconstruction for all \(m\)

On \(x_0=1\), put \(t=x_1\), \(u=x_2-t^3\), and
\(q=x_3-tx_2\). Then
\[
c_0=-u,\qquad
c_2=t^6u-2t^5q+O((u,q)^2).
\]
The normal order of the \(i\)-th summand in (1) is at least \(m+i\).
The initial form is therefore exactly \(B_m(c_{0,1},c_{2,1})\).
For \(t\ne0\), the two displayed linear normal coordinates are independent.
This proves that \(F\) is nonzero, of exact generic normal order \(m\),
and has precisely \(m\) distinct transverse tangent branches.

For a direct regularity check, set \(q=uz\). Then \(c_2/u\) has the
form \(t^6-2t^5z+uP(t,u,z)\), and
\[
\frac{F(t,u,uz)}{u^m}
=B_m(-1,t^6-2t^5z+uP)
 \sum_{i\ge1}u^iz^{3i}
B_{m-2i}(-1,t^6-2t^5z+uP).
\tag{2}
\]
At \(u=0\), its roots are
\[
z_j(t,0)=\frac{t^6+\lambda_j}{2t^5}.
\]
They are distinct and simple for \(t\ne0\). The formal implicit-function
theorem gives \(m\) regular branches
\(q=u z_j(t,u)\), each with \(u\) as its inverse-curve parameter.
The coefficients are defined over \(k(t)\), so the generic inverse
curves in the disjoint normalization have residue field \(k(t)\),
not a hidden extension of it.

This argument works equally for even and odd \(m\), including \(m=1\),
and for every lower coefficient choice. It does not extrapolate from a
finite sample of degrees or coefficients.

## Actual lines, a unique component, and simple attachment

On the target quadric \(q=0\), writing \(w=x_2\) gives
\[
c_0=t^3-w,\qquad c_2=-w^2c_0,\qquad
F|_{q=0}=c_0^mB_m(1,-w^2).
\]
For every \(j\), the two nonzero square roots \(w_{j,\pm}\) of
\(-\lambda_j\) give distinct actual lines
\[
L_{j,\pm}=V(x_2-w_{j,\pm}x_0,\ x_3-w_{j,\pm}x_1)
\subset V(F).
\]
All \(2m\) lines are distinct. Each meets \(C_0\) at the three distinct
nonendpoint parameters \(t^3=w_{j,\pm}\); its point at infinity is
outside \(C_0\).

A line cannot be generically shared by two carrier components. Away
from \(C_0\), the derivative along it is
\[
\left.\partial_w(F|_{q=0})\right|_{w=w_{j,\pm}}
=-2w_{j,\pm}c_0^m
\frac{\partial B_m}{\partial V}(1,\lambda_j)\ne0.
\]
Thus the full hypersurface is generically smooth on each line, which
belongs to a unique global irreducible component. Its strict transform
is finite birational over the smooth projective line, hence isomorphic
to it.

At \(t_0^3=w_{j,\pm}\), only the \(j\)-th root in (2) has
\(z_j(t_0,0)=0\). The actual line has \(q=0\) and
\(u=w_{j,\pm}-t^3\). Substitution into (2), with \(z=0\), vanishes
identically because
\(B_m(-1,w_{j,\pm}^2)=0\); all higher terms vanish as well.
The other branches have nonzero \(z\)-values at the origin, so this line
germ lies on precisely the \(j\)-th regular normalization branch.
Moreover
\[
\frac{d}{dt}(w_{j,\pm}-t^3)\big|_{t=t_0}
=-3t_0^2\ne0.
\]
The attaching multiplicity to that inverse curve is exactly one.
In particular, the same label \(j\) is selected at all three points of
each line. The global curve label is well defined by its generic
tangent equation \(c_2=\lambda_jc_0\).

## Reducible carriers and the global degree identity

Assume a sole-support mate \(G_b\) exists, and factor
\(F=\prod_a H_a^{e_a}\) into irreducible homogeneous forms.
Every \(H_a\) must contain \(C_0\). Indeed,
\(V(H_a,G_b)\subset C_0\), while an intersection of two positive-degree
projective hypersurfaces in \(\mathbf P^3\) has a curve unless they share
a surface component, which is even more immediately incompatible with
sole curve support. If \(H_a\) did not contain \(C_0\), its intersection
with the irreducible curve would be finite, a contradiction.

At the generic point of \(C_0\), the initial form of every \(H_a\) is
nonconstant. The associated graded local ring is a polynomial domain
in two normal variables. Hence the initial form of \(F\) is the product
of those initial forms to powers \(e_a\). Since \(B_m\) is squarefree,
every \(e_a=1\), and its \(m\) linear factors are partitioned among the
global components.

This is a conditional reduction under the hypothetical mate. It does
not assert that every member of (1) is globally squarefree irrespective
of factors avoiding \(C_0\); such factors would already exclude a mate.
It also does not assume irreducibility of \(F\).

Normalize the disjoint union of the reduced components and write
\(H=\nu^*\mathcal O_{\mathbf P^3}(1)\) on this disjoint normal surface.
The pulled-back section of \(G_b\) is nonzero on every component and has
effective divisor
\[
\operatorname{div}(\nu^*G_b)=\sum_{j=1}^{m}r_j\Gamma_j,\qquad r_j>0,
\]
where each \(\Gamma_j\) maps with generic degree one to \(C_0\).
A finite normalization cannot add a curve mapping to an isolated point.
No other divisor component is permitted by sole support.

At the line-attachment points, the relevant branch is regular and its
inverse curve has parameter \(u\). Sole support makes the section
\(u^{r_j}\) times a unit. Its restriction to either attached line
therefore has three zeros, each of order exactly \(r_j\), and no other
zeros. The line restriction is nonzero, since an identically zero
restriction would add that line to the intersection support. Thus
\[
b=3r_j\qquad\text{for every }j.
\tag{3}
\]
The degree of the reduced carrier under the hypothetical mate is
\(\sum_a\deg H_a=\deg F=3m\), and
\(H\cdot\Gamma_j=4\). Intersecting the effective divisor with \(H\)
on the disjoint normalization gives
\[
3mb=4\sum_{j=1}^{m}r_j=\frac{4mb}{3}.
\tag{4}
\]
This is impossible for \(m,b>0\). The contradiction proves the claim.
It covers arbitrary reducible and nonreduced mates and retains every
global carrier factor.

## Scope, negative tests, and review outcome

The audit actively checked the following possible failures:

- A carrier factor avoiding \(C_0\) cannot evade the argument; it already
  forces extra projective intersection support.
- Repeated carrier factors containing \(C_0\) contradict the actual
  squarefree initial form. The reduced-degree identity is therefore
  justified under the mate assumption.
- Different normalization branch orders are permitted. Their values are
  constrained separately by the lines; equality is a conclusion.
- Generic tangent directions alone would be insufficient. Equation (2)
  and the exact line substitution verify actual local attachment.
- The lines are generically smooth points of the full hypersurface, so
  a line cannot be counted on the wrong global component.
- Endpoint roots, repeated boundary roots, and positive characteristic
  are not silently discarded: they are excluded from the stated
  hypotheses and remain outside the conclusion.

The proof is uniform in every integer \(m\) and every allowed coefficient.
No finite degree enumeration is being substituted for it. The result is
restricted to the displayed weighted subalgebra and its squarefree
axis-free binary boundary. It does not classify arbitrary global forms,
close the general projection locus, or settle unrestricted STCI.
No canonical record was changed for this audit.
