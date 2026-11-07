# Smooth rational quartics in positive characteristic: cuspidal projection and descent

Let the ground field be algebraically closed of characteristic p>0. This chapter owns the full family-wide construction for every smooth nondegenerate rational quartic, fixed-degree constructibility, and exact mate degrees on the standard and nonclassical cusp carriers. It is not restricted to the monomial embedding; nor does it give global minimum defining degrees. The characteristic-free geometry is proved in [the foundations](../synthesis/global_equations_and_constructions.md); the smaller fixed-model quartic-carrier constructions are in [their own proof home](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md). These are inherited reviewed proofs.

## Universal rational-quartic construction (P-012): every smooth rational quartic is an STCI in positive characteristic

Let \(k\) be algebraically closed of characteristic \(p>0\), and let
\(C\subset\mathbf P^3_k\) be a smooth nondegenerate rational quartic. By
P-002 it has type \((1,3)\) on a smooth quadric. One ruling therefore induces
a degree-three morphism

\[
 f:C\simeq\mathbf P^1\longrightarrow\mathbf P^1.
\]

We first produce an internal cuspidal projection. If \(f\) is separable, the
different has degree four by Riemann--Hurwitz, including in the wild
characteristic-two case, so some ruling line cuts \(C\) in \(2R+P\) or in
\(3R\). If \(f\) is inseparable, necessarily \(p=3\), its inseparable degree
is three and every geometric fiber is \(3R\). If the chosen fiber is
\(2R+P\), project from \(P\). If it is \(3R\), project from \(R\), regardless
of whether \(f\) is separable.

Hyperplanes through the center, after removing their simple base point on
\(C\), give a basepoint-free three-dimensional subspace of
\(H^0(\mathbf P^1,\mathcal O(3))\). The associated map to
\(\mathbf P^2\) cannot have a line as image, since that would put \(C\) in a
plane. Its degree formula therefore shows that it is birational onto a plane
cubic.

The normalization map is not immersive at \(R\). In the \(2R+P\) case this
is the usual projection from a point on a line tangent to \(C\) at \(R\). In
the \(3R\) case, put the center at the affine origin and write

\[
 \gamma(u)=uv_1+u^2v_2+O(u^3).
\]

Triple contact with the ruling line means \(v_2\in kv_1\). After canceling
the simple base factor, the projected map is
\([v_1+uv_2+O(u^2)]\), whose derivative is the class of \(v_2\) modulo
\(kv_1\), hence zero.

Its fiber over that image is a singleton. For \(2R+P\), any further preimage
would lie on the line \(PR\), while the extended image of the center \(P\) is
its tangent direction and differs from \(PR\) because \(P\) occurs with
multiplicity one. For \(3R\), another preimage would lie on the same ruling
line, whose intersection with \(C\) is supported only at \(R\). Finally,
\[
 p_a(\text{plane cubic})-g(\mathbf P^1)=1,
\]
so the nonimmersive unibranch image at \(R\) accounts for the entire
\(\delta\)-invariant. It is the unique singularity and is a cusp rather than
a node.

Choose coordinates so the center is \([0:0:0:1]\), and let \(X\) be the cubic
cone over the projected cubic. In characteristic different from three the
cuspidal cubic has normalization

\[
 [s:t]\longmapsto[s^3:s^2t:t^3],
\]

and in characteristic three it has the possibly nonclassical normal form

\[
 [s:t]\longmapsto[s^3:s^2t:t^3+\alpha st^2].
\]

To see these normal forms, put the cusp preimage at \(s=0\) and its image at
\([0:0:1]\). Nonimmersion makes the first two pulled-back coordinates vanish
to order at least two; their span is
\(\langle s^3,s^2t\rangle\). Subtracting their multiples from the third
coordinate leaves \(t^3+\alpha st^2\). When \(3\ne0\), the substitution
\(t\mapsto t+\alpha s/3\), followed by target row operations, removes the
\(st^2\) term. This includes characteristic two. Thus \(X\) is defined
respectively by

\[
 Y^3-X^2Z=0
\]

