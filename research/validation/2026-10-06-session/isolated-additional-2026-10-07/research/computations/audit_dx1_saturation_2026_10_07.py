#!/usr/bin/env python3
"""Reconstruct and verify the dx=1 obstruction saturation over QQ.

The five source obstructions are parsed from the persisted 2026-10-05
four-parameter calculation. This audit generates a compact standalone M2
certificate, checks provenance against the 2026-10-06 inputs, and compares
the universal-coordinate snapshot without depending on it for saturation.
Use /private/tmp/stci-cas-venv/bin/python (SymPy) and /opt/homebrew/bin/M2.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sympy as sp

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
a,b,d,x=sp.symbols("a b d x")
u=b*x-a
t=x*u
alpha=2*a+1
beta=b+2
source_path=HERE/"e2_full4_obstruction_2026-10-05.txt"
source=source_path.read_text()
locals_map={str(v):v for v in (a,b,d,x)}
Delta=sp.sympify(re.search(r"^Delta = (.+)$",source,re.M).group(1),locals=locals_map)
assert sp.cancel(Delta.subs(d,1/x)-u**2/x)==0
Q=[]
G=[]
denominators=[]
for i in range(1,6):
    g=sp.sympify(re.search(rf"^G{i} = (.+)$",source,re.M).group(1),locals=locals_map)
    G.append(g)
    numerator,denominator=sp.fraction(sp.cancel(g.subs(d,1/x)))
    q,remainder=sp.div(sp.expand(numerator),u,a)
    assert remainder==0
    assert sp.cancel(g.subs(d,1/x)-u*q/denominator)==0
    assert sp.Poly(denominator,x).terms()==[((sp.degree(denominator,x),),1)]
    Q.append(sp.expand(q))
    denominators.append(str(denominator))

legacy=(HERE/"session_dx1_saturation_2026_10_06.m2").read_text()
legacy_Q=[sp.sympify(re.search(rf"^Q{i}=(.+);$",legacy,re.M).group(1).replace("^","**"),locals=locals_map) for i in range(1,6)]
assert all(sp.expand(q-r)==0 for q,r in zip(Q,legacy_Q))
R2=sp.cancel(Q[1]/alpha)
R4=sp.cancel(Q[3]/(2*beta))
assert sp.Poly(R2,a,b,x,domain=sp.QQ).as_expr()==R2
assert sp.Poly(R4,a,b,x,domain=sp.QQ).as_expr()==R4
H=[x*beta**2+alpha*beta-2*alpha**2,(4*x+2)*alpha*beta-3*alpha**2,beta**3,alpha*beta**2,alpha**2*beta,alpha**3]
HJ=sp.groebner(H,a,b,x,order="grevlex",domain=sp.QQ)
assert all(HJ.reduce(q)[1]==0 for q in Q)
assert all(sp.expand(q.subs({a:-sp.Rational(1,2),b:-2}))==0 for q in Q)
print("PASS SymPy: source specialization, denominator chart, all five provenance identities, L subset J.",flush=True)

# Independently expand a saved 5-by-6 multiplier matrix. Its entries were
# obtained with Macaulay2, but their validity is checked here by QQ polynomial
# multiplication rather than by recomputing a Groebner basis.
membership_path=HERE/"session_dx1_shifted_membership_2026_10_07.txt"
raw=membership_path.read_text().split("S^{6:{-3}},",1)[1]
assert raw.startswith("{{") and raw.endswith("}},Degree => {3})")
rows=re.split(r"\}\s*,\s*\{",raw[2:].rsplit("}},Degree =>",1)[0])
assert len(rows)==5
A,B=sp.symbols("A B")
shifted_symbols={"A":A,"B":B,"x":x}
coefficients=[[sp.Poly(sp.sympify(v.replace("^","**"),locals=shifted_symbols),A,B,x,domain=sp.QQ) for v in row.split(",")] for row in rows]
assert all(len(row)==6 for row in coefficients)
shift={a:(A-1)/2,b:B-2}
shifted_Q=[sp.Poly(q.subs(shift),A,B,x,domain=sp.QQ) for q in Q]
for j,h in enumerate(H):
    actual=sum((shifted_Q[i]*coefficients[i][j] for i in range(5)),sp.Poly(0,A,B,x,domain=sp.QQ))
    expected=sp.Poly((t*h).subs(shift),A,B,x,domain=sp.QQ)
    assert (actual-expected).is_zero
print("PASS SymPy: independent 5-by-6 polynomial expansion proves t*J subset L.",flush=True)

snapshot=ROOT/"research/validation/2026-10-06-session/isolated/research/scratch/primitive47universal/equations.json"
universal_check=None
if snapshot.exists():
    data=json.loads(snapshot.read_text())
    a0,a1,a2,b0,b1,b2=sp.symbols("a0 a1 a2 b0 b1 b2")
    sub={a0:x,a1:a,a2:1,b0:1,b1:b,b2:d}
    U=[sp.expand(sp.sympify(c["numerator"]).subs(sub)) for c in data["coordinates"]]
    assert all(sp.expand(U[i]-G[4-i]/32)==0 for i in range(5))
    assert sp.expand(sp.sympify(data["resultant"]).subs(sub)-Delta)==0
    universal_check={"snapshot_path":str(snapshot.relative_to(ROOT)),"snapshot_sha256":hashlib.sha256(snapshot.read_bytes()).hexdigest(),"coordinate_identity":"U_i(a0=x,a1=a,a2=1,b0=1,b1=b,b2=d)=G_(6-i)/32"}
    print("PASS SymPy: universal-coordinate specialization equals reversed P-044 coordinates /32.",flush=True)

m2_path=HERE/"verify_dx1_saturation_2026_10_07.m2"
script="-- Generated from the persisted five obstruction polynomials.\n-- Source SHA256: "+hashlib.sha256(source_path.read_bytes()).hexdigest()+"\n"
script+="R=QQ[a,b,x,MonomialOrder=>GRevLex];\n"
script+="".join(f"Q{i}={sp.sstr(q).replace('**','^')};\n" for i,q in enumerate(Q,1))
script+="""u=b*x-a; t=x*u; alpha=2*a+1; beta=b+2;
L=ideal(Q1,Q2,Q3,Q4,Q5);
J=ideal(x*beta^2+alpha*beta-2*alpha^2,(4*x+2)*alpha*beta-3*alpha^2,beta^3,alpha*beta^2,alpha^2*beta,alpha^3);
assert((gens L) % J == 0);
assert((t*gens J) % L == 0);
assert((J:ideal(t))==J);
assert((L:ideal(t))==J);
assert(saturate(L,ideal(t))==J);
assert(alpha^3 % J == 0_R and beta^3 % J == 0_R);
assert((gens J) % ideal(alpha,beta)==0);
assert(saturate(L,ideal(t*alpha*beta))==ideal(1_R));
print "PASS: t J subset L subset J; J:t=J; L:t=J; L:t^infinity=J.";
print "PASS: radical J=(2a+1,b+2), full residual open set empty.";
Ra=QQ[b,x,MonomialOrder=>GRevLex];
phi=map(Ra,R,{-1/2,b,x});
assert(saturate(phi L,ideal(x*(b*x+1/2)))==ideal((b+2)^2));
Rb=QQ[a,x,MonomialOrder=>GRevLex];
psi=map(Rb,R,{a,-2,x});
assert(saturate(psi L,ideal(x*(-2*x-a)))==ideal((2*a+1)^2));
print "PASS: a=-1/2 and b=-2 boundary saturated ideals are the claimed squares.";
"""
m2_path.write_text(script)
metadata={"source_path":str(source_path.relative_to(ROOT)),"source_sha256":hashlib.sha256(source_path.read_bytes()).hexdigest(),"variables":["a","b","x"],"Q":[str(q) for q in Q],"specialized_denominators":denominators,"u":"b*x-a","t":"x*(b*x-a)","alpha":"2*a+1","beta":"b+2","J_generators":[str(sp.expand(h)) for h in H],"membership_certificate_path":str(membership_path.relative_to(ROOT)),"membership_certificate_sha256":hashlib.sha256(membership_path.read_bytes()).hexdigest(),"localized_ideal_equalities":["L subset J","t*J subset L","J:t=J","L:t=J","L:t^infinity=J"],"universal_comparison":universal_check}
(HERE/"dx1_saturation_audit_2026_10_07.json").write_text(json.dumps(metadata,indent=2)+"\n")
completed=subprocess.run(["/opt/homebrew/bin/M2","--script",str(m2_path)],cwd=ROOT,capture_output=True,text=True,check=True)
(HERE/"verify_dx1_saturation_2026_10_07.out").write_text(completed.stdout+completed.stderr)
print(completed.stdout,end="")
if completed.stderr:print(completed.stderr,end="")
print("DX=1 FIVE-COORDINATE SATURATION AUDIT VERIFIED OVER QQ")
