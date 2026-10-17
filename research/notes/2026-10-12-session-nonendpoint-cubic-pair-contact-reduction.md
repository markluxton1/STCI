# Nonendpoint quintics: complete cubic contact and a modulus-free pair condition

Date: 2026-10-12. Author: `oct12_cubic_pair_support`.
Final assembly and integrity inspection: 2026-10-13.

Status: **NEW COMPLETE CUBIC-PAIR EXCLUSION; INDEPENDENT AUDIT
OUTSTANDING**. Supporting exact classifications, polynomial certificates,
and all failed execution versions are preserved and bound below. Work over an
algebraically closed field of characteristic zero, retaining `delta!=0`.

Use the [actual nonendpoint sections](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md)
and the independently audited [residual divisor and curve maps](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md).
An admissible projection has center avoiding the entire normalization
surface. A hypothetical mate requires full inverse support
`(nu^(-1)(C0))_red=c`; call this condition SUP.

## 1. Scope and parameters

Set `B=b-a`, `G=g-3b+2a`, `J=d-2g+2b-a`. The residual coefficient is
`A=a+d-b-g=G+J`. The partition considered here is `3+3`, on
`A=-3delta^2`, including a doubled cubic. Each source prime is the
smooth rational normal cubic

    t=-m*r-n,  T=r^2-m*r-n.

The accepted curve-map reduction says that under SUP it maps
isomorphically to a smooth target quadric curve of class `(2,1)`.
Both curve components have that class, including their cycle
multiplicities. The two roots of the actual polynomial T are retained
with multiplicity. The remaining point of the source cubic on c is
the intrinsic A4 point, `r=infinity`, whose target parameter is `z=1`.

The actual cubic coordinate polynomials are obtained by substituting
`t=-m*r-n` in

    U3=-r*t, U4=t^2-r^3-r*t,
    X0=U4+a*T,
    X1=X0-delta*U3+B*T,
    X2=X0-3delta*U3+3delta^2*r^2-delta^3*r+(3B+G)*T,
    X3=X0-4delta*U3+6delta^2*r^2-4delta^3*r+delta^4
          +(4B+2G+J)*T.

All four leading coefficients are -1, so the affine coordinate r
extends to the missing source point and all four target coordinates
are nonzero there. Their r^2-coefficient differences are

    [r^2](X1-X0)=B-delta*m,
    [r^2](X2-X0)=3(B-delta*m)+3delta^2+G.

## 2. The A4 contact is exactly one in every surviving cubic-pair case

On the target chart X0!=0, take Segre coordinates
`zeta=X1/X0`, `eta=X2/X0`. The target C0 is the smooth divisor
`eta-zeta^3=0`. Along the image cubic, use the actual smooth parameter
`epsilon=1/r` at its point above the A4 point. Expanding the displayed
coordinate polynomials gives

    eta-zeta^3=-(3delta^2+G)*epsilon+O(epsilon^2)
               =J*epsilon+O(epsilon^2).

Consequently its contact multiplicity with C0 is exactly one if J!=0.
This conclusion uses the complete smooth target equation at the point,
not a bound on later jets from first-normal data.

The complementary J=0 case on A=-3delta^2 has G=-3delta^2. These are
precisely the entire-line rank-one conditions

    R2=G+3delta^2=0,
    R3=2G+J+6delta^2=0.

The independently audited entire-line all-power obstruction excludes
every mate there; see the [separate pole/line proof audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md).
Thus only J!=0 needs further analysis in this note.

### 2a. The complete affine heptic and its exact extra-factor removal

The Segre factorization on each smooth target cubic can be normalized
in the following actual polynomials. Put `c0=g-a` and

    kappa=a-g+3delta*m-3delta^2,
    q=-(3delta*n+delta^3+c0*m)/kappa,
    w=-c0*n/kappa,
    Q0=-r^2+q*r+w,
    D=(delta^2/kappa)*(3*(m-delta)*r+delta^2+3n),
    Q1=Q0+D,
    sigma=m^2+m+a-q,
    L0=r-sigma, L1=L0+kappa.

Then the actual four coordinate sections are

    (X0,X1,X2,X3)=(L0*Q0,L0*Q1,L1*Q0,L1*Q1).

Here L0,L1 have degree one and Q0,Q1 have degree two. The first
Segre projection of a smooth `(2,1)` curve is an isomorphism to P1.
Consequently its local parameter at r=infinity is unramified, so
`kappa!=0`: it is minus the r^2 coefficient of X2-X0, which gives that
projection's first derivative in epsilon. This justifies every
division in the displayed formulas geometrically on the full locus
under consideration, rather than imposing a generic minor condition.

