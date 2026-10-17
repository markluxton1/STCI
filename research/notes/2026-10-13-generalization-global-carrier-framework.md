# Degree-free carrier framework and the smooth-normalization classification

Date: 2026-10-13 evening, continued 2026-10-14. Owner:
`global_structure`. Status: **NEW WRITTEN PROOFS; independent review
requested**. Accepted repository results are premises; no inherited
proof or computation was rerun. This note makes no novelty claim and
does not resolve either unrestricted STCI question.

## 1. Accepted inputs and the reason to change the organization

The controlling inputs are the [all-quartic acceptance](2026-10-11-session-all-quartic-results-acceptance.md),
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
and the current [all-branch inventory](2026-10-13-evening-branch-frontier-audit.md).
The all-quartic theorem excludes every integral quartic carrier of the
literal fixed `C0=[s^4:s^3t:st^3:t^4]` in characteristic zero, with
arbitrary mate degree. It does not force an arbitrary STCI presentation
to have a quartic carrier.

The reusable content of the accepted proofs is stronger than a collection
of degree exclusions. It is the combination of full inverse-image
support, a positive Cartier divisor on a ray in the normalization class
group, and descent through the entire conductor. The recovered thick
notes [normalization/APic bridge](../validation/2026-10-13-evening-branch-inventory/remote-snapshots/research_entirely-thick-rees-valuation/research/notes/2026-10-07-thick-apic-conductor-bridge.md)
and [generic normalization filter](../validation/2026-10-13-evening-branch-inventory/remote-snapshots/research_entirely-thick-rees-valuation/research/notes/2026-10-07-thick-generic-normalization-filter.md)
already preserve this organization and its unproved coverage boundary.
The new theorem below classifies an entire normalization lane in every
carrier degree.

## 2. The exact divisor ray on a singleton lift

Let `C` be a smooth integral curve of degree `d` and genus `g` in `P3`.
Let `X` be an integral degree-`a` hypersurface containing `C`, with finite
normalization `nu:S->X`, and put `H=nu*O_X(1)`; `H` is ample and
`H^2=a`. Assume

    (nu^{-1}(C))_red=c,  and  nu|c:c -> C is an isomorphism.       (2.1)

This is an explicit support and degree-one hypothesis. If `X` is
generically regular along `C` and has a mate, the accepted full-support
theorem implies (2.1): there is one dominating prime because normalization
is an isomorphism at the generic point, isolated inverse-image points
are prohibited by the mate, and a finite birational map to the normal
curve `C` is an isomorphism. Some nonregular unibranch carriers also
satisfy (2.1).

If a mate of degree `b` exists, its pullback has divisor `m c`, with

    m d=a b,   m c~b H,   c_num=(d/a)H,   c_num^2=d^2/a.          (2.2)

Here `c` is Q-Cartier because an actual positive multiple is Cartier;
the intersection numbers are therefore defined without any assumption
on the normalization singularity type.

Set `h=gcd(a,d)`, `u=a/h`, `v=d/h`, and

    D=u c-v H in Cl(S).                                        (2.3)

Every normalized mate has `m=u k,b=v k`. Its existence therefore forces
`D` to be torsion. Conversely, if `k D=0`, linear equivalence gives a
section of `O_S(v k H)` whose divisor is exactly `u k c`. This supplies
the required positive Cartier support upstairs. It supplies an ambient
mate exactly when this section descends through the full conductor.

For a normal carrier `X=S`, descent is automatic, so (under (2.1)) the
criterion `D is torsion` is necessary and sufficient. It is also necessary
and sufficient if all normalization defect is supported on `C`, by the
accepted [asymptotic conductor theorem](2026-10-06-session-conductor-support.md).
On a general nonnormal carrier, torsion upstairs leaves a real additional
descent obstruction. This exact distinction survives arbitrary degrees.

If `t c` is Cartier, restriction of its line bundle to the smooth `c`
gives the stronger elementary index condition

    a divides t d^2.                                          (2.4)

Indeed its restriction has integer degree `t c_num^2=t d^2/a`.
Using only the Cartier square would give the weaker condition
`a divides t^2 d^2`. If `z K_S` is Cartier, and `pi` is the sectional
genus of `(S,H)`, intersection with `c` similarly gives

    a divides z d(2 pi-a-2).                                  (2.5)

The sectional genus here is that of a general hyperplane pullback,
chosen to avoid the finitely many singular points of the normal surface.
Adjunction gives `K_S.H=2pi-a-2`; this numerical identity is defined
even if `K_S` itself is not Q-Cartier, by intersection with the Cartier
hyperplane divisor. Condition (2.5) is used only when the stated global
Cartier canonical multiple exists.

## 3. Smooth normalization of a rational curve: all degrees at once

