#!/usr/bin/env python3
"""Independent fixed-carrier jet test by explicit local normal division.

Python standard library plus a C++17 compiler. It constructs a different
normal basis from the Macaulay2 quotient computation, checks all 286 known
global multiples in the kernel, and checks the modular rank and matrix digest.
The certificate is printed to stdout.
"""
import array
import functools
import hashlib
import itertools
import json
import math
import shutil
import struct
import sys
import subprocess
import tempfile
from pathlib import Path

PRIME = 65521
assert all(PRIME % d for d in range(2, math.isqrt(PRIME) + 1))
ORDER = 12
MATRIX_SHA256 = "a3e546424d11200e1d8075c7f9d5d342787bd925a303901bd2b33b2661f56445"
INV2 = pow(2, -1, PRIME)
INV4 = pow(4, -1, PRIME)


def add(*polys):
    out = {}
    for poly in polys:
        for m, c in poly.items():
            out[m] = (out.get(m, 0) + c) % PRIME
    return {m: c for m, c in out.items() if c}


def scale(poly, c):
    return {m: c * a % PRIME for m, a in poly.items() if c * a % PRIME}


def mul(p, q, cutoff=None):
    out = {}
    for m, a in p.items():
        for n, b in q.items():
            key = tuple(i + j for i, j in zip(m, n))
            if cutoff is not None and sum(key) >= cutoff:
                continue
            out[key] = (out.get(key, 0) + a * b) % PRIME
    return {m: c for m, c in out.items() if c}


def power(p, n, cutoff=None):
    ans = {(0,) * len(next(iter(p))): 1}
    for _ in range(n):
        ans = mul(ans, p, cutoff)
    return ans


def exponents(degree):
    return [(a, b, c, degree - a - b - c)
            for a in range(degree + 1)
            for b in range(degree - a + 1)
            for c in range(degree - a - b + 1)]


SOURCE = exponents(16)
INDEX = {m: i for i, m in enumerate(SOURCE)}
assert len(SOURCE) == 969
NORMAL = [(0, j) for j in range(ORDER)] + [(1, j) for j in range(ORDER - 1)]
NORMAL_INDEX = {m: i for i, m in enumerate(NORMAL)}
assert len(NORMAL) == 23

# Construct the actual homogeneous sextic independently.
x0, x1, x2, x3 = (
    {tuple(int(i == j) for i in range(4)): 1} for j in range(4)
)
q4 = add(mul(x0, x3), scale(mul(x1, x2), -1))
d4 = add(power(x2, 3), scale(mul(x1, power(x3, 2)), -1))
F4 = add(scale(mul(power(q4, 2), power(x3, 2)), -1),
         scale(mul(mul(q4, d4), x2), -1),
         scale(power(d4, 2), INV4), power(q4, 3))
assert all(sum(m) == 6 for m in F4)
MULTIPLES = [
    [(INDEX[tuple(a + b for a, b in zip(m, h))], c) for m, c in F4.items()]
    for h in exponents(10)
]
assert len(MULTIPLES) == 286


def point_matrix(z):
    assert z % PRIME and (z * z + 1) % PRIME
    one = {(0, 0): 1}
    U, V = {(1, 0): 1}, {(0, 1): 1}
    image2 = add(scale(one, pow(z, 3, PRIME)), V)
    image3 = add(scale(one, pow(z, 4, PRIME)), U, scale(V, 3 * z * INV2))
    q = add(image3, scale(image2, -z))
    cubic = add(power(image2, 3), scale(power(image3, 2), -z))
    f = add(scale(mul(power(q, 2), power(image3, 2)), -1),
            scale(mul(mul(q, cubic), image2), -1),
            scale(power(cubic, 2), INV4), power(q, 3))
    assert min(map(sum, f)) == 2
    assert f.get((2, 0), 0) == pow(z, 8, PRIME) * (1 + z * z) % PRIME
    assert f.get((1, 1), 0) == 0
    assert f.get((0, 2), 0) == -pow(z, 10, PRIME) * INV4 % PRIME
    leading = f[(2, 0)]
    relations = [(m, -c * pow(leading, -1, PRIME) % PRIME)
                 for m, c in f.items() if m != (2, 0)]

    @functools.lru_cache(None)
    def reduce_monomial(i, j):
        if i + j >= ORDER:
            return ()
        if i < 2:
            return (((i, j), 1),)
        out = {}
        for (a, b), c in relations:
            for m, d in reduce_monomial(i - 2 + a, j + b):
                out[m] = (out.get(m, 0) + c * d) % PRIME
        return tuple((m, c) for m, c in out.items() if c)

    def reduce_poly(poly):
        out = [0] * len(NORMAL)
        for (i, j), c in poly.items():
            for m, d in reduce_monomial(i, j):
                k = NORMAL_INDEX[m]
                out[k] = (out[k] + c * d) % PRIME
        return out

    assert not any(reduce_poly(f)), "The actual carrier must reduce to zero"
    p2, p3 = [one], [one]
    for _ in range(16):
        p2.append(mul(p2[-1], image2, ORDER))
        p3.append(mul(p3[-1], image3, ORDER))
    base = {(c, d): reduce_poly(mul(p2[c], p3[d], ORDER))
            for c in range(17) for d in range(17 - c)}
    columns = [[pow(z, b, PRIME) * t % PRIME for t in base[(c, d)]]
               for _, b, c, d in SOURCE]
    rows = [list(row) for row in zip(*columns)]
    # No coefficient/monomial-order convention is implicit in this test.
    for vector in MULTIPLES:
        for row in rows:
            assert sum(row[index] * c for index, c in vector) % PRIME == 0, (
                "Known multiple not killed", z
            )
    return rows


