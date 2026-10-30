# Cubic contact and family exclusions

Permanent complete mathematical dossier for the nonendpoint quintic geometry. The original calculations, exact hypotheses, conditional status, counterexamples, failure modes and unresolved cases are preserved below. Independent certificates are mathematical arguments; executable code remains separately located in the repository.

---

## 1. nonendpoint cubic pair contact reduction

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


---

## 2. nonendpoint cubic contact symbolics

# Nonendpoint cubic residuals: actual factors and exact contact division

Date: 2026-10-12. Author: cubic_contact_symbolics, independent algebra companion
to oct12_cubic_pair_support.

Status: **DIRECT ALGEBRAIC DERIVATION, WITH TEN SUPPORTING IDENTITIES VERIFIED;
INDEPENDENT PROOF AUDIT AND ROOT ACCEPTANCE PENDING.** This is not a closure of
the cubic-pair locus. Work over an algebraically closed field of characteristic
zero. Retain delta!=0, actual center avoidance, and repeated cubic factors.

The actual sections and residual coefficients are those of the
[pole-filtration note](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md)
and the [residual-factor note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md).
No frozen source, canonical record, or Git state was changed for this work.

## 1. Actual restriction and complete cubic-divisor equations

Consider a prime cubic with affine equation t+m r+n=0. Its normalization is
P1 with affine coordinate r. Put

    T_c=r^2-m r-n.

The four actual projected sections restrict to cubic polynomials f_i:

    f0=-r^3+(m^2+m+a)r^2+[n(2m+1)-a m]r+n^2-a n,
    f1=-r^3+(m^2+m-delta m+b)r^2
             +[n(2m+1-delta)-b m]r+n^2-b n,
    f2=-r^3+(m^2+m-3delta m+3delta^2+g)r^2
             +[n(2m+1-3delta)-delta^3-g m]r+n^2-g n,
    f3=-r^3+(m^2+m-4delta m+6delta^2+d)r^2
             +[n(2m+1-4delta)-4delta^3-d m]r+n^2-d n+delta^4.

Let

    A=a+d-b-g, Bprod=ad-bg,
    C=(4a-3b-g)delta-3delta^3-A,
    E=Bprod+delta^4,
    P2=Bprod+(6a-3b)delta^2+3delta^3,
    L=(-4a+b)delta^3-delta^4, N=a delta^4.

The exact restricted quadric is

    f0 f3-f1 f2=T_c F(r,-m r-n),
    F=A t^2+(C r+E)t+(-3delta^2-A)r^3+P2 r^2+L r+N.

For the 3+3 residual partition A=-3delta^2. The cubic divides F exactly if

    D2=-3delta^2 m^2-C m+P2=0,
    D1=-6delta^2 m n-C n-E m+L=0,
    D0=-3delta^2 n^2-E n+N=0.                         (1)

These are complete conditions for this factor. They do not divide by n,
m, a root difference, or a discriminant. The other factor is

    t+m' r+n', m'=C/A-m, n'=E/A-n.

Consequently the conditions retain the doubled cubic m'=m,n'=n.

## 2. Actual linear/quadratic factorization on the class (2,1) image

Assume the actual projected cubic is a basepoint-free image of class (2,1),
as required by the cycle and fiber arguments in the residual-factor note.
On the Segre quadric the matrix [[f0,f1],[f2,f3]] has rank one. A primitive
factorization therefore has the form

    (f0,f1,f2,f3)=(L0 Q0,L0 Q1,L1 Q0,L1 Q1),

where the L_i are homogeneous linear forms and the Q_i are homogeneous
quadratic forms. The two pairs have no common zero. Since every f_i has
leading coefficient -1, the affine factors can be normalized so that
both L_i have leading coefficient 1 and both Q_i have leading coefficient -1.
Thus L1-L0 is a constant. It must be nonzero: otherwise the first Segre
coordinate would be constant and the image would not have class (2,1).

Define

    B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a,
    kappa=a-g+3delta m-3delta^2.

The constant L1-L0 is exactly kappa, obtained by comparing the r^2 term
of f2-f0. In particular kappa!=0 on this class (2,1) locus. The factors are
explicit:

    Q0=-r^2+q r+w,
    q=-(3delta n+delta^3+(g-a)m)/kappa,
    w=-(g-a)n/kappa,
    D=Q1-Q0=(delta^2/kappa)[3(m-delta)r+delta^2+3n],
    u=m^2+m+a-q,
    L0=r-u, L1=r-u+kappa.                             (2)

These formulas come from Q0=(f2-f0)/kappa and
Q1=(f3-f1)/kappa, followed by the r^2 coefficient of f0=L0 Q0.
They are justified by the primitive factorization, rather than by an
unchecked division of a specialized polynomial.

The first equation of (1) gives the useful exact identity

    kappa(B-delta m)-3delta^2(m-delta)=D2.             (3)

Hence the linear coefficient of D is B-delta m on the actual divisor
locus. No conclusion is asserted for kappa=0 beyond its incompatibility
with the stated class (2,1) assumption.

## 3. Degree-seven contact and the exact quartic excess factor

The fixed curve C0 on the Segre quadric has equation

    L1 Q0^3-L0 Q1^3=0.

Pulling it back to this cubic gives the binary form of degree seven

    K=L1 Q0^3-L0 Q1^3
      =kappa Q0^3-L0 D(3Q0^2+3Q0 D+D^2).             (4)

The r^7 coefficient cancels. Its r^6 coefficient is

    -kappa-3(B-delta m)=-Jbar,                       (5)

since A=G+Jbar=-3delta^2. Therefore the contact at the parameter infinity
is exactly one whenever Jbar!=0. This is the actual full contact form,
not a bound obtained from a first conormal symbol.

There is scheme-theoretic division by T_c, including a repeated root.
The actual cubic equations of C0 pull back as

    f0^2 f2-f1^3=L0^2 K,
    f2^3-f1 f3^2=L1^2 K.

Before restriction they are multiples of the actual affine equation T of
c. Thus both displayed polynomials are divisible by T_c. Since
L1-L0=kappa!=0, gcd(L0,L1)=1, and the divisibility at each irreducible
factor of T_c forces T_c|K with its full multiplicity. Write

    K=T_c H.                                       (6)

On Jbar!=0 the polynomial H has degree exactly four and leading
coefficient -Jbar. Full inverse support forces every root of H to be a
root of T_c: the cubic intersects c only at the finite T_c roots and
the shared infinity point, while (5) already accounts for exactly the
single contact at infinity. All endpoints, including a root r=0 or
r=delta, are retained by the polynomial formulation.

If T_c has distinct roots alpha,beta, full inverse support therefore
requires

    K=-Jbar(r-alpha)^N(r-beta)^P,
    N+P=6, N>=1, P>=1.

If T_c=(r-alpha)^2, it requires

    K=-Jbar(r-alpha)^6, H=-Jbar(r-alpha)^4.

These are necessary contact profiles, not realizations or exclusions.

