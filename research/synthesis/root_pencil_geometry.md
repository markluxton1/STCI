# Root pencils, conductor geometry, and arithmetic collision

These are reviewed calculations for the displayed actual four-sheet pencil, not an invariant or classification of arbitrary intersections. The fixed quartic is marked throughout. Distinct roots, geometric boundaries, residual degree and generic thickness are tracked separately.


Put
\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3,\qquad
Q=x_0x_3-x_1x_2,
\]
and mark \(p=[1:0:0:0]\), \(q=[0:0:0:1]\) on
\(C=[s^4:s^3t:st^3:t^4]\). The pencil varies the actual second equation,
with F fixed.

## A fixed-boundary pencil and its elliptic branch diagnostic

## 1. A deformation that keeps the four sheets

Consider the actual homogeneous quartics

\[
G_a=G+a x_3^2Q
=x_2^4-a x_1x_2x_3^2+(a-1)x_0x_3^3.
\tag{1}
\]

Every \(G_a\) vanishes on \(C\). On \(x_0=1\), put \(u=x_1\), \(y=x_2\)
and eliminate \(x_3=u^4\) using \(F\). Then

\[
G_a=y^4-a u^9y+(a-1)u^{12}.
\]

For \(u\ne0\), the substitution \(y=zu^3\) gives the root polynomial

\[
f_a(z)=z^4-a z+a-1
=(z-1)(z^3+z^2+z+1-a).
\tag{2}
\]

The marked root \(z=1\) is exactly the retained curve \(C\). Each other
root \(\lambda\ne0\) gives the smooth rational quartic

\[
C_\lambda=[s^4:s^3t:\lambda st^3:t^4].
\]

If all four roots are distinct and nonzero, these curves are projectively
equivalent by scaling \(x_2\), and their union exhausts the complete
intersection by degree and complete-intersection purity. This is a
four-sheet family, not a picture of exceptional fibers.

The affine family is flat. Over \(k[a,x_0,x_3]\), use a monomial order in
\(x_1,x_2\) refining total degree; the two monic relations have leading
monomials \(x_1^4,x_2^4\). The relatively prime leading monomials give a
monic Gröbner basis and the quotient is free on
\(x_1^ix_2^j\), \(0\le i,j<4\). In particular, every graded piece is
flat over \(k[a]\). Projectivizing the pencil adds the member at infinity;
every member remains a proper \((4,4)\) intersection, so the same Hilbert
polynomial persists there.

One could initially suspect that the \(\mu_4\) arrangement is isolated among
four smooth conjugate quartics with two concentrated contact points. This
family shows a continuous deformation of precisely that picture.
The roots of unity are a symmetric point within it.

## 2. The boundary stays fixed while the roots move

At \(p=[1:0:0:0]\), the surface \(F=0\) is smooth. Branches are
\(y=\lambda u^3\); distinct roots have pairwise intersection multiplicity
three. At \(q=[0:0:0:1]\), \(G_a=0\) is smooth whenever \(a\ne1\), because
its derivative with respect to \(x_0\) is \(a-1\). Using \(x_2\) as a local
parameter, the curves have

\[
x_1=\lambda^{-3}x_2^3,\qquad x_0=\lambda^{-4}x_2^4.
\]

The coefficients \(\lambda^{-3}\) are distinct for distinct roots when
\(a\ne1\). Indeed, if \(\eta=\omega\lambda\), \(\omega^3=1\), equations
\(f_a(\lambda)=f_a(\eta)=0\) imply
\((1-a)(\omega-1)=0\). Thus all six pair contacts at each endpoint
remain three throughout the open four-smooth-component locus.

Each component has conductor boundary \(9p+9q\). Both endpoint delta
invariants remain eighteen. In particular, this boundary and the total
delta invariant cannot recover the root arrangement.

Along the marked \(C\), the first-normal determinant has the particularly
simple parameter dependence

\[
\det(dF,dG_a)|_C\ \doteq\ (4-a)s^9t^9.
\tag{3}
\]

Here \(\doteq\) allows a fixed nonzero scalar and a choice of determinant
trivialization. On the first chart it is the derivative
\(\partial G_a/\partial y|_{y=u^3}=(4-a)u^9\). The homogeneous determinant
is a section of \(\mathcal O_{\mathbf P^1}(18)\). For \(a\ne4\) its divisor
is always \(9p+9q\). At \(a=4\) the section is zero everywhere; it has no
finite zero divisor there.

