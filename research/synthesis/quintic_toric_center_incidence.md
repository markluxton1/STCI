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
[fixed-carrier criterion](../results/fixed_carrier_conductor_criterion.md)
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
coefficients in the [finite-center input](../computations/quintic_toric_finite_centers.json),
produced by the [finite-center certificate](../computations/quintic_toric_finite_centers.py).
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

The [boundary certificate](../computations/quintic_toric_boundary_centers.py)
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

The [three-curve calculation](../computations/quintic_toric_exception_centers.py)
uses (2) on U0, V1 and V2. The independent source closeout review **passes**:
all three curves are excluded on `Delta*K0*d*N !=0`. It supplies the
[separate specialization audit](../computations/quintic_toric_exception_audit.py)
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
| [Finite-center program](../computations/quintic_toric_finite_centers.py) | `091e9b878f2dbb3b4cca64cac3e366449111dc26305936a13330da516ba05e80` |
| [Finite-center JSON input](../computations/quintic_toric_finite_centers.json) | `924bc8245c2b9cbee76f98862e7e304e9aecb32c4d2a96279666734f10a5b6ec` |
| [One-infinity boundary program](../computations/quintic_toric_boundary_centers.py) | `6de86103d9539039366cee0d99693b06f7d2eed511dad4566bb5233ac6a420b5` |
| [Three-curve program](../computations/quintic_toric_exception_centers.py) | `46a86f93c6aec48a8a79ec897bb60203d226cb27a263435cb4dfae863208016f` |
| [Independent specialization audit](../computations/quintic_toric_exception_audit.py) | `4d2b338367b09858427bcf8f036b5ffe64d39570bc9add8809198607618cdd00` |

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

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Nonendpoint single-root incidence and actual quotient fibers

Fix the embedded curve \(C_0=[s^4:s^3t:st^3:t^4]\), an algebraically closed characteristic-zero field, and the accepted anticanonical degree-five A4 pair \((S,c)\). Retain arbitrary \(\delta\ne0\), the four lift parameters \(a,b,g,d\), and an actual line center disjoint from \(S\), giving a finite birational projection \(\nu:S\to X\) onto an integral quintic. The restriction \(c\to C_0\) is an isomorphism. A hypothetical mate forces **full** reduced inverse support \((\nu^{-1}C_0)_{red}=c\), denoted SUP; it excludes isolated extra inverse points as well as extra curves. The proofs below concern this exact family, not every quintic carrier. The intrinsic pair is proved in [the A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md); actual projection coordinates and every target boundary are in [the target-fiber chapter](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md). The common-root reductions below are necessary conditions and specified branch exclusions; they do not exhaust the full conductor incidence. L1 and L2 arise from different actual maps, and inverse-denominator/degree-drop boundaries are retained.

<a id="2026-10-13-session-nonendpoint-regular-l1-double-root"></a>

## The regular L1 double conductor root

