# z4 lifting and deformation

Permanent mathematical dossier preserving complete proofs, computations, exact characteristic hypotheses, obstruction classes, counterexamples and conditional implications. No new theorem promotion is implied.

---

## 2026-10-20-z4-quartic-obstruction

# Integral obstruction for the prescribed Z4: independent calculation

Status: new exact calculation, independently reviewed on 2026-10-21; not
promoted. See [independent audit](#2026-10-20-z4-lift-independent-audit) and
[full report](#2026-10-20-z4-characteristic-zero-lifting-report).  This note does not rely on the
previous integral quartic-carrier exclusion or on previously recorded primitive
triple formulas.

Scope: the fixed curve `[s^4:s^3t:st^3:t^4]` over R=Z_(2) or R=Z_2.  Assume an embedded primitive
triple over the fixed curve has conormal line `O(-6)` and reduces to the
prescribed characteristic-two ribbon (raw direction `X=0, Y=epsilon`).  The
calculation proves this triple cannot exist.  A separate argument must show
that every admissible full Z4 lift supplies such a triple.

## Raw integral normal coordinates

Write `u=x1/x0`, `X=x3/x0-u^4`, `Y=x2/x0-u^3` and on the other chart
`c=x2/x3`, `A=x0/x3-c^4`, `B=x1/x3-c^3`.  Expansion of the exact rational
coordinate change gives

```
c = u^-1 + (u^-4 Y-u^-5 X) + (u^-9 X^2-u^-8 XY) + O((X,Y)^3),
A = 3u^-8 X-4u^-7 Y-9u^-12 X^2+16u^-11 XY-6u^-10 Y^2 + O(3),
B = 2u^-7 X-3u^-6 Y-5u^-11 X^2+9u^-10 XY-3u^-9 Y^2 + O(3).
```

The linear transition has determinant `-u^-14`.  At characteristic two it is
diagonal of degrees `-8,-6`; this integral frame avoids division by two in a
characteristic-zero balanced frame.

Trivialize the quotient line `L=O(-6)` by `epsilon` on U and `eta` on V,
with `eta=u^-6 epsilon` to first order.  Put `X=p(u)epsilon`,
`Y=q(u)epsilon`.  The opposite direction is

```
P(u^-1)=3u^-2 p-4u^-1 q,
Q(u^-1)=2u^-1 p-3q.
```

Requiring all four expressions to be regular on their charts gives exactly

```
p=a+b u+3h u^2,       q=d+2h u,
P=3a c^2+(3b-4d)c+h, Q=2a c+(2b-3d).
```

To see exhaustiveness, the equations on positive Laurent powers first imply
`2p_(j+1)-3q_j=0` and `3p_(j+2)-4q_(j+1)=0` for `j>0`.
Their coefficient determinant is a unit (`9-8=1`), eliminating all higher
terms.  The remaining relation `2p_2=3q_1` has exactly the parameterization
`p_2=3h,q_1=2h`, since three is a unit.  Thus all quotient variations are
included, before imposing the basepoint-free open condition.  The prescribed
special ribbon requires `a,b,h in 2R` and `d in R^times` with `d=1 mod 2`
after scalar trivialization.  The impossibility below holds on this entire
parameter space, so imposing basepoint-freeness adds no loophole.

## Exact triple cocycle and all quadratic corrections

Set `m_U=qX-pY`, `m_V=Q(c)A-P(c)B`.  Its linear transition is
`m_V=-u^-8 m_U`.  For a general local primitive triple write

```
X=p epsilon+r epsilon^2, Y=q epsilon+s epsilon^2,
eta=u^-6 epsilon+t epsilon^2, epsilon^3=0.
```

Here `r,s,t` are arbitrary local functions.  Equivalently the two local
equations for the line kernel are `m_U=gamma_U epsilon^2` and
`m_V=gamma_V eta^2`.  The exact ambient transition gives

```
m_V = -u^-8 m_U + Kfull epsilon^2,
u^8 Kfull = gamma_U(u)+u^-4 gamma_V(u^-1).
```

The quadratic remainder `m_V+u^-8 m_U`, denoted `Kfull epsilon^2`,
is independent of `r,s`; the quadratic parameter
change `t` disappears because it is multiplied by an additional epsilon.
The functions `gamma_U,gamma_V` range over the whole local correction
space.  Consequently the actual obstruction is the class of `K=u^8 Kfull`
in

```
R[u,u^-1] / (R[u]+u^-4 R[u^-1]) = H^1(P1_R,O(-4)),
```

with free basis `u^-1,u^-2,u^-3`.  It is the extension class for the kernel
line `M=O(-8)` against `L^2=O(-12)`; the sheaf is derived here from the
explicit embedded transition rather than postulated.

The complete Laurent expression is

```
K = 3a^3/u^5 + (9a^2b-12a^2d)/u^4
    + C3/u^3+C2/u^2+C1/u+3bh^2+3h^3u,
C1 = h(ah+3b^2-5bd+3d^2),
C2 = (b-d)(4ah+3b^2-8bd+6d^2),
C3 = a(ah+9b^2-23bd+15d^2).
```

For `a,b,h` even and `d` odd, `C2` is congruent to `2` modulo four: its
second factor is `2` modulo four and its first factor is odd.  Thus this
free cohomology class cannot vanish over `Z_(2)` or `Z_2`, over either of these specified bases. Ramified DVRs with a different
uniformizer are outside the stated parity argument.  Even the
necessary equations over `Z/4` are inconsistent.  This is one finite
integral identity, not a sequence of inconclusive lifts.

Changing the generator of `L` scales the cocycle by a unit and may change
its representative by the displayed coboundaries.  Every local quadratic
coordinate change is already covered by `r,s,t,gamma_U,gamma_V`.  Therefore
these freedoms cannot remove the obstruction.  Generator changes of the
full ideal have no effect on this intrinsic quotient and its extension.

## Reproduction and verification boundary

```
python3 -m venv /tmp/stci-z4-env
/tmp/stci-z4-env/bin/pip install -r research/computations/requirements-z4-2026-10-20.txt
/tmp/stci-z4-env/bin/python research/computations/verify_z4_quartic_obstruction_2026_10_20.py
```

The script reconstructs the rational coordinate changes with arbitrary
quadratic corrections, verifies their cancellation, checks every Laurent
coefficient and the uniform polynomial congruence modulo four.  The
global-family-to-triple reduction, existence of relative line bundles and
primitive filtrations, and the exhaustiveness proof above are mathematical
arguments, not claims certified by symbolic expansion alone.

The initial development run extracted an epsilon coefficient before expanding
a product and failed its correction-cancellation assertion. The code now
expands the entire expression before coefficient extraction; its final run and
the independent integer Macaulay2 reconstruction both pass. No failed run is
used as evidence for an algebraic assertion.


---

## 2026-10-20-z4-lift-independent-audit

# Independent audit: lifting the prescribed embedded Z4

Review status: independently reconstructed and passed for the exact scope
below. This is a review of new work, not a promoted canonical result and not
an invocation of the existing broad quartic-carrier exclusion. The audit was
completed on 2026-10-21 in the dedicated lifting worktree.

## Exact claim and evidence reviewed

The fixed curve is `C=[s^4:s^3t:st^3:t^4]`. The residue-field scheme is exactly
`V(x1^4-x0^3*x3,x2^4-x0*x3^3)` in projective 3-space over `F2`. The bases
covered by this audit are `R=Z_(2)` and `R=Z2`; their fraction fields are
respectively `Q` and `Q2`. The reviewed assertion is that no flat embedded
lift over either base can have generic reduced support exactly the fixed
curve. Its generic multiplicity would automatically be four.

Reviewed source contributions:

- [Exact local structure](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-20-z4-local-structuremd), including its
  Macaulay2 kernel, saturation, chart, and transition computation.
- [Deformation and containment lemmas](#2026-10-20-z4-ci-deformation-lemma),
  including every intermediate-stage flatness claim.
- [Integral obstruction calculation](#2026-10-20-z4-quartic-obstruction),
  including all first-order coefficients and all second-order corrections.

No normal-bundle calculation was repeated. The given splitting need not enter
the decisive calculation: the integral raw transition gives all necessary
bundle maps directly.

## Reconstructed reduction from the full embedded problem

The complete-intersection persistence proof is sound. Flatness identifies the
special restriction of the relative ideal sheaf with the actual special
ideal. The special Koszul resolution gives `H1(I_0(4))=0`. Multiplication by
2 is therefore surjective on the finite module `H1(I(4))`, so Nakayama kills
that module. The two exact special quartic generators lift to a basis of
`H0(I(4))`. The cokernel of their evaluation vanishes on the special fiber;
properness then kills its support everywhere. This proves global generation
by the two quartics without assuming the generic complete-intersection
property. The coprime primitive-factor argument proves their regularity over
the DVR polynomial ring. In particular generic embedded points cannot occur.

The support condition forces `I_Z subset I_C`: restriction to the relative
curve is zero generically and the curve is torsion-free over `R`. Generic
Cohen--Macaulayness and the single reduced component give a unique associated
prime. Localization at that prime is consequently injective, and its Artin
local algebra has length four. Its maximal ideal has fourth power zero.
Torsion-freeness of the relative structure sheaf then extends this to
`I_C^4 subset I_Z`. Thus the truncated normal neighborhood is forced rather
than imposed, and neither generic residual curves nor embedded points have
been silently discarded.

The map from the two quartic conormal sections to `I_C/I_C^2` has rank one at
each special point. Its rank-zero locus is proper and misses the closed
fiber, hence empty; its determinant vanishes generically, because rank two
would give generic multiplicity one. As the relative curve is integral, the
determinant vanishes identically. Its cokernel is therefore a line bundle.
The supplied local complete-intersection proof now chooses a quartic with a
unit normal coefficient, obtains a relative smooth local surface `W`, and
makes `C` a Cartier divisor `ell=0` on `W`. The other defining equation is
principal and on the generic fiber equals a unit times `ell^4`. The ideals
`I_(Z/W)` and `(ell^4)` are both 2-saturated, because their quotients are flat
over the DVR; equality after inverting 2 implies equality integrally. This
also excludes a hidden nonflat intermediate filtration.

It follows that every admissible full lift has canonical embedded flat
stages with local rings `O_C[ell]/ell^n`, `1<=n<=4`, and graded multiplication
given by powers of its first quotient `L`. The special transition forces
`L_k=O(-6)`; `Pic(P1_R)=Z` gives `L=O(-6)`. In particular a contradiction at
the canonical triple stage rules out the original full quadruple. This audit
does not replace the target quadruple by a freely chosen triple.

## Exhaustiveness of the quotient and correction space

Fix generators `epsilon,eta` of `L` on the two standard curve charts, with
linear transition `eta=u^-6 epsilon`. The raw ambient linear transition is

```
A = 3u^-8 X-4u^-7 Y,
B = 2u^-7 X-3u^-6 Y.
```

Put `X=p(u)epsilon`, `Y=q(u)epsilon`. Opposite-chart regularity requires

```
P(u^-1)=3u^-2 p-4u^-1 q,
Q(u^-1)=2u^-1 p-3q.
```

For every `n>=2`, the coefficient of `u^(n-1)` in the first expression and
of `u^n` in the second imposes
`3p_(n+1)-4q_n=0`, `2p_(n+1)-3q_n=0`. The determinant is `-1`, so all
`p_(n+1),q_n` vanish. The sole remaining positive-power condition is
`2p_2=3q_1`. Because 3 is a unit, the entire quotient space is exactly

```
p=a+b*u+3h*u^2,     q=d+2h*u,
P=3a*c^2+(3b-4d)c+h, Q=2a*c+(2b-3d).
```

No division by 2 occurs. The prescribed special ribbon requires
`a,b,h in 2R`, `d in 1+2R`. Actual quotients must also be surjective; enlarging
the parameter space by dropping that open condition only strengthens the
contradiction below. Thus a first-conormal quotient whose coordinate `q`
has a zero somewhere on the generic chart is not lost.

There is no assumed global retraction of the triple to `C`. On the inverse
image of the affine `u` chart, the ambient function `u` itself gives the
coefficient subalgebra `R[u]`. Affineness permits lifting the chosen generator
of `J/J^2` to a section `epsilon` of `J`. The filtration by free line modules
then proves that `1,epsilon,epsilon^2` is an `R[u]` basis, so the local triple
ring really is `R[u,epsilon]/epsilon^3`. The identical argument applies to
the `c` chart. Consequently all embedded triple corrections have the form

```
X=p epsilon+r(u)epsilon^2,
Y=q epsilon+s(u)epsilon^2,
eta=u^-6 epsilon+t(u)epsilon^2.
```

The actual `c` coordinate, including its nilpotent variation, is derived from
the ambient identity `c=(u^3+Y)/(u^4+X)`. Abstract nilpotent changes of a base
coordinate give no extra embedding: one can return to these fixed ambient
`u,c`. A change of epsilon by an arbitrary quadratic term is already covered
by `r,s,t`. The local kernel equation `m_U=qX-pY` has arbitrary quadratic
coefficient `gamma_U=q*r-p*s`; since a genuine quotient has unimodular
`(p,q)`, every local coefficient can occur. The same holds on the opposite
chart. Thus allowing unrestricted `gamma_U,gamma_V` does not omit a possible
correction. Generator changes of the full ideal cannot change this intrinsic
kernel-and-quotient formulation.

## Independently reconstructed decisive algebra

The independent Macaulay2 script starts from rational chart division over
`ZZ`, not from the proposed normal-transition expansions. It leaves `r,s`
as independent indeterminates and computes

```
m_V = -u^-8 m_U + u^-8 K epsilon^2,
K = 3a^3/u^5 + (9a^2b-12a^2d)/u^4
    + C3/u^3+C2/u^2+C1/u+3bh^2+3h^3u,
C1 = h(ah+3b^2-5bd+3d^2),
C2 = (b-d)(4ah+3b^2-8bd+6d^2),
C3 = a(ah+9b^2-23bd+15d^2).
```

Every `r,s` term cancels. The script separately verifies
`(u^-6 epsilon+t epsilon^2)^2=u^-12 epsilon^2` in the truncated ring, so the
quadratic transition gauge drops out. Matching the local quadratic kernel
relations requires

```
K=gamma_U(u)+u^-4 gamma_V(u^-1).
```

The three intermediate Laurent coefficients are therefore the complete
obstruction to this necessary embedded compatibility. Its controlling sheaf
is `Hom(O(-8),O(-12))=O(-4)`, derived from the kernel and square of the
quotient; the Cech quotient has free basis `u^-1,u^-2,u^-3` over `R`.
This derivation includes the variation of `P(c),Q(c)` under the nilpotent
change of `c`; dropping that variation would produce a different answer.

For the allowed reductions, direct polynomial substitution
`a=2wa,b=2wb,h=2wh,d=1+2wd` gives `C2=2` in the entire polynomial ring
`(ZZ/4)[wa,wb,wd,wh]`. This is a universal identity rather than evaluation
at finitely many coefficients. Thus the obstruction class cannot vanish
over either specified DVR. It appears at the triple extension of the
ribbon; it conclusively excludes a full quadruple by the preceding forced
canonical-stage argument.

The ribbon itself does lift: choose the surjective quotient given by
`p=0,q=1,P=-4c,Q=-3`, and take the inverse image of its kernel in `I_C`.
The resulting square-zero extension has flat graded pieces `O_C` and
`O(-6)`, with the correct special embedded ribbon. Hence the decisive failure
is in the double-to-triple compatibility and is not an already impossible
first quotient. The integral middle coefficient for this particular quotient
is `-6`; allowing all other permitted quotients still forces `2 mod 4`.

## Tests, corrections, and limits of this audit

Commands independently executed:

```
/opt/homebrew/bin/M2 --script research/computations/verify_z4_local_structure_2026_10_20.m2
/tmp/stci-z4-env/bin/python research/computations/verify_z4_quartic_obstruction_2026_10_20.py
/opt/homebrew/bin/M2 --script research/computations/audit_z4_lift_2026_10_20.m2
```

All completed successfully. Independent code and output are
[audit_z4_lift_2026_10_20.m2](../computations/audit_z4_lift_2026_10_20.m2) and
[audit.log](../validation/z4-lift-2026-10-20/audit.log). The first development
run of the audit script used a Macaulay2 built-in name as a variable in the
last polynomial ring and failed after the raw cocycle checks; changing those
fresh variable names resolved it. This was a scripting error, not a failed
mathematical identity.

One overbroad source statement was identified and reported: reduction modulo
the maximal ideal of an arbitrary ramified DVR does not force `a,b,h` to be
multiples of 2. The `mod 4` obstruction as stated proves the result for
`Z_(2)` and `Z2`; this audit makes no claim about arbitrary ramified DVRs or
every characteristic-zero primitive triple. This scope correction is
necessary and does not affect the question posed.

No mathematical dependency remains unproved within the above nonexistence
argument. The cohomology, properness, regularity, nilpotence, and filtration
arguments are proofs audited here, whereas the code independently checks the
stated algebraic identities. A `PASS` marker alone is not offered as a proof
of the deformation-theoretic reduction. Existing canonical mathematics has
not been changed, and no unrestricted STCI assertion is inferred.

The final integrated
[lifting report](#2026-10-20-z4-characteristic-zero-lifting-report) was also
read in full. Its theorem retains precisely the two requested DVRs, and its
logical use of the triple obstruction follows the forced-stage proof above.
The additional command

```
/opt/homebrew/bin/M2 --script research/computations/verify_z4_global_quartics_2026_10_20.m2
```

was independently rerun successfully. All 35 quartic monomials are present;
the 17 support coefficient sums have disjoint exponent fibers, giving the
claimed integral 18-column difference basis. The first-normal matrix retains
all coefficient powers through degree 12 and has the asserted exact rational
ranks. The same script verifies the explicit ribbon gluing over `ZZ[1/3]`,
which specializes over both requested bases. No further theorem-scope or
logical correction was required in the integrated report.


---

## 2026-10-20-z4-characteristic-zero-lifting-report

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

Detailed evidence: [local and global structure](OCT20_21_NORMAL_FILTRATIONS_AND_RECONCILIATION.md#source-2026-10-20-z4-local-structuremd).

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

Detailed proof: [CI, containment and relative primitives](#2026-10-20-z4-ci-deformation-lemma).

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

Detailed calculation: [integral obstruction](#2026-10-20-z4-quartic-obstruction).

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

[Independent audit, tested hypotheses, correction space and scope](#2026-10-20-z4-lift-independent-audit).
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


---

## 2026-10-20-z4-ci-deformation-lemma

# Persistence and containment for the prescribed embedded quadruple structure

Status: new lemma, independently reviewed on 2026-10-21; not promoted.
Review: [independent audit](#2026-10-20-z4-lift-independent-audit).

This note concerns only the curve
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) and the special fiber
\(Z_0=V(x_1^4-x_0^3x_3,x_2^4-x_0x_3^3)\) over \(k=\mathbf F_2\).
It does not use any existing characteristic-zero quartic-carrier exclusion.
The normal-bundle splitting is used as supplied in the assignment and is not
rederived here. The special-fiber regular-sequence and local-structure checks
are explicit hypotheses below; the companion computation verifies them.

## Proposition 1: every flat embedded lift is a global (4,4) complete intersection

Let \(R=\mathbf Z_{(2)}\) or \(R=\mathbf Z_2\), let \(K=\operatorname{Frac}(R)\),
and let \(X=\mathbf P^3_R\). Suppose \(Z\hookrightarrow X\) is closed and
\(R\)-flat and its special fiber, as an embedded scheme, is exactly the complete
intersection \(Z_0=V(F_0,G_0)\), where \(F_0,G_0\) are the prescribed quartics.
Then there are homogeneous quartics \(F',G'\in R[x_0,x_1,x_2,x_3]_4\), reducing
respectively to \(F_0,G_0\), for which
\[
 Z=V(F',G').
\]
They form a regular sequence. In particular the generic fiber is automatically
a global complete intersection of two quartics. The pair \(F',G'\) is a basis
of \(H^0(X,\mathcal I_Z(4))\); all other bases differ by \(\mathrm{GL}_2(R)\).

### Proof

Write \(\mathcal I=\mathcal I_Z\). From
\(0\to\mathcal I\to\mathcal O_X\to\mathcal O_Z\to0\) and \(R\)-flatness,
\(\mathcal I\) is \(R\)-flat and its special-fiber restriction is
\(\mathcal I_0\), not merely an ideal mapping onto \(\mathcal I_0\). Hence
\[
0\longrightarrow\mathcal I(4)\xrightarrow{2}\mathcal I(4)
 \longrightarrow\mathcal I_0(4)\longrightarrow0.                 \tag{1}
\]
The special Koszul sequence, twisted by four, is
\[
0\longrightarrow\mathcal O_{\mathbf P^3_k}(-4)
 \longrightarrow\mathcal O_{\mathbf P^3_k}^{\oplus2}
 \longrightarrow\mathcal I_0(4)\longrightarrow0.
\]
The vanishing of intermediate line-bundle cohomology on \(\mathbf P^3\) gives
\[
H^0(\mathcal I_0(4))=kF_0\oplus kG_0,
\qquad H^1(\mathcal I_0(4))=0.                               \tag{2}
\]
The long exact sequence of (1) shows that multiplication by 2 on
\(H^1(X,\mathcal I(4))\) is surjective. This module is finite over \(R\) by
properness, so Nakayama gives \(H^1(X,\mathcal I(4))=0\). Therefore
\[
H^0(X,\mathcal I(4))/2H^0(X,\mathcal I(4))
 \simeq H^0(\mathcal I_0(4)).                                \tag{3}
\]
The left-hand module before reduction is finite and torsion-free over the DVR,
hence free; (3) shows that its rank is two. Choose lifts \(F',G'\) of the exact
ordered basis \(F_0,G_0\). They are a basis by Nakayama. The inclusion
\(H^0(\mathcal I(4))\subseteq H^0(\mathcal O_X(4))=R[x]_4\) identifies them
with quartic polynomials.

Consider evaluation \(\mathcal O_X(-4)^2\to\mathcal I\), with coherent
cokernel \(\mathcal Q\). Its reduction modulo 2 is surjective because
\(F_0,G_0\) generate \(\mathcal I_0\), so \(\mathcal Q/2\mathcal Q=0\).
Nakayama kills \(\mathcal Q\) at every point of the special fiber. If its
support were nonempty, its proper image in \(\operatorname{Spec}R\) would be
a nonempty closed subset containing the generic point and therefore also the
closed point. This contradicts the empty special-fiber support. Thus
\(\mathcal Q=0\), proving \(Z=V(F',G')\) globally. This properness argument
excludes components or generators that exist only in the generic fiber.

For completeness, regularity can be checked directly. The polynomial ring
\(S=R[x_0,x_1,x_2,x_3]\) is a UFD. A common irreducible homogeneous factor of
\(F',G'\) cannot be 2. Any other common factor and its complementary factors
can be chosen primitive over \(R\), so their nonzero reductions give a common
positive-degree factor of \(F_0,G_0\). This contradicts the special regular
sequence. Thus \(F',G'\) are coprime. Since \(S\) is a domain and a UFD,
\(F'\) is regular and multiplication by \(G'\) is injective modulo \(F'\).
They form a regular sequence. The resulting projective Koszul resolution is
\[
0\to\mathcal O_X(-8)\to\mathcal O_X(-4)^2
 \to\mathcal I_Z\to0.                                      \tag{4}
\]
In particular its generic fiber is Cohen--Macaulay of pure dimension one.
The global homogeneous ideal is the saturated ideal \((F',G')\): twist (4)
by any integer and use \(H^1(\mathbf P^3_R,\mathcal O(n))=0\).
\(\square\)

There is also a direct verification of flatness for arbitrary quartic lifts.
If \(2h=aF'+bG'\), the reduced regular-sequence syzygy implies
\(\bar a=-\bar tG_0\), \(\bar b=\bar tF_0\). Lift \(\bar t\), write
\(a=-tG'+2a_1\), \(b=tF'+2b_1\), and cancel 2 in \(S\) to obtain
\(h=a_1F'+b_1G'\). Thus 2 is a non-zero-divisor in \(S/(F',G')\), proving
flatness over the DVR. This assertion alone says nothing about its generic
support.

## Proposition 2: the fourth normal power is forced, not an extra restriction

Let \(C_R\) be the displayed relative rational quartic. In addition to
Proposition 1, suppose the reduced support of \(Z_K\) is exactly \(C_K\),
with generic multiplicity four. Then, as ideal sheaves on \(\mathbf P^3_R\),
\[
 \mathcal I_{C_R}^{\,4}\subseteq\mathcal I_Z
 \subseteq\mathcal I_{C_R}.                                 \tag{5}
\]
Consequently the full truncated normal neighborhood of order four contains
every admissible lift in the question. An analysis within that neighborhood
does not discard any lift, provided it still allows all ideals and all
embedding/gluing data inside it.

### Proof

The family \(C_R\) is flat: on its two standard parameter charts it is
\(\operatorname{Spec}R[u]\) and \(\operatorname{Spec}R[c]\), with
\(c=u^{-1}\). A section of \(\mathcal I_Z\) restricts to zero on \(C_K\).
Its restriction to \(\mathcal O_{C_R}\) is therefore killed locally by some
power of 2. Torsion-freeness of \(\mathcal O_{C_R}\) makes that restriction
zero. This proves the second inclusion.

By Proposition 1 the generic fiber is Cohen--Macaulay of pure dimension one.
Its unique reduced component is \(C_K\), so it has exactly one associated
prime, the generic prime of \(C_K\); in particular it has no associated
points supported at isolated closed points. The natural map from
\(\mathcal O_{Z_K}\) into its localization at that generic prime is
injective. The target is an Artin local algebra of length four. Its maximal
ideal has fourth power zero: before the chain of its powers becomes zero,
every inclusion is strict by Nakayama, and four nonzero strict quotients
already account for length four. Thus \(\mathcal I_{C_K}^{\,4}\) vanishes in
that localization and, by injectivity, in \(\mathcal O_{Z_K}\) everywhere.

Finally the image of \(\mathcal I_{C_R}^{\,4}\) in \(\mathcal O_Z\) becomes
zero after inverting 2. Each local image section is killed by a power of 2,
whereas \(\mathcal O_Z\) is \(R\)-flat and torsion-free. The image is zero,
which proves the first inclusion in (5). \(\square\)

The multiplicity-four hypothesis in this proposition is redundant once the
support hypothesis is imposed: the (4,4) complete intersection has degree
16, and its unique reduced curve has degree four. The degree formula forces
generic length \(16/4=4\). Keeping the hypothesis explicit makes the source
of the nilpotence bound transparent.

## Corollary 3: relative primitiveness and the first conormal quotient are forced

Suppose the hypotheses of Propositions 1 and 2 hold, and use the independently
checked special local structure \(\mathcal O_{Z_0}=\mathcal O_{C_k}[y]/(y^4)\)
on the two indicated affine charts. Let
\(J=\mathcal I_{C_R}/\mathcal I_Z\subseteq\mathcal O_Z\). Then
\(J^4=0\), and \(L=J/J^2\) is an invertible sheaf on \(C_R\).

Indeed, the conormal presentation is the cokernel of
\[
 \mathcal O_{C_R}(-4)^{\oplus2}
 \longrightarrow\mathcal I_{C_R}/\mathcal I_{C_R}^2,
                                                               \tag{6}
\]
where the right side has rank two and is \(N^*\). Its special-fiber matrix
has rank exactly one everywhere by the prescribed primitive local model.
The rank-zero locus of (6) is closed on the proper curve \(C_R\) and misses
the special fiber; hence it is empty. At the generic point of \(C_K\) its
rank cannot be two: two independent normal linear terms would make the
generic Artin algebra length one, contradicting length four. Thus its
determinant vanishes at the generic point of the integral \(C_R\), and
vanishes identically. Matrix (6) has constant rank exactly one. Locally an
invertible matrix entry reduces it to \(\operatorname{diag}(1,0)\); its
cokernel \(L\) is therefore a line bundle.

Because \(J\) is nilpotent, a local lift of a generator of \(J/J^2\)
generates \(J\): from \(J=(y)+J^2\), iteration gives \(J=(y)\). Thus the
primitive property itself is forced, and is not an assumption about the
generic thickening.

### The full relative local model and the flatness of every canonical stage

In fact there is a stronger local assertion, which is useful if one seeks an
obstruction already in the double or triple stage. At every point of \(C_R\)
there is a relative smooth surface \(W\subseteq X\), containing \(Z\) locally,
such that \(C_R\) is a Cartier divisor \(\ell=0\) on \(W\), and
\[
 \mathcal I_{Z/W}=(\ell^4).                                  \tag{7}
\]

Here is a proof that does not assume the flatness of the intermediate stages.
Choose a local conormal frame \((a,b)\) of \(\mathcal I_{C_R}\). The
constant-rank-one assertion for (6) says that some local combination
\(H=\lambda F'+\mu G'\) has a conormal coefficient that is a unit. Choose
the combination so that \((\lambda,\mu)\) is unimodular; one may simply
choose one of \(F',G'\) whose conormal coefficient is a unit at the point.
After possibly interchanging \(a,b\), write \(H=\alpha a+\beta b\) with
\(\alpha\) a unit. Then \((H,b)=(a,b)=\mathcal I_{C_R}\) locally. Moreover
\(H\) has a nonzero relative normal differential at that point. Since both
\(X/R\) and \(C_R/R\) are smooth, the conormal sequence shows that
\(W=V(H)\) is smooth over \(R\) near the point. The image \(\ell=b|_W\)
generates the ideal of \(C_R\) on \(W\) and is a non-zero-divisor there.
This also follows directly from the regular sequence \((H,b)\) in the
regular local ring of \(X\).

The quotient \(\mathcal O_W/(\ell^4)\) is \(R\)-flat. Indeed its four-step
filtration has quotients
\(\ell^i\mathcal O_W/\ell^{i+1}\mathcal O_W\), \(0\le i\le3\), which
are invertible \(\mathcal O_{C_R}\)-modules and hence \(R\)-flat. Thus both
\(\mathcal I_{Z/W}\) and \((\ell^4)\) are 2-saturated ideals in
\(\mathcal O_W\): their quotient modules have no 2-torsion.

On the generic fiber, the first ideal is principal, because \(H\) is part
of a local basis of the two generators of \(\mathcal I_Z\). Its quotient is
Cohen--Macaulay, its only reduced component is the Cartier curve \(\ell=0\),
and its generic multiplicity is four. It equals \((\ell^4)\) on \(W_K\).
For an explicit local verification, Proposition 2 gives
\((\ell^4)\subseteq\mathcal I_{Z_K/W_K}\); in a regular local ring of the
smooth surface \(W_K\), a principal ideal dividing \((\ell^4)\) and having
radical \((\ell)\) is generated by a unit times \(\ell^r\). The generic
length forces \(r=4\). There are no isolated residual or embedded points,
by complete intersection and the prescribed support.

Two 2-saturated ideals in the same ring that become equal after inverting 2
are equal: if \(h\) belongs to the first, then \(2^n h\) belongs to the
second for some \(n\), and saturation gives membership already before
multiplication. Apply the argument in both directions. This proves (7)
over \(R\).

Consequently multiplication induces canonical isomorphisms
\[
 L^{\otimes i}\xrightarrow{\sim}J^i/J^{i+1},\qquad 0\le i\le3,
 \qquad L=J/J^2,
\]
and the associated graded algebra is
\[
 \operatorname{gr}_J\mathcal O_Z
 \simeq\mathcal O_{C_R}\oplus L\oplus L^{\otimes2}\oplus L^{\otimes3},
\]
with its truncated symmetric-algebra multiplication. These assertions follow
from (7), where multiplication is literally multiplication of powers of
\(\ell\), so they concern the multiplication maps and not just abstract
isomorphism classes of graded pieces. All \(J^i\), all these graded pieces,
and all \(\mathcal O_Z/J^n\) are \(R\)-flat, by their filtrations by line
bundles. Reduction modulo 2 therefore commutes with all the indicated
quotients and powers. In particular
\[
 Z_n=\operatorname{Spec}_{Z}(\mathcal O_Z/J^n),\qquad 1\le n\le4,
\]
is a canonical flat embedded lift of the prescribed \(n\)-fold stage. An
obstruction to the canonical triple stage therefore rules out a full lift;
this implication does not assume a triple lift chosen independently of the
quadruple. The associated-graded statement does not assert that the filtered
algebra is globally split: the quadratic and cubic terms of its transition
functions remain essential data.

The special transition of \(J/J^2\) is
\(B=u^{-6}Y\); hence \(L_k\simeq\mathcal O_{\mathbf P^1_k}(-6)\).
Using \(\operatorname{Pic}(\mathbf P^1_R)\simeq\mathbf Z\), one gets
\(L\simeq\mathcal O_{\mathbf P^1_R}(-6)\). This observation does not by
itself construct the nonlinear multiplication or gluing through cubic order.

## Scope and base distinction

All three arguments hold over either stated DVR. Over \(\mathbf Z_2\),
\(K=\mathbf Q_2\); the generic support condition must then mean the base
change \(C_{\mathbf Q_2}\). A nonexistence proof valid over every
characteristic-zero field rules out both DVRs. Existence over \(\mathbf Z_2\)
would not on its own imply algebraization over \(\mathbf Z_{(2)}\), and no
such implication is made here.

These results reduce the full embedded lifting problem to unrestricted
quartic coefficient equations over the DVR. They are reductions, not an
existence or nonexistence theorem for the required lift. No existing accepted
result has been edited or promoted by this note.


---

## 2026-10-21-z4-divided-frobenius-origin

# Divided fourth powers and the Z4 embedded triple obstruction

Status: preliminary focused calculation; **not independently audited or promoted**. Base R=Z_(2) or Z_2. Sources: research/notes/2026-10-20-z4-characteristic-zero-lifting-report.md and companion obstruction/audit notes.

## Verdict

The valuation-one arithmetic defect is real, but no coordinate-independent map from the divided-fourth-power polynomial to the embedded obstruction group has been constructed. Consequently identifying the global obstruction canonically as a divided-Frobenius image is **not established**. The established source is the quadratic ambient transition and moving-base-coordinate substitution.

## Integral equation on U

Put x0=1, x1=u, x3=u^4+X, x2=u^3+Y. Then exactly

F=-X,
G=4u^9Y+6u^6Y^2+4u^3Y^3+Y^4-3u^8X-3u^4X^2-X^3.

Thus the fourth-power defect contributes 6u^6Y^2 mod normal degree 3, and survives mod 4 as 2u^6Y^2. But the cubic power of x3 contributes -3u^4X^2 and the opposite chart has moving c; isolating 6 in this chart is not an intrinsic construction.

The independently audited quadratic ambient transitions are
c=u^-1+u^-4Y-u^-5X+u^-9X^2-u^-8XY+O(3),
A=3u^-8X-4u^-7Y-9u^-12X^2+16u^-11XY-6u^-10Y^2+O(3),
B=2u^-7X-3u^-6Y-5u^-11X^2+9u^-10XY-3u^-9Y^2+O(3).
The -6u^-10Y^2 term in A is a direct binomial-fourth-power contribution; the complete obstruction also uses the nonlinear change c and both normal equations.

## Full Cech reduction

For a=2alpha, b=2beta, h=2gamma, d=1+2delta, the audited expressions give

C1=h(ah+3b^2-5bd+3d^2) = 2gamma (mod 4),
C2=(b-d)(4ah+3b^2-8bd+6d^2) = 2 (mod 4),
C3=a(ah+9b^2-23bd+15d^2) = 2alpha (mod 4).

Hence [ob] = 2gamma[u^-1]+2[u^-2]+2alpha[u^-3] (mod 4) in H^1(P1_R,O(-4)), in the fixed audited trivializations. The proposed stronger equality [ob]=2[u^-2] (mod 4) is FALSE for general first quotients. The middle coordinate remains universally nonzero. For the distinguished quotient a=b=h=0,d=1, the exact class is -6[u^-2].

The controlling sheaf is Hom(M,L^2)=O(-4), M=O(-8), L=O(-6). Quadratic normal-coordinate and generator corrections contribute Cech coboundaries. A coordinate-dependent coefficient projection is not by itself an intrinsic morphism from divided-power defects.

## General p^r

For 0<j<p^r, v_p(binomial(p^r,j))=r-v_p(j), because binomial(p^r-1,j-1) is a p-adic unit (Lucas). Therefore the first j with valuation one is p^(r-1). Mod p,
D_(p^r)(a,b)=D_p(a^(p^(r-1)),b^(p^(r-1))),
where D_n=((a+b)^n-a^n-b^n)/p for n=p^r, and D_p is interpreted similarly. In particular D4 mod 2=a^2b^2.

A local valuation-one polynomial does not imply a nonzero global obstruction. A well-defined map to the obstruction sheaf, coordinate/generator invariance, and a nonzero resulting Cech class must be established separately. The numerical coincidence with -6 is evidence of a contribution, not proof of a canonical identification.

## Reproducibility

Run python3 research/computations/verify_z4_divided_frobenius_2026_10_21.py (requires SymPy). The script verifies exact U expansion, coefficient reductions, and finite illustrative binomial valuation tests. The general valuation identity is proved above, not inferred from tests.

## Limitations

No new complete coordinate-independent decomposition of the full Cech class into divided-power and moving-coordinate pieces has been proved here. No canonical divided-Frobenius-to-obstruction map is claimed. This note does not modify the audited nonliftability theorem.
