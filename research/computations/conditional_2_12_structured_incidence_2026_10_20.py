#!/usr/bin/env python3
"""Export the exact structured (2,12;6,16;2) candidate and its next lift.

No Groebner basis, determinant expansion, or search for global pairs is run.
The existing audited generator supplies the inherited first/second equations.
Its executable prefix is loaded without its artifact-writing footer.
"""
import ast
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    inherited = here / 'generalization_quadratic_root_global_second_model.py'
    tree = ast.parse(inherited.read_text())
    stop = next(i for i, node in enumerate(tree.body)
                if isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == 'stem'
                        for t in node.targets))
    env = {'__file__': str(inherited), '__name__': 'inherited_equation_export'}
    exec(compile(ast.Module(body=tree.body[:stop], type_ignores=[]),
                 str(inherited), 'exec'), env)
    data = json.loads((here / 'conditional_2_12_symbol_map_2026_10_20.json').read_text())
    ca, cm, cs, var, fmt = (env[n] for n in ('ca', 'cm', 'cs', 'var', 'fmt'))
    names = env['NAMES']
    alpha_indices = list(range(len(names), len(names)+9))
    names.extend(f'al{i}' for i in range(9))
    # H1 O(10,-14): base degree 0..10, direction Laurent powers -13..-1.
    source = [(j, k) for j in range(11) for k in range(-13, 0)]
    target = [(j, k) for j in range(13) for k in range(-11, 0)]
    vector_indices = list(range(len(names), len(names)+143))
    names.extend(f'tv{i}' for i in range(143))
    core_names = list(names)
    c_indices = list(range(len(names), len(names)+23))
    names.extend(f'gc{i}' for i in range(23))
    ell_indices = list(range(len(names), len(names)+16))
    names.extend(f'el{i}' for i in range(16))
    # fmt reads the same extended list object.
    alpha = [var(i) for i in alpha_indices]
    af = []
    for comp in range(3):
        for degree in range(11):
            af.append(ca(*(cm(alpha[k], var(3*comp+degree-k))
                           for k in range(9) if 0 <= degree-k <= 2)))
    symbol = [ca(*(cs(p, Q(c)) for p,c in zip(af,row) if c))
              for row in data['annihilator_11_by_33']]
    sparse = []
    torsion = []
    for ri, (j,k) in enumerate(target):
        equation = {}
        for ci, (l,m) in enumerate(source):
            base_degree, direction_degree = j-l, k-m
            if 0 <= base_degree <= 2 and 0 <= direction_degree <= 2:
                coefficient_index = 3*direction_degree+base_degree
                sparse.append([ri,ci,coefficient_index])
                equation = ca(equation, cm(var(coefficient_index),var(vector_indices[ci])))
        torsion.append(equation)
    # Explicit open: f finite in both rulings and generically separable.
    def sylvester_indices(swapped=False):
        out = [[None]*6 for _ in range(4)]
        for component in range(3):
            for shift in range(2):
                for degree in range(3):
                    idx = 3*degree+component if swapped else 3*component+degree
                    out[degree+shift][2*component+shift] = idx
        return out
    base_open = sylvester_indices()
    direction_open = sylvester_indices(True)
    # First unresolved global lift: retain actual 23 sextic coefficients.
    M = [[Q(x) for x in row] for row in data['symbol_matrix_33_by_23']]
    C = [[Q(x) for x in row] for row in data['cubic_layer_matrix_40_by_23']]
    sextic_symbol = [ca(*(cs(var(c_indices[i]),x) for i,x in enumerate(row) if x),
                        cs(af[j],Q(-1))) for j,row in enumerate(M)]
    cubic = []
    for comp in range(4):
        for degree in range(10):
            row = C[10*comp+degree]
            terms = [cs(var(c_indices[i]),x) for i,x in enumerate(row) if x]
            terms.extend(cs(cm(alpha[k],env['G0'].get((3-comp,comp,degree-k),{})),Q(-1))
                         for k in range(9))
            # f*(ell(z) u + m(z) v), degrees ell,m <= 7.
            for lin in range(2):
                fcomp = comp-lin
                if 0 <= fcomp <= 2:
                    for k in range(8):
                        if 0 <= degree-k <= 2:
                            terms.append(cs(cm(var(ell_indices[8*lin+k]),
                                               var(3*fcomp+degree-k)),Q(-1)))
            cubic.append(ca(*terms))

    def matrix_indices(rows):
        return 'matrix{'+','.join('{'+','.join('0' if x is None else names[x]
                                              for x in row)+'}' for row in rows)+'}'
    def equations(label, polys):
        return label+'={'+','.join(fmt(p) for p in polys)+'};'
    stem = Path(__file__).with_suffix('')
    model = stem.with_suffix('.m2')
    rows = [
        '-- Exact structured incidence; no saturation, elimination, or realization claimed.',
        '-- Work on the explicitly specified open and quotient the three free scalings.',
        'R=QQ['+','.join(names)+',MonomialOrder=>GRevLex];',
        equations('symbolEquations',symbol),
        equations('firstEquations',env['FIRST']),
        equations('secondEquations',env['SECOND']),
        equations('torsionEquations',torsion),
        'structuredIdeal=ideal join(symbolEquations,firstEquations,secondEquations,torsionEquations);',
        'baseSylvester='+matrix_indices(base_open)+';',
        'directionSylvester='+matrix_indices(direction_open)+';',
        'baseOpen=minors(4,baseSylvester);',
        'directionOpen=minors(4,directionSylvester);',
        'reducedOpen=ideal {'+','.join(fmt(p) for p in env['d'])+'};',
        'alphaOpen=ideal {'+','.join(names[i] for i in alpha_indices)+'};',
        'torsionVectorOpen=ideal {'+','.join(names[i] for i in vector_indices)+'};',
        '-- Required open: D(baseOpen) intersect D(directionOpen) intersect',
        '-- D(reducedOpen) intersect D(alphaOpen) intersect D(torsionVectorOpen).',
        '-- D(J) means the complement of V(J), not inversion of every generator.',
        '-- gc/el variables are absent from structuredIdeal: an unused affine factor.',
        equations('nextSexticSymbolEquations',sextic_symbol),
        equations('nextSexticCubicEquations',cubic),
        'nextGlobalLiftIdeal=structuredIdeal+ideal join(nextSexticSymbolEquations,nextSexticCubicEquations);',
        '-- This extension is exported, not asserted soluble or empty.',
        'print("STRUCTURED_MODEL_READY: 11 symbol,16 first,25 second,143 torsion-kernel equations");',
        'print("NEXT_GLOBAL_LIFT_EXPORTED: 33 symbol and40 cubic coefficient equations");',
        'print("NO_ELIMINATION_OR_GLOBAL_REALIZATION_CLAIMED");',
    ]
    model.write_text('\n'.join(rows)+'\n')
    meta = {
        'status':'exact candidate scheme and first unresolved global sextic lift; not an emptiness or nonemptiness certificate',
        'configuration':{'r':2,'s':12,'a':6,'b':16,'epsilon':2},
        'inherited_generator':inherited.name,
        'inherited_sha256':sha256(inherited.read_bytes()).hexdigest(),
        'inherited_artifacts_rewritten':False,
        'core_variables':core_names,
        'core_equation_counts':{'symbol':11,'first':16,'second':25,'torsion_kernel':143},
        'torsion_source_basis':source,'torsion_target_basis':target,
        'torsion_sparse_entries_row_column_f_index':sparse,
        'torsion_coefficient_order':['a0','a1','a2','b0','b1','b2','c0','c1','c2'],
        'torsion_matrix_shape':[143,143],
        'torsion_projective_vector_dimension':142,
        'torsion_determinant_degree':143,
        'torsion_equivalence':'On the reduced doubly finite (2,2) open, a nonzero kernel vector is a nonzero section of O_Z(12,-12); componentwise degree zero and connectedness make it nowhere zero.',
        'open_conditions':['rank baseSylvester=4','rank directionSylvester=4',
                           'not all binary-quartic discriminant coefficients zero',
                           'alpha != 0','torsion vector != 0'],
        'base_sylvester_f_indices':base_open,'direction_sylvester_f_indices':direction_open,
        'scalings':'f -> lambda f, alpha -> mu alpha, torsion vector -> nu vector; h invariant. Optional global coefficients gc scale by lambda*mu and el by mu.',
        'next_global_lift_equation_counts':{'symbol':33,'cubic':40},
        'next_global_lift':'M gc=coeff(alpha f); C gc-coeff(alpha G0)-coeff(f*(ell u+m v))=0; deg ell,m<=7.',
        'next_global_lift_interpretation':'First unresolved divisibility of an actual global sextic by the canonical embedded root lift, retaining all zeros of alpha.',
        'subsequent_conditions':['sextic quartic and later compatibility',
                                 'abstract next root obstruction at normal degree5',
                                 'actual degree16 coefficients and degree12 standard-basis certificate',
                                 'full initial-pair coprimality and global gcd/Bezout'],
        'model_file':str(model),
        'global_elimination_performed':False,
        'nonempty_full_incidence_claimed':False,
    }
    stem.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps({'model':str(model),'core_variables':len(core_names),
                      'core_equations':195,'next_lift_equations':73,
                      'torsion_nonzero_entries':len(sparse),
                      'elimination_performed':False},indent=2))


if __name__ == '__main__':
    main()
