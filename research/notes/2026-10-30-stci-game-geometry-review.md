# Geometric meaning and scope in the STCI research game

October 30, 2026. Reviewer: geometry_referee, with a separate
coplanarity check by geometry_referee/coplanarity_check.

This is independent geometric review and interpretation of the
[research game](../STCI_GAME.md), not canonical promotion. Statements
below distinguish reviewed inputs, newly checked consequences, and
proposals awaiting further audit. The fixed characteristic-zero problem
for \(C_0=[s^4:s^3t:st^3:t^4]\) remains open.

## 1. What a calculation must explain

For every computation or review, identify the actual geometric object,
the map or divisor being measured, the geometric event detected by a
rank or factorization, and the change to the general STCI strategy.
Also state the first geometric implication not supplied by the calculation.

A normal symbol, a curve on an exceptional divisor, a curve on a
normalization, a divisor on the original carrier, and a residual curve
downstairs are different objects. A numerical coincidence does not
identify them. In particular an isolated inverse point is an actual
support failure; an exceptional vertical curve need not be a residual
component in \(\mathbf P^3\).

## 2. Dictionary for the current results

| Result or calculation | Actual geometric content | Missing implication |
| --- | --- | --- |
| Dimensions of \(H^0(\mathcal I_C^m(d))\) and symbol ranks | Sections of a global linear system and the fibers of restriction to infinitesimal neighborhoods. A large kernel is freedom invisible at the tested neighborhood | Individual lifts do not construct a jointly supported pair, and a large fiber need not move its fixed restriction on \(Q\) |
| Forced \(q\)-factor below \(d=3m\) | The residual class \((d-m,d-3m)\) on the smooth quadric cannot be effective when its second degree is negative | Above the boundary, nonempty individual section spaces do not imply that the two equations can remove all residual support |
| Weighted-subalgebra ruling-line theorem | Actual curves on a carrier attach to normalization branches. Their restriction degrees and the hyperplane degree impose incompatible equations for a hypothetical mate divisor | Repeated roots change the branch structure; axis roots move attachments to endpoints. Those geometries require a new analysis |
| The large family \(W_H\) | All available next-order corrections vanish on \(Q\), so the common scheme \(V(q,H^m)\) is fixed and retains \(mR_H\) | The source has no fixed surface and does contain proper pairs, but that does not make its fixed curve movable |
| Saturation of the off-diagonal inverse ideal | Detects all points lying over \(C\) away from the marked inverse curve, including isolated points invisible to generic branch data | A zero-dimensional inverse scheme is not a divisor and cannot be discarded when testing full support |
| Odd squarefree part of the target discriminant | The branch divisor of a degree-two normalization map. Square factors account for singularities of the target image that normalization removes | Genus one and four target intersection points do not prove there are only four points on the normalization |
| Degree-twenty three-value cover in the order-two projection case | All Riemann--Hurwitz ramification is consumed by the two ruling boundaries and the four marked contacts | A cover and its marked divisor need not extend to two source ruling pencils and four global ambient sections |
| Pure-power coordinate-ring membership | Descent of the actual section whose upstairs zero divisor is supported on the marked inverse curve | Failure in one degree is not failure in all degrees; the full conductor, including its nilpotent quotient, controls all powers |
| The arithmetic higher-jet gap | A function is constant on the reduced conductor image but varies transversely upstairs in a direction missing from the downstairs ring | The gap is proved on the stated source, not on every possible carrier |

The first two rows use the reviewed
[global freedom calculation](2026-10-28-stci-search-freedom.md).
The curve-attachment row uses the reviewed
[all-degree line argument](2026-10-30-weighted-subalgebra-line-obstruction.md).
The fixed-curve row uses the reviewed
[quadric-boundary theorem](2026-10-30-stci-game-quadric-boundary.md).
The projection and arithmetic rows use the source notes linked below.

