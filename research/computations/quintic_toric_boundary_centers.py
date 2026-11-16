"""Exact exclusion of the one-infinity center boundary for the toric source.

No finite-center resultant or generic-condition exception is used.
"""
import json
import sys
import sympy as sp

r, t, ell, z = sp.symbols("r t ell z")
A = t + 3*r*ell
B = t**3*(t+1)
C = t**2*(t+1) + ell
D = t*(t+1) + (1+3*r)*ell
E = (t+1)**2 + (1+6*r+6*r**2)*ell
Q = sp.expand(B*D-C**2)
R = sp.expand(A*E*C-D**3)
T = sp.expand(A*B*E-C*D**2)
H = (1+3*r)*t**2-2*t
Lam = t*(t+1)*H
assert sp.factor(Q-ell*(Lam-ell)) == 0

# On the nonmarked Q=0 branch, ell=Lam. These are the exact residual
# equations after removing their common factor ell.
FR = sp.cancel((R/ell).subs(ell, Lam))
FT = sp.cancel((T/ell).subs(ell, Lam))
W = ((27*r**4+36*r**3+27*r**2+9*r+1)*t**5
     +(27*r**4-9*r**3-18*r**2-12*r-2)*t**4
     +(-45*r**3-9*r**2+1)*t**3
     +(30*r**2+6*r+1)*t**2+(-9*r-1)*t+1)
assert sp.factor(FR-t*(t+1)*W*(1-(3*r+1)*t)) == 0
assert sp.factor(FT+t**2*(t+1)*W) == 0
assert W.subs(t,0) == 1
pA = 3*r+1
pB = 9*r**3+9*r**2+6*r+1
pC = 6*r**2+6*r+1
pD = 9*r**3+21*r**2+15*r+11
assert sp.factor(W.subs(t,-1)+pC) == 0
assert sp.factor(sp.resultant(W,H,t)-pA**2*pD) == 0

# Generic parameters have degree(W)=5, W has no support at 0,-1 or H=0,
# so any root of W gives a finite nonmarked inverse point.
assert sp.factor(sp.Poly(W,t).LC()-pA*(9*r**3+9*r**2+6*r+1)) == 0

# The only exceptional irreducible parameter factors are these four.
factors = [pA, 9*r**3+9*r**2+6*r+1, pC, pD]
expected = [(4,0), (4,0), (5,1), (5,1)]
for i in range(len(factors)):
    for j in range(i):
        assert sp.gcd(factors[i],factors[j]) == 1
records = []
for p, (expected_wdeg, expected_support_gcd_degree) in zip(factors, expected):
    fac = sp.factor_list(p)[1]
    assert len(fac) == 1 and fac[0][1] == 1 and sp.degree(fac[0][0],r) == sp.degree(p,r)
    if sp.degree(p,r) == 1:
        alpha = sp.solve(p,r)[0]
        extension = None
    else:
        alpha = sp.CRootOf(p,r,0)
        extension = alpha
    Wp = sp.Poly(W.subs(r,alpha),t,extension=extension)
    Lamp = sp.Poly(Lam.subs(r,alpha),t,extension=extension)
    # All roots of Lambda have multiplicity at least one. Since deg(W)<=5,
    # support(W) subset support(Lambda) iff W divides Lambda^5.
    support_gcd = Wp.gcd(Lamp**5)
    wdeg, gdeg = Wp.degree(), support_gcd.degree()
    assert (wdeg,gdeg) == (expected_wdeg,expected_support_gcd_degree)
    assert gdeg < wdeg
    records.append({
        "factor":str(p),
        "irreducible_over_Q":True,
        "degree_W":wdeg,
        "degree_gcd_W_Lambda5":gdeg,
        "root_of_W_outside_Lambda_support":True,
    })

# The t=infinity target is [1:0:0:0]. Its fiber line through the marked
# point (0:1:0:0:0) and P(r), normalized with B=1, is
# (A,B,C,D,E)=(3rz,1,z,dz,ez).
d = 1+3*r
a = 3*r
e = 1+6*r+6*r**2
p_infty = sp.expand(d**3-a*e)
assert sp.factor(p_infty-pB) == 0
Qinf = sp.expand(z*(d-z))
Rinf = sp.expand(z**3*(a*e-d**3))
Tinf = sp.expand(z**2*(a*e-d**2*z))
# In Q[r,z], gcd of the fiber equations records only generic support;
# specializations are stated by their exact factors below.
assert sp.factor(Qinf-z*(d-z)) == 0
assert sp.factor(Rinf+z**3*pB) == 0
# If pB=0, d is nonzero and z=d is an extra point. If r=-1/3 then d=0
# and the fiber ideal is (z^2). At all other finite r it is (z).
r_special = sp.Rational(-1,3)
assert sp.factor(d.subs(r,r_special)) == 0
assert sp.factor(pB.subs(r,r_special)) != 0
assert sp.factor(sp.gcd(sp.gcd(Qinf.subs(r,r_special),Rinf.subs(r,r_special),z),
                        Tinf.subs(r,r_special),z)-z**2) == 0
assert sp.factor(sp.gcd(sp.gcd(Qinf.subs(r,0),Rinf.subs(r,0),z),
                        Tinf.subs(r,0),z)-z) == 0
# On pB=0, common root z=d (and d!=0 since pB(-1/3)!=0).
assert sp.factor((Qinf.subs(z,d))) == 0
assert sp.factor(Rinf.subs(z,d)+d**3*pB) == 0
assert sp.factor(Tinf.subs(z,d)+d**2*pB) == 0

print(json.dumps({
    "python":sys.version.split()[0],
    "sympy":sp.__version__,
    "K":-1,
    "W_coefficients_low_to_high":[str(sp.factor(sp.Poly(W,t).nth(i))) for i in range(6)],
    "exact_residual_identities":{"FR":"t*(t+1)*W*(1-(3*r+1)*t)",
                                  "FT":"-t^2*(t+1)*W"},
    "exceptional_specializations_support_test":records,
    "infinity_fiber":{"coordinates":"(3*r*z,1,z,(1+3*r)*z,(1+6*r+6*r^2)*z)",
       "equations":["z*(d-z)","-z^3*pB","z^2*(a*e-d^2*z)"],
       "pB_zero":"extra point z=d; d!=0",
       "r_minus_one_third":"ideal (z^2), marked point only",
       "other_finite_r":"ideal (z), marked point only"},
    "r_infinity":"center limit [0:0:0:0:1] lies on X, inadmissible",
    "conclusion":"every admissible one-infinity boundary parameter has an extra inverse point; finite-t residual W handles all r, and t=infinity independently gives an extra point when pB=0",
},indent=2))
