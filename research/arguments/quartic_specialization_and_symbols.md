---
id: STCI-A-0004
type: argument
title: Conormal splitting, mu4 specialization and actual quartic symbols
status: complete
scope: "#scope"
conclusion: "#conclusion"
---
# Conormal splitting, mu4 specialization and actual quartic symbols

## Scope

Fix the smooth embedded quartic \(C=C_0=[s^4:s^3t:st^3:t^4]\) in \(\mathbf P^3_k\).
Its two parameter charts have inverse parameters \(x_1/x_0=t/s\) and
\(x_2/x_3=s/t\), and cover \(C\). Write \(I=\mathcal I_C\),
\(E=I/I^2\), \(\mathcal O(n)=\mathcal O_{\mathbf P^1}(n)\), and
\(E(d)=E\otimes\mathcal O_{\mathbf P^1}(4d)\) for an ambient twist.
The transition and actual quartic-symbol calculations hold over any field.
The prescribed integral intersection is compared over geometric fibers of
characteristics zero and two. The homogeneous Euler/Jacobian route proves only
the characteristic-zero splitting.

The [equation-module comparison](../results/quartic_char2_fourth_equation_kernel.md)
identifies the fourth minimal initial equation with a canonical kernel for
the prescribed characteristic-two pair. The
[arithmetic ruled model](../results/quartic_arithmetic_ruled_models.md) studies
the conductor, the arithmetic four-section and its endpoint images on a ruled
surface. The calculations here are for the projective intersection downstairs.

## Conormal transition (P-009): characteristic jump in the normal bundle of \(C_0\)

The unique containing quadric is \(Q=V(q)\), where
\(q=x_0x_3-x_1x_2\). Indeed the degree-two monomials restrict to the nine
parameter monomials of degree eight, since the sums of two exponents from
\(\{0,1,3,4\}\) fill \(\{0,\ldots,8\}\). In Segre coordinates
\([x_0:x_1:x_2:x_3]=[a_0b_0:a_1b_0:a_0b_1:a_1b_1]\), the curve is the graph
\(([s:t],[s^3:t^3])\), a divisor of class \((3,1)\).
The conormal line of \(Q\) on \(C\) is \(\mathcal O(-8)\) and
\(\mathcal O_Q(-C)|_C=\mathcal O(-6)\).

On the \(x_0\ne0\) chart use \((y,z,w)=(x_1,x_2,x_3)/x_0\). Write the curve as

\[
y=u,\qquad z=u^3,\qquad w=u^4,
\]

with conormal generators \(a=z-y^3\), \(b=w-y^4\).  On the \(x_3\ne0\)
chart put

\[
\alpha=Y'-(Z')^3,\qquad\beta=X'-(Z')^4.
\]

