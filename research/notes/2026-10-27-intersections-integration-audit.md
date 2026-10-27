# Independent audit of the containing-intersection stratification and integration

Date: 2026-10-27. Reviewer: global-intersections agent, independently reviewing
the coordinating agent's [multiplicity-strata note](2026-10-27-intersection-multiplicity-strata.md).
Status: **PASS for the stated fixed-degree rank-locus, specialization, and
endpoint deductions, with the residual-scheme distinction below incorporated
in the source**. No canonical promotion. The broader synthesis is independently
reviewed in Section 7.

The review followed [INDEX](../INDEX.md), [MAP](../MAP.md), and
[the contribution protocol](../CONTRIBUTING_AGENT.md). It reconstructs the
new local argument; no accepted proof or inherited finite certificate was
rerun.

## 1. Reconstruction of the degree bound and finite algebra

Assume an algebraically closed field \(k\), in any characteristic, the fixed
smooth quartic \(C=[s^4:s^3t:st^3:t^4]\), and actual homogeneous equations of
fixed degrees \(a,b\) with no common surface factor. Their ideal is a regular
sequence in the polynomial ring; its projective curve \(Y\) is
Cohen–Macaulay and pure of dimension one. The fundamental cycle therefore
has the exact effective decomposition

\[
[Y]=m_C[C]+R,\qquad ab=4m_C+\deg R.
\]

At the generic point of \(C\), the completed ambient transverse ring is the
regular local ring \(K[[X,Y]]\), with \(K=k(u)\). Its quotient by the actual
equations is Artinian, of length \(m_C\le B=\lfloor ab/4\rfloor\).
If an Artinian local algebra has length \(m\), its maximal ideal has
\(m\)-th power zero: any chain surviving through that power would have at
least \(m+1\) nonzero successive quotients. Thus adding \((X,Y)^{B+1}\)
does not change this length. This bound is uniform for every proper pair
in the fixed degree range, and it avoids an unbounded stabilization
claim.

The multiplication map on
\[
A=K[X,Y]/(X,Y)^{B+1}
\]
must contain all truncated monomial multiples of both equations. Its image
is exactly the truncated ideal, so
\[
m_C=\dim_K A-\operatorname{rank}_K(A^2\longrightarrow A)
\]
is correct. A matrix containing just the two equation vectors would be
incorrect; the reviewed note explicitly does not make that substitution.
Using \(B+1\), rather than assuming a length-\(B\) quotient is already
visible from too short a jet, is safe. The empty \(B=0\) case is handled
separately.

## 2. Descent of the rank condition from \(k(u)\) to \(k\)

This is the essential global-coefficient check. Choose a basis of the
actual vector space \(H^0(I_C(d))\) over \(k\), introduce its scalar
coefficient variables, and use the displayed polynomial coordinate
substitution on \(x_0\ne0\). Every entry of the multiplication matrix is a
polynomial in \(u\), whose coefficients are polynomials in those scalar
variables. No arbitrary rational-function-valued coefficients are introduced.

The inequality \(m_C\ge r\) is equivalent to vanishing of all
\((\dim A-r+1)\)-minors over \(k(u)\). A polynomial in \(k[u]\) is zero in
\(k(u)\) precisely when every coefficient is zero. Each minor has finite
degree in \(u\), so coefficientwise vanishing is a finite list of equations
over \(k\). The locus is closed in every affine coefficient chart.
Rescaling either equation multiplies each relevant minor by the expected
scalar power, and hence preserves its zero locus. Therefore the conditions
descend to the product of projective equation spaces. Restriction to the
proper-pair open set gives the claimed relative closedness.

This argument works in positive characteristic as stated. A rank may change
between characteristics, but that does not invalidate closedness over any
fixed field. It proves no uniform rank across arithmetic fibers.

## 3. Specialization and the supported endpoint

The condition \(m_C\ge r\) is closed, so multiplicity is upper
semicontinuous: it can increase in a specialization remaining inside the
proper-pair locus. The cycle identity then says that residual degree can
decrease only by **multiples of four**. There is no assertion that every
intermediate value occurs or that the decrease is always exactly four.
If the equations acquire a common surface factor, the pure
complete-intersection degree argument ceases to describe that fiber, so
removing that boundary is necessary.

If \(4\nmid ab\), no multiplicity uses all of degree \(ab\). If
\(4\mid ab\), putting \(M=ab/4\) gives
\[
m_C=M\quad\Longleftrightarrow\quad R=0
\quad\Longleftrightarrow\quad \operatorname{Supp}(Y)=C.
\]
The last implication uses purity: a proper complete intersection has no
isolated support points which could escape the cycle calculation.
Consequently the supported locus is closed **relative to proper pairs**.
Its nonemptiness is not supplied by closedness, a local model, or an
approach to a common-factor pair.

