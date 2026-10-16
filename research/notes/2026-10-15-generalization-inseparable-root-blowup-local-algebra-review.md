# Local-algebra review of the inseparable-root blowup repair

Date: 2026-10-15. Reviewer: `inseparable_blowup_bridge`.
Status: **PASS for the new generic standard-basis, actual divided-ideal,
and root-prime length arguments in Sections 2--3 of the owner note.**
This is a focused written review of the new characteristic extension;
it does not reaudit the accepted characteristic-zero bridge, replay a
certificate, or certify the separate formal nonexistence theorem.

Reviewed source:
[the inseparable-root bridge owner note](2026-10-15-generalization-inseparable-root-blowup-bridge.md).

## 1. The generator change is valid in the uncompleted ring

Use the owner's notation

    A=O_(X,eta_C), m=I_C A, K=A/m, I=(F,G)A.

The ring `A` is regular local of dimension two, and `I` is `m`-primary.
The full initial ideal hypothesis is

    in_m(I)=(f_r,g_s) in gr_m(A)=K[x,y].

Choose an original equation `P` with degree-`r` initial form `f_r`,
up to multiplication by a lifted unit. The element `g_s` belongs to
the degree-`s` part of the initial ideal, which is the image of
`I intersect m^s` in `m^s/m^(s+1)`. Thus an actual element `H in I`
with initial form exactly `g_s` exists. It is not merely a formal
lift after completion.

For `J=(P,H)`, the inclusions

    (f_r,g_s) subset in_m(J) subset in_m(I)=(f_r,g_s)

give equality. Cancellation of the initial form of any element of
`I` raises its order using coefficients lifted from `gr_m(A)`. After
finitely many cancellations, that element lies in `J+m^n`, for each
fixed `n`. Consequently

    I/J subset intersection_n m^n(A/J)=0

by Krull intersection in the finite `A`-module `A/J`. This proves
`I=(P,H)` before completion. In particular there is no convergence
assumption on an infinite division process.

Both pairs `(F,G)` and `(P,H)` minimally generate the same height-two
ideal: one generator would violate the principal ideal theorem.
If `(P,H)^t=M(F,G)^t`, reduction on the two-dimensional space
`I/mI` makes `M mod m` invertible. Therefore `det M` is an actual
unit of `A`, so `M in GL_2(A)`. This is the unit condition needed on
the blowup; equality of abstract initial ideals alone is not being
used as an unsupported change of strict-transform equations.

## 2. The common division exponent retains the actual intersection

Blowup commutes with localization at `eta_C`. On a chart of
`Bl_m Spec A` with exceptional equation `u`, the pullback of `M`
remains invertible. Both original equations have order `r`, so the
intersection of their individual strict-transform divisors has ideal

    (F/u^r,G/u^r)=(P/u^r,H/u^r)
                  =(P/u^r,u^(s-r)*(H/u^s)).

All quotients displayed here are regular functions on the chosen
chart, since `m O_B=(u)`. The retained factor `u^(s-r)` is essential.
The second equation after the generator change is the divided
equation `H/u^r`; it is not the individual strict transform `H/u^s`.

This target is the **intersection of the strict transforms of the
original two divisors**. It is not the strict transform of the
supported intersection `Y` itself: `Y` has empty restriction away
from the center, so its strict transform defined by closure from
that open set is empty. In particular, saturating the divided ideal
by `u` would destroy the supported strict intersection. No such
saturation occurs in the owner argument.

## 3. The generic local length needs a reduced prime, not separability

Let `xi` be the generic point of a component of the actual smooth
root divisor. All these components dominate `C`: the actual
line-subbundle hypothesis prevents the binary root form from
vanishing on an entire exceptional fiber. On a chart `x=u,y=uv`,
the ring

    T=O_(Bl_m Spec A,xi)

is regular local of dimension two, with

    T/(u)=K[v]_(q),
    T/m_T=K'=K[v]/(q).

Here `q` is the irreducible polynomial defining the actual root
prime. Reducedness of the actual root divisor implies reducedness
after localization to the generic point of `C`. Thus the prime
factor `q` occurs to exponent one in `f_r(1,v)` over `K`. This
statement does not assert that `q` has a nonzero derivative or
distinct roots after algebraic closure. It remains valid when
`K'/K` is inseparable.

Set `p=P/u^r` and `a=H/u^s`. The reduction of `p` modulo `u`
is a unit times `q` in the DVR `K[v]_(q)`. Therefore

    m_T=(u,p).

Coprimality of `f_r` and `g_s` says that `a mod m_T` is nonzero
in the actual field `K'`; hence `a` is an actual unit in `T`.
With `ell=s-r`, the unsaturated divided ideal is exactly

    (p,u^ell*a)=(p,u^ell).

Because `(u,p)` is a regular system of parameters of `T`, the
uncompleted local ring `T/(p)` is a DVR with uniformizer `u`.
The successive quotients of its `u`-adic filtration through
`u^ell` are the field `K'`. It follows that

    length_T T/(p,u^ell)=ell.

This is length over the actual root prime, whose residue field is
`K'`. It is not a count of geometric roots. No separable extension,
fiber derivative, or compatible coefficient-field embedding is
needed. The owner's explicit refusal to assert a `K`-compatible
isomorphism with `K'[[u]]/(u^ell)` is necessary: an inseparable
root deformation need not admit that extra structure.

## 4. Scope of this review and the retained support boundary

The new generic calculation is valid in every characteristic.
Its root-prime length step needs only reducedness of the generic
root divisor. The separate extension to every closed point uses
the literal smoothness of the whole actual root divisor and its
full differential on the exceptional surface, as stated by the
owner. The calculation above supplies its generic exponent
without an additional separability hypothesis.

The generic generator change does not prove absence of vertical
components by itself. That conclusion continues to use the
original global hypotheses: the actual degree-`r` relation is a
line subbundle, and the actual leading coefficient pair has no
common zero. The restrictions of the original strict equations
are then `a f_r,b f_r`; their common zero scheme on `E` is the
actual root divisor. No defective point or vertical exceptional
fiber is discarded in passing to the generic local calculation.

There is no new gap in Sections 2--3 under the stated hypotheses.
This review does not promote the independent global scope audit
or a new canonical acceptance record on its own.