Substitute \(Y'=u/(u^4+b)\), \(Z'=(u^3+a)/(u^4+b)\) and
\(X'=1/(u^4+b)\), and use \((1+b/u^4)^{-n}=1-nb/u^4\) modulo
\((a,b)^2\). This gives

\[
\binom{\alpha}{\beta}=
\begin{pmatrix}
-3u^{-6}&2u^{-7}\\
-4u^{-7}&3u^{-8}
\end{pmatrix}
\binom a b,
\qquad \det=-u^{-14}.
\]

Use the quadric conormal generator \(q_s=b-ua\), with
\(q_t=\beta-u^{-1}\alpha=u^{-8}q_s\) in the conormal sheaf, and take
\(r_s=a,r_t=-\alpha\).  Then

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
unless the characteristic is two. When two is invertible, the first-chart
frame \(U=q_s-\tfrac12ur_s=b-\tfrac32ua,\ V=r_s\) has opposite frame
\((u^{-7}U,u^{-7}V)=(-\tfrac12r_t,2q_t+u^{-1}r_t)\). This is a frame on the
entire opposite chart, including \(s=0\). In characteristic two,
\((q_s,r_s)\) and \((q_t,r_t)\) already give diagonal transitions. Hence

\[
N_{C_0/\mathbf P^3}\cong
\begin{cases}
\mathcal O(7)\oplus\mathcal O(7),&\operatorname{char}k\ne2,\\
\mathcal O(6)\oplus\mathcal O(8),&\operatorname{char}k=2.
\end{cases}
\]

For all \(r\ge 0\), these splittings give the ambient twisted bundles
\[
(\operatorname{Sym}^r E)(d)=
\begin{cases}
\mathcal O(4d-7r)^{\oplus(r+1)}, & \operatorname{char}k\ne 2,\\
\displaystyle\bigoplus_{i=0}^r\mathcal O(4d-8r+2i), & \operatorname{char}k=2.
\end{cases}
\]
Regular embedding gives \(\operatorname{gr}_I\mathcal O_{\mathbf P^3}
=\operatorname{Sym}^\bullet E\) on the entire curve. Global normal order
is membership in a sheaf power of \(I\), equivalently in the corresponding
saturated homogeneous ideal.

### Characteristic-three primitive triple

In characteristic three take the cubic \(x_1^3-x_0^2x_2\) and quartic
\(x_0x_3^3-x_2^4\). On the first chart the cubic is \(-a\) and the quartic
reduces modulo \(a\) to \(b^3\). On the opposite chart the quartic is
\(\beta\) and the cubic reduces modulo \(\beta\) to \(\alpha^3\).
At \(x_0=0\) these equations force \(x_1=x_2=0\), so the two charts
cover the intersection. The local ideals \((a,b^3)\) and \((\beta,\alpha^3)\)
give a primitive triple. Modulo \(a\) in characteristic three the transition
of its remaining conormal generator is \(\alpha=2u^{-7}b\) to first order.
Hence its graded algebra has pieces
\(\mathcal O_C,\mathcal O(-7),\mathcal O(-14)\), and
\(\chi=1+(1-7)+(1-14)=-18\) gives arithmetic genus \(19\).

## The prescribed mu4 intersection and actual quartic symbols

The next sections separate the flat projective family, the associated graded
algebra of its curve-ideal filtration, and the source of actual normal symbols
of any quartic through \(C\). Their proof and review scopes are distinct.

## 1. What actually coalesces

Consider the integral equations

\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3.
\]

Their projective intersection is a flat family over \(\mathbf Z\). Indeed its
homogeneous coordinate ring is free over \(\mathbf Z[x_0,x_3]\), with basis
\(x_1^a x_2^b\), \(0\le a,b<4\): the two relations are monic in separate
variables. In particular every graded piece is a free abelian group. Homogeneous
localization preserves flatness over \(\mathbf Z\), as does taking its
degree-zero direct summand. This proves flatness of Proj.

On \(x_0=1\), put

\[
u=x_1,\qquad X=x_3-u^4,\qquad Y=x_2-u^3.
\]

Then \(I_C=(X,Y)\), \(F=-X\), and, modulo \(F\),

\[
P=(u^3+Y)^4-u^{12}
 =Y^4+4u^3Y^3+6u^6Y^2+4u^9Y.                 \tag{1}
\]
Before taking the quotient, \(G=P-3u^8X-3u^4X^2-X^3\), so the chart
ideal is \((X,P)\). The coordinate reversal
\((x_0,x_1,x_2,x_3)\mapsto(x_3,x_2,x_1,x_0)\) interchanges \(F,G\)
and gives the opposite chart with \((u,X,Y)\) replaced by \((c,A,B)\).

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

Outside the open in (2) only the two endpoints are possible. At
\(x_0=0\) the equations force \(x_1=x_2=0\), and on \(x_0=1,u=0\)
they force \(x_2=x_3=0\). At \(x_3=0\) they likewise force \(x_1=x_2=0\).
Thus the two affine charts cover the intersection and the ideal has height
two in every field fiber. In characteristic zero the four components
already have total degree sixteen. The complete intersection is
Cohen--Macaulay and generically reduced along each, so is the reduced
scheme union of the four quartics.

In characteristic two,

\[
z^4-1=(z-1)^4,\qquad (F,G)|_{x_0\ne0}=(X,Y^4).
\]

The analogous chart \(x_3\ne0\) has coordinates
\(c=x_2/x_3\), \(A=x_0/x_3-c^4\), \(B=x_1/x_3-c^3\), and ideal
\((A,B^4)\). These charts cover the intersection, proving its reduced support
is exactly \(C\). The generic transverse algebra is \(k(C)[Y]/(Y^4)\).

Thus the four sheets are **four geometric curve components in characteristic
zero**, indexed by the geometric points of \(\mu_4\). In characteristic two
the group scheme has one point with length four. Its nonreduced direction
becomes the transverse thickness of the single support curve. This is a
finite-flat scheme description of coalescence.

