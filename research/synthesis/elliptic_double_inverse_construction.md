# An actual elliptic double inverse on a quadric normalization

Fix an algebraically closed field of characteristic zero and the embedded
curve \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). The construction
below produces a smooth quadric mapping finitely and birationally onto an
integral octic, with an elliptic curve mapping two-to-one onto \(C_0\).
Its tested member has an additional isolated inverse scheme of projective
length twelve, so that particular octic has no mate in any degree. The full
five-parameter support and descent loci remain uncomputed.

The global sections, fixed normalization, inverse-scheme length, normal
geometry and fixed-member rejection have independent source review. These
are reviewed provisional statements, not canonical promotion. The exact
[Macaulay2 source](../computations/stci_game_existence_2026_10_30.m2) and
[complete saved output](../computations/stci_game_existence_2026_10_30.txt)
are retained from commit `b271fc5bf20a6920b1540cabd57f095139d8d7a5`.
Their execution and the independent October 31 existence audit are reused;
this integration did not rerun the calculation. The unrestricted
characteristic-zero STCI question remains open.
Independent preservation review accepted this integrated proof, including
all section rows, full scheme/support tests, rank strata and conditional filters.

## 1. The torsion discrepancy supplies actual quadratic sections

Work first over \(\mathbf Q(i)\), \(i^2=-1\). On
\[
 E:y^2=x^3-x,
 \qquad T=(i,1-i),\quad P=(0,0),\quad O=\infty,
\]
the tangent at \(T\) has slope \(-1-i\) and equation
\(y+(1+i)x=0\). Its third intersection is \(P\), so \(2T=P\).
Since \(P\ne O\) has order two, \(T\) has order four. Put
\[
 M=\mathcal O_E(4O),\qquad L=\mathcal O_E(O+T).
\]
The discrepancy \(L^2M^{-1}\) is the nonzero two-torsion class \(2T\):
\[
 L^4=M^2,\qquad L^2\ne M.
\tag{1}
\]
Thus the embedding bundle and the degree-two pencil become compatible
after squaring, without already being identical in degree four.

The function
\[
 A=\frac{y+1-i}{x-i}
\]
has simple poles exactly at \(O,T\); the apparent pole at \(-T\)
cancels. The tangent divisor and the divisor of \(x\) are
\[
 \operatorname{div}(y+(1+i)x)=2T+P-3O,\qquad
 \operatorname{div}(x)=2P-2O.
\]
Consequently
\[
 \phi=\frac{(y+(1+i)x)^2}{x}
      =x^2+2ix-1+2(1+i)y,
 \qquad\operatorname{div}(\phi)=4T-4O.
\]
For \(j=0,1,3,4\), the functions \(\phi A^j\) have no poles away
from \(O\) and pole order at most eight there. They are actual sections
of \(M^2\). At \(T\), and at \(O\) when viewed as sections of
\(8O\), their orders are \(4-j\). Hence they have no common zero and
define the degree-two morphism
\[
 E\longrightarrow C_0,\qquad [1:A:A^3:A^4],
\tag{2}
\]
including the pole points in the appropriate local frame.

The embedding by \(|M|\) is
\[
 Z=(Z_0:Z_1:Z_2:Z_3)=(1:x:y:x^2),
\]
with homogeneous ideal
\[
 Q_0=Z_0Z_3-Z_1^2,\qquad
 Q_1=Z_2^2-Z_1Z_3+Z_0Z_1.
\tag{3}
\]
For the ordered quadratic basis
\[
 (Z_0^2,Z_0Z_1,Z_0Z_2,Z_0Z_3,
   Z_1Z_2,Z_1Z_3,Z_2Z_3,Z_3^2),
\]
the sections in (2) have the following global representatives:
\[
\begin{aligned}
 V_0&=(-1,\ 2i,\ 2+2i,\ 1,\ 0,\ 0,\ 0,\ 0),\\
 V_1&=(-1-i,\ i-1,\ 3i,\ 2+2i,\ 1,\ 0,\ 0,\ 0),\\
 V_3&=(2-2i,\ -1-i,\ -2,\ 3i-3,\ 5i,\ 2+2i,\ 1,\ 0),\\
 V_4&=(4,\ -4i,\ 0,\ -5,\ 4i-4,\ 6i,\ 2+2i,\ 1).
\end{aligned}
\tag{4}
\]
Here each row denotes coefficients, not projective point coordinates.
The exact script solves the four identities
\(V_j(1,x,y,x^2)(x-i)^j=\phi(y+1-i)^j\) modulo
\(y^2-x^3+x\), in the eight-dimensional basis of \(H^0(E,8O)\),
and asserts every identity. Thus (4) supplies ambient scalar coefficients,
rather than rational normal data over \(k(C_0)\).

