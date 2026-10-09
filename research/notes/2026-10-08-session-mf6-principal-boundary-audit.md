# Principal e=1,d2=1: complete frame complements and carrier boundaries

Date: 2026-10-08. Fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, over an algebraically closed characteristic-zero
field. This note complements the
[independent open-chart rank proof](2026-10-08-session-mf6-principal-rank-open-independent-audit.md).
It uses actual complete quartic spaces at every exceptional frame, rather
than specializing a generic nullspace basis. No canonical records were
edited. The unrestricted C0 and universal STCI problems remain open.

**PROVED, conditional on the accepted ancestor reduction and P-037:**
every principal e=1,d2=1 common quartic ancestor is excluded. The open
chart has exactly one quartic at every point; the complete complement
has exactly one quartic except at one point, where every quartic is a
fixed cubic times a linear form. These two alternatives exclude a common
quartic ancestor by proportionality and by division to a forbidden
degree-one ancestor, respectively. This ancestor conclusion does not
assert that every quartic carrier has no higher-degree STCI mate.

**PROVED carrier exclusions on the complement:** the three b0=0
carriers are normal and hence excluded by the repository's accepted
all-normal-quartic theorem. The rational S=0 carrier and the two
infinity-defect carriers are integral quartics singular along smooth
twisted cubics and hence excluded by the accepted all-degree
twisted-cubic theorem. The node fiber consists of reducible quartics
and is excluded in every mate degree. The remaining complement carrier
at (p,r)=(8,1/2) is integral and nonnormal; its actual conductor/mate
obstruction remains open at the time this note was written.

## 1. Direction curve and complete chart coverage

On the principal locus a0*b1!=0 and b0!=0, quotient scaling and the
actual torus give

    A=1+r*z, B=1+p*z, p!=0, p-r!=0.

The condition p-r!=0 is the basepoint-free determinant, not a removable
computational frame restriction. The degree-six invariant direction
equation is

    H=8p^3-(64r^2+128r+16)p^2
      +(96r^4+512r^3+592r^2+128r+6)p
      -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9).

Its geometrically integral genus-one normalization and explicit
Weierstrass model `YE^2=XE^3+96XE-448` are checked in the
[curve source](../computations/verify_mf6_e1_d1_principal_curve_2026_10_08.py)
and the [checkpoint](2026-10-08-session-checkpoint.md). The corrected
fiber is H(p,-1/2)=8p(p+2)^2.

Set

    P=2p+12r^2+16r+9,
    Q=8p+12r^2+4r+3,
    T=2p-4r^2-4r-1,
    S=p-2r-1.

The quadratic cocycle coefficients are c1=-pP/8,
c2=-(2r+1)Q/8 and c3=-(2p+36r^2+16r+3)/4, with
H=64(c1*c3-c2^2). On pP!=0 the unique killing section and the finite
correction are

    delta=(2r+1)Q-pP*z,
    Gamma=nonnegative Laurent part of delta*h2.

The exact identity Res_z(delta,Gamma)=p^4*P^4/8 proves flatness at its
finite zero. Delta has nonzero leading coefficient, so it has no
infinity zero. The independent contact frame is valid on
pP(p-r)(2r-1)T!=0. Its rank is six everywhere, including the retained
S=0 rational point; S was never assumed to be a unit.

The complement is exhausted as follows.

- p=0 is outside the principal locus; p-r=0 violates basepoint freeness.
- At r=1/2, H=8(p-8)(p-2)^2, giving exactly p=2 and p=8.
- At T=0, H=-9(2r-1)^2(2r+1)^4. The r=1/2 point is p=2
  and is already included. The other possibilities are p=0 or the
  primitive point (p,r)=(-2,-1/2).
- On P=0, H=-9(2r+1)^2*Q^2. The nonprimitive possibilities are
  p=2r+1 with 12r^2+20r+11=0. They have c1=c2=0,c3!=0,
  and require the actual alternative section delta=1, whose zero is
  infinity. The primitive point (-2,-1/2) has zero quadratic cocycle;
  the accepted uniqueness argument H0(O(-3))=0 makes a genuine
  degree-one defect nonflat there. It is not a missing flat triple.
- On S=0,
  H=-(2r-1)^2(2r+1)(6r+1)(12r^2+20r+11). The only additional
  valid point is (p,r)=(2/3,-1/6); the quadratic points belong to P=0,
  and the other points were already included or excluded above.
- On the projective b0=0 chart, a1!=0 follows from H and p!=0.
  Normalizing a0=a1=1 gives A=1+z,B=pz and
  p^3-8p^2+12p-72=0. This polynomial is irreducible over Q and has
  nonzero discriminant -160704. One exact cubic-field calculation
  therefore covers all three distinct geometric conjugates. Its roots
  are nonzero and the determinant p is nonzero.

This is a full chart-complement argument. It makes no assertion about
other e, other defect degrees, or directions with a0*b1=0; the latter
defect-one endpoint directions were treated separately in the
[endpoint proof](2026-10-07-session-mf6-e1-d1-endpoints.md).

