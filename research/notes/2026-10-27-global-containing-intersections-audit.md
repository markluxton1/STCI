# Independent audit: global pairs and all-degree attachment dominance

Date: 2026-10-27. Reviewer: positive-characteristic research agent,
independent of the proposing global-intersections agent. Source:
[General intersections through the quartic](2026-10-27-global-containing-intersections.md).
**Outcome:** the proposed all-degree attachment-map deduction and its
geometric and liaison consequences pass independent reconstruction with
their stated characteristic-zero and general-pair hypotheses. They remain
provisional; this audit does not promote a result or settle sole support.

## 1. Premises and authority boundary

The fixed curve is C=[s^4:s^3t:st^3:t^4] over an algebraically closed field
of characteristic zero. R-0020 supplies N_C^*=O(-7)^2. R-0021 supplies
properness of F4=x1^4-x0^3*x3 and G4=x2^4-x0*x3^3. Those canonical premises
were not re-proved or recomputed.

The degrees-at-most-three ideal generation, graph embedding of the blowup,
and the two quartic differential images are taken from the [October 25
laboratory](2026-10-25-ci-cycle-deformation-laboratory.md) and its
[independent audit](2026-10-25-ci-cycle-exploration-audit.md). They are
**reviewed provisional evidence**, not promoted canonical results. I read
their exact statements and independent reconstruction, but did not rerun
the inherited quartic verifier. The all-degree conclusion is conditional
on those explicit premises in this authority sense, and the source note
correctly preserves that dependency.

## 2. Actual-pair witness and multiplication argument

For every a,b>=4 the proposed witness is

    Fa=x0^(a-4)*F4,   Gb=x3^(b-4)*G4.

Its two forms are coprime. The inherited quartics have no common factor;
x0 does not divide G4, x3 does not divide F4, and x0 and x3 are distinct
prime factors. Thus multiplication has not introduced a common surface.
This is a valid proper pair even though its residual scheme is often
nonreduced and reducible.

On x0=1 with u=x1, X=x3-u^4, Y=x2-u^3, its first-normal symbols are
(-1,0) and (-3u^(4b-8),4u^(4b-7)). Direct differentiation yields

    delta det = u^(4b-16)*(4u^9*A_h+3u^8*B_h)-B_k.

The factor x0^(a-4) has affine value one; no omitted a-dependent factor
is needed on this chart. Homogenization supplies the correct s exponent.

If h vanishes on C, then the first symbol of Mh is M|C times that of h:
the derivative of M times h contributes no first-normal term. For a
degree-r ambient monomial M its restriction weight is a sum of r terms
from {0,1,3,4}. Translating an eleven-term interval by 0,1,3,4 fills the
entire interval enlarged by four; induction proves the asserted coverage
for every r>=0. This uses products of actual global forms and preserves
constant coefficient constraints over k.

Applying it to the inherited quartic images gives a first-input image
containing every monomial in [4b-8,N] and a second-input image containing
every monomial in [0,4b-6], where N=4(a+b)-14. These intervals overlap in
three monomials and cover all 0,...,N. This independently proves affine
differential surjectivity in every bidegree a,b>=4; it is not an
extrapolation from the finite computation.

The base determinant is -4u^(4b-7), equivalently
-4s^(4a-7)t^(4b-7). It is nonzero and has the required total degree N.
Projectivizing removes its scalar direction. For equal degrees the GL2
change-of-basis directions also map to scalar multiples of that determinant,
so the projective map factors through the pencil Grassmannian without
losing target tangent directions. The parameter spaces and target are
smooth; surjective differential gives local smoothness at the witness,
and hence dominance.

The irreducibility of the pair parameter space matters in passing to a
general divisor. Its nonempty open locus with smooth integral residual
still maps dominantly, and its constructible image contains a nonempty
target open. This proves realization for **general** effective divisors.
It does not prove realization of every special divisor or a description
of every fiber.

## 3. General smooth integral residual and the blowdown bridge

Write B=Bl_C(P3), with H the pulled-back hyperplane and E exceptional.
The inherited graph embedding makes L4=4H-E very ample. Since H is
globally generated, Ld=L4+(d-4)H is very ample for every d>=4. General
members of La and Lb meet in a smooth geometrically integral curve:
apply Bertini to the smooth threefold, then to the resulting smooth
integral surface, using the restriction of the other very ample bundle.

