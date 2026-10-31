# Full formal geometry, fixed twists, and finite jets

Fix the embedded C=C0 over an algebraically closed field. Let Y be an actual proper pair of degrees a,b, with [Y]=m[C]+R. These are reviewed provisional deductions and standard formal-Lefschetz applications, not an STCI existence result. The full completed ideal, its generic transverse algebra, and two globally glued fixed-twist equations contain different information.

## What full formal geometry detects and extends

## 2. The answer already partly exists in the repository

The point-contact proof gives

    R is nonzero iff there is p in C with e_p(Y)>m.

Here e_p is Hilbert–Samuel multiplicity, computed with a general local linear slice. Associativity gives

    e_p(Y)=m+sum_(D != C, p in D) m_D e_p(D).

Proper projective complete-intersection curves are connected, including nonreduced ones: their Koszul resolution gives H^0(O_Y)=k. Thus a nonempty union of residual components must meet C somewhere. This is an exact recognition criterion, not a proof that such a point always exists. It works in arbitrary characteristic under the same geometric hypotheses.

Consequently the **full embedded completion along C does detect whether any residual component exists**, for an actual proper projective CI Y. Completed local rings preserve the slice lengths and multiplicities. There is no reason to expect this detector to be positive for every characteristic-zero pair without a new theorem.

Two cautions sharpen its meaning. Connectedness says the union of residual components meets C; it does not say every individual residual component does. A component can connect to C through other residual components. Also, the criterion controls support, not the nilpotent structure of a multiple curve supported on C.

