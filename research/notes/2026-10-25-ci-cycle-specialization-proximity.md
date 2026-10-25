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

For general \(a\), its four roots are distinct and nonzero, so the components remain four projectively equivalent smooth rational quartics with exactly the same endpoint pairwise contact. The marked-root derivative is \(4-a\); hence for \(a\ne4\) the boundary stays \(9p+9q\). The original roots-of-unity fiber is \(a=0\). See the sibling [root-pencil laboratory](2026-10-25-ci-cycle-root-pencil.md) for the independently calculated global and exceptional-parameter details. This directly shows that two-point conductor data does not force the roots-of-unity group configuration.

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
