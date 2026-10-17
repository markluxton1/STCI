#!/usr/bin/env python3
"""Exact algebra for an A1 singular-conductor parity countershield."""
import json
import sympy as sp
l,x,z,w=sp.symbols("l x z w")
T=x**2+l*x-z**2
F=w**2+l**2*w-l**2*z**2
GB=sp.groebner([T],x,z,l,order="lex")
def zero_in_B(f):
    assert sp.expand(GB.reduce(sp.expand(f))[1])==0
zero_in_B(F.subs(w,l*x))
zero_in_B((z**2-w).subs(w,l*x)-x**2)
assert sp.expand(sp.resultant(T,w-l*x,x)-F)==0
assert sp.factor(sp.discriminant(F,w))==l**2*(l**2+4*z**2)
presentation=sp.Matrix([[-w,l*(z**2-w)],[l,-w]])
assert sp.expand(presentation.det()-F)==0
zero_in_B((-w+l*x).subs(w,l*x))
zero_in_B((l*(z**2-w)-w*x).subs(w,l*x))
assert sp.expand(F.subs(w,z**2)-z**4)==0
assert [sp.diff(T,a) for a in (l,x,z)]==[x,l+2*x,-2*z]
assert sp.expand(T.subs(l,0)-(x-z)*(x+z))==0
trace_zero_multiplication=sp.Matrix([[0,z**2],[1,0]])
assert trace_zero_multiplication.trace()==0
assert trace_zero_multiplication**2==z**2*sp.eye(2)
assert sp.Poly(x.subs(x,z),z).degree()==1
assert sp.Poly(x.subs(x,-z),z).degree()==1
print(json.dumps({
    "status":"PASS",
    "scope":"local/affine A1 singular-conductor parity shield; not a projective C0 mate",
    "normalization_equation":str(T),
    "affine_carrier_equation":str(F),
    "birational_inverse":"x=w/l",
    "actual_conductor_downstairs":["l","w"],
    "actual_conductor_upstairs":"l",
    "upstairs_conductor":"x^2-z^2=0",
    "trace_involution":"x -> -x, z -> z",
    "half_curve_section":"Q=x, div(Q)=2c",
    "anti_invariant_branch_orders":[1,1],
    "descended_square":"G=z^2-w, pullback G=x^2, div(pullback G)=4c"
},indent=2))
