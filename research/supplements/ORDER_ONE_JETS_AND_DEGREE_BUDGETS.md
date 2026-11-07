# Order-one normal directions, divisor bounds and higher-jet tests

These are necessary restrictions on an actual supported complete intersection with generically curvilinear algebra. The full saturated Frobenius-pairing proof is owned by [Curvilinear genus and defects](CURVILINEAR_GENUS_AND_DEFECTS.md#2-direct-proof-of-the-saturated-duality-and-effective-defects); it applies to arbitrary multiplicity and retains every support point. This owner separates its degree arithmetic and early-divisor bounds from the later ambient Hankel/annihilator tests. The abstract saturated flag is not a global homogeneous realization.

For the fixed embedding C0, the historical quartic-mate cases below are closed by R-0001; that theorem is not a statement about every embedding of a smooth rational quartic. Their local controls, finite divisor profiles and exact ambient obstruction polynomials remain useful mathematical statements; old descriptions of them as the current quartic-mate frontier have no force.

<a id="2026-10-06-uniform-order-one-frontier"></a>
<a id="2026-10-06-session-uniform-audit"></a>

Let C be a smooth nondegenerate rational quartic over an algebraically
closed field of characteristic zero. Suppose a homogeneous pair (F_a,G_b)
has reduced projective support C, with at least one equation of generic
normal order one along C. We may take a,b>=4: a quadric carrier is excluded
by the ruling-class argument, and cubic carriers of arbitrary mate degree
are excluded by Craighero--Gattazzo. This note does not cover pairs whose
two equations have generic normal order at least two.

The transverse algebra is curvilinear at the generic point, so the
complete-intersection multiple structure is quasiprimitive. Write its
generic multiplicity and saturated BF pieces as

    m=ab/4,  E_i=L^i(D_i),  D_0=D_1=0,  0<=i<m.

The finite-flat local Gorenstein pairing audit in
[the actual saturated-pairing proof](CURVILINEAR_GENUS_AND_DEFECTS.md#2-direct-proof-of-the-saturated-duality-and-effective-defects) applies at every multiplicity. Thus
the multiplication divisors satisfy

    D_i+D_j <= D_(i+j),
    D_i+D_(m-1-i)=D_(m-1).

The first line-bundle quotient is

    O_P1(-7)^2 -> L=O_P1(e-7),  e>=0,

and the two homogeneous binary sections giving it have degree e and no
common zero. Adjunction and the top BF piece give

    E_(m-1)=omega_C tensor (omega_X|C)^(-1)
           =O_P1(14-4(a+b)).

Set c=7-e and s=m-1. Then

    deg D_s = c s + 14 - 4(a+b).                       (U1)

Since a+b>=8, the last constant is at most -18. Effectivity in (U1)
therefore forces c>0, proving the uniform bound

    0 <= e <= 6.                                     (U2)

This applies for arbitrarily large a,b in the order-one branch. Increasing
the equation degrees cannot make the primitive first quotient direction
have unbounded degree.

For the second defect, write s=2q+r, 0<=r<=1. Since s>=3, q>=1.
Repeated multiplication and effectivity imply q D_2<=D_s, so

    q deg D_2 <= 2cq + cr + 14 - 4(a+b) < 2cq.

The strict inequality follows from cr<=7 and 14-4(a+b)<=-18.
The same argument with s=3q+r, 0<=r<=2, gives

    q deg D_3 <= 3cq + cr + 14 - 4(a+b) < 3cq,

because cr<=14. Hence the following bounds are uniform over both carrier
degrees and multiplicity:

| e | Upper bound on deg D2 | Upper bound on deg D3 |
| --- | ---: | ---: |
| 0 | 13 | 20 |
| 1 | 11 | 17 |
| 2 | 9 | 14 |
| 3 | 7 | 11 |
| 4 | 5 | 8 |
| 5 | 3 | 5 |
| 6 | 1 | 2 |

At e=0, deg D2=0 would produce an embedded primitive triple of type
O(-7), excluded by P-010 for every characteristic-zero smooth rational
quartic. Thus deg D2>=1 in that row. The stronger degree-one/two exclusion
under investigation for a quartic carrier must not be applied to arbitrary
carrier degree.

## Additional lower bound for the order-one carrier

Suppose F_a is the equation whose generic normal order is one, and set
S=V(F_a). It is integral: any irreducible factor of a defining equation
must contain C, by intersecting with the mate, so more than one factor
would give normal order at least two. It is regular at the generic point
of C. Its torsion-free conormal along C is L, hence

    deg N_(C/S)=7-e.

On the normalization the unique lift C^nu of C is smooth and isomorphic
to C. The mate's pullback Cartier divisor is m C^nu, with m=ab/4;
finiteness of normalization creates no additional curve supported over
a closed point. Thus its numerical pullback satisfies

    (C^nu)^# == (4/a)H,  ((C^nu)^#)^2=16/a.

The audited numerical-normal-sheaf inequality in
[the numerical surface-pullback proof](../synthesis/numerical_surface_pullback.md) applies even if S is nonnormal at
finitely many points of C. It gives

    16/a <= 7-e,
    a >= ceil(16/(7-e)).                             (U4)

Combined with a>=4, the order-one carrier's necessary lower degree for
e=0,...,6 is respectively 4,4,4,4,6,8,16. This bound is on the degree
of the generically regular carrier; if the mate is thick along C it does
not transfer to that mate. The finite-order defect bounds above are
independently audited; this additional geometric deduction is recorded
with its explicit reliance on the proved normal-sheaf inequality.

## Companion bound for local-cohomology ancestors

For the fixed C0 let u,v be the recorded first-socle targets of degree -3.
If equal-degree homogeneous multipliers F_d,G_d and an ancestor alpha obey
F_d alpha=u, G_d alpha=v, then alpha has degree -(d+3). Suppose at least
one multiplier has nonzero first conormal symbol and alpha has top
principal-part order n>=3. Its top quotient is

    O_P1(7n-4d-5) tensor Sym^(n-1)(k^2).

Contraction by the nonzero linear symbol kills that top section. In
characteristic zero it is a pure (n-1)-st power in the perpendicular
primitive degree-e direction, multiplied by a nonzero binary section.
Consequently

    7n-4d-5-(n-1)e >= 0,
    (7-e)(n-1) >= 4d-2.                              (U3)

For d>=1 this again forces e<=6. If d>=4, the quotient of order two has
no global sections, so n>=3 is automatic for a nonzero ancestor. Coprimality
and the fixed-degree principal-part bound provide a finite maximum n for
each d, but do not bound d. If both multiplier first symbols vanish, the
linear contraction argument does not apply and no e-bound is asserted.


## 3. A uniform degree strengthening beyond the retained bounds

Assume a,b>=4, generic normal order one for at least one equation, and
N*=O(-7)^2. The conormal epimorphism onto L has

    L=O(e-7),     e>=0,     c=7-e,     m=ab/4, s=m-1.

Here ab must be divisible by 4. Adjunction gives

    deg D_s = c*(ab/4-1)+14-4(a+b).                   (1)

Effectivity first gives c>0, hence e<=6. Multiplying (1) by 4c and
completing the product gives the stronger necessary degree condition

    (c*a-16)(c*b-16) >= 256-56*c+4*c^2.               (2)

This is equivalent to top-defect effectivity, rather than an additional
geometric hypothesis. It displays degree restrictions missed by listing
only e<=6 or 16/a<=c. For the four highest direction degrees it becomes

| e | Exact necessary inequality | Each defining degree must be at least |
|---|---|---:|
| 3 | (a-4)(b-4)>=6 | 5 |
| 4 | (3a-16)(3b-16)>=124 | 6 |
| 5 | (a-8)(b-8)>=40 | 9 |
| 6 | (a-16)(b-16)>=204 | 17 |

For e=3 both factors are nonnegative because a,b>=4, and the right
side is positive. For e=4, if both factors were negative their product
would be at most 16; for e=5 the corresponding bound is 64 after
multiplying by four; for e=6 it is 144. Each is smaller than the
required right side. A mixed-sign product is also impossible, so both
factors must be strictly positive. This proves both degree lower bounds,
including for a mate that may be thick generically. It does not transfer
the geometric normal-sheaf inequality to a thick mate.

For completeness, (2) has right sides 60,64,76 for c=7,6,5
(e=0,1,2). None is negative. The exact constraints for e=1,2 are
(6a-16)(6b-16)>=64 and (5a-16)(5b-16)>=76.
At e=2,a=4 the latter is precisely b>=7. These conditions give no
upper bound on either degree and do not exclude the high-degree
order-one branch.

## 4. Why the primitive factorization stops at its stated hypotheses

For a quartic carrier m=b and the top formula is

    deg D_(b-1)=(3-e)*b+e-9.

At e=2 this is b-7. For b=7 the entire defect divisor vanishes.
For b=8, superadditivity forces D2=D3=0 because twice either one
is bounded by a divisor of degree one. The canonical primitive fourth
then exists, so its quotient lies on the audited fourth-obstruction
zero locus. On that locus the defining quartic lies in

    H0(I_(C3)(4))=T*H0(O_(P3)(1)).

Its nonzero plane factor forces an extra curve when intersected with
any mate, proving the two exclusions. The same argument works at
any larger b when D2=D3=0. It does not force these equalities once
b-7 permits nonzero early defects. The existing parity theorem does
give an all-b exclusion on its explicit parity quotient family with
D2=0, but it does not cover every quadratic quotient or D2=1.

## 5. Exact local CI controls against a numerical overclaim

Let R=k[[t]] and take integers r,h>=2. The local algebra

    B_(r,h)=R[x,y]/(t*x-y^r, x^h)

is finite free with basis x^i*y^j, 0<=i<h, 0<=j<r. One can see
this by first taking R[x]/(x^h) and adjoining the monic relation
y^r-t*x. It is a complete intersection supported on (x,y).
After inverting t it is K[y]/(y^(r*h)) with x=t^(-1)y^r.
Writing k=r*i+j shows that the saturated layer E_k has generator
t^(-i)y^k, whereas the image of E1^k has generator y^k. Hence

    d_k=ord_t D_k=floor(k/r),       0<=k<r*h.         (3)

This formula satisfies superadditivity and complement duality exactly:

    floor(i/r)+floor((r*h-1-i)/r)=h-1.

Two controls are directly compatible with the e=2 top degree:

| b=r*h | Local equations | (d2,d3,d_(b-1)) |
|---:|---|---|
| 9 | t*x-y^3, x^3 | (0,1,2) |
| 12 | t*x-y^2, x^6 | (1,1,5) |

In each case d_(b-1)=b-7 and the uniform early bounds are satisfied.
Thus even finite-flat, two-normal-generator, local CI and Gorenstein
duality do not extend the primitive exclusion to every b. These are
local numerical controls, not projectively embedded multiple curves
on C0 and not STCI counterexamples or constructions. They establish
the insufficiency of the proposed numerical inference.

## 6. A sharper small-degree surviving frontier

For e=2, repeated multiplication gives

    deg D2 <= floor((b-7)/floor((b-1)/2)),
    deg D3 <= floor((b-7)/floor((b-1)/3)).              (4)

In particular b=9,10,11 have D2=0 and deg D3<=1. A survivor must
have deg D3=1; otherwise the primitive factorization applies. Write
D3=p. At p, superadditivity and complement duality force every
top defect to lie at p:

* b=9: D3+D5=D8 and D5>=D3, so the top degree two is spent at p.
* b=10: 3D3<=D9, so the top degree three is spent at p.
* b=11: 3D3<=D9=D10. Moreover D10=2D5, so its coefficient
  at each point is even. Its coefficient at p is therefore at least
  four, exhausting the total degree four.

Consequently the complete divisor sequence is an integer profile
d_i*p. Exhausting the finitely many integers allowed by (BF) gives

| b | Complete permissible profiles (d0,...,d_(b-1)) |
|---:|---|
| 9 | (0,0,0,1,1,1,2,2,2) |
| 10 | (0,0,0,1,1,2,2,3,3,3) |
| 11 | (0,0,0,1,1,2,3,3,4,4,4); (0,0,0,1,2,2,2,3,4,4,4) |

The companion `verify_session_uniform_bf_profiles.py` independently
enumerates every complementary profile, imposes effectivity,
monotonicity (the i=1 multiplication case), all superadditivity
inequalities, and d2=0,d3=1. It checks exactly these lists.
The b=9 profile has the genuine local CI control above. The other
profiles remain necessary numerical possibilities; the verifier does
not assert their embedded or local nonmonomial existence.

## 7. Intrinsic fourth-layer annihilation for fixed C0

The universal moving-coordinate generator and exact P16/Delta formulas in this subsection concern the fixed embedded C0, with its stated quotient frames; they are not a universal formula for all smooth rational quartics.

When D2=0 the primitive triple has ideal-generator bundle fitting in

    0 -> L^3 -> V=I_(C3)/(I_C*I_(C3)) -> M -> 0,
    L=O(-5), M=O(-9).

Its class c lies in H1(O(-6)). A fourth layer with
E3=L^3(D3) induces a quotient V->E3 whose restriction to L^3
is the canonical multiplication section. Applying Hom(-,E3) gives
the necessary annihilation

    c maps to zero in H1(O(-6+D3)).                   (5)

If c is represented by coefficients c1,...,c5 of z^-1,...,z^-5,
a quadratic annihilator exists exactly when

    det [[c1,c2,c3],[c2,c3,c4],[c3,c4,c5]]=0.           (6)

This is multiplication of Laurent cocycles, so it includes the moving
infinity point when sections are treated homogeneously. For b=9..11
the stronger degree-one annihilator is necessary: the four-by-two
matrix with rows (c1,c2),(c2,c3),(c3,c4),(c4,c5) must have nonzero
kernel. The condition is rank at most one, not merely (6).

The session exporter `session_uniform_e2_hankel.py` imports the retained
exact moving-coordinate generator and writes only
`scratch/session_uniform_e2_hankel.json`. It derived c_j with a
single homogeneous-resultant denominator Delta; the Hankel determinant
reduces to P16/Delta, with P16 homogeneous of degree sixteen and
1112 monomials. The numerator vanishes to order at least six in
(2a1+b0,2a2+b1). Its parity specialization is

    - (beta+2)^6*(beta^2+8beta+36)
       *(beta^4+8beta^3-24beta^2-256beta-432)/1024.

Division by the specialized Delta=beta^2 gives the actual determinant.
At beta=-6,-2,6 the fourth vectors are respectively
(64,0,-8,0,0), (0,0,0,0,0), and (-128,0,160,0,-192);
the determinants are 512,0,-163840, matching the independent retained
parity certificate. There was no useful general polynomial
factorization, and no universal incidence exclusion was completed.

This export is exact derived data from the established generator,
not an independent audit of that generator. The open primitive-triple
problem combines actual quartic contact, the resultant-open condition,
and (5). For D2=1 a defective-triple gluing state is needed before
using any fourth class. The primitive calculation does not apply there.

The exporter also saves all six exact minors of the four-by-two
degree-one annihilator matrix, with their resultant denominator powers.
Their reduced numerator term counts are 392,412,447,416,412,392.
Thus the sharper b=9..11 necessary condition has a reproducible complete
polynomial specification. No saturation or emptiness certificate for its
intersection with the full ambient quartic-contact incidence is claimed.


## Exact scope of the tests

The local algebras B_(r,h) prove that saturation symmetry and a top divisor do not force early primitivity. The Hankel construction tests the specified primitive triple and the **same** allowable divisor; a nonzero cohomology group or a vanishing determinant is not a full embedded-incidence classification. The [profile verifier](../computations/verify_session_uniform_bf_profiles.py) exhausts the displayed integer profiles. The [Hankel exporter](../computations/session_uniform_e2_hankel.py) supplies the exact necessary polynomial equations and their denominators, not an emptiness certificate. For the complete actual quartic-source proof use [the accepted quartic-pair owner](../synthesis/quartic_pair_obstruction.md), and for arbitrary mate degree the [quartic-carrier theorem](../results/quartic_carrier_exclusion.md).

The saturated local duality is characteristic free. The numerical statements here use their explicit characteristic-zero normal bundle and lower-carrier exclusion hypotheses; these hypotheses must be replaced, rather than suppressed, before transferring a degree table to a prime. The ancestor contraction argument uses the ordinary characteristic-zero symmetric pairing. The separately reviewed [odd-characteristic r>=2 generator arithmetic](NORMAL_FLATNESS_AND_FILTERED_CI.md) concerns another generic initial-algebra class and is not a substitute for this order-one theorem.
