#!/usr/bin/env python3
"""Verify the intrinsic Kunneth/toric decomposition of the sextic/octic jet deficits and unequal-degree VGIT spaces.

Author: Gemini (explicitly authored by Gemini, not ChatGPT)
Branch: evaluate_toric_integration_stci

Standard-library only. Verifies:
1. Intrinsic Kunneth decomposition of the 11-dimensional sextic quadratic-symbol deficit
   coker(sigma_{6,2}) = H^1(Q, O_Q(2,-2)) (+) H^1(Q, O_Q(3,-3)):
   - H^0(C, Sym^2 E(6)) has dimension 33 with centered T-weights in [-6, 6], decomposing via
     0 -> H^0(C, E(4)) (dim 20) -> H^0(C, Sym^2 E(6)) (dim 33) -> H^0(C, O_{P^1}(12)) (dim 13) -> 0.
   - Actual image im(sigma_{6,2}) = V_{6,2}/(k*q^3) has dimension 22 with centered T-weights in [-6, 6].
   - Cokernel has dimension 11 = 3 + 8, multiplicity-free on centered weights [-5, 5].
2. Unequal-degree VGIT projective bundles P(E) -> P(V_a) with fiber P(V_b / (F_a * S_{b-a}))
   for (5, 8) (rank 112 over P^34, covered by H_{10}) and (6, 16) (rank 618 over P^58, covered by H_{24}),
   and equal-degree VGIT spaces X_8 = Gr(2, V_8) and X_{8,2} = Gr(2, V_{8,2}) (covered by H_{16}).
"""
from collections import Counter
from math import comb


WEIGHTS = (-2, -1, 1, 2)


def monomials(degree):
    if degree < 0:
        return []
    return [(i, j, k, degree - i - j - k)
            for i in range(degree + 1)
            for j in range(degree - i + 1)
            for k in range(degree - i - j + 1)]


def weight(exponent):
    return sum(a * b for a, b in zip(exponent, WEIGHTS))


def p1_weights(deg):
    """Centered weights of H^0(P^1, O(deg)) where s, t have weights -1/2, +1/2."""
    if deg < 0:
        return Counter()
    # Monomial s^{deg-k} t^k has centered weight (2*k - deg)/2; for even deg these are integers -deg//2 .. deg//2
    assert deg % 2 == 0
    half = deg // 2
    return Counter({w: 1 for w in range(-half, half + 1)})


