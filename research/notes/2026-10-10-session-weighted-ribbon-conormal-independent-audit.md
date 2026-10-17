# Independent audit: the weighted ribbon conormal obstruction

Date: 2026-10-10. Auditor: `weighted_ribbon_conormal`, delegated by
`bisection_weighted_normalization`. Status: **PROVED HERE, conditional
on the accepted genus-two bisection reduction**. This is an independent
geometric audit; the identities below are written out exactly, and no
additional computer execution is asserted. No canonical frontier file
was edited by this auditor.

## 1. Inputs and the result

Work over an algebraically closed field of characteristic zero. Let

    C0=[s^4:s^3t:st^3:t^4] in P3.

Let `nu:S->X` be the normalization of an integral nonnormal quartic
containing the smooth embedded C0, and write H for the pulled-back
hyperplane bundle. In the accepted normalization sectional-genus-two
stratum,

    chi(O_S(mH))=2m^2+m+1.

Suppose the bisection mate reduction supplies an actual section

    Q in H0(S,2H),   div(Q)=2c_S,

where the reduced prime curve `c_S` maps isomorphically to C0. In
particular this is an actual effective Cartier double divisor; the
statement is stronger than a numerical doubling relation. The
[second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md)
supplies precisely this actual relation in its bisection mate setting.

**Conclusion:** these inputs are incompatible with the specific
embedding of C0. Consequently a mate cannot exist in this bisection
stratum. The proof does not need to classify the conductor cover,
root-of-unity ratios, exceptional graphs, or singular conic fibers.
It does not by itself exclude the separate section/trisecant stratum,
all other quartic normalizations, or carriers of higher degree.

## 2. An actual Cartier double divisor with smooth reduction is a ribbon

Set `R=V(Q)` on S. A normal surface is Cohen--Macaulay. Since Q is a
nonzerodivisor, R is a Cohen--Macaulay curve, including at every
singular point of S. At its generic point, S has a discrete valuation
ring and Q has valuation two. Thus the nilradical J of R has generic
rank one and `J^2` vanishes generically.

The coherent subsheaf `J^2` of `O_R` is therefore supported on finitely
many closed points. A one-dimensional Cohen--Macaulay scheme has no
nonzero subsheaf of its structure sheaf supported on finitely many
points: locally a nonzerodivisor in the maximal ideal annihilates no
nonzero element, whereas some power of that maximal ideal would kill
a finite-length submodule. Hence `J^2=0` everywhere.

The square-zero J is an `O_{c_S}`-module. Its torsion is again a
finite-support subsheaf of `O_R`, and therefore vanishes. Since c_S
is a smooth curve, a coherent rank-one torsion-free sheaf on it is a
line bundle. We have an exact ribbon sequence

    0 -> J -> O_R -> O_{c_S} -> 0.

This argument uses neither smoothness of S along c_S nor a local ADE
classification. It retains the entire double structure at all closed
points.

## 3. The nilradical has degree minus eight

The effective Cartier equation gives, for every integer m,

    0 -> O_S((m-2)H) -> O_S(mH) -> O_R(mH) -> 0.

Taking Euler characteristics,

    chi(O_R(mH))
      =(2m^2+m+1)-(2(m-2)^2+(m-2)+1)
      =8m-6.

The reduced curve is P1 with `H|c_S=O_P1(4)`. If `J=O_P1(d)`, the
ribbon sequence instead gives

    chi(O_R(mH))=(4m+1)+(4m+d+1)=8m+d+2.

Consequently

    J=O_P1(-8).

The sign of the linear term matters: the polynomial above is for
`O_S`, not `omega_S`. Substituting the dualizing-sheaf polynomial
`2m^2-m+1` here would incorrectly give a degree-minus-twelve
nilradical. That incorrect value is not used.

## 4. Exact Euler and derivative computation for the fixed quartic

Write `i:P1->P3` for the displayed parametrization and `N` for its
normal bundle. Twisting the pulled-back Euler sequence by O(-8)
gives

    0 -> O(-8) -> O(-4)^4 -> i^*T_P3(-8) -> 0.

By Serre duality, the dual of its map on first cohomology is

    H0(O(2))^4 -> H0(O(6)),
    (P0,P1,P2,P3) |-> P0 s^4+P1 s^3t+P2 st^3+P3 t^4.

This map is surjective. Its monomial images have t-exponents
`{0,1,2}`, `{1,2,3}`, `{3,4,5}`, and `{4,5,6}`, which cover every
exponent from zero to six. Thus

    H0(i^*T_P3(-8))=0,

