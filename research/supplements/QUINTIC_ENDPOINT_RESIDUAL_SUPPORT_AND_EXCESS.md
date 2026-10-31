# Quintic endpoint: residual support and local excess obstructions

The characteristic-zero intrinsic degree-five A4 endpoint family has three
parameter strata. The complete inverse-support proofs below exclude every
admissible projection with `a != 0` and with `a=0,b != 0`; the
[actual fourth-blowup all-power argument](QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md)
excludes `a=b=0`. Together they close this endpoint lane in every mate
degree. The nonendpoint projection has a separate modulus, and these
arguments do not exclude arbitrary quintic normalizations or the
unrestricted STCI problem.

The global proof uses the full target-septic
[higher-contact calculation](QUINTIC_ENDPOINT_TARGET_CONTACT.md) and the
[three-root residual quartic](QUINTIC_ENDPOINT_THREE_ROOT_QUARTIC.md). The
source-parameter intersection-length argument at the end is a distinct
geometric control; a first-normal contact count alone would not suffice.

<a id="1-endpoint-a-nonzero-full-support-exclusion"></a>
<a id="2-endpoint-a-nonzero-global-independent-audit"></a>
## Full inverse support when a is nonzero

Status: **PROVED HERE; COMPLETE INDEPENDENT GLOBAL AUDIT PASS** for the
stated intrinsic endpoint lane and `a != 0`. No unresolved parameter stratum
remains within that scope. This is not an exclusion of nonendpoint
projections, all quintic carriers, or unrestricted STCI presentations.

