# Independent review: cubic contraction, conductor and realization charts

Date: 2026-10-21. Reviewer: `incidence_audit` worker.

Status: **PASS for the scoped bridges and chart exclusions described
below; no canonical promotion and no full conditional emptiness claim.**
This review uses saved source notes and executable certificates, not
unsaved worker conclusions. All actual-pair implications retain the
fixed `C0`, characteristic zero, degrees `(6,16)`, FULL generic coprime
ordinary initial CI `(2,12)`, ACTUAL saturated movement-two first
relation, and sole reduced support `C0`.

## 1. The explicit cubic contraction

The reviewed source is
[the cubic-image and conductor-interface note](2026-10-21-conditional-2-12-cubic-image-and-conductor-interface.md).
The new verifier was run directly:

    /opt/homebrew/bin/M2 --script research/computations/conditional_2_12_cubic_image_2026_10_21.m2

It terminated successfully, checking the five substituted quadratic
relations, dimension four, degree five, projective smoothness, and
resolution ranks `(1,5,5,1)` with shifts `(0,2,3,5)`. These are new
computations, not inherited theorem verifiers. The resolution gives
an arithmetically Cohen--Macaulay type-one ring and canonical sheaf
`O_V(-2)`. Connectedness follows from `H0(O_V)=k`; with smoothness
this gives the required geometric integrality. The off-quadric first
four cubic coordinates recover the original point of `P3`, so the
map is birational onto the integral threefold cut out by those five
equations. No classification of a Fano threefold is needed.

The seven degree-three generators give the relative Rees embedding

    Bl_C0(P3) -> P3 x P6.

The inverse projection from the cubic image has base ideal
`(y0,y1,y2,y3)`. Its scheme of zeros is the smooth conic
`y4*y6-y5^2=0`, so the graph closure is the blowup of that conic.
The image of the original blowup is a closed integral graph with the
same dense open and is exactly that graph closure, scheme-theoretically.
The exceptional divisor is `Q'=2H-E=L-H`; the inverse sections are
the common strict-quadric factor times the four original coordinates,
which have no common zero. **PASS for the graph and blowup bridge.**

Every displayed basis element of `H0(I_C0^2(6))` is a product of two
of the seven cubics. Thus every source sextic descends to a quadric
section `T` on `V`, and its transformed divisor is `phi^*T`.
The five quadratic relations are exactly the kernel dimension
`28-23=5`. The actual-pair quadric-factor exclusion makes `Q'`
absent from that pullback; equivalently `T` does not contain the
conic center. Therefore the pullback is also the strict transform.

The actual integrality deduction uses the literal Consequences in
[R-0001](../results/quartic_carrier_exclusion.md): its audited factor
reduction combines plane, quadric, cubic and quartic exclusions.
Every irreducible factor of `F6` must contain `C0`, and must itself
have the other equation as a mate. Each consequently has degree at
least five. A sextic has only one such factor, with multiplicity one.
Hence `F6`, its strict transform and the descended `T` are integral.
This is a valid use of the canonical scope, including reducible
presentations. It is not an assertion of integrality for arbitrary
members of the 23-dimensional source.

## 2. Canonical ideal and conductor-component genus

Let `nu:Y->T` normalize an actual integral quadric section. The
normal surface `Y` is Cohen--Macaulay. Finite duality, together with
the adjunction `omega_T=O_T`, identifies

    omega_Y = Hom_T(nu_*O_Y,O_T) = I_conductor

as fractional ideals in the common rational function field. The
last equality follows by the multiplier characterization of the
conductor and does not assert that `Y` is Gorenstein.

For the full conductor scheme `Delta`, the exact sequence
`0 -> omega_Y -> O_Y -> O_Delta -> 0` gives depth one for the
nonempty quotient; thus `Delta` is pure Cohen--Macaulay of dimension
one. Since `End(omega_Y)=O_Y` on the normal surface, applying
`Hom(-,omega_Y)` gives

    omega_Delta = Ext1(O_Delta,omega_Y)=O_Delta.

The map `omega_Y -> End(omega_Y)` in this calculation is the
inclusion of the conductor ideal, so the cokernel is precisely
`O_Delta`. This checks the global identification, not merely its
codimension-one restriction. **PASS without a Cartier conductor or
Gorenstein normalization assumption.**

For an integral reduced component `R` of generic conductor
multiplicity one, finite same-dimensional duality gives
`omega_R=Hom_Delta(O_R,omega_Delta)`. Its composition into `O_R`
is generically nonzero because the generic local ring of `Delta`
along `R` is its residue field. Torsion-freeness of `omega_R`
makes the map injective, with finite-length cokernel. Consequently
`2p_a(R)-2<=0`. Other conductor components may carry nilpotents;
none of those steps assumes they are reduced. **PASS for the
arithmetic-genus-at-most-one component lemma.**

