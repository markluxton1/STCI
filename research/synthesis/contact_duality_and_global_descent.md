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


## Consolidated historical supplement: `research/supplements/LOCALCOH_CONTACT_PARITY_AND_MF6_TYPE.md`

The following mathematical arguments, qualifications, and audit boundaries are retained verbatim from the historical supplement. Internal relative links refer to the source's original location.

# Ambient contact, parity and multiplicity-six reduction

Topical preservation of source mathematics, including qualifications and independent audits.

---

<a id="2026-10-06-localcoh-mixed-contact-pole"></a>

## A coprime mixed constant-direction contact pair fails the target equations

Date: 2026-10-06. Status: **PROVED / EXACT COMPUTATION** for the explicit
quartic pair only. The finite all-stage reduction depends on the existing
characteristic-zero quartic local-cohomology bound. This does not exclude
all mixed constant directions.

The exact companion `verify_localcoh_direction_contact_survivor.py` constructs
explicit ambient-coprime quartics \(F,G\) with balanced first symbols
\((2h_F,h_F)\), \((2h_G,h_G)\). Their common scalar divisor is

\[
D(t)=t^4-t^3-3t^2-t+1.
\]

It verifies \(\gcd(F,G)=1\) and the second-contact identity
\(h_F b_G-h_G b_F=0\), where \(b_F,b_G\) are the quadratic normal
coefficients along the kernel of the common first direction. Thus this pair
passes both first-conormal rank and generic length-at-least-three tests.
Its degree-four common scalar divisor also kills the P-010 obstruction class
\(h_{1/2}\), as checked independently by
`verify_localcoh_constant_direction_apolar.py`.

The complete target-specific generic inverse-system equations are finite.
An order-four ancestor has the ten inverse-monomial coefficients with
\(i+j\le3\), for monomials \(U^{-i-1}V^{-j-1}\). Multiplication by the
two quartics gives twelve linear equations over \(\mathbf Q(t)\), with
socle right sides \(1,t^2\). These are the actual balanced-frame
representatives of \(u,v\), since the first normal determinant of \((q,B)\)
relative to \((U,V)\) is \(t^3\).

The exact linear solution forces its four highest inverse coefficients to be

\[
(8,-4,2,-1)\,C(t),\qquad
C(t)=\frac{(t+1)D(t)(2t^6-3t^5+2t^4-3t^3-2t+1)}
 {5t^4-2t^3+6t^2-2t+5}.
\]

The lower principal-part freedom does not affect this coefficient. The
script now explicitly asserts that the displayed numerator and denominator
are coprime and that the denominator has degree four; earlier Oct5 output
merely printed the fractions. Therefore \(C(t)\) has finite poles over
the algebraic closure. A global highest symbol is a regular section of
\(O(7)^4\) in the fixed balanced frame, and cannot have these poles.

Thus this pair has no global quartic common ancestor for the two fixed
targets. The finite principal-part bound makes the exclusion apply at every
direct-limit stage. The lesson is concrete: rank-one first symbols, valid
second contact, and a permitted scalar pole divisor can all hold while the
target-specific highest ancestor coefficient still has forbidden poles.


---

<a id="2026-10-06-localcoh-parity-dual"></a>

## A corrected polynomial-dual exclusion for the normalized parity family

Date: 2026-10-06. Status: **PROVED BY AN EXACT POLYNOMIAL IDENTITY** over QQ,
hence over every characteristic-zero extension. This is a family exclusion
inside the finite quartic local-cohomology problem for C0. It does not
resolve the full quartic incidence or the general projective STCI question.

### The family and statement

In the balanced normal frame, take the degree2 normal-dual direction

    nu=(1+t²,c t),

with pure cubic top symbol coefficient h=1. For c≠0 its homogeneous pair
(s²+t²,c st) is coprime and has primitive degree2. The calculation also
includes c=0 as a boundary specialization. The unique nonzero top-lift line
has h constant: the top-image obstruction to h=t has a nonzero constant
component, independent of c. This is checked uniformly by the verifier.

Let a(c,lambda) be the chosen polynomial top lift plus an arbitrary multiple
lambda of the unique T3[-7] section. Every ancestor with this normalized top
symbol has this form. Let L(a) be the74×18 actual quartic multiplication
matrix from the exact tensor, whose target columns are e72 and e73.

There is a polynomial row vector n(c,lambda) over QQ[c,lambda] such that

    n(c,lambda)^T L(a(c,lambda)) = 0,
    n(c,lambda)^T e72 = 1.

Consequently **no quartic multiplier produces u at any point of this
family**, even over an algebraic closure. In particular this family has no
common quartic ancestor for u,v. The assertion includes every lower T3
coefficient and every c; it has no exceptional parameter locus. A nonzero
scalar multiple of the top coefficient is absorbed by scaling the ancestor
and the multiplier, so the h=1 normalization loses no nonzero top lift.

The same saved dual has n^T e73 equal to a linear polynomial in c. The one
dual therefore proves the common-ancestor exclusion through u; it should
not be represented as separately excluding v at that linear polynomial's
root. Separate one-target Groebner runs in the companion research lane
returned the unit ideal for both targets, but that additional v assertion
is not needed for this certificate.

### Exact certificate and verification

The complete polynomial coefficients are saved in
`../computations/localcoh-incidence-parity-dual-2026-10-06.json`. There are24
terms in the30 ancestor-coordinate polynomials and173 terms in the74 dual
entries. Terms are stored as rational coefficients with their c and lambda
exponents, so the identity is portable and inspectable.

Run from the repository root:

    python3 research/computations/localcoh-incidence-parity-dual-2026-10-06.py

This uses only Python's standard library. It checks coordinate-file hashes,
source-basis agreement, the top symbol and its h=t obstruction, contracts
all540 actual quartic products, multiplies the polynomial dual, and verifies
all18 zero identities plus the constant1 target identity. It contains no
Groebner call and no sampling.

The exact discovery/reproduction script is
`../computations/localcoh-incidence-parity-dual-2026-10-06.m2`. Its polynomial
ring has only c,lambda. For the74×18 matrix L it computes the kernel of
transpose L, evaluates its generators on e72, verifies that this evaluated
ideal is the unit ideal, and lifts1 through those generators. The resulting
polynomial dual is also saved in a readable text file with the same basename.
This is a small polynomial module calculation, rather than the unfinished
66-variable full bilinear Groebner attempt. The independent Python identity
check is the mathematical certificate.

### Extension to the nondegenerate unnormalized parity family

The curve has the ambient torus automorphism

    (x,y,z,w) -> (x,l y,l³ z,l⁴ w),     l≠0.

For the balanced normal coordinates U=w-(3/2)tz+(1/2)t⁴ and V=z-t³,
these coordinates scale by l⁴ and l³. Thus the geometric pushforward of a
normal-dual direction (p(t),r(t)) is

    (l⁴ p(t/l), l³ r(t/l)),

up to the immaterial common nonzero scalar used to describe its projective
direction. For p=a0+a2 t² and r=b1 t with a0 a2≠0, divide this pair by
l²a2 and choose l²=a2/a0. The result is

    (1+t²,(b1/a2)t).

Such l exists over an algebraically closed characteristic-zero field. The
pure-top coefficient h remains constant up to a nonzero scalar. Both target
classes are torus eigenvectors (their pullback factors are l^-7 and l^-5),
so existence of an ancestor is preserved up to nonzero target and multiplier
scalings. Therefore the normalized identity excludes the whole primitive
parity family with a0 a2 b1≠0. Cases with a0 a2=0 require separate handling
and are not obtained by this normalization argument.

### Audit provenance and limits

The earlier saved parity monomial-functional script used only the first row
of `basis(4,I)` as if it were the quartic basis. In Macaulay2 that row records
coefficients of one ideal generator, so those products had the wrong degree.
Its asserted vanishing of degree17 coefficients was vacuous. The present
certificate is a corrected proof: it uses the tensor whose quartic columns
sum all four ideal-generator contributions and whose full product span has
exact dimension74=dim E3[-3]. The older faulty script is not part of this
proof.

Validation on Oct6: the complete actual tensor and basis regenerated
byte-identically; Macaulay2 1.26.06 reran the two-variable module calculation;
the standard-library Python verifier checked the polynomial identity. The
remaining degree0/1/2 direction strata and the complete finite quartic
incidence remain separate research tasks.


---

<a id="2026-10-06-mf6-type3-independent-audit"></a>

## Independent audit of the MF6 degree-three nonregular exclusion

Date: 2026-10-06. One bounded audit of
`2026-10-05-mf6-further-audit.md` and
`../computations/verify_mf6_type3.py`. Scope: characteristic zero, the
monomial quartic C0, constant quotient degree e=0, and a hypothetical
(4,6) defining pair with (deg D2,deg D3)=(3,6). No new global candidate is
constructed. No shared report or verifier was edited.

**Verdict:** the stated exclusion of the entire nonregular branch passes.
No mathematical gap was found in the cubic-pole argument. Its conclusion is
that the first-normal ratio must be regular; it does not exclude existence
of the remaining regular member or an STCI representation in other types.

### 1. Why the DVR computation uses the actual quotient

At a support point, choose a lifted support parameter t and complete.
The ambient ring is k[[t,m,y]], where y maps to a generator of E1 and
m lies in N2. The finite-flat length-six algebra B is generated over
R=k[[t]] by m,y: nilpotence turns the ambient formal series into finite
polynomials. Since N4 is saturated, B/N4 is R-free, and it embeds in its
generic algebra K[y]/(y^4). Its image is exactly R[m,y], not an arbitrarily
selected sublattice of that generic algebra.

Modulo y^4 the generic image is

    m=f2*y^2+f3*y^3.

The complete list of necessary generating words is

    1,y,y^2,y^3,m,ym,

because m^2=my^2=y^4=0. In particular no later normal coefficient or
extra word supplied by the sextic can enlarge the degree-three lattice.
The quotient need not itself be Gorenstein; its generation and saturation
are the relevant inputs.

If f2 is regular, subtract f2*y^2 from m, using an allowed R-coefficient
change of generator. Then N3 has coefficient ideal R+R*f3 in the y^3
line, proving

    ord D2=0, ord D3=max(0,-val f3).

If val f2=-a<0, use m as the degree-two pivot. To cancel its y^2
coefficient, an integral combination c*m+d*y^2 must have
d=-c*f2 in R, which forces c into f2^-1 R. Consequently all remaining
degree-three vectors are generated by

    y^3, f2*y^3=ym, (f3/f2)*y^3=f2^-1*m-y^2.

Conversely all three displayed vectors belong to the actual lattice. Thus
its degree-three coefficient ideal is exactly

    R+R*f2+R*(f3/f2),

with minimum valuation min(0,-a,val f3+a), giving

    ord D2=a, ord D3=max(a,-a-val f3).

This is an equality proved over the DVR, not a pole-count heuristic or a
sampling result. Changing to another regular ambient normal frame would
change the displayed f2,f3 but not the resulting canonical defect divisor.
The computation uses the stated local frames on each chart throughout.

### 2. Exhaustion of the triple and quartic parameter spaces

For degree three, I independently recomputed the killing-matrix nullspaces
from the quadratic cocycle already derived by the defect12 verifier.
For every theta!=0 the finite-chart kernel is

    (d0,d1,d2,d3)=(0,2theta,1,0).

At theta=0 it is the span of z^2,z^3; at the missing quotient point it is
the span of 1,z. The latter two families have an unavoidable additional
homogeneous linear factor common to delta,gamma, hence are not flat
triples. This includes the case where that factor vanishes at infinity.
For theta!=0 the corrections gamma_U=3/8 and gamma_V=6theta^4 are units;
the triple is flat. The torus action permits theta=1 without discarding
any nonzero quotient direction.

The verifier builds the full I_C(4) space and imposes both the proportional
first-normal condition and the quadratic triple-membership condition.
The resulting pencil is therefore an ambient quartic pencil, not a list
of abstract first-normal coefficients. Its first-normal map is injective:
the unique ambient first-normal kernel is q^2, which does not contain the
triple. Thus no missing quartic can preserve the prescribed first forms
while changing the cubic coefficient.

The verifier was rerun successfully with

    python3 research/computations/verify_mf6_type3.py

It also reruns the complete degree-one and degree-two exclusions.

### 3. Independent extraction of the cubic coefficients

I checked the formal-root coefficients using a different extraction from
the expanded quartic. Express a local jet in m,y as

    F=h*m+c20*y^2+c11*m*y+c30*y^3+terms of higher relevant order.

Then

    f2=-c20/h, f3=-(c11*f2+c30)/h.

Terms in m^2 or m*y^2 have order at least four after substitution, so they
cannot affect this calculation. Applying these identities directly to
the complete quartics F0,F1 reproduces

    delta=z(z+2),
    P=alpha*z^2(z+2)^2+beta*(z^2+4)(z^4+16),
    N=alpha*z(z+2)(z+4)
      +beta*(z^5+2z^4+16z^2-16z+96),
    h=-2*delta*P,
    f2=3/(8*delta), f3=-N/(16*delta^2*P).

The generic quartic coefficient h is nonzero for every nonzero pencil
member. Thus its formal root is forced in the actual generic sextuple,
and the local lemma applies to the canonical quotient B/N4.

### 4. The resultant and every exceptional cancellation

The exact resultant is

    Res(P,N)=2^34*beta^10*(alpha+4beta).

For beta!=0 the denominator P is a degree-six section, nonzero at
0,-2,infinity. If alpha+4beta!=0, the numerator and denominator are
coprime and its full six zero units produce poles off D2. The local
lattice lemma then gives deg D3>=6+3=9.

At alpha=-4beta, scale beta=1. Direct factorization gives

    P=(z-2)^2*(z^2+2z+4)^2,
    N=(z-2)*(z^4+4z^3+4z^2-48),
    gcd(P,N)=z-2.

Exactly one pole unit cancels, leaving polar degree five off D2 and
deg D3>=5+3=8. The other repeated-root parameters of P do not create
additional cancellations. An independent discriminant check gives

    disc(P)=-2^24*beta^3*(alpha+4beta)^3
            *(alpha^2+80alpha*beta-128beta^2)^2.

At the extra quadratic parameter values the resultant is nonzero, so
the repeated roots retain their full pole multiplicities. All pencil
members with beta!=0 therefore fail the required deg D3=6.

### 5. Direct infinity check for the remaining member

For beta=0 the finite-chart root has

    f3=-(z+4)/(16*z^3*(z+2)^3).

At 0 and -2, f2 has pole order one and f3 has pole order three; the
lattice lemma gives ord D3=2 at each point. There are no further finite
defect points.

I independently expanded the homogeneous F0 in the actual other ambient
chart, using

    x3=1, x2=w, x1=w^3+2U', x0=w^4+V'/2+3wU'.

This follows directly from U'=a'/2 and V'=-3w*a'+2b'; it does not freeze
the moving normal coordinate or substitute w=1/z off the reduced curve.
In m'=U'+V',y'=V', the coefficient-extraction identities in section 3
give

    h'=-2*w^3*(1+2w)^3,
    f2'=6/(w*(1+2w)),
    f3'=-8*(18w^2+8w-1)/(w^3*(1+2w)^3).

At infinity, w=0, both numerators needed for the valuation calculation
are units. Hence the third contribution is again ord D3=2. This proves
the actual divisor equalities

    D3=2D2, H=3D2,

where D2 consists of the three simple points 0,-2,infinity. There is no
inference of the infinity contribution solely from a total degree.

MF6 now gives A=3D2=H. The pole divisor of the first-normal quotient is
H-A, so it is zero. This establishes the claimed nonregular-branch
exclusion. The argument still permits the beta=0 regular member.

### 6. Scope and the retained degree-five caveat

The completed further-audit note correctly retains the degree-five pure
triple family

    delta_U=d0+z^2*r(z), deg r<=3,
    gamma_U=3r/8, gamma_V=-3d0/8.

If d0!=0, there is no common zero: at a finite common zero one would
have r=delta=0, implying d0=0, while gamma_V is a nonzero constant on
the other chart. In particular d0=1,r=0 is flat and the explicitly
recorded quartic -2x0^3x3+3x0^2x1x2-x1^4 passes its triple condition.
Thus the note does not extend the degree-three and
degree-four endpoint-flatness failures to a blanket pure-direction
exclusion.

No additional realization or exclusion follows from this audit. The
remaining regular member, the nonregular type (4,5), e=1, and higher
carrier degrees require their own arguments. The precise distinction
between saturated and ordinary powers from the pairing audit remains
essential at every stage.


---

<a id="2026-10-06-mf6-type4-incidence"></a>

## Remaining e=0 type (d2,d3)=(4,5): exact triple/quartic incidence

Date: 2026-10-06. Characteristic zero; monomial quartic C0. Status:
**proved parameter reduction; exact exploratory quartic and cubic data;
exceptional loci remain open.** No exclusion of this complete defect type
is claimed. The established low-defect and type-three exclusions are in
`2026-10-05-mf6-further-audit.md`, independently audited in
`2026-10-06-mf6-type3-independent-audit.md`.

### Every possible degree-four triple

The two pure constant quotient directions fail flatness for d2=4: their
killing section has an additional degree-two factor common to delta and
gamma. Thus normalize every possible mixed constant quotient to
`m=U+V,ell=V`, using the torus as in the type-three proof.

Multiplication of the exact h2 cocycle by a section delta of O(4) must
kill both Laurent coordinates of `H1(O(-3))`. Its complete kernel is

    delta=A(z^2+2z)+B(z^3-4z)+C(z^4+8z+16),
    gamma_U=3[A+B(z-2)+C(z^2-2z+4)]/8,
    gamma_V=6Aw+6B(1-2w)+48Cw^2.

If C=0, delta and gamma are the degree-three triple data multiplied by
the homogeneous linear section `A+B(z-2)`. That section has a zero,
including infinity if B=0, so the proposed triple is not flat.

If C!=0, normalize C=1 and write

    delta=A(z^2+2z)+B(z^3-4z)+z^4+8z+16,
    R=A+B(z-2)+z^2-2z+4, gamma_U=3R/8.

The elementary identity `delta=z(z+2)R+16` gives the exact resultant
`Res_z(delta,R)=256`, independent of A,B. Thus
there is no finite common zero. At infinity delta_V has value one, so
every point `(A,B)` gives a flat embedded triple. Its D2 divisor is the
degree-four zero divisor of delta and has no infinity component. This
exhausts the triple parameter space rather than selecting a generic chart.

### Complete quartic equation and its cubic-pole constraint

Let `F=sum c_i F_i` range over the complete eight-dimensional quartic
space with first normal form `h(U+V)`; the basis is derived from the
18-dimensional `I_C(4)` by the preceding verifiers. Write

    Q=coeff_y^2 F(m=0,y),
    E=coeff_my F(m,y), K=coeff_y^3 F(m,y).

Containing the specified triple requires exactly the quadratic identity

    delta Q+(3/8)R h=0.

The resulting coefficient matrix is 13 by 8, affine in A,B. It has rank
seven over Q(A,B), so its generic solution space is a unique quartic up
to scalar. The [universal infinity verifier](../computations/verify_mf6_infinity_universal.py)
reconstructs the full coefficient matrix and its polynomial generic kernel
from the complete ambient quartic basis, then constructs S,T and checks
every kernel equation exactly. The generic kernel alone does not describe
the complete quartic family on rank-drop fibers; the full exceptional
fiber and a reduction independent of the generic kernel are supplied by
[the complete type-(4,5) proof](MULTIPLICITY_SIX_QUARTIC_CONTACT.md).

Since delta and R are coprime, the quadratic identity forces `h=delta S`.
S is a section of O(5). The formal cubic coefficient of the quartic is

    f2=3R/(8delta),
    f3=-(3R E+8delta K)/(8delta^2 S)=-T/(8delta^2 S).

At every finite point the third-piece DVR lattice lemma from the preceding
note gives the exact coefficientwise formula

    ord(D3-D2)=max(0,ord S-ord T).

This also holds at finite multiple roots of delta, because R is a unit
there and its pole order in f2 is exactly ord delta. The target d3=5
permits only one total unit of this excess. Therefore every candidate
requires that all but at most one of the finite zeros of S cancel in T.
An additional infinity contribution must be calculated with the moving
second frame whenever S has an infinity zero. It cannot be guessed by
the affine polynomial degrees.

At A=B=0 the matrix has rank seven and its S polynomial, up to scale, is

    41z^5+28z^4+56z^3+176z^2-80z+704.

Its gcd with T is exactly one. Thus the local cubic calculation forces
at least five excess units and d3>=9, excluding this parameter. More
generally, rank seven, a nonzero leading coefficient of S, and coprimality
of S,T are open conditions. This exact point proves that the generic
degree-four triple/quartic incidence is excluded; the surviving possible
parameters lie in a proper algebraic exceptional locus. Additional exact
sample parameters also have gcd one but do not constitute a universal
exclusion.

### Generic calculation and complete boundary control

