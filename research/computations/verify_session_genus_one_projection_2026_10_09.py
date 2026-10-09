#!/usr/bin/env python3
"""Exact identities for the uniform pi=1 projection and new A3+2A1 family.

This verifies the displayed representations, not exhaustion of every
projection parameter or existence/nonexistence of unrestricted STCI mates.
"""
import hashlib
import json
from pathlib import Path

import sympy as S


def zero(expr):
    assert S.expand(expr) == 0, S.factor(expr)


def main():
    x0, x1, z, x2, x3, s, t, u, v, w, h = S.symbols(
        "x0 x1 z x2 x3 s t u v w h")
    al, be, ga, de, ep, aa, bb, cc, dd, ee = S.symbols(
        "alpha beta gamma delta epsilon a b c0 d e")
    quads = [x0*z-x1*x1, x0*x2-x1*z, x0*x3-x1*x2,
             x1*x2-z*z, x1*x3-z*x2, z*x3-x2*x2]
    curve = {x0:s**4, x1:s**3*t, z:s*s*t*t, x2:s*t**3, x3:t**4}
    for q in quads:
        zero(q.subs(curve))
    monoms = [a*b for i,a in enumerate([x0,x1,z,x2,x3])
              for b in [x0,x1,z,x2,x3][i:]]
    matrix = S.Matrix([[S.Poly(q,x0,x1,z,x2,x3).coeff_monomial(m)
                        for m in monoms] for q in quads])
    assert matrix.rank() == 6
    Q1 = -quads[3]+al*quads[0]+be*quads[1]+ga*quads[2]+de*quads[4]+ep*quads[5]
    Q2 = aa*quads[0]+bb*quads[1]+cc*quads[2]+dd*quads[4]+ee*quads[5]
    A = al*x0-be*x1-de*x2+ep*x3
    L = aa*x0-bb*x1-dd*x2+ee*x3
    R1 = -al*x1*x1+be*x0*x2+ga*(x0*x3-x1*x2)+de*x1*x3-ep*x2*x2-x1*x2
    R = -aa*x1*x1+bb*x0*x2+cc*(x0*x3-x1*x2)+dd*x1*x3-ee*x2*x2
    zero(Q1-(z*z+A*z+R1)); zero(Q2-(L*z+R))
    zc = s*s*t*t
    Dc = S.expand((A+2*z).subs(curve)); Lc = S.expand(L.subs(curve))
    zero(R.subs(curve)+zc*Lc)
    assert S.Poly(Lc,s,t).coeff_monomial(s*s*t*t) == 0
    assert S.Poly(Dc,s,t).coeff_monomial(s*s*t*t) == 2
    T = A*A/4-R1; W = R-A*L/2
    zero(T.subs(curve)-Dc*Dc/4)
    zero(W.subs(curve)+Dc*Lc/2)
    zero(W*W-T*L*L-(R*R-A*L*R+R1*L*L))
    chart = {x0:1,x1:u,z:u*u+v,x2:u**3+w,x3:u**4+h}
    rows = []
    for q in [Q1,Q2]:
        fq = S.expand(q.subs(chart))
        rows.append([S.diff(fq,k).subs({v:0,w:0,h:0}) for k in [v,w,h]])
    expected = [
        [2*u*u+al-be*u-de*u**3+ep*u**4,
         be-(1+ga)*u-de*u*u-2*ep*u**3, ga+de*u+ep*u*u],
        [aa-bb*u-dd*u**3+ee*u**4,
         bb-cc*u-dd*u*u-2*ee*u**3, cc+dd*u+ee*u*u]]
    for actual, exp in zip(rows,expected):
        for value, want in zip(actual,exp):
            zero(value-want)
    # Whitney umbrella: exact ambient relation and the local pure power.
    xx, yy = u*v, v*v
    zero(xx*xx-u*u*yy)
    differential = S.Matrix([[1,0],[v,u],[0,2*v]])
    assert differential.subs({u:0,v:0}).rank() == 1
    assert differential.subs({u:0,v:1}).rank() == 2
    # New A3+2A1 family, bound to its actual Y-coordinate coefficient map.
    delta = al*de-be*ga
    D0 = ga*s+de*t; N0 = al*s+be*t
    cv = [s*s*D0*D0,t*t*D0*D0,s*t*D0*D0,
          s*t*N0*N0,-s*t*D0*N0]
    coeff = S.Matrix([[S.expand(f).coeff(s,4-i).coeff(t,i)
                       for i in range(5)] for f in cv])
    determinant = S.factor(coeff.det())
    zero(determinant-ga*ga*de*de*delta**3)
    ap,bp,cp,dp,epoint = coeff[:,2]
    qa,qb,qc,qd,qe = S.symbols("qa qb qc qd qe")
    F1=qa*qb-qc*qc; F2=qc*qd-qe*qe
    fam = dict(zip([qa,qb,qc,qd,qe],cv))
    point = dict(zip([qa,qb,qc,qd,qe],[ap,bp,cp,dp,epoint]))
    zero(F1.subs(fam)); zero(F2.subs(fam))
    value1=S.expand(F1.subs(point)); value2=S.expand(F2.subs(point))
    zero(value1+3*ga*ga*de*de); zero(value2+delta*delta)
    polar1=S.expand(ap*cv[1]+bp*cv[0]-2*cp*cv[2])
    polar2=S.expand(cp*cv[3]+dp*cv[2]-2*epoint*cv[4])
    zero(polar1-D0*D0*(ga*ga*s*s-4*ga*de*s*t+de*de*t*t))
    zero(polar2+2*delta*delta*s*s*t*t)
    P4=ga**4*s**4-2*ga**3*de*s**3*t-2*ga*de**3*s*t**3+de**4*t**4
    zero(value1*polar2-value2*polar1-delta*delta*P4)
    rr=S.symbols("r")
    disc=S.discriminant(rr**4-2*rr**3-2*rr+1,rr)
    assert disc == -1728
    result = {
        "status":"PASS", "rnc_quadratic_ideal_rank":6,
        "uniform_middle_coefficients":{"Lc":0,"Dc":2},
        "normal_gradient_rows_verified":True,
        "completed_square_verified":True,
        "isolated_rank_one_local_countershield_verified":True,
        "A3_two_A1_family_coefficient_determinant":str(determinant),
        "A3_two_A1_normalized_conductor_discriminant":int(disc),
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope":"Displayed identities and family; no full projection exhaustion or global STCI claim."}
    out=Path(__file__).resolve().parents[1]/"scratch"/"session-genus-one-projection-checks-2026-10-09.json"
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
