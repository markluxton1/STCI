"""New small algebra audit of the rational L2 cover; no old checker import."""
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
q, m, d, k = s.symbols("q m d k")
Pc = q**2 - 6*q + 6
D = 2*d*(q-1) + q*(q-2)
E = d**2 + d*(3*q-4) + q*(q-2)
L1 = 3*k*(q-1)**2*Pc + d*q*(3-2*q)*Pc - 3*d**2*(q-1)**2*(q-3)
L2 = (3*q*(q-1)*D*k**2 - 6*d*q*(q-1)*E*k
      + d**5*q + 3*d**4*(q-1)*(3*q-2)
      + 6*d**3*q*(q-1)*(2*q-3) + 3*d**2*q**2*(q-1)*(q-2))
dv = 3*(q-2)*Pc/(q*(q-1)*(3-m**2))
Dv = D.subs(d, dv)
Ev = E.subs(d, dv)
kv = dv*(Ev + m*dv**2/3)/Dv
H = (q**4*m**2 + 3*q**4*m - 3*q**3*m**2 - 3*q**4 - 15*q**3*m
     + 3*q**2*m**2 + 36*q**3 + 27*q**2*m - 144*q**2 - 18*q*m
     + 216*q - 108)
records = []

def check(label, expr):
    numerator = s.cancel(expr).as_numer_denom()[0]
    assert numerator == 0, (label, s.factor(numerator))
    records.append(label)
    print("PASS", label, flush=True)

check("complete compact L2 discriminant", s.discriminant(L2,k)
      - 12*q*(q-1)*d**5*(d*q*(q-1)-(q-2)*Pc))
check("rational-cover L2 equation", L2.subs({d:dv,k:kv}))
check("rational-cover inverse m", 3*(Dv*kv/dv-Ev)/dv**2-m)
check("rational-cover D factor", Dv
      -(q-2)*(q*m-3*q+6)*(q*m+3*q-6)/(q*(m**2-3)))
check("rational-cover L1 and H identity", L1.subs({d:dv,k:kv})
      +3*m*(q-2)*Pc**2*H/(q**2*(q-1)*(m**2-3)**2*(q*m+3*q-6)))
d0 = -q*(q-2)/(2*(q-1))
k0 = -q*(q-2)*(7*q**2-12*q+6)/(24*(q-1)**3)
check("D-zero actual k solve", L2.subs({d:d0,k:k0}))
check("D-zero nonzero linear coefficient", s.diff(L2,k).subs(d,d0)
      + 3*q**3*(q-2)**4/(4*(q-1)**2))
V = 5*q**4-30*q**3+66*q**2-72*q+36
check("D-zero L1 and V identity", L1.subs({d:d0,k:k0})
      +q*(q-2)*V/(8*(q-1)))
check("q-two full discriminant", s.discriminant(L2,k).subs(q,2)-48*d**6)
print(json.dumps({"new_identity_count":len(records),
                  "accepted_verifiers_rerun":False,
                  "checks":records},indent=2))
(Path(__file__).parent/"l2-cover-algebra-result.json").write_text(
    json.dumps({"scope":"New rational-cover identities only; no inherited octic verification",
                "new_identity_count":len(records),"checks":records,
                "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2)+"\n")
