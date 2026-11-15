# Toric quintic centers: full inverse support and the remaining incidence

Status: **independently reviewed partial exclusion**, with
an unfinished final parameter locus. Fix the embedded rational quartic
`C0=[u^4:u^3v:uv^3:v^4]` over an algebraically closed field of characteristic
zero. This closes out the calculation already in progress; it does not
exclude every toric quintic normalization or settle unrestricted STCI.

## 1. Geometric object and scope

The [marked-source proof, §§4.1–4.2](quintic_non_gorenstein_toric_sources.md)
reduces every hypothetical toric quintic normalization, together with its
marked quartic, to the normal surface in P4

    X: BD-C^2 = AEC-D^3 = ABE-CD^2 = 0,
    c(t)=(t,t^3(t+1),t^2(t+1),t(t+1),(t+1)^2).

The marked curve includes its projective point at infinity. There is an
actual section `q in H0(X,4H)` with `div(q)=5c`; every possible mate pulls
back to a power of q. A projection must be finite and birational and map
c isomorphically to fixed C0. An extra point of X outside c mapping into
C0 prevents every such power from descending. This is a full inverse-support
test, not a count of a residual curve in an ambient intersection. The
[fixed-carrier criterion](../../results/fixed_carrier_conductor_criterion.md)
supplies the implication to every mate degree.

The possible centers preserving the marked image form the PGL2 orbit of
the missing-middle-coordinate center of the rational normal quartic.
A finite distinct pair and a one-infinity pair cover this orbit. Coincident
pairs lie on c and are inadmissible centers. We test all admissible centers
in these charts, without replacing exceptional parameters by a generic one.

## 2. Finite-pair chart and certified exclusions

For distinct finite r,q put `m=r+q`, `n=rq`, `Delta=m^2-4n !=0`.
The source center `P=(a,b,c,d,e)` is

    a=3mn, b=3(m+2), c=m^2+2n+3m,
    d=m^2+2n+3mn, e=m^2+2n+6mn+6n^2.

Here c in this coordinate list is a scalar, not the marked curve. Set

    K=bd-c^2=-Delta*K0,   K0=m^2-n+3m+3,
    h(t)=dt^2-2ct+b,      D(t)=t(t+1)h(t).

On the fiber line `c(t)+lambda P`, the quadric equation is
`lambda(D+lambda K)=0`. For K nonzero the nonmarked branch is
`lambda=-D/K`. The residual polynomial W is preserved by its six exact
coefficients in the [finite-center input](../../computations/quintic_toric_finite_centers.json),
produced by the [finite-center certificate](../../computations/quintic_toric_finite_centers.py).
It satisfies

    W_5=d*N, W(0)=K0*U0, W(-1)=-K0*V1*V2,
    Res_t(W,h)=Delta^4*d^2*K0^3*M,   R(P)=-Delta*N,

where

    N=m^4+6m^3n+9m^2n^2+m^2n+9mn^3-6mn^2-2n^2,
    U0=m^4+4m^2n+4n^2+3m^3+6mn+3m^2-12n,
    V1=m^2+2n+6m+6,
    V2=m^2+2n+6mn+6n^2,
    M=11m^4+15m^3n+36m^3+21m^2n^2+8m^2n+39m^2
      +9mn^3+30mn^2-45mn+27m+6n^3+8n^2-30n+18.

The geometric meaning of a root of W outside `D=0` is an actual extra
inverse point: the resulting lambda is nonzero and all three equations
of X vanish. Thus `d*N*U0*V1*V2*M !=0` excludes full inverse support.
The factor M is essential; an earlier diagnostic omitted it and was
corrected before acceptance.

The following boundary arguments are also certified.

