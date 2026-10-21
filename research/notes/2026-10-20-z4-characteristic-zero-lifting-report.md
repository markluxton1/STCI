# The prescribed characteristic-two Z4 does not lift over Z_(2) or Z2

Investigation begun 2026-10-20; completed and independently reviewed 2026-10-21.
Status: **new, independently reviewed nonexistence theorem; not promoted to a
canonical result record**. This report and its companion notes are separate
from accepted research. They do not invoke the existing general quartic-carrier
exclusion, do not rederive the supplied normal bundle, and make no assertion
about the unrestricted STCI problem.

## Precise theorem and first obstruction

Let R be either Z_(2) or Z2, with fraction field K respectively Q or Q2. Let
C_R in P3_R be the fixed relative curve [s^4:s^3t:st^3:t^4]. There is **no**
closed R-flat subscheme Z in P3_R whose special embedded fiber is exactly

    Z4 = V(x1^4-x0^3*x3, x2^4-x0*x3^3) over F2

and whose generic reduced support is C_K. Generic multiplicity four is
already forced by these conditions.

The first incompatibility occurs in extending the prescribed ribbon to a
primitive triple over R. All possible first-order quotient directions and
all possible local quadratic embedding corrections give a necessary class
in H1(P1_R,O(-4)). Its middle Laurent coefficient is always 2 modulo 4.
The ribbon itself lifts. Every hypothetical full Z4 lift forces a flat
canonical triple with exactly these data, so the obstruction excludes the
entire quadruple. The argument does not assume that an arbitrary deformation
remains a complete intersection or that I_C^4 is contained in its ideal:
both properties are proved below.

This is an arithmetic lifting statement over the two specified bases. The
parity argument does not cover an arbitrary ramified DVR whose uniformizer
is different from 2, and does not claim that every characteristic-zero
primitive triple on this curve is impossible.

## A. Exact special scheme, embedding and multiplication

The saturated homogeneous ideal of C, over Q and over F2, is

    I_C = (q,f,h,g),
    q = x0*x3-x1*x2,
    f = x1^3-x0^2*x2,
    h = x1^2*x3-x0*x2^2,
    g = x2^3-x1*x3^2.

The generator h is missing from the proposed homogeneous presentation.
It is not in (q,f,g), but saturation of that ideal is I_C. Thus the three
stated equations give the correct ideal sheaf. The four identities
x0*h=x1^2*q+x2*f, x1*h=x3*f+x0*x2*q,
x2*h=-x0*g-x1*x3*q, and x3*h=-x1*g-x2^2*q exhibit the saturation issue.
Kernel elimination independently confirms the ideal in both characteristics.
The two charts x0!=0 and x3!=0 cover C and Z4: their complement would force
all four homogeneous coordinates to vanish.

On U write u=x1/x0, X=x3/x0-u^4, Y=x2/x0-u^3. On V write
c=x2/x3, A=x0/x3-c^4, B=x1/x3-c^3. In characteristic two the exact ideals are

    Z4|U: (X,Y^4),       Z4|V: (A,B^4).

On their overlap, with Y^4=0, the full transitions are

    c = u^-1+u^-4*Y,
    A = 0,
    B = u^-6*Y+u^-9*Y^2+u^-12*Y^3.

The inverse is u=c^-1+c^-4*B,
Y=c^-6*B+c^-9*B^2+c^-12*B^3. In particular the proposed cubic term is correct.
For J=I_C O_Z4, J=(Y) on U, J=(B) on V, J^4=0, and

    J^i/J^(i+1) = O_P1(-6i),  0<=i<=3.

The multiplication maps are the actual local products Y^i*Y^j=Y^(i+j),
respectively B^i*B^j=B^(i+j), truncated at power four. On the overlap
B^2=u^-12*Y^2 and B^3=u^-18*Y^3. The filtered algebra is glued by the full
nilpotent base-coordinate change c, as well as by B; its graded line bundles
alone do not determine it. The companion local-structure note gives the
complete coefficient substitution formula through cubic order using Hasse
derivatives. It even checks that the special ribbon has no retraction to C;
no global retraction is assumed anywhere in the lifting proof.