The complete contact section of binary degree seven is

    K=L1*Q0^3-L0*Q1^3
      =kappa*Q0^3-L0*D*(3Q0^2+3Q0*D+D^2).

It is not an ambient cubic numerator of degree nine. The two ambient
cubic restrictions factor exactly as

    X0^2*X2-X1^3=L0^2*K,
    X2^3-X1*X3^2=L1^2*K.

Thus their extra linear ruling factors are explicitly removed; no
common zero is lost because L1-L0=kappa!=0. This retains every finite
point with X0=0, as well as the other Segre chart. In the parent's
alternative naming, the degree-one polynomials are Q0,Q1 and the
degree-two polynomials L0,L1, and the same heptic is
`L0^3*Q1-L1^3*Q0`.

The actual residual-factor r^2 identity is
`kappa*(B-delta*m)=3delta^2*(m-delta)`. Hence the leading coefficient
of D is B-delta*m, and the leading coefficient of K is

    -(kappa+3B-3delta*m)=-J.

For J!=0, K has affine degree exactly six, whose binary degree-seven
homogenization has precisely one zero at infinity. Moreover the actual
polynomial T divides both ambient cubic restrictions, since their
universal expressions vanish identically on T=0. The coprimality of
L0,L1 then proves `T|K`, including any repeated root of T. In particular
`K=T*H4` with H4 of degree four and leading coefficient -J. All roots
of this complete contact section must be among the roots of T under
SUP. This proves the finite-profile bridge used below without any
tangent-only estimate.

There is also an exact intrinsic length statement. On the affine source
chart, restricting the ideal of c gives the degree-two polynomial T.
At infinity use the actual Z0=v=t^2-r^3 frame. The section cutting
c plus ell is `h=T/v`; on this cubic it is `-epsilon+O(epsilon^2)`.
It belongs to the ideal of c and has order one. As the point lies on c,
the restricted ideal therefore has length exactly one there. In total
the intrinsic restricted ideal of c has length three, while the
complete smooth target intersection has length seven. The excess
is exactly four on each cubic, including any repeated root of T.
The proof uses the full contact section to control this excess.

## 3. A finite contact classification, with no affine endpoint deletion

A target `(2,1)` curve has biform equation

    P2(U,V)*W0+Q2(U,V)*W1=0,

where `(U:V)` is the first Segre coordinate and `(W0:W1)` the second.
On C0 these coordinates are `(1:z^3)` and `(1:z)`. Thus its actual
degree-seven binary contact section has affine polynomial

    H(z)=P2(1,z^3)+z*Q2(1,z^3),

whose only possible exponents are `0,1,3,4,6,7`. Its z^2 and z^5
coefficients vanish. Smooth irreducibility requires that P2 and Q2 have
no common homogeneous zero; otherwise the biform has a ruling factor.

Under SUP and J!=0, this contact divisor has multiplicity one at z=1.
The other six contacts are supported at the two roots of T, or at their
single support when T has a repeated root. Put `u=r_alpha/delta` and
`v=r_beta/delta`. Then their homogeneous target linear forms are

    u*z1-(u-1)*z0,  v*z1-(v-1)*z0.

These formulas retain u=0 or v=0 (target infinity), and u=1 or v=1
(target zero). Neither finite source root maps to z=1. For distinct
roots, the contact multiplicities are, up to exchanging the roots,

    (N,P)=(1,5),(2,4),(3,3).

The contact polynomial is therefore the binary form

    (z1-z0)*(u*z1-(u-1)*z0)^N*(v*z1-(v-1)*z0)^P.

Its two missing coefficients give finite polynomial systems in u,v.
Repeated T gives the same formula with the coincident finite linear
form raised to the sixth power; it must be tested separately, rather
than silently removed by division by u-v. The complete exact
classification and smoothness filter are recorded in the
[separate sparse-heptic companion](2026-10-12-session-sparse-heptic-cubic-pair-classification.md).

## 4. Matching both source factors eliminates the modulus from one equation

For each quadratic T write

    T_i=r^2-delta*s_i*r+delta^2*p_i,
    s_i=u_i+v_i, p_i=u_i*v_i.

The source cubic equation is then
`t+delta*s_i*r-delta^2*p_i=0`. Let `x=B/delta^2`. Actual residual
factorization, with its fixed leading coefficient, is exactly

    F=-3delta^2*(t+delta*s1*r-delta^2*p1)
                 *(t+delta*s2*r-delta^2*p2).

