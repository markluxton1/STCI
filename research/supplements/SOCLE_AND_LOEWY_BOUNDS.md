# Conormal socle duality, reflection and Loewy bounds

This is the mathematical owner for the full conormal/socle budget R-0032 and its stronger reflection and higher-moment consequences. It retains the complete actual-layer argument, the independent socle/equality-duality reconstruction, the characteristic-free codimension-two Hilbert-drop proof and sharpness examples. A scalar budget is necessary data for an actual supported Gorenstein thickening; it neither realizes a homogeneous equation pair nor proves a general STCI obstruction.

The proof mechanisms are complementary. Duality compares complementary normal layers through the actual socle line and charges torsion defects. Reflection controls increasing odd centered moments and their equality criterion, beyond the final length. The codimension-two Hilbert-drop argument uses the Jordan structure of an annihilator, so it can control specialization without a characteristic-zero representation-theoretic argument. The exact statement is in [R-0032](../results/full_conormal_socle_budget.md).

---

## Source: 2026-10-13-generalization-higher-moment-and-loewy-bounds.md

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

---

## Source: 2026-10-13-generalization-socle-independent-audit.md

# Full conormal socle budget: independent audit and general consequences

Date: begun 2026-10-13, completed 2026-10-14. Status: **PROVED**, conditional
only on the stated smooth-support hypotheses and, when used, the slope
bound (S). This is an independent review of the new mathematics in
`2026-10-13-evening-entirely-thick-rees-progress.md`. Previously accepted
quartic, blowup, saturation, and higher-jet results were taken as inputs;
none of their computations was rerun. No state file is edited.

## 1. Audit verdict and scope

The full conormal-filtration theorem, exact socle line, Frobenius
inequality, defect identity, and balanced-rational equality argument in
Sections 2--7 of the reviewed note are sound. No substantive repair is
needed. The proof correctly permits torsion in intermediate normal
layers, and correctly uses the actual Loewy index of the entire generic
algebra rather than either chosen equation order.

The only clarifications needed for a reusable statement are these:

* For an arbitrary support curve, the real-valued defects need not be
  integers. They are integers in the reviewed C0 specialization.
* The choice lambda = mu_max(N) uses the characteristic-zero symmetric
  slope theorem. The elementary globally generated twist choice works
  in every characteristic and is sufficient for all arguments below.
* Equality gives a globally Gorenstein associated graded algebra on any
  smooth support curve. Its description by a constant algebra requires
  the extra balanced rational normal-bundle hypothesis.

The global STCI problem remains open. These are necessary structure
theorems for a proposed complete-intersection thickening, not an
existence theorem or an unrestricted exclusion.

## 2. Fixed notation

Let C be a smooth integral curve of degree e and genus g in P3, and let
Y = V(F_a,G_b) be a complete intersection with Y_red = C. Put

    J = I_C O_Y,
    n = length O_(Y,eta) = ab/e,
    d = max { j : J_eta^j != 0 },
    L_j = J^j/J^(j+1),
    T_j = torsion(L_j),  B_j = L_j/T_j,
    h_j = rank B_j,
    M = sum j h_j,
    L = e(a+b-4) - (2g-2).

Assume every torsion-free quotient V of Sym^j N_C^* satisfies
deg V >= -lambda j rank V. Write

    delta_j = deg B_j + lambda j h_j,
    t_j = length T_j,
    Delta_j = delta_j + t_j,
    Delta = sum Delta_j,
    Asym = nd - 2M.

All delta_j and t_j are nonnegative. The audited theorem gives

    S = Ann_Y(J) = omega_C tensor O_C(4-a-b),
    J^d = S(-D),  D effective,
    n(lambda d-L) = lambda Asym + 2 Delta.       (1)

Here and below deg D means the degree of the effective divisor; when
writing a numerical identity involving D we use deg D explicitly.

## 3. Equality is global self-duality on every smooth support

