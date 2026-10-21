# Conditional (2,12;6,16;2): forced-norm two-node reductions and exclusions

Date: 2026-10-21. Author: `singular_gluing` continuation worker.
Status: **new exact reductions and scoped exact exclusions; not
canonical promotion**. The cubic-defect identities, generic line/conic
decomposition and original-coordinate normalizations were independently
reviewed PASS by `two_node_torsion_audit` before that worker exhausted
its runtime allowance. The new completed line-component and boundary
CAS exclusions are submitted to `certificate_audit` for independent
review. An interrupted conic computation gives no exclusion or survival
certificate.

## 1. Literal actual-pair scope and dependencies

Retain characteristic zero, the fixed
`C0=[s^4:s^3t:st^3:t^4]`, an actual homogeneous pair of degrees
`6,16` with sole reduced support `C0`, FULL generic ordinary initial
ideal a coprime binary CI `(2,12)`, and the ACTUAL saturated first
relation of movement two. The promoted inputs are
[R-0010](../results/saturated_first_relation_normal_flatness.md),
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md),
and the universal first/second operators in
[R-0007](../results/quadratic_root_obstruction_model.md).
The finite singular-root bridge remains the reviewed proposal in
[the singular-root note](2026-10-20-conditional-2-12-singular-gluing.md).

This continuation additionally uses the independently reviewed
**actual-pair** norm identity from
[the geometric continuation](2026-10-20-conditional-2-12-geometric-continuation.md):
if `q1=u+zv/2`, `tau=f|_(q1=0)`, then `tau!=0` and

    alpha proportional tau(omega*z)*tau(omega^2*z), omega^3=1.

That identity retains collisions and endpoint ramification. It must
not be inferred on arbitrary low-order points just from the generic
orbit factorization. The sextic symbol image and its exact
one-dimensional kernel are the reviewed new computation in
[the symbol-map note](2026-10-20-conditional-2-12-symbol-map.md).

Only the two-node reducible root stratum is considered below. The
previously excluded cuspidal and tangent strata stay excluded;
integral nodal and smooth roots remain outside these reductions.

## 2. An exact cubic defect makes the forced-norm equations small

Write the two factors in the **original** accepted normal coordinates:

    li=(Ai+Ci*z)u+(Bi+Di*z)v,       Delta_i=Ai*Di-Bi*Ci !=0.

The two-node open additionally inverts
`T^2-4*Delta_1*Delta_2`, where

    T=A1*D2+A2*D1-B1*C2-B2*C1.

For a single factor suppress its index and put

    d=D-A/2, e=-C/2, tau_l=B+d*z+e*z^2,
    alpha_l=B^2-B*d*z+(d^2-B*e)z^2-d*e*z^3+e^2*z^4,
    kappa=(A+2D)*(d^2+BC/2),
    beta=-A*d^2+BC*(D-A).

Then `alpha_l=tau_l(omega*z)*tau_l(omega^2*z)` and the degree-one
normal symbol `p_l=alpha_l*l` differs from an ACTUAL global cubic
symbol by exactly

    p_l = c_l + (kappa/2)*z^3*v.                              (1)

The cubic-symbol image is spanned by

    q1, z*q1, z^3*q1, z^4*q1,
    v, -z^2*u+z^3*v/2, -2*z^5*u.

The coefficients of the last three generators in `c_l` are,
respectively,

    B^3,              beta,              -C^3/8.

The four `q1` coefficients, if `p_l=P(z)u+R(z)v`, are precisely
the coefficients of `P` at degrees `0,1,3,4`. Identity (1) follows
by direct multiplication, and does not assume first compatibility
of the single linear factor.

For `f=l1*l2` the forced multiplier is `alpha=alpha_1*alpha_2`.
Products of two actual cubic symbols lie in the global sextic
symbol image `V_(6,2)`. Applying its eleven exact quotient rows to
`p_1*p_2` leaves only zero-based rows `3,6,9`:

    row3 = -2*(kappa_1*B2^3+kappa_2*B1^3),
    row6 = -(kappa_1*beta_2+kappa_2*beta_1+kappa_1*kappa_2),
    row9 = (kappa_1*C2^3+kappa_2*C1^3)/4.                      (2)

