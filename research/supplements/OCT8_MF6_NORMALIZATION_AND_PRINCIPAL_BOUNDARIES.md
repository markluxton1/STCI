# October 8 historical mathematical investigations

Full original source text is preserved below, including calculations, qualifications, counterexamples, and unresolved questions. This compilation does not independently audit or promote claims.

---

## Source: 2026-10-08-session-mf6-principal-boundary-audit.md

# Principal e=1,d2=1: complete frame complements and carrier boundaries

Date: 2026-10-08. Fixed curve
`C0=[s^4:s^3t:st^3:t^4]`, over an algebraically closed characteristic-zero
field. This note complements the
[independent open-chart rank proof](#source-2026-10-08-session-mf6-principal-rank-open-independent-auditmd).
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
and the [checkpoint](OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-08-session-checkpointmd). The corrected
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
[endpoint proof](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-d1-endpointsmd).

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
[accepted applicability proof](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-conductor-applicabilitymd)
and [adversarial audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-conductor-adversarialmd)
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


---

## Source: 2026-10-08-session-mf6-principal-rank-open-independent-audit.md

# Principal e=1,d2=1 quartic rank: independent open-chart audit

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]`, characteristic
zero. Status: **PROVED HERE, exact polynomial certificate on the stated
open**. This does not exclude a quartic with a higher-degree mate.
The chart complement is separately owned by the principal-boundary audit.

For the quotient direction `A=1+r z`, `B=1+p z`, write

```
H = 8p^3 -(64r^2+128r+16)p^2
    +(96r^4+512r^3+592r^2+128r+6)p
    -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9),
P = 2p+12r^2+16r+9,
T = 2p-4r^2-4r-1,
S = p-2r-1,
Q = 12r^2+20r+11.
```

The theorem is that the complete vector space of ambient quartic forms
containing the associated genuine triple has dimension exactly one on

```
U = {H=0, p P (p-r) (2r-1) T != 0}.
```

Thus this entire open cannot supply two independent quartic ancestors.
A unique quartic can still serve as one carrier in an STCI pair; that
question is not settled by this calculation.

## 1. Complete ambient first-normal space and the exact frame

The standalone verifier
[`verify_session_mf6_principal_rank_open_2026_10_08.py`](../computations/verify_session_mf6_principal_rank_open_2026_10_08.py)
reconstructs the first and second normal equations from eighteen
independent actual quartic forms. Their coefficient rank is eighteen,
and all vanish on `C0`; the thirty-five quartic monomials restrict to
all seventeen powers `z^0,...,z^16`. Consequently these forms constitute
the entire degree-four ideal space, rather than a sampled subspace.

Using the normal chart

```
x0=1, x1=z, x2=z^3+V, x3=z^4+U+(3/2)zV,
U= -r m/(p-r)+(1+rz)y,
V= -p m/(p-r)+(1+pz)y,
```

the first normal matrix `M1` has shape `11 x 18`. Its columns
`0,1,2,3,4,5,6,11,12,14,15` have determinant

```
p^4(p-r)(2r-1)T^2 / 256.
```

It therefore has rank eleven everywhere on `U`. The seven columns
`N` saved in the reconstruction, after dividing each by its separately
recorded polynomial gcd, lie in `ker(M1)`. The free rows
`7,8,9,10,13,16,17` are diagonal, with diagonal entries

```
-(2r-1)T^2/256,
-(2r-1)T/128,
-(2r-1)T^2/256,
-1/32,
-p(2r-1)T^2/256,
-p^3(2r-1)T^2/256,
-p^4(2r-1)T^2/256.
```

Their determinant is `-p^8(2r-1)^6T^11/2^52`, a unit on `U`.
Thus these seven columns form the complete first-normal kernel in
every fiber of this open, with no generic-only frame assumption.

Let `h2` be the accepted quadratic cocycle,

```
h2 = -(2A+zB)(12A^2+3z^2B^2+4z^2(A'B-AB'))/(8z^5).
```

Its three negative Laurent coefficients satisfy `64(c1c3-c2^2)=H`.
Choose

```
delta = -8c2+8c1z = (2r+1)(8p+12r^2+4r+3)-pPz,
Gamma = polynomial part of delta*h2.
```

The exact identity `Res_z(delta,Gamma)=p^4P^4/8` gives triple flatness
on this chart. If a quartic's first normal coefficient in `m` is `h`
and its quadratic coefficient in `y` is `q2`, the second contact
condition is `delta*q2-Gamma*h=0`. Multiplying by the unit `p-r`
produces the saved complete matrix `M2`.

On `H=0`, the product `M2*N` has its last five rows zero; its seventh
row is a multiple of `H`. Divide the first six rows by
`p-r,p-r,p-r,p-r,p(p-r),p^2(p-r)`, respectively. The resulting
`6 x 7` polynomial matrix is denoted `D`. Every row division is by a
unit on `U`. Its rank is the actual contact rank of the complete
first-normal kernel.

## 2. Factor before reduction; only two residual norms are needed

The independent raw-factor computation retained all seven actual
cofactors, instead of reducing matrix entries modulo `H` before taking
determinants. The latter operation produces degree-fifty expressions,
although it is algebraically correct. For cofactors obtained by omitting
columns six and five, respectively, the exact factorization is

```
M6 = (27/2^51) p^5(2r-1)^4(2r+1)^3 S^3 T^7 R6,
M5 = (27/2^51) p^5(2r-1)^4(2r+1)^3 S^3 T^7 R5.
```

`R6` and `R5` are the completely recorded residual polynomials of
total degrees twenty and twenty-one in
[`audit-mf6-e1-principal-raw-minors-2026-10-08.json`](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.json).
The verifier independently recomputes every cofactor, checks these
factor identities and all five others, and compares their reductions
with the previously saved seven-cofactor remainders.

The factor `2r+1` is a unit on `U`, for the precise reason

```
H(p,-1/2)=8p(p+2)^2,
P(p,-1/2)=2(p+2).
```

Both possible points violate `pP!=0`. An earlier informal message
incorrectly gave `H(p,-1/2)=8(p+2)^3`; the corrected identity above is
checked directly by the verifier and is the one used in the proof.

On `S!=0`, every displayed prefactor of `M6,M5` is a unit. If their
residuals vanish simultaneously at a point of `H`, then both exact
resultants in `p` vanish at its `r` coordinate. Their gcd is

```
const * (2r-1)^16(2r+1)^26 Q^5,
const = 175495605123022848.
```

The full factorizations are

```
Res_p(H,R6) = const * (2r-1)^16(2r+1)^26 Q^6 F12,
Res_p(H,R5) = -8const * (2r-1)^16(2r+1)^27 Q^5 F16,
```

where

```
F12 = 626688r^12+2113536r^11+7473152r^10+9351168r^9
      +16506624r^8+15984640r^7+7622400r^6+3220992r^5
      +1515632r^4+554304r^3+123528r^2+14832r+801,

F16 = 518455296r^16-3247570944r^15-13217169408r^14
      -31615975424r^13-48489316352r^12-51974971392r^11
      -40950489088r^10-25317873664r^9-13339307520r^8
      -6235899392r^7-2459068928r^6-740795520r^5
      -157172544r^4-21102432r^3-1591200r^2-59976r-8577.