For a fully explicit coefficient division, write K=sum(k_i r^i,i=0..6).
The coefficients of H from r^4 through r^0 are

    h4=k6,
    h3=k5+m k6,
    h2=k4+m k5+(m^2+n)k6,
    h1=k3+m k4+(m^2+n)k5+(m^3+2mn)k6,
    h0=k2+m k3+(m^2+n)k4+(m^3+2mn)k5
                              +(m^4+3m^2 n+n^2)k6.

The supporting checker verifies this division with the two exact
remainder expressions; their vanishing on the actual class (2,1)
divisor follows from the preceding coprime-factor proof.

## 4. Complete two-cubic coefficient matching

To compare two cubic factors set

    m_i=delta s_i, n_i=-delta^2 p_i,
    x=B/delta^2, zeta=1/delta,
    S=s1+s2, Sprod=s1 s2,
    P=p1+p2, Pprod=p1 p2, Cross=s1 p2+s2 p1.

Matching F=-3delta^2(t+m1 r+n1)(t+m2 r+n2) first gives

    a/delta^2=-3 Pprod,
    G=delta^2[3(S-1)-6x]+3delta.

The remaining t,r^2,r coefficients are equivalent to

    Eeq=x^2-x(S-1)-x zeta+3Pprod+1/3-P=0,
    Peq=x^2-x S+(1-x)zeta+Sprod=0,
    Leq=x+9Pprod-3Cross-zeta=0.                       (7)

Subtracting Eeq-Peq and comparing with Leq gives the necessary pair
condition

    Sprod-3Cross+P+6Pprod-1/3=0,                    (8)

and both inverse-separation expressions

    zeta=x+9Pprod-3Cross
        =x-Sprod+1/3-P+3Pprod.                     (9)

One further matching equation must be retained. After (9), Eeq and Peq
are both

    x(2/3-S+Sprod+P-3Pprod)+1/3-P+3Pprod=0.         (10)

Equations (8)-(10), the a,G formulas, delta!=0 and zeta=1/delta give
complete coefficient matching. Equation (8) alone is only necessary.
No division by the coefficient of x in (10) is allowed when it vanishes;
that case remains in the formulas. Interchanging the two cubics and
coinciding factors are both retained.

## 5. Execution provenance and limits

The [Macaulay2 source](../computations/verify_session_nonendpoint_cubic_contact_2026_10_12.m2)
has SHA256

    c26395b318525b6b531ebc96f91bc9866fbbb186ae9982f79443c2fb7508bd58.

The final [execution record](../validation/2026-10-12-nonendpoint-cubic-contact/20261012T213343388888Z/execution-record.json)
records exit zero, ten supporting PASS markers, and empty stderr.
The stdout SHA256 is

    8b51e048a03a937068ead016b3bd3d572a4d5b00c0953d8a954bfa2ded938d55.

This is one checker lineage. Four earlier captured attempts remain:

| Captured attempt | Outcome |
| --- | --- |
| 20261012T213217027300Z | Setup failure: protected M2 name dd; no conditions executed. |
| 20261012T213255094212Z | Six conditions passed, then coefficient-extraction assertion failed because r was in a multivariate ring. |
| 20261012T213311715636Z | Seven conditions passed, then protected M2 name quotient caused setup failure. |
| 20261012T213321280566Z | Eight conditions passed, then the preexisting M2 identifier zeta prevented constructing the final ring. |
| 20261012T213343388888Z | All ten supporting conditions passed after using a polynomial coefficient ring and unambiguous identifiers. |

The second attempt is an actual recorded assertion failure in a faulty
coefficient interface. Passing after correction verifies the stated
polynomial coefficient; it does not erase the failed source or raw output.
The exact commands, per-version sources, hashes, times, exit codes and raw
stdout/stderr are preserved in the validation directory. No large
Gröbner computation, parameter-space exhaustion, generic numerical sample,
or global STCI conclusion is claimed by this note.


---

## 3. nonendpoint type1 two family exclusion

# The two Type1 conic-plus-quartic families have no mate

Date: 2026-10-12. Author: `nonendpoint_pole_spaces`.

Status: **DIRECT ALL-MATE EXCLUSION WITH EXACT SUPPORTING COMPUTATIONS;
INDEPENDENT PROOF AUDIT OUTSTANDING**. This note closes exactly the first two
one-parameter families in section 4a of the frozen
[residual factor and genus reduction](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md).
It does not close its other six families or the remaining nonendpoint
integral and cubic-pair residuals. The frozen owner and sealed files were
not edited.

## 1. Actual family and residual quartic

The field is algebraically closed of characteristic zero. Let delta be
arbitrary and nonzero, and let x be either root of `2x^2-2x-1=0`. Define

    eta=2x-1, eta^2=3,
    u=x delta^2, w=(u+4delta^2)/3,
    a=(u+w+delta-delta^2)/2,
    b=a-u, g=a-w, d=a-u-w,
    rho=delta/2.

This is the Type1 family whose conic image meets C0 with multiplicities
(1,3) at target parameters (1,-1). Its residual divisor is the actual
sum of the degree-two prime `r=rho` and a degree-four prime. Put

    j=(3u+w)delta-3delta^3=(5/3)eta delta^3,
    p2=-uw+(3a+3u)delta^2+3delta^3.

Since j is nonzero, the quartic prime is the graph

    t=[3delta^2 r^2-(p2-3delta^2 rho)r+2a delta^3]/j,
    T=r^2+t=N4(r)/j,
    N4=(j+3delta^2)r^2-(p2-3delta^2 rho)r+2a delta^3.          (1)

Its intrinsic anticanonical coordinates span 1,r,r^2,r^3,r^4, so it is
a smooth rational normal quartic in the intrinsic P5, including its
point r=infinity, which is the A4 point p.

Only admissible line centers, avoiding S and inducing its finite birational
normalization projection, are potential mates. No value of nonzero delta
is discarded for convenience; inadmissible centers simply cannot furnish
a candidate. A mate forces the full inverse-support condition (SUP),
and the restriction c->C0 is an isomorphism. The frozen residual reduction
then shows that this quartic maps birationally to the smooth Q-curve R4 of
class (3,1). In fact the finite birational curve map is an isomorphism.

## 2. The actual intrinsic contact length is four in every delta stratum

On the finite chart the ideal of c restricted to the quartic is generated
by T=N4/j. At infinity use the A4 coordinates

    alpha=rt/v, beta=t/v, chi=r^2/v, v=t^2-r^3.

The ideal of c is generated by

    beta+chi, (1-alpha)chi-alpha^2.

On the quartic these are exactly

    T/v, -r^3 T/v^2.                                     (2)

The ratio -r^3/v is regular and vanishes at infinity because t has a
nonzero quadratic leading coefficient and v has a nonzero quartic
leading coefficient. Thus the first expression generates the restricted
ideal there. The function v has pole four, while T is a nonzero polynomial
of degree at most two. If the degree of T drops, its finite zero length
drops by the same amount that its zero order in (2) at infinity increases.
Consequently the total intrinsic ideal length is always four.

