# Fifth intervention: contact depth and unbalanced quadric families

Date: 2026-08-23

Operation: direct lead proof, family test, and strategic synthesis.

## Question and reason for selection

The corrected multisection analysis showed that a surface-effective threshold can force
contact to survive the first infinitely-near level. The next question was whether this
was an isolated rational-quartic accident or the first case of a general, presentation-
stable invariant.

The answer is general. The normalized generic intersection multiplicity is unchanged by
powering either defining equation, and a plane-curve contact tree of depth \(h\) can
contribute at most \((h+1)pq\). A surface-effective threshold therefore gives a lower
bound on contact depth. On unbalanced curves in a smooth quadric this lower bound is
explicit and unbounded, turning the rational quartic into the first nontrivial member of
a family rather than the endpoint of the argument.

## 1. Generic normal contact tree

Let \(C\subset\mathbf P^3\) be smooth and irreducible, and suppose
\[
  \sqrt{(F_a,G_b)}=I_C.
\]
At the generic point of \(C\), complete in the two normal directions and extend the
function field to an algebraic closure. The equations become plane power-series germs
\(f,g\) with no common component. Let
\[
  p=\operatorname{mult}_0(f),
  \qquad q=\operatorname{mult}_0(g),
  \qquad m=i_0(f,g).
\]
Their common infinitely-near points form a finite rooted tree. Give the origin depth
zero, and let \(h(F,G)\) be the largest depth of a common point.

For a common infinitely-near point \(P\), write \(p_P,q_P\) for the multiplicities of
the two strict transforms. At every fixed depth \(j\), the tangent-cone degree budgets,
iterated from the preceding level, give
\[
  \sum_{P:\operatorname{depth}P=j}p_P\le p,
  \qquad
  \sum_{P:\operatorname{depth}P=j}q_P\le q.                  \tag{1}
\]
Only common points are included, so discarding the other branches can only lower these
sums.

## 2. Contact-depth theorem

### Proposition

With the notation above,
\[
  \boxed{m\le(h(F,G)+1)pq.}                                  \tag{2}
\]
Consequently
\[
  \boxed{
  h(F,G)\ge
  \left\lceil\frac{m}{pq}\right\rceil-1
  =\left\lceil\frac{ab}{dpq}\right\rceil-1.
  }                                                           \tag{3}
\]

### Proof

Noether's intersection formula gives
\[
  m=\sum_P p_Pq_P,
\]
where the sum runs over all common infinitely-near points, including the origin. At a
fixed depth, multiplicity is nonincreasing along every path, so \(q_P\le q\). Equation
(1) therefore yields
\[
  \sum_{P:\operatorname{depth}P=j}p_Pq_P
     \le q\sum_{P:\operatorname{depth}P=j}p_P
     \le pq.
\]
There are \(h(F,G)+1\) occupied depths. Summing proves (2). The complete-intersection
cycle has \(ab=dm\), which gives (3).

The same proof gives a quantitative tail statement. For every \(0\le L<h(F,G)\),
\[
 \sum_{P:\operatorname{depth}P>L}p_Pq_P
 \ge m-(L+1)pq.                                               \tag{4}
\]
Thus a lower bound on \(m/pq\) controls not only the existence of deeper contact but
also the multiplicity mass that must survive.

## 3. Power invariance and surface thresholds

Define the normalized contact ratio
\[
  \kappa(F,G)=\frac{m}{pq}
             =\frac{(a/p)(b/q)}d.
\]
Replacing \((F,G)\) by \((F^u,G^v)\) multiplies \((a,p)\) by \(u\), \((b,q)\) by
\(v\), and \(m\) by \(uv\). Hence both \(\kappa(F,G)\) and the underlying contact-tree
depth are invariant under this artificial thickening. Unlike raw normal order, they do
not mistake powers for new geometry.

Suppose \(C\) lies on a smooth integral surface \(S\), is not an STCI on \(S\), and
has pair-compatible surface-effective threshold \(\tau_S(C)\). The component-exclusion
lemma makes both slopes at least \(\tau_S(C)\), so
\[
  \kappa(F,G)\ge\frac{\tau_S(C)^2}{d}.
\]
Combining this with (3) gives the contact-depth obstruction
\[
 \boxed{
  h(F,G)\ge
  \left\lceil\frac{\tau_S(C)^2}{d}\right\rceil-1.
 }                                                             \tag{5}
\]
More precisely, (4) says that the contact mass beyond depth \(L\) is at least
\[
  pq\left(\frac{\tau_S(C)^2}{d}-(L+1)\right)
\]
whenever the parenthesis is positive.

This is a necessary condition for every defining pair, not a non-STCI theorem. It is
also surface-specific until a useful containing surface and its component exclusion have
been established.

## 4. Smooth-quadric family