The target-variable proof of contact order is the full
[two-common-root calculation](QUINTIC_ENDPOINT_TARGET_CONTACT.md). The
[direct source-parameter excess proof](#6-quintic-endpoint-a-nonzero-local-excess-bound)
gives a second route through actual intersection lengths; the global
argument below does not require its geometric length identification.
The [original-variable residual quartic](QUINTIC_ENDPOINT_THREE_ROOT_QUARTIC.md)
and [shifted certificate](#5-endpoint-three-common-roots-shifted-replay)
retain their two exact computational implementations.

## 1. Exact statement and the mate implication

Work over an algebraically closed field of characteristic zero. The normal
degree-five anticanonical del Pezzo surface `S` and smooth lifted quartic `c`
are the actual pair in the accepted
[quintic structural frontier](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit),
with the exhaustive
[intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#1-dp5-a4-intrinsic-pair-classification)
and its
[explicit-model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#2-dp5-a4-explicit-model-independent-audit).
The unique line is `ell`; the only surface singularity is A4. Its actual
anticanonical sections satisfy `div(U0)=5ell`, `div(hsec)=c+ell`.
Consequently `S minus ell` is the complete open chart `A2(r,T)`, with
`c:T=0` there.

In the endpoint lane the actual four projection sections are

    X0=1+aT,
    X1=r+bT,
    X2=r^3+(g-r)T,
    X3=r^4+(d-r-2r^2)T+T^2.

Assume `a != 0` and that the line center avoids S. The claim is that some
actual point of S outside c maps into

    C0=[s^4:s^3t:st^3:t^4].

This suffices to exclude a mate of every positive degree. As independently
proved in the structural frontier, an integral quintic is regular at the
generic point of C0: twice C0 on its unique quadric would leave the
noneffective class `(3,-1)`. Thus c is the unique dominating curve over C0.
For a mate G, the actual normalized divisor is `5k c` with `deg(G)=4k`.
The zero set of its pullback is therefore c. Every point over C0 must vanish
under that pullback, giving the necessary full inverse-support condition

    (pi^(-1)(C0))_red=c.

This argument concerns actual support, including isolated inverse points.
It does not replace that condition by equality of the dominating curve only.

On ell the projection is `[0:0:U3:U4]`, an isomorphism onto the line
`X0=X1=0`. That target line meets C0 set-theoretically only at
`[0:0:0:1]`; its preimage on ell is the A4 point, which lies on c. Thus
the open-chart argument below loses no possible extra endpoint fiber by
ignoring ell. More importantly, the contradiction constructs its extra
point in the actual A2 chart itself.

## 2. The projective infinity fiber is settled before division

Put

    Cb=a^2 g-ab-b^3,
    Db=a^3 d-b^4-2ab^2-a^2 b-a^2.

The actual affine point `(r,T)=(b/a,-1/a)` lies off c. Its projection has

    X0=X1=0, X2=-Cb/a^3, X3=-Db/a^4.

If Cb=Db=0 this is a base point, contrary to center avoidance. If Cb=0
and Db is nonzero, it maps to the actual endpoint `[0:0:0:1]` of C0.
Hence full inverse support forces `Cb != 0`. This proves the discarded
chart boundary impossible; it is not an unexamined saturation condition.

## 3. Every root of the exact septic gives a residual fiber

For a finite target point `[1:z:z^3:z^4]`, its second-coordinate equation
gives `r=z+AT`, where

    A=az-b,
    U=2az^3-3bz^2-z+g,
    V=3az^4-4bz^3-2z^2-z+d,
    H=az^3+z-g-1,
    J=AV-(Az-1)U.

Substitution in the last two target-coordinate equations gives exactly

    X2-z^3 X0=T P,
    X3-z^4 X0=T R,
    P=U+A(3zA-1)T+A^3 T^2,
    R=V+(6z^2 A^2-4zA-A+1)T+(4zA^3-2A^2)T^2+A^4 T^3.

The exact linear elimination identity is

    A R-(A^2 T+Az-1)P=J+A^2 H T.

The fixed-degree Sylvester identity is `Res_T(P,R)=A^7 E`, as checked
in the retained [subresultant source](../computations/verify_session_quintic_endpoint_subresultant_2026_10_11.m2).
The explicit linear identity, rather than division by this resultant,
settles the exceptional fibers below.

Define

    E=J^2-(3zA-1)HJ+AUH^2.

Direct expansion, independently checked, gives degree seven in z and
leading coefficient `a Cb`. Thus its degree stays exactly seven for every
parameter value now under consideration, and no root at infinity can
absorb a missing finite degree.

At `A=0`, the exact specialization is `E=az^3+z-g=-Cb/a^2`, so no
root of E is lost by division by A. Also the cleared identity

    a^2 P(-1/a)=Cb

proves that no residual P,R solution has `X0=0` on the present locus.

If `E(rho)=0` with `H(rho) != 0`, put
`T=-J/(A^2 H)` and `r=rho+AT`. The identity

    A H^2 P-E
      =(A^2 H T+J)(A^2 H T-J+(3zA-1)H)

gives `P=0`; the linear identity gives `R=0`. Since `X0 != 0`, this is
a defined point mapping to the specified finite point of C0. Under full
inverse support it must have `T=0`, which forces `U(rho)=V(rho)=0`.

If `H(rho)=0`, then `E(rho)=0` forces `J(rho)=0`. Every root of the
genuine quadratic P is then a root of R. None can have `X0=0`. Under full
inverse support all these roots must be zero, so `U=0` and `3rho A=1`.
At a common root the identity `H=3rho^2 A-1-U` now gives `rho=1`,
`A=1/3`. Then `V=0` as well, giving the complete exceptional family

    b=a-1/3, g=a, d=a+5/3.

The exact expansion of E at z=1 has first nonzero coefficient `1/9` in
degree two, independently of a. Thus this exceptional compatible root has
order exactly two. Every other H-zero septic fiber already gives an
off-curve point.

We have proved the global necessary support assertion:

    Supp(E) is contained in the common geometric roots of U,V.

The cubic U has leading coefficient `2a != 0`, so that support has at most
three distinct points.

## 4. Full higher coefficients give order at most four

At a common root rho put `w=a rho-b`, `q=w rho`. The equations U=V=0
give the exhaustive substitution

    b=a rho-w,
    g=a rho^3-3w rho^2+rho,
    d=a rho^4-4w rho^3+2rho^2+rho.

The exact identity

    Cb=w*(a(1-3q)+w^2)

excludes `w=0`; this is the `k=b-a rho=0` stratum in the opposite
sign convention. If `c_j` is the coefficient of `(z-rho)^j` in E,

    H(rho)=3w rho^2-1,
    c1=-H(rho)*(6q^2-6q+1+3wq).

The H-zero case was settled above with compatible order exactly two.
In the remaining case, order at least two forces

    D=6q^2-6q+1,
    w=-D/(3q), rho=q/w.

Here `q != 0` and `D != 0`: otherwise the defining equation would be
one or would force w=0. Furthermore

    H(rho)=-(3q-1)(3q^2+3q-1)/D.

Hence `3q-1` and `B=3q^2+3q-1` are nonzero on this branch. In these
parameters c2 is affine linear in a with nonzero slope

    -3q B(3q-1)^2/D^2.

Order at least three therefore forces exactly

    a=-D^2*(54q^4-72q^3+15q^2-3q+1)/(27q^3(3q-1)^2).

The final coefficients c3,c4 and their explicit numerator polynomials are
displayed in the
[independent target-contact audit](QUINTIC_ENDPOINT_TARGET_CONTACT.md#4-exact-coprimality-checks-and-maximum-contact-order).
I inspected that proof and its source. It derives the coefficients from E
itself and proves the exact polynomial gcd statements

    gcd(num(c3),num(c4)) is a nonzero rational multiple of D,
    gcd(num(c3),num(Delta)) is a nonzero rational multiple of D,

where `Delta=Res_z(U/(z-rho),V/(z-rho))` at the same forced parameters.
All rational denominators are products of nonzero rational constants,
powers of q and powers of `3q-1`; none vanishes on the branch. The quotient
polynomials have their actual degrees two and three since `a != 0`.
These are exact coprimality assertions valid after every allowed algebraic
specialization, not generic-rank checks or numerical samples.

Since D is nonzero, c3 and c4 cannot both vanish. Thus every compatible
root has order at most four. If its order is four, then c3=0 forces
`Delta != 0`, so there can be no other common U,V root. The assertion also
includes an additional common multiplicity at rho: that would make the
two quotients share rho and force their resultant to vanish.

This is the corrected bound. The preliminary bound of three was false and
is not used. No order estimate is inferred from first-normal degree.

## 5. Exhaustion of the number of common roots

There are four possible counts of distinct common roots of U,V:

* Zero: a nonconstant degree-seven E cannot have support in the empty set.
* One: its order is at most four, less than seven.
* Two: neither can have order four, because that would prohibit the second.
  Their orders are therefore at most three each, totaling at most six.
* Three: all cubic roots are distinct, so U divides V. Long division forces
  `a=3b^2/2`, `g=1/(9b)-2/3`, `d=1/(54b^2)-1/(9b)`, with b nonzero.

In the final case `Cb=-3b^3(2b+3)/4`, so `b != -3/2`. Write E=US.
The residual S has degree exactly four throughout this locus. The
[original-variable audit](QUINTIC_ENDPOINT_THREE_ROOT_QUARTIC.md#3-two-incompatible-necessary-resultants)
and its independent
[shifted-variable certificate](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md#5-endpoint-three-common-roots-shifted-replay)
give exact incompatible resultants: if every root of S were a root of U,
the two polynomials would share a root, while S would have a repeated root
because a quartic is supported at at most three points. Their resultant
and the derivative resultant of S would both vanish, but their retained
parameter factors are coprime in QQ[b]. Their leading coefficients stay
nonzero on `b != 0,-3/2`. Thus there is no missing degree-drop or repeated-
root exception. The corrected positive sign in `a=3b^2/2` is essential;
the earlier exploratory negative sign is explicitly rejected.

Every possible common-root count contradicts the necessary support
assertion. Consequently every admissible displayed endpoint projection with
`a != 0` has an actual point outside c mapping into C0. Its mate is excluded
in every degree.

## 6. Independent evidence and bounded acceptance

My separately written
[geometry checker](../validation/2026-10-11-endpoint-support-global-audit/verify_geometry.m2)
has SHA-256
`5e786b80c301f98a0aa34a360190d4596fbe52d9ae8e9e0df0e9050e1adc4de2`. The final source uses a flat polynomial ring and cleared polynomial evaluations throughout.

The separately retained [target-jet checker](../computations/verify_session_endpoint_a_nonzero_target_jets_2026_10_11.m2)
checks the original higher-jet and projective-boundary identities. Its
conditions overlap the full independent reconstruction below; no new run is
claimed by this consolidation.

The independent target-contact source has SHA-256 `c08e6512379953227600fb176164148d52acd3ce3fe7e9ec00a51b5526d5c5db` and verifies fourteen exact conditions. The degree assertions use the specified univariate coordinate, not total degree in all coefficient variables.

The global audit passes. Its acceptance covers only `a != 0` in the intrinsic
endpoint genus-one A4 lane. The two `a=0` subfamilies require their separate
support and jet arguments; the nonendpoint lane retains its extra modulus.
Other quintic normalizations, higher carriers and the universal STCI problem
remain open. This audit edits no prior frozen proof, canonical record or
existing evidence seal.


---

<a id="4-quintic-endpoint-a0-support-exclusion"></a>
<a id="3-quintic-endpoint-a0-polynomial-support-independent-audit"></a>
## Full inverse support when a vanishes and b is nonzero

Status: **DIRECT COMPLETE PROOF AUDIT PASS for the displayed affine family**.
The applicability to the entire intrinsic endpoint lane uses the separately
recorded A4 pair and projection-center classification. This note does not
exclude a!=0, a=b=0, nonendpoint projections, other quintic normalizations
or the unrestricted STCI problem. No frozen source, canonical record or
integrity seal is edited.

The [explicit model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#2-dp5-a4-explicit-model-independent-audit)
and [intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md#1-dp5-a4-intrinsic-pair-classification)
supply the normalization chart and the limited endpoint scope. Work over
an algebraically closed characteristic-zero field.

## 1. Actual residual equations and their degree-six elimination

On the actual open S minus ell=A2(r,T), the projection with a=0 is

    X0=1, X1=r+bT,
    X2=r^3+(g-r)T,
    X3=r^4+(d-2r^2-r)T+T^2,       b!=0.

The affine C0 ideal is generated by
`A=X2-X1^3` and `q=X3-X1 X2`: q together with A also generates
`X3-X1^4`. Thus the complete inverse-image test on this chart is exactly

    A=T(P-3rb^2 T-b^3 T^2), q=T(N+MT),
    P=-3br^2-r+g,
    N=-br^3-r^2-(1+g)r+d,
    M=br+1-bg.

No projective denominator is present because X0=1. An off-c point is an
actual solution of the two residual equations with T!=0, not a formal
infinitesimal point or a projection base point.

Set `R=P M^2+3rb^2 N M-b^3 N^2`. Direct leading-coefficient bookkeeping gives

    [r^6]R=-b^5,
    [r^5]R=-2b^4-3b^4=-5b^4,
    [r^4]R=-b^3(1+2b+2bg)-3b^3(2-bg)-3b^3
            =-b^3(10+2b-bg).

The three contributions to the last line come respectively from -b^3 N^2,
3rb^2 N M and P M^2. In particular R has exact degree six for every b!=0.
These equalities are direct coefficient identities, not observations at
sample parameters.

## 2. The denominator-zero fiber is retained, not saturated away

If a root r0 of R has M(r0)=0, its defining identity gives N(r0)=0.
The second residual equation then holds for every T. The first is a
quadratic in T with nonzero leading coefficient -b^3.

If P(r0)!=0, both quadratic roots are nonzero, giving an off-c point.
If P(r0)=0, the quadratic is `T(-3r0 b^2-b^3 T)`. Its other root is
nonzero because r0 cannot be zero: M(0)=0 would give g=1/b, hence
P(0)=g!=0. This also gives an off-c point.

Consequently, if no off-c point existed, every root of R would have M!=0.
At such a root the actual value `T=-N/M` solves both residual equations,
since substitution into the first gives R/M^2. Absence of off-c points
would force T=0, and therefore N=P=0. Hence every geometric root of R
would have to lie in the common zero set of P,N, with M nonzero there.

P has exact degree two, so that common zero set is empty, has one point,
or has two distinct points. The empty case is impossible because R is a
nonconstant polynomial over an algebraically closed field. The other two
cases are excluded below.

## 3. One common geometric root gives incompatible coefficients

Suppose the common zero set consists of rho, including the case where P
has a repeated root. The degree and leading coefficient force

    R=-b^5(r-rho)^6.

Comparing its r^5 coefficient gives `w=b rho=-5/6`. From P(rho)=0,

    bg=w+3w^2=5/4,       M(rho)=1-3w^2=-13/12.

Comparing r^4 coefficients gives

    10+2b-bg=15w^2=125/12,       b=5/6.

Now differentiate the actual defining R at a common P=N=0 root:

    R'=P'M^2+3rb^2 N'M.

At rho, `P'=-1-6w` and `N'=-1-(3w+6w^2)/b`. Substituting
`M=1-3w^2` gives the exact identity

    R'(rho)=-M(rho)[6w^2+(6+3b)w+1].

The alleged sixth power has derivative zero there. With w=-5/6 and M!=0,
this equation instead gives `1/6-5b/2=0`, or b=1/15. This contradicts
b=5/6. It treats all one-geometric-root gcd patterns without an assumed
simple ramification or a bound on the root multiplicity.

## 4. Two common roots reduce to one impossible quartic root

If P,N have two common distinct roots, then P divides N. Its leading
terms determine the quotient, and comparing the remaining coefficients
gives exactly

    N=(r/3+2/(9b))P,
    g=1/(6b)-3/4,       d=2g/(9b).

Put `w=br`, `gamma=bg`, `p=gamma-w-3w^2=bP` and
`m=1-gamma+w=M`. Substitution in R gives the actual factorization

    R=P S,
    S=m^2+(w^2+2w/3)m-p(w/3+2/9)^2.

Its leading coefficients are

    [w^4]S=1/3,
    [w^3]S=1+5/9=14/9.

Thus S is a nonconstant quartic for all these parameters. The necessary
root condition from Section 2 makes each root of S a root of p, with m
nonzero. At a root of p one has gamma=w+3w^2, and the displayed S reduces
exactly to

    S=(1-3w^2)(1-2w^2+2w/3).

The first factor is m, which is nonzero by the denominator-fiber analysis.
Every root of S must therefore also be a root of
`J=1-2w^2+2w/3`. The two distinct roots of p have sum -1/3, whereas the
two roots of J have sum 1/3. These quadratics cannot share both roots.
Their common geometric zero set consequently has at most one point.

Since S has degree four, it must have exactly one root w0 and therefore
`S=(1/3)(w-w0)^4`. Its w^3 coefficient gives w0=-7/6. But direct
substitution gives `J(-7/6)=-5/2`, which is nonzero. This contradicts the
required root condition and exhausts the two-common-root case.

## 5. Complete conclusion and bounded attribution

All possible common-zero patterns of P,N are contradicted. Hence the
displayed affine map has an actual point T!=0 above C0 for every b!=0
and all g,d. For an admissible finite normalization projection that point
violates the full inverse-support condition required by a mate in any
degree. The proof does not require a reduced conductor, a flat conductor
cover, a bounded descending exponent, or any generic parameter condition
beyond b!=0.

This direct audit independently reconstructs the denominator-zero fiber,
the three leading elimination coefficients, the one-root derivative and
coefficient incompatibility, the exact P|N quotient, and the S/J root
contradiction. No new script, symbolic run or numerical count is claimed;
the coefficient calculations are included explicitly as the proof.

The [a=b=0 jet proof](QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md) and
[complete a!=0 inverse-support proof](#full-inverse-support-when-a-is-nonzero)
close the complementary endpoint strata. The nonendpoint projection-center
parameter remains a separate problem. This support proof uses the intrinsic
pair classification and does not establish an unrestricted quintic-carrier theorem.


---

## 5. endpoint three common roots shifted replay

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

The final three-common-root construction uses `QQ[b][x]`, retaining the full x-coefficient polynomials. In contrast, `coefficient(x^k,f)` in flat `QQ[b,x]` discards terms with positive powers of b. The final nine conditions include the exact nonzero resultant constants.

The separate
[residual-quartic independent audit](QUINTIC_ENDPOINT_THREE_ROOT_QUARTIC.md#3-two-incompatible-necessary-resultants)
works directly in the original variable `z` and obtains the same parameter
factors, with its own captured eight-assertion source. The two sources are
independent implementations of this algebraic certificate; execution
snapshots of either source are copies, not additional implementations.


---

## 6. quintic endpoint a nonzero local excess bound

# Endpoint a!=0: full-jet excess bound and exclusion with at most two contacts

Date: 2026-10-11. Author: `oct11_endpoint_a_nonzero_support/a_nonzero_local_excess`.
Status: **DIRECT LOCAL-INTERSECTION PROOF WITH EXACT ALGEBRAIC CERTIFICATES;
pending independent audit**. This note changes no canonical or frozen record.
It proves the displayed endpoint a!=0 full-support condition impossible when
U and W have at most two distinct common roots. It does not by itself treat
the three-common-root stratum or nonendpoint projection centers.

## 1. Scope and retained transverse equations

Use the actual endpoint projection and center-avoidance hypotheses in the
[quadric-factor reduction](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#2-quintic-endpoint-factor-independent-audit)
and its [independent audit](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#2-quintic-endpoint-factor-independent-audit).
On the smooth affine normalization chart the coordinates are

    X0=1+aT, X1=r+bT,
    X2=r^3+(g-r)T, X3=r^4+(d-2r^2-r)T+T^2.

Work over an algebraically closed field of characteristic zero, with a!=0,
and assume for contradiction full reduced inverse support of C0 is c:T=0.
The two exact residual equations are

    K=ar^4-br^3-r^2-(1+g)r+d
      +T*(1+ad-bg-2ar^2-ar+br)+aT^2,
    E=U+T*P1+T^2*P2,
    U=g-r-3br^2+2ar^3,
    W=K(r,0)=ar^4-br^3-r^2-(1+g)r+d,
    P1=a^2r^3+2a(g-r)-3b^2r,
    P2=a^2(g-r)-b^3.

Indeed q pulls back to TK and X0^2 X2-X1^3 pulls back to TE. These
identities retain every transverse term. The factor audit proves that
the total excess intersection length length(O_D/(E)) is seven, all
supported at finite common roots of U and W, where D=V(K) is integral.
The present proof bounds these actual excess lengths, not their first jets.

## 2. Endpoint avoidance and the resultant's harmless chart factor

Put Cb=a^2g-ab-b^3. If Cb=0, the actual affine point

    r=b/a, T=-1/a

has X0=X1=X2=0. If also X3=0 it is a projection base point, contradicting
center avoidance. Otherwise it maps to the endpoint [0:0:0:1] of C0
and lies off c, contradicting full inverse support. Thus Cb!=0.

The exact resultant in the actual transverse variable factors as

    Res_T(K,E)=(ar-b)^2 H(r),
    deg H=7, [r^7]H=-a^4.

The square factor arises from the point with X0=X1=0 in the cubic-plus-
quadric target equations; those two equations alone also vanish along
the target line X0=X1=0. The factor is not silently interpreted as C0.

At a common root rho of U and W, set w=a rho-b. Substitution of U(rho)=0
gives the exact identity

    Cb=w*(a+w^2-3aw rho).

Consequently w!=0 at every possible excess support point. The factor
(ar-b)^2 is therefore a unit near rho and can be removed there.

The order of H at rho equals the total local intersection length of K,E
in the r-fiber over rho. To justify this even when D is singular, K/a is
monic quadratic in T. Over the DVR k[[r-rho]] the algebra defined by K/a
is free of rank two, and the resultant is, up to a nonzero scalar, the
determinant of multiplication by E. When the resultant is not identically
zero, the determinant's valuation is the length of its cokernel. Splitting
the finite fiber gives the sum of the local intersection lengths. H has
nonzero leading coefficient, so this finiteness condition holds.

Under full support, any common point of K,E in this fiber with T!=0 and
X0!=0 would map to affine C0 and is excluded. A point with X0=0 must have
X1=0 to satisfy the pulled cubic, hence r=b/a; this does not occur at rho
because w!=0. Thus the only supported common point in the rho-fiber is
(rho,0), and ord_rho H is exactly the actual excess length at that point.
This includes a double K-root at T=0 and singular D.

## 3. The second transverse root excludes one derivative factor

Write r=rho+s. The equations U(rho)=W(rho)=0 determine

    g=rho+3b rho^2-2a rho^3,
    d=rho+2rho^2+4b rho^3-3a rho^4.

At s=0 the full equations become

    K=T*(M+aT), E=T*(P1+P2T),
    M=1-3rho^2w^2,
    P1=-3rho w^2, P2=-w^2*(3a rho-w).

Define

    S1=1+3w rho^2*(3a rho-w),
    S2=1-6w rho+3w^2rho*(2rho+1).

Exact expansion of H gives

    [s]H(rho+s)=-w S1 S2,
    aP1-MP2=-w^3 S1.

If S1=0 then rho!=0, since S1=1 at rho=0. Also M!=0: if M=0,
the second identity gives aP1=0, impossible with a,w,rho all nonzero.
The second K-root T=-M/a is therefore nonzero and is also an E-root.
At this point X0=1-M=3rho^2w^2!=0, so it is an actual off-c point
mapping to affine C0. Full support consequently forces S1!=0.

Thus an excess length at least two requires S2=0. S2 is the exact
Jacobian determinant of K,E at (rho,0), but only serves here to
parametrize the higher-jet analysis that follows; no order bound is
inferred from this determinant alone.

## 4. All multiple-contact parameters and their higher coefficients

Assume S2=0 and put q=w rho. Necessarily q!=0. Solving S2 gives

    D=6q^2-6q+1,
    w=-D/(3q), rho=q/w.

D!=0 because w!=0. These formulas exhaust S2=0, including singular
residual-curve cases; they impose no smoothness assumption on D_K.

Let c_j=[s^j]H(rho+s). The exact coefficient c_2/S1 is

    ((243q^5-162q^4+27q^3)*a
      +1944q^8-6480q^7+8316q^6-5292q^5+1890q^4
      -468q^3+99q^2-15q+1)/(81q^4).

At q=1/3 this expression is -1/27 for every a. Hence that entire
exceptional parameter case has excess length exactly two. In particular
it is not lost by division by 3q-1.

For q!=1/3, excess length at least three forces the unique value

    a=-D^2 A4/(27q^3(3q-1)^2),
    A4=54q^4-72q^3+15q^2-3q+1.

At this value the exact next coefficient and the remaining unit factor are

    c_3=D^3 N6 N9/(2187q^7(3q-1)^4),
    S1=-N6/(3q-1)^2,
    N6=162q^6-216q^5+72q^4-27q^3-3q^2+6q-1,
    N9=8748q^9-20412q^8+18954q^7-8262q^6+1458q^5
       -252q^4+180q^3-66q^2+12q-1.

The retained denominator conditions q!=0,D!=0,q!=1/3 and S1!=0
are all explicit. The original a!=0 and Cb!=0 remain in force;
excluding further parameter values cannot weaken the bound below.

## 5. Exact certificates prove order at most four and uniqueness at order four

Let J be the resultant in s of the two quotient polynomials

    U(rho+s)/s, W(rho+s)/s.

After substituting the forced a from Section 4, compute c_3,c_4,J as
elements of QQ(q), retaining their actual numerators. The exact identities are

    gcd(num c_3,num c_4)=D^3,
    gcd(num c_3,num J)=D^3.

These are not numerical samples. The [fourteen-check M2 source](../computations/verify_session_quintic_endpoint_a_nonzero_local_excess_2026_10_11.m2)
derives both numerators directly from the retained full equations and
exports their rational coefficient lists. The independently generated
[Bezout certificates](../validation/2026-10-11-quintic-endpoint-a-nonzero-local-excess/bezout-certificates.json)
give, for each displayed pair, explicit polynomial multipliers over QQ
whose combination is D^3. A standard-library Fraction verifier multiplies
the exported polynomials and checks both identities exactly. Thus neither
pair can simultaneously vanish when D!=0.

If the excess length were at least five, then c_3=c_4=0, contradicting
the first certificate. Therefore every excess length is at most four.

If an excess length is four, then c_3=0. The second certificate forces
J!=0. Consequently the two quotient polynomials have no common root
over the algebraically closed field. Any other common U,W root would
give such a root; even an additional common multiplicity at rho would
do so at s=0. Thus an order-four excess forces rho to be the only common
root of U,W, with no additional common multiplicity.

## 6. Consequence for at most two distinct common roots

If there are no common roots, the necessary seven-excess condition fails.
If there is just one common root, its excess is at most four, again less
than seven. If there are two distinct common roots, neither can have
excess four, since that would force it to be the only common root.
Each then has excess at most three, for a total at most six. This is
also less than seven. Repeated roots and singular residual curves are
already covered by actual intersection lengths in Sections 2--5.

Hence full inverse support is impossible throughout the endpoint a!=0
family with at most two distinct common U,W roots. The three-distinct-
common-root family remains a separate obligation in this note.

## 7. Execution provenance and failure corrections

The exact local-excess source has SHA-256 `84d8ffa69ff8e74f971112cc3a8e18efe33832af8c6ed5ab0bd0a8b26c67fccd` and verifies the fourteen identities, including both Bézout checks.

Three failed source versions are preserved. The first two assertions
failed because unparenthesized multiline M2 assignments silently omitted
the following-line terms. An initial tentative quotient-ring diagnosis
was superseded by inspection of the actual parsed equations. Parentheses
repaired the source; the fraction-field presentation was retained and
every resulting rational identity is interpreted with the explicit
nonzero conditions above. The third version passed all fourteen checks
but failed while exporting coefficients because q had the wrong ring
binding. Rebinding to QQ[q] repaired only that export.

Earlier scratch resultant and parameter scripts are exploratory leads,
not additional accepted theorem certificates. The source's exact identities
and Bezout certificates support the algebraic calculations; the preceding
local determinant and support arguments supply the geometric quantifiers.
