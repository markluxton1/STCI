# Endpoint trisecant with irreducible residual conductor: conditional exclusion

Date: 2026-10-10. Author: `trisecant_conic_obstruction`.
Status: **PROVED HERE CONDITIONALLY / independent audit pending**.
This note excludes only the irreducible residual `(1,2)` divisor
at an endpoint trisecant. The reducible and nonreduced endpoint
residual divisors remain outside its scope. No canonical file is edited.

Use exactly the conditional structural inputs and lambda-one mate
inputs in section 1 of
[the nonendpoint obstruction](2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstruction.md).
In particular the actual strict transform T in the blowup of its
conductor line is assumed normal Gorenstein with a crepant resolution,
and the accepted no-zero-horizontal reduction supplies a special
horizontal prime B with

    B^2=-3,       f.B=1,       c#.B=0.

Suppose `D_T=B_T+R`, with R irreducible of class `(1,2)` on
`E=P1_Gamma x P1_f`. Then B is the sole horizontal exceptional prime.
The mate correction Z consequently satisfies

    coeff_B(Z)=K_M.Z=1.

Its fixed image p_B in Gamma lies on C0 by full mate support.

By reversal of the literal coordinates it suffices to take the endpoint
line `Gamma={x2=x3=0}`. Its only intersection with C0 is the endpoint
`[1:0:0:0]`, with scheme length three. On the affine chart x0=1 put

    a=x1/x0,       y=x2/x0,       x3/x0=y*b.

This is the actual blowup chart; a is the Gamma coordinate, b the
planes-through-Gamma parameter, and the exceptional surface is y=0.
For `r=t/s`, the lifted curve is exactly

    a=r,       b=r,       y=r^3.

Since p_B is the endpoint, B_T is a=0 in E. In this chart the equation
of T has the form

    a*R(a,b)+y*H(a,b,y)=0,

after multiplying by a local unit. Because R is an irreducible `(1,2)`
divisor, it is a smooth graph over the b-line. Substitution of the
actual lifted curve gives

    r*R(r,r)+r^3*H(r,r,r^3)=0,

so `R(r,r)` has order at least two. Thus R passes through (0,0).
The coefficient of a in its local equation is a unit: otherwise the
whole f-fiber at b=0 would be a component, contrary to irreducibility.
Write the graph as `a=phi(b)`. Its first-order identity is

    phi(0)=0,       phi'(0)=1.

In particular `R -> Gamma` is unramified at this point. Its degree is
two, so the entire fiber over the endpoint consists of two distinct
points, and R meets B_T transversely at both. The second point can lie
in the other affine chart; no finite-coordinate assumption is made.

Every singular point of T on B_T lies at one of these two transverse
intersections. The local equation there is `uv+y*h=0`; its quadratic
part has rank at least two. The Du Val and formal splitting argument
in section 4 of the nonendpoint note therefore gives at most two
endpoint A-chains attached to B, with arbitrary lengths.

The curve c# is disjoint from B. At the endpoint it must instead meet
one chain at a unique node k transversely; a smooth embedded descent
has intersection one with that contact prime. If that chain has length
n>=1 and the other has length m>=0, the correction calculation gives

    coeff_B(Z) = ((n+1-k)/(n+1)) /
        (3-n/(n+1)-m/(m+1)) < 1.

This contradicts `coeff_B(Z)=1`. Thus no mate exists in the endpoint
case with irreducible residual R, conditional on the stated structural
inputs. The argument retains the actual order-three normal contact
and does not replace it by a first-normal approximation.

The endpoint reducible residual cases, the lambda-zero stratum, and
the unrestricted genus-two mate problem are still open in this note.