Coefficient comparison with the saved actual F, without division by
either factor or by their difference, gives

    a/delta^2=-3*p1*p2,
    G=delta^2*(3*(s1+s2-1)-6*x)+3*delta,
    s1*s2=-x^2+x*(s1+s2)+(x-1)/delta,
    1/delta=x-s1*s2+1/3-p1-p2+3*p1*p2,
    1/delta=x+9*p1*p2-3*s1*p2-3*s2*p1.

In particular every admissible cubic pair must satisfy the modulus-free
condition

    s1*s2-3*s1*p2-3*s2*p1+p1+p2+6*p1*p2-1/3=0.       (PAIR)

The comparison is valid for equal factors as well as distinct factors.
It is a necessary condition; no sufficiency or center-avoidance claim
is made. Section 6 shows that (PAIR) fails on every possible contact
pair; additional coefficient equations therefore need not be solved.

## 5. The finite list of contact quadratics

The complete missing-coefficient classification, after removing exactly
the target biforms whose two binary quadratics have a common homogeneous
factor, gives
these possible pairs u,v. The ordering in the first two rows remembers
which root has the smaller contact multiplicity.

    type 15:  u=11*v-5,
              21*v^2-21*v+5=0;
    type 24:  u=42*v^3-63*v^2+42*v-10,
              63*v^4-126*v^3+111*v^2-48*v+8=0;
    type 33:  u=1-v,
              7*v^4-14*v^3+12*v^2-5*v+1=0.

The first two rows give respectively two and four quadratics T. The
last row gives two quadratics T, because exchanging u and v does not
change it. Every removed endpoint case has a ruling factor in its
target biform. The single-root sixth-power case gives only u=0 or u=1;
both corresponding biforms are reducible, so no repeated T root is
possible. This does not remove repeated *cubic factors* of D: each
individual cubic still has a distinct-root T, and the pair may coincide.

The more convenient equations for `s=u+v`, `p=u*v`, `h=s-1` are

    type 15:  7*h^2-12=0,
              p=s/2-5/42;
    type 24:  63*h^4-30*h^2-1=0,
              p=5/12+h/2-h^2/4;
    type 33:  s=1,
              7*p^2-5*p+1=0.

The identities are exact. For example, in type 24 put `w=v^2-v`.
The displayed quartic in v is `63*w^2+48*w+8=0` and
`h=(2v-1)*(21w+11)`. Reduction by the w-equation gives
`h^2=2w+1` and the stated p expression. The three field equations
are necessary for every survivor; sufficiency is unnecessary below.

## 6. No two of the eight possible contact quadratics satisfy (PAIR)

Call the left side of (PAIR) E. There are only six unordered pairings
of the three types. All rational numbers below are nonzero in the
stated characteristic-zero field.

* **15 with 15.** Substitution gives
  `E=2/147-h1*h2/2`. Since `h1^2=h2^2=12/7`, their product is
  `12/7` or `-12/7`, and E is respectively `-124/147` or `128/147`.
* **15 with 33.** If q is the type-33 p-coordinate, substitution gives
  `E=(2/7)*(q-1/3)`. The type-33 equation at q=1/3 is 1/9.
* **24 with 33.** Put e=h^2 for type 24. Then
  `E=(3e-1)*(1-3q)/6`. The type-24 equation in e,
  `63e^2-30e-1=0`, is -4 at e=1/3; the type-33 equation is 1/9
  at q=1/3. Thus neither factor can vanish.
* **33 with 33.** Direct substitution gives
  `E=(2/3)*(1-3p1)*(1-3p2)`, and again neither p-coordinate is 1/3.
* **15 with 24.** Write h1 for type 15 and h for type 24. Then
  `42E=1-3h^2-21h1*h`. If E vanished, squaring with
  `h1^2=12/7` would give `9e^2-762e+1=0`, where e=h^2.
  Together with `63e^2-30e-1=0`, this forces e=1/663. The latter
  quadratic has value `-459396/439569` there, a contradiction.
* **24 with 24.** Set ei=hi^2. Then
  `24E=(1-3e1)*(1-3e2)-12h1*h2` and each ei satisfies
  `63e^2-30e-1=0`. If e1 and e2 are the distinct roots, their sum
  is 10/21 and product is -1/63. The first product in 24E is then
  -4/7. Equality to `12h1*h2` would imply `16/49=-16/7`, impossible.
  If e1=e2=e, then `h1*h2=e` or `-e`. Equality forces respectively
  `9e^2-18e+1=0` or `(3e+1)^2=0`. The second alternative gives
  e=-1/3, where the type-24 equation is 16. The first, combined
  with that equation, gives e=1/12, where its value is -49/16.