This suggests keeping two distinct data: the **location and order of
contact on the base curve**, and the **configuration of separated sheets
seen after resolving that contact**.

## 3. Three ways the pencil leaves the open arrangement

The polynomial discriminant is

\[
\operatorname{disc}(f_a)
=256(a-1)^3-27a^4
=(a-4)^2(-27a^2+40a-16).
\tag{4}
\]

The exceptional parameters have different geometric meanings.

* **\(a=4\): collision with the marked sheet.** Here
  \[
  f_4(z)=(z-1)^2(z^2+2z+3).
  \]
  The fundamental cycle is
  \[
  2C+C_{-1+i\sqrt2}+C_{-1-i\sqrt2}.
  \]
  This is an explicit characteristic-zero deformation that transfers
  one quartic's worth of residual degree onto \(C\). The reduced support
  has three quartics; its conductor boundary on the marked component
  would be \(6p+6q\), whereas the full nonreduced scheme has the original
  Hilbert polynomial. The old \(9p+9q\) formula must not be applied to
  this reduced support.
* **\(27a^2-40a+16=0\): collision among residual sheets.** These parameters
  are \((20\pm4i\sqrt2)/27\). The marked root is simple, while two residual
  roots coincide. Equation (3) still supplies the degree-eighteen
  determinant boundary, even though the total curve is nonreduced.
* **\(a=1\): a root reaches zero.** Then \(f_1(z)=z(z^3-1)\); the root
  polynomial remains separable. But \(C_0\), interpreted here as the
  \(\lambda=0\) member rather than the repository name for the fixed
  quartic, has parametrization \([s^4:s^3t:0:t^4]\). It is a plane quartic
  with a \((3,4)\) cusp at \(q\), not a smooth conjugate of \(C\).
  Thus a root discriminant alone misses a geometric boundary of the
  embedded four-smooth-component arrangement.

At the projective pencil parameter **\(a=\infty\)**, the second equation is
\(x_3^2Q\). This gives a more drastic boundary, with cycle

\[
[C]+3[L_a]+9[L_d],\qquad
L_a=V(x_0,x_1),\quad L_d=V(x_1,x_3).
\tag{5}
\]

One can see this directly on \(Q\): write
\(x_0=ac,x_1=ad,x_2=bc,x_3=bd\), temporarily using \(a,b,c,d\) as Segre
coordinates unrelated to the pencil parameter. Then
\(F=a^3d(ad^3-bc^3)\); the last factor cuts out \(C\), giving
\(F\cap Q=C+3L_a+L_d\). Also \(F\cap\{x_3=0\}=4L_d\), so the doubled
plane contributes another \(8L_d\). The two residual lines meet at
\([0:0:1:0]\), away from \(C\).

The determinant boundary along \(C\) is still \(9p+9q\) at this infinity
member. A fixed boundary can coexist with changes from three smooth
residual quartics to two lines with large multiplicities and additional
incidence away from \(C\). This is a useful limitation, not a reason to
abandon the boundary viewpoint.

## 4. An elliptic curve hidden in the separated sheet configuration

Resolving the common order-three tangency exposes four marked directions
with coordinates \(\lambda\). Their unordered cross-ratio is summarized
by the double cover

\[
E_a:\quad w^2=f_a(z).
\tag{6}
\]

When the discriminant is nonzero this has a smooth projective completion
of genus one. The root \(z=1\) supplies a rational branch point, hence an
elliptic origin after completion. Its modulus is

\[
j(E_a)=1728\,
\frac{256(a-1)^3}{256(a-1)^3-27a^4}.
\tag{7}
\]

For a quick independent derivation, put \(z=1+1/x\) and
\(y=w/(z-1)^2\). The equation becomes

\[
y^2=(4-a)x^3+6x^2+4x+1.
\]

For \(b=4-a\ne0\), set \(X=bx,Y=by\). The cubic is
\(Y^2=X^3+6X^2+4bX+b^2\), with
\(c_4=192(a-1)\), \(c_6=-864a^2\), and
\(\Delta_E=16\operatorname{disc}(f_a)\), giving (7).
Classical binary-quartic invariants also yield this directly: here
\(I=12(a-1)\) and \(J=-27a^2\). The normalization of \(I,J\) and their
quartic discriminant is documented in
[Bhargava–Shankar, pp. 195–196](https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p03-p.pdf).
The calculation here concerns only their elementary invariant formulas.