```

The verifier checks the exact resultant gcd, including all possible
cross-factor common roots; this is stronger than separate informal
coprimality assertions about `F12,F16`.

The roots `r=+/-1/2` have already been removed on `U`. At a root of
`Q`, use `K=QQ(sqrt(-2))` and
`r=(-5+2sqrt(-2))/6`. Direct Euclidean division in `K[p]` yields

```
gcd(H,R6,R5)=p-(2r+1).
```

The checker verifies an extended-Euclidean identity and divisibility,
so this is a complete exact fiber calculation. Its conjugate covers
the other root of `Q`. But `p=2r+1` on `Q=0` implies `P=0`.
Therefore neither quadratic fiber contains a common residual zero
on `U`. This proves that the two cofactors cannot vanish simultaneously
on `U` intersected with `S!=0`.

## 3. Retain and cover the nonunit factor S

`S` is not a unit and was never silently cancelled. Its entire fiber
on `H` is given by

```
H(2r+1,r)=-(2r-1)^2(2r+1)(6r+1)Q,
P(2r+1,r)=Q.
```

The roots `r=+/-1/2` and `Q=0` violate the defining open conditions.
The sole remaining point is `r=-1/6,p=2/3`, with `P=8`.
At that point, the actual cofactor omitting column four is

```
1073741824 / 36472996377170786403 != 0.
```

This independently covers the retained `S=0` branch. Consequently
`rank(D)=6` everywhere on all of `U`. Since `rank(M1)=11` and the
first-normal kernel has dimension seven, the complete quartic matrix
has rank seventeen and its kernel has dimension one.

## 4. Evidence and exact remaining scope

The source and raw inputs are bound by SHA-256 in
[`session-mf6-principal-rank-open-audit-2026-10-08.json`](../scratch/session-mf6-principal-rank-open-audit-2026-10-08.json),
with the successful terminal transcript in
[`session-mf6-principal-rank-open-audit-2026-10-08.out`](../scratch/session-mf6-principal-rank-open-audit-2026-10-08.out).
The independent raw-factor explorer and norm explorer are preserved
beside their outputs. Three preliminary verifier runs were corrected:
one transcribed the free determinant denominator as `2^53` rather
than `2^52`; two used structural SymPy equality instead of
expanded polynomial equality (a cofactor remainder and the linear P specialization). Their failed transcripts are retained.
None of these failed runs entered the resultant/fiber argument.

This theorem covers only the displayed principal flat chart with
`a0=b0=1`, including every parameter of that chart, rather than merely
a generic rank computation. The `P=0` alternate-killing-section fibers,
`r=1/2` frame degenerations, `b0=0`, and the earlier endpoint orbits
must still be reconciled by their complete ambient quartic calculations
before asserting a theorem for the whole principal triple incidence.
The existence or nonexistence of an STCI mate for the remaining unique
quartic carriers is a separate problem and is not claimed here.


---

## Source: 2026-10-08-session-mf6-rhalf-scroll-conductor.md

# The principal MF6 boundary (p,r)=(8,1/2): an entire-conductor proof

Date: 2026-10-08. Status: **PROVED all-mate exclusion**, with exact
normalization/conductor identities and a completed
[independent audit](#source-2026-10-08-session-mf6-rhalf-scroll-independent-auditmd).
This is a fixed member of the principal
e=1,d2=1 quartic family, not an exclusion of every member of that family.

## 1. Carrier binding and a finite smooth normalization

The complete quartic space at this boundary has dimension one. The
source quartic is the `rhalf_unique` row of the
[exact principal-boundary record](../computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08_rational.json).
Make the invertible linear coordinate change

    x=x0+4x1-16x2-16x3,
    y=x1-4x2,
    z=x1-12x2-16x3,
    w=x3.

Set

    L=96w+x-8y+4z, chi=x-8y, G=xL-8yz.

The original quartic, in these coordinates, satisfies the exact identity

    -64 F=G^2-x^3 chi.

Thus its discriminant as a quadratic polynomial in w is
9x^5(x-8y). If instead one uses the rational coordinate T=xw, its
discriminant is 9x^3(x-8y); these are the same nonsquare obstruction.
The coefficients of F as a polynomial in w have gcd one. The
discriminant is nonsquare in k(x,y,z), so Gauss's lemma proves F is
irreducible over every characteristic-zero algebraically closed field.

Let S=P1_[a:b] times P1_[U:V] and H=O_S(2,1). Define a morphism
nu:S->P3 by the four sections

    x=U b^2,
    y=U(b^2-a^2)/8,
    z=V b^2,
    w=(U(ab-a^2)-V(a^2+3b^2))/96.

They have no common zero. For b!=0, x=z=0 would force U=V=0.
For b=0, a!=0, y=w=0 again forces U=V=0. Their substitution into F
is zero. The pullback of O_P3(1) is the ample H. A positive-dimensional
fiber would contain a curve on which H has degree zero, impossible;
therefore the proper morphism is finite onto its image.

The generic base parameter a/b is recovered from the image by

    a/b=G/x^2,

and the remaining parameter U/V is recovered as x/z. Thus nu is
birational. Its image is the integral quartic F, and S is its smooth
normalization. Its polarization is the smooth rational quartic scroll
F0 with H^2=4 and K_S.H=-6.

## 2. The complete normalization ring and the entire conductor ideal

Two additional degree-one sections are

    v=Uab, u=Vab.

Together with x,y,z,w they span the complete six-dimensional section
space H0(S,H), since they recover the six monomials
Ub^2,Uab,Ua^2,Vb^2,Vab,Va^2. The corresponding full section ring B is
the normal, projectively normal quartic-scroll ring. Let A be the
quartic hypersurface ring generated by x,y,z,w. Exact identities give

    xv=G, xu=zv, Lv-8yu=x chi,
    v^2=x chi, uv=z chi,
    u^2=zv-z chi-3z^2-96zw.

The A-module A+Av+Au is closed under multiplication, hence equals B.
The displayed monic quadratic equations also show B finite over A.
For the ideal

    J=(x^2,xy,G),

one has the six exact ambient cubic identities

    Jv=(xG, yG, x^2 chi),
    Ju=(zG, (LG-x^2 chi)/8, xz chi).

Therefore J annihilates B/A, so J is contained in the actual conductor
ideal I. Its Hilbert--Burch matrix is

    [ x,  0  ],
    [-z,  x  ],
    [ L, -8y ].

The maximal minors generate J. Its support is x=0,yz=0, so it has
height two, and the Hilbert--Burch resolution makes its projective
curve an ACM cubic with Hilbert polynomial 3m+1. The entire actual
conductor of this smooth quartic-scroll normalization also has
polynomial 3m+1 by the duality calculation in the
[applicability note](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-conductor-applicabilitymd).
The inclusion J subset I gives a coherent quotient I/J. Its Hilbert
polynomial is zero; a nonzero coherent sheaf on projective space has a
nonzero Hilbert polynomial. Hence the conductor ideal sheaves agree:

    I=J, Gamma=V(x^2,xy,G).

This identifies the entire scheme, rather than just its Jacobian or
reduced singular support. Gamma is a double line x=y=0 together with
a reduced line x=z=0. Pulling J to S gives

    x^2=U^2 b^4,
    xy=U^2 b^2(b^2-a^2)/8,
    G=U^2 a b^3.

After the common factor U^2b^2, the residual sections
b^2,(b^2-a^2)/8,ab have no common zero on P1. Therefore the entire
upstairs conductor is

    D=2E+2T, E={U=0}, T={b=0}.

No isolated conductor defect is left implicit.

## 3. The nonreduced downstairs conductor is Gorenstein and the cover flat

The entries of the Hilbert--Burch matrix cannot all vanish at a
projective point: x=y=z=0 would make L=96w, forcing w=0. At every
point of Gamma at least one matrix entry is a unit, so its localized
grade-two ideal has two generators and is a complete intersection.
Thus the actual nonreduced Gamma is locally Gorenstein.

The conductor duality exact sequence is

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,
    p=nu|D.

Its quotient omega_Gamma is invertible, so the sequence locally splits
as modules. Consequently p_*O_D is locally free of rank two over
Gamma, including its double-line points and the line intersection.
This is the reason flatness holds; Cohen--Macaulayness alone would
not suffice. Trace in characteristic zero gives the global algebra
involution sigma with fixed algebra exactly O_Gamma.

At the generic point of the double line, E is the unique reduced
upstairs component, and its reduced map has degree two:

    w/z=-(a^2+3b^2)/(96b^2).

Thus sigma preserves E and acts by a/b -> -a/b on its reduced function
field. At the generic point of the other line, T maps isomorphically
to that line and is doubled upstairs. Its generic algebra is the
dual-number algebra over the reduced line's function field, and sigma
acts trivially on the reduced field. In particular sigma preserves
both minimal associated primes of D. This statement retains the
generic nilpotent scheme structure.

## 4. Every descended power compresses to a descended square

Suppose F had a mate of positive degree n presenting C0 set
theoretically. The full-support argument for a smooth scroll gives a
unique c isomorphic to C0, c~H, and

    nu*G_mate=lambda f^n, div(f)=c.

The quotient is a global constant. Since the mate descends from X,
sigma(f|D)^n=(f|D)^n. The restricted section f is generically nonzero
on both conductor primes, hence invertible in each generic Artin ring
of D. The ratio h=sigma(f)/f satisfies h^n=1 there.

In a characteristic-zero Artin ring, any root of T^n-1 is one of the
constant roots of unity after choosing its reduced field root: the
derivative nT^(n-1) is a unit, so its nilpotent correction is zero.
On E the reduced field contains the algebraically closed constants,
and h is a constant root zeta. Applying sigma twice, while sigma
preserves this generic prime, gives zeta^2=1. On T the reduced action
of sigma is the identity, so the reduced ratio is one and h=1.
It follows that f^2 is sigma invariant in both generic Artin rings.

The Cartier conductor D on smooth S is Cohen--Macaulay and has no
embedded associated primes. A section of its invertible restricted
line bundle that vanishes in all generic localizations is therefore
zero globally. Hence f^2|D is sigma invariant everywhere, including
at the intersection and through all nilpotent jets. Since the fixed
algebra is O_Gamma, it is a section pulled back from O_Gamma(2).

The entire conductor square now glues f^2 with that downstairs
section to O_X(2). The quartic hypersurface sequence lifts it to an
ambient quadric Q, with

    (X intersect V(Q))_red=C0.

The sole quadric through C0 is q=x0x3-x1x2, smooth. On this quadric
C0 has bidegree (1,3), while the restriction of the integral quartic
F has divisor class (4,4). It cannot be supported only on C0.
This contradiction excludes a mate in every positive degree.

## 5. Exact evidence and retained limits

The standalone
[verifier](../computations/verify_session_mf6_rhalf_scroll_2026_10_08.py)
reconstructs every parameterization coefficient, checks the carrier
binding to the recorded MF6 member, verifies the three quadratic
closure identities and all six conductor annihilator certificates,
and checks the entire pullback conductor ideal. Its
[JSON evidence](../computations/verify_session_mf6_rhalf_scroll_2026_10_08.json)
records the source and input hashes. The all-mate conclusion is the
structural proof in sections 3--4, not a bounded numerical test.

During checker development, one assertion used the discriminant in
T=xw while labeling it as the discriminant in w; the exponent was
corrected from x^3 to x^5. A second assertion compared an expanded
polynomial with an unexpanded syntactic expression; it was replaced
by an exact difference check. Neither change alters the normalized
identities. Both earlier failures preceded the accepted PASS.

This example demonstrates that some nonreduced downstairs conductors
are tractable through actual finite flat algebras. It does not prove
every nonreduced ACM cubic conductor Gorenstein or every generic deck
action preserves its conductor primes. Those hypotheses must be
checked for another carrier. The unrestricted STCI problem and the
remaining principal-family strata are unchanged by this fixed-member
exclusion.


---

## Source: 2026-10-08-session-mf6-rhalf-scroll-independent-audit.md

# Independent audit: the principal MF6 (p,r)=(8,1/2) carrier

Date: 2026-10-08. Status: **ACCEPTED all-mate exclusion** of this
fixed characteristic-zero member of the principal e=1,d2=1 family.
The audit does not exclude the entire principal family. In particular
the reduced-downstairs-conductor theorem is not applied: the actual
conductor here contains a double line.

Audited owner proof:
`2026-10-08-session-mf6-rhalf-scroll-conductor.md`.
Audited exact source:
`../computations/verify_session_mf6_rhalf_scroll_2026_10_08.py`.
The source was freshly replayed in this audit and returned PASS with
SHA-256 `9d532c25c9f50f206e0d57c5ce7f35b9feb54707bf1b630fd622c0c473028aa2`.
Its JSON binds the independently parametrized carrier to the saved
`rhalf_unique` quartic row and records its input hash. The computations
verify algebraic identities; the arbitrary-degree conclusion is the
structural argument checked below.

## 1. The carrier and finite normalization

The invertible coordinate change in the owner note gives

    L=96w+x-8y+4z, chi=x-8y, G=xL-8yz,
    -64F=G^2-x^3*chi.

As a quadratic in w, the discriminant is 9x^5*chi. It is not a
square in k(x,y,z), and the coefficients are primitive. Thus F is
irreducible by Gauss's lemma over every algebraically closed
characteristic-zero field. Using T=xw instead changes the displayed
discriminant by a square; confusing those two polynomial variables
does not change irreducibility, but the recorded w exponent five is
the correct one.

On S=P1_[a:b] times P1_[U:V], the four proposed sections have class
H=O(2,1):

    x=Ub^2, y=U(b^2-a^2)/8, z=Vb^2,
    w=[U(ab-a^2)-V(a^2+3b^2)]/96.

They have no common zero. At b!=0 the equations x=z=0 would force
U=V=0; at b=0, y=w=0 likewise forces U=V=0. Consequently their
morphism pulls O_P3(1) back to the ample H. A positive-dimensional
fiber on the projective S would contain a curve of H-degree zero,
impossible. The morphism is therefore finite onto its image.
The generic ratios G/x^2=a/b and x/z=U/V recover both parameters,
so it is birational. Substitution vanishes on F; irreducibility makes
its image the whole carrier. The smooth S is its normalization.

## 2. The complete normalization module and actual conductor

The extra sections v=Uab and u=Vab recover, together with the four
ambient sections, the complete six-dimensional space H0(S,H).
The O(2,1) section ring is generated in degree one: every monomial
of bidegree (2m,m) decomposes into m monomials of bidegree (2,1).
It is the normal quartic-scroll section ring B. The hypersurface
ring A is generated by x,y,z,w.

The exact relations in the owner note show that A+Av+Au is closed
under multiplication and contains the six degree-one generators.
Hence B=A+Av+Au, as a finite A-module. The two monic quadratic
relations for u and v also give finiteness directly. The six cubic
identities show that J=(x^2,xy,G) annihilates B/A; they prove
J subset I, not merely vanishing on the normalization defect support.

The Hilbert--Burch matrix

    [x,0; -z,x; L,-8y]

has maximal minors generating J, which has height two and support
x=0,yz=0. Its resolution gives Hilbert polynomial 3m+1. The entire
actual conductor I of this smooth-scroll normalization has the same
polynomial by finite duality and Riemann--Roch. Thus the coherent
quotient I/J has polynomial zero and is zero: every nonzero coherent
sheaf on projective space has nonzero Hilbert polynomial, since high
twists are generated by nonzero global sections and have no higher
cohomology. This proves equality of the projective conductor ideal
sheaves I=J; no Jacobian or reduced-support substitution occurs.

Pulling J back gives the common factor U^2b^2 times
b^2,(b^2-a^2)/8,ab. Those residual sections have no common zero on
P1. Therefore the actual upstairs conductor is exactly

    D=2E+2T,  E={U=0}, T={b=0},

with no isolated remainder. It is the anticanonical Cartier divisor
on S. Downstairs its support is two lines, one doubled.

## 3. Gorenstein center and rank-two trace on a nonreduced base

At every projective point some entry of the Hilbert--Burch matrix is
a unit: if x=y=z=0 then L=96w, and their simultaneous vanishing is
only the irrelevant affine origin. Row and column operations with
that unit reduce the localized grade-two ideal to two generators,
so Gamma=V(J) is a local complete intersection and Gorenstein.

The previously proved whole-conductor sequence

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0

makes p_*O_D locally free of rank two because omega_Gamma is
invertible. This argument is valid over the nonreduced Gamma and
does not assert flatness from Cohen--Macaulayness alone.

For any rank-two locally free algebra over a ring with 2 invertible,
trace splits it as R plus a tracefree invertible module. Locally a
tracefree generator eta has eta^2=Delta in R by Cayley--Hamilton;
the map eta->-eta is the canonical involution sigma, with fixed
algebra exactly R. These assertions remain true when R is
nonreduced. The hyperplane line bundle on D is pulled back from
Gamma and therefore has its canonical sigma action.

The unique reduced conductor component above the doubled base line
is E. Its reduced map has degree two, with parameter a/b determined
by its square. The unique reduced component above the other line
is T, mapping isomorphically. Thus sigma preserves each minimal
prime of D: it cannot exchange components lying over different
base primes. On the reduced E function field it is the quadratic
deck action a/b->-a/b; on T it is the identity. Preservation of
these primes, rather than a presumed involution on the whole
surface S, is the fact required by the next step.

## 4. Roots of unity retain every generic nilpotent jet

The mate hypothesis gives the full inverse support c isomorphic to
C0, with c~H and nu*G_mate=lambda*f^n, div(f)=c. The divisor c is
different from E and T, so f is a unit after restricting its line
bundle to either generic local Artin ring of D. Choose a local
line-bundle frame pulled back from Gamma. The ratio

    h=sigma(f)/f

is then an element of that Artin ring, with h^n=1 because the mate
power descends.

The polynomial T^n-1 factors into distinct linear factors T-zeta
with zeta in the algebraically closed constant field. In a *local*
Artin ring the reduction of h selects one such zeta. Every other
factor h-zeta' is a unit, so the product being zero forces
h-zeta=0 exactly. Thus there is no surviving nilpotent correction.
This factor argument is stronger and more explicit than checking
only a reduced field ratio. Characteristic zero is essential.

At E, sigma preserves the generic local ring and fixes constants.
Applying it twice to sigma(f)=zeta*f gives zeta^2=1. At T its
reduced field action is the identity, so the selected zeta is one.
Therefore f^2 is invariant in both generic Artin localizations.
This includes the generic nilpotent directions above the double line.

## 5. Extension and line-bundle descent

D is Cartier on the smooth surface S, hence Cohen--Macaulay and
without embedded associated primes. An invertible sheaf on D has
the same associated primes. A section vanishing at every generic
localization cannot have finite-support residue; it is zero globally.
Thus sigma(f^2)-f^2 vanishes everywhere on D, including its intersection
and all nilpotent jets there.

Since the fixed algebra of the trace involution is O_Gamma, the
canonical pullback line-bundle action identifies f^2|D with a section
of O_Gamma(2). The *entire* conductor square glues it with f^2 on S
to a section of O_X(2). The hypersurface restriction sequence lifts
that section to an ambient quadric. Finiteness shows its zero support
on X is exactly C0.

That is impossible: C0 lies on its unique smooth quadric with class
(1,3), while the carrier restricts to class (4,4). No positive
multiple of (1,3) equals (4,4). Therefore this fixed MF6 carrier
has no mate in any degree.

## 6. Audit decision and scope

The normalization, whole conductor equality, local Gorensteinness,
nonreduced-base trace algebra, prime preservation and generic-to-global
extension all pass this independent audit. The proof is accepted for
the specified p=8,r=1/2 principal member. It does not infer reducedness
of Gamma and does not apply a reduced-center theorem to this scheme.
Other principal parameters, other conductor schemes, and the
unrestricted STCI problem remain separate.


---

## Source: 2026-10-08-session-new-results-acceptance.md

# Root acceptance of the October 8 scroll and defect-four results

Date: 2026-10-08. Fixed curve C0=[s^4:s^3t:st^3:t^4], over an
algebraically closed characteristic-zero field. This records proof
review, not a universal STCI resolution or a novelty claim.

This is the intermediate acceptance record. Its statements of pending
audit and the remaining reducible/nonreduced conductor boundary describe
that stage of the work. The
[late reconciliation](OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-late-results-acceptancemd)
records the completed independent audits, full smooth-scroll exclusion,
principal ancestor closure and current remaining strata.

## 1. Every integral quartic singular along a smooth twisted cubic

**Accepted:** such a quartic has no mate cutting out C0 set-theoretically,
in any positive degree. The [applicability proof](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-conductor-applicabilitymd)
and [conductor criterion](OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-irreducible-conductor-compressionmd)
together supply the argument. The [independent adversarial audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-conductor-adversarialmd)
checks the criterion and the entire-conductor Hilbert/CM calculation.
The root additionally checked the stronger equation-space and blowup
transition below. The independent auditor reported acceptance of these
steps before its turn ended at the account usage limit; its planned
section 10 was not completed, so that unwritten section is not cited.

The complete derivative restriction on all 35 quartic monomials has
rank 29. Six independent products of the three twisted-cubic quadrics
span the kernel. The independent [literal-minor source](../computations/audit_scroll_twisted_cubic_equation_space_2026_10_08.py)
rebuilds derivatives by substitution and computes the stated determinant
104509440 by Fraction elimination. Root replay passed in the isolated
continuation snapshot. Thus F=Q(xi1,xi2,xi3) holds for the entire
equation space, without an slc assumption. If Q factored, F would factor
into nonzero quadratic factors; hence integral F gives a smooth conic Q.

The two syzygies define a rank-two matrix at every point of P2. Their
incidence variety is therefore a smooth P1 bundle, agreeing with the
blowup of the smooth twisted cubic. The inverse image S of Q is a smooth
P1 bundle over a smooth conic. The exceptional fiber over each point of
the twisted cubic maps to a line in P2, which a smooth conic cannot
contain. Every fiber of S->X is finite, including tangencies, so this
proper birational map is finite and is the normalization. Off the cubic
it is an isomorphism. A normal local ring on the cubic would also make
it an isomorphism there; since S is smooth and X is singular there,
this is impossible. The whole nonnormal support is exactly the cubic.

Adjunction gives K_S=-E|S, H^2=4 and K_S.H=-6. Finiteness makes H ample,
and H has ruling degree one. On F_e this implies H=C_min+a f,
2a-e=4 and a>e, hence e=0 or 2. These verify the smooth quartic-scroll
hypotheses used by the criterion.

Finite absolute duality identifies the conductor with nu_*omega_S,
not with a relative formula requiring nu to be flat. It is maximal CM
over the quartic surface. Its quotient is a pure CM curve with Hilbert
polynomial 3m+1. Degree three and the smooth degree-three support force
generic multiplicity one. Any nilradical would then be supported at
finitely many points, prohibited by depth one. Thus the actual downstairs
scheme is the reduced smooth twisted cubic. The upstairs conductor is
Cartier and CM, finite over the smooth curve, and torsionfree over each
local DVR; it is flat, of rank H.D/3=2.

The root reviewed all three rank-two conductor cases. For integral
reduced D, invariance of f^n gives sigma(f)/f=+1 or -1, and f^2 descends
through the full conductor square. For reducible D, its algebra is
O+O(-2) with eta^2=q_2^2. Unequal branch factors force both restrictions
to be scalar multiples of q_2 times a linear section. Singleton fibers
put that section's zero at a branch intersection; a smooth lifted curve
cannot have contact greater than the mutual branch contact with both
branches. For nonreduced D, eta^2=0, and the all-n coefficient
n*a^(n-1)*b forces b=0, so f itself descends. The resulting quadric or
hyperplane mates are impossible for C0. The argument uses global
constant units, whole conductor schemes and full inverse support.

The primary equation/blowup presentation was checked in
[Ducat, section 5.7](https://d-nb.info/1317691679/34). The independent
equation certificate removes reliance on extending that paper's slc
classification. The absolute-duality input was checked against
[Stacks 0AX0](https://stacks.math.columbia.edu/tag/0AX0) and
[the CM concentration lemma](https://stacks.math.columbia.edu/tag/0AWQ).

**Boundary:** reducible/nonreduced downstairs conductors, singular
normalizations, other quartic classes and higher carrier degrees remain
outside this theorem.

## 2. Both algebraic e=1,d2=4 ancestor directions

**Accepted:** for A=r*z,B=1,12r^2+4r+3=0, every genuine defect-four
triple has at most one containing quartic. Hence it cannot supply two
independent quartic multiplier equations for the fixed ancestor targets.
This is the narrow [defect-four proof](OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-localcoh-e1-d4-algebraicmd),
not an STCI mate theorem.

The root checked the explicit seven ambient forms, their complete
35-column double conditions, and their normalized h/E coefficients.
Rank 28 of the complete double matrix and independence of the seven
forms establish completeness. Arithmetic in the quadratic field covers
both embeddings. The two free primitive h coefficients uniquely match
the constant and eighth coefficients of delta*E, so the quartic fiber
is exactly the kernel of the remaining seven-by-five operator.

The minors d0^4 and d4^4 give rank at least four on those two opens.
On d0=d4=0, the minors d1^5 and d3^5 give rank five when either is
nonzero. The final delta=d2*z^2 matrix has five pairwise distinct
diagonal constants, so at most one diagonal entry vanishes. This covers
all homogeneous delta, including repeated and infinity roots, and
proves kernel dimension at most one everywhere.

For theta=0, the local ideal (delta*m,my,m^2,y^3) leaves
R/(delta)*m torsion at every defect zero. A nonzero section of O(4)
has such a projective zero, so this is not a valid finite-flat triple.
Every genuine triple therefore has theta!=0, which is normalized to
one by scaling the equation. This discards no valid theta=0 boundary.

The verification agent independently reported this exact coverage and
the torsion check before its usage-limit interruption. Its isolated
source-byte replay is preserved in
[the audit replay directory](../validation/2026-10-08-e1-d4-algebraic-audit/replay-manifest.json);
it did not finish a separate narrative audit. Root's central isolated
replay also passed, with source SHA256
ae88024f00b8216be727957930747001b44f457e532a0746e6a8e2a657850a02.

**Boundary:** the principal obstruction-zero direction and directions
with nonzero primitive quadratic obstruction remain open at positive
D2. This does not exclude every defect-four Gorenstein quadruple.


---

## Source: 2026-10-08-session-nonimmersion-prime-independent-audit.md

# Independent audit: the generic nonimmersion-prime obstruction

Date: 2026-10-08. Auditor: `verification`. Status: **PROVED HERE**, independently audited from the full power identity. This note does not classify all nonnormal quartic surfaces.

## Exact statement

Let k be algebraically closed, let S be a smooth projective surface, and let nu:S -> X subset P^N be finite and birational. Write H=nu^*O_X(1). Suppose a smooth integral curve c on S satisfies c~H, there is f in H^0(S,O_S(H)) with divisor c, and an ambient homogeneous polynomial G of positive degree n satisfies

    nu^*G=lambda f^n, lambda in k^*.

Suppose that nu|c is an immersion into P^N. Assume n is nonzero in k; in particular the statement applies in characteristic zero. If E is any integral curve distinct from c with H.E>0, then dnu has generic rank two along E.

Neither smoothness of E nor a conductor hypothesis on E is required. A finite normalization of a smooth rational quartic scroll has H ample, so every actual conductor prime satisfies the positive-intersection hypothesis. The previously audited full-support mate reduction supplies exactly c, f, and the power identity in that application.

## Proof, including singular E and the point f=0

Because c.E=H.E>0 and E is distinct from c, choose a closed point P in c intersect E. Suppose that dnu has generic rank at most one along E. On any local chart, every two-by-two minor of its derivative matrix vanishes in k(E). The entries are regular and E is integral, so those minors vanish modulo the prime ideal of E. Hence the rank of dnu at P is at most one. Rank zero would already contradict immersion of c; its rank is therefore exactly one.

Choose an ambient hyperplane section h nonzero at nu(P). Its pullback trivializes H near P, and the target is in the affine chart h!=0. Trivialize the smooth source tangent bundle near P. Let q_1,...,q_N be the pulled-back affine target coordinates, and write a derivative row as (a,b), with at least one entry a unit at P. The regular vector field

    V=(-b,a)

in this tangent frame is nonzero at P. It kills that row identically. Its pairing with every other derivative row is a two-by-two minor, up to sign, so

    V(q_i)=0 modulo I_E for every i.

This is the required kernel construction. It works over the singular ring O_E: a unit pivot and vanishing minors suffice. There is no need to regard E as a smooth curve, to extend an a priori kernel line bundle, or to assume a global involution.

Put g=f/(nu^*h) and A=G/h^n. These are respectively a source regular function and a target affine regular function, with

    nu^*A=lambda g^n.

The chain rule gives V(nu^*A)=0 modulo I_E, and differentiation gives

    n lambda g^(n-1) V(g)=0 in O_E.

The image of g in the local domain O_E is nonzero: its divisor on S is c, distinct from E. Cancel its nonzero power in that domain, using n lambda!=0, to obtain V(g)=0 in O_E. The resulting equality is regular at P, so dg_P(V(P))=0. This cancellation takes place before specializing at g(P)=0; it does not divide by g(P).

Since c is smooth, dg_P is nonzero and its kernel is the one-dimensional tangent line T_Pc. The nonzero vector V(P) both lies in that tangent line and is killed by dnu_P. This contradicts immersion of nu|c. Thus the assumed generic rank deficiency is impossible.

## A local-unit variant and exact limits

The same cancellation argument even permits a local identity nu^*A=u g^n for a regular unit u, provided that A is an ambient function. Differentiation modulo I_E gives

    g^(n-1) (n u V(g)+g V(u))=0.

After cancelling in O_E and evaluating at P, where g(P)=0, one again obtains V(g)(P)=0. The global constant-power identity available in the scroll application is stronger than needed for this local argument.

The proof does not apply to an isolated rank-drop point on a prime which is generically immersive. It does not infer rank deficiency merely from an upstairs conductor multiplicity. A claim that a concrete conductor branch is excluded must establish its generic derivative rank from the actual normalization morphism or from a valid transverse singularity argument. In characteristic dividing n, the derivative of g^n loses the necessary information.

## Relation to the current frontier

This independently agrees with the separate [normal-global audit](#source-2026-10-08-session-normalization-differential-independent-auditmd), whose proof uses the equivalent constant-rank kernel over O_E. Agreement is not the proof: the unit-pivot argument above independently establishes the extension across singular E and across c intersect E.

For an integral quartic with smooth rational quartic-scroll normalization, any mate of the fixed smooth rational quartic C0 must therefore leave the normalization generically immersive along every actual conductor prime. The generic Artin classification or geometric transverse branch classification still has to establish which conductor possibilities have that property; the obstruction alone is not a closure of that carrier class.

No canonical frontier file was changed by this audit.


---

## Source: 2026-10-08-session-normalization-differential-independent-audit.md

# Independent audit: a rank-deficient normalization prime obstructs a mate

Date: 2026-10-08. Auditor: `normal_global_adversarial`. Status: **PROVED HERE,
independently accepted**, with the hypotheses below. No claim about all
nonnormal quartics is made by this lemma alone.

## Statement

Let k be an algebraically closed field of characteristic zero. Let
nu:S->X subset P^N be a finite birational morphism from a smooth projective
surface. Put H=nu^*O_X(1). Suppose there is a smooth integral curve c on S,
a section f of O_S(H) with div(f)=c, and a homogeneous polynomial G of
degree n>0 such that

    nu^*G=lambda f^n,       lambda in k^*,

as sections of O_S(nH). Suppose also that nu|c maps isomorphically to a
smooth embedded curve in P^N. Let E be an integral curve on S distinct
from c, with H.E>0. Then the differential

    dnu:T_S|E -> nu^*T_(P^N)|E

has generic rank two.

Equivalently, a prime E of generic differential rank at most one and
positive H-degree contradicts this collection of hypotheses. The curve
E need not be smooth, and E need not be a conductor prime. In the
application, E is an actual conductor prime and c~H, with H ample.
The characteristic assumption can be weakened to n nonzero in k.

## Proof with the extension at f=0 retained

Since c.E=H.E>0, choose a closed point P in c intersect E. The immersion
nu|c into P^N implies that dnu_P is nonzero on the tangent line T_P c.
In particular its rank is at least one.

Assume that dnu has generic rank at most one on E. Every two-by-two
minor of a local matrix for dnu is then zero in the function field of
the integral curve E, hence zero in O_E wherever that matrix is defined.
Consequently the rank at every point of E is at most one. At P it is
exactly one. After shrinking an open neighbourhood of P in E, an entry
of the matrix is a unit, so the map has constant rank one on that
neighbourhood. Its kernel K is therefore a line subbundle of T_S|E.
This elementary constant-rank assertion holds over O_E even when E is
singular: use the unit entry to perform row and column operations; all
remaining matrix entries vanish because its two-by-two minors do.

Choose an ambient hyperplane section h with h(nu(P)) nonzero, and shrink
the neighbourhood in S so that nu^*h is a unit frame for O_S(H). Write

    f=g nu^*h,        A=G/h^n on the ambient affine chart.

The global equality of sections becomes the equality of regular
functions

    nu^*A=lambda g^n.

For any local generator v of K, the differential of every ambient
function annihilates v, so

    0=d(nu^*A)(v)=lambda n g^(n-1) dg(v) in O_E.

The section g is nonzero at the generic point of E because E is
distinct from div(f)=c. The local ring O_E is a domain. Since n is
invertible, cancellation in this domain gives dg(v)=0 as a regular
section along E, including at P. This is the precise extension step:
no division by the value g(P)=0 is made.

At P, g is a local defining equation of the smooth curve c. Thus dg_P
is nonzero and ker(dg_P)=T_P c. The nonzero line K_P lies in this
kernel; both are one-dimensional, so

    T_P c=K_P=ker(dnu_P).

This contradicts the immersion of nu|c. Hence the generic rank on E
is two.

If the generic rank on E were zero, all matrix entries would vanish
on E and already contradict the immersion at P. The proof therefore
also handles the rank-zero case.

## Applicability to the scroll frontier

The previously audited mate reduction supplies exactly the required
data when S is a smooth rational quartic-scroll normalization of an
integral quartic carrying C0: the full inverse image of C0 is a single
smooth curve c isomorphic to C0, div(nu^*G)=n c, the torsion-free Picard
group gives c~H, and a section f with div(f)=c satisfies the full power
identity up to a constant. Finiteness makes H ample, so H.E>0 for
every conductor prime E.

Therefore every surviving smooth-scroll mate must have differential
rank two at the generic point of every actual upstairs conductor
prime. In particular a generically cuspidal normalization branch,
where one tangent direction is killed by the normalization map, is
excluded if that rank-one statement is verified for the actual
surface morphism. A conductor multiplicity by itself does not verify
that statement; the local normalization or transverse singularity
must still be identified.

For the proposed residual F2 divisor D=4F+2C_min, the implication is
conditional only on the local geometric identification of F as a
rank-deficient cuspidal branch. Once that identification is proved,
the lemma excludes it without any Gorenstein assumption on the
downstairs conductor and without extending a trace involution through
a nongorenstein point.

## Adversarial checks

- The argument differentiates the entire power identity, not its first
  normal coefficient or a chosen jet truncation.
- It uses a hyperplane frame pulled back from the ambient space; a
  general local frame could have a nonzero derivative on K.
- It cancels g only in the domain O_E before specialization, then
  specializes the regular equality dg(v)=0 at P.
- A local kernel generator need only be defined along E. A lift to a
  vector field on a neighbourhood of S is unnecessary: differentials
  restricted to E already pair with T_S|E.
- Singular E is harmless because a unit matrix entry and vanishing
  two-by-two minors give a locally free kernel near P.
- The positive intersection and the smooth embedded image are
  essential. Without either, the tangency contradiction need not
  arise. Characteristic dividing n invalidates the cancellation.

This is a structural obstruction. It does not by itself classify the
remaining nonreduced nongorenstein ACM cubic conductors.

## 2026-10-09 addendum: the local unit factor is harmless

Status: **PROVED HERE, independently accepted**. This is a stronger
local version. It does not require a global root section, a constant
factor, rationality of S, or a prescribed carrier degree.

Let nu:S->X subset P^N be a morphism, let P belong to a smooth integral
curve c on S, and suppose S is smooth on an open neighbourhood of P.
Assume nu|c is an immersion at P. Let E be an integral curve through P,
distinct from c, and suppose dnu has generic rank at most one on E.
If an ambient regular function A has pullback

    nu^*A=u f^m

near P, where f is a local defining equation of c, u is a regular unit,
m>0, and m is nonzero in the ground field, these hypotheses contradict
one another.

Indeed, the zero-minor argument in the original proof works on the
integral E near P. Rank zero at P already contradicts immersion; if
rank one, its kernel has a regular line generator V near P on E.
Pairing the differential of the entire equality with V gives

    0=f^m du(V)+m u f^(m-1) df(V) in O_E.

Since E is distinct from c, f is nonzero in the domain O_E. Cancel
f^(m-1) in that domain, obtaining the regular equality

    f du(V)+m u df(V)=0 in O_E.

Now specialize at P. The first summand vanishes because f(P)=0;
m and u(P) are nonzero, so df(V)_P=0. Smoothness of c identifies
ker(df_P) with its tangent line, and the nonzero kernel line of dnu_P
is precisely this line. This contradicts the immersion of nu|c.

Here V need only be a section of T_S|E. Pairing differentials with V
defines a derivation from O_S to O_E with the usual Leibniz rule; no
vector-field extension off E and no intrinsic derivation of O_E are
needed. The unit need not be a pullback from the ambient space.
The argument does not claim df(V)=0 at every generic point: for a
nonconstant unit, its regular relation with du(V), followed by
specialization at P, is what proves the contradiction.

### Consequence for an arbitrary finite smooth normalization

Let nu:S->X subset P^N now be finite with S smooth projective, and put
H=nu^*O_X(1). Suppose an ambient form G of degree b>0 has the entire
pullback divisor

    div(nu^*G)=m c,

where c is smooth integral, m>0 is nonzero in the ground field, and
nu|c is an immersion. On an affine chart obtained by dividing by a
nonvanishing ambient hyperplane to degree b, the pulled-back form is
u f^m with u a regular unit: equality of Cartier divisors on the
regular local ring at P provides this factorization.

The divisor identity gives m c~bH. Since H is ample, c is ample as
well (an invertible sheaf is ample if a positive tensor power is).
Consequently c meets every integral curve E distinct from c. Applying
the local lemma at such an intersection shows that dnu has generic
rank two on every such E. This includes every conductor prime
distinct from c, without requiring c~H, Picard-group torsion-freeness,
a global section cutting out c, or a globally constant power factor.

### Exact boundaries of the strengthening

- The distinction E!=c is essential. If E=c, the restriction of f to
  E is zero and the cancellation in its domain is unavailable.
  Ampleness ensures intersections with other primes; it does not
  remove this exception.
- The entire local pullback divisor must be m c near the chosen P.
  If another component of div(nu^*G) passes through P, its factor is
  not a unit and the specialization need not force df(V)_P=0.
- Immersion of nu|c at P is a separate hypothesis. A single smooth
  inverse-image curve alone does not establish it.
- Only smoothness of S near the selected P is needed, but the argument
  gives no conclusion when that intersection lies in the singular
  locus of a normalization. The singular-normalization boundary
  therefore remains.
- Characteristic dividing m invalidates this proof. Characteristic
  zero makes the relevant multiplicity automatically invertible.

No new classification of nonnormal carriers follows solely from this
local strengthening. The earlier historical nongorenstein-scroll
boundary was subsequently closed by the separate
[complete scroll audit](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-nongorenstein-independent-auditmd).


---

## Source: 2026-10-08-session-principal-e1-d1-independent-completeness-audit.md

# Independent completeness audit of principal e1,d2=1 quartic ancestors

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]`, characteristic zero.
Scope: the principal `a0*b1!=0` direction lane for a genuine second defect
of degree one, in the accepted canonical-triple reduction for common
quartic ancestors. This audit combines the complete open-frame proof
with fresh all-35-column boundary calculations. No canonical frontier
file is edited.