Use the finite common-root parameters and exact coefficients of the
[Taylor incidence note](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md#2026-10-13-session-nonendpoint-single-root-taylor-incidence):

    F(q+t)=t(u0+u1 t+...+u7 t^7),
    kappa=aq+B, Pc=q^2-6q+6.

Consider the explicit rational family

    delta=Pc(q-2)/[q(q-1)],
    kappa=delta+delta^2(2q-3)/[3(q-1)(q-2)],
    B=kappa-aq, G=Gs, J=Js,                         (1)

where Gs,Js are the complete common-root solutions in that note. Retain

    q(q-1)(q-2)Pc!=0.                              (2)

These are actual relations among projection parameters; delta is not
normalized to one. The conditions retain the modulus and every forbidden
denominator. They ensure delta is nonzero and the regular fiber denominator
does not vanish: on (1),

    U=q(kappa-delta)-delta^2
      =-delta^2 Pc/[3(q-1)(q-2)]!=0,
    Z(q)=q Pc U!=0.                                (3)

Exact substitution into the two exact coefficient polynomials gives

    u0=0,
    u1=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.              (4)

The second expression is independent of a. Its nonvanishing follows
from the explicitly retained factors (2); there is no numerical sampling
or Gröbner calculation. The underlying common-root substitution already
gives F(q)=0. Thus the actual conductor restriction has exactly order
two at q for every admissible projection in (1)--(2). This is a literal
coefficient calculation of its actual section, rather than a contact
bound inferred from a first-normal symbol.

In particular, if J!=0 and q is the sole common homogeneous conormal
root, full inverse support would force the entire degree-eight conductor
restriction to be supported at q. Its order two from (4) contradicts
that requirement. Hence the explicitly specified single-common-root
family cannot have a mate in any degree. Applying this consequence to
every regular L1 case also requires the separately justified quotient-
fiber necessity of (1), including its degree-drop case; that proof is
not replaced by this computation.


<a id="2026-10-13-session-nonendpoint-single-root-quotient-fibers"></a>

## The two quotient fibers and the diagonal exception

### 1. Hypotheses and inherited actual fiber system

Work over an algebraically closed field of characteristic zero. Retain
`delta!=0`, the actual center-avoidance condition and finite birational
projection hypotheses of the audited model. Let `q!=0` be a finite
common conormal root, and impose the complete solutions `G=Gs,J=Js`
from the [Taylor incidence note](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md#2026-10-13-session-nonendpoint-single-root-taylor-incidence):

    Gs=-(6B+delta^2-3delta)q-(3a-3B+2delta)q^2+2aq^3,
    2Js=-Gs(1+3q)-(6B+5delta^2-3delta)q
        -(3a+3B+delta-delta^2)q^2+(a+B)q^3.

These equations alone allow repeated and additional common roots. A
sole-common-root hypothesis is imposed explicitly only for the final
support-concentration consequence. Delta remains a parameter, not a
normalized constant.

For variable target `p`, use the actual target-fiber system of the
[diagonal norm note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#4-nonendpoint-diagonal-norm-identity):

    Z=Gp(2-p)+J(3-p),
    A=(3delta^2+G)p(2-p)+J(3-p),
    b=delta[delta^2p(p-3)+3Bp(2-p)+G(2-p)-J],
    c=delta^2[Bp(p-3)-G],
    A2=A r^2+b r+c,
    N=delta^2(pr-delta)[3(2-p)r-delta(3-p)],
    M=delta^2[3Jr^2+delta(2G-J)r-delta^2G],
    Psi=p^2 Z^2 r^4+p^2 Z(2r^2+r-a)N+p^2 N^2-MZ,
    C3=Psi/(pr-delta).

The last division is an exact polynomial division. On `pZ!=0`, common
finite roots of `A2,C3` other than `r=delta/p` reconstruct actual points
of the normalization outside c mapping to the target curve point.
This actual reconstruction, rather than just a resultant vanishing,
is the support obstruction used below. The root `r=delta/p` is the
diagonal c point; double or triple fibers supported there are permitted
by full inverse support.

The present quotient argument applies to the regular chart

    qZ(q)!=0.                                            (1)

The intrinsic A4 target `q=0`, target infinity and the entire `Z(q)=0`
locus remain outside (1); they are not removed by saturation or declared
empty. The denominator-free original fiber equations govern them.

### 2. A linear/quadratic quotient and its normalized common-root norm

Write

    kappa=aq+B, Pc=q^2-6q+6, P6=q^2-3q+3,
    U=q(kappa-delta)-delta^2, rho=delta/q.

On the complete common-root incidence, the fiber polynomials have exact
diagonal factors:

    A2(r,q)=(r-rho)L(r),
    C3(r,q)=(r-rho)Q(r),                            (2)

where `L` has degree at most one and `Q` at most two. Put

    L=Aq r+l0, Q=q Aq^2 r^2+eQ r+fQ,
    Aq=A(q),
    OffNorm=Aq fQ-l0 eQ+q Aq l0^2.                  (3)

The exact identities are

    Res_r(L,Q)=Aq OffNorm,
    OffNorm=delta^2 q^5 U^2 L1,                    (4)
    Z(q)=q Pc U,
    Aq=q^2[(kappa-delta)Pc+delta^2(3-q)],

with the same first Taylor factor as the earlier coefficient note:

    L1=3kappa(q-1)^2 Pc+delta q(3-2q)Pc
       -3delta^2(q-1)^2(q-3).

The factor `Aq` in the fixed-degree resultant is a false leading-degree
factor. It is removed in `OffNorm`, not taken as evidence of an actual
extra point. Here is the degree-drop check, retained explicitly.

If `Aq!=0`, L is linear and (3) vanishes exactly when its unique finite
root also solves Q. If `Aq=0` on (1), the inherited actual cubic has
nonzero quadratic coefficient

    d=-q[3delta^2q(2-q)]^2.

Indeed `A(q)=0` and `Z(q)!=0` force `q!=2`. After dividing by the
diagonal factor, Q is a genuine linear polynomial with `eQ=d!=0`.
Then `OffNorm=-l0 eQ`; its vanishing says `l0=0`, so L is identically
zero and Q still has a finite root. If `l0!=0`, there is no common
finite root. Thus on (1), `L1=0` always produces an actual common finite
quotient root, including this leading-coefficient drop.

Under full inverse support, every such root must be the diagonal rho.
For `Aq!=0` this is the unique root of L; for `Aq=0` it is the unique
root of Q. Therefore the necessary conditions on the regular L1 branch
are

    L(rho)=Q(rho)=0.                                (5)

This does not prohibit doubled or tripled source fibers supported on c.
It only excludes the alternative actual point outside c.

### 3. Solving the allowed diagonal exception without losing P6=0

Set

    S=3(kappa-delta)(q-1)(q-2)+delta^2(3-2q),
    T(kappa)=6(kappa-delta)^2 q(q-1)(q-3)
              +delta(kappa-delta)q Pc
              -4delta^2(kappa-delta)(2q^2-6q+3)
              -delta^3 Pc+3delta^4(q-2).

Both quotient values in (5) have exact compact expressions:

    L(rho)=delta q S,
    Q(rho)=q^2 delta^2 Pc T(kappa).                 (6)

The first condition excludes `q=1` and `q=2`, because S there is,
respectively, `delta^2` and `-delta^2`. Since q is nonzero, (1) also
implies `Pc!=0` and `U!=0`. The remaining S equation solves as

    kappa=delta+delta^2(2q-3)/[3(q-1)(q-2)].         (7)

After precisely this substitution, the following identities hold:

    U=-delta^2 Pc/[3(q-1)(q-2)],
    Aq=-delta^2 q^3 P6/[3(q-1)(q-2)],
    L1=delta P6[Pc-delta q(q-1)/(q-2)],
    Q(rho)=delta^5 q^2 Pc^2/[3(q-1)(q-2)^2]
            *[delta q(q-1)-Pc(q-2)].               (8)

The last equation is essential. Using L1 alone would miss the
`P6=0`, hence `Aq=0`, degree-drop stratum. Conditions (5) and (8), with
the retained units, force in every case

    delta=Pc(q-2)/[q(q-1)],
    kappa=delta+delta^2(2q-3)/[3(q-1)(q-2)],
    q(q-1)(q-2)Pc!=0.                              (9)

When P6 vanishes, (8) still supplies the first relation in (9).
The quotient proof never divides by P6 or Aq. It permits that actual
double/triple diagonal fiber before using the conductor section.

The separate [exact double-root calculation](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md#2026-10-13-session-nonendpoint-regular-l1-double-root)
substitutes (9) into the actual conductor restriction and proves

    F(q+t)=u1 t^2+terms of degree at least three,
    u1=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.              (10)

Thus the actual section has order exactly two at q on the specified
family, independently of a. If `J!=0` and q is the sole common
homogeneous conormal root, full inverse support would require the
nonzero degree-eight conductor section to be supported only at q,
hence to have order eight there. Equations (9)--(10) contradict this.
Consequently, under these explicit hypotheses, the entire regular
L1 branch has no mate in any degree. This is an actual-section
multiplicity calculation, not a contact bound from first-normal data.
If J vanishes or further common roots occur, an allowed contribution
elsewhere remains possible and this support-concentration exclusion
does not apply.

### 4. L2 is a different, diagonal Jacobian factor

With G,J fixed at Gs,Js for the projection under consideration, take
partial derivatives in the variable target p, not in the parameter q.
Define the diagonal wedge

    W=(partial_r A2)(partial_p C3)
      -(partial_p A2)(partial_r C3), evaluated at (r,p)=(rho,q).

The exact identity is

    W=delta^5 Pc^2 L2,                              (11)

where

    L2=3q(q-1)[2delta(q-1)+q(q-2)]kappa^2
       -6delta q(q-1)[delta^2+delta(3q-4)+q(q-2)]kappa
       +delta^5q+3delta^4(q-1)(3q-2)
       +6delta^3q(q-1)(2q-3)+3delta^2q^2(q-1)(q-2).

The earlier literal Taylor identity is `F'(q)=-delta q L1 L2`.
On (1), L1 governs actual residual quotient roots through (4), whereas
L2 governs this diagonal wedge through (11). Their roles are different.
Vanishing of the wedge is not claimed to bound a later contact order
or to classify the whole remaining fiber. On the sole-common-root,
`J!=0` support problem, removal of regular L1 leaves `L2=0` with all
seven exact Taylor vanishing conditions still required. The reviewed geometric bridge at the end of this chapter excludes its regular L1!=0, L2=0, qZ(q)!=0 sole-root sublocus; it does not solve the entire incidence.

At `q=1`, the separate Taylor identity `F'(1)=-delta^7` already gives
an exact simple root without requiring (1). At `q=2`, the regular L1 quotient exception is impossible by S; the L2 branch is covered by the exact two-embedding field calculation in the reviewed bridge.
When `Pc=0`, L1 is nonzero but `Z(q)=0`; (2)--(11) are not used to
replace the denominator-free fiber equations on that stratum. The
other `Z(q)=0` component `U=0`, intrinsic A4 point and target infinity
likewise retain their separate exact fiber equations. The Z=0 boundary, J=0 and higher homogeneous gcd degree prevent a whole-locus conclusion.


<a id="2026-10-13-session-nonendpoint-single-root-taylor-incidence"></a>

## All Taylor coefficients and the target-zero stratum

### 1. Exact finite common-root parameters

Use `B=b-a`, `G=g-3b+2a`, `J=d-2g+2b-a`, with `delta!=0`,
in characteristic zero. The conormal polynomials in the target coordinate
`p=1-z` are

    Pt=G+(6B+delta^2-3delta)p+(3a-3B+2delta)p^2-2ap^3,
    Jt=G+2J+(6B+3G+5delta^2-3delta)p
       +(3a+3B+delta-delta^2)p^2-(a+B)p^3.

They are the corrected cubic pair after the regular finite-target
normalization described in the
[diagonal norm note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#4-nonendpoint-diagonal-norm-identity).
Let `q!=0` be a specified finite common root. The complete equations
`Pt(q)=Jt(q)=0` solve without any further division as

    Gs=-(6B+delta^2-3delta)q-(3a-3B+2delta)q^2+2aq^3,
    2Js=-Gs(1+3q)-(6B+5delta^2-3delta)q
        -(3a+3B+delta-delta^2)q^2+(a+B)q^3.          (1)

This incidence includes repeated common roots and further common roots;
it does not silently impose homogeneous gcd degree one. The target
`q=0` is the intrinsic A4 point and is treated in the earlier conductor
records. Target infinity is likewise a separate common-root stratum.

Write `kappa=aq+B`, `Pq=q^2-6q+6`, and

    U=q(kappa-delta)-delta^2.

The regular fiber denominator and the two diagonal rank coefficients
specialize exactly to

    Z(q)=q Pq U,
    H12(delta/q,q)=-(3-2q)U,
    H13(delta/q,q)=q(4-3q)U.                         (2)

Thus the regular Cramer chart `qZ(q)!=0` additionally requires `Pq U!=0`.
The exceptional strata `Pq=0` and `U=0` are explicitly retained. On
`U=0`, both displayed rank coefficients vanish and the exact remaining
fiber equation on the diagonal is `qT^2=0`; the doubled source fiber
is allowed by full inverse support. It is not removed by saturation.

### 2. All eight exact Taylor coefficients and the seven necessary equations

Let `F(p)` be the exact primitive conductor polynomial of degree at most
eight, defined by the compact norm identity and identified with the
actual conductor restriction by the separate module audit. Write

    F(p)=sum_(n=0)^8 f_n(delta,a,B,G,J)p^n,
    Fstar(q+t)=F(q+t)|_(G=Gs,J=Js).

There is the exact automatic factor

    Fstar(q+t)=t*(u0+u1 t+u2 t^2+u3 t^3
                 +u4 t^4+u5 t^5+u6 t^6+u7 t^7),     (3)

where the compact, complete definition of the eight polynomials is

    u_i=sum_(n=i+1)^8 binomial(n,i+1)q^(n-i-1)
                         f_n(delta,a,B,Gs,Js), i=0,...,7.  (4)

The exact checker verifies the automatic factor and reconstructs the
polynomial from all eight coefficients. Run
`M2 --script research/computations/verify_session_nonendpoint_single_root_taylor_2026_10_12.m2`
from the repository root to write the expanded arrays `u0,...,u7` and the
factors `L1`, `L2`, and `L2` in the `kappa` coordinate to `/private/tmp`.
Macaulay2 1.26.06 reproduced all eleven
[original polynomial exports](https://github.com/markluxton1/STCI/tree/267affa79d3ad247f53f98381d9963fdc243df16/research/validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z) byte for byte. The first four arrays and expanded `L2` are inputs to
the exact checks and the collision-target resultant probe.
They have respectively 196,230,210,199,166,133,96,61 monomials before the
change from `B` to `kappa` (the counts are descriptive and do not prove
independence of the equations).

Now impose actual projection-center avoidance, `J=Js!=0`, full inverse
support, and that the specified finite root q is the only common
homogeneous conormal root. This includes the intended gcd-degree-one
stratum, but does not assert that (1) alone enforces it. The normalization
is a local isomorphism on c away from q under these hypotheses, including
at the A4 point because J is nonzero. Hence the actual degree-eight
conductor restriction is supported only at q. Its section is nonzero,
and therefore

    u0=u1=u2=u3=u4=u5=u6=0, u7!=0.                  (5)

These are seven explicit necessary polynomial equations in the four
parameters `delta,a,B,q`, with retained nonvanishing and actual
admissibility conditions. No Gröbner elimination, existence, emptiness
or parameter-space exhaustion of (5) is asserted here. The upper
coefficients u7,u6,u5 have no generic nonconstant factor in the initial
exact factor output; that observation supplies no exclusion on its own.

### 3. A compact first-coefficient factorization

The first of (5) has a much smaller structural expression:

    u0=-delta q L1 L2,                              (6)

with

    L1=3kappa(q-1)^2 Pq+delta q(3-2q)Pq
       -3delta^2(q-1)^2(q-3),

    L2=3q(q-1)[2delta(q-1)+q(q-2)]kappa^2
       -6delta q(q-1)[delta^2+delta(3q-4)+q(q-2)]kappa
       +delta^5q+3delta^4(q-1)(3q-2)
       +6delta^3q(q-1)(2q-3)+3delta^2q^2(q-1)(q-2).

Both factors depend only on `delta,q,kappa`; in particular L2 has no
separate dependence on a after this coordinate change. It is a quadratic
in kappa. The resulting necessary union is `L1=0` or `L2=0`.
Its geometric branches are not classified by this coefficient alone.

When `q!=1` and `Pq!=0`, the first branch permits an exact linear solve

    kappa=delta^2(q-3)/Pq
          -delta q(3-2q)/(3(q-1)^2).                (7)

The exceptional values cannot be discarded from (7):

* At `q=1`, `L1=delta` and `L2=delta^5`.
* At `Pq=0`, `L1=-3delta^2(q-1)^2(q-3)` is nonzero,
  because these two roots are neither 1 nor 3. Thus (5) requires L2=0
  on this stratum. Here `Z(q)=0`; the original rank equations apply.

For continuation, the exact representative of L2 modulo Pq is preserved
in the supplemental capture. In grouped form it is

    L2 mod Pq = q*[delta^5+39delta^4+198delta^3+198delta^2
                  -(30delta^3+312delta^2+396delta)kappa
                  +(114delta+198)kappa^2]
                -48delta^4-252delta^3-252delta^2
                +(36delta^3+396delta^2+504delta)kappa
                -(144delta+252)kappa^2.             (8)

### 4. The target-z=0 common-root stratum has a simple conductor zero

At `q=1`, equations (3) and (6) give the universal exact identities

    Fstar(1)=0, Fstar'(1)=-delta^7!=0.               (9)

Thus the actual conductor restriction has exactly a simple zero at this
target on every admissible projection satisfying the common-root
equations (1). This statement uses the actual section and its derivative,
rather than inferring a conductor-length bound from its first symbol.
It is valid even if there are additional common conormal roots.

Consequently an admissible projection with `J!=0` and sole common
homogeneous conormal root `q=1` cannot have full inverse support: that
root has length one while the total conductor restriction has degree
eight. This excludes the stated single-root subfamily in every mate
degree. It does not exclude the same q=1 incidence with another common
root or with an allowed A4 contribution when J=0.


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_session_nonendpoint_regular_l1_double_root_2026_10_13.m2](../computations/verify_session_nonendpoint_regular_l1_double_root_2026_10_13.m2), [verify_session_nonendpoint_single_root_quotient_2026_10_13.m2](../computations/verify_session_nonendpoint_single_root_quotient_2026_10_13.m2), [verify_session_nonendpoint_single_root_taylor_2026_10_12.m2](../computations/verify_session_nonendpoint_single_root_taylor_2026_10_12.m2), [verify_session_nonendpoint_single_root_compact_first_coefficient_2026_10_13.m2](../computations/verify_session_nonendpoint_single_root_compact_first_coefficient_2026_10_13.m2). No inherited computation was rerun for this consolidation.

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).


## Reviewed geometric bridges for the regular sole-root branches

In the following inherited bridge notation, \(d=\delta\) is the nonzero modulus (not the fourth lift parameter), \(k=\kappa\), and \(f_i=[t^i]F(q+t)\). Thus \(f_1=u_0\), \(f_2=u_1\), and generally \(f_i=u_{i-1}\). The full regular-L2 source uses this local notation; the preceding sections retain the four lift parameters \(a,b,g,d\) and write the modulus as \(\delta\).


The preceding direct exact coefficient reductions do not solve a full parameter incidence. The following independent geometric arguments supply the additional full-support implications on the stated regular sole-root charts; other L2, Z=0, multi-root and Jbar-zero situations retain their explicit boundaries.

## 7. Regular L2: geometric elimination cover and retained exceptional loci

The owner L2 theorem asserts that, on the accepted finite common-root
incidence and regular chart `qZ(q)!=0`, with `L1!=0,L2=0`, the actual
Taylor coefficients f2,f3,f4,f5 cannot all vanish. Here

    Pc=q^2-6q+6, U=q(k-d)-d^2,
    D=2d(q-1)+q(q-2), E=d^2+d(3q-4)+q(q-2),
    Z(q)=q Pc U.

The exact coefficient identity
`partial_a f2=-(dq/2)L1 partial_k L2 (mod L2)` justifies solving for a
only where the L2 root is simple and L1 is nonzero. No original fiber
leading coefficient or unstated center parameter is divided out.

The finite cover is complete. q=1 is impossible because L2=d^5. q=2 is
handled by its two-embedding quadratic-field cover. Away from q=1,2,
the D=0 boundary makes L2 genuinely linear in k and is handled separately.
On D!=0, a discriminant-zero root has the displayed L1=0 value and lies
outside the new L1!=0 theorem. The remaining points have the algebraic
coordinate m in [the complete owner cover equations](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-13-generalization-quintic-l2). Both signs are covered because
the inverse formula determines m from the actual k; no chosen square-root
branch is lost. All rational-cover denominators are units under d,q,Pc,
q-1,q-2,D nonzero and m^2!=3.

The audit initially flagged the extra polynomial H removed from the f3
numerator. The owner now records the exact identity

    L1=-3m(q-2)Pc^2 H/
      [q^2(q-1)(m^2-3)^2(qm+3q-6)].

Consequently m and H are units on the retained L1!=0 chart. This repairs
the proof gap that would arise from removing H without this identity.
The three normalizations of f3,f4,f5 therefore preserve every candidate.
A common finite m root forces both fixed-degree resultants R34,R35 to
vanish. This implication is valid even when their m-leading degrees drop;
no converse resultant implication is being used.

The completed literal original-resultant witness combines R34,R35 to
`q^53(q-2)^44 Pc^69`, a unit on this chart. The completed D=0 witness
combines the original f3,f4 numerators to q^4. On D=0 the displayed a
coefficient can vanish only when L1 does, by the same derivative identity;
its additional quartic V is therefore not a missing a-solve stratum.
At q=2 the owner gives an original five-generator witness, over the exact
field QQ(mu), mu^2=3, for f2,f3,f4,f5 together with
`1-z*d*(d+2mu/3)`. Both embeddings apply to the characteristic-zero
algebraically closed ground field, so the two L2 roots are retained.
The inverse equation imposes precisely the stated d,L1 units.

The exact original-generator witnesses are retained in the [complete regular-L2 proof](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-13-generalization-quintic-l2). Its inputs, targets and coefficient columns are necessary support; a recorded gcd or saturated ideal printout alone is insufficient. The inherited independent review inspected their construction without presenting that as a fresh execution.

**Audit conclusion: the local regular-L2 theorem and its all-mate
single-root consequence are proved by the displayed cover and completed
literal owner certificates, within their precise scope.** The latter
consequence additionally needs Jbar nonzero and q to be the sole common
homogeneous conormal root. Then full support concentrates the actual
nonzero degree-eight binary section at q, forcing order eight, while
nonvanishing of at least one of f2 through f5 gives order at most five.
The regular-L1 geometric bridge is reviewed explicitly in section 8.

This does not prove an order bound on Z=0, target infinity, q=0, Jbar=0,
or the excluded L1 branch. It does not exclude several support points
sharing conductor degree eight. All those distinctions survive handoff.

The independent audit additionally verifies nine small rational-cover
identities directly, without loading F or an inherited source. They
include the compact discriminant, the cover equation and inverse, the
L1/H identity, the D factor, and the D=0 solve. On D=0 the exact relation
is `L1=-q(q-2)V/[8(q-1)]`, confirming directly that V=0 is the already
excluded L1=0 boundary. The original full L2 discriminant at q=2 is
48d^6; the normalized quadratic after removing 2d has discriminant 12d^4.
Either is nonzero for d nonzero. This clarifies an exponent slip in the
owner note without changing its conclusion. The [small rational-cover identity source](../validation/2026-10-14-quintic-independent-audit/l2-cover-algebra.m2) supplies the exact cover controls. The full original-generator Bezout witnesses remain in the linked owner proof; this small check does not replace them.

## 8. Independent review of the existing regular-L1 geometric bridge

The quotient-fiber identities above combine with the following finite-point reconstruction to prove the regular-L1 support implication. The exact coefficient check and double-root identity are inherited evidence, not fresh computations.

On `qZ(q)!=0`, the actual finite normalization-point reconstruction in
the accepted fiber model applies to common quotient roots. Put
`rho=d/q`. After removing the diagonal factors, the exact linear and
quadratic quotients are L and Q, with normalized quotient norm

    OffNorm=d^2 q^5 U^2 L1.

When Aq!=0, L is a genuine linear polynomial. On L1=0 its unique finite
root also solves Q. When Aq=0, the accepted cubic's quadratic coefficient
is `-q[3d^2q(2-q)]^2`, nonzero on this chart. Thus Q after diagonal
division is a genuine linear polynomial. Its leading coefficient is
nonzero, and OffNorm=0 forces the constant L to vanish identically; Q
still has a finite common root. This retains the leading drop rather
than mistaking a fixed-degree resultant factor Aq for a point.

Full inverse support forces every such root to equal rho; an off-diagonal
root reconstructs an actual normalization point outside c. It follows
that `L(rho)=Q(rho)=0`. A doubled or tripled fiber supported at rho is
allowed at this stage and is not excluded by saturation.

The exact equation `L(rho)=dq*S=0` excludes q=1,2 and gives
`k=d+d^2(2q-3)/[3(q-1)(q-2)]`. The exact Q(rho) equation then forces

    d=Pc(q-2)/[q(q-1)].

That last equation is used even when `P6=q^2-3q+3` vanishes and Aq=0.
The proof does not divide by P6, so this degree-drop component is retained.
The actual-section identity on these precise parameters is

    F(q+t)=f2*t^2+terms of degree at least three,
    f2=(q-2)^4 Pc^12/[9q^8(q-1)^8] != 0.

All factors in this expression are units under the stated chart and the
just-derived exclusions q=1,2. If Jbar!=0 and q is the sole common
homogeneous conormal root, the accepted support bridge requires the
nonzero degree-eight conductor form to be concentrated at q, hence to
have order eight. Its actual order two contradicts that requirement.

**Audit conclusion: the regular-L1 all-mate exclusion is now independently
accepted in exactly this sole-root, Jbar-nonzero, qZ-nonzero scope.** This
supplies the previously pending geometric premise needed for section 7's
combined regular sole-root theorem. No such conclusion is extended to
Z=0, other conormal roots, or an allowed A4 contribution when Jbar=0.



## Consolidated historical supplement: `research/supplements/QUINTIC_H2_INCIDENCE_AND_LOCALCOH_FRONTIER.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# Quintic H2: the degree-five necessary incidence and its open boundary

**Status:** the `j=0` degree-five branch remains unresolved by the proposed
exclusions. Independent source-coordinate review found an upstream reduction
gap in both attempted eliminations and a reciprocal-coordinate error in the
later verifier. The reviewed common-factor, actual conductor-divisibility,
open-domain and logarithmic ODE reductions remain valid. They do not certify
emptiness or construct a projection or an STCI.

The complete abstract theorem formerly embedded here has a focused home in
[polynomial duals and observable affine pencils](POLYNOMIAL_DUALS_AND_AFFINE_PENCILS.md).
It treats arbitrary fields, observation rank/depth, parameter strata and exact
determinantal fallback; it does not supply rank or emptiness for this family.

<a id="source-2026-10-29-quintic-h2-degree-five-incidence-reductionmd"></a>
<a id="source-quintic-h2-degree-five-support-incidence-working-dossiermd"></a>
## Actual coordinates, domain and common-factor equations

Work over an algebraically closed characteristic-zero field. The global
monic exact-gcd-two incidence has parameters `delta,a,B,G,j,v,w` and
`H=x²+vx+w`, on the original open `delta E Delta1 != 0`. Keep repeated
roots of `H` and the inverse-map boundary. The full
[monic ODE proof](QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence)
retains all seventeen equations in nine variables, without inverting the
discriminant or the inverse-map denominator. The
[spectral/generator identities](QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md)
compress those equations; they are not an independent emptiness certificate.

Use the actual source coordinate `x=r/delta=T/S`. The primitive determinant
polynomial is in the reciprocal coordinate `p=delta/r=S/T=1/x`:

```
Fdet(p,1)=sum f_i p^i,
Fsrc(1,x)=x^8 Fdet(1/x,1),
Fsrc=H Q.
```

This is the [reviewed coordinate correction](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence).
The original exact input remains
[primitive-polynomial.txt](../validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt).
In the reciprocal chart, the same homogeneous quadratic factor is
`1+vp+wp²`, rather than `p²+vp+w`.

On `j=0` the conormal cubics in `x` are

```
P  = G*x³+(6*B+delta²-3*delta)*x²
       +(3*a-3*B+2*delta)*x-2*a,
Jc = G*x³+(6*B+3*G+5*delta²-3*delta)*x²
       +(3*a+3*B+delta-delta²)*x-a-B.
```

Set

```
T=3*G+4*delta²,
U=6*B-delta-delta²,  V=a-B,
L=6*B+delta²-3*delta,  M=3*a-3*B+2*delta,
N=L*T-G*U.
```

The cofactor determinant is `E=G*T`, so `G,T` are units. Since
`Jc-P=T*x²+U*x+V`, the common monic quadratic is forced to be

```
v=U/T,  w=V/T.
```

Divisibility of both cubics is equivalent to the two remainder equations

```
F0=-2*a*T²-V*N=0,
F1=M*T²-G*V*T-U*N=0.
```

Writing `A=2*T²+N`, `C=3*T²-G*T` gives, on the additional chart `A != 0`,

```
a=B*N/A,
Phi=B*C*N+A*(-3*B*T²+2*delta*T²+G*B*T-U*N)=0.
```

This rational chart does not authorize dropping `A=0`. The original source
also reports an auxiliary elimination on `A=0`: `F0` forces `B=0`, and
eliminating `G` from the remaining equations gives
`576*delta^10*(delta+1)²`; at `delta=-1` it reports `T=0`. That reported
auxiliary calculation has not been independently replayed here and is not
used to replace the full two remainder equations or globally invert `A`.
The original admissible open specializes to

```
delta*G*T*(G+3*delta²)*(G+delta²+2*B) != 0.
```

## The valid degree-five ODE and fixed A4 zero

The exact source quotient recursion is

```
q6=f0,
q_i=f_(6-i)-v*q_(i+1)-w*q_(i+2),
Q=sum q_i*x^i.
```

In particular `q6=f0=-3j Delta1`. On `j=0`, `q6=0` and

```
q5=f1=-2*(G+3*delta²)*Delta1
     =-2*G*(G+3*delta²)²*(G+delta²+2*B).
```

Thus `q5` is a unit on the prescribed open and the affine quotient has
exact degree five. The necessary source-support equation is

```
H Q'=(5x+u)Q.
```

It implies that each finite root of `Q` lies among the roots of `H`.
The homogeneous sextic quotient also has its fixed simple A4 zero, at
`S=0`, equivalently `p=0` and `x=infinity`. A degree-five affine quotient
is compatible with a monic quadratic `H` avoiding that point. This fixed
zero supplies no equation `H(0)=0` in the source affine chart.

<a id="source-quintic-h2-degree-five-exclusionmd"></a>
<a id="source-quintic-h2-research-next-stepsmd"></a>
## Why the proposed eliminations do not close the branch

The proposed reductions treated `Fdet(0)=0` and its unit linear
coefficient as a simple conductor zero at source `x=0`. They concern
A4 at source infinity. Consequently they do not justify `w=0`, `a=B=0`
or the special pure-power form `Q=q5(x+v)^5`. The earlier candidate
resultants of degrees eight and eight therefore do not exclude the
complete incidence, regardless of whether their polynomial identities
hold on an additionally restricted locus.

The later calculation also extracted `q5=f7`, followed by `q4` from
`f6` and `q3` from `f5`, directly from the unreversed determinant.
After `a=B=j=0` it used `q5=delta^7`. The actual source recursion instead
uses `f1,f2,f3`, with the displayed unit `q5`. Its degree-five/degree-seven
resultants are therefore not a certificate for the stated actual-source
incidence. A successful execution of that calculation would not repair
the earlier unsupported specialization.

Both exclusion claims are withdrawn. No executed certificate of emptiness
for the complete degree-five incidence is supplied here. A repaired
exclusion needs either a valid reduction of the full original incidence or
a direct certificate over it, retaining all prescribed opens, repeated
roots and inverse-map boundary cases. Merely replaying the two proposed
resultants is insufficient. The degree-six `j != 0` branch and nonlinear
conductor-power descent also remain unresolved.

## Review scope

Independent review compared the actual primitive input, source-coordinate
correction, full monic coefficient recursion and both proposed elimination
accounts. It found the coordinate and reduction gaps above without running
the invalid verifier. Consolidation retains the valid necessary equations
and the distinct polynomial-dual theorem; it does not infer nonemptiness,
new rank facts or a broader STCI conclusion.


### Archived exact certificate: `research/computations/verify_session_nonendpoint_h2_classification_2026_10_13.m2`

Original source retained verbatim, with original limitations and relative-path assumptions.

<details><summary>Original Macaulay2 source</summary>

```macaulay2
-- Complete homogeneous quadratic common-factor cover for the corrected pair.
-- These exact identities do not assert a mate or exhaust conductor descent.
R0=QQ[sepD,aa,bb,gg,parD,rr,zz];
po=((gg-3*bb+2*aa)*rr^3+(6*sepD*(bb-aa)+sepD^3-3*sepD^2)*rr^2
 +(sepD^2*(6*aa-3*bb)+2*sepD^3)*rr-2*aa*sepD^3);
jo=((2*parD-3*gg+bb)*rr^3+(3*sepD*(gg-bb)+5*sepD^3-3*sepD^2)*rr^2
 +(3*bb*sepD^2+sepD^3-sepD^4)*rr-bb*sepD^3);
pn=((gg-3*bb+2*aa)*zz^3+(6*(bb-aa)+sepD^2-3*sepD)*zz^2
 +(6*aa-3*bb+2*sepD)*zz-2*aa);
jn=((2*parD-3*gg+bb)*zz^3+(3*(gg-bb)+5*sepD^2-3*sepD)*zz^2
 +(3*bb+sepD-sepD^2)*zz-bb);
assert(substitute(po,{rr=>sepD*zz})==sepD^3*pn);
print "PASS 1: literal normalized P, with every delta factor retained";
assert(substitute(jo,{rr=>sepD*zz})==sepD^3*jn);
print "PASS 2: literal normalized J, with every delta factor retained";
p0=-2*aa; p1=6*aa-3*bb+2*sepD;
p2=6*(bb-aa)+sepD^2-3*sepD; p3=gg-3*bb+2*aa;
j0=-bb; j1=3*bb+sepD-sepD^2;
j2=3*(gg-bb)+5*sepD^2-3*sepD; j3=2*parD-3*gg+bb;
assert(p1+3*p0-3*j0==2*sepD and p2-3*p0+6*j0==sepD^2-3*sepD
 and j1+3*j0==sepD-sepD^2
 and j2-3*p3-3*p0+6*j0==5*sepD^2-3*sepD);
print "PASS 3: four complete affine coefficient constraints";
assert(substitute(pn,{sepD=>-1,aa=>0,bb=>-2/3,gg=>-2})==0
 and substitute(jn,{sepD=>1,bb=>0,gg=>-2/3,parD=>-1})==0);
print "PASS 4: zero-cubic boundary signs, not part of exact h2";

Rn=QQ[del,v,w,ca,cb,cc,cd,z];
mn=matrix{{w,v+3*w,0,-3*w},{v,1-3*w,0,6*w},{0,0,w,v+3*w},{-3,-3*w,v,1+6*w}};
rhsn=del*matrix{{2},{del-3},{1-del},{5*del-3}};
vec=matrix{{ca},{cb},{cc},{cd}};
hm=z^2+v*z+w;
pairP=(ca*z+cb)*hm; pairJ=(cc*z+cd)*hm;
cons=matrix{{ca*w+cb*v+3*cb*w-3*cd*w},
 {ca*v+cb-3*cb*w+6*cd*w},
 {cc*w+cd*v+3*cd*w},
 {cc*v+cd-3*ca-3*cb*w+6*cd*w}};
assert(mn*vec==cons);
print "PASS 5: exact finite-H coefficient matrix";
quadK=v^2+2*w+6*v*w+6*w^2;
assert(det mn==(v^2-4*w)*quadK);
print "PASS 6: determinant separates repeated H and exceptional conic";
aaRec=-cb*w/2; bbRec=-cd*w; ggRec=ca+3*bbRec-2*aaRec;
ddRec=(cc+3*ggRec-bbRec)/2;
npRec=((ggRec-3*bbRec+2*aaRec)*z^3+(6*(bbRec-aaRec)+del^2-3*del)*z^2
 +(6*aaRec-3*bbRec+2*del)*z-2*aaRec);
njRec=((2*ddRec-3*ggRec+bbRec)*z^3+(3*(ggRec-bbRec)+5*del^2-3*del)*z^2
 +(3*bbRec+del-del^2)*z-bbRec);
rowDef=mn*vec-rhsn;
assert(npRec-pairP==-rowDef_(1,0)*z^2-rowDef_(0,0)*z
 and njRec-pairJ==-rowDef_(3,0)*z^2-rowDef_(2,0)*z);
print "PASS 7: recovering actual a,b,g,d loses no coefficient constraint";
aug=mn|rhsn;
assert(substitute(det submatrix(mn,{0,1,2},{0,1,2}),{w=>v^2/4})
 ==-3*v^4*(v+2)^2/64);
print "PASS 8: repeated-H rank is three away from roots zero and one";
repComp=del*v^2+2*del*v-2*v-2;
assert(substitute(det submatrix(aug,{0,1,2,3},{0,2,3,4}),{w=>v^2/4})
 ==-3*del*v^3*(v+2)*repComp/8);
assert(substitute(quadK,{w=>v^2/4})==3*v^2*(v+2)^2/8);
print "PASS 9: repeated-H compatibility and exceptional-conic intersection";
badZero=substitute(mn,{v=>0,w=>0});
badOne=substitute(mn,{v=>-2,w=>1});
assert(all(flatten entries submatrix(badZero,{0},{0,1,2,3}),val->val==0));
assert(all(flatten entries(submatrix(badOne,{1},{0,1,2,3})+2*submatrix(badOne,{0},{0,1,2,3})),val->val==0)
 and all(flatten entries(submatrix(badOne,{3},{0,1,2,3})+3*submatrix(badOne,{0},{0,1,2,3})
 +2*submatrix(badOne,{2},{0,1,2,3})),val->val==0));
print "PASS 10: bad double-root charts have the stated incompatible row relations";

Kp=QQ[delK,tpar]; Fk=frac Kp; denK=tpar^2+6*tpar+6;
toK=map(Fk,Rn,{delK,-2*tpar/denK,-2/denK,0,0,0,0,0});
assert(toK quadK==0);
assert(det submatrix(toK aug,{0,1,2,3},{0,2,3,4})==-24*delK*(tpar+2)/denK^2);
print "PASS 11: the complete exceptional conic has no consistent factor pair";

Ri=QQ[delI,rhoI,ai,bi,zi];
mi=matrix{{-6*rhoI^2+6*rhoI-2,6*rhoI^2-3*rhoI},
 {-6*rhoI^2,6*rhoI^2+3*rhoI-1}};
rhsi=-delI*matrix{{(delI-3)*rhoI^2+2*rhoI},
 {(5*delI-3)*rhoI^2+(1-delI)*rhoI}};
infT=6*rhoI^2-6*rhoI+1;
assert(det mi==2*infT);
print "PASS 12: infinity-plus-finite matrix determinant";
augi=mi|rhsi;
assert(det submatrix(augi,{0,1},{1,2})==-2*rhoI*delI*infT*(2*delI*rhoI+1)
 and det submatrix(augi,{0,1},{0,2})==2*rhoI*delI*infT*(2*delI*rhoI-delI+1));
print "PASS 13: Cramer numerators retain the two exceptional infinity roots";
ai0=delI*rhoI*(2*delI*rhoI+1);
bi0=delI*rhoI*(2*delI*rhoI-delI+1);
assert(all(flatten entries(mi*matrix{{ai0},{bi0}}-rhsi),val->val==0));
print "PASS 14: exact particular solution in every infinity chart";
assert(all(flatten entries(mi*matrix{{3*rhoI-1},{1}}),val->val%ideal(infT)==0));
assert(mi_(0,0)%ideal(infT)==-1_Ri);
print "PASS 15: exceptional infinity charts have a one-dimensional solution fiber";
pq=(6*(bi-ai)+delI^2-3*delI)*zi^2+(6*ai-3*bi+2*delI)*zi-2*ai;
jq=(6*(bi-ai)+5*delI^2-3*delI)*zi^2+(3*bi+delI-delI^2)*zi-bi;
assert((6*(bi-ai)+5*delI^2-3*delI)-(6*(bi-ai)+delI^2-3*delI)==4*delI^2);
print "PASS 16: a double root at infinity is impossible for nonzero delta";
assert(substitute(pq,{ai=>ai0,bi=>bi0,zi=>rhoI})==0
 and substitute(jq,{ai=>ai0,bi=>bi0,zi=>rhoI})==0);
print "PASS 17: both literal quadratic restrictions vanish at the claimed finite root";
print "PASS ALL: 17 exact structural identities; conductor-support incidence remains necessary only";
```
</details>



## Consolidated historical supplement: `research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md`

Original mathematical content, hypotheses, qualifications, and proof status preserved verbatim. Relative links retain their historical source context.

# quintic h2 monic ode and open incidence

## Integration guide: the actual open and the differential equations

This dossier studies the quintic h=2 incidence scheme on the stated nonvanishing open, including the reduction to a shared logarithmic ODE and its coefficient equations. The [spectral and generator dossier](QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md) reorganizes these same equations to expose linear-algebra structure; that is a computational acceleration, not an independent proof of global support exclusion. The [degree-five incidence frontier](QUINTIC_H2_INCIDENCE_AND_LOCALCOH_FRONTIER.md) records a degree-five branch that remains unresolved: the proposed exclusion confuses the reciprocal determinant coordinate with the actual source coordinate and does not justify its pure-power reduction. Replaying those resultants alone cannot settle the branch. Preserve the open-set assumptions and the separate audit of the ODE equivalence.

---


Permanent mathematical dossier retaining full computations, coefficient systems, corrected formulas, proof scope and unresolved cases. Source labels below organize mathematics, not provenance authority.

---

## 2026-10-15-generalization-quintic-h2-automatic-open-ODE-independent-audit

# Independent audit: automatic qhigh and the shared logarithmic ODE

Date: 2026-10-15.

Status: **PASS. The coefficient ideal (q5,q6) is the unit ideal on the
declared actual localized domain. The eight ODE equations give an
equivalent incidence scheme, with unique witness coefficients, and
both proposed accelerator equations belong to the same localized
ideal.** The statements hold over nonreduced parameter bases as well
as at geometric points.

The full automatic-open and ODE proof is consolidated below.
All previous accepted h2 factor, reciprocal-coordinate, A4, closed-lane
and eleven-generator results are premises. No accepted verifier or
actual coefficient construction was replayed. This audit checks only
the new ideal membership, ODE presentation and its ring-level scope.

## 1. The precise actual ring and the q5 congruence

Let A be the actual finite h2 inverse-map parameter ring over the
characteristic-zero ground field, localized at the previously declared
factors: delta, the cover determinant, the cofactor determinant,
recorded denominator/content scalars and Delta1. These are the
original inverse-map conditions together with the newly justified
necessary Delta1 open. No division by j=Jbar is made. The cover determinant is a condition for this inverse-map chart, not a globally necessary condition on every remaining mate; its vanishing boundary remains in the separate global monic system below.

Use the actual monic factorization

    Fsrc=H*Qactual,       H=t^2+vst+ws^2.

Near A4 use p=s/t. In this chart H=1+vp+wp^2, and write F0,F1 for
the constant and linear coefficients of the actual F(p). The constant
and linear coefficients of Qactual are Qactual6 and Qactual5, so

    Qactual6=F0=-3j Delta1,
    Qactual5=F1-vF0.                                  (1)

This concerns coefficients t^8 and s*t^7 of the homogeneous octic;
the p coefficient is taken in the t=1 chart. The reciprocal source
coordinate introduces no further interchange here.

Put S0=G+3delta^2 and L0=G+delta^2+2B. The accepted actual A4
coefficient identity and literal Delta1 formula give

    Delta1=G*S0*L0+j*Psi,
    Qactual5=-2*S0*Delta1+j*T                         (2)

for regular Psi,T in A. In particular, the second congruence is
valid for the actual source sextic: modulo j, (1) gives
Qactual5=F1=-2G L0 S0^2=-2S0 Delta1. The relation is a congruence
in the ring, not merely an assertion on reduced points of j=0.

For the captured sextic, Q=kappa*Qactual with kappa the recorded
commonDen/delta^4, a unit on this domain. Consequently

    q5=-2*kappa*S0*Delta1 modulo j,
    q6=-3*kappa*Delta1*j=eta*j,       eta a unit.       (3)

This proves the exact captured-q5 scope requested in the new claim.

## 2. An explicit membership proves unimodularity

Equations (2) give the exact identity

    Delta1^2+(G*L0/2)*Qactual5
       =j*[Psi*Delta1+(G*L0/2)*T].                    (4)

Every coefficient is regular in A, and 2 is a unit. Since Delta1
is a unit, (4) proves (j,Qactual5)=A. Multiplication by the units
in (3) then gives

    (q5,q6)=(Qactual5,j)=A.                            (5)

This is equality of ideals, with no radical operation or reducedness
assumption. Equivalently, in the quotient by (q5,q6), relation (3)
first gives j=0 and then S0=0, while (2) makes the unit Delta1
zero, forcing the quotient to be the zero ring. Equation (4)
supplies the direct ideal-membership version of that argument.

Thus a separate saturation or inequation for (q5,q6) is redundant
after this one declared domain localization. This does not say the
ideal is the unit ideal before Delta1 and the original denominator
factors are inverted. The same argument does not require S0 to be
inverted as an additional global domain factor.

## 3. The cubic rank condition has globally unique witnesses

The first two columns sQ,tQ have two fixed coefficient pivots

    A56=q5^2-q4*q6,       A67=q6^2,

with q5^4=A56*(q5^2+q4*q6)+q4^2*A67. By (5), these two pivot
determinants generate the unit ideal. Thus their principal opens
cover the entire localized parameter scheme, including after
quotienting by a nonreduced cubic-rank ideal.

On either pivot open, vanishing of the cubic minors of [sQ,tQ,W]
gives unique coefficients lambda,mu with

    W=lambda*sQ+mu*tQ.                                (6)

The uniqueness makes these coefficients agree on overlaps. They
therefore glue to global elements of the affine quotient ring.
This proves that adjoining the two witness coefficients in (6)
gives an incidence scheme isomorphic to the cubic determinantal
scheme, rather than only a projection with the same field-valued
points. No global pivot coefficient is arbitrarily chosen.

For H=t^2+vst+ws^2 and Q of degree six, the exact homogeneous action
identity is

    W=D_(sH)Q=6H_t Q-3H Q_t.

Thus set u=(6v-lambda)/3 and d=(12-mu)/3. The characteristic-zero
ground field makes 3 invertible. Equation (6) is exactly

    H Q_t=(us+dt)Q,                                   (7)

and the correspondence between (lambda,mu) and (u,d) is invertible.
The ODE witnesses are therefore globally unique as well. This
argument uses algebras over the stated field; mere torsion-free
characteristic zero, without 3 invertible, would not suffice.

## 4. All eight coefficients and the accelerators

On s=1, write h=x^2+vx+w and q=sum_(i=0)^6 q_i*x^i. Equation (7)
becomes h*q'=(dx+u)q. Its coefficients are precisely

    E_i=w(i+1)q_(i+1)+(vi-u)q_i+(i-1-d)q_(i-1),
    0<=i<=7,                                          (8)

with out-of-range coefficients zero. Fixed-degree homogenization
keeps the eighth equation even when q6 vanishes. The top equations
are

    E7=(6-d)q6,
    E6=(6v-u)q6+(5-d)q5.

For P=(d-5)(d-6), direct polynomial identities give

    P*q5=(6-d)*E6-(6v-u)*E7,
    P*q6=-(d-5)*E7.                                  (9)

Using a Bezout identity for (5), these imply P belongs to the ODE
ideal itself. There is no cancellation by either q5 or q6. Relation
q6=eta*j with eta a unit likewise gives

    j*(d-6)=-eta^(-1)*E7.                             (10)

At geometric points, d=6 denotes a degree-six sextic without an infinity root, while d=5 denotes degree five with the allowed simple infinity root at the prescribed A4 point. This interpretation does not split the global computation into separately assumed branches.

Both proposed accelerators may therefore be appended without
changing the localized ideal or scheme. They are retained as
equations in one system; no decomposition by values of d or j is
needed to prove or use their membership.

## 5. The first rank condition is automatic scheme-theoretically

The homogeneous quadratic action R=D_HQ satisfies

    sR=6H_tQ-2H Q_t.

Using (7), the ODE ideal gives

    sR=[(6v-2u)s+2(6-d)t]Q.

Multiply by j and apply (10). Then

    s*[jR-j*(6v-2u)Q]=0.

Multiplication by the polynomial variable s is injective over every
coefficient ring, including one with nilpotents or zero divisors.
Consequently

    jR=j*(6v-2u)Q.                                   (11)

All minors of [Q,jR] vanish in the ODE quotient. Thus the ODE
scheme retains the full shared quadratic/cubic rank incidence,
with no separate first-rank equations. Conversely the full shared
rank equations include the cubic rank condition, which gives the
unique ODE witnesses by section 3. This proves the claimed exact
scheme presentation on the stated actual localized domain.

## 6. New arithmetic evidence and limitations

The [universal source](../computations/generalization_quintic_h2_localized_ode_2026_10_15.m2) checks membership identity (4) using independent symbols, all eight coefficients (8), both identities (9) and the two Hamiltonian action identities. It does not substitute or reconstruct the actual conductor map. Localization, captured-q5 identification and gluing require the written proofs above, not a finite sample or rank experiment.

All original actual-map unit and projection hypotheses remain in
force. In a polynomial computation they can be enforced by one
inverse of their product, including the justified Delta1 numerator.
The high-coefficient saturation adds no condition on that domain.
Appending a previously proved necessary norm product also does not
affect the equivalence of the underlying support presentations.

This audit proves the reduction and exact accelerator membership.
It proves no actual-parameter unit ideal, no characteristic-zero
emptiness from a finite-field prospect, no implication from support
to full inverse support, and no nonlinear conductor descent.


---

## 2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence

# One denominator-free incidence for all remaining homogeneous h2 candidates

Date: 2026-10-15. Status: **GLOBAL COVER AND EXACT INPUT ASSEMBLY;
independently audited** in the
[global monic ODE review](STRUCTURAL_CONTINUATION_AND_INDEPENDENT_INVESTIGATIONS.md#2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit).
Accepted conormal forms, the actual
conductor octic, the full h2 conductor factor, global Delta1 open, ODE
and spectral reductions are premises. No accepted verifier is replayed.
There is no unit-ideal, projection-existence or mate-existence claim.

## 1. Original parameters retain the inverse-map boundary

Use original parameters `(delta,a,B,G,j)`, with j=Jbar, and source
`x=r/delta`. The accepted corrected normalized conormal cubics are

```
P=G x^3+(6B+delta^2-3delta)x^2+(3a-3B+2delta)x-2a,
Jc=(G+2j)x^3+(6B+3G+5delta^2-3delta)x^2
                    +(3a+3B+delta-delta^2)x-a-B.
```

For a remaining h2 mate candidate, the common factor contains no source
infinity point: the accepted infinity leading equations would force
G=j=0, whose mate lane is already closed. Thus its complete homogeneous
gcd has the unique finite monic representative

```
H=x^2+v x+w.
```

This includes w=0, double finite roots, and every affine degree drop of
the original cubics. Put

```
A=G,                 Bc=6B+delta^2-3delta-vG,
C=G+2j,              Dc=6B+3G+5delta^2-3delta-v(G+2j).
```

The complete common-factor conditions are the four polynomials

```
-2a-w Bc=0,
3a-3B+2delta-v Bc-w A=0,
-a-B-w Dc=0,
3a+3B+delta-delta^2-v Dc-w C=0.                          (1)
```

They assert P=(Ax+Bc)H and Jc=(Cx+Dc)H. Exact homogeneous gcd two
requires the independent-cofactor unit

```
E=A Dc-Bc C
 =G(3G+4delta^2)-2j(6B+delta^2-3delta) != 0.              (2)
```

No determinant of the four-equation coefficient matrix is inverted.
In particular `Delta=v^2-4w=0` and
`K=v^2+6vw+6w^2+2w=0` remain in this system. The latter may be
inconsistent by an accepted theorem; it is not removed by cancellation.

## 2. Define the sextic by monic division of the actual octic

Read the accepted actual conductor polynomial in the target coordinate

```
Fdet(p,1)=sum_(i=0)^8 f_i p^i,        p=1/x.
```

Its source-coordinate form is the fixed-degree octic
`Fsrc(1,x)=sum f_i x^(8-i)`. Define polynomial coefficients recursively,
with q7=q8=0,

```
q_i=f_(6-i)-v q_(i+1)-w q_(i+2),        i=6,5,...,0.
```

Then, identically in the original parameter polynomial ring,

```
Fsrc=H Q+r1*x+r0,
Q=sum_(i=0)^6 q_i x^i,
r1=f7-v q0-w q1,        r0=f8-w q0.                       (3)
```

Add the two equations r0=r1=0. The accepted global conductor factor
theorem ensures these equations for every actual h2 projection. We
impose them explicitly in the incidence; no scheme-theoretic divisibility
on an arbitrary nonreduced conormal-cover base is inferred from that
geometric theorem.

The newly justified globally necessary unit is

```
Delta1=G(G+3delta^2)(G+delta^2+2B)
       +j[(delta^2-5B)G-3B(delta^2+3B)]-B j^2.
```

The one domain for this global monic incidence is

```
delta*E*Delta1 != 0.                                    (4)
```

Here delta and E express the original chart and exact-h2 hypotheses;
Delta1 is necessary under the accepted closed-lane and SUP arguments.
There is no `Delta*K` inverse and no rational-map denominator.

## 3. The same shared ODE and spectral identities hold globally

The accepted exact A4 identities give, for this unscaled actual Q,

```
q6=-3j Delta1,
q5=-2(G+3delta^2)Delta1  modulo j.                        (5)
```

The second identity follows from q5=f1-vq6 and the accepted first A4
coefficient. In the quotient by (q5,q6), the unit Delta1 forces j=0,
then G+3delta^2=0 by (5), and finally Delta1=0 from its j=0
factorization. Thus `(q5,q6)` is the unit ideal on (4), including
nonreduced coefficient bases. No inverse-map scalar is needed here.

Adjoin the two witnesses d,eta, with eta=dv-2u. The eight equations are

```
2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                         +2(i-1-d)q_(i-1)=0,  i=0,...,7, (6)
```

where out-of-range coefficients vanish. They are twice the coefficients
of `H q'=(dx+u)q`. The independently reviewed ODE and spectral proofs
use only monic H, (5), the Delta1 unit and coefficient unimodularity;
their algebra does not use rational inversion or `Delta*K!=0`.
Consequently the same derived accelerator equations are available:

```
(d-5)(d-6)=0,          j(d-6)=0,
(d-5)P6(eta)+(6-d)P5(eta)=0,                             (7)
P6(X)=X(X^2-4Delta)(X^2-16Delta)(X^2-36Delta),
P5(X)=(X^2-Delta)(X^2-9Delta)(X^2-25Delta).
```

Equations (1), r0=r1=0, and (6) give fourteen equations in the nine
variables `(delta,a,B,G,j,v,w,d,eta)`. Appending (7) gives the saved
seventeen-equation presentation. It uses one domain saturation by (4)
and no qhigh saturation, root partition, norm-factor branch or separate
degree computation.

On actual admissible projections satisfying the stated h2 hypotheses,
this system expresses exactly the accepted restricted-conductor support
obligation, with the intrinsic A4 allowance retained. It does not express
center avoidance, full inverse support at every original fiber, or full
nonlinear conductor power descent. A surviving algebraic parameter is
not thereby a mate.

## 4. Exact new assembly and continuation boundary

The new [assembly source](../computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2)
reads the accepted primitive octic once and forms the original-parameter
model. It asserts (2) and the new literal quotient/remainder identity
(3), writes all equation groups, all seven actual q_i, the single domain
unit and the equation degrees. The degrees are

```
3,3,3,3,13,13,14,13,12,11,10,9,8,7,2,2,8.
```

The retained exact seventeen-entry equation row and domain polynomial are the complete saved model. The assembly source specifies their construction from the actual octic; no Gröbner basis, saturation, resultant or emptiness conclusion follows from assembling this input.

The [input file](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2) reads the completed model over QQ and exposes `h2GlobalRing`, `h2GlobalEquations`, `h2GlobalIdeal` and `h2GlobalDomainUnit`. It checks the seventeen-entry matrix in the nine-variable ring and constructs the unsaturated ideal only; it does not execute domain localization or a Gröbner computation.

The outstanding shared h2 task can therefore be stated globally: prove
this one incidence empty after (4), or describe its actual admissible
survivors and test the full fibers and conductor. A finite inverse-map
calculation may be useful, but its `Delta*K!=0` conclusion must not be
reported as closure of this global seventeen-equation problem.

## Required evidence for an exclusion

The global seventeen-equation incidence remains unresolved. An exclusion by saturation must use the original domain δEΔ1, without silently adding a cover discriminant, K, coefficient or j inverse. A unit-ideal output needs an exact identity in the declared original generators and complete coverage of the stated boundary. A bounded attempt or its process-control checks supplies neither.


### Archived exact certificate: `research/computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2`

Original source retained verbatim, with its limitations and original relative-path assumptions.

<details><summary>Original Macaulay2 source</summary>

```macaulay2
-- NEW denominator-free global monic h2 incidence export; no GB/saturation.
-- Accepted actual primitive conductor is an input, not reconstructed.
outDir="research/validation/2026-10-15-quintic-h2-global-monic-ode/attempt-02-name-repair";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
base=QQ[delta,a,B,G,J,vH2,wH2,h2DGlobal,h2EtaGlobal];
actual=base[p];
F=value get "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt";
f=apply(toList(0..8),i->lift(coefficient(p^i,F),base));
q=new MutableList from toList(7:0_base);
qi=i->if i<0 or i>6 then 0_base else q#i;
scan(reverse toList(0..6),i->q#i=f#(6-i)-vH2*qi(i+1)-wH2*qi(i+2));
q=toList q;
frem={f#8-wH2*qi(0),f#7-vH2*qi(0)-wH2*qi(1)};
Plead=G; Pconstant=6*B+delta^2-3*delta-vH2*G;
Jlead=G+2*J; Jconstant=6*B+3*G+5*delta^2-3*delta-vH2*(G+2*J);
h2CoverEquations={-2*a-wH2*Pconstant,
       3*a-3*B+2*delta-vH2*Pconstant-wH2*Plead,
       -a-B-wH2*Jconstant,
       3*a+3*B+delta-delta^2-vH2*Jconstant-wH2*Jlead};
cofactorDet=Plead*Jconstant-Pconstant*Jlead;
assert(cofactorDet==G*(3*G+4*delta^2)-2*J*(6*B+delta^2-3*delta));
delta1=G*(G+3*delta^2)*(G+delta^2+2*B)+J*((delta^2-5*B)*G-3*B*(delta^2+3*B))-B*J^2;
domainUnit=delta*cofactorDet*delta1;
disc=vH2^2-4*wH2;
ode=apply(toList(0..7),i->2*wH2*(i+1)*qi(i+1)+((2*i-h2DGlobal)*vH2+h2EtaGlobal)*qi(i)+2*(i-1-h2DGlobal)*qi(i-1));
poly6=h2EtaGlobal*(h2EtaGlobal^2-4*disc)*(h2EtaGlobal^2-16*disc)*(h2EtaGlobal^2-36*disc);
poly5=(h2EtaGlobal^2-disc)*(h2EtaGlobal^2-9*disc)*(h2EtaGlobal^2-25*disc);
accelerators={(h2DGlobal-5)*(h2DGlobal-6),J*(h2DGlobal-6),(h2DGlobal-5)*poly6+(6-h2DGlobal)*poly5};
allEquations=join(h2CoverEquations,frem,ode,accelerators);
save("h2CoverEquations-four-equations",matrix{h2CoverEquations});
save("conductor-two-remainders",matrix{frem});
save("ODE-eight-equations",matrix{ode});
save("derived-three-accelerators",matrix{accelerators});
save("global-seventeen-equations",matrix{allEquations});
save("global-domain-unit",domainUnit);
save("actual-Q-coefficients",matrix{q});
scan(toList(0..6),i->save("actual-Q-coefficient-"|toString i,qi(i)));
-- The following is only the new export's division identity, not a claim
-- that the two remainders vanish on arbitrary parameter tuples.
h2SourceRing=base[xH2];
H=xH2^2+vH2*xH2+wH2;
Q=sum(toList(0..6),i->sub(qi(i),h2SourceRing)*xH2^i);
Fsource=sum(toList(0..8),i->sub(f#i,h2SourceRing)*xH2^(8-i));
assert(Fsource==H*Q+sub(frem#1,h2SourceRing)*xH2+sub(frem#0,h2SourceRing));
save("equation-degrees",apply(allEquations,g->first degree g));
print "PASS new monic quotient/remainder export and exact cofactor-determinant formula";
print("COMPLETE GLOBAL denominator-free monic h2 ODE incidence: "|toString(#allEquations)|" equations, delta*cofactor*Delta1 unit; no h2CoverEquations determinant inverted");
exit 0;
```
</details>


### Archived exact certificate: `research/computations/generalization_quintic_h2_localized_ode_2026_10_15.m2`

Original source retained verbatim, with its limitations and original relative-path assumptions.

<details><summary>Original Macaulay2 source</summary>

```macaulay2
-- NEW universal identities for automatic qhigh and a lower-degree ODE incidence.
-- Accepted A4 coefficient and actual scalar identities are premises, not rerun.
outDir="research/validation/2026-10-15-quintic-h2-localized-ode/attempt-01";
save=(label,f)->((outDir|"/"|label|".txt") << toString f << close);
A=QQ[gVal,sVal,lVal,jVal,psiVal,tVal];
deltaOne=gVal*sVal*lVal+jVal*psiVal;
qFive=-2*sVal*deltaOne+jVal*tVal;
membershipWitness=psiVal*deltaOne+(gVal*lVal/2)*tVal;
assert(deltaOne^2+(gVal*lVal/2)*qFive==jVal*membershipWitness);
save("automatic-qhigh-membership-witness",membershipWitness);
print "PASS Delta1^2 belongs to ideal(j,Qactual5), with explicit universal identity";
B=QQ[q0,q1,q2,q3,q4,q5,q6,v,w,d,u];
qf={q0,q1,q2,q3,q4,q5,q6};
qi=i->if i<0 or i>6 then 0_B else qf#i;
polyRing=B[z];
q=sum(toList(0..6),i->qi(i)*z^i);
h=z^2+v*z+w;
ode=h*diff(z,q)-(d*z+u)*q;
ec=apply(toList(0..7),i->w*(i+1)*qi(i+1)+(v*i-u)*qi(i)+(i-1-d)*qi(i-1));
assert(ode==sum(toList(0..7),i->ec#i*z^i));
assert(ec#7==(6-d)*q6);
assert(ec#6==(5-d)*q5+(6*v-u)*q6);
dp=(d-5)*(d-6);
assert(dp*q5==(6-d)*ec#6-(6*v-u)*ec#7);
assert(dp*q6==-(d-5)*ec#7);
quadAction=6*diff(z,h)*q-2*h*diff(z,q);
cubicAction=6*diff(z,h)*q-3*h*diff(z,q);
assert(quadAction==((12-2*d)*z+6*v-2*u)*q-2*ode);
assert(cubicAction==((12-3*d)*z+6*v-3*u)*q-3*ode);
save("eight-universal-ODE-generators",matrix{ec});
save("derived-degree-polynomial",dp);
print "PASS all eight ODE coefficients, top-degree identities, and both Hamiltonian action identities";
print "COMPLETE new universal localized ODE identities; no actual-coefficient elimination";
exit 0;
```
</details>

