# The regular L1 rational branch has an exact double conductor root

Date: 2026-10-13. Author: `oct12_restricted_conductor_section/residual_norm_identity`.

Status: **DIRECT EXACT DOUBLE-ROOT IDENTITY FOR A SPECIFIED FAMILY;
INDEPENDENT AUDIT REQUESTED**. The actual-conductor identification is
inherited from the
[independent module audit](2026-10-12-session-conductor-quadric-module-independent-audit.md).
The separate quotient-fiber argument owns the claim that this rational
family is the surviving regular L1 branch under full inverse support.
No full common-root incidence exhaustion or global STCI result is claimed.
All older sources and notes remain unchanged.

Use the finite common-root parameters and exact coefficients of the
[Taylor incidence note](2026-10-13-session-nonendpoint-single-root-taylor-incidence.md):

    F(q+t)=t(u0+u1 t+...+u7 t^7),
    kappa=aq+B, Pc=q^2-6q+6.

Consider the explicit rational family

    delta=Pc(q-2)/[q(q-1)],
    kappa=delta+delta^2(2q-3)/[3(q-1)(q-2)],
    B=kappa-aq, G=Gs, J=Js,                         (1)

where Gs,Js are the complete common-root solutions in that note. Retain

    q(q-1)(q-2)Pc!=0.                              (2)

These are actual relations among projection parameters; delta is not
normalized to one. The conditions retain the modulus and every forbidden
denominator. They ensure delta is nonzero and the regular fiber denominator
does not vanish: on (1),

    U=q(kappa-delta)-delta^2
      =-delta^2 Pc/[3(q-1)(q-2)]!=0,
    Z(q)=q Pc U!=0.                                (3)

Exact substitution into the two frozen coefficient polynomials gives

    u0=0,
    u1=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.              (4)

The second expression is independent of a. Its nonvanishing follows
from the explicitly retained factors (2); there is no numerical sampling
or Gröbner calculation. The underlying common-root substitution already
gives F(q)=0. Thus the actual conductor restriction has exactly order
two at q for every admissible projection in (1)--(2). This is a literal
coefficient calculation of its actual section, rather than a contact
bound inferred from a first-normal symbol.

In particular, if J!=0 and q is the sole common homogeneous conormal
root, full inverse support would force the entire degree-eight conductor
restriction to be supported at q. Its order two from (4) contradicts
that requirement. Hence the explicitly specified single-common-root
family cannot have a mate in any degree. Applying this consequence to
every regular L1 case also requires the separately justified quotient-
fiber necessity of (1), including its degree-drop case; that proof is
not replaced by this computation.

The [three-check source](../computations/verify_session_nonendpoint_regular_l1_double_root_2026_10_13.m2)
reads only the frozen u0,u1 polynomial artifacts and verifies both
identities (4) and the exact fiber-rank expression (3). It does not replay
the fifteen-check determinant source, the endpoint proof or the complete
Taylor expansion. Its
[20261013T142957009441Z captured run](../validation/2026-10-13-nonendpoint-regular-l1-taylor-branch/20261013T142957009441Z/execution-record.json)
has three supporting checks, a completion marker, exit zero and empty
stderr. Source SHA-256 is
`b223eb5e4e063bbbe3273ac4b82a2e98317412b5c92149fa692218180e217074`.

The earlier exploratory source evaluated u1,u2,u3,u7. It found (4),
and merely found the remaining displayed coefficients to be linear in
a after the same branch substitution. They are unnecessary for the
double-root obstruction and are retained as exploratory continuation
artifacts. That execution is not a parameter-space exhaustion.