**ACCEPTED, with the recorded antecedents:** no quartic common ancestor
for the independent fixed targets u,v has such a canonical triple. The
complete quartic fibre has dimension one throughout the declared open
and at its remaining genuine boundary points, except the node
`(p,r)=(2,1/2)`. The node has dimension four with a fixed cubic factor
and is excluded for ancestors by P-037. A literal uniform dimension-one
claim on the entire principal lane would be false.

This is an ancestor exclusion. A dimension-one containing-quartic space
does not by itself prohibit that single quartic from having an STCI mate
of some other degree. No all-mate carrier theorem is inferred here.
Other e-strata, second-defect degrees, higher multipliers, positive
characteristic, and the universal problem retain their separate scopes.

## 1. Parameter and triple coverage

For `b0!=0`, common direction scaling and the actual ambient torus give
the representative

```text
A=1+r*z, B=1+p*z,
p!=0, p-r!=0,
H=8p^3-(64r^2+128r+16)p^2
 +(96r^4+512r^3+592r^2+128r+6)p
 -(576r^6+960r^5+880r^4+544r^3+220r^2+60r+9)=0.
```

Here p nonzero is the principal condition and p-r nonzero is basepoint
freedom of the homogeneous linear direction pair. No arbitrary change
of the support coordinate or conormal frame is used to normalize it.
The accepted quadratic cocycle has coordinates c1,c2,c3 with
`H=64(c1*c3-c2^2)`. Its linear killing-section matrix is
`[[c1,c2],[c2,c3]]`.

