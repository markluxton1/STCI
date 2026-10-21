# Characteristic-zero STCI consequences of the intrinsic obstruction

Date: 2026-10-21. **Status: new research proposal with proofs and an independent mathematical check of the principal new implications; no canonical promotion.** The unrestricted characteristic-zero STCI question for the fixed quartic remains open.

The main positive result below is a necessary condition that incorporates the *actual first-normal defect divisor* of a generically curvilinear complete intersection. The obstruction need not vanish globally: it must vanish after allowing poles bounded by that divisor. For the distinguished quotient from the arithmetic problem this forces a divisor of degree at least two, with a precise condition in degree two. This is a restriction on a specified normal direction, not an exclusion of arbitrary characteristic-zero STCI presentations.

The principal negative results are also definite. A global complete intersection with smooth support can be generically primitive and still contain no global primitive triple; this remains true with integral projective defining surfaces. Spreading a characteristic-zero pair preserves support after spreading finite ideal identities, but cannot force residue characteristic two, the specified marking, or the prescribed special scheme. Direct flat specialization of a hypothetical surviving quartic STCI intersection to the multiplicity-four scheme Z4 is already impossible by degree.

## 1. Exact setup, inherited claims, and authority

Unless a statement specifies otherwise, k is an algebraically closed field of characteristic zero,

\[
C=C_0=\{[s^4:s^3t:st^3:t^4]\}\subset X=\mathbf P^3_k,
\qquad I=I_C.
\]

Let F,G be homogeneous forms of degrees d,e, with no common surface component, and put J=(F,G), Z=V(J). First one may consider only C contained in the reduced intersection; then the fundamental cycle is m[C]+R with R effective and not containing C. The STCI hypothesis used here is the stronger equality Supp(Z)=C, equivalently R=0 together with the asserted set-theoretic support. Exceptional curves above points of C on a blow-up are not additional curves downstairs.

The following are inherited premises, rather than computations repeated in this report.

* [STCI-R-0001](../results/quartic_carrier_exclusion.md), with its accepted lower-degree and factor reduction, gives d,e at least five for any characteristic-zero STCI presentation of this C. Its complete quartic-carrier exclusion is not reopened here.
* The fixed normal bundle is N=O(7) squared, hence E=I/I²=O(-7) squared. The basic generic local intersection and blow-up restrictions are recorded in [the simultaneous-surfaces synthesis](../synthesis/02-two-surfaces.md); the entirely-thick inequalities are not asserted to exclude that branch.
* [STCI-R-0012](../results/prescribed_z4_arithmetic_nonlifting.md) rules out the prescribed flat embedded Z4 lift over exactly Z_(2) and Z_2. It does not exclude arbitrary characteristic-zero STCI presentations or arbitrary ramified bases.
* The [corrected independent ribbon-to-triple audit](2026-10-21-intrinsic-ribbon-triple-independent-audit.md) constructs, for a line quotient q:E onto L with kernel M, the canonical extension

  \[
  0\longrightarrow L^2\longrightarrow B_q
  :=J_2/(I J_2+I^3)\longrightarrow M\longrightarrow0,
  \qquad J_2=\ker(I\to L).
  \tag{1}
  \]

  Its Yoneda class o_X(q) in H¹(M dual tensor L²) vanishes precisely when the fixed embedded ribbon admits an ambient embedded primitive triple. This is independently audited evidence, not a new promoted canonical record. The distinction matters: the ambient triple need not be contained in a given Z.
* The [persistent independent audit](2026-10-21-z4-persistent-independent-audit.md) proves the fixed marked integral first-order calculation and its precise relative meaning. In particular, every admissible integral quotient reducing to the specified q0 has a middle obstruction coefficient 2 modulo 4. This additional relative conclusion is audited evidence, rather than a broader restatement of R0012.

