"""Derive the new moving-relation quadratic operator, using exact fractions.

This is a new calculation from accepted embedded chart identities, rather
than a rerun of the accepted normal-bundle or line-obstruction verification.
It uses only Python's standard library and truncates every polynomial at
normal order two. Each monomial is indexed by (u power, v power, z power).
"""

from fractions import Fraction
import json


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Fraction(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def scale(polynomial, coefficient):
    return {exponent: coefficient * value
            for exponent, value in polynomial.items() if coefficient * value}


def multiply(left, right):
    result = {}
    for (iu, iv, iz), coefficient in left.items():
        for (ju, jv, jz), value in right.items():
            exponent = (iu + ju, iv + jv, iz + jz)
            if exponent[0] + exponent[1] <= 2:
                result[exponent] = result.get(exponent, Fraction(0)) + coefficient * value
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def power(polynomial, exponent):
    result = {(0, 0, 0): Fraction(1)}
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def z_power(exponent):
    return {(0, 0, exponent): Fraction(1)}


def normal_layer(polynomial, degree):
    return {exponent: coefficient for exponent, coefficient in polynomial.items()
            if exponent[0] + exponent[1] == degree}


def encoded(polynomial):
    return [{"u": u, "v": v, "z": z, "coefficient": str(value)}
            for (u, v, z), value in sorted(polynomial.items())]


one = z_power(0)
u = {(1, 0, 0): Fraction(1)}
v = {(0, 1, 0): Fraction(1)}
b = add(u, scale(multiply(z_power(1), v), Fraction(3, 2)))
denominator_correction = multiply(z_power(-4), b)
inverse = multiply(z_power(-4), add(one, scale(denominator_correction, -1),
                                    power(denominator_correction, 2)))
W = multiply(add(z_power(3), v), inverse)
a_prime = add(multiply(z_power(1), inverse), scale(power(W, 3), -1))
b_prime = add(inverse, scale(power(W, 4), -1))
u_prime = scale(a_prime, Fraction(1, 2))
v_prime = add(scale(multiply(W, a_prime), -3), scale(b_prime, 2))

result = {
    "status": "new exact quadratic moving-relation calculation",
    "base_displacement_epsilon": encoded(normal_layer(W, 1)),
    "Du": encoded(normal_layer(multiply(z_power(7), u_prime), 2)),
    "Dv": encoded(normal_layer(multiply(z_power(7), v_prime), 2)),
    "base_derivative_coefficient_mod_fV": encoded(
        scale(multiply(z_power(2), normal_layer(W, 1)), -1)),
    "degree_one_relation": "f(z;u,v)=A(u,v)+z B(u,v)",
    "operator": "Du*d_u(f)+Dv*d_v(f)+(-z^2*epsilon)*B, modulo f*V",
    "limitations": [
        "The quotient f*V moves with z; it is not a constant vector-space quotient.",
        "Vanishing of this one-step obstruction is necessary, not sufficient.",
        "No degree-one moving-relation exclusion is claimed.",
    ],
}
print(json.dumps(result, indent=2))
