# Endpoint three-common-root family: shifted-variable support certificate

Status: **PROVED, exact univariate algebra in characteristic zero.** This
note excludes the polynomial support condition in the corrected `U | V`
family. The parent's geometric identification of that condition and the
other common-root strata are separate obligations.

## Correct family and sign correction

For

\[
U=2az^3-3bz^2-z+g,\qquad
V=3az^4-4bz^3-2z^2-z+d,
\]

with `a != 0`, ordinary long division gives

\[
V-\left(\frac32z+\frac b{4a}\right)U
=\left(-\frac12+\frac{3b^2}{4a}\right)z^2
 +\left(-1-\frac32g+\frac b{4a}\right)z
 +d-\frac{bg}{4a}.
\]

Thus `U | V` requires and is equivalent to

\[
a=\frac32b^2,\qquad
g=\frac1{9b}-\frac23,\qquad
d=\frac1{54b^2}-\frac1{9b},\qquad b\ne0.
\]

The initially supplied negative sign for `a` was an exploratory error and
is rejected. It gives a nonzero `z^2` remainder. The corrected family has

\[
C_b=a^2g-ab-b^3=-\frac34b^3(2b+3).
\]

The admissible locus `C_b != 0` is therefore exactly `b != 0,-3/2`.

## Cleared polynomials and incompatible necessary resultants

Set

\[
A=az-b,\quad h=az^3+z-g-1,\quad J=AV-(Az-1)U,
\quad E=J^2-(3zA-1)hJ+AUh^2.
\]

Because `U | V`, one has `U | J` and `U | E`. Write `S=E/U`.
The change of variable `x=3bz-1` is invertible for every allowed parameter.
The exact cleared expressions are

\[
p=9bU=x^3-6x-6b-4,
\]

\[
\begin{aligned}
q=432bS={}&-(4b+6)x^4-(14b+9)x^3-48bx^2\\
&+(24b^2-26b+15)x-24b^2-340b.
\end{aligned}
\]

Hence `p` has degree three and `q` has degree four on the entire allowed
locus. Direct exact determinants of the two degree-seven Sylvester matrices
give

\[
\operatorname{Res}_x(p,q)=-1458R(b),\qquad
\operatorname{Res}_x(q,q')=7776D(b),
\]

where

\[
R=(12b^2+116b+3)(72b^4+252b^3+1126b^2+513b+54),
\]

\[
\begin{aligned}
D={}&(2b+3)(2b^2+9b+15)^2\\
&\cdot(9216b^6-208896b^5-2002096b^4-2800992b^3
-117672b^2+72b+45).
\end{aligned}
\]

Exact polynomial arithmetic in `QQ[b]` gives `gcd(R,D)=1`.

If every root of `q` were a root of `p`, they would share at least one root,
and the quartic `q` would have a repeated root because its distinct roots
would lie among at most three cubic roots. Both resultants would vanish.
Their nonzero constant factors and the coprimality of `R,D` make that
impossible. Thus **there is no allowed parameter with
`Supp(S) subset Supp(U)`**, including parameters with repeated roots of `U`.
Since `E=US`, this also proves that `E` has a root outside `U` throughout
the allowed family. There is no exceptional finite parameter set.

## Independent computation and preserved execution history

The source
[verify_session_endpoint_three_common_roots_2026_10_11.m2](../computations/verify_session_endpoint_three_common_roots_2026_10_11.m2)
has SHA-256
`31597e4c2057fabb87f9aaf76fdd562f1d5753cf75141dc0f85dfc3041eb97a1`.
Its final captured execution passes **nine exact assertions**: the two
divisibilities, the shifted cubic, the quotient, the carrier coefficient,
the shifted quartic, both resultant identities and their coprimality.

The [execution record](../validation/2026-10-11-endpoint-three-common-roots/execution-record.json)
retains five captured source snapshots with stdout and stderr. The first
failure is a fraction-field construction error; the second is an unsupported
generic polynomial-gcd call; the third is a coefficient-ring construction
error caught by a failed resultant assertion. In that third attempt,
`coefficient(x^k, f)` in `QQ[b,x]` discarded terms with positive powers of
`b`. The final construction uses `QQ[b][x]`, retaining the full coefficient
polynomials. Attempt four passes the development assertions; attempt five
passes the final nine assertions and checks the exact nonzero resultant
constants. All failures remain preserved. An initial uncaptured invocation
of the same failed source as attempt one appears in the tool transcript;
it supplies no additional certificate.

The separate
[residual-quartic independent audit](2026-10-11-session-three-common-roots-residual-quartic-independent-audit.md)
works directly in the original variable `z` and obtains the same parameter
factors, with its own captured eight-assertion source. The two sources are
independent implementations of this algebraic certificate; execution
snapshots of either source are copies, not additional implementations.