Let \(Q\simeq\mathbf P^1\times\mathbf P^1\) be a smooth quadric and let
\(C_{u,v}\subset Q\) be a smooth irreducible curve of bidegree \((u,v)\), with
\(u,v>0\) and \(u\ne v\). Then
\[
  d=u+v,
  \qquad g=(u-1)(v-1),
  \qquad H=(1,1).
\]
No positive multiple of \((u,v)\) is a multiple of \((1,1)\), so \(C_{u,v}\) is not
an STCI on \(Q\). If an order-\(p\), degree-\(a\) equation in a radical pair contained
\(Q\) as a component, the component-exclusion lemma would contradict this fact. Its
restriction to \(Q\) therefore yields the effective class
\[
  (a-pu,a-pv),
\]
and hence
\[
  \tau_Q(C_{u,v})=\max(u,v).
\]
Every hypothetical defining pair consequently satisfies
\[
 \boxed{
 h(F,G)\ge
 \left\lceil\frac{\max(u,v)^2}{u+v}\right\rceil-1.
 }                                                             \tag{6}
\]

For the rational family \(C_{1,n}\), \(n\ge2\), this simplifies to
\[
  \boxed{h(F,G)\ge n-1.}                                     \tag{7}
\]
Thus:

- the twisted-cubic numerical type \((1,2)\) requires at least one infinitely-near
  contact level, compatible with its familiar double complete-intersection mechanism;
- the rational quartic \((1,3)\) requires depth at least two, recovering and
  strengthening the preceding section/multisection exclusions; and
- the required generic contact depth grows without bound through the smooth rational
  curves \((1,n)\) on a quadric.

For \(n\ge3\), these curves are non-linearly-normal in \(\mathbf P^3\). The result does
not prove the linear-normality conjecture for smooth STCI curves, but it sharpens its
mechanistic content: any counterexample within this family would require defining
surfaces with generic normal contact of depth at least \(n-1\), not merely an unusually
singular first tangent cone.

For the rational quartic, (4) also shows that at least \(pq/4\) of normalized
intersection multiplicity lies strictly beyond depth one, because
\(m\ge(9/4)pq\) while the first two levels contribute at most \(2pq\).

## 5. Sharp local limitation

Arbitrarily deep contact is locally possible. The plane germs
\[
  f=y,
  \qquad g=y+x^N
\]
have \(p=q=1\), intersection multiplicity \(N\), and a single common chain attaining
the depth bound \(h=N-1\). Therefore (5) cannot become a global nonexistence theorem by
iteration alone. The missing input is global: degrees and line bundles of the successive
contact directions, proximity constraints inside the iterated exceptional ruled
surfaces, or a de-powering/APic mechanism that shortens an order-minimal pair.

This local example also explains why unbounded contact depth is not self-contradictory.
What is remarkable in the quadric family is that global surface geometry forces such
depth in *every* hypothetical homogeneous defining pair.

## Evidence boundary

- The contact tree is taken at the generic point of a smooth irreducible curve after a
  separable algebraic closure. Vertical exceptional components over finitely many closed
  points do not enter its generic depth.
- Noether's formula requires finite plane-curve intersection, which holds generically
  because the complete intersection is supported on \(C\).
- Formula (5) uses a smooth containing surface on which \(C\) is known not to be an
  STCI. It does not turn failure on that surface into global failure.
- The depth lower bound is necessary, not sufficient; the local example has no automatic
  homogeneous globalization.
- The quadric-family conclusion concerns every pair only after the component-exclusion
  argument; allowing the quadric itself as an equation would incorrectly lower the
  apparent slope.

## Research delta and strategic consequence

- **Power-invariant invariant:** \(\kappa=m/(pq)\) and contact depth survive powering,
  avoiding the principal presentation artifact in the thick branch.
- **General theorem:** a surface threshold gives the exact lower bound
  \(h\ge\lceil\tau^2/d\rceil-1\), with quantitative surviving contact mass.
- **Family consequence:** every hypothetical STCI pair for a smooth \((1,n)\) quadric
  curve has depth at least \(n-1\). Singular complexity would have to grow unboundedly
  along this non-linearly-normal family.
- **Interpretation:** the rational quartic resolves a general uncertainty by showing
  the first case where surface APic failure forces contact beyond one blow-up; it is not
  being treated as a proxy for all curves.
- **Next discriminating intervention:** globalize one surviving depth-two branch,
  carrying the proximity budget and line-bundle data simultaneously. In parallel, test
  whether order-minimal integral pairs admit any a priori upper bound on generic contact
  depth. Either result would distinguish a genuine thick-only mechanism from an
  indefinitely singular escape.

## Source boundary

The argument uses the classical Noether formula and elementary tangent-cone/proximity
budgets for plane curve germs, together with the component-exclusion and
surface-effective-threshold lemmas proved in the third intervention. The smooth-quadric
effective cone is elementary. No literature novelty claim is made; the contribution to
this research state is the integrated power-invariant formulation and its family-level
strategic consequence.
