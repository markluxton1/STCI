# Exact exclusions inside the order-one marked projection source

October 29, 2026. Investigator: `m1_projection`. Status: **reviewed
provisional contribution**, with the independent reconstruction in
[the audit](2026-10-29-projection-order-one-audit.md). This computes the
empty admissible loci of the literal four- and nine-parameter families below. It
does not compute the full sixteen-parameter source or any surviving
all-degree descent locus. No canonical result/question is changed.

Work over an algebraically closed characteristic-zero field. Put
\(S=\mathbf P^1\times\mathbf P^1\), in Segre coordinates
\([a:b:c:d]\) with \(ad=bc\), and set
\[
\Delta=b-c,\qquad Y=(b+c)/2,\qquad ad=Y^2-\Delta^2/4.
\]
The diagonal is \(c_\Delta=(\Delta=0)\). As in the
[full marked source](2026-10-29-projection-locus.md), require basepoint
freedom and full reduced inverse support of
\(C_0=[s^4:s^3t:st^3:t^4]\) equal to \(c_\Delta\), including isolated
inverse points. The argument below fails these requirements before
birationality or conductor descent needs testing. The literal hypotheses
of [R-0004](../results/projection_phase_reduction.md) are retained.

## 1. A complete four-parameter family, including its order-one open set

For arbitrary \(A,D,C,E\in k\), take
\[
U=(a^2+Aa\Delta+C\Delta^2,\ aY,\ dY,\
       d^2+Dd\Delta+E\Delta^2).
\tag{1}
\]
Every restriction to the diagonal is the fixed quartic parametrization.
The admissible parameter locus of (1) is **empty**.

The coefficient of \(\Delta\) in \(q(U)=U_0U_3-U_1U_2\), modulo
\(\Delta^2\), is
\[
ad(Ad+Da).
\]
On the diagonal this is \(s^2t^2(At^2+Ds^2)\). Hence (1) has determinant
order exactly one whenever \((A,D)\ne(0,0)\). This is an actual
order-one family, rather than a restatement of the earlier symmetric
\(\Delta^2\)-perturbation slice. The boundary \(A=D=0\) is retained.

If \(CE=0\), use either source point
\(a=d=0,Y=\pm\Delta/2\), \(\Delta\ne0\). Its image tuple is
\((C\Delta^2,0,0,E\Delta^2)\). If both coefficients vanish this is a
basepoint; if exactly one vanishes it is an extra inverse point of an
endpoint of \(C_0\). Thus only \(CE\ne0\) needs further work.

Normalize \(\Delta=1\). We construct a source point and a nonzero
\(r\) such that
\[
U=U_0(1,r,r^3,r^4).
\tag{2}
\]
If \(U_0\ne0\), this is an off-diagonal inverse point of \(C_0\);
if \(U_0=0\), it is a basepoint. Both alternatives are inadmissible.

### Generic parameter stratum

Assume
\[
F=CD^2-A^2E\ne0.
\]
For an auxiliary variable \(w\), put
\[
N=Cw^2-E,\quad V=w(D-Aw),\quad K=CDw-AE
\]
and define
\[
H(w)=N^2[(8CD+A)w-(8AE+D)]+4w(D-Aw)K^2.
\tag{3}
\]
There is a nonzero root \(w\) of \(H\) with \(N(w)V(w)\ne0\).
To see this without a generic-rank assumption, its constant and leading
coefficients are
\[
c_0=-E^2(8AE+D),\qquad c_5=C^2(8CD+A).
\]
They cannot both vanish under \(CEF\ne0\): their vanishing implies
\(A=-8CD,D=-8AE\), which gives either \(A=D=0\) or \(64CE=1\),
and in both cases \(F=0\).

If \(c_0,c_5\ne0\), the degree-five polynomial has a nonzero root.
If \(c_0=0\), then \(D=-8AE\), with \(A,D\ne0\); its coefficient
of \(w^4\) is \(-4AD^2C^2\ne0\). Thus it is not a pure fifth power
of \(w\), and has a nonzero root. If \(c_5=0\), then
\(A=-8CD\), with \(A,D\ne0\); its coefficient of \(w\) is
\(4A^2DE^2\ne0\). It is therefore nonconstant with nonzero constant
term, and again has a nonzero root. This covers every coefficient stratum.

At a nonzero root of \(N\), the polynomial (3) has value
\[
H=4C^2w^3(D-Aw)^3\ne0,
\]
because simultaneous vanishing of \(N\) and \(D-Aw\) would force
\(F=0\). At a nonzero root of \(D-Aw\), necessarily \(A\ne0\),
and
\[
H=8AN^3\ne0.
\]
Consequently every nonzero root supplied above avoids the required
denominators.