The [existing literature assessment](2026-10-21-z4-intrinsic-obstruction-literature.md) has been consulted. Its distinction between abstract multiple curves and fixed-ambient embedded extension is retained. No claim of priority over the multiple-curve literature is made for the elementary consequences proved here. The reports and the present proofs establish the stated scope; a familiar analogy with abstract extension or divided Frobenius is not being used as a theorem.

## 2. What an actual STCI presentation forces

### 2.1 Complete intersection, purity, and generic length — proved

The two equations have height two. Thus Z is a one-dimensional local complete intersection and is Cohen–Macaulay, Gorenstein, and unmixed. In the STCI situation its only associated support component is C; it has neither a residual curve nor an isolated embedded component.

At the generic point eta of C, the completed transverse regular local ring is K[[u,v]], K=k(C), and

\[
A_\eta=K[[u,v]]/(F,G)
\]

is a zero-dimensional complete intersection of length

\[
m=de/4\in\mathbf Z_{>0}.
\tag{2}
\]

The equality uses the full STCI support condition. With residual curves one only has de=4m+deg(R). If r,s are the normal orders of the displayed equations, m is at least rs; equality holds when their initial binary forms are coprime. Their first symbols need not generate the full initial ideal: (u²,u²+v³)=(u²,v³) is the basic cancellation example.

The maximal ideal of a local Artin algebra of length m has m-th power zero. Since O_Z injects into its localization at the unique generic associated point, this gives, sheaf-theoretically,

\[
I^m\subset J\subset I.
\tag{3}
\]

The injection follows from unmixedness: every function outside the prime of C is a nonzerodivisor. It is not inferred merely from equality of cycles. A larger finite power also suffices for every spreading argument below.

### 2.2 First-normal information and its exact limitations — proved

Write N1=image(J to E). If at least one equation has generic normal order one, N1 has generic rank one and A_eta is curvilinear, isomorphic to K[z]/(z^m). The saturation M of N1 in E is a line subbundle; its quotient L=E/M is invertible. On the smooth curve there is a unique effective divisor D such that

\[
N1=M(-D).
\tag{4}
\]

Here D is the common zero divisor of the *actual two first-normal symbols*, measured in their saturated line. It is not one of the divisors D_i of a saturated quasiprimitive order filtration. In particular it should not be silently substituted into [R0019](../results/quasiprimitive_residual_cycles.md).

If L=O(epsilon-7), then M=O(-7-epsilon), epsilon is nonnegative, and the two symbols are sections of

\[
M(4d)=O(4d-7-epsilon),\qquad
M(4e)=O(4e-7-epsilon).
\tag{5}
\]

One symbol can be zero identically. Where both vanish, both surfaces are singular along C in their normal directions. Saturation extends the generic direction, but does not supply a primitive triple in Z.

If both generic orders are at least two, N1=0; there is no preferred line quotient of E forced by the pair. The higher first relation, horizontal common-direction curve, and full initial ideal then require the additional hypotheses in such results as [R0006](../results/actual_ci_smooth_root_bridge.md). Neither the arithmetic Z4 result nor the construction (1) fills those interfaces.

## 3. A new necessary condition: defect-twisted obstruction vanishing

### Proposition A — proved

Let C be a smooth integral curve regularly embedded with codimension two in a smooth threefold, over any field. Let J be an ideal with support C, whose generic transverse algebra is curvilinear of length m at least three. Assume its first-normal image has rank one, and define M,L,D by (4). Set H=M dual tensor L². Then

\[
o_X(q)\longmapsto0
\quad\text{under}\quad
H^1(C,H)\longrightarrow H^1(C,H(D)).
\tag{6}
\]

Equivalently,

\[
o_X(q)\in
\operatorname{im}\bigl[H^0(C,H(D)/H)\longrightarrow H^1(C,H)\bigr].
\tag{7}
\]

Thus the ambient extension may have a nonzero obstruction, but the actual pair supplies a meromorphic splitting with poles bounded by its first-normal defect divisor. This assertion does not claim that the corresponding triple is globally contained in Z.