T cannot vanish identically: (1) has derivative at rho equal to
`N4'(rho)=-2delta^4`, which is nonzero. This argument retains all degree
drops and repeated zeros of T.

The target intersection has length

    C0.R4=(1,3).(3,1)=10.                               (3)

Therefore (SUP) would require six excess contact lengths beyond the
intrinsic four.

## 3. All possible finite conductor contacts are explicitly retained

Use the actual balanced conormal cubics P,J from the
[conormal reduction](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md).
Their homogeneous leading coefficients on this family are opposite
nonzero multiples of eta delta^2. There is no common zero at infinity.
At a finite smooth point of c where they are not both zero, the
normalization projection is immersive. Under (SUP) its fiber is one point
with the same residue field; finite cotangent surjectivity and Nakayama
make the map a local isomorphism. Such a point contributes no excess.

At the A4 point the actual tangent determinant is

    -3delta^3(d-2g+2b-a),
    d-2g+2b-a=w-3u=-(4/3)eta delta^2 !=0.

Thus the map is also a local isomorphism at p. All excess contact on the
quartic must occur at finite common zeros of P,J that also lie on T=0.

Both cubics have the factor r-rho. Write P=(r-rho)P2 and
J=(r-rho)J2. Their homogeneous quadratic resultant is exactly

    Res(P2,J2)=(8/3)delta^9 K(delta),
    K(delta)=5delta^3+9eta delta^2+45delta+9eta.              (4)

Their sum is

    P2+J2=-delta^2[Lsigma r-Nsigma],
    Lsigma=2(eta delta+3),
    Nsigma=delta[(eta+2)delta+3].                          (5)

The quartic contact polynomial at rho is

    N4(rho)=delta^4(eta delta+1)/4.                        (6)

The captured computation proves the stronger complete incidence equality
in `k[x,delta,r]/(2x^2-2x-1)`, after saturation by delta:

    (P,J,N4):delta^infinity
      = (r-rho,eta delta+1)
          intersect (K,Lsigma r-Nsigma).                 (7)

This equality retains every finite parameter value and common root,
including coincidences. In the second stratum Lsigma is a unit: substituting
delta=-3/eta in K gives -72/eta, which is nonzero. Also sigma=Nsigma/Lsigma
differs from rho, as follows from (5) evaluated at rho. In that stratum
delta and j are units as well. The two strata are disjoint because

    K(-1/eta)=-32/(3eta) !=0.                              (8)

Hence, for each fixed admissible delta, the quartic has at most one point
of possible excess contact: rho when eta delta+1=0, or sigma when K=0.
Outside these finite parameter strata there is no such point. There is
no inference from a first symbol about the possible contact order.

## 4. Full actual target contact has order two on both entire finite strata

On Q in the target chart X0!=0, the Cartier equation of C0 is

    phi=(X0^2 X2-X1^3)/X0^3.                             (9)

Use the actual four sections restricted to (1), rather than their first
symbols. For a jet r=r0+e, a common denominator j^2 gives scaled polynomial
sections Zi. They satisfy `Z0 Z3-Z1 Z2=0` identically. The numerator
`Z0^2 Z2-Z1^3` is the actual target contact expression. Both captured jet
checks verify that Z0 at the point is a unit, so this numerator computes
the exact contact order of (9).

On the linear stratum eta delta+1=0, take r0=rho. The constant and linear
jet coefficients vanish, and the second coefficient in the captured
homogeneous clearing is

    -800000 eta/129140163,

which is nonzero on both algebraic branches.

On the cubic stratum K=0, take r0=sigma. Clear its denominator using
`r=(Nsigma+e Lsigma)/Lsigma`; this scales each actual section by the
nonzero unit `j^2 Lsigma^4`. The constant and linear coefficients again
vanish. The second coefficient is a unit in the complete coefficient
algebra

    k[x,delta]/(2x^2-2x-1,K),

as verified by the exact ideal equality `(secondCoefficient)=(1)`.
This is a statement covering every cubic root and both x branches; no
generic nonvanishing is substituted for a finite-stratum check. The cubic
is separable: its discriminant is -746496, which is nonzero.

Thus the actual target contact order is exactly two on both strata.
The intrinsic contact order is at least one. The sole possible excess
is consequently at most one. All other contacts, including p and any
repeated intrinsic contact at a local-isomorphism point, contribute no
excess. This contradicts the six required by (3). Every admissible Type1
projection therefore has no mate in any degree.

## 5. Captured source and failure history

The validation folder is
[the complete ten-execution history](../validation/2026-10-12-nonendpoint-2plus4-families/).
All executions retain an exact source snapshot, separate raw stdout and
stderr, source/stream hashes, timestamps, exit status and scope.

The final sources and actual successful executions are:

* [factor, resultant, and complete incidence checker](../computations/probe_session_nonendpoint_2plus4_families_2026_10_12.m2),
  thirteen assertions, in
  [attempt 10](../validation/2026-10-12-nonendpoint-2plus4-families/attempt-10-type1-complete-incidence/execution-record.json);
* [full cubic-stratum target jet checker](../computations/probe_session_nonendpoint_type1_contact_jets_2026_10_12.m2),
  eight assertions, including a two-condition conjunction, in
  [attempt 07](../validation/2026-10-12-nonendpoint-2plus4-families/attempt-07-type1-cubic-name-repair/execution-record.json);
* [full linear-stratum target jet checker](../computations/probe_session_nonendpoint_type1_linear_contact_jets_2026_10_12.m2),
  the same assertion scope on the other complete finite stratum, in
  [attempt 09](../validation/2026-10-12-nonendpoint-2plus4-families/attempt-09-type1-linear-coercion/execution-record.json).

There were five exit-zero and five nonzero executions in these ten saved
attempts. The development history is not counted as ten independent proofs.
Attempts 01--02 failed coefficient/coercion setup in a nested algebraic
fraction-field construction. Attempt 03 passed six factor/common-root
assertions, but its unverified quotient-ring coefficient extraction produced
a spurious zero exploratory resultant; that output is not accepted as a
certificate. Attempt 04 replaced coefficient extraction by derivatives and
verified reconstruction, obtaining the correct nonzero resultant (4).
Attempt 05 genuinely failed the guessed assertion that only the linear
stratum was present; it exposed the additional cubic stratum retained in
(7), rather than being relabeled as a setup failure. Attempt 06 failed on
the protected name ambient. Attempt 08 failed because the integer constant
2 was compared as an ideal in the wrong ring. The repaired attempts and
all failed source versions remain saved.

The all-mate conclusion uses (SUP), the actual curve map, the global contact
degree ten, the local-isomorphism criterion, and the complete actual
higher-jet calculations on (7). Independent audit is required before
promoting this two-family exclusion to the accepted frontier. The six
Type2/Type3 one-parameter families remain separate research obligations.


---

## 4. nonendpoint type1 two family independent audit

# Independent audit: both Type 1 conic-plus-quartic families are excluded

Date: 2026-10-12. Auditor: `oct12_type1_two_family_audit`.

