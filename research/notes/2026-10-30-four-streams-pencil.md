# The full-ideal pencil can have exceptional covers of unbounded genus

Date: 2026-10-30. Author: `pencil_resolution_geometry`.
Status: **independently reviewed provisional**, with the
[independent proof audit](2026-10-30-four-streams-pencil-audit.md).
This is not a construction or exclusion for the fixed
quartic. No canonical mathematical status is changed.

## Question, retrieved evidence, and outcome

The motivating question is whether resolving a hypothetical supported
complete intersection on
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) in characteristic zero
forces exceptional covers sufficiently rigid to exclude every degree pair,
including common-singular and entirely-thick carriers.

The full-ideal exceptional-divisor statements are already proved in the
[October 19 Rees audit, §§2–5](2026-10-19-rees-residual-independent-audit.md):
the reduced exceptional divisor is a ruled surface; every exceptional prime
of the normalized blowup dominates the support curve; and its coefficients
and finite degrees satisfy the multiplicity identity. These are reused,
not offered as new conclusions. The
[October 28 graph note](2026-10-28-residual-degree-blowup-bounds.md)
already identifies the limit of nef inequalities on the first blowup.

The new outcome is a global characteristic-zero counterexample to an
automatic rationality or unramifiedness bridge. Two **integral surfaces of
equal degree**, both singular along a smooth rational support curve, can
have a supported complete intersection whose unique normalized-blowup
exceptional prime has normalization \(D\times\mathbf P^1\), where
\(D\to\mathbf P^1\) is a branched cyclic cover of unbounded genus. Its
finite map to the reduced exceptional ruled surface is exactly the product
of that cover with the identity.

The example uses a line, not \(C_0\). It refutes only implications asserted
from the stated general hypotheses. It supplies neither equations for
\(C_0\) nor evidence that the same cover occurs over \(C_0\).

## 1. The construction and precise claim

Work over an algebraically closed field \(k\) of characteristic zero.
Choose integers \(d\ge2\), \(e\ge1\), and put

\[
n=d(e+1),\qquad A=Z^{de}-W^{de}.
\]

In \(\mathbf P^3_{[X:Y:Z:W]}\), let

\[
G=Y^n+X^dA,\qquad F=G+X^n,
\qquad L=V(X,Y).
\tag{1}
\]

Let \(Y_0=V(F,G)\), \(B=\operatorname{Bl}_{\mathcal I_{Y_0}}\mathbf P^3\),
and \(\nu:\overline B\to B\) be normalization. Write \(E\) for the
effective Cartier exceptional divisor on \(B\).

**Proposition.** The following hold.

1. Both \(F\) and \(G\) are irreducible. Their surfaces are singular at
   every point of \(L\). The proper complete intersection \(Y_0\) has
   sole reduced support \(L\) and generic multiplicity \(n^2\).
2. The reduced exceptional surface is
   \(E_{\mathrm{red}}\simeq L\times\mathbf P^1\). The second factor is
   the actual equal-degree pencil with generators \(X^n,G\).
3. There is exactly one exceptional prime divisor \(T\) on
   \(\overline B\). Its normalization is
   \[
   T^\nu\simeq D\times\mathbf P^1,
   \tag{2}
   \]
   where \(D\) is the smooth projective curve with function field
   \[
   k(D)=k(t)(\beta),\qquad \beta^d=1-t^{de}.
   \tag{3}
   \]
   Under (2), the finite map to \(E_{\mathrm{red}}\) is
   \((D\to L)\times\operatorname{id}_{\mathbf P^1}\), of degree \(d\).
4. The cover \(D\to L\) is totally ramified at the \(de\) distinct
   roots of \(t^{de}=1\), is unramified elsewhere, and
   \[
   g(D)=\frac{(d-1)(de-2)}2.
   \tag{4}
   \]
   The exceptional coefficient is
   \[
   \nu^*E=n(e+1)T.
   \tag{5}
   \]

In particular, taking \(d=2\) gives \(g(D)=e-1\), so the irregularity
of the smooth normalization of the exceptional prime is unbounded.

## 2. Integral carriers and sole support

The equality of ideals

\[
(F,G)=(X^n,G)
\tag{6}
\]

