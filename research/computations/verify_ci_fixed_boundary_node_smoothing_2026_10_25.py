#!/usr/bin/env python3
"""Exact global quartic tangent maps at the line-plus-genus12 degeneration.

The source is V^2, where V=H0(I_C(4)) has the actual integral monomial-
difference basis constructed below. D is the nineteen-coefficient boundary
map derivative, and S is a unit-scaled five-node T1 map in QQ[r]/P.

The script checks ranks, all carrier/unit hypotheses, and five explicit
rational tangent pairs satisfying D=0 and S=1,r,r^2,r^3,r^4. It writes their
coefficients as JSON. This is finite tangent evidence, not a displayed
polynomial arc with exactly fixed boundary. Standard library only.
"""
from fractions import Fraction
from itertools import product


def add(*ps):
 o={}
 for p in ps:
  for m,c in p.items():o[m]=o.get(m,0)+c
 return {m:c for m,c in o.items()if c}
def sc(p,c):return {m:c*a for m,a in p.items()if c*a}
def mul(p,q):
 o={}
 for m,c in p.items():
  for n,d in q.items():
   z=tuple(a+b for a,b in zip(m,n));o[z]=o.get(z,0)+c*d
 return add(o)
def mono(*m):return {m:1}
x0,x1,x2,x3=(mono(*(int(i==j)for i in range(4)))for j in range(4))
def powm(x,n):return mono(*(n*a for a in next(iter(x))))
# Actual homogeneous quartics, with a=b=1 in the documented template.
Q=add(mul(x0,x3),sc(mul(x1,x2),-1));A=add(powm(x1,3),sc(mul(powm(x0,2),x2),-1));D3=add(powm(x2,3),sc(mul(x1,powm(x3,2)),-1))
F=add(powm(x1,4),sc(mul(powm(x0,3),x3),-1));G=add(powm(x2,4),sc(mul(x0,powm(x3,3)),-1))
H0=add(*(powm(x,2)for x in(x0,x1,x2,x3)),mul(x0,x2),sc(mul(x1,x3),2))
H1=add(sc(powm(x0,2),2),sc(powm(x1,2),3),sc(powm(x2,2),5),sc(powm(x3,2),7),mul(x0,x1),mul(x0,x3),mul(x1,x2),sc(mul(x2,x3),3))
f=add(F,mul(Q,H0),mul(x0,A));g=add(G,mul(Q,H1),mul(x3,D3))
# Restriction to C gives t-weight m1+3m2+4m3. Differences in each
# weight block form the global quartic source; coefficients stay in QQ.
wt=lambda m:m[1]+3*m[2]+4*m[3]
mons=[m for m in product(range(5),repeat=4)if sum(m)==4]
groups={w:[m for m in mons if wt(m)==w]for w in range(17)}
basis=[{m:1,block[0]:-1} for block in groups.values()for m in block[1:]]
assert len(basis)==18
def sym(p):
 a={};b={}
 for m,c in p.items():
  if m[3]:a[(wt(m)-4,)]=a.get((wt(m)-4,),0)+c*m[3]
  if m[2]:b[(wt(m)-3,)]=b.get((wt(m)-3,),0)+c*m[2]
 return add(a),add(b)
def wedge(a,b):return add(mul(a[0],b[1]),sc(mul(a[1],b[0]),-1))
def coeff(p, n):
    # Verify the global twist bound before extracting boundary coefficients.
    # This prevents silently truncating a bad local-coordinate calculation.
    if n == 19:
        assert all(0 <= exponent[0] <= 18 for exponent in p)
    return [p.get((i,), 0) for i in range(n)]
