#!/usr/bin/env python3
"""Replay finite quartic ancestor direction exclusions over exact fields.

Run with SymPy 1.14 and Macaulay2 1.26 on PATH. The four source files in
research/computations are the existing audited Ext and multiplication data.
Macaulay2 receives the exact chart and matrix computations in temporary scripts.
"""

import json
from math import comb
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

import sympy as sp
from sympy.polys.matrices import DomainMatrix


DATA = Path(__file__).resolve().parents[2] / "computations"
x, y, z, w, t = sp.symbols("x y z w t")
a, b, c, d, e, ell = sp.symbols("a b c d e ell")


def moments(numerator):
    """Quadratic and cubic residues in the balanced affine frame."""
    polynomial = sp.Poly(numerator.replace("^", "**"), x, y, z, w)
    # Substitute x=1, y=t, z=t^3+V, w=t^4+tV+q. Keys are q, V, t exponents.
    terms = {}
    for (_, y_power, z_power, w_power), value in polynomial.terms():
        weight = y_power + 3 * z_power + 4 * w_power
        for q_power in range(min(4, w_power + 1)):
            for from_z in range(min(4 - q_power, z_power) + 1):
                for from_w in range(min(4 - q_power - from_z, w_power - q_power) + 1):
                    v_power = from_z + from_w
                    key = q_power, v_power, weight - 4 * q_power - 3 * v_power
                    coefficient = comb(z_power, from_z) * comb(w_power, q_power)
                    coefficient *= comb(w_power - q_power, from_w)
                    terms[key] = terms.get(key, 0) + value * coefficient

    # U=q-tV/2 and B=V(t^3+V)-t^2 q. Extract q^-1 V^-1.
    residues = {}
    for degree in (2, 3):
        for i in range(degree + 1):
            values = {}
            for (q_power, v_power, weight), value in terms.items():
                for from_u in range(i + 1):
                    k = 3 - q_power - from_u
                    n = 6 - q_power - v_power - degree
                    if k < 0 or n < 0:
                        continue
                    exponent = weight + i - from_u - 12 - k - 3 * n
                    coefficient = comb(i, from_u) * sp.Rational(-1, 2)**(i - from_u)
                    coefficient *= comb(k + 3, 3) * (-1)**n * comb(k + n + 3, n)
                    values[exponent] = values.get(exponent, 0) + value * coefficient
            assert all(j >= 0 or not value for j, value in values.items())
            residues[i, degree - i] = sp.Poly(
                sum(value * t**j for j, value in values.items() if value), t
            )
    return residues


def resultant(p, r):
    """Degree-two binary resultant, including specialized leading zeros."""
    p0, p1, p2 = (sp.Poly(p, t).nth(i) for i in range(3))
    r0, r1, r2 = (sp.Poly(r, t).nth(i) for i in range(3))
    return (p2*r0 - p0*r2)**2 - (p2*r1 - p1*r2)*(p1*r0 - p0*r1)


def chart_check(name, parameters, equations, invert, expected):
    """Compare saturated ideals by exact ideal equality over QQ."""
    variables = ",".join(map(str, parameters))
    inputs = ",".join(str(sp.expand(f)).replace("**", "^") for f in equations)
    output = ",".join("sub(" + str(sp.expand(f)).replace("**", "^") + ",R)"
                      for f in expected)
    denominator = str(sp.expand(invert)).replace("**", "^")
    return (
        f"R=QQ[{variables}, MonomialOrder=>GRevLex];\n"
        f"assert(saturate(ideal({inputs}),{denominator},Strategy=>Iterate)"
        f"==ideal({output}));\n"
        f'print "PASS: {name} over QQ";\n'
    )


def run_m2(source):
    with TemporaryDirectory(prefix="stci-quartic-ancestor-") as scratch:
        script = Path(scratch) / "verify.m2"
        script.write_text(source)
        subprocess.run(["M2", "--script", str(script)], check=True)


def first_symbol_source(p, r):
    """The complete actual quartic kernel of evaluation along (p,r)."""
    lines = (DATA / "localcoh-incidence-bases.txt").read_text().splitlines()[32:]
    chart = {x: 1, y: t, z: t**3, w: t**4}
    evaluations = []
    for line in lines:
        form = sp.sympify(line.replace("^", "**"), locals={"x": x, "y": y, "z": z, "w": w})
        first_u = form.diff(w).subs(chart)
        first_v = form.diff(z).subs(chart) + 3*t*first_u/2
        evaluations.append(sp.Poly(p*first_u + r*first_v, t))
    degree = max(polynomial.degree() for polynomial in evaluations)
    matrix = sp.Matrix([[polynomial.nth(j) for polynomial in evaluations]
                        for j in range(degree + 1)])
    return sp.Matrix.hstack(*matrix.nullspace())


