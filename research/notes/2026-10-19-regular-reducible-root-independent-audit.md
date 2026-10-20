# Independent audit: a regular formal surface cannot lift the equal split root

Date: 2026-10-19. Reviewer: `regular_reducible_audit`. The local Cartier,
intersection-length, completion-transitivity, and companion-containment
steps were separately checked by `regular_reducible_audit/local_check`.

Status: **PASS for the precise conditional nonexistence statement below.**
This is an independent review note, not a promoted result record. No accepted
mathematics or canonical metadata is changed. In particular, this note does not
apply the smooth-root statement STCI-R-0005 to a singular root.

## 1. Exact statement and inputs

Work over an algebraically closed field of characteristic zero with the fixed
smooth rational quartic `C0`. Let

    B = Bl_C0(P3),  E = P1 x P1,  O_E(E) = O_E(7,-1).

The first factor is the base `C0`. Fix `q >= 1`, and let `D1,D2` be distinct
smooth integral divisors of class `(1,q)` on `E`. Put

    Z = D1 union D2

with its reduced scheme structure. Suppose compatible embedded effective
Cartier lifts on all exceptional neighborhoods produce a Cartier formal
surface `V` in `B-hat_E`, whose reduction modulo the exceptional parameter is
exactly `Z`.

**Claim audited.** Such a lift cannot have `V` regular at every point of at
least one full component `Di`.

The words “at every point” are essential: regularity only at the generic
point of a component is automatic here and does not satisfy this hypothesis.
The assertion permits arbitrary tangency and intersection multiplicities
between `D1` and `D2`.

The accepted blowup conventions and the branch normalization, resolution,
multiplicity, and plane-genus mechanisms are recorded in
[STCI-R-0005](../results/smooth_root_formal_obstruction.md) and its
[independent source audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md),
especially Sections 1--3 and 5--6. They are used within their stated scope;
the accepted smooth-root exclusion itself is not replayed. The new points
checked here are the self-intersection of a component of a reducible root,
the change of completion center, retention of the companion component, and
the resulting numerical contradiction.

The primary algebraicity input is
[Bost, Theorem 3.5 and Corollary 3.8, printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27).
The smooth-center version applies to a smooth connected projective curve
and a smooth formal surface with ample normal line; its algebraic closure
has the same dimension. The lci-center corollary also permits a proper
connected center that is not smooth. These are geometric results over a
field, with no number-field or analytic-convergence hypothesis. The
accepted source audit checks that the printed dimension condition includes
curves; the text extraction of the PDF loses the equality stroke.

## 2. Local algebra and the component normal degree

Write `E=(u)`. At an intersection point `p`, choose equations `a,b` of
`D1,D2` on `E` and lifts to the completed regular local ring of `B`.
After multiplying the equation of `V` by a unit, its equation is

    g = a*b + u*h.

At `p`, both `a,b` vanish, so the linear part of `g` is `h(p)*u`.
Consequently regularity of `V` at `p` forces `h` to be a unit. This argument
does not require that `a,b` be independent parameters: it includes tangent
components and higher intersection multiplicities.

Inside the regular full completed local ring of `V` at `p`,

    u = -a*b/h,
    I_D1 = (u,a) = (a),   I_D2 = (u,b) = (b).

Thus both components are Cartier there and

    length O_V,p/(a,b) = length O_E,p/(a,b).

Away from their intersection, the root is smooth and the differential of
its local equation already has a nonzero component tangent to `E`; hence
`V` is automatically regular there. It follows in particular that
regularity along one full `Di` implies regularity along all of `Z`.

The exceptional parameter is a nonzerodivisor on `V`: locally `g mod u`
is a nonzerodivisor on the smooth integral surface `E`, so `u,g` form a
regular sequence. Its zero divisor on `V` is exactly `D1+D2`. Restricting
the associated divisor identity to `D1` gives

    deg N_(D1/V)
       = deg O_D1(E) - (D1.D2)_V
       = (7q-1) - (D1.D2)_E
       = (7q-1) - 2q
       = 5q-1.                                      (1)

This is a normal line of positive degree for every `q>=1`, hence is ample
on the smooth projective curve `D1`. The same computation holds for `D2`.

## 3. Algebraization and why the other component is retained

Complete `V` along `D1`. The inclusion `D1 subset E subset B` permits
completion in two stages; completing `B-hat_E` further along `D1` gives
`B-hat_D1`. The resulting `V-hat_D1` is a closed smooth formal surface in
`B-hat_D1`, admits `D1` as its scheme of definition, and has normal line
(1). Bost's smooth-center theorem therefore gives an integral algebraic
surface `W subset B` containing this formal branch.

Formal containment along `D1` must not be replaced by an unsupported
claim that `W` has only this branch. Nevertheless it forces the algebraic
companion `D2` to be contained in `W`:

1. Choose any `p in D1 intersect D2`; such a point exists because the
   total intersection number is `2q>0`.
2. Let `w` be a local algebraic equation of `W` in `B` near `p`. It is
   zero on `V-hat_D1` and hence in its full maximal-ideal completion at
   `p`.
3. That full completion is exactly the full completion of the original
   `V` at `p`, by transitivity of completion. It contains the completed
   germ of `D2` as the quotient by `(b)` in Section 2. Thus `w` is zero
   in the completion of `O_D2,p`.
4. The map from the noetherian local domain `O_D2,p` to its completion
   is injective. Therefore `w` already vanishes in `O_D2,p`. This gives
   algebraic containment on a nonempty open subset of `D2`; integrality
   of `D2` and closedness of `W` give `D2 subset W` globally.

The argument uses an actual intersection point, the same full completed
branch at that point, and the algebraic curve `D2`. Mere abstract
isomorphism of formal surfaces would not justify it. Nor would it
justify retaining a second component disjoint from the completion center.
Here it gives scheme-theoretic containment of the reduced curves
`D1+D2` in the effective Cartier divisor `W|E` on the smooth surface `E`.

There is a shorter valid route in this specific setting. Section 2 shows
that `V` is smooth along its entire support `Z`; the center `Z` is proper,
connected, and Cartier in `V`. Its normal line is `O_Z(E)`, of degree
`7q-1>0` on each irreducible component, hence ample on `Z`. Bost's lci-center
Corollary 3.8 then algebraizes the full `V` directly, and reduction modulo
`u` immediately retains both components. The smooth-center route above
also proves the proposed continuation step explicitly.

## 4. Normalization, degree, and Hodge index

The selected formal branch is regular. On the algebraic normalization
of `W` it lifts uniquely and is the completion of a regular neighborhood
of an embedded copy of `D1`. This is the same finite-normalization and
whole-curve gluing mechanism checked in Section 3 of the accepted source
audit, now applied to the smooth center `D1`. Extra algebraic branches
are allowed. Resolve the normalization away from this regular
neighborhood, obtaining a smooth projective surface `T` with

    D1^2 = 5q-1.

Since `u` is nonzero on the selected formal branch, `W` is distinct from
`E`. Its image `S subset P3` is an integral surface and `W` is its strict
transform. Let `H` be the pullback to `T` of a hyperplane and put
`d=deg S`. Then

    H is nef,  H^2=d>0,  H.D1=4q.

Hodge index on `T` gives

    d*(5q-1) <= (4q)^2,
    d <= 16q^2/(5q-1) <= 4q,                         (2)

where the last inequality is equivalent to `q>=1`. No ruled-surface
classification or strict high-self-intersection threshold is needed for
this equal split case.

Let `m` be the generic order of `S` along `C0`. The restriction `W|E`
has degree `m` on a generic exceptional fiber and contains `D1+D2`.
Each component has fiber degree `q`; thus

    m >= 2q.                                         (3)

This lower bound remains valid with every additional algebraic branch,
exceptional intersection component, and multiplicity retained.

## 5. Numerical contradiction

The accepted plane-section argument for an integral degree-`d` surface
of generic multiplicity `m` along the smooth quartic gives

    (d-1)(d-2) >= 4m(m-1)
                >= 4(2q)(2q-1)
                 = 16q^2-8q.                        (4)

It uses a general integral plane section, transverse intersection with
the four points of `C0`, and the arithmetic genus after blowing up those
points. No assumption of ordinary plane singularities or absence of
residual surface branches is present.

For positive integral `d<=4q`,

    (d-1)(d-2) <= (4q-1)(4q-2)
                = 16q^2-12q+2
                < 16q^2-8q,

because the positive difference is `4q-2`. This contradicts (4). The
boundary `q=1` is included: (2) gives `d<=4`, whereas (4) demands at least
`8` on its left side, whose maximum in that range is `6`.

## 6. Outcome, limitations, and frontier impact

The proposed theorem passes the audit after making the following points
explicit: regularity is along a full component, not just generically;
the normal degree is computed in the regular formal surface; completion
along the component retains the same full local branch at its
intersection with the companion; and companion containment is an
algebraic consequence of local vanishing, rather than an assumed
equality `W|E=Z`.

This excludes an all-orders Cartier lift of the specified reduced equal
split root whenever its total formal surface is regular along `Z`.
It does not exclude a lift whose formal surface is singular at one or
more points of `D1 intersect D2`, roots with different component classes,
nonreduced roots, or any actual complete intersection without a separate
bridge to this exact formal-lift setting. In particular it supplies no
unrestricted characteristic-zero STCI conclusion.

Authority status remains **reviewed proposal/evidence, not promoted**.
No new computation is needed for the argument, and no finite checks or
load-only CAS tests are offered as a substitute for the geometric proof.
