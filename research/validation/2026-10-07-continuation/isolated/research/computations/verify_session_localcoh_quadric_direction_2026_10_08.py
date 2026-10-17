#!/usr/bin/env python3
"""Complete quartic first-symbol space in the unique smooth-quadric direction.

Fixed C0, characteristic zero. All 35 ambient monomials are reconstructed;
the full kernel of curve plus actual Q-path derivative conditions is q*S2.
The companion proof then applies P-037 to any canonical triple with this
first quotient, independently of its positive second defect.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

x0, x1, x2, x3, z, epsilon = s.symbols('x0 x1 x2 x3 z epsilon')
xs = (x0, x1, x2, x3)
monomials = [x0**a*x1**b*x2**c*x3**(4-a-b-c)
             for a in range(5) for b in range(5-a) for c in range(5-a-b)]
quadratics = [x0**a*x1**b*x2**c*x3**(2-a-b-c)
              for a in range(3) for b in range(3-a) for c in range(3-a-b)]
assert len(monomials) == 35 and len(quadratics) == 10
q = x0*x3-x1*x2
actual_q_path = {x0: 1, x1: z, x2: z**3+epsilon, x3: z**4+z*epsilon}
assert s.expand(q.subs(actual_q_path)) == 0
restrictions, first_derivatives = [], []
for monomial in monomials:
    expression = s.expand(monomial.subs(actual_q_path))
    restrictions.append(expression.coeff(epsilon, 0))
    first_derivatives.append(expression.coeff(epsilon, 1))
rows = []
for functions in (restrictions, first_derivatives):
    degree = max(s.degree(value, z) for value in functions if value)
    rows.extend([[s.expand(value).coeff(z, power) for value in functions]
                 for power in range(degree+1)])
matrix = s.Matrix(rows)
rank = matrix.rank()
assert rank == 25
factor_space = s.Matrix.hstack(*[
    s.Matrix([s.Poly(s.expand(q*quadratic), *xs).coeff_monomial(monomial)
              for monomial in monomials]) for quadratic in quadratics])
assert factor_space.rank() == 10
assert matrix*factor_space == s.zeros(matrix.rows, 10)
assert 35-rank == 10
HERE = Path(__file__).resolve().parent
record = {
    'scope': 'All quartic forms with C0 restriction zero and zero first normal along Q; no primitive-triple assumption',
    'status': 'PASS: complete first-symbol quartic kernel is q times all homogeneous quadratics',
    'ambient_columns': list(map(str, monomials)),
    'combined_matrix_shape': list(matrix.shape),
    'combined_rank': rank,
    'full_kernel_dimension': 10,
    'factor_basis': list(map(str, quadratics)),
    'q_path': {str(key): str(value) for key, value in actual_q_path.items()},
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof': 'Q restriction has class (4,4)-2(1,3)=(2,-2), so is zero; q*alpha gives forbidden degree2 ancestor',
    'retained': 'Other e1 positive-D2 directions, including other d2=4 Gorenstein possibilities'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
print('PASS: actual Q transverse path and all35 ambient quartic columns reconstructed.')
print('PASS: combined matrix rank25; entire kernel exactly q*H0(P3,O(2)), dimension10.')
print('PROVED under accepted ancestor/P-037 inputs: quadric quotient direction excluded for every D2.')
