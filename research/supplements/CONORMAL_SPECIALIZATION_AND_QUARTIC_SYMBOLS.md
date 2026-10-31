# Conormal splitting, mu4 specialization and actual quartic symbols

The fixed embedding is C0=[s4:s3t:st3:t4]. This chapter owns the characteristic-dependent conormal transition, the prescribed flat quartic-pair degeneration, and the actual global quartic-symbol images. The normal bundle, the first symbols of two displayed equations, the full normal initial ideal, and specialization of the associated graded algebra measure different data. Their proofs support [R-0020](../results/quartic_conormal_characteristic_jump.md) and [R-0021](../results/quartic_mu4_degeneration.md), with inherited independent geometry/symbol review. The general [filtration comparison](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md) owns the canonical equation-module kernel identification of R-0031.

## Conormal transition (P-009): characteristic jump in the normal bundle of \(C_0\)

On the
\(x_0\ne0\) chart write the curve as

\[
y=u,\qquad z=u^3,\qquad w=u^4,
\]

with conormal generators \(a=z-y^3\), \(b=w-y^4\).  On the \(x_3\ne0\)
chart put

\[
\alpha=Y-Z^3,\qquad\beta=X-Z^4.
\]

Modulo the square of the curve ideal, direct substitution on the overlap gives

\[
\binom{\alpha}{\beta}=
\begin{pmatrix}
-3u^{-6}&2u^{-7}\\
-4u^{-7}&3u^{-8}
\end{pmatrix}
\binom a b,
\qquad \det=-u^{-14}.
\]

Use the quadric conormal generator \(q_s=b-ua\), for which
\(q_t=u^{-8}q_s\), and take \(r_s=a,r_t=-\alpha\).  Then

\[
r_t=u^{-6}r_s-2u^{-7}q_s.
\]

Thus the extension class of

\[
0\longrightarrow\mathcal O(-8)
\longrightarrow N^*_{C_0/\mathbf P^3}
\longrightarrow\mathcal O(-6)
\longrightarrow0
\]

is represented by \(-2u^{-1}\in H^1(\mathcal O(-2))\).  It is nonzero
unless the characteristic is two.  Hence

\[
N_{C_0/\mathbf P^3}\cong
\begin{cases}
\mathcal O(7)\oplus\mathcal O(7),&\operatorname{char}k\ne2,\\
\mathcal O(6)\oplus\mathcal O(8),&\operatorname{char}k=2.
\end{cases}
\]

The transition identities and determinant were verified independently by exact
symbolic expansion.  In characteristic three, they also identify the
\((3,4)\) complete intersection above as a globally primitive triple:
locally its ideal is \((a,b^3)\) on the first chart and
\((\beta,\alpha^3)\) on the second, with

\[
\operatorname{gr}\mathcal O_X
=\mathcal O_C\oplus\mathcal O_C(-7)\oplus\mathcal O_C(-14).
\]
Its arithmetic genus is therefore \(19\), as required for a \((3,4)\)
complete intersection.

## The prescribed mu4 intersection and actual quartic symbols

The following full degeneration, initial-ideal and symbol calculations support R-0020–21. The conormal transition itself is proved above in P-009; no balanced frame is used in characteristic two. The inherited geometry/symbol review is preserved as review of these exact statements.

## 1. What actually coalesces

Consider the integral equations

\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3.
\]

Their projective intersection is a flat family over \(\mathbf Z\). Indeed its
homogeneous coordinate ring is free over \(\mathbf Z[x_0,x_3]\), with basis
\(x_1^a x_2^b\), \(0\le a,b<4\): the two relations are monic in separate
variables. In particular every graded piece is a free abelian group.

On \(x_0=1\), put

\[
u=x_1,\qquad X=x_3-u^4,\qquad Y=x_2-u^3.
\]

Then \(I_C=(X,Y)\), \(F=-X\), and, modulo \(F\),

\[
G=(u^3+Y)^4-u^{12}
 =Y^4+4u^3Y^3+6u^6Y^2+4u^9Y.                 \tag{1}
\]

