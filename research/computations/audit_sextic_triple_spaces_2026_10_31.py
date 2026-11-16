#!/usr/bin/env python3
"""Exact degree-four-to-six source spaces for the three O(-6) triples.

Standard-library only. Reuses the moving-chart/second-order substitution of
audit_mf6_e1_primitive_2026_10_07.py. Computes the coefficient-map ranks and,
in degree six, the images of h and Theta=gamma*E-K in the first contact test.
Fixed C0, characteristic zero; the algebraic directions are over Q(sqrt(-2)).
"""
from fractions import Fraction as F

# Q(a), a^2=-2; pairs are (rational part, a-coefficient).
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def q(n, d=1):
    return (F(n, d), F(0))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0] * b[0] - 2 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def inv(a):
    norm = a[0] * a[0] + 2 * a[1] * a[1]
    assert norm
    return (a[0] / norm, -a[1] / norm)


def scale(a, c):
    return {i: mul(v, c) for i, v in a.items() if mul(v, c) != ZERO}


def padd(a, b):
    out = dict(a)
    for i, v in b.items():
        w = add(out.get(i, ZERO), v)
        if w == ZERO:
            out.pop(i, None)
        else:
            out[i] = w
    return out


def pmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            k = i + j
            w = add(out.get(k, ZERO), mul(x, y))
            if w == ZERO:
                out.pop(k, None)
            else:
                out[k] = w
    return out


def yadd(a, b):
    return tuple(padd(x, y) for x, y in zip(a, b))


def ymul(a, b):
    out = ({}, {}, {})
    for i in range(3):
        for j in range(3 - i):
            row = list(out)
            row[i + j] = padd(row[i + j], pmul(a[i], b[j]))
            out = tuple(row)
    return out


def ypow(a, n):
    out = ({0: ONE}, {}, {})
    for _ in range(n):
        out = ymul(out, a)
    return out


def monomials(d):
    return [(i, j, k, d - i - j - k)
            for i in range(d, -1, -1)
            for j in range(d - i, -1, -1)
            for k in range(d - i - j, -1, -1)]


