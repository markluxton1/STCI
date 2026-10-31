# Nonendpoint residual cubic pairs: complete contact and coefficient proof

Fix the embedded curve \(C_0=[s^4:s^3t:st^3:t^4]\), an algebraically closed characteristic-zero field, and the accepted anticanonical degree-five A4 pair \((S,c)\). Retain arbitrary \(\delta\ne0\), the four lift parameters \(a,b,g,d\), and an actual line center disjoint from \(S\), giving a finite birational projection \(\nu:S\to X\) onto an integral quintic. The restriction \(c\to C_0\) is an isomorphism. A hypothetical mate forces **full** reduced inverse support \((\nu^{-1}C_0)_{red}=c\), denoted SUP; it excludes isolated extra inverse points as well as extra curves. The proofs below concern this exact family, not every quintic carrier. The intrinsic pair is proved in [the A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md); actual projection coordinates and every target boundary are in [the target-fiber chapter](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md).

<a id="2026-10-13-session-nonendpoint-cubic-pair-full-independent-audit"></a>
<a id="2026-10-13-session-cubic-pair-theorem-scope-qualification"></a>
<a id="1-nonendpoint-cubic-pair-contact-reduction"></a>

## The full 3+3 no-mate theorem

### 1. Correct theorem, actual setting and retained exceptions

Work over an algebraically closed field of characteristic zero, for the fixed
C0 and the accepted degree-five A4 normalization pair. Retain delta!=0 and
every actual center avoiding the surface. The induced projection is finite
birational, and c maps isomorphically to C0. A hypothetical mate implies the
complete inverse-support condition SUP, including no isolated extra point.

