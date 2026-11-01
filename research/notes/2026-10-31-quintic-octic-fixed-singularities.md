# Quintic–octic normal defects and fixed carrier singularities

Date: 2026-10-31. Status: **independently reviewed provisional mathematics**,
including the completed even-set exclusion in section 4.2.
No canonical promotion. The [companion review](2026-10-31-quintic-octic-fixed-singularities-audit.md)
records the independent reconstruction and disposition.

The [ADE continuation](2026-10-31-quintic-octic-ade-exclusion.md) removes
the reduced-first-symbol hypothesis from this note's quintic exclusion.
Its separate proof and review cover repeated zeros as well; this note
retains the fixed-singularity geometry and the actual residual controls.

## 1. Question, inherited inputs, and scope

Work over an algebraically closed field of characteristic zero with
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Suppose
\(Y=V(F_5,G_8)\) is proper and \(Y_{\rm red}=C\). All conclusions about
this hypothetical pair are necessary conditions. No such pair is constructed.
An explicit control in section 7 instead has residual support.

Use the following existing results at their recorded scopes:

- [R-0001](../results/quartic_carrier_exclusion.md), including its accepted
  lower-degree/factor reduction: every factor of an STCI equation must itself
  carry C and admit a mate, and its degree is at least five.
- [R-0020](../results/quartic_conormal_characteristic_jump.md):
  \(E=N_C^*=\mathcal O_{\mathbf P^1}(-7)^2\).
- [R-0034](../results/normal_carrier_index_socle.md) and its
  [proof](2026-10-14-generalization-normal-index-socle-theorem.md): the
  ordinary-layer torsion/socle identity and local Cartier-index compatibility.
- The reviewed [genus/torsion proof, sections 2–5](2026-10-26-normal-torsion-spectral-genus-budget.md),
  with its [audit](2026-10-26-normal-torsion-spectral-genus-budget-audit.md),
  identifies the torsion-free ordinary layers with powers of the first line
  quotient and identifies the first-symbol failure divisor. Its general
  explanatory synthesis is not a separate canonical promotion.
- The reviewed [moving-singularity argument, sections 4–5](2026-10-26-44-multiplicity-three-forces.md)
  and [audit](2026-10-26-44-multiplicity-three-forces-audit.md) supply a useful
  local control. Its multiplicity-three conclusion is not transferred to (5,8).

As specified in the question, the hypothetical pair has generic curvilinear
length \(m=10\) and \(p_a(Y)=181\). Write \(K=I_C\mathcal O_Y\),
\(T_i=\operatorname{tors}(K^i/K^{i+1})\), and
\(L=(K/K^2)/T_1=\mathcal O(-q)\). The inherited identities give

\[
\tau=\sum_i\operatorname{length}T_i=45q-190,
\qquad \deg D_{\rm soc}=9q-38,
\qquad \tau_p=5(D_{\rm soc})_p.                 \tag{1}
\]

Thus the three necessary rows are

| q | total ordinary torsion | socle-defect degree |
|---|---:|---:|
| 5 | 35 | 7 |
| 6 | 80 | 16 |
| 7 | 125 | 25 |

The conclusions below locate these defects on actual carrier singularities
and classify the case of a reduced common-singularity divisor. The global
rank bound followed by the even-set argument in section 4 excludes the
subclass with a reduced quintic first-symbol divisor and a globally ADE
quintic. The full degree pair is not excluded.

## 2. The first divisor and the actual octic system

Both F and every \(S_H=G+FH\), \(H\in H^0(\mathcal O_{\mathbf P^3}(3))\),
are integral: the factor reduction above would require each factor to have
degree at least five, impossible for two factors of either degree five or
eight. Also \((F,S_H)=(F,G)\), so the whole scheme, not just its cycle, is fixed.

The quintic has a nonzero first normal symbol. Indeed let
\(Q=x_0x_3-x_1x_2\). If a quintic vanishes to normal order at least two
along C, its restriction to the smooth quadric Q contains \(2C\). Taking
\(C\) of type \((1,3)\), the residual class \((5,5)-2(1,3)=(3,-1)\)
is not effective. Thus Q divides the quintic; smoothness of Q along C then
implies that the quotient cubic contains C. This proves

\[
H^0(\mathcal I_C^2(5))=Q\,H^0(\mathcal I_C(3)).       \tag{2}
\]