A generic nullspace vector does not identify every special solution,
and affine loss of degree in S can hide an infinity pole. These are
necessary cautions for any subresultant approach. The attempted full
generic resultant supplied no completed resultant certificate and is
not needed for the retained proof.

The [complete type-(4,5) proof](MULTIPLICITY_SIX_QUARTIC_CONTACT.md)
instead derives a universal second-frame annihilator from the full
incidence space. Its exact coefficient ideal forces A=12,B=4, and its
complete exceptional quartic space is a fixed cubic times linear forms.
The [self-contained checker](../computations/verify_mf6_infinity_universal.py)
reconstructs that incidence, the second-frame transition, the explicit
ideal-membership witnesses and the exceptional fiber. This closes the
stated e=0,(d2,d3)=(4,5) branch under the proof's hypotheses; the earlier
generic gcd calculation alone supplies only its proper-open exclusion.
The separate e=1 types and their precise boundaries are treated in
[the filtration account](../synthesis/normal_filtration_boundary_obstructions.md).



## Consolidated historical supplement: `research/supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md`

The following mathematical arguments, qualifications, and audit boundaries are retained verbatim from the historical supplement. Internal relative links refer to the source's original location.

# Complete rational endpoint ancestor exclusions

For the fixed characteristic-zero quartic, primitive degree-two normal-dual directions and pure cubic top h=t, both specified rational endpoint families fail target-u quartic-ancestor incidence for every admissible direction and every affine lower correction. This conclusion uses the accepted actual tensor and coordinate interpretation, not arbitrary formal multipliers. It does not cover p(0)=0 boundary families, nonendpoint top zeros or arbitrary-degree mates.

The first family has exceptional factors of degrees 2, 4, 4 and 13. Exact polynomial duals over the full quotient fields close all 23 geometric roots. The second has exceptional degrees 2, 2, 3, 4 and 15, and its exact duals close all 26 geometric roots. In each case the rank-29 top map gives the entire lower-lift fiber as an affine line. A left dual annihilates all 18 actual multiplier columns with nonzero target evaluation, normalized to one on the exceptional factors. The projective zero-top stratum is a separate inherited boundary.

The shared mechanism is a certificate in the cokernel of the actual multiplication morphism. The finite list of exceptional factors is a coverage argument; a normalized left dual at each whole factor closes its full parameter fiber. Generic rank or one successful sample would not establish either assertion.

## Degree-fifteen stratum

This is the completed certificate for the finite degree-fifteen exception stratum of one rational endpoint family. The earlier preparation did not itself exclude the stratum; the original-tensor polynomial dual below does. The result and necessary exact support are presented before the reusable construction.

<a id="2026-10-14-localcoh-degree15-fractionfree-certificate"></a>

## Exact result and scope

**Exact family exclusion, verified in the original tensor.** In the accepted second rational
endpoint family of the quartic-ancestor local-cohomology incidence, every root
of

\[
\begin{aligned}
f_{15}(k)={}&243k^{15}+810k^{14}+2646k^{13}+990k^{12}-9465k^{11}
-54222k^{10}-114414k^9-166406k^8\\
&-34359k^7+301686k^6+897946k^5+1296458k^4
+1345117k^3+811630k^2+285598k-610
\end{aligned}
\]

has no affine lower lift satisfying the actual tensor incidence. The new
certificate is a polynomial vector \(n(k,\lambda)\) with 74 coordinates,
reduced modulo the **entire** polynomial \(f_{15}\), satisfying

\[
 n^T L_{\rm actual}(k,\lambda)=0,\qquad n_{72}=1.
\]

The generated vector actually has degree at most **one** in \(\lambda\).
The inherited general corank-one construction allows degree two. These
identities exclude the target for every affine \(\lambda\), including at all
fifteen algebraic roots; this is not root sampling or a numerical rank test.

The accepted cubic and quartic field certificates are premises and were not
rerun. Combining their seven roots with this new certificate removes all
22 finite exception roots in this specific second rational family. This
statement does not enlarge the accepted quartic-ancestor incidence to
arbitrary carriers, change the other family's scope, or resolve the universal
STCI question. The established projective lower-lift boundary remains an
inherited separate premise.

## Direct original-tensor verification

The retained [normalized dual certificate](../computations/general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06-certificate.json) stores the 74 polynomial coordinates over \(\mathbb Q[k]/(f_{15})\). The [independent verifier](../computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py) reconstructs the actual 74-by-18 matrix from the retained tensor and rational-family seed. Using standard-library `Fraction` arithmetic, it checks every coefficient of all 18 column identities, the parameter-degree bound and coordinate 72 equal to one. The final identities are sufficient evidence for this exclusion; construction inverses and auxiliary duals are unnecessary premises.

The certificate is bound to the actual tensor, its coordinate bases, top map and second-family seed. Those inputs retain the accepted geometric interpretation and the completeness of the affine lower-lift fiber. The identity check uses the entire quotient polynomial, so it covers every root and every affine lower parameter without numerical sampling. It does not establish the inherited tensor interpretation or the separate projective boundary anew.

Run from the repository root:

```sh
python3 -B research/computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py --verify --stem general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06
```

The check closes the fifteen-root stratum. Together with the cubic and quartic certificates it closes their combined 22-root exception set; the complete second-family coverage additionally includes the separate quadratic factors and boundary premises described below. Its scope remains the specified ancestor incidence.

## A reusable corank-one dual construction

The complete general construction, including observability, degree-two duals and the companion sharpness example, is owned by [the local-cohomology dual lemma](POLYNOMIAL_DUALS_AND_AFFINE_PENCILS.md). The formulas below give its degree-fifteen specialization.

<a id="2026-10-14-localcoh-degree15-single-block-strategy"></a>

Let the exact pencil be L_can=(lambda*I_18+A;B), where B is 56 by 18 of rank 17. Choose row set I and column set J of size 17, with missing column l. Embed M^-1=B[I,J]^-1 into an 18 by 56 matrix D, and set E=e_l^T, h=(I_18-DB)e_l. The identities

    MM^-1=M^-1M=I_17,  h_l=1,  Bh=0,  DB=I_18-hE

prove rank 17 over the intended quotient algebra. They make no appeal to modular samples. Any row r with rh=0 has the exact lift rDB=r. If a=Ah and (h,a) has an invertible 2-by-2 minor, choose rows F_h,F_a dual to h,a. Then D_0=(I-hF_h)D satisfies D_0B=I-hF_h. This supplies all required transpose lifts by multiplication. Sixteen linear duals and one quadratic dual test target compatibility; their annihilation identities must be checked coefficient by coefficient in the full quotient. If target evaluations generate the unit ideal in the parameter ring, a Bezout combination gives n^TL=0,n^TU=1. A failed denominator or nonunit minor preserves a stratum; it is not an exclusion.

This is a linear-algebraic separation mechanism: the target defines a class in coker L; a normalized annihilator proves that class is nonzero. Parameter-polynomial identities exclude entire families, while pointwise ranks exclude only the points actually checked. The accepted tensor's geometric interpretation, completeness of the affine lower-lift fiber, and the separate projective boundary remain necessary upstream premises.

## Optional polynomial scaling

<a id="2026-10-14-localcoh-polynomial-scaling-design"></a>

For rational polynomial matrices B whose seed denominators are constants times powers of k-1 and k+1, integer row and column exponents can be chosen so their sums dominate each entry's pole order. Diagonal matrices D,E then give a polynomial matrix P=DBE; negative column exponents are allowed only after exact polynomial cancellation is checked. An exact inverse transports as B^-1=EP^-1D. A minimum-weight exponent cover can reduce determinant scaling degree. In this source matrix it reduces 306 to 152 (77 at k=1,75 at k=-1), with 150 nonzero entries and maximal degree 21. These are representation bounds, not an invertibility claim. A constant two-entry row permits one additional column subtraction and pivot, again without proving the remaining determinant nonzero. The retired historical scaling script
reproduced the [polynomial factors](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/validation/2026-10-14-localcoh-degree15-polynomial-scaling-design/selected-block-scaled-polynomials.json) and [constant-row pivot](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/validation/2026-10-14-localcoh-degree15-polynomial-scaling-design/constant-row-peel.json). The source script is available in Git history; it is not part of the current working tree.
from the repository root to regenerate the two outputs.

## First rational family: full parameter and exceptional-field coverage

<a id="source-2026-10-08-session-first-endpoint-completeness-auditmd"></a>

### 1. Scope and independent audit decision