The numerical comparisons are correct: \((5,5)\) cannot have sole support
because \(4\nmid25\); \((6,6)\) and \((5,8)\) pass this arithmetic test.
Passing the test is a necessary condition only. The accepted
characteristic-zero lower-degree exclusion is used within its canonical
scope and is not rederived.

## 4. Residual-scheme wording clarification

There are two different objects:

* The **once-linked residual** defined by \((F,G):I_C\), which may still
  contain \(C\) when \(m_C>1\).
* The residual scheme obtained by removing the entire \(C\)-primary
  component, whose fundamental cycle is \(R\).

For fixed \(a,b\), classical linkage to the fixed reduced \(C\) fixes the
degree and arithmetic genus of the once-linked residual:
\[
\deg D_{\mathrm{link}}=ab-4,\qquad
p_a(D_{\mathrm{link}})=\frac{(a+b-4)(ab-8)}2.
\]
These do not jump when \(m_C\) jumps. When \(m_C=1\), the linked residual is
the full residual away from \(C\), and these same invariants are fixed
throughout that open stratum; its normalization genus, singularities, and
component gluing may vary. For higher multiplicity, changes in the
supported primary thickening must be separated from the once-linked
residual before discussing Hilbert polynomials.

The earlier sentence about residual arithmetic genus possibly changing at
fixed \(m_C\) needed to specify the full primary residual in higher
multiplicity or use **normalization genus** on the multiplicity-one
stratum. The coordinating author incorporated this distinction after the
review. The rank-locus theorem and endpoint equivalence do not depend on
that wording.

## 5. Scope and review outcome

The fixed-degree stratification is mathematically sound with its literal
hypotheses and with scalar coefficients retained. It provides a
construction problem in actual projective equation spaces and an exact
test for each degree pair. It supplies neither a bound on witness degrees
nor existence or nonexistence of an unrestricted characteristic-zero
STCI. In particular a description of a closed terminal locus is not a
completed elimination of that locus.

The integration synthesis is independently reviewed in Section 7 below.

## 6. Additional degree-six Plücker locus

The later-added first-thickness locus was independently reconstructed.
Here \(\dim V_6=84-25=59\), so \(\dim\operatorname{Gr}(2,V_6)=114\).
The normal determinant has degree 34 on \(\mathbf P^1\), hence target
dimension 35. The all-degree boundary calculation supplies a differential
surjecting onto this 35-dimensional vector space. Each such derivative
has the form
\[
\Phi(h\wedge g+f\wedge k),
\]
so the linear wedge map \(\Phi:\bigwedge^2V_6\to H^0(\mathcal O(34))\)
is surjective. Its 35 equations are independent in the ambient Plücker
space.

At the generic transverse two-dimensional regular local ring, length one
is equivalent to the first symbols spanning the maximal ideal modulo its
square, by Nakayama. Within the proper-pair locus, determinant zero is
therefore equivalent to \(m_C\ge2\). The resulting linear section has
projective components of dimension at least \(114-35=79\), by successive
hyperplane intersection. Independence of the ambient equations does not
make their restriction transverse on the Grassmannian; the note correctly
asserts no equality of codimension.

For the explicit witness, \(A=x_0^2x_2-x_1^3\) has no common factor with
\(x_0q\). On \(x_0=1\), its generic transverse ideal with \(q\) is
\((X,Y-uX)\). Thus \((qx_0^4,A^2)\) gives the quotient
\(K[[X,Y]]/(Y-uX,X^2)\), of length exactly two. It is an actual proper
pair, even though its surfaces are reducible or nonreduced. Hence some
component of the projective first-thickness locus meets the proper open
set. The dimension bound persists on that nonempty open part.

**Outcome: PASS.** This does not assert existence of multiplicity three,
of an integral-carrier point in a selected component, or of the terminal
sextic multiplicity nine.

## 7. Independent integration review

Source: [Intersections containing C: residual geometry, formal visibility,
and construction](2026-10-27-containing-intersections-research-vision.md).
The review compared its assertions with the three source notes and their
separate independent audits, and independently reconstructed the logical
bridges below. **Outcome: PASS for the stated provisional synthesis.**

