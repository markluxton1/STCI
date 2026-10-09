# Reduced singular support and singleton normalization fibers

Date: 2026-10-08. Status: **PROVED HERE**, with an independent audit of
the planar-cubic argument. These are structural necessary conditions;
they do not resolve the unrestricted quartic-carrier or STCI problem.
No canonical frontier file is edited here.

Throughout, k is algebraically closed of characteristic zero. A
quartic means a geometrically integral hypersurface X in P3 unless
another hypothesis is expressly stated. The reduced curve support of
Sing(X) is denoted Sigma. Its degree is distinguished from the degree
of the Jacobian scheme and from the actual conductor scheme.

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

Suppose along C the first-normal equation factors as h times a
nowhere-zero local normal direction. At a point x choose formal
coordinates (z,y,m) with C=(y,m), z a local parameter on C, and that
normal direction represented by m. Then

    F = h(z)*m + a(z)*y^2 + b(z)*y*m + c(z)*m^2
        + terms of (y,m)-order at least three.

The point is singular precisely when h(x)=0. At such a point the
Hessian is

    [ 0      0       h'(x) ]
    [ 0    2a(x)      b(x) ]
    [ h'(x) b(x)     2c(x) ].

If h has a simple zero, the z,m minor has determinant -h'(x)^2,
so the rank is at least two. By section 5, a nonnormal carrier with
a mate must therefore have a **repeated zero of h**. This applies
in both charts of C; multiplicity is unchanged by a nonvanishing
change of frame. In the MF6 e=1 quartic lane h is a section of O_C(8),
but its degree is not needed for the local argument.

At a repeated zero, the remaining rank-at-most-one condition is

    4*a(x)*c(x) - b(x)^2 = 0.

If a contact identity separately gives a(x)=0, this reduces to
b(x)=0. For example this holds on an ordinary triple chart where
a is a multiple of h by a regular scalar. A contact expression
a=Gamma*h/delta does **not** justify that simplification at a zero
of delta unless the completed two-chart contact identity is also
checked. Thus a proposed gcd(h,h',b) filter must retain its defect
points or prove a(x)=0 there. The general homogeneous Hessian-minor
filter in section 5 has no such frame or denominator boundary.

These lemmas reduce possible mates to a precisely specified
singularity/contact locus. They do not yet show that the corresponding
parameter locus is finite, determine it for the unique principal
quartic family, or exclude its surviving fibers.
