# Three complementary coordinate projections and the spectral polynomial

Exploratory calculation, pending independent review. The governing question remains the restriction of M_1 to the full CI realization locus, not sole support. Uses classical Chow form / binary resultant identity for proper CI pairs (see [GKZ Chow forms overview](https://math.berkeley.edu/~bernd/chowforms.pdf) and the established [Chow coefficient dictionary](../../arguments/torus/chow_arrangement_moments.md)). No new vanishing is claimed.

Write [z:x:y:w] and C_(u,v)=[s^4:s^3t:u st^3:v t^4], q=u/v, eta=u^2/v. Three coordinate pairings define rational maps to P^1 x P^1; each is resolved by blowing up the two corresponding disjoint coordinate lines. Their common permutohedral refinement also resolves the consecutive-ratio product map. The first two are the two ruling projections on each Q_q: xy=qzw. The maps on C have degrees 1 and 3 onto graphs of bidegree (1,1), respectively. The third maps with degree 2 onto the graph eta lambda=beta^2 of bidegree (1,2) in ([z:w],[x:y]).

## Homogeneous Chow restriction formulas

For each pairing the joining lines of points in the two complementary coordinate lines form a P^1 x P^1 in Gr(2,4); restriction of the CI Chow form equals the binary resultant of the actual F,G restricted to that joining line. It has bidegree (ab,ab)=(4m,4m). For the first pairing use [a0:a1]=[z:x], [c0:c1]=[y:w]. For the second use [b0:b1]=[z:y], [d0:d1]=[x:w]. For the third use [l0:l1]=[z:w], [h0:h1]=[x:y]. Up to nonzero scalar, the three restrictions are
\[
R_1=a_1^{3m}c_0^{3m}\prod_i(a_1c_0-q_i a_0c_1)^{n_i},
\quad
R_2=b_1^m d_0^m\prod_i(b_1d_0-q_i b_0d_1)^{3n_i},
\]
\[
R_3=l_0^m l_1^m\prod_i(h_1^2 l_0-\eta_i h_0^2 l_1)^{2n_i}.
\]
Check componentwise using the resultant on its parameter P^1: for pairing one the two hyperplane equations restrict to s^3(a0 t-a1 s), t^3(c0 v t-c1 u s); for pairing two to s(b0 u t^3-b1 s^3), t(d0 v t^3-d1 s^3); for pairing three to l0 v t^4-l1 s^4, st(h0 u t^2-h1 s^2). Multiplicativity of the resultant gives the displayed factors including endpoint contributions. The formula holds at cycle level even without CI; for CI each expression is the resultant of the same two homogeneous surfaces in different joining-line families. Boundary factors cannot be dropped from actual homogeneous resultant identities.

## Common center L=V(z,w)

On the Grassmannian chart of lines z=A x+B y, w=C x+D y, normalized Chow form equals 1 at zero. Its quadratic part for a translated cycle is -M_1(AD+3BC). To check: on B=C=0 the first restriction is prod(1-q_i AD)^n_i, and on A=D=0 the second is prod(1-q_i BC)^(3n_i). There are no other quadratic monomials and no linear terms because intrinsic torus weights on A,B,C,D are -1,-3,3,1 (line coordinates transform with weight difference). In particular on A=C=-p,B=D=-r the quadratic term is -4M_1 pr, recovering the existing plane-section Chow coefficient. Thus the 1:3 ruling degrees are precisely the relative weights of the two mixed Hessian terms. This is a cycle-level identity, not a CI consequence. The Hessian vanishes exactly when M_1=0 in characteristic zero.

The source-side simultaneous restriction is the question to pursue: the three resultants are obtained from the same homogeneous F,G, not independent binary pairs. Determine what their common source imposes on the single quadratic coefficient. Do not infer that the resultant factorization itself forces a depressed polynomial: the cycle-level formulas apply to arbitrary translated cycles.

## Product map

The consecutive ratios (alpha,beta,gamma)=(x/z,y/x,w/y) give Q'_q: alpha=q gamma, and the translated graph beta=eta q gamma^2. The two marked base points of the (alpha,gamma) pencil yield the same direction parameters (reciprocal under the opposite local coordinates). The spectral equation homogenizes to bidegree (m,m), and M_1 is its first mixed coefficient normalized at the appropriate marked corner. A homogeneous degree-d source maps on the product torus to F(1,alpha,alpha beta,alpha beta gamma). Its exponent set is the staircase simplex 0<=k<=j<=i<=d in the alpha,beta,gamma exponents, equivalently the pullback of the original degree-d linear system with its boundary constraints. This describes precisely which product equations descend as original homogeneous surfaces, without a carrier choice. The third resultant separately remembers eta, but the full paired transverse Chow polynomial remains necessary to encode correlation of q and eta.