On the open where \(u\ne0\), set \(z=x_2/u^3\). The actual intersection is

\[
\operatorname{Spec}k[u,u^{-1},z]/(z^4-1)
 =\mathbf G_m\times\mu_4,                    \tag{2}
\]

and \(C\) is the locus \(z=1\).

In characteristic zero, over an algebraic closure, its four components close
up to the distinct smooth quartics

\[
C_\zeta=[s^4:s^3t:\zeta st^3:t^4],\qquad \zeta^4=1.
\]

There are no further components. At \(x_0=0\) the equations force
\(x_1=x_2=0\); on \(x_0=1,u=0\) they force \(x_2=x_3=0\).
The four components already have total degree sixteen. The complete
intersection is Cohen--Macaulay and generically reduced along each, so has
neither an embedded component nor an extra nilpotent structure supported at
the endpoints. It is the reduced union of the four quartics.

In characteristic two,

\[
z^4-1=(z-1)^4,\qquad (F,G)|_{x_0\ne0}=(X,Y^4).
\]

The analogous chart \(x_3\ne0\) has coordinates
\(c=x_2/x_3\), \(A=x_0/x_3-c^4\), \(B=x_1/x_3-c^3\), and ideal
\((A,B^4)\). These charts cover the intersection, proving its reduced support
is exactly \(C\). The generic transverse algebra is \(k(C)[Y]/(Y^4)\).

Thus the four sheets are **four actual curve components in characteristic
zero**, indexed by the geometric points of \(\mu_4\). In characteristic two
the group scheme has one point with length four. Its nonreduced direction
becomes the transverse thickness of the single support curve. This is a
specific finite-flat scheme explanation of coalescence, not an inference
from a drawing of a normal cone.

There is a numerical check at the endpoints. In the smooth surface
\(F=0\) near \([1:0:0:0]\), the four branches are
\(Y=(\zeta-1)u^3\); every pair has intersection multiplicity three.
The other endpoint has the same description using \(G=0\).
The two delta invariants are eighteen each. Consequently the reduced union
has arithmetic genus \(36-4+1=33\), exactly that of a \((4,4)\) complete
intersection. Relative to \(C_1=C\), the other three quartics meet it in the
cycle \(9p_0+9p_\infty\). These are components downstairs, not exceptional
fibers of a blowup.

## 2. The full initial ideal explains the multiplicity change

Both original equations have generic normal order one in both
characteristics. At the generic point of \(C\), let \(K=k(u)\).
In characteristic zero their first symbols are

\[
\operatorname{in}F=-X,\qquad
\operatorname{in}G=-3u^8X+4u^9Y.
\]

They are independent, so the complete initial ideal is \((X,Y)\) and the
intersection has generic multiplicity one on \(C\). The other twelve units
of degree occur on the three residual quartics.

In characteristic two the two first symbols generate just \((X)\).
Cancellation of the \(X\) terms using the **actual equations** produces
\(Y^4\). Hence

\[
\operatorname{in}_{I_C}(F,G)=(X,Y^4),\qquad
\operatorname{gr}_{I_C}\mathcal O_{V(F,G),\eta_C}
 \simeq K[Y]/(Y^4).                           \tag{3}
\]

The initial ideal of the pair is therefore strictly larger than the ideal
generated by their two first symbols. The missing second generator occurs
at order four. This is the decisive higher-initial-ideal phenomenon.

Generically reduced does not mean that the positive graded pieces vanish
over the entire characteristic-zero curve. On the full \(u\) chart, (1)
instead gives

\[
\operatorname{gr}_{I_C}\mathcal O_{V(F,G)}
 \simeq k[u,Y]/(u^9Y).
\]

The positive pieces are torsion at \(u=0\); the other chart gives the
analogous torsion at infinity. This records where the residual branches meet
\(C\). Equivalently the determinant of the two first-normal sections is
\(-4s^9t^9\), a section of \(\det(E(4))=\mathcal O_{\mathbf P^1}(18)\),
where the notation \(E(4)\) means the ambient twist by
\(\mathcal O_C(4)=\mathcal O_{\mathbf P^1}(16)\).

