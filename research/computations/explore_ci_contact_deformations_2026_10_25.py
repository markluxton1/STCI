#!/usr/bin/env python3
"""Selected exact experiments for the fixed-C (4,4) deformation notebook.

Uses actual degree-four homogeneous monomial differences, not arbitrary
k(C)-valued normal sections. Standard library only. This checks coordinate
identities and differential ranks; it is not a global classification.
"""
from fractions import Fraction
from itertools import product


def rank(columns):
    rows = [[Fraction(x) for x in row] for row in zip(*columns)]
    pivot = 0
    for j in range(len(columns)):
        k = next((i for i in range(pivot, len(rows)) if rows[i][j]), None)
        if k is None:
            continue
        rows[pivot], rows[k] = rows[k], rows[pivot]
        scale = rows[pivot][j]
        rows[pivot] = [x / scale for x in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot and rows[i][j]:
                scale = rows[i][j]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


monomials = [m for m in product(range(5), repeat=4) if sum(m) == 4]
weight = lambda m: m[1] + 3 * m[2] + 4 * m[3]
groups = {w: [m for m in monomials if weight(m) == w] for w in range(17)}
# Every degree-16 binary monomial occurs. In each weight block, differences
# against its first monomial give an integral basis of the restriction kernel.
basis = [(m, block[0]) for block in groups.values() for m in block[1:]]
assert len(basis) == 18


def first_symbol(m, ref):
    """A(u)X+B(u)Y; x0=1,x1=u,x2=u^3+Y,x3=u^4+X."""
    a, b = [0] * 13, [0] * 13
    for sign, exponents in ((1, m), (-1, ref)):
        w = weight(exponents)
        if exponents[3]:
            a[w - 4] += sign * exponents[3]
        if exponents[2]:
            b[w - 3] += sign * exponents[2]
    return a, b


symbols = [first_symbol(m, ref) for m, ref in basis]


def linear_combination(coefficients):
    return tuple(
        [sum(c * symbols[i][j][n] for i, c in enumerate(coefficients)) for n in range(13)]
        for j in range(2)
    )


def coords(polynomial):
    # Coefficient of every non-reference monomial is its basis coordinate.
    return [polynomial.get(m, 0) for m, ref in basis]


f = linear_combination(coords({(0, 4, 0, 0): 1, (3, 0, 0, 1): -1}))
g = linear_combination(coords({(0, 0, 4, 0): 1, (1, 0, 0, 3): -1}))
assert f[0] == [-1] + [0] * 12 and not any(f[1])
assert g[0][8] == -3 and g[1][9] == 4
assert sum(abs(x) for x in g[0]) == 3 and sum(abs(x) for x in g[1]) == 4


def wedge(a, b):
    out = [0] * 25
    for i in range(13):
        for j in range(13):
            out[i + j] += a[0][i] * b[1][j] - a[1][i] * b[0][j]
    assert not any(out[19:])
    return out[:19]


base_det = wedge(f, g)
assert base_det == [0] * 9 + [-4] + [0] * 9
vary_f = [wedge(h, g) for h in symbols]
vary_g = [wedge(f, h) for h in symbols]
assert rank(vary_f) == 11
assert rank(vary_g) == 11
assert rank(vary_f + vary_g) == 19
# The two image spaces have supports 8..18 and 0..10, respectively.
assert all(not any(v[:8]) for v in vary_f)
assert all(not any(v[11:]) for v in vary_g)
print('Actual quartic source: dimension 18; pencil space Gr(2,18): dimension 32')
print('At <F,G>: differential of affine determinant map has exact rational rank 19')
print('Vary F image: span u^8..u^18; vary G image: span 1..u^10')
print('Projective contact-divisor differential: rank18, kernel dimension14')

# Q*x0^2 is a genuine homogeneous quartic. Its affine first symbol is X-uY.
h = linear_combination(coords({(3, 0, 0, 1): 1, (2, 1, 1, 0): -1}))
assert h[0] == [1] + [0] * 12
assert h[1] == [0, -1] + [0] * 11
pencil_derivative = wedge(f, h)
assert pencil_derivative == [0, 1] + [0] * 17
print('F, G+lambda*Q*x0^2: determinant = -4*u^9+lambda*u')
print('Boundary for lambda!=0: 9q+p+8 simple mobile points, u^8=lambda/4')
print('SELECTED CONTACT-DEFORMATION EXPERIMENTS PASS')
