#!/usr/bin/env python3
"""Exact supporting checks for the whole nongorenstein ACM cubic note.

The geometric proof is in the companion Markdown. This script checks the
literal Hilbert--Burch ideals, early Hilbert functions, generic Artin rings,
finite integer rank constraints, and the explicit cusp projection algebra.
It does not infer an entire conductor from a reduced Jacobian support.
"""
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

x, y, z, w = sp.symbols("x y z w")
data = {}
matrices = {
    "double_line_plus_line": sp.Matrix([[y, 0], [z, y], [0, x]]),
    "curvilinear_triple_line": sp.Matrix([[x, 0], [y, x], [z, y]]),
    "fat_triple_line": sp.Matrix([[x, 0], [y, x], [0, y]]),
}
expected = {
    "double_line_plus_line": [y**2, x*y, x*z],
    "curvilinear_triple_line": [x**2, x*y, y**2-x*z],
    "fat_triple_line": [x**2, x*y, y**2],
}

def compositions(n, count):
    if count == 1:
        yield (n,)
    else:
        for first in range(n+1):
            for rest in compositions(n-first, count-1):
                yield (first,)+rest

for name, matrix in matrices.items():
    minors = [sp.expand(matrix.extract(pair, [0, 1]).det())
              for pair in itertools.combinations(range(3), 2)]
    gb = sp.groebner(minors, x, y, z, w)
    expected_gb = sp.groebner(expected[name], x, y, z, w)
    assert list(gb) == list(expected_gb)
    leading = [tuple(poly.LM(order=gb.order).exponents) for poly in gb.polys]
    hilbert = []
    for degree in range(10):
        count = sum(not any(all(a >= b for a, b in zip(monomial, lm))
                            for lm in leading)
                    for monomial in compositions(degree, 4))
        assert count == 3*degree+1
        hilbert.append(count)
    entry_coefficients = sp.Matrix([
        [sp.expand(entry).coeff(variable) for variable in (x,y,z,w)]
        for entry in matrix
    ])
    expected_rank = 2 if name == "fat_triple_line" else 3
    assert entry_coefficients.rank() == expected_rank
    data[name] = {"minors": list(map(str, minors)),
                  "hilbert_function_0_to_9": hilbert,
                  "entry_span_dimension": expected_rank}

curvi_generic = sp.groebner([x**2,x*y,y**2-x], x,y)
assert list(curvi_generic) == [x-y**2,y**3]
double_generic = sp.groebner([y**2,x*y,x], x,y)
assert list(double_generic) == [x,y**2]
fat_generic = sp.groebner([x**2,x*y,y**2], x,y)
assert list(fat_generic) == [x**2,x*y,y**2]

# In basis 1*,x*,y* of omega_A, N omega_A is precisely <1*>.
act_x = sp.Matrix([[0,1,0],[0,0,0],[0,0,0]])
act_y = sp.Matrix([[0,0,1],[0,0,0],[0,0,0]])
assert (act_x*act_x).is_zero_matrix
assert (act_x*act_y).is_zero_matrix
assert (act_y*act_y).is_zero_matrix
assert act_x.row_join(act_y).rank() == 1
data["fat_canonical_nil_image_rank"] = 1

# Every weighted factor type has a*r <= 6. Exhaust all multisets summing
# to total K-length six, retaining zero-image possibilities k=a.
factor_types = [(a,r,k) for a in range(1,7) for r in range(1,7)
                for k in range(1,a+1) if a*r <= 6]

def weighted_multisets(start=0, remaining=6, prefix=()):
    if remaining == 0:
        yield prefix
        return
    for i in range(start,len(factor_types)):
        a,r,k = factor_types[i]
        if a*r <= remaining:
            yield from weighted_multisets(i,remaining-a*r,prefix+((a,r,k),))

curvi_cases = fat_cases = 0
for factors in weighted_multisets():
    if (all(a <= 3*k for a,r,k in factors)
            and sum((a-k)*r for a,r,k in factors) == 4):
        assert all(a == 3*k for a,r,k in factors)
        curvi_cases += 1
    if (all(a <= 2*k for a,r,k in factors)
            and sum((a-k)*r for a,r,k in factors) == 3):
        assert all(a == 2*k for a,r,k in factors)
        fat_cases += 1
assert curvi_cases and fat_cases
data["exact_integer_factor_constraints"] = {
    "curvilinear_cases": curvi_cases, "fat_cases": fat_cases,
    "all_curvi_multiplicities_divisible_by_three": True,
    "all_fat_multiplicities_even": True,
}

# Explicit F2 projection family, with r nonzero.
t,u,r,s = sp.symbols("t u r s", nonzero=True)
image = sp.Matrix([t+u*(r+s*t), u*t**2, u*t**3])
jacobian = image.jacobian([t,u])
on_fiber = jacobian.subs(t,0)
assert all(sp.expand(on_fiber.extract(pair,[0,1]).det()) == 0
           for pair in itertools.combinations(range(3),2))
assert on_fiber[0,1] == r
quartic = x*y*z**2-w*z**3-r*y**4-s*y**3*z
# Variables here: w=x0, x=x1, y=x2, z=x3.
assert sp.expand(quartic.subs({w:1,x:image[0],y:image[1],z:image[2]},
                            simultaneous=True)) == 0

rho,beta,P,Q,R,S = sp.symbols("rho beta P Q R S")
u_at_rho = (rho-t)/(r+s*t)
h = beta*t+u_at_rho*(P+Q*t+R*t**2+S*t**3)
linear = sp.factor(sp.diff(h,t).subs(t,0))
expected_linear = beta-P/r+rho*(Q/r-P*s/r**2)
assert sp.cancel(linear-expected_linear) == 0
assert sp.cancel(h.subs({P:beta*r,Q:beta*s})
                 -(beta*rho+u_at_rho*(R*t**2+S*t**3))) == 0
data["explicit_projection"] = {
    "quartic_substitution_zero": True,
    "jacobian_rank_on_fiber": 1,
    "linear_power_obstruction_coefficient": str(linear),
    "linear_system_forces_ambient_hyperplane": True,
}

output = Path(__file__).resolve().parents[1]/"scratch"/"session-scroll-nongorenstein-cubic-checks-2026-10-08.json"
payload = {"status":"PASS", "scope":"supporting exact algebra; geometric proof separately audited",
           "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "checks":data}
output.write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps({"status":"PASS","output":str(output),
                  "source_sha256":payload["source_sha256"],
                  "curvilinear_integer_cases":curvi_cases,
                  "fat_integer_cases":fat_cases},indent=2))
