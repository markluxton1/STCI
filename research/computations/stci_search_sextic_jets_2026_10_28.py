#!/usr/bin/env python3
"""Search actual global degree-16 mates on previously untested sextics.

Exact modular necessary-jet ranks; no arbitrary k(C) source coefficients.
Only rank equal to the known maximum certifies that every source is a
global multiple. Smaller ranks are upper bounds on characteristic-zero
kernel dimension, and are never reported as constructions.

Uses the polynomial arithmetic and C++ modular elimination implementation
from the independently reviewed R-0025 script, without running its carrier
test. New inputs, normal equations and all-multiple checks are built here.
"""
import array
import functools
import hashlib
import itertools
import json
import shutil
import struct
import subprocess
import tempfile
from pathlib import Path

from endpoint4_fixed_jet_independent_2026_10_26 import (
    PRIME, INV4, add, scale, mul, power, exponents, RANK_CPP,
)

ORDER = 12
DEGREE = 16
SOURCE = exponents(DEGREE)
INDEX = {m: i for i, m in enumerate(SOURCE)}
NORMAL = [(0, j) for j in range(ORDER)] + [(1, j) for j in range(ORDER-1)]
NORMAL_INDEX = {m: i for i, m in enumerate(NORMAL)}
MAX_RANK = len(SOURCE) - len(exponents(DEGREE-6))
assert (len(SOURCE),len(NORMAL),MAX_RANK) == (969,23,683)


def carrier(t, kappa, images):
    x0,x1,x2,x3=images
    q=add(mul(x0,x3),scale(mul(x1,x2),-1))
    d=add(power(x2,3),scale(mul(x1,power(x3,2)),-1))
    return add(scale(mul(power(q,2),power(x3,2)),-1),
               scale(mul(mul(q,d),x2),-1),
               scale(mul(mul(q,d),x3),-t),
               scale(power(d,2),INV4),scale(power(q,3),kappa))