Every other quotient row is identically zero. Thus setting the
three right sides of (2) to zero gives the **exact pullback
scheme** of forced-norm global symbol membership in the original
factor coefficients.

The independent verifier
`../computations/conditional_2_12_singular_continuation2_2026_10_21_independent_symbol_audit.py`
checks both identities (1) and all eleven rows with sparse rational
polynomial arithmetic. Its recorded output is
`FACTOR_CANONICAL_CUBIC_DEFECT_IDENTITIES: PASS` and
`ALL_ELEVEN_GLOBAL_SYMBOL_ROWS: PASS`, with row multipliers
`-2,-1,1/4` as above.

## 3. Mixed zero/nonzero defects are empty on the actual-pair open

Suppose `kappa_1=0` and `kappa_2` is invertible. Equations (2) give

    B1^3=C1^3=beta_1=0.

As raw ideals these do not say `B1=C1=0`; they make these two
coefficients nilpotent. Since `Delta_1` is invertible, `A1,D1`
are units. The equation `beta_1=0` makes `d1^2`, and hence `d1`,
nilpotent. All coefficients of

    tau_1=B1+d1*z-C1*z^2/2

are nilpotent. Consequently the required open `tau_1*tau_2 !=0`
is empty as a scheme. At closed points the only possible first
factor is the already excluded quadric direction `q1`. The
symmetric mixed stratum is identical. It is therefore enough to
retain both defects zero, or both defects nonzero.

## 4. Generic nonzero defects: a disjoint line/conic decomposition

On

    B1*B2*C1*C2*kappa_1*kappa_2 !=0,

independent factor scaling sets `B1=B2=1`. The actual
`C0`-preserving torus, after dividing each factor by its common
scale, acts by

    (A,B,C,D) -> (t*A,B,t^2*C,t*D).

Thus `C1=1` is permitted on a square-root finite etale cover,
with residual `mu2`. Equations (2) then give exactly

    C2=w, w^3=1,
    kappa_2=-kappa_1,
    beta_2-beta_1=kappa_1.                                  (3)

All three cube roots, including one, must be retained. This is a
gauge slice using only the actual torus; no arbitrary ruling PGL2
transformation is applied to the ambient obstruction operator.

Put

    x=d1, y=w*d2, a=A1+x,
    U1=2*x^2+1, U2=2*y^2+1.

Then

    kappa_1=a*U1,
    kappa_2=(w*A2+y)*U2,
    kappa+2*beta=2*d^3+3*BC*d.

Consequently (3) is equivalent as an ideal to

    kappa_1+kappa_2=0,
    (x-y)*(2*(x^2+x*y+y^2)+3)=0.                              (4)

Since both defects are units, `U2` is already a unit and one can
eliminate `A2` without losing any additional stratum:

    w*A2=-y-a*(2*x^2+1)/(2*y^2+1).                           (5)

The line and conic in (4) are disjoint **on this open**. Indeed
if `ell=x-y` and `Q=2*(x^2+x*y+y^2)+3`, then

    Q=3*U1-2*ell*(y+2*x).

Thus `(ell,Q)=(1)` after `U1` is inverted, and their product
equation is an exact disjoint scheme union. Before localization
their intersection lies at `x=y,2*x^2+1=0`, which belongs to
the separate zero-defect strata and has not been discarded.

The compact generic model, including eight remaining first
equations and all forty-eight actual global cubic matching
equations, is
`../computations/conditional_2_12_singular_continuation_2026_10_21.m2`.
It loaded successfully and reported the stated equation counts.
Loading is not an elimination result. A metadata-label correction
is recorded in section 9.

## 5. The entire generic line component is exactly excluded

On `y=x`, equations (5) give

    A1=a-x,           D1=(a+x)/2,
    A2=-w^2*(a+x),    D2=w^2*(x-a)/2.

Writing `J=(a^2-x^2-2)/2`, the trace/determinant of the actual
two-node gluing matrix are

    T=-w^2*(a^2+x^2)-1-w,
    delta=w*J^2.

Use the exact spectral equation from the previous continuation,

    Q12=T*(T^2-delta)*(T^2-2delta)*(T^2-3delta)
                    *((T^2-2delta)^2-3delta^2)=0.             (6)

