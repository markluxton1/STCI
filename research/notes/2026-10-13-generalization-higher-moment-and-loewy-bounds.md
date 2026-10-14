# Reflection, higher moments, and sharp codimension-two Loewy bounds

Research batch: 2026-10-13, continued 2026-10-14. Contribution from the
`socle_audit/higher_moments` worker. No global STCI conclusion is asserted.

## Status and scope

**PROVED HERE:** the reflection identity and its equality criterion in §1;
the characteristic-free structural proof in §2; the sharp length/Loewy and
all-increasing-moment bounds in §3; and the explicit sharpness family in §4.

The codimension-two drop-by-at-most-one theorem is also **KNOWN**. A modern
primary research statement is J. Jelisiejew, S. K. Masuti, M. E. Rossi,
*On the Hilbert function of Artinian local complete intersections of
codimension three*, arXiv:2202.04021v2, §3, equation (3.2):
<https://arxiv.org/html/2202.04021v2>. It credits Macaulay, Briançon, and
Iarrobino, and cites V. Bertella, *Hilbert function of local Artinian level
rings in codimension two*, J. Algebra 321 (2009), 1429–1442, Theorem 2.6,
for realizations. The proof below removes any need to transfer
characteristic hypotheses from those references.

Throughout §1, let `(A,m,k)` be a finite local Gorenstein algebra over its
residue field `k`, with

\[
h_i=\dim_k \mathfrak m^i/\mathfrak m^{i+1},\qquad
n=\dim_k A,\qquad
d=\max\{i:\mathfrak m^i\ne0\},\qquad
M=\sum_{i=0}^d i h_i.
\]

Thus `d` is the last nonzero degree, and `m^(d+1)=0`. In §§2–4 assume
additionally that `k` is infinite and `A=k[[x,y]]/I`, with `I` primary to
`(x,y)`. These hypotheses hold for the completed generic transverse
algebra of a complete intersection supported on a curve over an
algebraically closed field. Let `b=ord(I)` denote the least order of a
nonzero element of `I`; use `b`, rather than `m`, to avoid conflating this
integer with the maximal ideal.

## 1. Exact reflection identity, not merely a first-moment estimate

Set

\[
T_i=\dim_k\mathfrak m^i=\sum_{j=i}^d h_j,
\qquad
\Delta_i=n-T_i-T_{d-i+1},\quad 1\le i\le d.
\]

Choose a linear functional `lambda:A->k` nonzero on the one-dimensional
socle. The pairing `lambda(ab)` is perfect. Consequently

\[
\dim_k\operatorname{Ann}(\mathfrak m^i)=n-T_i.
\]

The inclusion `m^(d-i+1) subset Ann(m^i)` proves

\[
\boxed{\Delta_i=
\dim_k\bigl(\operatorname{Ann}(\mathfrak m^i)/
\mathfrak m^{d-i+1}\bigr)\ge0.}
\]

Also `Delta_i=Delta_(d-i+1)`, and `Delta_1=Delta_d=0` when `d>=1`,
because `Ann(m)=m^d` is the socle.

If `X` has probability mass `h_i/n` at `i`, then

\[
\boxed{X\ \le_{\rm st}\ d-X.}
\]

Indeed, at every integer threshold `i`,
`P(X>=i)=T_i/n <= 1-T_(d-i+1)/n=P(d-X>=i)`.
This is the complete first-order stochastic dominance statement;
equivalently, `E f(X)<=E f(d-X)` for every increasing real function `f`
on `{0,...,d}`.

For any real odd function `phi` on the centered support, put `c=d/2`.
Summation by parts gives the exact identity

\[
\boxed{\sum_{i=0}^d h_i\phi(i-c)
=-\frac12\sum_{i=1}^d\Delta_i
\bigl(\phi(i-c)-\phi(i-1-c)\bigr).}
\tag{1}
\]

In particular, every increasing odd central moment is nonpositive:

\[
\sum_{i=0}^d h_i(i-d/2)^{2r+1}\le0
\qquad(r\ge0).
\]

The first instance gives `M<=nd/2`. If `phi` is strictly increasing at
each adjacent pair of support points, equality in (1) is equivalent to
every `Delta_i` vanishing. The following conditions are therefore
equivalent:

1. `M=nd/2`;
2. one, hence every, central odd power moment vanishes;
3. `Ann(m^i)=m^(d-i+1)` for every `i=1,...,d`;
4. `h_i=h_(d-i)` for every `i`;
5. `gr_m(A)` is Gorenstein.

