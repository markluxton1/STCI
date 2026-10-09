# MF6 constant-direction type (4,5): moving-chart annihilator reduction

Started 2026-10-06; resumed 2026-10-07 after a usage-limit interruption.
Characteristic zero; fixed monomial quartic
`C0=[s^4:s^3t:st^3:t^4]`.

**Status: PROVED HERE, INDEPENDENTLY AUDITED.** The complete
`e=0,(d2,d3)=(4,5)` branch is excluded, including every quartic rank-drop
fiber and infinity. On 2026-10-07 the root agent independently audited
the moving-support derivative correction, the degree-loss and infinity
annihilator argument, the shifted coefficient ideal, and the full
four-dimensional exceptional quartic fiber. The self-contained exact
verifier passed after adding direct ideal-membership witnesses and the
full fiber reconstruction.

The earlier note `2026-10-06-mf6-type4-incidence.md` remains a correct
historical record of its generic-only calculation. This continuation
supplies the missing intrinsic annihilator condition; it does not promote
that generic kernel to the complete family.

## 1. Complete triple family and quartic variable

The retained degree-four triple reduction exhausts the mixed constant
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

Let `F` be any quartic in the complete eight-dimensional space with
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

The exact DVR lattice lemma in the preceding MF6 audit gives, at every
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
in `verify_mf6_infinity_universal.py`; their discovery output is also in
`../scratch/session-mf6-minor-membership.json`.

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

The companion `../scratch/session-mf6-special-fiber.py` derives the
complete mixed quartic basis, computes all four special kernel vectors,
and certifies equality with `C3*<x0,x1,x2,x3>` by an exact quartic
monomial coefficient matrix of rank four. Its exact output is preserved
in `../scratch/session-mf6-special-fiber.json`.

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

The exploratory Groebner output is in
`../scratch/session-mf6-rank-boundary.json`. These other rank-drop fibers
need not be separately classified for the proof, because (4) eliminates
them independently of the quartic kernel. An attempted algebraic-field
factorization of all six fibers was interrupted after checking two
members at `(12,4)`; no missing factorization is used as evidence.
The useful exact special fiber was instead checked by rational linear
algebra. No full resultant was launched in this continuation.

## Reproduction and remaining audit

Run with bytecode disabled:

    PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_mf6_infinity_universal.py
    PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/scratch/session-mf6-special-fiber.py

The universal verifier reconstructs the complete original coefficient
matrix, its generic vector for the additional direct chart check, and
the entire four-dimensional exceptional quartic fiber from the original
ideal basis. It has no generated-JSON input dependency. Its universal
proof inputs are the exact formal transition, the complete mixed quartic
first-normal kernel, the four-by-two polynomial matrix, and the explicit
ideal-membership witnesses. The shorter special-fiber scratch verifier
reads the regenerated matrix and reconstructs the same original quartics;
it is corroboration rather than a necessary external proof input.
## Completed independent audit and exact validation

On 2026-10-07 the root agent separately derived (1)--(4), including
`deg T=deg S+3` when `S` loses degree, and checked the global length-one
annihilator on both charts. The root also reconstructed the shifted
`j4,...,j8` by hand and independently computed their minor ideal
`(alpha,beta)^2` in SymPy. It checked that the sole remaining full fiber
has rank four, rather than substituting its vanishing generic vector.
The proof was accepted under the stated characteristic-zero, fixed-C0,
quasiprimitive saturated-filtration hypotheses.

The final combined verifier passed through all assertions, including
both the exact Groebner equality and the explicit membership witnesses,
nonzero `S`, nonlinear moving-support correction, direct generic chart
expansion, and complete exceptional-fiber cubic factorization. Its
stdout is preserved in
`../scratch/session-mf6-infinity-universal-output.txt`.
The optional witness parser initially treated `beta` as SymPy's beta
function; explicit local symbols corrected this software-only issue,
and the entire combined verifier was rerun successfully. No mathematical
assertion depended on that failed parser run.

The next open MF6 branch is `e=1`, with types `(0,4),(1,3),(2,2)`.
The regular `e=0,(3,6)` member remains open. This result therefore
eliminates all remaining **nonregular constant-direction** `(4,6)`
strata, while leaving those stated regular and degree-one-direction
possibilities.
