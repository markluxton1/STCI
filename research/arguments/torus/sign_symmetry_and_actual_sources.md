# Sign symmetry, actual equation sources, and section defects

Work over an algebraically closed field of characteristic different from two.
Write \(S=k[z,w,x,y]\), \(B=k[z,w]\), with all variables of degree one,
and let \(\tau(z,w,x,y)=(z,w,-x,-y)\). Translated quartics mean
\(C_{u,v}=[s^4:s^3t:ust^3:vt^4]\), with coordinates ordered
\([z:x:y:w]\). Every such curve is preserved by \(\tau\).

**Review scope.** The one-equation norm reduction, source-space parity
bound, symmetrized-source comparison and central-CI converse were
independently reconstructed in the present contribution. The claims below
retain their stated actual-source and characteristic hypotheses. In
particular they establish neither universal moment vanishing nor the
nonexistence of arbitrary supported ACM thickenings.

## 1. One sign-eigen equation is sufficient

Let \(J=(F_a,G_b)\) be a proper homogeneous CI whose entire cycle is
\(\sum_i n_i[C_{u_i,v_i}]\). If either actual generator is a
\(\tau\)-eigenform, then
\[
                         M_1=\sum_i n_i u_i/v_i=0.             \tag{AS1}
\]
The generator may be reducible or nonreduced.

