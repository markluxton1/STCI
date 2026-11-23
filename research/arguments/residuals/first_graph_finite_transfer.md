# Socle defects and finite transfer on the first graph

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed SC1–SC6 and FT1–FT3, including the actual canonical colon and attachment-corrected finite transfer. Inherited inputs are the established R-0077 equality/second-blowup results, actual marked correspondence and saturated local duality.

The shared setup is the [two-blowup dictionary](blowup_residual_geometry.md#the-two-blowups-and-their-actual-global-section-dictionary), including the [marked correspondence](blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary). This account owns SC1–SC6 and FT1–FT2, including the canonical-ideal and several-marked-point comparison.

## Socle defects on the two presentations of the first graph

**Status:** new synthesis, covered by the scoped correctness review above, using the
existing R-0077 equality and second-blowup results and the actual
[marked correspondence](blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary). The local filtration comparisons are
[CF1–CF4](../normal-geometry/curvilinear_genus_and_defects.md#cartier-cuts-and-finite-modifications-of-the-saturated-filtration).
No existence of the hypothetical pairs is assumed.

### The exceptional-surface residual resultant

Retain sole support on the zero-direction boundary and suppose
the strict intersection \(W\) has generic embedding dimension
one, with length \(c>1\) on the constant section \(T\).
Put \(A=4a-7p,\ B'=4b-7q\) for the two restriction degrees
on \(T\), and write \(L_1=\mathcal O_T(-\ell)\) for its
free first conormal layer. Its top-socle defect has degree
\[
 D:=\deg D_{\rm top}=(c-1)\ell-(A+B'-7).                  \tag{SC1}
\]
This follows from actual CI adjunction on the graph and
\(\deg N_{T/B}=7\); it does not copy the original quartic
constant 14. Since \(A\ge5p,\ B'\ge5q\), one has \(\ell>0\).
The exact sequence
\(0\to \mathcal O_T\to N_{T/B}\to\mathcal O_T(7)\to0\)
is the one computed in R-0077. The free normal line
\(L_1^\vee\) cannot be contained in \(\mathcal O_T\) as it
has positive degree. Consequently the equation of the
exceptional surface \(E\) has generic order exactly one
on \(W\); \(\Theta\), the zero divisor of its free first
symbol, has degree \(7-\ell\).

Thus the actual divisorial gcd of the two restrictions to
\(E\) is exactly \(T\), not a thick copy of \(T\).
Any strict generator of generic normal order one on
\(T\) has a simple horizontal root \(T\) in its
restriction to \(E\): its first derivative in the direction
of \(N_{T/E}\) is generically nonzero, since the generic
surviving normal line is transverse to \(E\).
An order-at-least-two strict generator may have a
repeated root. After dividing by the single common \(T\),
the two binary forms on \(E\) have bidegrees
\((A,p-1),(B',q-1)\), and their common finite scheme is
supported on \(T\). CF2 gives the exact relative resultant
divisor on the base \(T\cong C\):
\[
 \boxed{\operatorname{div}\operatorname{Res}
        =(c-1)\Theta+D_{\rm top}.}                       \tag{SC2}
\]
If one of the remaining binary degrees is zero, the
resultant has its ordinary scalar-power interpretation.
The assertion is the pushforward of the finite
intersection, and does not identify a resultant with the
whole common-root scheme before division. Its degree is
\(A(q-1)+B'(p-1)=7(c-1)-(A+B'-7)\), by \(K=0\).
This is precisely the previous first-graph degree identity,
now localized pointwise. A primitive point can contribute
to the divided resultant only by tangency of \(L_1^\vee\)
to \(E\), and there it contributes \((c-1)\operatorname{mult}
\Theta\), not merely one.

For example, at \((6,8;2,2)\), the two divided forms
have bidegrees \((10,1),(18,1)\), so their resultant is
an actual two-by-two determinant of degree 28. Its
divisor is \(7\Theta+D_{\rm top}\). From the normal
splitting in R-0077, the endpoint directions have
\(N_{T/B}=\mathcal O(2)\oplus\mathcal O(5)\), and the
mixed directions have \(\mathcal O(3)\oplus\mathcal O(4)\).
A line subbundle giving a *surjective* conormal quotient
cannot have degree strictly between the two unequal
summands: the map to the smaller-degree summand is zero,
and a nonzero section of a positive-degree line bundle
into the other has zeros. Combined with SC1 and \(D\ge0\)
this gives exactly the following necessary rows:
\[
\begin{array}{c|c|c|c}
\text{direction}&\ell&\deg\Theta&\deg D_{\rm top}\\ \hline
\text{endpoint}&5&2&14\\
\text{mixed}&3&4&0\\
\text{mixed}&4&3&7
\end{array}
\]
In particular the mixed \(\ell=3\) row is automatically a
globally primitive thickening on the first graph, by the
ordinary-layer Frobenius criterion. In that row the
degree-28 determinant is a seventh power up to scalar
of a degree-four binary form. In the other rows its
remaining factor is exactly the top-socle divisor,
not a freely chosen defect. No row is asserted to occur.

### Primitive graph structures on the full degree-three/four slope edge

For \(a=3p,b=4q\), every hypothetical characteristic-zero
pair has \(p,q\ge2\) by the low-degree carrier exclusion.
If its first strict CI is globally primitive, then (SC1)
gives
\[
 \ell=\frac{5p+9q-7}{2pq-1}.
\]
This strictly decreases in either positive variable
on \(p,q\ge2\), so it is positive and at most three,
with equality three only at \((2,2)\). Integrality
of \(\ell\) leaves an exact finite list:
\[
 \begin{array}{c|l}
 \ell& (p,q)\\\hline
 3&(2,2)\\
 2&\text{none}\\
 1&(5,19),(6,8),(10,4),(21,3)
 \end{array}
\]
For \(\ell=2\) the equation is
\((4p-9)(4q-5)=25\); the factors must be positive
and the first is \(3\bmod4\), whereas all positive
divisors of 25 are \(1\bmod4\).
For \(\ell=1\) it becomes
\((2p-9)(2q-5)=33\); both negative factors could
give at most five with \(p,q\ge2\), so both are
positive. The four positive divisor choices give
the last row. For \(\ell=3\), the normal splitting
allows only the mixed direction because the endpoint
splitting has no line subbundle of degree three.
For \(\ell=1\) both orbit splittings allow the
required line subbundle degree; this is not an
embedded primitive-triple construction.

In particular for every hypothetical \((6,4q)\)
pair on this exact order boundary with \(q>2\),
the first strict intersection cannot be primitive
everywhere, whether or not it is generically
curvilinear. The later marked-line comparison ML9 rules out its mixed direction when \(p\le q\), leaving only \((10,4),(21,3)\) in the mixed orbit. This finite list concerns **global
primitivity on the graph**, unlike the classical
Ellia degree list for primitive structures on
the original curve in \(\mathbf P^3\). The list
is necessary, not a realization list.

### Recovering generic curvilinearity in all orders on a subset of the edge

The second-blowup inequality of R-0077 has
another useful order-only consequence on the
whole zero-direction boundary. Write \(r,s\)
for the strict orders on \(T\), and \(d=2\)
or \(3\) as in that theorem. Then
\(1\le r\le p,\ 1\le s\le q\), and
\[
 A s+B'r-drs\le(7-d)c .
\]
The left side is strictly increasing in both
orders on these ranges, since
\(A\ge5p,\ B'\ge5q\) and \(d\le3\).
If both strict orders are at least two,
necessarily
\[
 2(A+B')-4d\le(7-d)c.                                   \tag{SC6}
\]
This is one criterion for recovery of generic
curvilinearity on the first graph, independent
of the original pair's embedding dimension.

On the edge \((3p,4q)\) with \(p=2\), it fails
for every mixed direction and for every endpoint
direction with \(2\le q<6\).
More sharply the retained R-0077 inequality
at \(r=p\) gives \((5-d)s\le(5-2d)q\), so
in the mixed orbit the strict sextic must
have order one for **every** \(q\ge2\).
Thus the graph generator movement theorem
and LC3 produce a normal general degree-\(4q\)
strict carrier, with actual index \(4q\)
on its moving singularities, across this whole
mixed sextic edge. The lower bound on the number
of simple moving roots is \(9q-10>0\).
In the endpoint orbit for \(q=2\) the strict
sextic also has order one; for \(3\le q<6\)
either strict equation can supply generic
regularity. In the latter case a zero smaller
symbol need not furnish moving singularities.
For \(q\ge6\) the endpoint numerical test
allows both strict orders at least two.
These are precise recovery conditions and
remaining gaps, not all-degree normality of
the original sextic carrier.

### Finite transfer at the marked point on the degree boundary

On the endpoint slope boundary \(a=3p,b=4q\) (either
constant direction orbit), the actual \(V_5\) intersection
\(Z=(P=0)\cap(S=0)\) has sole support the marked quintic
\(\Delta\); its length is \(c=2pq\), by intersection degree
on \(V_5\). On the graph \(W\) has the same length and
support \(T\), since \(\phi|_T:T\to\Delta\) is an
isomorphism. Assume the generic algebra is curvilinear
on either side; the generic algebras agree. The actual
map \(\phi|_W:W\to Z\) is proper and quasi-finite (its
reduced map is an isomorphism), hence finite. It is an
isomorphism off the single marked point \(z\) and injective
on structure sheaves by purity of \(Z\). This is a finite
modification of the *nonreduced CI*, not normalization
of its reduced curve.

Write \(A_Z,A_W\) for the actual curve algebras, and
\(\delta_z=\operatorname{length}((\phi|_W)_*A_W/A_Z)_z\).
The ambient canonical divisor of the blowup of the smooth
conic is \(K_B=\phi^*K_{V_5}+Q'\), and the strict equations
have classes \(\phi^*(pM)\), \(\phi^*(2qM)-qQ'\).
Adjunction gives
\[
 \omega_W=\phi^*\omega_Z\otimes\mathcal O_W((1-q)Q').
\]
Both schemes are projective Gorenstein curves, so
\(\chi(\omega)=-\chi(\mathcal O)\). For a line bundle on
a pure multiplicity-\(c\) curve with smooth support,
twisting changes \(\chi\) by \(c\) times its degree on
the support; this follows directly from the saturated
filtration in the curvilinear case. Finite projection
formula and the punctual cokernel give
\(\chi(\phi^*\omega_Z)=\chi(\omega_Z)+\delta_z\).
Since \(Q'\cdot T=1\), it follows that
\[
 \boxed{\delta_z=\frac{c(q-1)}2=pq(q-1).}                 \tag{SC3}
\]
This does not assume that the strict or image CI is
primitive at \(z\). The difference in Euler characteristics
is supported only there.

The conormal map from the image to the graph is an
elementary modification of length one at that point:
write locally the smooth center as \((x,y)\), the
transverse marked curve as \((t,y)\), and \(y=xv\)
on its blowup chart, as in the marked correspondence.
At the reduced curve its conormal matrix has elementary
divisors \(1,x\). The free first layers map by a
nonzero homomorphism \(L_Z\to L_W\), whose zero
divisor is \(\xi[z]\), \(\xi\in\{0,1\}\). Indeed the
image of the entire ambient conormal in \(L_W\) has
cokernel of length at most one, and it factors through
the surjection onto the free first layer of \(Z\).
The value \(\xi=1\) is precisely when the surviving
normal line on \(W\) at the marked point is the kernel
of the normal differential of \(\phi\) (the contracted
ruling direction). This description makes sense at
nonprimitive points via the saturated line.

By CF4 and SC3 the top defects away from \(z\)
agree, and at \(z\) they satisfy the exact identity
\[
 \boxed{D_{Z,\rm top}(z)
  =D_{W,\rm top}(z)+(c-1)\xi-(q-1).}                     \tag{SC4}
\]
Thus for \(q>1\):
- if the surviving direction is not contracted, the
  graph thickening must supply \(D_{W,\rm top}(z)\ge q-1\);
- if the direction is contracted, the image defect is
  at least \(c-q\);
- if the graph thickening is primitive at the marked
  point, its direction must be contracted and its
  image has defect exactly \(c-q\).

In particular a globally primitive graph thickening
does **not** imply a primitive image quintic thickening.
In the \((6,8;2,2)\) mixed \(\ell=3\) row, it forces
\(\xi=1\), \(\ell_Z=\ell+1=4\), and all image top
defect is \(6[z]\), with all other points primitive.
SC3 computes a length-four finite modification. The
degree and support of the image defect are thus fixed,
rather than only subject to a total genus inequality.
The actual defining equations on \(V_5\) and their
conic normal forms are still needed for realization.

This transfer does not apply in the interior of the
zero-direction slope boundary when the image pair also
contains \(\Gamma\); that pair has another component
and the finite same-support modification premise fails.
More generally the CF3–CF4 comparison works on any
finite generically isomorphic pair of pure curvilinear
thickenings, and the SC3 proof applies to analogous
transverse-center blowups where the sole-support image
and strict CIs have the same generic length and a
single marked modification point. One must check the
actual support, relative canonical correction, and
degree of the conormal modification; these are not
automatic at the next blowup.

### Signed finite transfer throughout the interior equality boundary

**New extension of SC3--SC4, covered by the scoped correctness review above.**
The caveat at the end of the preceding section is genuine
for the entire image CI but can now be resolved by retaining
its full primary component. Use the marked correspondence
on the whole zero-direction boundary, with strict intersection
\(W\) supported on \(T\), image quintic \(\Delta\) and
marked conic \(\Gamma\). Put
\[
 u=a-3p,\quad v=b-3q,\qquad c=ab/4-pq .
\]
The actual image CI \(Y\) is defined by divisors of degrees
\(a-2p,b-2q\) in \(M\), with exact orders \(u,v\) along
\(\Gamma\). Its cycle is
\[
 [Y]=c[\Delta]+uv[\Gamma].
\]
Indeed off \(\Gamma\) this follows from the actual strict
intersection and the graph isomorphism. At the generic point
of \(\Gamma\) the two initial forms of degrees \(u,v\) have
no common root by the ruling test; hence their local
intersection multiplicity is \(uv\) (zero if one has
order zero). No other curve can occur, and purity prevents
isolated extra components.

Write \(Z\) for the full primary component of \(Y\) on
\(\Delta\) and \(R\) for its linked residual on
\(\Gamma\) (empty if \(uv=0\)). The finite map
\(f:W\to Y\) has scheme image \(Z\): it is proper
quasi-finite because its reduced map is an isomorphism
onto \(\Delta\); its image is pure by injection into
\(f_*\mathcal O_W\) and agrees with the generic primary
scheme of \(Y\). Thus \(W\to Z\) is finite, generically
an isomorphism, and an isomorphism away from \(z\).
In particular this is a finite map even though the
whole image CI has another component.

Set
\[
 \delta=\operatorname{length}((f_*\mathcal O_W)/\mathcal O_Z)_z,
 \qquad h=\operatorname{length}(Z\cap R),
 \qquad H_0=\Delta\cap R
\]
where \(H_0\) in the last expression is the *reduced
marked support's scheme-theoretic attachment divisor*
on \(\Delta\), not the reduction of the finite intersection.
All these finite modules are supported at \(z\).
Actual adjunction on the smooth ambient conic blowup gives
\[
 \omega_W=f^*(\omega_Y|_Z)
                 \otimes\mathcal O_W((1-u-v)Q').
\]
On the possibly non-Gorenstein \(Z\), ordinary linkage
gives
\[
 \omega_Z=I_{Z\cap R/Z}\otimes\omega_Y|_Z .
\]
Taking Euler characteristics and using Serre duality for
both CM curves yields
\[
 \chi(\omega_Y|_Z)=-\chi(\mathcal O_Z)+h,\qquad
 \chi(\omega_W)=-\chi(\mathcal O_Z)+h+\delta+
                                 c(1-u-v).
\]
On the other hand \(\chi(\omega_W)=-\chi(\mathcal O_Z)-\delta\).
Here the twist degree contributes \(c(1-u-v)\) since
\(Q'\cdot T=1\), by the Hilbert polynomial of a pure curve
(or the saturated flag when curvilinear). Thus
\[
 \boxed{2\delta+h=c(u+v-1).}                             \tag{FT1}
\]
This formula does not assume generic curvilinearity.
It is a comparison of actual finite structure sheaf
quotient and actual thick attachment lengths. In
particular \(h\le c(u+v-1)\); one cannot keep the
edge value of \(\delta\) unchanged when \(R\ne\varnothing\).
When \(uv=0\), \(h=0\), recovering SC3 on the outer edge.

Now assume the shared generic algebra of \(Z,W\) is
curvilinear. Retain the first conormal modification
\(\Xi=\xi[z]\), \(\xi\in\{0,1\}\), of SC4, since
the same ambient conormal inclusion supplies it.
Apply the [full-primary duality LA1--LA4](layerwise_attachment_and_triples.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component)
to \(Z\) with actual attachment to \(R\). For \(W\)
the full Gorenstein identity applies. The general
finite-lattice comparison CF3 gives
\[
 2\delta=c(c-1)\xi+cD_{W,\rm top}(z)
     -c(D_{Z,\rm top}(z)-H_0(z))-h .
\]
With FT1 this becomes
\[
 \boxed{D_{Z,\rm top}-H_0
 =D_{W,\rm top}+\big((c-1)\xi-(u+v-1)\big)[z].}          \tag{FT2}
\]
Away from \(z\) the two structures and their defects agree.
This is exactly the signed socle transfer: on the interior
it is incorrect to use \(D_{Z,\rm top}\) in place of
\(D_{Z,\rm top}-H_0\).
If the graph is primitive at the mark and \(\xi=0\),
FT2 forces \(H_0(z)\ge u+v-1\) on the image.
If it is primitive there and \(\xi=1\), the signed image
defect at the mark is \(c-u-v\).
The finite index, the first-line modification and all
individual layer defects are also coupled by CF3.
For any actual image generator of nonzero first symbol
the relation-line argument SM3 continues to apply,
now subtracting \(u\) or \(v\) respectively, since
the image and strict generic algebras along the marked
quintic agree.

This extends the geometric transfer to the genuine
interior two-component image problem, without assuming
the image primary is Gorenstein or the residual conic
primitive. The full attachment module there is also
the first local cohomology annihilator dual by LC-A1.
The image has Picard rank one in the surrounding
threefold but has a *two-component* actual intersection;
the singleton mate-compression conclusion must not
be substituted for its actual multiplicity relation.
No new realization on the interior is asserted.

### Local canonical-ideal version and several marked points

There is a local proof of FT1 which gives more than the
Euler characteristic argument. In any such transverse
blowup chart write the center as \((x,y)\), the marked
curve as \((t,y)\), and \(y=xv_0\). On the graph the
strict equations are \(P'=x^{-u}P,\ S'=x^{-v}S\),
where the exponent \(v\) is distinct from the chart
coordinate \(v_0\). Assume the same actual full-primary
finite map near the point and set
\(A=\widehat{\mathcal O}_{Z,z}\), \(B=(f_*\mathcal O_W)_z^\wedge\),
\(K=I_{Z\cap R/Z,z}^\wedge\), \(e=u+v-1\).
These are finite free lattices over \(k[[x]]\), except for the
finite quotients; in particular \(x\) is regular on both
primary curve algebras. The actual canonical generator
\(\eta_Y\) of the ambient CI \(Y\) is the determinant
adjunction frame given by \(dx\wedge dt\wedge dy\) and
the ordered regular equations \(P,S\).
Over \(x\ne0\), the analogous graph frame satisfies
\[
 \eta_Y=x^{1-u-v}\eta_W .
\]
This identity is the determinant of the ambient coordinate
change \(y=xv_0\) and of the two equation scalings, not
a trace determinant of a nonreduced field algebra.
It uses the canonical Koszul adjunction isomorphism on the
open where the blowup is an isomorphism.
By finite duality, first for \(Z\subset Y\) and then
for \(W\to Z\), the canonical modules are identified
in the common generic algebra, with the frame \(\eta_Y\),
as
\[
 \omega_Z=K\eta_Y,\qquad
 f_*\omega_W=\operatorname{Hom}_A(B,K)\eta_Y .
\]
Evaluation at 1 identifies the latter Hom with
\(\{a\in K:aB\subset K\}\) because the generic
algebras agree and the lattices are pure.
The adjunction frame computation identifies its
image with \(x^e B\). Thus, up to the harmless
unit of the chosen coordinate and regular-sequence
frames, one has the **actual canonical ideal identity**
and the chain of full lattices
\[
 \boxed{(K:B)=x^eB\subset K\subset A\subset B.}           \tag{FT3}
\]
These identifications follow from finite duality and
regular-immersion adjunction (e.g. [Stacks, Duality for
schemes §19](https://stacks.math.columbia.edu/tag/0AU3));
they do not assume the image primary Gorenstein.
In particular, if \(K=A\), FT3 identifies the actual
conductor ideal of the finite algebras, not merely a
length.

To compute lengths take the DVR dual of
\(0\to A\to B\to B/A\to0\).
The canonical module \(K\) is the DVR dual of \(A\)
after local trivialization; the dual of \(B\)
is \((K:B)\). The cokernel has length \(\delta\)
by \(\operatorname{Ext}^1_{k[[x]]}(B/A,k[[x]])\),
and \(A/K\) has length \(h\).
Since \(B\) is free of rank \(c\), the chain FT3
gives \(ce=\delta+h+\delta\).
This proves FT1 *pointwise* without a global genus
calculation. In the generically curvilinear case
FT2 follows pointwise exactly as above.
For several transverse intersections of the
marked curve with a smooth center, the same
proof works separately in the actual charts
provided each has this finite primary map and
the strict intersection has no residual curve
there. If the normal algebra changes generically,
or the image of the proper strict intersection
is not the full pure primary component, these
comparisons have not been established.

The global Euler characteristic derivation above
is retained as a short independent consistency
check. The local ideal description additionally
gives an exact target for the conductor approach:
one must identify the actual canonical ideal
\(K\), not substitute the reduced conductor or
a numerical surface class. This strengthening
was covered by the scoped correctness review above.


