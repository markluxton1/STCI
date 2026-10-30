# Historical mathematical investigations

Complete source text preserved below, including explicit hypotheses, calculations, counterexamples and unresolved issues. Compilation is not independent correctness audit or theorem promotion.

---

## Source: 2026-10-14-generalization-cartier-lift-minimal-degree.md

# Every Cartier rational singleton lift lies on a minimal-degree normalization

Date: 2026-10-14. Owner: `global_structure`. Status: **NEW WRITTEN
THEOREM; independent review requested**. This extends the already
reviewed [smooth-normalization theorem](2026-10-13-generalization-global-carrier-framework.md)
by a new proof of the extra singular-normalization scope. It does not
rerun or recheck the earlier theorem.

## 1. Exact theorem

Work over an algebraically closed field of characteristic zero. Let
`C subset P3` be a smooth rational curve of degree `d`, and let
`X subset P3` be an integral degree-`a` hypersurface with a mate for
`C`. Let `nu:S->X` be its finite normalization, `H=nu*O_X(1)`.
Assume the full reduced inverse image is one curve `c`, that
`nu|c:c->C` is an isomorphism, and that **c is Cartier on S**.

Then the complete system `|c|` identifies `S` with a normal surface
of minimal degree. With `n=c^2=d^2/a`, the possibilities are:

| Pair `(S,c)` | Integral hyperplane pullback | Carrier degree |
|---|---|---|
| `P2`, a line | `H=d h` | `a=d^2` |
| `P2`, a smooth conic; `d` even | `H=(d/2)h` | `a=d^2/4` |
| Smooth rational normal scroll of degree `n>=2`, hyperplane section; `n|d` | `H=(d/n)c` | `a=d^2/n` |
| Rational-normal cone of degree `n>=2`, smooth Cartier hyperplane section; `n|d` | `H=(d/n)c` | `a=d^2/n` |

The conclusion is about the normalization and its polarization. It
does not assert that every four-coordinate projection of these models
has a mate. Full support and entire conductor descent remain required.

## 2. Why Cartierness gives enough smoothness

At a point `P in c`, take a local defining nonzerodivisor `f` in the
normal surface ring `R=O_S,P`. The quotient `R/(f)=O_c,P` is regular
of dimension one because `c` is smooth. A generator of its maximal
ideal, lifted to `R`, together with `f` generates the maximal ideal
of `R` by Nakayama. Thus `embdim(R)<=2=dim(R)`, and `R` is regular.
Consequently `S` is smooth along all of `c`; its finitely many possible
singularities lie away from `c`.

The mate gives `m c~bH` with `md=ab`. Since `c` is Cartier,
`O(c)` is ample: a positive power is the ample `O(bH)`. Its square
is the positive integer `n=d^2/a`.

Resolve the isolated singularities by `sigma:M->S`, an isomorphism
near `c`. The strict transform `c_M` equals the Cartier pullback,
is smooth rational, and has square `n`. The pullback `L=sigma*H`
is nef and big, and `m c_M~bL`. Adjunction gives

    K_M.c_M=-n-2,    K_M.L=(m/b)(-n-2)<0.

Hence no positive multiple of `K_M` can be effective. The same
characteristic-zero surface-classification input as in the accepted
carrier work makes `M` rational or birationally ruled over a
positive-genus curve. In the latter case the ruling extends to `M`,
and the rational `c_M` is a fiber component, so has square at most
zero. This contradicts `n>0`. Thus `M` is rational.

Normality gives `sigma*O_M=O_S`. The Leray edge map injects
`H1(S,O_S)` into `H1(M,O_M)=0`, so `H1(S,O_S)=0`. No rational-
singularity hypothesis was assumed here; the eventual minimal-degree
classification will impose the actual singularity type.

## 3. The complete linear system and cone polarization

The sequence

    0 -> O_S -> O_S(c) -> O_P1(n) -> 0

gives `h0(O_S(c))=n+2` and surjective restriction. The canonical
section generates away from `c`, and restriction generates on `c`.
Therefore `|c|` is basepointfree. Since `c` is ample, its morphism
to `P^(n+1)` is finite. The nondegenerate image `Y` has

    n=deg(phi) deg(Y),    deg(Y)>=n.

