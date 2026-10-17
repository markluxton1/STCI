#!/usr/bin/env python3
"""Generate the actual first endpoint-family module at its Q1 exception.

This reduces rational coefficients before exporting to Macaulay2. No
denominator is discarded: every denominator is inverted in QQ[k]/Q1.
"""
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
k, lam = s.symbols('k lambda')
modulus = 3*k**4-9*k**3-19*k**2-43*k-4
assert s.Poly(modulus, k, modulus=23).is_irreducible


def reduce(value):
    numerator, denominator = s.fraction(s.cancel(value))
    denominator = s.rem(denominator, modulus, k)
    assert denominator != 0
    return s.rem(s.rem(numerator, modulus, k)*s.invert(denominator, modulus, k),
                 modulus, k)


data = json.loads((HERE/'session-localcoh-origin-family-1-seed.json').read_text())
seed = list(map(lambda v: reduce(s.sympify(v, locals={'k': k})), data['seed']))
kernel = list(map(s.Rational, data['kernel']))
tensor = [[s.Rational(0)]*540 for _ in range(74)]
for line in (HERE/'localcoh-incidence-tensor.txt').read_text().splitlines()[1:]:
    row, col, value = line.split()
    if int(col) < 540:
        tensor[int(row)][int(col)] += s.Rational(value)


def m2(value):
    return str(value).replace('**', '^')


def entry(row, col):
    constant = reduce(sum(tensor[row][18*i+col]*seed[i] for i in range(30)))
    linear = sum(tensor[row][18*i+col]*kernel[i] for i in range(30))
    return '(sub('+m2(constant)+',R))+lambda*(sub('+m2(linear)+',R))'


label = 'session-localcoh-origin-family-1-exception-q1'
script = [
    '-- Actual tensor module at Q1; all four geometric roots, all lambda.',
    'P=QQ[k]; K0=toField(P/ideal('+m2(modulus)+')); R=K0[lambda];',
    'L=matrix{'+','.join('{'+','.join(entry(row, col) for col in range(18))+'}'
                       for row in range(74))+'};',
    'U=matrix{'+','.join('{'+str(int(row == 72))+'}' for row in range(74))+'};',
    'print("actual 74 by 18 matrix ready at Q1");',
    'V=gens kernel transpose L;',
    'print("polynomial left kernel computed");',
    'E=transpose U*V; J=ideal E;',
    'ff=openOut "research/computations/'+label+'-evaluations.txt";',
    'ff << gens gb J << endl; close ff;',
    'print("target evaluation ideal saved");',
    'if J==ideal(1_R) then (',
    ' c=matrix{{1_R}} // E; n=V*c;',
    ' assert(transpose n*L==0); assert(transpose n*U==matrix{{1_R}});',
    ' ff=openOut "research/computations/'+label+'-dual.txt";',
    ' for row from 0 to 73 do ff << row << " " << toString n_(row,0) << endl;',
    ' close ff; print("exact polynomial dual saved")',
    ');',
    'exit 0;'
]
destination = HERE/(label+'.m2')
destination.write_text('\n'.join(script)+'\n')
print('PASS: Q1 is irreducible modulo 23 and every seed denominator is a unit.')
print(destination)
