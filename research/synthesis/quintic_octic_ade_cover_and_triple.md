# A quasi-étale cover and symbolic triple exclude globally ADE quintics

This is the full stronger degree-\((5,8)\) argument for the fixed embedded quartic. Its frozen source at `8e9a87a` and independent source audit accept the theorem as reviewed provisional mathematics. This consolidation retains the full proof and the audit’s distinct cover and numerical controls; independent preservation/integration review has accepted this replacement. No canonical promotion is made. The [surface-constraints account](quintic_octic_surface_constraints.md) retains the first-symbol geometry, the independent reduced-symbol/even-node proof, and the actual residual controls.

## 1. Exact statement and proof inputs

Let k be algebraically closed of characteristic zero and let
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\). There is no proper
intersection \(V(F_5,G_8)\) with reduced support exactly C for which
\(S=V(F_5)\) has only rational double points everywhere. No reducedness
assumption is made on either first-symbol divisor or their common divisor.
The assertion does not impose a singularity hypothesis on the octic.

Thus a hypothetical (5,8) STCI must have a quintic singularity outside the
ADE class somewhere, possibly away from C. This is a carrier-class exclusion,
not a complete exclusion of the degree pair or of unrestricted STCI.

We use the following inputs at their stated scopes:

- [R-0001](../results/quartic_carrier_exclusion.md), with its accepted
  lower-degree/factor reduction. In particular S is integral, and a quartic
  equation cannot have sole intersection support C with S.