Suppose lambda d = L. Then (1) forces Asym = 0 and all delta_j = t_j = 0.
The generic Frobenius inclusions all become equalities, so h_i = h_(d-i)
and the generic associated graded algebra is Gorenstein.

The global multiplication maps induce

    B_i -> B_(d-i)^* tensor J^d.                 (2)

These maps are generically isomorphisms. Their two bundles have the
same degree because deg B_j = -lambda j h_j and J^d = S has degree
-lambda d. Thus their determinants are nonzero sections of degree-zero
line bundles on the smooth proper curve. Every map (2) is an
isomorphism. Hence every pairing

    L_i tensor L_(d-i) -> S

is perfect everywhere on C. The entire associated graded algebra is
therefore a sheaf of graded Gorenstein algebras, with socle line S.

This proves more than generic Hilbert-function symmetry. It controls
all closed support points and gives the intrinsic filtered identities

    Ann_Y(J^i) = J^(d-i+1),  1 <= i <= d.        (3)

To prove (3), take a local section z annihilating J^i. If its first
nonzero normal symbol occurs at index j < d-i+1, the perfect pairing
L_j x L_(d-j) -> S gives a section of J^(d-j), hence of J^i, whose
product with z is nonzero. This is a contradiction.

All O_Y/J^i and J^i are Cohen--Macaulay sheaves of dimension one: their
successive quotients are vector bundles on C. Since Y is Gorenstein,
Cohen--Macaulay duality then also gives

    Hom_Y(O_Y/J^i, O_Y) = J^(d-i+1),
    Hom_Y(J^i, O_Y) = O_Y/J^(d-i+1).             (4)

