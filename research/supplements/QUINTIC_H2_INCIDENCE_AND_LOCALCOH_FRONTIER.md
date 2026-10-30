# Historical mathematical investigations

Complete source text is retained below, including original mathematical calculations, conditional arguments, failed approaches, counterexamples and open questions. This preservation does not independently certify the mathematical claims.

---

## Source: 2026-10-29-quintic-h2-degree-five-incidence-reduction.md

# Quintic h=2: degree-five support-incidence reduction (research checkpoint)

Status: **candidate exclusion; exact resultant identities require a standalone reproducible rerun before promotion to a proved result.** This is an investigation note, not a new authoritative result record.

## Scope

This concerns the *necessary restricted-conductor support incidence* in the characteristic-zero genus-one A4 quintic projection analysis, **not** a proof about the original rational-quartic STCI question. Work on the finite monic exact-gcd-two chart with parameters `delta,a,B,G,j,v,w`, quadratic `H=x^2+vx+w`, primitive source conductor `F_src=H Q`, and the source note's open conditions `delta E Delta1 != 0`. Do not invert the discriminant of H or the inverse-map denominator globally. Coordinate conventions matter: use the actual source-coordinate conductor, not the older shifted coefficient array.

Primary background: [conductor quotient](2026-10-14-generalization-quintic-h2-conductor-quotient.md) and [global monic ODE incidence](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md).

## Degree-five branch

On `j=0`, the leading coefficient of Q vanishes and the ODE support condition takes the form

```
H Q' = (5x+u) Q,   deg Q=5.
```

The conormal cubics have the same leading coefficient G. Their difference is

```
J_c-P = T*x^2 + U*x + V,
T=3G+4*delta^2, U=6B-delta-delta^2, V=a-B.
```

Since `E=G*T !=0`, the common monic quadratic must be

```
H=(J_c-P)/T,   v=U/T, w=V/T.
```

Put `L=6B+delta^2-3delta`, `M=3a-3B+2delta`, `N=L*T-G*U`. Divisibility of the first cubic by H is equivalent to

```
F0=-2*a*T^2-(a-B)*N=0,
F1=M*T^2-G*(a-B)*T-U*N=0.
```

Writing `A=2*T^2+N`, `C=3*T^2-G*T`, these give

```
a=B*N/A,
Phi=B*C*N + A*(-3*B*T^2+2*delta*T^2+G*B*T-U*N)=0.
```

The exceptional `A=0` case is excluded on the declared open set: `F0` forces `B=0`, and elimination of G from the remaining equations yields `576*delta^10*(delta+1)^2`; at `delta=-1` the common zero forces `T=0`. This calculation should be included in the reproducible rerun.

## Local conductor simplification

The candidate exact source-conductor coefficient identity on `j=0` is

```
[x]F_src = -2*G*(G+3*delta^2)^2*(G+delta^2+2*B).
```

It is a unit on the prescribed open set, while `F_src(0)=0`. Assuming these identities, the conductor has a simple zero at zero. Since every root of Q is a root of H by the ODE, a simple root of `H*Q` at zero must come from H but not Q. Thus `w=0`; the two cubic constant-term equations force `a=B=0`.

Then `H=x(x+v)`, `v != 0`, and the degree-five ODE forces

```
Q=q5*(x+v)^5.
```

The remaining common-factor equation becomes

```
R=9*G^2+2*G*delta^3+22*G*delta^2-4*G*delta
  +2*delta^5+12*delta^4-6*delta^3=0,
v=-delta*(delta+1)/(3*G+4*delta^2).
```

## Candidate exact exclusion

Using the saved quotient coefficient convention `Q=sum(q_i*x^i)`, the power condition requires

```
q4=5*v*q5,  q3=10*v^2*q5.
```

A prior exact-arithmetic calculation reported, after specializing `j=a=B=w=0`, clearing denominators, and eliminating G against R,

