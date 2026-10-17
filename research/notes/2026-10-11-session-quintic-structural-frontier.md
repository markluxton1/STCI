# Quintic carriers: rationality boundary and the degree-five A4 target

Date: 2026-10-11. Owner: `oct11_quintic_structural_frontier`.
Status: **PROVED HERE / DIRECT PROOF AUDITED; NECESSARY STRUCTURAL
REDUCTIONS**. The pi=0 statement is an all-mate exclusion; the other
statements retain the explicit open conductor and carrier strata below.
Scope: an algebraically closed field of characteristic zero, the fixed
smooth rational quartic `C0=[s^4:s^3t:st^3:t^4]`, an integral quintic
`X`, and an arbitrary ambient mate. This is structural progress beyond
the quartic-carrier work, not an exclusion of all quintics or an STCI
resolution. The accompanying
[independent conormal audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
records the independently checked parts; its status takes precedence
over any unreviewed continuation lead below.

## 1. The actual normalized divisor, rather than a quartic analogy

Let `nu:S->X` be the finite normalization, `sigma:M->S` its minimal
smooth resolution, `H=nu*O_X(1)`, and `L=sigma*H`.

The quintic is regular at the generic point of C0. On its unique smooth
quadric `Q`, the curve has class `(1,3)`. If a quintic were singular
along the entire curve, its restriction to Q would contain twice C0,
leaving class `(3,-1)`, which is not effective. Hence its equation
would be divisible by q, contrary to integrality. This is exactly the
saturated-sheaf-square argument in P-011 of the
[research record](../RESEARCH_RECORD.md), not membership in the
unsaturated ideal square.

The dominating lifted curve `c` is therefore isomorphic to C0. Under
a mate, the full-support theorem also gives
`(nu^{-1}(C0))_red=c`. Intersecting the mate divisor with H gives

    H^2=5, H.c=4, b=4k,
    div_S(nu*G)=5k c ~ 4k H,
    c_num=(4/5)H.

In particular `c_num^2=16/5`. If c were Cartier on S, this would be an
integer, a contradiction. Thus every quintic mate requires a
non-Cartier point of c on its normalization. A smooth normalization,
or a lift avoiding its singular locus, is excluded in every mate
degree. More generally, if r c is Cartier, then
`16r^2/5` is integral, so `5|r`.

Do not replace the relation by `2c~mH`: intersecting with H would give
`8=5m`, which has no integer solution. The quartic double-ribbon
mechanism cannot be imported in this form.

For orientation, `dim I_C0(5)=35`. Restriction of degree-five monomials
onto the binary forms of degree twenty is surjective: sums of five
weights from `{0,1,3,4}` cover `0,...,20`. The first normal map has
the previously verified image `H0(O(13))^2` and kernel `q I_C0(3)`
of dimension seven. These dimensions are not a parameter exhaustion
or a substitute for full conductor descent.

## 2. Rationality through sectional genus three, without a mate

Let pi be the genus of a general hyperplane curve on S. A general
plane quintic has arithmetic genus six, so

    0<=pi<=6; if X is nonnormal, pi<=5,
    K_M.L=2pi-7.

**Theorem.** If `pi<=3`, the normalization of an integral quintic
containing C0 is rational. A mate is not needed.

Here `K_M.L<0`; thus no positive multiple of K_M is effective and
the characteristic-zero surface classification makes M rational or
birationally ruled. Suppose its minimal ruled model has base B of
genus g>=1. Push L down successively through the point blowdowns and
write its ruling degree as `a>0`. At each blowup, the multiplicity
`m_i` satisfies `0<=m_i<=a`: intermediate polarizations are nef, and
the actual positive fiber cycle through the center has total L-degree
a. This holds at infinitely near centers as in the independently
checked [quartic ruled proof](2026-10-09-session-nonrational-normalization-independent-audit.md).

The same elimination of the ruled-section coefficient gives

    5=(2g-2)a^2+(7-2pi)a+sum_i m_i(a-m_i).          (1)

The smooth P1 strict transform `c#` maps constantly to B, hence is
one fiber component. Nefness and the positive component multiplicities
give `4=L.c#<=a`. For pi<=2, (1) instead gives `a<=1`, impossible.
For pi=3, it gives `4<=a<=5` and forces g=1.

If a=4, the final sum must be one. But the possible summands for
integer `0<=m_i<=4` are `0,3,4`, so this is impossible. If a=5,
the sum is zero and every m_i is zero or five. Initially a ruling
fiber has degree five. After each blowup, its strict components lose
an integer multiple of m_i and the new exceptional component has
degree m_i. Inductively the L-degree of every fiber component is
divisible by five. This contradicts `L.c#=4` and finishes the proof.

At pi=4 or five, K_M.L is positive and this proof supplies no
rationality theorem. Do not transfer the quartic rationality conclusion
to these strata.

## 3. The entire sectional-genus-zero lane is excluded

The characteristic-zero vanishing and minimal-degree argument used in
the [quartic genus-zero proof](2026-10-09-session-normalization-sectional-genus-zero.md)
applies with degree five. Namely `K_M.L=-7`,
`chi(K_M+L)=chi(O_M)-1`, and negative nef degree plus vanishing give
`chi(O_M)=1`, `p_g=0`, and `h1(O_M)=0`. Restriction to the general
P1 of degree five gives `h0(S,H)=7`. The complete map is finite
birational onto an integral minimal-degree surface of degree five
in P6. The classification leaves

    S(2,3), S(1,4), S(0,5).

The first two are smooth rational scrolls and are excluded by
`c_num^2=16/5`. On the cone S(0,5), resolve by F5 with negative
section E and `L=E+5f`. Any nonexceptional integral curve of
H-degree four would have strict-transform class `aE+4f`.
Its ruling degree a is a nonnegative integer. If a=0, an integral
vertical curve is a single ruling, of degree one, not four. If a>=1,
its intersection with E is `4-5a<0`, forcing E as a component,
contrary to being a strict transform. Thus the cone cannot even
contain this lifted degree-four curve.

This proves the pi=0 quintic-carrier exclusion in every mate degree.

## 4. A canonical-index filter independent of rationality

If S is Gorenstein, K_S is Cartier and

    K_S.c=(4/5)K_S.H=(4/5)(2pi-7)

must be an integer. Consequently `pi=1` or six. For a nonnormal
quintic this leaves only pi=1. If S is Q-Gorenstein and `rK_S`
is Cartier globally, the corresponding necessary condition is

    5 | r(2pi-7).

Thus pi=0,2,3,4,5 require `5|r`; a non-Q-Gorenstein normalization
remains a separate stratum. A rational singularity alone does not
give a Cartier canonical class.

Normal quintic hypersurfaces are Gorenstein and have pi=6. Nothing
in this filter excludes them.

## 5. Every pi=1 normalization under a mate has exactly one A4 point

By section 2 M is rational. The adjoint proof in the
[degree-four del Pezzo reduction](2026-10-09-session-genus-one-delpezzo-reduction.md)
now applies with `L^2=5`: `K_M.L=-5`, and vanishing and
Riemann--Roch give one effective divisor `A~K_M+L` with `L.A=0`.
Every component is sigma-exceptional. Minimality and prime adjunction
give `K_M.E>=0` on each exceptional prime. Hence
`A.E>=0`, so negative definiteness forces A=0. Therefore

    K_M=-L, K_M^2=5,
    S is a Gorenstein ADE del Pezzo surface of degree five.

The chosen-canonical-form proof of crepancy is unchanged. Its imported
surface input is [Reid's Du Val characterization](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf),
Theorem 2.1(2). The anticanonical orthogonal lattice is A4 and the
complete anticanonical model embeds in P5; the standard weak del Pezzo
lattice and embedding results are in
[Dolgachev, Chapter 8](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1467/2025/10/CAG-2.pdf),
sections 8.2 and 8.3, particularly Theorem 8.3.2(iii).

Write the Mumford correction as `c#+Z=(4/5)L`. Adjunction on the
smooth rational strict transform gives

    c#^2=2, -Z^2=6/5.                                (2)

The exceptional roots form a subsystem of A4. In the realization
`{e_i-e_j:1<=i!=j<=5}`, components are blocks of coordinate indices
and have type A_(block size-1). Any proper subsystem therefore has
Cartan determinant with no factor five. Its inverse matrix cannot
produce the denominator five in (2). The exceptional configuration
must be the full single A4 chain; there are no additional singular
points of S.

The smooth passage lemma gives one transverse contact with one prime
in this chain. The inverse Cartan diagonal is
`4/5,6/5,6/5,4/5`, so the contact is with the second or third vertex.
For the second vertex, `5Z=(3,6,4,2)`; the third is the reversal.
Numerical equivalence is linear equivalence on the smooth rational M,
and pushing the resulting section down gives the actual relation

    5c ~ 4H, Q in H0(S,4H), div_S(Q)=5c.             (3)

Every normalized mate is a scalar multiple of `Q^k`, with b=4k.
The section Q need not belong to the four-coordinate ambient section
ring. Equation (3) does not supply an ambient quartic carrier.

## 6. A unique tangent line fixes the restriction and projection geometry

We have `h0(S,H)=6` and `h0(c,H|c)=5`; restriction has a nonzero
kernel. Every kernel section has actual divisor `c+ell`, since the
residual effective Weil divisor has H-degree one. It has precisely
one integral component ell with multiplicity one. In the complete
anticanonical embedding, ell is a projective line, hence smooth P1.

Its strict transform is smooth, has `L.ell#=1`, and satisfies
`ell#^2=-1` by adjunction. Numerical degree gives
`ell_num=(1/5)L`, hence its correction has square `-6/5`; it too
passes through an interior A4 vertex. If two distinct such lines
existed, their numerical intersection would be 1/5, whereas the
cross correction for either pair of interior vertices is at least
4/5. Their strict-transform intersection would be negative, which
is impossible for distinct effective curves on a smooth surface.
The line ell is therefore unique.

Every kernel section has the same actual divisor c+ell; the ratio
is a global unit on the proper normal integral S, thus a scalar.
The restriction kernel is exactly one-dimensional and restriction
onto H0(P1,O(4)) is surjective. Consequently c is the full rational
normal quartic in its span P4 inside P5.

The two curves use opposite interior A4 vertices: using the same
vertex would make their strict intersection `4/5-6/5<0`.
For opposite vertices it is `4/5-4/5=0`. Thus c and ell meet only
at the A4 point. The Cartier anticanonical divisor c+ell has
arithmetic genus one, while both components have genus zero, so
their scheme intersection has length two. The line ell is the
tangent line to this rational normal quartic at the A4 point.

Also `5ell~H`, obtained by subtracting (3) from `5(c+ell)~5H`.
If h is the unique section with divisor c+ell and u the section
with divisor 5ell, then

    Q = h^5/u

is a regular section of 4H, with divisor 5c. This identity is
intrinsic; h and u need not descend to the chosen P3 projection.

The original four coordinates constitute a four-dimensional subspace
V of H0(S,H). They define projection from a line in P5 disjoint
from S. Their restriction to c is injective because C0 is not
planar. Hence the projection line meets the hyperplane span of c
in its prescribed rational-quartic projection center, the point
corresponding to the omitted binary quartic s^2t^2 after fixing
the C0 parametrization. Choosing lifts of these four sections
leaves four coefficients in the one-dimensional restriction kernel.
This is a concrete small projection target, with finiteness,
birationality, center avoidance and conductor descent still required.

## 7. The actual conductor has degree five, not a line

In this pi=1 lane finite duality and `omega_X=O_X(H)` give

    I=Hom_X(nu_*O_S,O_X)=nu_*O_S(-2H).

Thus the upstairs actual conductor D is Cartier in |2H|,
with `H.D=10` and `p_a(D)=6`. The downstairs conductor Gamma
is a pure Cohen--Macaulay curve. Computing the difference of the
quintic hypersurface and del Pezzo Hilbert polynomials gives

    P_Gamma(m)=5m-1, deg Gamma=5, p_a(Gamma)=2,
    nu_*O_S/O_X = omega_Gamma(-H), polynomial 5m-4.

These statements concern the entire conductor ideal. They do not
assert that Gamma is reduced, smooth or Gorenstein, or that
`D->Gamma` is everywhere flat. No quartic conductor-line theorem
has been transferred. The next geometric task is whether any of
these four-parameter projections can make a power `Q^k` descend
through its entire conductor; k remains unbounded.

## 8. Continuation boundary and first numerical target

The next fixed-C0 quintic lanes are:

* pi=1: the degree-five A4 del Pezzo target above, with its actual
  projection and full conductor power descent.
* pi=2,3: rational normalization, necessarily either non-Q-Gorenstein
  or with global canonical index divisible by five under a mate.
* pi=4,5: neither rationality nor a complete model classification
  has been proved here; retain the same canonical-index distinction.
* pi=6: normal Gorenstein quintic hypersurfaces, not covered by the
  quartic anticanonical exceptional-divisor classification.

The smallest mate degree after the complete quartic exclusion is
b=8, giving transverse multiplicity ten. The separate
[multiplicity-ten filtration audit](2026-10-11-session-multiplicity-ten-filtration-audit.md)
has 308 necessary degree profiles, not 308 realized structures or a
global parameter exhaustion. Nonregular first-normal ratios, higher
jets and genuine closed-point defect divisors must survive any
subsequent reduction. First-normal rank conditions alone cannot
exclude the quintic lane or the unrestricted STCI question.
