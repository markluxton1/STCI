"""Exact full conductor contact at the necessary singleton cone-vertex fiber.

Python 3 and SymPy. Reuses the reviewed universal conductor determinant.
The necessary family and its excluded rho values are in the October 31
conductor-cone note, section 6. L is an invertible affine reparameterization
of kappa, including L=0. No fixed center pivot or L inverse is used.
"""

import json
import sympy as sp
from quintic_conductor_cone_identity import conductor_quadric


rho, parameter, v = sp.symbols("rho L v")
sigma = 1-2*rho
pi = 1-6*rho+6*rho**2
delta_value = sigma*pi/(rho*(1-rho))
r0 = delta_value*rho
alpha = 1/(3*sigma**2)
kappa = (2-parameter)/(3*delta_value*sigma**3)
a_value = -4*r0**3*alpha+2*r0**2+r0-kappa*r0**4
b_value = delta_value*(3*r0**2*alpha-r0+kappa*r0**3)
g_value = -3*delta_value**2*(alpha*(2*r0-delta_value/3)
                            +kappa*(r0**2-r0*delta_value/3))
j_value = delta_value**4*(2*alpha/delta_value+kappa*(2*r0/delta_value-1))
assert sp.factor(j_value-delta_value**3*alpha*parameter) == 0

coordinates, universal = conductor_quadric()
original_parameters = [sp.Symbol("delta", nonzero=True), *sp.symbols("a B G J")]
values = [sp.factor(p) for p in (delta_value, a_value, b_value, g_value, j_value)]
substitution = dict(zip(original_parameters, values))
denominator = 6561*rho**2*(rho-1)**2*(2*rho-1)**7*pi**3
coefficients = {}
for monomial, coefficient in universal.terms():
    specialized = sp.factor(coefficient.subs(substitution, simultaneous=True))
    cleared = sp.cancel(denominator*specialized)
    # Prove no unrecorded parameter denominator remains.
    coefficients[monomial] = sp.Poly(cleared, rho, parameter, domain=sp.QQ).as_expr()

# This is C0 with source r=delta*v. The discarded overall factor delta^4
# in its four homogeneous coordinates is nonzero throughout this family.
curve = [v**4, v**3*(v-1), v*(v-1)**3, (v-1)**4]
contact = sp.Poly(sp.expand(sum(c*sp.prod(x**e for x, e in zip(curve, mon))
                               for mon, c in coefficients.items())), v)
constant = sp.factor(contact.as_expr().subs(v, rho))
linear = sp.factor(sp.diff(contact.as_expr(), v).subs(v, rho))
quadratic = sp.factor(sp.diff(contact.as_expr(), v, 2).subs(v, rho)/2)
expected = 9*rho**4*(rho-1)**4*(2*rho-1)*pi**5
assert constant == 0 and linear == 0
assert sp.factor(quadratic-expected) == 0

print(json.dumps({
    "sympy_version": sp.__version__,
    "parameters": "rho,L; kappa=(2-L)/(3*delta*(1-2*rho)^3)",
    "excluded_factor": "rho*(rho-1)*(2*rho-1)*(6*rho^2-6*rho+1)",
    "clearing_denominator": str(sp.factor(denominator)),
    "constant_coefficient_at_vertex": str(constant),
    "linear_coefficient_at_vertex": str(linear),
    "quadratic_coefficient_at_vertex": str(quadratic),
    "interpretation": "actual full conductor contact at the vertex is exactly two on every admissible member of this family"
}, indent=2))