There is a numerical check at the endpoints. In the smooth surface
\(F=0\) near \([1:0:0:0]\), the four branches are
\(Y=(\zeta-1)u^3\); every pair has intersection multiplicity three.
At the other endpoint on \(G=0\), the branch \(C_\zeta\) has
\(x_0/x_3=c^4\) and \(x_1/x_3=\zeta c^3\), so the same pairwise
multiplicity is three.
The delta invariant of a reduced planar union of smooth branches is the
sum of their pairwise intersection multiplicities. There are six pairs
at each endpoint, giving delta eighteen there and arithmetic genus
\(36-4+1=33\). The equation of the residual union on \(F=0\) is
\(\prod_{\zeta\ne 1}(Y-(\zeta-1)u^3)\). Its restriction to \(C\) has order
nine at \(p_0\). The analogous product on \(G=0\) has order nine at
\(p_\infty\), so the residual contact cycle is \(9p_0+9p_\infty\).

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

In characteristic two the first symbols are \(-X\) and \(u^8X\), so
they generate just \((X)\). In both cases the symbol of an ambient
coordinate means its class in normal degree one.
The combination \(G-(3u^8+3u^4X+X^2)F=P\) specializes to \(Y^4\).
The exact ideal in that fiber is already homogeneous in the normal
variables. Hence

\[
\operatorname{in}_{I_C}(F,G)=(X,Y^4),\qquad
\operatorname{gr}_{I_C}\mathcal O_{V(F,G),\eta_C}
 \simeq K[Y]/(Y^4).                           \tag{3}
\]

The initial ideal of the pair is therefore strictly larger than the ideal
generated by their two first symbols. The additional minimal generator occurs in order four.

The positive graded pieces in characteristic zero have endpoint support.
On the full \(u\) chart, (1) gives

\[
\operatorname{gr}_{I_C}\mathcal O_{V(F,G)}
 \simeq k[u,Y]/(u^9Y).
\]

The full initial ideal in the ambient normal algebra is
\((X,4u^9Y)\). The positive pieces are torsion at \(u=0\); the same
calculation with \(A,B,c\) on the opposite chart gives torsion at infinity.
The vertical support of the cone over the endpoints records where residual
branches meet \(C\). The residual curves downstairs are the three
\(C_\zeta\) with \(\zeta\ne1\) from §1. In the determinant trivialization
oriented by \((X,Y)\), the determinant of the two first-normal sections is
\(-4s^9t^9\), a section of \(\det(E(4))=\mathcal O_{\mathbf P^1}(18)\),
where the notation \(E(4)\) means the ambient twist by
\(\mathcal O_C(4)=\mathcal O_{\mathbf P^1}(16)\).

The same coefficient has three interpretations:

\[
P'_Y(u,0)=4u^9
 =\prod_{\zeta\ne1}\bigl((1-\zeta)u^3\bigr).
\]

This is the derivative at the identity after rewriting the roots-of-unity
equation in \(Y\), with scaling factor \(u^{12}/u^3\) relative to
\(z^4-1\). Up to the determinant sign it is also the determinant coefficient,
and the product records the separations from the three residual branches.

There is also an explicit failure of base change for the normal filtration.
For the integral chart \(\mathscr A=\mathbf Z[u,Y]/(P)\) of (1),

\[
\operatorname{gr}_{(Y)}\mathscr A
 =\mathbf Z[u,\eta]/(4u^9\eta).
\]

Elimination of \(X\) identifies the filtered quotient with the
\(Y\)-adic quotient of \(\mathbf Z[u,Y]\) by \((P)\). The lowest
\(Y\)-term of every nonzero product \(hP\) is the product of the lowest
terms of \(h\) and \(P\), since \(\mathbf Z[u]\) is a domain. This
proves the full initial ideal, including at the endpoint. The same argument
over \(k[u]\) proves the displayed characteristic-zero formula. The
reduction of the integral associated graded algebra modulo two is \(\mathbf F_2[u,\eta]\), whereas

\[
\operatorname{gr}_{(Y)}(\mathscr A\otimes\mathbf F_2)
 =\mathbf F_2[u,\eta]/(\eta^4).
\]

