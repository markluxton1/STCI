# The full conductor boundary of the tropical modification

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
see the [bounded audit](2026-10-31-tropical-conductor-audit.md).
This is an application of classical finite duality to the full tropical
thickening. It gives the finite schemes and algebra pairing at the two
contractions, including when the source is not Gorenstein. It does **not**
give a new STCI exclusion: the numerical conductor formula reproduces
the genus identity, and the full boundary condition has not been shown
incompatible with positive movement or with global equations.

## 1. Exact objects and the uniform boundary condition

Let k be algebraically closed, let

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\qquad Z=V(F_a,G_b),\qquad Z_{\mathrm{red}}=C,
\]

and put m=ab/4. Use the entire finite modification
\(\rho:W\to Z\), finite flat projection \(\pi:W\to\mathbf P^1\),
and algebra \(\mathcal B=\pi_*\mathcal O_W\) constructed in the
[reviewed descent note](2026-10-31-tropical-descent.md). In particular,
W is defined by saturation of the full ideal, not by dividing two
chosen equations. Write e=deg B and L=4(a+b)−14. The strict inequality
e>0 uses characteristic zero; all the conductor statements below work
in any characteristic under these hypotheses.

Let c be the conductor of \(\mathcal O_Z\subset\rho_*\mathcal O_W\),
viewed also as an ideal on W. At either endpoint, complete and write
\(A\subset B\) for the resulting algebras over R=k[[t]]; use the
actual parameter z instead of t at infinity. They are free of rank m
over R and have the same generic Artin algebra. Put

\[
\delta=\operatorname{length}(B/A),\qquad
D=B/c,\qquad E=A/c\subset D.
\]

The following necessary condition retains more than the number delta:

* D is an Artinian Gorenstein algebra of length 2 delta.
* E is a unital subalgebra of D of length delta. There is a Frobenius
  functional epsilon:D→k for which E is its own orthogonal complement
  under the perfect pairing (x,y)↦epsilon(xy).
* The entire endpoint algebra is recovered as
  \(A=B\times_D E\). In the tropical coordinates this recovered algebra
  must be precisely \(R[t^3U,t^4V]\), or
  \(k[[z]][z^3U',z^4V']\) at infinity, with the transformed coordinates
  in the descent note.