```
Res_G(R,q4-5*v*q5) = -12*delta^14*(delta+1)^2*f(delta)
Res_G(R,q3-10*v^2*q5) = 24*delta^16*(delta+1)^4*g(delta)
```

up to the explicitly chosen denominator-clearing convention, where

```
f=80*delta^8+1632*delta^7-25031*delta^6-51424*delta^5
  +358707*delta^4+288462*delta^3-103104*delta^2
  -294336*delta+34560

g=384*delta^8-8112*delta^7+7080*delta^6+254915*delta^5
  -1326324*delta^4-270648*delta^3+514152*delta^2
  +988956*delta-112320
```

and `gcd(f,g)=1`. Since `delta !=0` and `v !=0` excludes `delta=-1`, **these identities would exclude the entire degree-five branch**. The result is not promoted until the source expressions, coefficient ordering, denominator clearing and polynomial gcd are independently rerun from a single executable script.

## Next work

1. Reproduce the candidate exclusion directly from the saved exact source conductor and quotient coefficients, with a small exact-arithmetic script and clear assumptions.
2. If verified, promote a short theorem with the script as reusable calculation; do not preserve ordinary calculation mistakes or audit chronology.
3. Then analyze the remaining `j != 0`, degree-six branch. The degree-five result alone does not establish emptiness of the global h=2 incidence.

Repository design: this note is an **investigation dossier checkpoint**. General conductor-annihilation and support lemmas belong in their reusable theorem homes; this note links them and keeps the specialized reduction together.


---

## Source: generalization-localcoh-dual-lemma.md

# Polynomial duals, observable affine pencils, and parameter strata

Date: 2026-10-14. Author: the `dual_general_theorem` research agent.

**PROVED here:** the abstract algebra statements below. They do not prove
the global STCI assertion and do not assert the indicated rank hypotheses
for an entire repository parameter family. They provide a structural
replacement for repeatedly computing full polynomial left kernels.

The accepted actual-tensor and affine-lift interpretations are taken as
given. No accepted verifier was rerun to derive these statements.

## 1. The complete degree-two theorem

Let `K` be any field, let `lambda` be an indeterminate, and consider

```text
L(lambda) = [ lambda I_q + A ]       u = [ v ]
            [       B      ]           [ w ]
```

with constant matrices/vectors over `K`. Suppose

```text
rank B = q-1,    rank [B; B A] = q.
```

Then the following are equivalent:

1. `u` is outside `im L(lambda0)` for every `lambda0` in an algebraic
   closure of `K`.
2. There is a polynomial vector `n(lambda)` with
   `n^T L = 0` and `n^T u = 1`.
3. There is such a vector of degree at most **two** in `lambda`.

Thus the coefficient system obtained by writing
`n=n0+lambda*n1+lambda^2*n2` is a **complete decision procedure**, rather
than merely a sufficient search, on this observable corank-one locus.
The bound is independent of `q`, the degree of `K` over its prime field,
and the degrees of any additional parameters used to describe `A,B,u`.

### Proof and an explicit smaller obstruction system

If `w` is outside `im B`, a constant row annihilating `B` and nonzero on
`w` gives a degree-zero normalized dual. Otherwise choose `c` with `Bc=w`.
Let `h` span `ker B` and put `a=Ah`. The two rank hypotheses say exactly
that `h,a` are linearly independent. Every possible solution of the
bottom equations is `b=c+t h`, and the top equations become

```text
t (a+lambda h) = p-lambda c,    p=v-Ac.
```

The vector `a+lambda h` is nonzero at every geometric `lambda`. Therefore
incidence is equivalent to the vanishing of its wedge with
`p-lambda c`. This gives `q(q-1)/2` quadratic equations, but most are
redundant.

Change the constant state basis so `h=e1` and `a=e2`. Choose `c` in the
constant complement of `Kh`, so `c1=0`. In these coordinates the complete
incidence system is

```text
ell_j(lambda) = p_j-lambda*c_j = 0       (j=3,...,q),
g(lambda) = p_1-lambda*p_2+lambda^2*c_2 = 0.
```

