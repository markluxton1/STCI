# genus one ribbon net independent audit

## Dependency guide: ribbon reduction and quadratic net

This is the **upstream conditional reduction**: the degree-four ADE del Pezzo normalization and D5 torsion inputs force the indicated double divisor to be a ribbon and constrain its conormal quadratic net. Its two direction orbits organize, but do not by themselves exclude, all projection/contact cases. See [uniform projection conditions](genus_one_uniform_projection_analysis.md), [the repeated-partition proof](genus_one_ribbon_partition_proofs.md), and [independent partition certificates](genus_one_ribbon_partition_proofs.md#genus-one-ribbon-repeated-partition-independent-certificates). Preserve the stated normalization hypotheses; the ribbon conclusion is not a theorem about arbitrary quartic carriers.

---


Permanent detailed mathematical record, including all proofs, calculations, counterexamples and explicit unresolved conditions.

# Bounded audit: the genus-one double divisor is a ribbon, and its quadratic net has two direction orbits

Date: 2026-10-09. Owner: `ribbon_reduction_audit`.
Status: **PROVED HERE under the accepted hypotheses below**, with a separate
local-algebra/conormal audit by `local_double_structure_check`. This is an
independent bounded audit of the proposed ribbon reduction. It does not
exclude all genus-one normalizations or resolve the unrestricted STCI problem.
No state or acceptance file is changed by this note.

## 1. Inputs and conclusion

Work over an algebraically closed field of characteristic zero. Accept the
following inputs from the genus-one/D5 reductions:

* The finite normalization is an integral ADE del Pezzo surface
  `S=V(f1,f2)` in `P4`, a complete intersection of two quadrics, with
  `H=O_S(1)=-K_S`.
* Its lifted curve is the embedded smooth rational normal quartic
  `c=[U^4:U^3 V:U^2 V^2:U V^3:V^4]`.
* There is a nonzero section `Q` of `O_S(2H)` whose entire Weil divisor is
  exactly `2c`.

Then `D=V_S(Q)` is globally a ribbon over `c`, including at points where
`S` is singular and `c` is non-Cartier. Its nilideal is `O_P1(-6)`.
Every quadratic net defining this ribbon is given by the three equations
in section 4. Its direction must satisfy `B^2 != A C` if the two surface
quadrics define an integral degree-four surface. The discriminant-zero
directions instead have a cubic surface as their quadratic base locus.

The accepted preceding inputs are recorded in
[the genus-one reduction](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
and [the D5 filter](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd).
They are premises here, not reproved by this audit.

## 2. Pure multiplicity two over a smooth curve forces a ribbon

Here is the needed local lemma, which does not require characteristic zero.
Let `B` be a Noetherian one-dimensional local Cohen--Macaulay ring. Let
`J=sqrt(0)`, suppose `R=B/J` is a DVR, and suppose the generic Artinian
local ring `B_J` has length two. Then

    J^2=0,              J is a free rank-one R-module.

Indeed `J` is the only minimal prime and Cohen--Macaulayness excludes
embedded associated primes, so `Ass(B)={J}`. Every element outside `J`
is a nonzerodivisor and `B -> B_J` is injective. The maximal ideal of
the length-two Artinian local ring `B_J` has length one and square zero
(otherwise Nakayama would give that it vanishes). Thus `J^2=0` in `B`.

Multiplication on `J` therefore factors through `R`. The finite module
`J` has generic rank one. Every nonzero element of `R` lifts to an
element outside `J`, hence acts injectively on `J`. Thus `J` is
torsion-free over the DVR `R`, and consequently free of rank one.
Equivalently, any putative nonzero `J^2` would be a finite-length
submodule of the pure Cohen--Macaulay curve ring, which is impossible.

At a closed point of `D`, the surface ring is a normal local domain
of dimension two, hence Cohen--Macaulay by `S2`. The local equation of
`Q` is a nonzero nonzerodivisor, so its quotient is Cohen--Macaulay of
dimension one. The exact divisor identity `div(Q)=2c` gives the single
reduced support `c` and generic length two. Smoothness of the embedded
`c` makes its reduced local ring a DVR. The lemma applies at every point.
The resulting rank-one nilideals glue to an invertible sheaf `L` on `c`.

The distinction from a nonreduced scheme-theoretic inverse image is essential.
Only the Cartier divisor `D=V_S(Q)` is used here. For example

    k[[t,e]]/(t e^2,e^3)

has smooth reduction and generic length two but an embedded point;
its nilideal has nonzero square `(e^2)`. Thus support and generic
multiplicity alone would be insufficient.

### A1 and A3 local checks

For an `A1` singularity,

    A=k[[x,y,z]]/(xy-z^2),   p=(x,z),   q=x,
    A/(q)=k[[y,z]]/(z^2).

The reduced curve is smooth and the nilideal is freely generated by `z`
over `k[[y]]`. The curve is nevertheless non-Cartier at the singularity.
In fact

    p^2=x(x,y,z) is strictly contained in (x)=p^(2).

For the order-two class through the middle of an `A3` chain, use

    A=k[[x,y,z]]/(xy-z^4),
    p=(x-z^2,y-z^2),        q=x+y-2z^2.

Set `u=x-z^2` and `v=y-z^2`. The identities

    u v=-z^2 q,            u^2=q x,           v^2=q y

give

    p^2=q(x,y,z^2) is strictly contained in (q)=p^(2),
    A/(q)=k[[z,u]]/(u^2),   A/p=k[[z]].

Thus the Cartier double is a ribbon although `p` has two minimal
generators and is non-Cartier. Its divisor-class order is exactly two.
The ordinary square of the curve ideal defines a different thickening;
the ribbon assertion neither identifies that ordinary square with `(q)`
nor makes the reduced curve Cartier in the singular surface.

## 3. Genus and the nilideal degree

The restriction map

    H0(P4,O(2)) -> H0(S,O_S(2H))

is surjective. The complete-intersection resolution twisted by two is

    0 -> O_P4(-2) -> O_P4^2 -> I_S(2) -> 0,

and intermediate projective-space cohomology gives `H1(I_S(2))=0`.
Lift `Q` to a quadric `f3`. The first two quadrics are a regular
sequence and the third is nonzero in their integral quotient, hence
is a nonzerodivisor there. Consequently

    D=V(f1,f2,f3)

is a complete intersection of degrees `(2,2,2)` in `P4`. Its degree
is eight and adjunction gives arithmetic genus five:

    p_a(D)=1 + (2+2+2-5)*8/2=5.

From the ribbon sequence

    0 -> L -> O_D -> O_c -> 0

and `c=P1`, one has `chi(O_D)=deg(L)+2`. Since `chi(O_D)=-4`,

    L=O_P1(-6).

## 4. Direct conormal calculation and the exact kernel net

Use the six quadrics

    q01=Y0Y2-Y1^2,          q02=Y0Y3-Y1Y2,
    q03=Y0Y4-Y1Y3,          q12=Y1Y3-Y2^2,
    q13=Y1Y4-Y2Y3,          q23=Y2Y4-Y3^2.

They form a basis of `H0(I_c(2))`. On `U=1`, put `t=V/U` and
introduce normal coordinates in the `Y0=1` chart:

    a=Y2-t^2,              b=Y3-t^3,          e=Y4-t^4.

Modulo `I_c^2`, the first three quadrics have independent normal
classes `a`, `b-t a`, and `e-t b`. The other classes satisfy

    q12=t q02-t^2 q01,
    q13=t q03-t^3 q01,
    q23=t^2 q03-t^3 q02.

Any homomorphism `I_c/I_c^2 -> O_P1(-6)`, after twisting by
`O_P4(2)|c=O_P1(8)`, sends the six quadrics to global sections of
`O_P1(2)`. Write the first three images on this chart as degree-at-most-two
polynomials. The displayed relations and the same degree bound on the
last three force the first images to have the form

    f01=A,                 f02=B+A t,         f03=C+B t+A t^2.

For completeness, if these first images have coefficient lists
`(a0,a1,a2)`, `(b0,b1,b2)`, and `(c0,c1,c2)`, the three degree bounds
give `a1=a2=b2=0`, `b1=c2=a0`, and `c1=b0`. Thus there are exactly
the three free constants `A=a0`, `B=b0`, and `C=c0`.

Homogenizing gives all six quotient images:

| Quadric | Image in `H0(O_P1(2))` |
| --- | --- |
| `q01` | `A U^2` |
| `q02` | `B U^2+A U V` |
| `q03` | `C U^2+B U V+A V^2` |
| `q12` | `B U V` |
| `q13` | `C U V+B V^2` |
| `q23` | `C V^2` |

These formulas define global maps: on the two standard charts they
satisfy the normal relations, and their quadratic homogenizations
give the correct transition for the twisted target. The three maps
obtained from the unit coordinate triples give an isomorphism

    I_c/I_c^2 = O_P1(-6)^3.

Indeed the image matrix on the local conormal basis
`(q01,q02,q03)` is triangular with unit diagonal on `U!=0`;
on `V!=0`, use `(q23,q13,q03)` in the reversed order. This also
provides a direct proof of the required conormal splitting.
Every nonzero direction `[A:B:C]` defines an everywhere-surjective
quotient to `O_P1(-6)`.

For `q_d=sum d_ij q_ij`, the kernel is exactly

    A d01+B d02+C d03=0,
    A d02+B(d03+d12)+C d13=0,
    A d03+B d13+C d23=0.

The coefficient matrix has rank three at every nonzero direction:
triangular minors are `A^3`, `B^3`, or `C^3` according to the first
nonzero coordinate. Thus `H0(I_D(2))` is this three-dimensional net.
For the actual complete intersection `D`, its three defining quadrics
span the net. Merely specifying an arbitrary direction does not yet
show that its net cuts out a curve; the discriminant in section 5
detects exactly the failure.

## 5. Direction orbits and the cubic-base-locus obstruction

The projective direction space has two `PGL2` orbits, distinguished by

    Delta=B^2-A C.

This uses the symmetric binary quadratic with coefficients
`A,2B,C`; writing `A,B,C` as the three ordinary polynomial
coefficients would give the wrong discriminant.

Here is a direct coordinate check. On `U=1`, the quotient sends the
normal coordinate classes to

    a -> A,       b -> B+2A t,       e -> C+2B t+3A t^2.

The parameter translation `t'=t+h` induces the ambient transformation

    Y_i'=sum_(j=0)^i binomial(i,j) h^(i-j) Y_j.

Its action on the direction is

    A'=A,       B'=B+h A,       C'=C+2h B+h^2 A.

It preserves `Delta`. Parameter reversal swaps `A` and `C`;
parameter scaling acts projectively as

    [A:B:C] -> [A:lambda B:lambda^2 C].

These generate the parameter automorphism action and preserve the
zero/nonzero status of `Delta`. More explicitly, let `T` be the parameter
matrix acting on the column `(U,V)`, so the translation just used has
`T=[[1,0],[h,1]]`. The symmetric matrix `M=[[A,B],[B,C]]` transforms
as `M -> T M T^t` for this triangular generator, for parameter scaling
`T=diag(1,lambda)`, and for reversal, up to a common scalar.
Thus this is the usual projective action on symmetric binary
quadratics. Over the algebraically closed
field, rank-one quadratics form the single conic orbit `Delta=0`,
represented by `[1:0:0]`; nonsingular binary quadratics form the single
open orbit `Delta!=0`, represented by `[0:1:0]`.

At `[1:0:0]`, the net is

    <q12,q13,q23>.

Its common zero is the cone over the twisted cubic in the coordinate
`P3` with coordinates `Y1,Y2,Y3,Y4`, with vertex `[1:0:0:0:0]`.
The three equations are the two-by-two minors of

    [ Y1  Y2  Y3 ]
    [ Y2  Y3  Y4 ].

This is an integral cubic surface. Consequently every pair of net
quadrics contains this surface. Such a pair cannot define an integral
degree-four surface: an integral surface containing the cubic surface
of the same dimension would coincide with it as a reduced scheme,
contradicting the degree of an integral `(2,2)` complete intersection.
Parameter transformations carry this obstruction to every `Delta=0`
direction.

At `[0:1:0]`, the net is

    <q01,q03-q12,q23>.

In the `Y0=1` normal coordinates above, its equations successively give

    a=0,              e=2t b,              b^2=0.

Thus its chart ring is `k[t,b]/(b^2)`. The `Y4=1` chart is analogous.
There is no projective point of the common zero with `Y0=Y4=0`:
the first and last equations give `Y1=Y3=0`, and the middle then
gives `Y2=0`. The net therefore has dimension-one common zero with
support exactly `c`; it is a `(2,2,2)` complete-intersection ribbon.
All `Delta!=0` directions have the same property under parameter
automorphisms. Hence the cubic surface base-locus failure occurs
exactly on `Delta=0`.

This direction normalization moves the ambient projection center.
It does not justify replacing the fixed center `[0:0:1:0:0]` by itself
after a general `PGL2` change. Any derivative or full-fiber test for
the fixed projection must retain the transformed center or remain
in the original coordinates. No projection exclusion is claimed here.

## 6. Audit boundaries and evidence

The local lemma, local `A1/A3` identities, genus calculation, conormal
map, and net equations are direct proofs and calculations above.
The independent local auditor checked the associated-prime argument,
the ordinary-versus-symbolic-square distinction, every conormal
relation, and the rank-three matrix including boundary directions.
The same auditor independently accepted the exact direction transformations,
the two discriminant orbits, the cubic surface obstruction, and the
open-orbit complete-intersection chart calculation. Its single convention
correction was applied: with the active parameter matrix acting on the
column `(U,V)`, the symmetric direction matrix transforms as `T M T^t`.
No external classification table, numerical sample, or unrestricted
Gröbner search is used as a premise.

The exact global divisor identity and smooth reduced lift are essential
inputs. The audit does not substitute a strict transform for the
embedded smooth curve, or a support-only inverse image for a Cartier
double divisor. No non-ribbon countershield survives the stated
normal-surface/Cartier-divisor hypotheses.


### Archived exact certificate: `research/computations/derive_session_rnc_ribbon_net_2026_10_09.py`

Original source preserved verbatim, including its limitations and external dependencies.

<details><summary>Historical source</summary>

```python
"""Exact actual-coordinate conormal, ribbon-net, and derivative-map checks.

The companion proof note establishes the geometric antecedents and
completeness. This source contains no generated input or parameter search.
It checks identities over QQ and keeps the omitted middle coordinate fixed.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s

started=time.monotonic();here=Path(__file__).resolve()
Y=s.symbols('Y0:5');Y0,Y1,Y2,Y3,Y4=Y
t,U,V,W,a,lam,u,v=s.symbols('t U V W a lam u v')
quadrics=[Y0*Y2-Y1**2,Y0*Y3-Y1*Y2,Y0*Y4-Y1*Y3,
          Y1*Y3-Y2**2,Y1*Y4-Y2*Y3,Y2*Y4-Y3**2]
names=['q01','q02','q03','q12','q13','q23']
monomials=[Y[i]*Y[j] for i in range(5) for j in range(i,5)]
restriction=[m.subs(dict(zip(Y,[1,t,t**2,t**3,t**4]))) for m in monomials]
assert len(monomials)==15
assert s.Matrix([[f.coeff(t,j) for f in restriction] for j in range(9)]).rank()==9
assert s.Matrix([[s.Poly(q,*Y).coeff_monomial(m) for q in quadrics] for m in monomials]).rank()==6
assert all(s.expand(q.subs(dict(zip(Y,[1,t,t**2,t**3,t**4]))))==0 for q in quadrics)

# Balanced affine conormal generators, and their opposite-chart transition.
coordinates=[1,t,t**2+U,t**3+2*t*U+V,t**4+3*t**2*U+2*t*V+W]
sub=dict(zip(Y,coordinates));zero={U:0,V:0,W:0}
first=s.Matrix([[s.diff(q.subs(sub),(n)).subs(zero) for q in quadrics] for n in (U,V,W)])
expected=s.Matrix([[1,t,t**2,0,0,0],[0,1,t,t,t**2,0],[0,0,1,0,t,t**2]])
assert first==expected
op_t=coordinates[3]/coordinates[4]
op_U=coordinates[2]/coordinates[4]-op_t**2
op_raw_V=coordinates[1]/coordinates[4]-op_t**3
op_raw_W=coordinates[0]/coordinates[4]-op_t**4
op_V=op_raw_V-2*op_t*op_U
op_W=op_raw_W-3*op_t**2*op_U-2*op_t*op_V
transition=s.Matrix([[s.cancel(s.diff(e,n).subs(zero)) for n in (U,V,W)]
                     for e in (op_U,op_V,op_W)])
reverse=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
assert transition==t**-6*reverse

# The complete degree-two ideal is symmetric 3-by-3 matrices.
c=s.symbols('c0:6')
matrix=s.Matrix([[c[0],c[1],c[2]],[c[1],c[2]+c[3],c[4]],[c[2],c[4],c[5]]])
assert all(s.expand(e)==0 for e in first*s.Matrix(c)-matrix*s.Matrix([1,t,t**2]))
def Q(M):
    coeff=[M[0,0],M[0,1],M[0,2],M[1,1]-M[0,2],M[1,2],M[2,2]]
    return s.expand(sum(co*q for co,q in zip(coeff,quadrics)))
assert s.expand(Q(matrix)-sum(co*q for co,q in zip(c,quadrics)))==0

# Actual PGL2 generators preserve the matrix interpretation by congruence.
translated=[sum(s.binomial(i,j)*a**(i-j)*Y[j] for j in range(i+1)) for i in range(5)]
B=s.Matrix([[1,0,0],[a,1,0],[a*a,2*a,1]])
assert s.expand(Q(matrix).subs(dict(zip(Y,translated)),simultaneous=True)-Q(B.T*matrix*B))==0
scaled=[lam**i*Y[i] for i in range(5)];scale=s.diag(1,lam,lam**2)
assert s.expand(Q(matrix).subs(dict(zip(Y,scaled)),simultaneous=True)-lam**2*Q(scale.T*matrix*scale))==0
assert s.expand(Q(matrix).subs(dict(zip(Y,reversed(Y))),simultaneous=True)-Q(reverse*matrix*reverse))==0

# Net eta=(1,u,v): the three symmetric matrices with fixed kernel eta.
eta=s.Matrix([1,u,v]);left=s.Matrix([u,-1,0]);right=s.Matrix([v,0,-1])
net=[left*left.T,left*right.T+right*left.T,right*right.T]
assert all(M*eta==s.zeros(3,1) for M in net)
assert s.Matrix([[M[i,j] for M in net] for i,j in [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]]).rank()==3
net_forms=[Q(M) for M in net]
derivatives=[s.expand(s.diff(q,Y2).subs(dict(zip(Y,[1,t,t**2,t**3,t**4])))) for q in net_forms]
expected_derivatives=[(u-t)*(u+2*t),(2*u+t)*(v-t*t),(v-t*t)**2]
assert all(s.expand(g-h)==0 for g,h in zip(derivatives,expected_derivatives))
center=[s.Poly(q,Y2).coeff_monomial(Y2**2) for q in net_forms]
assert center==[-1,-u,-v]

# Standard admissible net eta=(0,1,0): local complete intersection ribbon.
standard=[quadrics[0],quadrics[2]-quadrics[3],quadrics[5]]
eps=s.symbols('eps')
ribbon_chart=dict(zip(Y,[1,t,t**2,t**3+eps,t**4+2*t*eps]))
assert [s.expand(q.subs(ribbon_chart)) for q in standard]==[0,0,-eps**2]
assert [s.expand(q.subs(dict(zip(Y,[0,Y1,Y2,Y3,0])))) for q in standard]==[-Y1**2,Y2**2-2*Y1*Y3,-Y3**2]
standard_derivatives=[s.expand(s.diff(q,Y2).subs(dict(zip(Y,[1,t,t**2,t**3,t**4])))) for q in standard]
assert standard_derivatives==[1,2*t*t,t**4]
assert standard_derivatives[1]**2-4*standard_derivatives[0]*standard_derivatives[2]==0

# Singular intrinsic quotient eta=(1,0,0) has every gradient zero at t=0.
singular_net=[quadrics[3],quadrics[4],quadrics[5]]
assert all(all(s.diff(q,y).subs(dict(zip(Y,[1,0,0,0,0])))==0 for y in Y) for q in singular_net)

# Exact degree-map controls, including the extra basepoint conic.
g0,g1,g2=expected_derivatives
y=(t+2*u)/(v-t*t);x=(u-t)*(u+2*t)/(v-t*t)**2
deck=-(v+2*u*t)/(t+2*u)
assert s.cancel(y.subs(t,deck)-y)==0
deck_difference=-9*u*(t*t+4*t*u+v)*(u*t*t+v*t+u*v)/((t*t-v)**2*(4*u*u-v)**2)
assert s.cancel(x.subs(t,deck)-x-deck_difference)==0
assert s.factor(y.subs(v,4*u*u))==-1/(t-2*u)
assert s.expand((g0*g2+2*g1*g1).subs(u,0))==0
base_gcd=s.gcd(s.gcd(g0.subs(v,u*u/4),g1.subs(v,u*u/4)),g2.subs(v,u*u/4))
assert s.Poly(base_gcd,t,domain=s.QQ.frac_field(u)).monic().as_expr()==t+u/2

record={
 'status':'PASS exact conormal, complete ribbon-net, and derivative-map identities',
 'source_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),
 'quadrics':dict(zip(names,map(str,quadrics))),
 'normal_frame':'Y0=1,Y1=t,Y2=t²+U,Y3=t³+2tU+V,Y4=t⁴+3t²U+2tV+W',
 'opposite_conormal_transition':'(U_infinity,V_infinity,W_infinity)=t^(−6)(W,V,U) modulo square ideal',
 'firstnormal_matrix':[[str(e) for e in row] for row in first.tolist()],
 'symmetric_matrix':[[str(e) for e in row] for row in matrix.tolist()],
 'ribbon_net':'M_Q eta=0; eta∈P²; intrinsic Veronese conic eta1²=eta0 eta2 excluded',
 'net_eta_1_u_v_forms':list(map(str,net_forms)),
 'derivative_eta_1_u_v_affine':list(map(str,expected_derivatives)),
 'center_functional_eta_1_u_v':center,
 'derivative_map_classification':{
    'double_conic':'eta1=0 or eta0=eta2=0, with intrinsic conic excluded',
    'birational_cubic_with_one_simple_basepoint':'eta1²=4eta0 eta2 and eta1!=0',
    'birational_quartic':'all other admissible eta',
    'chart_coverage':'eta0!=0 uses eta=(1,u,v); reversal handles eta2!=0; eta=(0,1,0) separately checked'},
 'deck_difference':str(deck_difference),
 'scope':'Identities support complete geometric ribbon classification in companion proof note. No all-mate exclusion or classification of admissible projection pencils is inferred from the derivative-map identities.',
 'elapsed_seconds':round(time.monotonic()-started,3)}
out=here.parents[1]/'scratch/session-rnc-ribbon-net-2026-10-09.json'
out.write_text(json.dumps(record,indent=2,default=str)+'\n')
print(json.dumps(record,indent=2,default=str),flush=True)
```
</details>
