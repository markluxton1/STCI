---
id: STCI-A-0003
type: argument
title: Constant embedded orbit families, endpoint descent, and actual equations
status: complete
scope: "#scope"
conclusion: "#conclusion"
---
# Constant embedded orbit families, endpoint descent, and actual equations

## Scope

Fix an algebraically closed field \(k\), the quartic
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and coordinate weights
\((0,1,3,4)\). Except where expressly restricted, the field has arbitrary
characteristic. The data are a finite positive-length **embedded** quotient

\[
B=k[u^{\pm1},v^{\pm1}]/J,\qquad n=\dim_k B,
\]

with its named units \(u,v\). The transverse quotient is constant along the
orbit parameter. The construction retains nilpotents, both endpoint algebras,
and the complete homogeneous equation spaces. It is not an assertion about
all moving thickenings of \(C_0\).

This Argument supplies the complete proofs of the [finite image](../results/constant_embedded_orbit_image.md)
R-0051, [endpoint polynomial](../results/orbit_image_endpoint_polynomial.md)
R-0052, [actual equation criterion](../results/constant_quotient_equation_criterion.md)
R-0053, [embedded counterexamples](../results/embedded_quotient_endpoint_counterexamples.md)
R-0054, [flat collision](../results/flat_collision_of_orbit_images.md) R-0055,
and [pure-curve degree exhaustion](../results/pure_curve_degree_exhaustion.md)
R-0056. Independent substantive review accepts the six reconstructed proof routes within their stated scopes, as recorded in Review.
The general degree-exhaustion section works over any field.

The reconstruction preserves the mathematics of
[constant quotient descent](../synthesis/toric_quotients_and_endpoint_descent.md).
A separate review of the source is distinct from acceptance of these reconstructed proofs. Intrinsic finite-map geometry and purity prove the
general construction. The examples additionally require the explicit finite
coefficient identities displayed below.

## Finite image and purity

Define \(S=k[x_0,x_1,x_2,x_3]\) and

\[
K=\ker\left(S\to B[s,t]\right),\qquad
(x_0,x_1,x_2,x_3)\mapsto(s^4,s^3t,ust^3,vt^4).
\tag{1}
\]

The kernel is homogeneous when the target is read in degrees divisible by
four. Multiplication by \(s^4\) on \(B[s,t]\) is injective even if \(B\)
has nilpotents. Hence \(K:x_0=K\), so \(K\) is irrelevant-saturated: if
the irrelevant ideal to a power kills a class, its power of \(x_0\) already
kills it. Localization by \(st\) is likewise injective. Thus \(K\) is the
contraction of the torus kernel, and its Proj is the scheme-theoretic
closure, including nilpotents, of \([1:r:ur^3:vr^4]\).

The four sections in (1) have no common zero on \(\mathbf P^1_B\), since
\(u,v\) are units. They define
\(\nu:\mathbf P^1_B\to Z_B=\operatorname{Proj}(S/K)\).
The opens \(x_0\ne0\) and \(x_3\ne0\) cover its image: on the source
they are \(s\ne0\) and \(t\ne0\), which cover the source.
On the first chart put \(r=t/s\). Its affine image ring is

\[
H_0=k[r,r^3u,r^4v]\subset B[r].
\tag{2}
\]

On the second chart put
\(z=(u/v)(s/t)\), \(\alpha=v^2/u^3\), \(\beta=v^3/u^4\).
This is a unit change of the source parameter, and

\[
x_2/x_3=z,\quad x_1/x_3=z^3\alpha,\quad x_0/x_3=z^4\beta.
\]

The second image ring is consequently

\[
H_\infty=k[z,z^3\alpha,z^4\beta]\subset B[z].
\tag{3}
\]

Each inclusion is finite: a \(k\)-basis of \(B\) generates \(B[r]\) as
an \(H_0\)-module because \(k[r]\subset H_0\), and the same holds for
\(z\). These finite affine maps glue to \(\nu\). Its source is proper,
so its scheme image is closed and is exactly the closure defined by (1).
Inverting \(r\) in (2) recovers \(u,v\), giving
\(H_0[r^{-1}]=B[r,r^{-1}]\). At infinity the same follows from

\[
u=\beta^2/\alpha^3,\qquad v=\beta^3/\alpha^4.
\tag{4}
\]

Thus \(\nu\) is an isomorphism off the endpoints. The boundary has only
the two indicated point supports, not a curve.

