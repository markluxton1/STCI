#!/usr/bin/env python3
"""Independent exact algebra for the (p,r)=(8,1/2) scroll conductor.

No owner checker or owner coefficient table is imported.  The full-scheme
conductor and all-mate conclusion are proved in the companion audit note.
"""
import hashlib
import json
from pathlib import Path
import sympy as sp

x, y, z, w, U, V, a, b = sp.symbols("x y z w U V a b")
chi = x - 8*y
L = 96*w + chi + 4*z
G = x*L - 8*y*z
F = sp.expand((x**3*chi-G**2)/64)
pull = {x: U*b**2, y: U*(b**2-a**2)/8, z: V*b**2,
        w: (U*(a*b-a**2)-V*(a**2+3*b**2))/96}
v, u = U*a*b, V*a*b

def restrict(poly):
    return sp.expand(poly.subs(pull, simultaneous=True))

assert restrict(F) == 0
assert sp.factor(sp.discriminant(F,w)) == 9*x**5*chi
assert sp.gcd_list(sp.Poly(F,w).all_coeffs()) == 1
sections = [restrict(q) for q in (x,y,z,w)] + [v,u]
complete_basis = [T*m for T in (U,V) for m in (a*a,a*b,b*b)]
matrix = sp.Matrix([[sp.Poly(q,U,V,a,b).coeff_monomial(m)
                     for q in sections] for m in complete_basis])
assert matrix.rank() == 6

# The two added sections have the following monic quadratic closure.
closure = [(v*v, x*chi), (u*v, z*chi)]
assert all(sp.expand(left-restrict(sp.cancel(right))) == 0
           for left,right in closure)
assert sp.expand(u*u-restrict(z)*v-restrict(-z*chi-3*z*z-96*z*w)) == 0

# Independently obtained multiplication-by-conductor identities.
conductor = [x*x, x*y, G]
v_products = [x*G, y*G, x*x*chi]
u_products = [z*G, (L*G-x*x*chi)/8, x*z*chi]
assert all(sp.expand(restrict(q)*v-restrict(p)) == 0
           for q,p in zip(conductor,v_products))
assert all(sp.expand(restrict(q)*u-restrict(p)) == 0
           for q,p in zip(conductor,u_products))
hb = sp.Matrix([[x,0],[-z,x],[L,-8*y]])
minors = [sp.expand(hb.extract(pair,[0,1]).det())
          for pair in ((0,1),(0,2),(1,2))]
assert all(sp.expand(p-q) == 0 for p,q in zip(minors,[x*x,-8*x*y,-G]))
residual = [sp.cancel(restrict(q)/(U*U*b*b)) for q in conductor]
assert residual == [b*b,(b*b-a*a)/8,a*b]
assert sp.expand(residual[0]-8*residual[1]) == a*a

# Direct fixed-C0 incidence after an invertible ambient linear change.
tt = sp.symbols("tt")
curve = {x:1+4*tt-16*tt**3-16*tt**4,
         y:tt-4*tt**3,z:tt-12*tt**3-16*tt**4,w:tt**4}
old_coordinates = [x-4*y+16*w,3*y/2-z/2-8*w,(y-z-16*w)/8,w]
assert sp.Matrix([[sp.diff(q,c) for c in (x,y,z,w)]
                  for q in old_coordinates]).det() != 0
assert [sp.expand(q.subs(curve)) for q in old_coordinates] == [1,tt,tt**3,tt**4]
assert sp.expand(F.subs(curve)) == 0
assert sp.factor(G.subs(curve)/curve[x]**2) == (1-2*tt)/(1+2*tt)

# Generic E chart: z=1, s=U/V, t=a/b; D is s^2=0.
s,t = sp.symbols("s t")
mod_s2 = lambda q: sp.Poly(sp.expand(q),s).rem(sp.Poly(s*s,s)).as_expr()
wE = (s*(t-t*t)-t*t-3)/96
sigma_tE = s-t
assert mod_s2(wE.subs(t,sigma_tE)-wE) == 0
assert mod_s2(sigma_tE.subs(t,sigma_tE)-t) == 0
assert mod_s2((1+s)*t*t-s*t+96*wE+3) == 0

# Generic F chart: U=a=1, t=b/a; D is t^2=0.
R = sp.symbols("R")
mod_t2 = lambda q: sp.Poly(sp.expand(q),t).rem(sp.Poly(t*t,t)).as_expr()
wF = (t-1-R)/96
sigma_tF, sigma_RF = -t,R-2*t
assert mod_t2(wF.subs({t:sigma_tF,R:sigma_RF},simultaneous=True)-wF) == 0
assert mod_t2(sigma_RF.subs({t:sigma_tF,R:sigma_RF},simultaneous=True)-R) == 0

# Nilpotent roots of unity have no nonzero infinitesimal term in char0:
# (c+d epsilon)^n = c^n+n c^(n-1)d epsilon.  Verify representative n,
# while the symbolic binomial formula proves every positive integer n.
c,d,eps = sp.symbols("c d eps")
for n in range(1,9):
    rem = sp.Poly(sp.expand((c+d*eps)**n),eps).rem(sp.Poly(eps**2,eps)).as_expr()
    assert rem == c**n+n*c**(n-1)*d*eps

source = Path(__file__).resolve()
out = {
    "status":"PASS",
    "scope":"Independent exact normalization/conductor and generic Artin deck identities for MF6 p8,r1/2; all-mate theorem is in the audit note",
    "checker_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
    "carrier_from_elimination":str(F),
    "complete_section_rank":matrix.rank(),
    "conductor_quadrics":[str(q) for q in conductor],
    "v_multiplication_certificates":[str(q) for q in v_products],
    "u_multiplication_certificates":[str(q) for q in u_products],
    "upstairs_entire_conductor":"2{U=0}+2{b=0}",
    "E_generic_trace_action":{"s":"s","t":"s-t"},
    "F_generic_trace_action":{"t":"-t","V":"V-2t"},
    "sympy_version":sp.__version__,
}
dest = source.with_suffix(".json")
dest.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":out["status"],"checker_sha256":out["checker_sha256"],"output":str(dest)},indent=2))
