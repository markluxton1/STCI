# cyclic cover and moving linear rigidity

Permanent subject dossier retaining full mathematical computations, counterexamples, proofs, precise hypotheses and unresolved scope. Computational implementations, where present, remain separate.

---

## 2026-10-14-cyclic-cover-local-smooth-curve

# Local torsion order, cyclic-cover splitting, and ramification along a smooth curve

Date: 2026-10-14. Author: `cyclic_cover_structure/local_torsion_curve`.

Status: **PROVED HERE**, with an independent audit of the explicit families in
[2026-10-14-cyclic-cover-D4-counterexample-audit.md](2026-10-14-cyclic-cover-D4-counterexample-audit.md).
These are local results. They do not give a projective mate for `C0` or resolve
the universal STCI question.

The accepted repository results were used as premises. This note studies a
new proposed bridge: whether the local Cartier index of a smooth curve can be
read from ramification of its cyclic class cover. The answer is **no**, even
on a cyclic quotient hypersurface. There is instead an exact formula involving
a fractional intersection invariant and a separate splitting number.

## 1. Setup and the exact local formula

Let `k` be algebraically closed of characteristic zero. Let `(R,m)` be a
complete normal two-dimensional local `k`-algebra, excellent and with residue
field `k`. Let `P` be a height-one prime such that

\[
  R/P\simeq k[[t]].
\]

Write `C=V(P)`. Assume that `[C]` has exact finite order `r` in `Cl(R)`. Thus
there is `f` in `R` with

\[
  \operatorname{div}_R(f)=rC.
\]

Choose `a` in `R` with `v_C(a)=1`, and put

\[
  D=\operatorname{div}(a)-C,\qquad h=a^r/f.
\]

Then `D` is effective and has no `C` component. Normality gives `h` in `R`,
and `h` does not lie in `P`, since

\[
  \operatorname{div}(h)=rD.
\]

Define

\[
  m_C=\operatorname{ord}_t(h\bmod P),\qquad
  \lambda_C=\frac{m_C}{r}\pmod{\mathbf Z}\in\mathbf Q/\mathbf Z.
\]

The choice of `a` exists: a uniformizer of the DVR `R_P` can be written
`a/b` with `a,b` in `R` and `b` not in `P`. Its numerator has valuation one.

**Theorem 1.** Let `S` be the normalization of `R` in

\[
  L=\operatorname{Frac}(R)(T),\qquad T^r=f.
\]

The cyclic class cover `Spec S -> Spec R` has degree `r`, is connected and
local, and is étale away from the closed point. Its reduced inverse image
`C^#` is the effective Cartier divisor `T=0`. It is finite flat of degree `r`
over `C`. The normalization of `C^#` has exactly

\[
  \boxed{b=\gcd(r,m_C)}
\]

branches. Each branch maps to `C` with ramification index

\[
  \boxed{e=\frac{r}{\gcd(r,m_C)}=\operatorname{ord}(\lambda_C)}.
\]

In particular,

\[
  r=be,
\]

and `e=r` holds precisely when `gcd(r,m_C)=1`. The equality `e=r` is an
additional local primitivity condition, not a consequence of smoothness of
`C`, normality of the surface, or the hypersurface hypothesis.

The invariant `lambda_C` is independent of the choices of `a` and `f`.
Equivalently, it is the local rational intersection

\[
  (D\cdot C)\pmod{\mathbf Z},
\]

where `D` is the effective representative of `-[C]` constructed above, and
`r(D.C)` means the order of the Cartier equation `h` on the smooth curve.
This convention avoids the sign ambiguity of calling it a self-linking
number. Its denominator, which is the ramification index, is independent
of that sign.

### Proof

If `f` were a `p`-th power in `Frac(R)` for a prime `p` dividing `r`, its
root would have divisor `(r/p)C`, contradicting exact order `r`. Since the
fraction field contains all roots of unity, Kummer theory shows that
`T^r-f` is irreducible. Thus `[L:Frac(R)]=r`, and `S` is a domain with a
cyclic group of order `r`.

Normalization is finite by excellence. A finite algebra over a complete
local ring is a product of complete local algebras; since `S` is a domain,
it has one factor and is local. Its residue field is `k`.

At each height-one prime `Q`, a local uniformizer has valuation `v_Q(f)`
divisible by `r`. Dividing `T` by the corresponding uniformizer power gives
a root of a unit, whose equation has invertible derivative. Hence the
normalized extension is étale at `Q`. A normal two-dimensional local ring
is regular away from its closed point, and every point of the punctured
spectrum has height at most one; this proves the asserted étaleness.

The same calculation at `C` gives

\[
  \operatorname{div}_S(T)=\pi^*C,
\]

with coefficient one at every prime over `C`. A normal two-dimensional
ring is Cohen--Macaulay. Therefore `S/(T)` is Cohen--Macaulay of dimension
one; it is generically reduced by the coefficient-one calculation. These
facts make it reduced everywhere. Thus `C^#=V(T)` is exactly the reduced
inverse image of `C`.

The finite `R/P`-module `S/(T)` is torsion-free: a nonzero element of `R/P`
vanishes at no generic component of `C^#`, and the Cohen--Macaulay curve
has no embedded associated primes. It is consequently free over the DVR
`k[[t]]`. Its generic rank is `r`, because the cover is étale over the
generic point of `C`.

To calculate its generic algebra, use `a` as the uniformizer at `C` and
set `w=a/T`. Then

\[
  w^r=h.
\]

Reduction at `C` gives

\[
  (S/(T))\otimes_{k[[t]]}k((t))
  \simeq k((t))[w]/(w^r-h_C),\qquad h_C=h\bmod P.
\]

Write `h_C=t^{m_C}u(t)` with `u` a unit. Every unit of `k[[t]]` has an
`r`-th root, by coefficient recursion or Hensel lifting. Replacing `w` by
its quotient by that root reduces the equation to `w^r=t^{m_C}`.

Put `b=gcd(r,m_C)`, `e=r/b`, and `j=m_C/b`. The equation has `b` distinct
irreducible factors over `k((t))`, each of degree `e`; the normalization of
each factor is `k[[s]]` with

\[
  t=s^e,\qquad w=\xi s^j
\]

for a suitable root of unity `xi`. The coprimality `gcd(e,j)=1` proves
irreducibility and total ramification of degree `e`. This includes
`m_C=0`, for which `b=r` and `e=1`.

For independence, replace `a` by another element `a'` of valuation one.
The rational function `a'/a` is a unit of `R_P` and has residue in
`k((t))^*`. Thus the valuation of `h_C` changes by