The comparison map is the quotient by \((\eta^4)\). In the integral
associated graded algebra the class of \(u^9\eta\) is nonzero and killed
by four, so that algebra is not \(\mathbf Z\)-flat. Each filtration term
\((Y)^n\mathscr A\) is \(\mathbf Z\)-flat, being a submodule of the
\(\mathbf Z\)-flat \(\mathscr A\) and hence torsion-free. The failure
occurs in the successive quotients. The ambient regular embedding has its
usual symmetric-algebra normal cone in both fibers.

### The distinct conormal line generated by the first equation

Over \(\mathbf Z[1/3]\), the alternate frames with first-chart kernel
generator \(X\) and quotient lift \(Y\) have opposite-chart generators
\(3A-4u^{-1}B\) and \(-B/3\), where \(A=\beta\), \(B=\alpha\) in the
conormal sheaf. The transition matrix above gives
\[
3A-4u^{-1}B=u^{-8}X,\qquad
-B/3=u^{-6}Y-(2/3)u^{-7}X.
\]
These are an opposite-chart frame since its determinant in \((A,B)\) is
\(-1\). Its normalized cocycle is \(-(2/3)u^{-1}\). The kernel subline
generated by \(X\) differs from the quadric subline \(X-uY\) over the
dense parameter torus. The first quartic symbol \(-X\) thus does not
arise as the normal linear part of a quadratic equation through \(C\).

## 4. Which symmetric-algebra sections come from quartics?

The incomplete embedding remains visible in this calculation. Its degree-one
linear series is
\(W=\langle s^4,s^3t,st^3,t^4\rangle\), missing \(s^2t^2\).
The exponent sums in degree two fill \(\{0,\ldots,8\}\).
Adding \(0\) and \(4\) then gives the entire next interval at each step.
The homogeneous coordinate ring therefore has the full section space in
every degree at least two, with a one-dimensional deficiency in degree one. In particular

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

Its cokernel on sections is \(H^1(Q,\mathcal O_Q(-2,2))\simeq k^3\),
since \(H^1(Q,\mathcal O_Q(1,3))=0\). On the affine graph the
restriction of a monomial of bidegree \((1,3)\) has exponent \(i+3j\)
with \(0\le i\le1\), \(0\le j\le3\).
Let

\[
V_{10}=\operatorname{im}H^0(Q,\mathcal O_Q(1,3))
 =\langle1,u,u^3,u^4,u^6,u^7,u^9,u^{10}\rangle.
\]

The quotient conormal symbol is the restriction to \(C\) of the
quartic's residual section on \(Q\). Every section of \(\mathcal O_Q(1,3)\)
occurs by multiplying by the equation of \(C\) on \(Q\) and lifting the result
from \(H^0(\mathcal O_Q(4,4))\) to a quartic on \(\mathbf P^3\), using
\(H^1(\mathbf P^3,\mathcal O(2))=0\). Quadratics restrict onto
\(H^0(\mathcal O(8))\), so \(q\) times quadratics supplies the full
nine-dimensional kernel of the quotient conormal map on sections.
Therefore, in every characteristic,

\[
\operatorname{im}\sigma_1
 =\{\xi\in H^0(E(4)):\bar\xi\in V_{10}\},\qquad
\dim\operatorname{im}\sigma_1=17.                \tag{7}
\]

In characteristic two, the frame \(e=q_s,f=r_s\) makes this
\(H^0(\mathcal O(8))e\oplus V_{10}f\). A symbol
\(A(u)e+B(u)f\) is realizable exactly when
\(B_2=B_5=B_8=0\).
When two is invertible use the balanced frame \(U=b-\tfrac32ua,V=a\).
Both coefficients have degree at most nine in this affine trivialization.
The quotient conormal coefficient is \(R(u)-uP(u)/2\), since
\(U=q_s-\tfrac12u r_s\). Its vanishing coefficients in degrees \(2,5,8\)
give the exact realizability test

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
of \(Q\) gives \(H\in kq\). The second symbol of \(q^2\) is the square of the
nonzero quadric conormal generator. It is nonzero, so no nonzero quartic lies in
\(H^0(\mathbf P^3,I^3(4))\).

The full second-symbol targets are nevertheless

