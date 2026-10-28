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
