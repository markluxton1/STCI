# Independent audit: intrinsic (4,4) exclusion by the K3 exceptional lattice

Date: 2026-10-23. Reviewer: independently delegated adversarial audit agent.

Status: **the reconstructed argument passes this independent mathematical audit**, with the precise hypotheses and local details below. This is an audit of a new proposal, not a canonical promotion. It does not use the previously accepted quartic-carrier exclusion, the previous quartic coefficient classification, or the earlier filtered \(4,4\) proof.

Reviewed documents: [the principal proof proposal](2026-10-23-intrinsic-44-k3-proof-proposal.md) and [the supporting local-algebra note](2026-10-23-intrinsic-quadruple-local-algebra.md). The reconstruction below was completed independently and then compared against both actual files. No mathematical discrepancy was found.

## Exact scope and inputs

Let \(k\) be algebraically closed of characteristic zero. Let \(C=C_0\subset\mathbf P^3_k\) be the fixed smooth rational quartic, with \(\mathcal O_C(1)=\mathcal O_{\mathbf P^1}(4)\) and balanced conormal

\[
E=I_C/I_C^2=\mathcal O_{\mathbf P^1}(-7)^{\oplus2}.
\]

Suppose that two quartics \(F,G\) have sole reduced intersection support \(C\). This supposition implies that \(F,G\) have no common surface factor, that \(Z=V(F,G)\) is a Cohen--Macaulay complete-intersection curve, that its degree is 16, and that its generic transverse length along \(C\) is four. Adjunction gives \(\omega_Z=\mathcal O_Z(4)\).

The initial noncurvilinear branch requires the elementary quadric input: \(C\) lies on a smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\) with class \((3,1)\), up to interchange, and \(Q\) is the only quadric through \(C\). This input can be checked directly from the fixed parametrization; it is not an exclusion theorem.

If a quartic has generic normal order at least two along \(C\), its first conormal symbol is zero everywhere, because it is a section of a vector bundle on the integral curve \(C\). Hence it belongs to the sheaf square \(I_C^2(4)\). Its restriction to \(Q\) would lie in \(H^0(\mathcal O_Q(4,4)-2C)=H^0(\mathcal O_Q(-2,2))=0\), so it is \(qH\), where \(q\) defines \(Q\). The order-two condition forces the quadric \(H\) to vanish on \(C\), and consequently this quartic is a scalar multiple of \(q^2\). A proper pair containing \(q^2\) cannot have sole reduced support \(C\): a mate not divisible by \(q\) cuts a divisor of class \((4,4)\) on \(Q\), which cannot have sole support the divisor \(C\) of class \((3,1)\); a mate divisible by \(q\) gives a common surface. This eliminates the transverse Hilbert function \((1,2,1)\) and any order-two member of the hypothetical pencil. The remaining generic algebra is curvilinear of length four.

The review below reconstructs the filtration and local statements directly. It does not import an unproved global retraction or a classification of embedded multiple curves.

## Finite flatness and the saturated pairing

At a closed point \(p\in C\), choose a formal parameter \(t\) on \(C\) and an ambient lift. Put \(R=k[[t]]\). The completed algebra \(B=\widehat{\mathcal O}_{Z,p}\) is finite over \(R\), since its reduction is \(R\) and its nilradical is nilpotent. It is torsion free over \(R\): \(Z\) is Cohen--Macaulay with sole reduced component \(C\), so this parameter is a nonzerodivisor. It is therefore free of rank four. The map \(R\to B\) is only a local coefficient choice, and no global splitting is used.

Let \(J\subset B\) be the nilradical. For \(i=1,2,3\), define \(N_i=B\cap J_K^i\subset B_K\simeq K[u]/(u^4)\), where \(K=k((t))\). These are the saturated nilpotent powers; \(N_1=J\). All the successive quotients \(N_i/N_{i+1}\) are free of rank one over \(R\).

Choose a filtered basis \(1,x,y,z\), with \(x\in N_1\), \(y\in N_2\), and \(z\in N_3\). Generically, and hence in the torsion-free algebra,

\[
x^2=a y+bz,\qquad xy=c z,\qquad xz=y^2=yz=z^2=0,
\]