Status: **PASS: independently reconstructed all-mate exclusion for exactly
the two Type 1 branches.** Characteristic zero and the fixed curve C0 are
essential hypotheses. This does not exclude the other six conic-plus-quartic
families, the integral residual or cubic-pair cases, all quintic carriers,
or C0 in unrestricted degree.

The frozen [owner proof](2026-10-12-session-nonendpoint-type1-two-family-exclusion.md)
was read and checked at SHA-256
`447f4d68991b862b33005ba6b60a73595a21d3d177f54a61e922b5a0605561ed`.
No owner, canonical, earlier audit or seal-bound file was edited.

## 1. Inputs, retained parameters and the exact conditional setting

I reconstructed section 4a of the
[residual reduction](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md),
SHA `d0efa3d74b5b8b59f9f5790b7323404765793905e3553b4e84f5ef865597fc44`,
and its [independent audit](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md),
SHA `db72f936486253cf91e82645de9c3b6b23562dac9da49eee6ee31f0cb94b5322`.
The missing z^2 coefficient in the conic plane section leaves exactly eight
necessary one-parameter families; the present audit covers the two branches
with contact pattern (1,3) at z=(1,-1).

Replace the owner's x by eta=2x-1, so eta^2=3, and retain arbitrary
delta!=0. Then

    u=(eta+1)delta^2/2,
    w=(u+4delta^2)/3,
    a=(u+w+delta-delta^2)/2,
    b=a-u, g=a-w, d=a-u-w, rho=delta/2.

No square-root branch is selected. Both algebraic branches are retained by
the coefficient algebra eta^2=3. No nonzero delta is omitted.

Admissibility means that the actual line center avoids S and the actual
projection is finite birational onto its integral quintic image X. The
accepted intrinsic pair and its projection formulas then give c->C0 an
isomorphism. A hypothetical mate of any positive degree forces the complete
reduced inverse support (SUP): (nu^-1 C0)_red=c, including absence of isolated
extra points. All geometric steps below are made under these hypotheses.
Inadmissible centers do not provide candidates and need not be classified.

## 2. The actual graph is a smooth rational quartic, even at the A4 point

Let j=(3u+w)delta-3delta^3=(5/3)eta delta^3. It is nonzero on the full
parameter domain. The literal residual polynomial factors into r-rho and
a graph component with

    t=[3delta^2 r^2-(p2-3delta^2 rho)r+2a delta^3]/j,
    p2=-uw+(3a+3u)delta^2+3delta^3,
    T=r^2+t=N4(r)/j.

The quadratic leading coefficient of t is 3delta^2/j, always nonzero.
The intrinsic coordinate restrictions therefore span 1,r,r^2,r^3,r^4:
the cubic coordinate -rt has nonzero cubic leading coefficient, and the
quartic coordinate v-rt, with v=t^2-r^3, has nonzero quartic leading
coefficient. Their projective closure is the degree-four rational normal
curve D4. It is smooth at infinity even though that point p is singular on
the ambient surface S. The nonzero cubic and quartic coefficients do not
depend on the leading coefficient of T, so a degree drop of T changes
neither the smoothness nor this argument.

The upstream map-degree argument gives a birational map to the integral
Q-curve R4 of class (3,1). Such an integral Q-curve has arithmetic genus
zero and is smooth. The finite birational curve map D4->R4 is consequently
an isomorphism. No source singularity or hidden multiplicity is inserted
by using this curve isomorphism.

## 3. Intrinsic length four and target length ten

On the finite A2 chart, I_c|D4=(T). At infinity the accepted A4 chart has
alpha=rt/v, beta=t/v, chi=r^2/v, and the actual curve ideal is generated by

    beta+chi=T/v,
    (1-alpha)chi-alpha^2=-r^3 T/v^2.

The second generator divided by the first equals -r^3/v, regular and
vanishing at infinity because v has pole four. Thus T/v generates the
restricted ideal at p. The independent identity N4'(rho)=-2delta^4 proves
T is nonzero. If deg T=m, its finite zero length is m and the infinity
length is 4-m. This proves

    length O_D4/(I_c|D4)=4

for every retained delta, including every repeated zero and every degree
drop. It is an exact ideal calculation on the smooth source curve.

Meanwhile C0.R4=(1,3).(3,1)=10. Via the curve isomorphism, the actual target
Cartier equation has zero divisor of degree ten on D4. Under (SUP), every
such zero lies on c. Its pullback ideal is contained in I_c|D4, so each
local target length is at least the intrinsic length. The total difference
would have to be six.

## 4. Every possible place of excess is retained

I used the corrected [conormal reduction](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md),
SHA `3576392d41d4f64db506291f7cd0609a6930a80296eeedd7c9ccdfa92352c3f5`,
and reconstructed its P,J from the unexpanded quotient-differentiation
expressions using the actual four T derivatives. At each finite point of
c, including r=0 in the opposite frame, a nonzero P or J gives cotangent
surjectivity. Under (SUP), the fiber has one point and equal residue field.
The finite local algebra lemma in the
[all-mate conormal/conductor audit](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md),
SHA `bddb6c89a77e14b25607c22a8e9aaab59d4159ac9a1718b8be651856387baf2a`,
then gives equality of local surface rings. Such points contribute exactly
zero excess; this is stronger than a first-normal estimate.

At p, the full singular cotangent determinant is -3delta^3 Jbar, and

    Jbar=d-2g+2b-a=w-3u=-(4/3)eta delta^2 !=0.

Thus the same local-isomorphism conclusion holds at p, with its full
three-dimensional cotangent space. No excess is available there.

Every possible finite excess point is therefore a common zero of P,J,N4.
The independently reconstructed exact ideal equality in
QQ[eta,delta,r]/(eta^2-3), saturated only by the known nonzero delta, is

    (P,J,N4):delta^infinity
      = (r-rho,eta delta+1) intersect (K,L r-N),
    K=5delta^3+9eta delta^2+45delta+9eta,
    L=2(eta delta+3), N=delta[(eta+2)delta+3].

This is the complete finite incidence, not a generic resultant test. The
checks additionally give

    K(-1/eta)=-32eta/9 !=0,
    K(-3/eta)=-24eta !=0,
    (L r-N)|r=rho=-2delta^2 !=0.

Hence the two parameter strata are disjoint; L cannot vanish on K=0;
sigma=N/L differs from rho. The classical discriminant of K is -746496.
For each fixed eta,delta there is at most one possible excess point: rho
on eta delta+1=0 or sigma on K=0. This exhausts all finite contact points,
including parameter specializations and source intersection multiplicities.

## 5. Direct actual jets bound the sole possible excess

The independent checker evaluates the actual Xi(r,T) on the graph, using
the local curve parameter e=r-r0. It does not copy the owner's cleared
Zi expressions or use first symbols to bound later contact.

For the linear stratum r0=rho, it uses the full coefficient algebra
eta^2=3, eta delta+1=0. For the cubic stratum r0=N/L, it uses the full
coefficient algebra eta^2=3,K=0, with inverses of j and L adjoined.
These are genuine nonzero algebras; the already proved denominator units
mean adjoining the inverses loses no parameter point or branch.

