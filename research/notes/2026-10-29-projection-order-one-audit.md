# Independent audit of a four-parameter projection family

October 29, 2026. Reviewer: outer_family_audit, independently reconstructing
the calculation proposed by m1_projection.

**Verdict: PASS for the entire literal four-parameter family below.**
Every parameter has a basepoint or an off-diagonal point mapping to the
fixed quartic. Consequently its admissible locus is empty. This does not
compute the full sixteen-parameter source, and it is not a canonical
promotion.

## Family and exact hypotheses

Work over an algebraically closed field of characteristic zero. Write
the smooth source quadric as
\[
ad=Y^2-\Delta^2/4,\qquad
Y=(b+c)/2,\quad \Delta=b-c.
\]
For arbitrary scalars \(A,D,C,E\), take
\[
U=(a^2+Aa\Delta+C\Delta^2,\ aY,\ dY,\
      d^2+Dd\Delta+E\Delta^2).
\]
The restriction to the diagonal is the literal fixed parametrization
\((s^4,s^3t,st^3,t^4)\). Admissibility includes basepoint freedom and
the absence of isolated extra inverse points, as in
[R-0004](../results/projection_phase_reduction.md). The proof does not
assume finiteness or birationality before producing its rejection.

If \(CE=0\), either of the source points \(a=d=0\),
\(Y=\pm\Delta/2\), \(\Delta\ne0\), gives
\(U=\Delta^2(C,0,0,E)\). It is a basepoint when \(C=E=0\);
otherwise it maps to an endpoint of the target quartic. Thus these
parameter strata are excluded without dividing by either coefficient.

## Generic coefficient stratum: an exact quintic witness

Assume \(CE\ne0\) and put \(F=CD^2-A^2E\). For an indeterminate \(w\),
set
\[
N=Cw^2-E,\quad V=w(D-Aw),\quad K=CDw-AE,
\]
\[
H(w)=N^2\bigl((8CD+A)w-(8AE+D)\bigr)
       +4w(D-Aw)K^2.
\]
For a nonzero root \(w\) of \(H\) with \(NV\ne0\), choose \(r^2=w\)
and define the off-diagonal affine point
\[
\Delta=1,\quad
a=N/V,\quad d=wa,\quad Y=r(a+A+C/a).
\]
Direct substitution proves
\[
U=U_0(1,r,r^3,r^4),\qquad
4N^2(D-Aw)(Y^2-ad-1/4)=H(w).
\]
Thus this point lies on the source quadric. If \(U_0=0\), all four
coordinates vanish; otherwise it maps to the quartic. Both alternatives
reject admissibility.

It remains to prove the required root exists for **every** parameter
with \(CEF\ne0\). At a root of \(N\),
\[
H=4C^2w^3(D-Aw)^3\ne0,
\]
because \(w\ne0\) and a common root of \(N\) and \(D-Aw\) would force
\(F=0\). If \(A\ne0\), the other possible nonzero root of \(V\) has
\[
H(D/A)=8F^3/A^5\ne0.
\]
When \(A=0\), \(F\ne0\) implies \(D\ne0\), so \(V\) has only its
zero root. Hence every nonzero root of \(H\) avoids \(NV=0\).

The leading and constant coefficients are
\[
h_5=C^2(8CD+A),\qquad h_0=-E^2(8AE+D).
\]
They cannot both vanish: their simultaneous vanishing, with \(CE\ne0\),
forces \(A=D=0\) or \(64CE=1\), and in either case \(F=0\).
If both are nonzero, the quintic has a nonzero root.
The two remaining coefficient cases require care:

- If \(h_0=0\), then \(D=-8AE\), while \(F\ne0\) forces \(A,D\ne0\).
  Its coefficient of \(w^4\) is \(-4AD^2C^2\ne0\). The degree-five
  polynomial is therefore not a pure fifth power monomial, so it has
  a nonzero root.
- If \(h_5=0\), then \(A=-8CD\), with \(A,D\ne0\). Its coefficient
  of \(w\) is \(4A^2DE^2\ne0\), so \(H\) is nonconstant. Since
  \(h_0\ne0\), it has a nonzero root.

This supplies the witness on the entire \(CEF\ne0\) stratum. It needs
neither a generic-coefficient assumption nor a parameter minor inversion.

## Exceptional coefficient stratum: \(F=0\)

Keep \(CE\ne0\). If \(A\ne0\), let \(w=D/A\); the relation \(F=0\)
implies \(w\ne0\), \(D=Aw\), and \(E=Cw^2\). If \(A=0\), then
\(D=0\); choose one of the two nonzero roots of \(w^2=E/C\).
In this latter case choose the sign so that \(8wC\ne1\), which is
possible in characteristic zero.

Choose \(r^2=w\) and a nonzero root \(a\) of
\[
J(a)=4w(Aa+C)(2a^2+Aa+C)-a^2.
\]
The constant coefficient is \(4wC^2\ne0\). When \(A\ne0\), \(J\)
has cubic leading coefficient \(8wA\ne0\). When \(A=0\), the chosen
sign gives the nonzero quadratic coefficient \(8wC-1\). Thus a nonzero
root always exists.

Set \(\Delta=1\), \(d=wa\), \(Y=r(a+A+C/a)\). The equations
\[
U=U_0(1,r,r^3,r^4),\qquad
4a^2(Y^2-ad-1/4)=J(a)
\]
hold identically under \(D=Aw,E=Cw^2\). This again gives a source
basepoint or an off-diagonal inverse point. All \(F=0\) parameters
are retained.

## Verification and scope

The independent
[symbolic verifier](../computations/stci_projection_order_one_audit_2026_10_29.m2)
checks the two source-point identities, the quintic coefficients, and
its bad-root evaluations exactly over rational polynomial and fraction
fields. Its
[saved output](../computations/stci_projection_order_one_audit_2026_10_29.txt)
ends with AUDIT_FOUR_PARAMETER_OUTER_FAMILY_IDENTITIES_PASS.
Root existence is proved algebraically above; it is not inferred from
finitely many numerical parameter tests.

The full marked source has sixteen parameters. This four-parameter
family contains genuine determinant-order-one members, but does not
exhaust that stratum or any of the still-surviving general residual
configurations. There is no admissible survivor in this family on which
to perform conductor or pure-power descent. No conclusion about the cone
or plane normalization source, or unrestricted STCI, follows.
