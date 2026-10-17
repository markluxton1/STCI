# Independent audit of the general normal-index consequences

Date: 2026-10-14. Author: `normal_general_threshold_audit`.
Status: **PROVED NEW CONSEQUENCES, WITH THE SCOPE BELOW.** This review
uses the accepted [local power-socle and ordinary-layer
theorem](2026-10-14-generalization-index12-filtered-compatibility.md)
as a premise. It does not rerun that proof, any accepted curve
obstruction, or any CAS computation. The new work checked here is the
degree-independent inequality, its integer and equality consequences,
the tame-characteristic scope, and the intrinsic version without a mate.

## 1. The scalar inequality does not need a denominator assumption

Let a smooth curve C of degree e and genus g lie on a normal integral
degree-a hypersurface F in P3. Suppose a degree-b mate cuts nC on F,
where n=ab/e. Put nu=deg N_C=4e+2g-2. The free first ordinary conormal
line B has degree -ell. Its dual is a saturated line subbundle of N_C.
Assume every such line subbundle has degree at most eta, so ell<=eta.

Write A=A_F for the common-zero divisor of the carrier's first normal
symbol and D=D_n for the actual top-power/socle defect. The accepted
ordinary-layer and socle identities give

```
deg A = ea-nu+ell,
deg(D+A) = n ell-eb = n(ell-e^2/a).
```

At P the actual local Cartier index r_P divides n. Let s>=1 be an
integer bound on all actual indices. If r_P<=s, the
accepted local formula implies the exact nonnegative slack expression

```
D_P-(n/s-1)A_P
  = n(1/r_P-1/s)A_P+(n/r_P)D_(r_P),P >= 0.
```

The expression remains valid even when s exceeds n. Summing, without
dividing by a possibly zero quantity, gives

```
(s-1)ell >= ea-nu+s e^2/a.
```

Since s>=1 and ell<=eta, it follows that

```
e a^2-[nu+(s-1)eta]a+s e^2 <= 0.                 (1)
```

Thus (1) applies also to edge cases where the earlier ratio notation
would have required separate numerator or denominator checks. The
normality, actual finite local Cartier indices, smooth support, and
line-subbundle bound are substantive hypotheses. It makes no assertion
for a nonnormal carrier or an entirely thick rank-two generic algebra.

## 2. Balanced rational curves: the smallest possible index

Suppose C is rational, e>=3, and N_C=O_P1(lambda)^2 with lambda=2e-1.
Then eta=lambda and nu=2lambda. Formula (1) becomes

```
Q_s(a)=e a^2-(s+1)(2e-1)a+s e^2 <= 0.          (2)
```

This forces s>=e-1. Here is an elementary proof that does not rely on
a sample of curve degrees. For 1<=s<=e-2 the discriminant of Q_s is

```
d_s=(s+1)^2(2e-1)^2-4e^3 s.
```

It is convex as a function of s. At the two endpoints,

```
d_1=4[(2e-1)^2-e^3] < 0,
d_(e-2)=-4e^3+13e^2-6e+1 < 0.
```

For e=3 these values are both -8. For e>=4 the first inequality follows
from e^3-(2e-1)^2=e^2(e-4)+4e-1>0; the second follows from
e^2(13-4e)-6e+1<0. Convexity bounds d_s above by the negative chord.
Hence Q_s is positive for every real a, contradicting (2).

When s=e-1, equation (2) factors as

```
Q_(e-1)(a)=e(a-e+1)(a-e) <= 0.
```

The integer degree a is therefore e-1 or e. In either case equality
holds. Since s-1=e-2>0, the two inequalities in Section 1 must both be
equalities, yielding

```
ell=lambda,
D_(r_P),P=0 at every P,
r_P=s wherever A_P>0.                           (3)
```

A point of F on C is singular precisely when A_P>0: the tangential
derivative of F vanishes on C and A records the common zeros of its
two normal derivatives. A Cartier smooth curve on a normal surface
makes that surface regular at the point, so an index-one point cannot
be a singular exception. Thus every singular point on C has actual
index exactly e-1, rather than merely an index dividing e-1. Such
points exist: at a=e-1 or e, deg A=ea-lambda is positive for e>=3.

## 3. The equality case yields a primitive triple only for e>=4

At a singular point, (3) and the accepted pointwise torsion identity
imply that its primitive-index complete intersection W_(r_P) has no
ordinary-layer torsion. The accepted full-lattice conclusion is

```
W_(r_P)=k[[t]][z]/(z^(r_P)).
```

For j<=r_P the ordinary power (z^j) has a torsion-free quotient over
k[[t]], so it is saturated. It therefore equals the image of the
symbolic j-fold curve ideal. At smooth points the symbolic thickenings
are the ordinary primitive ones in the smooth carrier.

For e>=4, the common singular index e-1 is at least three. The global
symbolic triple is consequently an embedded primitive triple at every
point. Its first conormal quotient is B=O(-lambda); the actual map
O(-lambda)^2 -> O(-lambda) has constant coefficients on P1.

