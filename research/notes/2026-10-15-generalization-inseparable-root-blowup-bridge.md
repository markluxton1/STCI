# The actual-CI blowup bridge does not require separable root fields

Date: 2026-10-15. Author: `formal_algebraization_route`.
Status: **ARBITRARY-CHARACTERISTIC BRIDGE; independent review passed** in
the [full new-scope audit](2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit.md),
with a separate [generic local-algebra review](2026-10-15-generalization-inseparable-root-blowup-local-algebra-review.md).
The accepted characteristic-zero bridge is a premise. This note proves
the new extension to arbitrary characteristic by replacing its single
root-splitting step with uncompleted local algebra over `K=k(C)`.
No accepted certificate, computation, or characteristic-zero proof was
replayed.

## 1. Literal hypotheses and conclusion

Let `k` be an algebraically closed field of any characteristic, `X` a
smooth threefold, and `C subset X` a smooth connected curve. Let the
actual complete intersection `Y=(F,G)` have reduced support exactly `C`.
Retain the literal hypotheses of the
[accepted actual-CI/root bridge](2026-10-14-generalization-blowup-root-curve-primitive-bridge.md):

1. The first ordinary normal relation has degree `r`, and its actual
   relation sheaf is a saturated line subbundle of `Sym^r N_C^*`.
2. Both chosen actual equations have generic normal order `r`. Their
   degree-`r` symbols jointly generate that line at every point of `C`.
   Their two coefficient sections have no common zero.
3. The **entire** generic ordinary initial ideal is the binary complete
   intersection `(f_r,g_s)`, with `s>r` and the two forms coprime. Put
   `ell=s-r` and assume `ell>=2`.
4. On `B=Bl_C X`, the actual Cartier root divisor `Z=(f_r)` in the
   exceptional divisor `E` is smooth. Smoothness of the reduced support
   of a nonreduced root is insufficient.