def verify_constant(lift, middle, tensor):
    """Exclude the mixed constant orbit by exact jets and a modular rank bound."""
    parameters = sp.symbols("ca cb cc cd ce")
    ca, cb, cc, cd, ce = parameters
    coefficients = [ca, cb, cc, (5*ca - 6*cb - 4*cc)/8,
                    -cc/4 - 12*cd + 40*ce, cc/8, cd, ce]
    h = sum(value*t**i for i, value in enumerate(coefficients))
    alpha, obstruction, quadratic = lift(sp.Integer(1), sp.Integer(1), h)
    assert not any(map(sp.expand, obstruction))
    contact = middle(sp.Integer(1), sp.Integer(1), quadratic)
    lower = (-85*ca + 110*cb - 736*cc + 3520*cd - 10880*ce)/672
    assert sp.expand(contact.as_expr() - 7*(ell - lower)) == 0
    alpha = alpha.subs(ell, lower).applyfunc(sp.expand)
    assert sp.Matrix.hstack(*(alpha.diff(v) for v in parameters)).rank() == 5
    source = first_symbol_source(1, 1)
    assert source.shape == (18, 8)
    multiplication = sum(
        (value*tensor[:, 18*j:18*(j + 1)] for j, value in enumerate(alpha)),
        sp.zeros(74, 18),
    )
    full = (multiplication*source).applyfunc(sp.expand)
    projected = full[:72, :]
    coefficient_rows = sp.Matrix.hstack(*(projected.diff(v) for v in parameters))
    selected_rows = list(coefficient_rows.T.rref()[1])
    assert len(selected_rows) == 11
    compact = projected[selected_rows, :]
    assert sp.Matrix.hstack(*(compact.diff(v) for v in parameters)).rank() == 11
    point = dict(zip(parameters, (128, 64, 0, 2, 1), strict=True))
    at_point = full.subs(point)
    assert at_point.rank() == 4
    assert all(at_point.row_join(tensor[:, j]).rank() == 5 for j in (540, 541))
    expression = str(compact.tolist()).replace("[", "{").replace("]", "}").replace("**", "^")
    run_m2(
        "R=QQ[ca,cb,cc,cd,ce,MonomialOrder=>GRevLex];\n"
        f"mt=matrix{expression};\n"
        "pt=map(QQ,R,{128_QQ,64_QQ,0_QQ,2_QQ,1_QQ});\n"
        "base=pt mt; assert(rank base==4);\n"
        "constantLeft=transpose gens kernel transpose base; constantRight=gens kernel base;\n"
        "assert(numRows constantLeft==7 and numColumns constantRight==4);\n"
        "constantNormal=(sub(constantLeft,R))*"
        "((map(R,R,{ca,cb,cc,cd,0_R})) mt)*(sub(constantRight,R));\n"
        "jets=minors(3,constantNormal,Strategy=>Dynamic);\n"
        "(jm,jc)=coefficients gens jets; assert(rank sub(jc,QQ)==14);\n"
        "R1=(ZZ/32003)[v_0..v_4,MonomialOrder=>GRevLex];\n"
        "mt1=(map(R1,R,gens R1)) mt;\n"
        "minors1=minors(7,mt1,Strategy=>Dynamic);\n"
        "(mm,mc)=coefficients gens minors1;\n"
        "assert(rank sub(mc,ZZ/32003)==309);\n"
        'print "PASS: constant orbit cubic-jet rank 14 and degree-seven minor rank 309";\n'
    )
    print("PASS: complete mixed constant orbit and both target exclusions")