Purity does not follow merely from the appearance of these supports.
The ring \(H_0\) is a \(k[r]\)-submodule of the finite free module
\(B[r]\); it is finitely generated and torsion-free over the PID \(k[r]\).
The same holds for \(H_\infty\) over \(k[z]\). At a closed point on
either chart the base parameter minus its residue is a nonzerodivisor;
the local ring has dimension one because the extension of the parameter
ring is finite and torsion-free. It is therefore Cohen--Macaulay.
An associated prime cannot contract to a nonzero prime of the parameter
ring, since that would give parameter torsion; primes over the generic
point in a finite extension are minimal. This proves pure dimension one
and excludes embedded points, including at the endpoints.

Finally \(B_{\mathrm{red}}\) is a product of copies of \(k\), indexed by
its finite support in \(\mathbf G_m^2\). The support point \((c,d)\)
gives \([s^4:s^3t:cst^3:dt^4]\). Its first image chart is \(k[r]\),
its last is \(k[z]\), giving a smooth embedded rational quartic.
Distinct points have disjoint torus restrictions and can meet only at
the two common endpoints. In particular \(C_0\) occurs if and only if
\((1,1)\) is in that support, and is the sole reduced support if and
only if the support is exactly \(\{(1,1)\}\). This proves R-0051.

## Endpoint defects and Hilbert polynomial

Completing the finite modules (2)--(3) at their boundary parameters gives

\[
A_0=k[[r]][r^3u,r^4v]\subset B[[r]],\qquad
A_\infty=k[[z]][z^3\alpha,z^4\beta]\subset B[[z]].
\tag{5}
\]

Brackets mean the finite completed image algebra. At parameter zero
the image has a single point support, so the parameter-adic completion
is its endpoint completion. Formula (5) is an actual algebra inclusion,
not merely its associated graded symbols.

An invertible element of a finite-dimensional \(k\)-algebra has an
annihilating polynomial with nonzero constant coefficient, so its inverse
is a polynomial in it. Positive monomials in \(u,v\) therefore span
\(B\); choose a monomial \(k\)-basis \(u^iv^j\), \(i,j\ge0\). For
\(N\ge\max(3i+4j)\), every \(r^Nu^iv^j\) belongs to \(A_0\).
Multiplying by \(k[[r]]\) gives

\[
r^N B[[r]]\subset A_0.
\tag{6}
\]

By (4) the same proof applies to \(\alpha,\beta\) at infinity. Both
cokernels have finite length, denoted \(\delta_0,\delta_\infty\).
These are cokernel lengths, without an identification with conductor
colengths or reduced normalization invariants.

The scheme-image definition and finite map give an injective map of
structure sheaves. Its cokernel vanishes on the punctured charts, so
there is an exact sequence

\[
0\to\mathcal O_{Z_B}\to\nu_*\mathcal O_{\mathbf P^1_B}
\to Q_0\oplus Q_\infty\to0,\qquad\ell(Q_i)=\delta_i.
\tag{7}
\]

The morphism defined by the four base-point-free degree-four sections has
\(\nu^*\mathcal O_{Z_B}(1)=\mathcal O_{\mathbf P^1_B}(4)\). Apply the
projection formula to (7) and take Euler characteristics. Since \(B\) has
\(k\)-dimension \(n\), we have
\(\chi(\mathbf P^1_B,\mathcal O(4d))=n(4d+1)\). Twisting a finite-length
sheaf leaves its Euler characteristic unchanged. Hence

\[
P_{Z_B}(d)=4nd+n-\delta_0-\delta_\infty,\quad
\deg Z_B=4n,\quad p_a(Z_B)=1-n+\delta_0+\delta_\infty.
\tag{8}
\]

This proves R-0052 in every characteristic without separability assumptions.

## Pure-curve degree exhaustion

Here \(k\) may be any field. Let \(Y\hookrightarrow X\subset\mathbf P^N_k\)
be a closed inclusion, with \(X\) a projective pure curve whose structure
sheaf has no nonzero finite-support subsheaf. Put
\(\mathcal L=\ker(\mathcal O_X\twoheadrightarrow\mathcal O_Y)\).
At each one-dimensional generic point \(\eta_i\), exactness gives

\[
\ell(\mathcal O_{X,\eta_i})
=\ell(\mathcal L_{\eta_i})+\ell(\mathcal O_{Y,\eta_i}).
\]