The saturated ideals of all four stages are computed from
((F,G)+I_C^n)^sat. Their Hilbert polynomials are respectively
4m+1, 8m-4, 12m-15, 16m-32. The full (F,G) is saturated, has radical I_C,
and contains I_C^4 but not I_C^3. These assertions are independently
checked by exact homogeneous computations.

Detailed evidence: [local and global structure](2026-10-20-z4-local-structure.md).

## B. Reduction of the entire embedded Hilbert problem

Let I be the ideal sheaf of any proposed R-flat embedded Z. Flatness gives

    0 -> I(4) --2--> I(4) -> I_special(4) -> 0.

The special Koszul resolution is
0 -> O(-4) -> O^2 -> I_special(4) -> 0. Intermediate line-bundle cohomology
on P3 gives H0(I_special(4))=F2^2 and H1(I_special(4))=0. Hence multiplication
by 2 on the finite R-module H1(I(4)) is surjective; Nakayama makes it zero.
It follows that H0(I(4)) is free of rank two and that its basis can be chosen
to reduce to the exact ordered pair F,G. Evaluation of these two quartics
generates I on the special fiber. Its coherent cokernel has proper support
missing the special fiber, and is therefore zero. Thus **every** flat
embedded deformation is globally V(F',G'), with

    F'=F+2F1,  G'=G+2G1,

where the corrections are unrestricted homogeneous quartics in R[x0,...,x3].
The special regular sequence forces regularity of F',G' over R. All bases
differ by GL2(R). This proves, rather than imposes, the generic (4,4)
complete-intersection property. In particular the generic curve is
Cohen--Macaulay and has no embedded points.

Generic support C_K first forces I_Z subset I_C_R, by torsion-freeness of
O_C_R. Its generic Artin algebra has length four, either from the stated
multiplicity hypothesis or from degree 16 divided by degree C=4. Its maximal
ideal has fourth power zero. Because the generic complete intersection has
only the associated prime of C_K, its structure sheaf injects into its
localization at that prime. Consequently I_C_K^4 vanishes everywhere in it.
R-flatness then gives I_C_R^4 subset I_Z integrally. Thus the full truncated
normal neighborhood captures every admissible lift here.

The matrix of the two first conormal sections has rank one everywhere along
C_R. Its rank-zero locus is proper and misses the special fiber, hence empty.
Its determinant vanishes generically, since rank two would give length one,
and therefore vanishes identically on the integral C_R. Its cokernel
L=J/J^2 is consequently invertible. Locally choose one quartic equation H
with a unit normal coefficient. The surface W=V(H) is smooth over R near C,
and C is Cartier on W, with local equation ell. On W_K, the other equation
is a unit times ell^4. Both I_Z/W and (ell^4) are 2-saturated: their quotients
are R-flat, the second by its four line-bundle filtration. Equality after
inverting 2 therefore gives equality over R:

    I_Z = (H,ell^4) locally.

All multiplication maps L^i -> J^i/J^(i+1) are isomorphisms, and all canonical
stages O_Z/J^n are R-flat and specialize exactly. The special transition
identifies L_special=O(-6); Pic(P1_R)=Z gives L=O(-6). Every admissible full
lift therefore supplies the primitive embedded triple used next. No
intermediate-stage flatness or multiplication condition has been assumed.

Detailed proof: [CI, containment and relative primitives](2026-10-20-z4-ci-deformation-lemma.md).

## C. Completed finite integral calculation with all corrections

The raw integral chart change, through quadratic normal order, is

    c = u^-1+u^-4*Y-u^-5*X+u^-9*X^2-u^-8*X*Y+O(3),
    A = 3u^-8*X-4u^-7*Y-9u^-12*X^2+16u^-11*X*Y-6u^-10*Y^2+O(3),
    B = 2u^-7*X-3u^-6*Y-5u^-11*X^2+9u^-10*X*Y-3u^-9*Y^2+O(3).

These come from exact rational division c=(u^3+Y)/(u^4+X),
A=(u^4+X)^-1-c^4, B=u/(u^4+X)-c^3. The cubic expansions are recorded and
verified over ZZ in the local-structure companion. No division by two or
integral balanced-frame assumption occurs.

