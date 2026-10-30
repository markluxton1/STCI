# October 9 historical mathematics

Full original source text preserved. Hypotheses, counterexamples, unsuccessful arguments, and open questions retain their source status; no new independent audit or theorem promotion.

---

## Source: 2026-10-09-session-mf6-principal-weighted-candidate.md

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


---

## Source: 2026-10-09-session-mf6-weighted-candidate-algebra-independent-audit.md

# Independent algebra and Bezout audit of the principal MF6 candidate

Date: 2026-10-09. Auditor: `verification`. Status: **PROVED HERE / independently accepted necessary finite reduction**, on the explicitly retained principal contact open. The finite zero list, exact nonnormal locus, and all-mate exclusion at those zeros remain unresolved by this reduction.

## 1. Accepted statement and its scope

Use weighted parameters (p,r,b) of weights (2,1,1), and the integral weighted sextic H from the [owner proof](2026-10-09-session-mf6-principal-weighted-candidate.md). Put

    d=p-rb,
    P=2p+12r^2+16rb+9b^2,
    T=2p-4r^2-4rb-b^2,
    U=p P d (2r-b) T.

On H=0,U!=0, the accepted complete contact-rank audit gives a one-dimensional space of containing quartics for the principal e=1,d2=1 triple. The checked first polynomial generator G0 either spans that space or vanishes at a parameter. Its actual first-normal binary octic, multiplied by d, defines a fixed 14-by-14 binary-gradient Sylvester determinant Delta. This audit accepts:

* Delta is a completely specified homogeneous polynomial of weighted degree 210, by its preserved actual matrix.
* Delta is nonzero on the geometrically integral weighted curve H.
* Every nonnormal carrier with an STCI mate for C0 on this contact open lies in Delta=0, using the separately accepted geometric multiple-zero necessity.
* There are at most 630 distinct principal weighted parameter points in this necessary locus.

Zero chosen-generator fibers and zero first-normal vectors remain in the candidate locus. The result is not a description of the exact nonnormal locus, a factorization or enumeration of Delta's zeros, or an exclusion of every mate there. Contact-frame complement fibers retain their independent boundary proofs.

## 2. Exact source and input binding

Owner source SHA256 is `78ed372321bb99c81003892e30ca48a253b56702d0a00e05c5347e7a93e17370`. Its three exact inputs are:

| Input | SHA256 |
| --- | --- |
| `derive-mf6-principal-weighted-kernel-2026-10-08.json` | `0da6eff927a635a81179ce631468e9d4f3fc89a1c78af1c7a6a8cd6cc81fe85d` |
| `mf6-principal-weighted-kernel-2026-10-08.json` | `4889f20b60fa094cde47992342701ebdf29a98413fc216b20f971550331cd9db` |
| `session-mf6-e1-principal-contact-2026-10-08.json` | `bc32db62b6d87e15300168a47f50d6bf3cd952d0d19b60ad52fc5ae8cdfa9818` |

The last is the contact reconstruction already bound by the [complete principal audit](2026-10-08-session-principal-e1-d1-independent-completeness-audit.md). All three inputs give exactly the same eighteen literal ambient quartic forms. The owner verifier proves each vanishes on actual C0, proves their ambient coefficient rank eighteen, and checks the thirty-five quartic monomials restrict to all z-degrees 0 through 16. Thus the full degree-four ideal kernel has dimension 35-17=18, and these forms constitute the complete space; this is not a generator-coordinate substitute for ambient forms.

The full 23-by-18 contact matrix specializes at b=1 to the accepted eleven first-contact rows and twelve second-contact rows. Its row offsets are exactly 1 through 11, then 10 through 21; its column offsets are exactly 1,0,2,3,4,5,6,1,3,4,5,6,7,7,8,9,9,10. Homogeneous polynomial extension of a fixed offset is uniquely determined by its b=1 specialization: a monomial p^i r^j has the unique possible b-exponent w-2i-j. The owner checks these entry weights, each coordinate of the three degrees 9,9,10 generators, and all sixty-nine contact identities modulo H.

The root separately performed the fresh isolated complete owner replay, exit zero in 25.463 seconds. This audit inspected that source and performed the smaller independent coefficient/matrix reconstruction described below; it did not duplicate the three large contact-syzygy calculations. Completeness of the kernel module over the entire parameter scheme is not needed for the candidate argument. The accepted pointwise rank-one conclusion on U!=0 and one actual checked polynomial syzygy suffice.

## 3. Independent actual normal-coefficient reconstruction

The new self-contained bounded audit source is [audit_session_mf6_weighted_candidate_2026_10_09.py](../computations/audit_session_mf6_weighted_candidate_2026_10_09.py), SHA256 `a513320aeeed37260151d209cd2d232ac321edb892d647b22395a06cb45a1ac8`. It asserts the three input hashes above, the frozen owner source hash, and the binding of the owner saved result.

It independently differentiates the eighteen actual forms and contracts the first polynomial generator to produce F_U and F_V along C0, in the balanced frame

    U=-r m/d+(1+rz)y,
    V=-p m/d+(b+pz)y.

With A=1+rz and B=b+pz, it verifies the full polynomial identities modulo H

    A F_U+B F_V=0,
    hhat=-r F_U-p F_V,
    d F_U=B hhat, d F_V=-A hhat.

It reconstructs all nine coefficients h_j of hhat, checks their exact equality with the saved vector, and checks that no coefficient of degree greater than eight survives modulo H. The two latter frame identities also explain why hhat is the actual common first-normal binary octic: F_U=B h and F_V=-A h, with hhat=d h and d a unit on the declared open. The homogeneous linear direction A,B is basepoint free when d!=0. This controls both curve charts rather than only an affine derivative chosen in a frame with a zero.

Each h_j is homogeneous of parameter weight 11+j. The independently rebuilt fixed matrix agrees entry by entry with the saved matrix. Its first seven row weights are 18 through 24; its other seven row weights are 19 through 25; its column weights are 0 through 13. Every determinant term therefore has weight

    sum(18,...,24)+sum(19,...,25)-sum(0,...,13)=210.

No leading coefficient is cancelled. A control octic s times the product of seven distinct (t-j s) has a simple infinity root and nonzero gradient determinant. A control octic s^2 times the product of six distinct (t-j s) has a double infinity root and zero determinant. A zero nine-coefficient vector gives the zero fixed matrix and zero determinant. These exact controls confirm the intended behavior of the fixed degree-seven padding.

## 4. Characteristic-zero nonvanishing from the exact modular witness

The independently reconstructed sample at (p,r,b)=(4,2,1) modulo 101 has

    H=0, U=16!=0,
    (h_0,...,h_8)=(26,6,34,38,38,31,17,81,16),
    det(fixed Sylvester matrix)=22!=0.

The sample octic has degree eight and is coprime to its derivative. The modular determinant is exact finite-field arithmetic, and the sample is on H and in the declared contact open.

