# Principal quartic carriers: polynomial compression and an explicit finite mate-candidate locus

Date: 2026-10-09. Fixed smooth rational quartic `C0` in characteristic
zero. This continues the accepted
[complete principal ancestor audit](2026-10-08-session-principal-e1-d1-independent-completeness-audit.md).
The principal common-quartic-ancestor lane is already excluded. The
present question is whether its unique integral quartic carriers can
have a mate of some other degree.

**PROVED exact algebra:** three polynomial contact syzygies of weighted
parameter degrees 9,9,10, and a nonzero explicit determinant candidate
of weighted degree 210. **PROVED NECESSARY REDUCTION, with independently accepted
singleton-fiber geometry:** every nonnormal
carrier with a mate on the stated contact open lies in this determinant's
zero locus. That locus has at most 630 distinct principal parameter
points. Its factors and exact zero list have not been computed. It is
not asserted to equal the locus of all nonnormal carriers.

## 1. Restore the homogeneous direction parameters

Put `A=1+rz`, `B=b+pz`, with parameter weights

```
wt(p)=2, wt(r)=wt(b)=1.
```

Here b is the previously normalized b0. The weighted homogeneous
sextic direction equation is

```
H=8p^3-(64r^2+128rb+16b^2)p^2
  +(96r^4+512r^3b+592r^2b^2+128rb^3+6b^4)p
  -(576r^6+960r^5b+880r^4b^2+544r^3b^3
    +220r^2b^4+60rb^5+9b^6).
```

Its geometrically integral genus-one normalization was previously
proved. The full ambient quartic ideal has the eighteen actual forms
recorded in the accepted contact reconstruction. Their ambient torus
weights are

```
4,3,5,6,7,8,9,4,6,7,8,9,10,10,11,12,12,13.
```

The first normal map has eleven coefficient rows. The quadratic contact
map has twelve. Their combined `23x18` polynomial matrix is homogeneous
with coefficient-column offsets `wi-3` and row offsets

```
1,2,...,11; 10,11,...,21.
```

The actual normal coordinates are

```
x0=1, x1=z, x2=z^3+V, x3=z^4+U+(3/2)zV,
U=-r*m/(p-rb)+(1+rz)y,
V=-p*m/(p-rb)+(b+pz)y.
```

The full matrix specializes at b=1 to the accepted complete contact
matrix. Homogeneity uniquely restores its b powers, so this is an
actual parameter homogenization, not a different conormal frame.

Macaulay2's kernel computation supplied three polynomial generators,
of degrees 9,9,10. Their eighteen coordinates are preserved in
[`mf6-principal-weighted-kernel-2026-10-08.json`](../scratch/mf6-principal-weighted-kernel-2026-10-08.json).
Each generator's coordinate i is homogeneous of degree `D+wi-3`.
The new independent verifier checks every coordinate weight and every
first- and second-contact identity modulo H using SymPy, and checks
that the eighteen forms constitute the complete degree-four ideal
space. Thus **the three actual polynomial syzygies are proved**.
Completeness of the whole kernel module is a separate M2 output; the
candidate theorem needs only the checked first syzygy, not an assertion
that these module generators independently cover every exceptional
fiber.

This avoids the earlier rational normalization by a single ambient
coefficient. That normalization produced denominator divisors of degree
22 in r. The polynomial generators introduce no such denominator
strata. If the chosen polynomial generator vanishes at a parameter,
its entire first-normal octic vanishes and the candidate determinant
vanishes there automatically; that parameter is retained.

## 2. Why a simple first-normal zero cannot be an allowed conductor meeting

Let X be an integral quartic carrier, regular generically along C0,
and suppose a mate has intersection support exactly C0. Let
`nu:S->X` be its finite normalization, with `H_S=nu^*O_X(1)` ample.
The pullback mate's zero divisor has only one reduced component c:
purity excludes any extra isolated zero points over C0, and generic
normality along C0 leaves one curve component. Its finite birational
map to smooth C0 is an isomorphism. Consequently the entire
normalization fiber over each point of C0 consists of that single
point on c. This is a full-support assertion, stronger than choosing
one branch of the inverse image.

If X is nonnormal, its conductor has a curve component upstairs. (For
an integral hypersurface S2, a normalization defect supported only in
codimension two would violate the R1/S2 normality criterion.) The mate
section on each conductor curve is nonzero and belongs to a positive
power of the ample H_S. It must have a zero there. Such a zero lies on
c by full support. Therefore c meets an actual conductor point.