There are only `q-2` linear polynomials and **one** quadratic polynomial.
They have no common geometric root if and only if their gcd in
`K[lambda]` is one.

To retain a dual certificate, choose a constant matrix `D` with
`D B=diag(0,1,...,1)` and `Dw=c`; such a `D` exists because `B` induces
an isomorphism from the chosen complement of `Kh` to `im B`. For any
polynomial row `t` satisfying `t(a+lambda h)=0`, the row

```text
n_t^T = [ t , -t(lambda I_q+A)D ]
```

annihilates `L` and evaluates on `u` as `t(p-lambda c)`.
Taking `t=e_j^T` for `j>=3` gives degree-at-most-one duals evaluating to
`ell_j`. Taking `t=e1^T-lambda*e2^T` gives a degree-at-most-two dual
evaluating to `g`.

The ideal of the linear polynomials is either zero, the unit ideal, or
generated by a single monic linear polynomial `ell=lambda-alpha`.

* If the ideal is the unit ideal, a constant linear combination of its
  generators equals one. The corresponding dual has degree at most one.
* If it is zero, full exclusion requires `g` to be a nonzero constant.
  Scaling its dual gives a normalized dual of degree at most two.
* Otherwise exclusion means `g(alpha)!=0`, and the explicit identity

  ```text
  1 = g(lambda)/g(alpha)
      - ((g(lambda)-g(alpha))/(lambda-alpha))/g(alpha) * ell(lambda)
  ```

  uses a constant coefficient on `g` and a coefficient of degree at most
  one on `ell`. The resulting dual again has degree at most two.

The converse follows immediately from specializing the two dual
identities. This proves all three equivalences.

The bound is sharp. For `q=2`, take

```text
A = [0,0;1,0],   B=[0,1],   u=(1,0,0)^T.
```

Then `L=[lambda,0;1,lambda;0,1]`, its polynomial left kernel is
`K[lambda]*(1,-lambda,lambda^2)^T`, and evaluation on `u` forces the
multiplier of a normalized dual to be one. Hence every normalized dual
has degree exactly two.

For the repository pencil with `q=18`, the reduction is to at most
**sixteen linear polynomials and one quadratic**, replacing either 153
wedge quadratics or a full kernel calculation. This numerical application
requires an exact rank certificate for the specific field/stratum used;
sampled ranks in a family do not establish its exceptional parameter
loci.

## 2. Full slope rank and observability

If an affine pencil `L0+lambda*L1` has constant slope `L1` of full column
rank `q`, a constant invertible change of output coordinates takes it to
the displayed form `[lambda I_q+A;B]`. The target changes by the same
output transformation.

Put

```text
O = [ B ; BA ; ... ; BA^(q-1) ].
```

**PROVED:** `L(lambda0)` has column rank `q` for every geometric `lambda0`
if and only if `O` has column rank `q`.

Indeed `N=ker O` is the largest `A`-invariant subspace contained in
`ker B`; invariance follows from Cayley-Hamilton. If `N!=0`, after
extending to an algebraic closure it contains an eigenvector of `A`,
which gives a rank drop of `L` at the negative eigenvalue. Conversely a
rank-drop vector of `L(lambda0)` is an eigenvector of `A` annihilated by
`B`, hence belongs to `N`. This is the elementary observability
criterion; it provides a structural description of the rank-drop
boundary.

If `O` has full rank, choose a constant left inverse `T` of `O`. Define

```text
E_j(lambda) = sum_(i=0)^(j-1) (-lambda)^i BA^(j-1-i),
S_j(lambda) = [ E_j(lambda), (-lambda)^j I ],
```

including `E_0=0`. Stacking `S_j` for `j=0,...,q-1` gives `S L=O`, so
`Q=T S` is a polynomial left inverse of `L` of degree at most `q-1`.
Consequently

```text
P = I-LQ,      P L=0,
```

