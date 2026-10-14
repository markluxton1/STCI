# Every Cartier rational singleton lift lies on a minimal-degree normalization

Date: 2026-10-14. Owner: `global_structure`. Status: **NEW WRITTEN
THEOREM; independent review requested**. This extends the already
reviewed [smooth-normalization theorem](2026-10-13-generalization-global-carrier-framework.md)
by a new proof of the extra singular-normalization scope. It does not
rerun or recheck the earlier theorem.

## 1. Exact theorem

Work over an algebraically closed field of characteristic zero. Let
`C subset P3` be a smooth rational curve of degree `d`, and let
`X subset P3` be an integral degree-`a` hypersurface with a mate for
`C`. Let `nu:S->X` be its finite normalization, `H=nu*O_X(1)`.
Assume the full reduced inverse image is one curve `c`, that
`nu|c:c->C` is an isomorphism, and that **c is Cartier on S**.

Then the complete system `|c|` identifies `S` with a normal surface
of minimal degree. With `n=c^2=d^2/a`, the possibilities are:

| Pair `(S,c)` | Integral hyperplane pullback | Carrier degree |
|---|---|---|
| `P2`, a line | `H=d h` | `a=d^2` |
| `P2`, a smooth conic; `d` even | `H=(d/2)h` | `a=d^2/4` |
| Smooth rational normal scroll of degree `n>=2`, hyperplane section; `n|d` | `H=(d/n)c` | `a=d^2/n` |
| Rational-normal cone of degree `n>=2`, smooth Cartier hyperplane section; `n|d` | `H=(d/n)c` | `a=d^2/n` |

The conclusion is about the normalization and its polarization. It
does not assert that every four-coordinate projection of these models
has a mate. Full support and entire conductor descent remain required.

## 2. Why Cartierness gives enough smoothness

At a point `P in c`, take a local defining nonzerodivisor `f` in the
normal surface ring `R=O_S,P`. The quotient `R/(f)=O_c,P` is regular
of dimension one because `c` is smooth. A generator of its maximal
ideal, lifted to `R`, together with `f` generates the maximal ideal
of `R` by Nakayama. Thus `embdim(R)<=2=dim(R)`, and `R` is regular.
Consequently `S` is smooth along all of `c`; its finitely many possible
singularities lie away from `c`.

The mate gives `m c~bH` with `md=ab`. Since `c` is Cartier,
`O(c)` is ample: a positive power is the ample `O(bH)`. Its square
is the positive integer `n=d^2/a`.

Resolve the isolated singularities by `sigma:M->S`, an isomorphism
near `c`. The strict transform `c_M` equals the Cartier pullback,
is smooth rational, and has square `n`. The pullback `L=sigma*H`
is nef and big, and `m c_M~bL`. Adjunction gives

    K_M.c_M=-n-2,    K_M.L=(m/b)(-n-2)<0.

Hence no positive multiple of `K_M` can be effective. The same
characteristic-zero surface-classification input as in the accepted
carrier work makes `M` rational or birationally ruled over a
positive-genus curve. In the latter case the ruling extends to `M`,
and the rational `c_M` is a fiber component, so has square at most
zero. This contradicts `n>0`. Thus `M` is rational.

Normality gives `sigma*O_M=O_S`. The Leray edge map injects
`H1(S,O_S)` into `H1(M,O_M)=0`, so `H1(S,O_S)=0`. No rational-
singularity hypothesis was assumed here; the eventual minimal-degree
classification will impose the actual singularity type.

## 3. The complete linear system and cone polarization

The sequence

    0 -> O_S -> O_S(c) -> O_P1(n) -> 0

gives `h0(O_S(c))=n+2` and surjective restriction. The canonical
section generates away from `c`, and restriction generates on `c`.
Therefore `|c|` is basepointfree. Since `c` is ample, its morphism
to `P^(n+1)` is finite. The nondegenerate image `Y` has

    n=deg(phi) deg(Y),    deg(Y)>=n.

Thus it is a finite birational map to a minimal-degree surface.
The [Del Pezzo--Bertini classification](https://arxiv.org/html/math/0404517v5)
gives normal `Y`, so finite birationality makes `S~Y`. The new
singular possibility is the cone over a rational normal curve; the
plane and Veronese surface remain smooth.

The smooth entries have the integral polarization already derived in
the earlier theorem. For a cone of degree `n`, its minimal resolution
is `F_n`, with exceptional section `E^2=-n` and ruling `f`. The
pullback of the Cartier hyperplane is

    L_c=E+n f.

Pullback injects `Pic(S)` into `Pic(F_n)`: pushing a trivial pulled-
back line bundle down and using `sigma*O_M=O_S` proves injectivity.
Any pulled-back Cartier line bundle has zero degree on the contracted
`E`, so its class `xE+yf` satisfies `y=nx`. It is therefore an
integer multiple of `L_c`. Since `c` itself is Cartier, this proves
`Pic(S)=Z[c]` and `H=(d/n)c` with `n|d`.

For `n=1` the cone is simply `P2` and belongs to the plane entry.
No additional singular minimal-degree surface is missing in dimension
two. The theorem is now proved with every displayed hypothesis retained.

## 4. Fixed C0 and a new non-Cartier boundary

For the literal degree-four `C0`, the accepted all-quartic theorem
removes the `a=4` entries. Every remaining carrier under the theorem's
support and degree-one assumptions has one of exactly three pairs:

    a=8,  S=P1 x P1, c=(1,1), H=(2,2);
    a=8,  S=quadric cone, c=Cartier conic, H=2c;
    a=16, S=P2, c=line, H=4h.

This classifies the entire **Cartier-lift lane**, including singular
normalizations and unibranch thick carriers satisfying the explicit
support assumptions. All have a primitive degree-one normalized
section `Q`, with divisor `2c` or `4c`; all normalized mates are
scalar powers of it.

In particular, every generically regular carrier of fixed C0 whose
degree is neither 8 nor 16 must have a non-Cartier point of its lift
on the normalization if it admits a mate. This is stronger than the
smooth-normalization statement and applies to all carrier degrees.
It does not classify the non-Cartier singularities or bound their
indices. For fixed C0 the index condition remains
`a divides 16 t` for any Cartier multiple `tc`.

Normal hypersurface carriers are even more restricted in this lane.
If `X=S` were a normal carrier satisfying the theorem, its minimal-
degree normalization would have `H^1(O_X)=0` and `p_g(X)=0`, whereas
a degree-8 or degree-16 hypersurface has
`p_g=(a-1)(a-2)(a-3)/6>0`. Equivalently, its canonical class
`(a-4)H` has positive degree on `c`, contradicting the smooth-locus
adjunction value `-n-2`. Thus a normal carrier of fixed C0 with a
mate cannot have Cartier lift at any degree; its lift must meet a
genuine non-Cartier singularity. This is conditional on the fixed-C0
premises and the actual mate, not an all-normal-carrier exclusion.

The missing global possibilities remain non-Cartier lifts, several
inverse-image primes, or finite inverse curves of degree greater than
one. The three projection targets still require full conductor descent.