Primary foundations refreshed on 2026-10-27: [Stacks 02QG](https://stacks.math.columbia.edu/tag/02QG) for the componentwise slice-length formula, [Stacks 01XS](https://stacks.math.columbia.edu/tag/01XS) for the cohomology input. These standard facts and the recognition criterion are inherited here, not new discoveries.

## 3. Generic transverse information loses attached residual branches

At the generic point of C, the completed normal ring is K[[x,y]], K=k(C). It gives m and hence deg R=ab-4m when the actual degrees are known. It does not locate the attachments or recover residual geometry.

An elementary local comparison makes the loss explicit. In k[[t,x,y]], mark C=(x,y) and compare

    J0=(x,y^m),
    J1=(x,y^m(t-y)).

After passing to k((t))[[x,y]], t-y is a unit, so both generic transverse quotients are k((t))[y]/(y^m). At the closed point t=x=y=0, J1 has the extra smooth residual branch x=0,t=y, while J0 has only the marked support. Their point multiplicities are m+1 and m, respectively. The full completed local ideals distinguish them immediately.

This is a local explanatory model, not a claimed homogeneous realization on the fixed quartic. Its role is to rule out the inference that a pure-power generic normal algebra excludes attached residual support.

## 4. Saturation extracts residual germs; linkage requires a different choice

Let A be the completed local ambient ring at p in C, let I be the ideal of the marked curve, and let J=(F,G)A. The ideal

    J:I^infinity = union_n (J:I^n)

removes the I-primary component and retains the residual primary components through p. To see this, use a primary decomposition of J. A power of I is contained in the C-primary factor, so saturation removes it; for any other primary factor Q, some element of I lies outside sqrt(Q), and multiplication by that element does not enlarge Q. Noetherianity makes the union stabilize. This extracts attached residual germs with their scheme structure; it does not manufacture a residual component from vertical exceptional geometry.

A single colon J:I, used for linkage to the reduced C, is a different operation. If m>1, the linked scheme can still contain C, with one layer removed generically. Nor does subtracting m[C] from a cycle specify a canonical embedded multiple structure on C to which one can link. Record the selected multiple structure before discussing a scheme-theoretic residual of degree ab-4m.

Completion is flat and exact for finite modules, and is faithfully flat at a local stalk with ideal of completion inside its maximal ideal: [Stacks 00MB](https://stacks.math.columbia.edu/tag/00MB), [00MC](https://stacks.math.columbia.edu/tag/00MC). Thus these ideal calculations can be compared to their algebraic stalks. The saturation statement is elementary local algebra; it is not asserted to be new.

## 5. Full formal geometry can carry global information: the G3 qualification

It would be too strong to say that a formal neighborhood intrinsically has no global information. For a connected positive-dimensional closed subvariety C of projective space over an algebraically closed field, Hironaka–Matsumura prove

    K(P3) = K(formal completion of P3 along C).

This is the G3 property. The original paper is [Hironaka–Matsumura, Formal functions and formal embeddings, JMSJ 20 (1968), 52–82](https://doi.org/10.2969/jmsj/02010052), Theorem (3.3). The original publisher metadata was inspected; its PDF endpoint failed during this check. The theorem and its relation to the Lefschetz condition were checked in the primary account [Hartshorne, Cohomology of non-complete algebraic varieties (1971), section 1, especially Proposition 1.2 and the ensuing projective-space statement](https://www.numdam.org/article/CM_1971__23_3_257_0.pdf). No claim is made to have reread the original HM proof in this session.

For our purposes a useful consequence is the following **section-extension fact**:

    H^0(P3,O(d)) -> H^0(formal completion along C, completed O(d))

is an isomorphism for every integer d.

Here is a reconstruction of the consequence, with its hypotheses visible. Divide a formal section by any nonzero rational section of O(d). This gives a formal rational function, so G3 identifies it with a rational function on P3. Thus the formal section is the completion of a rational section of O(d). At every p in C it is formally regular. Faithful flatness of local completion then implies ordinary regularity: if a/b becomes regular after completion, a belongs to b times the completion, hence to bA by contraction. Its polar divisor therefore avoids C. Every nonempty hypersurface in P3 meets the positive-dimensional projective curve C. A rational section on the smooth P3 with no polar divisor is global. Uniqueness follows from local injectivity, or from the same rational-function identification.

This does **not** say that a pair of arbitrary local formal generators algebraizes into homogeneous equations of chosen degrees. They must already glue as global sections of the *specified ambient twists*. A formal ideal or an abstract multiple curve does not supply that presentation. It also does not say that finite jets lift to all orders.

A current literature cross-check supports exactly this separation. [Halic, G3-criteria and applications, published 2026; arXiv v4, section 4, proof of Theorem 4.4](https://arxiv.org/html/2401.16196v4#S4) explicitly extends conormal sections first to formal sections and then, using G3/Lefschetz and absence of divisors in the complement, to global sections. This is a useful methodological connection, not a theorem applicable wholesale to C: section 4 assumes ambient dimension at least four, and its split conormal summands come from ambient line bundles. Our characteristic-zero summands O_P1(-7) do not come from O_P3(-d), whose restrictions have degree -4d. The article therefore supplies neither a CI construction nor an STCI exclusion for this quartic. Its lifting step depends on vanishing hypotheses absent in the curve setting. The exact current version was checked rather than relying on an older abstract.

A further distinction concerns an embedded formal ideal versus a marked pair of equations. A component disjoint from C contributes no local germ to completion along C; completion of its structure sheaf is zero. A globally glued formal equation, in contrast, determines its global homogeneous equation by the section-extension fact, and that equation can then be analyzed away from C. Discarding the equations and retaining only the quotient ideal can discard useful global presentation information. This note does not assert uniqueness of a global CI from its unlabelled completed ideal, nor a counterexample to such uniqueness within a particular fixed-degree CI family.

## 6. An exact construction-oriented reformulation

Fix positive integers a,b. The following two assertions are equivalent:

1. There are actual homogeneous F_a,G_b with reduced intersection C.
2. On the formal completion of P3 along C there are globally glued sections Fhat of completed O(a), Ghat of completed O(b), such that

       I_C^N subset (Fhat,Ghat) subset I_C

   for some N, as ideal sheaves on the formal completion.

The inclusion means uniform nilpotence of the marked ideal in the formal quotient. Merely saying its formal topological support is C is insufficient: the underlying topological space of the completion is already C even when residual branches pass through it.

Proof of 1 -> 2: the global radical equality gives a power containment by Noetherianity; complete the two equations.

Proof of 2 -> 1: section extension uniquely gives global F,G vanishing on C. They cannot have a common surface component H. Such a surface meets C, and at a point of intersection the power containment, faithful flatness, and contraction would give I_C^N subset (H) in the local ambient ring. This would put the local surface inside the local curve, contradicting dimension. Thus Y=V(F,G) is a proper CI. The power containment rules out any residual component meeting C. If residual components existed, their union would be disjoint from C; connectedness of Y rules that out. Hence its reduced support is C.

This is an exact reformulation using a classical extension theorem and standard connectedness. It is **not** an existence result, a finite construction algorithm, or a claim that local equations can always be made into fixed-twist global sections. Its strategic value is to locate the remaining difficulty precisely: produce the two globally compatible twisted formal sections and the uniform nilpotence condition. There is no additional mysterious algebraization gap after those exact data have been produced.

## 7. What finite jets can and cannot do

Write C_n=V(I_C^(n+1)). A section on C_n lifts to C_(n+1) only if its connecting class in

    H^1(C, Sym^(n+1)(E) tensor O_C(d))

vanishes, where E=I_C/I_C^2. This follows from the short exact sequence of consecutive neighborhoods. Even when a lift exists it need not be unique. Arbitrary K-linear normal symbols and compatible local equations do not solve this global obstruction problem.

R-0020 gives E=O_P1(-7)^2 in characteristic different from two. A nonzero global or global formal section of O(d) cannot vanish to normal order r>4d/7: its first nonzero symbol would belong to

    H^0(P1, O(4d-7r)^(r+1))=0.

If all symbols vanish, separatedness gives the zero section. Therefore restriction of such sections to C_n is injective for n=floor(4d/7), d>=0. In characteristic two the splitting O(-8)+O(-6) yields the analogous sufficient injectivity index n=floor(2d/3). These are direct fixed-degree consequences of the accepted conormal splitting, not fresh computations.

Injectivity is uniqueness, not surjectivity: a finite jet can fail to extend. A concrete control is d=1, where n=0 already gives injectivity, but the global linear forms restrict to the four-dimensional span of s^4,s^3t,st^3,t^4 inside H^0(P1,O(4)). The missing section s^2t^2 is a valid section on C which cannot extend through all infinitesimal neighborhoods as a section of the ambient O(1). The section-extension fact identifies the jets which extend to all orders with the image of the actual global homogeneous coefficient space. It is therefore reasonable to compute those exact images when choosing construction candidates, instead of first allowing arbitrary function-field coefficients and hoping to descend them later.

The inherited fixed-degree generic-length criterion can recognize a genuine pair exhausting its degree budget, but it supplies no degree bound for all possible pairs. The formal reformulation above supplies no such bound either.



## Verified extension input

[Hartshorne, section 1](https://www.numdam.org/article/CM_1971__23_3_257_0.pdf), freshly checked in this consolidation, states both the projective-space G3 theorem and its relation to the Lefschetz condition. Thus formal fixed-twist sections extend to a neighborhood, whose complement contains no divisor since every hypersurface meets C; normal Hartogs extension makes them global. This is a second route to section extension, independently of the rational-section reconstruction above. The original HM PDF was not freshly inspected. No finite jet, unlabelled ideal, or generic normal algebra is substituted for the globally glued pair.


## Characteristic reach and limitation

Connectedness, completion and saturation, the multiplicity detector,
Nakayama finite-length argument, and projective-space G3/Lefschetz section
extension have the stated arbitrary-characteristic hypotheses. The finite-jet
injectivity index uses the characteristic-dependent conormal splitting:
floor(4d/7) away from two and floor(2d/3) in characteristic two. Neither is a
surjectivity claim. The exact formal reformulation is compatible with actual
[quartic-carrier solutions in every positive characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