def rank_columns(cols):
    if not cols:
        return 0
    a = [[v for v in row] for row in zip(*cols)]
    nrow, ncol, pivot_row = len(a), len(cols), 0
    for c in range(ncol):
        p = next((r for r in range(pivot_row, nrow) if a[r][c] != ZERO), None)
        if p is None:
            continue
        a[pivot_row], a[p] = a[p], a[pivot_row]
        iv = inv(a[pivot_row][c])
        a[pivot_row] = [mul(x, iv) for x in a[pivot_row]]
        for r in range(nrow):
            if r != pivot_row and a[r][c] != ZERO:
                f = a[r][c]
                a[r] = [sub(x, mul(f, y)) for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == nrow:
            break
    return pivot_row


def rref_kernel(matrix, ncols):
    a = [row[:] for row in matrix]
    nrow, pivot_row, pivots = len(a), 0, []
    for c in range(ncols):
        p = next((r for r in range(pivot_row, nrow) if a[r][c] != ZERO), None)
        if p is None:
            continue
        a[pivot_row], a[p] = a[p], a[pivot_row]
        iv = inv(a[pivot_row][c])
        a[pivot_row] = [mul(x, iv) for x in a[pivot_row]]
        for r in range(nrow):
            if r != pivot_row and a[r][c] != ZERO:
                f = a[r][c]
                a[r] = [sub(x, mul(f, y)) for x, y in zip(a[r], a[pivot_row])]
        pivots.append(c)
        pivot_row += 1
        if pivot_row == nrow:
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [ZERO] * ncols
        v[f] = ONE
        for r, c in enumerate(pivots):
            v[c] = neg(a[r][f])
        basis.append(v)
    return len(pivots), basis


def orbit(name):
    z = {1: ONE}
    if name == "principal":
        A, B = {0: ONE, 1: ONE}, {0: q(-2), 1: q(-8)}
        S0, T0 = q(4, 3), q(1, 6)
        gamma = {0: q(96), 1: q(192)}
    else:
        # One root r=(-1+2*sqrt(-2))/6; the other is its conjugate.
        r = (F(-1, 6), F(1, 3))
        assert add(add(mul(q(12), mul(r, r)), mul(q(4), r)), q(3)) == ZERO
        A, B = {1: r}, {0: ONE}
        S0, T0, gamma = ZERO, ONE, {}
    x2 = ({3: ONE}, B, scale(gamma, S0))
    x3 = ({4: ONE}, padd(A, scale(pmul(z, B), q(3, 2))),
          padd(scale(gamma, neg(T0)),
               scale(pmul(z, scale(gamma, S0)), q(3, 2))))
    return A, B, S0, T0, gamma, z, x2, x3


def source_matrix(degree, data):
    _, _, _, _, _, z, x2, x3 = data
    columns = []
    for i, j, k, l in monomials(degree):
        col = ymul(ypow((z, {}, {}), j), ymul(ypow(x2, k), ypow(x3, l)))
        columns.append(col)
    keys = sorted({(n, e) for col in columns for n in range(3) for e in col[n]})
    matrix = [[col[n].get(e, ZERO) for col in columns] for n, e in keys]
    return columns, keys, matrix


def contact_map(degree, data, kernel):
    A, B, S0, T0, gamma, z, _, _ = data
    xm = scale({0: S0}, q(-1))
    xy = B
    x2 = {(0, 0): {3: ONE}, (1, 0): xm, (0, 1): xy}
    xm3 = padd({0: T0}, scale(pmul(z, {0: S0}), q(-3, 2)))
    xy3 = padd(A, scale(pmul(z, B), q(3, 2)))
    x3 = {(0, 0): {4: ONE}, (1, 0): xm3, (0, 1): xy3}

    def bmul(a, b):
        out = {}
        for (m, y), p in a.items():
            for (mm, yy), qpoly in b.items():
                if m + mm + y + yy <= 3:
                    key = (m + mm, y + yy)
                    out[key] = padd(out.get(key, {}), pmul(p, qpoly))
        return out

    def bpow(a, n):
        out = {(0, 0): {0: ONE}}
        for _ in range(n):
            out = bmul(out, a)
        return out

    hcols, ecols, kcols = [], [], []
    for i, j, k, l in monomials(degree):
        value = bmul(bmul(bpow({(0, 0): {0: ONE}}, i), bpow({(0, 0): z}, j)),
                    bmul(bpow(x2, k), bpow(x3, l)))
        hcols.append(value.get((1, 0), {}))
        ecols.append(value.get((1, 1), {}))
        kcols.append(value.get((0, 3), {}))

    h_out, theta_out = [], []
    for v in kernel:
        h = e = k = {}
        for c, col in zip(v, hcols):
            h = padd(h, scale(col, c))
        for c, col in zip(v, ecols):
            e = padd(e, scale(col, c))
        for c, col in zip(v, kcols):
            k = padd(k, scale(col, c))
        theta = padd(pmul(gamma, e), scale(k, q(-1)))
        h_out.append(h)
        theta_out.append(theta)
    h_degrees = sorted({i for p in h_out for i in p})
    t_degrees = sorted({i for p in theta_out for i in p})
    joint_degrees = sorted({("h", i) for p in h_out for i in p}
                           | {("theta", i) for p in theta_out for i in p})

    def vectors(polys, degrees):
        return [[p.get(i, ZERO) for i in degrees] for p in polys]

    h_rank = rank_columns(vectors(h_out, h_degrees))
    theta_rank = rank_columns(vectors(theta_out, t_degrees))
    joint = [[h_out[j].get(i, ZERO) if tag == "h" else theta_out[j].get(i, ZERO)
              for tag, i in joint_degrees] for j in range(len(kernel))]
    return (h_rank, theta_rank, rank_columns(joint),
            (min(h_degrees), max(h_degrees)),
            (min(t_degrees), max(t_degrees)))


def quadric_multiple_span(quartic_kernel, sextic_matrix):
    """Check the actual quartic-times-quadric subspace in sextic columns."""
    quartics, sextics = monomials(4), monomials(6)
    indexes = {mon: i for i, mon in enumerate(sextics)}
    products = []
    for vector in quartic_kernel:
        for quadric in monomials(2):
            product = [ZERO] * len(sextics)
            for coefficient, mon in zip(vector, quartics):
                dest = tuple(x + y for x, y in zip(mon, quadric))
                product[indexes[dest]] = coefficient
            products.append(product)
    for product in products:
        for row in sextic_matrix:
            total = ZERO
            for x, y in zip(row, product):
                total = add(total, mul(x, y))
            assert total == ZERO
    rank = rank_columns(products)
    assert rank == 20
    return rank


def report(name):
    data = orbit(name)
    quartic_kernel = None
    for degree in (4, 5, 6):
        columns, keys, matrix = source_matrix(degree, data)
        rank, kernel = rref_kernel(matrix, len(columns))
        print(f"{name} d={degree}: rows={len(keys)}, rank={rank}, dim={len(kernel)}")
        if degree == 4:
            quartic_kernel = kernel
        if degree == 6:
            product_rank = quadric_multiple_span(quartic_kernel, matrix)
            print(f"  quartic-times-quadric span={product_rank}; "
                  f"additional sextic directions={len(kernel)-product_rank}")
            h_rank, theta_rank, joint_rank, hrange, trange = contact_map(degree, data, kernel)
            print(f"  h: deg={hrange}, rank={h_rank}; Theta: deg={trange}, rank={theta_rank}; "
                  f"joint rank={joint_rank}, joint kernel={len(kernel)-joint_rank}")


if __name__ == "__main__":
    report("principal")
    report("algebraic")
