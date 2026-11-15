# A quasi-étale cover and symbolic triple exclude globally ADE quintics

This is the full stronger degree-\((5,8)\) argument for the fixed embedded quartic. Its frozen source at `8e9a87a` and independent source audit accept the theorem as reviewed mathematics. This consolidation retains the full proof and the audit’s distinct cover and numerical controls; independent preservation/integration review has accepted this replacement. The [surface-constraints account](quintic_octic_surface_constraints.md) retains the first-symbol geometry, the independent reduced-symbol/even-node proof, and the actual residual controls.

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
  [the full embedded-triple calculation](quasiprimitive_residual_cycles.md#2026-10-05-mf6-further-audit).
  Its embedded-triple calculation is independent of the final carrier degree.
  Section 6 below extends that calculation to this application; it does not
  import the later quartic-membership argument. [R-0033](../results/constant_first_relation_lifting.md) alone does not exclude
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

The frozen source proof and audit are independently reviewed evidence. Separate preservation/integration review has accepted this replacement, with no material finding.


## Consolidated historical supplement: `research/supplements/DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md`

# Degree-five del Pezzo A4 model: intrinsic classification and explicit equations

Complete mathematical analyses with precise projection-center distinctions and conditional scope. Computational scripts remain in their original executable locations.

---

## 1. dp5 a4 intrinsic pair classification

# The entire degree-five A4 intrinsic pair, and the missing projection-center parameter

Date: 2026-10-11. Owner: `oct11_a4_intrinsic_model`.

Status: **DIRECT GEOMETRIC PROOF; EXACT SUPPORTING IDENTITIES**. The
contraction argument and the conic orbit argument were independently
obtained by `oct11_quintic_structural_frontier/quintic_conormal_audit`.
This note classifies the intrinsic pair in the genus-one quintic lane;
it does not exclude quintic mates, classify all conductor schemes, or
bound a descending power. Frozen records and the earlier evidence seal
were left untouched.

Hypotheses throughout: an algebraically closed field of characteristic
zero; the genus-one normalization S and smooth lifted quartic c in
[the frozen quintic frontier](quintic_conductor_geometry.md#1-quintic-conormal-and-delpezzo-audit),
with its independently checked
[A4 and unique-line reductions](quintic_conductor_geometry.md#1-quintic-conormal-and-delpezzo-audit).
Thus S is a normal degree-five anticanonical del Pezzo surface, its only
singularity is A4, `5c~4H`, and its unique degree-one line ell satisfies
`5ell~H`, `c+ell~H`. The resolution has a four-prime A4 chain, c meets
one interior vertex transversely, and ell meets the opposite interior
vertex transversely.

## 1. An intrinsic contraction proves that the plane marking is exhaustive

Let M be the minimal resolution. Label its exceptional chain

    R1--R2--R3--R4,

so that the strict c meets R2 and the strict ell meets R3. Both contact
points are nonnodes: each strict transform meets precisely one prime,
once transversely. The strict ell is a smooth (-1)-curve. Contract,
in order,

    ell#, R3, R2, R1.                              (1)

After ell# is contracted, R3 becomes a smooth (-1)-curve. After R3 is
contracted, R2 becomes a smooth (-1)-curve. After R2 is contracted,
R1 becomes a smooth (-1)-curve. The original distinct transverse
intersection directions ensure that each intermediate contraction is
the ordinary contraction of a smooth (-1)-prime, and that all the
remaining named primes remain smooth. No contraction of an entire
singular surface or an unproved simultaneous graph operation is used.

The self-intersection of R4 evolves as follows:

| Stage | Initial | After ell# | After R3 | After R2 | After R1 |
| --- | --- | --- | --- | --- | --- |
| Square of the remaining R4 | -2 | -2 | -1 | 0 | 1 |

The final surface is smooth rational with canonical square nine. The
classification of smooth minimal rational surfaces makes it P2: a
nonminimal rational surface has canonical square at most eight, and
the minimal ruled rational surfaces have square eight. The image of
R4, now a smooth rational curve of square one, is a plane line.

Reverse (1). The first center is on this line; the second is its
intersection with the first exceptional; the third is its intersection
with the second exceptional. The fourth is a point of the third
exceptional away from both its neighboring exceptional and the strict
line. These exclusions follow from the nonnode contact of ell# with
R3. They retain the entire possible family of fourth centers.

Choose plane coordinates [x:y:z], let p1=[0:0:1], and let the line be
y=0. In the affine chart z=1 the four-point cluster is

    (y-lambda x^3, x^4), lambda!=0.               (2)

The first two zero jets express the first three centers on the line;
the nonzero third jet expresses the free fourth center. A diagonal
projective change normalizes lambda to one. Therefore the familiar
plane model with local cluster `(y-x^3,x^4)` is **every intrinsic pair
under the stated hypotheses**, rather than only an example.

In the total-transform basis h,e1,e2,e3,e4,

    L=3h-e1-e2-e3-e4,
    R1=e1-e2, R2=e2-e3, R3=e3-e4,
    R4=h-e1-e2-e3, ell#=e4.                    (3)

The correction vector `(3,6,4,2)` for c gives

    c#=(4L-3R1-6R2-4R3-2R4)/5=2h-e1-e2.       (4)

Thus c becomes a plane conic tangent to y=0 at p1, whose nonzero
second-order coefficient ensures that it does not pass through p3.

## 2. All possible smooth conics form one orbit

The entire conic system in (4) is

    A yz+B x^2+C xy+D y^2=0.                    (5)

It gives the required smooth c precisely when `A B!=0`.
Indeed A=0 makes p1 singular or the conic reducible; B=0 makes the
conic reducible with y as a factor. For A B!=0 the conic determinant
is nonzero, its tangent at p1 is y=0, and its second-order coefficient
is nonzero. It passes through the first two centers and no later
center. This explicitly proves that smooth c do exist in the A4
surface; its divisor classes alone do not yield an impossibility.

Every plane projective automorphism preserving the cluster (2), with
lambda=1, has, after setting its z coefficient to one, the form

    x'=a x+b y,
    y'=a^3 y,
    z'=z+g x+d y,       a!=0.                  (6)

Origin and tangent-line preservation force the triangular shape;
preservation of the third jet gives `y'-scale=(x'-scale)^3`.
Conversely these matrices preserve the complete length-four cluster.
The exact transformation of the reference conic is

    y'z'+x'^2 =
      a^3 yz+a^2 x^2+(a^3 g+2ab)xy+(a^3 d+b^2)y^2.  (7)

After scaling (5) to A=1, choose `a=1/B`, and then choose g,d to
realize C,D; b can be arbitrary. Hence the cluster stabilizer acts
transitively on **all** the smooth conics (5). In particular the
intrinsic pair `(S,c)` is unique up to polarized isomorphism, and may
always be written with

    c_plane: yz+x^2=0.                           (8)

This is an exhaustion proof: the contraction first produces every
possible marking, then (7) treats every conic in that marking.

## 3. The exact residual automorphism group is a translation group

It is essential to retain the smaller automorphism group after c has
been normalized. An automorphism of S lifts to its minimal resolution,
preserves the unique line ell, and hence preserves R3. The A4 graph
then fixes every vertex. Consequently it preserves the sequence (1)
and descends to a plane automorphism of the cluster. There is no
unaccounted diagram reversal or Cremona transformation in this pair.

In (7), preserving the standard conic up to scalar forces

    a=1, g=-2b, d=-b^2.

Thus **the full automorphism group of the intrinsic pair is Ga**,
represented by

    x'=x+b y, y'=y, z'=z-2b x-b^2 y.             (9)

Parametrize (8) by `[x:y:z]=[st:t^2:-s^2]`. Equation (9) acts as
`[s:t]->[s+bt:t]`, namely translation of r=s/t. It fixes the point
t=0, which is the A4 point on c, and has no remaining scaling
parameter on the affine r-line.

## 4. Complete anticanonical formulas and actual Cartier sections

The entire anticanonical cubic system through the cluster has basis

    Z0=yz^2-x^3, Z1=xyz, Z2=y^2z,
    Z3=x^2y,     Z4=xy^2, Z5=y^3.              (10)

The four jet conditions on ten plane cubics give exactly these six
independent forms. On the smooth blowup this system is nef and big:
for a plane curve of degree m distinct from y=0, Bezout with y=0
gives `m>=m1+m2+m3`, while `m4<=m`. Hence its anticanonical
degree is `3m-sum mi>=m>0`. The strict y=0 and the first three
exceptional differences have degree zero and form precisely A4;
the fourth exceptional has degree one. The usual anticanonical
construction of a weak del Pezzo surface contracts exactly that
A4 chain. This is the same anticanonical embedding input already
verified in the frozen structural reduction, not a new claim that
an arbitrary rational surface is anticanonically embedded.

Use coordinates

    U0=Z5, U1=Z4, U2=Z3, U3=-Z1, U4=Z0-Z1,
    hsec=Z2+Z3.

Restrict (10) to `[st:t^2:-s^2]` and remove the common factor t^2.
Then

    c=[t^4:st^3:s^2t^2:s^3t:s^4:0].             (11)

This is the complete smooth rational normal quartic, including
t=0. The unique line ell is its tangent line at t=0, spanned by
the U3 and U4 coordinate directions. The hyperplane `hsec=0`
has actual divisor c+ell; the section U0 has actual divisor 5ell.
The latter can also be read from the fourth exceptional valuation
of y^3: order nine minus base order four equals five. Its remaining
plane support is y=0, which contracts to the A4 point. Finally

    Q=hsec^5/U0=y^2(yz+x^2)^5                   (12)

is an actual regular section of 4H with divisor 5c. On the plane,
the right side is a degree-twelve form and satisfies the required
fourfold cluster conditions; the divisor relation also proves its
regularity intrinsically. Neither U0, hsec, nor Q is assumed to
descend to any chosen four-coordinate projection.

The coordinate/model auditor is preparing
[a separate explicit-model audit](#consolidated-historical-supplement-researchsupplementsdel_pezzo_five_a4_intrinsic_and_explicit_modelmd).
Its global ideal and local A4 certificates are independent of the
geometric contraction exhaustion here.

## 5. Relative C0 projection centers have two lanes, one with a modulus

The fixed space-curve C0 is the projection of the complete rational
normal quartic from its deleted-middle-coordinate point. Under the
SL2-equivariant identification of points in its P4 span with binary
quartics, that center has two distinct double roots. Conversely any
such center is PGL2-equivalent to the deleted-middle center and
projects the curve to a projective equivalent of C0.

For explicit signs and binomial factors, in the affine coordinate r
of (11), send a point `p=(p0,...,p4)` to

    Phi_p(Z)=p0 Z^4-4p1 Z^3+6p2 Z^2-4p3 Z+p4.  (13)

The rational-normal point `(1,r,r^2,r^3,r^4)` maps to `(Z-r)^4`.
The deleted-middle point maps to `6Z^2` (the two roots are zero
and infinity, each of multiplicity two).

The actual intrinsic pair automorphisms (9) permit only translations.
Therefore the C0 projection centers divide as follows:

* **Endpoint lane:** one double root equals the fixed A4 point at
  infinity. Translate the other root to zero. There is one such orbit,
  represented by the deleted-middle point `(0,0,1,0,0)`.
* **Nonendpoint lane:** both double roots are finite. Translate their
  midpoint to zero and write them as `delta,-delta`, with
  `delta!=0`, modulo `delta->-delta`. A center representative is

      p_delta=(1,0,-delta^2/3,0,delta^4),
      Phi_p=(Z-delta)^2(Z+delta)^2.              (14)

There is **no residual scaling automorphism of `(S,c)`** that can
normalize arbitrary nonzero delta to one. Thus the deleted-middle
center exhausts the endpoint lane only. Investigating its four
projection-lift parameters alone cannot exclude all genus-one
quintic carriers.

The original projection to P3 has a line center in P5. It meets the
hyperplane span of c at p. Once p is fixed, the line extensions
outside that hyperplane form a four-parameter space. The nonendpoint
lane therefore retains delta as well as those four parameters.
Avoidance of S, finiteness, birationality, and the full inverse-support
condition are still required in both lanes. These orbit statements
concern the intrinsic curve projection only; they do not assert that
every line extension is an admissible normalization map.

## 6. Exact check record and remaining mathematical boundary

The supporting source
[verify_session_quintic_a4_pair_classification_2026_10_11.m2](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_quintic_a4_pair_classification_2026_10_11.m2)
passes **15 exact checks**: the cluster and conic transformations,
translation group, full rational-normal restriction, actual section
identity, A4 lattice and corrections, and the nonendpoint center
formula. Source SHA256:

    e710635b396707a6414fb142472db1ead3b17cfd06c1cb1ee18c4f64318108f2

The retained exact source supplies the lattice, conic, automorphism and center identities. Macaulay2 namespace failures contributed no mathematical argument.

The exhaustion argument is the written contraction proof in section 1,
not the fifteen symbolic checks. The quintic STCI question remains
open. The next actual task is the entire conductor descent of Q^k,
with k unbounded, in **both** projection-center lanes. All higher
normalization genera and normal quintics remain outside this note.


---

## 2. dp5 a4 explicit model independent audit

# An explicit degree-five A4 del Pezzo pair: independent coordinate audit

Date: 2026-10-11. Author: `quintic_conormal_audit`.
Status: **EXACT CONSTRUCTION AND INDEPENDENT GEOMETRIC AUDIT**.

This note verifies the anticanonical model and pair arising in the
sectional-genus-one quintic reduction. It does not exclude that lane or
establish an ambient mate. Earlier frozen audit notes are unchanged.
Work over an algebraically closed field of characteristic zero.

The inputs concerning a hypothetical mate are in the separately frozen
[quintic structural audit](quintic_conductor_geometry.md#1-quintic-conormal-and-delpezzo-audit):
the normalization is a degree-five del Pezzo surface with one A4 point;
the smooth quartic meets an interior A4 vertex; the unique degree-one
curve meets the opposite interior vertex. The coordinates below verify
the abstract model and pair. Placement of the subsequent P3 projection
center is a further parameter and is treated explicitly in Section 8.

## 1. The complete system and its length-four base cluster

Use plane coordinates [x:y:z], and put

    Z0=yz^2-x^3, Z1=xyz, Z2=y^2z,
    Z3=x^2y, Z4=xy^2, Z5=y^3.

There are no base points on z=0: Z0 forces x=0 there, and Z5 then
forces y=0. In the affine z=1 chart the common ideal is exactly

    (y-x^3,x^4).

Indeed xy becomes x^4 modulo y-x^3, and the remaining monomials are
in the resulting ideal. The base scheme is curvilinear of length four.
A plane cubic belongs to it precisely when its coefficients of 1,x,x^2
vanish and its x^3 and y coefficients sum to zero. Thus the six displayed
cubics are an actual basis of the complete cubic system through the
cluster, rather than a subsystem selected by a generic rank computation.

## 2. Four explicit simple blowups resolve the system

The successive main charts, after dividing by the exceptional factor at
each step, are:

| step | substitution | section vector |
| --- | --- | --- |
| 1 | y=xu1 | `(u1-x^2, xu1, xu1^2, x^2u1, x^2u1^2, x^2u1^3)` |
| 2 | u1=xu2 | `(u2-x, xu2, x^2u2^2, x^2u2, x^3u2^2, x^4u2^3)` |
| 3 | u2=xu3 | `(u3-1, xu3, x^3u3^2, x^2u3, x^4u3^2, x^6u3^3)` |
| 4 | u3=1+xu4 | `(u4, 1+xu4, x^2(1+xu4)^2, x(1+xu4), x^3(1+xu4)^2, x^5(1+xu4)^3)` |

The first three centers have coordinates (0,0); the fourth is
`(x,u3)=(0,1)`. In each alternate chart the transformed Z0 is a unit
on the exceptional divisor away from the indicated next center. At the
third step its unique remaining zero is u3=1, and at the fourth step
the transformed Z1 is a unit along the main exceptional chart. Thus
there are exactly four simple base points and no unresolved base scheme.

Let M be the resulting smooth four-point blowup, with total exceptional
classes e1,...,e4 and plane line class h. The complete polarization is

    L=3h-e1-e2-e3-e4=-K_M, L^2=5.

It is basepoint free. The map is birational: on y!=0 the ratios
`Z4/Z5=x/y` and `Z2/Z5=z/y` recover the plane coordinates. Its image
therefore has degree five.

The four contracted prime curves are

    E1=e1-e2, E2=e2-e3, E3=e3-e4,
    E0=h-e1-e2-e3.

They form the chain E1--E2--E3--E0, each with square minus two. The
first three centers lie successively on the strict line y=0; the fourth
lies on the third exceptional curve away from that line. E0 is the strict
line y=0. All four map to P0=[1:0:0:0:0:0]. The fourth exceptional
curve ell#=e4 is not contracted: its image is

    ell={Z2=Z3=Z4=Z5=0},

with parametrization [u4:1:0:0:0:0] in the main chart.

## 3. Five exact defining quadrics

In P5 the image ideal is generated by

    Z4^2-Z3 Z5,
    Z2 Z4-Z1 Z5,
    Z2 Z3-Z1 Z4,
    Z2^2-Z3 Z4-Z0 Z5,
    Z1 Z2-Z3^2-Z0 Z4.

The delegated Macaulay2 audit computed the exact elimination kernel,
not merely the ideal generated by quadrics that happen to vanish.
Its coordinate ring has dimension three, degree five and Hilbert series

    (1-5t^2+5t^3-t^5)/(1-t)^6.

There is also a direct cover proof of integrality and normality. In the
chart Z5=1 the equations solve exactly as

    Z4=r, Z3=r^2, Z2=t, Z1=rt, Z0=t^2-r^3.

That chart is A2. On the complement Z5=0 the reduced support of the
equations is ell. At a point of ell with Z1!=0, set Z1=1 and write
a=Z0,b=Z2,c=Z3. The equations give

    b(1-ac)=c^2, Z4=bc, Z5=b^2c.

Near ell the factor 1-ac is a unit. This solves the local ring as a
localization of k[a,c], so the surface is smooth at every point of
ell other than P0. The remaining P0 chart is handled exactly below.
These covers also rule out embedded boundary components.

## 4. The formal and algebraic A4 chart

Set Z0=1 and write a=Z1,b=Z2,c=Z3. The last two quadrics eliminate

    Z4=ab-c^2, Z5=b^2-c(ab-c^2).

The remaining ideal is generated by

    b(c-a^2)+ac^2.

The triangular polynomial change

    u=c-a^2, v=b+ac+a^3

has a polynomial inverse, and the equation becomes

    uv+a^5=0.

The polynomial uv+a^5 is primitive and irreducible as a polynomial linear in v over k[a,u], since gcd(u,a^5)=1. Thus the containing affine chart is integral, as required in the density argument.

This is an exact affine coordinate-ring isomorphism, hence also an
isomorphism of completed local rings. In characteristic zero its only
singular point is a=u=v=0. The image has exactly one A4 singularity,
at P0. The affine hypersurface is Cohen–Macaulay, hence S2, and is regular away from its single closed singular point, hence R1; it is therefore normal. The [exact local-chart checker](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_dp5_a4_local_chart_2026_10_11.m2) retains the polynomial identities, while the written density proof below supplies actual-image identification independently of a global-kernel computation.

The four explicit (-2) curves above give its minimal resolution;
crepancy follows from K_M=-L and K_S=-H. In particular the full
anticanonical model, its normality and its singularity are checked
directly, without assuming them from the name "del Pezzo".

The saturated projective Jacobian scheme is nonreduced of degree four.
The delegated exact computation obtains its ideal

    (Z5,Z4,Z3^2,Z2 Z3,Z2^2,Z1 Z2,
     Z0 Z2+2Z1 Z3,Z1^2-Z0 Z3),

whose radical is (Z1,Z2,Z3,Z4,Z5). The nonreduced Jacobian scheme is
retained; its degree is not a count of four singular points.

Put d=Z4 and e=Z5 in the Z0=1 chart. The polynomial inverse of the triangular change is c=u+a², b=v−au−2a³. The following direct density argument also identifies the actual image chart without relying on an elimination-kernel calculation.

### Actual image closure without an elimination-kernel assumption

The preceding computation could otherwise only describe a proposed
containing scheme. Here density identifies it with the actual image.

On the nonempty open subset `e != 0` of the integral five-quadric chart,
take source coordinates `y=1`, `x=d/e`, `z=b/e`. The first two relations
give `a=b d/e`, `c=d^2/e`. The remaining relations give

```
e^2=b^2 e-d^3,
z^2-x^3=1/e.
```

Therefore the source parametrization, divided by its nonzero Z0, is
exactly `[1:a:b:c:d:e]`. Thus the entire open subset `e != 0` is in the
parametric image. It is nonempty, for example at
`(a,b,c,d,e)=(0,1,0,0,1)`, and hence dense in the integral chart.

All five quadrics vanish on S, so its chart is contained in this
five-quadric chart. Conversely the dense open subset just exhibited lies
in S. Since S is the reduced image closure, its chart is the entire
integral five-quadric chart scheme. This proves the asserted actual
chart identification without appealing to an unverified global kernel.

## 5. The smooth quartic and tangent line

Choose the smooth plane conic

    yz+x^2=0.

It passes through the first two cluster centers but not the third.
Its strict transform has class c#=2h-e1-e2, square two, and L-degree
four. It meets E2 once away from the chain nodes. Thus its image c
meets A4 vertex two, while ell# meets vertex three.

The conic parametrization `[x:y:z]=[st:s^2:-t^2]` gives, after
removing the common factor s^2, the image

    c=[t^4-st^3 : -st^3 : -s^2t^2 : s^2t^2 : s^3t : s^4].

The five independent quartic monomials show directly that c is a
rational normal quartic in the hyperplane Z2+Z3=0. The delegated
kernel calculation additionally checks the exact scheme identity

    I_S+(Z2+Z3)=I_c intersect I_ell.

The saturated intersection ideal is

    I_(c intersection ell)=(Z2,Z3,Z4,Z5,Z1^2).

It has length two, supported at P0. Thus ell is exactly the tangent
line to c at the A4 point, rather than a second secant obtained only
by numerical intersection theory.

## 6. The distinguished section and useful affine coordinates

Put h0=Z2+Z3. On S its actual divisor is c+ell. The section Z5 has
actual divisor 5ell. This is visible on the fourth blowup chart:
Z5 has order five along e4, and its other plane zero components are
contracted. Therefore

    Q=h0^5/Z5 in H0(S,4H), div(Q)=5c.

The normality of S and the absence of poles make this a regular entire
section. In plane coordinates it is the homogeneous degree-twelve
polynomial `y^2(yz+x^2)^5`; its class is four times L. It is not being
asserted to be a polynomial in the four coordinates of a P3 projection.

The invertible linear change

    U0=Z5, U1=Z4, U2=Z3, U3=-Z1,
    U4=Z0-Z1, H0=Z2+Z3

puts the y!=0 chart, with r=x/y and T=z/y+r^2, in the form

    [U0:U1:U2:U3:U4:H0]
      =[1:r:r^2:r^3-rT:r^4-(2r^2+r)T+T^2:T].

Here c is T=0, ell is the line U0=U1=U2=H0=0, the A4 point is the
point r=infinity on c, and Q=T^5 in this trivialization. These affine
identities do not replace the omitted boundary or conductor checks.

## 7. The abstract pair is exhaustive after the marking audit

The separate intrinsic-model agent independently confirmed the following
classification argument; its dedicated note records that proof. Starting
from the accepted unique line, label the roots so c# meets E2 and ell#
meets E3. Contract successively

    ell#, E3, E2, E1.

Each is a smooth (-1) curve at its turn. The remaining root E0 has
self-intersection sequence -2,-2,-1,0,1. The resulting smooth rational
surface has Picard rank one and K^2=9, so is P2 with E0 a line. Reversing
the four contractions gives exactly three successive centers on that
line and a fourth free center on the third exceptional divisor, away
from its two chain nodes. Plane coordinates therefore give the cluster
`(y-lambda x^3,x^4)`, lambda!=0; scaling normalizes lambda to one.
The quartic strict transform becomes a smooth conic through the first
two centers, with equation

    yz+alpha x^2+beta xy+gamma y^2=0, alpha!=0.

All such conics are equivalent under the cluster stabilizer. Indeed
the projective substitution

    x'=a x+b y, y'=d y, z'=e x+f y+g z,
    d g^2=a^3

preserves the length-four cluster. Choose
`g=1,a=1/alpha,d=1/alpha^3,b=0,e=beta,f=gamma`.
Then `y'z'+x'^2=alpha^(-3)(yz+alpha x^2+beta xy+gamma y^2)`.
This verifies the orbit calculation directly. Thus the displayed model
exhausts the abstract admissible (S,c) pair, conditional on the accepted
upstream A4 and unique-line reduction. It does not yet exhaust the
chosen P3 projections of that pair.

## 8. Projection-center scope: a required additional distinction

The coordinates in Section 6 fix the intrinsic A4 point at r=infinity.
Choosing restriction space `span(1,r,r^3,r^4)` puts the P4 center at
the omitted-middle-coordinate point. Its binary quartic has two double
roots at zero and infinity. Relative to the A4 point, this is the
endpoint placement of the fixed C0 projection.

For the entire fixed-C0 quintic lane, the center must instead be allowed
to range through the PGL2 orbit of this two-double-root binary quartic.
The automorphisms of the pair preserve the A4 point. In the plane model
their action on c is translation r->r+a; the conic-preserving projective
substitution can be chosen as

    x'=x+a y, y'=y, z'=z-2a x-a^2 y,

which fixes T. A pair of finite double-root points therefore has a
remaining separation parameter up to interchange, whereas a pair
containing infinity has a single translation orbit. The independent
intrinsic-model note owns the full automorphism and center-orbit proof.

Consequently four coefficients for lifting the fixed space
`span(1,r,r^3,r^4)` through the one-dimensional restriction kernel are
only the endpoint projection sublane. They must not be advertised as
an exhaustion of all A4 quintic carriers. The nonendpoint placement,
center avoidance, finite birationality, full inverse support and descent
of every possible Q^k remain separate requirements.

## 9. Evidence and continuation

The independent global-kernel and local-chart Macaulay2 agents preserve
their exact sources, raw output, failed scaffolds and execution records
under distinct new October 11 paths. This note records direct geometric
proofs and does not count a child execution again as a new verifier.
The exact logs distinguish degree four of the Jacobian scheme, length
two of the curve-line intersection, and degree five of S.

The next mate question is genuinely global: whether a permitted P3
projection can make any Q^k descend through its entire conductor while
retaining full inverse support over C0. Neither a successful local A4
chart nor the unique abstract pair supplies that descent or bounds k.



## Consolidated historical supplement: `research/supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md`

# October 9 historical mathematics

This compilation retains the mathematical hypotheses, counterexamples, unsuccessful arguments, and open questions. This compilation supplies no new independent audit.

---

## Source: 2026-10-09-session-A3-two-A1-projection-family.md

# A uniformly excluded A3+2A1 family containing fixed C0

Date: 2026-10-09. Author: `normal_global_adversarial`.
Status: **PROVED HERE for the displayed family**, characteristic zero.
Every member below is an integral quartic containing fixed C0 with
normalization singularity type A3+2A1, and admits no mate of any degree.
The family does not exhaust every pair or middle-coordinate projection
in this ADE stratum. No frontier file is edited.

## 1. The normal anticanonical model

In P4[a:b:c:d:e], let

    S=V(ab-c^2, cd-e^2).

The two equations form a complete intersection. On c nonzero it is
integral: a,b are nonzero, b=c^2/a and d=e^2/c. The closed set c=0
has also e=0 and ab=0, and has affine-cone dimension two, smaller
than the three-dimensional complete intersection. Thus no component
is contained there. The complete intersection has no embedded
components and is generically reduced, so its ring is a domain.

The Jacobian drops rank exactly at the three coordinate vertices a,b,d.
On the a chart the local equation is cd=e^2, an A1 point; the b chart
is identical. On d=1, eliminate c=e^2 and obtain ab=e^4, an A3 point.
All singularities are isolated, so the complete intersection is normal
by S2 and R1. Its degree is four and its dualizing sheaf is O_S(-1).

## 2. A rational normal quartic and the actual coordinate change

Choose parameters alpha,beta,gamma,delta with

    gamma delta Delta nonzero,       Delta=alpha delta-beta gamma.

Set D0=gamma s+delta t and N0=alpha s+beta t. The five binary quartics

    a=s^2 D0^2,       b=t^2 D0^2,       c=st D0^2,
    d=st N0^2,        e=-st D0 N0

satisfy both equations of S. Their coefficient matrix in the basis
(s^4,s^3t,s^2t^2,st^3,t^4) has determinant

    gamma^2 delta^2 Delta^3.

It is invertible, so the curve is a rational normal quartic. Explicitly
the projective coordinate change from Y0,...,Y4 is

    a=gamma^2 Y0+2gamma delta Y1+delta^2 Y2,
    b=gamma^2 Y2+2gamma delta Y3+delta^2 Y4,
    c=gamma^2 Y1+2gamma delta Y2+delta^2 Y3,
    d=alpha^2 Y1+2alpha beta Y2+beta^2 Y3,
    e=-alpha gamma Y1-(alpha delta+beta gamma)Y2-beta delta Y3.

At t=0 the curve meets the a A1 vertex, at s=0 the b A1 vertex, and
at D0=0 it meets the d A3 vertex. These are three distinct parameters
by gamma delta Delta nonzero. Deleting Y2 projects the curve to exactly

    C0=[s^4:s^3t:st^3:t^4].

## 3. Finite birational quartic projection and every extra fiber

Let p be the projection center Y2. In the a,b,c,d,e coordinates,

    p=(delta^2,gamma^2,2gamma delta,2alpha beta,-M),
    M=alpha delta+beta gamma.

For Q1=ab-c^2 and Q2=cd-e^2,

    Q1(p)=-3gamma^2 delta^2,       Q2(p)=-Delta^2.

In particular p lies outside S, and the projection is finite. Let
T_i be the derivative of Q_i in the omitted Y2 direction, restricted
to the rational normal quartic. Direct expansion gives

    T1=D0^2(gamma^2 s^2-4gamma delta st+delta^2 t^2),
    T2=-2Delta^2 s^2t^2.

The member Q1(p)Q2-Q2(p)Q1 has zero Y2^2 coefficient and linear
coefficient along the curve

    L_c=Q1(p) T2-Q2(p) T1
       =Delta^2 P4,
    P4=gamma^4 s^4-2gamma^3 delta s^3t
       -2gamma delta^3 st^3+delta^4 t^4.

This is nonzero, so the projection is birational on the nonempty
linear-coefficient open. Its integral image has degree four by the
hyperplane degree formula, and S is its finite normalization.

The endpoint coefficients of P4 are nonzero. Every zero therefore has
st nonzero, where T2 is nonzero. At such a point the projection-line
equations have, besides the displayed curve point, a distinct second
point of S: simultaneous coincidence would require T1=T2=0.
Equivalently, on the line c(s,t)+lambda p the restrictions are

    Q_i=lambda T_i+lambda^2 Q_i(p),

and L_c=0 supplies the common root
lambda=-T2/Q2(p)=-2s^2t^2, which is nonzero. Since the first curve
point projects isomorphically onto C0, this second point lies off it.

In fact P4 has four distinct roots. With r=gamma s/(delta t), its
affine polynomial is r^4-2r^3-2r+1, of discriminant -1728. The
four distinct extra points occur in four distinct fibers. Generic
uniqueness above C0 means no second curve component lies over C0;
these are isolated extra points of the full reduced inverse image.

A pulled-back mate section would have zero support exactly that
inverse image. On the integral surface its nonzero local equations
cannot have isolated zeros, so this is impossible. Every displayed
quartic is excluded for every positive mate degree.

## 4. Scope and exact control

Alpha or beta may be zero; only gamma delta Delta is required nonzero.
The determinant and all projection calculations are universal in these
parameters. They are checked in the independent
[uniform projection checker](https://github.com/markluxton1/STCI/blob/3a50e7675d965bd5fa15084189aaab750620bca3/research/computations/verify_session_genus_one_projection_2026_10_09.py).

This construction binds one three-parameter family of pairs to the
specific deleted-middle-coordinate projection. It does not identify
every admissible projection of an A3+2A1 pair. Parameter changes moving
the three singular passages also transform the projection center;
see the [uniform adversarial note](../supplements/GENUS_ONE_UNIFORM_PROJECTION_ANALYSIS.md).
The global C0 problem and the complete A3+2A1 projection stratum remain
open at this record's scope.

---

## Source: 2026-10-09-session-a1-singular-conductor-parity-shield.md

# An A1 point invalidates smooth-conductor valuation parity

Date: 2026-10-09. Author: `singular_local_lift`.
Status: **PROVED HERE**, local/affine only. This is not a projective
mate for the fixed C0 and does not resolve the global STCI problem.
It protects the entire ADE conductor lane against applying the
smooth elliptic-conductor parity proof at an ADE point.

Work over an algebraically closed field of characteristic zero. Put

    B=k[l,x,z]/(x^2+lx-z^2),
    w=lx,
    A=k[l,z,w]/(F),
    F=w^2+l^2w-l^2z^2.

The discriminant of F as a polynomial in w is l^2(l^2+4z^2), which
is nonsquare in k(l,z). Thus A is an integral affine hypersurface
of polynomial degree four. The ring B is a quadric cone with its
only singular point at the origin: the gradient of its equation is
(x,2x+l,-2z). It is Cohen--Macaulay and regular in codimension one,
hence normal, and the nondegenerate quadratic singularity is A1.

The map A->B is finite, since x^2=z^2-w and B=A[x]. It is
birational, since x=w/l in the common fraction field. Normality
therefore makes B exactly the normalization of A.

The actual conductor can be calculated without a support guess.
As an A-module B has generators 1,x and the complete presentation

    [ -w       l(z^2-w) ]
    [  l          -w   ].

To see completeness, first impose the monic relation x^2=z^2-w,
then generate the ideal of lx-w in the free basis 1,x. Its two
coefficient columns are exactly those displayed. The determinant
is F. Modulo the submodule generated by 1 this gives

    B/A=A/(l,w),
    Ann_A(B/A)=(l,w).

Thus the downstairs conductor is the entire smooth affine line
Gamma=Spec k[z], and upstairs its ideal is (l,w)B=(l). The actual
upstairs conductor is

    D=Spec k[x,z]/(x^2-z^2).

It is a node with two branches, passing through the A1 point of B.
The map D->Gamma is finite flat of degree two: its algebra is free
over k[z] with basis 1,x and x^2=z^2. Its global trace involution
fixes z and sends x to -x.

Let c=V_B(x,z). It is a smooth affine line with coordinate l and
passes through the A1 point. Its image is the smooth embedded line
C=V_A(z,w), also with coordinate l, and c->C is an isomorphism.
At the generic point of c, l is a unit and

    x=z^2/(x+l),

so the Weil divisor of Q=x is exactly 2c. There is no other prime
in its zero support because B/(x)=k[l,z]/(z^2).

The curve c is non-Cartier at the origin: the ideal (x,z) has two
independent degree-one generators modulo the maximal ideal times
that ideal. Its local divisor class has exact order two.

On D, the section q=Q|D is anti-invariant under the actual trace
involution. On its two normalized branches x=z and x=-z, its
vanishing order is one in both cases. This does not contradict
div_B(Q)=2c, because c is non-Cartier at the A1 point where D meets
it. A local equation for c whose square represents Q does not
exist there. The smooth-surface parity argument cannot be applied.

Indeed the square does descend and even supplies an affine mate:

    G=z^2-w in A,       pullback G=x^2,
    div_B(pullback G)=4c.

Restricting F to G=0 gives F|w=z^2=z^4. Hence F=G=0 has reduced
support exactly C. The full reduced inverse image of C is c:
in B, z=0 and lx=0 imply x^2=0 and therefore x=0 set-theoretically.
The restricted morphism remains immersive on c, including the A1
point, because its ambient parametrization is (l,z,w)=(t,0,0).

This example verifies all the local issues simultaneously: an actual
finite flat double conductor, its global involution, a smooth lifted
curve with a non-Cartier order-two class, an anti-invariant section
with doubled Weil divisor, and a descended positive power. Therefore
the entire del Pezzo conductor reduction needs a global obstruction
when D meets an ADE point; smooth-conductor parity alone is
insufficient.

The displayed affine line has degree one and its projective
homogenization is not asserted to provide the fixed degree-four
C0 or a projective mate. The [historical checker](https://github.com/markluxton1/STCI/blob/ab0cf6fddf3bcbeded056eb584186e566e467b30/computations/verify_a1_singular_conductor_parity_shield_2026_10_09.py)
checks the literal equations, finite relation, resultant, complete
presentation determinant, node factorization, branch orders, and
descended-square identity. The proofs above establish normality,
the actual conductor equality and the divisor claims.

The checker returned exit 0 and `status: PASS` on 2026-10-09.
Its source SHA256 is
`326a5fd0f0d445cb4e51e2c3e53e447529c2c079caca8d45be8ac766d34eacc6`.
Normality uses the primary
[Stacks Project Serre criterion](https://stacks.math.columbia.edu/tag/031S).

---

## Source: 2026-10-09-session-delpezzo-D5-root-independent-audit.md

# Root's independent reconstruction of the D5 torsion filter

Status: **PROVED HERE / accepted at the stated geometric and lattice scopes**. The argument below and the separate signed-partition check supply the independent acceptance.

Audited source: [D5 torsion filter](#source-2026-10-09-session-delpezzo-d5-torsion-filtermd).
The separate [genus-one reduction](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
and [its independent ADE audit](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
establish its weak-del-Pezzo/ADE hypotheses for every sectional-genus-one
normalization of an integral nonnormal quartic containing fixed C0.
This audit does not exclude mates in both surviving singularity types.

## 1. The geometric class lies outside the exceptional lattice

On the minimal resolution M, L=-K_M is nef and big with L^2=4.
The hypothetical mate supplies a smooth reduced curve c on S,
isomorphic to C0, with b c~bH. Its strict transform c# is also smooth
P1 and L.c#=4. Adjunction gives c#^2=2. Hence the integral class

    Z=L-c#,       L.Z=0,       Z^2=-2

is a root in the anticanonical orthogonal lattice. Pullback of the
actual effective Cartier divisor b c expresses b Z as a nonnegative
integral combination of exceptional curves, so Z belongs to their
rational span and to its integral saturation. It has Z.E<=0 on each
exceptional prime because c#.E>=0.

The owner correctly retains that c is smooth downstairs, not only
that its abstract strict transform is smooth. If Z were an integral
exceptional combination, the quotient
Cl(S)=Pic(M)/<exceptional curves> would give c~H as Weil divisors.
This makes c Cartier. At a point of c, its regular one-dimensional
quotient local ring, together with one defining equation, gives at
most two generators of the surface maximal ideal. A two-dimensional
surface local ring there must consequently be regular. Thus c avoids
all singular points of S, and c# avoids every exceptional curve.
Then Z.E=0 on the entire exceptional lattice, so its negative-definite
intersection form forces Z=0, contradicting Z^2=-2. Therefore

    Z in sat(R) minus R.

This is the required missing-root condition. It fails if one drops
downstairs smoothness, so the geometric premise is material.

## 2. The entire integral orthogonal lattice is D5

A weak del Pezzo surface of degree four is the blowup of five points
of P2, allowing infinitely near points and using total exceptional
transforms. The primary author-hosted source is
[Dolgachev, Classical Algebraic Geometry, section 8.1.3](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf).
Its definition and ensuing statement after Definition 8.1.18 give
the weak del Pezzo blowup model; the degree rules out F0 and F2
without blowups. The Picard group is free with intersection form
diag(1,-1,-1,-1,-1,-1), and L=3h-sum e_i is primitive of square four.
The orthogonal complement therefore has discriminant four.

The displayed five Picard roots in the owner note have negative
D5 Gram matrix, also of discriminant four. Their lattice consequently
equals the whole integral orthogonal complement. This discriminant
step rules out an unrecorded finite-index enlargement. Dolgachev's
Proposition 8.2.7 gives the same forty roots explicitly; root checked
both primary passages. A geometric effective ADE exceptional basis
generates a reflection-closed root subsystem of this forty-root system.

## 3. Reconstruction by signed connected components

Use the Euclidean pairing and D5={v in Z^5: sum v_i even}, reversing
the geometric intersection sign. For a coordinate-connected root
component, choose a spanning tree and switch signs so its tree roots
are differences u_i-u_j. Their reflections are transpositions along
a connected graph and generate every permutation of that block.
Consequently the subsystem contains all differences on the block.

If every other edge also becomes a difference, the block is A_(m-1)
with rational span sum epsilon_i v_i=0. If an edge becomes a sum,
permuting its coordinates produces all sums as well, giving the full
D_m block. This includes D2=2A1 and D3=A3. No third connected type
can occur in this coordinate-root model.

An integer vector in a balanced A block satisfying its signed-sum
equation belongs to that A root lattice. Its ordinary sum is even,
since signs have no effect modulo two. Each D block spans all its
coordinates rationally and has an independent even-sum condition
in the root lattice. The ambient D5 instead imposes just the total
even sum across all D blocks. With t nonempty D blocks the index
is 2^(t-1) when t>=1, and one when t=0.

A missing ambient root in the rational span cannot lie inside a
block: those roots are already present. If its two coordinates lie
in separate blocks, any balanced block gives a nonzero signed sum,
which excludes rational-span membership. Thus a missing root joins
two D blocks, and conversely every such root violates both separate
parities while satisfying the ambient total parity.

Each D block has at least two coordinates. On five coordinates two
blocks have sizes only (2,2) or (2,3). A further nontrivial block
cannot fit. These are exactly 4A1 and A3+2A1, with saturation D4
and D5 respectively, both index two. This is a direct completeness
proof, independent of the program's enumerated count.

## 4. Chamber, correction and parity

For the effective geometric exceptional roots, the inequalities are
z.alpha_i=-Z.E_i=c#.E_i>=0. In a D2 block with simple roots
u1-u2 and u1+u2, only +u1 among signed coordinate vectors satisfies
both inequalities. In a D3 block with simple roots u1-u2, u2-u3,
u2+u3, only +u1 does so. Therefore a missing root joining the two
blocks has exactly one dominant choice.

For 4A1 it is u1+u3, giving

    Z=(E1+E2+E3+E4)/2,       c#.Ei=1 for all four.

For A3+2A1 it is u1+u4. Here u1-u2 is the middle A3 root; the
other two D3 roots are its ends. This gives

    Z=E_mid+(E_left+E_right+F1+F2)/2,
    (c#.E_mid,c#.E_left,c#.E_right,c#.F1,c#.F2)=(1,0,0,1,1).

All coefficients are nonnegative, as required by the actual divisor
pullback. These corrections are the nonzero order-two classes in
sat(R)/R. Since b Z belongs to R, every hypothetical mate degree b
is even. This does not show that any even degree works.

## 5. Independent finite control and evidence boundary

The owner enumerates reflection closures and checks integer-lattice
membership with Hermite normal form. Root wrote a separate
[signed-partition countercheck](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/validation/2026-10-09-D5-root-audit/countercheck.py)
using all 52 set partitions of five coordinates and all balanced
sign assignments or full D blocks. It uses neither reflection
closure nor Hermite normal form. It obtains the same 428 embedded
subsystems and checks rational-span membership and the separate
parities of every one of the forty ambient roots. Exactly fifteen
embeddings are 4A1 and ten are A3+2A1; their missing-root counts
are sixteen and twenty-four. Every other embedding is saturated.

The written signed-component proof establishes the theorem; the two
independent finite controls check its arithmetic representation. Their
scope is the stated D5 lattice problem under the geometric hypotheses,
not an unrestricted surface classification.

## 6. Combined accepted conclusion

Combining this lattice proof with the separately audited rationality
and genus-one del Pezzo reductions, every hypothetical quartic mate
for fixed C0 in the normalization sectional-genus-one lane requires
exactly one of the two complete exceptional types above, and an even
mate degree. All other ADE types in that lane are excluded. The
explicit four-A1 family has an additional all-degree exclusion by
full fibers, but other four-A1 projections and A3+2A1 remain OPEN.
Rational genus-two normalizations and higher carrier degrees also
remain OPEN. No unrestricted C0 or universal STCI conclusion follows.

---

## Source: 2026-10-09-session-delpezzo-D5-torsion-filter.md

# The D5 root-saturation filter for degree-four ADE del Pezzo normalizations

Date: 2026-10-09. Owner: `delpezzo_d5_torsion_filter`.
Status: **PROVED HERE, independently accepted within the stated
weak-del-Pezzo/ADE hypotheses**; the exhaustive exact lattice checker
has terminal PASS. The [written independent proof audit](#source-2026-10-09-session-delpezzo-d5-torsion-independent-auditmd)
accepts sections 2--5 without corrections. This note does not classify all sectional-genus-one
normalizations, construct a mate, or resolve the STCI problem.

This follows the [sectional-genus reduction](../supplements/SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md)
and complements the [explicit four-A1 family](#source-2026-10-09-session-singular-delpezzo-four-a1-familymd).
The latter realizes the first surviving lattice pattern and then excludes
its displayed projections by an additional normalization-fiber argument.
That family is not assumed to exhaust the four-A1 lattice pattern.

## 1. Precisely scoped geometric conclusion

Work over an algebraically closed field of characteristic zero. Suppose
an integral quartic carrier X has finite normalization nu:S->X with
an ample Cartier polarization H=nu*O_X(1), H^2=4. Assume that S has
only ADE singularities and its minimal resolution sigma:M->S satisfies

    L=sigma*H=-K_M.

Thus M is a weak del Pezzo surface of degree four. Let c be the
embedded smooth P1 supplied by a hypothetical mate for the smooth
rational quartic C0, so that

    H.c=4,       div_S(nu*G)=b c ~ b H,

for a positive integer b. The full support and smooth lift are required
geometric inputs; smoothness of an abstract strict transform alone
does not suffice for the argument below.

Let E_1,...,E_r be all exceptional (-2) curves, and let R be the
lattice they generate in Pic(M). Their intersection graph is a
disjoint union of ADE diagrams. Then the complete exceptional type
is necessarily one of

    4A1,       A3+2A1.

In either case b is even. More precisely the unique possible exceptional
correction in the effective chamber is as follows:

| Exceptional type | Correction Z in L=c# + Z | Intersections of c# with exceptional curves |
| --- | --- | --- |
| 4A1 | (E1+E2+E3+E4)/2 | Once with each of the four curves |
| A3+2A1 | E_mid+(E_left+E_right+F1+F2)/2 | Once with the middle A3 curve and each F_i; zero with the A3 ends |

Here the A3 chain is E_left--E_mid--E_right and F1,F2 are its two
disjoint A1 components. All these assertions are necessary conditions.
Neither surviving type is claimed to admit a mate.

## 2. Why an actual mate produces a missing integral root

The strict transform c# is isomorphic to c. Indeed its map to c is
proper and birational and has finite fibers: an integral strict transform
cannot contain a positive-dimensional fiber without being exceptional.
It is therefore finite, and a finite birational map onto the normal
curve c is an isomorphism. In particular c# is a smooth P1.

Adjunction and L.c#=H.c=4 give

    c#^2+K_M.c#=-2,       c#^2=2.

Define the integral Picard class Z=L-c#. Its numerical identities are

    L.Z=0,       Z^2=4+2-2*4=-2.

Pulling back the effective Cartier divisor b c gives

    sigma*(b c)=b c# + sum_i n_i E_i ~ b L,
    n_i>=0.

Consequently b Z belongs to R. The exceptional intersection form is
negative definite; thus the rational exceptional class of Z has the
unique expression sum_i(n_i/b)E_i. Its coefficients are nonnegative,
although the coefficients need not be integral. Moreover

    Z.E_i=-c#.E_i<=0.

The integral class Z therefore lies in the saturation

    sat(R) = (R tensor Q) intersect Pic(M),

has square -2, and is anti-nef on the exceptional curves.

It is essential that Z is **not** in R. Here is the global descent
argument, which also identifies exactly where downstairs smoothness
enters. For a resolution of a normal surface, pushing Weil divisors
down gives the exact quotient

    Cl(S)=Pic(M)/<classes of the exceptional prime curves>.

Surjectivity uses strict transforms; the kernel assertion uses the
common rational function field and the fact that a divisor with
zero pushdown is exceptional. If Z belongs to R, pushing its class
down shows H-c~0 in Cl(S). Thus c is Cartier, since H is Cartier.

An embedded smooth curve which is Cartier through a point P of a
surface forces P to be regular. Locally its ideal is (f), and R_P/(f)
is regular of dimension one. Lifting a generator of its maximal ideal
together with f gives at most two generators of the maximal ideal
of the two-dimensional local ring R_P. Its embedding dimension is
therefore two, so R_P is regular. Consequently c avoids Sing(S).
Its strict transform is then disjoint from every E_i. Since Z lies
in their rational span and Z.E_i=0 for all i, negative definiteness
gives Z=0, contrary to Z^2=-2. This proves Z not in R.

The same argument also shows that c must meet Sing(S), without
assuming that conclusion from the sectional-genus-zero record.
If one retained only c# smooth, the implication Z not in R would be
false: the abstract class c#=L-E for an A1 root has the required
adjunction numbers but Z=E belongs to R; contraction can make its
image singular. That is not the smooth lifted c required by a mate.

## 3. The ambient root lattice, with its signs fixed

A weak degree-four del Pezzo surface has a geometric Picard marking
by the total transforms h,e1,...,e5 from five successive blowups of
P2. Its intersection form and anticanonical class are

    diag(1,-1,-1,-1,-1,-1),       L=3h-e1-e2-e3-e4-e5.

The negative definite lattice L-perp is the D5 root lattice. For
an explicit identification, the five Picard roots

    e1-e2, e2-e3, e3-e4, e4-e5, h-e1-e2-e3

have minus the Gram matrix of the standard Euclidean D5 simple roots

    u1-u2, u2-u3, u3-u4, u4-u5, u4+u5.

Both lattices have discriminant four, so this identifies the entire
integral orthogonal complement, not merely a finite-index sublattice.
Equivalently its forty square-minus-two vectors are precisely

    +/- (ei-ej),       +/- (h-ei-ej-ek).

The standard Euclidean model, with the sign of the pairing reversed
from the geometric intersection form, is

    D5 = {v in Z^5 : sum_i v_i is even},
    Phi(D5) = {+/- u_i +/- u_j : i<j}.

The checker binds these two models by their actual Gram matrices and
all forty roots. No choice of a root-system table is needed for the
saturation proof that follows. The familiar Picard marking and ADE
exceptional-lattice input can be checked in [Dolgachev, Classical
Algebraic Geometry](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf),
sections 8.1.3, 8.2.3 and 8.2.7; section 8.6.3 supplies a consistency
check against the quartic del Pezzo singularity list. The signed-coordinate
saturation argument in sections 4 and 5 is proved directly here.

## 4. All embedded root subsystems by signed coordinate components

Let Psi be the root subsystem generated by a simple ADE basis of R.
It is closed under negation and under reflections in its roots. Form
a graph with vertices the five coordinates: the support of a root
on coordinates i,j supplies an edge, recording the signs of its two
nonzero coefficients. Different connected coordinate components use
disjoint supports and hence are orthogonal. Ignore unused coordinates.

For a connected coordinate component on m vertices, switch coordinate
signs so that the edges of a spanning tree have the form u_i-u_j.
Their reflections are transpositions and generate the permutations
of its m coordinates. Reflection closure therefore contains every
difference +/- (u_i-u_j).

There are exactly two possibilities:

* **Balanced signs.** Every original edge becomes a difference.
  Its entire reflection closure is the A_(m-1) root system of
  differences. In unswitched coordinates its rational span is one
  hyperplane sum_i epsilon_i v_i=0, with epsilon_i in {+1,-1}.
* **Unbalanced signs.** Some original edge becomes u_i+u_j up to
  overall sign. Permuting coordinates now gives every sum root as
  well as every difference. The reflection closure is D_m, and its
  rational span is the whole coordinate block. Its integral root
  lattice consists of integer vectors with even coordinate sum.

This includes the small cases D2=2A1 and D3=A3. In particular two
orthogonal A1 components can share the same pair of coordinates;
grouping by coordinate connectivity handles this case correctly.
The sign switching is an ambient lattice isometry, since changing
coordinate signs preserves the even-sum condition. Only a lattice
classification is asserted here; no extra claim about Weyl orbits
of geometric markings is needed.

For a balanced block, an integer vector satisfying its signed-sum
equation belongs to its A lattice. Its ordinary coordinate sum is
even, because signed and ordinary sums agree modulo two. A D block
has no linear equation but imposes its own even-sum constraint in R.
Thus, if the number of D blocks is t, the saturation in D5 replaces
their t separate parity constraints by their single total parity
constraint. It follows that

    [sat(R):R] = 1 if t=0,
    [sat(R):R] = 2^(t-1) if t>=1.

There is a particularly direct root-level version. A root in the
rational span of R is either supported within one coordinate block,
or joins two blocks. Roots inside a balanced block are precisely
its signed differences; roots inside a D block are already its D
roots. A cross-block root has a nonzero signed sum in any balanced
block it touches, so cannot lie in that block's rational span. It
can therefore be a missing root only if it joins two D blocks.
Conversely every root joining two D blocks is in sat(R) and violates
both separate parities, so is outside R.

Every D block uses at least two coordinates. With five coordinates,
two such blocks can only have sizes

    (2,2),       (2,3).

There is no room for another root block in either case. These are
exactly

    R=4A1,       sat(R)=D4,       index two;
    R=A3+2A1,   sat(R)=D5,       index two.

The first case has sixteen missing roots, the second twenty-four.
All other embedded ADE root sublattices of D5 are saturated. This
proves the proposed filter, including its completeness, without
assuming that a computational sample exhausted embeddings.

## 5. The effective chambers determine the corrections uniquely

The positive Euclidean model has z.alpha_i=-Z.E_i=c#.E_i>=0 for
the effective simple roots alpha_i. This fixes the chamber.

For 4A1 choose

    alpha1=u1-u2, alpha2=u1+u2,
    alpha3=u3-u4, alpha4=u3+u4.

The missing roots join {1,2} to {3,4}. The inequalities on alpha1
and alpha2 permit only +u1 in the first block, and the inequalities
on alpha3 and alpha4 permit only +u3 in the second. Hence the unique
missing root in this chamber is

    z=u1+u3=(alpha1+alpha2+alpha3+alpha4)/2.

Its scalar product with each simple root is one. Translating back
gives the first row of section 1.

For A3+2A1 choose

    alpha1=u1-u2, alpha2=u2-u3, alpha3=u2+u3,
    alpha4=u4-u5, alpha5=u4+u5.

Here alpha1 is the middle of the A3 chain, with ends alpha2 and
alpha3. A missing root joins {1,2,3} to {4,5}. Chamber inequalities
force +u1 and +u4 respectively, so its unique value is

    z=u1+u4=alpha1+(alpha2+alpha3+alpha4+alpha5)/2.

Its scalar products with the five simple roots are (1,0,0,1,1).
This gives the second row of section 1. Other choices of simple
roots are carried to these by changing the chamber inside each
root subsystem; the uniqueness statement is relative to the actual
effective exceptional basis.

In both cases Z represents the nonzero order-two coset in sat(R)/R.
Since b Z belongs to R, b is necessarily even. This also describes
the order-two exceptional correction at every singularity met by
c: all four A1 points in the first case, or the A3 middle and the two
A1 points in the second. The zero intersections with the A3 end
curves follow numerically and are not extra geometric assumptions.

## 6. Exact exhaustive control and provenance

The standalone [checker](../../computations/verify_delpezzo_D5_torsion_filter_2026_10_09.py)
constructs the forty roots, precomputes their exact integer reflections,
and enumerates every embedded reflection-closed subsystem by adding
one root and taking reflection closure, starting from the empty
subsystem. Completeness follows inductively: any subsystem can be
generated by its roots in a finite sequence, and every intermediate
closure is contained in it. It obtains **428** embedded subsystems.

For each one, it independently takes the Hermite normal form of the
matrix of all its roots. Rational orthogonal projection and integral
coordinates in that integer-lattice basis determine the ambient roots
in its rational span and in its integral lattice. These results are
then compared with the signed-block classification. Gcds of maximal
minors check the saturation index, with the ambient D5 even-sum
condition retained. The computation verifies all 428 cases, not just
one representative per abstract ADE type, and verifies both chamber
formulas.

The only nonprimitive embedded subsystems are the fifteen 4A1
embeddings and the ten A3+2A1 embeddings. Their indices are two and
their missing-root counts are sixteen and twenty-four respectively.
The source run completed with terminal exit zero and PASS; its exact
source SHA256 is

    fdbb9bdddd0c7b6b20140835662b3526ba800aa814d3d71c5de91085097e3a7e

The checker reconstructs all type counts, the lattice profiles, both
root bases, both correction vectors and their intersections. Its scope
is the stated root-lattice filter: it does not classify all
sectional-genus-one normalizations and does not settle STCI.

The [bounded written audit](#source-2026-10-09-session-delpezzo-d5-torsion-independent-auditmd) accepted the frozen proof without corrections; its mathematical statements and checker source are unchanged.

## 7. Continuation boundary

The filter excludes every other exceptional ADE configuration under
the exact polarization L=-K_M. It leaves two concrete torsion patterns,
and restricts any mate degree there to even integers. The existing
four-A1 projection family meets the first pattern but its displayed
members fail full inverse support. Whether another projection of a
four-A1 pair, or a pair of type A3+2A1, can satisfy all mate conditions
is not resolved here.

No implication from arbitrary pi=1 normalizations to this weak degree-four
del Pezzo/ADE model has been used in the lattice proof. The separately
accepted [genus-one model-coverage theorem](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
now supplies those hypotheses for rational genus-one quartic normalizations
containing C0; combining the two theorems is justified by that separate
record. Sectional genus two, higher carrier degrees,
other normalizations, and the universal STCI question remain outside
this note's conclusion. No frontier file has been edited
by this owner.

---

## Source: 2026-10-09-session-delpezzo-D5-torsion-independent-audit.md

# Independent proof audit of the D5 missing-root filter

Date: 2026-10-09. Auditor: `verification`. Status: **ACCEPTED / PROVED HERE**, with the weak degree-four del Pezzo and ADE hypotheses stated below. This is a proof audit, not a duplicate run of the exhaustive lattice checker.

The frozen owner note [D5 torsion filter](#source-2026-10-09-session-delpezzo-d5-torsion-filtermd) was read in full at SHA256 `b4f4e4bb5a44c01022ce0e7d342bb1ce74127d0d3575aa227b3a18050e5d5919`. Its checker source, read/hash bound but not rerun here, is `computations/verify_delpezzo_D5_torsion_filter_2026_10_09.py`, SHA256 `fdbb9bdddd0c7b6b20140835662b3526ba800aa814d3d71c5de91085097e3a7e`.

## Exact accepted scope

Let S be an ADE normal surface with ample Cartier H of square four. Its minimal resolution sigma:M->S is assumed to satisfy L=sigma^*H=-K_M, so M is a weak del Pezzo surface of degree four. A mate supplies an embedded smooth c=P1 with H.c=4 and b c~b H. Let R be the lattice of all exceptional prime curves. Then necessarily

    R has type 4A1 or A3+2A1,
    [sat(R):R]=2,
    b is even.

The anti-nef correction Z=L-c# is respectively half the sum of the four A1 curves, or the middle A3 curve plus half its two ends and half the two isolated A1 curves. These are necessary conditions only. The theorem does not assert that either type admits a mate. Coverage of other normalization hypotheses is a separate theorem and is not proved by the lattice filter.

## Missing integral root and the essential downstairs smoothness

The map from the integral strict transform c# to the smooth curve c is proper birational with finite fibers, hence finite and therefore an isomorphism. Adjunction gives (c#)^2=2. Thus Z=L-c# is an integral class with L.Z=0 and Z^2=-2. Pulling back the effective Cartier divisor b c shows bZ is an effective integral exceptional divisor; in particular Z is in sat(R), its rational exceptional coefficients are nonnegative, and Z.E_i=-c#.E_i<=0.

The proof that Z is outside R is correct and substantive. Pushdown of Weil divisors gives Cl(S)=Pic(M)/R. If Z were in R, c would be linearly equivalent to the Cartier H and hence itself Cartier. At a point of c, quotienting the two-dimensional surface local ring by its Cartier equation gives the regular one-dimensional ring of the embedded smooth curve. A lift of its parameter together with that equation generates the surface maximal ideal, so the surface local ring is regular. Thus c avoids Sing(S), its strict transform is disjoint from all exceptional curves, and Z is orthogonal to R. Negative definiteness then forces Z=0, contrary to its square minus two. Smoothness of c# alone would not justify this conclusion.

The standard degree-four weak del Pezzo Picard marking identifies L-perp with the negative D5 lattice. The displayed five Picard roots have exactly the claimed Gram matrix; the primitive anticanonical class has square four, so its orthogonal complement has discriminant four. The root basis therefore gives the entire lattice, rather than a proper finite-index copy. Switching to positive pairing makes z a norm-two root in D5 outside R but inside its rational span.

## Signed-coordinate completeness, without computational exhaustion

In the model D5={v in Z^5:sum v_i even}, every root has exactly two nonzero coordinates. Form the signed support graph of the reflection-closed root system generated by R. On each connected block, switch signs so a spanning tree consists of differences. Their reflections generate all coordinate permutations in that block, hence all differences.

If all edges become differences, the block is A_(m-1), with rational span the signed-sum-zero hyperplane and integral lattice all integer vectors in that hyperplane. If any sum edge remains, permutation closure gives all sums as well, so the block is D_m with full rational coordinate span and an even-sum integral lattice. This includes D2=2A1 and D3=A3. Distinct coordinate blocks are orthogonal. Sign switching preserves the ambient even-sum lattice, so it does not change the saturation question.

A root supported inside one block is already in its root lattice. A root meeting a balanced A block in just one coordinate cannot satisfy that block's span equation. Therefore a missing norm-two root must join two D blocks. Conversely such a root belongs to the rational span and to D5 but violates each block's separate even-sum constraint, so is missing. Two D blocks each require at least two coordinates. The budget five permits only sizes (2,2) and (2,3), with no further nontrivial root block. These give exactly 4A1 and A3+2A1.

Their saturation replaces two separate parity constraints with the one total parity constraint; the index is two. This independently proves both completeness and the index claim. It also proves the stronger assertion in the owner note that every other embedded ADE root sublattice is saturated. The owner's enumeration of 428 reflection-closed subsystems is supporting exact evidence, not the proof of exhaustion used here.

## Chamber corrections and mate parity

For 4A1 take roots u1-u2,u1+u2,u3-u4,u3+u4. A missing root joins the two pairs. Nonnegative pairing with all four simple roots forces it to be u1+u3, half the sum of those four roots. Its pairings are all one.

For A3+2A1 take u1-u2,u2-u3,u2+u3,u4-u5,u4+u5. The first root is the middle A3 curve. A missing root joins the two blocks, and nonnegative simple-root pairings force u1+u4. Its coefficients are (1,1/2,1/2,1/2,1/2) and its pairings are (1,0,0,1,1). Translating back to negative geometric pairing gives exactly the owner correction and intersection tables. Choosing the actual effective simple basis fixes the chamber; no additional geometric Weyl-orbit claim is needed.

In either case the correction is the nonzero coset of the index-two saturation quotient. Since bZ is in R, b must be even. The conclusion survives this independent audit with no correction to the frozen proof.

No frontier file was changed and no new mathematical computation was run for this bounded audit.

---

## Source: 2026-10-09-session-delpezzo-entire-conductor-independent-audit.md

# Independent audit: the entire ADE del Pezzo conductor

**Accepted as a conditional structural theorem in characteristic zero.**
The audited proof is
[2026-10-09-session-delpezzo-entire-conductor.md](#source-2026-10-09-session-delpezzo-entire-conductormd).

The hypotheses are a finite normalization `nu:S -> X` of an integral quartic
surface in `P3`, with `S` a rational normal degree-four del Pezzo surface
having only ADE singularities, and
`H=nu^*O_X(1)=-K_S` ample Cartier, `H^2=4`. Every conductor scheme mentioned
below is the actual scheme defined by the conductor ideal, including its
nilpotents.

**Canonical modules and the actual Cartier conductor.** The Gorenstein
quartic has `omega_X` isomorphic to `O_X`. After choosing this trivialization,
finite absolute duality identifies `nu_*omega_S` with
`Hom_OX(nu_*O_S,O_X)`, compatibly with the normalization algebra action.
Locally every such homomorphism is multiplication by a fraction `r`; the
condition `1 in B` forces `r in A`, and its defining condition is precisely
`rB subset A`. This is the actual conductor ideal `I`, which is also an ideal
of `B` and satisfies `IB=I`. Since `omega_S=O_S(-H)` is invertible, its
embedding in `O_S` defines an effective Cartier divisor `D~H`, including at
ADE points. Here `I O_S` means the extended ideal, not an assertion that the
unmodified tensor pullback has no torsion.

**Vanishing and arithmetic Cohen--Macaulayness.** On the crepant rational
resolution `mu:M -> S`, put `A_M=mu^*H`. It is nef and big and
`K_M=-A_M`. For every `n>=0`, Kawamata--Viehweg vanishing applies to
`nA_M=K_M+(n+1)A_M`. Rational resolution and projection formula transfer the
vanishing to `S`. Gorenstein Serre duality transfers it to every negative
integer as well, giving `H1(S,O_S(nH))=0` for all integers `n`. The proof uses
the standard characteristic-zero vanishing theorem; this audit does not
claim a newly verified publisher full-text source.

The preimage ideal sequence
`0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0` is exact for the actual
conductor. Vanishing of both intermediate line-bundle cohomology groups on
`P3` therefore gives `H1(P3,J_Gamma(m))=0` for every integer `m`.

**Purity and classification of the entire downstairs scheme.** The
normalization and its canonical module are maximal Cohen--Macaulay over the
local hypersurface ring: parameters from that ring remain parameters at the
finite normalization points. Hence `I` has depth two at each closed point of
`X`. The depth lemma for `0 -> I -> O_X -> O_Gamma -> 0` forces every nonzero
conductor quotient at a closed point to have depth at least one. Its
dimension is at most one, so there are no embedded or isolated
zero-dimensional components. The Hilbert polynomial computed below ensures
that the curve is nonempty. Thus `Gamma` is pure Cohen--Macaulay, and the
all-twist ideal vanishing makes its saturated coordinate ring ACM.

Riemann--Roch on the rational resolution gives
`chi(O_S(nH))=1+2n(n+1)`. Consequently
`chi(O_Gamma(m))=(2m^2+2)-(1+2(m-1)m)=2m+1`. An Artinian reduction of the
ACM coordinate ring has a nonnegative Hilbert function with sum two and
weighted sum one, hence exactly `h=(1,1)`. Its degree-one coordinate piece
has dimension three, so precisely one independent plane equation belongs
to the ideal. Within that plane its coordinate ring is Cohen--Macaulay of
codimension one in a polynomial ring of dimension three. Auslander--Buchsbaum
makes its ideal a free graded rank-one module, hence principal; the Hilbert
series gives a degree-two generator. Therefore the actual saturated ideal is
a complete intersection `(ell,Q2)`. This proves that `Gamma` is a smooth
conic, two meeting distinct lines, or the plane double-line scheme, rather
than a classification merely of its reduced support. Adjunction gives
`omega_Gamma=O_Gamma(-1)`.

**Duality and finite flatness on the entire schemes.** Over a Gorenstein
local surface ring `A`, MCM duality gives
`I=Hom_A(B,A)`, `Hom_A(I,A)=B`, and the requisite positive Ext vanishing.
Applying the dual to `0 -> I -> A -> A/I -> 0` identifies the natural
quotient `B/A` with the codimension-one canonical module. Globalizing gives
`nu_*O_S/O_X=omega_Gamma` (with the fixed trivialization of `omega_X`). Since
`I` is the same ideal in both rings, quotienting by it gives

\[
0\longrightarrow O_\Gamma\longrightarrow p_*O_D
\longrightarrow \omega_\Gamma\longrightarrow0.
\]

The right-hand module is invertible, so this sequence splits locally as
modules even at a nodal or nonreduced point. Its middle module is locally
free of rank two. The finite morphism `p` is therefore finite flat of degree
two without assuming reducedness or smoothness of either conductor scheme.

**The trace involution includes nilpotents.** Trace of multiplication by
`1` is two, so in characteristic zero the algebra has the canonical module
decomposition `p_*O_D=O_Gamma direct_sum N`, with
`N=ker(trace)` isomorphic to `omega_Gamma`. For a local generator `z` of
`N`, Cayley--Hamilton makes `z^2` a scalar in `O_Gamma`. Thus the map fixing
the scalar algebra and negating `N` is an algebra involution; changes of
trace-zero generator show that these local maps glue. This calculation is
valid over arbitrary nonreduced base rings. Its invariant algebra is exactly
`O_Gamma` because two is invertible.

**Upstairs data and the surviving boundary.** Cartier adjunction gives
`omega_D=O_D`. The all-twist vanishing applied to
`0 -> O_S(-H) -> O_S -> O_D -> 0` gives `H0(D,O_D)=k`, hence connectedness.
Its Hilbert polynomial is `4m`, so its arithmetic genus is one. These facts
do not imply that `D` is reduced, smooth, or disjoint from the ADE points.
The earlier ramification-parity argument for a smooth elliptic conductor
cannot be transferred to these singular or nonreduced cases without an
additional proof. The present theorem supplies the full conductor algebra
and involution, but by itself supplies no mate exclusion or quadratic
descent theorem.

---

## Source: 2026-10-09-session-delpezzo-entire-conductor.md

# The entire conductor of a rational ADE degree-four del Pezzo normalization

Date: 2026-10-09. Author: `singular_local_lift`, for
`singular_normalization_next_frontier`.

Status: **PROVED HERE, independently audited**, under the hypotheses in Section 1. This note
concerns the actual conductor schemes, including reducible and
nonreduced cases. It does not assume the upstairs conductor is smooth
or avoids the normalization singularities. No mate or universal STCI conclusion follows from this
structural reduction alone.

## 1. Hypotheses and conclusions

Work over an algebraically closed field k of characteristic zero.
Let X be an integral quartic surface in P3, and let nu:S->X be its
finite normalization. Assume S is a rational normal degree-four del
Pezzo surface with only ADE singularities and

    H=nu^*O_X(1)=-K_S,
    H ample and Cartier,       H^2=4.

ADE is used through its precise properties: S is Cohen--Macaulay and
Gorenstein, and its minimal resolution mu:M->S is rational and
crepant, so R^i mu_*O_M=0 for i>0 and K_M=mu^*K_S. No list of ADE
types, including 4A1 or A3+2A1, is required in the proof.

Let I=Ann_OX(nu_*O_S/O_X) be the conductor. Define the actual schemes

    Gamma=V_X(I),       D=V_S(I O_S),       p:D->Gamma.

Then:

1. I O_S is invertible and isomorphic to O_S(-H). Consequently D
   is an effective Cartier divisor with D~H.
2. Gamma is pure Cohen--Macaulay of dimension one and arithmetically
   Cohen--Macaulay in P3, with Hilbert polynomial 2m+1. Its ideal is
   a complete intersection of degrees (1,2). Thus the entire Gamma
   is a plane conic: smooth, two distinct lines, or a double line.
3. There is an exact sequence on Gamma

       0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,

   and omega_Gamma=O_Gamma(-1) is invertible. Therefore p is finite
   flat of degree two, on the entire schemes.
4. Trace gives a canonical global involution sigma of the O_Gamma
   algebra p_*O_D, with decomposition

       p_*O_D = O_Gamma direct_sum N,
       N=ker(trace) isomorphic to omega_Gamma.

   Locally N has a generator z with z^2 in O_Gamma and sigma(z)=-z.
   These statements retain nilpotents when Gamma or D is nonreduced.
5. D is a connected Gorenstein anticanonical curve with
   omega_D=O_D, H^0(D,O_D)=k, and Hilbert polynomial 4m. Its
   arithmetic genus is one. Smoothness and reducedness are not
   asserted.

## 2. Finite absolute duality identifies the actual upstairs conductor

The quartic hypersurface X is Gorenstein with omega_X=O_X. Finite
absolute duality, together with Cohen--Macaulay concentration on
the equal-dimensional schemes, gives

    nu_*omega_S = Hom_OX(nu_*O_S,omega_X).

This is an identity of canonical modules, not a use of relative
duality requiring nu to be flat. Locally write A for the domain of
X, B for its finite birational normalization and K for their common
fraction field. Every A-linear homomorphism B->A is multiplication
by an element r in K, because it becomes multiplication after
tensoring with K. Since 1 belongs to B, such r belongs to A, and

    Hom_A(B,A)={r in A:rB subset A}=I.

This identifies the right side with the actual conductor ideal,
also as a B-module. Since S is Gorenstein and K_S=-H,

    I=nu_*omega_S,
    I O_S=omega_S=O_S(-H)

as B-ideals after using the duality identification. The inclusion
into O_S is a nonzero inclusion of an invertible sheaf into the
structure sheaf of an integral scheme. Its zero scheme is an
effective Cartier divisor D with O_S(-D)=I O_S. Therefore D~H.
This remains valid when D passes through an ADE point.

## 3. All twists have the required H1 vanishing

Put A_M=mu^*H. It is nef and big, and K_M=-A_M by crepancy. For
n>=0,

    n A_M-K_M=(n+1)A_M

is nef and big. Kawamata--Viehweg vanishing on the smooth resolution
therefore gives H^1(M,O_M(n A_M))=0. Rationality of the ADE
resolution and the projection formula identify this group with
H^1(S,O_S(nH)). Thus the latter vanishes for n>=0.

For n<=-1, Serre duality on the projective Gorenstein surface gives

    H^1(S,O_S(nH))^* = H^1(S,O_S((-n-1)H)).

The exponent on the right is nonnegative. Consequently

    H^1(S,O_S(nH))=0       for every integer n.

The exact conductor preimage sequence on P3 is

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0,

where J_Gamma is the ideal sheaf of the actual downstairs scheme.
After twist m, both intermediate cohomology groups H^1 and H^2 of
O_P3(m-4) vanish. The long exact sequence therefore identifies

    H^1(P3,J_Gamma(m)) = H^1(S,O_S((m-1)H)) = 0

for every integer m.

## 4. Purity, the Hilbert polynomial, and the entire plane conic

The conductor I is maximal Cohen--Macaulay as an O_X-module.
Locally this follows from its identification with the canonical
module of the finite Cohen--Macaulay normalization. More explicitly,
a system of parameters of the two-dimensional local ring A is a
system of parameters at all finite normalization points above it;
it is regular on their canonical modules. Hence depth_A(I)=2.
The depth lemma applied to

    0 -> I -> O_X -> O_Gamma -> 0

gives depth at least one for O_Gamma at its closed points. The
conductor is a nonzero rank-one ideal, so its quotient has dimension
at most one. It follows that Gamma is a pure Cohen--Macaulay curve;
there are no embedded or isolated zero-dimensional components.

Riemann--Roch on the rational crepant resolution, and rationality
of the resolution, give for every integer n

    chi(O_S(nH))=1+2n(n+1).

The quartic hypersurface sequence gives

    chi(O_X(m))=2m^2+2.

Using I=nu_*O_S(-H) in the conductor sequence yields

    chi(O_Gamma(m))
      =(2m^2+2)-(1+2(m-1)m)=2m+1.

Thus Gamma has degree two and arithmetic genus zero. The H^1
ideal vanishing from Section 3 makes its saturated homogeneous
coordinate ring Cohen--Macaulay of dimension two.

To retain the scheme classification, take an Artinian reduction
by two general regular linear forms. Its nonnegative Hilbert
function h has h0=1, sum h_i=degree(Gamma)=2, and
sum i h_i=1 from arithmetic genus zero. Thus h=(1,1). The degree-one
piece of the coordinate ring has dimension 2+1=3, so exactly one
linear form belongs to the ideal in P3. Gamma lies in a plane.
In degree two its coordinate ring has dimension five, while that
of the plane has dimension six. Thus a nonzero plane quadratic
equation Q_2 belongs to its ideal. The plane quotient by Q_2 and
Gamma have the identical Hilbert series (1+t)/(1-t)^2. Their graded
surjection is consequently an isomorphism in every degree. This
proves that the entire saturated ideal is

    I_Gamma=(ell,Q_2),       degrees (1,2).

This excludes extra embedded structures. Over k the equation is a
smooth conic, a product of
two distinct linear forms, or a square of a linear form. The double
line here is the actual plane double-line scheme, not an arbitrary
ribbon supported on a line. In every case Gamma is Gorenstein, and
adjunction gives omega_Gamma=O_Gamma(-1).

## 5. The quotient is the dualizing sheaf and forces finite flatness

Work again over a Gorenstein local surface ring A, with B its
normalization and I the conductor. The modules B and I are maximal
Cohen--Macaulay. Duality on that category gives

    I=Hom_A(B,A),       Hom_A(I,A)=B,
    Ext_A^j(B,A)=Ext_A^j(I,A)=0 for j>0.

Apply Hom_A(-,A) to 0->I->A->C->0, where C=A/I. Since A is a domain
and I contains a nonzero element, Hom_A(C,A)=0. The resulting
exact sequence is

    0 -> A -> B -> Ext_A^1(C,A) -> 0.

The last module is the canonical module of the pure codimension-one
Cohen--Macaulay scheme C. Globalizing with omega_X=O_X therefore
gives

    nu_*O_S/O_X = omega_Gamma.

Since the same conductor I is an ideal of both A and B, quotienting
the inclusion A subset B by I gives, on the actual conductor schemes,

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

The right-hand line bundle is locally free of rank one over every
local ring of Gamma, including a node or a double-line point. The
sequence therefore splits as a sequence of modules locally: a
generator of omega_Gamma lifts, and the resulting middle module is
free of rank two. Because p is finite, this proves that p is finite
flat of degree two. No smoothness, generic reducedness or separate
flatness assertion has been inserted here.

## 6. Trace constructs an involution on the entire algebra

Let E=p_*O_D. It is a locally free O_Gamma algebra of rank two.
The trace of multiplication satisfies trace(1)=2. In characteristic
zero this gives the canonical splitting

    E=O_Gamma direct_sum N,       N=ker(trace).

The line bundle N maps isomorphically onto E/O_Gamma=omega_Gamma.
Locally choose a generator z of N. Its rank-two multiplication
matrix has trace zero. Cayley--Hamilton gives

    z^2=-det(multiplication_by_z) in O_Gamma.

Thus the O_Gamma-linear map fixing 1 and sending z to -z is an
algebra automorphism. It squares to the identity and is independent
of the trace-zero generator, so these maps glue to a global
involution sigma. Its invariant algebra is O_Gamma, and its
anti-invariant module is N=omega_Gamma.

These are statements about all sections of the entire schemes.
They remain true if the base conic is a double line, if D is
nonreduced, or if the local algebra has equation z^2=0. No branch
point, function-field sign ratio or decomposition into reduced
components is required to construct sigma.

For the later quadratic descent calculation, this gives an exact
description of the entire restriction space. Since O_D(H)=p^*O_Gamma(1),
the invariant and anti-invariant summands of p_*O_D(2H) are

    O_Gamma(2),       omega_Gamma tensor O_Gamma(2)=O_Gamma(1).

Their spaces of global sections have dimensions five and three,
respectively, for every plane conic scheme classified above. In a
local trace-zero generator, a quadratic restriction can be written
a+z h, with a an invariant degree-two section and h a degree-one
section in the anti-invariant summand. It descends exactly when the
entire anti-invariant component is zero. This is a full module
statement even for a double line, not a test at generic points.
The multiplication N tensor N->O_Gamma is equivalently a global
section of omega_Gamma^(-2)=O_Gamma(2), including when that section
defines a nonreduced or singular upstairs curve.

## 7. Upstairs arithmetic data and limits of this reduction

Since D is Cartier and S is Gorenstein,

    omega_D=(omega_S tensor O_S(D))|D=O_D.

The sequence 0->O_S(-H)->O_S->O_D->0, together with the all-twist
H^1 vanishing and H^0(S,O_S(-H))=0, gives H^0(D,O_D)=k. Thus D
is connected. Its Hilbert polynomial is

    chi(O_D(mH))
      =chi(O_S(mH))-chi(O_S((m-1)H))=4m.

In particular its arithmetic genus is one. The same formula follows
from p_*O_D=O_Gamma direct_sum omega_Gamma and chi(O_Gamma(m))=2m+1,
which provides an independent consistency check of the twists.

The structural reduction leaves the following possibilities in
scope: D may pass through an ADE point, have singularities, split
into components, or be nonreduced; Gamma may be two lines or a
double line. It supplies the global trace involution in all of those
cases. It does not by itself show that a section Q with divisor
2c is invariant under that involution, nor that such a section
descends to X. Arguments using a smooth elliptic conductor or a
simple ramification parameter must separately justify those
hypotheses before being applied to the entire lane.

## 8. Primary inputs and provenance

The independent scheme-theoretic audit is saved in
`research/notes/2026-10-09-session-delpezzo-entire-conductor-independent-audit.md`.
It accepts the canonical-module identifications, entire conic scheme
classification, finite flatness and trace involution, while retaining
the singular/nonreduced-D descent boundary. Independent agreement is
audit evidence; the proof is the argument above.

Finite absolute duality is the
[Stacks Project finite-ring dualizing lemma](https://stacks.math.columbia.edu/tag/0AX0),
combined with
[Cohen--Macaulay concentration](https://stacks.math.columbia.edu/tag/0AWQ).
The local conductor identification and the maximal-Cohen--Macaulay
dual sequence are written out above. The projective-space
cohomology vanishing is the
[Stacks Project computation](https://stacks.math.columbia.edu/tag/01XS).

The vanishing input is the standard characteristic-zero
Kawamata--Viehweg theorem, used on the smooth resolution with
(n+1)mu^*H nef and big. Its original primary reference is
[Kawamata, Mathematische Annalen 261 (1982), 43--46](https://link.springer.com/article/10.1007/BF01456407).
The publisher's bibliographic record was freshly inspected; its
full text is subscription-only. The author-hosted link to Viehweg's
1982 paper returned HTTP 410. No fresh full-text verification of
those original vanishing papers is claimed. The use and hypotheses
of the standard vanishing theorem are explicit in Section 3.

No symbolic test is used as a substitute for these scheme-theoretic
proofs. No classification or novelty claim is made.

---

## Source: 2026-10-09-session-dp4-projection-independent-audit.md

# Independent audit: singular degree-four del Pezzo projection

**PROVED for this carrier, in characteristic zero:** the integral quartic
surface described below contains the fixed smooth rational quartic `C0`, but
has no set-theoretic mate of any degree. This is a carrier exclusion, not a
resolution of the unrestricted `C0` or universal STCI problem.

## The normalization and projected image

Use coordinates `[r:p:z:q:t]` on `P4` and set

\[
Q_1=pq-z^2,\quad L=r-3p-6q+4t,
\]

\[
D=-p^2-2pq+6pt-4q^2+3qr+2rt,
\qquad Q_2=7Q_1+D+Lz.
\]

Let `S=V(Q1,Q2)`. The following independently reconstructed linear change
has determinant `2`, with the rows ordered as `a,b,c,d,e` and the original
columns as `r,p,z,q,t`:

\[
a=p+q+2z,\quad b=r+3p+2z,\quad c=p+2q+3z,
\]

\[
d=3q+2t+z,\qquad e=p+4q+4z.
\]

It gives the literal identities

\[
ae-c^2=Q_1,\qquad bd-c^2=Q_2.
\]

The affine cone on this intersection is integral. Its open set `c != 0` is
integral, while the set `c=0` has dimension two, too small to contain a
component of the three-dimensional complete intersection. The complete
intersection is generically reduced and has no embedded components. Its
singular locus consists of the four coordinate axes `a,b,d,e`; this has
codimension two. Thus the cone, and consequently `S`, is normal by `S2` and
`R1`. On `S` the corresponding four vertices have local equations of type
`xy-z^2=0`, hence are `A1` singularities.

The projection center `[0:0:1:0:0]` does not lie on `S` since `Q1=-1` there.
Deleting `z` therefore gives a finite morphism to `P3[r:p:q:t]`; algebraically
finiteness also follows from the monic equation `z^2=pq`. On `L != 0` its
inverse is `z=-D/L`, proving birationality. The image is the integral quartic

\[
X=V(F),\qquad F=D^2-pqL^2.
\]

To justify irreducibility without assuming it: the image is an integral
surface, the projection is birational, and its hyperplane pullback is the
hyperplane class on the degree-four complete intersection `S`. The image
therefore has degree four. Its prime equation divides the nonzero quartic
`F`, so it equals `F` up to scalar. The finite birational map from the normal
`S` is the normalization of `X`.

## Exact conductor calculation

Let `A=k[r,p,q,t]/(F)` and
`B=k[r,p,z,q,t]/(Q1,Q2)`. As an `A`-module, `B` is generated by `1,z`, with
relations given by the columns of

\[
\begin{pmatrix}D&pqL\\L&D\end{pmatrix}.
\]

Indeed, reducing modulo `z^2-pq` leaves the free module with generators
`1,z`; the remaining relation `D+Lz` and its multiple by `z` generate all
relations. The determinant is `F`, consistent with the image equation.
Quotienting by the embedded copy of `A` yields the exact graded formula

\[
B/A\simeq (A/(L,D))(-1).
\]

Consequently the conductor is exactly
`Ann_A(B/A)=(L,D)`. Its projective sheaf is the actual downstairs conductor,
not merely a candidate support ideal.

## Full inverse-image support excludes every mate

The rational normal quartic

\[
c:[u:v]\longmapsto [u^4:u^3v:u^2v^2:uv^3:v^4]
\]

lies on `S`. Its projection is exactly
`C0=[u^4:u^3v:uv^3:v^4]`. This restricted projection is an isomorphism:
on the chart `r != 0`, `p/r=v/u`, and near the opposite endpoint `q/t=u/v`.
These provide local inverses, including at both endpoints.

Along this curve,

\[
L|_c=(u^2-4uv+2v^2)(u^2+uv+2v^2),\qquad D|_c=-u^2v^2 L|_c.
\]

The two affine quadratic factors have discriminants `8` and `-7`, and
resultant `50`. They therefore have four distinct roots in characteristic
zero, none with `uv=0`. Above any one of the corresponding points of `C0`,
`L=D=0`, and the normalization fiber consists of the two distinct points

\[
z=\pm u^2v^2.
\]

Only the positive-sign point lies on `c`, because `c -> C0` is an
isomorphism. The negative-sign point cannot belong to a second curve in the
inverse-image support: a finite morphism maps every curve over `C0`
surjectively onto `C0`, whereas the inverse over its generic point is unique
and lies on `c` (`L != 0` there). Thus each negative-sign point is genuinely
isolated in `nu^{-1}(C0)`; it is not just an additional point on a hidden
component. The support is `c` together with these four isolated points.

Suppose a homogeneous mate `G` satisfied `V(F,G)=C0` set-theoretically.
Its pullback is a nonzero section of an invertible sheaf on the integral
surface `S`, with zero support exactly `nu^{-1}(C0)`. The section is nonzero
since a mate cannot vanish identically on `X`. Its zero scheme is an
effective Cartier divisor, whose support cannot have an isolated closed
point on a surface. The four isolated normalization points contradict that
requirement. Hence this `F` has no mate in any degree.

This identifies a necessary hypothesis in any argument that writes
`nu^*G` as a power of an equation for the lifted curve: the full inverse-image
support must be checked first. Smoothness and an isomorphism `c -> C0`
alone do not establish that hypothesis.

The coordinate-change identities, both substitutions on the rational normal
quartic, the factorization of `L`, the two discriminants, the resultant, and
the determinant `2` were independently checked with SymPy on 2026-10-09.
The literal four-distinct-roots statement also holds in characteristic not
`2,5,7`; the audit's accepted scope is characteristic zero.

---

## Source: 2026-10-09-session-dp4-projection-local-lift.md

# An exact quartic carrier of C0 with four A1 normalization points

Date: 2026-10-09. Author: `singular_local_lift`, working for
`singular_normalization_next_frontier`.

Status: **PROVED HERE**, with the exact identities below. This constructs
one integral quartic containing the fixed C0 and proves its finite
birational normalization has four isolated singularities on the lifted
curve. It also excludes every mate for this particular carrier by an
explicit fiber obstruction. The singular-normalization frontier as a
whole and the universal STCI problem remain open.

## 1. The normal degree-four del Pezzo surface

Over an algebraically closed field k of characteristic zero, let

    S = V(ae-c^2, bd-c^2) in P4[a:b:c:d:e].

Its homogeneous coordinate ring is a domain. Indeed first form the
domain R0=k[a,b,d,e]/(ae-bd), whose fraction field is k(a,b,d), with
e=bd/a. The polynomial c^2-bd is irreducible over that fraction field:
bd has odd valuation at b and d and is not a square. Being monic,
it embeds R0[c]/(c^2-bd) into that quadratic field. This quotient is
exactly the coordinate ring of S.

The two equations form a complete intersection, so the surface is
Cohen--Macaulay, has degree four, and has dualizing sheaf O_S(-1).
The Jacobian has rank less than two at exactly the four coordinate
vertices corresponding to a,b,d,e. On c!=0, all of a,b,d,e are
nonzero and the two rows have rank two. On c=0, ae=bd=0: if two
coordinates are nonzero the rows again have rank two, while a
coordinate vertex has rank one. Thus there are exactly four isolated
singularities. In the chart a=1, eliminate e=c^2 and obtain
bd=c^2; this is an A1 singularity. The other vertices are symmetric.
Serre's criterion proves normality. The same argument proves the
homogeneous coordinate ring is normal: its singular locus has
codimension at least two in the affine cone. Hence S is the normal
four-A1 degree-four del Pezzo surface, polarized by H=O_S(1).

## 2. An invertible coordinate change and the exact projection

Put [r:p:z:q:t]=[Y0:Y1:Y2:Y3:Y4] and set

    a = p+4z+4q,
    b = -r-3p-2z,
    c = -p-3z-2q,
    d = -z-3q-2t,
    e = p+2z+q.

The five-by-five matrix has determinant 2, so this is a projective
coordinate change. In these coordinates the equations become

    Q1 = pq-z^2,
    Q2 = 7Q1+D+Lz,

where

    L = r-3p-6q+4t,
    D = -p^2-2pq+6pt-4q^2+3qr+2rt.

Project from the center [0:0:1:0:0], deleting z. At the center Q1=-1
and Q2=-7, so the center lies outside S. The projection is a morphism
on S, and it is finite: every fiber is the intersection of S with a
line through the center; a positive-dimensional intersection would
contain that whole line and hence the center, which is impossible.
The morphism is proper with finite fibers and therefore finite.

On the nonempty open L!=0 it has the inverse

    z = -D/L.

Consequently it is birational. Its image is an integral surface X in
P3[r:p:q:t]. Since the polarization is pulled back from O_X(1), the
degree formula gives deg(X)=H^2=4. Eliminating z gives the exact
quartic equation

    F = D^2-pq L^2 = 0.

Indeed this degree-four polynomial vanishes on the image. The
irreducible defining equation of the integral degree-four image must
have that same degree and hence equals F up to a scalar. In
particular the image is a quartic, not a quadric with a degree-two
map. Since S is normal and the morphism is finite and birational,
S is the normalization of X.

## 3. The lifted C0 passes through all four normalization singularities

The rational normal quartic

    c_tilde = [u^4:u^3v:u^2v^2:uv^3:v^4] in P4[r:p:z:q:t]

lies on S by literal substitution into Q1 and Q2. Its projection is
the fixed curve

    C0 = [u^4:u^3v:uv^3:v^4] in P3[r:p:q:t].

This is the standard smooth embedded rational quartic. The projection
restricts to an isomorphism from c_tilde onto C0. In a chart at either
endpoint, respectively p/r=v/u and q/t=u/v give local coordinates;
the remaining points are covered by r!=0 or t!=0, where the same
parameter recovery proves the isomorphism.

In a,b,c,d,e coordinates the lifted parametrization is

    a = uv(u+2v)^2,
    b = -u^2(u+v)(u+2v),
    c = -uv(u+v)(u+2v),
    d = -v^2(u+v)(u+2v),
    e = uv(u+v)^2.

Thus u=0, v=0, u+v=0 and u+2v=0 map respectively to the d,b,a,e
vertices. The smooth lifted curve meets all four A1 singularities.
Its ambient projection remains the smooth C0. This is an actual
degree-four C0 carrier demonstrating that smoothness of the curve
does not force smoothness of its normalization along that curve.

## 4. The actual conductor is a smooth plane conic

Let A=k[r,p,q,t]/(F) and

    B=k[r,p,z,q,t]/(z^2-pq,D+Lz).

As an A-algebra B is generated by z, with module generators 1,z.
To compute B/A completely, first use z^2=pq. Over the polynomial
ring R=k[r,p,q,t], this intermediate ring is free with basis 1,z.
Multiples of D+Lz have coefficient vectors generated by

    (D,L),       (pq L,D).

Thus B has that two-by-two module presentation. Quotienting by the
image of R generated by 1 leaves precisely

    B/A = (R/(L,D))(-1) = (A/(L,D))(-1).

The annihilator of B/A is therefore exactly J=(L,D), which is the
actual conductor ideal downstairs. This proves equality of schemes,
not only equality of supports or a proposed candidate conductor.
Sheafifying yields the actual projective conductor.

On L=0, substitute r=3p+6q-4t and obtain

    D|L = -p^2+7pq+14q^2+12pt-8t^2.

Its symmetric quadratic matrix has determinant -294, so Gamma=V(L,D)
is a smooth plane conic in characteristic zero. Pulling J to B gives
(L), since D=-Lz in B. The upstairs conductor is the Cartier
hyperplane curve E=V(L) on S. It is the degree-two cover of Gamma
given by z^2=pq. The cover has generic degree two and has four distinct
simple branch points, namely Gamma intersect {pq=0}. On p=0 and q=0
the quadratic restrictions of D|L have discriminants 448t^2 in q
and 112t^2 in p, respectively. Neither has a root at t=0. At the
intersection p=q=0 the value is -8t^2. Thus the four points are
distinct, and E is a smooth genus-one
curve. The four A1 vertices have L-values -14,-1,-2,-28, respectively,
so E avoids them.

This smooth-conic conductor is outside the smooth-scroll conductor
Hilbert-polynomial calculation. The normalization here is singular
and anticanonically polarized.

## 5. An actual quadric divisor 2 c_tilde on S

For completeness the original proposed torsion relation can be made
literal. In a,b,c,d,e coordinates take

    Q = ab+ad+be+4de+2ac+2bc+6c^2+4cd+4ce.

Under the finite degree-two map P1xP1->S

    [s0:s1],[h0:h1] |->
    [s0^2 h0^2:s0^2 h1^2:s0s1h0h1:s1^2 h0^2:s1^2 h1^2],

the pullback of Q is f^2, where

    f = s0^2 h0h1+s0s1 h0^2+s0s1 h1^2+2s1^2 h0h1.

The map is finite since the pullback polarization O(2,2) is ample;
its generic degree is two and its involution changes the signs of
s0 and h0 simultaneously. The polynomial f is irreducible: viewed
as a quadratic in h0/h1, its discriminant is s0^4+4s1^4, which has
four distinct roots and is not a square in k(s0/s1). It has no
vertical component. Consequently Q has one irreducible zero-support
curve on S. Direct substitution shows that curve contains c_tilde,
so its support is exactly c_tilde. The cover is unramified at its
generic point, and its pulled-back multiplicity is two. Therefore

    div_S(Q)=2 c_tilde,       2 c_tilde ~ 2H.

In Y coordinates the same quadric is

    Q = -6pq-2pt+pz-qr+2qz+6z^2.

Modulo the surface equation z^2=pq this becomes
(p+2q)z-2pt-qr. The divisor c_tilde is non-Cartier at all four A1
vertices by the smooth-Cartier criterion proved in the companion
singular-local-lift note. Thus the local class there has exact order
two. The torsion is real; a forced c_tilde~H or forced avoidance of
the vertices would be unjustified.

## 6. This particular projected carrier has no mate of any degree

The construction of Q on S does not give a projected mate. In fact
this explicit projection excludes every mate.

On C0 the conductor linear form is

    L|C0=(u^2-4uv+2v^2)(u^2+uv+2v^2).

The two quadratic factors have discriminants 8 and -7 and resultant
50 after v=1. They have four distinct zeros, all with uv!=0.
At each of the corresponding four points of C0, L=D=0 and
pq=(uv)^4 is nonzero. The finite normalization fiber therefore has
exactly the two distinct points

    z = +u^2v^2,       z = -u^2v^2.

Only the first is on c_tilde, because c_tilde->C0 is an isomorphism.
The second is an isolated point of the reduced full inverse image
of C0 off c_tilde. Indeed off L=0 the inverse is uniquely z=-D/L,
so every curve component above C0 must be c_tilde; the extra fibers
occur only at these four points.

If a homogeneous mate G existed, its pullback to the normal integral
surface S would be a nonzero section of O_S(nH) whose zero support
was exactly the full inverse image of C0. Such a section is a
nonzerodivisor and defines a Cartier divisor. It cannot have an
isolated zero off its curve components: every minimal prime of a
nonzero principal ideal in a local domain has height one. At the
second point in any displayed fiber this would require an additional
curve of zeros. Finiteness would map that curve onto C0, contradicting
the uniqueness of the curve component above C0. Thus no mate exists,
in any positive degree.

The explicit quadric also witnesses the descent failure. On the
second lift it takes the value

    -2 u^3v^3(u^2+2v^2),

which is nonzero at all four conductor crossings: the resultant of
L(u,1) with u^2+2 is 64. It vanishes on the first lift. Hence no
positive power of Q can descend as a section pulled back from X.
This last calculation is supplementary; the full fiber argument
already excludes every possible projected mate, not merely powers
of a chosen quadric.

## 7. Verification and scope

The [historical checker](https://github.com/markluxton1/STCI/blob/ab0cf6fddf3bcbeded056eb584186e566e467b30/computations/verify_dp4_projection_local_lift_2026_10_09.py)
checks
the invertible coordinate change, exact quadrics and eliminant,
RNC parametrization, actual module relations, conductor conic,
vertex values, squared-cover quadric, and all conductor crossing
and opposite-fiber identities. The proofs above, rather than the
checker status alone, establish normality, integral degree-four
image, finite birationality, equality of the conductor scheme and
the all-mate obstruction.

The final replay returned exit 0 and `status: PASS` on 2026-10-09.
Source SHA256:
`9cf1ac1ff6d30f1f0415afe59a3b987de06631253dd8359ca6fd55e9040f0dc0`.

The first replay failed at a SymPy structural-equality comparison of
two differently factored expressions for the same discriminant. The
expanded difference was exactly zero. The correction compares that
expanded difference with zero; it changes no mathematical identity.

The [independent proof audit](#source-2026-10-09-session-dp4-projection-independent-auditmd)
accepted the finite birational normalization, actual conductor module
and all-mate fiber obstruction.
Serre's criterion used above is the primary
[Stacks Project lemma](https://stacks.math.columbia.edu/tag/031S).

This is one verified excluded carrier. It does not exhaust the
singular degree-four del Pezzo normalization family, other singular
normalizations, or higher carrier degrees.



## Consolidated historical supplement: `research/supplements/OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md`

# October 9 historical mathematics

This compilation retains the mathematical hypotheses, counterexamples, unsuccessful arguments, and open questions. This compilation supplies no new independent audit.

---

## Source: 2026-10-09-session-singular-delpezzo-four-A1-family-independent-audit.md

# Independent audit of the projected four-A1 family

Date: 2026-10-09. Auditor: `family2_quadratic_independent_audit`, independent of the construction owner. This bounded audit used no child agents and edited no original source or frontier document.

## Verdict and exact scope

**PROVED HERE:** over an algebraically closed field of characteristic zero, every quartic in the displayed family with

```text
alpha*beta*gamma*delta*(alpha*delta-beta*gamma) != 0
```

fails to admit a mate of any degree whose set-theoretic intersection is the exact fixed curve `C0=[U^4:U^3V:UV^3:V^4]`.

The [owner proof](#source-2026-10-09-session-singular-delpezzo-four-a1-familymd) is accepted at this scope. A separate implementation checks the universal coordinate identities. The mathematical proof is the algebra and geometry below, not agreement between agents or a numerical parameter sample. The singular surface, smooth lifted curve, finite birational quartic image, and extra normalization point are bound to the actual fixed coordinates.

This family is not asserted to exhaust all four-A1 embeddings or projections, all genus-one singular normalizations, genus-two normalizations, or the unrestricted STCI problem. The parameter boundary where the displayed transformation becomes singular is outside this construction and outside this theorem.

## 1. The standard surface is integral and normal

Put `S=V(ae-c^2,bd-c^2)` in `P4[a:b:c:d:e]`. Here is a direct domain proof supplementing the owner's quotient-cover argument. In lexicographic order `a>b>c>d>e`, the leading monomials are `ae` and `bd`, which are relatively prime. The two equations therefore form a Groebner basis. Map their quotient ring to a Laurent polynomial ring in independent `r,s,t` by

```text
a -> r, b -> s, c -> t, d -> t^2/s, e -> t^2/r.
```

A standard monomial `a^i b^j c^k d^l e^h` has `i*h=j*l=0`, and maps to `r^(i-h)s^(j-l)t^(k+2l+2h)`. Its Laurent exponents recover `i,h` and `j,l` uniquely, and then recover `k`. Distinct standard monomials have distinct images. The homomorphism is consequently injective, so the quotient is a domain. It has dimension three: it contains algebraically independent `a,b,c` and embeds in their fraction field. The two equations form a height-two complete intersection, and the projective surface is integral of degree four.

The two gradient rows are

```text
(e,0,-2c,0,a),   (0,d,-2c,b,0).
```

Their rank drops exactly at the four projective coordinate vertices with nonzero `a,b,d,e`. The independent source forms all ten minors and verifies that their ideal with the two quadrics contains `c^3`, `(ae)^2`, `(bd)^2`, and the other four cross products in `a,b,d,e`. Conversely every generator vanishes at all four vertices. Its radical is therefore the four-axis ideal. Equivalently, if `c!=0` the minors force all other coordinates to vanish, contradicting a surface equation; with `c=0`, all six cross products vanish and only the four vertices remain.

In the `a=1` chart, eliminate `e=c^2`; the remaining local equation is `bd-c^2=0`. The other three vertices have the same A1 model. The complete intersection is Cohen-Macaulay, hence S2, and its singularities are isolated, hence it is R1. Serre's criterion gives normality. For `H=O_S(1)`, complete-intersection adjunction gives `K_S=-H`, `H^2=4`, and sectional genus one.

## 2. The curve and the coordinate transformation are correctly bound

Write `Delta=alpha*delta-beta*gamma`, `m=alpha*delta+beta*gamma`, and `n=alpha*beta*gamma*delta`. The owner's five-by-five transformation from `Y0,...,Y4` to `a,b,c,d,e` has determinant `n*Delta^3`. It is invertible on the entire specified parameter open. Thus the image of `Y_i=U^(4-i)*V^i`, `i=0,...,4`, is a smooth embedded rational normal quartic, denoted `c_S`. It is a projective change of coordinates of the standard RNC, not a merely generic parametrization. Its actual formulas are

```text
a=UV*(gamma U+delta V)^2,
b=-U^2*(alpha U+beta V)*(gamma U+delta V),
c=-UV*(alpha U+beta V)*(gamma U+delta V),
d=-V^2*(alpha U+beta V)*(gamma U+delta V),
e=UV*(alpha U+beta V)^2.
```

Both surface quadrics vanish identically. The curve passes through all four A1 vertices at four distinct parameters:

| Vertex | Parameter `[U:V]` | Nonzero coordinate value |
|---|---|---|
| `b` | `[1:0]` | `-alpha*gamma` |
| `d` | `[0:1]` | `-beta*delta` |
| `a` | `[beta:-alpha]` | `-alpha*beta*Delta^2` |
| `e` | `[delta:-gamma]` | `-gamma*delta*Delta^2` |

All values are nonzero under exactly the stated hypotheses. Deleting `Y2` gives the exact curve `C0` in the exact retained coordinates. This parametrization is an embedding: on `U!=0`, `x1/x0=V/U`, and on `V!=0`, `x2/x3=U/V`. These two affine charts prove smoothness and injectivity at the endpoints as well.

## 3. The projected image is an integral quartic with this normalization

Put `(x0,x1,x2,x3,z)=(Y0,Y1,Y3,Y4,Y2)`. The complete uniform identities are

```text
Q1=Delta^2*(x1*x2-z^2),
Q2=((m^2-n)/Delta^2)*Q1+z*L+R,

L=alpha^2*gamma^2*x0-alpha*gamma*m*x1
  -beta*delta*m*x2+beta^2*delta^2*x3,

R=alpha*gamma*m*x0*x2+n*x0*x3-alpha^2*gamma^2*x1^2
  -n*x1*x2+beta*delta*m*x1*x3-beta^2*delta^2*x2^2.
```

The independent checker verifies the second identity after clearing only `Delta^2`. Neither `m` nor `m^2-n` is inverted, so their zero loci are included.

The projection center `P=[0:0:1:0:0]` is outside `S`, since `Q1(P)=-Delta^2!=0`. Projection is a morphism. Every fibre is finite: on its projective line, the nonzero quadratic coefficient `-Delta^2` in `z` bounds the fibre by two points, including multiplicities. Properness makes the morphism finite.

On `L!=0`, the inverse is `z=-R/L`, or homogeneously

```text
[x0:x1:x2:x3] -> [L*x0:L*x1:-R:L*x2:L*x3].
```

This is an isomorphism on that open of the image. The open is nonempty because the restriction of `L` to `c_S` has nonzero endpoint values. The map is therefore birational. Its hyperplane pullback is `H`, so the finite degree-one image has degree `H^2=4`. The image `X` is integral, and `S->X` is its normalization since `S` is normal.

The polynomial `F=R^2-x1*x2*L^2` vanishes on the image. Its `x0^2*x3^2` coefficient is `n^2!=0`, so it is a nonzero quartic in every allowed specialization. The integral hypersurface image has degree four, hence `F`, up to a nonzero scalar, is its actual irreducible equation. The exact identity `Res_z(Q1,Q2)=Delta^4*F` is checked separately; irreducibility and birationality do not follow from that resultant alone.

## 4. The extra normalization point excludes every mate

On the exact curve, the independent source verifies

```text
L_C=alpha^2*gamma^2*U^4-alpha*gamma*m*U^3*V
    -beta*delta*m*U*V^3+beta^2*delta^2*V^4,
R_C=-U^2*V^2*L_C.
```

Both endpoint coefficients are nonzero. Over the algebraically closed field this homogeneous quartic has a root `[U:V]`, and every root has `UV!=0`. No squarefreeness is assumed: repeated-root subloci are covered.

At any such root, both points

```text
y_plus =[U^4:U^3V:+U^2V^2:UV^3:V^4],
y_minus=[U^4:U^3V:-U^2V^2:UV^3:V^4]
```

lie on `S` and project to the same point of `C0`. Indeed `Q1` vanishes on both and `Q2(y_minus)=-2U^2V^2*L_C=0`. They are distinct since characteristic zero and `UV!=0` give `2U^2V^2!=0`.

The negative point is outside `c_S`: the quadratic `Y0*Y2-Y1^2` vanishes on the entire RNC, but its value at `y_minus` is `-2U^6V^2!=0`. This excludes membership through a different parameter as well.

Here is the full-support argument without presupposing a singleton-fibre rule. Because the map is finite and is an isomorphism on `L!=0`, every curve in the inverse image of `C0` must dominate `C0` and equal `c_S`: its generic point lies over the generic point where `L_C!=0` and the inverse is unique. Additional points can only lie over the finite zero set of `L_C`.

Suppose a mate `G` of any degree satisfied `V_X(G)_red=C0`. Its pullback is a nonzero section of `O_S(deg G)`, since otherwise `G` would vanish on all of `X`. It vanishes at `y_minus`, which maps into `C0`. Locally trivialize the line bundle there. A nonzero nonunit in the integral surface's local ring has a height-one zero prime by the principal ideal theorem. Hence a curve in the pullback zero support passes through `y_minus`. Its finite image is contained in `C0`, so that curve must equal `c_S`. This contradicts `y_minus` being outside `c_S`.

This excludes every mate degree simultaneously. It requires neither a conductor calculation nor a bound on the mate degree nor cancellation of a multiple curve divisor on a singular surface.

## 5. The auxiliary double-curve and non-Cartier claims also hold

The owner uses the finite quotient cover from `P1xP1` given by its five invariant `(2,2)` sections. They are basepoint free and their torus function field has index two under `(t,u)->(-t,-u)`. For its odd `(2,2)` section, setting `r=t/u` gives

```text
u^2=-(alpha+beta*r)/(r*(gamma+delta*r)).
```

The four branch points `0,infinity,-alpha/beta,-gamma/delta` are distinct under precisely the hypotheses. The double cover is connected and has genus one. No boundary coordinate fibre is a component, because all four coefficients are nonzero. Its integral `(2,2)` closure has arithmetic genus one, so it has no singular defect.

The stated quadric section `Q` pulls back exactly to the square of this odd section. The independent checker verifies that identity and `Q` vanishing on the actual RNC. The odd curve is irreducible, so its finite image is the entire support of `Q`; since the RNC is contained in that support, the image is exactly `c_S`. The cover is unramified at the generic point, as the involution has only four fixed points. Thus the divisor of `Q` is exactly `2c_S`, giving `2c_S~2H`.

At each A1 vertex the curve is non-Cartier. Its curve local ring is regular of dimension one, whereas the surface local ring has embedding dimension three. Quotient by one element could decrease embedding dimension by at most one, leaving at least two; the curve ideal therefore cannot be principal. Together with the Cartier divisor `2c_S`, its nonzero local class has order two. On the minimal resolution the smooth curve meets each exceptional `(-2)` curve once: its three A1 chart coordinates vanish to first order, so its tangent direction lifts to one transverse point on the exceptional conic. The correction is half the sum of the four exceptional curves, of square `-2`. This validates the auxiliary identity `q=2pi=2`. The exclusion itself is already proved in section 4.

## 6. Exact computational support

The independent
[countercheck](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/validation/2026-10-09-four-A1-family-audit/countercheck.py)
uses universal parameters. It verifies the coordinate, cancellation,
resultant, actual-curve, singular-locus, local-A1, cover-square,
branch-equation and extra-point identities. The [historical owner checker](https://github.com/markluxton1/STCI/blob/ab0cf6fddf3bcbeded056eb584186e566e467b30/computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py)
records the original implementation.

Run the independent controls from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  research/validation/2026-10-09-four-A1-family-audit/countercheck.py
```

The algebra and geometry above establish the accepted exclusion for this
explicit family. The global question and singular-normalization strata
outside that family remain open.


---

## Source: 2026-10-09-session-singular-delpezzo-four-A1-family.md

# A genus-one four-A1 normalization family for fixed C0

Date: 2026-10-09. Owner: `singular_normalization_next_frontier`.
Status: **PROVED HERE, submitted for independent audit**. Uniform
exclusion of the displayed family in every mate degree; no assertion
that this family exhausts all singular normalizations of genus one.

This note follows the [sectional-genus reduction](../supplements/SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md).
The remaining quartic normalization lane has pi=1 or pi=2 and a
non-Cartier smooth lifted curve passing through Sing(S). The example
here realizes the genus-one numerical and torsion conditions with
the actual fixed C0, then excludes its projected quartics by their
full inverse-image fibers. Thus existence of those numerical and
torsion conditions is weaker than existence of a mate.

Throughout k is algebraically closed of characteristic zero. Set

    C0=[U^4:U^3 V:U V^3:V^4] subset P3.

## 1. The singular del Pezzo normalization

In P4[a:b:c:d:e], let

    S:  a e=c^2,       b d=c^2.

This is an integral degree-four complete intersection. One direct
description is the quotient of P1[u0:u1] times P1[v0:v1] by the
involution (u1,v1)->(-u1,-v1), with invariant sections of O(2,2)

    a=u0^2 v0^2, b=u0^2 v1^2, c=u0u1v0v1,
    d=u1^2v0^2, e=u1^2v1^2.

They have no common zero, and the resulting map is generically of
degree two: on the torus its invariant function field is
k((u1/u0)^2,(v1/v0)^2,(u1/u0)(v1/v0)). The image is integral of
degree (2,2)^2/2=4 and is contained in the two independent quadrics.
Those quadrics form a codimension-two complete intersection of
degree four, so their scheme is this integral image. Equivalently
one can use the toric ring with relations a e=c^2=b d; its dense
torus and the reduced coordinate boundary give the same conclusion.

The singular points of S are exactly the four coordinate vertices
with nonzero a,b,d, or e. In the a!=0 chart, eliminating e gives
b d=c^2, the A1 surface singularity at its origin; the other three
charts have the same local equation. All other points have independent
quadric gradients. The surface is S2 by the complete-intersection
property and R1 by its isolated singularities, hence normal.

Write H=O_S(1). Adjunction gives K_S=-H and H^2=4. A general
hyperplane section therefore has genus one. This is a singular
normalization outside the accepted smooth F0/F2/P2 lanes.

## 2. A smooth rational quartic with 2c linearly equivalent to 2H

Choose parameters alpha,beta,gamma,delta satisfying

    alpha beta gamma delta Delta != 0,
    Delta=alpha delta-beta gamma,     M=alpha delta+beta gamma.

The odd (2,2) section on the quotient cover is

    f=alpha u0^2v0v1 + beta u0u1v0^2
      + gamma u0u1v1^2 + delta u1^2v0v1.

Its curve is smooth elliptic. For instance, on the torus put
t=u1/u0, u=v1/v0, and r=t/u. Dividing f by u gives

    u^2=-(alpha+beta r)/(r(gamma+delta r)).

The four branch points 0, infinity, -alpha/beta, -gamma/delta
are distinct on the stated parameter open. The connected degree-two
cover has genus one; the integral (2,2) closure already has arithmetic
genus one, so it has no singular defect. Its quotient is a smooth P1.

More concretely, introduce the standard rational normal quartic
coordinates

    Y_i=U^(4-i)V^i,       i=0,...,4.

Its image in S is obtained by the linear transformation

    a=gamma^2 Y1+2 gamma delta Y2+delta^2 Y3,
    b=-alpha gamma Y0-M Y1-beta delta Y2,
    c=-alpha gamma Y1-M Y2-beta delta Y3,
    d=-alpha gamma Y2-M Y3-beta delta Y4,
    e=alpha^2 Y1+2 alpha beta Y2+beta^2 Y3.

The determinant of this transformation is

    alpha beta gamma delta Delta^3.

It is therefore a projective change of coordinates on the whole
parameter open. Substituting the binary quartics into the two equations
of S gives zero. Its image, denoted c, is a smooth rational normal
quartic of degree four passing through all four A1 vertices, at the
four distinct branch parameters recorded above.

The square of the odd section is the invariant quadric section

    Q=alpha^2 a b+beta^2 a d+gamma^2 b e+delta^2 d e
      +2c(alpha beta a+alpha gamma b+beta delta d+gamma delta e)
      +2(alpha delta+beta gamma)c^2.

Its pullback is exactly f^2. On S its divisor is exactly 2c, because
the quotient map is finite and generically unramified over that curve.
Consequently 2c~2H. The curve c is non-Cartier at the four A1 points;
its local class has order two, as in the
[local lift countershield](#source-2026-10-09-session-singular-local-liftmd).
On the minimal resolution the correction is half the sum of the four
disjoint (-2) curves, so q=-Z^2=2. This realizes the surviving identity
q=2pi for pi=1. No descent of Q to a projected quartic is assumed.

## 3. Projection gives integral quartics containing the exact fixed C0

Use the inverse coordinates Y0,...,Y4 of section 2 and project by
deleting Y2. Put

    (x0,x1,x2,x3,z)=(Y0,Y1,Y3,Y4,Y2).

The image of c is exactly the displayed C0. Let Q1=a e-c^2 and
Q2=b d-c^2, now expressed in these coordinates. Their complete
identities are

    Q1=Delta^2(x1 x2-z^2),
    Q2=-A2(x1 x2-z^2)+L z+R,
    A2=-(alpha^2delta^2+alpha beta gamma delta+beta^2gamma^2),

where

    L=alpha^2gamma^2 x0-alpha gamma M x1
      -beta delta M x2+beta^2delta^2 x3,

    R=alpha gamma M x0x2+alpha beta gamma delta x0x3
      -alpha^2gamma^2 x1^2-alpha beta gamma delta x1x2
      +beta delta M x1x3-beta^2delta^2 x2^2.

The center P=(Y0,Y1,Y2,Y3,Y4)=(0,0,1,0,0) has Q1(P)=-Delta^2,
so it is disjoint from S. The projection is a morphism, and is finite
because its pullback O(1)=H is ample. The coefficient of x0 in L
is alpha^2gamma^2!=0. On the dense open L!=0 the equation L z+R=0
recovers z=-R/L. Thus the map S->X subset P3 is birational, not a
degree-two projection onto a quadric.

Since S is normal and the map is finite birational, it is the
normalization of its image X. The image has degree four and is integral.
Its equation, up to a nonzero scalar, is

    F=R^2-x1 x2 L^2.

Indeed eliminating z gives

    resultant_z(Q1,Q2)=Delta^4 F.

The geometric finite-birational degree calculation proves that F is
the actual integral quartic equation; an uncancelled resultant alone
would not suffice to prove that statement. There is no nonzero scalar
specialization in this parameter open that destroys the argument.

## 4. Uniform full-fiber obstruction to every mate

The lifted c is the rational normal quartic with

    (x0,x1,x2,x3,z)
       =(U^4,U^3V,UV^3,V^4,U^2V^2).

The pullback of L to C0 is the nonzero binary quartic

    L_C=alpha^2gamma^2 U^4-alpha gamma M U^3V
        -beta delta M UV^3+beta^2delta^2 V^4.

Its endpoint values are

    L_C(U,0)=alpha^2gamma^2 U^4,
    L_C(0,V)=beta^2delta^2 V^4.

Therefore it has a zero [U:V] over k and every zero has U V!=0.
Repeated roots and special parameter values are allowed here; the
proof does not assume L_C squarefree. At any such zero,

    R_C=-U^2V^2 L_C=0,
    z^2=x1x2=U^4V^4 != 0.

The two distinct points

    [U^4:U^3V:+U^2V^2:UV^3:V^4],
    [U^4:U^3V:-U^2V^2:UV^3:V^4]

both lie on S and project to the same point of C0. Only the plus
point belongs to c. The C0 parametrization is an embedding, so the
four retained coordinates determine [U:V] uniquely; they cannot be
the retained coordinates of a different parameter on c. Characteristic
zero and U V!=0 make the two points distinct.

Thus the entire inverse image of C0 has an additional point outside
its unique curve lift c. A mate would require its entire support to
be exactly c and nu|c to be an isomorphism. Equivalently this
normalization fiber would have to be a singleton. The two explicit
points contradict that necessary condition.

**Theorem.** Every quartic X in the entire parameter open of section
2 is excluded as a carrier of a mate for fixed C0, in every mate
degree. This includes all repeated-root subloci of L_C in that open.

## 5. Exact controls and independent records

The [historical uniform checker](https://github.com/markluxton1/STCI/blob/ab0cf6fddf3bcbeded056eb584186e566e467b30/computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py)
reconstructs the actual five-by-five transformation, its determinant,
the two quadratic equations, the elimination identity and its scalar,
the C0 coordinate restriction, both normalization points over every
L_C zero, and the quotient-cover equality q*Q=f^2. Its identities
are over Q[alpha,beta,gamma,delta]; it does not replace parameter
coverage by a finite sample. The geometry and proof of the full-fiber
obstruction are the text above.

The first source run was terminal exit zero with PASS in 0.47 seconds.
Source SHA256:

    0e72ced585c9e1135648b5e9a278c09964c6677009f50554aac46a68d3b6cef4

The uniform parameter open is the one stated in this proof. The
[retained independent family audit](#source-2026-10-09-session-singular-delpezzo-four-a1-family-independent-auditmd)
treats the family proof; the explicit alpha=beta=gamma=1,delta=2 example
below includes its actual conductor. The family exclusion remains
separate from an unrestricted STCI claim.

For that example,

    L=x0-3x1-6x2+4x3,
    R=-x1^2-2x1x2+6x1x3-4x2^2+3x0x2+2x0x3,
    L_C=(U^2-4UV+2V^2)(U^2+UV+2V^2).

All its conductor intersections likewise have U V!=0. The actual
conductor calculation is useful evidence but is not needed by the
uniform support proof, which already uses the actual finite
normalization and two distinct fiber points.

## 6. Scope of the progress

The construction proves that pi=1, non-Cartier c through isolated
normalization singularities, b c~bH, and even 2c~2H can occur on
actual integral quartic carriers of the fixed C0. Those facts alone
do not justify a minimal-degree reduction. The complete normalization
fiber condition excludes the displayed family.

Parameters with alpha beta gamma delta Delta=0 make the displayed
five-coordinate transformation singular. They are not part of this
normalization construction, and no claim about quartic carriers
obtained by another construction at those degenerations is made.
Other four-A1 projections, the A3+2A1 torsion configuration, other
genus-one singular normalizations, and genus-two normalizations still
require a structural argument or an exhaustive correctly scoped
classification. No frontier file has been edited by this
owner note.


---

## Source: 2026-10-09-session-singular-local-lift-independent-audit.md

# Independent audit of the singular local lift

**Accepted, with the scheme-versus-support distinction below.** This is a
countershield in characteristic different from 2, using a smooth conic, not the
fixed degree-four curve `C0`. The universal STCI question remains open.

The proposed rings are
`B=k[x,g,v]/(v^2-4*x*g)` and
`A=k[x,g,w]/((w+(x-g)^2)^2-4*(x+g)^2*w)`, with
`w=(x+g+v)^2`. The quadratic discriminant in `w` is
`64*x*g*(x+g)^2`, nonsquare in `k(x,g)`, so `A` is a domain.
`B` is finite over `A`, generated by `1,v`; the rational expression
`v=(w-x^2-6*x*g-g^2)/(2*(x+g))` proves equality of fraction fields.
The quadric cone `B` is Cohen--Macaulay with an isolated singularity, hence
normal. Therefore it is the normalization of `A`.

The smooth prime divisor `c=(g,v)` maps isomorphically onto the smooth curve
`C=(g,w-x^2)`. Its divisor satisfies `div_B(g)=2*c`. At the cone vertex its
ideal has two minimal generators, so `c` is non-Cartier there and has exact
local divisor-class order two. The derivative identity
`F_g|C=-16*x^3` verifies generic order one of the quartic carrier.

The essential correction is

\[
I_C B=(g,xv),\qquad \sqrt{I_C B}=(g,v).
\]

Thus the inverse image has exactly `c` as its **full support**, but its scheme
is `k[x,v]/(v^2,xv)` and contains a nilpotent supported at the origin. An
argument requiring a reduced scheme-theoretic inverse image cannot use this
example unchanged.

Homogenizing yields an integral quartic whose plane section `g=0` is exactly
`(wt-x^2)^2`, a double smooth conic. This supplies a projective STCI
countershield to a blanket exclusion of singular normalization points along
smooth curves. No claim about the inverse-image scheme at infinity is needed
or made here.

The independent audit directly checked all polynomial identities with SymPy.
The owner's self-contained checker is
[historical checker](https://github.com/markluxton1/STCI/blob/ab0cf6fddf3bcbeded056eb584186e566e467b30/computations/verify_singular_local_lift_countershield_2026_10_09.py),
reported terminal `PASS`; the main note is
[2026-10-09-session-singular-local-lift.md](#source-2026-10-09-session-singular-local-liftmd).
A longer independent proof is preserved in
[2026-10-09-singular-normalization-local-countershield-audit.md](#source-2026-10-09-singular-normalization-local-countershield-auditmd).


---

## Source: 2026-10-09-session-singular-local-lift.md

# Smooth lifted curves can meet singular normalization points

Date: 2026-10-09. Author: `singular_local_lift`, subagent of
`singular_normalization_next_frontier`.

Status: **PROVED HERE**, by the explicit algebra below. The universal
STCI problem and the fixed rational quartic C0 problem remain open.
This note provides a local countershield and a surviving local class
group criterion. It makes no classification claim about quartic
normalizations.

## 1. Precise surviving criterion

Let (R,m) be a normal Noetherian local ring of dimension two, and let
P be a height-one prime such that R/P is regular of dimension one.
Thus the reduced curve c defined by P is smooth at the closed point.

**The curve c is Cartier at that point if and only if R is regular.**

For the forward implication, write P=(f). The maximal ideal of R/P
has one generator. Lift that generator to a in m. Then m=(a,f), so
the embedding dimension of R is at most two. Since dim R=2, R is
regular. Conversely a regular local ring of dimension two is a UFD,
so P is principal.

Suppose a mate reduction gives b c Cartier, for an integer b>0. At a
singular point of c, the local divisor class [c] is consequently a
nonzero torsion class, of order dividing b. In particular, if the
local class group is torsion free, c cannot pass through that point.
The same conclusion holds for a locally factorial normalization.

The relation bH=b c in the Weil divisor class group only proves that
[c-H] is killed by b. Without an argument controlling torsion, it does
not prove c is Cartier, c~H, or the existence of a section f with
div(f)=c. This is the exact limitation relevant to the remaining
singular-normalization frontier.

## 2. An affine quartic with isolated singular normalization

Work over an algebraically closed field k of characteristic zero.
Put

    B = k[x,g,v]/(v^2-4xg),
    y = x+g+v,
    w = y^2,
    F = (w+(x-g)^2)^2-4(x+g)^2 w,
    A = k[x,g,w]/(F).

The assignments x->x, g->g, w->(x+g+v)^2 identify A with a subring
of B. To see that the displayed hypersurface is integral, regard F as
a monic quadratic in w over k(x,g). Its discriminant is

    64 x g (x+g)^2,

which is not a square in k(x,g). Gauss's lemma makes F irreducible in
k[x,g,w]. Its image vanishes in B. Since x,g are algebraically
independent in B, the image has dimension two, so its defining prime
ideal is exactly (F).

In B the element y satisfies both

    y^2=w,
    y^2-2(x+g)y+(x-g)^2=0.

Thus B=A[y] is finite over A, with v=y-x-g. Moreover

    y = (w+(x-g)^2)/(2(x+g))

in the fraction field. The denominator is a nonzero element of A,
so Frac(A)=Frac(B): the map is birational.

The ring B is normal. The hypersurface equation v^2-4xg has gradient
(-4g,-4x,2v), so the only singular point is the origin. A hypersurface
is Cohen--Macaulay; here it is regular in codimension one. Serre's
criterion therefore proves normality. Its embedding dimension at the
origin is three and its dimension is two, so that point is singular.
This is the ordinary A1 surface singularity. Since B is normal,
integral over A, and has the same fraction field, it is the full
integral closure of A: an element of Frac(A) integral over A is also
integral over B and hence belongs to B.

Therefore Spec B is the finite birational normalization of the
integral affine quartic Spec A.

## 3. The smooth curve, full support, and mate

Let

    c = V(g,v) in Spec B,
    C = V(g,w-x^2) in Spec A.

Both coordinate rings are k[x], and the restriction of normalization
is the identity on x. Thus c and C are smooth, c->C is an
isomorphism, and C is an embedded smooth parabola in affine
three-space. At the origin its parametrization (x,g,w)=(t,0,t^2)
has nonzero derivative (1,0,0).

The full reduced inverse image of C is c. Indeed v^2=4xg gives
v in sqrt((g)), and

    w-x^2 = 2xv + g(6x+g+2v) in B.

Consequently sqrt((g,w-x^2)B)=(g,v). There is no second normalization
branch lying above C.

The scheme-theoretic inverse image is not asserted to be reduced:
its ideal is (g,xv). Modulo g its coordinate ring is
k[x,v]/(v^2,xv), which retains a nilpotent supported at the origin.
The support assertion and the isomorphism of reduced curves are the
precise statements used here.

The Weil divisor of g in Spec B is exactly 2c. Its zero set has only
the prime (g,v). At that prime x is a unit and v is a uniformizer:
g=v^2/(4x). Hence the valuation is exactly two.

Downstairs the plane g=0 is a mate, since

    F(x,0,w)=(w-x^2)^2.

The surface is smooth at the generic point of C. Substituting g=0,
w=x^2 into the gradient of F gives

    (F_x,F_g,F_w)|C = (0,-16x^3,0).

Thus this example also has carrier order one at the generic point of
C. It does not rely on C being a component of a generic nonnormal
locus. Nevertheless c meets the isolated singular point of the
normalization and its ambient image remains smooth and immersed.

Finally c is not Cartier at the origin. The prime ideal (g,v) needs
two generators there: their independent degree-one classes survive
modulo m(g,v), whose homogeneous terms start in degree two. A
principal ideal in a local ring has at most one generator. Therefore
the local class [c] is nonzero. The relation div(g)=2c shows that
its order is exactly two.

## 4. Projective quartic countershield, with degree explicitly retained

The homogenization in P3 with coordinates [x:g:w:t] is

    F_h = (wt+(x-g)^2)^2-4(x+g)^2 wt.

It is an integral quartic: its affine chart t=1 is integral by the
argument above, and t is not a factor of F_h. The plane g=0 cuts

    F_h|g=0 = (wt-x^2)^2.

The reduced intersection is the smooth projective conic
g=0, wt=x^2. Its gradient on that plane is (-2x,t,w), which never
vanishes at a projective point. The normalization of this projective
quartic restricts on t=1 to Spec B, so the lifted conic certainly
passes through the isolated singular normalization point established
above, while mapping isomorphically in its affine neighbourhood.

The curve here has degree **two**, not degree four. In particular this
is not a mate for the fixed rational quartic C0. We do not assert that
the projective full inverse image of the conic has a single smooth
component at the point t=0; the verified local countershield already
invalidates a local smooth-lift avoidance claim. The explicit plane
mate for the projective conic is, however, an actual global STCI.

## 5. Consequence for the continuation frontier

The implication

    smooth lifted curve + embedded smooth image + full mate support
    + order-one generic carrier  =>  avoidance of Sing(normalization)

is false as a local statement, even for an affine quartic. An
argument specifically using degree four for C0, its global divisor
class, or a classification of the possible normalization singularities
may still exclude the remaining cases. It must supply that additional
input explicitly. The accepted smooth F0/F2 normalization results do
not acquire a singular-normalization extension from this local step.

## 6. Exact verification and sources

The [historical checker](https://github.com/markluxton1/STCI/blob/ab0cf6fddf3bcbeded056eb584186e566e467b30/computations/verify_singular_local_lift_countershield_2026_10_09.py)
verifies the literal normalization relations, birational recovery
identity, discriminant, pulled-back curve equation, mate restriction,
generic gradient and projective homogenization. The geometric proofs
above supply normality, finiteness, divisor valuation and the local
Cartier criterion; the script does not label those conclusions proved
merely because a polynomial identity passed.

Terminal replay on 2026-10-09 returned exit 0 and `status: PASS`.
Source SHA256:
`edb3a209b026fd2cbde4a11335087fce7430b291e6380b4774f62ca2415aa503`.
The [independent proof audit](#source-2026-10-09-singular-normalization-local-countershield-auditmd)
accepts the example and checks the nonreduced inverse image scheme. Independent agreement is additional audit evidence;
the mathematical proof remains the explicit argument above.

Normality uses the primary
[Stacks Project, Serre's criterion](https://stacks.math.columbia.edu/tag/031S).
The normalization identification also uses the definition of a normal
domain as integrally closed in its fraction field in the
[Stacks Project, normal rings](https://stacks.math.columbia.edu/tag/037B). All other
algebra in the countershield is explicit in this note. No novelty claim
is made.


---

## Source: 2026-10-09-singular-normalization-local-countershield-audit.md

# Singular-normalization countershield: independent audit

Status: **PROVED**, for an algebraically closed field of characteristic different
from 2. This example concerns a smooth degree-two curve, not the fixed rational
quartic `C0`. It prevents a general argument from excluding a singular point of
the normalization merely because the downstairs curve is smooth and has a
set-theoretic complete-intersection mate.

Let

\[
B=k[x,g,v]/(v^2-4xg),\qquad y=x+g+v,\qquad w=y^2,
\]

and put

\[
F=(w+(x-g)^2)^2-4(x+g)^2w,
\qquad A=k[x,g,w]/(F).
\]

The discriminant of `F`, viewed as a monic quadratic in `w`, is
`64*x*g*(x+g)^2`. It is not a square in `k(x,g)`: the valuations at the prime
elements `x` and `g` are odd. Thus `F` is irreducible, and substitution of
`w=(x+g+v)^2` embeds `A` in `B`. The kernel has height one and contains the
irreducible polynomial `F`, so it equals `(F)`.

The ring `B` is finite over `A`, generated as an `A`-module by `1,v`, since
`v^2=4xg`. It has the same fraction field because

\[
v=\frac{w-x^2-6xg-g^2}{2(x+g)}.
\]

The quadric cone `B` is normal: it is a hypersurface, hence Cohen--Macaulay,
and its singular locus consists only of the origin in this two-dimensional
surface. Therefore it satisfies Serre's `S2` and `R1` conditions. Consequently
`B` is exactly the finite birational normalization of `A`.

The prime divisor `c=(g,v)` has coordinate ring `k[x]`. Its image is
`C=(g,w-x^2)`, also with coordinate ring `k[x]`, and the restricted map is an
isomorphism. At the generic point of `c`, `x` is invertible and
`g=v^2/(4x)`, so `div_B(g)=2c`. At the origin the ideal `(g,v)` has two
independent generators modulo the maximal ideal times this ideal; it is not
principal. Hence `c` is non-Cartier at that point, and its local divisor class
has exact order two.

The **scheme-theoretic** inverse image of `C` is

\[
(g,w-x^2)B=(g,xv).
\]

Its radical is `(g,v)`, so its full support is precisely `c`. Its quotient is
`k[x,v]/(v^2,xv)`; the nilpotent `v` is supported at the origin. The claim is
about support, not equality with the reduced inverse-image scheme.

Differentiation gives `F_g|C=-16*x^3`. Thus `F` has order one along the generic
point of `C`, although the normalization is singular at the point over its
origin and the lifted curve is non-Cartier there.

Homogenize with coordinates `[x:g:w:t]`:

\[
F_h=(wt+(x-g)^2)^2-4(x+g)^2wt.
\]

The homogenization is irreducible because its dehomogenization is irreducible
and it is not divisible by `t`. Its plane section is exactly

\[
F_h\vert_{g=0}=(wt-x^2)^2.
\]

The conic `g=0, wt=x^2` is smooth, and the intersection scheme of the integral
quartic surface with the plane `g=0` is its double. The normalization over the
chart `t=1` is `Spec B`, so it really has a singular point above this smooth
conic. This gives a projective set-theoretic complete-intersection example,
with generic multiplicity two, rather than only a formal local model.

An independent SymPy calculation on 2026-10-09 verified the normalization
substitution modulo `v^2-4*x*g`, the displayed discriminant, the rational
inverse identity, `F_g|C`, and the squared conic plane section. All remainders
were zero where required. These calculations check identities; the arguments
above establish normality, finiteness, irreducibility, and divisor behavior.

No conclusion about the fixed degree-four curve `C0`, or the universal STCI
problem, follows from this example.



## Consolidated historical supplement: `research/supplements/QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md`

# Quintic A4 conductor contact and actual sextic support incidence

Fix the accepted anticanonical degree-five A4 pair and an actual admissible
finite birational nonendpoint projection in characteristic zero, with
\(\delta\ne0\). The curve is the fixed embedded
\(C_0=[s^4:s^3t:st^3:t^4]\). The complete conductor module and octic are
proved in [the conormal/conductor home](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md);
actual target fibers and SUP, the full reduced inverse-support condition,
are in [the target-fiber home](quintic_conductor_geometry.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions).
The [complete homogeneous gcd cover](quintic_conductor_geometry.md#nonendpoint-residual-cubic-pairs-complete-contact-and-coefficient-proof)
supplies the degree-two conormal stratum used below.

This chapter proves the homogeneous differential factor, logarithmic
support criteria, actual sextic incidence, intrinsic A4 contact bounds,
and regular-L2 all-mate consequence. These are independently reviewed
reductions and scoped exclusions. The distinct finite-chart
quadratic norm calculation retains its captured-arithmetic status and
review boundary. Support of an octic, actual full inverse support, and
nonlinear conductor power descent remain separate conditions; the
unrestricted quintic and STCI questions are not closed.

Use \(x=r/\delta=T/S\), \(p=\delta/r=S/T\), and \(j=\bar J\).
The intrinsic A4 point is \(S=0\), while \(x=0\) is target
\(p=\infty\). The actual conductor octic in source coordinates is
\(F_{\rm src}(1,x)=x^8F_{\rm det}(1/x,1)\). The two affine parameters
are reciprocal. The scalar and source-coordinate conventions below
retain all repeated roots, infinity and fixed-degree drops.

<a id="2026-10-14-generalization-quintic-h2-conductor-quotient"></a>
<a id="2026-10-14-generalization-quintic-h2-conductor-factor-independent-audit"></a>

## The degree-two conormal divisor divides the actual octic

### 1. The actual restricted differential module

For any ring inclusion A into B with conductor I, one has

    I Omega_(B/A)=0.                                      (1)

For a in I and b in B, both a and ab belong to A, so
a db=d(ab)-b da=0 in the relative differential module. The db generate
that module. This argument holds before source localization and hence
also after localizing at any source point or tensoring with the curve.
In particular it does not require a singleton normalization fiber or
the full inverse-support hypothesis.

Let q be a finite point of the accepted source curve c. The source
surface is smooth there with regular parameters (u,T), where c is T=0.
The map c to C0 is an isomorphism. Choose a target curve parameter y
and balanced target normal coordinates U,V. Their pullbacks restricted
to c have differentials

    dy=alpha du+beta dT,       alpha a unit,
    dU=u1 dT,                 dV=v1 dT.                  (2)

The normal derivatives have no du contribution because U and V vanish
identically on c. The target coordinates (y,U,V) form a regular ambient
coordinate system: the balanced replacement of the two normal
coordinates is triangular with invertible linear part. Thus the image
of the pulled-back target cotangent module is generated by the three
displayed differentials. Passing from ambient cotangents to those of
the hypersurface introduces relations among these generators but does
not change their image in the source cotangent module.

After tensoring the cotangent cokernel with O_c, eliminating du by dy
gives the exact local description

    Omega_(S/X) tensor O_c
        = O_c/(u1,v1) times the local normal frame dT.   (3)

This is a cokernel computation; no left-exactness of tensor product is
being assumed. The accepted explicit conormal formulas give

    V_T=P(r)/r^7,       U_T=J(r)/(2r^7)

where r is nonzero. At r=0 the accepted opposite chart replaces r^7
by (r-delta)^7 and interchanges the two components by nonzero constant
factors. Since delta is nonzero, these cover every finite source
point with unit denominators. Replacing r by delta*x also multiplies
the normalized cubic pair by units. Consequently (u1,v1) is precisely
the local ideal generated by the two corrected cubic sections.

In the DVR O_(c,q), its order is the full minimum of the two cubic
orders. This includes a repeated common root and gives

    (u1,v1)=(local equation of H),
    Ann_Oc(Omega_(S/X) tensor O_c)=(u1,v1).             (4)

The accepted actual ambient conductor quadric pulls back to a generator
of the entire upstairs conductor ideal, up to a local unit. Equation
(1), restricted to c, therefore implies

    Fsrc belongs to (u1,v1),
    ord_q(Fsrc) >= ord_q(H).                           (5)

This is a lower bound on the conductor's actual local multiplicity.
It asserts neither equality nor an upper bound, and uses the actual
conductor in addition to first-normal data.

### 2. The intrinsic A4 point and homogeneous divisibility

Use source homogeneous coordinates (S,T) with

    x=r/delta=T/S,         p=delta/r=S/T.

The only source point on c not covered by section 1 is the intrinsic
A4 point S=0. On the complete accepted h2 cover this point occurs in
H at most once: double infinity is impossible. If it occurs, both
cubic leading coefficients vanish, whence

    g=3b-2a,             d=4b-3a,
    j=Jbar=d-2g+2b-a=0.

The accepted exact value Fdet(0,1)=-3 j Delta1 then gives
Fdet(0,1)=0. This is the zero at source S=0, so it supplies at least
the one unit of conductor order required there. No calculation of
relative differentials at the singular A4 point is needed.

Together with (5) at every finite point, this proves

    H divides Fsrc as homogeneous binary forms.        (6)

The accepted nonzero conductor restriction has homogeneous degree
eight. For degree H=2, the quotient Q=Fsrc/H is therefore a nonzero
homogeneous sextic, even when its affine degree drops. The proof uses
no inverse of the finite-cover determinant and hence retains its
repeated-root and infinity-once strata. It only claims (6) for the
actual admissible finite birational quintic projections covered by the
accepted premises; no admissibility claim for an arbitrary coefficient
pair follows.

### 3. Common-coordinate correction

With p=S/T and x=T/S, the common-coordinate binary octic is

    Fsrc(S,T)=Fdet(S,T),
    Fsrc(1,x)=x^8 Fdet(1/x,1).                         (7)

The equality in the first line uses the same ordered homogeneous
variables for the target p coordinate and the reciprocal source x
coordinate. It does not identify their affine parameters. In this
coordinate, the intrinsic A4 point is the linear form Pinf=S, and
source x=0 is target p=infinity.

If the previously captured coefficients describe
B(t)=sum c_i t^i=Fdet(1-t,1), up to their recorded common scalar, then

    Fsrc(1,x)=sum c_i (x-1)^i x^(8-i),
    g_j=(-1)^(8-j) sum_(i=8-j)^8 binomial(i,8-j)c_i.    (8)

Expanding the summands proves the second identity directly. The
inverse polynomial transformation is

    B(t)=(1-t)^8 Fsrc(1,1/(1-t)).                     (9)

Equations (8)-(9) are an invertible constant binary-coordinate
transformation. They preserve all fixed-degree leading drops. They
also preserve a nonzero coefficient vector and its common parameter
content. This confirms the coordinate repair in attempt05; the earlier
attempt04 vector cannot be paired with H=x^2+v*x+w as an actual h2
incidence.

The scalar comparison to the actual octic remains subject to the
original denominator, removed-content and inverse-map restrictions.
An invertible coordinate transformation does not extend that rational
map to its exceptional boundary.

### 4. Sextic support equations and exact coefficient signs

Since H is nonzero and (6) holds, support of Fsrc=H Q is contained in
support of H Pinf^epsilon precisely when the same holds for Q. This
follows by taking the union of the two supports, and needs no condition
on their intersection or root multiplicities.

For K a nonzero binary form, put

    D_K=K_T partial_S-K_S partial_T.

The independently audited characteristic-zero Hamiltonian criterion
says that support of a nonzero Q lies in K precisely when Q divides
D_K Q. Applying it to quadratic H and cubic H Pinf gives one incidence
for the complete A4 allowance:

    D_(H Pinf) Q=L Q,       L homogeneous of degree one,
    j D_H Q=mu Q,          mu a scalar.                (10)

For j nonzero the second equation forces support in H, and the first
then holds automatically. For j=0, Q nonzero forces mu=0, and the
first equation permits precisely support in H Pinf. This includes a
repeated H, Pinf already dividing H, and infinity. The statement is
about geometric points over the characteristic-zero field, with H and
Q nonzero; it does not assert a witness-lifting theorem over arbitrary
nonreduced parameter bases.

The product rules have a necessary correction term in the cubic case:

    D_H(H Q)=H D_H Q,
    D_(PH)(H Q)=H[D_(PH)Q-(D_H P)Q].                 (11)

Indeed D_(PH)=P D_H+H D_P and D_P H=-D_H P. For P=S,
D_H P=H_T, so the correction is -H_T Q. It is a linear multiple of
Q and is absorbed in the unrestricted L of (10). The linear quotient
for the original octic and that for the sextic must therefore not be
identified without this shift.

For a binary form of degree n, dehomogenization on S=1 gives

    D_K Q=n k'(x)q(x)-degree(K) k(x)q'(x).           (12)

Use n=6 and H(1,x)=x^2+vx+w. For q_i=0 outside 0 through 6, the
quadratic action has coefficients

    d_i=(6-2i)v q_i+(14-2i)q_(i-1)-2(i+1)w q_(i+1),

and the cubic action for P=S has coefficients

    e_i=(6-3i)v q_i+(15-3i)q_(i-1)-3(i+1)w q_(i+1).

These are exactly the attempt06 formulas, with d through degree six
and e through degree seven. In particular the cubic uses homogeneous
degree three despite its affine polynomial being the same H(x).
The product rules in that source are exactly (11) dehomogenized.

The quadratic action on Sym^6 has characteristic polynomial

    mu*(mu^2-4Delta)*(mu^2-16Delta)*(mu^2-36Delta),
    Delta=v^2-4w.

This follows from eigenvalues 1 and -1 times a square root of Delta
on the two-dimensional representation and the seven weights of its
sixth symmetric power. Polynomial continuation gives the same formula
at Delta=0, where it is mu^7. This identity is not an eigenvector
existence or incidence-emptiness assertion for the actual family.

### 5. Supplementary Hessian criterion

The additional proposed criterion, independently checked in a separate
worker calculation, is also valid. Let A=Hess(Fsrc), a degree-twelve
form, and Q=Fsrc/H a degree-six form. Then

    J(A,Q)=0 iff A=kappa Q^2 for a scalar kappa.        (13)

After dehomogenizing, the Jacobian is six times q*a'-2a*q', so its
vanishing says the rational function a/q^2 has derivative zero. In
characteristic zero this function is constant; the case A=0 is
included. If Fsrc has a root outside H of order e, then 1<=e<=6,
while Q has order e. The Hessian has exact order 2e-2 there: for
f=z^e u with u(0) nonzero, its first nonzero coefficient in

    Hess(Fsrc)(z,1)=7*[8 f f''-7(f')^2]

is 7e(e-8)u(0)^2, which is nonzero. This contradicts (13), including
kappa=0. A linear coordinate change covers infinity; Hessians acquire
only the nonzero factor det(g)^2 and Jacobian vanishing is invariant.

Conversely, if H=lambda L M has distinct roots and support holds,
write Fsrc=c L^a M^b with a+b=8 and a,b>=1. Direct differentiation
gives

    Hess(Fsrc)=7ab Hess(H) Q^2.

The scalar lambda cancels correctly through Q. If H is a square,
support forces Fsrc to be an eighth power and its Hessian vanishes.
Thus J(Hess(Fsrc),Q)=0 is equivalent to support in H. Finally,

    H J(A,Fsrc)-Fsrc J(A,H)=H^2 J(A,Q),

so the displayed quotient-free equation is equivalent in the binary
polynomial domain. This Hessian condition is only
for support in H; when j=0 permits an extra A4 point outside H, use
(10).

<a id="2026-10-14-generalization-quintic-logarithmic-conductor-support"></a>
<a id="2026-10-14-generalization-quintic-logarithmic-support-independent-audit"></a>

## Homogeneous logarithmic support and its exact field-valued scope

### 1. General Hamiltonian criterion

Let k be algebraically closed of characteristic zero. Let F,H be nonzero
binary forms of degrees n>=1 and h>=1. Define

    D_H = H_t partial_s - H_s partial_t.

Then the following three conditions are equivalent:

    supp(div F) contained in supp(div H);
    F divides H F_s and F divides H F_t;
    F divides D_H F.                                      (A)

Here support is projective support. In the final divisibility D_H F has
degree n+h-2; when h=1 the condition means D_H F=0.

For the middle condition, factor F=ell^m G at any linear factor ell of F,
with ell not dividing G. At least one of the two nonzero constants
ell_s,ell_t is nonzero. Differentiating in that coordinate gives exact
ell-adic order m-1, because m is nonzero in k. Each other coordinate
derivative has order at least m-1. Consequently the two divisibilities
hold at ell precisely when ell divides H. Checking all factors of F
proves the first equivalence, including their full multiplicities.

For the final condition, use s!=0 and x=t/s, writing

    F=s^n f(x), H=s^h q(x).

A direct product-rule calculation gives

    D_H F = s^(n+h-2) [n q'(x) f(x) - h q(x) f'(x)].      (B)

Suppose f has a root alpha of multiplicity m. If q(alpha)!=0, the
second summand has order exactly m-1, while the first has order at
least m. The nonzero scalar h*m prevents cancellation of that leading
term, so F cannot divide D_H F. If q has order r>=1 at alpha, both
summands have order at least m+r-1>=m, including the case in which a
summand vanishes identically. The other projective chart gives exactly
the same argument at s=0. Thus F divides D_H F precisely when every
root of F is a root of H. No squarefreeness assumption is present.

This proof needs both degree h and all relevant multiplicities m to be
nonzero scalars. Characteristic zero supplies that hypothesis. An
unrestricted positive-characteristic statement is false, for instance
when F is a p-th power. For h=1, degree alone forces the quotient to
be zero, and (A) says exactly F is a nonzero scalar multiple of H^n.

The two-derivative formulation yields unique homogeneous quotients
L_s,L_t of degree h-1 and Euler's identity

    H F_s=L_s F, H F_t=L_t F,
    s L_s+t L_t=n H.

These equations and (A) retain all root multiplicities. They express a
support condition; they do not determine conductor multiplicities or
prove descent of a section through a nonnormal surface.

### 2. Quadratic H: the eigenvector test and characteristic polynomial

For H=a s^2+b st+c t^2, D_H preserves degree n. Therefore (A) is
equivalent to

    D_H F=mu F for a scalar mu.                           (C)

For a nonzero coefficient vector f, this is equivalent to all two-by-two
minors of [f | D_H f] vanishing. Indeed, choose any nonzero coefficient
f_i; vanishing of its minors with all other rows gives
mu=(D_H f)_i/f_i and then all rows of (C). Choosing that coefficient
in the proof introduces no coefficient inversion in the global minor
equations themselves.

The induced vector field on x=t/s is -2H(1,x) partial_x. Its zero
divisor is the quadratic divisor of H, including a double zero when
H is a square. The geometric eigenvector argument also follows directly: any root outside its zero divisor gives a forbidden
order m-1 term.

The derivation acts on coordinate functions by

    D_H(s)=b s+2c t, D_H(t)=-2a s-b t.

The matrix of these values on the coordinate column (s,t)^T is

    A=[[b,2c],[-2a,-b]], A^2=(b^2-4ac) I.

With coefficient columns for the basis (s,t), the operator matrix is
A^T. This transpose convention has no effect on the characteristic
polynomial or any support conclusion, but specifying the convention
avoids confusing point-coordinate and coefficient-coordinate matrices.

Put Delta=b^2-4ac. If Delta!=0, A has eigenvalues lambda,-lambda with
lambda^2=Delta. Its induced action on degree n forms has eigenvalues
(n-2i)lambda, for 0<=i<=n. For n=8 this gives

    char(D_H;mu)
      =mu (mu^2-4Delta)(mu^2-16Delta)
           (mu^2-36Delta)(mu^2-64Delta).                  (D)

Both sides are polynomial in a,b,c, so equality on Delta!=0 proves
the polynomial identity everywhere. Alternatively, if Delta=0 and
H!=0, an invertible linear coordinate change takes H to a nonzero
multiple of s^2, for which D_H is a nonzero multiple of s partial_t.
That action is nilpotent, has characteristic polynomial mu^9, and
has kernel spanned by s^8. Thus the repeated-root locus is retained;
it permits exactly the single-root support that (A) requires.

For H=z^2+vz+w and F(z)=sum_(i=0)^8 c_i z^i, homogenize with
z=t/s. Formula (B) becomes

    8(v+2z)F(z)-2(z^2+vz+w)F'(z).

Its z^9 terms cancel, and its degree-i coefficient is exactly

    d_i=(8-2i)v c_i+(18-2i)c_(i-1)-2(i+1)w c_(i+1),
    c_(-1)=c_9=0.                                        (E)

Thus (E) gives the coefficient formula for any supplied octic
coefficient vector in this same coordinate. It does not validate the
geometric provenance of that coefficient vector.

### 3. Projective stabilizer rank test

For F!=0 of degree n>=1, consider the four coefficient columns

    F, (s partial_s-t partial_t)F, s partial_t F, t partial_s F.

Their rank is at most three if and only if some nonzero element X of
sl2 acts by X(F)=mu F. A dependence cannot use only the first column,
since F!=0. Conversely such an eigenrelation is a dependence. The last
three operators form a basis of sl2 over characteristic zero.

The projective vector field induced by a nonzero X is nonzero and is a
global section of T_(P1)=O_(P1)(2). In a finite chart it is a polynomial
of degree at most two times partial_x; its projective zero divisor has
degree two. The same root-valuation argument used in section 1 forces
every root of F to lie in this divisor. Hence F has at most two distinct
projective roots. Conversely, if the support of F has one or two
points, choose a nonzero quadratic H vanishing on these points. Section
2 gives D_H F=mu F, supplying the dependence. Therefore

    rank[F | (s partial_s-t partial_t)F |
               s partial_t F | t partial_s F]<=3
       iff F has at most two distinct projective roots.   (F)

This proof also covers n=1,2, when the rank inequality is automatic and
the root bound is automatic. No assertion about a reduced determinantal
scheme or about stabilizers in positive characteristic is needed.

### 4. Unified Jbar/A4 allowance

Let H be a nonzero quadratic, P a nonzero linear form, F a nonzero octic,
and j the actual Jbar scalar. Then the conditional support requirement

    j!=0: supp(F) contained in supp(H);
    j=0:  supp(F) contained in supp(HP)

is equivalent, on k-valued points, to existence of L_1 in Sym^1 and
mu in k satisfying

    D_(HP) F=L_1 F,
    j D_H F=mu F.                                        (G)

If j!=0, the second equation is (C) with eigenvalue mu/j. It forces
support in H, which also lies in HP; the first equation follows from
section 1. If j=0, F!=0 forces mu=0, and the first equation is exactly
the degree-three case of (A), allowing HP. This includes P equal to a
root of H, repeated H, and P at infinity. No disjoint-root hypothesis or
root-partition enumeration is required.

One can also remove the auxiliary quotient variables without choosing
roots: the first equation says that the degree-nine coefficient vector
of D_(HP)F lies in the span of the independent vectors sF,tF. Thus it is
equivalent on F!=0 to rank[sF | tF | D_(HP)F]<=2, together with
rank[F | j D_HF]<=1. These fixed-size matrix conditions retain the same
conditional support statement. They add no conductor-descent result.

All assertions above concern geometric points and a polynomial
incidence presenting them. They do not identify that incidence with a
reduced scheme, nor claim that an underlying-support condition over an
arbitrary nonreduced parameter base is equivalent to those equations.
For example, over k[epsilon]/(epsilon^2), F=s^2+epsilon t^2 and H=s^2
have the same underlying support, but D_H F=-4epsilon st is not a
scalar multiple of F. This distinction is harmless for the stated
characteristic-zero geometric-point criterion and should be preserved
in subsequent elimination or closure language.

There is a separate witness-lifting caveat for (F). Over the same ring,
let F=s^n+epsilon t^n with n>=3. Subtracting nF from the second column
of the stabilizer matrix leaves that column divisible by epsilon;
the third column is also divisible by epsilon. Thus all four-by-four
minors vanish. But D_H F=mu F for H=a s^2+b st+c t^2 forces

    mu=n b, c=0, epsilon a=0, 2n epsilon b=0.

Every coefficient of H is then in (epsilon), so no such H defines an
R-valued point of the projective quadratic space. This example forbids
extending the field-valued determinantal criterion to a witness-lifting
statement over arbitrary bases. It does not by itself show that the
determinantal ideal is nonradical.

### 5. Nonzero forms and the exact localization boundary

The abstract criteria need F,H,P nonzero. If any is zero, its divisor
or the support criterion used here is undefined or changes meaning;
matrix minors alone may then vanish for an irrelevant reason. The
original geometric zero-form stratum remains a separate obligation.

The rational finite-h2 cover also retains its original determinant
open condition, exact-gcd cofactor condition, actual projection-center
avoidance, and any other accepted geometric hypotheses. A normalized
polynomial coefficient vector obtained by clearing denominators and
removing common parameter content represents the actual conductor only
where the resulting scalar comparison is a unit and the original
conductor is nonzero. On denominator or content boundaries, a
specialized primitive extension or the closure of the rational map
cannot replace the original coefficient equations. In particular,
the original four linear cover equations are the correct data for
retaining the repeated-root determinant boundary; the homogeneous
general criterion itself excludes no such boundary.

The [initial coefficient capture](https://github.com/markluxton1/STCI/blob/9cdb518dff6ffb10e1b25d6f7651520301e42cab/research/computations/generalization_quintic_logarithmic_support_2026_10_14_attempt02.m2) uses \(p=1-x\). Applying the Hamiltonian operator directly to that vector would therefore give the wrong finite-h2 conductor incidence.
The relation \(p=1-z_{\rm target}\) uses the target normalization
coordinate, whereas the conormal cover uses \(x=r/\delta\) and hence
\(p=1/x\). The reciprocal transformation proved above repairs this
binding, including the intrinsic A4 point and all degree drops.
[Attempt05](https://github.com/markluxton1/STCI/blob/fea752a7f04c5140cdafb29efaa31732c43f1999/research/computations/generalization_quintic_logarithmic_support_2026_10_14_attempt05.m2)
checks both forward/inverse binary transformations and both Hamiltonian
images; it reuses the saved coefficients without reconstructing the octic
or inverse map. Such a coordinate repair does not extend the rational
coefficient map across denominator or content boundaries.


<a id="2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence"></a>

## Actual sextic coefficient incidence and all homogeneous charts

### 1. Captured sextic coefficient system on the accepted inverse-map open

For the nonzero sextic Q=Fsrc/H and P=S, use the exact shared support equations

    D_(HP)Q=L Q,       j D_HQ=mu Q.                  (5)

On the monic finite chart write `Q=sum_(i=0)^6 q_i x^i`, with
`q_i=0` outside `0<=i<=6`. The two Hamiltonian images in (5) have
coefficients

```
d_i=(6-2i)v q_i+(14-2i)q_(i-1)-2(i+1)w q_(i+1),  0<=i<=6,
e_i=(6-3i)v q_i+(15-3i)q_(i-1)-3(i+1)w q_(i+1),  0<=i<=7.
```

Here `d` is the degree-preserving quadratic action and `e` is the
degree-seven cubic action, because `P=S` has affine dehomogenization one.
For `L=ell0*S+ell1*T`, (5) is the single fifteen-equation system

```
e_i=ell0 q_i+ell1 q_(i-1),       0<=i<=7,
j d_i=mu q_i,                  0<=i<=6.             (7)
```

For the nonzero-j part, all two-by-two minors of the stored seven-by-two
matrix `(q,d)` express the second line after removing its scalar unknown.
The characteristic polynomial of the action on Sym^6, with eigenvalue
`nu=mu/j`, is

```
nu*(nu^2-4 Delta)*(nu^2-16 Delta)*(nu^2-36 Delta),
Delta=v^2-4w.
```

Equivalently the shared scalar variable satisfies
`mu*(mu^2-4*j^2*Delta)*(mu^2-16*j^2*Delta)*(mu^2-36*j^2*Delta)=0`.

This is one representation equation, including its nilpotent repeated-root
boundary; the spectral identity is not an assertion that the actual family
has an eigenvector at any parameter.

The [attempt06 source](https://github.com/markluxton1/STCI/blob/fea752a7f04c5140cdafb29efaa31732c43f1999/research/computations/generalization_quintic_logarithmic_support_2026_10_14_attempt06.m2)
divides the corrected G by the monic H, asserts the literal identity G=HQ,
and asserts both coefficient formulas and both product-action formulas.
It saves all seven q_i, the seven-by-two
quadratic matrix and all eight A4-cubic coefficients. This is exact
incidence data, not an emptiness certificate.

The rational coefficient map is valid only off

```
(v^2-4w)*(v^2+2w+6vw+6w^2)=0.
```

Its stored denominator and delta^4 content retain those restrictions.
The written factor proof and homogeneous system (5) do not use that inverse.

### 2. One polynomial system retains every h2 chart

To avoid every inverse denominator, take all forms in the source homogeneous
coordinates `(S,T)` and use the literal accepted octic coefficient map. Use
quadratic H, independent linear cofactors A,C, sextic Q, linear L and scalar
mu as auxiliary variables. Impose coefficientwise

```
Psource=H A,        Jsource=H C,
Gactual=H Q,
D_(SH)Q=L Q,       j D_HQ=mu Q.                     (8)
```

Require `delta!=0`, H and Q nonzero, and the determinant of A,C nonzero.
The last condition makes the homogeneous gcd exactly two. Add the original
center-avoidance and finite-birational hypotheses when interpreting this as
an actual normalization projection. No quadratic leading coefficient, H
discriminant, center pivot, or cofactor coefficient is inverted in (8).
The accepted h2 cover proves that finite monic, repeated finite and
infinity-once loci are all represented; its exceptional K locus is already
inconsistent and double infinity is already impossible.

The support part of (8) is necessary and sufficient for the actual
restricted conductor to have only the permitted roots, under the actual
h2 geometric hypotheses. It is not sufficient for full inverse support or
for power descent through the full conductor algebra. The precise remaining
task is to prove this finite incidence incompatible with the original
projection and fiber equations, or describe its surviving geometric family
and test the complete conductor logarithm. No partition of the six or eight
contact multiplicities is required to state or investigate it.

### 3. Scalar-free shared matrices and the intrinsic contact bound

The scalar unknowns in (5) may be removed without choosing a root or a
coefficient of Q. In coefficient spaces the same incidence is

```
rank[Q | j D_HQ] <= 1,               a 7-by-2 matrix,
rank[S Q | T Q | D_(SH)Q] <= 2,      an 8-by-3 matrix.       (9)
```

The first column Q is nonzero. Multiplication by S and T gives two
linearly independent columns for nonzero Q, so the second rank condition
is exactly membership in their span; it does not add a hidden leading
coefficient assumption. At j=0 the first rank condition is automatic.
Thus all two-by-two minors of the first matrix and all three-by-three
minors of the second form one homogeneous coefficient ideal.

The separately audited
[intrinsic A4 contact bound](#consolidated-historical-supplement-researchsupplementsquintic_a4_conductor_and_sextic_incidencemd)
proves that after accepted G=j=0 mate closure, every j=0 full-support
candidate has actual A4 conductor contact one or two. Therefore every
surviving h2 mate candidate, including j=0, satisfies `Res(H,Q)=0`.
On the captured finite inverse-map chart this is the single necessary
condition `N12*N18=0` from the
[bounded norm calculation](#consolidated-historical-supplement-researchsupplementsquintic_a4_conductor_and_sextic_incidencemd).
Neither factor is separately declared impossible.

This contact bound also gives one coefficient-open condition useful for
the shared matrix ideal. H has no A4 root in a surviving lane, since its
infinity leading equations would give accepted-closed G=j=0. For j
nonzero, the accepted A4 target-fiber criterion makes F(A4) nonzero, so
q6 is nonzero. For j=0, source-infinity contact one or two makes Q have
affine degree five or four. Consequently

```
(q4,q5,q6) != (0,0,0)                                    (10)
```

on every surviving finite-chart candidate. Condition (10) is a single
ideal-open locus. Saturating by a product q4*q5*q6 would be wrong: it
would remove the entire j=0 locus. A future exact shared ideal certificate
may use saturation by the ideal `(q4,q5,q6)`, together with the stipulated
delta, inverse-map determinant and exact-h2 cofactor determinant units.
The j factor in the first matrix's minors must be retained.

<a id="2026-10-14-generalization-quintic-intrinsic-a4-contact-bound"></a>
<a id="2026-10-14-generalization-quintic-intrinsic-a4-contact-independent-audit"></a>

## Intrinsic A4 contact one or two and the common-root consequence

### 1. Actual A4 fibers force the needed nonvanishing

Work on the accepted admissible finite birational nonendpoint quintic
projection family, in characteristic zero, with delta nonzero. Write
j=Jbar and let SUP mean full inverse support. The accepted A4 target
fiber criterion at j=0 states that an off-c point exists exactly when

    D0=delta^2/2+B is nonzero,       G=-2D0.

For G nonzero, put L=delta^2+2B+G=2D0+G. If L=0, then
D0=-G/2 is nonzero and the displayed criterion produces an actual
off-c point. Thus

    j=0, G nonzero, SUP implies L nonzero.              (1)

This implication respects the D0=0 exception: that exception cannot
occur when L=0 and G is nonzero. No affine/projective denominator is
discarded in the argument.

### 2. Exact contact one or two

Let F(p) be the accepted actual conductor octic, with intrinsic A4
point p=0. The new coefficient identities are

    F(0)|_(j=0)=0,
    [p]F|_(j=0)=-2G L(3delta^2+G)^2,
    [p^2]F|_(j=0,G=-3delta^2)
        =-108delta^5(delta^2-B).                        (2)

The new source reads the accepted primitive polynomial directly and
asserts precisely these identities; it reconstructs neither the
conductor determinant nor the accepted fiber theorem.

On j=0, G nonzero, SUP, equation (1) makes the factors G and L in
the first coefficient nonzero. If G+3delta^2 is nonzero, F has exact
order one at p=0. If G=-3delta^2, the first coefficient vanishes and

    L=2(B-delta^2),
    [p^2]F=54delta^5 L,                                 (3)

which is nonzero by (1). F therefore has exact order two. Since p is
a uniformizer of the smooth curve C0 at this point and c maps
isomorphically to C0, these orders are the actual conductor-contact
orders on c. Thus the new all-parameter conclusion is

    j=0, G nonzero, SUP implies ord_A4(F) in {1,2}.      (4)

The new argument does not apply (4) to G=0. For mate candidates, that
lane is removed by the separate accepted G=j=0 theorem. Only its
mate-exclusion conclusion is needed here; no new assertion about its
full-support scope is required.

### 3. The h2 resultant condition

Use the independently audited factorization Fsrc=H Q6, with H the
complete homogeneous conormal gcd of degree two, Q6 nonzero of degree
six, and source coordinates x=T/S=r/delta. The intrinsic A4 point
is S=0. The accepted leading-coefficient identities imply

    S divides H implies G=j=0.

Consequently H avoids A4 on all surviving mate candidates after the
accepted G=j=0 closure.

For j nonzero, SUP requires support(Q6) contained in support(H).
A nonzero homogeneous sextic over the algebraically closed field has
a root; hence Q6 and H have a common root and Res(H,Q6)=0.

For j=0, suppose instead that Res(H,Q6) is nonzero. This is the
homogeneous resultant, so H and Q6 have no common projective root,
including infinity and repeated-root cases. SUP permits support(Q6)
only in support(H) together with A4. Disjointness from H therefore
forces

    Q6=c S^6,       c nonzero.

Since H avoids A4, this would give ord_A4(Fsrc)=6. Equation (4)
gives a contradiction. Therefore

    every surviving actual h2 mate candidate satisfies
    Res(H,Q6)=0, for either value of j.                  (5)

This is a necessary incidence condition. It does not assert that the
quadratic and sextic have precisely one common root, that any root is
simple, or that conductor support or descent follows from the
resultant. On a rational finite inverse-map chart, a previously
captured exact factorization of this resultant may now be imposed
for j=0 as well as j nonzero, subject to that capture's denominator,
content and projection restrictions. No boundary chart is eliminated
by the proof of (5).

The accepted proofs remain premises. The deductions (1), (3)–(5) use the literal coefficient identities and
their precise geometric scope.

The [exact coefficient source](https://github.com/markluxton1/STCI/blob/d945dc39fd65f4d6133e05534af867b2eee879a1/research/computations/generalization_quintic_intrinsic_a4_contact_2026_10_14.m2)
extracts these literal first two coefficients from the accepted primitive
octic. The displayed proof uses the actual target-fiber criterion and
accepted G=j=0 mate exclusion, rather than replaying either premise.

## Captured quadratic norm: a necessary factor locus

### Quadratic-algebra norm and its finite inverse-map chart

This section concerns the finite monic inverse-map chart of the shared
coefficient capture, with its determinant, denominators, removed common
content, and nonzero conductor condition retained. This exact arithmetic capture was outside the structural proof audit;
its independent norm-computation audit was pending in the inherited source.
Preservation review of this chapter does not change that status.

In the quadratic algebra `A=k[z]/(z^2+v*z+w)`, write the remainder
of the captured sextic `Q` as `r0+r1*z`. Its norm is

    Norm_A(r0+r1*z)=r0^2-v*r0*r1+w*r1^2=Res_z(H,Q).          (13)

This determinant formula holds whether or not `H` is squarefree.
The new exact calculation finds

    gcd(r0,r1)=D,
    D=(v^2-4w)*(v^2+6vw+6w^2+2w),
    Res_z(H,Q)=D^2*N12*N18,                                 (14)

where `N12,N18` are saved explicit parameter polynomials of total
degrees twelve and eighteen. The source asserts the literal product
identity, the two factor degrees and their exponent one. The saved
factor files are sufficient to inspect the factors without listing
their long expansions here.

When `j!=0`, the required support is only `H`. Since `Q` is a nonzero
degree-six binary form, support in the finite monic `H` implies that
`H,Q` share a root. Thus on the declared `D!=0` chart,

    support(Q) subset support(H) implies N12*N18=0.           (15)

The two-factor condition is a necessary reduction, not an equivalent
support test. In particular it retains parameter families with only
one accidental shared root and does not assert that every remaining
sextic root belongs to `H`. For abstract sextics, allowing the additional A4 point when j=0
would permit Q to be supported entirely at that point. The intrinsic
contact bound proved above excludes that possibility for every surviving
actual mate candidate: Res(H,Q)=0, and hence (15), is necessary for j=0
as well on this same D!=0 inverse-map chart. This extension uses the
actual geometric contact theorem; it does not follow from the abstract
norm identity alone. The full homogeneous support equations remain the
uniform criterion on exceptional coefficient-map charts.

To determine whether an existing open condition removes either
factor, the new source also computes the actual rational h=2
cofactor map and verifies

    gcd(N12*N18, numerator(A*Dcofactor-Bcofactor*C))=1,
    gcd(N12*N18, numerator(Jbar))=1,
    gcd(N12*N18, numerator(G))=1,
    gcd(N12*N18, numerator(Delta1))=1.

Consequently these known parameter numerators do not remove either
whole factor. This does not prove existence of admissible points on
their zero loci.

The
[bounded norm source](https://github.com/markluxton1/STCI/blob/fea752a7f04c5140cdafb29efaa31732c43f1999/research/computations/generalization_quintic_h2_quotient_norm_2026_10_14.m2)
reuses only the authoritative new sextic from
`attempt-06-sextic-quotient/Q-sextic.txt`; no octic construction or
accepted verifier is replayed. It retains the literal norm factors, primitive remainder, parameter numerators and four exact gcd values; no incidence elimination is asserted.

<a id="2026-10-13-generalization-quintic-l2"></a>

## Complete regular-L2 proof and every-mate-degree consequence

### 1. Local order bound and all-mate consequence

Work over an algebraically closed field of characteristic zero in the
accepted nonendpoint sectional-genus-one quintic A4 normalization model.
Retain every actual projection-center avoidance and finite birational
projection hypothesis. Write `d=delta`, `k=kappa=aq+B`,

    Pc=q^2-6q+6, U=q(k-d)-d^2,
    D=2d(q-1)+q(q-2), E=d^2+d(3q-4)+q(q-2).

Impose the complete finite common-root incidence `Pt(q)=Jt(q)=0`, with
`G=Gs,J=Js` as in the accepted
[Taylor incidence](quintic_toric_center_incidence.md#2026-10-13-session-nonendpoint-single-root-taylor-incidence).
The actual octic conductor restriction has expansion

    F(q+t)=sum_(i=1)^8 f_i t^i,
    f1=-d q L1 L2.

The regular chart is `qZ(q)!=0`, where `Z(q)=q Pc U`. Thus `d,q,Pc,U`
are units. We do not invert the original fiber leading coefficient
`A(q)`, either diagonal quotient value, or any unmentioned projection
parameter.

**Local theorem.** On this regular chart, if `L1!=0` and `L2=0`,
then `f2,f3,f4,f5` cannot all vanish. Consequently the actual conductor
restriction has local order at most five at q. This is a statement
about the full section, rather than a bound inferred from its first
normal symbol. It is independent of mate degree and does not require
Jbar nonzero or the sole-root condition.

**All-mate consequence.** If additionally `Jbar=Js!=0` and q is
the sole common homogeneous conormal root, there is no mate of any
positive degree on the regular chart. The inherited
[quotient-fiber theorem](quintic_toric_center_incidence.md#2026-10-13-session-nonendpoint-single-root-quotient-fibers)
already excludes the regular L1 branch under full inverse support.
The remaining branch has `L1!=0,L2=0`, but full inverse support and
the sole-root/Jbar hypotheses concentrate the nonzero degree-eight
actual conductor section entirely at q. That would force local order
eight, contradicting the new local theorem.

The common-root equations by themselves do not impose homogeneous gcd
degree one. Sole-root and Jbar conditions are used only in the last
support-concentration implication. Centers on the normalization remain
inadmissible, as in the accepted model; they are not silently removed
from a claimed unrestricted parameter exhaustion.

### 2. The discriminant and the first genuine unfolding parameter

The following exact new identities explain why four-parameter Taylor
incidence becomes a two-parameter algebraic problem:

    Disc_k(L2)=12 q(q-1)d^5 [d q(q-1)-(q-2)Pc],

    partial_a f2 = -(d q/2) L1 partial_k L2  (mod L2).       (1)

The second identity is modulo the actual complete L2 equation, with
the accepted common-root substitutions already made. In particular,
on `L1!=0` and away from its discriminant, `f2=0` uniquely determines
a. No later coefficients are discarded.

At `q=1`, L2 is the nonzero value `d^5`, so the L2 branch is empty.
At `q!=1,2` the discriminant-zero family, whenever its k-leading
coefficient is nonzero, has

    d=(q-2)Pc/[q(q-1)], k=d E/D,
    L1=0,
    f2=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.                    (2)

Thus it cannot meet the new local incidence. Its possible k-leading
drop is treated separately in section 4, rather than lost in `k=dE/D`.
At q=2 the full discriminant in (1) is exactly 48d^6.
After removing the nonzero scalar factor 2d from L2, the normalized
quadratic has discriminant 12d^4. These are distinct normalizations;
both are nonzero for d!=0, so no discriminant-zero family is lost.

### 3. Complete rational cover when q!=1,2 and D!=0

Over an algebraically closed field every point on this chart has an
exact discriminant coordinate m satisfying

    m^2=3-3(q-2)Pc/[d q(q-1)],
    d=3(q-2)Pc/[q(q-1)(3-m^2)],
    k=d(E+m d^2/3)/D.                                  (3)

Conversely the chosen m for a given point is
`m=3(Dk/d-E)/d^2`, so (3) covers both quadratic roots and does not
require choosing one branch of a square root. The pointwise inverse
requires precisely d,D nonzero. Here `m^2-3!=0` because
`q(q-1)(q-2)Pc!=0`. Also

    D=(q-2)(qm-3q+6)(qm+3q-6)/[q(m^2-3)].              (4)

Thus both displayed linear factors in (4) are units on this chart.
Write the following explicit polynomial:

    H=q^4m^2+3q^4m-3q^3m^2-3q^4-15q^3m+3q^2m^2
        +36q^3+27q^2m-144q^2-18qm+216q-108.

On the cover the exact first-factor expression is

    L1=-3m(q-2)Pc^2 H/
          [q^2(q-1)(m^2-3)^2(qm+3q-6)].              (5)

Therefore `L1!=0` forces both m and H nonzero. This justifies the H
division below; H is not saturated away without explanation.
Identity (1) makes the coefficient of a in f2 nonzero. Define

    av=-[f2|_(a=0)]/[partial_a f2]

on this exact chart. Its fully expanded rational function and both
numerator/denominator inputs are saved, rather than suppressed behind
an existence claim.

After substituting `a=av`, let n3,n4,n5 be the literal polynomial
numerators of f3,f4,f5, in the rational function field QQ(q,m).
The exact normalizations are

    n3=(q-2)^5 Pc^7 H g3,
    n4=(q-2)^5 Pc^7 g4,
    n5=(q-2)^5 Pc^7 g5.                               (6)

The saved g3,g4,g5 have total degrees 22,32,32. All factors removed
in (6) are units under the stated assumptions. Thus simultaneous
vanishing of f2,f3,f4,f5 implies `g3=g4=g5=0`.

Compute the literal fixed-degree resultants in m:

    R34=Res_m(g3,g4), R35=Res_m(g3,g5).

The exact QQ gcd is

    gcd(R34,R35)=q^53(q-2)^44 Pc^69.                  (7)

A common finite root of g3,g4,g5 forces both resultants to vanish,
including any leading-degree drop of these polynomials. Formula (7)
then forces one of q,q-2,Pc to vanish, contrary to the chart. The
argument uses only this necessary resultant implication, not a claim
that every resultant root is an actual solution. The literal Bezout
witness for the original resultants is saved separately.

### 4. The k-leading drop D=0 is retained and excluded

This boundary is the leading coefficient of L2 as a polynomial in k;
it is different from a geometric Cramer denominator or the original
fiber leading coefficient A(q). Since q=1 is already impossible,
`D=0,d!=0,q!=0` gives

    d=-q(q-2)/[2(q-1)], q!=2,
    k=-q(q-2)(7q^2-12q+6)/[24(q-1)^3].               (8)

The L2 equation is genuinely linear in k on this chart: its k
coefficient is `-3q^3(q-2)^4/[4(q-1)^2]`, which is nonzero.
Consequently (1) again makes f2 affine with nonzero a coefficient
on L1!=0. More explicitly that coefficient is

    3q^6(q-2)^6 V/[128(q-1)^4],
    V=5q^4-30q^3+66q^2-72q+36.

The drop V=0 is precisely an L1=0 point here and is outside the
new local theorem. After solving f2 for a, the full f3,f4 rational
functions are saved. Their literal numerators satisfy

    gcd(numerator f3,numerator f4)=q^4.              (9)

The saved literal Bezout witness combines those original numerators
to q^4. Since q is a unit, f3 and f4 cannot both vanish. No putative
exception at V=0 or a denominator of the a-solve is silently retained
as a solution: those conditions contradict L1!=0 by (1).

### 5. The target q=2 is retained and excluded

At q=2, L2 is a nonzero scalar multiple of

    6k^2-6d(d+2)k+d^2(d^2+6d+6).

The complete quadratic-field cover is

    mu^2=3, k=d+(3+mu)d^2/6,
    L1=-mu d(d+2mu/3).                              (10)

Because the ground field is algebraically closed and characteristic
zero, the two embeddings of QQ(mu) include both roots. With d nonzero,
L1 nonzero is exactly the retained unit `d+2mu/3!=0`.

In the exact ring QQ(mu)[d,a,z], let h2,h3,h4,h5 be the actual Taylor
coefficients under (10), and let

    h6=1-z*d*(d+2mu/3).

The literal polynomial identity in the saved five-entry column is

    (h2 h3 h4 h5 h6) * C = 1.                       (11)

Its multiplication was asserted exactly before saving C. Under the
retained units h6 can be zero; therefore h2,h3,h4,h5 cannot all be
zero. The witness is over the actual quadratic number field, not a
floating-point embedding or a sample mu value.

An earlier attempted unsaturated unit assertion failed because L1=0
solutions remained. That failure was mathematically informative and
is preserved. Equation (11) applies after the inherited L1 exclusion;
it is not a claim that the unrestricted q=2 Taylor ideal is empty.

### 6. Generalization and exact remaining scope

The new bound is **uniform in mate degree** and follows from the
actual conductor section plus its polynomial deformation in a. The
Jacobian factor L2 is accompanied by a discriminant, and the next
Taylor coefficient detects its simple-root unfolding through (1).
After one coefficient solves the unfolding parameter, three more
coefficients give a finite exact cover obstruction. This avoids
separate searches for every mate exponent.

The local theorem is stronger than the single-root application, but
the order-five bound alone cannot rule out several conductor-support
points sharing total degree eight. No general conductor local-order
bound for arbitrary carriers follows from these particular formulas.
The useful broader scheme is to combine an actual conductor section,
a complete discriminant cover, a nonzero unfolding coefficient and
a literal higher-coefficient Bezout obstruction.

The unclosed incidences remain `Z(q)=0` (including Pc=0 and U=0),
the intrinsic q=0 target, target infinity, Jbar=0 where permitted
A4 contribution can occur, and additional common homogeneous
conormal roots. Other normalization genera and other carrier degrees
are outside this model. The universal projective-curve STCI question
and the unrestricted characteristic-zero C0 question remain open.

The [independently reviewed geometric bridge](quintic_toric_center_incidence.md#reviewed-geometric-bridges-for-the-regular-sole-root-branches)
retains the same complete cover and original-generator witnesses, including
the corrected discriminant normalization at q=2. The regular sole-root,
Jbar-nonzero consequence is accepted in this precise scope; no denominator,
multiroot or Jbar-zero boundary is thereby closed.

The exact sources are the [complete rational cover](https://github.com/markluxton1/STCI/blob/d49dcb591d705c2d531f9c1fc336c89072e0d346/research/computations/generalization_quintic_l2_cover.m2),
[fixed-degree resultants](https://github.com/markluxton1/STCI/blob/ca3833beb667fd2a8b13d84805a4017249834189/research/computations/generalization_quintic_l2_resultants.m2),
[original-resultant Bézout witness](https://github.com/markluxton1/STCI/blob/e3eb2b332d5f7d45f7afd735bf7e5555d050bbb8/research/computations/generalization_quintic_l2_bezout.m2),
[leading-drop witness](https://github.com/markluxton1/STCI/blob/d49dcb591d705c2d531f9c1fc336c89072e0d346/research/computations/generalization_quintic_l2_drops.m2), and
[quadratic-field boundary witness](https://github.com/markluxton1/STCI/blob/d49dcb591d705c2d531f9c1fc336c89072e0d346/research/computations/generalization_quintic_l2_boundaries.m2).
Their declared polynomial inputs and literal witnesses remain retained.
The coefficient-cover source generated the exact rational data and
numerators before entering a redundant direct saturation. That saturation
was interrupted after the separate exact resultant route completed; no
saturation result is claimed. Its coefficient outputs feed the completed
resultant and original-generator Bézout sources.

The failed unsaturated q=2 unit assertion exposed genuine L1=0 solutions;
the final witness applies after imposing the displayed L1 unit. Literal
witness identities over both embeddings of the actual quadratic field
supply the stated boundary exclusion. Software syntax/interface failures
are not additional mathematical evidence. No inherited calculation was
rerun for this consolidation.


### Archived exact certificate: `research/computations/generalization_quintic_intrinsic_a4_contact_2026_10_14.m2`

Original source retained verbatim, with original limitations and relative-path assumptions.

<details><summary>Original Macaulay2 source</summary>

```macaulay2
-- NEW intrinsic A4 contact bound: only the first two needed octic
-- coefficients are extracted from the accepted actual primitive section.
-- This is not a replay of any accepted verifier.
base=QQ[delta,a,B,G,J]; R=base[p];
inPath="research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
outDir="research/validation/2026-10-14-quintic-intrinsic-a4-contact/attempt-01";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
F=value get inPath;
F0=sub(F,{sub(J,R)=>0_R});
c0=lift(coefficient(p^0,F0),base);
c1=lift(coefficient(p^1,F0),base);
assert(c0==0_base);
assert(c1==-2*G*(delta^2+2*B+G)*(3*delta^2+G)^2);
specialF=sub(F0,{sub(G,R)=>-3*(sub(delta,R))^2});
c2special=lift(coefficient(p^2,specialF),base);
assert(c2special==-108*delta^5*(delta^2-B));
save("jzero-first-coefficient",c1);
save("jzero-Gminus3delta2-second-coefficient",c2special);
print "PASS jzero A4 value, literal first coefficient, and literal second coefficient on its only surviving first-drop locus";
print "COMPLETE new intrinsic A4 contact identities; no accepted verifier replay";
exit 0;
```
</details>



## Consolidated historical supplement: `research/supplements/SEXTIC_ADE_REDUCTION.md`

# Sextic pairs with an ADE pencil carrier

**Review, October 31, 2026: independently reviewed reduction.** Fix \(C_0=[s^4:s^3t:st^3:t^4]\) in characteristic zero.
If a proper supported sextic pair has a general normal pencil carrier
with only rational double points, its canonical filtration satisfies
\[
 \boxed{L=\mathcal O_{\mathbf P^1}(-6),\qquad D_2=0.}
\]
Its saturated triple is therefore an embedded primitive triple of type
\(\mathcal O(-6)\). This leaves a restricted case; it does not imply
that every normal pencil carrier is ADE or exclude every sextic pair.

The [all-pair sextic reduction](../supplements/SEXTIC_PAIR_REDUCTION.md) owns the normal
pencil, smoothness off the curve and saturated divisor profile. Retain
\(L=\mathcal O(-l)\), \(l\in\{5,6,7\}\), \(D_8=2T\), and
\(\deg T=4l-17\). The full first-symbol divisor of a general member
\(S\) has degree \(l+10\). Its mate cuts \(9C_0\), so local Cartier
indices divide nine. All singularities of \(S\) lie on \(C_0\).

## Marked local models and exact defects

The smooth marked rational-double-point classification in
[Jaffe, Theorem 4.1 and Propositions 5.2–5.3](https://arxiv.org/pdf/alg-geom/9410008)
lists \(A_{r-1}^{c}\), the two marked \(D\) families, \(E_{6,1}\)
and \(E_{7,1}\). The \(D\) and \(E_7\) indices are two or four,
which cannot divide nine. There is no smooth marked \(E_8\) case.
A smooth Cartier curve cannot pass through a singular hypersurface point:
quotienting an embedding-dimension-three surface ring by one equation
leaves embedding dimension at least two.

For \(A_{r-1}^{c}\), the first-symbol order is \(c\), with
\(1\le c\le r/2\), and the actual index is \(r/\gcd(r,c)\).
Use coordinates
\[
 S:(UV+t^r=0),\qquad C_0:(U,V)=(-t^{r-c},t^c).
\]
Since \(9C_0\) is Cartier, \(k=9c/r\) is an integer in
\(\{1,2,3,4\}\). The exact local divisor coefficients are
\[
 D_8=(k-1)c,\qquad T=\frac{(k-1)c}{2},\qquad
 D_2=\max\{0,3c-r\}.                                  \tag{1}
\]

For the socle formula, put \(v=V-t^c\) and let \(D\) be the axis
prime \((V,t)\). Then \(\operatorname{div}(v)=C_0+cD\) and
\(\operatorname{div}(V)=rD\). The rational function \(h=v^9/V^k\)
has divisor \(9C_0\), and is regular by normality. An actual local mate
differs from it by a unit. The reviewed
[local Jacobian/socle identity](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md) gives
\[
 c+D_8=\operatorname{ord}_t((v^9/h)|_{C_0})
      =\operatorname{ord}_t(V^k|_{C_0})=kc.
\]
For the second defect, put \(u=U+t^{r-c}\). The carrier equation is
\(uv+t^cu-t^{r-c}v=0\), and its saturated first direction is
\(m=u-t^{r-2c}v\). Generically,
\[
 m=-t^{r-3c}v^2+O(v^3).
\]
The [actual-pole identification](../supplements/SEXTIC_PAIR_REDUCTION.md#the-constant-direction-triple-and-its-actual-defects)
is local and does not require a constant global direction. It identifies
the second defect with the pole order of this quadratic coefficient,
proving (1).

The remaining non-\(A\) type \(E_{6,1}\) has first-symbol order two
and index three, with model
\[
 x^2-2xt^2-y^3=0,\qquad C_0:(x,y)=0.
\]
Here \(x\) cuts \(3C_0\), giving a primitive triple on the smooth
surface \(x=0\). Its primitive-index defect is zero. The local
power-socle formula gives \(D_8=4,T=2\), and its saturated triple has
\(D_2=0\).

The complete local numerical list is:

| Type | Parameters | First-symbol order | \(T\) | \(D_2\) | Root rank \(\rho\) |
|---|---|---:|---:|---:|---:|
| \(A\), \(k=1\) | \(r=9c\) | \(c\) | 0 | 0 | \(9c-1\) |
| \(A\), \(k=2\) | \(c=2h,r=9h\) | \(2h\) | \(h\) | 0 | \(9h-1\) |
| \(A\), \(k=3\) | \(r=3c\) | \(c\) | \(c\) | 0 | \(3c-1\) |
| \(A\), \(k=4\) | \(c=4h,r=9h\) | \(4h\) | \(6h\) | \(3h\) | \(9h-1\) |
| \(E_{6,1}\) | — | 2 | 2 | 0 | 6 |

All parameters are positive integers. The first row has no defect, hence
is locally primitive. For a general pencil member its singularities in
that locus are simple moving zeros, so \(c=1\). The inequalities below
also hold for every listed \(c\), without this refinement.

## The rank budget and the surviving row

An ADE sextic resolution has \(h^{1,1}=86\). Its negative-definite
exceptional root lattices are independent of the positive-square hyperplane
class, giving total root rank at most 85. This is also Jaffe's Lemma 11.3
specialized to degree six. No such bound is asserted here for arbitrary
normal singularities or in positive characteristic.

Every local row satisfies \(8c-\rho\le8T\). Summing over all
singularities, including moving ones, yields
\[
 \rho_{\rm total}\ge8(l+10)-8(4l-17)=216-24l.          \tag{2}
\]
For \(l=5\), this is 96, exceeding 85 and excluding the row.

For \(l=6\), a positive \(D_2\) requires a \(k=4\) point. The
budget \(\deg T=7\) permits only one, with \(h=1\). It consumes
first-symbol order four and \(T=6\), and contributes rank eight. The
other points have total first-symbol order twelve and \(T=1\), hence
rank at least 88 by the local inequality. Total rank would be at least
96, so \(D_2=0\).

For \(l=7\), the global triple obstruction requires \(D_2>0\).
The budget \(\deg T=11\) permits exactly one positive-second-defect
point, necessarily \(k=4,h=1\). Thus \(D_2=3[P]\). The reviewed
global actual-pole restrictions exclude this: axis directions have no
actual degree-three defect, and mixed directions require three distinct
points. This excludes the last row.

Only \(l=6,D_2=0\) remains. Its saturated triple has local basis
\(1,v,v^2\) with \(v^3=0\), so is primitive even at nonprimitive
points of the length-nine structure.

Independent reconstruction accepted the marked classification coverage,
actual-index restrictions, both defect formulas, the \(E_6\) contribution,
rank budget and all three row dispositions. Existing surface and triple
results were reused within their established scopes. The proof uses exact
formulas and inequalities rather than a finite search. The
\(\mathcal O(-6)\) primitive-triple case and non-ADE carriers remain open.

## Three remaining primitive-triple orbits

The surviving primitive triples have an existing complete classification.
The independently audited
[primitive-direction calculation](normal_filtration_boundary_obstructions.md#independent-audit-and-all-degree-exclusion-of-primitive-e1-quartic-triples),
subsection “Every basepoint-free primitive triple direction,” uses only
the embedded curve, \(L=\mathcal O(-6)\), \(M=\mathcal O(-8)\),
and its quadratic transition class. Its four actual ambient torus orbits
are represented by
\[
 (A,B)=(1+z,-2-8z),\qquad
 (A,B)=(rz,1),\quad (2r+1)(12r^2+4r+3)=0.
\]
Here \(A,B\) describe the conormal quotient in the source's balanced
frame. The triple in each fixed direction is unique, since
\(H^0(\operatorname{Hom}(M,L^2))=H^0(\mathcal O(-4))=0\).
The classification has no quartic-ancestor hypothesis. The source's later
degree-four carrier exclusions do not transfer automatically to sextics.

The \(r=-1/2\) orbit is excluded for sextics directly. In the actual chart
\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+V,\quad
 x_3=z^4+U+\tfrac32zV,
\]
the containing quadric is \(q=U+zV/2\). For
\((A,B)=(-z/2,1)\), the kernel direction \(BU-AV\) is exactly
\(q\). Its quadratic cocycle has the identically zero factor
\(2A+zB\), so the unique primitive correction is zero. The triple is
precisely the Cartier divisor \(3C_0\) on \(Q\).

A sextic containing it restricts to a section of
\[
 \mathcal O_Q(6,6)(-3C_0)=\mathcal O_Q(3,-3),
\]
which has no nonzero sections. Both sextics would therefore be divisible
by \(q\), contradicting properness. Only the principal orbit and the
two roots of \(12r^2+4r+3=0\) remain.

Independent reuse review checked the classification's complete curve-only
scope, the actual torus action, frame convention, unique triple, and
quadric restriction. These three orbits classify the remaining triples.
Their full degree-six equation spaces and first further contact condition
are computed below; higher extensions and sole support remain unresolved.

## Full sextic spaces and the first further contact equation

The [exact source-space computation](https://github.com/markluxton1/STCI/blob/9deae1cc7f4b008fb287d13bdb2776faa1e75bf5/research/computations/audit_sextic_triple_spaces_2026_10_31.py)
uses all ambient monomials and the accepted triple substitution
\[
 U=Ay-T_0\gamma y^2,\qquad V=By+S_0\gamma y^2,
 \qquad AS_0+BT_0=1.
\]
For the principal orbit,
\((S_0,T_0,\gamma)=(4/3,1/6,96+192z)\); for the algebraic
orbits, \((S_0,T_0,\gamma)=(0,1,0)\).
Vanishing of every coefficient of \(y^0,y^1,y^2\) is exactly
containment of the triple. Its purity makes the dense affine calculation
sufficient for a global section: no nonzero image section can be supported
only at infinity.

| Exact quantity in characteristic zero | Principal orbit | Either algebraic orbit |
| --- | ---: | ---: |
| Dimension of containing quartics | 2 | 2 |
| Dimension of containing quintics | 11 | 11 |
| Dimension of containing sextics | 27 | 27 |
| Span of quartic-source multiples by quadrics | 20 | 20 |
| Additional sextic directions modulo that span | 7 | 7 |
| Rank of the first-normal map \(h\) | 17 | 17 |
| Rank of the cubic-contact map \(\Theta\) | 18 | 12 |
| Rank of the joint map \((h,\Theta)\) | 23 | 24 |

To define the last maps, use the linear coordinates
\(U=T_0m+Ay,\ V=-S_0m+By\). The relevant terms of a containing
sextic are
\[
 F=h_Fm+\gamma h_Fy^2+E_Fmy+K_Fy^3+\cdots,
 \qquad \Theta_F=\gamma E_F-K_F.
\]
The omitted terms do not affect the cubic coefficient after eliminating
\(m\), whose order along the triple is two. With
\(q'=m+\gamma y^2\), the expansion begins
\(F=h_Fq'-\Theta_Fy^3+\cdots\). If \(h_F\ne0\) generically,
eliminating \(q'\) from \(F,G\) leaves cubic coefficient
\[
 \frac{h_G\Theta_F-h_F\Theta_G}{h_F}.
\]
Thus a generically curvilinear supported sextic pair necessarily satisfies
\[
 \boxed{h_G\Theta_F-h_F\Theta_G\equiv0.}
\]
Otherwise its generic transverse length is three, instead of nine.
At least one first-normal coefficient is nonzero in the length-nine
curvilinear setting. The next coefficients through order eight must also
vanish; those conditions and properness have not been solved here.

The script uses exact rational arithmetic and
\(\mathbb Q(\sqrt{-2})\). Conjugation transports the complete algebraic
source and contact matrices to the other root, preserving the ranks.
An independent review reconstructed the substitution, global-source
coverage and contact sign, ran the exact calculation, and added a direct
rank-and-containment check for all twenty quartic-times-quadric products.
Run `PYTHONDONTWRITEBYTECODE=1 python3 research/computations/audit_sextic_triple_spaces_2026_10_31.py`.
This completes the stated linear calculation and first necessary contact
test; it does not exclude the remaining sextic pairs.

## Necessary ADE arithmetic census for a normal quintic with direction degree one

The historical finite enumeration was **necessary-only**, not a geometric existence or exclusion proof. Its inputs are the smooth marked ADE pairs in Jaffe's classification, target quadratic defect `46/5`, total ADE rank at most `44`, and total marked order at most `12` for direction degree one (the auxiliary degree-zero option uses order at most `13`). For `A_n^k` it assigns rank `n`, marked order `k`, defect `k(n+1-k)/(n+1)`, and local index `(n+1)/gcd(n+1,k)`. For marked `D_n` vector/spin and `E_6,E_7` it uses the corresponding Jaffe table. It enumerates multisets with exact total defect `46/5`, pruning by the rank/order budgets and the upper bound `q <= nr*pr/(nr+pr)` on the remaining defect. Every surviving numerical row for direction degree one has **marked order exactly 12 and rank at least 40** (the looser degree-zero enumeration has order at least 12 and rank at least 32). The local-index lcm yields only a necessary mate divisibility `4*index/gcd(index,5)`. These numerical rows are not asserted to be realized by a normal quintic or by a global supported pair.


### Archived certificate: `research/computations/audit_sextic_triple_spaces_2026_10_31.py`

Original finite calculation preserved verbatim with its stated scope and historical relative paths.

<details><summary>Original Python source</summary>

```python
#!/usr/bin/env python3
"""Exact degree-four-to-six source spaces for the three O(-6) triples.

Standard-library only. Reuses the moving-chart/second-order substitution of
audit_mf6_e1_primitive_2026_10_07.py. Computes the coefficient-map ranks and,
in degree six, the images of h and Theta=gamma*E-K in the first contact test.
Fixed C0, characteristic zero; the algebraic directions are over Q(sqrt(-2)).
"""
from fractions import Fraction as F

# Q(a), a^2=-2; pairs are (rational part, a-coefficient).
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def q(n, d=1):
    return (F(n, d), F(0))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0] * b[0] - 2 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def inv(a):
    norm = a[0] * a[0] + 2 * a[1] * a[1]
    assert norm
    return (a[0] / norm, -a[1] / norm)


def scale(a, c):
    return {i: mul(v, c) for i, v in a.items() if mul(v, c) != ZERO}


def padd(a, b):
    out = dict(a)
    for i, v in b.items():
        w = add(out.get(i, ZERO), v)
        if w == ZERO:
            out.pop(i, None)
        else:
            out[i] = w
    return out


def pmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            k = i + j
            w = add(out.get(k, ZERO), mul(x, y))
            if w == ZERO:
                out.pop(k, None)
            else:
                out[k] = w
    return out


def yadd(a, b):
    return tuple(padd(x, y) for x, y in zip(a, b))


def ymul(a, b):
    out = ({}, {}, {})
    for i in range(3):
        for j in range(3 - i):
            row = list(out)
            row[i + j] = padd(row[i + j], pmul(a[i], b[j]))
            out = tuple(row)
    return out


def ypow(a, n):
    out = ({0: ONE}, {}, {})
    for _ in range(n):
        out = ymul(out, a)
    return out


def monomials(d):
    return [(i, j, k, d - i - j - k)
            for i in range(d, -1, -1)
            for j in range(d - i, -1, -1)
            for k in range(d - i - j, -1, -1)]


def rank_columns(cols):
    if not cols:
        return 0
    a = [[v for v in row] for row in zip(*cols)]
    nrow, ncol, pivot_row = len(a), len(cols), 0
    for c in range(ncol):
        p = next((r for r in range(pivot_row, nrow) if a[r][c] != ZERO), None)
        if p is None:
            continue
        a[pivot_row], a[p] = a[p], a[pivot_row]
        iv = inv(a[pivot_row][c])
        a[pivot_row] = [mul(x, iv) for x in a[pivot_row]]
        for r in range(nrow):
            if r != pivot_row and a[r][c] != ZERO:
                f = a[r][c]
                a[r] = [sub(x, mul(f, y)) for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == nrow:
            break
    return pivot_row


def rref_kernel(matrix, ncols):
    a = [row[:] for row in matrix]
    nrow, pivot_row, pivots = len(a), 0, []
    for c in range(ncols):
        p = next((r for r in range(pivot_row, nrow) if a[r][c] != ZERO), None)
        if p is None:
            continue
        a[pivot_row], a[p] = a[p], a[pivot_row]
        iv = inv(a[pivot_row][c])
        a[pivot_row] = [mul(x, iv) for x in a[pivot_row]]
        for r in range(nrow):
            if r != pivot_row and a[r][c] != ZERO:
                f = a[r][c]
                a[r] = [sub(x, mul(f, y)) for x, y in zip(a[r], a[pivot_row])]
        pivots.append(c)
        pivot_row += 1
        if pivot_row == nrow:
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [ZERO] * ncols
        v[f] = ONE
        for r, c in enumerate(pivots):
            v[c] = neg(a[r][f])
        basis.append(v)
    return len(pivots), basis


def orbit(name):
    z = {1: ONE}
    if name == "principal":
        A, B = {0: ONE, 1: ONE}, {0: q(-2), 1: q(-8)}
        S0, T0 = q(4, 3), q(1, 6)
        gamma = {0: q(96), 1: q(192)}
    else:
        # One root r=(-1+2*sqrt(-2))/6; the other is its conjugate.
        r = (F(-1, 6), F(1, 3))
        assert add(add(mul(q(12), mul(r, r)), mul(q(4), r)), q(3)) == ZERO
        A, B = {1: r}, {0: ONE}
        S0, T0, gamma = ZERO, ONE, {}
    x2 = ({3: ONE}, B, scale(gamma, S0))
    x3 = ({4: ONE}, padd(A, scale(pmul(z, B), q(3, 2))),
          padd(scale(gamma, neg(T0)),
               scale(pmul(z, scale(gamma, S0)), q(3, 2))))
    return A, B, S0, T0, gamma, z, x2, x3


def source_matrix(degree, data):
    _, _, _, _, _, z, x2, x3 = data
    columns = []
    for i, j, k, l in monomials(degree):
        col = ymul(ypow((z, {}, {}), j), ymul(ypow(x2, k), ypow(x3, l)))
        columns.append(col)
    keys = sorted({(n, e) for col in columns for n in range(3) for e in col[n]})
    matrix = [[col[n].get(e, ZERO) for col in columns] for n, e in keys]
    return columns, keys, matrix


def contact_map(degree, data, kernel):
    A, B, S0, T0, gamma, z, _, _ = data
    xm = scale({0: S0}, q(-1))
    xy = B
    x2 = {(0, 0): {3: ONE}, (1, 0): xm, (0, 1): xy}
    xm3 = padd({0: T0}, scale(pmul(z, {0: S0}), q(-3, 2)))
    xy3 = padd(A, scale(pmul(z, B), q(3, 2)))
    x3 = {(0, 0): {4: ONE}, (1, 0): xm3, (0, 1): xy3}

    def bmul(a, b):
        out = {}
        for (m, y), p in a.items():
            for (mm, yy), qpoly in b.items():
                if m + mm + y + yy <= 3:
                    key = (m + mm, y + yy)
                    out[key] = padd(out.get(key, {}), pmul(p, qpoly))
        return out

    def bpow(a, n):
        out = {(0, 0): {0: ONE}}
        for _ in range(n):
            out = bmul(out, a)
        return out

    hcols, ecols, kcols = [], [], []
    for i, j, k, l in monomials(degree):
        value = bmul(bmul(bpow({(0, 0): {0: ONE}}, i), bpow({(0, 0): z}, j)),
                    bmul(bpow(x2, k), bpow(x3, l)))
        hcols.append(value.get((1, 0), {}))
        ecols.append(value.get((1, 1), {}))
        kcols.append(value.get((0, 3), {}))

    h_out, theta_out = [], []
    for v in kernel:
        h = e = k = {}
        for c, col in zip(v, hcols):
            h = padd(h, scale(col, c))
        for c, col in zip(v, ecols):
            e = padd(e, scale(col, c))
        for c, col in zip(v, kcols):
            k = padd(k, scale(col, c))
        theta = padd(pmul(gamma, e), scale(k, q(-1)))
        h_out.append(h)
        theta_out.append(theta)
    h_degrees = sorted({i for p in h_out for i in p})
    t_degrees = sorted({i for p in theta_out for i in p})
    joint_degrees = sorted({("h", i) for p in h_out for i in p}
                           | {("theta", i) for p in theta_out for i in p})

    def vectors(polys, degrees):
        return [[p.get(i, ZERO) for i in degrees] for p in polys]

    h_rank = rank_columns(vectors(h_out, h_degrees))
    theta_rank = rank_columns(vectors(theta_out, t_degrees))
    joint = [[h_out[j].get(i, ZERO) if tag == "h" else theta_out[j].get(i, ZERO)
              for tag, i in joint_degrees] for j in range(len(kernel))]
    return (h_rank, theta_rank, rank_columns(joint),
            (min(h_degrees), max(h_degrees)),
            (min(t_degrees), max(t_degrees)))


def quadric_multiple_span(quartic_kernel, sextic_matrix):
    """Check the actual quartic-times-quadric subspace in sextic columns."""
    quartics, sextics = monomials(4), monomials(6)
    indexes = {mon: i for i, mon in enumerate(sextics)}
    products = []
    for vector in quartic_kernel:
        for quadric in monomials(2):
            product = [ZERO] * len(sextics)
            for coefficient, mon in zip(vector, quartics):
                dest = tuple(x + y for x, y in zip(mon, quadric))
                product[indexes[dest]] = coefficient
            products.append(product)
    for product in products:
        for row in sextic_matrix:
            total = ZERO
            for x, y in zip(row, product):
                total = add(total, mul(x, y))
            assert total == ZERO
    rank = rank_columns(products)
    assert rank == 20
    return rank


def report(name):
    data = orbit(name)
    quartic_kernel = None
    for degree in (4, 5, 6):
        columns, keys, matrix = source_matrix(degree, data)
        rank, kernel = rref_kernel(matrix, len(columns))
        print(f"{name} d={degree}: rows={len(keys)}, rank={rank}, dim={len(kernel)}")
        if degree == 4:
            quartic_kernel = kernel
        if degree == 6:
            product_rank = quadric_multiple_span(quartic_kernel, matrix)
            print(f"  quartic-times-quadric span={product_rank}; "
                  f"additional sextic directions={len(kernel)-product_rank}")
            h_rank, theta_rank, joint_rank, hrange, trange = contact_map(degree, data, kernel)
            print(f"  h: deg={hrange}, rank={h_rank}; Theta: deg={trange}, rank={theta_rank}; "
                  f"joint rank={joint_rank}, joint kernel={len(kernel)-joint_rank}")


if __name__ == "__main__":
    report("principal")
    report("algebraic")
```
</details>
