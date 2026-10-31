# Independent audit: opposite torus limits and endpoint defects

Date: 2026-10-30. Reviewer: independent degeneration-audit agent (Sol/high),
with no delegation. Reviewed state: [source proposal](2026-10-30-four-streams-degeneration.md),
including Propositions 2.1, 3.1 and 5.1 and equations (1)–(11).

**Disposition:** the stated results pass independent hand reconstruction.
No material mathematical correction is required. They are reviewed
**provisional** results; this audit makes no canonical promotion and supplies
no obstruction or construction for the unrestricted characteristic-zero
STCI question for the fixed quartic. No numerical or symbolic computation
was run, and no inherited proof was rerun.

## 1. Scope and external input

The curve is the smooth embedded quartic
\(C_0=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field of
characteristic zero. The hypothetical ideal is an actual homogeneous
complete intersection \(J=(F_a,G_b)\) with **affine-cone radical**
\(\sqrt J=I_C=P\). The opposite initial ideals are full weight initial
ideals, not the ideals of the two initial generators.

I inspected [Hellus–Hübl, Theorem 1.2 and Remark 1.4, PDF pp. 4–5](https://arxiv.org/pdf/1312.7661).
The source correctly imports their necessary conditions on both extreme
pairs and on the number of weight components. Changing their first
bigrading coordinate to weights \((0,1,3,4)\) reverses the extremes on each
fixed usual degree; their two-sided conclusion is unaffected. Those
conditions do not concern the full flat initial ideal and do not establish
nonexistence. The line example is not represented as a quartic example or
as a counterexample to the paper.

## 2. Full initial ideals and endpoint support

The actual argument is the sandwich
\[
P^N\subset J\subset P
\quad\Longrightarrow\quad
P^N\subset\operatorname{in}_{\pm w}J\subset P.
\]
Both bounding ideals are invariant, hence equal to their own initial
ideals; the implication holds for all their elements, not just selected
generators. It proves equality of radicals even before projectivizing.
Weight degeneration preserves the graded Hilbert function. After removing
irrelevant-vertex torsion, the Hilbert polynomial and degree remain those
of the original complete intersection. The generic length is consequently
\(ab/4\); no reduced residual component appears in these actual limits.

On \(x_0x_1\ne0\), the source's coordinates give the actual ambient ring
\(k[u,u^{-1},A,B]\), with \(u\) of weight one and \(A,B\) invariant.
Every invariant ideal is extended from \(k[A,B]\): decompose a polynomial
into its finitely many weights, then multiply each homogeneous term by a
unit power of \(u\). The invariant local scheme is therefore
\(\mathbf G_m\times\operatorname{Spec}(k[A,B]/K)\), with the second
factor Artinian of length \(ab/4\). This proves Cohen–Macaulayness on the
whole open orbit, without a Gorenstein or two-generator assumption on
\(K\). Its complement in \(C\) consists precisely of the two endpoints.

For a one-dimensional scheme with this sole reduced support, the maximal
finite-support subsheaf \(T\subset\mathcal O_Z\) is an ideal. Quotienting
by it removes all dimension-zero associated points and yields a locally
Cohen–Macaulay curve. Additivity in
\(0\to T\to\mathcal O_Z\to\mathcal O_{\overline Z}\to0\) proves
\[
\chi(\mathcal O_{\overline Z})+\ell
=-ab(a+b-4)/2,\qquad
p_a(\overline Z)=1+ab(a+b-4)/2+\ell.
\]
These are sheaf statements. A finite-length graded module supported only
at the irrelevant vertex contributes nothing to \(T\). The proposal
explicitly maintains this distinction.

## 3. All-degree line control: exact family and embedded length

For every \(d\ge2\),
\((F,G)=(X^d+Y(Z^{d-1}+W^{d-1}),Y^d)\) has radical \((X,Y)\) and
height two. The forms are a regular sequence: reduction modulo the
nilpotent variable \(Y\), or unique factorization, verifies the required
nonzerodivisor. All three weight components are nonzero, including in
positive characteristic.

The substitution \(s=t^{d-1}\) in the proposed family has the correct
exponents. Write \(A_s=Z^{d-1}+s^2W^{d-1}\) and
\(M_i=X^{di}Y^{d-i}\). Multiplying
\(Y A_s+sX^d\) by \(X^{d(i-1)}Y^{d-i}\) gives
\(A_sM_{i-1}+sM_i\), so every listed \(M_i\) lies in parameter
saturation. Conversely, with lexicographic priority for \(Z\), the
listed generators are monic over \(k[s]\). For \(i<d\) the only
nontrivial mixed S-polynomial has remainder
\(sM_{i+1}+s^2W^{d-1}M_i\), which reduces to zero. For \(i=d\),
both remaining terms are divisible by \(M_d\). Monomial-generator pairs
have zero S-polynomial. Standard monomials thus make the quotient free
over \(k[s]\), proving saturation rather than merely guessing initial
generators. Localizing at \(s\) recovers the two original equations.
Base change to \(k[t]\) remains free and \(t\)-torsion-free, even if
the power map is inseparable. Hence (4) really gives the two full limits.

The negative limit contains no \(W\) in its monomial generators, so
\(W\) is a nonzerodivisor and the homogeneous ideal is saturated.
Its hull is exactly \(H=(Y,X^{d^2})\): the quotient by \(H\) is
Cohen–Macaulay, while \(H/I_-\) has finite projective support at
\([0:0:0:1]\). On \(W=1\), its surviving monomials are precisely
\[
X^iY^jZ^k,\quad
1\le j\le d-1,\quad i<d(d-j),\quad k<d-1,
\]
with all exponents nonnegative. Their number is
\(d^2(d-1)^2/2\). This is the length of the embedded sheaf, not the
length of the entire local ring. Exchanging \(Z,W\) proves the positive
case. The \(d=2\) example independently gives basis \(Y,XY\) for
the length-two embedded module. The separate Euler-characteristic
calculation agrees, including the sign of the genus change.

Thus both endpoint defects, extra generators, equal pure hulls and
unbounded defect length can coexist in actual global homogeneous
supported complete intersections. This rules out the proposal's listed
general bridges. It supplies no conclusion about analogous existence on
the fixed quartic.

## 4. Missing section, Rao sequence and prescribed four-space lift

The degree-one defect needs only the five independent monomials of
\(H^0(\mathbf P^1,\mathcal O(4))\) and the four prescribed ambient
ones. The Koszul resolution of an actual complete intersection with
\(a,b\ge2\) gives
\(H^1(\mathcal I_Y(1))=0\) and \(H^0(\mathcal I_Y(1))=0\).
Consequently \(e=s^2t^2\) cannot lift to \(\mathcal O_Y(1)\), proving
(8). No liaison theorem or full all-twist Rao computation is required
for that assertion.

For a limit, the image of \(T\) in \(\mathcal O_C\) is zero because
the latter has no finite-support subsheaf. The resulting exact sequence
\(0\to T\to\mathcal N_Z\to\mathcal N_{\overline Z}\to0\)
gives the claimed natural isomorphism on \(H^1\); naturality identifies
the two connecting classes. Also
\(H^0(\mathcal O_Z(1))\to H^0(\mathcal O_{\overline Z}(1))\)
is surjective. These assertions need no choice of splitting or local
formal-to-projective gluing.

In the ideal-sheaf sequence
\(0\to\mathcal I_Z(1)\to\mathcal I_{\overline Z}(1)\to T(1)\to0\),
both initial global-section spaces vanish: their ideals are contained
in the ideal of the nondegenerate reduced curve. Since \(H^1(T(1))=0\),
its cohomology is exactly (10). The inclusion into \(\mathcal I_C\)
factors through the hull ideal, so the injected endpoint summand maps
to zero in \(M_C(1)\). The ideal sequence for \(C\subset\overline Z\),
or the restriction sequence of structure sheaves, proves the equivalence
of (1)–(3). No assumption that \(H^0(\mathcal O_Z(1))=(R/J_\pm)_1\)
is made; that equality could fail.

Finally, diagonalizability of \(\mathbf G_m\) provides a weight-two lift
whenever any lift exists. The prescribed four ambient sections already
generate \(\mathcal O_{\overline Z}(1)\), including on nilpotents.
Adding the fifth gives a morphism avoiding the projection center. Over
\(\mathbf P^4\setminus\{\text{center}\}\simeq
\operatorname{Tot}(\mathcal O_{\mathbf P^3}(1))\), it is the graph of
an actual global section over the given closed immersion of the hull.
It is a closed immersion there, and properness gives a closed immersion
into \(\mathbf P^4\). The converse extra-coordinate restriction is
immediate. This verifies the particular marked embedding in (4), not
an arbitrary four-space embedding.

## 5. Findings and effect on the full problem

**Material findings: none.** Explicitly tested possible failure mechanisms
were confusing initial generators with the full initial ideal; ignoring
parameter torsion; losing projective saturation; counting vertex torsion
as endpoint length; using arithmetic Cohen–Macaulayness for a pure hull;
equating graded pieces with sheaf sections; inferring a global embedding
from formal local lifts; and importing the line control as a quartic
construction. None occurs in the reviewed proposal. Characteristic zero
is required for the imported quartic literature statements; the exact
line algebra itself works in every characteristic.

The geometric contribution is a description of how equivariant
degeneration can retain sole curve support while distributing nilpotent
structure between a pure multiple curve and finite endpoint torsion.
The missing-coordinate class, however, is unaffected by deleting that
torsion; it belongs to the extension carried by the pure hull. Thus a
successful quartic-specific argument must control these pure embedded
extensions for two limits of the same actual ideal. No compatibility
theorem, positive residual bound, nonvanishing after specialization or
contradiction between the two limits has been proved here. The
unrestricted STCI question for \(C_0\) remains open.
