#!/usr/bin/env python3
"""Toric weight decomposition and VGIT Plucker analysis of the O(-6) primitive triples.

Author: Gemini (explicitly authored by Gemini, not ChatGPT)
Branch: evaluate_toric_integration_stci

Standard-library only. Builds on audit_sextic_triple_spaces_2026_10_31.py to verify:
1. Exact T-invariance and centered weight profiles of the algebraic triple spaces
   V_{alg,d} for d = 4, 5, 6, and explicit formula Q_-(1, z, z^3+y, z^4+(r+3/2)zy+m) = (1-sqrt(-2))*m.
2. Intrinsic identification ker(h) = V_{triple,6} cap V_{6,2} (dimension 10) for both
   principal and algebraic orbits, where V_{6,2} = H^0(I_{C0}^2(6)) (dimension 23).
3. Intrinsic restriction Theta|_{ker(h)} : ker(h) -> k[z]_{<=6} (rank 7 on algebraic,
   rank 6 on principal cut out by the quadric-tangency hyperplane Theta(1/2) = 0),
   explaining the 24 vs 23 joint-rank split in SEXTIC_ADE_REDUCTION.md via
   rank(h, Theta) = rank(h) + rank(Theta|_{ker(h)}).
4. Endpoint proportionality [Theta_F]_d = lambda_0 * [h_F]_{d+5} for d = 7..11 on V_{alg,6},
   and surjectivity of the Plucker cubic-contact map
   Omega_3 : wedge^2 V_{triple,6} -> k[z]_{<=22} (rank 23, kernel 328) for both orbits,
   decomposing into 23 rank-1 Plucker weight blocks W in [-11, 11] and 8 zero blocks
   W in [-15, -12] union [12, 15] on the algebraic orbit.
"""
from fractions import Fraction as F
import audit_sextic_triple_spaces_2026_10_31 as ast


def centered_weight(mon, d):
    """Centered T-weight under (-2, -1, 1, 2) on (x0, x1, x2, x3)."""
    i, j, k, l = mon
    return -2 * i - j + k + 2 * l


def double_sextic_condition_matrix(d):
    """Return matrix whose kernel in S_d is V_{d,2} = H^0(I_{C0}^2(d))."""
    # Along C0 in chart x0=1: x1=z, x2=z^3+y, x3=z^4+m.
    # Vanishing to order >= 2 along C0 means coefficients of (0,0), (1,0), (0,1) in (m,y) vanish.
    mons = ast.monomials(d)
    z = {1: ast.ONE}
    x2 = {(0, 0): {3: ast.ONE}, (0, 1): {0: ast.ONE}}
    x3 = {(0, 0): {4: ast.ONE}, (1, 0): {0: ast.ONE}}

    def bmul(a, b):
        out = {}
        for (m, y), p in a.items():
            for (mm, yy), qpoly in b.items():
                if m + mm + y + yy <= 1:
                    key = (m + mm, y + yy)
                    out[key] = ast.padd(out.get(key, {}), ast.pmul(p, qpoly))
        return out

    def bpow(a, n):
        out = {(0, 0): {0: ast.ONE}}
        for _ in range(n):
            out = bmul(out, a)
        return out

    cols = []
    for i, j, k, l in mons:
        val = bmul(bmul(bpow({(0, 0): {0: ast.ONE}}, i), bpow({(0, 0): z}, j)),
                   bmul(bpow(x2, k), bpow(x3, l)))
        cols.append(val)
    keys = sorted({(m_exp, y_exp, deg)
                   for col in cols
                   for (m_exp, y_exp), poly in col.items()
                   for deg in poly})
    mat = [[col.get((m_exp, y_exp), {}).get(deg, ast.ZERO) for col in cols]
           for m_exp, y_exp, deg in keys]
    return mons, mat