The arithmetic phenomenon is especially geometric. In characteristic
zero, powering a unit with constant residue and nonzero transverse
linear term preserves a nonzero first infinitesimal variation.
In characteristic \(p\), Frobenius moves the first surviving variation
to order \(p^{v_p(b)}\). This is why a conductor jet gap can force
degree growth and why Frobenius can eventually permit descent.
It is a deformation of the full nonreduced gluing data, not simply
the disappearance of coefficients in one binomial equation. See the
[arithmetic proof](2026-10-29-arithmetic-beyond-binomial.md).

## 3. The support-quartic obstruction is a coplanarity theorem

**Independent interpretation: PASS.** The reviewed zero-middle-coefficient
condition has an intrinsic projective meaning:

> The four marked target points of a surviving order-two projection
> must span \(\mathbf P^3\).

Indeed let \(D=P_1+\cdots+P_4\) be any reduced degree-four divisor on
\(C_0\), and let \(f_D(s,t)\) be its binary quartic, unique up to scalar.
The hyperplane restriction map is injective, because \(C_0\) is
nondegenerate, and has image
\[
\langle s^4,s^3t,st^3,t^4\rangle
\subset H^0(\mathbf P^1,\mathcal O(4)).
\]
Therefore
\[
[s^2t^2]f_D=0
\quad\Longleftrightarrow\quad
P_1,\ldots,P_4\text{ are coplanar}.
\]
The containing plane, if it exists, is unique. This equivalence includes
endpoint divisors, although the surviving elliptic projection problem
already excludes endpoints by its full-inverse-support conditions.

On the target quadric the plane cuts a conic of class \((1,1)\).
If this conic is irreducible it is the graph \(B=M(A)\) of a Möbius
transformation between the two target rulings. If the four \(A\)-values
are distinct, this is equivalently equality of the ordered cross-ratios
of \(A_i=t_i^3\) and \(B_i=t_i\). A cross-ratio must not be written when
the \(A_i\) collide.

If the conic is reducible, its distinct nonendpoint intersections with
\(C_0\) have the pattern three points on one constant-\(A\) ruling
and one on a constant-\(B\) ruling. Three marked elliptic points would
then belong to one fiber of the degree-two ruling map \(A\), impossible.
This is the geometric content of the degenerate Möbius determinant case.

The irreducible conic case is excluded by the reviewed Picard and
interpolation argument. Its line-bundle identity
\[
L^2=\mathcal O_E(Z),\qquad M=L^3
\]
says that the marked degree-four divisor is linearly equivalent to two
fibers of the degree-two pencil \(A\). If a degree-two source ruling
agrees at all four marked points with \(M(A)\), the zero and pole
degrees of their difference force it to have the same degree-two bundle.
Its complete pencil then forces equality globally. Both source rulings
would coincide, collapsing the proposed \((2,2)\) elliptic embedding
into the diagonal.

This is a marked-embedding obstruction. It is stronger than a numerical
degree check and different from saying that the abstract elliptic target
curve does not exist. The
[target and extension note](2026-10-30-projection-elliptic-target-incidence.md)
retains an actual elliptic target incidence with four contact-five
points that fails precisely this global extension.
Linear equivalence \(L^2=\mathcal O_E(Z)\) does not identify \(Z\)
with the actual ramification divisor of \(A\).

## 4. Geometric audit of the new elliptic double-cover source

The existence side's new source is outside the old rational-diagonal
degree-one inverse setting. It uses
\[
E:y^2=x^3-x,\quad T=(i,1-i),\quad
L=\mathcal O_E(O+T),\quad M=\mathcal O_E(4O).
\]
The point \(T\) has order four and \(2T=(0,0)\).
The identities
\[
L^4=M^2,\qquad L^2\ne M
\]
are a controlled order-two discrepancy in the Picard group. The first
permits the desired quartic-coordinate sections on the embedded
elliptic curve; the second changes how the degree-two deck involution
acts on the source quadrics. It is not by itself a conductor-descent
or STCI existence theorem.