The second identity follows by dualizing 0 -> J^i -> O_Y -> O_Y/J^i -> 0;
the sheaf Ext^1 of its Cohen--Macaulay quotient into O_Y vanishes.
This standard input is supplied by Stacks Project
[Lemma 47.16.7](https://stacks.math.columbia.edu/tag/0B5A), specialized to
the normalized dualizing complex O_Y[1] locally. Tensoring (4) with
omega_Y yields the corresponding canonical-module formulation.

Neither (3) nor (4) identifies O_Y with an O_C-algebra. A global
retraction Y -> C and splitting of the embedded formal neighborhood
remain separate questions.

## 4. A stronger torsion identity away from numerical equality

Assume only Asym = 0. This is equivalent to the generic associated
graded algebra being Gorenstein. The maps (2) remain generically
isomorphisms between bundles of equal rank h_i = h_(d-i), hence are
injective with torsion cokernel. Let epsilon_i be its length and put
t = sum t_j. Since

    deg J^d = -lambda d + delta_d,
    delta_d = lambda d-L-deg D,

one gets the individual inequalities

    epsilon_i = h_i delta_d - delta_i - delta_(d-i) >= 0.  (5)

Summing (5), and using (1) with Asym = 0, gives the exact new identity

    sum epsilon_i = 2t - n deg D.               (6)

In particular

    2t >= n deg D.                             (7)

If the entire normal filtration is torsion free, t = 0; then D = 0 and
every epsilon_i = 0. Thus (2)--(4) hold globally even when lambda d > L.
This is a support-point obstruction beyond the scalar budget: failure
of the top power to reach the actual socle forces enough intermediate
torsion to pay at least n deg D/2, and additional torsion measures the
degeneracy of the complementary-layer pairings.

For any order-one presentation, the generic algebra has embedding
dimension one, hence is K[z]/(z^n), with d = n-1 and all h_j = 1.
Consequently Asym = 0 automatically and (5)--(7) apply. If all its
normal layers are torsion free, the natural surjections L_1^j -> L_j
are isomorphisms of line bundles; therefore

    L_1^(n-1) = omega_C tensor O_C(4-a-b).

That is a global Picard-group condition, stronger than equality of
degrees. Torsion is precisely where this primitive-multiple-curve
description can break down.

## 5. Entirely thick presentations force exact early layers

Let m >= 2 be the smallest generic order of an element of the local
complete-intersection ideal; equivalently m = min(p,q) for a chosen
generating pair with exact generic normal orders p,q. For 0 <= j < m,
the conormal quotient map has no generic kernel. Its kernel is a
subsheaf of a vector bundle and therefore vanishes globally. Thus

    L_j = Sym^j N_C^*,  0 <= j < m.             (8)

In particular every entirely thick presentation has L_1 = N_C^*,
including at all special support points. If nu = deg N_C / 2, (8) gives

    Delta_j = j(j+1)(lambda-nu),  j < m,
    2 Delta >= [2m(m^2-1)/3] (lambda-nu).        (9)

For characteristic zero, choose lambda = mu_max(N_C). If N_C is
unstable, lambda > nu and the budget has strictly positive compulsory
slack. Numerical equality is possible only when N_C is semistable.
More precisely,

    n(lambda d-L)
       >= lambda Asym + [2m(m^2-1)/3] (lambda-nu).  (10)

This is a general normal-bundle obstruction applying to all degrees
simultaneously. In the balanced C0 case lambda = nu = 7, its compulsory
early-layer contribution is zero, so the ambient extension obstruction
must supply additional information.

## 6. Higher moments and uniform Loewy bounds

The companion independent derivation is in
`2026-10-13-generalization-higher-moment-and-loewy-bounds.md`.
Its elementary Frobenius and generic-linear-parameter arguments give,
in every characteristic over an infinite coefficient field:

* The distribution h_j/n is stochastically dominated by its reflection
  j -> d-j. Every odd central moment is nonpositive, and equality in
  any strictly increasing odd central test forces Asym = 0.
* For codimension-two Artin Gorenstein algebras of initial ideal order
  m, the Hilbert function begins 1,2,...,m and thereafter falls at most
  one at each step. Thus

      d <= n-1-(m-1)^2.                        (11)

The companion proof was independently checked at its delicate step:
both A/xA = K[[y]]/(y^m) and gr(A)/(x*) = K[y]/(y^m) are computed by
restricting the original ideal and its initial ideal separately. It
does not interchange quotient and associated graded without proof.
After generic-linear multiplication is surjective from degree m-1,
Nakayama gives m_A^(i+1) = x m_A^i. Frobenius duality identifies Ann(x)
as one K[y] Jordan block, and its intersections with the powers of m_A
have successive drops at most one. The explicit sharpness family has
the stated three-element standard basis; its rectangle of mixed
monomials plus the pure-y chain gives the claimed Hilbert sequence
without characteristic-dependent coefficients.

There is a stronger sharp moment statement. Put k = n-m^2 >= 0. The
Hilbert distribution at fixed n,m is stochastically dominated by the
sequence

    (1,2,...,m,m-1,...,2,1, followed by k extra ones).

Consequently

    M <= M_max(n,m)
      = m^2(m-1)+2(m-1)k+k(k+1)/2
      = [n(n-1)-(m-1)^2(2n-m^2)]/2.            (11a)

This is sharp in every characteristic, as witnessed by the local CI
(x y^(m-1), x^m+y^N), where N = n-(m-1)^2-m+1 >= m. Combining
Riemann--Roch, 2 Delta = 2 lambda M-nL, with (11a) gives

    nL <= lambda[n(n-1)-(m-1)^2(2n-m^2)].      (11b)

With the normal-bundle instability cost retained, its stronger version
is

    lambda[n(n-1)-(m-1)^2(2n-m^2)]-nL
        >= [2m(m^2-1)/3] (lambda-nu).           (11c)

For all entirely thick C0 presentations, using m >= 2 already yields

    n[4(a+b)-14] <= 7(n^2-3n+4), n=ab/4.     (11d)

When only a lower bound on m is known, the corresponding bound remains
valid: the correction (m-1)^2(2n-m^2) increases on 1 <= m <= sqrt(n).

Combining (11) with (1) gives a degree-independent necessary inequality

    L <= lambda [n-1-(m-1)^2],                 (12)

and combining with (10) yields

    n{lambda[n-1-(m-1)^2]-L}
        >= [2m(m^2-1)/3] (lambda-nu).           (13)

For C0, (12) specializes to

    7ab >= 16(a+b) + 28(m-1)^2 - 28.           (14)

These do not bound degrees uniformly or settle the higher-order branch.
They replace independent degree-by-degree checks with structural tests
of the entire generic algebra and its global normal filtration.

## 7. Continuation boundary

The equality obstruction from the ambient second neighborhood is a
separate new proof being independently reviewed in a companion note.
It must not be folded into the accepted socle-budget theorem without
checking relation lifting and the multiplicity-sensitive coefficient
extraction. The accepted nonzero marked-direction extension class is
used as an input, not recomputed.

The most informative unresolved data away from equality are now the
generic annihilator deficits, the torsion in every normal layer, the
determinant lengths epsilon_i when the generic graded algebra is
Gorenstein, and the degree defects of the first initial-relation bundle.
The structure above preserves all higher normal orders; no tangent-only
multiplicity cap or generic-to-special root comparison has been used.

---

## Source: 2026-10-13-evening-entirely-thick-rees-progress.md

# Entirely thick presentations: full conormal filtration and socle budget

Date: 2026-10-13. Status: **PROVED necessary structure, pending independent
audit**. This note gives a theorem about the entire complete-intersection
thickening, at every normal order. It does not exclude all entirely thick
presentations and does not resolve the STCI problem. No novelty claim is made.

## 1. Reconstructed frontier and retained boundaries

The current audited record is `research/AUDITED_STATE_2026-10-07.md`, updated
through October 12. The characteristic-zero curve

    C0 = [s^4:s^3 t:s t^3:t^4]

has normal bundle `O_P1(7)^2`. Every integral quartic carrier is now excluded
in characteristic zero, with arbitrary mate degree. The unresolved global
branches include higher-degree order-one carriers and entirely thick pairs.

The October 6 independent thick audit proves, for degrees `a,b` and exact
generic normal orders `p,q`, the first blowup restriction

    W = (u,v),
    u = 7ab/4 + 7pq - 4(aq+bp),
    v = ab/4 - pq,
    u >= 0, v >= 0, a >= 3p, b >= 3q.

At `a=3p,b=4q`, its support consists of constant sections and the quadric
residual binary form has at most `min(p,q)` distinct ruling roots. The
entire `a=3p,b=3q` boundary is already excluded by `u<0`.

The branch inventory recovered the live remote branch
`research/entirely-thick-rees-valuation`, commit
`a843888ce15b06247c576f8f717bec6b7ef5a352`, into
`research/validation/2026-10-13-evening-branch-inventory/remote-snapshots/`.
Its October 7 notes contain the generic Noether cluster reformulation,
the relative blowup budget, marked-root countershields, and the proof of
power saturation in degrees `d>=3m`. Direct inspection verified the
quadric exact sequence and the saturation proof in
`2026-10-07-rational-quartic-power-saturation.md`: there is no hidden
ordinary-power correction at or above degree `3m`.

The recovered notes deliberately reject a comparison between generic
exceptional-cycle coefficient and special repeated-root multiplicity.
This note retains that rejection. The higher data used below is the full
`I_C`-adic algebra of the complete intersection, together with its global
dualizing sheaf. It requires neither constant tangent roots nor clean
normalization/conductor hypotheses.

## 2. A theorem for any smooth support curve

Let `C` be a smooth integral projective curve in `P3` over an algebraically
closed field. Write its degree as `e` and genus as `g`. Let

    Y = V(F_a,G_b),  Y_red = C.

The two surfaces have no common surface component. Thus `Y` is a pure
one-dimensional Cohen--Macaulay Gorenstein complete intersection. Put

    J = I_C O_Y,
    A = O_(Y,eta),
    n = length A = ab/e,
    d = max { j : (J_eta)^j != 0 }.

Here `eta` is the generic point of `C`. The integer `d` is the actual
generic Loewy index of the full thickening; it is not the order of either
chosen equation. Write

    h_j = dim_(k(C)) (J_eta)^j/(J_eta)^(j+1),
    M = sum_(j=0)^d j h_j,
    L_j = J^j/J^(j+1).

Let `T_j` be the torsion subsheaf of `L_j` as an `O_C`-module, and
`B_j=L_j/T_j`. Then `B_j` is a vector bundle of rank `h_j`. Torsion in
these quotients is allowed and must be retained.

Choose a positive real number `lambda` such that every torsion-free
quotient `V` of `Sym^j N_(C/P3)^*` satisfies

    deg V >= -j lambda rank V                    (S)

for every `j>=0`. One elementary sufficient choice is `lambda=deg A0`
for a positive-degree line bundle `A0` with `N_C^* tensor A0` globally
generated: all symmetric powers after twisting by `A0^j` are then
globally generated. Thus the theorem has a choice of `lambda` for every
smooth support curve. In characteristic zero the standard slope theorem
also permits `lambda=mu_max(N_C)`; for semistable `N_C`, this is
`deg N_C/2`. The quartic application below uses its explicit split
normal bundle and does not depend on the slope theorem.

Define

    L = e(a+b-4) - (2g-2),
    Delta_j = deg B_j + j lambda h_j + length T_j,
    Delta = sum Delta_j,
    Asym = nd - 2M.

Then all the following hold:

1. `J^(d+1)=0` on all of `Y`.
2. The global socle along the support is the line bundle

       S_C(Y) = Ann_(O_Y)(J)
              = Hom_(O_Y)(O_C,O_Y)
              = omega_C tensor O_C(4-a-b).

3. `J^d` is a line bundle on `C` and there is an effective divisor `D`
   with

       J^d = S_C(Y)(-D).

4. `Sym^j N_C^*` surjects onto `L_j` for every `j`; hence
   `Delta_j>=0`.
5. The generic Gorenstein algebra satisfies `Asym>=0`.
6. The exact global budget is

       n(lambda d - L) = lambda Asym + 2 Delta.   (B)

In particular

       lambda d >= e(a+b-4) - (2g-2).            (N)

The effective top-socle defect is visible more precisely as

       deg D <= lambda d - L.

These assertions are independent of any upper bound on the degrees,
normal orders, or higher contact lengths. They apply equally to thick
and order-one presentations of a smooth support curve.

## 3. Proof: purity and the actual socle

Since `Y` is Cohen--Macaulay of pure dimension one and has only the
irreducible support `C`, the only associated point of `O_Y` is `eta`.
Every subsheaf of `O_Y` supported on finitely many closed points is zero.
The sheaf `J^(d+1)` is generically zero, so it is zero everywhere. This
does not assert that the quotients `L_j` are torsion free: a quotient of
a pure sheaf may have zero-dimensional torsion.

For the finite closed immersion `i:C->Y`, duality gives

    Hom_Y(O_C,omega_Y) = omega_C.

Since `omega_Y=O_Y(a+b-4)` is invertible, tensoring this identity by its
inverse gives the stated socle isomorphism. One can obtain the same
identity by the change-of-rings computation of
`Ext^2_(P3)(O_C,omega_(P3))` through the regular sequence `(F,G)`.
Its degree is

    deg S_C(Y) = 2g-2-e(a+b-4) = -L.

The ideal `J^d` is annihilated by `J`, and thus is a subsheaf of this
socle. The generic Artin algebra `A` is Gorenstein and has a
one-dimensional socle; its nonzero highest power `(J_eta)^d` lies in
that socle and therefore equals it. Consequently `J^d` is a rank-one
subsheaf of the socle line bundle. On the smooth curve it is locally
free and has the form `S_C(Y)(-D)` for an effective divisor `D`.

In particular the Loewy index at the generic point is a global
nilpotency bound, but special points can still contribute precisely
through the torsion of intermediate quotients and through `D`.

## 4. Proof: conormal quotients and Euler characteristic

The regular embedding `C->P3` gives

    I_C^j/I_C^(j+1) = Sym^j N_C^*.

Passing to `O_Y` therefore yields a surjection onto `L_j`. Composing
with `L_j->B_j` and applying (S) shows that

    deg B_j + j lambda h_j >= 0.

This proves `Delta_j>=0`, including the torsion length. For `j=d`,
`L_d=J^d` is torsion free and rank one, so

    -L - deg D = deg J^d >= -lambda d,

which gives the top-socle inequality directly.

Riemann--Roch on the support curve and additivity for the filtration
give

    chi(O_Y)
       = sum_j [deg B_j + length T_j + (1-g)h_j]
       = Delta - lambda M + n(1-g).

The complete-intersection genus formula gives

    chi(O_Y) = -ab(a+b-4)/2 = -ne(a+b-4)/2.

Combining them yields the exact relation

    2 Delta = 2 lambda M - n L.                  (E)

## 5. Proof: a Frobenius inequality retaining all higher jets

Choose a coefficient field in the completed generic Artin algebra; this
has residue field `K=k(C)`. Since `A` is Artin Gorenstein, choose a
`K`-linear functional nonzero on its socle. The multiplication pairing
defined by that functional is perfect. For every ideal `U` of `A`,

    dim_K Ann_A(U) = n - dim_K U.

With `m=J_eta`, the identity `m^(d+1)=0` gives

    m^(d-i+1) subset Ann_A(m^i),

and hence

    dim m^i + dim m^(d-i+1) <= n,  1<=i<=d.

Summing over `i` and using

    sum_(i=1)^d dim m^i = sum_j j h_j = M

gives `2M<=nd`. No symmetry of the Hilbert function was assumed:
the associated graded algebra of an Artin Gorenstein algebra can fail
to be Gorenstein. Formula (B) now follows from (E), with
`Asym=nd-2M>=0`.

This is the first-moment consequence of the classical symmetric
decomposition of a local Artin Gorenstein Hilbert function, but the
short pairing proof above avoids assuming that its individual layers
are symmetric.

## 6. Specialization to C0: an integral defect identity

For `C0`, take `lambda=7`, `e=4`, `g=0`. Then

    n=ab/4,
    mu=7d+14-4(a+b),
    Delta_j=deg B_j+7j h_j+length T_j.

The theorem becomes

    n mu = 7 Asym + 2 Delta,
    mu >= 0,
    0 <= deg D <= mu.                           (C0)

Every `Delta_j` is a nonnegative integer. This couples three genuinely
different measurements of the full thickening:

- its generic nonhomogeneous Gorenstein Hilbert function (`Asym`);
- global degree/torsion defects of all normal layers (`Delta`);
- the actual top socle line and its special-point divisor (`D`).

This is more information than the first blowup cycle. It is still a
necessary condition: large Loewy index is permitted, and the local
families already showing unbounded higher contact remain consistent
with it.

## 7. Equality rigidity: a constant graded Artin algebra

Suppose `mu=0`. The identity forces `Asym=0` and every `Delta_j=0`.
Consequently `T_j=0` and `deg B_j=-7j h_j` for all `j`. The bundle
`L_j(7j)` is a globally generated vector bundle of degree zero on `P1`,
so it is trivial. Thus

    L_j = O_P1(-7j) tensor B_j^0

for constant vector spaces `B_j^0` of dimension `h_j`.

After these twists, every multiplication map has constant coefficients:
it is a map between trivial bundles on the complete connected curve
`P1`. The surjections from `Sym^j N_C^*` also have constant matrices.
Therefore there is a graded Artin quotient `B` of `k[x,y]` with

    gr_J(O_Y) = direct_sum_j O_P1(-7j) tensor B_j.

At the generic point, equality in the summed Frobenius inequalities
forces equality in each individual inequality:

    m^(d-i+1) = Ann_A(m^i),  1<=i<=d.

The resulting pairings

    (m^i/m^(i+1)) x (m^(d-i)/m^(d-i+1)) -> m^d

are perfect. This proves that the associated graded algebra, and hence
the constant algebra `B`, is Gorenstein. In the entirely thick branch,
its embedding dimension is two. A graded Artin Gorenstein quotient of
`k[x,y]` is a homogeneous complete intersection, say of degrees `r,s`.
Thus equality imposes the exact relations

    ab = 4rs,
    d = r+s-2,
    4(a+b) = 7(r+s).                            (R)

The degrees `r,s` are the degrees of generators of the full initial
ideal, not necessarily the normal orders `p,q` of the chosen pair.
For example, a cancellation between chosen equations can expose the
second generator at a higher normal order. Identifying `(r,s)` with
`(p,q)` would discard the very higher-jet phenomenon this theorem
retains.

Equality is therefore a rigid boundary with a constant Gorenstein
normal algebra. This does not imply that the filtered algebra itself
is constant, or that its embedded formal neighborhood splits. Those
would require further extension/embedding arguments.

## 8. Explicit remaining equality data and limitations

The smallest thick degree pair surviving the old scalar inequalities is
`(a,b,p,q)=(6,8,2,2)`. Here `n=12` and the new theorem requires `d>=6`.
If `d=6`, equality forces a constant graded complete intersection of
degrees `(r,s)=(2,6)` and no normal-layer torsion or degree defects.
The alternative factorization `(3,4)` has socle degree five and is
incompatible with `d=6`.

This is an exact dichotomy for the full `(6,8)` thickening:

1. a very rigid constant graded `(2,6)` algebra at Loewy index six; or
2. a higher Loewy index with the defect budget in (C0).

Neither branch is excluded here. At equality the original two quadratic
symbols can be scalar multiples of the same constant quadratic
direction; their scalar coefficients can have complementary zero
divisors. Their cancellation produces the degree-six initial generator.
One must not assume that a global regular change of the original
homogeneous generators realizes that cancellation.

The result supplies no uniform bound on `d` or on `a,b`. It introduces
no tangent-only multiplicity cap, no generic-to-special root comparison,
and no assumption that the graded algebra is Gorenstein away from the
equality boundary.

## 9. Continuation targets

The useful next step is to analyze the full filtered deformation of the
constant graded complete intersection on the equality boundary, or to
bound the allowable global defect `Delta` using actual homogeneous
generation. This is a structural theorem before any computation.

For `(6,8)`, compare the global exact generator filtration

    0 -> O(-42) -> O(-24) + O(-32) -> O(-14) -> 0

suggested by a graded `(2,6)` model, with the actual sextic normal-image
constraints and the global embedded filtered deformation. The exact
sequence is a proposed next bridge, not established in this note.

For larger degrees, retain the entire nonnegative budget rather than
enumerating first symbols: every candidate generic Hilbert function
must satisfy its exact arithmetic, and every special-point repair must
pay the corresponding degree/torsion defect. There is no finite generic
Hilbert-function classification claimed uniformly in the degrees.

## 10. Provenance and standard inputs

The proof above derives the numerical budget and equality statement
directly. Standard inputs were checked against primary sources:

- Stacks Project, [regular immersions, Lemma 31.22.5](https://stacks.math.columbia.edu/tag/0638),
  for the symmetric conormal associated graded of a regular embedding.
- Stacks Project, [Duality for curves](https://stacks.math.columbia.edu/tag/0E31),
  and [finite-morphism duality, Remark 48.20.12](https://stacks.math.columbia.edu/tag/0AX4),
  for the actual socle line via the finite closed immersion.
- Iarrobino and Macias Marques,
  [Symmetric Decomposition of the Associated Graded Algebra of an Artinian
  Gorenstein Algebra](https://arxiv.org/abs/1812.03586), for the literature
  context behind nonhomogeneous Gorenstein Hilbert functions. Its
  symmetric-decomposition theorem is not needed for the elementary
  pairing proof in Section 5.
