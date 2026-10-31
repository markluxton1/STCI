#!/usr/bin/env python3
"""Reproduce the two exact QQ rank-drop fiber exclusions (SymPy 1.14/Singular).

Derive the length-19 base's shape from the maintained augmented minors, check
its rational and degree-18 factors, then run the maintained full incidence on
both coefficient fields. This checks these rank-drop fibers only; it says
nothing about the rank-two open or unrestricted STCI. No generated CAS files
are retained. Run with Python having SymPy and Singular on PATH.
"""
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory

import sympy as s
from quadratic_root_torsion_two_model import generate, singular_polynomial

C0, C1, k, iv = s.symbols('C0 C1 k iv')
SYMBOLS = {'C0': C0, 'C1': C1, 'k': k, 'iv': iv}


def run_cas(directory, name, script):
    path = directory / (name+'.sing')
    path.write_text(script)
    try:
        result = subprocess.run(['Singular', '-q', str(path)], text=True,
                                capture_output=True, timeout=300, check=True)
    except subprocess.TimeoutExpired as error:
        partial = ''.join(part.decode(errors='replace') if isinstance(part, bytes)
                          else (part or '') for part in (error.stdout, error.stderr))
        raise RuntimeError(name+': timed out after 300 seconds\n'+partial) from error
    output = result.stdout+result.stderr
    if '?' in output:
        raise RuntimeError(name+': Singular reported an error\n'+output)
    return output


def base_shape(directory):
    source = Path(__file__).with_name('quadratic_root_torsion_two_rank_strata.sing')
    prefix = source.read_text().split('ideal rankdrop=')[0]
    old_ring = 'ring R=0,(C0,C1,k,iv),dp;'
    assert prefix.count(old_ring) == 1
    script = prefix.replace(old_ring, 'ring R=0,(iv,C0,C1,k),lp;')
    script += ('ideal I=d01,d02,d03,d12,d13,d23,iv*openPoly-1;\n'
               'ideal G=std(I); short=0;\n'
               'for(int i=1;i<=size(G);i++){print("SHAPE:"+string(G[i]));}\nquit;\n')
    output = run_cas(directory, 'base_shape', script)
    shape = [s.sympify(line[6:].replace('^', '**'), locals=SYMBOLS)
             for line in output.splitlines() if line.startswith('SHAPE:')]
    assert len(shape) == 4
    univariate = [f for f in shape if f.free_symbols <= {k}]
    assert len(univariate) == 1
    p19 = s.Poly(univariate[0], k, domain=s.QQ)
    assert p19.degree() == 19 and s.gcd(p19, p19.diff()).degree() == 0
    _, factors = s.factor_list(p19)
    assert len(factors) == 2 and all(e == 1 for _, e in factors)
    assert any(f.monic().as_expr() == k+1 for f, _ in factors)
    p18 = next(f for f, _ in factors if f.degree() == 18)
    assert p18.is_irreducible
    values = {}
    for variable in (C0, C1, iv):
        relation = [f for f in shape if variable in f.free_symbols]
        assert len(relation) == 1
        polynomial = s.Poly(relation[0], variable)
        assert polynomial.degree() == 1
        coefficient = polynomial.coeff_monomial(variable)
        assert not coefficient.free_symbols
        values[variable] = -polynomial.coeff_monomial(1)/coefficient
        assert values[variable].free_symbols <= {k}
    assert values[C0].subs(k, -1) == 4 and values[C1].subs(k, -1) == s.Rational(1, 5)
    # Check the shape substitution against the actual maintained minors/open.
    env = dict(SYMBOLS)
    for name, expression in re.findall(r'poly (\w+)=(.*?);', prefix):
        env[name] = s.sympify(expression.replace('^', '**'), locals=env)
    def remainder(expression):
        return s.rem(s.expand(expression.subs(values, simultaneous=True)), p18.as_expr(), k)
    for name in ('d01', 'd02', 'd03', 'd12', 'd13', 'd23'):
        assert remainder(env[name]) == 0
    opened = remainder(env['openPoly'])
    assert s.gcd(s.Poly(opened, k), p18).degree() == 0
    assert remainder(iv*env['openPoly']-1) == 0
    print('BASE: squarefree degree 19 = (k+1) times irreducible degree 18; '
          'six minors and open verified', flush=True)
    return p18.as_expr(), values


def main():
    with TemporaryDirectory(prefix='stci-rank-fibers-') as temporary:
        directory = Path(temporary)
        p18, values = base_shape(directory)
        model = generate('finite', 'C2', 0)
        ring = 'ring R=0,(A0,A1,A2,C0,C1,k,iv),dp;'
        assert model.count(ring) == 1
        # Measure the localized first-stage scheme before the second obstruction.
        boundary = 'poly v0='
        assert model.count(boundary) == 1
        first_length = ('ideal firstOpen=first,iv*openCond-1;\n'
                        'ideal firstOpenGB=std(firstOpen);\n'
                        'if ((dim(firstOpenGB)==0)&&(vdim(firstOpenGB)==4)) '
                        '{ print("FIRST_LENGTH_4"); }\n')
        model = model.replace(boundary, first_length+boundary)
        number_field = ('ring R=(0,k),(A0,A1,A2,iv),dp;\nminpoly='
                        +singular_polynomial(p18)+';\n'
                        +'\n'.join('number '+str(v)+'='+singular_polynomial(values[v])+';'
                                    for v in (C0, C1)))
        rational = ('ring R=0,(A0,A1,A2,iv),dp;\n'
                    'number k=-1; number C0=4; number C1=1/5;')
        for name, declaration in [('rational', rational), ('degree18', number_field)]:
            output = run_cas(directory, name, model.replace(ring, declaration))
            assert 'FIRST_LENGTH_4' in output.splitlines()
            assert 'UNIT_IDEAL' in output.splitlines()
            assert 'NONUNIT_IDEAL' not in output.splitlines()
            print(name+': first scheme dimension 0, length 4; '
                  'exact characteristic-zero full incidence UNIT_IDEAL', flush=True)
        print('First-stage total QQ scheme length: 4+18*4=76 '
              '(not a distinct-root count)', flush=True)


if __name__ == '__main__':
    main()