The endpoint coefficients are `a2=w,c0=1`, so eight first-unit
variables can be eliminated by the triangular recurrences, with
no new denominator besides the already invertible `w`. Four
variables `h4,h5,h6,h7` remain.

For `w=1`, the root coefficients depend on `a` only through
`p=a^2`. Eliminating those four first-unit variables gives the
following four exact necessary polynomials in `p,x`:

    48p^3+1130px^2+292p^2+8400x^2+1072p-615,
    4x^4+2px^2-14x^2-2p+1,
    22px^3+8p^2x+60x^3-28px-15x,
    6p^2x^2-38px^2-22p^2-390x^2-49p+30.                      (7)

Here `T=-(p+x^2+2)`, `delta=((p-x^2-2)/2)^2`, and the precise
generic two-node open is

    p*(2*x^2+1)*(p-x^2-2)*(x^2+2) !=0.

The saturation of (7) plus (6) by this open is the unit ideal
over `QQ`. The calculation completed with return code zero in
0.407 seconds and maximum RSS 122,503,168 bytes. Its exact input,
log and run metadata have common stem
`../computations/conditional_2_12_singular_continuation_2026_10_21_line_component_w1`.

For a primitive cube root, use the exact number field
`QQ[w]/(w^2+w+1)` and keep `a,x`. The actual open is

    a*(2*x^2+1)*(a^2-x^2-2)*(2*a^2-3) !=0.

The same first-unit elimination followed by adding (6) and
saturating this open again returns the unit ideal. It completed
with return code zero in 1.242 seconds, maximum RSS 283,295,744
bytes; the common artifact stem ends in
`_line_component_primitive`. Both conjugate primitive roots are
covered by this number-field calculation.

Thus all three `w` branches of the generic line component are
excluded, before the complete second obstruction or global cubic
matching is needed. These are exact characteristic-zero
computations on specified coefficient schemes, not finite samples.

## 6. The full nonzero-defect B/C boundary is exactly excluded

With both defects units, `B1=0` forces `B2^3=0`. On closed points
both `B` coefficients vanish; the same statement holds for the
two `C` coefficients. If both `B` and both `C` vanish, the old
diagonal exclusion in
[the preceding continuation](2026-10-20-conditional-2-12-singular-continuation.md)
applies. The remaining `B=0` boundary has both `C_i` invertible.
Set `C1=C2=1` by factor scaling. Here `Delta_i=Ai*Di` and
`d_i, Ai+2Di` are units. Equations (2) give

    A2*d2^2+2*D1*d1^2=0,
    2*D2*d2^2+A1*d1^2=0.

Let `rho=d1/d2`. It follows that

    A2=-2*D1*rho^2,
    D2=-A1*rho^2/2,
    d2=rho^2*d1,
    rho^3=1.

After `C_i=1`, the actual torus sends `Ai,Di` to
`Ai/t,Di/t`, so set the unit `D1=1`. Rename `A1=t`, `rho=w`:

    A1=t, D1=1, A2=-2*w^2, D2=-w^2*t/2,
    B1=B2=0, C1=C2=1, w^3=1,
    t*(t^2-4) !=0.                                          (8)

The last open is exactly the nonzero-defect, finite two-component,
two-node open. The universal sixteen first equations are now
linear in twelve unit coefficients and polynomial in one parameter.
Their contraction is `(t-2)` for `w=1`, and `(1)` over
`QQ[w]/(w^2+w+1)` for primitive `w`. Thus (8) is already empty at
first compatibility. The two complete runs returned zero; their
artifact stems are

    ../computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_w1
    ../computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_primitive.

Their `.log` files also record the redundant first-plus-torsion
unit calculation. The first-order contraction alone proves the
exclusion on the open (8).

The `C=0` boundary is covered by the **actual** coordinate reversal
`x0<->x3,x1<->x2` preserving `C0`. Its first normal action in the
accepted balanced frame is

    (u,v) -> z^(-7)*(v/2,2u),
    (A,B,C,D) -> (2D,C/2,2B,A/2).

It exchanges the `B=0` and `C=0` boundaries, preserving `Delta`
and `kappa`. This is not an arbitrary ruling normalization.
Nilpotent structures in the unnormalized boundary equations
cannot hide a nonempty scheme with empty closed-point support;
all schemes here have finite type over the algebraically closed
field. Thus the closed-point cover and exact unit computations
exclude the entire nonzero-defect boundary scheme.

