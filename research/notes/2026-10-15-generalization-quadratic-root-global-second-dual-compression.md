# A chart-free complete 25-pairing test for the universal second obstruction

Date: 2026-10-15. Author: `universal_root_obstruction`.
Status: **NEW GLOBAL REDUCTION; independent review passed.** Accepted
first/second ambient class constructions, the exact embedded chart, and
their earlier seed certificates are premises. None is rerun. This note
compresses the entire second obstruction into one polynomial family with
no coefficient chart, then exports a single bounded-elimination input.
It does not yet assert that the second zero scheme is empty.

## 1. The global dual presentation removes 39 unit variables

Let `f=a(z)u²+b(z)uv+c(z)v²` have base degree two. Throughout this
section assume only that its three homogeneous base coefficients have
no common zero; the root divisor can be singular or nonreduced. The
transpose of multiplication by `f` in the direction ruling is

```
        [ a b c 0 0 ]
T_f  =  [ 0 a b c 0 ] : O_P1^5 -> O_P1(2)^3.
        [ 0 0 a b c ]
```

It is surjective on every base fiber: its transpose is multiplication
by a nonzero binary quadratic from degree two to degree four, which is
injective. Thus `W=ker T_f` is a rank-two vector bundle with
`det W=O(-6)`.

The complete Serre-dual space of the actual second obstruction consists
of polynomial vectors `q=(q0,...,q4)`, of degree at most ten, such that

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0,
    a q2+b q3+c q4=0.                                 (1)

It is exactly `H0(P1,W(10))`, of dimension sixteen. This is the dual of
`coker[H1 O(-14,2) --f--> H1 O(-12,4)]`; no first-order normal-symbol
replacement is made.

Dualizing the exact sequence defining `W`, and using the canonical
rank-two identification `W*=W tensor(det W)^-1`, gives

    0 -> O(-2)^3 -> O^5 -> W(6) -> 0.                 (2)

After twisting by `O(4)`, the left term is `O(2)^3` and has no `H1`.
Consequently

    H0(O(4))^5 -> H0(W(10)) -> 0                     (3)

is surjective. Its source dimension is twenty-five and its kernel
dimension is nine. Thus twenty-five scalar pairings give a complete
test for all sixteen actual obstruction coordinates. This works on
the entire basepoint-free family, including every splitting-jump locus.
It makes no choice of an invertible coefficient or matrix minor.

For an explicit polynomial version, form a skew `5 by 5` matrix `P_f`.
With zero-based indices `0,...,4`, put for `i<j`

    (P_f)_ij=(-1)^(i+j+1) det(T_f with columns i,j deleted),
    (P_f)_ji=-(P_f)_ij,    (P_f)_ii=0.                (4)

Then `T_f P_f=0`. Its five columns are the five generating sections of
`W(6)` in (2), written as signed complementary maximal minors. Each
entry has degree at most six in the affine base coordinate and is cubic
in the coefficients of `f`.

Let `R4` be any Cech representative of the actual second class, with
quartic direction components `r0,...,r4` and Laurent powers retained in
`z^-11,...,z^-1`. The second obstruction vanishes if and only if

    coefficient_z^-1 [ z^j sum_i (P_f)_i,l r_i ]=0
                for l=0,...,4 and j=0,...,4.          (5)

The criterion is scheme-theoretic. Indeed the family version of (3) is
a surjection of vector bundles; the twenty-five pairings generate the
same zero ideal as the rank-sixteen second section. It follows that
(5) does not lose exceptional coefficient strata or retain only generic
rank information.

For projective coefficient space `U`, the universal matrix is
`O^5 -> O(2) tensor O_U(1)^3`. Thus
`det W=O(-6) tensor O_U(-3)`, and the globally correct version of (2)
is

    0 -> O(-2) tensor O_U(-1)^3
      -> O^5
      -> W(6) tensor O_U(3) -> 0.

After the same base twist by four and pushforward, (3) becomes an
everywhere-surjective bundle map from `O_U^25` onto
`p_*W(10) tensor O_U(3)`. The dual of the actual second obstruction
bundle is `p_*W(10) tensor O_U(-1)`. Twisting the displayed surjection
by `O_U(-4)` therefore gives a surjection from `O_U(-4)^25` onto that
dual. This verifies the scheme-theoretic claim and the homogeneous
coefficient degree four of the scalar pairings. On the affine coefficient
cone the representatives are exactly (4); the cubic coefficient degree
of the Plucker vectors is a twist, not a denominator.

## 2. A single actual-chart model supplies R4 universally

The accepted full embedded transition is used as input:

```
den=z⁴+u+(3/2)zv, w=(z³+v)/den,
a'=z/den−w³, b'=1/den−w⁴,
u'=a'/2, v'=−3w a'+2b'.
```

Write `f1` for the second-chart root equation obtained by reversing each
quadratic coefficient polynomial:

    f1=(a2+a1w+a0w²)u'²
       +(b2+b1w+b0w²)u'v'
       +(c2+c1w+c0w²)v'².

Expand only through normal degree four. Let

    beta=-2z^-4u-z^-3v,
    h=sum_(k=-6)^(-1) (h_(u,k)u+h_(v,k)v)z^k,
    L1=h+beta,
    S3=[z^16 f1]_3-L1*f.                             (6)

Its sixteen middle Laurent coefficients, on `z^-4,...,z^-1` times
binary cubics, are the universal first equations. They are equivalent
to the accepted `A_f h=d_f`. No new first-incidence rank claim is needed.

