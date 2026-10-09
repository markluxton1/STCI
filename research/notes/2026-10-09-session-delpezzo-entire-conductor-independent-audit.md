# Independent audit: the entire ADE del Pezzo conductor

**Accepted as a conditional structural theorem in characteristic zero.**
The audited proof is
[2026-10-09-session-delpezzo-entire-conductor.md](2026-10-09-session-delpezzo-entire-conductor.md).
No canonical files were edited and no additional agents were used.

The hypotheses are a finite normalization `nu:S -> X` of an integral quartic
surface in `P3`, with `S` a rational normal degree-four del Pezzo surface
having only ADE singularities, and
`H=nu^*O_X(1)=-K_S` ample Cartier, `H^2=4`. Every conductor scheme mentioned
below is the actual scheme defined by the conductor ideal, including its
nilpotents.

**Canonical modules and the actual Cartier conductor.** The Gorenstein
quartic has `omega_X` isomorphic to `O_X`. After choosing this trivialization,
finite absolute duality identifies `nu_*omega_S` with
`Hom_OX(nu_*O_S,O_X)`, compatibly with the normalization algebra action.
Locally every such homomorphism is multiplication by a fraction `r`; the
condition `1 in B` forces `r in A`, and its defining condition is precisely
`rB subset A`. This is the actual conductor ideal `I`, which is also an ideal
of `B` and satisfies `IB=I`. Since `omega_S=O_S(-H)` is invertible, its
embedding in `O_S` defines an effective Cartier divisor `D~H`, including at
ADE points. Here `I O_S` means the extended ideal, not an assertion that the
unmodified tensor pullback has no torsion.

**Vanishing and arithmetic Cohen--Macaulayness.** On the crepant rational
resolution `mu:M -> S`, put `A_M=mu^*H`. It is nef and big and
`K_M=-A_M`. For every `n>=0`, Kawamata--Viehweg vanishing applies to
`nA_M=K_M+(n+1)A_M`. Rational resolution and projection formula transfer the
vanishing to `S`. Gorenstein Serre duality transfers it to every negative
integer as well, giving `H1(S,O_S(nH))=0` for all integers `n`. The proof uses
the standard characteristic-zero vanishing theorem; this audit does not
claim a newly verified publisher full-text source.

The preimage ideal sequence
`0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0` is exact for the actual
conductor. Vanishing of both intermediate line-bundle cohomology groups on
`P3` therefore gives `H1(P3,J_Gamma(m))=0` for every integer `m`.

**Purity and classification of the entire downstairs scheme.** The
normalization and its canonical module are maximal Cohen--Macaulay over the
local hypersurface ring: parameters from that ring remain parameters at the
finite normalization points. Hence `I` has depth two at each closed point of
`X`. The depth lemma for `0 -> I -> O_X -> O_Gamma -> 0` forces every nonzero
conductor quotient at a closed point to have depth at least one. Its
dimension is at most one, so there are no embedded or isolated
zero-dimensional components. The Hilbert polynomial computed below ensures
that the curve is nonempty. Thus `Gamma` is pure Cohen--Macaulay, and the
all-twist ideal vanishing makes its saturated coordinate ring ACM.

Riemann--Roch on the rational resolution gives
`chi(O_S(nH))=1+2n(n+1)`. Consequently
`chi(O_Gamma(m))=(2m^2+2)-(1+2(m-1)m)=2m+1`. An Artinian reduction of the
ACM coordinate ring has a nonnegative Hilbert function with sum two and
weighted sum one, hence exactly `h=(1,1)`. Its degree-one coordinate piece
has dimension three, so precisely one independent plane equation belongs
to the ideal. Within that plane its coordinate ring is Cohen--Macaulay of
codimension one in a polynomial ring of dimension three. Auslander--Buchsbaum
makes its ideal a free graded rank-one module, hence principal; the Hilbert
series gives a degree-two generator. Therefore the actual saturated ideal is
a complete intersection `(ell,Q2)`. This proves that `Gamma` is a smooth
conic, two meeting distinct lines, or the plane double-line scheme, rather
than a classification merely of its reduced support. Adjunction gives
`omega_Gamma=O_Gamma(-1)`.

**Duality and finite flatness on the entire schemes.** Over a Gorenstein
local surface ring `A`, MCM duality gives
`I=Hom_A(B,A)`, `Hom_A(I,A)=B`, and the requisite positive Ext vanishing.
Applying the dual to `0 -> I -> A -> A/I -> 0` identifies the natural
quotient `B/A` with the codimension-one canonical module. Globalizing gives
`nu_*O_S/O_X=omega_Gamma` (with the fixed trivialization of `omega_X`). Since
`I` is the same ideal in both rings, quotienting by it gives

\[
0\longrightarrow O_\Gamma\longrightarrow p_*O_D
\longrightarrow \omega_\Gamma\longrightarrow0.
\]

The right-hand module is invertible, so this sequence splits locally as
modules even at a nodal or nonreduced point. Its middle module is locally
free of rank two. The finite morphism `p` is therefore finite flat of degree
two without assuming reducedness or smoothness of either conductor scheme.

**The trace involution includes nilpotents.** Trace of multiplication by
`1` is two, so in characteristic zero the algebra has the canonical module
decomposition `p_*O_D=O_Gamma direct_sum N`, with
`N=ker(trace)` isomorphic to `omega_Gamma`. For a local generator `z` of
`N`, Cayley--Hamilton makes `z^2` a scalar in `O_Gamma`. Thus the map fixing
the scalar algebra and negating `N` is an algebra involution; changes of
trace-zero generator show that these local maps glue. This calculation is
valid over arbitrary nonreduced base rings. Its invariant algebra is exactly
`O_Gamma` because two is invertible.

**Upstairs data and the surviving boundary.** Cartier adjunction gives
`omega_D=O_D`. The all-twist vanishing applied to
`0 -> O_S(-H) -> O_S -> O_D -> 0` gives `H0(D,O_D)=k`, hence connectedness.
Its Hilbert polynomial is `4m`, so its arithmetic genus is one. These facts
do not imply that `D` is reduced, smooth, or disjoint from the ADE points.
The earlier ramification-parity argument for a smooth elliptic conductor
cannot be transferred to these singular or nonreduced cases without an
additional proof. The present theorem supplies the full conductor algebra
and involution, but by itself supplies no mate exclusion or quadratic
descent theorem.
