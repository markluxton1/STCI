# Residual curves as a corrected hyperplane test

The mechanism is to correct the hyperplane class until it has degree zero
on the known negative residual curves. Every other curve still has positive
degree, so this corrected class measures how much of an actual equation can
vanish along the inverse of the marked curve. The construction below is an
elementary nef-divisor argument, not a new general theory of nef cones.
The classical reference point is Zariski decomposition on a smooth projective
surface: its negative part has negative-definite intersection matrix and
is orthogonal to the nef part; see Thomas Bauer,
[*A simple proof for the existence of Zariski decompositions on surfaces*,
Theorem, p. 1, conditions (i)–(iii)](https://arxiv.org/pdf/0712.1576#page=1).
Here we prove only the special elementary correction for the specified
Cartier curves on a normal surface. We do not invoke a general decomposition
theorem on that surface or identify this correction as the Zariski
decomposition of the ample class \(H\).

A **proper containing form** means a homogeneous equation containing the
marked curve and sharing no surface component with the carrier. Unlike a
sole-support mate, it may have a residual intersection curve. All numerical
bounds below concern these actual forms, not arbitrary normal symbols.

## A reusable negative-curve correction

Let \(S\) be a normal integral projective surface over an algebraically
closed field, with an ample Cartier class \(H\). Suppose a nonzero section
\(q\) of \(\mathcal O_S(eH)\), \(e>0\), has complete divisor
\[
 \operatorname{div}(q)=\sum_i a_i\Gamma_i+\sum_j t_jT_j,
 \qquad a_i,t_j>0.
\tag{1}
\]
The curves listed are distinct. Assume every \(T_j\) lies entirely in the
regular locus of \(S\), and its intersection matrix
\(M=(T_j\cdot T_k)\) is negative definite. These curves are then Cartier,
and intersections with distinct effective curves are nonnegative. Put
\(h_j=H\cdot T_j>0\), and define
\[
 c=-M^{-1}h,\qquad P=H+\sum_j c_jT_j.
\tag{2}
\]
All \(c_j\) are strictly positive. Indeed \(-M\) is positive definite
with nonpositive off-diagonal entries. Its quadratic function
\(\frac12x^t(-M)x-h^tx\) has unique minimizer \(c\). Replacing the
negative coordinates of a vector by zero lowers this function: the removed
quadratic block is positive, the cross terms are nonnegative, and the
removed linear terms are positive. Thus \(c\ge0\). A zero coordinate
would make the corresponding entry of \((-M)c\) nonpositive, contradicting
\((-M)c=h>0\).

Consequently \(P\cdot T_j=0\), whereas \(P\cdot Z>0\) for every other
integral curve \(Z\): its hyperplane degree is positive and its intersections
with the \(T_j\) are nonnegative. Thus \(P\) is nef, with null curves
exactly the \(T_j\), and \(P\cdot H>0\). Equation (1) gives
\[
 \sum_i a_i(P\cdot\Gamma_i)=e(P\cdot H).
\tag{3}
\]
Even without a section \(q\), the correction (2) gives the following
inequality; (1) supplies the useful weight normalization (3).
For any nonzero section of \(\mathcal O_S(bH)\) with divisor
\(\sum_i r_i\Gamma_i+E\), where \(E\) is effective and contains no
\(\Gamma_i\), this proves the weighted capacity bound
\[
 \sum_i r_i(P\cdot\Gamma_i)\le b(P\cdot H).
\tag{4}
\]
Equality holds exactly when \(E\) is supported on the \(T_j\).
For fixed \(r_i\), its coefficients are uniquely determined by
intersecting with all \(T_j\), since \(M\) is invertible. Hence there
is at most one such section up to a nonzero scalar: two have the same
Weil divisor, so their ratio and its inverse are regular on the normal
surface and therefore constant by projectivity. This is uniqueness,
not existence of an equation with a proposed divisor.

If \(S\) normalizes an integral hypersurface and \(H\) is the pulled-back
hyperplane class, equality of two restricted degree-\(b\) forms means
polynomial equality modulo the carrier equation. If the curves \(\Gamma_i\)
lie over a marked curve \(C\) with residue degrees \(f_i\), the generic
intersection multiplicity is
\[
 m_C=\sum_i f_i r_i.
\tag{5}
\]
For completeness, localize at the generic point of \(C\). The finite
normalization quotient has finite length. Multiplication by a proper
form on that quotient has kernel and cokernel of equal length. The
normalization exact sequence therefore identifies the length downstairs
with the sum of the valuation lengths upstairs, weighted by the residue
field degrees. Thus (4) controls actual intersection multiplicity whenever
the weights \(P\cdot\Gamma_i\) are known relative to \(f_i\).

Negative definiteness, complete divisor (1), and regularity along every
test curve are substantive hypotheses. A residual curve merely occurring
on a quadric does not establish them. This construction is not asserted
for arbitrary singular or reducible residual schemes.

### Checking negativity from the two quadric rulings

There is a useful test beyond disjoint residual curves. Suppose the setting
comes from the marked quartic on its smooth quadric, with complete divisor
\(\operatorname{div}(q)=\Gamma+\sum_jT_j\sim2H\), all coefficients one.
Assume the strict residual curves lie in the regular locus, map birationally
to their images of bidegree \((\alpha_j,\beta_j)\) on the quadric, and
have verified simple attachments giving
\(\Gamma\cdot T_j=C\cdot T_j=3\alpha_j+\beta_j\).
Then the row sum of their intersection matrix is
\[
 \sum_k M_{jk}=2H\cdot T_j-\Gamma\cdot T_j
 =\beta_j-\alpha_j.
\]
If \(\alpha_j\ge\beta_j\) for all \(j\), and each connected component
of the intersection graph contains a strict inequality, then \(M\) is
negative definite. Indeed
\[
 x^t(-M)x=\sum_j(\alpha_j-\beta_j)x_j^2+
 \sum_{j<k}M_{jk}(x_j-x_k)^2.
\]
Vanishing forces a constant on each graph component and then forces that
constant to be zero. This verifies the hypothesis of (2) even for
intersecting residual curves with the stated regularity and attachment
properties. A whole balanced component instead gives a nonzero null
vector, explaining exactly why this negativity test fails there. No such
attachment or Cartier hypotheses are inferred merely from bidegrees.

## Sharp half-contact bound on the ordinary full-source open

Work in characteristic zero with
\(C=[s^4:s^3t:st^3:t^4]\), its smooth quadric \(Q=V(q)\), and the
[nonempty full-source open](carrier_test_curves.md#3-a-nonempty-dense-open-subset-of-every-full-actual-source-is-excluded)
of degree-\(a\), order-\(m\) carriers, \(m\ge1\), \(a\ge3m\).
Precisely, the normal root is a smooth irreducible degree-\(m\) cover
of \(C\). The quadric restriction is \(mC+T\), where \(T\) has class
\((a-m,a-3m)\); for \(a>3m\) it is smooth irreducible, and for
\(a=3m\) it consists of \(2m\) disjoint nonendpoint ruling lines.
All attachments to \(C\) are transverse and correspond to simple normal
roots. The cited construction establishes these conditions on a nonempty
open of the actual homogeneous source, not the entire abstract symbol space.

These carriers are integral without an additional rank computation.
Every homogeneous factor restricts nontrivially to \(Q\). A factor not
containing \(C\) would restrict to a divisor supported only on \(T\).
In the irreducible case its bidegree is a multiple of the unequal pair
\((a-m,a-3m)\); in the critical case all its components lie in one ruling.
Neither can equal \((d,d)\) for a positive-degree factor. Every factor
therefore contains \(C\), whereas irreducibility of the generic normal
symbol permits only one such factor, with multiplicity one.

On the finite normalization, let \(\Gamma\) be the prime over \(C\),
of residue degree \(m\). The normalization is regular along the strict
transform of \(T\). Away from \(C\), the smooth reduced quadric
restriction makes the carrier smooth. At an attachment the simple normal
root selects a smooth sheet; transversality gives a reduced intersection
with \(\Gamma\). In particular the complete quadric divisor is
\[
 \operatorname{div}(\nu^*q)=\Gamma+T\sim2H.
\tag{6}
\]
The restriction to \(Q\) is exactly \(mC+T\), with \(T\) not containing
\(C\), so the order-\(m\) symbol is nonzero on the quadric direction.
In the generic blowup chart its reduced separable degree-\(m\) root
therefore makes \(q\) a uniformizer on the inverse branch. It also has
order one along the reduced residual. Finite normalization adds no divisorial
components over isolated points.

For \(a>3m\), the known bidegrees and attachments give
\[
 H\cdot T=2a-4m,\qquad \Gamma\cdot T=4a-6m,
 \qquad T^2=-2m.
\]
The last equality is (6) intersected with \(T\). Thus the correction is
\(P=H+(a-2m)T/m\). At \(a=3m\), each disjoint line has
\(H\cdot L=1\), \(\Gamma\cdot L=3\), \(L^2=-1\), so
\(P=H+\sum L\). In either case (3) reads
\(P\cdot\Gamma=2P\cdot H\). A proper degree-\(b\) containing form
therefore has generic branch order
\[
 r\le\lfloor b/2\rfloor,\qquad
 \boxed{m_C\le m\lfloor b/2\rfloor,\quad
 \deg R\ge ab-4m\lfloor b/2\rfloor.}
\tag{7}
\]
This explains the factor one-half: the corrected class annihilates precisely
the residual part of the quadric divisor, leaving twice the hyperplane
capacity on the single inverse prime.

The bounds are sharp for every \(b\ge2\): take \(q^{b/2}\) when
\(b\) is even, and \(q^{(b-1)/2}\ell\) when \(b\) is odd, with
\(\ell\) a linear form not vanishing identically on \(C\).
No linear form contains this nondegenerate curve. In even degree every
equality form is proportional to \(q^{b/2}\) modulo the carrier: (4)
is equality, and the uniqueness statement after it applies to the known
section \(q^{b/2}\). The low odd-degree window is classified below; no general odd-degree
equality classification is asserted.
These are sharp quantitative bounds on the stated open, not on its special
closed complement and not on all possible carriers.

### An actual-source description of low odd-degree maximizers

There is also a limited odd-degree classification on this same open. Write
\(b=2r+1\), with \(1\le r\le m\). A proper containing form has maximal
branch order \(r\) exactly when it belongs to the actual source
\[
 q^{r-1}H^0(\mathbf P^3,\mathcal I_C(3)).
\tag{8}
\]
The word proper excludes a form vanishing on the carrier.

Indeed if a form of branch order at least \(r\) had ordinary generic
normal order \(d<r\), its nonzero first symbol of degree \(d<m\)
would have to vanish on the irreducible degree-\(m\) normal root. That
is impossible over \(k(C)\). Thus its ordinary order is at least \(r\),
and it lies in the ideal-sheaf power \(\mathcal I_C^r\) globally:
successive lower symbols are sections of vector bundles on the integral
curve and vanish if they vanish generically. For \(r\ge2\), restriction
to the quadric in degree \(2r+1\) has quotient
\(\mathcal O_Q(r+1,1-r)\), with no global sections. The
[quadric flag sequence](../equations/global_equation_jets.md#exact-homogeneous-equation-spaces-and-fixed-quadric-restrictions)
therefore divides every such form by \(q\), leaving
\(H^0(\mathcal I_C^{r-1}(2r-1))\). Iteration gives exactly (8).
Conversely \(q\) has branch order one, and every cubic through \(C\)
has branch order at least one. A proper form in (8) consequently attains
order \(r\), since (7) rules out a larger order. This describes all
proper cubic maximizers when \(r=1\); it makes no classification claim
for odd degrees greater than \(2m+1\).

## Related boundary mechanisms

For the squarefree split graded family, the same correction applies separately
to each normalization component; the [full application](carrier_test_curves.md#a-sharp-residual-bound-for-the-split-graded-family) retains distinct branch orders, odd-characteristic attachments and necessary descent constraints.
The [fixed-sextic boundary valuation proof](../../results/ci_fixed_sextic_jet_rigidity.md) gives a complementary weighted boundary inequality with an exact nonnegative loss identity. Neither mechanism is asserted for an unspecified carrier without its geometric or regular-function hypotheses.

## KG04: fix the quadric residual before varying the carrier

The ordinary full-source open above has irreducible \(T\) or disjoint
lines. The ruling test also gives new families with intersecting residual
components. The point is to **hold the residual section fixed** and vary
only the quadric-divisible part of the equation. That part controls the
normal direction, without changing the divisor on the quadric.

### An actual lifting lemma for fixed reduced residuals

Work in characteristic zero, with \(m\ge1\) and \(a=3m+u\), \(u\ge0\).
Fix a reduced divisor \(T\) of bidegree \((a-m,a-3m)\) on \(Q\)
that meets \(C\) transversely at smooth points of \(T\) away from the
endpoints. In particular no point of \(C\) is an intersection of two
components of \(T\). Let \(f_Q\) cut out \(C\) on \(Q\), and let \(t_Q\)
cut out \(T\). There is a degree-\(a\) ambient form \(F_0\) with
\(F_0\in H^0(\mathcal I_C^m(a))\) and
\[
 F_0|_Q=f_Q^m t_Q.
\tag{9}
\]
Indeed the three cubics restricting to
\(a_0^2 f_Q,\ a_0a_1 f_Q,\ a_1^2 f_Q\) span the quadratic sections in the
first ruling after dividing by \(f_Q\). Their \(m\)-fold products
give all sections of bidegree \((2m,0)\); multiply by ordinary degree-\(u\)
forms, which restrict onto the \((u,u)\) sections on \(Q\).
The resulting products span \((2m+u,u)=(a-m,a-3m)\).
This proves (9) using actual ambient equations.

Consider the affine space
\[
 F_0+q\,H^0(\mathcal I_C^{m-1}(a-2)).
\tag{10}
\]
There is a nonempty open in (10) whose carrier is integral, whose
generic normal root is the single smooth irreducible degree-\(m\) cover,
and whose normalization is regular along the strict residual curves.
Here are the separate checks.

1. **Root away from and on the quadric direction.** Because
   \(a-2\ge3(m-1)\), products of \(m-1\) actual cubic sections times
   ordinary forms generate the \((m-1)\)-st normal symbol bundle at
   every point, as in the [full-source construction](carrier_test_curves.md#3-a-nonempty-dense-open-subset-of-every-full-actual-source-is-excluded).
   For \(m=1\) use ordinary forms. On the ruled normal-direction surface,
   the projectivized linear system generated by the terms in (10)
   is therefore basepoint free off the \(q=0\) direction section.
   On that section the restriction is fixed up to scalar, and its
   only base points are the simple zeros of \(t_Q|_C\). The derivative
   along the section is nonzero at those base points for a nonzero
   \(F_0\) coefficient. Bertini gives smoothness elsewhere for a general
   member. The normal divisor has bidegree \((4a-7m,m)\), with both
   entries positive, hence is connected by the quadric cohomology
   sequence (the inverse twist has zero \(H^1\)). It is consequently
   smooth irreducible. At each base point the vertical derivative
   can also be chosen nonzero: the variation \(q\) times a generated
   \((m-1)\)-symbol changes exactly that derivative at the specified
   quadric direction. These finitely many nonvanishing conditions
   hold together on a nonempty open. This is the simple attached-root
   condition, distinct from smoothness of the whole normal divisor.
2. **Smoothness away from the marked curve.** The same ambient
   products for the correction in (10) have no base point off \(C\).
   Bertini applies off \(Q\), where \(q\) is nonzero. On \(Q\setminus C\)
   the carrier is smooth wherever \(T\) is smooth, by (9). At the
   finitely many singular points of the reduced curve \(T\), all off
   \(C\), the derivative normal to \(Q\) can be made nonzero by (10).
   Each such condition is the complement of a proper affine
   hyperplane, so the conditions hold simultaneously. Thus the
   carrier is smooth off \(C\).
3. **Integrality and the marked attachments.** A repeated factor would
   give nonsmooth points off \(C\). Two different surface components
   must meet in a projective curve; smoothness off \(C\) would force
   both to contain \(C\). Their nonzero initial normal forms would
   then factor the irreducible generic root, a contradiction. At a
   point of \(T\cap C\), blowing up the normal directions and using
   the simple root gives a regular sheet with parameters the base
   coordinate and the normal radial coordinate. Equivalently, in
   coordinates \(q=vw\), for \(v\) a parameter normal to \(C\) in
   \(Q\), the strict equation divided by \(v^m\) solves uniquely
   for \(w\) at this simple root. The resulting local branch is a
   smooth graph \(q=v\,w(t,v)\). It is one sheet of the finite
   normalization (use the corresponding simple factor in the
   completed local ring; normalization commutes here with completion
   by excellence). The curve \(T\) attaches to that sheet and
   meets its inverse curve transversely: \(v=0\) there is the
   inverse curve and has a simple zero on \(T\). Away from \(C\)
   the normalization is already an isomorphism along \(T\).
   Thus all strict residuals lie in the regular locus, not merely
   at their generic points.

Writing \(T_j\) for the strict residual components, the resulting
normalization has \(\operatorname{div}(q)=\Gamma+\sum T_j\);
the generic root is irreducible of degree \(m\) and does not meet the
quadric direction generically, so \(q\) has order one there. The
reduced quadric residual gives order one on every \(T_j\). There are
no other divisorial components, by finiteness of normalization.
The literal attachment counts are
\(\Gamma\cdot T_j=C\cdot T_j\) on \(Q\). Whenever the ruling
row-sum test above gives negative definiteness, the sharp bound
(7) and its equality reasoning apply on this new family as well.
The row-sum condition is only a sufficient test. The [weighted extension below](#weighted-fixed-quadric-residuals-arbitrary-effective-fixed-divisors) proves negative definiteness on the constructed open for every fixed effective \(T\) of the specified class, without componentwise ruling imbalance; it also verifies the needed Q-Cartier variant for repeated residuals.

### The degree-seven pilot, including the crossing

For \(a=7,m=2\), take \(T=L+D\), with \(L\) of class \((1,0)\) a
nonendpoint ruling and \(D\) a general smooth \((4,1)\) curve.
The ruled linear system can be chosen so that \(L,D\) each meet
\(C\) transversely away from the endpoints, their marked intersections
are disjoint, and \(L\cap D\) is a single transverse intersection
away from \(C\). This is just a \((4,1)\) very ample linear system
on \(Q\), with transversality and avoidance of finitely many specified
points. Hence (10) gives a nonempty family of actual integral carriers
with two intersecting strict residual curves. It is outside the
irreducible-residual open.

At the crossing, the carrier is smooth and \(q=0\) cuts out the two
transverse components, so \(L\cdot D=1\) on the normalization.
Their row sums are \(-1,-3\); with
\((H\cdot L,H\cdot D)=(1,5)\) this gives
\[
 M=\begin{pmatrix}-2&1\\1&-4\end{pmatrix},
 \qquad
 P=H+\tfrac97 L+\tfrac{11}{7}D,
 \qquad P\cdot H=\tfrac{113}{7}.
\]
Both components have degree zero against \(P\), although they meet.
For every proper degree-\(b\) equation containing \(C\),
\[
 m_C\le2\lfloor b/2\rfloor,\qquad
 \deg R\ge7b-8\lfloor b/2\rfloor.
\tag{11}
\]
These bounds are attained for every \(b\ge2\) by the quadric powers
(with a linear factor in odd degree) as in (7); even equality forms
are unique modulo the carrier and scaling. In odd degrees three and
five the actual-source description (8) also applies. This is a
verified application with intersecting residual curves, not a
description of all degree-seven carriers.


## Weighted fixed quadric residuals: arbitrary effective fixed divisors

The proposition below extends the fixed-residual lifting lemma and excludes every sole-supported mate on its constructed opens. It does not classify the exceptional complement or assert an unrestricted STCI obstruction. Work over an algebraically closed field of characteristic zero. Let

\[
 C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
 \qquad Q=V(q)\simeq\mathbf P^1\times\mathbf P^1,
 \qquad [C]=(1,3).
\]

Fix \(m\ge1\), \(a\ge3m\), and an effective divisor

\[
 T=\sum_{i=1}^n d_iT_i\quad\text{on }Q,
 \qquad d_i\in\mathbf Z_{>0},\qquad
 [T]=(A,B)=(a-m,a-3m),
\]

where the \(T_i\) are distinct integral curves and none equals \(C\). Write \([T_i]=(\alpha_i,\beta_i)\). Neither reducedness of \(T\), smoothness of its components, nor transverse or disjoint attachment to \(C\) is assumed.

### Actual carriers with this fixed restriction

**Proposition (weighted fixed-residual opens).** Under the hypotheses above, an actual lift \(F_0\in H^0(\mathcal I_C^m(a))\) of \(f_C^m t_T\) exists. For each fixed \(T\), consider the affine family

\[
 \mathcal A_T=F_0+qH^0(\mathcal I_C^{m-1}(a-2)).        \tag{W1}
\]

There is a nonempty Zariski open \(U_T\subset\mathcal A_T\) with the following properties.

1. The full normal root divisor is smooth and irreducible, and has degree \(m\) over \(C\). At every point of \(T\cap C\), the root in the quadric direction is simple.
2. The carrier \(X=V(F)\) is integral, and its singularities off \(C\) are isolated. At every singular point of the reduced support of \(T\) off \(C\), the carrier is smooth. This includes every intersection of distinct \(T_i\).
3. On the finite normalization \(\nu:S\to X\), every strict residual component is \(\mathbf Q\)-Cartier. At all residual attachment points over \(C\), and at all intersections of distinct residual components, the normalization is regular. Its complete pulled-back quadric divisor is

\[
 \operatorname{div}(\nu^*q)=\Gamma+\sum_i d_iT_i,
 \qquad [k(\Gamma):k(C)]=m.                           \tag{W2}
\]

Here and below the same notation \(T_i\) denotes the strict curve on \(S\). Its full residual intersection matrix is negative definite. Every carrier in \(U_T\) is excluded for **every** proper sole-supported mate degree: the sharp bound below gives

\[
 \deg R\ge ab-4m\lfloor b/2\rfloor
 \ge b(a-2m)>0\qquad(b\ge2).
\]

No linear form contains \(C\). Openness is asserted separately in **each prescribed affine family** \(\mathcal A_T\), with \(T\) fixed; no uniform open in the space of all liftings of a given bidegree is asserted. Exceptional lifts of the same \(T\) are not classified.

**Proof of existence and geometry.** There is an actual degree-\(a\) equation \(F_0\in H^0(\mathcal I_C^m(a))\) whose restriction to \(Q\) is \(f_C^m t_T\). This is the existing lifting argument: the three cubic restrictions divided by \(f_C\) span \(H^0(\mathcal O_Q(2,0))\); their \(m\)-fold products and restrictions of ambient degree-\(a-3m\) forms span \(H^0(\mathcal O_Q(a-m,a-3m))\). The remaining proof establishes the geometric properties and matrix; the corollaries derive the sharp bound and exclusion.

#### Why the stronger local conditions are available

The normal symbols of the correction source in (W1) generate the appropriate \((m-1)\)-symbol line bundle, since \(a-2\ge3(m-1)\). Thus the normal-root system is basepoint free away from the quadric-direction section. Its finitely many base points on that section are the support of \(T\cap C\). At each such point the correction changes the vertical derivative freely, so that derivative can be required to be nonzero. This works even if the fixed restriction has a multiple zero there; a nonzero derivative along the section is unnecessary. Bertini applies away from the base points. Smoothness at the base points follows instead from the chosen vertical derivative. The positive bidegree normal divisor is connected by the existing quadric-cohomology argument, hence smooth irreducible. For the fixed finite set \(\operatorname{Supp}(T|_C)\), each forbidden zero vertical derivative is a proper affine hyperplane in \(\mathcal A_T\). The complement of their finite union is nonempty over the infinite field. At a multiple zero the same vertical derivative condition suffices, with no requirement on the tangential derivative. Intersecting this open with the Bertini open gives the simultaneous conditions.

The correction source has no base points off \(C\). Bertini gives smoothness off \(Q\). On each residual component one can make the derivative normal to \(Q\) nonzero generically. One can also require it to be nonzero at the finitely many singular points of the reduced residual support off \(C\). Each requirement is a nonempty open condition on the actual correction space. On the rest of a component, its zeros are finite unless it is identically zero, which has been excluded. Consequently all remaining singularities off \(C\) are isolated and lie on just one smooth residual component. The zeros of the normal derivative along a repeated component need not be simple: generic nonvanishing already gives finite zero support. No first-jet transversality assertion is needed for this finiteness conclusion.

A repeated surface factor would produce a positive-dimensional singular locus off \(C\). If two distinct surface components existed, they would meet along a projective curve. Isolated singularities off \(C\) force that intersection curve to be \(C\), so both components contain \(C\). Their initial forms would factor the irreducible generic normal root. Both possibilities are impossible; the carrier is integral. An integral hypersurface is Cohen–Macaulay, hence satisfies S2. Its isolated off-\(C\) singularities satisfy R1, so it is normal off \(C\).

At an attachment, use coordinates \((t,v,q)\) with \(C=(v,q)\), \(Q=(q)\), and blow up using \(q=vw\). After dividing the carrier equation by \(v^m\), its derivative with respect to \(w\) at the attached root is a unit. Formal implicit solving gives a regular normalization sheet

\[
 q=v\,w(t,v).
\]

Since the divided equation at \(w=0\) is a unit times the local equation \(t_T(t,v)\), the implicit solution satisfies

\[
 w(t,v)=\text{unit}\cdot t_T(t,v).                   \tag{W3}
\]

This follows directly by writing the equation as \(g(t,v,0)+wU(t,v,w)=0\), with \(U\) a unit. Thus every residual component through this point belongs to that one sheet, and projection to the \((t,v)\) coordinates identifies its local equations and all intersection lengths with those on \(Q\). This includes multiple components, tangencies, singular residual branches, and shared attachments. The inverse curve on that sheet is \(v=0\). To identify this graph with the finite normalization, let \(\widetilde X\) be the strict transform in \(\operatorname{Bl}_C\mathbf P^3\). In either normal blowup chart its equation is obtained by dividing by the order-\(m\) radial power, and its restriction to the exceptional divisor is the normal symbol. At each \(p\in C\), its exceptional fiber is therefore the scheme-theoretic zero scheme on \(\mathbf P(N_{C/\mathbf P^3,p})\simeq\mathbf P^1\) of the degree-\(m\) binary form \(\sigma_m(F)_p\). This form is **nonzero**: off the attachments its value in the quadric direction is nonzero; at an attachment its vertical derivative is nonzero, even when \(T|_C\) has a multiple zero. Thus each such fiber is finite, of scheme length \(m\); off \(C\) the map is an isomorphism. The map is proper as a restriction of the blowup, hence finite by [Stacks Project, Lemma 37.44.1 (Tag 02LS)](https://stacks.math.columbia.edu/tag/02LS).

Regularity is needed at **all** points over \(C\), not only the distinguished attached roots. In a smooth blowup chart the strict-transform equation restricts on the smooth exceptional divisor to an equation for the entire smooth normal-root curve. Its differential along that divisor is nonzero at every point of the curve, so the strict-transform equation also has nonzero differential there. Thus \(\widetilde X\) is regular along the entire exceptional locus. It is normal off \(C\) by the preceding argument. This finite birational normal strict transform is the normalization \(S\), so the local graph above is on the actual normalization.

The Q-Cartier claim has three distinct local cases.

1. **Over \(C\):** the graph (W3) is regular and each residual curve is Cartier. The identity \(w=\text{unit}\cdot t_T\) retains multiplicities and shared or tangent attachments.
2. **Off \(C\), at a singular or intersection point of the reduced residual support:** the imposed nonzero derivative normal to \(Q\) gives a smooth graph over \(Q\), preserving residual ideals and intersection lengths. The residual curves are again Cartier.
3. **At any remaining isolated singularity off \(C\):** only one prime residual curve \(T_i\) passes. Its multiplicity in the quadric section is generically \(d_i\). Thus \(\operatorname{div}(q)=d_iT_i\) is an equality of **local Weil divisors on the normal surface**. The left side is principal Cartier, so \(d_iT_i\) is Cartier and \(T_i\) is Q-Cartier. This uses the actual divisor, not the illustrative example below.

All other residual points are regular, so each strict residual is globally Q-Cartier. The generic normal root misses the \(q=0\) normal direction because \(t_T|_C\ne0\) generically. On the \(q\)-radial blowup chart, \(q\) is a local equation for the reduced exceptional root divisor, so \(\operatorname{ord}_\Gamma(q)=1\). At the generic point of \(T_i\), its order is \(d_i\). Finiteness prevents additional divisorial components over isolated points. This proves the complete divisor identity (W2).


A useful local control is the normal surface singularity

\[
 qs-t^2=0.
\]

Its quadric-coordinate section \(q=0\) is twice the prime curve \((q,t)\). That curve is not generally Cartier at the vertex, but \(2T=\operatorname{div}(q)\), so it is \(\mathbf Q\)-Cartier. This explains why demanding regularity along every repeated residual would be unnecessarily strong. It is a local control, not a separately asserted global carrier construction.

### The full intersection matrix is negative definite

By (W3), the literal attachment counts are

\[
 \Gamma\cdot T_i=C\cdot T_i=3\alpha_i+\beta_i,
 \qquad H\cdot T_i=\alpha_i+\beta_i,
 \quad H=\nu^*\mathcal O_X(1).
\]

For \(i\ne j\), the local graph identifications give

\[
 T_i\cdot T_j=\alpha_i\beta_j+\beta_i\alpha_j.        \tag{W4}
\]

These are actual intersection lengths, not just presumed numerical classes on the normalization. All their common points lie in its regular locus. Intersecting (W2) with \(T_i\) gives the weighted row relation

\[
 \sum_jd_j(T_i\cdot T_j)=\beta_i-\alpha_i.           \tag{W5}
\]

Consequently, if \(M=(T_i\cdot T_j)\),

\[
 M=\alpha\beta^t+\beta\alpha^t
 -\operatorname{diag}\!\left(
 \frac{(B+1)\alpha_i+(A-1)\beta_i}{d_i}\right).
\tag{W6}
\]

No componentwise condition \(\alpha_i\ge\beta_i\) is required.

#### A Hodge-index proof on the smooth quadric

Put \(L=(A-1,B+1)\) on \(Q\). This is ample: \(A-B=2m\ge2\) and \(B\ge0\). For a nonzero real vector \(x\), set

\[
 D=\sum_i x_iT_i\quad\text{as a real divisor on }Q,
 \qquad N_x=\sum_i\frac{x_i^2}{d_i}(L\cdot T_i)>0.
\]

Formula (W6) says

\[
 x^tMx=D_Q^2-N_x.
\]

The classical Hodge index theorem ([Hartshorne, *Algebraic Geometry*](https://link.springer.com/book/10.1007/978-1-4757-3849-0), Chapter V, Theorem 1.9 and Remark 1.9.1, for real numerical divisors and the equality case), applied on the smooth quadric, and weighted Cauchy–Schwarz give

\[
 D_Q^2\le\frac{(D\cdot L)^2}{L^2}
 \le\frac{T\cdot L}{L^2}\,N_x.                     \tag{W7}
\]

Indeed the weights in the second inequality are \(d_i(L\cdot T_i)>0\). Now

\[
 L^2-T\cdot L=A-B-2=2m-2.
\]

For \(m>1\), (W7) is strictly smaller than \(N_x\), proving \(x^tMx<0\). For \(m=1\), equality in Cauchy–Schwarz would force \(x_i/d_i\) to be constant, hence \(D=cT\). Equality in Hodge would then require \(T\) numerically proportional to \(L\), unless \(c=0\). They are not proportional: \(A-B=2\), whereas \(L=(A-1,B+1)\) is balanced in this case. The zero constant would give \(x=0\). Thus equality is impossible for a nonzero vector here too. This proves negative definiteness in every case.

The Hodge theorem is used only on the smooth quadric, not on an unspecified singular surface. Rational self-intersections on the normalization are accommodated by the verified \(\mathbf Q\)-Cartier property.

### Sharp capacity and even-degree rigidity

**Corollary (sharp bound and all-degree exclusion).** For any carrier in \(U_T\) and any proper degree-\(b\) form containing \(C\), (W8) holds and is sharp for every \(b\ge2\). Its residual degree is positive, as stated in the proposition.

**Proof.** The existing negative-curve correction works unchanged for effective \(\mathbf Q\)-Cartier curves. Their intersections with distinct integral curves are nonnegative: a positive Cartier multiple has an effective local equation, whose restriction has nonnegative zero divisor. With \(h_i=H\cdot T_i>0\), set

\[
 c=-M^{-1}h,\qquad P=H+\sum_i c_iT_i.
\]

The established positive-definite matrix argument gives \(c_i>0\). Thus \(P\) is nef, vanishes precisely on the \(T_i\), and has strictly positive degree on every other integral curve. Equation (W2) implies \(P\cdot\Gamma=2P\cdot H\).

For any proper degree-\(b\) form containing \(C\), its divisor on \(S\) is \(r\Gamma+E\), with \(E\) effective and not containing \(\Gamma\). Therefore

\[
 0\le P\cdot E=(b-2r)P\cdot H,
 \qquad r\le\lfloor b/2\rfloor.
\]

The inverse prime has residue degree \(m\), so the normalization-length formula gives

\[
 \boxed{m_C\le m\lfloor b/2\rfloor,
 \qquad\deg R\ge ab-4m\lfloor b/2\rfloor.}           \tag{W8}
\]

For every \(b\ge2\), the bounds are attained by \(q^{b/2}\) for even degree and by \(q^{(b-1)/2}\ell\) for odd degree, with \(\ell\) not vanishing identically on \(C\). Properness follows because the integral carrier is not \(Q\). No linear form contains \(C\), so there is no containing degree-one case.

**Corollary (even-degree rigidity).** For \(b=2r\), equality in (W8) holds exactly for (W9), modulo the carrier equation and up to nonzero scalar.

**Proof.** If equality holds, \(E\) is supported on the residual curves. Intersecting with all \(T_i\) determines its coefficients uniquely, because \(M\) is invertible. Comparing with the known divisor of \(q^r\) gives \(E=r\sum_i d_iT_i\). The two sections have the same Weil divisor; their ratio is a global unit on the normal integral projective surface, hence a scalar. Consequently

\[
 G=cq^r+F H_{b-a},\qquad c\ne0,                     \tag{W9}
\]

with a negative-degree \(H\) understood as zero. Conversely (W9) restricts to the quadric power, which attains the bound. No general odd-degree equality classification beyond the previously stated low-degree window is asserted. The existing low odd-degree actual-source argument can be applied under its separate bound \(r\le m\); negativity alone does not extend that window.

### What this says already in carrier degrees four and five

For \(a=4\) or \(5\), the range \(a\ge3m\), \(m\ge1\), forces \(m=1\). The fixed quadric residual classes are respectively \((3,1)\) and \((4,2)\). Every effective fixed divisor of that class with no component \(C\) is allowed in the lifting construction above, including reduced configurations with opposite-ruling components and nonreduced configurations. A nonempty open of its actual affine lifting space has the verified hypotheses.

On these carriers,

\[
 \begin{array}{c|c|c}
 a& b\text{ even}&b\text{ odd}\ge3\\\hline
 4&\deg R\ge2b&\deg R\ge2b+2\\
 5&\deg R\ge3b&\deg R\ge3b+2
 \end{array}
\]

All bounds are sharp in these families, and every even maximizer is the quadric power modulo the carrier. This supplies a geometric residual-capacity statement; in degree four it does not supersede the stronger already-known exclusion of arbitrary quartic carriers. In degree five it concerns the specified nonempty lifting opens, not every quintic carrier.

### Scope and boundary of the extension

The extension removes the componentwise ruling-imbalance criterion and the reduced/disjoint residual restrictions. Total imbalance \(A-B=2m\), together with actual local identifications, controls the full weighted matrix. Repeated residuals may introduce normal singularities; their verified \(\mathbf Q\)-Cartier structure is the correct replacement for regularity along their entire support.

It does **not** infer these hypotheses from a bidegree alone on an arbitrary carrier. Outside the constructed open, the normal root may split or fail to be simple in the quadric direction; the carrier may fail to be normal off \(C\); the strict residuals may not be \(\mathbf Q\)-Cartier; or normalization may change intersections and inverse support. In such cases (W2), (W4), or the capacity weights can fail, and this proof gives no conclusion. Failure of a sufficient condition marks an exceptional lift for this proof; it is not automatically an obstruction to existence, nor evidence of an STCI. No exceptional cases are analyzed here. The characteristic-zero construction and the single inverse prime remain explicit hypotheses; no positive-characteristic or unrestricted STCI conclusion is asserted.