Away from c1 zero the unique defect section is

```text
delta=-8c2+8c1*z=(2r+1)(8p+12r^2+4r+3)-p*P*z,
P=2p+12r^2+16r+9,
Gamma=the polynomial part of delta*h2.
```

The correction is unique because `H0(O(-4+d2))=H0(O(-3))=0`.
On pP nonzero, the z coefficient of delta is nonzero, so its homogeneous
degree-one section has no infinity zero. The exact resultant
`Res_z(delta,Gamma)=p^4*P^4/8` proves flatness at its finite zero.
Repeated-root assumptions do not enter this argument.

If c1=c2=0 and c3 nonzero, the correct alternative killing section is
`delta=1` in the finite chart, a homogeneous section with its zero at
infinity. It must not be replaced by the identically zero expression
`-8c2+8c1*z`. The boundary source explicitly makes this switch. The
surviving c3 gives the nonzero opposite-chart correction at that zero;
its negative has norm 24 over the quadratic field on the two affected
fibres. Thus these fibres are retained rather than deleted by the
generic choice of killing section.

The actual projective coordinate change was independently checked.
The raw reversed-chart normals have linear transition
`(Uraw_inf,Vraw_inf)=z^-7*(V/2,2U)`. Taking
`Uop=Vraw_inf/2,Vop=2Uraw_inf` gives the balanced opposite chart
`x3=1,x2=w,x1=w^3+2Uop,x0=w^4+Vop/2+3wUop` and the direction
`A_inf=r+w,B_inf=p+w`. The literal-form companion uses exactly this
chart. It computes `Gamma_inf=3w^2+(-6+3a)w+4/3-10a/3`, with
`a^2=-2`, by exact zero-remainder division of the actual quadratic
coefficient; its constant is `-c3`, of norm 24. This verifies genuine
flatness at infinity in the actual frame, beyond a finite-chart
resultant with constant delta.