## 3. Ramified simple base multiplier: local and global audit

The reviewed saved source is
[the conductor-ramification note](2026-10-21-conditional-2-12-conductor-ramification.md).
At a smooth ramified root point over a simple base zero, its
Weierstrass and parameter-Morse steps preserve the exceptional
parameter `t` and give

    F'=x^2-B(w,t),
    B=(s-t^5 sqrt(u))*(s+t^5 sqrt(u)),
    s(w,0)=w^2/2,       u a unit.

The two factors have degree two in `w` in Weierstrass form and
have no common factor. Nonnormality therefore forces one factor
to be `unit*d^2`, with `d=w-phi(t)`. The other cannot also be a
square: its restriction to `d=0` has odd `t`-valuation five.
It is reduced, so the double cover `y^2=B_+` is normal and is
the full normalization of the original ring. The inclusions are

    R+d R y subset R+R y,        R=k[[w,t]].

An element of the smaller ring is a conductor element precisely
when multiplication by `y` remains in that ring; this forces its
even coefficient as well as its odd coefficient to be divisible
by `d`. Thus the conductor is exactly `d*(R+R y)`. Its curve germ
is `y^2=t^5*unit`, reduced and irreducible with delta invariant
two and generic conductor multiplicity one. These computations
are exact and retain the full conductor scheme.

If its global conductor curve is not contracted by `phi`, it maps
finite birationally to a conductor curve on the normalization of
`T`: it meets the open where `phi` is an isomorphism. Arithmetic
genus can only increase under the resulting finite birational
image. The genus-two cusp therefore contradicts section 2.

If the nonnormal curve is a contracted ruling `W`, its normal
bundle is `O_W + O_W(-1)` and `D|W=O_W`. Since the equation
vanishes to order at least two on `W`, its quadratic normal form
has discriminant in `H0(P1,O(2))`. The local model has quadratic
form `x^2-t^5*unit*d^2`, so the same nonzero discriminant has
order five at that point. Unit changes of normal frame preserve
this order, contradicting total degree two. A curve contained in
`D intersect Q'` is a residual ruling and is covered by this case.

The explicit cubic contraction and actual integrality in section 1
supply all the formerly unresolved global bridges in the saved
ramification note. **PASS for exclusion of a nonnormal curve
through a smooth ramified root over a simple BASE multiplier
zero.** Unramified simple zeros are already isolated `A9` points.
This result does not dispose of repeated base multiplier zeros
or multiplier zeros at root nodes.

## 4. Tiny free-orbit unit certificate and its exact coverage

The persisted new audit

    python3 research/computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py

was run successfully. It compares the full-cubic residuals from
the saved 48-equation source with the candidate residual set
after exact specialization and polynomial reduction; it also
checks the following identity without a Groebner basis. Put

    P=648h^4+45h^2-4,
    E4=3eta/4+369h/16-891h^3/2,
    E8=eta/8+27h/32-81h^3/4.

Then `E4-6E8=18h-324h^3`, and identically over QQ,

    1=((162h^2-1)/4)*P
        +(81h^3+77h/8)*(E4-6E8).

Thus the exact candidate family cannot satisfy the full global
sextic cubic lift, independently of the second ambient or Picard
tests. This is a polynomial unit identity, not just exclusion of
four numerical approximations.

The new exact family ideal-equality verifier was also run:

    /opt/homebrew/bin/M2 --script research/computations/conditional_2_12_cubic_reduction_2026_10_21_family_certificate.m2

It completed with `EXACT_IDEAL_EQUALITY_VERIFIED`, dimension zero
and degree four. It checks both coefficient-matrix inclusions
between the saved first/quadric-cubic family ideal and the
triangular ideal defining `P=0`. This bridges the tiny identity
back to the entire displayed family, rather than just checking
that the four candidate points solve necessary equations.

Coverage was audited separately:

* The normalization `d0=d4=1` uses projective root scaling and
  the actual `C0`-preserving torus. Choosing a fourth root of a
  nonzero ratio gives a finite faithfully flat cover of the
  nonzero-endpoint chart. It covers no endpoint-zero root.
* On that chart, multiplication by the norm complement in
  `k[z]/(D)` has determinant `81*detJ^2`. Thus `detJ!=0` is
  exactly the absence of collisions between roots in different
  rotated cubic-ruling positions. It need not make `D`
  squarefree: repeated roots of `D` with no rotated collision
  are INCLUDED in this exclusion.
* The smaller differentiated quadric test is equivalent to the
  all-strata test precisely on this open: both `z` and the
  multiplier are units in `k[z]/(D)`. No inverse of `D'` is
  used, so repeated roots are not accidentally lost.
