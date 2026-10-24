# The projection-center moduli and a characteristic-two outlook

Date: 2026-10-24. Status: **independently audited exploratory observations;
not canonically promoted**. The principal discussion is
over an algebraically closed field of characteristic zero. Section 4 explicitly
changes the characteristic to two. No STCI conclusion, normal-bundle
calculation, or carrier exclusion is asserted or used.

This note supplies the literature and moduli context for the
[projection and automorphism note](2026-10-24-quartic-projection-automorphisms.md)
and the [symmetric-square note](2026-10-24-quartic-symmetric-square-bitangents.md).
The retrieval route was [research/INDEX](../INDEX.md); the earlier
[special-lines investigation](2026-10-24-special-lines-planes-research-note.md)
and its [geometry audit](2026-10-24-special-lines-planes-geometry-audit.md)
are supporting exploratory evidence. The calculations below are independently
reconstructed from the quartic linear system. None of those evidence files
is treated as a promoted canonical result.

The [independent projection audit](2026-10-24-quartic-projection-independent-audit.md)
also checks the moduli statements and the characteristic-two scope.

## 1. Literature checked and the boundary of the comparison

Two primary research sources were inspected, including their relevant text:

1. Alessandro Bernardi, *Normal bundle of rational curves and Waring
   decomposition*, Journal of Algebra 400 (2014), 123–141,
   [author preprint, Section 2.1 and Remark 2.7](https://arxiv.org/pdf/1203.4955#page=3),
   [Proposition 2.8](https://arxiv.org/pdf/1203.4955#page=5).
   The relevant material is the contraction/apolarity convention, the
   catalecticant rank bound on secant varieties, and the criterion for a
   point projection to preserve a smooth curve isomorphically. The paper's
   normal-bundle results are not imported into this investigation.
2. A. V. Isaev, *Duality for binary quartics and ternary cubics arising from
   their Milnor algebras*, Rev. Roumaine Math. Pures Appl. 60 (2015),
   471–480,
   [Section 3, printed pp. 476–477](https://imar.ro/journals/Revue_Mathematique/pdfs/2015/4/5.pdf#page=6).
   The relevant material is the strictly semistable orbit classification,
   the invariant formulas (3.3)–(3.5), and the quotient description. Its
   associated-form duality is not identified with our osculating involution.

These references establish that the surrounding constructions belong to
classical apolarity and binary-quartic invariant theory. We make no novelty
or literature-priority claim for the specialized observations proved here.
The checked text of Isaev is stated over the complex numbers; the elementary
root-orbit arguments and invariant formulas used below work over every
algebraically closed field of characteristic zero.

## 2. Smooth projection centers and their invariant quotient

Let $W=H^0(\mathbf P^1,\mathcal O(4))$. Use the monomial basis
$s^4,s^3t,s^2t^2,st^3,t^4$ of $W$, and its dual coordinates
$[a_0:a_1:a_2:a_3:a_4]$ on $\mathbf P(W^\vee)$. The complete embedding is

\[
\nu_4([s:t])=[s^4:s^3t:s^2t^2:st^3:t^4].
\]

The closed secant variety $\sigma_2(C_4)$ includes tangent lines. Its equation
is the catalecticant cubic

\[
J=\det\begin{pmatrix}
a_0&a_1&a_2\\a_1&a_2&a_3\\a_2&a_3&a_4
\end{pmatrix}=0.
\tag{2.1}
\]

For completeness, the rank-one matrix of a point of $C_4$ shows that every
secant has rank at most two; the closed secant variety is therefore contained
in this cubic. The secant variety is irreducible of dimension three: at the
two endpoints its two tangent lines span a projective three-space, and the
same rank condition persists on an open set of pairs. The determinant is
irreducible. Indeed, as a polynomial in $a_4$ it has coefficient
$a_0a_2-a_1^2$ and constant term
$-a_0a_3^2+2a_1a_2a_3-a_2^3$; these are relatively prime. To see this,
the first is irreducible, while on $a_0=1,a_2=a_1^2$ the second becomes
$-(a_3-a_1^3)^2$, which is not identically zero. The irreducible cubic
hypersurface consequently equals $\sigma_2(C_4)$.

A center outside this variety identifies no two points and kills no tangent
direction. The induced linear system separates every length-two subscheme
of $\mathbf P^1$, which is precisely the very-ampleness criterion for the
map to its projective target to be a closed immersion. Conversely, a
center on a secant or tangent prevents that separation. Hence

\[
U=\mathbf P(W^\vee)\setminus\sigma_2(C_4)=\{J\ne0\}
\tag{2.2}
\]

is the parameter space of point centers yielding embedded smooth rational
quartics. The same projection criterion is Bernardi's Proposition 2.8.

In characteristic zero the alternating form on a two-dimensional vector
space identifies its fourth symmetric power projectively with the dual
fourth symmetric power, with the appropriate binomial factors. Under this
identification a dual-coordinate point can be written as the binary form

\[
f=a s^4+4b s^3t+6c s^2t^2+4d st^3+e t^4.
\]

Reversal and alternating signs in an equivariant self-duality do not change
the following invariant values. Set

\[
I=ae-4bd+3c^2,\qquad
J=ace-ad^2-b^2e-c^3+2bcd.
\tag{2.3}
\]

Thus $J$ is the catalecticant determinant, and the discriminant has the
normalization

\[
\Delta=I^3-27J^2.
\tag{2.4}
\]

The invariant ring in characteristic zero is $k[I,J]$, of generator degrees
two and three; this standard fact and the normalization are recorded in
Isaev, Section 3. Localizing at $J$, its degree-zero subring is

\[
(k[I,J,J^{-1}])_0=k[z],\qquad z=I^3/J^2.
\tag{2.5}
\]

Consequently the good GIT quotient of $U$ is $\mathbf A^1_z$. The statement
is about the coarse invariant quotient. The quotient stack
$[U/\operatorname{PGL}_2]$ retains stabilizers and distinct nonclosed orbits;
it is a more faithful moduli object for the projected embeddings up to
ambient projectivity. That interpretation follows because a projective
equivalence between two embedded quartics restricts to an automorphism of
their parameter lines and hence identifies their four-dimensional
hyperplane systems, and conversely such an identification induces the
ambient projectivity.

## 3. Our center is a special orbit, not a singular projected curve

The subsystem

\[
V=\langle s^4,s^3t,st^3,t^4\rangle\subset W
\]

has annihilator $[0:0:1:0:0]$. Under the characteristic-zero self-duality
its binary form has two double roots, so it belongs to the orbit of
$s^2t^2$. For $f=s^2t^2$, one has $c=1/6$, $I=1/12$, $J=-1/216$,
and therefore

\[
J\ne0,\qquad \Delta=0,\qquad z=27.
\tag{3.1}
\]

The double-double orbit has dimension two and stabilizer the normalizer of
the torus fixing the two root points. It is closed **inside the semistable
locus**, not inside the full projective space: coalescing its two root
points tends to a quadruple-root, unstable form. There is one other strictly
semistable orbit, represented by $s^2(s^2+t^2)$. It has a unique double
root and two simple roots; its dimension is three and its closure contains
the double-double orbit. These are exactly the two orbits specified in
Isaev, printed p. 476. This is the precise meaning of the unique closed
strictly semistable orbit here.

Both representatives have nonzero catalecticant: in the one-double-root
example, $a=1,c=1/6,e=b=d=0$ still gives $J=-1/216$. Thus both yield
smooth embedded projected quartics and both have $z=27$, although their
centers are inequivalent. The coarse quotient is not an orbit
classification at that value. Four distinct roots are stable and are
classified by their unordered root cross-ratios; in $U$ their quotient
values satisfy $z\ne27$. Squarefree centers with $J=0$ are excluded from
$U$ because they lie on the secant hypersurface.

This distinction is the useful moduli lesson: **a multiple root of the
binary form representing a projection center does not imply a singular
projected quartic**. The discriminant detects collisions in the auxiliary
root divisor of the center; the catalecticant detects failed secant and
tangent separation. Our curve lies on a special orbit for the first
notion while remaining in the open embedding locus for the second.

There is also a concise moduli characterization of this orbit. **Our
quartic is the unique projective-equivalence class of smooth embedded
rational quartics in $\mathbf P^3$ with positive-dimensional projective
automorphism group.** Such a curve is nondegenerate: a smooth plane quartic
has genus three. Every such embedding is therefore a point projection of
$C_4$, because its complete degree-four system has dimension five. A binary
quartic with at least three distinct roots has finite stabilizer: its
stabilizer acts on a finite root set, with kernel fixing three points of
$\mathbf P^1$ and hence trivial. With at most two distinct roots, the
possible multiplicity types are $(4)$, $(3,1)$, and $(2,2)$. The first
two have $J=0$ (substitute $s^4$ or $s^3t$ into the catalecticant), so
cannot give an embedding. The remaining type is exactly our orbit.
Restriction of ambient automorphisms to the curve has trivial kernel
and image the center stabilizer, as proved in the projection note, so
this root argument establishes both directions of the characterization.

## 4. Brief characteristic-two outlook

Now let $k$ be algebraically closed of characteristic two. Keep the actual
subsystem $V\subset W$ and its dual center, rather than reducing the
characteristic-zero binary-form identification. The natural identification
$(\operatorname{Sym}^4 E^\vee)^\vee\cong\operatorname{Sym}^4 E$ uses
binomial/factorial normalizations in characteristic zero; in characteristic
two it must be replaced by divided-power language. In particular, a
fourth power $(as+bt)^4$ has only its two endpoint monomials. The literal
binary form $s^2t^2$ is therefore not a valid substitute for the dual center
without a new representation-theoretic argument.

The map $[s:t]\mapsto[s^4:s^3t:st^3:t^4]$ remains a closed immersion:
on $s\ne0$, the coordinate $u=t/s$ itself occurs among the affine image
coordinates, and the reverse chart gives $s/t$. It remains the graph of
$u\mapsto u^3$ on the same smooth Segre quadric. The latter map is separable
in characteristic two, with its two totally ramified endpoints.

Even its subgroup preserving $V$ does not automatically become larger or
nonreduced. For an invertible matrix
$g=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ acting by substitution on $s,t$,
the middle coefficients of the four basis sections are

\[
0,\quad ab\det(g),\quad cd\det(g),\quad0.
\tag{4.1}
\]

Since $\det(g)$ is invertible, the stabilizer in $\operatorname{GL}_2$ is
cut out by $ab=cd=0$. On the open set $ad\ne0$ this means $b=c=0$;
on $bc\ne0$ it means $a=d=0$. These two opens cover the stabilizer,
because $ad+bc$ is invertible. It is therefore the disjoint union of the
diagonal and antidiagonal tori, scheme-theoretically. Passing to scalars
gives the same smooth torus normalizer in $\operatorname{PGL}_2$.

The order-two subgroup $\mu_2$ inside the torus is, however, nonreduced;
its only geometric point is the identity. The characteristic-zero central
element $u\mapsto-u$ specializes to the identity. This collapse is not an
enlargement of the reduced automorphism group.

For the symmetric square, the divisor represented by
$h=\alpha s^2+\beta st+\gamma t^2$ doubles to $h^2$. Its missing middle
coefficient is $\beta^2$. Hence the incidence condition becomes the
nonreduced double line

\[
\mathcal B=V(\beta^2)\subset\mathbf P^2.
\tag{4.2}
\]

The reduced diagonal is $V(\beta)$: over $k$, every quadratic with zero
mixed coefficient is a square. Its parametrization
$[s:t]\mapsto[t^2:0:s^2]$ is inseparable. Thus the polynomial expression
$\beta^2-4\alpha\gamma$ now cuts out a double line, whereas the actual
reduced image of the diagonal in $\operatorname{Sym}^2\mathbf P^1$ is a
line. One must distinguish that image from the characteristic-zero conic
and its scheme-theoretic flat specialization.

For finite $u\ne0$, Hasse derivatives of
$c(u)=(1,u,u^3,u^4)$ span its ordinary order-two jet plane. The latter is

\[
H_u=V(x_3+u^4x_0),\qquad H_u|_C=4c(u).
\tag{4.3}
\]

Indeed, the section is $(z+u)^4$. At either endpoint, the second Hasse jet
drops rank, but the unique contact-four plane still has this limiting
formula. The osculating-plane map has reduced image the line of planes
$Ax_0+Dx_3=0$ and is purely inseparable of degree four onto it. Every point
has contact four, and there are no two distinct double-contact points in
one hyperplane section. These direct identities explain why reducing
$\rho+\rho^{-1}=-4$ cannot preserve the characteristic-zero two-partner
picture. No classification of the nonreduced correspondence or of
positive-characteristic projection moduli is claimed here.

## 5. Review and computational boundary

The new claims submitted for independent review are: the distinction
between the catalecticant and discriminant conditions, the quotient and
two-orbit warning at $z=27$, and the explicit characteristic-two
stabilizer and incidence degenerations. The characteristic-zero orbit
classification and invariant ring are classical literature inputs with
the checked sources above. Equations (2.1), (2.3), (3.1), (4.1), (4.2),
and (4.3) are suitable for exact symbolic replay. Such replay verifies
identities, not the GIT quotient theorem or the completeness of an orbit
classification. No unresolved inference from these statements to STCI
is proposed.
