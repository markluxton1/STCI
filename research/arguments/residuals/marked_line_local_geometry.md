# Marked-line geometry and primitive finite modifications

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed ML1–ML9 and MJ1–MJ4, including marked-line interpolation, the full finite-modification lattice and higher-jet constraints. Inherited inputs are the actual R-0077 marked correspondence and established first-graph model.

Use the [two-blowup dictionary](blowup_residual_geometry.md#the-two-blowups-and-their-actual-global-section-dictionary) and [marked correspondence](blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary) for the global setup. The symbols SC1–SC6 and FT1–FT2 refer to [socle defects and finite transfer](first_graph_finite_transfer.md#socle-defects-on-the-two-presentations-of-the-first-graph). This account keeps the coupled marked-line, primitive finite-lattice, and higher-jet proofs together.

### The marked line excludes primitivity at the mixed sextic boundary

**New necessary theorem, covered by the scoped correctness review above.** On the
characteristic-zero edge \((a,b;p,q)=(6,4q;2,q)\), \(q\ge2\),
every hypothetical sole-support pair in the mixed direction
has a **nonprimitive first strict intersection at the marked
point** \(z\). In particular the globally primitive mixed
\((6,8)\) row of SC1 is impossible, independently of the local
singularity type or normality of either image carrier. For an
endpoint direction and the same degree edge, primitivity at
the marked point instead forces exact higher contact with a
particular line; see below. The statement uses the actual
marked correspondence of R-0077.

#### Marked coordinates and a geometric source constraint

Write \(X=y_0/y_4,\ Y=y_1/y_4,\ Z=y_5/y_4\) on
the chart \(y_4\ne0\) of \(V_5\). The cubic map gives the
following regular coordinate chart:
\[
 y_4=1,\qquad y_2=XZ+Y^2,\quad
 y_3=YZ+X^2Z+XY^2,\quad y_6=Z^2-XYZ-Y^3.                 \tag{ML1}
\]
For verification use \(x_0=1,\ x_1=a_0,\ x_2=b_0\),
write \(q_0=x_3-a_0b_0,\ c_4=b_0-a_0^3\), and set
\(X=q_0/c_4,\ Y=a_0X,\ Z=b_0-a_0^2X\).
Substitution gives the displayed identities on the dense
open of the cubic image. Conversely the polynomial graph
in this chart is the closure of the parametrized image,
since when \(X\ne0\) one recovers \(a_0=Y/X\),
\(b_0=Z+Y^2/X\), \(q_0=X(b_0-a_0^3)\).
Hence ML1 is a chart of the actual smooth threefold,
not a formal tangent approximation.

For the mixed representative above the marked point is
\((X,Y,Z)=(0,0,-1)\). Put
\[
 x=X,\quad y=Y+X-2X^2,\quad
 t=Z+1-5X+8X^2-4X^3.
\]
The conic and quintic have ideals
\(\Gamma=(x,y)\), \(\Delta=(t,y)\). Indeed on
\(\Delta_{\rm mix}\) the original curve parameter is
\(2X-1\); on \(\Gamma\) one has \(X=Y=0\).
In the blowup chart \(y=xv\) the graph section has ideal
\((v,t)\), with \(x\) its parameter, and \(x=0\)
is the contracted fiber near the point.

The threefold contains the projective line \(\mathfrak l\)
whose affine parametrization is
\[
 (X,Y,Z)=(x,-x,-1-x).
\]
Every projective coordinate in ML1 restricts to an affine
linear polynomial on it. This is the line corresponding
to the marked point of the degree-three ruling projection,
among the lines through \(z\). It meets \(\Delta\) only
at \(z\): away from \(X=0\), the quotient \(Y/X=-1\)
would force the original quintic parameter to be \(-1\),
which is precisely \(z\). At the point at infinity
on \(\mathfrak l\), \(y_0\ne0\), while the point at
infinity on the quintic parameter with \(y_4=0\) has
\(y_0=0\). The intersection is transverse there in
\(V_5\) in the sense of distinct tangent lines.
On its strict lift,
\[
 v=-2x,\qquad t=-6x+8x^2-4x^3.                           \tag{ML2}
\]
In particular \(t\) has simple vanishing.
This uses the actual line, not merely the contracted
fiber or an arbitrary tangent direction. The general
three-lines geometry of \(V_5\) is classical; cf.
 Amerik, [*Some remarks on morphisms between Fano
threefolds*, §1](https://ems.press/content/serial-article-files/25953?nt=1).
The marked formulas and their use below are the new
source/strict-intersection comparison.

#### A local tangency lemma for any \(p,q\ge2\)

Suppose \(P,S\) are the actual \(V_5\) equations of
degrees \(p,2q\), and \(W\) is primitive at the
marked point on the graph. In the same local
coordinates \((x,t,y)\), with
\(\Gamma=(x,y),\Delta=(t,y)\), write
\[
 P(0,t,0)=t^{2p}u(t),\quad u(0)\ne0,\qquad
 S'=x^{-q}S(x,t,xv).
\]
This uses the exact trace and marked binary-root
condition from the endpoint correspondence.
The other strict equation is \(P'=P(x,t,xv)\).
It vanishes on the entire marked fiber and on the
curve, and its linear part at the marked point is
zero: the \(t\)-derivative vanishes by the trace, the
\(x\)-derivative by the quintic, and the
\(v\)-derivative by the factor \(x\).
Thus primitivity forces \(S'\) smooth. Its
restriction to the marked fiber has order exactly
\(q\), so \(S'_v(0)=0\); also \(S'_x(0)=0\) since
it vanishes along the graph section. Hence
\(S'_t(0)\ne0\), and locally its smooth surface
can be written
\[
 t=f(x,v),\qquad f(x,0)=0,\qquad
 f(0,v)=v^q w(v),\quad w(0)\ne0 .
\]
The actual complete intersection on this smooth
surface is the Cartier divisor \(cT\), \(c=2pq\).
Consequently
\[
 P(x,f(x,v),xv)\in(v^{2pq}).                              \tag{ML3}
\]
This is the complete actual local equation, not
merely cancellation of the two first symbols.

The first-order expansion in the **curve parameter**
\(x\), writing \(f=f_0(v)+xf_1(v)+O(x^2)\), gives
\[
 [x^1]P(x,f,xv)=
 P_\Gamma'(f_0)f_1+
 P_x(0,f_0,0)+vP_y(0,f_0,0).                             \tag{ML4}
\]
Here \(\operatorname{ord}_v f_0=q,\ f_1(0)=0\).
Since \(P_\Gamma=t^{2p}u\), the first term has
order at least \((2p-1)q+1>q\).
Also \(P_x(0,0,0)=0\) because \(P\) vanishes on
\(\Delta\). Comparing coefficients of \(v\) and
\(v^q\), which must vanish by ML3, gives
\[
 \boxed{P_y(z)=0,\quad P_{xt}(z)=0.}                     \tag{ML5}
\]
In the second comparison \(vP_y(0,f_0,0)\)
has order at least \(q+1\) after the first.
In particular \(P\) is singular at \(z\), and
its quadratic part vanishes on the plane \(y=0\):
the \(x^2\) term is zero by \(\Delta\), the
\(t^2\) term by the trace (\(2p\ge4\)), and the
mixed \(xt\) term by ML5. The proof does not
require the carrier to be normal or its generic
first symbol to be nonzero.

For \(p=2\), the actual quadratic section \(P\)
must therefore contain the line \(\mathfrak l\):
it passes through \(z\) with tangent in \(y=0\),
so its restriction has zero order at least three,
greater than its degree two. This is the
elementary line-restriction argument for a
section of \(\mathcal O_{\mathfrak l}(2)\);
no assertion that every tangent plane section
of \(V_5\) contains a line is involved.

But by ML2 and the smooth \(S'\) equation,
\(S'(x,t(x),v(x))\) vanishes to **exact order one**
along the strict line, since \(S'_t(0)\ne0\),
\(S'_x(0)=S'_v(0)=0\), and \(t'(0)=-6\).
Thus on the original projective line \(S\) has
zero order exactly \(q+1\) at \(z\), by its
factor \(x^q\). It is a nonzero section of
\(\mathcal O_{\mathfrak l}(2q)\) and sole
support of the image CI would force its full
zero divisor to be \(2q[z]\). This contradicts
\(q+1<2q\). The mixed marked-point theorem follows.

#### All orders: the marked-line comparison by interpolation

The same mechanism has a sharp useful extension
beyond degree-two carriers. Retain \(p,q\ge2\)
and the mixed direction. With \(W\) primitive
at \(z\), use ML3 and the marked line
\((x,t(x),y(x))\) of ML2, where
\(t(x)=-6x+O(x^2)\), \(y(x)=-2x^2\).
Then
\[
 \boxed{\operatorname{ord}_x(P|_{\mathfrak l})
       \ge \min(2p,q+1).}                               \tag{ML9}
\]
The convention includes the identically zero
restriction. In particular **for every \(2\le
p\le q\)** a hypothetical pair on the
\((3p,4q)\) edge in a mixed direction must
be nonprimitive at the marked point.

**Proof.** In \(k[[x,y]]\), restrict the
actual \(S\) to the formal surface \(t=t(x)\).
Modulo \(x\) its equation has exact order \(q\)
in \(y\), because its homogeneous conic normal
form at \(z\) has all \(q\) roots at \([1:0]\).
By Weierstrass preparation its equation
is a unit times a monic polynomial \(Q(y)\)
of degree \(q\). Divide the corresponding
restriction of \(P\) by \(Q\) using Weierstrass
division, writing \(P=AQ+R(y)\), with
\(A\in k[[x,y]]\), \(R\in k[[x]][y]\),
\(\deg_y R<q\).

In the extension \(x=\epsilon^q\), put
\(v=\epsilon u\) in \(f(x,v)=t(x)\).
After dividing by \(\epsilon^q\), the special
fiber is \(w(0)u^q+6=0\), with \(q\) distinct
nonzero roots by characteristic zero.
All omitted terms vanish in the special fiber:
\(f(0,v)\) has exact order \(q\), and every
positive \(x\)-coefficient of \(f\) is divisible
by \(v\). Hensel's lemma therefore gives \(q\)
distinct roots \(v_i=\epsilon u_i(\epsilon)\).
The roots of \(Q(y)\) are exactly
\(y_i=xv_i\): for \(x\ne0\) they satisfy
\(S(x,t(x),y_i)=0\), and there are \(q\)
distinct such roots. These satisfy
\[
 \operatorname{ord}_{\epsilon} y_i
 =\operatorname{ord}_{\epsilon}(y_i-y_j)=q+1
 \quad(i\ne j).
\]
ML3 implies
\(\operatorname{ord}_{\epsilon}P(x,t(x),y_i)
 \ge2pq\).
On the marked line, \(y(x)\) has
\(\epsilon\)-order \(2q>q+1\).
Evaluate the Lagrange interpolation formula
for \(R\) at \(y(x)\). Every Lagrange basis
polynomial there is a unit over
\(k[[\epsilon]]\), since its numerator
and denominator have the same valuation
\((q-1)(q+1)\).
Hence \(R(y(x))\) has \(\epsilon\)-order at
least \(2pq\), i.e. \(x\)-order at least \(2p\).
The term \(A Q(y(x))\) has \(x\)-order at
least \(q+1\) since \(Q(y(x))\) is the product
of the \(q\) differences of
\(\epsilon\)-order \(q+1\).
This proves ML9. Notice that this is just
Weierstrass division and the simple-root
form of Hensel's lemma, not an assumption of
generic splitting of the global equation or
of a convergent analytic normal form.

If \(p\le q\), the lower bound is strictly
greater than \(p\), so the marked projective
line is contained in the actual degree-\(p\)
carrier. The actual degree-\(2q\) mate still
has vanishing order exactly \(q+1\) on this
line, contradicting sole support exactly as
above. If \(p>q\), the bound forces at least
\(q+1\) contact on the marked line but does
not force containment. The distinction is
a genuine degree limitation.
\(\square\)

This sharpens the primitive graph arithmetic
above: of its five possible global primitive
order pairs, the mixed direction is excluded
for \((2,2),(5,19),(6,8)\); only
\((10,4),(21,3)\) are still allowed in the
mixed direction by this test. The endpoint
directions remain subject to their normal
splitting and the separate marked-line
condition. The \((2,2)\) endpoint row was
already excluded by its normal splitting.
This all-order source obstruction is included in the scoped correctness review above.

#### Endpoint comparison and the precise remaining condition

Reverse the original quartic coordinates, which
exchanges the two endpoint directions. The
endpoint image quintic can be taken in ML1 as
\[
 (X,Y,Z)=(x,2x^2,4x^3),
\]
with marked point the origin. This follows from
the displayed \(\Delta_{\rm end}\) formula by
reversal and normalization of \(y_4\). Use
\(y=Y-2X^2,\ t=Z-4X^3\). The projective line
\(\mathfrak l_{\rm end}\) has \((X,Y,Z)=(x,0,0)\);
the remaining coordinates in ML1 are zero except
\(y_4=1\). Its intersection with the quintic
is supported at \(z\) (the quintic's point at
infinity is not on this line), and its tangent
is the tangent of the quintic. On the strict lift,
\[
 v=-2x,\qquad t=-4x^3.
\]
The same ML5 proof forces the degree-two carrier
to contain this line if \(W\) is primitive at
the marked point. The mate then has only
\(2q[z]\) as its intersection divisor on the
line. Since \(S'= \text{unit}\cdot(t-f(x,v))\),
the exact necessary contact becomes
\[
 \boxed{\operatorname{ord}_x(-4x^3-f(x,-2x))=q.}         \tag{ML6}
\]
This is not contradictory from the leading
fiber degree alone. It is the actual required
higher contact, not an unconstrained higher
symbol. In contrast to the mixed case the
linear term of \(t\) vanishes on the strict
line.

The two cases illustrate the role of
the *uncontracted line* in the image
threefold and its strict lift. The
[conditional K3 obstruction](k3_marked_lattice.md#a-k3-marked-lattice-obstruction-to-the-primitive-graph-row) is
subsumed as an exclusion of the
globally primitive mixed \((6,8)\) row;
its ADE correction analysis remains
useful for other source strata.

#### Consequence for the pointwise resultant

For every mixed \((6,4q;2,q)\), SC6
forces generic curvilinearity on the
first graph and ML5--ML6's argument
forces \(D_{W,\rm top}(z)>0\).
By SC2 the divided exceptional resultant
has the explicit positive common-defect
contribution at this prescribed marked point,
not only an unspecified effective divisor
of positive degree somewhere. In particular
at \((6,8)\) the mixed slope-three row of SC1
is excluded and the slope-four row has
\(D_W=7\) in degree with at least one unit
at \(z\). There is no restriction here
on the endpoint slope-five row beyond
the stated conditional line contact.
These deductions depend on R-0077 and
were covered by the scoped correctness review above.

### Full marked finite-modification lattice in the primitive-at-the-point stratum

The local form in ML3 also supplies a
higher-layer refinement of SC3--SC4.
Suppose on any \((3p,4q)\) edge that
\(W\) is primitive just at \(z\), not
necessarily elsewhere. Use \(R=k[[x]]\)
and the smooth \(S'\) parameter \(v\):
\[
 A_W=R[v]/(v^{2pq}),\qquad
 A_Z=R[xv,f(x,v)]\subset A_W .
\]
The notation denotes the finite complete
\(R\)-subalgebra; \(f(x,0)=0\) and
\(f(0,v)\) has exact order \(q\).
The \(2pq\) elements
\[
 (xv)^i f(x,v)^j,\quad
 0\le i<q,\quad 0\le j<2p
\]
form an actual \(R\)-basis of \(A_Z\).
Indeed after factoring \(x^i\) from each
column their reduction at \(x=0\) has
distinct initial \(v\)-powers \(qj+i\),
covering all powers from zero to \(2pq-1\).
Their determinant length inside \(A_W\) is
\(2p\sum_{i=0}^{q-1}i=pq(q-1)\).
This is exactly the entire finite quotient
length SC3, so the sublattice generated
by them equals \(A_Z\), not merely a
finite-index submodule. The argument
works despite nonzero lower \(v\)-terms
of \(f\) over the generic point of \(R\).
For \(q>2\) it does not by itself identify
that basis with the saturated power flag.

For \(q=2\) there is a stronger exact normal
form. Subtract \(f_v(x,0)v\) from \(f\);
its coefficient lies in \(xR\), so this
is a change of image generator
\(t'=t-(f_v(x,0)/x)y\), preserving the
marked conic and quintic ideals.
Now \(t'=v^2u(x,v)\) for a unit \(u\).
Take a formal square root and put
\(w=v\sqrt u\), so \(t'=w^2\).
The inverse substitution writes
\(v=w a(x,w^2)+b(x,w^2)\) with \(a\) a unit
and \(b(x,0)=0\), by separating even and odd
powers. Replacing \(y\) by
\((y-xb(x,t'))/a(x,t')\) preserves the
two marked curves and gives \(y'=xw\).
Thus the *embedded completed ideal*
of the image CI in these formal coordinates
is exactly
\[
 \boxed{I_Z=(\,y'^2-x^2t',\ t'^{\,2p}\,),\quad
        A_Z=R[w^2,xw]\subset R[w]/(w^{4p}).}            \tag{ML7}
\]
To check the ideal, the displayed quotient
is \(R\)-free with basis \(y'^i t'^j\),
\(i=0,1,\ 0\le j<2p\), and maps injectively to
\(A_W\) by that basis. It is onto the image
algebra generated by the new coordinates.
This proof does not assume a global retraction
or the existence of actual primitive image
thickenings.

The saturated flag is now explicit:
the free first layer is generated by \(xw\),
whereas the saturated layer of order \(j\)
has image generated by \(x^{j\bmod 2}w^j\).
Hence its multiplication divisors at \(z\)
are precisely \(D_{Z,j}(z)=2\lfloor j/2\rfloor\).
The top value \(4p-2\) agrees with SC4;
this is a refinement of that scalar equality,
not a second independent genus constraint.

If \(P\) is also generically regular on the
image quintic, the actual carrier and Cartier
index have a sharp local dichotomy. Drop
primes in the coordinates of ML7.
Since \(S\in(x,y)^2\), and \(S'\) has exact
fiber degree two at the marked point,
\[
 S=B t^{2p}+C(y^2-x^2t),\qquad
 B\in(x,y)^2,\quad C\ \text{a unit}.
\]
The coefficient containment uses that \(t\) is
a nonzerodivisor modulo \((x,y)^2\).
The actual ideal generators and the nonzero conic
trace similarly give, after multiplying by a unit,
\[
 P=t^{2p}+\alpha(x,t,y)(y^2-x^2t).                      \tag{ML8}
\]
If \(\alpha(z)\ne0\), rescale \(x,y\) by
\(\sqrt\alpha\), a formal coordinate change
preserving the quintic, to obtain the usual
\(D_{2p+1}\) equation \(t^{2p}+y^2-x^2t\).
Its actual marked Cartier index is **two**,
not four: the equation \(t=0\) cuts \(2\Delta\)
and the singular carrier cannot have \(\Delta\)
Cartier with smooth reduced support. The first
symbol has order two at \(z\). In the normal
case the locally free divisorial square descends
from completion by faithful flatness; the
index is the downstairs one. The classification
of rational double points used in this
identification is classical, e.g. Artin,
[*Coverings of the rational double points*](https://doi.org/10.1017/CBO9780511569197.003).
No new classification of \(D_n\) singularities
is being claimed.

If \(\alpha(z)=0\), the carrier has multiplicity
at least three, and its saturated first-symbol
order at \(z\) is \(2+\operatorname{ord}_x
\alpha(x,0,0)\ge3\), since it is generically
regular. Its actual local almost-Cartier index
is **\(4p\)**. To see this, the actual mate
implies that the local index \(r\) divides
\(4p\) and \(S\) on \(P\) is a unit times
\(h^{4p/r}\) for an equation of \(r\Delta\),
using the [S2 power theorem](../carriers/normal_carrier_symbolic_torsion.md#normality-is-unnecessary-the-actual-almost-cartier-power-theorem).
If \(r=1\), the carrier would be smooth at the
marked smooth Cartier curve. Otherwise \(r\ge2\),
and if \(4p/r\ge3\), multiplicity of \(S\)
at least three modulo \(P\) is impossible
since \(S\) has quadratic part a unit times
\(y^2\). If \(4p/r=2\), a lift of \(h\)
must have linear part a nonzero multiple of
\(y\). But \(y=xw\) generates the free
first normal quotient of the actual CI,
and a function of generic curve valuation
\(r\ge2\) maps to zero in that free quotient.
Contradiction. Thus \(r=4p\).
This direction of the index argument only
uses existence of a downstairs Cartier
multiple and the actual completed equations;
it does not assume the carrier normal at \(z\).

The two cases exhaust the local primitive
graph stratum when \(q=2\). In particular
the primitive-at-\(z\) endpoint \((6,8)\)
row, if present, has an image sextic-side
carrier with either the marked index-two
\(D_5\) type or a multiplicity-at-least-three
point of actual index eight. On the mixed
sextic edge the entire primitive-at-\(z\)
stratum was already excluded by the line
argument. This local classification is
kept for its wider use beyond the forbidden
mixed case.


### Finite-index rigidity of higher marked jets

**Necessary theorem, characteristic zero, covered by the scoped correctness review above.**
The exact marked finite-lattice basis above has an additional
consequence for \(q\ge3\). It constrains the coefficient of
the *actual* local equation \(S'\), before passing to an
intrinsic graded algebra.

Let \(R=k[[x]],\ B=R[v]/(v^{qh})\), \(q\ge2,h\ge2\),
and let
\[
 y=xv,\quad t=f(x,v),\quad f(x,0)=0,\quad
 f(0,v)=v^q u(v),\quad u(0)\ne0.
\]
Assume the image algebra \(A=R[y,t]\subset B\)
has finite colength exactly \(qh(q-1)/2\).
The classes \(y^it^j\) for
\(0\le i<q,\ 0\le j<h\) have distinct initial
\(v\)-orders \(i+qj\) after extracting \(x^i\).
Consequently their \(R\)-span \(M\) has that same
colength, so \(A=M\). This is the finite-index
basis proof above, expressed without global geometry.
In particular the *finitely many border products*
\[
 y^q t^j\ (0\le j<h),\qquad
 y^i t^h\ (0\le i<q)                               \tag{MJ1}
\]
must all belong to the displayed \(R\)-span \(M\).
Conversely these border products being in \(M\)
make \(M\) closed under multiplication by
its algebra generators \(y,t\), hence \(A=M\).
Thus (MJ1) is an exact finite **local equation gate**
for attaining the maximal permitted finite-modification
colength. In a calculation one should reduce
these products by the actual \(qh\times qh\)
basis matrix over \(k[[x]]\), rather than only
check its determinant.

**Classical algebra identification.** This closure test is the rectangular
instance of the border-basis criterion: a chosen monomial basis together
with its border reductions defines the intended zero-dimensional algebra
exactly when the formal multiplication operators commute (equivalently,
the neighboring border syzygies reduce compatibly). See
Kehrein--Kreuzer, *Characterizations of Border Bases*, J. Pure Appl.
Algebra 196 (2005), 251--270. Thus MJ1 itself is not a new general
border-basis theorem; the STCI-specific content begins with the forced
marked-jet consequences MJ2--MJ4.

Write \(f(x,v)=f_0(v)+x f_1(v)+O(x^2)\).
Then (MJ1) implies
\[
 \boxed{\quad f_1(v)\equiv\lambda v\pmod {v^q},
      \qquad \lambda\in k.\quad}                       \tag{MJ2}
\]
Here \(\operatorname{char}k\nmid h\) is enough for
this first-jet assertion if the same finite-index
identity holds in that characteristic.

**Proof.** The element \(t^h=f^h\) lies in
\(M\). Modulo \(x^2B\) its expansion is
\(h x f_0^{h-1}f_1\), because
\(f_0^h=v^{qh}u^h=0\). In an \(R\)-linear
expression in the basis \(y^it^j\),
its reduction modulo \(x\) forces all
coefficients of the \(i=0\) basis elements
to be divisible by \(x\), since
\(1,f_0,\ldots,f_0^{h-1}\) are independent
over \(k\) modulo \(v^{qh}\). Dividing by
\(x\) and reducing modulo \(x\) gives
\[
 h f_0^{h-1}f_1
 =\sum_{j<h}a_j f_0^j+
      \sum_{j<h}b_j v f_0^j
              \pmod {v^{qh}} .
\]
Every displayed term has distinct initial
\(v\)-order \(qj\) or \(qj+1\).
Since \(f_1(0)=0\), the left side has
\(v\)-order at least \(q(h-1)+1\).
Triangular independence forces all
coefficients to vanish except possibly
\(b_{h-1}\). Divide by the unit \(u^{h-1}\)
and the power \(v^{q(h-1)}\), obtaining
\(h f_1=\lambda'v\bmod v^q\), as required.
The proof is a DVR lattice computation,
not a deformation-theoretic existence
theorem. \(\square\)

For \(q=2\) (MJ2) is automatic after the
linear \(v\)-term is recognized; the previous
exact completed normal form ML7 is stronger.
For \(q=3\) it forbids an \(xv^2\) coefficient
in \(f\). For example,
\[
 f=v^3+xv^2,\qquad B=k[[x]][v]/(v^{12})
\]
does **not** have colength twelve
over its image \(k[[x]][xv,f]\), although
the canonical twelve basis columns alone
have colength twelve. Indeed
\(f^4=4xv^{11}+O(x^2)\) in \(B\), whereas
all degree-11 monomials in the canonical
basis require an \(x^2\)-factor.
The extra product enlarges the subalgebra.
This is a control against checking the
resultant determinant while omitting
multiplication closure.

On the marked \((3p,4q)\) edge where the
graph is primitive at the marked point,
put \(h=2p\). The exact finite quotient
length SC3 forces precisely the colength
in this theorem. In the actual marked
chart with \(S':t=f(x,v)\) smooth, the
change \(t\mapsto t-\lambda y\) preserves
the marked conic and quintic, and removes
the linear term in (MJ2) so that
\[
 \partial_x f(0,v)\equiv0\pmod {v^q}.                  \tag{MJ3}
\]
This is a local *source constraint* on the
actual image section, not a claim that every
locally allowed \(f\) lifts to a degree-\(2q\)
section or yields the required global CI.

There is a further necessary contact condition
in the **endpoint** chart where the distinguished
line has \(t=-4x^3,\ v=-2x\). In the original
fixed coordinates, write
\(f=f_0+x f_1+x^2 f_2+\cdots\).
If the order on this line is the required \(q\)
and \(q\ge3\), (MJ2) forces
\(\lambda=0\) (otherwise the line contact has
order two). For \(q\ge4\), the order-three
coefficient must then cancel, giving
\[
 \boxed{\ f_1(v)\equiv0\pmod {v^q},\qquad
                [v]f_2(v)=2.\ }                        \tag{MJ4}
\]
Indeed \(f_0(-2x)=O(x^q)\) and
\(x^2 f_2(-2x)=-2[v]f_2\,x^3+O(x^4)\);
the line equation has coefficient \(-4\)
at \(x^3\). For \(q=3\), the order-three
coefficient is only required to be nonzero,
not to vanish. These statements use the
specific marked coordinates: a simultaneous
coordinate change of \(t\) and the line
changes the displayed coefficient, but
not the intersection order. They do
not exclude the endpoint rows; they
give concrete low-jet constraints to impose
on their actual homogeneous section spaces.

The mechanisms involved here are the
standard DVR Smith/index comparison and
finite Weierstrass expansion, already used
in SC3 and ML7. The nontrivial additional
step is to use **algebra closure of the full
finite image**, rather than merely
a section-space determinant. No all-degree
novelty claim or local-to-global lift
claim is made.