Fix generators epsilon,eta of L on the two curve charts with linear
transition eta=u^-6*epsilon. Put X=p(u)epsilon, Y=q(u)epsilon to first order.
If P(c),Q(c) are the opposite images of A,B, chart regularity gives

    P(u^-1) = 3u^-2*p-4u^-1*q,
    Q(u^-1) = 2u^-1*p-3q.

The **entire** solution space over R is

    p = a+b*u+3h*u^2,         q = d+2h*u,
    P = 3a*c^2+(3b-4d)*c+h,   Q = 2a*c+2b-3d.

Indeed the two coefficient equations for every higher pair have determinant
9-8=1, so eliminate all higher terms. The final relation 2p2=3q1 gives
p2=3h,q1=2h since 3 is a unit. Specializing to the prescribed ribbon forces

    a,b,h in 2R,       d in 1+2R.

This parameterization includes every change of the first quotient. The
obstruction below holds even before imposing the surjectivity open condition.

For a general primitive triple, the fixed ambient support coordinate u gives
its affine algebra the basis 1,epsilon,epsilon^2 over R[u]. This follows by
lifting the line generator on the affine chart and using its flat primitive
filtration; it does not require a global projection onto C. Thus all local
embedding and nilpotent-coordinate corrections are

    X=p*epsilon+r(u)*epsilon^2,
    Y=q*epsilon+s(u)*epsilon^2,
    eta=u^-6*epsilon+t(u)*epsilon^2,  epsilon^3=0.

Set m_U=qX-pY and m_V=Q(c)A-P(c)B. The complete substitution, **evaluating
P,Q at the moving c**, gives

    m_V = -u^-8*m_U+u^-8*K*epsilon^2,
    K = 3a^3/u^5+(9a^2*b-12a^2*d)/u^4
        +C3/u^3+C2/u^2+C1/u+3b*h^2+3h^3*u,
    C1 = h*(a*h+3b^2-5b*d+3d^2),
    C2 = (b-d)*(4a*h+3b^2-8b*d+6d^2),
    C3 = a*(a*h+9b^2-23b*d+15d^2).

Every r,s term cancels from the remainder. Also eta^2=u^-12*epsilon^2, so t
cannot change it. Local kernel equations m_U=gamma_U*epsilon^2 and
m_V=gamma_V*eta^2 require exactly

    K = gamma_U(u)+u^-4*gamma_V(u^-1).

The kernel conormal line is M=O(-8), its target is L^2=O(-12), and the
controlling sheaf is therefore Hom(M,L^2)=O(-4). Explicitly its obstruction
module is

    R[u,u^-1]/(R[u]+u^-4*R[u^-1])
      = R*[u^-1] + R*[u^-2] + R*[u^-3].

This derives both the sheaf and all its coordinates from the actual embedded
transition. Arbitrary local corrections give exactly the stated coboundaries.
Rescaling line generators multiplies the class by a unit; quadratic changes
are covered by r,s,t. Changes of the two quartic generators do not affect the
intrinsic quotient or kernel. Hence all the allowed gauge freedoms are included.

Now substitute a=2alpha, b=2beta, h=2eta0, d=1+2delta. The second factor in
C2 is 2 modulo 4, while b-d is odd. Consequently the exact polynomial identity

    C2(2alpha,2beta,1+2delta,2eta0) = 2
       in (ZZ/4)[alpha,beta,delta,eta0]

holds. In particular C2 cannot be zero in R. The necessary Cech equation has
no solution. This is a uniform divisibility obstruction, already visible
modulo four, which excludes every possible integral lift; no indefinite
sequence of finite-modulus experiments is involved.

Detailed calculation: [integral obstruction](2026-10-20-z4-quartic-obstruction.md).

## Global coefficient coverage and the first successful stage

