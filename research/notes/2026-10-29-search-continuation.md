# Projection, mixed-weight contact, and arithmetic search continuation

October 29, 2026. Status: **synthesis of reviewed provisional contributions**.
This is not a canonical result or a claim that all three requested endpoints
have been completed. The full marked-quadric admissible locus and descent on
its surviving strata remain uncomputed.

This continuation uses the existing branch
codex/intersections-containing-quartic-2026-10-27, starting from commit
9238210. Proofs, audits and computations are retained as local changes.

Throughout, \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Characteristic
zero is understood in the projection and mixed-weight sections; the
arithmetic section specifies its characteristic. For a proper containing
pair retain \([V(F_a,G_b)]=m_C[C_0]+R\) and \(ab=4m_C+\deg R\).
The unrestricted characteristic-zero STCI question remains open.

| Requested direction | Completed result | Exact remaining limit |
| --- | --- | --- |
| Admissible marked smooth-quadric projections and descent | Determinant orders reduced to one and two; several complete coefficient slices and residual-divisor strata excluded | The remaining order-one/order-two parameter incidence is not solved. No admissible surviving stratum has been supplied for a conductor or pure-power descent calculation |
| Global contact in an explicit mixed-weight family | The complete \((6,6)\) contact-nine incidence is empty for every nonzero pair of seed parameters | Higher mate degrees, including sixteen, and other carrier families remain untested |
| Arithmetic obstruction beyond binomial carriers | A higher-jet obstruction forces \(p\mid b\) on a specified 23-parameter source; explicit two-non-binomial \((16,p)\) pairs attain the bound for every prime \(p\ge43\) | This is a restricted-source minimum. There is no reduction of arbitrary pairs to this source and no all-pairs growing lower bound |

## 1. Projection: computed exclusions and the unresolved incidence

The source is the entire sixteen-parameter system
\[
U=(a^2,ab,dc,d^2)+\Delta(A_0,A_1,A_2,A_3),\qquad
ad=bc,\quad\Delta=b-c,\quad A_i\in\langle a,b,c,d\rangle.
\]
Retain basepoint freedom, birationality and full reduced inverse support
equal to the diagonal, including isolated inverse points. These are the
literal requirements of [R-0004](../results/projection_phase_reduction.md),
not consequences of the model classification
[R-0002](../results/cartier_singleton_lift.md).

The [projection calculations](2026-10-29-projection-locus.md) exclude:

- Every member with \(U_0=a^2,U_1=ab\), with all eight coefficients of
  \(A_2,A_3\) free.
- Every member of
  \(U=(a^2+A\Delta^2,aL,dL,d^2+D\Delta^2)\),
  \(L=pb+(1-p)c\), including all zero and \(p=1/2\) strata.
- The full coefficient locus with
  \(q(U)=\kappa\Delta^2ad\), \(\kappa\ne0\), inside the complete
  nine-parameter order-two source. Exact coefficient-ideal saturation
  retains both branches and forces an endpoint inverse point or a basepoint.

The entire order-two **square residual** stratum \(D=2R\), for every
effective divisor \(R\) of type \((1,1)\) distinct from \(c\), is also
excluded by the [double-residual calculation](2026-10-29-projection-double-residual.md)
and its [independent audit](2026-10-29-projection-double-residual-audit.md).
For smooth \(R\), the image would be an integral \((3,1)\) curve on the
target quadric meeting \(C_0\) in at most two points. The exact binary-form
restriction calculation rules that out. Reducible \(R\) forces an
integral \((1,1)\) conic with fourth-order contact at a single point;
its missing binary coefficient rules that out as well.

The [residual geometry](2026-10-29-projection-residual-geometry.md) proves
that every basepoint-free tuple has nonzero \(q(U)\), and
\[
V(q(U))=mc+D,\qquad m=1\ \hbox{or}\ 2,\qquad
D\in|\mathcal O(4-m,4-m)|.
\]
Here \(c=(\Delta=0)\); \(D\) may be reducible or nonreduced.
The two target-ruling degrees on \(D\) are
\((8-3m,8-m)\). The section cutting out \(C_0\) on \(D\) has total degree
26 or 20, while \(D\cap c\) has length six or four.
Full inverse support requires every zero of this section to lie on
the support of \(D\cap c\), with no component mapping into \(C_0\).
The first-normal derivative-zero boundary is a four-dimensional symmetric
source and cannot be birational.