or, in characteristic three, by

\[
 Y^3+\alpha XY^2-X^2Z=0.
\]

Let

\[
 \nu:\mathbf P(1,1,3)\longrightarrow X
\]

be the finite normalization, with weighted coordinates \(s,t,z\), given by
\([s^3:s^2t:t^3:z]\) in the first case and by
\([s^3:s^2t:t^3+\alpha st^2:z]\) in the second. The induced graded map is
finite: \(s,t\) satisfy monic cubic equations over the standard cusp ring,
and in characteristic three \(t\) satisfies
\[
 T^3+\alpha sT^2-Z=0
\]
after adjoining \(s\). It is birational, since on \(X\ne0\),
\[
 t/s=Y/X,\qquad z/s^3=W/X.
\]
Its geometric fibers are singletons: away from the vertex the cusp point
determines its unique normalization point and the fourth coordinate determines
\(z\) up to weighted scaling; the vertex has unique preimage
\([0:0:1]\). Thus the finite normalization is radicial and surjective, hence a
universal homeomorphism.

The three projected coordinates of the original quartic have a common linear
factor \(l(s,t)\), the point used as the projection center. Write its fourth
coordinate as a quartic \(h(s,t)\). Since the original map is defined at the
center \(P=(l=0)\), one has \(h(P)\ne0\). On
\(\mathbf P(1,1,3)\setminus\{[0:0:1]\}\), the set-theoretic inverse image of
\(C\) is the graph \(z=h/l\); there is no point over \(l=0\), and its closure
adds exactly the weighted vertex. It is the weighted degree-four hypersurface

\[
 D=(\phi=0),\qquad \phi=lz-h.
\]

Suppose first that \(p\ne3\). Put

\[
 R_0=k[s^3,s^2t,t^3].
\]

A binary monomial whose total degree is divisible by three belongs to \(R_0\)
unless its \(s\)-exponent is one. In characteristic \(p\),

\[
 \phi^{3p}=(l^pz^p-h^p)^3.
\]

Every binary coefficient in this expansion is the \(p\)-th power of one of
\(l^3,l^2h,lh^2,h^3\). Its total degree is divisible by three, while all of
its \(s\)-exponents are multiples of \(p\); because \(p\ge2\),
none can equal one. Hence

\[
 \phi^{3p}\in R_0[z].
\]

It has weighted degree \(12p\), so it descends through \(\nu\) to an ordinary
homogeneous form \(G\) of degree \(4p\) on the cubic cone.

In characteristic three put

\[
 R_\alpha=k[s^3,s^2t,t^3+\alpha st^2].
\]

Writing \(X=s^3,Y=s^2t,Z=t^3+\alpha st^2\), direct expansion gives

\[
 s^3t^6=XZ^2+\alpha Y^2Z+\alpha^2XYZ-\alpha^3Y^3,
\]

and \(Z^3=t^9+\alpha^3s^3t^6\). Thus \(s^9,t^9\in R_\alpha\), and the
freshman's-dream identity

\[
 \phi^9=l^9z^9-h^9
\]

lies in \(R_\alpha[z]\). It again has weighted degree \(36\), hence descends
to an ordinary form \(G\) of degree \(12=4p\).

In both cases

\[
 \nu^*G=\phi^{3p}.
\]

Because \(\nu\) is a universal homeomorphism, the zero set of \(G\) on \(X\)
is exactly \(\nu(D)=C\). If \(F\) is the cubic equation of \(X\), then

\[
 \boxed{\sqrt{(F,G)}=I_C,\qquad(\deg F,\deg G)=(3,4p).}
\]

Indeed, the pullback of \(V_X(G)\) is exactly \(D\); the universal
homeomorphism therefore identifies its support with \(C\). Equality of the
projective zero set also gives equality of the homogeneous affine cones, since
their common origin already lies on the cone over \(C\), so homogeneous
Nullstellensatz gives the displayed unsaturated radical equality.