immediately gives \(\sqrt{(F,G)}=(X,Y)\): modulo \(X\), the second
generator is \(Y^n\). The two generators form a regular sequence because
\(G\) is not divisible by \(X\). Over the generic point of \(L\), monic
division gives the basis \(x^iy^j\), \(0\le i,j<n\), for the quotient
by \((x^n,y^n+A(t)x^d)\). Its length is \(n^2\), agreeing with the
projective complete-intersection degree since \(\deg L=1\).

For irreducibility of \(G\), view it as a polynomial in \(Y\) over the
UFD \(k[X,Z,W]\). Eisenstein at any one of the distinct prime factors
\(Z-\zeta W\) of \(A\) applies: the constant term \(X^dA\) has
valuation one there. Gauss's lemma proves irreducibility.

For \(F\), its constant term as a polynomial in \(Y\) is

\[
X^d(X^{de}+Z^{de}-W^{de}).
\]

The parenthesized polynomial is squarefree: a repeated prime factor would
divide all three partial derivatives, hence divide the relatively prime
monomials \(X^{de-1},Z^{de-1},W^{de-1}\), which is impossible. It has
no factor \(X\). Eisenstein at any one of its prime factors again
applies, proving irreducibility of \(F\).

Every term of both polynomials has order at least \(d\ge2\) along
\((X,Y)\). All first partial derivatives therefore vanish along \(L\),
including the derivatives in \(Z,W\). Thus these are integral,
entirely-thick carriers with common singular locus containing \(L\).

## 3. Direct calculation of the normalized exceptional prime

On \(W\ne0\), write \(x=X/W\), \(y=Y/W\), \(t=Z/W\), and set
\(K=k(t)\), \(A(t)=t^{de}-1\). Localize at the generic point of \(L\).
The blowup chart on which the generator \(x^n\) is used has coordinate
\(\lambda=G/x^n\), and equation

\[
\lambda x^n=y^n+A(t)x^d.
\tag{7}
\]

Because the ideal is a regular sequence, this is the actual blowup chart,
not an enlarged symmetric-algebra chart. The generic exceptional prime
has \((x,y)=0\) and residue field \(K(\lambda)\).

In the fraction field adjoin the already rational element

\[
\beta=\frac{y^{e+1}}x.
\]

It is integral over the chart, since (7) gives

\[
\beta^d=\lambda x^{de}-A(t).
\tag{8}
\]

The polynomial \(\beta^d+A(t)\) is irreducible over \(K\), and remains
irreducible over the purely transcendental extension \(K(\lambda)\).
For example, Eisenstein at \(t-1\) proves the first assertion over
\(k[t]\). Consequently this finite birational extension of the local
ring at the generic exceptional prime has a unique maximal ideal, with
residue field

\[
K(\lambda)(\beta),\qquad \beta^d=-A(t).
\tag{9}
\]

Here \(\beta\) is a unit, and

\[
x=\frac{y^{e+1}}\beta.
\tag{10}
\]

The maximal ideal of the extension is therefore generated by \(y\).
It is a one-dimensional Noetherian local domain with principal maximal
ideal, hence a DVR. Being finite and birational over the original local
ring and integrally closed, it is its normalization.

This proves that exactly one normalized prime lies over the generic
exceptional prime. The reused full-ideal theorem excludes additional
exceptional prime divisors over closed points of \(L\): a finite
normalization cannot create a surface over a one-dimensional blowup
fiber. Thus \(T\) is the unique exceptional prime globally.

Its valuation, normalized by \(v(y)=1\), satisfies

\[
v(x)=e+1,\qquad
v(x^n)=v(G)=n(e+1).
\tag{11}
\]

The last equality uses \(G=\lambda x^n\), with \(\lambda\) a unit at
the generic exceptional prime. This proves (5). Its residue field is
precisely \(k(D)(\lambda)\), with the indicated inclusion
\(k(L)(\lambda)\subset k(D)(\lambda)\).

Since both defining equations have degree \(n\), the reduced exceptional
surface is \(L\times\mathbf P^1\). Normalizing this surface in
\(k(D)(\lambda)\) gives \(D\times\mathbf P^1\): this product is normal
and finite over \(L\times\mathbf P^1\), with the required function
field. Uniqueness of normalization proves (2) and the claimed finite
map. This argument determines the normalization of \(T\); it does not
assert that \(T\) itself is normal inside \(\overline B\).

As a separate consistency check, the inherited coefficient identity gives

