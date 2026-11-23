# Conditional (6,16): singular roots, cubic source, and conductor

The historical sections retain their hypotheses, qualifications, and proof status. Where an argument is repeated, links point to the full proof.

# conditional 2 12 singular and conductor

## Proof-dependency map: node gluing and conductor constraints

The [two-node torsion calculation](#2026-10-20-conditional-2-12-singular-continuation) and [subsequent singular continuation](#2026-10-21-conditional-2-12-singular-continuation2) analyze branch identifications. The [cubic-image/conductor interface](#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface) and [conductor ramification](#2026-10-21-conditional-2-12-conductor-ramification) add global compatibility conditions, with an [independent chart review](#2026-10-21-conditional-2-12-conductor-and-chart-independent-review).

The [symbol-map and sextic realization dossier](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-elimination) supplies the equation-level inputs; the [strict-surface continuation](rank_strata_and_sextic_lifts.md#nonnormal-conductor-budget-and-local-escape-models) imposes further conditions. The torsion and conductor tests are necessary compatibility constraints in the stated conditional geometry; they are not an unconditional exclusion of the (2,12) degree pair.

Preserve the exact two-node factors, torsion scheme, diagonal-slice countercheck, and chart-independence qualifications below.

---


The \((2,12)\) configuration is conditional throughout; no actual global pair is constructed.

---

## 2026-10-20-conditional-2-12-singular-continuation

# Conditional (2,12;6,16;2): exact two-node torsion and a diagonal exclusion

The factor-matrix and torsion-scheme calculation gives an exact reduction and a diagonal ambient exclusion on the stated chart, with its contraction ideal and source substitution. The exceptional and collision strata are not excluded by this calculation.

## Scope and existing interface

Retain precisely the characteristic-zero curve, actual-CI, full generic
coprime `(2,12)` initial ideal and saturated movement-two relation
hypotheses in
[the singular-root bridge note](singular_root_actual_pair_bridge.md).
The current task investigates the necessary structured incidence, not
unrestricted homogeneous equations. The inherited universal first
incidence and complete second test are stated in [STCI-R-0007](../../results/quadratic_root_obstruction_model.md), and the
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

The [original-coordinate generator](../../computations/conditional_2_12_singular_continuation_2026_10_20.py)
constructs the exact first/second incidence with (3) and open (1).
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


---

## 2026-10-21-conditional-2-12-singular-continuation2

# Conditional (2,12;6,16;2): forced-norm two-node reductions and exclusions

Date: 2026-10-21. Author: `singular_gluing` continuation worker.
Status: **new exact reductions and scoped exact exclusions**. The cubic-defect identities, generic line/conic
decomposition and original-coordinate normalizations were independently
reviewed by `two_node_torsion_audit`. The new completed line-component and boundary
CAS exclusions are submitted to `certificate_audit` for independent
review. An interrupted conic computation gives no exclusion or survival
certificate.

## 1. Literal actual-pair scope and dependencies

Retain characteristic zero, the fixed
`C0=[s^4:s^3t:st^3:t^4]`, an actual homogeneous pair of degrees
`6,16` with sole reduced support `C0`, FULL generic ordinary initial
ideal a coprime binary CI `(2,12)`, and the ACTUAL saturated first
relation of movement two. The inputs are
[R-0010](../../results/saturated_first_relation_normal_flatness.md),
[R-0011](../../results/moving_nonreduced_spectral_root_obstruction.md),
and the universal first/second operators in
[R-0007](../../results/quadratic_root_obstruction_model.md).
The finite singular-root bridge remains the reviewed proposal in
[the singular-root note](singular_root_actual_pair_bridge.md).

This continuation additionally uses the independently reviewed
**actual-pair** norm identity from
[the actual-pair norm proof](../carriers/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge):
if `q1=u+zv/2`, `tau=f|_(q1=0)`, then `tau!=0` and

    alpha proportional tau(omega*z)*tau(omega^2*z), omega^3=1.

That identity retains collisions and endpoint ramification. It must
not be inferred on arbitrary low-order points just from the generic
orbit factorization. The sextic symbol image and its exact
one-dimensional kernel are the reviewed new computation in
[the exact sextic symbol map](rank_strata_and_sextic_lifts.md#2-the-exact-global-k-linear-symbol-map).

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
over `QQ`. The historical calculation returned zero in 0.407 seconds with maximum
RSS 122,503,168 bytes. The [exact rational input](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_w1.m2) reproduces
(7) and the unit saturation. [Historical run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_w1.log).

For a primitive cube root, use the exact number field
`QQ[w]/(w^2+w+1)` and keep `a,x`. The actual open is

    a*(2*x^2+1)*(a^2-x^2-2)*(2*a^2-3) !=0.

The same first-unit elimination followed by adding (6) and
saturating this open again returns the unit ideal. It completed
with return code zero in 1.242 seconds with maximum RSS 283,295,744
bytes. The [exact number-field input](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_primitive.m2) covers both
conjugate primitive roots. [Historical run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_primitive.log).

Thus all three `w` branches of the generic line component are
excluded, before the complete second obstruction or global cubic
matching is needed. These are exact characteristic-zero
computations on specified coefficient schemes, not finite samples.

## 6. The full nonzero-defect B/C boundary is exactly excluded

With both defects units, `B1=0` forces `B2^3=0`. On closed points
both `B` coefficients vanish; the same statement holds for the
two `C` coefficients. If both `B` and both `C` vanish, the old
diagonal exclusion in
[the preceding continuation](#2026-10-20-conditional-2-12-singular-continuation)
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

The [rational input](https://github.com/markluxton1/STCI/blob/6bb084487daafca4af85489949a00ce0ef193ece/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_w1.m2) gives `(t-2)` and the
[number-field input](https://github.com/markluxton1/STCI/blob/959d131f7ce23401aa7fbd437739b734d0462fa6/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_primitive.m2) gives `(1)` before torsion.
The first-order contraction proves the exclusion on (8). The
[rational run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_w1.log) and
[number-field run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_primitive.log) also record the
redundant first-plus-torsion unit calculation.

The historical outputs of the two line and two boundary calculations
were reproduced with `M2 --script` on the four linked inputs from the
repository root.

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

with its B/C and endpoint boundaries retained, the quadric direction
component removed, and the sign-odd sublocus excluded below. Each
factor satisfies

    (Ai+2Di)*((Di-Ai/2)^2+Bi*Ci/2)=0.

By (1), there is then a unique actual global cubic `Hi` with
symbol `alpha_i*li`; the cubic symbol map is injective. Thus the
ENTIRE allowed global sextic family on this stratum has the form

    F6=H1*H2+eta*q^3.                                       (9)

This uses the exact kernel `k*q^3` of the sextic symbol map.
An actual supported pair requires `eta!=0`: if `eta=0`, its
degree-six equation has cubic factors, contradicting the
factor-reduction and lower-carrier consequences explicitly stated
in [R-0001](../../results/quartic_carrier_exclusion.md). Formula (9)
does not establish normality, global realization, or emptiness
when `eta!=0`. It gives a concrete cubic-product pencil for the
remaining global cubic-jet condition.

The [sign-odd cubic-factor proof](sign_odd_two_node_sextics.md)
now excludes `Ai=Di=0`, `Bi*Ci!=0` for both factors, with
`B1*C2-B2*C1!=0`. The unique actual cubics there are sign-odd,
so (9) is sign-even for every `eta` and cannot have a sole-support
mate of any degree. This is distinct from the earlier both-even
diagonal slice. It does not exclude the remaining zero-defect locus
or the nonzero-defect conic.

## 8. First unresolved lifting conditions and actual-pair boundary

On the remaining conic and zero-defect strata, impose the first incidence,
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

## 9. Exact certificate authority and remaining discrepancy

The original-coordinate `.m2` equations, rather than the formerly mislabeled `norm_symbol_equations` JSON strings, are authoritative. The [exporter](../../computations/conditional_2_12_singular_continuation_2026_10_21.py) now captures equation strings before display-variable renaming. This does not resolve the separate FIRST-residual discrepancy. The exclusion in section 5 uses the completed `w=1` and primitive-quadratic-field unit-ideal certificates; the interrupted mixed-cube-root trial proves nothing.


---

## 2026-10-21-conditional-2-12-cubic-image-and-conductor-interface

# The cubic image and the anticanonical conductor interface

Status: **independently reviewed conditional proof in the actual-pair scope**. The fixed curve is C0, and the antecedent is an actual sole-support degree-(6,16) pair with full generic initial CI (2,12) and actual saturated movement-two first relation. The proof does not assert that this antecedent is realized, nor emptiness of the remaining incidence.

## 1. Explicit cubic image

Put q=x0*x3-x1*x2, A=x0^2*x2-x1^3,
B0=x0*x2^2-x1^2*x3, D0=x2^3-x1*x3^2. The seven cubics

    q*x0,q*x1,q*x2,q*x3,A,B0,D0

generate I_C0(3). They define the line bundle L=3H-E on
B=Bl_C0(P3), and a morphism phi:B->P6. The pair of maps given by
H and L is the graph closed immersion B->P3 x P6: the seven cubics
give the usual relative Proj embedding of the Rees algebra, after
twisting by O(3). In particular H+L is ample.

In P6 with coordinates y0,...,y6, the image is cut out by

    y0*y5-y2*y4+y1^2,
    y0*y6-y2*y5+y1*y3,
    y1*y5-y3*y4+y0*y2,
    y1*y6-y3*y5+y2^2,
    y4*y6-y5^2+y1*y2.                                  (1)

The new exact M2 calculation
[cubic-image verifier](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_cubic_image_2026_10_21.m2)
checks the following over QQ:

* substituting the seven displayed cubics makes all five equations zero;
* their quotient ring has dimension four and degree five;
* the affine singular locus is zero-dimensional (only the cone vertex),
  so their projective threefold V is smooth;
* the quotient has free resolution with ranks (1,5,5,1) and shifts
  (0,2,3,5).

The resolution proves arithmetically Cohen--Macaulay, type one, with
canonical sheaf omega_V=O_V(-2). It also gives H0(O_V)=k, so V is
connected. A smooth connected projective scheme here is integral.
The cubic map is birational onto its image because off q=0 the first
four cubics recover [x0:x1:x2:x3]. Its image is closed, dimension
three, and contained in integral V of dimension three, hence equals V.
The same statements base-change to every characteristic-zero field.

## 2. An explicit blowup identification

Let Gamma be the conic cut out on V by y0=y1=y2=y3=0; equation (1)
leaves y4*y6-y5^2=0 in P2, so Gamma is smooth. The inverse rational
map V-->P3 is the projection [y0:y1:y2:y3]. Its graph closure is
Bl_Gamma(V), since its base ideal on V is exactly the ideal generated
by these four sections, whose scheme of zeros is Gamma.

Under the graph closed immersion B->P3 x V, the image is exactly this
graph closure: on the dense open q!=0 it is the graph of the inverse
birational maps, and B is integral and the graph embedding is closed.
Thus

    B = Bl_Gamma(V).                                    (2)

The exceptional divisor of (2) is Q'=2H-E=L-H, the strict transform
of the original smooth quadric. Indeed the common zero divisor of
the four pullback sections y0,...,y3 is Q': each section is the strict
q factor times x_i, and the four x_i have no common zero. The map
Q'->Gamma is the contraction of one ruling, with degree-two image
polarization. This proof needs no classification theorem for V5.

## 3. The actual sextic descends to an anticanonical surface

The exact 23-element source basis in
[the symbol computation](rank_strata_and_sextic_lifts.md#2-the-exact-global-k-linear-symbol-map)
consists of products of the seven cubics. Consequently every actual
sextic in H0(I_C0^2(6)) gives a quadric section T of V with

    D=phi^* T,              O_V(T)=O_V(2),
    omega_T=O_T.                                     (3)

For an actual supported pair, F6 cannot have Q as a component, by
the quadric Picard argument in
[the quadric-factor exclusion](../carriers/normalization_conductor_phase2_addendum.md#the-quadric-direction-is-not-a-root-component).
Thus D has no Q' component, T does not contain Gamma, and D is the
strict transform as well as total pullback of T. Off Q', phi is an
isomorphism, so local normalizations and conductors there transfer
between D and T unchanged.

For the remaining conductor discussion one needs T integral. This
follows within the actual supported-pair scope from the accepted
exclusion of all carriers of degree at most four. Every irreducible
factor of F must contain C: otherwise its positive-degree intersection
with G gives a curve outside C. Each such factor is itself a supported
carrier for C with mate G. Hence each has degree at least five. A
sextic can have only one such factor and no higher power, so F, D,
and T are integral. This use of the lower-carrier exclusion must be
checked against its literal canonical hypotheses before applying the
conductor claim; it is not needed for (1)-(2).

## 4. Full conductor of a Gorenstein anticanonical surface

The [conductor-duality proof](rank_strata_and_sextic_lifts.md#3-full-conductor-duality-and-component-genus-independent-review-pass) applies to the integral
Gorenstein anticanonical surface with trivial dualizing sheaf. It identifies
the full upstairs conductor ideal with the canonical module of the
normalization. If nonempty, its conductor scheme Delta is a pure
Cohen--Macaulay curve with trivial dualizing sheaf, hence
`chi(O_Delta)=0` by Serre duality. Each integral component of generic
multiplicity one has arithmetic genus at most one, including when other
components are nonreduced. The proof allows a non-Gorenstein normalization
and a non-Cartier conductor.

A local model forcing a generically reduced conductor branch with delta
invariant at least two therefore needs a separate analysis of whether that
branch maps onto a conductor component after the contraction. The
[ramified-simple-zero argument](#5-the-contracted-ruling-fiber-case) checks
this issue in its stated setting.

## Reviewed actual-pair scope

The seven cubic coordinates, five quadrics, graph/base-ideal blowup construction and full conductor duality above were independently reconstructed in the actual sole-support (6,16), full generic (2,12), saturated movement-two setting. The [stronger conductor continuation](rank_strata_and_sextic_lifts.md#2026-10-21-conditional-2-12-surface-audit-cont2) retains the critical-value unit argument, monic local normalization, component-genus refinement and explicit rejection of the nonfinite nodal model. The argument does not assert that an abstract low-order incidence point supplies an actual global pair, nor does it close the remaining exceptional strata.

## 2026-10-21-conditional-2-12-conductor-ramification

# Conditional (2,12;6,16;2): conductor control at a ramified simple multiplier zero

Date: 2026-10-21. Author: `conductor_budget` worker.

Status: **reviewed conditional conductor and ramification argument**. The anticanonical contraction hypothesis used below is established for the actual-pair scope in the preceding cubic-model proof and the stronger continuation. The local monic normalization and critical-value argument retain their explicit hypotheses. The nodal nonfinite attempted normalization is rejected as explained in section7. No global pair, full incidence-emptiness certificate or general nonnormal-surface bound is claimed.

## 1. Exact scope and source boundary

Use the same actual-pair hypotheses as the reviewed
[surface-bound proposal](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus): an actual
homogeneous supported pair of degrees `(6,16)`, full generic coprime initial CI
of degrees `(2,12)`, and actual saturated movement-two first relation, over an
algebraically closed field of characteristic zero. The inputs are
[R-0010](../../results/saturated_first_relation_normal_flatness.md) and
[R-0011](../../results/moving_nonreduced_spectral_root_obstruction.md); the finite
singular-root bridge remains the reviewed dependency in
[the singular-gluing proposal](singular_root_actual_pair_bridge.md).

Put `B=Bl_C0(P3)`, `L=3H-E`, and `Q'=2H-E=L-H`. The strict sextic is
`D in |2L|`, and `K_D=Q'|D`. In this note **D is assumed integral**. At a root
point above a zero of the base multiplier `alpha`, the actual finite bridge
and invertible generator change give

    F'=A*p+t^10*U,       U a unit,       p=G16/t^2 up to a unit,       (1)

where `t=0` cuts out `E`. On `E`, the coefficient of `p` is `alpha/beta`;
`beta` is a unit at a zero of `alpha`. Thus a simple zero of `alpha` on the
BASE gives `A|E=z` up to a unit, with `z` a local base parameter. This does
not assert that the pullback divisor on the double root cover is reduced.

The reduced root `Z` has bidegree `(2,2)`. The full spectral condition removes
the cuspidal and tangent-component strata, retaining smooth integral,
integral nodal, and two-node reducible roots, with their actual gluing data.
No earlier first or second obstruction computation is repeated here.

The global canonical-ideal facts used below are specializations of finite
duality and codimension-one adjunction. A primary reference is Miles Reid,
[Nonnormal del Pezzo Surfaces, section 2](https://ems.press/content/serial-article-files/40537).
Only those general duality facts are used; the del Pezzo classification and
its antiample hypotheses are not transferred to the present situation.

## 2. The conductor of a Gorenstein surface with trivial dualizing sheaf

The [full proof](rank_strata_and_sextic_lifts.md#3-full-conductor-duality-and-component-genus-independent-review-pass) shows that the nonempty conductor
of the normalization of an integral projective Gorenstein surface with
trivial dualizing sheaf is a pure Cohen--Macaulay curve with trivial
dualizing sheaf. It also proves that an integral component of generic
multiplicity one has arithmetic genus at most one. An intrinsically
unibranch point of delta invariant two on such a component is therefore
impossible. This holds when other conductor components are nonreduced.

## 3. Explicit global contraction hypothesis

For the application below, assume a morphism

    psi:B -> Y0

with ALL the following properties:

* `Y0` is a smooth projective threefold, with an ample class `M`;
* `psi` is birational and is an isomorphism off `Q'`;
* `Q'=P1 x P1`, with normal bundle `O(1,-1)`, is its exceptional divisor;
  `psi` contracts exactly the ruling fibers on which `L|Q'=O(2,0)` has
  degree zero;
* `psi^*M=L`, `K_Y0=-2M`, and the integral `D in |2L|` is the pullback of
  an integral `T in |2M|`.

Then `T` is Gorenstein with trivial dualizing sheaf. The expected target is
the degree-five del Pezzo threefold in `P6`. **This note does not establish
that contraction or the descent of every section of `2L`. They are required
bridges, not consequences of the numerical identities alone.**

Let `Y_D` and `Y_T` be the normalizations of `D` and `T`. The morphism
`Y_D->T` factors through a proper birational map `Y_D->Y_T`. A conductor
component `R_D` whose image curve in `B` is not contracted by `psi` maps
finite birationally onto a conductor component `R_T`: away from `Q'` the
ambient morphism is an isomorphism. Generic conductor multiplicity one is
preserved. For proper integral curves a finite birational map gives

    p_a(R_T) >= p_a(R_D).                                    (6)

Consequently the genus bound of section 2 applies to every such
NONCONTRACTED component. Contracted exceptional ruling fibers require a
separate argument; section 5 supplies one for the particular local germ
arising below.

## 4. Exact local normal form at a ramified simple base zero

Assume `Z` is smooth at `x`, its degree-two map to the base is ramified
there, and `alpha` has a simple zero on the base. In completed local
coordinates one may arrange

    A|t=0 = z times a unit,       p|t=0 = (z-w^2) times a unit.

Both `A` and `p` are regular in `z`. By formal Weierstrass division,

    A=a*(z-a0(w,t)),       p=b*(z-p0(w,t)),

where `a,b` are units, `a0(w,0)=0`, and `p0(w,0)=w^2` after the allowed
coordinate choices. Divide (1) by `ab`, center the `z` coordinate, and put
`s=(p0-a0)/2`. This gives

    F'=z_c^2-s(w,t)^2+t^10*V(z_c,w,t),       V a unit.

Its `z_c`-critical section `c(w,t)` lies in `(t^10)`. Parameter-dependent
formal completion of the square gives an actual formal coordinate `x` and
unit `u(w,t)` with

    F'=x^2-B(w,t),
    B=s(w,t)^2-t^10*u(w,t),       s(w,0)=w^2/2.              (7)

Indeed the critical value differs from `-s^2` by `t^10` times a unit;
`c^2/t^10` is divisible by `t^10`, so the unit remains a unit. Formal square
roots of units exist in characteristic zero over the algebraically closed
field. Hence

    B=B_-*B_+,       B_-=s-t^5*sqrt(u),   B_+=s+t^5*sqrt(u). (8)

Each factor is Weierstrass of degree TWO in `w`. They have no common
irreducible factor: any common factor would divide `t^5`, but neither
factor is divisible by `t`.

A double-cover hypersurface `x^2=B` in characteristic zero is normal
exactly when `B` is squarefree. Thus nonnormality at this germ forces one
factor, say `B_-`, to have the form

    B_-=e*d^2,       d=w-phi(t),       e a unit.              (9)

The other factor cannot also be a square. If `B_+=e2*d2^2`, restriction to
`d=0` would make `t^5` times a unit a square in `k[[t]]`, impossible because
its valuation is odd. It follows that `B_+` is reduced, and

    B_+|d=0 = t^5 times a unit.                              (10)

After absorbing `sqrt(e)`, the normalization is

    Y_local: y^2=B_+(w,t),       x=d*sqrt(e)*y.

This is normal, because `B_+` is reduced. Write `R=k[[w,t]]`; the original
ring and its normalization have presentations

    R + d*R*y  subset  R + R*y.

Their conductor is EXACTLY `d*(R+R*y)`: multiplication by `y` forces both
coefficients of a conductor element to be divisible by `d`. Consequently
the conductor curve germ is

    d=0,       y^2=t^5 times a unit.                         (11)

It is reduced, irreducible, of generic multiplicity ONE, and has
`delta=2`. Thus its global reduced conductor component has arithmetic
genus at least two.

Under the contraction hypothesis of section 3, if the corresponding
nonnormal curve is not contracted, (6) and the genus-one bound contradict
(11). This argument includes the case where the particular point lies on
`Q'`; a noncontracted conductor curve still maps finite birationally.

## 5. The contracted ruling-fiber case

Suppose the nonnormal curve in section 4 is a ruling fiber `W` contracted
by `psi`. On `B` one has

    N_(W/Q')=O_W,       N_(Q'/B)|W=O_W(-1).

The normal sequence splits since `H^1(P1,O(1))=0`, so

    N_(W/B)=O_W + O_W(-1),       O_B(D)|W=O_W.                (12)

The equation of `D` vanishes to order at least two along `W`. Its quadratic
normal cone is a global section of
`Sym^2(N_(W/B)^*) tensor O_B(D)|W`. Its discriminant is therefore a section

    disc(q2) in H^0(W,(det N_(W/B)^*)^2 tensor O_B(2D)|W)
             = H^0(P1,O(2)).                               (13)

The local normal form (9)--(10) is an ordinary transverse double crossing at
the generic point of `W`, so this discriminant is nonzero. In the local
coordinates `(x,d)` normal to `W`, its quadratic form is

    q2=x^2-t^5*unit*d^2.

Here `t` is a uniformizer on `W`, since `W=(x,d)` and `d=w-phi(t)`. The
discriminant thus vanishes to order FIVE at the point. That contradicts
(13), whose total zero degree is two. This excludes the contracted case
without applying the anticanonical conductor genus bound to a contracted
curve.

Combining sections 4 and 5 gives the following conditional conclusion:

> Subject to the contraction bridge in section 3, no nonnormal curve of
> the integral strict sextic can pass through a smooth ramification
> point of the root where alpha has a simple zero on the base.

At a smooth UNRAMIFIED root over a simple base zero, `(A,p,t)` are regular
coordinates; the germ is an isolated `A9` singularity. It contributes no
nonnormal curve. Thus the word "ramified" is now removed from the generic
simple-base-zero exception, but repeated base zeros and root nodes remain.

## 6. Conditional residual locus with squarefree alpha

The following consequence uses only the actual finite bridge, the local
conclusion above, the ampleness of `G'=16H-2E=10H+2L`, and the preceding
normal-strict-sextic exclusion. Ampleness follows if `H` and `L` give the
closed graph embedding into `P3 x P6`; that graph property is part of the
same geometric bridge and must be checked separately.

Suppose `alpha` is squarefree on the BASE and is nonzero at every singular
point of `Z`. Along `E` away from `Z`, the equation `F'|E=alpha*f` has
nonzero derivative in the base direction whenever it vanishes; hence `D`
is smooth there. At smooth root points over `alpha=0`, sections 4--5 and
the unramified `A9` calculation exclude any nonnormal curve. At smooth
root points where `alpha` is a unit, `D` is smooth.

A nonnormal curve `Sigma` would therefore meet `E` only at root nodes where
`alpha` is a unit. It cannot be contained in `E`, since the preceding
singular points in `E` are finite. At such a node one may take `p=F'`, and
parameter-dependent Morse coordinates give

    p=X*Y+h(t).

A singular curve exists there only if `h=0` identically, and its local
parameter is then `t`. Thus every such intersection with `E` is transverse.
There are at most two root nodes in the retained spectral strata. Put

    d=H.Sigma,       n=E.Sigma,       1<=n<=2.

The strict second equation restricts to `t^10` times a unit at each node,
and its intersection with `D` has sole support `Z`; hence

    (16H-2E).Sigma=10*n.

It follows that `16d=12n`, or `4d=3n`, impossible for integral `d>=1` and
`n=1,2`. A curve with `H.Sigma=0` would lie in an exceptional `E`-fiber,
already excluded. Thus `D` has no nonnormal curve, so its integral
hypersurface is normal. The existing normal-strict-sextic exclusion then
applies.

Accordingly, conditional on the geometric bridges and the normal-surface
proposal, an actual pair with integral strict sextic must satisfy at least
one of

    alpha has a repeated zero on the base;
    alpha vanishes at a root node.                           (14)

This is an exact exceptional-locus restriction, not a proof that its
remaining locus is empty. In particular it does not replace the actual
nodal or two-node gluing conditions by normalization data.

## 7. Exact local escape at a root node

**Correction flagged by independent reviewer `surface_bound` on 2026-10-21:**
the displayed map below obtained by adjoining `y=w/(z-t^3)` is NOT finite
at the origin: its fiber there contains the affine `y`-line. Consequently
it is not the finite normalization, and the ensuing assertions about its
conductor and normalization singularities must not be used. The equation
`F=z*p+t^10` and the existence of its nonnormal curve remain correct local
countermodels. The correction and a genuinely integral normalization
candidate are recorded in
[the continuation audit](rank_strata_and_sextic_lifts.md#2026-10-21-conditional-2-12-surface-audit-cont2).
This defect is confined to the nodal example; sections 2--6 use the monic
`x^2` normalization calculation and do not divide by a nonunit coefficient.

The local calculations do not remove the second stratum in (14). For
example

    F=z*w^2-(z-t^3)^2*(z-t^4)
      = z*p+t^10,

where

    p=w^2-z^2+z*t^4+2*z*t^3-2*t^7-t^6.

On `t=0`, the full root is the ordinary node `p=w^2-z^2`, and the base
multiplier is the simple zero `alpha=z`. The surface is nonnormal along

    W: w=0, z=t^3,

which leaves E. The attempted parametrization

    y=w/(z-t^3), z*(y²−1)=−t^4

is not finite at the origin: its fiber there contains the affine y-line. It therefore supplies neither the finite normalization nor a conductor or normalization-singularity calculation. The valid content is the displayed local surface equation and its nonnormal curve; it is not an actual globally allowed sextic or a supported pair. A monic integral extension candidate, whose normality and exact conductor are still to be verified, is retained in the stronger continuation.

Repeated zeros of `alpha` are likewise genuinely unresolved. A gap-ten
term alone does not force transverse singularity `z^m+t^10` along a
nonnormal curve. For example `p*(z^2+t^2)+t^10` has a generic ordinary
double transverse singularity along `z=t=0`, with conductor cost two,
rather than the cost ten of `p*z^2+t^10`. A conductor-degree budget by
itself does not exclude these strata.

## Remaining actual-equation incidence

The actual anticanonical contraction and reviewed monic ramification exclusion do not settle the multiple-base-zero or nodal-contact strata. Retain the forced norm multiplier, all first and second ambient equations, full spectral gluing and actual homogeneous coefficient lifting. None of the local escape models constructs a point of that full incidence, a degree-twelve standard basis, or a proper degree-sixteen mate.

## 2026-10-21-conditional-2-12-conductor-and-chart-independent-review

# Cubic contraction, conductor and realization charts

The scoped bridges and chart exclusions below assume fixed `C0`, characteristic zero, degrees `(6,16)`, full generic coprime ordinary initial CI `(2,12)`, actual saturated movement-two first relation, and sole reduced support `C0`. They do not prove full conditional emptiness.

## 4. Tiny free-orbit unit certificate and its exact coverage

The persisted new audit

The archived command uses [conditional_2_12_cont2_independent_unit_audit_2026_10_21.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py) from the pinned repository snapshot.

    python3 research/computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py

was run successfully. It compares the full-cubic residuals from
the saved 48-equation source with the candidate residual set
after exact specialization and polynomial reduction; it also
checks the following identity without a Groebner basis. Put

    P=648h^4+45h^2-4,
    E4=3eta/4+369h/16-891h^3/2,
    E8=eta/8+27h/32-81h^3/4.

Then `E4-6E8=18h-324h^3`, and identically over QQ,

    1=((162h^2-1)/4)*P
        +(81h^3+77h/8)*(E4-6E8).

Thus the exact candidate family cannot satisfy the full global
sextic cubic lift, independently of the second ambient or Picard
tests. This is a polynomial unit identity, not just exclusion of
four numerical approximations.

The [lightweight exact family verifier](https://github.com/markluxton1/STCI/blob/8775cf615047b7a878c436eab7bd9b0a0f039190/research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2)
was also run successfully, as recorded in its
[historical successful run record](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.json).
It checks both exact ideal containments by rational normal forms,
with dimension zero and degree four, between the saved
first/quadric-cubic family ideal and the triangular ideal defining `P=0`. This bridges the tiny identity
back to the entire displayed family, rather than just checking
that the four candidate points solve necessary equations.

Coverage was audited separately:

* The normalization `d0=d4=1` uses projective root scaling and
  the actual `C0`-preserving torus. Choosing a fourth root of a
  nonzero ratio gives a finite faithfully flat cover of the
  nonzero-endpoint chart. It covers no endpoint-zero root.
* On that chart, multiplication by the norm complement in
  `k[z]/(D)` has determinant `81*detJ^2`. Thus `detJ!=0` is
  exactly the absence of collisions between roots in different
  rotated cubic-ruling positions. It need not make `D`
  squarefree: repeated roots of `D` with no rotated collision
  are INCLUDED in this exclusion.
* The smaller differentiated quadric test is equivalent to the
  all-strata test precisely on this open: both `z` and the
  multiplier are units in `k[z]/(D)`. No inverse of `D'` is
  used, so repeated roots are not accidentally lost.
* The eight-variable family keeps all four first-correction
  variables. Its ideal-equality and tiny unit certificates do
  not require the separate four-row Schur pivot determinant.
  Hence pivot-rank-drop points on this free-orbit chart are
  included.

An old October 20 printed Schur matrix omitted the
term `-d1*d3` in its middle diagonal entry. The October 21
exporters used for these certificates contain that term. The
old printed formula must not be used to redefine this chart.

**PASS on `d0*d4*detJ!=0`; no endpoint or orbit-collision
emptiness follows from this certificate.**

## 5. Endpoint multiplicity lemma and two exact normal forms

Here is an additional actual-pair reduction, independently checked
at the root agent's request. Write `tau=f(-z/2,1)` and assume
`m=ord_0(tau)>0`. The norm lemma gives residual divisor
`R=b^m*unit` on the quadric chart `(z,b)`, where
`C0:b=z^3`. The residual mate divisor `T` has restriction of
degree ten to the ruling `b=0`. It cannot contain that ruling;
actual sole support forces its zero divisor on the ruling to
be precisely ten times its sole intersection point with `C0`.
Thus `T(z,0)=z^10*unit`.

The actual ideal equality on the strict quadric is

    (R,T)=(p,t^10),             t=b-z^3.

Reduce it modulo `b`. The left side becomes `(z^10)`, while
the right side is `(p(z,0),z^30)`. Hence

    ord_z p(z,0)=10.

Substitution `b=z^3` changes a regular power series by an
element of `(z^3)`, so `p(z,z^3)` is divisible by `z^3`.
Its order is exactly `m`, since the exceptional restriction of
`p` is a unit multiple of the saturated root equation. Therefore

    ord_0(tau)>=3.

The same argument in the opposite homogeneous chart gives
`ord_infinity(tau)>=3` whenever that order is positive. A
nonzero binary quartic cannot satisfy both inequalities. Thus,
up to the actual projective/torus scaling and inversion of
`C0`, every remaining endpoint root has one of the two forms

    tau=z^3*(1+z),       or       tau=z^4.

The multiplicity-three case has a nonzero remaining finite
root; a remaining root at infinity would violate the second
endpoint inequality. Torus scaling moves that finite nonzero
root to `-1`. These reductions do not assume the endpoint
multiplier is nonzero and do not divide by it.

**Review outcome:** PASS for the endpoint lemma within the
actual supported-pair scope. It is a finite chart reduction,
not exclusion of either resulting chart. Together with section
4 it leaves the nonzero-endpoint orbit-collision chart and the
two endpoint normal forms for the structured computation.

## 6. Fourth-order endpoint: the retained root and exact nodal modulus

On the endpoint chart `D=4tau=z^4`, the symbol equations give

    a=a0+2b2*z+z^2,
    b=b1*z+b2*z^2,
    c=(b1/2-a0/4)*z^2,
    a0!=0.

The root meets the smooth quadric-direction diagonal only at
`p=(z,w)=(0,0)`, with total intersection length four, where
`w=-2u/v`. It cannot be a reduced two-component survivor: each
`(1,1)` component would meet that diagonal with total degree two,
all at `p`, and would consequently be tangent to the diagonal.
The two smooth components would be tangent to each other, the
already excluded additive Picard stratum. A diagonal component
itself is forbidden by `tau!=0`.

Hence any retained endpoint-four root is integral nodal. Its
tangent quadratic is

    (u+z*v/2)*(a0*u+(b1-a0/2)*z*v).

The two slopes `dw/dz` are therefore

    1,       rho=2*b1/a0-1.

They are nonzero and distinct on the retained open. Distinctness
is the nodal condition. If `rho=0`, the displayed coefficient
`c` is zero identically and the binary root has a constant
direction component, violating finiteness in both rulings.

To check that the modulus is the actual Picard gluing, let the
normalization ruling maps be `z=X1/X0` and `w=Y1/Y0`, each of
degree two. Their degree-two numerators vanish at both node
preimages, so `Y1=c*X1`. Their local slope ratios are
`r_i=c*X0(i)/Y0(i)`. On the other hand the actual identification
of `O_Z(1,-1)` at the two preimages gives

    lambda=Y0(p)*X0(q)/(X0(p)*Y0(q))=r_q/r_p.

Thus `lambda=rho` up to inversion, with no normalization-degree
substitution for the conductor identification. The exact spectral
condition on this chart is

    (2*b1/a0-1)^12=1,           2*b1/a0-1 !=1.

After clearing the unit denominator this is
`(2*b1-a0)^12-a0^12=0` on the stated open. This is a necessary
torsion equation, not an exclusion of its intersection with K1
or higher global lifts. The argument was independently
reconstructed from the root agent's proposed endpoint reduction.


### Retired source certificate: `research/computations/conditional_2_12_cubic_image_2026_10_21.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- New exact cubic-image calculation. No actual pair is constructed.
R=QQ[y0,y1,y2,y3,y4,y5,y6];
I=ideal(y0*y5-y2*y4+y1^2,
        y0*y6-y2*y5+y1*y3,
        y1*y5-y3*y4+y0*y2,
        y1*y6-y3*y5+y2^2,
        y4*y6-y5^2+y1*y2);
assert(dim(R/I)==4);
assert(degree(R/I)==5);
singIdeal=I+minors(3,jacobian gens I);
assert(dim(R/singIdeal)==0);
F=res(coker gens I);
assert(length F==3);
assert(degrees F_1==toList(5:{2}));
assert(degrees F_2==toList(5:{3}));
assert(degrees F_3=={{5}});
S=QQ[x0,x1,x2,x3];
q=x0*x3-x1*x2;
A=x0^2*x2-x1^3;
B=x0*x2^2-x1^2*x3;
D=x2^3-x1*x3^2;
phi=map(S,R,{q*x0,q*x1,q*x2,q*x3,A,B,D});
assert(phi(I)==ideal(0_S));
print("CUBIC_IMAGE_EXACT: projectively smooth threefold, degree5, resolution(1,5,5,1) shifts(0,2,3,5)");
print("CUBIC_SYZYGIES_ZERO: canonical sheaf O(-2), by the codimension3 selfdual resolution");
print betti F;
print("NO_GLOBAL_PAIR_OR_EMPTINESS_CERTIFICATE_CLAIMED");
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_collision.py`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""One-pair mu3 collision chart, retaining its explicit rank-drop boundary.

D=(z-1)(z-omega)(z^2+e*z+ff), monic. On ff*S!=0, norm-symbol
compatibility is the displayed four-parameter family; no arbitrary root
coefficient chart or global sextic search is introduced.
"""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
accepted=HERE/'generalization_quadratic_root_curve_universal_incidence.json'
data=json.loads(accepted.read_text())
first=[]
for row,rhs in zip(data['A_f'],data['d_f']):
    terms=[f'({p})*h{j}' for j,p in enumerate(row) if p!='0']
    first.append('+'.join(terms)+f'-({rhs})')
stem=Path(__file__).with_suffix('')
lines=[
 '-- Generic one-pair collision chart; rank-drop factors explicitly retained.',
 'K=QQ[omega]/ideal(omega^2+omega+1);',
 'R=K[ee,ff,lambda,tt,H4,H5,H6,H7,fi,MonomialOrder=>GRevLex];',
 'd0=omega*ff; d1=omega^2*ff+omega*ee; d2=ff+omega^2*ee+omega; d3=ee+omega^2;',
 'a0=4*tt+2*ee*lambda; a1=d3/2+2*lambda; a2=1;',
 'b0=-d1/4-ff*lambda; b1=4*tt-d2/2+ee*lambda; b2=-d3/4+lambda;',
 'c0=d0/4; c1=d1/8-ff*lambda/2; c2=tt;',
 'h4=H4; h5=H5; h6=H6; h7=H7;',
 'h3=-a0*h5-a1*h4;',
 'h2=-3-a0*h4-a1*h3;',
 'h1=-4*a1+3*b2-a0*h3-a1*h2;',
 'h0=-5*a0+3*b1-a0*h2-a1*h1;',
 'c0Inverse=4*omega^2*fi;',
 'h8=-c0Inverse*(c2*h6+c1*h7);',
 'h9=-9/2-c0Inverse*(c2*h7+c1*h8);',
 'h10=c0Inverse*(-4*c1-3/8*b0-c2*h8-c1*h9);',
 'h11=c0Inverse*(-7/2*c2-3/8*b1-c2*h9-c1*h10);',
 'firstEquations={'+','.join(first)+'};',
 'endpointUnit=ff*fi-1;',
 'S=R[zz];',
 'aa=a0+a1*zz+zz^2; bb=b0+b1*zz+b2*zz^2; cc=c0+c1*zz+c2*zz^2;',
 'DD=(zz-1)*(zz-omega)*(zz^2+ee*zz+ff);',
 'U=d0+d3*zz^3; V=d1*zz+zz^4; W=d2*zz^2;',
 'alphaCanonical=U^2+V^2+W^2-U*V-U*W-V*W;',
 'coeffR=(p,j)->sub(coefficient(zz^j,p),R);',
 'normSymbol=apply(3,j->coeffR(alphaCanonical*aa,3*j+1)-coeffR(alphaCanonical*bb,3*j+2)-(j+1)*coeffR(alphaCanonical*DD,3*j+3)/4);',
 'assert(all(normSymbol,p->p==0));',
 'g30=-(a1*h5+a2*h4)-a2*h5*zz;',
 'g21=-(b1*h5+b2*h4+a1*h11+a2*h10)-(b2*h5+a2*h11)*zz;',
 'g12=-(3/4*a2+c1*h5+c2*h4+b1*h11+b2*h10)-(c2*h5+b2*h11)*zz;',
 'g03=-(3/8*b2+c1*h11+c2*h10)-c2*h11*zz;',
 'GG=g30*(-zz/2)^3+g21*(-zz/2)^2+g12*(-zz/2)+g03;',
 'LL=diff(zz,DD)-12*zz^2*GG;',
 'qlCoefficients=new MutableList from apply(7,j->coeffR(LL,j));',
 'scan(reverse toList(2..6),j->(v:=qlCoefficients#j;qlCoefficients#(j-2)=qlCoefficients#(j-2)-ff*v;qlCoefficients#(j-1)=qlCoefficients#(j-1)-ee*v;qlCoefficients#j=0));',
 'qlineEquations={qlCoefficients#0,qlCoefficients#1};',
 'collisionBoundary=((omega+1)*ee-ff-omega)*(ee^2-ff);',
 'collisionIdeal=ideal join(firstEquations,qlineEquations,{endpointUnit});',
 'print "ONE_PAIR_COLLISION_9VAR_MODEL_READY";',
 '-- Necessity on ff*collisionBoundary !=0. The boundary needs separate charts.',
 '-- No Groebner basis is run by this exporter.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
out={'status':'new exact collision chart; no emptiness assertion',
     'accepted_first_input_sha256':hashlib.sha256(accepted.read_bytes()).hexdigest(),
     'D':'(z-1)(z-omega)(z^2+e*z+f)',
     'normalization':'torus fixes one collision root to1; projective f scale makesDmonic',
     'symbol_kernel':'(v0,v1,v2)=lambda*(-f,e,1)',
     'deviation_coordinates':'v0=y0+d1/4,v1=y1-4t+d2/2,v2=y2+d3/4',
     'rank_drop_boundary':'S=((omega+1)*e-f-omega)*(e^2-f)',
     'boundary_meanings':['first factor: complete orbit {1,omega,omega^2}',
                          'second factor: residual quadratic itself is a mu3 pair'],
     'qline_condition':'On f*S!=0, exact norm-alpha qline condition is rem_(z^2+e*z+f)(Dprime-12*z^2*G)=0, two equations',
     'variables':['e','f','lambda','t','H4','H5','H6','H7','fInverse'],
     'h_elimination':'Eight accepted first equations solve h0..3,h8..11 usinga2=1,c0=omega*f/4. f*fInverse=1 retains all endpoint-nonzero points.',
     'limitations':'Endpointzero, completeorbit and two-pair boundary separately retained; no globalpair claim.'}
stem.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'model':str(stem.with_suffix('.m2')),'variables':9,'qline_equations':2},indent=2))
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_nodal_normalization_2026_10_21.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- New finite-normalization audit of the LOCAL nodal caution family only.
-- It does not construct homogeneous global coefficients or a supported pair.
R=QQ[t,z,w,v];
scan(1..4,n->(
    m:=10-2*n;
    d:=z-t^n;
    e:=z-t^m;
    f:=z*w^2-d^2*e;
    J:=ideal(v^2-z*e,z*w-d*v,v*w-d*e);
    assert(dim(R/J)==2);
    -- Hilbert--Burch: these are all 2x2 minors of a 2x3 matrix,
    -- and height two gives CM. Do not use the length of M2's
    -- nonminimal inhomogeneous resolution as a CM test.
    assert(J==minors(2,matrix{{z,v,d},{v,e,w}}));
    assert(dim(R/(J+ideal(z)))==1);
    -- On z!=0 this is the integral double cover v^2=z(z-t^m).
    -- Hence CM + dimension drop gives an integral ring.
    assert(dim(R/(J+minors(2,jacobian gens J)))==0);
    -- R1 + CM gives normality. v is monic-integral over the original ring.
    assert(eliminate(J,{v})==ideal(f));
    conductor:=J+ideal(d,w);
    expected:=ideal(z-t^n,w,v^2-t^n*(t^n-t^m));
    assert(conductor==expected);
    print("LOCAL_NODAL_FINITE_NORMALIZATION n="|toString n|", m="|toString m|": PASS");
    print("CONDUCTOR_EQUATION: "|toString(v^2-t^n*(t^n-t^m)));
    ));
print("NO_GLOBAL_SEXTIC_OR_PAIR_ASSERTED");
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_primitive.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- Exact primitive-cube-root line component over QQ(w), w^2+w+1=0.
K=toField(QQ[ww]/ideal(ww^2+ww+1));
R=K[h4,h5,h6,h7,a,x,MonomialOrder=>Eliminate 4];
w=sub(K_0,R);
firstEquations={1/2*a-1/2*x-8*w*x-w*h6-1/2*w*w*a-1/2*w*w*x-w*a*h7+w*x*h7-1/4*a*a*a+7/4*a*a*x-11/4*a*x*x+5/4*x*x*x+w*w*a*h7+w*w*x*h7+5/2*w*a*a*x-5/2*w*x*x*x-a*a*a*h4-3*a*a*x*h4-3*a*x*x*h4-x*x*x*h4+1/4*w*w*a*a*a+7/4*w*w*a*a*x+11/4*w*w*a*x*x+5/4*w*w*x*x*x+w*a*a*a*h4+1/2*w*a*a*a*h7-3*w*a*a*x*h4-1/2*w*a*a*x*h7+3*w*a*x*x*h4-1/2*w*a*x*x*h7-w*x*x*x*h4+1/2*w*x*x*x*h7-a*a*a*a*h5-2*a*a*a*x*h5+2*a*x*x*x*h5+x*x*x*x*h5-1/2*w*w*a*a*a*h7-1/2*w*w*a*a*x*h7+1/2*w*w*a*x*x*h7+1/2*w*w*x*x*x*h7+1/4*w*a*a*a*a*h6-1/2*w*a*a*x*x*h6+1/4*w*x*x*x*x*h6+1/2*a*a*a*a*a*h4+3/2*a*a*a*a*x*h4+a*a*a*x*x*h4-a*a*x*x*x*h4-3/2*a*x*x*x*x*h4-1/2*x*x*x*x*x*h4-w*w*a*a*a*a*h5+2*w*w*a*a*a*x*h5-2*w*w*a*x*x*x*h5+w*w*x*x*x*x*h5-1/2*w*a*a*a*a*a*h4+3/2*w*a*a*a*a*x*h4-w*a*a*a*x*x*h4-w*a*a*x*x*x*h4+3/2*w*a*x*x*x*x*h4-1/2*w*x*x*x*x*x*h4+1/2*a*a*a*a*a*a*h5+a*a*a*a*a*x*h5-1/2*a*a*a*a*x*x*h5-2*a*a*a*x*x*x*h5-1/2*a*a*x*x*x*x*h5+a*x*x*x*x*x*h5+1/2*x*x*x*x*x*x*h5+1/2*w*w*a*a*a*a*a*a*h5-w*w*a*a*a*a*a*x*h5-1/2*w*w*a*a*a*a*x*x*h5+2*w*w*a*a*a*x*x*x*h5-1/2*w*w*a*a*x*x*x*x*h5-w*w*a*x*x*x*x*x*h5+1/2*w*w*x*x*x*x*x*x*h5,1/2+1/2*w-w*h7-1/4*a*a+3/2*a*x-5/4*x*x-1/4*w*a*a-3/2*w*a*x-5/4*w*x*x-1/2*a*a*h7+a*x*h7-1/2*x*x*h7-3*w*w*x*x-w*a*a*h4+w*a*a*h7+2*w*a*x*h4-w*x*x*h4-w*x*x*h7-1/4*a*a*a*h6+1/4*a*a*x*h6+1/4*a*x*x*h6-1/4*x*x*x*h6-w*w*a*a*h4-1/2*w*w*a*a*h7-2*w*w*a*x*h4-w*w*a*x*h7-w*w*x*x*h4-1/2*w*w*x*x*h7+1/4*w*a*a*a*h6+1/4*w*a*a*x*h6-1/4*w*a*x*x*h6-1/4*w*x*x*x*h6+1/4*a*a*a*a*h7-1/2*a*a*a*x*h7+1/2*a*x*x*x*h7-1/4*x*x*x*x*h7-2*w*w*a*a*x*h5+2*w*w*x*x*x*h5+1/2*w*a*a*a*a*h4-1/4*w*a*a*a*a*h7-w*a*a*a*x*h4+1/2*w*a*a*x*x*h7+w*a*x*x*x*h4-1/2*w*x*x*x*x*h4-1/4*w*x*x*x*x*h7+1/8*a*a*a*a*a*h6-1/8*a*a*a*a*x*h6-1/4*a*a*a*x*x*h6+1/4*a*a*x*x*x*h6+1/8*a*x*x*x*x*h6-1/8*x*x*x*x*x*h6+1/2*w*w*a*a*a*a*h4+1/4*w*w*a*a*a*a*h7+w*w*a*a*a*x*h4+1/2*w*w*a*a*a*x*h7-w*w*a*x*x*x*h4-1/2*w*w*a*x*x*x*h7-1/2*w*w*x*x*x*x*h4-1/4*w*w*x*x*x*x*h7-1/8*w*a*a*a*a*a*h6-1/8*w*a*a*a*a*x*h6+1/4*w*a*a*a*x*x*h6+1/4*w*a*a*x*x*x*h6-1/8*w*a*x*x*x*x*h6-1/8*w*x*x*x*x*x*h6+w*w*a*a*a*a*x*h5-2*w*w*a*a*x*x*x*h5+w*w*x*x*x*x*x*h5,-1/4*w*a+7/4*w*x-1/2*a*h7+1/2*x*h7+1/4*w*w*a+7/4*w*w*x+1/2*w*a*h7-2*w*x*h4+1/2*w*x*h7-1/4*a*a*h6+1/4*x*x*h6+1/8*w*a*a*a+5/8*w*a*a*x-w*a*a*h5-1/8*w*a*x*x-5/8*w*x*x*x+w*x*x*h5+1/2*a*a*a*h7-1/2*a*a*x*h7-1/2*a*x*x*h7+1/2*x*x*x*h7-1/8*w*w*a*a*a+5/8*w*w*a*a*x-w*w*a*a*h5+1/8*w*w*a*x*x-5/8*w*w*x*x*x+w*w*x*x*h5-1/2*w*a*a*a*h7+w*a*a*x*h4-1/2*w*a*a*x*h7+1/2*w*a*x*x*h7-w*x*x*x*h4+1/2*w*x*x*x*h7+1/4*a*a*a*a*h6-1/2*a*a*x*x*h6+1/4*x*x*x*x*h6+3/2*w*w*a*a*x*h7+1/2*w*w*x*x*x*h7+1/2*w*a*a*a*a*h5-1/8*w*a*a*a*a*h6-1/4*w*a*a*a*x*h6-w*a*a*x*x*h5+1/4*w*a*x*x*x*h6+1/2*w*x*x*x*x*h5+1/8*w*x*x*x*x*h6-1/8*a*a*a*a*a*h7+1/8*a*a*a*a*x*h7+1/4*a*a*a*x*x*h7-1/4*a*a*x*x*x*h7-1/8*a*x*x*x*x*h7+1/8*x*x*x*x*x*h7+1/2*w*w*a*a*a*a*h5-1/8*w*w*a*a*a*a*h6+1/4*w*w*a*a*a*x*h6-w*w*a*a*x*x*h5-1/4*w*w*a*x*x*x*h6+1/2*w*w*x*x*x*x*h5+1/8*w*w*x*x*x*x*h6+1/8*w*a*a*a*a*a*h7+1/8*w*a*a*a*a*x*h7-1/4*w*a*a*a*x*x*h7-1/4*w*a*a*x*x*x*h7+1/8*w*a*x*x*x*x*h7+1/8*w*x*x*x*x*x*h7-1/16*a*a*a*a*a*a*h6+3/16*a*a*a*a*x*x*h6-3/16*a*a*x*x*x*x*h6+1/16*x*x*x*x*x*x*h6-3/4*w*w*a*a*a*a*x*h7+1/2*w*w*a*a*x*x*x*h7+1/4*w*w*x*x*x*x*x*h7+1/16*w*a*a*a*a*a*a*h6+1/8*w*a*a*a*a*a*x*h6-1/16*w*a*a*a*a*x*x*h6-1/4*w*a*a*a*x*x*x*h6-1/16*w*a*a*x*x*x*x*h6+1/8*w*a*x*x*x*x*x*h6+1/16*w*x*x*x*x*x*x*h6+1/16*w*w*a*a*a*a*a*a*h6-1/8*w*w*a*a*a*a*a*x*h6-1/16*w*w*a*a*a*a*x*x*h6+1/4*w*w*a*a*a*x*x*x*h6-1/16*w*w*a*a*x*x*x*x*h6-1/8*w*w*a*x*x*x*x*x*h6+1/16*w*w*x*x*x*x*x*x*h6,-1/2*w-h4-w*h4-1/2*a*a-1/2*a*x-a*h5+x*x+x*h5+1/4*w*a*a+5/4*w*x*x+1/2*a*a*h4+1/4*a*a*h7-1/2*x*x*h4-1/4*x*x*h7-1/2*w*w*a*a+1/2*w*w*a*x+w*w*a*h5+w*w*x*x+w*w*x*h5+1/2*w*a*a*h4-1/4*w*a*a*h7-1/2*w*a*x*h7-1/2*w*x*x*h4-1/4*w*x*x*h7+1/16*a*a*a*a+1/4*a*a*a*x+1/2*a*a*a*h5+1/8*a*a*a*h6-3/8*a*a*x*x-1/2*a*a*x*h5+1/8*a*a*x*h6-1/4*a*x*x*x-1/2*a*x*x*h5-1/8*a*x*x*h6+5/16*x*x*x*x+1/2*x*x*x*h5-1/8*x*x*x*h6-1/4*w*w*a*a*h7+1/2*w*w*a*x*h7-1/4*w*w*x*x*h7-1/4*a*a*a*a*h7+1/2*a*a*x*x*h7-1/4*x*x*x*x*h7+1/16*w*w*a*a*a*a-1/4*w*w*a*a*a*x-1/2*w*w*a*a*a*h5-1/8*w*w*a*a*a*h6-3/8*w*w*a*a*x*x-1/2*w*w*a*a*x*h5+1/8*w*w*a*a*x*h6+1/4*w*w*a*x*x*x+1/2*w*w*a*x*x*h5+1/8*w*w*a*x*x*h6+5/16*w*w*x*x*x*x+1/2*w*w*x*x*x*h5-1/8*w*w*x*x*x*h6+1/8*w*a*a*a*a*h7+w*a*a*a*x*h7-3/4*w*a*a*x*x*h7-3/8*w*x*x*x*x*h7-1/8*a*a*a*a*a*h6-1/8*a*a*a*a*x*h6+1/4*a*a*a*x*x*h6+1/4*a*a*x*x*x*h6-1/8*a*x*x*x*x*h6-1/8*x*x*x*x*x*h6+1/8*w*w*a*a*a*a*h7-w*w*a*a*a*x*h7-3/4*w*w*a*a*x*x*h7-3/8*w*w*x*x*x*x*h7+3/8*w*a*a*a*a*x*h6-1/4*w*a*a*x*x*x*h6-1/8*w*x*x*x*x*x*h6+1/16*a*a*a*a*a*a*h7-3/16*a*a*a*a*x*x*h7+3/16*a*a*x*x*x*x*h7-1/16*x*x*x*x*x*x*h7+1/8*w*w*a*a*a*a*a*h6-1/8*w*w*a*a*a*a*x*h6-1/4*w*w*a*a*a*x*x*h6+1/4*w*w*a*a*x*x*x*h6+1/8*w*w*a*x*x*x*x*h6-1/8*w*w*x*x*x*x*x*h6-3/8*w*a*a*a*a*a*x*h7+3/8*w*a*a*a*a*x*x*h7+1/4*w*a*a*a*x*x*x*h7-1/4*w*a*a*x*x*x*x*h7+1/8*w*a*x*x*x*x*x*h7-1/8*w*x*x*x*x*x*x*h7+1/32*a*a*a*a*a*a*a*h6+1/32*a*a*a*a*a*a*x*h6-3/32*a*a*a*a*a*x*x*h6-3/32*a*a*a*a*x*x*x*h6+3/32*a*a*a*x*x*x*x*h6+3/32*a*a*x*x*x*x*x*h6-1/32*a*x*x*x*x*x*x*h6-1/32*x*x*x*x*x*x*x*h6+3/8*w*w*a*a*a*a*a*x*h7+3/8*w*w*a*a*a*a*x*x*h7-1/4*w*w*a*a*a*x*x*x*h7-1/4*w*w*a*a*x*x*x*x*h7-1/8*w*w*a*x*x*x*x*x*h7-1/8*w*w*x*x*x*x*x*x*h7-3/16*w*a*a*a*a*a*a*x*h6+5/16*w*a*a*a*a*x*x*x*h6-1/16*w*a*a*x*x*x*x*x*h6-1/16*w*x*x*x*x*x*x*x*h6-1/32*w*w*a*a*a*a*a*a*a*h6+1/32*w*w*a*a*a*a*a*a*x*h6+3/32*w*w*a*a*a*a*a*x*x*h6-3/32*w*w*a*a*a*a*x*x*x*h6-3/32*w*w*a*a*a*x*x*x*x*h6+3/32*w*w*a*a*x*x*x*x*x*h6+1/32*w*w*a*x*x*x*x*x*x*h6-1/32*w*w*x*x*x*x*x*x*x*h6,1-h7-w*h7-1/2*a*a-5/2*x*x+w*a*a-w*a*x-1/2*w*a*h6-2*w*x*x-1/2*w*x*h6-a*a*h4+1/2*a*a*h7+2*a*x*h4-x*x*h4-1/2*x*x*h7+w*w*a*a+w*w*a*x+1/2*w*w*a*h6-2*w*w*x*x-1/2*w*w*x*h6+w*a*a*h4+1/2*w*a*a*h7-w*x*x*h4-1/2*w*x*x*h7-w*w*a*a*h4-2*w*w*a*x*h4-w*w*x*x*h4-1/8*w*a*a*a*a+1/2*w*a*a*a*x+w*a*a*a*h5+1/4*w*a*a*a*h6+3/4*w*a*a*x*x-w*a*a*x*h5+1/4*w*a*a*x*h6-1/2*w*a*x*x*x-w*a*x*x*h5-1/4*w*a*x*x*h6-5/8*w*x*x*x*x+w*x*x*x*h5-1/4*w*x*x*x*h6+1/2*a*a*a*a*h4-4*a*a*a*x*h4-3*a*a*x*x*h4-3/2*x*x*x*x*h4-1/8*w*w*a*a*a*a-1/2*w*w*a*a*a*x-w*w*a*a*a*h5-1/4*w*w*a*a*a*h6+3/4*w*w*a*a*x*x-w*w*a*a*x*h5+1/4*w*w*a*a*x*h6+1/2*w*w*a*x*x*x+w*w*a*x*x*h5+1/4*w*w*a*x*x*h6-5/8*w*w*x*x*x*x+w*w*x*x*x*h5-1/4*w*w*x*x*x*h6-w*a*a*a*a*h4+2*w*a*a*x*x*h4-w*x*x*x*x*h4-3*a*a*a*a*x*h5+2*a*a*x*x*x*h5+x*x*x*x*x*h5+1/2*w*w*a*a*a*a*h4+4*w*w*a*a*a*x*h4-3*w*w*a*a*x*x*h4-3/2*w*w*x*x*x*x*h4-w*a*a*a*a*a*h5+w*a*a*a*a*x*h5+2*w*a*a*a*x*x*h5-2*w*a*a*x*x*x*h5-w*a*x*x*x*x*h5+w*x*x*x*x*x*h5+3/2*a*a*a*a*a*x*h4+3/2*a*a*a*a*x*x*h4-a*a*a*x*x*x*h4-a*a*x*x*x*x*h4-1/2*a*x*x*x*x*x*h4-1/2*x*x*x*x*x*x*h4+w*w*a*a*a*a*a*h5+w*w*a*a*a*a*x*h5-2*w*w*a*a*a*x*x*h5-2*w*w*a*a*x*x*x*h5+w*w*a*x*x*x*x*h5+w*w*x*x*x*x*x*h5+1/4*w*a*a*a*a*a*a*h4-3/4*w*a*a*a*a*x*x*h4+3/4*w*a*a*x*x*x*x*h4-1/4*w*x*x*x*x*x*x*h4+3/2*a*a*a*a*a*a*x*h5-5/2*a*a*a*a*x*x*x*h5+1/2*a*a*x*x*x*x*x*h5+1/2*x*x*x*x*x*x*x*h5-3/2*w*w*a*a*a*a*a*x*h4+3/2*w*w*a*a*a*a*x*x*h4+w*w*a*a*a*x*x*x*h4-w*w*a*a*x*x*x*x*h4+1/2*w*w*a*x*x*x*x*x*h4-1/2*w*w*x*x*x*x*x*x*h4+1/4*w*a*a*a*a*a*a*a*h5-1/4*w*a*a*a*a*a*a*x*h5-3/4*w*a*a*a*a*a*x*x*h5+3/4*w*a*a*a*a*x*x*x*h5+3/4*w*a*a*a*x*x*x*x*h5-3/4*w*a*a*x*x*x*x*x*h5-1/4*w*a*x*x*x*x*x*x*h5+1/4*w*x*x*x*x*x*x*x*h5-1/4*w*w*a*a*a*a*a*a*a*h5-1/4*w*w*a*a*a*a*a*a*x*h5+3/4*w*w*a*a*a*a*a*x*x*h5+3/4*w*w*a*a*a*a*x*x*x*h5-3/4*w*w*a*a*a*x*x*x*x*h5-3/4*w*w*a*a*x*x*x*x*x*h5+1/4*w*w*a*x*x*x*x*x*x*h5+1/4*w*w*x*x*x*x*x*x*x*h5,1/4*a+7/4*x+a*h4-x*h4+x*h7-1/4*w*w*a+7/4*w*w*x-w*a*h4-w*x*h4-1/8*a*a*a+5/8*a*a*x-1/4*a*a*h6+1/8*a*x*x-5/8*x*x*x+1/4*x*x*h6-w*a*a*h5+w*x*x*h5-a*a*a*h4+a*a*x*h4-1/2*a*a*x*h7+a*x*x*h4-x*x*x*h4+1/2*x*x*x*h7+1/8*w*w*a*a*a+5/8*w*w*a*a*x-1/4*w*w*a*a*h6-1/8*w*w*a*x*x-5/8*w*w*x*x*x+1/4*w*w*x*x*h6+w*a*a*a*h4+w*a*a*x*h4-w*a*x*x*h4-w*x*x*x*h4-1/2*a*a*a*a*h5+1/8*a*a*a*a*h6+a*a*a*x*h5-1/4*a*a*x*x*h6-a*x*x*x*h5+1/2*x*x*x*x*h5+1/8*x*x*x*x*h6-3*w*w*a*a*x*h4-w*w*x*x*x*h4+w*a*a*a*a*h5-2*w*a*a*x*x*h5+w*x*x*x*x*h5+1/4*a*a*a*a*a*h4-1/4*a*a*a*a*x*h4-1/2*a*a*a*x*x*h4+1/2*a*a*x*x*x*h4+1/4*a*x*x*x*x*h4-1/4*x*x*x*x*x*h4-1/2*w*w*a*a*a*a*h5+1/8*w*w*a*a*a*a*h6-w*w*a*a*a*x*h5-1/4*w*w*a*a*x*x*h6+w*w*a*x*x*x*h5+1/2*w*w*x*x*x*x*h5+1/8*w*w*x*x*x*x*h6-1/4*w*a*a*a*a*a*h4-1/4*w*a*a*a*a*x*h4+1/2*w*a*a*a*x*x*h4+1/2*w*a*a*x*x*x*h4-1/4*w*a*x*x*x*x*h4-1/4*w*x*x*x*x*x*h4+1/4*a*a*a*a*a*a*h5-1/2*a*a*a*a*a*x*h5-1/4*a*a*a*a*x*x*h5+a*a*a*x*x*x*h5-1/4*a*a*x*x*x*x*h5-1/2*a*x*x*x*x*x*h5+1/4*x*x*x*x*x*x*h5+3/2*w*w*a*a*a*a*x*h4-w*w*a*a*x*x*x*h4-1/2*w*w*x*x*x*x*x*h4-1/4*w*a*a*a*a*a*a*h5+3/4*w*a*a*a*a*x*x*h5-3/4*w*a*a*x*x*x*x*h5+1/4*w*x*x*x*x*x*x*h5+1/4*w*w*a*a*a*a*a*a*h5+1/2*w*w*a*a*a*a*a*x*h5-1/4*w*w*a*a*a*a*x*x*h5-w*w*a*a*a*x*x*x*h5-1/4*w*w*a*a*x*x*x*x*h5+1/2*w*w*a*x*x*x*x*x*h5+1/4*w*w*x*x*x*x*x*x*h5,-1/4-1/4*w-h4+1/8*a*a-3/4*a*x+5/8*x*x+1/8*w*a*a+3/4*w*a*x+5/8*w*x*x+a*a*h4-1/4*a*a*h7-1/2*a*x*h7-x*x*h4-1/4*x*x*h7+3/2*w*w*x*x-1/2*w*a*a*h4-w*a*x*h4-1/2*w*x*x*h4+1/2*a*a*a*h5-1/2*a*a*x*h5-1/2*a*x*x*h5+1/2*x*x*x*h5-1/2*w*w*a*a*h4-1/4*w*w*a*a*h7+w*w*a*x*h4+1/2*w*w*a*x*h7-1/2*w*w*x*x*h4-1/4*w*w*x*x*h7-1/2*w*a*a*a*h5-1/2*w*a*a*x*h5+1/2*w*a*x*x*h5+1/2*w*x*x*x*h5-1/4*a*a*a*a*h4+1/8*a*a*a*a*h7+1/4*a*a*a*x*h7+1/2*a*a*x*x*h4-1/4*a*x*x*x*h7-1/4*x*x*x*x*h4-1/8*x*x*x*x*h7+1/4*w*w*a*a*x*h6-1/4*w*w*x*x*x*h6+1/4*w*a*a*a*a*h4+1/2*w*a*a*a*x*h4-1/2*w*a*x*x*x*h4-1/4*w*x*x*x*x*h4-1/4*a*a*a*a*a*h5+1/4*a*a*a*a*x*h5+1/2*a*a*a*x*x*h5-1/2*a*a*x*x*x*h5-1/4*a*x*x*x*x*h5+1/4*x*x*x*x*x*h5+1/4*w*w*a*a*a*a*h4+1/8*w*w*a*a*a*a*h7-1/2*w*w*a*a*a*x*h4-1/4*w*w*a*a*a*x*h7+1/2*w*w*a*x*x*x*h4+1/4*w*w*a*x*x*x*h7-1/4*w*w*x*x*x*x*h4-1/8*w*w*x*x*x*x*h7+1/4*w*a*a*a*a*a*h5+1/4*w*a*a*a*a*x*h5-1/2*w*a*a*a*x*x*h5-1/2*w*a*a*x*x*x*h5+1/4*w*a*x*x*x*x*h5+1/4*w*x*x*x*x*x*h5-1/8*w*w*a*a*a*a*x*h6+1/4*w*w*a*a*x*x*x*h6-1/8*w*w*x*x*x*x*x*h6,-2*x-h5-1/8*w*a-1/8*w*x-1/2*a*h4-1/2*x*h4+1/8*w*w*a-1/8*w*w*x+5/8*a*a*x-5/8*x*x*x+1/2*w*w*a*h4-1/2*w*w*x*h4+1/16*w*a*a*a+7/16*w*a*a*x+11/16*w*a*x*x+5/16*w*x*x*x+1/4*a*a*a*h4+1/8*a*a*a*h7+1/4*a*a*x*h4+3/8*a*a*x*h7-1/4*a*x*x*h4+3/8*a*x*x*h7-1/4*x*x*x*h4+1/8*x*x*x*h7-1/16*w*w*a*a*a+7/16*w*w*a*a*x-11/16*w*w*a*x*x+5/16*w*w*x*x*x-1/8*w*a*a*a*h7+3/8*w*a*a*x*h7-3/8*w*a*x*x*h7+1/8*w*x*x*x*h7+1/4*a*a*a*a*h5-1/2*a*a*x*x*h5+1/4*x*x*x*x*h5-1/4*w*w*a*a*a*h4+1/4*w*w*a*a*x*h4+1/4*w*w*a*x*x*h4-1/4*w*w*x*x*x*h4-1/16*w*a*a*a*a*h6+1/8*w*a*a*a*x*h6-1/8*w*a*x*x*x*h6+1/16*w*x*x*x*x*h6-1/16*a*a*a*a*a*h7-3/16*a*a*a*a*x*h7-1/8*a*a*a*x*x*h7+1/8*a*a*x*x*x*h7+3/16*a*x*x*x*x*h7+1/16*x*x*x*x*x*h7-1/16*w*w*a*a*a*a*h6-1/8*w*w*a*a*a*x*h6+1/8*w*w*a*x*x*x*h6+1/16*w*w*x*x*x*x*h6+1/16*w*a*a*a*a*a*h7-3/16*w*a*a*a*a*x*h7+1/8*w*a*a*a*x*x*h7+1/8*w*a*a*x*x*x*h7-3/16*w*a*x*x*x*x*h7+1/16*w*x*x*x*x*x*h7+1/32*w*a*a*a*a*a*a*h6-1/16*w*a*a*a*a*a*x*h6-1/32*w*a*a*a*a*x*x*h6+1/8*w*a*a*a*x*x*x*h6-1/32*w*a*a*x*x*x*x*h6-1/16*w*a*x*x*x*x*x*h6+1/32*w*x*x*x*x*x*x*h6+1/32*w*w*a*a*a*a*a*a*h6+1/16*w*w*a*a*a*a*a*x*h6-1/32*w*w*a*a*a*a*x*x*h6-1/8*w*w*a*a*a*x*x*x*h6-1/32*w*w*a*a*x*x*x*x*h6+1/16*w*w*a*x*x*x*x*x*h6+1/32*w*w*x*x*x*x*x*x*h6};
I=ideal firstEquations;
print("PRIMITIVE_LINE_FIRST_ELIMINATION_START");
E=eliminate({h4,h5,h6,h7},I);
print("PRIMITIVE_LINE_FIRST_ELIMINATION_READY");print gens E;
S=K[a,x];phi=map(S,R,{0,0,0,0,a,x});
ES=ideal phi(gens E);w=sub(K_0,S);
tau=w^2*(1-a^2-x^2);delta=w*((a^2-x^2-2)/2)^2;
q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);
op=a*(2*x^2+1)*(a^2-x^2-2)*(2*a^2-3);
J=saturate(ES+ideal(q),ideal(op));
print("PRIMITIVE_LINE_FIRST_TORSION_RESULT");print gens gb J;
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_w1.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- Exact w=1,y=x generic norm component, p=a^2; p nonzero.
R=QQ[h4,h5,h6,h7,p,x,MonomialOrder=>Eliminate 4];
firstEquations={-h6-9*x+2*h7*x+6*p*x-6*h4*p*x-2*h5*p*p+1/4*h6*p*p-h7*p*x+3*h4*p*p*x-2*h4*x*x*x+h5*p*p*p-1/2*h6*p*x*x+h7*x*x*x-2*h4*p*x*x*x-h5*p*p*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-h5*p*x*x*x*x+h5*x*x*x*x*x*x,1-h7-1/2*p-2*h4*p-11/2*x*x+h4*p*p-2*h4*x*x-2*h5*p*x+1/2*h6*p*x+1/4*h7*p*p-2*h7*x*x+h5*p*p*x+2*h5*x*x*x-1/4*h6*p*p*x-1/2*h6*x*x*x+1/2*h7*p*x*x-h4*x*x*x*x-2*h5*p*x*x*x+1/2*h6*p*x*x*x-3/4*h7*x*x*x*x+h5*x*x*x*x*x-1/4*h6*x*x*x*x*x,7/2*x-2*h4*x-2*h5*p-1/4*h6*p+h7*x+5/4*p*x+h4*p*x+h5*p*p+2*h5*x*x+1/4*h6*x*x+1/2*h7*p*x-5/4*x*x*x-h4*x*x*x-2*h5*p*x*x+1/16*h6*p*p*p-1/2*h6*p*x*x-1/2*h7*p*p*x+3/2*h7*x*x*x+h5*x*x*x*x+1/16*h6*p*p*x*x+1/2*h6*x*x*x*x-5/16*h6*p*x*x*x*x+1/2*h7*x*x*x*x*x+3/16*h6*x*x*x*x*x*x,-1/2-2*h4-3/4*p+h4*p+2*h5*x-1/4*h7*p+1/8*p*p+13/4*x*x-h4*x*x-h5*p*x+1/4*h6*p*x-3/4*h7*x*x-3/4*p*x*x+h5*x*x*x+1/8*h6*p*p*x-1/4*h6*x*x*x+1/16*h7*p*p*p-h7*p*x*x+5/8*x*x*x*x-1/8*h6*p*p*p*x+1/4*h6*p*x*x*x+9/16*h7*p*p*x*x-h7*x*x*x*x+1/8*h6*p*p*x*x*x-3/8*h6*x*x*x*x*x-5/16*h7*p*x*x*x*x+1/8*h6*p*x*x*x*x*x-5/16*h7*x*x*x*x*x*x-1/8*h6*x*x*x*x*x*x*x,1-2*h7+3/2*p-h4*p-h6*x+h7*p-1/4*p*p-13/2*x*x-3*h4*x*x-2*h5*p*x+1/2*h6*p*x-h7*x*x+3/2*p*x*x+1/4*h4*p*p*p-4*h4*p*x*x-h5*p*p*x+2*h5*x*x*x-1/2*h6*x*x*x-5/4*x*x*x*x+9/4*h4*p*p*x*x-4*h4*x*x*x*x+h5*p*p*p*x-2*h5*p*x*x*x-5/4*h4*p*x*x*x*x-h5*p*p*x*x*x+3*h5*x*x*x*x*x-5/4*h4*x*x*x*x*x*x-h5*p*x*x*x*x*x+h5*x*x*x*x*x*x*x,7/2*x-2*h4*x-h5*p-1/2*h6*p+h7*x+5/4*p*x-h4*p*x+h5*x*x+1/4*h6*p*p+1/2*h6*x*x-1/2*h7*p*x-5/4*x*x*x+h4*p*p*x-3*h4*x*x*x+1/4*h5*p*p*p-2*h5*p*x*x-1/2*h6*p*x*x+1/2*h7*x*x*x+1/4*h5*p*p*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-5/4*h5*p*x*x*x*x+3/4*h5*x*x*x*x*x*x,-1/2-h4+1/4*p-1/2*h7*p+11/4*x*x+1/4*h4*p*p-2*h4*x*x-h5*p*x+1/4*h6*p*x+1/4*h7*p*p-1/2*h7*x*x+1/2*h4*p*x*x+1/2*h5*p*p*x+h5*x*x*x-1/8*h6*p*p*x-1/4*h6*x*x*x-3/4*h4*x*x*x*x-h5*p*x*x*x+1/4*h6*p*x*x*x-1/4*h7*x*x*x*x+1/2*h5*x*x*x*x*x-1/8*h6*x*x*x*x*x,-h5-9/4*x-h4*x+3/2*p*x+1/2*h4*p*x+1/4*h5*p*p-1/8*h6*p*p+3/4*h7*p*x-1/2*h4*x*x*x-1/2*h5*p*x*x+1/16*h6*p*p*p-3/8*h7*p*p*x+1/4*h7*x*x*x+1/4*h5*x*x*x*x-1/16*h6*p*p*x*x+1/8*h6*x*x*x*x+1/4*h7*p*x*x*x-1/16*h6*p*x*x*x*x+1/8*h7*x*x*x*x*x+1/16*h6*x*x*x*x*x*x};
I=ideal firstEquations;
print("W1_LINE_FIRST_ELIMINATION_START");
E=eliminate({h4,h5,h6,h7},I);
print("W1_LINE_FIRST_ELIMINATION_READY");print gens E;
S=QQ[p,x];phi=map(S,R,{0,0,0,0,p,x});
ES=ideal phi(gens E);
tau=-(p+x^2+2);delta=((p-x^2-2)/2)^2;
q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);
op=p*(2*x^2+1)*(p-x^2-2)*(x^2+2);
J=saturate(ES+ideal(q),ideal(op));
print("W1_LINE_FIRST_TORSION_RESULT");print gens gb J;
```
</details>