The audit proves H is a primitive integer polynomial, with leading coefficient 8 in p, and checks that every rational coefficient in the actual determinant matrix has denominator a power of two. Consequently Delta lies in Z[1/2][p,r,b]. If Delta vanished identically on the irreducible characteristic-zero H, H would divide Delta over Q. Clear only a power of two to make an integer polynomial; the primitive polynomial H then divides it in Z[p,r,b] by Gauss's lemma. Reducing that identity modulo 101 is legitimate. Since 101 does not divide the cleared power of two and the sample lies on H, it would force the sample determinant to be zero, contrary to 22. Thus Delta is nonzero on H in characteristic zero.

Geometric integrality of H is an accepted preceding theorem, not inferred from the single modular point. Its explicit certificate in `verify_mf6_e1_d1_principal_curve_2026_10_08.py` rules out a root of the cubic H(p,r,1) over the algebraic closure's rational function field: integrality makes a rational root polynomial in r, leading-degree comparison bounds its degree by two, and the coefficient equations for p=a r^2+c r+d have Groebner ideal (1). A cubic with no such root is absolutely irreducible. Homogenization introduces no b factor, since H contains 8p^3. The prior genus-one model is compatible with this stronger irreducibility argument but is not needed for Bezout.

## 5. Specialization and exceptional-generator qualification

At a point of U!=0 where G0 is nonzero, it lies in the complete contact kernel and hence is a nonzero scalar multiple of the unique actual quartic. That scalar and d do not change first-normal root multiplicities. The geometric necessity proved by the [separate audit](2026-10-09-session-mf6-weighted-candidate-geometric-audit.md) forces a multiple projective root, so Delta vanishes.

If G0 specializes to zero, its first-normal vector specializes to zero, and Delta vanishes automatically. If G0 remains nonzero but its entire first-normal vector is zero, the same conclusion holds. No exceptional parameter was removed by dividing by a coefficient of G0, by a leading coefficient h_8, or by a rational scalar chosen on a smaller chart. The basepoint-free and contact units are the explicit U factors; parameters outside that open are handled separately, not silently added to this candidate theorem.

## 6. Ordinary-plane cover and the 630 bound

The map

    pi:P2 -> P(2,1,1), [a:r:b] -> [a^2:r:b]

is the finite quotient by a -> -a; equivalently its invariant graded ring is k[a^2,r,b], with generator degrees 2,1,1. Pullback gives ordinary homogeneous equations of degrees six and 210. Even if the lifted sextic splits, each of its irreducible curve components maps onto the integral H: finiteness prevents a curve from being contracted, and the only dimension-one closed image in H is H itself. Since Delta is nonzero on H, none of these components is contained in the pulled-back Delta. The two plane curves therefore have no common component.

Bezout bounds their scheme intersection length by 6*210=1260. A principal point has p!=0. On H it cannot have r=b=0 because H would then be 8p^3. It consequently has two distinct plane lifts [a:r:b] and [-a:r:b]: scaling would have to fix a nonzero r or b and hence be one, while a!=0 and characteristic zero forbid identifying the signs. Thus every distinct principal candidate consumes at least two distinct intersection points, proving at most 1260/2=630 candidates. Intersection multiplicities can only strengthen this upper bound; no reducedness of the intersection or irreducibility of its lift is assumed.

The bound concerns distinct weighted parameter points in the necessary locus, not 630 constructed quartics or 630 proven nonnormal fibers. Normal carriers, singularities away from C0, and generator base fibers may all occur among zeros; the exact zero list remains uncomputed here.

## 7. Durable execution record

The bounded independent source completed in isolation with exit zero, wall time 7.909 seconds. Its log and result hash is `061217ff3b5ecc72aeec7bd5aa0791a3b7299ac43a8865f35f2f1529b1743ce2`. The original sources and all four input/result artifacts were unchanged. Full snapshots, source hashes, accepted-input hashes, exact sample coefficients, matrix agreement, and the infinity controls are preserved under `research/validation/2026-10-09-mf6-weighted-candidate-audit/`.

This is one new bounded countercheck execution in addition to the central owner replay. It does not change the status of the universal STCI question and does not edit canonical frontier files.


---

## Source: 2026-10-09-session-mf6-weighted-candidate-geometric-audit.md

# Independent geometric audit of the principal mate-candidate reduction

Date: 2026-10-09. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted** for the geometric necessity.
The exact polynomial reconstruction and modular nonzero certificate
are separate computational obligations, not certified by this note.

Owner source:
[Principal weighted candidate](2026-10-09-session-mf6-principal-weighted-candidate.md),
especially section 2. This bounded audit checks the actual conductor
meeting, Hessian, formal branches, and the resulting necessary
multiple-root condition. No canonical frontier documents were edited.

## 1. A nonnormal mate carrier necessarily meets its conductor

Let X subset P3 be an integral quartic containing the fixed smooth
rational quartic C0. It is automatically regular at the generic point
of C0: a general integral plane quartic would otherwise have four
distinct singular points, contradicting arithmetic genus three.
The full argument is appended to the
[sectional-genus audit](2026-10-09-session-normalization-genus-zero-independent-audit.md).

Suppose a form G of degree b>0 has intersection support exactly C0.
For the finite normalization nu:S->X, the accepted full-support
argument gives a unique reduced smooth curve c isomorphic to C0,
div(nu^*G)=b c, and singleton entire normalization fibers above C0.
Normality of S supplies the purity needed to exclude isolated extra
zero components; no smoothness of the whole S is assumed.

If X is nonnormal, it has a codimension-one normalization defect.
Indeed X is a hypersurface and satisfies S2, so a defect supported
only in codimension two would leave R1 and force normality by Serre's
criterion. The actual conductor consequently has a curve component
upstairs E. It is distinct from c, since X is generically regular
along C0. The section nu^*G restricts generically nonzero to E, and
its line bundle is a positive power of the ample nu^*O_X(1).
On an integral projective curve such a section must have a zero;
otherwise it would trivialize a line bundle of positive degree.
Its zero lies on c by full inverse support. Thus there is a point
P in C0 which is actually nonnormal on X and whose normalization
fiber is nevertheless a singleton.

This argument uses an actual conductor curve, not a curve in a
Jacobian scheme or an arbitrarily chosen inverse-image branch. It
also remains valid if the point of S above P is singular.

## 2. A simple first-normal zero gives a nondegenerate quadratic pair

On the stated basepoint-free contact open, use regular ambient
parameters (x,m,y) with C0=(m=y=0) and write the first-normal term
of the actual quartic equation as h(x)m. At a nonnormal point P
the hypersurface is singular, so h(P)=0. Translate x(P) to zero.
If h has a simple zero at P, its quadratic Taylor part has the form

    a x m + A m^2 + B m y + C y^2,       a=h'(P)!=0.

There is no x^2 term because the equation vanishes on C0, and no
x y term because the first-normal y coefficient vanishes identically
in this direction frame. The x,m principal minor of the symmetric
quadratic matrix has determinant -a^2/4. Hence the Hessian rank is
at least two, independently of the other quadratic terms.