def ambient_carrier(t,kappa):
    variables=[{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
    f=carrier(t,kappa,variables)
    assert all(sum(m)==6 for m in f)
    return f


def point_matrix(z,t,kappa,multiples):
    one={(0,0):1}
    u,v={(1,0):1},{(0,1):1}
    x2=add(scale(one,pow(z,3,PRIME)),v)
    x3=add(scale(one,pow(z,4,PRIME)),u,scale(v,3*z*pow(2,-1,PRIME)))
    f=carrier(t,kappa,[one,scale(one,z),x2,x3])
    a=(1+2*t*z+z*z)%PRIME
    assert z%PRIME and a
    assert min(map(sum,f))==2
    assert f.get((2,0),0)==pow(z,8,PRIME)*a%PRIME
    assert f.get((1,1),0)==t*pow(z,10,PRIME)%PRIME
    assert f.get((0,2),0)==-pow(z,10,PRIME)*INV4%PRIME
    leading=f[(2,0)]
    relations=[(m,-c*pow(leading,-1,PRIME)%PRIME)
               for m,c in f.items() if m!=(2,0)]

    @functools.lru_cache(None)
    def reduce_monomial(i,j):
        if i+j>=ORDER:return ()
        if i<2:return (((i,j),1),)
        out={}
        for (a,b),c in relations:
            for m,d in reduce_monomial(i-2+a,j+b):
                out[m]=(out.get(m,0)+c*d)%PRIME
        return tuple((m,c) for m,c in out.items() if c)

    def reduce_poly(poly):
        out=[0]*len(NORMAL)
        for (i,j),c in poly.items():
            for m,d in reduce_monomial(i,j):
                k=NORMAL_INDEX[m]
                out[k]=(out[k]+c*d)%PRIME
        return out

    assert not any(reduce_poly(f))
    p2,p3=[one],[one]
    for _ in range(DEGREE):
        p2.append(mul(p2[-1],x2,ORDER));p3.append(mul(p3[-1],x3,ORDER))
    base={(c,d):reduce_poly(mul(p2[c],p3[d],ORDER))
          for c in range(DEGREE+1) for d in range(DEGREE+1-c)}
    columns=[[pow(z,b,PRIME)*a%PRIME for a in base[(c,d)]]
             for _,b,c,d in SOURCE]
    rows=[list(row) for row in zip(*columns)]
    for vector in multiples:
        for row in rows:
            assert sum(row[index]*c for index,c in vector)%PRIME==0,(
                "Actual global multiple not annihilated",t,kappa,z)
    return rows


def main():
    # The known R-0025 point (t,kappa)=(0,1) is deliberately not replayed.
    parameters=[(0,0),(1,0),(1,1),(1,-1),(2,0),(2,1),(0,-1)]
    results=[]
    compiler=shutil.which("clang++") or shutil.which("g++")
    if not compiler:raise RuntimeError("C++17 compiler required")
    with tempfile.TemporaryDirectory(prefix="stci-search-jets-") as work:
        work=Path(work)
        cpp,exe,data=work/"rank.cpp",work/"rank",work/"matrix.bin"
        cpp.write_text(RANK_CPP)
        subprocess.run([compiler,"-std=c++17","-O3",str(cpp),"-o",str(exe)],
                       check=True,capture_output=True,text=True)

        def rank_rows(rows):
            payload=array.array("I",itertools.chain.from_iterable(rows)).tobytes()
            data.write_bytes(struct.pack("=III",len(rows),len(SOURCE),PRIME)+payload)
            rank=int(subprocess.run([str(exe),str(data)],check=True,
                                    capture_output=True,text=True).stdout)
            return rank,hashlib.sha256(payload).hexdigest()

        for t,kappa in parameters:
            f=ambient_carrier(t,kappa)
            multiples=[[(INDEX[tuple(a+b for a,b in zip(m,h))],c) for m,c in f.items()]
                       for h in exponents(DEGREE-6)]
            points=[z for z in range(1,80) if (1+2*t*z+z*z)%PRIME
                    and (1+2*t*z+(1+t*t)*z*z)%PRIME][:40]
            rows=[]
            for z in points:rows.extend(point_matrix(z,t,kappa,multiples))
            rank,digest=rank_rows(rows)
            filtration=[]
            # Build once at order12, then retain lower-degree normal rows.
            # Reduction cannot decrease normal degree, so truncation commutes.
            for order in (8,9,10,11,12):
                if order==12:r,h=rank,digest
                else:
                    selected=[row for i,row in enumerate(rows)
                              if sum(NORMAL[i%len(NORMAL)])<order]
                    r,h=rank_rows(selected)
                filtration.append({"normal_cutoff":order,"rank_lower_bound":r,
                                   "kernel_dimension_upper_bound":len(SOURCE)-r,
                                   "possible_proper_directions_upper_bound":MAX_RANK-r,
                                   "kernel_equals_global_multiples":r==MAX_RANK,
                                   "matrix_sha256_native_uint32":h})
            first=next((x["normal_cutoff"] for x in filtration
                        if x["kernel_equals_global_multiples"]),None)
            result={"t":t,"kappa":kappa,"ambient_carrier_mod_prime":
                    [[list(m),c] for m,c in sorted(f.items())],
                    "sample_points":points,"matrix_shape":[len(rows),len(SOURCE)],
                    "all_286_global_multiples_annihilated_at_every_sample":True,
                    "filtration":filtration,
                    "first_certified_cutoff_among_tested":first,
                    "all_degree16_proper_mates_generic_length_upper_bound":
                    None if first is None else 2*(first-1),
                    "all_degree16_proper_mates_residual_degree_lower_bound":
                    None if first is None else 96-8*(first-1)}
            results.append(result)
            print(json.dumps({k:result[k] for k in ("t","kappa",
                "first_certified_cutoff_among_tested",
                "all_degree16_proper_mates_generic_length_upper_bound",
                "all_degree16_proper_mates_residual_degree_lower_bound")}))
            print("filtration",[(a["normal_cutoff"],a["rank_lower_bound"])
                                 for a in filtration],flush=True)
            destination=Path(__file__).with_suffix(".json")
            destination.write_text(json.dumps({"status":"provisional exact rank certificates",
                "prime":PRIME,"source_degree":DEGREE,"known_multiples":286,
                "source_dimension":969,"max_rank":MAX_RANK,
                "scope":"Seven selected actual sextics, all degree16 global mates; no family exhaustion",
                "results":results},indent=2)+"\n")


if __name__=="__main__":main()
