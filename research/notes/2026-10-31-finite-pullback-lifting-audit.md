# Independent audit: finite pullback and polarization lifting

Date: 2026-10-31. Reviewer: the fresh `gpt-6.1-sol/high`
`finite_pullback_picard_review` worker, independently reconstructing the
argument. No nested delegation or numerical computation. Status:
**reviewed provisional mathematics; no canonical promotion**.

Reviewed artifact: [the preserved finite-pullback note](2026-10-31-finite-pullback-lifting.md),
particularly §§2–5 and the construction-source disposition in §6.
The final bounded check also covers the corresponding finite-pullback
summary, displayed bundle deduction and stopping recommendation in
[strategy assessment §11](2026-10-31-unrestricted-strategy-assessment.md#11-constructive-selection-finite-pullbacks-and-controlled-bundle-degeneration).
Secondary bounded source check: Forster–Wolffhardt Theorem 1.5 and the
conditional projective determinant deduction described below. The audit
does not review a general bundle-construction program or Ferrand's proof.

## Exact outcome and scope

**PASS.** Let k be algebraically closed with characteristic different
from three, let T be a twisted cubic in projective three-space, and let
C be a smooth rational space curve of degree prime to three. There is
no finite endomorphism Phi of projective three-space with full scheme
inverse image W of T satisfying W_red=C. This includes
C0=[s^4:s^3t:st^3:t^4], in every polarization degree d.

The proof also verifies the note's abstract section-lifting principle:
the restriction of the ambient morphism must factor **scheme-theoretically**
through the rational normal curve, and all its stated Picard, unit,
lifting and absence-of-equations hypotheses must hold. The rational
normal curve corollary holds for Gamma_N in P^N, N>=2, when N is
invertible in k and the reduced inverse image is **smooth rational**.
It excludes N|d; coprimality of the reduced curve's degree with N is a
sufficient condition forcing that divisibility.

The reviewer requested two small scope clarifications in the preserved
draft: retain “smooth rational” explicitly in the coprime-degree
corollary, and make the scheme-theoretic factorization in the abstract
lemma explicit. **Both are resolved in the checked final wording**:
§3 states scheme-theoretic factorization, and §5 explicitly retains
smooth rationality in the coprime-degree consequence. These clarify the
proved statement rather than impose new hypotheses on the finite-pullback
theorem. No substantive proof repair or failed mathematical condition
remains.

## Independent reconstruction and challenges

1. **Full inverse image and flatness.** A finite map between the smooth
   equidimensional projective spaces is flat. Its pullback of the ideal
   resolution of T is therefore the ideal-sheaf resolution of the full
   W, not merely of its reduction:
   `0 -> O(-3d)^2 -> O(-2d)^3 -> I_W -> 0`.
   Line-bundle cohomology on P^3 gives H^1(I_W(t))=0 for every t,
   H^0(I_W(d))=0, and H^0(O_W)=k. No primitive multiple-curve,
   normal-flatness, or local classification assumption has entered.

2. **The nilpotent Picard kernel is controlled.** For the nilradical J,
   the exact unit-sheaf sequence identifies its H^1(1+J) with the kernel
   of Pic(W)->Pic(P^1). The possible obstruction to this identification
   would be the boundary of a global unit on P^1. That boundary is zero
   because every such unit is a scalar and lifts to W. This checks the
   point where a quotient of a torsion-free group could otherwise
   acquire torsion.

3. **The characteristic refinement is valid.** If N is invertible,
   raising to N is an automorphism of 1+J: on the finite filtration
   quotients `(1+J^r)/(1+J^(r+1)) = J^r/J^(r+1)` it is multiplication
   by N. It therefore acts invertibly on H^1(1+J). Together with
   Pic(P^1)[N]=0, this proves Pic(W)[N]=0. The positive-characteristic
   assertion is only this prime-to-characteristic torsion vanishing;
   full torsion-freeness is not being inferred. In characteristic zero
   the logarithm gives the stronger torsion-free statement.

4. **Root and coordinate compatibility.** The pulled-back pencil L
   has L^3=O_W(d). The degree identity 3e=cd forces 3|d for the stated
   c, and Pic(W)[3]=0 forces L=O_W(d/3). The two identifications after
   taking the cube differ by a single global unit. H^0(O_W)=k makes
   this a scalar, not a nonconstant nilpotent unit. Arbitrary independent
   coordinate scalars are not being assumed or needed.

5. **Global lifting really produces a contradiction.** The two pencil
   sections lift to degree-d/3 forms A,B. The degree-d coordinate
   differences vanish globally since H^0(I_W(d))=0. The original map's
   forms are consequently a common scalar times A^3,A^2B,AB^2,B^3.
   Two positive-degree forms have a common zero in projective space
   of dimension at least two; thus these forms cannot define a
   morphism there. This is a global argument on the full W, not a
   generic-field or formal-neighborhood conclusion.

6. **The extra multiplicity calculation is correct but unnecessary.**
   For C0, the identities 3e=4d, 4n=3d^2 and en=d^3 imply 6|d.
   They give (e,n)=(8,27) at d=6. The contradiction uses only 3|d,
   so no numerical search, generic-length hypothesis beyond the
   full inverse image, or uncompleted degree-six computation supports
   the theorem.

7. **The rational normal generalization has the required cohomology.**
   Its characteristic-independent linear resolution has twists
   -2 through -N. Flat pullback scales the twists by d. Vanishing
   of intermediate line-bundle cohomology on P^N, including the
   hypersurface case N=2, gives the stated section lifting and
   absence of degree-d equations. The same N-th-root proof applies.
   The qualifier N>=2 excludes a dimension-one noncontradiction.

## Geometric interpretation and unrestricted boundary

The object being measured is the full finite-flat inverse-image curve,
including its nilpotent transverse structure. Its map to P^1 supplies
a root of the ambient polarization. Rational support and prime-to-
characteristic Picard rigidity force that root to be an ambient twist.
ACM cohomology then extends the associated pencil, and the absence of
correction equations prevents the coordinate map from leaving the
Veronese image globally. This explains both the source exclusion and
the reusable principle; multiplicity arithmetic alone is not the
mechanism.

The characteristic-two control is sound. The inherited quartics
`x1^4-x0^3*x3` and `x2^4-x0*x3^3` have radical I_C0 in characteristic
two: on x0=1 they give x3=x1^4 and `(x2-x1^3)^4=0`; at x0=0 only
the endpoint [0:0:0:1] remains. The prescribed pair is also the input
of [R-0031](../results/quartic_char2_fourth_equation_kernel.md).
The finite-twisted-cubic exclusion holds in that same characteristic.
Hence this construction source is demonstrably nonexhaustive even
where C0 is STCI. No conclusion about arbitrary characteristic-zero
pairs follows without a further exhaustive reduction, and none has
been supplied.

## Primary-source and secondary-premise checks

- [Poonen, Theorem 2.2](https://math.mit.edu/~poonen/papers/selfmap.pdf)
  concerns sufficiently high polarization for a fixed closed subscheme.
  It imposes no sole-inverse-support condition. It therefore neither
  supplies the desired W nor contradicts the no-correction argument.
- [Jamet, §1](https://arxiv.org/pdf/math/0103202) supplies the complex
  finite-flat inverse-image and direct-image framework. The current
  prime-to-characteristic extension is justified by the direct proofs
  above, rather than an unstated extension of Jamet's field hypotheses.
- [Forster–Wolffhardt, Theorem 1.5 and Proposition 1.6](https://www.math.lmu.de/~forster/eprints/zeroschemes.pdf)
  have the claimed **affine** scope. For a rank-two bundle E and section
  s with zero scheme Z, det(E)|Z trivial permits sections satisfying
  `psi(s)+lambda*h=1`. Their map
  `Phi=psi tensor psi+i(lambda)` has determinant lambda^2, and the
  resulting dual section has exactly the same zero scheme. The proof
  uses the affine lifts and splitting implicit in this identity; it
  does not establish a projective version. Independently, on P^3,
  det(E)=O(c) trivial on Z with Z_red=C0 forces 4c=0 by restriction
  to C0. Thus c=0 and the rank-two wedge isomorphism gives E*=E.
  Dualization under that hypothesis alone supplies no splitting
  of E into line bundles and no projective split target.

These checks establish source scope, not publication novelty. No
novelty claim is supported or made. The limited Forster–Wolffhardt
deduction is not a review of all possible bundle manipulations.

The checked strategy-assessment §11 preserves this scope: it reports the
single bounded verification and stop rule, all-degree source exclusion,
prime-to-characteristic root mechanism, characteristic-two nonexhaustivity,
and the absence of an unrestricted STCI reduction. Its Forster–Wolffhardt
paragraph keeps the affine hypothesis, exact-zero preservation and
conditional projective self-duality separate from the missing split target.
Its recommendation stops both the finite-twisted-cubic source and the bare
transplant without requiring an unproved future mechanism to succeed in
advance. These statements align with this review. The separate remarks on
Ferrand and inspected monad descriptions remain covered by the source
worker's evidence, not an additional proof review in this audit.

## Disposition

The approved bounded verification is complete. Retain the all-degree
finite-source exclusion, abstract lifting principle, characteristic
qualification and nonexhaustivity example. Stop this construction
source: no degree-six search, adjacent target enumeration, or further
bundle campaign is justified by this audit. The unrestricted
characteristic-zero STCI question remains open. No inherited proof
script was rerun and no canonical result was promoted.
