# Independent audit: residual equation recovery and deformation space

Date: 2026-10-28. Reviewer: root integration agent. Source:
[residual liaison construction](2026-10-28-residual-liaison-construction.md).
**Outcome: fixed-pair claims, relative-family §2.1 and Artinian recovery in
§5 pass independent reconstruction in their stated scope. No canonical
promotion.**

## Scope and inherited premises

The curve is the fixed smooth rational quartic in characteristic zero,
the pair is proper, and \(4\le a\le b\). The source's \(D\) means the
once-linked curve \((F,G):I_C\), including when it still contains \(C\).
It does not mean removal of the full primary component. The inherited Rao
module calculation is used as a premise; the accepted conormal calculation
and inherited smooth-residual certificates were not rerun.

## Reconstruction of the equation and resolution assertions

1. Linkage gives \(I_D/I_Y=\omega_C(4-a-b)\) as sheaves. The complete
   intersection Koszul resolution makes \(H^1(I_Y(n))=0\) for all twists.
   Thus this quotient can be taken on graded global sections, with no
   hidden failure of surjectivity. Since \(\omega_C(n+4-a-b)\) has
   degree \(4n+14-4(a+b)\), it has no sections through degree \(a+b-4\).
   Both defining degrees are in that range. The recovered ideal generated
   through degree \(b\) is exactly \(I_Y\), with the correct mixed-degree
   redundancy. This argument uses the embedded residual, not its invariants.

2. I independently checked the displayed canonical-module matrices. Every
   column of \(M\) annihilates \((s^2,st,t^2)\) under the curve's
   parametrization; multiplying \(M N\) gives zero. The first column of
   \(N\) has no common projective zero. On \(x_0\ne0\), proportionality
   of its two columns forces the quadric and the cubic
   \(x_0^2x_2-x_1^3\); the other endpoint chart and
   \(x_0=x_3=0\) give precisely the claimed rank-drop support. The
   maximal minors of \(N\) therefore have height two. The matrix \(M\)
   has rank three, so the rank-and-grade criterion applies. Products of
   \(s^2,st,t^2\) with the coordinate monomials fill every exponent of
   degree \(4n-2\); the numerator gives the same Hilbert function. This
   identifies the module, rather than just giving a complex with the right
   ranks.

3. The horseshoe construction has last summands in degrees \(a+b-1,a+b\)
   and an additional degree-\(a+b\) summand one step earlier. The latter
   must cancel: local duality identifies the minimal generators of the
   dual last cokernel with those of the dual Rao module. The latter has
   exactly one generator, corresponding to degree \(a+b-1\). The
   remaining degrees of all differential entries are positive for
   \(a,b\ge4\). Thus no dependence on a generality assumption or a
   sampled matrix remains in the proposed minimal resolution.

The five new finite-field controls are correctly described as corroboration,
not as a characteristic-zero existence or smoothness certificate. Their
new script tests actual colon ideals, properness, degrees, genera and all
resolution shifts; it does not replay an accepted proof.

## Primary literature and deformation claims

I opened [Kleppe's original paper](https://www.numdam.org/article/AIF_2006__56_5_1297_0.pdf)
and checked Theorem 1.3, Proposition 1.4 and its terminology. The paper's
curves are locally Cohen–Macaulay and its field has characteristic zero.
Its obstruction products vanish for the source's resolution. Its extra
condition in Proposition 1.4 is also satisfied: the Rao module is supported
in degree \(a+b-5\ge3\). Its conclusions therefore justify smoothness and
the stated difference between the two deformation-space dimensions. The
source applies existing results; no new unobstructedness theorem is claimed.

For the dimension calculation I independently used the opposite linkage
sequence to compute
\(h^1(O_D(n))=h^0((I_C/I_Y)(a+b-4-n))\). All the syzygy and three
additional generator degrees have zero in this group. At the two carrier
degrees the answer is
\(v_{b-4}-s_{b-a-4}\) and \(v_{a-4}\). The subtraction occurs because
only multiples of the smaller defining equation can occur in degree
\(b-4\). This verifies the mixed-degree term, including arbitrarily
unequal degrees. Elementary binomial expansion then gives the difference
from the varying-partner incidence dimension claimed in the source.

The table is consistent with those formulas: the quintic-quintic family
has dimension 82 when its linked quartic can move, inside a smooth
84-dimensional residual Hilbert neighborhood. The two extra directions
change postulation. They do not belong to the original fixed-equation
incidence problem.

## Family/recovery boundary

Low-equation recovery over an Artinian base requires the graded pieces to
remain flat, as they do in the fixed-postulation functor. It is not an
assertion about arbitrary Hilbert deformations. Properness of the recovered
pair is open, and relative complete-intersection linkage then recovers a
flat linked quartic. Smooth embedded rational quartics form an open
neighborhood of the given partner. This supplies a local inverse on the
postulation stratum, rather than just a pointwise dimension comparison.

I separately reviewed the completed relative addendum, §2.1. Fiberwise
properness makes the relative equations a regular sequence and their
Koszul quotient flat. Both embeddings in the ambient projective space
have codimension two. Change of rings identifies the annihilator
\(\operatorname{Hom}_{Y_T}(O_{C_T},O_{Y_T})\) with the line bundle
\(\omega_{C_T/T}\otimes\omega_{Y_T/T}^{-1}|_{C_T}\), including its
evaluation inclusion. This can be checked using the two ambient Koszul
complexes, so its identification survives arbitrary locally Noetherian
base change. Higher Ext over \(Y_T\) vanishes here because the ambient
dual complex for \(C_T\) is concentrated in the same codimension, not
because arbitrary curve modules have no Ext.

The source and target of the evaluation map are flat over the parameter
base. The map on every geometric fiber is still the injective
annihilator inclusion. The local flatness criterion therefore makes its
quotient flat and preserves exactness after pullback. The resulting ideal
is the base-changed colon by the same identification. This verifies the
flatness and base-change assertions even when the linked curves share
support. At \(\eta_C\), the Artinian Gorenstein ring has a
one-dimensional socle; taking the colon by the reduced curve removes
exactly that socle and decreases length by one. Other generic components
are unchanged. This proves the claimed cycle formula.

This argument uses the fixed reduced \(C_T\), which remains a flat
linked subscheme through the jump. It does not apply a full-primary-family
specialization theorem outside its hypotheses. For a direct local control,
\(Y_t=(x,y(y+t))\) contains the fixed \(C=(x,y)\), and its once-linked
family is \((x,y+t)\), flat and equal to \(C\) at \(t=0\). The full
primary component changes there. This is exactly the distinction the
relative result is meant to preserve.

## Interpretation and limitations

The source makes residual geometry a genuine construction parameter and
identifies which residual deformations retain the particular embedded
quartic. None of the smooth Hilbert-space conclusions says that a
multiplicity-jump locus is smooth or nonempty, that primary extraction is
flat, or that sole support is possible or impossible. A general curve with
the same Hilbert polynomial or Rao module need not have the required low
equations. These limitations are essential and retained.
