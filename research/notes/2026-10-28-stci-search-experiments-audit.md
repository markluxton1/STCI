# Independent audit of the new sextic candidate search

Started October 28; completed October 29, 2026. Reviewer:
`candidate_engine/experiment_audit`. Status: independent mathematical and
computational review of provisional fixed-carrier statements. No canonical
record is promoted, and no unrestricted STCI conclusion is asserted.

## Exact inputs and scope

The fixed curve is
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), with \(k\) an
algebraically closed field of characteristic zero. Write
\[
q=x_0x_3-x_1x_2,\qquad D=x_2^3-x_1x_3^2,
\]
and consider the actual homogeneous sextics
\[
F_{t,\kappa}=-q^2x_3^2-qDx_2-tqDx_3+D^2/4+\kappa q^3.
\tag{1}
\]
Their origin and global second-symbol realization are inherited from the
[actual-sextic note](2026-10-25-endpoint4-actual-sextics.md), in the
\(a_0=1,b_1=0,b_2=t\), or \(\rho=-1\), chart. That origin does not
establish existence of a mate. The earlier fixed sextic
\((t,\kappa)=(0,1)\) has the separate promoted
[R-0025](../results/ci_fixed_sextic_jet_rigidity.md) scope; it was not
replayed in the new computations.

The primary [new engine](../computations/stci_search_sextic_jets_2026_10_28.py)
and [saved output](../computations/stci_search_sextic_jets_2026_10_28.json)
test seven specified rational points, retaining all 969 constant global
coefficients of \(G_{16}\). This audit inspects that implementation and
independently reconstructs the key \(t=1\) cases using Macaulay2 quotient
coordinates rather than the engine's recursive normal division.

## The local implication is valid uniformly in the parameters

Use the actual balanced chart
\[
(x_0,x_1,x_2,x_3)=(1,z,z^3+v,z^4+u+3zv/2).
\]
Directly from \(q_1=u+zv/2\) and \(D_1=-2z^5u\), the quadratic
normal term of (1) is
\[
z^8\bigl((1+2tz+z^2)u^2+t z^2uv-z^2v^2/4\bigr).
\tag{2}
\]
The discriminant, up to a rational square, is
\[
P_t(z)=1+2tz+(1+t^2)z^2.
\]
Its quadratic discriminant is \(-4\). Thus it has simple geometric
zeros for every constant \(t\); when \(1+t^2=0\), it is linear with a
simple zero. It is therefore nonsquare in \(k(z)\), even after any
characteristic-zero extension of the constant field. The quadratic term
defines two transverse branches exchanged by the quadratic extension of
\(k(z)\). This conclusion is independent of \(\kappa\).

For a proper pair \((F_{t,\kappa},G)\) containing \(C\), generic
transverse length is finite. Its two conjugate branch orders are equal,
say \(n\), and
\[
\ell_C(F_{t,\kappa},G)=2n,
\qquad G_\eta\in(F_{t,\kappa})+(u,v)^n.
\tag{3}
\]
For completeness, divide by the prepared quadratic and write the remainder
as \(a(v)u+b(v)\). The difference of its restrictions to the two branches
is \(a(v)(\phi_+(v)-\phi_-(v))\); the second factor has order one.
If both branch restrictions have order at least \(n\), then
\(\operatorname{ord}a\ge n-1\) and \(\operatorname{ord}b\ge n\).
The converse follows by restricting \((u,v)^n\) to either smooth branch.
The intersection length is the order of the determinant of multiplication
by \(G\) on the rank-two prepared quotient, hence the sum of the two
branch orders. This does not replace the full initial ideal with two
chosen leading forms.

## The modular rank bridge is sound

At cutoff \(N\), the coefficient of \(u^2\) in (2) is a unit over
\[
\mathbf Z[1/2,t,\kappa,z,z^{-1},(1+2tz+z^2)^{-1}].
\]
Division modulo \((u,v)^N\) has the free basis
\[
1,v,\ldots,v^{N-1},\quad u,uv,\ldots,uv^{N-2}.
\]
Replacing \(u^2\) never lowers total normal degree; at fixed degree it
lowers the \(u\)-exponent. The recursive reduction terminates, and
restriction from cutoff twelve to a smaller cutoff commutes with this
reduction. The engine's selection of lower-degree remainder rows is
therefore legitimate.

Every global generic jet identity specializes to zero at every good
sample. A modular rank is consequently a characteristic-zero lower bound
for the matrix rank. Multiplication by the nonzero global sextic embeds
the 286-dimensional space \(H^0(\mathcal O(10))\), and these actual
multiples are killed at every sample. Rank 683 therefore proves that the
entire compatible global source consists of these multiples. All this
uses constant global source coefficients; the coefficients are never
enlarged to arbitrary \(k(z)\)-valued source parameters.

