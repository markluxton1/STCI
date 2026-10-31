# A defect divisor and the full quartic-contact family in multiplicity six

For fixed C0 in characteristic zero, a hypothetical quasiprimitive(4,6) pair has several possible saturated-filtration types. This owner proves the complete exclusion of the mixed constant-direction type e=0,(d2,d3)=(4,5), including every quartic rank-drop fiber and infinity. The exact two-parameter triple family is retained, as are the actual eight-dimensional quartic source, nonlinear support-coordinate change, global length-one annihilator and full exceptional cubic factorization.

The calculation measures an elementary modification: the allowed difference D3−D2 has total degree one, so it must annihilate the cubic residue on the complete zero divisor of the actual first-symbol multiplierS. The moving second chart forces a degree-loss identity; the resulting four-by-two Hankel matrix controls the allowable annihilator overP1. Its minor ideal is a nonreduced double point, and the quartic kernel at that point must be computed separately. This is the geometry behind the exact polynomial calculation.

The arbitrary-mate quartic theorem R-0001 already closes such pairs for C0; the present proof remains useful because it isolates the divisor/gluing and actual-source mechanism. It is not a proof for every smooth rational quartic or every positive characteristic.

<a id="2026-10-06-session-mf6-progress"></a>

## 1. Complete triple family and quartic variable

