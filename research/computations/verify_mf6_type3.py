#!/usr/bin/env python3
"""Exact e=0,d2=3 quartic incidence and cubic-pole exclusion on C0.

Uses and reruns the independently derived I_C(4) basis in defect12 verifier.
No sampling of the quartic pencil or omission of its exceptional member.
"""
import verify_mf6_defect12 as a

s, z, U, V, xs = a.s, a.z, a.U, a.V, a.xs
linear_U = s.Matrix([[j.coeff_monomial(U).coeff(z, i) for j in a.jets] for i in range(10)])
linear_V = s.Matrix([[j.coeff_monomial(V).coeff(z, i) for j in a.jets] for i in range(10)])
mixed = [s.expand(sum(c*a.I4[i] for i, c in enumerate(v))) for v in (linear_U-linear_V).nullspace()]
assert len(mixed) == 8
jets = [s.Poly(s.expand(f.subs(a.sub)), U, V) for f in mixed]
delta = z*(z+2)
errors = [s.expand(delta*s.expand(j.as_expr().subs(U,-V)).coeff(V,2) + s.Rational(3,8)*j.coeff_monomial(U)) for j in jets]
matrix = s.Matrix([[e.coeff(z,i) for e in errors] for i in range(13)])
quartics = [s.expand(sum(c*mixed[i] for i,c in enumerate(v))) for v in matrix.nullspace()]
assert len(quartics) == 2
F0,F1 = quartics
alpha,beta,Y = s.symbols("alpha beta Y")
F = alpha*F0+beta*F1
jet = s.Poly(s.expand(F.subs(a.sub)), U,V)
P = alpha*z**2*(z+2)**2 + beta*(z**2+4)*(z**4+16)
N = alpha*z*(z+2)*(z+4) + beta*(z**5+2*z**4+16*z**2-16*z+96)
h = jet.coeff_monomial(U)
assert s.expand(h+2*delta*P)==0
f2 = s.Rational(3,8)/delta
restriction = s.expand(jet.as_expr().subs({U:f2*Y**2-Y,V:Y}))
assert s.cancel(restriction.coeff(Y,2))==0
f3 = s.factor(-restriction.coeff(Y,3)/h)
assert s.cancel(f3+N/(16*delta**2*P))==0
assert s.factor(s.resultant(P,N,z))==2**34*beta**10*(alpha+4*beta)
# beta != 0 ensures degree P=6 and P is nonzero at all three support points of D2.
assert P.subs(z,0)==64*beta
assert P.subs(z,-2)==256*beta
assert s.expand(P).coeff(z,6)==beta
special_P = s.expand(P.subs({alpha:-4,beta:1}))
special_N = s.expand(N.subs({alpha:-4,beta:1}))
assert s.factor(special_P)==(z-2)**2*(z**2+2*z+4)**2
assert s.gcd(special_P,special_N)==z-2
# Hence f3 has total polar degree 6, or 5 at alpha=-4 beta, off D2.
assert s.cancel(f3.subs(beta,0)+(z+4)/(16*z**3*(z+2)**3))==0
# Direct infinity chart, keeping the moving normal frame rather than substituting 1/z.
w,uprime,vprime=s.symbols("w uprime vprime")
subinf={a.x3:1,a.x2:w,a.x1:w**3+2*uprime,a.x0:w**4+vprime/2+3*w*uprime}
infjet=s.Poly(s.expand(F0.subs(subinf)),uprime,vprime)
hinf=infjet.coeff_monomial(uprime)
assert s.factor(hinf)==-2*w**3*(2*w+1)**3
assert infjet.coeff_monomial(vprime)==hinf
f2inf=6/(w*(1+2*w))
ri=s.expand(infjet.as_expr().subs({uprime:f2inf*Y**2-Y,vprime:Y}))
assert s.cancel(ri.coeff(Y,2))==0
f3inf=s.factor(-ri.coeff(Y,3)/hinf)
assert s.cancel(f3inf+8*(18*w**2+8*w-1)/(w**3*(2*w+1)**3))==0
print("PASS: complete degree-three triple-compatible quartic space is a pencil")
print("PASS: beta!=0 forces deg D3>=9, or >=8 for alpha=-4 beta")
print("PASS: beta=0 has D3=2D2 and quartic divisor H=3D2")
print("RESULT: e=0 numerical type (d2,d3)=(3,6) necessarily has regular first-normal ratio")
