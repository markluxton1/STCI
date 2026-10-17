# Independent audit of the all-degree smooth-normalization classification

Date: 2026-10-14, America/New_York. Auditor: `frontier_reconcile`.
Status: **PASS FOR THE NEW THEOREM UNDER ITS EXPLICIT SINGLETON-LIFT AND
SMOOTH-NORMALIZATION HYPOTHESES**. This audit reviews the new derivation;
accepted quartic, conductor and fixed-C0 premises were not rerun. The theorem
does not imply that an arbitrary minimum carrier has these hypotheses.

Owner source read:
[degree-free carrier framework](2026-10-13-generalization-global-carrier-framework.md),
SHA-256 `38bff3c497b1c0f8310a623e36c0fd5d6ded0517fc6903115b4321f5672d5848`.
The acceptance here is for section 3 and the finite fixed-C0 classification
in section 4. The later power-compression consequences have their separate
new-theorem dependency and are not promoted by this audit.

## 1. The exact accepted theorem

Let `C subset P3` be a smooth rational curve of degree `d` over an
algebraically closed field of characteristic zero. Let `X` be an integral
degree-`a` hypersurface admitting an actual mate for C, with finite
normalization `nu:S->X`. Require:

    S smooth,
    (nu^-1(C))_red=c,
    nu|c:c->C an isomorphism.

Put `H=nu*O_X(1)`. Then `(S,c)` is a smooth surface of minimal degree
with c its complete hyperplane class. The possibilities are exactly:

| Surface and c | H | a |
|---|---|---|
| P2 and a line | `d h` | `d^2` |
| P2 and a smooth conic | `(d/2) h`, requiring d even | `d^2/4` |
| Smooth rational normal scroll of degree n>=2 | `(d/n)c`, requiring n to divide d | `d^2/n` |

The scroll can be written `F_e`, `c=E+t f`, with `E^2=-e`,
`t>e>=0` and `n=2t-e`. These are finitely many normalization/polarization
types for a fixed d. The conclusion is necessary; it neither constructs
the four-coordinate projection nor proves support or conductor descent.

## 2. Independent reconstruction of the proof

The pullback of a degree-b mate is a nonzero section of `O_S(bH)`.
Its complete zero support is c by the stated singleton inverse-image
condition. On the smooth surface its actual divisor is `m c` for a
positive integer m. Since H.c=d and H^2=a, intersecting yields

    m d=a b,
    c_num=(d/a)H,
    n=c^2=d^2/a.

There is no hypothesis that the downstairs C is Cartier on X. Smoothness
of S makes c Cartier upstairs, so n is an integer. It is positive and
c is ample by numerical equivalence with the positive multiple of ample
H. This is the first place the smooth-normalization hypothesis is essential.

Adjunction on the smooth rational c gives `K_S.c=-n-2`. Thus `K_S.H<0`.
An effective positive canonical multiple would have nonnegative
intersection with ample H, so no such multiple is effective. The standard
characteristic-zero surface classification used in the accepted repository
arguments therefore makes S rational or birationally ruled over a
positive-genus curve.

The second alternative is impossible. A smooth ruled minimal model over
the positive-genus base is reached by point contractions, and the ruling
pulls back to a morphism on S. The rational c maps constantly to the base.
Write the fiber containing it as `F=m0*c+sum mi*Di`. Then

    0=F.c=m0*c^2+sum mi*(Di.c).

Every other component has nonnegative intersection with c on the smooth
surface, and m0 is positive. This contradicts c^2>0, including a reducible
or nonreduced fiber. Hence S is rational and `H1(S,O_S)=0`.

Now use the actual Cartier-curve sequence

    0 -> O_S -> O_S(c) -> O_c(c)=O_P1(n) -> 0.

It yields `h0(O_S(c))=n+2` and surjectivity onto all n+1 sections on c.
The canonical section of O_S(c) is nonzero at each point outside c.
At each point of c, some lifted section is nonzero because O_P1(n)
is globally generated. Consequently the complete system |c| is basepoint
free everywhere, not only generically.

Its morphism `phi:S->P^(n+1)` is finite: a positive-dimensional fiber
would contain a curve D with `c.D=0`, contradicting ampleness. The image
Y is an integral nondegenerate surface. Nondegeneracy follows from using
a basis of the complete linear system. If e is the generic map degree,
the intersection-degree formula and the minimal-degree inequality give

    n=c^2=e*deg(Y),
    deg(Y)>=codim(Y)+1=(n+1-2)+1=n.

Thus e=1 and deg(Y)=n. This includes n=1: then the map is finite
birational onto P2; no scroll-only assumption loses that case.

