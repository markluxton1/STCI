# Contact duality and global descent

The fixed embedded quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) remains an open
characteristic-zero existence problem: can two homogeneous equations
have exactly this reduced support? This account studies necessary
structure of an arbitrary hypothetical proper pair and explicit controls
showing why several proposed shortcuts do not answer that question.
For an intersection containing residual curves, the sole-support conclusions
below require separate justification on its primary part.

**Review status (2026-10-31).** Independent mathematical and preservation review reconstructed this replacement and its explicit characteristic extensions. The varying-Hilbert-function local control, degree-four defect notation, and ribbon section calculation were checked in their corrected homes. No material finding remains unresolved within the stated scopes. These remain reviewed deductions; no computation or inherited certificate rerun was needed.

All deductions in the four linked proof chapters retain **independently
reviewed** status. Their source proofs and corrections were
reviewed on the source branch. Inputs, including the conormal splitting and
full-socle formula, remain governed by their result records. Every displayed
calculation below has a complete algebraic proof in its owning chapter;
no recorded rank or unperformed computation substitutes for one.

## The approaches and their exact reach

| Approach | Object retained | What is established | What remains missing |
|---|---|---|---|
| [Jacobian/contact](contact_jacobians_and_hamiltonian_actions.md) | Actual CI ideal and actual socle line | All six Jacobians recover tangent sextics; exact different/colon and involutive ideal | Quartic-specific incompatibility, or a pair satisfying the global identities |
| [Full tropical modification](tropical_thickenings_and_endpoint_duality.md) | Entire saturated finite family \(W\to\mathbf P^1\), its two contracted subalgebras and conductor schemes | Every characteristic-zero pair forces positive embedded movement and no two global Cartier equations upstairs | Whether its image can have two compatible homogeneous equations downstairs |
| [Polarization root](polarization_roots_and_section_defects.md) | Full nilpotent root algebra, its grading and reduced vertex defect | A unique ample fourth root; Gorenstein full algebra; exact invariant defect and restrictions on reduced section images | A theorem forcing forbidden sections or a construction of the requisite fourth Veronese |
| [Embedded-neighborhood and Rees controls](section_defects_and_exceptional_cover_controls.md) | Specified section-lifting class; actual normalized exceptional cover | First-order obstruction persists; exceptional covers can be branched with unbounded genus | A proved link to actual residual support using the fixed quartic's equation spaces |

The [foundation account](global_equations_and_constructions.md) supplies related
actual-equation and affine-descent formulations when available; these are
not replacements for the full objects above. The difference between the
rank-\(m=ab/4\) tropical projection and the degree-\(ab\) pencil
\([x_0:x_3]\) is essential. The first uses the parameter of the reduced
curve itself; the second reduces to its fourfold cyclic cover.

## Characteristic is part of each mechanism

