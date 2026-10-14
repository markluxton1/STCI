# Normal carriers: local power-socle compatibility and uniform exclusion

Date: 2026-10-14. Status: **PROVED, WITH A SEPARATE INDEPENDENT NEW-PROOF
AUDIT**. This is the current theorem statement and integration record.
The [full independent proof](2026-10-14-generalization-index12-filtered-compatibility.md)
reconstructs every new local step. The
[earlier ordinary-curvilinear note](2026-10-14-generalization-curvilinear-torsion-and-index12.md)
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
