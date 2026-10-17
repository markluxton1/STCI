"""Exact sparse-polynomial counterchecks, using Python's standard library."""

import json

VARIABLES = ("r", "T", "a", "b", "g", "d")
ZERO_EXPONENT = (0,) * len(VARIABLES)


class P:
    def __init__(self, terms=None):
        if isinstance(terms, int):
            terms = {ZERO_EXPONENT: terms}
        self.terms = {e: c for e, c in (terms or {}).items() if c}

    @staticmethod
    def of(value):
        return value if isinstance(value, P) else P(value)

    def __add__(self, other):
        answer = dict(self.terms)
        for e, c in self.of(other).terms.items():
            answer[e] = answer.get(e, 0) + c
        return P(answer)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + -self.of(other)

    def __rsub__(self, other):
        return self.of(other) + -self

    def __mul__(self, other):
        answer = {}
        for e, c in self.terms.items():
            for f, coefficient in self.of(other).terms.items():
                exponent = tuple(x + y for x, y in zip(e, f))
                answer[exponent] = answer.get(exponent, 0) + c * coefficient
        return P(answer)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        answer = P(1)
        for _ in range(n):
            answer = answer * self
        return answer

    def coefficient_T(self, n):
        answer = {}
        for e, c in self.terms.items():
            if e[1] == n:
                exponent = e[:1] + (0,) + e[2:]
                answer[exponent] = c
        return P(answer)

    def same(self, other):
        return self.terms == self.of(other).terms


def variable(index):
    exponent = list(ZERO_EXPONENT)
    exponent[index] = 1
    return P({tuple(exponent): 1})


r, T, a, b, g, d = (variable(i) for i in range(len(VARIABLES)))
U0 = P(1)
U1 = r
U2 = r**2
U3 = r**3-r*T
U4 = r**4-(2*r**2+r)*T+T**2
X0 = U0+a*T
X1 = U1+b*T
X2 = U3+g*T
X3 = U4+d*T
K = a*U4-b*U3-U2-(1+g)*U1+d*U0+(1+a*d-b*g)*T
q_pull = X0*X3-X1*X2
U = g-r-3*b*r**2+2*a*r**3
V = d-r-2*r**2-4*b*r**3+3*a*r**4
W = a*r**4-b*r**3-r**2-(1+g)*r+d
A_pull = X0**2*X2-X1**3
quartic_pull = X0**3*X3-X1**4
P1 = a**2*r**3+2*a*(g-r)-3*r*b**2
P2 = a**2*(g-r)-b**3

checks = {
    "actual_quadric_factorization": q_pull.same(T*K),
    "cubic_first_normal_coefficient": A_pull.coefficient_T(1).same(U),
    "quartic_first_normal_coefficient": quartic_pull.coefficient_T(1).same(V),
    "quadric_factor_on_c": K.coefficient_T(0).same(W),
    "normal_residual_relation": W.same(V-r*U),
    "full_cubic_residual_factorization": A_pull.same(T*(U+T*P1+T**2*P2)),
    "normalized_quadric_residual_numerator":
        (X0**3*X3-X1**4-X1*(X0**2*X2-X1**3)).same(X0**2*q_pull),
}
assert all(checks.values()), checks
print(json.dumps({"status": "PASS", "exact_checks": len(checks),
                  "coefficient_ring": "Z[r,T,a,b,g,d]", "checks": checks}, indent=2))
