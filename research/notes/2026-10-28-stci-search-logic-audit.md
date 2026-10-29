# Independent audit: finite searches and the characteristic limit

Date: 2026-10-28. Reviewer: `search_logic_audit`, with an independent
constructibility check by `search_logic_audit/constructibility_check` and
comparison with `arithmetic_search/spreadout_audit`.

Status: **PASS for the exact reduction below; provisional, not canonically
promoted.** This is an audit of the proposed search logic. It neither proves
existence nor nonexistence of an STCI for the fixed quartic. No accepted
proof or inherited computational certificate was rerun.

## 1. Question, quantifiers and inherited input

Throughout, the curve is
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3
\]
over an algebraically closed field. Characteristic zero and every positive
characteristic are considered separately. Defining equations are actual
homogeneous forms with scalar coefficients, of positive degrees \(a,b\).
They contain \(C_0\). A proper pair means that they have no common surface
factor; its complete intersection is pure of dimension one.

The inherited, independently reviewed fixed-degree test is in
[the finite endpoint, Section 6](2026-10-26-boundary-repair-global-lifting.md)
and its [audit, Section 6](2026-10-26-boundary-repair-global-lifting-audit.md).
[The rank-locus audit, Sections 1–3](2026-10-27-intersections-integration-audit.md)
also checks coefficientwise equations and the proper-pair restriction.
These are reviewed provisional sources, rather than additional canonical
records. This note audits their extension to an arithmetic parameter space.

## 2. Explicit fixed-degree parameter space over the integers

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
along \(C_0\). The inherited degree/Artin-length argument gives
\[
\ell\le M,\qquad n-\operatorname{rank}_{k(t)}T=\ell.
\]
Consequently
\[
\sqrt{(F,G)}=I_{C_0}
\quad\Longleftrightarrow\quad
\operatorname{rank}_{k(t)}T\le n-M.\tag{1}
\]
The radical here describes projective reduced support, equivalently the
radical of the saturated homogeneous ideal. Degree exhaustion and purity
are essential for (1); the same rank equations outside the proper locus
are not an STCI certificate.

Set every coefficient in \(t\) of every \((n-M+1)\)-minor to zero.
This is a finite collection of equations over \(\mathbb Z\), valid after
specialization to every characteristic. It defines a closed condition
on each affine coefficient chart, invariant under nonzero rescaling of
either form. Therefore the STCI locus \(Z_{a,b}\) is closed relative to
\(U_{a,b}\), in particular a scheme of finite type over \(\mathbb Z\).
This construction keeps coefficients in \(k\), rather than allowing
arbitrary choices in \(k(t)\).

## 3. Independent incidence proof of constructibility