def verify_linear_boundary(lift, middle, tensor):
    """All degree-one directions with a component zero at a toric endpoint."""
    parameter_a, parameter_c = sp.symbols("la lc")
    hs = sp.symbols("h0:5")
    h = sum(coefficient*t**i for i, coefficient in enumerate(hs))
    coordinates = (*hs, ell)

    def maps(p, r):
        alpha, top, quadratic = lift(p, r, h)
        contact = middle(p, r, quadratic)
        assert contact.degree() <= 5
        equations = top + [contact.nth(i) for i in range(6)]
        return (sp.linear_eq_to_matrix(alpha, coordinates)[0],
                sp.linear_eq_to_matrix(equations, coordinates)[0])

    factors_a = (
        4*parameter_a**2 + 2*parameter_a + 1,
        4*parameter_a**2 + 4*parameter_a + 5,
        20*parameter_a**2 + 4*parameter_a + 1,
        4*parameter_a**3 - 8*parameter_a**2 - 3*parameter_a - 1,
        16*parameter_a**3 + 12*parameter_a**2 + 8*parameter_a - 1,
    )
    factor_c = (3*parameter_c**6 - 38*parameter_c**5 + 183*parameter_c**4
                - 360*parameter_c**3 + 4*parameter_c**2 + 528*parameter_c - 640)
    determinant_a = 7*parameter_a**3*(2*parameter_a - 1)**3*sp.prod(factors_a)/18
    sparse = [(row, column//18, column%18, value)
              for (row, column), value in tensor.todok().items() if column < 540]
    targets = tensor[:, 540:]
    for p, r, parameter, factors, expected in (
        (parameter_a*t, 1, parameter_a, factors_a, determinant_a),
        (parameter_a*t, 1 + t, parameter_a, factors_a, determinant_a),
        (1 + t, parameter_c*t, parameter_c, (factor_c,), 896*parameter_c**3*factor_c/9),
    ):
        alpha_map, incidence = maps(p, r)
        assert sp.expand(incidence[:6, :].det(method="domain-ge") - expected) == 0
        for factor in factors:
            modulus = sp.Poly(factor, parameter, domain=sp.QQ)
            assert modulus.is_irreducible
            field = sp.QQ.algebraic_field(sp.CRootOf(modulus, 0))
            assert list(field.mod.to_list()) == modulus.rep.to_list()

            def specialize(matrix):
                entries = [[field.new(sp.Poly(entry, parameter, domain=sp.QQ)
                                      .rem(modulus).rep.to_list())
                            for entry in row] for row in matrix.tolist()]
                return DomainMatrix(entries, matrix.shape, field)

            solutions = specialize(incidence).nullspace().transpose()
            assert solutions.shape == (6, 1)
            alpha, = (specialize(alpha_map)*solutions).transpose().to_list()
            values = [[field.zero for _ in range(18)] for _ in range(74)]
            for row, ancestor, quartic, value in sparse:
                values[row][quartic] += field.convert(value)*alpha[ancestor]
            multiplication = DomainMatrix(values, (74, 18), field)
            target = DomainMatrix.from_Matrix(targets).convert_to(field)
            rank = multiplication.rank()
            assert all(multiplication.hstack(target.extract(range(74), [j])).rank() == rank + 1
                       for j in range(2))

    z0, z1, z2 = parameters = sp.symbols("z0:3")
    checks = ["R=QQ[z0,z1,z2];\n"]
    for p, r, point, span in (
        (t/2, 1, (0, 0, 1), (z0, z1)),
        (t/2, 1 + t, (sp.Rational(7, 22), -sp.Rational(7, 44), 1),
         (22*z0 - 7*z2, 44*z1 + 7*z2)),
        (1, t, (-2, 0, 1), (z0 + 2*z2, z1)),
    ):
        alpha_map, incidence = maps(p, r)
        lifts = incidence.nullspace()
        assert len(lifts) == 3
        alpha = alpha_map*sp.Matrix.hstack(*lifts)*sp.Matrix(parameters)
        source = first_symbol_source(p, r)
        assert source.shape == (18, 7)
        multiplication = sum(
            (value*tensor[:, 18*j:18*(j + 1)] for j, value in enumerate(alpha)),
            sp.zeros(74, 18),
        )*source
        projected = multiplication[:72, :].applyfunc(sp.expand)
        row_span = sp.Matrix.hstack(*(projected.diff(variable) for variable in parameters))
        independent = list(row_span.T.rref()[1])
        matrix = projected[independent, :]
        assert matrix.shape == (9, 7)
        expression = str(matrix.tolist()).replace("[", "{").replace("]", "}").replace("**", "^")
        checks += [f"small=matrix{expression};\n",
                   "assert(saturate(minors(6,small),ideal(z0,z1,z2))"
                   f"==(ideal({span[0]},{span[1]}))^4);\n"]
        fibre = multiplication.subs(dict(zip(parameters, point, strict=True)))
        assert fibre.rank() == 3
        assert all(fibre.row_join(targets[:, j]).rank() == 4 for j in range(2))
    run_m2("".join(checks))

    # The interior direction calculation records only a necessary locus.
    p, r = 1 + t, b + c*t
    _, incidence = maps(p, r)
    polynomial = sp.cancel(36*incidence[:6, :].det(method="domain-ge")
                           / (7*(2 - b)**3*(b - c)**3))
    assert polynomial.is_polynomial(b, c)
    assert sp.Poly(polynomial, b, c).total_degree() == 12
    assert len(sp.Poly(polynomial, b, c).terms()) == 49
    print("PASS: linear endpoint boundary and degree-twelve necessary interior locus")


def main():
    bases = (DATA / "localcoh-incidence-bases.txt").read_text().splitlines()
    assert bases[0] == "ancestor stage4 numerators"
    assert bases[31] == "quartic multipliers" and len(bases[32:]) == 18
    assert bases[1:31] == (DATA / "localcoh-symbol-numerators.txt").read_text().splitlines()
    residues = [moments(numerator) for numerator in bases[1:31]]
    saved_top = json.loads((DATA / "localcoh-symbol-top.json").read_text())
    top_map = sp.Matrix([
        [column[i, 3 - i].nth(j) for column in residues]
        for i in range(4) for j in range(8)
    ])
    assert all(column[i, 3 - i].degree() <= 7 for column in residues for i in range(4))
    assert top_map == sp.Matrix(saved_top["matrix"])
    obstruction = sp.Matrix(saved_top["annihilator"])
    assert obstruction.rank() == 3 and obstruction * top_map == sp.zeros(3, 30)
    columns = list(top_map.rref()[1])
    rows = list(top_map[:, columns].T.rref()[1])
    assert len(rows) == len(columns) == 29
    section = sp.zeros(30, 32)
    inverse = top_map[rows, columns].inv()
    for j, column in enumerate(columns):
        for k, row in enumerate(rows):
            section[column, row] = inverse[j, k]
    kernel, = top_map.nullspace()

    def lift(p, r, h):
        top = sp.Matrix([
            sp.Poly(h * p**i * r**(3 - i), t).nth(j)
            for i in range(4) for j in range(8)
        ])
        alpha = section * top + ell * kernel
        uu, uv, vv = (
            sp.expand(sum(value * column[i, 2 - i].as_expr()
                          for value, column in zip(alpha, residues)))
            for i in (2, 1, 0)
        )
        return alpha, list(obstruction * top), (uu, uv, vv)

    def middle(p, r, quadratic):
        uu, uv, vv = quadratic
        return sp.Poly(r**2 * uu - 2*p*r*uv + p**2 * vv, t)

    def chart(p, r, h):
        _, top, quadratic = lift(p, r, h)
        return top + middle(p, r, quadratic).all_coeffs()

    p = 1 + a*t + b*t**2
    r = c + d*t + e*t**2
    p_zero = a*t + b*t**2
    r_unit = 1 + d*t + e*t**2
    r_zero = d*t + e*t**2
    checks = [
        chart_check("endpoint h=t, p(0)=1", (ell, e, d, b, c, a),
                    chart(p, r, t), resultant(p, r), [1]),
        chart_check("endpoint h=t, p(0)=0 and r(0)=1", (ell, e, d, b, a),
                    chart(p_zero, r_unit, t), resultant(p_zero, r_unit), [1]),
        chart_check("off endpoint, p(0)=0", (ell, e, d, b, a),
                    chart(p_zero, r_unit, 1 + t), resultant(p_zero, r_unit),
                    [4*a**2 + 4*a + 5, 4*b + 2*a - 3, 2*d + 2*a + 5,
                     e - 2*a + 5, 14*ell + 246*a - 115]),
        chart_check("off endpoint, r(0)=0", (ell, e, d, b, a),
                    chart(p, r_zero, 1 + t), resultant(p, r_zero),
                    [a**2 + 1, 2*b + a - 1, d + a + 1, e - 2*a + 4,
                     7*ell - 2*a + 2]),
    ]

    # On b*e != 0, the middle equation implies p | uu and r | vv.
    # Strip powers of the leading coefficients, which are invertible here.
    _, top, (uu, _, vv) = lift(p, r, 1 + t)
    p_remainder = sp.Poly(sp.prem(uu, p, t), t)
    r_remainder = sp.Poly(sp.prem(vv, r, t), t)
    divisibility = [sp.cancel(f/b**2) for f in p_remainder.all_coeffs()]
    divisibility += [sp.cancel(f/e**power)
                     for f, power in zip(r_remainder.all_coeffs(), (4, 3), strict=True)]
    e_value, = sp.solve(top[0], e)
    reduced = [sp.expand(f.subs(e, e_value)) for f in top[1:] + divisibility]
    assert all(f.is_polynomial(a, b, c, d) for f in reduced)
    checks.append(chart_check(
        "off endpoint, p(0)=1 and both quadratic coefficients nonzero", (d, b, c, a),
        reduced, (b * e * resultant(p, r)).subs(e, e_value),
        [4*b + 2*a - 3*c - 2, 2*d + 2*a + 5*c + 2,
         5*c**2 + 4*c*a + 4*a**2 + 8*c + 4],
    ))
    run_m2("".join(checks))

    lines = (DATA / "localcoh-incidence-tensor.txt").read_text().splitlines()
    assert lines[0] == "30 18 74 542"
    tensor = sp.zeros(74, 542)
    for line in lines[1:]:
        row, column, value = line.split()
        tensor[int(row), int(column)] = sp.Rational(value)
    assert tensor[:, 540:] == sp.eye(74)[:, 72:]
    verify_constant(lift, middle, tensor)
    verify_linear_boundary(lift, middle, tensor)
    blocks = [tensor[:72, 18*j:18*(j + 1)] for j in range(30)]
    field = sp.QQ.algebraic_field(sp.I)

    def projected(alpha, domain):
        matrix = sum((value * block for value, block in zip(alpha, blocks)),
                     sp.zeros(72, 18))
        return DomainMatrix(
            [[domain.from_sympy(sp.expand(f)) for f in row] for row in matrix.tolist()],
            matrix.shape, domain,
        )

    # The other root is obtained by rational conjugation.
    a_value = -sp.Rational(1, 2) + sp.I
    p_special = p_zero.subs({a: a_value, b: (3 - 2*a_value)/4})
    r_special = r_unit.subs({d: -a_value - sp.Rational(5, 2), e: 2*a_value - 5})
    alpha, top, quadratic = lift(p_special, r_special, 1 + t)
    assert not any(map(sp.expand, top))
    lam = (115 - 246*a_value)/14
    assert sp.expand(middle(p_special, r_special, quadratic).as_expr().subs(ell, lam)) == 0
    assert sp.expand(resultant(p_special, r_special)) != 0
    assert projected(alpha.subs(ell, lam), field).rank() == 17
    print("PASS: projected tensor excludes both targets together on the quadratic fibre")

    a_value = -c/2 + sp.I*(c + 1)
    substitutions = {a: a_value, b: (2 - 2*a_value + 3*c)/4,
                     d: -a_value - 1 - 5*c/2, e: 2*a_value - 4 - 5*c}
    p_line, r_line = p.subs(substitutions), r.subs(substitutions)
    alpha, top, quadratic = lift(p_line, r_line, 1 + t)
    assert not any(map(sp.expand, top))
    contact = middle(p_line, r_line, quadratic)
    assert sp.expand(contact.nth(0).coeff(ell)) == 7*c
    lam = sp.cancel(-contact.nth(0).subs(ell, 0)/(7*c))
    assert lam.is_polynomial(c) and sp.expand(lam.subs(c, 0) - (2*sp.I - 2)/7) == 0
    assert sp.expand(contact.as_expr().subs(ell, lam)) == 0
    ring = field.poly_ring(c)
    matrix = projected(alpha.subs(ell, lam), ring)
    minors = [
        matrix.extract([21, 18, 6, 8, 2, 4, 22, 25, 13, 11, 16, 12, 9, 3, 26, 23, 27],
                       list(range(17))).det(),
        matrix.extract([71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 57, 56, 54, 55, 58],
                       [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0]).det(),
    ]
    assert [minor.degree() for minor in minors] == [51, 31]
    common = minors[0].gcd(minors[1])
    primitive = ring.from_sympy(sp.expand(resultant(p_line, r_line)))
    # Removing factors of the resultant covers all roots, with multiplicity.
    while (factor := common.gcd(primitive)).degree() > 0:
        common = common.exquo(factor)
    assert common.degree() == 0
    print("PASS: projected tensor has rank at least 17 on both primitive parameter lines")


if __name__ == "__main__":
    main()