**Proof.** Since the first symbols of J lie in M, one has J contained in J2. Map J into B_q in (1), and let P be its image. This is an O_C-module: multiplication by I kills B_q. Its image under B_q to M is exactly N1=M(-D).

At eta choose adapted transverse parameters f,y with J_eta=(f,y^m); the existence of f with nonzero linear part follows from generic curvilinearity. For m at least three, y^m maps to zero in B_q because I³ is killed. The image of f spans a line that projects isomorphically to M_eta. Hence P_eta meets L²_eta trivially.

The kernel of P to M is a subsheaf of the line bundle L². It has generic rank zero, so it is zero on the integral curve. Consequently P is isomorphic to N1. Its inclusion in B_q is a lift of N1 to B_q and therefore a splitting of the pullback of (1) along N1 to M. Pullback of extensions induces the map

\[
\operatorname{Ext}^1(M,L^2)\to
\operatorname{Ext}^1(M(-D),L^2)
=H^1(H(D)),
\]

which proves (6). The long exact sequence of 0 to H to H(D) to H(D)/H to 0 proves (7). All images here are sheaf images; no unproved flatness of an ordinary associated graded is used. The proof fails for m=2 because the second generator y² survives in L². End of proof.

For projective C, Serre duality gives the equivalent incidence condition

\[
\langle o_X(q),V\rangle=0
\quad\text{for every}\quad
V\in H^0(C,\omega_C\otimes H^{-1}(-D)).
\tag{8}
\]

This form makes explicit which divisor data would have to be imposed on the actual homogeneous first symbols.

### Concrete corollary for the distinguished q0 — proved, restricted direction

For the fixed quartic and the distinguished marked characteristic-zero quotient q0 from the integral calculation,

\[
L=O(-6),\quad M=O(-8),\quad H=O(-4),\qquad
o_X(q0)=-6[u^{-2}].
\]

If a characteristic-zero STCI pair has generic normal order one and its saturated quotient is this q0, then its divisor D in (4) satisfies

\[
\deg D\ge2.
\tag{9}
\]

If deg D=2, write its defining binary quadratic in the marked coordinates as

\[
Q_D=A s^2+B st+C t^2.
\]

Then a further necessary condition is B=0. For deg D at least three the first obstruction in (6) is automatically killed, so this argument gives no further restriction.

**Proof.** Under the audited Laurent/Serre pairing, [u^-2] is the functional extracting the middle coefficient of a binary quadratic. For D=0 it is nonzero. For D=P a point, H0(O(2)(-P)) is the kernel of evaluation at P. A nonzero functional annihilates this kernel exactly if it is proportional to evaluation at P. The evaluation functionals have coordinates [a²:ab:b²]; none equals [0:1:0] in characteristic zero. Thus degree one cannot work. In degree two, H0(O(2)(-D)) is spanned by Q_D and (8) is exactly B=0, including nonreduced divisors. In degree at least three H¹(O(-4+D))=0. End of proof.

This is a condition on actual surface singularity/common-zero data. It does not assert that any such pair exists, or that the incidence condition suffices to lift all later stages. The q0 label includes the chosen integral embedding and marking; it is not assigned to every quotient of degree -6.

### Size of the unrestricted first obstruction — proved

For any line quotient of E=O(-7) squared with L=O(epsilon-7),

\[
H=M^\vee\otimes L^2=O(3epsilon-7),\qquad
h^1(H)=\max(0,6-3epsilon).
\tag{10}
\]

Therefore the first embedded ribbon-to-triple obstruction vanishes for **every** such quotient when epsilon is at least two. All those ribbons have ambient embedded primitive triples, irrespective of whether a particular STCI scheme contains them. In the accepted order-one range 0 at most epsilon at most 6, only epsilon=0 or 1 can be detected at this first stage.

Even epsilon=1 does not uniformly obstruct. The inherited full cubic coefficient formulas are