where \(a,c\ne0\). Since \(B\) is a local complete intersection, its relative dualizing module \(\operatorname{Hom}_R(B,R)\) is free of rank one as a \(B\)-module. Choose a generator \(\tau\). The determinant of the Frobenius matrix \((\tau(e_i e_j))\), in the displayed basis, is

\[
c^2\tau(z)^4.
\]

It is a unit. Therefore \(c\) is a unit, and the product of the first and second saturated pieces identifies them perfectly with the third. This establishes the required pairing even at defect points; generic perfection alone would not have been sufficient.

Globally, write \(L=N_1/N_2\). The product \(L^2\to N_2/N_3\) is nonzero, so

\[
E_1=L,\qquad E_2=L^2(D),\qquad E_3=L^3(D)
\]

for an effective divisor \(D\). Here \(E_i=N_i/N_{i+1}\), and \(N_4=0\). Also \(N_3=\operatorname{Ann}(J)\), by checking generically and using torsion freeness. Finite duality gives

\[
E_3=\omega_C\otimes(\omega_Z|_C)^{-1}=\mathcal O_{\mathbf P^1}(-18).
\]

The first piece \(L\) is a line quotient of \(E\). Write \(L=\mathcal O(e-7)\). Balancedness gives \(e\ge0\), while the degree equality gives

\[
\deg D=3-3e.
\]

Consequently only \((e,\deg D)=(1,0)\) and \((0,3)\) occur.

## The defect normal form, including the ambient embedding

