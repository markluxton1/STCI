# An actual elliptic double inverse on a quadric normalization

Fix an algebraically closed field of characteristic zero and the embedded
curve \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). The construction
below produces a smooth quadric mapping finitely and birationally onto an
integral octic, with an elliptic curve mapping two-to-one onto \(C_0\).
Its tested member has an additional isolated inverse scheme of projective
length twelve, so that particular octic has no mate in any degree.
The [support test](#a-length-twelve-scheme-testing-every-basepoint-free-fiber)
extends to every smooth basepoint-free fiber. The [center-line calculation](#the-characteristic-zero-center-line)
excludes every eligible fiber on one characteristic-zero line. The
[generic node calculation](#the-generic-double-branch-has-conductor-coefficient-one)
excludes mates of degree at most five for every birational octic in the
family. Full inverse support and higher-degree descent elsewhere remain open.

The global sections, fixed normalization, inverse-scheme length, normal
geometry and fixed-member rejection have independent source review. These
are reviewed statements. The exact
[Macaulay2 source](https://github.com/markluxton1/STCI/blob/5884d52e5fe0e9fd0885645d277e22c640e00d38/research/computations/stci_game_existence_2026_10_30.m2) comes
from commit `b271fc5bf20a6920b1540cabd57f095139d8d7a5`. Its execution and
the independent October 31 existence audit are reused. The retirement replay
matched the [historical output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/stci_game_existence_2026_10_30.txt). The unrestricted
characteristic-zero STCI question remains open.
The review status of the extension to every smooth basepoint-free fiber
is recorded with [R-0076](../../results/elliptic_inverse_support.md#review).

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
[R-0002](../../results/cartier_singleton_lift.md) assumes an inverse curve
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

By [R-0020](../../results/quartic_conormal_characteristic_jump.md), the full
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
alone do not prove equality of those image schemes, reducedness or
multiplicity one; the [cycle identity and squarefree check](#the-vertical-divisor-counts-the-residual-inverse-scheme)
below supply those conclusions for this fixed member. Nor does this example prove that every vertical exceptional divisor
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

### A length-twelve scheme testing every basepoint-free fiber

Fix any smooth source quadric \(S=S_\mu\) and basepoint-free sections
in (5). Write \(M=\mathcal O_S(1)\), \(H=M^2\), and let \(f\) be their
finite map. The target quadric \(Q\) has coordinates
\([u_0v_0:u_1v_0:u_0v_1:u_1v_1]\). If the entire image lay on that
quadric, the pullbacks of its rulings would be nef of square zero with
sum \((2,2)\). They would have classes \((2,0),(0,2)\), both of
degree four on \(E\). The map (2) has ruling degrees two and six.
Thus \(q(U)=U_0U_4-U_1U_3\) cuts a divisor \(Y=E+D\), where
\(D\sim H\) is cut by \(d=q(U)/Q_0\).

Let \(A,B\) be the pulled-back ruling bundles on \(Y\), in that order.
Their product is \(H|_Y\). Let \(X=f(S)\) be the integral image
hypersurface of degree \(e\), and let \(r=[k(S):k(X)]\), so
\(re=H^2=8\). The Cartier divisor \(Y\) on \(S\) is the pullback
of \(X\cap Q\) on \(X\). Pushforward of Cartier divisor cycles gives
\(f_*[Y]=r[X\cap Q]\) as cycles on \(Q\). The equation of \(X\)
restricts to a section of \(\mathcal O_Q(e,e)\) cutting out \(X\cap Q\).
Thus the two ruling degrees on \(Y\) are \((8,8)\).
[Cartier divisor pushforward, Stacks Project, Lemma 42.26.3](https://stacks.math.columbia.edu/tag/02ST)

Degrees on a curve are the sums of the degrees on its integral
components weighted by their generic lengths. Subtracting the ruling
degrees \((2,6)\) on \(E\) gives \((6,2)\) on \(D\). Write
\([D]=\sum_i m_i[C_i]\) with distinct integral curves \(C_i\) and
multiplicities \(m_i\ge1\). Finiteness gives integral image curves
\(T_i=f(C_i)\) and degrees \(\delta_i=[k(C_i):k(T_i)]\ge1\).
In particular
\[
 2=\deg_D B=\sum_i m_i\delta_i\deg_{T_i}\mathcal O_Q(0,1).
\]
Every summand is nonnegative. If \(T_i=C_0\), its summand is
\(3m_i\delta_i\ge3\), since the second ruling has degree three on
\(C_0\). This is impossible, and in particular \(E\) is no component
of \(D\). [Degree on a proper curve, Stacks Project, Lemma 33.44.6](https://stacks.math.columbia.edu/tag/0AYW)

On the target quadric the graph of \(C_0\) has equation
\(u_0^3v_1-u_1^3v_0=0\). Its pullback to \(Y\) is zero on \(E\).
The ideal of \(E\) in \(E+D\) is \(\mathcal O_D(-E)\), with its
inclusion into \(\mathcal O_Y\) given by multiplication by \(Q_0\).
Dividing the pullback by \(Q_0\) therefore gives
\(s'\in H^0(D,A^2|_D)\), using \(AB=H|_Y\) and \(\mathcal O_S(E)=H\).
The generic point of each \(C_i\) lies outside \(E\) and maps outside
\(C_0\), so \(s'\) is nonzero on the residue field there. As an effective
Cartier divisor on the smooth surface \(S\), \(D\) is a
Cohen–Macaulay curve whose associated points are precisely these
generic points, including when \(D\) is nonreduced. Thus \(s'\) is a
nonzerodivisor and defines an effective Cartier zero scheme \(Z\) on
\(D\). The sequence
\[
 0\longrightarrow\mathcal O_D\xrightarrow{s'} A^2|_D
   \longrightarrow A^2|_Z\longrightarrow0
\]
gives \(\operatorname{length}(Z)=\deg_D(A^2)=2\cdot6=12\).
Off \(E\), \(Q_0\) is invertible and \(Y=D\), so \(Z\) there is
scheme-theoretically the inverse of \(C_0\). **Full inverse support is
equivalent to \(|Z|\subset E\).** The extra inverse scheme is the
portion of \(Z\) away from \(E\).

#### The support locus is a nilpotence locus inside a proper norm divisor

Work over an algebraically closed characteristic-zero field and let U be
the nonempty open subset of the five-parameter space where the source
quadric is smooth and the four sections are basepoint-free. No birationality
assumption is needed for the support calculation in this paragraph.
The original member belongs to U. The relative constructions above produce
D and its residual zero scheme Z over U, and

    pi:Z -> U is finite flat of degree twelve.

Here is the family justification, rather than an inference from sampled
ranks. The universal source surface is smooth over U. The section d is a
nonzerodivisor on every surface fiber, as proved above, so D is a relative
effective Cartier divisor and is flat over U. The section s' is a
nonzerodivisor on every D fiber, including reducible and nonreduced fibers.
The fiberwise Cartier criterion therefore makes Z flat over U. Its fibers
have length twelve by the preceding degree calculation. It is proper and
quasi-finite over U, hence finite; finite flatness gives rank twelve.
The bundles and the section s' are relative: the two ruling bundles are
pulled back along Y->Q, and division by Q0 uses the same Cartier divisor
sequence as on each fiber.

Put L=M^2|Z, so Q0 restricts to a section of L. Multiplication by this
section is a map between rank-twelve vector bundles on U,

    pi_*O_Z --Q0--> pi_*L.

Its determinant is the norm section in
`det(pi_*L) tensor det(pi_*O_Z)^(-1)`. At a geometric parameter point it
is nonzero exactly when Q0 is a unit at every point of the finite scheme
Z, equivalently Z is disjoint from E. The original member has all twelve
units of length away from E, so this norm section is nonzero there.
Since U is integral, its zero scheme is a proper effective Cartier divisor
(or empty). Thus a dense open subset of the **whole five-parameter family**
has Z disjoint from E and fails full inverse support. Every possible
full-support fiber lies in this proper norm-divisor locus. This is a
restriction on the remaining parameter locus, not its exclusion.

The norm detects whether *some* residual inverse point meets E; it does
not detect whether *all* of them do. Locally on U one can trivialize L
over the finite scheme Z: choose a generator on the finite Artin fiber,
lift it, and shrink the base so that it remains a generator. Then Q0 is
an element q of the rank-twelve finite algebra pi_*O_Z. At geometric
points the following conditions are equivalent:

- all of Z is supported on E;
- q is nilpotent;
- the characteristic polynomial of multiplication by q is t^12.

The last equivalence follows because an Artin algebra element is nilpotent
exactly when it lies in every maximal ideal; equivalently all eigenvalues
of its multiplication operator vanish. Cayley--Hamilton then gives
q^12=0. Consequently, besides the determinant, all the other eleven
characteristic coefficients must vanish. These are algebraic conditions
on each such local trivialization, not independent conditions whose
codimension is asserted to be twelve.

There is also a global formulation without choosing that trivialization:
Q0^12 is a section of the rank-twelve bundle pi_*(M^24|Z), and its zero
locus has exactly the geometric full-support fibers. This is the intrinsic
length-twelve quotient behind the degree-24 matrix test (9). The possible
nonreduced scheme structures defined by the power section and by the
characteristic coefficients are not identified here; only their geometric
zero loci are asserted to coincide. Neither the norm condition nor this
support test supplies descent of a pure power to an actual ambient equation.

#### An intersection bound and the missing descent step

Write \(e=Q_0\) locally in a bundle trivialization. The pullback ideal
of \(C_0\) is exactly
\[
 \mathcal I_{C_0}\mathcal O_S=\mathcal I_E\mathcal I_Z .
\]
To check this on local rings, let \(q\) cut the target quadric and
choose a lift \(\widetilde g\) of the graph equation \(g\) of
\(C_0\subset Q\), in local frames at the target point. The ideal
of \(C_0\) there is \((q,\widetilde g)\) since its quotient by \(q\)
is the graph ideal on the smooth quadric. Explicitly, on \(W_0\ne0\) in target coordinates
\((W_0,W_1,W_3,W_4)\), take \(t=W_1/W_0\),
\(\widetilde g=W_3/W_0-t^3\) and \(q=W_4/W_0-tW_3/W_0\).
On \(W_4\ne0\) reverse the coordinate ordering and use the same
formulas; these two charts cover \(C_0\) and its inverse. On the first
chart the source expressions are
\[
 e=Q_0/U_0,\quad
 d=(U_0U_4-U_1U_3)/(Q_0U_0),\quad
 \widetilde s'=(U_0^2U_3-U_1^3)/(Q_0U_0^2).
\]
In a source frame
\(f^*q=ed\). Since \(f(E)\subset C_0\), the pullback
\(f^*\widetilde g=e\widetilde s'\) is divisible by \(e\); on \(D\)
the quotient \(\widetilde s'|_D\) is the divided graph section
\(s'\). Hence the inverse ideal is \((ed,e\widetilde s')\) and the
ideal of \(Z\) in the source is \((d,\widetilde s')\). Changing the
lift of \(g\) adds a multiple of \(d\) to \(\widetilde s'\), and
changing trivializations only changes the generators by units.
These local calculations apply at every inverse point, including
ramification and special fibers; away from \(E\) use that \(e\)
is a unit, and away from the inverse both sides are unit ideals.

The inclusion \(Z\subset D\) gives a scheme-theoretic bound
\[
 \operatorname{length}(Z\cap E)\le
 \operatorname{length}(D\cap E)=H^2=8 ,
\]
because \(E\) is not a component of \(D\). Consequently multiplication
by \(e\) from \(H^0(\mathcal O_Z)\) to \(H^0(H|_Z)\) has rank at least
four: its cokernel has length \(\operatorname{length}(Z\cap E)\).
A full-support fiber therefore has nontrivial nilpotent thickening on
\(Z\) and cannot have \(Z\) reduced. The norm can vanish without
full support, and even in the full-support locus multiplication by \(e\)
cannot be zero.

In a full-support fiber let \(n\) be the least positive integer such
that \(Q_0^n|_Z=0\). If an actual degree-\(b\) mate exists, its pullback
is a nonzero scalar multiple of \(Q_0^b\) by (8). It belongs to the
pullback ideal above; cancellation of the nonzerodivisor \(e\) then
gives \(Q_0^{b-1}|_Z=0\), hence \(b\ge n+1\) (in particular \(b\ge3\)).
Conversely that inequality on a full-support fiber puts \(Q_0^b\) in
the upstairs ideal; it does not put it in the coordinate subalgebra
in (8). Thus the residual inverse scheme supplies a necessary degree
bound, not an automatic descending equation.

The balanced conormal bundle strengthens the length bound. Put
\(L_\pi=(f|_E)^*\mathcal O_{C_0,\mathbf P^1}(1)\), where the degree one
is on the parametrizing \(\mathbf P^1\). Thus \(\deg L_\pi=2\) and
\(\mathcal O_E(E)=H|_E=L_\pi^4\).
The [balanced conormal bundle](../../results/quartic_conormal_characteristic_jump.md)
and the inverse ideal identity give the map
\[
 (L_\pi^{-7})^{\oplus 2}\longrightarrow
 \mathcal I_E/\mathcal I_E^2=L_\pi^{-4}
\]
with image \(\mathcal I_{Z\cap E/E}L_\pi^{-4}\): locally it is obtained
by dividing each inverse generator by \(e\) and restricting to \(E\).
It therefore has entries two sections of \(L_\pi^3\), not both zero
because \(D\) does not contain \(E\). Their common zero divisor has
length at most six. This gives the sharper
\(\operatorname{length}(Z\cap E)\le6\) and
\(\operatorname{rank}(e:H^0(\mathcal O_Z)\to H^0(H|_Z))\ge6\).
It does not decide whether all of \(Z\) is supported on \(E\).

#### The generic double branch has conductor coefficient one

Assume the image is an octic, so \(f:S\to X\) is the normalization.
At the generic point of \(C_0\), the only inverse curve is \(E\), by
the ruling-degree argument above. We show that after splitting its
degree-two residue extension, the two transverse branches are smooth
and have distinct tangent lines.

The conceptual consequence is that the saturated conormal pencil
on \(E\) is nonconstant: its values
at the two generic deck conjugates are distinct. After removing its
common zeros its degree is \(6-\operatorname{length}(Z\cap E)\); a
nonconstant map from an elliptic curve to a line has degree at least
two. On this birational locus, therefore,
\(\operatorname{length}(Z\cap E)\le4\) and multiplication by \(e\)
on \(Z\) has rank at least eight. In a full-support fiber, trivializing
the line bundle on the Artin scheme makes that multiplication a
nilpotent endomorphism of dimension twelve with at most four Jordan
blocks. Its nilpotence index is at least three, so a mate must have
degree at least four.

##### Exact direction calculation

On \(Z_0=1\), put \(Z_1=x,Z_2=y,Z_3=x^2+e\). Then
\(y^2=x^3-x+(x-\mu)e\) on \(S\); thus the normal derivative at
fixed \(x\) is given by \(2y\,\partial_e y=x-\mu\).
On \(E\) write \(t=(y+1-i)/(x-i)\). Substituting
\(y=t(x-i)-1+i\) into \(y^2-x^3+x\) and dividing by \(x-i\)
gives
\[
 K=-x^2+(t^2-i)x-it^2-2t+2it+2.
\]
The roots correspond to the two deck conjugates. On the target chart
\(U_0\ne0\), use the normal coordinates
\(U_3/U_0-(U_1/U_0)^3\), \(U_4/U_0-(U_1/U_0)^4\).
In the affine source chart put
\[
 D_j=2y(\partial_{Z_3}V_j+\rho_j)+(x-\mu)\partial_y V_j,
\]
evaluated at \(Z_3=x^2,\ y=t(x-i)-1+i\). Up to a common nonzero
scale, the two normal derivatives are
\[
 N_3=D_3-3t^2D_1+2t^3D_0,\qquad
 N_4=D_4-4t^3D_1+3t^4D_0.
\]
Indeed differentiation of the coordinate ratios uses
\(U_j/U_0=t^j\) on \(E\); a tangential correction to keep the target
base parameter fixed makes no difference to these normal derivatives.
Reduce \(N_j\) modulo \(K\) to \(a_j+b_j x\). The normal-vector
determinant at the two roots is \((x_{\rm deck}-x)W(t)\) where
\(W=a_3b_4-a_4b_3\).

Here is an exact coefficient check using the rows (4). Differentiating,
substituting and taking polynomial remainders as just prescribed
gives \((\mu-i)\mid W\). For \(\mu\ne i\), the coefficients of
\(t^7,t^6,t^5,t^4\) of \(W/(\mu-i)\), after dividing each by a
nonzero scalar, are
\[
\begin{aligned}
 &\rho_0+(-1+i)\rho_1/2-1,\\
 &-i\mu/2+\rho_0+1/2,\\
 &4i\mu+\rho_0+(-1+i)\rho_1+3(1+i)\rho_3/2-9,\\
 &7i\mu/2+\rho_0+(1-i)\rho_1/4+(1+i)\rho_3+\rho_4/2-5 .
\end{aligned}
\]
They solve successively in \(\rho_0,\rho_1,\rho_3,\rho_4\):
\[
 (\rho_0,\rho_1,\rho_3,\rho_4)=
 (i\mu/2-1/2,\;(-1+i)\mu/2-3(1+i)/2,\;
 -7(1+i)\mu/6+13(1-i)/6,\;-23i\mu/6+23/6).
\]
With these substitutions the remaining coefficients of \(W/(\mu-i)\),
in descending order, are \((\mu+i)\) times
\((-16/3,32(1+i)/3,-16i,16(-1+i)/3)\).
Thus the vanishing locus is \(\mu=i\) with arbitrary lifts, or
\(\mu=-i\) with \(\rho=(0,-1-i,1-i,0)\).
These identities can be replayed in any exact polynomial ring over
\(\mathbf Q(i)\): form \(K,D_j,N_j\) by the displayed substitutions,
take \(x\)-remainders using the leading coefficient \(-1\) of \(K\),
and compare the coefficients of \(W\) in \(t\).

Both loci are deck-invariant maps, not birational octics. Substitution
of the displayed matrix \(\mathsf M\) into (4) gives
\[
\begin{aligned}
 V_0\circ\mathsf M&=8V_0,& V_4\circ\mathsf M&=8V_4,\\
 V_1\circ\mathsf M-8V_1&=8[-(1+i)Q_0+(-1+i)Q_1],\\
 V_3\circ\mathsf M-8V_3&=8[(1-i)Q_0-(1+i)Q_1].
\end{aligned}
\]
Using \(Q_0\circ\mathsf M=8iQ_1\) and \(Q_1=-\mu Q_0\), all
four \(U_j\circ\mathsf M=8U_j\) on the two stated loci.
The deck involution acts nontrivially on \(E\), hence on the
surface function field, so an invariant map cannot be birational.

On a birational member \(W\ne0\). The two split normal derivative
vectors are nonzero and independent. In the generic completed
transverse plane each branch is smooth because a normal coordinate
with nonzero derivative gives a uniformizer. The distinct tangent
lines make their union an ordinary node. Its normalization conductor
is the maximal ideal on each branch, as seen in
\(k'[[u,v]]/(uv)\subset k'[[u]]\times k'[[v]]\) after the residue
field extension. Finite normalization and the conductor calculation
here are compatible with the separable residue splitting and
completion (the conductor is given by the finite-module annihilator).
Thus the conductor coefficient on \(E\) is exactly one.

#### The vertical divisor counts the residual inverse scheme

Retain the birational octic hypotheses. Write \(G=Z\cap E\) and
\(\pi=f|_E\). Let \(V\) be the vertical coefficient divisor of the
actual quadratic normal symbol of the octic: on the target curve
it is the common-zero divisor of its three coefficients in a balanced
frame. The following identities relate this divisor and the residual
conductor to the embedded inverse scheme:
\[
 V=\pi_*[G]+f_*[Z],\qquad
 (B_{\rm cond}-E)|_E=\pi^*V+\Delta-R.
\]
Here \(\Delta\) is the coincidence divisor of the saturated direction
map on \(E\) and its deck translate, and \(R\) is the ramification
divisor of \(\pi\).

**The inverse-scheme identity.** On the target quadric write
\(X|_Q=2C_0+R_Q\). The coefficient two follows from the two distinct
generic normal directions and from the nonzero evaluation of each
on the normal direction in \(Q\); the latter holds because \(D\)
does not contain \(E\). Birational pushforward of the Cartier
quadric section gives \(f_*[D]=[R_Q]\). The map on \(D\) also
factors through the residual Cartier scheme \(R_Q\): locally the
restriction of the octic equation is \(g^2 r_Q\), where \(g\) is
the graph equation of \(C_0\) on \(Q\). On \(D\) its pullback is
\((e s')^2 f_D^*r_Q=0\). The Cartier curve \(D\) on a smooth surface is Cohen–Macaulay
at every point. Its associated primes are its component generic
points; \(e\) is in none of them since \(E\) is no component of
\(D\), and \(s'\) is in none by the residual ruling-degree bound.
Thus multiplication by \((es')^2\) is injective even in the local
rings at exceptional or ramified points, proving the factorization.
For the projection formula, the graph divisor \(g=0\) is Cartier
on \(Q\) and meets every component of \(R_Q\) properly; its
pullback cuts \(es'=0\) on \(D\). The local exact sequence
\[
 0\to\mathcal O_D/(e)\xrightarrow{\;s'\;}
 \mathcal O_D/(es')\to\mathcal O_D/(s')\to0
\]
gives the sum of \([D\cap E]\) and \([Z]\) with their local
scheme lengths, and finite pushforward gives the divisor on \(C_0\)
\[
 C_0\cdot R_Q=\pi_*[D\cap E]+f_*[Z].
\]

Alternatively restrict the actual quadratic normal symbol to the
normal direction of \(C_0\) in \(Q\). Its value there cuts exactly
\(C_0\cdot R_Q\): the octic restriction is \(g^2r_Q\), so its
divided leading value on \(Q\) is \(r_Q|_{C_0}\).
After removing \(V\), the binary normal form is primitive, and its
two linear factors over the degree-two extension are conjugate.
The restriction of the pulled-back conormal coordinate \(q\),
after removing the common zero divisor \(G\), has zero divisor
\([D\cap E]-[G]\), since \(f^*q=ed\). Evaluation of the primitive
quadratic on the quadric direction is the norm of this primitive
linear evaluation, up to units, so its divisor is the pushforward of
\([D\cap E]-[G]\). To see the unit statement locally, over each DVR
on \(E\) both linear factors have a unit coefficient, and their
product is primitive. The pulled-back primitive quadratic is also
primitive, hence differs from their product by a unit. At a ramified
point the factor and conjugate evaluations have the same order; the
order of their product and the pullback of the target order both
include a factor of two. Dividing by the ramification index gives
the cycle pushforward with residue degree one, not twice that term. The resulting
divisor on \(C_0\) is therefore
\[
 C_0\cdot R_Q=V+\pi_*\bigl([D\cap E]-[G]\bigr),
\]
and subtraction proves the first identity.

In particular \(\deg V=12+\operatorname{length}(G)\).
The morphism \(Z\to C_0\) factors scheme-theoretically through \(V\):
at each point of its fiber over \(y\), the maximal ideal of the
Artin local ring is nilpotent to exponent at most its length, which
is at most \(\operatorname{ord}_y V\). This is not equality of the
scheme-theoretic image with \(V\). A simple point of \(V\) forces
an inverse point off \(E\), because each inverse point on \(E\)
would contribute both through \(G\) and through \(Z\).
Under full support, \(|V|=f(|G|)\) has at most four geometric points,
all of multiplicity at least two. If an actual degree-\(b\) mate
exists, multiplication by a local trivialization of \(e\) on the
part of \(Z\) over \(y\) is nilpotent with exponent at most \(b-1\)
and has cokernel of length \(\operatorname{ord}_y\pi_*[G]\).
Counting its Jordan blocks gives
\(\operatorname{ord}_y V\le b\,\operatorname{ord}_y\pi_*[G]\).
For the fixed member in §4, \(\deg V=12\) gives \(G=0\) and
\(V=f_*[Z]\) as divisors. Its archived monic coefficient gcd \(h(t)\)
is squarefree: reduce at \(i\mapsto3\) over \(\mathbf F_5\) (all
its denominators are units there), giving
\[
 t^{12}-2t^{11}+2t^{10}-t^9+2t^8-2t^7-2t^5
       +2t^4+2t^3-2t^2-t-2,
\]
whose gcd with its derivative is one. There is no vertical zero
at infinity by the other chart (§4). Thus each fiber of \(Z\to V\)
has length one at its unique point, and this finite map is an
isomorphism for the fixed member. This is not a scheme equality
for arbitrary lifts.

**The conductor identity.** Use the ambient
[Jacobian–conductor identity](conductor_jacobian_local_residue_proof.md#3-relation-to-the-jacobian-conductor-formula)
in local coordinates tangent and normal to \(C_0\).
Along \(E\) the pullbacks of the normal coordinates are divisible by
its local equation \(e\). The common zero divisor of the
two-column differential minors on \(E\) is \(G+R\): the tangential
column is the derivative of \(\pi\), and the normal column in the
two normal coordinates has common zeros exactly \(G\).
In contrast, divide the pullbacks of the implicit partial derivatives
by \(e\) before restricting to \(E\). The tangent partial then gives
zero, and the normal partials give the gradient of the quadratic
symbol evaluated at the actual normal column. Its common divisor
is \(\pi^*V+G+\Delta\): removing \(V\) and \(G\) leaves the
gradient of a product of two primitive linear forms evaluated on
the kernel of one of them. The result is a primitive covector
times the determinant of their two directions, cutting \(\Delta\),
also where they coincide. Since the conductor contains \(E\) with
coefficient one, canceling \(e\) in the Jacobian–conductor identity
and comparing these divisors proves the second identity.

Off ramification the coincidence divisor is invariant under the
deck map and descends. At a ramification point choose a local
parameter with deck action \(u\mapsto-u\) and a direction coordinate
regular at the common value. The difference of the two direction
values is odd in \(u\) and not identically zero because the
directions differ generically. Its first nonzero term has order
\(2m+1\) for some \(m\ge0\), at this arbitrary ramification point.
Thus subtracting the simple ramification contribution gives order
\(2m\), the pullback of a coefficient \(m\) on \(C_0\). Combined
with deck-invariant orders at the unramified pairs this proves
\(\Delta-R=\pi^*J\) for an effective divisor \(J\) on \(C_0\). The discriminant of the quadratic symbol has
divisor \(2(V+J)\) plus the branch divisor: after pullback it is
the square of the determinant of the primitive factors times the
square of the vertical coefficient. In particular
\(\deg(B_{\rm cond}-E)|_E=32\), also obtained from
\(B_{\rm cond}\sim5H\) and \(E\sim H\).
These identities describe restriction to \(E\), not the full
off-\(E\) conductor, and do not settle full inverse support or
higher-degree descent.

#### The horizontal symbol and the actual elliptic pencils

The focused [contact and spectral comparison](elliptic_contact_and_spectral_comparison.md#1-contact-moves-defect-between-the-vertical-and-horizontal-curves)
owns this geometry across all contact lengths \(g=\operatorname{length}(Z\cap E)\).
The actual direction bundle is \(B=A^3(-G)\), where
\(A=\pi^*\mathcal O(1)\) and \(G=Z\cap E\). The horizontal root
has type \((6-g,2)\), normalization \(E\), and trace conductor of
degree \(4-g\) on the base. Its full-root Picard classes retain the
conductor gluing when \(g<4\); at \(g=4\) the root is smooth and
the pencil difference is \(A^2(-G)\).

If the **actual** first degree-two kernel itself is a line subbundle,
the [socle comparison](elliptic_contact_and_spectral_comparison.md#3-four-necessary-rows-when-the-actual-first-kernel-is-saturated)
forces \(g(b-2)=24\), leaving four necessary degree rows. This
hypothesis is stronger than taking the saturation of a kernel and
does not classify all mates. The [fixed marking also prevents target
sign symmetry](elliptic_contact_and_spectral_comparison.md#4-the-fixed-marking-prevents-target-sign-symmetry).
Neither statement settles full inverse support or actual descending
powers. The support question concerns the whole family and every
contact stratum, including the singular-root strata \(g<4\).
The [conjugate-source account](elliptic_conjugate_sources.md) identifies
the actual \((8,8)\) pair \((F_8,\tau F_8)\), its residual degree
\(48\), and the precise poles in the saturated local cancellation.
Upstairs \(Q_0^b\) is already a global section for every \(b\);
the remaining descent question concerns the actual four-section
subalgebra and full conductor.

#### Descent and the remaining degrees

Write the upstairs conductor as \(\mathcal O_S(-B_{\rm cond})\).
[Finite duality](conductor_jacobian_local_residue_proof.md#2-direct-residue-and-finite-duality-proof)
gives \(\mathcal O_S(-B_{\rm cond})=\omega_S\otimes f^*\omega_X^{-1}\);
adjunction on the smooth quadric and the octic yields
\(B_{\rm cond}\sim5H\). In the hypothetical coefficient-five case
this would force \(B_{\rm cond}=5E\) by ampleness, so \(Q_0^5\) would
descend and give an actual quintic via the hypersurface restriction
sequence. The inverse ideal would then also force full support and
\(Q_0^4|_Z=0\). But the generic node calculation excludes the premise
throughout this birational lifting family.

In fact no mate of degree at most five exists in this family. The
inverse bound already requires \(b\ge4\). If a degree \(4\le b\le5\)
mate descended, its pullback would be a scalar times \(Q_0^b\).
Its linear normal form along \(C_0\) would vanish on the tangent
lines of both split branches, since its pullback has order \(b\)
on each. Distinct lines force that linear form to be zero. By the
[low-degree normal-order bound](../normal-geometry/formal-normal-intersection.md#low-degree-surfaces-singular-along-the-whole-quartic)
(P-011), a form of degree at most five of order at least two along
\(C_0\) is divisible by \(q\) (or is zero). But \(X\cap Q\)
has type \((8,8)\) on \(Q\), not a multiple of \((1,3)\), so it
already has residual support. This contradicts sole support.

For higher degrees the conductor automatically gives target membership
over the generic point of \(C_0\), but not necessarily over other
divisorial conductor images. An upstairs-regular section must first be
checked for membership in \(\mathcal O_X(b)\) at all codimension-one
points of \(X\). Only then does the \(S_2\) extension property of the
integral hypersurface imply global target regularity. Full support
of \(Z\) and higher-degree coordinate-subalgebra descent remain open.

#### A finite descent test on the residual quadric curve

Continue with birational octics, and suppose the source residual curve
\(D\) is integral and \(R_Q\) is reduced. The cycle identity proves
that \(D\to R_Q\) is finite birational. Let \(T\) be the second ruling
line of the target quadric. The two maps to \(T\) are finite flat of
degree two: they have degree two from the ruling calculation, are
nonconstant on the integral curves, and their direct images are
torsion-free over the smooth line. The arithmetic genera are one
for the source \((2,2)\) curve and five for the target \((2,6)\) curve,
by adjunction. Thus the trace splittings of the two algebras over
\(T\) are \(\mathcal O_T\oplus\mathcal O_T(-2)\) for \(D\) and
\(\mathcal O_T\oplus\mathcal O_T(-6)\) for \(R_Q\), by their Euler
characteristics. Trace agrees on the common generic algebra, so the
inclusion on the trace-zero summands is multiplication by a nonzero
binary quartic \(h\).

Locally on \(T\) this is the inclusion \(A\oplus hAw\subset A\oplus Aw\),
with \(w^2\in A\) for a trace-zero generator \(w\).
Both \(a+bw\) and \(w(a+bw)\) belong to the smaller algebra precisely
when \(h\) divides \(a,b\). The conductor on \(D\) is therefore
\(h\mathcal O_D\), cutting out a scheme of length eight. The target
double-cover discriminant is the source discriminant times \(h^2\),
as is seen by replacing \(w\) with \(hw\). This is the conductor
of the residual curves, not the ambient surface conductor or, if
\(D\) is singular, the conductor of a normalization. Concretely the
binary discriminant of the residual equation divided by the degree-four
trace discriminant of \(D\) gives \(h^2\) up to scalar; neither
discriminant is assumed squarefree.

The residual-curve conductor can also be compared with the ambient
one when \(R_Q\) is reduced. Write \(B'=B_{\rm cond}-E\). Then
\[
 B'|_D=2Z+B_{D/R_Q},
\]
where \(B_{D/R_Q}\) is the Cartier divisor of the finite birational
curve conductor. In local target coordinates \((t,v,q)\), with
\(Q=(q)\), write \(F|_Q=g^2r_Q\) for the implicit equation.
A rational residue generator on \(X\) is
\(\eta_X=dt\wedge dq/F_v\). Pull back using \(f^*q=ed\), divide
by the equation \(d\) of \(D\) in the adjunction residue, and
restrict to \(D\). The resulting expression is
\(e/(f^*g)^2\) times the pullback of \(dt/(r_Q)_v\) on \(R_Q\).
This is computed rationally on each generic component, choosing a
nonzero partial there; the curves are Cartier and the resulting
identities are of rational sections of dualizing line bundles.
Multiplying by the ambient conductor generator gives the regular
dualizing generator on \(D\) by finite duality and adjunction.
Comparing it with the pullback generator for \(R_Q\) identifies
the curve conductor by finite duality. The divisor of the comparison
coefficient is \(B_{\rm cond}|_D+E|_D-2(E|_D+Z)=B'|_D-2Z\),
because \(f^*g|_D=es'\). In the finite double-cover scope this
recovers the length relation \(32=2\cdot12+8\). It is not an
absorption operation and does not produce any descent survivor.

Near the finite conductor fibers use a target frame of
\(\mathcal O_X(1)\), pulled back to \(D\), to express the section
\(e=Q_0\). By the algebra inclusion, \(e^b|_D\) descends to \(R_Q\)
if and only if its trace-zero part vanishes modulo \(h\). This is
necessary for a degree-\(b\) mate by (8). On a conductor fiber disjoint
from \(E\), \(e\) is a unit and the condition becomes
\[
 (e/\tau e)^b=1\quad\text{in }\mathcal O_D/(h),
\]
where \(\tau\) is the involution of the source double cover.
The ratio is independent of the target frame on the conductor,
because target functions have invariant image modulo \(h\).
In characteristic zero a nontrivial principal unit has infinite
order, as follows by taking the first nonzero term in the nilpotent
filtration of its positive powers. Thus the residue ratios being
roots of unity is not sufficient: the full ratio must be torsion
in the finite algebra.

If one point over a conductor fiber is on \(E\) and another is not,
they map to the same target point (the trace-zero coordinate there
is zero), and that target point lies on \(C_0\). The off-\(E\)
point therefore already rules out full inverse support. For a
full-support candidate every remaining conductor fiber is either
disjoint from \(E\) or supported entirely on \(E\). In the latter
case \(e\) acts nilpotently on its Artin algebra and \(e^b=0\)
there for \(b\ge8\). Consequently eventual residual-curve descent
in this scope is equivalent to all off-\(E\) ratios having finite
order; any sufficiently large common multiple of their orders
passes the residual test. This does not establish ambient descent.

The scope occurs generically in the actual family, without asserting
that a full-support survivor lies in it. On the basepoint-free locus,
the derivatives of \(d\) in the four lifting parameters are
\((U_4,-U_3,-U_1,U_0)\) by (5), so the total divisor is smooth.
By generic smoothness and properness the general \(D\) is smooth,
and its ample class makes it connected. The original coefficients
(4) with \(\mu=2\) and zero lifts give an exact control for generic
degree one onto the residual target. Reduce at \(i\mapsto5\)
over \(\mathbf F_{13}\) on \(Z_0=1\). In the second-ruling fiber
\(B=9\), the two points \((Z_1,Z_2,Z_3)=(6,7,12),(12,12,5)\)
are off \(E\), with target tuples \((12,10,4,12),(8,10,7,12)\);
their first-ruling values are respectively 3 and 11. The determinants
of the derivatives in \((Z_1,Z_2,Z_3)\) of
\((Q_1+2Q_0,U_3-9U_0,U_4-9U_1)\) are 7 and 12.
Thus these distinct first-ruling values persist on a pair of points
étale-locally to characteristic zero and to general parameters.
A degree-two image map on the integral \(D\) would instead have
image second-ruling degree one, so could not give those two values.
Thus the general \(R_Q\) is reduced by the cycle identity. Keep the
full inverse support test first; only for a survivor in this scope
does the finite conductor algebra give the next descent check.

#### The meeting norm divisor and its normalization

Let \(U\) be the characteristic-zero parameter open where the source
quadric is smooth and the four sections are basepoint-free. Over this
open, let \(N\subset U\) be the divisor defined by the norm of \(e=Q_0\)
on the relative length-twelve scheme \(Z\), and \(G=Z\cap E\) the
relative intersection. On \(U\), \(N\) is reduced and integral and
\(G\to N\) is its normalization. In particular \(N\) is birational to
\(E\times\mathbf A^3\).

For a point \(p\in E\) over parameter \(t\in C_0\), consider the two
pulled-back normal derivatives after division by \(e\). Their affine
dependence on the four lifts \(\rho\) comes from \(U_j=V_j+\rho_j e\).
In a normal frame on a finite chart the linear part is, up to a unit,
the quotient \(k^4/T_t\) with
\[
 v(t)=(1,t,t^3,t^4),\qquad T_t=\langle v(t),v'(t)\rangle .
\]
Indeed the direction of a projective ratio is unchanged by adding
the projective radial direction, and passing to the normal derivative
also quotients by the tangent direction of \(C_0\). At infinity the
two-plane is spanned by the last two coordinate vectors in this
ordering. The two divided inverse generators define \(G\); this description
holds also at ramification, since taking a projective normal derivative
uses the tangent line of the smooth target curve, not a local inverse
to \(\pi\). Their linear parts have rank two. Thus before deleting basepoints the
scheme is an affine plane bundle over \(E\) times the smooth
\(\mu\)-line. For fixed \(\mu\), a basepoint is necessarily away
from \(E\) and gives \(\rho=-(V_j/e)_j\). The closure of the image of
this map on \(S_\mu\setminus E\) is irreducible of dimension at most
two and has affine span \(k^4\). An affine linear equation for the
image would, after clearing \(e\) and restricting to \(E\), give a
linear dependence among the four independent sections \(V_j|_E\).
The closure therefore cannot contain an affine two-plane, so every
plane of lifts has basepoint-free members. Consequently \(G\) over
\(U\) is smooth integral of dimension four. It is finite over \(U\)
as a closed subscheme of \(Z\), and its image is the support of \(N\).

To check generic degree, consider distinct points \(p,p'\in E\).
If their projected parameters \(t,u\) are distinct and finite,
the determinant of their two cone tangent frames is, up to sign,
\((t-u)^4(t^2+4tu+u^2)\). The planes are distinct: in the first-two
coordinate projection they are graphs with slope entries \(3t^2\)
and \(4t^3\), which together distinguish \(t\). When one parameter
is infinity the finite plane is transverse to the last-two coordinate
plane. For a general distinct pair the two affine planes of lifts meet
in at most a point. The exceptional distinct-parameter pairs have
dimension one and plane intersection dimension at most one. Including
\(\mu\), either stratum gives dimension at most three. When
\(p\ne p'\) project to the same parameter they are deck conjugates
and the two planes are parallel. If the offsets agree in \(k^4/T_t\), the normal vectors for all
lifts are proportional there: after trivializing their nonzero linear
scales both are the same translation of the quotient map. For each fixed \(\mu\ne i\) the determinant at zero lift is a
nonzero rational function of \(t\). In particular \(\mu=-i\) requires
nonzero lifts in the zero-determinant table and is not an exception
at zero lift. Basepoint freeness away from \(E\) is not needed to
take these derivatives near \(E\). Thus equal offsets occur over
at most finitely many \(t\) for each such \(\mu\), including any in
the infinity chart. For \(\mu=i\), the deck transformation scales
\(Q_0\) and each \(U_j\) by eight on the source, so both the local
equation \(e=Q_0/U_0\) and all target ratios are invariant. Their
divided coefficients therefore agree at conjugate points. This
whole fixed-\(\mu\) stratum has one dimension before adding the
two free lift coordinates. In either case the equality locus has
dimension at most three after adding those coordinates. Thus the generic geometric fiber of
\(G\to N\) has a single point. Separability in characteristic zero
makes the generic field degree one.

At the generic DVR of the prime image, the norm vanishing order
is the length of the cokernel of multiplication by \(e\). This
cokernel is the finite pushforward of the twisting line bundle
restricted to \(G\). Since \(G\) is reduced, it factors through the
reduced image, so the cokernel at the generic DVR is killed by its
uniformizer. The generic field degree one gives DVR length one. The norm cuts an effective Cartier divisor
on the smooth parameter open, with no embedded components, so \(N\)
is reduced. The open of the smooth affine-plane bundle obtained by removing
basepoints is smooth, hence normal; the finite map is birational
because the function fields agree. Since both source and target
are integral, this identifies it with the normalization over the
whole asserted open, not just over its generic points. An affine plane bundle over the smooth product base is
generically trivial, yielding the claimed birational type.

A geometric point of \(N\) is normal exactly when its \(G\)-fiber has
length one. Indeed in length one the unit spans the finite fiber
algebra, and Nakayama makes the local map onto the normalization
surjective; it is already injective. Conversely local normality makes
the normalization an isomorphism. This detects nonnormality even when
a fiber is a single nonreduced point. Normality here is equivalent
to smoothness, since the normalization is smooth and is an
isomorphism precisely on the normal locus. For full inverse support the
nilpotent operator \(e\) on the length-twelve inverse scheme has
\(\operatorname{length}(G)\) Jordan blocks. In degree \(b\) their lengths
are at most \(b-1\) by the inverse-ideal test. Hence a mate requires
\[
 \operatorname{length}(G)\ge \left\lceil\frac{12}{b-1}\right\rceil .
\]
In particular degree six requires length at least three, and degrees
seven through twelve require the nonnormal locus of \(N\).
At normal points of \(N\), a full-support fiber could only admit
mates of degree at least thirteen. This restriction does not exclude
full support at such a normal point; keep the support test before
the descent test.

##### A meeting fiber that fails full support

Take \(\mu=2\) and
\(\rho=(0,0,-2+2i,-4-2i)\). At \(p=-T\) on the marked elliptic
curve, the source coordinates are \(x=i,y=-1+i\) on \(Z_0=1\);
the removable value of the pencil parameter is \(t=1+i\).
In the displayed direction formulas, substitute \(x=i,t=1+i\)
after taking the remainders of \(N_3,N_4\) modulo \(K\).
Both divided normal derivatives vanish. Equivalently one can
differentiate the ratios at \(p\), using their regular values there.
Thus the parameter belongs to \(N\) once the following basepoint
check is made.

Here are exact arithmetic checks for this actual member, with its
characteristic-zero parameters fixed over \(\mathbf Q(i)\). Work
over the DVR \(\mathbf Z[i]_{(13,i-5)}\), with residue field
\(\mathbf F_{13}\) and \(i\mapsto5\). For the five polynomials
\(Q_1+2Q_0,U_0,U_1,U_3,U_4\) of (3)–(5), set one projective
coordinate \(Z_j\) to one in turn; the reduced Gröbner basis in the
other three variables is \((1)\) on each of the four charts.
The basepoint incidence is projective over this DVR; a nonempty
geometric generic fiber would specialize to its closed fiber by
properness, so the geometric generic fiber is empty. On the affine chart \(Z_0=1\),
the point \((x,y,Z_3)=(11,0,9)\) has \(e=5\) and target tuple
\((U_0,U_1,U_3,U_4)=(1,3,1,3)\) modulo 13. The three equations
\[
 Q_1+2Q_0,\qquad U_0U_4-U_1U_3,\qquad U_0^2U_3-U_1^3
\]
vanish there and their Jacobian determinant in \((x,y,Z_3)\) is
12 modulo 13. The square Jacobian gives an étale neighborhood
of the special-fiber point over the DVR, so it lifts over the
henselization with the original coefficients unchanged. Both \(e\)
and \(U_0\) remain units (their residues are nonzero). The generic
point of this lifted section is therefore an actual characteristic-zero
inverse point off \(E\).

This member is birational onto an octic. The map is finite and
its degree times the image degree is eight. A plane image is
impossible since \(C_0\) spans the target, and a quadric image
was already excluded by the ruling degrees. If the map had
degree two onto a quartic, pushing forward the source quadric
section \(E+D\) would give coefficient two on \(C_0\), so the
image quadric section would have coefficient one there. The image
would then be generically smooth along \(C_0\), and both divided
normal derivative vectors would lie in the same line in the
target normal plane. But \(\mu=2\ne\pm i\) has nonzero deck
determinant for every choice of lifts by the direction calculation.
This excludes degree two.

The closed full-support locus, cut out set-theoretically by the
power section above, is therefore proper inside the integral
four-dimensional \(N\). It has dimension at most three, also
after restricting to birational octics. This is a search restriction
for every degree, not a proof that this smaller locus is empty.

#### Matrix formulation

There is a single matrix test throughout the basepoint-free locus. In
the homogeneous coordinate ring \(R\) of the source quadric, put
\[
 g_0=(U_0^2U_3-U_1^3)/Q_0,\qquad
 g_\infty=(U_3^3-U_1U_4^2)/Q_0 .
\]
The numerators vanish on \(E\), so these quotients are quartics.
Substituting the Segre coordinates into the two cubics gives
\(v_0^2(u_0^3v_1-u_1^3v_0)\) and \(v_1^2(u_0^3v_1-u_1^3v_0)\),
respectively. Dividing on \(Y\) by \(Q_0\) as above shows that
\(g_0|_D=v_0^2s'\) and \(g_\infty|_D=v_1^2s'\), with the
\(v_i\) pulled back to \(D\). Full inverse support holds exactly when
\[
 Q_0^{12}\in dR_{22}+g_0 R_{20}+g_\infty R_{20}\subset R_{24}.
\tag{9}
\]
Indeed \(Q_0^{12}\) vanishes on \(Z\) exactly when \(Q_0\) vanishes
on its support, since each Artin local ring has length at most twelve.
Identify \(R_n=H^0(S,M^n)\) by the hypersurface sequence. For
\(n=20,24\), the divisor sequence for \(D\) gives a surjective
restriction to \(H^0(D,M^n)\) with kernel \(dR_{n-2}\), since
\(H^1(S,M^{n-2})=0\) on the product of projective lines. Thus the
\(d\)-multiples span a subspace of dimension \(23^2=529\) in degree 24,
and the quotient is \(H^0(D,M^{24})\) of dimension \(25^2-23^2=96\).

The two cohomology groups needed on \(D\) are
\[
 H^1(D,M^{20}B^{-2})=0,\qquad H^1(D,M^{24}A^{-2})=0.
\]
Adjunction on the smooth quadric gives \(\omega_D\simeq\mathcal O_D\).
By Serre duality it suffices to show that \(M^{-20}B^2\) and
\(M^{-24}A^2\) have no sections on \(D\). On each integral \(C_i\),
the ruling degrees are nonnegative, since the bundles are pulled
back from the two projective lines. Their multiplicity-weighted totals
give \(0\le\deg_{C_i}B\le2\) and \(0\le\deg_{C_i}A\le6\).
As \(\deg_{C_i}M\ge1\), the two dual degrees are at most \(-16\)
and \(-12\), respectively.

For either dual bundle \(L\), take an effective subdivisor \(T\) of
\(D\) and remove one copy of any integral component \(C_i\), writing
\(T=C_i+T'\). The divisor sequence on \(S\), tensored on \(T\)
by \(L|_T\), gives
\[
 0\longrightarrow L|_{C_i}\otimes\mathcal O_{C_i}(-T')
   \longrightarrow L|_T\longrightarrow L|_{T'}\longrightarrow0 .
\]
This follows locally by multiplying by an equation of \(T'\), and
holds when \(T'\) still contains \(C_i\). Both \(T'\) and \(C_i\)
have nonnegative bidegrees on \(S\), so \(T'\cdot C_i\ge0\).
The kernel therefore has negative degree on the integral curve
\(C_i\). Induction on the sum of the multiplicities of \(T\) gives
\(H^0(D,L)=0\), proving both vanishings.

On \(D\), the basepoint-free pencil \(v_0^2,v_1^2\) gives a
surjection \(\mathcal O_D^2\to B^2\) with kernel \(B^{-2}\).
After tensoring by \(M^{20}\), the first vanishing makes it
surjective on sections. Multiplication by the regular section \(s'\)
identifies its image bundle \(M^{20}B^2=M^{24}A^{-2}\) with
\(\mathcal I_{Z/D}M^{24}\). Since the multipliers in degree 20
all lift to \(R_{20}\), the \(g_0,g_\infty\) multiples span
all of \(H^0(D,\mathcal I_{Z/D}M^{24})\) modulo \(dR_{22}\).
The second vanishing gives surjectivity of the restriction from
\(H^0(D,M^{24})\) to \(H^0(Z,M^{24})\), so this span has dimension
\(96-12=84\). The right side of (9) is therefore the full space of
forms vanishing on \(Z\), of rank \(529+84=613\).

A birational fiber passing the geometric support test (9) requires
an actual identity (8) to produce a mate.
[Review status of STCI-R-0076](../../results/elliptic_inverse_support.md#review)

### The characteristic-zero center line

On the line \(\mu=2,\ \rho_0=\rho_1=\rho_3=0,\ \rho_4=p\), every
basepoint-free characteristic-zero fiber fails the full inverse support
test. For a birational fiber the Cartier-divisor argument of §3
therefore excludes a homogeneous mate of every positive degree for its
implicit octic. [Exact elimination and replay in STCI-I-0005](../../investigations/stci-equation-search/index.md#characteristic-zero-center-line)
· [Separate finite-field test](../../investigations/stci-equation-search/index.md#finite-field-candidate-search).

## 6. Low-degree filters and the constructive question that remains

The [generic node and descent argument](#descent-and-the-remaining-degrees)
excludes all mates of degree at most five on the birational octic locus.

An equal-degree control needs an additional hypothesis not established
on the family: suppose the irreducible quadratic symbol of an octic is
saturated. For a degree-eight
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
In fact this saturation hypothesis fails on the birational family.
The generic node gives a quadratic symbol of class \((18,2)\).
Its horizontal divisor is the image of \(E\) under the pair of maps
to \(C_0\) and to the balanced direction line: these give the two
distinct generic roots, each simple. The map onto that divisor is
birational because the directions separate the two generic deck
conjugates. The image therefore has bidegree \((d,2)\), with
\(d=6-\operatorname{length}(Z\cap E)\) the degree of the saturated
direction pencil. The vertical divisor of the quadratic symbol has
degree \(18-d\ge12\). This explains why the equal-degree filter
cannot settle the birational lifting family; degree-eight descent
is not decided here.

The first unresolved implication is whether the support-unit locus (7)
meets the smooth, basepoint-free, birational locus. Only then is a descending
pure power in (8) a constructive target. An alternative would be a uniform
obstruction covering this entire five-parameter source. The center-line
rejection settles the support test on that line for every \(b\). Existence
elsewhere in the family remains open.

The involution quotient, described as a degree-four join of two conics in
\(\mathbf P^5\), suggests another geometric model for studying the source
quadrics and a residual inverse curve. Its required residual class and
scheme saturation have not been computed; no universal residual floor
follows. The value of (1)–(8) is an actual higher-degree inverse construction
and a precise geometric support/descent problem, rather than a forced claim
of STCI existence or nonexistence. These exact number-field equations and
saved characteristic-zero calculations assert no uniform reduction modulo
primes or positive-characteristic family theorem.

## A distinct failed marked inverse candidate

An earlier explicit test on the Segre quadric \(S=(ad-bc=0)\), with
\(\Delta=b-c\), used the four quadratic sections
\[
(U_0,U_1,U_2,U_3)=
(a^2+\Delta^2,\ ab+\Delta^2,\ dc+2\Delta^2,\ d^2+3\Delta^2).
\]
They restrict on \(\Delta=0\) to the marked quartic parametrization.
The historical exact computation found no basepoints on the chart
\(\Delta=1\), but the pullback of the four homogeneous generators of
\(I_C\) on that chart defined an **extra inverse scheme of length sixteen**
(zero-dimensional). Thus this candidate fails the full-inverse-support
requirement; its failure does not classify other perturbations or prove
an STCI obstruction. The corresponding Macaulay2 diagnostic was retired.