\[
(\operatorname{Sym}^2 E)(4)=
\begin{cases}
\mathcal O(2)^3,&\operatorname{char}k\ne 2,\\
\mathcal O(0)\oplus\mathcal O(2)\oplus\mathcal O(4),&\operatorname{char}2.
\end{cases}
\]

Both have nine sections; only one dimension is realized. There is no jump
in the rank of the quartic first-symbol map or in the dimension of its
kernel. The characteristic dependence lies in the conormal extension and
the higher compatibility of actual equations, not in an extra supply of
quartics of normal order two.

## 5. A uniform reduction of all (4,4) candidates

Every nonzero equation of order at least two is a scalar multiple of
\(q^2\) by (8). The same conclusion applies to a quartic vanishing to
order at least two generically, since its first symbol is a section of a
vector bundle on an integral curve. A quartic mate cuts
on \(Q\) a divisor of class \((4,4)\), which cannot have support just
\(C\) of class \((3,1)\). If the mate is divisible by \(q\), the common
locus contains \(Q\). Thus both equations of a sole-support pair have
normal order one.

A coprime quartic pair has pure curve intersection of degree sixteen.
Writing its cycle as \(m[C]+R\) with effective residual cycle \(R\), one
has \(16=4m+\deg R\). Sole support forces \(m=4\). Conversely \(m=4\)
forces \(\deg R=0\), so the degree and purity give sole support. The local algebra at \(\eta_C\) of a proper pair of normal orders
\((1,1)\) can be computed in its completion \(K[[X,Y]]\), where
\(K=k(C)\). Using one equation as a regular normal parameter, quotient
by it and express the other equation as a series in the remaining parameter.
Its order equals the local length. In particular, length four requires
dependent first symbols and first nonzero remaining term in order four.
The criterion uses the full series of the actual global equations.

The characteristic-two example passes the test by its exact chart
ideal \((X,Y^4)\). To use the criterion for a new pair one still needs
the global quartics and their coprimality.

## 6. What the symmetric algebra does and does not explain

The same normal bundle can support a curvilinear quotient that does
not come from the desired global equations. In every characteristic the
quadric conormal sequence gives a quotient \(E\twoheadrightarrow\mathcal O(-6)\), and therefore the
graded quotient

\[
\operatorname{Sym}^\bullet E\twoheadrightarrow
\mathcal O_C\oplus\mathcal O(-6)\oplus\mathcal O(-12)\oplus\mathcal O(-18)
=\operatorname{Sym}^\bullet(\mathcal O(-6))/\operatorname{Sym}^{\ge4}(\mathcal O(-6)).
\]

This algebra has precisely the graded line bundles and Hilbert polynomial
\(16d-32\) of the characteristic-two \((4,4)\) structure. The Cartier divisor \(4C\) on the smooth quadric \(Q\) realizes this
quotient as the graded algebra of an embedded primitive quadruple, since
its filtration has pieces \(\mathcal O_Q(-iC)|_C\) for \(0\le i<4\).
Its ideal contains \(q\). A \((4,4)\) complete-intersection ideal has no
sections in ambient degree two, by its Koszul resolution. The graded quotient and Hilbert polynomial therefore
do not suffice for ambient degree-four realization.

Nor does a bare symmetric algebra remember the nonlinear coordinate changes
needed for embedded higher neighborhoods. For the prescribed characteristic-
two quadruple the full overlap is

\[
c=u^{-1}+u^{-4}Y,\qquad
B=u^{-6}Y+u^{-9}Y^2+u^{-12}Y^3 \pmod{Y^4}.
\]