and the ideal of **all** polynomial left-dual evaluations on `u` is
exactly the ideal generated by the coordinates of `P u`.

The same construction works over a parameter ring `R0` whenever `O`
has a left inverse over `R0`. Its maximal-minor ideal being the unit
ideal guarantees such a left inverse by an adjugate/Bezout construction.
Then a single unit-ideal certificate for the entries of `P u` in
`R0[lambda]` gives a single normalized dual over the entire parameter
domain. The sharper degree-two theorem is stated over a field;
specialization of degree-two coefficient systems across a parameter ring
must not be assumed to be exact without a lifting or module certificate.

### Arbitrary corank and observation depth

The structural reduction extends beyond corank one. Suppose
`corank B=c` and `rank[B;BA]=q`. Then `N=ker B` and `A N` are disjoint:
if `Ah in N` for `h in N`, then `BAh=0`, contradicting injectivity of
`BA` on `N`. This also proves `A` is injective on `N`, so
`dim(N+A N)=2c` and `2c<=q`. In a state basis sending a basis of
`N` to the first `c` coordinate vectors and their `A`-images to the next
`c`, a bottom-compatible target reduces to

```text
q-2c linear residuals,
c quadratic residuals p_i-lambda*p_(c+i)+lambda^2*b_(c+i).
```

The associated linear duals have degree at most one, and the quadratic
duals have degree at most two, by the same construction as in section 1.
Full geometric exclusion is equivalent to the residuals having gcd one;
it yields a normalized dual of degree at most **three**. Indeed arbitrary
polynomials of degree at most two with gcd one admit a Bezout identity
whose coefficients have degree at most one. To see this over any field,
reduce the coefficient identity modulo one residual of maximal degree;
all coefficients can be reduced to degree below that maximal degree,
and the remaining quotient coefficient has the same bound.

This degree-three bound is sharp for `c=2`, including in positive
characteristic. Take `q=4`, `A=[0,0;I_2,0]` in two-by-two block notation,
`B=[0,I_2]`, and `u=(0,1,0,-1,1,1)^T`. The two kernel generators are

```text
n1=(1,0,-lambda,0,lambda^2,0),
n2=(0,1,0,-lambda,0,lambda^2),
```

evaluating to `g1=lambda^2` and `g2=lambda^2+lambda+1`. The identity
`lambda*g1+(1-lambda)*g2=1` gives a degree-three dual. A dual of degree
at most two would have constant multipliers of `n1,n2`, because their
last coordinates are `lambda^2` times the respective multipliers. No
constant combination of `g1,g2` is one.

More generally, if the truncated observation matrix
`O_ell=[B;BA;...;BA^(ell-1)]` has full column rank, the construction above
uses `Q` of degree at most `ell-1` and `P` of degree at most `ell`.
If full geometric exclusion holds, the coordinates of `P u` have gcd
one and admit Bezout coefficients of degree at most `ell-1`. Hence a
normalized dual of degree at most `2ell-1` exists. This bounds search
degree by **observation depth**, rather than by a growing ambient
ancestor degree. Corank one at observation depth two has the sharper,
optimal bound two proved in section 1.

The general bound `2ell-1` is sharp for every `ell>=1`. Take two
independent nilpotent state chains of length `ell`, let `A` shift each
chain forward, and let `B` read their two terminal coordinates. The
observation depth is `ell`, and the two polynomial left-kernel
generators have chain coordinates
`(1,-lambda,...,(-lambda)^(ell-1))` and separate bottom coordinates
`(-lambda)^ell`. A constant target can give their evaluations
`f1=lambda^ell` and `f2=1+lambda`. Every normalization
`a*f1+b*f2=1` forces

```text
b = 1-lambda+...+(-lambda)^(ell-1) modulo lambda^ell.
```

Thus `degree b>=ell-1`; its separate bottom coordinate forces normalized
dual degree at least `2ell-1`. The displayed truncated geometric series
achieves the bound. This sharpness argument works over every field.