The fixed curve has an STCI with a quartic carrier in
[every positive characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
The characteristic-free parts of this account are therefore compatibility
conditions that such equations may satisfy, not hidden nonexistence claims.
The full tropical closure, conductor modules/pairings, endpoint indices and
constant-family two-divisor lemma do not require separability or an inverse
multiplicity. Strict movement uses characteristic-zero Hellus–Hübl and
fails for the explicit characteristic-seven constant family. Actual
Jacobian socle recovery instead needs the multiplicity \(m\) invertible;
its displayed symplectic/tame-cover interpretation additionally needs two
invertible. The root construction and perfect degree-four torsor pairing
extend when four is invertible, while its degree-one image restriction
also needs six invertible. The smooth-cubic moving control requires
\(p\ne2,3\); the exceptional cyclic-cover control requires \(p\nmid re\).
Each owning proof states precisely which assertions extend and which
steps fail. No exponential action or complex-analytic deformation theorem
is transferred to characteristic \(p\) merely from a formal identity.

## Duality supplies a module before it supplies a number

For a hypothetical pair \(Z=V(F_a,G_b)\), the actual socle is
\(\mathcal S=\mathcal O_{\mathbf P^1}(14-4a-4b)\). The local
projection-change lemma proves that its relative Jacobian is a generator
for every local parameter étale on the smooth support. Comparing algebraic
parameters \(z+\lambda u\) forces the mixed minors to vanish. This is the
intrinsic mechanism behind the tangent sextic tuple and exact contact
identity: the complete-intersection differential has one surviving direction
in its socle, fixed by the reduced tangent geometry. The proof requires no
normal flatness and no absolute trace normalization across different
projections.

The conductor of the full tropical modification is another dualizing
module, now on \(W\):

\[
\omega_W=\mathfrak c\otimes\rho^*\omega_Z,\qquad
\pi_*\mathfrak c=\mathcal B^\vee\otimes\mathcal O(14-4a-4b).
\]

This is an actual module identification. Its local quotient retains an
Artinian Gorenstein algebra \(D\) and a half-length self-orthogonal
**subalgebra** \(E\subset D\), with \(A=B\times_D E\). Replacing this by
its determinant forgets multiplication and descent; it gives only the
already-known genus equation. Replacing it by a scalar is worse: the
explicit length-four local example has non-Gorenstein \(B\) and a
nonprincipal conductor, although the downstairs algebra is CI and its
finite conductor quotient is Gorenstein.

The root algebra uses duality in a third way. Its fourth-power torsor has
an actual trace pairing perfect off the vertex; the full section modules'
depth two extends that pairing across the vertex. Hence the full root
algebra is Gorenstein. Its reduction can still have a finite vertex defect.
A Gorenstein statement about the nilpotent cover therefore cannot be
substituted for normality or CM of its reduced cover.

These are proved applications of finite/closed-immersion duality to three
different objects. They are a shared mechanism, **not** theorem arrows
identifying those objects or their defects.

## Lifting and descent have to retain the marked equation data

The missing coordinate \(s^2t^2\) has a rank-two first-order obstruction
represented by the graph-normal extension
\(0\to\mathcal O(-3)^2\to\mathcal O(-2)^3\to\mathcal O\to0\).
This identifies the actual section, not an arbitrary extension with matching
degrees. Every entirely thick torus translate and both full Hilbert limits,
including their pure hulls, contain this same first neighborhood. Thus the
obstruction survives there automatically; asking it to vanish would already
contradict a fixed embedded neighborhood. Torus-invariant Gorenstein
quadric multiples independently have exactly four linear sections while
failing ACM in higher twists.

The tropical family measures a different lifting failure. Its Plücker degree
is positive because degree zero would make the whole embedded quotient
constant, force torus invariance of the actual CI ideal, and contradict
Hellus–Hübl's extreme-component theorem for this exact quartic. Positivity
also rules out **every** global two-Cartier-divisor presentation upstairs
by adjunction. It does not rule out a homogeneous CI image after contraction.
For every \(m\ge2\), the explicit smooth-cubic multiple \(mC\) has a moving
curvilinear family and both primitive Gorenstein contractions. Its two affine
pieces are themselves genuine scheme CIs, yet every homogenization of
an affine generating pair introduces a residual curve, because the common
projective thickening cannot be a homogeneous CI. Thus local equations and
local Gorensteinness fail to retain the required global twists and gluing.

For roots the analogous retained datum is equivariant: the reduced root
algebra has \(D_4=k\cdot s^2t^2\), while its other fourth-divisible defects vanish.
A known twisted-cubic CI has a Gorenstein root algebra with nonnormal
reduction and an ample root without sections, but zero invariant defect.
It controls general root-based inferences without disposing of the quartic's
specific invariant defect. Taking normalization or affinizing the reduced
puncture erases precisely the data one hopes to use.

## From a defect to actual residual support: the missing implication

For a proper pair with
\([V(F,G)]=m[C]+R\), one has \(ab=4m+\deg R\). To use any defect above
as a positive cost in this equality, one must prove that it cannot be
absorbed into the \(C\)-primary thickening and must create a curve component
outside \(C\). The following distinctions block an automatic inference:

* Endpoint lattice indices measure functions gained by a finite modification;
  they are not degrees of residual curves.
* Conductor schemes are finite boundary pinching schemes; their length identity
  is the genus identity, not an additional residual budget.
* Root defects occur at a cone vertex and measure failure of section extension
  through nilpotents. They are not established attachment lengths.
* Ramification of normalized exceptional covers can consist of whole
  pencil-direction curves mapping to points on the support. The explicit
  line-support CI has such branched covers of unbounded genus and no residual
  curve downstairs.
* Hamiltonian actions in the entirely thick branch move only nilpotent
  transverse structure, kill the whole socle, and force cofactors in \(I_C\).
  Their large kernel prevents direct use of reduced constant-kernel deformation
  theory; failure of that theory's hypotheses is not nonexistence.

A sufficient constructive bridge would be a moving finite family with two
compatible endpoint pinching algebras whose projective image has a saturated
ideal generated by two forms with prescribed twists. A sufficient obstructive
bridge would show that every such candidate violates that actual presentation,
or would bound allowed primary concentration so that a positive residual cycle
is unavoidable. No such universal bridge is proved here. The displayed moving
family and the twisted-cubic/contact/Rees controls explain which weaker
conditions are insufficient.

## Literature and bounded stopping points

The primary literature is integrated where its hypotheses are checked:
CI Jacobian/different formulas and finite duality; the reduced Legendrian
and Lagrangian deformation settings; Tevelev and Luxton–Qu's tropical
compactification guarantees; Hellus–Hübl's exact fixed-quartic theorem;
primitive multiple-curve geometry; affine Serre construction and
Quillen–Suslin; canonical-ribbon examples; and Jaffe's scope restrictions
on iterated curve blowups. None is cited as an unrestricted STCI theorem
for this embedding. No literature-priority claim is made.

The bounded synthesis isolates actual algebraic/geometric objects and
removes three unsupported upgrades: different-relative-map normalization,
scalar replacement of a canonical conductor module, and normalization of
a reduced root model without its vertex defect. It also separates proved
implications from common mechanisms. Further work requires the stated
homogeneous-realization or residual-support theorem; repeating local tests,
genus identities, or abstract cover normalizations alone cannot supply it.


### Archived certificate: `research/computations/session-localcoh-corners.py`

Exact original source preserved with its stated scope and external dependencies. Its relative paths refer to the historical source location.

<details><summary>Historical Python source</summary>

```python
#!/usr/bin/env python3
"""Reproduce and verify three complete e=2 zero-at-origin corner exclusions.

Default: verify the stored rational polynomial duals using the standard
library only. --regenerate: use SymPy and M2 to rebuild the ancestor lifts,
one-variable module calculations, and JSON certificate from the audited
tensor. The theorem has the scope stated in the companion session note.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CERT = HERE / 'session-localcoh-corners-certificate.json'
COORDINATES = ['localcoh-incidence-tensor.txt', 'localcoh-incidence-bases.txt',
               'localcoh-symbol-top.json', 'localcoh-symbol-numerators.txt']


def regenerate():
    import sympy as s
    top = json.loads((HERE / 'localcoh-symbol-top.json').read_text())
    M = s.Matrix(top['matrix'])
    pivots = M.rref()[1]
    independent = M[:, pivots]
    independent_rows = independent.T.rref()[1]
    inverse = independent[list(independent_rows), :].inv()
    kernel = M.nullspace()[0]
    tensor = s.zeros(74, 542)
    for line in (HERE / COORDINATES[0]).read_text().splitlines()[1:]:
        row, col, value = line.split()
        tensor[int(row), int(col)] = s.Rational(value)
    t, parameter = s.symbols('t lambda')
    directions = [('corner18', 1+t, -6*t+18*t*t),
                  ('corner2', 1+t-t*t, 2*t*t),
                  ('corner10', 1+t-t*t, 10*t*t)]
    cases = []
    for label, p, r in directions:
        pure = s.Matrix([s.expand(t*p**i*r**(3-i)).coeff(t, j)
                         for i in range(4) for j in range(8)])
        assert s.Matrix(top['annihilator'])*pure == s.zeros(3, 1)
        seed = s.zeros(30, 1)
        for index, value in zip(pivots, inverse*pure[list(independent_rows), :]):
            seed[index] = value
        assert M*seed == pure and M*kernel == s.zeros(32, 1)
        ancestor = seed + parameter*kernel
        matrix = s.Matrix(74, 18, lambda row, col: s.expand(sum(
            tensor[row, 18*i+col]*ancestor[i] for i in range(30))))
        def m2(value):
            return str(value).replace('**', '^')
        script = [
            '-- Generated by session-localcoh-corners.py --regenerate.',
            'R=QQ[lambda];',
            'L=matrix{' + ','.join('{' + ','.join(m2(v) for v in matrix.row(row))
                                      + '}' for row in range(74)) + '};',
            'K=gens kernel transpose L;',
            'U=matrix{' + ','.join('{' + str(int(row == 72)) + '}'
                                  for row in range(74)) + '};',
            'E=transpose U*K; J=ideal E;',
            'assert(J==ideal(1_R));',
            'c=matrix{{1_R}} // E; n=K*c;',
            'assert(transpose n*L==0); assert(transpose n*U==matrix{{1_R}});',
            'ff=openOut "research/computations/session-localcoh-' + label + '-dual.txt";',
            'for row from 0 to 73 do ff << row << " " << toString n_(row,0) << endl;',
            'close ff;',
            'print "PASS: exact polynomial dual excludes u for every lambda";',
            'exit 0;'
        ]
        script_path = HERE / ('session-localcoh-' + label + '.m2')
        script_path.write_text('\n'.join(script) + '\n')
        subprocess.run(['M2', '--script', str(script_path)], cwd=HERE.parent.parent,
                       check=True)
        dual = []
        for row, line in enumerate((HERE / ('session-localcoh-' + label + '-dual.txt'))
                                   .read_text().splitlines()):
            index, value = line.split(maxsplit=1)
            assert int(index) == row
            polynomial = s.Poly(s.sympify(value.replace('^', '**').replace('lambda', 'lam'),
                                         locals={'lam': parameter}), parameter)
            dual.append([[power[0], str(coefficient)]
                         for power, coefficient in polynomial.terms() if coefficient])
        cases.append({'label': label,
                      'p': [str(s.expand(p).coeff(t, i)) for i in range(3)],
                      'r': [str(s.expand(r).coeff(t, i)) for i in range(3)],
                      'seed': list(map(str, seed)), 'kernel': list(map(str, kernel)),
                      'dual': dual})
    CERT.write_text(json.dumps({
        'coordinate_sha256': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                              for name in COORDINATES},
        'scope': 'primitive e=2, h=t, r(0)=0, p(0)=1; three torus-normalized cases',
        'cases': cases}, indent=2) + '\n')


def add(first, second):
    answer = dict(first)
    for power, coefficient in second.items():
        answer[power] = answer.get(power, Q(0)) + coefficient
        if not answer[power]:
            del answer[power]
    return answer


def scale(polynomial, value):
    return {power: coefficient*value for power, coefficient in polynomial.items()
            if coefficient*value}


def multiply(first, second):
    answer = {}
    for i, a in first.items():
        for j, b in second.items():
            answer = add(answer, {i+j: a*b})
    return answer


def power(polynomial, exponent):
    answer = {0: Q(1)}
    for _ in range(exponent):
        answer = multiply(answer, polynomial)
    return answer


def verify():
    data = json.loads(CERT.read_text())
    for name, expected in data['coordinate_sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected, name
    lines = (HERE / COORDINATES[0]).read_text().splitlines()
    assert lines[0] == '30 18 74 542'
    tensor = [[Q(0)]*542 for _ in range(74)]
    for line in lines[1:]:
        row, col, value = line.split()
        tensor[int(row)][int(col)] = Q(value)
    assert [row[540] for row in tensor] == [Q(i == 72) for i in range(74)]
    assert [row[541] for row in tensor] == [Q(i == 73) for i in range(74)]
    bases = (HERE / COORDINATES[1]).read_text().splitlines()
    assert bases[1:31] == (HERE / COORDINATES[3]).read_text().splitlines()
    M = [[Q(value) for value in row] for row in
         json.loads((HERE / COORDINATES[2]).read_text())['matrix']]
    for case in data['cases']:
        seed, kernel = list(map(Q, case['seed'])), list(map(Q, case['kernel']))
        p = {i: Q(value) for i, value in enumerate(case['p']) if Q(value)}
        r = {i: Q(value) for i, value in enumerate(case['r']) if Q(value)}
        top = []
        for i in range(4):
            polynomial = multiply({1: Q(1)}, multiply(power(p, i), power(r, 3-i)))
            top.extend(polynomial.get(j, Q(0)) for j in range(8))
        assert [sum(a*b for a, b in zip(row, seed)) for row in M] == top
        assert all(sum(a*b for a, b in zip(row, kernel)) == 0 for row in M)
        dual = [{int(exponent): Q(value) for exponent, value in terms}
                for terms in case['dual']]
        assert dual[72] == {0: Q(1)}
        for col in range(18):
            result = {}
            for row in range(74):
                entry = {0: sum(tensor[row][18*i+col]*seed[i] for i in range(30)),
                         1: sum(tensor[row][18*i+col]*kernel[i] for i in range(30))}
                result = add(result, multiply(dual[row], entry))
            assert not result, (case['label'], col, result)
        print('PASS:', case['label'], 'pure-top lift and all 18 polynomial-dual identities; n^T u=1.')
    print('PROVED: all three normalized primitive corner directions exclude u for every lower coefficient.')


if __name__ == '__main__':
    if '--regenerate' in sys.argv:
        regenerate()
    verify()
```
</details>


### Archived certificate: `research/computations/session-localcoh-origin-generic-dual.py`

Exact original source preserved with its stated scope and external dependencies. Its relative paths refer to the historical source location.

<details><summary>Historical Python source</summary>

```python
#!/usr/bin/env python3
"""Clear/verify the generic first rational endpoint family's polynomial dual.

Default verification uses exact standard-library arithmetic only.
--regenerate uses SymPy to clear the saved M2 rational dual and ancestor.
The dual proves exclusion only where its displayed denominator is nonzero.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent
INDEX=next((int(value) for value in sys.argv[1:] if value.isdecimal()),1)
assert INDEX in (1,2,3,4)
STEM='session-localcoh-origin-family-'+str(INDEX)
CERT=HERE/(STEM+'-polynomial-dual.json')

def regenerate():
    import sympy as s
    k,lam=s.symbols('k lam')
    dual=[]
    for row,line in enumerate((HERE/(STEM+'-generic-dual.txt')).read_text().splitlines()):
        index,value=line.split(maxsplit=1)
        assert int(index)==row
        dual.append(s.cancel(s.sympify(value.replace('^','**').replace('lambda','lam'),
                                      locals={'k':k,'lam':lam})))
    denominator=s.Integer(1)
    for value in dual:
        for coefficient in s.Poly(value,lam).all_coeffs():
            denominator=s.lcm(denominator,s.denom(s.cancel(coefficient)))
    saved=json.loads((HERE/(STEM+'-seed.json')).read_text())
    seed=[s.sympify(value,locals={'k':k}) for value in saved['seed']]
    kernel=[s.Rational(value) for value in saved['kernel']]
    ancestor_denominator=s.Integer(1)
    for value in seed:
        ancestor_denominator=s.lcm(ancestor_denominator,s.denom(s.cancel(value)))
    alpha=[s.cancel(ancestor_denominator*value)+lam*ancestor_denominator*correction
           for value,correction in zip(seed,kernel)]
    polynomial_dual=[s.cancel(denominator*value) for value in dual]
    def terms(value):
        return [[i,j,str(coefficient)] for (i,j),coefficient
                in s.Poly(value,k,lam).terms() if coefficient]
    inputs=['localcoh-incidence-tensor.txt','localcoh-incidence-bases.txt',
            'localcoh-symbol-top.json',STEM+'-seed.json',STEM+'-generic-dual.txt']
    CERT.write_text(json.dumps({
        'coordinate_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in inputs},
        'alpha':[terms(value) for value in alpha],
        'dual':[terms(value) for value in polynomial_dual],
        'ancestor_denominator':terms(ancestor_denominator),
        'dual_on_u':terms(denominator),
        'denominator_factorization':str(s.factor(denominator)),
        'scope':'origin family '+str(INDEX)+'; k outside all displayed denominator roots; every lambda',
        'status':'POLYNOMIAL IDENTITY TO BE VERIFIED'
    },indent=2)+'\n')
    print('Cleared ancestor denominator:',s.factor(ancestor_denominator))
    print('Cleared dual denominator:',s.factor(denominator))

def decode(terms):
    result={}
    for i,j,value in terms:
        assert i>=0 and j>=0 and (i,j) not in result
        if Q(value): result[i,j]=Q(value)
    return result

def add(first,second):
    result=dict(first)
    for power,value in second.items():
        result[power]=result.get(power,Q(0))+value
        if not result[power]:del result[power]
    return result

def scale(poly,value):
    return {power:coefficient*value for power,coefficient in poly.items() if coefficient*value}

def multiply(first,second):
    result={}
    for (i,j),a in first.items():
        for (l,m),b in second.items():
            power=(i+l,j+m)
            result[power]=result.get(power,Q(0))+a*b
            if not result[power]:del result[power]
    return result

def verify():
    data=json.loads(CERT.read_text())
    for name,expected in data['coordinate_sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected,name
    alpha=list(map(decode,data['alpha']))
    dual=list(map(decode,data['dual']))
    target=decode(data['dual_on_u'])
    assert len(alpha)==30 and len(dual)==74 and target
    assert dual[72]==target
    products=[[{} for col in range(18)] for i in range(30)]
    lines=(HERE/'localcoh-incidence-tensor.txt').read_text().splitlines()
    assert lines[0]=='30 18 74 542'
    for line in lines[1:]:
        row,col,value=line.split();row,col=int(row),int(col)
        if col<540:
            i,j=divmod(col,18)
            products[i][j]=add(products[i][j],scale(dual[row],Q(value)))
    for col in range(18):
        total={}
        for i in range(30):total=add(total,multiply(products[i][col],alpha[i]))
        assert not total,('tensor identity',col,len(total))
    print('PASS: all 18 cleared polynomial tensor identities over QQ[k,lambda].')
    print('PASS: n^T u is exactly the displayed nonzero denominator polynomial.')
    print('PROVED: origin family',INDEX,'excludes u away from that polynomial\'s roots, for every lambda.')
    print('OPEN: primitive exceptional denominator roots and any uncertified origin families.')

if __name__=='__main__':
    if '--regenerate' in sys.argv:regenerate()
    verify()
```
</details>


### Archived certificate: `research/computations/verify_localcoh_direction_contact_survivor.py`

Exact original source preserved with its stated scope and external dependencies. Its relative paths refer to the historical source location.

<details><summary>Historical Python source</summary>

```python
#!/usr/bin/env python3
"""Exact coprime e=0 third-contact survivor and highest-ancestor audit.

The pair defeats a tangent-contact exclusion; the final rational-coefficient
audit decides only this explicit pair, not its contact chart.
"""
import sympy as sp

x,y,z,w,t,U,V=sp.symbols('x y z w t U V')
q=x*w-y*z;A=x*x*z-y**3;B=x*z*z-y*y*w;C=y*w*w-z**3
T=q*(2*x+2*y-2*z-2*w)+A-2*B-C
P6=x*y*w*w+x*z**3-2*y*y*z*w
P7=2*x*z*z*w-y*y*w*w-y*z**3
P9=2*x*w**3-3*y*z*w*w+z**4
# The complement quartics have first symbols (2h,h), and may be obtained
# directly from the universal lift in verify_localcoh_direction_image.py.
K4=w*w*y*y-y*z**3+w*w*x*y-2*w*y*y*z+x*z**3
K5=w*w*y*z-z**4+2*w*w*x*z-2*w*y*z*z-w*w*y*y+2*w*x*z*z-y*z**3
K6=w**3*y-w*z**3+2*w**3*x-3*w*w*y*z+z**4
# K4,K5,K6 above must agree with the e0 universal-lift basis at lambda=2.
L=[x*T,y*T,z*T,w*T,K4,K5,K6,q*q]
fc=[sp.Rational(2,9),-sp.Rational(5,9),sp.Rational(4,9),-sp.Rational(7,9),1,0,-1,2]
gc=[sp.Rational(1,9),-sp.Rational(1,3),sp.Rational(2,9),sp.Rational(1,3),0,1,0,1]
F=sp.expand(sum(c*f for c,f in zip(fc,L)))
G=sp.expand(sum(c*f for c,f in zip(gc,L)))
assert sp.gcd(F,G)==1
chart={x:1,y:t,z:t**3+V,w:t**4+U+sp.Rational(3,2)*t*V}
f=sp.Poly(sp.expand(F.subs(chart)),U,V)
g=sp.Poly(sp.expand(G.subs(chart)),U,V)
hf=f.coeff_monomial(V);hg=g.coeff_monomial(V)
assert sp.expand(f.coeff_monomial(U)-2*hf)==0
assert sp.expand(g.coeff_monomial(U)-2*hg)==0
bf=f.coeff_monomial(U*U)-2*f.coeff_monomial(U*V)+4*f.coeff_monomial(V*V)
bg=g.coeff_monomial(U*U)-2*g.coeff_monomial(U*V)+4*g.coeff_monomial(V*V)
assert sp.expand(hf*bg-hg*bf)==0
D=t**4-t**3-3*t*t-t+1
assert sp.Poly(sp.gcd(hf,hg),t).monic().as_expr()==D
print('F=',sp.factor(9*F));print('G=',sp.factor(9*G))
print('hF=',sp.factor(hf),'hG=',sp.factor(hg))
print('bF=',sp.factor(bf),'bG=',sp.factor(bg))
print('PASS: coprime ambient pair with exact second transverse contact')

# Localize generically on C.  The module inverse monomial U^(-i-1)V^(-j-1)
# has normal order i+j+1. An order-four ancestor therefore uses i+j<=3.
supports=[(i,j) for d in range(4) for i in range(d+1) for j in [d-i]]
cs=sp.symbols('c0:'+str(len(supports)))
out=[(i,j) for d in range(3) for i in range(d+1) for j in [d-i]]
rows=[];rhs=[]
for poly,target in [(f,1),(g,t*t)]:
    for a,b in out:
        rows.append([poly.coeff_monomial(U**(i-a)*V**(j-b)) if i>=a and j>=b else 0 for i,j in supports])
        rhs.append(target if (a,b)==(0,0) else 0)
mat=sp.Matrix(rows);target=sp.Matrix(rhs)
solution=sp.linsolve((mat,target),cs)
assert solution is not sp.EmptySet
sol=list(solution)[0]
print('generic inverse coefficient solution =',tuple(sp.factor(v) for v in sol))
top=[sp.factor(sol[i]) for i,(a,b) in enumerate(supports) if a+b==3]
pole_denominator=5*t**4-2*t**3+6*t**2-2*t+5
pole_numerator=(t+1)*D*(2*t**6-3*t**5+2*t**4-3*t**3-2*t+1)
highest=pole_numerator/pole_denominator
assert all(sp.cancel(value-multiple*highest)==0
           for value,multiple in zip(top,(8,-4,2,-1)))
assert sp.Poly(sp.gcd(pole_numerator,pole_denominator),t).degree()==0
assert sp.Poly(pole_denominator,t).degree()==4
assert all(not (value.free_symbols & set(cs)) for value in top)
print('PASS: forced highest coefficient has uncancelled finite poles; no global quartic ancestor')
print('highest coefficients=',top)
for v in top:
    print('highest numerator=',sp.factor(sp.together(v).as_numer_denom()[0]),'denominator=',sp.factor(sp.together(v).as_numer_denom()[1]))
```
</details>
