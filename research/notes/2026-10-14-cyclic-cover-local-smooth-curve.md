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
