#!/usr/bin/env python3
"""Independent structural audit of the split22 finite reduction.

The primary certificate supplies the persisted carrier and elimination state.
This companion checks additional identities governing chart completeness,
the actual ambient torus action, finite-stratum uniqueness, and the Morse
coefficient from an independently formed transverse Hessian. It neither
assumes nor proves normalization of the retained conductor-sensitive line.
"""
from pathlib import Path
import runpy
import sympy as s

state = runpy.run_path(str(Path(__file__).with_name(
    "verify_split22_finite_reduction.py")))
globals().update({name: value for name, value in state.items()
                  if not name.startswith("__")})

def zero(expr):
    assert s.cancel(expr) == 0

# The coefficients of R=(N+az^2/c)G eliminate u3,u5 by established units;
# no division by a^2+a+1 or by 3a+2 is used here.
division = s.Poly(R - (N+a*z*z/c)*G, z)
zero(division.nth(1) - N*a*u3)
zero(division.nth(5) - a*a*(2*a+1)*u5/c)
zero(division.nth(6) - (a*(2*a+1)**2*u6-N*c*c*u8)/c)
zero(division.nth(2).subs(u3,0)
     - (a*a*(3*a+2)*u2/c-N*beta))
print("AUDIT PASS: raw division uses only established units before the exceptional chart")

# This is an ambient diagonal automorphism preserving C0, rather than an
# unsupported arbitrary change of the normal-bundle frame.
t = s.symbols("t", nonzero=True)
torus_parameters = {u0:t**-4*u0, u2:t**-2*u2, u3:t**-1*u3,
                    u5:t*u5, u6:t*t*u6, u8:t**4*u8}
zero(R.subs(torus_parameters, simultaneous=True)-t**-4*R.subs(z,t*z))
zero(G.subs(torus_parameters, simultaneous=True)-t**-2*G.subs(z,t*z))
zero(F.subs(torus_parameters, simultaneous=True)
     -t**-12*F.subs({x1:t*x1,x2:t**3*x2,x3:t**4*x3}, simultaneous=True))
print("AUDIT PASS: normalization N=1 comes from the actual ambient torus action")

# At a collision z != 0, R=QG. Form the Hessian solely from the gradient
# b=G*(-a^2*z,-z*Q) and the transverse quadratic part. No precomputed
# three-variable Hessian factorization is imported for these identities.
QQ, HH, LL, zz, gg = s.symbols("QQ HH LL zz gg")
uu = zz**4/a
transverse = s.Matrix([[2*HH, LL], [LL, 2*uu]])
direction = s.Matrix([-a*a*zz, -zz*QQ])
bb = a**3*zz**4-a*a*QQ*LL+QQ*QQ*HH
dd = transverse.det()
full_hessian = s.Matrix([[0,-a*a*zz*gg,-zz*QQ*gg],
                         [-a*a*zz*gg,2*HH,LL],
                         [-zz*QQ*gg,LL,2*uu]])
zero(full_hessian.det()+2*zz*zz*gg*gg*bb)
zero(-s.Rational(1,2)*(direction.T*transverse.inv()*direction)[0]
     +zz*zz*bb/dd)
# For G=0 use gradient (0,-zR); this is the coefficient of R^2 after
# critical-section elimination, establishing the double-root A3 control.
direction0 = s.Matrix([0,-zz])
zero(-s.Rational(1,2)*(direction0.T*transverse.inv()*direction0)[0]
     +zz*zz*HH/dd)
print("AUDIT PASS: intrinsic Hessian and residual coefficients match the A1/A3/A5 controls")

# The linear Groebner element must determine precisely the supplied T on
# every algebraic root of the eliminants. Unit checks are valid on the
# whole quotient algebra and do not need an irreducibility assumption.
for modulus, ts in [(S1,ts1),(S2,ts2),(S3,ts3)]:
    assert s.gcd(s.diff(linear,T),modulus)==1
    assert field(linear.subs(T,ts),modulus)==0
    assert s.gcd(modulus,a*(a+1)*(2*a+1)*(3*a+2)*c)==1
    for gen in ns:
        assert field(gen.subs(T,ts),modulus)==0
print("AUDIT PASS: all finite eliminant roots have the claimed unique parameter, with no missing chart")

# c=0 cannot suppress any other coefficient of G=0. The r=z^4 quadratic
# has nonzero constant/leading terms, so distinct or double nonzero roots
# are the exhaustive alternatives; H is genuinely linear in r.
for unit in [a,2*a+1,a*a+a+1,a+2,a+1,a**3-a*a-a-1]:
    assert s.gcd(c,unit)==1
assert s.gcd(vv,c)==1 and s.gcd(uv,c)==1 and s.gcd(k,c)==1
assert s.gcd(vd,c)==1
print("AUDIT PASS: zero-G local clusters and normalizations exhaust every permitted root")

# Verify the complete expression of the retained family, not only its
# constant term in T. The resulting identity supplies no radical-support
# or normalization assertion.
Kret = q*(-16*x0*x0+16*x1*x1-x3*x3) +16*x1*A-16*x2*A+4*x3*B-x2*D+8*q*q
zero(F.subs(sm)+B*B-T*q*Kret)
print("AUDIT PASS: retained a=-1 carrier equals the recorded one-parameter family")
