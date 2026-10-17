#!/usr/bin/env python3
"""Independent exact affine-rank audit of the three repeated partitions.

Constructs all direction kernels from the literal quadrics and solves the
unreduced five-variable Q1 systems at every determinant root.  The conductor
certificate uses x1=0, a different conic section from the owner's checker.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time

import sympy as s


START = time.perf_counter()
SOURCE = Path(__file__).resolve()
ROOT = SOURCE.parents[3]
CHECKS = []
STRATA = []


def simp(value):
    return s.simplify(s.expand(value))


def equal(label, left, right=0):
    if isinstance(left, s.MatrixBase):
        difference = left-right
        assert all(simp(e) == 0 for e in difference), (label, difference)
    else:
        assert simp(left-right) == 0, (label, left, right)
    CHECKS.append(label)


def true(label, condition):
    assert condition, label
    CHECKS.append(label)


def rank(matrix):
    return matrix.rank(iszerofunc=lambda e: simp(e) == 0)


Y = s.symbols("Y0:5")
U, V, t, k = s.symbols("U V t k")
literal = [
    Y[0]*Y[2]-Y[1]**2,
    Y[0]*Y[3]-Y[1]*Y[2],
    Y[0]*Y[4]-Y[1]*Y[3],
    Y[1]*Y[3]-Y[2]**2,
    Y[1]*Y[4]-Y[2]*Y[3],
    Y[2]*Y[4]-Y[3]**2,
]
rnc = {Y[i]: U**(4-i)*V**i for i in range(5)}


def quadric(coefficients):
    return s.expand(sum(a*b for a, b in zip(coefficients, literal)))


def kernel_matrix(coefficients):
    a, b, c, d, e, f = coefficients
    return s.Matrix([[a, b, c], [b, c+d, e], [c, e, f]])


def contact(coefficients):
    return s.expand(s.diff(quadric(coefficients), Y[2]).subs(rnc))


for index, equation in enumerate(literal):
    equal(f"E{index} is an actual RNC quadric", equation.subs(rnc))
reverse = {Y[i]: Y[4-i] for i in range(5)}
for index, image in enumerate([5, 4, 2, 3, 1, 0]):
    equal(f"center-preserving reversal E{index}",
          literal[index].subs(reverse, simultaneous=True), literal[image])

# Exhaustive orbit equations are recomputed from factor products.
a, b, c, d = s.symbols("a b c d")
equal("[4] middle coefficient", s.Poly((a*U+b*V)**4, U, V).coeff_monomial(U**2*V**2), 6*a**2*b**2)
equal("[3,1] middle coefficient", s.Poly((a*U+b*V)**3*(c*U+d*V), U, V).coeff_monomial(U**2*V**2), 3*a*b*(a*d+b*c))
equal("[2,2] middle coefficient", s.Poly((a*U**2+b*U*V+c*V**2)**2, U, V).coeff_monomial(U**2*V**2), b**2+2*a*c)
equal("[3,1] allowed diagonal orbit normalization",
      ((a*U+b*V)**3*(c*U+d*V)).subs({U: -b*U/a, d: -b*c/a}),
      b**4*c/a*(U-V)**3*(U+V))
equal("[2,2] allowed diagonal orbit normalization",
      (a*U**2+b*U*V+c*V**2).subs({U: b*U/a, c: -b**2/(2*a)}),
      b**2/a*(U**2+U*V-V**2/2))

unknowns = s.symbols("u0 u1 u2 u4 u5")
first = s.Matrix([unknowns[0], unknowns[1], unknowns[2], 1, unknowns[3], unknowns[4]])

# [4], keeping its entire eta boundary and endpoint singleton condition.
four_second = s.Matrix([1, 0, k, 0, 0, 0])
equal("[4] E2 determinant", kernel_matrix(four_second).det(), -k**3)
lam = s.symbols("lam")
four_eta = s.Matrix([0, 1, lam])
four_equations = list(kernel_matrix(first)*four_eta)+[contact(first).subs({U: 0, V: 1})]
four_matrix, four_rhs = s.linear_eq_to_matrix(four_equations, unknowns)
true("[4] complete affine rank is four for every lambda", rank(four_matrix) == 4)
four_base = s.Matrix([0, lam, -1, 1, 0, 0])
equal("[4] entire family is base plus Q2", four_matrix*s.Matrix([four_base[i] for i in [0, 1, 2, 4, 5]]), four_rhs)
equal("[4] Q2 supplies the unique free direction", four_matrix*s.Matrix([1, 0, 0, 0, 0]), s.zeros(4, 1))
four_line = {Y[0]: 0, Y[1]: 0, Y[2]: 0}
equal("[4] both quadrics contain an actual line", s.Matrix([quadric(four_base).subs(four_line), literal[0].subs(four_line)]), s.zeros(2, 1))
equal("[4] gradient of E0 vanishes on that line", s.Matrix([s.diff(literal[0], yi).subs(four_line) for yi in Y]), s.zeros(5, 1))

# [3,1] endpoint triple: its kernel is on the intrinsic direction conic.
endpoint = s.Matrix([a, -b, k, 0, 0, 0])
equal("[3,1] endpoint determinant", kernel_matrix(endpoint).det(), -k**3)
equal("[3,1] endpoint rank-two minor", kernel_matrix(endpoint).subs(k, 0)[:2, :2].det(), -b**2)
equal("[3,1] endpoint kernel is on direction conic", kernel_matrix(endpoint).subs(k, 0)*s.Matrix([0, 0, 1]), s.zeros(3, 1))


def check_all_roots(name, second, determinant, roots, support_polynomial, base, survivor):
    """Unreduced affine systems, with kernels computed afresh at each root."""
    equal(f"{name} determinant with invisible E2 retained", kernel_matrix(second).det(), determinant)
    remainder = s.Poly(s.rem(contact(first).subs({U: 1, V: t}), support_polynomial, t), t)
    for root in roots:
        second_at_root = second.subs(k, root)
        matrix_at_root = kernel_matrix(second_at_root).applyfunc(simp)
        true(f"{name} rank two at root {root}", rank(matrix_at_root) == 2)
        nullspace = matrix_at_root.nullspace(iszerofunc=lambda e: simp(e) == 0)
        true(f"{name} unique entire direction at {root}", len(nullspace) == 1)
        eta = nullspace[0].applyfunc(simp)
        true(f"{name} actual direction off conic at {root}", simp(eta[1]**2-eta[0]*eta[2]) != 0)
        equations = list(kernel_matrix(first)*eta)+[remainder.coeff_monomial(t), remainder.coeff_monomial(1)]
        matrix, rhs = s.linear_eq_to_matrix(equations, unknowns)
        matrix, rhs = matrix.applyfunc(simp), rhs.applyfunc(simp)
        r, augmented = rank(matrix), rank(matrix.row_join(rhs))
        if root == survivor:
            true(f"{name} complete survivor affine rank four", r == augmented == 4)
            base_vector = s.Matrix([base[i] for i in [0, 1, 2, 4, 5]])
            free_vector = s.Matrix([second_at_root[i] for i in [0, 1, 2, 4, 5]])
            equal(f"{name} base solves every original equation", matrix*base_vector, rhs)
            equal(f"{name} Q2 is entire unique affine direction", matrix*free_vector, s.zeros(5, 1))
            classification = "one affine family, one pencil modulo Q2"
        else:
            true(f"{name} hidden branch inconsistent at {root}", augmented > r)
            classification = "inconsistent"
        STRATA.append({"partition": name, "E2_root": str(root), "rank_Q2": rank(matrix_at_root), "rank_Q1": r, "rank_augmented": augmented, "classification": classification})


second31 = s.Matrix([1, 2, k, 0, -2, -1])
base31 = s.Matrix([1, 0, -1, 1, 0, 1])
equal("[3,1] actual normalized contact", contact(second31), (U-V)**3*(U+V))
check_all_roots("[3,1]", second31, -k*(k**2+9), [0, 3*s.I, -3*s.I], 1-t**2, base31, 0)
line31 = {Y[0]: a, Y[1]: b, Y[2]: a, Y[3]: b, Y[4]: a}
equal("[3,1] actual common singular line", s.Matrix([quadric(base31).subs(line31), quadric(second31.subs(k, 0)).subs(line31)]), s.zeros(2, 1))
equal("[3,1] base quadric gradient vanishes on line", s.Matrix([s.diff(quadric(base31), yi).subs(line31) for yi in Y]), s.zeros(5, 1))

second22 = s.Matrix([1, -2, k, 0, 1, s.Rational(1, 4)])
base22 = s.Matrix([0, 2, 0, 1, -1, 0])
q22 = U**2+U*V-V**2/2
equal("[2,2] actual normalized contact", contact(second22), q22**2)
roots22 = [-s.Rational(1, 2), (1+3*s.sqrt(7)*s.I)/4, (1-3*s.sqrt(7)*s.I)/4]
check_all_roots("[2,2]", second22, -(2*k+1)*(2*k**2-k+8)/4, roots22, 1+t-t**2/2, base22, -s.Rational(1, 2))

# Actual conductor and a different two-point certificate: x1=0 rather than x2=0.
x0, x1, x2, x3, z = s.symbols("x0 x1 x2 x3 z")
rename = dict(zip(Y, [x0, x1, z, x2, x3]))
q1 = quadric(base22).subs(rename)
q2 = quadric(second22.subs(k, -s.Rational(1, 2))).subs(rename)
linear = s.diff(q2, z)
constant = q2.subs(z, 0)
A = s.diff(q1, z).subs(z, 0)
R1 = q1.subs(z, 0)
ell = s.diff((literal[3].subs(rename)-q1), z)
q = (literal[3].subs(rename)-q1).subs(z, 0)
equal("[2,2] actual monic equation", q1, -z**2+A*z+R1)
equal("[2,2] actual linear projection equation", q2, linear*z+constant)
equal("[2,2] third ribbon quadric on surface", literal[3].subs(rename)-q1, ell*z+q)
solve_plane = {x0: s.solve(linear, x0)[0]}
conic = s.expand(constant.subs(solve_plane))
equal("[2,2] actual conductor conic nondegenerate", s.det(s.hessian(conic, (x1, x2, x3))/2), s.Rational(243, 128))
trace = s.expand((2*q+A*ell).subs(solve_plane))
norm = s.expand((q**2+A*q*ell-R1*ell**2).subs(solve_plane))
disc = s.expand((A**2+4*R1).subs(solve_plane))
equal("[2,2] norm-trace-discriminant identity", trace**2-4*norm, disc*ell.subs(solve_plane)**2)
other_slice = {x1: 0, x2: t, x3: 1}
p = 18*t**2-1
equal("[2,2] independent conductor section", conic.subs(other_slice), -p/8)
slice_trace = s.rem(trace.subs(other_slice), p, t)
slice_norm = s.rem(norm.subs(other_slice), p, t)
true("[2,2] norm nonzero at both independent points", s.gcd(slice_norm, p) == 1)
ratio = s.rem(slice_trace**2*s.invert(slice_norm, p, t), p, t)
equal("[2,2] independent all-powers obstruction", ratio, 22+72*t)
true("[2,2] independent points are distinct", s.discriminant(p, t) != 0)
true("[2,2] generic conductor cover is separable", s.gcd(s.rem(disc.subs(other_slice), p, t), p) == 1)

dependencies = [
    ROOT/"research/notes/2026-10-09-session-ribbon-repeated-partitions-complete.md",
    ROOT/"research/computations/verify_session_ribbon_repeated_partitions_2026_10_09.py",
]
result = {
    "status": "PASS",
    "scope": "Independent exact affine-rank reconstruction of complete [4], [3,1], [2,2] partition coverage under the explicit net and fixed projection hypotheses.",
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "dependencies": [{"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in dependencies],
    "sympy_version": s.__version__,
    "checks": CHECKS,
    "checked_conditions": len(CHECKS),
    "all_affine_root_systems": STRATA,
    "independent_conductor_slice": {"equation": str(p), "trace_square_over_norm": str(ratio), "nonzero_linear_coefficient": 72},
    "elapsed_seconds": time.perf_counter()-START,
    "does_not_claim": "Upstream ribbon/D5 completeness, the [2,1,1] partition, all genus-one promotion by itself, higher carrier degrees, or the universal STCI problem.",
}
(SOURCE.parent/"result.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"status": result["status"], "checked_conditions": len(CHECKS), "elapsed_seconds": result["elapsed_seconds"], "source_sha256": result["source_sha256"], "result": str(SOURCE.parent/"result.json")}, indent=2))
