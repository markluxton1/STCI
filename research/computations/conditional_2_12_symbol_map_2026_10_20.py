#!/usr/bin/env python3
"""Exact sextic second-symbol map for C0, using only Python's standard library.

The ambient chart and balanced conormal frame are those of STCI-R-0007:
  (x0,x1,x2,x3)=(1,z,z^3+v,z^4+u+(3/2)zv).
No accepted computation is rerun. This computes the newly requested global
k-linear restriction map by rational polynomial arithmetic and linear algebra.
The output is a proposal/evidence artifact, not a global realization certificate.
"""

from fractions import Fraction as Q
from functools import reduce
from itertools import combinations_with_replacement
from math import gcd, lcm
from pathlib import Path
import hashlib
import json


def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, Q(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: c*a for e, a in p.items() if c*a}


def mul(p, q, trunc=None):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(x+y for x, y in zip(e, f))
            if trunc is not None and g[1]+g[2] > trunc:
                continue
            out[g] = out.get(g, Q(0)) + a*b
    return {e: c for e, c in out.items() if c}


def power(p, n, trunc=None):
    out = {(0,)*len(next(iter(p))): Q(1)}
    for _ in range(n):
        out = mul(out, p, trunc)
    return out


def exponents(d):
    return [(a,b,c,d-a-b-c) for a in range(d,-1,-1)
            for b in range(d-a,-1,-1) for c in range(d-a-b,-1,-1)]


def rref(a):
    a = [[Q(x) for x in row] for row in a]
    pivots = []
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r,len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        factor = a[r][c]
        a[r] = [x/factor for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x-factor*y for x,y in zip(a[i],a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a, pivots


def transpose(a):
    return list(map(list,zip(*a)))


def nullspace(a):
    red, pivots = rref(a)
    free = [j for j in range(len(a[0])) if j not in pivots]
    out = []
    for c in free:
        row = [Q(0)]*len(a[0])
        row[c] = Q(1)
        for i,j in enumerate(pivots):
            row[j] = -red[i][c]
        out.append(row)
    return out


def primitive(row):
    den = lcm(*(x.denominator for x in row))
    ints = [int(x*den) for x in row]
    div = reduce(gcd, (abs(x) for x in ints if x))
    ints = [x//div for x in ints]
    if next(x for x in ints if x) < 0:
        ints = [-x for x in ints]
    return ints


def matmul(a,b):
    bt = transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def determinant(a):
    a = [[Q(x) for x in row] for row in a]
    out = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j,len(a)) if a[i][j]),None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j],a[pivot] = a[pivot],a[j]
            out = -out
        p = a[j][j]
        out *= p
        for i in range(j+1,len(a)):
            factor = a[i][j]/p
            a[i] = [x-factor*y for x,y in zip(a[i],a[j])]
    return out


def show_x(p):
    names = ('x0','x1','x2','x3')
    terms = []
    for e,c in sorted(p.items(), reverse=True):
        mon = '*'.join(n+(f'^{a}' if a != 1 else '')
                       for n,a in zip(names,e) if a) or '1'
        terms.append(f'{c}*{mon}')
    return ' + '.join(terms)


def encode(a):
    return [[str(x) for x in row] for row in a]