## 2. The complete five-parameter lifting family and its symmetry

Let
\[
 S_\mu=V(Q_1+\mu Q_0),\qquad
 \Gamma=E\subset S_\mu,\qquad H=\mathcal O_{S_\mu}(2).
\]
The determinant of the quadratic form is a nonzero scalar multiple of
\(\mu(\mu^2-1)\). Thus the finite smooth-pencil locus is
\(\mu(\mu^2-1)\ne0\); the member at infinity is singular. Over the
algebraic closure a smooth member is \(\mathbf P^1\times\mathbf P^1\),
with \(H=(2,2)\) and \(\Gamma\sim H\).

Every lift of the four fixed sections (4) to this member is
\[
 U_j=V_j+\rho_jQ_0,\qquad j=0,1,3,4.
\tag{5}
\]
Indeed quadrics vanishing on \(E\) are spanned by \(Q_0,Q_1\);
modulo \(Q_1+\mu Q_0\) their kernel is the one-dimensional span of
\(Q_0\). This proves completeness of the four lifting parameters for
these particular sections, elliptic curve and pencil. It does not classify
all elliptic inverse curves. In particular
[R-0002](../results/cartier_singleton_lift.md) assumes an inverse curve
mapping isomorphically onto \(C_0\); it does not classify (2).

The deck involution \(R\mapsto T-R\) preserves \(M\), and hence
extends linearly to the containing projective space. A representative is
\[
 \mathsf M=
 \begin{pmatrix}
 -1&2i&2i+2&1\\
 -i&2&0&i\\
 1-i&0&0&1-i\\
 1&-2i&2i+2&-1
 \end{pmatrix}.
\]
The independently checked substitutions are
\[
 \mathsf M^2=8I,\qquad
 Q_0(\mathsf MZ)=8iQ_1(Z),\qquad
 Q_1(\mathsf MZ)=-8iQ_0(Z).
\]
It sends \(S_\mu\) to \(S_{-1/\mu}\). Only \(\mu=\pm i\)
are fixed, and \(S_2\) is not. A deck symmetry of the marked elliptic
curve therefore does not force a symmetry of every chosen source surface.
Even on invariant members one must separately test the actual coordinate
sections before deducing a nonbirational surface map.

## 3. A finite birational octic with an extra inverse scheme of length twelve

Take \(\mu=2\) and all \(\rho_j=0\). The exact source checks
smoothness and computes
\[
 (Q_1+2Q_0,V_0,V_1,V_3,V_4):
 (Z_0,Z_1,Z_2,Z_3)^\infty=(1).
\]
The sections therefore define a morphism. Its pullback hyperplane bundle
is the ample \(H\); a positive-dimensional projective fiber would contain
a curve of zero \(H\)-degree. Thus the map is finite onto its image.
The kernel of the target ring map is prime, since the source is integral;
the saved computation gives one generator of degree eight. The degree
formula
\[
 H^2=8=\deg(f)\deg(f(S_2))
\]
then gives generic degree one. The smooth source is the normalization of
an actual integral octic, independently of the support test that follows.

Use every generator of the fixed quartic ideal. On the affine slice
\(Q_0=1\) the full off-\(\Gamma\) inverse ideal is
\[
\begin{aligned}
 J_2=(&Q_1+2Q_0,Q_0-1,
 V_0V_4-V_1V_3,\\
 &V_1^3-V_0^2V_3,
 V_1^2V_4-V_0V_3^2,
 V_3^3-V_1V_4^2).
\end{aligned}
\tag{6}
\]
Its quotient is zero-dimensional of length 24. On the affine cone over
the projective complement, normalizing the nonzero quadratic \(Q_0\)
to one gives a finite étale \(\mu_2\)-torsor: each scalar orbit has two
representatives. Therefore length divides by two, including for a
nonreduced scheme. The projective extra inverse scheme has length twelve.
Neither twelve distinct points nor twelve distinct target images is asserted.