The unrestricted global coefficient check uses **all 35 quartic monomials**.
A monomial x0^i0*x1^i1*x2^i2*x3^i3 restricts on C to u^(i1+3i2+4i3).
For a quartic H to contain C, the coefficient sums for each exponent
0,...,16 must vanish. These are 17 independent integral equations; choosing
one monomial per exponent supplies an integral 18-column difference basis
for every quartic in I_C(4). Since the original F,G already vanish on C_R,
all corrections F1,G1 of an admissible lift lie in this full module. No
monomial, coefficient, or generator mixing is restricted beyond necessity.
The combined value/first-normal map on all 35 columns has rank 34 over Q;
the first-normal image on I_C(4) has rank 17 with kernel Q*q^2.
These checks corroborate the coefficient space, but the proof of
nonexistence uses the stronger exhaustive quotient-and-gluing contradiction,
so it needs no remaining nonlinear quartic elimination.

The prescribed ribbon really does lift. On U use the ideal (X,Y^2); on V
use (A-(4/3)cB,B^2). These agree on the overlap: the exact square-zero
transitions are

    c=u^-1+u^-4*Y,  B=-3u^-6*Y,  A=-4u^-7*Y,
    u=c^-1-(1/3)c^-4*B,  Y=-(1/3)c^-6*B.

Both local rings are polynomial square-zero algebras over R, hence flat;
their embedded ideals glue, have support C_R, and specialize exactly to Z2.
Here 3 is a unit in both requested bases. This example has a=b=h=0,d=1,
for which C2=-6. Allowing every other permitted ribbon deformation still
gives C2=2 mod 4. Thus the first failure is the triple extension rather than
the ribbon, and the forced canonical-stage argument proves the full theorem.

## D. Verdict, review and limitations

**Conclusion 2: the required full embedded lift does not exist**, over either
R=Z_(2) or R=Z2 with the corresponding fixed generic curve. Its invariant
obstruction is the nonzero middle coordinate of the necessary embedded
extension class in H1(P1_R,O(-4)). It survives every allowable first quotient,
local quadratic correction, line-parameter gauge, and GL2(R) generator change.

Independent review reconstructed the geometric reduction and separately
recomputed the cocycle directly from raw chart division over ZZ in Macaulay2,
including arbitrary quadratic corrections. A separate universal computation
in a polynomial ring over ZZ/4 verifies the parity identity. The proposing
SymPy calculation and the independent Macaulay2 implementation agree.

[Independent audit, tested hypotheses, correction space and scope](2026-10-20-z4-lift-independent-audit.md).
There are no unresolved mathematical dependencies within this stated theorem.
The standard projective cohomology, properness, regularity, and filtration
arguments are proved in the companion reduction and audit; computation
certifies the exact algebraic identities rather than replacing those proofs.
An initially overbroad ramified-DVR formulation was corrected during review.
The known normal-bundle splitting was not recomputed and is unnecessary in
the decisive raw integral argument. No established result has been altered
or promoted, and no conclusion about higher-degree STCI presentations follows.

## E. Reproducible files and commands

From this worktree's repository root, the complete integer/finite-field audit
can be reproduced using Macaulay2 alone:

```sh
/opt/homebrew/bin/M2 --script research/computations/verify_z4_local_structure_2026_10_20.m2
/opt/homebrew/bin/M2 --script research/computations/verify_z4_global_quartics_2026_10_20.m2
/opt/homebrew/bin/M2 --script research/computations/audit_z4_lift_2026_10_20.m2
python3 research/computations/validate_records.py
```

The proposing independent-language reconstruction uses SymPy 1.14.0:

```sh
python3 -m venv /tmp/stci-z4-env
/tmp/stci-z4-env/bin/pip install -r research/computations/requirements-z4-2026-10-20.txt
/tmp/stci-z4-env/bin/python research/computations/verify_z4_quartic_obstruction_2026_10_20.py
```

Use `M2` from PATH instead of the absolute executable path on another host.
There are no floating-point computations. Tested versions: Macaulay2 1.26.06,
SymPy 1.14.0. Recorded outputs are in
[validation/z4-lift-2026-10-20](../validation/z4-lift-2026-10-20/):
local-structure.log, global-quartics.log, obstruction.log, audit.log and
records.log. The first three mathematical source notes and the separate audit
above preserve the proofs and verification boundaries. Initial scripting
errors and their corrections are disclosed in the affected notes; final
outputs represent completed successful runs.