The `b0=0` chart is also retained. Its weighted H equation specializes,
after scaling r to one, to
`p^3-8p^2+12p-72=0`. Before that scaling, r zero would force p zero,
contradicting the principal condition. These are exactly three geometric
points. The cubic has no root modulo five: its values at 0,1,2,3,4 are
`3,3,3,4,2`. Hence it is irreducible over QQ; its discriminant is
`-160704`, so the three characteristic-zero embeddings are distinct.
One exact cubic-field calculation therefore covers all three points.

## 2. Complete frame on the open

Put

```text
T=2p-4r^2-4r-1, S=p-2r-1, Q=12r^2+20r+11,
U={H=0, p*P*(p-r)*(2r-1)*T!=0}.
```

The audited open source reconstructs eighteen independent actual
quartics vanishing on C0. These forms contain no direction parameters;
their only free symbols are the four ambient coordinates. All 35
ambient quartic monomials restrict to
the seventeen distinct powers `z^0,...,z^16`; consequently the curve
restriction has rank 17 and these eighteen forms span the full ideal
space in degree four.

The actual first-normal matrix M1 has shape `11x18`. Its columns

```text
0,1,2,3,4,5,6,11,12,14,15
```

have the exact determinant

```text
D=p^4*(p-r)*(2r-1)*T^2/256.
```