### Affine lift scope and projective infinity

All the field theorems above concern every **affine** `lambda`. For a
homogenized pencil `t L0+s L1` and a fixed target `u`, the projective
point `t=0` must also be tested. With the full-slope normalization its
column span is `[I_q;0]`, so infinity is excluded exactly when the
transformed bottom target `w` is nonzero. This is a separate condition;
affine exclusion alone does not imply it. When the repository affine
lift was normalized by a nonzero pure-top coefficient, the associated
top-zero ancestor stratum also retains its original geometric scope.

## 3. Corank-one rank-drop boundary

The observable hypothesis has a precise failure mode. If `rank B=q-1`
but `Ah=alpha*h`, then

```text
(lambda I_q+A)h=(lambda+alpha)h.
```

As before, a bottom target outside `im B` immediately gives a constant
normalized dual. In the compatible case the following classification is
complete.

Choose `h=e1` and a bottom lift with `c1=0`. Put `p=v-Ac`. For
`lambda!=-alpha`, consistency is equivalent to

```text
p_j-lambda*c_j=0       (j=2,...,q).
```

At the sole rank-drop point `lambda=-alpha`, consistency additionally
requires `p1=0`. This is an exact field decision rule. In particular,
full-fiber exclusion may hold when the linear residuals have the common
root `-alpha` and `p1!=0`, even though no normalized polynomial dual
exists. Therefore a failed polynomial-dual search on a rank-drop locus
does not establish incidence.

More precisely, the entire polynomial left-dual evaluation ideal is
`J_u=(p_j-lambda*c_j : j=2,...,q)`: annihilation of the first state
direction forces `(lambda+alpha)t1=0`, hence `t1=0` over `K[lambda]`.
Full exclusion occurs exactly in one of two cases: `J_u=(1)`, which has
a normalized dual of degree at most one; or `J_u=(lambda+alpha)` and
`p1!=0`, which has no normalized polynomial dual. If `J_u=0` there is
incidence away from `-alpha`, while a different common linear root
produces incidence at that root.

## 4. Evaluation ideals over parameter rings

Let `R` be a Noetherian commutative ring, `L:R^q->R^m`, and `u in R^m`.
Define

```text
S = ker(L^T),     J_u = { n^T u : n in S }.
```

This image is an ideal. Then `J_u=R` if and only if one normalized dual
exists, because the sum of finitely many syzygies is again a syzygy.
Kernel and evaluation commute with localization. Thus a dual exists over
`R[1/d]` exactly when `d^N in J_u` for some `N`.

If `coker L` is projective, dual formation commutes with specialization.
For a reduced finite-type algebra over an algebraically closed field,
constant fiber rank of `L` is enough to ensure this hypothesis. On this
locus, pointwise exclusion everywhere is equivalent to `J_u=R`.

Without this hypothesis the converse fails. Even a pencil with full
slope rank gives a counterexample:

```text
L = [ lambda, 0 ; 0, lambda ; 0, 1 ],    u=(1,0,1)^T.
```

Its fibers are inconsistent for every `lambda`, but every polynomial
left dual is a multiple of `(0,1,-lambda)` and its evaluations on `u`
generate `(lambda)`. The specialized left kernel at the rank-drop point
is larger than the specialized module of polynomial left syzygies.

## 5. Exact determinantal fallback, with no rank assumptions

Let `R` be a finite-type algebra over an algebraically closed field.
Write `I_r(M)` for its `r`-minor ideal, with `I_0(M)=R`, and let
`C=[L|u]`. Full pointwise exclusion is equivalent to either of the
following conditions for every `0<=r<=min(m,q)`:

```text
I_r(L) subset radical(I_(r+1)(C)),
( I_(r+1)(C) : I_r(L)^infinity ) = R.
```

The consistency locus of rank `r` is precisely

```text
V(I_(r+1)(C)) \ V(I_r(L)).
```

