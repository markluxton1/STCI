# Jacobian sections and opposite-line cofactors

Provisional calculation for the [trace and projection investigation](index.md).
Use its full translated-cycle scope, and write
\(E=k[z,x,y,w]/(F_a,G_b)\), \(d=a+b-2\), and
\(D_{ij}=F_iG_j-F_jG_i\) in the coordinate order \(z,x,y,w\).
Let \(D=Y_{\rm red}\), and write \(\Sigma\) for the annihilator of the
nilradical in \(E\) or its associated sheaf on \(Y\). All four coordinates
are nonzerodivisors in \(E\).

## One differential on each normalized branch

CI adjunction gives \(\omega_Y=\mathcal O_Y(d-2)\). Duality for the
closed immersion \(D\to Y\) identifies \(\Sigma(d-2)=\omega_D\) as
sheaves. The mixed-minor socle identity and purity put all six minors
in \(\Sigma_d\). Relative residue in the chart \(z=1\) identifies
\(D_{12}\) on each normalized reduced branch with \(n_i\,dw\). The
complementary tangent formulas give the other components. [Jacobian and
residue bridge](../../arguments/torus/spectral_jacobian_first_jet_bridge.md).
[Six complementary ambient minors for smooth support](../../arguments/torus/contact_jacobians_and_hamiltonian_actions.md#the-six-ambient-minors-different-and-contact-identity).

Put \(r=t/s\) and let \(\tau_i=n_i\,dr/r\). As rational sections of
\(\omega_D(2)\) on the normalizations, the minors are
\[
 (D_{01},D_{02},D_{03},D_{12},D_{13},D_{23})
       =(yw,-3xw,2xy,4zw,-3zy,zx)\tau.
\]
On the normalization of \(C_{u_i,v_i}\) these are sections of
\(\omega_{\mathbf P^1}\otimes\mathcal O_{\mathbf P^1}(8)\). Their
coefficient and endpoint orders in the degree-six homogeneous
presentation are
\[
 \frac1{n_i}(D_{01},D_{02},D_{03},D_{12},D_{13},D_{23})
  =(u_iv_it^6,-3v_is^2t^4,2u_is^3t^3,4v_is^3t^3,-3u_is^4t^2,s^6).
\]
In particular the first and last span the fibers at the two endpoints,
and these sections generate \(\mathcal O_{\mathbf P^1}(6)\).
The identification describes these specific sections. The normalization
pullback of the dualizing sheaf of the singular \(D\) need not equal the
canonical bundle of a normalized branch.

Because \(x,y\) vanish at both endpoints, \(P=x\tau\) and \(Q=y\tau\)
are regular sections of \(\omega_D(1)\). The CI section dictionary
identifies them with unique classes in \(\Sigma_{d-1}\). The coordinate
expressions give identities in \(E\)
\[
 D_{01}=wQ,\quad D_{02}=-3wP,\quad D_{03}=2yP=2xQ,\quad
 D_{13}=-3zQ,\quad D_{23}=zP,\quad
 4zwP=xD_{12},\quad 4zwQ=yD_{12}.
\]

## Regular quotients of the minors

Rosenlicht's dualizing-sheaf criterion for a rational differential on
the normalization tests its total residues against local regular
functions. For simple poles this is the cancellation of total residues
at each point, since the constant value is shared by all branches.
Thus \((D_{03}-cD_{12})/(zw)\) is regular precisely for
\(c=M_1/(2m)\). Indeed its branch differential is
\(2n_i(q_i-2c)\,dr/r\). This gives the actual identity
\[
 D_{03}=\frac{M_1}{2m}D_{12}+zw\,K,\qquad K\in\Sigma_{d-2}.
\]
The normalized socle \(D_{12}\) is nonzero in both endpoint
section algebras. Consequently \(M_1=0\) is equivalent to divisibility
of \(D_{03}\) by \(z\), by \(w\), or by \(zw\) in \(E\).
The [endpoint-plane responses](endpoint_plane_response.md) give an
independent calculation of the two restrictions using the actual
source sections.

The same residue criterion treats any quotient by a quadratic monomial.
In \(z=1\) write a minor as \(n_i c_i r^e dr\) and a denominator as
\(b_i r^k\). The quotient has endpoint orders \(e-k\) and \(k-e-2\).
The eight logarithmic pairs, in minor/monomial notation, are
\[
 \frac{D_{01}}{yw},\quad\frac{D_{02}}{xw},\quad
 \frac{D_{03}}{xy},\quad\frac{D_{12}}{zw},\quad
 \frac{D_{13}}{zy},\quad\frac{D_{23}}{zx},\quad
 \frac{D_{03}}{zw},\quad\frac{D_{12}}{xy}.
\]
Their total residues at zero are respectively
\(m,-3m,2m,4m,-3m,m,2M_1,4\sum_i n_i/q_i\), with the opposite
signs at infinity. For other orders only local coordinate monomials
of weight \(k-e-1\) at zero or \(e-k+1\) at infinity can contribute
to the test, with a negative target weight giving no condition.
These tests use the branch values of each ambient monomial with its
shared coefficient. The section dictionary identifies regularity of
a quotient with divisibility of its numerator in \(E\). For example,
the uncentered divisibility condition for \(D_{12}/xy\) is inverse
moment balance.

## A Koszul class on the line through the endpoints

The relation \(yP-xQ=0\) gives a class \(\sigma\) in \(H_1(x,y;E)\)
represented by \((-Q,P)\). A homogeneous \(h\in B=k[z,w]\) kills it
precisely when \(hP=xR,\ hQ=yR\) for a homogeneous class \(R\).
Regularity of \(x\) identifies \(R\) with the rational socle section
\(h\tau\), and implies \(R\in\Sigma\). Conversely a regular section
\(h\tau\) gives \(R\) by the section dictionary. In the \(z\)- and
\(w\)-frames its total residues are \(m h(1,0)\) and \(-m h(0,1)\).
Hence \(\operatorname{Ann}_B(\sigma)=(zw)\), also for nonhomogeneous
\(h\) by grading.

Let \(K_{\rm line}=V(x,y)\), \(F_K=F(z,0,0,w)\), \(G_K=G(z,0,0,w)\),
and \(H=\gcd(F_K,G_K)\). These restrictions vanish at both endpoints
and have no common projective zero elsewhere, since the entire support
is translated. They cannot both vanish identically, so \(H\) is a
nonzero scalar times \(z^r w^s\) with \(r,s\ge1\). This includes the
case of one identically zero restriction. The Koszul resolutions
for \((x,y)\) and \((F,G)\) compute the same \(\operatorname{Tor}_1^S(E,B)\),
where \(S=k[z,x,y,w]\). In \(B\) the syzygy module of \(F_K,G_K\)
is generated by \((G_K/H,-F_K/H)\) and boundaries multiply this
generator by \(H\). It follows that
\[
 H_1(x,y;E)\simeq (B/(H))(-(a+b-\deg H)).
\]
Choose homogeneous lifts of \(P,Q\), and write \(yP-xQ=A F+B'G\)
with \(\deg A=b-2\), \(\deg B'=a-2\). The cofactors for these lifts
are unique since any difference is a Koszul relation with multiplier
of degree \(-2\). The restricted pair \((A_K,B'_K)\) represents
\(\sigma\) up to the comparison sign and so is
\(J(G_K/H,-F_K/H)\) for a homogeneous \(J\) of degree \(\deg H-2\).
The annihilator of the class of \(J\) in \(B/(H)\) is
\((H/\gcd(H,J))=(zw)\). Therefore \(J=cH/(zw)\) for some
\(c\in k^*\), and
\[
 A_K=c\,G_K/(zw),\qquad B'_K=-c\,F_K/(zw).
\]
The restrictions are independent of the lifts because changing \(P,Q\)
by \(F,G\) changes the cofactors by terms in \((x,y)\).

## The same sections on the disjoint line

The binary algebra \(E/(z,w)\) has socle degree \(d\). The
trace–Jacobian identity and the equations \(4zwP=xD_{12}\) and
\(4zwQ=yD_{12}\) give
\[
 \operatorname{Res}(xP)=\operatorname{Res}(yQ)=0,\qquad
 \operatorname{Res}(yP)=\operatorname{Res}(xQ)=M_1.
\]
Here the relative traces of \(x^2,y^2\) are zero and the trace of
\(xy\) is \(4zwM_1\), as seen on the generic reduced sheets with
multiplicities. The relative identities specialize at \(z=w=0\).
Perfect residue pairing with degree one identifies the images of
\(P,Q\) in degree \(d-1\) as \(M_1\) times the classes dual to \(y,x\).
Thus these images vanish together exactly when \(M_1=0\).

The prescribed cofactor restriction and the central residue concern
the same two polynomial sections. The present calculation gives no
implication from the cofactors on \(V(x,y)\) to vanishing on \(V(z,w)\).
The [first-order control](first_order_wedge_control.md) tests the
limits of the truncated Jacobian identities.