**Theorem.** Work over an algebraically closed field of characteristic
zero. Let `C` be a smooth rational curve of degree `d`, and assume (2.1),
that `S` is smooth, and that `X` has a mate. Then the polarized pair
`(S,c)` is a smooth surface of minimal degree with `c` its hyperplane
section. More precisely, the complete possibilities are:

| Normalization and lifted curve | Hyperplane pullback `H` | Carrier degree `a` |
|---|---|---|
| `S=P2`, `c` a line | `O_P2(d)` | `d^2` |
| `S=P2`, `c` a smooth conic; `d` even | `O_P2(d/2)` | `d^2/4` |
| A smooth rational normal scroll of degree `n>=2`, `c` its hyperplane section; `n` divides `d` | `(d/n)c` | `d^2/n` |

The scroll entry means `S=F_e`, `c=E+t f`, with `E^2=-e`,
`t>e>=0`, `n=2t-e`, and the usual equality of the two rulings when
`e=0`. The scroll degree `n` is finite: it is a positive divisor of
`d`, not an independently unbounded carrier parameter.

**Proof.** Smoothness makes `c` Cartier. Equation (2.2) implies

    n=c^2=d^2/a is a positive integer.

It also makes `c` ample, since its numerical class is a positive multiple
of the ample `H`. Adjunction on the smooth rational `c` gives

    K_S.c=-n-2<0.

Thus `K_S.H<0`. No positive multiple of `K_S` is effective, and the
characteristic-zero classification makes `S` rational or birationally
ruled over a curve of positive genus. In the latter case the ruling
extends to a morphism from `S` after the point blowups from its minimal
ruled model. Any map `P1` to the positive-genus base is constant, so
`c` is contained in a fiber. A fiber component has self-intersection
at most zero: for the full effective fiber `F`, `F.c=0`, while the
other components meet `c` nonnegatively. This contradicts `c^2=n>0`.
Consequently `S` is rational, and `H^1(S,O_S)=0`.

The exact sequence

    0 -> O_S -> O_S(c) -> O_P1(n) -> 0

shows `h0(S,O_S(c))=n+2` and that restriction to `c` is surjective.
The canonical section is nonzero away from `c`, and the restricted
sections generate `O_P1(n)`, so `|c|` has no base point. Its morphism
`phi:S->P^(n+1)` is finite because `c` is ample. If `Y` is its image
and `e_phi` its generic degree, then

    n=e_phi deg(Y),   deg(Y)>=codim(Y)+1=n.

The image is nondegenerate because the complete system is used.
Therefore `e_phi=1` and `deg(Y)=n`. The Del Pezzo--Bertini classification
makes `Y` a minimal-degree surface: a plane, a rational normal scroll
(including cones), or the Veronese surface. These surfaces are normal.
Hence the finite birational map from normal `S` is an isomorphism.
Since `S` is smooth, the singular cones are excluded; the smooth
classification in the table follows.

On a smooth rational surface numerical and linear equivalence of
divisors agree. Thus `H=(d/n)c` in `Pic(S) tensor Q`. On a scroll the
coefficient of `E` in `c` is one, so integrality forces `n|d`. On `P2`
with a line this gives `H=d h`; with a conic it gives `H=(d/2)h` and
requires `d` even. The displayed carrier degrees follow by squaring.

