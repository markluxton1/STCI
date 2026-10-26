# Two arithmetic scales in the root pencil: a collision tree near a = 4

Date: 2026-10-25. **Exploratory continuation, not canonically promoted.**
This is a selective calculation in the actual fixed-\(C\) pencil from
[the root-pencil note](2026-10-25-ci-cycle-root-pencil.md). It explores a
valuative picture of proximity and uses no accepted STCI obstruction.
The established mixed-characteristic reference configuration is exactly
[STCI-R-0021](../results/quartic_mu4_degeneration.md); its proof is not rerun.

## 1. The experiment and its three distinct scales

Retain
\[
F=x_1^4-x_0^3x_3,\quad
G_a=x_2^4-a x_1x_2x_3^2+(a-1)x_0x_3^3.
\]
Over a complete rank-one valued field \(K\) of characteristic zero with
residue characteristic two, write
\[
\varepsilon=a-4,\qquad h=v(2)>0,\qquad
\gamma=v(\varepsilon)>0.
\]
Extend the valuation to an algebraic closure when discussing roots. We
initially exclude \(\varepsilon=0\) and the two residual discriminant
parameters, so the four geometric roots are distinct. Odd rational
integers are units. The root coordinate \(\lambda=1+w\) gives
\[
f_a(1+w)=w\bigl(w^3+4w^2+6w-\varepsilon\bigr).
\tag{1}
\]
The marked curve \(C\) is \(w_0=0\). The other three sheets correspond to
the roots of the cubic in parentheses. Since all their valuations below
are positive, every \(\lambda=1+w\) is a unit and all four generic
components are smooth conjugate quartics.

There are two arithmetic scales: \(h\), the size of the prime two, and
\(\gamma\), proximity of the pencil parameter to the characteristic-zero
double-\(C\) member. A local endpoint parameter later introduces a third,
horizontal scale. These should be recorded separately before any weighted
sum is chosen.

