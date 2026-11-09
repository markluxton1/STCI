---
id: STCI-R-0064
type: result
title: A supported length-five family with a jump in the actual transverse defect
scope: "#scope"
statement: "#statement"
proofs:
  - name: finite free algebra and full equation filtration
    at: "#proof"
    using: [STCI-R-0030]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---

# A supported length-five family with a jump in the actual transverse defect

## Scope

Let \(k\) be any field, \(A=k[[t]]\), \(K=k((t))\), \(R=A[[x,y]]\),
and \(I=(x,y)\). The marked smooth curve is the formal \(t\)-axis.
We also use the polynomial model over \(k[t]\) on the affine \(t\)-axis
in \(\mathbf A^3_k\), and the ordinary homogenizations of its two equations
in \(\mathbf P^3_k\). All normal orders refer to the \((x,y)\)-adic
filtration. The actual transverse fibers are formed by specializing the
equations before computing their normal filtrations.

## Statement

Let
\[
f=x^2-txy+y^3,\qquad g=xy+ty^2-t^2x,\qquad J=(f,g).
\]
The quotient \(T=R/J\) has the free \(A\)-basis \(1,x,y,y^2,y^3\) and
\(\sqrt J=I\). The two equations form a regular sequence. The same freeness,
support and regular-sequence assertions hold over \(k[t]\) in the polynomial
model. The actual generic algebra over \(K\) is \(K[y]/(y^5)\) with normal
ideal \((y)\).

Put \(N=IT\), \(v=t^4x-t^3y^2\) and \(w=tv-t^2y^3\) in \(T\). The powers of
\(N\) are given by
\[
\begin{array}{c|l}
n&N^n\\ \hline
0&T\\
1&Ax\oplus Ay\oplus Ay^2\oplus Ay^3\\
2&A(t^2x)\oplus Ay^2\oplus Ay^3\\
3&Av\oplus Ay^3\\
4&Aw\\
n\ge5&0 .
\end{array}
\]
Writing \(S=A[X,Y]=\operatorname{gr}_I R\) and \(S_+=(X,Y)\), the full
initial ideals are
\[
\begin{aligned}
H=\operatorname{in}_I J&=(t^2X,\ X^2-tXY,\ tXY^2,\ XY^3,\ Y^5),\\
B=\operatorname{in}_I(IJ)&=S_+H\\
&=(X^3,\ X^2Y-tXY^2,\ t^2X^2,\ t^2XY,\ tXY^3,\ XY^4,\ Y^6).
\end{aligned}
\]
The actual equation module \(D=J/IJ=Ae_f\oplus Ae_g\) has its filtration
\(F^nD=((J\cap I^n)+IJ)/IJ\) and comparison modules
\(Q_n=(H/S_+H)_n\), \(G_n=\operatorname{gr}_F^nD\) as follows.
\[
\begin{array}{c|l|l|l}
n&F^nD&Q_n&G_n\\ \hline
1&Ae_f\oplus Ae_g&A&A\\
2&Ae_f&A/(t^2)&A/(t^2)\\
3&t^2Ae_f&A/(t)&A/(t)\\
4&t^3Ae_f&A/(t)&A/(t)\\
5&t^4Ae_f&A&A\\
n\ge6&0&0&0 .
\end{array}
\]
The comparison \(Q_n\to G_n\) is an isomorphism in every degree and
\(\Delta=\ker(Q\to G)=0\). In particular the generic defect vanishes.

The actual closed ideal \(J_0=(x^2+y^3,xy)\subset k[[x,y]]\) is a
length-five complete intersection supported at the origin. Its full
initial ideals are
\[
H_0^{\rm act}=(X^2,XY,Y^4),\qquad
B_0^{\rm act}=(X^3,X^2Y,XY^2,Y^4).
\]
Thus \(\Delta_0^{\rm act}\) is a copy of \(k\) in degree four, whereas
\(\Delta\otimes_A k=0\). The coefficient-specialization image of the
relative \(H\) is \(\overline H=(X^2,XY^3,Y^5)\). The quotient by this
image has length eight. In particular the relative normal graded
algebra does not specialize to the actual closed normal graded algebra.

The equations \(f,g\) are weighted homogeneous of weights six and five
for \(\mathrm{wt}(t,x,y)=(1,3,2)\). Their ordinary homogenizations are the
cubics
\[
F=zx^2-txy+y^3,\qquad G=zxy+ty^2-t^2x
\]
in \(\mathbf P^3_{[z:t:x:y]}\). The proper intersection of these cubics
has reduced support \(L\cup D_{\rm con}\) and cycle
\[
[V(F,G)]=5[L]+2[D_{\rm con}],\qquad
L=V(x,y),\quad D_{\rm con}=V(z,y^2-tx).
\]
The conic is a residual curve of degree two and contributes residual
cycle degree four.

