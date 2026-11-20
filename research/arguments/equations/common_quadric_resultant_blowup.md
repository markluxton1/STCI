# The local resultant graph is the common-quadric blowup

Use the [clean common-quadric setup](common_quadric_chow_boundary.md):
\(C\sim(1,3)\) smooth on \(Q\), \(a,b\ge3\), over an
algebraically closed field of any characteristic. Put
\[
 X=\mathbf P H^0(\mathcal I_C(a))\times\mathbf P H^0(\mathcal I_C(b)),
 \qquad Z_Q=\mathbf P(QS_{a-2})\times\mathbf P(QS_{b-2}).
\]
At a point \(z=([QA],[QB])\), assume \(A,B\) are coprime, their
restrictions are nonzero, and the restrictions' common divisor has class
\((h_1,0)\). This includes the regular-sequence case \(h_1=0\).
There is a Zariski neighborhood \(U\subset X\) such that
the resultant coefficient ideal is \(I_{\rm res}=J_{Z_Q}^2\), and
the reduced graph closure of the line-resultant map is
\[
                    \Gamma_U\simeq\operatorname{Bl}_{Z_Q\cap U}U.
\]
The exceptional fibre is the projectivization of the actual normal
image \(W_z\) in the [source calculation](common_quadric_chow_boundary.md#normal-cancellation-at-restriction-rank-drops).
For regular restrictions it is the full residual source \(V_Z\).
This describes every generically
proper arc through this neighborhood, including arcs with higher contact
with the center. It is not a global blowup classification.

## The quadratic initial resultant

Let \(J\) define the smooth center \(Z_Q\). The Koszul calculation
identifies its normal space at \(z\) with \(W_z\): a normal pair
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
\(Q\nmid K\), and ambient coprimality makes
\(\operatorname{Res}(A,B)\ne0\). The next calculation identifies
their entire span, rather than only absence of basepoints.

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

## The exact base ideal and graph

The full Veronese followed by a linear inclusion means that these
quadratic coefficient forms span
\(\operatorname{Sym}^2N_z^*=J^2/\mathfrak m_zJ^2\). This holds
also in characteristic two: in \(k\otimes k\), the mixed coordinate
\(a_i a_j\) multiplies \(e_i\otimes e_j+e_j\otimes e_i\), which
remains independent of the diagonal tensors. No division by two occurs.
Since \(I_{\rm res}\subset J^2\), Nakayama applied to
\(J^2/I_{\rm res}\) gives \(I_{\rm res}=J^2\) at \(z\), and
coherence gives this equality after shrinking \(U\).

The closure of the graph of a rational map given by generators of an
ideal on this integral \(U\) is the Proj of its Rees algebra. Thus it
is \(\operatorname{Bl}_{I_{\rm res}}U\). The Rees algebra of \(J^2\)
is the second Veronese of that of \(J\), with the same Proj. Hence
\(\Gamma_U=\operatorname{Bl}_{J}U\), with exceptional fibre
\(\mathbf P(N_z)=\mathbf P(W_z)\) and the map just computed.
This proves the scheme-theoretic statement and identifies the base
scheme itself as the double center.

Consequently the first nonzero normal direction of a lifted arc
determines its exceptional Chow point on this open. A restriction gcd
of class \((h_1,h_2)\) with \(h_2>0\) instead has a nonzero normal
kernel, so its coefficient ideal is not \(J^2\). Its graph, zero
restrictions, common ambient factors and gluing across other strata
remain outside the theorem. Characteristic zero is unnecessary: the
resultant identity is integral, transverse secants exist in every
characteristic, and the Veronese and Rees arguments require no division.

## The center is outside the closure of sole-support pairs

Fix \((a,b)\). If \(m=ab/4\) is not an integer, there is no proper
pair with sole support \(C\). Otherwise take the closed Chow point
\(m[C]\). Every point of the exceptional fibre above \(z\) has cycle
\([V(A,B)]+[V(Q,K)]\), with a positive balanced quadric subcycle.
Such a cycle cannot equal \(m[C]\), by the
[cycle exclusion](common_quadric_chow_boundary.md#cycle-exclusions-even-at-cofactor-restriction-rank-drops).
The inverse image of \(m[C]\) in \(\Gamma_U\) is closed, and its
image in \(U\) is closed because the blowup projection is proper.
That image misses \(z\). Removing it gives a Zariski neighborhood
of \(z\) containing no sole-support proper pair.

Thus the entire \(h_2=0\) locus is outside the closure of the
fixed-degree sole-support locus. Higher contact with the center or a
vanishing first tangent cancellation cannot rescue such a point. This
does not exclude closure of *varying translated cycles*, whose limits
can leave the exact Chow-polytope fibre; that is a different closed-set
question.

## Which hypotheses the graph calculation needs

More generally let \(C\) be an effective Cartier divisor of class
\((r,s)\) on a smooth quadric, with \(r,s\ge0\). Smoothness of
\(C\) is not used here. Keep \(a,b\ge3\), regular cofactor
restrictions, and positive normal rank. The normal source is
\[
 N_z=H^0\mathcal O_Q(a-r,a-s)\oplus
                         H^0\mathcal O_Q(b-r,b-s).
\]
Its cancellation kernel is \(H^0\mathcal O_Q(2-r,2-s)\).
If this group vanishes, equivalently \(\max(r,s)\ge3\), the
source injects into the residual section space. The secant calculation
works on **any** subspace, so it still gives \(I_{\rm res}=J^2\)
and the ordinary local blowup with exceptional fibre \(\mathbf P(N_z)\).
Surjectivity onto the full residual source is unnecessary.

Vanishing also of \(H^1\mathcal O_Q(2-r,2-s)\) ensures that the
source is the entire residual space. This holds when \(r=3\),
\(s=3\), or both \(r,s\ge3\). If this \(H^1\) is nonzero,
the cokernel is its kernel under the next Koszul cohomology map; it
must not be identified with the whole group without checking that map.
The balanced-class comparison separately requires an unbalanced integral
\(C\). For balanced \(r=s\) that class comparison gives no exclusion;
regular cofactor restrictions still supply the independent positive
off-quadric component \(V(A,B)\).

## Reduced support at the remaining cancellation directions

For the integral \((1,3)\) curve, assume only ambient coprimality of
\(A,B\), and that at least one cofactor does not contain \(C\).
Then locally at \(z\),
\[
                         \sqrt{I_{\rm res}}=J_{Z_Q}.
\]
Indeed the projective common-factor incidence map is proper for each
of the finitely many possible factor degrees. A common factor at \(z\)
divides \(\gcd(QA,QB)=Q\), so only degree two can occur near \(z\).
Within that incidence, the closed locus where both cofactors contain
\(C\) has proper image missing \(z\); remove it too. For any remaining
factorization \((HA',HB')\) through the integral \(C\), either
\(H\) contains \(C\) or both cofactors do. The second case was
removed; uniqueness of the containing quadric gives \(H=Q\).

Thus positive-\(h_2\) cases satisfying this hypothesis have additional
infinitesimal resultant-base structure on the **same reduced center**,
despite \(I_{\rm res}\ne J^2\). If both cofactors contain \(C\),
varying the common quadric with the cofactors fixed produces other base
points through \(C\); the reduced-center conclusion is not asserted.
This does not identify the higher-order ideal or its blowup.

The independent correctness review reconstructed the initial resultant,
secant/Veronese immersion, exact square-ideal statement and scheme-theoretic
graph identification, the ruling-gcd extension and local closure
exclusion. Separate geometric review checked the Cartier-class
generality and the distinction between an injective and a full source.
The reduced-center statement received independent correctness review
under its separate cofactor-containment hypothesis.