S=[sym(h)for h in basis];fs=sym(f);gs=sym(g)
Bd=[coeff(wedge(h,gs),19)for h in S]+[coeff(wedge(fs,h),19)for h in S]
# Five geometric residual nodes are encoded without choosing their roots.
P=[Fraction(c)for c in(2,3,2,9,-2,4)]
def mod(p):
 p=[Fraction(c)for c in p]
 while p and p[-1]==0:p.pop()
 while len(p)>=len(P):
  c=p[-1]/P[-1];j=len(p)-len(P)
  for i,d in enumerate(P):p[i+j]-=c*d
  while p and not p[-1]:p.pop()
 return p+[Fraction(0)]*(5-len(p))
def pmul(a,b):
 o=[Fraction(0)]*(len(a)+len(b)-1)
 for i,c in enumerate(a):
  for j,d in enumerate(b):o[i+j]+=c*d
 return mod(o)
def leval(p):
 o=[0]*5
 for m,c in p.items():o[m[0]+m[1]]+=c*(-1)**(m[0]+m[2])
 return o
# The derivative with respect to x2 is a unit in the node algebra.
# Scaling the actual smoothing class by that unit avoids modular inverses.
f1=[0,-2,-3,-1];g1=[-1,-9,2,-4]
Nv=[pmul([-x for x in g1],leval(h))for h in basis]+[pmul(f1,leval(h))for h in basis]
def rank(cols):
 a=[[Fraction(c)for c in row]for row in zip(*cols)];r=0;ps=[]
 for j in range(len(cols)):
  k=next((k for k in range(r,len(a))if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];c=a[r][j];a[r]=[x/c for x in a[r]]
  for k in range(len(a)):
   if k!=r and a[k][j]:
    c=a[k][j];a[k]=[x-c*y for x,y in zip(a[k],a[r])]
  ps.append(j);r+=1
  if r==len(a):break
 return r,ps

# Reconstruct the carrier derivatives and line determinant from the actual pair.
def derivative(poly, variable):
    out = {}
    for exponents, coefficient in poly.items():
        if exponents[variable]:
            target = list(exponents)
            target[variable] -= 1
            out[tuple(target)] = coefficient * exponents[variable]
    return out


def trim(poly):
    poly = [Fraction(c) for c in poly]
    while poly and not poly[-1]:
        poly.pop()
    return poly


def remainder(poly, divisor):
    poly = trim(poly)
    divisor = trim(divisor)
    while len(poly) >= len(divisor):
        coefficient = poly[-1] / divisor[-1]
        shift = len(poly) - len(divisor)
        for i, value in enumerate(divisor):
            poly[i + shift] -= coefficient * value
        poly = trim(poly)
    return poly


def polynomial_gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, remainder(a, b)
    return [c / a[-1] for c in a]


def raw_multiply(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i + j] += c * d
    return out


assert trim(leval(f)) == trim(leval(g)) == []
assert trim(leval(derivative(f, 2))) == trim(f1)
assert trim(leval(derivative(g, 2))) == trim(g1)
assert polynomial_gcd(P, [i * P[i] for i in range(1, len(P))]) == [1]
assert polynomial_gcd(P, f1) == [1]
for variable in range(4):
    lhs = pmul(f1, leval(derivative(g, variable)))
    rhs = pmul(g1, leval(derivative(f, variable)))
    assert lhs == rhs
line_det = raw_multiply(leval(derivative(f, 0)), g1)
other_product = raw_multiply(f1, leval(derivative(g, 0)))
line_det = [a - b for a, b in zip(line_det, other_product)]
assert trim(line_det) == trim([-c for c in raw_multiply([1, 1], P)])

boundary_rank, boundary_pivots = rank(Bd)
node_rank, node_pivots = rank(Nv)
joint_columns = [a + b for a, b in zip(Bd, Nv)]
joint_rank, joint_pivots = rank(joint_columns)
assert (boundary_rank, node_rank, joint_rank) == (19, 5, 24)

# Solve 24 exact equations for five explicit tangent pairs. The first nineteen
# outputs are zero; the last five are 1,r,r^2,r^3,r^4, respectively, in QQ[r]/P.
selected = joint_pivots
augmented = [
    [Fraction(joint_columns[j][i]) for j in selected]
    + [Fraction(int(i == 19 + k)) for k in range(5)]
    for i in range(24)
]
for column in range(24):
    pivot = next(i for i in range(column, 24) if augmented[i][column])
    augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
    value = augmented[column][column]
    augmented[column] = [c / value for c in augmented[column]]
    for row in range(24):
        if row != column and augmented[row][column]:
            value = augmented[row][column]
            augmented[row] = [
                a - value * b for a, b in zip(augmented[row], augmented[column])
            ]

witnesses = []
for k in range(5):
    vector = [Fraction(0)] * 36
    for i, j in enumerate(selected):
        vector[j] = augmented[i][24 + k]
    image = [
        sum(vector[j] * joint_columns[j][i] for j in range(36))
        for i in range(24)
    ]
    assert image == [Fraction(int(i == 19 + k)) for i in range(24)]
    witnesses.append(vector)

# Changes of basis of the equations affect no node smoothing parameter.
# Their boundary effect is only the scalar determinant direction.
base_boundary = coeff(wedge(fs, gs), 19)
assert any(base_boundary)
assert base_boundary[0] == 2 and base_boundary[18] == 1
assert polynomial_gcd(base_boundary,
    [i * base_boundary[i] for i in range(1, 19)]) == [1]

def curve_restriction(poly):
    out = {}
    for exponent, value in poly.items():
        w = wt(exponent)
        out[w] = out.get(w, 0) + value
    return {w: value for w, value in out.items() if value}

assert curve_restriction(f) == curve_restriction(g) == {}
for h in basis:
    assert curve_restriction(h) == {}
for poly in (f, g):
    assert trim(leval(poly)) == []

import json
from pathlib import Path

result = {
    'scope': 'Exact QQ tangent maps for one actual global quartic pencil. No explicit constant-boundary polynomial arc is asserted.',
    'source_dimension': 36,
    'quartic_basis': [
        [{'exponents': list(m), 'coefficient': c} for m, c in h.items()]
        for h in basis
    ],
    'source_order': 'First 18 coefficients perturb f; last 18 perturb g in the listed global basis.',
    'node_polynomial_ascending': [int(c) for c in P],
    'scaled_smoothing_class': 'F1*delta_g|L - G1*delta_f|L modulo P',
    'F1_ascending': f1,
    'G1_ascending': g1,
    'F1_is_unit_modulo_P': True,
    'node_polynomial_is_squarefree': True,
    'base_boundary_degree18_and_squarefree': True,
    'actual_global_source_vanishes_on_C': True,
    'ranks': {'affine_boundary': boundary_rank, 'nodes': node_rank, 'joint': joint_rank},
    'grassmannian_dimensions': {'pencil_space': 32, 'boundary_target': 18, 'fixed_boundary_tangent': 14, 'fixed_boundary_and_all_nodes_unsmoothed_tangent': 9},
    'joint_pivot_columns_zero_based': selected,
    'explicit_tangent_witnesses': [
        {'node_image': 'r^' + str(k), 'boundary_image': 0,
         'source_coefficients': [str(c) for c in vector]}
        for k, vector in enumerate(witnesses)
    ],
    'base_boundary_ascending': base_boundary,
    'all_exact_witness_checks_passed': True,
}
destination = Path(__file__).with_name('ci_fixed_boundary_node_smoothing_2026_10_25.json')
destination.write_text(json.dumps(result, indent=2) + '\n')
print('Exact ranks: boundary19, node5, joint24')
print('Node polynomial squarefree; smooth carrier derivative a unit; gradient dependence: PASS')
print('Five explicit rational global tangent pairs have zero boundary derivative and basis node images: PASS')
print('Projective fixed-boundary tangent dimension 14; node map onto dimension 5; common kernel 9')
print('Wrote', destination.name)
