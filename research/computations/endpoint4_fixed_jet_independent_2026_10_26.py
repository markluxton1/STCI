#!/usr/bin/env python3
"""Independent fixed-carrier jet test by explicit local normal division.

Python standard library plus a C++17 compiler. It constructs a different
normal basis from the Macaulay2 quotient computation, checks all 286 known
global multiples in the kernel, and computes the modular rank. A rank below
683 is reported as such and is not an exclusion certificate.
"""
import array
import functools
import hashlib
import itertools
import json
import math
import shutil
import struct
import subprocess
import tempfile
from pathlib import Path

PRIME = 65521
assert all(PRIME % d for d in range(2, math.isqrt(PRIME) + 1))
ORDER = 12
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
        out = [0] * 23
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
               for a, b, c, d in SOURCE]
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
using U=std::uint32_t; using W=std::uint64_t;
U modpow(U a,U e,U p){ U r=1; while(e){if(e&1)r=W(r)*a%p;a=W(a)*a%p;e>>=1;}return r;}
int main(int argc,char**argv){
 std::ifstream in(argv[1],std::ios::binary); U nr,nc,p;
 in.read((char*)&nr,4);in.read((char*)&nc,4);in.read((char*)&p,4);
 std::vector<U> a(W(nr)*nc);in.read((char*)a.data(),a.size()*4);
 U r=0;
 for(U j=0;j<nc && r<nr;j++){
  U k=r;while(k<nr && a[W(k)*nc+j]==0)k++;if(k==nr)continue;
  if(k!=r)for(U c=j;c<nc;c++)std::swap(a[W(k)*nc+c],a[W(r)*nc+c]);
  U inv=modpow(a[W(r)*nc+j],p-2,p);
  for(U c=j;c<nc;c++)a[W(r)*nc+c]=W(a[W(r)*nc+c])*inv%p;
  for(U i=r+1;i<nr;i++){
   U q=a[W(i)*nc+j];if(!q)continue;
   a[W(i)*nc+j]=0;
   for(U c=j+1;c<nc;c++){
    U v=W(q)*a[W(r)*nc+c]%p;
    U old=a[W(i)*nc+c];a[W(i)*nc+c]=old>=v?old-v:old+p-v;
   }
  }
  r++;
 }
 std::cout<<r<<"\n";
}
"""


def main():
    rows = []
    for z in range(1, 31):
        rows.extend(point_matrix(z))
    assert len(rows) == 690
    payload = array.array("I", itertools.chain.from_iterable(rows)).tobytes()
    compiler = shutil.which("clang++") or shutil.which("g++")
    if not compiler:
        raise RuntimeError("A C++17 compiler is required for the modular rank replay")
    with tempfile.TemporaryDirectory(prefix="stci-endpoint4-") as work:
        work = Path(work)
        cpp, executable, data = work / "rank.cpp", work / "rank", work / "matrix.bin"
        cpp.write_text(RANK_CPP)
        data.write_bytes(struct.pack("=III", len(rows), len(SOURCE), PRIME) + payload)
        subprocess.run([compiler, "-std=c++17", "-O3", str(cpp), "-o", str(executable)],
                       check=True, capture_output=True, text=True)
        rank = int(subprocess.run([str(executable), str(data)], check=True,
                                 capture_output=True, text=True).stdout)
    result = {
        "status": "independent normal-division finite-field probe",
        "prime": PRIME,
        "sample_points": list(range(1, 31)),
        "matrix_shape": [690, 969],
        "rank": rank,
        "kernel_dimension": 969 - rank,
        "known_global_multiples": 286,
        "all_286_known_multiples_annihilated_at_every_sample": True,
        "normal_basis": NORMAL,
        "coefficient_matrix_sha256_native_uint32": hashlib.sha256(payload).hexdigest(),
        "rank_683_target_met": rank == 683,
        "scope": "Selected rational F6, order12 necessary jet test; rank lift requires the accompanying proof.",
    }
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "matrix_shape", "rank", "kernel_dimension",
        "all_286_known_multiples_annihilated_at_every_sample",
        "rank_683_target_met")}, indent=2))
    print("Wrote", destination.name)
    assert rank == 683, "The target rank was not certified; retain the JSON without an exclusion claim."


if __name__ == "__main__":
    main()