\[
\begin{aligned}
C_1&=h(ah+3b^2-5bd+3d^2),\\
C_2&=(b-d)(4ah+3b^2-8bd+6d^2),\\
C_3&=a(ah+9b^2-23bd+15d^2).
\end{aligned}
\tag{11}
\]

The distinguished parameters (a,b,d,h)=(0,0,1,0) give (0,-6,0). By contrast (0,1,1,0) gives (0,0,0). The latter quotient is surjective on both charts: its local pairs are (p,q)=(u,1) and (P,Q)=(-c,-1). Thus there is an actual unobstructed quotient of the same degree. It does not reduce to the prescribed q0 modulo two, so there is no conflict with the marked integral obstruction.

## 4. Exactly when an actual pair supplies a primitive triple

### Proposition B — proved: an all-points sufficient condition

Suppose locally at **every** point of C there is f in J with nonzero linear normal coefficient, and

\[
J\subset(f)+I^3.
\tag{12}
\]

Then J3=J+I³ is a globally defined embedded primitive triple, contained in Z. Its local ideal is (f,y³) for I=(f,y); its ribbon is induced by the first-normal image, and its obstruction (1) vanishes.

Indeed (12) and f in J give J+I³=(f)+I³=(f,y³). These local expressions concern one global ideal J+I³, so no extra gluing choice is being assumed. The condition is pointwise, rather than merely generic.

In particular, if Z is an actual local complete intersection with support exactly C, generic multiplicity m at least three, and its first-normal image is a line subbundle of E **everywhere** (D=0), then it is locally a primitive m-fold structure and Proposition B applies. To prove this, choose f in J generating the first-normal image at a given point. The surface W=(f) is smooth there and C is Cartier on W, say with equation y. The remaining equation has zero support exactly C on W. The regular local ring of W is factorial, so that equation is a unit times y^m. Its exponent is the generic multiplicity. Thus J=(f,y^m), and (12) follows. The same proof works relatively over a DVR for a smooth relative setup with this everywhere rank-one condition and the asserted total support.

Proposition A recovers ambient vanishing when D=0; the local support argument in this paragraph additionally proves containment of the primitive triple in Z.

### Counterexample C — generic primitivity does not globalize

Let C be the line V(x,y) in projective three-space with coordinates [t:x:y:w], and consider the complete intersection

\[
Y=V(x^2,y^2+t x).
\tag{13}
\]

Its support is exactly C. The two *integral* quadrics

\[
F=x^2+y^2+t x,\qquad G=x^2+2y^2+2t x
\tag{14}
\]

generate the same ideal, since 2F-G=x² and G-F=y²+t x. Each has rank three in characteristic zero, hence is irreducible even over the algebraic closure.

On w=1 the algebra is free over k[t] with basis 1,x,y,xy: it is a monic quadratic extension of k[t][x]/(x²). Where t is invertible,

\[
(x^2,y^2+t x)=(x+y^2/t,y^4),
\]

so Y is generically primitive of multiplicity four. At the point t=0, however, its transverse algebra is k[x,y]/(x²,y²). There is no surjection from this algebra to k[z]/(z³). Any such map sends x to az+bz² and y to cz+dz²; squaring forces a=c=0, so the images cannot generate z. A primitive triple inside Y near that point would be finite flat of rank three over the local t-axis and would give exactly this forbidden quotient after setting t=0. Hence no global primitive triple is contained in Y.

There is nevertheless a global embedded ribbon V(x,y²) contained in Y. Its quotient has M=L=O_C(-1), so its *ambient* obstruction lies in H¹(O(-1))=0. The ambient primitive triple V(x,y³) exists, but is not contained in Y: y²+t x maps to y². Thus even an actual induced ribbon and a vanishing ambient Yoneda class do not establish the missing containment implication. The generic triple kernel x+y²/t displays the unavoidable pole.

This example disproves the general implication using a smooth projective support and integral defining surfaces. Its support is a line, not C0. It does not disprove a possible special theorem using extra geometry of C0. Such a theorem must supply that additional argument; generic local complete intersection or generic curvilinearity is insufficient.

