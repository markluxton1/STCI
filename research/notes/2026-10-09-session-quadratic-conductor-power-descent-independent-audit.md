# Independent audit of exact quadratic-conductor power descent

Date: 2026-10-09. Author: `quadratic_torsion_exact_audit`, for
`quadratic_conductor_power_descent`.

Status: **PROVED HERE, independent audit accepted under the stated
hypotheses.** This audit checks the algebraic criterion in
`2026-10-09-session-quadratic-conductor-power-descent.md`. It does not
assert that any of the remaining conductor data occurs on a del Pezzo
surface containing the fixed rational quartic. It gives no STCI
exclusion or bound on all possible mate degrees.

## 1. Hypotheses and verdict

Let k be algebraically closed of characteristic zero, let Gamma be an
actual plane conic, and put M=O_Gamma(1). Permit a smooth conic, two
distinct lines, and the full plane double line. Let

    E=p_*O_D=O_Gamma direct_sum M^(-1),
    w^2=delta,       sigma(w)=-w,
    q=m+w ell,

where m is a section of M^2, ell a section of M, and delta a section
of M^2. Assume multiplication by q is injective on O_D, with its
line-bundle twist understood. Define

    Cycl={((1+zeta)/(1-zeta))^2:
          zeta a root of unity in k, zeta != 1,-1}.

For a smooth conic or an entire double line, some positive power of q
is invariant if and only if either

    m ell=0 on the entire Gamma,

or

    m^2=rho delta ell^2 on the entire Gamma for some rho in Cycl.

For two distinct lines the same criterion is applied to each line,
with independent constants and a common multiple of their power
orders. The parent's criterion, including its nilpotent data and
its coefficient-rank consequences, is correct.

## 2. Independent necessity proof in the generic Artin rings

For an irreducible reduced conic or a reduced line, its generic ring
is a field K. For the plane double line its generic ring is
T=K[epsilon]/(epsilon^2). After trivializing M, the generic algebra
is the finite Artin algebra

    E_T=T[w]/(w^2-delta).

The nonzerodivisor q becomes a unit in E_T. Thus, if q^n is
invariant, the element t=sigma(q)/q is well defined and satisfies
t^n=1.

In a local Artin algebra over K, every solution of t^n=1 is an
actual constant root of unity in k, with no nilpotent correction.
Indeed T^n-1 is a product of distinct factors T-zeta. If the residue
of t is zeta, every other factor evaluated at t is a unit, forcing
t-zeta=0 in the Artin ring itself. The residue-field solution is in
k because k already contains all roots of T^n-1. This argument
works even when the residue field is a nontrivial extension of K.

The generic quadratic algebra has exactly the following cases.

| Residue of delta in K | Generic algebra and involution | Consequence |
| --- | --- | --- |
| Nonzero nonsquare | One local Artin factor with quadratic residue field; sigma preserves that factor | t=zeta and sigma(t)=t^(-1) force zeta=+1 or -1. Hence ell=0 or m=0, as exact identities in T. |
| Zero | One local Artin factor with residue field K; sigma induces the identity on that residue field | The residue of sigma(q)/q is 1, so t=1 exactly. Hence ell=0 in T. |
| Nonzero square | Two Artin factors interchanged by sigma | A chosen square root s of delta lifts across epsilon because 2s is a unit, so E_T=T x T. Then t=(zeta,zeta^(-1)). |

In the last row, zeta=+1 or -1 again yields ell=0 or m=0. For the
other roots of unity, one component of t gives

    (m-s ell)/(m+s ell)=zeta,
    m=((1+zeta)/(1-zeta)) s ell,

after possibly exchanging the factors. The denominators are units
because q is a unit in both factors. Squaring proves the required
identity m^2=rho delta ell^2 in the full T, not just its residue
field.

These generic identities extend to Gamma. The plane conic is a
pure Cohen--Macaulay curve, and the sections at issue belong to
invertible sheaves, whose maps into their generic total quotient
modules are injective. For the double line this can be seen directly
in k[a,b,epsilon]/(epsilon^2): a homogeneous section is
f(a,b)+epsilon g(a,b); vanishing in its generic Artin ring kills
both f and g. It does not follow merely from vanishing on the
reduced line. For two distinct lines, injection into the product of
their two generic fields proves that identities valid on both
lines hold on the whole reduced conic, including the node.

This proves necessity without assuming that D is reduced,
irreducible, smooth, or normal.

## 3. Independent sufficiency proof

Put v=w ell, so v^2=delta ell^2. The equality m ell=0 immediately
implies

    (m+v)^2=(m-v)^2,

because the difference is 4m w ell. Thus q^2 is invariant, retaining
all nilpotents.

