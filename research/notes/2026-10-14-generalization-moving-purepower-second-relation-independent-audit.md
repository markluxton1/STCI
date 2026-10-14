# Moving pure-power first relations: a uniform second-relation obstruction

Date: 2026-10-14. Status: **independently proved new obstruction and exact
degree identity** under the hypotheses stated below. The previously accepted
normal-layer defect convention and first-relation gap cost are premises; they
are not replayed here. The new apolar quotient is independently established in
[the finite-order tower audit](2026-10-14-generalization-moving-purepower-tower-independent-audit.md).

## 1. Bundle setting and the new second relation

Let `C` be a smooth integral projective curve in characteristic zero, with
balanced conormal bundle

    E=H^-1 tensor V,

where `V` is a constant two-dimensional vector space. Let

    M subset V tensor O_C,   deg M=-e<0,
    W=H^-1 tensor M,
    L=E/W=H^-1 tensor det(V) tensor M^-1.

Assume the first generic initial relation is the pure power `m^r`, with
`r>=2`. Let `s>r` be the next independent generic relation degree, and put
`g=s-r`. At the generic point, assume that this new binary form is coprime
to `m`; in particular this holds when the generic initial ideal is the
complete intersection `(m^r,g_s)`.

Write `K_s` for the actual degree-`s` relation kernel inside `Sym^s E`.
The saturated space of multiples of the first relation is

    A_prior=W^r tensor Sym^g E subset Sym^s E.

It is a rank-`g+1` subbundle. Define

    U_s=K_s intersection A_prior,
    T=K_s/U_s subset A_s,
    A_s=Sym^s E/A_prior.

The intersection and the quotient are taken as actual sheaves. The map to
`A_s` identifies `T` with a torsion-free rank-one subsheaf, so `T` is a line
bundle on the smooth curve. It need not be a subbundle at special points.
This definition does not identify a generic generator with a globally
saturated special-fiber generator.

The apolar quotient formula, including its constant factor, is

    A_s=H^-s tensor M^(-(g+1))
        tensor det(V)^(g+1) tensor Sym^(r-1)V.

Restriction to the quotient direction `E -> L` induces a canonical map

    A_s -> L^s.

The assumed generic coprimality makes its restriction to `T` nonzero.
Consequently there is an effective divisor `D` such that

    T=L^s(-D).

Here `D` is the actual zero divisor of this map, including any failure of the
subsheaf `T` to remain a subbundle. It is not discarded by saturation.

## 2. Uniform coprimality is impossible for a moving power of order at least two

Suppose the full initial algebra is a complete intersection of degrees
`r<s` on every fiber, with its first generator the line `W^r` and first
generator `m^r`. Then `T` is the second generator line and the map
`T -> L^s` is nowhere zero: a binary form is coprime to `m` exactly when
its restriction to `m=0` is nonzero. Thus `D=0` and `T=L^s`.

But the natural inclusion `T -> A_s` would then be a nonzero section of

    Hom(L^s,A_s)
      = M^(r-1) tensor det(V)^(1-r) tensor Sym^(r-1)V.

The final two factors are constant. Since `(r-1)deg M<0`, this bundle has
no global section on an integral projective curve. This is a contradiction.

Therefore a pure-power first relation of order `r>=2` in a genuinely moving
basepoint-free direction cannot extend to a fiberwise complete-intersection
initial algebra of two distinct generator degrees. The conclusion is
uniform in `r` and `s`. It does not exclude merely generic complete
intersection initial algebras with special-point defects, nor the linear
case `r=1`.

## 3. Generic coprimality forces an effective degeneration cost

In the generic situation of Section 1, the nonzero inclusion `T -> A_s`
instead defines a section of

    Hom(T,A_s)
      = M^(r-1)(D) tensor det(V)^(1-r) tensor Sym^(r-1)V.

A line bundle carrying a nonzero section has nonnegative degree. Hence,
writing `delta=deg D`,

    delta >= (r-1)e.

This includes subsheaf zeros and the special-point loss of coprimality in
one intrinsic divisor. No special fiber is assumed to retain its generic
minimal-generator presentation. If equality holds, the line bundle
`M^(r-1)(D)` is trivial; this follows because its nonzero section has an
effective zero divisor of degree zero. On `P^1`, its corresponding map into
the constant factor of `A_s` is a constant binary form of degree `r-1`.
Its evaluation divisor is the pullback of that form's root divisor by the
moving direction map. This equality description is not needed for the
inequality.

## 4. Exact degree-s defect, retaining the first relation's pole divisor

The first relation may itself have an effective defect divisor:

    K_r=W^r(-D0),       delta0=deg D0.

Multiplication of this actual relation by degree-`g` normal forms gives

    A_prior(-D0) subset U_s subset A_prior.

Both `U_s` and `A_prior` have rank `g+1`, so put

    tau=length(A_prior/U_s)>=0.

This retains the defect of the old relation multiples at the new-generator
degree. For example `D0=0` forces `tau=0`; in general
`tau<=(g+1)delta0`.

Let `lambda=deg H`. By definition of the accepted normal-layer defect,
with `rank K_s=g+2`,

    Delta_s=-deg K_s-lambda s(g+2).

The exact sequence `0 -> U_s -> K_s -> T -> 0` gives

    deg A_prior=-lambda s(g+1)-r e(g+1),
    deg U_s=deg A_prior-tau,
    deg T=-lambda s+s e-delta.

Adding these degrees yields the new exact identity

    Delta_s=e g(r-1)+delta+tau.

Consequently,

    Delta_s >= e(r-1)(g+1)+tau
             >= e(r-1)(g+1).

This calculation uses the actual degree-`s` kernel and the actual divisor
`D`. It does not silently replace either by its saturation. The identity
holds on any smooth projective support curve with the stated balanced
conormal and generic relation ranks.

## 5. Combination with the accepted earlier-gap cost

The accepted first-relation gap calculation has movement degree
`epsilon=r e` for the pure power. The sum of its defects in degrees
`r,...,s-1` is therefore at least

    r e g(g+1)/2+delta0.

The remaining normal-layer defects are nonnegative. Adding the new
degree-`s` bound gives

    Delta >= r e g(g+1)/2+delta0
             +e(r-1)(g+1)+tau.

In particular, omitting only the explicitly nonnegative `tau` proves the
proposed lower bound

    Delta >= r e g(g+1)/2+delta0+e(r-1)(g+1).

For the accepted rational-quartic exact socle budget
`n mu=7 Asym+2 Delta`, this entails the necessary condition

    n mu >= 7 Asym+r e g(g+1)+2delta0
            +2e(r-1)(g+1)+2tau.

It is a uniform obstruction cost, rather than a complete exclusion of all
moving generic initial complete intersections. The gap can be one; unlike
the separate constant-direction quadratic pole obstruction, no gap-at-least-
two hypothesis is needed here.

## 6. Audit verdict and frontier meaning

**Pass.** The new fiberwise exclusion, generic divisor bound, exact
`Delta_s` identity, and combination with the already accepted gap cost
follow from the quotient bundle and the actual sheaf degree sequences.

The first relation's divisor `D0`, the old-multiple defect `tau`, and the
evaluation divisor `D` are distinct and are all retained. The finite-order
existence theorem in the companion audit is compatible with this exclusion:
it adds a full truncation relation at its last degree, and for `r>1` its
top layer already has socle dimension at least `r`. A future complete-
intersection second relation must pay the new divisor cost; it cannot be
inserted with fiberwise coprimality and zero defects.
