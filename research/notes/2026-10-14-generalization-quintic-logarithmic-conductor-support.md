# Logarithmic conductor support as one homogeneous representation equation

Date: 2026-10-14. **Coordinate-binding correction:** the attempt02/04
coefficient capture below used p->1-z while the h2 source and actual
octic parameters are reciprocal. Its exact algebraic output is retained
as a failed geometric bridge and must not be used as the actual h2
incidence. The [corrected capture](2026-10-14-generalization-quintic-h2-coordinate-correction-and-sextic-incidence.md)
now uses z^8 F(1/z) and has passed literal transformation checks.
The general support/eigenvector proof is unaffected.

Status: **PROVED STRUCTURAL LEMMA, with [independent review](2026-10-14-generalization-quintic-logarithmic-support-independent-audit.md)**. This continues the existing quintic lane without
splitting workers by root partitions. Accepted conductor forms, gcd
covers and previously closed quintic charts are premises. No inherited
certificate is replayed. The new lemma is valid in arbitrary degree;
its quadratic specialization supplies one equation for the remaining
degree-two allowed support, including repeated roots and infinity.

## 1. A power-free support criterion

Let k be algebraically closed of characteristic zero. Let F,H be nonzero
homogeneous binary forms of degrees n>=1 and h>=1. Then

```
supp(div F) subset supp(div H)
  iff F divides H partial_s F and F divides H partial_t F.       (1)
```

This uses projective support and retains the entire divisor of F. At a
root P of F of multiplicity m, a local derivation transverse to P lowers
that multiplicity to m-1, because m is nonzero in characteristic zero.
The two homogeneous coordinate derivatives span that transverse
direction locally. Thus divisibility in (1) forces H(P)=0. Conversely,
if H vanishes at every root, its at least one unit of root valuation
repairs the at most one unit lost by either derivative. This proves both
divisibilities at every linear prime. Unique factorization proves (1).
The argument includes the point at infinity and does not assume F or H
squarefree. In characteristic p the implication can fail at a root whose
multiplicity is divisible by p; no unrestricted positive-characteristic
version is used here.

Equivalently, there are homogeneous forms L_s,L_t of degree h-1 with

```
H partial_s F=L_s F,  H partial_t F=L_t F,
s L_s+t L_t=n H.                                             (2)
```

The last identity is Euler's identity. Thus an arbitrary large power
divisibility or a root-partition enumeration can be replaced by one
finite logarithmic linear system. For h=1, (2) gives the single-root
criterion directly. The forms H and F must remain nonzero; the zero
form is a separate original geometric stratum.

There is an even more economical equivalent condition. Put
`D_H=H_t partial_s-H_s partial_t`, for arbitrary h>=1. Then

```
supp(div F) subset supp(div H) iff F divides D_H F.            (2a)
```

For h>=2 this is `D_H F=L F`, with L homogeneous of degree h-2;
for h=1 it means `D_H F=0`. Indeed, on x=t/s write
H=s^h h(x), F=s^n f(x). The operator becomes
`n h'(x)f(x)-h h(x)f'(x)`. At a root of f not vanishing on h,
the last term has order exactly m-1 and the first at least m.
The degree h and the multiplicity m are nonzero scalars in
characteristic zero. At a root on h both terms have order at
least m. This proves (2a), including all multiplicities. Thus one
homogeneous Hamiltonian equation suffices in every allowed-support
degree.

## 2. For quadratic H, the criterion is a Lie-algebra eigenvector equation

Write H=a s^2+b st+c t^2 and define the degree-zero derivation

```
D_H=(partial_t H) partial_s-(partial_s H) partial_t.
```

It acts on the constant vector space Sym^n(k^2). The induced vector
field on P1 vanishes precisely at div H, since on x=t/s it is
`-2H(1,x) partial_x`. Then (1) is equivalent to

```
D_H F=mu F for some scalar mu in k.                           (3)
```

Indeed (3) makes div F invariant under that vector field. If a root of
F were not a zero of the vector field, its nonzero transverse derivative
would have order m-1 while mu F has order at least m, a contradiction.
Conversely, if the support lies at the zeros of the vector field, the
same valuation argument makes F divide D_H F. Both have degree n, so
their quotient is a scalar. This proof handles a double zero of H and
all multiplicity distributions of F at once.

For any coefficient vector f of F, (3) says exactly

```
rank[ f | D_H f ]<=1.                                       (4)
```

All two-by-two minors of this (n+1)-by-two matrix are one homogeneous
scheme of necessary and sufficient support conditions on the nonzero
F,H locus. No coefficient of F or H is inverted, so this formulation
keeps leading drops and roots at infinity. It is an assertion about
support, not about the full nonreduced conductor or descent.

The operator on the standard two-dimensional representation is

```
[[b,2c],[-2a,-b]],  discriminant Delta=b^2-4ac.
```

