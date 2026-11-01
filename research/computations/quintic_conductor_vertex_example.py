"""Exact actual projection with a singleton length-three fiber on C0.

Python 3 and SymPy; imports the reviewed rational conductor implementation.
This certificate identifies the fiber and a remaining full-support failure.
"""

from fractions import Fraction
import sympy as sp
from quintic_conductor_singular_incidence import conductor_equations, curve_restriction


r, t, u = sp.symbols("r T u")
delta, a, b, g, j = (sp.Rational(1, 2), sp.Rational(1, 9), sp.Rational(1, 3),
                     -sp.Rational(9, 8), sp.Rational(3, 4))
u3 = r**3 - r*t
u4 = r**4 - (2*r**2 + r)*t + t**2
sections = [u4 + a*t, u4 - delta*u3 + (a+b)*t,
            u4 - 3*delta*u3 + 3*delta**2*r**2 - delta**3*r + (a+3*b+g)*t,
            u4 - 4*delta*u3 + 6*delta**2*r**2 - 4*delta**3*r + delta**4 + (a+4*b+2*g+j)*t]
fiber_equations = [sections[1] + sections[0]/2,
                   sections[2] + sections[0]/8, sections[3] - sections[0]/16]
fiber_basis = list(sp.groebner(fiber_equations, r, t))
assert fiber_basis == [r-sp.Rational(1, 3)-3*t-54*t**2, t**3]

# The source boundary U0=0 has line support, with image X2-3X1+2X0=0.
# The selected target point [1:-1/2:-1/8:1/16] is not on that line.
boundary_value = -sp.Rational(1, 8) - 3*(-sp.Rational(1, 2)) + 2
assert boundary_value != 0

p = g*r**3 + (6*delta*b+delta**3-3*delta**2)*r**2 + (delta**2*(3*a-3*b)+2*delta**3)*r - 2*a*delta**3
q = (g+2*j)*r**3 + (3*delta*(2*b+g)+5*delta**3-3*delta**2)*r**2 + (3*(a+b)*delta**2+delta**3-delta**4)*r - (a+b)*delta**3
normal_gcd = sp.Poly(sp.gcd(p, q), r).monic().as_expr()
assert normal_gcd == r-sp.Rational(1, 3)
assert sp.degree(p, r) == sp.degree(q, r) == 3  # no homogeneous gcd root at infinity

rank, equations = conductor_equations(tuple(Fraction(str(v)) for v in (delta, a, b, g, j)))
assert rank == 3
coordinates = sp.symbols("X0:4")
quadric = sum(sp.Rational(c.numerator, c.denominator)*sp.prod(x**e for x, e in zip(coordinates, mon[:4]))
              for mon, c in equations[0].items())
vertex = (1, -sp.Rational(1, 2), -sp.Rational(1, 8), sp.Rational(1, 16))
gradient_at_vertex = [sp.diff(quadric, x).subs(dict(zip(coordinates, vertex))) for x in coordinates]
quadric_rank = sp.hessian(quadric, coordinates).rank()
assert gradient_at_vertex == [0, 0, 0, 0] and quadric_rank == 3
coefficients, degree = curve_restriction(equations[0])
contact = sp.Poly(sum(sp.Rational(c.numerator, c.denominator)*u**i
                      for i, c in enumerate(coefficients)), u).monic().as_expr()
expected = (2*u+1)**2*(32*u**6-8*u**5+22*u**3-u**2+9)/128
assert sp.expand(contact-expected) == 0
assert degree == 8 and sp.degree(contact, u) == 8
assert sp.simplify((32*u**6-8*u**5+22*u**3-u**2+9).subs(u, -sp.Rational(1, 2))) != 0

print("center_rank:", rank)
print("conductor_quadric_rank:", quadric_rank)
print("vertex:", vertex)
print("gradient_at_vertex:", gradient_at_vertex)
print("entire_projective_fiber:", fiber_basis)
print("boundary_line_value:", boundary_value)
print("conormal_gcd:", normal_gcd)
print("A4_cotangent_parameter_J:", j)
print("conductor_contact:", sp.factor(contact))
print("interpretation: singleton triple fiber exists; residual conductor contact of degree six prevents full inverse support")
