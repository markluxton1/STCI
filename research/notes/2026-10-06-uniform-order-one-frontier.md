# Uniform first-jet and defect bounds beyond fixed carrier degree

Date: 2026-10-06. Status: **PROVED conditional on the checked BF duality
and characteristic-zero rational-quartic normal-bundle inputs**; the
algebraic bounds were independently audited in
`2026-10-06-primitive-quadruple-audit.md`, section 6. This is a necessary finite early-jet reduction, not
an upper bound on either defining degree or total multiplicity.

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
`2026-10-05-mf6-pairing-audit.md` applies at every multiplicity. Thus
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
`2026-10-05-mumford-normal-bound.md` applies even if S is nonnormal at
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

## What this reduction supplies and what remains

The order-one STCI branch can now be organized through finitely many first
direction degrees and bounded early divisor degrees, before allowing either
surface degree to grow. The binary coefficients and divisor positions still
vary in positive-dimensional parameter spaces; this is not a finite list
of curves or a completed classification of embedded triples and quadruples.
Nor does a permitted early structure imply an arbitrarily long Gorenstein
filtration or a global arithmetically Gorenstein thickening.

The entirely thick branch remains separate. Its leading binary tangent
forms do not determine later horizontal multiplicity, and its valid state
must retain higher normal jets, Rees/valuation data, or equivalent information.
The uniform bounds here do not repair the tangent-only recurrence defeated
by y^p+x^(p+r).

This is a direct consequence of the checked normal bundle, saturated BF
duality, and complete-intersection adjunction. No claim of novelty is made.