For n=8 its characteristic polynomial is

```
mu (mu^2-4Delta)(mu^2-16Delta)(mu^2-36Delta)(mu^2-64Delta).
```

This single representation identity replaces the list of nine possible
root-multiplicity weights. When Delta=0 it remains the nilpotent
identity mu^9; the repeated-root boundary has not been removed.

## 3. A root-free test when H is not specified

The projective stabilizer of a nonzero degree-n binary form F has
positive-dimensional Lie algebra if and only if F has at most two
distinct projective roots. A nonzero projective vector field preserving
its finite root set must vanish at each root and has at most two zeros.
Conversely, a vector field vanishing at the one or two prescribed points
makes F an eigenvector by Section 2. Thus, in characteristic zero,

```
F has at most two distinct roots
 iff rank[ F | s partial_sF-t partial_tF |
                    s partial_tF | t partial_sF ]<=3.        (5)
```

The displayed four columns represent F and a basis of sl2 acting on F.
The first column is nonzero, so a linear dependence supplies a nonzero
Lie-algebra element, not merely a zero multiple of F. This is a
determinantal condition in the original coefficients, with no root
adjoining. It can be used as a preliminary geometric obstruction;
when an allowed quadratic H is already fixed, (4) retains the stronger
requirement that the roots occur at its actual support.

## 4. Application and precise unfinished quintic obligation

In the accepted nonendpoint genus-one A4 quintic model, the actual
binary conductor form has degree eight. Full support requires its roots
to lie in the actual permitted inverse-C0 support, with the intrinsic A4
contribution kept exactly as in the original conductor theorem. Wherever
the remaining permitted form is the homogeneous gcd H of degree two,
the entire support requirement is (3) or (4), after using the actual
coefficient map. If an additional permitted point is present on an
exceptional chart, multiply it into H and use (1)--(2) instead. No
exceptional permitted point is silently discarded to force h=2.

The finite monic quadratic cover used in the new computation only
parameterizes quadratics avoiding its infinity point. Its determinant,
denominators, nonzero conductor condition and all content factors are
recorded. That calculation is an exact coefficient/incidence capture,
not a global quintic exclusion. In particular a leading coefficient
cannot be divided out on the claim that an infinity chart has already
been handled; its precise previously accepted coverage must be cited.

The current next step is to insert the actual octic coefficient map
into the homogeneous eigenvector incidence and prove incompatibility
with the full-support/projection conditions, or exhibit the remaining
geometric family and test its full conductor. The nonlinear logarithmic
conductor defect still has to vanish for any proposed mate. A support
identity alone does not solve descent, and no assertion that the whole
quintic lane is closed is made.

### One incidence keeps the intrinsic A4 allowance as well

Let j be the actual Jbar scalar and let P be the fixed nonzero
linear form of the intrinsic A4 point. The accepted condition is
support(F) contained in support(H) when j!=0 and in support(HP)
when j=0. It is equivalent to the simultaneous equations

```
D_(HP) F=L_1 F,          deg L_1=1,
j D_H F=mu F,           mu a scalar,                        (6)
```

for quadratic H and octic F. When j!=0 the second equation forces
support in H and the first is automatic. When j=0, nonzero F
forces mu=0 and only the first equation remains, allowing exactly
HP. Thus the entire A4 allowance is retained by one polynomial
incidence, rather than splitting work by j=0 or root partitions.
F,H,P must stay nonzero, and all projection/cofactor conditions apply.

For the monic H=z^2+vz+w chart, if F=sum_(i=0)^8 c_i z^i,
the Hamiltonian image has coefficients

```
d_i=(8-2i)v c_i+(18-2i)c_(i-1)-2(i+1)w c_(i+1),
c_(-1)=c_9=0.                                             (7)
```

The [completed coefficient capture](../validation/2026-10-14-quintic-logarithmic-support/attempt-04/execution-record.json)
stores an exact 9-by-two matrix (c,d) for the supplied, incorrectly
coordinate-bound substitution, with exit zero and empty stderr.
It is not an actual h2 geometric certificate. The rational-map calculation
in attempt02 produced all nine coefficients before a later ring-
coercion error; those saved coefficients were reused instead of
reconstructed. Attempt03's sequence/list setup failure is retained
separately. This is new incidence data, not a proof that its rank
locus is empty.

The accepted finite quadratic cover solves four linear equations
for the two cofactor pairs, with determinant
`(v^2-4w)(v^2+2w+6vw+6w^2)`. The stored rational map is valid only
off this determinant. To retain the repeated-root locus without
splitting cases, use those four linear equations in (6) instead
of their rational inverse. Retain projective coefficients of H
to include infinity. Equation (6) itself needs neither inverse.

This is one shared structural problem. It deliberately avoids creating
separate research tasks for the multiplicity partitions of an octic on
two points.
