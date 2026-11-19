#!/usr/bin/env python3
"""Exact integer certificates for the full-column Chow-polytope H15 proof.

No third-party dependencies. Expand 8x8 Sylvester determinants directly;
variables are (a0,a1,a2,a3,b0,b1,b2,b3). The line is reduced, so its Chow
form is a bracket, NOT the quartic-parametrization resultant.
"""
from collections import defaultdict
from itertools import permutations
import json

ZERO = (0,) * 8
EXPONENTS = (0, 1, 3, 4)


def clean(p):
    return {u: c for u, c in p.items() if c}


def add(p, q):
    out = defaultdict(int, p)
    for u, c in q.items():
        out[u] += c
    return clean(out)


def neg(p):
    return {u: -c for u, c in p.items()}


def mul(p, q):
    out = defaultdict(int)
    for u, c in p.items():
        for v, d in q.items():
            out[tuple(x + y for x, y in zip(u, v))] += c * d
    return clean(out)


def power(p, n):
    out = {ZERO: 1}
    for _ in range(n):
        out = mul(out, p)
    return out


def variable(i):
    u = list(ZERO)
    u[i] = 1
    return {tuple(u): 1}


def bracket(i, j):
    return add(mul(variable(i), variable(4 + j)),
               neg(mul(variable(j), variable(4 + i))))


def sylvester(support):
    """Matrix entries are variable indices or None (the zero entry)."""
    rows = []
    for row_offset in (0, 4):
        coefficients = [None] * 5
        for i in support:
            coefficients[4 - EXPONENTS[i]] = row_offset + i
        for shift in range(4):
            rows.append([None] * shift + coefficients + [None] * (3 - shift))
    return rows


def determinant(matrix):
    """Leibniz expansion over Z, combining equal monomials exactly."""
    out = defaultdict(int)
    for perm in permutations(range(8)):
        selected = [matrix[i][perm[i]] for i in range(8)]
        if None in selected:
            continue
        inversions = sum(perm[i] > perm[j]
                         for i in range(8) for j in range(i + 1, 8))
        u = [0] * 8
        for i in selected:
            u[i] += 1
        out[tuple(u)] += (-1) ** inversions
    return clean(out)


def weight(u):
    return tuple(u[i] + u[i + 4] for i in range(4))


def equal_up_to_sign(p, q):
    assert p == q or p == neg(q), 'Polynomial identity failed'


def certify(support, degree, minimum, face, width, expected_initial):
    p = bracket(0, 3) if len(support) == 2 else determinant(sylvester(support))
    assert p, 'Zero Chow polynomial'
    assert all(sum(u[:4]) == degree and sum(u[4:]) == degree for u in p)
    weights = {weight(u) for u in p}
    assert all(sum(w) == 2 * degree for w in weights)
    if degree == 4:
        assert all(sum(e * v for e, v in zip(EXPONENTS, w)) == 16
                   for w in weights)
    assert min(w[1] + w[2] for w in weights) == 0
    assert min(w[0] for w in weights) == minimum
    face_weights = {w for w in weights if w[0] == minimum}
    assert face_weights == set(face), (support, face_weights)
    assert max(w[2] for w in face_weights) - min(w[2] for w in face_weights) == width
    initial = {u: c for u, c in p.items() if weight(u)[0] == minimum}
    equal_up_to_sign(initial, expected_initial)
    witnesses = []
    for w in sorted(face_weights):
        units = [(u, c) for u, c in initial.items() if weight(u) == w and abs(c) == 1]
        assert units, ('No characteristic-free unit witness', w)
        u, c = sorted(units)[0]
        witnesses.append({'weight': w, 'monomial': u, 'coefficient': c})
    endpoint_specialization = {u: c for u, c in p.items() if weight(u)[1] + weight(u)[2] == 0}
    equal_up_to_sign(endpoint_specialization, power(bracket(0, 3), degree))
    if support == (0, 2, 3):
        equal_up_to_sign(p, add(power(bracket(0, 3), 4),
                               neg(mul(power(bracket(0, 2), 3), bracket(2, 3)))))
    return {'support': support, 'degree': degree, 'terms': len(p),
            'minimum_w0': minimum, 'face_weights': sorted(face_weights),
            'width_w2': width, 'unit_witnesses': witnesses}


def main():
    d01, d02, d03 = bracket(0, 1), bracket(0, 2), bracket(0, 3)
    d12, d13, d23 = bracket(1, 2), bracket(1, 3), bracket(2, 3)
    cases = [
        ((0, 3), 1, 1, [(1, 0, 0, 1)], 0, d03),
        ((0, 1, 3), 4, 1, [(1, 4, 0, 3)], 0, mul(d01, power(d13, 3))),
        ((0, 2, 3), 4, 3, [(3, 0, 4, 1)], 0, mul(power(d02, 3), d23)),
        ((0, 1, 2, 3), 4, 1, [(1, 4, 0, 3), (1, 3, 3, 1)], 3,
         mul(d01, add(power(d13, 3), mul(power(d12, 2), d23)))),
    ]
    results = [certify(*case) for case in cases]
    assert [r['terms'] for r in results] == [2, 13, 13, 64]
    print(json.dumps({'status': 'PASS', 'coefficient_ring': 'Z',
                      'variables': ['a0', 'a1', 'a2', 'a3', 'b0', 'b1', 'b2', 'b3'],
                      'cases': results}, indent=2))


if __name__ == '__main__':
    main()
