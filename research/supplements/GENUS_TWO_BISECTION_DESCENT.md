# Bisection quadratic compression and split-conductor descent

This is a distinct conditional conductor argument. Under the actual
genus-two bisection hypotheses, the [second-pencil/global ribbon proof](GENUS_TWO_BISECTION_PROOF.md)
provides an actual Cartier double `2c~2H` with a section Q whose entire
divisor is2c. It need not be an ambient quadric. If a degree2n mate existed,
its pullback would be a scalar multiple of Q^n on the normal projective
normalization. The argument below keeps the extra quadratic section and
its full conductor, including nilpotents; it is not an open list of
quartic mates after the global ribbon contradiction.

## 1. The extra quadratic section and its entire conductor restriction

The [entire-conductor audit](GENUS_TWO_ENTIRE_CONDUCTOR_PROOF.md)
gives the actual reduced conductor line `Gamma` and the exact sequence

    0 -> O_X -> nu_*O_S -> O_Gamma(-2) -> 0.

Twisting by two and using the hypersurface restriction sequence gives

    h0(S,2H)=11,
    H0(S,2H)/H0(X,O_X(2))=k.

The ten sections of `O_X(2)` are precisely ambient quadrics. On the entire
upstairs conductor `D`, the canonical trace splitting is

    p_*O_D=O_Gamma (+) O_Gamma(-2),
    w^2=delta, delta in H0(Gamma,O_Gamma(4)).

Here `w` denotes the local trace-zero generator, with its global twist.
After twisting by `2H`, every section restricts in the form

    Q|D=m+a w,
    m in H0(Gamma,O_Gamma(2)), a in k.

The coefficient `a` is zero exactly when the section is ambient. This
follows either from the normalization sequence above or directly from
the exact common-conductor square: a section descends if and only if its
entire restriction to `D` comes from `Gamma`. The trace-zero part of the
normalization quotient is the displayed `O_Gamma(-2)`.

For our `Q`, one must have `a!=0`. Otherwise `Q` would give a quadric
mate for `C0`. Every ambient quadric containing `C0` is a scalar multiple
of the unique smooth quadric

    q=x0 x3 - x1 x2.

On `q=P1 x P1`, the curve has class `(1,3)`, while an integral quartic
carrier cuts class `(4,4)`. A divisor supported only on `C0` would have
class `j(1,3)`, and no positive `j` gives `(4,4)`. Hence this quadric
cannot be a mate. Normalize `Q` so that

    Q|D=m+w.

The restriction is a nonzerodivisor on the CM curve `D`: the divisor of
`Q` has support only `c_S`, and `c_S` cannot be a component of `D`, whose
entire `H`-degree is two rather than four.

## 2. The trace-zero alternative is excluded by the known (4,4) theorem

If `m=0`, then

    Q^2|D=delta

comes from `Gamma`, on the entire conductor including every nilpotent
stratum. The common-conductor square therefore descends `Q^2` to a
section of `O_X(4)`. The hypersurface restriction sequence lifts it to
an ambient quartic. Its pullback has divisor `4c_S`, so its zero set on
`X` is precisely `C0`; finiteness and surjectivity of normalization
justify that full-support conclusion. This gives a `(4,4)` STCI.

The descended ambient quartic is integral and reduced, as required by
the cited surface theorem. Every irreducible factor must contain C0 by
the coprimality/purity factor argument. Nonplanarity rules out a linear
factor; the only possible reducible degree-four case is a product of
two copies of the unique quadric, which would make that quadric a mate
and is excluded by the same divisor-class argument above. Repeated
factors are included in this reasoning.

Craighero--Gattazzo's 1986 theorem excludes exactly this degree pair for
the literal Cremona quartic over an algebraically closed field of
characteristic different from `2,3`, hence in characteristic zero.
The primary PDF was checked live on 2026-10-10: its abstract on printed
page 177 states the characteristic hypotheses, and Proposition 4 on
printed page 187 is the two-quartic exclusion. See
[the primary paper](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf).
This use is only a `(4,4)` exclusion, not an unrestricted non-STCI
theorem. Consequently `m!=0`.