## Independent finite reconstruction and the sharp nonzero-parameter case

The [independent M2 script](../computations/verify_stci_search_nodal_m2_2026_10_28.m2)
and [complete log](../computations/verify_stci_search_nodal_m2_2026_10_28.txt)
use prime 65521 and the 80 good samples \(z=1,\ldots,80\), with the
same actual global source but a separately computed quotient basis. They
reconstruct the following selected cases:

| \(t\) | \(\kappa\) | cutoff | matrix shape | modular rank |
|---|---|---|---|---|
| 1 | 0 | 9 | \(1360\times969\) | 672 |
| 1 | 0 | 10 | \(1520\times969\) | 683 |
| 1 | 1 | 8 | \(1200\times969\) | 682 |
| 1 | 1 | 9 | \(1360\times969\) | 683 |

In every case the independent global multiplication matrix has rank 286
and its product with the sampled jet matrix is zero. These checks catch
both a wrong global carrier and a wrong source-column convention.

For the four primary-engine points
\[
(t,\kappa)=(1,1),(1,-1),(2,1),(0,-1),
\]
the reported ranks 682 at cutoff eight and 683 at cutoff nine prove
\[
K_8=F_{t,\kappa}H^0(\mathcal O(10))\oplus kq^8,
\qquad K_9=F_{t,\kappa}H^0(\mathcal O(10)),
\tag{4}
\]
where \(K_N\) denotes the actual global degree-sixteen jet kernel.
Indeed \(q^8\) supplies the additional cutoff-eight vector, and it is
independent of the multiples because \(F_{t,\kappa}\bmod q=D^2/4\ne0\).
The modular upper bounds and these explicit lower bounds coincide.
The independent M2 replay covers \((1,1)\); the other three points use
the primary implementation, whose construction and scope bridge were
reviewed here.

By (3), the maximal generic intersection multiplicity at these four
points is exactly sixteen. Every proper mate attaining it has
\(G=cq^8+F_{t,\kappa}H_{10}\) with \(c\ne0\), so its whole complete
intersection ideal equals \((F_{t,\kappa},q^8)\).

This candidate's failure can be identified globally. On the smooth
quadric use Segre coordinates
\((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\). Then
\[
D=b^2(bc^3-ad^3),\qquad \operatorname{div}_Q(D)=C+2L_0,
\quad L_0=V(x_2,x_3).
\]
Since \(F_{t,\kappa}|_Q=D^2/4\), one obtains
\[
[V(F_{t,\kappa},q^8)]=16[C]+32[L_0].
\tag{5}
\]
Thus the residual degree lower bound 32 is attained at the four specified
nonzero-\(\kappa\) points, and their maximal-contact mate schemes all
retain this line. No tangent, formal, or exceptional component is being
relabelled as the residual line; (5) is a global divisor computation.

For the three tested \(\kappa=0\) points, cutoff ten gives only
\(\ell_C\le18\) and residual degree at least 24. The cutoff-nine
rank 672 does not prove that any of the eleven possible extra
characteristic-zero directions exists. In particular the stronger
cutoff-nine exclusion was tried and failed as a rank test; the final
audit records this negative finding rather than imposing rank 683.

## Geometry of the parameter boundary and remaining limitations

Introduce a degree-one auxiliary coordinate \(W\). The exact identity
\[
F_{t,\kappa}=q^2\left[
W^2-2(x_2+tx_3)W-x_3^2+\kappa(x_0x_3-x_1x_2)
\right]_{W=D/(2q)}
\]
exhibits a genuine geometric degeneration. The auxiliary quadric has rank
five when \(\kappa\ne0\): its gradient equations force all five
coordinates to vanish. When \(\kappa=0\), its restriction to
\((x_2,x_3,W)\) has symmetric matrix determinant one and its remaining
two coordinates are free, so the rank is three and the vertex is a line.
This verifies the rank change. It does not identify the whole surface
normalization or prove that the rank change explains the exact jet-kernel
dimensions.

The reviewed conclusions concern seven fixed rational sextics and
degree-sixteen mates, with an independent finite replay for the two
\(t=1\) representatives. They do not exhaust the parameter family,
other root charts, other degree pairs, or possible STCI constructions.
Lower modular ranks provide upper bounds on compatible characteristic-zero
freedom, not automatic constructions. The new engine and this audit
leave all canonical mathematical status unchanged.