Indeed assume \(\tau F=\epsilon F\), \(\epsilon\in\{1,-1\}\).
Properness gives both \(\gcd(F,G)=1\) and
\(\gcd(F,\tau G)=1\), so
\[
                         (F,G\tau G)
\]
is a proper, sign-invariant CI. Cartier-divisor additivity on \(V(F)\)
gives its cycle as
\([V(F,G)]+[V(F,\tau G)]\), including repeated factors of \(F\).
The second summand is the \(\tau\)-transform of the first, hence is
the same translated cycle. Its moment is therefore \(2M_1\).
[Sign-invariant ACM vanishing](chow_acm_parity_vanishing.md#1-the-finite-flat-sign-symmetry-theorem)
and \(2\ne0\) prove (AS1).

Consequently nonzero moment forbids a sign-eigen member of the actual
smallest generator space. This is weaker symmetry than being an eigenform
for the full intrinsic torus. The
[linkage parity bound](chow_moment_residual_speciality.md#source-space-parity-and-residual-speciality)
expresses the resulting constraint on that space and its residual
cohomology.

## 2. Symmetrizing an actual ACM source

Let \(J\subset S\) be a homogeneous ideal with \(A=S/J\) ACM of
dimension two, whose entire reduced projective support is a union of
translated quartics. A CI presentation is unnecessary in this section.
Put
\[
 A'=S/\tau J,\quad U=J\cap\tau J,\quad K=J+\tau J,\quad
 Q=S/K,\quad T=H^0_{(z,w)}(Q)=K^{\rm sat}/K.                  \tag{AS2}
\]
Here saturation is by the irrelevant ideal of \(S\). The equality of
the two torsion descriptions follows from finiteness over \(B\): the
projection center misses the common support, so the radicals of
\((z,w)Q\) and \(S_+Q\) agree. Both \(A,A'\) are finite graded
free \(B\)-algebras. The algebra \(E=S/U\) is pure: its injection into
\(A\oplus A'\) permits no associated primes beyond their curve primes.

There are canonical algebra descriptions
\[
 \boxed{\quad E=A\times_Q A',\qquad
 N=E^{**}_B=A\times_{Q/T}A',\qquad N/E\simeq T.\quad}       \tag{AS3}
\]
Thus the missing sections are pairs of actual source sections agreeing
after removal of the intersection's vertex torsion.

For the proof, the usual union sequence is
\[
 0\longrightarrow E\longrightarrow A\oplus A'
   \xrightarrow{(a,a')\mapsto a-a'} Q\longrightarrow0.
                                                               \tag{AS4}
\]
The inverse image of \(T\) is the displayed fiber product over
\(Q/T\). Since \(Q/T\) has no vertex torsion, the depth lemma makes
this inverse image depth two over \(B\), hence graded free. It agrees
with \(E\) away from the base vertex and is therefore its reflexive
section hull. The algebra structure is the fiber-product structure, not
an inference from freeness. Taking the quotient proves (AS3), and local
cohomology of (AS4) also gives
\[
 H^1_{(z,w)}(E)\simeq H^0_{(z,w)}(Q)=T.                       \tag{AS5}
\]
For the saturated pure curve \(\operatorname{Proj}E\), this is its
finite section/Rao defect.

The sign in the equivariant comparison matters. On \(A\oplus A'\),
\(\tau\) interchanges the two factors using the coordinate involution.
The difference map in (AS4) intertwines this action with **minus** the
natural action on \(Q\). Consequently, as graded \(B\)-modules with
involution,
\[
                         N/E\simeq T\otimes\operatorname{sgn}.
                                                               \tag{AS6}
\]
If the moment of the union's entire cycle is nonzero, the
[section-parity theorem](chow_section_parity_defect.md#2-opposite-signs-in-the-same-degree)
forces opposite signs in one generator degree of \(N\), and a
nonstandard-parity class in \((N/E)/(z,w)(N/E)\). Equivalently some
degree-\(d\) class of the **\(B\)-head** \(T/(z,w)T\) has natural
sign \((-1)^d\). This is not a statement about the \(S_+\)-head.

In characteristic zero, if \(J\) has sole support \(C_{u,v}\), its
union with \(\tau J\) has cycle \(n[C_{u,v}]\), \(n>0\), and
nonzero moment. Therefore \(T\ne0\): the actual parity-part ideal
\(J+\tau J\) is not saturated. For a CI, it is generated by the
even and odd parts of its two equations. This necessary condition already
holds for every homogeneous ACM supported source, before imposing CI.

Nonsaturation alone can be cheap. If \(K^{\rm sat}=I_C\) and the
generators of \(K\) have degree greater than two, the containing quadric
already lies in \(K^{\rm sat}\setminus K\). A useful further test must
control the actual torsion, its \(B\)-head, the multiplication on \(N\),
or its realization by the same source; merely exhibiting \(T\ne0\) is
not an additional nonexistence argument. For several translated components
the union multiplicities can change independently, so its moment must be
computed rather than identified with that of \(J\).

The same mechanism explains the
[projected-source defects](../linkage/projected_thickening_section_defects.md#uniform-failure-of-acm-for-the-actual-power-images):
an inclusion into an ACM source identifies the ambient missing sections
with vertex torsion in its cokernel. In the displayed power and binary
mixture sources, \(\tau\) fixes the auxiliary coordinate and preserves
the source equations. Their pure projected images are therefore
sign-invariant, so their characteristic-zero failure of ACMness also
follows structurally from the matrix theorem. The explicit Rao classes
retain stronger graded information and their separate characteristic scope.
Neither a bare Rao module nor its length recovers the first-moment value;
the algebra inclusion and multiplication remain part of the comparison.

### A signed hull profile that is already forced

Even the signed free-generator profile can be automatic. Suppose the
original source is a CI of type \((a,b)\) on \(C=C_{1,1}\), and
\(K^{\rm sat}=I_C\). Write
\(h_{a,b}(q)=(1+\cdots+q^{a-1})(1+\cdots+q^{b-1})\).
For \(E_C=S/I_C\), the missing degree-one section \(h=s^2t^2\) gives
\[
 E_C^-=B(-1)^2,\qquad E_C^+=B\oplus(z,w)B(-1).
\]
Indeed the odd part is generated by \(x,y\), and the even part by
\(1,zh,wh\), with the one relation between the last two.
Identify \(A'\) with \(A\) using \(\tau\), and let \(r:A\to E_C\)
be restriction. The eigenspaces of (AS3) identify with
\(r^{-1}(E_C^+)\) and \(r^{-1}(E_C^-)\), respectively. Thus
\[
 \operatorname{HS}(N^+)=\frac{h_{a,b}(q)-2q}{(1-q)^2},\qquad
 \operatorname{HS}(N^-)=\frac{h_{a,b}(q)-1-2q^2+q^3}{(1-q)^2}. \tag{AS6b}
\]
Both summands are graded free, so these numerators give their minimal
\(B\)-generator degrees. For \(a,b\ge3\), the degree-two coefficient
is three in the positive sector and one in the negative sector. Opposite
signs, including a nonstandard negative generator, are therefore already
forced in that degree. Diagonal coordinate scaling gives the same profile
on any single translate.

This calculation is conditional on the **actual** equality
\(K^{\rm sat}=I_C\). Under that equality, searching for the required
signed profile adds no constraint on the unknown source multiplication.
At points where the two first-normal images span \(I_C/I_C^2\),
Nakayama already gives \(\widetilde K=\mathcal I_C\) locally; deviations
are confined to their coincidence and nonprimitive loci and depend on
higher jets. Entirely thick sources require a different comparison.

For a characteristic-zero sole-support pair that is generically
curvilinear, this angular comparison is uniformly bounded. The
[actual first-symbol system](../carriers/normal_carrier_divisor_geometry.md#the-global-moving-root-theorem-the-larger-normal-carrier-has-index-m)
has saturated line \(M=\mathcal O_C(\ell-14)\subset
\mathcal O_C(-7)^2\). Its nonnegative top-defect degree
\((m-1)\ell-4(a+b)+14\), and \(a,b\ge5\), give
\(1\le\ell\le7\). If \(M\) and \(\tau^*M\) do not agree
identically, their wedge has a coincidence divisor of exact degree
\(14-2\ell\le12\). Off that divisor and the two nonprimitive loci,
\(\widetilde K=\mathcal I_C\). This bounds the angular coincidence,
not the nonprimitive divisor or its higher jets. If the lines agree
identically, no such finite-locus conclusion follows. Low-degree angular
movement and the growing-rank movement of the whole transverse algebra
in R-0072 are different conditions.

## 3. Actual controls for changing the symmetry

The [source controls](sign_source_controls.md) give explicit \((8,8)\)
and \((16,16)\) translated-cycle CIs breaking ideal symmetry; the latter
also has no sign-eigen member of its source plane. Both retain zero moment.
They show why symmetry tests alone do not characterize nonzero moment.
A parity homotopy keeps the central binary CI and the actual parity-part
ideal fixed (away from zero) while scaling the source differential by
\(\lambda^2\). If a sole-supported member exists with nonzero multiplicity
in the field, precisely its two conjugate parameters remain sole-supported.
The factors and maps in (AS3), not merely their common quotient or torsion,
are therefore part of the required source information.
The same control account resolves the reduced quartet's cyclic Hilbert
map on the blowup of the base origin; its nonconstant exceptional family
explains why the free section hull cannot substitute for an actual cyclic
lift. Additional generic Hilbert moduli in repeated cycles prevent extending
that reduced no-lift argument without new evidence.

## 4. The source realization problem after these comparisons

The [Hilbert converse](chow_hilbert_symplectic_form.md#a-central-binary-ci-gives-the-global-two-equation-source)
shows that a homogeneous finite-flat **cyclic** Hilbert lift of the full
quartet-cycle map, with central binary CI of degrees \((a,b)\), already
is a global homogeneous \((a,b)\) CI. There is no further generator
lifting condition after those hypotheses hold. In contrast, the free
section algebra \(N\) in (AS3) need not be generated by the original
\(x,y\); its extra sections are precisely what invalidates that converse
for an abstract free replacement.

For nonzero moment, the actual Hilbert lift would be symplectic at the
central binary CI. A sign-invariant homogeneous lift is even in the base:
\(f(-z,-w)=f(z,w)\), so its derivative at the origin is zero. This gives
a geometric interpretation of sign-symmetric vanishing in characteristic
zero. The full quartet Hilbert--Chow restriction, beyond axis collapse or
the central Gorenstein condition, must distinguish the desired lift.

These are different concrete questions: construct or obstruct that cyclic
Hilbert lift; determine which actual symmetrized fiber products and torsion
modules can occur; or prove aggregate first-jet cancellation in the
[actual carrier norm](spectral_boundary_modulus.md#2-an-actual-carrier-relation-supplies-an-ordinary-norm).
That ordinary norm relation exists for every actual pair, using row
replacement and normalized hyperplane curves on integral carrier factors.
Its aggregate jet is the same source residue; the remaining assertion is
a geometric reason for its cancellation. Proposed upstairs sections still
require actual polarized descent before this construction applies. The exact growing-degree Jacobian
and full determinant criteria still recognize support. Their equivalence
to source incidence does not select one of these additional mechanisms or
prove that it vanishes.
