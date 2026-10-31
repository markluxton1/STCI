# Independent audit of the foliation and affine-degree selection

Date: 2026-10-31. Reviewer: fresh `gpt-6.1-sol/high` worker, without
nested delegation. **Disposition: the scoped deductions and stopping
recommendation are supported.** They remain provisional and do not settle
the unrestricted characteristic-zero STCI question.

## Reviewed state and boundaries

This audit covers Sections 1–5 of
[the foliation/affine selection note](2026-10-31-foliation-affine-selection.md)
and the corresponding recommendation in
[the unrestricted assessment, Section 10](2026-10-31-unrestricted-strategy-assessment.md#10-arbitrary-pair-selection-foliation-and-affine-boundary-losses),
as read after integration of the three foliation deductions and the
reduced affine control. Later review-status and navigation edits do not
change the mathematical state covered here.

The curve is exactly
`C=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of characteristic
zero. Homogeneous hypothetical pairs are proper with sole reduced support
C and arbitrary degrees. The affine argument permits every polynomial
pair with radical the indicated graph ideal, including nonreduced
structures of arbitrary generic length. No reduction to coordinate pairs,
normal-flat structures or a chosen local singularity type is used.

I followed INDEX and MAP, then checked the relevant affine-endpoint,
weighted-initial, Jacobian/contact and Hamiltonian notes. Their existing
proofs and certificates were reused as inherited evidence; they were not
rerun. I checked the primary source statements identified below and
independently reconstructed the new elementary arguments. No numerical
experiment, exhaustive classification or canonical promotion was performed.

## Foliation deductions

1. **Normalization and singular support.** Euler contraction of
   `bG dF-aF dG` is zero, its coefficient degree is `a+b-1`, and removing
   a homogeneous coefficient gcd D gives normal determinant
   `O(e)`, `e=a+b-deg D`. The normalized form still vanishes on C.
   Over the complex numbers, regularity at a base point would make the
   meromorphic first integral `F^b/G^a` a meromorphic germ in one Frobenius
   transverse coordinate. Its zero and pole divisors cannot both pass
   through that point while remaining coprime. This contradicts the local
   height-two condition. The vanishing assertion is algebraic and passes
   through a finitely generated field of definition and faithful base
   change to the stated characteristic-zero scope.

2. **Raw differential versus normalized differential.** Direct
   differentiation gives `dω0=-(a+b)dF∧dG`. At the generic transverse
   regular local ring, independence of the linear parts of F,G would give
   colength one. Thus generic length greater than one makes this wedge
   vanish on reduced C. If D is generically a unit on C, both the form
   and its differential vanish there; regularity extends that vanishing
   across all C. This argument does not cover D vanishing identically on
   C. Normalization can change the transverse differential in that branch.

3. **The smooth-curve zero-divisor dichotomy.** Since the normalized form
   vanishes on C, its differential restricts independently of the local
   trivialization. If the restriction is nonzero, its nonvanishing open
   set is Kupka. There its two-form lies in `det N_C^*`, because the smooth
   Kupka locus has tangent line TC. The quotient of this conormal line
   subbundle inside the restricted two-form bundle is locally free;
   hence membership extends across the finitely many omitted points.
   Now `deg det N_C=16-2=14`, while the ambient twist `O(e)|C` has degree
   `4e`. The resulting nonzero line-bundle section has zero divisor of
   degree `4e-14`. Its nonnegative degree forces integer `e>=4`, and
   its degree is then positive. This direct argument remains valid when
   other singular curves meet C. It supplies no finite divisor when the
   restricted two-form is identically zero.

   [Calvo-Andrade–Corrêa–Fernández-Pérez, Theorem 2](https://arxiv.org/pdf/1506.05438)
   separately requires a connected lci singular component with a finite
   non-Kupka complement. The note correctly distinguishes that published
   scope from the direct smooth-curve extension just reviewed. The
   entirely non-Kupka branch does not meet its finite-divisor premise.

4. **The D=1 residue specialization.** Off C, either F or G is a unit.
   On a small complex neighborhood with G nonzero, choose its fractional
   power and write `ω0=bG^(1+a/b)d(FG^(-a/b))`. The multiplying function
   is a unit. On a generic transverse two-disc to an off-C singular curve,
   the exact form `dh` has tangent Hamiltonian vector field
   `(h_v,-h_u)`, whose divergence vanishes identically. Its `c1^2`
   Grothendieck residue is therefore zero.
   [Corrêa–Lourenço, Theorems 1.1–1.2](https://arxiv.org/pdf/1612.05787)
   supports the global localization and the transverse residue computation
   without the older Baum–Bott genericity condition. Thus every off-C
   curve contribution vanishes in this specialization and
   `BB(C)=(a+b)^2/4`. The nonzero residue is compatible with pointwise
   vanishing of the two-form on reduced C.

   I explicitly challenged extension of this argument to an arbitrary
   holomorphic first integral after saturation. It fails: `h=x*y^2`
   has primitive form `y dx+2x dy`, whose transverse vector field has
   eigenvalues 2 and -1 and nonzero residue. A first integral alone is
   weaker than the unit-times-exact premise. The final note retains that
   distinction and does not discard the other curve contributions for
   arbitrary D.

5. **Scheme and classical Kupka loci.**
   [Massri–Molinuevo–Quallbrunn, Section 4](https://arxiv.org/pdf/1509.07231)
   defines the coefficient-ideal quotient and supplies radical/generic
   hypotheses for the relevant identifications. Its examples distinguish
   the scheme support from the closure of classical Kupka points without
   those hypotheses. The note does not infer a classical Kupka open set
   from a nonzero ideal-quotient scheme.

Geometrically these deductions concern the actual transverse foliation
of a thick pencil base. They isolate a finite degeneracy divisor only in
the generically Kupka alternative and a localized transverse residue in
the D=1 alternative. Neither condition excludes a supported thick base.

## Affine deductions and source applications

The triangular coordinates have inverse `y=Y+z^3`,
`w=W+zY+z^4`. A linear form with nonzero w coefficient restricts to a
degree-four polynomial on C. The reduced coordinate ring is finite over
`k[ℓ]`; lifting monic integral equations through the nilpotent ideal
establishes finiteness of B. The height-two two-generator ideal is a
complete intersection, hence B is Cohen–Macaulay and has no associated
prime other than its integral support. Every nonzero polynomial in ℓ is
therefore a nonzerodivisor. Finite torsion-free modules over `k[ℓ]` are
free, and the generic-length calculation gives rank `4m`.

A finite nonempty fiber of H has local dimension zero. The local
dimension inequality forces H to be dominant, hence generically finite.
Conservation of isolated intersection multiplicities gives `4m<=μ`;
ordinary affine Bézout gives `μ<=ab`. The two nonnegative losses in
`ab-4m=(ab-μ)+(μ-4m)` consequently have the stated meanings. For the
ordinary homogenizations, their sum is exactly the residual cycle degree
at infinity. The same proof for an integral degree-d affine curve and
a general linear projection gives `dm<=μ<=ab`; it is not peculiar to
this quartic or characteristic zero.

I supplied the reduced pair `f=Y,g=W` as a direct challenge to any
finiteness-based existence inference. Substitution makes ℓ a quartic in
z over `k[f,g]` with constant nonzero leading coefficient. Thus H is
finite of degree four, although `ab=6` and `m=1`. The losses are exactly
2 and 0. The common leading-form line is the projective residual support.
This control lies inside the actual quartic class under discussion.

- [Jelonek, Proposition 6 and Theorem 15](https://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf)
  were checked in full text. Their finite-fiber multiplicity criterion and
  nonproperness degree bound specialize to the stated H and `ab-μ`.
  They make `ab=4m` imply finiteness but do not establish its converse.
- [Mondal, Theorem 3.1 and Example 3.4](https://arxiv.org/pdf/1111.0614)
  distinguish the general sufficient equality statement from the explicit
  weighted-degree biconditional. Ordinary degree is its all-weights-one
  case. For general ℓ, a line avoids the finite intersection of coprime
  leading plane forms but necessarily meets any common curve. Thus the
  ordinary equality criterion is the inherited projective boundary test;
  a changed completion does not establish equality for this embedding.
- [Vénéreau, Definition and Properties preceding the main theorem](https://arxiv.org/pdf/0704.1561)
  supplies the displayed derivative estimate for an element `R(f,g)` of
  the subalgebra. H's dominance also ensures algebraic independence of
  f,g. Neither ideal power containment with ambient coefficients nor the
  inherited contact identity provides the required subalgebra membership.

## Independent strategy challenge and disposition

I tested whether the recommendation merely follows producer agreement,
whether the finite-map reformulation adds a sufficient construction, and
whether the stopping rule could disallow a legitimate existence experiment.
The exact reduced-pair control defeats the proposed finiteness shortcut;
the source hypotheses and the entirely non-Kupka alternative defeat a bare
finite-divisor application. The new residue specialization remains an
equality, with no incompatible quartic-specific comparison established.
These are reasons to stop the bare applications, not to retire either
mathematical subject.

Section 5 and assessment Section 10 correctly allow a specified unproved
mechanism to be tested without requiring proof of prospective success.
An existence experiment may use a restricted source if it has an actual
sufficient global construction step; only an unrestricted exclusion needs
coverage of every hypothetical pair. Missing prerequisites can themselves
be a bounded research target. The stop applies when the proposed
application lacks its premise, merely recovers an existing budget or
extends case enumeration without a new comparison. It does not turn lack
of a contradiction into evidence against existence.

**No unresolved material correction was found in the integrated version.**
The review establishes the scope and elementary deductions above, not
classification of D, a general residue inequality, subalgebra membership,
an affine equality construction or a homogeneous defining pair. C being
STCI remains a live possibility, and no next campaign or canonical change
is authorized by this audit.
