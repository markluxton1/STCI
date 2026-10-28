# Independent audit: two blowups and actual residual geometry

Date: 2026-10-28. Reviewer: `singular_carrier_construction` research agent.
Source reviewed: [two projections of containing
intersections](2026-10-28-blowup-residual-geometry.md).

**Outcome: PASS for the scoped deductions (2)–(10), after a proof repair
to the actual-cycle assertion (6).** New work remains provisional and
unpromoted. This review independently reconstructs the new deductions;
it treats the already reviewed cubic-image graph and R-0020 as inputs,
without rerunning their inherited certificates.

The literal setup is the fixed quartic C in P3 over an algebraically
closed characteristic-zero field, B=Bl_C(P3), and the inherited second
description B=Bl_Gamma(V), with V the smooth quintic del Pezzo threefold
and Gamma a smooth conic. Here E is exceptional for the P3 projection;
Q' is exceptional for the V projection. They cannot be interchanged.

## 1. All-degree section spaces, including the fixed-factor region

From L=3H-E and Q'=2H-E I independently obtain

\[
 H=L-Q',\quad E=2L-3Q',\quad
 aH-rE=(a-2r)L-(a-3r)Q'.
\]

For nonnegative e, the pushforward of O_B(-eQ') is I_Gamma^e. The center
is smooth codimension two; in regular parameters its ideal powers are
exactly the order filtration, so there is no normalization or symbolic
power substitution. The same applies at C. This yields source (2) when
a>=3r.

For j>=0, the pushforward of O_B(jQ') is O_V: any potential pole is
supported over a codimension-two locus in the smooth normal variety V,
so a rational function regular away from it extends. Therefore when
2r<=a<=3r the section space is H^0(V,O(a-2r)), with fixed divisor
(3r-a)Q' upstairs and fixed factor q^(3r-a) downstairs. When a<2r,
the same pushforward leaves a negative ample twist, so there are no
sections. This checks the omitted sign ranges independently and avoids
using a supposed formula with a negative ideal power.

For a section P of degree k vanishing to order e along Gamma, the
substitution P(c_0,...,c_6) is divisible by q^e. At the generic point of
the irreducible quadric, q is a uniformizer and measures the exceptional
order of the conic blowup. Divisibility at that prime implies polynomial
divisibility in the ambient polynomial UFD. The quotient has degree
3k-2e and C-order at least k-e. The exact-order checks in source §2 are
necessary: an additional q factor measures excess conic order, whereas
an additional E component measures excess C-order and corresponds to
Sigma in V. Neither exactness follows from the class of a line bundle
alone. **PASS.**

## 2. The nonnormal anticanonical surface and its full conductor

Literal substitution gives c_0*c_3-c_1*c_2=q^3. The total transform of
q is E+Q', while the quadratic section in the cubic map removes 2E.
Thus its divisor on B is E+3Q'. Since the nonexceptional component E
has multiplicity one, its image is the reduced integral Cartier surface
Sigma in V. A Cartier divisor on smooth V has no embedded components,
so this is stronger than an equality of supports.

A conic-blowup fiber is a trisecant ruling in Q'. Its intersection with
E has length three and does not contain the whole ruling. The proper
map E→Sigma consequently has finite fibers; it is finite and birational,
as it is an isomorphism off Q'. Smooth E is the normalization. This
argument does not mistake E for the divisor contracted by the V
projection.

The bundle restrictions are, independently,

\[
 H|_E=(4,0),\quad E|_E=(7,-1),\quad Q'|_E=(1,1),
 \quad L|_E=(5,1).
\]

Because Q is smooth along C, B_0=E∩Q' is a reduced smooth section of
E→C. In Segre coordinates the equation va^3-ub^3 of C gives the
degree-three map from B_0 to the conic center, with the stated two
totally ramified values.

Adjunction gives omega_Sigma=O_Sigma. Finite duality identifies
Hom_Sigma(nu_*O_E,O_Sigma), as an O_E-module, with omega_E. In the
common function field, that Hom module is the conductor ideal. It is
therefore an **invertible actual ideal** in O_E, supported on the one
irreducible curve B_0. Since omega_E=O_E(-2,-2) and B_0=(1,1), the
conductor is exactly O_E(-2B_0). There can be no additional punctual
ideal factor: an invertible ideal on the smooth surface is determined
by its effective Cartier divisor. This is not just a generic
conductor multiplicity or a linear-equivalence claim. **PASS.**

At a general conic point the three normalization preimages are distinct,
and E meets Q' transversely. The blowup has thus separated three smooth
transverse branches of the transverse plane curve: it is an ordinary
triple point there. This does not identify the type at the ramified
endpoints.

## 3. Actual cycles and exceptional visibility

There was one proof issue in the initial draft: a Chow projection
formula only proves equality modulo rational equivalence, and does not
by itself prove the displayed equality of actual 1-cycles. I reported
this to the proposer, who repaired source §4.

Here is the needed independent argument. At the generic point of C,
the ambient local ring is a two-dimensional regular local ring with
residue field k(C). The actual pair has local intersection length m
and orders r,s. The blowup formula for two plane-curve germs gives
m=rs plus the sum of their strict-transform intersection lengths on
the exceptional P1, weighted by residue degrees. That sum is precisely
the coefficient of C in pi_*[W]. Off E, the blowup is an isomorphism
and the residual cycles agree with their strict transforms. Hence

\[
 \pi_*[W]=(m-rs)[C]+R
\]

holds as actual cycles. Computing the Chow class afterward checks it
but does not replace this local argument.

The strict-transform intersection W is a pure curve because the strict
divisors have no common surface component in smooth B. Therefore R=0
is equivalent to Supp(W) contained in E. A component contained in E
can dominate C or map to a point; neither is an additional residual
curve downstairs. Conversely a contracted ruling of Q' is an actual
trisecant line in P3, despite having a point image in V. The source
table records both possibilities correctly. **PASS after repair.**

I also expanded the four triple products from
H^3=1, H^2E=0, HE^2=-4, E^3=-14. They give exactly source (8).
Those numbers do not identify residual support when W has components
in E or Q'.

## 4. General-pair residuals and blowdown to V

For the inherited general pair with a,b>=4, m=r=s=1. There are no
E components dominating C; the general first-normal data do not vanish
simultaneously at a point, so no whole exceptional fiber appears.
Thus W is the strict transform of the smooth residual D. Blowing up
the finite Cartier divisor D∩C on smooth D changes no curve scheme,
and W is isomorphic to D.

On Q'=Q the strict equations restrict to full systems of bidegrees
(a-1,a-3), (b-1,b-3). Surjectivity follows from the quadric restriction
sequence and H^1(P3,O(a-2))=0. At a general contracted ruling the
leading forms are general binary forms of degrees a-3,b-3 and have
no common projective root. The generic conic multiplicity is
(a-3)(b-3).

The two restricted equations have transverse finite common zeros on
Q'. To test injectivity after blowdown, fix two distinct points on a
single contracted ruling. Each equation imposes two independent
conditions, because its degree on that ruling is at least one. The
ruling and two points vary in a three-dimensional space, against four
conditions. A general pair therefore has no such identification.
At every point of W∩Q', transversality gives a local parameter t on W
which is the exceptional parameter. In the blowup chart the projection
is (u,t,v)↦(u,t,tv); its derivative on W is nonzero. This proves the
closed immersion W→V rather than merely generic birationality.

Independently the L and Q' triple products now give

\[
 \deg_M D'=3ab-4a-4b+2,
 \qquad |D'\cap\Gamma|=2ab-4a-4b+6.
\]

The second scheme is reduced because the conic ideal restricts in the
same chart to (t) on W. It concerns attachment to the **reduced conic**,
not to its higher primary structure. The numerical table agrees with
these formulas. **PASS.**

## 5. Literature and authority boundary

I freshly opened [Cheltsov–Przyjalkowski–Shramov, Lemma
6.13](https://arxiv.org/html/1809.09223v1#S6.L13): it explicitly includes
the parametrization [u^4:u^3v:uv^3:v^4] and the two blowups connecting
P3 and V5. The model is established geometry. I also inspected the
[Stacks blowup construction](https://stacks.math.columbia.edu/tag/01OF)
and the [finite-duality Hom formula](https://stacks.math.columbia.edu/tag/0FKW).
These support the standard ingredients; the exact conductor and
residual dictionary are reconstructed above.

The inherited cubic-image evidence is reviewed provisional, and all
new source deductions remain provisional after this audit. Nothing
here transports a fixed-carrier STCI conclusion from P3 to Sigma,
computes every conic-vanishing section space, supplies a complete
absorption pair, or changes the unrestricted characteristic-zero
open status. The useful constructive output is an actual-section
dictionary on a fixed smooth threefold, with the graph retaining the
residual curves lost by either projection separately.