RANK_CPP = r"""
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

using Entry = std::uint32_t;
using Product = std::uint64_t;

Entry modpow(Entry base, Entry exponent, Entry modulus) {
    Entry result = 1;
    while (exponent) {
        if (exponent & 1) result = Product(result) * base % modulus;
        base = Product(base) * base % modulus;
        exponent >>= 1;
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 2) return 1;
    std::ifstream input(argv[1], std::ios::binary);
    Entry rows, cols, prime;
    input.read(reinterpret_cast<char*>(&rows), sizeof(rows));
    input.read(reinterpret_cast<char*>(&cols), sizeof(cols));
    input.read(reinterpret_cast<char*>(&prime), sizeof(prime));
    if (!input) return 1;

    std::vector<Entry> matrix(Product(rows) * cols);
    input.read(reinterpret_cast<char*>(matrix.data()), matrix.size() * sizeof(Entry));
    if (!input) return 1;

    auto at = [&](Entry row, Entry col) -> Entry& {
        return matrix[Product(row) * cols + col];
    };

    Entry rank = 0;
    for (Entry col = 0; col < cols && rank < rows; ++col) {
        Entry pivot = rank;
        while (pivot < rows && at(pivot, col) == 0) ++pivot;
        if (pivot == rows) continue;
        for (Entry k = col; k < cols; ++k) {
            std::swap(at(pivot, k), at(rank, k));
        }
        const Entry inverse = modpow(at(rank, col), prime - 2, prime);
        for (Entry k = col; k < cols; ++k) {
            at(rank, k) = Product(at(rank, k)) * inverse % prime;
        }
        for (Entry row = rank + 1; row < rows; ++row) {
            const Entry factor = at(row, col);
            if (factor == 0) continue;
            at(row, col) = 0;
            for (Entry k = col + 1; k < cols; ++k) {
                const Entry subtract = Product(factor) * at(rank, k) % prime;
                const Entry old = at(row, k);
                at(row, k) = old >= subtract ? old - subtract : old + prime - subtract;
            }
        }
        ++rank;
    }
    std::cout << rank << "\n";
}
"""


def main():
    rows = []
    for z in range(1, 31):
        rows.extend(point_matrix(z))
    assert len(rows) == 690
    entries = array.array("I", itertools.chain.from_iterable(rows))
    assert entries.itemsize == 4
    payload = entries.tobytes()
    compiler = shutil.which("clang++") or shutil.which("g++")
    if not compiler:
        raise RuntimeError("A C++17 compiler is required for the modular rank replay")
    with tempfile.TemporaryDirectory(prefix="stci-endpoint4-") as work:
        work_dir = Path(work)
        cpp = work_dir / "rank.cpp"
        executable = work_dir / "rank"
        data = work_dir / "matrix.bin"
        cpp.write_text(RANK_CPP)
        data.write_bytes(struct.pack("=III", len(rows), len(SOURCE), PRIME) + payload)
        subprocess.run([compiler, "-std=c++17", "-O3", str(cpp), "-o", str(executable)],
                       check=True, capture_output=True, text=True)
        rank = int(subprocess.run([str(executable), str(data)], check=True,
                                 capture_output=True, text=True).stdout)
    if sys.byteorder == "big":
        entries.byteswap()
    digest = hashlib.sha256(entries.tobytes()).hexdigest()
    assert digest == MATRIX_SHA256, f"Unexpected jet matrix digest: {digest}"
    assert rank == 683, f"The target rank was not certified: {rank}"

    result = {
        "status": "independent normal-division finite-field probe",
        "prime": PRIME,
        "sample_points": list(range(1, 31)),
        "matrix_shape": [690, 969],
        "rank": rank,
        "kernel_dimension": len(SOURCE) - rank,
        "known_global_multiples": 286,
        "all_286_known_multiples_annihilated_at_every_sample": True,
        "normal_basis": NORMAL,
        "coefficient_matrix_sha256_little_endian_uint32": digest,
        "scope": "Selected rational F6, order12 necessary jet test; rank lift requires the accompanying proof.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