Near its image P on C0, take regular ambient parameters `(x,m,y)` with
C0 given by m=y=0. The quartic's first normal form is `h(x)*m` in the
basepoint-free direction frame. At a nonnormal point h(P)=0. If this
zero were simple, the quadratic Taylor form would contain the nonzero
term `h'(P)*x*m`, so its Hessian rank is at least two.

In characteristic zero, formal elimination of a nondegenerate
quadratic pair writes the completed hypersurface as

```
uv+g(w)=0.
```

If g is nonzero, this is either regular or an isolated normal A-type
hypersurface: its singular locus is isolated, and the hypersurface is
S2. If g=0, its completed normalization has two separate branches
`k[[u,w]]` and `k[[v,w]]`. Excellence of these algebraic local rings
and compatibility of finite normalization with completion imply two
points in the actual normalization fiber. Both alternatives contradict
an allowed nonnormal conductor meeting with a singleton fiber.

Hence the first-normal octic has a multiple zero at some point of C0.
This argument includes a multiple zero at infinity; an affine-only
derivative test would not suffice. It does not say that every multiple
zero is a conductor point, or that every nonnormal carrier admits a
mate.

## 3. The exact determinant candidate

Let G0 be the checked degree-nine polynomial generator. Form its actual
first-normal m coefficient, and multiply by the parameter unit
`d=p-rb`. Write the resulting binary octic as

```
hhat(s,t)=sum(h_j*s^(8-j)*t^j, j=0,...,8).
```

The verifier reconstructs h directly from derivatives of all eighteen
actual quartic forms:

```
d*h = -r*F_U -p*F_V,
F_U=F_x3|C0,
F_V=(F_x2+(3/2)z*F_x3)|C0.
```

After reduction modulo H in p, h_j is a polynomial homogeneous of
weight `11+j`. Its entire nine-coefficient vector is saved, with no
floating-point approximation.

Define the candidate polynomial Delta as the **fixed** 14x14 Sylvester
determinant of the two binary gradients. In the chart s=1 these are

```
partial_s hhat = 8*hhat(1,z)-z*(d/dz)hhat(1,z),
partial_t hhat = (d/dz)hhat(1,z),
```

each padded to the fixed homogeneous degree seven. Fixed padding
retains a common infinity root when h_8=h_7=0. The determinant vanishes
exactly when the binary octic has a multiple root, and also when the
whole chosen octic is zero. No leading coefficient is divided out.

The Sylvester row weights are 18,...,24 and 19,...,25; column weights
are 0,...,13. Hence each nonzero determinant term has parameter weight

```
(18+...+24)+(19+...+25)-(0+...+13)=210.
```

The explicit polynomial is preserved as its actual coefficient vector
and actual 14x14 determinant matrix, rather than an oversized expanded
expression. This is a fully defined polynomial candidate, not an
unspecified resultant to be calculated later.

A modular certificate proves Delta is nonzero on the characteristic-zero
integral curve H. At the good point

```
prime=101, p=4,r=2,b=1,
H=0, pP(p-rb)(2r-b)T!=0,
```

the fixed determinant is nonzero and the actual degree-eight h is
coprime to its derivative. Every source denominator is a power of two.
If Delta were divisible by the primitive integer H over QQ, clearing
those powers of two and applying Gauss's lemma would make the same
identity valid modulo 101. The nonzero exact evaluation rules this out.
This is an algebraic nonvanishing certificate in characteristic zero;
it is not an extrapolation from a numerical plot or random examples.

On the accepted contact open, a nonzero G0 is the unique containing
quartic up to scalar. Its scalar parameter normalization and d are
units and preserve root multiplicities. If G0 or its first normal
coefficient is zero, Delta already vanishes and retains that fiber.
Thus the singleton-fiber lemma forces every hypothetical nonnormal
STCI carrier on this open into Delta=0.

## 4. A rigorous finite candidate bound

The sextic H and Delta have no common component. A bound follows using
an ordinary projective-plane cover rather than a weighted intersection
formula. Substitute `p=a^2`. This gives plane equations of degrees six
and 210. No irreducible component of the lifted sextic can be contained
in the lifted Delta: every component maps dominantly to the integral
weighted sextic, on which Delta is nonzero. Bezout therefore bounds the
lifted intersection length by 1260.