Degree is the sum of these generic lengths times the positive degrees
of the reduced components. Equality of degrees therefore forces
\(\mathcal L_{\eta_i}=0\) for every \(i\), including any component absent
from \(Y\). The support of \(\mathcal L\) is consequently finite. Purity
of \(\mathcal O_X\) forces \(\mathcal L=0\), and \(X=Y\).

The final step is essential. Generic equality would allow a finite-support
kernel in an impure containing scheme. A curve with an embedded point can
have the same degree as the subscheme obtained by deleting that point.

For coprime positive-degree \(F,G\in k[x_0,x_1,x_2,x_3]\), UFD
factorization of \(F\) shows that multiplication by \(G\) is injective
modulo \(F\). They form a regular sequence. The quotient is
Cohen--Macaulay of dimension two; its projective curve is pure
Cohen--Macaulay of degree \((\deg F)(\deg G)\), and its ideal is saturated.
Indeed depth at the irrelevant maximal ideal is two, so the quotient has
no irrelevant-torsion submodule, which is exactly what saturation removes.
Thus the preceding lemma applies to every proper pair with actual
containment. Saturated homogeneous ideals are the ideals of their
projective schemes, so scheme equality gives equality of these ideals.
This proves R-0056.

## Actual equations and the CI criterion

For \(e=(e_0,e_1,e_2,e_3)\), the image of \(x^e\in S_d\) is

\[
u^{e_2}v^{e_3}s^{4d-w}t^w,\qquad w=e_1+3e_2+4e_3.
\tag{9}
\]

Distinct integer weights give distinct binary monomials over every field;
they do not coincide when their labels are congruent modulo the
characteristic. Thus a degree-\(d\) polynomial belongs to \(K_d\)
exactly when its coefficient in \(B\) vanishes separately at every weight.
For

\[
E_{d,w}=\{e\in\mathbf Z_{\ge0}^4:|e|=d,\
e_1+3e_2+4e_3=w\},\qquad
\psi_{d,w}:k^{E_{d,w}}\to B,\quad
(c_e)\mapsto\sum_e c_eu^{e_2}v^{e_3},
\]

this says \(K_d=\bigoplus_w\ker\psi_{d,w}\), and
\(\dim_k(S/K)_d=\sum_w\dim_k\operatorname{im}\psi_{d,w}\).
These are the complete actual homogeneous source spaces.

If \(Z_B\) is a scheme CI of type \((a,b)\), its saturated ideal has a
regular sequence of those degrees, giving a coprime such pair, and its
degree \(ab\) equals \(4n\) by (8). Conversely, let \(F\in K_a,G\in K_b\)
be coprime with \(ab=4n\). The actual inclusion
\(Z_B\subset X=V(F,G)\) and equality of degrees satisfy pure-curve
degree exhaustion. It kills the generic kernel and then the possible
finite-support remainder. Thus \(Z_B=X\), and saturation gives
\(K=(F,G)\). Equal degrees alone have not been used as equality.

The Koszul resolution gives the CI formula
\(\chi(\mathcal O_X)=-ab(a+b-4)/2\). Compare with (8) and substitute
\(ab=4n\) to get

\[
\delta_0+\delta_\infty=n(2a+2b-7).
\tag{10}
\]

This is only the necessary numerical shadow of the criterion, without
replacing its actual coprime-pair clause. This proves R-0053.

## Endpoint examples

### The fourth-root image and its conductor

Take \(B=k[u]/(u^4-1)\), \(v=1\), in any characteristic. The forms

\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3
\tag{11}
\]

belong to \(K\). The polynomial \(F\) is primitive and linear in \(x_3\)
over \(k[x_0,x_1]\), hence irreducible by Gauss's lemma. It cannot divide
\(G\), whose coefficient of \(x_2^4\) is one. The forms are coprime;
the criterion gives \(Z_B=V(F,G)\), degree sixteen and genus thirty-three.

At zero \(r^4v\) is redundant and an exact free \(k[[r]]\)-basis is

\[
1,\ r^3u,\ r^6u^2,\ r^9u^3.
\tag{12}
\]

All powers of \(r^3u\) reduce using \(u^4=1\), and these coefficient
vectors are independent. At infinity \(\alpha=u^{-3}=u\), \(\beta=1\);
the same calculation applies. The two indices are \(3+6+9=18\).

The conductor into the finite modification is exactly \(r^9B[[r]]\).
Below order nine the allowable coefficient spaces of (12) are contained
in \(\operatorname{span}_k(1,u,u^2)\). The pairing

