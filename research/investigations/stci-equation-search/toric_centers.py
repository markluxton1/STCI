"""Find candidate fibers of the remaining toric-quintic center incidence."""

import json
from pathlib import Path

import sympy as sp


source = Path(__file__).resolve().parents[2] / "computations/quintic_toric_finite_centers.json"
data = json.loads(source.read_text())
m, n = sp.symbols("m n")


def polynomial(expression):
    return sp.sympify(expression, locals={"m": m, "n": n})


weights = [polynomial(data["generic_W_coefficients_low_to_high"][str(i)]) for i in range(6)]
b, c, d = (polynomial(data["center"][key]) for key in ("b", "c", "d"))
curve = polynomial(data["finite_exception_factors"]["M"])
leading = weights[5]
negative_constant = 10 * c * leading + d * weights[4]
coefficients = []
for i, weight in enumerate(weights):
    previous = weights[i - 1] if i else 0
    following = weights[i + 1] if i < 5 else 0
    coefficient = leading * (
        (i - 6) * d * previous - 2 * c * i * weight + b * (i + 1) * following
    ) + negative_constant * weight
    coefficients.append(sp.expand(coefficient))

assert coefficients[-1] == 0
eliminants = [sp.resultant(curve, eq, n) for eq in coefficients[:-1]]
candidate = sp.Poly(sp.gcd_list(eliminants), m).sqf_part().monic()
print("Candidate m values:", sp.factor(candidate.as_expr()))

gate = (m**2 - 4*n) * (m**2 + 3*m - n + 3)
for name in ("d", "N", "U0", "V1", "V2"):
    gate *= polynomial(data["finite_exception_factors"][name])
for factor, _ in candidate.factor_list()[1]:
    if factor.degree() == 1:
        value = -factor.nth(0) / factor.nth(1)
        field = sp.QQ
    else:
        field = sp.QQ.alg_field_from_poly(factor, alias="alpha")
        value = field.ext

    def specialize(expr):
        # Reduce before substitution to keep powers of the field generator small.
        reduced = sp.rem(expr, factor.as_expr(), m)
        return sp.Poly(reduced.subs(m, value), n, domain=field)

    common = specialize(curve)
    for equation in coefficients[:-1]:
        common = common.gcd(specialize(equation))
    support = common.sqf_part()
    admissible = support.exquo(support.gcd(specialize(gate.expand())))
    assert admissible.degree() == 0, (factor, admissible)
    print(f"m-factor {factor.as_expr()}: common degree {common.degree()}, "
          f"admissible support {admissible.monic().as_expr()}", flush=True)
