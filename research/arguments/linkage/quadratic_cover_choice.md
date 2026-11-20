# Choosing a nonsplit auxiliary quadratic cover

## The cover-choice theorem

Work over an algebraically closed field \(k\) of characteristic zero. Put

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,\qquad
q=x_0x_3-x_1x_2,\qquad r=2x_1x_2-x_0x_3,
\]
\[
r_\lambda=r+\lambda q
=(\lambda-1)x_0x_3+(2-\lambda)x_1x_2,\qquad
X_\lambda=V(z^2-r_\lambda)\subset\mathbf P^4.
\]

**Theorem.** For every integral surface \(V(F)\subset\mathbf P^3\)
of degree greater than two, there is a finite set

\[
E_F\subset k,\qquad \{1,2\}\subset E_F,
\]

such that, for every \(\lambda\in k\setminus E_F\), the quadric
threefold \(X_\lambda\) is smooth and \(r_\lambda\) is nonsquare in
the function field of \(V(F)\). Here a quadratic form is interpreted
as the rational function \(r_\lambda/\ell^2\) for any nonzero linear
trivialization \(\ell\); changing \(\ell\) multiplies it by a square.

For every \(\lambda\ne1,2\), the reduced inverse image of \(C\)
consists of the same two curves

\[
D^\pm=[s^4:s^3t:\pm s^2t^2:st^3:t^4],
\]

in coordinates \([x_0:x_1:z:x_2:x_3]\). On the endpoint charts,
with local parameter \(t=x_1/x_0\) or \(t=x_2/x_3\), respectively,
the affine quadratic function \(r_\lambda\) restricts to \(t^4\)
on \(C\).

Thus **general \(\lambda\)** means every parameter in a nonempty
Zariski-open subset of the affine parameter line, depending on the
carrier \(F\). The theorem does not choose one parameter that works
simultaneously for all integral carriers.

### Proof by a reduced pencil fiber

Let \(V=V(F)\). Neither \(q\) nor any nonzero quadratic can vanish
identically on \(V\), since \(F\) is irreducible of degree greater
than two. In particular \(f=r/q\in k(V)\) is defined and nonconstant:
if \(f=c\in k\), then \(F\) divides the nonzero quadratic \(r-cq\).

Choose a linear form \(\ell\) not vanishing identically on \(V\).
On the normalization of \(V\), take the nonempty smooth open subset

\[
U\subset\{q\ne0,\ \ell\ne0\}.
\]

There \(f:U\to\mathbf A^1\) is a dominant morphism. We check that
a general fiber is nonempty and reduced without making assumptions
on the singularities of the carrier or on the pencil's base locus.
The critical locus is the zero locus of \(df\) on the smooth surface
\(U\). Since \(f\) is nonconstant in characteristic zero, \(df\ne0\)
at the generic point. Every positive-dimensional irreducible
component \(Z\) of the critical locus is mapped to a point: the
restriction of \(df\) to \(k(Z)\) is zero, and in characteristic zero
the kernel of \(d:k(Z)\to\Omega_{k(Z)/k}\) is \(k\). Its
zero-dimensional components also have point images. There are only
finitely many such components, hence only finitely many critical
values. Finally, the constructible dense image of \(U\) contains a
nonempty open subset of \(\mathbf A^1\).

It follows that outside finitely many \(c\in k\), the fiber
\(f^{-1}(c)\subset U\) is nonempty and smooth of dimension one:
at each point its equation \(f-c\) has nonzero differential. Choose
an irreducible component and take its closure \(E\) on the normal
surface. Its generic point lies in \(U\), so its divisorial valuation
satisfies

\[
\operatorname{ord}_E(f-c)=1,\qquad
\operatorname{ord}_E(q/\ell^2)=0.
\]

For \(c=-\lambda\) this gives

\[
\operatorname{ord}_E(r_\lambda/\ell^2)
=\operatorname{ord}_E\bigl((q/\ell^2)(f+\lambda)\bigr)=1.
\]

A square has even valuation at every prime divisor, proving
nonsquareness. This argument uses a moving pencil component away
from its base locus; fixed or exceptional divisors contribute no
obstruction to finding that component.

The quadratic form \(z^2-r_\lambda\) has rank five whenever
\(\lambda\ne1,2\), proving smoothness. Finally \(q|_C=0\) and
\(r|_C=s^4t^4\), so the two displayed lifts and the two endpoint
values are unchanged. This proves the theorem.

## Consequence for the same conductor comparison

Suppose an actual proper homogeneous complete intersection

\[
Y=V(F_a,G_b)\subset\mathbf P^3,\qquad Y_{\mathrm{red}}=C,
\qquad 5\le a\le b,
\]

has integral smaller carrier \(F_a\). Choose
\(\lambda\notin E_{F_a}\). Apply the full primary-branch extraction
to \(X_\lambda\times_{\mathbf P^3}Y\), and denote its actual branch
algebra by \(B_\lambda\supset A=S/(F_a,G_b)\). Write
\(J_{\Delta_\lambda}\subset S\) for the inverse image of its conductor,
and \(\delta_\lambda=\ell\Delta_\lambda\).

