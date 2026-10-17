# An intrinsic normal divisor and index thresholds for smooth curves

Date: 2026-10-14. Author: `normal_index_general_scope`.
Status: **PROVED NEW STRUCTURAL THEOREMS; independently reviewed in
[the general-scope audit](2026-10-14-generalization-normal-index-general-scope-independent-audit.md).**
The accepted local power-socle theorem in
[the root theorem](2026-10-14-generalization-normal-index-socle-theorem.md)
and its
[filtered compatibility audit](2026-10-14-generalization-index12-filtered-compatibility.md)
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
theorem](2026-10-14-generalization-normal-carrier-torsion.md) gives the
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
