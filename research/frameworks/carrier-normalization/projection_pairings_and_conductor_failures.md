# Projection pairings and conductor descent failures

[Carrier Framework](index.md) · [Original section addresses](normalization_conductor_projection.md)

## Opposite-ruling pairing and the sparse-family boundary

On the smooth quadric with diagonal \(c\), the specified pairing ((x,0)\leftrightarrow(0,ax)), \(a\ne0,-1\), forces phase (a^{-2}) and permits the **full form within this pairing**
\[
U(x,y)=W_0+\frac{ax+y}{a+1}W_1+
(a^2x^2+y^2-(a^2+1)xy)D+
xy\bigl(xE+y(W_2-E)\bigr)+x^2y^2W_3,
\]
where \(D,E\in k^4\) are arbitrary. The sparse choice \(D=W_2,E=uW_2\) is finite but has extra inverse points mapping to ([0:0:0:1]): (\(\infty,-a^2/u\)) when \(u\ne0\), and ((-1/(1-u),\infty)) when \(u\ne1\). The boundary coefficient pairs of the full form are (a^2D+yE+y^2W_3) and (D+x(W_2-E)+x^2W_3), which can avoid these particular sparse-family defects. Thus only the **sparse family** is excluded. Sources: [current proof](../../arguments/carriers/projection_support_differential_obstructions.md#the-opposite-ruling-pairing-and-its-complete-coefficient-freedom), [current proof](../../arguments/spectral/spectral_pushforward_powers.md#2026-10-14-quadric-opposite-ruling-phase-family-failure).



## Divisor-lattice failure and additive conductor failure

The imported Space Curves III examples illustrate distinct obstructions within the fixed-carrier criterion, and should not be conflated.

* Cuspidal cubic: on the carrier y^3-x^2 z=0, the necessary divisor proportionality holds on normalization, but the nonreduced conductor quotient has a nonzero additive polar term -3 z^(-2). This prevents descent of every positive power in characteristic zero. The symbolic companion checks an explicit Cartier identity and a conductor restriction, but does not independently prove the global conductor identification.
* Ruled cubic: on x z^2-y^2 w=0, local pinch-point torsion is compatible with descent of a power, but normalization classes H=(2,1) and lifted C=(2,0) are not positively proportional. Here the obstruction is already in the normalization divisor lattice, not in the local conductor unit group.

These are historical examples, not new exclusions of unaddressed carrier degrees. Source: research/archive/space-curves-2026-10-19/README.md, section 4, and its linked Space Curves III artifacts and symbolic companion. The imported status is historical/source-reviewed, with its stated review scope.



## A rank-two scroll conductor: three distinct algebras

The October 8 adversarial source proves a conditional result for an integral quartic carrier normalized by a smooth rational quartic scroll, generically regular along C0. If the actual conductor center is a smooth twisted cubic Gamma and its upstairs conductor D maps finite flat of rank two to Gamma, there is no mate in any degree. Crucially D need not be reduced.

Finite duality gives the actual upstairs conductor divisor D linearly equivalent to -K_S. The rank-two algebra on Gamma=P1 splits by trace as O + O(-2) eta, with eta^2=Delta, Delta a quartic section. The proof separates:

* Integral reduced D: invariance of a descending power forces the square of the upstairs primitive section to descend. This produces a quadric cutting C0 on the quartic carrier, contradicting the unique smooth quadric's bidegree (1,3) against the carrier intersection class (4,4).
* Reducible reduced D: Delta=q2^2. The two branches glue modulo q2, including tangencies. Their section restrictions differ by a root of unity. Nontrivial phase forces simultaneous branch contact exceeding their mutual intersection multiplicity, impossible for a third smooth branch by a local Taylor expansion.
* Nonreduced D: Delta=0, eta^2=0. If f=a+b eta, descent of f^n forces n a^(n-1)b=0; characteristic zero and a nonzero force b=0, so f itself descends, producing an impossible hyperplane.

The source also proves that assuming the *entire nonnormal support* is a smooth twisted cubic suffices to recover the conductor hypotheses: the actual conductor center has Hilbert polynomial 3m+1, is pure Cohen-Macaulay and therefore reduced on its smooth degree-three support; upstairs D is finite flat of rank two by torsion-freeness over Gamma and H.D=6. A further applicability argument proves every integral quartic singular along a smooth twisted cubic has this scroll normalization: the space of quartics singular along the cubic is the six-dimensional span of products of its three quadratic generators, and integrality gives a smooth conic in the associated quadratic-map target. The incidence blowup identifies its normalization as a smooth quartic scroll. The source reports independent exact symbolic checks of the derivative matrix and rank. These statements remain scoped to a smooth twisted-cubic singular support; singular or reducible degenerations are not covered. Moreover quartic carriers are already excluded for C0 by R-0001, so this is valuable mechanism and geometry rather than a newly open quartic case.

Source: [current proof](../../arguments/carriers/quartic_scroll_reduced_conductors.md) and its cited applicability and computation companions. The argument is retained without generalizing its rank-two conductor hypotheses to arbitrary scroll projections.



## Nonreduced ramification is not determined by full support

The exact local model X: X^2+Y^2(Y+Z^2)=0 has normalization k[w,z] via X=-w^3-wz^2, Y=-w^2-z^2, Z=z. Its actual conductor is YB and its relative differential Fitting ideal is (w,z^2), a length-two ramification scheme. The smooth image curve X=-2Z^3, Y=-2Z^2 has lift c=(w-z), and the full pulled-back curve ideal is (w-z)(w+z,z^2), so the *full reduced inverse support* is c. Nevertheless the ramification scheme is not contained scheme-theoretically in c, since w-z maps to -z modulo (w,z^2).

More generally for c_f=(w-f\(z\)), h=ord\(f\) and r=ord(f^2+z^2), the source computes length(R intersect c_f)=min(h,2), with scheme containment exactly when h>=2. Choosing f=iz+z^k gives unbounded conductor contact r=k+1 but ramification intersection length one. The local Jacobian factorization J_X B=\(Y\) I_R yields first-normal vanishing order s=r+min(h,2). This blocks the unsupported inference from smooth image plus full inverse support to containment of nonreduced ramification. It is a local counterexample, **not** an STCI presentation or a global normalization classification.

Source: the historical [ramification counterexample proof](../../arguments/carriers/ramification_and_socle_controls.md#source-2026-10-07-session-ramification-scheme-counterexamplemd). Its symbolic checker was retired after the explicit model and scheme-theoretic distinctions were preserved. These local distinctions should be preserved in future conductor/ramification arguments.