In both algebras the checks prove Xi lie on Q, T(r0)=0, X0(r0) is a unit,
and for the actual contact numerator

    f=X0^2 X2-X1^3

the constant and linear coefficients are zero while the quadratic
coefficient is a unit. In the linear stratum the independently evaluated
unscaled coefficient is exactly -eta/19440. In the cubic stratum its full
coefficient-algebra ideal equals the unit ideal. Since X0 is a unit,
division by X0^3 does not alter the order. The actual target Cartier
contact length is therefore exactly two at every point of both complete
strata.

The intrinsic length at this point is at least one; thus the sole possible
excess is at most one. All other points, including p, give zero excess.
This contradicts the required six. Both Type 1 branches have no mate in
any positive degree.

## 6. Independent exact checks, bindings and failures

The independently constructed [checker](../validation/2026-10-12-type1-two-family-independent-audit/verify_type1.m2)
has final SHA `bbb0042130a391a18f1cfe2fed175c15cc70ffac62912a0604436035d835ffed`.
The [final captured run](../validation/2026-10-12-type1-two-family-independent-audit/attempt-06/execution-record.json)
passed 30 distinct conditions, exited zero, and had empty stderr. Its
stdout SHA is `de8205519577a7dea2aa486b71e4e2d695ce02449a393aece49e17670475bcf7`.

All six audit development executions have immutable source snapshots and
separate raw streams. Attempts 01 and 04 failed on protected M2 names
`check` and `dd`. Attempt 02 passed fifteen identities, then genuinely
failed an assertion equating M2's `discriminant(K,delta)` call to the
classical cubic discriminant. The separately captured
[diagnostic](../validation/2026-10-12-type1-two-family-independent-audit/diagnostic-01/execution-record.json)
shows this library call returns 3732480, whereas the explicit classical
coefficient formula returns -746496; the final checker uses the explicit
formula. Attempt 03 passed sixteen identities, then failed because quotient
ring creation rebound generator symbols before coercion. Attempt 05 passed
28 conditions; attempt 06 added explicit nonzero-algebra checks and passed
30. A direct diagnostic rerun of the attempt-02 snapshot also reproduced
its same failed assertion; it is tool-visible and is not counted as an
additional saved source lineage or proof.

I freshly checked all source/stdout/stderr bindings of the owner's ten
executions 01--10: all thirty bindings match. They contain five exit-zero
and five nonzero executions. The live final owner sources match the
snapshots in attempts 10,07,09 respectively. The history is not interpreted
as ten independent proofs, and attempt 03's spurious exploratory zero
resultant is not used. This audit adds a separate construction of the
finite incidence and actual unscaled jets, together with the geometric
length argument above.

No finite degree scan, unchecked generic specialization, pole-stratum
first-normal bound, or agent agreement supplies the all-mate conclusion.


---

## 5. nonendpoint type23 six family exclusion

# The six Type2/Type3 conic-plus-quartic families have no mate

Date: 2026-10-12. Author: `nonendpoint_pole_spaces`.

Status: **DIRECT ALL-MATE EXCLUSION WITH EXACT SUPPORTING COMPUTATIONS;
INDEPENDENT PROOF AUDIT OUTSTANDING**. This is a new owner note. It closes
exactly the six Type2/Type3 families in section 4a of the frozen
[residual factor and genus reduction](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md).
Together with the separate [Type1 exclusion](2026-10-12-session-nonendpoint-type1-two-family-exclusion.md),
it excludes all eight conic-plus-quartic families, conditional on the
independent audit of the new proofs. The integral residual and cubic-pair
residual lanes remain separate obligations. No frozen owner, canonical,
seal, or Git state was edited.

## 1. All six actual families and the admissibility hypothesis

The field is algebraically closed of characteristic zero. Delta is
arbitrary and nonzero. Set

    u=x delta^2, w=3u,
    b=a-u, g=a-3u, d=a-4u,
    eta=2x-1, rho=tau delta.

The two Type2 families have

    tau=1/2, 6x^2-6x+1=0,
    a=2u+(delta-delta^2)/2.

Here eta^2=1/3. The four Type3 families have

    6tau^2-6tau+1=0,
    3x^2-6tau x-1+3tau=0,
    a=(6tau-1)u+tau delta-(3tau-2/3)delta^2.

For Type3, tau is a unit with inverse 6(1-tau), and eta is nonzero: x=1/2
would make its defining quadratic equal -1/4. Every algebraic branch and
every nonzero delta are retained throughout.

On S minus ell use (r,T), t=T-r^2, v=t^2-r^3. The actual projected sections are

    X0=r^4-(2r^2+r)T+T^2+aT,
    U3=r^3-rT,
    X1=X0-delta U3+(b-a)T,
    X2=X0-3delta U3+3delta^2 r^2-delta^3 r+(g-a)T,
    X3=X0-4delta U3+6delta^2 r^2-4delta^3 r+delta^4+(d-a)T.

Only centers avoiding S and inducing its finite birational normalization
projection are candidates. If a mate exists, its full inverse-support
condition is (SUP): the reduced inverse image of C0 is exactly c, and
c maps isomorphically to C0. The frozen reduction then gives the actual
residual D=D2+D4. Both primes map birationally to smooth Q-curves, of
classes (1,1) and (3,1) respectively. The smooth intrinsic rational normal
quartic D4 consequently maps isomorphically to its image R4. We assume
these necessary conditions for a contradiction; no exceptional delta
is discarded by an unproved center test.

## 2. Actual quartic equation and intrinsic contact length

Put

    j=(3u+w)delta-3delta^3=3eta delta^3 !=0,
    p2=-3u^2+(3a+3u)delta^2+3delta^3,
    M=-(p2-3delta^2 rho),
    N=(a/tau)delta^3.

The actual residual factor is the quartic graph

    t=(3delta^2 r^2+M r+N)/j,
    T=N4(r)/j,
    N4=(j+3delta^2)r^2+M r+N.                       (1)

The factor reconstruction and conic condition are verified in the
captured source. Write k=3delta^2/j, m=M/j, n=N/j. Thus
t=kr^2+mr+n, with k nonzero; v has pole four on D4.

At finite points the ideal of c restricted to D4 is generated by T.
At its point p with r=infinity use the actual A4 coordinates

    alpha=rt/v, beta=t/v, chi=r^2/v.

The generators beta+chi and (1-alpha)chi-alpha^2 restrict exactly to

    T/v, -r^3 T/v^2.                                 (2)

Since -r^3/v is regular and vanishes at p, the first generator gives
the restricted ideal. If s=degree T, its intrinsic contact order at p
is 4-s; finite zeros have total length s. Section 4 verifies that s is
always two or one in these six families. In particular T is never zero
or constant. The total intrinsic contact length is exactly four for
every delta, including repeated finite roots and the degree drop.

The target intersection length is

    C0.R4=(1,3).(3,1)=10.                            (3)

