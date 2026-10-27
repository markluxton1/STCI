#!/usr/bin/env python3
"""Exact finite identities for one (4,4) triple-C residual example.

Standard library only. Arithmetic is in Q[r]/(12*r^2+4*r+3).
This checks the new residual factorization, its two parametrized branches,
endpoint contact lengths, and the explicit first-normal coefficient pencil.
It neither reconstructs inherited direction classifications nor proves a
global cycle decomposition from finite identities alone; see the README.
"""

from dataclasses import dataclass
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path


@dataclass(frozen=True)
class K:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, "a", Fraction(self.a))
        object.__setattr__(self, "b", Fraction(self.b))

    @staticmethod
    def of(value):
        return value if isinstance(value, K) else K(value)

    def __add__(self, other):
        other = K.of(other)
        return K(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, other):
        return self + -K.of(other)

    def __rsub__(self, other):
        return K.of(other) + -self

    def __mul__(self, other):
        other = K.of(other)
        # r^2 = -r/3 - 1/4.
        return K(self.a * other.a - self.b * other.b / 4,
                 self.a * other.b + self.b * other.a - self.b * other.b / 3)

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a**2 - self.a * self.b / 3 + self.b**2 / 4
        if not norm:
            raise ZeroDivisionError("zero in the quadratic field")
        return K((self.a - self.b / 3) / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * K.of(other).inverse()

    def __rtruediv__(self, other):
        return K.of(other) * self.inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = K(1)
        for _ in range(exponent):
            result *= self
        return result

    def __bool__(self):
        return bool(self.a or self.b)

    def record(self):
        return {"constant": str(self.a), "r_coefficient": str(self.b)}


def trim(poly):
    poly = [K.of(x) for x in poly]
    while poly and not poly[-1]:
        poly.pop()
    return poly


def add(poly, other):
    out = [K()] * max(len(poly), len(other))
    for i, value in enumerate(poly):
        out[i] += value
    for i, value in enumerate(other):
        out[i] += value
    return trim(out)


def multiply(poly, other):
    if not poly or not other:
        return []
    out = [K()] * (len(poly) + len(other) - 1)
    for i, left in enumerate(poly):
        for j, right in enumerate(other):
            out[i + j] += left * right
    return trim(out)


def power(poly, exponent):
    out = [K(1)]
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


def divide(poly, other):
    remainder = trim(poly)
    other = trim(other)
    if not other:
        raise ZeroDivisionError("zero polynomial")
    quotient = [K()] * max(0, len(remainder) - len(other) + 1)
    while remainder and len(remainder) >= len(other):
        shift = len(remainder) - len(other)
        coefficient = remainder[-1] / other[-1]
        quotient[shift] += coefficient
        subtraction = [K()] * shift + [-coefficient * x for x in other]
        remainder = add(remainder, subtraction)
    return trim(quotient), remainder


def gcd(poly, other):
    poly, other = trim(poly), trim(other)
    while other:
        _, remainder = divide(poly, other)
        poly, other = other, remainder
    return [value / poly[-1] for value in poly] if poly else []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    root = Path(__file__).resolve().parents[2]
    parser.add_argument("--output", type=Path,
                        default=root / "research/validation/44-triple-residual-2026-10-26/checks.json")
    args = parser.parse_args()
    checks = []

    def check(name, condition, detail):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "status": "PASS", "detail": detail})

    r = K(0, 1)
    a, b = r + Fraction(3, 2), r + Fraction(1, 2)
    c, t = r - Fraction(7, 6), Fraction(1, 6) - r
    check("field_relation", 12 * r**2 + 4 * r + 3 == K(),
          "Arithmetic reduces modulo 12r^2+4r+3.")

    # On x0=1, z=x1 and z!=0, p=x2/z^3 and q=x3/z^4.
    # R0=0 gives q=ap-b; R1/z^12=q^3+c*p*q^2+t*p^4.
    qpoly = [-b, a]
    quartic = add(add(power(qpoly, 3), multiply([K(), c], power(qpoly, 2))),
                  [K(), K(), K(), K(), t])
    factored = multiply(power([K(-1), K(1)], 3), [b**3, t])
    check("residual_factorization", quartic == factored,
          "R1|R0=(p-1)^3*((1/6-r)*p+(r+1/2)^3), after torus normalization.")

    kappa = (2 * r - 3) / (18 * r - 3)
    eta = -kappa / 3
    check("simple_residual_root", t * kappa + b**3 == K(),
          "The residual linear factor has root kappa.")
    check("kappa_minimal_polynomial", 27 * kappa**2 - 14 * kappa + 3 == K(),
          "27*kappa^2-14*kappa+3=0.")
    check("residual_x3_coefficient", a * kappa - b == eta,
          "The residual q coefficient is eta=-kappa/3.")
    check("distinct_nonzero_roots", all((t, b, kappa, eta, kappa - 1, eta - 1)),
          "Both parametrized quartics are diagonal embeddings; the residual root is simple and distinct from 1.")
    check("original_parametrization", 1 - a + b == K() and 1 + c + t == K(),
          "Substitution [s^4:s^3t:st^3:t^4] annihilates R0 and R1.")
    check("residual_parametrization",
          eta - a * kappa + b == K()
          and eta**3 + c * kappa * eta**2 + t * kappa**4 == K(),
          "Substitution [s^4:s^3t:kappa*st^3:eta*t^4] annihilates both quartics.")
    check("residual_quadric", 3 * eta + kappa == K(),
          "The residual quartic is on 3*x0*x3+x1*x2=0.")

    # In the x0=1 chart both branches use z=x1; their normal differences
    # are (kappa-1)*z^3 and (eta-1)*z^4, hence quotient length 3.
    p_orders = [3 if kappa - 1 else None, 4 if eta - 1 else None]
    # In x3=1 use w=x2 on both branches. Residual x1 and x0 are
    # eta^2/kappa^3*w^3 and eta^3/kappa^4*w^4 respectively.
    infinity_cubic = eta**2 / kappa**3
    infinity_quartic = eta**3 / kappa**4
    q_orders = [3 if infinity_cubic - 1 else None,
                4 if infinity_quartic - 1 else None]
    check("endpoint_contact_lengths", p_orders == [3, 4] and q_orders == [3, 4],
          "At each endpoint the branch-intersection ideal is generated by nonzero multiples of parameter^3 and parameter^4; length is 3.")
    check("no_other_curve_intersections", bool(kappa - 1) and bool(eta),
          "On x0!=0 equality of the two parametrizations forces z=0; at x0=0 each has only the opposite endpoint.")

    # Independently expand explicit R1 at x2=z^3+y, x3=z^4+m+a*z*y.
    # R0=m exactly. The displayed scalar coefficients carry z exponents
    # 12,9,6,3,0 for the pure-y powers 0,...,4.
    pure_y = [1 + c + t,
              3 * a + c * (1 + 2 * a) + 4 * t,
              3 * a**2 + c * (a**2 + 2 * a) + 6 * t,
              a**3 + c * a**2 + 4 * t,
              t]
    h = 3 + 2 * c
    check("explicit_first_normal_symbols",
          pure_y[0] == K() and pure_y[1] == K()
          and h == 2 * r + Fraction(2, 3) and bool(h),
          "R0=m, while the R1 first symbol is (2r+2/3)*z^8*m, with no linear y term.")
    check("explicit_triple_contact", pure_y[2] == K() and pure_y[3] == -8 * r / 9 and bool(pure_y[3]),
          "After setting R0=m=0, R1 has first nonzero y term (-8r/9)*z^3*y^3 at the generic point.")
    # Globally on C, grad(R0)=s^8*v and grad(R1)=h*t^8*v, where
    # v=(-2r*t^4,(-a+4b)*s*t^3,-a*s^3*t,s^4).
    # The vector v never vanishes: its last entry handles s!=0, and
    # its first entry handles s=0. This checks the projective endpoints
    # as well as the finite-chart first-symbol coefficient.
    check("global_gradient_pencil",
          h * (-2 * r) == K(1)
          and h * (-a + 4 * b) == c
          and h * (-a) == c + 4 * t,
          "On C, grad(R0)=s^8*v and grad(R1)=(2r+2/3)*t^8*v with nowhere-zero degree-four vector v; their common singular locus on C is empty.")
    hpoly = [K(1)] + [K()] * 7 + [h]
    derivative = [K()] * 7 + [8 * h]
    check("eight_simple_first_symbol_zeros", len(hpoly) - 1 == 8 and gcd(hpoly, derivative) == [K(1)],
          "For the representative R0+R1, 1+(2r+2/3)*z^8 has degree 8 and is coprime to its derivative. The same argument works for alpha*beta!=0.")

    payload = {
        "status": "PASS",
        "scope": "Finite exact identities for the displayed explicit quartic pair; not an exhaustive classification or a standalone global proof.",
        "field": "Q[r]/(12*r^2+4*r+3)",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameters": {"kappa": kappa.record(), "eta": eta.record(),
                       "h": h.record(), "infinity_cubic": infinity_cubic.record(),
                       "infinity_quartic": infinity_quartic.record()},
        "quartic_coefficients_low_to_high": [value.record() for value in quartic],
        "endpoint_intersection_lengths": {"p": 3, "q": 3},
        "checks": checks,
        "proof_obligations_outside_this_script": [
            "R0 is irreducible by the primitive linear-polynomial argument; R1 is not proportional, so the pair is proper.",
            "Complete-intersection purity and degree 16 turn the dense-chart components of degrees 12 and 4 into the full global cycle.",
            "Nonzero diagonal scalings preserve the smooth embedded rational quartic.",
            "The interpretation of first-symbol roots as surface singularities uses the standard differential criterion; an A2 classification is not certified here.",
            "No classification of all multiplicity-three pairs or inherited primitive directions is performed."
        ]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(checks)} exact finite checks")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