| Parameter locus | Actual reason for exclusion |
| --- | --- |
| `K=0` | `n=m^2+3m+3`. For `m != -1,-2`, take `t=1/(m+1)` and `lambda=-t^2(t+1)/c`; the resulting point has B=C=D=0 and lies on X outside c. The diagonal case m=-2 is inadmissible. At `(m,n)=(-1,1)`, take t=0 and lambda=-1/3, obtaining `[1:-1:0:0:0]`. |
| `K !=0, d !=0, N=0` | At the marked point at infinity, `Q=lambda(d+lambda K)` and `R=lambda^3 R(P)`. The nonzero root `lambda=-d/K` also satisfies T by the toric syzygy, giving an extra point. |
| `K !=0, d=0` | Substitute `n=-m^2/(3m+2)`. W has degree four on the retained locus. Full support would require `W | D^5`. The remainder-coefficient numerator gcd is `243(m+2)^5`, whose only root is diagonal. All denominator zeros are outside the retained locus. |

After these tests, the initially certified remaining finite locus is

    Delta*K0*d*N !=0,   U0*V1*V2*M=0.                 (1)

## 3. The entire one-infinity boundary is excluded

Here

    P(r)=(3r,0,1,1+3r,1+6r+6r^2), K=-1,
    h=(1+3r)t^2-2t, D=t(t+1)h.

The [boundary certificate](../../computations/quintic_toric_boundary_centers.py)
uses exact identities on `lambda=D`:

    (R/lambda)=t(t+1)W_b[1-(3r+1)t],
    (T/lambda)=-t^2(t+1)W_b.

The polynomial W_b has constant coefficient one, leading coefficient
`(3r+1)(9r^3+9r^2+6r+1)`, value
`W_b(-1)=-(6r^2+6r+1)`, and resultant with h equal to
`(3r+1)^2(9r^3+21r^2+15r+11)`. Away from these four parameter factors,
any root supplies an extra point. The complete exceptional tests give:

| Parameter factor | Degree of W_b | Degree of gcd(W_b,D^5) |
| --- | ---: | ---: |
| `3r+1` | 4 | 0 |
| `9r^3+9r^2+6r+1` | 4 | 0 |
| `6r^2+6r+1` | 5 | 1 |
| `9r^3+21r^2+15r+11` | 5 | 1 |

Each factor is irreducible over Q and the factors are pairwise coprime;
the exact number-field computations therefore cover every conjugate
parameter in characteristic zero. The strict degree inequality supplies
an extra root in every case. The support test uses D^5 rather than D,
so repeated roots are retained.

The projective marked endpoint was separately checked with fiber coordinates
`(3rz,1,z,(1+3r)z,(1+6r+6r^2)z)`. It has an extra point when
`9r^3+9r^2+6r+1=0`; at r=-1/3 the fiber is a double point supported
on c. The limiting center r=infinity is `[0:0:0:0:1]` on X and is
inadmissible. These endpoint checks do not replace the finite-t argument.

## 4. Three exceptional curves and the uncompleted locus

For nonzero W in characteristic zero, the exact elementary criterion is

    Supp V(W) subset Supp V(D)  iff  W divides D*W'.     (2)

At a root of multiplicity e, W' has order e-1. This explains both
necessity and sufficiency and why characteristic zero matters; it is
not a characteristic-independent support certificate.

The [three-curve calculation](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_centers.py)
uses (2) on U0, V1 and V2. The independent source closeout review **passes**:
all three curves are excluded on `Delta*K0*d*N !=0`. It supplies the
[separate specialization audit](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_audit.py)
and the following complete evidence, rather than inferring coverage from a
generic remainder.

Write the source equations on the fiber line as R and T, distinguishing
the coordinate D of P4 from the polynomial D(t). The exact identities are

    K^2 (R/lambda)|_(lambda=-D/K) = -Delta*t(t+1)*W*(dt-c),
    K^2 (T/lambda)|_(lambda=-D/K) = -Delta*t(t+1)*W*(ct-b).

The two linear cofactors have resultant `c^2-bd=-K !=0`. Thus the
specialized residual gcd after the universal endpoint factors is exactly
W up to a unit at every retained point, not only generically.

The parameterizations and numerator-gcd tests are:

| Curve | Parameterization | Gcd of numerator coefficients of rem(D W',W) |
| --- | --- | --- |
| V1 | `m=k, n=-(k^2+6k+6)/2` | `81(k+2)^4` |
| V2, m nonzero | `m=-2k/q, n=km`, `q=6k^2+6k+1` | `81(2k+1)^4(10k^2+6k+1)` |
| U0, m nonzero | `m=-12(k+3)/p`, `x=6+(k-3)m/2`, `n=(x-m^2)/2`, `p=k^2+27` | `139968(k-3)^3(k+3)(k^2-12k+63)` |

Every root of these gcds has Delta=0 or K0=0. The V1 graph is complete.
For V2 with m nonzero, k=n/m gives `mq+2k=0`; q=0 would also force k=0,
so its poles give no affine center. The m=0 points are `(0,0)`, excluded
by Delta, and `(0,-1/3)`, whose separately computed remainder has
coefficient-numerator gcd 800 and is nonzero. For U0 put
`x=m^2+2n`, `y=2x+3m-6`; then
`y^2+27m^2+36m-36=4U0`. With m nonzero, `k=(y-6)/m` gives
`pm+12(k+3)=0`. Its poles again give no finite center. The two m=0
points are `(0,3)` with K0=0 and `(0,0)` with Delta=0.

For explicit denominator coverage, define

    A1=k^2+4k+2,
    B1=k^6+14k^5+78k^4+212k^3+276k^2+144k+8,
    A0=k^3-3k^2+99k+135,
    B0=k^9+3k^8+144k^7+648k^6+15066k^5-30618k^4
       +577368k^3-1714608k^2-6528195k+27497151.

| Curve | Leading coefficient of W (dN) | Common denominator of canceled remainder coefficients, up to rational units |
| --- | --- | --- |
| V1 | `27(k+2)^2 A1 B1/16` | `8 A1 B1^3` |
| V2 | `1728 k^10(2k+1)^2/q^6` | `k^3 q^8` |
| U0 | `5038848(k-3)^2 A0 B0/p^10` | `p^10 A0 B0^3` |

All additional denominator zeros lie on dN=0, on an excluded Delta=0
point, or at parameter poles with no affine center. W therefore has
degree five throughout the retained open set, division commutes with
specialization there, and no degree-drop point was silently omitted.

The remaining finite incidence is consequently

    M=0, Delta*K0*d*N*U0*V1*V2 !=0,
    W divides h*W'.                                      (3)

The omitted t(t+1) factor in (3) is invertible on Supp(W), by the
nonzero U0,V1,V2 conditions. The infinity fiber is already controlled
by N nonzero. The quadratic h has two distinct roots, since its
discriminant is `4(c^2-bd)=-4K !=0`. Thus (3) is equivalently

    W=gamma*(t-alpha)^j*(t-beta)^(5-j), j=0,...,5,

where alpha,beta are those two roots and gamma is nonzero. Up to their
exchange there are three multiplicity patterns, 5+0, 4+1 and 3+2.
Geometrically all five residual-polynomial roots would have to coalesce
at the two parameters where the nonmarked branch returns to the marked
point. These are candidate full-support configurations, not demonstrated
centers or residual components downstairs. This is a useful formulation
for a later bounded test, not a completed classification of (3).

The unfinished M calculation must be kept separate. A previous scratch
run formed the remainder of D W' modulo W, found coefficient numerators
of degree 22 and their scalar gcd with M equal to one, then stopped
before the multivariate Groebner calculation completed. The process was
cancelled at the user's earlier closeout request. A gcd of one in two
variables proves neither an empty common zero locus nor finiteness.
There is no certified classification of M, no surviving admissible center,
and no STCI construction from this calculation. The temporary unfinished
program has no continuing consumer; the exact input W and condition (2)
preserve the mathematical question.

## 5. Exact evidence and integration scope

The proof and five exact support files are selectively preserved from commit
`61290bdf906aa419c9542732f32fdcc34ba338a1`. The finite chart, boundary,
three exceptional curves and specialization audit keep their original formulas
and characteristic-zero hypotheses. This integration makes no new mathematical
deduction. Independent preservation and scope
review passed without a material finding, by direct comparison to the fixed
source and all five exact support files. This review made no fresh CAS replay;
the unchanged source arguments retain the reviews described below.

The independent source implementation review checked the finite chart and
corrected one-infinity calculation and executed them with Python 3.15.2 /
SymPy 1.14.0, exit zero. The retained finite copy differed only in execution
metadata and removal of an unused no-op; the boundary copy was byte-identical
to that reviewed version. The support lemma (2) separately received mathematical
reconstruction. A fresh independent closeout review reconstructed the final
written §§1–4, including the K=0 points, universal residual-factor identities,
parameter coverage, denominator and leading-coefficient specializations, endpoints
and exact remaining multiplicity patterns. It found no material correction.
That reviewer executed the retained three-curve program and retained independent
specialization audit with Python 3.15.2 / SymPy 1.14.0, both exit zero; the
latter ended in PASS. No M-locus calculation was performed or certified.

| Exact retained support | SHA-256 |
| --- | --- |
| [Finite-center program](../../computations/quintic_toric_finite_centers.py) | `091e9b878f2dbb3b4cca64cac3e366449111dc26305936a13330da516ba05e80` |
| [Finite-center JSON input](../../computations/quintic_toric_finite_centers.json) | `924bc8245c2b9cbee76f98862e7e304e9aecb32c4d2a96279666734f10a5b6ec` |
| [One-infinity boundary program](../../computations/quintic_toric_boundary_centers.py) | `6de86103d9539039366cee0d99693b06f7d2eed511dad4566bb5233ac6a420b5` |
| [Three-curve program](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_centers.py) | `46a86f93c6aec48a8a79ec897bb60203d226cb27a263435cb4dfae863208016f` |
| [Independent specialization audit](https://github.com/markluxton1/STCI/blob/719e47f452b5286a794731637df5c086b068bad5/research/computations/quintic_toric_exception_audit.py) | `4d2b338367b09858427bcf8f036b5ffe64d39570bc9add8809198607618cdd00` |

The JSON preserves the six coefficients of W and the earlier four-curve gate
(1). Its remaining-incidence field describes that stage of the calculation;
§4 gives the later reviewed exclusion of U0,V1,V2. The JSON is an exact input,
not an independent statement that all four curves are still open. Both the
three-curve program and audit read the sibling JSON; no temporary input is
needed. The audit additionally prints the three-curve program's hash. The
finite and boundary programs are otherwise self-contained apart from SymPy
and the Python standard library.

For reproduction, use Python with SymPy and run these individual scripts from
`research/computations/`. This integration checks exact source-byte preservation
and dependencies; it does not claim a fresh CAS replay. The source closeout's
captured three-curve output SHA-256 was
`e11e46536605ea9153e71be7e52a06d1bd5cade48929368e06f17deee51fe94f`;
the specialization-audit output SHA-256 was
`5f0a79542fb6f4a95c7886108fbc81a4d8b6b4bf87c17bdb11a14cd90db563f6`.
These identify the source executions, not executions in this integration.

The result is a partial exclusion for the exhaustive toric quintic-source
reduction. It leaves (3) unresolved and does not imply a complete toric-quintic
exclusion, a classification of non-Gorenstein quintic normalizations, or an
unrestricted characteristic-zero STCI conclusion. Even a surviving full-support
center would still require actual descent of a pure power q^N through its
projection/conductor algebra.


### Archived exact certificate: `research/computations/quintic_toric_exception_audit.py`

The following is the original computational certificate, preserved verbatim. Its stated scope and caveats remain in force; archiving does not independently validate or broaden its claims.

<details><summary>Original source</summary>

```python
"""Independent specialization audit for the three exceptional center curves.

Print exact denominator, leading-coefficient and parameter-boundary evidence;
verify the universal residual-factor identities used by the companion note.
No calculation on the remaining M locus is performed.
"""
import json, sympy as s, hashlib
from pathlib import Path
m,n,k,t,l=s.symbols('m n k t l')
p=Path(__file__).with_name('quintic_toric_finite_centers.json')
audit=Path(__file__).with_name('quintic_toric_exception_centers.py')
print('SHA256_INPUT',hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
print('SHA256_SCRIPT',hashlib.sha256(audit.read_bytes()).hexdigest(),flush=True)
data=json.loads(p.read_text()); W=s.expand(sum(s.sympify(v,locals={'m':m,'n':n})*t**int(i) for i,v in data['generic_W_coefficients_low_to_high'].items()))
Delta=m*m-4*n; K0=m*m-n+3*m+3; d=m*m+2*n+3*m*n
N=m**4+6*m**3*n+9*m*m*n*n+m*m*n+9*m*n**3-6*m*n*n-2*n*n
H=d*t*t-2*(m*m+2*n+3*m)*t+3*(m+2); D=t*(t+1)*H
subs={'V1':{m:k,n:-(k*k+6*k+6)/2},'V2':{m:-2*k/(1+6*k+6*k*k),n:-2*k*k/(1+6*k+6*k*k)}}
mu=-12*(k+3)/(k*k+27); xu=6+(k-3)*mu/2
subs['U0']={m:mu,n:s.factor((xu-mu*mu)/2)}
for name,sub in subs.items():
 print(name,'m,n',*[str(s.factor(sub[x])) for x in (m,n)],flush=True)
 for expr,label in ((Delta,'Delta'),(K0,'K0'),(d,'d'),(N,'N'),(d*N,'LC_W')):
  print(name,label,s.factor(expr.subs(sub)),flush=True)
 w=s.Poly(s.cancel(W.subs(sub)),t); z=s.Poly(s.cancel((D*s.diff(W,t)).subs(sub)),t)
 rem=s.Poly(s.rem(z,w),t)
 den=s.factor(s.lcm_list([s.fraction(s.cancel(c))[1] for c in rem.all_coeffs()]))
 print(name,'W_degree',w.degree(),'W_coeff_den_lcm',s.factor(s.lcm_list([s.denom(s.cancel(c)) for c in w.all_coeffs()])),flush=True)
 print(name,'REM_den_lcm',den,flush=True)
 nums=[s.fraction(s.cancel(c))[0] for c in rem.all_coeffs()]
 print(name,'REM_num_gcd',s.factor(s.gcd_list(nums)),flush=True)
print('PARAM_POLE_GCD_U0',s.gcd(k*k+27,k+3),flush=True)
print('PARAM_POLE_GCD_V2',s.gcd(1+6*k+6*k*k,k),flush=True)
a=3*m*n; b=3*(m+2); c=m*m+2*n+3*m; e=m*m+2*n+6*m*n+6*n*n; K=-Delta*K0
Ac=t; Bc=t**3*(t+1); Cc=t*t*(t+1); Dc=t*(t+1); Ec=(t+1)**2
A=Ac+l*a; B=Bc+l*b; C=Cc+l*c; DD=Dc+l*d; E=Ec+l*e
for name,expr in [('R',A*E*C-DD**3),('T',A*B*E-C*DD**2)]:
 poly=s.Poly(s.expand(expr),l)
 assert poly.nth(0)==0
 cleared=s.expand(K*K*poly.nth(1)-K*D*poly.nth(2)+D*D*poly.nth(3))
 quo,rem=s.div(cleared,s.expand(t*(t+1)*W),t)
 assert s.expand(rem)==0
 print('UNIVERSAL_FACTOR',name,'K^2*(equation/l) at l=-D/K = t(t+1)W *',s.factor(quo),flush=True)

# Complete affine parameter coverage and the separately tested omitted point.
assert s.factor(s.Poly(W,t).LC()-d*N)==0
U0=m**4+4*m*m*n+4*n*n+3*m**3+6*m*n+3*m*m-12*n
V1=m*m+2*n+6*m+6; V2=m*m+2*n+6*m*n+6*n*n
for name,eq in [('U0',U0),('V1',V1),('V2',V2)]:
 assert s.factor(eq.subs(subs[name]))==0
 print(name,'param_identity=0')
x=m*m+2*n; y=2*x+3*m-6
assert s.expand(y*y+27*m*m+36*m-36-4*U0)==0
print('U0 conic transform exact')
for name,pt in [('U0_base',{m:0,n:3}),('U0_infinity',{m:0,n:0}),('V2_origin',{m:0,n:0}),('V2_omitted',{m:0,n:-s.Rational(1,3)})]:
 print(name,'Delta,K0,d,N=',*[str(s.factor(e.subs(pt))) for e in [Delta,K0,d,N]])
 if name=='V2_omitted':
  w=s.Poly(W.subs(pt),t); z=s.Poly((D*s.diff(W,t)).subs(pt),t)
  rem=s.rem(z,w)
  print('W_omitted=',s.factor(w.as_expr()))
  print('D_omitted=',s.factor(D.subs(pt)))
  print('REM_omitted=',s.factor(rem.as_expr()))
  print('GCD_numerators=',s.gcd_list([s.fraction(s.cancel(c))[0] for c in rem.all_coeffs()]))
print('PASS')
```
</details>


### Archived exact certificate: `research/computations/quintic_toric_exception_centers.py`

The following is the original computational certificate, preserved verbatim. Its stated scope and caveats remain in force; archiving does not independently validate or broaden its claims.

<details><summary>Original source</summary>

```python
"""Root-support diagnostics on U0, V1, V2; M remains unresolved.

Review status and remaining coverage are recorded in the companion research note.
"""
import json,sys,sympy as s
from pathlib import Path
m,n,t,k=s.symbols('m n t k')
data=json.loads(Path(__file__).with_name('quintic_toric_finite_centers.json').read_text())
W=s.expand(sum(s.sympify(v,locals={'m':m,'n':n})*t**int(i)
               for i,v in data['generic_W_coefficients_low_to_high'].items()))
d=m**2+2*n+3*m*n
H=d*t**2-2*(m**2+2*n+3*m)*t+3*(m+2)
D=t*(t+1)*H
Delta=m**2-4*n; K0=m**2-n+3*m+3
N=m**4+6*m**3*n+9*m**2*n**2+m**2*n+9*m*n**3-6*m*n**2-2*n**2
U0=m**4+4*m**2*n+4*n**2+3*m**3+6*m*n+3*m**2-12*n
V1=m**2+2*n+6*m+6
V2=m**2+2*n+6*m*n+6*n**2

def support_rem_gcd(sub):
    w=s.Poly(s.cancel(W.subs(sub)),t,domain='EX')
    z=s.Poly(s.cancel((D*s.diff(W,t)).subs(sub)),t,domain='EX')
    rem=s.rem(z,w)
    nums=[s.fraction(s.cancel(c))[0] for c in rem.all_coeffs()]
    return s.factor(s.gcd_list(nums)), s.factor(w.as_expr())

# In characteristic zero, for nonzero W, Supp(W) subset Supp(D)
# iff W divides D*W': at a root of W of multiplicity e, W' has order e-1.
# V1 is a graph over m.
g1,w1=support_rem_gcd({m:k,n:-(k**2+6*k+6)/2})
assert s.factor(g1-81*(k+2)**4)==0 and s.Poly(g1,k).degree()>0
assert s.factor(g1-81*(k+2)**4)==0
v1cand={m:-2,n:s.Integer(1)}
assert s.factor(Delta.subs(v1cand))==0

# V2 conic from (0,0); handle m=0 separately.
sub2={m:-2*k/(1+6*k+6*k**2),n:-2*k**2/(1+6*k+6*k**2)}
g2,w2=support_rem_gcd(sub2)
assert s.factor(g2-81*(2*k+1)**4*(10*k**2+6*k+1))==0
v2zero={m:0,n:0}; v2half={m:-2,n:1}
assert s.factor(Delta.subs(v2zero))==0 and s.factor(Delta.subs(v2half))==0
root_poly=10*k**2+6*k+1
mroot=s.factor(sub2[m]); nroot=s.factor(sub2[n])
assert s.rem(s.together(K0.subs({m:mroot,n:nroot})).as_numer_denom()[0],root_poly,k)==0
v2miss={m:0,n:-s.Rational(1,3)}
assert s.factor(V2.subs(v2miss))==0
miss_gcd,wm=support_rem_gcd(v2miss)
assert miss_gcd==800

# U0 conic rational parametrization from the point (m,n)=(0,3).
# Let x=m^2+2n, y=2x+3m-6, then y^2=-27m^2-36m+36 and y=6+k*m.
mu=s.factor(-12*(k+3)/(k**2+27))
yu=s.factor(6+k*mu)
xu=s.factor(6+(k-3)*mu/2)
nu=s.factor((xu-mu**2)/2)
assert s.factor(U0.subs({m:mu,n:nu}))==0
g0,w0=support_rem_gcd({m:mu,n:nu})
assert s.factor(g0-139968*(k-3)**3*(k+3)*(k**2-12*k+63))==0
assert s.factor(g0.subs(k,3))==0 and s.factor(g0.subs(k,-3))==0
ucand={m:-2,n:1}
assert s.factor(Delta.subs(ucand))==0
u_tangent={m:0,n:3}; u_infty={m:0,n:0}
assert s.factor(K0.subs(u_tangent))==0 and s.factor(Delta.subs(u_infty))==0
Knum=s.together(K0.subs({m:mu,n:nu})).as_numer_denom()[0]
assert s.rem(Knum,k**2-12*k+63,k)==0

out={
 'execution':{'command':f'python3 {__file__}',
              'python':sys.version.split()[0],'sympy':s.__version__},
 'root_support_criterion':'In char 0, for nonzero W and D=t(t+1)H, Supp(W) subset Supp(D) iff W divides D*dW/dt. For each root alpha of multiplicity e in W, ord_alpha(Wprime)=e-1, so divisibility is equivalent to D(alpha)=0.',
 'U0':{'param':'m=-12(k+3)/(k^2+27), x=m^2+2n, y=2x+3m-6=6+km, n=(x-m^2)/2',
       'coefficient_gcd_of_remainder_DWprime_mod_W':str(g0),'candidate_roots':'k=3 gives (m,n)=(-2,1), Delta=0; k=-3 gives (0,3), K0=0; roots of k^2-12k+63 have K0=0',
       'parameter_boundary':'k tends to infinity at the affine point (m,n)=(0,0), where Delta=0; k^2+27=0 are parameter poles and give no finite affine center'},
 'V1':{'param':'m=k, n=-(k^2+6k+6)/2','coefficient_gcd_of_remainder_DWprime_mod_W':str(g1),
       'only_candidate':'k=-2 gives (m,n)=(-2,1), Delta=0'},
 'V2':{'param':'m=-2k/(1+6k+6k^2), n=km (covers m!=0)',
       'coefficient_gcd_of_remainder_DWprime_mod_W':str(g2),
       'candidate_roots':'k=-1/2 gives (-2,1), Delta=0; roots of 10k^2+6k+1 have K0=0; k=0 is not a zero of the remainder gcd',
       'omitted_affine_point':{'point':'(m,n)=(0,-1/3)','coefficient_gcd_of_remainder_DWprime_mod_W':str(miss_gcd),'W_specialized':str(wm)}},
 'conclusion':'The specialized universal W fails the root-support criterion at every point of U0,V1,V2 satisfying the reviewed open conditions Delta*K0*d*N!=0. At the only candidate roots, a displayed open-condition factor vanishes. M=0 remains unresolved; no finiteness or emptiness conclusion is certified by this script.',
 'scope':'Finite distinct-pair chart only; separate one-infinity chart untouched.'}
print(json.dumps(out,indent=2))
```
</details>


## Consolidated historical supplement: `research/supplements/NONENDPOINT_SINGLE_ROOT_INCIDENCE.md`

**Complete development: [extracted_nonendpoint_single_root_incidence.md](extracted_nonendpoint_single_root_incidence.md).** Original headings below remain as compatibility anchors; the linked file retains the full proof and hypotheses.

# Nonendpoint single-root incidence and actual quotient fibers

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## The regular L1 double conductor root

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## The two quotient fibers and the diagonal exception

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 1. Hypotheses and inherited actual fiber system

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 2. A linear/quadratic quotient and its normalized common-root norm

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 3. Solving the allowed diagonal exception without losing P6=0

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 4. L2 is a different, diagonal Jacobian factor

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## All Taylor coefficients and the target-zero stratum

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 1. Exact finite common-root parameters

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 2. All eight exact Taylor coefficients and the seven necessary equations

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 3. A compact first-coefficient factorization

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

### 4. The target-z=0 common-root stratum has a simple conductor zero

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## Exact support and characteristic scope

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## Reviewed geometric bridges for the regular sole-root branches

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## 7. Regular L2: geometric elimination cover and retained exceptional loci

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## 8. Independent review of the existing regular-L1 geometric bridge

[Full mathematical section](extracted_nonendpoint_single_root_incidence.md).

## Consolidated historical supplement: `research/supplements/QUINTIC_H2_INCIDENCE_AND_LOCALCOH_FRONTIER.md`

**Complete development: [extracted_quintic_h2_incidence_and_localcoh_frontier.md](extracted_quintic_h2_incidence_and_localcoh_frontier.md).** Original headings below remain as compatibility anchors; the linked file retains the full proof and hypotheses.

# Quintic H2: the degree-five necessary incidence and its open boundary

[Full mathematical section](extracted_quintic_h2_incidence_and_localcoh_frontier.md).

## Actual coordinates, domain and common-factor equations

[Full mathematical section](extracted_quintic_h2_incidence_and_localcoh_frontier.md).

## The valid degree-five ODE and fixed A4 zero

[Full mathematical section](extracted_quintic_h2_incidence_and_localcoh_frontier.md).

## Why the proposed eliminations do not close the branch

[Full mathematical section](extracted_quintic_h2_incidence_and_localcoh_frontier.md).

## Review scope

[Full mathematical section](extracted_quintic_h2_incidence_and_localcoh_frontier.md).

### Archived exact certificate: `research/computations/verify_session_nonendpoint_h2_classification_2026_10_13.m2`

[Full mathematical section](extracted_quintic_h2_incidence_and_localcoh_frontier.md).

## Consolidated historical supplement: `research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md`

**Complete development: [extracted_quintic_h2_monic_ode_and_open_incidence.md](extracted_quintic_h2_monic_ode_and_open_incidence.md).** Original headings below remain as compatibility anchors; the linked file retains the full proof and hypotheses.

# quintic h2 monic ode and open incidence

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## Integration guide: the actual open and the differential equations

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

# Independent audit: automatic qhigh and the shared logarithmic ODE

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 1. The precise actual ring and the q5 congruence

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 2. An explicit membership proves unimodularity

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 3. The cubic rank condition has globally unique witnesses

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 4. All eight coefficients and the accelerators

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 5. The first rank condition is automatic scheme-theoretically

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 6. New arithmetic evidence and limitations

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

# One denominator-free incidence for all remaining homogeneous h2 candidates

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 1. Original parameters retain the inverse-map boundary

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 2. Define the sextic by monic division of the actual octic

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 3. The same shared ODE and spectral identities hold globally

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## 4. Exact new assembly and continuation boundary

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

## Required evidence for an exclusion

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

### Archived exact certificate: `research/computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2`

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

### Archived exact certificate: `research/computations/generalization_quintic_h2_localized_ode_2026_10_15.m2`

[Full mathematical section](extracted_quintic_h2_monic_ode_and_open_incidence.md).

