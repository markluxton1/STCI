# Polarization lifting and multiple-quadric matrix defects

Two independently reviewed provisional mechanisms are proved here in full. The first excludes a specified sufficient construction in every degree; the second refutes a universal factorization shortcut. Neither is a reduction of arbitrary STCI pairs or a canonical promotion. Source audits reconstructed the full inverse-image scheme, prime-to-characteristic Picard argument, section-lifting proof and rational-normal generalization; and independently reconstructed the arbitrary-intermediate-bundle matrix proof and all cokernel layers. The characteristic and scheme hypotheses below are essential.

## Polarization and section lifting

### A sufficient construction that creates thickness

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
[contact note](contact_jacobians_and_hamiltonian_actions.md#hamiltonian-actions-in-the-entirely-thick-branch).
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

## Double-quadric matrices and punctual defects

The source counterexample was independently reviewed in characteristic zero. Its determinant, rank-zero, line-subbundle contradiction and cokernel-layer proofs below in fact work over an algebraically closed field of **any** characteristic: they use smoothness of Q, regular parameters, and exact module identities, with no division by two. This characteristic extension is made explicit for review; no characteristic extension of an unrelated carrier theorem is inferred. Set

\[
q=x_0x_3-x_1x_2,\qquad Q=V(q)\subset\mathbf P^3,
\qquad C=[s^4:s^3t:st^3:t^4].
\]

An arbitrary hypothetical supported pair \((F_a,G_b)\) supplies an identity
\(q^N=AF+BG\), hence a homogeneous two-by-two matrix
\(\left(\begin{smallmatrix}F&-B\\G&A\end{smallmatrix}\right)\)
with determinant \(q^N\). Its adjugate gives a matrix factorization of
\(q^N\). This retains the actual two global equations, unlike restriction
to the reduced quadric alone. The standard matrix-factorization/ACM-sheaf
dictionary was checked in [Hartshorne, *Liaison with Cohen–Macaulay
modules*, Appendix, pp. 430–431](https://seminariomatematico.polito.it/rendiconti/64-4/419.pdf).
The following example rejects a potential uniform shortcut: decomposing
every such matrix into matrices with determinant \(q\). It does not reject
a theorem with additional hypotheses specific to \(C\).

## The counterexample

Put \(\ell=x_1\), \(m=x_2\), and consider

\[
M=
\begin{pmatrix}
\ell^2&\ell m+q\\
\ell m-q&m^2
\end{pmatrix}:
\mathcal O_{\mathbf P^3}(-2)^2\longrightarrow
\mathcal O_{\mathbf P^3}^{2}.
\tag{1}
\]

Direct multiplication gives

\[
\det M=\ell^2m^2-(\ell m+q)(\ell m-q)=q^2,
\qquad M\operatorname{adj}(M)=q^2I_2.
\tag{2}
\]

On \(Q\),

\[
\overline M=
\begin{pmatrix}\ell\\m\end{pmatrix}
\begin{pmatrix}\ell&m\end{pmatrix}.
\tag{3}
\]

Its rank-zero **support** is exactly the nonempty finite scheme support

\[
T=Q\cap V(x_1,x_2)
=\{p_0=[1:0:0:0],p_\infty=[0:0:0:1]\}.
\tag{4}
\]

Here \(T\) itself is reduced; the ideal of the rank-zero locus of
\(\overline M\) is \((\ell^2,\ell m,m^2)\), so that locus has additional
scheme structure. Only its support is used below. These are precisely
the two marked endpoints of \(C\).

More precisely, the rank-zero scheme has length three at each point,
since its local ideal is the square of the maximal ideal on the smooth
surface Q.

**Proposition.** The map (1) cannot factor as

\[
\mathcal O(-2)^2\xrightarrow{B}\mathcal E
\xrightarrow{A}\mathcal O^2
\tag{5}
\]

through any rank-two vector bundle \(\mathcal E\) on \(\mathbf P^3\)
when the determinant divisor of each map is exactly the reduced quadric
\(Q\). This includes homogeneous matrix factors of determinant a nonzero
constant times \(q\), with arbitrary compatible twists. The same remains
true after invertible changes of source and target.

**Proof.** Each of \(A|_Q\) and \(B|_Q\) has rank exactly one at every
point. Indeed, its determinant vanishes on \(Q\), so the rank is at most
one. If the rank were zero at a point, all four local matrix entries
would belong to the maximal ideal there. The determinant would belong
to its square, contrary to the fact that a local equation of the smooth
reduced divisor \(Q\) has nonzero differential.

Consequently \(\mathcal L=\operatorname{im}(B|_Q)\subset\mathcal E|_Q\)
and \(\mathcal K=\ker(A|_Q)\subset\mathcal E|_Q\) are line subbundles.
The composition in (5) has rank zero at exactly the zeros of the induced
line-bundle map

\[
\mathcal L\longrightarrow\mathcal E|_Q/\mathcal K.
\tag{6}
\]

If this map is zero, the composition has rank zero everywhere on \(Q\).
Otherwise its zero locus is empty or an effective Cartier divisor on
the integral smooth surface \(Q\). Its support cannot be nonempty and
finite. This contradicts (3)–(4). Source and target isomorphisms preserve
pointwise rank, proving the last assertion. \(\square\)

## What the cokernel measures

Let \(\mathcal M=\operatorname{coker}M\). The injective presentation

\[
0\longrightarrow\mathcal O(-2)^2
\xrightarrow{M}\mathcal O^2
\longrightarrow\mathcal M\longrightarrow0
\tag{7}
\]

makes \(\mathcal M\) an ACM sheaf, maximal Cohen–Macaulay on the double
quadric \(2Q=V(q^2)\). For example, (7) gives
\(H^1(\mathbf P^3,\mathcal M(t))=0\) for every integer \(t\), and its
graded module has projective dimension one over the four-variable
polynomial ring. At the generic point of \(Q\), a matrix entry is a unit
and (2) identifies the cokernel with the ring of \(2Q\). Thus it is
generically free of rank one over \(2Q\).

It is locally free of rank one on \(2Q\setminus T\), but not at either
point of \(T\). At those points all entries in (1) lie in the maximal
ideal, so the cokernel needs two generators, whereas a rank-one free
module needs one. Hence even a two-generator, globally ACM, generically
rank-one module on a multiple smooth quadric can have a finite nonfree
locus. An argument using only extensions of line bundles to \(2Q\)
does not cover it.

One can see the precise defect without classifying modules. Write
\(e_1,e_2\) for the two degree-zero generators of the cokernel, and
\(u=\ell e_1+m e_2\). The two column relations in (1) give

\[
q e_1=-m u,\qquad q e_2=\ell u,\qquad qu=0.
\tag{8}
\]

In sheaf notation these identify

\[
\operatorname{Ann}_{\mathcal M}(q)=\mathcal O_Q(-1),
\qquad q\mathcal M=\mathcal I_{T,Q}(-1),
\tag{9}
\]

and give an exact sequence on \(2Q\)

\[
0\longrightarrow\mathcal O_Q(-1)
\longrightarrow\mathcal M
\longrightarrow\mathcal I_{T,Q}(1)
\longrightarrow0.
\tag{10}
\]

For completeness, restricting (7) to \(Q\), its kernel is generated by
\((-m,\ell)\), with source \(\mathcal O_Q(-3)\). The Tor identification
is \(\operatorname{Tor}_1(\mathcal M,\mathcal O_Q)
=\operatorname{Ann}_{\mathcal M}(q)(-2)\), proving the first identity
in (9). Equation (8) proves the second. Modulo \(u\), the generators
map to \(m,-\ell\), giving the quotient in (10).

Thus the complete ACM object has a natural quadric layer containing
the ideal of two points. That layer is not a line bundle; it also fails
the ACM condition, since
\(H^1(Q,\mathcal I_{T,Q}(-1))\simeq k^2\). Factoring through two simple
quadric determinant maps would force the rank-one bundle composition
(6), which cannot encode this punctual defect.

## Exact consequence for the STCI investigation

The false implication is

\[
\det M=q^N\quad\Longrightarrow\quad
M\text{ factors into }N\text{ rank-two maps with determinant divisor }Q.
\]

It already fails at \(N=2\), without degree enumeration or a carrier
classification. This blocks a general reduction of the multiple-quadric
matrix problem to successive simple-quadric factors.

The example is **not** asserted to arise from a pair supported on \(C\).
In fact its first column
\((x_1^2,x_1x_2-q)=(x_1^2,2x_1x_2-x_0x_3)\) defines
the two lines \(V(x_1,x_0)\) and \(V(x_1,x_3)\) as reduced support.
Its finite defect (4) already lies at the two marked points on \(C\).
A hypothetical STCI matrix has the additional actual column
\((F,G)\), whose common support is exactly \(C\); its nonfree locus is
therefore contained in \(C\), a condition this example also satisfies.
A successful argument must use the stronger actual
column-support condition, its homogeneous twists, and the actual normal
action together. No result here shows that those additional conditions
force a simple-quadric factorization or exclude the matrix.



## Boundary of the finite-pullback result

The line target used to encode an arbitrary pair has degree-d correction equations and does not satisfy H0(I_W(d))=0. The theorem therefore does not prohibit that encoding. Poonen's sufficiently high-degree extension theorem permits correction sections for a fixed subscheme; the hypothetical full W here has none in degree d. Extending a reduced curve map may create additional inverse support. The source exclusion has no degree bound and no uncompleted degree-six search; it is not an exhaustive reduction of possible STCI constructions.

## Characteristic comparison of the two mechanisms

The polarization-lifting theorem requires the rational-normal degree N to be invertible in k, and N|d; it makes no claim when p divides N. For the twisted cubic N=3, the exclusion therefore includes characteristic two. The existing characteristic-two STCI pair shows explicitly that this constructive source is nonexhaustive. No separability hypothesis on the finite ambient map was used: flatness and scheme-theoretic pullback, the prime-to-p root argument, and section lifting are the inputs. If p divides N, the N-th power map on nilpotent units can fail to be injective, so the proof's root rigidity is unavailable.

For the double-quadric matrix, in characteristic two the displayed first column simplifies to (x1²,x0x3), which has the same two-line reduced support; the distinguished column still does not vanish along C0. The matrix becomes symmetric, but its determinant remains q², its rank-zero scheme on Q is still the two length-three fat points, and a factor with reduced smooth determinant Q must still have rank one at every point of Q. Thus the obstruction to two simple determinant factors survives, while supplying no obstruction to the known positive-characteristic STCI pairs.
