# Principal MF6 carriers: an exact finite necessary locus

For the fixed C0 in characteristic zero, use principal parameters(p,r,b)
of weights(2,1,1), direction A=1+rz,B=b+pz, and the actual principal
second-defect-one contact locus. Put

    d=p-rb,
    P=2p+12r^2+16rb+9b^2,
    T=2p-4r^2-4rb-b^2,
    U=p*P*d*(2r-b)*T.

On the integral sextic H=0 and U!=0, the
[complete contact-rank theorem](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-principal-e1-d1-independent-completeness-auditmd)
gives rank 17 and makes the actual ambient quartic space one-dimensional. One checked
polynomial syzygy supplies its binary first-normal octic, with zero-
generator specializations kept. The fixed binary-gradient determinant
has weighted degree210, is nonzero on H, and cuts a necessary locus of
at most630 distinct principal parameters for a hypothetical nonnormal
mate carrier. Its exact zero list is uncomputed and is not the exact
nonnormal locus. The later [all-quartic theorem](../synthesis/quartic_carrier_proof.md)
closes actual mate existence. The separate complete contact-space proof
also closes this principal common-quartic-ancestor branch. The curve and
candidate calculation remain useful independent mechanisms; they do not
compute other common-ancestor incidences.

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

Its geometric integrality and genus-one normalization follow from the
[complete birational curve calculation](MF6_PRINCIPAL_DIRECTION_CURVE.md). The full ambient quartic ideal has the eighteen actual forms
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

The full 23-by-18 contact matrix specializes at b=1 to the accepted eleven first-contact rows and twelve second-contact rows. Its row offsets are exactly 1 through 11, then 10 through 21; its column offsets are exactly 1,0,2,3,4,5,6,1,3,4,5,6,7,7,8,9,9,10. Homogeneous polynomial extension of a fixed offset is uniquely determined by its b=1 specialization: a monomial p^i r^j has the unique possible b-exponent w-2i-j. The owner checks these entry weights, each coordinate of the three degrees 9,9,10 generators, and all sixty-nine contact identities modulo H.

## 2. The geometric multiple-root necessity

### 2.1. A nonnormal mate carrier necessarily meets its conductor