The same coefficient has three interpretations:

\[
P'_Y(u,0)=4u^9
 =\prod_{\zeta\ne1}\bigl((1-\zeta)u^3\bigr).
\]

It is the derivative of the roots-of-unity equation at its identity, the
coefficient of the conormal determinant, and the product of the separations
from the three residual branches.

There is also an explicit failure of base change for the normal filtration.
For the integral chart \(\mathscr A=\mathbf Z[u,Y]/(P)\) of (1),

\[
\operatorname{gr}_{(Y)}\mathscr A
 =\mathbf Z[u,\eta]/(4u^9\eta).
\]

Indeed the initial ideal of the principal ideal \((P)\) is generated by
\(4u^9Y\), since \(\mathbf Z[u]\) is a domain. Its reduction modulo two
is \(\mathbf F_2[u,\eta]\), whereas

\[
\operatorname{gr}_{(Y)}(\mathscr A\otimes\mathbf F_2)
 =\mathbf F_2[u,\eta]/(\eta^4).
\]

The whole intersection family is flat, but taking its associated graded
algebra along \(C\) does not commute with this specialization. This is an
explicit reason that specializing only first normal symbols loses the
new order-four relation.

## 4. Which symmetric-algebra sections come from quartics?

The incomplete embedding remains visible in this calculation. Its degree-one
linear series is
\(W=\langle s^4,s^3t,st^3,t^4\rangle\), missing \(s^2t^2\).
In degree two, the sums of exponents \(\{0,1,3,4\}+\{0,1,3,4\}\)
already fill \(\{0,\ldots,8\}\). Induction gives every exponent through
\(4n\) for \(n\ge2\). Thus the homogeneous coordinate ring differs from
the full section ring only in degree one; it is incorrect to propagate that
one-dimensional deficiency to all higher degrees. In particular

\[
h^0(\mathcal I_C(4))=35-17=18.
\]

Let \(\sigma_1\) be the quartic first-symbol map. Its image is not the whole
twenty-dimensional space \(H^0(E(4))\). Twisting the conormal sequence gives

\[
0\to\mathcal O(8)\to E(4)\to\mathcal O(10)\to0.
\]

The residual restriction on \(Q\) gives

\[
0\to\mathcal O_Q(-2,2)\to\mathcal O_Q(1,3)
 \to\mathcal O(10)\to0.
\]

Its cokernel on sections is \(H^1(Q,\mathcal O_Q(-2,2))\simeq k^3\).
Let

\[
V_{10}=\operatorname{im}H^0(Q,\mathcal O_Q(1,3))
 =\langle1,u,u^3,u^4,u^6,u^7,u^9,u^{10}\rangle.
\]

Quadratics restrict onto \(H^0(\mathcal O(8))\), so \(q\) times
quadratics supplies the full nine-dimensional kernel summand. Therefore,
**in both characteristics**,

\[
\operatorname{im}\sigma_1
 =\{\xi\in H^0(E(4)):\bar\xi\in V_{10}\},\qquad
\dim\operatorname{im}\sigma_1=17.                \tag{7}
\]

In characteristic two, the splitting makes this
\(H^0(\mathcal O(8))e\oplus V_{10}f\). A symbol
\(A(u)e+B(u)f\) is realizable exactly when
\(B_2=B_5=B_8=0\).
In characteristic zero use the balanced frame
\(U=b-\tfrac32ua,V=a\). For \(P(u)U+R(u)V\), realizability is exactly

\[
P_1=2R_2,\qquad P_4=2R_5,\qquad P_7=2R_8.
\]

The second-symbol map has a more severe realization restriction:

\[
H^0(\mathcal I_C^2(4))=kq^2,
\quad \ker\sigma_1=kq^2,
\quad \operatorname{im}\sigma_2=k\,\operatorname{in}(q^2).          \tag{8}
\]

