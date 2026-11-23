# The first moment as a marked boundary class

**Status.** Application of the classical generalized Jacobian of a rational
curve with modulus. The generalizations and algebraic-geometry reviewers
independently checked the coordinate calculation and norm criterion;
the literature review checked the classical attribution. This is not a proof of UM1.

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

## 2. The missing complete-intersection bridge

Ordinary rational equivalence imposes no first-jet condition. For example,
\((T-q)/T\) has divisor \([q]-[0]\), but equals \(1-qz\) at infinity.
With only the reduced modulus \(\infty\), every normalized degree-zero
relation is already trivial; \(2\infty\) is the first level detecting
this additive invariant.

The [intrinsic spectral account](quadric_pencil_spectral_intrinsic_geometry.md#2-the-spectral-form-is-the-unique-divisor-equation-on-the-quadric-pencil)
pushes the cycle to the pencil line. To prove UM1, an actual CI relation
must additionally supply the first-order trivialization in (BM2).
Neither ordinary Cartier equivalence on a carrier nor Hodge equality alone
establishes that compatibility. Exceptional and conductor corrections of a
proposed pushforward must be retained.

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
Ramification is allowed. No such construction is established for arbitrary
translated-support CIs; (BM3) specifies the missing datum rather than
asserting it exists.

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
It leaves compatibility with actual equation-source and carrier relations
unproved. It is an exact reformulation of the coefficient, not an
independent obstruction or a proof of universal depression.
