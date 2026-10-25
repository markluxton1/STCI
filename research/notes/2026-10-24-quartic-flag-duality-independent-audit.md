# Independent audit of the quartic flag and duality package

Date: 2026-10-24. Reviewer role: `independent_audit`.

**Outcome: the consequential new propositions listed below are confirmed
in their stated characteristic-zero scope.** The global flag,
marked conormal product, scroll Gauss resolution, three full dual
intersections, and embedded endpoint contributions to the discriminant's
singular scheme have mathematical proofs. The explicit global primary
presentations and Hilbert polynomials also have exact computational
certificates. This is review of provisional intrinsic geometry, **not
canonical promotion**, and it has no STCI consequence.

The curve is exactly
\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k,
\]
where \(k\) is algebraically closed of characteristic zero. Claims about
characteristic two are identified separately below. Nothing here applies
unchanged to an arbitrary rational quartic or another projection center.

## 1. Independence, scope, and retained premises

The reviewer began with [INDEX](../INDEX.md) and the
[contribution checklist](../CONTRIBUTING_AGENT.md), then reconstructed the
bilinear flag, residual conormal equations, Gauss tuple, and discriminant
identities directly from the marked linear system, before reading the
authors' completed notes. The authors' proofs were then inspected for
globality, omitted nonreduced fibers, missing endpoint components, and
confusion between different ramification maps.

The exact premises retained without rerunning inherited proofs are:

- The merged [projection/group and symmetric-square
  synthesis](2026-10-24-quartic-automorphisms-bitangents-synthesis.md),
  including the embedded automorphism group, secant normalization, and
  trisecant fibers. These are independently reviewed provisional
  geometry, not numbered canonical results.
- The finite normalization of the primal cubic on \(\mathbb F_1\), with
  hyperplane \(H=E+2f\) and conductor section \(D=E+f\), from the
  [merged ruled-surface synthesis](2026-10-24-p4-ruled-surfaces-synthesis.md)
  and its cited independent audits. Its old normalization computation
  was not rerun.
- [R0020](../results/quartic_conormal_characteristic_jump.md), only for
  the already accepted normal/conormal splitting when it is mentioned.
  The new marked-product argument does not need to reprove it.
- The dual's reduced singular support of four components from the
  [earlier geometry audit](2026-10-24-special-lines-planes-geometry-audit.md).
  The new work refines its scheme structure.

No carrier-exclusion theorem, primitive-thickening classification, or
other STCI argument is a dependency. The reviewer did not consult older
conversation state as mathematical evidence.

The supporting notes reviewed are the
[flag note](2026-10-24-quartic-flag-incidence.md),
[conormal note](2026-10-24-quartic-conormal-residual-geometry.md),
[scroll note](2026-10-24-cubic-scroll-gauss-dual.md),
[intersection note](2026-10-24-quartic-dual-intersections.md), and
[singular-scheme note](2026-10-24-quartic-dual-singular-scheme.md).

## 2. The global flag and the two different branch constructions

Let \(U=H^0(\mathcal O_{\mathbf P^1}(2))\). Taking the missing middle
coefficient of the product of two quadratics gives
\[
b((a,b,c),(A,B,C))=aC+bB+cA.
\]
Its matrix has determinant \(-1\), including in characteristic two.
Thus the closed scheme \(\mathcal I=V(b)\) is the ordinary smooth
point-line flag variety after identifying its second plane with the
dual of the first by this specific pairing. This proves the isomorphism
on all divisors, not merely on pairs of distinct points. If the analogous
pairing for another system is degenerate, pairs of vectors in its left
and right radicals are singular points of the bilinear hypersurface;
that incidence cannot be the smooth flag variety.

The swap equalizer is the diagonal of the ambient product restricted to
\(\mathcal I\), hence its exact ideal there gives
\[
\operatorname{Fix}(\tau)=V(b^2+2ac).
\]
It is the smooth bitangent conic in characteristic zero. The equalizer
becomes a double line in characteristic two; smoothness of the ambient
flag does not force its involution's fixed scheme to be reduced.

Addition of degree-two divisors is finite flat of degree six over
\(\operatorname{Sym}^4 C\): properness and finite fibers give
finiteness, the smooth target and Cohen--Macaulay source give flatness,
and a reduced four-point divisor has six choices of the first pair.
Base change gives the same result for
\(\mu:\mathcal I\to\mathbf P(V)\). The monic-factor Jacobian is
the quadratic resultant; its vanishing divisor has class \((2,2)\).
At one double root there are two ramified marked factorizations and two
unramified ones, the latter keeping the double root in one factor.
Consequently
\[
\mu_*\operatorname{Ram}(\mu)=2[C^\vee]
\]
as cycles. In particular the surface where the **first quadratic is a
square** is not the ramification divisor. This distinction is essential
and is correctly retained in the final notes.