* The eight-variable family keeps all four first-correction
  variables. Its ideal-equality and tiny unit certificates do
  not require the separate four-row Schur pivot determinant.
  Hence pivot-rank-drop points on this free-orbit chart are
  included.

An old unpromoted October 20 printed Schur matrix omitted the
term `-d1*d3` in its middle diagonal entry. The October 21
exporters used for these certificates contain that term. The
old printed formula must not be used to redefine this chart.

**PASS on `d0*d4*detJ!=0`; no endpoint or orbit-collision
emptiness follows from this certificate.**

## 5. Endpoint multiplicity lemma and two exact normal forms

Here is an additional actual-pair reduction, independently checked
at the root agent's request. Write `tau=f(-z/2,1)` and assume
`m=ord_0(tau)>0`. The norm lemma gives residual divisor
`R=b^m*unit` on the quadric chart `(z,b)`, where
`C0:b=z^3`. The residual mate divisor `T` has restriction of
degree ten to the ruling `b=0`. It cannot contain that ruling;
actual sole support forces its zero divisor on the ruling to
be precisely ten times its sole intersection point with `C0`.
Thus `T(z,0)=z^10*unit`.

The actual ideal equality on the strict quadric is

    (R,T)=(p,t^10),             t=b-z^3.

Reduce it modulo `b`. The left side becomes `(z^10)`, while
the right side is `(p(z,0),z^30)`. Hence

    ord_z p(z,0)=10.

Substitution `b=z^3` changes a regular power series by an
element of `(z^3)`, so `p(z,z^3)` is divisible by `z^3`.
Its order is exactly `m`, since the exceptional restriction of
`p` is a unit multiple of the saturated root equation. Therefore

    ord_0(tau)>=3.

The same argument in the opposite homogeneous chart gives
`ord_infinity(tau)>=3` whenever that order is positive. A
nonzero binary quartic cannot satisfy both inequalities. Thus,
up to the actual projective/torus scaling and inversion of
`C0`, every remaining endpoint root has one of the two forms

    tau=z^3*(1+z),       or       tau=z^4.

The multiplicity-three case has a nonzero remaining finite
root; a remaining root at infinity would violate the second
endpoint inequality. Torus scaling moves that finite nonzero
root to `-1`. These reductions do not assume the endpoint
multiplier is nonzero and do not divide by it.

**Review outcome:** PASS for the endpoint lemma within the
actual supported-pair scope. It is a finite chart reduction,
not exclusion of either resulting chart. Together with section
4 it leaves the nonzero-endpoint orbit-collision chart and the
two endpoint normal forms for the structured computation.

## 6. Fourth-order endpoint: the retained root and exact nodal modulus

On the endpoint chart `D=4tau=z^4`, the symbol equations give

    a=a0+2b2*z+z^2,
    b=b1*z+b2*z^2,
    c=(b1/2-a0/4)*z^2,
    a0!=0.

The root meets the smooth quadric-direction diagonal only at
`p=(z,w)=(0,0)`, with total intersection length four, where
`w=-2u/v`. It cannot be a reduced two-component survivor: each
`(1,1)` component would meet that diagonal with total degree two,
all at `p`, and would consequently be tangent to the diagonal.
The two smooth components would be tangent to each other, the
already excluded additive Picard stratum. A diagonal component
itself is forbidden by `tau!=0`.

Hence any retained endpoint-four root is integral nodal. Its
tangent quadratic is

    (u+z*v/2)*(a0*u+(b1-a0/2)*z*v).

The two slopes `dw/dz` are therefore

    1,       rho=2*b1/a0-1.

They are nonzero and distinct on the retained open. Distinctness
is the nodal condition. If `rho=0`, the displayed coefficient
`c` is zero identically and the binary root has a constant
direction component, violating finiteness in both rulings.

To check that the modulus is the actual Picard gluing, let the
normalization ruling maps be `z=X1/X0` and `w=Y1/Y0`, each of
degree two. Their degree-two numerators vanish at both node
preimages, so `Y1=c*X1`. Their local slope ratios are
`r_i=c*X0(i)/Y0(i)`. On the other hand the actual identification
of `O_Z(1,-1)` at the two preimages gives

    lambda=Y0(p)*X0(q)/(X0(p)*Y0(q))=r_q/r_p.

Thus `lambda=rho` up to inversion, with no normalization-degree
substitution for the conductor identification. The exact spectral
condition on this chart is

    (2*b1/a0-1)^12=1,           2*b1/a0-1 !=1.

After clearing the unit denominator this is
`(2*b1-a0)^12-a0^12=0` on the stated open. This is a necessary
torsion equation, not an exclusion of its intersection with K1
or higher global lifts. The argument was independently
reconstructed from the root agent's proposed endpoint reduction.
