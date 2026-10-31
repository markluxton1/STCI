# normal index socle and torsion

## Integration guide: numerical indices and actual symbolic structures

The [general index scope](#2026-10-14-generalization-normal-index-general-scope) derives inequalities that may be applied before a second defining surface is chosen; the [socle theorem](#2026-10-14-generalization-normal-index-socle-theorem) then imposes additional local structure under its exact assumptions. The independent audit distinguishes scalar inequalities from stronger equality-case conclusions and records characteristic restrictions.

[Symbolic carrier torsion](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-torsion) provides Cartier-index and divisor-class information, while [normal flatness](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-generic-ci-normal-flatness) concerns propagation of a filtered complete-intersection structure. Neither a favorable scalar budget nor a formal normal carrier supplies a global second equation automatically. Conversely, the presence of a mate introduces additional numerical constraints that should not be silently assumed in the one-carrier arguments.

Preserve the equality-case, characteristic, and pointwise-index qualifications in the original audits.

---


Permanent mathematical dossier. Complete source arguments are preserved with their precise hypotheses, conditional scope, calculations, failed approaches, and unresolved boundaries. This grouping does not promote claims to canonical results.

---

<a id="2026-10-14-generalization-normal-index-general-scope"></a>

## An intrinsic normal divisor and index thresholds for smooth curves

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

### 1. The comparison exists before a mate does

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

#### Construction and divisor

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

### 2. A mate adds a numerical ray, not another power problem

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

### 3. General normal-bundle and pointwise-index bounds

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

### 4. A uniform threshold for balanced rational curves

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

#### The exact threshold is structurally rigid

If all actual indices are at most e-1, set s=e-1 in (9):

    e[a-(e-1)] (a-e) <= 0.

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

### 5. Distribution constraints retain more than a maximum

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

### 6. Characteristic and remaining scope

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

<a id="2026-10-14-generalization-normal-index-socle-theorem"></a>

## Normal carriers: local power-socle compatibility and uniform exclusion

Date: 2026-10-14. Status: **PROVED, WITH A SEPARATE INDEPENDENT NEW-PROOF
AUDIT**. This is the current theorem statement and integration record.
The [full independent proof](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility)
reconstructs every new local step. The
[earlier ordinary-curvilinear note](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-curvilinear-torsion-and-index12)
records the route to this theorem. Previously accepted socle duality,
normal-carrier torsion/index arithmetic, C0 normal splitting, low-degree
carrier exclusions and P-010 were used as premises and were not rerun.

### 1. The local theorem

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

### 2. Ordinary free powers and a pointwise torsion identity

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

### 3. A bound on every normal carrier degree from its actual local indices

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

### 4. All normal C0 carriers with actual indices at most four are excluded

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

### 5. Remaining obligations

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

<a id="2026-10-14-generalization-normal-index-general-scope-independent-audit"></a>

## Independent audit of the general normal-index consequences

Date: 2026-10-14. Author: `normal_general_threshold_audit`.
Status: **PROVED NEW CONSEQUENCES, WITH THE SCOPE BELOW.** This review
uses the accepted [local power-socle and ordinary-layer
theorem](NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility)
as a premise. It does not rerun that proof, any accepted curve
obstruction, or any CAS computation. The new work checked here is the
degree-independent inequality, its integer and equality consequences,
the tame-characteristic scope, and the intrinsic version without a mate.

### 1. The scalar inequality does not need a denominator assumption

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

### 2. Balanced rational curves: the smallest possible index

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

### 3. The equality case yields a primitive triple only for e>=4

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

### 4. Tame positive characteristic needs r_P invertible, not n

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

### 5. Intrinsic divisor identity without assuming a mate

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

### 6. Audit conclusion and limits

The general inequality, index threshold, exact equality consequences,
conditional primitive-triple obstruction, tame extension, and
intrinsic line-bundle identity all pass this independent scope review.
The relevant qualifications are e>=4 for the triple conclusion, an
actual embedded-triple obstruction rather than a numerical substitute,
tameness of every actual local index in positive characteristic, and
the explicit surviving-line convention when R=1. None of these results
bounds actual indices for arbitrary normal carriers, handles wild
indices, or excludes all balanced rational curves from being STCI.

### 7. Addendum: direct construction on a smooth projective threefold

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

### 8. Characteristic-zero equality gives an actual minimal primitive CI

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

<a id="2026-10-14-generalization-transverse-differential-socle-bound"></a>

## A full first-layer and socle bound for transverse ramification

Date: 2026-10-14. Owner: `global_structure`. Status: **NEW WRITTEN
PROOF; independent review requested**. The accepted normal bundle of
fixed C0 and accepted carrier exclusions are premises, with no reruns.
This note studies new restrictions on the three Cartier-lift models
from the [accepted classification](QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md#2026-10-14-generalization-cartier-lift-independent-audit).
The full socle line is the previously reviewed duality interface in the
[conormal-socle budget audit](SOCLE_AND_LOEWY_BOUNDS.md#source-2026-10-13-generalization-socle-independent-auditmd);
the new ingredient here is the actual first-layer identification from
the normalization differential and its ramification divisor.

### 1. Exact hypotheses and statement

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

### 2. Identification of the full first layer

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

### 3. Why the top multiplication is global

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

### 4. The actual Gorenstein socle and the inequality

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

### 5. All-mate consequences on fixed C0 models

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

### 6. Preserved boundaries

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

<a id="2026-10-14-generalization-transverse-socle-independent-audit"></a>

## Independent review: the actual transverse first layer and global socle

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

<a id="source-2026-10-14-generalization-ribbon-independent-reviewmd"></a>

## Independent written review of the symbolic-ribbon generalization

Date: 2026-10-14. Reviewer: `global_structure`, distinct from the author
`ribbon_general`. Status: **NEW CONDITIONAL THEOREM REVIEWED; root
acceptance remains separate**. This is mathematical review of a new
written proof. No accepted repository statement or verifier was rerun.

The reviewed source is
[the symbolic-ribbon criterion](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-ribbon-numerical-criterionmd).
I independently reconstructed its sheaf arguments, multiplication maps,
Euler identity and all displayed numerical specializations. The theorem
is sound under its stated normality, smooth curve, actual Cartier
relation, finite normalized-carrier map and degree-one-lift hypotheses.
Its conormal inequality additionally requires the stated generically
nonzero first-layer map; the valuation version instead measures its
first surviving layer.

### 1. What makes the symbolic double an entire ribbon

On a normal surface every divisorial ideal `I_i=O(-ic)` is reflexive
and has depth two at closed points. The quotient of `I_i` by
`I_(i+1)` has depth at least one by the depth lemma. The quotient is
annihilated by the reduced curve ideal `I_1`, has generic rank one
on `c`, and has no finite-point torsion. Because `c` is smooth it is
therefore a line bundle `E_i`, including at singular points of the
ambient normal surface.

The defining valuation inequalities prove `I_1^2 subset I_2` and
`sqrt(I_2)=I_1`. Hence `O/I_2` has square-zero nilideal `E_1` and
is Cohen--Macaulay of generic length two. This is the entire symbolic
ribbon; no Cartierness of `2c` has entered. The corresponding assertion
for ordinary ideal squares would not follow from this proof.

### 2. Multiplication and the actual Cartier relation

Products of representatives descend to

    E_i tensor E_j -> E_(i+j)

because changing a representative introduces a product in
`I_(i+j+1)`. This is an `O_c`-linear map, generically an isomorphism,
and therefore an injection of line bundles. Its zero divisor is
effective. Associativity verifies the coefficientwise defect
inequality in the author's note.

If `rc~bH` is Cartier, the equality of divisorial sheaves is

    I_(i+r)=I_i tensor O(-rc).

It gives `E_r=O_c(-bH)` and the stated periodicity. Multiplying a
layer until its index is a multiple of `r` gives

    deg E_j <= -j d^2/a,

since `rd=ba`. This is independent of whether any ambient first
normal direction survives.

### 3. The Euler identity and conormal bounds

The hyperplane Euler difference computes

    chi(O_S(mH))=(a/2)m^2-(kappa/2)m+chi(O_S).

For the carrier application a general Cartier hyperplane section
avoids the isolated normal-surface singularities. The arithmetic
Euler difference also works without requiring its geometric
smoothness. Subtracting the value at `m=-b` from that at zero and
using the symbolic filtration yields

    sum_(i=0)^(r-1) deg E_i
      =-(ab^2+b kappa)/2-r(1-g).

Thus the arbitrary surface Euler constant cancels. The inequality
`deg E_i>=i ell`, for `ell=deg E_1`, gives exactly the author's
bound for `r>=2`. For `r=2` no higher multiplication defect remains,
so the bound is an equality.

A generically nonzero map `N_C*->E_1` gives a generically injective
dual map `E_1^{-1}->N_C`. Saturating this line can only increase
its degree. Therefore `ell>=-M` whenever `M` bounds all line
subbundle degrees of `N_C`. The larger splitting degree supplies
the exact `M` on `P1`; semistability supplies the separate claimed
slope bound on an arbitrary smooth curve.

The valuation refinement is also valid globally. If `q` is the
minimum generic valuation of the pulled-back ambient curve ideal,
that ideal lies in `I_q` by its defining valuation, and its square
lies in `I_(2q) subset I_(q+1)`. Passing to `E_q` therefore gives
a map from the ambient conormal bundle. It is generically nonzero
by the definition of `q`, so the periodicity and saturation argument
give `q d^2<=a M`. This does not manufacture singleton support or
an isomorphic lift; those remain assumptions.

### 4. Numerical scope and one corrected sentence

Substitution of `M=2d-1,g=0,kappa=2pi-a-2` gives

    r[d^2-a(2d-1)]+2d(pi-1)+a(d+1)<=0.

At `a=d` it reduces to `2pi<=(r-1)(d-1)`. At `r=2,a=d`, the
nilbundle has degree exactly `-d-2pi`. This proves the all-degree
balanced-rational Cartier-double obstruction `2pi>d-1`, conditional
on the actual double relation and nonzero first conormal map.

The accepted quintic input gives only `ell<=-7/2`, hence
`-7<=ell<=-4`; the new criterion does not exclude it. The existing
quartic bisection instance is used as an accepted specialization,
not reverified.

During review I found one overbroad monotonicity sentence: increasing
`r` need not weaken the Euler bound merely because `pi>=g` when
`a` and `d` differ. The author corrected this before finalization.
Writing the upper bound as

    -A-(A+B)/(r-1),
    A=d^2/a, B=d kappa/a+2(1-g),

shows that enlargement weakens it precisely when `A+B>=0`.
For `a=d` this sign is `2(pi-g)`. No theorem conclusion depended
on the former broad sentence.

This review accepts the stated conditional inequalities and ribbon
construction. It supplies no global Cartier-index bound, no
classification of the multiplication defects, no exclusion for
multiple normalization primes, and no unrestricted STCI resolution.


---

<a id="source-2026-10-14-normal-carrier-picard-local-torsion-primarymd"></a>

## Normal carrier Picard and local torsion: primary sources and new index audit

Date: 2026-10-14. Owner: `normal_torsion_primary`, child of `conductor_general`.

Scope: integral normal hypersurface surface `X` in projective three-space over an algebraically closed characteristic-zero field. The smooth rational quartic `C0` is fixed. Previously accepted exclusions of all mates of degree at most four are premises; no inherited verification was rerun. This note records new source checks and new numerical deductions only.

### 1. Picard torsion vanishes; Weil class torsion need not vanish

**KNOWN, primary theorem.** [Grothendieck, SGA 2, Expose XII, Corollary 3.5](https://wstein.org/sga/circle/SGA2.pdf), printed p.120, PDF page 128: for a projective scheme `V`, an ample invertible sheaf, and a regular section with zero scheme `Z`, the map of etale fundamental groups is surjective when the ambient depth at closed points is at least two. With depth at least three at closed points of `Z`, and purity at closed points outside `Z`, it is an isomorphism. Regular local rings give the required purity.

Apply this with `V=P3`, the ample sheaf `O(a)`, and the equation of `X`. The ambient local rings have depth three and are regular everywhere. Thus `pi_1^et(X)=pi_1^et(P3)=1`. The triviality for projective space can also be obtained by repeated applications of the same corollary starting with `P1`, whose connected finite etale covers are trivial by Riemann-Hurwitz.

**PROVED consequence.** [Stacks Project, Kummer theory, Lemma 59.28.1](https://stacks.math.columbia.edu/tag/03PK) applies to every positive integer in characteristic zero. Since the only global units on integral proper `X` are constants and the field is algebraically closed, Kummer gives

`Pic(X)[n] = H^1_et(X,mu_n) = Hom_cont(pi_1^et(X),mu_n) = 0`.

Therefore `Pic(X)` is torsion-free. This statement does **not** imply that `Cl(X)` is torsion-free.

**KNOWN, primary local-global sequence.** [Hartshorne--Polini, Divisors Class Groups of Singular Surfaces, Proposition 2.2(c)](https://arxiv.org/pdf/1301.3222), pp.2--3, gives the sequence of Picard, almost Picard, and local almost Picard groups. For a normal surface it specializes to

`0 -> Pic(X) -> Cl(X) -> direct_sum_{P in Sing(X)} Cl(O_X,P)`.

Exactness at `Cl(X)` is the required assertion; no surjectivity onto the direct sum is assumed. Picard torsion-freeness implies that localization is injective on the torsion subgroup of `Cl(X)`.

### 2. Exact local-index formula for the normal quartic carrier

Write `a=deg X`, `g=gcd(a,4)`, `mu=a/g`, `v=4/g`, and

`Delta0 = mu[C0] - v[H]`.

Assume `Delta0` has finite order `t`; this is the accepted normal-carrier mate criterion. The accepted exact progression of mate degrees gives `b_min=v*t`.

**PROVED HERE.** Let `r_P` be the algebraic local Cartier index of `C0` at `P in C0 intersect Sing(X)`. These indices are finite: the torsion relation makes `t*mu*C0` Cartier. Off `C0`, the local class of `Delta0` is zero. At a point on `C0` its local class is `mu[C0]_P`, hence its order is `r_P/gcd(r_P,mu)`. Injectivity of localization on global torsion gives

`t = lcm_P (r_P/gcd(r_P,mu))`.

Set `R=lcm_P r_P`, using `R=1` for the empty set. For each prime `ell`, the valuation on the preceding least common multiple is

`max_P max(v_ell(r_P)-v_ell(mu),0) = max(v_ell(R)-v_ell(mu),0)`.

Consequently

`t = R/gcd(R,mu)` and `b_min = (4/g)*R/gcd(R,a/g)`.

If `R` divides `a=g*mu`, the valuation formula gives `t` dividing `g`, so `b_min<=4`. The accepted low-degree exclusions therefore imply:

**Every normal carrier admitting a mate must have at least one singular point on `C0` whose local Cartier index does not divide the carrier degree.**

The special case `C0` disjoint from `Sing(X)` has `R=t=1` and is excluded. The same conclusion follows directly because then `C0` is Cartier everywhere, so `Delta0` is a torsion element of `Pic(X)` and must vanish.

### 3. Ordinary nodes and bounded local exponents

**KNOWN, primary local class computations.** [Brevik--Nollet, Local Picard Groups, Sections 4.1.1--4.1.3](https://arxiv.org/pdf/1110.1867), pp.8--9, give the completed rational-double-point class groups:

| Type | Completed local class group | Exponent |
|---|---|---|
| `A_n` | `Z/(n+1)` | `n+1` |
| `D_n`, `n` odd | `Z/4` | `4` |
| `D_n`, `n` even | `(Z/2)^2` | `2` |
| `E_6` | `Z/3` | `3` |
| `E_7` | `Z/2` | `2` |
| `E_8` | `0` | `1` |

Their Proposition 2.4 uses the injective map from the algebraic local class group to the completed class group. Its injectivity follows by faithful flat descent: if the completed rank-one reflexive module is free, the original module is free. In this normal excellent setting completion preserves the relevant rank-one reflexive module.

Source caution: the introductory summary at the beginning of their Section 4 reverses some `D_n` parity and `E_6/E_7` assignments. The detailed subsections and the introduction's explicit `D_n` discussion agree with the table above; use those precise locations.

**PROVED HERE, node corollary.** At an ordinary node, completion has exponent two, so `r_P` divides two. A smooth curve through a singular surface point cannot be Cartier: if its local ideal is `(f)`, the one-dimensional quotient is regular, giving embedding dimension of the surface local ring at most two, hence regularity. Thus a node on `C0` has `r_P=2`.

If all singularities on `C0` are ordinary nodes, `R` is one or two. For even `a`, `R` divides `a`; all these carriers are excluded. For odd `a`, the torsion formula alone requires a node on `C0`, and then `g=1`, `mu=a` odd, `R=t=2`, and `b_min=8`. The stronger Cartier-intersection constraint in Section 6 also excludes this odd-degree possibility. Thus the final result excludes all normal carriers with only ordinary nodes on `C0`, in every carrier degree covered by the accepted low-degree-carrier exclusions.

More generally, if every on-curve local class group has exponent dividing `L`, then `R` divides `L` and

`t divides L/gcd(L,mu)`, so `b_min <= (4/g)*L/gcd(L,a/g)`.

All new formulas and both node parity consequences passed an independent symbolic argument supplied to `conductor_general`. Algebraic local indices, not an unsupported equality between algebraic and analytic class groups, are used throughout.

### 4. Failure shield: normal hypersurface class groups can have torsion

**KNOWN construction plus explicit consequence.** [Elsenhans--Jahnel, Kummer Surfaces and the Computation of the Picard Group, Sections 4.2--4.3](https://arxiv.org/pdf/1109.4346), pp.6--7, describe a Kummer quartic `Q` with sixteen ordinary nodes, its abelian double cover, and the divisibility of the exceptional sum on the resolution `S`:

`2 alpha = E_1+...+E_16` in `Pic(S)`.

The exceptional curves are linearly independent over the rationals, as their intersection matrix is diagonal with entries `-2`. Under `Pic(S)=Cl(S) -> Cl(Q)`, the class of `alpha` has order two: its double is exceptionally supported, while `alpha` cannot be an integral combination of the `E_i`. Thus a normal quartic hypersurface has nonzero torsion in its Weil class group, although its Picard group is torsion-free.

This example defeats any unrestricted claim that normal projective hypersurfaces in `P3` have torsion-free `Cl`. It supplies no normal carrier for `C0` satisfying the required torsion relation; that is a separate problem.

### 5. Precise cyclic-cover source and its scope

[Ambro, Cyclic Covers and Toroidal Embeddings, Section 4, Lemmas 4.1--4.2](https://arxiv.org/pdf/1310.3951), pp.25--26, prove that a torsion Weil divisor of exact order `t`, with `t` prime to the characteristic, gives an irreducible normal cyclic cover of degree `t` by adjoining the root of a principal representative of `tD`. Lemma 3.5, p.22, gives the codimension-one ramification index `t/gcd(t,ord_E(phi))`; the proof of Lemma 3.6, p.23, gives etaleness on the regular locus when `D` is integral. Hence the torsion cover is quasi-etale, rather than necessarily etale at singular points.

Source caution: Theorem 0.1(a)'s introductory phrase about the entire etale locus, if read literally for non-Cartier integral `D`, is overbroad and conflicts with the stated flatness criterion. The precise later lemmas and the local Cartier argument are sufficient here. Do not use that introductory phrase to erase singular-point ramification.

No statement about the fundamental group of `X_reg` being trivial has been obtained or assumed. The Kummer example proves that such a general assertion is false. No universal bound on `t` across unbounded carrier degree is claimed.

### 6. New integral Cartier-intersection constraint and finite index families

Added on 2026-10-14 after the preceding source work. This is a new independent audit of the root's suggested strengthening, not a replay of an inherited computation.

**PROVED HERE.** Under the mate relation, `C0` is Q-Cartier. By the definition of each algebraic local index, `R*C0` is Cartier at every singular point on `C0`. It is automatically Cartier at regular points and, as a divisor, is zero locally outside `C0`. Therefore `R*C0` is globally Cartier.

If a mate gives `m*C0 ~ b*H`, intersection with `H` gives `4m=ab`, so `b/m=4/a`. The rational self-intersection is consequently

`C0^2 = (b/m)(H.C0) = 16/a`.

Equivalently, one can avoid treating the Q-Cartier self-intersection as a separate definition: restrict the line-bundle relation for `m*R*C0 ~ b*R*H` to `C0`, then take integer degrees and divide by `m`. Since `H|C0` has degree four, this gives

`deg(O_X(R*C0)|C0) = 4bR/m = 16R/a`.

The left side is the degree of an actual invertible sheaf on the smooth projective curve. It is an integer, hence

`a divides 16R`.

This argument would also work for an integral projective curve of degree `d`, giving `a divides d^2 R`, whenever the mate relation and actual local Cartier indices exist.

**PROVED finite arithmetic consequences.** Assume the accepted exclusion of normal carrier degrees at most four, so a surviving carrier has `a>=5`. If every local index divides a fixed integer `L`, enumerate only

`R|L`, `a|16R`, `g=gcd(a,4)`, `t=R/gcd(R,a/g)`, `b_min=(4/g)*t>4`.

An elementary integer divisor enumeration gives:

| Local index bound | Surviving `(a,R,t,b_min)` |
|---|---|
| `L=2` | none |
| `L=3` | none |
| `L=4` | none |
| `L=6` | none |
| `L=12` | `(6,12,4,8)` and `(8,12,6,6)` |

For `L=12`, the proper-divisor values `R=1,2,3,4,6` are already excluded by the preceding rows. For `R=12`, the carrier degrees to inspect are the divisors of `192` at least five: `6,8,12,16,24,32,48,64,96,192`. Substitution in the exact torsion formula leaves precisely `6` and `8`; the degree `12` case has mate degree four and the remaining cases have smaller mates. The enumeration was also checked with a short Python integer-divisor loop; this is elementary arithmetic verification, not a new CAS certificate or a rerun of an old verifier.

**Final node conclusion.** On-curve ordinary nodes give `R<=2`, so `a|32`. No odd carrier degree at least five divides `32`; the even degrees have already been excluded by `b_min<=4`. Hence all normal `C0` carriers whose on-curve singularities are ordinary nodes are excluded, assuming the accepted carrier-degree-at-most-four exclusions. Singularities away from `C0` are unrestricted in this statement.

The two `L=12` rows are only necessary arithmetic survivors. No existence statement, classification of actual on-curve ADE configurations, or global normal-carrier resolution follows from this table alone.


---

<a id="source-2026-10-14-generalization-normal-carrier-torsion-filtermd"></a>

## All-degree torsion filter for normal carriers of fixed C0

Date: 2026-10-14. Owner: `global_structure`. Status: **NEW DIRECT
COROLLARY OF ACCEPTED PREMISES; independent review requested**.
No earlier verifier or proof was rerun.

### 1. Exact divisor-class criterion

Let `X subset P3` be a normal integral surface of degree `a` containing
the fixed smooth rational quartic `C0`, over an algebraically closed
field of characteristic zero. Let `H=O_X(1)` and let `c` be the
smooth Weil prime `C0` on `X`. Put

    h=gcd(a,4),    u=a/h,    v=4/h,
    Delta=u c-v H in Cl(X).

If a degree-`b` mate exists, its Cartier divisor is `m c` and
intersection with `H` gives `4m=ab`. Hence `m=u k,b=v k` and

    k Delta=0.

Conversely, if `Delta` is torsion of order `t`, its class relation
`t u c~t v H` supplies a global section of `O_X(tv)` with divisor
exactly `tu c`. Normality means no conductor descent remains. The
hypersurface restriction sequence lifts this section to an ambient
form of degree `tv`, giving a mate. Every normalized mate section is
unique up to scalar at its degree, because its specified divisor is
fixed and `X` is proper integral.

Therefore the complete normal-carrier criterion is:

    a mate exists iff Delta is torsion;
    if it does, its minimum mate degree is b_min=t*4/gcd(a,4).  (1)

This statement uses normality, not smoothness or Cartierness of `c`.
It covers arbitrary singularities and arbitrary carrier degree.

### 2. The accepted low-degree theorem forces nonzero torsion

The accepted fixed-C0 plane/quadric/cubic/quartic exclusions prohibit
any ambient mate of degree at most four, regardless of the other
carrier degree. If `Delta=0`, the converse construction above gives
a mate of degree `v`, which is one, two, or four. This is impossible.

Consequently every surviving normal carrier with a mate has

    Delta nonzero torsion,   t*v>=5.                         (2)

In particular **every normal carrier with torsion-free `Cl(X)` is
excluded for fixed C0 in every mate degree and every carrier degree**.
More generally, any normal carrier whose torsion subgroup does not
contain the required nonzero class order is excluded.

The congruence cases are:

| Carrier degree | `v` | Necessary class order and smallest possible mate degree |
|---|---:|---|
| `a` odd | 4 | `t>=2`, `b_min>=8` |
| `a=2 mod 4` | 2 | `t>=3`, `b_min>=6` |
| `a=0 mod 4` | 1 | `t>=5`, `b_min>=5` |

These are exact necessary class-order restrictions, not a theorem
that the indicated classes occur or that their divisor is the fixed
embedded curve.

### 3. Resolution formulation and a coverage warning

For a smooth projective resolution `M->X`, the class group can be
computed as the Picard group modulo the classes of exceptional primes.
The relevant torsion is therefore controlled by nonprimitive embeddings
of the exceptional lattice and, where present, Picard torsion.
Knowing that `Pic(M)` is torsion-free does not by itself show that
`Cl(X)` is torsion-free: a quotient by a nonprimitive exceptional
subgroup can acquire torsion. One must use the actual saturated
exceptional lattice, not silently discard this quotient torsion.

The accepted quartic/quintic lattice arguments already preserve this
distinction in their respective finite ADE types. The present result
does not classify exceptional lattices at arbitrary carrier degree.
It proves an all-degree exclusion for the torsion-free class-group
lane and leaves the required nonzero torsion classes as an explicit
global obstruction to be studied.

The Cartier-lift classification gives a different all-degree boundary:
a smooth rational degree-`d>=3` curve with a mate on a normal carrier
must be non-Cartier somewhere. The present torsion filter additionally
requires the particular primitive degree-zero divisor class `Delta`
to be nonzero torsion for fixed C0. Neither condition supplies a
uniform bound on all normal carriers.
