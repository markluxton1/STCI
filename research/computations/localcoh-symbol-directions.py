#!/usr/bin/env python3
"""Exact pure-cubic lifting tests for the balanced T4(-7) top image.

Pure symbols in divided-power coefficients have c_i=h*p^i*r^(3-i).
For primitive direction degree e, deg(h)=7-3e. This script derives
its obstruction matrix from the three exact linear top-image equations.
It proves every e=0 or e=1 direction admits a nonzero top lift by
linear dimension, and gives both surviving and excluded e=2 directions.
A top lift alone is not a common ancestor for the target socle classes.
"""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'localcoh-symbol-top.json').read_text())
L=s.Matrix(DATA['annihilator'])
M=s.Matrix([[s.sympify(v) for v in row] for row in DATA['matrix']])
t=s.symbols('t')

def vector(p,r,h):
    return s.Matrix([s.expand(h*p**i*r**(3-i)).coeff(t,j)
                     for i in range(4) for j in range(8)])

def obstruction(p,r,e):
    return L*s.Matrix.hstack(*(vector(p,r,t**j) for j in range(8-3*e)))

# The map has three independent linear obstructions, so its restriction to
# 8-dimensional or 5-dimensional coefficient spaces always has a kernel.
assert L.rank()==3 and M.rank()==29 and L*M==s.zeros(3,30)
for e,dimension in ((0,8),(1,5)):
    assert dimension-L.rows>0
    print(f'PROVED linear-algebra bound: every e={e} direction has at least {dimension-L.rows} top lifts')

# Degree-two parity family, homogeneous p=a0*s^2+a2*t^2, r=b1*s*t.
a0,a2,b1=s.symbols('a0 a2 b1',nonzero=True)
p=a0+a2*t**2;r=b1*t
N=obstruction(p,r,2)
parity_matrix=N
assert N[:,0]==s.zeros(3,1)
assert s.factor(N[1,1])==-24*a0*a2**2
assert N.rank()==1
print('PASS: degree-two parity family has exactly one top-lift line (h=1)')
print('Obstruction of the second coefficient h=t:',[str(s.factor(v)) for v in N[:,1]])

# Two exact excluded primitive degree-two directions.
for p,r in ((t**2,s.Integer(1)),(s.Integer(1),t**2)):
    N=obstruction(p,r,2)
    assert N.rank()==2
    print(f'PASS: no pure top lift for p={p}, r={r}')

# One fully explicit surviving top lift in E4. This will be useful as a
# reproducible seed for the lower-order incidence, without claiming existence.
target=vector(1+t**2,t,1)
solution,params=M.gauss_jordan_solve(target)
seed=solution.subs({param:0 for param in params})
assert M*seed==target
print('PASS: explicit seed p=1+t^2, r=t, h=1 is in the computed top image')
(ROOT/'localcoh-symbol-seed.json').write_text(json.dumps({
    'p':'1+t^2','r':'t','h':'1',
    'basis_coordinates':[str(v) for v in seed],
    'kernel_coordinates':[[str(v) for v in col] for col in M.nullspace()],
    'parity_e2_obstruction_matrix':[[str(s.factor(v)) for v in row] for row in parity_matrix.tolist()],
    'warning':'Pure top lifting is necessary only; no quartic common ancestor is asserted.'
},indent=2)+'\n')
print('ALL SYMBOL-LIFTING ASSERTIONS PASSED')
