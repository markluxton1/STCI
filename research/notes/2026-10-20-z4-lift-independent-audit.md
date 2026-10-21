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

- [Exact local structure](2026-10-20-z4-local-structure.md), including its
  Macaulay2 kernel, saturation, chart, and transition computation.
- [Deformation and containment lemmas](2026-10-20-z4-ci-deformation-lemma.md),
  including every intermediate-stage flatness claim.
- [Integral obstruction calculation](2026-10-20-z4-quartic-obstruction.md),
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
[lifting report](2026-10-20-z4-characteristic-zero-lifting-report.md) was also
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
