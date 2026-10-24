#!/usr/bin/env python3
"""Exact local identities for the prescribed quartic conormal/lifting audit.

Only the Python standard library is used.  The checks are finite symbolic
identities over Q, Z, and F_2, using sparse Laurent polynomials.  They verify
the displayed chart expansions, first-normal transitions, conormal matrices,
and fourth-order lifts.  They do not establish global support exhaustion,
normal-bundle classification in general, the intrinsic filtered-module
comparison theorem, or an STCI existence/nonexistence statement.  Those
deductions require the accompanying mathematical arguments and hypotheses.
"""

from fractions import Fraction


NAMES = ("a", "u", "v", "b", "A", "B")
ZERO_EXPONENT = (0,) * len(NAMES)


class Laurent:
    """Small exact Laurent-polynomial implementation for this calculation."""

    def __init__(self, value=0):
        if isinstance(value, Laurent):
            self.terms = value.terms.copy()
        elif isinstance(value, dict):
            self.terms = {
                exponent: Fraction(coefficient)
                for exponent, coefficient in value.items()
                if coefficient
            }
        else:
            coefficient = Fraction(value)
            self.terms = {ZERO_EXPONENT: coefficient} if coefficient else {}

    def __add__(self, other):
        answer = self.terms.copy()
        for exponent, coefficient in Laurent(other).terms.items():
            answer[exponent] = answer.get(exponent, Fraction(0)) + coefficient
            if not answer[exponent]:
                del answer[exponent]
        return Laurent(answer)

    __radd__ = __add__

    def __neg__(self):
        return Laurent({exponent: -value for exponent, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-Laurent(other))

    def __rsub__(self, other):
        return Laurent(other) - self

    def __mul__(self, other):
        answer = {}
        for left_exponent, left_coefficient in self.terms.items():
            for right_exponent, right_coefficient in Laurent(other).terms.items():
                exponent = tuple(x + y for x, y in zip(left_exponent, right_exponent))
                answer[exponent] = (
                    answer.get(exponent, Fraction(0))
                    + left_coefficient * right_coefficient
                )
        return Laurent(answer)

    __rmul__ = __mul__

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("Only integer powers are supported")
        if power < 0:
            if len(self.terms) != 1:
                raise ValueError("A negative power requires a nonzero monomial")
            exponent, coefficient = next(iter(self.terms.items()))
            return Laurent({tuple(power * x for x in exponent): coefficient**power})
        answer = Laurent(1)
        factor = self
        while power:
            if power & 1:
                answer = answer * factor
            factor = factor * factor
            power //= 2
        return answer

    def reduce_mod(self, prime):
        answer = {}
        for exponent, coefficient in self.terms.items():
            denominator = coefficient.denominator % prime
            if not denominator:
                raise ValueError("A coefficient denominator is zero in the residue field")
            residue = (coefficient.numerator * pow(denominator, -1, prime)) % prime
            if residue:
                answer[exponent] = residue
        return Laurent(answer)

    def normal_part(self, variables, maximum_degree):
        indices = [NAMES.index(name) for name in variables]
        for exponent in self.terms:
            if any(exponent[index] < 0 for index in indices):
                raise ValueError("Normal variables must have nonnegative exponents")
        return Laurent({
            exponent: coefficient
            for exponent, coefficient in self.terms.items()
            if sum(exponent[index] for index in indices) <= maximum_degree
        })

    def __repr__(self):
        return repr(self.terms)


def variable(name):
    exponent = list(ZERO_EXPONENT)
    exponent[NAMES.index(name)] = 1
    return Laurent({tuple(exponent): 1})


CHECKS = 0


def equal(label, left, right=0, prime=None):
    global CHECKS
    difference = Laurent(left) - right
    if prime is not None:
        difference = difference.reduce_mod(prime)
    if difference.terms:
        raise AssertionError(f"{label}: nonzero difference {difference!r}")
    CHECKS += 1
    print(f"PASS {label}")


def equal_mod_normal_square(label, difference, normal_variables):
    equal(label, Laurent(difference).normal_part(normal_variables, 1))


def main():
    a, u, v, b, A, B = (variable(name) for name in NAMES)

    # Both affine coordinate substitutions, checked before reduction of terms.
    F0 = a**4 - (a**4 + v)
    G0 = (a**3 + u)**4 - (a**4 + v)**3
    expected_G0 = (
        u**4 + 4*a**3*u**3 + 6*a**6*u**2 + 4*a**9*u
        - 3*a**8*v - 3*a**4*v**2 - v**3
    )
    equal("exact F0 expansion over Z", F0, -v)
    equal("exact G0 expansion over Z", G0, expected_G0)

    Finfinity = (b**3 + B)**4 - (b**4 + A)**3
    Ginfinity = b**4 - (b**4 + A)
    expected_Finfinity = (
        B**4 + 4*b**3*B**3 + 6*b**6*B**2 + 4*b**9*B
        - 3*b**8*A - 3*b**4*A**2 - A**3
    )
    equal("exact G_infinity expansion over Z", Ginfinity, -A)
    equal("exact F_infinity expansion over Z", Finfinity, expected_Finfinity)

    # Exact rational overlap: d=a^4+v, b=(a^3+u)/d,
    # A=(d^3-(a^3+u)^4)/d^4, B=(a*d^2-(a^3+u)^3)/d^3.
    # Clear every denominator, including powers of a, before reducing mod I^2.
    d = a**4 + v
    A_numerator = d**3 - (a**3 + u)**4
    B_numerator = a*d**2 - (a**3 + u)**3
    equal_mod_normal_square(
        "base-coordinate overlap after clearing denominators",
        a**5*(a**3 + u) - d*(a**4 + a*u - v), ("u", "v"),
    )
    equal_mod_normal_square(
        "A overlap after clearing denominators",
        a**8*A_numerator - d**4*(3*v - 4*a*u), ("u", "v"),
    )
    equal_mod_normal_square(
        "B overlap after clearing denominators",
        a**7*B_numerator - d**3*(2*v - 3*a*u), ("u", "v"),
    )

    A1 = 3*a**-8*v - 4*a**-7*u
    B1 = 2*a**-7*v - 3*a**-6*u
    overlap_determinant = (3*a**-8)*(-3*a**-6) - (-4*a**-7)*(2*a**-7)
    equal("first-normal overlap determinant", overlap_determinant, -a**-14)

    # Equalities here are in the conormal bundle, over Q.
    w0 = v - Fraction(3, 2)*a*u
    equal("balanced characteristic-zero first frame", Fraction(1, 2)*B1, a**-7*w0)
    equal("balanced characteristic-zero second frame", 2*A1 - 3*a**-1*B1, a**-7*u)
    equal("characteristic-two diagonal A transition", A1, a**-8*v, prime=2)
    equal("characteristic-two diagonal B transition", B1, a**-6*u, prime=2)

    # Matrices have columns F,G and rows (V,U), respectively (A,B).
    phi0_determinant = (-Laurent(1))*(4*a**9) - (-3*a**8)*0
    phiinfinity_determinant = (-3*b**8)*0 - (-Laurent(1))*(4*b**9)
    equal("phi0 determinant", phi0_determinant, -4*a**9)
    equal("phi_infinity determinant", phiinfinity_determinant, 4*b**9)
    equal(
        "F conormal column agrees on overlap",
        (-3*a**-8)*A1 + (4*a**-9)*B1, a**-16*(-v),
    )
    equal(
        "G conormal column agrees on overlap",
        -A1, a**-16*(-3*a**8*v + 4*a**9*u),
    )
    equal(
        "conormal determinant patching",
        (4*a**-9)*overlap_determinant, a**-32*phi0_determinant,
    )

    # Corrections vanish on C and therefore preserve the class in J/IJ.
    correction0 = a**4*v + v**2
    correctioninfinity = b**4*A + A**2
    equal("zero-chart lift correction vanishes on C", correction0.normal_part(("u", "v"), 0))
    equal("infinity-chart lift correction vanishes on C", correctioninfinity.normal_part(("A", "B"), 0))
    equal(
        "characteristic-two zero-chart corrected lift is exactly u^4",
        (a**8 + correction0)*F0 + G0, u**4, prime=2,
    )
    equal(
        "characteristic-two infinity-chart corrected lift is exactly B^4",
        Finfinity + (b**8 + correctioninfinity)*Ginfinity, B**4, prime=2,
    )
    equal(
        "zero-chart first-order relation lies in kernel mod two",
        a**8*(-v) + (-3*a**8*v + 4*a**9*u), prime=2,
    )
    equal(
        "infinity-chart first-order relation lies in kernel mod two",
        (-3*b**8*A + 4*b**9*B) + b**8*(-A), prime=2,
    )

    # e_F,infinity=a^-16 e_F,0 and e_G,infinity=a^-16 e_G,0.
    # r_infinity=(1,b^8), r0=(a^8,1), with b=a^-1 along C.
    equal("kernel transition F coefficient", a**-16, a**-24*a**8)
    equal("kernel transition G coefficient", a**-16*a**-8, a**-24)
    equal("Q4 transition modulo lower generators", B1**4, a**-24*u**4, prime=2)

    # The actual nilpotent chart gluing, an additional exact check of the
    # nonlinear terms that are omitted by the first-normal transition.
    b_on_Z = a**-1 + a**-4*u
    B_on_Z = a**-3 - b_on_Z**3
    equal(
        "characteristic-two nonlinear B gluing",
        B_on_Z, a**-6*u + a**-9*u**2 + a**-12*u**3, prime=2,
    )

    print(f"ALL {CHECKS} QUARTIC CONORMAL/LIFTING IDENTITY CHECKS PASS")
    print("Boundary: finite exact symbolic identities; global conclusions require the report's arguments.")


if __name__ == "__main__":
    main()
