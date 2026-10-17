# Structural continuation for the defective e=1 MF6 triples

Date: 2026-10-07. Fixed C0, characteristic zero. Status: **PROVED
NECESSARY REDUCTIONS; REMAINING INCIDENCE OPEN**. This follows the
all-degree primitive-triple exclusion in
[`2026-10-07-session-mf6-e1-independent-audit.md`](2026-10-07-session-mf6-e1-independent-audit.md).
No exclusion of MF6 types `(d2,d3)=(1,3),(2,2)` is claimed here.
The subsequent bounded endpoint work is now proved in
[`2026-10-07-session-mf6-e1-d1-endpoints.md`](2026-10-07-session-mf6-e1-d1-endpoints.md):
all six degree-one endpoint orbits in section 4 admit no mate, for any
mate degree. The principal direction locus and type (2,2) remain open.

## 1. Intrinsic module and the correct twist of the cubic residue

Retain `L=O(-6)`, `M=O(-8)`. At a point of the canonical triple with
positive second defect, choose a DVR R and regular normal parameters
`m,y`. Its ideal has the form

    J=(delta*m-gamma*y^2, m*y, m^2, y^3),

where delta is a local equation of D2 and gamma is a unit at its zeros.
This unit condition is the finite-flatness condition for the embedded
triple. Near such a point y^3 is redundant, since

    gamma*y^3=delta*m*y-y*(delta*m-gamma*y^2).

Writing the first three generators as `g1,g2,g3`, the two syzygies are

    m*g1+gamma*y*g2-delta*g3=0,
    m*g2-y*g3=0.

Their matrix has maximal minors g1,g2,g3 (up to signs), and is the
Hilbert--Burch presentation of this height-two triple ideal. After
restricting to C, it gives

    J/(I_C*J)=R*g1 + R*g2 + (R/(delta))*g3.

The torsion generator is g3. The relation for y^3 becomes
`[y^3]=(delta/gamma)[g2]` in the torsion-free quotient. At a point
where delta is a unit, the primitive presentation gives the same
torsion-free module. Thus the global torsion-free ideal-generator
bundle V fits the exact sequence

    0 -> P=L^3(D2) -> V -> Q=M(-D2) -> 0.             (1)

The quotient is the image of J in the first conormal: its generator has
symbol delta*m, so the image is M(-D2). The subline P contains the
ordinary third power L^3 with zero divisor D2. These identifications
are intrinsic and survive a change of regular normal frame.

In a hypothetical fourth saturated layer, functions in J map into
`E3=L^3(D3)`. Multiplication by I_C sends them into the next step,
so this defines a map `V -> E3`; torsion maps to zero. Its restriction
to P is the canonical section with zero divisor `D3-D2`. Therefore
the extension class

    c in Ext1(Q,P)=H1(L^3*M^-1(2D2))

must be killed by the section of `O(D3-D2)`. For e=1 this is

    c in H1(O(-10+2*d2)),
    c maps to zero in H1(O(-10+d2+d3)).               (2)

This includes the nonprimitive correction to the kernel bundle; using
M rather than M(-D2) would lose one D2 twist and give the wrong matrix.

There is also a direct valuation check. If the generic formal root is
`m=f2*y^2+f3*y^3` and `val(f2)=-a<0`, the exact third-piece lattice
gives

    ord D3=max(a,-a-val(f3)),
    ord(D3-D2)=max(0,-2a-val(f3)).

Hence the normalized cubic residue is delta^2*f3, up to a regular
unit and a regular change of splitting. That is exactly the twist in
(1)--(2), rather than delta*f3 or f3 alone. For the previously accepted
e=0,d2=4,d3=5 branch, (2) becomes
`H1(O(-6)) -> H1(O(-5))`, agreeing with its four-by-two linear
annihilator certificate. This is a consistency check, not the proof of
the new sequence.

## 2. Exact annihilator sizes for the two remaining MF6 types

For `(d2,d3)=(1,3)`, the class c is in H1(O(-8)). Write it as
`sum(c_i*z^-i,i=1,...,7)`. A nonzero quadratic section
`l0+l1*z+l2*z^2` must kill it in H1(O(-6)). Thus the exact necessary
condition is a nonzero kernel for

    [c1 c2 c3]
    [c2 c3 c4]
    [c3 c4 c5].                                     (3)
    [c4 c5 c6]
    [c5 c6 c7]

Equivalently all ten three-by-three minors of this five-by-three
matrix vanish. The coefficients l0,l1,l2 are homogeneous sections of
O(2), so an infinity point or a doubled point is included; no fixed
finite support is assumed. The cubic class must be computed using the
actual defective triple and moving support/frame transition.

For `(d2,d3)=(2,2)`, the map P->E3 is an isomorphism. The class is
already in H1(O(-6)), and the exact necessary condition is simply

    c1=c2=c3=c4=c5=0.                                (4)

