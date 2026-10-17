# Continuation audit: the nonendpoint trisecant stratum is excluded

Session date: 2026-10-10. Auditor: `trisecant_nonendpoint_audit`.
Status: **PROVED HERE / independent global coverage audit passed**, using
the accepted inputs identified below. No canonical frontier file is
edited. This proves a bounded mate exclusion for the fixed monomial
rational quartic in characteristic zero; it does not resolve arbitrary
carrier degrees or the universal STCI question.

## 1. Binding source and scope

The owner proof is
[the nonendpoint trisecant conic obstruction](2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstruction.md),
SHA-256
`5d02eb6f79da5e4c367a472a5ce711dfe42953bfb78abefed82459027831c975`.
The following separately accepted inputs were read in full for this audit:

* [Normal ambient conic model](2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md),
  SHA-256 `8b2f8b2c73f95b5b71854425359fc9c8dfa188156ccc8375bc8acd513619d41b`.
* [Actual entire conductor](2026-10-10-session-genus-two-entire-conductor-independent-audit.md),
  SHA-256 `77bc3c17b7832907fd2d859de6e4d82735f6b279efb923ecd9a865fbc0767550`.
* [Lambda-one marked-prime classification](2026-10-10-session-genus-two-lambda-one-marked-prime-audit.md),
  SHA-256 `c7dd16ed8d9c18c921faaaaba130daec59fd2aec845f4ce59a9232567bb22f34`.
* [Exclusion with the degree-zero horizontal prime absent](2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md),
  SHA-256 `f6ac621d0906917947cbc5ea2ecb91c7ef85ab81129e8b1e2a9527fb47c07f26`.

Let `X` be an integral nonnormal quartic carrier of

    C0=[s^4:s^3t:st^3:t^4]

over an algebraically closed field of characteristic zero, and suppose
its normalization has sectional genus two. Assume a mate of any positive
degree exists in the retained lambda-one stratum. The accepted inputs
then give a resolution `M`, the smooth embedded lift `c#`, and

    f.c#=1,       c# ~ L-Z,
    Z effective rational sigma-exceptional,
    K_M.Z=1,      Z.E=-c#.E for every sigma-exceptional prime E.

There is an actual normal Du Val strict transform

    rho:M -> T subset Bl_Gamma(P3),
    D_T=E_B|T,       E_B=P1_Gamma x P1_f,       [D_T]=(2,2).

Only vertical (-2) exceptional curves are contracted by `rho`; the
subsequent map `T->S` contracts the horizontal (-3) sections. The
absence-of-B exclusion forces the actual prime

    B=e0-e_i-e_j,       B^2=-3,       f.B=1,       c#.B=0.

Its image `B_T` is a whole fiber of `E_B->Gamma`, of class `(1,0)`.
There can be at most one other horizontal prime. The coefficient of
`B` in `Z` is **not** assumed positive in the reducible-divisor cases.

Assume `Gamma` is a nonendpoint trisecant of fixed `C0`. Equivalently
it is a line in the degree-three ruling of the unique smooth quadric,
with parameter neither zero nor infinity. Its three curve contacts
are distinct in both their Gamma coordinates and their f coordinates.
For example, after a diagonal automorphism they are the three roots
of `t^3-s^3`, while the actual plane-pencil map on `C0` is `[s:t]`.
This elementary assertion is also recorded in
[the conductor-line position note](2026-10-10-session-genus-two-conductor-line-position.md).

**Conclusion:** no such mate exists. The proof below exhausts all
effective divisor decompositions of `D_T`, including nonreduced ones.

## 2. Where the singleton-support test is valid

Because `f|c#` has degree one, the image `c_T` is the actual section of
`T->P1_f` obtained by composing the inverse of `c#->P1_f` with `rho`.
The map `c#->c_T` is an isomorphism. Thus each Gamma-contact corresponds
to one specified point and one specified f-coordinate on `c_T`.

Let `G` be the hypothetical mate. At any Gamma point `p` on `C0`,
`G(p)=0`; therefore the pullback of `G` vanishes at every point of the
actual finite inverse conductor `D->Gamma` above `p`. Its zero-set on
`S` is exactly `c`. Since `c->C0` is an isomorphism, the support of
that inverse-conductor fiber must be a singleton, the point of `c`.

This test can be transferred from `S` to `D_T` at every Gamma point
which is not the image of a contracted horizontal prime: `T->S` is an
isomorphism there. It cannot be transferred blindly over the image
of a horizontal section. We use precisely this qualified test.

In particular the argument never infers that `c_T` avoids `B_T` from
`c#.B=0`. The curves can be separated on `M` by an ADE chain and meet
after that chain contracts on `T`. It also never assumes that the
finite inverse conductor, or `D_T`, is reduced.