\[
B\times B\to k,\qquad (b,c)\mapsto
\text{coefficient of }u^3\text{ in }bc
\]

is nondegenerate: in the cyclic basis every basis vector has a unique
partner with exponent \(3\) modulo \(4\), with coefficient one. Hence
no nonzero ideal of \(B\) is contained in that three-dimensional space,
in any characteristic. A nonzero conductor series of order below nine
could be multiplied by a suitable \(c\in B\) to violate that coefficient
constraint. Conversely every order at least nine is in the lattice.
This proves the claimed conductor; replace \(r\) by \(z\) at infinity.

In characteristic two write \(u=1+\epsilon\), \(\epsilon^4=0\). A
triangular change gives (12) as
\(1,r^3\epsilon,r^6\epsilon^2,r^9\epsilon^3\). Its conductor and index
stay unchanged. The reduced image, however, is smooth \(C_0\): its reduced
normalization defect is zero and its normalization conductor is the whole
ring. These are distinct conductor problems. The integral flatness and
prescribed arithmetic specialization of (11) remain the separate legacy
[R-0021](../results/quartic_mu4_degeneration.md). Here only the fixed-field
image and lattice assertions are reconstructed.

### Embedded quotients and characteristic-dependent endpoints

We first prove an elementary lattice observation. Suppose
\(1,c_1,c_2,c_1^2\) is a basis of a four-dimensional coefficient algebra.
Then

\[
L=k[[z]]\langle1,z^3c_1,z^4c_2,z^6c_1^2\rangle
\tag{13}
\]

is an algebra. The only product of nonunit basis vectors with total
weight below seven is \((z^3c_1)^2=z^6c_1^2\); every other product
has weight at least seven, whereas all basis weights are at most six.
Expand its coefficient in the chosen basis, using only nonnegative
powers of \(z\). If the image algebra is generated by \(z^3c_1,z^4c_2\),
(13) is exactly that image: it is a containing algebra, and all four
displayed basis vectors are generated. Its index is \(3+4+6=13\).

In characteristic zero compare the fourth-root embedding of \(k^4\)
with \(B=k^4\) where \(u\) has values \(1,2,3,4\) and \(v=1\).
At zero \(u\) generates \(B\); the exact weights are \(0,3,6,9\), giving
\(\delta_0=18\). At infinity \(\alpha=u^{-3},\beta=u^{-4}\), and

\[
M=\begin{pmatrix}
1&1&1&1\\
1&1/8&1/16&1/64\\
1&1/27&1/81&1/729\\
1&1/64&1/256&1/4096
\end{pmatrix},\qquad
\det M=\frac{1505}{7962624}\ne0.
\tag{14}
\]

This rational matrix is a finite certificate that
\(1,\alpha,\beta,\alpha^2\) is a basis. Observation (13) proves exact
infinity weights \(0,3,4,6\), giving \(\delta_\infty=13\). Formula (8)
gives \(P(d)=16d-27\), genus twenty-eight. The fourth-root embedding
of the same abstract algebra had genus thirty-three. These images differ,
and the new image is not a \((4,4)\) CI.

Still in characteristic zero, take \(B=k[\epsilon]/(\epsilon^4)\),
\(u=1+\epsilon,v=1\). At zero the exact basis
\(1,r^3\epsilon,r^6\epsilon^2,r^9\epsilon^3\) gives index eighteen.
At infinity subtract constants:

\[
a=u^{-3}-1=-3\epsilon+6\epsilon^2-10\epsilon^3,\qquad
b=u^{-4}-1=-4\epsilon+10\epsilon^2-20\epsilon^3.
\tag{15}
\]

The required finite identities are

\[
b=\tfrac43a+\tfrac29a^2-\tfrac4{81}a^3,\qquad
\det\begin{pmatrix}-3&-4&0\\6&10&9\\-10&-20&-36\end{pmatrix}=36.
\tag{16}
\]

Thus \(1,a,b,a^2\) is a basis. Observation (13) gives exact infinity
weights \(0,3,4,6\), index thirteen and genus twenty-eight. The identities
are verified by multiplication modulo \(\epsilon^4\). This is the
necessary finite calculation, with no claim about arbitrary local algebras.

This endpoint is not Gorenstein. Modulo the regular parameter \(z\), put
\(x=[z^3a]\), \(y=[z^4b]\). The four classes are \(1,x,y,x^2\).
Every product beyond \(x^2\) has total weight strictly greater than six,
so its expansion in (13) has a positive factor of \(z\). Including the
four-dimensional basis count proves