def full_contact_columns(degree, data, max_order=3):
    A, B, S0, T0, gamma, z, _, _ = data
    xm = ast.scale({0: S0}, ast.q(-1))
    xy = B
    x2 = {(0, 0): {3: ast.ONE}, (1, 0): xm, (0, 1): xy}
    xm3 = ast.padd({0: T0}, ast.scale(ast.pmul(z, {0: S0}), ast.q(-3, 2)))
    xy3 = ast.padd(A, ast.scale(ast.pmul(z, B), ast.q(3, 2)))
    x3 = {(0, 0): {4: ast.ONE}, (1, 0): xm3, (0, 1): xy3}

    def bmul(a, b):
        out = {}
        for (m, y), p in a.items():
            for (mm, yy), qpoly in b.items():
                if m + mm + y + yy <= max_order:
                    key = (m + mm, y + yy)
                    out[key] = ast.padd(out.get(key, {}), ast.pmul(p, qpoly))
        return out

    def bpow(a, n):
        out = {(0, 0): {0: ast.ONE}}
        for _ in range(n):
            out = bmul(out, a)
        return out

    mons = ast.monomials(degree)
    cols = []
    for i, j, k, l in mons:
        val = bmul(bmul(bpow({(0, 0): {0: ast.ONE}}, i), bpow({(0, 0): z}, j)),
                   bmul(bpow(x2, k), bpow(x3, l)))
        cols.append(val)
    return mons, cols, gamma


def evaluate_h_theta(vec, cols, gamma):
    h = e = k = {}
    for c, col in zip(vec, cols):
        if c != ast.ZERO:
            h = ast.padd(h, ast.scale(col.get((1, 0), {}), c))
            e = ast.padd(e, ast.scale(col.get((1, 1), {}), c))
            k = ast.padd(k, ast.scale(col.get((0, 3), {}), c))
    theta = ast.padd(ast.pmul(gamma, e), ast.scale(k, ast.q(-1)))
    return h, theta


def verify_algebraic_weight_decomposition():
    data = ast.orbit("algebraic")
    profiles = {}
    for d in (4, 5, 6):
        cols, _, mat = ast.source_matrix(d, data)
        mons = ast.monomials(d)
        _, kern = ast.rref_kernel(mat, len(cols))
        by_w = {}
        for idx, mon in enumerate(mons):
            by_w.setdefault(centered_weight(mon, d), []).append(idx)
        w_profile = {}
        for w, idxs in sorted(by_w.items()):
            submat = [[row[i] for i in idxs] for row in mat]
            _, kw = ast.rref_kernel(submat, len(idxs))
            if kw:
                w_profile[w] = len(kw)
        assert sum(w_profile.values()) == len(kern)
        profiles[d] = w_profile

    assert profiles[4] == {-4: 1, 4: 1}
    assert profiles[5] == {-6: 1, -5: 1, -3: 1, -2: 1, -1: 1, 0: 1, 1: 1, 2: 1, 3: 1, 5: 1, 6: 1}
    expected_6 = {
        -8: 1, -7: 1, -6: 1, -5: 1,
        -4: 2, -3: 2, -2: 2, -1: 2,
        0: 3,
        1: 2, 2: 2, 3: 2, 4: 2,
        5: 1, 6: 1, 7: 1, 8: 1,
    }
    assert profiles[6] == expected_6

    # Check explicit quartic Q_- = (1-sqrt(-2))*x0^2*q - x1*(x0^2*x2 - x1^3)
    # expands to (1-sqrt(-2))*m identically in chart x0=1.
    mons4, cols4, _ = full_contact_columns(4, data, max_order=4)
    idx4 = {m: i for i, m in enumerate(mons4)}
    q_minus = [ast.ZERO] * len(mons4)
    q_minus[idx4[(3, 0, 0, 1)]] = (F(1), F(-1))
    q_minus[idx4[(2, 1, 1, 0)]] = (F(-2), F(1))
    q_minus[idx4[(0, 4, 0, 0)]] = (F(1), F(0))
    expansion = {}
    for c, col in zip(q_minus, cols4):
        if c != ast.ZERO:
            for k_my, poly in col.items():
                expansion[k_my] = ast.padd(expansion.get(k_my, {}), ast.scale(poly, c))
    expansion = {k: v for k, v in expansion.items() if v}
    assert expansion == {(1, 0): {0: (F(1), F(-1))}}
    return profiles