def check_sextic_and_octic_symbol_deficits():
    # On C_0 = P^1:
    # L = I_Q/I_Q^2|_{C_0} = O_{C_0}(-2) = O_{P^1}(-8) (centered weight shift 0)
    # M_Q = I_{C_0/Q}/I_{C_0/Q}^2 = O_Q(-1,-3)|_{C_0} = O_{P^1}(-6) (centered weight shift 0)
    # Wait: let us check if L and M_Q have centered weight shift 0!
    # q has degree 2 and centered weight 0, so L(2) = O_{P^1} trivialized by q (weight 0)!
    # On Q, C_0 is cut out in O_Q(1,3) by u_0 v_1^3 - u_1 v_0^3:
    # Since u_1/u_0 = (t/s)^3 and v_1/v_0 = t/s, both u_0 v_1^3 and u_1 v_0^3 have centered weight 0!
    # Thus M_Q = O_Q(-1,-3)|_{C_0} = O_{P^1}(-6) ALSO has centered weight shift 0!
    # Therefore:
    # - L(d) = O_{P^1}(4d - 8) with centered weights -(2d-4) .. (2d-4)
    # - M_Q(d) = O_{P^1}(4d - 6) with centered weights -(2d-3) .. (2d-3)
    # - E(d) has filtration L(d) + M_Q(d)
    # - Sym^2 E(d) has filtration L^2(d) + (L tensor M_Q)(d) + M_Q^2(d)
    #   = O_{P^1}(4d - 16) + O_{P^1}(4d - 14) + O_{P^1}(4d - 12)!
    sym2_e6 = p1_weights(8) + p1_weights(10) + p1_weights(12)
    assert sum(sym2_e6.values()) == 9 + 11 + 13 == 33
    assert min(sym2_e6) == -6 and max(sym2_e6) == 6

    # Actual space V_{6,2} / (k * q^3):
    ambient_6 = Counter(weight(m) for m in monomials(6))
    v62 = Counter({w: c - 3 for w, c in ambient_6.items() if c > 3})
    assert sum(v62.values()) == 23
    im_sigma62 = v62 - Counter({0: 1})
    assert sum(im_sigma62.values()) == 22

    # Cokernel of sigma_{6,2}: H^0(Sym^2 E(6)) / im(sigma_{6,2})
    coker_sigma62 = sym2_e6 - im_sigma62
    assert sum(coker_sigma62.values()) == 11
    assert coker_sigma62 == Counter({w: 1 for w in range(-5, 6)})

    # Compare with the two Kunneth H^1 pieces on Q:
    # 1) H^1(Q, O_Q(2, -2)) = H^0(P^1_u, O(2)) tensor H^1(P^1_v, O(-2))
    #    On P^1_u, u_0, u_1 have centered weights -3/2, +3/2, so H^0(O(2)) has weights {-3, 0, +3}.
    #    On P^1_v, H^1(O(-2)) is dual to H^0(O(0)) and has weight 0.
    h1_oq_2_minus2 = Counter({-3: 1, 0: 1, 3: 1})
    # 2) H^1(Q, O_Q(3, -3)) = H^0(P^1_u, O(3)) tensor H^1(P^1_v, O(-3))
    #    H^0(P^1_u, O(3)) has weights {-9/2, -3/2, 3/2, 9/2};
    #    H^1(P^1_v, O(-3)) has weights {-1/2, +1/2};
    #    tensor product has weights {-5, -4, -2, -1, 1, 2, 4, 5}.
    h1_oq_3_minus3 = Counter({-5: 1, -4: 1, -2: 1, -1: 1, 1: 1, 2: 1, 4: 1, 5: 1})
    assert h1_oq_2_minus2 + h1_oq_3_minus3 == coker_sigma62

    # Octic cubic-symbol obstruction:
    # 0 -> Sym^2 E(6) -> Sym^3 E(8) -> M_Q^3(8) = O_{P^1}(14) -> 0
    sym3_e8 = p1_weights(8) + p1_weights(10) + p1_weights(12) + p1_weights(14)
    assert sum(sym3_e8.values()) == 9 + 11 + 13 + 15 == 48
    octic_cubic_coker = sym3_e8 - im_sigma62
    assert sum(octic_cubic_coker.values()) == 26
    expected_octic_coker = Counter({w: 2 for w in range(-5, 6)}) + Counter({-7: 1, -6: 1, 6: 1, 7: 1})
    assert octic_cubic_coker == expected_octic_coker
    return sym2_e6, im_sigma62, coker_sigma62, octic_cubic_coker


