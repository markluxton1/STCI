# An intrinsic K3 obstruction to a quartic–quartic thickening

Date: 2026-10-23. **New proof proposal; independent review pending.**

## Claim and scope

Let \(k\) be an algebraically closed field of characteristic zero and let

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k.
\]

There are no homogeneous quartics \(F,G\) with
\(\sqrt{(F,G)}=I_C\). Reducible and nonreduced equations are included.

The argument below uses the balanced conormal bundle, the elementary
saturated Gorenstein pairing theorem, and the geometry of rational double
points on quartic surfaces. It does **not** use the prior quartic-carrier
exclusion, the primitive-triple classification, any classification of
quartic contact pencils, or their cubic-contact determinants.

Its geometric obstruction is that a general member of the hypothetical
quartic pencil would have too many independent exceptional curves on its
K3 resolution. The local defect points do not evade that obstruction:
their rational double points replace the apparent loss of moving
singularities.

## Exact dependencies and status

1. The promoted result
   [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md) gives
   \(E=N^*_{C/\mathbf P^3}=\mathcal O_{\mathbf P^1}(-7)^2\).
   Also \(\mathcal O_C(1)=\mathcal O_{\mathbf P^1}(4)\), and the unique
   quadric containing \(C\) is the smooth quadric
   \(q=x_0x_3-x_1x_2\); \(C\) has class \((3,1)\), up to exchanging the
   rulings.
2. The accepted source-level
   [saturated pairing audit](2026-10-05-mf6-pairing-audit.md), sections 1–2,
   proves that a finite-free Gorenstein algebra with generic fiber
   \(K[v]/(v^4)\) has invertible saturated layers and perfect multiplication
   \(E_1\otimes E_2\longrightarrow E_3\).
   This is a general local-algebra theorem, not the inherited primitive
   classification. We use that accepted theorem without rerunning it.