On this set the ranks of `C` and `L` are both `r`, so the target is in the
column span; conversely every consistency point has this form. The
Nullstellensatz and finite generation of ideals prove the stated
equivalences. A finite certificate can give, for each `r`, an exponent
`N_r` and explicit containment
`I_r(L)^N_r subset I_(r+1)(C)`.

Equivalently, after extending the coefficient field to an algebraic
closure, full exclusion is equivalent to the unit ideal generated by
the entries of `L b-u` in the polynomial ring including the unknown
column coefficients `b`. This single Nullstellensatz certificate remains
complete even where rank jumps. Its multipliers may involve `b`; that
extra dependence is what a constant normalized dual cannot detect.

## 6. Combining exception factors without rootwise splitting

If `f(k)` is square-free over a characteristic-zero field and all source
denominators are units modulo `f`, calculations can be made over the
finite reduced algebra `K[k]/(f)`. Exact rank hypotheses need to hold in
every factor, rather than merely in one numerical embedding.

If a degree-at-most-two normalized dual is available modulo every
pairwise-coprime factor `f_i` of `f`, the Chinese remainder theorem gives
one degree-at-most-two dual modulo `f`. Coefficientwise CRT proves the
same identities modulo the whole polynomial. No root embeddings and no
accepted-verifier reruns are needed for this consolidation.

Alternatively the smaller linear/quadratic obstruction system can be
built directly over the quotient algebra. Any inversion used in choosing
bases or performing gcd steps must be certified as a unit modulo all of
`f`. A nonunit pivot is a reason to split the algebra by gcd/idempotents
or use the determinantal fallback; treating it as invertible would omit
geometric parameter points.

The recommended next structural work is to certify the exact locus of
`rank B=q-1` and `rank[B;BA]=q`, derive the linear/quadratic obstruction
system there, and use the corank-one boundary rule or the determinantal
fallback on its complement. This replaces repeated ancestor-family
kernel calculations with a reusable theorem, while retaining every
exceptional stratum.


---

## Source: quintic-h2-degree-five-exclusion.md

# Quintic h2: exclusion of the degree-five support-incidence branch

**Result (characteristic zero, necessary incidence only).** On the global monic h2 parameter domain delta*E*Delta1 != 0, the j=0 (degree-five conductor quotient) branch satisfying the conormal common-quadratic, conductor-divisibility, and support ODE equations has no points.

**Proof.** For j=0, the actual primitive source conductor has zero constant coefficient and linear coefficient
`-2*G*(G+3*delta^2)^2*(G+delta^2+2*B)`, a unit on the prescribed open. Write Fsrc=H*Q and H*Q'=(5*x+u)*Q. All roots of Q are roots of H. The simple conductor zero at x=0 therefore forces H(0)=0 and Q(0) nonzero. The two conormal constant equations imply w=a=B=0. Thus H=x*(x+v), v nonzero, and Q=q5*(x+v)^5.

The remaining common-factor equation is
```
R=9*G^2+2*G*delta^3+22*G*delta^2-4*G*delta
  +2*delta^5+12*delta^4-6*delta^3=0,
v=-delta*(delta+1)/(3*G+4*delta^2).
```
The ODE implies q4=5*v*q5 and q3=10*v^2*q5. Set T=3*G+4*delta^2, P=T*(q4-5*v*q5), S=T^2*(q3-10*v^2*q5), using the quotient coefficients from the actual primitive conductor after a=B=j=0. Exact QQ elimination gives
```
Res_G(R,P)=6*delta^13*(delta+1)^2*f(delta)
Res_G(R,S)=-9*delta^15*(delta+1)^4*g(delta)
f=40*delta^5-323*delta^4-2018*delta^3-288*delta^2-600*delta+156
g=128*delta^7+4720*delta^6+600*delta^5-58408*delta^4
  +124123*delta^3+2484*delta^2+44376*delta-11016
gcd(f,g)=1.
```
Since delta != 0 and v != 0 implies delta != -1, the resultants cannot vanish simultaneously. QED.

