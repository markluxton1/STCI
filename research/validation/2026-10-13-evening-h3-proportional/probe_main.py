"""New h=3 conductor support probe; consumes the accepted primitive octic.

Does not replay conductor/module identities or old coefficient verifiers.
All symbols belong to QQ; every denominator restriction is recorded.
"""
from pathlib import Path
import json
import time
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
delta, lam, a, B, G, J, p = s.symbols('delta lam a B G J p')
source = ROOT / 'research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt'
F = s.sympify(source.read_text().replace('^', '**'), locals={str(x):x for x in [delta,a,B,G,J,p]})
aa = delta*(delta+2*lam-1)/(6*lam**2)
bb = 2*lam*aa
gg = delta*((lam-3)*delta+lam+1)/3
dd = delta*((lam**2-12)*delta+lam**2-2*lam+6)/6
BB = bb-aa
GG = gg-3*bb+2*aa
JJ = dd-2*gg+2*bb-aa
H = GG+(6*BB+delta**2-3*delta)*p+(3*aa-3*BB+2*delta)*p**2-2*aa*p**3
HC = s.Poly(s.cancel(-3*lam**2/delta*H), p).as_expr()
print('PHASE specialization', flush=True)
FC = s.Poly(F,p)
coeffs = [s.cancel(c.subs({a:aa,B:BB,G:GG,J:JJ})) for c in reversed(FC.all_coeffs())]
Fm = s.Poly(sum(c*p**i for i,c in enumerate(coeffs)),p,domain=s.QQ.frac_field(delta,lam))
Hm = s.Poly(H,p,domain=s.QQ.frac_field(delta,lam))
Sm = Fm.exquo(Hm)
SC = s.Poly(s.cancel(432*lam**4/delta**3*Sm.as_expr()),p).as_expr()
SC = s.Poly(SC,p).as_expr().expand()
(OUT/'main-H.txt').write_text(str(HC)+'\n')
(OUT/'main-S.txt').write_text(str(SC)+'\n')
data = {'coefficient_field':'QQ(delta,lam)', 'open_conditions':'delta != 0, lam != 0',
        'H_clear':str(HC),'S_clear':str(SC),'Jbar':str(s.factor(JJ)),
        'H_leading':str(s.factor(s.Poly(HC,p).LC())),
        'S_leading':str(s.factor(s.Poly(SC,p).LC())),
        'H_discriminant':str(s.factor(s.discriminant(HC,p)))}
(OUT/'main-artifacts.json').write_text(json.dumps(data,indent=2)+'\n')
print('H LEADING:',data['H_leading'],flush=True)
print('S LEADING:',data['S_leading'],flush=True)
print('H DISCRIMINANT:',data['H_discriminant'],flush=True)
print('PHASE resultant',flush=True)
then=time.monotonic()
res=s.factor(s.resultant(HC,SC,p))
data['resultant']=str(res)
data['resultant_seconds']=time.monotonic()-then
(OUT/'main-artifacts.json').write_text(json.dumps(data,indent=2)+'\n')
(OUT/'main-resultant.txt').write_text(str(res)+'\n')
print('H,S RESULTANT:',res,flush=True)
print('DONE resultant',flush=True)
