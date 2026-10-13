# Nonendpoint cubic residuals: actual factors and exact contact division

Date: 2026-10-12. Author: cubic_contact_symbolics, independent algebra companion
to oct12_cubic_pair_support.

Status: **DIRECT ALGEBRAIC DERIVATION, WITH TEN SUPPORTING IDENTITIES VERIFIED;
INDEPENDENT PROOF AUDIT AND ROOT ACCEPTANCE PENDING.** This is not a closure of
the cubic-pair locus. Work over an algebraically closed field of characteristic
zero. Retain delta!=0, actual center avoidance, and repeated cubic factors.

The actual sections and residual coefficients are those of the
[pole-filtration note](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md)
and the [residual-factor note](2026-10-12-session-nonendpoint-residual-factor-and-genus-reduction.md).
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
