# General intersections through the quartic: residual curves and a flexible attachment map

Date: 2026-10-27. Author: global-intersections research agent. Status:
**provisional research contribution; independently reviewed** in the
[separate audit](2026-10-27-global-containing-intersections-audit.md). The new
all-degree attachment-map deduction is separated below from standard liaison
and from the previously studied quartic examples. No canonical result changes.

Throughout, \(k\) is algebraically closed of characteristic zero and

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\quad F_4=x_1^4-x_0^3x_3,
\quad G_4=x_2^4-x_0x_3^3.
\]

The question is to understand **all proper intersections containing the fixed
embedded curve**, then use their geometry to guide constructions. The
sole-support case is a special endpoint; none of the conclusions below
excludes it in unrestricted degrees.

## 1. Inputs, repo check, and what is actually new here

Retrieval followed [INDEX](../INDEX.md), [MAP](../MAP.md), and the
[contribution protocol](../CONTRIBUTING_AGENT.md), then these exact inputs:

* [R-0020](../results/quartic_conormal_characteristic_jump.md): the fixed
  characteristic-zero conormal is \(\mathcal O_{\mathbf P^1}(-7)^2\).
* [R-0021](../results/quartic_mu4_degeneration.md): the displayed quartic pair
  is proper and its characteristic-zero support is the specified four quartics.
* [R-0023](../results/ci_quartic_explicit_residual_geometry.md): specific actual
  quartic pairs have the smooth residual and line degeneration stated there.
  This record is **not** a theorem about every general pair.
* The [October 25 deformation laboratory](2026-10-25-ci-cycle-deformation-laboratory.md),
  Sections 2–3, and its [independent audit](2026-10-25-ci-cycle-exploration-audit.md),
  Sections 1–2: the ideal is generated in degrees at most three, \(4H-E\)
  is very ample on the blowup, and the two quartic determinant differential
  images are \(\langle u^8,\ldots,u^{18}\rangle\) and
  \(\langle1,u,\ldots,u^{10}\rangle\). These are **reviewed provisional
  evidence**, not a separate promoted result record. The new all-degree proof
  below uses these explicit, independently audited image computations as
  premises; their inherited verifier was not rerun.
* The [October 25 conductor note](2026-10-25-ci-cycle-conductor-topology.md),
  Section 2, already gives the general reduced multiplicity-one boundary
  degree \(4a+4b-14\). That formula is not new here.

A targeted repository search for attachment-map dominance in all degrees did
not locate an existing statement. The extension in Section 3 is new **to this
research pass**; no claim of literature novelty is made. The genus and Rao
calculations are applications of classical linkage. The point of combining
them is a larger, construction-oriented parameter space in degrees at least
five, where residual geometry is a variable to investigate.

## 2. The general picture in every bidegree \(a,b\ge4\)

Put \(V_d=H^0(I_C(d))\). The curve has type \((1,3)\) on its smooth containing
quadric. The sequence

\[
0\longrightarrow\mathcal O_{\mathbf P^3}(d-2)
\longrightarrow I_C(d)
\longrightarrow\mathcal O_{\mathbf P^1\times\mathbf P^1}(d-1,d-3)
\longrightarrow0
\]

and Künneth give \(H^1(I_C(d))=0\) for \(d\ge2\). Consequently

\[
v_d:=\dim V_d=\binom{d+3}{3}-(4d+1)\qquad(d\ge2).
\]

For equal degrees the basis-free pair space is the open subset of

\[
\operatorname{Gr}(2,V_d)
\]

consisting of pencils without a common surface component. Its dimension is

\[
2(v_d-2)=2\binom{d+3}{3}-8d-6.
\]

For mixed degrees one may use the open set of proper ordered pairs in

\[
\mathbf P(V_a)\times\mathbf P(V_b),
\]

remembering that when \(a<b\), replacing \(G_b\) by \(G_b+H_{b-a}F_a\)
preserves the intersection. We do not interpret this redundant product as
the moduli space of distinct schemes.

