#!/usr/bin/env python3
"""Export the exact necessary conormal cup-product ranks for quartic ancestors.

No actual ambient extension class is substituted. The output is a
continuation-ready structural reduction, not an incidence exclusion.
"""
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
z = s.symbols('z')
rows = []


def connecting(domain_degree, target_line_degree, extension_line_degree):
    assert target_line_degree <= -2
    assert extension_line_degree == target_line_degree-domain_degree
    row_count = -target_line_degree-1
    coefficients = s.symbols('c1:'+str(-extension_line_degree))
    laurent = sum(value*z**(-j-1) for j, value in enumerate(coefficients))
    matrix = s.Matrix(row_count, domain_degree+1,
                      lambda i, j: s.expand(z**j*laurent).coeff(z, -i-1))
    assert all(matrix[i, j] == coefficients[i+j]
               for i in range(row_count) for j in range(domain_degree+1))
    return matrix, coefficients


for d2 in range(1, 5):
    n = 5-d2
    matrix, coefficients = connecting(n-1, -n-1, -2*n)
    assert matrix.shape == (n, n) and matrix == matrix.T
    rows.append({'e': 1, 'd2': d2, 'd3': 4,
                 'extension_line_degree': -2*n,
                 'extension_dimension': 2*n-1,
                 'connecting_matrix': [[str(value) for value in row] for row in matrix.tolist()],
                 'required_rank': n-1,
                 'determinant_equation': str(s.expand(matrix.det())),
                 'rank_open_condition': 'some minor of size '+str(n-1)+' is nonzero' if n>1 else 'all entries zero',
                 'required_split': 'V(4)=O(2)+O(4)'})
assert rows[2]['determinant_equation'] == 'c1*c3 - c2**2'
assert rows[3]['determinant_equation'] == 'c1'
for d2 in range(2):
    domain_degree, target_degree = 1-d2, -5+d2
    matrix, coefficients = connecting(domain_degree, target_degree, -6+2*d2)
    rows.append({'e': 2, 'd2': d2, 'd3': 1,
                 'extension_line_degree': -6+2*d2,
                 'extension_dimension': len(coefficients),
                 'connecting_matrix': [[str(value) for value in row] for row in matrix.tolist()],
                 'required_rank': 1-d2, 'required_split': 'V(4)=O(2)+O(6)'})
for d2 in range(7):
    m = 7-d2
    matrix, coefficients = connecting(m-1, -m-1, -2*m)
    rows.append({'e': 0, 'd2': d2, 'd3': 7,
                 'extension_line_degree': -2*m,
                 'extension_dimension': len(coefficients),
                 'connecting_matrix': [[str(value) for value in row] for row in matrix.tolist()],
                 'required_rank': m, 'required_split': 'V(4)=O(2)^2'})
record = {'scope': 'Necessary intrinsic conormal splitting for a common quartic ancestor on characteristic-zero C0',
          'splitting': 'V(4)=O(2)+O(2e+2), e=0,1,2',
          'status': 'EXACT STRUCTURAL REDUCTION; actual ambient extension classes not evaluated',
          'rows': rows,
          'e0_d2_7': 'extension group zero; intrinsic sequence is already split O(2)^2',
          'retained_boundary': 'e=1,d2=d3=4 requires zero extension, not excluded'}
(HERE/'session_localcoh_conormal_hankel_2026_10_07.json').write_text(json.dumps(record, indent=2)+'\n')
print('PASS: connecting matrices reconstructed from exact Laurent multiplication.')
print('Structural criterion: e1 Hankel rank n-1; e2 rectangular ranks1,0; e0 square full rank.')
print('OPEN: actual ambient extension classes and all still-retained defective-triple incidence strata.')