Such a quintic is not integral. This argument concerns sheaf powers; no
unsaturated homogeneous-power identification is assumed.

Let \(M=\ker(E\twoheadrightarrow L)=\mathcal O(q-14)\). In its saturated
direction the first symbols of the equations are scalar sections

\[
a\in H^0(\mathcal O(q+6)),\qquad
b\in H^0(\mathcal O(q+18)),\qquad a\ne0.
\]

Put \(B=\gcd(a,b)\), \(\beta=\deg B\), with
\(\gcd(a,0)=\operatorname{div}(a)\). Saturation makes the local direction
nonzero in every fiber, so the scheme of simultaneous singularities
restricted to C is exactly B. The first ordinary torsion is
\(T_1=M/M(-B)\), of length \(\beta\).

In fact

\[
\operatorname{Supp}\Bigl(\bigoplus_i T_i\Bigr)=\operatorname{Supp} B,
\qquad 1\le\beta\le q+6.                            \tag{3}
\]

At a point outside B one carrier is smooth. On that surface the smooth
curve C is Cartier, and sole support forces the mate locally to be a unit
times its tenth power. The ideal is therefore \((x,y^{10})\), so all
ordinary layers are free. Conversely every point of B has nonzero T1.
Equation (1) makes B nonempty. This is a statement about ordinary-layer
torsion; it does not identify that torsion with the different filtered-equation
comparison invariant \(\Delta\) in [R-0030](../results/local_filtration_comparison_defect.md).

The first symbol of \(S_H\) is \(b+ha\), where
\(h=H|_C\in H^0(\mathcal O(12))\). Cubic restrictions fill this whole
space: sums of three exponents from \(\{0,1,3,4\}\) contain every integer
from zero to twelve. After removing B, the linear system spanned by
\(b/B\) and \((a/B)H^0(\mathcal O(12))\) is basepoint free.
A general member has simple zeros, avoids B, and also avoids the zeros
of a outside B. Generic simplicity follows either from curve Bertini in
characteristic zero or directly from value and first-jet separation wherever
\(a/B\ne0\). The affine family with coefficient of b equal to one meets
this open set; the case b=0 is the complete degree-twelve system times a.

Consequently a general octic has on C the fixed divisor B and

\[
N=q+18-\beta\ \ge12                              \tag{4}
\]

distinct moving singular points. All these moving singularities are
\(A_9^1\). To see this, at such a point straighten the smooth quintic to
x; the pair is \((x,y^{10})\), and
\(S_H=xA+y^{10}U\) with \(U\) a unit and \(A|_C\) having a simple zero.
Use A as the curve coordinate and absorb a tenth root of U into y. This
gives \(xt+y^{10}\), preserving C as \((x,y)\).

The degree-eight system is generated by G and the cubic multiples of F,
and has base support exactly C. Bertini makes its general member smooth
off C. Its first-symbol zero set on C is finite, so the general integral
octic has only isolated singularities and is normal. **Rational double
singularities at B do not follow from this argument.**

## 3. A reduced fixed divisor forces two defect types

Assume in this section that B is reduced. At each of its points the general
octic's first normal symbol vanishes to order exactly one. In coordinates
\((t,x,y)\), with \(I_C=(x,y)\), its Hessian therefore contains a nonzero
\(tx\) term. Its quadratic rank is at least two. The formal splitting
lemma and isolation just proved make it an \(A_{r-1}\) singularity.
The split one-variable term cannot vanish identically, since that would
give a curve of singularities.