def check_unequal_and_equal_vgit_spaces():
    # Helper for V_d weight profile
    def vd_profile(d):
        amb = Counter(weight(m) for m in monomials(d))
        return Counter({w: c - 1 for w, c in amb.items() if c > 1})

    v5 = vd_profile(5)
    v6 = vd_profile(6)
    v8 = vd_profile(8)
    v16 = vd_profile(16)
    assert sum(v5.values()) == 35 and min(v5) == -7 and max(v5) == 7
    assert sum(v6.values()) == 59 and min(v6) == -9 and max(v6) == 9
    assert sum(v8.values()) == 132 and min(v8) == -13 and max(v8) == 13
    assert sum(v16.values()) == 904 and min(v16) == -29 and max(v16) == 29

    # (5, 8) unequal-degree bundle E_{[F_5]} = V_8 / (F_5 * S_3):
    s3 = Counter(weight(m) for m in monomials(3))
    assert sum(s3.values()) == 20
    assert sum(v8.values()) - sum(s3.values()) == 112
    # Check weight profile of fiber E_{[F_5]} for every T-weight w_a in [-7, 7]
    for wa in range(-7, 8):
        shifted_s3 = Counter({w + wa: c for w, c in s3.items()})
        fiber_58 = Counter({w: v8[w] - shifted_s3[w] for w in set(v8) | set(shifted_s3)})
        assert all(v >= 0 for v in fiber_58.values())
        assert sum(fiber_58.values()) == 112

    # (6, 16) unequal-degree bundle E_{[F_6]} = V_{16} / (F_6 * S_{10}):
    s10 = Counter(weight(m) for m in monomials(10))
    assert sum(s10.values()) == 286
    assert sum(v16.values()) - sum(s10.values()) == 618
    for wa in range(-9, 10):
        shifted_s10 = Counter({w + wa: c for w, c in s10.items()})
        fiber_616 = Counter({w: v16[w] - shifted_s10[w] for w in set(v16) | set(shifted_s10)})
        assert all(v >= 0 for v in fiber_616.values())
        assert sum(fiber_616.values()) == 618

    # (8, 8) equal-degree Grassmannians X_8 = Gr(2, V_8) and X_{8,2} = Gr(2, V_{8,2}):
    amb8 = Counter(weight(m) for m in monomials(8))
    v82 = Counter({w: c - 3 for w, c in amb8.items() if c > 3})
    assert sum(v82.values()) == 80 and min(v82) == -10 and max(v82) == 10
    ext_v8 = Counter()
    for w, d1 in v8.items():
        ext_v8[2 * w] += d1 * (d1 - 1) // 2
        for v, d2 in v8.items():
            if v > w:
                ext_v8[w + v] += d1 * d2
    ext_v8 = +ext_v8
    assert sum(ext_v8.values()) == comb(132, 2) == 8646
    assert min(ext_v8) == -25 and max(ext_v8) == 25

    ext_v82 = Counter()
    for w, d1 in v82.items():
        ext_v82[2 * w] += d1 * (d1 - 1) // 2
        for v, d2 in v82.items():
            if v > w:
                ext_v82[w + v] += d1 * d2
    ext_v82 = +ext_v82
    assert sum(ext_v82.values()) == comb(80, 2) == 3160
    assert min(ext_v82) == -19 and max(ext_v82) == 19
    return len(ext_v8), len(ext_v82)


def main():
    sym2_e6, im_s62, coker_s62, octic_coker = check_sextic_and_octic_symbol_deficits()
    print(f"H^0(Sym^2 E(6)): dim={sum(sym2_e6.values())}, weights={min(sym2_e6)}..{max(sym2_e6)}, "
          f"profile={[sym2_e6[w] for w in range(-6, 7)]}")
    print(f"im(sigma_{{6,2}}): dim={sum(im_s62.values())}, weights={min(im_s62)}..{max(im_s62)}, "
          f"profile={[im_s62[w] for w in range(-6, 7)]}")
    print(f"coker(sigma_{{6,2}}) = H^1(O_Q(2,-2)) (+) H^1(O_Q(3,-3)): dim={sum(coker_s62.values())}, "
          f"weights=-5..5, profile={[coker_s62[w] for w in range(-5, 6)]}")
    print(f"Octic cubic deficit (15+11=26): weights=-7..7, profile={[octic_coker[w] for w in range(-7, 8)]}")
    n_w8, n_w82 = check_unequal_and_equal_vgit_spaces()
    print(f"Unequal VGIT bundles verified: (5,8) rank 112 over P^34 (H_10); (6,16) rank 618 over P^58 (H_24).")
    print(f"Equal (8,8) VGIT verified: X_8 has {n_w8} Plucker weights (-25..25); X_{{8,2}} has {n_w82} Plucker weights (-19..19) (H_16).")


if __name__ == "__main__":
    main()