def verify_intrinsic_double_sextic_kernel_and_tangency():
    _, mat_v62 = double_sextic_condition_matrix(6)
    _, kern_v62 = ast.rref_kernel(mat_v62, 84)
    assert len(kern_v62) == 23

    results = {}
    for name in ("algebraic", "principal"):
        data = ast.orbit(name)
        cols6, _, mat6 = ast.source_matrix(6, data)
        _, kern6 = ast.rref_kernel(mat6, len(cols6))
        assert len(kern6) == 27

        # Intersection V_{triple,6} cap V_{6,2} is kernel of stacked matrix mat6 + mat_v62
        _, kern_inter = ast.rref_kernel(mat6 + mat_v62, 84)
        assert len(kern_inter) == 10

        mons6, contact_cols, gamma = full_contact_columns(6, data, max_order=3)
        h_list, theta_list = [], []
        for v in kern6:
            h, theta = evaluate_h_theta(v, contact_cols, gamma)
            h_list.append(h)
            theta_list.append(theta)

        # Kernel of h inside V_{triple,6}
        h_mat = [[h.get(d, ast.ZERO) for h in h_list] for d in range(17)]
        h_rank, h_kern_coords = ast.rref_kernel(h_mat, len(kern6))
        assert h_rank == 17
        assert len(h_kern_coords) == 10

        # Verify every vector in ker(h) lies in V_{6,2} (so ker(h) == V_{triple,6} cap V_{6,2})
        h_kern_ambient = []
        for kv in h_kern_coords:
            v = [ast.ZERO] * 84
            for c, bvec in zip(kv, kern6):
                if c != ast.ZERO:
                    for i in range(84):
                        v[i] = ast.add(v[i], ast.mul(c, bvec[i]))
            for row in mat_v62:
                total = ast.ZERO
                for x, y in zip(row, v):
                    total = ast.add(total, ast.mul(x, y))
                assert total == ast.ZERO
            h_kern_ambient.append(v)

        # Evaluate Theta on ker(h): must have degree <= 6
        theta_on_kerh = []
        for v in h_kern_ambient:
            h, theta = evaluate_h_theta(v, contact_cols, gamma)
            assert not h
            assert all(0 <= d <= 6 for d in theta)
            theta_on_kerh.append(theta)

        t_mat = [[theta.get(d, ast.ZERO) for theta in theta_on_kerh] for d in range(7)]
        t_rank_kerh, tkern_coords = ast.rref_kernel(t_mat, len(h_kern_ambient))

        if name == "algebraic":
            assert t_rank_kerh == 7
            assert len(tkern_coords) == 3
            # Check endpoint proportionality [Theta_F]_d = lambda_0 * [h_F]_{d+5} for d = 7..11
            # lambda_0 = (28 + 16*sqrt(-2)) / 81
            lam0 = (F(28, 81), F(16, 81))
            for h, theta in zip(h_list, theta_list):
                for d in range(7, 12):
                    lhs = theta.get(d, ast.ZERO)
                    rhs = ast.mul(lam0, h.get(d + 5, ast.ZERO))
                    assert lhs == rhs
        else:
            assert t_rank_kerh == 6
            assert len(tkern_coords) == 4
            # Verify exact tangency hyperplane relation Theta(1/2) = 0 on ker(h)
            half = ast.q(1, 2)
            for theta in theta_on_kerh:
                val = ast.ZERO
                for d, coeff in theta.items():
                    term = coeff
                    for _ in range(d):
                        term = ast.mul(term, half)
                    val = ast.add(val, term)
                assert val == ast.ZERO

        # Build Plucker map Omega_3 on wedge^2 V_{triple,6} (351 columns)
        pairs = [(i, j) for i in range(len(kern6)) for j in range(i + 1, len(kern6))]
        omega_cols = []
        for i, j in pairs:
            w = ast.padd(ast.pmul(h_list[i], theta_list[j]),
                         ast.scale(ast.pmul(h_list[j], theta_list[i]), ast.q(-1)))
            omega_cols.append(w)
        degs = sorted({d for w in omega_cols for d in w})
        assert degs == list(range(23))
        omat = [[w.get(d, ast.ZERO) for w in omega_cols] for d in degs]
        orank, okern = ast.rref_kernel(omat, len(pairs))
        assert orank == 23
        assert len(okern) == 328

        results[name] = {
            "h_rank": h_rank,
            "ker_h_dim": len(h_kern_coords),
            "theta_on_kerh_rank": t_rank_kerh,
            "joint_rank": h_rank + t_rank_kerh,
            "joint_ker_dim": len(tkern_coords),
            "omega3_rank": orank,
            "omega3_ker_dim": len(okern),
        }
    return results


