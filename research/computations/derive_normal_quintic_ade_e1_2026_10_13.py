#!/usr/bin/env python3
"""New exact necessary ADE census for normal quintic carriers, direction e=1.

This is a numerical superset, not geometric realization or an STCI proof.
Inputs accepted from the prior record: Jaffe's smooth ADE pair table.
New inputs proved in the companion note: q=46/5, rank<=44, order=12.
"""
from fractions import Fraction as Q
from math import gcd, lcm
import json
import sys

TARGET = Q(46, 5)
MAXRANK = 44
direction = int(sys.argv[1]) if len(sys.argv) > 1 else 1
assert direction in (0, 1)
MAXORDER = 13 - direction
types = []
for n in range(1, MAXRANK + 1):
    for k in range(1, min((n + 1) // 2, MAXORDER) + 1):
        types.append((n, k, Q(k * (n + 1 - k), n + 1),
                      (n + 1) // gcd(n + 1, k), f'A{n}^{k}'))
for n in range(4, MAXRANK + 1):
    types.append((n, 2, Q(1), 2, f'D{n}^vector'))
    if n // 2 <= MAXORDER:
        types.append((n, n // 2, Q(n, 4), 2 if n % 2 == 0 else 4,
                      f'D{n}^spin'))
types += [(6, 2, Q(4, 3), 3, 'E6'), (7, 3, Q(3, 2), 2, 'E7')]
types.sort(key=lambda x: (x[1], x[0], x[4]))
rows = []
visited = 0

def search(start, N, P, q, idx, names):
    global visited
    visited += 1
    if q == TARGET:
        rows.append({'rank': N, 'order': P, 'q': str(q), 'local_index': idx,
                     'minimum_mate_divisibility': 4 * idx // gcd(idx, 5),
                     'pairs': names})
        return
    if q > TARGET or N >= MAXRANK or P >= MAXORDER:
        return
    nr, pr = MAXRANK - N, MAXORDER - P
    # Every smooth ADE pair satisfies q<=n*s/(n+s).
    if q + Q(nr * pr, nr + pr) < TARGET:
        return
    for i in range(start, len(types)):
        n, s, x, index, name = types[i]
        if N + n > MAXRANK or P + s > MAXORDER or q + x > TARGET:
            continue
        search(i, N+n, P+s, q+x, lcm(idx,index), names+[name])

search(0, 0, 0, Q(0), 1, [])
assert all(row['order'] >= 12 and row['rank'] >= 32 for row in rows)
if direction == 1:
    assert all(row['order'] == 12 and row['rank'] >= 40 for row in rows)
print(json.dumps({'scope': 'normal quintic, ADE everywhere, hypothetical arbitrary mate',
                  'direction_degree': direction,
                  'status': 'necessary exact arithmetic census only',
                  'visited_states': visited, 'types': len(types),
                  'rows': rows}, indent=2))
