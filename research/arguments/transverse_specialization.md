---
id: STCI-A-0006
type: argument
title: Transverse specialization of normal cones and the filtered equation comparison
status: complete
scope: "#scope"
conclusion: "#conclusion"
---
# Transverse specialization along a marked curve

## Scope

The normal cone of a marked inclusion is intrinsic to the inclusion.
An actual transverse slice uses a chosen lift \(t\) of a uniformizer
of the marked curve. The specialization maps below use the resulting
\(B\)-algebra structure. They are natural for maps of \(B\)-algebras
taking each filtered ideal into the corresponding filtered ideal. In
the [marked embedding diagram](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#2-retain-the-entire-embedding-and-its-maps),
each map uses its own actual ambient quotient and induced ideal-power
filtration. The carrier ideals and labelled source lines remain part
of that data.

The general Tor calculation in [R-0062](../results/normal_cone_slice_specialization.md)
needs a Noetherian algebra over a DVR. The equation comparison in
[R-0063](../results/normal_flat_comparison_specialization.md) uses
[R-0030](../results/local_filtration_comparison_defect.md) in formal
coordinates along a smooth curve in a smooth threefold, with an actual
two-equation regular sequence. Residual components are allowed in the
initial hypotheses. The proofs work in arbitrary characteristic in
the displayed settings. The single-degree control taken from the
punctual family uses characteristic zero.

## Normal-cone specialization

Let \(B\) be a DVR with uniformizer \(t\), residue field \(k\), \(M\)
a Noetherian \(B\)-algebra, and \(K\subset M\) an ideal. Put
\[
N_n=M/K^n,\qquad A_n=K^n/K^{n+1},\qquad
U_n=\operatorname{Tor}_1^B(N_n,k),\qquad A=\operatorname{gr}_K M.
\]
Bars on the algebras or ideals denote reduction or image modulo \(t\),
respectively. Tensor
\[
0\longrightarrow A_n\longrightarrow N_{n+1}\longrightarrow N_n
\longrightarrow 0
\]
over \(B\) with \(k\). The image of \(A_n\otimes_B k\) in
\(N_{n+1}\otimes_B k=M/(K^{n+1}+tM)\) is
\[
(K^n+tM)/(K^{n+1}+tM)=\bar K^n/\bar K^{n+1}.
\]
This identifies the end of the Tor sequence as
\[
U_{n+1}\longrightarrow U_n\longrightarrow
A_n\otimes_B k\xrightarrow{\gamma_n}
\operatorname{gr}_{\bar K}^n\bar M\longrightarrow0.
\]
The map \(\gamma=\bigoplus_n\gamma_n\) sends the class of a product
to the product of the reduced classes. It gives a closed immersion of
the actual slice cone into the special fiber of the relative normal cone.
Under injectivity of \(t\) on \(M\), the kernel in degree \(n\) is given
directly by
\[
E_n=\frac{(K^n\cap tM)+K^{n+1}}{tK^n+K^{n+1}}.
\]

The free resolution of \(k\) with differential \(t\) gives
\(U_n=(K^n:_M t)/K^n\). With the corresponding connecting map, a class
represented by \(m\) with \(tm\in K^n\) maps to the class of \(tm\) in
\(A_n\otimes_B k\). Thus \(E_n=\operatorname{coker}(U_{n+1}\to U_n)\)
canonically. For \(a\in K^d\), multiplication on representatives sends
\(m\) to \(am\) and \(tm\) to \(t(am)\). Changing \(m\) by \(K^n\)
changes \(am\) by \(K^{n+d}\). An element coming from \(U_{n+1}\)
maps into the image of \(U_{n+d+1}\), since \(t(am)\) then lies in
\(K^{n+d+1}\). Changing \(a\) by \(K^{d+1}\) also puts \(am\) in that
image, and changing \(a\) by \(tK^d\) has zero effect since \(tm\in K^n\).
This describes the \(A\otimes_B k\)-action on the cokernels and shows
compatibility with the ideal inclusion into \(A\otimes_B k\).
Compatible algebra maps respect these sequences and products.

### From all-degree agreement to normal flatness

Suppose \(t\) acts injectively on \(M\) and \(M/K=B\). Over a DVR,
flatness is equivalent to torsion freeness. Thus flatness of the
\(N_n\) is equivalent to \(t\)-saturation of all the \(K^n\).
If the \(N_n\) are flat, each \(A_n\subset N_{n+1}\) is torsion free.
Conversely, the extensions with successive kernels \(A_n\) prove
flatness of the \(N_n\) from that of the \(A_n\), starting with \(N_1=B\).
The Tor sequence gives every \(\gamma_n\) invertible if all \(N_n\)
are flat.

If all \(\gamma_n\) are invertible, the Tor transitions
\(U_{n+1}\to U_n\) are surjective. Artin–Rees for \(tM\subset M\)
and the ideal \(K\) gives an integer \(c\ge1\) such that
\(tM\cap K^{n+c}\subset tK^n\) for every \(n\ge0\).
A representative \(m\) of a class in \(U_{n+c}\) has \(tm\in K^{n+c}\),
so \(tm\in tK^n\). Injectivity of \(t\) makes \(m\in K^n\).
The map \(U_{n+c}\to U_n\) is therefore zero and also surjective as a
composite of the adjacent transitions. Hence every \(U_n\) vanishes.
This establishes the four-way equivalence without a completeness assumption.
The normal-flatness condition here is the ordinary flatness of
\(\operatorname{Spec}(\operatorname{gr}_K M)\) over \(B\). The Tor cokernel
measures whether a torsion class in one neighborhood lifts to the next.

### A single degree can agree in the presence of torsion

When \(M/K=B\), one has \(U_1=0\), so \(\gamma_1\) is an isomorphism.
The relative piece \(A_1\) can still have torsion.

For the \(m=2\) case of the
[characteristic-zero punctual family](punctual_comparison_defects.md#actual-closed-algebra-and-specialization),
take \(B=k[[t]]\), \(I=(x,y)\subset R=B[[x,y]]\), \(a=t^r\) with \(r\ge1\),
and \(J=(ax+x^2+y^2,ay+xy+y^2+x^3)\). The closed slice ideal is
primary to \((x,y)\). In fact its first symbols \(X^2+Y^2\) and
\(Y(X+Y)\) are coprime in characteristic zero, so the associated
graded quotient is a quotient of the length-four homogeneous algebra
cut out by the two quadrics. To see the length of the actual quotient,
if lowest terms cancel in an expression in the two equations, the
homogeneous syzygy of the two relatively prime symbols is a multiple of
their Koszul syzygy. Subtracting the corresponding actual syzygy raises
the canceled weighted order and gives the full initial ideal in these
two symbols. This verifies length four. The two equations together
with \(t\) are a system of parameters in the regular local ring \(R\),
so they form a regular sequence. The actual algebra is finite over
\(B\) by completeness and the finite slice, and it is free since \(t\)
is regular on it. Explicitly, lifts of a finite \(k\)-basis of the
slice span after repeated reduction modulo \(t\) in the complete ring.
Along the generic marked component the independent linear symbols give
length one, so the length-four actual family has a residual generic
contribution of rank three. This is a conclusion from the actual family.

The relative degree-one symbols are precisely the \(B\)-span of \(aX,aY\).
Thus \(A_1=(B/(t^r))X\oplus (B/(t^r))Y\). The slice has no linear
relations, so \(\gamma_1:kX\oplus kY\to kX\oplus kY\) is an isomorphism
despite the torsion in \(A_1\).

### Regularity of the parameter is essential

In \(R=k[[t,x,y]]\) take \(I=(x,y)\), \(f=x\), \(g=ty+x^2\), so
\(J=(x,ty)\). The carrier polynomials are distinct and integral in
\(k[t,x,y]\). The second is primitive and linear in \(t\), with
coprime coefficients \(y,x^2\). The pair is a regular sequence since
\(ty\) is nonzero in the domain \(R/(x)\). In the frames from \(f,g\)
and \(X,Y\), the conormal matrix is \(\operatorname{diag}(1,t)\).
Here \(M=B[[y]]/(ty)\) and \(A=B[X,Y]/(X,tY)\).
The ideals \(J=(x,ty)\) and \(IJ=(x^2,xy,ty^2)\) are generated by
normal-homogeneous elements, so their full initial ideals are
\[
H=(X,tY),\qquad T=(X^2,XY,tY^2)=S_+H .
\]
Thus the comparison defect is zero. Both specialized normal algebras are
\(k[Y]\), whereas every positive piece of \(A\) is \(B/(t)\).
The class of \(y\) is nonzero in \(M\) and killed by \(t\).
The additional support \(V(x,t)\) is allowed in this test.

## Comparison under normal flatness

Now let \(B=k[[t]]\), \(R=B[[x,y]]\), \(I=(x,y)\), and \(J=(f,g)\subset I\)
a regular-sequence ideal. Put \(M=R/J\), \(K=IM\), \(S=B[X,Y]\),
\(H=\operatorname{in}_I J\) and \(T=\operatorname{in}_I(IJ)\). The two
normal algebras used below are
\[
A=S/H=\operatorname{gr}_I(R/J),\qquad
A'=S/T=\operatorname{gr}_I(R/IJ).
\]
Write \(D=J/IJ\), \(F^nD=((J\cap I^n)+IJ)/IJ\), and \(G=\operatorname{gr}_F D\).
By R-0030 there is an exact comparison
\[
0\longrightarrow \Delta=T/S_+H\longrightarrow Q=H/S_+H
\longrightarrow G=H/T\longrightarrow0 .
\]

### The two-cone criterion

The Koszul presentation of \(J\) has its relation in \(IR^2\), giving
\(D=B^2\) in the two generator frames. If \(M\) is \(B\)-flat, so is
\(R/IJ\) by the extension with kernel \(D\) and quotient \(M\).
The \(I\)-adic filtration on \(R/IJ\) induces \(F^nD\), since
\[
D\cap (I^n+IJ)/IJ=((J\cap I^n)+IJ)/IJ.
\]
The quotient map from \(R/IJ\) to \(M\) maps \(I^n(R/IJ)\) onto \(K^n\).
To check exactness on the associated gradeds, if an element in
\(I^n(R/IJ)\) maps to \(K^{n+1}\), subtract a lift from \(I^{n+1}(R/IJ)\)
to get an element of \(F^nD\). The kernel of the induced map from
\(F^nD\) into the degree-\(n\) associated graded is \(F^{n+1}D\).
Consequently
\[
0\longrightarrow G_n\longrightarrow A'_n\longrightarrow A_n
\longrightarrow0 .
\]
Thus flatness of \(A,G\) is equivalent to flatness of \(A,A'\), degree
by degree. In one direction use extension closure of flatness, and in
the other use that a submodule of a torsion-free module is torsion free.

Regularity of \(t\) on \(M\) gives \(J\cap tR=tJ\), and so
\(D\otimes_B k=\bar J/(\bar I\bar J)\). The sequence \(f,g,t\) is
regular in the regular local ring \(R\). Permuting it proves that
\(\bar f,\bar g\) is a regular sequence in \(R/tR\).
Both quotients have degree-zero normal algebra \(B\). R-0062 therefore
identifies \(A\otimes_B k\) and \(A'\otimes_B k\) with the actual
associated gradeds of \(R/(J,t)\) and \(R/(IJ,t)\) under the assumed
degreewise flatness. The image of \(IJ\) modulo \(t\) is \(\bar I\bar J\).
Tensoring the sequences \(0\to H_n\to S_n\to A_n\to0\) and
\(0\to T_n\to S_n\to A'_n\to0\) preserves injectivity since their
quotients are flat. Thus \(H\otimes_B k\) and \(T\otimes_B k\) are
the full actual slice initial ideals inside \(k[X,Y]\).

Right exactness applied to \(Q=H/S_+H\), \(G=H/T\) and \(\Delta=T/S_+H\)
now gives the three identifications on the slice. Indeed the
multiplication maps defining \(S_+H\) reduce to multiplication by
\((X,Y)\) on the actual slice initial ideal, with the same image in both
reduced numerators. Since \(G\) is flat, tensoring the relative comparison
sequence gives
\[
0\longrightarrow\Delta\otimes_B k\longrightarrow Q\otimes_B k
\longrightarrow G\otimes_B k\longrightarrow 0 .
\]
The cokernel identifications give an isomorphism of this exact sequence
with the comparison of R-0030 for the actual slice.

The specialization maps also exist without the flatness hypotheses.
A degree-\(n\) symbol of an equation in \(J\cap I^n\) reduces to the
degree-\(n\) symbol of the sliced equation, or zero if its order
increases. This gives \(H\otimes_B k\to H_{\rm slice}\).
The same construction for \(IJ\) gives \(T\otimes_B k\to T_{\rm slice}\)
because the image of the ordinary product is \(\bar I\bar J\).
These maps carry the reduced positive-degree products into
\(\bar S_+ H_{\rm slice}\), so they induce the maps on \(Q,G,\Delta\)
by their respective cokernel descriptions.

The image \(\widetilde H\) of \(H\otimes_B k\) in \(k[X,Y]\) satisfies
\(A\otimes_B k=k[X,Y]/\widetilde H\) by right exactness. The Tor
group of \(A\) can give a kernel in \(H\otimes_B k\to k[X,Y]\).
The slice kernel \(E\) for \(R/J\) is the quotient of the full actual
slice initial ideal by \(\widetilde H\). These are distinct tests.
The same statements apply to \(T\) and \(A'\) for \(R/IJ\).

### The two lowest initial-equation degrees

Let \((V,\mathfrak m,L)\) be an equicharacteristic regular local ring
of dimension two, and \(J_0\subset\mathfrak m\) a two-generator
regular-sequence ideal. Let \(H_0=\operatorname{in}_{\mathfrak m}J_0\)
in \(L[X,Y]\). The two filtration weights \(a\le b\) of
\(D_0=J_0/\mathfrak m J_0\) are the two lowest degrees, counted with
multiplicity, in a minimal homogeneous generating set of \(H_0\).
The quotient Hilbert function of \(L[X,Y]/H_0\) determines both weights.

Indeed \(J_0\) is \(\mathfrak m\)-primary, so the filtration of \(D_0\)
terminates since \(\mathfrak m^{N+1}\subset\mathfrak m J_0\) for some
\(N\). Take a basis adapted to its two weights and lift the classes to
equations \(u,v\) of orders \(a,b\). A representative of a class of
weight \(a\) that lies in \(\mathfrak m^a\) has order exactly \(a\), and
likewise for \(b\). Nakayama makes the lifts generators. If \(a=b\), the
degree-\(a\) symbols are independent. A scalar leading relation would
raise the order of a representative of a nonzero class beyond \(a\).
Since all elements have order at least \(a\) and the generators span the
degree-\(a\) symbols, this gives exactly two minimal generators there.

If \(a<b\), every expression \(cu+dv\) of order \(n<b\) has initial
symbol a multiple of the initial symbol of \(u\), since the second
summand has order at least \(b\). At degree \(b\), the initial symbol of
\(v\) is independent modulo multiples of the first symbol. If it were
a multiple by a homogeneous polynomial of degree \(b-a>0\), lift that
multiplier in \(\mathfrak m^{b-a}\) and subtract its product with \(u\)
from \(v\). This would increase the order of the same class in
\(D_0\) beyond \(b\). In degree \(b\), every initial symbol is in the
span of the multiples of the first symbol and scalar multiples of the
second. Indeed an expression of order \(b\) cannot have \(cu\) of
order below \(b\), since \(dv\) cannot cancel it there. Hence the
first two minimal-generator degrees are \(a,b\), and every additional
minimal equation has degree above \(b\).

Recover \(a\) as the first degree where \(H_{0,a}\) is nonzero.
If \(\dim_L H_{0,a}=2\), then \(b=a\). Otherwise, multiplication by
the single degree-\(a\) symbol is injective in \(L[X,Y]\).
Then \(b\) is the first degree \(n\ge a\) where
\(\dim_L H_{0,n}>n-a+1\). The dimensions \(\dim_L H_{0,n}\) are the
differences of \(n+1\) and the quotient Hilbert function.

### Ordinary normal flatness implies equation-module flatness

Assume \(A\) is flat in every degree. The \(K\)-adic filtration on \(M\)
is separated by Krull intersection. If a nonzero element of \(M\) were
killed by \(t\), its nonzero initial class in some \(A_n\) would be
killed by \(t\). Thus \(M\) is \(B\)-flat. R-0062 now gives flatness of
each \(M/K^n\) and compatibility of \(A\) with the actual slice.

Reduction of the filtered ideal \(J\) is strict. To see this, lift an
element of \(\bar J\cap\bar I^n\) to \(h\in J\). Write \(h=i+tr\)
with \(i\in I^n\). The class of \(r\) in \(M\) lies in \(K^n\), since
\(t[r]\) does and \(M/K^n\) is flat. Write \(r=i'+j'\) with
\(i'\in I^n\) and \(j'\in J\). The element \(h-tj'\) lies in
\(J\cap I^n\) and gives the desired reduction. Together with
\(D\otimes_B k=\bar J/(\bar I\bar J)\) this proves
\[
\operatorname{im}(F^nD\longrightarrow D\otimes_B k)=F^n\bar D .
\]

Let \(L=\operatorname{Frac}(B)\). At the generic point of the marked
curve use \(R_I\) and then its \(IR_I\)-adic completion. Indeed
\[
R_I/I^n R_I=(R/I^n)\otimes_B L
   \simeq L[x,y]/(x,y)^n
\]
for \(n\ge1\). After tensoring, each element of \(R\setminus I\) has
invertible constant term and nilpotent higher terms in these quotients,
which explains the localization identity. Passing to the inverse
limit identifies the completion with \(L[[x,y]]\). The rank of
\(F^nD\) is the dimension of its generic transverse filtration stage.
Localization is exact and so commutes with intersections, and the
faithfully flat completion preserves the intersections and the
equation-module quotient killed by \(I\). It also preserves the regular
sequence \(f,g\). The transverse ideal is primary to the maximal ideal,
since the ambient ring there is regular of dimension two and the ideal
has height two. The closed slice is likewise an actual two-generator
complete intersection by regularity of \(t\) on \(M\).

Each \(A_n\) is finite free over \(B\), as a flat quotient of the finite
\(B\)-module \(S_n\). Its rank is the generic transverse Hilbert
function in degree \(n\), by the finite jets just described. Its
reduction is the actual sliced graded piece by R-0062. Thus the generic
and sliced Hilbert functions agree. The two-lowest-degrees lemma
identifies the two equation-module weights in each fiber, and therefore
\[
\operatorname{rank}_B F^nD=\dim_k F^n\bar D
\]
for every \(n\). In \(D=B^2\), the submodule \(F^nD\) is finite free.
Its image modulo \(t\) has dimension equal to its rank by strict
reduction and this equality. In Smith normal form every invariant
factor for \(F^nD\subset D\) must be a unit, since a nonunit factor
would lower the image dimension. Thus \(D/F^nD\) is torsion free for
every \(n\). Each \(F^nD/F^{n+1}D\) is a submodule of the torsion-free
module \(D/F^{n+1}D\), so \(G_n\) is flat. The two-cone criterion
now gives all the asserted identifications.

### Local support under normal flatness

The generic transverse algebra is Artinian by the height-two
regular sequence in the two-dimensional ambient ring. Its normal
graded pieces vanish in large degrees. Finite flatness over \(B\)
makes the relative \(A_n\) vanish in those degrees, since they have
rank zero there. Thus \(K^N=K^{N+1}\) for some \(N\). The ideal
\(K\) lies in the maximal ideal of \(M\), and Nakayama gives \(K^N=0\).
Together with \(M/K=B\) this proves that the local reduced support is
the marked curve. Where another component meets the curve the general
Tor sequence still applies, while the normal-flat criterion cannot hold.

### The supported length-four control

Take \(J=(f,g)\) with \(f=x^2\), \(g=y^2+tx\). The ideal can equally
be presented by the integral polynomial carriers \(g,f+g\), since
both are primitive and linear in \(t\) with coprime coefficients.
They are singular at the origin and their first conormal symbols along
the generic marked curve agree and have rank one. Modulo \(J\), the
algebra is free on \(1,x,y,xy\) by the two monic relations
\(x^2=0,\ y^2=-tx\). For example, form the polynomial quotient by
first adjoining \(x\) with the monic relation and then adjoining \(y\)
with its monic relation. Both \(x,y\) are nilpotent, so completion in
\((x,y)\) gives the same algebra. The quotient has sole reduced support
\(I\), whence \(J\) is a height-two complete intersection.
Its ideal powers as \(B\)-modules are
\[
K=B x+B y+B xy,\quad K^2=B(tx)+B(xy),\quad
K^3=B(txy),\quad K^4=0 .
\]
In particular the full initial ideal is
\[
H=(tX,X^2,XY^2,Y^4).
\]
Indeed the four displayed generators vanish in the associated graded.
The quotient by them has degree pieces \(B\) in degree zero,
\(B Y\oplus (B/(t))X\) in degree one,
\(B Y^2\oplus (B/(t))XY\) in degree two, and \(B Y^3\) in degree
three, and vanishes above. In degree two \(Y^2\) maps to \(-tx\)
modulo \(K^3\), and in degree three \(Y^3\) maps to \(-txy\).
The power calculation proves each piece maps isomorphically.

In \(Q=H/S_+H\) the successive generators \(tX,X^2,XY^2,Y^4\)
have coefficient modules \(B,B/(t),B/(t),B\), respectively.
Indeed each homogeneous lower-generator multiple is a monomial with
coefficient either a unit or a multiple of \(t\). For \(X^2,XY^2\)
the lower generators give exactly their \(t\)-multiples and for \(Y^4\)
the lower generators have a factor \(X\). The indicated symbols lift
to
\[
g,\quad f,\quad xg-tf=xy^2,\quad (y^2-tx)g+t^2 f=y^4.
\]
Their images in \(D\) are \(e_g,e_f,-t e_f,t^2e_f\). To obtain
\(F^nD\), cancel the initial symbol of an element of \(J\cap I^n\)
using these lifts, and repeat in increasing degree. Positive-degree
multipliers vanish in \(D\), and constant multipliers only occur
on lifts of order at least \(n\). The procedure for \(D\) stops at
order five since \(I^4\subset J\) and \(I^5\subset IJ\). Hence
\[
F^1D=D,\quad F^2D=B e_f,\quad F^3D=tB e_f,\quad
F^4D=t^2B e_f,\quad F^5D=0 .
\]
The four displayed lifts induce an isomorphism \(Q_n\to G_n\) in
every degree. This gives \(\Delta=0\) despite the torsion in \(Q_2,Q_3\).

The sliced pair is \((x^2,y^2)\), whose comparison has zero defect
since its normal-homogeneous generators give
\(H_{\rm slice}=(X^2,Y^2)\) and \(T_{\rm slice}=(X,Y)H_{\rm slice}\).
However, the specialization of the relative cone is
\[
k[X,Y]/(X^2,XY^2,Y^4)\longrightarrow k[X,Y]/(X^2,Y^2).
\]
Its kernel is generated by \(Y^2\) and has basis \(Y^2,Y^3\) in
degrees two and three. Thus even a finite flat, supported intersection
can have agreement of the defects and failure of normal-cone
specialization. The relative module \(H\otimes_B k\) also has a
nonzero class represented by \(tX\) in its kernel in \(k[X,Y]\).

## Conclusion

The Tor cokernel for each actual ambient quotient detects whether
normal-cone formation loses information on a specified slice.
For the equation comparison both \(R/J\) and \(R/IJ\) enter.
In the formal two-equation complete intersection, ordinary normal
flatness already controls the second cone because the transverse
Hilbert function fixes the two weights in the actual equation module.
The proof imposes no restrictions on the characteristic of the field.

When \(G\) is flat the torsion in \(Q\) equals the torsion in \(\Delta\)
by the exact comparison. Existence of punctual torsion on the
normal-flat locus is unresolved here. Away from that locus the two
Tor kernel profiles provide separate measurements for \(R/J\) and
\(R/IJ\). The [supported length-five control](../results/supported_length_five_defect_specialization.md)
shows that a nonzero slice defect can coexist with zero relative
defect. The
[sole-support question](../FRONTIER.md#punctual-relative-defect-under-sole-support)
concerns the relative defect. The cone and equation defect retain specific filtered
information about the actual embedding. Reconstruction of the full
embedded scheme or a global homogeneous pair for \(C_0\) requires
additional data.

## Source review

The October 24 [transverse specialization account](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-transverse-specialization-and-normal-flatness)
records an independent reconstruction of its local proofs. It uses the
earlier reviewed filtered-equation comparison and two examples from the
normal-Koszul continuation. Its [evidence scope](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#evidence-scope-and-the-remaining-geometric-bridge)
records the basis check for the supported quadruple and distinguishes
sampled Rees computations from exact family proofs. The reconstructed
routes here have their own review passages in R-0062 and R-0063.