The common hypotheses are consistently fixed: the displayed smooth quartic,
actual global homogeneous equations, and proper intersections. The
characteristic-zero general-pair geometry has \(a,b\ge4\); its formulas are
not transferred to determinant-zero or arbitrary singular-carrier strata.
The table's mixed-degree \((5,8)\) values reconstruct as degree 36, genus
\((13-4)(40-8)/2=144\), and attachment length \(52-14=38\).
The equal-sextic parameter and fiber dimensions reconstruct as 114 and 80.
General attachment dominance does not assert realization of every special
divisor or every residual curve with the right numerical invariants.

The residual interpretations are kept distinct. Once-linked residuals
have fixed degree and genus and the linkage-dual Rao module, even if they
retain \(C\). Full primary removal has cycle degree \(ab-4m_C\).
No embedded thickening is inferred solely from a cycle. The arithmetically
Buchsbaum/even-liaison interpretation follows from the one-dimensional
Rao module and its self-duality up to shift, with no classification or
direct-link existence asserted.

For the formal interface, the inherited multiplicity detector follows
from associativity:
\[
e_p(Y)=m_C+\sum_{D\ne C,\ p\in D}m_D e_p(D).
\]
The reduced marked curve is smooth, so its local multiplicity is one.
Projective CI connectedness forces a nonempty residual *union* to meet
\(C\); it does not force every residual component to meet it individually.
This proves the asserted existence detector but does not make it positive
for every pair. The local pure-power example in the formal note has the
same generic algebra with or without a special residual branch, so generic
transverse information cannot replace full embedded completion.

The global formal-section statement uses a stronger object than an
unlabelled formal ideal. Assuming the cited classical G3 theorem, dividing
by a rational section identifies a globally glued fixed-twist formal
section with a rational section on \(\mathbf P^3\). Faithful flatness gives
regularity along \(C\). A polar divisor cannot avoid the projective curve,
so there is no polar divisor, and smooth ambient normality extends the
section globally. The synthesis accurately locates the remaining
construction problem in producing compatible fixed-twist formal sections
and uniform power containment; finite jets or symbols alone do not do so.
With those exact data, common surfaces are impossible by local dimension,
and any remaining residual components would contradict connectedness.
Hence the stated formal equivalence is sound and supplies no existence
theorem by itself.

The conormal-based sufficient finite-jet injectivity thresholds have the
correct indexing. For \(C_n=V(I_C^{n+1})\), vanishing of every possible
first nonzero symbol in orders \(r\ge n+1\) follows from
\(7(n+1)>4d\), or \(6(n+1)>4d\) in characteristic two. Thus the stated
floors are sufficient. The missing ambient linear monomial \(s^2t^2\)
exhibits failure of liftability despite injectivity.

For the positive-characteristic interface, the monic relations give a
flat actual complete intersection. On the torus,
\(w^q-1=(w^{m_0}-1)^{p^e}\) when \(q=p^em_0\), so the generic
component count and thickness in the synthesis are exact. The \(m_0\)
quartic closures, each weighted \(p^e\), exhaust degree \(4q\); purity
prevents hidden zero-dimensional components. The pure-\(p\)-power case
must remain subject to the displayed semigroup condition
\(q\in\langle3,4\rangle\). Suitable powers exist in every prime; the
synthesis first states that condition and does not claim that every
small \(p^e\) is admissible.

The attachment formula has total degree
\((q+5)+(3q-3)=4q+2\), agreeing with the conormal determinant degree.
At \(q=7\), each separate endpoint contact at \(p_0\) is three since no
nontrivial seventh root is a cube root; the sum is 18, while the scheme
union has length 12 there. Thus its gluing warning is substantive.
Odd-characteristic examples have balanced conormal by R-0020, confirming
that the characteristic-two splitting jump is not necessary for the
finite-group-scheme mechanism. None of this implies failure of other
characteristic-zero constructions.

The proposed next computations stay inside the proved interface:
first study the proper sextic \(m_C\ge2\) locus, then impose actual
higher-jet rank conditions. Dimension at least 79 and an exact-\(m_C=2\)
point do not imply that \(m_C=3\), \(m_C=9\), or any integral-carrier
subfamily exists. The partial rational sextic experiment supplies only
properness, residual degree, and arithmetic genus; the source note
explicitly states that smoothness and reduced attachments were not
certified. The synthesis makes no use of that unfinished certificate.

The authority table distinguishes canonical premises, inherited reviewed
provisional inputs, standard literature consequences, and new reviewed
provisional deductions. No claim is promoted, the unrestricted
characteristic-zero question remains open, and no degree-independent
existence/nonexistence result is inferred. Primary literature access gaps
remain explicit in the formal source note rather than being presented as
completed original-proof checks.
