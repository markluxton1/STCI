# Choosing a nonsplit auxiliary quadratic cover

## The cover-choice theorem

Work over an algebraically closed field \(k\) of characteristic different
from two. Put

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,\qquad
q=x_0x_3-x_1x_2,\qquad r=2x_1x_2-x_0x_3,
\]
\[
r_\lambda=r+\lambda q
=(\lambda-1)x_0x_3+(2-\lambda)x_1x_2,\qquad
X_\lambda=V(z^2-r_\lambda)\subset\mathbf P^4.
\]

**Theorem.** Let \(V=V(F)\subset\mathbf P^3\) be integral, with
\(q|_V\ne0\) and \(r/q\in k(V)\) nonconstant. In particular these
hypotheses hold for every integral surface of degree greater than two.
There is a finite set

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

First, if \(\deg F>2\), neither \(q\) nor any nonzero quadratic
can vanish identically on \(V\). If \(r/q=c\in k\), then \(F\)
would divide the nonzero quadratic \(r-cq\). This proves the
sufficient degree criterion.

Under the intrinsic hypotheses put \(f=r/q\in k(V)\), nonconstant.
In characteristic zero put \(h=f\) and \(P=1\).
In characteristic \(p>2\), write
\[
f=h^{p^e},\qquad P=p^e,
\]
with \(e\ge0\) maximal. This height is finite: a nonconstant rational
function on the projective normalization has a nonzero divisorial
valuation, and \(p^e\) must divide that fixed nonzero integer. Indeed
a rational function with zero divisor on a normal projective variety
is an invertible global regular function and hence constant. Since
\(k\) is perfect, the kernel of the differential on \(k(V)\) is
\(k(V)^p\); maximality therefore gives \(dh\ne0\). The same
nonvanishing holds for \(h=f\) in characteristic zero.

Choose a linear form \(\ell\) not vanishing identically on \(V\).
On the normalization take a nonempty smooth open subset \(U\) where
\(h\) is regular, \(dh\ne0\), and \(q/\ell^2\) is a unit. The
morphism \(h:U\to\mathbf A^1\) is smooth of relative dimension one,
so its image is nonempty and open. Thus outside finitely many
\(c\in k\), the fiber \(h^{-1}(c)\subset U\) is nonempty and
smooth. Choose an irreducible component and take its closure \(E\)
on the normal surface. Its generic point lies in \(U\), so

\[
\operatorname{ord}_E(h-c)=1,\qquad
\operatorname{ord}_E(q/\ell^2)=0.
\]

For \(\lambda=-c^P\) we have \(f+\lambda=(h-c)^P\), giving

\[
\operatorname{ord}_E(r_\lambda/\ell^2)
=\operatorname{ord}_E\bigl((q/\ell^2)(f+\lambda)\bigr)=P.
\]

A square has even valuation at every prime divisor, whereas \(P\)
is odd. The map \(c\mapsto-c^P\) is a bijection on \(k\), so the
excluded parameter set is finite. This proves nonsquareness without
claiming that a general fiber of \(f\) is reduced in positive
characteristic. The argument uses a moving pencil component away
from its base locus; fixed or exceptional divisors contribute no
obstruction to finding that component.

The quadratic form \(z^2-r_\lambda\) has rank five whenever
\(\lambda\ne1,2\), proving smoothness. Finally \(q|_C=0\) and
\(r|_C=s^4t^4\), so the two displayed lifts and the two endpoint
values are unchanged. This proves the theorem.

## Consequence for the same conductor comparison

For the remainder of this account assume characteristic zero.
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

The existing [all-minors estimate](endpoint_lattice_capacity.md#all-minors-capacity-and-a-cyclic-control)
also applies with \(u=0\). Give level \(j\) to
\(h_j\) basis vectors, equivalently to the basis vectors of
\(\operatorname{ann}(J^{j+1})/\operatorname{ann}(J^j)\), and list the
levels \(i_1\le\cdots\le i_n\). These multiplicities depend on the
generic algebra of \(Y\), not on \(\lambda\). Let \(S_k\) be the sum
of the \(k\) largest levels minus the sum of the \(k\) smallest,
with \(S_0=0\). At both endpoints \(\epsilon_{\lambda,i}\in JA_i\),
so
\[
\boxed{\quad
\delta_\lambda\le2\max_{0\le k\le n}(4S_k-2k)
\le2n(n-1).
\quad}                                                     \tag{3}
\]
For the last inequality use \(S_k\le k(n-k)\) and
\(\max_k(4k(n-k)-2k)=n(n-1)\), attained at
\(k=\lfloor n/2\rfloor\).

Equations (1), (2) and (3) constrain the **same chosen-cover
conductor**. Thus the lower bound in (1) must be at most the minimum
of the two upper bounds. Nonsplitting in the originally selected
cover is not an additional restriction on these comparisons.

The [transverse endpoint lemma](endpoint_lattice_capacity.md#transverse-endpoints-throughout-the-cover-pencil)
computes \(\epsilon_\lambda\) on both charts and proves a sharper
limitation: if even one endpoint has a pair member with a nonzero
\(dv\) normal coefficient, its conductor length is \(n(n-1)\) for
every allowed \(\lambda\), already strictly larger than the scalar
lower bound (1). Varying the cover cannot produce a contradiction
from that scalar comparison in this stratum.

## Scope and remaining capacity gap

The theorem needs no normality or endpoint regularity of the
carrier and does not assume a mate exists. Its degree hypothesis
ensures only that the restricted pencil is nonconstant; the proof
also works for any integral carrier on which \(r/q\) is
nonconstant. In odd characteristic a reduced fiber of its maximal
Frobenius root supplies an odd moving valuation instead. The
conductor application above separately assumes characteristic zero,
an actual supported complete intersection and the hypotheses of the cited
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

This removes splitting as a coverage restriction for the nonsplit onset
**when the cover may be chosen for each carrier**. In the characteristic-zero
conductor application, the moment and all-minors bounds supply no
contradiction for arbitrary pairs. For an integral smaller carrier smooth
at both endpoints, the
[two-endpoint calculation](conductor_on_a_smooth_carrier.md#the-two-fixed-endpoints-leave-at-most-one-common-parameter)
now restricts where (1) can yield a contradiction. A dense
open of actual carrier equations passes this scalar comparison in
every allowed cover. From degree six upward, only the parameter
cancelling both first coefficients can give a deficit; for a quintic
there are at most two candidates. Compute the higher coefficients
and test nonsplitting there. A singular endpoint requires its own
full lattice. A [different cover moving the boundary to one general
point](moving_quadratic_covers.md#the-homogeneous-jet-test) tests
the embedded ranks on all hypothetical pairs. Neither comparison proves
a general sextic exclusion or settles characteristic-zero STCI.

## Independent review

The integrated proof was independently reconstructed on 2026-11-20,
including finite Frobenius height, the nonvanishing-differential open and
odd moving valuation, the carrier-dependent exceptional set, and both
uniform capacity bounds on the same chosen-cover conductor. The
transverse-stratum deduction and its strict scalar inequality were also
independently checked in the linked endpoint proof. The cover choice
holds in characteristic different from two; the application retains
characteristic zero and the integral smaller-carrier hypothesis. No
transfer of finer endpoint estimates or positive-characteristic cyclic
determinant equality is asserted.
