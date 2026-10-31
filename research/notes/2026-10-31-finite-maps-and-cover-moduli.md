# Finite maps, supported closure, and the limits of cover moduli

Date: 2026-10-31. Status: **independently reviewed provisional
deductions and source-scope assessment**; see §6. No canonical promotion.
The unrestricted characteristic-zero STCI question remains open.

The target is the fixed curve
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
The elementary statements in §§1 and 3 work over an algebraically
closed field in every characteristic. The ramification comparison
in §2 is in characteristic zero. These are geometric extractions,
not new nonexistence theorems.

## 1. A finite ambient map is an exact reformulation

Suppose \(V(F_a,G_b)_{\rm red}=C_0\). Set \(D=ab\) and
\[
\Phi=[F^b:G^a:x_0^D:x_3^D]:\mathbf P^3\longrightarrow\mathbf P^3.
\]
There are no basepoints: simultaneous zeros of the first two
coordinates lie on C0, where x0 and x3 do not vanish together.
Since \(\Phi^*\mathcal O(1)=\mathcal O(D)\) is ample, no fiber
can contain a curve. Properness then makes Phi finite; its image
has dimension three and is the whole target. For the line
\(L=V(y_0,y_1)\),
\[
\Phi^{-1}(L)=V(F^b,G^a),\qquad
\Phi^{-1}(L)_{\rm red}=C_0.
\tag{1}
\]
Conversely, the pullbacks of the two equations of a line under a
finite endomorphism give a proper CI with that reduced inverse
image. One can replace D by lcm(a,b), using powers D/a and D/b.
Equalizing degrees preserves the existence question, not the
original thickening.

This proves a general dictionary. A nonempty projective subset
\(X\subsetneq\mathbf P^n\) of pure codimension r is an STCI if
and only if it is the reduced inverse image of a codimension-r
linear space under a finite endomorphism of \(\mathbf P^n\).
Equalize its r defining degrees to D, and add Dth powers of
n+1-r linear forms whose common \(\mathbf P^{r-1}\) misses X.
The same ample-pullback argument proves finiteness. The converse
pulls back the r linear equations; their zero set has codimension r.

For C0 the restriction of the displayed map to C0 is
\([s:t]\mapsto[s^{4D}:t^{4D}]\), of degree 4D. Its target is a
line, not C0. This is not a totally invariant curve:
\(\Phi^{-1}(C_0)=C_0\) has not been supplied. Any argument requiring
iteration on the same embedded variety therefore needs new input.

Geometrically, the remaining two coordinates complete an existing
supported pair to a finite map. They do not remove residual support
from a pair that had it. Thus (1) gives no independent construction
of the two missing equations.

## 2. The new ambient ramification returns the old different

In characteristic zero the homogeneous Jacobian determinant is
\[
\det(d\Phi)=\pm abD^2
 F^{b-1}G^{a-1}x_0^{D-1}x_3^{D-1}
 (F_{x_1}G_{x_2}-F_{x_2}G_{x_1}).
\tag{2}
\]
Factor the derivatives of the four powers from their rows, then
expand along the x0 and x3 rows. The total degree is \(4D-4\).
After removing the explicitly added power ramification, the
remaining determinant has degree \(a+b-2\).

On the chart x0 nonzero, the base coordinate of the original
pencil is x3/x0. The last factor of (2) is its relative Jacobian,
up to the usual invertible chart factor. It generates the
different of the finite CI cover
\[
Y=V(F,G)\longrightarrow B=\mathbf P^1,\quad [x]\mapsto[x_0:x_3].
\]
This is the full, possibly nonreduced cover in the
[reviewed different calculation](2026-10-31-cyclic-cover-duality.md),
not just its reduced fourfold map. The canonical-degree formula
for the completed ambient morphism supplies no independent
budget beyond this existing different.

The primary-source scope checks are:

- [Chinburg–Moret-Bailly–Pappas–Taylor, Definition 1.1 and
  Theorem 1.2](https://arxiv.org/pdf/1201.0678) complete already
  supplied ample sections, preserving their zero supports.
  The desired pair remains an input in this application.
- [Poonen, Theorem 2.2](https://math.mit.edu/~poonen/papers/selfmap.pdf)
  extends suitably polarized maps to ambient projective space.
  An extension of a map C0 to a line only ensures containment
  in its inverse image, without eliminating residual support.
- [Jamet, Proposition 1.1 and §1.3](https://arxiv.org/pdf/math/0103202)
  concerns the full inverse scheme. Its section-lifting statements
  cannot be transferred to that scheme's reduction.
- [Luo–Meng, stated invariance hypothesis](https://arxiv.org/pdf/2610.10103)
  requires \(f^{-1}(V)=V\), absent in (1). Only this hypothesis
  and its use of iteration were checked, not the entire new preprint.

These limits do not exclude a different finite-map construction.
The existing finite-pullback exclusion with a twisted-cubic target
has different polarization and correction-space hypotheses; it
does not apply to the line target here.

## 3. Supported flat closure exists; two global equations need not survive

Let \(M=V(x_0,x_3)\), let \(P=\operatorname{Bl}_M\mathbf P^3\),
and use its plane-bundle morphism \(p:P\to B=\mathbf P^1\).
The strict transform of C0, denoted C, misses the exceptional
divisor and is finite over B. Let \(B^\circ\subset B\) be any
nonempty open subset. Suppose an actual embedded scheme
\[
Y^\circ\subset P|_{B^\circ}
\]
is finite flat over \(B^\circ\), with reduced support \(C|_{B^\circ}\).
Then its scheme-theoretic closure \(\overline Y\subset P\) is
the unique embedded B-flat extension. It is finite flat of the
same degree, is supported on C, and descends to an embedded
locally Cohen–Macaulay thickening of C0 in \(\mathbf P^3\).

Indeed, the topological support of scheme closure is the closure
of C restricted to \(B^\circ\), hence C
([Stacks, Lemma 29.6.3](https://stacks.math.columbia.edu/tag/01R5)).
Thus the proper map \(\overline Y\to B\) is quasi-finite and
therefore finite
([Stacks, Lemma 37.44.1](https://stacks.math.columbia.edu/tag/02LS)). At an
omitted point of B, its ideal is saturated under the base
uniformizer: closure is defined as the kernel of restriction
to \(Y^\circ\). Multiplication by that uniformizer is injective
on its structure sheaf. A finite torsion-free module over a DVR
is free, proving flatness and preservation of degree
([Stacks, Lemma 15.22.10](https://stacks.math.columbia.edu/tag/0539)). Any flat
embedded extension has the same saturation, proving uniqueness.
The support misses the exceptional divisor, so the closure
descends through the isomorphism over \(\mathbf P^3\setminus M\).
Flatness over the smooth curve gives the locally CM assertion.

The proof works for any projective curve disjoint from an axis
of a finite linear pencil, and does not use the monomial
parametrization, two distinguished points, or a prescribed cycle.
It is a standard scheme-closure argument extracted here for its
meaning in the affine-to-projective strategy.

It does **not** preserve Gorenstein endpoint fibers, a specified
splitting of \(p_*\mathcal O_{\overline Y}\), algebra-linear
canonical duality, or the global two-generator ideal. Closing a
scheme and closing its two defining equations are different
operations. Homogenized equations can acquire components at
infinity which saturation removes from the scheme closure,
without leaving a two-generated ideal. Thus closure alone
cannot force a residual curve; a proposed obstruction must
retain the two-equation requirement.

## 4. The checked moduli theorems leave this ambient condition open

For the actual CI pencil, the inherited module splitting is
\[
\pi_*\mathcal O_Y\simeq
\bigoplus_{0\le i<a,\ 0\le j<b}\mathcal O_B(-i-j).
\]
[Poonen, Proposition 1.1 and §2](https://arxiv.org/pdf/math/0608491)
gives an affine parameter scheme for algebras with a global
ordered module basis. This nontrivial bundle has no such basis.
Its algebra law is described on its frame bundle equivariantly,
or by a map to the quotient stack, not by a map from B to the
affine based-algebra scheme. Proper-to-affine constancy supplies
no contradiction.

Nor must every complete family of punctual CIs meet the
non-CI boundary. [Benoist, Theorem 0.8, Corollary 0.10 and
Proposition 3.23](https://arxiv.org/pdf/1212.4862v2) constructs
complete curves in the homogeneous binary-CI locus for
unequal degrees. These represent subschemes of the affine
plane supported at the origin. Remark 3.24 gives rational
examples for consecutive degrees; Remark 3.25 does not
assert rational examples for every pair. The equal-degree
locus is affine. This flexibility refutes a blanket
boundary-positivity premise; it neither supplies the fixed
ambient normal symbols nor constructs the required C0 thickening.

[Deopurkar, Definition 3.3(2) and Theorem 3.8](https://ananddeopurkar.org/papers/CompHurwitz.pdf)
requires a generically étale cover on each target component.
The full hypothetical Y is generically nonreduced, with
identically degenerate trace discriminant. The proper Hurwitz
branch morphism therefore does not apply to it.
[Lieblich, Proposition 2.1.5](https://arxiv.org/pdf/math/0603034)
represents coherent algebra laws, but the properness results
of Theorems 1.3–1.4 concern branchvarieties with geometrically
reduced source fibers (Definition 1.1). Representability of
the algebra problem does not give that properness for Y.

## 5. Consequence for the unrestricted question

The useful gains are the general finite-map dictionary, the
identification of its ramification with existing data, and
the supported-closure lemma. None supplies new equations
or a residual-degree floor. The source checks also rule out
an unjustified affineness or forced-boundary shortcut.

For existence, an actual supported punctured family can be
closed in the correct ambient threefold; the decisive remaining
question concerns the global ideal and its section ring.
For nonexistence, one needs a new restriction on that same
embedded closure, beyond support or the inherited different.
Abstract algebra families and rational punctual-CI families
retain genuine flexibility.

Stop these two bounded selections. Do not follow them with a
map-degree, Artin-length, Hilbert-function or endpoint-type
classification. Reopen only with an actual ambient operation
that changes the global equation/section defect while preserving
support, or a specified all-pair comparison involving that
defect. A one-step inverse-image theorem must apply without
total invariance; a boundary theorem must include the full
nonreduced cover and its prescribed ambient data. Stop if the
proposed argument discards those conditions or merely specifies
the two missing equations in another form.

## 6. Independent review and disposition

The two read-only selections used fresh gpt-6-astra/xhigh
contexts: /root/finite_endomorphism_global_selection and
/root/gorenstein_cover_moduli_selection. The independent
challenger /root/finite_map_moduli_strategy_challenge used a
fresh gpt-6.1-sol/high context. No nested delegation or
computational experiment was performed.

The challenger independently reconstructed the finite-map
equivalence and generalization, the determinant, and the
supported-closure lemma. It checked the source hypotheses,
challenged both stopping decisions for missing constructive
input, and then checked this written note, assessment §33 and
the literature-ledger section. Its disposition was **scoped
PASS, with no material correction**. The closure operation
was expressly retained as positive input; no unsupported
next experiment was identified.

The exact pre-metadata source SHA256 was

    9de8cd4c8d8e0090581be9e64db26074f7441b9fbbe768153c661b964e7b0b2d

After that review the parent changed status metadata, added
this record and the three Stacks references already checked
by the reviewer. No mathematical assertion changed. The
review did not audit the entire Luo–Meng preprint, rerun
inherited proofs, or establish an unrestricted STCI conclusion.
All three bounded assignments are complete and are not
assigned further research from these contexts.
