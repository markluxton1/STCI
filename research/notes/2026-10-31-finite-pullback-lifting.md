# Polarization and section lifting in finite pullback constructions

Date: 2026-10-31. Status: **independently reviewed provisional theorem**;
see the [audit](2026-10-31-finite-pullback-lifting-audit.md), including its
final check of the preserved statement. No canonical promotion or
unrestricted STCI claim.

## 1. A sufficient construction that creates thickness

Let

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\qquad T=[u^3:u^2v:uv^2:v^3]\subset\mathbf P^3.
\]

The twisted cubic has the actual supported complete intersection

\[
q=y_0y_2-y_1^2,\qquad
g=y_2^3-2y_1y_2y_3+y_0y_3^2,
\qquad V(q,g)_{\rm red}=T.
\]

Its generic length is two. This inherited pair is recorded in the
[contact note](2026-10-31-contact-global-consequence.md#4-commuting-homogeneous-generators-are-an-additional-requirement).
If a finite morphism \(\Phi:\mathbf P^3\to\mathbf P^3\), with
\(\Phi^*O(1)=O(d)\), satisfied
\(\Phi^{-1}(T)_{\rm red}=C_0\), then \(q(\Phi),g(\Phi)\) would give
both defining equations for C0, of degrees (2d,3d). Unlike ordinary
Cremona equivalence, a finite ramified map can create transverse
thickness. It was therefore a legitimate constructive source to assess.

The literature separates extension of a reduced map from control of its
full inverse image. [Poonen, Theorem 2.2](https://math.mit.edu/~poonen/papers/selfmap.pdf)
extends a suitably polarized map from a **fixed** closed subscheme of
projective space when its degree is sufficiently large. It gives no
sole-inverse-support conclusion. [Jamet, §1](https://arxiv.org/pdf/math/0103202)
uses the finite-flat full inverse image and its direct images; replacing
that scheme by its reduction would discard the relevant structure.

The following argument excludes this construction source in all degrees.
It also extracts a general polarization-and-lifting principle. It is not
a claim of publication novelty or a reduction of arbitrary STCI pairs to
finite pullbacks.

## 2. Prime-to-characteristic torsion on a rational thickening

Let W be a projective scheme with \(W_{\rm red}=C\simeq\mathbf P^1\)
over an algebraically closed field k. Let N be a positive integer
invertible in k. Then

\[
\operatorname{Pic}(W)[N]=0.
\tag{1}
\]

Indeed let J be the nilradical. The sequence of abelian sheaves

\[
1\longrightarrow1+J\longrightarrow O_W^\times
\longrightarrow O_C^\times\longrightarrow1
\]

is exact. Every global unit on C is a constant and lifts to W. Therefore

\[
H^1(1+J)\ \simeq\
\ker(\operatorname{Pic}(W)\to\operatorname{Pic}(C)).
\]

The N-th power map is an automorphism of \(1+J\). One can see this
through its finite filtration: on
\((1+J^r)/(1+J^{r+1})\simeq J^r/J^{r+1}\), it is multiplication by
the invertible scalar N. Hence it also acts invertibly on
\(H^1(1+J)\). Since \(\operatorname{Pic}(C)=\mathbf Z\) has no
N-torsion, (1) follows. In characteristic zero the logarithm identifies
the entire kernel with the additive vector space \(H^1(J)\), so Pic(W)
is torsion-free. In positive characteristic only the asserted
prime-to-characteristic torsion vanishing is used.

Geometrically, nilpotent thickening of this rational support cannot
introduce a new prime-to-characteristic choice of a root of a fixed line
bundle. No primitive, normal-flat or Gorenstein hypothesis is needed.

## 3. A section-lifting principle

Let \(W\subset\mathbf P^r\), r≥2, have \(H^0(O_W)=k\), and suppose

\[
\operatorname{Pic}(W)[N]=0,\quad d=Nq>0,\quad
H^1(I_W(q))=0,\quad H^0(I_W(d))=0.
\tag{2}
\]

There cannot be a morphism
\(\Phi:\mathbf P^r\to\mathbf P^N\), represented by degree-d forms
without a common zero, whose restriction to W factors scheme-theoretically
through the degree-N rational normal
curve \(\Gamma_N\subset\mathbf P^N\).

For suppose it exists, and write \(\pi:W\to\Gamma_N\simeq\mathbf P^1\).
Put H=O_W(1) and \(L=\pi^*O_{\mathbf P^1}(1)\). The target embedding
gives \(L^N\simeq H^d\). Condition (2) forces \(L\simeq H^q\).
The two pullbacks of the standard sections of \(O_{\mathbf P^1}(1)\)
therefore give sections a,b of H^q. They lift to degree-q ambient forms
A,B by the cohomology vanishing in (2).

The identification of \(L^N\) with H^d differs from the N-th power of
the chosen identification of L with H^q by one global unit on W. Since
\(H^0(O_W)=k\), it is a scalar λ. In standard target coordinates,

\[
(\Phi_0,\ldots,\Phi_N)|_W
 =\lambda(a^N,a^{N-1}b,\ldots,b^N).
\]

Subtract the corresponding monomials in A,B. Every difference is a
degree-d equation of W, hence is zero by (2). These are identities of
ambient forms. Consequently their common zero set contains V(A,B), which
is nonempty in \(\mathbf P^r\) because r≥2 and q>0. This contradicts
the assumed morphism. Equivalently its coordinate map has been forced
globally into the same one-dimensional Veronese image. \(\square\)

The mechanism is global: a forced root of the hyperplane polarization
extends to a two-section pencil, and the lack of correction sections
prevents the original map from escaping the pencil's Veronese image.
All four conditions in (2) are material; mere agreement on the reduced
curve is not enough.

## 4. Finite pullback of the twisted cubic

**Theorem.** Over an algebraically closed field of characteristic other
than three, no finite \(\Phi:\mathbf P^3\to\mathbf P^3\) has
\(\Phi^{-1}(T)_{\rm red}=C_0\). More generally this holds with C0
replaced by any smooth rational space curve whose degree is prime to three.

**Proof.** Write \(\Phi^*O(1)=O(d)\), d>0, and let W denote the full
scheme inverse image. A finite morphism between the smooth equidimensional
projective spaces is flat. Pulling back the twisted cubic's ideal-sheaf
resolution therefore gives

\[
0\longrightarrow O_{\mathbf P^3}(-3d)^2
\longrightarrow O_{\mathbf P^3}(-2d)^3
\longrightarrow I_W\longrightarrow0.
\tag{3}
\]

Vanishing of intermediate cohomology of line bundles on \(\mathbf P^3\)
implies

\[
H^1(I_W(t))=0\quad\text{for all integers }t,
\qquad H^0(I_W(d))=0,
\qquad H^0(O_W)=k.
\tag{4}
\]

If C has degree c and \(e=\deg(C\to T)\), comparison of polarizations
gives \(3e=cd\). For c prime to three, this forces 3|d. Apply §2 with
N=3 and then §3 using (4). The result is a contradiction. \(\square\)

For C0 there are additional consistent numerical conditions. If n is
the generic length of W along C0, finite-flat pullback gives

\[
3e=4d,\qquad4n=3d^2,\qquad en=d^3.
\]

Thus 6|d, and the supported complete intersection pulled back from (q,g)
would have length 2n. The first numerical possibility would have been
d=6, (e,n,2n)=(8,27,54). No such map exists by the theorem. The proof
uses only 3|d; it does not rest on a bounded search or on the multiplicity
calculation.

## 5. Generalization and the scope control from characteristic two

The same argument applies to \(\Gamma_N\subset\mathbf P^N\), N≥2,
over an algebraically closed field in which N is invertible. A finite
endomorphism of polarization degree d cannot have smooth rational reduced
inverse image if N|d. In particular it cannot have a reduced inverse
curve that is smooth rational and of degree c coprime to N, since
\(Ne=cd\) forces N|d.

To check the cohomological input, the rational normal curve has its linear
free resolution, with successive twists
\(-2,-3,\ldots,-N\). Flat pullback multiplies these by d. Intermediate
cohomology of the resulting line bundles gives
\(H^1(I_W(t))=0\) for all t and \(H^0(I_W(d))=0\), exactly as in
(4). Thus §3 applies; no classification of thickenings is involved.

The characteristic qualification is substantive. When the characteristic
divides N, the nilpotent unit group need not have an invertible N-th power
map, and this proof does not apply. It makes no existence claim in those
characteristics.

For the fixed quartic, N=3 means the exclusion includes characteristic
two. Yet C0 **is** an STCI there, with the inherited quartics

\[
x_1^4-x_0^3x_3,\qquad x_2^4-x_0x_3^3.
\]

On x0=1 these give \(x_3=x_1^4\) and
\((x_2-x_1^3)^4=0\); at x0=0 only the endpoint remains. This is the
prescribed pair used in [R-0031](../results/quartic_char2_fourth_equation_kernel.md).
Thus the finite-twisted-cubic source is provably nonexhaustive even in a
characteristic where this curve is STCI. This is a scope check using
existing equations, not a new characteristic-p search.

## 6. Effect on the unrestricted question and disposition

The result closes a sufficient construction source in every degree and
extracts a general obstruction from polarization roots, global section
lifting and the absence of correction terms. It supplies no arbitrary-pair
reduction. In particular the line target, which is itself a CI, has
degree-d equations in its pullback and does not satisfy the no-correction
hypothesis in §3. The theorem therefore does not prohibit the usual
finite-map encoding of two defining equations.

Poonen's extension result remains compatible: it permits corrections in
large degrees for a fixed subscheme. The hypothetical full W in this
construction has no degree-d corrections at all, as (3) shows. Extending
the reduced map C0→T can consequently introduce additional inverse
support without violating that theorem.

**Stop this construction source.** No degree-six search, replacement
target list or local transverse classification is assigned. A future use
of §3 must verify its actual hypotheses; a construction outside this
source may evade any of them. No claim is made that the characteristic-zero
answer is negative. Both existence and nonexistence remain live.

The source selection used a fresh `gpt-6-astra/xhigh` worker. A fresh
`gpt-6.1-sol/high` reviewer reconstructed the proposed proof and its
generalization, checked the source scopes and challenged the allocation.
The recommendation and stopping rule for this single verification were
reported before it proceeded. The final review confirmed the preserved
statement, including explicit scheme-theoretic factorization and smooth
rational hypotheses. Both workers completed their tasks. No numerical
computation was needed.
