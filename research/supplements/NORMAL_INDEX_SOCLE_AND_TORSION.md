# normal index socle and torsion

## Integration guide: numerical indices and actual symbolic structures

The [general index scope](#2026-10-14-generalization-normal-index-general-scope) derives inequalities that may be applied before a second defining surface is chosen; the [socle theorem](#2026-10-14-generalization-normal-index-socle-theorem) then imposes additional local structure under its exact assumptions. The independent audit distinguishes scalar inequalities from stronger equality-case conclusions and records characteristic restrictions.

[Symbolic carrier torsion](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-torsion) provides Cartier-index and divisor-class information, while [normal flatness](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-generic-ci-normal-flatness) concerns propagation of a filtered complete-intersection structure. Neither a favorable scalar budget nor a formal normal carrier supplies a global second equation automatically. Conversely, the presence of a mate introduces additional numerical constraints that should not be silently assumed in the one-carrier arguments.

Preserve the equality-case, characteristic, and pointwise-index qualifications in the original audits.

---


Permanent mathematical dossier. Complete source arguments are preserved with their precise hypotheses, conditional scope, calculations, failed approaches, and unresolved boundaries. This grouping does not promote claims to canonical results.

---

## 2026-10-14-generalization-normal-index-general-scope

# An intrinsic normal divisor and index thresholds for smooth curves

Date: 2026-10-14. Author: `normal_index_general_scope`.
Status: **PROVED NEW STRUCTURAL THEOREMS; independently reviewed in
[the general-scope audit](#2026-10-14-generalization-normal-index-general-scope-independent-audit).**
The accepted local power-socle theorem in
[the root theorem](#2026-10-14-generalization-normal-index-socle-theorem)
and its
[filtered compatibility audit](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility)
are premises. Their proofs and the inherited computations were not
repeated. The present note removes the choice of mate from the local
budget, extends the comparison before any mate exists, and obtains
uniform index thresholds for arbitrary smooth and balanced rational
curves. It does not resolve the universal STCI problem or unrestricted
characteristic-zero C0.

## 1. The comparison exists before a mate does

Let X be a smooth projective threefold over an algebraically closed
field of characteristic zero, let S be a normal integral Cartier
hypersurface in X, and let C be a smooth projective prime curve in S.
Assume C is Q-Cartier on S. Write r_P for its actual local Cartier
index at P in C and

    R = lcm_P r_P,
    M = O_S(R C)|C,
    C^2 = deg(M)/R.

Indices at smooth surface points are one; only finitely many points
contribute. Let N=N_(C/X), and saturate the first normal symbol of S:

    O_C(-S) -> K subset N^*,
    B = N^*/K,
    deg B = -ell.

K and B are line bundles. Let A be the zero divisor of the resulting
nonzero map O_C(-S) -> K. Thus

    O_C(A) = K tensor O_C(S),
    deg A = S.C - deg N + ell.                         (1)

Its support is precisely the singular points of S on C. Indeed the
first normal symbol vanishes at P precisely when all ambient first
derivatives vanish there, since S already vanishes identically on C.
If C is Cartier at P, smoothness of C forces the normal surface S to
be regular at P. Therefore r_P=1 precisely at the smooth points on C;
there A_P=0.

At a singular point choose a local regular function h with divisor
r_P C, and let W_(r_P)=S/(h). This is a pure local complete
intersection with generic transverse length r_P. Let D_(r_P),P be its
actual top ordinary normal-power/socle defect. This is an invariant of
the actual local thickening; it is not a tangent-cone multiplicity or
a surface multiplicity. Define the effective rational divisor

    E = sum_(P in C) (A_P + D_(r_P),P)/r_P [P].         (2)

Use A_P=D_1,P=0 at smooth points. The definition is independent of the
local generator h, which changes only by a unit, and of a generator
of the free first normal quotient.

**Intrinsic comparison theorem.** There is a naturally induced
nonzero map of line bundles

    B^R -> M^(-1)

whose zero divisor is R E. Equivalently,

    O_C(R E) = B^(-R) tensor M^(-1),
    deg E = ell - C^2 >= 0.                           (3)

This comparison does not assume C is STCI, a mate exists, S has an
ample multiple of C, C is rational, or Cl(S) is torsion-free.
Moreover E has positive coefficient at every singular point of S on
C, since A_P>=1 there. Thus C^2<=ell<=eta, with the first inequality
strict when S is singular at an on-curve point. Under a mate, a
genuinely non-Cartier carrier therefore has e^2/a<eta.

### Construction and divisor

Let I be the ideal of C on S. Normality and the Cartierness of R C
give a canonical inclusion of the ordinary into the divisorial power,

    I^R subset O_S(-R C).

If an element belongs to I^(R+1), division by a local equation of R C
is regular and vanishes on C. Hence restriction factors through the
ordinary graded layer I^R/I^(R+1). Its torsion-free quotient is B^R:
the ordinary associated graded algebra is generated in degree one,
the sum of its layer torsion is an ideal, and each free layer has rank
one. Therefore multiplication surjects from B^R to that free layer
and is an isomorphism of line bundles. This gives the map in (3).

Locally let z generate B and put r=r_P. The accepted local theorem
identifies the vanishing order of z^r/h on C as A_P+D_r,P. A local
equation of R C differs from h^(R/r) by a unit. Thus the restriction
of the preceding map has zero order

    (R/r)(A_P+D_r,P),

which proves (3). This retains the difference between ordinary and
divisorial powers; it does not assert that saturated normal filtrations
have no multiplication defects.

There is also a global duality check. The effective Cartier divisor
W_R=R C on S is lci in X. Adjunction gives

    omega_(W_R)|C = omega_X|C tensor O_C(S) tensor M,
    Soc(W_R) = omega_C tensor (omega_(W_R)|C)^(-1).

The ordinary top power is B^(R-1)=Soc(W_R)(-D_R). Multiplying this
identity by O_C(A), and using det N=omega_C tensor omega_X^(-1)|C,
cancels the ambient and curve canonical factors and gives

    O_C(D_R+A) = B^(-R) tensor M^(-1).

The local power-socle formula says D_R+A=R E. When R=1, W_R=C has
zero ordinary nilradical. In that case B is defined by the saturated
carrier symbol above, rather than by J/J^2 of W_1; B=M^(-1), A=E=0,
and (3) has the same interpretation.

## 2. A mate adds a numerical ray, not another power problem

Specialize to X=P^3, put e=deg C, g=g(C), and let a=deg S. If a mate
of degree b exists, its divisor on S is n C with

    n = ab/e,
    n C linearly equivalent to b H,
    C^2 = e^2/a.

The generic transverse algebra is curvilinear because S is regular
at the generic point of C. For its actual ordinary top-socle defect
D_n the accepted local formula gives the divisor identity

    D_n + A = n E.                                    (4)

Consequently the exact global budget is

    ell - e^2/a = sum_P (A_P+D_(r_P),P)/r_P.            (5)

The entire right side, as well as B and A, is determined by S and C.
There is no b on the right or left. Passing to a higher mate power
does not evade this budget. The line-bundle form retains more than
degrees:

    O_C(D_n+A) = B^(-n) tensor O_C(-b).

In positive genus, (3) is an actual line-bundle constraint on C and
should be retained rather than reduced to a degree count. It imposes
no extra unproved global torsion factor; it follows from the Cartier
divisor R C itself.

## 3. General normal-bundle and pointwise-index bounds

Let eta be any upper bound for the degrees of line subbundles of N.
Since B^* is such a line subbundle, ell<=eta. One can use the maximum
Harder--Narasimhan slope; if N is semistable, eta=deg(N)/2 is valid.
Write nu=deg N=4e+2g-2, and assume all actual local indices along C
are at most s. Equations (1)--(3), before any mate exists, give

    s(ell-C^2) >= deg A = ea-nu+ell,
    ea+s C^2 <= nu+(s-1)eta.                          (6)

This uses a pointwise maximum, not a common multiple and not the
largest ADE label. It does not bound the number of singular points,
the embedding multiplicity, or the higher local corrections.

Under a hypothetical mate, substitute C^2=e^2/a to obtain

    e a^2 - [nu+(s-1)eta]a + s e^2 <= 0.             (7)

No division by a possibly zero expression is needed. In particular,
an index bound gives a linear upper bound on carrier degree,

    a < [nu+(s-1)eta]/e,

and a negative discriminant rules out every carrier degree at once.
If s=1, the exact intrinsic budget actually has A=E=0 and forces
nu=ea+e^2/a under a mate, recovering the Cartier adjunction equality.

For a rational curve with N=O(u) direct_sum O(v), u<=v and
u+v=4e-2, choose eta=v. The criterion becomes

    e a^2-(u+s v)a+s e^2 <= 0.                       (8)

Thus the result is useful for unbalanced as well as balanced curves;
the balanced hypothesis is needed only for the stronger uniform
threshold below.

## 4. A uniform threshold for balanced rational curves

**Theorem.** Let C be a smooth rational degree-e curve in P^3,
e>=3, with N=O(2e-1)^2. Every normal carrier admitting a mate has
an on-curve point of actual Cartier index at least e-1.

Put lambda=2e-1. Criterion (7) reads

    e a^2-(s+1)lambda a+s e^2 <= 0.                  (9)

Its discriminant must be nonnegative:

    lambda^2(s+1)^2 >= 4s e^3.                       (10)

For s>=1, (s+1)^2/s=s+2+1/s increases with s. At s=e-2 the
difference between the sides of (10) is

    lambda^2(e-1)^2 - 4(e-2)e^3
      = -(e-3)(4e^2-e+3)-8 < 0.

It is therefore negative throughout 1<=s<=e-2. This proves s>=e-1
in one argument for every e, independently of both defining degrees.

### The exact threshold is structurally rigid

If all actual indices are at most e-1, set s=e-1 in (9):

    e[a-(e-1)](a-e) <= 0.

Since a is integral, a=e-1 or a=e. At either endpoint all inequalities
are equalities. Therefore

    ell = lambda,
    every singular point of S on C has actual index e-1,
    D_(e-1),P=0 at every such point.                  (11)

Indeed equality forces sum D_r,P/r=0, and every positive A_P must
occur at r=s. No mixed-index distribution or positive primitive
defect survives at this threshold. The first normal quotient is
B=O(-lambda), so its quotient map from O(-lambda)^2 is a constant
direction.

In characteristic zero the sharp threshold is stronger still. The
accepted [rational-ample local torsion detection
theorem](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-torsion) gives the
exact minimal mate degree on a normal carrier. All singular indices
are e-1, so R=e-1. For a=e-1, the primitive numerical pair is
(mu,v)=(e-1,e), and the minimal mate degree is e; for a=e it is
(mu,v)=(1,1), and the minimal mate degree is e-1. Thus

    the minimal unordered defining degree pair is (e-1,e),
    its generic transverse length is n_min=e-1=R.

At singular points r=n_min and D_r=0. At smooth points A=D_1=0.
The exact local formula gives D_(n_min)=0 everywhere. The pointwise
Frobenius identity therefore kills all ordinary-layer torsion, and
the minimal complete intersection is a global primitive (e-1)-fold
structure in the constant first direction. This conclusion uses
characteristic-zero global torsion detection; the tame local formula
alone does not supply a corresponding positive-characteristic
minimal-degree assertion.

For e>=4, all singular-point primitive thickenings have length
e-1>=3. Their zero top-socle defect, together with the accepted
pointwise Frobenius identity, makes every ordinary layer torsion-free.
They are locally R[z]/(z^(e-1)); the symbolic triple is therefore
primitive at those points. At smooth points it is primitive as well.
These local symbolic powers glue to the global symbolic triple of C
on S, whose first normal direction is the constant direction in (11).

**Conditional strengthening.** If a balanced rational degree-e curve,
e>=4, admits no primitive symbolic triple in any constant first
normal direction, every normal mate carrier must have an actual
on-curve Cartier index at least e.

The obstruction hypothesis must be proved for the particular curve.
It is accepted for C0 via P-010; it is not asserted for every balanced
rational curve. For e=3 the threshold only supplies a primitive
double, so the triple strengthening does not apply. For C0, this
general threshold is compatible with the stronger newly accepted
actual-index-at-most-four exclusion; it does not replace that result.

## 5. Distribution constraints retain more than a maximum

Let

    T = ell-e^2/a,
    A_total = ea-nu+ell,
    A_j = sum_(r_P=j) A_P,
    Q_j = sum_(r_P=j) D_j,P.

The exact budget is the pair of moments

    sum_j A_j = A_total,
    sum_j (A_j+Q_j)/j = T.                           (12)

For A_total>0 its weighted harmonic index
A_total / sum_j(A_j/j) must be at least A_total/T. Positive primitive
defects consume part of T and increase the required harmonic index.
This distinguishes distributions with the same least common multiple
or maximum and never replaces the full local defect by tangent data.

For 1<=q<s define A_high=sum_(j>q) A_j. If all indices are at most s,
then

    T >= (A_total-A_high)/q + A_high/s,
    A_high >= s(A_total-q T)/(s-q).                  (13)

Use zero as the lower bound when the displayed right side is negative.
With no upper bound on the high indices one still has

    A_high >= A_total-q T.                           (14)

If the right side is positive, the inequality in (14) is strict,
because a nonempty high-index contribution has positive reciprocal
cost. Integral A_high is then at least floor(A_total-q T)+1.
For balanced rational C, ell<=lambda gives the explicit weaker bound

    A_high >= ea-(q+1)lambda+q e^2/a.                (15)

These are necessary requirements on actual singular-point contact,
not existence certificates or exclusions obtained by enumerating
surface degrees. The pointwise Frobenius identity also forces D_j,P
even whenever j is odd. Its parity should be retained in any future
exact distribution argument.

The number of singular points of S on C is at most floor(s T), since
each contributes at least 1/s to the reciprocal budget. This controls
the number only after an actual index bound is supplied; it imposes
no independent bound on an unrestricted normal carrier.

## 6. Characteristic and remaining scope

All preceding theorems hold in characteristic zero. They also extend
to characteristic p provided every actual on-curve local index r_P
is prime to p. The only characteristic-sensitive step in the local
formula is the primitive length-r Jacobian-socle generator and the
invertible coefficient r in differentiating z^r=h w. The
[primary Jacobian-socle input](https://arxiv.org/pdf/1309.2050),
Eisenbud--Ulrich, Theorem 8.5, applies when the characteristic does not
divide the Artinian CI length. The colon identity, ordinary-layer
Frobenius pairing, divisorial-power inclusion, adjunction and slope
arguments are characteristic-free. The multiplier k=n/r may be
divisible by p; the proof does not differentiate h^k or divide by k.

This tame extension does not use characteristic-zero global torsion
detection. If an actual local index is divisible by p, the Jacobian
generator can vanish, and the displayed defect formula and resulting
index thresholds are not established here. No assertion about wild
torsion, an inseparable index cover, or all characteristic-p curves
follows.

The theorem also leaves nonsmooth curves, nonnormal carriers,
presentations in which both surfaces are generically thick, and
unbounded local-index distributions open. A useful next general task
is to constrain the intrinsic divisor E geometrically, or compute its
line-bundle comparison using a Rees/valuation model, rather than
testing successive mate degrees. Separately, proving the constant
primitive-triple obstruction for further balanced rational curves
would strengthen the uniform s>=e-1 threshold without reopening the
accepted C0 computations.


---

## 2026-10-14-generalization-normal-index-socle-theorem

# Normal carriers: local power-socle compatibility and uniform exclusion

Date: 2026-10-14. Status: **PROVED, WITH A SEPARATE INDEPENDENT NEW-PROOF
AUDIT**. This is the current theorem statement and integration record.
The [full independent proof](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility)
reconstructs every new local step. The
[earlier ordinary-curvilinear note](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-curvilinear-torsion-and-index12)
records the route to this theorem. Previously accepted socle duality,
normal-carrier torsion/index arithmetic, C0 normal splitting, low-degree
carrier exclusions and P-010 were used as premises and were not rerun.

## 1. The local theorem

Let C be a smooth curve on a normal integral hypersurface F in a smooth
threefold over an algebraically closed field of characteristic zero.
Suppose a mate cuts the Cartier divisor nC. At P on C let r be C's
actual local Cartier index, so r divides n, and write k=n/r. A local
equation h of rC gives complete intersections W_r=(F,h) and W_n=(F,h^k).
Let A_F,P be the vanishing order of F's first normal symbol in its
saturated rank-one direction. Let D_j,P be the defect of the actual
top ordinary normal power in the actual socle of W_j. Then

```
D_n,P = (k-1) A_F,P + k D_r,P.                    (1)
```

These are the full embedded ideals, including all their higher jets.
Neither the tangent cone nor the surface multiplicity replaces r or D_r.
There is no hypothesis that the other carrier is normal or that the
global complete intersection has a primitive presentation.

The proof proceeds through three exact identities. In the normal local
surface domain, with I the curve ideal,

```
(h^k:I) = h^(k-1)(h:I),
Soc(W_n) = h^(k-1) Soc(W_r),
w=z^r/h is regular and ord_C,P(w)=A_F,P+D_r,P.
```

Here z has curve valuation one and generates the free first normal
quotient. The first two identities follow by height-one valuations and
normality. For the third, the relative Jacobian of (F,h) generates its
actual socle over k[[t]], not merely the generic socle. Its Artinian
special fiber generates the fiber socle, and finite Gorenstein duality
identifies the socle with k[[t]] compatibly with base change. Differentiating
z^r=hw modulo (F,h) then gives the stated order. Multiplication by
h^(k-1) compares the top powers and proves (1).

The primary Artinian Jacobian input is the formal, nonhomogeneous CI
theorem: [Vasconcelos, The Top of a System of Equations, Theorem 1.1,
printed page 550](https://boletin.math.org.mx/pdf/2/37/BSMM(2).37.549-556.pdf).
The independent audit also supplies
[Eisenbud–Ulrich, Theorem 8.5](https://arxiv.org/pdf/1309.2050).
Characteristic zero is sufficient for all local lengths; a proposed
positive-characteristic extension must retain the prime-to-characteristic
length condition rather than using a possibly zero Jacobian.

## 2. Ordinary free powers and a pointwise torsion identity

For any curvilinear complete-intersection thickening Y of generic
length n, put J=I_C O_Y and let T_i be the torsion of J^i/J^(i+1).
The torsion sum is a graded ideal, so the torsion-free ordinary graded
algebra remains generated in degree one. If B is its first line bundle,
then every free layer is B^i. Purity gives J^n=0 everywhere and

```
J^(n-1)=Soc(Y)(-D_n),
2 sum_i length(T_i)_P = n D_n,P.                  (2)
```

The second equality is pointwise. Complete over R=k[[t]] and compare
the full algebra with its lattice R[z]/(z^n). Its lattice index is the
total normal-layer torsion. A perfect relative Frobenius pairing has
unit Gram determinant on the full algebra and determinant valuation
n D_n,P on the powers of z. The change of lattice doubles the index,
proving (2). This is an ordinary J-adic statement; it does not set the
multiplication defects of a saturated BF filtration to zero.

## 3. A bound on every normal carrier degree from its actual local indices

For C0=[s^4:s^3t:st^3:t^4] write a=deg F, b=deg G, n=ab/4 and
B=O_P1(-ell). The accepted conormal splitting gives ell<=7. Socle
duality and the actual saturated first normal relation give

```
deg D_n = (n-1)ell - 4(a+b) + 14,
deg A_F = 4a - 14 + ell,
deg(D_n+A_F) = n(ell-16/a).
```

If all actual local indices are at most s, summing (1) implies

```
s(ell-16/a) >= 4a-14+ell.
```

For a>=5 the right side is positive. The ratio of that side to
ell-16/a decreases in ell, so ell<=7 gives

```
s >= (4a-7)/(7-16/a),
4a^2-(7s+7)a+16s <= 0.                           (3)
```

Thus a pointwise bound on actual curve indices yields a linear carrier
degree bound. The number of singular points and their higher contact
need not be bounded. This is stronger than replacing s by the potentially
much larger least common multiple of all the indices.

For a smooth rational degree-e support with balanced normal bundle
O(2e-1)^2, put lambda=2e-1. The same argument gives

```
s >= (ea-lambda)/(lambda-e^2/a)
```

in the non-Cartier case with positive denominator. The precise edge
conditions and monotonicity proof are in the independent audit. No
uniform bound on actual local curve indices is supplied by this theorem.

## 4. All normal C0 carriers with actual indices at most four are excluded

Assume every on-curve index is at most four. Their common exponent is
at most twelve. The accepted normal torsion/index reduction leaves only
the minimal pair (6,8), generic length twelve. Equivalently (3) leaves
a<=6, and the accepted Cartier integrality and low-degree exclusions
force a=6 and minimum b=8. Choosing this minimum mate loses no candidate:
the accepted class-group theorem constructs it whenever any mate exists.

At every point k=12/r>=3, so (1) gives D_n>=2A_F. A normal octic would
have deg(D_n-2A_F)=9ell-78<0 for ell<=7, an immediate contradiction.
A normal sextic instead has deg(D_n-2A_F)=9ell-62. It forces ell=7,
deg D_n=35, deg A_F=17, and total slack exactly one. Locally that slack is

```
D_n,P-2A_F,P = (k-3)A_F,P+kD_r,P.
```

An index-two point costs at least three and is impossible. Any positive
D_r,P at an index-three or index-four point costs at least three and
is likewise impossible. Thus D_r,P=0 at every such point. Formula (2)
then gives W_r=R[z]/(z^r) exactly. For j<=r its ordinary power ideal is
already R-saturated, so its symbolic j-fold curve has the same primitive
local algebra. In particular the symbolic triple is primitive at every
index-three/four point. At an index-one point the smooth curve is Cartier
on the normal hypersurface, which makes the surface smooth there;
its symbolic triple is primitive as well.

The global symbolic triple is therefore an embedded primitive triple
whose first conormal quotient is O(-7). The actual quotient map
O(-7)^2 -> O(-7) has constant direction. The accepted P-010 quadratic
obstruction is nonzero for every such direction, including the endpoints.
This is a contradiction. Hence:

**In characteristic zero, no normal integral hypersurface containing C0
can admit a mate if every actual on-curve Cartier index of C0 is at most
four, in any carrier or mate degree.**

This includes arbitrary mixtures of D/E rational double points and
A1,A2,A3 along C0 using their accepted curve-index bounds. Other
singularities of actual curve index at most four are covered as well.
Singularities away from C0 impose no extra hypothesis.

## 5. Remaining obligations

The class whose indices merely divide twelve still permits actual
index-six and index-twelve points. They have k=2 and k=1 respectively
in the length-twelve formula, so the slack argument above does not
exclude them. In particular index-twelve points may carry poles in the
first-symbol ratio. The primitive local defects D_r,P are now charged
exactly, rather than dropped.

Normal carriers with larger actual indices, nonnormal normalization and
conductor problems, multiple inverse branches and entirely thick
presentations all remain. The universal integral-curve STCI question
and unrestricted C0 remain open. This theorem establishes a structural
carrier-degree bound and a complete bounded-index exclusion; it is not
a degree-by-degree verification or a global exhaustion theorem.


---

## 2026-10-14-generalization-normal-index-general-scope-independent-audit

# Independent audit of the general normal-index consequences

Date: 2026-10-14. Author: `normal_general_threshold_audit`.
Status: **PROVED NEW CONSEQUENCES, WITH THE SCOPE BELOW.** This review
uses the accepted [local power-socle and ordinary-layer
theorem](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility)
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
[owner note](#2026-10-14-generalization-normal-index-general-scope)
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
[rational-ample torsion detection theorem](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-torsion)
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


---

## 2026-10-14-generalization-transverse-differential-socle-bound

# A full first-layer and socle bound for transverse ramification

Date: 2026-10-14. Owner: `global_structure`. Status: **NEW WRITTEN
PROOF; independent review requested**. The accepted normal bundle of
fixed C0 and accepted carrier exclusions are premises, with no reruns.
This note studies new restrictions on the three Cartier-lift models
from the [accepted classification](2026-10-14-generalization-cartier-lift-independent-audit.md).
The full socle line is the previously reviewed duality interface in the
[conormal-socle budget audit](2026-10-13-generalization-socle-independent-audit.md);
the new ingredient here is the actual first-layer identification from
the normalization differential and its ramification divisor.

## 1. Exact hypotheses and statement

Let `C subset P3` be smooth integral of degree `d` and genus `g` over
an algebraically closed field. Let `F,G` have degrees `a,b`, no common
surface component, and scheme-theoretic complete intersection `Z` with
reduced support exactly `C`. Assume `X=V(F)` is integral and regular
at the generic point of `C`. Let `nu:S->X` be the finite normalization,
and assume its full reduced inverse image of `C` is a single smooth
curve `c`, mapped isomorphically to `C`, with `c` Cartier on `S`.
In particular `S` is regular along `c`, by the Cartier-lift lemma.

Write `H=nu*O_X(1)`. The pullback mate has divisor `n c`, where

    n=ab/d,    n c~bH,    k=c^2=d^2/a.

Assume `n>=2`. At the generic point of `c`, the differential of the
composite `f:S->P3` induces an injective map of normal directions

    alpha:N_c/S=O_c(c) -> N_C/P3.

The normal bundles are restricted to `c` using its isomorphism with
`C`. Let `A` be the entire effective zero divisor of this map, so
its saturated image is the line subbundle

    B=O_c(c)(A) subset N_C/P3.

The map is generically nonzero because the carrier is generically
regular and normalization is an isomorphism there. The definition of
`A` retains every isolated ramification point, with its full common-zero
order; `A=0` is not assumed.

**Theorem.** If `J` is the nilradical of `O_Z`, then its actual first
layer has torsion-free quotient

    L=(J/J^2)_tf = O_c(-c)(-A).                         (1)

Moreover the full Gorenstein socle implies

    (n-1) deg(A) >= d(a-4)+d^2/a-(2g-2).                (2)

No primitive multiple-curve hypothesis, finite-flat retraction onto
`C`, special splitting of the normal bundle, or assumed absence of
first-layer torsion is used. The generic regularity of `X` and the
actual singleton Cartier lift are essential hypotheses.

## 2. Identification of the full first layer

Because `C` is a smooth codimension-two immersion,

    N_C/P3^*=I_C/I_C^2.

The actual nilradical is `J=I_C/I_Z`, so reduction modulo its square
gives the globally surjective map

    I_C/I_C^2 -> J/J^2,

whose kernel is the sheaf generated by the actual first normal symbols
of `F` and `G`. At the generic point, `F` has order one; after quotient
by `F`, the carrier ring is a DVR and `G` has order `n>=2`. Thus the
transverse algebra of `Z` is curvilinear of length `n`, and the two
first symbols span the single line supplied by `F`.

The differential `alpha` describes the normal tangent direction of
the normalization along `c`. On the generic regular locus this is the
normal tangent direction of `C` inside the carrier. Therefore the
generic first-symbol line is its annihilator in `N_C^*`.

The saturated image `B` is a line subbundle of `N_C`. Its annihilator
`B^perp` is a saturated line subbundle of `N_C^*`, and dualizing the
subbundle inclusion gives the surjection

    N_C^* -> B^*=O_c(-c)(-A).

Passing from `J/J^2` to its torsion-free quotient saturates exactly
the generic kernel of the preceding first-symbol map. On a smooth
curve a saturated subsheaf of a fixed vector bundle is determined by
its generic subspace. Hence that kernel is precisely `B^perp`, and
its quotient is `B^*`. This proves (1), using the full actual first
layer rather than a chosen first-jet parameterization.

## 3. Why the top multiplication is global

The complete intersection `Z` is a pure one-dimensional Cohen--Macaulay
Gorenstein scheme. Its structure sheaf has no submodule supported at
finitely many closed points. Generically its algebra is curvilinear
of length `n`, so `J^n` vanishes generically. As an ideal subsheaf of
`O_Z`, it must therefore vanish everywhere:

    J^n=0.

The ideal `J^(n-1)` is nonzero generically, has no finite-point torsion,
and is annihilated by `J`. It is consequently a torsion-free rank-one
`O_C`-module and therefore a line bundle. Multiplication defines a
global map

    (J/J^2)^(tensor(n-1)) -> J^(n-1).

Changing a representative by `J^2` changes the product by `J^n=0`.
Any torsion section in an input produces a finite-support torsion
section in the target, which is zero. Thus the multiplication factors
canonically through

    L^(tensor(n-1)) -> J^(n-1).

It is nonzero generically because the generic algebra is curvilinear.
It is therefore an injection of line bundles. This step does not
replace the full nilpotent structure by a first-jet model.

## 4. The actual Gorenstein socle and the inequality

The socle sheaf is

    Soc=Ann_O_Z(J)=Hom_O_Z(O_C,O_Z).

Finite closed-immersion duality in equal dimension identifies
`Hom_O_Z(O_C,omega_Z)=omega_C`. Since the complete intersection has
`omega_Z=O_Z(a+b-4)`, this gives the full sheaf identity

    Soc=omega_C tensor O_C(4-a-b),
    deg(Soc)=2g-2+d(4-a-b).

The inclusion `J^(n-1) subset Soc` composed with multiplication is a
generically nonzero map of line bundles. Consequently

    (n-1)(-k-deg A) <= 2g-2+d(4-a-b).

Using `n k=bd` reduces this exactly to (2):

    (n-1)deg A >= d(a-4)+k-(2g-2).

The socle is identified on the entire curve. Neither a top graded
piece with a discarded closed-point defect nor a pointwise generic
length calculation is substituted for it.

## 5. All-mate consequences on fixed C0 models

For the accepted `C0`, `d=4,g=0,N_C=O(7)^2`. A saturated line
`B=O(k+deg A)` inside this bundle has degree at most seven. Therefore

    0<=deg A<=7-k.

The degree-eight smooth quadric and quadric-cone normalization targets
have `k=2,n=2b`, so every generically regular projection admitting a
mate requires

    1<=deg A<=5,    (2b-1)deg A>=20.                    (3)

The degree-sixteen plane normalization target has `k=1,n=4b`, so

    1<=deg A<=6,    (4b-1)deg A>=51.                    (4)

In particular every transverse-coprime projection (`A=0`) is excluded
in all mate degrees. The remaining task is a finite set of nonzero
common-root-degree strata, with their actual projection maps and
conductor retained; no mate-power enumeration is needed to obtain
this reduction.

For orientation, `deg A=1` forces `b>=11` at degree eight and
`b>=13` at degree sixteen; `deg A=2` forces respectively `b>=6`
and `b>=7`. These are necessary lower bounds, not upper bounds or
constructions. The inherited all-degree-at-most-four exclusions
separately require `b>=5` for every fixed-C0 presentation.

If finite duality makes the upstairs conductor Cartier with divisor
`D=(a-4)H-K_S`, then

    D.c=d(a-4)+k-(2g-2)

by adjunction along the smooth Cartier `c`. In that case (2) says that
the total conductor contact is at most `(n-1)` times the transverse
ramification divisor degree. This interpretation is conditional on
that actual duality/divisor identification; the proof of (2) did not
assume it.

## 6. Preserved boundaries

If both ambient generators have generic normal order at least two,
the transverse algebra need not be curvilinear and the generic first
layer may have rank two; the identification (1) and this top multiplication
argument do not apply as written. If the normalization lift is non-Cartier,
its normal direction bundle and the smooth-along-lift lemma also need
replacement. If several inverse primes or a higher-degree inverse
curve occur, this single line is not the full normalization datum.

These are the precise global open boundaries. The theorem removes
the `A=0` projection stratum in all mate degrees and supplies uniform
necessary common-root bounds in the remaining Cartier-lift models.


---

## 2026-10-14-generalization-transverse-socle-independent-audit

# Independent review: the actual transverse first layer and global socle

Date: 2026-10-14. Reviewer: root. Status: **PROVED under the owner's
explicit hypotheses, in every characteristic**. The reviewed source is
[the transverse-differential theorem](#2026-10-14-generalization-transverse-differential-socle-bound).
The accepted socle-duality theorem and C0 normal splitting are inputs;
neither was recomputed.

The carrier must be regular at the generic point of the smooth support.
Its full normalization inverse support must be a singleton degree-one
smooth curve c that is Cartier upstairs. These hypotheses give a global
normal differential from `O_c(c)` to `N_C/P3`; the source surface is
regular along c. Saturating its generically nonzero image gives
`B=O_c(c)(A)` for its actual common-zero divisor A.

I independently reconstructed the first-layer identification. The
quotient of `I_C/I_C^2` by the actual first symbols of both equations
is `J/J^2`. Generic carrier regularity makes its generic quotient the
single normal direction inside the carrier. Removing torsion saturates
its kernel, and a saturated kernel is determined by its generic
subspace. This kernel is exactly the annihilator of B, hence
`(J/J^2)_tf=B^*=O_c(-c)(-A)`. This is an identification of the full
actual first layer, not a replacement by the derivative at one point.

Generic curvilinearity of length `n=ab/deg C` gives `J^n=0` everywhere
by Cohen--Macaulay purity. The top ideal `J^(n-1)` has no point torsion
and lies in the actual socle. Multiplication through the first layer
kills its torsion in every input and gives a generically nonzero map
of line bundles

```
O_c(-(n-1)c)(-(n-1)A) -> J^(n-1) -> omega_C(4-a-b).
```

Its degree inequality, using `c^2=deg(C)^2/a` and `n c^2=b deg(C)`,
is exactly

```
(n-1)deg A >= deg(C)(a-4)+deg(C)^2/a-(2g(C)-2).
```

The proof keeps the entire top-socle inclusion; its finite-point defect
can only strengthen the inequality. For C0 the image line cannot
exceed degree seven in `O(7)^2`, so the three Cartier-lift targets
have precisely the owner's bounds: degree8 requires
`1<=deg A<=5`, `(2b-1)deg A>=20`; degree16 requires
`1<=deg A<=6`, `(4b-1)deg A>=51`. The mate lower bounds for A of
degrees one and two follow by integer rounding and are correct.

This accepts the written theorem and those necessary consequences.
It neither bounds mate degree above nor proves a surviving projection
exists. The generic regularity, Cartier-lift and singleton assumptions
are essential; rank-two first layers in entirely thick cases and
non-Cartier lifts remain outside the argument. The optional conductor
intersection interpretation needs its additional duality hypothesis
and is not used to prove the inequality.


---

## 2026-10-14-generalization-pointwise-conductor-socle-independent-audit

# Exact pointwise conductor contact and the top-socle defect

Date: 2026-10-14. Status: **NEW POINTWISE STRENGTHENING PROVED UNDER
THE STATED CHARACTERISTIC-ZERO HYPOTHESES**. Independent review of the
proposed argument, with separate checks of actual-socle specialization
and the divisor comparison. This note supplies a new proof and scope
record; no old computation, carrier exclusion, or accepted proof was
replayed.

Accepted inputs are the
[transverse first-layer/socle theorem and independent review](#2026-10-14-generalization-transverse-socle-independent-audit)
and the actual conductor residue identities in the
[conductor--Jacobian bridge](2026-10-14-generalization-projection-conductor-jacobian-bridge.md).
The standard characteristic-zero Artin complete-intersection theorem
that the Jacobian determinant generates its socle is also an input.
The new steps below justify its use for the **actual relative socle at
every point**, the injection into the normalized thickening, and the
resulting exact divisor comparison.

## 1. Statement and definition of the defect

Let `M` be a smooth threefold over an algebraically closed field of
characteristic zero, and let `C` be a smooth curve. Suppose

```
Y=(F,G),               Supp(Y)_red=C,
```

is an actual complete intersection. Assume the integral carrier
`X=(F=0)` is regular at the generic point of `C`. Let `nu:S -> X` be
its finite normalization. Require that the full reduced inverse support
of `C` is a singleton smooth Cartier curve `c`, mapped isomorphically
to `C`, and that `S` is smooth along `c`.

Let the actual conductor near `c` be the invertible ideal

```
conductor O_S=O_S(-B),
```

where `B` is effective and has no component `c`. Let `A` be the full
zero divisor, with common-zero multiplicities, of

```
alpha:O_c(c) -> N_(C/M).
```

Write `nu*G=unit*u^n` locally along `c`, where `u=0` defines `c` and
`n>=2`. Thus the actual generic normal algebra is curvilinear of
length `n`. Put `J=I_C O_Y` and `Soc(Y)=Ann_(O_Y)(J)`. The accepted
socle theorem identifies this as an invertible sheaf on `C`; purity
gives `J^n=0`, and `J^(n-1)` is an invertible subsheaf. Define its
actual top-power/socle defect divisor `D_n` by

```
J^(n-1)=Soc(Y)(-D_n).                                 (1)
```

Equivalently this is the defect of the multiplication map from
`L^(tensor(n-1))` to the full actual socle, where
`L=(J/J^2)_tf=O_c(-c)(-A)`. Multiplication onto `J^(n-1)` is surjective:
it is generated by products of `n-1` elements of `J`; terms from `J^2`
change such a product by `J^n=0`, and torsion in a first-layer input
maps to zero in the torsion-free target. Consequently no extra defect
is inserted between this multiplication image and the actual top
ordinary power.

**Theorem.** There is an equality of actual divisors on `c=C`:

```
D_n=(n-1)A-B|c.                                       (2)
```

In particular, for every closed point `P`,

```
(n-1)A_P >= (B|c)_P.                                 (3)
```

This is stronger than an equality of degrees or divisor classes. No
primitive multiple-curve hypothesis, absence of first-layer torsion,
or global retraction onto `C` is assumed.

## 2. The actual CI embeds in the normalized thickening

Fix a closed point `P` of `C` and its unique inverse point on `c`.
Choose completed ambient coordinates `(t,y,z)` with `C=(y,z)` and
`t|C` a uniformizer. The pullback of `t`, together with a local
equation `u` of `c`, gives regular parameters on `S`. Thus

```
R=Bbbk[[t]],
Lambda=R[[y,z]]/(F,G),
nu(t,u)=(t,Y(t,u),Z(t,u)),          Y,Z in (u).
```

The full inverse-support hypothesis makes

```
g=nu*G=gamma(t,u)u^n,              gamma a unit.       (4)
```

Indeed the regular local surface ring is factorial, and `c` is the
only prime in the support of the pullback mate. Generic carrier
regularity identifies its multiplicity with the actual generic
complete-intersection length `n`.

The finite map induces

```
Lambda -> T=R[[u]]/(u^n).                             (5)
```

This map is injective. Its kernel vanishes at the generic point of
`C`, where normalization is an isomorphism. It therefore has finite
support. But `Lambda` is a pure one-dimensional complete intersection
and has no nonzero finite-length submodule. Equivalently, `Lambda`
is finite free over `R`: support on `C` gives finiteness, and the
parameter `t` is a nonzerodivisor by Cohen--Macaulay purity. Its rank
is `n`. The target is also free of rank `n`, so (5) is generically an
isomorphism with a finite-length cokernel.

That cokernel is retained. The proof does not replace the actual
complete intersection by the normalized thickening.

## 3. The relative Jacobian generates the actual socle

Let

```
j=F_y G_z-F_z G_y,
Sigma=Ann_Lambda((y,z)Lambda).
```

The generic Artin complete-intersection Jacobian theorem puts `j` in
the socle after inverting `t`. Since `Lambda` is `R`-torsion free,
the equalities `yj=zj=0` then hold in `Lambda` itself. Hence `j in Sigma`.

The relative socle `Sigma` is a free rank-one `R`-module. Its rank is
one generically, and it is an `R`-submodule of the finite free module
`Lambda`. It is also saturated in `Lambda`: if `t a in Sigma`, then
`t ya=t za=0`, so torsion freeness gives `ya=za=0`. It follows that

```
Sigma/t Sigma -> Lambda/t Lambda
```

is injective. The special fiber

```
Lambda/t Lambda
 = Bbbk[[y,z]]/(F(0,y,z),G(0,y,z))
```

is an Artin complete intersection of length `n`, because `Lambda`
is free of rank `n`. The image of `j` is precisely its Jacobian
determinant and is a nonzero socle generator in characteristic zero.
Thus `j` is nonzero in `Sigma/t Sigma`, and Nakayama gives

```
Sigma=R j.                                           (6)
```

This proves the actual generator statement at the closed point. It
does not assume in advance that taking socles commutes with base
change. In particular, no hidden nonunit specialization factor is
allowed in (6).

## 4. Exact images of the socle and top ordinary power

Let `h` be a local generator of the actual conductor. The accepted
residue identities give a single unit `epsilon` with

```
F_y composed with nu = -epsilon h Z_u,
F_z composed with nu =  epsilon h Y_u.                (7)
```

Since the ambient coordinate `t` pulls back to the chosen parameter
`t`, the chain rule and (4) give

```
j composed with nu
 = -epsilon h (Z_u(G_z composed with nu)
                        +Y_u(G_y composed with nu))
 = -epsilon h partial_u(g)
 = -epsilon h (n gamma u^(n-1)+gamma_u u^n).
```

In `T`, this is

```
j composed with nu
 = -n epsilon(t,0) gamma(t,0) h(t,0) u^(n-1).          (8)
```

The coefficient other than `h(t,0)` is a unit. Therefore (6) yields
the exact image

```
im(Sigma)=h(t,0)R u^(n-1).                            (9)
```

Write

```
a=A_P=min(ord_t Y_u(t,0),ord_t Z_u(t,0)),
b=(B|c)_P=ord_t h(t,0).
```

The second order is finite because the conductor has no component
`c`. Write `Y=u a_1(t)+O(u^2)`, `Z=u a_2(t)+O(u^2)`. Every product
of `n-1` elements of the actual ideal `J=(y,z)Lambda` maps to
`u^(n-1)` times a coefficient in `(a_1,a_2)^(n-1)`; all higher
`u` terms vanish. Conversely the monomials in `y,z`, with arbitrary
coefficients from `R`, realize that whole coefficient ideal. Hence

```
im(J^(n-1))
 = (Y_u(t,0),Z_u(t,0))^(n-1) R u^(n-1)
 = t^((n-1)a)R u^(n-1).                              (10)
```

The injection (5) shows in particular that `J^n=0` and that its actual
top power is exactly the lattice in (10). Comparing (9) and (10)
gives

```
length_R(Sigma/J^(n-1))=(n-1)a-b >=0.                 (11)
```

By definition, this length is `D_(n,P)`. Equality (2) follows point by
point; faithful flatness of completion recovers the original local
divisor multiplicities.

This computation also confirms the suggested generator comparison:
after a local invertible linear change of the ambient normal coordinates,
one normal function `w` has
`nu*w=t^a unit*u+O(u^2)` and maps to a generator of the torsion-free
first layer. Then `w^(n-1)/j` has order exactly `(n-1)a-b`. Formula
(10) avoids choosing `w` and retains the entire actual top ideal.

## 5. Consequences across all mate powers

For a fixed carrier and its fixed normalization data, (3) supplies
necessary conditions in every mate multiplicity at once:

- `Supp(B|c) subset Supp(A)`. A conductor contact with `A_P=0` excludes
  every mate satisfying these hypotheses, regardless of its degree.
- At each point with `A_P>0`,
  `n>=1+ceil((B|c)_P/A_P)`.
  Their maximum is a simultaneous necessary lower bound for `n`.
- The entire actual defect is determined by the same divisor formula
  for every permitted mate multiplicity. No closed-point correction
  or higher-jet defect has been omitted from `D_n`.

Taking degrees recovers the accepted conductor-contact inequality.
In projective space, the accepted adjunction expression
`B.c=d(a-4)+c^2-(2g-2)` identifies it with the earlier transverse
socle bound. That numerical consequence is used as a consistency
check, not as a substitute for the new pointwise proof.

The pointwise necessary conditions neither bound mate multiplicity
above nor settle the residual phase/torsion conditions for conductor
descent. Vanishing of the displayed defect does not by itself supply
a projective mate.

## 6. Exact colength in the thickening on the carrier normalization

There is a further pointwise consequence using the accepted ordinary
[Frobenius/free-powers lattice identity](#2026-10-14-generalization-normal-index-socle-theorem),
Section 2. Keep the local notation above and choose `w in J` mapping to
a generator of the torsion-free first layer, so

```
nu*w=t^a q(t)u+O(u^2),                 q(t) a unit.
```

The ordinary free-powers lattice is
`Lambda_0=R[w] subset Lambda`, isomorphic to `R[v]/(v^n)`, with basis
`1,w,...,w^(n-1)`. The accepted lattice identity is

```
length_R(Lambda/Lambda_0)=n D_(n,P)/2.                 (12)
```

Relative to this basis and `1,u,...,u^(n-1)` of `T`, the inclusion
`Lambda_0 -> T` is triangular, with diagonal

```
1, t^a q, (t^a q)^2, ..., (t^a q)^(n-1).
```

Consequently its determinant has valuation `n(n-1)a/2`; the higher
coefficients of `nu*w` make no contribution. The actual inclusions
`Lambda_0 subset Lambda subset T` give the exact sequence

```
0 -> Lambda/Lambda_0 -> T/Lambda_0 -> T/Lambda -> 0.
```

Subtracting lengths and applying (2) yields the new exact formula

```
length_R(T/Lambda)
 = n((n-1)a-D_(n,P))/2
 = n(B|c)_P/2.                                       (13)
```

Thus if `delta_n` is the effective divisor recording these local
colengths, one has

```
2 delta_n=n B|c.                                     (14)
```

In particular, **odd `n` forces every coefficient of `B|c` to be
even**. This is a necessary condition on every actual CI in this
lane; arbitrary normalized support or a graded construction alone
does not supply the lattice inclusions used in the proof.

Here `T=O_S/(nu*G)` locally is the **normalized thickening**, meaning
the pullback thickening on the normalization of the carrier `X`.
It is not asserted to be a normalization of the nonreduced scheme
`Y`. Formula (13) measures the finite colength of the actual CI
inside this specified pullback thickening.

Finally the accepted
[length-two/three primitive theorem](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-symbolic-triple-certificate),
Section 2, gives `D_n=0` for `n in {2,3}`. Hence in these two lengths
the pointwise divisor relation specializes to

```
B|c=(n-1)A.                                         (15)
```

These are consequences of accepted lattice and small-rank premises;
neither earlier proof was rerun.

## 7. Scope and audit disposition

The proposed identity passes under all the explicit hypotheses. The
two potentially delicate bridges both pass: purity gives the
injection into `T`, and saturation plus the Artin-fiber Jacobian
theorem gives the actual relative-socle generator at every point.
Finite colength of `Lambda` in `T` contributes no additional term
to (2).

Characteristic zero is substantive for this proof: the factor `n`
in (8) and nonvanishing of the Artin Jacobian must be retained. The
same argument works when the characteristic does not divide `n`;
there is no claim here in characteristic dividing `n`. For example,
`F=y,G=z^p` in characteristic `p` has a nonzero socle but zero
Jacobian. Generic carrier regularity, singleton degree-one inverse
support, the Cartier lift, smoothness of the normalization along the
lift, and the actual supported complete intersection are also
substantive hypotheses. No extension to several inverse branches,
non-Cartier lifts, singular normalization along the lift, or entirely
thick carriers is inferred.

The universal STCI question and unrestricted characteristic-zero
`C0` remain open.