For completeness, even generic primitivity itself need not hold for a complete intersection: (u²,v²) in K[[u,v]] has embedding dimension two and no curvilinear length-three quotient by the same argument. Its Gorenstein property does not change this fact.

## 5. Spreading out: what survives, and what does not

### Proposition D — proved: support-preserving finite-type spread

For a characteristic-zero STCI pair of the fixed C there is a finite-type integral Z-algebra A contained in k and forms F_A,G_A of the same degrees such that

\[
I_A^N\subset(F_A,G_A)\subset I_A
\tag{15}
\]

as ideals, for some finite N, and every field fiber has reduced support exactly C. One may arrange that Z_A is a flat relative complete intersection of type (d,e).

**Proof.** Projective support equality gives height two for (F,G). Its homogeneous quotient is Cohen–Macaulay of depth two, so (F,G) is saturated. Hence its homogeneous radical is I_C and some homogeneous power I_C^N lies in (F,G). This explains the passage from sheaf support to homogeneous polynomial identities.

The fixed integral model of C can be given by

\[
\begin{aligned}
q&=x_0x_3-x_1x_2,& f&=x_1^3-x_0^2x_2,\\
h&=x_1^2x_3-x_0x_2^2,& g&=x_2^3-x_1x_3^2.
\end{aligned}
\]

It is the standard relative P¹: on x0 nonzero the chart is A[u] with coordinates (1,u,u³,u⁴), and on x3 nonzero it is the analogous chart A[c]. These charts cover the projective scheme, since x0=x3=0 forces x1=x2=0 at every homogeneous prime.

Choose finite membership identities expressing F,G in this ideal and each monomial generator of its N-th power in (F,G). Adjoin to Z every coefficient in those identities and in F,G. The resulting domain A is finite type, and the identities hold over A and after **every** base change. Thus every field fiber has the prescribed radical. This argument does not assume that tensor product preserves injections.