There is an exact geometric check of that claim. In the embedding
\[
Z=(1,x,y,x^2),\qquad
Q_0=Z_0Z_3-Z_1^2,\quad
Q_1=Z_2^2-Z_1Z_3+Z_0Z_1,
\]
the deck involution \(P\mapsto T-P\) is induced by
\[
\mathsf M=
\begin{pmatrix}
-1&2i&2i+2&1\\
-i&2&0&i\\
1-i&0&0&1-i\\
1&-2i&2i+2&-1
\end{pmatrix}.
\]
Independent exact substitution gives
\[
\mathsf M^2=8I,\qquad
Q_0(\mathsf M Z)=8iQ_1(Z),\qquad
Q_1(\mathsf M Z)=-8iQ_0(Z).
\]
The induced action on the quadric pencil \(S_\mu:Q_1+\mu Q_0=0\)
is consequently
\[
\mu\longmapsto-1/\mu.
\]
Only the members \(\mu=\pm i\) are invariant. The tested source
\(S_2\) is not. Thus the torsion choice genuinely prevents the old
argument that a deck symmetry on the elliptic curve must preserve the
chosen global source surface. It does not prevent the involution from
extending linearly to the containing \(\mathbf P^3\).

The fixed tested coordinate system is basepoint free and has a
degree-eight birational image according to the existence computation.
Its first failure is instead full inverse support: the affine scheme
with \(Q_0=1\) has length 24 away from \(E\). Because \(Q_0\) has
degree two, this affine normalization is a free \(\mu_2\)-cover of the
projective complement. It corresponds to a projective extra-inverse
scheme of length twelve, not 24 distinct projective points. This
single input is therefore rejected in every mate degree; the larger
coefficient family is not excluded.

The smooth-root theorem
[R-0005](../results/smooth_root_formal_obstruction.md) does not apply
merely because the inverse curve is elliptic. Its object is the
actual full root on the exceptional divisor in the blowup, with a
specified bidegree. Applying the actual-CI bridge
[R-0006](../results/actual_ci_smooth_root_bridge.md) also requires
saturation, joint generation, the full initial ideal and the required
gap. None follows from the Picard identities above.

## 5. Independent audit of the critical-degree test-curve principle

**PASS for the following scoped statements proposed by the non-existence
side.** These are new provisional results, not an unrestricted theorem.

Let \(F\in V_{3m,m}=H^0(\mathcal I_C^m(3m))\).
Assume its generic first normal form is irreducible of degree \(m\)
over \(k(C)\). The corresponding normalization inverse curve
\(\Gamma\to C\) has generic degree \(m\), rather than \(m\)
independently labelled global curves. Suppose an actual ruling line
on \(V(F)\) meets \(C\) at three nonendpoint points and attaches to
\(\Gamma\) simply at those points, in regular normalization
neighborhoods. A hypothetical degree-\(b\) mate then has divisor
\(r\Gamma\) upstairs and satisfies
\[
3mb=4mr,\qquad b=3r.
\]
These identities are incompatible. Under the hypothetical mate every
carrier factor must contain \(C\); irreducibility of the initial
form then forces one global factor with multiplicity one. Thus global
integrality need not be assumed separately.