The only newly consulted primary classification interface is
[Eisenbud--Green--Hulek--Popescu, *Small schemes and varieties of minimal degree*, introduction](https://arxiv.org/html/math/0404517v5),
which states the degree bound and Del Pezzo--Bertini classification.
The surface-classification and rational-surface Picard facts are the
same standard inputs already used in the accepted quartic/quintic
arguments. This proof does not use an unverified classification of
projections of these surfaces.

## 4. Fixed C0: only two higher smooth-normalization models remain

For `d=4`, the scroll divisors are `n=2,4`; the plane-conic entry also
has `n=4`. Thus all smooth-normalization carriers satisfying (2.1)
have degree `4,8,16`. The accepted degree-four theorem removes the
entire first degree, leaving exactly:

    a=8:  S=P1 x P1, c=(1,1), H=(2,2), pi=1;
    a=16: S=P2,       c=line,  H=4h,    pi=3.                  (4.1)

For the degree-two scroll, smoothness and ampleness force the smooth
quadric: `2t-e=2,t>e>=0` leaves `t=1,e=0`. The sectional genera in
(4.1) follow either from the polarization or from adjunction:

    2g-2=d(d+2pi-a-2)/a,
    for d=4,g=0: pi=(a-4)/4.                                (4.2)

These are necessary normalization/projection targets, not constructed
mate carriers. The original four ambient coordinates must be a
four-dimensional generating subspace of `H0(S,H)`, finite birational
onto its degree-8 or degree-16 image, restricting to the prescribed
deleted-middle-monomial quartic on `c`. Full inverse-image equality,
the actual conductor, and its entire power-descent equation remain
required. The dimensions of the complete systems are respectively
9 and 15. The finite target does not by itself bound all projections
or remove their split conductor phases.

Both entries have `H~q c` with `q=2,4`. Consequently the primitive
normalized section `Q` has degree one and divisor `q c`, and every
normalized mate of degree `b` is a scalar multiple of `Q^b`.
Under the separately audited [single-field conductor power-compression theorem](2026-10-13-evening-general-conductor-power-compression.md),
if no conductor prime is contained in `c` and every generic reduced
upstairs conductor algebra is one field of degree at most two, any
mate compresses to ambient degree two. This is excluded by the accepted
quadric theorem. More generally, residual degrees at most three
compress to degree six, a bounded remaining target; residual degrees
at most four compress to degree twelve. The exponent is the least
common multiple across field degrees, so one must not replace this
by their maximum.

If all actual generic residue degrees are exactly one, two, or four,
without a degree-three point, exponent four suffices; the accepted
all-quartic theorem then excludes the carrier. This is a conditional
coverage statement. Split residual products, conductor components
inside `c`, and larger degrees remain outside it. In particular,
ordinary projection heuristics are not a proof that every projection
has an integral double-cover conductor.

## 5. Normal carriers and the actual source of unboundedness

On a normal hypersurface, the exact criterion is torsion of (2.3).
The canonical index filter imposes no new restriction there:
`K_X=(a-4)H`, so `K_X.c=d(a-4)` is already integral. If a mate exists,
the curve's Cartier index is at least `a/gcd(a,d^2)` by (2.4).
This lower bound grows with `a`; it is not an upper degree bound.

For a rational singleton lift on a normal carrier whose singularities
along `c` are ADE, let `sigma:M->S` be its crepant resolution and
write the Mumford pullback `c_num=c# +Z`. The smooth strict transform
is rational and adjunction gives the uniform exact correction equation

    -Z^2=2+d(a-4)+d^2/a.                                    (5.1)

Indeed `c#^2=c_num^2+Z^2`, and `K_M.c#=K_S.c=d(a-4)`.
This is a necessary equation in the entire exceptional lattice.
It organizes every carrier degree by a local correction budget. The
exceptional lattice can itself grow with the carrier and is not
bounded by the accepted quartic proof. Without a new global bound or
geometric realization theorem, (5.1) does not exclude all `a`.
For noncrepant resolutions the discrepancy intersection must also
be retained; replacing it by zero would be invalid.

## 6. Minimum-carrier choice: what is justified

For an actual STCI pair with no common surface component, each
irreducible factor of either form is itself a carrier with the other
form as mate; this is the accepted positive-degree factor argument.
It is therefore legitimate to select an integral carrier of minimum
degree among all carriers that admit a mate for `C`.

This choice supplies neither generic regularity along `C` nor smooth
normalization nor the singleton degree-one lift (2.1). The fact that
there are smooth general surfaces containing `C` in sufficiently
large degree also supplies no mate on such a surface. Linear
combinations `G+F T` preserve a given pair when the degrees permit,
but can stay singular along `C` when both generators have generic
normal order at least two. Thus there is no presently justified
degree-lowering or smooth-normalization lemma for a minimum carrier.

The theorem in section 3 consequently reduces every smooth-normalization,
singleton degree-one rational lane at once, including thick carriers
when they satisfy those stated hypotheses. It leaves singular
normalizations, several inverse-image primes, and finite lifts of
degree greater than one as distinct global tasks. The accepted
quartic/quintic exclusions do not remove those tasks.

## 7. Continuation-ready program

The fastest general continuation now has specific targets:

1. Independently audit the proof of section 3 and route it as an all-degree
   normalization theorem if accepted. No old verifier rerun is needed.
2. On the two models (4.1), derive the entire conductor from the actual
   four-coordinate projection and either exclude split phase descent
   geometrically or apply a justified residual-field bound. This is a
   finite normalization-type problem across all mate degrees.
3. For singular normalizations, work with the primitive ray (2.3), the
   stronger Cartier index (2.4), and the full exceptional correction
   equation, rather than extrapolating a quartic first-jet proof.
4. For thick carriers with multiple primes above `C`, retain a positive
   coefficient vector on every prime and its Cartier/Picard compatibility.
   A singleton divisor-ray theorem cannot be substituted for that vector.
5. Seek a structural theorem about minimum mate-admitting carriers. The
   missing theorem must actually force bounded Cartier index, bounded
   normalization type, or a divisor-class obstruction across every
   allowed inverse-image vector. None of these is assumed established.

The companion [symbolic-ribbon generalization](2026-10-13-generalization-ribbon-numerical-criterion.md)
develops a different reusable obstruction from the accepted ribbon
arguments. Its audit status must be checked before using it as a
premise. The root's new conductor power theorem is also a separate
dependency, not proved by this note.

No claim here proves that every integral projective curve is STCI,
or supplies a universal counterexample. The new content is a written
classification of an entire rational-curve normalization lane and an
exact framework that identifies why the remaining global degrees are
still unbounded.