This one octic has no mate in any degree. If an ambient mate existed,
its nonzero pullback would be a section of \(bH\) whose zero support is
exactly \(\Gamma\) together with the nonempty isolated extra scheme.
A principal nonzerodivisor on a smooth surface gives an effective Cartier
divisor of pure codimension one; it cannot have isolated zero support
away from its curve support. This contradiction uses the full inverse
scheme, and does not itself require the birationality calculation.
Raising the mate degree cannot change the inverse support of this fixed map.

## 4. The actual first symbol records a different boundary defect

For the implicit octic \(F\), substitute
\((x_0,x_1,x_2,x_3)=(1,t,t^3+n,t^4+m)\). Its least total
\((n,m)\)-degree is two. The gcd \(h(t)\) of the three quadratic
coefficients has degree twelve. The separate infinity substitution
\((s^4+m,s^3+n,s,1)\) gives coefficient-gcd order zero at \(s=0\).
Hence the full vertical first-symbol divisor on \(C_0\) has degree twelve.
This is a divisor of actual coefficient sections, invariant under an
invertible change of normal frame.

By [R-0020](../results/quartic_conormal_characteristic_jump.md), the full
quadratic symbol has class \((18,2)\) on the balanced exceptional
\(\mathbf P^1\times\mathbf P^1\). Dividing by its vertical coefficient
gcd leaves horizontal class \((6,2)\), of arithmetic genus five.
The exact squarefree decomposition of its discriminant has odd part of
degree four. The quadratic extension is consequently irreducible, branched
at four points with no additional odd branch at infinity, and has elliptic
normalization. The root itself is singular, with total delta invariant four.
Neither the inverse elliptic curve nor this singular exceptional root is
an automatic instance of a saturated smooth-root obstruction.

The saved output prints the full monic \(h\), so no separate coefficient
certificate is needed here. Let
\(\widetilde h(W_0,W_1)=W_0^{12}h(W_1/W_0)\). In the full quotient
by (6), the script verifies that \(V_0\) is invertible and
\[
 \widetilde h(V_0,V_1)=0.
\]
The morphism of the entire extra inverse scheme to the target curve
therefore factors through \(h=0\), and this factorization descends through
the free \(\mu_2\)-cover. This is scheme-theoretic containment of its
target image in the vertical divisor. Equal numerical degrees twelve
do not prove equality of those image schemes, reducedness or multiplicity
one. Nor does this example prove that every vertical exceptional divisor
creates residual or isolated support downstairs.

## 5. Fiberwise support and actual descending equations

The literal parameter ring is
\[
 B=\mathbf Q(i)[\mu,\rho_0,\rho_1,\rho_3,\rho_4],
 \qquad R=B[Z_0,Z_1,Z_2,Z_3].
\]
Retain \(\mu(\mu^2-1)\ne0\). For every geometric parameter point,
the required conditions concern the actual specialized fiber:

1. The projective basepoint ideal
   \((Q_1+\mu Q_0,U_0,U_1,U_3,U_4):
   (Z_0,Z_1,Z_2,Z_3)^\infty\) is the unit ideal. Finiteness then follows
   from ampleness as above.
2. The image ideal under \(W\mapsto(U_0,U_1,U_3,U_4)\) has degree eight.
   The finite map then has degree one. Other image degrees are outside this
   octic-normalization subproblem.
3. The specialized ideal
   \[
   \begin{aligned}
   J_p=(&Q_1+\mu Q_0,Q_0-1,U_0U_4-U_1U_3,\\
       &U_1^3-U_0^2U_3,U_1^2U_4-U_0U_3^2,U_3^3-U_1U_4^2)_p
   \end{aligned}
   \tag{7}
   \]
   is the unit ideal. This is exactly absence of inverse points outside
   \(\Gamma\). There is no further saturation by \(Q_0\) on this slice.
   Equivalently use the homogeneous inverse ideal saturated by
   \(Q_0^\infty\) and by the irrelevant ideal. Computation over
   \(\operatorname{Frac}(B)\) tests only the generic fiber; all exceptional
   constructible support and rank strata must remain.
4. For a mate degree \(b>0\), require exact global membership
   \[
   Q_0^b\in\operatorname{span}_k
   \{U_0^{e_0}U_1^{e_1}U_3^{e_3}U_4^{e_4}:
      e_0+e_1+e_3+e_4=b\}
   \quad\text{in }k[Z]/(Q_1+\mu Q_0).
   \tag{8}
   \]

