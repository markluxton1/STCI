# Sextic pairs with an ADE pencil carrier

**Status, October 31, 2026: independently reviewed provisional reduction;
not promoted.** Fix \(C_0=[s^4:s^3t:st^3:t^4]\) in characteristic zero.
If a proper supported sextic pair has a general normal pencil carrier
with only rational double points, its canonical filtration satisfies
\[
 \boxed{L=\mathcal O_{\mathbf P^1}(-6),\qquad D_2=0.}
\]
Its saturated triple is therefore an embedded primitive triple of type
\(\mathcal O(-6)\). This leaves a restricted case; it does not imply
that every normal pencil carrier is ADE or exclude every sextic pair.

The [all-pair sextic reduction](SEXTIC_PAIR_REDUCTION.md) owns the normal
pencil, smoothness off the curve and saturated divisor profile. Retain
\(L=\mathcal O(-l)\), \(l\in\{5,6,7\}\), \(D_8=2T\), and
\(\deg T=4l-17\). The full first-symbol divisor of a general member
\(S\) has degree \(l+10\). Its mate cuts \(9C_0\), so local Cartier
indices divide nine. All singularities of \(S\) lie on \(C_0\).

## Marked local models and exact defects

The smooth marked rational-double-point classification in
[Jaffe, Theorem 4.1 and Propositions 5.2–5.3](https://arxiv.org/pdf/alg-geom/9410008)
lists \(A_{r-1}^{c}\), the two marked \(D\) families, \(E_{6,1}\)
and \(E_{7,1}\). The \(D\) and \(E_7\) indices are two or four,
which cannot divide nine. There is no smooth marked \(E_8\) case.
A smooth Cartier curve cannot pass through a singular hypersurface point:
quotienting an embedding-dimension-three surface ring by one equation
leaves embedding dimension at least two.

For \(A_{r-1}^{c}\), the first-symbol order is \(c\), with
\(1\le c\le r/2\), and the actual index is \(r/\gcd(r,c)\).
Use coordinates
\[
 S:(UV+t^r=0),\qquad C_0:(U,V)=(-t^{r-c},t^c).
\]
Since \(9C_0\) is Cartier, \(k=9c/r\) is an integer in
\(\{1,2,3,4\}\). The exact local divisor coefficients are
\[
 D_8=(k-1)c,\qquad T=\frac{(k-1)c}{2},\qquad
 D_2=\max\{0,3c-r\}.                                  \tag{1}
\]

For the socle formula, put \(v=V-t^c\) and let \(D\) be the axis
prime \((V,t)\). Then \(\operatorname{div}(v)=C_0+cD\) and
\(\operatorname{div}(V)=rD\). The rational function \(h=v^9/V^k\)
has divisor \(9C_0\), and is regular by normality. An actual local mate
differs from it by a unit. The reviewed
[local Jacobian/socle identity](NORMAL_INDEX_SOCLE_AND_TORSION.md) gives
\[
 c+D_8=\operatorname{ord}_t((v^9/h)|_{C_0})
      =\operatorname{ord}_t(V^k|_{C_0})=kc.
\]
For the second defect, put \(u=U+t^{r-c}\). The carrier equation is
\(uv+t^cu-t^{r-c}v=0\), and its saturated first direction is
\(m=u-t^{r-2c}v\). Generically,
\[
 m=-t^{r-3c}v^2+O(v^3).
\]
The [actual-pole identification](SEXTIC_PAIR_REDUCTION.md#the-constant-direction-triple-and-its-actual-defects)
is local and does not require a constant global direction. It identifies
the second defect with the pole order of this quadratic coefficient,
proving (1).

The remaining non-\(A\) type \(E_{6,1}\) has first-symbol order two
and index three, with model
\[
 x^2-2xt^2-y^3=0,\qquad C_0:(x,y)=0.
\]
Here \(x\) cuts \(3C_0\), giving a primitive triple on the smooth
surface \(x=0\). Its primitive-index defect is zero. The local
power-socle formula gives \(D_8=4,T=2\), and its saturated triple has
\(D_2=0\).

The complete local numerical list is:

| Type | Parameters | First-symbol order | \(T\) | \(D_2\) | Root rank \(\rho\) |
|---|---|---:|---:|---:|---:|
| \(A\), \(k=1\) | \(r=9c\) | \(c\) | 0 | 0 | \(9c-1\) |
| \(A\), \(k=2\) | \(c=2h,r=9h\) | \(2h\) | \(h\) | 0 | \(9h-1\) |
| \(A\), \(k=3\) | \(r=3c\) | \(c\) | \(c\) | 0 | \(3c-1\) |
| \(A\), \(k=4\) | \(c=4h,r=9h\) | \(4h\) | \(6h\) | \(3h\) | \(9h-1\) |
| \(E_{6,1}\) | — | 2 | 2 | 0 | 6 |

All parameters are positive integers. The first row has no defect, hence
is locally primitive. For a general pencil member its singularities in
that locus are simple moving zeros, so \(c=1\). The inequalities below
also hold for every listed \(c\), without this refinement.

## The rank budget and the surviving row

An ADE sextic resolution has \(h^{1,1}=86\). Its negative-definite
exceptional root lattices are independent of the positive-square hyperplane
class, giving total root rank at most 85. This is also Jaffe's Lemma 11.3
specialized to degree six. No such bound is asserted here for arbitrary
normal singularities or in positive characteristic.

Every local row satisfies \(8c-\rho\le8T\). Summing over all
singularities, including moving ones, yields
\[
 \rho_{\rm total}\ge8(l+10)-8(4l-17)=216-24l.          \tag{2}
\]
For \(l=5\), this is 96, exceeding 85 and excluding the row.

For \(l=6\), a positive \(D_2\) requires a \(k=4\) point. The
budget \(\deg T=7\) permits only one, with \(h=1\). It consumes
first-symbol order four and \(T=6\), and contributes rank eight. The
other points have total first-symbol order twelve and \(T=1\), hence
rank at least 88 by the local inequality. Total rank would be at least
96, so \(D_2=0\).

For \(l=7\), the global triple obstruction requires \(D_2>0\).
The budget \(\deg T=11\) permits exactly one positive-second-defect
point, necessarily \(k=4,h=1\). Thus \(D_2=3[P]\). The reviewed
global actual-pole restrictions exclude this: axis directions have no
actual degree-three defect, and mixed directions require three distinct
points. This excludes the last row.

Only \(l=6,D_2=0\) remains. Its saturated triple has local basis
\(1,v,v^2\) with \(v^3=0\), so is primitive even at nonprimitive
points of the length-nine structure.

Independent reconstruction accepted the marked classification coverage,
actual-index restrictions, both defect formulas, the \(E_6\) contribution,
rank budget and all three row dispositions. Existing surface and triple
results were reused within their established scopes. The proof uses exact
formulas and inequalities rather than a finite search. The
\(\mathcal O(-6)\) primitive-triple case and non-ADE carriers remain open.

## Three remaining primitive-triple orbits

The surviving primitive triples have an existing complete classification.
The independently audited
[primitive-direction calculation](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#independent-audit-and-all-degree-exclusion-of-primitive-e1-quartic-triples),
subsection “Every basepoint-free primitive triple direction,” uses only
the embedded curve, \(L=\mathcal O(-6)\), \(M=\mathcal O(-8)\),
and its quadratic transition class. Its four actual ambient torus orbits
are represented by
\[
 (A,B)=(1+z,-2-8z),\qquad
 (A,B)=(rz,1),\quad (2r+1)(12r^2+4r+3)=0.
\]
Here \(A,B\) describe the conormal quotient in the source's balanced
frame. The triple in each fixed direction is unique, since
\(H^0(\operatorname{Hom}(M,L^2))=H^0(\mathcal O(-4))=0\).
The classification has no quartic-ancestor hypothesis. The source's later
degree-four carrier exclusions do not transfer automatically to sextics.

The \(r=-1/2\) orbit is excluded for sextics directly. In the actual chart
\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+V,\quad
 x_3=z^4+U+\tfrac32zV,
\]
the containing quadric is \(q=U+zV/2\). For
\((A,B)=(-z/2,1)\), the kernel direction \(BU-AV\) is exactly
\(q\). Its quadratic cocycle has the identically zero factor
\(2A+zB\), so the unique primitive correction is zero. The triple is
precisely the Cartier divisor \(3C_0\) on \(Q\).

A sextic containing it restricts to a section of
\[
 \mathcal O_Q(6,6)(-3C_0)=\mathcal O_Q(3,-3),
\]
which has no nonzero sections. Both sextics would therefore be divisible
by \(q\), contradicting properness. Only the principal orbit and the
two roots of \(12r^2+4r+3=0\) remain.

Independent reuse review checked the classification's complete curve-only
scope, the actual torus action, frame convention, unique triple, and
quadric restriction. These three orbits classify the remaining triples.
Their full degree-six equation spaces and first further contact condition
are computed below; higher extensions and sole support remain unresolved.

## Full sextic spaces and the first further contact equation

The [exact source-space computation](../computations/audit_sextic_triple_spaces_2026_10_31.py)
uses all ambient monomials and the accepted triple substitution
\[
 U=Ay-T_0\gamma y^2,\qquad V=By+S_0\gamma y^2,
 \qquad AS_0+BT_0=1.
\]
For the principal orbit,
\((S_0,T_0,\gamma)=(4/3,1/6,96+192z)\); for the algebraic
orbits, \((S_0,T_0,\gamma)=(0,1,0)\).
Vanishing of every coefficient of \(y^0,y^1,y^2\) is exactly
containment of the triple. Its purity makes the dense affine calculation
sufficient for a global section: no nonzero image section can be supported
only at infinity.

| Exact quantity in characteristic zero | Principal orbit | Either algebraic orbit |
| --- | ---: | ---: |
| Dimension of containing quartics | 2 | 2 |
| Dimension of containing quintics | 11 | 11 |
| Dimension of containing sextics | 27 | 27 |
| Span of quartic-source multiples by quadrics | 20 | 20 |
| Additional sextic directions modulo that span | 7 | 7 |
| Rank of the first-normal map \(h\) | 17 | 17 |
| Rank of the cubic-contact map \(\Theta\) | 18 | 12 |
| Rank of the joint map \((h,\Theta)\) | 23 | 24 |

To define the last maps, use the linear coordinates
\(U=T_0m+Ay,\ V=-S_0m+By\). The relevant terms of a containing
sextic are
\[
 F=h_Fm+\gamma h_Fy^2+E_Fmy+K_Fy^3+\cdots,
 \qquad \Theta_F=\gamma E_F-K_F.
\]
The omitted terms do not affect the cubic coefficient after eliminating
\(m\), whose order along the triple is two. With
\(q'=m+\gamma y^2\), the expansion begins
\(F=h_Fq'-\Theta_Fy^3+\cdots\). If \(h_F\ne0\) generically,
eliminating \(q'\) from \(F,G\) leaves cubic coefficient
\[
 \frac{h_G\Theta_F-h_F\Theta_G}{h_F}.
\]
Thus a generically curvilinear supported sextic pair necessarily satisfies
\[
 \boxed{h_G\Theta_F-h_F\Theta_G\equiv0.}
\]
Otherwise its generic transverse length is three, instead of nine.
At least one first-normal coefficient is nonzero in the length-nine
curvilinear setting. The next coefficients through order eight must also
vanish; those conditions and properness have not been solved here.

The script uses exact rational arithmetic and
\(\mathbb Q(\sqrt{-2})\). Conjugation transports the complete algebraic
source and contact matrices to the other root, preserving the ranks.
An independent review reconstructed the substitution, global-source
coverage and contact sign, ran the exact calculation, and added a direct
rank-and-containment check for all twenty quartic-times-quadric products.
Run `PYTHONDONTWRITEBYTECODE=1 python3 research/computations/audit_sextic_triple_spaces_2026_10_31.py`.
This completes the stated linear calculation and first necessary contact
test; it does not exclude the remaining sextic pairs.

## Intrinsic double-sextic kernel, torus weight grading, and VGIT Plücker contact map

*(Authored by Gemini on `evaluate_toric_integration_stci`; independently reviewed and verified by Gemini subagent and [`verify_sextic_triple_toric_vgit.py`](../computations/verify_sextic_triple_toric_vgit.py).)*

The numerical invariants in the table above admit an intrinsic geometric and torus-equivariant explanation that connects the three \(\mathcal O(-6)\) primitive triples directly to the double-sextic source space \(V_{6,2} = H^0(\mathcal I_{C_0}^2(6))\) (\(\dim = 23\)) and to the surface-pair VGIT Grassmannian \(X_6 = \operatorname{Gr}(2, V_6)\).

### 1. Intrinsic identification of \(\ker(h)\) and the \(23\) vs. \(24\) joint-rank split

Let \(I_{\mathrm{triple}} \subset I_{C_0}\) be any of the three surviving \(\mathcal O(-6)\) primitive triple ideals, and write \(V_{\mathrm{triple},d} = H^0(\mathcal I_{\mathrm{triple}}(d))\). Along \(C_0\) in the dense affine chart \(x_0 = 1\), \(I_{C_0} = (m, y)\) and \(I_{\mathrm{triple}} = (q', y^3)\) where \(q' = m + \gamma(z) y^2 \equiv m \pmod{I_{C_0}^2}\).

- **Intrinsic Double-Sextic Kernel Lemma:** Sheaf-theoretically, \((\mathcal I_{\mathrm{triple}} + \mathcal I_{C_0}^2)/\mathcal I_{C_0}^2 = \mathcal I_{\mathrm{rib}}/\mathcal I_{C_0}^2 \cong M = \mathcal O_{\mathbf P^1}(-8)\). Twisting by \(\mathcal O_{\mathbf P^3}(6)|_{C_0} = \mathcal O_{\mathbf P^1}(24)\) gives the exact sequence
  \[
    0 \longrightarrow \mathcal I_{\mathrm{triple}}(6) \cap \mathcal I_{C_0}^2(6) \longrightarrow \mathcal I_{\mathrm{triple}}(6) \xrightarrow{\;h\;} M(6) \cong \mathcal O_{\mathbf P^1}(16) \longrightarrow 0.
  \]
  In the chart \(x_0 = 1\), any \(F \in V_{\mathrm{triple},6}\) satisfies \(F \equiv h_F(z) m \pmod{I_{C_0}^2}\), so by purity of \(\mathcal I_{C_0}^2\):
  \[
    \ker\bigl(h: V_{\mathrm{triple},6} \to k[z]_{\le 16}\bigr) = V_{\mathrm{triple},6} \cap V_{6,2} = H^0\bigl(\mathcal I_{\mathrm{triple}}(6) \cap \mathcal I_{C_0}^2(6)\bigr).
  \]
  For all three orbits, \(h: V_{\mathrm{triple},6} \to k[z]_{\le 16}\) is surjective of rank \(17\), and the double-sextic intersection \(\ker(h) = V_{\mathrm{triple},6} \cap V_{6,2}\) has dimension \(27 - 17 = 10\).
- **Canonical fourth-order contact on \(\ker(h)\) and the quadric-tangency hyperplane:** Locally, \(\mathcal I_{\mathrm{triple}} \cap \mathcal I_{C_0}^2 = ((q')^2, q'y, y^3) = \mathcal I_{C_0}\cdot \mathcal I_{\mathrm{rib}}\) and \(\mathcal I_{C_0}\cdot \mathcal I_{\mathrm{triple}} = ((q')^2, q'y, y^4)\), with canonical quotient
  \[
    \frac{\mathcal I_{\mathrm{triple}} \cap \mathcal I_{C_0}^2}{\mathcal I_{C_0} \cdot \mathcal I_{\mathrm{triple}}} \cong L^{\otimes 3} = \mathcal O_{\mathbf P^1}(-18), \qquad L^{\otimes 3}(6) \cong \mathcal O_{\mathbf P^1}(6).
  \]
  Thus on \(\ker(h) = V_{\mathrm{triple},6} \cap V_{6,2}\), the cubic-contact map \(\Theta|_{\ker(h)}: \ker(h) \to H^0(L^{\otimes 3}(6)) \cong k[z]_{\le 6}\) (\(\dim = 7\)) is canonically defined with kernel \(\ker(h, \Theta) = H^0(\mathcal I_{C_0}\cdot \mathcal I_{\mathrm{triple}}(6))\), and
  \[
    \operatorname{rank}(h, \Theta) = \operatorname{rank}(h) + \operatorname{rank}\bigl(\Theta|_{\ker(h)}\bigr) = 17 + \operatorname{rank}\bigl(\Theta|_{\ker(h)}\bigr).
  \]
  Along the triple locus \(q' = 0\), the quadric \(q = U + \tfrac{1}{2} z V\) and transverse coordinate \(V = -S_0 m + B(z)y\) restrict to
  \[
    q \equiv \mu(z) y - \nu(z) y^2 \pmod{q'}, \quad V \equiv B(z)y + S_0\gamma(z)y^2 \pmod{q'},
  \]
  where \(\mu(z) := A(z) + \tfrac{1}{2} z B(z)\) and \(\nu(z) := (T_0 - \tfrac{1}{2} z S_0)\gamma(z)\). Via \(0 \to q\cdot H^0(\mathcal I_{C_0}(4)) \to V_{6,2} \to H^0(\mathcal O_Q(0,4)) \to 0\), every \(F \in V_{6,2}\) restricts on \(Q = \{q=0\}\) (where \(x_2/x_0 = z^3 + V\)) to \(P(z^3+V)V^2 = \alpha_0(z)V^2 + \beta_0(z)V^3 + O(V^4)\) for \(P(w) \in k[w]_{\le 4}\), so \(\alpha_0(z) = P(z^3)\) and \(\beta_0(z) = P'(z^3)\) satisfy the chain-rule identity \(\alpha_0'(z) = 3 z^2 \beta_0(z)\). Expanding \(F \equiv \alpha_2(z)q^2 + \alpha_1(z)qV + \alpha_0(z)V^2 + \beta_3(z)q^3 + \beta_2(z)q^2 V + \beta_1(z)q V^2 + \beta_0(z)V^3 \pmod{I_{C_0}^4}\), vanishing of the \(y^2\) coefficient modulo \(q'\) is \(\alpha_2\mu^2 + \alpha_1 B\mu + \alpha_0 B^2 \equiv 0\). At any root \(z_0\) of \(\mu(z_0) = 0\) with \(B(z_0) \ne 0\), this forces \(\alpha_0(z_0) = 0\) and \(\alpha_1(z_0) = -B(z_0)\frac{\alpha_0'(z_0)}{\mu'(z_0)} = -B(z_0)\frac{3 z_0^2}{\mu'(z_0)}\beta_0(z_0)\), leaving only the \(\alpha_1(z_0)qV + \beta_0(z_0)V^3\) contributions to \(y^3\) modulo \(q'\):
  \[
    -\Theta_F(z_0) = B(z_0)^2\left(\frac{3 z_0^2 \nu(z_0)}{\mu'(z_0)} + B(z_0)\right)\beta_0(z_0).
  \]
  1. For the two **algebraic orbits** \((A,B) = (rz, 1)\) (\(12r^2+4r+3=0\)), \(\mu(z) = (r + \tfrac{1}{2})z\) has no roots in \(k^\times\) and \(\gamma(z) \equiv 0\). Consequently, \(\Theta|_{\ker(h)}: \ker(h) \to k[z]_{\le 6}\) is **surjective of rank \(7\)**, yielding \(\operatorname{rank}(h, \Theta) = 17 + 7 = 24\) and \(\dim \ker(h, \Theta) = 10 - 7 = 3\).
  2. For the **principal orbit** \((A,B) = (1+z, -2-8z)\), \(\mu(z) = 1 - 4z^2 = (1-2z)(1+2z)\) vanishes at \(z_0 = -1/2\) and \(z_0 = +1/2\). At \(z_0 = -1/2\), \(\nu(-1/2) = 0\) and \(B(-1/2) = 2 \ne 0\), so \(-\Theta_F(-1/2) = 8\beta_0(-1/2)\) does not vanish identically. At **\(z_0 = +1/2\)**, \(\mu'(1/2) = -4\), \(\nu(1/2) = -32\), and \(B(1/2) = -6\), so
     \[
       \frac{3(1/2)^2 \nu(1/2)}{\mu'(1/2)} + B(1/2) = \frac{(3/4)(-32)}{-4} - 6 = 6 - 6 = 0 \implies \Theta_F(1/2) = 0 \quad \forall\, F \in \ker(h).
     \]
     Thus \(\operatorname{im}(\Theta|_{\ker(h)}) = \{p \in k[z]_{\le 6} : p(1/2) = 0\}\) has codimension \(1\) (**rank \(6\)**), explaining why \(\operatorname{rank}(h, \Theta) = 17 + 6 = 23\) and \(\dim \ker(h, \Theta) = 10 - 6 = 4\).
- **Universal containment of \(q \cdot V_{\mathrm{triple},4}\) in \(\ker(h, \Theta)\):** Since \(q \in H^0(\mathcal I_{C_0}(2))\) and \(V_{\mathrm{triple},4} = H^0(\mathcal I_{\mathrm{triple}}(4))\), their product \(q \cdot V_{\mathrm{triple},4}\) (\(2\)-dimensional) lies in \(H^0(\mathcal I_{C_0}\cdot \mathcal I_{\mathrm{triple}}(6)) = \ker(h, \Theta)\) for all three orbits.

### 2. Torus weight decomposition of the \(T\)-invariant algebraic orbits

Under the centered \(\mathbf G_m\)-weights \(\operatorname{wt}(x_0, x_1, x_2, x_3) = (-2, -1, 1, 2)\) (uncentered \((0, 1, 3, 4)\)), the affine substitution \(x_0 = 1, x_1 = z, x_2 = z^3 + y, x_3 = z^4 + (r + \tfrac{3}{2})zy + m\) for the algebraic orbits \((A,B) = (rz, 1)\) is strictly homogeneous of uncentered weights \(\operatorname{wt}(z, y, m) = (1, 3, 4)\). Therefore \(I_{\mathrm{alg}}\) is **\(T\)-invariant**, and its source spaces decompose into centered \(T\)-weight subspaces:

- **Degree \(4\) (\(\dim V_{\mathrm{alg},4} = 2\)):** Centered weights \(\{-4, +4\}\) (each \(1\)-dimensional), spanned explicitly by
  \[
    Q_- = (1 - \sqrt{-2}) x_0^2 q - x_1(x_0^2 x_2 - x_1^3), \qquad Q_+ = (1 + \sqrt{-2}) x_3^2 q - x_2(x_1 x_3^2 - x_2^3).
  \]
  Since \((1 - \sqrt{-2})(r + \tfrac{1}{2}) = 1\) for \(r = (-1 + 2\sqrt{-2})/6\), in the chart \(x_0 = 1\) the quartic \(Q_-\) satisfies the exact identity \(Q_-(1, z, z^3+y, z^4+(r+3/2)zy+m) = (1 - \sqrt{-2})m\) with zero pure-\(y\) tail to all orders.
- **Degree \(5\) (\(\dim V_{\mathrm{alg},5} = 11\)):** Centered weights \(\{-6, -5, -3, -2, -1, 0, 1, 2, 3, 5, 6\}\), each of dimension \(1\).
- **Degree \(6\) (\(\dim V_{\mathrm{alg},6} = 27\)):** Centered weights \(w \in [-8, 8]\) with symmetric profile
  \[
    \dim V_{\mathrm{alg},6}[w] = (1, 1, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1) \quad (w = -8, \dots, 8).
  \]
  For any \(F \in V_{\mathrm{alg},6}[w]\), \(h_F(z) = \alpha_F z^{w+8}\) (\(\deg_z h_F = w + 8 \in \{0, \dots, 16\}\)) and \(\Theta_F(z) = -K_F(z) = \beta_F z^{w+3}\) (\(\deg_z \Theta_F = w + 3 \in \{0, \dots, 11\}\) for \(w \ge -3\), and \(\Theta_F \equiv 0\) for \(w \in \{-8, -7, -6, -5, -4\}\)).
- **Endpoint proportionality at \(p_\infty\) and the \(3\)-dimensional joint kernel:** For \(w \in \{4, 5, 6, 7, 8\}\), \(V_{\mathrm{alg},6}[w]\) is spanned modulo \(\ker(h, \Theta)\) by \(M_{w-4} Q_+\) where \(M_{w-4}\) is a monomial quadric of centered weight \(w-4\) restricting to \(z^w\) on \(C_0\). Because \(Q_+ \in (m, y^3)\) has no \(y^1, y^2\) terms, multiplying by \(M_{w-4}\) scales both \(h_{Q_+}\) and \(\Theta_{Q_+}\) by \(z^{w-4}\), locking the top \(5\) coefficients of \(\Theta_F\) to the top \(5\) coefficients of \(h_F\):
  \[
    [\Theta_F]_d = \lambda_0 \, [h_F]_{d+5} \quad \text{for } d \in \{7, 8, 9, 10, 11\}, \qquad \lambda_0 = \frac{28 + 16\sqrt{-2}}{81}.
  \]
  The \(10\)-dimensional double-sextic subspace \(\ker(h) = V_{\mathrm{alg},6} \cap V_{6,2}\) is supported in weights \(w \in [-4, 4]\) with profile \((1, 1, 1, 1, 2, 1, 1, 1, 1)\), and the \(3\)-dimensional joint kernel \(\ker(h, \Theta)\) is supported in weights \(\{-4, 0, +4\}\) (spanned by \(q Q_-\) in weight \(-4\), \(q Q_+\) in weight \(+4\), and a unique weight-\(0\) generator).

### 3. Surface-pair VGIT Plücker cubic-contact map \(\Omega_3\)

On the sub-Grassmannian \(\operatorname{Gr}(2, V_{\mathrm{triple},6}) \subset X_6 = \operatorname{Gr}(2, 59)\), the necessary cubic-contact equation \(h_G \Theta_F - h_F \Theta_G \equiv 0\) is the restriction of the intrinsic bundle map
\[
  \Omega_3: \bigwedge^2 V_{\mathrm{triple},6} \longrightarrow H^0\bigl(M(6) \otimes L^{\otimes 3}(6)\bigr) = H^0\bigl(\mathcal O_{\mathbf P^1}(22)\bigr) \cong k[z]_{\le 22}, \qquad F \wedge G \longmapsto h_F(z) \Theta_G(z) - h_G(z) \Theta_F(z).
\]
- **Cancellation of degrees \(23 \dots 27\) and uniform rank \(23\):** Because \(h_G F - h_F G\) defines a global section of \(M(6) \otimes (\mathcal I_{\mathrm{triple}} \cap \mathcal I_{C_0}^2)(6)\) across \(C_0 \cong \mathbf P^1\), its image in \(M(6) \otimes L^{\otimes 3}(6) \cong \mathcal O_{\mathbf P^1}(22)\) automatically has degree \(\le 22\) in \(z\), explaining why all terms of degree \(> 22\) in \(h_F \Theta_G - h_G \Theta_F\) cancel identically. For **all three orbits** (both principal and algebraic), \(\Omega_3: \bigwedge^2 V_{\mathrm{triple},6} \to k[z]_{\le 22}\) is **surjective of exact rank \(23\)**, cutting out a linear subspace \(\ker(\Omega_3) \subset \bigwedge^2 V_{\mathrm{triple},6}\) of dimension \(\binom{27}{2} - 23 = 351 - 23 = 328\).
- **Diagonal Plücker weight decomposition on the algebraic orbits:** On \(\bigwedge^2 V_{\mathrm{alg},6}\), the centered Plücker weights \(W = w_1 + w_2\) span the \(31\) integers \([-15, 15]\). For \(F \in V_{\mathrm{alg},6}[w_1]\) and \(G \in V_{\mathrm{alg},6}[w_2]\), \(\Omega_3(F \wedge G)\) is a scalar multiple of \(z^{W+11}\). Thus \(\Omega_3\) decomposes diagonally into \(31\) Plücker weight blocks:
  - \(23\) blocks of **rank \(1\)** for \(W \in [-11, 11]\) (mapping onto \(k \cdot z^{W+11}\) for \(W + 11 \in \{0, \dots, 22\}\)), and
  - \(8\) **zero blocks** for \(W \in [-15, -12] \cup [12, 15]\) (where either both \(w_i \le -4\) so \(\Theta = 0\) at \(p_0\), or both \(w_i \ge 4\) so \(\Theta = \lambda_0 z^{-5} h_{\ge 12}\) cancels at \(p_\infty\)).
