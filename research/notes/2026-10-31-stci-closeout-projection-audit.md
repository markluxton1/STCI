# Closeout audit: marked quadric projections and elliptic target incidence

October 31, 2026. Independent reviewer: `projection_audit`, with the
degree-ten calculation independently reconstructed by
`projection_audit/degree_ten_review`.
Status: **reviewed provisional evidence; no canonical promotion**.

The curve is the literal
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) over an algebraically
closed field of characteristic zero. This audit closes the status of the
saved projection computations; it does not compute their remaining loci.
The promoted [Cartier singleton classification](../results/cartier_singleton_lift.md)
and [projection phase reduction](../results/projection_phase_reduction.md)
are used with their literal hypotheses. Their model list and finite
structural reduction are not assertions that an admissible projection or
mate exists.

## 1. Final decisions and evidence

| Claim/computation | Final verdict and literal scope | Evidence |
| --- | --- | --- |
| Order-two residual boundary, reduced disjoint ruling divisors, primitive elliptic image | **PASS as inherited independently reviewed premises.** For a basepoint-free marked \((2,2)\) source with determinant order two, full reduced inverse support the diagonal, and birational surface map, the residual is smooth elliptic; its target image is primitive of class \((6,2)\). | [survivor record](2026-10-30-projection-order-two-survivor.md), [boundary audit](2026-10-29-projection-m2-boundary-audit.md), [smooth-residual audit](2026-10-29-projection-m2-doublecover-audit.md) |
| Degree-twenty three-branch cover and Picard identities | **PASS as inherited reviewed premises.** The four attachment points are distinct and avoid endpoints; \(B^3/A\) has passports \((3^6,1^2),(3^6,1^2),(n_1,n_2,n_3,n_4)\), \(\sum n_i=20\), and \(\mathcal O_E(Z)=L^2,\ M=L^3\). These are line-bundle identities, not equality of effective divisors. | [support theorem and independent audit](2026-10-30-projection-elliptic-target-incidence-audit.md) |
| Zero-middle-coefficient support stratum | **PASS as inherited reviewed exclusion**, for every contact distribution and both Möbius determinant strata. It excludes coplanar four-point image support on this actual marked source. | [source proof](2026-10-30-projection-elliptic-target-incidence.md), [audit](2026-10-30-projection-elliptic-target-incidence-audit.md) |
| Explicit palindromic elliptic target | **PASS, now independently checked in the quadratic number field**, including normalization, four unique smooth normalized inverse points, contact five, and simple disjoint ruling boundaries. It is an actual target incidence; it fails the source-extension theorem. | [construction](2026-10-30-projection-elliptic-target-palindromic.md), [new exact control](../computations/stci_closeout_palindromic_independent_2026_10_31.m2), [output](../computations/stci_closeout_palindromic_independent_2026_10_31.txt) |
| Balanced affine discriminant degrees at most eight | **Completed empty necessary-incidence charts** for square-factor affine degrees zero, one, two. Each saved saturation is the unit ideal. The enclosing loop did not finish degree three. | [boundary script](../computations/stci_projection_elliptic_target_boundary_2026_10_30.m2), [output](../computations/stci_projection_elliptic_target_boundary_2026_10_30.txt) |
| Balanced degree-ten resultant/number-field classification | **PASS, completed and independently reconstructed in this closeout.** Nonzero middle coefficient, four distinct nonzero support roots, affine discriminant degree ten: no genus-one normalization. Generic parameters give genus four; every nondegenerate exceptional resultant factor gives genus three. | [original script](../computations/stci_projection_elliptic_target_degree_ten_resultant_2026_10_30.m2), [complete output](../computations/stci_projection_elliptic_target_degree_ten_resultant_2026_10_30.txt), [independent control](../computations/stci_closeout_degree_ten_independent_2026_10_31.m2) and [captured output](../computations/stci_closeout_degree_ten_independent_2026_10_31.txt), Section 3 below |
| Earlier multivariate degree-ten saturation | **Interrupted; superseded for its stated degree-ten endpoint by the completed independent resultant route.** Its own output is not a completion certificate. | [partial output](../computations/stci_projection_elliptic_target_degree_ten_2026_10_30.txt) |
| Balanced degree-twelve nonzero-middle chart | **Unfinished.** Source and eight remainder equations built; saturation never returned. No emptiness, dimension or component classification follows. | [source](../computations/stci_projection_elliptic_target_2026_10_30.m2), [job](../computations/stci_projection_elliptic_target_nonzero_middle_2026_10_30.m2), [partial output](../computations/stci_projection_elliptic_target_nonzero_middle_2026_10_30.txt) |
| General primitive elliptic contact, full order-one source, conductor descent | **Unresolved**, with exact continuation specifications in Sections 5–7. No complete cover enumeration, admissible parameter classification, or actual descending mate is saved. | [survivor specification](2026-10-30-projection-order-two-survivor.md), [full source](2026-10-29-projection-locus.md), [order-one exclusions](2026-10-29-projection-order-one.md) |

