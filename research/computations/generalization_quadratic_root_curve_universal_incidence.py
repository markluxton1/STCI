#!/usr/bin/env python3
"""Exact universal first ambient incidence for (2,2) root curves.

Only Python's standard library is needed. The accepted ambient derivation
is input, not recomputed. This script converts that derivation to Cech
matrices and verifies an explicit smooth zero of the obstruction.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

VARIABLES = [f"{letter}{j}" for letter in "abc" for j in range(3)]
ROWS = [(k,3-i,i) for i in range(4) for k in (-4,-3,-2,-1)]
COLS = [(k,1-i,i) for i in range(2) for k in range(-6,0)]
# Laurent monomial dictionaries have keys (z exponent, u degree, v degree).
F = {(j,2-i,i): {VARIABLES[3*i+j]: Q(1)} for i in range(3) for j in range(3)}
DU = {(-4,2,0): Q(-5,2), (-3,1,1): Q(-3), (-2,0,2): Q(-3,8)}
DV = {(-5,2,0): Q(3), (-4,1,1): Q(-1), (-3,0,2): Q(-9,4)}
ALPHA = {(-3,1,0): Q(1), (-2,0,1): Q(1,2)}

def add_term(poly, monomial, value):
    target = poly.setdefault(monomial, {})
    for name, coefficient in value.items():
        target[name] = target.get(name, Q(0)) + coefficient
        if not target[name]:
            del target[name]

def diff(poly, index):
    out = {}
    for powers, value in poly.items():
        if powers[index]:
            new = list(powers)
            new[index] -= 1
            add_term(out, tuple(new), {n:c*powers[index] for n,c in value.items()})
    return out

def multiply_scalar(poly, scalar):
    out = {}
    for p, value in poly.items():
        for q, coefficient in scalar.items():
            add_term(out, tuple(p[i]+q[i] for i in range(3)), {n:c*coefficient for n,c in value.items()})
    return out

def fmt(value):
    if not value:
        return "0"
    terms=[]
    for name in VARIABLES:
        c=value.get(name, Q(0))
        if not c:
            continue
        coefficient = "" if abs(c)==1 else str(abs(c))+"*"
        terms.append(("-" if c<0 else "+")+coefficient+name)
    result="".join(terms)
    return result[1:] if result.startswith("+") else result

def evaluate(value, point):
    return sum((c*point[n] for n,c in value.items()), Q(0))

D={}
for piece in (multiply_scalar(diff(F,1),DU), multiply_scalar(diff(F,2),DV), multiply_scalar(diff(F,0),ALPHA)):
    for key,value in piece.items():
        add_term(D,key,value)
D_VECTOR=[D.get(row,{}) for row in ROWS]
A=[]
for row in ROWS:
    entries=[]
    for col in COLS:
        entries.append(F.get(tuple(row[i]-col[i] for i in range(3)), {}))
    A.append(entries)

# Exact rational row reduction, also checks the asserted certificate.
def solve(matrix, rhs):
    aug=[list(row)+[v] for row,v in zip(matrix,rhs)]
    rank=0
    pivots=[]
    for j in range(len(matrix[0])):
        pivot=next((i for i in range(rank,len(aug)) if aug[i][j]),None)
        if pivot is None:
            continue
        aug[rank],aug[pivot]=aug[pivot],aug[rank]
        divisor=aug[rank][j]
        aug[rank]=[x/divisor for x in aug[rank]]
        for i in range(len(aug)):
            if i!=rank and aug[i][j]:
                coefficient=aug[i][j]
                aug[i]=[x-coefficient*y for x,y in zip(aug[i],aug[rank])]
        pivots.append(j)
        rank+=1
    if any(all(x==0 for x in row[:-1]) and row[-1] for row in aug):
        return rank,None
    solution=[Q(0)]*len(matrix[0])
    for i,j in enumerate(pivots):
        solution[j]=aug[i][-1]
    assert all(sum((x*y for x,y in zip(row,solution)),Q(0))==v for row,v in zip(matrix,rhs))
    return rank,solution

EXAMPLE={"a0":Q(4),"a1":Q(0),"a2":Q(1),"b0":Q(0),"b1":Q(0),"b2":Q(0),"c0":Q(-8),"c1":Q(0),"c2":Q(1)}
numeric_A=[[evaluate(value,EXAMPLE) for value in row] for row in A]
numeric_d=[evaluate(value,EXAMPLE) for value in D_VECTOR]
rank,solution=solve(numeric_A,numeric_d)
assert rank==12 and solution is not None

# Jacobian of A_f h-d_f at the seed. Its rank determines the local
# dimension of the universal compatibility scheme, rather than a sample rank.
jacobian=[]
for i in range(16):
    f_derivatives=[sum((entry.get(n,Q(0))*h for entry,h in zip(A[i],solution)),Q(0))-D_VECTOR[i].get(n,Q(0)) for n in VARIABLES]
    jacobian.append(f_derivatives+numeric_A[i])
pivot_columns=[0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16]
minor=[[row[j] for j in pivot_columns] for row in jacobian]
determinant=Q(1)
for j in range(16):
    pivot=next((i for i in range(j,16) if minor[i][j]),None)
    assert pivot is not None
    if pivot!=j:
        minor[j],minor[pivot]=minor[pivot],minor[j]
        determinant=-determinant
    divisor=minor[j][j]
    determinant*=divisor
    for i in range(j+1,16):
        coefficient=minor[i][j]/divisor
        minor[i]=[x-coefficient*y for x,y in zip(minor[i],minor[j])]
assert determinant==Q(-405)

artifact={
    "status":"exact matrix conversion of accepted ambient operator; smooth zero certificate",
    "characteristic":"zero",
    "variables":VARIABLES,
    "f":"(a0+a1*z+a2*z^2)*u^2+(b0+b1*z+b2*z^2)*u*v+(c0+c1*z+c2*z^2)*v^2",
    "row_basis":[f"z^{k}*u^{u}*v^{v}" for k,u,v in ROWS],
    "column_basis":[f"z^{k}*u^{u}*v^{v}" for k,u,v in COLS],
    "A_f":[[fmt(value) for value in row] for row in A],
    "d_f":[fmt(value) for value in D_VECTOR],
    "incidence":"A_f*h=d_f; equivalently all 13x13 minors of [A_f | d_f] vanish on the basepoint-free open",
    "smooth_example":{
        "f":"(z^2+4)*u^2+(z^2-8)*v^2",
        "coefficients":{n:str(v) for n,v in EXAMPLE.items()},
        "rank_A_f":rank,
        "h_solution":[str(x) for x in solution],
        "verified_identity":"A_f*h=d_f in rational arithmetic",
        "smoothness":"a=z^2+4 and c=z^2-8 are squarefree, coprime, and both nonzero at infinity; the double-cover branch divisor consists of their four distinct roots",
        "jacobian_certificate":{
            "variables":VARIABLES+[f"h{j}" for j in range(12)],
            "matrix":[[str(x) for x in row] for row in jacobian],
            "minor_columns_zero_based":pivot_columns,
            "minor_determinant":str(determinant),
            "affine_incidence_dimension_at_seed":5,
            "projective_compatibility_dimension_at_seed":4
        },
        "ruling_difference":"O_Z(-1,1) has exact order two; proved geometrically in the companion note",
        "scope":"first obstruction vanishes only; no higher lift, actual CI, or STCI existence asserted"
    }
}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(artifact,indent=2)+"\n")
print(json.dumps({"artifact":str(path),"rank_A_f":rank,"h_solution":[str(x) for x in solution],"jacobian_minor_determinant":str(determinant)},indent=2))
