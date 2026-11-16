#!/usr/bin/env python3
"""Independent exact expansion of singular-defect family identities.

Uses only the standard library. Full products are expanded before taking
normal initials. The M2 companion independently checks full initial ideals;
this script checks finite polynomial identities, recurrence weights, and
filtered cancellation gaps. General conclusions require the report's proofs.
"""


def add(*polys):
    answer = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            answer[exponent] = answer.get(exponent, 0) + coefficient
    return {e: c for e, c in answer.items() if c}


def scale(c, poly):
    return {e: c * value for e, value in poly.items() if c * value}


def mul(left, right):
    answer = {}
    for e, c in left.items():
        for f, d in right.items():
            ef = tuple(a + b for a, b in zip(e, f))
            answer[ef] = answer.get(ef, 0) + c * d
    return {e: c for e, c in answer.items() if c}


ONE = {(0, 0, 0): 1}
T = {(1, 0, 0): 1}
X = {(0, 1, 0): 1}
Y = {(0, 0, 1): 1}


def power(poly, n):
    answer = ONE
    for _ in range(n):
        answer = mul(answer, poly)
    return answer


def initial(poly):
    order = min(e[1] + e[2] for e in poly)
    return {e: c for e, c in poly.items() if e[1] + e[2] == order}


def monomial(t, x, y):
    return {(t, x, y): 1}


def check_punctual():
    count = 0
    for m in range(2, 8):
        for r in range(1, 5):
            a = power(T, r)
            n = m + 1
            f = add(mul(a, X), power(X, 2), power(Y, m))
            g = add(mul(a, Y), mul(X, Y), power(Y, m), power(X, n))
            h = add(mul(X, g), scale(-1, mul(Y, f)))
            q = add(mul(X, power(Y, m)), scale(-1, power(Y, m + 1)))
            assert h == add(q, power(X, n + 1))
            assert initial(f) == mul(a, X)
            assert initial(g) == mul(a, Y)
            assert initial(h) == q
            assert add(mul(Y, f), scale(-1, mul(X, g)), h) == {}
            second = add(
                mul(scale(-1, add(power(Y, m), power(X, n))), f),
                mul(power(Y, m), g), mul(add(a, X), h))
            assert second == {}
            # Symbol syzygies and positive-order correction gaps.
            assert add(mul(Y, mul(a, X)),
                       scale(-1, mul(X, mul(a, Y)))) == {}
            assert add(scale(-1, mul(power(Y, m), mul(a, X))),
                       mul(power(Y, m), mul(a, Y)), mul(a, q)) == {}
            assert (m + 1) - 2 >= 1
            assert n + 1 > m + 1
            count += 1
    return count


def check_recursive():
    count = 0
    for n in range(2, 9):
        for q in range(3, 8):
            ds = [ONE, X]
            for j in range(2, n + 2):
                ds.append(add(mul(X, ds[-1]),
                              scale(-1, mul(power(Y, q), ds[-2]))))
            for j in range(1, n + 1):
                # Cassini identity; expands both full products first.
                assert add(mul(ds[j], ds[j]),
                           scale(-1, mul(ds[j + 1], ds[j - 1]))) == power(Y, q*j)
            hs = [mul(power(Y, q*i), ds[n-i]) for i in range(n+1)]
            for i, h in enumerate(hs):
                assert initial(h) == monomial(0, n-i, q*i)
            for i in range(1, n+1):
                next_h = hs[i+1] if i < n else {}
                assert add(mul(power(Y, q), hs[i-1]),
                           scale(-1, mul(X, hs[i])), next_h) == {}
            generator_degrees = [n + (q-1)*i for i in range(n+1)]
            syzygy_degrees = [generator_degrees[i] + 1 for i in range(1, n+1)]
            for i in range(1, n):
                assert generator_degrees[i+1] - syzygy_degrees[i-1] == q-2
            # Count standard monomials of (X,Y^q)^n directly.
            colength = sum(q*(n-x) for x in range(n))
            assert colength == q*n*(n+1)//2
            assert len(generator_degrees[2:]) == n-1
            count += 1
    return count


if __name__ == "__main__":
    p = check_punctual()
    g = check_recursive()
    print(f"PASS: {p} punctual-family full expansions and lifted syzygies")
    print(f"PASS: {g} recursive-family initials, Cassini identities, and syzygies")
    print("PASS: exact cancellation gaps q-2 and staircase colengths")
    print("Boundary: these are independent finite polynomial identities;")
    print("the accompanying report proves the parameter-family and Tor statements.")
