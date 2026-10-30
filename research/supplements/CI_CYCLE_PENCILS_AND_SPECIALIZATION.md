# Complete-intersection cycles: consolidated mathematical investigations

Full source mathematical content retained in subject sections. Statements retain their original provisional or audited scope; this compilation does not promote results.


---

## 2026-10-25-ci-cycle-specialization-proximity.md

# Proximity by specialization, boundary, and arithmetic collision

Date: 2026-10-25. Exploratory contribution to the complete-intersection-cycle notebook.

**Status.** Competing pictures and proposed experiments, with elementary calculations identified below. This is not a proposed STCI theorem. Work over an algebraically closed field of characteristic zero unless a base ring or characteristic is explicitly specified. The marked curve is

\[
C=[s^4:s^3t:st^3:t^4],\qquad
Z=V(x_1^4-x_0^3x_3,\ x_2^4-x_0x_3^3).
\]

The accepted input is [STCI-R-0021](../results/quartic_mu4_degeneration.md): this prescribed integral family is flat, has four reduced quartic components in geometric characteristic zero, and has generic transverse length four on the sole reduced support \(C\) in characteristic two. Its source note supplies the local branch-separation formula and conductor boundary. The [ruled-surface synthesis](2026-10-24-p4-ruled-surfaces-synthesis.md), sections 5–6, and its linked audits supply additional **provisional, independently audited geometry**, rather than promoted results. No accepted argument is reopened here.

## 1. Start with an honest ambiguity in “closer”

A bouquet of four identical-looking curves can feel closer to one curve than an irreducible curve of degree sixteen feels. There are at least three different reasons for that intuition:

1. All normalized components are rational, so each piece has the simplest possible intrinsic geometry.
2. The three extra pieces meet the marked piece only at its two exceptional points, so all the residual contact is concentrated there.
3. The four pieces are an orbit of a very small finite group scheme, and that group scheme becomes supported at its identity in characteristic two.

These reasons need different invariants. The first concerns normalization; the second concerns a divisor on a marked normalization; the third concerns an arithmetic model. None is determined by the numerical cycle class in \(\mathbf P^3\).

For example, \(A_1(\mathbf P^3)\cong\mathbf Z\) records degree. Every \((4,4)\) complete intersection has the class \(16[\text{line}]\). Passing to numerical or Chow-group classes erases precisely the arrangement one wants to compare. A **Chow parameter point**, which remembers the actual effective cycle, is more useful here than a Chow-group class.

## 2. A cycle mass that survives powers of equations

Write the actual fundamental cycle of a complete intersection \(W=V(A_a,B_b)\) containing \(C\) as

\[
[W]=m_C[C]+R,\qquad C\not\subset\operatorname{Supp}R.
\]

Its degree is \(ab=4m_C+\deg R\). Normalize all cycles to degree four:

\[
\widehat{[W]}=\frac4{ab}[W],\qquad
\rho_C(W)=\frac{4m_C}{ab},\qquad
\epsilon_C(W)=1-\rho_C(W).
\]

