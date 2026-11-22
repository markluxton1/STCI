# Numerical pullback and the normal line

This note separates a reusable surface inequality from the numerical assumptions
of any particular carrier. Work over an algebraically closed field of
characteristic zero. The lemma below concerns an **integral projective surface**
\(S\) and a smooth integral curve \(C\subset S\), with \(S\) regular
at the generic point of \(C\). Neither normality of \(S\) nor Cartierness
of \(C\) is required. Its application to a hypothetical STCI requires the actual
carrier and its normal line, not only an abstract singularity model.

## The pullback defect

Write \(I=I_{C/S}\), let
\(L=(I/I^2)/\operatorname{torsion}\), and set \(N=L^\vee\). Since \(C\)
is smooth and \(S\) is regular at the generic point of \(C\), \(L\) is a line bundle.
Let \(S^\nu\to S\) be the finite normalization. Choose a smooth
projective resolution \(\pi:T\to S\) factoring through both \(S^\nu\)
and the blowup of \(I\), with smooth strict transform \(\widetilde C\). Then
\(\widetilde C\to C\) is an isomorphism and
\[
I\mathcal O_T=\mathcal O_T(-D),\qquad D=\widetilde C+Z,
\]
where \(Z\) is effective and exceptional for \(T\to S^\nu\). There is
only one curve \(C^\nu\) above \(C\) dominating it, by generic regularity.
The finite birational map \(C^\nu\to C\) is an isomorphism since \(C\) is
normal. Define its numerical pullback
\(C^\#=\widetilde C+R\) by \(C^\#\cdot E_i=0\) for every exceptional
curve. Then
\[
\boxed{\deg N-(C^\#)^2=(Z-R)\cdot\widetilde C\ge0.}
\]

**Proof.** The rational lift \(C\dashrightarrow T\) extends at every
point by properness and the DVR valuative criterion. It is a section over
\(C\), hence a closed immersion with image \(\widetilde C\). This
identifies \(\widetilde C\) with \(C\). Any nonexceptional divisor in
the support of \(I\mathcal O_T\) would map finitely onto \(C\) from
\(S^\nu\); generic regularity makes \(C^\nu\) its only possibility,
with coefficient one. Thus \(D=\widetilde C+Z\) as asserted. The surjection
\(\pi^*I\twoheadrightarrow\mathcal O_T(-D)\), restricted to
\(\widetilde C\), kills \(I^2\): multiplication by the local equation of
\(D\) vanishes on \(\widetilde C\). It therefore induces a surjection
\(I/I^2\twoheadrightarrow\mathcal O_T(-D)|_{\widetilde C}\). Torsion
maps to zero in a line bundle, so the induced surjection of line bundles is
an isomorphism. Consequently \(\deg N=D\cdot\widetilde C\).

Let \(M=(E_i\cdot E_j)\), \(c_i=\widetilde C\cdot E_i\), and write
\(Z=\sum z_iE_i\), \(R=\sum r_iE_i\). For \(T\to S^\nu\), the matrix \(M\) is negative
definite with nonnegative off-diagonal entries. Relative generation of
\(\mathcal O_T(-D)\) gives \(D\cdot E_i\le0\), hence
\[
c+Mz\le0,\qquad c+Mr=0.
\]
The inverse of \(-M\) is entrywise nonnegative. To see the sign without a
matrix classification, if \(Ax=b\ge0\) for a positive-definite symmetric
matrix \(A\) with nonpositive off-diagonal entries, write
\(x=x_+-x_-\) with disjoint nonnegative supports. If \(x_-\ne0\),
\(x_-^TAx=x_-^TAx_+-x_-^TAx_-<0\), contradicting \(x_-^Tb\ge0\).
Apply this to \(A=-M\) and \(-M(z-r)\ge0\); then \(z-r\ge0\).
Finally, orthogonality to \(R\) gives
\((C^\#)^2=\widetilde C^2+R\cdot\widetilde C\), proving the formula
and sign. \(\square\)

The exceptional intersection input is the classical negative-definiteness
argument in [Mumford, *The topology of normal singularities of an algebraic
surface* (1961), §1, p.6](https://www.numdam.org/item/PMIHES_1961__9__5_0.pdf).
The displayed normal-line identification and defect formula are proved above;
they are not attributed to an unchecked literature statement. Resolving and
principalizing the curve ideal is essential to that identification.

**Characteristic boundary.** Once a smooth principalizing model with the stated
exceptional intersection properties is supplied, the displayed defect identity
and its sign use no characteristic-zero argument. They therefore hold over an
algebraically closed field of any characteristic under those same model
hypotheses. This observation does not transfer a characteristic-zero surface
classification, a bound on exceptional configurations, or a particular
application's normal-bundle calculation to positive characteristic.

## What the defect measures

The integral divisor \(D\) records the actual vanishing of the curve ideal
on a resolution. The rational divisor \(C^\#\) records numerical
orthogonality. Their difference measures exceptional vanishing that cannot be
seen from the numerical pullback alone. At an ordinary double point where
\(\widetilde C\) meets the exceptional \((-2)\)-curve once, \(r=1/2\).
On the blowup principalizing the smooth branch ideal, \(z=1\); the contribution
to the displayed defect is \(1/2\).

A carrier application must still compute \(\deg N\), \((C^\#)^2\), and
the actual exceptional contacts. This lemma alone neither excludes a carrier
nor supplies a value such as \(13/5\) for its pullback square. If the
surface is singular at the generic point of \(C\), the rank-one conormal
and coefficient-one arguments fail; that case is outside this lemma.

## Cartier index does not bound the numerical correction

On the normal surface singularity \(uv=w^{2m}\), take the smooth branch
\(C: u=v=w^m\). Its strict transform meets the middle curve of the
\(A_{2m-1}\) resolution chain transversally. For the negative chain matrix,
\[
-(M^{-1})_{ij}=\frac{\min(i,j)(2m-\max(i,j))}{2m}.
\]
Thus the middle correction is \(-(M^{-1})_{mm}=m/2\). The local divisor
class of the branch has order two: in the cyclic discriminant group of the
chain it is the class \(m\in\mathbb Z/(2m)\), and the function
\(u+v-2w^m\) has divisor \(2C\). Its numerical pullback has coefficient \(1/2\) at
the first exceptional curve, so the branch is not Cartier. In the middle
resolution chart \(u=w^m x,v=w^m/x\), its strict transform is \(x=1\),
transverse to the central exceptional curve \(w=0\). In particular the Cartier index remains
two while the correction is unbounded.

This concrete family rules out an estimate of the correction using only the
local Cartier index, such as \(-(M^{-1})_{jj}\le r/4\). It does not contradict
a theorem with additional geometric or direction hypotheses. Any bounded-index
carrier argument must keep those hypotheses visible and cannot substitute
index for the full resolution data.

## Limits of numerical and generic input

The correction matrix, discrepancy divisor and actual normal derivatives are
different inputs. In particular, the inequality for the conormal line
is conditional on principalization of the actual curve ideal, not on
an arbitrary numerical pullback chosen without that ideal. For arbitrary normal surface singularities, one cannot assume
the discrepancy contribution has the sign available in a crepant ADE
calculation. Nor does the Cartier index alone establish a lower bound
\(\operatorname{ord}_p(\nabla F|_C)\ge r_p-1\). A proof using either step
must establish its singularity and marked-curve hypotheses independently; the
index-two family above already rules out replacing the correction matrix by
an index-only estimate.

On a nonnormal carrier, an intersection number with the conductor counts
scheme-theoretic multiplicity, not distinct normalization points. Two plane
curves \(y=0\) and \(y=x^N\) already have one intersection point of length
\(N\). Likewise, a nonzero transverse differential does not by itself produce
a second distinct normalization sheet. The [full conductor and inverse-support
criterion](../../frameworks/carrier-normalization/carrier_descent.md#42-the-full-conductor-descent-criterion) requires the actual finite
algebra and full inverse fiber, including nonreduced structure.

Generic curvilinearity supplies no automatic compatible primitive stage on the
whole support. In characteristic zero, the [explicit supported complete-intersection
control](../arithmetic/arithmetic_root_collision.md#counterexample-c--generic-primitivity-does-not-globalize)
has equations \((x^2,y^2+tx)\) on a line-supported projective
complete intersection. It has generic length four but a special algebra
\(k[x,y]/(x^2,y^2)\) with no curvilinear length-three quotient. It therefore
prevents a generic normal model from being substituted
for an everywhere compatible primitive triple. A reduction from arbitrary
entirely thick pairs to movement-two root lifts needs its own theorem; none
follows from these numerical identities.

## Branch valuations and the actual first blowup

**Status: new synthesis of the normalization and graph-cycle proofs,
pending independent mathematical review.** It applies to actual
integral carriers, including those singular at the generic point of the
marked curve. It does not identify the Rees valuations of the full CI
ideal with the branches of a chosen carrier.

Let \(X=V(F_a)\) be an integral hypersurface containing a smooth integral
curve \(C\) of degree \(d\) and genus \(g\) in \(\mathbf P^3\).
Write \(p=\operatorname{ord}_C F>0\), and let \(G_b\) be a proper mate
candidate of normal order \(q\), so the actual intersection cycle is
\(m[C]+R\). Denote by \(X'\) the strict transform on
\(B=\operatorname{Bl}_C\mathbf P^3\), with exceptional divisor \(E\),
and by \(S\to X\) the finite normalization. Take a smooth projective
resolution \(T\) dominating \(S\) and \(X'\), so
\[
 I_C\mathcal O_T=\mathcal O_T(-D),\qquad D=E|_T .
\]
Such a model follows by principalizing the actual marked ideal on a
resolution of \(S\), using the universal property of blowing up
([Stacks, Lemma 31.33.5](https://stacks.math.columbia.edu/tag/0806)).
The intersection arguments below work wherever the indicated smooth
principalizing model is available. The balanced formulas specialize
to the characteristic-zero fixed quartic.

Write \(\Gamma_i\) for the divisorial inverse branches on \(S\), and
write \(\widetilde\Gamma_i\) for their strict transforms on \(T\).
Let \(M_i\) be their Mumford numerical pullbacks, and
\[
 f_i=[k(\Gamma_i):k(C)],\quad
 e_i=v_{\Gamma_i}(I_C),\quad n_i=v_{\Gamma_i}(G),\qquad
 p=\sum_i e_i f_i,\quad m=\sum_i n_i f_i.
\]
The last two equalities are the normalization length formulas in
[normalization capacity](normalization_residual_capacity.md#4-several-inverse-curves-give-a-finite-collection-of-linear-constraints);
the degrees include inseparable parts. Let \(E_j\) denote the exceptional
curves of \(T\to S\), and write
\[
 D=\sum_i e_i\widetilde\Gamma_i+\sum_j z_j E_j,\quad
 D^{\rm num}=\sum_i e_iM_i,\quad V=D-D^{\rm num}.
\]
Then \(V\) is exceptional and effective. Indeed \(D\cdot E_j\le0\)
by relative global generation, \(D^{\rm num}\cdot E_j=0\), and the
inverse-matrix positivity proof above works for the entire vector of
branches, with their multiplicities. No individual branch is assumed
Cartier, smooth, or of residue degree one.

### The precise cycle dictionary

The intersection of the two strict surfaces on \(B\), denoted \(W\),
is the pushforward from \(T\) of the effective Cartier divisor
\[
 \operatorname{div}_T(G)-qD.                              \tag{N1}
\]
Indeed the latter is the restriction of the divided strict mate to
the resolution of the strict carrier. Its pushforward is the
Cartier-divisor intersection by the projection formula (Fulton,
*Intersection Theory*, Proposition 2.3(c)). Properness of the
original pair ensures the restricted section is nonzero. The
coefficient of \(W\) on a horizontal curve \(Z\subset E\) is therefore
\[
 \boxed{\quad \sum_{\widetilde\Gamma_i\mapsto Z}
       (n_i-qe_i)[k(\Gamma_i):k(Z)] .\quad}                \tag{N2}
\]
In particular \(n_i\ge q e_i\), and the total horizontal degree over
\(C\) is \(m-pq\). The analogous vertical coefficient over a closed
point is the sum of
\((g_j-qz_j)[k(E_j):k(E_P)]\) over curves mapping onto the exceptional
fiber \(E_P\), where \(g_j=v_{E_j}(G)\) and the field degree is that
of the map of curves. Curves contracted to points contribute zero
to this pushforward. For sole support the normalized mate divisor
is Cartier with Weil divisor \(\sum_i n_i\Gamma_i\); if
\(M_i=\widetilde\Gamma_i+\sum_j r_{ij}E_j\), its Cartier pullback
gives \(g_j=\sum_i n_i r_{ij}\). Thus the actual order \(q\) requires
the componentwise inequalities
\[
 n_i\ge qe_i,\qquad \sum_i n_i r_{ij}\ge qz_j.             \tag{N3}
\]
These inequalities relate the actual normalized branch vector to
both horizontal and vertical coefficients of the strict intersection,
rather than equating those two unrelated valuation lists. They also
apply to the respective directions of the two carriers separately.
For arbitrary residual support (N1)--(N2) still hold; \(g_j\) must
then include the contributions of the normalized residual, rather
than only the marked branch vector.

The converse to (N3) is **not** asserted: valuation inequalities on
a principalizing model test integral closure of powers of the
marked ideal on the carrier, not membership of an actual ambient
form in \(I_C^q(b)\). Global degree-bounded source images and
conductor section descent still matter. In particular this
dictionary is not a classification of full-ideal Rees valuations
or of higher infinitely-near jets.

### Exact decomposition of the first-graph gap

Put \(H=\mathcal O_T(1)\), the pullback from projective space, and
\(\lambda=\deg N_{C/\mathbf P^3}=4d+2g-2\).
The ambient graph gives
\[
 H^2=a,\quad H D=dp,\quad D^2=p\lambda-ad.
\]
For the last identity, intersect \(E^2\) with the strict carrier
\(aH-pE\) in the threefold; \(H E^2=-d\), \(E^3=-\lambda\).
The intersections upstairs agree by projection formula.
Let
\[
 Q_{ij}=M_iM_j-d^2 f_i f_j/a,\qquad
 \kappa=d^2p^2/a+ad-p\lambda.
\]
By Hodge index \(Q\) is negative semidefinite; it is the
arrangement Hodge matrix on the normalization, now for all inverse
branches of a thick carrier. Orthogonality of \(D^{\rm num}\) to
exceptional curves gives the exact decomposition
\[
 \boxed{\quad
   \kappa=-\mathbf e^{\,t}Q\mathbf e-V^2 .
 \quad}                                                  \tag{N4}
\]
Both terms on the right are nonnegative. Thus the ambient
self-intersection gap consists of a **normalized branch imbalance**
and an **exceptional principalization gap**. If an actual sole-support
mate exists, its positive valuation vector is in \(\ker Q\).
In particular, if \(\mathbf n\) is proportional to \(\mathbf e\)
(as it necessarily is for a singleton inverse), then
\[
 \boxed{-V^2=\kappa.}                                     \tag{N5}
\]
This quantifies precisely the singular or vertical geometry
required in that case. It does not bound each singularity by its
Cartier index.

For the fixed balanced quartic, \(d=4,\lambda=14\), so
\[
 \kappa=16p^2/a+4a-14p>0
\]
for any positive \(a,p\), by AM--GM, and \(\kappa\ge10p/3\)
when \(a\ge3p\). Consequently **without vertical first-normal
fibers, every singleton inverse is excluded, regardless of
its residue degree or its Cartier status**. To justify this
statement, absence of vertical fibers of \(X'\to X\) makes this
proper birational map quasi-finite, hence finite. The normalization
then factors through \(X'\), so the pullback of \(E|_{X'}\) to \(S\)
is Cartier, with divisor \(\sum_i e_i\Gamma_i\). Its numerical
pullback is \(D\), so \(V=0\). More directly, exceptional curves on
\(T\to S\) all have \(D\)-degree zero precisely when none maps onto
an exceptional fiber of \(X'\to X\). Negative definiteness then
implies \(V=0\). This is a fixed-carrier all-mate exclusion. It also
excludes the proportional valuation vector on any multibranch
carrier with no vertical fibers.

### Root slopes recover the branch matrix

Now specialize to \(C_0\) in characteristic zero, so
\(E=C_0\times\mathbf P^1\) and
\(\mathcal O_E(E)=\mathcal O_E(7,-1)\).
Let \(h_i\) be the direction-degree of \(\widetilde\Gamma_i\)
under its map into \(E\) (the degree of the pullback of
\(\mathcal O_{\mathbf P^1}(1)\) from the direction factor).
Let \(h_j^{\rm exc}=-D\cdot E_j\ge0\); over a point of \(C\)
this is the degree of its map onto the direction fiber, zero
if contracted. For curves over other points it is zero.
Write \(\epsilon_i=V\cdot\widetilde\Gamma_i\ge0\). The restriction
of \(D=E|_T\) gives
\[
 D\cdot\widetilde\Gamma_i=7f_i-h_i,\qquad
 D^{\rm num}\cdot M_i=7f_i-h_i-\epsilon_i.
\]
The first-normal divisor of the carrier on \(E\) has bidegree
\((4a-7p,p)\). Its full vertical coefficient sum
\(v_F=\sum_j z_jh_j^{\rm exc}\) therefore also satisfies
\[
 \sum_i e_i h_i+v_F=4a-7p.                                \tag{N6}
\]
When a mate exists, intersect its normalized Cartier pullback
with \(D\):
\[
 \sum_i n_i(h_i+\epsilon_i)=7m-4bp,\qquad m=ab/4.         \tag{N7}
\]
The left side agrees with \(\sum_i n_i h_i+\sum_jg_jh_j^{\rm exc}\)
by orthogonality and the exceptional intersection matrix. The
direction-degree of the actual exceptional strict intersection is
thus exactly
\[
 u=\sum_i(n_i-qe_i)h_i+\sum_j(g_j-qz_j)h_j^{\rm exc}.
\]
Combining (N6)--(N7) recovers the first-graph slack equality with
\(R=0\); it is not an independent scalar obstruction. Formula
(N2), however, retains the branchwise coefficients that the scalar
equality discards.

In particular the positive weights \(n_i f_i\) force the
mate-independent slope bound
\[
 \min_i h_i/f_i\ \le\ 7-16p/a.                              \tag{N8}
\]
If all the branches map to the same horizontal root curve on \(E\),
their direction slopes coincide, say \(\rho\), even when their
degrees over that curve differ. Equations (N6)--(N8) give
\[
 \boxed{v_F\ge4a-14p+16p^2/a=\kappa.}                     \tag{N9}
\]
In particular, one horizontal root and no vertical first-symbol
content are incompatible with a mate, for **every** carrier
degree and normal order. A repeated single section of a thick
sextic (\(a=6,p=2\)) must have horizontal degree \(h_i/f_i\le1\),
hence vertical content at least eight; a single irreducible
quadratic multisection must have direction bidegree at most
three, hence vertical content at least seven. This last sentence
uses the integer bidegrees of these two possible horizontal
divisors, not a classification of sextic carriers. Neither bound
asserts such a vertical stratum is realizable.

A further exact matrix refinement is available whenever
\[
 \kappa_{\rm br}=16p^2/a-(D^{\rm num})^2>0.
\]
Put \(\rho_*=7-16p/a\) and
\(w_i=f_i\rho_*-h_i-\epsilon_i\). In \(H^\perp\), the vector
\(D^{\rm num}-(4p/a)H\) has square \(-\kappa_{\rm br}\)
and pairs with \(M_i-(4f_i/a)H\) by \(w_i\).
Orthogonally projecting onto this vector yields
\[
 \boxed{Q+\frac{ww^t}{\kappa_{\rm br}}\ \preceq\ 0.}       \tag{N10}
\]
This is an inequality of symmetric forms, not entrywise.
If there are exactly two inverse branches and a positive mate
vector, they span modulo \(H\) at most one line; the nonzero
vector of square \(-\kappa_{\rm br}\) spans that line. Therefore
equality holds in (N10):
\[
 M_iM_j=16 f_i f_j/a-w_iw_j/\kappa_{\rm br}.               \tag{N11}
\]
Also \(\sum_i n_iw_i=0\), and the two \(w_i\)'s have opposite
signs, since positive mate coefficients and nonzero
\(\kappa_{\rm br}\) exclude either both zero or a single nonzero
entry. This determines the ratio of all possible mate
valuations on that fixed carrier. In the no-vertical case
\(\epsilon_i=0,\kappa_{\rm br}=\kappa\); then these are
explicit functions of degree, normal order, residue degrees
and root slopes. For more than two branches a new orthogonal
component may remain. If \(\kappa_{\rm br}=0\), the projected
vector is numerically zero and all \(w_i=0\); do not divide by
zero or infer a unique mate ray.

**Recovering the split-sextic calculation.** For \(a=6,p=2\),
two content-free sections of slopes \(d_1,10-d_1\), and
\(e_i=f_i=1\), one has \(\rho_*=5/3,\kappa=20/3\).
Their slopes must straddle \(5/3\), so \(d_1=0\) or \(1\)
after exchange. Formula (N11) gives respectively
\[
 (\Gamma_1^2,\Gamma_1\Gamma_2,\Gamma_2^2)
 =(9/4,19/4,-31/4),\quad(13/5,17/5,-27/5).
\]
The off-diagonal values reproduce the existing P-020
fractionality obstruction. Thus the two-lift numerical matrix
is not a peculiarity of sextics: it is determined by projection
onto one explicitly known direction in the Hodge space.
This calculation only excludes Cartier branches as in P-020;
the non-Cartier correction, conductor gluing and actual
equations remain essential in the surviving cases.

### Relation to the generically regular socle theorem

When \(p=1\), there is one inverse branch of degree one and
\(D\cdot\widetilde C=\ell\), the dual free first conormal degree
in the original numerical pullback lemma. Thus
\(\epsilon_1=\ell-C^2\), the degree of the intrinsic defect
divisor in the
[actual almost-Cartier power–socle theorem](normal_index_socle_and_torsion.md#intrinsic-divisor-on-a-possibly-nonnormal-generically-regular-carrier)
when its downstairs index is finite. For a mate, (N5) gives
\(-V^2=4a-14+16/a\), the same scalar budget that crepant
adjunction measures by exceptional pullback correction on an
ADE carrier. The cycle \(V\) here is the difference between
the principalized ideal and its numerical pullback, **not**
the exceptional part of the numerical pullback of the
strict curve. The equality of their global energies in the
crepant mate setting is not an identification of those
cycles or of their local defects.

The same two mechanisms now have one mathematical source:
intersection of the original marked ideal with the normalized
divisor lattice. Generalizing beyond the first graph would
require actual successive principalizations and contact data;
nothing in (N1)--(N11) gives a uniform higher-depth bound.

## Conditional split-sextic application

Use the hypotheses and notation of
`research/notes/2026-10-05-split-sextic.md`: the low branch is a smooth
section, the strict sextic is an integral surface regular generically along
that branch, and both selected ramified-root endpoints are ordinary nodes.
Let `delta` be the zero-divisor length of the nonzero Jacobian map

\[
 N_{\Gamma/B}\longrightarrow O_\Gamma(D)=O_{\mathbf P^1}(12).
\]

From `deg N_{Gamma/B}=2+6=8`, its saturated kernel is

\[
 N_{\Gamma/D}=O_{\mathbf P^1}(\delta-4).
\]

This degree computation uses the normal extension only through its
determinant; it does not split that extension.

P-020/P-023 force `Gamma#^2=13/5` for a mate-compatible type `d=1`.
The general inequality alone would imply `delta>=7`. The two endpoint
contributions in (4) improve it to

\[
 \delta-4-13/5\geq1,
 \qquad\boxed{\delta\geq8.}
\]

Each ordinary endpoint has Jacobian common order one. Thus the interior
Jacobian common divisor must have length at least six. In the finite
chart, away from the endpoints and after the stated trivializations, this
means

\[
 \deg\gcd(R,g)\geq6,
\]

provided `R` and `g` are the exact two Jacobian components there (as in the
split-sextic note). Since `R(0)=a_h u_0 != 0` and `g=zG` with
`deg G <= 6`, **if `G` is nonzero**, this further forces

\[
 \boxed{\deg G=6,\qquad G\mid R.}
\]

The identically-zero case is a separate stratum: the coefficient of
`z^6` in `G` can vanish even though the high factor is content-free. In
that case `gcd(R,0)=R`, so the degree-six argument does not apply. It is
handled separately in `2026-10-06-split22-finite-reduction.md`.

This is a conditional necessary restriction, not an STCI exclusion. The
reviewed lemma supplies the normal-sheaf inequality, while the asserted
13/5 pullback square, exact Jacobian components and actual-carrier hypotheses
remain separate antecedents; they were not independently recertified here.
