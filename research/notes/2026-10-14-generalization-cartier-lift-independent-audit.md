# Independent audit: Cartier rational lifts on normalizations of arbitrary degree

Date: 2026-10-14, America/New_York. Auditor: `frontier_reconcile`.
Status: **PASS FOR THE NEW SINGULAR-NORMALIZATION EXTENSION UNDER ITS
EXPLICIT CARTIER, SINGLETON AND DEGREE-ONE LIFT HYPOTHESES**.

Source audited:
[Cartier-lift minimal-degree theorem](2026-10-14-generalization-cartier-lift-minimal-degree.md),
SHA-256 `0a120c0caf2847b38c749fd47adddc0896a864c1b44e1646225889b34f7055ba`.
The [smooth-normalization theorem](2026-10-13-generalization-smooth-normalization-independent-audit.md)
is an accepted premise and was not rechecked. This audit concerns only the
new singular scope, cone polarization and added consequences. No inherited
verifier, mathematical source or remote branch was reread to reconfirm it.

## 1. Exact theorem and new scope

Over an algebraically closed field of characteristic zero, let a smooth
rational curve C of degree d have an actual mate on an integral degree-a
hypersurface X. Let `nu:S->X` be its finite normalization and
`H=nu*O_X(1)`. Assume the full reduced inverse image is a single smooth
curve c mapping isomorphically to C and **c is Cartier on S**.

Then the complete system |c| identifies S with a normal minimal-degree
surface. In addition to the accepted smooth entries, the only new entry is
a rational-normal cone of degree

    n=c^2=d^2/a>=2,
    H=(d/n)c,
    n divides d.

For fixed C0, the accepted all-quartic theorem leaves exactly three
normalization/polarization targets:

    a=8:  P1xP1, c=(1,1), H=(2,2);
    a=8:  quadric cone, c a smooth Cartier conic, H=2c;
    a=16: P2, c a line, H=4h.

The new target is the quadric cone. Actual projections and complete
conductor descent remain conditions, so none of these entries asserts an
existing mate. Non-Cartier lifts and multiple or nonisomorphic inverse
curves remain outside the theorem.

## 2. Independent review of the extra singular argument

At a closed point of c, let R be the normal surface local ring and f a
local Cartier equation. Since `R/(f)` is the regular one-dimensional
local ring of c, a lift t of its parameter together with f generates
the maximal ideal of R. Thus its embedding dimension is at most two,
equal to its dimension. R is regular. At the generic point normality
already gives a DVR. Therefore S is regular along all of c; over the
algebraically closed characteristic-zero field it is smooth there.
Its possible singularities are isolated and disjoint from c.

The actual mate divisor gives `m c~bH`, `md=ab`. This makes O_S(c)
ample directly: a positive power is the ample O_S(bH). In particular
`n=c^2=d^2/a` is a positive integer. Cartierness supplies the integral
self-intersection even though S may have singularities elsewhere.

Choose a resolution `sigma:M->S` that is an isomorphism near c. No
exceptional component occurs in the pullback of c, because the resolution
centers lie away from its support. Consequently

    c_M=sigma*c,
    c_M^2=n,
    m c_M~b L, where L=sigma*H is nef and big.

Adjunction takes place in the unchanged smooth neighborhood of c_M and
gives `K_M.c_M=-n-2`. Hence

    K_M.L=(m/b)(-n-2)<0.

An effective canonical multiple has nonnegative intersection with the
nef L, so none exists. The already used characteristic-zero surface
classification makes M rational or birationally ruled over a
positive-genus curve. The latter ruling extends after the point
contractions to its minimal ruled model. Its restriction to the rational
c_M is constant, so c_M is a fiber component. Intersecting that effective
fiber with c_M gives

    0=m0*c_M^2+sum mi*(Di.c_M),

with m0>0 and every remaining intersection nonnegative. This contradicts
n>0. Therefore M is rational. Notice that c_M need not be ample on M;
positive self-intersection is enough for this ruling contradiction, and
nefness of L is enough for the canonical argument.

Normality gives `sigma_*O_M=O_S`. The degree-one Leray edge sequence has
an injection

    H1(S,O_S) -> H1(M,O_M)=0.

Thus `H1(S,O_S)=0`. This step requires no vanishing of
`R1 sigma_*O_M` and no prior rational-singularity hypothesis. In
particular the proof has not smuggled such a hypothesis into the new
singular scope.

The accepted complete-system argument now applies using the actual
Cartier sequence

    0 -> O_S -> O_S(c) -> O_c(c)=O_P1(n) -> 0.

Its proof uses ampleness, this restriction surjectivity and the degree
bound, rather than smoothness away from c. It gives a finite birational
map to an integral normal minimal-degree surface. A finite birational
map to a normal target is an isomorphism. The surface classification
therefore supplies the plane, Veronese, smooth scroll or rational-normal
cone; in dimension two there is no additional singular family.

## 3. Cone Picard computation and integral polarization

For the degree-n rational-normal cone with n>=2, its minimal resolution
is F_n. Write its exceptional negative section E and fiber f, with

    E^2=-n, E.f=1, f^2=0.