## 7. Precise retained two-node strata

After these exclusions, the nonzero-defect two-node root can only
lie on the generic **conic** component

    B1=B2=C1=1, C2=w, w^3=1,
    Q=2*(x^2+x*y+y^2)+3=0,
    a*(2*x^2+1)*(2*y^2+1) !=0,
    w*A2=-y-a*(2*x^2+1)/(2*y^2+1),

with the original `Delta_1*Delta_2*(T^2-4delta)` also inverted.
The identity on this conic

    (2*x^2+1)/(2*y^2+1)=(x*y-1)/(x^2+2)

is useful: `x^2+2` is already a unit there. Indeed
`(2*y^2+1)*(2*(-x-y)^2+1)=2*(2*x^2+1)*(x^2+2)`.

A bounded `w=1` trial eliminated four first-unit variables and
`A2` before imposing torsion, with all clearing factors retained.
It stopped at its sixty-second cap with exit `-15` and maximum RSS
714,358,784 bytes, before returning an elimination ideal. Its
artifacts have stem
`../computations/conditional_2_12_singular_continuation2_2026_10_21_conic_w1`.
This supplies **no** emptiness, dimension or survival certificate.
The other cube-root branches remain equally unresolved. No
unchanged rerun or larger resource limit is proposed here.

The other surviving two-node stratum is

    kappa_1=kappa_2=0,

including all its B/C and endpoint boundaries, with the quadric
direction component removed. Each factor satisfies

    (Ai+2Di)*((Di-Ai/2)^2+Bi*Ci/2)=0.

By (1), there is then a unique actual global cubic `Hi` with
symbol `alpha_i*li`; the cubic symbol map is injective. Thus the
ENTIRE allowed global sextic family on this stratum has the form

    F6=H1*H2+eta*q^3.                                       (9)

This uses the exact kernel `k*q^3` of the sextic symbol map.
An actual supported pair requires `eta!=0`: if `eta=0`, its
degree-six equation has cubic factors, contradicting the
factor-reduction and lower-carrier consequences explicitly stated
in [R-0001](../results/quartic_carrier_exclusion.md). Formula (9)
does not establish normality, global realization, or emptiness
when `eta!=0`. It gives a concrete cubic-product pencil for the
remaining global cubic-jet condition.

## 8. First unresolved lifting conditions and actual-pair boundary

On the conic and zero-defect strata, impose the first incidence,
the complete twenty-five second pairings and the actual spectral
equation (6), along with the forced multiplier. The first
unresolved global lifting test is still

    [F3-alpha*G0] mod(f)=0

with ACTUAL global sextic coefficients. The compact exported
forty-eight syzygy equations implement it without dividing by any
coefficient of `f` or by `alpha`; on (9) its only remaining
sextic freedom is the nonzero scalar `eta`. Later root or sextic
lifts, actual degree-sixteen coefficients, the full degree-twelve
standard-basis certificate and its coprimality, and the global
gcd/Bezout argument remain necessary. None of the reduced schemes
in this note is asserted nonempty or realized.

## 9. Metadata correction and evidence boundaries

Independent review found a naming defect in the committed
`conditional_2_12_singular_continuation_2026_10_21.json`: its
`norm_symbol_equations` strings were formatted after the exporter
mutated its display-name array for the later line exports. The
original-coordinate `.m2` equations were formatted BEFORE that
mutation and are correct; all completed calculations use those
mathematical input files. The old JSON strings are not equation
authority. The exact corrected strings, original names and source
hash are preserved in the NEW sidecar
`../computations/conditional_2_12_singular_continuation2_2026_10_21_metadata_correction.json`.
Previously committed files were not silently rewritten.

The old generic mixed-cube-root line trial returned a large first
Groebner basis but was stopped before a torsion result; it is not
used as an exclusion. Splitting `w=1` and the primitive quadratic
field, suppressing large intermediate output and eliminating
linear unit variables first produced the completed certificates
in section 5. The proof depends on their exact inputs and returned
unit ideals, not on the interrupted trial or an equation count.
