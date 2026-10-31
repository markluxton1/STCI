"""Exact bounded replay for the nonintegral conductor-module witness.

Scope: (delta,a,B,G,J)=(1,0,0,-2,1), on X0=1 and
2*X1-X2+5 != 0. This script does not analyze the excluded chart boundary,
additional components there, or irreducibility of the residual cubic factor.
"""
import json
import sys
import sympy as s

X0, X1, X2, X3, h, z = s.symbols("X0 X1 X2 X3 h z")
X = (X0, X1, X2, X3)
params = {"delta": 1, "a": 0, "B": 0, "G": -2, "J": 1}

# The accepted inverse substitution, specialized at the stated parameters.
U3 = X0 - X1
U2 = (X2 - 3*X1 + 2*X0 + 2*h + z) / 3
U0 = X3 - 2*X2 + 2*X1 - X0 - h + 2*z
Z0, Z1, Z2, Z3, Z4, Z5 = (
    X0 - U3, -U3, h - U2, U2, z, U0
)
source_quadrics = [
    Z4**2 - Z3*Z5,
    Z2*Z4 - Z1*Z5,
    Z2*Z3 - Z1*Z4,
    Z2**2 - Z3*Z4 - Z0*Z5,
    Z1*Z2 - Z3**2 - Z0*Z4,
]
P = (
    Z0**2*Z2*Z5 + Z0**2*Z3**2 - 2*Z0*Z1**2*Z3
    + 5*Z0*Z1**2*Z5 - 5*Z0*Z1*Z3**2 + Z0*Z1*Z3*Z5
    + Z1**4 + 5*Z1**3*Z3 + 10*Z1**3*Z4 + Z1**3*Z5
    + 10*Z1**2*Z3**2 + 5*Z1**2*Z3*Z4
)

# Rank-three center certificate and actual residual linear equations.
center_monomials = (h**2, h*z, z**2)
rows = [s.expand(q) for q in source_quadrics]
pivot = 0
for mon in center_monomials:
    idx = next((i for i in range(pivot, 5)
                if s.Poly(rows[i], h, z).coeff_monomial(mon) != 0), None)
    if idx is None:
        continue
    rows[pivot], rows[idx] = rows[idx], rows[pivot]
    coeff = s.Poly(rows[pivot], h, z).coeff_monomial(mon)
    rows[pivot] = s.expand(rows[pivot] / coeff)
    for i in range(5):
        if i != pivot:
            c = s.Poly(rows[i], h, z).coeff_monomial(mon)
            if c:
                rows[i] = s.expand(rows[i] - c*rows[pivot])
    pivot += 1
assert pivot == 3
residual = [s.Poly(row, h, z) for row in rows[3:]]
a1, a2 = [p.coeff_monomial(1) for p in residual]
b1, b2 = [p.coeff_monomial(h) for p in residual]
c1, c2 = [p.coeff_monomial(z) for p in residual]

# Reduce P to A4+B3*h+C3*z using three independent center relations.
quadrics = [s.Poly(s.expand(q), h, z, *X) for q in source_quadrics]
Cmat = s.Matrix([[q.coeff_monomial(m) for m in center_monomials]
                 for q in quadrics])
selected = [0, 1, 3]
M = Cmat[selected, :]
assert M.det() != 0
rhs = [-(quadrics[i].as_expr() - sum(Cmat[i, j]*center_monomials[j]
                                      for j in range(3)))
       for i in selected]
sol = M.inv() * s.Matrix(rhs)
replacement = {center_monomials[j]: s.expand(sol[j]) for j in range(3)}

def vertical_reduce(poly):
    p = s.Poly(s.expand(poly), h, z, *X)
    while True:
        chosen = None
        for mon, coeff in p.terms():
            eh, ez = mon[:2]
            xpart = s.prod(X[i]**mon[i+2] for i in range(4))
            if eh >= 2:
                chosen = (coeff, h**2, h**(eh-2)*z**ez*xpart)
                break
            if eh >= 1 and ez >= 1:
                chosen = (coeff, h*z, h**(eh-1)*z**(ez-1)*xpart)
                break
            if ez >= 2:
                chosen = (coeff, z**2, h**eh*z**(ez-2)*xpart)
                break
        if chosen is None:
            return s.expand(p.as_expr())
        coeff, key, factor = chosen
        p = s.Poly(s.expand(p.as_expr() - coeff*factor*key
                            + coeff*factor*replacement[key]), h, z, *X)

normal_form = vertical_reduce(P)
A4 = s.expand(normal_form.subs({h: 0, z: 0}))
B3 = s.expand(s.diff(normal_form, h).subs({h: 0, z: 0}))
C3 = s.expand(s.diff(normal_form, z).subs({h: 0, z: 0}))

# Full ideal reductions certify q=P and its explicit module representation
# modulo all five source quadrics.
gb = s.groebner(source_quadrics, h, z, *X, order="lex")
root_identity_remainder = gb.reduce(s.expand(P*Z5 - (Z2 + Z3)**5))[1]
module_identity_remainder = gb.reduce(
    s.expand(P - A4 - B3*h - C3*z)
)[1]
assert root_identity_remainder == 0
assert module_identity_remainder == 0