Rescale \(z\) so \(xy=z\). In characteristic zero the substitution \(x'=x-(b/2)y\) removes the \(bz\) term from \(x^2\). Rescaling \(y\) by a unit then gives

\[
B\simeq R[[x,y]]/(x^2-t^d y,\ y^2),\qquad d=\operatorname{mult}_pD.
\]

The source quotient is free over \(R\), with basis \(1,x,y,xy\), so the surjection to \(B\) is an isomorphism. This also checks that no omitted higher nilpotent products remain in the presentation.

When \(d>0\), \(x,y\) are independent in the relative cotangent space of the special fiber. Ambient lifts, together with \(t\), therefore form formal coordinates in the smooth ambient threefold. In those actual ambient coordinates the ideal of \(Z\) is

\[
I_Z=(r_1,r_2)=(x^2-t^d y,\ y^2).
\]

When \(d=0\), these \(x,y\) are not independent ambient coordinates; using them as such would be an error. Instead the structure is primitive and ambient coordinates \(t,x,v\) can be chosen with

\[
I_Z=(v,x^4).
\]

The subsequent analysis treats these cases separately.

## Actual pencil coefficients do not invalidate the ADE calculation

The original pair \(F,G\) and either displayed local regular sequence are minimal generating sets of the same ideal. They differ by an invertible \(2\times2\) matrix over the completed ambient local ring. Thus an actual pencil member has coefficients which are formal functions, rather than assumed constants. At each fixed defect point, the two conditions that either coefficient vanish at that point each exclude at most one pencil parameter. There are finitely many defect points, so a general pencil member has both coefficients units at every defect.

At a defect point its equation can therefore be divided by a unit to give

\[
f=x^2-a(t)y+b(t,x,y)y^2,\qquad a(t)=t^d,\quad b(0,0,0)\ne0.
\]

The formal Morse lemma in the \(x\) variable gives \(f=x'^2+g(t,y)\). More explicitly, the critical solution \(x=\xi(t,y)\) is divisible by \(y^2\), and therefore

\[
g(t,y)=-a(t)y+c(t,y)y^2,\qquad c(0,0)\ne0.
\]

The parametric Morse lemma in \(y\) now gives \(g=y'^2+v(t)\), up to rescaling a unit coefficient. The critical point in \(y\) has order \(a(t)\), and direct substitution shows

\[
v(t)=-a(t)^2\cdot u(t),\qquad u(0)\ne0.
\]

Taking a \(2d\)-th root of the unit and changing the parameter \(t\) proves that \(f\) has type \(A_{2d-1}\). The coefficient-function issue therefore produces no additional hidden singularity types.

Away from \(D\), write a pencil member as \(f=A(t,x,v)v+B(t,x,v)x^4\). At a simple zero of its first symbol, \(A(t,0,0)\) has a simple zero and \(B(0,0,0)\ne0\), the latter by invertibility of the generating matrix. Divide by \(B\) and take \(T=A/B\) as a new ambient coordinate; its derivative in the support direction is nonzero. Then

\[
f/B=Tv+x^4,
\]

which is exactly \(A_3\). At a nonzero first symbol the surface is smooth.

## Global count and a general surface

Let \(M=\ker(E\to L)=\mathcal O(-7-e)\). Locally at a defect point, the first symbols of \(r_1,r_2\) are \(-t^d y,0\), with \(y\) a local generator of \(M\). Away from a defect, the relation \(v\) has a unit first symbol. Consequently the common vanishing divisor of the two first-symbol sections is exactly \(D\), with its multiplicities. Dividing it out yields a basepoint-free pencil in

\[
H^0(M(16)(-D))=H^0(\mathcal O(6+2e)).
\]

This pencil is nonconstant: a proportional pair of sections of a positive-degree line bundle would have a common zero. In characteristic zero the induced finite map \(\mathbf P^1\to\mathbf P^1\) is separable. A general pencil section therefore has \(6+2e\) simple zeros, avoiding \(D\).

Bertini on \(\mathbf P^3\setminus C\), together with the local calculations along \(C\), gives a member \(S\) smooth off finitely many ADE points. This statement does not require a separate irreducibility assertion for the pencil. Indeed a reducible hypersurface in \(\mathbf P^3\) is singular along the curve where two positive-degree components meet; a nonreduced component also gives a positive-dimensional singular locus. Therefore this member is reduced and irreducible. As a hypersurface with isolated singularities it is normal.

Adjunction gives \(\omega_S=\mathcal O_S\), and the hypersurface cohomology sequence gives \(H^1(S,\mathcal O_S)=0\). Rational double points have a crepant rational minimal resolution. Hence the minimal resolution \(\widetilde S\) is a smooth projective K3 surface.

The exceptional configurations at distinct singular points form the direct sum of their negative definite \(A_n\) lattices. For \(e=1\), the eight ordinary first-symbol zeros give rank \(8\cdot3=24\). For \(e=0\), write \(D=\sum_{j=1}^r d_jp_j\), so \(\sum d_j=3\) and \(r\le3\). The six ordinary zeros and the defect points give rank

\[
6\cdot3+\sum_{j=1}^r(2d_j-1)=24-r\ge21.
\]

A characteristic-zero projective K3 surface has Picard rank at most 20. In fact the exceptional rank is at most 19, since the pullback hyperplane class has positive square and is orthogonal to the negative definite exceptional lattice. Both cases contradict this bound.

For arbitrary algebraically closed \(k\) of characteristic zero, the hypothetical pair and the finite constructions descend to a finitely generated characteristic-zero subfield and can be embedded into \(\mathbf C\). The complex K3 bound therefore applies; an unmentioned assumption \(k=\mathbf C\) is unnecessary.

## Primary-source checks and conclusion

The external input is standard surface theory. Directly checked sources are D. R. Morrison, [The geometry of K3 surfaces](https://web.math.ucsb.edu/~drm/conferences/ITP99/morrison/cortona.pdf), printed pp. 5--6, for the \(A_n\) local forms, their \(n\) exceptional curves and crepant K3 resolution; and I. Shimada, [Rational double points on supersingular K3 surfaces](https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/RDPssK3/rdpssk3.pdf), Introduction, printed p. 1, for the characteristic-zero total exceptional-rank bound 19. The bound is invoked only in characteristic zero, and does not exclude the characteristic-two constructions.

No failure or counterexample was found after independently checking finite flatness, Frobenius perfection at defects, ambient-coordinate validity, varying coefficients in the actual global pencil, reducedness and normality, and the exceptional-curve count. The one necessary separation in the argument is that the normal form with two independent nilpotent ambient coordinates applies only at \(d>0\); the primitive \(d=0\) calculation must use \(I_Z=(v,x^4)\). The generic Hilbert-function \((1,2,1)\) branch must also be explicitly removed by the elementary quadric lemma above. With those points included, this gives an intrinsic exclusion of the sole-support \((4,4)\) case and no assertion about quartic mates of other degrees or unrestricted STCI.