The boundary fiber lengths in the flag note are also correct. For a
root of multiplicity \(m\), choosing \(n\) of its multiplicity for
the first factor contributes local length \(\binom mn\); clusters
multiply. At a quadruple root the displayed algebra
\(k[a,b]/(a^3-2ab,a^2b-b^2)\) has length six and embedding dimension
two. Thus a one-point support is not a reduced fiber.

The group-action fixed loci were checked directly from the simultaneous
eigenspaces of \(b\): six torus-fixed flags, three disjoint lines for
the central involution or a reflection, no full-group fixed flag, and
the separate swap-fixed conic. The explicit combined equalizer
\(\operatorname{Fix}(\tau g)=\{x:g^2x=x,\ b(x,gx)=0\}\)
handles the exceptional fourth-root torus elements as stated. The
abstract flag automorphism group is not used in place of the embedded
curve's smaller automorphism group.

## 3. Conormal product and marked sections

The conormal incidence has first divisor \(D=2p\). In affine root
coordinates, if \(p=u\) and the residual quadratic is
\(A+Bz+Cz^2\), its equation in the flag is
\[
A-2uB+u^2C=0.
\]
Viewed as a quadratic equation in \(u\), the other root is a companion
\(v\), giving
\[
R(z)=z^2+\frac{u+v}{2}z+uv.
\]
This verifies the construction on a chart. Its global proof is the
universal incidence of a point on a smooth Veronese conic and a line
through that point: removing the recorded point from the degree-two
line section supplies the companion. Conversely a chord, including a
tangent when the two points coincide, supplies the line. Effective
Cartier residual makes the constructions inverse in families, so the
canonical marked isomorphism
\(N\simeq C\times C\) includes the diagonal and endpoints.

This product depends on the embedded system's polarity; it is not
deduced from an arbitrary choice of balanced splitting. Multiplying
\((z-u)^2R(z)\) gives the covector
\[
[u^3v:(u^3-3u^2v)/2:(v-3u)/2:1],
\]
whose homogeneous continuation has bidegree \((3,1)\). It has no base
point. Finiteness follows because a nonzero quartic has finitely many
multiple roots; a general dual plane has a unique double contact.
Thus this is the normalization of the sextic dual.

The residual map \(r:N\to\mathbf P^2\) is the symmetric-square
quotient in the companion coordinates, followed by a projectivity.
It is finite flat of degree two. Its branch conic is
\(B^2-AC=0\), and its ramification is the diagonal \(v=u\).
There the residual is \(z^2+uz+u^2\); multiplication gives precisely
the quadric-tangent covector. Thus \(\sigma_Q\) is this ramification
section. The osculating section is the different graph \(v=-u\),
and its residual is the paired divisor \(p+\iota(p)\).

Both sections have class \((1,1)\) and square two. They meet simply
at the two endpoints. Their dual images meet to order three at each
endpoint, as direct comparison of the covectors confirms. Neither this
marked product nor quadric polarity gives an isomorphism carrying
\(\sigma_Q\) to \(C\subset Q\), whose square is six.