The degree inequality and Del Pezzo--Bertini classification were inspected
in the primary author source [Eisenbud--Green--Hulek--Popescu, *Small Schemes
and Varieties of Minimal Degree*, introduction](https://arxiv.org/html/math/0404517v5).
For integral surfaces, its list is a plane, an integral quadric/rational
normal scroll, or a Veronese surface. These standard surfaces are normal,
including the singular rational normal cones. Therefore the finite
birational map to Y is an isomorphism: on affine opens, the finite integral
algebra inside the common function field equals the integrally closed
target ring. Smoothness of S eliminates singular cones. The complete
polarized classification follows.

On each resulting rational surface numerical equivalence and linear
equivalence agree. For `P2`, c is h or 2h, so H is respectively d h or
(d/2)h; the latter requires d even. On a scroll `Pic(F_e)=ZE+Zf` and
c has E coefficient one. Therefore the rational equality
`H=(d/n)c` forces `d/n` to be an integer. Squaring gives the carrier
degrees in the table. The necessary divisibility n|d gives a uniform
finite list of smooth normalization types at once, rather than a separate
degree-pair search.

## 3. Every fixed-C0 case in the finite list

For d=4, the line model gives a=16. The conic model gives a=4. Smooth
scroll degree n must divide four and satisfy n>=2, so n=2 or n=4:

* n=2 gives a=8. In `n=2t-e` with `t>e>=0`, the only possibility is
  `e=0,t=1`, hence `S=P1xP1`, `c=(1,1)`, `H=(2,2)`.
* n=4 gives a=4. The scroll models are `e=0,t=2` or `e=2,t=3`;
  together with the plane conic, these fall in the already accepted
  all-integral-quartic exclusion. No new check of that theorem is needed.

Thus the only remaining smooth-normalization singleton-lift candidates
for the literal fixed C0 are

    a=8:  (S,c,H)=(P1xP1,(1,1),(2,2)),
    a=16: (S,c,H)=(P2,line,4h).

Their sectional genera are one and three, obtained directly by adjunction
on H. Their complete H systems have dimensions nine and fifteen.
Those dimensions describe parameter spaces for projections, not an
exhaustion of projection centers. Actual finite birational projection,
the prescribed deleted-middle-monomial restriction to c, full inverse
support and every conductor layer remain active conditions.

## 4. Scope audit and retained limitations

The proof needs neither generic regularity of X along C nor a smooth
mate once the full singleton isomorphic lift is explicitly assumed.
Conversely, the theorem does not provide that lift for a general
generically nonregular carrier. Several primes above C and degree-greater-
than-one lifts have a coefficient-vector divisor relation and are outside
this scalar argument.

A singular normalization cannot simply be substituted into the audited
proof. There c may not be Cartier, its self-intersection may be rational,
and the Cartier-curve exact sequence can fail. A proposed extension to
normal S with smooth Cartier c would be a new theorem requiring its own
precise statement, cone/Picard analysis and review. It is not implicitly
accepted here.

The global existence of high-degree smooth surfaces through C does not
yield mates on those surfaces. Nor does choosing a minimum mate-admitting
carrier force smooth normalization. Entirely thick pairs can remain
singular under `G+F*T`. The remaining normalization and filtered-algebra
branches cannot be discarded by this result.

For the two fixed-C0 models, `H=2c` or `H=4c` supplies a primitive
normalized degree-one section, but an upstairs section is still not an
ambient mate. The separate conductor-power theorem may compress it
under its single-field/unit hypotheses. This audit accepts neither a
geometric residue-degree bound for every projection nor the exclusion of
split conductor phases. No unconditional degree-eight or degree-sixteen
carrier exclusion follows.

## 5. Optional proof simplification, not needed for acceptance

One can obtain `H1(O_S)=0` before surface classification. Every morphism
from the rational c to an abelian variety is constant. If the Albanese
morphism of S had positive-dimensional image, pulling back a suitable
ample divisor on that image would give a nonzero effective divisor D
with `c.D=0`, since c is contracted. Ampleness of c contradicts this.
Thus the Albanese variety is trivial; in characteristic zero this gives
`H1(O_S)=0`. The complete-|c| proof then establishes rationality from
the minimal-degree classification itself.

This alternative explains the same geometric rigidity: an ample rational
curve forbids irregularity. It is supplied as an optional simplification;
the audited owner proof already establishes the necessary vanishing by
the standard surface-classification route.

## 6. Evidence and review boundaries

This is a written independent mathematical reconstruction, including
ampleness, reducible fiber signs, n=1 and n=2 cases, finite-map degree,
normality/isomorphism, all Picard divisibilities and the complete fixed-C0
list. There was no symbolic execution and no inherited verifier rerun.
The live primary check was restricted to the new minimal-degree interface.
Parallel agreement is not used as a proof: the argument above supplies the
reviewed implications.

The all-quartic theorem and the normal-bundle/conductor results retain
their earlier audit provenance. No novelty or universal resolution is
claimed. The mathematical advance accepted here is a finite
normalization-type classification for an entire explicitly stated rational
support lane across all carrier and mate degrees.
