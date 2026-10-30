# Large lifting freedom can preserve a fixed quadric residual

October 30, 2026. Investigator: root. Status: **independently reviewed
provisional theorem**, with the
[independent audit](2026-10-30-stci-game-quadric-boundary-audit.md).
The accepted/reviewed equation-freedom formula is an input,
not reproved here. This note supplies a concrete opening construction,
its obstruction, and two general interfaces for the adversarial search.
No canonical mathematical status changes.

## 1. A genuine large family that cannot remove its residual

Work over an algebraically closed field of characteristic zero. Fix
\[
C=C_0=[s^4:s^3t:st^3:t^4],\qquad Q=(q=0),\quad
q=x_0x_3-x_1x_2.
\]
Choose any cubic \(H\in H^0(\mathcal I_C(3))\) not divisible by \(q\).
For \(m\ge1\), put \(d=3m+2\) and take the entire actual source
\[
\mathcal W_H=
H^m\,k[x_0,x_1,x_2,x_3]_2+
H^0(\mathcal I_C^{m+1}(d)).
\tag{1}
\]
The powers are sheaf powers, or saturated homogeneous powers.
For \(m\) even and at least two, \(d\) is an even degree at least eight,
so the pair \((d,d)\) passes the low-degree and degree-divisibility filters.
No claim is made that a generic member is integral or a pair is proper.

The constructive motivation is literal: take
\[
F=f_2H^m+K,\qquad G=g_2H^m+L,
\]
with different quadratic coefficients \(f_2,g_2\) and all available
higher-normal-order corrections \(K,L\). The leading normal forms
have a common factor; their coefficient ratio may be nonconstant on
\(C\), so a constant row subtraction need not cancel them.

Nevertheless, **no two members of (1) can define \(C\) set-theoretically**.
The reviewed [freedom formula](2026-10-28-stci-search-freedom.md) gives
\[
H^0(\mathcal I_C^{m+1}(3m+2))
\subset q\,k[x_0,x_1,x_2,x_3]_{3m}.
\]
Indeed \(3m+2<3(m+1)\), so the next-order source has a forced quadric factor.
Thus every member of \(\mathcal W_H\) belongs to \((q,H^m)\), and
\[
V(q,H)\subset V(F,G).
\]
On \(Q\simeq\mathbf P^1\times\mathbf P^1\), the cubic cuts a divisor
of class \((3,3)\), while \(C\) has class \((1,3)\). It contains \(C\)
exactly once: two copies would leave a negative second ruling degree.
Its residual divisor therefore has class \((2,0)\). This is a nonzero
degree-two cycle of ruling lines, possibly a doubled line, and is
genuine support outside \(C\).

There is a stronger scheme-theoretic consequence for every proper pair:
\[
V(q,H^m)\subset V(F,G),\qquad
[V(q,H^m)]=m[C]+mR_H.
\]
At the generic point of each residual ruling, the quotient by \((F,G)\)
surjects onto the quotient by \((q,H^m)\); both lengths are finite.
Consequently the genuine residual cycle of the proper pair satisfies
\[
\boxed{R\ge mR_H,\qquad \deg R\ge2m.}
\]
If \(R_H\) is a doubled line, its multiplicity is retained in this
inequality. Attainment of the floor is not asserted.

The freedom in \(K,L\) cannot alter this residual because all such
corrections vanish identically on \(Q\). This is an all-parameter
global restriction, not the failure of one sampled equation.

## 2. The asymptotic lesson goes in both directions

Write
\[
D(m)=\frac{5m^3+15m^2+16m+6}{6}.
\]
The same reviewed source calculation gives
\[
\dim H^0(\mathcal I_C^{m+1}(3m+2))=D(m).
\]
Multiplication by \(H^m\) injects the ten-dimensional space of quadrics.
Its intersection with the next-order source consists exactly of
\(qH^m\): the cubic has generic normal order one, so the order increases
precisely when the quadratic vanishes on \(C\), and its only quadratic
equation is \(q\). Consequently
\[
\dim\mathcal W_H=D(m)+9.
\]
The full individual equation source has
\[
\dim H^0(\mathcal I_C^m(3m+2))
=D(m)+(m+1)(5m+9).
\]
Hence the excluded fixed-\(H\) family occupies a fraction of vector-space
dimension tending to one, while remaining a proper subspace of positive
codimension for every \(m\). This does not mean that it contains a
generic form or is exhaustive.