The surface–curve pair is \(A_{r-1}^1\): in the standard classification of
smooth curves on an A singularity the first-symbol order equals the smaller
end-distance k, and here it is one. See Ellia, Definition 8 and Lemma 10,
[arXiv:1409.3801](https://arxiv.org/html/1409.3801). Equivalently the pair has
formal coordinates

\[
S_H:tu-w^r=0,\qquad C:(u,w)=0.                    \tag{5}
\]

In this normal local surface C has Cartier index r and \(\operatorname{div}(u)=rC\).
Since the actual mate cuts \(10C\), \(r\mid10\), and, up to a unit and
adding a multiple of S_H, its equation is \(u^k\), \(k=10/r\).
The complete intersection at this point is exactly

\[
\mathcal B=k[[t,u,w]]/(tu-w^r,u^k),\qquad rk=10.    \tag{6}
\]

This normal form supplies the higher layers, not just a first-order count.
It is free over \(D=k[[t]]\) on \(u^i w^j\),
\(0\le i<k,\ 0\le j<r\). Its generic curvilinear generator is w, and
\(w^{ri+j}=t^i u^i w^j\). Hence the index of the monomial lattice D[w]
in \(\mathcal B\), equal to the total ordinary-layer torsion by the
inherited lattice proof, is

\[
\tau_p=r\sum_{i=0}^{k-1}i=5(k-1).
\]

The socle generator is \(u^{k-1}w^{r-1}\), while
\(w^9=t^{k-1}u^{k-1}w^{r-1}\); thus \((D_{\rm soc})_p=k-1\).
The case r=10 makes the other carrier smooth and has no defect, so it
cannot occur on B. The case r=1 is smooth. The only fixed types are

| general octic pair | r | local mate | first torsion | total ordinary torsion | socle defect |
|---|---:|---|---:|---:|---:|
| \(A_1^1\) | 2 | \(u^5\) | 1 | 20 | 4 |
| \(A_4^1\) | 5 | \(u^2\) | 1 | 5 | 1 |

Let u now count the fixed A1 points and v the fixed A4 points (these counts
are unrelated to the local coordinate in (5)). Then

\[
4u+v=9q-38,\qquad \beta=u+v\le q+6.                \tag{7}
\]

The exhaustive nonnegative integer possibilities are the eight rows below.
They describe necessary local types and counts, not a realization theorem.

| q | fixed A1: u | fixed A4: v | beta | moving A9 on general octic |
|---|---:|---:|---:|---:|
| 5 | 0 | 7 | 7 | 16 |
| 5 | 1 | 3 | 4 | 19 |
| 6 | 2 | 8 | 10 | 14 |
| 6 | 3 | 4 | 7 | 17 |
| 6 | 4 | 0 | 4 | 20 |
| 7 | 4 | 9 | 13 | 12 |
| 7 | 5 | 5 | 10 | 15 |
| 7 | 6 | 1 | 7 | 18 |

In particular, if every fixed singularity of the general octic is an
ordinary node, then \(q=6\) and there are exactly four fixed nodes.
This conclusion does not require first assuming B reduced: a smooth curve
through an ordinary node has first-symbol order one, so that assumption
then follows. Neither q=5 nor q=7 can be paid for by nodes alone.

## 4. A genuine global bound, with its hypotheses retained

### 4.1 The rank bound leaves one configuration

Impose two additional conditions on the actual quintic:

1. Its first-symbol zero divisor \(\operatorname{div}(a)\) is reduced.
2. The quintic has only rational double points everywhere (smooth points
   allowed), including away from C.

These conditions are not consequences of the STCI hypothesis. They imply
B reduced. At a fixed point write \(F=\epsilon u^k+hS_H\) using (5)–(6),
where \(\epsilon\) is a unit and k is 5 or 2. Simplicity of a forces h to
be a unit. Dividing by h and replacing
\(t\) by \(t+(\epsilon/h)u^{k-1}\) proves that F has the same A1 or A4
pair type there. At every other zero of a the octic is smooth, and the
primitive local calculation from section 2 makes F an A9. Thus the rank
of its exceptional configurations above C is

\[
R_C=u+4v+9(q+6-u-v)=9q+54-8u-5v.                 \tag{8}
\]

For the Hodge calculation, descend the finite defining data to a finitely
generated characteristic-zero field and embed that field into the complex
numbers. For a quintic with only rational double points, its minimal resolution is
crepant and has the same Chern numbers and \(\chi(\mathcal O)\) as a smooth
quintic: \(K^2=5\), \(c_2=55\), \(p_g=4\), and irregularity zero.
Consequently \(h^{1,1}=45\). These hypersurface formulas are also the
ones used in Ellia's Proposition 14. The negative definite exceptional
root lattices, together with the positive-square pullback of a hyperplane,
are independent algebraic classes. Therefore

\[
R_C\le44.                                         \tag{9}
\]

The values of (8) in the eight rows, in order, are
\(64,76;\ 52,64,76;\ 40,52,64\). Exactly one row survives:

\[
\boxed{q=7,\quad 4A_1+9A_4\text{ on the quintic along C},
\quad\beta=13.}                                   \tag{10}
\]

Its general octic has those fixed types and twelve moving A9 points.
Additional quintic exceptional rank off C is at most four. This is the
only configuration left by the rank bound under the two extra conditions.
The actual integral divisor relation eliminates it as follows.

### 4.2 Picard divisibility and a double cover eliminate the last row

Let \(\pi:X\to S=V(F_5)\) be the minimal resolution, let H denote the
pulled-back hyperplane class, and write \(\widetilde C\) for the strict
transform of C. The actual octic cuts the Cartier divisor \(10C\), so
\(10C\sim8H\) on S. Label each A4 chain so that \(\widetilde C\) meets
its first end. The rational pullback of C has correction \(E/2\) at an
A1 point and
\((4E_1+3E_2+2E_3+E_4)/5\) at an A4 point. These coefficients follow
by imposing zero intersection with every exceptional curve. For example,
the latter coefficient vector has intersections \((-1,0,0,0)\) with
the A4 chain, canceling the intersections of \(\widetilde C\).

Let N be the sum of the four exceptional node curves and let A be the
sum of the integral weighted divisors
\(4E_1+3E_2+2E_3+E_4\) over the nine A4 points. Pulling back the actual
Cartier linear equivalence gives an equality in \(\operatorname{Pic}(X)\):

\[
10\widetilde C+5N+2A\sim8H.
\]

In particular, the integral divisor class

\[
D=4H-5\widetilde C-A-2N
\quad\text{satisfies}\quad 2D\sim N.               \tag{13}
\]

This explicit expression does not divide an equality in the numerical
lattice or assume that \(\operatorname{Pic}(X)\) is torsion free. The four
nodes form an even set in the Picard group. Exceptional curves over points
away from C have coefficient zero in the pullback of \(10C\); they do not
enter (13).

Choose the section of \(\mathcal O_X(2D)\) with divisor N. The algebra
\(\mathcal O_X\oplus\mathcal O_X(-D)\), with multiplication given by
that section, defines a finite double cover \(f:Z\to X\). Its branch
divisor consists of four smooth disjoint curves, so Z is smooth. It is
connected and integral: after rationally trivializing the defining line
bundle, the branch section has odd valuation along each component of N
and cannot be a square in \(k(X)\).

Since \(K_X\sim H\), \(K_X^2=5\), and \(\chi(\mathcal O_X)=5\), while
\(N^2=-8\) and \(H\cdot N=0\), equation (13) gives
\(D^2=-2\) and \(K_X\cdot D=0\). The double-cover formulas yield

\[
\begin{aligned}
\chi(\mathcal O_Z)
 &=2\chi(\mathcal O_X)+\tfrac12D\cdot(D+K_X)=9,\\
K_Z^2&=2(K_X+D)^2=6.
\end{aligned}                                      \tag{14}
\]

Here the Euler-characteristic formula also follows directly from
\(f_*\mathcal O_Z=\mathcal O_X\oplus\mathcal O_X(-D)\) and
Riemann–Roch. The ramification curves \(R_i\) map isomorphically to the
four exceptional node curves. From \(f^*E_i=2R_i\) and \(E_i^2=-2\),
one gets \(R_i^2=-1\). Contract them to a smooth surface
\(\sigma:Z\to W\). They are disjoint, so

\[
\chi(\mathcal O_W)=9,\qquad K_W^2=6+4=10.
\]

Write \(R=\sum R_i\). The tautological section of the cover gives
\(R\sim f^*D\), and the canonical formulas give

\[
\sigma^*K_W\sim K_Z-R\sim f^*K_X=f^*H.             \tag{15}
\]

The right side is nef and big. Thus \(K_W\) is nef and big, W is minimal
of general type, and Noether's inequality applies:

\[
10=K_W^2\ \ge\ 2p_g(W)-4
\ \ge\ 2\chi(\mathcal O_W)-6=12,
\]

a contradiction. The characteristic-zero descent used above may be
performed on the original hypothetical pair before resolving over the
complex numbers. Any finite line-bundle and isomorphism data used in the
cover can likewise be included in the field of definition.

The external inputs are the double-cover construction and canonical formula
in Debarre, [*Inégalités numériques pour les surfaces de type général*,
section 1.4, printed p. 322](https://www.numdam.org/item/10.24033/bsmf.1965.pdf),
and Noether's inequality as stated in the introduction, printed p. 320.
The [1983 addendum](https://www.numdam.org/item/10.24033/bsmf.1990.pdf)
repairs a proof for the stronger irregular-surface theorem 6.1; that theorem
is not used here. The even-set implication (13) and its application to
this STCI configuration are the additional argument, not a result
attributed to Debarre.

**Conditional exclusion.** No hypothetical (5,8) STCI of the fixed C can
have both a reduced quintic first-symbol divisor and a quintic with only
rational double points everywhere. Equivalently, any such STCI must have
a repeated zero in \(\operatorname{div}(a)\), or a quintic singularity
that is not a rational double point, possibly away from C. This does not
imply that the common divisor B is nonreduced. The cover argument also
shows, independently of C, that the resolution of a globally ADE quintic
cannot have an even set consisting of exactly four exceptional node curves.

## 5. Exactly where the primitive singularity argument stops

Ellia's Theorem 12 assumes that the complete-intersection multiple curve is
primitive, meaning locally contained in a smooth surface. His proof uses
the existence, at each point of C, of a smooth member of the containing
system; its singularity incidence is then a graph over C.
[Source, Theorem 12 and proof](https://arxiv.org/html/1409.3801).

Here B is nonempty, and every local equation of Y lies in the square of
the ambient maximal ideal at each point of B: both generators are singular.
No local smooth surface can contain Y there. Every octic G+FH is singular
at those points. In a pencil, the incidence contains the fixed fibers
\(\{p\}\times\mathbf P^1\), in addition to its moving part. Thus the
primitive smooth-member premise and the graph argument fail exactly on B.
Normality of the general octic survives by section 2, but uniform ADE type
and a global ADE singularity bound cannot be imported across B.

Sections 3–4 recover a portion of that strategy by proving the necessary
local hypotheses separately, then using the actual Picard relation to
construct the forbidden cover. The torsion total itself is not a surface
singularity bound.

## 6. What the numerical and local controls do establish

The two algebras (6) are actual supported complete intersections of length
ten in a formal smooth threefold. They realize total torsion 20 and 5 at
one reduced common-singularity point. In particular, each eight-row budget
can be paid arithmetically by local models of the correct multiplicity.
This supplies local flexibility and disproves the proposed inequality
\(\tau\le\operatorname{length}(B)\). It does not disprove every possible
bound with an additional factor or further geometric hypotheses.

It does not glue those algebras on the fixed projective C, produce global
degree-five/eight equations, or establish the prescribed line quotient.
The inherited control \(4C\) on the smooth quadric already shows why a
normal algebra and the right genus need not give equations of the required
degrees; see [the genus note, sections 8–10](2026-10-26-normal-torsion-spectral-genus-budget.md).

Even in the reduced-B case, the usual octic A-singularity inequality does
not discard a row. Its weighted sum is
\[
\tfrac32u+\tfrac{24}{5}v+\tfrac{99}{10}(q+18-u-v),
\]
whose eight values are \(192,204;180,192,204;168,180,192\), all below
\(2\cdot8\cdot7^2/3=784/3\). This is a direct check of a valid bound under
the ADE conclusions of section 3, not evidence that the rows are realizable.

## 7. Actual homogeneous equations exhibit the missing higher-jet control

There is also a simple proper pair of exactly the requested degrees that
shows why arbitrary fixed points cannot automatically be assigned ADE types.
It is deliberately a **residual-support control**, not an STCI candidate.
Put

\[
A=x_0^2x_2-x_1^3,\quad Q=x_0x_3-x_1x_2,\qquad
F=x_1^2 A+x_3 Q^2,\quad G=A^2Q.                    \tag{11}
\]

These homogeneous equations have degrees five and eight and contain C.
Neither A nor Q divides F, so they have no common factor and form a proper
complete intersection. On \(x_0=1\), use the polynomial coordinates

\[
t=x_1,\quad x=x_2-t^3=A,\quad y=x_3-tx_2=Q.
\]

Then C is \((x,y)=0\) and

\[
F=t^2x+(t^4+tx+y)y^2
  =t(t+y^2)x+y^2(t^4+y),\qquad G=x^2y.             \tag{12}
\]

F is integral: its coefficient and constant term as a linear polynomial
in x are relatively prime in \(k[t,y]\), and its homogenization has no
x0 factor. At \(p=[1:0:0:0]\), both F and G have ambient multiplicity
three. For every cubic H, \(G+FH\) has no quadratic term there. Hence
every member is worse than a rational double point at p. Its first-symbol
common divisor on C has order two at this point.

The first symbol of F is \(x_1^2\sigma_A\), and that of G is zero.
The saturated first direction of A has quotient \(\mathcal O(-7)\): on
the finite chart its first symbol is x; at infinity, in coordinates
\(c=x_2/x_3, X=x_0/x_3-c^4, Y=x_1/x_3-c^3\), it is
\(2c^5X-3c^6Y\), with common order five. Thus its saturated line has
degree \(-12+5=-7\). This is an actual q=7 first-direction control.

Generically t is invertible. Eliminating x from (12) gives
\(x=-t^2y^2+O(y^3)\), so \(G\) has order five. The intersection cycle is
\(5C+R\), with \(\deg R=40-20=20\). Residual support is real: the line
\(x_1=x_3=0\), locally \(t=y=0\), lies in both surfaces and passes
through p. No multiplicity-ten defect or sole-support conclusion is claimed
for this control. The equations show directly that the first direction and
degree bounds alone do not supply the missing ADE hypothesis; residual
exclusion remains an essential extra condition.

## 8. Disposition and remaining boundary

This stage yields a completed conditional exclusion and explicit controls.
For an arbitrary hypothetical (5,8) pair, all required ordinary torsion is
at fixed common singularities, and a general normal octic has at least twelve
moving A9 points. Reduced B admits just the eight fixed-type rows above.
Under a reduced quintic first-symbol divisor and a globally ADE quintic,
the rank bound leaves only the \(q=7,4A_1+9A_4\) row, and the even-set
double cover excludes that row too. The two-hypothesis subclass is empty.

The full quintic first-symbol divisor may have repeated zeros even when
B is reduced. The subsequent
[ADE continuation](2026-10-31-quintic-octic-ade-exclusion.md), with its
[separate audit](2026-10-31-quintic-octic-ade-exclusion-audit.md), now also
excludes repeated zeros when the quintic is globally ADE. Its double-cover
canonical-map bound and embedded-triple obstruction are additional arguments,
not consequences of the rank calculation in this note. Quintics with worse
singularities remain outside the combined exclusion. That boundary is not a
construction mechanism merely because it survives; the residual-support
control (11) does not realize a supported intersection. The unrestricted
characteristic-zero STCI question, and even the entire (5,8) degree pair,
remain open. No neighboring degrees are studied.

All new evidence consists of the displayed proofs, finite arithmetic, and
explicit polynomial identities. No computational search, inherited proof
rerun, or new canonical promotion is asserted. The fresh independent reviewer
reconstructed the local pair classification, global bound, eight rows, and
residual nature of (11). The [audit](2026-10-31-quintic-octic-fixed-singularities-audit.md)
accepts these scoped claims with no unresolved material finding. The lead
corrected three octic weighted sums and adopted the reviewer's clarification
that the local examples refute only the stated inequality
\(\tau\le\operatorname{length}(B)\), not every possible boundary bound.

The even-set continuation in section 4.2 was supplied in the user's
October 31 reply. Its reported external review was not treated as repository
acceptance: the mathematical reviewer independently reconstructed the
Picard divisibility, connected cover, contraction, and Noether contradiction.
The same companion audit accepts the integrated continuation under the
two stated hypotheses, with no unresolved material condition.

### Source-state and integration boundary

This work was developed in the detached d121 worktree at
`9d734e1b03dc2de1faf3d2497ce2916cec5c4dac`. That commit is an ancestor of
`43cf8b378872112e7cb10fa0d80bba7c52894833`, the later research commit
mentioned in the supplied reply. A read-only comparison found the actual
R-0001, R-0020, R-0034 records and the linked genus/torsion and moving-singularity
proof inputs unchanged. The later commit adds research, navigation, and
geometric-contribution guidance. Its unrestricted status remains open.
The subsequent local research head `ffe97dae929a12089e36694b20418a209b843240`
adds a root-algebra/contact-budget checkpoint without changing those
dependencies or resolving this degree pair.

This note and audit, and the subsequent ADE continuation and its audit,
were initially saved as local uncommitted evidence. All four were subsequently
preserved byte-for-byte in commit `fd9e628` on the characteristic-zero research
branch. The [lane closeout](2026-10-31-quintic-octic-closeout-and-interfaces.md)
records their committed preservation, the broader carrier boundary and the
separate cleanup integration state. No canonical promotion is asserted.
Integration must preserve the receiving branch's newer navigation; the older
INDEX file must not replace it.