- [R-0020](../results/quartic_conormal_characteristic_jump.md):
  \(E=N_C^*=\mathcal O(-7)^2\). The given genus/normal-layer calculation
  supplies generic length ten and \(L=\mathcal O(-q)\), \(q=5,6,7\).
  Its reviewed proof is retained in
  [the shared filtration and first-symbol proofs](quintic_octic_surface_constraints.md#1-filtration-data-and-the-three-numerical-rows).
  In particular the quintic first symbol is nonzero, with divisor degree q+6.
- The exact constant-direction quadratic cocycle in
  [the full embedded-triple calculation](../supplements/MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mf6-further-audit).
  Its embedded-triple calculation is independent of the final carrier degree.
  Section 6 below extends that calculation to this application; it does not
  import the later quartic-membership argument. The promoted
  [R-0033](../results/constant_first_relation_lifting.md) alone does not exclude
  positive-defect triples.
- Jaffe, [*Applications of iterated curve blowup to set theoretic complete
  intersections in P3*](https://arxiv.org/pdf/alg-geom/9410008), Theorem 4.1
  and Propositions 5.2, 5.3, 5.7, for the ADE smooth-curve pairs, first orders,
  local indices and rational-pullback corrections.
- Debarre, [*Inégalités numériques pour les surfaces de type général*](https://www.numdam.org/item/10.24033/bsmf.1965.pdf),
  Proposition 3.1 and Theorem 3.2, printed pp. 325–326, for the birational
  canonical-map inequality. This is not the stronger irregular-surface
  theorem whose proof is repaired in the
  [1983 addendum](https://www.numdam.org/item/10.24033/bsmf.1990.pdf).

Generic curvilinearity is not an extra hypothesis of this theorem. A globally ADE quintic is smooth at the generic point of C. There the quintic supplies one regular ambient normal parameter, so the length-ten transverse complete intersection is a quotient of a one-variable regular local ring and is curvilinear. The shared layer identities therefore apply.

The proof combines global surface invariants with the location, not only the
degree, of a saturated quadratic-layer defect. No total ordinary-torsion
upper bound is assumed or inferred from a first-order coefficient count.
One may descend a hypothetical pair and the finite data used below to a
finitely generated characteristic-zero field and embed it in C. The complex
surface arguments therefore suffice for the stated ground-field scope.

## 2. Three global budgets on the quintic

Let \(\pi:X\to S\) be the minimal resolution, and denote the pulled-back
hyperplane class by H. Since all singularities are ADE,

\[
K_X=H,\quad K_X^2=5,\quad \chi(\mathcal O_X)=5,
\quad p_g(X)=4,\quad q_{\rm irr}(X)=0,\quad h^{1,1}(X)=45.
\]

The independent negative-definite exceptional classes and H give
\(R_{\rm all}\le44\), where R counts exceptional curves. In particular
the rank \(R_C\) contributed by singularities on C is at most 44.
Singularities away from C can only consume additional rank.

The actual octic cuts the Cartier divisor \(10C\sim8H\) on S.
The strict transform \(\widetilde C\simeq C\) has square -6 by adjunction.
Its rational pullback is numerically \(\tfrac45H\). If \(\Delta_p\)
denotes the positive local correction to its square, then

\[
\sum_{p\in C}\Delta_p=\frac{16}{5}-(-6)=\frac{46}{5}.       \tag{1}
\]

Here \(\Delta_p\) is a resolution intersection number. It is not the
filtered-equation comparison invariant used elsewhere in the repository.

Let \(s_p\) be the vanishing order of the quintic first normal symbol in
its saturated direction. From its line-bundle degree,

\[
\sum_{p\in C}s_p=q+6.                                    \tag{2}
\]

The sums in (1) and (2) are supported precisely at singularities of S on C.
Repeated first-symbol zeros are permitted. Define the bookkeeping number
\(d_p=9s_p-10\Delta_p\); we use only
\(\sum d_p=9q-38\), not an identification of each d with another defect.

## 3. The forced double cover and its canonical map

The Weil divisor class \(T=5C-4H\) satisfies \(2T=0\) in \(\operatorname{Cl}(S)\).
It is nonzero. Otherwise \(5C\sim4H\) would give a section of
\(\mathcal O_S(4)\) with divisor 5C. It lifts to a quartic in P3 by
the hypersurface sequence and \(H^1(\mathcal O_{\mathbf P^3}(-1))=0\).
That quartic and S would have sole support C, contrary to R-0001 and its
factor reduction. Thus T has exact order two.

The reflexive algebra \(\mathcal O_S\oplus\mathcal O_S(T)\), with
multiplication supplied by \(2T\sim0\), defines a connected normal double
cover \(Z\to S\). If the associated quadratic function-field equation
were a square, T would be principal; thus the cover is connected. Its
algebra is S2 because both summands are reflexive on the normal surface,
and it is étale in codimension one, hence R1. This proves normality.
It is étale off finitely many singular points. Locally
an ADE point is a quotient of a smooth plane by a finite subgroup of SL2;
the nontrivial cover is the quotient by the kernel of the corresponding
order-two character. Hence Z again has only ADE singularities. A trivial
local class gives two copies of the original singularity. Away from C,
T is locally trivial, even at singular points of S.

Let W be the minimal resolution of Z. The canonical divisor pulls back
from \(K_S=H\), so W is minimal of general type with \(K_W^2=10\).
For a point where the cover is nontrivial, let r and r' be the exceptional
ranks of the base and cover. Define

\[
\epsilon_p=\frac{2r-r'+1}{12},\qquad
w=4\sum_p\epsilon_p.
\]

Euler characteristics give

\[
\chi(\mathcal O_W)=10-\frac w4.                           \tag{3}
\]

Indeed \(e(X)=55\), resolving a rank-r ADE point adds r to the Euler
characteristic, and a nontrivial local double cover has one point over the
singular point instead of two. Thus
\(e(W)=110-\sum(2r-r'+1)\); Noether's formula gives (3).
Locally trivial points, including every singularity off C, cancel from
this calculation.

There is a stronger restriction than Noether's inequality alone:

\[
w\ge16.                                                  \tag{4}
\]

To prove it, the invariant subspace of \(H^0(K_W)\) is exactly the
four-dimensional \(H^0(K_S)\). Descent of canonical forms holds on the
étale smooth locus and extends reflexively across the ADE points. Ratios
of these invariant sections recover the function field of the quintic S.
If \(p_g(W)>4\), a nonzero anti-invariant section has a noninvariant ratio
to an invariant section, generating the quadratic extension \(k(W)/k(S)\).
Consequently the full canonical map is birational.

Debarre's Proposition 3.1 applied to K gives
\(4p_g-6\le h^0(2K)=K^2+\chi\); equivalently
\(K^2\ge3p_g+q_{\rm irr}-7\). Since \(K_W^2=10\), this forces
\(p_g(W)\le5\) when the canonical map is birational. If \(p_g\le4\)
already, the same upper bound holds. Hence \(\chi(W)\le p_g+1\le6\),
and (3) proves (4). No assumption of regularity of W is made.

The canonical-map step cannot be replaced by Noether’s inequality alone. The numerical configuration \(3A_1^1+7A_4^1+A_9^3\) has \(\sum s=13\), \(\sum\Delta=46/5\), rank forty and \(w=8\). It satisfies the base budgets with \(q=7\); the cover values \(K^2=10,\chi=8\) are compatible with Noether when \(p_g=7,q_{\rm irr}=0\). It fails the stronger bound (4). This is an arithmetic control, not an asserted realization by a quintic.


## 4. Exhaustive ADE bookkeeping

At a point of C the local class of C has order dividing ten, because 10C
is Cartier. Write \(A_{N-1}^k\) for the smooth-curve pair with
\(1\le k\le N/2\). Its first order, pullback correction and local index are

\[
s=k,\qquad \Delta=\frac{k(N-k)}N,\qquad
\operatorname{ind}(C)=\frac N{\gcd(N,k)}.
\]

Thus its index is 2, 5 or 10. If the index is odd, T is locally trivial
and its contribution to w is zero. Otherwise the cover is
\(A_{N/2-1}\), giving contribution \(N/2\) to w.
The other allowed pairs and their cover contributions are:

| Pair | s | Delta | local index | nontrivial cover | contribution to w | rank |
|---|---:|---:|---:|---|---:|---:|
| D_n vector, n >= 4 | 2 | 1 | 2 | A_(2n-5) | 2 | n |
| D_n spin, even n >= 6 | n/2 | n/4 | 2 | D_(n/2+1) | n/2 | n |
| E7 | 3 | 3/2 | 2 | E6 | 3 | 7 |

D4's arms are equivalent and are covered by the vector row. Odd-D spin
and E6 pairs have indices four and three respectively and cannot occur.
There is no smooth-curve E8 pair. This uses the exhaustive smooth-curve
pair classification, not an assumption that only A-type points occur.

For the nontrivial A cover, write the base equation as \(xy=z^N\). The normal cover is \(XY=z^{N/2}\), with \(x=X^2,y=Y^2\) and deck involution \((X,Y)\mapsto(-X,-Y)\). Its only fixed point is the origin, and its type is \(A_{N/2-1}\), including a smooth cover when \(N=2\). This is the order-two character of the marked curve class, not an arbitrary double cover of the same surface.

The non-A cover identifications can also be checked directly. For the
D_n vector pair take \(x^2+y^2z+z^{n-1}=0\), \(C=(x,z)\), and
adjoin \(w^2=z\), \(x=wu\); the normal cover is
\(u^2+y^2+w^{2n-4}=0\). For the even spin pair take
\(C=(x,y+i z^{n/2-1})\), adjoin \(w^2=y+i z^{n/2-1}\), and
\(x=wu\); the cover is \(u^2+zw^2-2i z^{n/2}=0\).
For E7 use \(x^2+y^3+yz^3=0\), \(C=(x,y)\), and
\(w^2=y,x=wu\), giving \(u^2+w^4+z^3=0\). These equations also
identify the relevant local order-two class: in each displayed substitution the involution negates the square root and the new variable u, fixing only the origin. The normal hypersurface types are respectively \(A_{2n-5}\), \(D_{n/2+1}\) and \(E_6\); the weights follow from (3).

For bookkeeping, replace each allowed type by copies of five base types
as follows. These are arithmetic replacements, not asserted deformations:

| Actual type | Replacement | excess of actual rank |
|---|---|---:|
| A_(2c-1)^c | c copies of A1 | c-1 |
| A_(5c-1)^c | c copies of A4^1 | c-1 |
| A_(5c-1)^(2c) | c copies of A4^2 | c-1 |
| A_(10c-1)^c | c copies of A9^1 | c-1 |
| A_(10c-1)^(3c) | c copies of A9^3 | c-1 |
| D_n vector | 2 copies of A1 | n-2 |
| D_n spin, n even | n/2 copies of A1 | n/2 |
| E7 | 3 copies of A1 | 4 |

Each replacement preserves s, Delta, d and w, while weakly decreasing
rank. Exhaustiveness for A follows by writing N=rc, k=ac with
\(r\in\{2,5,10\}\), \(\gcd(r,a)=1\), \(a\le r/2\).
The five base rows have data:

| Type | s | d = 9s-10 Delta | w | rank |
|---|---:|---:|---:|---:|
| A1 | 1 | 4 | 1 | 1 |
| A4^1 | 1 | 1 | 0 | 4 |
| A4^2 | 2 | 6 | 0 | 4 |
| A9^1 | 1 | 0 | 5 | 9 |
| A9^3 | 3 | 6 | 5 | 9 |

Let their nonnegative multiplicities be x,y,z,u,v, and put h=x+v.
Equations (1) and (2) give

\[
u=3h+4z-8q+44,\qquad
R_0=244-36q+12h+16z\le R_C\le44,\qquad
w=x+5(u+v).                                             \tag{5}
\]

For q=5 the rank is at least 64, impossible. For q=6, nonnegativity of u
and the rank bound force \(3h+4z=4\), hence h=0,z=1,u=0,x=v=0,y=10.
This has w=0, contrary to (4). For q=7 they force
\(3h+4z\in\{12,13\}\). Nonnegative integer solutions are
\((h,z)=(4,0),(0,3),(3,1)\). Applying (4) leaves exactly:

| row | x | y | z | u | v | R0 | w |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| I | 1 | 3 | 0 | 0 | 3 | 40 | 16 |
| II | 0 | 1 | 0 | 0 | 4 | 40 | 20 |
| III | 1 | 3 | 1 | 1 | 2 | 44 | 16 |
| IV | 0 | 1 | 1 | 1 | 3 | 44 | 20 |

This small table follows directly from (5); it is not dependent on a
computer search. Each row has x at most one, so no non-A pair can occur
before replacement. Rows III and IV have no allowance for positive rank
excess and consist of precisely the displayed base points. In rows I and
II, some A4^1 or A9^3 copies may instead come from a single higher A-type
with c greater than one, provided the total rank excess is at most four.
The next calculation covers every such partition. Extra singularities
off C can only reduce the available excess.

## 5. The actual symbolic triple and its quadratic defect

The actual curve \(10C\subset S\) contains the symbolic triple
\(C_3=V(\mathcal I_{C/S}^{(3)})\subset S\subset\mathbf P^3\).
Its ideal is the contraction of the generic order-three ideal; this is the
Cohen–Macaulay, saturated triple, not a chosen model or ordinary third power.
Locally its ring is the image of \(\widehat{\mathcal O}_{S,p}\) in the
generic transverse ring modulo its third power. Its saturated first line
quotient is the same L as for Y: both are determined by the identical
generic direction and saturated kernel in E. Its last line is
\(L^2(D_2)\), with effective divisor D2 the zero divisor of multiplication
\(L^{\otimes2}\to L^2(D_2)\). This is a saturated-layer divisor, not
the ordinary-layer torsion or the first-symbol divisor.

For \(A_{N-1}^k\), write the completed surface-curve pair as

\[
uv+t^k v+t^{N-k}u=0,\qquad C=(u,v),\qquad k\le N/2.
\]

Over \(K=k((t))\), solve modulo u cubed:

\[
v=-t^{N-2k}u+t^{N-3k}u^2\pmod{u^3}.
\]

Put \(D=k[[t]]\). Since \(N-2k\ge0\), the exact image algebra has
D-basis

\[
1,\quad u,\quad t^{\min(0,N-3k)}u^2.
\]

Indeed u and the displayed v generate it; their products supply u squared,
and every further product is zero modulo u cubed. This proves the exact
local formula

\[
(D_2)_p=\max(0,3k-N).                                    \tag{6}
\]

At a smooth point of S the contribution is zero. Formula (6) gives one
at A1 or A4^2, and zero at A4^1, A9^1, A9^3. It also gives zero for every
larger A-type replacing A4^1 or A9^3 in rows I and II. Hence the four
survivors force respectively

\[
\deg D_2=1,\quad0,\quad2,\quad1.                         \tag{7}
\]

In row III the degree-two divisor consists of two distinct reduced points,
one A1 and one A4^2. They cannot merge: positive rank excess is forbidden.

## 6. The embedded-triple obstruction finishes the exclusion

All four rows have q=7, so \(E\twoheadrightarrow L=\mathcal O(-7)\)
has constant kernel direction in the balanced conormal frames. On the
chart \(x_0=1\), set

\[
U=x_3-z^4-\tfrac32z(x_2-z^3),\qquad V=x_2-z^3.
\]

For the kernel \(m=U+\theta V\), the exact second-order transition
obstruction, reused from the MF6 audit cited above, is

\[
h_\theta=3\theta^3z^{-5}-\tfrac32\theta^2z^{-4}
           +\tfrac34\theta z^{-3}-\tfrac38z^{-2}
       \in H^1(\mathcal O(-7)).                           \tag{8}
\]

For the remaining direction m=V, it is \(h_\infty=3z^{-5}\).
The original calculation uses the actual moving-coordinate transition,
including its quadratic terms; a first-order conormal transition alone
would not give (8).

If \(d=\deg D_2\), the nonzero multiplication section
\(\delta\in H^0(\mathcal O(d))\) must kill h in
\(H^1(\mathcal O(-7+d))\). This necessity applies to the actual saturated
triple even when it is nonprimitive or not a local complete intersection.
The retained Laurent coordinates of that cohomology group are
\(z^{-1},\ldots,z^{-6+d}\). Thus:

- For d=0, every h in (8), including the missing direction, is nonzero.
- For d=1, the coefficient matrix for \(\delta=a+bz\) has rows
  \((0,-3/8)\) and \((-3/8,3\theta/4)\), of determinant -9/64.
  The missing-direction matrix also has rank two. No nonzero delta exists.
- For d=2, rows 1, 2 and 4 of the three-column matrix have determinant
  \(-27\theta^4/32\). Therefore finite \(\theta\ne0\) is impossible.
  At \(\theta=0\), the sole section up to scalar is \(\delta=z^2\);
  at the missing direction it is \(\delta=1\) on this chart, which has
  a double zero at infinity. Consequently D2 must be twice one endpoint.

The two degree-two endpoint triples really are flat; they are not excluded
here. The contradiction is that row III requires two distinct points.
Rows I, II and IV fail the degree-one or degree-zero condition. Every
globally ADE quintic possibility has therefore been excluded.

## 7. Outcome, dependencies and remaining boundary

The full quintic first-symbol divisor may have repeated zeros: the proof has not assumed reducedness of it or of the common first-symbol divisor. The added force is the cover’s canonical map and the actual location of the symbolic triple’s saturated quadratic defect, rather than an upper bound on ordinary torsion totals. No hypothesis on octic singularities was inserted.

The theorem requires the quintic to be ADE **everywhere**. ADE only along C does not supply the resolution invariants, global cover calculation or canonical-map comparison used here. A normal quintic with a non-ADE singularity, possibly off C, and a nonnormal quintic remain outside this proof. The whole degree pair and unrestricted characteristic-zero STCI remain open; no neighboring degrees or positive-characteristic extension are asserted.

The [fixed-singularity account](quintic_octic_surface_constraints.md) preserves the invariant family \(G_8+F_5H_3\), its fixed common-singularity locus, the failure of Ellia’s primitive smooth-member hypothesis at that locus, the eight reduced-divisor budgets and the distinct even-node proof. Its actual homogeneous control has cycle \(5C+R\) and residual degree twenty; it neither realizes length ten nor constructs an STCI pair.

The proof uses R-0001 and its factor/lower-degree reduction, R-0020, the shared ordinary-layer/genus identities, Jaffe’s exhaustive ADE smooth-curve-pair data, Debarre’s birational canonical-map inequality, and the exact constant-direction moving-coordinate cocycle. The source audit independently reconstructed the cover’s connectedness and normality, all local cover types, rank domination, four-row arithmetic, symbolic-triple lattice and killing matrices. Its additional Noether-only numerical control is retained in §3. No new executable computation is needed. The inherited [degree-one/two triple checker](../computations/verify_mf6_defect12.py) supports the unchanged moving-chart calculation; no inherited certificate was rerun. The written determinants and local image algebra give the proof’s finite calculations.

The frozen source proof and audit are independently reviewed provisional evidence. Separate preservation/integration review has accepted this replacement, with no material finding. Neither that review nor consolidation promotes a canonical result.
