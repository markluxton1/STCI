# The K3 marked-lattice obstruction

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed the displayed marked ADE correction, rank-19 budget and index-two/four/eight cases. Inherited inputs are the stated ADE/Milnor-lattice inputs and established first-graph model; this supplementary lattice argument is distinct from ML1–ML9.

Use the [two-blowup dictionary](blowup_residual_geometry.md#the-two-blowups-and-their-actual-global-section-dictionary) and [marked correspondence](blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary) for the global setup. The SC formulas are in [finite transfer](first_graph_finite_transfer.md#socle-defects-on-the-two-presentations-of-the-first-graph), and ML1–ML9 are in [marked-line geometry](marked_line_local_geometry.md#the-marked-line-excludes-primitivity-at-the-mixed-sextic-boundary). This account owns the supplementary lattice proof and its local correction mechanism.

### A K3 marked-lattice obstruction to the primitive graph row

The image in \(V_5\) changes the useful singularity budget.
A degree-two Cartier divisor there is anticanonical, so
its smooth deformation is a K3 surface, rather than the
large-degree hypersurface occurring in the original
projective space.

**Supplementary marked-lattice argument (covered by the scoped correctness review above).** The stronger [marked-line theorem ML1--ML9](marked_line_local_geometry.md#the-marked-line-excludes-primitivity-at-the-mixed-sextic-boundary) excludes its primitive mixed premise without the ADE hypothesis. The following independent lattice calculation is retained for its reusable local correction mechanism, not as a still-open worse-singularity alternative in this primitive row.
Suppose an actual characteristic-zero \((6,8;2,2)\)
sole-support pair lies in the primitive row of SC1
(mixed direction, \(\ell=3\)). Then its degree-two image
carrier \(U=(P=0)\subset V_5\) must have a singularity
along \(\Delta\) worse than Du Val.
This conclusion does not assume global normality of \(U\)
or any restrictions on singularities away from the marked
quintic. It excludes the whole primitive graph row with
only smooth or Du Val marked points on the smaller image
carrier, not the two nonprimitive graph rows.

**Proof.** The actual original sextic is integral, by
the independent low-degree factor exclusion (each factor
would have degree at least five), hence its image carrier
is integral. Assume \(U\) is normal and smooth or Du Val
in a neighborhood of \(\Delta\), as it would be under
the hypothesis to be contradicted.
The SC3--SC4 comparison gives an image CI \(Z\) of
multiplicity \(8\) with first free conormal slope \(4\)
and full top defect \(6[z]\).
The ambient normal bundle degree on the quintic is
\(\deg N_{\Delta/V_5}=8\), by adjunction and
\(K_{V_5}=-2M\). The scalar first-symbol divisor of
\(U\) on \(\Delta\) has degree \(2M\cdot\Delta-8+4=6\).
It is denoted \(A\), retaining every on-curve singular
point with its multiplicity. The image CI is primitive
at every point other than \(z\). By the actual
power--socle formula on a smooth threefold, every
singular point of \(U\) on \(\Delta\setminus\{z\}\)
has local Cartier index \(8\). At the marked point,
write \(r\) for the actual local index and \(a_z\) for
the first-symbol order. Smoothness is impossible there
because the CI is nonprimitive. Thus \(r\in\{2,4,8\}\)
and
\[
 6=(8/r-1)a_z+(8/r)D_{r,z},\qquad
  \sum_{P\in\Delta}a_P=6.
\]
In particular \(a_z=2\) if \(r=2\), and \(a_z\) is
positive even if \(r=4\).

On the normalization of \(U\) the actual mate gives
\(8\Delta\sim4M\) with \(M^2=10\) and \(M\Delta=5\).
There is no extra inverse branch, since the normalization
is an isomorphism along \(\Delta\). Hodge equality, or
intersection with the actual Cartier multiple, gives
\(\Delta_{\rm num}^2=5/2\).
On a resolution that is minimal above its marked ADE
points, the smooth strict transform of \(\Delta\) has
square \(-2\): its canonical intersection is zero
because \(\omega_U\cong\mathcal O_U\) and the resolution
is crepant near \(\Delta\), and all other exceptional
curves are disjoint from it.
Consequently the total local numerical-pullback
correction is
\[
 \sum_{P\in\Delta}\gamma_P=9/2 .                         \tag{SC5}
\]
Here \(\gamma_P=-R_P^2\) where \(R_P\) is the exceptional
part of the Mumford numerical pullback over \(P\).
The actual order of the class of \(\Delta\) at \(P\)
is the order of \(R_P\) modulo the integral ADE lattice.
Thus if the order is \(2\), then
\(\gamma_P\in\frac12\mathbb Z\), since the exceptional
lattice is even.

We can use the rank bound 19 for the sum of the
marked ADE lattices even if \(U\) has worse
singularities elsewhere. Indeed a general pencil in the
basepoint-free \(|2M|\) smooths \(U\) to a smooth
anticanonical K3 surface (adjunction, Kodaira vanishing
and Bertini). Choose the second pencil section nonzero
at the finitely many marked ADE points. In disjoint
small Milnor neighborhoods these induced smoothings
carry the negative definite ADE vanishing lattices
(the classical Milnor lattice of a simple surface
singularity, equivalently Brieskorn's simultaneous
resolution). Their intersection pairing in the global
smooth fiber is the orthogonal sum of the local
pairings. Nondegeneracy gives injectivity on the span
in homology. The K3 intersection form has signature
\((3,19)\), so their total rank is at most 19.
This smoothing proof uses only the local isolated ADE
germs at the chosen points, not simultaneous resolution
of any non-ADE singularities elsewhere. Over any
algebraically closed characteristic-zero field the
finite carrier, curve and local-type data descend to a
complex model. For classical ADE and K3 lattice inputs,
see [Shimada, *On normal K3 surfaces*](https://www.math.sci.hiroshima-u.ac.jp/shimada/preprints/normalK3/normalK3.pdf)
and the classical Brieskorn lattice theorem as recalled in
[Frenkel--Givental--Milanov, §3.3](https://math.berkeley.edu/~giventh/papers/fgm-ade.pdf)
(the local simple-singularity/vanishing-lattice theorem
is the input, not a new classification).

For local index eight, only \(A_{N-1}\) is possible
(the D and E discriminant groups have exponent at
most four). For a smooth marked branch of type
\(A_{N-1}^j\), the standard chain formulas give
\[
 r_P=N/\gcd(N,j),\quad
 a_P=\min(j,N-j),\quad
 \gamma_P=j(N-j)/N .
\]
The smooth-branch contact formula is the one in
[Ellia, Definition 8 and Lemmas 9--10](https://arxiv.org/abs/1409.3801);
the index and square are also immediate from the
inverse chain matrix. In particular for index eight
write \(N=8g\). Then
\[
 (a_P,\gamma_P)=(g,7g/8)\quad\hbox{or}\quad(3g,15g/8).
\]
Its rank \(8g-1\) is at least \(7g\). Thus if
\(G=\sum_{r_P=8}g_P\), the rank budget gives \(G\le2\).

* If \(r=8\) at \(z\), all marked singularities have
  index eight. Their total correction is at most
  \(15G/8\le15/4<9/2\), contradicting SC5.
* If \(r=2\), \(a_z=2\). The other contacts sum to
  four; by \(G\le2\) this is only two \(A_7\) points
  with contacts one and three. They contribute
  \(11/4\) to SC5, requiring \(\gamma_z=7/4\),
  impossible for index two on an even lattice.
* Suppose \(r=4\). If \(a_z=6\) there are no other
  marked singularities, and \(\gamma_z=9/2\).
  An A-type index-four smooth marked branch has
  \(N=4g,\ a_z=g,\ \gamma_z=3g/4\), requiring
  \(N=24\) and rank 23. A D-type index-four class
  occurs only in odd \(D_n\); its discriminant
  square correction is \(n/4\bmod 2\), an odd
  quarter, not \(9/2\bmod2\). The E groups have
  no elements of order four.
  If instead \(a_z=2\) or \(4\), the other contacts
  sum to four or two. Their parity and \(G\le2\)
  force \(G=2\), contributing respectively \(11/4\)
  or \(7/4\). The required correction at \(z\)
  is respectively \(7/4\) or \(11/4\).
  The other ADE ranks total at least 14, leaving
  rank at most five at \(z\). An A-type index-four
  point of rank at most five must be \(A_3\) and
  has contact one, not the required even value.
  The only D-type possibility is \(D_5\), whose
  order-four class has correction \(5/4\bmod2\).
  Neither required correction has that residue.
  This exhausts the remaining case.

For the D-type discriminant formula, use the positive
root lattice \(D_n=\{x\in\mathbb Z^n:\sum x_i\ \text{even}\}\)
with the Euclidean form. For odd \(n\) the two order-four
cosets are represented by the half-integral spinor
vectors with all entries of absolute value \(1/2\);
their squared norm is \(n/4\bmod2\). Negating the
exceptional lattice and then taking the correction
\(-R_P^2\) gives exactly the sign used above.
This last check does not require identifying a
particular D-type marked branch with an end of its
resolution diagram.

All possible indices at \(z\) contradict the
marked ADE assumption. \(\square\)

This illustrates an important general improvement:
the use of the smoothing's negative rank and the
actual local discriminant square can be combined with
a *punctual* socle transfer, rather than merely with
a genus or global singularity count. The K3 rank here
is a property of the ambient Fano-side linear system,
not an accidental bound on a particular sextic.
The lattice argument alone does not prove normality at the marked point
or exclude worse-than-Du-Val marked germs. In the mixed primitive premise,
the stronger marked-line obstruction already excludes the graph lift without
an ADE assumption; endpoint and nonprimitive strata retain their separate gaps.