For `(3)=>(5)`, an element of `m^i` outside `m^(i+1)` cannot annihilate
`m^(d-i)`, because `Ann(m^(d-i))=m^(i+1)`. Thus the product pairing
`G_i x G_(d-i) -> G_d` is perfect. Conversely a graded Gorenstein
algebra has symmetric Hilbert function, which implies equality of all
tails and annihilators. This proof includes `i=0,d` by the usual
`Ann(A)=0`, `Ann(0)=A` conventions.

**Edge cases.** For `d=0`, `A=k`, `n=1`, the tail sum is empty, every
central moment is zero, and the equality conditions are vacuous or
automatic. For `d=1,2`, the endpoint deficit identities force all
`Delta_i=0`, so every local Gorenstein algebra in these socle degrees
has a Gorenstein associated graded algebra.

A quantitative refinement is available when
`D=nd/2-M>0`, necessarily `d>=3`. For `r>=0`, let

\[
O_{2r+1}=\sum_i h_i(i-d/2)^{2r+1},\qquad
\alpha_r=\begin{cases}1&d\text{ even},\\2^{-2r}&d\text{ odd},\end{cases}
\]

and

\[
\beta_r=(d/2-1)^{2r+1}-(d/2-2)^{2r+1}.
\]

Since only `Delta_2,...,Delta_(d-1)` can contribute, their positive
discrete-derivative weights give

\[
\boxed{\alpha_r D\le -O_{2r+1}\le\beta_rD.}
\tag{2}
\]

In particular no higher central odd moment can vanish while the first
one is negative. Higher moments reweight the same annihilator defects;
they are not independent existence obstructions without further data.

## 2. Characteristic-free drop theorem from one Jordan block

Write `G=gr_m(A)=k[X,Y]/I*`, where `I*` is the ideal of initial forms.
The equality `ord(I)=b` gives `h_i=i+1` for `0<=i<b`.

Choose a nonzero order-`b` element of the original ideal `I`. Over an
infinite field, choose a linear coordinate `x` such that its degree-`b`
initial form remains nonzero after restriction to `x=0`. Complete it by
a coordinate `y`. Then

\[
A/xA\cong k[[y]]/(y^b).
\tag{3}
\]

To justify (3) directly, every original ideal element restricts to a
series of order at least `b` in `y`, and the chosen element restricts to
one of order exactly `b`; ideals of `k[[y]]` are principal. Independently,
restriction of the initial ideal gives

\[
G/(X)\cong k[Y]/(Y^b).
\]

No assertion that taking associated graded commutes with this quotient
is needed. These are two direct restriction calculations.

For `i>=b-1`, multiplication by `X` maps `G_i` onto `G_(i+1)`.
Therefore

\[
\mathfrak m^{i+1}=x\mathfrak m^i+\mathfrak m^{i+2}
\quad\Longrightarrow\quad
\mathfrak m^{i+1}=x\mathfrak m^i
\tag{4}
\]

by Nakayama applied to `m^(i+1)/x m^i`.

Put `K=Ann_A(x)`. The perfect Gorenstein pairing identifies `K`, as a
`k[[y]]`-module, with `(A/xA)^vee`. By (3) its `y` action consists of
one Jordan block of length `b`. In particular its submodules are exactly
`y^aK`, `0<=a<=b`.

Set `F_i=K cap m^i=y^(a_i)K`. The containment

\[
yF_i\subseteq F_{i+1}\subseteq F_i
\]

implies `a_i<=a_(i+1)<=a_i+1`, so
`dim(F_i/F_(i+1))<=1`. The exact sequence obtained from (4) gives

\[
\dim_kF_i=\dim_k\mathfrak m^i-\dim_k\mathfrak m^{i+1}=h_i
\qquad(i\ge b-1).
\]

Hence

\[
\boxed{h_i-h_{i+1}\in\{0,1\}\quad(i\ge b-1).}
\tag{5}
\]

This proves the classical codimension-two drop theorem in all
characteristics. The argument needs only the infinite-field coordinate
choice, not differentiation, Lefschetz theory, or classification of
Hilbert functions. Before degree `b-1`, the function rises by one.

The same argument also gives a modest extension: for an arbitrary
Artinian quotient of `k[[x,y]]` of socle type `t`, `Ann(x)` has `t`
Jordan blocks, and a submodule of this `k[[y]]`-module has at most `t`
generators. Thus every decline after the initial rising segment is at
most `t`. The Gorenstein case is the one-block case `t=1` above.

## 3. Sharp length/Loewy bound and a stronger moment bound

From `h_(b-1)=b` and (5), the earliest possible descent to one is

\[
B=(1,2,\ldots,b-1,b,b-1,\ldots,2,1),
\]