**Exact source-based verifier:** [verify_quintic_h2_degree_five.py](../computations/verify_quintic_h2_degree_five.py). **Global hypotheses:** [monic incidence](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md). **Working reduction:** [degree-five dossier](quintic-h2-degree-five-support-incidence-working-dossier.md).

**Limit:** This excludes the j=0 branch only. The j != 0, degree-six branch is unresolved. The necessary incidence is not equivalent to STCI existence. The argument does not invert the discriminant of H or inverse-map denominators.


---

## Source: quintic-h2-degree-five-support-incidence-working-dossier.md

# Quintic h2: degree-five support-incidence reduction (working dossier)

**Status:** mathematical reduction with a **provisional computational exclusion**; not a promoted theorem. Characteristic zero. This note records the current argument and the exact verification still required, not a history of attempts.

## Question and scope

For the quintic h2 projection/mate investigation, determine whether the *necessary* common-conormal-quadratic, conductor-divisibility, and conductor-support ODE incidence has points. Even a point of this incidence would **not** by itself produce a projection or an STCI: inverse fibers, center avoidance, and nonlinear conductor descent remain additional conditions.

The global, denominator-free formulation and its hypotheses are in [the monic ODE incidence note](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md). This dossier treats the **degree-five branch** `j=0`; the degree-six branch `j != 0` remains open. Keep the global open `delta * E * Delta1 != 0`; do not invert the discriminant of H or inverse-map denominators.

## Exact common-factor reduction for j=0

In source coordinate `x=r/delta`, the conormal cubics are

```text
P  = G*x^3 + (6*B+delta^2-3*delta)*x^2
     + (3*a-3*B+2*delta)*x - 2*a
Jc = G*x^3 + (6*B+3*G+5*delta^2-3*delta)*x^2
     + (3*a+3*B+delta-delta^2)*x - a-B.
```

Set
```text
T=3*G+4*delta^2,
U=6*B-delta-delta^2,
V=a-B,
L=6*B+delta^2-3*delta,
M=3*a-3*B+2*delta,
N=L*T-G*U.
```
On `j=0`, the cofactor determinant is `E=G*T`, so `G,T` are units. Since `Jc-P=T*x^2+U*x+V`, the common monic quadratic must be
```text
H=x^2+v*x+w,  v=U/T,  w=V/T.
```
Divisibility of both cubics is equivalent to the two remainder equations
```text
F0=-2*a*T^2 - V*N = 0,
F1=M*T^2 - G*V*T - U*N = 0.
```
Put `A=2*T^2+N` and `C=3*T^2-G*T`. Then `F0=-A*a+B*N` and `F1=C*a-3*B*T^2+2*delta*T^2+G*B*T-U*N`. Where `A` is invertible,
```text
a=B*N/A,
Phi=B*C*N + A*(-3*B*T^2+2*delta*T^2+G*B*T-U*N)=0.
```
The admissible open specializes to
```text
delta*G*T*(G+3*delta^2)*(G+delta^2+2*B) != 0.
```
The claim that `A` is a unit on this locus follows by examining `A=0`: `F0` forces `B=0`, and the resultant of the remaining equations restricts `delta` to `0,-1`; `delta=0` is excluded and the `delta=-1` solution forces `T=0`. This argument should be encoded in a small exact symbolic test before promotion.

## Conductor/ODE restriction and provisional exclusion