The October 8, 2026 auditor was independent of the certificate producers.
The decision was **proved** under the previously audited actual top map,
coordinate bases and multiplication tensor. For the fixed quartic
\(C_0=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field of
characteristic zero, take a primitive degree-two normal-dual direction
with pure cubic top coefficient `h=t`.
Every admissible direction of the first rational endpoint family fails
target-`u` quartic-ancestor incidence for every affine lower correction.
The generic identity and the four exceptional-field duals cover every
admissible direction, including all 23 exceptional roots. The earlier
21-point remainder after Q2 is closed by Q1, Q3 and Q13. Other endpoint
families, nonendpoint top-zero strata and the unrestricted STCI problem have
separate scope. [Original audit decision](https://github.com/markluxton1/STCI/blob/b3db4bfcc4b70d85a13ff1862b2a81a553f78b39/research/supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#1-verdict).

### 2. Precisely which parameters are covered

Write the normalized direction as

```text
p(t)=1+a1*t+a2*t^2,   r(t)=1+b1*t+b2*t^2,
a1=(k^2+3)/(2(1-k^2)),
a2=-(k^2+2k+3)/(2(k+1)^2),
b1=(k-3)(k^2+2k+3)/((k-1)^2(k+1)),
b2=-2(k^2-4k+5)(k^2+2k+3)^2/((k-1)^3(k+1)^3).
```

The parameter chart is `k!=1,-1`. The fixed-degree homogeneous quadratic
resultant is

```text
8*(k^2+2k+3)^2*(9k^4-21k^3+5k^2-31k+134)
 /((k-1)^6*(k+1)^6).
```

Thus an admissible parameter also avoids the roots of
`qk=k^2+2k+3` and `B=9k^4-21k^3+5k^2-31k+134`. Using a four-by-four
Sylvester determinant matters: a dehomogenized resultant alone could
miss a common root at infinity when a leading coefficient vanishes.
The existing geometric audit and all exceptional-field checkers use
the fixed-size homogeneous determinant.

The [rational classification](LOCAL_COHOMOLOGY_CONORMAL_GEOMETRY.md#4-exact-rational-normalization-when-both-endpoint-coordinates-are-nonzero)
covers the normalized finite directions.
On `2a1+1!=0` its inverse is

```text
k=(32a2+16a1^2+12)/(4(2a1+1)^2).
```

Modulo the top-image equation, this recovers both `a1` and `a2`, and
`k^2-1=-4/(2a1+1)`. The only omitted normalization point at
`2a1+1=0`, equivalently the limit `k=infinity`, is
`(a1,a2,b1,b2)=(-1/2,-1/2,1,-2)`. Its quadratics share `1-t`, so it is
nonprimitive. Neither `k=+/-1` nor `k=infinity` leaves an admissible
first-family point unexamined. The second choice of `b2` and the separate
`p(0)=0` boundary branches belong to the other families and remain outside
this conclusion.

For any admissible `k`, the actual top map `M` has shape `32x30` and rank
29. Its rational nonzero kernel vector `k0` spans its kernel. Consequently
all lifts of the fixed nonzero top are exactly

```text
alpha(k,lambda)=a*(k)+lambda*k0,   lambda in the base field.
```

The rank remains 29 after extension to any characteristic-zero field.
The pure-top check compares all 32 coefficients of
`t*p^i*r^(3-i)`, `i=0,1,2,3`, through degree seven. It verifies both the
constant seed and the vanishing top of the entire `lambda` direction.
This is the whole affine fibre, including every specialization of
`lambda`. A projective point `lambda=infinity` would have zero top after
projective rescaling and is not a lift of this fixed nonzero top. It
belongs to a different stratum; it is not an omitted point of this affine
fibre. Nonzero scalar multiples of `h=t` are absorbed by ancestor scaling
as in the geometric classification.

### 3. Exhaustive partition of the generic denominator

The generic certificate uses the cleared ancestor

```text
alpha_cleared=120*(k-1)^9*(k+1)^9*alpha(k,lambda).
```

This scalar is nonzero throughout the admissible chart. Its exact dual
target value, independent of `lambda`, is

```text
D=89514547200*(k-1)^14*(k+1)^11*Q2^5*qk^8*B*Q1*Q3*Q13,
Q2=k^2-4k+5,
Q1=3k^4-9k^3-19k^2-43k-4,
Q3=13k^4+26k^3+34k^2+6k-7,
Q13=729k^13+1620k^12+2889k^11-11268k^10-26574k^9-39642k^8
    +94014k^7+272968k^6+454897k^5+62256k^4-571463k^3
    -1210068k^2-966908k-379834.
```

The independent countercheck reconstructs this polynomial exactly
from `dual_on_u`, verifies its degree is 76, and verifies all 30 cleared
ancestor coordinates against the rational seed and kernel. It also
checks every one of the eight distinct displayed factors is squarefree
over `QQ`, and that they are pairwise coprime. The factor multiplicities
are retained rather than replaced by a reduced zero locus.

| Factor | Multiplicity in D | Geometric treatment |
|---|---:|---|
| `k-1` | 14 | Outside the rational chart |
| `k+1` | 11 | Outside the rational chart |
| `qk` | 8 | Nonprimitive homogeneous direction |
| `B` | 1 | Nonprimitive homogeneous direction |
| `Q2` | 5 | Exact dual at both geometric roots, every `lambda` |
| `Q1` | 1 | Exact dual at all four geometric roots, every `lambda` |
| `Q3` | 1 | Exact dual at all four geometric roots, every `lambda` |
| `Q13` | 1 | Exact dual at all thirteen geometric roots, every `lambda` |

There is therefore no additional denominator locus. Off its roots the
generic dual gives `n^T L(alpha_cleared)=0` and `n^T u=D!=0`. Since
ancestor clearing is by a nonzero scalar, this excludes the original
ancestor as well. Every root that survives chart and primitivity tests
lies in exactly one of the four exceptional-field loci below.

### 4. Audit of the exceptional-field arithmetic

The saved Q1, Q3 and Q13 duals have verified lambda-degree bounds 2, 1
and 2 respectively. Each vector has 26 nonzero entries. The linear Q3
certificate gives a stronger degree bound within the same all-lambda proof.

The Q1, Q2, Q3, and Q13 default checkers use exact `Fraction` arithmetic
in `K[lambda]`, with `K=QQ[k]/Qi`, and dictionaries for polynomial powers
of `lambda`. Convolution followed by descending reduction implements
the appropriate power-basis multiplication. In particular the Q3
relation is
`k^4=-2k^3-(34/13)k^2-(6/13)k+7/13`, exactly the relation from `Q3`.
For Q13 the lower coefficients divided by the leading coefficient 729
give the reduction relation; rational inverses are computed by solving
the exact multiplication matrix and their products are asserted to be
one. The Q13 rational-expression parser admits only integers, `k`,
rational arithmetic, and nonnegative integral powers.

The fields really are fields. Q2 has discriminant `-4`, hence is
irreducible over `QQ`. The other checkers prove irreducibility through
degree-preserving finite-field reductions and complete Rabin conditions:

| Polynomial | Prime | Monic coefficients in ascending order | Conditions |
|---|---:|---|---|
| Q1 | 23 | `[14,1,9,20,1]` | `x^(23^4)=x`, `gcd(f,x^(23^2)-x)=1` |
| Q3 | 17 | `[6,7,0,2,1]` | `x^(17^4)=x`, `gcd(f,x^(17^2)-x)=1` |
| Q13 | 53 | `[15,43,6,38,30,45,19,21,8,22,31,2,14,1]` | `x^(53^13)=x`, `gcd(f,x^53-x)=1` |

These are the complete tests: the first identity puts every irreducible
factor degree among the divisors of the total degree; for degree four
the gcd condition removes degrees one and two, and for prime degree
thirteen it removes degree one. The first identity also rules out
repeated factors. The integer leading coefficients survive reduction,
so irreducibility lifts to `QQ` by the usual primitive-polynomial
argument. The independent countercheck recomputes the monic reductions
and both conditions with SymPy's separate `galoistools` implementation;
it does not invoke the saved verifier bodies. All conditions passed.

In characteristic zero each `Qi` is separable. Its `deg(Qi)` embeddings
into an algebraically closed characteristic-zero field correspond to
all its geometric roots. Exact polynomial identities over `K[lambda]`
transport through every embedding. A nonzero denominator inverted in
`K` remains nonzero under every such embedding. There are no
`lambda`-denominators: the duals are polynomials, with entry 72 exactly
one, so specialization introduces no exceptional lower-parameter values.

### 5. Actual tensor, full lifts, and direct source binding

The retained tensor has header `30 18 74 542`: thirty ancestor coordinates,
eighteen actual quartic multiplier coordinates, seventy-four quotient
coordinates, and `30*18+2` columns. All exceptional-field checkers read
this tensor, assert the two final columns are `e72` and `e73`, and check
all eighteen identities

```text
sum(row=0..73) n[row](lambda) *
    sum(i=0..29) tensor[row,18*i+col]*alpha[i](lambda) = 0,
for col=0..17,
n[72](lambda)=1.
```

Thus if `L(alpha)*x=u` for any eighteen-coordinate multiplier vector,
left multiplication by `n` would give `0=1`. This argument is valid for
every `lambda` and every field embedding. It does not require trusting
the saved Macaulay2 module command, its evaluation ideal, or the claim
that the returned row spans an entire kernel. One correct exact row is
enough. Failure to reach `u` also rules out the stronger incidence that
requires both target eigenclasses.

The Q3 and Q13 source loops, field relations, irreducibility tests,
target checks, all 32 pure-top coefficient checks, rank-29 Gaussian
elimination, homogeneous resultants, and all eighteen tensor identities
were inspected rather than inferred from terminal success messages.
Q1 and Q2 follow the same complete identity pattern. Every coefficient
certificate binds the actual tensor, bases, top map, rational seed,
saved full dual, and auxiliary generation records by SHA256.

One provenance limitation needed an explicit additional check: the
default Q1/Q2/Q3 verifiers validate the saved field direction and pure-top
lift but do not themselves derive every constant seed/direction
coefficient from the rational first-family expressions. Hash binding
alone does not establish that derivation. The Q13 default verifier does
derive those coefficients directly. The independent countercheck
supplies the missing direct comparison for **all four** fields: all
thirty seed coefficients, all thirty lower slopes, and all six direction
coefficients match the rational first-family source after exact modular
reduction. Every rational denominator is checked nonzero and inverted.
This closes the provenance limitation without editing the existing
checkers or relying on a fresh regeneration of their inputs.

### 6. Exact inputs and replay

The fixed coordinate inputs are the [multiplication tensor](../computations/localcoh-incidence-tensor.txt),
[ancestor and multiplier bases](../computations/localcoh-incidence-bases.txt),
[top map and annihilator](../computations/localcoh-symbol-top.json), and
[first-family seed and lower kernel](../computations/session-localcoh-origin-family-1-seed.json).
Each saved dual lists the SHA256 hashes of its bound inputs, including its
auxiliary generation data.

| Stratum | Exact verification | Saved input |
| --- | --- | --- |
| Generic | [Cleared polynomial identity](../computations/session-localcoh-origin-generic-dual.py) | [Cleared dual](../computations/session-localcoh-origin-family-1-polynomial-dual.json) |
| Q1 | [Field verifier](../computations/verify_session_localcoh_q1_dual_2026_10_07.py) | [Q1 dual](../computations/session_localcoh_q1_dual_audit_2026_10_07.json) |
| Q2 | [Field verifier](../computations/verify_session_localcoh_q2_dual_2026_10_07.py) | [Q2 dual](../computations/session_localcoh_q2_dual_audit_2026_10_07.json) |
| Q3 | [Field verifier](../computations/verify_session_localcoh_q3_dual_2026_10_07.py) | [Q3 dual](../computations/session_localcoh_q3_dual_audit_2026_10_07.json) |
| Q13 | [Field verifier](../computations/verify_session_localcoh_q13_dual_2026_10_07.py) | [Q13 dual](../computations/session_localcoh_q13_dual_audit_2026_10_07.json) |

Run from the repository root with Python 3 and SymPy. The
[geometric audit](../computations/audit_session_localcoh_endpoint_2026_10_07.py)
checks the rational inverse, homogeneous resultant and rank-29 lift and
runs the generic and Q2 verifiers. The next three checks close the
historical 21-point remainder printed by that audit. Use a disposable
checkout for the audit and countercheck reports.

```sh
(
  set -e
  export PYTHONDONTWRITEBYTECODE=1
  python3 research/computations/audit_session_localcoh_endpoint_2026_10_07.py
  for factor in q1 q3 q13; do
    python3 "research/computations/verify_session_localcoh_${factor}_dual_2026_10_07.py"
  done
  python3 research/validation/2026-10-08-first-endpoint-audit/countercheck.py
)
```

The [independent SymPy countercheck](../validation/2026-10-08-first-endpoint-audit/countercheck.py)
checks the full factor partition, multiplicities, finite reductions, and
the rational-source coefficients in all four fields. It reads the frozen
inputs directly without invoking the coefficient verifiers or regenerating
their inputs. The separate [actual tensor reconstruction](#fresh-reconstruction-of-the-complete-actual-tensor)
binds the retained tensor to the actual forms and all multiplication
columns. This shared check can be replayed with Macaulay2.

```sh
M2 --script research/validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2
```

## Second rational family: cubic and quartic exception strata

<a id="source-2026-10-13-evening-localcoh-exception-fieldsmd"></a>

## Exact result currently completed

**PROVED under the audited actual multiplication tensor and coordinate bases:**
every root of both factors

```text
f3=3*k^3+4*k^2+9*k-4
f4=13*k^4+10*k^3+2*k^2-42*k-7
```

is excluded for **every** affine lower-lift parameter `lambda`. These account
for seven of the 22 geometric parameter points still retained after the
accepted generic and quadratic calculations. The degree-fifteen stratum is closed by the exact original-tensor certificate above.

The Macaulay2 computations returned target evaluation ideal `(1)` over each
number-field polynomial ring `K[lambda]` and a polynomial left dual `n` with

```text
n^T L(a*(k)+lambda*k0)=0,
n^T u=1.
```

The cubic dual has 26 nonzero entries and degree at most two in `lambda`.
The quartic dual has 26 nonzero entries and degree at most one in `lambda`.
Consequently these certificates exclude the entire affine lower-lift fibers;
they are not ranks or point samples.

## Full-fiber verification and logical scope

The new standard-library verifier
[`evening_localcoh_family2_exception_fields_2026_10_13.py`](../computations/evening_localcoh_family2_exception_fields_2026_10_13.py)
uses `Fraction`, exact polynomial division, and a restricted AST expression
parser. It works in the quotient `QQ[k]/(f)` represented by coefficient
vectors and separately in its polynomial variable `lambda`. Its certificate
verification rederives every source denominator inverse, all rational
direction expressions, all 30 seed coefficients, the affine slope vector,
and both primitive homogeneous directions. It checks:

1. The actual 32-by-30 top matrix has rank 29 over `QQ`.
2. The specified slope vector is nonzero and every seed plus `lambda*k0`
   satisfies all 32 pure-top identities. Since the top map has one-dimensional
   kernel, this gives every possible affine lift of the specified top.
3. The factor is square-free, so its degree counts distinct geometric roots.
4. The homogeneous Sylvester determinant matches the rational source
   resultant and is a **unit** modulo the factor, so every root has a
   primitive direction and no omitted nonprimitive stratum.
5. The actual tensor target columns are `e72,e73`, the dual coordinate
   `n72` is the constant one, and all eighteen entries of `n^T L` vanish
   identically as polynomials in `lambda` modulo the full factor.

The last identities imply exclusion after every homomorphism from the
quotient into an algebraically closed field of characteristic zero. Thus
coverage of all roots does not depend on accepting a numerical embedding,
a sampled rank, or even the Macaulay2 factorization result. The exact
Macaulay2 `factor` output also reports both factors as irreducible, but the
independent verification only needs square-freeness and the explicitly
checked unit inversions.

The actual tensor and coordinate sources are unchanged and SHA-256-bound
inside each certificate. They are the same tensor sources accepted in the
[previous independent quadratic audit](LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md).
This certificate inherits that audited coordinate interpretation; it does
not reconstruct the ambient quotient basis from fresh geometric generators.


The standard-library verifier above reads the saved exact cubic/quartic certificates under the stems evening-localcoh-family2-cubic-2026-10-13 and evening-localcoh-family2-quartic-2026-10-13. Its default invocation with `cubic quartic` verifies the complete identities; regeneration of kernel generators is unnecessary for checking a saved normalized left dual. One alternative generation method writes L=L0+lambda*L1 and n=n0+lambda*n1+lambda²*n2, equates the four polynomial coefficients of n^TL to zero, and sets the constant target coefficient to one and the other two to zero. This yields a 75-by-222 exact linear system over QQ[k]/(f15). It is a construction method, not additional proof beyond a verified dual.

## Second-family generic coverage and actual tensor meaning

<a id="source-2026-10-08-session-localcoh-family2-genericmd"></a>

## The exact generic denominator locus

**PROVED under the audited actual multiplication tensor and coordinate
bases:** the second rational endpoint family excludes target `u`, for
every lower-correction parameter `lambda`, away from the displayed
denominator roots. After removing chart poles and nonprimitive directions,
the following five square-free, pairwise-coprime factors retain exactly
26 primitive geometric parameter points:

```text
k^2+1
k^2-2k-1
3k^3+4k^2+9k-4
13k^4+10k^3+2k^2-42k-7
243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
 -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
 +1296458k^4+1345117k^3+811630k^2+285598k-610
```

Each retained parameter point still has its complete affine `lambda`
fibre. These are exceptions to this certificate, with no implication
that they support an ancestor or even an actual rank jump. The full factor fibers are closed by the quadratic, cubic, quartic and degree-fifteen certificates in this owner.

## Actual direction and complete affine family

The independently classified second family has

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

Its actual quartic lift is the complete affine line
`a*(k)+lambda*k0`, where the 32-by-30 pure-top map has rank 29 and `k0`
is its nonzero kernel vector. The clearing factors are

```text
B=2(k-1)^3(k+1)^3                  [direction denominator]
A=120(k-1)^9(k+1)^9               [ancestor denominator].
```

The certificate stores `alpha=A*(a*+lambda*k0)`, along with
`P=B*p` and `R=B*r`. Its standard-library verifier checks all four
rational direction formulas by polynomial cross-multiplication, the
rank-29 top map, and the coefficient of `lambda` in each of the thirty
ancestor coordinates. It verifies all 32 cleared pure-top identities

```text
B^3 * M(alpha) = A * coefficients(t*P^i*R^(3-i)), i=0,1,2,3.
```

Since `A` and `B` are nonzero on the retained chart, these checks prove
coverage of the entire affine lift fibre at every retained parameter.

## Exact polynomial dual

The saved full 74-by-18 module calculation over `QQ(k)[lambda]` returned
target evaluation ideal `(1)` and a complete polynomial left dual. The
cleared dual has 26 nonzero entries and degree at most two in `lambda`.
Its exact target value is

```text
D=89514547200*(k-1)^15*(k+1)^12*(k^2+1)^5*(k^2-2k-1)^5
 *(k^2+2k+3)^4*(3k^3+4k^2+9k-4)
 *(3k^4-2k^3-6k^2-18k-9)*(13k^4+10k^3+2k^2-42k-7)
 *(243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
   -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
   +1296458k^4+1345117k^3+811630k^2+285598k-610).
```

The verifier checks all eighteen actual tensor-column identities
`n^T L(alpha)=0` over `QQ[k,lambda]` and `n^T u=D`. It also checks
the actual target columns in the stored tensor are `e72,e73`.
Therefore target `u` cannot lie in the multiplier image wherever `D!=0`,
for every value of `lambda`.

A fixed four-by-four homogeneous Sylvester determinant gives

```text
Res_hom(p,r)=-8*(k^2+2k+3)*(3k^4-2k^3-6k^2-18k-9)
             /((k-1)^5*(k+1)^6).
```

Thus `k=+/-1` are chart poles, while the roots of `k^2+2k+3` and
`3k^4-2k^3-6k^2-18k-9` are nonprimitive. The independent verifier
reconstructs the full factorization of `D`; verifies the five remaining
factors are square-free and pairwise coprime; and verifies they are
coprime to both the chart factor and the homogeneous resultant numerator.
This establishes the precise count and scope of the retained 26 points.


<a id="source-2026-10-08-session-localcoh-family2-quadraticsmd"></a>

## Exact fields and independent coefficient reconstruction

The two computations use

```text
Kplus=QQ[k]/(k^2+1),       k^2=-1,       discriminant=-4;
Kminus=QQ[k]/(k^2-2k-1),  k^2=2k+1,     discriminant=8.
```

Both quadratics are irreducible over `QQ`, since their discriminants
are nonzero rational nonsquares. A single standard-library verifier
implements exact arithmetic in both fields with rational coefficient
pairs. For `k^2=c+d*k`, it inverts `a+b*k` by the explicit formula

```text
(a+b*k)^(-1) = (a+d*b-b*k)/(a^2+d*a*b-c*b^2).
```

Every rational source denominator is checked by this norm formula to
be a field unit. A restricted AST parser, with no `eval`, reconstructs
all source expressions directly in the quadratic field and its
polynomial ring in `lambda`. On every default verification run, it
rederives all thirty saved seed coefficients, all thirty lower slopes,
and the four direction coefficients from the family2 rational expressions.
It compares them exactly with the certificate; it does not merely trust
a previously reduced coefficient table or a point sample.

The explicit direction formulas checked are

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

In both fields the verifier checks all 32 actual pure-top identities,
the rank-29 top map, and that the coefficient of `lambda` in the lift
is the exact nonzero kernel vector. Thus the full affine lift fibre is
covered. Its fixed four-by-four Sylvester determinant confirms the
homogeneous direction is primitive, even though `r` loses its quadratic
coefficient at these parameter values.

## Full polynomial duals

Separate reduced 74-by-18 modules were generated from the actual tensor,
using the directly reconstructed field coefficients. In each field,
Macaulay2 computed the full polynomial left-kernel module over `K[lambda]`
and returned target evaluation ideal `(1)`. The resulting duals each have
27 nonzero entries and degree at most two in `lambda`.

The independent verifier checks every coefficient of all eighteen
identities `n^T L(a*+lambda*k0)=0`, and checks `n^T u=1`. It checks the
actual target columns in the tensor are `e72,e73`, so the target evaluation
is tied to the same actual multiplier incidence. Since the fields are
quadratic and separable in characteristic zero, these identities hold
through both embeddings of each field into an algebraic closure. No
specialization or generic-rank extrapolation enters the conclusion.


<a id="source-2026-10-08-session-localcoh-family2-quadratic-independent-auditmd"></a>

## Actual forms, top map, and complete parameter fibre

The independent
[`countercheck.py`](../validation/2026-10-08-family2-quadratic-audit/countercheck.py)
parses the displayed stage-four ancestor numerators and quartic forms in
[`localcoh-incidence-bases.txt`](../computations/localcoh-incidence-bases.txt).
It verifies the quartics are the following **actual degree-four forms**:

```text
q=xw-yz, A=x^2z-y^3, B=xz^2-y^2w, C=yw^2-z^3;
q*(x^2,xy,xw,yz,zw,w^2),
A*(x,y,z,w), B*(x,y,z,w), C*(x,y,z,w).
```

They all vanish on `C0` and have independent coefficient vectors of rank
18. The restriction of the 35 degree-four monomials to `C0` has rank 17,
so the displayed forms span exactly the full degree-four ideal piece.
They are not four-coordinate generator rows mistaken for polynomial forms.

The checker independently substitutes `x=1,y=t,z=t^3+a,w=t^4+ta+q`
in every actual ancestor numerator. It extracts its normal-order-three
part, converts it to the previously audited balanced normal coordinates,
and computes all four degree-six residues. All thirty top columns match
the saved top map literally. The resulting `32x30` matrix has rank 29.
Its nonzero rational kernel vector is exactly the lower slope in the
family2 seed. Consequently every lift of the specified nonzero pure top
is the full affine line

```text
alpha(k,lambda)=a*(k)+lambda*k0.
```

At each quadratic field, all thirty constant seed coefficients and all
thirty slopes are compared directly to the rational family2 source, and
all six direction coefficients are compared to the same source. Every
source denominator is inverted only after checking it is a unit modulo
the defining quadratic. All 32 coefficients of the specified actual
normalization `t*p^i*r^(3-i)`, `i=0,1,2,3`, match the top of `alpha`.
Thus no lower parameter is lost through sampling or a generic-rank
argument. The projective limit with zero top is a different stratum,
not a lift of this fixed nonzero top.

The independent fixed-size homogeneous Sylvester determinant is nonzero
in each field even though `r` loses its quadratic coefficient there:

| Field | Chosen exact embedding | Homogeneous resultant |
|---|---|---|
| `QQ[k]/(k^2+1)` | `k=i` | `-8i` |
| `QQ[k]/(k^2-2k-1)` | `k=1+sqrt(2)` | `-96+68sqrt(2)` |

The second norm is `-32`, so neither conjugate resultant vanishes. Both
quadratics are coprime to the chart-pole factor and homogeneous
nonprimitive factors. These four parameters are admissible primitive
directions, not excluded chart or normalization points.

## Fresh reconstruction of the complete actual tensor

The independent
[`actual-tensor-reconstruction.m2`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2)
rebuilds the ancestor space from the Ext map, verifies that it has
dimension 30 and that the map is injective in degree `-7`, and sums all
four ideal-generator contributions to obtain actual quartic forms.
Every one of its thirty degree-thirteen ancestor polynomial entries and
eighteen quartic polynomial entries agrees literally with the frozen
displayed bases. It additionally verifies `I^4*h subset (q^4,B^4)` for
each ancestor and every generator of `I^4`.

All 540 actual ancestor-times-quartic product columns and the two target
columns are reduced modulo `(q^4,B^4)` afresh. Their full coefficient
matrix has rank 74, the product-only matrix already has rank 74, and
the independent compressed matrix is **literally equal** to the retained
`74x542` tensor. The union of the uncompressed coefficient rows and stored
rows also has rank 74. Thus no quotient equation or target row was lost
through compression. The entire degree `-3` stage-three Ext image is
independently reconstructed in the same quotient, its injection is
verified, and its union with the 540 product columns has rank 74. This
establishes actual equality with the complete next-stage image, beyond
merely matching its abstract dimension.


The [generic certificate/verifier](../computations/verify_session_localcoh_family2_generic_2026_10_08.py), [quadratic certificates/verifier](../computations/verify_session_localcoh_family2_quadratics_2026_10_08.py) and [independent quadratic countercheck](../validation/2026-10-08-family2-quadratic-audit/countercheck.py) supply exact support for these assertions. Their raw inputs are part of the proof dependency closure. Source hashes and successful process records alone do not establish that the tensor represents the complete actual incidence; the Ext and polynomial reconstruction above does.

## Characteristic of the tensor and dual certificates

An exact annihilator identity nᵀL=0,nᵀu=1 excludes the target over any coefficient algebra in which it is defined. The certificates here, however, use the characteristic-zero balanced frame, rational denominators, polynomial quotient units and rank29 source coverage. Reduction modulo a prime requires verifying that the geometric tensor still represents the same complete actual source and that every cleared denominator and normalized target unit survives; the present rational certificates do not establish those checks. In particular characteristic2 changes the conormal splitting. Polynomial duality as a mechanism extends, whereas these particular family exclusions retain their audited characteristic-zero scope. [the every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) shows why a universal positive-characteristic nonexistence conclusion would be false.


---

## Source: 2026-10-14-generalization-localcoh-pencil-independent-review.md

# Independent review of the observable corank-one pencil theorem

Date: 2026-10-14. Reviewer: root. Status: **PROVED under the stated exact
rank hypotheses**. This reviews the new abstract theorem in
[the polynomial-dual note](POLYNOMIAL_DUALS_AND_AFFINE_PENCILS.md), not
any previously accepted tensor computation.

For a field `K`, consider `L(lambda)=(lambda I_q+A; B)` with
`rank B=q-1` and `rank(B;BA)=q`. These hypotheses give a generator
`h` of `ker B` with `h,Ah` independent. If the lower target is outside
`im B`, a constant normalized left dual excludes it. Otherwise choose
`Bc=w`. Every prospective solution has the form `c+t h`. After a
constant basis change making `h=e1,Ah=e2`, and choosing `c1=0`, its
top equation is exactly

```
t(lambda e1+e2)=p-lambda c,  p=v-Ac.
```

Eliminating `t` gives the `q-2` linear equations
`p_j-lambda c_j=0` for `j>=3`, and the single quadratic
`p1-lambda p2+lambda^2 c2=0`. The direction `lambda e1+e2` never
vanishes, so these equations are sufficient as well as necessary,
including every finite geometric parameter value.

For a matrix `D` with `DB=diag(0,1,...,1)` and `Dw=c`, each row
`t` annihilating `lambda h+Ah` defines the left dual

```
(t, -t(lambda I_q+A)D).
```

Direct multiplication gives zero on `L`, and evaluation on the target
gives `t(p-lambda c)`. Rows `e_j` give the linear residuals with dual
degree at most one; `e1-lambda e2` gives the quadratic with dual
degree at most two. If the linear residual ideal is the unit ideal,
constant coefficients already produce one. If it has a common
linear factor, division of the quadratic by that factor gives the
stated Bezout identity with coefficient degree at most one. If all
linear residuals vanish identically, exclusion requires the quadratic
to be a nonzero constant. Thus full geometric exclusion is equivalent
to a normalized polynomial dual of degree at most two. The bound is
complete on this locus, not a guess about a syzygy search.

I also checked the note's rank-drop counterexample and determinantal
fallback. At an unobservable point the specialized left kernel can
grow, and normalized global polynomial duals need not detect an
exclusion there. The rank-stratified minor ideals retain this
exception. Over a parameter ring, the field rank hypotheses and any
pivots must be certified throughout the stratum; a generic matrix
calculation is insufficient.

This review accepts the abstract algebra and its finite-dimensional
reduction. It does not certify any particular family-two exceptional
field computation, any unrecorded rank stratum, the projective lift
at infinity, or the full ancestor incidence. Those applications have
separate evidence records.

## Current exact verification

The saved degree-fifteen certificate was verified successfully in the consolidated tree: all18 original-tensor polynomial column identities vanish modulo the entire degree-fifteen polynomial, the dual has degree at most2 in the affine parameter, and coordinate72 is exactly1. The mathematical inputs and source hashes are retained; absent process metadata is not a prerequisite for this identity check. This is a replay of the normalized dual against its complete actual tensor, not a fresh reconstruction of that tensor or a rerun of every inherited family computation.



## Consolidated historical supplement: `research/supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md`

The following mathematical arguments, qualifications, and audit boundaries are retained verbatim from the historical supplement. Internal relative links refer to the source's original location.

# Local-cohomology direction spaces and apolarity

Consolidated mathematical source material. Original claims, calculations, and qualifications are preserved; audits have the review scopes stated below.

The [current finite continuation](../results/quartic_ancestor_direction_reduction.md)
excludes all constant and quadratic directions and the linear endpoint
boundary. It leaves an explicit line and degree-twelve curve of linear
directions for the two lower target equations. The scoped arguments
below supply its antecedents and independent controls.

---

<a id="2026-10-05-localcoh-degree4"></a>

## Degree-four local-cohomology frontier: finite reduction and ruling slices

Date: 2026-10-05.  This investigation concerns only the characteristic-zero
monomial quartic

\[
C_0=[s^4:s^3t:st^3:t^4],\quad
I=(q,A,B,C),\quad q=xw-yz,
\]

with \(A=x^2z-y^3\), \(B=xz^2-y^2w\), and \(C=yw^2-z^3\).
The target classes remain
\(u=xz/(qB),\ v=yw/(qB)\), both of degree \(-3\).
The question is whether \(F\alpha=u,G\alpha=v\) with quartic \(F,G\)
and \(\alpha\) of degree \(-7\).  No general STCI conclusion is claimed.

### New all-stage exclusion: both ruling-ratio slices

**Proved, conditional only on the already proved P-010 and P-037.**  There is
no common ancestor for any quartic pair whose nonzero first-conormal symbols
have ratio a Möbius transform of either \(t\) or \(t^3\) on the chart
\([1:t:t^3:t^4]\).  This excludes each full 14-dimensional linear slice,
including all its boundary specializations.  P-043's one-parameter family is
contained in the ratio-\(t\) slice.

This is an all-stage proof; it does not infer a direct-limit conclusion from
a finite stage scan.  Its ingredients are explained below.

#### The complete linear classification of the ratio-t slice

If \(\sigma(G)=t\sigma(F)\), then \(xG-yF\) vanishes to second order
along \(C_0\).  Every quintic with this property is \(qD\), with
\(D\in I_3\): on \(Q=V(q)\), a degree-five section vanishing twice along
the type-\((1,3)\) curve would have residual class \((3,-1)\), which has
no sections.  Dividing by \(q\) leaves a cubic vanishing on the curve.
The identity

\[
xG-yF=qD=(xw-yz)D
\]

then implies \(x(G-wD)=y(F-zD)\).  Since \(x,y\) are coprime,
there is a cubic \(H\) such that

\[
\boxed{F=xH+zD,\qquad G=yH+wD,\qquad H,D\in I_3.}
\]

The restriction of \(F\) to the integral curve shows \(H\in I_3\),
and the representation is unique.  Conversely every such pair has ratio
\(t\) to first order.  Since \(\dim I_3=7\), the slice has dimension 14,
including its two-dimensional kernel of the first-symbol map.

The exact determinant identities are

\[
xG-yF=qD,\qquad wF-zG=qH.
\]

For P-039, one has \(H=A-\lambda B\), \(D=\lambda A\).

#### A surviving pair must be coprime, with independent cubic symbols

If a nonconstant \(T\) divides both \(F,G\), then \(T\alpha\) is a
common ancestor with multipliers of degree at most three, contradicting
P-037.  Thus any surviving pair is ambient-coprime.

If \(\sigma(H),\sigma(D)\) are proportional, P-037's characteristic-zero
cubic classification gives either a scalar pair \(H,D\), or two
\(q\)-divisible cubics.  In the scalar case the resulting \(F,G\) share
a cubic factor; in the second they share \(q\).  Hence a surviving pair
must have generically independent \(\sigma(H),\sigma(D)\).

#### Ancestors of principal-part order at most three are impossible

Write
\(\mathcal T_n=(0:_{\mathcal H^2_{C_0}(O_{\mathbf P^3})}I^n)\).
The balanced normal bundle gives

\[
(\mathcal T_n/\mathcal T_{n-1})(-7)
\simeq O_{\mathbf P^1}(7n-21)^{\oplus n}.
\]

Thus \(H^0(\mathcal T_2(-7))=0\).  Suppose the ancestor has order three.
Its highest symbol is a nonzero constant quadratic in the two balanced
normal-dual directions.  Since multiplying by the nonzero linear normal
symbol of \(F\) must kill its highest symbol, that quadratic is a pure
square.  In characteristic zero, a homogeneous polynomial killed by a
nonzero constant directional derivative is a power of the perpendicular
direction.  The pure square is nowhere zero because its coefficients lie in
\(H^0(O_{\mathbf P^1})\).

The cyclic inverse system generated by such an ancestor defines an embedded
primitive triple with conormal line \(O(-7)\).  Here is the local statement
that makes the implication precise.  After choosing normal coordinates
\(\xi,\eta\), an order-three inverse system with normalized pure-square
top term is

\[
\alpha=\xi^{-1}\eta^{-3}
 +c\xi^{-2}\eta^{-1}
 +d\xi^{-1}\eta^{-2}
 +e\xi^{-1}\eta^{-1},\qquad c,d,e\in k[[z]].
\]

Its annihilator is
\((\xi-c\eta^2,\eta^3)\).  Its cyclic module is free of rank three over
\(k[[z]]\), with basis \(\alpha,\eta\alpha,\eta^2\alpha\), and it is
curvilinear in every transverse fiber.  These annihilator ideals glue,
because changing the trivialization multiplies the ancestor by a unit.
The constant balanced direction identifies the conormal line as \(O(-7)\).
P-010 excludes exactly this primitive triple in characteristic zero.

Consequently any quartic common ancestor would have principal-part order at
least four.  This argument applies to every quartic multiplier pair with
nonzero first symbol, not just to ruling ratios.

#### Every higher principal-part order in the ruling slice is impossible

Work at the generic point of the curve and let the highest order be \(n\ge4\).
The first symbols of \(F,G\) are proportional and nonzero.  Their action on
the highest symbol of \(\alpha\) must vanish, because the targets lie in
\(\mathcal T_1\).  Therefore that highest inverse-system symbol is
\(c\nu^{n-1}\) for a nonzero normal-dual vector \(\nu\), with

\[
\sigma(F)(\nu)=\sigma(G)(\nu)=0.
\]

The exact determinant identity also gives

\[
qD\alpha=xv-yu\in\mathcal T_1.
\]

Its highest action is double contraction, a nonzero characteristic-zero
scalar times
\(q(\nu)D(\nu)\nu^{n-3}\).  Because \(n-3\ge1\), it cannot be a
socle term unless

\[
q(\nu)D(\nu)=0.
\]

If \(q(\nu)\ne0\), then \(D(\nu)=0\), and
\(F=xH+zD\) forces \(H(\nu)=0\) as well.  This contradicts the
independence of the two cubic first symbols.

Therefore \(q(\nu)=0\).  The common quartic first-symbol direction must
then be the quadric direction.  But a quartic with that direction restricts
to a section on \(Q\) vanishing twice along \(C_0\); its residual class
is \((2,-2)\), which is ineffective.  Thus \(q\) divides both \(F,G\),
contradicting coprimality.  This completes the all-stage exclusion.

Transposing the quadric matrix gives the second ruling slice

\[
F=xH+yD,\qquad G=zH+wD,
\quad xG-zF=qD,\quad wF-yG=qH,
\]

with first-symbol ratio \(t^3\).  The identical contraction argument
applies.  Constant invertible changes of the two equations give every
Möbius transform of either ratio; they also change the target pair by an
invertible constant matrix, preserving its independence and socle order.

### Independent exact computation of the low principal parts

**Exact computation over QQ, hence stable under extension to any
characteristic-zero field.**  The Macaulay2 script
`../computations/verify_localcoh_finite_principal_parts.m2` computes

\[
\dim H^0(\mathcal T_n(-7))=0,0,1,30,105\quad(n=1,2,3,4,5).
\]

It also computes that for the unique nonzero order-three section \(a_3\),

\[
\{F\in S_4: IFa_3=0\}=kq^2.
\]

Thus the order-three exclusion is independently corroborated by exact
canonical-module algebra.  The one-dimensional space
\(H^0(\mathcal T_3(-7))\) is **not zero**; any attempted proof based on
its vanishing would be false.  Its surviving top quadratic is nondegenerate,
so it cannot be the pure square needed by a quartic first-order multiplier.

The canonical module \(E_n=\operatorname{Ext}^2_S(S/I^n,S)\) has depth at
least two, and its sheaf is \(\mathcal T_n\).  Thus its degree \(-7\)
piece computes the displayed global sections without a vertex correction.
The script calculates the colon ideal with Gröbner algebra and checks its
degree-four dimension and membership of \(q^2\), rather than only sampling
multipliers.

The Python script
`../computations/verify_localcoh_quartic_ratio_t_slice.py` independently
checks the exact 14-dimensional classification of both ruling slices, all
determinant identities, and the P-039 specialization.

### Uniform finite reduction for the remaining degree-four locus

The separate audit in `2026-10-05-localcoh-finite-bound.md` proves the
following reduction.  Coprime quartics have generic transverse intersection
length \(m\le4\) along \(C_0\), by Bézout.  Equality would exhaust the
complete-intersection degree and produce a \((4,4)\) STCI, which is excluded
by the recorded Craighero--Gattazzo result.  Hence \(m\le3\).

Since \(IF\alpha=IG\alpha=0\), the Artin-algebra inclusion
\(I^m\subset(F,G)\) at the generic point gives
\(I^{m+1}\alpha=0\) there.  Finite Laurent inverse systems are torsion-free
over the curve's local DVR, so this annihilation extends along the whole
curve.  Consequently

\[
\boxed{\alpha\in H^0(\mathcal T_4(-7)),\qquad \dim=30.}
\]

This removes the unbounded-stage issue for **all** degree-four pairs.  The
exact Ext map to \(S/(q^4,B^4)(20)\) injects these 30 sections into the
fixed diagonal Čech stage \(N=4\), where their numerator degree is 13.
Thus the remaining problem is a finite bilinear incidence problem between
30 ancestor coordinates and the two 18-dimensional quartic multiplier
spaces, with target numerators
\(xz(qB)^3\) and \(yw(qB)^3\), of degree 17.

The order-three argument above forces a survivor's order to be exactly four.
Its top symbol is a pure cubic.  If its primitive normal-dual direction has
projective degree \(e\), the top coefficient has degree \(7-3e\);
therefore \(e\le2\).  This sharply reduces the remaining conormal
classification, but does not by itself exclude it.

### Limitations and highest-value continuation

The full degree-four locus is still open.  The new geometric theorem excludes
two entire ruling-ratio slices and their Möbius transforms; it does not
classify arbitrary ratios between scalar factors of a common conormal
direction.  The finite bound uses the known characteristic-zero \((4,4)\)
exclusion and is not asserted in positive characteristic.  The contraction
and primitive-triple argument also use characteristic zero.

The remaining high-value task is to classify primitive conormal directions
of degree \(e=0,1,2\) that support two ambient-coprime quartics, then impose
the order-four symbol-lifting equations in the 30-dimensional exact ancestor
space.  This is a finite geometric/algebraic problem, not an invitation to
repeat increasingly high direct-limit stage scans.

Validated with Python 3.14.8, SymPy 1.14.0 and Macaulay2 1.26.06; both dedicated scripts passed.


---

<a id="2026-10-05-localcoh-direction-image"></a>

## Exact quartic symbol image and primitive direction strata

Date: 2026-10-05. This note works in characteristic zero, on the smooth
monomial rational quartic

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_{x,y,z,w}.
\]

It is a first-conormal calculation. It does not assert existence or
nonexistence of a common local-cohomology ancestor, or of an STCI pair.
The exact companion script is
`research/computations/verify_localcoh_direction_image.py`.

### 1. The image, with the frame fixed explicitly

On the chart \(x=1\), use \(t=y\) and the balanced conormal frame

\[
 U=w-t^4-\frac32t(z-t^3),\qquad V=z-t^3.
\]

For a quartic \(F\in I_{C_0}(4)\), its first normal symbol is

\[
 \sigma(F)=P(t)U+Q(t)V,
\]

where

\[
 P=F_w(1,t,t^3,t^4),\qquad
 Q=(F_z+\tfrac32yF_w)(1,t,t^3,t^4).
\]

Both coefficient polynomials have degree at most nine. If \(P_i,Q_i\)
denote their coefficients of \(t^i\), the image is exactly

\[
 \boxed{\mathcal V=\{(P,Q)\in H^0(O(9))^2:
 P_1=2Q_2,\ P_4=2Q_5,\ P_7=2Q_8\}.}
\]

Thus \(\dim\mathcal V=17\), whereas \(\dim I_{C_0}(4)=18\). The kernel is
\(kq^2\), where

\[
 q=xw-yz,\quad A=x^2z-y^3,\quad B=xz^2-y^2w,\quad C=yw^2-z^3.
\]

Here is a direct proof and a usable inverse. Put

\[
 R=Q-\frac t2P.
\]

For the three cubic generators their affine symbols and resulting \(R\)
are

\[
\begin{array}{c|c|c}
\text{generator}&(P,Q)&R\\\hline
A&(0,1)&1\\
B&(-t^2,\tfrac12t^3)&t^3\\
C&(2t^5,0)&-t^6.
\end{array}
\]

Multiplication by \(x,y,z,w\) multiplies the symbol by
\(1,t,t^3,t^4\), respectively. A symbol \(qH\), with \(H\) quadratic,
is \((p,\frac t2p)\), where \(p=H|_{C_0}\) can be any polynomial of
degree at most eight. Consequently all image symbols have

\[
 R_2=R_5=R_8=0.
\]

Conversely, let \((P,Q)\) satisfy these three equations and define

\[
 J=R_0xA+R_1yA+R_3zA+R_4wA
   +R_6zB+R_7wB-R_9zC-R_{10}wC.
\]

Then

\[
 P_J=-R_6t^5-R_7t^6-2R_9t^8-2R_{10}t^9,
\quad R_J=R.
\]

Since \(Q\) has degree at most nine,
\(R_{10}=-P_9/2\). Hence \(p=P-P_J\) has degree at most eight.
Choose the quadratic lift

\[
 H(p)=p_0x^2+p_1xy+p_2y^2+p_3xz+p_4xw
        +p_5yw+p_6z^2+p_7zw+p_8w^2.
\]

Every quartic with the prescribed symbol is exactly

\[
 \boxed{F=qH(p)+J+cq^2,\qquad c\in k.}
\]

Indeed, the nine forms \(qH(t^i)\), the eight displayed summands of
\(J\), and \(q^2\) are independent quartics in the ideal. The restriction
map from the 35-dimensional space of quartics to \(H^0(O(16))\) is
surjective: quartic monomials on \(C_0\) attain every exponent
\(0,\ldots,16\). Thus \(\dim I_{C_0}(4)=35-17=18\), proving that these
18 forms exhaust it.

### 2. Intersections with primitive binary directions

Write a primitive direction of degree \(e\) as

\[
 r=(r_1,r_2),\qquad
 r_1(s,t)=\sum_{i=0}^e a_i s^{e-i}t^i,\quad
 r_2(s,t)=\sum_{i=0}^e b_i s^{e-i}t^i.
\]

Primitive means the homogeneous binary forms have no common zero. In
particular, this is stronger than checking an affine gcd alone. Write

\[
 h(s,t)=\sum_{j=0}^{9-e}h_j s^{9-e-j}t^j.
\]

The multiplication map \(h\mapsto(r_1h,r_2h)\) is injective, so the
dimension of \(\mathcal V\cap rH^0(O(9-e))\) is the nullity of the
following three scalar equations:

\[
 \boxed{\sum_{i=0}^e a_i h_{3k+1-i}
          -2\sum_{i=0}^e b_i h_{3k+2-i}=0,
          \qquad k=0,1,2,}
\]

where coefficients outside \(0\le j\le9-e\) are zero.

#### Degree zero

Each row has coefficients \((a_0,-2b_0)\) in a separate pair of columns.
The direction is nonzero, so all three rows are independent. Therefore

\[
 \boxed{e=0:\quad \dim(\mathcal V\cap rH^0(O(9)))=7}
\]

for every direction.

#### Degree one

Each row is the coefficient triple

\[
 (a_1,\ a_0-2b_1,\ -2b_0)
\]

in its own block of three scalar coefficients. Thus the matrix has rank
three unless all three entries vanish; in the latter case its rank is
zero. The exceptional equations imply

\[
 r=(2b_1s,b_1t),\qquad b_1\ne0.
\]

Consequently

\[
 \boxed{e=1:\quad
 \dim(\mathcal V\cap rH^0(O(8)))=
 \begin{cases}
 9,&r\sim(2s,t),\\
 6,&\text{otherwise}.
 \end{cases}}
\]

The exceptional point is precisely the quadric symbol direction. Its
quartic preimage is \(qS_2\), of dimension ten, because all its symbols
are provided by \(qH\) and its one-dimensional symbol kernel is
\(kq^2\).

#### Degree two

Set

\[
 D=a_1-2b_2,\quad E=a_0-2b_1,\quad
 T=a_2,\quad K=-2b_0.
\]

In the coefficient basis \((h_0,\ldots,h_7)\), the constraint matrix is

\[
 \begin{pmatrix}
 D&E&K&0&0&0&0&0\\
 0&0&T&D&E&K&0&0\\
 0&0&0&0&0&T&D&E
 \end{pmatrix}.
\]

If \(D\ne0\) or \(E\ne0\), its minors in columns \((0,3,6)\) and
\((1,4,7)\) are \(D^3\) and \(E^3\), so its rank is three. When
\(D=E=0\), its only possibly nonzero columns are \(h_2,h_5\), with
matrix

\[
 \begin{pmatrix}K&0\\T&K\\0&T\end{pmatrix}.
\]

This has rank two provided \((T,K)\ne(0,0)\). If \(T=K=0\) as well,
then

\[
 r=(2s(b_1s+b_2t),\ t(b_1s+b_2t)),
\]

which is not primitive. Hence

\[
 \boxed{e=2:\quad
 \dim(\mathcal V\cap rH^0(O(7)))=
 \begin{cases}
 6,&a_0=2b_1\text{ and }a_1=2b_2,\\
 5,&\text{otherwise},
 \end{cases}}
\]

always under the primitive hypothesis. Both strata occur: \((t^2,s^2)\)
is primitive and exceptional, while \((s^2,t^2)\) is primitive and
generic. The exceptional locus is the primitive open subset of the
projective three-space

\[
 r_1=2b_1s^2+2b_2st+a_2t^2,\qquad
r_2=b_0s^2+b_1st+b_2t^2.
\]

Every primitive exceptional direction has the same scalar kernel:

\[
 \boxed{h_2=h_5=0,\qquad
 h\in\langle1,t,t^3,t^4,t^6,t^7\rangle.}
\]

The displayed span is affine notation for the corresponding homogeneous
degree-seven binary forms. It follows at once from the two-column rank-two
matrix, whether one or both of \(T,K\) are nonzero.

Equivalently, on this locus

\[
sr_1-2tr_2=-2b_0s^3+a_2t^3.
\]

In the coordinates \((a_0,a_1,a_2,b_0)\), with
\(b_1=a_0/2,b_2=a_1/2\), the primitive open subset is defined explicitly
by the nonvanishing homogeneous resultant

\[
 \boxed{\operatorname{Res}(r_1,2r_2)
 =a_0^3a_2-6a_0a_1a_2b_0+2a_1^3b_0+4a_2^2b_0^2\ne0.}
\]

### 3. Dimensions in the ambient quartic space

The preimage of each symbol intersection adds the independent parameter
\(cq^2\). Thus the quartics whose first symbol has the given direction
form linear spaces of dimension eight for \(e=0\), seven or ten for
\(e=1\), and six or seven for \(e=2\). Zero symbols are included in
these linear spaces; selecting an actual pair with primitive common
direction still requires nonzero scalar symbols, appropriate gcd
conditions, and every higher direct-limit equation.

### 4. Coprime quartic pairs exist in every remaining direction

Let \(K_r\) be the scalar kernel computed above and put

\[
 L_r=\sigma^{-1}(rK_r)\subset I_{C_0}(4).
\]

For the exceptional quadric direction \(r_q=(2s,t)\), the calculation
above gives \(L_{r_q}=qS_2\). Every pair in this space shares the
ambient factor \(q\). Hence this direction supplies no ambient-coprime
quartic pair.

For **every other primitive direction of degree at most two**, the
opposite conclusion holds at first-conormal order: there exist
ambient-coprime quartic pairs with linearly independent scalar symbols.
Thus their first-symbol ratio is nonconstant. Here is a constructive
proof.

Any \(q\)-divisible quartic has first symbol
\((p,\frac t2p)\), or zero. Consequently, a quartic with nonzero symbol
in direction \(r\ne r_q\) is not divisible by \(q\). This follows also
by taking the determinant with the quadric row: a nonzero scalar symbol
would otherwise force \(2r_2-tr_1=0\), whose only primitive homogeneous
solution is the degree-one direction \(r_q\).

The table proves \(\dim K_r\ge5\). Choose two independent nonzero
scalars \(h_1,h_2\in K_r\) and use the explicit inverse from Section 1
to lift them to \(F,G_0\in L_r\). The form \(F\) is not divisible by
\(q\). For each irreducible factor \(D\) of \(F\), there is at most one
constant \(c\in k\) for which

\[
 D\mid G_0+cq^2.
\]

Indeed, two distinct constants would imply \(D\mid q^2\), hence
\(D\sim q\), contradicting \(q\nmid F\). Avoiding the finitely many
excluded constants gives

\[
 G=G_0+cq^2,\qquad \gcd(F,G)=1,
\]

while the symbols remain \(h_1r,h_2r\). The field is infinite, so such
\(c\) exists. Their ratio cannot be constant because \(h_1,h_2\) are
independent.

The base ideal generated by \(L_r\) has no hypersurface component:
it contains both \(q^2\) and a form \(F\) not divisible by \(q\).
Equivalently its forms have gcd one. The coprime independent-symbol
pairs comprise a nonempty Zariski-open subset of \(L_r\times L_r\).
The common-factor locus is closed, since for each possible common
factor degree it is the image of the corresponding projective
factor-multiplication incidence; there are only four such degrees.
Scalar-symbol dependence is closed by the two-by-two minors of the
symbol coefficient matrix.

This establishes that coprimality and nonconstant first-symbol ratio
cannot remove any of the other degree-zero, degree-one, or degree-two
directions. It makes no claim that any of these coprime pairs passes
the higher ancestor equations.

The calculation provides a complete exact parametrization of the
first-conormal coefficient space for the \(e\le2\) frontier. It leaves
the higher normal jets as the next research obligation.


---

<a id="2026-10-05-localcoh-finite-bound"></a>

## A finite principal-part bound for quartic local-cohomology ancestors

Status: **PROVED**, conditional only on the already checked P-037 low-degree
exclusion and the literature's degree-(4,4) exclusion. This note does not
exclude every quartic ancestor; it reduces that question to a finite vector
space and bounds its primitive conormal direction.

Throughout, \(k\) is algebraically closed of characteristic zero,

\[
 S=k[x,y,z,w],\qquad
 C_0=[s^4:s^3t:st^3:t^4],\qquad
 I=I_{C_0},\qquad M=H_I^2(S),
\]

and

\[
 q=xw-yz,\quad B=xz^2-y^2w,\quad
 u=\frac{xz}{qB},\quad v=\frac{yw}{qB}.
\]

The target classes are in the first socle: \(Iu=Iv=0\). Suppose homogeneous
quartics \(F,G\) and a homogeneous \(\alpha\in M_{-7}\) satisfy

\[
 F\alpha=u,\qquad G\alpha=v.
\]

P-037 supplies \(F,G\in I\) and proportional first conormal symbols.

### 1. Coprimality and generic transverse length

The two forms are coprime. Indeed, if their greatest common divisor \(H\)
has positive degree \(r\), then \(\beta=H\alpha\) satisfies

\[
 (F/H)\beta=u,\qquad (G/H)\beta=v.
\]

These are equal-degree multipliers of degree \(4-r\le3\), contradicting
P-037. Scalar-proportional forms are excluded in the same way, or directly
by the linear independence of \(u,v\).

Consequently \(X=V_+(F,G)\) is an unmixed complete-intersection curve of
degree 16. Let \(m\) be its generic multiplicity along \(C_0\), equivalently
the length of the transverse Artinian algebra at the generic point of
\(C_0\). Its cycle contains \(m[C_0]\), so \(4m\le16\) and \(m\le4\).

If \(m=4\), the cycle degree is exhausted by \(4[C_0]\). Unmixedness leaves
no other curve component or isolated embedded point, so the support of \(X\)
is exactly \(C_0\). This would be a degree-\(4,4\) STCI presentation, contrary
to Craighero--Gattazzo, *Rend. Sem. Mat. Univ. Padova* 76 (1986), 177--200,
whose checked scope includes characteristic zero. Thus

\[
 \boxed{m\le3.}
\]

The precise literature record is in `research/LITERATURE_LEDGER.md`, under
“Craighero--Gattazzo, 1986”; the primary source is
<https://www.numdam.org/item/RSMUP_1986__76__177_0/>.

### 2. Generic annihilation extends over every curve point

Write

\[
 \mathcal E=\mathcal H^2_{C_0}(O_{\mathbf P^3}),\qquad
 \mathcal T_n=(0:_{\mathcal E}I^n).
\]

At the generic point of \(C_0\), the ideal \(I\) is the maximal ideal
of a regular local ring of dimension two. A local Artinian algebra of
length \(m\) has its maximal ideal's \(m\)-th power zero: if all successive
powers up to that point were nonzero, their strict descending chain would
already contribute more than \(m\) composition factors. Therefore

\[
 I^m\subset(F,G)
\]

at that generic point. Since \(I(F,G)\alpha=0\), we obtain

\[
 I^{m+1}\alpha=0
\]

generically along \(C_0\).

This is not merely generic information. At a closed curve point \(P\),
smoothness of the curve and ambient space gives the completed local model

\[
 R=k[[c,\xi,\eta]],\qquad I R=(\xi,\eta).
\]

Its local-cohomology module is the finite inverse-monomial module

\[
 H^2_{(\xi,\eta)}(R)
 =\bigoplus_{i,j\ge1}k[[c]]\,\xi^{-i}\eta^{-j}.
\]

In particular it has no \(k[[c]]\)-torsion. More invariantly, any element
of \(R\) whose restriction to \(C_0\) is nonzero acts injectively: in the
largest total inverse degree of a putative kernel element, multiplication
is multiplication by that nonzero restriction; normal terms lower the
inverse degree and cannot cancel it. Thus this sheaf has no nonzero
sections supported at a finite subset of \(C_0\). The generically zero
section \(I^{m+1}\alpha\) therefore vanishes at every curve point.

There is no additional element supported only at the cone vertex. The
composition spectral sequence for \(\Gamma_{\mathfrak m}\Gamma_I\), where
\(\mathfrak m=(x,y,z,w)\), gives

\[
 H^0_{\mathfrak m}(H_I^2(S))=0:
\]

the entry of total degree two has no possible incoming differential and
no outgoing differential because \(H_I^0(S)=H_I^1(S)=0\), while
\(H^2_{\mathfrak m}(S)=0\). Thus \(M\) injects into the graded sections of
its sheafification, and sheaf annihilation implies module annihilation.

Combining these facts gives

\[
 \boxed{I^4\alpha=0,\qquad
   \widetilde\alpha\in H^0(\mathbf P^3,\mathcal T_4(-7)).}
\]

The argument does not assume that the finite transverse algebras have
constant length at the special points, and does not require global ideal
containment \(I^m\subset(F,G)\). Torsion-freeness is exactly what extends
the generic annihilation of this particular local-cohomology element.

### 3. A genuinely fixed direct-limit stage

Since \(q,B\in I\), the bound implies \(q^4\alpha=B^4\alpha=0\). The sequence
\((q,B)\) is regular in \(S\), and

\[
 (0:_{H^2_{(q,B)}(S)}(q^n,B^n))
 =\left\{\frac{h}{q^nB^n}:h\in S\right\}
 \simeq S/(q^n,B^n)(5n).
\]

One proof first takes the kernel of \(q^n\) via the exact sequence for
\(S/q^nS\), obtaining \(H^1_{(B)}(S/q^nS)\), and then takes the kernel of
\(B^n\). Regularity of \(B\) modulo \(q^n\) identifies that kernel with
\(S/(q^n,B^n)\). The direct-system transition maps are injective as well,
by

\[
 (q^{n+1},B^{n+1}):qB=(q^n,B^n).
\]

Hence an ancestor must already have a representative \(h\in S_{13}\)
at stage \(n=4\), and it obeys the exact equations

\[
 \begin{aligned}
 Fh-xz(qB)^3&=q^4a+B^4b,\\
 Gh-yw(qB)^3&=q^4c+B^4d,
 \end{aligned}
\]

where \(a,c\in S_9\) and \(b,d\in S_5\). In addition
\(I^4h\subset(q^4,B^4)\) expresses membership in \((0:_M I^4)\). Solving in the full stage quotient
without this support/annihilator condition may introduce irrelevant
residual-line classes, so that condition should be retained in a finite
computation.

### 4. The primitive common conormal direction has degree at most two

Use the checked splitting \(N_{C_0/\mathbf P^3}\simeq O_{\mathbf P^1}(7)^2\).
In characteristic zero, the principal-part quotients are

\[
 \mathcal T_n/\mathcal T_{n-1}
 \simeq \operatorname{Sym}^{n-1}N\otimes\det N.
\]

After twisting by \(O_{\mathbf P^3}(-7)|_{C_0}=O_{\mathbf P^1}(-28)\), this
becomes

\[
 (\mathcal T_n/\mathcal T_{n-1})(-7)
 \simeq O_{\mathbf P^1}(7n-21)^{\oplus n}.
\]

Therefore \(H^0(\mathcal T_2(-7))=0\). A nonzero ancestor has a largest
principal-part order \(n\in\{3,4\}\).

Both first conormal symbols cannot vanish: a quartic vanishing to normal
order at least two along \(C_0\) is a scalar multiple of \(q^2\), by P-011
and \(I_2=kq\); two such forms cannot give the independent targets. Write
the nonzero common conormal direction as a basepoint-free pair

\[
 r=(r_1,r_2),\qquad r_i\in H^0(O_{\mathbf P^1}(e)),
\]

of coprime homogeneous binary forms. The quartic symbols are
\((a r,b r)\), with \((a,b)\) sections of \(O(9-e)\), because
\(N^*(4)=O(9)^2\). This definition includes a zero first symbol for one
of the two forms.

Multiplication by a linear normal symbol acts on the highest principal-part
symbol by contraction. Since \(F\alpha,G\alpha\in\mathcal T_1\), the
highest symbol of \(\alpha\) is killed by contraction with \(r\). For
binary symmetric powers in characteristic zero that kernel is the line
generated by

\[
 (-r_2,r_1)^{n-1}.
\]

Thus the highest symbol equals this vector times a nonzero section of

\[
 O_{\mathbf P^1}\bigl(7n-21-(n-1)e\bigr).
\]

Its degree must be nonnegative. For \(n=3\) this forces \(e=0\); for
\(n=4\) it forces \(e\le2\). Consequently

\[
 \boxed{e\le2.}
\]

This is a bound on the degree of the primitive common direction in the
balanced normal-bundle frame. It is not the degree of the quotient
(\sigma(G)/\sigma(F)), and should not be confused with an affine
coordinate polynomial degree before converting to that frame.

### 5. General form of the bound and remaining obstacle

For coprime equal-degree multipliers of degree \(d\) containing a smooth
degree-\(\delta\) curve, the same proof gives

\[
 m\le\left\lfloor\frac{d^2}{\delta}\right\rfloor,
 \qquad I^{m+1}\alpha=0
\]

whenever the targets are in the first socle. Thus each fixed multiplier
degree has a finite principal-part search, although that search grows with
\(d\). If the curve is \(C_0\), the ancestor has degree \(-(d+3)\), and the
highest quotient has degree \(7n-4d-5\) in the balanced normal frame.

For quartics the remaining problem is a finite, genuinely nonlinear
incidence problem: find \(\alpha\in(0:_M I^4)_{-7}\) for which the
quartic multiplication image contains both \(u,v\). The direction bound
\(e\le2\) is necessary, not an existence theorem or an exclusion. Exact
dimensions, annihilator generators, and the formal-neighborhood extension
of the candidate highest symbols require a separate verified computation.


---

<a id="2026-10-05-localcoh-generic-length"></a>

## A quartic ancestor forces a curvilinear triple and a degree-four residual cycle

Date: 2026-10-05. Status: **PROVED**, conditional on the antecedent results
identified below. This note concerns the characteristic-zero monomial rational
quartic only; it does not exclude every quartic local-cohomology ancestor.

Let

\[
C_0=[s^4:s^3t:st^3:t^4],\quad I=I_{C_0},\quad
u=\frac{xz}{qB},\quad v=\frac{yw}{qB},\quad
q=xw-yz,\quad B=xz^2-y^2w.
\]

Suppose quartics \(F,G\) and \(\alpha\in H_I^2(S)_{-7}\) satisfy
\(F\alpha=u\), \(G\alpha=v\). P-037 supplies coprimality of the pair
and membership \(F,G\in I\). The note
`2026-10-05-localcoh-finite-bound.md` bounds its generic intersection
multiplicity by \(m\le3\), using the recorded characteristic-zero
degree-(4,4) exclusion. The note `2026-10-05-localcoh-degree4.md` excludes
principal-part order at most three, using P-010; therefore the ancestor has
order exactly four.

### Generic length is exactly three, rather than merely at most three

At the generic point of the curve, complete the transverse regular local
ring to \(R=K[[\xi,\eta]]\), where \(K=k(C_0)\), and write
\(E=H^2_{(\xi,\eta)}(R)\). Set

\[
J=(F,G)R,\qquad A=R/\operatorname{Ann}_R(\alpha),\qquad
\ell=\operatorname{length}_R A.
\]

The cyclic module \(R\alpha\) is isomorphic to \(A\), and its socle is
one-dimensional: it is a nonzero subspace of the one-dimensional socle
\(Ke\) of the transverse injective hull \(E\). Equivalently, \(A\) is
an Artinian Gorenstein algebra.

Since \(I^3\alpha\ne0\) and \(I^4\alpha=0\), its maximal-ideal chain
has at least four nonzero successive quotients, so \(\ell\ge4\).
Both targets are nonzero multiples of \(e\) over \(K\), hence the image
of \(J\) in \(A\) is its socle and has length one. The quotient map gives

\[
R/J\twoheadrightarrow A/JA,\qquad
m\ge\ell-1\ge3.
\]

The upper bound \(m\le3\) now forces

\[
\boxed{m=3,\qquad \ell=4,\qquad
\operatorname{Ann}_R(\alpha)\subset J.}
\]

The four nonzero terms in the maximal-ideal filtration already exhaust the
length of \(A\); its Hilbert function is \((1,1,1,1)\). Consequently
\(A\simeq K[[\tau]]/(\tau^4)\), and its socle quotient is
\(R/J\simeq K[[\tau]]/(\tau^3)\). Thus a surviving quartic pair must
define a **curvilinear triple at the generic transverse point**; its
ancestor defines the corresponding curvilinear quadruple there.

The complete intersection has degree sixteen, and \(3[C_0]\) contributes
degree twelve to its fundamental cycle. The remaining effective cycle has
degree exactly four. This is a cycle statement; it does not assert that the
residual curve is integral, reduced, smooth, or disjoint from \(C_0\).

### A further exclusion inside the constant-direction stratum

Write the proportional quartic first symbols in the balanced normal frame as
\(ar,br\), where \(r\) is a primitive basepoint-free direction of degree
\(e\), and \(a,b\in H^0(O_{\mathbf P^1}(9-e))\).

If \(a,b\) have no common projective zero, at every curve point one equation
has a nonzero linear normal term. It supplies a smooth local surface through
the curve. In that surface the second equation is locally
\(\eta^3 h(c,\eta)\), since the generic multiplicity is three. Removing
the residual factor \(h\) gives the local \(C_0\)-primary component
\((\xi,\eta^3)\). These components glue to an embedded primitive triple
with conormal quotient

\[
N_{C_0/\mathbf P^3}^*\twoheadrightarrow O_{\mathbf P^1}(e-7).
\]

For \(e=0\), this is the primitive triple of type \(O(-7)\) excluded
by P-010. Hence

\[
\boxed{e=0\quad\Longrightarrow\quad \gcd(a,b)\text{ has positive degree}}
\]

for any surviving ancestor. This excludes the open subset of the
constant-direction stratum on which the scalar factors form a basepoint-free
pencil. It leaves its scalar-basepoint boundary and every possible \(e=1,2\)
stratum unresolved.

### Failed shortcut: a top-symbol zero does not force target vanishing

It is tempting to argue that the length-four cyclic inverse system must be
Gorenstein in every transverse fiber, and therefore that its pure-cubic top
coefficient is nowhere zero. This implication is false. Over
\(D=k[[c]]\), in the finite inverse-monomial module
\(H^2_{(\xi,\eta)}(D[[\xi,\eta]])\), take

\[
\alpha=c\,\xi^{-1}\eta^{-4}+\xi^{-2}\eta^{-1},\qquad
e=\xi^{-1}\eta^{-1}.
\]

Then

\[
\xi\alpha=e,\qquad \eta^3\alpha=ce.
\]

The ideal \((\xi,\eta^3)\) has transverse length three. The cyclic module
\(D[[\xi,\eta]]\alpha\) is free of rank four over \(D\), with basis
\(\alpha,\eta\alpha,\eta^2\alpha,e\), and actions

\[
\eta:(\alpha,\eta\alpha,\eta^2\alpha,e)
\longmapsto(\eta\alpha,\eta^2\alpha,ce,0),\qquad
\xi:(\alpha,\eta\alpha,\eta^2\alpha,e)
\longmapsto(e,0,0,0).
\]

At \(c=0\), this abstract cyclic algebra has a two-dimensional socle,
spanned by the classes of \(\eta^2\alpha\) and \(e\); its injection into
the inverse-monomial module does not remain injective after passage to the
fiber. The top coefficient vanishes while \(e\) remains generated. The
exact companion `verify_localcoh_generic_length_model.py` checks these
actions, generic and special socle dimensions, and the annihilator description

\[
\operatorname{Ann}(\alpha)
=(\xi^2,\xi\eta,\eta^3-c\xi).
\]

Thus finite-flat cyclicity along the curve does not supply relative
Gorenstein fibers. Any global argument excluding top-coefficient zeros must
use extra ambient or multiplier information.

### Continuation boundary

Combine the new multiplicity-three condition with the exact pure-cubic
top-symbol lifting equations and the full multiplication tensor. The next
required information is the lower principal-part equation, which controls
whether the quartic scalar pencil can map this curvilinear quadruple to both
fixed socle targets. A primitive quadruple in the ambient space, or a pure
cubic that lifts to the 30-dimensional ancestor space, does not by itself
produce those two multiplier equations.


---

<a id="2026-10-05-localcoh-pure-direction-audit"></a>

## Independent audit of pure constant quartic directions

Date: 2026-10-05. Status: **PASS**. Scope is the characteristic-zero
monomial rational quartic \(C_0=[s^4:s^3t:st^3:t^4]\), quartic multiplier
pairs, and the two pure constant directions in the balanced frame

\[
U=w-t^4-\frac32t(z-t^3),\qquad V=z-t^3.
\]

This proves an exclusion for quartic common local-cohomology ancestors
using the established order-three primitive-triple obstruction. It does
not settle the mixed constant directions or degree-one/two directions.
The exact independent companion is
`research/computations/verify_localcoh_pure_direction_audit.py`.

### 1. Exact pure-direction space and transverse coefficients

Retain

\[
q=xw-yz,\quad A=x^2z-y^3,\quad
B=xz^2-y^2w,\quad C=yw^2-z^3.
\]

The quartic symbol-image classification gives every pure-\(V\) form
uniquely as

\[
\begin{aligned}
 F={}&c_0xA+c_1yA+c_3zA+c_4wA\\
 &+c_6(zB+qyw)+c_7(wB+qz^2)
  +c_9(-zC+2qw^2)+\kappa q^2.
\end{aligned}
\]

Its first symbol is \(h_FV\), where

\[
h_F=c_0+c_1t+c_3t^3+c_4t^4+c_6t^6+c_7t^7+c_9t^9.
\]

Substituting \(x=1,y=t,z=t^3,w=t^4+U\), equivalently setting \(V=0\),
gives the exact identity

\[
 F|_{V=0}=R_FU^2+2c_9U^3,
 \qquad R_F=\kappa+c_6t-c_7t^2+3c_9t^4.
\]

In particular, \(R_F=0\) if and only if
\(\kappa=c_6=c_7=c_9=0\), and then \(F\in AS_1\). A zero first symbol
means \(F=\kappa q^2\); this boundary is included.

### 2. The contact identity has no missing coefficient strata

For two such forms, define

\[
\Delta=h_FR_G-h_GR_F.
\]

The following exhaustive algebraic statement holds:

\[
\boxed{\Delta=0\quad\Longrightarrow\quad
\text{either }F,G\text{ are scalar-proportional, or }F,G\in AS_1.}
\]

To prove it, if some \(R\) is nonzero choose the highest active coefficient
among \(c_9,c_7,c_6,\kappa\) across both forms, interchange the forms if
necessary so that it occurs in \(F\), and subtract a scalar multiple of
\(F\) from \(G\) to kill that coefficient in \(G\). This operation preserves
the contact identity. The four possible cases are:

* If \(c_9\ne0\), now \(c'_9=0\). The coefficients of \(\Delta\) in
  degrees eleven, ten, and nine successively give
  \(-4c_9c'_7=0\), \(-2c_9c'_6=0\), and \(c_9\kappa'=0\).
* If both degree-nine coefficients vanish and \(c_7\ne0\), now
  \(c'_7=0\). Degrees eight and seven successively give
  \(2c_7c'_6=0\) and \(c_7\kappa'=0\).
* If all degree-nine and degree-seven coefficients vanish and
  \(c_6\ne0\), now \(c'_6=0\). Degree six gives
  \(c_6\kappa'=0\).
* In the last case both forms have \(c_9=c_7=c_6=0\), and
  \(\kappa\ne0\). Killing \(\kappa'\) already gives \(R_G=0\).

In each case all four coefficients of \(R_G\) vanish. Since \(R_F\ne0\),
the identity then forces \(h_G=0\). Together with \(\kappa'=0\), all eight
coefficients of the adjusted \(G\) vanish, so the original \(G\) was
proportional to \(F\). This includes \(h_F=0\), since the final argument
does not divide by \(h_F\). If both \(R\)'s initially vanish, both forms
lie in \(AS_1\), as claimed.

Therefore an ambient-coprime pair has \(\Delta\ne0\). The two forms
cannot both have zero first symbol, since the first-symbol kernel is
\(kq^2\).

### 3. Generic transverse length and the ancestor implication

Let \(K=k(C_0)\). For an ambient-coprime pair the generic transverse
algebra is the finite-colength complete intersection in \(K[[U,V]]\).
At least one of \(h_F,h_G\) is nonzero; interchange the forms so that
\(h_F\ne0\). The formal implicit-function theorem eliminates \(V\):

\[
 V=-\frac{R_F}{h_F}U^2+O(U^3).
\]

Modulo \(F\), the coefficient of \(U^2\) in \(G\) is

\[
 R_G-\frac{h_G}{h_F}R_F=\frac\Delta{h_F}.
\]

Thus generic transverse length at least three is equivalent to
\(\Delta=0\), under the finite-colength hypothesis. Since a coprime pair
has \(\Delta\ne0\), its generic transverse length is exactly two. This
also covers a zero first symbol for \(G\): then
\(G=\kappa' q^2\) with \(\kappa'\ne0\), and the same coefficient is
\(\kappa'\).

Suppose now quartics obey \(F\alpha=u,G\alpha=v\), where the independent
targets lie in the first socle and \(\alpha\) has degree \(-7\). P-037
forces \(F,G\) to be coprime: a common factor would produce multipliers
of degree at most three. Generic transverse length two gives
\(I^2\subset(F,G)\) at the generic curve point. Since
\(I(F,G)\alpha=0\), it follows that \(I^3\alpha=0\) generically.

The torsion-free local inverse-monomial module propagates this
annihilation over every closed curve point. The established
\(H^0_{\mathfrak m}(H_I^2(S))=0\) then removes the possible cone-vertex
ambiguity. These are precisely the propagation arguments in
`2026-10-05-localcoh-finite-bound.md`, with \(m=2\). Hence globally

\[
\boxed{I^3\alpha=0.}
\]

The balanced normal bundle gives

\[
(\mathcal T_n/\mathcal T_{n-1})(-7)
\simeq O(7n-21)^{\oplus n},
\qquad H^0(\mathcal T_2(-7))=0.
\]

Thus a nonzero ancestor would have order exactly three, with a nonzero
constant quadratic top symbol. Multiplication by the nonzero pure first
symbol \(hV\), while the result belongs to the first socle, forces that
quadratic to be the perpendicular pure square. It is nowhere zero because
its coefficients are global constants.

As proved in the order-three argument of
`2026-10-05-localcoh-degree4.md`, this cyclic inverse system defines a
primitive triple of conormal type \(O(-7)\). Locally one may normalize it
to

\[
 \alpha=\xi^{-1}\eta^{-3}
       +c\xi^{-2}\eta^{-1}
       +d\xi^{-1}\eta^{-2}
       +e\xi^{-1}\eta^{-1},
\]

whose annihilator is \((\xi-c\eta^2,\eta^3)\). Its cyclic module has
the free basis \(\alpha,\eta\alpha,\eta^2\alpha\), so it is a primitive
triple in every transverse fiber. The annihilator ideals glue under the
unit changes in local trivialization of the twisted ancestor. P-010
excludes such a primitive triple in characteristic zero. Therefore no
pure-\(V\) quartic pair supplies a common ancestor.

### 4. The pure-\(U\) direction is included by an exact symmetry

The ambient coordinate reversal
\(\tau(x,y,z,w)=(w,z,y,x)\) preserves \(C_0\), sends the curve parameter
to its inverse, fixes \(q\), and sends \(B\) to \(-B\). In the fixed
balanced frame its quartic symbol action is exactly

\[
 \boxed{\sigma(\tau F)
 =(2t^9Q(1/t),\tfrac12t^9P(1/t)).}
\]

The independent script verifies this on an 18-element basis of
\(I_{C_0}(4)\). Consequently reversal exchanges the two pure constant
directions, preserving ambient coprimality and generic transverse length.
It also exchanges the specific local-cohomology targets by
\(\tau u=-v,\tau v=-u\). The pure-\(U\) exclusion follows with no
additional hypothesis.

The audited conclusion is an all-stage exclusion of both pure constant
directions for quartic ancestors. Its contact argument alone is about
generic multiplicity two; the essential final input is the established
order-three primitive-triple obstruction.


---

<a id="2026-10-06-localcoh-constant-direction-apolar"></a>

## Constant directions require a prescribed common scalar divisor

Date: 2026-10-06. Status: **PROVED**, conditional on the characteristic-zero
P-010 quadratic transition class and the generic length-three reduction in
`2026-10-05-localcoh-generic-length.md`. This is a necessary second-contact
condition on quartic ancestor pairs, not a complete exclusion.

Use the balanced conormal frame \((U,V)\) of the monomial quartic and a
constant primitive first-symbol direction \(m=U+\theta V\), with
\(\ell=V\). Write the quartic symbols as \(a m,b m\), where
\(a,b\in H^0(O(9))\), and let \(D\) be their common-zero divisor.

Generic transverse multiplicity three forces their pure \(\ell^2\)
second coefficients \(f_2,g_2\) to obey \(b f_2-a g_2=0\). Hence
\(\beta=f_2/a=g_2/b\) is a rational quadratic correction to the common
surface equation. Its poles are bounded by \(D\): at any curve point the
two expressions bound the pole order by the minimum of the vanishing orders
of \(a,b\). Since the first coefficients have degree nine and second
coefficients have degree two, \(\beta\) is a meromorphic local section
of \(O(-7)\).

On chart overlaps these corrections differ by the P-010 class

\[
h_\theta=3\left(\theta^3t^{-5}-\frac12\theta^2t^{-4}
 +\frac14\theta t^{-3}-\frac18t^{-2}\right)
 \in H^1(O(-7)).
\]

Consequently this class must vanish after allowing the poles:

\[
\boxed{D\cdot h_\theta=0\quad\text{in }H^1(O(\deg D-7)).}
\]

Here multiplication by \(D\) means multiplication by a homogeneous binary
form defining that divisor. In the affine notation \(D(t)=\sum d_i t^i\),
the equation says that the coefficients of \(t^{-1},\ldots,
t^{-(6-\deg D)}\) in \(D(t)h_\theta\) vanish. This gives exact linear
conditions on its coefficients, rather than just a positive-degree bound.

For finite mixed directions \(\theta\ne0\), the multiplication maps
for divisors of degrees one and two have full column rank. A nonzero
degree-three divisor exists, and its kernel is exactly

\[
(d_0,d_1,d_2,d_3)\sim(0,2\theta,1,0).
\]

Therefore

\[
\boxed{\theta\ne0:\quad \deg D\ge3;\qquad
\deg D=3\Rightarrow D\sim st(t+2\theta s).}
\]

The boundary direction \(\theta=0\) first permits a degree-two divisor
\(D\sim t^2\). The missing direction \(m=V,\ell=U\), whose class is
\(3t^{-5}\), first permits \(D\sim s^2\). Both pure directions are
already excluded by the stronger contact theorem in
`2026-10-05-localcoh-pure-direction-audit.md`.

The retired historical checker `verify_localcoh_constant_direction_apolar.py` checked
the ranks using nonzero minors and the exceptional axis kernels. In
particular its degree-two mixed minor is \(-\theta^4/32\), so the proof
does not confuse generic rank with an assertion at \(\theta=0\).
It also checks that the degree-four scalar divisor of the explicit mixed
contact pair in `verify_localcoh_direction_contact_survivor.py` kills
\(h_{1/2}\). That example shows that this pole-bound condition can be
satisfied by ambient-coprime contact pairs.

The remaining obligation is target-specific: even after this formal
second-contact condition, the highest coefficient forced by
\(F\alpha=u,G\alpha=v\) must be a regular global section of \(O(7)\),
and every lower principal part must agree. The explicit mixed pair fails
that regularity condition, but no exclusion of all mixed constant directions
is claimed here.

A separate explicit rank-one quartic control, historically checked over
\(\mathbf Q(\lambda)\), is
\[
q=xw-yz,\quad A=x^2z-y^3,\qquad
F=xA+\lambda y^2q,\quad G=yA+\lambda xzq.
\]
Both vanish on the marked quartic, and for \(\lambda\ne0\) their
first-normal rows on the \(x=1\) chart, using \(A=a,q=b\), are
\((1,\lambda t^2)\) and \((t,\lambda t^3)\).
The identities \(xzF-y^2G=A^2\) and
\(-yF+xG=\lambda Aq\) provide a direct coprimality control.
This is a **nonconstant proportional first-symbol ratio** example, not
a common local-cohomology ancestor or an STCI construction. Its historical
symbolic checker was retired.



## Consolidated historical supplement: `research/supplements/OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md`

The following mathematical arguments, qualifications, and audit boundaries are retained verbatim from the historical supplement. Internal relative links refer to the source's original location.

# Simultaneous socle targets and exact endpoint dual certificates

The primitive e=1 simultaneous-target argument below uses both nonzero socle targets. The failed single-target bridge is retained for its exact failure mechanism and is not theorem authority. Complete endpoint-family normalization and all exceptional-field closures are owned by [the full local-cohomology certificate proof](LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md).

---

<a id="e1-simultaneous"></a>

## Simultaneous-target repair for primitive e=1 quartic ancestors

Date: 2026-10-07. Fixed `C0` over an algebraically closed field of
characteristic zero. Status: **PROVED UNDER THE EXPLICIT ACCEPTED INPUTS;
root and independent adversarial audits accepted on 2026-10-07.** Under the already accepted socle
theorem, P-037 and complete primitive-e=1 quartic fibres, this excludes
common quartic ancestors with `e=1,D2=0`. The defective-triple stratum
`e=1,D2>0` remains open.

The original single-multiplier argument is preserved separately as
[`2026-10-07-session-localcoh-mf6-bridge.md`](OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md#mf6-bridge),
explicitly labeled **FAILED**. Its error was treating `F*alpha=u` as
`F=0` in the quadruple rather than a nonzero socle target. This repair
keeps both target equations and their independence throughout.

### 1. Primitive triple, complete fibres and rank-two targets

The accepted quartic-ancestor reduction gives a saturated finite-flat CM
quadruple `Z` whose generic transverse algebra is curvilinear of length
four, with

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

Its saturated socle `E3` is an ideal, and `OZ/E3` is torsion-free over
the reduced curve. Since the images of `F,G` in `OZ` are generically
socle elements, both vanish in `OZ/E3` everywhere. They contain the
embedded canonical triple `Z3=Spec(OZ/E3)`.

If `D2=0`, a local generator `ell` of the first quotient has square
generating the second quotient. The triple then has local basis
`1,ell,ell^2` and is primitive, whether or not the quadruple has a
defective last piece. For `e=1` it has `L=O(-6)` and belongs to the four
complete actual torus orbits in
[`2026-10-07-session-mf6-e1-independent-audit.md`](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-independent-auditmd).
This proof uses its complete quartic fibres, rather than its individual
carrier cubic-pole bounds or its STCI mate-support argument.

Three of these fibres are two-dimensional pencils. The original
multipliers `F,G` are linearly independent because their images are the
independent classes `u,v`. Thus they form a basis of the full pencil.
For any chosen fixed basis `F0,F1`, its target images `f0,f1` must be
an invertible constant change of `u,v`, and remain a rank-two,
basepoint-free target pencil.

### 2. The global socle and normal frames

The accepted socle-pencil theorem gives the **untwisted** isomorphism

```text
alpha: E3 -> omegaC(-3)=O_P1(-14).
```

After twisting by an ambient quartic it gives

```text
alpha: E3(4) -> omegaC(1)=O_P1(2).
```

Choose the finite socle frame `w` using this isomorphism. In the first
support chart `x0=1,x1=z`, the balanced normal parameters are exactly
the ones used by MF6:

```text
V=x2-z^3, U=q-z*V/2, q=x3-z*x2.
```

The first-normal determinant of `(q,B)` relative to `(U,V)` is `z^3`.
The raw target numerators restrict to `xz=z^3` and `yw=z^5`, so their
socle coefficients are `1,z^2` after cancellation. The accepted socle
theorem verifies that this cancellation extends at the endpoints.
Therefore, in this finite frame,

```text
f0,f1 in span_k(1,z^2),
```

and together they must be a rank-two, basepoint-free basis of that
pencil. The raw numerators are not substituted for these normalized
sections.

For the principal primitive direction, use
`ell=(4/3)U+(1/6)V`; its constant Bezout relation against
`A=1+z,B=-2-8z` is one. For the algebraic directions
`A=r*z,B=1`, use `ell=V`. Hence both represent the actual finite frame
of `L=O(-6)`. On the overlap its first class transforms as
`ell_infinity=z^-6*ell`; normal terms of order at least two do not
affect its cube in a length-four algebra. The moving support-coordinate
correction also contributes only normal order at least four after
multiplication by `ell^3`. Thus

```text
ell_infinity^3=z^-18*ell^3,
w_infinity=z^-14*w,
tau_infinity=z^-4*tau,
```

where `ell^3=tau*w`. Consequently
`tau in H0(Hom(L^3,E3))=H0(O(4))` is a polynomial of degree at most
four on the finite chart.

The corrected primitive-triple normal parameter `m+gamma*ell^2` has a
regular socle coefficient `a` in `OZ`. With the accepted MF6 convention
`T=gamma*E-K`, every quartic in its complete fibre has exactly

```text
f_i=h_i*a-T_i*tau.
```

The relevant twists are `h in H0(O(8))`, `f in H0(O(2))`, and
`tau in H0(O(4))`. The corrected normal coefficient `a` and the cubic
coefficient `T` have inhomogeneous transition, so neither is assigned
an unsupported polynomial-degree bound. If the corrected normal frame
changes as `m_corr,infinity=z^-8*m_corr+rho*ell^3`, putting
`sigma=z^14*rho` gives

```text
a_infinity=z^6*a+sigma*tau,
h_infinity=z^-8*h,
T_infinity=z^2*T+z^-4*h*sigma,
f_infinity=z^-2*f.
```

These identities make the nonzero target equation glue correctly.
They do not replace it by an annihilation equation.

### 3. Principal orbit: simultaneous compatibility contradicts basepoint freedom

Put `P=4z^2+2z+1`. The complete principal pencil has

```text
h0=P*z^3/16,
h1=P*(64z^6+8z^3+1)/1024,
T0=(2z+1)*(1536z^5+1152z^4+448z^3+48z^2-24z+4),
T1=(2z+1)*(1536z^8+1152z^7+448z^6+240z^5+120z^4
           +60z^3+30z^2+15z+8).
```

Eliminating `a` from the two correct equations gives

```text
h1*f0-h0*f1=(h0*T1-h1*T0)*tau,
h0*T1-h1*T0=(2z-1)^3*(2z+1)*P/256.
```

Cancel the nonzero polynomial `P` to obtain

```text
(64z^6+8z^3+1)*f0-64z^3*f1
       =4*(2z-1)^3*(2z+1)*tau.
```

At `z=1/2` this requires `3f0(1/2)-8f1(1/2)=0`; at `z=-1/2`
it requires `f0(-1/2)+8f1(-1/2)=0`. Each `f_i` lies in
`span(1,z^2)`, so its values at these two points are equal. The two
independent relations force both targets to vanish there. This
contradicts their basepoint freedom. The principal contradiction needs
no degree bound on `tau`.

For a stronger exact coefficient check, the full remainder matrix
modulo `(2z-1)^3*(2z+1)` has rank three and kernel

```text
(f0,f1)=c*(z^2-1/4, (3/8)*(z^2-1/4)).
```

Thus it even forces the target pencil to rank at most one. Both
checks use the nonzero target terms, unlike the failed shortcut.

### 4. The two algebraic orbits: polynomial-degree contradiction

For `A=r*z,B=1,12r^2+4r+3=0`, the complete pencil has `gamma=0`
and

```text
h0=1, T0=0,
h1=(2r+2/3)*z^8, T1=(8r/9)*z^3.
```

Both scalar coefficients are units modulo the defining quadratic.
The target equations become

```text
a=f0,
f1=(2r+2/3)*z^8*f0-(8r/9)*z^3*tau.
```

The first right-hand term has degree at least eight for any nonzero
`f0`; the second has degree at most seven because `deg tau<=4`; and
`deg f1<=2`. Hence `f0=0`. The remaining right-hand term is divisible
by `z^3`, so `f1=0` as well. This contradicts target independence.
The exact quadratic-field unit checks treat both roots without generic
field-specialization inference.

### 5. The fourth orbit and exact evidence

For `A=-z/2,B=1`, the complete fibre is
`q*H0(P3,O(2))`. Hence `F=q*F2,G=q*G2`, and

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This is a degree-two common ancestor, forbidden by the all-stage P-037
theorem. It is the ancestor-specific quadric-factor argument, with no
STCI mate assumption.

The independent exact coefficient verifier is
[`verify_session_localcoh_e1_simultaneous_2026_10_07.py`](../computations/verify_session_localcoh_e1_simultaneous_2026_10_07.py).
It reconstructs the determinant and target remainder matrix from the
displayed accepted pencil coefficients, checks both simple evaluations
and the complete rank-three constraint, and verifies the scalar units
and all forcing degree coefficients over the exact algebraic field.
Its JSON states the required geometric inputs explicitly. Script
agreement is not a substitute for the frame argument in Section 2.

The root independently verified both simultaneous contradictions. The
separate frame audit
[`2026-10-07-session-socle-bridge-adversarial-audit.md`](OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-socle-bridge-adversarial-auditmd)
accepted the global socle frame, normalized targets, quotient-frame
transitions, tau degree bound and complete quadric orbit. The corrected
`e=1,D2=0` ancestor exclusion is therefore accepted. The failed earlier
proof remains clearly labeled as such.


---

<a id="mf6-bridge"></a>

## FAILED bridge: a nonzero socle target was incorrectly treated as annihilation

Date: 2026-10-07. Fixed `C0` in characteristic zero. Status:
**FAILED; ORIGINAL PROOF RETRACTED.** The original text is retained below
as a failure record and must not be used as a proved exclusion.

The root audit caught the exact flaw: `F*alpha=u` makes the image of F
in OZ a **nonzero socle element**, rather than zero. It vanishes only
in the canonical triple OZ/E3. Section 3 below therefore incorrectly
uses `h*a=T*c^d3*unit`. The actual equation is
`h*a-T*c^d3*unit=f_u`, with a regular nonzero target coefficient.
Dividing by h can introduce extra target poles, so the claimed
single-multiplier cubic polar bound does not follow. The same applies
to G. The canonical-triple containment and the quadric-factor P-037
argument remain valid; the claimed four-orbit conclusion does not follow
from this failed proof. A separate simultaneous-two-target repair is
now saved and independently accepted as
[`2026-10-07-session-localcoh-e1-simultaneous.md`](#e1-simultaneous).
The failed text does not establish the exclusion
retained here; use that corrected two-target proof instead.

---

### Historical retracted argument

### 1. Precise corollary

Suppose quartics `F,G` and a local-cohomology ancestor `alpha` satisfy
`F*alpha=u,G*alpha=v`. Its saturated annihilator defines the finite-flat
CM quadruple `Z` from the audited generic-length reduction. Write

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

The socle-pencil theorem in
[`2026-10-06-session-localcoh-progress.md`](LOCAL_COHOMOLOGY_CONORMAL_GEOMETRY.md#2026-10-06-session-localcoh-progress),
Section 2, forces `degD3=7-3e`. Therefore:

> There is no common quartic ancestor with `e=1,D2=0`.

The accepted MF6 orbit calculations used here are Sections 2--5 of
[`2026-10-07-session-mf6-e1-independent-audit.md`](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-independent-auditmd).
Only their complete primitive-triple classification and cubic polar
degree bounds are needed. The further mate-support argument for the
pure quartic carriers is not used in the ancestor setting.

### 2. Why the two multipliers contain the canonical triple

The saturated socle `E3` is an ideal in `OZ`, and `OZ/E3` is torsion-free
over the smooth reduced support. Generically the images of `F,G` in
`OZ` are socle elements. Their images in `OZ/E3` therefore vanish
generically and, by torsion-freeness, vanish everywhere. Thus both
quartics contain the embedded canonical triple

```text
Z3=Spec(OZ/E3).
```

When `D2=0`, the multiplication `L^2 -> E2` is everywhere a unit. In a
completed support DVR, choose a normal parameter `ell` whose first
class generates `L`. Its square generates `E2`. The canonical triple
is locally generated by that one normal parameter, with basis
`1,ell,ell^2`. Consequently it is an embedded primitive triple. This
does not require the quadruple's special fibres to be curvilinear:
the possible extra degeneration lies in its last piece `E3` and has
been quotiented out.

For `e=1`, this is exactly a global primitive triple with
`L=O(-6)`. It therefore belongs to one of the four actual torus orbits
of the independent MF6 classification.

### 3. The cubic pole bound remains valid for a defective quadruple

Fix a completed support DVR `R=k[[c]]`. In a primitive-triple chart take
ambient normal parameters `m,ell` and the regular quadratic correction
`gamma` so that

```text
m+gamma*ell^2=0 in OZ3.
```

Let `w` generate the locally free socle line `E3`. Since this relation
holds in the canonical triple, it has the form
`m+gamma*ell^2=a(c)*w` in `OZ`, with `a(c)` regular. The ordinary cubic
product has the form

```text
ell^3=c^d3*unit*w,
```

where `d3` is the local multiplicity of `D3`. This is precisely the
definition of the saturated multiplication map `L^3 -> E3`.

For a quartic containing `Z3`, let `h` be its first-normal coefficient
and `T` the cubic coefficient after the regular quadratic correction.
If `h` is not identically zero, its vanishing in `OZ` gives, up to the
chosen harmless sign convention,

```text
h*a(c)=T*c^d3*unit.
```

Thus `T/h` has pole order at most `d3`. Summing the exact local pole
orders over the curve gives

```text
deg(cubic pole divisor of that quartic) <= degD3.
```

Only containment in the quadruple and regularity of its socle lattice
are used. No relative Gorenstein-fibre assumption and no mate support
condition enter this inequality.

### 4. The four complete quartic fibres give the contradiction

For the principal orbit `A=1+z,B=-2-8z`, every nonzero quartic in its
complete two-dimensional fibre has a nonzero first-normal symbol, and
its cubic polar degree is at least six. For each of the two conjugate
orbits `A=r*z,B=1,12r^2+4r+3=0`, every nonzero quartic likewise has a
nonzero first symbol and cubic polar degree at least five, including
the directly expanded infinity member. But the ancestor socle theorem
gives `degD3=4` when `e=1`. Section 3 contradicts each of these three
orbits, for either multiplier separately.

In the fourth orbit, `A=-z/2,B=1`, the complete quartic fibre is
`q*H0(P3,O(2))`. This fibre includes members with zero first-normal
symbol, so the polar argument cannot be substituted here. Both
multipliers instead have the form `F=q*F2,G=q*G2`. Their equations give

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This is a common ancestor with degree-two multipliers, prohibited by
the all-stage theorem P-037. The equation `u!=0` also ensures
`q*alpha!=0`. The obstruction is valid for the ancestor equations;
the separate STCI unique-quadric-factor argument is unnecessary.

All four primitive `e=1` directions are therefore excluded in the
common quartic-ancestor problem. The `e=1,D2>0` stratum remains open:
its canonical triple is defective and does not belong to the primitive
classification used in this proof.


---



## Consolidated historical supplement: `research/supplements/OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md`

The following mathematical arguments, qualifications, and audit boundaries are retained verbatim from the historical supplement. Internal relative links refer to the source's original location.

# Quartic ancestor incidence and conductor descent

The quartic-ancestor incidence and conductor arguments below retain their stated hypotheses. Endpoint-family closure is complete in [the exact local-cohomology proof](LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md), including the degree-fifteen field.

---

<a id="source-2026-10-08-session-irreducible-conductor-compressionmd"></a>

## Smooth normalized quartic scrolls: conductor descent and mate compression

Date: 2026-10-08. Status: **PROVED conditional structural exclusion**,
independently audited from the proposed conductor argument. The result
uses the actual entire conductor scheme, a smooth twisted-cubic
downstairs conductor, and a finite flat cover of rank two. It is not a
classification of all nonnormal quartic carriers. No frontier
file is edited here, and no novelty claim is made.

The initial assigned target was an integral reduced upstairs conductor.
Sections 1--5 prove that target, including nodal conductors. Section 6
audits the reduced reducible extension. Section 7 records a separately
audited rank-two nonreduced extension, whose restrictive hypotheses
must remain attached to it.

### 1. Exact statement and support hypotheses

Work over an algebraically closed field of characteristic zero. Let
X be an integral quartic hypersurface in P3. Let nu:S->X be its finite
normalization, with S a smooth rational quartic scroll and
H=nu*O_X(1). In particular,

    H^2=4, K_S.H=-6, and Pic(S) has no torsion.

Let I be the actual conductor ideal, let Gamma=V(I) on X, and let
D=V(I O_S) on S. Assume:

1. Gamma, with this exact scheme structure, is a smooth twisted cubic;
2. p=nu|D:D->Gamma is finite flat of rank two;
3. initially, D is integral and reduced.

Then X cannot occur in a set-theoretic complete-intersection
presentation of

    C0=[s^4:s^3t:st^3:t^4] in P3,

with a mate of any positive degree. The same conclusion holds if D is
reduced reducible (section 6), or nonreduced under these unchanged
rank-two finite-flat hypotheses (section 7).

The exact conductor is necessary: replacing it by its reduced support
can discard compatibility conditions required for descent. The
smoothness and rank assumptions on Gamma and p are also substantive.

The normalization is an isomorphism off Gamma. Since C0 has degree
four and Gamma has degree three, C0 is not contained in Gamma, so X is
regular at the generic point of C0. If a mate G of degree n exists,
its pullback is a nonzero effective Cartier divisor on the smooth
surface S. The full support of that divisor is (nu^-1 C0)_red. There
is a unique curve component c, finite birational over C0, and it is
isomorphic to C0 since C0 is normal. A principal divisor on a smooth
surface cannot have isolated support points. Therefore

    (nu^-1 C0)_red=c,

and every normalization fiber above C0 consists of exactly one point.
This is a full-fiber condition, not merely a statement about the
generic fiber along C0. It is the same support argument as in the
[earlier normalization note](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-nonnormal-structural-progressmd).

If div(nu*G)=m c, intersection with H gives 4m=4n, so m=n. Since c
is Cartier and Pic(S) has no torsion, n(c-H)~0 implies c~H. Choose
f in H0(S,O_S(H)) with div(f)=c. Then

    nu*G=lambda f^n,  lambda in k*,

because their quotient has neither zeros nor poles on the projective
integral surface S. This global constant-unit conclusion is stronger
than a local affine-unit statement.

### 2. The actual upstairs conductor has no isolated defects

For completeness, the conductor is an invertible ideal on the smooth
normalization in this setting. This does not require the normalization
morphism itself to be flat.

Locally let A be a domain and B its finite normalization in the same
function field. Every A-linear homomorphism B->A becomes multiplication
by a scalar after tensoring with that function field. Evaluation at 1
therefore identifies

    Hom_A(B,A)={a in A : aB subset A}=I.

Finite absolute duality identifies Hom_A(B,omega_A) with the canonical
module of B. On the present surfaces, both are Cohen--Macaulay, X is
Gorenstein, and the dualizing sheaves have the same absolute dimension
shift. Thus, globally as an O_S-module,

    I O_S = omega_S tensor nu*(omega_X)^(-1).

Since X is a quartic hypersurface in P3, omega_X=O_X. Hence

    I O_S is isomorphic to omega_S,
    O_S(-D) is isomorphic to omega_S,  and D~-K_S.

In particular the actual conductor is an effective Cartier divisor
on S; there is no residual isolated or embedded zero-dimensional
conductor ideal upstairs. Reducedness of its support alone still does
not prove that this Cartier divisor is reduced.

The finite absolute-duality step is supported by the
[Stacks finite-map dualizing-complex lemma](https://stacks.math.columbia.edu/tag/0AX0)
and its [Cohen--Macaulay concentration criterion](https://stacks.math.columbia.edu/tag/0AWQ).
These are used for absolute dualizing complexes; no formula requiring
a flat Cohen--Macaulay morphism is applied to nu.

Also H.D=6, whereas H.c=4, so c is not D in the integral case. In the
rank-two reducible or nonreduced cases, each reduced component maps
isomorphically to Gamma and has H-degree three; c is not any such
component either. Consequently f|D is generically nonzero on every
reduced component used below.

### 3. The double-cover involution remains exact at nodes

Because 2 is invertible and p is finite flat of rank two, trace splits
the algebra as

    p_*O_D=O_Gamma direct-sum L,

where L is its trace-zero line bundle. Cayley--Hamilton for multiplication
by a trace-zero local generator eta gives eta^2=Delta in O_Gamma.
The map sigma(eta)=-eta, sigma(1)=1 is an algebra involution. Its fixed
algebra is exactly O_Gamma, including at branch points and nodal points
of D. This equality is scheme-theoretic; it is not inferred just from
the behavior on closed points.

The restricted hyperplane bundle is canonically

    O_S(H)|D=p*O_Gamma(1).

Here O_Gamma(1)=O_P1(3), since Gamma is a twisted cubic. The pullback
line bundle has the canonical sigma action. Projection formula and the
trace splitting show that its invariant sections, and those of every
tensor power, are exactly the sections pulled back from Gamma.

For integral reduced D, the same fixed-ring conclusion also follows
from normality of Gamma: an invariant section belongs to k(Gamma), is
integral over O_Gamma, and hence belongs to O_Gamma. The trace-algebra
proof makes explicit why a node upstairs introduces no additional
descent obstruction under the stated smooth-base hypotheses.

### 4. Integral reduced D forces a quadratic descended mate

The section nu*G descends from X, so its restriction to D is sigma
invariant. Thus, in the function field of the integral reduced curve D,

    (sigma(f|D)/(f|D))^n=1.

The roots of T^n-1 lie in k. A field element satisfying this polynomial
is one of those constants, so sigma(f|D)=zeta f|D for zeta in k*. Applying
sigma twice gives zeta^2=1. It follows that (f|D)^2 is sigma invariant.

An equality of rational sections of a line bundle on an integral
reduced curve is an equality of global regular sections when both
sides are regular: the line bundle is torsionfree. Thus this argument
is valid when D is nodal; it neither deletes the nodes nor replaces D
by its normalization. Consequently f^2|D is the pullback of a section

    t_Gamma in H0(Gamma,O_Gamma(2)).

If zeta=1, f itself descends by the same argument, yielding the even
stronger impossible hyperplane in section 6. The quadratic compression
works uniformly for zeta=1 and zeta=-1.

### 5. Entire-conductor gluing and the C0 contradiction

The conductor square is exact for every finite normalization. Locally,
with I its conductor,

    A = B fiber-product_(B/I) (A/I).

Indeed an element of B whose residue is in A/I differs from an element
of A by an element of I subset A. Twisting the sheaf identity by the
invertible O_X(2) gives the kernel sequence

    0 -> O_X(2) -> nu_*O_S(2H) direct-sum O_Gamma(2)
      -> nu_*O_D(2H).

The matching pair (f^2,t_Gamma) therefore gives a global section t_X of
O_X(2). This is direct gluing by a kernel equality, so no H1 vanishing
on the conductor or normalization is needed. Its pullback is f^2.

The hypersurface sequence

    0 -> O_P3(-2) -> O_P3(2) -> O_X(2) -> 0

and H1(P3,O(-2))=0 lift t_X to an ambient quadric Q. Finiteness and
surjectivity of nu, together with div(f^2)=2c, show

    (X intersect V(Q))_red=C0.

This contradicts the elementary quadric geometry of C0. Substituting
its displayed parametrization into the ten quadratic monomials gives
nine distinct degree-eight monomials, with the sole coincidence
x0*x3=x1*x2. Thus the unique quadric containing C0 is

    q=x0*x3-x1*x2,

which is smooth. On q=P1xP1, C0 has bidegree (1,3), after choosing the
order of the two factors. The restriction of an integral quartic X to
q is nonzero and has divisor class (4,4). A divisor supported only on
C0 would have class m(1,3), which cannot equal (4,4) for any positive
integer m. Hence the descended quadric cannot exist.

### 6. Reduced reducible D: contact prevents unequal eigenvalues

Retain all hypotheses except integrality, and now suppose D is
reduced reducible. Since D~-K_S, its arithmetic genus is one, so
chi(O_D)=0. For the trace splitting over Gamma=P1 this gives

    L=O_P1(-2),  eta^2=Delta,
    Delta in H0(P1,O(4)).

Reduced reducibility makes Delta a nonzero square in k(P1). Its divisor
is even; hence Delta=q^2 for a nonzero q in H0(P1,O(2)), up to a scalar
square absorbed over k. Thus D consists of two smooth copies D+ and
D- of Gamma, eta=+q and eta=-q, meeting at the zeros of q. At a zero
of multiplicity m their intersection multiplicity is m, where m=1 or 2.

Write f|D=a+eta b, where a is a section of O(3) and b a section of
O(1). The mate descent gives

    (a+q b)^n=(a-q b)^n.

Both sides are generically nonzero. In the function field of Gamma,
there is therefore a constant root of unity zeta with

    a-q b=zeta(a+q b).

If zeta=1, then b=0 and f itself is an invariant section. Entire
conductor gluing in degree one yields an ambient hyperplane containing
C0, impossible since its four coordinate forms are independent.

Suppose zeta!=1. Solving the displayed identity shows that both branch
restrictions are nonzero scalar multiples of q ell, with ell a nonzero
section of O(1). The section ell has exactly one simple zero on P1.
If that zero were not a zero of q, then f would vanish at two distinct
normalization points over the same point of Gamma. Both would belong
to c, contradicting the full singleton-fiber condition in section 1.
Therefore ell vanishes at a zero of q of multiplicity m. At their
common point, the restrictions of f to both D+ and D- have order m+1.

Here is the exact local smoothness contradiction. Two smooth branches
on a smooth surface with contact m can be written formally as

    D+:w=0,  D-:w=u(t)t^m,  u(0)!=0.

Their restrictions of f have order >m, hence >1. The first branch
therefore gives f_t(0)=0; smoothness of c=V(f) gives f_w(0)!=0. Taylor
expansion then gives

    f(t,u(t)t^m)-f(t,0)
       =u(0) f_w(0) t^m + terms of higher order.

Its order is exactly m, while the difference of the two restrictions
of order >m must have order >m. This is a contradiction. Thus no
zeta!=1 is possible. The reduced reducible case is excluded without
assuming its conductor nodes are ordinary pinch points.

### 7. A rank-two nonreduced addendum

This addendum was proposed and independently audited by the separate
normal-global-adversarial agent. It retains the exact entire conductor,
smooth Gamma, and finite flat rank-two assumptions; it is not a claim
about arbitrary nonreduced conductors.

In characteristic zero, a rank-two algebra eta^2=Delta is generically
reduced when Delta is not identically zero. Flatness over the smooth
curve prevents nilpotents supported only at finitely many points.
Hence a nonreduced D under these hypotheses has Delta=0 and

    p_*O_D=O direct-sum O(-2),  eta^2=0.

Writing f|D=a+eta b as above, a is generically nonzero because c is not
the reduced conductor component. The equality that f^n descends is

    f^n=a^n+n a^(n-1)b eta,
    n a^(n-1)b=0.

The tracefree summand is a line bundle on the integral smooth Gamma,
so is torsionfree. Since n!=0 and a is nonzero generically, b=0.
Thus f itself descends to an ambient hyperplane, again impossible.
This handles all conductor scheme structures inside the specified
smooth-base, flat-rank-two class.

### 8. Boundaries and continuation information

The resulting criterion excludes every smooth normalized rational
quartic scroll whose actual downstairs conductor is a smooth twisted
cubic and whose entire upstairs conductor is finite flat of rank two
over it. It requires no ordinary-pinch assumption. Its applicability to
a literature-defined class still requires verification of these exact
conductor-scheme hypotheses, not merely a picture of its double curve.

It does not settle cases where Gamma is nonnormal, reducible,
nonreduced, or has additional conductor scheme structure; where the
finite conductor map has another rank or is not flat; where S is
singular; or where c meets singularities of S. On a nonnormal Gamma,
the invariant ring may be its normalization rather than O_Gamma, and
an invariant section need not descend through the actual conductor
square. On a higher-rank or nonflat nonreduced conductor, the simple
rank-two nilpotent argument is insufficient.

The proof uses global homogeneous sections and the actual conductor,
so arbitrary affine units, omitted isolated inverse-image points, or
normalization of D cannot silently change its hypotheses. The local
contact and trace-algebra identities have a self-contained exact
[companion verifier](../computations/verify_session_scroll_conductor_compression.py).
The verifier is an identity check; the all-degree proofs are the
field-root, Taylor-order, and torsionfree arguments above.

---

<a id="source-2026-10-08-session-late-results-acceptancemd"></a>

## Ancestor incidence and smooth-scroll consequences

Fix C0 in characteristic zero. The [quartic-carrier theorem](../synthesis/quartic_carrier_proof.md) supplies the complete quartic-carrier exclusion; the incidence and conductor arguments below retain independent structural content. Ancestor exclusions and carrier exclusions have different hypotheses. The unrestricted characteristic-zero STCI question remains open.

### 1. The entire e=1,d2=1 common quartic ancestor lane

**PROVED under the accepted canonical-triple reduction and P-037.**
No common quartic ancestor of the two fixed independent targets has
e=1 and a genuine second defect of degree one.

The [independent principal completeness audit](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-principal-e1-d1-independent-completeness-auditmd)
exhausts the principal chart and its projective complement. On the
declared open the complete eighteen-dimensional quartic ideal space
has first/contact rank 17. The first-normal determinant, complete
seven-column frame, all seven cofactors, resultant gcd, quadratic-field
fibre and the retained nonunit S branch are checked exactly. The
alternative killing section at infinity is reconstructed in the actual
balanced chart. All three b0=0 conjugates are retained.

The sole dimension exception is (p,r)=(2,1/2): the complete quartic
space has dimension four, with a fixed cubic times every linear form.
It is excluded by division and P-037. Every other valid principal
fibre has quartic dimension one, so cannot produce independent targets.
A uniform dimension-one assertion on the whole lane would be false.

Root rechecked the antecedents: the six nonprincipal endpoint triples
are exhausted and excluded by their complete quartic spaces in the
[endpoint ancestor proof](#source-2026-10-08-session-localcoh-e1-d1-endpoint-ancestorsmd).
At the primitive obstruction-zero point, the only correction has no
additional H0(O(-3)) freedom; multiplication by a degree-one killing
section shares its zero, so it is not a genuine finite-flat positive
defect triple. The principal and endpoint pieces therefore exhaust
the degree-one ancestor lane. The surviving e=1 ancestor degrees are
d2=2,3,4, with the separately excluded quadric and algebraic directions
still removed.

The principal-rank proof uses the exact reconstructed input and independent geometric argument. Repeated source snapshots and process transcripts are not additional independent mathematical checks.

### 2. Smooth quartic scrolls: reduced or locally Gorenstein conductor

**PROVED:** if an integral quartic X has smooth rational quartic-scroll
normalization and its actual downstairs conductor Gamma is reduced
or locally Gorenstein, X has no mate supported only on C0, in any
positive degree. The theorem retains arbitrary upstairs conductor D.

The actual conductor is an ACM cubic with Hilbert polynomial 3m+1;
this is a scheme-level result, not a claim about the Jacobian radical.
The [ACM audit](QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md)
and [owner proof](QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md)
derive its Hilbert--Burch presentation and the exact sequence
0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.
The reduced theorem includes the smooth twisted cubic, conic plus line,
and all three-line configurations. The concurrent three-line case is
excluded geometrically before any flat-cover assertion. See the
[conic-plus-line audit](QUARTIC_SCROLL_REDUCED_CONDUCTORS.md)
and [three-line audit](QUARTIC_SCROLL_REDUCED_CONDUCTORS.md).

For locally Gorenstein Gamma the exact sequence makes p finite flat
of rank two even when Gamma is nonreduced. A locally Gorenstein triple
line is impossible: devissage makes the degree of every invertible
sheaf divisible by three, while deg(omega_Gamma)=-2. The doubled-line
generic Artin algebra gives only the partitions (a,r)=(4,1),(2,2),
or two (2,1), with a the upstairs nilpotent length and r the residue
extension degree. The F0/F2 anticanonical classes exhaust these cases.
Disjoint paired fibres and the global prime-exchange incidence
obstruction remove the exchanged-prime configurations. In the remaining
cases the involution preserves every conductor prime. The equation
sigma(f)^n=f^n then forces sigma(f)/f=+1 or -1 in each entire generic
Artin ring, with no nilpotent correction. Cohen--Macaulay purity extends
square invariance globally, and the conductor square descends f^2 to
the forbidden quadric mate. The
[independent Gorenstein audit](QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md)
accepts this scope. Root checked the thick-base partitions and the
prime-exchange qualification; reduced-fibre reasoning alone would not
justify them.

Section 5 supplies the full nonreduced nongorenstein conductor argument. Singular normalizations and higher carrier degrees remain separate from this smooth-scroll theorem.

### 3. The principal exceptional quartic (p,r)=(8,1/2)

**PROVED all-mate exclusion of this fixed carrier.** Its explicit
normalization is F0. In invertibly changed coordinates the equation is
(xL-8yz)^2-x^3(x-8y), L=96w+x-8y+4z. The entire downstairs conductor
is (x^2,xy,xL-8yz), a double line plus a line; its upstairs divisor is
2{U=0}+2{b=0}. The actual nonreduced conductor is locally Gorenstein,
so its complete finite flat algebra, including nilpotents, gives the
square compression in section 2.

The [owner proof](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-rhalf-scroll-conductormd)
and [independent audit](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-rhalf-scroll-independent-auditmd)
bind this equation to the unique actual boundary quartic. Root
independently derived the normalization-ring closure and all six
annihilator identities. Hilbert--Burch and the actual conductor Hilbert
polynomial prove equality of the entire ideal sheaves, not just their
support.

The other complement carriers were already excluded as normal quartics
or quartics singular along smooth twisted cubics. The principal direction-curve incidence remains distinct. Its nonnormal locus is a proper
closed finite subset of the geometrically integral direction curve:
the unique quartic kernel gives a regular projective family away from
the treated node, and a normal b0=0 fibre makes the closed
positive-dimensional Jacobian-fibre locus proper. The exact finite
subset is not yet enumerated. See section 6 of the
[boundary proof](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-principal-boundary-auditmd).

### 5. Final accepted extension: every smooth rational quartic scroll

**PROVED:** let X be an integral quartic with finite normalization S=F0,
H=C+2f, or S=F2,H=C+3f, over an algebraically closed characteristic-zero
field. No hypersurface of any positive degree has intersection with X
supported exactly on the fixed C0. Both actual conductor schemes are
unrestricted. It includes every conductor type; singular normalizations and other polarized normalization classes remain outside this smooth-scroll theorem.

The [nongorenstein classification](QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md)
uses the actual three-by-two linear Hilbert--Burch matrix. Its projective
rank-zero locus is a point or a line. The point case is a cone over a
noncollinear length-three scheme in P2; saturation and absence of linear
ideal forms, not merely h0(O_Z(1))=3, prove noncollinearity. The residual
nonreduced nongorenstein ideals are the double-line-plus-line,
curvilinear triple-line, and fat triple-line ideals. The locally
Gorenstein cases were already covered in section 2.

At a curvilinear triple line A=K[epsilon]/epsilon^3, B is free of rank
two. Multiplication by epsilon has K-rank four. Its truncated-DVR
factors have ranks bounded by two thirds of their lengths, so equality
forces every actual upstairs multiplicity divisible by three. This
contradicts the coefficient two of C in D=-K_S.

For a fat triple line A=K+N,N^2=0,dim N=2, the exact quotient B/A=omega_A
gives dim NB=3 and dim B=6. The finite product of truncated DVR factors
is Frobenius over K. Since (NB)^2=0, NB=Ann_B(NB); consequently every
conductor multiplicity is even. Thus D=2E with E=C+f on F0 or C+2f
on F2. A prime E has degree three over the supporting line and would
need three transverse totally ramified intersection points with c;
Riemann--Hurwitz permits at most two. A horizontal degree-two component
plus a degree-one fibre forces a double zero at one ramification point,
contradicting transversality of the smooth image. Distinct fibres give
two different normalization points above the same required zero. The
only remaining class is D=2C_min+4F on F2.

That final pattern has NB_F=(t^2) in its length-four factor. Ambient
normal coordinates to the support line therefore vanish to order at
least two along F, making d nu generically rank one there. The
[independent differential lemma](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-normalization-differential-independent-auditmd)
excludes it. Root checked the lemma directly: a unit Jacobian pivot
gives a regular kernel vector modulo the prime ideal of the conductor
component. Differentiating the full power identity in an ambient-unit
trivialization yields n f^(n-1)V(f)=0 on that integral component.
Cancellation takes place generically, followed by extension in the
domain; it does not divide by f at its zero. At an intersection with
the smooth c, its tangent is the kernel, contradicting immersion of
nu|c. The lemma also permits singular conductor primes. An isolated
differential rank-drop point does not satisfy its hypothesis.

Finally, the [exact Artin audit](QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md)
completes double-line-plus-line conductors directly, including the
nongorenstein junction. Above the doubled line, free rank two over
K[epsilon]/epsilon^2 gives only (a,r)=(4,1),(2,2), or two (2,1).
Above the reduced line the patterns are (2,1),(1,2), or two (1,1).
The (4,1) and (2,1) single-prime cases have generic rank-one differential
and are excluded. On F0 the remaining doubled horizontal prime leaves
two distinct paired fibres. On F2 the remaining doubled minimal section
and fibre likewise leave paired fibres, or two doubled fibres leave an
impossible reduced-line component class. Every pattern is therefore
excluded. No global trace through a nongorenstein point is asserted.

This proof uses entire Artin rings and the whole mate equation. The
alternative transversal-plane delta argument is retained as a proposed
secondary route; it is not needed for the accepted theorem. The
independent Artin audit, differential audit, the
[complete independent scroll audit](QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md)
and root verification supply the scope. No broad classification of all nonnormal quartic
surfaces is inferred from the classification of these ACM cubics.

### 6. Exact second-family closure and actual-tensor binding

Both factors k^2+1 and k^2-2k-1 are excluded at all four geometric roots
and for every lower parameter lambda. The
[owner proof](LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md)
and [independent audit](LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md)
check polynomial duals with n^T L=0 and n^T u=1 on all eighteen actual
quartic columns. Separate exact-field arithmetic rederives the seeds,
directions, slopes, rank-29 top map and complete affine lift fibre.
The independent Macaulay2
[actual-tensor reconstruction](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2)
binds all 540 products and both target columns literally and proves
equality with the complete next-stage Ext image.

The cubic, quartic and degree-fifteen factors are also closed over their full exact quotient fields, uniformly in lambda, in [the completed endpoint proof](LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md). Thus all 26 exceptional geometric roots of the second family are excluded; the first family is likewise complete. Nonendpoint top-zero charts require their separate actual incidence analysis.

---

<a id="source-2026-10-08-session-localcoh-e1-d1-endpoint-ancestorsmd"></a>

## The six defective e=1 endpoint triples also exclude quartic ancestors

Date: 2026-10-08. Fixed `C0` in characteristic zero. Status:
**PROVED COROLLARY OF THE ACCEPTED COMPLETE QUARTIC FIBRES AND P-037.**
This is an ancestor-specific consequence; it uses no STCI mate, BF mate
bound or single-carrier cubic-pole inference.

Let quartics `F,G` and an ancestor alpha satisfy `F*alpha=u,G*alpha=v`.
Their canonical triple is contained in both multipliers. If it has
`e=1,d2=1` and is on the complete `a0=0` or `b1=0` boundary of the
defect-killed quadratic class, the actual torus normalization gives one
of the six triples from
[`2026-10-07-session-mf6-e1-d1-endpoints.md`](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-d1-endpointsmd):

```text
A=r*z, B=1+z, delta=z,
or A=1+r*z, B=1, delta=1,
with r=-1/2 or 12r^2+4r+3=0.
```

At each of the four algebraic direction fibres, the **complete** quartic
space has dimension one (rank 34 in all 35 ambient monomials). Hence
F and G are proportional. Their images u and v would then be
proportional, contradicting their linear independence.

At each of the two rational-root fibres, the complete quartic space is
`C*H0(P3,O(1))`, with the fixed nonzero cubic C equal to C_L or C_R
from the endpoint audit. Thus `F=C*F1,G=C*G1` for actual homogeneous
linear forms F1,G1, and

```text
F1*(C*alpha)=u, G1*(C*alpha)=v.
```

This is a common ancestor with degree-one multipliers, prohibited by
the all-stage P-037 theorem. Since u is nonzero, `C*alpha` is nonzero;
the passage does not annihilate the ancestor.

The only symmetry used to normalize the six triples is the actual
ambient torus preserving C0 (and the reversal for equivalent charts).
Under the torus `(x0,x1,x2,x3)->(x0,lambda*x1,lambda^3*x2,lambda^4*x3)`,
q and B have weights four and six and the target numerators have weights
three and five. Therefore u and v are eigenvectors of respective
weights -7 and -5. Nonzero scalings can be absorbed into F1,G1, so
P-037 remains applicable to the fixed targets. Coordinate reversal
preserves q, sends B to -B, and swaps the two target numerators;
it exchanges u and v with the same harmless nonzero sign.

All six endpoint triples are therefore excluded from the quartic-ancestor
problem. The principal `a0*b1!=0` portion of the d2=1 sextic remains
open, as do the positive-defect d2=2,3,4 ancestor strata. In particular
the d2=4 Gorenstein case remains; its elimination does not follow from
the STCI quartic bound.

More generally, the same exact argument excludes a candidate canonical
triple if its full quartic space has dimension at most one, or if every
quartic in that space has a fixed factor of degree one, two or three:
division gives multipliers of degree at most three, prohibited by P-037.
This is a useful first check before computing the unique conormal
socle quotient from the splitting criterion.

The complete ambient fibre ranks and fixed factors were independently
audited in the endpoint source. The MF6 auditor reconfirmed those ranks,
the actual torus weights and reversal on 2026-10-08. This proof depends
on those complete spaces; merely inspecting the displayed FL/FR forms
would not suffice.

---

<a id="source-2026-10-08-session-localcoh-e1-d4-algebraicmd"></a>

## Two algebraic e=1 directions exclude d2=4 quartic ancestors for every defect section

Date: 2026-10-08. Fixed C0 in characteristic zero. Status:
**PROVED BY COMPLETE QUARTIC FIBRES AND A PARAMETER-COVERING RANK ARGUMENT;
accepted after independent and root review.** See the
[root acceptance record](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-new-results-acceptancemd).
This treats exactly the two
directions `A=r*z,B=1,12r^2+4r+3=0` with d2=4. Other positive-D2
directions and Gorenstein quadruples outside these fibres remain open.

### 1. Genuine degree-four defects and their complete linear incidence

These directions have zero primitive quadratic obstruction and unique
primitive correction gamma0=0. For a defect section delta in H0(O(4)),
every degree-four corrected triple has relation

```text
delta*m+theta*y^2=0,
m=U-r*z*V, y=V.
```

The extra global correction theta is a constant because its bundle is
O(-4+d2)=O(0). If theta=0, it shares every zero of delta, violating
finite-flatness of a genuine defect-four triple. Every nonzero homogeneous
quartic has a projective zero, including an infinity zero when its affine
degree drops. Thus theta is nonzero, and simultaneous scaling of delta
and theta normalizes theta=1. Delta is an arbitrary nonzero homogeneous
quartic; its repeated roots and infinity roots are retained.

Write the actual quartic jet on the canonical double as
`F=h*m+E*y^2+...`. It contains this triple if and only if

```text
h=delta*E.
```

An ancestor needs two linearly independent quartics because its target
classes u and v are independent. The proof below shows that this exact
linear containment system has dimension at most one for every delta.
No STCI mate or BF d2 bound is involved.

### 2. The complete seven-dimensional double-quartic space

The independent source reconstructs all 35 ambient degree-four monomials
and imposes both the curve restriction and the first normal coefficient
along `U=r*z*y,V=y`. Its exact matrix has rank 28 over the quadratic
field; all identities are reduced modulo `12r^2+4r+3`, so both roots
are covered. The complete seven-dimensional quartic space has two
primitive members with `(h,E)=(1,0),(z^8,0)`, and five other members
with

```text
(h,E)=(a_i*z^(i+2), z^i), i=0,1,2,3,4,
a0=3r-1/2,
a1=6r+2,
a2=0,
a3=4r-5/3,
a4=(66r+13)/18.
```

Their seven explicit ambient forms and the full rank verification are
stored in the standalone checker and its JSON. The five a_i are pairwise
distinct at either root: every difference is a unit modulo the defining
quadratic.

For a general member write `E=sum(e_i*z^i,i=0..4)`. Its h is

```text
h=A+B*z^8+sum(a_i*e_i*z^(i+2),i=0..4).
```

The free A and B match the constant and eighth coefficients of delta*E
uniquely. Thus the full quartic containment space is canonically the
kernel of the seven-by-five matrix obtained from coefficients z^1
through z^7 of

```text
delta*E-sum(a_i*e_i*z^(i+2),i=0..4).
```

### 3. Exact minors cover every defect section

Write `delta=d0+d1*z+d2*z^2+d3*z^3+d4*z^4` in its finite chart.

If d0 is nonzero, the rows z^1 through z^4 and columns e1 through e4
have determinant d0^4. Therefore the matrix has rank at least four
and kernel dimension at most one. Equivalently those low coefficients
determine e1,e2,e3,e4 successively from e0.

If d4 is nonzero, the rows z^4 through z^7 and columns e0 through e3
have determinant d4^4. The same conclusion follows from the high
coefficients, including infinity behavior.

It remains to retain the entire boundary d0=d4=0. There the first five
rows have determinant d1^5, and the last five rows have determinant
d3^5. If either d1 or d3 is nonzero, the matrix has full rank five.

The final boundary is `delta=d2*z^2`. The middle five rows are the
diagonal matrix

```text
diag(d2-a0,d2-a1,d2-a2,d2-a3,d2-a4).
```

Since the a_i are pairwise distinct, at most one entry can vanish.
Its rank is at least four. This final case includes the defect section
with double zeros at both endpoints; it is not discarded as a repeated
or pole stratum.

These cases cover every delta, and prove kernel dimension at most one
uniformly. Hence every genuine defect-four triple in either algebraic
direction has at most one independent containing quartic, and cannot
support the two independent multiplier equations of a common quartic
ancestor.

### 4. Exact evidence and retained scope

Run

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
 research/computations/verify_session_localcoh_e1_d4_algebraic_2026_10_08.py
```

The checker independently reconstructs the complete ambient space,
checks all seven explicit forms and their h/E coefficients, checks
pairwise differences in the exact field, and verifies all four minor
identities and the last diagonal case. It uses no discovery JSON as a
proof input. Its companion JSON records the full matrix and source hash.

The principal obstruction-zero direction `A=1+z,B=-2-8z` still needs its
defect-four rank incidence. Its complete double-quartic map is saved in
`explore_session_localcoh_e1_d4_quartic_map_2026_10_08.json`. The unique
quadric direction is already excluded for every D2 by the separate
double-divisor/P-037 proof. Directions with nonzero primitive quadratic
obstruction are not covered by this note. No claim eliminating an entire
d2=4 Gorenstein stratum follows.

---

<a id="source-2026-10-08-session-localcoh-e1-d4-independent-auditmd"></a>

## Independent audit of the algebraic e1,d2=4 quartic exclusion

Date: 2026-10-08. Fixed C0, characteristic zero. Scope: exactly
`A=r*z,B=1,12r^2+4r+3=0`, genuine degree-four second defect. The audited
claim is in
[`2026-10-08-session-localcoh-e1-d4-algebraic.md`](#source-2026-10-08-session-localcoh-e1-d4-algebraicmd).

**ACCEPTED:** every genuine triple in either algebraic direction has a
complete space of containing ambient quartics of dimension at most one.
It therefore cannot be the canonical triple of a quartic common ancestor
with independent target classes u and v. This is uniform over every
defect section, including repeated roots and roots at infinity. It does
not eliminate the other directions or an entire Gorenstein stratum.

### Genuine triples and normalization

The previously audited defective-triple presentation is
`J=(delta*m+theta*y^2,m*y,m^2,y^3)`, up to the harmless sign convention
for the correction. For these obstruction-zero directions the primitive
correction is zero. The possible additional correction is a section of
`O(-4+d2)=O(0)`, so theta is a scalar.

The theta-zero branch is excluded by finite-flatness, rather than being
discarded to make the rank argument work. Near a zero of the nonzero
defect section, take a support DVR R. If theta is zero, the quotient has
R-module presentation

```text
R*1 + R*y + R*y^2 + (R/(delta))*m.
```

The last summand is nonzero torsion, inconsistent with finite-flatness
over R. Every nonzero homogeneous section of `O(4)` has a projective
zero over the algebraically closed field. This includes an infinity
zero when its finite polynomial has degree below four. Thus theta must
be nonzero. Dividing the relation by theta normalizes theta to one and
replaces delta by delta/theta, preserving the same triple and its defect
divisor. This retains every nonzero five-coefficient quartic delta; no
root separation or finite-support assumption is used.

With theta one, the quotient has free basis `1,y,m` and relation
`y^2=-delta*m`. Therefore an actual quartic jet
`F=h*m+E*y^2+...` vanishes on the triple exactly when `h=delta*E`.
The omitted terms lie in `(m*y,m^2,y^3)`. This also proves the containment
criterion at zeros of delta, rather than merely away from them.

### Complete ambient quartic space

The source enumerates all exponent quadruples of sum four: there are
`binomial(7,3)=35`, each occurring once. It substitutes the actual
finite-chart normal parameters and imposes the constant and first
normal coefficients of the canonical double. The resulting `31x35`
matrix has rank 28 over `QQ(sqrt(-2))`.

The defining polynomial has discriminant `-128` and is irreducible over
QQ. The chosen root is `(-1+2*sqrt(-2))/6`. Every entry is rational in
r; conjugation preserves rank, so the second root is also covered.
The source verifies seven independent homogeneous quartic forms in the
kernel. Rank-nullity shows that these span the complete ambient space,
rather than a selected pencil. Checking the dense finite chart suffices
for the global double conditions: the primitive double is finite-flat
over C0, so its structure sheaf has no support torsion at infinity.
The forms themselves are homogeneous global forms.

The normalized basis consists of two forms with `(h,E)=(1,0),(z^8,0)`
and five forms with

```text
(h,E)=(a_i*z^(i+2),z^i), i=0,...,4,
(a0,a1,a2,a3,a4)=(3r-1/2,6r+2,0,4r-5/3,(66r+13)/18).
```

All their normal coefficients are checked exactly modulo the quadratic.
Every pairwise difference `a_i-a_j` is a unit in the field.

For `E=sum(e_i*z^i)`, the two primitive basis coefficients determine
the constant and eighth coefficients of h freely. Containment determines
them uniquely as the corresponding coefficients of `delta*E`. The
remaining seven equations are the coefficients z through z^7 of
`delta*E-sum(a_i*e_i*z^(i+2))`. Hence the containing-quartic space is
isomorphic to the kernel of the displayed `7x5` operator. In particular,
E zero does not leave an extra primitive quartic: it forces h zero and
both primitive coefficients zero.

### Coverage of every defect section

The four minor identities provide an exhaustive case split:

1. If d0 is nonzero, the lower `4x4` triangular minor is d0^4.
2. If d4 is nonzero, the upper `4x4` triangular minor is d4^4.
3. With d0=d4=0, the first five-row determinant is d1^5, and the last
   five-row determinant is d3^5. A nonzero d1 or d3 gives rank five.
4. The entire remaining locus is `delta=d2*z^2`. Its middle five-row
   matrix is `diag(d2-a0,...,d2-a4)`. Since the a_i are pairwise distinct,
   at most one diagonal entry can vanish, so rank is at least four.

These are polynomial identities and field-unit statements, valid at
both roots of the quadratic. They prove rank at least four everywhere,
and kernel dimension at most one. The last case explicitly retains the
section with double zeros at both endpoints. A section with d4 zero has
an infinity zero; it is covered by the same coefficient split. Nothing
in the argument assumes reduced support.

If two quartics F,G gave `F*alpha=u,G*alpha=v`, both would contain the
canonical triple and would be proportional in this at-most-one-dimensional
space. Their images would be proportional, contrary to the independent
targets. This uses the accepted canonical-triple reduction for ancestors,
not an STCI mate bound or a further carrier classification.

### Exact computational support

The retained self-contained
[`source`](../computations/verify_session_localcoh_e1_d4_algebraic_2026_10_08.py)
reconstructs the complete matrix and basis, checks the seven ambient forms,
and verifies the minor identities and final diagonal case used above.
It reads no discovery JSON or generated proof input. The geometric
interpretation and the theta-zero torsion argument remain part of the
proof, with the characteristic and direction hypotheses stated there.

---

<a id="source-2026-10-08-session-localcoh-quadric-directionmd"></a>

## Every quartic ancestor in the quadric quotient direction is excluded

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]` in characteristic
zero. Status: **PROVED, conditional on the accepted ancestor-to-canonical-
triple reduction and P-037.** This removes a specific conormal direction
for **every** second-defect divisor. It does not remove an entire
positive-D2 degree stratum. The d2=4 Gorenstein possibility outside this
direction is retained.

Let `Q=(q=0)`, with `q=x0*x3-x1*x2`. It is the smooth Segre quadric.
Up to interchange of the two rulings, C0 has class `(1,3)` on Q:
its two projection degrees are three and one. In the balanced finite
normal frame

```text
V=x2-z^3, U=q-z*V/2,
```

the quotient direction `A=-z/2,B=1` is exactly the conormal quotient
of C0 inside Q, of degree -6. Indeed the transverse path
`U=-(z/2)*epsilon,V=epsilon` has q identically zero. Thus its canonical
double is the double divisor `2C0` on Q. This identification uses only
the first quotient; positive D2 and any higher degeneration do not
change the canonical double.

Suppose a common quartic ancestor exists in this direction. Both F and
G contain its canonical triple, hence contain this canonical double.
Their restrictions to Q therefore belong to

```text
H0(Q, O_Q(4,4)(-2C0))=H0(Q,O_Q(2,-2))=0.
```

The last equality follows from the product cohomology of P1 times P1:
a negative degree on either ruling has no global sections. Consequently
both quartics restrict to zero on Q and are divisible by q. Write
`F=q*F2,G=q*G2`. The original equations give

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This contradicts the all-stage degree-two common-ancestor exclusion
P-037. The nonzero target u ensures `q*alpha` is nonzero. The proof
uses neither a mate supported on C0 nor a false assertion that F
annihilates the quadruple.

In particular the proof includes the otherwise retained `e=1,d2=d3=4`
Gorenstein boundary **when its first quotient is this quadric direction**.
It also includes quartics with zero first-normal symbol. No assumption
that the canonical triple is primitive is made.

The independent exact coefficient check
[`verify_session_localcoh_quadric_direction_2026_10_08.py`](../computations/verify_session_localcoh_quadric_direction_2026_10_08.py)
reconstructs all 35 ambient degree-four monomials and imposes both
vanishing on C0 and the first derivative along the actual Q path. The
combined matrix has rank 25. Its complete ten-dimensional kernel is
`q*H0(P3,O(2))`, checked against ten independent homogeneous quadratic
monomials. This matches the divisor proof and rules out any omitted
quartic first-symbol kernel member.

The rank check is a separate exact verification of the complete quartic
space; the global divisor proof supplies the defect-independent reason.
The two already excluded cubic-factor endpoint directions and four
one-dimensional endpoint fibres are recorded separately in
[`2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md`](#source-2026-10-08-session-localcoh-e1-d1-endpoint-ancestorsmd).