\[
  r\operatorname{ord}_t((a'/a)\bmod P).
\]

Another generator of `rC` differs from `f` by a unit of `R`; its residue
on `C` has valuation zero. Hence `m_C mod r`, `lambda_C`, `b`, and `e`
are well defined. Finally, the usual local definition of intersection with
a `Q`-Cartier divisor gives `(D.C)=m_C/r`. ∎

## 2. A `D_n` counterexample: local order two, ramification one

For any integer `n>=4`, put

\[
  R_n=k[[x,y,z]]/(x^2+y^2z+z^{n-1}),\qquad C=(x,z).
\]

The curve is the smooth `y`-axis. The hypersurface has an isolated `D_n`
singularity and is normal. At the generic point of `C`, `y` is a unit and
the equation gives valuation two for `z` and valuation one for `x`. There
is no other prime in the support of `z`, since `R_n/(z)=k[[x,y]]/(x^2)`.
Thus

\[
  \operatorname{div}(z)=2C.
\]

The prime ideal `(x,z)` has two minimal generators, so `C` is not Cartier.
Its exact local class order is therefore `r=2`.

The class cover is

\[
  B_n=k[[u,y,t]]/(u^2+y^2+t^{2n-4}),\quad
  x=tu,\quad z=t^2.
\]

It is the normal `A_(2n-5)` hypersurface, with involution

\[
  (u,y,t)\longmapsto(-u,y,-t).
\]

Its invariant ring is `R_n`, and its only fixed point is the origin. The
inverse curve is

\[
  t=0,\qquad u^2+y^2=0.
\]

It has two smooth branches, `u=iy` and `u=-iy`. Each maps isomorphically
to `C` by the coordinate `y`. Consequently

\[
  r=2,\qquad b=2,\qquad e=1.
\]

Theorem 1 gives the same answer directly. Take `a=x` and `f=z`; then

\[
  h=x^2/z=-(y^2+z^{n-2}),\qquad m_C=2.
\]

This also disproves the stronger guess that a smooth finite-index curve
on a hypersurface surface germ forces the surface to be a cyclic quotient
singularity: `D_n` is a counterexample.

## 3. The complete `A`-type family realizes every possible ramification divisor

Fix `N>=2` and `1<=a<N`, and put

\[
  R_N=k[[x,y,z]]/(xy-z^N),\qquad
  C_a=(x-z^a,\ y-z^{N-a}).
\]

The curve is smooth, with parameter `z`. Define

\[
  g=\gcd(N,a),\quad r=N/g,\quad A=a/g.
\]

**Theorem 2.** The exact local class order of `C_a` is `r`. Its cyclic
class cover is

\[
  B_g=k[[U,V,z]]/(UV-z^g),\qquad
  x=U^r,\quad y=V^r,\quad z=z.
\]

Its inverse curve has

\[
  \boxed{b=\gcd(r,g)}
\]

normalized branches, each with ramification index

\[
  \boxed{e=r/\gcd(r,g)}.
\]

The fractional intersection invariant of Theorem 1 is

\[
  \boxed{\lambda_{C_a}=a^2/N\pmod{\mathbf Z}}.
\]

### Proof of exact order and cover identification

Write the usual cyclic quotient presentation

\[
  R_N=k[[u,v]]^{\mu_N},\quad
  x=u^N,\quad y=v^N,\quad z=uv,
\]

where `zeta` acts by `(u,v)->(zeta u,zeta^{-1}v)`. The invariant-ring
description follows directly by expressing every invariant monomial using
`u^N,v^N,uv`.

The reduced inverse image of `C_a` has equation

\[
  q=u^{N-a}-v^a.
\]

This is reduced in characteristic zero and transforms by the character
`zeta^{-a}`, of exact order `r`. Thus `q^r` is invariant and its downstairs
divisor is `rC_a`.

Conversely, if `ell C_a` were principal, pull a defining equation to the
regular local ring `k[[u,v]]`. Since the quotient map is étale away from
the origin, the pullback has the divisor of `q^ell`. Unique factorization
makes it a unit times `q^ell`. Evaluating that unit at the origin shows
that invariance is possible only when `zeta^{-a ell}=1` for every `zeta`.
Hence `N` divides `a ell`, and `r` divides `ell`. This proves exact order.

The kernel of the character `zeta^{-a}` is `mu_g`. Consequently the field
generated by `q` over `Frac(R_N)` is the `mu_g` invariant field. The
normalization is its invariant ring

\[
  k[[u,v]]^{\mu_g}
  =k[[U,V,z]]/(UV-z^g),\quad U=u^g,\quad V=v^g.
\]

This identifies the class cover without an assumed class-group table.

On this cover, the inverse curve has equation

\[
  q=U^{r-A}-V^A=0.
\]

Over the generic point of `C_a`, `V=z^g/U`, so its algebra is

\[
  k((z))[U]/(U^r-z^a).
\]

The splitting count is `gcd(r,a)`. Since `gcd(r,A)=1`, this equals
`gcd(r,g)`. Kummer normalization gives ramification `r/gcd(r,g)` on each
branch.

To compute the fractional invariant without resolving the singularity,
take the element `s=x-z^a` in place of `a` in Theorem 1. It has valuation
one along `C_a`, and in the quotient presentation

\[
  s=u^a q.
\]

For `f=q^r`, this gives

\[
  h=s^r/f=u^{ar}=x^A.
\]

Restriction to `C_a` yields

\[
  h_C=z^{aA},\qquad m_C=aA=gA^2.
\]

Thus `m_C/r=a^2/N`, and `gcd(r,m_C)=gcd(r,g)` as asserted. ∎

### Every index--ramification pair occurs

For any `r>=2` and any positive divisor `e` of `r`, put

\[
  b=r/e,\qquad N=rb,\qquad a=b.
\]

Then `g=b`, the curve has exact class order `r`, and its class cover has
`b` branches of ramification index `e`. Therefore **every pair allowed by
`e | r` is realized by a smooth curve on an `A`-type hypersurface**.

In particular, with

\[
  N=r^2,\qquad a=r,
\]

the local class order is arbitrarily large while `e=1`. The cover is the
`A_(r-1)` surface `UV=z^r`; the inverse Cartier curve is

\[
  V=U^{r-1},\qquad U^r=z^r.
\]

It is an ordinary `r`-branch plane curve singularity, and all its
normalized branches map isomorphically to `C_a`.

The smallest instance is already on `A_3`:

\[
  xy=z^4,\quad C=(x-z^2,y-z^2),\quad
  f=x+y-2z^2,\quad\operatorname{div}(f)=2C.
\]

Its class cover is `UV=z^2`, with `f=(U-V)^2`. The inverse curve consists
of `U=V=z` and `U=V=-z`, both unramified over `C`.

## 4. The gluing defect is visible in the discriminant

The preceding examples do not evade the index by making the inverse
Cartier curve smooth. They move the defect into its multiple branches and
their gluing at the closed point.

Let `A_C=S/(T)` in Theorem 1, and let `bar A_C` be its normalization.
Set

\[
  \delta=\dim_k(\bar A_C/A_C).
\]

Both rings are finite free over `k[[t]]`, with rank `r`, and their generic
algebra is étale. The trace discriminant satisfies the exact identity

\[
  \boxed{\operatorname{ord}_t\operatorname{disc}(A_C/k[[t]])
  = r-b+2\delta.}
\]

Indeed, the normalization is a product of `b` tame DVR extensions of
degree `e`; their discriminant orders sum to `b(e-1)=r-b`. Changing a
normalization basis to a basis of `A_C` multiplies the discriminant by
the square of the inclusion determinant. The valuation of that
determinant is `length_(k[[t]])(bar A_C/A_C)=delta`.

For the unramified family `N=r^2,a=r`, the inverse curve
`k[[U,z]]/(U^r-z^r)` has

\[
  b=r,\quad e=1,\quad \delta=r(r-1)/2,
\]

because its `r` smooth branches meet pairwise transversely. Its
discriminant has order `r(r-1)`, equivalently the discriminant of
`U^r-z^r` is a nonzero constant times `z^{r(r-1)}`.

Thus a future global argument may control the arithmetic genus,
discriminant, or gluing defect of the pulled-back Cartier curve. Applying
Riemann--Hurwitz only to its normalization discards the `2delta` term and
cannot bound the local Cartier index.

## 5. Consequences and failure shields for the global structural lane

- A hyperplane class is Cartier locally. Adding a multiple of it to a
  global torsion relation does not itself change local class order or
  supply a primitivity hypothesis.
- For the class cover of `[C]`, local order `r` is a cover degree;
  normalized curve ramification is `e`; branch count is `b`; these obey
  `r=be`. They are different quantities even for a smooth embedded curve.
- If a global cyclic cover of degree `M` restricts at a completed point
  to a class of exact local order `r | M`, its local algebra splits into
  `M/r` copies of the degree-`r` class cover. This follows because units
  of the complete local ring have `M`-th roots. It does not recover
  `e=r` inside each copy.
- For a multiple `q[C]`, both its local order and its curve-restriction
  Kummer character must be recomputed. A cover associated to another
  torsion class is not automatically the cover of `[C]`.
- Smoothness of `C` permits the exact one-variable Kummer formula.
  Smoothness of the normalization of its inverse curve is automatic in
  this local setting and does not make the inverse Cartier curve normal.
- The new formula is degree independent and exact. It gives a structural
  obstruction to a proposed global argument, not a negative STCI theorem.

No canonical research record or other agent's file was edited. The
independent example audit is the companion note linked at the beginning.


---

## 2026-10-14-cyclic-cover-D4-counterexample-audit

# A smooth curve of local class order two whose cyclic cover splits

Date: 2026-10-14.
Author: `duval_counterexample`; independent elementary local audit for
`local_torsion_curve` and `cyclic_cover_structure`.

Status: **NEW PROVED EXAMPLE.** This note checks a new local example only.
Previously accepted global STCI results are premises and have not been
replayed. It gives no counterexample to the global STCI conjecture.

## 1. The surface and smooth curve

Let `k` be algebraically closed of characteristic zero and choose
`i in k` with `i^2=-1`. Put

```
A = k[[x,y,z]] / (x^2 + y^3 + y z^2),
X = Spec A,
C = V(x,y).
```

This is the `D_4` surface singularity. It is a two-dimensional normal
domain: the hypersurface is Cohen--Macaulay, and its gradient vanishes
only at the closed point, so it is regular in codimension one and
normal by Serre's criterion. The equation is irreducible, for example
because `y(y^2+z^2)` has odd valuation at the prime `y` of `k[[y,z]]`
and therefore is not a square in its fraction field. The curve `C` is
smooth, since

```
A/(x,y) = k[[z]].
```

The principal divisor of `y` is

```
div_X(y) = 2 C.
```

Indeed, `A/(y)=k[[x,z]]/(x^2)` has the unique minimal prime `(x,y)`;
at the generic point of `C`, `y^2+z^2` is a unit and the relation
`x^2=-y(y^2+z^2)` gives valuation two for `y`.

The ideal `(x,y)` needs two generators at the closed point. The images
of `x` and `y` are linearly independent modulo `m(x,y)`, since the
hypersurface equation has no linear term. Thus the ideal is not
principal and `C` is not Cartier. On a local normal scheme, triviality
of a Weil divisor class is equivalent to being principal. Consequently

```
order([C] in Cl(A)) = 2.
```

## 2. The normalized class cover

Adjoin a square root `t` of `y` to `Frac(A)`, and put `w=x/t`. The
normalization is

```
B = k[[t,w,z]] / (w^2 + t^4 + z^2),
y = t^2,  x = t w,  z = z.
```

The substitution satisfies the defining equation of `A`. Both new
generators are integral over `A`:

```
t^2=y,  w^2=-(y^2+z^2).
```

Thus `B` is finite over `A`, and its fraction field is
`Frac(A)(sqrt(y))`. The extension has degree two: if `y=g^2` in
`Frac(A)`, then `div(g)=C`; normality implies `g in A`, contradicting
the nonprincipality of `C` just proved.

In coordinates `u=w+i z`, `v=w-i z`, the equation of `B` is

```
u v = -t^4.
```

It is the normal `A_3` surface singularity. Hence this finite normal
ring is exactly the integral closure of `A` in the quadratic extension.
This is the cyclic class cover attached to `[C]`, using the
trivialization `2C=div(y)`.

The deck involution is

```
(t,w,z) |-> (-t,-w,z).
```

Its invariant ring is `A`: it is generated by `z`, `t^2`, `tw`, and
`w^2`, and `w^2=-t^4-z^2` removes the last generator. The fixed locus
has `t=w=0`; the defining equation then forces `z=0` on its support.
The action is therefore free away from the closed point, and the
finite cover is etale there. In particular it is quasi-etale.

## 3. Two inverse branches, each unramified over the curve

The reduced inverse support of `C` is `V(t)`. Its two components are

```
C_+ = V(t,w-i z),
C_- = V(t,w+i z).
```

Each is a smooth formal curve with parameter `z`, and each restriction
to `C` is the identity on `k[[z]]`:

```
C_+ -> C,  C_- -> C
```

are isomorphisms. The involution interchanges the two components. In
particular, the class cover has

```
class order r = 2,
number of inverse branches b = 2,
ramification index of either normalized curve map e = 1 = r/b.
```

Here `e` refers to the maps of normalized curves at the closed point.
It is distinct from divisorial ramification of the surface cover,
which is absent in every quasi-etale class cover.

The scheme-theoretic inverse ideal is `(t w,t^2)` and has reduced
support as above; no claim that this ideal equals `(t)` is needed.

## 4. Consequence and a whole `D_n` family

The assertion that a smooth curve on an isolated normal hypersurface
surface necessarily has ramification index equal to its local class
order on the associated cyclic cover is false. A further local
primitivity condition, such as having a single inverse branch, is
necessary.

The same construction gives a family. For `n>=4`, take

```
A_n = k[[x,y,z]]/(x^2+y^2 z+z^(n-1)),
C_n = V(x,z).
```

Then `div(z)=2C_n`, the ideal `(x,z)` has two minimal generators, and
`C_n` has local class order two. Its class cover is

```
B_n = k[[t,w,y]]/(w^2+y^2+t^(2n-4)),
z=t^2,  x=t w.
```

The cover has type `A_(2n-5)` and inverse branches
`t=0,w=+-i y`, both mapping isomorphically to `C_n`. The same
integrality, normality, fixed-point, and exact-order arguments apply.
This family includes the preceding `D_4` example after interchanging
the roles of `y` and `z`.

The lesson is about local cyclic covers and branch counts. It does
not by itself bound carrier degrees, force conductor torsion, or
settle whether a projective curve is a set-theoretic complete
intersection.

## 5. Independent audit of an arbitrary-order cyclic-quotient family

The parent `local_torsion_curve` independently found the following
stronger family during this audit. The formulas below were independently
derived here and have written elementary proofs; agreement alone is not
the evidence.

Let `N>=2`, `1<=a<N`, and put

```
R = k[[x,y,z]]/(xy-z^N),
C_a = V(x-z^a, y-z^(N-a)),
g = gcd(N,a),  r=N/g.
```

The curve is smooth, with parameter `z`. Write `P=V(x,z)`. One has

```
div(x-z^a)=aP+C_a,
```

so `[C_a]=-a[P]`. The class of `P` has exact order `N`. For an
elementary proof, realize `R` as the invariant subring of `k[[u,v]]`
under

```
(u,v) |-> (zeta u,zeta^(-1) v),
x=u^N,  y=v^N,  z=uv.
```

This quotient is unramified away from the origin. If `jP` is principal,
its pulled-back generator in `k[[u,v]]` has divisor `jV(u)` and hence
is `u^j` times a unit. Invariance and the nonzero constant term of that
unit imply `zeta^j=1`. Thus `N` divides `j`, while `div(x)=NP` gives
the converse. Therefore `C_a` has exact class order `r=N/g`.

The polynomial

```
q=u^(N-a)-v^a
```

is squarefree and cuts out precisely the reduced inverse divisor of
`C_a`. Its character is `zeta^(-a)`, of exact order `r`. The class
cover is consequently the quotient by the kernel `mu_g` of this
character:

```
B = k[[U,V,z]]/(UV-z^g),
U=u^g,  V=v^g,
x=U^r,  y=V^r.
```

Equivalently, `q^r` lies in `R` with divisor `rC_a`, and adjoining its
`r`-th root produces this normalized cover. The cover is connected,
local, normal, cyclic of degree `r`, and etale away from the origin.

At the generic point of `C_a` its inverse algebra is

```
k((z))[U]/(U^r-z^a),  V=z^g/U.
```

Since `k` is algebraically closed of characteristic zero, the equation
has exactly

```
b=gcd(r,a)=gcd(r,g)
```

irreducible factors over `k((z))`. Each factor normalizes to a branch
with ramification index

```
e=r/b.
```

For instance, a branch can be parametrized by `z=s^e`,
`U=c s^(a/b)`, `V=c^(-1)s^((N-a)/b)`; the coprimality of
`e` and `a/b` proves that the normalized branch has degree exactly
`e`. The equality of the two gcd expressions follows from
`gcd(r,a/g)=1`.

Every pair `r>=2`, `e|r` occurs: set `b=r/e`, `N=rb`, and `a=b`.
Then `g=b`, the exact class order is `r`, the branch count is `b`,
and the ramification index is `e`. In particular,

```
N=r^2,  a=r
```

gives arbitrary class order `r` and `r` inverse branches, each mapping
isomorphically to the original smooth curve. The case `N=4,a=2` is
already an `A_3` example of class order two and two unramified branches.

One can also read the ramification directly from a fractional
self-intersection. Take `D=(N-a)P`, which is linearly equivalent to
`C_a`. The equation

```
h=x^((N-a)/g)
```

has divisor `rD` and restricts to `z^(a(N-a)/g)` on `C_a`. Therefore

```
(D.C_a)_p=a(N-a)/N,
e=N/gcd(N,a^2).
```

This is equal to the value `r/gcd(r,g)` found from the class cover.

## 6. The fractional-intersection explanation

Here is the mechanism behind the distinction between class order and
ramification. Let `C` be a smooth curve through the closed point of a
normal complete local surface over `k`, with finite class order `r`.
Choose an effective Weil divisor `D` linearly equivalent to `C` and
not containing `C`. Such a representative exists by choosing a
section of the finite divisorial module `O(C)` whose valuation at the
generic point of `C` is exactly `-1`.

If `div(f)=rC` and `div(h_0)=D-C`, put `h=f h_0^r`. Then
`div(h)=rD`, so `h` is regular on the normal surface and restricts to
a nonzero element of `k[[z]]=O_C`. Write

```
h|_C=z^m epsilon,  epsilon in k[[z]]^*,
(D.C)_p=m/r.
```

The formal unit `epsilon` has an `r`-th root, and the class cover can
equally be constructed by adjoining an `r`-th root of `h`. Its
normalized inverse curve therefore has the same branches as

```
T^r=z^m.
```

Thus its branch count is `gcd(r,m)` and the ramification index of each
branch is `r/gcd(r,m)`, exactly the denominator of `(D.C)_p` in
lowest terms. Changing `D` changes this intersection by an integer,
because the ratio of its two Cartier equations is an `r`-th power
at the generic point of `C`. The denominator is intrinsic.

This argument concerns normalization of the reduced inverse curve;
it does not assume that restriction of the normal surface cover is
itself a normal curve.

For the `D_4` example in sections 1--3, let

```
D_+ = V(x,y-i z),  D_- = V(x,y+i z),
D=D_++D_-.
```

Then `div(x)=C+D`, so `D` is linearly equivalent to `C`, and

```
h=y(x/y)^2=-(y^2+z^2),
h|_C=-z^2,
(D.C)_p=2/2=1.
```

Its denominator is one, explaining the two unramified branches
despite local class order two.

## 7. Signed independent audit of the general theorem and discriminant

Auditor: `duval_counterexample`, 2026-10-14.
Audited source:
[2026-10-14-cyclic-cover-local-smooth-curve.md](2026-10-14-cyclic-cover-local-smooth-curve.md),
sections 1 and 4 only. The examples already audited above were not
recomputed. **Verdict: the statements and written proofs are sound under
the source's complete, excellent, normal two-dimensional local
characteristic-zero hypotheses, with algebraically closed residue field
and smooth `R/P=k[[t]]`.**

The decisive steps were checked separately:

1. Exact class order makes the Kummer extension have degree exactly `r`.
   Finite normalization is local because a finite algebra over a complete
   local ring decomposes into local factors and the normalization is a
   domain. At every height-one prime, dividing the root by the appropriate
   uniformizer power leaves a root of a unit, so the extension is etale.

2. The pulled-back divisor of `T` has coefficient one at each prime over
   `C`. Normality in dimension two makes `S` Cohen--Macaulay. Hence
   `S/(T)` is a Cohen--Macaulay curve, generically reduced and consequently
   reduced everywhere. Thus it is the reduced Cartier inverse curve.
   Every generic component dominates `C`; the absence of embedded
   associated primes makes the finite `k[[t]]`-module torsion-free,
   therefore free of generic rank `r`.

3. The residue equation is `w^r=h_C`, where `w=a/T` at the generic point
   of `C`. Extracting the root of its formal unit reduces it to
   `w^r=t^m`. This has `b=gcd(r,m)` factors; each normalization is
   `k[[s]]` with `t=s^(r/b)`. Replacing the numerator uniformizer `a`
   changes `m` by an element of `rZ`; changing `f` multiplies the residue
   by a unit and changes no valuation. Thus the fractional invariant,
   branch count, and ramification index are well defined.

4. The source uses `D=div(a)-C`, whose class is `-[C]`. Section 6 here
   instead used an effective representative of `[C]`. Their fractional
   intersections have opposite signs modulo integers; their denominators
   agree. The source's sign convention is explicit and consistent.

5. For `A_C=S/(T)` and its finite normalization `bar A_C`, both are
   free lattices of rank `r` in the same separable generic algebra.
   The normalized branch discriminants have total valuation
   `b(e-1)=r-b`. If `M` is the inclusion matrix of an `A_C` basis in
   a `bar A_C` basis, its determinant has valuation
   `length_(k[[t]])(bar A_C/A_C)=dim_k(bar A_C/A_C)=delta`.
   Restricting the generic trace pairing multiplies its determinant by
   `det(M)^2`. Therefore the exact identity is

   ```
   ord_t disc(A_C/k[[t]]) = r-b+2 delta.
   ```

No gap was found in these two new results. This audit is a proof audit,
not computational evidence and not a claim of mathematical novelty.


---

## 2026-10-14-normal-cyclic-cover-torsion-detection

# Torsion detected on an ample smooth rational curve

Date: 2026-10-14.
Author: `cyclic_cover_structure`, independently checking a proposal from
`conductor_general` and the root research agent. Local counterexample and
local Kummer refinement: `local_torsion_curve`.

Status: **NEW PROOF WRITTEN HERE.** Accepted repository results are premises,
not recomputed. No novelty claim is made. This note concerns normal carriers;
it does not eliminate all normal carriers or resolve the universal STCI
problem.

## 1. An intrinsic torsion-detection theorem

Let `X` be a normal integral projective surface over an algebraically closed
field `k`. Let `C` be a smooth rational prime curve. Assume that some positive
multiple `M C` is an ample effective Cartier divisor. In characteristic `p>0`,
only torsion of order prime to `p` is considered in this section. There is no
restriction on torsion orders in characteristic zero.

**Theorem.** A torsion Weil class `T` which is Cartier at every point of `C`
is zero in `Cl(X)`. Consequently the restriction homomorphism

```
Cl(X)_tors -> product_{P in C intersect Sing(X)} Cl(O_{X,P})
```

is injective (on prime-to-`p` torsion in characteristic `p`). If `T` has exact
order `t`, then

```
t = lcm_{P in C intersect Sing(X)} order(T_P).
```

The empty least common multiple is one. In particular this theorem detects
torsion at singularities **on `C`**, independently of singularities elsewhere
on the surface. It does not assert that `Cl(X)` is torsion-free.

### Proof of the cyclic-cover construction

Choose a Weil divisor representing `T`, write `t T=div(phi)`, and form the
usual cyclic reflexive algebra

```
A = direct_sum_{i=0}^{t-1} O_X(iT),
```

where multiplication crossing degree `t` uses the isomorphism
`O_X(tT)->O_X`, `f -> f phi`. Generically this is the Kummer algebra
`k(X)[z]/(z^t-phi)`.

It is a field. Indeed, `k(X)` contains all `t`-th roots of unity, and Kummer
irreducibility fails only if `phi` is a `q`-th power for a prime `q` dividing
`t`. Such a power would give
`div(psi)=(t/q)T`, contradicting the exact order `t`. Equivalently, the
Kummer extension has degree equal to the order of the class of `phi` in
`k(X)^*/k(X)^{*t}`; that order is `t` by the same divisor argument.

The relative spectrum `Y=Spec_X A` is finite, integral and projective. It is
normal: every summand is reflexive, hence has depth two at the closed points
of the normal surface; the finite algebra is therefore `S2`. At every
codimension-one point of `X`, `T` is Cartier, and its cyclic algebra is
finite etale because `t` is invertible. Thus `Y` is regular in codimension
one, and the `R1+S2` criterion applies. These facts can also be obtained by
normalizing `X` in the Kummer field; the displayed reflexive algebra is that
normalization. The cover has cyclic group `mu_t` and is etale outside the
non-Cartier locus of `T`, a finite set. Its reflexive pullback of `O_X(T)`
is trivial.

These precise construction statements agree with Ambro, *Cyclic covers and
toroidal embeddings*, Section 4, Lemmas 4.1--4.2, [primary paper
PDF](https://arxiv.org/pdf/1310.3951). Etaleness near the Cartier locus here
is established directly by the local equation `w^t=unit`; the proof does
not use an assertion of etaleness at arbitrary non-Cartier singular points.

### Proof of the torsion-detection assertion

If `T` is Cartier at every point of `C`, its invertible locus is an open
neighborhood of `C`. The cyclic cover is finite etale on that neighborhood.
Therefore `Y x_X C -> C=P1` is finite etale of degree `t`. Each connected
component is a smooth projective curve finite etale over `P1`. The
Riemann--Hurwitz formula shows that its degree is one: a degree-`e`
component would have `2g-2=-2e`, impossible for `e>1`. Thus this inverse
image consists of `t` pairwise disjoint copies of `P1`.

On the other hand `D=pi^*(M C)` is an ample effective Cartier divisor on
the normal integral projective surface `Y`, with support exactly
`pi^{-1}(C)`. Such support is connected. Here is a proof retaining all
nilpotent layers of the multiple divisor. A normal surface is
Cohen--Macaulay and has a dualizing sheaf `omega_Y`. Serre duality and
Serre vanishing give, for sufficiently large `n`,

```
H^1(Y,O_Y(-nD)) = H^1(Y,omega_Y(nD))^* = 0.
```

Also `H^0(Y,O_Y)=k` and `H^0(Y,O_Y(-nD))=0`. From the exact sequence for
the effective Cartier divisor `nD` one obtains

```
H^0(nD,O_{nD}) = k.
```

A disconnected support would give a nontrivial idempotent in this ring,
a contradiction. Hence `t=1`.

For the exact local-order formula, let `h` be the least common multiple
of the local orders of `T` at the finite set `C intersect Sing(X)`.
Every local order divides `t`, so `h` divides `t`. The class `hT` is
Cartier at every point of `C`, is torsion, and has order `t/h`. The
assertion just proved gives `hT=0`; therefore `t=h`.

The proof works without an ambient projective space and without a global
fundamental-group theorem for `X`. More generally it works if `C` is a
proper connected reduced curve with no nontrivial finite etale covers,
provided an ample effective Cartier divisor has support `C`.

## 2. Exact normal-carrier formula for the quartic

Let `X subset P3` be a normal integral degree-`a` hypersurface in
characteristic zero, containing the accepted smooth rational quartic
`C0`. Put `H=O_X(1)` and

```
g = gcd(a,4),  r = a/g,  s = 4/g,
Delta_0 = r[C0] - s[H].
```

Assume `Delta_0` is torsion of exact order `t`. This is the primitive
class of a hypothetical mate; it gives the accepted first relation

```
m C0 ~ b H,  m = t r,  b = t s.
```

In particular `m C0` is ample Cartier, so the theorem applies. For each
`P in C0 intersect Sing(X)`, let `n_P` denote the exact local Cartier
index of `C0`, that is, the order of `[C0]` in `Cl(O_{X,P})`.
It is finite because `m C0` is Cartier. The hyperplane class is locally
principal, whence `Delta_{0,P}=r[C0]_P` has order

```
k_P = n_P/gcd(n_P,r).
```

Therefore

```
t = lcm_P k_P,
b_min = (4/g) lcm_P [n_P/gcd(n_P,a/g)].
```

For a normal carrier there is no normalization-conductor exponent.
The accepted primitive-ray theorem therefore says that all mate degrees
on this carrier are exactly the positive multiples of `b_min`.

This is a **conditional exact formula**, not a converse based only on
local indices. Finite local indices alone do not imply that
`Delta_0` is torsion: after local Cartier defects are removed, an
infinite-order global Cartier class can remain.

Accepted exclusion of all mates of degree at most four now implies the
necessary condition

```
(4/g) lcm_P k_P >= 5.
```

Thus the following whole normal-carrier classes are excluded at once:

* carriers for which `C0` avoids `Sing(X)`;
* carriers for which every `n_P` divides `a/g`;
* more generally, carriers for which `(4/g) lcm_P k_P <= 4`.

The possible torsion orders are consequently constrained uniformly:

```
g=1: t>=2;  g=2: t>=3;  g=4: t>=5.
```

These are necessary conditions on a hypothetical mate, not an exhaustive
carrier classification. No bound on `a`, on the local indices, or on
their least common multiple has been proved here.

## 3. Failure shield: local order is not curve ramification

A local cyclic class cover can have several branches over a smooth
curve, meeting above the surface singularity. Normalizing those branches
can remove the meeting and lose information needed for the connectedness
argument. In particular a local class order cannot simply be substituted
as a ramification index in Riemann--Hurwitz.

An explicit characteristic-zero example is

```
R = k[[x,y,z]]/(x^2 + z y^2 + z^3),
C = V(x,z).
```

This is a normal isolated hypersurface singularity and `C` is the smooth
`y`-axis. One has `div_R(z)=2C`; the ideal `(x,z)` is not principal at
the origin (its two generators remain independent modulo the maximal
ideal times the ideal). Thus `[C]` has exact local order two.

Adjoining `t` with `t^2=z` and setting `u=x/t` gives the normal cyclic
cover

```
B = k[[u,y,t]]/(u^2+y^2+t^4),
x=t u,  z=t^2.
```

The involution is `(u,y,t)->(-u,y,-t)`, and its invariant ring is `R`.
Its only fixed point is the origin, so the cover is etale outside that
point. The reduced inverse image of `C` is

```
t=0,  u= i y   union   t=0,  u=-i y.
```

It has two branches meeting at the origin. Each normalized branch maps
isomorphically to `C`; its ramification index is one, although the local
class order is two. This example is local and does not assert that this
configuration occurs on a global quartic carrier with a mate. It rules
out the general local equality needed for that shortcut.

There are examples with **arbitrarily large** local class order and
normalized-curve ramification one, even among `A`-type hypersurface
singularities. Let

```
R_N = k[[x,y,z]]/(xy-z^N),
C_a: x=z^a, y=z^(N-a),  1<=a<N.
```

This curve is smooth because its local ring is `k[[z]]`. Write

```
g0=gcd(N,a),  n=N/g0.
```

The cyclic quotient presentation of `R_N` is the invariant ring of
`k[[u,v]]` under `mu_N` acting with weights `(1,-1)`, where
`x=u^N`, `y=v^N`, `z=uv`. The reduced inverse curve is cut out by

```
q=u^(N-a)-v^a.
```

Its semi-invariant character has weight `-a` and exact order `n`.
Consequently `[C_a]` has exact order `n`. To see the exactness without
assuming a class-group classification, `q^n` is invariant and has
divisor `n C_a` downstairs. If a rational function downstairs had
divisor `j C_a`, its pullback would be `q^j` times a unit upstairs.
This unit is semi-invariant; its nonzero constant term forces its
character to be trivial. Hence `N` divides `a j`, so `n` divides `j`.

The class cover is the quotient by the kernel `mu_{g0}` of this
character. It is

```
B = k[[U,V,z]]/(UV-z^g0),
x=U^n, y=V^n.
```

On the generic point of the curve its algebra is `U^n=z^a`. Thus there
are `gcd(n,a)=gcd(n,g0)` normalized branches, each having ramification
index `n/gcd(n,a)`. Given **any** `n>=2` and any `e` dividing `n`,
take `b=n/e`, `N=n b`, and `a=b`. Then the local class order is `n`,
the number of branches is `b`, and every branch has ramification `e`.
In particular `N=n^2,a=n` gives `n` smooth branches mapping
isomorphically to `C_a`. They meet above the surface singularity.

This family proves that local Cartier indices cannot be bounded using
the normalized-curve ramification alone. It does not produce global
fixed-degree hypersurface carriers with unbounded indices.

The independent local Kummer calculation is recorded in
`2026-10-14-cyclic-cover-local-smooth-curve.md`: if `div(f)=nC`, choose
`a` with `v_C(a)=1`, and let `h=a^n/f`. Then `h` is regular, nonzero
on the generic point of `C`, and if `ell` is the order of `h|_C` at
the closed point in the smooth curve parameter, the full local class
cover has

```
gcd(n,ell) normalized branches,
ramification index n/gcd(n,ell) on each branch.
```

The residue class `ell mod n` is independent of the choices. The
ramification invariant is the fractional local intersection class
`ell/n mod Z`; it can be zero for a nontrivial divisor class.

## 4. A conditional global budget retaining the gluing

This additional calculation was independently audited by
`local_torsion_curve`. Retain the normal quartic-carrier setup of section 2
and its degree-`t` cyclic cover `pi:Y->X`. Put `H_Y=pi^*H` and let `D` be
the **reduced** inverse curve. Impose the extra hypothesis that `D` is
Cartier. The primitive relation alone does not imply this hypothesis.

The cover is etale in codimension one. Since the base hypersurface is
Gorenstein, the reflexive dualizing sheaf on `Y` agrees away from
codimension two with `pi^*omega_X` and hence agrees with it everywhere.
Thus `Y` is Gorenstein and

```
K_Y=(a-4) H_Y,  H_Y^2=t a,  H_Y.D=4t,
r D ~ s H_Y,  D^2=16t/a.
```

Adjunction to the Cartier curve gives

```
p_a(D)=1+2t(a-4)+8t/a.
```

Let `R` be the total Riemann--Hurwitz ramification of all components of
the normalization of `D` over `C0=P1`, and let `delta` be the sum of the
local delta invariants of `D`. Their total covering degree is `t`.
The normalization exact sequence and Riemann--Hurwitz, allowing
disconnected normalization, give

```
p_a(D)=1-t+R/2+delta.
```

Consequently

```
delta+R/2 = t(2a-7+8/a),
a divides 8t.
```

The finite map `D->P1` is flat because the reduced Cartier curve is
Cohen--Macaulay and has no component mapped to a point. Its trace
discriminant has degree

```
R+2delta = 2t(2a-7+8/a).
```

This is the global budget which a ramification-only argument omits. It
is a structural formula, not yet a contradiction. For example the
unramified local `A_(n^2-1)` family has the ordinary `n`-fold point
`U^n=z^n` as inverse curve, with `delta=n(n-1)/2`. If the local class
of `Delta_0` generates this order-`n` local class of `C0`, the global
degree-`t` cover has `t/n` such local copies. Their combined contribution
gives the necessary bound

```
n-1 <= 2(2a-7+8/a).
```

This bound is uniform in the mate degree **within the stated local
singularity stratum and the extra Cartier-inverse hypothesis**. It does
not bound arbitrary local indices on arbitrary carriers. Obtaining an
analogue with the residual non-Cartier inverse curve is an open next step.

## 5. What this proves and what remains

The new degree-independent gain is exact localization of the global
torsion obstruction to the finite singular set on the hypothetical
ample rational support. Normal-carrier searches can organize themselves
by those local indices rather than by separate mate degrees. The proof
also applies to arbitrary smooth rational curves with an ample Cartier
multiple and to prime-to-characteristic torsion in positive
characteristic.

The unresolved step is to bound or eliminate the allowable local indices
for **all** normal hypersurface carriers of `C0`, while retaining the
global primitive relation. The local cover may have singularities and a
singular, reducible inverse image of `C0`; its normalization need not be
rationally connected or yield a Hurwitz contradiction. Finite local
indices are necessary but do not certify the global relation. No
statement here covers nonnormal or entirely thick carriers.

For comparison, a separate standard hypersurface route uses the
simple-connectedness of a complex projective hypersurface, stated in
Maxim, *On the topology of complex projective hypersurfaces*, Proposition
2.6, [primary author PDF](https://people.math.wisc.edu/~maxim/hyp_survey.pdf),
and the local class-group exact sequence. The proof above is stronger in
its geometric scope and is self-contained apart from standard Kummer
theory, Serre's normality criterion, Serre duality, and Serre vanishing.



---

## 2026-10-14-moving-linear-cubic-compatibility

# Degree-one moving linear relations: the cubic obstruction

Date: 2026-10-14. Status: new exact cubic calculation, independently accepted in the
[sign/frame audit](2026-10-14-moving-linear-cubic-independent-audit.md). The accepted embedded chart and the independently established
quadratic obstruction locus are premises; neither is re-audited here.

The calculation below eliminates the nonquadric members of the quadratic
obstruction-zero locus. Precisely, among basepoint-free moving linear relation
lines `O(-8) -> N_C0^*=O(-7)^2`, the only line admitting a compatible relation
through cubic normal degree is the line of the actual quadric. This is a
classification of the specified relation-lifting problem. A relation with
torsion or poles, a first relation of higher order, and an additional relation
in the relevant degree are separate problems.

## 1. Accepted inputs and the next target

Use the frames and coefficients from the [independent quadratic
audit](2026-10-14-moving-linear-quadratic-obstruction-independent-audit.md):

    a=A+Cz, b=B+Dz, Delta=AD-BC != 0,
    f0=a u+b v,
    f1=(Aw+C)u'+(Bw+D)v'.

The relation line is `W=O(-8)` and its quotient is `M=O(-6)`. The quotient is
normalized by `(u,v) -> (b,-a)q`; on the other chart its frame is
`q1=z^-6 q0`. The next relation obstruction therefore lies in

    Hom(W,Sym^3 M)=O(-10).

In the chart-zero frame, its Cech class retains exactly the coefficients of
`z^-1,...,z^-9`. Nonnegative exponents and exponents at most `-10` are
coboundaries. There is no extra power of `z` after evaluating a cubic expression
at `(u,v)=(b,-a)`.

The accepted quadratic class vanishes precisely at the three diagonal points

    [A:B:C:D]=[t:0:0:1],
    (t-2)(3t^2-4t+12)=0,

and on the open conic

    A=2D, BC=8D^2, D!=0.

The conic is normalized below by `D=1, B=t, C=8/t`, with `t!=0`.

## 2. Canonical quadratic correction and the unit term

Let `T` be the accepted quadratic discrepancy evaluated at `(b,-a)`. On its
obstruction-zero locus, split it uniquely as

    T=T_plus+T_minus,
    supp(T_plus) contained in {0,1,...},
    supp(T_minus) contained in {...,-5,-4}.

There is no remaining quotient-level quadratic lifting freedom because
`H^0(O(-4))=0`. Define

    ell0=(-C u-D v)/Delta,
    ell1=(A u'+B v')/Delta,
    q0=T_plus,
    q1(w)=-z^4 T_minus(z),
    F0=f0+q0 ell0^2,
    F1=f1+q1(w)ell1^2.

On the reduced curve, `ell0(b,-a)=1`. On the other chart the corresponding
evaluation is `ell1=z^-6` in the first quotient frame. Consequently the
quadratic part of `z^8 F1-F0` evaluates to zero. The coefficient pair `(a,b)`
is unimodular, so this part is exactly divisible by the relation:

    [z^8 F1-F0]_2=f0 L2,

where `L2` has normal degree one. The degree-one term of the unit comparing
the two local generators is thus `L2`. Its contribution in degree three is
`L2 q0 ell0^2`. The evaluated cubic remainder is

    R=[z^8 F1-F0]_3(b,-a)-q0 L2(b,-a).

Local additions to either quadratic correction that are multiples of `f`
change the local generator by a unit. They change the cubic calculation by
the corresponding unit contribution and a cubic coboundary. Thus they do not
introduce another compatibility parameter. The unspecified degree-two term
of the comparison unit multiplies `f0` and vanishes in the quotient.

## 3. Exact chart calculation

The accepted chart is expanded only through normal degree three:

    b_orig=u+(3/2)zv, a_orig=v,
    inv=(z^4+b_orig)^-1,
    W=(z^3+v)inv,
    a'=z inv-W^3,
    b'=inv-W^4,
    u'=a'/2,
    v'=-3W a'+2b'.

In the second-chart corrections above, the coefficient variable `w` is
substituted by the actual `W`, including its normal terms. In particular,
the derivative of `q1(w)` is retained. The source uses the exact finite series

    inv=sum_(j=0)^3 (-b_orig)^j z^(-4j-4) modulo (u,v)^4.

All arithmetic uses `fractions.Fraction`, sparse Laurent polynomials in `t,z`,
and truncation only in the normal variables `u,v`. There is no sampling,
floating-point calculation, or generic-parameter saturation. The two nonreal
diagonal points are handled together in the exact field
`Q[t]/(3t^2-4t+12)`; negative powers of `t` use
`t^-1=1/3-t/4` there.

At the accepted quadric point `t=2`, both quadratic corrections vanish and

    L2(b,-a)=4 z^-3,
    [R]=0 in H^1(O(-10)).

The actual quadric equation is an accepted all-orders lift.

At either other diagonal point,

    q0=q1=0,
    L2(b,-a)=(2t-4)z^-3,
    [R]=(64/27)(3-t)z^-5.

Since `3t^2-4t+12` has value `27` at `t=3`, this cohomology class is nonzero
at both points. Thus neither diagonal relation extends compatibly through
cubic normal degree.

On the entire open conic, the exact corrections are

    q0=-96/t^2-192z/t^3,
    q1(w)=-6t^2-3t^3 w.

The comparison-unit evaluation is

    L2(b,-a)=64/t^3+16z^-1/t^2+20z^-2/t+4z^-3
                 -3t z^-4+t^2 z^-5+t^3 z^-6.

Its cubic class is exactly

    [R]=512z^-1/t^4-384z^-2/t^3+64z^-3/t^2
           +4t^2 z^-7-6t^3 z^-8+2t^4 z^-9.

The `z^-1` coefficient is nonzero for every allowed `t`. Hence no member of
the open conic extends through cubic normal degree. The points in the conic's
closure with `D=0` have `Delta=0`, so they are outside the basepoint-free
degree-one relation problem and are not discarded by a saturation here.

## 4. Conclusion and scope

The complete basepoint-free degree-one quadratic zero locus has now been
tested in the next normal degree. Only the actual quadric relation survives.
Equivalently, a primitive length-four structure on `C0` with a single
compatible relation line `O(-8)` and quotient conormal `O(-6)` must use the
quadric relation line. This statement fixes the line, not an arbitrary
higher-order thickening or an STCI presentation.

For a moving linear relation of movement degree `e`, the cubic target is
generally `O(4e-14)`. The new calculation concerns `e=1`; it does not exclude
`e=2` or `e=3`, whose cubic cohomology can still be nonzero, or `e>=4`, for
which this particular cohomology group vanishes. It also does not justify
taking an `r`th root of a higher-order pure-power first relation.

A useful further consequence concerns an actual primitive length-four
structure `Y` with this first quotient conormal, rather than a formal relation
alone. The relation's quotient-level corrections in degrees two and three
are unique once they exist: the differences of two compatible lifts are
sections of `Hom(W,Sym^j M)=O(8-6j)`, which have no global sections for
`j=2,3`. Multiples of the relation merely change its local generators.
Therefore the compatible ideal of `Y` modulo `I_C0^4` agrees with that of
the accepted actual quadric, and its quadric equation lies in `I_Y`.

In particular, if `Y` is the full symbolic length-four structure on an
integral normal degree-eight carrier, then the quadric section vanishes to
order at least four along `C0`. Its complete-intersection cycle has degree
`2*8=4*4`. There is no residual curve and no isolated component, because the
ambient complete intersection is pure. The quadric and that carrier would
have set-theoretic intersection `C0`, contradicting the accepted low-carrier
exclusion. Thus a normal degree-eight carrier cannot have an everywhere
primitive symbolic quadruple with free conormal `O(-6)`. This uses the full
symbolic quadruple hypothesis, not merely its generic first symbol.

The exact [new computation](../computations/moving_linear_cubic_compatibility_2026_10_14.py)
and [full coefficient output](../validation/2026-10-14-moving-linear-cubic/cubic-results.json)
preserve the complete discrepancy and the retained obstruction for all three
strata. No inherited accepted computation was rerun.


---

## 2026-10-14-moving-linear-cubic-independent-audit

# Independent audit of the degree-one moving linear cubic obstruction

Date: 2026-10-14. Status: **PASS**, exact independent derivation of the new
cubic calculation. The accepted embedded chart and [quadratic
audit](2026-10-14-moving-linear-quadratic-obstruction-independent-audit.md)
are premises. Their earlier computations were not re-audited. The owner's
[cubic note](2026-10-14-moving-linear-cubic-compatibility.md) was first read
after this audit's separate expansion had produced its answer.

## 1. Frame and correction signs

Write `W=O(-8)`, `M=O(-6)`,

    a=A+Cz, b=B+Dz, Delta=AD-BC != 0,
    f0=a u+b v,
    f1=(Aw+C)u'+(Bw+D)v'.

On the reduced overlap the quotient frame transforms by `q1=z^-6 q0`,
whereas the relation frame transforms by `W1=z^-8 W0`. Consequently the
cubic target is `Hom(W,Sym^3 M)=O(-10)`. Its first-chart coefficient is
obtained by evaluating at `(u,v)=(b,-a)`, with no additional factor of `z`.
Exactly `z^-1,...,z^-9` survive in its Cech cohomology; exponents at least
zero and at most `-10` are coboundaries.

Let `T` denote the accepted evaluated quadratic discrepancy. On its zero
locus write `T=T_plus+T_minus`, with exponent supports at least zero and
at most `-4`, respectively. Set

    ell0=(-C u-D v)/Delta,
    ell1=(A u'+B v')/Delta,
    q0=T_plus,
    q1(w)=-z^4 T_minus(z),
    F0=f0+q0 ell0^2,
    F1=f1+q1(w)ell1^2.

The quotient evaluations are `ell0=1` and `ell1=z^-6`. Thus the second
degree quotient discrepancy is `T+z^-4 q1-q0=0`; this fixes both correction
signs. The remaining second-degree expression is `f0 L2`. The gluing unit
therefore has first normal term `L2`, and

    z^8 F1=(1+L2+L3)F0 modulo normal degree four.

After evaluating in the quotient, the third-degree remainder is precisely

    R=[z^8 F1-F0]_3(b,-a)-q0 L2(b,-a).

The minus sign comes from the third-degree product `L2 q0 ell0^2`.
The term `L3 f0` vanishes in the quotient.

## 2. Independent expansion method and exact output

The independent source changes normal variables before expanding:

    u=b e+(D/Delta) h,
    v=-a e-(C/Delta) h.

Then `f0=h` and `ell0=e` exactly. In particular the coefficient of `e h`
in the second-degree overlap is directly `L2(b,-a)`. This avoids copying
the owner's binary-polynomial division or cubic output.

Put `p=u+(3/2)zv` and `k=u+(1/2)zv`. Direct expansion of the exact embedded
chart gives the new third-degree terms

    [u']_3=(1/2)z^-15(-p^3+3p^2k+6pk^2+k^3),
    [v']_3=z^-16(p^3+5p^2k-12pk^2-4k^3).

The second-chart base coordinate is the actual
`W=(z^3+v)/(z^4+p)`. Its normal terms are retained in the coefficients
of `f1` and `q1(W)`. In particular, the normal derivative of `q1` contributes
to degree three. Expanding the inverse through degree three is exact modulo
`(e,h)^4`; all arithmetic is over rational Laurent polynomials in the
indeterminate parameters `z,t`.

For the diagonal `A=t,B=C=0,D=1`, the accepted quadratic-zero condition is
`(t-2)(3t^2-4t+12)=0`. Both local quadratic corrections are zero. The raw
cubic quotient is

    R=(-10+22t-16t^2+(13/2)t^3-(11/8)t^4)z^-5.

At `t=2` it vanishes. In the exact field `Q[t]/(3t^2-4t+12)` it is

    R=(64/27)(3-t)z^-5.

This is nonzero at both nonquadric diagonal points, since the quadratic
has value `27` at `t=3`. The comparison unit at those points evaluates to
`(2t-4)z^-3`; at the quadric point it evaluates to `4z^-3`.

On the open conic `A=2,B=t,C=8/t,D=1`, with `t!=0`, the exact local
quadratic corrections are

    q0=-96/t^2-192z/t^3,
    q1(w)=-6t^2-3t^3 w.

The independently computed comparison unit is

    L2(b,-a)=t^3z^-6+t^2z^-5-3tz^-4+4z^-3
              +20t^-1z^-2+16t^-2z^-1+64t^-3.

After the required subtraction, the complete cubic quotient is

    R=3t^6z^-11+9t^5z^-10+2t^4z^-9-6t^3z^-8+4t^2z^-7
       +64t^-2z^-3-384t^-3z^-2+512t^-4z^-1
       +9216t^-5+12288t^-6z.

Its retained cohomology class is therefore

    [R]=2t^4z^-9-6t^3z^-8+4t^2z^-7
         +64t^-2z^-3-384t^-3z^-2+512t^-4z^-1.

The `z^-1` coefficient is nonzero at every allowed point. These are
identities over the parameter Laurent ring, not tests at finitely many
parameters. They agree with the owner's calculation term for term.

## 3. Lifting freedom and primitive length-four scope

Two quotient-level quadratic lifts of the same leading line differ by a
global section of `Hom(W,Sym^2 M)=O(-4)`, whose `H^0` is zero. Thus the
quadratic correction is unique modulo changes of the local relation
generator by units. Adding `f P` in local normal degree two is such a unit
change to that order. Its induced degree-three product is a local correction,
so the corresponding change of the cubic remainder is a Cech coboundary.
The unrestricted degree-two part of a comparison unit multiplies `f0` and
vanishes in the quotient. Hence no extra quadratic parameter or unit
parameter can remove a nonzero class above. Local cubic corrections remove
exactly the displayed cubic coboundaries.

A primitive curvilinear structure of length four has `I_C^4` in its ideal,
and locally its ideal modulo `I_C^4` is generated by its first relation.
There is no independent initial relation in normal degrees one, two, or
three. Its local first-relation generators must therefore pass this cubic
compatibility problem. The owner's conclusion is valid: with the specified
line `O(-8)` and quotient conormal `O(-6)`, its line must be the actual
quadric line. The calculation does not apply when torsion or poles are
allowed, or when another independent relation enters in the relevant
degree. It does not take a root of a higher-order pure-power relation and
does not assert an STCI exclusion on its own.

The independent [source](../computations/moving_linear_cubic_independent_audit_2026_10_14.py)
and [complete stdout](../validation/2026-10-14-moving-linear-cubic/independent-audit/stdout.txt)
preserve the new derivation and its exact field reductions.


---

## 2026-10-14-moving-linear-ideal-rigidity-independent-audit

# Degree-one moving linear relations: ideal rigidity and a carrier consequence

Date: 2026-10-14. Status: independent geometric audit conditional only on the
new cubic classification's recorded exact coefficient verification. This
note does not repeat the accepted quadric or constant-direction calculations.

Use the [quadratic frame review](2026-10-14-moving-linear-quadratic-obstruction-independent-audit.md)
and [new cubic classification](2026-10-14-moving-linear-cubic-compatibility.md).
They identify the unique compatible basepoint-free moving linear relation
line `W=O(-8)` through normal degree three as the line of the actual quadric
`q=u+(z/2)v`. Its quotient conormal is `M=O(-6)`.

## 1. Finite principal ideals with a fixed relation line

Let `C` be a smooth curve in a smooth threefold, with conormal bundle `E`.
Fix a subline `W` in `E` whose quotient `M=E/W` is a line bundle. Consider
coherent ideals modulo `I_C^N` locally generated by one normal-order-one
relation with this leading subline. Such ideals include `I_C^N` by
definition; their associated initial ideal is generated by `W` in each
order below `N`.

Suppose two such ideals agree through normal degree `j-1`. Locally choose
their generators to agree to that order, using multiplication by units.
Their degree-`j` difference is a local section of

    Hom(W, Sym^j E / (W tensor Sym^(j-1)E))
       =Hom(W,M^j).

Compatibility of the two ideals makes these local differences a single
global section of `Hom(W,M^j)`. If that space of global sections is zero,
the differences are multiples of the common leading relation and can be
removed by multiplying the local generators by units of normal degree
`j-1`. The ideals then agree through degree `j`.

Thus a compatible finite principal ideal with fixed `W` is unique if

    H^0(Hom(W,M^j))=0 for 2<=j<N.

This is uniqueness of ideals. It does not choose a distinguished local
generator; generator units are exactly the harmless differences removed
in the argument.

## 2. The quadric direction is rigid at every finite length

For `C0`, `W=O(-8)` and `M=O(-6)` give

    Hom(W,M^j)=O(8-6j).

All these spaces of global sections vanish for `j>=2`. The actual quadric
supplies a compatible principal ideal at every finite order. Therefore,
once the degree-one moving relation has survived the cubic obstruction,
every finite principal ideal with that line equals

    (q)+I_C^N

as an ideal on the `N`th ambient infinitesimal neighborhood of `C`.
In particular, every primitive length-`N` structure with quotient
conormal `O(-6)`, for `N>=4`, is scheme-theoretically contained in the
actual quadric. Here primitive means that locally it has the form
`(f,t^N)` in smooth ambient coordinates, with `C=(f,t)`; this hypothesis
implies `I_C^N` is already contained in its ideal. Its ideal modulo
`I_C^N` is precisely of the principal form used above.

No claim is made about higher-order pure-power relations, nonsaturated
first relations, torsion in the first normal quotient, or a second
independent relation before normal degree four.

## 3. Consequence for a normal carrier

Let `F` be an integral hypersurface of degree `a` containing `C0`, and
assume its entire symbolic multiple `C_N` is a primitive length-`N`
structure with quotient conormal `O(-6)`, where `N>=4`. The rigidity result
gives `q in I_(C_N)`. If `F` is normal, this says that the effective Weil
divisor of the quadric restriction satisfies

    div_F(q) >= N C0.

If `F` differs from the quadric, `q` is nonzero on `F`, and intersecting
with the hyperplane class gives

    2a >= 4N,  hence N<=a/2.

In the equality case `N=a/2`, the residual effective Weil divisor has
degree zero and therefore vanishes. Hence the support of `F intersect Q`
is exactly `C0`: the actual quadric is a mate. This contradicts the
accepted low-degree-carrier exclusion for `C0` in characteristic zero.

Consequently such a normal carrier must satisfy the strict inequality

    N<a/2.

For `a=8`, even a primitive symbolic quadruple with conormal `O(-6)` is
therefore impossible. This conclusion requires the entire symbolic
quadruple to be primitive, not just generic curvilinearity or first
conormal freeness at selected points. It applies in every carrier degree
with the stated structure and makes no assertion about unbounded local
index strata lacking that structure.

## 4. Verification and boundary

The finite ideal uniqueness proof, inclusion of `I_C^N` for a primitive
multiple, and the divisor-degree consequence have been independently
checked geometrically. The new cubic classification supplies the actual
quadric direction; its exact source and coefficient record are linked in
the owner note. Existing low-degree exclusions are premises, not rerun
computations. This is a structural reduction with explicit hypotheses,
not a solution of the universal STCI question.


---

## 2026-10-14-quadric-opposite-ruling-phase-family-failure

# A global opposite-ruling phase family always has extra inverse points

Date: 2026-10-14. Owner: `quadric_global_phase_geometry`, for
`projection_conductor_ray/quadric_phase_review`.
Status: **EXACT FAILURE SHIELD FOR THE DISPLAYED FAMILY ONLY**.

Let `S=P1 x P1`, with affine coordinates `(x,y)`, diagonal `c:y=x`,
and polarization `H=(2,2)`. For `a!=0,-1` and arbitrary `u`,
homogenize the following four polynomials to bidegree `(2,2)`:

    U0=1,
    U1=(a x+y)/(a+1),
    U2=a^2 x^2+y^2-(a^2+1)xy+u x^2y+(1-u)xy^2,
    U3=x^2y^2.

On the diagonal their restriction is `[1:t:t^3:t^4]`, the literal
fixed C0. On the opposite rulings through `(0,0)`, the points
`(s,0)` and `(0,a s)` have the same projective image. The section
`Q=(y-x)^2` has respective values `s^2` and `a^2 s^2`, so this
branchwise phase is the arbitrary constant `a^{-2}`.

The four sections have no common zero. On the finite chart this
follows from `U0=1`. On the boundary `x=Infinity`, they reduce to

    [0:0:a^2 y0^2+u y0 y1:y1^2],

and on `y=Infinity` they reduce to

    [0:0:x0^2+(1-u)x0 x1:x1^2].

In each case the last two entries have no common zero; at
`(Infinity,Infinity)` the last entry is nonzero. The resulting
morphism is finite because its pulled-back polarization is ample.

However, its entire inverse image of C0 always includes a point
outside the diagonal. If `u!=0`, the point

    (x,y)=(Infinity,-a^2/u)

maps to `[0:0:0:1]`. If `u!=1`, the point

    (x,y)=(-1/(1-u),Infinity)

maps to the same endpoint. Both displayed finite coordinates are
nonzero, so these are actual boundary points outside `c`.
At least one exists for every `u`: avoiding both would require
simultaneously `u=0` and `u=1`.

Therefore this family never satisfies the full inverse-image
support condition `nu^{-1}(C0)_red=c`. In particular it supplies
no global fixed-C0 mate-admitting carrier and no counterexample to
the accepted projective frontier. The argument does not require
birationality and places no restriction on the order of `a^{-2}`.

It also does not exclude general opposite-ruling pairs. The
[complete coefficient normal form](2026-10-14-quadric-opposite-ruling-phase-normal-form.md)
contains arbitrary vectors `D,E in k^4` in place of the restricted
choice `D=W2,E=u W2`; those coefficients can remove this particular
boundary obstruction. No general phase-order bound or full
four-section family exclusion follows from this calculation.