Define the local cubic corrections by their regular Cech parts:

    G0 = the z>=0 part of S3,
    z^-5 G1(z^-1;u,v) = - the z<=-5 part of S3.       (7)

All coefficients of `G0` have degree at most one in `z`, and those of
`G1` have degree at most one in `w`; these bounds follow from the finite
supports in (6), with no coefficient open imposed. On the first zero
scheme, (7) gives the exact cubic patch identity

    [z^16(f1+G1)]_3-G0-L1*f=0.

The universal representative used in (5) is

    R4=pr_(z^-11,...,z^-1)
         ( [z^16(f1+G1)]_4 - L1*G0 ).                (8)

Here `G1` is substituted using the full nonlinear coordinates `w,u',v'`.
The base derivative, the first equation unit, and its product with the
first correction are all retained. The unknown next equation unit is
a multiple of `f`; it disappears under every pairing (1). Unknown
quartic local corrections are Cech coboundaries. Therefore no thirty-nine
quartic unit variables are required in the final system.

The model has the nine coefficient variables of `f` and twelve variables
of `h`. Its sixteen first equations are bilinear. Its twenty-five second
equations have total degree at most six, homogeneous degree four in the
coefficients of `f` and degree at most two in `h`. There is one affine
model for the full coefficient cone. Scale of `f` is harmless on the
smooth open and need not be normalized by a coefficient chart.

## 3. The smooth open is one homogeneous binary-quartic discriminant

Put

    Delta(z)=b(z)^2-4a(z)c(z)=d0+d1z+d2z²+d3z³+d4z⁴,

regarded throughout as the binary quartic
`d0 Y⁴+d1 XY³+d2 X²Y²+d3 X³Y+d4 X⁴`.
Define

    I=12d4d0-3d3d1+d2²,
    J=72d4d2d0+9d3d2d1-27d4d1²-27d3²d0-2d2³,
    Disc=(4I³-J²)/27.                                (9)

In characteristic zero this is the homogeneous binary-quartic
discriminant. It is homogeneous of degree twelve in the nine coefficients
of `f`.

The condition `Disc!=0` is exactly the smooth-root condition. A common
base zero of `a,b,c` gives a common homogeneous linear factor and forces
its square to divide `Delta`, so it makes `Disc=0`. Thus the open already
implies basepoint freeness. On that open the double-cover discriminant
is the branch divisor; it has four simple roots exactly when the root
curve is smooth. Conversely every smooth `(2,2)` root gives a finite
separable degree-two map with four simple branch points, so its binary
discriminant is nonzero.

No leading affine coefficient is inverted. In particular `d4=0` with
`d3!=0` represents a simple branch point at infinity and is allowed by
(9). A second zero at infinity gives vanishing discriminant, as required.
The formula does not silently discard degree-drop cases.

The single global smooth-family ideal is therefore generated by the
sixteen equations from (6), the twenty-five pairings (5), and

    smoothInverse*Disc-1.                             (10)

It is the full smooth `K2` incidence, not a finite set of samples or a
union missing coefficient charts. Proving it is the unit ideal would
prove `K2` empty on the entire smooth `(2,2)` family. Failure to finish
an elimination proves nothing about emptiness.

## 4. Exact export and one bounded prospect

The new standard-library sparse generator is
[global second-model generator](../computations/generalization_quadratic_root_global_second_model.py).
It exports
[one characteristic-zero M2 model](../computations/generalization_quadratic_root_global_second_model.m2)
and [its term/count metadata](../computations/generalization_quadratic_root_global_second_model.json).
The new algebraic consistency check verifies `T_f P_f=0` identically;
no accepted seed or previous rank verifier is invoked.

The exported system has twenty-two variables including `smoothInverse`,
sixteen first equations, twenty-five complete dual second equations, and
one discriminant inverse equation. The second equations have at most
535 terms each; the homogeneous discriminant has 1010 terms. These counts
are exact export metadata, not complexity or solvability claims.

The new proof and the exported generator algorithm passed
[the independent compression audit](2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit.md).
Exactly one bounded M2 launch was made, with the heavy quintic window
held separately. Its supervisor hit a sandbox `PermissionError` when
invoking `/bin/ps` for RSS monitoring. The M2 child had a 45-second CPU
limit. Its PID `32960` was subsequently confirmed absent with authorized
process inspection; the original exit code was not recoverable after the
supervisor failed. Captured stdout contains `MODEL_READY`, but no
`GB_COMPLETE` or unit-ideal marker. Thus the run supplies no elimination
result and no mathematical conclusion.

The input, exact source/supervisor snapshots, hashes, captured logs, and
terminal PID check are in
[the execution record](../validation/2026-10-15-quadratic-root-global-second/attempt-01-QQ-full-smooth-family/execution-record.json).
The future supervisor now checks monitor availability before launching
any child and stops safely if monitoring later fails; it was not rerun.
The quintic owner received confirmation that this process was absent
before using the next heavy computation window. No extra coefficient
chart, seed, profile, or second global launch was opened.

The accepted all-orders formal nonexistence theorem proves an existential
empty stage on the smooth family. This compression does not supply a
value of that stage. In particular no `N<=5`, all-smooth second
nonvanishing, actual-CI exclusion, or unrestricted STCI conclusion is
claimed until an exact global certificate or a new geometric proof exists.
No commit or memory update was made.