Under (SUP), every one of these target intersections has a preimage
in D4 intersect c. The isomorphism D4 to R4 computes its local target
length in the parameter of D4. Therefore six total excess lengths
beyond the intrinsic four are necessary.

## 3. All possible finite excess contacts and their exact parameter strata

Use the actual balanced conormal polynomials

    P=(g-3b+2a)r^3+[6delta(b-a)+delta^3-3delta^2]r^2
        +[delta^2(6a-3b)+2delta^3]r-2a delta^3,
    J=(2d-3g+b)r^3+[3delta(g-b)+5delta^3-3delta^2]r^2
        +[3b delta^2+delta^3-delta^4]r-b delta^3.

Their degree-three coefficients vanish in all six families. Their
degree-two coefficients differ by -4delta^3, which is nonzero. Thus
they cannot both vanish identically, and for each fixed delta their
common finite support has at most two points. At a finite c point where
P,J are not both zero the projection is immersive. Under (SUP) the
fiber is a single point with equal residue field, so the finite
cotangent/Nakayama argument makes the projection a local isomorphism.
Its contribution to excess contact is zero. This uses the actual
map and the full inverse-support condition, rather than a bound
deduced from the order of a first symbol.

All finite points where D4 can acquire excess belong to the complete
scheme

    I=(P,J,N4):delta^infinity.                        (4)

The exact computations retain its nonreduced structure and do not
replace it by a generic common-root count.

For Type2 the captured ideal equality is

    I=(5(delta+3eta)^2(delta+3eta/5),
          4r-(3eta+2)delta-1).                       (5)

It has length six across the two x branches. Its reduced support has
two delta values on each branch, with a single possible finite contact
point for each value:

    delta=-3eta,   r=-(1+3eta)/2;
    delta=-3eta/5, r=(1-3eta)/10.                    (6)

The doubled parameter component at delta=-3eta remains in (5).

For Type3 the scheme (4) has length twelve across the four (tau,x)
branches. The exact parameter-only eliminated ideal is generated by

    H3(delta)=delta^2+(8x-4tau-2)delta+1.             (7)

Every finite point over these values is retained by (4), with the
full Groebner basis captured in attempt 15. No particular root r is
selected or thrown out, and no extra irreducibility or simple-root
assumption is used. Equation (7) has nonzero constant coefficient.
For any fixed delta the preceding quadratic-degree argument still
bounds its actual finite contact support by two points.

On the complete schemes (4), delta, j, r, and X0 at the contact point
are units, as asserted in the jet source. Thus every finite possible
excess contact is covered by the actual target chart X0 nonzero,
including the entire parameter exceptions in (5) and (7). There is
no unhandled opposite-frame or denominator stratum.

## 4. A4 full contact, including the leading-degree drop

Although the projection tangent determinant at p is zero here because
d-2g+2b-a=w-3u=0, the actual target contact can be computed directly.
Let e=1/r and let Zi=j^2 e^4 Xi be the four scaled actual sections.
At e=0 all Zi have value 9delta^4, a nonzero unit. The actual target
equation of C0 in this Q chart is

    phi=(Z0^2 Z2-Z1^3)/Z0^3.

The captured check verifies Z0 Z3-Z1 Z2=0 identically. The constant,
linear, and quadratic coefficients of A=Z0^2 Z2-Z1^3 vanish, and
its cubic coefficient is exactly

    [e^3]A=54delta^9 j^2(j+3delta^2).                (8)

If j+3delta^2 is nonzero, T has degree two. The actual target contact
order is exactly three, and the intrinsic order at p is two.

The entire degree-drop stratum j+3delta^2=0, saturated by delta, has
the following exact parameter relations:

    Type2: delta+6x-3=0, equivalently delta+3eta=0;
    Type3: delta+6x-12tau+3=0.                       (9)

On both complete strata the ideal of the middle numerator M is the
unit ideal. Hence degree T is exactly one there, and there is no
further constant or zero-polynomial T stratum. The quartic coefficient
of the actual target equation, modulo the degree-drop ideal, is

    [e^4]A=-2delta^3 j^5 M,                         (10)

which is a unit. Thus actual target contact is exactly four and
intrinsic contact exactly three. In every delta stratum, the excess
at p is exactly one. This is a full third/fourth-jet calculation of
the actual sections; a rank-two tangent calculation would not establish it.

## 5. Complete finite higher jets, including the Type2 degeneration

On each complete coefficient scheme (4), take r=r0+e and evaluate
the four actual sections on (1). The source scales them by the unit
j^2 to obtain polynomial Zi, asserts their Q equation identically,
asserts T(r0)=0 and Z0(r0) a unit, and evaluates the actual numerator

    A(e)=Z0(e)^2 Z2(e)-Z1(e)^3.

Its constant and linear coefficients vanish on the whole incidence
scheme. Write a2=[e^2]A and a3=[e^3]A. For Type2 the captured exact
identities in that coefficient algebra are

    (a2)=(delta+3eta),   (a2,a3)=(1).                (11)

The first intrinsic coefficient of T is a unit on a2=0, verified by
its joint unit ideal with a2. Therefore at delta=-3eta the finite
actual target contact has order exactly three, the intrinsic contact
has order exactly one, and its finite excess is exactly two. At the
other retained delta=-3eta/5 the second target coefficient is a unit,
so actual target contact has order exactly two. In particular there
is no fourth-or-higher finite contact concealed by the vanishing of
the second coefficient or by the doubled parameter component in (5).

For Type3 the second target coefficient is a unit on the entire
scheme (4):

    (a2)=(1).                                      (12)

Every finite possible excess contact consequently has actual order
exactly two. The intrinsic order is at least one, so each finite
excess is at most one. All roots of (7), all branches, and every
common-root coincidence are included in this unit-ideal assertion.

## 6. Contact-degree contradiction and scope

For Type2, (5) supplies at most one possible finite excess point
for a fixed delta, contributing at most two. For Type3 there are
at most two such points, each contributing at most one. At p the
excess is exactly one in every stratum. Every other intersection
is at a local-isomorphism point and contributes zero excess.
Thus in all six families the total excess is at most three.
Equation (3) requires six. This is impossible.

Every admissible Type2 or Type3 projection therefore has no mate in
any degree. No center value was lost to a genericity assumption, no
finite parameter stratum was suppressed, and all actual higher-jet
degeneracies affecting the proof are retained. The conclusion closes
these six families only; it does not prove the global STCI assertion,
nor exclude the nonendpoint integral or cubic-pair residual families.

## 7. Exact sources, captures, and development history

All six new executions (attempts 11--16) are preserved in the existing
[validation directory](../validation/2026-10-12-nonendpoint-2plus4-families/).
Each has an exact source snapshot, raw stdout and stderr, UTC timestamps,
cwd, command, actual exit status, and SHA256 hashes for source and streams.
The complete directory also preserves the ten Type1 executions and its
earlier mathematical and setup failures.

Final Type2/Type3 sources and successful final executions are:

* [complete finite incidence and explicit parameter strata](../computations/probe_session_nonendpoint_type23_incidence_2026_10_12.m2),
  SHA256 `3e38399e9e235fb0bf99d26ecf45c7c5496ac8a159cbc6de04223b58b5907616`,
  [attempt 15](../validation/2026-10-12-nonendpoint-2plus4-families/attempt-15-type23-polynomial-strata-repair/execution-record.json);
* [actual finite target contact jets](../computations/probe_session_nonendpoint_type23_full_contact_jets_2026_10_12.m2),
  SHA256 `9137a847ba2d6fa271047c0d103fe8cb62f8f451cf61f20cd367f3b4689502df`,
  [attempt 16](../validation/2026-10-12-nonendpoint-2plus4-families/attempt-16-type23-explicit-second-jet-degeneration/execution-record.json);
* [actual A4 contact jets and complete degree-drop checks](../computations/probe_session_nonendpoint_type23_a4_contact_2026_10_12.m2),
  SHA256 `366c242c57f43cd94792c81fd0ad13c00b8b2d7f17e3635ea775c8fd3196d092`,
  [attempt 13](../validation/2026-10-12-nonendpoint-2plus4-families/attempt-13-type23-a4-contact/execution-record.json).

Attempts 11 and 12 were successful, respectively computing complete
incidence and checking actual second/third jets before making the finite
strata explicit. The nonunit second coefficient in Type2 was retained as
a real degeneracy, with a nonvanishing third coefficient, not called a
setup failure or discarded. Attempt 13 proved both complete A4 cases.
Attempt 14 passed the Type2 exact incidence equality and the Type3
parameter polynomial containment but exited nonzero on an optional
parameter-only elimination call: Macaulay2 requires the elimination ideal
in a polynomial ring, rather than the quotient ring used in that call.
Attempt 15 lifted the ideal and included both algebraic defining relations
in the polynomial ring, proving the exact eliminated ideal (7).
Attempt 16 sharpened the finite jet result to the complete Type2
degeneration equality (11) and the Type3 unit identity (12).
The six new executions contain five actual exit-zero and one nonzero
execution. Independent audit is still required before promotion.


---

## 6. nonendpoint type23 six family independent audit

# Independent audit: all six Type 2/Type 3 quartic-residual families are excluded

Date: 2026-10-12. Auditor: `oct12_type1_two_family_audit`.

Status: **PASS: independently reconstructed all-mate exclusion for the two
Type 2 and four Type 3 branches.** Together with the separate
[Type 1 independent audit](2026-10-12-session-nonendpoint-type1-two-family-independent-audit.md),
this excludes the entire residual partition 2+4 in the accepted nonendpoint
genus-one quintic family. The integral and cubic-pair residual cases, other
quintic normalizations and higher-degree carriers remain outside this result.
The fixed C0 and the universal STCI problem remain open.

The frozen [owner proof](2026-10-12-session-nonendpoint-type23-six-family-exclusion.md)
was read at SHA-256
`11c13ba7201b84e02cf1a2ab1d6b42d8cf5fbcbaf15b51e95d5c75c65f7de48d`.
No owner, canonical or old seal-bound file was changed. The audit is separate
from the earlier Type 1 audit and has a new independent checker lineage.

## 1. Exact scope and independent algebraic branch coordinates

Work over an algebraically closed field of characteristic zero, on the
accepted degree-five A4 normalization pair (S,c) with c mapping isomorphically
to C0. Retain every nonzero delta. Under an admissible normalization projection
and a hypothetical mate in any degree, full inverse support (SUP) holds:
the reduced inverse image of C0 is exactly c, without isolated extra points.

The eight necessary conic-plus-quartic families were reconstructed in the
[residual reduction audit](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md),
SHA `db72f936486253cf91e82645de9c3b6b23562dac9da49eee6ee31f0cb94b5322`,
binding the owner reduction SHA
`d0efa3d74b5b8b59f9f5790b7323404765793905e3553b4e84f5ef865597fc44`.
The present families have u=x delta^2, w=3u, b=a-u, g=a-3u, d=a-4u.

The independent checker uses different algebraic coordinates from the owner:

    Type 2: epsilon^2=3, x=(epsilon+3)/6, tau=1/2,
            a=2u+(delta-delta^2)/2.
    Type 3: theta^2=3, zeta^2=6,
            tau=(theta+3)/6, x=(theta+zeta+3)/6,
            a=(6tau-1)u+tau delta-(3tau-2/3)delta^2.

For Type 2 this is equivalent to 6x^2-6x+1=0. For Type 3 the substitution
is equivalent to 6tau^2-6tau+1=0 and
3x^2-6tau x-1+3tau=0: the latter says (x-tau)^2=1/6.
Thus the reduced coefficient algebras retain all two or four branches over
an algebraically closed field; no numerical square root or selected root is
used. The tau inverse is exactly 2 for Type 2 and 6(1-tau) for Type 3.

The graph denominator is

    j=3(2x-1)delta^3.

In the independent coordinates it equals epsilon delta^3 for Type 2 and
(theta+zeta)delta^3 for Type 3. Epsilon^2=3, while
(theta+zeta)(theta-zeta)=-3. Thus j has no root for delta!=0 in any branch.
Adjoining its inverse in the checker loses no candidate, and center
avoidance is never assumed generically in place of checking an exceptional
parameter: the argument applies to any admissible center with these values.

## 2. Source curve, intrinsic contact and target contact

The actual factor reconstruction gives D=D2+D4, where

    t=(3delta^2 r^2+M r+N)/j,
    M=-(p2-3delta^2 rho), rho=tau delta,
    p2=-3u^2+(3a+3u)delta^2+3delta^3,
    N=(a/tau)delta^3,
    T=[(j+3delta^2)r^2+Mr+N]/j.

Its nonzero t quadratic coefficient makes D4 a smooth intrinsic rational
normal quartic, including its point p at infinity on the singular A4
surface. This statement is unaffected by a degree drop of T. Under (SUP),
the upstream map-degree proof gives D4 a finite birational map to the
smooth Q-curve R4 of class (3,1), hence a curve isomorphism.

At finite r the actual restricted curve ideal is (T). At p its accepted
A4 generators restrict to T/v and -r^3 T/v^2, where v=t^2-r^3 has pole four.
The ratio -r^3/v is regular and vanishes at p, so T/v generates there.
The checker proves degree T is always two or one, with all drop parameters
retained. Therefore finite intrinsic lengths total deg T, the infinity
length is 4-deg T, and total intrinsic length is exactly four.

The actual target intersection degree is C0.R4=(1,3).(3,1)=10. Under
(SUP), all ten local target lengths occur over c. The pullback of the
target ideal is contained in the reduced source ideal I_c; thus each
target length is at least its corresponding intrinsic length. The total
excess required is six. The next two sections prove the excess is at most
three without imposing a degree bound on the hypothetical mate.

## 3. Every possible finite excess and its actual higher jets

I reconstructed P,J directly from the unexpanded conormal expressions and
the actual projection derivatives. Their cubic terms vanish on these six
families; their quadratic coefficients differ by 4delta^3. Hence they
cannot both vanish identically at any retained parameter, and have at most
two common finite points for a fixed parameter.