## 3. Every remaining bisection mate has a reduced split conductor

Apply the independently audited
[quadratic power-descent criterion](QUADRATIC_CONDUCTOR_POWER_DESCENT.md)
to the actual nonzerodivisor `m+w`. Since `m!=0` and the trace-zero
coefficient is one, descent of a positive power forces

    m^2=rho delta,
    rho=((1+zeta)/(1-zeta))^2,

where `zeta` is a root of unity different from `1` and `-1`.
The equality is an equality of global quartic sections, including all
special fibers. In particular `delta` is a nonzero square.

Write `delta=r^2` after choosing a constant square root, with
`r in H0(O_Gamma(2))`, and `m=alpha r`. Then `D` is reduced with two
components mapping isomorphically to `Gamma`; they meet at the zero
scheme of `r`. The conductor sections are

    Q_+=(alpha+1)r, Q_-=(alpha-1)r.

Nonzerodivisorship gives `alpha!=1,-1`; the excluded trace-zero case
gives `alpha!=0`. The remaining condition for a power to descend is

    ((alpha+1)/(alpha-1))^n=1.

Conversely this equality implies descent on the entire reduced `D`,
since equality on its two generic components implies equality of the
sections on a reduced scheme. No unbounded root-of-unity order has been
replaced by a finite search. If the ratio has order `n`, the compressed
mate degree is `2n`, with `n>=3`.

Thus this branch now requires a **reduced split genus-one conductor**
and a constant root-of-unity ratio. The nonreduced `delta=0` branch and
all nonsplit quadratic-cover branches are excluded for a bisection
mate; they were retained through the reduction rather than assumed
away at the start.



## 4. Entire contact schemes under the split-descent assumptions

This conditional lemma uses the hypothetical bisection and split-descent assumptions just obtained; its argument was independently accepted. The stronger global ribbon proof excludes the lane without these conductor refinements.

Every exceptional fiber met by c has positive correction and
lies wholly in Supp(Z), by the support-closure argument. Thus
its graph is entirely vertical (-2). In the accepted normal ADE
ambient conic model T these graphs are contracted, while only
horizontal (-3) curves can be contracted by T->S. Therefore S
is ADE near c_S, and in particular Gorenstein there. Its actual
conductor ideal is omega_S and is locally invertible. Hence D
is Cartier near every point of c_S intersecting D.

Let d be its local Cartier equation at such a point. On the
ribbon R_C, d meets the reduction properly and is a
nonzerodivisor on both O_(c_S) and J. Quotienting the ribbon
sequence by d shows

    length(O_(R_C)/(d))=2*length(O_(c_S)/(d)).

In the split conductor algebra with Q=m+w=alpha r+w, the
quotient by Q is locally O_Gamma/(r^2), since alpha^2-1 is
nonzero. Its length at a zero of r is twice the order of r.
These two lengths describe the same scheme R_C intersect D.
The common conductor ideal pulled to c_S is precisely the
ambient ideal of Gamma intersect C0. Its degree is two in
the accepted bisection line-position theorem. Therefore

    div_Gamma(r)=Gamma intersect C0

as entire degree-two schemes, not just as supports. At a
simple contact, Q has order one on each of the smooth split
conductor components; a smooth S would make c_S Cartier and
Q a unit times its squared equation, forcing even order on
each component. Thus each simple contact would be singular
on S. A tangent double contact is not excluded by that
parity observation alone.

The existence of the forced global ribbon, however, has
already contradicted the balanced normal bundle regardless
of these contact types.



## Scope and characteristic

The normalization sequence, trace-zero global section, degree-four descent
and split-conductor phase are the mechanisms of this alternative proof.
Its support/purity statements are algebraic; the trace splitting requires
two invertible, and the all-powers torsion/nilpotent argument used here is
characteristic zero. The particular (4,4) input has its own published
characteristic restrictions. In positive characteristic, Frobenius can
remove nilpotent conductor obstructions, and no all-characteristic quartic
exclusion is inferred. The actual fixed C0 has quartic-carrier STCI
presentations in every positive characteristic.
