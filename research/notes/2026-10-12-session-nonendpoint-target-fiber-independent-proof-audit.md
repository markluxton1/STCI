# Nonendpoint target fibers: independent projective-coverage and exclusion audit

Date: 2026-10-12. Author: `degree_factor_audit`.
Status: **DIRECT INDEPENDENT PROOF AUDIT OF THE STATED BOUNDED
EXCLUSIONS; ADDITIONAL EXACT CHECKS OF OMITTED COEFFICIENT AND
SPECIALIZATION STATEMENTS**. The full nonendpoint family, the remaining
quintic lanes, and the global STCI question remain open.

The audited owner note is
[target-fiber reduction and bounded exclusions](2026-10-12-session-nonendpoint-target-fiber-reduction-and-bounded-exclusions.md),
SHA-256 `c5c7b5b75babd6aa8881f2afc0489e2816f546bd79865e4e1e3458564abb7d5c`.
It was read without modification. All owner execution-manifest source and
stream hashes were checked against the actual files and matched. The
owner's seventeen accepted identities were inspected as supporting
identities, not counted as seventeen new executions or as a substitute
for the geometric arguments below.

Work over an algebraically closed field of characteristic zero, with
delta!=0. In this note `J=d-2g+2b-a` is the owner's lift parameter;
it is not the cubic first-normal polynomial denoted J in the separate
conormal audit. Put B=b-a and G=g-3b+2a.

## 1. Upstream hypotheses and the all-degree bridge

