# The first moment as a marked boundary class

**Status.** Application of the classical generalized Jacobian of a rational
curve with modulus. The generalizations and algebraic-geometry reviewers
independently checked the coordinate calculation and norm criterion;
the literature review checked the classical attribution. The November 23
carrier reassessment and independent generality review reconstructed
the ordinary carrier norm, its extension to every actual translated-support
pair, and the boundary-trace formula below. This is not a proof of UM1.

## 1. Depression is a first-order boundary trivialization

Let \(k\) be algebraically closed, in any characteristic, and retain the
distinguished spectral line \(P=\mathbf P^1_T\), points \(0,\infty\),
and parameter \(z=1/T\) at infinity. Its degree-zero divisor class group
with modulus \(2\infty\) is
\[
 J(P,2\infty)(k)=
 \frac{\operatorname{Div}^0(P\setminus\{\infty\})}
 {\{\operatorname{div}(f): f\equiv1\pmod{z^2}\text{ at }\infty\}}.
                                                               \tag{BM1}
\]
For \(D=\sum_j e_j[c_j]\), \(\sum e_j=0\), its unique rational
function of divisor \(D\) and value one at infinity is
\[
 f_D(T)=\prod_j(T-c_j)^{e_j}
       =\prod_j(1-c_jz)^{e_j}
       =1-\Big(\sum_j e_jc_j\Big)z+O(z^2).
\]
Uniqueness follows since two functions of the same divisor differ by a
constant. Multiplication of these normalized functions adds their linear
coefficients, so
\[
 \operatorname{aj}_1(D)=-[z]f_D=\sum_j e_jc_j
\]
is a homomorphism. Its kernel is precisely the denominator in (BM1), and
\([c]-[0]\) maps to \(c\). Hence \(J(P,2\infty)(k)\simeq(k,+)\)
with this sign convention. The generalized-Jacobian construction is
classical; the calculation proves the particular identification used here.

For the translated cycle \(\sigma=\sum_i n_i[C_{u_i,v_i}]\), put
\(q_i=u_i/v_i\), \(m=\sum n_i\), and
\(D_\sigma=\sum_i n_i[q_i]\). Its spectral polynomial satisfies
\[
 \frac{H_\sigma(T,1)}{T^m}=1-M_1z+O(z^2),\qquad
 \operatorname{aj}_1(D_\sigma-m[0])=M_1.             \tag{BM2}
\]
Consequently these three assertions are equivalent:

1. \(H_\sigma\) is depressed in its distinguished coordinate.
2. \([D_\sigma-m[0]]=0\) in \(J(P,2\infty)(k)\).
3. Its unique normalized ordinary divisor trivialization is one modulo
   \(z^2\) at infinity.

Repetitions are included. In positive characteristic the multiplicities
in the additive coordinate are interpreted in the field.

The reference point matters: replacing \(m[0]\) by \(m[c]\) changes
the invariant to \(M_1-mc\). Thus arbitrarily translating a polynomial
to depress it changes the marked condition. Scaling the spectral coordinate
scales the invariant and preserves its zero locus.

## 2. An actual carrier relation supplies an ordinary norm

Ordinary rational equivalence imposes no first-jet condition. For example,
\((T-q)/T\) has divisor \([q]-[0]\), but equals \(1-qz\) at infinity.
With only the reduced modulus \(\infty\), every normalized degree-zero
relation is already trivial; \(2\infty\) is the first level detecting
this additive invariant.

Work in characteristic zero, with
\([z:x:y:w]=[x_0:x_1:x_2:x_3]\). First let \(S=V(F_a)\) be an
integral carrier containing no line of the pencil base locus
\(V(xy,zw)\). Suppose \((F_a,G_b)\) is a proper pair with entire
cycle \(\sigma=\sum_i n_i[C_{u_i,v_i}]\), so \(ab=4m\).
No normality or generic regularity of the carrier is assumed.