If delta=0 the boundary is empty and these assertions have the evident
zero-algebra interpretation. E is a **subalgebra**, not an ideal of D.
Geometrically, Spec D is the finite conductor subscheme in W; the finite
map Spec D→Spec E is the complete pinching datum at the endpoint. Its
self-orthogonality means that exactly half the boundary functions
descend, with multiplicative compatibility imposed by duality. These
are boundary schemes of a nonreduced curve, not residual curves and not
normalizations of reduced curve singularities.
The conductor fiber-product interpretation is classical; see
[Ferrand, Sections 2.2 and 5.4](https://www.numdam.org/item/BSMF_2003__131_4_553_0/).

## 2. The conductor is the full dualizing module

For the finite birational inclusion A⊂B, evaluation at 1 identifies

\[
\operatorname{Hom}_A(B,A)
=\{q\in A[1/t]:qB\subset A\}=c.
\tag{1}
\]

Indeed any A-linear map becomes multiplication by q after inverting t,
because then A=B; its value at 1 is q∈A. This proof uses the common
generic Artin algebra and does not assume that it is a field or that
B is Gorenstein.

Finite duality for the CM curve W and the Gorenstein curve Z gives

\[
\omega_W\simeq c\otimes\rho^*\omega_Z.
\tag{2}
\]

The tropical morphism is given globally by the four sections
\([s^4:s^3t:u st^3:v t^4]\) of \(\pi^*O(4)\), with no common zero.
Consequently \(\rho^*O_Z(1)\simeq\pi^*O(4)\). CI adjunction and
finite-flat duality for pi then imply the actual B-module isomorphism

\[
\pi_*c\simeq\mathcal B^\vee\otimes O(-L).
\tag{3}
\]

This is an identification with the conductor **module**. It does not
make c invertible and does not assert that omega_W is a line bundle.

The standard finite-map input is
[Stacks, dualizing modules for quasi-finite ring maps](https://stacks.math.columbia.edu/tag/0BUK).
[Battistella–Carocci, Section 2](https://msp.org/gt/2023/27-3/gt-v27-n3-p05-p.pdf)
explicitly discusses conductors and finite birational modifications in
the possibly nonreduced CM curve setting. Their formula with two
Gorenstein curves is not being used to assume W Gorenstein here.

## 3. Local residue proof, including the entire boundary pairing

Since A is finite free and Gorenstein over the DVR R, choose a
Frobenius functional lambda:A→R: the pairing lambda(xy) identifies
A with its R-dual. Extend lambda to the common generic Artin algebra
Q=A[1/t]=B[1/t]. Its A-dual lattice is

\[
\{q\in Q:\lambda(qA)\subset R\}=A.
\tag{4}
\]

The B-dual lattice for the same pairing is exactly c. One direction
follows from cB⊂A. Conversely, if lambda(qB)⊂R, then q∈A by (4),
and for b∈B, a∈A the element ab is in B. Thus lambda(qba)∈R,
so qb∈A by (4). Hence qB⊂A.

Dualizing the inclusion of free R-lattices A⊂B therefore gives

\[
\operatorname{length}(A/c)=\operatorname{length}(B/A)=\delta,
\qquad \operatorname{length}(B/c)=2\delta.
\tag{5}
\]

Equivalently, applying Hom_A(−,A) to 0→A→B→B/A→0 identifies
A/c with the finite-length dual of B/A. The required Ext vanishing
uses B maximal CM over the one-dimensional Gorenstein ring A, not
B Gorenstein.

Define epsilon on D by taking the coefficient of t^(−1) in lambda(b).
This is well-defined because lambda(c)⊂R. It vanishes on E. If b∈B
is orthogonal to every b'∈B, then the same is true of t^j b' for
every j≥0. Every negative coefficient of lambda(bb') therefore
vanishes, so lambda(bB)⊂R and b∈c. Thus epsilon(bb') is a perfect
k-pairing on D. This proves D Gorenstein directly, even when B is not.

Since E is a subalgebra and epsilon(E)=0, it is isotropic. Equation
(5) gives half the dimension of D, so \(E=E^\perp\). Finally,
A is exactly the inverse image of E under B→D, proving the pullback
description. The choice of lambda changes the presentation of the
pairing; existence of this compatible pairing is the invariant claim.

These are classical canonical-ideal and residue-duality phenomena.
For the canonical-ideal formulation, see
[Elias, Section 2, Lemma 2.1 and Proposition 2.2](https://arxiv.org/pdf/1309.5193):
quotienting a one-dimensional CM ring by a canonical ideal gives an
Artinian Gorenstein ring. The proof above includes the compatibility
with the actual subalgebra A, avoiding a reduced-normalization premise.

## 4. A non-Gorenstein source control

Over R=k[[t]], start with the supported complete intersection

\[
A=R[x,y]/(x^2+y^2,xy),\qquad x=t^3U,\quad y=t^4V.
\]

The full saturated upstairs algebra is

\[
B=R[U,V]/(U^2+t^2V^2,UV,V^3).
\tag{6}
\]

It is free with basis 1,U,V,V², and after inverting t it is the
displayed CI algebra. Freeness therefore proves that (6) is the full
contraction from the punctured chart. Its special fiber has socle
spanned by U and V², so B is not Gorenstein.

Inside this basis A is the lattice with exponents (0,3,4,8), hence
delta=15. Multiplication by U and V gives the exact conductor

\[
c=R t^8\oplus R t^6U\oplus R t^8V\oplus R t^8V^2
  =(t^8,t^6U)B.
\tag{7}
\]

For example, membership in A first imposes the four lattice bounds;
multiplying by U,V,V² strengthens them to (8,6,8,8), which proves
both inclusions in (7). Thus D has length 30. Its socle is the single
line spanned by t^7V². Taking the coefficient of this monomial is a
Frobenius functional killing E, which has length 15.

Geometrically, saturating a locally complete-intersection contraction
can replace its transverse length-four Gorenstein fiber by a
non-Gorenstein punctual scheme upstairs. The finite conductor boundary
still has perfect duality. Thus replacing omega_W by a line bundle,
or replacing c by a principal ideal, would discard an allowed local
phenomenon. This is an exact local control in every characteristic,
not a homogeneous projective realization on C. The computations are
the displayed basis and multiplication calculations; no computer
algebra certificate or inherited computation was rerun.

## 5. What this changes, and what it does not

Taking degrees in (3), or summing (5), gives only

\[
2(\delta_0+\delta_\infty)=2e+mL.
\]

This is exactly the descent note's genus identity. Finite duality has
not supplied a second independent numerical equation. The full
boundary algebra and its self-orthogonal subalgebra retain information
that this determinant calculation forgets, but no incompatibility with
e>0 has been proved.

[R-0032](../results/full_conormal_socle_budget.md) concerns the complete
normal filtration and actual socle of Z. The
[October 26 torsion account](2026-10-26-normal-torsion-spectral-genus-budget.md)
has pointwise pairing identities under its stated transverse hypotheses.
The present construction instead retains the complete finite conductor
scheme of W→Z, allowing non-Gorenstein B. This difference of objects
does not establish a stronger exclusion. The earlier
[formal-neighborhood criterion](2026-10-27-formal-neighborhood-residual-visibility.md)
and [full-primary attachment module](2026-10-27-absorption-attachment-module.md)
already retain formal global equations and residual attachment,
respectively; neither is replaced by conductor lengths.

[R-0003](../results/fixed_carrier_conductor_criterion.md) and
[R-0036](../results/pointwise_conductor_socle_defect.md) use conductors
of carrier normalizations with their own hypotheses. The map here is
a finite modification of the entire nonreduced intersection; those
carrier criteria are not being reapplied without their assumptions.

The remaining bridge is global: determine whether such moving W with
these two actual endpoint pinching algebras can have an image generated
by two homogeneous equations. Local Gorenstein contraction, conductor
self-duality and a numerical genus match do not answer that question.
The separately reviewed [moving primitive control](2026-10-31-moving-family-descent.md)
realizes positive movement and both Gorenstein contractions for every
m≥2, while its projective image fails the global two-equation condition.
Likewise pulling back a candidate subcanonical line-bundle identity
to W can lose endpoint descent data; equality of the pulled-back
bundles is not asserted sufficient for equality on Z. This proposal
preserves an exact boundary formulation and rejects the claimed
shortcut from the conductor identity to a uniform contradiction.
The full-conductor unit and characteristic-zero logarithmic descent
mechanism is already recorded in the
[October 27 conductor interface](2026-10-27-absorption-characteristic-conductor-interface.md)
and is not a new conclusion here.