The [complete degree-four triple reduction](LOCALCOH_CONTACT_PARITY_AND_MF6_TYPE.md#every-possible-degree-four-triple) exhausts the mixed constant
normal directions after torus normalization `m=U+V,y=V`. Its parameters
are arbitrary `A,B`, with

    R=A+B(z-2)+z^2-2z+4,
    delta=z(z+2)R+16,
    gamma=3R/8,
    Res_z(delta,R)=256.

Thus `delta` has degree four with leading coefficient one, has no infinity
zero, and has no finite common zero with `R`. The discarded homogeneous
coefficient chart `C=0` in the original triple construction fails
flatness, rather than being omitted generically.

Let `F` be any quartic in the [complete eight-dimensional source](LOCALCOH_CONTACT_PARITY_AND_MF6_TYPE.md#complete-quartic-equation-and-its-cubic-pole-constraint) with
first-normal form `h(U+V)`. In the finite moving frame, write its quadratic
and cubic coefficients as `Q,E,K`, where `Q` is the `y^2` coefficient
at `m=0`, `E` the `my` coefficient, and `K` the `y^3` coefficient.
Triple containment is precisely

    delta Q+(3/8)R h=0.

Coprimality forces `h=delta S`, where `S` is a section of `O(5)`.
Every nonzero incidence quartic has `S!=0`: the first-normal kernel of
the mixed quartic space is the single line `<q^2>`, and its quadratic
restriction at `m=0` is nonzero, so `q^2` fails the triple equation.
Consequently the generic formal root is

    m=f2*y^2+f3*y^3+...,
    f2=3R/(8delta),
    f3=-T/(8delta^2 S), T=3RE+8delta K.

No kernel dimension or generic parameter assumption enters these formulas.

## 2. The moving second chart through cubic order

The actual second support parameter is

    W=(z^3+y)/(z^4+m+(3z/2-1)y).

It must be retained in the cubic calculation. In particular, replacing
`W` by `1/z` too early loses a derivative term. The balanced second normal
coordinates are

    a'=z/(z^4+m+(3z/2-1)y)-W^3,
    b'=1/(z^4+m+(3z/2-1)y)-W^4,
    U'=a'/2, V'=-3W a'+2b',
    m'=U'+V', y'=V'.

For a general formal root `m=f(z)y^2+g(z)y^3`, direct expansion gives

    f_infinity(1/z)=z^7 f(z)+p2(z),
    g_infinity(1/z)=z^14 g(z)+C(z)f(z)+D(z)f'(z)+P(z),

where

    p2=(-3z^5+6z^4-12z^3+24z^2)/8,
    C=-2z^11+9z^10-12z^9,
    D=-z^12/2+z^11,
    P=7z^9/16-25z^8/8+9z^7-14z^6+19z^5-18z^4.

The derivative term is the support-coordinate correction. The exact
companion `../computations/verify_mf6_infinity_universal.py` derives these
identities using cubic truncated polynomial arithmetic, with `f,f',g`
independent variables.

Put `w=1/z` on the reduced support. The specified triple has

    delta_infinity=w^4 delta(1/w),
    gamma_infinity=6Aw+6B(1-2w)+48w^2,
    S_infinity=w^5 S(1/w).

In the actual second quartic chart

    x3=1, x2=w,
    x1=w^3+2(m'-y'),
    x0=w^4+y'/2+3w(m'-y'),

let `E_infinity,K_infinity` denote the `m'y'` and `y'^3`
coefficients of `F`, and put

    T_infinity=8 gamma_infinity E_infinity
               +8 delta_infinity K_infinity.

The cubic root there is
`g_infinity=-T_infinity/(8delta_infinity^2 S_infinity)`.
Define the triple-dependent polynomial

    J=3R delta C+3(R' delta-R delta')D+8delta^2 P,
    Jhat=w^17 J(1/w).

The root transition yields the identity

    w^9 T_infinity=w^8 T(1/w)-S_infinity Jhat.       (1)

It holds for every incidence quartic, including all larger exceptional
kernels: its proof uses the universal formal-root transition. The saved
generic vector is only an additional independent direct quartic check.
Exactly `deg J=17` and `Jhat(0)=1/2`.

## 3. Intrinsic one-unit annihilator and the degree argument

The [exact third-piece DVR lattice lemma](MULTIPLICITY_MIXED46_AND_MF6.md#4-the-exact-third-piece-lattice-lemma) gives, at every
finite point,

    ord(D3-D2)=max(0,ord S-ord T).

At a zero of `delta`, `R` is a unit, so this remains true for multiple
zeros of `delta`; no simple-root assumption is used. At infinity
`delta_infinity(0)=1`, and the same formula is

    ord_infinity(D3-D2)
      =max(0,ord_0 S_infinity-ord_0 T_infinity).

Therefore a total excess degree at most one is equivalent to the
existence of a nonzero section `L` of `O(1)` annihilating the cubic
residue on the zero divisor of `S`: if the effective excess is one
point, choose that point as the zero of `L`; if it is zero, choose
any nonzero `L`. This includes repeated zeros and the possible extra
point at infinity. Write

    L(z)=l0+l1z, L_infinity(w)=l0w+l1.

The finite condition is exact polynomial divisibility

    L T=S Q.                                      (2)

The degree bound on `Q` must be derived rather than guessed. Let
`n=deg_z S`, so `0<=n<=5` and `ord_0 S_infinity=5-n`.
The left side of (1) has order at least nine, while
`S_infinity Jhat` has order exactly `5-n<=5`. Hence
`w^8 T(1/w)` must have exactly that order. Thus

    deg_z T=n+3,
    deg_z Q<=4.

This conclusion includes all affine degree losses in `S`; in particular
it controls rather than omits infinity zeros.

Multiplying (1) by `L_infinity/S_infinity` and using (2) gives

    w^9 L_infinity T_infinity/S_infinity
      =w^4 Q(1/w)-L_infinity Jhat.                 (3)

The infinity annihilator condition says that the left quotient is
regular at `w=0`. Thus the right side is divisible by `w^9`.
The first term has degree at most four. If
`j_i=coeff_(w^i) Jhat`, coefficients five through eight require

    [j4 j5] [l0]   [0]
    [j5 j6] [l1] = [0]
    [j6 j7]        [0]
    [j7 j8]        [0].                            (4)

For a compact independent specification, set `alpha=A-12,beta=B-4`.
Then the five required coefficients are

    j4=alpha^2/2+8alpha-4beta^2,
    j5=alpha^2-8alpha beta+16alpha+16beta^2-72beta,
    j6=-2alpha^2+16alpha beta-16alpha-32beta^2,
    j7=4alpha^2-32alpha beta-80alpha+64beta^2+288beta,
    j8=-8alpha^2+64alpha beta+128alpha-64beta^2.

The six two-by-two minors of this four-by-two matrix have exact ideal

    ((A-12)^2,(A-12)(B-4),(B-4)^2).

This is certified twice: by an exact rational Groebner calculation, and
by eighteen explicitly recorded linear-polynomial coefficients whose
three combinations of the six minors give `alpha^2,alpha beta,beta^2`.
Conversely every minor has no term below total degree two. Thus the
ideal equality can be checked solely by polynomial expansion, without
trusting a Groebner-basis output. The witnesses are embedded directly
in [the universal verifier](../computations/verify_mf6_infinity_universal.py),
which checks all three combinations by exact polynomial expansion.

Consequently any nonzero `L` forces `A=12,B=4` over an algebraically
closed characteristic-zero field. This conclusion uses the whole
incidence space and the annihilator on `P1`; no resultant, generic
kernel, rank-seven localization, or fixed pole placement is needed.

## 4. Complete remaining exceptional fiber

At `A=12,B=4`,

    delta=(z^2+2z+4)^2, R=z^2+2z+8.

The complete triple/quartic coefficient matrix has rank four, and its
kernel has dimension four. The saved generic kernel specializes to zero
here, so it supplies no quartics at this point.

Direct calculation of the full kernel gives exactly

    H0(I_triple(4))=C3 * H0(P3,O(1)),

where the explicit cubic is

    C3=64x0^2x2+64x0^2x3-64x0x1x2+32x0x1x3
       -16x0x2^2-8x0x2x3-4x0x3^2-64x1^3-32x1^2x2
       +16x1^2x3+8x1x2^2+4x1x2x3-x1x3^2+x2^3.

The [universal verifier](../computations/verify_mf6_infinity_universal.py)
reconstructs the complete mixed quartic basis, computes all four special
kernel vectors, and certifies equality with `C3*<x0,x1,x2,x3>` by an
exact quartic monomial coefficient matrix of rank four.

Every nonzero remaining quartic thus has an ambient plane factor. It
cannot occur in a defining pair with radical support `C0`: if the plane
factor divides the mate, the pair has a common surface; otherwise the
mate restricts to a nonzero positive-degree homogeneous equation on
that plane and cuts a nonempty projective curve in it. That curve would
be contained in the integral nonplanar `C0`, which is impossible.

This proves that the
`e=0,(d2,d3)=(4,5)` numerical branch is empty for the hypothesized
`(4,6)` presentation of `C0`. It does not settle the unrestricted STCI
question for `C0`, larger degree pairs, `e=1`, or the entirely-thick branch.

## 5. Additional exact boundary evidence and discarded work

For provenance, the seven nonzero rows of the original 13-by-8 matrix
have signed maximal minors exactly equal to the saved primitive kernel
vector (no nonconstant common factor). Their ideal has geometric support
at six points:

    (12,4), (-12,-2),
    (0,B), B^2-2B+4=0,
    (-12,B), B^2+4B+40=0.

This six-point list is additional boundary information, not an input to
the exclusion. These other rank-drop fibers need not be separately
classified for the proof, because (4) eliminates them independently of
the quartic kernel. The full exceptional fiber at (12,4), rather than
the vanishing generic vector, is indispensable.

## Exact support and review scope

The self-contained [universal verifier](../computations/verify_mf6_infinity_universal.py) reconstructs the complete original coefficient matrix and its full exceptional fiber from the actual ideal basis, checks the moving-support derivative, derives the polynomial matrix and verifies both its ideal equality and the explicit membership witnesses. It reads no generated-JSON proof fixture. The independent reconstruction in the inherited source state rederived the global annihilator, the degree loss whenS has infinity zeros, the shifted coefficient ideal and the whole rank-four exceptional fiber. No separate generated special-fiber fixture is needed.

The ordinary rational formulas use2 as a unit, and their exact coefficient/minor identities have only been certified in their stated characteristic-zero model. A prime-characteristic application would need the correct conormal and actual source model and all relevant inversions. The [positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) prevents interpreting this fixed characteristic-zero contact proof as a universal STCI obstruction. Other multiplicity-six types have their own proofs and prerequisites; the scalar divisor budget alone does not remove them.