The scalar \(\epsilon_C\) is the proportion of degree carried away from the marked support. It is insensitive to replacing the equations by \(A^r,B^s\): the fundamental cycle and the total degree both multiply by \(rs\). The justification is local intersection multiplicity for a regular sequence; it is not an assertion that the resulting schemes are isomorphic. For the standard definition of the fundamental cycle, see [Stacks, cycle associated to a closed subscheme](https://stacks.math.columbia.edu/tag/0AZA).

For the distinguished fibers,

\[
\rho_C(Z_0)=\tfrac14,\qquad
\widehat{[Z_0]}=\tfrac14\sum_{\zeta^4=1}[C_\zeta],\qquad
\rho_C(Z_2)=1,\qquad \widehat{[Z_2]}=[C_2].
\]

This gives a precise arithmetic version of proximity: the normalized cycle becomes exactly the marked curve cycle in characteristic two. It also reveals a limitation. Every generically simple \((4,4)\) intersection containing \(C\) has \(\rho_C=1/4\), regardless of whether its residual degree-twelve curve is smooth, reducible, or particularly symmetric. This mass sees coalescence, but cannot distinguish \(Z\) among nearby simple intersections.

The bare effective-cycle relation \([Z]\ge[C]\) is equally valid but less informative. The normalized difference \(\widehat{[Z]}-[C]\) is **not** effective in characteristic zero: its coefficient at \(C\) is \(-3/4\). Consequently an effective-cycle ordering and a normalized notion of proximity cannot be silently identified.

**Promising refinement.** Use \(\epsilon_C\) as one coordinate of a profile, together with normalization genera, boundary concentration, and a contact filtration. Do not try to make it carry the whole comparison.

## 3. Specialization gives directed paths, not a universal ranking

Over a DVR, cycles have a natural specialization map defined by closing each generic component and taking the cycle of its special fiber. A flat family specializes its fundamental cycle to the special-fiber fundamental cycle; see [Stacks, specialization of cycles](https://stacks.math.columbia.edu/tag/0H4H). Thus the accepted mixed-characteristic family gives the directed relation

\[
\sum_{\zeta^4=1}[C_\zeta]\rightsquigarrow4[C_2].
\]

The relation belongs to the chosen arithmetic family. It does not put \(C\) itself in the degree-sixteen Hilbert scheme: \(C\) has Hilbert polynomial \(4n+1\), while a \((4,4)\) complete intersection has \(16n-32\). Its characteristic-two fiber still has the latter polynomial. Reduction changes the object one is studying.

In a fixed-degree Chow variety in characteristic zero, the locus of cycles whose coefficient at a **fixed** curve \(C\) is at least \(m\) is closed. One can see this by multiplying the fixed Chow form of \(mC\) by the Chow forms of degree \(d-4m\) cycles: the source is projective, hence the image is closed. Therefore \(m_C\) can increase under specialization; \(\epsilon_C\) can decrease. This is a concrete candidate for the desired direction of a proximity order, with the preceding limitation that it is often constant. Projectivity of fixed-degree Chow parameter spaces is discussed in [Kollár, *Families of varieties of general type*, section 3.1](https://web.math.princeton.edu/~kollar/book/modbook20170720.pdf).

There is a separate trap in saying “\(W\) specializes to \(Z\)” without specifying a restricted class of deformations. If one allows arbitrary paths through the parameter space of \(C\)-containing quartic pencils, a special fiber can simply be prescribed to equal \(Z\). Such accessibility does not make \(Z\) intrinsically minimal. A useful order would need extra rules: a group orbit closure, fixed carrier, prescribed normal data, a fixed arithmetic model, or a restricted contact profile.

**Experiment.** Record a directed graph of *specified mechanisms*: split residual branches, merge roots in a finite flat cover, concentrate a boundary divisor, or increase transverse multiplicity. The arrows should retain the mechanism and base; two arrows of different kinds need not be comparable.

## 4. The boundary produces an unexpected binary-form picture

For a proper \((4,4)\) intersection that is generically simple along \(C\), take the determinant of the two first-normal sections. Its zero divisor is a degree-eighteen divisor on \(C\cong\mathbf P^1\). In the distinguished case this is

\[
B_Z=9p+9q,\qquad [b_Z]=[s^9t^9]\in\mathbf P H^0(\mathbf P^1,\mathcal O(18)).
\]

Here “first-normal” refers to \(I_C/I_C^2\), and the ambient quartic twist has degree sixteen on \(\mathbf P^1\). The determinant has degree \(-14+32=18\); the balanced characteristic-zero splitting is the accepted [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md). The equality of this determinant divisor with the residual intersection divisor requires the simple-component, proper-intersection setting. It should not be used when the determinant vanishes identically.

Now temporarily forget the marked embedding and allow the full \(\mathrm{PGL}_2\) of the abstract normalization. Binary-form GIT says that a degree-eighteen divisor is semistable if every point has multiplicity at most nine, and stable if every multiplicity is smaller than nine. The form \(s^9t^9\) is the closed, strictly semistable orbit. Every strictly semistable binary form has this orbit in its semistable orbit closure. These standard facts are explicitly recalled in [Alper–Isaev, *Associated forms and hypersurface singularities: the binary case*, section 5.2](https://sites.math.washington.edu/~jarod/papers/binary.pdf).

This is a surprisingly exact version of “concentrated but balanced.” The divisor has the fewest possible support points among semistable degree-eighteen divisors, and its two masses are equal. A one-point divisor of degree eighteen is more concentrated, but is unstable for this comparison.

**Why this could work.** A boundary map might place the special configuration on a distinguished polystable boundary of a moduli problem. The two points then express balance as well as concentration. One could investigate how the four branches, their conductor modules, and the embedding lift the coarse binary-form datum.

**Why it may fail.** A generic divisor of eighteen distinct points is stable. Its orbit is closed in the semistable locus, so its \(\mathrm{PGL}_2\)-orbit does not contain \([s^9t^9]\) in that locus. This is not a universal flow from every boundary to the special one. Moreover, the full \(\mathrm{PGL}_2\) changes the embedded hyperplane system. For the fixed embedding the relevant ambient stabilizer is smaller. The larger quotient is a deliberate change of viewpoint, not a projective-automorphism equivalence of embedded configurations.

## 5. Boundary alone must have large fibers

There is an elementary dimensional reason to retain more information than \(B_Z\). Let

\[
V=H^0(\mathbf P^3,I_C(4)),\qquad \dim V=18.
\]

The dimension follows from quartic restriction: there are 35 ambient monomials and all 17 degree-sixteen monomials on \(\mathbf P^1\) occur. The quartic-pencil space is \(\operatorname{Gr}(2,V)\), of dimension 32. Taking the wedge of the first-normal map defines the rational map

\[
\beta:\operatorname{Gr}(2,18)\dashrightarrow
\mathbf P H^0(\mathbf P^1,\mathcal O(18))=\mathbf P^{18}.
\]

It is a linear map in Plücker coordinates followed by projectivization. It is defined in a neighborhood of the distinguished point because its determinant is nonzero there. Locally a fiber is cut out by at most eighteen equations in a smooth 32-dimensional space, so every component through the distinguished point has dimension at least fourteen. Restricting to the open proper-complete-intersection locus does not remove this local lower bound.

This calculation does **not** assert dominance, smoothness, reducedness, or a classification of any fiber. It does say that the divisor \(9p+9q\) cannot by itself characterize the four-component configuration. The distinguished point sits in a substantial family with the same first-normal boundary. Higher gluing, residual topology, or symmetry must distinguish it.

There is already an explicit line of examples in this fiber. Put \(Q=x_0x_3-x_1x_2\) and perturb only the second equation:

\[
G_a=G+a x_3^2Q.
\]

On \(F=0\), substituting \(x_2=\lambda u^3\) gives

\[
\lambda^4-a\lambda+a-1
=(\lambda-1)(\lambda^3+\lambda^2+\lambda+1-a).
\]

For general \(a\), its four roots are distinct and nonzero, so the components remain four projectively equivalent smooth rational quartics with exactly the same endpoint pairwise contact. The marked-root derivative is \(4-a\); hence for \(a\ne4\) the boundary stays \(9p+9q\). The original roots-of-unity fiber is \(a=0\). See the sibling [root-pencil laboratory](#2026-10-25-ci-cycle-root-pencilmd) for the independently calculated global and exceptional-parameter details. This directly shows that two-point conductor data does not force the roots-of-unity group configuration.

**Next experiment.** Compute a small slice of \(\beta^{-1}([s^9t^9])\) and test whether nearby members preserve four rational components, or instead replace them by fewer components with positive normalization genus. This is more informative than merely rediscovering the divisor.

## 6. Arithmetic collision has a second, independent valuation

The accepted local equation on \(x_0=1\) is

\[
P(u,Y)=(u^3+Y)^4-u^{12},\qquad
P_Y(u,0)=4u^9.
\]

At the marked branch this derivative is the product of separations from the other three branches. It factors into two quite different collision contributions:

- \(u^9\) records the three order-three contacts at the geometric endpoint;
- \(4\) records failure of the four-root algebra to be étale at the arithmetic prime two.

On the torus the algebra is \(A[z]/(z^4-1)\). In the basis \(1,z,z^2,z^3\), its trace-pairing matrix is

\[
\begin{pmatrix}
4&0&0&0\\
0&0&0&4\\
0&0&4&0\\
0&4&0&0
\end{pmatrix},\qquad \det=-256.
\]

This is a fresh, elementary calculation, checked by a direct determinant expansion using only Python's standard library. It is the discriminant of the finite rank-four algebra, not the conductor of the global curve. For the trace-pairing discriminant and its étale interpretation, see [Stacks, discriminant of a finite locally free morphism](https://stacks.math.columbia.edu/tag/0BVH).

Likewise the local polynomial \(w^4-u^{12}\), with \(w=u^3+Y\), has discriminant \(-256u^{36}\). The exponent 36 is twice the sum of the six pairwise contact orders, \(2\cdot6\cdot3\). The derivative at one branch uses three separations and therefore has exponent nine; the full discriminant uses all pairs and squares them. These are related but different invariants.

After the splitting extension \(A=\mathbf Z_2[i]\) with uniformizer \(\pi=1-i\), the root differences from 1 have valuations

\[
v_\pi(1-i)=1,\qquad v_\pi(1+i)=1,\qquad
v_\pi(1-(-1))=2.
\]

Their sum is \(v_\pi(4)=4\). Locally a pairwise separation is a unit times \(\pi^a u^3\). A two-coordinate valuation \((a,3)\), or a weighted valuation \(a\alpha+3\gamma\), keeps arithmetic coalescence and endpoint contact visible at once. This is a promising “collision budget” picture.

**Scope warning.** The full derivative is zero after reduction modulo two. Its degree-eighteen horizontal zero divisor cannot simply be reduced as though it remained a nonzero section. Dividing by the common arithmetic factor 4 in this explicit integral model recovers \(s^9t^9\), but making such a primitive normalization functorial in larger parameter spaces is a new problem. It needs a specified model and saturation rule.

## 7. Normal cones can detect contact, but arithmetic base change matters

The source note gives, on the characteristic-zero endpoint chart,

\[
\operatorname{gr}_{(Y)}k[u,Y]/(P)
\cong k[u,\eta]/(u^9\eta).
\]

The positive-degree pieces are supported at the endpoint: they measure residual branches meeting the marked branch. In characteristic two the actual normal graded algebra is instead \(k[u,\eta]/(\eta^4)\), with positive-degree pieces extending along the whole curve. This is an appealing geometric change: contact that was confined to two places becomes transverse thickness everywhere.

The associated graded algebra of the integral model is

\[
\mathbf Z[u,\eta]/(4u^9\eta),
\]

whose reduction modulo two is \(\mathbf F_2[u,\eta]\), **not** the actual special-fiber graded algebra \(\mathbf F_2[u,\eta]/(\eta^4)\). Thus the normal-cone construction and the characteristic-two base change do not commute here. A proposed ordering based only on first symbols would lose the order-four relation that causes coalescence.

The deformation-to-the-normal-cone construction is still useful, but it deforms to a different ambient geometry, and exceptional components there must not be counted as additional components downstairs. For the construction, see [Vakil, *The Rising Sea*, exercise 22.4.U and section 24.3](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf). For this investigation it is best regarded as a microscope for the marked embedding, not as an automatic path among complete intersections in the original \(\mathbf P^3\).

## 8. A spectral-cover analogy that deserves a controlled test

On the provisional common ruled model, the strict four-section divisor is

\[
q^4-h^4=0,\qquad h=st^3\in H^0(\mathbf P^1,\mathcal O(4)).
\]

Away from \(h=0\), dividing by \(h\) turns the configuration into four constant points \(q/h=\zeta\). Resolving the graph pencil makes those points constant sections of a product surface. Hence much of the apparent complexity lies in how the trivial four-point cover is compactified at the zeros of \(h\), and in the nonnormal carrier map back to \(\mathbf P^3\).

One may compare this with a spectral polynomial in a line-bundle coordinate:

\[
q^4+a_1q^3+a_2q^2+a_3q+a_4,
\qquad a_j\in H^0(\mathbf P^1,\mathcal O(4j)).
\]

Retaining the section \(q=h\) imposes the polynomial identity obtained by substituting \(h\). The other three sheets may ramify, form an irreducible degree-three cover, or collide. Their discriminant is then a natural competitor to the boundary at the marked sheet.

This is an **analogy and a larger laboratory**, not an assertion that arbitrary such coefficients come from ambient quartic perturbations. Ambient descent through the singular carrier restricts the coefficients, and strict lifts omit full-inverse-image corrections. The source geometry explicitly distinguishes pairwise divisor \(3p+q\) on the ruled model from \(3p+3q\) downstairs. The experiment must keep the actual map to \(\mathbf P^3\).

## 9. A practical profile, with no claim of total order

A useful exploratory data record for \(W\supset C\) could be

\[
\left(
\epsilon_C(W),\;
\{g(\widetilde D_i)\}_i,\;
B_C(W),\;
\text{contact filtration},\;
\text{arithmetic root-collision data}
\right).
\]

Each coordinate has a reason to matter and an obvious blind spot. The degree fraction ignores contact; genera ignore how pieces are glued; the boundary has large fibers; finite normal data may lose later cancellations; arithmetic collision depends on a model. These limitations are productive: they indicate which extra observation is needed when two configurations look equally close by one measure.

The most promising first comparison is therefore not “every \(Z'\) ranks above \(Z\).” It is: **within a specified deformation class, which parts of the residual degree, normalization genus, and gluing budget can move into contact with \(C\), and which can become transverse multiplicity?** The distinguished configuration provides an unusually transparent point where all three languages—four-point orbit, two-point boundary, and arithmetic thickness—can be compared.

## 10. Next experiments and audit questions

1. Compute a local slice of the degree-eighteen boundary map at \(Z\); keep the expected large fiber and ask what residual topologies occur there.
2. Separate binary-form GIT for the abstract normalization from the action of the actual embedded stabilizer. Determine which boundary strata remain distinguished in the smaller quotient.
3. Perturb the spectral polynomial while retaining \(q=h\), then test precisely which perturbations descend to ambient quartics and preserve a proper intersection.
4. For explicit integral perturbations, record both the horizontal boundary divisor and the valuation of its common arithmetic content. Test whether a natural saturation makes the pair behave well under base change.
5. Compare the full Rees algebra before and after reduction modulo two, rather than only its first-symbol matrix. The existing example already shows why this distinction changes the answer.

An independent reviewer should check especially the domain of the boundary map, the simple-component hypothesis behind its intersection interpretation, the change from embedded to abstract \(\mathrm{PGL}_2\), and the distinction between a finite-cover discriminant and the conductor of a global curve. The new contribution is an exploratory organization and these testable proposals; no canonical record is changed.



---

## 2026-10-25-ci-cycle-root-pencil.md

# A root pencil through the four-quartic configuration

Date: 2026-10-25. **Exploratory contribution; not canonically promoted.**
This note studies actual complete intersections containing the fixed embedded
curve, and introduces a small laboratory for contact, component multiplicity,
and a possible elliptic moduli invariant. It is not an STCI argument.

## Inputs, conventions, and status

Work over an algebraically closed field of characteristic zero until a change
is explicitly stated. Let

\[
C=[s^4:s^3t:st^3:t^4],\quad
F=x_1^4-x_0^3x_3,\quad
G=x_2^4-x_0x_3^3,\quad Q=x_0x_3-x_1x_2.
\]

The established input is [STCI-R-0021](../results/quartic_mu4_degeneration.md),
with its [source discussion](2026-10-23-quartic-characteristic-conormal.md):
\(V(F,G)\) is the reduced union of the four \(C_\zeta\) in characteristic
zero and has reduced support \(C\), generic multiplicity four, in
characteristic two. The common ruled-surface picture in
[the October 24 synthesis](2026-10-24-p4-ruled-surfaces-synthesis.md) is
reviewed provisional evidence; none of its global claims is needed below.

The family, discriminant, and elliptic interpretation below are fresh
exploratory calculations. The [exact verifier](../computations/verify_ci_cycle_root_pencil_2026_10_25.py)
and its [JSON output](../computations/ci_cycle_root_pencil_2026_10_25.json)
check thirteen polynomial identities using Python's standard library. Those
identities do not themselves prove any global extremality principle.
Independent notebook review is recorded separately by the notebook owner.

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

## 5. Why this is a useful laboratory, and what it cannot decide

The member \(a=4\) makes a concrete distinction between several kinds of
proximity. Normalized cycle mass carried by \(C\) grows from \(1/4\) to
\(1/2\); the generic transverse length on \(C\) grows from one to two;
the reduced support loses one component; and the degree-eighteen
first-normal boundary ceases to be a divisor. These changes occur in a
flat family with fixed Hilbert polynomial \(16n-32\). Thus they are
compatible but genuinely different observables.

At \(a=\infty\), the normalized mass carried by \(C\) remains \(1/4\),
the determinant boundary is unchanged, and the residual geometry changes
radically. At general finite \(a\), the same boundary and contact orders
coexist with a varying elliptic modulus. Together these comparisons
argue for a vector of invariants or a stratification, rather than one
universal distance.

In characteristic two the formula reduces to
\(f_a(z)=z^4+a z+a+1\). Its derivative is \(a\). Therefore the special
member \(a=0\) is \((z+1)^4\), whereas generic \(a\ne0\) has four distinct
geometric roots. The characteristic-zero collision parameter \(4\)
reduces to the same special parameter \(0\). The rational formula (7)
is not a useful characteristic-two invariant of this double cover:
\(w^2=f_a(z)\) is an inseparable equation there. A characteristic-two
analogue would need an appropriate separable cover or a different moduli
construction, not reduction of this formula.

Promising next experiments are: test the agreement of the endpoint moduli
when the carrier moves; map this pencil into the full determinant-boundary
fiber in \(\operatorname{Gr}(2,H^0(I_C(4)))\); compute residual schemes at
the three collision values with their nilpotent structures; and trace
the four-sheet moduli under a deformation that moves the boundary points.
Nothing here closes or reopens a canonical STCI question.



---

## 2026-10-25-ci-cycle-conductor-topology.md

# Conductor, topology, and where the genus is stored

Date: 2026-10-25. Status: exploratory contribution to the complete-intersection cycle notebook; new calculations and interpretations below are provisional, pending the package audit. This is geometry of cycles containing the fixed curve, with no STCI objective or canonical promotion.

Throughout the main discussion, the field is algebraically closed of characteristic zero; assertions about Betti numbers use the associated complex curve. Set

\[
C=[s^4:s^3t:st^3:t^4],\quad
F=x_1^4-x_0^3x_3,\quad G=x_2^4-x_0x_3^3,
\quad Z=V(F,G).
\]

Write \(p=[1:0:0:0]\), \(q=[0:0:0:1]\). The prescribed four-component decomposition and mixed-characteristic flatness are promoted in [STCI-R-0021](../results/quartic_mu4_degeneration.md); its [source note](2026-10-23-quartic-characteristic-conormal.md), Section 1, supplies the endpoint contact calculation. These established inputs are used without rerunning their proof. The ruled cubic used for a competing example below comes from [the independently reviewed provisional cubic-scroll note](2026-10-24-cubic-scroll-normalization.md); that geometry has not been promoted canonically.

## 1. An intuitive starting point: the same genus in different places

A useful picture is that arithmetic genus is a budget. It can live in the genera of normalized components, in loops made by gluing components, or in higher-order infinitesimal gluing invisible to the underlying topology. The special curve puts a striking amount into the third account.

At \(p\), eliminating the smooth equation \(F\) gives the plane germ

\[
f(u,y)=y^4-u^{12}=0,
\]

where \(u=x_1\), \(y=x_2\). Its four branches are \(y=\zeta u^3\), \(\zeta^4=1\). A pair of branches has contact three, so

\[
\delta_p=\sum_{i<j} I_p(C_i,C_j)=6\cdot3=18.
\]

The same calculation holds at \(q\). Consequently

\[
\delta(Z)=36,\qquad
p_a(Z)=\sum_i g(C_i)+\delta(Z)-4+1=33.
\]

This number also follows from the complete-intersection formula. Its meaning here is particularly transparent: all four normalized components are rational, and all the arithmetic genus arises from the way they are attached.

Let \(D=C_{-1}\cup C_i\cup C_{-i}\) be the residual union to \(C=C_1\). At either endpoint, its three pairwise contacts contribute \(3\cdot3=9\), so \(\delta(D)=18\) and \(p_a(D)=18-3+1=16\). Meanwhile

\[
C\cap D=9p+9q,\qquad \operatorname{length}(C\cap D)=18.
\]

Thus

\[
33=p_a(C)+p_a(D)+18-1=0+16+18-1.
\]

This is a promising deformation picture: a nearby smooth residual curve of genus sixteen would trade its eighteen units of singularity defect for intrinsic genus, while the marked attachment divisor on \(C\) retains total degree eighteen. The genus is moving from gluing to handles, without changing the Hilbert polynomial.

The residual genus is **sixteen**, not seventeen. The liaison difference is
\((4+4-4)(12-4)/2=16\); the union formula above is an independent check.

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

## 7. Candidate invariants worth carrying forward

- **Marked boundary distribution.** Total degree is fixed by (1), but support size, endpoint weights, and multiplicity partitions can vary. Concentration is geometrically meaningful, while a numerical concentration score would need a fixed normalization and a decision about endpoint weighting. Without symmetry, a single point of multiplicity eighteen is even more concentrated than \(9p+9q\), if realizable; the latter is special as the balanced symmetric divisor.
- **Residual singularity defect.** For a reduced \(C\cup D\), \(\delta(C\cup D)=\delta(D)+\operatorname{length}(C\cap D)\) when \(C\) is smooth. This separates attachment from internal residual geometry. At \(Z\) the two summands are eighteen and eighteen. Delta is useful for specialization in suitable reduced families, but does not extend by simply reducing a generically nonreduced fiber.
- **Generalized-Jacobian signature.** The vector \((a,t,u)\) distinguishes handles, topological loops, and higher contact. The value \((0,3,30)\) is a concise description of the special arrangement. It captures more than either arithmetic genus or reduced-support topology.
- **Decorated gluing graph.** Four vertices joined at two multi-branch points, with pairwise contact three and conductor weight nine, retains the incidence and the tangency. An ordinary dual graph loses both multiplicities and three-dimensional embedding data. A metric/tropical enhancement could assign lengths from a chosen one-parameter degeneration, but those lengths depend on the degeneration and are not presently intrinsic to \(Z\).
- **Canonical boundary plus visible symmetry.** The pair \((C,9p+9q)\) is canonically meaningful relative to the embedding and has a unique invariant boundary of the forced degree under the displayed torus and swap. Whether the complete intersection is extremal within its boundary fiber remains an attractive, genuinely open experiment.

## 8. Audit and continuation boundary

This contribution separates a promoted input (the prescribed degeneration), reviewed but unpromoted ruled-surface geometry, direct numerical/topological calculations, a finite coordinate computation, and exploratory interpretations. The parent package's independent reviewer should reconstruct the genus sixteen calculation, the generalized-Jacobian ranks, the distinction between marked and full conductor boundaries, and the reduced eight-component competitor. No canonical research result, question, or STCI frontier is changed.

Promising next computations are the boundary-map image, the local marked deformation of \(y^4-u^{12}\) into nine transverse attachments while preserving the branch \(y=u^3\), and the Picard signature along such a global family. The last two require an actual family and should not be inferred solely from compatible numbers.

