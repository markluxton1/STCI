#!/usr/bin/env python3
"""Exact two-chart Cech calculation for H^0(I^2/I^(n+1))(6), n <= 6.

Uses the accepted balanced normal-coordinate transition in
generalization_quadratic_root_global_second_model.py. Arithmetic is rational.
"""
from fractions import Fraction as F
import json
import sympy as sp

# Sparse Laurent polynomial: (u exponent, v exponent, z exponent) -> Q.
Poly = dict[tuple[int, int, int], F]


def clean(p):
    return {m: c for m, c in p.items() if c}


def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, F(0)) + c
    return clean(out)


def scale(p, c):
    return clean({m: c * v for m, v in p.items()})


def mul(p, q, n):
    out = {}
    for (i, j, k), a in p.items():
        for (r, s, t), b in q.items():
            if i + j + r + s <= n:
                key = (i + r, j + s, k + t)
                out[key] = out.get(key, F(0)) + a * b
    return clean(out)


def power(p, e, n):
    out = {(0, 0, 0): F(1)}
    for _ in range(e):
        out = mul(out, p, n)
    return out


def degree(m):
    return m[0] + m[1]


def homogeneous_part(p, m):
    return {key: c for key, c in p.items() if degree(key) == m}


def coordinates(n):
    z = {(0, 0, 1): F(1)}
    u = {(1, 0, 0): F(1)}
    v = {(0, 1, 0): F(1)}
    T = add(power(z, 4, n), u, scale(mul(z, v, n), F(3, 2)))
    # T^-1 = z^-4 sum_j (-z^-4 u - 3/2 z^-3 v)^j.
    perturb = {(1, 0, -4): F(1), (0, 1, -3): F(3, 2)}
    Tinv = {(0, 0, -4): F(1)}
    for j in range(1, n + 1):
        Tinv = add(Tinv, scale(mul({(0, 0, -4): F(1)}, power(perturb, j, n), n), F((-1) ** j)))
    W = mul(add(power(z, 3, n), v), Tinv, n)
    AP = add(mul(z, Tinv, n), scale(power(W, 3, n), F(-1)))
    BP = add(Tinv, scale(power(W, 4, n), F(-1)))
    UP = scale(AP, F(1, 2))
    VP = add(scale(mul(W, AP, n), F(-3)), scale(BP, F(2)))
    return T, W, UP, VP


def transition(pinf, n):
    T, W, UP, VP = coordinates(n)
    inside = {}
    for (i, j, e), c in pinf.items():
        # e is a Laurent exponent in z; chart-∞ polynomials have e <= 0.
        if e > 0:
            raise ValueError("chart-infinity coefficient has positive z exponent")
        term = mul(power(UP, i, n), power(VP, j, n), n)
        term = mul(term, power(W, -e, n), n)
        inside = add(inside, scale(term, c))
    return mul(power(T, 6, n), inside, n)


def monomials(m):
    return [(i, m - i) for i in range(m + 1)]


def mismatch(p0, pi, m):
    return homogeneous_part(add(p0, scale(transition(pi, m), F(-1))), m)


def gaps(m):
    L = 24 - 7 * m
    return [(i, m - i, k) for i, j in monomials(m) for k in range(L + 1, 0)]


def canonical_lift(p0, pi, m):
    """Return canonical local lifts if the Laurent gap obstruction vanishes."""
    L = 24 - 7 * m
    r = mismatch(p0, pi, m)
    bad = [key for key in r if L < key[2] < 0]
    if bad:
        return None
    c0, ci = {}, {}
    for (i, j, k), c in r.items():
        if k >= 0:
            c0[(i, j, k)] = -c
        elif k <= L:
            # z^L times w^(L-k) has z-exponent k.
            ci[(i, j, k - L)] = c
    return add(p0, c0), add(pi, ci)


def combine(basis, coefficients):
    p0, pi = {}, {}
    for (a, b), c in zip(basis, coefficients):
        c = F(c)
        if c:
            p0, pi = add(p0, scale(a, c)), add(pi, scale(b, c))
    return p0, pi


