# Nonendpoint quintics: corrected conormal cubics and necessary socle bound

Date: 2026-10-12. Auditor:
`oct11_quartic_assembly_audit/degree_factor_audit`, independently assigned
by root. Status: **CORRECTED EXACT IDENTITIES AND DIRECT GLOBAL-FRAME
AUDIT; NECESSARY DEGREE RESTRICTIONS ONLY**.

This note audits the actual nonendpoint family in section 1 of the
[pole-filtration and line-jet note](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md),
using the accepted intrinsic A4 pair and fixed characteristic-zero
C0. It does not re-audit every argument of that note, classify its
entire conductor, or exclude generic mates in all degrees. The
projection center must still miss S for an admissible normalization.
No canonical, sealed, or previously frozen proof file is changed.

## 1. The proposed J expansion failed and is explicitly superseded

The first independent execution passed P, both opposite balanced-frame
transitions, and the socle arithmetic, but failed the displayed J
expansion and the moving U first-normal identity. This is an actual
mathematical coefficient failure, not a scaffold or environment failure.
Root independently identified the same expansion error.

The incorrect J had r^2 coefficient
`3delta(g-b)-delta^3-3delta^2` and r coefficient
`3bdelta^2+delta^3+delta^4`. The correct coefficients are

    r^2: 3delta(g-b)+5delta^3-3delta^2,
    r:   3bdelta^2+delta^3-delta^4.

The difference of the correct and incorrect polynomials is
`2delta^3*r*(3r-delta)`, nonzero for every delta!=0 in characteristic
zero. The earlier preliminary approval of that expansion is withdrawn.
The original failed source and raw streams are preserved in
[attempt 01](../validation/2026-10-12-nonendpoint-conormal-independent-audit/attempt-01-wrong-J-expansion/execution-record.json).

## 2. Derivation from the actual moving target coordinates

Let s=r-delta, delta!=0, and use the actual section family in the
linked note. On c its restrictions are

    X0=r^4, X1=r^3*s, X2=r*s^3, X3=s^4.

Write Ai=(partial_T Xi)|c. Then

    A0=a-2r^2-r,
    A1=b+delta*r-2r^2-r,
    A2=g+3delta*r-2r^2-r,
    A3=d+4delta*r-2r^2-r.

On the target chart x0!=0 the actual moving support coordinate is
z=x1/x0, whose restriction is s/r. Define the balanced residuals

    V=x2/x0-z^3,
    U=x3/x0-(3/2)z*(x2/x0)+(1/2)z^4.

Differentiating all the target ratios, including z, gives

    V_T=P/r^7, U_T=J/(2r^7),
    P=r^3*A2-3r*s^2*A1+2s^3*A0,
    J=2r^3*A3-3s*r^2*A2+s^3*A1.

Expanding those identities yields exactly

    P=(g-3b+2a)r^3
      +[6delta(b-a)+delta^3-3delta^2]r^2
      +[delta^2(6a-3b)+2delta^3]r-2a delta^3,

    J=(2d-3g+b)r^3
      +[3delta(g-b)+5delta^3-3delta^2]r^2
      +[3bdelta^2+delta^3-delta^4]r-b delta^3.

The coefficients of U would be wrong if z were frozen to its value
on c before differentiating. The independent checker reconstructs
the entire section family and takes its actual ratio jets.

## 3. The opposite balanced frame has the same scalar transition

In the first target chart write, to first normal order,

    x0=1, x1=z, x2=z^3+V,
    x3=z^4+U+(3/2)zV.

On the opposite chart put the actual moving coordinate w=x2/x3 and

    a_inf=x1/x3-w^3, b_inf=x0/x3-w^4,
    Vraw_inf=a_inf, Uraw_inf=b_inf-(3/2)w*a_inf.

Expansion modulo I_C^2 gives

    a_inf=2z^(-7)U,
    b_inf=3z^(-8)U+(1/2)z^(-7)V.

Consequently the correct adjusted frame is

    Uop=Vraw_inf/2, Vop=2Uraw_inf,
    Uop=z^(-7)U, Vop=z^(-7)V modulo I_C^2.

Both components have the same scalar transition. In particular their
projective ratio glues as a map to a fixed P1, with no residual swap
or unequal twist. On the source r-chart this also gives

    (Uop)_T=J/[2(r-delta)^7],
    (Vop)_T=P/(r-delta)^7.

Thus r=0, which maps to the opposite target endpoint, is covered
correctly. The intrinsic r=infinity point maps to target z=1;
it must also be retained when homogenizing the cubics.

