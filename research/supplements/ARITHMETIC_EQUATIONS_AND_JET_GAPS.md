# Arithmetic degree bounds, missing jets, and actual non-binomial equations

The embedded curve is the fixed integral model \(C_0=[s^4:s^3t:st^3:t^4]\). All defining forms have actual scalar coefficients over the algebraically closed field in question. The arithmetic reduction and restricted constructions below have inherited independent review; they remain unpromoted. Their minima range over specified carriers or sources, not every homogeneous pair.

Two extensions have separate focused proofs: [the torus weight bounds](EQUIVARIANT_DEGREE_BOUNDS.md)
allow one weight-homogeneous equation with an arbitrary mate, at most two
weights in each equation, or a specified pair of boundary congruences. They
also constrain extreme components when \(p\nmid ab\).
[Effective characteristic transfer](EFFECTIVE_CHARACTERISTIC_TRANSFER.md)
quantifies the bounded-degree arithmetic reduction below and, using the
promoted quartic exclusion, proves unconditional growth of mate degrees
over every quartic carrier. Neither establishes unrestricted degree growth
without the characteristic-zero nonexistence hypothesis.

The characteristic comparison has a broader purpose than degree estimates.
Degree growth tests nonexistence across all presentations; a horizontal
component of a fixed-degree incidence would instead construct a
characteristic-zero presentation. Local lifting obstructions distinguish
particular special fibers, and Frobenius/conductor calculations identify
which infinitesimal gluing conditions disappear in characteristic \(p\).
These are different routes to the characteristic-zero question.
The [mixed-characteristic trace obstruction](MIXED_CHARACTERISTIC_TRACE_OBSTRUCTION.md)
now constrains simultaneous deformations of both equations near the
torus-homogeneous locus: it excludes unramified good reduction when
\(v_p(ab)=1\) and gives a necessary valuation bound for ramified lifts.
It does not calculate every horizontal component.
The [prime-to-p power-extraction theorem](PRIME_TO_P_POWER_EXTRACTION.md)
goes further for the prescribed powered-quartic points: every prime-to-\(p\)
power can be extracted from an actual supported trait, excluding those
points from horizontal components even after ramification. Pure \(p\)-powers
and other special presentations remain unresolved.

## Bounded degree and characteristic-zero existence

## 1. The exact characteristic limit that would settle the question

Define the minimum over **all** supported pairs
\[
\delta(p)=\min\{\max(a,b):V(F_a,G_b)_{\mathrm{red}}=C_0
\text{ over }\overline{\mathbb F}_p\}.
\]
The convention is \(+\infty\) if no pair exists. Known positive-
characteristic constructions make it finite for this curve.

The precise form of the arithmetic strategy is
\[
\boxed{C_0\text{ is not an STCI in characteristic zero}
\quad\Longleftrightarrow\quad
\delta(p)\longrightarrow\infty\text{ as primes }p\longrightarrow\infty.}
\tag{1}
\]
It is enough to prove an unbounded sequence of actual values of
\(\delta(p)\) along distinct primes. Exact minimality of the known
Frobenius constructions is stronger than needed.