\[
\bigl(n(e+1)\bigr)d=n^2,
\]

exactly the transverse complete-intersection multiplicity. No finite
computation or normal-form classification is being substituted for the
local normalization calculation above.

## 4. Ramification and geometric interpretation

Equation (3) is a connected cyclic cover because \(1-t^{de}\) has
simple zeros. Each of its \(de\) zeros gives one point of ramification
index \(d\). At infinity put \(s=1/t\) and \(\gamma=\beta s^e\);
then

\[
\gamma^d=s^{de}-1.
\]

At \(s=0\) its \(d\) roots are distinct and nonzero, so the cover is
unramified there. Riemann–Hurwitz now gives

\[
2g(D)-2=-2d+de(d-1),
\]

which is (4). The ramification divisor of
\(D\times\mathbf P^1\to L\times\mathbf P^1\) is
\(\sum_{p\in\operatorname{Ram}(D/L)}(d-1)\{p\}\times\mathbf P^1\).
It consists of whole pencil-direction curves over special points of the
support. It does not represent additional curve support downstairs.

Geometrically, the successive transverse root directions are not defined
over \(k(L)\); their field of definition is the cyclic extension
\(k(D)\). Normalizing the full blowup retains those directions as a
cover of the entire exceptional ruled surface. Its irregularity comes
from \(D\), despite the rationality of both the ambient threefold and
the support line. For \(d=2,e=2\), for example, the two integral sextics
in (1) give an elliptic \(D\); increasing \(e\) gives every genus.

## 5. What the proposed general proof would still need

The example disproves each of the following statements when based only
on a characteristic-zero smooth rational support, an actual two-generator
complete intersection, and integral entirely-thick carriers:

- every normalized exceptional prime is a rational surface;
- its field of constants over the support is unchanged;
- its finite map to the reduced exceptional ruled surface is unramified;
- nontrivial ramification or irregularity forces a residual curve outside
  the support;
- the genus of the exceptional cover is bounded by the genus of the
  support alone.

It does **not** disprove a theorem using the particular embedding of
\(C_0\), its normal bundle \(\mathcal O_{\mathbf P^1}(7)^2\), its
quadric flag, or a comparison with the actual global equation spaces.
Any useful universal quartic obstruction through this pencil geometry
must constrain the allowable cover/ramification/conductor data using
that additional geometry. Neither ordinary exceptional ruledness nor
characteristic-zero separability supplies the missing constraint.

For unequal degrees \(a,b\), the original full-ideal exceptional surface
over \(C_0\) is
\(\mathbf P_{C_0}(\mathcal O_{C_0}(-a)\oplus\mathcal O_{C_0}(-b))\),
isomorphic to \(\mathbb F_{4|a-b|}\). The raw expression \([F_a:G_b]\)
is a section of the associated projective bundle away from the base
locus, not an ordinary map to a fixed \(\mathbf P^1\). Taking suitable
powers gives an equal-degree pencil with the same reduced support but
changes the full ideal and its blowup. Such replacement cannot silently
identify the two exceptional constructions.

## 6. Literature boundary and review requirements

The primary literature check used
[Jaffe, *Applications of iterated curve blowup to set-theoretic complete
intersections in P3*](https://arxiv.org/pdf/alg-geom/9410008), especially
the introduction and its hypotheses: the degree-finiteness theorem assumes
no common singularities, and the iterated-section construction assumes
the support is not contained in either carrier's singular locus. The
family (1) intentionally lies outside those hypotheses. It does not
contradict Jaffe's theorems.

[Stacks, blowups](https://stacks.math.columbia.edu/tag/01OF) supplies the
standard effective-Cartier and universal-property framework.
[Swanson, *Rees Valuations*, §2](https://www.math.purdue.edu/~iswanso/reesvals.pdf)
describes the normalization-of-blowup-chart construction of Rees valuation
rings. The displayed DVR calculation proves the instance used here.
No claim of literature novelty or exhaustive search is made.

Independent review should reconstruct irreducibility, the localization
and finite normalization in (7)–(10), the uniqueness of the exceptional
prime, the passage from its function field to its global normalization,
and the branch calculation at infinity. It should test the controls
\((d,e)=(2,1),(2,2)\), and distinguish \(T\) from \(T^\nu\).
The unrestricted characteristic-zero STCI question for \(C_0\) remains
unresolved by this contribution.
