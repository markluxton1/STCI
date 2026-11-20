"""Principal parts for a quadratic conductor on a transverse algebra.

Use an O-basis of the completed algebra at a root, where O=k[[u]] and
the chosen section is w=u**e. Supply polynomial jets for multiplication
by R-w**2 and for the actual ambient sections in that basis. The ground
field can contain exact symbolic parameters. The return value is a linear
map over that field. Its kernel is the space of sections regular after
multiplication by the chosen square root. Run this file for the embedded
ribbon calculation in the moving-cover proof.
"""

import sympy as sp


def conductor_jet_matrix(error, sections, u, root_order, nilpotence_index):
    """Return the negative Laurent coefficients, ordered by power then basis.

    The input nilpotence index is any proven bound L with error**L=0 in
    the full algebra. Only jets modulo u**max(0, e*(2*L-3)) enter. Columns of
    sections must use the same basis as error. Matrix rank therefore
    measures the actual evaluation image for those columns.
    """
    if error.rows != error.cols or sections.rows != error.rows:
        raise ValueError("The square operator and source columns need the same basis.")
    if root_order < 1 or nilpotence_index < 1:
        raise ValueError("Root order and nilpotence index must be positive.")
    pole_bound = max(0, root_order * (2 * nilpotence_index - 3))
    principal_parts = sp.zeros(pole_bound * error.rows, sections.cols)
    if pole_bound == 0:
        return principal_parts

    def truncate(entry):
        polynomial = sp.Poly(entry, u)
        return sum(coefficient * u**power for (power,), coefficient in polynomial.terms()
                   if power < pole_bound)

    error = error.applyfunc(truncate)
    images = sections.applyfunc(truncate)
    for j in range(1, nilpotence_index):
        images = (error * images).applyfunc(truncate)
        if images.is_zero_matrix:
            break
        pole = root_order * (2 * j - 1)
        scalar = sp.binomial(sp.Rational(1, 2), j)
        for row in range(images.rows):
            for col in range(images.cols):
                for (power,), coefficient in sp.Poly(images[row, col], u).terms():
                    if power < pole:
                        index = (pole_bound - pole + power) * images.rows + row
                        principal_parts[index, col] += scalar * coefficient
    return principal_parts


def osculating_quadric(a, b, c, d, p):
    return (a**2*p**8 - 8*a*b*p**7 + 28*b**2*p**6 - 56*a*c*p**5
            + (62*a*d + 8*b*c)*p**4 - 56*b*d*p**3 + 28*c**2*p**2
            - 8*c*d*p + d**2)


def check_moving_ribbon():
    p, u, y = sp.symbols("p u y")
    a, b, c, d = coordinates = sp.symbols("a b c d")
    quadric = osculating_quadric(*coordinates, p)
    point = {a: 1, b: p, c: p**3, d: p**4}
    assert all(sp.expand(quadric.diff(letter).subs(point)) == 0
               for letter in coordinates)
    assert sp.hessian(quadric.subs(p, 1), coordinates).rank() == 3

    # Work on the actual double divisor of the graph in its smooth quadric.
    x = p + u
    surface = {a: 1, b: x, c: x**3 + y, d: x * (x**3 + y)}
    residual = sp.Poly(quadric.subs(surface) - u**8, y)
    assert sp.expand(residual.nth(0)) == 0
    derivative = residual.nth(1)
    assert derivative.subs(u, 0) == 0
    assert derivative.diff(u).subs(u, 0) == 72 * p**4

    # In the basis (1,y), multiplication by y kills its second column.
    error = sp.Matrix([[0, 0], [derivative, 0]])
    linear_forms = sp.Matrix([[1, x, x**3, x**4], [0, 0, 1, x]])
    jets = conductor_jet_matrix(error, linear_forms, u, 4, 2)
    plane = sp.Matrix([-p**4, 2*p**3, -2*p, 1])
    assert jets.rank() == 3
    assert (jets * plane).applyfunc(sp.expand).is_zero_matrix

    # The whole local conductor uses all jets in the algebra, not just
    # the restrictions of the four ambient linear forms.
    local_columns = sp.Matrix.hstack(*(u**j * sp.eye(2) for j in range(4)))
    assert conductor_jet_matrix(error, local_columns, u, 4, 2).rank() == 3

    # A longer string checks cancellation between different binomial terms.
    jordan = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    all_jets = sp.Matrix.hstack(*(u**j * sp.eye(3) for j in range(3)))
    assert conductor_jet_matrix(jordan, all_jets, u, 1, 3).rank() == 3


if __name__ == "__main__":
    check_moving_ribbon()
    print("Verified the osculating cone, conductor length 3 and unique moving plane.")