The proofs of the [full branch extraction and conductor
construction](quadratic_covers_and_conductor_descent.md#6-the-entire-hypothetical-intersection-and-its-separated-branches)
apply verbatim: the cover is smooth, its roots along the generic
point of \(C\) are distinct, the reduced lifts meet only at the two
endpoints, and \(B_\lambda=A+Az\), with \(z^2=r_\lambda\).
In particular all nilpotent structure is retained. By the
[nonsplit onset argument](endpoint_lattice_capacity.md#nonsplit-lower-onset-in-the-same-conductor-quotient),

\[
(J_{\Delta_\lambda})_d=(F_a)_d
\quad\text{if }2d+2<b.
\]

Indeed a boundary form \(h\) supplies \(P\) of degree \(d+1\)
with \(P^2-r_\lambda h^2\in(F_a,G_b)\). Below degree \(b\) the
right-hand side lies in \((F_a)\); unless \(F_a\mid h\), it makes
\(r_\lambda=(P/h)^2\) in \(k(V(F_a))\), contrary to the chosen
cover. Multiples of \(F_a\) already vanish in \(A\).

Put

\[
q_b=\lceil b/2\rceil-1,\qquad
H_*={q_b+2\choose3}-{q_b-a+2\choose3},
\]

where a binomial with upper entry less than three is zero. The
existing canonical complementary Hilbert-function inequality and
the absence of internal h-vector zeros then give

\[
\boxed{\quad
\delta_\lambda\ge
2H_*+(a+b-4)-2q_b+1.
\quad}                                                     \tag{1}
\]

The [conormal-moment upper
bound](endpoint_lattice_capacity.md#an-upper-bound-from-the-conormal-moment)
also applies to this chosen cover. If \(J\) is the nilpotent ideal
of \(C\) in the generic Artin algebra of \(Y\), let

\[
h_i=\dim_{k(C)}J^i/J^{i+1},\qquad
n=\sum_i h_i=ab/4,\qquad M=\sum_i i h_i.
\]

These depend on the actual intersection \(Y\), not on the auxiliary
cover. At either endpoint the fixed completed algebra
\(A_i\) is free over \(k[[t]]\), and

\[
\epsilon_{\lambda,i}=r_\lambda-t^4\in J A_i.
\]

The finite nilpotent square-root expansion and the saturated
annihilator filtration therefore give

\[
\boxed{\quad
\delta_\lambda\le8M-4(n-1).
\quad}                                                     \tag{2}
\]

Equations (1) and (2) constrain the **same chosen-cover conductor**.
Consequently every actual pair under these hypotheses must satisfy
the cover-independent necessary numerical inequality obtained by
placing their right-hand sides in increasing order. Nonsplitting
in the originally selected cover is not an additional restriction
on this use of the moment comparison.

## Scope and remaining capacity gap

The theorem needs no normality or endpoint regularity of the
carrier and does not assume a mate exists. Its degree hypothesis
ensures only that the restricted pencil is nonconstant; the proof
also works for any integral carrier on which \(r/q\) is
nonconstant. Characteristic zero supplies the reduced general
fiber. The conductor application separately requires an actual
supported complete intersection and the hypotheses of the cited
conductor theorems; choosing a cover does not construct such a pair.

Only the endpoint *values on the reduced curve* persist. In the
actual completed algebra,

\[
\epsilon_{\lambda,i}=\epsilon_{0,i}+\lambda q_i,
\]

where \(q_i\) is the affine trivialization of \(q\). Thus actual
\(t\)-divisibilities, coefficient slopes and Smith minors can
change with \(\lambda\). The branch algebras, conductor ideals and
lengths can change as well. Neither a favorable fixed-cover
capacity estimate nor its conductor value transfers merely because
the reduced lifts coincide. No semicontinuity, constancy or
simultaneous favorable endpoint condition is asserted here.

This removes splitting as a coverage restriction for the nonsplit
onset **when the cover may be chosen for each carrier**. It leaves
the local realization problem: an exclusion still needs an upper
bound incompatible with (1) for that same choice. The moment bound
alone supplies no such contradiction for arbitrary pairs. A sharper
comparison must control both actual endpoint capacities as the
pencil varies, or establish a suitable cover-independent bound.
An abstract generic Artin algebra or a favorable first normal symbol
does not supply those actual endpoint lattices. In particular this
deduction does not prove a general sextic exclusion or settle
characteristic-zero STCI.

## Independent review

The integrated proof was independently reconstructed on 2026-11-20:
finite critical values and the odd moving-divisor valuation, the
carrier-dependent exceptional set, the postulation indexing and
complementary Hilbert-function bound, and the conormal-moment comparison
in the same chosen cover. The review retains the integral smaller-carrier
hypothesis in the application and establishes no transfer of the finer
endpoint estimates between covers.
