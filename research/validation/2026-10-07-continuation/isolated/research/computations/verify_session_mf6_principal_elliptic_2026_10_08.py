#!/usr/bin/env python3
"""Exact elliptic compression of the saved principal e1,d2=1 direction curve.

This verifies birational equation identities, not every contact matrix,
chart boundary, or an STCI exclusion. The polynomial H is copied literally
from session-mf6-e1-principal-contact-2026-10-08.json and root-compared.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

p, r, x, W, Y, XE, YE = s.symbols('p r x W Y XE YE')
H = (8*p**3-64*p**2*r**2-128*p**2*r-16*p**2
     +96*p*r**4+512*p*r**3+592*p*r**2+128*p*r+6*p
     -576*r**6-960*r**5-880*r**4-544*r**3-220*r**2-60*r-9)
A = -W**3+8*W**2-12*W+72
C = 2*(W**2-6*W+36)
quadratic = A*x*x-2*C*x+C
assert s.expand(H.subs({p:-2+4*x+W*x*x, r:x-s.Rational(1,2)})
                +8*x**4*quadratic) == 0
assert s.expand(C-A-W*W*(W-6)) == 0
assert s.expand((A*x-C)**2-C*(C-A)-A*quadratic) == 0
elliptic = Y*Y-2*(W-6)*(W*W-6*W+36)
assert s.cancel(quadratic.subs(x,(C+W*Y)/A)-W*W*elliptic/A) == 0
weierstrass = YE*YE-XE**3-96*XE+448
assert s.expand(weierstrass.subs({XE:2*(W-4),YE:2*Y})-4*elliptic) == 0
assert s.discriminant(2*(W-6)*(W*W-6*W+36),W) != 0
assert s.expand(H.subs(r,-s.Rational(1,2))-8*(p+2)**3) == 0
discriminant = -16*(4*96**3+27*448**2)
assert discriminant == -143327232
j_invariant = s.Rational(1728)*4*96**3/(4*96**3+27*448**2)
assert j_invariant == s.Rational(2048,3)

# On x!=0 the change (p,r)<->(W,x) is birational. The quadratic
# discriminant is 4*W² times a cubic with three distinct roots, so it
# is not a square even over algebraically closed characteristic-zero
# constants. No missing component lies on x=0, by H(-1/2,p) above.
# Thus H is geometrically integral, with genus-one normalization.
record = {
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'status':'PASS: exact equation identities; geometric integrality and genus-one normalization by the stated nonsquare argument',
    'H':str(H), 'shift':'x=r+1/2, W=(p+2-4x)/x^2',
    'elliptic':str(elliptic),
    'inverse':'x=(C+W*Y)/A; r=x-1/2; p=-2+4x+W*x^2',
    'A':str(A),'C':str(C),
    'weierstrass':'YE^2=XE^3+96*XE-448; XE=2(W-4),YE=2Y',
    'weierstrass_discriminant':discriminant,'j_invariant':str(j_invariant),
    'rational_map_open':'x*W*A!=0; excluded transformation charts remain in the original H curve',
    'retained':'No full quartic-rank-drop ideal exhaustion, exceptional chart closure, or mate exclusion is claimed.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: principal sextic direction curve is birational to YE^2=XE^3+96XE-448.')
print('PASS: discriminant=-143327232, j=2048/3; geometric genus is one.')
print('OPEN: full contact rank-drop locus, exceptional frames, and STCI/ancestor conclusions.')
