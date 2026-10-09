# Root acceptance of the October 8 scroll and defect-four results

Date: 2026-10-08. Fixed curve C0=[s^4:s^3t:st^3:t^4], over an
algebraically closed characteristic-zero field. This records proof
review, not a universal STCI resolution or a novelty claim.

This is the intermediate acceptance record. Its statements of pending
audit and the remaining reducible/nonreduced conductor boundary describe
that stage of the work. The
[late reconciliation](2026-10-08-session-late-results-acceptance.md)
records the completed independent audits, full smooth-scroll exclusion,
principal ancestor closure and current remaining strata.

## 1. Every integral quartic singular along a smooth twisted cubic

**Accepted:** such a quartic has no mate cutting out C0 set-theoretically,
in any positive degree. The [applicability proof](2026-10-08-session-scroll-conductor-applicability.md)
and [conductor criterion](2026-10-08-session-irreducible-conductor-compression.md)
together supply the argument. The [independent adversarial audit](2026-10-08-session-scroll-conductor-adversarial.md)
checks the criterion and the entire-conductor Hilbert/CM calculation.
The root additionally checked the stronger equation-space and blowup
transition below. The independent auditor reported acceptance of these
steps before its turn ended at the account usage limit; its planned
section 10 was not completed, so that unwritten section is not cited.

The complete derivative restriction on all 35 quartic monomials has
rank 29. Six independent products of the three twisted-cubic quadrics
span the kernel. The independent [literal-minor source](../computations/audit_scroll_twisted_cubic_equation_space_2026_10_08.py)
rebuilds derivatives by substitution and computes the stated determinant
104509440 by Fraction elimination. Root replay passed in the isolated
continuation snapshot. Thus F=Q(xi1,xi2,xi3) holds for the entire
equation space, without an slc assumption. If Q factored, F would factor
into nonzero quadratic factors; hence integral F gives a smooth conic Q.

The two syzygies define a rank-two matrix at every point of P2. Their
incidence variety is therefore a smooth P1 bundle, agreeing with the
blowup of the smooth twisted cubic. The inverse image S of Q is a smooth
P1 bundle over a smooth conic. The exceptional fiber over each point of
the twisted cubic maps to a line in P2, which a smooth conic cannot
contain. Every fiber of S->X is finite, including tangencies, so this
proper birational map is finite and is the normalization. Off the cubic
it is an isomorphism. A normal local ring on the cubic would also make
it an isomorphism there; since S is smooth and X is singular there,
this is impossible. The whole nonnormal support is exactly the cubic.

Adjunction gives K_S=-E|S, H^2=4 and K_S.H=-6. Finiteness makes H ample,
and H has ruling degree one. On F_e this implies H=C_min+a f,
2a-e=4 and a>e, hence e=0 or 2. These verify the smooth quartic-scroll
hypotheses used by the criterion.

Finite absolute duality identifies the conductor with nu_*omega_S,
not with a relative formula requiring nu to be flat. It is maximal CM
over the quartic surface. Its quotient is a pure CM curve with Hilbert
polynomial 3m+1. Degree three and the smooth degree-three support force
generic multiplicity one. Any nilradical would then be supported at
finitely many points, prohibited by depth one. Thus the actual downstairs
scheme is the reduced smooth twisted cubic. The upstairs conductor is
Cartier and CM, finite over the smooth curve, and torsionfree over each
local DVR; it is flat, of rank H.D/3=2.

The root reviewed all three rank-two conductor cases. For integral
reduced D, invariance of f^n gives sigma(f)/f=+1 or -1, and f^2 descends
through the full conductor square. For reducible D, its algebra is
O+O(-2) with eta^2=q_2^2. Unequal branch factors force both restrictions
to be scalar multiples of q_2 times a linear section. Singleton fibers
put that section's zero at a branch intersection; a smooth lifted curve
cannot have contact greater than the mutual branch contact with both
branches. For nonreduced D, eta^2=0, and the all-n coefficient
n*a^(n-1)*b forces b=0, so f itself descends. The resulting quadric or
hyperplane mates are impossible for C0. The argument uses global
constant units, whole conductor schemes and full inverse support.

The primary equation/blowup presentation was checked in
[Ducat, section 5.7](https://d-nb.info/1317691679/34). The independent
equation certificate removes reliance on extending that paper's slc
classification. The absolute-duality input was checked against
[Stacks 0AX0](https://stacks.math.columbia.edu/tag/0AX0) and
[the CM concentration lemma](https://stacks.math.columbia.edu/tag/0AWQ).

**Boundary:** reducible/nonreduced downstairs conductors, singular
normalizations, other quartic classes and higher carrier degrees remain
outside this theorem.

## 2. Both algebraic e=1,d2=4 ancestor directions

**Accepted:** for A=r*z,B=1,12r^2+4r+3=0, every genuine defect-four
triple has at most one containing quartic. Hence it cannot supply two
independent quartic multiplier equations for the fixed ancestor targets.
This is the narrow [defect-four proof](2026-10-08-session-localcoh-e1-d4-algebraic.md),
not an STCI mate theorem.

The root checked the explicit seven ambient forms, their complete
35-column double conditions, and their normalized h/E coefficients.
Rank 28 of the complete double matrix and independence of the seven
forms establish completeness. Arithmetic in the quadratic field covers
both embeddings. The two free primitive h coefficients uniquely match
the constant and eighth coefficients of delta*E, so the quartic fiber
is exactly the kernel of the remaining seven-by-five operator.

The minors d0^4 and d4^4 give rank at least four on those two opens.
On d0=d4=0, the minors d1^5 and d3^5 give rank five when either is
nonzero. The final delta=d2*z^2 matrix has five pairwise distinct
diagonal constants, so at most one diagonal entry vanishes. This covers
all homogeneous delta, including repeated and infinity roots, and
proves kernel dimension at most one everywhere.

For theta=0, the local ideal (delta*m,my,m^2,y^3) leaves
R/(delta)*m torsion at every defect zero. A nonzero section of O(4)
has such a projective zero, so this is not a valid finite-flat triple.
Every genuine triple therefore has theta!=0, which is normalized to
one by scaling the equation. This discards no valid theta=0 boundary.

The verification agent independently reported this exact coverage and
the torsion check before its usage-limit interruption. Its isolated
source-byte replay is preserved in
[the audit replay directory](../validation/2026-10-08-e1-d4-algebraic-audit/replay-manifest.json);
it did not finish a separate narrative audit. Root's central isolated
replay also passed, with source SHA256
ae88024f00b8216be727957930747001b44f457e532a0746e6a8e2a657850a02.

**Boundary:** the principal obstruction-zero direction and directions
with nonzero primitive quadratic obstruction remain open at positive
D2. This does not exclude every defect-four Gorenstein quadruple.
