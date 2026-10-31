#!/usr/bin/env python3
"""Exact second-obstruction certificate on the three smooth diagonal families.

See supplements/STCI_COMPLEXITY_AND_QUADRATIC_ROOTS.md. Reuse the accepted
embedded-chart construction through R4 without running its export or its
25-pairing/discriminant construction. All new arithmetic is in Q[t,t^-1].
No sampling, equation search, or Groebner basis is used. Standard library only.
"""

import ast
from fractions import Fraction as Q
from pathlib import Path


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
    return {e: c for e, c in result.items() if c}


def multiply(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, Q(0)) + a * b
    return {e: c for e, c in result.items() if c}


def monomial(coefficient, exponent=0):
    return {exponent: Q(coefficient)} if coefficient else {}


def specialize(polynomial, values):
    result = {}
    for indices, coefficient in polynomial.items():
        term = monomial(coefficient)
        for index in indices:
            term = multiply(term, values[index])
        result = add(result, term)
    return result


def in_z_product(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = add(result.get(i + j, {}), multiply(a, b))
    return {e: c for e, c in result.items() if c}


def accepted_model():
    source = Path(__file__).with_name("generalization_quadratic_root_global_second_model.py")
    tree = ast.parse(source.read_text())
    # ABC begins the unrelated 25-pairing construction, immediately after R4.
    stop = next(i for i, node in enumerate(tree.body)
                if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "ABC"
                        for target in node.targets))
    namespace = {"__file__": str(source)}
    exec(compile(ast.Module(body=tree.body[:stop], type_ignores=[]), str(source), "exec"), namespace)
    return namespace["FIRST"], namespace["R4"]


def families():
    m = monomial
    zero = m(0)
    # Coefficient order is a0,a1,a2,b0,b1,b2,c0,c1,c2. In every
    # family t != 0; c2=1 uses only the projective scale of the root.
    yield "plus", [m(4), zero, m(1, 1), zero, zero, zero, m(-8, -1), zero, m(1)], [
        m(-8, -1), zero, m(-3), zero, zero, zero,
        zero, zero, zero, m(Q(-9, 2)), zero, m(Q(-1, 8), 1)], -16
    yield "minus", [m(-4), zero, m(1, 1), zero, zero, zero, m(32, -1), zero, m(1)], [
        m(Q(32, 3), -1), zero, m(Q(-7, 3)), zero, m(Q(1, 6), 1), zero,
        zero, m(Q(32, 3), -1), zero, m(Q(-29, 6)), zero, m(Q(1, 24), 1)], -640
    yield "mixed", [m(-4), m(1, 1), m(Q(-5, 44), 2), zero, zero, zero,
                    m(880, -2), m(44, -1), m(1)], [
        m(Q(176, 27), -2), m(Q(286, 27), -1), m(Q(-137, 54)),
        m(Q(7, 108), 1), m(Q(29, 9504), 2), m(Q(-41, 38016), 3),
        m(Q(-79376, 27), -3), m(Q(-1276, 27), -2), m(Q(154, 27), -1),
        m(Q(-511, 108)), m(Q(13, 432), 1), m(Q(-1, 9504), 2)], 1648


def main():
    first, fourth = accepted_model()
    for name, root, correction, expected in families():
        values = root + correction
        assert all(not specialize(equation, values) for equation in first), name
        a = {j: root[j] for j in range(3) if root[j]}
        c = {j: root[6 + j] for j in range(3) if root[6 + j]}
        c_squared = in_z_product(c, c)
        # q=(0,-c^3,0,a*c^2,0) lies in ker T_f, with base degree <=6.
        q1 = {j: multiply(monomial(-1), p)
              for j, p in in_z_product(c_squared, c).items()}
        q3 = in_z_product(a, c_squared)
        assert not add_z(in_z_product(a, q1), in_z_product(c, q3))
        residue = {}
        for direction, dual in ((1, q1), (3, q3)):
            for z_degree, coefficient in dual.items():
                component = fourth.get((4 - direction, direction, -1 - z_degree), {})
                residue = add(residue, multiply(coefficient, specialize(component, values)))
        assert residue == monomial(expected), (name, residue)
        print(f"{name}: all 16 first equations vanish identically; second residue = {expected}")
    print("PASS: every smooth first-compatible root with b=0 fails the second lift.")
    print("Scope: fixed ambient coordinates, characteristic zero, classified diagonal locus only.")


def add_z(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = add(result.get(exponent, {}), coefficient)
    return {e: c for e, c in result.items() if c}


if __name__ == "__main__":
    main()