The cases include the diagonal pair of two identical cubic factors,
because the displayed identities never divide by a difference of
factors or field roots. Thus (PAIR) fails for every possible pair.

## 7. Result and exact scope

**THEOREM (new proof, independent audit outstanding).** No admissible
nonendpoint projection in the actual genus-one quintic A4 family whose
residual divisor has partition 3+3 satisfies full inverse support SUP.
This includes a doubled residual cubic. Consequently no such quintic
carrier can participate in a set-theoretic complete intersection of C0,
in any mate degree.

The proof uses full target intersection divisors, exact smooth-quadric
factorization, the homogeneous missing-coefficient conditions, and
actual source coefficient comparison. It imposes no first-normal
upper bound on intersection multiplicity. Center avoidance is used
only through the actual finite projection and the accepted isomorphism
of each source cubic to a smooth target cubic.

The complete affine heptic and its division by the actual T are in the
[cubic-contact companion](2026-10-12-session-nonendpoint-cubic-contact-symbolics.md).
The finite coefficient classification is in the separate sparse-heptic
companion linked above. The integral residual, conic-plus-quartic,
other quintic normalization lanes, higher carriers, and the unrestricted
STCI question remain outside this theorem.

## 8. Exact bindings, failures, and checker scope

The frozen supporting inputs are:

| Artifact | SHA-256 |
| --- | --- |
| Cubic-contact companion note | `0b85a793349a0a35c6b9f1b3ea0a677d90d2076d14f2f28257ab5b86c1b1fb4c` |
| [Cubic-contact exact source](../computations/verify_session_nonendpoint_cubic_contact_2026_10_12.m2) | `c26395b318525b6b531ebc96f91bc9866fbbb186ae9982f79443c2fb7508bd58` |
| [Final cubic-contact execution record](../validation/2026-10-12-nonendpoint-cubic-contact/20261012T213343388888Z/execution-record.json) | `278bed883b148653b86a34adf1d5ab1f7d814914c3776322c7e8a186ca99eabe` |
| Sparse-heptic companion note | `58ceb45611e48755169b78fc9a3b8d666853c705f1d2281a8f6a80a489a96bc8` |
| [Sparse-heptic exact source](../computations/verify_session_sparse_heptic_cubic_pairs_2026_10_12.m2) | `1e18cdedcd5ed9a4181f6baf21ff5d959ed7e2a9dfcedaf522e546716809fdeb` |
| [Sparse-heptic execution record](../validation/2026-10-12-sparse-heptic-cubic-pair-classification/execution-record.json) | `30ce05de9892a50aa56331f35d9717c411de01b4f346c785c7c0e6c201a0958d` |
| [Sparse-heptic manifest](../validation/2026-10-12-sparse-heptic-cubic-pair-classification/manifest.json) | `f31b48dc7dcc8e36307e9fd5c3407675d80bb5ddc375c362987940c7c5b3c2fa` |

The cubic-contact checker is one algebra-support lineage. Its five
captured attempts consist of four failures followed by one pass:
protected `dd` (zero checks), a wrong coefficient-ring assertion failure
(six checks passed), protected `quotient` (seven passed), preexisting
`zeta` preventing construction of the final ring (eight passed), then
all ten supporting identities passing with empty stderr. This checker
verifies actual restrictions, exact heptic identities/division, and
coefficient matching; it does not exhaust contact profiles.

The sparse-heptic checker is a separate algebra-support lineage. Its
record preserves two setup/checker failures, four successful scratch
scripts, and the final successful checker. Scratch captures are explicit
replays, not independent lineages. The final source executes 30 assertion
invocations in ten substantive blocks, plus a terminal PASS summary:
three saturated ideal equalities, one single-root exclusion, and all six
pair identities with literal original-generator Bezout products equal
to one. Empty stderr and exit zero are recorded. The exact homogeneous
Sylvester resultant retains its roots at infinity.

The owner has read both companion proofs and sources, reconstructed
the six elementary contradictions, and verified current capture
bindings without rerunning the completed calculations. Independent
geometric proof audit remains outstanding; this statement is a new
owner proof, not a claim that agreement between workers is proof.
The [assembly manifest](../validation/2026-10-13-nonendpoint-cubic-pair-assembly/manifest.json)
binds this note, the accepted dependencies, both checker lineages, all
captured failures, and their raw outputs. Its separate integrity result
does not constitute mathematical acceptance.