def verify_plucker_weight_blocks_algebraic():
    data = ast.orbit("algebraic")
    cols6, _, mat6 = ast.source_matrix(6, data)
    mons6, contact_cols, gamma = full_contact_columns(6, data, max_order=3)
    by_w = {}
    for idx, mon in enumerate(mons6):
        by_w.setdefault(centered_weight(mon, 6), []).append(idx)

    weight_basis = []
    for w, idxs in sorted(by_w.items()):
        submat = [[row[i] for i in idxs] for row in mat6]
        _, kw = ast.rref_kernel(submat, len(idxs))
        for vec in kw:
            full_v = [ast.ZERO] * 84
            for c, idx in zip(vec, idxs):
                full_v[idx] = c
            h, theta = evaluate_h_theta(full_v, contact_cols, gamma)
            weight_basis.append((w, full_v, h, theta))

    assert len(weight_basis) == 27
    plucker_by_w = {}
    for i in range(27):
        for j in range(i + 1, 27):
            w1, _, h1, t1 = weight_basis[i]
            w2, _, h2, t2 = weight_basis[j]
            pw = w1 + w2
            omega = ast.padd(ast.pmul(h1, t2), ast.scale(ast.pmul(h2, t1), ast.q(-1)))
            if omega:
                assert list(omega.keys()) == [pw + 11]
            plucker_by_w.setdefault(pw, []).append(omega.get(pw + 11, ast.ZERO))

    assert sorted(plucker_by_w.keys()) == list(range(-15, 16))
    nonzero_weights = [pw for pw, vals in sorted(plucker_by_w.items()) if any(v != ast.ZERO for v in vals)]
    zero_weights = [pw for pw, vals in sorted(plucker_by_w.items()) if all(v == ast.ZERO for v in vals)]
    assert nonzero_weights == list(range(-11, 12))
    assert zero_weights == [-15, -14, -13, -12, 12, 13, 14, 15]
    return len(plucker_by_w), len(nonzero_weights), len(zero_weights)


def main():
    profiles = verify_algebraic_weight_decomposition()
    print("Algebraic triple T-weight profiles:")
    for d in (4, 5, 6):
        print(f"  d={d}: dim={sum(profiles[d].values())}, centered weights={profiles[d]}")

    res = verify_intrinsic_double_sextic_kernel_and_tangency()
    for name in ("algebraic", "principal"):
        r = res[name]
        print(f"{name}: rank(h)={r['h_rank']}, dim ker(h)={r['ker_h_dim']}, "
              f"rank(Theta|_ker(h))={r['theta_on_kerh_rank']}, "
              f"rank(h,Theta)={r['joint_rank']}, dim ker(h,Theta)={r['joint_ker_dim']}, "
              f"rank(Omega_3)={r['omega3_rank']}, dim ker(Omega_3)={r['omega3_ker_dim']}")

    n_blocks, n_nz, n_z = verify_plucker_weight_blocks_algebraic()
    print(f"Algebraic wedge^2 V_{{alg,6}} Plucker weights: {n_blocks} blocks (-15..15); "
          f"{n_nz} rank-1 blocks (-11..11) and {n_z} zero blocks ([-15,-12] U [12,15]).")
    print("All intrinsic double-sextic kernel, quadric-tangency hyperplane, and Plucker VGIT checks passed.")


if __name__ == "__main__":
    main()