The basepoint-free condition on the direction frame is material:
it makes m,y regular normal parameters at every point where this
argument is used. A first-normal coefficient taken in a frame with
a pole or a zero would not justify this calculation. On the second
curve chart the same local argument applies, so an infinity point
is covered by the homogeneous multiple-root test.

## 3. Hessian rank at least two contradicts the allowed meeting

In characteristic zero, the formal splitting lemma puts a hypersurface
with a nondegenerate quadratic pair into the form

    Ahat = k[[u,v,w]]/(uv+g(w)).

For completeness, the two formal partial derivatives in the pair
variables have an invertible Jacobian. The formal implicit-function
theorem shifts their critical section to zero, and successive
formal coordinate changes eliminate higher terms involving that
pair. Completeness makes these degreewise changes converge; the
remaining function involves only w. This is the formal Morse argument
used here, not an assertion about an arbitrary tangent-only model.

If g is nonzero, write it as w^r times a unit and absorb the unit by
a formal coordinate change. At the singular point r>=2, the ring
k[[u,v,w]]/(uv+w^r) is a domain with isolated singular locus: its
partials are v,u,r w^(r-1). It is a hypersurface, hence S2, and is
regular in codimension one, hence normal. Normality of the completion
implies normality of the original local ring by faithful-flat descent;
see [Stacks, Lemma 15.44.7](https://stacks.math.columbia.edu/tag/07NU).
This contradicts P being an actual nonnormal conductor point. A
regular formal model would of course give the same contradiction.

If g=0, the completion has precisely two minimal branches, u=0 and
v=0, with normalization

    k[[u,w]] x k[[v,w]].

The algebraic local ring is excellent, since X is of finite type
over k. For an excellent local ring, the number of branches agrees
with that of its completion, and for a domain these branches count
the maximal ideals of its finite integral closure. Thus the actual
normalization fiber at P has two points. This follows directly from
[Stacks, Lemma 15.110.8](https://stacks.math.columbia.edu/tag/0C27).
It contradicts the singleton full fiber required by the mate.

Neither formal alternative is compatible with the conductor meeting
in section 1. Therefore the actual first-normal coefficient has a
multiple zero at some point of C0.

## 4. Accepted determinant implication and computational boundary

The geometric conclusion is: every hypothetical nonnormal mate carrier
on the specified contact open has a multiple zero of its actual
first-normal binary octic. If the checked chosen polynomial generator
is nonzero and spans the unique quartic carrier there, multiplication
by its parameter scalar and the frame unit d preserves multiplicities.
If that generator or its entire coefficient vector vanishes, its
binary-gradient determinant vanishes automatically. Thus the owner's
fixed binary-gradient Sylvester polynomial Delta gives a necessary
condition Delta=0, provided the claimed coefficient reconstruction
and spanning statement are independently certified.

The arithmetic argument for the stated bound is also valid conditional
on those exact inputs: H is an integral weighted sextic, Delta has
weight 210 and is nonzero on H. The finite cover

    P2 -> P(2,1,1),       [a:r:b] -> [a^2:r:b]

lifts the equations to ordinary degrees six and 210. Every irreducible
component of the lifted sextic dominates H, so no component lies in
the lifted Delta. Bezout bounds the intersection length by 1260.
At a principal point p!=0 with (r,b)!=(0,0), there are two distinct
projective lifts: [a:r:b] and [-a:r:b] cannot differ by scaling since
at least one of r,b is nonzero and a is nonzero. Hence at most 630
distinct principal points lie in that necessary candidate locus.

This audit does not independently replay the degree-210 determinant
weights, all eighteen ambient polynomial columns, or the modular
nonvanishing certificate. Their computational audit must be reported
separately. The bound is a bound on a necessary candidate locus, not
the exact nonnormal parameter set and not a survivor exclusion.

`git diff --check` passed after this independent geometric note was saved.


---

## Source: 2026-10-09-session-normalization-genus-zero-independent-audit.md

# Independent audit: sectional genus zero and the singular cone

Date: 2026-10-09. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted**, with the scope below.
This is a bounded proof audit; no canonical frontier documents were edited.

Owner proof:
[Normalization sectional genus zero](2026-10-09-session-normalization-sectional-genus-zero.md),
sections 1--6. Accepted earlier inputs are the full inverse-support
reduction, the all-scroll theorem, the all-Veronese theorem, and the
local-unit differential lemma. The vanishing and minimal-degree
classification inputs are identified explicitly below.

## 1. Exact scope and definition of sectional genus

Let k be algebraically closed of characteristic zero, X subset P3 an
integral quartic, nu:S->X its finite normal normalization, and
H=nu^*O_X(1). Assume X is regular at the generic point of the smooth
rational quartic C under consideration. Under a mate of degree b,
the full-support reduction gives a unique smooth integral c isomorphic
to C and

    div_S(nu^*G)=b c,       b c~bH,

with every normalization fiber above C a singleton. It does not assert
that c itself is Cartier at a singular point of S.

Define pi as the genus of a general divisor from the original four
pulled-back ambient coordinate sections. They are basepoint-free and
their morphism is finite. Since S is a normal surface, Sing(S) is
finite; a general member avoids it. Characteristic-zero Bertini on
S_reg gives smoothness, and the irreducibility theorem for a
basepoint-free system with two-dimensional image gives integrality.
This is a smooth integral curve whose finite birational image is a
general plane quartic, so it is that plane curve's normalization.
There is no circular assumption that the complete |H| is already
six-dimensional.

Consequently 0<=pi<=3, and pi<=2 if X is nonnormal: its codimension-one
singular support meets a general plane and produces a singular plane
quartic with positive normalization defect. In the normal case a
general plane avoids the isolated singular locus and has pi=3.

## 2. Vanishing on the resolution is valid without rationality

Choose a smooth projective resolution sigma:M->S and put L=sigma^*H.
The divisor is nef and big, with L^2=4, regardless of the rationality
or singularity type of S. A general hyperplane divisor avoids the
exceptional locus, so its strict transform Y has class L and genus pi.
Adjunction gives K_M.L=2pi-6.

If pi=0 then (K_M+L).L=-2. Since L is nef, no effective divisor can
have negative intersection with L, so h0(K_M+L)=0. The standard
characteristic-zero Kawamata--Viehweg theorem applies on the smooth
projective M to the nef and big Cartier divisor L and gives
Hi(K_M+L)=0 for i>0. Surface Riemann--Roch therefore gives

    0=chi(K_M+L)=chi(O_M)+(K_M+L).L/2=chi(O_M)-1.

The same nef-intersection argument with K_M.L=-6 gives p_g(M)=0.
Thus chi(O_M)=1 forces q(M)=0. Normality gives sigma_*O_M=O_S, and
the low-degree Leray sequence injects H1(O_S) into H1(O_M), proving
H1(O_S)=0. Rational singularities were not assumed, and no assertion
R1 sigma_*O_M=0 is required for this injection.

For a primary-source consistency check, Proposition 2.6 of
[Horing, The sectional genus of quasi-polarised varieties](https://math.univ-cotedazur.fr/~hoering/articles/a12-sect-genus.pdf)
uses this nef-big vanishing and Riemann--Roch mechanism. Its complex-field
Theorem 1.2 is not needed: the direct surface proof uses standard
characteristic-zero vanishing over the stated field.

## 3. The complete map and classification are exhaustive

The exact sequence on S of a general smooth Y is

    0 -> O_S -> O_S(H) -> O_Y(H) -> 0.

Here Y=P1 and deg(H|Y)=4. Since H1(O_S)=0, it gives h0(H)=1+5=6.
The complete basepoint-free system defines phi:S->T subset P5.
It is finite: H is ample, so no positive-dimensional fiber can contain
a curve of H-degree zero. It is birational because the original
four-section map factors through it and already has k(X)=k(S).
More explicitly, the projection center is disjoint from T, as the
four sections have no common zero on S; hence
k(X) subset k(T) subset k(S) are equal. Nondegeneracy is automatic
for the image of a complete six-dimensional system. The finite
birational map gives deg(T)=H^2=4 and codim(T,P5)=3.

[Eisenbud--Green--Hulek--Popescu, Small Schemes and Varieties of Minimal Degree](https://www.math.stonybrook.edu/~sorin/eprints/2-regular.pdf),
Theorem 0.1, gives the classification over an algebraically closed
field. For a degree-four surface in P5 it yields exactly S(2,2),
S(1,3), S(0,4), and the Veronese surface. They are respectively
(F0,C+2f), (F2,C_min+3f), the rational-normal-quartic cone, and
(P2,O(2)). The first, second, and fourth are smooth. The cone is
normal: its homogeneous ring is a polynomial extension of the normal
fourth Veronese subring of k[s,t]. Thus all four T are normal.
Finite birational phi to normal T is an isomorphism, proving the
claimed exhaustive classification of the polarized normal S.

The qualification “normalization is smooth” is not introduced into
the reduction. The one singular minimal-degree possibility remains
explicitly in the list.

## 4. The singular cone exclusion passes in every mate degree

Let sigma:F4->S(0,4) contract its negative section E, with E^2=-4,
and let f be a ruling fiber. The polarization pulls back to L=E+4f.
Removing E and the vertex v identifies the two remaining smooth open
sets. Weil localization gives

    Cl(S)=Pic(F4)/Z[E]=Z[f],       [H]=4[f].

This group is torsion-free. The mate identity b(c-H)~0 therefore
makes c~H as Weil divisors, so c is Cartier. If c passed through v,
the principal quotient defining its regular one-dimensional local
ring would give embdim(O_S,v)<=2, forcing that surface local ring to
be regular. This contradicts the singular vertex. Equivalently, the
vertex has embedding dimension five and a principal quotient can
decrease it by at most one. Thus c avoids v.

Its strict transform is a smooth ruling section c#~E+4f, disjoint
from E, meeting each fiber once away from E. Choose the original
four sections so that three vanish at v and the fourth does not.
They define a cone projection: the three sections are binary
quartics q0,q1,q2, and on a ruling the remaining section is a
nonzero vertex coefficient plus a binary quartic. The q_i have no
common zero; otherwise a ruling would be contracted (indeed a point
on it would be a base point), contrary to finiteness.

They define beta:P1->B subset P2. Birationality of nu forces beta
birational, and beta^*O_B(1)=O_P1(4) makes B an integral rational
plane quartic. Every source ruling maps isomorphically to the
corresponding image ruling; only their common vertex is collapsed
on F4, and it has already been excluded from c.

If beta has a fiber containing distinct p1,p2, take the image of the
unique c#-point on the first ruling. It is a nonvertex point and has
another preimage on the second ruling. The entire inverse-support
condition forces that preimage onto c#, contradicting singleton
fibers or nu|c being an isomorphism. Thus beta must be unibranch
everywhere.

The rational plane quartic B is nevertheless singular, since its
arithmetic genus is three. At a singular point with one normalization
preimage, d beta vanishes. In formal local plane coordinates, any
nonzero first derivative would give a uniformizer with a formal
inverse, making the complete branch ring k[[t]] and the point regular.

Away from the vertex the cone map has local form

    (t,z) -> (z,beta_1(t),beta_2(t)).

Consequently its differential has rank one along the ruling above
that unibranch singularity. The ruling meets c at a point where S
is smooth. The entire pulled-back mate there is u f_c^b with u a
unit, so the independently accepted local-unit differential lemma
contradicts immersion of nu|c. This excludes the cone in every
positive mate degree. It imports no arbitrary-degree cone theorem.

## 5. The exceptional correction also passes

The owner's further identity is valid and retains the singular
normalization boundary. On any resolution, the actual effective
Cartier pullback of b c gives

    sigma^*(b c)/b=c# + Z numerically equivalent to L,

where Z is effective rational exceptional, with denominators dividing
b. The strict transform c# maps properly birationally to smooth c.
A dominant map of integral curves cannot have a positive-dimensional
fiber; otherwise the whole source curve would map to that point.
It is therefore quasi-finite, hence finite, and normality of c makes
the finite birational map an isomorphism. In particular c# is smooth.

Exceptional orthogonality L.Z=0 gives

    q=-Z^2=c#.Z>=0,       c#^2=4-q.

Adjunction to c# together with K_M.L=2pi-6 then gives exactly

    q+K_M.Z=2pi.

All intersections take place on smooth M; no Q-Gorenstein condition
on S is needed. For ADE singularities K_M is orthogonal to all
exceptional curves, giving q=2pi. At any singular point of S lying
on c, its local Weil class is nonzero torsion of order dividing b:
zero class would make c Cartier there and force S regular by the
principal-quotient argument.

## 6. Accepted conclusion and retained boundary

Combining this exhaustive pi=0 reduction and cone proof with the
accepted F0/F2 and P2 projection theorems excludes every pi=0
normalization in every mate degree. If c avoids Sing(S), it is
Cartier and its pullback on the resolution is c# with no exceptional
correction; c# is numerically L, and adjunction forces pi=0.

Therefore, under the stated generic-regularity hypothesis, any
remaining nonnormal quartic mate must have

    pi in {1,2},       c intersect Sing(S) nonempty.

In particular every integral quartic with smooth normalization is
excluded under these hypotheses. This does not cover carriers
singular at the generic point of C, other carrier degrees, or all
positive-sectional-genus singular normalizations. The singular local
countershields remain pertinent: b c may be Cartier while c is not.
No universal STCI resolution follows from this audit.

`git diff --check` passed after this independent proof was saved.

## Addendum: generic regularity along C0 is automatic for integral quartics

Status: **PROVED HERE / independently accepted**. The generic-regularity
qualifier in the earlier statement can be removed for the fixed C0.

Suppose an integral quartic X=V(F) were singular at the generic point
of the smooth degree-four curve C0. In characteristic zero the
hypersurface Jacobian criterion implies that every homogeneous partial
derivative of F vanishes at that generic point, hence on the entire
integral C0. Choose a general plane Pi. Two nonempty open conditions
can be imposed simultaneously: Pi cuts C0 transversely in four distinct
points, and Y=X intersect Pi is an integral plane quartic. The latter
is the standard Bertini irreducibility and reducedness conclusion
for the hyperplane system of an integral embedded surface; it does
not require X to be normal or smooth. See
[Stacks, Bertini theorems](https://stacks.math.columbia.edu/tag/0G4C).

At each of those four points, every derivative of the plane quartic
equation is a linear combination of the ambient partial derivatives
of F and therefore vanishes. Thus Y has four distinct singular points.
For its normalization Ybar, the normalization exact sequence gives

    3=p_a(Y)=g(Ybar)+sum_P delta_P(Y).

Each singular point of an integral plane curve has delta_P>=1, and
g(Ybar)>=0. Four such points contradict this identity. Therefore X
is regular at the generic point of C0.

Neither nonplanarity of C0 nor normality of X is used. The general
plane is chosen not to contain C0, and all four intersections are
proper, reduced, and distinct. The same argument, simultaneously
avoiding intersections and exceptional points of the finitely many
singular curve components, bounds the total degree of the reduced
one-dimensional singular support of any integral quartic by three.

Consequently the combined accepted theorem has the unqualified form:

**Every integral quartic in P3 containing C0 whose normalization is
smooth is excluded as a carrier for a set-theoretic complete-intersection
mate of every positive degree, over an algebraically closed field
of characteristic zero.**

More generally, every remaining nonnormal integral quartic carrier
with a hypothetical mate has normalization sectional genus pi in
{1,2}, and its unique smooth lift c meets Sing(S). There is no separate
generically-singular-along-C0 integral-quartic lane. Other carrier
degrees and the unrestricted STCI problem remain outside this result.


---

## Source: 2026-10-09-session-quadratic-conductor-power-descent-independent-audit.md

# Independent audit of exact quadratic-conductor power descent

Date: 2026-10-09. Author: `quadratic_torsion_exact_audit`, for
`quadratic_conductor_power_descent`.

Status: **PROVED HERE, independent audit accepted under the stated
hypotheses.** This audit checks the algebraic criterion in
`2026-10-09-session-quadratic-conductor-power-descent.md`. It does not
assert that any of the remaining conductor data occurs on a del Pezzo
surface containing the fixed rational quartic. It gives no STCI
exclusion or bound on all possible mate degrees.

## 1. Hypotheses and verdict

Let k be algebraically closed of characteristic zero, let Gamma be an
actual plane conic, and put M=O_Gamma(1). Permit a smooth conic, two
distinct lines, and the full plane double line. Let

    E=p_*O_D=O_Gamma direct_sum M^(-1),
    w^2=delta,       sigma(w)=-w,
    q=m+w ell,

where m is a section of M^2, ell a section of M, and delta a section
of M^2. Assume multiplication by q is injective on O_D, with its
line-bundle twist understood. Define

    Cycl={((1+zeta)/(1-zeta))^2:
          zeta a root of unity in k, zeta != 1,-1}.

For a smooth conic or an entire double line, some positive power of q
is invariant if and only if either

    m ell=0 on the entire Gamma,

or

    m^2=rho delta ell^2 on the entire Gamma for some rho in Cycl.

For two distinct lines the same criterion is applied to each line,
with independent constants and a common multiple of their power
orders. The parent's criterion, including its nilpotent data and
its coefficient-rank consequences, is correct.

## 2. Independent necessity proof in the generic Artin rings

For an irreducible reduced conic or a reduced line, its generic ring
is a field K. For the plane double line its generic ring is
T=K[epsilon]/(epsilon^2). After trivializing M, the generic algebra
is the finite Artin algebra

    E_T=T[w]/(w^2-delta).

The nonzerodivisor q becomes a unit in E_T. Thus, if q^n is
invariant, the element t=sigma(q)/q is well defined and satisfies
t^n=1.

In a local Artin algebra over K, every solution of t^n=1 is an
actual constant root of unity in k, with no nilpotent correction.
Indeed T^n-1 is a product of distinct factors T-zeta. If the residue
of t is zeta, every other factor evaluated at t is a unit, forcing
t-zeta=0 in the Artin ring itself. The residue-field solution is in
k because k already contains all roots of T^n-1. This argument
works even when the residue field is a nontrivial extension of K.

The generic quadratic algebra has exactly the following cases.

| Residue of delta in K | Generic algebra and involution | Consequence |
| --- | --- | --- |
| Nonzero nonsquare | One local Artin factor with quadratic residue field; sigma preserves that factor | t=zeta and sigma(t)=t^(-1) force zeta=+1 or -1. Hence ell=0 or m=0, as exact identities in T. |
| Zero | One local Artin factor with residue field K; sigma induces the identity on that residue field | The residue of sigma(q)/q is 1, so t=1 exactly. Hence ell=0 in T. |
| Nonzero square | Two Artin factors interchanged by sigma | A chosen square root s of delta lifts across epsilon because 2s is a unit, so E_T=T x T. Then t=(zeta,zeta^(-1)). |

In the last row, zeta=+1 or -1 again yields ell=0 or m=0. For the
other roots of unity, one component of t gives

    (m-s ell)/(m+s ell)=zeta,
    m=((1+zeta)/(1-zeta)) s ell,

after possibly exchanging the factors. The denominators are units
because q is a unit in both factors. Squaring proves the required
identity m^2=rho delta ell^2 in the full T, not just its residue
field.

These generic identities extend to Gamma. The plane conic is a
pure Cohen--Macaulay curve, and the sections at issue belong to
invertible sheaves, whose maps into their generic total quotient
modules are injective. For the double line this can be seen directly
in k[a,b,epsilon]/(epsilon^2): a homogeneous section is
f(a,b)+epsilon g(a,b); vanishing in its generic Artin ring kills
both f and g. It does not follow merely from vanishing on the
reduced line. For two distinct lines, injection into the product of
their two generic fields proves that identities valid on both
lines hold on the whole reduced conic, including the node.

This proves necessity without assuming that D is reduced,
irreducible, smooth, or normal.

## 3. Independent sufficiency proof

Put v=w ell, so v^2=delta ell^2. The equality m ell=0 immediately
implies

    (m+v)^2=(m-v)^2,

because the difference is 4m w ell. Thus q^2 is invariant, retaining
all nilpotents.

For the other case, write lambda=(1+zeta)/(1-zeta), and let n be
the order of zeta. Then lambda is nonzero and lambda^2 is neither
zero nor one. Consider the polynomial

    P_n(m,v)=(m+v)^n-(m-v)^n.

It vanishes identically after either substitution m=lambda v or
m=-lambda v. The distinct linear factors m-lambda v and
m+lambda v consequently both divide P_n, and their product
m^2-lambda^2 v^2 divides P_n. Substituting the quadratic algebra
therefore gives P_n=0 whenever
m^2=lambda^2 delta ell^2. No cancellation of v, ell, or a
nilpotent is needed. Equivalently the parent's odd-binomial
coefficient polynomial S_n(m,d) is divisible by m^2-lambda^2 d.

For two reduced lines, choose a common multiple N of the two
orders, using order two for a product-zero case. The anti-invariant
coefficient of q^N vanishes on both lines and hence on their entire
union. No extra condition at their common point remains.

## 4. A nilpotent countershield

Scheme-level identities are essential. In the generic double-line
ring take

    T=K[epsilon]/(epsilon^2),
    E=T[w]/(w^2-(1+epsilon)),
    m=i, ell=1, q=i+w, i^2=-1.

The element q is a nonzerodivisor: in the two residual factors its
values are i+1 and i-1, both nonzero. On the reduced line one has
m^2=-delta, the cyclotomic constant for a fourth root of unity.
But this equality fails in the entire ring:

    m^2+delta=epsilon != 0,
    q^4-sigma(q)^4=8i w epsilon != 0.

Indeed no positive power is invariant. The generic ratio has a
nonzero nilpotent correction, whereas an Artin-ring root of unity
in characteristic zero has none. The exact criterion detects this
failure. Another elementary shield is m=1, ell=epsilon,
delta=1: the product m ell vanishes on the reduced line but

    q^n-sigma(q)^n=2n w epsilon != 0

for every positive n. Thus testing only reduced-support coefficients
would invalidate either branch of the criterion.

## 5. The finite coefficient conditions have the claimed scope

For a smooth conic or a double line, the exact criterion implies
linear dependence of m^2 and delta ell^2 in H^0(Gamma,M^4).
In a product-zero case, the generic q-unit condition ensures that
either m=0 or ell=0 in its single generic base ring; alternatively
apply the necessity argument to q^2. The resulting identity extends
to the entire Gamma. Thus one of the two sections is zero.

The common dimension of H^0(Gamma,M^4) is nine. For the smooth
conic, M corresponds to O_P1(2), giving binary octics. For the
double line, the full basis is

    a^4,a^3b,a^2b^2,ab^3,b^4,
    epsilon a^3,epsilon a^2b,epsilon ab^2,epsilon b^3.

Hence the 2 x 9 coefficient matrix has rank at most one; its
36 two-column minors are finite algebraic necessary conditions.
For two lines, each restriction is a binary quartic, yielding two
2 x 5 matrices and ten minors for each. Separate proportionality
constants must be allowed.

These rank conditions do not replace the exact cyclotomic
criterion. For example the double-line example m=epsilon, ell=1,
delta=1 has a rank-one pair (m^2,delta ell^2)=(0,1), while the
product m ell is nonzero and q has no invariant positive power.
The proportionality constant zero is outside Cycl. This distinction
prevents promotion of a finite necessary determinantal locus into
a sufficient descent condition.

## 6. The abstract unbounded-order example is valid

For Gamma=P1 embedded as a smooth conic, take M=O_P1(2), a section
s of M with two simple zeros, and delta=s^2. The finite quadratic
curve D is two copies of P1 meeting transversely at the two zeros
of s. It is connected, Gorenstein, has arithmetic genus one, and
has p_*O_D=O_Gamma direct_sum M^(-1). For

    lambda=(1+zeta)/(1-zeta),
    ell=s, m=lambda s^2,

the restrictions of q to the two components are
(lambda+1)s^2 and (lambda-1)s^2. Both constants are nonzero for
zeta != 1, and their ratio is zeta^(-1). Thus q is a
nonzerodivisor, and its smallest descended power is exactly the
order of zeta. These orders are unbounded. Its zeros have order
two on both components, and all its zero fibers have singleton
support.

This is an algebraic counterexample to a bound derived solely from
connectedness, arithmetic genus one, even component valuations,
and singleton fibers at the zeros. It is not an actual quartic
surface or an STCI construction. Those surface requirements
remain a separate geometric problem.

## 7. Acceptance boundary

The parent's exact criterion and finite necessary coefficient
conditions are accepted as an algebraic result. The proof needs
characteristic zero, the entire plane-conic schemes, and the
nonzerodivisor hypothesis on q. No use of only the reduced support
or of a global sign on exchanged components is justified. No
computation or literature claim is needed for this direct audit.



---

## Source: 2026-10-09-session-quadratic-conductor-power-descent.md

# Exact power descent in the entire quadratic conic conductor algebra

Date: 2026-10-09. Author: `quadratic_conductor_power_descent`.

Status: **PROVED HERE; independent audit requested.** These are algebraic
necessary and sufficient conditions for power descent on the actual
conductor. They do not classify which conductor data come from the fixed
rational quartic on a normal del Pezzo surface. In particular they are not
an exclusion of the remaining genus-one carriers or a resolution of STCI.

## 1. Scope and the section decomposition

Work over an algebraically closed field `k` of characteristic zero. Let
`Gamma` be the actual plane conic, allowing a smooth conic, two distinct
lines, or a plane double line. Let `M=O_Gamma(1)` and let `p:D -> Gamma`
be the entire finite flat quadratic conductor algebra

```
p_*O_D = O_Gamma direct_sum M^(-1).
```

The second summand is the trace-zero part. In a local pulled-back frame
write its generator as `w`, with multiplication `w^2=delta`. In these
coordinates `delta` has the transition rule of a section of `M^2`.
The involution fixes the base and sends `w` to `-w`.

For a section `q` of `p^*M^2`, the corresponding global decomposition is

```
q = m + w ell,
m in H^0(Gamma,M^2),  ell in H^0(Gamma,M),
delta in H^0(Gamma,M^2).
```

All products below use those transition rules, so they define global
sections. Assume `q` is a nonzerodivisor on the entire scheme `D`. In the
surface application, this holds for `q=Q|D` if `div_S(Q)=2c` and no
irreducible component of `D` is `c`: `D` is Cartier on the Cohen--Macaulay
surface, hence has no embedded associated points, and `Q` does not vanish
at any generic point of `D`. An actual conductor component cannot be `c`
when its image is in the degree-two conic while the image of `c` is the
degree-four integral curve `C0`.

For the two-quadric model used by the root, with

```
z^2 - A z - R1 = 0,       L z + R = 0,
Gamma = V(L,R),           D = V_S(L),
Q = q2 + z ell,
```

the decomposition is exactly

```
w=z-A/2,       delta=A^2/4+R1,       m=q2+A ell/2
```

on the entire `Gamma`, including its nilpotents. The complete conductor
square identifies descent of `Q^n` to the quartic surface with invariance
of `q^n` under the involution. This note addresses that algebraic
invariance; the conductor-square identification is proved in the separate
entire-conductor note.

## 2. A universal polynomial equation for a specified power

Put `d=delta ell^2`, a section of `M^4`. The anti-invariant coefficient
of `q^n` is

```
ell S_n(m,d),
S_n(m,d) = sum_{j=0}^{floor((n-1)/2)}
           binomial(n,2j+1) m^(n-2j-1) d^j.
```

Thus, for every positive integer `n`,

```
q^n descends  <=>  ell S_n(m,delta ell^2)=0 on the entire Gamma.
```

This equivalence uses that `1,w` are a free basis of the quadratic
algebra, not division by `w` or reduction to the support. For example
`S_2=2m`, `S_3=3m^2+d`, and
`S_4=4m(m^2+d)`.

## 3. Exact criterion for existence of some descended power

Define the following countable set of constants:

```
Cycl = { ((1+zeta)/(1-zeta))^2 :
         zeta in k is a root of unity, zeta != 1,-1 }.
```

Neither `0` nor `1` belongs to `Cycl`. The two reciprocal roots of unity
give the same constant. For a smooth conic or the entire plane double
line, the following criterion is necessary and sufficient:

> Some positive power of `q` descends if and only if either
> `m ell=0` as a section on the entire `Gamma`, or there exists
> `rho in Cycl` such that `m^2=rho delta ell^2` on the entire `Gamma`.

For two distinct lines, use this criterion separately on each reduced
line; the two constants may differ. A common multiple of the two chosen
root-of-unity orders, and of `2` for each `m ell=0` case, gives a single
descended power on the whole conic. There is no discarded condition at
the node: the base conic is reduced, so a section vanishing on both
irreducible components vanishes on the whole scheme.

### Necessity, with double-line nilpotents retained

At the generic point of an irreducible reduced conic or line, the base
ring is its function field `K`. At the unique generic point of a plane
double line, the base ring is the Artin ring `K[epsilon]/(epsilon^2)`.
Write this base ring as `T`, and let `E=T[w]/(w^2-delta)`. The image of
the nonzerodivisor `q` is a unit in `E`: in the generic zero-dimensional
ring a nonzerodivisor is invertible. If `q^n` is invariant, the unit

```
t = sigma(q)/q
```

satisfies `t^n=1`. The factors of `T^n-1` over `k` are the distinct
linear factors `T-zeta`. Consequently an `n`th root of unity in a
finite Artin algebra is a constant root of unity on each local factor,
with no nonzero nilpotent correction. This follows directly from the
pairwise coprime linear factors and their idempotent decomposition.

There are precisely three generic possibilities for `E`.

1. If the residual `delta` is nonzero and nonsquare in `K`, `E` is
   local with quadratic residue field. Thus `t=zeta` is a single
   constant. Since `sigma(t)=t^(-1)` and `sigma` fixes constants,
   `zeta=+1` or `-1`. These possibilities imply `ell=0` or `m=0`
   respectively, as exact identities in `T`.
2. If the residual `delta` is zero, `E` is local and `sigma` acts as
   the identity on its residue field. Hence `t=1`, and `ell=0` as
   an exact identity in `T`. This excludes nilpotent anti-invariant
   corrections; it is stronger than an identity only on the reduced
   support.
3. If the residual `delta` is a nonzero square, its square root lifts
   uniquely across the nilpotents after choosing a sign, since `2`
   times that root is a unit. Then `E=T x T`, with `sigma` swapping
   the two factors. Consequently `t=(zeta,zeta^(-1))`. For
   `zeta=+1` or `-1` this again gives `ell=0` or `m=0`. Otherwise,
   writing `s^2=delta` in `T` gives

   ```
   m = lambda s ell,  lambda=(1+zeta)/(1-zeta)
   ```

   up to exchanging the two factors. Hence
   `m^2=rho delta ell^2` exactly in `T`, with `rho=lambda^2 in Cycl`.

The identities on the smooth conic extend from its function field. On
the double line they extend from the generic Artin ring, not from its
residue field: a section of a locally free sheaf on this pure
Cohen--Macaulay conic that vanishes at the generic Artin ring is zero.
This can also be checked explicitly in the plane double-line ring
`k[a,b,epsilon]/(epsilon^2)`, where a homogeneous section has its full
two terms `f(a,b)+epsilon g(a,b)` and generic vanishing kills both.

Thus the global identities in the criterion retain the double-line
first-order data. On a union of distinct lines the argument applies
component by component, giving the stated separate identities.

### Sufficiency without a reducedness assumption

If `m ell=0`, the coefficient of `w` in `q^2` is `2m ell=0`, so
`q^2` descends on every conic type, with all nilpotents included.

Suppose `m^2=rho d`, where
`rho=((1+zeta)/(1-zeta))^2` and `zeta` has order `n` other than
`1` or `2`. The polynomial `S_n(m,d)` is divisible by
`m^2-rho d` in `k[m,d]`. To verify this, formally put `d=b^2`.
The difference `(m+b)^n-(m-b)^n=2b S_n(m,b^2)` vanishes at both
`m=+lambda b` and `m=-lambda b`, since their two ratios are
`zeta` and `zeta^(-1)`. Since `lambda` is nonzero and the two
linear factors are distinct, `m^2-lambda^2 b^2` divides it after
cancellation of `2b`. The resulting even polynomial in `b` is the
claimed divisibility in `k[m,d]`. The universal polynomial equation
in Section 2 then proves descent of `q^n` without division by a
potential zero or nilpotent on `Gamma`.

## 4. Finite polynomial necessary conditions independent of mate degree

The exact criterion has a countable constant set because mate degree is
unbounded. It nevertheless has a finite algebraic necessary shadow.
For a smooth conic or an entire double line, the two sections

```
m^2, delta ell^2 in H^0(Gamma,M^4)
```

must be linearly dependent over `k`. Indeed, the exact criterion gives
a constant proportionality, except in the case `m ell=0`. In that
case the generic Artin proof above gives `m=0` or `ell=0`, and the
generic identity extends to the whole irreducible scheme, so one of
these two sections is zero.

For the smooth conic, parameterize by `P1`; `M=O_P1(2)`, so the two
sections are binary forms of degree eight. Their `2 x 9` coefficient
matrix has rank at most one: all `36` two-column minors vanish.
For a plane double line, `h^0(M^4)=9` as well. In coordinates
`Gamma:epsilon^2=0` in `P2[a,b,epsilon]`, a convenient basis is

```
a^4,a^3b,a^2b^2,ab^3,b^4,
epsilon a^3,epsilon a^2b,epsilon ab^2,epsilon b^3.
```

The same `36` minors must vanish with these full scheme coefficients.
Checking only the first five coefficients is insufficient.

For two distinct lines, the separate restrictions of `m^2` and
`delta ell^2` are binary quartics. The required ranks are at most
one for two `2 x 5` matrices, hence `10` minors per line. The constants
are allowed to differ on the two lines, so imposing a single global
proportionality on all nine conic coefficients would be unjustified.

These finite equations are necessary, not sufficient for power descent.
For example, proportionality with a constant outside `Cycl` need not
give a descended power, and the double-line proportionality at `rho=0`
does not by itself kill a nonzero nilpotent `m`.

## 5. A split-cover example prevents an algebra-only degree bound

Take a smooth conic `Gamma=P1` with `M=O_P1(2)`. Choose a section
`s` of `M` with two simple zeros and form the complete quadratic
algebra with `delta=s^2`. Thus `D` consists of two copies of `P1`
meeting at those two points; it is connected, Gorenstein and has
arithmetic genus one. Its algebra still satisfies
`p_*O_D=O_Gamma direct_sum M^(-1)` and `H^0(D,O_D)=k`.

Choose any root of unity `zeta != 1`, and set

```
lambda=(1+zeta)/(1-zeta),  ell=s,  m=lambda s^2,
q=(lambda s+w)s.
```

The two components have restrictions

```
q_+=(lambda+1)s^2,     q_-=(lambda-1)s^2.
```

Both constants are nonzero, so `q` is a nonzerodivisor. Their ratio
is `zeta^(-1)` with this choice of lambda; the inverse has the same
order. Accordingly the smallest positive descended power is the
order of `zeta`, which can be arbitrarily large. The only zeros lie
over the two singleton support fibers `s=0`, and the orders on each
component are even. Thus connectedness, arithmetic genus one,
singleton support fibers at zeros, and even component valuations do
not bound the power exponent in this algebra alone.

This is **not** a construction of a del Pezzo surface, a doubled
rational normal quartic, or an STCI pair. Those additional geometric
requirements may exclude the example. It identifies the exact
remaining obstruction to an argument based only on the quadratic
conductor algebra. In particular a root-of-unity ratio on exchanged
components must not be silently replaced by a global sign.

## 6. Remaining surface-geometric work

For an integral nonsplit cover of a reduced irreducible conic, power
descent does force `q` to be invariant or anti-invariant. Invariance
of the original global `Q` on the entire conductor yields an ambient
quadric with doubled `C0`, which is already excluded by the fixed
curve's unique smooth quadric and its ruling class `(1,3)`.

Anti-invariance remains possible when the conductor passes through
singularities at which `c` is not Cartier. The local `A1` model
`x^2+l x-z^2=0`, `c=(x,z)`, `Q=x`, `D=(l)` has
`div(Q)=2c`, and on the nodal conductor `sigma(x)=-x` while `x^2`
descends. Thus the smooth-conductor parity proof does not extend by
ignoring those singular points.

The root and `singular_normalization_next_frontier` are pursuing the
actual rational-normal-quartic ribbon, two-quadric pencil and
projection singleton constraints. The bounded rank equations here
can be combined with those exact geometric constraints; they do not
replace them.



---

## Source: 2026-10-09-session-rational-genus-one-ADE-independent-audit.md

# Independent audit: rational sectional-genus-one normalizations

Date: 2026-10-09. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted**. This is the bounded
structural lemma proposed by root; it does not itself exclude mates.
No canonical frontier records were edited.

Binding owner source, subsequently read in full:
[Genus-one del Pezzo reduction](2026-10-09-session-genus-one-delpezzo-reduction.md),
sections 1--5. Its canonical-form representative argument agrees
with the independent proof below. Its proposed lattice filter is
explicitly a separate obligation, not promoted by this audit.

## Statement

Let S be a normal projective rational surface over an algebraically
closed field of characteristic zero, with an ample globally generated
Cartier divisor H of square four. Suppose a general member has genus
one. Let sigma:M->S be its minimal resolution and L=sigma^*H. Then

    K_M~ -L,       K_S~ -H,

S is a Gorenstein del Pezzo surface of degree four with only Du Val
singularities, and sigma is crepant. In particular M is a weak del
Pezzo surface of degree four with anticanonical divisor L. No mate
is required for this reduction.

## 1. The adjoint section is effective exceptional

Rationality gives chi(O_M)=1. Adjunction to a general genus-one
hyperplane section, disjoint from the exceptional locus, gives
K_M.L=-4 and L^2=4. Kawamata--Viehweg vanishing for the nef and big
L gives Hi(K_M+L)=0 for i>0. Riemann--Roch therefore gives

    h0(K_M+L)=1+(K_M+L).L/2=1.

Choose the effective divisor D of this nonzero section. Since
D~K_M+L, one has L.D=0. Every component of an effective divisor has
nonnegative L-degree, and any component mapping to a curve on S has
strictly positive degree because H is ample. Thus every component
of D is sigma-exceptional. This conclusion does not presuppose
Cartierness of K_S or a discrepancy formula.

## 2. Minimality and negative definiteness force D=0

For each integral exceptional prime E, negative definiteness gives
E^2<0. A minimal resolution has no exceptional smooth rational
(-1)-curve. Adjunction on M gives

    K_M.E=2p_a(E)-2-E^2>=0.

Indeed, if p_a(E)=0 it is smooth P1 and E^2<=-2; if p_a(E)>=1,
the expression is positive. Thus D.E=K_M.E+L.E=K_M.E>=0 for every
exceptional prime. If D=sum d_i E_i were nonzero, effectiveness
would give

    D^2=sum d_i(D.E_i)>=0,

contradicting negative definiteness of the exceptional intersection
form. Therefore D=0, and the adjoint section is nowhere vanishing.
This proves K_M~ -L exactly as a linear equivalence. It is stronger
than merely finding an effective representative of a discrepancy
class, and avoids any ambiguity in that interpretation.

## 3. Canonical representatives and the crepant conclusion

Choose a Cartier divisor A representing H. Since K_M+sigma^*A~0,
choose a rational canonical differential theta on the common function
field with

    div_M(theta)=-sigma^*A.

Pushing that same differential down defines the compatible canonical
Weil divisor div_S(theta)=-A. Hence K_S is Cartier and

    div_M(theta)=sigma^*div_S(theta).

This is an actual crepant equality with compatible representatives,
not an inference that an arbitrary effective divisor linearly
equivalent to K_M+L is the discrepancy divisor. Normal surfaces are
Cohen--Macaulay, so Cartier K_S makes the dualizing sheaf invertible;
S is Gorenstein. Since -K_S~H is ample with square four, it is a
degree-four del Pezzo surface.

The crepant-resolution criterion identifies its singularities as
Du Val. A primary author's formulation is
[Reid, The Du Val singularities, Theorem 2.1(2)](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
The standard algebraic criterion applies in characteristic zero.
The exceptional-curve calculation is also intrinsic over the stated
field: K_M.E=0 implies E^2=2p_a(E)-2<0, hence every exceptional prime
is smooth rational with square -2. Negative definiteness makes the
intersection graphs the finite ADE graphs. No quartic slc table is
used to establish these singularity hypotheses.

## 4. Accepted scope and unfinished work

Together with the separately audited nonrational reduction, this
establishes that the entire sectional-genus-one normalization lane
for nonnormal quartics containing C0 is a Gorenstein degree-four
del Pezzo model with an ADE minimal resolution. Consequently the
scoped weak-del-Pezzo/ADE and D5 lattice task has its geometric
hypotheses established. Its lattice proof, enumeration, and remaining
curve and mate hypotheses still require their own acceptance.
This lemma is a hypothesis reduction, not a new conclusion that
all such carriers have no mate.

Rational sectional-genus-two normalizations, their singular points
and conductors, and higher carrier degrees remain outside it. The
unrestricted C0 and universal STCI problems remain open.

`git diff --check` passed. No children were spawned; work froze after
saving this bounded proof and the companion nonrational audit.