The primary [smooth Bertini statement](https://stacks.math.columbia.edu/tag/0FD4)
requires generation and an immersion, supplied here by very ampleness.
The primary [irreducible Bertini statement](https://stacks.math.columbia.edu/tag/0G4C)
applies to these very ample hyperplane systems in dimensions three and two.
I checked those sources independently in this audit.

Smoothness upstairs alone would not establish smoothness of the image.
Here dominance of the attachment map implies simple determinant zeros for
a general pair. At such a zero the normal matrix has rank one: if its
four entries all vanished, its determinant would vanish to order at least
two along C. Choose a generator smooth at the rank-one point. On its
smooth surface, the other equation has the form y*h(u,y), with C=(y)
and h(u,0) having a simple zero. Thus the residual h=0 is smooth and
meets C transversely. This verifies the source's blowdown argument.

There is also a complementary direct check: global generation of I_C(a)
gives a generated rank-two conormal bundle on the one-dimensional C, so a
general Fa has no normal zero anywhere on C. Such a surface is smooth
along C and general smoothness holds away from C. The strict transform
of that surface is isomorphic to the surface, since blowing up a Cartier
divisor C on it is an isomorphism. This provides an independent route
around a possible contraction singularity.

Adjunction on this smooth degree-a surface gives C^2=14-4a and residual
class bH-C. I independently obtain

    deg D=ab-4,
    C.D=4(a+b)-14,
    g(D)=(a+b-4)*(ab-8)/2.

The formulas give (degree,genus,attachments)=(21,51,26) for (5,5) and
(32,112,34) for (6,6), agreeing with the source. They describe the general
multiplicity-one regime. A determinant identically zero or singular
carrier cannot be imported into this smooth-surface calculation without
further analysis.

## 4. Rao-module shift and liaison interpretation

The quadric sequence reduces H1(I_C(n)) to H1(O_Q(n-1,n-3)). Kunneth
gives one copy of k at n=1 and zero in every other integral twist. For
n<=0 both possible H1 terms have a zero H0 factor (at n=0 the first
factor is O(-1)); for n>=2 neither term contributes. Thus M_C is k in
degree one, with the positive-degree coordinate ideal acting trivially.

For the locally Cohen–Macaulay residual D linked by a proper (a,b) CI Y,
the linkage sequence is

    0 -> I_Y(n) -> I_D(n) -> omega_C(n+4-a-b) -> 0.

Since Y is ACM, H1(I_D(n)) is the kernel of the next H1-to-H2 map.
Duality on C and the Gorenstein CI Y identifies its dual with the cokernel
of H0(O_Y(a+b-4-n)) -> H0(O_C(a+b-4-n)). All sections on Y lift from P3,
so this cokernel is H1(I_C(a+b-4-n)). Hence

    H1(I_D(n)) = H1(I_C(a+b-4-n))^*,

and the unique nonzero degree is n=a+b-5. This confirms the source's sign
and shift without assuming a graded-module convention. In particular the
quintic-link deficiency is in degree five and sextic-link deficiency in
degree seven.

I independently checked [Hartshorne's primary exposition, Theorem 1.1(a)](https://arxiv.org/html/math/0106250v1),
which identifies even liaison classes of locally Cohen–Macaulay curves in
P3 by Rao modules up to shift. Since the one-dimensional module is
self-dual up to its degree, the asserted common even liaison class follows.
The source correctly does not infer that degree, genus, module, or liaison
class alone supplies a direct link to this **fixed embedded** C.

## 5. Fresh computation and exact limitations

I ran only the new verifier
[verify_containing_pair_boundary_degrees_2026_10_27.py](../computations/verify_containing_pair_boundary_degrees_2026_10_27.py).
All 27 higher/mixed-degree calculations passed. I parsed its output and
compared it with the saved JSON; the objects agree exactly. Its basis
construction groups actual homogeneous monomials by restriction weight,
and its nonzero derivative columns are single monomials, so the finite
rank count is exact over Q. The generic fiber dimensions independently
reconstruct as 40 for quintic pencils and 80 for sextic pencils.

These finite checks corroborate the new coordinate formulas. They do not
prove the all-degree result; the multiplication proof above does that
from the reviewed provisional quartic inputs. They establish neither
surjectivity at every source point nor a smooth residual over every target
divisor. The determinant-nonzero domain excludes the higher-thickness
strata central to any eventual sole-support construction.

No required correction was found. No inherited verifier, accepted proof,
canonical record, or navigation file was altered by this audit.
