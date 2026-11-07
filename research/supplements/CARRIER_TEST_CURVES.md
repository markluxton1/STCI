# Test curves, normalization attachments, and restrictions on actual carriers

Fix \(C=C_0=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field; the ordinary full-source theorems use characteristic zero, while the weighted-subalgebra theorem below explicitly allows every odd characteristic. Throughout, a mate means an actual homogeneous form of positive degree with sole reduced intersection support \(C\). The arguments compare the divisor of its pullback with restrictions to actual projective curves. A curve on the exceptional divisor alone is not a test curve downstairs.

The weighted-subalgebra and critical-degree arguments have inherited independent review. The all-degree residual-curve extension below has a full proof and exact hypotheses. Its historical source review covered the critical-degree case; the present independent consolidation review also reconstructed the all-degree elimination, actual open-locus construction and slope refinement. These are not unrestricted STCI theorems.

## The reusable degree mechanism

Let \(\nu:S\to X\subset\mathbf P^3\) be the finite normalization of an integral surface of degree \(a\), and write \(H=\nu^*\mathcal O_X(1)\). Suppose the divisorial inverse image of a fixed integral curve \(C\) of degree \(d\) consists of curves \(\Gamma_1,\ldots,\Gamma_l\) of generic degrees \(e_i\) over \(C\). Let \(T_j\subset X\) be actual reduced test curves having no irreducible component equal to \(C\), and let their strict transforms map birationally onto them. Suppose these transforms meet the inverse support only at regular points of \(S\), where the inverse support consists of a single regular curve. Let \(n_{ji}\) be the sum of local intersection multiplicities of \(\widetilde T_j\) with \(\Gamma_i\), including branch multiplicities if a test curve is singular.

A degree-\(b\) sole-support mate necessarily gives positive integers \(r_i\) satisfying
\[
ab=d\sum_i e_i r_i,\qquad
b\deg T_j=\sum_i n_{ji}r_i\quad\text{for every }j.             \tag{*}
\]
Indeed its pulled-back divisor is \(\sum r_i\Gamma_i\); intersecting with \(H\) gives the first equation. On the normalization of a test curve its section has zeros only at the attaching points. At a regular single-branch attachment a local equation is a unit times the inverse-curve parameter to power \(r_i\), giving the second equation. A nonzero section of \(\mathcal O_{T_j}(b)\) has total zero degree \(b\deg T_j\). The section cannot vanish identically on a test component, since that component would be extra support.

Thus inconsistency even over positive rational \(r_i/b\) obstructs all mate degrees. This separates the reusable mechanism from the quartic example: full support, actual test curves and verified local attachments are the essential hypotheses. It is not a sufficiency criterion when the linear system has a positive solution. Singular normalization points require a different local calculation; generic normal roots alone do not supply \(n_{ji}\).

## Four lines on the mixed-weight sextic

## Exact proposed statement

Let \(k\) be algebraically closed of characteristic zero and
\[
C_0=[s^4:s^3t:st^3:t^4],\quad
q=x_0x_3-x_1x_2,\quad
c_0=x_1^3-x_0^2x_2,\quad c_2=x_2^3-x_1x_3^2.
\]
For every \(\alpha\beta\ne0\), the integral surface
\[
X_{\alpha,\beta}=V(q^3+\alpha c_0^2+\beta c_2^2)
\]
has **no homogeneous set-theoretic mate of any positive degree** for
\(C_0\).
Integrality of every member is an input from the reviewed degree-six
calculation. The new argument uses actual ruling lines and the degrees of
the pullback of a hypothetical global equation on the normalization.
It makes no assertion about other sextic families or arbitrary carriers.

## 1. Normalization of the parameters and four actual lines

The curve-preserving torus substitution from the
[earlier proof](MIXED_SEXTIC_CONTACT.md) puts every nonzero
parameter pair, up to a projective automorphism and nonzero scalar, into
\[
F_h=hq^3+c_2^2-c_0^2,\qquad h\ne0.
\]
Work with this form. On the affine chart \(x_0=1\), write
\[
x_1=t,\qquad x_2=w,\qquad x_3=tw+q.
\]
On the target quadric \(q=0\),
\[
c_0=t^3-w,\qquad c_2=w^2(w-t^3),\qquad
F_h|_{q=0}=(w-t^3)^2(w^4-1).
\]
Consequently, for each fourth root of unity \(\zeta\), the **actual
projective line**
\[
L_\zeta=V(x_2-\zeta x_0,\ x_3-\zeta x_1)
\]
lies on \(X_h\). It is not a component of \(C_0\).
Its intersection with \(C_0\) consists of the three distinct points
\[
[1:t:t^3:t^4],\qquad t^3=\zeta.
\]
None is a parameter endpoint. The remaining point of the projective line
is \([0:1:0:\zeta]\), which is not on \(C_0\).

## 2. Which normal branch each line meets

At the generic point of \(C_0\), set \(u=w-t^3\). The quadratic transverse
initial form of \(F_h\) is
\[
(t^6u-2t^5q)^2-u^2
=[(t^6-1)u-2t^5q][(t^6+1)u-2t^5q].
\]
There are two distinct smooth formal branches over \(k(t)\), labelled
by their tangent equations \(c_2=+c_0\) and \(c_2=-c_0\). Let
\(\Gamma_+\) and \(\Gamma_-\) be the corresponding irreducible curves in
the finite normalization \(\nu:S\to X_h\). Each maps to \(C_0\) with
generic degree one. These are the only divisorial components above
\(C_0\), since the generic transverse curve has exactly these two
branches.

The same two branches remain distinct and their normalizations remain
smooth at every point \(t^3=\zeta\): the discriminant of the displayed
binary quadratic is \(16t^{10}\ne0\). More explicitly, its \(q^2\)
coefficient is a unit. The formal Weierstrass factors therefore write
each local surface branch as a smooth graph \(q=q_\pm(t,u)\), and
\(u=0\) is its local inverse curve.

On \(L_\zeta\) one has the exact identity
\[
c_2=-\zeta^2c_0.
\]
Thus its strict transform meets only the curve with label
\(-\zeta^2\) at each of the three intersection points. Its transverse
coordinate is \(u=\zeta-t^3\), which has a simple zero there. The
intersection with that inverse curve has multiplicity one at each
point. Two of the four lines attach to \(\Gamma_+\), and two attach
to \(\Gamma_-\). This is actual branch attachment, not merely a
comparison of generic tangent directions.

The line is generically in the smooth locus of \(X_h\). Indeed at
\(q=0,w=\zeta,w\ne t^3\), differentiating the displayed restriction
with respect to \(w\) gives \(4\zeta^3(\zeta-t^3)^2\ne0\).
Its strict transform therefore maps to the line birationally.

## 3. A hypothetical mate gives incompatible degree identities

Suppose a homogeneous form \(G_b\), \(b>0\), satisfied
\(V(F_h,G_b)_{\mathrm{red}}=C_0\).
It does not vanish identically on \(X_h\), and its pullback is a
nonzero section of \(bH\), where \(H=\nu^*\mathcal O_{X_h}(1)\).
Its effective divisor has the form
\[
\operatorname{div}(\nu^*G_b)=r\Gamma_++s\Gamma_-,
\qquad r,s>0.
\]
There can be no other divisor component: its image would be contained
in \(C_0\), and the two listed generic branches exhaust the divisorial
inverse image. Possible isolated inverse points do not add a divisor
component or alter the degree identity.

Near an attaching point of \(L_\zeta\), the relevant local surface
branch is regular, with inverse curve parameter \(u\). The pullback
of \(G_b\) is therefore \(u^r\) times a unit, or \(u^s\) times a unit,
according to the label. An extra zero of the remaining factor would
give another divisor component, contrary to the support assumption.
Since \(u|_{L_\zeta}\) has a simple zero, the order of \(G_b\) on the
line is exactly \(r\), respectively \(s\), at each of its three
points on \(C_0\).

The restriction \(G_b|_{L_\zeta}\) is a nonzero section of
\(\mathcal O_{\mathbf P^1}(b)\). Otherwise the line itself would be
additional intersection support. It has no zeros outside those three
points. The two labels consequently give
\[
b=3r,\qquad b=3s.
\tag{1}
\]
On the other hand, \(H^2=6\) and \(H\cdot\Gamma_\pm=4\). Intersecting
the pullback divisor with \(H\) gives
\[
6b=4(r+s).
\tag{2}
\]
Equations (1) and (2) imply \(6b=8b/3\), impossible for \(b>0\).
This proves the proposed exclusion without fixing the mate degree.

## 4. A residual consequence retaining proper intersections

For any actual proper containing pair \((F_h,G_b)\), let \(r,s\) be
its two finite generic branch orders, so \(m_C=r+s\). If
\(m_C>2b/3\), at least one branch order exceeds \(b/3\).
Both ruling lines attached to that branch must then be contained in
\(V(G_b)\): a nonzero degree-\(b\) restriction would already have more
than \(b\) zeros at its three attaching points. Those two lines are
genuine residual components downstairs.

This last argument uses a lower bound for the local zero orders; any
additional local zeros strengthen it. It does not assert that every
proper mate has high contact, or compute the full residual scheme.
It explains geometrically why a sole-support candidate is impossible.

## A larger graded subalgebra: all coefficients and all mate degrees

## Exact larger family

Let \(k\) be algebraically closed of characteristic different from two and put
\[
q=x_0x_3-x_1x_2,\quad c_0=x_1^3-x_0^2x_2,\quad
c_2=x_2^3-x_1x_3^2.
\]
Fix \(m\ge1\). For arbitrary constant-coefficient binary homogeneous
forms \(B_j(U,V)\) of degree \(j\), consider the actual global equation
\[
F=\sum_{i=0}^{\lfloor m/2\rfloor}
q^{3i}B_{m-2i}(c_0,c_2).
\tag{1}
\]
It is homogeneous of ordinary degree \(3m\). Assume that \(B_m\)
is squarefree and that neither \(U\) nor \(V\) divides it. Equivalently,
its \(m\) distinct roots are
\[
V=\lambda_j U,\qquad \lambda_j\in k^*,\quad 1\le j\le m.
\tag{2}
\]
The reviewed conclusion is:

> For every \(F\) in (1) satisfying (2), and every homogeneous \(G_b\)
> of positive degree, \(V(F,G_b)_{\mathrm{red}}\ne C_0\).

No integrality hypothesis on \(F\) is needed. In particular this is
larger than the diagonal sextic seed and permits reducible carriers.
For \(m=2k\) the coefficient space has dimension \((k+1)^2\);
for \(m=2k+1\) it has dimension \((k+1)(k+2)\).
These are dimensions of actual homogeneous source spaces: \(q,c_0,c_2\)
are algebraically independent. For example, at \(x_0=x_3=1,x_1=x_2=0\), their Jacobian with respect to \(x_1,x_2,x_3\) is
\[
\begin{pmatrix}0&0&1\\0&-1&0\\-1&0&0\end{pmatrix},
\]
with determinant \(-1\) in every characteristic.

## The ordinary branches and their actual attached lines

On \(x_0=1\) use \(t=x_1,w=x_2,q=x_3-tw\), and set \(u=w-t^3\).
Then \(c_0=-u\) and
\[
c_2=t^6u-2t^5q+\text{terms of normal order at least two}.
\]
The normal order of the \(i\)-th summand in (1) is at least \(m+i\).
Thus the first initial form is \(B_m(c_0,c_2)\), which is a product
of \(m\) distinct linear forms over \(k(t)\). The \(m\) branches all
have residue field \(k(t)\). More explicitly, substitute \(q=uz\)
and divide (1) by \(u^m\). At \(u=0\), its roots in \(z\) are
\[
z_j(t)=\frac{t^6+\lambda_j}{2t^5},
\]
and all are simple. The implicit function theorem therefore gives
regular local branches \(q=u z_j(t,u)\) at every finite nonzero
curve parameter.

On the target quadric \(q=0\), the exact identities are
\[
c_0=t^3-w,\qquad c_2=-w^2c_0,\qquad
F|_{q=0}=c_0^m B_m(1,-w^2).
\]
For each \(\lambda_j\), both square roots \(\zeta\) of
\(\zeta^2=-\lambda_j\) give actual projective ruling lines
\[
L_\zeta=V(x_2-\zeta x_0,\ x_3-\zeta x_1)\subset V(F).
\]
There are \(2m\) distinct such lines. Each meets \(C_0\) in the length-three nonendpoint scheme \(t^3=\zeta\). It consists of three distinct points when the characteristic is not three, and one point of intersection multiplicity three in characteristic three. At those points it lies
on exactly the branch labelled \(\lambda_j\), since
\(c_2=\lambda_jc_0\) on the line. Its normal parameter \(u=\zeta-t^3\) has total zero order three on the line: one at each of three points outside characteristic three, or order three at the single attaching point in characteristic three.

Each line is generically in the smooth locus of the reduced surface:
at \(w=\zeta\), away from \(C_0\), the \(w\)-derivative of
\(c_0^mB_m(1,-w^2)\) is nonzero because \(\zeta\ne0\) and the binary
root is simple. Hence a line is contained in one global irreducible
surface component, and its strict transform in that component's
normalization is finite and birational over a smooth projective line.
It cannot acquire an attachment on a second local branch.

## Reducible equations do not evade the degree contradiction

Suppose a sole-support mate \(G_b\) existed. Every irreducible factor
of \(F\) must contain \(C_0\): otherwise its positive-degree proper
intersection with \(G_b\) would be a projective curve lying in its
finite intersection with \(C_0\), impossible. A common surface factor
with \(G_b\) would already violate sole support.

Each factor therefore has positive generic normal order along \(C_0\).
Since the initial form of \(F\) is squarefree, no global factor can
occur with multiplicity greater than one. Thus \(F\) is squarefree
under the hypothetical mate assumption, and the sum of degrees of
its distinct irreducible factors is \(3m\).

Normalize the components separately. The divisorial inverse image
of \(C_0\) has precisely \(m\) branches \(\Gamma_j\), each of generic
degree one over \(C_0\). The pullback of \(G_b\) has divisor
\[
\sum_{j=1}^{m}r_j\Gamma_j,\qquad r_j>0.
\]
Intersecting with the pulled-back hyperplane, and summing over these
normalizations, gives
\[
3mb=4\sum_{j=1}^{m}r_j.
\tag{3}
\]
The two actual lines attached to branch \(j\) lie on its global
component. Their attaching points are regular normalization points with local inverse-curve parameter \(u\). Restricting \(G_b\) to either line gives zero order \(r_j\operatorname{ord}(u)\), of total \(3r_j\), and no other zeros. In characteristic three this is a single zero of order \(3r_j\). Hence
\[
b=3r_j\quad\hbox{for every }j.
\tag{4}
\]
Combining (3) and (4) yields \(3mb=4mb/3\), a contradiction for
\(m,b>0\).

## Search consequence and exact limitations

Within this graded subalgebra source, a possible supporting equation
must therefore lie on the repeated-root or axis-root locus of its
leading binary form. Lower terms in (1) cannot repair the obstruction
on the stated nondegenerate open set. This is an actual global
equation restriction across all these degrees and all mate degrees,
not a finite numerical sample.

It does not cover arbitrary forms in \(H^0(\mathcal I_C(3m))\),
the excluded binary boundary, or other normalization models. The proof extends to every odd characteristic with the length-three attachment interpretation just given. It does not establish an all-pairs lower bound for \(\delta(p)\). In characteristic two the linear change from \(c_0,c_2\) to the two normal parameters loses rank, the two square-root ruling lines merge, and this proof does not apply.

## Critical degree and the residual-curve extension

## 2. Literal test-curve theorem in every degree margin

Fix \(m\ge1\), \(a\ge3m\), and \(F\in V_{a,m}\) of exact normal order
\(m\), with \(q\nmid F\). Assume:

1. The full first normal root divisor is horizontal, reduced and
   irreducible. Equivalently here, the initial binary normal form is
   irreducible of degree \(m\) over \(k(C)\), with no vertical coefficient
   divisor. Its normalization branch \(\Gamma\) has generic degree \(m\)
   over \(C\).
2. Inside \(Q\simeq\mathbf P^1\times\mathbf P^1\), the actual restriction is
   \[
   \operatorname{div}_Q(F)=mC+T,
   \quad [T]=(a-m,a-3m),
   \]
   with \(T\) reduced, no component equal to \(C\), and \(T\cap C\)
   reduced. The intersection avoids the two parametrization endpoints.
3. At each point of \(T\cap C\), the normal root in the direction tangent
   to \(Q\) is simple. The corresponding local branch of the normalization
   is regular, and the strict transform of \(T\) meets \(\Gamma\) simply.
   This last assertion follows from the simple-root condition and the
   transverse intersection in item 2, as verified below.

Then **no homogeneous \(G_b\), \(b>0\), has
\(V(F,G_b)_{\mathrm{red}}=C\)**. Global irreducibility of \(F\) need not
be added as a separate hypothesis.

### Why the branch hypothesis has actual geometric content

Use local coordinates \(t,u,q\), with \(C=(u,q)\) and \(Q=(q)\).
Blow up \((u,q)\) and use \(q=uz\). After dividing by \(u^m\), the
strict-transform equation has the form
\[
f_m(t,1,z)+u(\cdots)=0.
\]
At a point of \(T\cap C\), its root \(z=0\) is simple. The implicit
function theorem gives a regular graph \(z=z(t,u)\). Its inverse curve
is \(u=0\). The strict transform of the actual residual \(T\), with
\(q=0\), lies on this one local branch. Since \(T\) meets \(C\)
transversely in \(Q\), \(u\) has order one on \(T\).
Other normal roots at the same base point need not be simple: only
this attached root is used.

Every component of \(T\) is generically in the smooth locus of \(V(F)\):
away from \(C\), its reduced equation in \(Q\) has a nonzero derivative.
Thus its strict transform maps birationally to that actual component.
These are genuine curves downstairs, not vertical exceptional cycles.

### The two incompatible degree equations

Suppose a sole-support mate existed. Every irreducible factor of \(F\)
must contain \(C\); otherwise its proper positive-degree intersection
with \(G_b\) would be a projective curve contained in its finite
intersection with \(C\). A common surface factor with \(G_b\) already
violates sole support. The irreducible first normal form then forces
\(F\) to have just one global factor, with multiplicity one.

Let \(\nu:S\to V(F)\) be its finite normalization and
\(H=\nu^*\mathcal O(1)\). The divisorial inverse image of \(C\) is the
single curve \(\Gamma\), of degree \(m\) over \(C\). A hypothetical mate
has
\[
\operatorname{div}(\nu^*G_b)=r\Gamma,\qquad r>0.
\]
Intersection with \(H\), using \(H^2=a\), \(H\cdot\Gamma=4m\), gives
\[
ab=4mr. \tag{1}
\]
Its restriction to the actual residual curve \(T\) is nonzero and has
zeros only at \(T\cap C\). The local graph above makes every zero have
order exactly \(r\). Therefore
\[
b\,\deg T=r(C\cdot T).
\]
Here the actual divisor classes on the smooth target quadric give
\[
\deg T=2a-4m,\qquad C\cdot T=4a-6m.
\]
Consequently
\[
b(2a-4m)=r(4a-6m). \tag{2}
\]
Eliminating \(r\) between (1) and (2) requires
\[
2a^2-7am+8m^2=0.
\]
This is impossible: its discriminant in \(a/m\) is \(-15\), or
\[
2a^2-7am+8m^2
=2(a-7m/4)^2+15m^2/8>0.
\]
The obstruction is uniform in the mate degree.

When the normalization is regular along the whole \(\Gamma\), the same
geometry can be expressed as a numerical divisor gap. The pullback of
the quadric is \(\Gamma+\widetilde T\), so
\[
\Gamma^2=14m-4a,\qquad
\det\begin{pmatrix}H^2&H\Gamma\\H\Gamma&\Gamma^2\end{pmatrix}
=-2(2a^2-7am+8m^2)<0.
\]
A mate would make \(bH=r\Gamma\), forcing that determinant to vanish.
The actual residual curve exhibits the numerical independence directly.

## 3. A nonempty dense open subset of every full actual source is excluded

The preceding hypotheses hold on a nonempty Zariski-open subset of
every \(V_{a,m}\), \(a\ge3m\). This is a statement about the full actual
global source, not merely the small subalgebra \(k[q,c_0,c_2]\).

The [normal-bundle splitting R-0020](../results/quartic_conormal_characteristic_jump.md)
gives \(\mathcal I_C/\mathcal I_C^2=\mathcal O(-7)^2\).
On the normal-direction surface
\[
P=\mathbf P^1_{\rm base}\times\mathbf P^1_{\rm direction},
\]
the order-\(m\) symbol of a degree-\(a\) equation cuts a divisor of class
\[
(4a-7m,m).
\]
The first entry is the coefficient degree on the base; the second is
the degree of its covering of \(C\).

The actual cubic equations globally generate
\((\mathcal I_C/\mathcal I_C^2)(3)=\mathcal O(5)^2\): use the cubic
generators of \(\mathcal I_C\) and the products \(q x_i\). Hence their
normal forms give a basepoint-free system of class \((5,1)\) on \(P\).
Writing \(a=3m+u\), \(u\ge0\), the products of \(m\) cubics multiplied
by ambient degree-\(u\) forms lie in \(V_{a,m}\) and generate the
symbol line bundle \(\mathcal O_P(4a-7m,m)\) at every point.
The full actual symbol system is therefore basepoint free and ample.

In characteristic zero a general member is smooth. For the actual basepoint-free symbol space \(W\), the universal zero incidence inside \(P\times\mathbf P(W)\) is a projective bundle over the smooth surface \(P\): evaluation onto the symbol line bundle is surjective. Its total space is smooth. The generic parameter fiber is regular as a localization of this regular total space, and is smooth over the characteristic-zero function field. The projection is proper, so the image of its nonsmooth locus is closed and misses the generic parameter. Its complement is the required nonempty open set of smooth divisors. This argument uses the actual symbol image and does not assume that its map is an immersion or that every abstract symbol lifts.

The divisor is connected because
\[
H^1(P,\mathcal O_P(-(4a-7m),-m))=0
\]
by the Künneth formula. A smooth connected divisor is irreducible. This produces the single horizontal normal cover, of degree \(m\). Ampleness, basepoint freedom and connectedness are verified for the actual symbol system; no surjectivity onto the entire abstract symbol target is needed.

The residual restriction system on \(Q\) contains all products of
degree-\(2m\) forms in the first ruling and forms of class \((u,u)\).
It is therefore the complete system of class \((2m+u,u)\).
For \(u>0\), a general residual \(T\) is smooth and meets \(C\)
transversely away from the endpoints. For \(u=0\), it is \(2m\)
distinct nonendpoint ruling lines, and their cubic inverse parameters
on \(C\) are distinct in characteristic zero.

The simple attached normal root is also an actual open condition with
a nonempty complement to its failure locus. At each point of the
quadric-direction section on \(P\), choose a cubic \(H_3\) whose normal
value is nonzero and an ambient linear form \(\ell\) nonzero at the
base point. The normal forms of
\[
H_3^m P_u,\qquad qH_3^{m-1}P_{u+1}
\]
can be chosen with respectively a nonzero value, and zero value but
nonzero vertical derivative. Both have degree \(a\) and order at
least \(m\). Thus value and vertical derivative impose two independent
linear conditions at each point of this one-dimensional section.
The bad incidence has codimension at least one in the projective
symbol parameter space. Its image is closed because the section is
projective. A general symbol avoids it.

The finite collection of nonempty open conditions just described has
nonempty intersection in the irreducible actual parameter space.
Pulling them back under the linear symbol map gives the claimed
nonempty dense open subset of \(V_{a,m}\). Every member in that open
has no mate of any degree.

This does not prove that a generic pair fails by a new dimension
heuristic: it identifies an explicit geometric open carrier class and
a uniform test-curve contradiction on it. A hypothetical STCI can
still lie in its special closed complement.

## 4. A normal-root slope balance on the remaining ordinary locus

There is a refinement when the full normal root divisor is horizontal
and reduced but possibly reducible, while the actual residual and all
its attachments satisfy the regularity conditions above. Let its
components have projection degrees
\[
e_j=\deg(Z_j\to C),\qquad d_j=\deg(Z_j\to\mathbf P^1_{\rm direction}).
\]
Then
\[
\sum e_j=m,\qquad \sum d_j=4a-7m.
\]
The quadric normal direction is a graph of degree one. Indeed its
conormal form is a nowhere-simultaneously-zero pair of linear forms
in the balanced splitting. Its intersection with \(Z_j\) therefore
has degree \(e_j+d_j\); these are exactly the ordinary actual
attachments of \(T\) to the inverse curve \(\Gamma_j\).

A hypothetical mate has orders \(r_j>0\) on these inverse curves.
The two global degree equations become
\[
ab=4\sum e_jr_j,\qquad
b(2a-4m)=\sum(e_j+d_j)r_j.
\]
Thus
\[
\frac{\sum d_jr_j}{\sum e_jr_j}=7-\frac{16m}{a}. \tag{3}
\]
The unweighted ratio of the two sums is
\((4a-7m)/m\), strictly larger, since
\[
4a/m-7-(7-16m/a)
=\frac{2(2a^2-7am+8m^2)}{am}>0.
\]
Consequently a surviving ordinary candidate must have some component
\[
\boxed{\frac{d_j}{e_j}\le7-\frac{16m}{a}<7.}
\]
At the critical degree \(a=3m\), the bound is \(5/3\); a component
of covering degree one then has direction degree at most one.
This locates the possible escape in a low-variation component,
repeated/vertical normal structure, or nonordinary attachments.
It does not say that such a component is globally realizable by a
supporting pair.

## 5. An explicit new carrier outside the old subalgebra

The test-curve criterion is nonvacuous beyond the old source. Put
\[
F=c_0^2+c_2^2+q\,x_0c_0,\qquad
c_0=x_1^3-x_0^2x_2,\quad c_2=x_2^3-x_1x_3^2.
\]
It has degree six and order two. On \(x_0=1\), with \(u=w-t^3\),
its initial binary quadratic is
\[
4t^{10}q^2+(-4t^{11}-1)qu+(1+t^{12})u^2.
\]
Its discriminant is \(1+8t^{11}-16t^{10}\), of odd degree eleven,
so it is not a square in \(k(t)\). Hence there is one generic
normalization inverse curve of degree two over \(C\).

On the actual quadric,
\[
F|_Q=u^2(w^4+1).
\]
The four residual lines have \(w=\zeta\), \(\zeta^4=-1\), and meet
\(C\) at \(t^3=\zeta\). At these points the coefficient
\(-4t^{11}-1\) is nonzero: its vanishing together with
\(t^{12}=-1\) would force \(t=4\), impossible in characteristic zero.
Thus each attached \(q=0\) branch is regular and every line meets it
simply. The single-cover test-line argument excludes all mate degrees:
\[
6b=8r,\qquad b=3r.
\]

The carrier is outside the constant-coefficient degree-six subalgebra
source. Its quadric restriction fixes the binary boundary
\(c_0^2+c_2^2\); representing its remaining term there would require
\(q x_0c_0\) to be a scalar multiple of \(q^3\), which it is not.

The [new exact control](../computations/stci_game_obstruction_2026_10_30.m2)
checks this carrier's normal form, discriminant, line factorization
and nonvanishing condition. These are local/global identity controls;
they do not supply a normalization classification. This example need not belong to every smooth-root
generic condition in Section 3; the smaller test-line criterion suffices.

## What a surviving carrier must change

The critical-degree \(a=3m\) single-cover theorem and its nonempty open actual-source class were independently reconstructed in the source geometric review. The all-degree extension received independent consolidation review of its openness, actual residual restriction, attachment hypotheses and numerical elimination; it is not a sampled-rank extrapolation.

The degree-eight elliptic normalization source gives a useful numerical boundary case: its horizontal inverse component has covering degree two and direction degree six, and \(6/2=7-16\cdot2/8=3\). The full order-two normal divisor has class \((18,2)\), so that horizontal component requires vertical degree twelve. This is an actual reason it escapes the ordinary full-horizontal class. Its first explicit image nevertheless fails full inverse support; [the projection/gluing construction](../synthesis/projection_and_elliptic_gluing.md) treats that separate issue. A numerical solution of (*) need not descend to an equation or remove isolated inverse points.

The concrete remaining alternatives are repeated normal roots, vertical coefficient divisors, low-direction-degree components, or nonordinary attachments. No theorem here puts every hypothetical STCI carrier in the excluded open class. A closed complement can contain all solutions of a nonlinear existence problem.

## Exact polynomial controls

The [mixed-line verifier](../computations/stci_mixed_weight_lines_2026_10_30.m2) and its independent counterpart retain the quadric factorization, line identities and discriminant. Their purpose is to establish the geometric input to (*), rather than supply a surrogate normalization classification. The [extra sextic verifier](../computations/stci_game_obstruction_2026_10_30.m2) retains the nonsquare discriminant and simple attachment check for the carrier outside the small subalgebra. The exact [degree-six branch computation](MIXED_SEXTIC_CONTACT.md) remains separate because its branch-order bound and residual floor are stronger quantitative information in that degree.


## Characteristic reach of the test-curve mechanism

The reusable degree equations (*) hold in arbitrary characteristic under their stated finite-normalization and regular-attachment hypotheses, because intersection multiplicities and section degrees are integer equalities. The weighted-subalgebra theorem and its universal Jacobian minor received independent consolidation review in every odd characteristic. The theorem is proved above in every odd characteristic, with a triple contact at one line attachment in characteristic three. The mixed-weight sextic seed is contained in that source, so its all-mate exclusion also holds in odd characteristic without importing the characteristic-zero integrality or matrix-rank proof. The detailed individual branch-order bound in degree six remains characteristic zero.

The full-source dense-open construction and normal-slope application are retained in characteristic zero. Their smooth-cover argument uses characteristic-zero generic smoothness; inseparable positive-characteristic symbol systems need separate analysis. Characteristic two changes the normal splitting and the subalgebra root separation. These are specific failure mechanisms, compatible with the [quartic-carrier STCI construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