Every field fiber is then a height-two intersection of the same two positive-degree forms, hence a regular sequence. The fiberwise regular-sequence flatness criterion gives A-flatness of O_Z and the relative regular sequence; see [Stacks, Lemma 10.99.3, tag 00MG](https://stacks.math.columbia.edu/tag/00MG). Alternatively, generic flatness followed by a principal-open shrink suffices, and leaves the identities intact. End of proof.

The fixed Hilbert polynomial is

\[
P_Z(n)=de\,n+de(4-d-e)/2.
\tag{16}
\]

Generically defined conormal quotients can also be spread after enlarging A and shrinking: descend the morphism to O(l) on P¹_A, then remove the proper image of its nonsurjectivity locus. Properness of C_A makes that image closed, and the kernel is then a line bundle. This is an existence statement after localization; it gives no control over which residue characteristics survive. A primitive triple that actually exists over k can similarly be spread, but that does not mean its flat closure is primitive over every originally chosen special point.

Over a general finite-type integral Z-algebra, the locus removed by shrinking is a proper closed locus, **not necessarily finitely many points or rational primes**. In particular, A[1/2] is always another valid spread of the same characteristic-zero data. Therefore no existence theorem for a spread can force a characteristic-two fiber. Nor does a finite-type coefficient ring supply a map to Z_(2) or Z_2: coefficient fields, transcendental parameters, residue fields, and possible ramification all matter.

### Direct reduction to Z4 is numerically impossible for a surviving pair

By R0001 and its accepted lower-degree/factor consequences, d,e are at least five; by (2), four divides de. The smallest possible product is 36, from (6,6), so

\[
m\ge9.
\tag{17}
\]

The prescribed Z4 has degree 16 and generic multiplicity four. A flat complete-intersection family of degrees (d,e) specializing to it must satisfy equality of (16) with 16n-32. This forces de=16 and d+e=8, hence d=e=4. Thus the **whole** intersection scheme of a hypothetical surviving STCI pair cannot specialize flatly to Z4. This degree obstruction is independent of its arithmetic nonlifting.

Extracting a degree-16 intermediate structure would avoid that particular degree mismatch, but requires a global primitive fourth stage, a compatible integral extension of that stage, and the exact marked special fiber. None is forced by an arbitrary STCI. Counterexample C shows why generic primitive stages are not enough.

### Conditional arithmetic corollary — proved under explicit model hypotheses

Suppose a hypothetical characteristic-zero pair admits a model over R=Z_(2) or Z_2, in the fixed relative quartic embedding, such that the total support is C_R, the family is flat, its first-normal image is a line subbundle at every point of C_R, its generic multiplicity is at least three, and its induced quotient reduces to the distinguished q0 of the marked arithmetic problem. Then this model cannot exist.

Indeed Proposition B gives a relative primitive triple. Its canonical extension (1) must split over R. The audited full admissible-quotient calculation gives middle coefficient 2 modulo 4 for every integral quotient reducing to q0, contradicting such a splitting. This rules out a particular kind of *good marked reduction*, for any multiplicity at least three. It does not assert that a hypothetical characteristic-zero STCI must possess such a model. For a total special fiber equal to prescribed Z4, the independently stronger full nonlifting statement is precisely the promoted R0012, with its two-DVR limitation.

Flatness cannot be omitted in descent arguments. Over a DVR, generic containments extend to the total scheme when the target quotients O_Z and O_C are torsionfree, but quotient flatness is what also identifies the base-changed ideal with the actual special-fiber ideal via Tor vanishing. An ideal itself is torsionfree without its quotient being flat: (2x,x²) in Z_2[x] is an elementary counterexample.

## 6. Outcome, audit boundary, and the next mathematical target

**Proved in this report:** the defect-twisted necessary condition (6); the q0 common-zero divisor restriction (9) and its exact degree-two incidence; automatic first-stage vanishing for epsilon at least two; the all-points sufficient bridge to a triple contained in Z; the projective integral-surface counterexample to generic globalization; and the support-preserving spreading/degree statements.

**Conditional:** the arithmetic exclusion of an everywhere rank-one model over either exact unramified base with the specified marked ribbon reduction. It uses the audited relative coefficient calculation and supplies no such model for an arbitrary characteristic-zero pair.

**Open:** whether the actual homogeneous surface symbols of any surviving pair force a direction and divisor violating (6); whether C0-specific geometry forces stronger global intermediate stages despite Counterexample C; all entirely-thick interfaces not covered by existing scoped results; and the unrestricted characteristic-zero STCI question. No new unconditional carrier-degree exclusion is claimed.

The most focused next step on the order-one branch is to impose (6) on the *actual first-normal symbols* (5), together with their global lift conditions, rather than classify arbitrary ribbons. For epsilon=1 this is a finite-dimensional incidence between the quotient q, the common-zero divisor D of those symbols, and the Serre-dual functional (11). A proof that all actual surviving pairs violate that incidence would be an exclusion. The present report establishes the incidence as necessary and gives one exact restricted-direction obstruction; it does not establish the missing actual-pair classification. For epsilon at least two, the first Yoneda stage is identically insufficient, so a later-stage or independent geometric condition is required.

Independent checks were supplied during this investigation by the structural-audit worker for Propositions A/B, the projective counterexample, and the q0 Serre-dual bound; a separate spreading-audit worker reconstructed Proposition D and checked the fiberwise flatness reference. These checks do not promote the report. The independent audit's stable path should be consulted when attached by the coordinating report.

Reproducible calculation:

```text
python3 research/computations/verify_z4_stci_consequences_2026_10_21.py
```

This standard-library script checks the exact q0/q1 cubic values, the evaluation-conic determinant, obstruction-group dimensions, the integral-quadric ideal identities and ranks, nilpotence in the degeneration example, and the finite minimum/CI Hilbert-polynomial arithmetic. The geometric proofs above carry the global statements; a script PASS is not a substitute for them.
