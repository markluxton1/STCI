# Projection-center moduli and the exact characteristic-two comparison

The projection center and its binary-form avatar are distinct in small characteristic. The catalecticant tests embedded smoothness, whereas the discriminant tests collisions of the auxiliary center roots. The full calculation below retains two inequivalent smooth projected curves with the same coarse quotient value and gives the literal characteristic-two stabilizer and Hasse contact maps. It is independently reviewed exploratory geometry, not an unrestricted STCI statement.

## 1. Literature checked and the boundary of the comparison

The classical inputs are [Bernardi, *Normal bundle of rational curves and Waring decomposition*, J. Algebra 400 (2014), §2.1, Remark 2.7 and Proposition 2.8](https://arxiv.org/pdf/1203.4955#page=3), for apolarity, catalecticant secant rank, and smooth projection-center criteria; and [Isaev, *Duality for binary quartics and ternary cubics arising from their Milnor algebras*, Rev. Roumaine Math. Pures Appl. 60 (2015), §3](https://imar.ro/journals/Revue_Mathematique/pdfs/2015/4/5.pdf#page=6), for the strictly semistable orbit quotient and invariants (3.3)–(3.5). Neither Bernardi's normal-bundle results nor Isaev's associated-form duality is being imported as an osculating-involution theorem. Isaev works over \(\mathbf C\); the elementary root-orbit arguments below apply over algebraically closed characteristic-zero fields. No priority claim is made for these classical constructions.

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


The positive-characteristic STCI constructions for the fixed curve are proved [separately](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier); no binary-form orbit classification is substituted for that construction.



## Consolidated historical supplement: `research/supplements/QUARTIC_SINGULAR_SUPPORT_AND_SINGLETON_FIBERS.md`

# Reduced singular support and singleton normalization fibers

Let k be algebraically closed of characteristic zero. A quartic here means
a geometrically integral X in P3, and Sigma denotes the **reduced curve
support** of Sing(X), not its Jacobian or conductor scheme. The first
three propositions apply to any such quartic. The singleton-Hessian
argument applies to an integral hypersurface surface at its stated local
hypotheses; the conductor-contact consequence applies to a smooth integral
curve along which the carrier is generically regular. Only the final MF6
application specializes to fixed C0. These independently accepted bounded
statements distinguish reduced support from thick schemes; they do not
establish a general residual component or an unrestricted STCI obstruction.

## 1. The reduced curve support has degree at most three

**Proposition.** For an integral quartic X, deg(Sigma) <= 3. If X is
nonnormal, Sigma is nonempty, so 1 <= deg(Sigma) <= 3.

Choose a general plane H. Bertini irreducibility makes Y=X intersect H
geometrically irreducible; Bertini smoothness on X_reg makes Y smooth
at its generic point. The plane hypersurface Y is Cohen--Macaulay, so
irreducibility plus generic reducedness makes it integral. The plane
can simultaneously avoid the isolated singular points of X, the
finitely many singular points and component intersections of Sigma,
and be transverse to every component at each point of H intersect
Sigma. Consequently H intersect Sigma consists of exactly deg(Sigma)
distinct geometric points. For the Bertini inputs, see the primary
[Stacks irreducibility theorem](https://stacks.math.columbia.edu/tag/0G4C)
and [smoothness theorem](https://stacks.math.columbia.edu/tag/0FD4).

Every one of those points is singular on Y: all ambient first
derivatives of its quartic equation vanish there, hence the two plane
derivatives vanish. Let nu_Y:Y_tilde -> Y be the finite normalization.
The exact sequence

    0 -> O_Y -> (nu_Y)_* O_Y_tilde -> T -> 0

has T of finite length, with length at each singular point at least
one. (An integral curve over this perfect field is regular exactly
where it is normal.) Both proper integral curves have H0=k. Taking
Euler characteristics gives

    p_a(Y) = g(Y_tilde) + length(T).

The arithmetic genus of a plane quartic is three, directly from
0 -> O_P2(-4) -> O_P2 -> O_Y -> 0. Hence

    deg(Sigma) <= length(T) <= 3.

An integral hypersurface is S2. If it were regular in codimension one,
Serre's criterion would make it normal. Thus a nonnormal quartic has a
singular curve component. This proves the lower bound.

If deg(Sigma)=3, the same proof gives g(Y_tilde)=0 and exactly delta=1
at each of the three general singular section points. It does not
identify the global normalization, classify special fibers, or bound
the degree of the Jacobian scheme.

**Irreducible-support corollary.** If Sigma is irreducible of degree
three, it is a smooth twisted cubic. Section 2 excludes the planar
case. For a nonplanar integral degree-three curve, pull O(1) to the
smooth normalization Z. The resulting line bundle L has degree three
and at least four independent sections, since the four ambient
coordinates are linearly independent on a nondegenerate curve. If Z
had positive genus, every effective divisor of degree d>0 would have
h0 at most d: h0(O_Z(p))=1 for any point p (a second section would give
a degree-one map to P1), and adding the other d-1 points increases h0
by at most one each. A nonzero section of L supplies such a divisor,
contradicting h0(L)>=4. Hence Z=P1, L=O(3), and the four coordinates
give the complete degree-three embedding. The image is consequently
a smooth twisted cubic. Reducible degree-three support is not covered
by this irreducible corollary.

## 2. Every reduced planar cubic singular support is impossible

**Proposition.** If a quartic form F has all its first derivatives
vanishing on a reduced planar cubic C, then its plane equation divides
F. More precisely, after writing the plane as z=0 and its squarefree
cubic equation as g(x0,x1,x2)=0, one has

    F = z (lambda*g + z*Q2).

In particular an integral quartic cannot have such a cubic in its
singular support.

Write

    F = A4(x0,x1,x2) + z*B3(x0,x1,x2) + z^2*Q2(x0,x1,x2,z).

Support containment gives g|A4, g|partial_i(A4) for i=0,1,2,
and g|B3 from the normal derivative partial_z F. If an irreducible
factor q of g occurs only once in a nonzero A4=q*a, choose a nonzero
partial_i q. Its degree is smaller than deg(q), so q does not divide
partial_i q. Reducing partial_i A4 modulo q gives

    partial_i A4 = (partial_i q)*a mod q,

which is nonzero in the domain k[x0,x1,x2]/(q), a contradiction. Each
factor of the squarefree g therefore occurs at least twice in A4.
Thus g^2|A4; degree six exceeds degree four, so A4=0. Since g and B3
have the same degree, B3=lambda*g, giving the displayed formula.

This treats irreducible cubics (including singular cubics), a conic
and line, and three distinct lines with any planar arrangement. It
also gives the ordinary-ideal certificate

    F in (z^2,z*g)_4 = (I_C^2)_4.

No symbolic-power equality or unproved absence of embedded primes is
needed. A repeated or embedded thickening of the Jacobian scheme does
not affect the support-based proof. A **nonreduced degree-three plane
scheme whose reduced support has degree one or two** is outside this
cubic assertion. In particular, a Jacobian scheme of degree three is
not itself evidence of a reduced planar cubic.

The subagent planar_cubic_audit supplied a separate complete factor
argument and reached the same exact formula. Agreement supplements
the written proof; it is not substituted for it.

### Complete reduced degree-three support list

**Corollary.** If the reduced singular curve support Sigma has degree
three, it is connected and nonplanar. Its underlying reduced curve
has one of exactly four forms:

1. A smooth twisted cubic.
2. A smooth plane conic together with a line outside its plane,
   meeting the conic.
3. A chain of three lines, with the two endpoint lines skew.
4. Three concurrent lines spanning P3.

This is a list of possible reduced supports, not an existence claim
for quartics realizing every entry, and not a conductor-scheme
classification.

Nonplanarity follows from the proposition above. The irreducible case
is the corollary in section 1. An irreducible degree-two component is
a smooth plane conic: normalization and the degree-two line-bundle
section bound exclude a nondegenerate embedding in P3, and a reduced
integral plane conic is smooth over this field. Thus the only other
degree partitions are a conic plus a line, or three distinct lines.

Suppose a line L is disjoint from a conic K in its plane P. Double
vanishing of F on the reduced conic gives

    F|P = lambda*q2^2,

by the same irreducible-factor derivative proof used above. The line
cannot lie in P, and its intersection p with P is off K. Since
F(p)=0, lambda=0 and P divides F, contradicting integrality. Therefore
the conic-plus-line case is connected. If the line also lay in the
conic's plane, their union would be the forbidden planar cubic.

For three lines, if one pair intersects and the third is disjoint
from that pair, let P be the plane of the intersecting pair and let
q2 be their squarefree degree-two product. Again F|P=lambda*q2^2.
The third line meets P at a point off the pair, forcing lambda=0 and
a plane factor. Thus this disconnected case is impossible.

If the three lines are pairwise skew, put them by a projective change
of coordinates into

    L1: x2=x3=0,
    L2: x0=x1=0,
    L3: x2=x0, x3=x1.

They lie on the smooth quadric Q: x0*x3-x1*x2=0, and they are in the
same ruling. The restriction of the quartic to Q has class (4,4).
Because F and all its first derivatives vanish on each line, its
restriction vanishes to order at least two along each line. If this
restriction were nonzero, subtracting those three doubled ruling
lines would give a section of O_Q(-2,4), which has no sections.
Therefore Q divides F, another contradiction. This removes the last
disconnected three-line case.

Connected nonplanar three-line arrangements are precisely a chain
with skew endpoints or three concurrent lines spanning P3. Three
pairwise intersecting lines with three distinct intersection points
are a planar triangle and were already excluded. This exhausts the
list. The independent planar_cubic_audit subagent checked the
disconnected cases, the smooth-quadric restriction, and the line
incidence exhaustion without finding a gap.

## 3. The Jacobian scheme can have larger degree

For a concrete distinction, take

    F = x^2*z^2 + y^3*w.

This quartic is integral: viewed as a polynomial in w it is primitive
and linear over k[x,y,z], with coprime coefficients y^3 and x^2*z^2;
Gauss's lemma gives irreducibility. Its derivatives give the Jacobian
ideal, up to nonzero constants,

    (x*z^2, y^2*w, x^2*z, y^3).

The reduced singular support is the union of the two lines
(x,y)=0 and (y,z)=0, of degree two. At the first line's generic point,
z and w are units and the Jacobian ideal is (x,y^2), of length two.
At the second, x and w are units and it is (z,y^2), also of length two.
Thus the one-dimensional Jacobian scheme has degree four. Embedded
points, if present, do not change this leading degree computation.
The degree-at-most-three theorem must not be applied to that scheme.

## 4. A nonnormal singleton-fiber surface point has Hessian rank at most one

**Local proposition.** Let x be a closed point of an integral
hypersurface surface X over k, and let nu:S -> X be its finite
normalization. If X is nonnormal at x and nu^{-1}(x) has exactly one
point, the rank of the local hypersurface Hessian at x is at most one.

Suppose instead that the rank is at least two. Formal splitting in
characteristic zero puts the completed local equation into the form

    u*v + g(w),  g in k[[w]].

One can obtain this with the formal implicit function theorem for two
variables with invertible quadratic Hessian block, followed by the
formal Morse lemma with parameter w. This uses a formal coordinate
change and multiplication by a unit; it does not require convergent
or analytic coordinates. A primary precise statement allowing
non-isolated singularities is [Greuel--Pfister, The Splitting Lemma in
any Characteristic, Theorem 2.1(2)](https://arxiv.org/html/2507.17078v2).
If g is nonzero, its derivative is also
nonzero. The hypersurface is Cohen--Macaulay and its singular support
is isolated (the derivatives are v,u,g'(w)). It is therefore normal
by S2+R1. Normality of the completion descends along the faithfully
flat map to the completion, so X is normal at x, a contradiction.

If g=0, the completed ring is

    A_hat = k[[u,v,w]]/(u*v),

with two nonzero zero divisors u and v. Set A=O_X,x and let B be its
finite normalization algebra. The singleton fiber means B has just
one maximal ideal, so it is a local normal ring. Rings essentially
of finite type over a field, their localizations, and finite algebras
over them are excellent. Exact completion of the finite injection
A -> B gives an injection

    A_hat -> B tensor_A A_hat = B_hat.

Here completion at the maximal ideal of B agrees with completion at
m_A*B because the two adic topologies are equivalent for a finite
local algebra. The completed local ring B_hat is normal, hence a
domain. A ring with the displayed nonzero zero divisors cannot inject
into a domain. This is the required contradiction. The exact
excellence inputs are [Stacks Proposition 15.53.3 and Lemmas
15.53.2](https://stacks.math.columbia.edu/tag/07QS) and the precise
[normal-completion Lemma 15.53.6](https://stacks.math.columbia.edu/tag/0C23).

This argument avoids treating formal branch counting as automatically
equal to normalization fiber counting, and avoids any unqualified
claim that normalization commutes with arbitrary completion.

At a singular point, Hessian rank is invariant under regular or
formal coordinate changes and multiplication of the equation by a
unit. For a homogeneous equation, Euler's identity places the radial
vector in the Hessian kernel once all first derivatives vanish.
Thus the rank of the homogeneous four-variable Hessian at a
projective representative equals the rank of the three-variable
Hessian in any affine chart.

## 5. A mate forces a conductor intersection with Hessian rank at most one

**Global proposition.** Let X be an integral nonnormal hypersurface
surface in P3 and C a smooth integral projective curve in X, with X
regular at the generic point of C. If a hypersurface mate cuts out C
set-theoretically on X, then some point x in C where X is nonnormal
has Hessian rank at most one.

Let G be a mate and b its degree, with nu:S -> X the finite
normalization and H=nu^*O_X(1), an ample Cartier divisor. The full
inverse support of C is the support of the nonzero effective Cartier
divisor defined by nu^*G. Because nu is an isomorphism at the generic
point of C, there is just one curve c above C. Its finite birational
map to the smooth curve C is an isomorphism. The zero support of a
nonzero section of a line bundle on a normal surface is pure of
codimension one, so no isolated inverse-image point can remain.
Hence

    (nu^{-1}(C))_red = c,  nu|c:c -> C is an isomorphism,
    div(nu^*G) = m*c linearly equivalent to b*H

for a positive integer m. In particular every fiber over C is a
singleton. When deg(X)=deg(C)=4, intersecting with H gives m=b.

Since X is an S2 nonnormal hypersurface, its nonnormal locus contains
a curve. Choose a prime curve D on S in the inverse image of that
locus. It is distinct from c, since X is regular at the generic point
of C. Restrict the section defining m*c to D. It is a nonzero section
of O_D(b*H), which has positive degree by ampleness. It must have a
zero: pull the restricted section to the smooth normalization of
the integral curve D, where this is the ordinary positive divisor
degree statement. Therefore c intersects D, even if S is singular at that
intersection and even if c is only a Weil divisor: m*c is Cartier,
which is all the restriction argument uses.

The image x of such an intersection is nonnormal on X and has a
singleton normalization fiber. Section 4 now gives Hessian rank at
most one. No smoothness hypothesis on the normalization, no ADE
assumption, and no reducedness hypothesis on the conductor is used.
Here singleton means a singleton underlying set; no assertion that
the finite scheme fiber is reduced is needed. The independent
planar_cubic_audit subagent also audited sections 4--6, including the
finite-algebra completion topologies and the Cartier restriction,
and found no substantive gap.

Consequently, an exact computation showing that C has **no** singular
point of X at which all two-by-two Hessian minors vanish excludes a
mate in every degree. The condition is necessary; the existence of
a rank-at-most-one point does not establish a mate.

## 6. First-normal consequences and the defect-chart boundary

At a point of \(C=(y,m)\) with local curve parameter \(z\), suppose the first normal equation is \(h(z)m\). Then
\[
F=h(z)m+a(z)y^2+b(z)ym+c(z)m^2+O((y,m)^3).
\]
The carrier is singular there precisely when \(h=0\). Its Hessian at a zero of \(h\), in coordinates \((z,y,m)\), is
\[
\begin{pmatrix}0&0&h'\\0&2a&b\\h'&b&2c\end{pmatrix}.
\]
A simple zero gives the nonzero minor \(-(h')^2\), contradicting the rank-at-most-one condition from §5 for a nonnormal carrier with a mate. Thus **\(h\) must have a repeated zero**, invariant under regular normal-frame changes. At such a zero the additional rank condition is \(4ac-b^2=0\). It reduces to \(b=0\) only when an independently established contact identity gives \(a=0\). In particular \(a=\Gamma h/\delta\) cannot be specialized at a zero of \(\delta\) without a completed two-chart identity. A proposed \(\gcd(h,h',b)\) filter must therefore retain all defect points; the homogeneous Hessian-minor test has no such denominator restriction.

These are necessary singularity/contact conditions, not a finite-locus theorem or an exclusion of surviving quartic fibers. The reduced plane-section degree bound does not bound a thick Jacobian scheme. The singleton-fiber Hessian argument uses characteristic-zero formal splitting and actual finite normalization; in positive characteristic its separability and coefficient hypotheses require fresh verification. The [positive-characteristic construction](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) remains valid.