\[
A_\infty/zA_\infty\simeq k[x,y]/(x^3,xy,y^2).
\tag{17}
\]

Its socle has basis \(x^2,y\), hence dimension two. Quotienting a
Gorenstein local ring by a nonzerodivisor would give an Artin Gorenstein
ring with one-dimensional socle. The Cohen--Macaulay endpoint is
therefore not Gorenstein, and not a local complete intersection.
Its sole reduced support \(C_0\) does not repair that defect.

Form the same specified quotient separately in each characteristic.
The zero index stays eighteen. For characteristic zero or \(p>3\),
the determinant \(36\) gives infinity index thirteen. In characteristic
two (15) becomes \(a=\epsilon,b=0\), so the weights are \(0,3,6,9\)
and the index eighteen; \(u^4=1\) identifies this with (11). In
characteristic three,

\[
a=-\epsilon^3,\quad b=2\epsilon+\epsilon^2+\epsilon^3,\quad
b^2=\epsilon^2+\epsilon^3,\quad ab=a^2=0.
\]

The vectors \(a,b,b^2\) are independent. The exact infinity basis is
\(1,z^3a,z^4b,z^8b^2\): products close since \(ab=a^2=0\),
\(b^3\) is a multiple of \(a\), and higher powers vanish.
Its index is \(3+4+8=15\). Thus

| Characteristic | \(\delta_0\) | \(\delta_\infty\) | \(p_a(Z_B)\) |
| --- | ---: | ---: | ---: |
| \(0\), or \(p>3\) | 18 | 13 | 28 |
| \(2\) | 18 | 18 | 33 |
| \(3\) | 18 | 15 | 30 |

The genera exclude type \((4,4)\) except in characteristic two. These
are fixed-field images; no commutation with arithmetic reduction is
asserted. This proves R-0054. The existing
[finite verifier](../investigations/torus-residual-controls/verify.py),
in its quotient_checks function, checks (14)--(16) and these endpoint
indices. The geometric proof remains the complete argument above.

## A flat collision of the genus-twenty-eight images

Work in characteristic zero. Over a neighborhood of \(h=0\), set

\[
B_h=k[h,\epsilon]/\bigl(\epsilon(\epsilon-h)
(\epsilon-2h)(\epsilon-3h)\bigr),\qquad u=1+\epsilon,\ v=1.
\tag{18}
\]

This algebra is free of rank four with basis
\(1,\epsilon,\epsilon^2,\epsilon^3\). Restrict to an affine open
neighborhood \(U\) of zero where \(u\) and the coefficient determinant
of \((1,a,b,a^2)\), with \(a=u^{-3}-1,b=u^{-4}-1\), are units.
It exists: the norm of \(u\) at zero is one and that determinant at
zero is \(36\). Write \(R=\mathcal O(U)\), \(B_R=B_h\otimes R\).

At zero the image has free \(R[r]\)-basis

\[
1,\ r^3\epsilon,\ r^6\epsilon^2,\ r^9\epsilon^3.
\tag{19}
\]

The monic relation (18) expresses \(\epsilon^4\) in
\(R\epsilon+R\epsilon^2+R\epsilon^3\). Every reduction lowers the
exponent and its weight, so all coefficients in (19) have nonnegative
powers of \(r\). After scalar subtraction the image generators are
\(r^3\epsilon\) and the redundant \(r^4\).

At infinity the free \(R[z]\)-basis is

\[
1,\ z^3a,\ z^4b,\ z^6a^2.
\tag{20}
\]

The proof is the relative version of (13): the coefficient basis is
invertible over \(R\), the one product below weight seven is exactly
\(a^2\), and every other product has sufficient parameter weight for
expansion. This proves closure explicitly; a unit coefficient determinant
alone would not prove a submodule is the image algebra.

The endpoint quotients are direct sums of \(R[r]/(r^q)\) or
\(R[z]/(z^q)\), for the listed basis weights \(q\). They are free over
\(R\) of ranks eighteen and thirteen. The weighted bases prove this on
the uncompleted affine charts as well as their completions. Off the
endpoint sections the relative image equals the source torus.
Its sheaf inclusion therefore has these two \(R\)-flat endpoint
cokernels, and its source structure sheaf is \(R\)-flat. The kernel,
which is the image structure sheaf, is \(R\)-flat. Equivalently the
free affine image bases already prove flatness on a cover.
The flat endpoint cokernels ensure these inclusions remain injective
on every fiber base change, so each fiber is the image formed from
its fiber quotient. Image base change has been proved for this family,
rather than assumed for arbitrary scheme images.