The raw saved seven-column kernel N satisfies `M1*N=0`, and its rows
`7,8,9,10,13,16,17` are precisely the diagonal matrix `-D*I7`.
Thus M1 has rank eleven and N has rank seven in **every** fibre of U;
rank-nullity proves N is the complete kernel there. This statement
does not assume a generic nullspace specializes correctly. The new
independent countercheck reconstructs M1 from the actual quartic jets
and recomputes the determinant and the raw diagonal identities.

The source divides the seven columns by their recorded polynomial gcds.
Every divisor is a unit on U. Its normalized free determinant is
`-p^8*(2r-1)^6*T^11/2^52`. It then reconstructs the second contact map
from the exact condition `delta*q2-Gamma*h=0`. On H zero all but six
contact rows vanish, with the seventh row a multiple of H. The six
recorded row divisions use only p and p-r, also units on U. The resulting
`6x7` matrix is therefore the contact operator on the complete
first-normal kernel, without omitted quartics.

## 3. Two cofactors, their exact norms, and the nonunit S branch

The open verifier recomputes all seven actual maximal cofactors before
reducing modulo H, and checks their retained factorizations. The
cofactors omitting columns six and five have the shared prefactor

```text
(27/2^51)*p^5*(2r-1)^4*(2r+1)^3*S^3*T^7,
```