At a finite c point with P or J nonzero, the actual target cotangent map is
surjective, including r=0 in the reversed frame. Under (SUP) the fiber is a
single point with equal residue field. The finite local Nakayama argument
in the [conormal/conductor audit](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md)
makes the surface projection a local isomorphism. The actual reduced curve
ideals then agree, so such a point contributes zero excess. First symbols
are used here to prove a local ring equality, not to bound later contact.

All possible finite excess belongs to the complete incidence

    I=(P,J,N4):delta^infinity,
    N4=(j+3delta^2)r^2+Mr+N.

The independent Type 2 identity is

    I=(5(delta+epsilon)^2(delta+epsilon/5),
           4r-(epsilon+2)delta-1).

The scheme has length six across both branches, including the doubled
parameter component. For each fixed delta its support has at most one
point. The independent Type 3 parameter-only eliminated ideal is exactly

    (delta^2+(2theta+4zeta)delta/3+1),

equivalent to the owner's H3. The full source incidence has length twelve
across all four branches. The actual incidence, rather than just this
parameter polynomial, is retained throughout the finite jet check.

Both independent finite algebras are explicitly checked nonzero. Only
delta and the already proved j units are inverted. On the full incidence,
r=0 is absent and X0 at the point is a unit; therefore the finite target
chart covers every possible exceptional point, without losing an opposite
frame. The actual sections Xi are directly evaluated at r=r0+e and the
graph T(r). Their Q equation holds identically, and T(r0)=0. Write

    f(e)=X0(e)^2 X2(e)-X1(e)^3.

Its constant and linear coefficients are zero in both full incidence
algebras. In Type 2 the independent exact ideal equalities are

    ([e^2]f)=(delta+epsilon),
    ([e^2]f,[e^3]f)=(1).

The intrinsic first T coefficient together with [e^2]f also generates
the unit ideal. Thus on delta=-epsilon the target order is exactly three,
the intrinsic order exactly one, and the excess exactly two. At the other
retained value delta=-epsilon/5 the target order is exactly two and excess
at most one. The second coefficient is genuinely not a unit on the whole
Type 2 incidence; its degeneration is retained, including the nonreduced
parameter component.

For Type 3, [e^2]f is a unit on the entire incidence. The actual target
order is exactly two at every exceptional finite point, hence the excess
is at most one per point. The at-most-two common-root bound gives at most
two finite excess lengths. Because X0 is a unit, dividing f by X0^3 to
obtain the actual Cartier equation of C0 on Q does not change any order.

## 4. Infinity: actual third and fourth jets retain the degree drop

Put q=1/r and W=q^2 T. Independently homogenizing the actual affine
sections gives Fi=q^4 Xi(1/q,W/q^2), with

    F0=1-2W+W^2-qW+a q^2 W,
    F1=F0-delta q(1-W)+(b-a)q^2 W,
    F2=F0-3delta q(1-W)+3delta^2 q^2-delta^3 q^3+(g-a)q^2 W,
    F3=F0-4delta q(1-W)+6delta^2 q^2-4delta^3 q^3+delta^4 q^4
          +(d-a)q^2 W.

This uses actual sections, independently of the owner's j^2-scaled
expressions. The complete delta-open coefficient algebras are explicitly
checked nonzero. F0(0)=9delta^4/j^2 is a unit, and the Q equation holds.
Let f_inf=F0^2 F2-F1^3. Its first three coefficients, through q^2, vanish.
The independently reconstructed cubic coefficient identity is

    [q^3]f_inf=54delta^9(j+3delta^2)/j^4.

Outside j+3delta^2=0 this is nonzero. T has degree two, so intrinsic order
at p is two and actual target order is three: excess one.

The complete degree-drop ideal in the delta-open algebra is

    Type 2: (delta+epsilon),
    Type 3: (delta+zeta-theta).

These are exactly the owner's delta+6x-3 and delta+6x-12tau+3 relations.
On each complete ideal the middle numerator M is a unit; no constant or
zero T stratum exists. The independent actual fourth coefficient satisfies

    [q^4]f_inf=-2delta^3 M/j
          modulo (j+3delta^2),

and is a unit there. Thus T has degree one, intrinsic order at p is three,
and actual target order is four. The excess is again exactly one. These
third/fourth-jet identities cover every nonzero delta and all six algebraic
branches; the zero cotangent determinant at p is never turned into an
unsupported later-contact bound.

## 5. Contradiction, source bindings and preserved failures

For Type 2 the complete incidence gives at most one finite excess point,
with excess at most two. For Type 3 there are at most two finite excess
points, with excess at most one each. The infinity excess is always one.
Every other intersection is at a local-isomorphism point and gives zero
excess. Total excess is therefore at most three, contradicting the six
required by the exact intrinsic and target lengths. This proves no mate
in any degree on all six families. Combining this with the already frozen
Type 1 audit excludes all eight necessary 2+4 families and therefore the
entire 2+4 residual partition in this nonendpoint normalization family.

The independent [checker](../validation/2026-10-12-type23-six-family-independent-audit/verify_type23.m2)
has final SHA-256
`33cb06e8fa2c0bc2ec44aab1992df03296254c6640008eb74891b323c77c3a5e`.
The [final captured run](../validation/2026-10-12-type23-six-family-independent-audit/attempt-05/execution-record.json)
passed 58 distinct checks, exited zero and had empty stderr. Its stdout
SHA is `be967c3ea87013ebcb4e99274fd8be52b1fa5f3c79b81d92d91686958b3031e4`.
The five saved independent development runs are one failed and four
successful executions of this single lineage. The initial run genuinely
failed its first tau-inverse assertion because my template applied the
Type 3 expression 6(1-tau) to Type 2's tau=1/2. The corrected value is 2;
that failed source and streams are retained. Subsequent successful versions
added the no-j-denominator-loss identities, exact finite degeneration and
parameter elimination, and full degree-drop ideal and nonzero-algebra
checks. They are not counted as independent proofs.

I freshly matched all eighteen source/stdout/stderr bindings of the owner's
six executions 11--16. All match. There are five exit-zero and one nonzero
executions, as claimed. The final live owner source hashes match attempts
15,16,13 respectively:

    incidence: 3e38399e9e235fb0bf99d26ecf45c7c5496ac8a159cbc6de04223b58b5907616
    finite jets: 9137a847ba2d6fa271047c0d103fe8cb62f8f451cf61f20cd367f3b4689502df
    A4 jets: 366c242c57f43cd94792c81fd0ad13c00b8b2d7f17e3635ea775c8fd3196d092

The owner's failed quotient-ring elimination call in attempt 14 and its
repaired polynomial-ring elimination in attempt 15 remain separate captures.
The Type 2 second-jet degeneration is a mathematical parameter stratum,
not a setup failure. The proof above depends on actual higher jets, exact
ideal equalities and the curve intersection count, not agreement among
agents or a generic symbolic run.