Therefore a balanced rational curve of degree e>=4 that admits no
embedded primitive triple with a constant first direction satisfies

```
max_P r_P >= e
```

on any normal mate-admitting carrier. This conclusion is conditional on
the stated intrinsic embedded-triple obstruction; the audit does not
claim that every balanced rational curve has that obstruction. For
e=3 the equality case supplies only a primitive double, so the same
triple conclusion is unavailable. The C0 constant-direction obstruction
is an accepted characteristic-zero input and has not been replayed.

## 4. Tame positive characteristic needs r_P invertible, not n

The local theorem and its consequences above extend to characteristic
p>0 if p divides none of the actual indices r_P along C. The two
characteristic-sensitive steps in the accepted local argument involve
the primitive local thickening W_(r_P): its Artinian special fiber has
length r_P, and differentiating z^(r_P)=h w uses the scalar r_P. Both
are legitimate when p does not divide r_P. The multiplier k=n/r_P may
be divisible by p: neither the colon comparison nor the subsequent
power comparison differentiates h^k.

The formal Artinian CI Jacobian theorem explicitly applies when the
characteristic does not divide its length; see [Vasconcelos, *The Top
of a System of Equations*, Theorem 1.1, printed page
550](https://boletin.math.org.mx/pdf/2/37/BSMM(2).37.549-556.pdf).
The primary formulation was inspected for this new scope question.
The relative Frobenius/lattice argument, purity, saturation, and bundle
degree calculations are characteristic-free. Thus p need not be
prime to the global mate length n. No wild-index extension is asserted.
Any characteristic-p use of Section 3 must separately supply its
constant-direction primitive-triple obstruction in that characteristic.

## 5. Intrinsic divisor identity without assuming a mate

Let C instead be any smooth Q-Cartier curve on a normal degree-a
hypersurface F. Put R=lcm_P r_P, so RC is an effective Cartier divisor
on F, and put M=O_F(RC)|C. Let W_R denote that divisor as an embedded
curve scheme in P3. It is locally a regular sequence (F,h), hence is
lci and Cohen--Macaulay pure, even though its second defining equation
need not be a global hypersurface equation. For R>=2 it is generically
curvilinear of length R, with the same saturated first conormal line B
defined by the carrier direction.

Adjunction for an effective Cartier divisor on the Gorenstein
hypersurface gives

```
omega_(W_R)|C = O_C(a-4) tensor M.
```

Finite duality for the same-dimensional CM quotient O_(W_R)->O_C gives
Hom_(W_R)(O_C,omega_(W_R))=omega_C. Since omega_(W_R) is invertible,
this identifies its actual socle, globally and with its embedded
transition functions, as

```
Soc(W_R)=omega_C tensor O_C(4-a) tensor M^(-1).
```

Combine B^(R-1)=Soc(W_R)(-D_R) with
O_C(A)=det(N_C^*) tensor B^(-1) tensor O_C(a). Ambient adjunction
det N_C=omega_C tensor O_C(4) cancels the dualizing terms, proving

```
O_C(D_R+A)=B^(-R) tensor M^(-1).                 (4)
```

The local theorem gives the effective rational divisor

```
E=sum_P [(A_P+D_(r_P),P)/r_P] P,
D_R+A=R E,
O_C(R E)=B^(-R) tensor M^(-1),
deg E=ell-C^2,                                 (5)
```

where C^2=deg M/R is the Q-Cartier self-intersection. These are full
line-bundle identities, not only numerical equalities. The denominator
of E divides R and its support lies among singular points of F on C.

When R=1, ordinary J/J^2 of W_1=C is zero, so it cannot define B.
One must explicitly use B=O_C(-C), the surviving carrier conormal line.
The carrier is smooth along C, A=D_1=E=0, and B^(-1)=M. With this
convention (4)--(5) remain valid.

The same tame-characteristic hypothesis as Section 4 suffices. No mate,
global torsion-detection theorem, vanishing theorem, or assumption on
singularities away from C is used. If every r_P<=s, (5) immediately
gives the intrinsic bound

```
ea+s C^2 <= nu+(s-1)eta.                         (6)
```

For a mate, numerical equivalence nC=bH gives C^2=e^2/a; equation (6)
then recovers (1). This provides a structural Q-Cartier normal-carrier
constraint before one chooses a mate degree.

## 6. Audit conclusion and limits

The general inequality, index threshold, exact equality consequences,
conditional primitive-triple obstruction, tame extension, and
intrinsic line-bundle identity all pass this independent scope review.
The relevant qualifications are e>=4 for the triple conclusion, an
actual embedded-triple obstruction rather than a numerical substitute,
tameness of every actual local index in positive characteristic, and
the explicit surviving-line convention when R=1. None of these results
bounds actual indices for arbitrary normal carriers, handles wild
indices, or excludes all balanced rational curves from being STCI.

## 7. Addendum: direct construction on a smooth projective threefold

After this audit was drafted, the
[owner note](2026-10-14-generalization-normal-index-general-scope.md)
supplied a direct construction preceding the duality calculation.
That construction also passes independent review. Its natural scope
is a smooth projective threefold X, a normal integral Cartier divisor
S, and a smooth Q-Cartier curve C on S; the P3 hypothesis is only
needed in the later numerical substitutions.

Write I=I_(C/S). Normality gives the inclusion
I^R subset O_S(-RC): its elements have C-valuation at least R and
nonnegative valuation at all other height-one primes. Division of an
element of I^(R+1) by a local equation of RC is regular by the same
valuation argument and belongs to the prime ideal I. Restriction to C
therefore factors through I^R/I^(R+1). Every free ordinary graded
layer has rank one; its torsion sum is an ideal, so the free graded
quotient is generated by its first layer B. The surjection B^R onto
the R-th free layer is an isomorphism of line bundles. Since the
target O_S(-RC)|C=M^(-1) has no curve torsion, the restricted inclusion
induces the claimed nonzero map B^R->M^(-1).

At P, write a local equation of RC as a unit times h^(R/r_P).
The image of a generator z^R is a unit times
(z^(r_P)/h)^(R/r_P). The accepted local formula gives precisely
the zero order (R/r_P)(A_P+D_(r_P),P), so its divisor is R E.
This confirms the line-bundle identity directly, including its
transition functions, and does not confuse ordinary with symbolic
powers. For R=1 it simply becomes the Cartier ideal equality.

The alternative global-duality calculation in Section 5 also extends
to X. Replace O_C(a-4) by omega_X|C tensor O_C(S). Then
det N_(C/X)=omega_C tensor omega_X^(-1)|C cancels the two canonical
factors in exactly the same way. Smooth projectivity supplies global
degree and divisor notation; the comparison itself is local along C
and glues without an ampleness hypothesis.

The owner's additional distribution inequalities have the correct
signs. If T=sum_j(A_j+Q_j)/j and A_total=sum_j A_j, then the contact
at indices greater than q satisfies, under an upper bound s>q,

```
A_high >= s(A_total-qT)/(s-q).
```

Without an upper bound, a nonempty high-index contribution has
strictly positive reciprocal cost. Therefore a positive value of
A_total-qT forces A_high>A_total-qT, and its integral lower bound
is floor(A_total-qT)+1. For balanced rational curves, replacing
ell by its upper bound lambda weakens this to the stated
ea-(q+1)lambda+q e^2/a expression. Finally, the accepted pointwise
identity 2 sum_i length(T_i)_P=r_P D_(r_P),P makes every primitive
defect even when its actual index is odd. These conclusions use the
full local defects and keep all singular support points.

## 8. Characteristic-zero equality gives an actual minimal primitive CI

The additional equality consequence also passes review. Work in
characteristic zero and in the balanced rational threshold case
s=e-1. Section 2 gives a=e-1 or e, every singular on-curve index
equal to e-1, and D_(e-1),P=0 at every such point. The singular set
is nonempty, so its actual global Cartier index is R=e-1.

Use the accepted
[rational-ample torsion detection theorem](2026-10-14-generalization-normal-carrier-torsion.md)
without reauditing its proof. Its hypotheses hold: the support is
smooth rational, the surface is normal, and the hypothetical mate
makes a positive multiple of C an ample Cartier divisor. For
g=gcd(a,e), mu=a/g and v=e/g, the primitive carrier class
mu[C]-v[H] is torsion, with exact order

```
t=R/gcd(R,mu),
b_min=v t.
```

The two degree possibilities give

```
a=e-1:  (mu,v)=(e-1,e),  t=1,    b_min=e;
a=e:    (mu,v)=(1,1),    t=e-1,  b_min=e-1.
```

Thus the unordered minimal degree pair is (e-1,e), and its actual
generic length is n_min=ab_min/e=e-1=R. Existence of the minimal mate
is part of the accepted Cartier-ray theorem: the exact principal
relation gives a section with divisor n_min C, which lifts to an
ambient defining form on a hypersurface in P3. This argument starts
from an existing mate and does not infer global torsion from finite
local indices alone.

At every singular point, r_P=n_min and D_(r_P),P=0, so the local
power-socle formula gives D_(n_min),P=0. At smooth points, r_P=1
and A_P=D_1,P=0, giving the same result. The full global top-power
defect therefore vanishes. The accepted pointwise Frobenius identity
eliminates all ordinary-layer torsion and identifies the local algebra
everywhere with k[[t]][z]/(z^(e-1)). This is an embedded primitive
(e-1)-fold curve: in the regular ambient ring the other normal
coordinate is a polynomial in t,z modulo z^(e-1), so subtracting
that polynomial yields a local smooth containing surface.

Consequently the minimal complete intersection is itself a global
primitive (e-1)-fold curve, with free first conormal quotient
O(-lambda) and constant quotient direction. This is stronger than
the symbolic-triple consequence; it also has its literal primitive
double meaning when e=3. The conclusion uses the accepted
characteristic-zero global torsion detection, so it is not asserted
in the tame positive-characteristic part of this audit. Tame local
indices do not by themselves eliminate an invisible wild global
torsion factor.
