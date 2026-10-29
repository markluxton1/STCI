# Searching across characteristics: the minimum degree and the binomial boundary

Started 2026-10-28; continued 2026-10-29. Author: `arithmetic_search`.

**Status:** independently reviewed provisional research synthesis, extending
an inherited binomial-carrier argument. The unrestricted characteristic-zero
STCI question remains open. The arithmetic search equivalence has an
[independent logic audit](2026-10-28-stci-search-logic-audit.md). The
binomial-carrier divisibility argument below has a separate
[arithmetic audit, verdict PASS](2026-10-28-stci-search-arithmetic-audit.md),
which independently reconstructs factor reduction, the arbitrary-mate
argument, full inverse support, and the missing coefficient. No canonical
record is changed here.

The curve throughout is the fixed integral model
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_{\mathbb Z}.
\]
In each characteristic, equations are actual homogeneous forms over the
algebraically closed coefficient field. A supported pair means
\(V(F_a,G_b)_{\mathrm{red}}=C_0\), with positive degrees. Such a pair is
automatically proper, and its generic transverse multiplicity satisfies
\(ab=4m_C\).

## 1. The exact characteristic limit that would settle the question

Define the minimum over **all** supported pairs
\[
\delta(p)=\min\{\max(a,b):V(F_a,G_b)_{\mathrm{red}}=C_0
\text{ over }\overline{\mathbb F}_p\}.
\]
The convention is \(+\infty\) if no pair exists. Known positive-
characteristic constructions make it finite for this curve.

The precise form of the user's proposed strategy is
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

The [independent logic audit](2026-10-28-stci-search-logic-audit.md) gives
both this incidence proof and a finite rank-locus construction preserving
the original scalar coefficients and properness. It also checks that
existence in an arbitrary algebraically closed characteristic-zero field
is equivalent to existence over \(\overline{\mathbb Q}\). Transcendental
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

## 2. The fixed-quartic minimum is already known

The repository's
[fixed-carrier optimality proof](2026-10-05-positive-quartic-carrier-optimality.md)
and [independent reconstruction, Section 6](2026-10-05-foundational-frontier-audit.md)
cover the quartic
\[
S=x_0x_3^3-x_2^4.
\]
For arbitrary, possibly non-binomial degree-\(N\) mates on this particular
surface, the exact criterion in characteristic \(p\) is
\[
p^{v_p(N)}\in\langle3,4\rangle.
\tag{2}
\]
Thus the minimum mate degrees are \(4\) in characteristic two, \(3\)
in characteristic three, \(25\) in characteristic five, and \(p\)
for \(p\ge7\). In characteristic zero this carrier has no mate.
These are independently reviewed historical results, with no separate
canonical result record for the positive-characteristic minimum.

The [all-prime construction note](2026-10-27-positive-characteristic-construction-interface.md)
records actual equations. For \(q\in\langle3,4\rangle\), choose
\(r,t\ge0\) with \(3r+4t=q\) and set \(h=2r+3t\). Then
\[
G_q=x_1^q-x_0^h x_2^r x_3^t
\]
has degree \(q\). The proper pair \((S,G_q)\) has sole reduced support
\(C_0\) precisely when \(q\) is a power of the characteristic. In
characteristic zero it has \(q\) actual quartic components. The same
historical sources also contain cubic-carrier constructions of degrees
\((3,4p)\), so the fixed quartic's minimum is not a global minimum
theorem.

Equation (2) already proves the suggested smaller-degree statement **on
that carrier**. It cannot imply unrestricted characteristic-zero
nonexistence: minimizing over additional carriers can lower a minimum.
The promoted [R-0001](../results/quartic_carrier_exclusion.md) already
excludes every integral quartic carrier in characteristic zero. The
remaining search uses higher-degree carriers.

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

The [independent arithmetic audit, Sections 5–6](2026-10-28-stci-search-arithmetic-audit.md)
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

## 4. The next all-pairs interface and a tempting failed reduction

A concrete sufficient target for the unrestricted arithmetic strategy is:

> For arbitrarily large primes \(p\), every supported pair for this
> curve has \(p\mid m_C\).

By (3), the assertion is now understood in the one-binomial class. If
proved for arbitrary pairs it would give \(\delta(p)\ge p\) along
those primes and settle characteristic-zero nonexistence by (1). The
assertion for **two non-binomial equations** is open. No automatic
lifting or tameness theorem when \(p>\max(a,b)\) has been established
by the arguments here.

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

## 5. Evidence and remaining limits

- **Inherited, promoted:** R-0001 excludes integral quartic carriers in
  characteristic zero and, with its factor reduction, forces both
  hypothetical degrees to be at least five.
- **Inherited, reviewed historical:** the exact arbitrary-mate degree
  criterion (2) on the fixed cuspidal quartic, with its source and audit
  linked in Section 2.
- **Primary literature inspected in this run:** Thoma (1989), especially
  Theorems 2.3, 2.4 and 3.1, through the author-uploaded text linked in
  Section 3; and Stacks Tag 054K for constructibility. Direct AMS access
  to Moh (1985) failed, so no newly inspected theorem number or proof is
  attributed to Moh here. The exact constructions used are already
  available in repository evidence.
- **Reviewed provisional exact reduction:** (1), with the separate
  search-logic audit. It is qualitative and gives no effective prime
  cutoff or termination bound.
- **New reviewed provisional deduction:** (3), (9), and the exceptional-
  prime minima, with the independent arithmetic audit linked above.
  They cover one-binomial
  pairs, including non-binomial mates, and do not cover every carrier.
- **Unresolved:** any lower bound on \(\delta(p)\) covering all pairs,
  an exhaustive reduction of two non-binomial equations to an understood
  class, or an actual characteristic-zero supported pair.

No previously accepted proof was rerun to write this note. No finite
enumeration of primes is presented as a proof of the universal statements.