Then the actual strict intersection `Y'=D_F intersect D_G` has support
exactly `Z`, no vertical exceptional-fiber component, and the exact
uncompleted local form

    I_(Y',p)=(h,u^ell)                                  (1)

at every point `p in Z`, with `S=(h)` a smooth surface and `u` an
exceptional equation cutting out `Z` as a reduced Cartier divisor on
`S`. Consequently `Y'` is an embedded primitive `ell`-fold structure
on the full smooth `Z`, with surviving conormal `O_Z(-E)`.

The conormal extension for `Z subset E subset B` splits. The actual
first obstruction therefore vanishes. Moreover `Y'` gives a compatible
embedded Cartier lift of `Z` on `V(I_E^ell)` and hence at every stage

    E_m=V(I_E^(m+1)),       m<ell.                      (2)

No separability of `Z->C`, tame ramification, or invertibility of `r`,
`s`, or `ell` in the field is assumed.

## 2. The generic standard basis exists before completion

Set `A=O_(X,eta_C)`, a two-dimensional regular local ring, with maximal
ideal `m=I_C A` and residue field `K=k(C)`. Its associated graded ring
is `K[x,y]`. Put `I=(F,G)A`. It is an `m`-primary complete intersection.

Choose one original generator `P` whose degree-`r` symbol is nonzero;
multiply it by a unit of `A` if necessary, so that its symbol is `f_r`.
Choose `H in I` with initial form `g_s`. Such a lift exists by the
definition of the degree-`s` part of the full initial ideal. Put
`J=(P,H)`. Then

    J subset I,
    (f_r,g_s) subset in_m(J) subset in_m(I)=(f_r,g_s).

Thus the two initial ideals agree. Successive order reduction says that
every element of `I` lies in `J+m^n` for every `n`. Krull intersection
in the finite module `A/J` gives

    I=(P,H)                                              (3)

in the actual local ring `A`. Equivalently, the homogeneous regular
sequence gives the same finite colength for the two ideals. No
completion, coefficient field, geometric root splitting, or division by
the characteristic is used.

Both generating pairs `(F,G)` and `(P,H)` minimally generate the
height-two complete intersection `I`. Their coefficient change matrix
is therefore in `GL_2(A)`; this follows by reducing its generating map
modulo `m` and applying Nakayama.

On the ordinary blowup of `Spec A` at `m`, divide **both** members of
either pair by `u^r`. The invertible change matrix remains invertible,
so it preserves the actual ideal of the strict intersection:

    (F/u^r,G/u^r)=(P/u^r,H/u^r).                        (4)

The second entry on the right is `u^(s-r)*(H/u^s)`. Replacing that entry
by `H/u^s` would instead saturate away the multiplicity and is not
permitted. The proof uses (4), with the common exponent `r`, throughout.
The object is the intersection of the two original strict divisors,
not the strict transform of the supported intersection `Y`. Saturating
the eventual ideal `(p,u^ell)` by `u` would give the unit ideal and
destroy this object entirely; no such saturation is performed.

## 3. The generic root prime may be inseparable

Let `xi` be the generic point of a component of `Z`. Every component is
horizontal over `C`: a line subbundle gives a nonzero binary polynomial
on every exceptional fiber, so `Z->C` is finite of degree `r`.

Choose a blowup chart `x=u`, `y=uv` containing `xi`, and let

    T=O_(Bl_m Spec A,xi).

It is a regular local ring of dimension two, and

    T/(u)=K[v]_(q),
    K'=k(xi)=K[v]/(q),                                  (5)

where `q` is the irreducible polynomial of that generic root. The
actual smooth root divisor is reduced; consequently its generic fiber
is reduced and `q` occurs to exponent exactly one in `f_r(1,v)` as a
polynomial over `K`. It may have zero derivative and become a repeated
root after an inseparable extension. Neither circumstance changes
the exponent of its prime factor over `K` in (5).

Put `p=P/u^r` and `a=H/u^s`. Modulo `u`,

    p=f_r(1,v)=unit*q in K[v]_(q),
    a=g_s(1,v).

Coprimality makes the latter nonzero modulo `q`. Thus `a` is a full
unit in `T`, while `(u,p)` is its maximal ideal. Formula (4) becomes

    I_(Y',xi)=(p,u^ell) in T.                           (6)

The ring `T/(p)` is an uncompleted DVR with uniformizer `u`, so

    length_T T/(p,u^ell)=ell.                           (7)

This proves the generic transverse multiplicity on every component of
`Z` over its actual root field. It does not replace `K'` by an
algebraic closure, use `q'`, or count distinct geometric roots.

In particular no `K`-compatible identification with
`K'[[u]]/(u^ell)` is asserted. For inseparable residue extensions a
deformed root equation need not admit such a compatible coefficient
field. The exact local ideal (6) and length (7) are the needed facts.

A single family illustrates this distinction without a root-case
enumeration. In characteristic `p>0`, take `C=(x,y)` in affine
`(t,x,y)`-space and

    F=y^p-t*x^p+x^(p+1),
    G=F+x^(p+ell),       ell>=2.

Its full generic initial ideal has the coprime generators
`y^p-t*x^p,x^(p+ell)`, with `r=p` and `s=p+ell`. On the `x=u,y=uv`
chart the actual strict ideal is

    (v^p-t+u,u^ell).

The root `v^p=t` is a smooth total-space divisor, purely inseparable
over the `t`-line, and the displayed ideal is exactly the claimed
primitive `ell`-fold. In the containing DVR the relation is
`t=v^p+u`. A `K`-compatible coefficient field containing a root of
`a^p=t` would require `(a-v)^p=u`, impossible because its `u`-valuation
would be `1/p`. The same obstruction survives modulo `u^ell`: the
linear `u` term cannot be canceled by a `p`-th power of an element in
`(u)`. Thus the stronger split `K`-algebra claim genuinely fails even
though the local ideal and transverse length theorem hold.

## 4. Actual support and every closed point are retained

The characteristic-free support argument uses the original strict
equations. Their restrictions to `E` are `a f_r,b f_r`, and the actual
coefficient pair `a,b` has no common zero. Their common zero set on
`E` is exactly `Z`. Off `E`, the blowup is an isomorphism and the
original pair has no common point off `C`. Hence

    Supp(Y')=Z.

No entire exceptional fiber is a component. In particular no vertical
component has been removed by saturation. Neither strict divisor
contains `E`; a shared surface component off `E` would contradict
the original complete intersection. Thus their height-two intersection
in the smooth threefold is Cohen--Macaulay and has no discarded embedded
or isolated component.

Fix a closed point `z in Z`. One original strict equation `h` has a
leading coefficient which is a unit there. Its restriction to `E`
cuts out the actual smooth divisor `Z`. The **full** differential on
`E`, including base directions, is nonzero. Therefore `(h,u)` cuts
out the smooth curve `Z` in the smooth threefold: `S=(h)` is smooth
at `z`, transverse to `E`, and `u` cuts out `Z` as a reduced Cartier
divisor on `S`.

Restrict the other strict equation `h_2` to the regular local surface
ring `O_(S,z)`. It is nonzero, and its zero set is precisely `(u)`.
This ring is a UFD and `(u)` is prime, so

    h_2|S=epsilon*u^b,       epsilon a unit.

Its order at the generic point of this component is (7), hence `b=ell`.
Lifting the unit gives exactly (1), before completion. This also covers
smooth points at which the root projection is purely inseparable.
For example `v^p-t` has vanishing fiber derivative but nonzero full
differential `-dt`; the latter is what this proof uses.

## 5. Conormal splitting and compatible actual lifts

Locally (1) with `ell>=2` shows that the first normal symbols of the
two equations span precisely the conormal line generated by `h`.
Its projection to `O_Z(-Z_E)` is an isomorphism, since `h|E` generates
the ideal of `Z` in `E`. These local image lines are the image of the
global two-equation symbol map and therefore glue. They split

    0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0.

The actual quotient line, hence the first ordinary normal layer of
`Y'`, is `O_Z(-E)`; no torsion layer is discarded. The cotangent
extension description of the first embedded root-divisor obstruction
is characteristic free and uses the full differential. Thus the
splitting gives `kappa(df_r)=0` in the actual obstruction group.
This is the geometric class in the chosen characteristic. No
characteristic-zero chart representative involving rational denominators
is transferred to an exceptional characteristic.

Formula (1) also gives `I_E^ell subset I_(Y')`. On `V(I_E^ell)`, the
quotient ideal is generated by `h`, which is a nonzerodivisor since
`(h,u)` is a regular sequence. It is therefore an actual invertible
embedded ideal extending `I_(Z/E)`. This proves (2), with all equation
units and all points retained.

## 6. Consequence for the characteristic-free smooth-root cutoff

The [characteristic-scope addendum](2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md)
already proves the formal smooth movement-two nonexistence theorem
and its finite empty smooth-root stage in every characteristic under
the explicit normal-bundle hypothesis. The present new proof supplies
the missing actual-CI bridge in that characteristic as well, under
the literal hypotheses in Section 1.

For a fixed balanced smooth rational embedding of degree `e>=4` and a
fixed first normal order `r`, let its empty smooth-root stage be `K_N`.
The actual gap `ell=s-r` supplies the stage `K_(ell-1)` by (2). Thus

    s-r<=N, equivalently s<=r+N.                        (8)

Equality only supplies stage `N-1` and is not excluded. The cutoff
is existential, depends on the actual embedding and `r`, and excludes
no finite-gap pair merely because it is finite. No normal-bundle
splitting in an exceptional characteristic is inferred for `C0`.

The proof does not cover a nonreduced actual root, first-relation
defects, joint leading base points, a noncoprime next initial relation,
or the absence of the full ordinary initial complete-intersection
hypothesis. Those are substantive retained boundaries. The universal
STCI and unrestricted `C0` problems remain open.