There is a short geometric proof. A double-vanishing quartic restricts on
\(Q\) to a section of \(\mathcal O_Q((4,4)-2(3,1))
=\mathcal O_Q(-2,2)\), hence restricts to zero. Write it as \(qH\).
Double vanishing forces the quadric \(H\) to contain \(C\), and uniqueness
of \(Q\) gives \(H\in kq\). Its second symbol is nonzero.

The full second-symbol targets are nevertheless

\[
\operatorname{Sym}^2E(4)=
\begin{cases}
\mathcal O(2)^3,&\operatorname{char}0,\\
\mathcal O(0)\oplus\mathcal O(2)\oplus\mathcal O(4),&\operatorname{char}2.
\end{cases}
\]

Both have nine sections; only one dimension is realized. There is no jump
in the rank of the quartic first-symbol map or in the dimension of its
kernel. The characteristic dependence lies in the conormal extension and
the higher compatibility of actual equations, not in an extra supply of
quartics of normal order two.

## 5. A uniform reduction of all (4,4) candidates

Equation (8) removes the proposed normal-order cases \((1,2)\) and
\((2,2)\), and every higher order, in **both** characteristics. An equation
of order at least two is a scalar multiple of \(q^2\). A quartic mate cuts
on \(Q\) a divisor of class \((4,4)\), which cannot have support just
\(C\) of class \((3,1)\). If the mate is divisible by \(q\), the common
locus even contains \(Q\). Thus every possible pair has orders \((1,1)\).

Multiplicity four then requires dependent first symbols. Locally over
\(K=k(C)\), replace one generator by its difference with a \(K\)-multiple
of the other and eliminate the linear normal variable. Multiplicity four
means that the first surviving term in the remaining normal variable is of
order exactly four. Local cancellation is necessary; its coefficients must
also arise from global degree-four forms with coefficients in \(k\).

The characteristic-two example passes these conditions and exhausts degree
sixteen on \(C\). For an arbitrary coprime global quartic pair, generic
intersection multiplicity four on the degree-four \(C\) also exhausts the
degree, so complete-intersection purity rules out residual or embedded
components. A construction over \(K[[X,Y]]\) alone supplies neither those
global quartics nor their coprimality.

## 6. What the symmetric algebra does and does not explain

The difference in (1), the vanishing extension class in (4), and the
order-four initial generator in (3) explain why the **known equations** work
in characteristic two and fail in characteristic zero. They do not by
themselves show that every different characteristic-zero pair fails.

An explicit control prevents that overclaim. In every characteristic, (4)
gives a quotient \(E\twoheadrightarrow\mathcal O(-6)\), and therefore the
graded quotient

\[
\operatorname{Sym}^\bullet E\twoheadrightarrow
\mathcal O_C\oplus\mathcal O(-6)\oplus\mathcal O(-12)\oplus\mathcal O(-18).
\]

This algebra has precisely the graded line bundles and Hilbert polynomial
\(16d-32\) of the characteristic-two \((4,4)\) structure. It is even
realized by an embedded primitive quadruple: take the Cartier divisor
\(4C\) on the smooth quadric \(Q\). That quadruple is not a complete
intersection of two quartics. For example its ideal contains \(q\), whereas
a \((4,4)\) complete intersection has no quadratic equation. Thus even an
actual primitive quadruple, together with the correct graded algebra and
genus, is insufficient. **Ambient degree-four realization is essential.**

Nor does a bare symmetric algebra remember the nonlinear coordinate changes
needed for embedded higher neighborhoods. For the prescribed characteristic-
two quadruple the full overlap is

\[
c=u^{-1}+u^{-4}Y,\qquad
B=u^{-6}Y+u^{-9}Y^2+u^{-12}Y^3 \pmod{Y^4}.
\]

The change in the base coordinate and the quadratic and cubic terms carry
information that its graded line bundles alone omit.