The hyperplane pullback is `L_c=E+n f`. This is the usual cone
polarization: it has degree zero on the contracted E, degree one on
each ruling f and square n. The smooth Cartier hyperplane c avoids
the vertex, consistently with regularity along c established above.

Pullback on line bundles is injective. Indeed, if a line bundle A
pulls back trivially, the projection formula and
`sigma_*O_M=O_S` give

    A=sigma_*sigma*A=sigma_*O_M=O_S.

Every pulled-back Cartier line bundle has degree zero on the contracted
E. In the free Picard group `Pic(F_n)=ZE+Zf`, a class xE+yf
therefore satisfies

    -n x+y=0,

so it is an integer multiple of L_c. Since c itself pulls back to
L_c, injectivity implies `Pic(S)=Z[c]`, with no unnoticed fractional
or torsion generator. Thus the ample H is an integer multiple q c,
and

    d=H.c=q n,
    q=d/n,
    n divides d,
    a=H^2=d^2/n.

This proves the only extra integrality constraint needed by the singular
extension. For n=1 the cone is P2 and already belongs to the line entry.

For d=4, the new cone degrees are n=2 and n=4. The latter would have
a=4 and is removed by the accepted theorem. The former has a=8 and
is the quadric cone with H=2c. Together with the two accepted smooth
higher targets this gives the complete three-entry list.

## 4. Additional degree-free corollary: downstairs Cartier rational curves

The source's normal-carrier consequence is correct. In fact its scope
can be strengthened without using the characteristic-zero classification.

**Corollary, every characteristic.** Let C be a smooth integral curve of
degree d and genus g over an algebraically closed field. Suppose an
integral degree-a hypersurface X contains C as a Cartier curve and has
an actual mate for C. Then X is normal and

    a divides d^2,
    2g-2=d^2/a+(a-4)d.                         (G)

Consequently a is a positive divisor of d^2 and satisfies the strict
bound `a<4+(2g-2)/d`, independent of the mate degree. For rational C,
the only numerical possibilities are

    X a plane, C a line or smooth conic;
    X a quadric, C a smooth Cartier conic.

In particular every smooth rational curve of degree d>=3 is non-Cartier
on every integral carrier on which it has a mate. This statement is about
Cartierness on X itself; it does not exclude the three nonnormal
Cartier-normalization-lift targets above.

Proof of normality. The same quotient-regular local argument makes X
regular along the smooth Cartier C. The mate's Cartier zero divisor D
has reduced support C. In the regular neighborhood of C it is `m C`
for one positive integer m; away from C both Cartier divisors are zero.
Thus `m C~b O_X(1)` globally, and C is ample. Every codimension-one
nonregular component would be a projective curve disjoint from C.
Its restriction of O_X(C) would be trivial, since the canonical section
has no zero there; ampleness would require strictly positive degree.
This is impossible. Thus X satisfies R1. A hypersurface is Cohen--Macaulay,
hence S2, so Serre's criterion makes X normal. This argument permits
possible isolated singularities away from C.

Now `n=C^2=d^2/a>0` is an integer, proving `a divides d^2`.
Cartier adjunction in the smooth neighborhood of C, together with
`omega_X=O_X(a-4)`, gives equation (G). The strict bound follows by
dividing it by d and retaining the positive summand d/a.
For rational C, this becomes

    (a-4)d=-n-2=-d^2/a-2.                     (A)

Thus a>=4 is impossible. For the three remaining positive carrier
degrees, equation (A) gives respectively

    a=1: (d-1)(d-2)=0;
    a=2: (d-2)^2=0;
    a=3: d^2-3d+6=0.

The last polynomial has negative discriminant, so has no real, hence
no positive integer, root. This proves the numerical list. These are
ordinary integer intersection calculations in every characteristic,
not equations reduced modulo the field characteristic. No Frobenius
or surface-resolution input is used.

For fixed C0, the corollary directly forces a genuine non-Cartier
singularity on every normal mate-admitting carrier, in every degree.
This conclusion does not require repeating the inherited all-quartic
proof. A nonnormal carrier may still have a Cartier lift upstairs while
C is non-Cartier downstairs; complete conductor descent remains the
obstruction in that case.

## 5. Review boundaries and continuation

The extension changes the support lane from smooth S to normal S with
Cartier c. It does not classify the non-Cartier singularities, bound their
Cartier indices, or force every presentation to have a degree-one
singleton lift. A finite inverse curve of degree greater than one, or
several inverse-image primes, requires its actual coefficient-vector
divisor relation.

The three fixed-C0 normalization targets have a primitive normalized
degree-one section Q with divisor 2c or 4c. The source's assertion that
normalized mates are scalar powers follows from the exact polarization
and the fact that two nonzero projective sections with the same divisor
differ by a global unit, hence a scalar. Whether any such power descends
through the full conductor is a separate question. This audit establishes
neither single-field residue bounds nor a uniform bound on split phase
orders for their actual four-coordinate projections.

No mathematical verifier was executed. The review consists of the new
local regularity, resolution/Leray and cone Picard arguments and the
displayed additional adjunction proof. The previously accepted smooth
proof and all-quartic result retain their original provenance. Neither a
universal STCI theorem nor an unrestricted counterexample is claimed.