Write the actual primitive source conductor as `Fsrc=H*Q`. On the degree-five branch, `Q` has degree five, and the support ODE is
```text
H*Q'=(5*x+u)*Q.
```
On the admissible `j=0` open, the source-conductor linear coefficient was calculated as
```text
[x]Fsrc = -2*G*(G+3*delta^2)^2*(G+delta^2+2*B),
```
which is a unit. Since `Fsrc(0)=0` is a simple zero and all roots of `Q` lie among roots of `H`, the zero cannot come from `Q`; hence `w=0` and `Q(0) != 0`. The two cubic constant remainders give `a=B=0`. Then `H=x*(x+v)`, with `v != 0`, and the ODE forces `Q=q5*(x+v)^5`. Thus
```text
q4=5*v*q5,  q3=10*v^2*q5.
```
With `a=B=j=w=0`, the remaining conormal equation is
```text
R=9*G^2+2*G*delta^3+22*G*delta^2-4*G*delta
  +2*delta^5+12*delta^4-6*delta^3=0,
v=-delta*(delta+1)/(3*G+4*delta^2).
```
A previous exact-symbolic computation of the two quotient-coefficient resultants reported (up to nonzero constants/denominator clearing) factors `delta^14*(delta+1)^2*f(delta)` and `delta^16*(delta+1)^4*g(delta)`, where
```text
f=80*delta^8+1632*delta^7-25031*delta^6-51424*delta^5
  +358707*delta^4+288462*delta^3-103104*delta^2
  -294336*delta+34560
g=384*delta^8-8112*delta^7+7080*delta^6+254915*delta^5
  -1326324*delta^4-270648*delta^3+514152*delta^2
  +988956*delta-112320
```
and `gcd(f,g)=1`. Because `delta != 0` and `v != 0` excludes `delta=-1`, these identities **would** prove the degree-five incidence empty.

**Verification boundary:** the exact source quotient-coefficient expressions, denominator-clearing factors, and both resultant identities have **not been independently replayed in this dossier**. Do not cite the exclusion as an established result or remove the degree-five branch from authoritative global systems until that replay succeeds. In particular, verify the claimed conductor linear coefficient from the original octic and confirm that the saved `q_i` index convention matches `Q=sum(q_i*x^i)`.

## Next work

1. Build a compact exact-arithmetic script that loads the authoritative conductor/quotient input, specializes `j=a=B=w=0`, and checks the two resultant identities and `gcd(f,g)=1`.
2. If verified, promote a concise degree-five exclusion theorem with its exact domain and link to the script.
3. Only then investigate the degree-six branch `j != 0`; retain discriminant-zero and inverse-map boundary cases.

This is an investigation dossier, not an audit log. Ordinary correction history is intentionally omitted.


---

## Source: quintic-h2-research-next-steps.md

# Quintic h2: research status and next steps

## Current result

The characteristic-zero degree-five (j=0) branch of the necessary common-conormal-quadratic/conductor-support incidence has been excluded. See [proof](quintic-h2-degree-five-exclusion.md) and [exact verifier](../computations/verify_quintic_h2_degree_five.py). This is not an STCI nonexistence theorem. The degree-six (j != 0) branch remains unresolved. The global model, including the discriminant-zero and inverse-map boundaries, is [here](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md).

## Recommended continuation, when research resumes

1. **Degree-six local test.** Compute the primitive conductor's vanishing order at x=0 on j != 0. Test whether conductor divisibility and H*Q'=(6*x+u)*Q constrain H as sharply as in degree five. Do not assume the degree-five pure-power form.
2. **If the local test reduces parameters**, carry out exact elimination using the authoritative primitive conductor and the smallest necessary coefficient comparisons; retain all required open conditions and repeated-root cases.
3. **If it does not**, study the support geometry and symmetric-power/spectral constraints before attempting large saturation computations. Set a computational stopping criterion.
4. **After degree six**, assess whether the obstruction mechanism extends to higher projection degrees. If it is confined to the quintic configuration, prioritize the global degree-growth problem (freedom versus constraints, residual curves allowed) instead of overinvesting in one projection lane.

## Repository handling

This is a forward-looking investigation agenda, not a promoted result. Preserve mathematical reductions, hypotheses, boundary cases, exact computational inputs and useful failed approaches; do not preserve ordinary error histories or check logs. Keep the h2 investigation coherent and link reusable conductor theory rather than duplicating it. No changes to the main branch.