The saved degree-ten output ends with
`DEGREE_TEN_PARAMETER_CLASSIFICATION_COMPLETE`. The palindromic target
output ends with
`PRIMITIVE_BALANCED_ELLIPTIC_TARGET_CANDIDATE_VERIFIED`; the new independent
control ends with `PALINDROMIC_TARGET_CLOSEOUT_CONTROL_COMPLETE` and
`EXIT_CODE=0`. In contrast, the nonzero-middle degree-twelve output ends
after `NONZERO_MIDDLE_COEFFICIENT_CHART_START` and contains no
`NONZERO_MIDDLE_SATURATION_DONE`. The boundary output records three
individual `SATURATED_IS_UNIT=true` results and then stops at square-factor
degree three. Completion is inferred from those actual outputs, not the
dates or the surrounding agents' messages.

## 2. What the target survivor means geometrically

On the target quadric
\(Q=\mathbf P^1_A\times\mathbf P^1_B\), the fixed curve is
\(A=B^3\). A primitive elliptic target image of class \((6,2)\) has
an equation
\[
e_0(A)+B e_1(A)+B^2e_2(A)=0,\qquad \deg e_j\le6.
\]
Restriction to \(C_0\) identifies this 21-dimensional vector space
with the binary forms of degree twenty: each exponent is uniquely
\(3i+j\), \(0\le j\le2\). Thus the contact polynomial determines
the actual target curve, not just a numerical contact count.

For \(\eta^2=-4/5\), take
\[
R(t)=t^4+\eta t^3+\eta t+1,\qquad P(t)=R(t)^5.
\]
Regrouping \(P\) gives an actual primitive curve with
\[
e_1^2-4e_0e_2=-3S(A)^2D(A),
\]
where
\[
S=(\eta A+1)(A+\eta)(A^2-7\eta A+1),\qquad
D=5A^4+\frac{28}{5}\eta A^3+\frac{102}{25}A^2+
\frac{28}{5}\eta A+5.
\]
The independently checked separability of \(D\) proves that
\(Y^2=-3D(A)\) is a smooth elliptic normalization and that the
quadratic target equation is irreducible over \(k(A)\). The coefficient
triple has no common factor, so there is no omitted fixed ruling. The
coprimality \(\gcd(R(t),\Delta(t^3))=1\) makes each of the four target
intersection points smooth and unramified for the quadratic projection.
There is consequently exactly one point of the normalization over each
of them, with contact five. Matching degrees alone would not prove this.

The apparent squared zeros in \(e_0,e_2\) are target nodes, not
double zeros of the normalized function \(B\). At the two nodes the
independent control checks two distinct nonzero tangent slopes; both
normalized branches therefore have simple zero or simple pole of \(B\).
The remaining zero and pole roots are simple, and the first-ruling
endpoints avoid them. This supplies actual reduced disjoint boundary
divisors and the degree-twenty cover passport.

