#!/usr/bin/env python3
"""Generate a Singular torsion-two incidence test; never launch Singular.

Requires SymPy (developed with 1.14). The accepted sibling's AST prefix supplies
FIRST and R4 without running its separate global-model export. Only this prefix
is reused; changing its sparse coefficient indexing affects this consumer.
The finite/infinity root positions and C2/A2 coefficient charts are separate
inputs. A generated file performs first-ideal reduction before the 16 second
residues, then tests the localized full ideal. Generation alone is no result.
"""
import argparse
import ast
from pathlib import Path

import sympy as s


def accepted_source():
    """Load the sibling through R4, before ABC and all export side effects."""
    source = Path(__file__).with_name(
        'generalization_quadratic_root_global_second_model.py')
    tree = ast.parse(source.read_text())
    cut = next(i for i, node in enumerate(tree.body)
               if isinstance(node, ast.Assign)
               and any(isinstance(t, ast.Name) and t.id == 'ABC'
                       for t in node.targets))
    env = {'__file__': str(source)}
    exec(compile(ast.Module(body=tree.body[:cut], type_ignores=[]),
                 str(source), 'exec'), env)
    return env


def root_model(orientation, source):
    """Direct FIRST substitution and Sylvester solve, with source denominators."""
    aa = s.symbols('A0:3')
    cc = s.symbols('C0:3')
    k = s.symbols('k')
    z, X, Y = s.symbols('z X Y')
    A = sum(aa[j]*z**j for j in range(3))
    C = sum(cc[j]*z**j for j in range(3))
    if orientation == 'finite':
        roots = [A+C, 2*(A+k*C), A+k*k*C]
        un, vn, ell = k*X-Y, Y-X, k-1
    else:
        roots = [A, 2*A, A+C]
        un, vn, ell = X-Y, Y, s.Integer(1)
    oldf = [s.expand(poly).coeff(z, j) for poly in roots for j in range(3)]

    def subroot(poly):
        return s.expand(sum(s.Rational(v.numerator, v.denominator)
                            * s.prod(oldf[i] for i in mon)
                            for mon, v in poly.items()
                            if all(i < 9 for i in mon)))

    dv = [subroot(poly) for poly in source['FIRST']]
    transformed = s.Poly(sum(dv[4*i+j]*un**(3-i)*vn**i*z**j
                             for i in range(4) for j in range(4)), X, Y, z)
    D = [sum(transformed.coeff_monomial(X**(3-i)*Y**i*z**j)*z**j
             for j in range(4)) for i in range(4)]
    sylvester = s.Matrix([[aa[2], aa[1], aa[0], 0],
                          [0, aa[2], aa[1], aa[0]],
                          [cc[2], cc[1], cc[0], 0],
                          [0, cc[2], cc[1], cc[0]]])
    det = s.factor(sylvester.det())
    adj = sylvester.adjugate()
    solved = []
    for i, j in [(0, 2), (1, 3)]:
        left = adj*s.Matrix([s.expand(D[h]).coeff(z, v)
                             for h in (i, j) for v in (0, 1)])
        right = adj*s.Matrix([s.expand(D[h]).coeff(z, v)
                              for h in (i, j) for v in (2, 3)])
        solved.append(list(left)+list(right[2:]))
    if orientation == 'finite':
        H = ([solved[0][j]+solved[1][j] for j in range(6)]
             + [solved[0][j]+k*solved[1][j] for j in range(6)])
    else:
        H = solved[0]+[solved[0][j]+solved[1][j] for j in range(6)]
    first = []
    for expr in [C*D[0]-A*D[2], C*D[1]-A*D[3]]:
        for j in range(2):
            coefficient = s.Poly(s.expand(expr), z).coeff_monomial(z**(3-j))
            first.append(s.cancel(coefficient/ell))
    # Preserve the original rational source solve: h = H / den.
    H = [s.cancel(h/ell) for h in H]
    den = det*ell**2
    duals = {2: [], 4: []}
    for i in range(5):
        di = s.Poly(un**(4-i)*vn**i, X, Y)
        duals[2].append(s.Poly(s.expand(
            C*di.coeff_monomial(X**3*Y)-A*di.coeff_monomial(X*Y**3)), z))
        duals[4].append(s.Poly(s.expand(
            C*C*di.coeff_monomial(X**4)-A*C*di.coeff_monomial(X**2*Y**2)
            + A*A*di.coeff_monomial(Y**4)), z))
    return aa, cc, k, z, ell, det, den, oldf+H, first, duals


def singular_polynomial(expr):
    """Coefficient first prevents Singular treating a rational as a monomial."""
    expr = s.expand(expr)
    variables = sorted(expr.free_symbols, key=str)
    if not variables:
        return '('+str(expr)+')'
    parts = []
    for powers, coefficient in s.Poly(expr, *variables).terms():
        factors = ['('+str(coefficient)+')']
        factors += [str(v)+('^'+str(n) if n != 1 else '')
                    for v, n in zip(variables, powers) if n]
        parts.append('*'.join(factors))
    return '+'.join(parts)