The accepted input is the actual normal anticanonical degree-five surface
S and its smooth rational quartic c, described in the
[explicit model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
This audit checks fiber coverage and exclusions on that model; it does
not reprove the upstream classification of every admissible normalization
pair. The nonendpoint sections are exactly the sections displayed in the
owner note, with the entire delta modulus retained.

When the four sections have no common zero, they define a morphism
phi:S->P3 with phi^*O(1)=H. Since H is ample, no curve can be contracted,
so phi is finite onto its surface image. The image is nondegenerate:
its restriction to c is the fixed nondegenerate quartic C0. The degree
identity is

    5=H^2=deg(phi)*deg(phi(S)).

A surface of degree one in P3 is a plane, which is incompatible with
nondegeneracy. Hence deg(phi)=1 and phi is finite birational; normal S
is the normalization of the resulting integral quintic. Thus center
avoidance is sufficient for the actual normalization projection used by
the owner note.

The accepted
[quintic structural reduction](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
supplies the actual section

    Q=h^5/U0, div(Q)=5c, Q=T^5 on the complete affine open U0=1.

A hypothetical mate of degree 4k pulls back to a scalar Q^k. Equivalently
its effective zero divisor is 5kc. Therefore a point y outside c with
phi(y) in C0 is an all-mate-degree obstruction: the downstairs mate
vanishes at phi(y), while its pulled-back section is nonzero at y.
Every hypothetical mate degree is covered, since the accepted divisor
and degree reduction requires the mate degree to be a positive multiple
of four. This bridge uses an actual section and actual zero divisor;
mere set support without that divisor argument would not suffice.

## 2. Complete projective source boundary

In the anticanonical coordinates, the reduced complement of Z5!=0 is
exactly

    ell={Z2=Z3=Z4=Z5=0}.

The chart Z5=1 is the complete A2(r,T) used by the owner. On ell with
Z1=1, put u=Z0. Its four projection sections are exactly

    (u-1,u-1+delta,u-1+3delta,u-1+4delta).

Their pulled quadric value is -3delta^2. Hence no finite u point maps
to C0, which lies on that quadric. These points are also never base
points, because the first two sections differ by the nonzero delta.

The unique omitted point of ell is

    P0=[1:0:0:0:0:0].

It is the intrinsic A4 point and belongs to c. At P0 the actual
sections are (1,1,1,1), so it is not a base point and maps to target
z=1. There is no further off-c source boundary above C0. In particular,
source r=infinity is this intrinsic point on c, while target z=infinity
comes from the affine c-point r=0. These two infinities cannot be
identified.

Consequently every off-c inverse point above C0 occurs in A2(r,T) with
T!=0. All subsequent affine equations retain the full off-c source
support once this boundary argument has been supplied.

## 3. Finite targets: exact equations and the regular-chart scope

For finite target z, put p=1-z. The point of C0 is
lambda*(1,z,z^3,z^4), with lambda!=0. The three triangular combinations
of X0,...,X3 used to define F1,F2,F3 are invertible after X0 is specified.
Thus F1=F2=F3=0 together with X0=lambda is the exact fiber system.
If the reconstructed lambda were zero, all four sections would vanish;
center avoidance excludes that possibility.

For p!=0, eliminating lambda yields exactly

    H12*T+R2=0, H13*T+R3=0, J0=0.

This elimination divides only by the explicitly nonzero p. It neither
removes T^2 from X0 nor assumes a generic linear rank. On the further
open pZ!=0, the two equations F2,F3 have invertible coefficient matrix
in (T,lambda), and Cramer's rule gives the owner's T=-N/Z and
lambda=M/(p^2 Z). F1 becomes the displayed A2 residual after removing
the c factor pr-delta.

The normalization polynomial Psi has degree at most four in r and
is exactly divisible by pr-delta. Its quotient C3 has degree at most
three, with cubic coefficient p*A^2. This coefficient statement was
not asserted by the owner's final identity checker and is checked by
the independent source linked below. It allows A=0; no degree-drop
locus is removed.

For r!=delta/p on pZ!=0, A2=C3=0 reconstructs a point of the exact
fiber. If T=0, the known embedding c->C0 would force r=delta/p;
if lambda=0, the point would be a base point. Both alternatives are
excluded under the stated conditions. Conversely every off-c point
on this chart satisfies this quadratic/cubic system. The conclusion
is an exact reduction on the stated open, not a full parameter
exclusion. Z=0 remains governed by the denominator-free system.

Any future projective resultant of the degree-two/degree-three pair
must separately handle their shared leading-coefficient degeneration
A=0: a common homogeneous root at infinity does not by itself produce
an affine off-c point. The owner currently makes no such resultant
claim.

## 4. Rank-one compatibility includes the primitive cube roots

If H12=H13=0, compatibility requires R2=R3=0. For p!=0, delta!=0,
the factorization of R2 exhausts the alternatives. The root r=0
does not work because R3=delta^4. Away from pr=delta, the other
alternative is (3-p)r=delta; p=3 is impossible. Substitution into
R3 gives the condition

    p^2-3p+3=0, r=delta/(3-p).

These two p values correspond to z^2+z+1=0, the two primitive cube
roots. They are not generic-rank artifacts. At these points r!=0 and
pr-delta!=0, so J0 is a quadratic in T with nonzero leading coefficient
p and nonzero constant r^3(pr-delta). It has a nonzero root over the
algebraically closed field. Center avoidance then makes lambda nonzero,
and the point is an actual off-c inverse point. The specified rank-one
parameter strata are excluded in every mate degree.

At the alternative r=delta/p, the exact quadratic is

    T*(p*T+pa+B-delta-delta^2/p).

Unless the second factor has zero constant coefficient, it supplies
an off-c point. The equality pa+B-delta-delta^2/p=0 is therefore
necessary for full support. With equality, the doubled T=0 fiber
remains allowed; the owner correctly does not exclude it.

## 5. Target z=1 and the correct direction of Delta1

The intrinsic A4 point supplies the c-point above z=1. There is no
affine c-point above this target. On the affine open, the three
p=0 equations are exactly the owner's equations, and T=0 cannot
solve them: the first then forces r=0, while the third is delta^4.

For J!=0, eliminating T gives P1 and Q1 with degrees exactly three
and two, respectively, and nonzero leading coefficients J and 3J.
The accepted resultant is -J^2*delta^6*Delta1. These fixed leading
coefficients prevent a degree-drop root at infinity. Thus

    J!=0 and Delta1=0

gives an affine common root, necessarily T!=0; center avoidance
supplies X0!=0. This is an all-degree exclusion. The condition
J!=0 and Delta1!=0 merely avoids this obstruction. It is not itself
an excluded stratum and does not certify full inverse support.

For J=0, the third equation forces r=delta/2. The first two become
delta^4/8-D0*T=0 and delta^4/4+G*T=0, with
D0=delta^2/2+B. A point exists exactly when D0!=0 and G=-2D0.
If D0=0, the first equation is a nonzero constant. This correctly
handles the specialization that the general resultant cannot handle.

## 6. Target infinity and degree-drop resultants

The endpoint has equations X0=X1=X2=0. The affine c-point is r=T=0.
For r=0 and T!=0, the equations require B=G=0, a!=0 and T=-a.
Its X3 value is delta^4-J*a; center avoidance is needed if this value
vanishes. This precisely explains the owner's base-point caveat.

For r!=0, the first equation forces Dr=delta*r+B!=0 and
T=delta*r^3/Dr. The remaining equations are exactly Pinf=Qinf=0.
On B!=0, Qinf(0)=-delta^2*B is nonzero, and

    Pinf(-B/delta)=-B^3/delta!=0.

Thus neither a zero-r root nor a denominator-zero root can enter.
Pinf has fixed quadratic leading coefficient -delta^2, so it has
no homogeneous root at infinity. Consequently the nominal
quadratic resultant remains an exact common-affine-root test even
when Qinf drops degree. On B!=0 its vanishing gives an actual
off-c endpoint point, conditional on center avoidance, and excludes
every mate degree. No explicit expanded infinity resultant is
claimed here or needed for this criterion.

At B=0 the exact factorizations are

    Pinf=delta^2*r*(a-r),
    Qinf=r*((3delta^2+G)*r-delta^3).

Hence the complete off-c condition is exactly the owner's
a!=0 and [G=0 or (3delta^2+G)*a=delta^3], including the separate
r=0 branch. With a=0 there is no off-c affine endpoint point.

## 7. Equal lifts: the all-degree proof is complete for every delta!=0

For a=b=g=d, B=G=J=0. This entire subfamily is base-point free.
On the affine open, a hypothetical base point would make all three
coordinate combinations zero. The third would force r=delta/2,
but the second would then equal delta^4/4, a contradiction. Section 2
already rules out every boundary base point. Thus these maps really
are finite birational quintic projections by Section 1.

If a!=0, (r,T)=(0,-a) maps to [0:0:0:delta^4]. It is an off-c point
with a nonzero target scalar, independent of any generic assumption.

For a=0, use the owner's r_s,T_s,lambda_s, valid on p!=0,2,3.
The three target constraints are satisfied exactly, and the remaining
equation factors as the displayed nonzero rational prefactor times
Pc*V, where

    Pc=p^2-6p+6,
    P6=p^2-3p+3,
    V=p^5-9p^4+30p^3-45p^2+(27+9delta)*p-18delta.

The special values V(0)=-18delta, V(2)=2, V(3)=9delta remove those
three denominators. Modulo P6, V=-9delta*(2-p); hence a V-root is
not a P6-root. Modulo Pc,

    V=9*((5p-6)-delta*(2-p)).

The two distinct Pc-roots cannot both be V-roots: the map
(5p-6)/(2-p) has determinant four and its denominator is nonzero
at either root. If every V-root belonged to Pc, all five roots
counted with multiplicity would therefore be one Pc-root rho.
Monicity would give V=(p-rho)^5. Its next coefficient forces rho=9/5,
but Pc(9/5)=-39/25. This contradiction proves a V-root outside Pc.

At that root, all denominators are nonzero and P6 and Pc are nonzero.
Hence T_s!=0, lambda_s!=0 and X0=lambda_s, producing an actual
off-c inverse point. Every equal-lift projection, for every nonzero
delta, therefore has no mate in any degree.

## 8. Open continuation claims and precise verification boundary

The owner correctly leaves the general nonendpoint family open. This
audit also leaves the open G=J=0, B!=0 continuation lane open. Its
forced value a=2B^2/delta^2-B/delta follows from the rank-one c-fiber
at p=-delta^2/B and the condition of Section 4. On this lane,
Qinf=delta*(delta*r+B)*(3r-delta). Full support requires
Pinf(delta/3)!=0. After the forced-a substitution,

    9delta*Pinf(delta/3)
      =-(delta^5+6delta^3B-9delta^2B^2+9delta B^2-18B^3).

This verifies the stated bridge from the infinity test to the
nonvanishing leading coefficient of the exploratory V_B polynomial.
The complete V_B factorization and its V_B(2) specialization were
read in the owner's hash-verified exploratory source and streams;
they were not independently recomputed by this bounded audit and
are not promoted here into a fresh full-family certificate.

No mathematical failure was found in the closed bounded exclusions.
Classification hypotheses are inherited from the accepted upstream
pair theorem. The general quadratic/cubic parameter incidence, the
remaining parameter incidences arising from Z=0 fibers, and higher
contact lengths remain unexhausted.

## 9. New bounded execution and preserved checker failure

The [new independent source](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/verify_proof_gaps.m2)
checks eleven coefficient, boundary, remainder and specialization
statements omitted from the owner's seventeen assertions. Its source
SHA-256 is
`3cac9be6e6bfe7fdd3502f5e66e70f5c34fb024c5ed67e5f9922a8ac50e8ddfc`.
The [captured execution record](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/execution-record.json)
records the actual Macaulay2 command, exit zero, elapsed time, and raw
stdout/stderr hashes. The final PASS ALL line is not a twelfth check.

One earlier execution failed at the first assertion because the
checker used coefficient(r^3,C3) in a flat multivariate ring. That
operation extracts a single monomial coefficient; it does not extract
the coefficient polynomial in r. The exact failed source and streams
remain in
[attempt 01](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/attempt-01-coefficient-extraction-error/execution-record.json).
The corrected source extracts the whole coefficient by the third
r derivative at r=0, divided by six. The whole V polynomial is also
checked instead of incorrectly using the same monomial-coefficient
operation for its p coefficients.

There is one independent checker lineage with two actual executions:
one checker-operation failure and one accepted pass. No owner source,
canonical record, previously frozen source, or Git state was edited.