The construction includes inseparable degree-three rulings in characteristic
three and wild separable ramification in characteristic two. P-008 gives
smaller equations for the monomial member in characteristics two and three;
the theorem here is uniform for the entire smooth rational-quartic family.
The argument proves the family-wide statement directly. The verified Barile–Morales–Thoma fixed-monomial construction at the beginning of this chapter has narrower curve scope; no novelty claim is made from the bounded literature comparison.

## Constructibility (P-013): fixed-degree STCI is constructible in families

Let \(S\) be noetherian and let
\(\mathcal C\subset\mathbf P^3_S\) be a closed family.  Fix positive integers
\((a,b)\).  Then

\[
 \{s\in S:\ |\mathcal C_{\bar s}|=
 |V(F_a,F_b)|\text{ for some geometric forms }F_a,F_b\}
\]

is constructible.

Indeed, let \(Q\) be the product over \(S\) of the two projective coefficient
spaces, and on \(\mathbf P^3_Q\) let \(Z\) be the common zero scheme of the
two universal forms.  Put \(\mathcal C_Q=\mathcal C\times_SQ\).  Failure of
either set-theoretic inclusion is detected by a point of

\[
 \mathcal C_Q\setminus Z
 \quad\text{or}\quad
 Z\setminus\mathcal C_Q.
\]

Each image in \(Q\) is constructible by Chevalley's theorem.  Taking their
complements and intersection gives a constructible subset \(W\subset Q\) on
which the two supports agree.  Its image in \(S\), again constructible by
Chevalley, is exactly the displayed locus.  Properness is not needed, and the
locus need not be open or closed.

Now take a model over a one-dimensional arithmetic base with infinitely many
closed points, for example a nonempty open subscheme of the spectrum of the
ring of integers of a number field.  A constructible subset that omits the
generic point is finite, while one that contains the generic point contains a
nonempty open set and therefore all but finitely many closed points.
Consequently, for a fixed pair \((a,b)\), the following are equivalent:

1. the geometric generic fiber has such a pair;
2. infinitely many geometric closed fibers have such a pair;
3. all but finitely many geometric closed fibers have such a pair.

The infinite-closed-point hypothesis is essential for the equivalence with
item 2.  The earlier wording "over a localized number ring" was too broad:
for a semilocal localization such as \(\mathbf Z_{(p)}\), "infinitely many
closed fibers" can be vacuous.  The constructibility theorem itself is
unchanged.

The same is true with both degrees bounded by a fixed \(B\), since only
finitely many pairs occur.  This explains rigorously why P-012 does not force a
characteristic-zero presentation: its second degree \(4p\) is unbounded.  In
particular, Craighero--Gattazzo's characteristic-zero exclusion of every cubic
carrier implies that for each fixed \(B\), only finitely many reductions of a
number-field rational quartic can have a \((3,d)\) presentation with
\(d\le B\), even though P-012 supplies a \((3,4p)\) presentation at every
prime.

## Exact cuspidal-carrier minima (P-014): sharp degree on the cuspidal cubic carriers

The Frobenius degree in P-012 is not merely an artifact of that proof on the
chosen cubic carrier.  First consider the standard cusp ring

\[
 R_0=k[s^3,s^2t,t^3]\subset k[s,t].
\]

Its ordinary degree-\(m\) piece consists of all binary forms of degree \(3m\)
except for the one missing semigroup monomial \(st^{3m-1}\).  Thus membership
is equivalent to vanishing of that single coefficient.  If a second surface
on the cone has support equal to the graph \(D=(\phi=lz-h=0)\), unique
factorization upstairs forces its pullback to be \(c\phi^N\).  Homogeneity
forces \(3\mid N\), with second degree \(d=4N/3\).

For \(\phi^N\) to descend coefficientwise, it is necessary and sufficient
that \(p\mid N\).  Sufficiency follows because an \(N\)-th power with
\(p\mid N\) is a polynomial in \(p\)-th powers, so every relevant binary
\(s\)-exponent is a multiple of \(p\) and cannot equal one.