The standard Newton-polygon rule reads root valuations, counted with
multiplicity, from negative slopes and horizontal lengths of the lower
hull; see [Sharifi, Algebraic Number Theory, Proposition 5.4.11](https://math.ucla.edu/~sharifi/notes/algnum-ch05.html).
Everything specific to this pencil is calculated below.

## 2. First break: which sheets approach the marked curve fastest?

The Newton points of the residual cubic are
\[
(0,\gamma),\quad(1,h),\quad(2,2h),\quad(3,0).
\]
The point \((2,2h)\) never contributes a lower-hull vertex. The first break
is at \(\gamma=3h/2\):

| Parameter scale | Valuations of the three differences from the marked root |
| --- | --- |
| \(0<\gamma<3h/2\) | \(\gamma/3,\gamma/3,\gamma/3\) |
| \(\gamma=3h/2\) | \(h/2,h/2,h/2\) |
| \(\gamma>3h/2\) | \(\gamma-h,h/2,h/2\) |

The sum is always \(\gamma\), as it must be from the constant coefficient
\(-\varepsilon\). Above the break, label the uniquely closest root
\(w_1\), so \(v(w_1)=\gamma-h\), and call the other roots \(w_2,w_3\).

The critical equality does **not** produce a residue collision. To see
this, choose \(t^2=2\), divide the cubic at \(w=tz\) by \(t^3\), and reduce.
The result is
\[
\bar z^3+\bar z+\beta,\qquad
\beta=\overline{\varepsilon/t^3}\ne0.
\]
Its derivative is \((\bar z+1)^2\), but its value at \(\bar z=1\) is
\(\beta\ne0\). Thus the residual cubic has three distinct nonzero roots.
All six pairwise differences among \(0,w_1,w_2,w_3\) have valuation
\(h/2\) at this equality. Below it, the reduced equation after scaling is
\(z^3-\beta\), also separable in residue characteristic two; all six
pairwise differences then have valuation \(\gamma/3\).

This corrects a tempting first guess: a change in Newton slopes need not
be a collision of residual roots. Here the tree changes from four equal
branches to two closer pairs only *after* the first break.

## 3. Second break: a residual pair can collide independently of C

The first Newton polygon does not determine the mutual separation of
\(w_2\) and \(w_3\). Above the first break, they share a leading residue.
Their discriminant supplies the missing coordinate. Set
\[
B(\varepsilon)=-288-176\varepsilon-27\varepsilon^2.
\tag{2}
\]
This is both the discriminant of the residual cubic and the factor
\(-27a^2+40a-16\) of the quartic discriminant. In particular
\[
\operatorname{disc}(f_a)=\varepsilon^2B(\varepsilon).
\tag{3}
\]
The three terms in (2) have valuations
\[
5h,\qquad4h+\gamma,\qquad2\gamma.
\]
The middle term is never minimal. Therefore
\[
v(B)=
\begin{cases}
2\gamma,&\gamma<5h/2,\\
5h,&\gamma>5h/2,
\end{cases}
\tag{4}
\]
whereas at \(\gamma=5h/2\) cancellation may increase \(v(B)\).

For \(\gamma>3h/2\), put \(\delta=v(w_2-w_3)\). The two differences
\(w_1-w_2,w_1-w_3\) have valuation \(h/2\), so the cubic discriminant gives
\[
v(B)=2(h+\delta),\qquad
\delta=\frac{v(B)}2-h.
\tag{5}
\]
Thus the full collision pattern is:

| Region | Marked pair depth \(v(w_1-w_0)\) | Other pair depth \(\delta\) | Cross-pair depth |
| --- | --- | --- | --- |
| \(3h/2<\gamma<5h/2\) | \(\gamma-h\) | \(\gamma-h\) | \(h/2\) |
| \(\gamma=5h/2\) | \(3h/2\) | \(v(B)/2-h\ge3h/2\) | \(h/2\) |
| \(\gamma>5h/2\) | \(\gamma-h\) | \(3h/2\) | \(h/2\) |

The marked pair and the other pair initially deepen at the same rate.
Beyond the second break, only the marked pair continues to deepen for a
parameter approaching zero \(\varepsilon\); the other pair stabilizes.
But in a different parameter direction through the critical shell,
the *residual* pair can deepen arbitrarily while the marked pair stays
at depth \(3h/2\). This is an actual distinction between concentration
onto \(C\) and collisions elsewhere in the residual curve.

A schematic tree above the first break is

```text
all four roots, common depth h/2
  ├── {marked root 0, w1}: additional depth (gamma-h) - h/2
  └── {w2, w3}:             additional depth delta - h/2
```

Depth is a valuation of a coordinate difference. No choice of a global
metric on the ambient projective space is being asserted.

## 4. The exceptional shell retains residue information

At \(\gamma=5h/2\), use \(t^2=2\) and write
\(\varepsilon=t^5e\), with \(e\) a unit. After dividing (2) by \(t^{10}\),
the residue is
\[
\overline{B/t^{10}}=\bar e^2+1=(\bar e+1)^2.
\]
Thus \(\bar e\ne1\) gives \(v(B)=5h\); the residue \(\bar e=1\) requires
further terms and can give deeper collisions. If the residue field is
\(\mathbf F_2\), every unit has residue one, so cancellation on this
critical shell is automatic. A generic noncancelling residue exists
after a suitable residue-field extension.

An explicit ramified example is
\(K=\mathbf Q_2(\sqrt2)\), \(h=1\),
\(\varepsilon=4\sqrt2\), so \(\gamma=5/2\). Then
\[
B=-1152-704\sqrt2,\qquad v(B)=13/2,
\]
because the summands have distinct valuations \(7\) and \(13/2\).
Consequently the residual-pair depth is \(\delta=9/4\), larger than the
naive \(3/2\) value on the critical shell.

More precisely, the two zeros of \(B\) are
\[
\varepsilon_\pm=
\frac{-88\pm4\sqrt{-2}}{27}.
\]
Each has valuation \(5h/2\), while
\(v(\varepsilon_+-\varepsilon_-)=7h/2\). Writing
\(r_\pm=v(\varepsilon-\varepsilon_\pm)\), one has the exact refinement
\[
v(B)=r_++r_-,\qquad
\delta=\frac{r_++r_-}{2}-h.
\tag{6}
\]
Away from the zeros themselves these numbers are finite. If one distance
is below \(7h/2\), both distances equal that smaller value. If one exceeds
\(7h/2\), the other is \(7h/2\). At equality the residue of the next
coefficient matters again. This describes the full critical-shell
refinement in terms of the actual two discriminant points, rather than
pretending that \(\gamma\) alone determines the tree.

At \(\varepsilon=\varepsilon_\pm\), the residual pair is genuinely double;
at \(\varepsilon=0\), the marked pair is double instead. These are
separate characteristic-zero strata in the same arithmetic neighborhood.

## 5. Recovering the fourth roots of unity and the elliptic marker

The original \(\mu_4\) member has \(a=0\), hence \(\varepsilon=-4\) and
\(\gamma=2h\). The marked differences are
\[
-2,\quad i-1,\quad-i-1,
\]
with valuations \(h,h/2,h/2\); the other close pair has difference \(2i\)
and depth \(h\). Thus the two pairs have equal depths. The derivative
budget is \(h+h/2+h/2=2h=v(4)\), and the full quartic discriminant has
valuation \(8h=v(-256)\), as predicted by (3).

For \(\gamma>3h/2\), choose the cross-ratio adapted to the two pairs,
\[
x=\frac{(w_0-w_1)(w_2-w_3)}{(w_0-w_2)(w_1-w_3)}.
\]
Its depth is
\[
\ell=v(x)=\gamma+\delta-2h>0.
\tag{7}
\]
This combines the two short-pair depths after subtracting the common
cluster depth. The elliptic double cover from the root-pencil note has
\[
j=256\frac{(1-x+x^2)^3}{x^2(1-x)^2}.
\]
Since \(v(x)>0\), the factors \(1-x\) and \(1-x+x^2\) are units. Therefore
\[
v(j)=8h-2\ell
=14h-v(\operatorname{disc}f_a).
\tag{8}
\]
The second equality also follows directly from the exact pencil formula
for \(j\), since \(a-1\) is a unit in this neighborhood.
At the \(\mu_4\) member \(\ell=h\) and \(v(j)=6h\), agreeing with
\(j=1728\). This is a useful consistency bridge between a root-collision
tree and the coarse elliptic modulus. We do not infer a model of stable
reduction or a reduction type from this numerical identity alone.

## 6. Endpoint contact adds a horizontal contribution

Near \(p\), a branch has transverse coordinate \(Y=w u^3\) relative to
\(C\). If an endpoint valuation assigns \(v(u)=\alpha\ge0\), then
\[
v(Y_i-Y_j)=v(w_i-w_j)+3\alpha.
\tag{9}
\]
The first-normal determinant is \(-\varepsilon u^9\), and its valuation
is exactly
\[
\gamma+9\alpha
=\sum_{i=1}^3\bigl(v(w_i)+3\alpha\bigr).
\tag{10}
\]
The full local quartic discriminant similarly has valuation
\(v(\operatorname{disc}f_a)+36\alpha\). These equations separate
arithmetic coalescence of coefficients from the order-three geometric
contact at the endpoint.

At the other endpoint, the leading coefficients are \(\lambda^{-3}\).
They are obtained from the first endpoint by
\[
\lambda\longmapsto\frac{\lambda}{a\lambda+1-a}.
\]
In the present neighborhood its determinant \(1-a\) and all denominators
\(\lambda^4\) are units. Hence it preserves every pairwise valuation of
the coefficient differences. The same arithmetic collision tree occurs
at both endpoints, with the local horizontal factor then added as in
(9). This agreement is stronger than equality of the two elliptic
\(j\)-invariants.

## 7. What this suggests, and the next experiment

A single marked determinant records the sum \(\gamma\) and misses how it
is distributed among the three residual sheets. The first Newton polygon
recovers those three individual depths, but misses an independent
residual-pair collision. Adding the discriminant and its residue data
recovers that next layer. The tree, rather than one number, is therefore
a concrete candidate organizing object for a neighborhood of this family.

It is particularly suggestive that approaching the double-\(C\) member
and approaching a residual double-sheet member deepen different branches
of the same tree. The \(\mu_4\) configuration occupies an intermediate
balanced-pair pattern. This balance does not isolate it: the entire
region \(3h/2<\gamma<5h/2\) has equal pair depths. Unit and higher
residue data, which the exact cross-ratio retains, still distinguish
configurations. This is a useful geometric picture of symmetry, not a
global extremality assertion.

The [stdlib experiment](../computations/verify_ci_cycle_root_collision_valuations_2026_10_25.py)
and [JSON output](../computations/ci_cycle_root_collision_valuations_2026_10_25.json)
record exact rational lower hulls and budget checks. Reproduce with
`python3 research/computations/verify_ci_cycle_root_collision_valuations_2026_10_25.py research/computations/ci_cycle_root_collision_valuations_2026_10_25.json`.
The computation does not approximate algebraic roots or decide residue
cancellation; those distinctions are explicit in the formulas above.

**Review boundary.** The primary agent independently reconstructed the Newton hull, the two thresholds, the discriminant coefficients, the exceptional example in \(\mathbf Q_2(\sqrt2)\), and the cross-ratio valuation identity, and replayed all fifty finite checks. The separate valuative audit concerns the earlier local framework; it does not claim an additional independent review of this later collision experiment. These calculations remain exploratory and unpromoted.

Next one could perturb the pencil by a second actual quartic in
\(I_C(4)\), compute the local transverse Weierstrass polynomial, and ask
whether the marked collision tree, endpoint determinant, and residual
discriminant form compatible charts on a larger deformation space.
A failure would be informative: moving branch points, nonmonic
presentations, or changing carriers can make the chosen root coordinate
inadequate. No unrestricted ordering of complete intersections, stable
model, or canonical promotion is claimed here.