## Proof

### The finite free actual algebra

Use the actual equations
\[
\begin{aligned}
f+tg&=x^2+y^3+t^2y^2-t^3x,\\
k_3&=txy^2-y^4=(t^2-y)f+(x-ty)g,\\
k_4&=xy^3=tk_3+y^2g,\\
k_5&=y^5=tk_4-yk_3 .
\end{aligned}
\]
In the quotient \(y^5=0\) and \(x^2\in(y)\), so \(x,y\) are nilpotent.
Since \(J\subset I\) and the marked axis is reduced, \(\sqrt J=I\).
Moreover
\[
\begin{aligned}
xy&=t^2x-ty^2, & x^2&=t^3x-t^2y^2-y^3,\\
xy^2&=t^4x-t^3y^2-ty^3, & y^4&=txy^2=t^5x-t^4y^2-t^2y^3.
\end{aligned}
\]
Multiplication of \(f=0\) by \(y\) gives \(x^2y=txy^2-y^4=0\).
Multiplication by \(x\) gives \(x^3=tx^2y-xy^3=0\). Together with
\(xy^3=y^5=0\), these reductions give the asserted five spanning
vectors and show \(I^5\subset J\).

For independence work first over the coefficient ring \(k[t]\).
On the free module with basis denoted by \(1,x,y,y^2,y^3\), define the
operators \(M_x,M_y\) by the following table. Use
\(a=t^2x-ty^2\), \(b=t^3x-t^2y^2-y^3\), and
\(c=t^4x-t^3y^2-ty^3\) as module vectors.
\[
\begin{array}{c|cc}
e&M_xe&M_ye\\ \hline
1&x&y\\
x&b&a\\
y&a&y^2\\
y^2&c&y^3\\
y^3&0&tc .
\end{array}
\]
The two compositions have common values \(a,0,c,0,0\) on the
successive basis vectors. In fact
\[
M_xa=t^2b-tc=0,\quad
M_yb=t^3a-t^2y^3-tc=0,\quad M_ya=t^2a-ty^3=c,\quad
M_yc=t^4a-t^3y^3-t^2c=0 .
\]
Here \(c=tb\) and \(M_x(tc)=t^5b-t^4c=0\). The operators therefore
commute and \(1\) is a cyclic vector. The polynomial relations \(f,g\)
give the vectors \(b-ta+y^3=0\) and \(a+ty^2-t^2x=0\) on \(1\), so
they annihilate the full module by commutation and cyclicity.
The polynomial quotient consequently maps to this module by evaluation on
\(1\), taking the proposed basis to a free basis. The same table over \(A\)
proves independence for the completed ring since the action kills \(I^5\)
and hence extends to \(A[[x,y]]\). This proves the finite free
presentations in both models. They are also compatible with localization
at the origin and completion there. In both regular ambient rings, \(f\)
is a nonzerodivisor and the associated primes of \((f)\) have height one.
Since \(J\) has height two, \(g\) belongs to none of these primes. This
proves the regular-sequence assertion.

For the actual generic algebra, \(t^2-y\) is invertible in \(T\otimes_A K\)
since \(y\) is nilpotent and \(t^2\) is a unit. The equation \(g=0\) gives
\(x=ty^2/(t^2-y)\), which lies in \((y^2)\). Hence \(K[y]/(y^5)\)
surjects onto \(T\otimes_A K\), and their common dimension five makes this
an isomorphism with \(N_K=(y)\). The integer identities in this proof
apply in every characteristic.

### The full normal initial ideal

In the actual algebra the normal monomials of degree at least two
reduce to the span of \(t^2x,y^2,y^3\), each of which is in \(N^2\)
by \(t^2x=xy+ty^2\). Those of degree at least three are spanned by
\(y^3,xy^2,y^4\) because \(x^2y=x^3=xy^3=y^5=0\).
Since \(xy^2=v-ty^3\) and \(y^4=txy^2=w\), this gives the asserted
third and fourth powers. The first power is the span of the nonconstant
basis vectors, and the directness of the stated sums follows from
the coefficients of those vectors in the free presentation over \(A\).