def generate(orientation, chart, characteristic, test='existence', mixed=False):
    if mixed and orientation != 'finite':
        raise ValueError('The mixed-direction open is defined only for finite orientation.')
    source = accepted_source()
    aa, cc, k, z, ell, det, den, values, first, duals = root_model(orientation, source)
    subs = {cc[2]: 1} if chart == 'C2' else {cc[2]: 0, aa[2]: 1}
    variables = [str(v) for v in list(aa)+list(cc)
                 + ([k] if orientation == 'finite' else []) if v not in subs]+['iv']
    fmt = lambda expr: singular_polynomial(s.sympify(expr).subs(subs))
    mode = ('Exact characteristic-zero test over QQ.' if characteristic == 0 else
            'Positive-characteristic diagnostic only; no characteristic-zero conclusion.')
    out = ['// '+mode,
           '// Root orientation: '+orientation+'; coefficient chart: '+chart+'.',
           '// Opens: Res(A,C), Disc(A), Disc(C), and k-1 in finite orientation.',
           '// Additionally k!=0.' if mixed else '// The finite chart includes k=0.',
           '// Chart C2: C2=1; chart A2: C2=0,A2=1.',
           'ring R='+str(characteristic)+',('+','.join(variables)+'),dp;',
           'option(redSB);', 'ideal first='+','.join(fmt(f) for f in first)+';',
           'print("FIRST_START");', 'ideal FG=std(first);', 'print("FIRST_DONE");',
           'poly den='+fmt(den)+';', 'poly result='+fmt(det)+';',
           'poly openCond='+('k*' if mixed else '')+'('+fmt(ell)+')*result*('+fmt(aa[1]**2-4*aa[0]*aa[2])
           +')*('+fmt(cc[1]**2-4*cc[0]*cc[2])+');']
    for i, value in enumerate(values):
        out.append('poly v'+str(i)+'=reduce('+fmt(value)+',FG);')
    out += ['poly den2=reduce(den^2,FG);',
            'proc mulred(poly a,poly b){return(reduce(a*b,FG));}']
    for (_, v, zp), poly in source['R4'].items():
        terms = []
        for mon, coefficient in poly.items():
            hcount = sum(i >= 9 for i in mon)
            part = 'den2' if hcount == 0 else 'den' if hcount == 1 else '1'
            for idx in mon:
                part = 'mulred('+part+',v'+str(idx)+')'
            terms.append('('+str(coefficient)+')*'+part)
        out.append('poly r'+str(v)+'x'+str(-zp)+'=reduce('
                   + ('+'.join(terms) or '0')+',FG);')
    out.append('print("R4_DONE");')
    second = []
    for order, count in [(2, 9), (4, 7)]:
        for j in range(count):
            terms = []
            for i in range(5):
                for zz in range(order+1):
                    if (4-i, i, -1-j-zz) in source['R4']:
                        coefficient = duals[order][i].coeff_monomial(z**zz)
                        if coefficient != 0:
                            terms.append('mulred(('+fmt(coefficient)+'),r'
                                         +str(i)+'x'+str(1+j+zz)+')')
            name = 's'+str(order)+'x'+str(j)
            out.append('poly '+name+'=reduce('+('+'.join(terms) or '0')+',FG);')
            second.append(name)
    out += ['ideal second='+','.join(second)+';', 'print("SECOND_DONE");']
    if test == 'resultant':
        # Membership is a sufficient exclusion certificate on Res(A,C)!=0.
        # Failure of this stronger test does not establish nonemptiness.
        out += ['ideal equations=first,second;', 'print("MEMBERSHIP_START");',
                'ideal GB=std(equations);', 'print("MEMBERSHIP_DONE");',
                'if (reduce(result,GB)==0) { print("RESULTANT_IN_IDEAL"); }',
                'else { print("RESULTANT_NOT_IN_IDEAL"); }']
    else:
        out += ['ideal full=first,second,iv*openCond-1;', 'print("FULL_START");',
                'ideal GB=std(full);', 'print("FULL_DONE");',
                'if (reduce(1,GB)==0) { print("UNIT_IDEAL"); }',
                'else { print("NONUNIT_IDEAL"); print(size(GB)); print(dim(GB)); }']
    out.append('quit;')
    return '\n'.join(out)+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--orientation', choices=['finite', 'infinity'], required=True)
    parser.add_argument('--chart', choices=['C2', 'A2'], required=True)
    parser.add_argument('--characteristic', type=int, default=0)
    parser.add_argument('--test', choices=['existence', 'resultant'], default='existence',
                        help='Resultant membership suffices to exclude the smooth open.')
    parser.add_argument('--mixed', action='store_true',
                        help='In finite orientation, also exclude the pure direction k=0.')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.characteristic < 0:
        parser.error('--characteristic must be nonnegative')
    if args.mixed and args.orientation != 'finite':
        parser.error('--mixed requires --orientation finite')
    args.output.write_text(generate(args.orientation, args.chart, args.characteristic,
                                    args.test, args.mixed))
    print(args.output)


if __name__ == '__main__':
    main()