At the distinguished member, \(a=0\), one has \(j=1728\). Thus the
square of fourth roots of unity gives the elliptic double cover with
extra order-four symmetry. At \(a=1\), one has \(j=0\), despite the
singular embedded \(\lambda=0\) quartic. At \(a=4\) and the two residual
collision parameters, \(E_a\) degenerates.

**Interpretation to explore.** The endpoint boundary measures how much
contact was compressed, whereas the elliptic modulus measures the
relative positions of sheets after that contact has been separated.
The distinguished arrangement is a symmetry point in this moduli
coordinate, and a continuous family shares its boundary. One should not
claim from this that an elliptic curve is canonically attached to every
complete intersection containing \(C\). In this laboratory we chose the
fixed carrier \(F\), the order-three separation, and one endpoint.
The two endpoints do supply the same modulus on this open pencil. Indeed,
for a root \(\lambda\),
\[
\lambda^{-3}=\frac{\lambda}{a\lambda+1-a}.
\]
For \(a\ne1\) this is a Möbius transformation of the coefficient line,
so the four \(\lambda\) and the four \(\lambda^{-3}\) have the same
unordered cross-ratio. How this agreement changes when \(F\) moves is a
next question.

An affine change of the leading coefficient \(\lambda\) under a local
coordinate change is a projective transformation of its line, so its
cross-ratio is a sensible local analytic diagnostic on the equal-contact
stratum. The double cover forgets labelling and retains its coarse
cross-ratio modulus. This is promising extra data, not a complete local
or embedded classification.



## Conductor, topology, generalized Jacobians, and a larger-delta control

## 2. The boundary is canonical, but its total degree is already forced

For a reduced Gorenstein curve \(W\) with normalization \(\nu:\widetilde W\to W\), write \(B\) for the conductor divisor upstairs. The relation

\[
\nu^*\omega_W\simeq\omega_{\widetilde W}(B)
\]

says that the conductor is exactly what turns ordinary differentials on the normalization into dualizing differentials on the singular curve. For this particular plane germ, the standard residue generator is

\[
\frac{du}{f_y}=\frac{du}{4y^3}.
\]

On a branch \(y=\zeta u^3\), it has a pole of order nine. This explains the exponent nine in differential language: each branch is separated from three others to order three, and the product of those separations vanishes to order nine.

Globally, \(\omega_Z=\mathcal O_Z(4)\). On each quartic normalization,

\[
\nu^*\omega_Z|_{C_\zeta}=\mathcal O_{\mathbf P^1}(16)
 =\omega_{\mathbf P^1}(9p+9q).
\]

The total boundary degree on the four normalizations is \(4\cdot18=72=2\delta(Z)\). This is not a mysterious extra numerical coincidence; it is the Gorenstein conductor-degree identity in this explicit example.

For any reduced \((a,b)\) complete intersection containing \(C\) as a component of multiplicity one, the same restriction calculation forces the boundary on the smooth marked branch to have degree

\[
\deg B_C=\deg(\omega_W|_C)-\deg\omega_C
 =4(a+b-4)+2=4a+4b-14.                 \tag{1}
\]

For \((4,4)\), the answer is always eighteen. Therefore the *degree* of the marked boundary cannot detect specialness within the reduced fixed-degree locus. Its distribution can: eighteen distinct simple attachments and \(9p+9q\) are very different divisors of the same degree.

There is another distinction worth preserving. On a nodal \(C\cup D\) with \(D\) smooth of genus sixteen and eighteen transverse intersections, the full conductor degree is thirty-six, not seventy-two. Its eighteen points on \(C\) are matched by eighteen points on \(D\). At \(Z\), the residual curve has its own singularities, producing the additional boundary. The marked boundary on \(C\) sees the attachment to the residual curve but does not recover the residual curve's internal singularity defect.

This makes \(B_C\) a good marked invariant and an incomplete invariant of the total curve. A proposed ordering using only \(B_C\) must expect large fibers.

