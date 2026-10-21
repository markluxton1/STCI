# Conditional (2,12;6,16;2): exact two-node torsion and a diagonal exclusion

Date: 2026-10-20. Author: `singular_gluing` continuation worker.
Status: **new proposal; exact reduction and scoped exclusion**. No
canonical record or inherited proof is changed. The factor-matrix and
torsion-scheme calculation below was independently reconstructed by
`two_node_torsion_audit`, with an additional factorization check by its
`factor_check` worker. The diagonal ambient exclusion, its exact
contraction ideal, its source substitution in the actual chart,
and its arithmetic were independently reviewed by the same auditor
and its `diagonal_arithmetic` worker, with verdict PASS.

## Scope and existing interface

Retain precisely the characteristic-zero curve, actual-CI, full generic
coprime `(2,12)` initial ideal and saturated movement-two relation
hypotheses in
[the singular-root bridge note](2026-10-20-conditional-2-12-singular-gluing.md).
The current task investigates the necessary structured incidence, not
unrestricted homogeneous equations. The inherited universal first
incidence and complete second test are the promoted
[STCI-R-0007](../results/quadratic_root_obstruction_model.md), and the
finite singular bridge remains a reviewed proposal in the linked note.

The source generator for these new calculations is
`../computations/conditional_2_12_singular_continuation_2026_10_20.py`.
It imports the inherited universal equation constructor without its
artifact-writing footer and substitutes into the existing exact
operators. It does not rerun an inherited proof or seed certificate.

## 1. Full two-node factors in the original coordinates

Write the two actual `(1,1)` factors as

    li=(Ai+Ci*z)u+(Bi+Di*z)v,       i=1,2,
    Delta_i=Ai*Di-Bi*Ci.

No change of base or direction ruling is performed. In homogeneous
base coordinates `z=[z0:z1]`, put

    Mi=[[-Bi,-Di],[Ai,Ci]].

The component `Di=(li)` is the graph `[u:v]=[Mi*z]`, and it is a
smooth `(1,1)` component exactly when `Delta_i !=0`. Set

    N=adj(M1)*M2,
    tau=tr(N)=A1*D2+A2*D1-B1*C2-B2*C1,
    delta=det(N)=Delta_1*Delta_2.

The nodes are the eigenlines of `N`. More precisely
`det(M1*z,M2*z)=det(z,N*z)`, with binary discriminant

    D=tau^2-4*delta.

Thus the full two-node open, with neither node discarded, is

    delta*D != 0.                                                (1)

This parameterization covers all ordered pairs of smooth `(1,1)`
components with two transverse intersections, up to the independent
nonzero scales of the two factors. The finite swap of the factors
does not change any condition below.

## 2. Exact torsion scheme of the actual node identifications

For `L=O_Z(1,-1)`, the fiber at `(z,w)` is
`Hom(ell_z,ell_w)`. The matrix `Mi` supplies a nowhere-zero section
`sigma_i` of `L|Di`. At a node represented by an eigenvector `v_j`,

    M2*v_j=mu_j*M1*v_j,
    g_j=sigma_1(z_j)/sigma_2(z_j)=mu_j^(-1).

Consequently the actual two-node gluing modulus is

    lambda=g_1/g_2=mu_2/mu_1,

up to inversion. Rescaling either factor changes both eigenvalues
together and leaves this ratio unchanged. This proves directly in
the original coefficients that

    L^12=O_Z  iff  N^12 is scalar.                               (2)

It does not replace the original coefficients in the ambient first
or second operator by an arbitrary ruling normal form.

Cayley-Hamilton gives the exact equation

    Q12=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)
              *((tau^2-2*delta)^2-3*delta^2)=0.                  (3)

The polynomial has degree twenty-two in the eight factor
coefficients. Equivalently,

    Q12=tau^11-10*delta*tau^9+36*delta^2*tau^7
        -56*delta^3*tau^5+35*delta^4*tau^3-6*delta^5*tau.

This is an exact scheme equation on (1), not just a closed-point
test. Indeed `N^12=Q12*N-delta*U10*I`. If
`N=[[a,b],[c,d]]`, its scalar-matrix ideal is

    Q12*(b,c,a-d).

But `D=(a-d)^2+4*b*c` is invertible on (1), so
`(b,c,a-d)` is the unit ideal and the scalar-matrix ideal is exactly
`(Q12)`. Thus the full two-node torsion parameter scheme is

    Spec k[Ai,Bi,Ci,Di]_[delta*(tau^2-4delta)] / (Q12).           (4)

This includes orders two, three, four, six and twelve, as required
by divisibility by twelve. The factor `tau` must occur only once:
replacing it by `tau^2` gives the correct geometric support but
doubles the involution stratum. At `tau=0`, the quotient
`Q12/tau=-6*delta^5` is a unit. The independent audit specifically
caught and corrected this possible scheme error.

The exact original-coordinate first/second incidence with (3) and
open (1) is exported to
`../computations/conditional_2_12_singular_continuation_2026_10_20_two_node.m2`.
This replaces a 143-component torsion-kernel witness by one
polynomial on this stratum. It is still a low-order necessary
incidence; the actual global sextic cubic matching condition and
all subsequent certificates remain additional requirements.