Thus it is a finite birational map to a minimal-degree surface.
The [Del Pezzo--Bertini classification](https://arxiv.org/html/math/0404517v5)
gives normal `Y`, so finite birationality makes `S~Y`. The new
singular possibility is the cone over a rational normal curve; the
plane and Veronese surface remain smooth.

The smooth entries have the integral polarization already derived in
the earlier theorem. For a cone of degree `n`, its minimal resolution
is `F_n`, with exceptional section `E^2=-n` and ruling `f`. The
pullback of the Cartier hyperplane is

    L_c=E+n f.

Pullback injects `Pic(S)` into `Pic(F_n)`: pushing a trivial pulled-
back line bundle down and using `sigma*O_M=O_S` proves injectivity.
Any pulled-back Cartier line bundle has zero degree on the contracted
`E`, so its class `xE+yf` satisfies `y=nx`. It is therefore an
integer multiple of `L_c`. Since `c` itself is Cartier, this proves
`Pic(S)=Z[c]` and `H=(d/n)c` with `n|d`.

For `n=1` the cone is simply `P2` and belongs to the plane entry.
No additional singular minimal-degree surface is missing in dimension
two. The theorem is now proved with every displayed hypothesis retained.

## 4. Fixed C0 and a new non-Cartier boundary

For the literal degree-four `C0`, the accepted all-quartic theorem
removes the `a=4` entries. Every remaining carrier under the theorem's
support and degree-one assumptions has one of exactly three pairs:

    a=8,  S=P1 x P1, c=(1,1), H=(2,2);
    a=8,  S=quadric cone, c=Cartier conic, H=2c;
    a=16, S=P2, c=line, H=4h.

This classifies the entire **Cartier-lift lane**, including singular
normalizations and unibranch thick carriers satisfying the explicit
support assumptions. All have a primitive degree-one normalized
section `Q`, with divisor `2c` or `4c`; all normalized mates are
scalar powers of it.

In particular, every generically regular carrier of fixed C0 whose
degree is neither 8 nor 16 must have a non-Cartier point of its lift
on the normalization if it admits a mate. This is stronger than the
smooth-normalization statement and applies to all carrier degrees.
It does not classify the non-Cartier singularities or bound their
indices. For fixed C0 the index condition remains
`a divides 16 t` for any Cartier multiple `tc`.

Normal hypersurface carriers are even more restricted in this lane.
If `X=S` were a normal carrier satisfying the theorem, its minimal-
degree normalization would have `H^1(O_X)=0` and `p_g(X)=0`, whereas
a degree-8 or degree-16 hypersurface has
`p_g=(a-1)(a-2)(a-3)/6>0`. Equivalently, its canonical class
`(a-4)H` has positive degree on `c`, contradicting the smooth-locus
adjunction value `-n-2`. Thus a normal carrier of fixed C0 with a
mate cannot have Cartier lift at any degree; its lift must meet a
genuine non-Cartier singularity. This is conditional on the fixed-C0
premises and the actual mate, not an all-normal-carrier exclusion.

The missing global possibilities remain non-Cartier lifts, several
inverse-image primes, or finite inverse curves of degree greater than
one. The three projection targets still require full conductor descent.


---

## Source: 2026-10-14-generalization-first-relation-pole-budget-independent-audit.md

# Independent review of the constant-relation pole budget

Date: 2026-10-14, America/New_York. Reviewer: root.
Status: **PROVED under the explicit hypotheses below**. This reviews new
Section 6 of [the thick extension](2026-10-13-generalization-thick-equality-extension.md).
The previously accepted quadratic transition and apolar annihilator
classification are inputs; their calculations were not repeated.

## 1. Hypotheses and verdict

Work in characteristic zero on fixed
`C0=[s^4:s^3t:st^3:t^4]`, with `N_C0=O(7)^2`. Let `Q` be an actual
embedded ideal defining a thickening, and write

```
K_j = ker(Sym^j N_C0^* -> gr_j(O_Y)).
```

Suppose the first generic relation has degree `r`, its generic direction
is a constant nonzero binary form `f`, and there is no independent
relation in degree `r+1`. Suppose its actual line sheaf is

```
K_r = O(-7r) f(-D),  D effective, delta=deg D.
```

The conclusion is correct: the section cutting out `D` annihilates the
accepted primitive-triple obstruction `h_m` for **each** linear factor
`m` of `f`. This retains the multiplicity of every factor and the full
special-point divisor; it does not discard poles or claim the generic
direction is constant in other cases.

## 2. Saturation is the crucial step

The generic degree-`r+1` relation space is `f V`, where `V=k^2`.
The constant subbundle `O(-7(r+1)) tensor f V` has a locally free
quotient in the ambient symmetric conormal bundle. Composing the
inclusion of `K_(r+1)` with that quotient gives a generically zero
map from a vector bundle to a vector bundle on an integral smooth
curve. It is zero everywhere. Therefore every actual next-order
relation lies in the saturated constant span `f V`, even where
`K_(r+1)` has a modified lattice.

It is consequently legitimate to test a lifted degree-`r` generator
in the quotient `W=Sym^(r+1)V/f V`. No assertion that the actual
relation lattice equals its saturation is needed.

## 3. The obstruction has the stated twist

Choose local normal coordinates and a local generator `h` of the
divisor ideal of `D`. A lift of the initial relation `h f` changes in
next normal order by `h D_ambient(f)`. Differentiating `h` under
motion of the support coordinate contributes a multiple of `f` times
a linear normal coordinate. Changing the scalar gluing unit has the
same form. Both contributions vanish in `W`. Local next-order
corrections change the resulting cocycle by a coboundary.

The correction bundle is intrinsically

```
Hom(K_r, O(-7(r+1)) tensor W) = O(D-7) tensor W.
```

Thus the necessary obstruction is the image of the quadratic ambient
transition class under multiplication by the global section of
`O(D)` cutting out `D`, in `H^1(O(D-7)) tensor W`. This explains the
positive divisor twist, rather than merely assigning it by analogy
with the linear case. On `P1`, this is `H^1(O(delta-7)) tensor W`.

## 4. Factor extraction and consequences

Write `f=m^t H(m,ell)` with `H(0,1)!=0`. The coefficient functional
extracting `m^(t-1) ell^(r+2-t)` vanishes on `f V`, so it defines a
constant map from `W` to `k`. The Leibniz rule sends the obstruction
to

```
t H(0,1) D h_m.
```

Both scalar factors are nonzero in characteristic zero. An actual
embedded lift therefore requires `D h_m=0` for every factor `m`.

The imported apolar classification gives the following necessary
conditions uniformly in `r`:

- `delta<=1` is impossible.
- At `delta=2`, `f` is a power of one pure endpoint direction and
  `D` is its doubled endpoint.
- At `delta=3`, `f` is still a power of one direction. A mixed
  `m=U+theta V` requires exactly `D=div(st(t+2theta s))`;
  an endpoint requires its doubled endpoint plus one point.
- If `f` has two distinct factors, `delta>=4`.

These use the established facts that a mixed direction has no
annihilator below degree three and a unique degree-three annihilator,
while the endpoints require divisibility by their respective squared
coordinates. Distinct mixed directions have distinct degree-three
divisors, and a mixed degree-three divisor has only simple endpoint
zeros. A divisor annihilating both endpoints has degree at least four.
No accepted rank calculation was rerun.

This theorem is necessary structure. It does not assert existence
of any remaining power relation, control higher obstructions, handle
moving binary directions, or exclude positive-defect STCI
presentations. In positive characteristic the factor multiplicity
`t` can vanish, so the argument is not transferred there.


---

## Source: 2026-10-14-generalization-localcoh-pencil-independent-review.md

# Independent review of the observable corank-one pencil theorem

Date: 2026-10-14. Reviewer: root. Status: **PROVED under the stated exact
rank hypotheses**. This reviews the new abstract theorem in
[the polynomial-dual note](generalization-localcoh-dual-lemma.md), not
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


---

## Source: 2026-10-14-generalization-moving-relation-gap-cost-independent-audit.md

# Independent audit: movement and saturation of the first normal relation

Date: 2026-10-14. Reviewer: root. Status: **PROVED** under the stated
balanced-normal and generic relation-rank hypotheses. This reviews new
Section 7 of [the thick extension](2026-10-13-generalization-thick-equality-extension.md).
It does not replay a previously accepted statement or computation.

Let `N_C=H tensor k^2` on a smooth integral projective curve, and let
the unique first generic initial relation have degree r. Write its
saturated line bundle and actual relation line as

```
W=H^-r tensor A^-1,    K_r=W(-D).
```

Here A is the pullback of `O(1)` by the projective binary-relation
direction map, so it is globally generated. Put `epsilon=deg A>=0`
and `delta=deg D>=0`. Let s>r be the next independent generic
relation degree. For every r<=j<s, the generic relation space is
the first relation times all normal forms of degree j-r.

Multiplication by a nonzero binary form on every fiber is injective.
Consequently

```
A_j=W tensor Sym^(j-r)N_C^*
```

injects into `Sym^j N_C^*` with constant fiber rank and locally free
cokernel. Its image is saturated. Since its generic span equals
that of K_j, it is exactly the saturation of K_j. Products of actual
degree-r relations give the other inclusion, hence

```
A_j(-D) subset K_j subset A_j.
```

Set `t_j=length(A_j/K_j)`. On a curve the inclusions give

```
0<=t_j<=(j-r+1)delta,   t_r=delta.
```

Since `rank A_j=j-r+1` and its degree is
`-(j-r+1)(j deg H+epsilon)`, the exact kernel/quotient degree formula
gives

```
Delta_j=(j-r+1)epsilon+t_j.
```

This retains the torsion of the actual normal-layer quotient. Summing
these identities, and using nonnegativity of the other layer defects,
proves

```
Delta >= epsilon(s-r)(s-r+1)/2 + delta.
```

For C0 the accepted exact socle budget therefore gives

```
n mu >= 7 Asym+epsilon(s-r)(s-r+1)+2delta.
```

No generic Gorenstein associated graded hypothesis is needed for this
inequality. A moving direction has epsilon>=1; a constant direction
has epsilon=0. On the constant branch, the separately accepted pole
constraints apply when s>=r+2. If s=r+1, the next independent relation
can absorb the quadratic obstruction; no such pole lower bound is
claimed there. This qualification was requested during review.

Thus movement pays a quadratic cost in the gap before the next
independent relation, while saturation pays its effective-divisor
cost. These are necessary global compatibility constraints and do not
bound all carrier degrees or all possible Loewy indices. The separate
moving-base differential operator in the owner note is a new exact
reduction with its own evidence; it is not used in this proof.


---

## Source: 2026-10-14-generalization-normal-carrier-torsion-filter.md

# All-degree torsion filter for normal carriers of fixed C0

Date: 2026-10-14. Owner: `global_structure`. Status: **NEW DIRECT
COROLLARY OF ACCEPTED PREMISES; independent review requested**.
No earlier verifier or proof was rerun.

## 1. Exact divisor-class criterion

Let `X subset P3` be a normal integral surface of degree `a` containing
the fixed smooth rational quartic `C0`, over an algebraically closed
field of characteristic zero. Let `H=O_X(1)` and let `c` be the
smooth Weil prime `C0` on `X`. Put

    h=gcd(a,4),    u=a/h,    v=4/h,
    Delta=u c-v H in Cl(X).

If a degree-`b` mate exists, its Cartier divisor is `m c` and
intersection with `H` gives `4m=ab`. Hence `m=u k,b=v k` and

    k Delta=0.

Conversely, if `Delta` is torsion of order `t`, its class relation
`t u c~t v H` supplies a global section of `O_X(tv)` with divisor
exactly `tu c`. Normality means no conductor descent remains. The
hypersurface restriction sequence lifts this section to an ambient
form of degree `tv`, giving a mate. Every normalized mate section is
unique up to scalar at its degree, because its specified divisor is
fixed and `X` is proper integral.

Therefore the complete normal-carrier criterion is:

    a mate exists iff Delta is torsion;
    if it does, its minimum mate degree is b_min=t*4/gcd(a,4).  (1)

This statement uses normality, not smoothness or Cartierness of `c`.
It covers arbitrary singularities and arbitrary carrier degree.

## 2. The accepted low-degree theorem forces nonzero torsion

The accepted fixed-C0 plane/quadric/cubic/quartic exclusions prohibit
any ambient mate of degree at most four, regardless of the other
carrier degree. If `Delta=0`, the converse construction above gives
a mate of degree `v`, which is one, two, or four. This is impossible.

Consequently every surviving normal carrier with a mate has

    Delta nonzero torsion,   t*v>=5.                         (2)

In particular **every normal carrier with torsion-free `Cl(X)` is
excluded for fixed C0 in every mate degree and every carrier degree**.
More generally, any normal carrier whose torsion subgroup does not
contain the required nonzero class order is excluded.

The congruence cases are:

| Carrier degree | `v` | Necessary class order and smallest possible mate degree |
|---|---:|---|
| `a` odd | 4 | `t>=2`, `b_min>=8` |
| `a=2 mod 4` | 2 | `t>=3`, `b_min>=6` |
| `a=0 mod 4` | 1 | `t>=5`, `b_min>=5` |

These are exact necessary class-order restrictions, not a theorem
that the indicated classes occur or that their divisor is the fixed
embedded curve.

## 3. Resolution formulation and a coverage warning

For a smooth projective resolution `M->X`, the class group can be
computed as the Picard group modulo the classes of exceptional primes.
The relevant torsion is therefore controlled by nonprimitive embeddings
of the exceptional lattice and, where present, Picard torsion.
Knowing that `Pic(M)` is torsion-free does not by itself show that
`Cl(X)` is torsion-free: a quotient by a nonprimitive exceptional
subgroup can acquire torsion. One must use the actual saturated
exceptional lattice, not silently discard this quotient torsion.

The accepted quartic/quintic lattice arguments already preserve this
distinction in their respective finite ADE types. The present result
does not classify exceptional lattices at arbitrary carrier degree.
It proves an all-degree exclusion for the torsion-free class-group
lane and leaves the required nonzero torsion classes as an explicit
global obstruction to be studied.

The Cartier-lift classification gives a different all-degree boundary:
a smooth rational degree-`d>=3` curve with a mate on a normal carrier
must be non-Cartier somewhere. The present torsion filter additionally
requires the particular primitive degree-zero divisor class `Delta`
to be nonzero torsion for fixed C0. Neither condition supplies a
uniform bound on all normal carriers.