3. Standard characteristic-zero surface facts: an \(A_j\) surface
   singularity has a chain of \(j\) independent exceptional \((-2)\)-curves;
   the minimal resolution of an integral quartic with only rational double
   points is a K3 surface; over characteristic zero its Picard rank is at
   most 20. Primary references are
   [Morrison, *The Geometry of K3 Surfaces*](https://web.math.ucsb.edu/~drm/conferences/ITP99/morrison/cortona.pdf),
   pp. 5–6, and
   [Shimada, *Rational Double Points on Supersingular K3 Surfaces*](https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/RDPssK3/rdpssk3.pdf),
   introduction. Shimada records the stronger characteristic-zero bound
   19 on the total exceptional rank of a projective K3 model; the weaker
   bound 20 already suffices below.

Everything after these inputs is derived here. This file is a proposal,
not a promotion of a new canonical result.

Supporting artifacts are the independently developed
[local-algebra note](2026-10-23-intrinsic-quadruple-local-algebra.md), the
[exact local verification script](../computations/verify_intrinsic_quadruple_local_algebra_2026_10_23.py),
and the
[independent proof audit](2026-10-23-intrinsic-44-k3-independent-audit.md).
The script checks representative polynomial identities and Milnor-algebra
dimensions; the argument for arbitrary formal unit coefficients is the
proof below, together with the local-algebra note. It is not inferred
from a finite collection of examples.

## 1. Generic order and the saturated numerical types

Suppose such \(F,G\) exist and put \(Z=V(F,G)\). They have no common
surface component, hence form a regular sequence. Thus \(Z\) is a
Gorenstein complete-intersection curve, of degree 16, with reduced support
\(C\). Its generic transverse length is \(16/4=4\), and

\[
\omega_Z=\mathcal O_Z(4).
\tag{1}
\]

First, a quartic having normal order at least two on \(C\) must be a
multiple of \(q^2\). Indeed, its restriction to the smooth quadric belongs
to

\[
H^0\bigl(Q,\mathcal O_Q((4,4)-2(3,1))\bigr)=0.
\]

It is therefore \(qH\) for a quadric \(H\); its first normal symbol is
\(H|_C\) times the nonzero symbol of \(q\), so \(H|_C=0\). Uniqueness of the
quadric gives \(H\in kq\). Generic normal order at least two suffices:
the first-symbol sheaf is locally free on \(C\), so generic vanishing is
everywhere vanishing.

Such a quartic cannot occur in the supposed pair. If it is \(q^2\), the
other equation restricts on \(Q\) to a divisor of class \((4,4)\) supported
only on \(C\). That would require \((4,4)=m(3,1)\), which is impossible.
If the other restriction is identically zero, the pair has a common
quadric instead. Consequently both equations have generic normal order
one. Their generic first symbols must be dependent, since independent
symbols would give transverse length one. The generic local algebra is
therefore \(K[v]/(v^4)\).

Let \(N_i\) denote the saturated nilpotent filtration on \(\mathcal O_Z\),
and \(E_i=N_i/N_{i+1}\), for \(0\leq i\leq3\). Locally this is exactly

\[
N_i=B\cap(v^i)B_K.
\]

Write \(L=E_1\). The conormal sheaf surjects onto \(L\), so

\[
L=\mathcal O(e-7),\qquad e\geq0.
\tag{2}
\]

The saturated top layer is the annihilator of the nilradical. Finite
duality for the closed immersion \(C\hookrightarrow Z\), combined with
(1), gives

\[
E_3=\operatorname{Hom}_{\mathcal O_Z}(\mathcal O_C,\mathcal O_Z)
    =\omega_C\otimes(\omega_Z|_C)^{-1}
    =\mathcal O(-18).
\tag{3}
\]

Multiplication \(L^2\longrightarrow E_2\) is generically invertible;
write its effective zero divisor as \(D\), so \(E_2=L^2(D)\).
The perfect pairing \(L\otimes E_2\simeq E_3\) identifies

\[
E_3=L^3(D),\qquad d:=\deg D=3-3e.
\tag{4}
\]

Effectivity leaves exactly \(e=0,d=3\) and \(e=1,d=0\). No classification
of embedded triples has entered this reduction.

## 2. The local defect algebra

Here is the key local construction, valid for any multiplicity-four
Gorenstein structure under these filtration hypotheses in characteristic
different from two.

Fix \(p\in C\), put \(R=k[[t]]\), and complete \(Z\) at \(p\). A lift of
the support parameter \(t\) to the ambient regular local ring provides a
map \(R\longrightarrow B=\widehat{\mathcal O}_{Z,p}\). The algebra \(B\)
is finite over \(R\), and is free of rank four: finiteness follows from
the Artin special fiber, while \(t\) is a nonzerodivisor because \(Z\) is
Cohen–Macaulay with smooth reduced support. The quotient by its
nilradical is \(R\).

Choose \(y\in N_1\) lifting a basis of \(E_1\), and \(x\in N_2\) lifting a
basis of \(E_2\). Since \(E_1E_2\longrightarrow E_3\) is perfect, we may
choose the basis of \(N_3=E_3\) to be \(z=xy\). Then

\[
B=R\cdot1\oplus R\cdot y\oplus R\cdot x\oplus R\cdot z,
\quad y^2=a(t)x+b(t)z.
\]

All of \(x^2,yz,xz,z^2\) vanish, since \(N_iN_j\subset N_{i+j}\) and
\(N_4=0\). Replacing \(y\) by \(y-bx/2\) leaves \(xy=z\) and changes the
square relation to \(y^2=ax\). The vanishing order of \(a\) is exactly
\(d_p=\operatorname{mult}_pD\), by the definition of \(D\). Consequently

\[
B\simeq R[x,y]/(x^2,\ y^2-a(t)x),\qquad
\operatorname{ord}_t a=d_p.
\tag{5}
\]

This is an algebra isomorphism: the displayed quotient is free on
\(1,y,x,xy\), and the indicated map sends this basis to the adapted
basis of \(B\).

When \(d_p>0\), the elements \(t,x,y\) are independent modulo the square
of the maximal ideal of \(B\), since both displayed relations have order
at least two. Lifting \(x,y\) to ambient functions therefore gives a
regular system of parameters \(t,x,y\) in the completed ambient ring.
In those ambient coordinates the completed ideal of \(Z\) is exactly

\[
J=(x^2,\ y^2-a(t)x)\subset k[[t,x,y]].
\tag{6}
\]

Indeed, the induced surjection from the regular power-series ring has
the quotient (5), so its kernel is the two indicated relations. Thus (6)
is an embedded formal normal form, not merely an abstract algebra model.

When \(d_p=0\), equation (5) eliminates \(x\) and gives
\(B\simeq R[y]/(y^4)\). Equivalently, suitable ambient formal coordinates
\(t,m,l\) identify the ideal with

\[
J=(m,l^4).
\tag{7}
\]

In particular, \(D\) is precisely the nonprimitive locus.

## 3. The actual first-symbol pencil and its fixed divisor

Let \(M=\ker(E\longrightarrow L)\). It is a line bundle and

\[
M=\mathcal O(-7-e).
\tag{8}
\]

The first symbols of the actual global quartics \(F,G\) are sections
\(h_F,h_G\in H^0(C,M(16))\). This assertion uses actual equations, not
arbitrary abstract sections of the conormal bundle.

Their common zero divisor is exactly \(D\). To see this at a defect
point, write \(F,G\) in terms of the generators in (6). Their coefficient
matrix is invertible over the completed ambient local ring: both are
minimal generating sets of the same complete-intersection ideal. In
particular, their coefficients of \(y^2-ax\), restricted to \(C\), generate
the unit ideal. The first symbols are precisely those coefficients
times \(-a\bar x\). Hence their common vanishing order is exactly
\(\operatorname{ord}_t a=d_p\). At a primitive point the same conclusion
with zero common vanishing follows from (7), since the coefficients of
\(m\) generate the unit ideal.

Dividing the two sections by their common fixed divisor therefore gives
a basepoint-free pencil in

\[
M(16)(-D)=\mathcal O(n),\qquad
n=(9-e)-(3-3e)=6+2e.
\tag{9}
\]

Because \(n>0\), these two generating sections cannot be proportional:
that would give a nowhere-vanishing section of a positive-degree line
bundle. The associated map \(C\longrightarrow\mathbf P^1\) is therefore
nonconstant. In characteristic zero it is separable. Thus a general
member of this pencil has exactly \(n\) distinct zeros, avoiding the
finite support of \(D\). Equivalently, a general quartic in the original
pencil has \(n\) simple first-symbol zeros away from the defects.

No surjectivity of the global jet map is asserted or needed: the
basepoint-free pencil just obtained is the pencil furnished by the
hypothetical equations themselves.

## 4. Surface singularities of a general pencil member

Let \(X=V(\lambda F+\mu G)\) for a general \([\lambda:\mu]\).
Off \(C\), smoothness follows from the characteristic-zero Bertini
theorem, applied to the pencil with its base locus removed. Along \(C\)
the complete formal models determine all singularities.

At a primitive point, use (7). At a zero of the moving first-symbol
section, choose another member of the pencil whose \(m\)-coefficient is
a unit, and take its equation as the ambient parameter \(m\). Because
the two equations generate \(J\), the selected equation then has form

\[
X:\quad A(t,m,l)m+U(t,m,l)l^4=0,\qquad U(0)\ne0.
\]

The zero of \(A(t,0,0)\) is simple, so \(\partial A/\partial t(0)\ne0\).
The change \(T=A(t,m,l)/U(t,m,l)\), \(M=m\), \(L=l\) is formally
invertible and identifies the equation, up to a unit, with

\[
TM+L^4=0.
\tag{10}
\]

This is an \(A_3\) rational double point. At every other primitive point
the nonzero first symbol makes \(X\) smooth. Equation (9) consequently
produces exactly \(n=6+2e\) singularities of type \(A_3\) outside \(D\).

At a defect point of multiplicity \(d_p>0\), write the general equation
using (6):

\[
f=\alpha(t,x,y)x^2+\beta(t,x,y)(y^2-a(t)x).
\tag{11}
\]

For a general member, \(\alpha(0)\beta(0)\ne0\), because the generator
matrix is invertible and there are only finitely many defect points.
The coefficients here are arbitrary formal functions; they are not
being assumed constant. Divide (11) by the unit \(\beta\), and put
\(u=\alpha/\beta\). The equation becomes

\[
f'=u(t,x,y)x^2+y^2-a(t)x.
\tag{12}
\]

The Hessian in \(x,y\), at \(t=x=y=0\), is invertible. The formal implicit
function theorem solves \(f'_x=f'_y=0\) as

\[
x_c(t)=\frac{a(t)}{2u(t,0,0)}+O(a(t)^2),\qquad
y_c(t)=O(a(t)^2).
\]

The critical value is

\[
g(t)=f'(t,x_c(t),y_c(t))
     =-\frac{a(t)^2}{4u(t,0,0)}+O(a(t)^3).
\tag{13}
\]

In particular, it has order exactly \(2d_p\), with nonzero leading
coefficient. The formal Morse lemma with parameter \(t\) writes (12) as
a nondegenerate quadratic form in two new variables plus \(g(t)\).
Over the algebraically closed characteristic-zero field, a unit has a
\(2d_p\)-th root, so a further change of \(t\) identifies the completed
surface germ with

\[
XY+T^{2d_p}=0.
\tag{14}
\]

This is an \(A_{2d_p-1}\) rational double point. This calculation includes
\(d_p=1\), where the germ is an ordinary node.

These are all singularities of \(X\), and they are isolated. Therefore
\(X\) is integral and normal: a repeated surface component is singular
along that component, while two distinct projective surface components
meet in a curve along which their union is singular. Both contradict
the established finite singular locus. An integral hypersurface is
Cohen–Macaulay; isolated singularities then imply normality by Serre's
criterion.

## 5. The K3 contradiction

The minimal resolution \(\widetilde X\to X\) is a K3 surface. Let
\(r=\#\operatorname{Supp}D\), so \(r=0\) when \(e=1\), and \(1\leq r\leq3\)
when \(e=0\). The exceptional curves above distinct singularities have
orthogonal negative-definite intersection matrices; the number of
independent exceptional classes is consequently

\[
\begin{aligned}
R
&=3n+\sum_{p\in\operatorname{Supp}D}(2d_p-1)\\
&=3(6+2e)+2(3-3e)-r\\
&=24-r.
\end{aligned}
\tag{15}
\]

If \(e=1\), this is 24. If \(e=0\), it is at least 21. Both exceed the
characteristic-zero bound \(\rho(\widetilde X)\leq20\). This contradicts
the existence of \(F,G\).

For an arbitrary algebraically closed characteristic-zero field, choose
a finitely generated subfield containing the coefficients of the two
equations, and take its algebraic closure inside \(k\). The resulting
algebraically closed subfield \(k_0\) has finite transcendence degree and
embeds into \(\mathbf C\). The assertion that the sole reduced support is
\(C\) descends to \(k_0\) by faithful flatness. Make the construction above
over \(k_0\), then extend that construction to \(\mathbf C\). Smoothness
off the stated points, the ADE types, and the exceptional intersection
matrices are preserved under algebraically closed base extension. The
complex K3 Picard bound therefore gives the same contradiction. No
embedding of the whole original field into \(\mathbf C\) is required.

## Characteristic boundary and proof-ingredient replacement

The proof uses characteristic zero in the separability of the moving
first-symbol pencil and in the K3 Picard bound. The local normal-form
argument also uses that two is invertible. In characteristic two the
conormal bundle itself changes, so the numerical setup (2)–(9) changes
as well. Thus the explicit characteristic-two positive example is
consistent with this argument; the proof does not assert that its
general pencil member has eight distinct \(A_3\) singularities.

The prior primitive \(e=1\) classification is replaced by the eight
moving \(A_3\) points and the K3 bound. The prior \(e=0\) direction
classification is replaced by the defect algebra (5), the resulting
\(A_{2d_p-1}\) points, and the same bound. All explicit cubic-contact
nonvanishing checks and quartic-pencil enumeration are unnecessary for
this proof. The general saturated pairing input remains an explicit
dependency; the conormal splitting remains the only special numerical
input from the fixed embedding beyond the smooth-quadric facts.

This proves only the stated quartic–quartic exclusion, subject to
independent review of this new argument. It does not establish an
all-degree quartic-carrier theorem or settle the unrestricted STCI
question.