def source_projection(basis):
    """Matrix of restriction to the 33-dimensional order-two symbol space."""
    cols = []
    for p0, _ in basis:
        col = []
        for i, j in monomials(2):
            for k in range(11):
                col.append(p0.get((i, j, k), F(0)))
        cols.append(col)
    return sp.Matrix(33, len(basis), lambda i, j: cols[j][i])


def compute(max_n=6, return_basis=False):
    # H^0(Sym^2 E(6)): 3 normal monomials, each with 11 base monomials.
    basis = []
    for i, j in monomials(2):
        for k in range(11):
            basis.append(({(i, j, k): F(1)}, {(i, j, k - 10): F(1)}))
    rows = [{"order": 2, "dimension": len(basis), "obstruction_rank": 0,
             "obstruction_equations": 0, "order_two_projection_rank": source_projection(basis).rank(),
             "order_two_projection_kernel": 0}]
    pure_cubic_rank = None
    q3_check = None

    for m in range(3, max_n + 1):
        gs = gaps(m)
        old_proj = source_projection(basis)
        columns = []
        for p0, pi in basis:
            r = mismatch(p0, pi, m)
            columns.append([r.get(key, F(0)) for key in gs])
        if gs:
            mat = sp.Matrix([[columns[j][i] for j in range(len(columns))] for i in range(len(gs))])
        else:
            mat = sp.zeros(0, len(basis))
        null = mat.nullspace()
        restricted_pure_cubic_rank = None
        if m == 4:
            # At order three the chosen basis is 33 lifted quadratic symbols,
            # followed by the 16 independent pure cubic symbols.
            restricted_pure_cubic_rank = mat[:, 33:49].rank()
        new_basis = []
        for coeffs in null:
            p0, pi = combine(basis, list(coeffs))
            lifted = canonical_lift(p0, pi, m)
            if lifted is None:
                raise ArithmeticError("kernel vector retained a nonzero Cech obstruction")
            new_basis.append(lifted)
        L = 24 - 7 * m
        if L >= 0:
            for i, j in monomials(m):
                for k in range(L + 1):
                    new_basis.append(({(i, j, k): F(1)}, {(i, j, k - L): F(1)}))
        proj = source_projection(new_basis)
        row = {"order": m, "dimension": len(new_basis),
               "obstruction_rank": len(basis) - len(null),
               "obstruction_equations": len(gs),
               "order_two_projection_rank": proj.rank(),
               "order_two_projection_kernel": len(new_basis) - proj.rank()}
        if restricted_pure_cubic_rank is not None:
            pure_cubic_rank = restricted_pure_cubic_rank
            row["quartic_obstruction_rank_on_pure_cubic_subspace"] = pure_cubic_rank
        if m == 5:
            kernel = old_proj.nullspace()
            if kernel:
                restricted = mat * sp.Matrix.hstack(*kernel)
                row["quintic_obstruction_rank_on_zero_quadratic_projection"] = restricted.rank()
                # For the expected one-dimensional kernel, test q^3 in the
                # x0=1 chart: q=u+z*v/2, so q^3 has coefficients below.
                if len(kernel) == 1:
                    p0, pi = combine(basis, list(kernel[0]))
                    # Explicit expansion (u + z v/2)^3.
                    q3 = {}
                    import math
                    for i in range(4):
                        # i powers of u, 3-i powers of z*v/2.
                        q3[(i, 3-i, 3-i)] = F(math.comb(3, i), 2 ** (3-i))
                    actual = homogeneous_part(p0, 3)
                    scalar = None
                    for key, value in q3.items():
                        if value:
                            scalar = actual.get(key, F(0)) / value
                            break
                    q3_check = (scalar is not None and
                                actual == {key: scalar * value for key, value in q3.items()})
                    row["zero_quadratic_projection_is_q_cubed"] = q3_check
        rows.append(row)
        basis = new_basis
    return (rows, basis) if return_basis else rows


if __name__ == "__main__":
    print(json.dumps({"field": "QQ", "object": "H^0(I^2/I^(n+1))(6)",
                      "method": "two-chart Cech lifting in balanced coordinates",
                      "rows": compute()}, indent=2))