## 3. A proper diagonal slice is exactly excluded already at first order

Consider only

    l1=t1*u+z*v,          l2=t2*u+z*v,
    t1*t2*(t1-t2) !=0.                                         (5)

This is a proper two-parameter slice in the original ambient
coordinates. It is not a normal form for every two-node root under
automorphisms of `C0`. Separate arbitrary PGL2 transformations of
the two rulings would change the ambient obstruction operator and
are not used.

Substituting

    a0=t1*t2, b1=t1+t2, c2=1,
    all other root coefficients zero

in the universal sixteen first equations and eliminating the twelve
first-unit coefficients gives the exact ideal with generators

    P(t1)+P(t2),             (t1-t2)*P(t2),
    P(T)=3*T^3-10*T^2+20*T-24
        =(T-2)*(3*T^2-4*T+12).                                (6)

The complete QQ elimination in
`../computations/conditional_2_12_singular_continuation_2026_10_20_diagonal.m2`
returned these two generators. Thus on (5), first compatibility
forces `P(t1)=P(t2)=0` with distinct roots.

There is also an exact elimination proof without relying on a
Groebner-basis transcript. Put `S=t1+t2`, `T=t1*t2`. In the inherited
first-unit variable ordering the equations force

    h9=-7/2-3*S/8,
    h2=(3*S^2-10*S-6*T)/8.

Rows one and six, using zero-based row indices, then reduce to
`-C/8,-A/8`, where

    A=P(t1)+P(t2),
    C=t2*P(t1)+t1*P(t2).

All other first-unit variables may be set to zero; direct
substitution makes every first equation vanish when `A=C=0`.
Consequently their exact contraction is
`(A,C)=(A,(t1-t2)*P(t2))`, with no radical taken. On (5) this is
`(P(t1),P(t2))`, consisting of the six reduced ordered pairs of
distinct roots. The first unit is unique on that open.

There is a short exact arithmetic exclusion. If one selected root
is `2` and the other is a root `r` of `3*T^2-4*T+12`, then

    t1/t2+t2/t1 = r/2+2/r = 2/3.

If the two selected roots are the two roots of that quadratic, their
sum is `4/3` and their product is `4`, whence

    t1/t2+t2/t1 = ((4/3)^2-8)/4 = -14/9.

Neither rational number is an algebraic integer. A root of unity
and its inverse have algebraic-integer sum. Therefore no ratio of
two distinct roots in (6) is any root of unity, and in particular
it cannot satisfy the required twelfth-power condition. This
excludes every point of the diagonal slice (5), before the second
ambient obstruction or global cubic matching is considered.

For a direct rational nonvanishing certificate specific to twelve,
put `x=(t1+t2)^2/(t1*t2)`. The two cases give `x=8/3` and `x=4/9`.
After dividing (3) by the nonzero factor
`(t1+t2)*(t1*t2)^5`, its values are respectively

    (x-1)*(x-2)*(x-3)*((x-2)^2-3)
        =230/243,                  x=8/3,
        =75670/59049,               x=4/9.

Both are nonzero in every characteristic-zero field. This supplies
an exact torsion nonvanishing check without choosing complex
embeddings or approximating eigenvalue ratios.

For an independent exact computation check, the same M2 input adds

    sum_(j=0..11) t1^(11-j)*t2^j,
    iv*t1*t2*(t1-t2)-1

to the sixteen first equations. Its QQ Groebner basis is `{1}`.
Adding the complete twenty-five second equations again gives `{1}`.
The latter repetition is recorded only as an output already produced
by the same script; the first-order argument is sufficient.

The independent auditor expanded the accepted actual transition
through normal degree three with a separate stdlib rational-Laurent
implementation and compared all sixteen substituted first equations;
every entry matched exactly. Its continuation-ready source is
`../computations/conditional_2_12_singular_continuation_2026_10_20_independent_diagonal_audit.py`.
The independent output was
`INDEPENDENT_DIRECT_TRANSITION_FIRST_EXPORT_MATCH: True`.

## 4. Retained coverage and first unresolved global condition

The diagonal exclusion does not eliminate the full two-node scheme
(4), nor the integral nodal or smooth-root loci. Cuspidal and tangent
strata are excluded by the reviewed torsion-free Picard argument
in the previous note. On retained roots, symbol membership and
universal root compatibility still have to be compared with the
actual jets of a global sextic. Their first matching condition is

    [F3-alpha*G0] mod(f)=0,
    F=F0(alpha*f)+lambda*q^3,

with actual `k` coefficients and with every zero of `alpha`
retained. The next abstract Cartier obstruction at `E3` is a
separate condition. Nothing here asserts a nonempty low-order
incidence, a global pair, a full degree-twelve standard basis, or
the global gcd/Bezout support certificate.

The general-factor first-incidence/torsion computation, if attempted,
must report its exact chart, resources and returned ideal. An
interrupted computation is neither an emptiness nor a survival
certificate. This note preserves the full original-coordinate
parameter scheme (4) regardless of the outcome on any individual
computational chart.