## 2. Fresh ambient quartic spaces

The [boundary verifier](../computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08.py)
rebuilds all 35 degree-four monomials. It imposes restriction to C0,
vanishing of the first quotient-normal coefficient, and the actual
quadratic-contact equation delta*Qquad-Gamma*h=0. It computes over Q,
Q(sqrt(-2)), or the irreducible cubic field. No generic seven-column
kernel is evaluated at a bad point.

| Fiber | Number of geometric points | Full 35-column rank | Quartic space |
|---|---:|---:|---|
| (p,r)=(2,1/2) | 1 | 31 | Cstar times all four linear forms |
| (p,r)=(8,1/2) | 1 | 34 | one quartic |
| (p,r)=(2/3,-1/6) | 1 | 34 | one quartic |
| p=2r+1, 12r^2+20r+11=0 | 2 | 34 | one quartic at each conjugate |
| b0=0, p^3-8p^2+12p-72=0 | 3 | 34 | one quartic at each conjugate |

All literal quartics are preserved in the three hash-bearing JSON
records adjacent to the source, with suffixes `_rational`, `_quadratic`
and `_infinity`. The fixed cubic is

    Cstar=x0^2*x2-x0^2*x3+x0*x1*x2-x0*x1*x3
      -2*x0*x2^2+x0*x2*x3+x0*x3^2-x1^3+x1^2*x2+2*x1^2*x3
      -x1*x2^2-x1*x2*x3-x1*x3^2+x2^3.

The displayed complete basis is Cstar times
`x0,x1,x0+x1/2+x2/2,x3`, so it is the entire linear system
Cstar*H0(O_P3(1)). For a carrier F=Cstar*L, every positive-degree
mate intersects the plane L=0 in a curve or contains the plane; its
support cannot be solely C0. For a common quartic ancestor, dividing
F and G by Cstar gives a common degree-one ancestor, forbidden by
accepted P-037. At every other fiber, F and G are proportional;
they cannot produce the two independent fixed local-cohomology targets.

## 3. The infinity-defect frame is flat

For the quadratic roots write a^2=-2 and

    r=(-5+2a)/6, p=2r+1, c3=-4/3+10a/3.

The finite correction is
Gamma=(-5-a)z/9+(-2+5a)/9 and delta=1. Flatness cannot be inferred
from an affine resultant with constant delta, so the actual second
chart was rebuilt:

    x3=1, x2=w, x1=w^3+2U, x0=w^4+V/2+3wU,
    A_inf=r+w, B_inf=p+w,
    Bezout=(-1/(p-r),1/(p-r)), delta_inf=w.

The unique quartic has

    h_inf=-w^3*(w-1)^3*(w^2+w-1/3+a/3),
    Gamma_inf=3w^2+(-6+3a)w+4/3-10a/3.

This is obtained by exact polynomial division
Gamma_inf=delta_inf*Qquad_inf/h_inf, with zero remainder.
Its constant is -c3, of norm 24, and is nonzero at both geometric
roots. Thus the infinity defect is genuinely flat. The
[literal-form two-chart verifier](../computations/verify_mf6_e1_d1_principal_boundary_residues_2026_10_08.py)
checks the full actual-frame calculation.

## 4. Geometry and mate scope of the unique boundary carriers

The [self-contained M2 certificate](../computations/verify_mf6_e1_d1_principal_boundary_geometry_2026_10_08.m2)
contains the literal quartics, number-field equations and explicit
curve ideals. It checks the following exact facts.

The b0=0 quartic has a Jacobian cone of dimension one. Thus its
projective singular locus is finite, after every extension of the
constant field. A reducible or nonreduced projective hypersurface
would have a positive-dimensional singular locus. The surface is
therefore geometrically integral, and the hypersurface Cohen–Macaulay
property plus regularity in codimension one makes it normal. The
[accepted normal-carrier theorem](2026-10-06-session-normal-carrier-progress.md)
excludes all three carriers in every mate degree.

The S=0 rational quartic and both infinity-defect quartics have Jacobian
cones of dimension two and degree three. The certificate supplies an
ideal Tc of three quadratic generators, with dimension two, degree
three and a free resolution of length two. It verifies that the
projective curve Tc is geometrically smooth and that all derivatives
of F vanish on it. This is a nondegenerate ACM smooth degree-three
curve, hence a smooth twisted cubic.

These quartics are geometrically integral. Their singular scheme has
degree three and already contains the twisted cubic of degree three,
so it has no other curve component. A nonreduced surface would have
a surface component in its singular locus. A reducible quartic has a
factor partition of degrees (1,3) or (2,2); the factor intersection is
a complete-intersection curve of degree three or four, supported in
the singular locus. The degree-three alternative is planar and
cannot be supported on a twisted cubic. The degree-four alternative
cannot have sole reduced support of degree three, because its generic
multiplicity there would have to be an integer. This proves
integrality, including over an algebraic closure. The
[accepted applicability proof](2026-10-08-session-scroll-conductor-applicability.md)
and [adversarial audit](2026-10-08-session-scroll-conductor-adversarial.md)
then exclude every mate degree.

