# Fixed quartic normal bundle: independent Jacobian certificate

Date: 2026-10-10. Auditor: `quartic_normal_bundle_audit`.
Status: **PROVED HERE as an independent verification of the existing P-009**.
The possible application to a normalization ribbon is stated separately and
requires its geometric hypotheses; this note makes no global STCI claim and
edits no canonical frontier file.

Let `k` be algebraically closed of characteristic zero, and let

    j:P1 -> P3, [s:t] -> [s^4:s^3t:st^3:t^4].

Then `j` is a closed immersion. Its image is covered by `x0!=0` and
`x3!=0`. On the first chart the inverse parameter is `x1/x0=t/s`; on
the second it is `x2/x3=s/t`. These chart maps identify the image with
the corresponding affine lines, including both endpoints. In particular
the curve is smooth and its normal sheaf is a rank-two vector bundle.

## 1. Euler and homogeneous derivative presentation

The pulled-back Euler sequence and the tangent sequence give

    0 -> O_P1(1)^2 -> O_P1(4)^4 -> N_C0/P3 -> 0.

To justify the left term, the two homogeneous partial derivative columns
map `O(1)^2` into `O(4)^4`. Their span contains the radial Euler column
since `s*d_s j+t*d_t j=4*j`; after quotienting that radial column the
induced map is the actual tangent map. Characteristic zero ensures `4`
is invertible. The resulting rank-two subbundle is therefore precisely
the preimage of `T_P1` in the Euler bundle. Dualizing yields

    0 -> N_C0/P3^* -> O_P1(-4)^4 --J--> O_P1(-1)^2 -> 0,

where

    J = [[4s^3,3s^2t,t^3,0],
         [0,s^3,3st^2,4t^3]].

The `4x2` cubic matrix

    V = [[-2t^3,0],
         [3st^2,t^3],
         [-s^3,-3s^2t],
         [0,2s^3]]

satisfies `JV=0`. Its six maximal minors are, in row-pair order,

    -2t^6, 6s^2t^4, -4s^3t^3,
    -8s^3t^3, 6s^4t^2, -2s^6.

They have no common projective zero: the first is nonzero when `t!=0`
and the last when `s!=0`. Thus `V` gives a rank-two subbundle

    O_P1(-7)^2 -> ker(J)=N_C0/P3^*.

It is an isomorphism on every fiber, hence an isomorphism of vector
bundles. Therefore

    N_C0/P3 = O_P1(7) (+) O_P1(7).

This proves the splitting without a generic-rank argument or a computer
inference. The exact Macaulay2 companion checks the displayed identities
and projective rank conditions over `QQ`. All coefficients and minors
remain valid after any extension of an algebraically closed
characteristic-zero ground field.

## 2. Independent quadratic-kernel check

Write a potential degree-two derivative syzygy as

    u0=a0 s^2+a1 st+a2 t^2,
    u1=b0 s^2+b1 st+b2 t^2,
    u2=c0 s^2+c1 st+c2 t^2,
    u3=d0 s^2+d1 st+d2 t^2.

Comparing the six coefficients in each row of `J*u=0` gives

    4a0=0, 4a1+3b0=0, 4a2+3b1=0,
    3b2+c0=0, c1=0, c2=0,
    b0=0, b1=0, b2+3c0=0,
    3c1+4d0=0, 3c2+4d1=0, 4d2=0.

The only residual pair is `c0=-3b2`, `b2+3c0=-8b2=0`, so all
twelve coefficients vanish. The companion verifies that the determinant
of this `12x12` coefficient matrix has absolute value `2^15`.
Consequently `H0(N^*(6))=0`, independently excluding `O(6)(+)O(8)`.
The two cubic columns above then provide the full splitting directly.

The repository already contains this splitting as P-009 in
[`RESEARCH_RECORD.md`](../RESEARCH_RECORD.md), via a two-chart conormal
calculation and [`verify_normal_bundle.py`](../computations/verify_normal_bundle.py).
The new source supplies a short, independently runnable certificate under
the currently available Macaulay2 runtime. It does not count the old
result as a new theorem.

## 3. Conditional ribbon obstruction and its exact limitation

For any line bundle `J0=O_P1(-8)`, the proved splitting gives

    Hom_C0(I_C0/I_C0^2,J0)
        = H0(O_P1(-1))^2 = 0.

Hence a scheme morphism `r:R -> P3` whose reduced restriction identifies
`R_red` with `C0`, and whose square-zero ideal is `J0`, cannot induce a
nonzero global map

    I_C0/I_C0^2 -> J0.

If `r` is generically an immersion of the ribbon, this map is necessarily
generically nonzero, so such an `r` cannot exist. The implication follows
directly by pulling back the ambient ideal into the nilpotent ideal:
products of two pulled-back ideal sections vanish, so the map factors
through the conormal bundle. If the map were zero at the generic point,
the morphism would factor there through the reduced curve and could not
be a ribbon immersion.

For the root's proposed application, establishing the *global* ribbon,
its square-zero ideal `O(-8)`, and generic immersion is indispensable.
In particular a doubled Weil divisor on a singular surface need not be
a ribbon without the Cohen--Macaulay and duality argument. This audit
does not replace those required geometric checks by tangent data.

Here is that general ribbon argument, independently of the unresolved
carrier hypotheses. Suppose a normal surface `S` contains a smooth
reduced integral curve `c`, the effective Weil divisor `2c` is Cartier,
and `D=2c` is Cohen--Macaulay. Normality identifies `I_c` with the
functions of valuation at least one at the generic point of `c`, and
`I_D=O_S(-2c)` with valuation at least two. Consequently
`I_c^2 subset I_D`, so `J=I_c/I_D` is square-zero. The sequence

    0 -> J -> O_D -> O_c -> 0

and the depth lemma give depth one for `J` at every point of `c`.
Equivalently, any parameter of the smooth local curve ring is a
nonzerodivisor on `J`: the associated primes of the CM curve `D` are
its generic points, and the parameter avoids the sole generic prime.
The generic rank of `J` over `c` is one, from the length-two quotient of
the normal-surface DVR at the generic point. Thus `J` is a torsion-free
rank-one sheaf on a smooth curve and therefore a line bundle. This
proves that `D` is a ribbon; no regularity of `S` at all points of `c`
is required for this step.

If `S` is additionally Gorenstein near `c`, Cartier adjunction makes
`omega_D=omega_S(D)|D` invertible. Finite duality for `c subset D` gives

    omega_c=Hom_D(O_c,omega_D)
           =J tensor omega_D|c,

because the annihilator of `J` in a ribbon is `J` itself. Therefore

    J=omega_c tensor (omega_D|c)^(-1).

In particular, **conditional on** `c=P1`, `2c~2H`, `H.c=4`, and
`K_S.c=-2`, one obtains `deg(omega_D|c)=6`, hence `J=O(-8)`.
A finite normalization morphism to a quartic carrier is an isomorphism
away from the conductor. If `c` is not contained in that conductor,
its restriction to `D` is generically a ribbon immersion, so the
nonzero-conormal-map contradiction applies. This establishes the
root's proposed mechanism from these explicit hypotheses. Verifying
that every carrier in the intended stratum satisfies them remains the
root's separate geometric audit.

## 4. Exact execution evidence

The source is
[`verify_session_quartic_normal_bundle_2026_10_10.m2`](../computations/verify_session_quartic_normal_bundle_2026_10_10.m2).
Its command, source hash, raw stdout/stderr, exit code, and assertion count
are recorded in the sibling validation directory
`research/validation/2026-10-10-quartic-normal-bundle-independent-audit/`.