STCI-R-0012 supplies a stronger, independently audited statement about this
specific example: no flat embedded lift over \(\mathbf Z_{(2)}\) or
\(\mathbf Z_2\) can retain the fixed curve as its generic reduced support.
Every such lift would force a primitive triple, whose free
\(H^1(\mathcal O(-4))\) obstruction has a Laurent coefficient congruent to
two modulo four. The flat family in section 1 is consistent with this
theorem: its generic support has four components. This is not a theorem
about arbitrary ramified bases or every characteristic-zero quadruple.





## An independent homogeneous Euler/Jacobian proof

Work over an algebraically closed characteristic-zero field with the same embedded quartic. This alternative gives an everywhere independent homogeneous kernel basis, including both endpoints, rather than recovering the splitting only from a generic rank or the two-chart extension. Its original independent source review and exact companion computation are reused.

## 1. Euler and homogeneous derivative presentation

The pulled-back Euler sequence and the tangent sequence give

    0 -> O_P1(1)^2 -> O_P1(4)^4 -> N_C0/P3 -> 0.

To justify the left term, the two homogeneous partial derivative columns
map `O(1)^2` into `O(4)^4`. Their span contains the radial Euler column
since `s*d_s j+t*d_t j=4*j`; after quotienting that radial column the
induced map is the actual tangent map. Characteristic zero ensures `4`
is invertible. The resulting rank-two subbundle is therefore precisely
the preimage of `T_P1` in the Euler bundle. Dualizing yields

    0 -> N_C0/P3^* -> O_P1(-4)^4 --J--> O_P1(-1)^2 -> 0,

where

    J = [[4s^3,3s^2t,t^3,0],
         [0,s^3,3st^2,4t^3]].

The `4x2` cubic matrix

    V = [[-2t^3,0],
         [3st^2,t^3],
         [-s^3,-3s^2t],
         [0,2s^3]]

satisfies `JV=0`. Its six maximal minors are, in row-pair order,

    -2t^6, 6s^2t^4, -4s^3t^3,
    -8s^3t^3, 6s^4t^2, -2s^6.

They have no common projective zero: the first is nonzero when `t!=0`
and the last when `s!=0`. Thus `V` gives a rank-two subbundle

    O_P1(-7)^2 -> ker(J)=N_C0/P3^*.

It is an isomorphism on every fiber, hence an isomorphism of vector
bundles. Therefore

    N_C0/P3 = O_P1(7) (+) O_P1(7).

This proves the splitting without a generic-rank argument or a computer
inference. The exact Macaulay2 companion checks the displayed identities
and projective rank conditions over `QQ`. All coefficients and minors
remain valid after any extension of an algebraically closed
characteristic-zero ground field.

## 2. Independent quadratic-kernel check

Write a potential degree-two derivative syzygy as

    u0=a0 s^2+a1 st+a2 t^2,
    u1=b0 s^2+b1 st+b2 t^2,
    u2=c0 s^2+c1 st+c2 t^2,
    u3=d0 s^2+d1 st+d2 t^2.

Comparing the six coefficients in each row of `J*u=0` gives

    4a0=0, 4a1+3b0=0, 4a2+3b1=0,
    3b2+c0=0, c1=0, c2=0,
    b0=0, b1=0, b2+3c0=0,
    3c1+4d0=0, 3c2+4d1=0, 4d2=0.

The only residual pair is `c0=-3b2`, `b2+3c0=-8b2=0`, so all
twelve coefficients vanish. The companion verifies that the determinant
of this `12x12` coefficient matrix has absolute value `2^15`.
Consequently `H0(N^*(6))=0`, independently excluding `O(6)(+)O(8)`.
The two cubic columns above then provide the full splitting directly.

The repository already contains this splitting as P-009 in
the transition proof at the start of this chapter, via a two-chart conormal
calculation and [`verify_normal_bundle.py`](../computations/verify_normal_bundle.py).
The new source supplies a short, independently runnable certificate under
the currently available Macaulay2 runtime. It does not count the old
result as a new theorem.


The retained exact companion is [the homogeneous normal-bundle verifier](../computations/verify_session_quartic_normal_bundle_2026_10_10.m2). The conditional ribbon application is owned by the quartic-carrier bisection proof and is not duplicated here.