The symbols of \(g,f,k_3,k_4,k_5\) give the inclusion
\((t^2X,X^2-tXY,tXY^2,XY^3,Y^5)\subset H\). Let \(H'\) denote the
displayed candidate. In degree one \(S/H'\) has pieces \(AY\) and
\((A/(t^2))X\). In degree two eliminate \(X^2=tXY\), leaving
\(AY^2\oplus(A/(t^2))XY\). In degree three the same elimination
leaves \(AY^3\oplus(A/(t))XY^2\), since \(tXY^2=0\). In degree four
only \(AY^4\) survives, and degrees at least five vanish. Degree zero
is \(A\).

Under the natural map to \(\operatorname{gr}_N T\), degree one identifies
with \(N/N^2\) by the power table. In degree two the quotient
\(N^2/N^3\) has the presentation on \(t^2x,y^2\) with relation
\(t^4x-t^3y^2=t^2(xy)\). Replacing \(t^2x\) by \(xy=t^2x-ty^2\)
makes it the indicated free-plus-torsion presentation. In degree three
\(N^3/N^4\) is presented on \(v,y^3\) with relation \(w=t(v-ty^3)\).
Replacing \(v\) by \(xy^2=v-ty^3\) gives the degree-three isomorphism.
In degree four \(w=y^4\) freely generates \(N^4\).
In degree zero and degrees at least five the identifications follow
directly. This proves \(S/H'=\operatorname{gr}_N T\) in all degrees,
so \(H'=H\). Over \(K\) this is the initial ideal \((X,Y^5)\).

### Filtered actual equations and comparison

The syzygies of the regular sequence \(f,g\) are generated by \((-g,f)\),
whose entries belong to \(I\). Thus \(J/IJ\) is freely generated over
\(A\) by the two equation classes. The identities for the \(k_i\) give
\[
[k_3]=t^2e_f,\qquad [k_4]=t^3e_f,\qquad [k_5]=t^4e_f .
\]
To compute \(F^nD\), start with an equation in \(J\cap I^n\) and write its
lowest nonzero symbol as a homogeneous combination of the generators
of \(H\). Subtract that combination of \(g,f,k_3,k_4,k_5\) with
multipliers lifted to the same normal degrees. The remainder is still
in \(J\) and has higher order. Only degree-zero multipliers contribute
in \(D\), and these use lifts of order at least \(n\). Repeat up to
order six, where \(I^6\subset IJ\) because \(I^5\subset J\). This proves
that \(F^nD\) is spanned by the classes of exactly the displayed lifts
of order at least \(n\), which belong to the filtration by construction.
It gives the stated \(F^nD\) and \(G_n\). The free piece of \(G\) in
degree five is generated by \(t^4e_f\), as a submodule of \(D\).

For \(Q_n\), quotient in each degree by the ideal generated by the
lower-degree symbols. The degree-one generator \(-t^2X\) is free.
In degree two the lower generator gives relations \(t^2X^2=t^2XY=0\)
and the class of \(X^2-tXY\) has annihilator \((t^2)\). In degree three
one eliminates higher powers of \(X\) by \(X^2=tXY\), and the only
coefficient relation on \(XY^2\) from the lower generators is
\(t^2XY^2=0\). Thus the class of \(tXY^2\) has annihilator \((t)\).
In degree four the additional relation from \(tXY^2\) is
\(tXY^3=0\) after the same elimination. The class of \(XY^3\) has
annihilator \((t)\). In degree five the lower generators all have
a factor \(X\), so \(Y^5\) freely generates its piece. Every higher
piece of \(Q\) vanishes since \(H\) has no higher generators.

By [R-0030](local_filtration_comparison_defect.md), the comparison
\(Q_n\to G_n\) sends each of these initial classes to the filtered class
of its lift. For \(n=1,2,3,4,5\), their images are respectively represented
by \(e_g,e_f,t^2e_f,t^3e_f,t^4e_f\), and each map is an isomorphism
by the computed modules. All three relative torsion pieces therefore
survive in \(G\). The comparison exact sequence gives \(\Delta=0\) and
\(B=S_+H\). Multiplying the five symbols by \(X,Y\) gives the stated
generators for \(B\). For the generator \(X^3\), the identity is
\[
X^3=X(X^2-tXY)+tY(X^2-tXY)+t^2XY^2 .
\]
Conversely \(X(X^2-tXY)=X^3-tY(X^2-tXY)-t^2XY^2\).
The other products of \(X,Y\) with the five symbols are in the
displayed ideal by \(X^2Y^2=Y(X^2Y-tXY^2)+tXY^3\) and its
multiples, together with \(XY^5\in (XY^4)\).

### Specialization of the actual closed equations

Flatness gives the closed algebra the five specialized basis elements.
Its support is the origin, so the two equations form a regular sequence
in \(k[[x,y]]\).
The equation \(y(x^2+y^3)-x(xy)=y^4\) shows
\((X^2,XY,Y^4)\subset H_0^{\rm act}\), and the candidate quotient has
length five. The actual normal graded algebra also has length five
since the normal filtration on the actual closed algebra is finite.
This proves equality. The two actual generator classes in
\(J_0/(x,y)J_0\) have order two, and their linearly independent quadratic
symbols show that no nonzero class is of order at least three. The
closed initial generator module has two copies of \(k\) in degree two
and one in degree four. By R-0030 the degree-four copy is the whole
defect, represented by \(Y^4\). As \((X,Y)H_0^{\rm act}=
(X^3,X^2Y,XY^2,Y^5)\), adjoining \(Y^4\) gives the displayed
\(B_0^{\rm act}\).

The coefficient-specialization image is
\(\overline H=(H+(t)S)/(t)S\subset k[X,Y]\). This image is the image
of \(H/tH\to S/tS\), a map with a kernel. For example, \(t^2X\)
has nonzero class in \(H/tH\) and zero image in \(S/tS\).
The quotient by \(\overline H\) has basis
\(1,Y,Y^2,Y^3,Y^4,X,XY,XY^2\). Hence the relative normal cone
specialized at \(t=0\) has length eight while the actual closed
normal cone has length five. This occurs while the actual algebra
remains finite free and has sole support on the marked curve.
The nonzero defect in this slice therefore cannot certify a nonzero
punctual relative defect.

### The two homogenized cubics

The weighted degrees follow term by term from the specified weights.
On \(z\ne0\), dehomogenization gives the polynomial affine model,
so the support there is the line and its generic length is five.
On \(z=0\), the two equations become \(yq,tq\) for \(q=y^2-tx\).
If \(y=t=0\) then \(q=0\) as well. Thus the reduced support on this
plane is the conic \(D_{\rm con}\), which is smooth in every
characteristic. Indeed, the partial derivatives \(-x,-t,2y\)
cannot vanish simultaneously at a point of \(q=0\) in the plane
over any extension field.

There is no common surface factor. On \(z\ne0\) this follows from
height two in the affine model, and a common factor supported at
infinity would have to be \(z\), which divides neither cubic.
To calculate the conic multiplicity, work on the chart \(t=1\) at
its generic point. The elements \(z,q\), where \(q=y^2-x\) on this
chart, form regular parameters. With \(G=q+zxy\), the quotient by
\(G\) is a DVR with parameter \(z\). In that quotient
\[
F=zx^2+yq=zx(x-y^2)=-zxq=z^2x^2y .
\]
The factor \(x^2y\) is a unit at the generic conic point, so the length
there is two. Purity of the proper complete intersection and
\(5\cdot1+2\cdot2=3\cdot3\) give the full cycle. The
scheme-theoretic closure of the affine intersection itself is obtained
by saturating \((F,G)\) with respect to \(z\). Its reduced support
is \(L\) and its cycle is \(5[L]\), since taking this closure retains
the generic line multiplicity and removes the component on \(z=0\).

## Limitations

The result gives one supported family in which all relative comparison
maps are invertible despite a nonzero defect on the actual closed fiber.
Whether there is a regular-sequence ideal with \(\sqrt J=I\),
\(\Delta_K=0\) and nonzero punctual relative defect remains open here.
This includes the narrower question with finite free rank five and the
specified generic and closed transverse algebras. The example concerns
a marked line and gives no sole-support projective pair for the fixed
quartic \(C_0\).

## Review

The Phase 5 nonauthor reviewer `review_length_five` accepted the finite
free algebra and full equation filtration route over every field, using
the canonical comparison of R-0030. The reviewer reconstructed the free
basis, the generic algebra, all normal ideal powers and the full relative
\(H\) and \(B\). They checked filtered division through order six and the
annihilator and image of each comparison generator. They reconstructed the
actual closed initial ideals and distinguished them from the coefficient
specialization of \(H\). They also checked the conic multiplicity of the
homogenized intersection separately from the closure of the affine scheme.
An exact polynomial replay over the integers checked the lift identities,
the multiplication operators and their relations, the normal monomial images
through degree five, and the local conic identity. The proof gives the full
filtration calculation and the characteristic range.

The [source review](../synthesis/comparison_defect_specialization.md#independent-review)
records independent reconstruction of the finite free actual algebra,
all powers of its normal ideal, the full initial ideal, terminating
filtered division for the equation module, and the comparison in every
degree. It records separate checks of the closed-fiber mismatch and
the doubled residual conic, with integer identities in all characteristics.
The review leaves open the existence of a supported family with nonzero
punctual relative defect.
