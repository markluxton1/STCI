"""Independent exact fourth-blowup coefficient audit; standard library only."""

import json

VARIABLES = ("x", "r", "g", "d")
ZERO = (0,) * len(VARIABLES)


class Polynomial:
    def __init__(self, value=None):
        if isinstance(value, int):
            value = {ZERO: value}
        self.terms = {e: c for e, c in (value or {}).items() if c}

    @staticmethod
    def cast(value):
        return value if isinstance(value, Polynomial) else Polynomial(value)

    def __add__(self, other):
        answer = dict(self.terms)
        for e, c in self.cast(other).terms.items():
            answer[e] = answer.get(e, 0)+c
        return Polynomial(answer)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        answer = {}
        for e, c in self.terms.items():
            for f, z in self.cast(other).terms.items():
                exponent = tuple(a+b for a, b in zip(e, f))
                answer[exponent] = answer.get(exponent, 0)+c*z
        return Polynomial(answer)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        answer = Polynomial(1)
        for _ in range(n):
            answer *= self
        return answer

    def same(self, other):
        return self.terms == self.cast(other).terms

    def coefficient_x(self, n):
        return Polynomial({(0,)+e[1:]: c for e, c in self.terms.items() if e[0] == n})

    def derivative(self, index):
        answer = {}
        for e, c in self.terms.items():
            if e[index]:
                exponent = list(e)
                exponent[index] -= 1
                answer[tuple(exponent)] = c*e[index]
        return Polynomial(answer)


def variable(index):
    exponent = [0]*len(VARIABLES)
    exponent[index] = 1
    return Polynomial({tuple(exponent): 1})


def quotient_jet(numerator, denominator):
    """Exact coefficients modulo x^2, for the denominators used here."""
    n0, n1 = numerator.coefficient_x(0), numerator.coefficient_x(1)
    d0, d1 = denominator.coefficient_x(0), denominator.coefficient_x(1)
    assert d0.same(1) or d0.same(-1)
    inverse_constant = d0
    return n0*inverse_constant, n1*inverse_constant-n0*d1


x, r, g, d = (variable(i) for i in range(len(VARIABLES)))
w = 1+x*r
z = 1+x*w
Z0, Z1, Z2 = r, w, x**2*w**2
Z3, Z4, Z5 = x*w, x**3*w**2, x**5*w**3
h = Z2+Z3
U0, U1, U3, U4 = Z5, Z4, -Z1, Z0-Z1
X0, X1, X2, X3 = U0, U1, U3+g*h, U4+d*h
Q = w**2*z**5
q0, q1 = quotient_jet(Q, X2**4)
y00, y01 = quotient_jet(X0, X2)
y10, y11 = quotient_jet(X1, X2)
y30, y31 = quotient_jet(X3, X2)
kappa = r**2-g*r+g-d
first_normal = 5-2*r+4*g
checks = {
    "actual_h_section": h.same(x*w*z),
    "actual_Q_cancellation": (Q*U0).same(h**5),
    "projection_X2_factor": X2.same(w*(-1+g*x*z)),
    "q_restriction": q0.same(1),
    "q_transverse_derivative": q1.same(first_normal),
    "q_tangent_derivative": q0.derivative(1).same(0),
    "target_X0_zero_first_jet": y00.same(0) and y01.same(0),
    "target_X1_zero_first_jet": y10.same(0) and y11.same(0),
    "target_X3_restriction": y30.same(1-r),
    "target_X3_transverse_derivative": y31.same(kappa),
    "target_X3_tangent_derivative": y30.derivative(1).same(-1),
    "transverse_kernel_kills_target":
        all((normal+kappa*constant.derivative(1)).same(0)
            for constant, normal in [(y00,y01),(y10,y11),(y30,y31)]),
}
assert all(checks.values()), checks
print(json.dumps({"status": "PASS", "exact_checks": len(checks),
                  "coefficient_ring": "Z[x,r,g,d]",
                  "scope": "Fourth-blowup identities and first jets; all-power consequence is proved separately",
                  "checks": checks}, indent=2))