At (p,r)=(8,1/2), the Jacobian cone has dimension two and degree five.
Its reduced curve support consists of the two rational lines

    L1=(x1-4*x2,x0-16*x3),
    L2=(x1-12*x2-16*x3,x0+32*x2+48*x3).

Equivalently it is the plane conic

    x0+4*x1-16*x2-16*x3=0,
    (x1-4*x2)*(x1-12*x2-16*x3)=0.

Their intersection [16:-8:-2:1] is C0 at z=-1/2; L1 also meets
C0 at z=1/2. This reduced support is not the actual conductor scheme.
No reduced-conductor theorem is transferred to it.

This quartic is geometrically integral. A quadratic factor containing
C0 would be its unique quadric q, which the source checks is not a
factor. For a plane*cubic factorization, the cubic contains C0 and
the plane's restriction to C0 divides
h=(2z-1)^3*(2z+1)^5. There is no infinity root. A plane restriction
lies in span(1,z,z^3,z^4); among divisors of degree four supported at
z=1/2,-1/2, its missing z^2 coefficient forces multiplicities (1,3)
or (3,1). The only candidate planes are
x0+4x1-16x2-16x3 and x0-4x1+16x2-16x3. The certificate checks that
neither divides F. Every reducible degree-four factorization has a
factor of degree one or two, so this excludes all factorizations over
an algebraic closure. Its conductor and all-mate exclusion were passed
to the degenerate-scroll-conductor lane as an explicit remaining target.

## 5. Cubic residue bounds and continuation

The residue verifier uses S=h/delta and T=Gamma*E-delta*K in the
actual local expansion h*m+Qquad*y^2+E*m*y+K*y^3. The normalized
cubic residue is T/S up to sign. Its finite pole divisor and its
infinity pole order are checked in both actual charts.

| Carrier | Finite excess | Infinity excess | Necessary degree D3 |
|---|---:|---:|---:|
| p=8,r=1/2 | 2 | 0 | at least 3 |
| p=2/3,r=-1/6 | 1 | 3 | at least 5 |
| two infinity-defect roots | 3 | 1 | at least 5 |

The last two rows cannot realize MF6 type (d2,d3)=(1,3), but the
all-degree carrier exclusions above use the stronger geometric
theorems. The p8 row meets the MF6 cubic budget exactly; the cubic
bound does not remove it. A generic quartic or a higher-degree mate
on the remaining elliptic direction curve remains a distinct problem
from the now-complete principal common-ancestor incidence.

Saved source-byte outputs are adjacent to the three verifiers. The
boundary Python source is frozen for independent isolated replay.
The exact M2 and residue verifiers both passed with their literal
forms. A derivation attempt using `radical` directly over a number
field failed because M2 supplied no applicable strategy; the final
certificate instead verifies explicit twisted-cubic ideals. Two M2
API corrections (`isCM` and resolution of a quotient ring) were
replaced by the checked length-two resolution of `coker gens Tc`.
These execution repairs changed no mathematical assertion.

## 6. A structural finite reduction for principal STCI carriers

There is a further consequence that does not require computing a large
Jacobian elimination ideal. Let U be the valid flat principal direction
curve with the fixed-cubic node removed. The zero-cocycle primitive
point and the determinant/nonprincipal loci are already outside U.
The independent open-chart proof and the complete complementary ranks
show that the quartic contact kernel has constant dimension one on U.

The unique defect line and correction are intrinsic. Their local
algebraic formulas on the finite and infinity charts glue because the
correction is unique (H0(O(-3))=0). Thus the actual contact matrices
define a kernel line bundle on U and a regular morphism

    U -> P(H0(P3,O(4))).

Equivalently this can be constructed on the genus-one normalization;
the finitely many deleted or singular direction points have already
been treated separately. The universal projective Jacobian locus of
this quartic family is closed in U times P3, and its projection to U
is proper. Upper semicontinuity of fiber dimension makes

    {u in U : the quartic has a positive-dimensional singular locus}

a closed subset of U. It is proper: all three b0=0 fibers have finite
singular loci. Since U is an integral curve of finite type, this subset
is finite. Outside it, every quartic is geometrically integral and
normal by the argument of section 4, and the accepted normal-carrier
theorem excludes every mate.

**PROVED finite reduction, not an exception-list computation:** only
finitely many nonnormal quartics in the principal defect-one family
can remain STCI carriers. The exact finite nonnormal parameter ideal
has not been computed in this note. The rational S=0 point and the two
infinity-defect points belong to that finite set and are already
excluded by the twisted-cubic theorem. The p8,rhalf point is another
member and has been assigned an explicit nonreduced-conductor proof.
Further nonnormal points on the independent contact open remain to
be identified or excluded structurally. Neither finiteness nor the
complete common-ancestor conclusion is presented as a universal STCI
theorem.