times the recorded residuals R6 and R5. The factor 2r+1 is also a unit
on U: `H(p,-1/2)=8p(p+2)^2` and `P(p,-1/2)=2(p+2)`, so every point
there violates pP nonzero. S is **not** a unit and is handled separately.

On S nonzero, if both cofactors vanished at a point of H, R6 and R5
would vanish. Their two resultants in p would both vanish at its r
coordinate. The exact resultant gcd is, up to a nonzero rational scalar,

```text
(2r-1)^16*(2r+1)^26*Q^5.
```

The r-half fibres have already been removed on U. Q has discriminant
`-128`, so it defines a quadratic field. Exact Euclidean polynomial
division at one root, together with an extended-Euclidean identity,
gives `gcd(H,R6,R5)=p-(2r+1)`; conjugation covers its other root.
But `P(2r+1,r)=Q`, so this common root violates P nonzero. Therefore
the two cofactors cannot vanish simultaneously on this part of U.
Leading-coefficient specializations of a resultant can only add
possible exceptional r values; they cannot conceal a finite common
root. The exact gcd and field-fibre calculation remove those possible
extras rather than assuming generic resultant sufficiency.

The entire S-zero branch is retained using

```text
H(2r+1,r)=-(2r-1)^2*(2r+1)*(6r+1)*Q,
P(2r+1,r)=Q.
```

