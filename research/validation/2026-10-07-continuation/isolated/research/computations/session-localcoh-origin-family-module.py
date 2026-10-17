#!/usr/bin/env python3
"""Export a generic-point module calculation for one rational endpoint family.

Run with family index 1, 2, 3, or 4. M2 works over QQ(k)[lambda]; its output is
generic evidence until all denominator/exceptional loci are audited.
"""
from pathlib import Path
import json
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
index = int(sys.argv[1]) if len(sys.argv)>1 else 1
assert index in (1, 2, 3, 4)
if index<=2:
    family = json.loads((HERE/'session-localcoh-origin-families.json').read_text())['families'][index-1]
elif index==3:
    family = {'label':'boundary-rational','p0':'0','a1':'k','a2':'1','b1':'8*k**2',
              'b2':'-2*(2*k-1)*(16*k**4+8*k**2+5)/(2*k+1)**2'}
else:
    family = {'label':'boundary-exceptional','p0':'0','a1':'-1/2','a2':'1','b1':'2','b2':'k'}
top = json.loads((HERE/'localcoh-symbol-top.json').read_text())
M = s.Matrix(top['matrix'])
pivots = M.rref()[1]
independent = M[:, pivots]
independent_rows = independent.T.rref()[1]
inverse = independent[list(independent_rows), :].inv()
kernel = M.nullspace()[0]
tensor = s.zeros(74, 542)
for line in (HERE/'localcoh-incidence-tensor.txt').read_text().splitlines()[1:]:
    row, col, value = line.split()
    tensor[int(row), int(col)] = s.Rational(value)
k, parameter, t = s.symbols('k lambda t')
coeff = {name: s.sympify(family[name], locals={'k': k}) for name in ('a1','a2','b1','b2')}
p = s.Rational(family.get('p0','1'))+coeff['a1']*t+coeff['a2']*t*t
r = 1+coeff['b1']*t+coeff['b2']*t*t
pure = s.Matrix([s.expand(t*p**i*r**(3-i)).coeff(t,j)
                 for i in range(4) for j in range(8)])
seed = s.zeros(30, 1)
for i, value in zip(pivots, inverse*pure[list(independent_rows), :]):
    seed[i] = s.cancel(value)
assert all(s.cancel(value)==0 for value in M*seed-pure)
matrix = s.Matrix(74,18,lambda row,col: s.collect(s.cancel(sum(
    tensor[row,18*i+col]*(seed[i]+parameter*kernel[i]) for i in range(30))), parameter))
def m2(value):
    return str(value).replace('**','^')
def m2_entry(value):
    polynomial=s.Poly(value,parameter)
    constant=polynomial.coeff_monomial(1)
    linear=polynomial.coeff_monomial(parameter)
    return '(sub('+m2(constant)+',K0))+lambda*(sub('+m2(linear)+',K0))'
label='session-localcoh-origin-family-'+str(index)
script=[
    '-- Exploratory QQ(k)[lambda] module calculation; exceptional k must be audited.',
    'P=QQ[k]; K0=frac P; R=K0[lambda];',
    'L=matrix{'+','.join('{'+','.join(m2_entry(value) for value in matrix.row(row))+'}'
                       for row in range(74))+'};',
    'U=matrix{'+','.join('{'+str(int(row==72))+'}' for row in range(74))+'};',
    'print("matrix ready over QQ(k)[lambda]");',
    'V=gens kernel transpose L;',
    'print("generic dual module computed");',
    'E=transpose U*V; J=ideal E;',
    'ff=openOut "research/computations/'+label+'-evaluations.txt";',
    'ff << gens gb J << endl; close ff;',
    'print("generic evaluation ideal saved");',
    'if J==ideal(1_R) then (',
    ' c=matrix{{1_R}} // E; n=V*c;',
    ' assert(transpose n*L==0); assert(transpose n*U==matrix{{1_R}});',
    ' ff=openOut "research/computations/'+label+'-generic-dual.txt";',
    ' for row from 0 to 73 do ff << row << " " << toString n_(row,0) << endl;',
    ' close ff; print("generic exact dual saved; exceptional k remains")',
    ');',
    'exit 0;'
]
destination=HERE/(label+'.m2')
destination.write_text('\n'.join(script)+'\n')
(HERE/(label+'-seed.json')).write_text(json.dumps({
    'family':family,'seed':list(map(str,seed)),'kernel':list(map(str,kernel)),
    'status':'EXPLORATORY GENERIC MODULE INPUT'
},indent=2)+'\n')
print(destination)