and the kernel of the displayed multiplication map is
five-dimensional. The following is an exact basis of that kernel:

    P^(0)=(st,-s^2,0,0),
    P^(1)=(t^2,-st,0,0),
    P^(2)=(0,t^2,-s^2,0),
    P^(3)=(0,0,st,-s^2),
    P^(4)=(0,0,t^2,-st).

Independence is immediate from their respective free coefficients;
alternatively, the seven monomial equations for a quadratic syzygy
leave exactly these five parameters.

Now twist the tangent-normal sequence by O(-8):

    0 -> O(-6) -> i^*T_P3(-8) -> N(-8) -> 0.

The dual of its map
`H1(O(-6))->H1(i^*T_P3(-8))` sends a syzygy P to

    sum_j Pj d(fj),
    f=(s^4,s^3t,st^3,t^4).

The syzygy identity and Euler's identity make this differential a
unique quartic multiple of `t ds-s dt`. Direct differentiation of
the five basis syzygies above gives respectively

    s^4 (t ds-s dt),
    s^3t (t ds-s dt),
    2s^2t^2 (t ds-s dt),
    st^3 (t ds-s dt),
    t^4 (t ds-s dt).

Thus the dual map, in the displayed syzygy basis and the ordinary
quartic monomial basis, is exactly

    diag(1,1,2,1,1).

It is invertible in characteristic zero. The cohomology sequence,
together with the already proved vanishing of
`H0(i^*T_P3(-8))`, now yields

    H0(N(-8))=0.

For completeness, `deg(N)=4*4-2=14`. Splitting a vector bundle on
P1 and using this vanishing therefore also gives

    N=O(7) direct_sum O(7).

The vanishing, rather than the named splitting type, is the part
needed below. This exact calculation depends on the specific
missing-middle-coordinate quartic. It is not asserted for an
arbitrary projection of the rational normal quartic without checking
its analogous derivative map.

## 5. The morphism of the entire ribbon to P3 gives a contradiction

The normalization morphism followed by the inclusion X in P3 defines
a morphism `R->P3` reducing to the given embedding of c_S as C0.
The ideal of C0 pulls back into the nilradical J, and its square pulls
back to zero because `J^2=0`. Therefore it induces a global homomorphism
of vector bundles on the reduced curve,

    I_C0/I_C0^2 = N^* -> J=O(-8).

Its space of global homomorphisms is

    Hom(N^*,O(-8))=H0(N(-8))=0.

Nevertheless this homomorphism must be nonzero at the generic point
of C0. The conductor downstairs is a line, whereas C0 is a
nondegenerate quartic; C0 is not contained in that line. At its
generic point the normalization S->X is therefore an isomorphism.
There R is an actual Cartier double curve in X, and its composition
with the closed embedding X in P3 is a closed embedding. In this
neighborhood the ambient ideal of C0 generates J in the double
curve, giving a surjective conormal map at the generic point. A
generically surjective rank-one target map cannot be the zero global
map. This is the desired contradiction.

Only generic immersion is needed here. The entire R->P3 need not be
an embedding along the conductor, and no unproved global embedding
has been assumed.

## 6. Relation to the weighted normalization presentation

The separate weighted-ring reconstruction places S in
`P(1,1,1,1,2)`, with weight-two coordinate z represented by the extra
quadratic section Q. This weighted space is smooth near C0, since
at least one of its weight-one coordinates is nonzero on every
point of C0. Along the zero section its conormal bundle restricted
to C0 is

    N_C0/P3^* direct_sum O(-8).

For the specific ribbon `R=V(Q)`, the weight-two coordinate z is
identically zero on R, so its O(-8) conormal direction maps to zero
in J. The remaining map is exactly the impossible ambient P3 map
proved above. The existence of the extra O(-8) summand in the
weighted conormal therefore does not evade the obstruction.

The direct normalization-morphism proof in Section 5 does not
depend on correctness of a weighted Hilbert--Burch reconstruction.
It remains valid with the actual Cartier doubling and genus-two
Euler polynomial as its stated inputs.

## 7. Preserved scope

The bisection-stratum exclusion is conditional on the upstream
actual relation `2c_S~2H`, not on a merely numerical class equality.
Its ribbon and generic conormal arguments include singular points
of the normalization and the entire conductor. No conclusion about
the section/trisecant branch, arbitrary carrier degrees, the
unrestricted fixed-C0 STCI question, or the universal STCI question
is supplied by this note alone.