Every principal weighted parameter point has p nonzero and has two
distinct plane lifts `[a:r:b]` and `[-a:r:b]`. The sextic has no point
with r=b=0, since there H=8p^3. Thus the two lifts cannot be identified
by projective scaling. Consequently there are at most **630 distinct
principal parameter points** in this candidate locus. This bound keeps
all chosen-generator base fibers and all infinity multiple roots.
It is not asserted to be sharp.

The actual contact-frame complement remains separately governed by the
accepted complete boundary audit. The zero list of Delta has not been
computed, nor have its candidate carriers been classified. A complete
finite necessary locus differs from an exact nonnormal locus and from
a proof that its remaining carriers have no mate.

## 5. Repairs and failed leads retained

The first homogeneous M2 module experiment used the wrong signs for
free-module grading shifts. It printed `isHomogeneous=false`, with
mislabelled degrees 29,29,30. The underlying polynomial vectors were
unchanged; correcting the shifts gave `isHomogeneous=true` and their
actual degrees 9,9,10. Both transcripts are retained. The independent
SymPy weight and syzygy checks use the corrected degrees.

A second lead sampled r=0 modulo 13 and 23. Those reductions have
repeated first-normal roots and apparent triple-point jets; this was
initially suggested as evidence for a characteristic-zero nonnormal
r=0 fiber. Exact cubic-field computation contradicts that suggestion:
the characteristic-zero r=0 quartics have finite projective singular
locus. All three conjugates are geometrically integral and normal.
Thus the modular small-prime observations are bad-reduction phenomena,
not proof of a characteristic-zero singular curve. Their transcripts
and the exact correction are preserved. The nonzero Delta certificate
uses a directly checked good point at 101.

The universal STCI problem, unrestricted characteristic-zero C0, and
the exact finite principal nonnormal parameter subset remain open.

## 6. Frozen source and completed checks

The standalone
[`verify_session_mf6_principal_weighted_candidate_2026_10_09.py`](../computations/verify_session_mf6_principal_weighted_candidate_2026_10_09.py)
completed with exit zero in 24.132 seconds, at source SHA-256
`78ed372321bb99c81003892e30ca48a253b56702d0a00e05c5347e7a93e17370`.
It checks the complete actual quartic ideal, binding of the full weighted
matrix to the accepted b=1 contact reconstruction, all three polynomial
syzygies, the actual first-normal coefficient, every determinant entry's
weight, and the nonzero fixed Sylvester determinant **22 modulo 101**.
The source and exact input hashes, actual nine-coefficient octic, full
14x14 matrix and scope are in
[`session-mf6-principal-weighted-candidate-2026-10-09.json`](../scratch/session-mf6-principal-weighted-candidate-2026-10-09.json),
with the
[terminal transcript](../scratch/session-mf6-principal-weighted-candidate-2026-10-09.out).
The determinant remains unexpanded; none of the finite candidate fibers
has been asserted to be exhausted.

The corrected r=0 computation is independently self-contained in
[`verify_session_mf6_principal_rzero_normality_2026_10_09.m2`](../computations/verify_session_mf6_principal_rzero_normality_2026_10_09.m2).
Its field polynomial is `8p^3-16p^2+6p-9`, irreducible modulo five
(the values at 0,...,4 are 1,4,3,1,1). Its literal quartic is bound to
the checked degree-nine generator restricted at r=0 in
[the input record](../scratch/session-mf6-principal-rzero-normality-input-2026-10-09.json).
The exact M2 check completed with exit zero and asserted Jacobian cone
dimension one, of degree fifteen; its
[terminal transcript](../scratch/session-mf6-principal-rzero-normality-2026-10-09.out)
is preserved. Dimension survives constant-field extension. Reducible or
nonreduced projective quartics have a curve of singular points, so this
also proves geometric integrality. The hypersurface S2 property and
finite singular locus prove geometric normality of all three conjugates.
The accepted normal-carrier theorem excludes their mates in every degree.

No canonical frontier file was edited. The
[independent geometric audit](2026-10-09-session-mf6-weighted-candidate-geometric-audit.md)
accepts the actual conductor meeting, Hessian argument, two-branch
contradiction, and the 630 bound conditional on the exact inputs. The
exact syzygy, determinant and r=0 certificates have their completed local
runs and are ready for independent isolated replay. No candidate-zero
classification is thereby asserted.