There is a nonempty Zariski open subset of the **full**
\(V_{3m,m}\) where this argument applies. Here is the independent check.
With the balanced normal bundle, the first normal forms are sections
of \(\mathcal O_{\mathbf P^1\times\mathbf P^1}(5m,m)\), in the
ordering (base, normal direction). Cubic equations generate the
conormal bundle twisted by three; products of \(m\) such equations
give a basepoint-free subsystem of that ample line bundle.
Characteristic-zero Bertini gives a smooth general divisor, and
\[
H^1(\mathcal O(-5m,-m))=0
\]
gives connectedness. Smoothness and connectedness imply irreducibility,
so it is one degree-\(m\) cover of \(C\). The use of Bertini here is
for smoothness of a basepoint-free system in characteristic zero,
not an unsupported assertion of irreducibility; see
[Kleiman's primary discussion](https://www.sba.unipi.it/sites/default/files/persona_archivio/steven_l._kleiman_bertini_and_his_two_fundamental_theorems.pdf).

The quadric restriction of \(F\) is \(C^m\) plus \(2m\) ruling lines.
The cubic residual quadratics span all binary forms of degree two in
the first target ruling. Products therefore give all degree-\(2m\)
binary forms in that ruling. Generically their \(6m\) intersections
with \(C\) are simple and away from the endpoints.

At every point of the quadric-normal direction section, value and
vertical directional derivative are independent linear conditions on
the actual symbol source. A cubic \(H\) nonzero at that direction
gives the nonzero value via \(H^m\); a cubic \(q x_i\), with
\(x_i(p)\ne0\), gives an independent vertical derivative via
\((q x_i)H^{m-1}\). The incidence where both vanish has codimension
two at each point of a one-dimensional section. Its projection is
therefore a proper closed bad locus. Avoiding it makes all the
actual line attachments regular and simple. The intersection of
these nonempty open conditions is nonempty.

This proves a generic-family exclusion in the full critical-degree
source. It does not say that all members are excluded. A hypothetical
STCI carrier must specialize the root-cover or attachment geometry,
and this is a concrete geometric constraint on the existence program.

For a reduced horizontal root divisor with components having cover
degree \(e_j\) and directional degree \(b_j\), the quadric-normal
section is a degree-one graph, so its attachment count is
\(e_j+b_j\). The global and test-line equations become
\[
3m b=4\sum_j e_jr_j,\qquad
2m b=\sum_j(e_j+b_j)r_j.
\]
They force the weighted average of \(b_j/e_j\) to be \(5/3\).
Under the stated ordinary-attachment hypotheses, all components of
slope greater than \(5/3\) are therefore excluded together. This is a
geometric description of the possible escape: at least one component
must have sufficiently low motion in the normal-direction factor, or
the ordinary attachment assumptions must fail.

## 6. A broader residual-curve principle to test

The following is a proposal, not included in the preceding PASS.
For degree \(a\ge3m\), replace the ruling lines by the whole actual
residual curve
\[
T=(F|_Q)-mC,\qquad [T]=(a-m,a-3m).
\]
If the generic normal root is one degree-\(m\) inverse curve and
the normalization of \(T\) attaches simply to it at every point of
\(T\cap C\), a hypothetical mate would satisfy
\[
ab=4mr,\qquad
b(2a-4m)=r(4a-6m).
\]
Elimination gives \(2a^2-7am+8m^2=0\), impossible for positive
\(a,m\), since its discriminant is negative.

For \(a>3m\), generic residual divisors on \(Q\) have both ruling
degrees positive and should be smooth irreducible members of their
actual complete restriction space. Cubic products multiplied by
ambient forms give a basepoint-free normal-symbol subsystem, and
the same value/vertical-derivative construction has the correct
degrees. The hypotheses concerning actual restriction surjectivity,
normalization and all attachments must still be checked independently
before declaring a generic all-degree-source theorem.

This proposal illustrates the intended use of geometry: a calculation
of line counts points toward a test-curve degree obstruction that may
extend to whole residual curves. Its geometric assumptions, rather
than just the polynomial identity, determine its coverage.

## 7. Consequences for both independent programs

The existence program should say which geometry changes when it leaves
an excluded source. A repeated binary root changes branch separation;
an axis root changes endpoint attachment; a new elliptic cover changes
the inverse map degree and its Picard data. Merely increasing the number
of coefficients does not identify a way to move a fixed divisor.

The non-existence program should search for actual test curves, common
fixed divisors, ramification exhaustion, and descent gaps across larger
classes. It should also identify the geometric degeneration that defeats
each principle and attack that degeneration separately. The other
side's current construction does not bound this program.

The referee should insist that a rank calculation name its map, a
discriminant name its normalization, a torsion calculation name its
gluing or symmetry, and a degree inequality name its actual curves.
The common question remains whether all possible global pairs are
excluded or one pair survives every global test.