Use B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a, so A=a+d-b-g=G+Jbar. The 3+3
partition lies on A=-3delta^2. The upstream
[residual audit](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#2-nonendpoint-residual-factor-and-genus-independent-audit),
SHA `db72f936486253cf91e82645de9c3b6b23562dac9da49eee6ee31f0cb94b5322`,
proves under SUP that every prime cubic is a smooth rational normal cubic
with equation t+m r+n=0, and maps isomorphically to a smooth Q-curve of class
(2,1). The pushforward cycle retains multiplicity; a doubled source cubic
is permitted. The line-cover and ruling-degree-drop alternatives are already
excluded in that upstream proof, rather than discarded by selecting a minor.

The precise conclusions accepted here are:

* If Jbar!=0, no such projection satisfies SUP, including distinct or doubled
  residual cubics.
* If Jbar=0, no such carrier has a mate, by the separate all-power obstruction;
  failure of SUP is not claimed.
* Thus the entire residual 3+3 lane has no mate in any degree.

### 2. Actual contact at infinity and the complete heptic

On a source cubic put T=r^2-mr-n. Its four actual coordinate sections are
cubic polynomials with leading coefficient -1, so their homogeneous values
at r=infinity are all nonzero. The smooth source and target cubic are
isomorphic; epsilon=1/r is therefore an actual smooth curve parameter there.
For the actual Q-chart equation eta-zeta^3 of C0, where
eta=X2/X0 and zeta=X1/X0, direct expansion gives first coefficient Jbar.
My fresh checker independently verifies that the numerator X0^2 X2-X1^3,
after homogenizing each Xi to epsilon^3 Xi, has first coefficient -Jbar.
Its denominator has constant value (-1)^3, giving the same Jbar. Hence
the contact is exactly one when Jbar!=0. No first-normal estimate of a
later contact order is used.

The primitive Segre factorization of the degree-three curve map is

    (X0,X1,X2,X3)=(L0 Q0,L0 Q1,L1 Q0,L1 Q1),

with homogeneous L_i of degree one and Q_i of degree two, both pairs
basepoint-free. Each factor is nonzero at infinity since all Xi are nonzero
there. Normalize L_i to have affine leading coefficient one and Q_i to have
leading coefficient -1. Then L1-L0=kappa is constant. It is nonzero: if it
vanished, the first Segre projection would be constant, whereas a smooth
(2,1) curve has that projection of degree one. Thus every division by
kappa in the owner's formulas is justified on the full admissible class,
without assuming a generic center minor.

Comparing X2-X0 gives kappa=a-g+3delta m-3delta^2 and

    Q0=(X2-X0)/kappa
       =-r^2-[3delta n+delta^3+(g-a)m]r/kappa-(g-a)n/kappa.

The actual divisor's r^2 coefficient condition gives
kappa(B-delta m)=3delta^2(m-delta). Together with X3-X1-X2+X0 this gives
the exact Q1-Q0 formula in the owner. The r^2 coefficient of X0 determines
L0=r-(m^2+m+a-q), hence all four factor formulas follow from the primitive
factorization and actual coordinate comparison.

The complete contact form is the binary heptic

    K=L1 Q0^3-L0 Q1^3.

The exact ambient identities, independently checked afresh, are

    X0^2 X2-X1^3=L0^2 K,
    X2^3-X1 X3^2=L1^2 K.

Consequently the extra ambient ruling factors are removed, and no common
root is lost because L0,L1 are coprime. This includes target X0=0 and all
other Segre-chart endpoints. The affine leading term of degree seven
cancels; its degree-six coefficient is
-kappa-3(B-delta m)=-Jbar. Thus K has exactly one binary zero at infinity
and six finite contact lengths.

Both ambient cubic restrictions are divisible by the actual polynomial T:
before restriction their expressions are divisible by the affine ideal
generator T of c. Substituting T(r) preserves that exact divisibility even
when T has a repeated root. The two coprime L_i then imply T divides K
with full multiplicity. Under SUP every finite root of K is a root of T;
the binary root at infinity is already accounted for. This is the precise
interpretation of the owner's affine-support statement.

The intrinsic restricted curve ideal has finite length two and infinity
length one. At infinity h=T/v belongs to the actual ideal of c and has
expansion -epsilon+O(epsilon^2), since v=t^2-r^3 has pole three. Hence the
intrinsic total length is three, whereas C0.(2,1)=7. The contact classification
below uses the entire target intersection divisor to control the four
excess lengths, rather than a bound from tangent data.

### 3. Complete homogeneous classification, including all endpoints

A (2,1) target curve has equation P2(U,V)W0+Q2(U,V)W1. Restricting to
C0, where the Segre coordinates are (1:z^3) and (1:z), gives the binary
heptic with possible affine exponents 0,1,3,4,6,7. The two missing
coefficients are z^2,z^5. This restriction is injective because these six
monomials are distinct. Coprimality of the two binary quadratics is exactly
the irreducibility filter: a shared homogeneous root yields a ruling
component, while coprime quadratics give a smooth graph over their first
coordinate line. A four-by-four homogeneous Sylvester resultant includes
the common root at infinity and every leading-degree drop.

For each finite source T-root r=delta u, the target root is represented by
u z1+(1-u)z0. This is defined at u=0 (target infinity) and u=1 (target zero),
and never vanishes at z=1. Distinct roots have profiles (1,5),(2,4),(3,3),
up to exchanging labels; repeated T must have the separate profile (6).

I constructed the binary coefficients afresh as finite binomial sums, not
by replaying the owner's expanded-polynomial coefficient extraction.
The resulting exact sparse ideals, saturated only by root distinction and
the binary resultant, equal

    15: (u-11v+5, 21v^2-21v+5),
    24: (u-42v^3+63v^2-42v+10,
             63v^4-126v^3+111v^2-48v+8),
    33: (u+v-1, 7v^4-14v^3+12v^2-5v+1).

All three are zero-dimensional, reduced, and disjoint from both the
saturated bad locus and u v(u-1)(v-1)=0. Thus zero and infinity are retained
before the exact ruling-factor filter, rather than omitted by a denominator.
The ordered counts are 2,4,4. The last identifies exchanged root labels,
leaving two contact quadratics. For type 24, h=s-1 separates the four
solutions: v=1/2+h/(21h^2+1), and its denominator cannot vanish on
63h^4-30h^2-1=0. Hence the list has exactly eight source T quadratics.

The repeated-root sparse ideal is exactly (u(u-1)); both surviving endpoints
have zero binary resultant, and saturation by that resultant is the unit
ideal. No irreducible cubic has a repeated-root T in this contact setting.
This excludes repeated roots of T only; it does not remove a repeated
cubic component of the residual divisor.

The independently verified invariant equations are

    15: h^2=12/7, p=8/21+h/2;
    24: 63h^4-30h^2-1=0, p=5/12+h/2-h^2/4;
    33: h=0, 7p^2-5p+1=0,

with s=1+h and p=uv. These necessary equations retain all algebraic branches.

### Actual coefficient matching closes the classification

The full primitive factor formulas, all coefficient equations and the six pair contradictions are proved below. They retain coincident factors and both signs of every algebraic branch. They contradict each possible pair on Jbar!=0. On Jbar=0 the separate entire-line all-power argument closes the no-mate theorem without asserting failure of SUP.

<a id="2-nonendpoint-cubic-contact-symbolics"></a>

## Actual primitive Segre factors and complete matching equations

### 1. Actual restriction and complete cubic-divisor equations

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

### 2. Actual linear/quadratic factorization on the class (2,1) image

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

### 3. Degree-seven contact and the exact quartic excess factor

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

<a id="2026-10-13-session-nonendpoint-cubic-pair-coefficient-independent-subaudit"></a>

## Exact coefficient reconstruction and the six pair contradictions

### 2. Direct reconstruction from the actual residual polynomial

To avoid the distinct uses of B and J in older notes, use

    B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a,
    beta=ad-bg, A=G+Jbar.

Then

    b=a+B, g=a+3B+G, d=a+4B+2G+Jbar,
    beta=a*A-3B^2-B*G.

On the cubic-pair hyperplane `A=-3delta^2`, the actual F is

    F=-3delta^2*t^2+(C*r+E)*t+P2*r^2+L*r+N,
    C=(-6B-G)*delta-3delta^3+3delta^2,
    E=-3a*delta^2-3B^2-B*G+delta^4,
    P2=-3B^2-B*G-3B*delta^2+3delta^3,
    L=(-3a+B)*delta^3-delta^4,
    N=a*delta^4.

Let `S=s1+s2`, `Sprod=s1*s2`, `P=p1+p2`,
`Pprod=p1*p2`, `Cross=s1*p2+s2*p1`, and `x=B/delta^2`.
The product with the fixed leading coefficient expands as

    -3delta^2*(t+delta*s1*r-delta^2*p1)
               *(t+delta*s2*r-delta^2*p2)
      =-3delta^2*t^2-3delta^3*S*r*t+3delta^4*P*t
        -3delta^4*Sprod*r^2+3delta^5*Cross*r-3delta^6*Pprod.

The constant and rt comparisons give exactly

    a=-3delta^2*Pprod,
    G=3delta^2*(S-1)-6x*delta^2+3delta.

After these substitutions define the following polynomials, with no
inverse parameter in their definitions:

    Q2=delta*(Sprod+x^2-x*S)-x+1,
    Q0=delta*(x-Sprod+1/3-P+3Pprod)-1,
    Q1=delta*(x+9Pprod-3Cross)-1.

The full residual difference is the literal identity

    F-(-3delta^2*factor1*factor2)
       =3delta^3*Q2*r^2+3delta^3*(Q0+Q2)*t+delta^4*Q1*r.

This verifies all coefficients, including the absent r-cubed term.
Because `delta!=0`, factorization is equivalent to `Q2=Q0=Q1=0`
after the first two comparisons. Their subtraction gives the identity

    Q1-Q0=delta*(Sprod-3Cross+P+6Pprod-1/3).

Thus the owner's modulus-free PAIR equation is necessary:

    Epair=Sprod-3Cross+P+6Pprod-1/3=0.                 (PAIR)

The same three coefficient equations give both displayed expressions
for `1/delta` and the owner's r-squared relation. Only delta is divided
by. The reconstruction applies without change to identical factors.

The unused additional equation in the companion is also correct.
Set `zeta=x-Sprod+1/3-P+3Pprod`. Both

    x^2-x*(S-1)-x*zeta+3Pprod+1/3-P,
    x^2-x*S+(1-x)*zeta+Sprod

are identically

    x*(2/3-S+Sprod+P-3Pprod)+1/3-P+3Pprod.

This coefficient must be retained for sufficiency; PAIR alone is only
necessary. The exclusion below only needs that necessary equation to
fail. We impose no inverse on the coefficient of x in the extra equation.

The equivalent inverse-separation expression is zeta=1/delta with

    zeta=x+9Pprod-3Cross=x-Sprod+1/3-P+3Pprod.

Together with PAIR, the retained extra coefficient equation, the a,G formulas and delta!=0, these are complete matching conditions. The coefficient of x in the extra equation is never divided out.

### 3. The supplied root rows give the stated invariant equations

I reconstructed the `u,v` to `s,p,h` conversion directly, where
`s=u+v`, `p=u*v`, `h=s-1`.

For type 15, reduction by `21v^2-21v+5=0` with `u=11v-5` gives

    7h^2-12=0, p=s/2-5/42.

For type 24, reduction by
`63v^4-126v^3+111v^2-48v+8=0` with
`u=42v^3-63v^2+42v-10` gives

    63h^4-30h^2-1=0, p=5/12+h/2-h^2/4.

For type 33, `u=1-v` gives `s=1`; its supplied v quartic is
exactly `7p^2-5p+1=0` after substituting `p=v(1-v)`.

These are necessary consequences of the supplied rows, rather than a
claim here that the rows exhaust homogeneous contact profiles. Exhaustion,
endpoint treatment, ruling-factor removal and the geometric support
bridge belong to the parent's independent audit.

### 4. Complete six-pair contradictions, including diagonal pairs

For each type the polynomial PAIR is symmetric in the two cubics. The
three types therefore have exactly six unordered pairings. Direct
substitution produces the following identities, before using their field
equations.

| Pair | Exact expression for Epair |
| --- | --- |
| 15 / 15 | `2/147-h1*h2/2` |
| 15 / 24 | `(1-3h2^2-21h1*h2)/42` |
| 15 / 33 | `(2/7)*(q-1/3)` |
| 24 / 24 | `((1-3h1^2)*(1-3h2^2)-12h1*h2)/24` |
| 24 / 33 | `(3h1^2-1)*(1-3q)/6` |
| 33 / 33 | `(2/3)*(1-3p)*(1-3q)` |

For **15 / 15**, `h1*h2=12/7` or `-12/7`; Epair equals
`-124/147` or `128/147`. Both are nonzero.

For **15 / 33**, Epair zero would require `q=1/3`, but
`7q^2-5q+1` has value `1/9` there.

For **24 / 33**, put `e=h1^2`. The field polynomial
`63e^2-30e-1` has value `-4` at `e=1/3`, and the type-33
polynomial has value `1/9` at `q=1/3`. Neither factor can vanish.

For **33 / 33**, neither p nor q is `1/3`, by the same field
polynomial evaluation. The displayed product is nonzero.

For **15 / 24**, put `e=h2^2`. Epair zero gives
`1-3e=21h1*h2`; squaring and using `h1^2=12/7` yields
`9e^2-762e+1=0`. Subtract seven times this equation from
`63e^2-30e-1=0` to obtain `5304e-8=0`, so `e=1/663`.
The latter field polynomial has the nonzero value
`-459396/439569` there.

For **24 / 24**, put `ei=hi^2`. If e1,e2 are distinct roots of
`63e^2-30e-1`, their sum is `10/21` and product is `-1/63`.
Then `(1-3e1)*(1-3e2)=-4/7`. Equality to `12h1*h2`
would imply the false rational identity `16/49=-16/7` after
squaring. If `e1=e2=e`, the product `h1*h2` is e or -e.
In the first case Epair zero gives `9e^2-18e+1=0`;
comparison with the field polynomial gives `e=1/12`, where the
field polynomial is `-49/16`. In the second case Epair zero
gives `(3e+1)^2=0`; then `e=-1/3`, where the field
polynomial is 16. Every value is retained, including both signs of h.

No part of this reasoning divides by `h1-h2`, `e1-e2`, or a
cubic-factor difference. A repeated cubic is an explicit diagonal pair
within the 15 / 15, 24 / 24 or 33 / 33 case and is excluded.


<a id="2026-10-13-session-nonendpoint-homogeneous-gcd-rank-and-cover-independent-audit"></a>

## Full homogeneous gcd rank and parameter cover

### 1. Correct normalization and special zero cubics

Work over an algebraically closed field of characteristic zero, with
`delta != 0`. Put `z=r/delta`. The correctly scaled polynomials are

    P(delta*z)/delta^3 = (g-3b+2a)z^3
      + [6(b-a)+delta^2-3delta]z^2
      + [6a-3b+2delta]z - 2a,
    J(delta*z)/delta^3 = (2d-3g+b)z^3
      + [3(g-b)+5delta^2-3delta]z^2
      + [3b+delta-delta^2]z - b.

Write these degree-three homogenizations as `P,J` again. The coordinate
change is invertible, so it preserves homogeneous gcd degree, including
infinity and repeated roots. In particular the normalized coefficient
`2delta`, and the terms `delta^2-3delta` and `5delta^2-3delta`, must not
be replaced by their delta-one values.

The exact zero-polynomial strata are

    P=0: delta=-1, a=0, b=-2/3, g=-2, d arbitrary;
    J=0: delta= 1, b=0, g=-2/3, d=-1, a arbitrary.

For the first, the other cubic is

    J=(2d+16/3)z^3+4z^2-4z+2/3,

which is nonzero. For the second, it is

    P=(2a-2/3)z^3+(-6a-2)z^2+(6a+2)z-2a,

which is nonzero. These are the homogeneous-gcd-degree-three strata,
even when the nonzero affine polynomial has degree less than three.
The two cubics are never both identically zero.

An early message derivation by this auditor lost a delta factor during
scaling and consequently gave the wrong sign for the zero-P stratum.
Those substitutions were explicitly discarded. The formulas here are
checked directly against the literal original polynomials.

### 2. Exact homogeneous Bezout and syzygy criteria

Let

    P(u,v)=p0*u^3+p1*u^2*v+p2*u*v^2+p3*v^3,
    J(u,v)=j0*u^3+j1*u^2*v+j2*u*v^2+j3*v^3,
    wij=pi*jj-pj*ji, i<j.

The intrinsic cubic Bezout matrix is

    B = [ w01  w02       w03 ]
        [ w02  w03+w12   w13 ]
        [ w03  w13       w23 ].

It satisfies the literal identity

    P(u,v)J(s,t)-J(u,v)P(s,t)
      = (ut-vs)*(u^2,uv,v^2)*B*(s^2,st,t^2)^transpose.

If `h=degree(gcd_homogeneous(P,J))`, then

    rank(B)=3-h.

Here is a proof that also covers multiple roots and infinity. Factor
`P=H*A`, `J=H*C`, with `degree H=h` and coprime homogeneous residual
forms of degree `m=3-h`. The Bezout biform factors as the product
`H(u,v)H(s,t)` and the residual Bezout biform. Multiplication by H is
injective, so the coefficient matrix has the form `T*Bm*T^transpose`,
with T of full column rank. For `m>0`, change projective coordinates
so A has affine degree m. In `k[x]/(A)`, the residual Bezout biform
equals multiplication by the unit C times the divided difference of A.
The latter matrix is anti-triangular with nonzero antidiagonal, hence
invertible. Thus Bm is invertible and B has rank m. For `m=0`, the
biform is zero. If one cubic is zero, the other is the homogeneous
gcd and this last case applies.

Therefore `h>=2` is exactly the following six equations:

    w01*(w03+w12)-w02^2 = 0,
    w01*w13-w02*w03 = 0,
    w01*w23-w03^2 = 0,
    w02*w13-w03*(w03+w12) = 0,
    w02*w23-w03*w13 = 0,
    (w03+w12)*w23-w13^2 = 0.

These are all the two-by-two minors of the symmetric matrix. The
third and fourth coincide on the coefficient-pair locus, by the
Plucker identity `w01*w23-w02*w13+w03*w12=0`. Exact degree two also
requires `B != 0`; exact degree three requires `B=0`, equivalently all
six wij vanish. No affine-leading-coefficient nonvanishing is assumed.

The universal degree-one syzygy map has the five-by-four matrix

    S = [ p0  0   j0  0  ]
        [ p1  p0  j1  j0 ]
        [ p2  p1  j2  j1 ]
        [ p3  p2  j3  j2 ]
        [ 0   p3  0   j3 ].

UFD divisibility of the coprime residual pair gives

    dimension(kernel S)=max(h-1,0),
    rank(S)=4 if h<=1; 3 if h=2; 2 if h=3.

For h=2 the kernel is the unique scalar line generated by
`(J/H,-P/H)`. These are independent linear forms. Conversely independent
linear cofactors after dividing by a quadratic force h=2. The matrix S
is naturally five-by-four; the separate actual coefficient matrix in
section 3 is four-by-four and has a different purpose.

If `H=h0*u^2+h1*u*v+h2*v^2` and
`P=H*(l0*u+l1*v)`, `J=H*(m0*u+m1*v)`, then

    B=(l0*m1-l1*m0)*(h0,h1,h2)^transpose*(h0,h1,h2).

Consequently any nonzero column of a rank-one B recovers H projectively.
For example `P=uv^2,J=v^3` retains the double common root at infinity:
its Bezout matrix is diagonal with entries `(0,0,1)`.

### 3. Finite monic quadratic common factor

Let `H=z^2+v*z+w`, and write

    P=(A*z+B)*H, J=(C*z+D)*H.

The actual parameters are recovered without any additional division by
cofactor coefficients:

    a=-B*w/2, b=-D*w,
    g=A+3b-2a, d=(C+3g-b)/2.

The four remaining actual coefficient relations are exactly

    M*(A,B,C,D)^transpose
      = delta*(2,delta-3,1-delta,5delta-3)^transpose,

where

    M = [ w   v+3w    0   -3w  ]
        [ v   1-3w    0    6w  ]
        [ 0   0       w    v+3w]
        [-3  -3w      v    1+6w].

Direct expansion gives

    det(M)=(v^2-4w)*K,
    K=v^2+2w+6vw+6w^2.

Thus outside these two factors, M is invertible and gives the complete
unique coefficient pair for each `(delta,v,w)`. Exact gcd degree two
requires the additional open condition `A*D-B*C != 0`.

### 3a. The exceptional K locus has no solutions

If `K=0,w=0`, then `v=0`, and the first equation is `0=2delta`,
impossible. If `w!=0`, put `t=v/w` and `S=t^2+6t+6`. Then

    S != 0, w=-2/S, v=-2t/S.

The augmented four-by-four minor using columns `(A,C,D,rhs)` is

    -24*delta*(t+2)/S^2.

It is nonzero except `t=-2`. At that last value `H=(z-1)^2`.
The second coefficient equation is minus twice the first, requiring
`delta=-1`. The fourth is minus three times the first minus twice the
third, requiring `delta=-5/3`. These cannot hold simultaneously. Hence
the entire K locus is inconsistent, including its intersections with
the repeated-factor locus.

### 3b. Repeated finite common factor

For `H=(z-rho)^2`, so `v=-2rho,w=rho^2`, the case `rho=0` is already
impossible by the first equation, and `rho=1` is impossible by section 3a.
For `rho!=0,1`, M has rank three: its first three rows and columns have
minor `-3*rho^4*(rho-1)^2`. A left-kernel vector is

    (-(2rho+1),-rho*(rho+2),2rho,rho^2).

Its pairing with the actual right-hand side is

    2delta*[2delta*rho*(rho-1)+2rho-1].

Therefore the necessary and sufficient compatibility condition is

    2delta*rho*(rho-1)+2rho-1=0.

When this holds there is one free cofactor coefficient. Again retain
`A*D-B*C != 0` for exactly h=2. The requirement `delta!=0` also removes
`rho=1/2`; no additional unstated root condition is introduced.

### 4. Common quadratic containing infinity

A common factor with infinity once is `H=v*(u-rho*v)`. Then the
affine cubics have leading coefficients zero, so

    g=3b-2a, d=4b-3a.

The remaining common-root equations in a,b are

    [ -6rho^2+6rho-2   6rho^2-3rho   ] [a]
    [ -6rho^2         6rho^2+3rho-1 ] [b]

    = -delta*[ (delta-3)rho^2+2rho,
               (5delta-3)rho^2+(1-delta)rho ]^transpose.

The determinant is `2*T`, where `T=6rho^2-6rho+1`. For every rho,
including T=0, a particular solution is

    a0=delta*rho*(2delta*rho+1),
    b0=delta*rho*(2delta*rho-delta+1).

For `T!=0` this is the unique solution. For `T=0`, the coefficient
matrix has rank one and the compatibility is automatic. All solutions
are `(a,b)=(a0,b0)+eta*(m12,-m11)`, where m11,m12 are its first-row
entries. They cannot both vanish when T=0. Recover the linear
cofactors of P,J and retain their nonzero determinant for exactly h=2.

Double infinity would require both affine degrees at most one. After
the leading cubic coefficients vanish, the quadratic coefficients
differ by `4delta^2`, so they cannot both vanish. This case is impossible.

The finite monic cover, infinity-once cover, and impossible double
infinity case exhaust all projective quadratic factors, including
repeated factors. No actual projection admissibility is asserted.

### 5. Complete proportional locus, including the zero cubics

For `P!=0`, homogeneous gcd degree three is exactly `J=kappa*P` for
a scalar kappa. Comparing the literal corrected coefficients gives

    b=2kappa*a,
    6kappa^2*a=delta*(delta+2kappa-1),
    g=4kappa^2*a+(kappa-5)*delta^2/3+(1-kappa)*delta,
    d=(kappa+3)*g/2-3kappa^2*a,
    delta!=0.

These conditions are necessary and sufficient: after substituting b,g,d,
the literal difference is

    J-kappa*P = -[delta*(delta+2kappa-1)-6kappa^2*a]*z.

For `kappa!=0` this expresses a rationally in `(delta,kappa)`. For
`kappa=0` it gives `delta=1`, a free, and precisely the zero-J stratum.
The separate zero-P stratum in section 1 supplies the missing
projective-ratio chart. Thus no zero polynomial or proportional pair
is silently removed from the full h>=2 classification.


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_binary_contact.m2](../validation/2026-10-13-cubic-pair-full-independent-audit/verify_binary_contact.m2), [verify_session_cubic_pair_coefficient_subaudit_2026_10_13.m2](../computations/verify_session_cubic_pair_coefficient_subaudit_2026_10_13.m2), [verify_session_nonendpoint_homogeneous_gcd_rank_2026_10_13.m2](../computations/verify_session_nonendpoint_homogeneous_gcd_rank_2026_10_13.m2), [verify_session_nonendpoint_h2_cover_audit_2026_10_13.m2](../computations/verify_session_nonendpoint_h2_cover_audit_2026_10_13.m2). No inherited computation was rerun for this consolidation.

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