Let X subset P3 be an integral quartic containing the fixed smooth
rational quartic C0. It is automatically regular at the generic point
of C0: a general integral plane quartic would otherwise have four
distinct singular points, contradicting arithmetic genus three.
The full argument is appended to the
[generic-regularity proof](../synthesis/quartic_carrier_proof.md#1-sole-support-smooth-passage-and-the-common-correction-identity).

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

### 2.2. A simple first-normal zero gives a nondegenerate quadratic pair

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

### 2.3. Hessian rank at least two contradicts the allowed meeting

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
in Section 2.1. Therefore the actual first-normal coefficient has a
multiple zero at some point of C0.

## 3. Actual normal coefficient and determinant

The [independent exact coefficient checker](../computations/audit_session_mf6_weighted_candidate_2026_10_09.py) reconstructs the following data.

It independently differentiates the eighteen actual forms and contracts the first polynomial generator to produce F_U and F_V along C0, in the balanced frame

    U=-r m/d+(1+rz)y,
    V=-p m/d+(b+pz)y.

With A=1+rz and B=b+pz, it verifies the full polynomial identities modulo H

    A F_U+B F_V=0,
    hhat=-r F_U-p F_V,
    d F_U=B hhat, d F_V=-A hhat.

It reconstructs all nine coefficients h_j of hhat, checks their exact equality with the saved vector, and checks that no coefficient of degree greater than eight survives modulo H. The two latter frame identities also explain why hhat is the actual common first-normal binary octic: F_U=B h and F_V=-A h, with hhat=d h and d a unit on the declared open. The homogeneous linear direction A,B is basepoint free when d!=0. This controls both curve charts rather than only an affine derivative chosen in a frame with a zero.

Explicitly, the binary form and candidate determinant are

    hhat(s,t)=sum(h_j*s^(8-j)*t^j, j=0,...,8),
    Delta=det Sylv_7(partial_s hhat, partial_t hhat).

Here Sylv_7 is the fixed 14-by-14 Sylvester matrix of the two
homogeneous degree-seven gradients. On s=1 their coefficient
polynomials are 8*hhat(1,z)-z*hhat'(1,z) and hhat'(1,z), with the
fixed degree-seven padding even when a leading coefficient vanishes.
No h_8 division or smaller-degree resultant is substituted. The
[full symbolic coefficient vector and matrix](../scratch/session-mf6-principal-weighted-candidate-2026-10-09.json)
are literal inputs to the independent reconstruction.

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

At a point of U!=0 where G0 is nonzero, it lies in the complete contact kernel and hence is a nonzero scalar multiple of the unique actual quartic. That scalar and d do not change first-normal root multiplicities. The geometric necessity proved by the [geometric proof above](#2-the-geometric-multiple-root-necessity) forces a multiple projective root, so Delta vanishes.

If G0 specializes to zero, its first-normal vector specializes to zero, and Delta vanishes automatically. If G0 remains nonzero but its entire first-normal vector is zero, the same conclusion holds. No exceptional parameter was removed by dividing by a coefficient of G0, by a leading coefficient h_8, or by a rational scalar chosen on a smaller chart. The basepoint-free and contact units are the explicit U factors; parameters outside that open are handled separately, not silently added to this candidate theorem.

## 6. Ordinary-plane cover and the 630 bound

The map

    pi:P2 -> P(2,1,1), [a:r:b] -> [a^2:r:b]

is the finite quotient by a -> -a; equivalently its invariant graded ring is k[a^2,r,b], with generator degrees 2,1,1. Pullback gives ordinary homogeneous equations of degrees six and 210. Even if the lifted sextic splits, each of its irreducible curve components maps onto the integral H: finiteness prevents a curve from being contracted, and the only dimension-one closed image in H is H itself. Since Delta is nonzero on H, none of these components is contained in the pulled-back Delta. The two plane curves therefore have no common component.

Bezout bounds their scheme intersection length by 6*210=1260. A principal point has p!=0. On H it cannot have r=b=0 because H would then be 8p^3. It consequently has two distinct plane lifts [a:r:b] and [-a:r:b]: scaling would have to fix a nonzero r or b and hence be one, while a!=0 and characteristic zero forbid identifying the signs. Thus every distinct principal candidate consumes at least two distinct intersection points, proving at most 1260/2=630 candidates. Intersection multiplicities can only strengthen this upper bound; no reducedness of the intersection or irreducibility of its lift is assumed.

The bound concerns distinct weighted parameter points in the necessary locus, not 630 constructed quartics or 630 proven nonnormal fibers. Normal carriers, singularities away from C0, and generator base fibers may all occur among zeros; the exact zero list remains uncomputed here.

## 7. Bad reduction does not prove a characteristic-zero singular curve

Reductions at r=0 modulo 13 and 23 have repeated first-normal roots
and apparent triple-point jets. These are bad-reduction controls;
they do not prove a characteristic-zero nonnormal fiber or a singular
curve, as the exact cubic-field computation below shows.

The corrected r=0 computation is independently self-contained in
[`verify_session_mf6_principal_rzero_normality_2026_10_09.m2`](../computations/verify_session_mf6_principal_rzero_normality_2026_10_09.m2).
Its field polynomial is `8p^3-16p^2+6p-9`, irreducible modulo five
(the values at 0,...,4 are 1,4,3,1,1). Its literal quartic is bound to
the checked degree-nine generator restricted at r=0 in
[the input record](../scratch/session-mf6-principal-rzero-normality-input-2026-10-09.json).
The exact M2 check completed with exit zero and asserted Jacobian cone
dimension one, of degree fifteen. Dimension survives constant-field extension. Reducible or
nonreduced projective quartics have a curve of singular points, so this
also proves geometric integrality. The hypersurface S2 property and
finite singular locus prove geometric normality of all three conjugates.
The accepted normal-carrier theorem excludes their mates in every degree.

## Exact support and characteristic boundaries

The three degrees9,9,10 polynomial syzygies and the full coefficient/matrix
inputs are retained in the linked scratch files. The complete exact
checker is [verify_session_mf6_principal_weighted_candidate_2026_10_09.py](../computations/verify_session_mf6_principal_weighted_candidate_2026_10_09.py),
with the independent coefficient/infinity test linked in Section3. It
preserves the actual nine-coefficient octic and14-by14 matrix; no expanded
resultant or generic sample replaces that support. Existing independently
reviewed executions are reused without a fresh rerun.

The polynomial weight and matrix identities can be reduced where their
rational denominators are invertible. The binary-gradient multiple-root
criterion uses degree8 invertible, and the simple-zero formal splitting
argument requires two invertible. The two-to-one plane cover requires
characteristic different from two. The good prime101 witness proves
characteristic-zero nonvanishing by the primitive-polynomial argument;
it does not certify every other prime. Actual contact-rank and full-support
hypotheses must be checked before applying the same geometric inference
in positive characteristic. The direction curve itself has the explicit
[genus-one model](MF6_PRINCIPAL_DIRECTION_CURVE.md) away from characteristics
two and three. None of these statements transports the full quartic-carrier
exclusion to positive characteristic.