The full third-contact divisor is
\[
T_3=\sigma_O+F_0+F_\infty\sim\mathcal O(3,1).
\]
The two endpoint fibers are indispensable. The fourth-contact ideal near
the first endpoint is
\[
(R(u),R'(u))=(u^2,v+5u),
\]
of length two, with the same result at infinity. This is also the
scheme intersection \(N\cap\operatorname{Fix}(\tau)\).
Finally the resultant of \((z-u)^2\) and \(R\) is \(R(u)^2\),
so the exact Cartier restriction is
\(\operatorname{Ram}(\mu)|_N=2T_3\). These statements correctly
distinguish ordinary curve involution, deck involution, and residual
swap, rather than identifying their different domains.

## 4. Gauss resolution and the second flag surface

On the retained primal normalization chart
\([1:r:rw:w^2]\), the primitive Gauss tuple is
\[
[rw^2:-2w^2:2w:-r].
\]
Globally its line bundle is \(2H-D=E+3f\), after removing the
conductor divisor from the pulled-back gradient system. Its only base
ideals are \((r,w)\) and the reversed endpoint ideal. One ordinary
blowup at each point resolves it. The moving class then has square
\((E+3f)^2-2=3\).

Substitution gives the irreducible cubic
\[
R^\vee=V(AC^2+B^2D).
\]
The general ruling parameter is recovered by \(w=-B/C\), then the
fiber coordinate is recovered, so the Gauss map is birational onto this
surface. Its image is not a curve. The resolved map contracts the
strict transforms of the two endpoint rulings; the exceptional blowup
curves map to the full endpoint pencil lines. These two elementary
transformations produce the dual finite-normalization scroll
\(\mathbb F_1\). Source conductor and negative sections exchange
their marked roles. The raw gradient ideal
\((C^2,BD,AC,B^2)\) and its saturation
\((B^2,BC,C^2,AC,BD)\) define the same projective singular scheme;
the latter makes its two embedded pinch-point additions explicit.

An independently reconstructed small bridge is useful. Let
\(L_\iota\subset\operatorname{Sym}^2C\) be the line of divisors
\(p+\iota(p)\). Restricting the first projection of the flag to this
line gives a ruled surface. With first factor \(1+z u^2\), its
second factor is \(A+Bu-Azu^2\), and multiplication is
\[
A+Bu+Bzu^3-Az^2u^4.
\]
Hence the restricted multiplication map is finite birational onto the
same dual cubic. This flag surface is smooth, therefore its finite
normalization. Its kernel bundle is
\(\mathcal O(-2)\oplus\mathcal O(-1)\), so it is precisely a
cubic scroll. The **same line** \(L_\iota\) parametrizes the primal
secants sweeping \(R\), and the flag surface parametrizes planes
containing these lines. Thus the primal and dual scroll constructions
have an actual common incidence origin. It does not identify the dual
of the singular projected cubic with the full dual of the smooth scroll
in its different ambient \(\mathbf P^4\).

## 5. Full intersection schemes

In dual coordinates put
\[
L=BC-4AD,\quad K=AC^2+B^2D,\quad M=AD-BC,\quad N=AC^2-B^2D.
\]
Independent expansion verifies
\[
\Delta=-4L^3-27K^2
       =4M(8AD+BC)^2-27N^2.
\]
Consequently the exact full homogeneous intersection ideals are
\[
(\Delta,K)=(K,L^3),\qquad
(\Delta,M)=(M,N^2),\qquad
(K,M).
\]
These identities retain every endpoint nilpotent; no inference from a
generic multiplicity is needed. The reduced complete intersection
\((K,L)\) is the osculating quartic and two endpoint lines. Its
generic reducedness follows by eliminating \(A\) on \(D=1\):
\(K=B(B+C^3/4)\) after imposing \(L=0\). The opposite chart
and the two remaining line points complete the support argument.
Being a complete-intersection curve, it has no embedded points and
is reduced. The full discriminant cut on the cubic is its triple
Cartier divisor, not the cube of its ambient ideal.

On the smooth dual quadric, Segre coordinates give
\[
[A:B:C:D]=[ac:ad:bc:bd],
\quad f=(as^3+bt^3)(cs+dt),
\]
and
\[
N=ab(bc^3-ad^3),\quad K=ab(bc^3+ad^3).
\]
Thus the discriminant cut on \(Q^\vee\) is twice the
quadric-tangent quartic plus the same two endpoint lines, each also
with multiplicity two. The cut by the dual cubic is reduced, with
the plus-sign quartic and the two lines, each once. The quartics
are smooth graphs, and each line meets the appropriate quartic in
length three at an endpoint. These complete Cartier factorizations
rule out omitted isolated components.

The notes correctly distinguish such full intersections from
same-point conormal traces. A generic plane on an endpoint line has
triple contact with \(C\) at the endpoint and quadric contact at a
different point. On the cubic it may be merely a limiting Gauss
plane at the singular pinch point. The plus-sign quartic in
\(R^\vee\cap Q^\vee\) likewise parametrizes contacts at different
smooth points. There is no common tangent plane at a point where both
primal surfaces are smooth: their intersection support is
\(C\cup L_0\cup L_\infty\), and direct comparison of the
two gradients excludes equality on each smooth part.

## 6. The singular scheme and its endpoint correction

The projective Jacobian ideal of the sextic is the gradient ideal
\(J=(\Delta_A,\Delta_B,\Delta_C,\Delta_D)\), with \(\Delta\)
redundant by Euler. At every nonquadruple triple-contact plane its
transverse model is a cusp; the Jacobian scheme has transverse length
two. At two distinct double contacts the transverse model is a node;
the Jacobian scheme is reduced. The restriction to the marked linear
system is transverse to the relevant root-multiplicity strata away
from quadruple roots, as the authors' coefficient differentiation
proves, including all endpoint-pencil members except their
quadruple-root plane. This yields degree sixteen, but **does not by
itself determine embedded points**.

The endpoint analysis supplies what the generic calculation misses.
On \(D=1\), the discriminant has weights \((4,3,1)\) in
\((a,b,c)\), weighted degree twelve. With
\(g_A=-\Delta_a/6,g_B=-\Delta_b/12,g_C=-\Delta_c/12\), and
\(h=(bc+8a)(ac^2+b^2)\), the stated \(4\times3\) matrix has
signed maximal minors \(9(g_A,g_B,g_C,h)\). The reviewer separately
checked its determinants and syzygies. Its height-two minor ideal
is perfect by Hilbert--Burch, so adjoining \(h\) removes all
embedded structure on this chart. The syzygies give
\(a h,b h,c h\in(g_A,g_B,g_C)\). Weight ten in that ideal is spanned
by \(c^2g_A,cg_B\), neither of which has an \(ab^2\) term,
whereas \(h\) has coefficient eight on it. Thus \(h\) supplies a
nonzero length-one embedded class at the endpoint. Since its class is
annihilated by the maximal ideal, nonvanishing also persists after
localization. Reversal gives the other endpoint. The nonquadruple
local models exclude additional embedded structure elsewhere.

The reviewer independently entered the sextic into Macaulay2, without
using the author's verifier, and obtained six associated primes:
four curve primes and the two hyperosculating point primes. The
unmixed ideal has Hilbert polynomial \(16n-45\); the full saturated
Jacobian has \(16n-43\). Their quotient has annihilator
\((B,C,AD)\) and constant Hilbert polynomial two. This corroborates
the two length-one pieces. These are exact algebra computations,
separate from the local proof above. The explicit primary presentation
in the singular-scheme note is appropriately labelled computational.

## 7. Evidence, precision corrections, and remaining boundaries

The review's independently authored replay is
[audit_quartic_flag_duality_2026_10_24.m2](../computations/audit_quartic_flag_duality_2026_10_24.m2),
with [saved output](../computations/quartic_flag_duality_independent_audit_2026_10_24_m2.txt).
It checks the two discriminant identities and ideal equalities, six
associated primes, Hilbert polynomials, endpoint annihilator, local
Hilbert--Burch determinants and syzygies, nonmembership, and weighted
Euler. Reproduce with

```sh
M2 --script research/computations/audit_quartic_flag_duality_2026_10_24.m2
```

The replay ran under Macaulay2 1.26.06 over \(\mathbf Q\) and passed.
During author/auditor exchange, the cubic singular ideal was refined
from raw gradients to its saturated homogeneous ideal, making the
embedded pinch-point structure explicit. The raw gradients already
defined the correct projective scheme; this precision correction
does not change its dual equation or Gauss geometry.

The final notes correctly preserve the following failed identifications:
the conormal surface is not the threefold cover's ramification divisor;
the marked quadric-tangent section cannot be matched to \(C\subset Q\);
the secant map is not injective over trisecants; full dual intersections
are not common-point traces; and ordinary, deck, and residual-swap
involutions are different operations. No unresolved proof gap was found
in the fixed characteristic-zero core reviewed here.

The characteristic-zero smooth-conic product construction fails in
characteristic two. There the doubled-divisor map is inseparable onto
a line, the conormal ruled surface is \(\mathbb F_2\), and its map
to the reduced dual is inseparable, so it is not the normalization.
These changes are consistent with the accepted splitting and the
direct first-jet equations in the conormal note. The fixed flag pairing
itself remains nondegenerate. The old Gauss resolution and ordinary
cusp calculations require a separate characteristic analysis and are
not transported by these checks.

Varying the projection center, descending all marked constructions
without the exceptional endpoint pair, and building a broader theory
of higher contact remain research questions. They are extensions of
the proved fixed setup, not unproved dependencies of its propositions.
No novelty claim, canonical theorem promotion, or STCI frontier closure
is supported by this audit.

## 8. Synthesis integration addendum, 2026-10-25

Recorded by the integrating author, following the independent reviewer's
final message. The reviewer read the main synthesis and found one actual
diagram error: an arrow from the ruling parameter curve directly to its
swept cubic surface claimed a morphism that the line family does not
supply. The corrected diagram displays the universal point-on-ruling
\(\mathbb F_1\), its projection to the ruling curve, its finite map to
the primal cubic, and the two-blowup Gauss resolution. Each displayed
arrow then has the stated morphism domain. This correction concerns the
synthesis diagram; the supporting scroll proof already retained those
domains.

The reviewer also confirmed the scheme equality
\(\tau(N_C)\cap\mathscr S=\tau(\sigma_O)\) for the second flag
surface. Its further intersection with \(N_C\) must not be identified
with \(T_4\) merely from equal endpoint lengths: their first-order
directions differ. The synthesis uses only the separately proved
equality \(T_4=N_C\cap\operatorname{Fix}(\tau)\). No new broader
claim is introduced by this integration addendum.