There is a shorter proof that does not use (1). In the universal
intersection \(Y\subset\mathbf P^3\times P_{a,b}\), remove the fixed
closed subscheme \(C_0\times P_{a,b}\). A parameter is bad exactly when
the resulting open subscheme has a nonempty geometric fiber over it.
By [Chevalley's theorem, Stacks Tag 054K](https://stacks.math.columbia.edu/tag/054K),
the image of this open subscheme in \(P_{a,b}\) is constructible. Its
complement is the geometric sole-support locus and is constructible.
Any such sole-support pair is automatically proper: a common surface
would lie in its reduced support. This is the independent route supplied
by the arithmetic audit lane and reconstructed here.

Both proofs give the same constructibility conclusion. The rank version
additionally specifies an exact finite algebraic search; the incidence
version does not pretend to compute its defining equations.

## 4. The characteristic dichotomy at a fixed degree bound

For an integer \(B\ge1\), take the finite union of the loci for
\(1\le a,b\le B\). Its image \(E_B\subset\operatorname{Spec}\mathbb Z\)
is constructible by Chevalley. A constructible subset containing the
generic point contains an open neighbourhood of it; a constructible
subset missing the generic point misses an open neighbourhood of it.
See [Stacks Lemma 28.2.2](https://stacks.math.columbia.edu/tag/054B).
Every nonempty open subset of \(\operatorname{Spec}\mathbb Z\) contains
all but finitely many prime points. Therefore exactly one alternative
holds:

1. There is an STCI pair with both degrees at most \(B\) in characteristic
   zero, and there is such a pair over \(\overline{\mathbb F}_p\) for all
   sufficiently large primes \(p\).
2. There is no such pair in characteristic zero, and such pairs exist
   over \(\overline{\mathbb F}_p\) for only finitely many primes \(p\).

Existence in an arbitrary algebraically closed characteristic-zero field
is equivalent to existence over \(\overline{\mathbb Q}\), because each
nonempty finite-type stratum over \(\mathbb Q\) has a closed point over
a finite extension of \(\mathbb Q\). Likewise, a nonempty fiber over
\(\mathbb F_p\) has a point over its algebraic closure. No rational
coefficients or \(\mathbb F_p\)-rational coefficients are asserted.

The same dichotomy applies to a single exact degree pair. Thus existence
at a fixed degree pair in infinitely many distinct characteristics is
already equivalent to characteristic-zero existence at that pair.

## 5. What a global minimum-degree theorem would accomplish

Define
\[
\delta(p)=\min\{\max(a,b):\sqrt{(F_a,G_b)}=I_{C_0}
\text{ over }\overline{\mathbb F}_p\},
\]
with \(+\infty\) if there is no pair. Known positive-characteristic
existence makes it finite here, but is not needed for the equivalence
with the extended-value convention.

The exact conclusion of Section 4 is
\[
C_0\text{ is not an STCI in characteristic zero}
\quad\Longleftrightarrow\quad
\delta(p)\longrightarrow\infty\quad(p\text{ through primes}).\tag{2}
\]
Equivalently, an unbounded sequence of actual values of \(\delta(p)\)
along primes suffices: a characteristic-zero pair would impose one
eventual bound. Conversely characteristic-zero nonexistence forces the
full limit in (2), rather than merely an unbounded subsequence.

This validates the user's proposed strategy after adding its missing
quantifier: the lower bound must cover **every global defining pair**,
or an exhaustive class to which every pair reduces. A lower bound for
mates of one fixed quartic does not bound \(\delta(p)\) below: taking a
minimum over more carriers can lower the answer. An upper construction
whose degrees grow with \(p\) likewise gives no lower bound.

## 6. Audit limits and search implications

- No exceptional-prime set or effective cutoff is computed. Its existence
  follows from constructibility at each fixed degree bound.
- Enumerating primes and finding only the known Frobenius examples does
  not establish a lower bound for all pairs.
- Failure to find \(\mathbb F_p\)-rational solutions does not establish
  geometric emptiness; extensions must remain allowed.
- A small successful family is a candidate source, not an exhaustive
  parameter space. An empty proper rank locus **for all global pairs at
  fixed degrees** is an exact exclusion for those degrees.
- Increasing \(B\) after each empty search is a valid search procedure,
  but no termination theorem or uniform witness-degree bound follows.

The arithmetic strategy is therefore mathematically equivalent to the
original problem in its fully unrestricted form. Its potential advantage
is that Frobenius, integral coefficient relations and finite-field
geometry may expose a usable global lower bound. That advantage must be
demonstrated by a bound covering all carriers, not inferred from the
already known fixed-quartic construction.

## 7. Addendum: an exact positive test on the degree-eight quadric model

Continuation date: 2026-10-29. This addendum independently checks the
candidate-inventory lane's proposed construction interface. Its scope is
one of the three necessary Cartier singleton normalization models of
[STCI-R-0002](../results/cartier_singleton_lift.md), not all STCI pairs.

Let \(S=\mathbf P^1\times\mathbf P^1\), with coordinates
\(([u_0:u_1],[v_0:v_1])\), and put
\(\Delta=u_0v_1-u_1v_0\). Its diagonal is a \((1,1)\) curve.
Choose the four \((2,2)\) sections
\[
B=(u_0^2v_0^2,\ u_0^2v_0v_1,\ u_0u_1v_1^2,\ u_1^2v_1^2).
\]
They restrict to \((s^4,s^3t,st^3,t^4)\) on the diagonal. Every lift with
exactly those fixed restrictions is uniquely
\[
U_i=B_i+\Delta A_i,\qquad A_i\in H^0(S,\mathcal O_S(1,1)).\tag{3}
\]
Indeed, the kernel of restriction of \((2,2)\) sections is
\(\Delta H^0(\mathcal O_S(1,1))\); the restriction map is surjective.
Thus (3) is an actual 16-parameter family of global sections.

For a chosen parameter, check that the four sections have no common
zero. This basepoint-free condition automatically makes the resulting
map finite onto its image: a positive-dimensional proper fiber contains
a curve, whereas the ample bundle \(\mathcal O_S(2,2)\), being the pullback
of \(\mathcal O_{\mathbf P^3}(1)\), would have degree zero on that curve.
The map must **separately** be checked birational to identify the image
as a degree-eight surface with normalization \(S\). A finite map could
have degree \(e>1\), in which case its image has degree \(8/e\).

For a basepoint-free birational parameter \(U\), with image \(X\),
**whose full reduced inverse support of \(C_0\) is the diagonal**, the
positive mate criterion is exactly
\[
\text{a degree-}b\text{ mate on }X\text{ exists}
\quad\Longleftrightarrow\quad
\Delta^{2b}\in
\operatorname{span}_k\{U_0^{\alpha_0}\cdots U_3^{\alpha_3}:
|\alpha|=b\}.\tag{4}
\]
For necessity, pull back a mate section. If the full reduced inverse
support is the diagonal, its zero divisor on the smooth surface is
\(m\Delta\). Comparing classes \((2b,2b)=m(1,1)\) gives \(m=2b\);
the ratio to \(\Delta^{2b}\) is a nowhere-vanishing global function, hence
a scalar. For sufficiency, an identity
\(G(U)=\Delta^{2b}\) supplies the actual global equation directly. It
does not vanish identically on \(X\), and its inverse zero support is
exactly the diagonal, whose image is \(C_0\). Hence \((F_X,G)\) is an
STCI pair. The exact identity includes every conductor-descent condition;
no additional phase test is needed after it succeeds.

Full singleton inverse support is a useful independent early rejection
test. It is also forced by a successful identity in (4): restriction to
the diagonal shows \(G\) vanishes on \(C_0\), so every point over \(C_0\)
must be in the zero support \(\Delta\). Consequently the necessity part
of (4) requires singleton support, while the sufficiency part proves it.
Without that support hypothesis, failure of (4) alone does not rule out
all mates: a mate could pull back to a divisor on extra inverse curves.
For the proposed singleton-model search, the hypothesis is explicit.

At fixed \(b\), (4) is a finite linear membership problem in the
coefficients of \(G\), with nonlinear dependence on the 16 map
parameters. Its matrix has \((2b+1)^2\) rows and
\(\binom{b+3}{3}\) columns before deleting kernel relations. Membership
means the augmented matrix has the same rank as the section matrix;
unknown-parameter searches must keep its rank strata. Assuming maximal
rank in advance can discard exceptional candidates. Each fixed-\(b\)
locus is constructible, consistent with
[STCI-R-0004](../results/projection_phase_reduction.md): its warning that
the unbounded mate locus need not be constructible concerns an infinite
union over degrees.

The criterion and elementary finiteness proof work in every
characteristic for maps meeting their hypotheses. The canonical
classification selecting this model is characteristic-zero scoped;
neither that classification nor birationality can be inferred in
positive characteristic from the diagonal restriction alone.

As an independent check of a completed failure, set
\(a=u_0v_0,b=u_0v_1,c=u_1v_0,d=u_1v_1\) and examine
\[
U=(a^2+\Delta^2,\ ab,\ dc,\ d^2+\lambda\Delta^2),
\qquad\Delta=b-c.
\]
In the chart \(u_0=v_0=1,v_1=0,u=u_1\), these become
\((1+u^2,0,0,\lambda u^2)\). At either characteristic-zero root of
\(u^2=-1\), the point is off the diagonal and maps to
\([0:0:0:1]\in C_0\) when \(\lambda\ne0\), whereas \(\lambda=0\)
has basepoints. Thus this pencil fails the singleton-model filter for
every parameter. This independently reconstructs the
[candidate note's endpoint test](2026-10-28-stci-search-quadric-test.md);
it does not exclude the full family (3), the quadric-cone model, or
other inverse-lift geometries.

## 8. Updated quadric candidate: the off-diagonal scheme has length sixteen

Continuation date: 2026-10-29. The candidate-inventory lane next changed
the map to
\[
U=(a^2+\Delta^2,\ ab+\Delta^2,\ dc+2\Delta^2,
\ d^2+3\Delta^2),\qquad ad=bc,\quad\Delta=b-c.\tag{5}
\]
This does repair both middle coordinates. It is basepoint free. On the
diagonal the prescribed quartic is basepoint free. Off the diagonal use
\(\Delta=1\). A common zero of \(U_0,U_1\) would give \(a^2=-1\)
and \(b=a\), hence \(a\ne0\) and \(ad=bc\) gives \(d=c\).
Then \(U_3-U_2=1\), a contradiction. The ample-line-bundle argument in
Section 7 therefore makes this a finite morphism onto its integral image.

The exact chart used in the computation warrants care. The Segre surface
is
\(\operatorname{Proj}\mathbb Q[a,b,c,d]/(ad-bc)\), with all four
variables of degree one. Its entire off-diagonal locus is the single
affine projective chart \(D_+(\Delta)\), whose coordinate ring is
\[
\mathbb Q[a,b,c,d]/(ad-bc,b-c-1).
\]
Setting \(\Delta=1\) is unique ordinary projective scaling in these
Segre coordinates. It introduces no covering degree or extra scale
multiplicity from the original two factors of \(\mathbf P^1\).

On this chart pull back the four actual ideal generators
\[
x_0x_3-x_1x_2,\quad x_0^2x_2-x_1^3,\quad
x_0x_2^2-x_1^2x_3,\quad x_2^3-x_1x_3^2
\]
of \(C_0\). Because the map is basepoint free, there are no simultaneous
target-coordinate zeros creating spurious inverse points. This ideal
computes the full scheme-theoretic inverse of \(C_0\) on
\(D_+(\Delta)\); no further saturation by \(\Delta\) is needed after
it has been made a unit.

The reviewer independently replayed
[the updated Macaulay2 script](../computations/stci_search_quadric_updated_2026_10_29.m2).
It returned dimension zero and degree sixteen, and the additional command
`numgens source basis(R/J)` gave sixteen for the quotient's vector-space
basis. Thus the
precise assertion is a **nonempty off-diagonal inverse scheme of length
sixteen over \(\mathbb Q\)**. Base extension to
\(\overline{\mathbb Q}\) preserves that length. Neither sixteen distinct
points nor reducedness is asserted.

Its points are isolated in the full inverse support: all off-diagonal
inverse support lies in this affine chart, where it is zero dimensional.
Consequently this particular image admits no mate, even without deciding
birationality. Indeed, the pullback of a putative mate would be a nonzero
section of \(\mathcal O_S(2b,2b)\) whose zero support is the full inverse
of \(C_0\). A nonzero section of a line bundle on the smooth integral
surface has an effective Cartier zero divisor, with no isolated
zero-dimensional component. The computed isolated inverse points
contradict that requirement.

Reviewer outcome: **PASS for the literal map (5), basepoint-freeness,
projective-chart interpretation, length-sixteen assertion, and resulting
no-mate rejection of this map's image.** No genericity, birationality,
distinctness, characteristic-\(p\), or exhaustive degree-eight claim is
made. This second failure shows that varying the middle coordinates is
insufficient by itself; the next search must impose full inverse support
as an actual condition on the parameter source.
