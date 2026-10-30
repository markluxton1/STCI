# Independent audit of the sparse five-parameter projection slice

October 29, 2026. Reviewer:
projection_incidence/five_param_slice/five_slice_audit.

**Verdict: PASS.** Over an algebraically closed characteristic-zero field,
the entire literal five-parameter slice below has no admissible map.
The zero-parameter boundary in the antisymmetric direction is nonbirational;
every other basepoint-free member fails full singleton inverse support.
This is reviewed provisional evidence, not canonical promotion or a
computation of the full sixteen-parameter locus.

The audited proof is
[the five-parameter note](2026-10-29-projection-five-parameter.md).
The full marked source, admissibility conditions and degree calculation
are those of [the projection record](2026-10-29-projection-locus.md),
[the residual geometry note](2026-10-29-projection-residual-geometry.md),
and [R-0004](../results/projection_phase_reduction.md).

## Literal source and the symmetric boundary

On the smooth quadric \(ad=y^2-z^2/4\), with diagonal \(c=(z=0)\), take
\[
\begin{aligned}
U_0&=a^2+h_0z^2,&U_1&=a(y+Cz)+h_1z^2,\\
U_2&=d(y-Cz)+h_2z^2,&U_3&=d^2+h_3z^2.
\end{aligned}
\]
There are no restrictions on the five scalar parameters
\(C,h_0,h_1,h_2,h_3\). The restrictions to \(c\) are the literal
quartic parametrization.

If \(C=0\), the four sections are invariant under the nontrivial
interchange of the two factors of the source quadric, namely
\((a,y,d,z)\mapsto(a,y,d,-z)\). The map has generic degree at least
two whenever it is a morphism, so cannot be birational onto its image.
This checks the complete \(C=0\) boundary without treating it as a
generic failure.

Assume \(C\ne0\) and basepoint freedom. The established determinant-order
calculation applies: \(q(U)=z^2R\), with a residual Cartier divisor
\(D=V(R)\) of class \((2,2)\), and \(c\) is not a component of \(D\).
The identically zero or higher-order determinant boundaries cannot be
basepoint free and need not be silently removed.

## Independent normal and endpoint calculations

On the chart \(a=1\), set \(d=t^2-z^2/4\), \(y=t\).
For the normal cubic numerator \(H=U_0^2U_2-U_1^3\), expansion gives
\[
H=-4Ct^2z+O(z^2).
\]
The first normal derivative is consequently nonzero at every point
of \(c\) except the two endpoints \(p_0=[1:0:0:0]\) and
\(p_\infty=[0:0:0:1]\). In homogeneous diagonal coordinates its
vanishing divisor is \(2(s=0)+2(t=0)\).

At a nonendpoint \(p\in c\), the pullback of the target ideal of \(C_0\)
is exactly \((z)\): all generators vanish on \(c\), and the displayed
normal derivative supplies a generator \(z\) times a unit. On \(D\),
the pulled-back target-\(C_0\) divisor therefore has precisely the
local intersection multiplicity of \(D\) with \(c\).

The endpoint \(p_0\) belongs to \(D\) exactly when \(h_3=0\).
If \(h_3=h_2=0\), consider the two off-diagonal source fibers
\(d=0\), \(z=1\), \(y=\epsilon/2\), \(\epsilon=\pm1\). They satisfy
the quadric equation and have
\[
U_2=U_3=0,\qquad
U_1=a(\epsilon/2+C)+h_1.
\]
At least one of the two coefficients \(\epsilon/2+C\) is nonzero.
Choose \(a\) to make \(U_1=0\). This gives either a basepoint or an
extra inverse point of \(p_0\), according to \(U_0\). Thus full singleton
support with \(h_3=0\) requires \(h_2\ne0\).

In that remaining case, on the chart \(a=1\), put
\(d=y^2-z^2/4\). An exact quotient for the determinant is
\[
R=(C^2-\tfrac14)d-h_2(y+Cz)-h_1d(y-Cz)
 h_0d^2-h_1h_2z^2.
\]
Its linear term at \(p_0\) is \(-h_2(y+Cz)\). Therefore \(D\) is
smooth and transverse to \(c\) there, with \(z\) a uniformizer on \(D\).
Independently of solving its higher jets,
\[
U_0^2U_2-U_1^3=h_2z^2+O((y,z)^3).
\]
After restricting to \(D\), the target-\(C_0\) divisor has length exactly
two. This uses the cubic generator in the target chart \(x_0\ne0\);
its leading coefficient is nonzero even at \(C=\pm1/2\).

The other endpoint is symmetric but I checked its calculation separately.
It lies on \(D\) exactly when \(h_0=0\). Full singleton support then
requires \(h_1\ne0\), using \(a=0,z=1,y=\pm1/2\) and solving the linear
equation \(U_2=0\). On the chart \(d=1\), \(a=y^2-z^2/4\),
\[
R=-h_1(y-Cz)+O((y,z)^2),\qquad
U_2^3-U_1U_3^2=-h_1z^2+O((y,z)^3).
\]
Thus \(D\) is again transverse to \(c\), and its target-\(C_0\) contact
length is exactly two rather than its diagonal intersection length one.

## Degree contradiction, including nonreduced residuals

The two target ruling degrees on the full residual scheme \(D\) are
\((2,6)\). Hence the target divisor \(C_0\) of class \((1,3)\)
pulls back to a section of a line bundle of degree \(2+3\cdot6=20\).
If a component of \(D\) mapped into \(C_0\), singleton support would
already fail. Otherwise this section is a nonzerodivisor on \(D\):
the effective Cartier divisor \(D\) on the smooth surface is
Cohen--Macaulay, with no embedded associated points, and the section
does not vanish at a component's generic point. Its zero scheme has
length twenty, also when \(D\) is reducible or nonreduced.

Suppose its entire zero support were on \(c\cap D\). The diagonal
intersection has total length four. Away from the endpoints the local
target-\(C_0\) length equals that intersection length. Each endpoint
present is a smooth transverse point of \(D\), and changes length one
to length two. Thus the total zero length would be
\[
4+\#\{p_0,p_\infty\text{ lying on }D\}\le6,
\]
contradicting twenty. This proves the claimed exclusion. No assumption
of reduced \(D\), distinct diagonal intersections, or equality of
parameter ranks enters the argument.

## Exact control and scope

I independently assembled the two local substitutions in Macaulay2 over
\(\mathbf Q[C,h_0,h_1,h_2,h_3]\). Exact polynomial reduction verified:

- Both determinant quotients \(q(U)=z^2R\).
- Their linear parts \(-h_2(y+Cz)\), \(-h_1(y-Cz)\).
- The cubic initial terms \(h_2z^2\), \(-h_1z^2\).
- The generic first-normal term \(-4Ct^2z\).

The scratch verification exited zero with
INDEPENDENT_FIVE_PARAMETER_ENDPOINT_JETS_PASS.
These are independent controls of the local calculation; the uniform
exclusion follows from the global degree and local-length argument above.
The full remaining nine-parameter and sixteen-parameter sources are not
exhausted by this slice.
