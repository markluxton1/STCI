# Independent audit: the entire genus-two conductor is a reduced line

Date: 2026-10-10. Auditor: `oct10_genus_two_conductor_audit`.
Status: **PROVED HERE / independent structural audit passed**.

This audit accepts the conductor reduction proposed by the root agent. It
does not exclude mates in the genus-two branch. In particular it proves
neither that the adjoint pencil descends to the normalization nor that the
resolution maps to the blowup of the conductor line in the ambient space.
No canonical frontier file was edited.

## 1. Hypotheses and conclusions

Work over an algebraically closed field of characteristic zero. Let
`X` be an integral nonnormal quartic hypersurface in `P3`, let
`nu:S -> X` be its finite normalization, and let `sigma:M -> S` be a
smooth projective resolution. Write

    H = nu*O_X(1),       L = sigma*H.

Assume the accepted genus-two inputs: `M` is rational, `L^2=4`, and
`K_M.L=-2`. For the generic plane-section conclusion in section 7, use
the accepted fact that a general member of the actual pullback plane
system is smooth integral of genus two. These hypotheses hold in the
accepted genus-two branch for a quartic containing the fixed smooth
rational quartic `C0`; no mate is needed.

Then the following statements concern the **entire conductor schemes**:

1. Every singularity of `S` is rational. No Cartier or Q-Cartier
   hypothesis on `K_S` is needed.
2. The actual conductor ideal `I` on `X` satisfies
   `I = Hom_X(nu*O_S,O_X) = nu*omega_S` and is maximal Cohen--Macaulay.
3. `Gamma=V_X(I)` is a reduced line in `P3`, with no embedded points or
   isolated components.
4. If `D=V_S(I O_S)`, the induced map `p:D -> Gamma` is finite flat of
   degree two and

       p*O_D = O_Gamma (+) O_Gamma(-2)

   as modules, with the second summand canonically the trace-zero part.
   Its quadratic multiplication is a section of `O_Gamma(4)`.
5. `D` is connected Gorenstein, has arithmetic genus one and degree two
   for `H|D`, and `omega_D` is trivial. It can be singular or nonreduced;
   it need not be Cartier on `S`.
6. The quartic equation has generic order exactly two along `Gamma`.
7. A curve of `H`-degree four, such as the curve above `C0`, cannot be a
   component of `D`.

## 2. Rational singularities without assuming a canonical pullback

A normal surface is Cohen--Macaulay, and its dualizing sheaf is a
rank-one reflexive sheaf `omega_S=O_S(K_S)`. Use the same rational top
form to choose compatible canonical Weil divisors on `M` and `S`.
Then `sigma_*K_M=K_S`. Projection formula for intersection with the
Cartier divisor `H` gives

    K_S.H = K_M.sigma*H = -2.

A nonzero section of `omega_S` would define an effective canonical
Weil divisor. Every nonzero effective Weil divisor has positive degree
against the ample Cartier divisor `H`; the zero divisor has degree zero.
Neither can have degree minus two. Thus `H0(S,omega_S)=0`, and proper
Serre duality gives `H2(S,O_S)=0`.

Normality gives `sigma_*O_M=O_S`. The relevant Leray sequence is

    0 -> H1(S,O_S) -> H1(M,O_M)
      -> H0(S,R1 sigma_*O_M) -> H2(S,O_S) -> H2(M,O_M).

Rationality of `M` makes its two displayed higher cohomology groups
zero. Hence `H1(S,O_S)=0` and `H0(S,R1 sigma_*O_M)=0`. The higher direct
image `R1 sigma_*O_M` is coherent and supported on the finite singular
locus. A nonzero sheaf with finite support has nonzero global sections,
so it vanishes. Higher direct images in degrees at least two vanish
because the fibers have dimension at most one. Therefore

    R sigma_*O_M = O_S.

This proves rationality of all singularities of `S`. It also gives
`chi(O_S)=chi(O_M)=1`.

The rational-singularity portion was separately counterchecked by the
subagent `rational_singularity_duality_check`; its argument agreed and
explicitly verified that `K_S` need not be Q-Cartier.

