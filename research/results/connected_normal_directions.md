---
id: STCI-R-0077
type: result
title: Connected normal directions, residual degree and deep contact on the equality boundary
scope: "#scope"
statement: "#statement"
proofs:
  - name: quadric restriction, connectedness and the normal bundle of the surviving section
    at: "#proof"
    using: [STCI-R-0020]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Connected normal directions and deep generic contact

## Scope

Let \(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field. Take
actual homogeneous equations \(F_a,G_b\) meeting properly and containing
\(C\), with exact generic normal orders \(p,q\ge1\). Write their cycle as
\(m[C]+R\), with \(\delta=\deg R=ab-4m\). Assume \(a\ge3p,\ b\ge3q\).
Every sole-support pair satisfies these slope inequalities by restriction
to the smooth quadric containing \(C\). The residual test works in every
characteristic. The deep-contact estimate uses characteristic zero.
[Quadric restriction and depth conventions](../arguments/residuals/generic_contact_depth.md#4-smooth-quadric-family).

On \(B=\operatorname{Bl}_C\mathbf P^3\), let \(H\) be the hyperplane
pullback and \(E\) the exceptional divisor. Let \(W\) be the proper
intersection of the strict transforms, of classes \(D_F=aH-pE\) and
\(D_G=bH-qE\). On \(E\) form the scheme
\[
 U=V_E(\sigma_p(F),\sigma_q(G))=W\cap E
\]
from the two actual leading forms, retaining coefficient zeros at closed
points. Write \(t\) for the sum of the scheme lengths at isolated points
of \(U\) and \(h\) for the number of connected components of its support
that contain curves.

## Statement

1. **Residual test in all degrees.** \(H^0(W,\mathcal O_W)=k\). For sole
   support, \(U_{\rm red}=W_{\rm red}\) is a nonempty connected curve of
   pure dimension one. An isolated common zero or disconnected common
   zero set therefore forces a projective residual curve. Whenever
   \(R\ne0\), its degree satisfies \(3\delta\ge t+h\).
2. **A unique common direction on the numerical boundary.** In
   characteristic different from two write \(E=\mathbf P^1_C\times
   \mathbf P^1_{\rm dir}\) in the balanced normal frame. Under sole
   support the degree of the cycle of \(W\) in the direction factor is
   \[
        u=7ab/4+7pq-4(aq+bp).
   \]
   If \(u=0\), then \(W_{\rm red}\) is one constant section \(T\), of
   cycle multiplicity \(c=ab/4-pq\). At \((a,b)=(3p,4q)\) the
   restriction of \(F\) to the quadric after removing \(pC\) is \(2p\)
   times a single ruling line. The divided restriction of \(G\) cuts
   that line in \(q\) times one marked point.
3. **A projective bound on the next orders.** Assume characteristic zero,
   sole support and \(u=0\). Put \(r=\operatorname{ord}_T D_F\),
   \(s=\operatorname{ord}_T D_G\). Let \(d=2\) at the two endpoint
   directions of the marked balanced frame and \(d=3\) at every mixed
   direction. Then
   \[
    (4a-7p)s+(4b-7q)r\ \le\ (7-d)c+d\,rs.                 \tag{1}
   \]
   In the generic plane contact tree, give the original point depth zero.
   **Strictly more than \(pq/2\) units of intersection multiplicity
   occur at depths at least three.** A mixed direction requires a common
   point of depth at least four. These statements hold on the entire
   equality \(u=0\), with arbitrary \(p,q\) and arbitrary subsequent
   branching.

## Proof

### Connectedness and residual attachment

The strict quadric \(Q'\sim2H-E\) is the original smooth quadric, since
\(C\) is Cartier on it. Use ruling coordinates with \(C\sim(1,3)\).
In every characteristic,
\[
 H^i(B,\mathcal O_B(jH-nE))=0
 \quad (i>0,\ n\ge0,\ j\ge3n-1).
\]
For \(n=0\) this is projective-space cohomology, using
\(R\pi_*\mathcal O_B=\mathcal O_{\mathbf P^3}\). Locally the blowup of
the regular sequence defining \(C\) is the divisor of a linear equation
in a relative \(\mathbf P^1\), whose ideal \(\mathcal O(-1)\) has zero
direct images. For \(n>0\), restriction to \(Q'\) gives kernel
\(\mathcal O_B((j-2)H-(n-1)E)\) and quotient
\(\mathcal O_Q(j-n,j-3n)\). The kernel satisfies the induction bound
and both ruling degrees are at least \(-1\).
[Cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS).

Since \(K_B=-4H+E\), this gives higher-cohomology vanishing for
\(K_B+D\) with \(D=D_F,D_G,D_F+D_G\). Serre duality gives
\(H^i(B,\mathcal O_B(-D))=0\) for \(i=0,1,2\).
The strict divisors share no surface. Their Koszul resolution now gives
\(H^0(\mathcal O_W)=k\), including for reducible or nonreduced members.
In particular \(W\) is nonempty and connected. It is a pure
Cohen–Macaulay curve. Off \(E\) it agrees with the original intersection
off \(C\), so its components outside \(E\) have cycle the strict
transform \(\widetilde R\).

At an isolated point of \(U\), a local equation of \(E\) is a
nonzerodivisor on \(\mathcal O_W\). There the length of \(U\) equals
the intersection multiplicity of \(E\) with \(\widetilde R\), including
the generic multiplicities of residual components. If \(R\ne0\),
each curve-containing connected component of \(U\) must also meet
\(\widetilde R\). Otherwise that component would be open and closed in
\(W_{\rm red}\). Such an attachment contributes at least one at a
point distinct from the isolated points and the other components.
The cubics through \(C\) generate its twisted ideal, so \(3H-E\) is nef.
Indeed \(\mathcal I_C(3)\) is an extension of
\(\mathcal O_Q(2,0)\) by \(\mathcal O_{\mathbf P^3}(1)\). The quotient
generators lift since \(H^1(\mathcal O_{\mathbf P^3}(1))=0\), and
linear multiples of the quadric generate the kernel.
Consequently
\[
 t+h\ \le\ E\cdot\widetilde R\ \le\ 3H\cdot\widetilde R=3\delta .
\]
This identifies what the two symbols alone can charge to the
[valuative residual contact cycle](../arguments/residuals/residual_contact_cycles.md#3-a-contact-cycle-built-from-the-actual-residual-branches).
In the balanced frame the test uses bihomogeneous polynomials on a
product of lines. Their common divisor, including any fiber factors,
gives the curve part of \(U\). The common zeros of the divided forms
away from this divisor give exactly the isolated scheme measured by \(t\).

Connected symbols can occur with substantial residual degree. In every
even degree \(a\ge6\), take a general \(F\in H^0(I_C(a))\) and
\(G=F+Q^{a/2}\), where \(Q\) also denotes the quadric equation.
The actual first-order source generates the twisted conormal bundle.
A general section of this rank-two bundle on a curve has no zero, and
its value at the generic point is independent of the quadric direction.
Indeed, evaluation at each point has rank two, so the incidence of a
zero has codimension at least one in the source. Independence at one
fixed point is also a nonempty open condition. Thus \(U\) is one smooth
section. The pair generates \((F,Q^{a/2})\) and has \(m=a/2\) and
\(\delta=a(a-2)>0\).
[Actual cubic generation](../arguments/curve/carrier_test_curves.md#3-a-nonempty-dense-open-subset-of-every-full-actual-source-is-excluded).

### The equality boundary on the first blowup

Under sole support, every component of \(W\) lies in \(E\). In the
balanced frame \(H|_E=(4,0)\), \(E|_E=(7,-1)\). The first blowup gives
total degree \(c=m-pq\) over \(C\) and direction degree \(u\) as in the
statement. Equivalently, \(H\cdot W=ab-4pq\) and
\(E\cdot W=4(aq+bp)-14pq=7c-u\).
[Intersection computation](../arguments/normal-geometry/rees_and_vertical_controls.md#supported-cycle-bidegrees-and-the-universal-numerical-restriction).

If \(u=0\), each effective component has constant direction. Different
constant sections are disjoint, so connectedness leaves precisely one.
For \(a=3p,\ b=4q\) the strict restrictions to \(Q'\) have classes
\((2p,0)\) and \((3q,q)\). Every ruling line in the first meets the
second in a nonzero divisor of degree \(q\), since a shared line would
survive downstairs. Each of these points belongs to \(W\cap Q'\).
The quadric direction \(Q'\cap E\) is a section of bidegree \((1,1)\),
so it meets \(T\) at just one point \(P\). Only one line of the chosen
ruling passes through \(P\). This proves the line and trace assertions
without any assumption on ramification of the trisecant projection.
[Earlier distinct-ruling bound](../arguments/normal-geometry/rees_and_vertical_controls.md#the-exact-supported-3p4q-boundary-and-distinct-residual-roots).

### The normal bundle of a constant section

In characteristic zero, the sequence for \(T\subset E\subset B\) is
\[
 0\longrightarrow\mathcal O\longrightarrow N_{T/B}
   \longrightarrow\mathcal O(7)\longrightarrow0.
\]
Its extension class, up to sign and a nonzero scalar, is the quadratic
class for the corresponding constant direction. To see this, choose a
normal relation \(w\) defining the direction and a complementary normal
coordinate \(l\). In the established two-chart transition,
\(w'=z^{-7}(w+h\,l^2)\) modulo terms divisible by \(w\) of order two
and terms of order three. On the blowup chart \(v=w/l\) the section has
ideal \((v,l)\). Modulo its square, \(l'=z^{-7}l\) and
\(v'=v+h\,l\). This is the conormal extension, dual to the displayed
normal sequence. In the marked frame the cocycles are
\[
 h_\theta=3\bigl(\theta^3z^{-5}-\tfrac12\theta^2z^{-4}
                    +\tfrac14\theta z^{-3}-\tfrac18 z^{-2}\bigr),
 \qquad h_\infty=3z^{-5}.
\]
[Two-chart formula](../arguments/equations/global_lifting_interfaces.md#4-applying-accepted-p-010-data-to-c0).

The least degree \(d\) of a nonzero binary form annihilating \(h\) in
cohomology is two for \(\theta=0,\infty\) and three otherwise.
For example, at a mixed direction, for \((b_0+b_1z+b_2z^2)h_\theta\)
the coefficients of \(z^{-1},z^{-2},z^{-4}\) successively force
\(b_1=2\theta b_2,\ b_0=0,\ b_1=0\). A cubic annihilator exists since
the target \(H^1(\mathcal O(-4))\) has dimension three. The two endpoint
monomials give the degree-two assertion directly.
[Annihilator calculation](../arguments/local-cohomology/direction_and_apolarity.md#constant-directions-require-a-prescribed-common-scalar-divisor).

Twist the normal sequence by \(\mathcal O(-7+j)\). For \(0\le j<7\),
sections of the middle term are exactly the degree-\(j\) forms killed
by \(h\). By splitting on \(\mathbf P^1\), the largest normal summand
therefore has degree \(7-d\) (a summand of degree greater than seven
could map to neither outer line). The determinant gives the other
summand. Hence \(N_{T/B}\simeq\mathcal O(d)\oplus\mathcal O(7-d)\).
This gives the geometric role of the quadratic class at the next blowup.

### Bounding the orders after blowing up the section

More generally, let two proper Cartier divisors \(D_1,D_2\) on a
smooth projective threefold intersect with sole reduced support a
smooth curve \(T\), with cycle \(c[T]\). Put \(r,s\) for their exact
orders along \(T\), and \(A_1,A_2\) for their respective degrees on
\(T\). If a line bundle \(M\) of degree \(\lambda\) on \(T\) makes
\(N_{T/B}^{\vee}\otimes M\) nef (here \(B\) denotes the threefold), then
\[
 A_1s+A_2r\le \lambda c+(\deg N_{T/B}-\lambda)rs.        \tag{2}
\]
Indeed, after blowing up \(T\), the new strict intersection cycle \(Z\)
lies in \(E_2=\mathbf P_{\rm lines}(N_{T/B})\). Its degree over \(T\)
is \(c-rs\) by the plane blowup formula at the generic point. Put
\(\xi=c_1(\mathcal O_{E_2}(1))=-E_2|_{E_2}\). Intersecting the two
strict divisor classes with \(E_2\) gives
\[
 \xi\cdot Z=(\deg N_{T/B})rs-A_1s-A_2r .
\]
Here \(\pi_*E_2^2=-[T]\) and \(\deg E_2^3=-\deg N_{T/B}\).
The nef class \(\xi+\pi_{E_2}^*M\) pairs nonnegatively with the
entire cycle \(Z\), including any vertical fibers. This proves (2).
[Exceptional bundle convention](https://stacks.math.columbia.edu/tag/0FUT).

For the constant section, take \(\lambda=7-d\). The restriction
degrees are \(A_1=4a-7p\), \(A_2=4b-7q\), giving (1). For instance,
at \((3p,4q)\) retaining \(r=p\) forces
\((5-d)s\le(5-2d)q\). Thus a mixed direction forces a drop in the
first equation's order, and an endpoint with \(r=p\) requires \(3s\le q\).

### How much generic contact must occur deeper

Set \(\alpha=a/p,\ \beta=b/q,\ k=c/(pq)\), and put
\(A=4\alpha-7,\ B'=4\beta-7\). The boundary equation gives
\[
 \alpha\beta=4(k+1),\quad A+B'=7k,\quad AB'=15(k+1).
\]
Also \(5/4\le k\le2\). The lower bound follows from
\(\alpha,\beta\ge3\), and the upper from
\((\alpha-3)(\beta-3)=5(2-k)/4\).
Set \(x=r/p,\ y=s/q,\ z=xy\). Both \(x,y\) lie in \((0,1]\)
because the next multiplicity of a plane germ cannot exceed its starting
multiplicity. Equation (1) and AM–GM give
\[
 2\sqrt{15(k+1)z}\le Ay+B'x\le (7-d)k+dz .
\]
Since \(z\le1<k\) and \(d\ge2\), this implies
\(2\sqrt{15(k+1)z}-2z\le5k\). The left side is strictly increasing
on \((0,1]\). At \(z_0=k/2-1/4\) it exceeds \(5k\), since
\[
 60(k+1)z_0-(5k+2z_0)^2=-6k^2+21k-61/4>0 .
\]
The quadratic is concave and has values \(13/8\) and \(11/4\) at the
endpoints of the stated interval. Thus \(c-2rs>pq/2\).

After extending \(k(C)\) to its algebraic closure, all positive depths
belong to the subtree above the unique first direction. Its total
contact is \(c\) by Noether's intersection formula. Depth one
contributes \(rs\), and each later depth contributes at most \(rs\),
by the tangent multiplicity budgets in that subtree. Removing depths
one and two proves the asserted strict tail. For a mixed direction take
\(d=3\). The same increasing-function test, now with
\(2\sqrt{15(k+1)z}-3z\) at \(z=k/3\), gives
\(60(k+1)k/3-(4k+3k/3)^2=5k(4-k)>0\). Hence \(3rs<c\), and even
depths one through three cannot exhaust the subtree.
[Generic point-basis and per-depth argument](../arguments/residuals/generic_contact_depth.md#1-generic-normal-contact-tree).

## Limitations

In characteristic three, the known cubic–quartic pair has \(p=q=1\),
\(u=0\), and a single constant direction. On \(x_0=1\) write
\(x_1=t,\ x_2=t^3+X,\ x_3=t^4+Y\). Up to signs its equations are
\(X\) and \(Y^3-t^9X-t^3X^3-X^4\). These are smooth generic germs
with intersection length three, exhausted by three common simple
points of depths \(0,1,2\). Their powers give the same depth in
arbitrary multiples of the two degrees. The quadratic class displayed
above vanishes in characteristic three. This distinguishes the
characteristic-free connectedness from its characteristic-zero
deep-contact consequence on an actual supported pair.
[Positive-characteristic construction](../arguments/arithmetic/positive_characteristic_constructions.md#fixed-model-cubic-constructions-p-008-exact-positive-characteristic-presentations-of-the-monomial-quartic).

For \(u>0\), connectedness allows moving multisections, meeting
horizontal components and vertical fibers. Formula (2) applies if the
actual strict intersection is supported on a single smooth curve and
a nef twist of its normal bundle is established. A comparison for
intersecting components must also account for the strict transforms of
the other components. On \(u=0\) the remaining realization question is
whether the actual higher equations can sustain the required contact.
The lower tail bounds alone leave that question open. On the edge
\((3p,4q)\) the second contraction gives a
[two-way test on marked quintics in \(V_5\)](../arguments/residuals/blowup_residual_geometry.md#actual-equations-on-the-zero-direction-edge).

## Review

Independent review reconstructed the quadric vanishing and Koszul
argument, isolated-point lengths and connected-component attachment,
the ruling trace, the chart identification of the normal extension,
the second exceptional intersection with both sign conventions, and
the two strict tail estimates. Replaying
[the quadratic transition calculation](../computations/generalization_moving_first_relation_operator.py)
and evaluating \(D_u+\theta D_v\) at \(u=-\theta v\) reproduced
\(h_\theta v^2\) identically. Evaluating \(D_v\) at \(v=0\) reproduced
the missing direction. The characteristic-three comparison was also
checked by exact expansion on the cited global pair.
