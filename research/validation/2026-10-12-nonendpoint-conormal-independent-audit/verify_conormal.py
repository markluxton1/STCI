"""Exact independent first-normal and moving-frame audit; standard library only."""

from fractions import Fraction
import json

NAMES = ("r", "T", "delta", "a", "b", "g", "d", "z", "U", "V", "k", "e")
ZERO = (0,) * len(NAMES)


class Polynomial:
    def __init__(self, value=None):
        if isinstance(value, (int, Fraction)):
            value = {ZERO: value}
        self.terms = {ex: Fraction(c) for ex, c in (value or {}).items() if c}

    @staticmethod
    def cast(value):
        return value if isinstance(value, Polynomial) else Polynomial(value)

    def __add__(self, other):
        answer = dict(self.terms)
        for ex, c in self.cast(other).terms.items():
            answer[ex] = answer.get(ex, 0) + c
        return Polynomial(answer)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({ex: -c for ex, c in self.terms.items()})

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        answer = {}
        for ex, c in self.terms.items():
            for ey, v in self.cast(other).terms.items():
                exponent = tuple(x + y for x, y in zip(ex, ey))
                answer[exponent] = answer.get(exponent, 0) + c*v
        return Polynomial(answer)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0:
            assert len(self.terms) == 1, "Only monomial inverses are used"
            exponent, coefficient = next(iter(self.terms.items()))
            return Polynomial({tuple(n*x for x in exponent): coefficient**n})
        answer = Polynomial(1)
        for _ in range(n):
            answer *= self
        return answer

    def same(self, other):
        return self.terms == self.cast(other).terms

    def coefficient(self, index, degree):
        answer = {}
        for ex, c in self.terms.items():
            if ex[index] == degree:
                exponent = list(ex)
                exponent[index] = 0
                answer[tuple(exponent)] = c
        return Polynomial(answer)

    def substitute_constants(self, substitutions):
        answer = {}
        for ex, c in self.terms.items():
            exponent = list(ex)
            coefficient = c
            for index, value in substitutions.items():
                coefficient *= Fraction(value)**ex[index]
                exponent[index] = 0
            exponent = tuple(exponent)
            answer[exponent] = answer.get(exponent, 0) + coefficient
        return Polynomial(answer)


def variable(index):
    exponent = [0]*len(NAMES)
    exponent[index] = 1
    return Polynomial({tuple(exponent): 1})


def jadd(left, right):
    return left[0]+right[0], left[1]+right[1]


def jscale(scalar, value):
    return scalar*value[0], scalar*value[1]


def jmul(left, right):
    return left[0]*right[0], left[0]*right[1]+left[1]*right[0]


def jinv(value):
    return value[0]**-1, -value[1]*value[0]**-2


def jdiv(left, right):
    return jmul(left, jinv(right))


def jpow(value, n):
    answer = Polynomial(1), Polynomial(0)
    for _ in range(n):
        answer = jmul(answer, value)
    return answer


r, T, delta, a, b, g, d, z, U, V, k, e = (variable(i) for i in range(len(NAMES)))
u0, u1, u2 = Polynomial(1), r, r**2
u3 = r**3-r*T
u4 = r**4-(2*r**2+r)*T+T**2
sections = [u4+a*T, u4-delta*u3+b*T,
            u4-3*delta*u3+3*delta**2*u2-delta**3*u1+g*T,
            u4-4*delta*u3+6*delta**2*u2-4*delta**3*u1+delta**4*u0+d*T]
on_c = [f.coefficient(1, 0) for f in sections]
normal = [f.coefficient(1, 1) for f in sections]
s = r-delta
P = ((g-3*b+2*a)*r**3 + (6*delta*(b-a)+delta**3-3*delta**2)*r**2
     + (delta**2*(6*a-3*b)+2*delta**3)*r - 2*a*delta**3)
J = ((2*d-3*g+b)*r**3 + (3*delta*(g-b)+5*delta**3-3*delta**2)*r**2
     + (3*b*delta**2+delta**3-delta**4)*r - b*delta**3)
actual_P = r**3*normal[2]-3*r*s**2*normal[1]+2*s**3*normal[0]
actual_J = 2*r**3*normal[3]-3*s*r**2*normal[2]+s**3*normal[1]

# Full moving target-coordinate jets, without freezing z=X1/X0.
z_jet = jdiv((on_c[1], normal[1]), (on_c[0], normal[0]))
y2_jet = jdiv((on_c[2], normal[2]), (on_c[0], normal[0]))
y3_jet = jdiv((on_c[3], normal[3]), (on_c[0], normal[0]))
V_jet = jadd(y2_jet, jscale(-1, jpow(z_jet, 3)))
U_jet = jadd(jadd(y3_jet, jscale(Fraction(-3,2), jmul(z_jet, y2_jet))),
             jscale(Fraction(1,2), jpow(z_jet, 4)))

# Actual opposite target chart, with its moving support coordinate w.
denominator = z**4, U+Fraction(3,2)*z*V
w_jet = jdiv((z**3, V), denominator)
a_prime = jadd(jdiv((z, Polynomial(0)), denominator), jscale(-1, jpow(w_jet, 3)))
b_prime = jadd(jdiv((Polynomial(1), Polynomial(0)), denominator), jscale(-1, jpow(w_jet, 4)))
raw_U = jadd(b_prime, jscale(Fraction(-3,2), jmul(w_jet, a_prime)))
raw_V = a_prime
op_U, op_V = jscale(Fraction(1,2), raw_V), jscale(2, raw_U)

defect = (5*k-1)*(7-e)-6-16*k
example = {2: 1, 3: 1, 4: 0, 5: 0, 6: 0}
Pe = P.substitute_constants(example)
Je = J.substitute_constants(example)
checks = {
    "actual_curve_restriction": all(f.same(h) for f,h in
        zip(on_c, [r**4, r**3*s, r*s**3, s**4])),
    "P_polynomial_identity": actual_P.same(P),
    "J_polynomial_identity": actual_J.same(J),
    "moving_V_first_normal": (r**7*V_jet[1]).same(P) and V_jet[0].same(0),
    "moving_U_first_normal": (2*r**7*U_jet[1]).same(J) and U_jet[0].same(0),
    "no_zero_pair_unit_witness":
        (delta*P.coefficient(0,1)+3*P.coefficient(0,0)-3*J.coefficient(0,0)).same(2*delta**4),
    "opposite_balanced_U_transition": op_U[0].same(0) and op_U[1].same(z**-7*U),
    "opposite_balanced_V_transition": op_V[0].same(0) and op_V[1].same(z**-7*V),
    "socle_defect_expansion": defect.same((19-5*e)*k+e-13),
    "k2_defect_degrees": all(defect.substitute_constants({10:2,11:i}).same(n)
                             for i,n in enumerate([25,16,7,-2])),
    "e3_unbounded_k_formula": defect.substitute_constants({11:3}).same(4*k-10),
    "algebraic_coprime_example": Je.same(2*r**2) and
        Pe.substitute_constants({0:0}).same(-2) and
        Pe.coefficient(0,3).same(2),
}
assert all(checks.values()), checks
print(json.dumps({"status":"PASS", "exact_checks":len(checks),
                  "coefficient_ring":"QQ[r,r^-1,T,delta,a,b,g,d,z,z^-1,U,V,k,e]",
                  "checks":checks,
                  "scope":"First-normal identities, actual opposite frame, zero-pair witness, and socle arithmetic; no carrier/parameter exhaustion"}, indent=2))