## 3. The topology is much simpler than the arithmetic genus suggests

Topologically, a high-order tangency still glues the same points as an ordinary gluing. The normalization consists of four spheres, and at each endpoint four points are identified. The bipartite incidence graph has four component vertices, two singular-point vertices, and eight branch edges. Its first Betti number is \(8-6+1=3\).

The complex curve therefore has

\[
b_0(Z)=1,\quad b_1(Z)=3,\quad b_2(Z)=4,\quad\chi_{\rm top}(Z)=2.
\]

The Euler characteristic is the same as that of the smooth rational curve \(C\). This is a genuinely surprising failure of a plausible proximity statistic: Euler characteristic alone would place them together even though one has four irreducible components and three independent topological loops. Keeping the full Betti vector separates them.

The following comparison is a picture of possible fibers, not an assertion that all deformations are topologically equivalent to the second row.

| Complex curve | Normalization | Total delta | \(b_1\) | \(b_2\) | Euler characteristic |
|---|---|---:|---:|---:|---:|
| Special \(Z\) | Four copies of \(\mathbf P^1\) | 36 | 3 | 4 | 2 |
| Nodal \(C\cup D\), \(D\) smooth genus 16, 18 attachments | \(\mathbf P^1\amalg D\) | 18 | 49 | 2 | -46 |
| Smooth \((4,4)\), allowing \(C\) to disappear as a component | Smooth genus 33 curve | 0 | 66 | 1 | -64 |
| Reduced characteristic-two support of prescribed fiber | One \(\mathbf P^1\) | 0 | — | — | — |

The last row is algebraic, so complex Betti numbers are deliberately not assigned. Its underlying reduced curve is rational; the full characteristic-two scheme still has the complete-intersection Hilbert polynomial and arithmetic genus thirty-three. Reduction has forgotten that arithmetic information.

The local Milnor number at either endpoint in characteristic zero is

\[
\mu=(4-1)(12-1)=33=2\delta-r+1.
\]

Thus a full smoothing trades \(66\) units of local vanishing-cycle complexity against Euler characteristic: \(2-66=-64\). In a nodal marked deformation the eighteen remaining nodes leave Euler characteristic \(-64+18=-46\). A drawing of four highly tangent rational curves can conceal a large reservoir of vanishing cycles.

