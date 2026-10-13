# Cubic residual pairs: independent coefficient and six-pair algebra subaudit

Date: 2026-10-13. Auditor: `pair_coefficient_audit`, child of
`oct12_type1_two_family_audit`.

Status: **INDEPENDENT ALGEBRA SUBAUDIT PASS.** The actual residual
coefficient comparison and all six invariant pair contradictions are
reconstructed below. This is conditional on the parent's separate audit
that the geometric support requirement and complete homogeneous contact
classification give the three supplied invariant types. This note does
not independently establish that geometric/classification bridge and does
not by itself accept an entire quintic-lane theorem.

Work over an algebraically closed field of characteristic zero. Retain
`delta!=0`. No coefficient equation below divides by a difference of
cubic factors, a difference of field roots, or a minor. In particular,
coinciding cubic factors remain in scope.

## 1. Exact audited inputs and scope

The relevant portion of the owner's
[cubic-pair note](2026-10-12-session-nonendpoint-cubic-pair-contact-reduction.md)
is Sections 4–6. Its digest at this audit is

    7276aa227795695682684f4e1468a45d07c4513eb5a8465190966274d4464f2a

The complete actual coefficients and the extra matching equation are in
Sections 1 and 4 of the
[cubic-contact companion](2026-10-12-session-nonendpoint-cubic-contact-symbolics.md),
digest

    0b85a793349a0a35c6b9f1b3ea0a677d90d2076d14f2f28257ab5b86c1b1fb4c

The actual ambient residual polynomial is taken from Section 1 of the
[residual-factor note](2026-10-12-session-nonendpoint-residual-factor-and-genus-reduction.md),
digest

    d0efa3d74b5b8b59f9f5790b7323404765793905e3553b4e84f5ef865597fc44

No input, owner, canonical, frozen record, or Git state was modified.
Input snapshots, input digest bindings, all three new checker execution
versions, and their raw streams are retained in the
[new validation directory](../validation/2026-10-13-cubic-pair-coefficient-subaudit/input-bindings.json).

## 2. Direct reconstruction from the actual residual polynomial

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

## 3. The supplied root rows give the stated invariant equations

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

## 4. Complete six-pair contradictions, including diagonal pairs

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

## 5. New exact supporting execution and preserved failures

The fresh independently written
[checker](../computations/verify_session_cubic_pair_coefficient_subaudit_2026_10_13.m2)
has SHA-256

    a067b9847fc4150a302aa229e6a626ecf78480a66cebfd776da525e347477e7a

The final
[execution record](../validation/2026-10-13-cubic-pair-coefficient-subaudit/attempt-03/execution-record.json)
records exit zero, **38 supporting PASS conditions**, and empty stderr.
The stdout digest is

    b7ffd2871d4f666ae094d73579c5c29a4660938f6b6e8114a616e96e8e0832fb

The terminal `FINAL PASS 38` summary is additional to, and not counted
among, the 38 supporting conditions. The checks verify ten residual
identities, three additional matching identities, six invariant
transformations, six exact pairing expressions, six unit ideals, three
explicit diagonal unit ideals, and four arithmetic contradiction values.
The six unit ideals are in a rational polynomial ring with the original
type field equations and Epair. Thus they independently confirm the
written contradictions over every algebraically closed field extension
of QQ. They are not finite-field samples or a generic-rank calculation.
The explicit algebraic proof in Section 4 is the certificate independent
of the ideal-equality interface; this source does not print literal
Bézout multipliers for its unit ideals.

There are three captured source versions in this new checker lineage:

| Version | Outcome |
| --- | --- |
| attempt-01 | Setup failure assigning the protected M2 identifier `check`; zero supporting conditions. |
| attempt-02 | All 29 initial conditions passed, exit zero and empty stderr. It has the full coefficient and six-pair checks but predates the extra equation and invariant-conversion checks. |
| attempt-03 | All 38 final conditions passed, exit zero and empty stderr. |

The first setup failure is retained with its exact source and raw
streams. No mathematical assertion failed in this lineage. Before the
second run, protected/common identifiers were replaced by task-specific
names and residual coefficients were checked directly, avoiding the
known multivariate coefficient-extraction interface pitfall. This note
is one independent algebra subaudit, not three independent audits.

## 6. Conditional conclusion and remaining obligations

The coefficient-comparison and six-pair algebra in Sections 4–6 of the
owner note are correct. Every pair drawn from the three supplied contact
types fails the necessary actual PAIR condition, including doubled
cubic factors. Subject to the parent's independent verification that
all SUP cubic images lie among those types, this establishes the claimed
cubic-pair exclusion for all mate degrees in this fixed characteristic-zero
normalization family.

This narrow subaudit does not assert closure of the integral residual,
other quintic carriers, higher carriers, unrestricted C0, or the universal
projective-curve STCI problem. All remain outside its scope.