For necessity, keep the standard cusp coordinates fixed with
\(R=[0:1]\), and write \(l=as+bt\).  Assume the homogeneous condition
\(3\mid N\) and \(p\nmid N\).  There are three cases.

1. If \(b=0\), then \(P=(l=0)=R\).  The coefficient of \(z\) in
   \(\phi^N\) has missing-monomial coefficient
   \(\pm Na h(R)^{N-1}\ne0\).
2. If \(a,b\ne0\), the coefficient of \(z^N\) is \(l^N\), whose missing
   \(st^{N-1}\) coefficient is \(Na b^{N-1}\ne0\).
3. If \(a=0\) and \(b\ne0\), smoothness of the original quartic at \(R\)
   forces the \(st^3\) coefficient \(h_1\) of \(h\) to be nonzero.  The
   coefficient of \(z^{N-1}\), namely \(-N l^{N-1}h\), has missing
   \(st^{N+2}\) coefficient \(-Nb^{N-1}h_1\ne0\).

Thus descent fails whenever \(p\nmid N\).  The earlier proof's attempt to move
\(P\) while retaining the displayed semigroup coordinates was unjustified,
and its use of the constant coefficient failed when \(h(R)=0\); the
three-case argument above repairs both defects.  Therefore

\[
 N_{\min}=\operatorname{lcm}(3,p),\qquad
 d_{\min}=4N_{\min}/3.
\]

This is \((N,d)=(3p,4p)\) for \(p\ne3\) and \((3,4)\) for the standard cusp
in characteristic three.

There is a genuinely different characteristic-three cusp.  For
\(\alpha\ne0\), put

\[
 R_\alpha=k[s^3,s^2t,t^3+\alpha st^2].
\]

If \(f=\sum_{i=0}^{3m}c_i s^{3m-i}t^i\), then

\[
 f\in(R_\alpha)_m
 \quad\Longleftrightarrow\quad
 c_{3m-1}=m\alpha c_{3m}.
\]

To prove this, note that
\(Y^3+\alpha XY^2-X^2Z\) is the full kernel of the normalization map, so
\(\dim(R_\alpha)_m=3m\), one less than the full binary space.  Among generator
monomials, only \(Z^m\) contributes to the two top \(t\)-coefficients, and

\[
 Z^m=t^{3m}+m\alpha st^{3m-1}+O(s^2).
\]

The displayed relation is therefore both necessary and, by dimension,
sufficient.

Only \(N=3,6,9,\ldots\) are homogeneous possibilities.  If
\(P\ne R=[0:1]\), write \(l=as+bt\) with \(b\ne0\).  Freshman's dream makes
the next-to-top coefficient of \(l^3\), respectively \(l^6\), zero while the
top coefficient is \(b^3\), respectively \(b^6\); the membership relation
fails for \(m=1\), respectively \(m=2\).  If \(P=R\), then \(l=s\) and
\(h(R)\ne0\); the same argument applied to \(h^3\) and \(h^6\), with
\(m=4,8\), excludes \(N=3,6\).  But

\[
 \phi^9=l^9z^9-h^9
\]

always descends because the relevant values \(m=3,12\) vanish in the field.
An explicit lift is obtained from

\[
 U=XZ^2+\alpha Y^2Z+\alpha^2XYZ-\alpha^3Y^3,
 \quad S_9=X^3,
 \quad T_9=Z^3-\alpha^3U,
\]

whose pullbacks are \(s^3t^6,s^9,t^9\).  If
\(l=as+bt\) and \(h=\sum h_i s^{4-i}t^i\), set

\[
 L_9=a^9S_9+b^9T_9,
 \qquad
 H_9=\sum_{i=0}^4h_i^9S_9^{4-i}T_9^i.
\]

Then the ordinary degree-twelve form

\[
 G=L_9W^9-H_9
\]

pulls back exactly to \(\phi^9\).  Hence on the nonclassical cusp carrier

\[
 \boxed{N_{\min}=9,\qquad d_{\min}=12.}
\]

These are minima on the specified cubic cone; they do not claim that no
different carrier can give a lower-degree presentation of the same quartic.