This also warns against a naive family of normalizations. Four rational normalizations do not simply deform as four disjoint rational curves into the normalization \(\mathbf P^1\amalg D\) of a nodal marked deformation. Normalization need not commute with the family. In suitable reduced families over a normal one-dimensional base, delta-constancy is tied to simultaneous normalization; see [Greuel–Pfister, *The delta invariant and fiberwise normalization*, 2022](https://www.journalofsing.org/volume25/greuel-pfister.pdf). Their precise hypotheses concern isolated non-normal singularities and the relevant flat/finite setup. They do not license applying the classical finite-delta picture to a fiber nonreduced along its entire curve.

## 4. A refined genus ledger: generalized Jacobians

For a connected reduced proper curve over an algebraically closed characteristic-zero field, the generalized Jacobian has an abelian quotient from the Jacobians of its normalized components, a torus from the gluing graph, and an additive contribution from the higher-order gluing. The normalization units sequence gives the concrete calculation here. For the general framework separating the maximal torus and the unipotent part, see [Geisser, *The affine part of the Picard scheme*, corrected version](https://arxiv.org/html/0704.0479v4), Theorems 1 and 3.

At an endpoint of \(Z\), the local unit quotient has dimension \(\delta_p=18\). Its torus dimension is \(r_p-1=3\); the remaining fifteen dimensions are unipotent. At the two endpoints these give six torus dimensions and thirty additive dimensions. Dividing by the three independent rescalings of four normalized components leaves a torus of dimension three. Since the normalized Jacobians vanish, the result is, noncanonically,

\[
\operatorname{Pic}^0(Z)\simeq\mathbf G_m^3\times\mathbf G_a^{30}.
\]

The split expression is characteristic zero only. The count \(3+30=33\) recovers the arithmetic genus.

For a nodal \(C\cup D\) as in the table,

\[
0\longrightarrow\mathbf G_m^{17}\longrightarrow
\operatorname{Pic}^0(C\cup D)\longrightarrow
\operatorname{Jac}(D)\longrightarrow0.
\]

Here the gluing graph has two vertices and eighteen edges, hence seventeen cycles. There is no additive part because the singularities are nodes. The dimensions now read \(17+16=33\).

This suggests recording a vector

\[
(\text{abelian dimension},\text{torus rank},\text{unipotent dimension})
\]

instead of a single genus. Its values in the three characteristic-zero pictures are

\[
Z:(0,3,30),\qquad C\cup D:(16,17,0),\qquad
\text{smooth CI}:(33,0,0).
\]

The first coordinate measures handles on the normalization; the second measures topological gluing loops; the third measures infinitesimal contact. This is an appealing way to articulate “exceptionally close to rational components”: almost all of \(Z\)'s genus is additive contact data. It is not yet an ordering, and none of the three coordinates should be asserted to vary monotonically in every family. Degenerations can exchange them.

## 5. A symmetry principle for the boundary, and a toric shadow

The embedded curve has the explicit torus action \(u\mapsto\lambda u\), realized by

\[
[x_0:x_1:x_2:x_3]\longmapsto
[x_0:\lambda x_1:\lambda^3x_2:\lambda^4x_3],
\]

and the endpoint-swapping coordinate reversal. These preserve the four-curve configuration. No classification of the full automorphism group is needed for the following observation: an effective degree-eighteen divisor invariant under this torus must be supported at \(p,q\), and endpoint swap then forces it to be \(9p+9q\).

Thus \(B_C\) is the unique degree-eighteen boundary invariant under these visible symmetries. This is a precise and modest extremality principle. It explains the balanced endpoint concentration without claiming that the complete intersection itself is unique among configurations having that boundary.

The reduced boundary provides another useful change of viewpoint:

\[
(\mathbf P^1,p+q)\quad\text{has}\quad K_{\mathbf P^1}+p+q\sim0.
\]

It is the standard toric compactification of \(\mathbf G_m\). On the open torus the prescribed family is \(\mathbf G_m\times\mu_4\), so the same two points are simultaneously the compactification boundary and the locus of conductor concentration. There is a toric/logarithmic shadow of the configuration.

One must retain the coefficient distinction. The actual canonical conductor is \(9p+9q\), giving \(K+B\) degree sixteen; the reduced toric boundary gives degree zero. Passing from one to the other discards contact order. A logarithmic model with only reduced boundary therefore needs additional contact data, such as decorations of order nine or the pairwise order-three separation data, to recover the original geometry.

Possible experiment: study the map from the fixed-degree parameter space to \(\operatorname{Sym}^{18}(C)\) sending a reduced marked intersection to \(B_C\), then examine the fiber over \(9p+9q\). Does the special roots-of-unity configuration occupy an isolated symmetry stratum in that fiber, or are there many different residual curves with the same concentrated boundary? The first possibility would make boundary plus symmetry more selective; the second would identify exactly what further data must be retained.

## 6. A useful competing configuration: larger delta is possible

It would be tempting to call \(\delta(Z)=36\) maximal among all \((4,4)\) intersections containing \(C\). Reducible hypersurfaces already give a reason to resist this conjecture.

Set

\[
Q=x_0x_3-x_1x_2,\qquad R=x_0x_2^2-x_1^2x_3,
\]

and choose planes

\[
\begin{aligned}
L_1&=x_0+x_1+x_2+x_3,\\
L_2&=x_0+2x_1+3x_2+5x_3,\\
L_3&=x_0+7x_1+11x_2+13x_3.
\end{aligned}
\]

Consider the actual \((4,4)\) pair

\[
W=V(Q L_1L_2,\ R L_3).
\]

The factors share no surface component. The Segre parametrization \((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\) gives

\[
R|_Q=ab(bc^3-ad^3),
\]

so \(Q\cap R\) is \(C\) plus the two ruling lines \(a=0,b=0\). The remaining components are the conic \(Q\cap L_3\), two plane cubics \(R\cap L_1,R\cap L_2\), and two lines \(L_1\cap L_3,L_2\cap L_3\).

The two cubic sections are geometrically irreducible and rational. This can be seen directly on the cubic normalization: a plane \(\alpha x_0+\beta x_1+\gamma x_2+\delta x_3=0\) pulls back to

\[
 A(\alpha v_0^2+\delta v_1^2)+B(\beta v_0+\gamma v_1)=0.
\]

For \(L_1\), the two coefficient forms are \(v_0^2+v_1^2\) and \(v_0+v_1\); for \(L_2\), they are \(v_0^2+5v_1^2\) and \(2v_0+3v_1\). Neither pair has a common projective zero, so the inverse plane section is a smooth rational section of the ruling, mapping birationally to the plane cubic. They meet the double line \(x_1=x_2=0\) at \((-1:0:0:1)\) and \((-5:0:0:1)\), respectively. At these non-pinch points their plane equations have a nondegenerate quadratic leading term, hence an ordinary node. An irreducible plane cubic has arithmetic genus one, so its normalization has genus zero. The conic is smooth: eliminating \(x_0\) with \(L_3\) gives \(-x_1x_2-7x_1x_3-11x_2x_3-13x_3^2\), whose symmetric matrix has determinant \(-16\). Thus there are eight rational normalized components, and the normalization sequence gives

\[
\delta(W)=p_a(W)+8-1=33+7=40>36.
\]

The exact finite-ideal check is preserved in [the M2 script](../computations/verify_ci_cycle_eight_component_competitor_2026_10_25.m2). Running

```sh
/opt/homebrew/bin/M2 --script research/computations/verify_ci_cycle_eight_component_competitor_2026_10_25.m2
```

returns degree sixteen, Hilbert polynomial \(16n-32\), equality to the intersection of the eight displayed component ideals, and primality of those eight ideals; their degrees are \(4,1,1,2,3,3,1,1\). This establishes the checked coordinate example. The rationality and delta interpretation use the elementary node/genus argument just given. The calculation is not a classification of any family.

The lesson is productive rather than dismissive: an extremality claim needs a chosen comparison class. Requiring integral hypersurfaces, prescribing the number/degrees of normalized components, fixing symmetry, or comparing the marked boundary could each recover a meaningful question. They are different questions and should remain separate.



## Balanced boundary and the limits of specialization ordering

## 10. A precise balanced-boundary interpretation from GIT

Regard \(B(Z)\) as the degree-18 binary form \(s^9t^9\). In the usual \(\operatorname{PGL}_2\) invariant theory of divisors on \(\mathbf P^1\), semistability permits multiplicity at most nine. The equal two-point divisor is strictly polystable: it represents the unique closed orbit in the strictly semistable locus. Thus there is a precise sense in which \(9p+9q\) is an exceptionally balanced **boundary configuration**.

This is a compelling version of the guiding intuition. It is balanced between two equal concentrations, not spread uniformly over eighteen points. The root pencil shows why a boundary quotient should be only the first stage of a richer moduli problem.

Two qualifications preserve the geometry. First, full \(\operatorname{PGL}_2\) forgets the specified four-dimensional hyperplane linear system defining the embedding \(C\subset\mathbf P^3\). The actual embedded automorphism group is smaller. Second, stable binary forms do not all have \(s^9t^9\) in their semistable orbit closure. This GIT observation does not order every complete intersection above \(Z\). See [Alper–Isaev, §5.2](https://sites.math.washington.edu/~jarod/papers/binary.pdf) and the [specialization notebook](root_pencil_geometry.md).

Under the actual torus fixing \(p,q\), plus endpoint exchange, \(9p+9q\) is the unique invariant effective divisor of degree eighteen. But it is not the unique torus-fixed complete-intersection pencil: the whole root pencil is torus invariant. This is a symmetry principle for a quotient of the geometry, with a substantial fiber still to understand.

## 11. Hilbert, Chow, and the choice of a specialization relation

On the Hilbert scheme the degree and arithmetic genus of a proper \((4,4)\) family stay fixed. On the Chow space one remembers component cycles and their multiplicities but loses the conductor algebra and much embedded structure. In the numerical curve group of \(\mathbf P^3\), even the position of a quartic has disappeared: every \(Z\) has class \(16[\text{line}]\).

The reduced curve \(C\) has Hilbert polynomial \(4n+1\), so it cannot be the special fiber of a flat projective family with Hilbert polynomial \(16n-32\). A multiple structure with support \(C\) can be such a fiber. This is precisely why the characteristic-two example matters.

A usable exploratory relation could be: a **stratum** of marked intersections lies above another if its closure contains the latter, with a specified flat family as evidence. The generic point of a chosen family then lies above its special point. Over an algebraically closed field, two distinct closed Hilbert-scheme points do not specialize directly to one another in the literal topological sense; one needs a family, a generic point, or orbit closures.

The finite root pencil gives \(Z_a\rightsquigarrow Z_0=Z\) along its parameter curve, but other special members occur on that same curve. This puts \(Z\) into a web of degenerations rather than making it a unique terminal object. An orbit-closure relation under automorphisms preserving \(C\) would be more restrictive. Neither relation is asserted to compare all of \(U\).

Another useful invariance check is \(V(F^r,G^s)\): its fundamental cycle is \(rs[Z]\). Any degree-normalized cycle score is unchanged by this presentation thickening, even though the Hilbert polynomial and local algebras change. This is a reason to carry a scheme invariant alongside a normalized cycle invariant.

## 12. Characteristic two: residual mass becomes transverse thickness

The result [STCI-R-0021](../results/quartic_mu4_degeneration.md) gives a flat integral model of \(Z\). Away from the endpoints it is
\[
\mathbf G_m\times\mu_4.
\]
In characteristic zero there are four geometric sheets. In characteristic two,
\[
z^4-1=(z-1)^4,
\]
and the generic transverse algebra is \(k(C)[Y]/(Y^4)\). The cycle is \(4[C]\), while the reduced support and its normalization are just \(C\cong\mathbf P^1\). A normalization of the nonreduced special fiber cannot retain its transverse thickness: normalization is taken through the reduction.

After normalizing all cycles to degree four,
\[
\tfrac14[Z_{\overline{\mathbf Q}}]
=\tfrac14\sum_{\zeta^4=1}[C_\zeta],
\qquad
\tfrac14[Z_{\overline{\mathbf F}_2}]=[C].
\]
Here the phrase “closer to \(C\)” has a precise cycle interpretation. The scheme still carries arithmetic genus thirty-three, whereas its reduction has genus zero. Genus has moved from reduced branch gluing into nilpotent structure.

The first-normal determinant explains a second transition. Its coefficient is \(4s^9t^9\); the horizontal contact information lies in \(s^9t^9\), while \(4\) carries arithmetic collision. Modulo two the determinant is identically zero, so the degree-18 divisor does not specialize as an ordinary effective Cartier divisor. The missing information reappears at higher normal order. The full normal filtration, rather than only its first determinant, is the natural continuation of the boundary map across this locus.

There are therefore two axes worth studying together: collision along the curve, measured by endpoint orders, and collision across characteristics, measured by valuations of root differences. The derivative \(4u^9\) and discriminant \(-256\) are small expressions coupling those axes. The arithmetic ruled-model notes warn that normalization and branch intersections need not commute with specialization; vertical exceptional components upstairs must not be mistaken for additional curve components downstairs.




## Arithmetic continuation

The [two-scale root-collision calculation](arithmetic_root_collision.md) proves the complete mixed-characteristic cluster and residue-polynomial analysis separately, retaining the characteristic-zero field, residue characteristic two and horizontal endpoint parameter as different data.

## Characteristic reach and limitation

The pencil equations, flat monic presentation and explicit cycle
factorizations are algebraic and can be reduced with the stated exceptional
parameters retained. The double-cover elliptic diagnostic and generalized
Jacobian decomposition as multiplicative and additive groups use the displayed
characteristic-zero assumptions. In characteristic two the root polynomial is
z^4+a z+a+1: the a=0 member is (z+1)^4 while a!=0 is separable. The
mixed-characteristic collision tree retains v(2), parameter valuation and
residue polynomials separately, so it is not a characteristic-zero
nonexistence statement. The general [positive-characteristic quartic-carrier
construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
has its separate proof.


## Exact computational support

The [root-pencil verifier](../computations/verify_ci_cycle_root_pencil_2026_10_25.py) retains the polynomial discriminant, Weierstrass invariants, special cycles and two endpoint coefficient relation. The [eight-component verifier](../computations/verify_ci_cycle_eight_component_competitor_2026_10_25.m2) supports the actual larger-delta competing scheme. These inherited calculations were not rerun in consolidation; the distinct symbolic derivations and geometric interpretations survive above.