Choose a general integral hyperplane curve \(\Gamma\subset S\)
avoiding \(S\cap V(xy,zw)\) and the translated curves' endpoints.
Irreducibility is [Bertini](https://stacks.math.columbia.edu/tag/0G4C);
the hyperplane section of the integral hypersurface is Cohen--Macaulay
and generically reduced, hence integral. Let
\(\nu:\widetilde\Gamma\to\Gamma\) be its normalization. This is
a smooth proper curve, and the pencil gives a finite map
\[
 p=(xy/zw)\nu:\widetilde\Gamma\longrightarrow P,
 \qquad \deg p=2a.
\]
Indeed its two sections have no common zero and generate
\(\nu^*\mathcal O_\Gamma(2)\), of degree \(2a>0\).

Normalization preserves the required Cartier zero-cycle, even at
singular points of \(\Gamma\). Locally, let \(A\subset B\) be
the finite normalization of its one-dimensional local ring and
\(Q=B/A\). For a nonzero local Cartier equation \(f\), the exact
sequence is
\[
0\longrightarrow Q[f]\longrightarrow A/fA
 \longrightarrow B/fB\longrightarrow Q/fQ\longrightarrow0.
\]
Multiplication by \(f\) on the finite-length module \(Q\) has
kernel and cokernel of equal length. Thus the Cartier length downstairs
equals the sum of the normalized orders upstairs. This is also the
degree-one case of [Cartier-divisor pushforward](https://stacks.math.columbia.edu/tag/02ST).

Put \(g=\nu^*((G_b/x^b)|_\Gamma)\). Its numerator divisor has
total multiplicity \(4n_i\) over each \(q_i=u_i/v_i\). Its
denominator has degree \(ab\) and is supported over \(0\):
a point with \(x=0\) outside the base locus has \(xy/zw=0\).
The endpoints were excluded, so these divisors are disjoint. Hence
\[
 p_*\operatorname{div}(g)
   =4D_\sigma-ab[0]=4(D_\sigma-m[0]).                 \tag{BM4}
\]
The function \(g\) is a unit over \(\infty\).
[Norms push forward principal divisors](https://stacks.math.columbia.edu/tag/02RS);
after normalizing their value at infinity, uniqueness
of the rational function of the displayed divisor gives
\[
 \frac{\operatorname{Nm}_p(g)}{\operatorname{Nm}_p(g)(\infty)}
 =\frac{H_\sigma(T,1)^4}{T^{4m}}
 =1-4M_1z+O(z^2).                                    \tag{BM5}
\]
This constructs the ordinary norm without a surface-normalization
descent assumption: the mate section already exists downstairs.

### Every actual pair has such a product of norms

Now let \((F_a,G_b)\), \(a\le b\), be any proper pair with the
entire translated cycle \(\sigma\). Neither generator need be
integral or avoid the four pencil base lines. Choose
\[
 K_b=G_b+F_aL,\qquad L\in H^0(\mathcal O(b-a)),
\]
containing none of those lines. Such a choice exists: if \(F_a\)
vanishes identically on a base line, \(G_b\) does not, since the
line is absent from the entire intersection support. Otherwise the
condition \(G_b+F_aL=0\) on that line is a proper affine linear
condition on \(L\). Finitely many proper affine subspaces do not
cover this parameter space over \(k\).

Factor \(K_b=\prod_j H_j^{e_j}\) into integral factors. Every
carrier \(V(H_j)\) avoids the base lines and has a proper mate
\(F_a\), with translated subcycle \(\sigma_j\). Cartier-intersection
additivity gives \(\sigma=\sum_j e_j\sigma_j\), including all
generic multiplicities. Apply the preceding construction to a normalized
general hyperplane curve \(\widetilde\Gamma_j\subset V(H_j)\),
with \(p_j=xy/(zw)\) of degree \(2\deg H_j\) and
\(g_j=F_a/x^a\). Multiplying the normalized norms to powers \(e_j\)
gives exactly
\[
 \prod_j\left[
 \frac{\operatorname{Nm}_{p_j}(g_j)}
      {\operatorname{Nm}_{p_j}(g_j)(\infty)}
 \right]^{e_j}
       =\frac{H_\sigma(T,1)^4}{T^{ab}}.
\]
Thus every actual translated-support CI has an ordinary norm relation,
including entirely-thick generic intersections. On a fixed carrier
containing a base line a direct pencil calculation still needs its
exceptional corrections; homogeneous row replacement and factorization
remove that coverage restriction for the all-pair question.

There is a precise local expression for that term. Over the completed
local ring \(k[[z]]\) at infinity, \(p_*\mathcal O_{\widetilde\Gamma}\) is
finite free. In any basis write multiplication by \(g\) as
\(U(z)=U_0+zU_1+O(z^2)\), with \(U_0\) invertible. Expanding its
determinant and using (BM5) gives
\[
 \boxed{\quad4M_1=-\operatorname{Tr}(U_0^{-1}U_1).\quad} \tag{BM6}
\]
For the product construction, use the direct sum of these multiplication
operators, repeating the \(j\)-th block \(e_j\) times. Formula (BM6)
then holds for the aggregate trace. Ramification is allowed. The trace
is independent of the chosen bases, since it is the normalized product
of norms' first coefficient.

On the same actual translated-cycle incidence, the [source first-jet
formula](chow_hilbert_symplectic_form.md#1-an-exact-pullback-formula)
has \(\Theta(F,G)=2M_1\). Therefore the aggregate boundary trace
in (BM6) is exactly \(-2\Theta(F,G)\). Computing this scalar again
adds no new test. A proof of UM1 through the boundary must establish a
geometric cancellation or reciprocity constraint on this existing jet.

## 3. Sufficient pointwise trivializations and the remaining boundary

A precise sufficient norm construction is the following. Suppose smooth
proper curves \(\Gamma_j\) have finite maps \(p_j:\Gamma_j\to P\)
and rational functions \(g_j\) such that
\[
 g_j\equiv1\pmod{2p_j^*(\infty)},\qquad
 \sum_j(p_j)_*\operatorname{div}(g_j)
       =N(D_\sigma-m[0]),\qquad N\ne0.
                                                               \tag{BM3}
\]
Their norms have the displayed pushed-forward divisors. On the completed
local ring at infinity, the finite pushforward is free and multiplication
by \(g_j\) is the identity modulo \(z^2\); its determinant is therefore
one modulo \(z^2\). The product of norms proves \(NM_1=0\), hence
\(M_1=0\) in characteristic zero (or when \(N\) is invertible in \(k\)).
Ramification is allowed. These pointwise congruences are stronger than
necessary: the product of the normalized norms need only be one modulo
\(z^2\). For every actual pair Section 2 constructs the ordinary norm
relation, but neither the pointwise congruence in (BM3)
nor the weaker aggregate cancellation in (BM6) has been proved in
general. Ordinary Cartier equivalence or Hodge equality alone does
not supply that first-order compatibility. Constructing a mate from
upstairs data on a nonnormal carrier still requires its full conductor;
that descent problem is not a condition omitted from the norm of an
already existing downstairs section.

In characteristic zero the higher boundary jets are related by
\[
 \log(H_\sigma(T,1)/T^m)
       =-\sum_{j\ge1}\frac{\sum_i n_iq_i^j}{j}z^j.
\]
Triviality modulo \(z^{r+1}\) is equivalent to the first \(r\) power
sums vanishing. This identifies higher retained information; it predicts
no higher universal CI vanishings and imposes no classification requirement
on the first-moment investigation.

## Sources and scope

Kahn–Saito–Yamazaki, [*Reciprocity sheaves I*](https://webusers.imj-prg.fr/~bruno.kahn/preprints/rec-7.1.pdf),
introductory Theorem 1 and §9.4, Proposition 9.7, give the classical
modulus reciprocity and generalized-Jacobian framework. See also
Binda–Cao–Kai–Sugiyama, [*Torsion and divisibility for reciprocity sheaves
and 0-cycles with modulus*](https://arxiv.org/abs/1503.02161), introduction.
The literature review checked these applicability statements; no novelty
claim for generalized Jacobians or reciprocity is made.

This interpretation supplies a concrete additive target retaining the
marked boundary, improving the formulation of the
[open divisor-functional route](universal_first_moment_corpus_review.md#2-supported-divisor-cycles-and-class-group-relations-a-distinct-route).
The ordinary norm relation exists for every actual translated-support
pair by Section 2; its aggregate first-jet cancellation remains unproved.
Thus the marked
boundary class is an exact reformulation of the coefficient and an
explicit comparison target, not a proof of universal depression.