For the equivalence in item 4, a sole-support mate pulls back to a divisor
\(n\Gamma\sim bH\). Since \(\Gamma\sim H\) and \(H^2=8>0\),
intersection gives \(n=b\). Proper integrality makes any two sections
with divisor \(b\Gamma\) scalar multiples, yielding (8). Conversely
(8) constructs an actual homogeneous equation and forces absence of extra
inverse support: its pullback zeros are exactly \(b\Gamma\). This is
coordinate-subalgebra membership, retaining all conductor descent data;
a reduced phase or Picard condition does not replace it.

There is a finite exact matrix at each chosen degree. Reduce forms by
\[
 Z_2^2=Z_1Z_3-Z_0Z_1-\mu(Z_0Z_3-Z_1^2).
\]
The monomials of degree \(2b\) with \(Z_2\)-exponent at most one form
a basis of size \((2b+1)^2\). The degree-\(b\) monomials in the
\(U_j\) are columns; append the column of \(Q_0^b\). For \(b=6\)
the two matrix sizes are \(169\times84\) and \(169\times85\);
for \(b=8\) they are \(289\times165\) and \(289\times166\).
Membership means equal ranks. On original rank \(s\), impose all augmented
\((s+1)\)-minors and require at least one original \(s\)-minor nonzero.
Inverting one convenient maximal minor does not cover the remaining strata.
No universal degree-six or degree-eight matrix computation is claimed.

## 6. Low-degree filters and the constructive question that remains

Suppose a member's actual implicit octic has exact normal order two and
irreducible quadratic initial form over \(k(C_0)\). A quintic of normal
order one has a coprime linear initial form and generic local intersection
length two, whereas sole support requires \(8\cdot5/4=10\). A quintic
of order at least two has a forced factor of the unique containing quadric
\(q\), by the [global sheaf-power calculation](../supplements/ACTUAL_EQUATION_SPACES.md)
since \(5<3\cdot2\). The octic's restriction to \(q\) has class
\((8,8)\), which cannot be a multiple of \(C_0\) of class \((1,3)\).
Thus the \(q\)-factor retains residual support. This excludes degree five
only on that verified first-form locus. The fixed member satisfies it,
but already fails the stronger full-support test.

A related equal-degree control needs an additional hypothesis: suppose the
irreducible quadratic symbol of an octic is saturated. For a degree-eight
mate, normal order one gives coprime initial forms and length two, less
than the required \(8\cdot8/4=16\). Normal order at least three forces
a factor \(q\), since \(8<3\cdot3\), and retains the residual intersection
with \(q\) as above. At normal order two, length greater than four requires
the two quadratic initial forms to have a common factor. Irreducibility
then makes them proportional over \(k(C_0)\). Saturation means that the
coefficients of the first symbol have no common zero anywhere on
\(\mathbf P^1\), so their proportionality ratio has no poles. Both
symbols have the same coefficient bundle; the ratio is consequently a
global regular function on \(\mathbf P^1\), hence a scalar. Subtracting
that actual scalar multiple of the first octic raises the second's normal
order to at least three while preserving their intersection ideal.
The forced-quadric argument again gives a residual curve. Thus all three
normal-order cases exclude degree-eight sole support in this saturated scope.
The fixed construction has a degree-twelve vertical divisor, so this
scalar-subtraction argument does not discard it or its defective family.
On degenerate-leading parameter strata the actual order and factorization
must be computed before either filter is used.

The first unresolved implication is whether the support-unit locus (7)
meets the smooth, basepoint-free, birational locus. Only then is a descending
pure power in (8) a constructive target. An alternative would be a uniform
obstruction covering this entire five-parameter source. The fixed rejection
supplies neither answer, and cannot be repaired by increasing \(b\).

The involution quotient, described as a degree-four join of two conics in
\(\mathbf P^5\), suggests another geometric model for studying the source
quadrics and a residual inverse curve. Its required residual class and
scheme saturation have not been computed; no universal residual floor
follows. The value of (1)–(8) is an actual higher-degree inverse construction
and a precise geometric support/descent problem, rather than a forced claim
of STCI existence or nonexistence. These exact number-field equations and
saved characteristic-zero calculations assert no uniform reduction modulo
primes or positive-characteristic family theorem.