Every projective fiber has \(P(d)=16d-27\). At \(h=0\) it is (15).
At every \(h\ne0\) in \(U\), the four roots of (18) are distinct, so
the image consists of four reduced quartic components. The quotient
\(\epsilon=0\) gives \(u=v=1\) on every fiber and retains marked \(C_0\).
This proves R-0055: it is a flat collision of genus-twenty-eight images,
not a deformation through these images of the genus-thirty-three CI.

## Binomial quotient types and their limitation

The source's useful arithmetic observation is retained. Let a full-rank
lattice \(L\subset\mathbf Z^2\) specify compatible relations
\(u^{\ell_1}v^{\ell_2}=c_\ell\), with \(c_\ell\in k^*\).
Algebraic closedness extends this character on \(L\) to \(\mathbf Z^2\):
in Smith coordinates this requires only roots of two nonzero constants.
Rescale the original units by that character. The quotient is
\(k[\mathbf Z^2/L]\), and Smith normal form gives the abstract presentation

\[
k[U^{\pm1},V^{\pm1}]/(U^{d_1}-1,V^{d_2}-1),\quad
d_1\mid d_2,\quad n=d_1d_2.
\tag{21}
\]

In characteristic \(p>0\), write \(d_i=p^{a_i}m_i\), \(p\nmid m_i\).
Since \(U^{d_i}-1=(U^{m_i}-1)^{p^{a_i}}\) has \(m_i\) distinct roots,
there are \(m_1m_2\) reduced points, each with local algebra

\[
k[\eta_1,\eta_2]/(\eta_1^{p^{a_1}},\eta_2^{p^{a_2}}),
\]

of length \(p^{a_1+a_2}\). In characteristic zero all \(n\) points are
reduced. This is an abstract group-algebra calculation. The original
\(u,v\) must still be carried through (5) to determine the image.
Smith invariants cannot recover endpoint gluing, just as the two
embeddings of \(k^4\) above have different endpoint defects.
No classification of arbitrary embedded quotients or homogeneous
defining pairs follows.

## Conclusion

A constant embedded quotient determines an actual saturated pure curve,
its complete endpoint algebras, Hilbert polynomial and all homogeneous
equation spaces. Its exact prescribed-degree CI test is degree
exhaustion plus an actual coprime pair. Abstract algebra, sole support,
endpoint indices and flat collision each omit some of this information.

Nothing here supplies a moving embedded quotient representing an arbitrary
supported CI, or a comparison between geometric endpoint defects and
opposite Hilbert-limit directions. The existing
[entire finite modification and positive-movement theorem](../synthesis/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification)
is a distinct scoped premise when used elsewhere; it is not reconstructed
or strengthened here. No unrestricted characteristic-zero STCI
conclusion is obtained.

## Review

The retained chapter received a separate review of its image, proper-pair, endpoint and collision arguments; finite arithmetic was checked separately. That review is distinct from acceptance of the reconstructed proofs.

Independent reconstruction review, 2026-11-04: reviewer
pilot_review_hilbert accepted this Argument and the exact R-0051--R-0056
routes with no blockers. The reviewer independently reconstructed finite
image formation, saturation, finite charts, Cohen--Macaulay purity,
the endpoint exact sequence and Hilbert polynomial, pure-curve degree
exhaustion including its finite-support kernel, and the gcd-one criterion
using the actual equation spaces. The review also reconstructed the
benchmark conductors, the type-two endpoint, and the relative flat
collision and image base-change proof. The explicit weighted-product
closure argument was checked on semisimple as well as nilpotent fibers.
The evaluation determinant 1505/7962624, coefficient determinant 36,
truncated nilpotent identity, and characteristic-two and
characteristic-three reductions were independently recomputed.
Preservation of the constant-quotient source mathematics, including the
binomial Smith-normal-form section, was checked.

This decision has basis reconstructed and accepts only those exact
scopes. The moving-modification positivity theorem and the separate
legacy R-0021 proof were outside review. No global STCI conclusion or
endpoint/opposite-limit comparison was accepted. The six Result reviews cover only their stated scopes; the moving-modification positivity theorem and legacy R-0021 proof were outside review.