Primary inputs checked: [normality and S2, Stacks 10.157.4](https://stacks.math.columbia.edu/tag/031S),
[proper top-degree duality, Stacks 48.27.1](https://stacks.math.columbia.edu/tag/0FVU),
and [higher direct images versus fiber dimension, Stacks 30.20.9](https://stacks.math.columbia.edu/tag/02V7).

## 3. The canonical Hilbert polynomial

Apply Grothendieck duality to `R sigma_*O_M=O_S`, with the normalized
dualizing complexes `omega_M[2]` and `omega_S[2]`. It gives

    R sigma_*omega_M = omega_S.

This is an equality in the derived category, including vanishing of the
higher direct images. It is valid for a noninvertible `omega_S`.
Projection formula and Riemann--Roch on the smooth rational `M` yield,
for every integer `m`,

    chi(S,omega_S(mH))
      = chi(M,omega_M(mL))
      = 1 + (K_M+mL).(mL)/2
      = 1 + 2m^2 - m.

An independent numerical check is Serre duality followed by
`R sigma_*O_M=O_S`:

    chi(omega_S(mH)) = chi(O_S(-mH))
                    = chi(O_M(-mL)) = 1+2m^2-m.

The exact derived formulas are among [Stacks 48.19, proper and finite duality](https://stacks.math.columbia.edu/tag/0AU3);
the trace identification for rational surface singularities is also
given by [Stacks 54.9.6](https://stacks.math.columbia.edu/tag/0BBU).

## 4. The canonical module is the actual conductor

Put `B=nu_*O_S` and `A=O_X`. Quartic hypersurface adjunction gives
`omega_X=O_X`. Finite duality therefore identifies

    nu_*omega_S = Hom_A(B,A).

The right hand side is the actual conductor ideal. To see the
identification rather than merely a module isomorphism, work locally
inside the common fraction field. An `A`-linear map `B -> A` becomes
multiplication by an element of that field. Evaluating it at `1`
shows that the element is in `A`, and its entire image lies in `A`
exactly when it multiplies `B` into `A`. Thus

    I = {a in A : aB subset A} = Ann_A(B/A) = Hom_A(B,A).

This also shows that `I` is an ideal in both `A` and `B`, so its
extension to `S` is the same ideal, not a larger image ideal.

The finite module `B` is maximal Cohen--Macaulay over `A`: a system of
parameters at a closed point of `X` remains a system of parameters at
each point of its finite inverse image, and `S` is a normal surface,
hence Cohen--Macaulay. Over the Gorenstein surface `A`, the canonical
dual of an MCM module is MCM. Consequently `I` has depth two at closed
points. In the exact sequence

    0 -> I -> A -> O_Gamma -> 0,

the depth lemma gives depth at least one wherever `O_Gamma` is
nonzero at a closed point. Since `I` is generically all of `A`, its
quotient has dimension at most one. The quotient is therefore pure
one-dimensional Cohen--Macaulay; it has no embedded points or isolated
zero-dimensional components.

Its Hilbert polynomial is determined without a conductor assumption:

    chi(O_X(m)) = 2m^2+2,
    chi(I(m))   = 1+2m^2-m,
    chi(O_Gamma(m)) = m+1.

Thus `Gamma` has degree one. Its fundamental cycle consists of one
reduced line with generic multiplicity one. Any nilpotents would be
supported at finitely many points; a pure Cohen--Macaulay curve admits
no nonzero such subsheaf. Hence the scheme itself is that reduced line.

For the CM duality and biduality used here, the relevant primary
statement is [Stacks 47.16.7](https://stacks.math.columbia.edu/tag/0A7M).

## 5. The entire upstairs double cover

Gorenstein MCM biduality gives the **natural** multiplication/evaluation
isomorphism

    Hom_A(I,A) = B.

Dualize `0 -> I -> A -> O_Gamma -> 0`. Since `O_Gamma` is torsion and
`A` is a domain, `Hom_A(O_Gamma,A)=0`. The resulting exact sequence is

    0 -> A -> B -> Ext1_A(O_Gamma,A) -> 0.

Closed-immersion duality and `omega_X=O_X` identify the Ext sheaf with
`omega_Gamma`. It follows that

    B/A = omega_Gamma = O_Gamma(-2).

This is a sheaf identity with its twists, not just a generic length
calculation. Quotienting the common ideal `I` out of `A subset B`
gives the exact sequence on the actual line

    0 -> O_Gamma -> p_*O_D -> O_Gamma(-2) -> 0.

The quotient is locally free, so `p_*O_D` is locally free of rank two.
This proves finite flatness on **all** of `Gamma`, including fibers
above singular points of `S`. Moreover

    Ext1_Gamma(O(-2),O) = H1(P1,O(2)) = 0.

In characteristic zero, the algebra trace satisfies `tr(1)=2`, so
`tr/2` gives a canonical splitting of the inclusion of `O_Gamma`.
Its trace-zero kernel `N` is `O_Gamma(-2)`. Cayley--Hamilton for a
trace-zero element shows that multiplication `N tensor N -> p_*O_D`
lands in `O_Gamma`. It is determined by

    delta in H0(Gamma,N^(-2)) = H0(P1,O(4)).

Locally the algebra is `O_Gamma[w]/(w^2-delta)`. The section `delta`
may be identically zero; in that case the cover is a nonreduced
genus-one ribbon. If it is nonzero, repeated roots and square cases
are still retained. No smoothness or reducedness is imposed on `D`.

No normalization/base-change commutation assertion is used in this
argument. `D` is the quotient by the common conductor ideal, and
its finite flat cover is established directly from the exact sheaves.

## 6. Genus, canonical sheaf, and degree of D

The local monic quadratic presentation is a hypersurface over the
regular line. Therefore `D` is Gorenstein. Its Euler characteristic is

    chi(O_D) = chi(O_P1) + chi(O_P1(-2)) = 1-1 = 0,

and `H0(D,O_D)=k`, so it is connected and has arithmetic genus one.
The cover formula for the dualizing sheaf gives

    omega_D = p*(omega_Gamma tensor N^(-1)) = O_D.

There is also a direct algebraic check of this formula: projection
onto `N=omega_Gamma` gives a functional `p_*O_D -> omega_Gamma`;
its multiplication pairing is perfect. Locally, in the basis `1,w`,
the pairing has matrix with off-diagonal entries `1` and diagonal
entries `0`, hence unit determinant. This identifies the relative
dual with the algebra even when `delta=0`.

Since `H|D=p*O_Gamma(1)`,

    chi(O_D(mH)) = (m+1)+(m-1) = 2m.

Thus its degree is two. All components have positive `H`-degree,
so a curve of degree four cannot be a component of `D`.

This conclusion does **not** make `S` Gorenstein: the conductor ideal
`I O_S=omega_S` need not be invertible. In particular `D` has not
been claimed to be a Cartier divisor on `S`.

## 7. The generic transverse multiplicity is exactly two

Take a general plane `P` transverse to `Gamma`. It meets the conductor
line at one point `p`, and avoids the finitely many images of the
singular points of `S`. Its pullback to `S` is smooth integral of
genus two by the accepted plane-system hypothesis. It is the
normalization of the integral plane quartic `C=X intersect P`.

The equation of `P` is regular on `B/A=O_Gamma(-2)`. Consequently
restricting

    0 -> O_X -> nu_*O_S -> O_Gamma(-2) -> 0

to `P` introduces no Tor term on the left, and gives a length-one
normalization quotient supported at `p`. This is an actual finite
base change (finite pushforward is exact); it does not assume that
normalization commutes with arbitrary base change. Smoothness of
the pulled-back section establishes the normalization here.

Let `m` be the multiplicity of the plane quartic at `p`. The defect
one makes it singular, so `m>=2`. Blow up `P` at `p`. Its strict
transform has arithmetic genus

    3 - m(m-1)/2,

by the divisor class `4h-mE` and the canonical class `-3h+E`.
The normalization still has genus two, and the normalization quotient
has nonnegative length. Therefore

    3-m(m-1)/2 >= 2,

forcing `m<=2`. Hence `m=2`.

At a general transverse slice this equals the order of the quartic
equation in the ideal of the conductor line. Thus the homogeneous
equation belongs to `I_Gamma^2` and not to `I_Gamma^3`. Higher
multiplicity at special points has not been excluded.

## 8. Audit boundary and continuation

Every step of the requested entire-conductor reduction passes. The
argument covers all rational genus-two normalization models with the
stated quartic polarization, including non-Gorenstein normalizations,
nonreduced upstairs conductors, and special conductor fibers.

The next geometric obligation is still open: identify the rational
map from the planes through `Gamma` with the accepted adjoint pencil
and prove that it extends on the chosen resolution. The assertion
that the strict transform in `Bl_Gamma(P3)` is normal requires that
identification or another complete proof. Neither assertion follows
solely from the reduced-line conductor or its double-cover algebra.

The genus-two mate strata, the unrestricted fixed-`C0` question, and
the universal STCI question remain **OPEN**.
