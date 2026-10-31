"""Independent sparse Fraction arithmetic in Q[p,k,delta,s]/(s*s-3).

Checks exported certificates by direct multiplication, without a Groebner
basis, saturation, symbolic library, or regeneration of certificate vectors.
"""
from fractions import Fraction
from pathlib import Path
import ast
import json
import re
import sys

ZERO_EXP = (0, 0, 0, 0)


class Poly:
    def __init__(self, terms=None):
        self.terms = {m: Fraction(c) for m, c in (terms or {}).items() if c}

    @staticmethod
    def constant(value):
        return Poly({ZERO_EXP: Fraction(value)})

    @staticmethod
    def variable(index):
        m = list(ZERO_EXP)
        m[index] = 1
        return Poly({tuple(m): Fraction(1)})

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly.constant(value)

    def __add__(self, other):
        other = self.coerce(other)
        out = dict(self.terms)
        for m, c in other.terms.items():
            out[m] = out.get(m, Fraction(0)) + c
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for a, ca in self.terms.items():
            for b, cb in other.terms.items():
                m = tuple(x+y for x, y in zip(a, b))
                power_s = m[3]
                m = m[:3] + (power_s % 2,)
                c = ca * cb * (3 ** (power_s // 2))
                out[m] = out.get(m, Fraction(0)) + c
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if set(other.terms) != {ZERO_EXP}:
            raise ValueError('Only nonzero rational scalar division is permitted')
        scalar = other.terms[ZERO_EXP]
        return Poly({m: c/scalar for m, c in self.terms.items()})

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError('Only nonnegative integer polynomial powers')
        result = Poly.constant(1)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def coefficient_p(self, exponent):
        return Poly({(0, m[1], m[2], m[3]): c
                     for m, c in self.terms.items() if m[0] == exponent})

    def substitute(self, index, value):
        value = self.coerce(value)
        result = Poly()
        for m, c in self.terms.items():
            reduced = list(m)
            power = reduced[index]
            reduced[index] = 0
            result += Poly({tuple(reduced): c}) * value**power
        return result


p, k, delta, s = (Poly.variable(i) for i in range(4))
one = Poly.constant(1)
checks = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    checks.append(label)


# Reconstruct the forced parameter, branch and normalization numerator.
B = k*delta**2
a = 2*k**2*delta**2-k*delta
P6 = p**2-3*p+3
Pc = p**2-6*p+6
E = (1+3*k)*p-3-6*k
L = (1+3*k)**2-9*delta*k**2*(1+2*k)
W = (p*P6*E**2
     -9*delta*(p-2)*(k*p**2-2*k*p-1)
     *(2*k**2*p**2-6*k**2*p+k*p**2+6*k**2-4*k*p+6*k+1))
check('forced a at p=-1/k (cleared by k)', -a+k*(B-delta)+k**2*delta**2 == 0)
check('E_s=-delta^2 E', delta**2*(3-p)+3*B*(2-p) == -delta**2*E)
check('branch collision polynomial', p*(3-p)-3*(2-p) == -Pc)

# r=rn/(3q), T=tn/(9p q^2 E), lambda=delta^4/(3p^2q^2).
# These checks clear all denominators and use actual sections, not jets.
q = 2-p
rn = delta*(3-p)
tn = delta**2*P6*Pc
check('F1 branch equation with exact common denominator',
      delta*rn**3*p*E
      -(delta*rn+3*q*B)*tn
      -9*delta**4*q*E == 0)
check('F2 branch equation with exact common denominator',
      3*delta**2*rn**2-3*delta**3*rn*q
      -3*delta**4*(3-p) == 0)
check('F3 branch equation with exact common denominator',
      3*delta**4*q-2*delta**3*rn+delta**4*p == 0)

# 81p^2(2-p)^4E^2 times X0-lambda, independently from U4+aT.
normalization_numerator = (
    rn**4*p**2*E**2
    -2*rn**2*tn*p*E
    -3*rn*tn*p*q*E
    +9*a*tn*p*q**2*E
    +tn**2
    -27*delta**4*q**2*E**2
)
check('actual denominator-cleared X0-lambda identity',
      normalization_numerator == 3*delta**3*Pc*q*W)
check('degree-five leading coefficient', W.coefficient_p(5) == L
      and max(m[0] for m in W.terms) == 5)
check('p=2 exclusion', W.substitute(0, 2) == 2)

# Explicit polynomial quotient verifies denominator-root control without
# polynomial ideal membership or a rational parameter localization.
qp = p-2
h2 = 18*p*qp**2*P6
h1 = 9*qp*(p*qp*(qp**2+2)-2*P6)-6*p*qp*(p-3)*P6
h0 = (p-3)*(18*qp-3*p*qp*(qp**2+2)+6*P6+2*p*(p-3)*P6)
exceptional_quotient = 3*p*(2-p)*P6*E+delta*(h2*k**2+h1*k+h0)
check('E exceptional-root polynomial quotient',
      3*(2-p)*W-delta*P6**2*Pc == E*exceptional_quotient)
check('P6 residual source equality', (3-p)**2-3*(2-p) == P6)

# Independent actual target-infinity calculations after forcing a.
def pinf(r):
    return -delta**2*r**2+(B**2-delta*B+a*delta**2)*r+a*delta*B


qinf = 3*delta**2*p**2+(3*delta*B-delta**3)*p-delta**2*B
check('Qinf factor including forbidden denominator root',
      qinf == 3*delta**2*(p+k*delta)*(p-delta/3))
check('forbidden denominator root is not Pinf root',
      pinf(-k*delta) == -k**3*delta**5)
check('infinity fiber forces L nonzero', pinf(delta/3) == -delta**4*L/9)
check('k=-1/3 degree boundary', L.substitute(1, Fraction(-1,3)) == -delta/3)

# Verify the actual exported vectors; parsing accepts only polynomial ASTs.
names = {'p': p, 'k': k, 'par_delta': delta, 's': s}


def polynomial_ast(node):
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return Poly.constant(node.value)
    if isinstance(node, ast.Name) and node.id in names:
        return names[node.id]
    if isinstance(node, ast.UnaryOp):
        val = polynomial_ast(node.operand)
        if isinstance(node.op, ast.USub):
            return -val
        if isinstance(node.op, ast.UAdd):
            return val
    if isinstance(node, ast.BinOp):
        left, right = polynomial_ast(node.left), polynomial_ast(node.right)
        if isinstance(node.op, ast.Add):
            return left+right
        if isinstance(node.op, ast.Sub):
            return left-right
        if isinstance(node.op, ast.Mult):
            return left*right
        if isinstance(node.op, ast.Div):
            return left/right
        if isinstance(node.op, ast.Pow):
            if set(right.terms) != {ZERO_EXP}:
                raise ValueError('Nonconstant exponent')
            exponent = right.terms[ZERO_EXP]
            if exponent.denominator != 1:
                raise ValueError('Noninteger exponent')
            return left**int(exponent)
    raise ValueError('Unsupported expression in certificate')


certificate_path = Path(sys.argv[1])
certificates = {}
for line in certificate_path.read_text().splitlines():
    match = re.fullmatch(r'CERTIFICATE \((\d+),(\d+),(\d+)\) matrix (.*)', line)
    if not match:
        raise ValueError('Unexpected certificate line')
    profile = tuple(int(match.group(i)) for i in (1,2,3))
    entries = re.findall(r'\{([^{}]*)\}', match.group(4))
    if len(entries) != 5 or profile in certificates:
        raise ValueError('Incorrect or duplicated certificate vector')
    vector = [polynomial_ast(ast.parse(re.sub(r'\bdel\b', 'par_delta', x.strip()).replace('^','**'), mode='eval').body)
              for x in entries]
    check('polynomial certificate has no p coefficient '+str(profile),
          all(all(m[0] == 0 for m in b.terms) for b in vector))
    certificates[profile] = vector

expected = {(i,j,5-i-j) for i in range(6) for j in range(6-i)}
check('all 21 multiplicity profiles including every p=0 order',
      set(certificates) == expected and len(expected) == 21)
coeffs = [W.coefficient_p(t) for t in range(6)]
check('profile leading equation is automatic', coeffs[5] == L)
verified_profiles = []
for profile in sorted(expected):
    i, j, h = profile
    monic = p**i*(p-(3+s))**j*(p-(3-s))**h
    check('monic degree-five profile '+str(profile),
          monic.coefficient_p(5) == one)
    system = [coeffs[t]-L*monic.coefficient_p(t) for t in range(5)]
    product = sum((f*b for f,b in zip(system, certificates[profile])), Poly())
    check('direct exported Bezout product equals one '+str(profile), product == one)
    verified_profiles.append(profile)

print(json.dumps({
    'status':'PASS',
    'arithmetic':'sparse rational polynomial arithmetic with s^2=3',
    'certificate_inputs':str(certificate_path),
    'checks_passed':len(checks),
    'structural_checks':15,
    'direct_exported_certificate_products':21,
    'all_profiles':verified_profiles,
    'scope':'G=J=0 coefficient profiles and denominator-cleared actual fiber identities; geometric audit supplied separately.',
    'check_labels':checks
}, indent=2))
