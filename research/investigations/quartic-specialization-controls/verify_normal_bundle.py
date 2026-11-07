#!/usr/bin/env python3
"""Exact normal-bundle and characteristic-3 primitive-triple checks for C0."""

import sympy as sp

u, v = sp.symbols("u v", nonzero=True)
a, b = sp.symbols("a b")
alpha, beta = sp.symbols("alpha beta")
s, t = sp.symbols("s t")


def mod_expr(expr, p, variables):
    return sp.Poly(sp.expand(expr), *variables, modulus=p).as_expr()


def rank_mod(matrix, p):
    rows = [[int(value) % p for value in row] for row in matrix.tolist()]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column] % p),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, p)
        rows[rank] = [(entry * inverse) % p for entry in rows[rank]]
        for row in range(len(rows)):
            if row != rank and rows[row][column] % p:
                factor = rows[row][column] % p
                rows[row] = [
                    (rows[row][j] - factor * rows[rank][j]) % p
                    for j in range(len(rows[row]))
                ]
        rank += 1
    return rank


print("1. CONORMAL TRANSITION MATRIX")
y = u
z = u**3 + a
w = u**4 + b
alpha_expr = y / w - (z / w) ** 3
beta_expr = 1 / w - (z / w) ** 4
transition = sp.Matrix(
    [
        [
            sp.factor(sp.diff(alpha_expr, a).subs({a: 0, b: 0})),
            sp.factor(sp.diff(alpha_expr, b).subs({a: 0, b: 0})),
        ],
        [
            sp.factor(sp.diff(beta_expr, a).subs({a: 0, b: 0})),
            sp.factor(sp.diff(beta_expr, b).subs({a: 0, b: 0})),
        ],
    ]
)
expected = sp.Matrix(
    [[-3 * u**-6, 2 * u**-7], [-4 * u**-7, 3 * u**-8]]
)
assert sp.simplify(transition - expected) == sp.zeros(2)
assert sp.factor(transition.det()) == -u**-14

q_s = sp.Matrix([[-u, 1]])
q_t_in_s = sp.Matrix([[-u**-1, 1]]) * transition
assert sp.simplify(q_t_in_s - u**-8 * q_s) == sp.zeros(1, 2)
r_s = sp.Matrix([[1, 0]])
r_t_in_s = sp.Matrix([[-1, 0]]) * transition
assert sp.simplify(
    r_t_in_s - (u**-6 * r_s - 2 * u**-7 * q_s)
) == sp.zeros(1, 2)
print("  transition, determinant, and extension cocycle verified")


print("2. INDEPENDENT JACOBIAN-SYZYGY CERTIFICATE")
forms = [s**4, s**3 * t, s * t**3, t**4]
quadratics = [s**2, s * t, t**2]
coefficients = sp.symbols("c0:12")
syzygy_entries = [
    sum(coefficients[3 * i + j] * quadratics[j] for j in range(3))
    for i in range(4)
]
conditions = []
for variable in (s, t):
    expression = sp.expand(
        sum(
            syzygy_entries[i] * sp.diff(forms[i], variable)
            for i in range(4)
        )
    )
    polynomial = sp.Poly(expression, s, t)
    conditions.extend(
        polynomial.coeff_monomial(s**power * t ** (5 - power))
        for power in range(6)
    )
syzygy_matrix, _ = sp.linear_eq_to_matrix(conditions, coefficients)
assert syzygy_matrix.shape == (12, 12)
assert syzygy_matrix.rank() == 12
assert int(syzygy_matrix.det()) == 2**15
for characteristic in (3, 5):
    assert rank_mod(syzygy_matrix, characteristic) == 12
print("  determinant=2^15; full rank in characteristics 0, 3, and 5")


print("3. CHARACTERISTIC-3 PRIMITIVE TRIPLE")
f_s = y**3 - z
g_s = w**3 - z**4
f_s_3 = mod_expr(f_s, 3, (u, a, b))
g_s_3 = mod_expr(g_s, 3, (u, a, b))
assert f_s_3 == -a
assert mod_expr(g_s_3 - b**3, 3, (u, a, b)).subs(a, 0) == 0

capital_z = v
capital_y = v**3 + alpha
capital_x = v**4 + beta
f_t = capital_y**3 - capital_x**2 * capital_z
g_t = capital_x - capital_z**4
f_t_3 = mod_expr(f_t, 3, (v, alpha, beta))
g_t_3 = mod_expr(g_t, 3, (v, alpha, beta))
assert g_t_3 == beta
assert mod_expr(f_t_3 - alpha**3, 3, (v, alpha, beta)).subs(beta, 0) == 0

chi = 1 + (1 - 7) + (1 - 14)
arithmetic_genus = 1 - chi
assert chi == -18 and arithmetic_genus == 19
print("  local ideals (a,b^3) and (beta,alpha^3); arithmetic genus 19")

print("ALL ASSERTIONS PASSED")