For the other case, write lambda=(1+zeta)/(1-zeta), and let n be
the order of zeta. Then lambda is nonzero and lambda^2 is neither
zero nor one. Consider the polynomial

    P_n(m,v)=(m+v)^n-(m-v)^n.

It vanishes identically after either substitution m=lambda v or
m=-lambda v. The distinct linear factors m-lambda v and
m+lambda v consequently both divide P_n, and their product
m^2-lambda^2 v^2 divides P_n. Substituting the quadratic algebra
therefore gives P_n=0 whenever
m^2=lambda^2 delta ell^2. No cancellation of v, ell, or a
nilpotent is needed. Equivalently the parent's odd-binomial
coefficient polynomial S_n(m,d) is divisible by m^2-lambda^2 d.

For two reduced lines, choose a common multiple N of the two
orders, using order two for a product-zero case. The anti-invariant
coefficient of q^N vanishes on both lines and hence on their entire
union. No extra condition at their common point remains.

## 4. A nilpotent countershield

Scheme-level identities are essential. In the generic double-line
ring take

    T=K[epsilon]/(epsilon^2),
    E=T[w]/(w^2-(1+epsilon)),
    m=i, ell=1, q=i+w, i^2=-1.

The element q is a nonzerodivisor: in the two residual factors its
values are i+1 and i-1, both nonzero. On the reduced line one has
m^2=-delta, the cyclotomic constant for a fourth root of unity.
But this equality fails in the entire ring:

    m^2+delta=epsilon != 0,
    q^4-sigma(q)^4=8i w epsilon != 0.

Indeed no positive power is invariant. The generic ratio has a
nonzero nilpotent correction, whereas an Artin-ring root of unity
in characteristic zero has none. The exact criterion detects this
failure. Another elementary shield is m=1, ell=epsilon,
delta=1: the product m ell vanishes on the reduced line but

    q^n-sigma(q)^n=2n w epsilon != 0

for every positive n. Thus testing only reduced-support coefficients
would invalidate either branch of the criterion.

## 5. The finite coefficient conditions have the claimed scope

For a smooth conic or a double line, the exact criterion implies
linear dependence of m^2 and delta ell^2 in H^0(Gamma,M^4).
In a product-zero case, the generic q-unit condition ensures that
either m=0 or ell=0 in its single generic base ring; alternatively
apply the necessity argument to q^2. The resulting identity extends
to the entire Gamma. Thus one of the two sections is zero.

The common dimension of H^0(Gamma,M^4) is nine. For the smooth
conic, M corresponds to O_P1(2), giving binary octics. For the
double line, the full basis is

    a^4,a^3b,a^2b^2,ab^3,b^4,
    epsilon a^3,epsilon a^2b,epsilon ab^2,epsilon b^3.

Hence the 2 x 9 coefficient matrix has rank at most one; its
36 two-column minors are finite algebraic necessary conditions.
For two lines, each restriction is a binary quartic, yielding two
2 x 5 matrices and ten minors for each. Separate proportionality
constants must be allowed.

These rank conditions do not replace the exact cyclotomic
criterion. For example the double-line example m=epsilon, ell=1,
delta=1 has a rank-one pair (m^2,delta ell^2)=(0,1), while the
product m ell is nonzero and q has no invariant positive power.
The proportionality constant zero is outside Cycl. This distinction
prevents promotion of a finite necessary determinantal locus into
a sufficient descent condition.

## 6. The abstract unbounded-order example is valid

For Gamma=P1 embedded as a smooth conic, take M=O_P1(2), a section
s of M with two simple zeros, and delta=s^2. The finite quadratic
curve D is two copies of P1 meeting transversely at the two zeros
of s. It is connected, Gorenstein, has arithmetic genus one, and
has p_*O_D=O_Gamma direct_sum M^(-1). For

    lambda=(1+zeta)/(1-zeta),
    ell=s, m=lambda s^2,

the restrictions of q to the two components are
(lambda+1)s^2 and (lambda-1)s^2. Both constants are nonzero for
zeta != 1, and their ratio is zeta^(-1). Thus q is a
nonzerodivisor, and its smallest descended power is exactly the
order of zeta. These orders are unbounded. Its zeros have order
two on both components, and all its zero fibers have singleton
support.

This is an algebraic counterexample to a bound derived solely from
connectedness, arithmetic genus one, even component valuations,
and singleton fibers at the zeros. It is not an actual quartic
surface or an STCI construction. Those surface requirements
remain a separate geometric problem.

## 7. Acceptance boundary

The parent's exact criterion and finite necessary coefficient
conditions are accepted as an algebraic result. The proof needs
characteristic zero, the entire plane-conic schemes, and the
nonzerodivisor hypothesis on q. No use of only the reduced support
or of a global sign on exchanged components is justified. No
computation or literature claim is needed for this direct audit.