**General-pair deduction.** For every \(a,b\ge4\), a general proper pair gives

\[
Y=C\cup D
\]

as a reduced scheme union, where \(D\) is smooth and geometrically integral,
with

\[
\boxed{\deg D=ab-4,\quad
g(D)=\frac{(a+b-4)(ab-8)}2,\quad
\operatorname{length}(C\cap D)=4(a+b)-14.}\tag{1}
\]

The attachments are distinct transverse points for a general pair.
This extends the general quartic picture using the same standard geometry;
it makes no assertion about all special pairs or fixed-boundary fibers.

Here are the hypotheses and proof. On the smooth blowup

\[
B=\operatorname{Bl}_C\mathbf P^3,
\quad H=\pi^*\mathcal O_{\mathbf P^3}(1),
\quad E=\pi^{-1}(C),
\]

the graph embedding from \(I_C(3)\), already checked in the cited note, makes

\[
L_d=dH-E=(4H-E)+(d-4)H
\]

very ample for \(d\ge4\): tensor a very ample line bundle with a globally
generated one, or use the same graph embedding with the Segre-Veronese
polarization \(\mathcal O(d-3,1)\). General divisors in \(L_a,L_b\) therefore
intersect in a smooth geometrically integral curve upstairs. This is the
usual [Bertini smoothness theorem](https://stacks.math.columbia.edu/tag/0FD4)
and [Bertini irreducibility theorem](https://stacks.math.columbia.edu/tag/0G4C).
The [Rees construction](https://stacks.math.columbia.edu/tag/01OF) identifies
these sections with actual global forms containing \(C\).

Section 3 proves that general first-normal determinant zeros are simple.
At any such zero, the first-normal matrix has rank one. Choose a generator
which is smooth there and make its local equation a coordinate \(x=0\).
The other equation on this smooth surface is \(y h(u,y)=0\), with

\[
C=(x,y),\qquad h(u,0)\text{ having a simple zero at }u=0.
\]

The residual \(h=0\) is smooth and meets \(y=0\) transversely. This proves the
needed blowdown assertion, including smoothness at the attachments; smoothness
upstairs alone would not justify it.

The numbers in (1) may be reconstructed on a general smooth degree-\(a\)
surface \(S\supset C\). Such an \(S\) exists: \(I_C(a)\) generates the
conormal fibers, so a general section has no normal zero along the
one-dimensional base \(C\), and Bertini applies away from \(C\). Adjunction gives

\[
K_S=(a-4)H,\quad C^2=14-4a,\quad D\sim bH-C.
\]

Thus \(H\cdot D=ab-4\), \(C\cdot D=4(a+b)-14\), and

\[
2g(D)-2=(bH-C)\cdot((a+b-4)H-C)
=(a+b-4)(ab-8)-2.
\]

These are classical adjunction/liaison calculations; they are not new
restrictions on STCI pairs with singular carriers or higher multiplicity.

| Bidegree | General residual degree | General residual genus | Simple attachments |
|---|---:|---:|---:|
| \((4,5)\) | 16 | 30 | 22 |
| \((5,5)\) | 21 | 51 | 26 |
| \((5,6)\) | 26 | 77 | 30 |
| \((6,6)\) | 32 | 112 | 34 |

For example, a general pair of quintics through \(C\) gives a genus-51 curve
of degree 21 attached at 26 points. This is the baseline geometry from which
one may deliberately specialize the residual and increase thickness along
\(C\). Since 25 is not divisible by four, \((5,5)\) itself cannot be a
sole-support endpoint; it is a useful geometry laboratory. The first equal
degree beyond quartics with an arithmetically possible endpoint is \((6,6)\).

## 3. New deduction: attachment-map dominance for all \(a,b\ge4\)

For an actual pair let \(f,g\) be its first-normal sections. Their determinant
is a section of

\[
\det N^*_{C/\mathbf P^3}\otimes\mathcal O_C(a+b)
\simeq\mathcal O_{\mathbf P^1}(N),
\qquad N=4(a+b)-14.
\]

On the open set where the pair is proper and this determinant is nonzero,
there is a morphism

\[
\beta_{a,b}:(F_a,G_b)\longmapsto[\det(f,g)]
\in\mathbf P H^0(\mathbf P^1,\mathcal O(N)).\tag{2}
\]

For \(a=b\), it descends to the Grassmannian of pencils. Its zeros give
the scheme \(C\cap D\), where \(D\) is the curve linked to the reduced \(C\).
This remains true when \(D\) is nonreduced. Locally write

\[
F=A x+B y,\qquad G=C_1x+D_1y.
\]

The elementary codimension-two linkage calculation gives

\[
((F,G):(x,y))=(F,G,AD_1-BC_1).
\]

After restriction to \(C\), the intersection ideal is therefore the first-normal
determinant. When the determinant is nonzero, \(D\) does not contain \(C\)
as a component and this is a finite effective divisor. The determinant-zero
locus requires higher-order data; it is outside the domain of (2).

**Proposition, provisional.** For every \(a,b\ge4\), \(\beta_{a,b}\) is
dominant and has surjective differential at the following explicit proper
pair:

\[
F_a=x_0^{a-4}F_4,\qquad G_b=x_3^{b-4}G_4.\tag{3}
\]

In particular a **general** divisor of degree \(N\) on the fixed marked
\(C\) is the attachment divisor of an actual proper \((a,b)\) pair. On a
dense open set of divisors it can also be realized with the smooth integral
residual of Section 2. This is a generic existence statement, not a claim
that every special effective divisor is realized by a smooth residual.

**Proof.** On \(x_0=1\), put

\[
u=x_1,\quad X=x_3-u^4,\quad Y=x_2-u^3.
\]

The first symbols at (3) are

\[
f=(-1,0),\qquad
g=(-3u^{4b-8},4u^{4b-7}).
\]

For actual global perturbations \(h\in V_a,k\in V_b\), with symbols
\((A_h,B_h),(A_k,B_k)\), the affine determinant differential is

\[
\delta\det
=u^{4b-16}(4u^9A_h+3u^8B_h)-B_k.\tag{4}
\]

The inherited, independently audited quartic calculation supplies

\[
\{4u^9A_h+3u^8B_h:h\in V_4\}
=\langle u^8,\ldots,u^{18}\rangle,
\quad
\{B_k:k\in V_4\}=\langle1,u,\ldots,u^{10}\rangle.\tag{5}
\]

For any ambient monomial \(M\) of degree \(r\), multiplication by \(M\)
multiplies a first-normal symbol of a form vanishing on \(C\) by \(M|_C\).
Here \(M|_C=u^w\), with \(w\) a sum of \(r\) elements of \(\{0,1,3,4\}\).
For \(r=1\), the possible shifts are \(0,1,3,4\), whose translates of an
interval of length eleven overlap to fill an interval four longer. Iterating
this observation for each extra degree shows that the products of quartic
perturbations with degree-\(r\) monomials span every exponent from the old
minimum to the old maximum plus \(4r\). These are actual homogeneous
perturbations over \(k\); there is no substitution of arbitrary \(k(C)\)
coefficients.

Applying this to (5), the \(h\)-part of (4) contains

\[
\langle u^{4b-8},\ldots,u^N\rangle,
\]

and the \(k\)-part contains

\[
\langle1,u,\ldots,u^{4b-6}\rangle.
\]

Their intervals overlap and cover \(0,\ldots,N\), proving surjectivity.
The base determinant is \(-4u^{4b-7}\), or homogeneously

\[
-4s^{4a-7}t^{4b-7}.
\]

It is nonzero. The pair (3) is proper: the accepted proper quartic pair
has no common factor, and the additional factors \(x_0,x_3\) do not divide
the opposite quartic. Thus it is a point of the stated domain. Affine
surjectivity gives projective surjectivity; when \(a=b\), the infinitesimal
change-of-basis directions affect the determinant by a scalar, so quotienting
by them preserves projective surjectivity. Source and target are smooth at
this point, and the differential criterion proves local smoothness and
dominance. The smooth-integral-residual open set in the irreducible source
has dense image under a dominant map; constructibility gives the asserted
dense open set of target divisors. □

The point (3) usually has nonreduced residual components on coordinate planes.
That causes no defect in the argument: it is only a regular point of the
**parameter space and attachment map** used to prove dominance. It is not
asserted to be a smooth residual example.

For equal degrees, the generic attachment fiber has dimension

\[
2(v_d-2)-(8d-14)
=\boxed{2\binom{d+3}{3}-16d+8}.\tag{6}
\]

Thus the numbers are 40 for quintic pencils and 80 for sextic pencils.
The attachment divisor leaves a great deal of actual global equation freedom.
Equation (6) is not a count of distinct residual isomorphism types, nor proof
that all analytic residual behavior is available in one fiber.

## 4. The residual also remembers a global cohomological defect

The same quadric sequence above, now for all integral twists, gives

\[
H^1(I_C(n))=
\begin{cases}k,&n=1,\\0,&n\ne1.\end{cases}\tag{7}
\]

Indeed the only nonzero Künneth term in
\(H^1(\mathcal O_Q(n-1,n-3))\) occurs at \(n=1\), namely
\(H^0(\mathcal O_{\mathbf P^1})\otimes H^1(\mathcal O_{\mathbf P^1}(-2))\).
Thus the fixed curve's Rao module is a copy of \(k\) in degree one, annihilated
by the positive-degree coordinate ideal. This is standard for this curve,
and even the official [Macaulay2 SpaceCurves documentation](https://www.macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/SpaceCurves/html/_rao__Module.html)
uses the monomial curve \(\{1,3,4\}\) as its example; this is explicitly not
claimed as a new discovery.

Classical complete-intersection linkage yields

\[
H^1(I_D(n))\simeq H^1(I_C(a+b-4-n))^*,
\]

so

\[
\boxed{H^1(I_D(n))=
\begin{cases}k,&n=a+b-5,\\0,&n\ne a+b-5.\end{cases}}\tag{8}
\]

For clarity, the degree shift can be reconstructed without trusting a shift
convention. The linkage sequence is

\[
0\to I_Y(n)\to I_D(n)\to\omega_C(n+4-a-b)\to0.
\]

The complete intersection \(Y\) is ACM. Duality on \(C\) and on \(Y\) turns
the kernel defining \(H^1(I_D(n))\) into the dual of the cokernel of

\[
H^0(\mathcal O_Y(a+b-4-n))\to
H^0(\mathcal O_C(a+b-4-n)).
\]

Since all sections on \(Y\) lift from projective space, this cokernel is
\(H^1(I_C(a+b-4-n))\). This proves the displayed formula and (8).
The linked \(D\) is locally Cohen–Macaulay; smoothness and reducedness are not
required for linkage duality. On the determinant-nonzero locus it is the
geometric residual with no \(C\)-component. On the determinant-zero locus,
the colon residual can itself retain \(C\), so it must not be identified with
the residual cycle away from \(C\).

The classical framework is recorded in Hartshorne's primary exposition
[*Experiments with Gorenstein Liaison*, Section 1, Theorem 1.1](https://arxiv.org/html/math/0106250v1):
for curves in projective three-space, Rao modules govern even liaison classes.
No assertion here that a numerical genus/degree and module alone determine
a curve, an embedding, or an actual pair of equations.

There is a useful connection to a very small cohomological model: the module
in (8) is annihilated by the positive-degree coordinate ideal, so these
residuals are diameter-one arithmetically Buchsbaum curves. Since the dual of
the one-dimensional module is again a one-dimensional module up to shift,
Rao's theorem puts all of them in the same even liaison class as the fixed
quartic, after the appropriate degree shift. This is a standard liaison
interpretation, not a classification of their singularities or attachment
maps. It suggests constructing residuals via basic double links and
Rao-preserving deformations, then testing the additional requirement that
the particular fixed embedded C be their direct partner.

This supplies a global companion to the formal neighborhood: a proposed
degree-\(ab-4\) residual cannot be arbitrary even when its attachments are
flexible. For a quintic link its one-dimensional deficiency lies in degree
five; for a sextic link it lies in degree seven. These are useful exact
filters in constructive searches.

## 5. Evidence, literature boundary, and next experiments

The new standard-library verifier
[verify_containing_pair_boundary_degrees_2026_10_27.py](../computations/verify_containing_pair_boundary_degrees_2026_10_27.py)
constructs the actual homogeneous restriction-kernel basis separately in each
degree, differentiates (3), and checks 27 higher/mixed-degree cases over
\(\mathbf Q\): \((4,5),(5,4)\), and \(5\le a,b\le9\). Every derivative column
is a scalar times a single monomial, so its exact rank is the number of
exponents with a nonzero column. The saved
[JSON output](../computations/containing_pair_boundary_degrees_2026_10_27.json)
records supports, ranks, and formula values. Run:

```sh
python3 research/computations/verify_containing_pair_boundary_degrees_2026_10_27.py
```

All 27 checks passed. They corroborate the coordinate formulas in new degrees;
the proof using multiplication in Section 3 establishes the all-degree
statement. The finite output alone would not prove it. No inherited proof
or accepted quartic smoothness certificate was replayed.

A separate bounded attempt at an exact rational sextic benchmark is retained
in [the exploratory Macaulay2 script](../computations/explore_sextic_residual_2026_10_27.m2)
and [partial output](../computations/sextic_residual_partial_2026_10_27.txt).
It completed properness and the residual degree-32/genus-112 calculation.
It was interrupted during the later scheme-union comparison; the Jacobian
and reduced-attachment assertions were not reached. Thus it supplies no
computed smooth sextic benchmark. An initial syntax error in the intersection
call was corrected before this bounded rerun. The all-degree geometric proof
does not depend on this unfinished experiment.

Primary literature was checked on 2026-10-27 for liaison/Rao modules and
blowup/Bertini inputs. Searches for the fixed quartic's all-degree attachment
dominance did not identify an existing precise statement; that is a limited
search observation, not a novelty certificate. The standard material is
identified as such above. The following routes are the next substantive
construction tests:

1. **Fix a general attachment divisor in degree \((6,6)\).** The sextic pencil
   space has dimension 114 and the attachment map has target dimension 34,
   leaving an 80-dimensional generic fiber. Construct one exact rational
   smooth residual in a selected fiber, then examine its node and splitting
   strata. The expected residual has degree 32 and genus 112. This begins in
   the first equal degree beyond quartics where full degree absorption is
   arithmetically possible, without assuming it occurs.
2. **Separate attachment concentration from absorption.** Moving 34 points
   together changes contact distribution but leaves generic multiplicity one
   as long as the determinant remains nonzero. To increase thickness, cross
   the determinant-zero locus and compute higher symbols of actual equations.
   Mere concentration of the attachment divisor is not that crossing.
3. **Use reverse linkage as a construction tool.** Search for residual
   schemes in the exact liaison class (8), together with a containing surface
   and the divisor relation \(D\sim bH-C\). Verify the colon identities and
   full homogeneous equations. A formally admissible attached germ or a
   curve with the right Hilbert polynomial does not supply those global data.
4. **Compare fixed-boundary fibers with moduli of curves.** The 40- and
   80-dimensional fibers provide actual global directions invisible to the
   marked attachment divisor. Determine which affect the residual's
   normalization, singularities, and Rao-preserving deformations. The
   established quartic node-smoothing example is a precedent; it need not be
   recomputed.

What remains unresolved is the geometry of the determinant-zero strata,
their higher-order attachment replacements, and whether any higher-degree
stratum reaches sole support. Nothing here presupposes the answer.