Only `r=-1/6,p=2/3` survives the U conditions. Its actual cofactor
omitting column four is
`1073741824/36472996377170786403`, nonzero. The independent countercheck
also verifies the full first/contact matrix in the eighteen-dimensional
ideal space has rank 17 there. Consequently the contact rank is six
everywhere on U, and the complete containing-quartic space has dimension
`18-11-6=1`.

## 4. Exhaustive complement and fresh ambient boundary evidence

The independent countercheck verifies the precise polynomial identities

```text
H|P=0=-9*(2r+1)^2*Q^2,
H|T=0=-9*(2r-1)^2*(2r+1)^4,
H(p,1/2)=8*(p-8)*(p-2)^2,
H(p,-1/2)=8*p*(p+2)^2.
```

Thus the entire valid complement of U in the b0-nonzero principal chart
consists of the two r-half points and the two Q-root points with
`p=2r+1`, together with the primitive point `p=-2,r=-1/2`. The p-zero
case is nonprincipal; p=r violates basepoint freedom. At the primitive
point all c_i vanish. Its unique primitive correction multiplied by
any degree-one defect shares the zero of that defect, and there is no
additional `H0(O(-3))` correction. It cannot be a genuine positive-defect
finite-flat triple, as in the accepted defective-triple module argument.

The boundary verifier recomputes all 35 ambient monomial columns from
scratch, imposing curve restriction, first normal vanishing, and the
quadratic contact condition in the appropriate exact field. It does
not specialize N at a frame boundary. It asserts the expected ranks
and verifies the complete nullspace, not just a supplied form.

| Genuine parameter fibre | Full 35-column rank | Quartic dimension |
|---|---:|---:|
| `r=1/2,p=2` | 31 | 4, fixed cubic times every linear form |
| `r=1/2,p=8` | 34 | 1 |
| `Q=0,p=2r+1`, both roots, `delta=1` | 34 | 1 |
| `b0=0`, all three cubic-field points | 34 | 1 |
| `r=-1/6,p=2/3` within U, independent frame cross-check | 34 | 1 |

At the node, the four normalized quotient linear forms after dividing
the common cubic C are `x0,x1,x0+x1/2+x2/2,x3`. They span the complete
four-dimensional linear space. If `F*alpha=u,G*alpha=v`, then
`F=C*L,G=C*M` would yield a common ancestor `C*alpha` with linear
multipliers L,M. It is nonzero because u is nonzero, contradicting the
all-stage P-037 theorem. Elsewhere the two quartics would be proportional
in their dimension-one space, contradicting target independence.

These arguments exhaust the principal direction lane for the stated
ancestor problem. They neither decide a higher-degree mate for one
unique carrier nor use an STCI-only second-defect bound.

## 5. Evidence and reproducibility

The open theorem and source are preserved in
[the source-owner's detailed proof](#source-2026-10-08-session-mf6-principal-rank-open-independent-auditmd)
and
[`verify_session_mf6_principal_rank_open_2026_10_08.py`](../computations/verify_session_mf6_principal_rank_open_2026_10_08.py).
Its frozen source hash is
`2fbefebda6723b7d721f0034c0167a2c70a3b79eed01675b99baf453453a9ac8`.
The source owner observed the complete final run exit zero in 82.912
seconds. This audit inspects its reconstruction and exact proof logic
and independently recomputes the frame and coverage checks; it does not
count that owner's run as a second auditor execution.

The fresh
[`coverage-countercheck.py`](../validation/2026-10-08-principal-e1-d1-audit/coverage-countercheck.py)
completed exit zero. Its
[`result`](../validation/2026-10-08-principal-e1-d1-audit/coverage-countercheck-result.json)
binds the actual contact input and source hash, determinant, diagonal,
complement identities, opposite-correction norm, cubic irreducibility,
and S-zero rank. It does not invoke an existing verifier or regenerate
proof inputs.

The frozen all-35-column
[`boundary source`](../computations/verify_mf6_e1_d1_principal_boundaries_2026_10_08.py)
has hash
`9d485f208f61afc495e43bd62054651df37e65c297534ca9930033c44bfea53e`.
Its exact bytes were replayed with `--scope all` in an isolated snapshot;
the run exited zero, and the output and all five field calculations are
retained separately. The actual two-chart
[`residue source`](../computations/verify_mf6_e1_d1_principal_boundary_residues_2026_10_08.py)
was also replayed from exact bytes, with source hash
`02fac92723ff5b5b29c6024e49d8706e4ffe7445431e55cd1761030adaa6dcdb`.
It exited zero. The independent
[`residue-input-comparison.py`](../validation/2026-10-08-principal-e1-d1-audit/residue-input-comparison.py)
then bound all three literal quartics, direction parameters, cocycles,
defect sections and finite corrections to the fresh complete-35-column
output, and derived the raw normal transition from the actual coordinate
change. Its exact checks also passed. The companion's cubic-pole outputs
are separate necessary bounds; they do not strengthen this audit into
an all-mate carrier exclusion.
The complete source/input closure, copied open-proof result/transcript,
fresh boundary and residue results/logs, and both countercheck hashes are in
[`audit-manifest.json`](../validation/2026-10-08-principal-e1-d1-audit/audit-manifest.json).
The snapshot preserves the required `research/computations` and
`research/scratch` layout, so the open proof can also be replayed there.

The source-owner note preserves three earlier checker repairs: one
incorrect free-determinant denominator and two structural-expression
comparisons. The frozen source uses `2^52` and exact expanded polynomial
differences. No altered failed source is treated as passing mathematics.