Every horizontal prime supplies a Gamma-fiber component of `D_T`.
Conversely a Gamma-fiber component has `L`-degree zero and f-degree
one, and its strict transform is one of those horizontal primes.
Consequently an additional horizontal contraction cannot occur over
an unlisted Gamma point in any divisor case below.

## 3. Exhaustion of effective divisor decompositions

On `P1 x P1`, every effective prime has nonnegative bidegree.
Since `B_T` has degree `(1,0)` and `D_T` degree `(2,2)`, its
multiplicity is one or two. This includes every scheme multiplicity.

### Multiplicity two on B

If `D_T=2B_T+F` with `[F]=(0,2)`, then `F` is two f-fibers, possibly
equal. There are at least two C0 contacts away from `p_B` with
different f-coordinates. Equal f-fibers cannot contain both specified
points. Distinct f-fibers give two different points above every Gamma
point away from `p_B`, violating singleton support. There is no other
horizontal prime in this class budget.

### Multiplicity one, reducible residual

Write `D_T=B_T+R` with `[R]=(1,2)`. There is exactly one prime of
positive first degree in any reducible `R`; the remaining primes are
f-fibers. Its first degree is one, and its second degree is zero or
one. Hence the exhaustive possibilities are

    R=G_(1,1)+F_(0,1),
    R=B'_T+F_(0,2),

where the second expression includes equal or distinct f-fibers.
A reducible divisor of class `(1,1)` is already in the second case.

If `G_(1,1)` is irreducible, it maps isomorphically to Gamma. Together
with the fixed f-fiber it gives singleton support above at most the
one Gamma point where they intersect. There is no second horizontal
prime; the at least two contacts away from `p_B` therefore contradict
the support test.

In the second expression, if `B'_T=B_T` this is the preceding
multiplicity-two case. Otherwise there are two horizontal fibers.
For two distinct f-fibers the third C0 contact, away from both
horizontal-image points if they are contacts, has two inverse points.
If one or both horizontal-image points are not contacts there are
still more contacts away from them. In every case singleton support
fails at some contact away from both horizontal-image points.

For a double f-fiber the only potential divisor is

    D_T=B_T+B'_T+2F0,       p_B != p_B'.

At least one C0 contact is away from both horizontal-image points.
If either image point is not a C0 contact, there are at least two
contacts away from both with distinct f-coordinates, which cannot
both lie on `F0`. Thus the two horizontal-image points must be two
of the three C0 contacts, and the remaining contact lies on `F0`.
The f-coordinate of the contact over `p_B` differs from that last
contact's coordinate. At that point `D_T` is locally just the reduced
smooth component `B_T`; neither `B'_T` nor `F0` passes through it.
Its defining equation on the smooth `E_B` has nonzero differential.
The same is therefore true for the defining equation of `T` in the
smooth ambient blowup, and `T` is smooth at that point. The resolution
is an isomorphism there, so `c#` meets `B` there, contradicting
`c#.B=0`.

This last argument covers the important case in which the coefficient
of `B` in `Z` is zero and the other proper horizontal prime contributes
the required canonical correction. No premature assertion that
`p_B` is a C0 contact was used.

## 4. The integral residual has two transverse crossings

It remains that `R` is an irreducible divisor of class `(1,2)`.
Its projection to `P1_f` has degree one. There is no fixed f-fiber
component, so this projection is finite and `R` is the graph of a
morphism from `P1_f`; in particular it is a smooth rational curve.
Its other projection, to Gamma, has degree two and is separable.

There is no additional horizontal fiber in this divisor. Thus `B`
is the sole horizontal sigma-exceptional prime. All vertical primes
have canonical degree zero, while `K_M.B=1`, so

    a := coeff_B(Z) = K_M.Z = 1.

This positivity is established only now. The actual pullback divisor
of `G` has positive B coefficient, so `G` vanishes at its Gamma image
`p_B`. Set-theoretic equality `X intersect V(G)=C0` forces `p_B` to
be one of the three contacts.

The other two contacts are away from all horizontal contractions.
Their residual fibers are singletons, hence they are branch values
of the separable degree-two morphism `R->Gamma`. Riemann--Hurwitz
gives total ramification degree two for a degree-two map of P1.
These are already its two distinct branch values. It is consequently
unramified over `p_B`, and `R` intersects `B_T` at two distinct
transverse points.

There is no singular point of `T` on `B_T` outside these crossings:
there `D_T` is a reduced smooth divisor on the smooth `E_B`, so its
equation has nonzero differential. At a crossing choose coordinates
with `E_B=(r=0)` and actual branches `(u,r)`, `(v,r)`. Its equation is

    F=uv+r h(u,v,r).