The family is not excluded merely because it has no proper pairs.
It has no fixed surface: it contains \(H^mS_2\) and
\(q^{m+1}S_m\), whose common fixed factor is one because \(q\nmid H\).
Over the infinite ground field, a generic second member avoids all
surface factors of a fixed nonzero first member. The proper-pair
locus is therefore nonempty. The quadratic leading coefficients can
also be chosen independent modulo \(q\), so every nonzero scalar
pencil member can retain exact normal order \(m\).

The floor \(2m\) grows with degree, but its ratio to
\((3m+2)^2\) tends to zero. It is not a uniform positive gap in contact
score, and it does not imply a floor for arbitrary sources.

There is a complementary warning for non-existence. The source excluded
by the [weighted-subalgebra line theorem](2026-10-30-weighted-subalgebra-line-obstruction.md)
at degree \(3m\) has dimension asymptotic to \(m^2/4\), whereas the
full \(H^0(\mathcal I_C^m(3m))\) has dimension \(D(m)\sim5m^3/6\).
Its relative dimension is asymptotic to \(3/(10m)\), tending to zero.

Thus an all-degree family theorem need not asymptotically exhaust the
actual source, and a very large actual lifting space need not be able
to repair a fixed global boundary. Neither team may use a raw dimension
count as a substitute for the paired equations and full support test.

## 3. A necessary row-operation restriction on any hypothetical pair

Suppose actual homogeneous \(F_a,G_b\) define \(C\) set-theoretically
in characteristic zero, with \(a\le b\).
For every actual polynomial \(A\) of degree \(b-a\), the nonzero form
\[
G_b+A F_a
\tag{2}
\]
cannot have generic normal order greater than \(b/3\).
Otherwise the reviewed fixed-factor formula forces a factor \(q\)
(or forces the form to be zero when its order is too high even for a
nonzero section). A zero form in (2) makes the pair improper.
In the nonzero case
\[
V(F_a,q)\subset V(F_a,G_b+A F_a)=V(F_a,G_b).
\]
The accepted quadric-carrier exclusion and factor reduction say that
\(V(F_a,q)\) cannot have reduced support just \(C\) in characteristic zero.
This contradicts sole support. The corresponding restriction applies
after any mate-preserving homogeneous triangular row operation.

In particular, for equal-degree pairs, no nonzero scalar pencil member
may cross this normal-order threshold. This is a necessary condition
on all actual hypothetical pairs, not only (1).

The missing universal implication is substantial: large generic contact
does not automatically produce such a representative by **actual global
polynomial** row operations. Formal standard-basis cancellation can use
coefficients in \(k(C)\) with poles. No such globalization is proved here.

## 4. A common global interface for the next construction and exclusion

For actual forms not divisible by \(q\), factor their restrictions on
the smooth quadric as divisors
\[
F_a|_Q=C^{u}A_Q,\qquad G_b|_Q=C^{v}B_Q,
\]
where \(u,v\) are their exact vanishing orders on \(C\) **inside \(Q\)**,
and
\[
[A_Q]=(a-u,a-3u),\qquad [B_Q]=(b-v,b-3v).
\]
These orders need not equal the ambient normal orders.
Sole support forces the entire common zero support of \(A_Q,B_Q\)
to lie on \(C\), with no common residual curve outside \(C\).
When the two residual divisors have no common component their total
intersection degree is
\[
(a-u)(b-3v)+(a-3u)(b-v).
\]
The problem is to concentrate that full intersection on \(C\), then solve
the remaining ambient contact and support conditions.

This is the constructive response to the fixed-\(H\) failure: choose
global restrictions whose residual factors do not share the fixed
ruling divisor, or move to degrees where next-order lifts can change
the quadric restriction. The obstruction program can independently
seek uniform bounds on this concentration or classify more residual
configurations. Neither response is yet an existence or non-existence
proof for arbitrary pairs.