These formulas follow by substituting \(x_3/x_0=u^4\) in
\(c=x_2/x_3\) and \(B=x_1/x_3-c^3\). In particular the linear generator
changes by \(u^{-6}\), so the graded algebra of this quadruple is the same
truncated symmetric algebra and has Hilbert polynomial
\(\sum_{i=0}^3(4d-6i+1)=16d-32\).
The two graded algebras are isomorphic as graded \(\mathcal O_C\)-algebras.
As quotients of \(\operatorname{Sym}^\bullet E\), their degree-one kernels
are different. The Cartier divisor \(4C\) on \(Q\) kills \(q_s=X-uY\),
whereas the prescribed pair kills \(X\), as in the
[alternate conormal frame](#the-distinct-conormal-line-generated-by-the-first-equation).
The nonlinear overlap of the prescribed pair also retains the change in base
coordinate and the quadratic and cubic terms.

[STCI-R-0012](../results/prescribed_z4_arithmetic_nonlifting.md) rules out
a flat embedded lift with this prescribed special fiber and with the fixed
curve as generic reduced support, over \(\mathbf Z_{(2)}\) or \(\mathbf Z_2\).
Every such lift would force a primitive triple, whose free
\(H^1(\mathcal O(-4))\) obstruction has a Laurent coefficient congruent to
two modulo four. The flat family in §1 has four geometric components in its generic fiber.
The arithmetic obstruction is scoped to the two indicated bases and the
prescribed special fiber.


## An independent homogeneous Euler/Jacobian proof

Work over an algebraically closed characteristic-zero field with the same embedded quartic. This alternative gives an everywhere independent homogeneous kernel basis, including both endpoints, rather than recovering the splitting only from a generic rank or the two-chart extension. The October 10 audit checked this characteristic-zero route in its original scope.

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
Consequently `H0(N^* tensor O_P1(6))=0`, independently excluding `O(6)(+)O(8)`.
The two cubic columns above then provide the full splitting directly.

The [homogeneous normal-bundle verifier](../investigations/quartic-specialization-controls/verify_session_quartic_normal_bundle_2026_10_10.m2)
checks these same identities over \(\mathbf Q\). The separate conditional
ribbon application belongs to the quartic-carrier bisection argument.

## Conclusion

The conormal transition gives the characteristic jump
([R-0020](../results/quartic_conormal_characteristic_jump.md)).
The prescribed intersection is a flat integral family whose four reduced
geometric components in characteristic zero become one primitive quadruple
in characteristic two ([R-0021](../results/quartic_mu4_degeneration.md)).
Its full normal initial ideal exhibits a specific failure of base change
([R-0057](../results/quartic_normal_initial_base_change.md)).
The intrinsic degree-four restriction calculation determines the actual first
and second symbol images ([R-0058](../results/quartic_actual_symbols.md)).
These yield an exact normal-order reduction for actual coprime quartic
equations ([R-0059](../results/quartic_pair_normal_order_reduction.md)).
The Cartier quadruple on \(Q\) isolates the gap between realizing a normal
graded algebra and realizing it by two equations of the required degree.

## Source review and verification

The October 23, 2026 geometry/symbol audit is preserved in Git as
`d382837:research/notes/2026-10-23-quartic-geometry-symbol-independent-audit.md`.
It independently checked the monic flatness proof, four-component decomposition,
both endpoint contacts and the delta count, full normal initial ideals,
base change, the quadric and alternate conormal frames, and the actual
quartic symbol images. It used the previously established balanced splitting
as a premise. It inspected the
[Macaulay2 family check](../investigations/quartic-specialization-controls/verify_44_mu4_family_2026_10_23.m2)
and its successful log without rerunning that script in the audit. It
constructed and ran the
[exact symbol comparison](../investigations/quartic-specialization-controls/verify_44_quartic_symbol_comparison_2026_10_23.py)
over \(\mathbf Q\) and \(\mathbf F_2\) using all 35 quartic monomials
and the integral 18-column restriction kernel. The script checks the two
first-symbol matrices and the \(q^2\) kernel coordinates and reports the
second-symbol target dimensions from the conormal splittings.

The October 23 reconciliation
(`c7e9f78:research/RECONCILIATION_2026-10-23-44.md`) recorded the
scope-limited decisions for R-0020, R-0021 and the separate filtered
exclusion R-0022. Its [successful CI run](https://github.com/markluxton1/STCI/actions/runs/39972680627)
included the family and symbol checks and the separate filtered-contact
jobs. The geometry/symbol audit did not rerun the inherited quartic-carrier
exclusion or the arithmetic lifting obstruction.

The [transition verifier](../investigations/quartic-specialization-controls/verify_normal_bundle.py)
checks the two-chart normal transition, the quadratic Jacobian-syzygy matrix
and the characteristic-three triple. The October 10 independent audit
(`8d4ea1a:research/notes/2026-10-10-session-quartic-normal-bundle-independent-audit.md`)
gives the homogeneous Euler/Jacobian argument in characteristic zero and
records an exact execution of its companion check. Its conditional ribbon
argument requires the separate geometric hypotheses stated in that audit.
The computations corroborate the written proofs here. Current route review is
recorded with each Result.