For completeness, the proof uses finite type rather than an assumed
lifting theorem. At fixed \((a,b)\), take the projective coefficient
space of pairs containing the parametrized curve. In its universal
intersection remove the fixed copy of \(C_0\). The image of the remaining
open subscheme in coefficient space is constructible by
[Chevalley's theorem, Stacks Tag 054K](https://stacks.math.columbia.edu/tag/054K).
Its complement is the geometric sole-support locus. For a fixed degree
bound \(D\), its finite union over \(a,b\le D\) has constructible image
in \(\operatorname{Spec}\mathbb Z\). That image either contains the
generic point and all but finitely many primes, or misses the generic
point and contains only finitely many primes. This proves (1).

The finite rank-locus construction below supplies an actual integral
incidence scheme for the same condition. A nonempty finite-type
characteristic-zero fiber has a closed point over a number field; hence
existence over any algebraically closed characteristic-zero field is
equivalent to existence over \(\overline{\mathbb Q}\). Transcendental
coefficients create no loophole in (1).

Two equivalent measurements are
\[
\mu(p)=\min ab,\qquad \tau(p)=\min m_C=\mu(p)/4.
\]
They diverge exactly when \(\delta(p)\) does, since
\(\delta(p)\le\mu(p)\le\delta(p)^2\). In contrast,
\(\min\min(a,b)\) cannot diverge: known constructions keep one equation
quartic. All minima here allow finite extensions of \(\mathbb F_p\);
failure to find rational coefficient pairs over \(\mathbb F_p\) is not
geometric emptiness.

## The full simultaneous equation incidence

The parametrization defines a closed copy of \(\mathbf P^1_{\mathbb Z}\) in
\(\mathbf P^3_{\mathbb Z}\): on \(x_0\ne0\) its coordinates are
\((x_1,x_2,x_3)=(t,t^3,t^4)\), and on \(x_3\ne0\) the ratio \(x_2/x_3\)
is the local parameter at infinity. This description works in every
characteristic.

Let \(P_{a,b}\) be the closed subscheme of the product of the two full
projective coefficient spaces obtained by setting every coefficient of
\(F(s^4,s^3t,st^3,t^4)\) and of the corresponding substitution in \(G\)
equal to zero. This avoids assuming any cohomology base-change statement
about a chosen basis of global sections. Its geometric points are exactly
the nonzero degree-\(a,b\) forms containing the fixed curve.

Inside \(P_{a,b}\), the proper-pair locus \(U_{a,b}\) is open. Indeed,
the common-factor locus is the finite union, for
\(1\le e\le\min(a,b)\), of the images of the projective multiplication
maps
\[
\mathbf P(S_e)\times\mathbf P(S_{a-e})\times\mathbf P(S_{b-e})
\longrightarrow\mathbf P(S_a)\times\mathbf P(S_b),
\qquad(H,A,B)\longmapsto(HA,HB).
\]
These images are closed. Here \(S_d\) is the free module of homogeneous
degree-\(d\) forms, including \(S_0\).

If \(4\nmid ab\), the STCI locus is empty by the degree identity. Otherwise
put \(M=ab/4\). On the chart above, use
\[
u=x_2-t^3,\qquad v=x_3-t^4,\qquad K=k(t),\qquad
A_M=K[u,v]/(u,v)^{M+1},\qquad n=\binom{M+2}{2}.
\]
Substituting \((1,t,t^3+u,t^4+v)\) in the universal forms and taking all
truncated monomial multiples gives a multiplication matrix
\(T:A_M^2\to A_M\). Every entry is a polynomial in \(t\), with integral
polynomial expressions in the original scalar coefficients.

For a proper geometric pair let \(\ell\) be its generic transverse length
along \(C_0\). The degree identity gives \(4\ell\le ab\). In the generic
transverse Artin quotient, length \(\ell\) implies that its maximal
ideal to power \(\ell\) vanishes. Truncation at \((u,v)^{M+1}\)
therefore preserves that quotient, and the multiplication matrix presents
it. Hence
\[
\ell\le M,\qquad n-\operatorname{rank}_{k(t)}T=\ell.
\]
Consequently
\[
\sqrt{(F,G)}=I_{C_0}
\quad\Longleftrightarrow\quad
\operatorname{rank}_{k(t)}T\le n-M.\tag{Rank}
\]
The radical here describes projective reduced support, equivalently the
radical of the saturated homogeneous ideal. Degree exhaustion and purity
are essential for (Rank); the same rank equations outside the proper locus
are not an STCI certificate.

Set every coefficient in \(t\) of every \((n-M+1)\)-minor to zero.
This is a finite collection of equations over \(\mathbb Z\), valid after
specialization to every characteristic. It defines a closed condition
on each affine coefficient chart, invariant under nonzero rescaling of
either form. Therefore the STCI locus \(Z_{a,b}\) is closed relative to
\(U_{a,b}\), in particular a scheme of finite type over \(\mathbb Z\).
This construction keeps coefficients in \(k\), rather than allowing
arbitrary choices in \(k(t)\).

## Mixed-characteristic lifting on the full incidence

Fix a characteristic-\(p\) point \(z\in Z_{a,b}\). A DVR trait in
\(Z_{a,b}\) with closed point mapping to \(z\) and characteristic-zero
generic point exists, allowing residue extension and ramification, exactly
when
\[
p\notin\sqrt{0}\quad\text{in }\mathcal O_{Z_{a,b},z}. \tag{Trait}
\]
Indeed, nonnilpotence says that \(z\) lies in the closure of
\(Z_{a,b}[1/p]\). Applying the finite-type closure-to-trait lemma to
that open immersion produces the trait. Conversely, a local map to a DVR
of mixed characteristic sends \(p\) to a nonzero element, so \(p\)
cannot have been nilpotent. No properness of the incidence over
\(\mathbb Z\) is asserted or needed. This is a reformulation of the
horizontal-component question, not a calculation of (Trait).
[Stacks, Lemma 32.15.1](https://stacks.math.columbia.edu/tag/0CM1).

There is also a precise formal route. Let \(R\) be one complete
mixed-characteristic DVR with uniformizer \(\pi\). Suppose compatible
embedded flat subschemes \(W_n\subset\mathbf P^3_{R/\pi^n}\) are supplied
for every \(n\). They algebraize to a proper embedded subscheme over
\(R\), by [Stacks, Lemma 76.43.1](https://stacks.math.columbia.edu/tag/0A00).
To obtain the desired supported complete intersection, retain compatible
actual degree-\((a,b)\) generators and the support containments as part
of this system: for one fixed \(N\), require
\[
\mathcal I_{C_R}^{N}\mathcal O_{\mathbf P^3_{R/\pi^n}}
 \subset \mathcal I_{W_n}
 \subset \mathcal I_{C_R}\mathcal O_{\mathbf P^3_{R/\pi^n}}
\quad\text{for every }n. \tag{Support}
\]
The compatible coefficients have limits in \(R\); the resulting two
forms have exactly these reductions. Exactness and faithfulness of
completion for coherent sheaves on the proper ambient space transport
(Support) and identify their ideal with the algebraized ideal. Flatness and
the given complete-intersection presentation likewise persist. Thus the
generic fiber is an actual supported pair. This implication presupposes
the compatible global lifts; it does not construct them. Reduced support
at each infinitesimal level alone cannot replace the uniform containments
(Support), which control the generic fiber.

An unramified second-Witt-vector obstruction does not exclude a ramified
lift. For example, the special point \(x=0\) of \(x^2=p\) has no lift
to \(\mathbb Z/p^2\mathbb Z\): every possible lift is divisible by
\(p\), whose square is zero there, whereas \(p\ne0\). It does lift
to the ramified complete DVR
\(\mathbb Z_p[\varpi]/(\varpi^2-p)\), by \(x=\varpi\). Therefore the
[known higher-degree \((16,p)\) examples](#a-larger-source-with-an-actual-transverse-jet-gap)
remain unresolved under simultaneous deformation of both equations.
Their fixed-carrier jet obstruction cannot decide the local ring of the
full incidence. The [Granger–Schulze construction](https://arxiv.org/abs/1804.01316)
concerns deformations of monomial space-curve singularities; its analytic,
equicharacteristic semigroup setting supplies no support-preserving
projective mixed-characteristic lift here.

For the separate torus-homogeneous special-fiber locus, the
[reviewed integral trace calculation](MIXED_CHARACTERISTIC_TRACE_OBSTRUCTION.md)
does allow arbitrary simultaneous deformations of both equations. If
\(r\ge1\) is the least valuation of their normalized non-eigen
coefficients, every actual mixed-characteristic supported lift satisfies
\(e\,v_p(ab)\ge2r\), where \(e=v_\pi(p)\). This is a necessary
condition on a trait, not a proof that the condition produces one.

There is now a full-trait exclusion for a specified family. The
[power-extraction proof](PRIME_TO_P_POWER_EXTRACTION.md) shows that every
supported trait reducing to \((G_p,F_4^n)\), \(p\nmid n\),
would yield a quartic mate on its characteristic-zero generic fiber.
Thus these points satisfy \(p\in\sqrt{0}\) in their local incidence
rings. This allows arbitrary deformations of both equations and arbitrary
ramification. It does not calculate the whole degree-\((p,4n)\) locus.

The remaining arithmetic input is a support-preserving lifting operation
or a structural calculation on this full simultaneous-pair incidence.
One horizontal component would establish characteristic-zero existence;
excluding the selected special-fiber points or fixed carriers does not
establish nonexistence without an exhaustive reduction. No horizontal
component or compatible supported lifting system has been constructed.

## One binomial equation, with an arbitrary mate

## 3. A broader exact bound: every pair with a binomial equation

**Reviewed provisional proposition.** Let \(k\) be algebraically closed of
characteristic \(p>0\). If \(C_0\) is the sole reduced support of a
degree-\((a,b)\) pair and at least one defining equation is a binomial,
then
\[
p\mid m_C=ab/4,
\qquad ab\ge4p,
\qquad \max(a,b)\ge p.
\tag{3}
\]
The mate may be an arbitrary homogeneous polynomial. No hypothesis of
two binomial equations is imposed.

The carrier reduction used below is classical. In
[Thoma's primary paper, Theorems 2.3 and 2.4](https://www.researchgate.net/publication/303334542_Monomial_space_curves_in_as_binomial_set_theoretic_complete_intersections),
an admissible irreducible binomial carrier of a monomial space curve
must have a pure power of an interior coordinate as one monomial. The
excluded mixed-support types cannot admit a mate in any characteristic.
For the present curve the two possible interior coordinates are exchanged
by \((x_0,x_1,x_2,x_3)\mapsto(x_3,x_2,x_1,x_0)\). The following
coefficient argument extracts a positive-characteristic divisibility
consequence of that reduction; no novelty claim is made.

### 3.1 Reduction of powers and factors

Every irreducible factor of either defining equation must contain
\(C_0\). Otherwise its intersection with the other positive-degree
surface contains a curve outside \(C_0\), or a common surface component.
This is the usual factor reduction, also used in R-0001.

A monomial factor cannot contain \(C_0\). After removing a common
monomial from a binomial and extracting the gcd of its exponent
difference, its factors over an algebraically closed field are primitive
binomials indexed by roots of unity. Exactly the factor of phase one
contains the dense torus of \(C_0\). Consequently a binomial defining
equation in a supported pair is a scalar times
\(F_0^{p^e}\), with \(F_0\) irreducible binomial. In particular
\((F_0,G)\) itself is supported on \(C_0\).

Write \(a_0=\deg F_0\), so \(a=p^e a_0\), and let
\(m_0=a_0b/4\), an integer by degree exhaustion. It suffices to prove
\(p\mid m_0\). Then \(m_C=p^e m_0\) gives (3).

The carrier reduction can also be reconstructed directly. Grade
\(R=k[x_0,x_1,x_2,x_3]/(F_0)\) by weights \((0,1,3,4)\).
It is a domain, and \(\sqrt{(\overline G)}=I_{C_0}/(F_0)\) is
homogeneous for this grading. Every nonzero weight component \(g_i\)
of \(\overline G\) consequently has \(g_i^N=H\overline G\) for
some \(N>0\). In a graded domain the difference between largest and
smallest occurring weights adds under multiplication. The left side
has difference zero; hence \(\overline G\) is weight-homogeneous.
It has a representative of ordinary degree \(b\) and one weight,
obtained from the corresponding weight component of the original \(G\).

If neither monomial of \(F_0\) is a pure power of \(x_1\) or
\(x_2\), both coordinate points \([0:1:0:0]\) and \([0:0:1:0]\)
lie on its carrier and outside \(C_0\). The representative mate must
be nonzero at both. Thus it must contain both \(x_1^b\) and
\(x_2^b\), which have different weights \(b\) and \(3b\).
This is impossible. A pure power of \(x_0\) or \(x_3\) cannot be
a term in a nonzero binomial relation of \(C_0\), because its torus
weight is extremal. This proves the required pure-interior-power
reduction in every characteristic without relying on OCR of the source.

### 3.2 The finite cover and the missing first coefficient

By the carrier reduction and coordinate reversal, write
\[
F_0=x_1^{a_0}-x_0^{n_0}x_2^{n_2}x_3^{n_3},
\qquad n_0+n_2+n_3=a_0,
\qquad 4n_0+n_2=3a_0.
\tag{4}
\]
Primitivity means \(\gcd(a_0,n_0,n_2,n_3)=1\). The two equations in
(4) imply
\[
n_2=3a_0-4n_0,\qquad n_3=3n_0-2a_0,
\qquad \frac{2a_0}{3}\le n_0\le\frac{3a_0}{4}.
\tag{5}
\]
There is no solution at \(a_0=1,2\). Therefore \(a_0\ge3\) and
\(n_0\ge2\).

Consider the finite, basepoint-free morphism
\[
\phi:\mathbf P^2\longrightarrow V(F_0),\quad
[U:V:W]\longmapsto
[U^{a_0}:U^{n_0}V^{n_2}W^{n_3}:V^{a_0}:W^{a_0}].
\tag{6}
\]
Its finiteness follows because the coordinate subring contains
\(U^{a_0},V^{a_0},W^{a_0}\); its image is the integral hypersurface
\(V(F_0)\). The full reduced inverse image of \(C_0\) is the
irreducible plane quartic
\[
B=V^4-UW^3=0.
\tag{7}
\]
Here is a direct check of full inverse support. On \(UW\ne0\), put
\(z=V^4/(UW^3)\). Membership of the image in \(C_0\), applied to its
quartic and cubic toric relations, implies
\(z^{a_0}=z^{n_2}=z^{n_3}=1\). The gcd of these exponents is one,
because it equals \(\gcd(a_0,n_0)\), which is one by primitivity and
(5). Thus \(z=1\) in every characteristic. Conversely, the
parametrization \([U:V:W]=[s^4:st^3:t^4]\) of (7) maps to \(C_0\)
with parameters \((s^{a_0},t^{a_0})\). If \(UW=0\), the relation
\(x_2^4=x_0x_3^3\) forces \(V=0\), which is again in (7).

Since \(G\) cuts out precisely \(C_0\) on the carrier, its pullback
is a homogeneous polynomial with sole reduced zero support (7).
Unique factorization gives
\[
\phi^*G=c(V^4-UW^3)^N,
\qquad a_0b=4N,
\qquad N=m_0>0.
\tag{8}
\]
But \(\phi^*G\) belongs to the subring
\[
k[U^{a_0},\ U^{n_0}V^{n_2}W^{n_3},\ V^{a_0},\ W^{a_0}].
\]
Every monomial in this subring has \(U\)-exponent
\(a_0r_0+n_0r_1\), with \(r_0,r_1\ge0\). Because
\(a_0\ge3\) and \(n_0\ge2\), exponent one is impossible.
The coefficient of \(UV^{4N-4}W^3\) on the right of (8) is
\(-cN\). It must vanish. Thus \(p\mid N\), proving (3).
The last inequality in (3) follows from the stronger divisibility:
\(p\mid ab\) forces \(p\mid a\) or \(p\mid b\).

### 3.3 Exact minimum in this restricted class for large primes

Let \(\delta_{\mathrm{bin}}(p)\) minimize \(\max(a,b)\) over supported
pairs having at least one binomial equation, with arbitrary mate.
Combining (3) with the actual \((4,p)\) pair from Section 2 gives
\[
\boxed{\delta_{\mathrm{bin}}(p)=p\quad\text{for every prime }p\ge7.}
\tag{9}
\]
This is a minimum over all binomial carriers, rather than only the fixed
quartic. It remains a restricted-class statement. The inequality
\(\delta(p)\le\delta_{\mathrm{bin}}(p)\) has the wrong direction to
turn (9) into an unrestricted lower bound.

The [independent arithmetic audit, Sections 5–6](ARITHMETIC_EQUATIONS_AND_JET_GAPS.md#exceptional-prime-minima-with-their-proof)
also proves the exceptional-prime minima and displays a chart-verified
characteristic-five \((3,20)\) pair:

| Prime | Exact minimum \(\delta_{\mathrm{bin}}(p)\) | One attaining pair |
| --- | --- | --- |
| 2 | 4 | \((4,4)\) |
| 3 | 4 | \((4,3)\) |
| 5 | 20 | \((3,20)\) |
| \(p\ge7\) | \(p\) | \((4,p)\) |

For a fixed degree bound \(D\), choosing a prime \(p>D\) therefore
removes the entire one-binomial class from a bounded-degree search.
Any surviving pair of degrees at most \(D\) must use two non-binomial
equations. This is a useful search filter and leaves the class where a
bounded-degree arithmetic route to characteristic zero could occur.

## Why degeneration does not cover every pair

An equivariant degeneration is a possible way to compare these classes,
but contains a precise obstruction. The diagonal torus preserving
\(C_0\) acts on the projective coefficient spaces. An orbit has limits
whose equations are weight-homogeneous. Even if a stronger theorem about
such limiting equations is available, these limits can acquire a common
surface factor. The sole-support rank locus is closed **inside the
proper-pair open subset**, not across that boundary. The full flat-limit
ideal can require more generators than the two displayed limiting forms.
Therefore a torus degeneration does not reduce every supported pair to
a binomial pair unless it also preserves properness or supplies a new
argument retaining the entire flat-limit ideal. This is a missing
implication, not an exclusion theorem.

For candidate searches, a positive-characteristic example of bounded
degrees with two non-binomial equations and \(p\nmid m_C\) would directly
test the proposed all-pairs divisibility target. Such a pair at a single
prime would refute that target at that prime; persistence at infinitely
many distinct primes with one fixed degree bound would produce
characteristic-zero existence by (1). A failed search proves only the
emptiness of the actual family or fixed-degree locus tested.

## A larger source with an actual transverse jet gap

## 1. A specified twenty-three-parameter source

On \(\mathbf P^2_{s:t:z}\), put
\[
\begin{aligned}
 U_0&=s^4+s^2zL_0,&U_1&=s^3t+s^2zL_1,\\
 U_2&=st^3+\alpha z^4+szC_2,&U_3&=t^4+zB_3,
\end{aligned}\tag{1}
\]
where \(\alpha\ne0\), \(L_0,L_1\) are arbitrary linear forms,
\(C_2\) an arbitrary quadratic, and \(B_3\) an arbitrary cubic.
There are \(1+3+3+6+10=23\) scalar parameters. Every system restricts
on \(c=(z=0)\) to literal \(C_0\). This enlarges the inherited
eleven-parameter family by varying both formerly fixed coordinates and
the transverse terms of the third.

Retain basepoint-free systems with **full** reduced inverse support of
\(C_0\) equal to \(c\). Basepoint freeness makes the map finite onto
its integral image because its pullback of \(\mathcal O(1)\) is the
ample \(\mathcal O_{\mathbf P^2}(4)\). Birationality is separate;
when present the image has degree sixteen and the map is its normalization.
The admissible locus of this enlarged source is not classified here, and
a generic member is not asserted admissible.

The family is nonempty: \(L_0=L_1=C_2=0\),
\(\alpha=1,B_3=s^3\) gives the inherited finite birational map
\[
U=(s^4,s^3t,st^3+z^4,t^4+s^3z).\tag{2}
\]
Its full singleton support and degree-sixteen image are recorded in
[R-0017](../results/singleton_plane_conductor_descent.md) and its cited
evidence. Those accepted characteristic-zero proofs are inputs, not
replayed computations. The same literal map works in every characteristic:
on \(s\ne0\) its inverse uses \(t/s=X_1/X_0\) and
\(z/s=X_3/X_0-(X_1/X_0)^4\); on \(s=0\), membership in \(C_0\)
forces \(z=0\). These formulas do not divide by a characteristic.

## 2. Higher jets turn descent failure into degree divisibility

**Jet-gap lemma.** Let \(A\) be a target local ring inside a source
DVR with uniformizer \(r\) and residue field \(E\). Suppose that,
modulo \(r^e\), \(e\ge2\), every element of \(A\) has the form
\(R(w)\), where \(R\in k(W)\) and the residue \(w_0\) is
transcendental over \(k\). Let
\[
q=c+ar+O(r^2),\qquad c\in k^*,\quad a\in E^*.
\]
If \(q^b\in A\), for \(b>0\), then characteristic zero is
impossible; in characteristic \(p>0\), necessarily
\[
\boxed{p^{v_p(b)}\ge e.}\tag{3}
\]

The residue of \(R(w)=q^b\bmod r^e\) is \(c^b\). Injectivity
of \(k(W)\to E\) forces \(R(W)=c^b\), so the whole jet must be
constant. In characteristic zero its coefficient of \(r\) is
\(bc^{b-1}a\ne0\). In characteristic \(p\), write
\(b=p^vn\), \(p\nmid n\). Frobenius gives the first nonconstant
term \(nc^{b-p^v}a^{p^v}r^{p^v}\), with nonzero coefficient. This
proves (3). Localized denominators are allowed: a denominator with nonzero
residue is invertible modulo \(r^e\). Ordinary differentiation detects
only \(p\mid b\); the first surviving Hasse order records the necessary
\(p\)-power.

Apply this at \(D=(s=0)\), using \(z=1\), \(r=s/z,y=t/z\) and
the target frame \(X_2\). Put
\(u=U_2=\alpha+r[y^3+C_2(r,y,1)]\). The coordinates
\(U_0/u,U_1/u\) vanish modulo \(r^2\), while
\[
w=U_3/u,\quad w_0=\frac{y^4+B_3(0,y,1)}\alpha,\quad q=1/u.
\]
The element \(w_0\) is transcendental: its numerator has degree exactly
four in \(y\). The linear coefficient of \(q\) is
\(-\alpha^{-2}[y^3+C_2(0,y,1)]\ne0\), since the quadratic term
has degree at most two. The target local ring at the image line reduces
modulo \(r^2\) to rational functions of \(w\), with the denominator
check in the lemma.

A sole-support mate \(G_b\) pulls back to
\(G_b(U)=\lambda z^{4b}\), \(\lambda\ne0\), by full inverse
support and unique factorization. Division by \(\lambda U_2^b\)
forces \(q^b\) to descend. Every retained member of (1) therefore has
no characteristic-zero mate and, in characteristic \(p>0\), every mate
satisfies
\[
\boxed{p\mid b.}\tag{4}
\]
Neither equation has a binomial hypothesis. On the sublocus
\(L_0=l_0s,L_1=l_1s\), the first two target coordinates vanish
modulo \(r^3\), strengthening (3) to \(p^{v_p(b)}\ge3\), in
particular \(4\mid b\) in characteristic two. For a birational
degree-sixteen image, \(m_C=4b\); thus \(p\mid m_C\) for every odd
prime, and \(\max(16,b)\ge p\).

## 3. A carrier admitting no binomial relation

For (2), set
\[
A=x_0^3x_3-x_1^4,\quad B=x_0^2x_2-x_1^3,\quad
F=A^4-x_0^{13}B.\tag{5}
\]
Its image is the integral degree-sixteen surface \(X=V(F)\), and
\[
A(U)=s^{15}z,\qquad B(U)=s^8z^4.\tag{6}
\]
The polynomial \(F\) is primitive and linear in \(x_2\), with
coefficient \(-x_0^{15}\). Its constant coefficient is not divisible
by \(x_0\), since at \(x_0=0\) it is \(x_1^{16}\). Hence it is
irreducible in every characteristic.

The image lies on **no nonzero homogeneous binomial hypersurface**.
The source polynomials \(st^3+z^4\) and \(t^4+s^3z\) are distinct
irreducibles: each is primitive linear in one variable, with coprime
coefficients in the polynomial ring of the other two. They are not
associates of \(s\) or \(t\). In a relation \(U^a=cU^b\), unique
factorization forces equal exponents of \(U_2,U_3\); the \(t\)-
exponents then force equality for \(U_1\), and the \(s\)-exponents
force equality for \(U_0\). Only the trivial relation remains.

This proves that the carrier itself is genuinely non-binomial. A
binomial containing \(C_0\) need not contain \(X\), so this argument
alone does not exclude binomial mates. The explicit mates below are
proved non-binomial separately.

## 4. Explicit degree-p mates and exact minimum for p at least 43

Let \(p\ge43\) be prime. Set
\[
r\equiv3p\pmod4,\quad0\le r<4,\qquad
n=(3p-r)/4,\qquad E=(p-3r)/4.
\]
Here \(r=1\) or \(3\), and \(E\ge9\). For \(j=4h+\ell\),
\(0\le\ell<4\), define
\[
P_p=x_1^r\sum_{j=0}^{n}(-1)^j\binom nj
x_0^{E+h-3\ell}x_3^{n-j}B^hA^\ell,
\qquad G_p=x_2^p-P_p.\tag{7}
\]
All exponents are nonnegative because \(E+h-3\ell\ge E-9\ge0\).
Each summand has ordinary degree \(p\). The bound \(E\ge9\) holds
for primes \(p\equiv3\pmod4\) at \(p\ge43\), and for
\(p\equiv1\pmod4\) at \(p\ge53\); the only primes from 43 to 52
are 43 and 47. Thus (7) covers every prime at least 43.

In \((k[x]/(F))_{x_0}\), the identities
\(x_1^4=x_0^3x_3-A\) and \(A^4=x_0^{13}B\) give
\[
\frac{x_1^{3p}}{x_0^{2p}}
=\frac{x_1^r(x_0^3x_3-A)^n}{x_0^{2p}}=P_p.\tag{8}
\]
For \(j=4h+\ell\), the exponent of \(x_0\) after replacing
\(A^{4h}\) is \(3(n-j)-2p+13h=E+h-3\ell\), as in (7).
Pullback gives \(P_p(U)=s^pt^{3p}\), initially on \(s\ne0\),
then as a polynomial identity. Frobenius therefore gives
\[
\boxed{G_p(U)=(st^3+z^4)^p-s^pt^{3p}=z^{4p}.}\tag{9}
\]
The form \(G_p\) does not vanish identically on \(X\). The finite
surjective map and full singleton inverse support prove
\[
V(F,G_p)_{\rm red}=C_0,\qquad [V(F,G_p)]=4p[C_0].\tag{10}
\]
Thus the actual pair is proper and has degrees \((16,p)\).

Both equations are non-binomial. Every term of \(P_p\) is divisible
by \(x_1^r\), with \(r>0\), so \(G_p\) has the pure monomial
\(x_2^p\) with coefficient one. If \(G_p\) were a binomial
\(x_2^p-cM\), (9) would force \(cM(U)=s^pt^{3p}\).
Unique factorization forces the \(x_2,x_3\) exponents of \(M\) to
vanish, because \(U_2,U_3\) are irreducibles distinct from \(s,t\).
Writing \(M=x_0^ax_1^b\), its pullback is
\(s^{4a+3b}t^b\). Hence \(b=3p\), impossible for a
degree-\(p\) monomial. Thus \(G_p\)
is not binomial. This is a literal two-non-binomial construction.

Combining (4) and (9), the minimum positive mate degree on this
particular non-binomial carrier is exactly
\[
\boxed{b_{\min}(p)=p\qquad(p\ge43).}\tag{11}
\]
The minimum maximum defining degree in (1), restricted to birational
admissible members, is also exactly \(p\) for \(p\ge43\): (4) is
the lower bound and (2),(7) attain it. This is a restricted-source
minimum, not the unrestricted \(\delta(p)\).

The dependency-free [exact verifier](../computations/stci_arithmetic_beyond_2026_10_29.py)
checks homogeneity, nonnegative exponents and sparse polynomial pullbacks
at \(p=43,47,53,59,61,101\). Its
[saved output](../computations/stci_arithmetic_beyond_2026_10_29.json)
records every input. Run
`python3 research/computations/stci_arithmetic_beyond_2026_10_29.py`.
These are finite controls; the uniform proof is (8)--(9).

## Full conductor explanation of eventual Frobenius descent

For (2), normalization is an isomorphism off \(D=(s=0)\). Finite
duality identifies its conductor upstairs with
\(\omega_{\mathbf P^2}\otimes\nu^*\omega_X^{-1}\), since \(X\)
is a hypersurface and hence Gorenstein. The finite-duality input is
[Stacks, Lemma 48.11.4](https://stacks.math.columbia.edu/tag/0AX2);
the hypersurface calculation is given in
[de Jong's lecture notes, Lemma 1.2](https://www.math.columbia.edu/~dejong/courses/schemes-spring-2020/lecture-notes-b.pdf).
Locally the conductor identification follows because
\(\operatorname{Hom}_A(B,A)\) consists of multiplication by common-
fraction-field elements carrying \(B\) into \(A\).

Here \(\omega_X=\mathcal O_X(12)\), so the conductor ideal has
class \(\mathcal O(-3-48)=\mathcal O(-51)\). Being invertible and
supported on the single line \(D\), it is exactly
\(\mathcal O(-51D)\). With \(Q=z^4\) and
\(Q-U_2=-st^3\), every Frobenius power \(q=p^e\ge51\) has
\(Q^q-U_2^q\) in the conductor twisted by \(\mathcal O(4q)\).
Hence \(Q^q\) descends to a global section of \(\mathcal O_X(q)\),
which lifts to an ambient degree-\(q\) form by the hypersurface sequence
and \(H^1(\mathbf P^3,\mathcal O(q-16))=0\). This independently
explains how Frobenius removes the nilpotent defect, with the weaker
large-prime threshold 53. Formula (7) supplies threshold 43 without
depending on this duality calculation.

To force unrestricted \(\delta(p)\to\infty\), one still needs an
obstruction for every possible carrier/pair, or a valid reduction to
sources with a gap such as (3). This note proves neither. Arbitrary
normalizations may have nonconstant reduced phases, multiple inverse
branches, or no suitable boundary gap. The concrete advance is a
restricted-source growing lower bound, attained by explicit pairs whose
two equations are non-binomial, and a first surviving Hasse order that
retains the characteristic power invisible to ordinary differentiation.

## Geometric interpretation and exact support

The jet-gap lemma measures the first infinitesimal variation upstairs that the target local ring cannot represent. Ordinary differentiation sees only divisibility by \(p\); the first surviving Hasse order sees the whole \(p^{v_p(b)}\). Conversely, once a Frobenius difference vanishes in the full conductor, it descends. This is a relation between infinitesimal gluing and an actual homogeneous equation, and it persists for a carrier with no nonzero binomial relation.

The [dependency-free sparse verifier](../computations/stci_arithmetic_beyond_2026_10_29.py) with its [exact output](../computations/stci_arithmetic_beyond_2026_10_29.json) checks the literal identity at \(p=43,47,53,59,61,101\), all exponents and ordinary degrees. Independent direct four-variable Macaulay2 substitution at \(43,53\) was recorded in the source audit. The uniform proof is the localization identity followed by Frobenius; no inference across all primes is made from the finite controls. No fresh run was needed to preserve the proof.

[Positive-characteristic constructions](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md) supplies the family-wide rational-quartic theorem and fixed-cubic minima. [The exact binomial-family analysis](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#exact-two-binomial-reduced-support-and-endpoint-contacts) preserves the distinct characteristic-five minimum 25 in its quartic-plus-binomial family. The minimum 20 in the one-binomial class uses a different cubic carrier. A family minimum is never a lower bound for the unrestricted minimum without a coverage theorem.


## Exceptional-prime minima with their proof

## 5. A concrete characteristic-five comparison

The fixed quartic's inherited minimum mate degree is \(25\) in
characteristic five. The inherited cubic-carrier family has a smaller
maximum defining degree there. One explicit member is
\[
\begin{aligned}
F&=x_1^3-x_0^2x_2,\\
G&=x_2^{20}-3x_0x_1x_2^{13}x_3^5
 +3x_0^2x_1^2x_2^6x_3^{10}-x_0^5x_3^{15}.
\end{aligned}
\tag{A8}
\]
Its degrees are \((3,20)\). On \(x_0=1\), \(F=0\) gives
\(x_2=x_1^3\), and direct substitution gives
\[
G(1,u,u^3,v)=(u^4-v)^{15}\quad\text{in characteristic five}.
\]
Thus the affine reduced intersection is exactly
\([1:u:u^3:u^4]\). On \(x_0=0\), \(F=0\) gives
\(x_1=0\), and then \(G=x_2^{20}\); the only projective point
is \([0:0:0:1]\). This proves full projective support equality,
not only generic contact. Its generic thickness is \(15\), in
accord with (A1).

## 6. A sharper small-prime consequence

The same audited argument yields the exact restricted minima
\[
\delta_{\rm bin}(2)=\delta_{\rm bin}(3)=4,
\qquad\delta_{\rm bin}(5)=20.
\tag{A9}
\]
For \(p=2,3\), a smaller maximum would force both degrees at most
three. No degree-one equation contains \(C_0\), an admissible
binomial cannot have degree two by Section 2, and \((3,3)\) has
degree product nine, not divisible by four. The inherited
\((4,4)\) and \((4,3)\) pairs attain four.

For \(p=5\), assume a binomial pair has maximum degree less than
20 and reduce to \(F_0\) as above. If \(n_2=0\), primitivity
forces the fixed quartic \((a_0,n_0,n_3)=(4,3,1)\), whose
inherited minimum mate is 25. If \(n_3=0\), primitivity forces
the cubic \((a_0,n_0,n_2)=(3,2,1)\). The endpoint monomial
\(U^NW^{3N}\) in the pullback identity above, since \(n_2>0\), forces
\(a_0\mid N\) and hence \(4\mid b\); then \(5\mid N\)
forces \(20\mid b\), a contradiction.

In the remaining case \(n_2,n_3>0\), the same endpoint gives
\(4\mid b\), so \(b\in\{4,8,12,16\}\). From \(5\mid a_0b\)
we obtain \(a_0\in\{5,10,15\}\). The interval in the carrier reduction has no
integer solution for \(a_0=5\). For \(a_0=10\), its only
solution is \(n_0=7\). For \(a_0=15\), \(n_0=10\) is
nonprimitive, leaving \(n_0=11\). In both remaining cases
\(v_5(N)=1\). Therefore the coefficient with binomial index five
in the pullback identity above is nonzero: writing \(N=5M\), it is the index-one
coefficient in \((V^{20}-U^5W^{15})^M\), with \(5\nmid M\).
It has \(U\)-exponent five, absent from the image semigroup
\(\langle a_0,n_0\rangle\), whose smallest positive element is
at least seven. This contradiction rules out maximum degree below
20, and the displayed cubic pair attains it.

The only imported input in this small-prime sharpening is the reviewed
[fixed-quartic mate minimum](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic)
and its [independent reconstruction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#all-mate-degrees-on-a-fixed-cuspidal-quartic).
The finite arithmetic cases above are proved explicitly, rather than
being presented as an incomplete enumeration.