# Actual conductor minors, up to nonzero scalar, from the residual rows.
quadric = s.factor(b1*c2 - b2*c1)
cubic_h = s.factor(c1*a2 - c2*a1)
cubic_z = s.factor(b2*a1 - b1*a2)
chart_Q = s.expand(quadric.subs(X0, 1))
chart_coeff = s.factor(chart_Q.coeff(X3))
chart_const = s.expand(chart_Q - chart_coeff*X3)
chart_X3 = s.factor(-chart_const/chart_coeff)
assert s.factor(chart_coeff - (2*X1 - X2 + 5) / s.Integer(18)) == 0
chart_cubics = [s.together(f.subs({X0: 1, X3: chart_X3})).as_numer_denom()[0]
                for f in (cubic_h, cubic_z)]
common = s.factor(s.gcd(*chart_cubics))
line = X1 - X2
residual_cubic = (56*X1**3 - 96*X1**2*X2 + 56*X1**2
                  + 42*X1*X2**2 - 32*X1*X2 - 50*X1 - X2**3
                  - 15*X2**2 + 65*X2 - 25)
assert s.factor(common / (line*residual_cubic)) in (1, -1)
assert s.gcd(s.denom(chart_X3), line) == 1
assert s.gcd(s.denom(chart_X3), residual_cubic) == 1

# On the line component row 1 vanishes, so row 2 supplies the vertical
# direction. On every irreducible factor of the residual cubic, row 1 is
# generically nonzero and its q-direction numerator is nonzero.
line_b1 = s.factor(b1.subs({X0: 1, X1: X2, X3: chart_X3.subs(X1, X2)}))
line_c1 = s.factor(c1.subs({X0: 1, X1: X2, X3: chart_X3.subs(X1, X2)}))
line_b2 = s.factor(b2.subs({X0: 1, X1: X2, X3: chart_X3.subs(X1, X2)}))
line_c2 = s.factor(c2.subs({X0: 1, X1: X2, X3: chart_X3.subs(X1, X2)}))
assert line_b1 == 0 and line_c1 == 0
assert line_b2 != 0 and line_c2 != 0

def chart_numerator(expr):
    return s.together(expr.subs({X0: 1, X3: chart_X3})).as_numer_denom()[0]

line_direction_num = s.factor(chart_numerator(c2*B3 - b2*C3))
line_direction_remainder = s.factor(s.rem(line_direction_num, line, X1))
assert line_direction_remainder != 0
line_root_defect = 8*X2**3-29*X2**2+36*X2-16
assert s.expand(line_direction_remainder
                -54*(X2+5)**3*line_root_defect) == 0
assert s.factor(residual_cubic.subs(X1, X2)) == (X2-1)*(X2+5)**2
assert all(line_root_defect.subs(X2, value) != 0 for value in (0, 1, -5))
# On this line the fixed curve has X1=X2=X3=u, hence u^3=u^4=u.
# The cubic root-defect points avoid that intersection and the chart pole.
curve_parameter = s.Symbol("u")
assert s.gcd(curve_parameter**3-curve_parameter,
             curve_parameter**4-curve_parameter) == curve_parameter**2-curve_parameter
cubic_b1_num = chart_numerator(b1)
cubic_c1_num = chart_numerator(c1)
cubic_direction_num = chart_numerator(c1*B3 - b1*C3)
assert s.gcd(cubic_b1_num, residual_cubic) == 1
assert s.gcd(cubic_c1_num, residual_cubic) == 1
assert s.gcd(cubic_direction_num, residual_cubic) == 1

record = {
    "execution": {"command": "python3 research/computations/quintic_component_root_witness.py",
                  "python": sys.version.split()[0], "sympy": s.__version__},
    "parameters": params,
    "center_rank": pivot,
    "root_identity_remainder": str(root_identity_remainder),
    "module_identity_remainder": str(module_identity_remainder),
    "A4": str(s.factor(A4)),
    "B3": str(s.factor(B3)),
    "C3": str(s.factor(C3)),
    "residual_equations": [str(s.factor(rows[3])), str(s.factor(rows[4]))],
    "conductor_quadric": str(quadric),
    "chart_open": "X0=1 and 2*X1-X2+5 != 0",
    "chart_X3": str(chart_X3),
    "common_cubic_minor_factor": str(common),
    "line_row1_b_c": [str(line_b1), str(line_c1)],
    "line_row2_b_c": [str(line_b2), str(line_c2)],
    "line_q_direction_numerator_remainder": str(line_direction_remainder),
    "line_root_defect_polynomial": str(line_root_defect),
    "residual_factor_on_line": str(s.factor(residual_cubic.subs(X1, X2))),
    "line_curve_intersection_parameters": [0, 1],
    "line_root_defect_avoids_curve_and_chart_pole": True,
    "residual_cubic_row1_b_c_gcds": [
        str(s.gcd(cubic_b1_num, residual_cubic)),
        str(s.gcd(cubic_c1_num, residual_cubic)),
    ],
    "residual_cubic_q_direction_gcd": str(s.gcd(cubic_direction_num,
                                                 residual_cubic)),
    "scope_limits": [
        "No claim about additional conductor components in the excluded chart boundary.",
        "Residual cubic irreducibility was not checked.",
        "This one witness does not settle generic or component-selective descent in the family.",
    ],
}
print(json.dumps(record, indent=2))
