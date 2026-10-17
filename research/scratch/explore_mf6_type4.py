#!/usr/bin/env python3
"""Exact exploratory quartic incidence for e=0,d2=4; no exclusion claimed.

Run --resultant for the possibly expensive generic cubic-pole resultant.
"""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"computations"))
import verify_mf6_type3 as a
from sympy.polys.matrices import DomainMatrix

s,z=a.s,a.z
A,B=s.symbols("A B")
delta=A*(z**2+2*z)+B*(z**3-4*z)+z**4+8*z+16
R=A+B*(z-2)+z**2-2*z+4
assert s.resultant(delta,R,z)==256
errors=[s.expand(delta*s.expand(j.as_expr().subs(a.U,-a.V)).coeff(a.V,2)+s.Rational(3,8)*R*j.coeff_monomial(a.U)) for j in a.jets]
matrix=s.Matrix([[e.coeff(z,i) for e in errors] for i in range(13)])
kernel=DomainMatrix.from_Matrix(matrix).nullspace().to_Matrix()
assert kernel.shape==(1,8)
vector=list(kernel)
common=s.gcd_list(vector)
vector=[s.cancel(v/common) for v in vector]
assert all(s.expand(v)==0 for v in matrix*s.Matrix(vector))
jet=s.expand(sum(c*j.as_expr() for c,j in zip(vector,a.jets)))
h=jet.coeff(a.U,1).coeff(a.V,0)
S=s.cancel(h/delta)
assert s.denom(S)==1
m,y=s.symbols("m y")
moving=s.expand(jet.subs({a.U:m-y,a.V:y}))
E=moving.coeff(m,1).coeff(y,1)
K=moving.coeff(m,0).coeff(y,3)
T=s.expand(3*R*E+8*delta*K)
sample_sub={A:0,B:0}
sample_S=s.Poly(S.subs(sample_sub),z)
sample_expected=s.Poly(41*z**5+28*z**4+56*z**3+176*z**2-80*z+704,z)
assert sample_S.monic()==sample_expected.monic()
assert s.degree(s.gcd(sample_S.as_expr(),T.subs(sample_sub)),z)==0
assert matrix.subs(sample_sub).rank()==7
out=Path(__file__).with_name("mf6_type4_incidence.json")
out.write_text(json.dumps({"status":"EXPLORATORY; generic kernel only; rank-drop boundary unclassified",
 "delta":str(delta),"R":str(R),"kernel":[str(v) for v in vector],"S":str(S),"T":str(T),
 "matrix":[[str(v) for v in row] for row in matrix.tolist()]},indent=2)+"\n")
print("Saved exact incidence:",out,flush=True)
print("generic rank7; deg_z S=",s.degree(S,z),"deg_z T=",s.degree(T,z),flush=True)
print("PASS: A=B=0 rank7 and gcd(S,T)=1; generic degree-four triple incidence forces d3>=9",flush=True)
if "--resultant" in sys.argv:
    print("Computing generic Res_z(S,T)",flush=True)
    result=s.factor(s.resultant(S,T,z))
    result_path=Path(__file__).with_name("mf6_type4_resultant.txt")
    result_path.write_text(str(result)+"\n")
    print("Saved exact resultant:",result_path,"characters",len(str(result)),flush=True)