with last degree `2b-2`, length `b^2`, and first moment
`b^2(b-1)`. Thus

\[
\boxed{d\ge2b-2,\qquad n\ge b^2,\qquad
d\le n-(b-1)^2-1.}
\tag{6}
\]

For the final inequality, subtract one from every nonzero Hilbert
entry. The initial rise contributes `b(b-1)/2`; the forced descent
contributes `(b-1)(b-2)/2`. Hence
`n-(d+1)>= (b-1)^2`.

Equality in the last inequality of (6) holds exactly when the Hilbert
function is `B` followed by `n-b^2` additional entries equal to one.

There is a stronger statement at fixed `n,b`. Put `q=n-b^2>=0` and let
`h^max` be `B` followed by `q` ones, with last degree
`d_max=2b-2+q=n-(b-1)^2-1`. Every admissible Hilbert function satisfies

\[
\sum_{j=0}^i h_j\ \ge\ \sum_{j=0}^i h^{\max}_j
\qquad\text{for every }i.
\tag{7}
\]

For `i<=2b-2`, this follows from the forced pointwise lower baseline.
For `2b-2<i<=d`, every entry is at least one. For `i>d`, the left-hand
side is already the total length `n`. These cases prove (7).

Thus the degree distribution of `A` is stochastically dominated by the
distribution `h^max/n`. Every increasing function `f` satisfies

\[
\boxed{\sum_i h_i f(i)\le
\sum_{i=0}^{2b-2}B_i f(i)+
\sum_{r=1}^q f(2b-2+r).}
\tag{8}
\]

Equality for any strictly increasing `f` is equivalent to `h=h^max`.
In particular

\[
\boxed{M\le b^2(b-1)+q(2b-2)+\frac{q(q+1)}2.}
\tag{9}
\]

Unlike the weaker substitution of (6) into `M<=nd/2`, (9) uses the
whole forced staircase. Relative to that substitution it gains
`q(b-1)^2/2`. All power moments of positive degree have the corresponding
sharp upper bound from (8).

An equivalent useful expression is

\[
\boxed{M\le\frac{n(n-1)-(b-1)^2(2n-b^2)}2.}
\tag{10}
\]

If only `ord(I)>=a` is known, then (10) remains valid with `a` in place
of `b`: the correction `(b-1)^2(2n-b^2)` increases on
`1<=b<=sqrt(n)`. Its real derivative is
`2(b-1)(2n-2b^2+b)>=0` there. In particular every algebra of embedding
dimension two has `b>=2`, giving the sharp uniform estimate

\[
\boxed{M\le(n^2-3n+4)/2.}
\tag{11}
\]

## 4. Explicit sharpness in every characteristic

For any `b>=1` and `q>=0`, set `N=b+q` and

\[
A_{b,q}=k[[x,y]]/(x y^{b-1},\ x^b+y^N).
\]

This is an Artinian complete intersection: its only prime support is
`(x,y)`, and the two generators form a regular sequence in the regular
two-dimensional ambient ring. For a local degree order with `x^b`
leading `y^N` when `N=b`, an enhanced standard basis is

\[
x y^{b-1},\quad x^b+y^N,\quad y^{N+b-1}.
\]

The last element comes from
`y^(b-1)(x^b+y^N)-x^(b-1)(x y^(b-1))`; all remaining S-pairs reduce
immediately. This calculation uses no divisions or characteristic
restrictions. Its standard monomials are

\[
y^j\ (0\le j\le N+b-2),\qquad
x^a y^j\ (1\le a\le b-1,\ 0\le j\le b-2).
\]

Consequently `n=b^2+q`, `d=2b-2+q`, and the Hilbert function is exactly
`h^max`. Thus (6), (8), and (9) are sharp, including in positive
characteristic. For `b=1`, the rectangle of mixed monomials is empty
and the family is simply the curvilinear algebra `k[[y]]/(y^(q+1))`.

## 5. What this contributes to the STCI search

The transverse generic algebra of a hypothetical two-equation
thickening is a codimension-two Artinian complete intersection.
Its Hilbert filtration therefore obeys these uniform inequalities for
all equation degrees. They replace repeated low-degree Hilbert-function
casework with a single structural package: reflection defects, a
one-block argument, and a sharp staircase moment bound.

These necessary local conditions are compatible with explicit local
complete intersections of arbitrarily large socle degree. A global
exclusion must still use the conormal filtration, its degree/extension
data, or another compatibility constraint preventing these local
algebras from occurring globally on the curve. No local numerical
bound here is by itself a global STCI obstruction.