Choose \(r\ne0\) with \(r^2=w\), and set
\[
a=N/V,\qquad d=wa,\qquad Y=r(a+A+C/a).
\tag{4}
\]
The identities
\[
U_1=rU_0,\qquad U_2=r^3U_0,\qquad U_3=r^4U_0
\]
follow directly; for the last, the difference is
\(w(D-Aw)a+E-Cw^2=Va-N=0\). Moreover,
\[
Y^2-ad-\frac14=\frac{wH(w)}{4N^2V}=0.
\tag{5}
\]
Thus (4) is a point of the actual Segre quadric and gives the required
witness (2). This is a global projective point, not a formal normal
symbol.

### Exceptional parameter stratum

Assume \(F=0\), still with \(CE\ne0\). Choose a nonzero \(w\) with
\[
D=Aw,\qquad E=Cw^2.
\]
If \(A\ne0\), take \(w=D/A\). If \(A=0\), then \(D=0\) and
choose either square root of \(E/C\). Choose \(r^2=w\) and set
\(d=wa,Y=r(a+A+C/a)\), where \(a\ne0\) solves
\[
4w(Aa+C)(2a^2+Aa+C)-a^2=0.
\tag{6}
\]
This equation has nonzero constant term \(4wC^2\). If \(A\ne0\),
its cubic coefficient \(8wA\) is nonzero, so it has a nonzero root.
If \(A=0\), it becomes
\((8wC-1)a^2+4wC^2=0\). Among the two opposite square roots of
\(E/C\), at most one satisfies \(8wC=1\). Choose the other, giving a
nonconstant quadratic and hence a nonzero root.

Equation (6) is exactly the Segre relation after multiplying by
\(4a^2\). The target proportionality (2) holds identically because
\(D=Aw,E=Cw^2\). This completes every exceptional case, including
\(A=D=0\), without dropping a convenient minor or parameter boundary.

## 2. The endpoint exclusion extends to a nine-parameter family

There is also a direct enlargement of the earlier two-fixed-coordinate
slice. Let
\[
U_0=a^2,\quad U_1=aL,\quad L=pb+(1-p)c,
\quad U_2=dc+\Delta A_2,\quad U_3=d^2+\Delta A_3,
\]
with arbitrary \(p\) and all eight coefficients of the linear forms
\(A_2,A_3\) free. This nine-dimensional coefficient locus is inadmissible.
It includes the earlier slice at \(p=1\), but varies the second
coordinate through every compatible linear combination of \(b,c\).

The endpoint-fiber argument is unaffected by this change. On both fibers
\(a=b=0\) and \(a=c=0\), the first two target coordinates vanish for
**every** \(p\). Writing
\(A_2=e_0a+e_1b+e_2c+e_3d\), its third coordinate restricts to
\[
c((1-e_3)d-e_2c),\qquad b(e_1b+e_3d),
\]
respectively. Absence of an off-diagonal zero in the first quadratic
forces \(e_3=1,e_2\ne0\); absence in the second forces
\(e_3=0,e_1\ne0\). Identically zero restrictions also fail, since a
whole off-diagonal subset then gives basepoints or endpoint inverse
points. At every such zero, the fourth coordinate can only decide which
of these two failures occurs. The contradiction excludes the full nine
parameters without a birationality hypothesis.

This extension uses the already-reviewed endpoint argument from
[the projection record](2026-10-29-projection-locus.md), with the literal
new coefficient checked above. It does not imply that every marked map
can be changed into this coordinate form.

## 3. A multiplicity obstruction on the complete order-one source

This smaller additional boundary does not require the coefficient shape
(1). For any basepoint-free tuple in the full marked source, suppose
\[
V(q(U))=c_\Delta+3R,\qquad R\in|\mathcal O_S(1,1)|,
\quad R\ne c_\Delta.
\]
The cokernel line bundle on the determinant divisor has total degree
eight and restriction degree three on the diagonal, by the reviewed
[residual-geometry calculation](2026-10-29-projection-residual-geometry.md).
Degree additivity on component cycles would give
\(3\deg_R L=8-3=5\), impossible. This includes reducible \(R\):
\(\deg_R L\) remains an integer. Hence this entire triple-residual
order-one stratum contains no basepoint-free tuple.

More generally, the greatest common divisor of the residual component
multiplicities must divide five. This is only a cycle-degree condition;
it does not classify residual components with multiplicity gcd one.

## Evidence and limits

The [exact rational verifier](../computations/stci_projection_order_one_2026_10_29.m2)
and [saved output](../computations/stci_projection_order_one_2026_10_29.txt)
check the complete parameter coefficient controls, bad-root identities,
actual target proportionality, Segre construction, exceptional cubic and
first determinant coefficient. It exits zero with
`ALL_FOUR_PARAMETER_LOCUS_EXCLUDED_BY_CONSTRUCTION_IN_COMPANION_NOTE`.
The independent audit uses an elementary coefficient proof of the root
existence, as above; no finite sample over parameters is used.

These exclusions provide new order-one boundaries and an explicit
parameter generator to avoid. They do not solve the general residual
\((3,3)\) contact-26 incidence, nor test descent on an actual surviving
admissible stratum. The full sixteen-parameter problem remains open.
