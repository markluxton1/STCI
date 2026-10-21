# The cubic image and the anticanonical conductor interface

Date: 2026-10-21. Status: **new exact computation and proposed geometric
interface; independent review requested**. This note concerns the fixed
curve C0 and the conditional pair (2,12;6,16;epsilon2). It does not
claim emptiness or existence. No canonical record is changed.

## 1. Explicit cubic image

Put q=x0*x3-x1*x2, A=x0^2*x2-x1^3,
B0=x0*x2^2-x1^2*x3, D0=x2^3-x1*x3^2. The seven cubics

    q*x0,q*x1,q*x2,q*x3,A,B0,D0

generate I_C0(3). They define the line bundle L=3H-E on
B=Bl_C0(P3), and a morphism phi:B->P6. The pair of maps given by
H and L is the graph closed immersion B->P3 x P6: the seven cubics
give the usual relative Proj embedding of the Rees algebra, after
twisting by O(3). In particular H+L is ample.

In P6 with coordinates y0,...,y6, the image is cut out by

    y0*y5-y2*y4+y1^2,
    y0*y6-y2*y5+y1*y3,
    y1*y5-y3*y4+y0*y2,
    y1*y6-y3*y5+y2^2,
    y4*y6-y5^2+y1*y2.                                  (1)

The new exact M2 calculation
[cubic-image verifier](../computations/conditional_2_12_cubic_image_2026_10_21.m2)
checks the following over QQ:

* substituting the seven displayed cubics makes all five equations zero;
* their quotient ring has dimension four and degree five;
* the affine singular locus is zero-dimensional (only the cone vertex),
  so their projective threefold V is smooth;
* the quotient has free resolution with ranks (1,5,5,1) and shifts
  (0,2,3,5).

The resolution proves arithmetically Cohen--Macaulay, type one, with
canonical sheaf omega_V=O_V(-2). It also gives H0(O_V)=k, so V is
connected. A smooth connected projective scheme here is integral.
The cubic map is birational onto its image because off q=0 the first
four cubics recover [x0:x1:x2:x3]. Its image is closed, dimension
three, and contained in integral V of dimension three, hence equals V.
The same statements base-change to every characteristic-zero field.

## 2. An explicit blowup identification

Let Gamma be the conic cut out on V by y0=y1=y2=y3=0; equation (1)
leaves y4*y6-y5^2=0 in P2, so Gamma is smooth. The inverse rational
map V-->P3 is the projection [y0:y1:y2:y3]. Its graph closure is
Bl_Gamma(V), since its base ideal on V is exactly the ideal generated
by these four sections, whose scheme of zeros is Gamma.

Under the graph closed immersion B->P3 x V, the image is exactly this
graph closure: on the dense open q!=0 it is the graph of the inverse
birational maps, and B is integral and the graph embedding is closed.
Thus

    B = Bl_Gamma(V).                                    (2)

The exceptional divisor of (2) is Q'=2H-E=L-H, the strict transform
of the original smooth quadric. Indeed the common zero divisor of
the four pullback sections y0,...,y3 is Q': each section is the strict
q factor times x_i, and the four x_i have no common zero. The map
Q'->Gamma is the contraction of one ruling, with degree-two image
polarization. This proof needs no classification theorem for V5.

## 3. The actual sextic descends to an anticanonical surface

The exact 23-element source basis in
[the symbol computation](2026-10-20-conditional-2-12-symbol-map.md)
consists of products of the seven cubics. Consequently every actual
sextic in H0(I_C0^2(6)) gives a quadric section T of V with

    D=phi^* T,              O_V(T)=O_V(2),
    omega_T=O_T.                                     (3)

For an actual supported pair, F6 cannot have Q as a component, by
the quadric Picard argument in
[the norm note](2026-10-20-conditional-2-12-geometric-continuation.md).
Thus D has no Q' component, T does not contain Gamma, and D is the
strict transform as well as total pullback of T. Off Q', phi is an
isomorphism, so local normalizations and conductors there transfer
between D and T unchanged.

For the remaining conductor discussion one needs T integral. This
follows within the actual supported-pair scope from the accepted
exclusion of all carriers of degree at most four. Every irreducible
factor of F must contain C: otherwise its positive-degree intersection
with G gives a curve outside C. Each such factor is itself a supported
carrier for C with mate G. Hence each has degree at least five. A
sextic can have only one such factor and no higher power, so F, D,
and T are integral. This use of the lower-carrier exclusion must be
checked against its literal canonical hypotheses before applying the
conductor claim; it is not needed for (1)-(2).

## 4. Full conductor of a Gorenstein anticanonical surface

Assume T integral and let nu:Tn->T be its finite normalization.
The normal surface Tn is Cohen--Macaulay. Finite duality and
omega_T=O_T identify the canonical module on Tn with its conductor
ideal:

    omega_Tn = Hom_T(nu_*O_Tn,O_T) = I_Delta subset O_Tn. (4)

The identification on the right is the conductor as a fractional
ideal in the common function field. Since the canonical module has
depth two, Delta is a pure Cohen--Macaulay curve. The local
canonical-ideal quotient argument additionally gives

    omega_Delta = O_Delta.                              (5)

For detail apply Hom(-,omega_Tn) to
0->I_Delta->O_Tn->O_Delta->0. The map
Hom(O_Tn,omega_Tn)->Hom(I_Delta,omega_Tn) identifies with
I_Delta->O_Tn because End(omega_Tn)=O_Tn on a normal domain;
its cokernel is O_Delta, which is Ext1(O_Delta,omega_Tn), the
canonical module of Delta. These statements do NOT require the
normalization itself to be Gorenstein or the conductor to be Cartier.
Serre duality also gives chi(O_Delta)=0.

An immediate useful consequence is that an integral conductor
component R with generic multiplicity one satisfies pa(R)<=1.
Finite closed-immersion duality gives

    omega_R=Hom_Delta(O_R,omega_Delta)=Ann(I_R) subset O_Delta.

Its composition with O_Delta->O_R is generically nonzero because
Delta is generically reduced along R. It is injective, since
omega_R is torsion free on integral R. The finite-length cokernel
implies deg(omega_R)<=0, hence 2pa(R)-2<=0. Nilpotents on OTHER
conductor components do not change this argument.

This supplies an interface for excluding local models that force a
generically reduced conductor branch with delta invariant at least
two. It does not yet classify all possible nonreduced conductor
components. In particular a necessary low-order root incidence does
not supply an actual integral surface T or its conductor.

## 5. Audit boundary

The M2 calculation proves the exact ideal, resolution, degree, and
projective smoothness assertions, not a global pair. Independent
review is requested for the graph/blowup identification, use of the
lower-carrier exclusion for integrality, finite-duality global
identification, and the generic-multiplicity-one component lemma.
All conclusions retain the exact conditional-pair scope.