The separately delegated
[relative formal Morse and specified-branch audit](2026-10-10-session-relative-morse-conductor-branches-independent-audit.md),
SHA-256 `a88aacc867f2cfae9e77ee8e54e88875b395f6446935dfc24f8ad540008e5153`,
proves directly that formal coordinates preserving `r` give

    F=xy+g(r),       (u,r)=(x,r),       (v,r)=(y,r).

If singular, `g` has finite order at least two. A harmless unit
rescaling gives `xy=r^(n+1)` and preserves these actual branch
ideals. The explicit resolution charts in that audit show that the
two specified branches meet the opposite endpoints of the exceptional
A_n chain, transversely. For A1 they meet its sole exceptional curve
at distinct points. This is consistent with the primary normal forms
in [Reid's Du Val notes, Table 1 and section 2.2](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf),
which this audit also read directly. The local argument is algebraic
over every algebraically closed characteristic-zero field, using
completed local rings; it does not require the field to be C.

Hence the sigma-fiber containing `B` consists of the (-3) curve `B`
and at most two A-chains attached at endpoints. No finite chain-length
bound, A1-only assumption, or D/E graph enumeration is being used.

## 5. Exact all-length contradiction

The contact of `c_T` over `p_B` must be at a singular point of `T`;
otherwise `c#` would meet `B` directly. The accepted embedded-smooth
uniformizer condition implies that `c#` meets exactly one exceptional
prime in that connected sigma-fiber, transversely once. Label the
chain over this contact by `1,...,n`, with B attached at node 1, and
let `k` be the contact node, `1<=k<=n`. The other crossing supplies a
chain of length `m>=0`, where zero means the crossing is smooth.
The section `c_T` has one f-coordinate over `p_B` and cannot contact
both crossing chains.

For completeness, the exact solution on the contact chain is

    z_i = a*(n+1-i)/(n+1) + i*(n+1-k)/(n+1),       i<=k,
    z_i = a*(n+1-i)/(n+1) + k*(n+1-i)/(n+1),       i>=k.

These formulas agree at k, vanish at the opposite virtual boundary
`i=n+1`, have virtual boundary `z_0=a`, and satisfy the second
difference equation `2z_i-z_(i-1)-z_(i+1)=1_(i=k)`.
Thus its neighboring coefficient is

    z_1 = n*a/(n+1) + (n+1-k)/(n+1).

The other chain has no source and contributes `m*a/(m+1)`. Since
`Z.B=-c#.B=0`, the exact B intersection equation yields

    a = ((n+1-k)/(n+1)) /
        (3-n/(n+1)-m/(m+1)).

Its denominator is exactly

    d = 1 + 1/(n+1) + 1/(m+1) > 1.

The numerator is positive and strictly less than one. Equivalently
the strict gap has the exact positive formula

    1-a = ((k+1)/(n+1)+1/(m+1))/d > 0.

Therefore `a<1` for all `n>=1`, `m>=0`, `1<=k<=n`, contradicting the
necessary value `a=1`. This proves the irreducible residual exclusion.

## 6. Exact computation, failures, and preserved boundaries

The geometric proof and positivity argument above are the proof.
The independently supplied symbolic script is only a countercheck of
the rational identities. An isolated replay of its initial bytes
failed after six passing identities because `source` is a protected
Macaulay2 global. A minimally repaired copy failed after nine passing
identities because `denominator` is also protected. Both full sources,
stdout, stderr, execution metadata, and hashes are retained in

[the continuation validation directory](../validation/2026-10-10-genus-two-nonendpoint-trisecant-continuation-audit/README.md).

Renaming just those two identifiers to `chainSource` and
`chainDenominator` gives the final source hash
`6a8b08f36f28c37865a2fd6708652e1d857fb2695c023687940186b2f91f4c7a`.
Its isolated Macaulay2 1.26.06 execution passed **12 exact rational
identities**, exit zero, observed tool chunk `e1c56e`, wall time
0.683747833 seconds (subprocess time 0.658300333 seconds). Its checked
expressions retain symbolic n, m and k; this is not a finite graph
search. The source is a repaired version of the same mathematical
checker, not a new distinct mathematical source. The historical
97-source/110-execution index is untouched.

All divisor types of `(2,2)` containing B, zero B correction when
another horizontal prime occurs, the unique satellite allowed in
the marked model, arbitrary A-chain lengths, and singular or
nonreduced finite inverse conductors are covered by this exclusion.
The relative local geometry forces the endpoint attachment in the
irreducible residual case; it is not imposed as a marked-graph
shortcut.

The endpoint triple-contact trisecants remain outside this proof:
their unique Gamma-contact supplies no two distinct residual branch
values. The lambda-zero stratum, higher carrier degrees, unrestricted
fixed-C0 STCI, and the universal projective-curve question remain
**OPEN**. No novelty or literature-resolution claim is made.