A determinant alone would be weaker and inappropriate. Conditions
(3)--(4) are necessary for the fourth layer. Their satisfaction alone
does not establish quartic containment, finite-flat higher layers, a
sextic mate, or STCI.

## 3. The preceding defective-triple incidence is much smaller

For the quotient direction `A=a0+a1*z,B=b0+b1*z`, let c1,c2,c3 be
the three quadratic cocycle coordinates already independently derived:

    c1=-b1*(2*a0*b1+12*a1^2+16*a1*b0+9*b0^2)/8,
    c2=-(2*a1+b0)*(8*a0*b1+12*a1^2+4*a1*b0+3*b0^2)/8,
    c3=-a0*(2*a0*b1+36*a1^2+16*a1*b0+3*b0^2)/4.

Basepoint freedom is `a0*b1-a1*b0!=0`.

When d2=1, a linear defect section `delta0+delta1*z` kills the
quadratic class in H1(O(-3)), so its complete killing matrix is

    [c1 c2]
    [c2 c3].                                        (5)

Away from c=0 it has rank one and a unique projective kernel. The
base direction must satisfy the sextic `c1*c3-c2^2=0`. Setting
`p=a0*b1,t=a1,b=b0`, its numerator after multiplication by 64 is

    8p^3-(64t^2+128tb+16b^2)p^2
    +(96t^4+512t^3b+592t^2b^2+128tb^3+6b^4)p
    -(576t^6+960t^5b+880t^4b^2+544t^3b^3
      +220t^2b^4+60tb^5+9b^6).                     (6)

This is a compact torus-invariant polynomial specification, not an
irreducibility claim or a solved parameter curve. It includes
`a0*b1=0` boundaries, which must not be dropped by the invariant p.

When d2=2, the quadratic defect section has coefficients
`delta0,delta1,delta2`, and the complete quadratic-class killing
condition in H1(O(-2)) is the one linear equation

    delta0*c1+delta1*c2+delta2*c3=0.                  (7)

It has a projective line of possible sections away from c=0. In both
cases the finite and infinity corrections are unique because
`H0(O(-4+d2))=0`. The correction is obtained by splitting
`delta*h2` into its Laurent coboundary pieces. Finite-flatness still
requires delta and the local correction gamma to have no common zero.

In fact the primitive obstruction-zero locus cannot support a genuine
positive D2 of degree at most three. If h2 is already a coboundary,
its unique primitive correction is gamma0. Multiplication by delta
gives a correction delta*gamma0. Because
`H0(O(-4+d2))=0` for `d2<=3`, there is no alternate correction.
At every zero of delta the two coefficients delta and gamma share
that zero, violating triple finite-flatness. Thus the four primitive
direction orbits of the preceding audit can be removed from these
defective incidences. Together with the quartic-specific uniform
bound `d2<=3`, this applies to all mate degrees in the e=1 lane.

## 4. Six complete boundary triples for d2=1

The two boundaries of (6) can be retained as six finite test fibers.

If `a0=0,b1!=0`, basepoint freedom says `a1*b0!=0`. Then c3=0,
so (5) requires c2=0. Removing the primitive c=0 locus, c1!=0 and
the unique defect section is delta=z. Actual torus and quotient
scaling yield the representatives

    A=r*z, B=1+z, delta=z,
    r=-1/2 or 12r^2+4r+3=0.

The two quadratic roots have c1!=0, as does r=-1/2, so these are
genuine distinct boundary directions, not the primitive B=1 fibers.
If `b1=0,a0!=0`, similarly c1=0,c2=0,c3!=0, and the unique
defect section is the homogeneous section whose finite polynomial is
delta=1 (its zero is infinity). The representatives are

    A=1+r*z, B=1, delta=1,
    r=-1/2 or 12r^2+4r+3=0.

At the respective defect points the other coefficient is a unit, so
the boundary triples pass that flatness check. The subsequent endpoint
note reconstructs their complete quartic fibers and proves the six
bounded exclusions. The principal `a0*b1!=0` portion of the sextic
remains unsolved.

## 5. Continuation-ready next calculation

The highest-value next step is the intrinsic class in (2), calculated
on the actual triple incidence (5) or (7), with delta/gamma flatness
and complete ambient quartic containment. For type (2,2), test the
five coefficients directly. For type (1,3), test the actual quadratic
annihilator matrix (3) on the remaining principal direction sextic.
The six boundary fibers above have now been checked and excluded in
the separate endpoint proof.

The companion
[`verify_mf6_e1_defective_structural.py`](../computations/verify_mf6_e1_defective_structural.py)
checks the local syzygies, the normalized third-layer valuation formula,
the killing matrices, the exact sextic and boundary directions, and the
two target twists. It does not compute the universal cubic class or
prove either remaining type empty. The universal STCI question and the
unrestricted char-zero status of C0 remain open.
