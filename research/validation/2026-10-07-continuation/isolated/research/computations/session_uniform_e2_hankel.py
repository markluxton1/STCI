#!/usr/bin/env python3
"""Session exploration: universal e=2 fourth-class quadratic annihilator.

This imports the established moving-coordinate obstruction generator; it is
not an independent verification of that generator.  Outputs are isolated
from canonical certificate inputs.
"""
from pathlib import Path
import importlib.util
from itertools import combinations
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "primitive47session", ROOT / "research/scratch/primitive47universal/generate.py"
)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def main():
    A = {0:g.a0, 1:g.a1, 2:g.a2}
    B = {0:g.b0, 1:g.b1, 2:g.b2}
    Av = {2-i:c for i,c in A.items()}
    Bv = {2-i:c for i,c in B.items()}
    delta, S, T = g.bezout(A, B)
    _, Sv, Tv = g.bezout(Av, Bv)
    W, up, vp = g.ambient([{}, A, {}, {}], [{}, B, {}, {}])
    mp = g.plus(g.prod(g.evalpoly(Bv,W),up), g.scale(-1,g.prod(g.evalpoly(Av,W),vp)))
    h2 = g.shift(9,mp[2])
    gu = {e:c for e,c in h2.items() if e>=0}
    gv = {-e-1:-c for e,c in h2.items() if e<0}
    U2 = g.neg(g.mul(T,gu))
    V2 = g.mul(S,gu)
    W,up,vp = g.ambient([{},A,U2,{}],[{},B,V2,{}])
    mp = g.plus(g.prod(g.evalpoly(Bv,W),up),g.scale(-1,g.prod(g.evalpoly(Av,W),vp)))
    ep = g.plus(g.prod(g.evalpoly(Sv,W),up),g.prod(g.evalpoly(Tv,W),vp))
    gv0 = {-e:c for e,c in gv.items()}
    gv1 = g.mul({-e:c for e,c in g.derivative(gv).items()},W[1])
    h3 = g.shift(9,g.add(mp[3],g.shift(-5,g.smul(2,g.mul(gv0,ep[2]))),g.shift(-10,gv1)))
    coords = [g.reduce_inverse(h3.get(-j,g.zero),delta) for j in range(1,6)]
    denominator_power = max(d for _,d in coords)
    c = [p*delta**(denominator_power-d) for p,d in coords]
    print("Universal coefficient terms:", [len(p.terms()) for p in c], flush=True)
    # Exact determinant of the three-by-three Hankel matrix over the ring.
    determinant = c[0]*(c[2]*c[4]-c[3]**2)-c[1]*(c[1]*c[4]-c[2]*c[3])+c[2]*(c[1]*c[3]-c[2]**2)
    determinant_denominator_power = 3*denominator_power
    while determinant_denominator_power:
        q,rem = divmod(determinant,delta)
        if rem:
            break
        determinant = q
        determinant_denominator_power -= 1
    print("Reduced Hankel numerator terms:",len(determinant.terms()),flush=True)
    scalar, factors = sp.factor_list(determinant.as_expr())
    factor = scalar*sp.prod(p**n for p,n in factors)
    print("Hankel factor degrees:",
          [(sp.Poly(p, *sp.symbols('a0 a1 a2 b0 b1 b2')).total_degree(), n)
           for p,n in factors], flush=True)
    linear_annihilator_minors = []
    for i,j in combinations(range(4),2):
        numerator = c[i]*c[j+1]-c[i+1]*c[j]
        dp = 2*denominator_power
        while dp:
            q,rem = divmod(numerator,delta)
            if rem:
                break
            numerator,dp = q,dp-1
        linear_annihilator_minors.append(
            {"rows":[i,j],"numerator":str(numerator.as_expr()),"denominator_power":dp}
        )
    print("Linear-annihilator minor terms:",
          [len(sp.Poly(sp.sympify(x['numerator'])).terms())
           for x in linear_annihilator_minors],flush=True)
    output = {
        "status":"Exact polynomial from the existing generator, not independent input audit",
        "variables":["a0","a1","a2","b0","b1","b2"],
        "resultant":str(delta.as_expr()),
        "coordinates":[{"numerator":str(p.as_expr()),"denominator_power":d} for p,d in coords],
        "hankel_numerator":str(determinant.as_expr()),
        "hankel_factorization":str(factor),
        "hankel_denominator_power":determinant_denominator_power,
        "linear_annihilator_minors":linear_annihilator_minors,
    }
    target = ROOT / "research/scratch/session_uniform_e2_hankel.json"
    target.write_text(json.dumps(output,indent=2)+"\n")
    print("Wrote",target,flush=True)


if __name__ == "__main__":
    main()
