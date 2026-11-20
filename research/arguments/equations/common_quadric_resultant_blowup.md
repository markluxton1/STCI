# The local resultant graph is the common-quadric blowup

Use the [clean common-quadric setup](common_quadric_chow_boundary.md):
\(C\sim(1,3)\) smooth on \(Q\), \(a,b\ge3\), over an
algebraically closed field of any characteristic. Put
\[
 X=\mathbf P H^0(\mathcal I_C(a))\times\mathbf P H^0(\mathcal I_C(b)),
 \qquad Z_Q=\mathbf P(QS_{a-2})\times\mathbf P(QS_{b-2}).
\]
At a point \(z=([QA],[QB])\) where \(A|_Q,B|_Q\) are a regular
sequence, there is a Zariski neighborhood \(U\subset X\) such that
the reduced graph closure of the line-resultant map is
\[
                    \Gamma_U\simeq\operatorname{Bl}_{Z_Q\cap U}U.
\]
The exceptional fibre is \(\mathbf P(V_Z)\), with \(V_Z\) the full
residual source in the linked proof. This describes every generically
proper arc through this neighborhood, including arcs with higher contact
with the center. It is not a global blowup classification.

## The initial resultant resolves on the ordinary blowup

Let \(J\) define the smooth center \(Z_Q\). The Koszul isomorphism
identifies its normal space at \(z\) with \(V_Z\): a normal pair
\((F_1,G_1)\) goes to \(k=(BF_1-AG_1)|_Q/s_C\). On a line,
the initial resultant is
\[
 \operatorname{Res}(QA+tF_1,QB+tG_1)
   =\pm t^2\operatorname{Res}(A,B)\operatorname{Res}(Q,K)+O(t^3),
 \qquad K=BF_1-AG_1.
\]
For a general line with disjoint roots of \(Q,A,B\), the two roots
of \(Q\) move by \(-tF_1/(Q'A)\). The values of the second
equation there are \(-tK/A\). Contributions from the roots of \(A\)
supply \(\operatorname{Res}(A,Q)\operatorname{Res}(A,B)\), cancelling
the denominator \(\operatorname{Res}(Q,A)\). This proves the identity
on a dense open and hence polynomially, including repeated cofactors.

All resultant coefficients lie in \(J^2\). Their quadratic initial
forms have no projective normal basepoint: nonzero \(k\) gives
\(Q\nmid K\), and regular restrictions make
\(\operatorname{Res}(A,B)\ne0\). On the ordinary blowup, factor
\(\mathcal O(-2E)\) from the pulled-back coefficient ideal. The
remaining ideal is a unit near the entire fibre over \(z\). Its
failure locus has closed image under the proper blowup map; removing
that image shrinks \(U\) so the map is resolved throughout its inverse
image. This also removes any additional base locus outside the center.

## The exceptional map is a closed immersion

For any subspace \(V\subset H^0(Q,\mathcal O_Q(r,s))\), the map
\(\mathbf P(V)\to\operatorname{Chow}\) taking a section to its
divisor is a closed immersion, even for reducible or nonreduced divisors.
To see the scheme structure, write points of \(Q\) as
\(x=(u,v),y=(u',v')\). Pull the Chow form back along the dominant
secant-line map. Up to scalar it is
\[
                [u,u']^s[v,v']^r\, k(x)k(y).
\]
On transverse secants the vanishing is exactly \(k(x)k(y)=0\).
The remaining divisorial loci are pairs in a common ruling; degrees
force the fixed factors displayed. Pullback on Chow-form sections is
injective by dominance. Cancelling that fixed factor identifies the
map with \(k\mapsto[k\otimes k]\), the quadratic Veronese followed
by a linear inclusion. This is a closed immersion in every characteristic.
Fixed basepoints of \(V\) cause no change.

The exceptional map here multiplies that divisor Chow form by the fixed
nonzero Chow forms of \(V(A,B)\) and \(C\). Multiplication is a
linear injection, so each exceptional fibre still maps by a closed
immersion.

## Identification with the reduced graph

The resolution gives a proper map \(B=\operatorname{Bl}_{Z_Q\cap U}U
\to\Gamma_U\), an isomorphism away from the center. On each
exceptional fibre it is the immersion just proved. It is therefore
geometrically injective and quasi-finite. Any tangent kernel lies in
the tangent space of a fibre of \(B\to U\), and the fibre immersion
makes that kernel zero. Thus the map is unramified and radicial.
Properness makes it finite, and a proper unramified radicial morphism
is a closed immersion. Its image contains the dense graph. Since the
target graph closure is reduced, this closed immersion is an isomorphism.

Consequently the first nonzero normal direction of a lifted arc
determines its exceptional Chow point on this open. Rank-drop points
of \(A|_Q,B|_Q\), other common factors and gluing across those strata
remain outside the proof. Characteristic zero is unnecessary: the
resultant identity is integral, transverse secants exist in every
characteristic, and the Veronese and scheme arguments require no division.

The independent correctness review reconstructed the initial resultant,
secant/Veronese immersion, neighborhood argument and scheme-theoretic
graph identification after the geometric review proposed the strengthening.
