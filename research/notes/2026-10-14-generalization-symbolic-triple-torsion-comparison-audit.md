# Symbolic triple torsion comparison: independent structural audit

Date: 2026-10-14. Worker: `socle_audit/higher_moments`.
Status: **PROVED NEW COMPARISON AND ARITHMETIC CONSEQUENCE, CONDITIONAL
ONLY ON THE EXPLICIT ACCEPTED INPUTS BELOW.** No canonical file edited.

Accepted inputs, not reverified: the fixed C0 normal/conormal coefficients;
the ordinary curvilinear CI free-layer and pointwise Frobenius theorem;
the local power-socle identity; and the fixed constant-direction pole
obstruction forcing `deg E>=2` for the symbolic triple. This assessment
audits the quotient comparison and its new implications, rather than
assuming the symbolic triple is a complete intersection.

Let X be a normal integral carrier of C0, of degree a, with a mate.
At P let r be the actual local Cartier index of C0. A regular local
function h has divisor rC, and `W_r=O_X/(h)` is a local complete
intersection of generic length r. Set

    Z_3 = O_X / I_C^(3),
    L_1(Z_3) = I_C / (I_C^2 + I_C^(3)),
    E_P = length torsion L_1(Z_3).

The symbolic quotient is pure and has generic length three. Its
first-layer relation line has the common saturated F_1 direction;
in the constant-direction branch ell=7 it is
`K_1=O(-7)(-E)`. None of these statements requires Z_3 to be lci.

## 1. Comparison at r>=3

The valuation description of the symbolic power gives
`(h) subset I_C^(3)` when r>=3, and hence a quotient `W_r -> Z_3`.
Complete along the smooth curve parameter and use `R=k[[t]]`.
Let V be the ambient first conormal module, free of rank two over R.
Write

    M_r = kernel(V -> L_1(W_r)),
    M_3 = kernel(V -> L_1(Z_3)).

Then `M_r subset M_3`. Their generic rank-one relation space is the
same F_1 direction, so their R-saturations equal a common line L in V.
Therefore

    torsion L_1(W_r) = L/M_r,
    torsion L_1(Z_3) = L/M_3,

and the map of torsion modules is surjective. In particular

    E_P <= length T_1(W_r)_P
        <= sum_i length T_i(W_r)_P
        = r D_r,P / 2.                         (1)

The perfect Frobenius pairing is used on the actual complete
intersection W_r. It is never used on Z_3. Thus no hidden lci or
Gorenstein assumption on the symbolic triple enters (1).

## 2. Comparison at r=2 and r=1

For r=2, normality and the height-one valuation description give

    I_C^(3) = h I_C.

Indeed division by h subtracts exactly two units of curve valuation
and no valuation at any other prime. The ambient first symbols of
`h I_C` vanish: both factors lie in the ambient curve ideal. Thus
the only first-symbol relation is the carrier F_1, and

    E_P = A_F,P.                               (2)

For r=1, the smooth curve is Cartier on the normal surface; the
surface is smooth there, so `E_P=A_F,P=0`. This is the accepted
smooth-Cartier case, not a new general primitive hypothesis.

Subsequent strengthening, independently reconstructed by `socle_audit`
and the root: the relative CI W_r is automatically primitive when
r<=3. Its special Artinian CI fiber has length below four, hence cannot
have embedding dimension two; Nakayama then makes the whole finite
free algebra R[z]/(z^r). Thus D_2=D_3=0 and E_P=0 for r=3. The full
proof is recorded in
`2026-10-14-generalization-normal-carrier-symbolic-triple-certificate.md`,
Section 2. In (3)--(4), positive defects may therefore be restricted to
r>=4. The s=3/no-index-two case in (5) is impossible; the displayed
2/3 bound is an earlier necessary conditional inequality, not evidence
for a surviving positive-defect index-three model.

Summing (1)--(2), the accepted fixed-direction obstruction gives

    2 <= deg E
      <= sum_(r=2) A_F,P + (1/2) sum_(r>=3) r D_r,P.       (3)

## 3. Positive defects and parity

If there are no index-two points, (3) forces at least one positive
`D_r,P` with r>=3. The pointwise Frobenius identity implies
`r D_r,P` is even; consequently odd r forces `D_r,P>=2` whenever
positive, while even r forces at least one. Thus

    sum_P D_r,P/r >= min_(actual r>=3) delta_r/r,
    delta_r = 1 for r even, 2 for r odd.         (4)

If only r<=s is known and index two is absent, this minimum can be
bounded uniformly by

    eta_3 = 2/3,
    eta_s = 1/s       for even s>=4,
    eta_s = 1/(s-1)   for odd s>=5.              (5)

With no r>=3 available, (3) already contradicts the absence of
index two. The weaker universal estimate from (4) is `1/s`.

## 4. A one-unit improvement of the normal index bound

Let `A=sum_P A_F,P`, `A_2=sum_(r=2) A_F,P`, and retain the accepted
identity

    Q = ell-16/a = sum_P (A_F,P+D_r,P)/r.

Suppose s>=3 bounds all actual indices and ell=7, so the accepted
constant-direction pole obstruction supplies (3). Then

    Q - A/s >= 1/s.                            (6)

There are two exhaustive cases. If a `D_r,P` is positive, it is an
integer at least one and r<=s, so its contribution is at least `1/s`.
If every `D_r,P=0`, equation (3) forces `A_2>=2`, and

    Q-A/s >= A_2(1/2-1/s)
            >= (s-2)/s >= 1/s.

Thus index-two points do not prevent the weaker improvement (6).
In the ell=7 branch, `A=4a-7`, and therefore

    s(7-16/a) >= 4a-6,
    4a^2-(7s+6)a+16s <= 0.                     (7)

When index two is absent, replace `1/s` in (6) by the sharper
`eta_s` of (5), or use the actual-index minimum in (4).

The integer branch ell<=6 is also compatible with (7). The accepted
original bound and its monotonicity in ell give

    4a^2-(6s+8)a+16s <= 0.

For s>=2 the left side in (7) is smaller by `(s-2)a`, so this implies
(7). Hence, after accepting the fixed-direction pole obstruction,
(7) can be used for all ell<=7 with s>=3. The case s<=2 is already
covered by the accepted bounded-index exclusion, and is not inferred
from the new constant-direction argument.

## 5. Scope

The comparison applies to a pure symbolic triple even if it has
special-point non-lci structure. It uses the actual local index and
full CI defect of W_r; surface multiplicity, first-jet smoothness, or
index lcm does not replace those data. This is a stronger necessary
index/degree inequality, not an exclusion of unrestricted normal
carriers, nonnormal carriers, or all STCI presentations of C0.