These are necessary strata and completed exclusions, not an evaluation
of the full sixteen-parameter admissible locus. The
[independent projection audit](2026-10-29-projection-locus-audit.md)
reconstructs the proofs and records this limitation. On an actual
admissible stratum the next descent equation remains
\[
\Delta^{2b}\in\operatorname{span}_k\{U^\alpha:|\alpha|=b\}.
\]
There is no surviving admissible stratum identified here on which this
all-degree descent problem has been completed.

## 2. Mixed-weight contact: the bounded endpoint is empty

Put \(q=x_0x_3-x_1x_2\), \(c_0=x_1^3-x_0^2x_2\),
\(c_2=x_2^3-x_1x_3^2\), and take
\[
F_{\alpha,\beta}=q^3+\alpha c_0^2+\beta c_2^2,\qquad
\alpha\beta\ne0.
\]
The [complete incidence calculation](2026-10-29-mixed-weight-contact.md)
proves that every member is integral and every proper actual sextic
mate satisfies
\[
m_C\le8,\qquad \deg R=36-4m_C\ge4.
\]
Thus the required length-nine \((6,6)\) incidence is empty. Attainment
of the bound eight is not asserted.

The generic node splits. The calculation therefore controls both
branch orders separately, including asymmetric contact: branch order
at least five forces a global sextic to be a scalar multiple of \(F\).
It retains all 84 global coefficients. The parameter remains symbolic
over \(\mathbf Q[h]\); two exact finite schemes for the curve coordinate
eliminate all exceptional parameter roots left by the first rank test.
The [independent proof and verifier](2026-10-29-mixed-weight-contact-audit.md)
confirm the uniform conclusion. This does not compute degree-sixteen
mates on this family.

## 3. Arithmetic: a larger source with attained degree growth

The specified enlargement is
\[
\begin{aligned}
U_0&=s^4+s^2zL_0,&U_1&=s^3t+s^2zL_1,\\
U_2&=st^3+\alpha z^4+szC_2,&U_3&=t^4+zB_3,
\end{aligned}
\]
where \(\alpha\ne0\), \(L_0,L_1\) are linear, \(C_2\) quadratic, and
\(B_3\) cubic. Retain basepoint-free members with full singleton inverse
support. Its larger admissible locus has not been classified.

The [arithmetic proof](2026-10-29-arithmetic-beyond-binomial.md) gives a
higher-jet descent mechanism: a target-ring gap through order \(e-1\)
and a required unit with constant nonzero residue and nonzero linear term force
\[
p^{v_p(b)}\ge e.
\]
The whole source has \(e=2\), so every mate degree satisfies \(p\mid b\)
in characteristic \(p\); characteristic zero permits no positive mate
degree. A sublocus has \(e=3\), forcing \(4\mid b\) in characteristic two.
This is not a binomial-equation argument.

On the concrete member
\[
U=(s^4,s^3t,st^3+z^4,t^4+s^3z),
\quad
F=(x_0^3x_3-x_1^4)^4-x_0^{13}(x_0^2x_2-x_1^3),
\]
the note supplies explicit homogeneous \(G_p\) of degree \(p\) with
\[
G_p(U)=z^{4p},\qquad
V(F,G_p)_{\mathrm{red}}=C_0,\qquad [V(F,G_p)]=4p[C_0]
\]
for every prime \(p\ge43\). Both equations are non-binomial.
Consequently the minimum mate degree on this carrier, and the minimum
maximum defining degree within the retained birational source, equal
\(p\) for these primes.
The [jet and constructive audit](2026-10-29-arithmetic-beyond-binomial-audit.md)
and [separate explicit-equation audit](2026-10-29-arithmetic-explicit-mate-audit.md)
check the obstruction and the positive construction independently.

The unrestricted \(\delta(p)\) minimizes over all presentations, so it is
not bounded below by this restricted-source minimum. The missing
implication is a mechanism covering every possible supported pair, or a
valid reduction of all pairs to sources with such a gap. The explicit
family demonstrates both growing obstruction and Frobenius-supported
attainment; it does not resolve that implication.

## Authority and verification

All new conclusions remain reviewed provisional evidence. No canonical
result/question record is changed. The source notes link exact scripts,
saved outputs and independent reviews. The accepted result records are
used only within their stated scopes; no inherited quartic proof or
previous fixed-carrier certificate was rerun for this continuation.