## 4. Homogeneous gcd determines the saturated quotient degree

Let P_h(R,S)=S^3 P(R/S), J_h(R,S)=S^3 J(R/S), and let Gamma be
their homogeneous gcd, of degree h. The pair cannot be identically
zero when delta!=0. Indeed their constant coefficients force a=b=0,
after which P's r coefficient is 2delta^3. Equivalently the exact
denominator-free witness is

    delta*[r]P + 3*[1]P - 3*[1]J = 2delta^4.

After dividing by Gamma, the pair is basepoint free and consists of
binary forms of degree 3-h. Its induced P1 map therefore has degree

    e=3-h, with 0<=e<=3.

This includes a common zero at R/S=infinity and the case where
one polynomial is identically zero. Taking only an affine gcd could
miss a common infinity factor.

For a hypothetical quasiprimitive defining CI, the first saturated
BF quotient is a line bundle L with a surjection
`N_C^*=O(-7)^2 ->> L`. Its generic quotient images are precisely
the displayed U_T,V_T, up to one common rational scalar. Generic
regularity of the quintic and birational normalization identify these
with the actual transverse direction at the generic point. Saturating
the kernel globally determines this quotient uniquely. The adjusted
frame above makes its projective direction pair `[J_h:2P_h]`;
passing to the annihilating first-normal relation `[2P_h:-J_h]`
uses only a constant invertible change of basis. Thus both have the
same homogeneous gcd degree, and

    L=O_P1(e-7), e=3-deg Gamma.

This deduction uses the actual global saturated quotient, not a
choice of first-normal generators with a prescribed common scale.
It imposes no divisibility of one equation's first-normal scalar by
the other's; nonregular first-normal ratios remain permitted.

As an algebraic check that the coprime locus is not identically absent,
delta=1,a=1,b=g=d=0 gives

    P=2r^3-8r^2+8r-2, J=2r^2.

The only finite root of J is zero, where P=-2, and P's leading
coefficient is two, so the homogeneous pair has no infinity common
factor either. This is a polynomial-family check, not a declaration
that this particular projection center is admissible or gives a mate.

## 5. Socle inequality for every hypothetical CI(5,4k)

The quintic is regular at the generic point of C0, so a hypothetical
CI(5,4k) is generically curvilinear of multiplicity m=5k. Complete
intersection adjunction gives `omega_Y=O_Y(4k+1)`. Its top saturated
BF piece is

    E_(5k-1)=Ann_(O_Y)(I_C)
            =omega_C tensor (omega_Y|C)^(-1)
            =O_P1(-16k-6).

The generically nonzero multiplication of the first piece into that
top piece gives `E_(5k-1)=L^(5k-1)(D_top)` with D_top effective.
It follows that

    deg D_top=(5k-1)(7-e)-6-16k
             =(19-5e)k+e-13 >=0.

For k=2, the four possibilities e=0,1,2,3 give respectively
`25,16,7,-2`. Therefore a hypothetical (5,8) pair requires e<=2,
equivalently a nonconstant homogeneous common factor of P_h,J_h.

For coprime cubics e=3, the same condition is `4k-10>=0`, which
requires k>=3. It excludes degree eight and leaves degree twelve
and larger permitted by this one necessary inequality. It is not
an exclusion of generic mates in all degrees or an existence theorem
in the retained degrees. Closed-point defect divisors, nonregular
ratios, higher jets, center avoidance and entire conductor descent
still require their own arguments.

## 6. Preserved executions and exact evidence scope

The final independent standard-library
[source](../validation/2026-10-12-nonendpoint-conormal-independent-audit/verify_conormal.py)
passes twelve exact checks. Its SHA-256 is
`e5a8b003dbec8bcef1d23636e5d50bd058ee25a3ddb3411b00140e1bf9fa29a7`.
The [current execution record](../validation/2026-10-12-nonendpoint-conormal-independent-audit/execution-record.json)
binds the exact source, actual exit zero, command, interpreter,
elapsed time, and separate raw streams.

Attempt 01 preserves the mathematically false J expansion. Attempt 02
preserves the first successful corrected-J source and complete record.
The final execution changes only the printed coefficient-ring metadata
to include the r^-1 used during ratio normalization; it retains the
same twelve mathematical checks. These are three executions of one
checker lineage, including one genuine mathematical failure, rather
than three independent verifiers. The recording wrapper is not a
mathematical verifier. No frozen historical execution index is inflated.

The calculations verify the stated identities. The global saturation
argument and the socle-duality proof supply their geometric scope.
