# Two blowups, actual residual cycles, and supporting nef bounds

Fix C=C0 over an algebraically closed characteristic-zero field. The seven cubics give the established graph B=Bl_C(P3)=Bl_Gamma(V5), where Gamma is a smooth conic. This underlying birational model is verified in [Cheltsov–Przyjalkowski–Shramov, Lemma 6.13](https://arxiv.org/html/1809.09223v1#S6.L13). The explicit cubic-image construction and its exact certificate are retained in the conditional sextic geometric account; the model itself does not require a (6,16) pair. The deductions below have independent review.

## The two blowups and their actual global section dictionary

Write

\[
H=\pi^*\mathcal O_{\mathbf P^3}(1),\quad E=\pi^{-1}(C),
\quad L=3H-E,\quad Q'=2H-E.
\]

The other projection is
\(\phi:B=\operatorname{Bl}_\Gamma V\to V\), with
\(L=\phi^*M\), \(M=\mathcal O_V(1)\), and exceptional divisor \(Q'\).
Its fibers on \(Q'\cong\mathbf P^1\times\mathbf P^1\) are the trisecant
ruling lines of the original quadric \(Q=V(q)\). The useful change of basis is

\[
\boxed{H=L-Q',\qquad E=2L-3Q'.}\tag{1}
\]

## 2. Actual equation spaces become sections with prescribed conic vanishing

Here and below \(I_C^r\) and \(I_\Gamma^e\) are **ideal sheaf powers**.
Their global sections are not being identified silently with an unsaturated
homogeneous ideal power.

**Section dictionary.** For integers \(r\ge0\) and \(a\ge3r\), there is a
natural vector-space identification

\[
\boxed{
H^0(\mathbf P^3,I_C^r(a))
\cong H^0\bigl(V,I_\Gamma^{\,a-3r}(a-2r)\bigr).
}\tag{2}
\]

Indeed the left side is \(H^0(B,aH-rE)\). By (1),

\[
aH-rE=(a-2r)L-(a-3r)Q'.
\]

For the blowup of a smooth codimension-two center,
\(\phi_*\mathcal O_B(-eQ')=I_\Gamma^e\) for \(e\ge0\).
This follows directly on a regular-parameter chart from the Rees algebra;
the same fact for \(\pi\) gave the first equality. The projection formula
proves (2). See also the primary [Stacks blowup construction](https://stacks.math.columbia.edu/tag/01OF).

This correspondence retains actual global constant coefficients. It is not
merely a correspondence between symbols over \(k(C)\).

For completeness the other region has a simple interpretation. If
\(2r\le a\le3r\), put \(k=a-2r\), \(j=3r-a\). Then

\[
H^0(\mathbf P^3,I_C^r(a))\cong H^0(V,\mathcal O_V(k)),
\quad aH-rE=kL+jQ'.\tag{3}
\]

Here \(\phi_*\mathcal O_B(jQ')=\mathcal O_V\): a rational function allowed
to have poles only above a codimension-two subset extends on normal \(V\).
Every section has the fixed factor \(q^j\) downstairs. If \(a<2r\), the
space is zero, since the same calculation leaves a negative multiple of
the ample class \(M\). For example, the familiar spaces of order-two forms
in degrees four, five and six become respectively constants times \(q^2\),
\(q\) times the seven cubics, and all quadric sections of \(V\). These are
checks of the dictionary, not new claims about those previously computed
spaces.

There is an explicit polynomial construction behind (2). Let

\[
(c_0,\ldots,c_6)=(qx_0,qx_1,qx_2,qx_3,
x_0^2x_2-x_1^3,x_0x_2^2-x_1^2x_3,x_2^3-x_1x_3^2).
\]

Take a section \(P\in H^0(V,I_\Gamma^e(k))\). Projective normality of the
inherited cubic model represents it by a degree-\(k\) polynomial in the
\(y_i\). Then

\[
F(x)=\frac{P(c_0(x),\ldots,c_6(x))}{q(x)^e}\tag{4}
\]

is a polynomial of degree \(a=3k-2e\), vanishing to order at least
\(r=k-e\) on \(C\), when \(k\ge e\ge0\). Divisibility by \(q^e\) can be
checked at the generic point of \(Q\), where \(\phi\)'s transverse order to
\(\Gamma\) is the \(q\)-order; polynomial unique factorization then gives
global divisibility. Formula (2) supplies the coordinate-free justification.
No claim about a chosen nonsaturated ideal presentation of
\(I_\Gamma^e(k)\) is required.

If \(P\) has exact generic order \(e\) on \(\Gamma\), then \(F\) has no
quadric factor. If its divisor does not contain the surface \(\Sigma\) of
§3, then \(F\) has exact order \(r\) on \(C\). Conversely, a form of exact
order \(r\) with no quadric factor gives exactly these conditions. Thus this
is an equation-construction dictionary with explicit order checks.

## 3. The original exceptional divisor has a fixed anticanonical image

The image of \(E\), which was not identified in the retrieved source notes,
is particularly useful. Set

\[
\Sigma=V\cap V(y_0y_3-y_1y_2)\subset\mathbf P^6.
\]

**Proposition.** \(\Sigma\) is an integral nonnormal
anticanonical surface on \(V\). Its normalization is the finite birational
map

\[
\nu=\phi|_E:E\cong\mathbf P^1\times\mathbf P^1\longrightarrow\Sigma.
\]

Put \(B_0=E\cap Q'\), to distinguish this curve from the threefold \(B\).
Then

\[
\boxed{\phi^*\Sigma=E+3Q',\quad B_0\sim(1,1)\text{ on }E,
\quad I_{\mathrm{cond},E}=\mathcal O_E(-2B_0).}\tag{5}
\]

The map \(B_0\to\Gamma\) has degree three and, in the displayed coordinates,
is \([s:t]\mapsto[s^3:t^3]\) followed by the conic embedding. In particular
its two totally ramified values retain the marked endpoint geometry of \(C\).

**Proof.** Substitution of the seven cubics gives the literal identity

\[
c_0c_3-c_1c_2=q^3.
\]

The divisor of this section of \(2L=6H-2E\) on the blowup is
\(3Q'+E\). The nonexceptional component is \(E\), with coefficient one;
hence its image is precisely the integral reduced quadratic section
\(\Sigma\), and the equality in (5) is scheme-theoretic at the divisor
level. Since \(K_V=-2M\), adjunction gives \(\omega_\Sigma=\mathcal O_\Sigma\).
The morphism \(\phi\) is an isomorphism off \(Q'\), so \(\Sigma\) is smooth
off \(\Gamma\).

No contracted ruling of \(Q'\) lies in \(E\): its intersection with \(E\)
is its length-three intersection with \(C\) on \(Q\). Thus \(\phi|_E\) has
finite fibers and is finite, as it is proper. It is birational, since it is
an isomorphism outside \(B_0\). Smooth \(E\) is therefore the normalization.

Use the product coordinates on \(E\) given by R-0020 and the lines convention
for \(\mathbf P(N_C)\). Then

\[
H|_E=\mathcal O(4,0),\quad E|_E=\mathcal O(7,-1),
\quad L|_E=\mathcal O(5,1),\quad Q'|_E=\mathcal O(1,1).
\]

The curve \(B_0\) is the section of the normal projective bundle supplied by
the smooth quadric, so is smooth and isomorphic to \(C\). On \(Q'\), take
coordinates with
\(x_0=ua,x_1=ub,x_2=va,x_3=vb\). Then \(C\) has equation
\(va^3-ub^3=0\), and the last three cubic coordinates restrict, after
removing this equation, to \([u^2:uv:v^2]\). This proves the degree-three
map and its endpoint assertion.

Finally finite duality for the normalization of a Gorenstein surface gives

\[
\nu_*\omega_E=
\mathcal Hom_\Sigma(\nu_*\mathcal O_E,\omega_\Sigma),
\]

which, with \(\omega_\Sigma=\mathcal O_\Sigma\), identifies the conductor
ideal on \(E\) with \(\omega_E\cong\mathcal O_E(-2,-2)\). Its support is
contained in the single smooth irreducible curve \(B_0\); an invertible
ideal with this support is \(\mathcal O_E(-dB_0)\). Comparison of classes
forces \(d=2\), proving the full ideal assertion in (5), including the
absence of an additional punctual correction. The finite-duality formula
is the same standard input already independently reconstructed in the
[October 21 review, §2](../carriers/normalization_conductor_phase2_addendum.md);
see also [Stacks, finite morphisms](https://stacks.math.columbia.edu/tag/0FKW).

At a general point of \(\Gamma\), the three preimages in \(B_0\) are
distinct. The transverse curve singularity of \(\Sigma\) is therefore an
ordinary triple point; \(2B_0\) is the expected conductor on its three
branches. No assertion of this transverse type is made at the ramified
endpoint values.

This produces an actual, explicitly marked nonnormal anticanonical surface
associated to the quartic. It is not a containing surface in the original
\(\mathbf P^3\), and no fixed-carrier STCI result is transported to it.

## 4. Residual curves and the two different ways a curve can disappear

The [symbol attachment refinement and sextic slack control](../../results/connected_normal_directions.md#what-the-cubic-contraction-misses-in-the-attachment-count) compare the contracted residual cycle with the demand visible in its normal symbols.

Let \(F_a,G_b\) be an actual proper pair with exact generic normal orders
\(r,s\) along \(C\), and write

\[
[V(F,G)]=m[C]+R.
\]

On \(B\) their strict transforms have classes
\(A=aH-rE\), \(A'=bH-sE\) and have no common surface component. Their
scheme intersection \(W\) is a proper complete-intersection curve. There is
an identity of actual cycles, stronger than an equality of Chow classes:

\[
\boxed{\pi_*[W]=(m-rs)[C]+R.}\tag{6}
\]

Off \(C\), the actual residual cycles agree because \(\pi\) is an
isomorphism. At \(\eta_C\), work in the two-dimensional regular local ring
\(\mathcal O_{\mathbf P^3,\eta_C}\). Its blowup at the maximal ideal has
exceptional \(\mathbf P^1_{k(C)}\). The local blowup intersection formula is

\[
i_{\eta_C}(F,G)
=rs+\sum_{z\in\mathbf P^1_{k(C)}}
[\kappa(z):k(C)]\,i_z(F',G').
\]

This formula follows by separating the exceptional orders \(r,s\) in the
intersection of two plane germs; the exceptional contribution is their
product and the remaining local intersections are those of their strict
transforms. The weighted sum is exactly the coefficient of \(C\) in
\(\pi_*[W]\), proving (6) coefficient by coefficient. The projection formula
and \(\pi_*(E^2)=-[C]\) give a separate check of its Chow class; that check
alone would not prove the actual-cycle assertion.

The components of \(W\) outside \(E\) are precisely the strict transforms
of actual residual components. Components contained in \(E\) can dominate
\(C\) or map to isolated points. Consequently

\[
\boxed{R=0\quad\Longleftrightarrow\quad\operatorname{Supp}W\subset E.}\tag{7}
\]

For (7), use that \(\pi\) is an isomorphism off \(E\) and \(W\) is pure
one-dimensional. This criterion concerns the actual strict-transform
intersection, not the common zeros of two leading symbols alone.

The second projection gives complementary visibility:

| Curve on the graph \(B\) | Image in \(\mathbf P^3\) | Image in \(V\) |
|---|---|---|
| A fiber of \(E\to C\) | A point | A line in \(\Sigma\) |
| A ruling fiber of \(Q'\to\Gamma\) | An actual trisecant line | A point of \(\Gamma\) |
| A curve in \(E\) dominating \(C\) | Thickness along \(C\) | A curve in \(\Sigma\) |
| A curve outside \(E\cup Q'\) | Residual curve | Its birational transform |

Thus even an actual curve in \(\Sigma\) need not be a residual curve in the
original space; conversely an actual residual trisecant can vanish to a point
on \(V\). The weaker condition \(\phi(W)\subset\Sigma\) does **not** replace
(7), since \(\phi^{-1}(\Sigma)=E\cup Q'\). Retain the graph and both
projections whenever residual support matters.

The numerical record of the two polarizations, useful without any generic
coprime-symbol assumption, is

\[
\begin{aligned}
H\cdot W&=ab-4rs,\\
E\cdot W&=4(as+br)-14rs,\\
L\cdot W&=3ab-4(as+br)+2rs,\\
Q'\cdot W&=2ab-4(as+br)+6rs.
\end{aligned}\tag{8}
\]

These follow from \(H^3=1,H^2E=0,HE^2=-4,E^3=-14\).
An intersection number with \(E\) or \(Q'\) is not a point count if \(W\)
has a component in that divisor. Nor does its sign by itself assert a
residual component downstairs.

### Actual equations on the zero-direction edge

Cheltsov–Przyjalkowski–Shramov, [Lemma 6.13 and diagram (6.14)](https://arxiv.org/html/1809.09223v1#S6.L13), prove the two-blowup birational model and explicitly display the same monomial quartic in the proof. Their lemma does not assert the actual-section realization criterion. This published birational model is an input; the actual-section equivalence below is proved here, not attributed to that lemma. The projection from the conic has pullback class \(M-Q'\), giving \(H=L-Q'\), \(E=2L-3Q'\). The seven cubics are the coordinate model for \(L=3H-E\).

**Proposition (fixed direction).** Work over an algebraically closed field of characteristic zero; fix \(p,q>0\) and a constant section \(T\subset E\). Put \(\Delta=\phi(T)\) and \(z=\phi(T\cap Q')\). There are proper homogeneous equations of degrees \((3p,4q)\), exact normal orders \((p,q)\) along \(C\), sole reduced support \(C\), and first strict-intersection support \(T\), if and only if there are sections \(P\in H^0(V_5,pM)\), \(S\in H^0(V_5,I_\Gamma^q(2qM))\) with all of the following:
- \(P,S\) meet properly; neither divisor contains the anticanonical image \(\Sigma=\phi(E)\); their exact orders along \(\Gamma\) are \(0,q\).
- Their intersection has reduced support exactly \(\Delta\).
- The value at \(z\) of the degree-\(q\) normal form of \(S\) along \(\Gamma\) is nonzero.

**The marked curve and fibre.** \(L|_E=(5,1)\) and \(Q'|_E=(1,1)\), so \(L\cdot T=5,\; Q'\cdot T=1\); a constant section is not the diagonal-type \(B_0=E\cap Q'\). Thus \(T\) meets \(Q'\) in a unique transverse point. The map \(\phi|_T\) is proper quasi-finite, hence finite, and an isomorphism away from this point. On a chart of the conic blowup, a generator of \(I_\Gamma\) pulls back to a local equation of \(Q'\), which restricts to a uniformizer of \(T\). Thus the fibre over \(z\) is one reduced point. For the finite map to the reduced image, Nakayama now gives surjectivity of \(\mathcal O_{\Delta,z}\to(\phi|_T)_*\mathcal O_T\), because the fibre algebra is generated by \(1\); the map is injective since the image is the reduced integral curve. Hence \(\Delta\simeq T\) is smooth rational degree five and \(\Delta\cap\Gamma\) is the reduced point \(z\), using \(I_\Gamma\mathcal O_B=\mathcal O_B(-Q')\).

**Actual sections, orders and properness.** By blowup pushforward of ideal sheaf powers and the projection formula, \((3p)H-pE=pL\), \((4q)H-qE=2qL-qQ'\) give exactly the two actual section spaces above. These identifications preserve homogeneous equations, not arbitrary normal symbols. For a corresponding section, exact vanishing order along \(\Gamma\) makes its divisor after subtracting the prescribed \(Q'\) multiple free of \(Q'\); equivalently the resulting original polynomial has no quadric divisor. Exact order along \(C\) similarly excludes \(E\) from that divisor, equivalent to not containing \(\Sigma\). Both implications use \(\phi(E)=\Sigma\) and the generic isomorphism of the blowup outside its exceptional divisor. These guarantees ensure the strict divisors on the graph represent both presentations, so common surface components correspond: any common surface on either target not among the exceptional images lifts to a common surface on the other side. The other potential common surface would be \(Q\) or \(\Sigma\), removed by order conditions. An original sole-support proper pair has neither quadric factor: if one contained the smooth quadric and the other did not, the restriction of the latter to \(Q\) would give a nonzero divisor of class \((b,b)\) not supported solely on \(C\sim(1,3)\); if both did they would not be proper.

**Forward direction.** By R-0077, sole support on the edge \(a=3p,b=4q\) has \(u=0\) and gives \(W_\mathrm{red}=T\) on the graph. Off \(\Gamma\) the image intersection is precisely \(\Delta\setminus\{z\}\). A point \(\gamma\in\Gamma\) of \(V(P,S)\) is a zero of \(P|_\Gamma\), so the strict \(P\) divisor contains the whole fibre \(Q'_\gamma\) (order of \(P\) is zero). The strict \(S\) divisor restricts there to its leading homogeneous binary form of degree \(q>0\): either it vanishes on the whole fibre or it has at least one root over the algebraically closed field. Thus \(\gamma\) is in \(\phi(W)\), and must be \(z\). At \(z\) the leading form cannot vanish identically, since its whole fibre would be a curve of \(W\) not contained in the section \(T\) and would push to a genuine trisecant residual line downstairs. Thus both conditions hold.

**Reverse direction.** Because \(S\) vanishes on \(\Gamma\), exact order zero for \(P\) and the common support \(\Delta\) give \(P|_\Gamma\) nonzero with zero divisor exactly \(2p[z]\). Consequently the strict \(P\) divisor meets \(Q'\) only over \(z\). The strict \(S\) divisor cuts the nonzero degree-\(q\) form on this one fibre, so there is no vertical curve in \(W\). Off \(Q'\) the intersection has support the graph lift of \(\Delta\setminus\{z\}\), whose closure is \(T\). The proper intersection \(W\) of Cartier divisors is pure, so it has support exactly \(T\). In particular the binary form has all \(q\) zeros (with multiplicity) at \(T\cap Q'\). Since \(T\subset E\), pushing to \(\mathbf P^3\) gives sole support: any residual curve there would have a strict transform outside \(E\). Membership in the original two ideal-sheaf powers already gives \(C\) in the reduced support. This is equivalence for actual pairs with all conditions retained, not a proof that such sections exist.


Finally, in the marked balanced coordinates on the chart \(x_0=1\),
write \(t=x_1\), \(v=x_2-t^3\) and \(u=x_3-t^4-3tv/2\).
The quartic's torus scales \(u,v\) with weights \(4,3\), so all
mixed constant directions form one orbit. Coordinate reversal
conjugates the torus action to its inverse and swaps the two fixed
directions. Direct expansion at first normal order gives \((u',v')=t^{-7}(v/2,2u)\), explicitly exchanging the endpoint directions. These automorphisms lift to the cubic graph and preserve
the marked conic. One endpoint direction and one mixed direction
therefore suffice.

The two curves and the first equation source are explicit. In the cubic
coordinates \((y_0,\ldots,y_6)\) of (4), evaluate the linear normal
part of each cubic at \((u,v)=(1,0)\) and \((1,2)\), respectively.
Homogenizing the following rows to degree five gives the maps on the
whole base.
\[
\begin{aligned}
 \Delta_{\rm end}(t)&=[1:t:t^3:t^4:0:-t^2:-2t^5],\\
 \Delta_{\rm mix}(t)&=[1+t:t+t^2:t^3+t^4:t^4+t^5:2:t^3-t^2:-2t^5].
\end{aligned}
\]
In each row the coordinates span the polynomials of degree at most
five. Thus each is a rational normal quintic in a unique hyperplane.
The respective hyperplane equations are
\[
 h_{\rm end}=y_4,\qquad
 h_{\rm mix}=2y_0-2y_1+2y_2-2y_3-y_4-2y_5-y_6 .
\]
On \(\Gamma=[0:0:0:0:i^2:ij:j^2]\) these restrict to \(i^2\) and
\(-(i+j)^2\), respectively. For either representative the whole space
of first equations vanishing on \(\Delta\) with trace \(2p[z]\) is
\[
      P=\lambda h_\Delta^p+K,\qquad
      \lambda\in k^\times,\quad
      K\in H^0(V_5,I_{\Gamma\cup\Delta}(pM)).
\]
Indeed, subtracting the matching scalar power kills the restriction
on both curves. Properness, the exact-order conditions and the two
requirements on \(S\) still have to be satisfied.

The revised proof supplies both directions of the criterion, the
reduced conic intersection, the exceptional fiber condition and the
two representatives under the marked symmetries; the associated R-0077 review remains pending. Exact substitution
in the seven cubics verified both rows, their rank-six spans and the
two hyperplane traces on the conic. Existence of the required sections
for either quintic remains open.

### The marked correspondence on the whole equality boundary

Work in characteristic zero. For an actual proper pair of degrees
\((a,b)\) and exact orders \((r,s)\) along \(C\), put
\[
 K=16(as+br)-7ab-28rs .
\]
Under sole support and \(K=0\), the slack identity and connectedness
give a single constant section \(T\) as the reduced strict
intersection on the graph. Write \(\Delta=\phi(T)\) and
\(z=\Delta\cap\Gamma\) as in the endpoint correspondence. In the
same marked frame the actual source spaces on \(V_5\) are
\[
 H^0(\mathcal I_\Gamma^{a-3r}((a-2r)M)),\qquad
 H^0(\mathcal I_\Gamma^{b-3s}((b-2s)M)).
\]
The exponents are nonnegative by quadric restriction: neither
original equation can have the quadric as a factor. Impose exact
orders along \(\Gamma\), properness, and no \(\Sigma\) component.
Then sole support on this marked section is equivalent to these
conditions on the actual sections:

- Off \(\Gamma\) their common reduced support is
  \(\Delta\setminus\{z\}\).
- On the exceptional ruling over any \(\gamma\ne z\), their conic
  normal forms have no common root; over \(z\) the two forms do not
  both vanish identically.

Indeed the actual-section dictionary and the same exceptional
component checks as at the endpoint identify the strict divisors.
Their common scheme off the exceptional divisor is the punctured
section. The ruling test leaves at most finitely many points on the
marked fiber and none on the other fibers. Purity of the strict
complete intersection excludes isolated components; the strict support
is \(T\). Conversely a strict intersection supported on \(T\) has those
fiber properties. If both conic orders are positive the image divisors
also contain \(\Gamma\); thus the image intersection is not being
asserted to have sole support \(\Delta\).

Writing \(m=a-3r\), \(n=b-3s\), the two normal forms on the ruled
quadric have bidegrees \((a-r,m),(b-s,n)\).
The resultant on the ruling parameter line is a section of degree
\[
 (a-r)n+(b-s)m=ab/4-rs
\]
by bihomogeneity and \(K=0\). Its divisor must be
\((ab/4-rs)[z]\), because it vanishes exactly at parameters where
the forms share a root. If one fiber degree is zero this means
the corresponding scalar section raised to the other fiber degree.
Both degrees cannot be zero on \(K=0\). The resultant does not exclude
a whole contracted ruling at the marked point; the separate nonzero
test there is essential. This extends the endpoint
\((3r,4s)\) correspondence to interior slopes without asserting
existence there.

It is enough to analyze irreducible equations on this boundary.
Every cross-pair of irreducible factors of a proper sole-support
pair is proper and has sole support by degree and containment.
Its \(K\) is nonpositive. The total \(K\) is the sum of these
values with factor multiplicities by bilinearity, so equality
forces equality for every cross-pair. For positive orders the
slope equation is \((7a/r-16)(7b/s-16)=60\), making all slopes on
one side equal and the opposite slope fixed. All cross-pairs
give the same section, because their strict intersections lie in
the original one. The [all-mate low-degree exclusions](../../frameworks/carrier-normalization/degree_exclusions.md#52-factors-and-the-degree-bound)
force both irreducible degrees to be at least five; at the endpoint
this requires \(r,s\ge2\).

### A conductor requirement on the endpoint carriers

Consider only the endpoint correspondence in which the actual pair
on \(V_5\) has sole support \(\Delta\), not the interior equality
case in which \(\Gamma\) remains in the image intersection.
Take an integral component \(U\in|mM|\) of either member, regular at
the generic point of \(\Delta\), with normalization smooth along its
inverse curve \(c\). The pullback of the proper mate is an ample
Cartier divisor supported precisely over \(\Delta\). Generic
regularity and finiteness give one inverse curve \(c\cong\Delta\)
and no other points in its full inverse (a Cartier divisor on the
normal surface has pure support). If the mate has degree \(n\)
on \(V_5\), its pullback has divisor \(mn c\) by intersection
with \(M\), since \(M^3=5\) and \(M\cdot\Delta=5\). Intersecting
with \(c\) gives \(c^2=5/m\). Smoothness along \(c\) makes this
an integer, so \(m=1\) or \(5\).

For \(m=1\), if the component has order \(j\) along \(\Gamma\),
its strict transform has class
\[
 mL-jQ'=(3m-2j)H-(m-j)E .
\]
It gives an original carrier of positive degree at most three
(the component is not \(\Sigma\)), contradicting the
[all-mate low-degree exclusions](../../frameworks/carrier-normalization/degree_exclusions.md).
For \(m=5\) the full Cartier conductor divisor \(B_{\rm cond}\)
on the normalization near \(c\) has
\[
 B_{\rm cond}\cdot c = 5m-8+5/m=18 .
\]
Indeed finite duality identifies its negative with the relative
canonical line bundle near the smooth inverse curve;
\(\omega_U=(m-2)M|_U\), and adjunction on \(c\cong\mathbf P^1\)
gives \(K\cdot c=-2-c^2\) on the normalization.

The transverse differential along the inverse curve is a nonzero map
\(\mathcal O_c(c)\to N_{\Delta/V_5}\). Across the transverse blowup
point \(z\), the normal bundle on \(V_5\) is an elementary positive
modification of \(N_{T/B}\) of length one: in local coordinates with
\(\Gamma=(x,y)\), \(\Delta=(t,y)\), use the blowup chart \(y=xv\).
On the normal directions the map is diagonal with entries \(1,x\),
so the cokernel has length one. The largest line degree of
\(N_{\Delta/V_5}\) is at most \(8-d\) from the splitting
\(\mathcal O(d)\oplus\mathcal O(7-d)\) on \(T\), where \(d=2\) for
endpoint directions and \(d=3\) for mixed directions.
Thus the common-zero orders \(h_p\) of the transverse differential
sum to at most \(8-d-c^2\), namely five or four respectively.

At smooth points of the full downstairs conductor, its inverse is
finite flat of rank two there. Indeed local duality over the
Gorenstein hypersurface identifies the finite quotient of the
normalization by the original ring with the dualizing module of
the downstairs conductor; over its smooth parameter ring this
has rank one. The conductor sequence then gives rank two for the
upstairs conductor algebra. The existing
[smooth-conductor contact estimate](../carriers/square_descent_and_singular_gluing.md#smooth-conductor-contact-is-bounded-by-the-actual-normal-differential)
applies: the actual mate descends, pulls back to a power of a
local equation of \(c\) up to a unit, and conductor contact
\(b_p\) is at most \(2h_p\) on these points. Hence the points over
the nonsmooth downstairs conductor must supply
\[
 \sum_{p\text{ over nonsmooth conductor}}(b_p-2h_p)
 \ \ge\ 8\text{ (endpoint direction), or }10\text{ (mixed direction)} .
\]
This is a requirement on a hypothetical endpoint carrier.
It is not an exclusion if the necessary nonsmooth contacts occur,
and does not apply to a carrier generically singular along the
marked curve or a normalization singular along its inverse.

## 5. General residuals acquire a second constructive description

For a general \((a,b)\) pair, \(a,b\ge4\), use the inherited multiplicity-one
theorem of §1. Then \(W\cong D\) and \(r=s=1\). The corresponding divisors
\(T_a,T_b\) on \(V\) have

\[
T_a\in |(a-2)M|,\quad\operatorname{ord}_\Gamma T_a=a-3,
\qquad
T_b\in |(b-2)M|,\quad\operatorname{ord}_\Gamma T_b=b-3.
\]

Their intersection has a conic-primary component of generic multiplicity
\((a-3)(b-3)\), and residual image \(D'=\phi(W)\) of degree

\[
\boxed{\deg_M D'=3ab-4a-4b+2.}\tag{9}
\]

The multiplicity is the product because the general normal forms along
\(\Gamma\) have no common projective root at its generic point. Equivalently,
subtract (9) from the total \(M\)-degree \(5(a-2)(b-2)\) and divide by the
conic degree two. The general transformed residual is smooth, and isomorphic
to \(D\), for the following reason. On \(Q'\cong Q\), restrictions of the
two strict equations are general sections of
\(\mathcal O_Q(a-1,a-3)\) and \(\mathcal O_Q(b-1,b-3)\); restriction is
surjective by the quadric sequence. Their common zeros are transverse and
finite. No two lie in the same contracted ruling for a general pair: at two
chosen distinct points of one ruling each equation imposes two independent
linear conditions, while the ruling and its two points vary in dimension
three. The four conditions exceed this dimension. At a transverse meeting
with \(Q'\), the blowdown restricted to \(W\) is an immersion in the standard
two-parameter blowup chart. These two facts exclude both identifications and
ramification. Hence \(\phi|_W\) is a closed immersion.

The reduced conic attachment divisor has length

\[
\operatorname{length}(D'\cap\Gamma)
=Q'\cdot W=2ab-4a-4b+6.\tag{10}
\]

This is attachment to **reduced** \(\Gamma\); it is not the attachment length
to the full conic-primary component when \((a-3)(b-3)>1\).

| Original bidegree | \(\deg D\) in \(\mathbf P^3\) | \(\deg_M D'\) on \(V\) | Generic conic multiplicity | Reduced conic attachments |
|---|---:|---:|---:|---:|
| \((4,4)\) | 12 | 18 | 1 | 6 |
| \((5,5)\) | 21 | 37 | 4 | 16 |
| \((5,6)\) | 26 | 48 | 6 | 22 |
| \((6,6)\) | 32 | 62 | 9 | 30 |

These are examples of one formula, not a proposed degree-by-degree agenda.
They show that the same smooth residual curve can be interpreted either as
linked to the quartic in \(\mathbf P^3\), or as linked to a multiple conic on
the quintic del Pezzo threefold. The full primary schemes and attachment
budgets in these two presentations differ.





## Supporting nef bounds, exact slack, and equality controls

Write delta=deg R=ab-4m and K=16(as+br)-7ab-28rs. For arbitrary actual proper pairs the balance below gives 5delta>=K, and delta>=K if no residual component lies on Q. No normality, integral-carrier or saturated-root assumption is imposed.

## 2. Exact slack identities and what makes the bounds strict

On \(B=\operatorname{Bl}_C\mathbf P^3\), put
\(H=\pi^*\mathcal O(1)\), exceptional \(E\), \(L=3H-E\), and
\(Q'=2H-E=L-H\). The second projection
\(\phi:B\to V_5\) contracts precisely the ruling fibers of \(Q'\).

Let \(W\) be the proper intersection of the two strict surfaces. Decompose
its actual effective cycle as

\[
[W]=Z_E+\widetilde R,
\qquad Z_E\subset E,
\]

where \(\widetilde R\) is the strict-transform cycle of the actual
residual. In the product description
\(E=\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm direction}\), write

\[
[Z_E]_E=u\alpha+n\beta,\qquad u,n\ge0,
\quad n=m-rs.
\]

Here \(u\) includes vertical fibers and the direction-degree contributions
of horizontal components. The restrictions
\(H|_E=4\alpha\), \(L|_E=5\alpha+\beta\) give

\[
L\cdot W=3ab-4(as+br)+2rs
=5(m-rs)+u+L\cdot\widetilde R.
\]

After using \(ab=4m+\delta\), this is the exact numerical identity

\[
\boxed{5\delta-K=4\bigl(u+L\cdot\widetilde R\bigr).}\tag{3}
\]

Nefness of \(L\) and effectiveness of \(Z_E\) recover the earlier (1).
Since \(L=H+Q'\), the same identity is

\[
\boxed{\delta-K=4\bigl(u+Q'\cdot\widetilde R\bigr).}\tag{4}
\]

If no residual component lies in \(Q\), the last intersection is
nonnegative, proving the earlier (2). These are equalities of intersection
numbers of specified actual cycles. They do not identify those cycles
with the common zero scheme of the two leading symbols.

In particular equality in (1) holds precisely when \(u=0\) and every
residual component has \(L\)-degree zero. Since \(L\) is pulled back from
an ample bundle on \(V_5\), such components are exactly the curves contracted
by \(\phi\): the trisecant ruling lines on \(Q\), with their actual
multiplicities. Equality in (2), under its no-quadric-component hypothesis,
requires \(u=0\) and \(Q'\cdot\widetilde R=0\). The first statement is
about intersection-cycle geometry; neither equality is an assertion that
every allowable numerical tuple is attained.

For the mixed form, decompose \(R=R_{\rm out}+R_Q\), let
\(\delta_{\rm out}=\deg R_{\rm out}\), and write
\([R_Q]_Q=x\alpha_Q+y\beta_Q\), with \(C\) of type \((1,3)\).
Then \(Q'\cdot\widetilde R_Q=y-x\), so (4) gives the previously known

\[
\boxed{\delta_{\rm out}+5x-3y\ge K.}\tag{5}
\]

The ruling with length-three attachment to \(C\) is precisely what weakens
the universal coefficient from one to five. This is a useful geometric
reason to record residual components rather than just their total degree.

## Nef cone and the limit of first-graph positivity

The real Picard space of \(B\) has basis \(H,L\). Both classes are nef.
A fiber of \(\pi\) has \((H,L)\)-degrees \((0,1)\), while a contracted
ruling of \(\phi\) has degrees \((1,0)\). Thus a nef divisor
\(xH+yL\) must have \(x,y\ge0\), and conversely these inequalities
are sufficient. Consequently

\[
\boxed{\operatorname{Nef}(B)
=\mathbf R_{\ge0}H+\mathbf R_{\ge0}L.}\tag{6}
\]

On the exceptional effective cycle, \(H\)-positivity gives just
\(\delta\ge0\); \(L\)-positivity gives (1). Every other nef divisor on
this first graph gives a nonnegative linear combination of these two
inequalities. Therefore changing to the \(V_5\) presentation does not,
by itself, produce a stronger uniform linear nef bound. Its anticanonical
surface \(\Sigma\) pulls back as \(E+3Q'\sim2L\), so simply intersecting
its class supplies no new nef direction either. Its conductor and marked
curve geometry may matter with additional hypotheses, but not as an
automatic extra positivity assumption.

The inherited moving-root refinement makes the additional data explicit.
Suppose every common horizontal root curve in \(E\) has slope at least
\(\rho\ge0\), meaning direction-degree divided by degree over \(C\)
is at least \(\rho\). Then \(u\ge\rho(m-rs)\). Equations (3)–(4) give

\[
\boxed{
(5+\rho)\delta\ge K+\rho(ab-4rs),
}\tag{7}
\]

and, if there is no residual component on \(Q\),

\[
\boxed{
(1+\rho)\delta\ge K+\rho(ab-4rs).
}\tag{8}
\]

These are rearrangements of the support-sensitive inequality already in
October 19 §2a. They become stronger only when a lower slope has actually
been established for the horizontal support of the actual pair. A moving
first-relation label alone is not that hypothesis. If no horizontal
exceptional cycle occurs, \(m=rs\) already gives the exact residual degree
\(ab-4rs\).

## 4. Uniform actual-pair equality controls

Both coefficients can be attained by actual global constructions. These
controls test the stated generality; they do not construct a sole-support
endpoint or show that every extremal numerical tuple exists.

**Universal coefficient five.** Take

\[
F=q^r,\qquad G=P_s(c_0,\ldots,c_6),
\]

where the \(c_i\) are the seven known cubics and \(P_s\) is a general
degree-\(s\) polynomial section on \(V_5\). The pair has degrees
\(a=2r,b=3s\), exact normal orders \(r,s\), and is proper since
\(q\nmid G\). On \(Q\), after removing \(sC\), its remaining divisor
is of type \((2s,0)\): these are \(2s\) general trisecant ruling fibers.
At \(\eta_C\), the quadric normal direction and the other normal form
are coprime, so \(m=rs\). Consequently

\[
R=r\,(\text{the }2s\text{ ruling fibers}),\quad
\delta=2rs,\quad K=10rs,
\]

and \(5\delta=K\). This is compatible with, and extends by powers, the
earlier smooth-quadric sharpness control. One carrier is allowed to be a
power of the quadric; an integral-carrier restriction would change the scope.

**No-quadric-component coefficient one.** Take general sections
\(P_r\in H^0(V_5,\mathcal O(r))\),
\(P_s'\in H^0(V_5,\mathcal O(s))\) and put

\[
F=P_r(c_0,\ldots,c_6),\qquad G=P_s'(c_0,\ldots,c_6).
\]

Their zero divisors have no common point on \(\Gamma\) for a general
choice: choose the first restriction's finite zero set and choose the
second restriction nonzero at those points. The complete-intersection
curve on smooth \(V_5\) is smooth integral by Bertini. Its pullback \(W\)
therefore avoids \(Q'\). It has no curve component in \(E\), because the
two general divisors intersect the fixed surface \(\Sigma\) properly in
finitely many points. Thus \(m=rs\). The actual pair has

\[
a=3r,\quad b=3s,\quad
\delta=ab-4rs=5rs,\quad K=5rs,
\]

so equality holds in (2), with no residual component on \(Q\).
This also follows from \(W\sim rsL^2\), \(L^3=5\), and
\(Q'\cdot L^2=0\). No small-degree STCI problem has been reopened.

## 5. Integer strengthening, usefulness region, and exact limitations

Because \(\delta=ab-4m\), a valid lower bound must be combined with

\[
\delta\ge0,\qquad \delta\equiv ab\pmod4,
\qquad \delta\le ab-4rs.
\tag{9}
\]

For (1), take the smallest nonnegative integer congruent to \(ab\)
modulo four and at least \(\lceil K/5\rceil\). For (2), use \(K\)
instead. If that lower bound exceeds the last upper bound, the specified
normal-order data cannot occur under the stated residual-location
hypotheses. If \(ab\) is not divisible by four, a positive minimum can
come from arithmetic alone rather than from a new geometric restriction.

| Actual degree/order data | Universal graph bound after congruence | Bound if no component of \(R\) lies on \(Q\) |
|---|---:|---:|
| \(a=b=4,r=s=1\) | 0 | 0 |
| \(a=b=5,r=s=1\) | 1 (arithmetic only) | 1 (arithmetic only) |
| \(a=b=6,r=s=2\) | 4 | 20 |
| \(a=6,b=9,r=2,s=3\) | 6 | 30 |
| \(a=b=8,r=s=2\) | 0 | 0 |

For example, the \((6,6)\) statement with exact orders \((2,2)\) really
does force residual degree at least four universally, and at least twenty
when residual components avoid the quadric. The latter value is attained
by the cubic-generated construction. These are specified-order claims,
not claims about all sextic pairs, whose exact orders can be different.

If neither equation has a quadric factor, restriction to \(Q\) gives
\(a/r\ge3,b/s\ge3\). Put \(\alpha=a/r,\beta=b/s\). Then

\[
\frac K{rs}=16(\alpha+\beta)-7\alpha\beta-28,
\qquad
7\frac K{rs}=60-(7\alpha-16)(7\beta-16).
\]

Thus the unsloped bound is geometrically positive only in the region
\((7\alpha-16)(7\beta-16)<60\); in particular both ratios must be less
than four. For low normal orders in sufficiently high degree it becomes
\(\delta\ge0\), apart from the congruence. The same equations then leave
the unrestricted endpoint unresolved. They must not be presented as a
uniform positive residual bound in characteristic zero.



## 7. Computable order-one corollary: the first-normal gcd supplies the slope

There is a useful explicit application of the **already reviewed**
October 19 common-root-slope inequality. It is not an independent new
normal-carrier mechanism. Suppose \(F_a\) has exact generic order one
along \(C\), while \(G_b\) has exact order \(s\). Write its nonzero first
normal symbol, using the accepted balanced conormal splitting, as a pair
of binary forms

\[
f=(f_0,f_1),\qquad \deg f_i=4a-7.
\]

Let \(d_F\) be the degree of their common zero divisor. Dividing that
common factor leaves a basepoint-free pair of degree

\[
h=4a-7-d_F\ge0.
\]

Consequently the only horizontal component of the zero divisor of \(f\)
on \(E\) is the graph of a degree-\(h\) map between the two projective
lines. The remaining zero divisor consists of the vertical fibers over
the first-normal gcd. Every horizontal exceptional component of the
actual strict-pair intersection must therefore be this graph. Its
intersection multiplicity is retained in \(m-s\), rather than read off
from the first symbols. In the notation of §2,

\[
u\ge h(m-s).
\]

If the graph is not common to the second symbol, there is no horizontal
exceptional component and \(m=s\); the displayed inequality is then
vacuous and remains valid. Thus no unspoken common-root or
\(m>s\) assumption is needed for the following corollary.

Substituting \(r=1,\rho=h\) into (7), with
\(K=16(as+b)-7ab-28s\), gives

\[
\boxed{
\deg R\ge
\frac{b(4a^2-14a+16-a d_F)+4s d_F}
     {4a-2-d_F}.}\tag{10}
\]

Indeed the numerator before substitution is

\[
K+h(ab-4s)
=b\bigl((h-7)a+16\bigr)
 +s(16a-28-4h),
\]

and the two brackets become \(4a^2-14a+16-ad_F\) and \(4d_F\).
The denominator is \(h+5\ge5\). If no component of \(R\) lies on \(Q\),
(8) gives the same numerator with the stronger denominator

\[
\boxed{4a-6-d_F=h+1\ge1.}\tag{11}
\]

As throughout, negative numerical right sides add no lower bound beyond
effectivity; positive values should be strengthened by the congruence in
(9). These are inequalities for the genuine residual of an actual proper
pair. They are available without a normality or Q-Cartier hypothesis on
the degree-\(a\) carrier. Integrality may be imposed for comparison with
the carrier formulas below, but is not needed in this graph argument.

For a carrier regular generically along \(C\), the first-normal gcd gives
\(\deg N_{C/S}=14-4a+d_F\). Replacing a numerical self-intersection by
that upper bound in the normal-sheaf capacity argument gives only the
first term of the numerator in (10). The extra nonnegative term
\(4s d_F\) is already supplied by the inherited moving-root graph
inequality, so the weaker gcd-only capacity bound must not be presented
as a new independent mechanism. An exact Mumford self-intersection can
nevertheless be smaller than \(\deg N_{C/S}\); its sharper quantitative
bound can then improve on (10). Which comparison wins depends on the
actual marked carrier geometry and the mate order.

This corollary makes one part of the needed slope data directly
computable from actual homogeneous coefficients. It neither supplies an
automatic positive numerator for all carriers nor replaces the remaining
higher-normal and full-primary geometry.

## Uniform remaining contact after the first blowup

This is a corollary of (1), not a new independent inequality. Keep the
arbitrary actual-pair hypotheses of §1, and set

\[
p=\frac{rs}{ab},\qquad \theta=\frac{\delta}{ab}.
\]

The local intersection formula gives \(rs\le m\), hence
\(p\le(1-\theta)/4\). AM–GM in (1) gives the degree-independent
necessary condition

\[
\boxed{5\theta\ge32\sqrt p-7-28p.}\tag{12}
\]

The original K bound retains the asymmetry of as and br and is at least
as strong. A positive right side of (12) forces a positive residual
fraction for that actual pair; nonpositive values give no such conclusion.

If the pair is an STCI, then \(\theta=0\), \(m=ab/4\), and
\(0\le\sqrt p\le1/2\). The inequality
\(32\sqrt p-7-28p\le0\) consequently forces
\(\sqrt p\le(8-\sqrt{15})/14\); its other root exceeds 1/2. Thus

\[
\boxed{
\frac{rs}{m}\le\frac{79-16\sqrt{15}}{49},\qquad
\frac{m-rs}{m}\ge\frac{16\sqrt{15}-30}{49}
\simeq0.6524027.
}\tag{13}
\]

Here \(m-rs=n\) is the degree over C of the actual horizontal
exceptional intersection cycle from §2. It measures the generic contact
remaining after the first blowup, including its scheme multiplicities.
It is not the degree of R or the number of distinct normal directions.
Consequently every hypothetical supported pair must concentrate over
65.2 percent of its generic intersection multiplicity in this remaining
contact. Coprime generic leading symbols cannot supply such a pair.
The conclusion is uniform in both degrees and imposes no normality,
integrality, saturation or ordinary-initial-CI assumption.

The reciprocal constant \((79+16\sqrt{15})/49\) already occurs in
the [October 19 filtration investigation, §4](../../frameworks/formal-normal-geometry/normal_filtration_boundaries.md)
and [October 20 report](../../frameworks/formal-normal-geometry/normal_filtration_boundaries.md).
There it bounds a ratio of relation orders under additional saturated
generic-CI hypotheses. Those relation orders must not be identified with
the chosen-equation orders here. No novelty claim is made for the
constant. The useful extraction is the all-pair geometric interpretation
and its asymptotic search consequence.

**Existence and nonexistence:** a construction must create this much
remaining contact and still realize two global equations with no residual
support. For nonexistence, (13) supplies no upper bound contradicting that
requirement. Repeating first-blowup nef calculations cannot improve it
without new data, by §3. A further direction needs a mechanism controlling
actual higher contact, its movement and attachment, or constructing it
globally; a list of local contact types alone does not do so.



## Characteristic reach and limitation

The actual-cycle pushforward and exceptional-support criterion use regular-local blowup intersection and purity in any characteristic. The \(V_5\) model and finite normalization of \(\Sigma\) retain their **characteristic-zero** scope. The first-blowup inequality \(5\delta\ge K\) and slope refinement use global generation of \(I_C(3)\) and balanced normal bundle, so extend to characteristic \(\ne2\) without the \(V_5\) contraction. In characteristic two \(N_C=\mathcal O(8)\oplus\mathcal O(6)\); the product/slope constants do not carry over. [Positive-characteristic quartic-carrier STCI](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) is compatible with this necessary inequality.

## Lefschetz compression on ample strict carriers

**Scope and status.** This is a new application of established Lefschetz
and Kummer theory to the actual first graph, pending independent review.
It applies in characteristic zero, also to entirely-thick original pairs.
The equality case below uses the connected-direction and second-blowup
bounds of [R-0077](../../results/connected_normal_directions.md), whose
independent review is pending. It does not assume a normal original carrier.

**Lefschetz input.** For an integral ample Cartier surface \(S\) in a
smooth projective threefold \(B\), the restriction of \(\operatorname{Pic}(B)\)
has saturated image in \(\operatorname{Pic}(S)\) if \(\operatorname{Pic}(B)\)
is torsion-free (over an algebraically closed characteristic-zero field).
More precisely, if \(rM=A|_S\) with \(A\in\operatorname{Pic}(B)\),
then \(A=rA_0\) in \(\operatorname{Pic}(B)\) and \(M=A_0|_S\).
Indeed [Cotner–Zavyalov, Theorem 3.2.2](https://www.cambridge.org/core/journals/compositio-mathematica/article/lefschetz-theorems-in-flat-cohomology-and-applications/8556201EDB51D7F2F76F5950A800CD64)
applied to \(\mu_{\ell^j}\), with affine complement to the ample divisor,
gives an isomorphism in \(H^1\) and injectivity in \(H^2\).
The Kummer sequence, since both schemes have global units \(k^*\),
gives \(\operatorname{Pic}(S)[\ell^j]=0\) and injectivity of
\(\operatorname{Pic}(B)/\ell^j\to\operatorname{Pic}(S)/\ell^j\).
Prime-power decomposition gives the assertion for \(r\).
This is the existing ample-divisor Lefschetz theorem, not a new
Noether–Lefschetz assertion that every class on \(S\) is ambient.
Normality of \(S\) is not needed.

**Application (LC1).** Retain the actual proper sole-support pair with
orders \(p,q>0\) and degrees \(a\ge3p,\ b>3q\), and suppose its first
strict intersection \(W\) has sole reduced support a smooth integral
curve \(T\subset E\). Write \(c=m-pq\) if \(T\) is a section over \(C\);
more generally let \(c\) be the actual generic length along \(T\).
Assume the strict degree-\(b\) carrier \(S\) is integral and regular at
the generic point of \(T\). Set \(A=aH-pE\).
The divisor \(S\sim bH-qE=(b-3q)H+qL\) is ample: the maps of the two
basepoint-free classes \(H,L\) have no common contracted curve, so the
map to their product is finite. The blowup formula gives
\(\operatorname{Pic}(B)=\mathbb ZH\oplus\mathbb ZE\).

Let \(R\) be the lcm of the actual local indices of \(T\) on \(S\)
in the almost-Cartier sense. The effective Cartier divisor \(W=cT\)
gives \(R\mid c\); the generically regular \(S_2\) extension argument
of [AC1–AC3](../carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices)
gives the effective Cartier divisor \(RT\) on \(S\).
Putting \(k=c/R\), the equality \(k[RT]=A|_S\) and the Lefschetz input give
\[
 \boxed{k\mid\gcd(a,p),\qquad
 RT\sim (a/k)H-(p/k)E\ \text{ on }S.} \tag{LC1}
\]
The index is on the strict carrier, not the normalization or the original
carrier in \(\mathbf P^3\).

**Actual lift (LC2).** Write \(a'=a/k,p'=p/k\). If
\(p'\le q\) and \(a'-3p'\le b-3q\), restriction of
\(\mathcal O_B(a'H-p'E)\) to \(S\) is surjective on global sections.
By Serre duality the required vanishing of
\(H^1(B,\mathcal O_B(a'H-p'E-S))\) is equivalent to vanishing of
\[
 H^2(B,\mathcal O_B((b-a'-4)H+(1+p'-q)E)).
\]
For \(p'<q\), use the
[graph vanishing in R-0077](../../results/connected_normal_directions.md#connectedness-and-residual-attachment),
\(H^i(B,jH-nE)=0\) for \(i>0,n\ge0,j\ge3n-1\), with
\(n=q-p'-1,\ j=b-a'-4\).
For \(p'=q\), restriction to \(E\) of the extra \(E\)-twist has
fiber degree \(-1\) and is acyclic, reducing to \(H^2(\mathbf P^3,\mathcal
O(b-a'-4))=0\). Lift the canonical section of \(RT\) to \(B\); the
blowup section dictionary supplies an actual degree-\(a'\) form in
\(H^0(\mathbf P^3,I_C^{p'}(a'))\). Its intersection with the original
degree-\(b\) carrier has reduced support exactly \(C\): off \(E\) the
strict carrier has no intersection with the lifted section, and the new
form vanishes along all of \(C\). It is a proper intersection since
its restriction to \(S\) is nonzero. The lift need not preserve the
original nonreduced ideal or have exact order \(p'\) in general.
Thus for a minimum actual mate, or an absolute minimum degree-product
pair, these lifting inequalities force \(R=c\). On the edge
\((a,b)=(3p,4q)\), \(p\le q\), they always hold and \(c=2pq\) for a
constant section. For \(p=1\), (LC1) already gives \(R=c\).

**Normal replacement on the graph (LC3).** If the strict pair has
generic embedding dimension at most one along its smooth sole-support
curve, and \(bH-qE-A\) is globally generated, a general member of
\[
 \{\lambda G'+F'J:J\in H^0(B,\mathcal O_B(bH-qE-A))\}
\]
is smooth off \(T\) by characteristic-zero Bertini and regular at its
generic point by the first-symbol test. It is \(S_2\) as a hypersurface
and hence normal; connectedness of an ample divisor gives integrality.
Choose \(\lambda\ne0\) and avoid the proper linear condition of
containing \(E\), so the ideal on \(B\) is preserved and this member is
the strict transform of an actual degree-\(b\), order-\(q\) equation.
This is the same generator-replacement argument as NR1, now on \(B\).
On the edge with \(p\le q\), the difference is \(qH+(q-p)L\) and is
globally generated. The replacement is normal on the graph even if
both original equations are generically thick along \(C\).

**Application to the first entirely-thick numerical pair.** Suppose
\((a,b;p,q)=(6,8;2,2)\) is an actual sole-support pair. By R-0077 its
first strict intersection is supported on one constant section with
\(c=8\). Let \(r,s\) be the actual generic orders on that section of
the strict sextic and octic. They lie in \(\{1,2\}\), since each
order is bounded by the multiplicity of the corresponding normal root.
The second-blowup inequality of
[R-0077](../../results/connected_normal_directions.md#bounding-the-orders-after-blowing-up-the-section)
gives
\[
 10s+18r\le(7-d)8+d\,rs,\qquad d\in\{2,3\}.
\]
For \(r=2,s=1\) it fails (46 exceeds 44 or 38), and for \(r=s=2\)
it fails (56 exceeds 48 or 44). Hence \(r=1\).
By LC3 a general strict octic is normal and preserves the strict
pair, since the difference is \(2H\). The original ambient pair is
also preserved by this replacement. By LC1 the marked section on that
strict octic has \(R\mid8\) and \(8/R\mid\gcd(6,2)=2\), so \(R=4\)
or \(8\). If \(R=4\), LC2 produces a degree-three ambient mate for
the replaced octic, contrary to the low-degree carrier exclusion
([R-0001](../../results/quartic_carrier_exclusion.md) and the degree
\(\le3\) exclusions). Thus
\[
 \boxed{R=8,\quad\text{and some point of }T\text{ has actual local index }8.}
 \tag{LC4}
\]
The last statement follows because every local index divides eight.
This is not an exclusion of \((6,8)\). It changes its remaining
entirely-thick problem to a generically curvilinear CI on the first
graph, with a forced maximal local Cartier index on an ample normal
strict carrier. Normality of the original octic in \(\mathbf P^3\)
does not follow. Local symbolic-power and socle arguments can now
be studied on the marked section with its actual conormal bundle,
rather than assumed on the original \(C\).


## Socle defects on the two presentations of the first graph

**Status:** new synthesis, pending independent review, using the
existing R-0077 equality and second-blowup results and the actual
marked correspondence above. The local filtration comparisons are
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
curvilinear. This finite list concerns **global
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

### A K3 marked-lattice obstruction to the primitive graph row

The image in \(V_5\) changes the useful singularity budget.
A degree-two Cartier divisor there is anticanonical, so
its smooth deformation is a K3 surface, rather than the
large-degree hypersurface occurring in the original
projective space.

**New conditional exclusion (pending independent review).**
Suppose an actual characteristic-zero \((6,8;2,2)\)
sole-support pair lies in the primitive row of SC1
(mixed direction, \(\ell=3\)). Then its degree-two image
carrier \(U=(P=0)\subset V_5\) must have a singularity
along \(\Delta\) worse than Du Val.
This conclusion does not assume global normality of \(U\)
or any restrictions on singularities away from the marked
quintic. It excludes the whole primitive graph row with
only smooth or Du Val marked points on the smaller image
carrier, not the two nonprimitive graph rows.

**Proof.** The actual original sextic is integral, by
the independent low-degree factor exclusion (each factor
would have degree at least five), hence its image carrier
is integral. Assume \(U\) is normal and smooth or Du Val
in a neighborhood of \(\Delta\), as it would be under
the hypothesis to be contradicted.
The SC3--SC4 comparison gives an image CI \(Z\) of
multiplicity \(8\) with first free conormal slope \(4\)
and full top defect \(6[z]\).
The ambient normal bundle degree on the quintic is
\(\deg N_{\Delta/V_5}=8\), by adjunction and
\(K_{V_5}=-2M\). The scalar first-symbol divisor of
\(U\) on \(\Delta\) has degree \(2M\cdot\Delta-8+4=6\).
It is denoted \(A\), retaining every on-curve singular
point with its multiplicity. The image CI is primitive
at every point other than \(z\). By the actual
power--socle formula on a smooth threefold, every
singular point of \(U\) on \(\Delta\setminus\{z\}\)
has local Cartier index \(8\). At the marked point,
write \(r\) for the actual local index and \(a_z\) for
the first-symbol order. Smoothness is impossible there
because the CI is nonprimitive. Thus \(r\in\{2,4,8\}\)
and
\[
 6=(8/r-1)a_z+(8/r)D_{r,z},\qquad
  \sum_{P\in\Delta}a_P=6.
\]
In particular \(a_z=2\) if \(r=2\), and \(a_z\) is
positive even if \(r=4\).

On the normalization of \(U\) the actual mate gives
\(8\Delta\sim4M\) with \(M^2=10\) and \(M\Delta=5\).
There is no extra inverse branch, since the normalization
is an isomorphism along \(\Delta\). Hodge equality, or
intersection with the actual Cartier multiple, gives
\(\Delta_{\rm num}^2=5/2\).
On a resolution that is minimal above its marked ADE
points, the smooth strict transform of \(\Delta\) has
square \(-2\): its canonical intersection is zero
because \(\omega_U\cong\mathcal O_U\) and the resolution
is crepant near \(\Delta\), and all other exceptional
curves are disjoint from it.
Consequently the total local numerical-pullback
correction is
\[
 \sum_{P\in\Delta}\gamma_P=9/2 .                         \tag{SC5}
\]
Here \(\gamma_P=-R_P^2\) where \(R_P\) is the exceptional
part of the Mumford numerical pullback over \(P\).
The actual order of the class of \(\Delta\) at \(P\)
is the order of \(R_P\) modulo the integral ADE lattice.
Thus if the order is \(2\), then
\(\gamma_P\in\frac12\mathbb Z\), since the exceptional
lattice is even.

We can use the rank bound 19 for the sum of the
marked ADE lattices even if \(U\) has worse
singularities elsewhere. Indeed a general pencil in the
basepoint-free \(|2M|\) smooths \(U\) to a smooth
anticanonical K3 surface (adjunction, Kodaira vanishing
and Bertini). Choose the second pencil section nonzero
at the finitely many marked ADE points. In disjoint
small Milnor neighborhoods these induced smoothings
carry the negative definite ADE vanishing lattices
(the classical Milnor lattice of a simple surface
singularity, equivalently Brieskorn's simultaneous
resolution). Their intersection pairing in the global
smooth fiber is the orthogonal sum of the local
pairings. Nondegeneracy gives injectivity on the span
in homology. The K3 intersection form has signature
\((3,19)\), so their total rank is at most 19.
This smoothing proof uses only the local isolated ADE
germs at the chosen points, not simultaneous resolution
of any non-ADE singularities elsewhere. Over any
algebraically closed characteristic-zero field the
finite carrier, curve and local-type data descend to a
complex model. For classical ADE and K3 lattice inputs,
see [Shimada, *On normal K3 surfaces*](https://www.math.sci.hiroshima-u.ac.jp/shimada/preprints/normalK3/normalK3.pdf)
and the classical Brieskorn lattice theorem as recalled in
[Frenkel--Givental--Milanov, §3.3](https://math.berkeley.edu/~giventh/papers/fgm-ade.pdf)
(the local simple-singularity/vanishing-lattice theorem
is the input, not a new classification).

For local index eight, only \(A_{N-1}\) is possible
(the D and E discriminant groups have exponent at
most four). For a smooth marked branch of type
\(A_{N-1}^j\), the standard chain formulas give
\[
 r_P=N/\gcd(N,j),\quad
 a_P=\min(j,N-j),\quad
 \gamma_P=j(N-j)/N .
\]
The smooth-branch contact formula is the one in
[Ellia, Definition 8 and Lemmas 9--10](https://arxiv.org/abs/1409.3801);
the index and square are also immediate from the
inverse chain matrix. In particular for index eight
write \(N=8g\). Then
\[
 (a_P,\gamma_P)=(g,7g/8)\quad\hbox{or}\quad(3g,15g/8).
\]
Its rank \(8g-1\) is at least \(7g\). Thus if
\(G=\sum_{r_P=8}g_P\), the rank budget gives \(G\le2\).

* If \(r=8\) at \(z\), all marked singularities have
  index eight. Their total correction is at most
  \(15G/8\le15/4<9/2\), contradicting SC5.
* If \(r=2\), \(a_z=2\). The other contacts sum to
  four; by \(G\le2\) this is only two \(A_7\) points
  with contacts one and three. They contribute
  \(11/4\) to SC5, requiring \(\gamma_z=7/4\),
  impossible for index two on an even lattice.
* Suppose \(r=4\). If \(a_z=6\) there are no other
  marked singularities, and \(\gamma_z=9/2\).
  An A-type index-four smooth marked branch has
  \(N=4g,\ a_z=g,\ \gamma_z=3g/4\), requiring
  \(N=24\) and rank 23. A D-type index-four class
  occurs only in odd \(D_n\); its discriminant
  square correction is \(n/4\bmod 2\), an odd
  quarter, not \(9/2\bmod2\). The E groups have
  no elements of order four.
  If instead \(a_z=2\) or \(4\), the other contacts
  sum to four or two. Their parity and \(G\le2\)
  force \(G=2\), contributing respectively \(11/4\)
  or \(7/4\). The required correction at \(z\)
  is respectively \(7/4\) or \(11/4\).
  The other ADE ranks total at least 14, leaving
  rank at most five at \(z\). An A-type index-four
  point of rank at most five must be \(A_3\) and
  has contact one, not the required even value.
  The only D-type possibility is \(D_5\), whose
  order-four class has correction \(5/4\bmod2\).
  Neither required correction has that residue.
  This exhausts the remaining case.

For the D-type discriminant formula, use the positive
root lattice \(D_n=\{x\in\mathbb Z^n:\sum x_i\ \text{even}\}\)
with the Euclidean form. For odd \(n\) the two order-four
cosets are represented by the half-integral spinor
vectors with all entries of absolute value \(1/2\);
their squared norm is \(n/4\bmod2\). Negating the
exceptional lattice and then taking the correction
\(-R_P^2\) gives exactly the sign used above.
This last check does not require identifying a
particular D-type marked branch with an end of its
resolution diagram.

All possible indices at \(z\) contradict the
marked ADE assumption. \(\square\)

This illustrates an important general improvement:
the use of the smoothing's negative rank and the
actual local discriminant square can be combined with
a *punctual* socle transfer, rather than merely with
a genus or global singularity count. The K3 rank here
is a property of the ambient Fano-side linear system,
not an accidental bound on a particular sextic.
The marked point still may be worse than Du Val;
nothing here proves normality along it, or excludes
all possible primitive graph lifts.

## Relation to actual normalized carrier branches

The [valuation dictionary and Hodge-gap decomposition](../carriers/numerical_surface_pullback.md#branch-valuations-and-the-actual-first-blowup) refine the first-graph cycle by choosing one integral carrier and a resolution dominating its finite normalization and the first graph. An actual strict mate pulls back to `div(G)-qD`, with D the principalized marked ideal. Thus each horizontal component coefficient is the pushforward of `n_i-qe_i`; the exceptional coefficients record the full vertical cycle and give further inequalities. The scalar graph equality (3) is recovered by summing these coefficients against direction degree and is not independent of that sum. The additional information is the fixed-carrier Hodge matrix, the decomposition of the marked-ideal square gap, and, for two inverse branches, the resulting necessary matrix. This does **not** identify normalized carrier branches with the Rees valuations of the full CI ideal in the next section. Independent review of the new refinement is pending.

## The normalized blowup of the full complete intersection

This is a different blowup from the blowup of the reduced quartic
support used above. Its center is the actual CI ideal. The following
component identity works in every characteristic and allows residual
components, nonreduced components and singular reduced supports.

Let \(Y=V(F_a,G_b)\subset\mathbf P^3\) be any proper complete
intersection over an algebraically closed field, and write
\[
[Y]=\sum_j m_j[C_j]
\]
for its irreducible reduced components and generic lengths. Put
\(B=\operatorname{Bl}_Y\mathbf P^3\), with exceptional Cartier
divisor \(E_Y\), and let \(\nu:\overline B\to B\) be its normalization.
This normalization is finite because B is of finite type over a field.
Write
\[
\nu^*E_Y=\sum_i\rho_iD_i,\qquad \rho_i>0.
\]
Every \(D_i\) maps onto an irreducible component \(E_{Y,j}\) of \((E_Y)_{\rm red}\).
Its center in P3 is C_j, never an isolated point. If
\(f_i=[k(D_i):k(E_{Y,j})]\) for this finite map, then
\[
\boxed{\quad
\sum_{i:\,\nu(D_i)=E_{Y,j}}\rho_i f_i=m_j
\quad\text{for every }j.
\quad}                                                     \tag{14}
\]
The degrees include any inseparable part.

**Proof.** The regular immersion gives
\[
E_Y=\operatorname{Proj}_Y\operatorname{Sym}(\mathcal I_Y/\mathcal I_Y^2).
\]
Thus \(E_Y\) is a projective-line bundle over the full nonreduced Y.
Each \(E_{Y,j}\) is the corresponding projective-line bundle over C_j,
and its coefficient in \([E_Y]\) is \(m_j\). Locally this is just
preservation of the generic Artinian length after a purely
transcendental residue-field extension. No smoothness of C_j
is needed. A finite morphism preserves the dimension of each
closed integral subvariety, so a divisor D_i cannot map into
a fiber or a point of \(E_Y\). Finally the projection formula for
the exceptional Cartier divisor and the finite birational
normalization gives
\[
\nu_*[\nu^*E_Y]=[E_Y].
\]
Comparing coefficients proves (14). The regular-embedding
description is recalled in [Aluffi, §2.2](https://www.math.fsu.edu/~aluffi/archive/paper569.old.pdf).
The same proof applies to an lci curve in any smooth
threefold of finite type over a field. \(\square\)

Consequently,
\[
\sum_i\rho_i f_i\deg C_{j(i)}=ab.                         \tag{15}
\]
For a distinguished component C0, the genuine residual degree is
\[
\deg R=\sum_{j(i)\ne C_0}\rho_i f_i\deg C_{j(i)}.
\tag{16}
\]
These are the existing component degrees expressed on the
normalized blowup, not new lower bounds. Further log resolutions
can introduce divisors centered at points. Equation (14) does
not forbid those valuations or remove punctual defects; it
distinguishes them from the divisors of this normalized blowup
and from residual components downstairs.

### The exceptional-coefficient positivity bound

Over \(\mathbf C\), [Ein–Lazarsfeld, Proposition 3.1](https://arxiv.org/pdf/math/9810004)
applies to an ideal J with \(J\otimes L\) globally generated and
L nef on a smooth projective variety. In dimension three it gives
\(\sum_i\rho_i\deg_L C_{j(i)}\le L^3\), retaining repeated centers.
For \(J=\mathcal I_Y\), \(a\le b\), take \(L=\mathcal O(b)\).
The stronger elementary inequality is already
\[
\sum_i\rho_i\deg_L C_{j(i)}
\le b\sum_i\rho_i f_i\deg C_{j(i)}
=ab^2\le b^3.                                           \tag{17}
\]
Thus the redundancy holds for every proper pair, before imposing
sole support. In the STCI case (14) reads
\(\sum_i\rho_i f_i=ab/4\); the published bound only gives
\(\sum_i\rho_i\le b^2/4\).

Their Remark 3.2 subtracts the number \(n_{\rm out}\) of common points
outside Y of three general sections of \(\mathcal I_Y(b)\).
Here \(n_{\rm out}=b(b-a)^2\). For b>a, write these sections as
\(A_\ell F+\lambda_\ell G\); eliminating G twice gives two
general degree-(b-a) equations, and the remaining equation
has degree b. Their complete intersection avoids Y and has
the displayed degree. For a=b the section space is a pencil,
so \(n_{\rm out}=0\). The improved right side is therefore
\[
b^3-n_{\rm out}=ab(2b-a)\ge ab^2,
\]
still weaker than (17). This \(n_{\rm out}\) counts a different three-section intersection;
it is neither the original residual R nor the generic transverse
Milnor number in the [pencil identity](../carriers/pencil_milnor_budget.md).

Geometrically, normalization distributes each full CI component's
transverse length among exceptional multiplicities and finite
covering degrees. The checked positivity theorem bounds a sum
that is already controlled by that distribution. It supplies
neither an upper limit on later contact nor a positive residual
degree, and does not strengthen the surviving-contact estimate
above. No valuation-tree classification follows.