Nevertheless these target data do not extend to the marked source
\(S=\mathbf P^1_u\times\mathbf P^1_v\). The support polynomial has
zero \(t^2\) coefficient. Intrinsically, the four image points on
\(C_0\) are coplanar: a hyperplane cuts a quartic in
\(\langle s^4,s^3t,st^3,t^4\rangle\), precisely the quartics with
zero middle coefficient. The plane section of \(Q\) supplies, in its
nondegenerate case, a Möbius correspondence between its ruling
parameters. On the normalization it gives a degree-two function \(a'\)
with the four marked diagonal values \(t_i\).

The actual source would require two degree-two ruling functions \(u,v\)
with those same four values and \(\mathcal O_E(Z)=L^2\), where
\(L=A^*\mathcal O(1)\). The reviewed interpolation lemma forces both
functions to have bundle \(L\), then to equal \(a'\). Their image lies
in the diagonal, contradicting an embedded elliptic \((2,2)\) residual.
The degenerate Möbius case instead puts three marked points in one
degree-two \(A\)-fiber, also impossible. This is a global obstruction
to the two source pencils, after target incidence has succeeded.

The unrestricted STCI question is unchanged. The example demonstrates
that target genus and inverse-point counts are insufficient for existence;
the reusable obstruction is source extension with its actual marking and
line bundles. Noncoplanar support, the order-one source, and other
normalization models are outside this exclusion.

## 3. Independent verdict on the degree-ten calculation

The literal family is balanced contact
\[
P(t)=(t^4+a t^3+b t^2+c t+1)^5,
\]
with distinct nonzero support roots. Normalizing both leading and constant
support coefficients is allowed over the algebraically closed field by
a torus scaling of \(t\) and a scalar. The already excluded \(b=0\)
stratum is separated. The coefficient of \(A^{12}\) in the quadratic
discriminant is \(-5(4b+3a^2)\). Its vanishing and the vanishing of the
\(A^{11}\) coefficient, on \(b\ne0\), force
\[
b=-\frac34a^2,\quad
c=\frac{7a^4+40}{20a},\quad a\ne0.
\]
The latter formula follows by substitution in the second coefficient;
there is no discarded \(a=0,b\ne0\) branch. Put \(t=ay\) and
\(\lambda=a^4\). Up to a nonzero scalar the support becomes
\[
20\lambda y^4+20\lambda y^3-15\lambda y^2+
(7\lambda+40)y+20.
\]
Because \(a\ne0\), this scaling does not change target normalization
genus or root multiplicities. Every nonzero \(\lambda\) occurs over
the algebraic closure.

The saved rational resultant of the new discriminant and its derivative
factors into six nonconstant irreducible factors with degrees
\(1,2,2,3,12,14\). The degree-one factor is \(\lambda\), excluded by
the support hypotheses. The factor
\(169\lambda^2+280\lambda-800\) lowers the affine discriminant degree
and belongs to the lower-degree boundary, not the degree-ten chart.
For each root of the other four factors, exact polynomial arithmetic
over the corresponding number field gives odd squarefree discriminant
degree eight. The double cover therefore has eight branch points and
genus three. Away from the resultant roots the degree-ten polynomial is
squarefree and has genus four. Neither possibility is the required
elliptic normalization.

The independent reconstruction used the same literal support but fresh
coefficient formation, a fresh rational resultant, and an independent
repeated-gcd layer count of odd multiplicities. The surviving number-field
cases have successive derivative-gcd degree sequence \((10,1,0)\),
hence a double root and eight simple roots. This reconstructs the genus
conclusion rather than merely checking the final marker. The fresh run
was bounded to 60 seconds, completed in approximately 30 seconds, and
did not invoke a multivariate Gröbner calculation. Its
[exact independently executed code](../computations/stci_closeout_degree_ten_independent_2026_10_31.m2)
and [captured successful output](../computations/stci_closeout_degree_ten_independent_2026_10_31.txt)
are retained. The output is explicitly labelled as copied from the actual
tool capture without rerunning, and ends with
`INDEPENDENT_GCD_LAYER_CONTROL_COMPLETE`.

The eligible affine discriminant degrees are even. In an actual surviving
elliptic residual, the degree-two \(A\)-map has reduced zero and pole
divisors, hence has no branch over \(A=0,\infty\). A binary degree-twelve
discriminant that is square times a separable quartic with branch quartic
avoiding infinity has even order at infinity. An odd affine degree would
branch there and violates the inherited uniform boundary theorem. The
completed square-factor charts of affine degrees zero, one, two cover the
eligible affine discriminant degrees at most eight. The degree-ten chart
is now also excluded. The degree-twelve chart remains distinct and open.

**Verdict:** PASS for this balanced, nonzero-middle, degree-ten necessary
target incidence. It is not an exclusion of all balanced contacts, all
primitive elliptic targets, all marked projections, or all STCI carriers.

## 4. Resource accounting and the unfinished degree-twelve job

No large parameter calculation was restarted in this closeout. The new
palindromic independent control used exact arithmetic over
\(\mathbf Q(\eta)\), a custom Euclidean gcd, and local tangent tests;
each invocation had an external 60-second limit and the successful final
run completed in under a second. Setup errors in the new checker were
corrected before the saved successful output; they did not alter the
mathematical family. The independent degree-ten control had a 60-second
limit and completed. Neither ran an unbounded Gröbner job.

The inherited degree-twelve problem has seven parameter variables and
eight equations of total degrees at most thirteen, with term counts
\(126,187,335,378,445,366,319,228\). Its script was stopped before the
saturation returned. The earlier degree-ten multivariate saturation and
the boundary loop's degree-three iteration were also interrupted. The
separate completed resultant route resolves the degree-ten mathematical
endpoint, without retroactively completing those interrupted jobs.

## 5. Continuation specification: balanced degree twelve

This is a saved exact reduction, **not an executed empty-locus result**.
Let
\[
B=\mathbf Q[a,b,c,s_0,s_1,s_2,s_3],\quad
R(t)=t^4+at^3+bt^2+ct+1,
\]
and obtain \(e_0,e_1,e_2\in B[A]\) by grouping \(R^5\) modulo three.
Write \(\delta=e_1^2-4e_0e_2\) and
\[
S_4(A)=A^4+s_3A^3+s_2A^2+s_1A+s_0.
\]
The exact ideal is
\[
I=\bigl([A^j]\operatorname{rem}(\delta,S_4^2):0\le j\le7\bigr)
\subset B.
\]
The saved stopped job asks for
\(I:(b\operatorname{Disc}(R))^\infty\). For the literal degree-twelve
chart one also retains \(4b+3a^2\ne0\). No coefficient minor or
\(s_0\) is to be inverted merely for convenience: a square factor may
pass through \(A=0\).

If this incidence survives, its quotient \(D_4=\delta/S_4^2\) must be a
separable quartic, with \(D_4(0)\ne0\) and nonzero leading coefficient.
These retain precisely the four branch values away from the first-ruling
endpoints. The target equation must also be primitive of actual
bidegree \((6,2)\), have reduced disjoint normalized ruling boundaries,
and have exactly four normalized inverse points over its intersection
with \(C_0\). Four target support points alone do not supply this last
condition. No scheme equality, branch multiplicity, or extension to the
source follows from the discriminant factorization alone.

The first unresolved operation is the exact component classification of
this saturated necessary incidence (or a mathematically smaller exact
equivalent), with every coefficient boundary retained. Before a future
large run, declare a wall-time and memory cap and retain an output marker
only after the requested computation has returned. The already stopped
job supplies no bound on the time needed to finish.

## 6. Continuation specification: general primitive elliptic contact

For each ordered positive quadruple \((n_1,n_2,n_3,n_4)\) with sum twenty,
normalize \(t_4=1\) by the curve-preserving torus. Use
\[
B_n=\mathbf Q[t_1,t_2,t_3],\quad
P_n(t)=\prod_{i=1}^4(t-t_i)^{n_i}.
\]
Localize at the product of the \(t_i\), their pairwise differences and
their differences from one. Group exponents modulo three to recover the
unique target equation. The next necessary equation is that its binary
degree-twelve discriminant equal a binary square times a separable binary
quartic, with the branch quartic avoiding the endpoints. Homogeneous
binary equations retain every square-factor-at-infinity chart; the
balanced degree-ten result must not be applied to other contact
distributions.

For each surviving integral target, normalize it and count the actual
points over the target intersection, retaining their local lengths and
contact multiplicities. Then construct two degree-two source pencils
\(u,v\) on that elliptic curve with
\[
u(P_i)=v(P_i)=t_i,\qquad
\mathcal O_E(Z)=L^2,\qquad M=L^3.
\]
They must define a genuine embedded \((2,2)\) curve on the source, and
four global \((2,2)\) coordinate sections must extend the target map with
the prescribed diagonal restriction. The zero-middle theorem says this
is impossible for coplanar support; it supplies no answer for the
remaining noncoplanar support. No passport enumeration or full family
solution is saved.

For an equivalent test retaining the actual source from the outset, use
the full nine-parameter order-two form in
[the residual-geometry record](2026-10-29-projection-residual-geometry.md),
Section 4, over
\(\mathbf Q[A,B,C,D,E,\kappa_0,\kappa_1,\kappa_2,\kappa_3]\).
The necessary support quartic has coefficients
\[
(\kappa_3-CD),\quad(-\kappa_2-CE),\quad
(C^2-1/4),\quad(-\kappa_1+AC),\quad(\kappa_0+BC).
\]
The coefficient order here is constant through degree four. Its
discriminant and endpoint coefficients are nonzero on the surviving
uniform stratum, and the new support theorem requires \(C^2-1/4\ne0\).
The full off-diagonal inverse ideal in Section 7, specialized to this
form, is the first actual-source support condition still uncomputed.

## 7. Continuation specification: full order-one source and descent

Use the entire marked source, not one of its excluded slices:
\[
P=\mathbf Q[p_{ij}:0\le i,j\le3],\quad
U=(a^2,ab,dc,d^2)+\Delta(A_0,A_1,A_2,A_3),
\quad A_i=\sum_jp_{ij}(a,b,c,d)_j,
\]
in the Segre ring \(P[a,b,c,d]/(ad-bc)\), \(\Delta=b-c\).
The order-one open set is the complement of the seven coefficient
equations of
\[
t^4 A_0(s^2,st,st,t^2)+s^4 A_3(s^2,st,st,t^2)
-st^3 A_1(s^2,st,st,t^2)-s^3t A_2(s^2,st,st,t^2).
\]
It is covered by the seven principal opens where one coefficient is
nonzero; inverting their product would incorrectly discard points where
only some coefficients are nonzero.

The fixed quartic ideal is generated by
\[
q=x_0x_3-x_1x_2,\quad
c_0=x_0^2x_2-x_1^3,\quad
c_1=x_0x_2^2-x_1^2x_3,\quad
c_2=x_2^3-x_1x_3^2.
\]
Set \(\Delta=1\), \(b=h+1/2,c=h-1/2\). In
\(P[a,h,d]\), take the literal off-diagonal inverse ideal
\[
J=(ad-h^2+1/4,\ q(U),c_0(U),c_1(U),c_2(U)).
\]
For a coefficient tuple, \(J\) must specialize to the unit ideal.
This is exactly absence of off-diagonal inverse points, including
basepoints: a basepoint also zeros all four pulled-back ideal generators.
The diagonal restrictions are already basepoint free. Equivalently one
may retain the homogeneous inverse ideal and saturate by \(\Delta\)
and the source irrelevant ideal; affine \(\Delta=1\) avoids a missing
projective chart because every off-diagonal projective point lies there.
The parameter locus with unit fiber must be computed constructibly,
retaining all rank or leading-coefficient strata; a generic unit-ideal
calculation over the parameter fraction field is insufficient.

The residual divisor on order one has class \((3,3)\), arithmetic genus
four, ruling degrees five and seven, and total contact degree twenty-six
with the inverse curve. Its intersection with the diagonal has length
six. These measure the actual residual contact problem; they do not
constitute a solution of \(J=(1)\). Reviewed four- and nine-parameter
slice exclusions and the residual multiplicity-gcd condition are useful
boundaries, not an exhaustion of the sixteen parameters. Birationality
onto a degree-eight image remains a separate check after support; finite
degree follows from basepoint freedom and the ample source polarization.

Only after obtaining an actual basepoint-free finite birational source
with full inverse support equal to the diagonal is the mate test
\[
\Delta^{2b}\in\operatorname{span}_k\{U^\alpha:|\alpha|=b\}
\]
the relevant degree-\(b\) equation. In the source Segre ring, expand its
columns in any full degree-\(2b\) basis and retain all parameter rank
strata. This tests membership in the actual homogeneous coordinate
subalgebra, hence actual descent of the pure diagonal divisor. The
promoted full-conductor criterion is an alternative all-degree framework;
its abstract phase reduction has not computed this family's phase image.

The elliptic degree-two inverse-curve, five-parameter double-lift family
is a different source. Its literal ring, support ideal and first
unresolved condition are in the
[existence closeout audit](2026-10-31-stci-closeout-existence-audit.md).
The fixed member's rejection does not compute that five-parameter locus,
and the degree-one diagonal involution exclusion cannot be transferred
without checking its hypotheses.

## Effect on the general question

The completed exclusion chain is substantial within the marked smooth
quadric source: only determinant orders one and two remain; the latter
requires a primitive elliptic target with noncoplanar four-point support;
its balanced contact discriminant charts through degree ten are excluded,
while a genuine target survivor is obstructed by global source extension.
The remaining degree-twelve balanced chart, other contact distributions,
order-one incidence, and actual descent are sharply separated open
conditions. Cone and plane singleton models, non-Cartier lifts, multiple
inverse branches, higher-degree inverse curves and defective first-normal
data are not exhausted. The unrestricted characteristic-zero STCI
question remains open.