def main():
    xs = [{tuple(1 if i==j else 0 for i in range(4)): Q(1)} for j in range(4)]
    x0,x1,x2,x3 = xs
    q = add(mul(x0,x3), scale(mul(x1,x2),-1))
    A = add(mul(power(x0,2),x2), scale(power(x1,3),-1))
    B = add(mul(x0,power(x2,2)), scale(mul(power(x1,2),x3),-1))
    D = add(power(x2,3), scale(mul(x1,power(x3,2)),-1))
    # All 28 degree-six products of the known ideal generators, with multipliers.
    candidates = [mul(power(q,2),{e:Q(1)}) for e in exponents(2)]
    labels = [f'q^2*{show_x({e:Q(1)})}' for e in exponents(2)]
    for name, cubic in zip(('A','B','D'), (A,B,D)):
        candidates += [mul(mul(q,cubic),x) for x in xs]
        labels += [f'q*{name}*x{i}' for i in range(4)]
    for i,j in combinations_with_replacement(range(3),2):
        candidates.append(mul((A,B,D)[i],(A,B,D)[j]))
        labels.append(f'{("A","B","D")[i]}*{("A","B","D")[j]}')

    ambient_basis = exponents(6)
    source_columns = [[p.get(e,Q(0)) for e in ambient_basis] for p in candidates]
    _, source_pivots = rref(transpose(source_columns))
    assert len(source_pivots) == 23
    source_basis = [candidates[i] for i in source_pivots]
    source_labels = [labels[i] for i in source_pivots]

    chart = ({(0,0,0):Q(1)}, {(1,0,0):Q(1)},
             {(3,0,0):Q(1),(0,0,1):Q(1)},
             {(4,0,0):Q(1),(0,1,0):Q(1),(1,0,1):Q(3,2)})
    chart_powers = [[power(x,n,3) for n in range(7)] for x in chart]

    def chart_eval(p, trunc=2):
        out = {}
        for ex,coeff in p.items():
            term = {(0,0,0):coeff}
            for j,n in enumerate(ex):
                term = mul(term,chart_powers[j][n],trunc)
            out = add(out,term)
        return out

    # Compute every sextic's zeroth/first jets independently of the ideal-product
    # presentation. Vanishing on the dense affine C is equivalent to global
    # vanishing because O_C and E(6) are vector bundles on the integral curve.
    all_charts = [chart_eval({e:Q(1)}) for e in ambient_basis]
    jet_indices = [(j,a,b) for a,b in ((0,0),(1,0),(0,1)) for j in range(25)]
    first_jet = [[p.get(e,Q(0)) for p in all_charts] for e in jet_indices]
    _, first_jet_pivots = rref(first_jet)
    assert len(first_jet_pivots) == 61
    assert 84-len(first_jet_pivots) == len(source_basis) == 23
    # Hence the product basis spans H^0(I_C^2(6)), including sheaf saturation.
    evaluated = [chart_eval(p) for p in source_basis]
    assert all(not c or e[1]+e[2] == 2 for p in evaluated for e,c in p.items())
    assert all(e[0] <= 10 for p in evaluated for e in p)
    target_indices = [(j,a,b) for a,b in ((2,0),(1,1),(0,2)) for j in range(11)]
    symbol_matrix = [[p.get(e,Q(0)) for p in evaluated] for e in target_indices]
    _, symbol_pivots = rref(symbol_matrix)
    assert len(symbol_pivots) == 22
    image_matrix = [[row[i] for i in symbol_pivots] for row in symbol_matrix]
    image_minor_rows = rref(transpose(image_matrix))[1]
    image_minor_determinant = determinant([image_matrix[i] for i in image_minor_rows])
    assert image_minor_determinant
    annihilator = [primitive(row) for row in nullspace(transpose(image_matrix))]
    assert len(annihilator) == 11
    assert all(not x for row in matmul(annihilator,image_matrix) for x in row)
    assert len(rref(annihilator)[1]) == 11
    assert chart_eval(power(q,3)) == {}
    # The one-dimensional kernel is therefore exactly k*q^3.
    cubic_indices = [(j,a,b) for a,b in ((3,0),(2,1),(1,2),(0,3)) for j in range(10)]
    evaluated3 = [chart_eval(p,3) for p in source_basis]
    assert all(e[0] <= 8 for p in evaluated3 for e in p if e[1]+e[2] == 3)
    cubic_matrix = [[p.get(e,Q(0)) for p in evaluated3] for e in cubic_indices]

    # Multiplication alpha*f has 33 coefficients linear in alpha_0,...,alpha_8
    # for each f. The eleven equations are stored symbolically as triples
    # (integer coefficient, alpha index, f component, quadratic base index).
    incidence_equations = []
    for row in annihilator:
        terms = []
        for comp in range(3):
            for ai in range(9):
                for fj in range(3):
                    coeff = row[11*comp+ai+fj]
                    if coeff:
                        terms.append([coeff,ai,('a','b','c')[comp],fj])
        incidence_equations.append(terms)

    # A controlled boundary test, not a search: the accepted first-compatible
    # torsion-two seed survives the new degree-six second-symbol membership.
    seed_f = [[Q(4),Q(0),Q(1)], [Q(0)]*3, [Q(-8),Q(0),Q(1)]]
    seed_alpha_matrix = [[sum(row[11*j+i+k]*seed_f[j][k]
                             for j in range(3) for k in range(3))
                          for i in range(9)] for row in annihilator]
    seed_alpha_kernel = nullspace(seed_alpha_matrix)
    assert len(seed_alpha_kernel) == 1
    seed_alpha = primitive(seed_alpha_kernel[0])
    assert seed_alpha == [1024,0,256,0,96,0,-8,0,1]

    # The actual-sextic cubic comparison is exported as a finite linear layer.
    # For the displayed seed its canonical first relation is known explicitly.
    seed_target = [sum(seed_alpha[i-k]*seed_f[j][k]
                       for k in range(3) if 0 <= i-k <= 8)
                   for j in range(3) for i in range(11)]
    seed_g0 = {(1,2,1):Q(1,8),(0,1,2):Q(-3,4),(1,0,3):Q(1,8)}
    alpha_poly = {(i,0,0):Q(c) for i,c in enumerate(seed_alpha) if c}
    seed_ag0 = mul(alpha_poly,seed_g0)
    seed_fpoly = {(i,2-j,j):c for j,row in enumerate(seed_f)
                  for i,c in enumerate(row) if c}
    f_linear_columns = [mul(seed_fpoly,{(j,a,b):Q(1)})
                        for a,b in ((1,0),(0,1)) for j in range(8)]
    seed_cubic_eqs = [list(symbol_matrix[i])+[Q(0)]*16 for i in range(33)]
    seed_cubic_rhs = list(seed_target)
    for i,e in enumerate(cubic_indices):
        seed_cubic_eqs.append(list(cubic_matrix[i])+
                               [-p.get(e,Q(0)) for p in f_linear_columns])
        seed_cubic_rhs.append(seed_ag0.get(e,Q(0)))
    seed_cubic_rank = len(rref(seed_cubic_eqs)[1])
    seed_cubic_augmented_rank = len(rref([row+[rhs] for row,rhs in
                                        zip(seed_cubic_eqs,seed_cubic_rhs)])[1])
    seed_cubic_witness = next(primitive(w) for w in nullspace(transpose(seed_cubic_eqs))
                              if sum(a*b for a,b in zip(w,seed_cubic_rhs)))
    assert all(sum(seed_cubic_witness[i]*seed_cubic_eqs[i][j]
                   for i in range(len(seed_cubic_eqs))) == 0 for j in range(39))
    seed_cubic_witness_value = sum(a*b for a,b in zip(seed_cubic_witness,seed_cubic_rhs))
    assert seed_cubic_witness_value

    # New comparison with the accepted first-incidence tangent space. The
    # accepted Jacobian is an input; its old seed proof is not rerun here.
    first_input = Path(__file__).with_name('generalization_quadratic_root_curve_universal_incidence.json')
    first_data = json.loads(first_input.read_text())
    accepted_jacobian = first_data['smooth_example']['jacobian_certificate']['matrix']
    combined_jacobian = [[Q(x) for x in row]+[Q(0)]*9 for row in accepted_jacobian]
    for row in annihilator:
        f_derivatives = [sum(seed_alpha[i]*row[11*j+i+k] for i in range(9))
                         for j in range(3) for k in range(3)]
        alpha_derivatives = [sum(row[11*j+i+k]*seed_f[j][k]
                                 for j in range(3) for k in range(3)) for i in range(9)]
        combined_jacobian.append(f_derivatives+[Q(0)]*12+alpha_derivatives)
    combined_rank = len(rref(combined_jacobian)[1])
    assert combined_rank == 26

    output = {
        'status':'new exact reduction; see independent audit note; no canonical promotion',
        'field':'QQ; formulas base-change to every characteristic-zero field',
        'curve':['s^4','s^3*t','s*t^3','t^4'],
        'chart':['1','z','z^3+v','z^4+u+(3/2)*z*v'],
        'frame':'u=b_original-(3/2)*z*a_original, v=a_original; both O(-7)',
        'target_basis':'z^j*u^2, z^j*u*v, z^j*v^2, each j=0,...,10',
        'ideal_generators':{'q':show_x(q),'A':show_x(A),'B':show_x(B),'D':show_x(D)},
        'ambient_sextic_dimension':84,
        'zeroth_and_first_jet_rank':61,
        'source_dimension':23,
        'source_basis_labels':source_labels,
        'source_basis_polynomials':[show_x(p) for p in source_basis],
        'symbol_matrix_33_by_23':encode(symbol_matrix),
        'symbol_rank':22,
        'kernel':'k*q^3',
        'image_basis_labels':[source_labels[i] for i in symbol_pivots],
        'image_matrix_33_by_22':encode(image_matrix),
        'image_rank_certificate':{'minor_rows_zero_based':image_minor_rows,
                                  'minor_determinant':str(image_minor_determinant)},
        'annihilator_11_by_33':annihilator,
        'alpha_f_incidence_terms':incidence_equations,
        'alpha_f_term_encoding':['integer coefficient','alpha index','f component','f base index'],
        'interpretation':'Eleven bilinear equations for [f] in P8 and [alpha] in P8. Retain basepoint-free f and alpha nonzero; alpha is allowed to have zeros.',
        'cubic_layer_matrix_40_by_23':encode(cubic_matrix),
        'cubic_layer_basis':'z^j*u^3, z^j*u^2*v, z^j*u*v^2, z^j*v^3, each j=0,...,9; degree-nine rows are zero',
        'next_global_sextic_condition':'M*c=coeff(alpha*f), F_c,3-alpha*G0=f*(ell(z)*u+m(z)*v), deg ell,m <=7; G0 is the accepted canonical first cubic correction over K1.',
        'accepted_seed_membership':{'f':['z^2+4','0','z^2-8'],
                                    'alpha_coefficients_ascending':seed_alpha,
                                    'alpha_matrix_rank':len(rref(seed_alpha_matrix)[1]),
                                    'cubic_system_rank':seed_cubic_rank,
                                    'cubic_augmented_rank':seed_cubic_augmented_rank,
                                    'cubic_witness_row_73':seed_cubic_witness,
                                    'cubic_witness_value':str(seed_cubic_witness_value),
                                    'already_excluded_by':'accepted second ambient obstruction 1/8'},
        'new_membership_tangent_test':{
            'accepted_input':str(first_input),
            'accepted_input_sha256':hashlib.sha256(first_input.read_bytes()).hexdigest(),
            'variables':'a0,a1,a2,b0,b1,b2,c0,c1,c2,h0,...,h11,alpha0,...,alpha8',
            'combined_jacobian_27_by_30':encode(combined_jacobian),
            'combined_jacobian_rank':combined_rank,
            'projective_tangent_dimension':30-combined_rank-2,
            'accepted_K1_projective_dimension':4,
            'interpretation':'The new global-symbol membership condition is not automatic on the smooth first-incidence component through the seed. No K2 or torsion intersection conclusion follows.'},
        'limitations':['No first/second ambient obstruction or Picard intersection is solved here.',
                       'No global mate or standard-basis certificate is asserted.'],
    }
    dest = Path(__file__).with_suffix('.json')
    dest.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'source_dimension':23,'target_dimension':33,'image_rank':22,
                      'annihilator_rank':11,'kernel':'k*q^3','output':str(dest)}))
    for i,row in enumerate(annihilator,1):
        names=[f'{c}{j}' for c in ('P','Q','R') for j in range(11)]
        print(f'L{i}: '+' + '.join(f'{c}*{name}' for c,name in zip(row,names) if c))
    print(f'Seed new membership alpha kernel dimension=1; cubic ranks={seed_cubic_rank},{seed_cubic_augmented_rank}')


if __name__ == '__main__':
    main()
