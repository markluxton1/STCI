# Every genus-one quartic normalization containing C0 is a degree-four weak del Pezzo model

Date: 2026-10-09. Owner: root. Status: **PROVED HERE, independently
accepted in the bounded audit below**. This establishes the hypotheses
of the del Pezzo root-lattice reduction. It does not exclude every
genus-one normalization or supply a mate on any of them.

Let k be algebraically closed of characteristic zero. Let X in P3 be
an integral nonnormal quartic containing the smooth rational quartic
C0, let nu:S->X be its finite normalization, and let
H=nu*O_X(1). Suppose its normalization sectional genus is pi=1.
The proof does not require a mate.

The accepted [nonrational-normalization theorem](2026-10-09-session-nonrational-quartic-normalizations.md)
shows that S is rational. Let sigma:M->S be its minimal smooth
resolution and L=sigma*H. Then L is a nef and big Cartier divisor,
L^2=4, and a general smooth hyperplane curve of class L has genus
one. Adjunction gives

    K_M.L=-4,       (K_M+L).L=0.

## 1. The adjoint has a unique effective representative

The smooth projective surface M is rational, so chi(O_M)=1.
Characteristic-zero Kawamata--Viehweg vanishing for the nef and big
L gives Hi(M,K_M+L)=0 for i>0. Surface Riemann--Roch therefore gives

    h0(M,K_M+L)=chi(K_M+L)
      =1+(K_M+L).L/2=1.

Choose the effective divisor D of that nonzero section. Thus
D~K_M+L and L.D=0. Since L is the pullback of an ample divisor
under sigma, any prime curve not contracted by sigma has positive
L-degree. Consequently every prime component of D is exceptional.
No rational-singularity or Gorenstein assumption on S was used here.

## 2. Minimality and negative definiteness force D=0

The exceptional intersection matrix of a resolution of a normal
surface is negative definite. Every exceptional integral prime E
therefore has E^2<0. Minimality excludes an exceptional smooth
rational curve of self-intersection -1, since it could be contracted
to give a smaller smooth resolution over S. Adjunction consequently
gives

    K_M.E=2 p_a(E)-2-E^2 >= 0.

Indeed, if p_a(E)=0 then E is a smooth rational curve, so E^2<=-2;
if p_a(E)>=1 then the displayed intersection is positive. Since
L.E=0, one also has D.E=K_M.E>=0 for every exceptional prime.
Writing the effective divisor as D=sum d_i E_i now gives

    D^2=sum d_i (D.E_i) >= 0.

This contradicts negative definiteness unless D=0. Hence the unique
adjoint section has no zeros and

    K_M~ -L,       K_M^2=4.

In particular M is a rational weak del Pezzo surface of degree four:
its anticanonical line bundle is nef and big. The curves contracted
by sigma have anticanonical degree zero.

## 3. The normalization is Gorenstein del Pezzo with ADE singularities

To make the crepant conclusion precise, choose an actual hyperplane
divisor H0 in |H|, whose pullback is L0 in |L|. The linear equivalence
K_M~ -L lets us choose a rational two-form omega on M with

    div_M(omega)=-L0.

Use the same rational two-form on S, which has the same function
field. Pushing its divisor forward gives the canonical Weil divisor

    K_S=div_S(omega)=-H0.

It is Cartier, and its negative is ample. Moreover these choices give
the actual equality of divisors

    K_M=sigma* K_S.

Thus sigma is crepant. The standard surface characterization of
Du Val singularities by a crepant resolution applies. The primary
author-hosted statement is [Miles Reid, The Du Val singularities,
Theorem 2.1(2)](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
Accordingly S has only ADE singularities and is a normal Gorenstein
del Pezzo surface of degree four. This conclusion comes from the
adjoint argument; it is not an assumed classification hypothesis.
The usual characteristic-zero form of this surface result applies;
equivalently the finite coefficients and resolution data descend to
a finitely generated field that embeds in C, where Reid's stated
characterization applies, and the resulting intersection and crepant
properties transfer back.

## 4. Relation to a hypothetical mate and the root-lattice task

Under a mate of degree b, the accepted full-support theorem gives a
smooth lifted curve c isomorphic to C0 and b c~bH on S. Its strict
transform c# on M is also smooth. The Cartier pullback supplies an
effective rational exceptional correction Z with

    c#+Z numerically equivalent to L,       -Z^2=2 pi=2.

The previous [sectional-genus proof](2026-10-09-session-normalization-sectional-genus-zero.md)
establishes this identity without assuming that c is Cartier. On the
rational weak del Pezzo M, the integral class L-c# realizes Z in
the saturation of the exceptional root lattice inside the
anticanonical orthogonal lattice D5. Thus the forthcoming D5 torsion
filter is applicable to every remaining genus-one normalization,
once its own lattice proof is accepted. The classification of that
lattice filter and the exclusion of any surviving conductor types
are separate obligations.

The displayed [four-A1 family](2026-10-09-session-singular-delpezzo-four-A1-family.md)
already realizes the order-two correction in an actual normalization,
then fails the full-fiber condition. It does not represent every
possible projection of a four-A1 surface. Genus-two rational
normalizations, higher carrier degrees, and entirely thick
presentations are outside this theorem.

## 5. Audit and source scope

The independent auditor `normal_global_adversarial` accepted the
KV/Riemann--Roch calculation, exceptional support, all exceptional
prime adjunction inequalities on the minimal resolution, negative
definiteness, and the chosen-canonical-form crepant equality before
this owner note was written. Its standalone audit is recorded in
the October 9 acceptance record once frozen. No new computational
test is needed for these divisor arguments. The source inputs are
the standard characteristic-zero nef-big vanishing theorem, surface
Riemann--Roch, negative definiteness on a normal-surface resolution,
and the explicitly linked Du Val characterization.
