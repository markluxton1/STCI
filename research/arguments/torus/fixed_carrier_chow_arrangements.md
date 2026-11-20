# Fixed-carrier Chow arrangements and collisions

**Review, November 20, 2026:** independent review checked the descent
criterion, parameter spaces, collision, reduced-generator bridge and quadric
comparison below.
The statements concern specified toric carriers, rather than arbitrary
complete intersections whose reduced cycle support lies on those surfaces.

## The fixed quartic and its translated sections

Let \(k\) be algebraically closed, of arbitrary characteristic, and put
\[
 A=x_2^4-x_0x_3^3,\qquad X=V(A),\qquad
 C_a=[s^4:a s^3t:st^3:t^4]\quad(a\in k^\times).
\]
Thus \(C_1=C_0\). Write \(h=s^3t\). The
[canonical normalization proof](../arithmetic/positive_characteristic_constructions.md#normalization-and-its-fibers)
gives the finite normalization
\[
 \nu:\mathbf P(1,1,4)\longrightarrow X,\qquad
 [s:t:z]\longmapsto[s^4:z:st^3:t^4],
\]
with homogeneous image ring \(R[z]\), where
\(R=k[s^4,st^3,t^4]\). It is an isomorphism over the dense coordinate
torus; the set-theoretic inverse image of \(C_a\) is \(V(z-ah)\). The
[semigroup calculation](../arithmetic/positive_characteristic_constructions.md#exact-semigroup-and-characteristic-criteria)
says \(h^j\in R\) exactly when \(j\in\langle3,4\rangle\), whose positive
gaps are \(1,2,5\).

## Exact realization by a mate on \(X\)

Fix \(N>0\) and a multiset of \(N\) nonzero scalars, written as distinct
\(a_i\) with positive multiplicities \(n_i\), where \(\sum_i n_i=N\).
Let
\[
 P(T)=\prod_i(T-a_i)^{n_i}
     =T^N+\sum_{j=1}^N c_jT^{N-j}.
\]
Then the following are equivalent:

1. A homogeneous degree-\(N\) form \(G\) gives a proper intersection
   with exact fundamental cycle
   \([V(A,G)]=\sum_i n_i[C_{a_i}]\).
2. \(c_j=0\) for every \(j\in\{1,2,5\}\) with \(j\le N\).

Equivalently, the elementary symmetric functions \(e_1,e_2,e_5\) of the
multiset vanish whenever their index is at most \(N\). When these conditions
hold, the embedded ideal \((A,G)\) is unique: \(G\) is determined modulo
\(A S_{N-4}\) and multiplication by a nonzero scalar, with \(S_d=0\) for
\(d<0\).

**Proof.** A proper complete intersection is pure. Thus its specified
cycle leaves no further projective support of any dimension. Pulling back
\(G\) gives a nonzero weighted homogeneous polynomial whose zero set is
precisely the union of the divisors \(z-a_i h=0\). Unique factorization gives
\[
 \nu^*G=\gamma\prod_i(z-a_i h)^{n_i}
 =\gamma\left(z^N+\sum_{j=1}^N c_jz^{N-j}h^j\right),\qquad
 \gamma\in k^\times.
\]
The exponents equal the cycle multiplicities because the normalization is
an isomorphism over the dense torus, where these divisors are distinct.
Membership in \(R[z]\) is coefficientwise. A nonzero coefficient
\(c_jh^j\) belongs to \(R\) exactly when \(j\in\langle3,4\rangle\), proving
necessity and the descent criterion.

Conversely, descent supplies a homogeneous lift \(G\). Its pullback has
exactly those divisors, so finite surjectivity of \(\nu\) excludes any other
projective support. The polynomial is nonzero on \(X\), so \(A,G\) are
coprime and give a proper complete intersection. The generic lengths are
the exponents \(n_i\). Finally the pullback map on the coordinate ring of
\(X\) is injective, so two normalized lifts differ by an \(A\)-multiple.
This also proves uniqueness. \(\square\)

This statement requires \(A\) as one actual generator. Merely assuming
that another, possibly nonreduced CI has its reduced support on \(X\)
does not put \(A\) in its ideal; that case needs a separate bridge.

Every classified ideal, including repeated cycles, is invariant under the
intrinsic torus of coordinate weights \((0,1,3,4)\): it preserves \(A\)
and each \(C_a\), so uniqueness fixes the ideal. Explicitly, a monomial
lift of \(h^j\) has weight \(j\), so \(G\) can have weight \(N\) while
\(A\) has weight twelve. A non-invariant lift of such a cycle supported
on \(X\) therefore cannot retain \(A\) as an actual generator.

## Parameter space and characteristic dependence

The multiset coordinates identify \(\operatorname{Sym}^N\mathbf G_m\)
with monic degree-\(N\) polynomials having nonzero constant term.
The explicit realization parameter space is the coordinate locus
\(c_1=c_2=c_5=0\), omitting indices larger than \(N\), with \(c_N\ne0\).
It is empty for \(N=1,2,5\); otherwise it is
\[
 \begin{cases}
 \mathbf A^{N-3}\times\mathbf G_m,&N=3,4,\\
 \mathbf A^{N-4}\times\mathbf G_m,&N\ge6.
 \end{cases}
\]
Its dimensions are \(1,2,N-3\), respectively. This coefficient model does
not assert a scheme-theoretic identification with a locus in the full
Chow scheme.

The reduced-cycle locus is the squarefree open subset. It is nonempty in
every characteristic for the allowed degrees \(N=3,4\) or \(N\ge6\),
except \(N=3\), \(\operatorname{char}k=3\).
Indeed \(T^N+d\), \(d\ne0\), is squarefree when the characteristic does
not divide \(N\). If \(p\mid N\), choose \(j\in\{3,4\}\) with \(j<N\)
and \(p\nmid j\). Then \(T^N+cT^{N-j}+d\), with \(c,d\ne0\), has
derivative a nonzero monomial and has no zero root. Such a \(j\) exists for
\(N\ge6\), and for \((N,p)=(4,2)\) take \(j=3\).
For \((N,p)=(3,3)\), every allowed polynomial is \(T^3+d\).

In characteristic zero, Newton's identities rewrite the missing
coefficients as
\[
 \sum_i n_i a_i=\sum_i n_i a_i^2=\sum_i n_i a_i^5=0.
\]
Every realized cycle therefore has at least three distinct components.
One component contradicts the first identity. For two components with
multiplicities \(r,s>0\), the first gives \(b=-ra/s\), and the second gives
\(r(r+s)a^2/s=0\), impossible in characteristic zero. This excludes full
coalescence and every two-support partition on this fixed carrier; it
allows partial collisions involving three or more supports.

For the single-support polynomial \(P(T)=(T-a)^N\), the criterion
recovers the
[existing exact Frobenius degree sets](../arithmetic/positive_characteristic_constructions.md#theorem-and-its-scope):
there is no characteristic-zero mate, while in characteristic \(p>0\)
descent is equivalent to \(p^{v_p(N)}\in\langle3,4\rangle\).

## An actual partial collision in characteristic zero

For \(c\ne-1\), take the proper quartic pair
\[
 A=x_2^4-x_0x_3^3,\qquad
 G_c=x_1^4+c x_0^2x_1x_2-(1+c)x_0^3x_3.
\]
Its normalized polynomial is \(P_c(T)=T^4+cT-(1+c)\), which always has
the root \(T=1\). Generic \(c\) gives four distinct translated components:
squarefreeness is open and holds at \(c=0\). At \(c=-4\),
\[
 P_{-4}(T)=(T-1)^2(T^2+2T+3),
\]
so the actual intersection cycle is
\[
 2[C_0]+[C_{-1+\sqrt{-2}}]+[C_{-1-\sqrt{-2}}].
\]
The remaining roots are distinct, nonzero and different from \(1\).
Thus another translate can collide with \(C_0\) in characteristic zero
inside the proper CI locus. The fixed-carrier obstruction concerns
complete coalescence, rather than an absence of collisions.

The family is flat over \(c\ne-1\): its fibers are proper complete
intersections of fixed type \((4,4)\), so relative regular-sequence
flatness applies. The marked multiplicity of \(C_0\) rises from one
generically, with residual-cycle degree twelve, to two at \(c=-4\), with
residual-cycle degree eight: this is actual marked absorption in a flat
proper-CI family. Throughout the fixed-\(A\), \((4,4)\) translated-arrangement
locus containing \(C_0\), at least three distinct supports force marked
multiplicity at most two and residual degree at least eight, attained here.

## When reduced cycle support supplies the quartic equation

Suppose an arbitrary proper homogeneous pair has reduced fundamental
cycle consisting of distinct \(C_{a_i}\), all on this fixed \(X\).
Then it has type \((4,N)\), up to swapping, and its ideal admits \(A\)
as a minimal generator. Hence the preceding classification applies.

**Proof.** Purity and generic reducedness make the CI scheme the reduced
union \(Y\), so its saturated homogeneous ideal contains \(A\). Order its
generator degrees as \(d\le e\). Since \(A\in I_Y(4)\), \(d\le4\).
There is no linear equation on any \(C_a\). Each \(C_a\) has the unique
quadric \(x_1x_2-a x_0x_3\): the ten quadratic monomials restrict to nine
distinct binary exponents, only \(x_1x_2,x_0x_3\) coinciding.
Distinct parameters therefore have no common quadric. For a single
component, Bézout would force a hypothetical degree-two pair to be
\((2,2)\), requiring two independent quadrics. Thus \(d\ne1,2\).

If \(d=3\), Bézout gives \(4\mid e\). For \(e>4\), membership
\(A\in I_Y(4)\) makes the irreducible quartic \(A\) a multiple of the
cubic generator, a contradiction. Hence \(e=4\), and \(A\), being
independent of cubic multiples, can replace the quartic generator.
If \(d=4<e\), the degree-four generator is a scalar multiple of \(A\);
if \(d=e=4\), a linear change of the generator basis includes \(A\).
These exhaust the possibilities. \(\square\)

The reducedness hypothesis is essential to this bridge. For repeated
cycles, support on \(X\) only implies that some power of \(A\) belongs to
the ideal. Classifying those thickenings is a different realization problem.

## Comparison with the fixed smooth quadric

Put \(Q=V(x_0x_3-x_1x_2)\). In the quotient coordinates of the
[Chow account](../equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle),
the translates lying on \(Q\) have \(u=v\).
They all have the same ruling class \((1,3)\), up to swapping the rulings:
the diagonal maps \(\operatorname{diag}(1,1,u,u)\) preserve each ruling.
By the [canonical quadric argument](../equations/global_equations_and_constructions.md#p-004-why-the-quadric-cannot-be-one-of-two-equations),
a degree-\(N\) mate cuts class \((N,N)\). It cannot have divisor cycle
\(\sum_i n_i[C_i]\), whose class is \((m,3m)\), \(m=\sum_i n_i>0\).
Thus no actual pair \((Q,G)\) has sole support on these translates, in any
characteristic. Any reduced CI union of them would have \(Q\) in its ideal;
nonplanarity forces minimal generator degree two, so \(Q\) could replace
that generator, contradicting the class calculation. Repeated cycle
support alone does not supply this generator bridge.
