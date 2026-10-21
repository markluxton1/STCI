#!/usr/bin/env python3
"""Independent derivative/binomial audit of the new sextic symbol presentation.

Uses standard-library rational arithmetic, does not import the producer, and
does not rerun inherited ambient-obstruction or normal-flatness computations.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json


def rank(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][j]
        a[r] = [v/divisor for v in a[r]]
        for i in range(r+1, len(a)):
            if a[i][j]:
                multiplier = a[i][j]
                a[i] = [x-multiplier*y for x,y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def parse_polynomial(text):
    out = []
    for term in text.split(' + '):
        factors = term.split('*')
        coefficient = Q(factors[0])
        exponent = [0,0,0,0]
        for factor in factors[1:]:
            name, *power = factor.split('^')
            exponent[int(name[1:])] += int(power[0]) if power else 1
        out.append((coefficient, tuple(exponent)))
    return out


def direct_layer(poly, normal_degree, base_bound):
    accumulated = {}
    for coefficient, (_,b,c,d) in poly:
        for p in range(min(c,normal_degree)+1):
            for q in range(min(d,normal_degree-p)+1):
                r = normal_degree-p-q
                if q+r > d:
                    continue
                z = b+3*(c-p)+4*(d-q-r)+r
                scalar = (coefficient*comb(c,p)*factorial(d)
                          / (factorial(q)*factorial(r)*factorial(d-q-r))
                          * Q(3,2)**r)
                scalar = Q(scalar)
                # u exponent q and v exponent p+r; block 0,1,2 is v exponent.
                key = (p+r,z)
                accumulated[key] = accumulated.get(key,Q(0))+scalar
    out = [Q(0)]*((normal_degree+1)*(base_bound+1))
    for (block,z), scalar in accumulated.items():
        if scalar:
            assert 0 <= z <= base_bound
            out[(base_bound+1)*block+z] = scalar
    return out


def main():
    stem = Path(__file__).with_name('conditional_2_12_symbol_map_2026_10_20')
    data = json.loads(stem.with_suffix('.json').read_text())
    matrix = [[Q(x) for x in row] for row in data['symbol_matrix_33_by_23']]
    image = [[Q(x) for x in row] for row in data['image_matrix_33_by_22']]
    annihilator = data['annihilator_11_by_33']
    polynomials = [parse_polynomial(p) for p in data['source_basis_polynomials']]
    direct = [direct_layer(p,2,10) for p in polynomials]
    reconstructed = [list(row) for row in zip(*direct)]
    assert reconstructed == matrix
    cubic = [[Q(x) for x in row] for row in data['cubic_layer_matrix_40_by_23']]
    assert [list(row) for row in zip(*(direct_layer(p,3,9) for p in polynomials))] == cubic
    assert rank(matrix) == rank(image) == 22
    assert rank(annihilator) == 11
    assert all(sum(Q(x)*y for x,y in zip(row,col)) == 0
               for row in annihilator for col in zip(*matrix))

    # Independent first-order test using ordinary derivatives in x2 and x3.
    # The balanced frame is irrelevant to this calculation.
    columns = []
    for a in range(7):
        for b in range(7-a):
            for c in range(7-a-b):
                d = 6-a-b-c
                exponent = b+3*c+4*d
                columns.append([int(n == exponent) for n in range(25)]
                    + [c*int(n == exponent-3) for n in range(22)]
                    + [d*int(n == exponent-4) for n in range(21)])
    first_rank = rank(list(zip(*columns)))
    assert first_rank == 61
    monomials = [(a,b,c,6-a-b-c) for a in range(7)
                 for b in range(7-a) for c in range(7-a-b)]
    coefficient_columns = []
    for polynomial in polynomials:
        coefficients = dict((ex,co) for co,ex in polynomial)
        coefficient_columns.append([coefficients.get(ex,Q(0)) for ex in monomials])
    assert rank(list(zip(*coefficient_columns))) == 23
    for source_column in coefficient_columns:
        assert all(sum(Q(c)*x for c,x in zip(row,source_column)) == 0
                   for row in zip(*columns))

    # Audit only the NEW seed membership/cubic comparison. The accepted first
    # Jacobian is an input and is not reconstructed or independently re-proved.
    f = list(map(Q,[4,0,1,0,0,0,-8,0,1]))
    alpha = list(map(Q,[1024,0,256,0,96,0,-8,0,1]))
    multiplication = [[sum(f[3*component+p] for p in range(3)
                           if p+ai == degree)
                       for ai in range(9)]
                      for component in range(3) for degree in range(11)]
    membership = [[sum(Q(c)*v for c,v in zip(row,column))
                   for column in zip(*multiplication)]
                  for row in annihilator]
    assert rank(membership) == 8
    assert all(sum(c*v for c,v in zip(row,alpha)) == 0 for row in membership)

    new_jacobian_rows = []
    for row in annihilator:
        f_part = [sum(Q(row[11*component+ai+p])*alpha[ai] for ai in range(9))
                  for component in range(3) for p in range(3)]
        alpha_part = [sum(Q(row[11*component+ai+p])*f[3*component+p]
                          for component in range(3) for p in range(3))
                      for ai in range(9)]
        new_jacobian_rows.append(f_part+[Q(0)]*12+alpha_part)
    inherited = json.loads(Path(__file__).with_name(
        'generalization_quadratic_root_curve_universal_incidence.json').read_text())
    accepted_jacobian = inherited['smooth_example']['jacobian_certificate']['matrix']
    combined = [[Q(x) for x in row]+[Q(0)]*9 for row in accepted_jacobian]
    combined += new_jacobian_rows
    assert rank(combined) == 26
    assert combined == [[Q(x) for x in row] for row in
                         data['new_membership_tangent_test']['combined_jacobian_27_by_30']]

    cubic_divisibility = []
    for component in range(4):
        for degree in range(10):
            cubic_divisibility.append([
                -f[3*(component-lin)+degree-power]
                if 0 <= component-lin <= 2 and 0 <= degree-power <= 2 else Q(0)
                for lin in range(2) for power in range(8)])
    system = [row+[Q(0)]*16 for row in matrix]
    system += [row+extra for row,extra in zip(cubic,cubic_divisibility)]
    symbol_target = [sum(c*v for c,v in zip(row,alpha)) for row in multiplication]
    g0 = {(1,1):Q(1,8),(2,0):Q(-3,4),(3,1):Q(1,8)}
    cubic_target = [sum(alpha[ai]*g0.get((component,degree-ai),Q(0))
                        for ai in range(9))
                    for component in range(4) for degree in range(10)]
    target = symbol_target+cubic_target
    witness = list(map(Q,data['accepted_seed_membership']['cubic_witness_row_73']))
    assert all(sum(c*v for c,v in zip(witness,column)) == 0 for column in zip(*system))
    assert sum(c*v for c,v in zip(witness,target)) == -384
    assert rank(system) == 39
    assert rank([row+[value] for row,value in zip(system,target)]) == 40
    output = {
        'status':'independent exact audit PASS for the new symbol map',
        'producer_not_imported':True,
        'source_dimension_by_independent_derivatives':84-first_rank,
        'source_basis_independent_ambient_rank':23,
        'source_basis_has_vanishing_zeroth_and_first_jets':True,
        'second_symbol_by_independent_binomial_formula_matches':True,
        'cubic_layer_by_independent_binomial_formula_matches':True,
        'image_dimension':rank(image),
        'annihilator_dimension':rank(annihilator),
        'all_eleven_annihilators_kill_full_symbol_matrix':True,
        'new_seed_membership_rank':8,
        'new_membership_jacobian_rank_using_accepted_first_jacobian_input':26,
        'new_seed_cubic_system_rank':39,
        'new_seed_cubic_augmented_rank':40,
        'new_seed_cubic_witness_pairing':-384,
        'scope':'The new rational linear map only; no ambient incidence emptiness or global realization is asserted.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
