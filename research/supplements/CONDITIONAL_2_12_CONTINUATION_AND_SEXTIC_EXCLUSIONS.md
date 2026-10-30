# conditional 2 12 continuation and sextic exclusions

## Proof-dependency map: conditional exclusions and exceptional loci

The [strict-surface continuation](#2026-10-21-conditional-2-12-surface-bound-continuation) and [exceptional-locus audit](#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus) refine the original conditional (2,12;6,16;2) geometry. The [surface audit continuation](#2026-10-21-conditional-2-12-surface-audit-cont2) and [free-orbit sextic exclusion](#2026-10-21-cont2-free-orbit-global-sextic-exclusion) make more specific deductions under the retained assumptions.

These depend on the [symbol and actual sextic realization tests](CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-global-realization-incidence) and on the [node/conductor constraints](CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface). The surface-bound arguments, exceptional-locus computations, and actual homogeneous lifting are distinct steps. A conditional exclusion on a specified orbit or singularity type does not eliminate all (2,12) pairs.

Retain the original hypotheses, computational certificates, exceptional cases, and independent audits as the evidence for each narrow conclusion.

---


Complete mathematical arguments and exploratory boundaries preserved. Conditional conclusions remain conditional; computational and geometric obstructions are not asserted beyond their original hypotheses.

---

## 2026-10-21-conditional-2-12-surface-bound-continuation

# Conditional (2,12;6,16;2): strict-surface continuation and independent audit

Date: 2026-10-21. Author: `surface_bound` worker.

Status: **continuation of reviewed conditional proposals**. The normal
strict-sextic exclusion has independent review PASS in the linked audit.
The ampleness and nodal extension are independently reconstructed below.
No canonical result record is changed, and no global pair or emptiness
of the full residual incidence is asserted.

## 1. Saved work and exact authority

The pre-interruption contribution is
[the October 20 surface-bound proposal](CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-surface-bound).
It proves that an ACTUAL supported pair in the exact conditional
configuration cannot have a normal strict sextic `D` on
`B=Bl_C0(P3)`. Its proof was independently reconstructed by
`incidence_audit` in
[the October 21 audit, section 2](#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus).
The inherited mathematical inputs are promoted R-0010 and R-0011;
the finite singular-root bridge remains a separately reviewed,
unpromoted dependency. This continuation does not broaden those
promoted theorem statements.

For a normal strict sextic, the local Jacobian containment

    J_(A*p+t^10*U) subset (A,p,t^9)

gives total Milnor number at least `9*16=144`. It applies to all
multiplier multiplicities and all retained root types. A genus-six
general plane section of a resolution bounds its irregularity by six;
the resolution/contraction exact sequences give `b1(D),b3(D)<=12`.
Since a smoothing has Euler number 28, the isolated singularities have
total Milnor number at most 50. The contradiction `144>50` is the
reviewed normality obstruction. It needs no V5 model, discriminant
degree formula, or K3 singularity classification.

## 2. Independent audit: the strict mate is ample

Let `L=3H-E`. The seven cubic generators of `I_C0(3)` give a closed
graph embedding

    B -> P3 x P6.

Indeed the Rees algebra of the generated twisted ideal is a quotient
of its symmetric algebra, so its relative Proj embeds in the trivial
projective bundle. The restrictions of the two hyperplane bundles
are `H` and `L`. Consequently

    G' =16H-2E=10H+2L

is the restriction of the ample bundle `O(10,2)`.

If a projective curve `Gamma` is contained in `Sing(D)`, it must
intersect `G'`, unless it is contained in `G'`; in the latter case it
is already in the actual common support. The actual strict pair has
common support precisely `Z`. Thus every singular curve of `D`
meets `Z`. This is a consequence of the ACTUAL supported pair and
does not follow from the abstract root incidence alone.

**Independent verdict: PASS.** This replaces an unjustified global
normality assumption by a local analysis along the actual common root.

## 3. Independent audit: reduced div_Z(alpha) excludes every retained root

The retained root types are smooth integral genus one, integral nodal,
and two `(1,1)` components meeting in two nodes. Assume
`div_Z(alpha)` is reduced. Then `alpha` has simple base zeros, each
away from root nodes and branch values of the degree-two projection.
In particular every zero of `alpha|Z` is a smooth point of `Z`.

Along the entire exceptional surface:

* At a multiplier fiber away from `Z`, the base derivative of
  `alpha*f` is nonzero, so `D` is smooth.
* At a smooth root point with `alpha` a unit, the root derivative
  makes `D` smooth.
* At a zero of `alpha|Z`, the exact equation is `A*p+t^10*unit`
  in regular coordinates, hence an isolated `A9` singularity.
* At a retained node, `alpha` is a unit. The parameter-preserving
  Morse lemma writes the strict sextic as `xy+h(t)`, where `t=0`
  is the exceptional surface. It has a singular curve through the
  point only when `h=0`; then that curve is uniquely `x=y=0` and
  is smooth and transverse to `E`.

Thus no singular curve is contained in `E`. Any singular curve
`Gamma` not contained in `E` can meet `E` only at the at most two
nodes of `Z`, with local intersection multiplicity one. On its
normalization put

    d=H.Gamma>0,          e=E.Gamma<=2.

At all these contacts `alpha` is a unit, so one may take the first
finite-bridge generator to be `F'` itself. Then

    G'=C*F'+t^10*unit.

Since `F'` vanishes on `Gamma`, restriction gives order exactly
ten times the order of `E` at each contact. There are no other
zeros of `G'|Gamma`, by actual sole common support `Z`. Hence

    G'.Gamma=10e.

The divisor class of `G'` also gives

    16d-2e=10e,          e=4d/3.

Integral positive `d,e` then imply `e>=4`, contradicting `e<=2`.
There is no singular curve, so the Cohen--Macaulay hypersurface
`D` is regular in codimension one and normal. Section 1 excludes it.

**Independent verdict: PASS.** Therefore every actual pair in the
exact configuration must have a NONREDUCED divisor `div_Z(alpha)`.
The proof retains singular nodes; it does not add a smooth-root
assumption. In coefficient terms the reviewed exceptional condition
is currently

    Disc_8(Ncomp(tau))*Res_(8,4)(Ncomp(tau),Delta)=0,

of total degree 52 in the nine root coefficients, with
`Delta=b^2-4ac`, `tau=f(-z/2,1)`, and the actual norm multiplier.
The earlier full root discriminant factor is unnecessary.

## 4. Conductor budget: a useful identity, not yet an exclusion

For an integral nonnormal strict sextic let `nu:Y->D` normalize it.
The finite-duality identity gives

    omega_Y = I_conductor tensor nu^*omega_D,
    omega_D=O_D(Q'),          Q'=2H-E.

Let `Cbar` be the conductor scheme on `Y`. If a general `L` section
meets all its components properly, normalizes the corresponding
section curve, and avoids the finitely many normalization singular
points, ordinary curve conductor duality gives

    L.Cbar=2*(6-g_L)<=12.

Here `g_L` is the geometric genus of that section curve. The identity
records the arithmetic-genus-six budget for a general `L` section;
it cannot be used when that section does not separate components or
meets a contracted conductor component improperly without checking
the stated conditions. In particular it is not a bound on the
length of the whole Jacobian scheme.

The normal plane class `H` has degree zero on exceptional vertical
fibers, whereas `L` has degree one there, so `L` can detect conductor
on such fibers. The initial budget of twelve alone nevertheless
allows several generic ordinary-double fibers and supplies no
contradiction by itself. High contact does not force their generic
transverse singularity to be `z^m+t^10`: the permitted formal model

    F'=p*(z^2+t^2)+t^10

is generically an ordinary double point along the fiber `z=t=0`.
Its conductor cost cannot be estimated by silently omitting the
`t^2` term in `A`.

## 5. Local nonnormal escape models and the global degree boundary

At a smooth ramification point a simple BASE multiplier can still
give a nonreduced pulled-back divisor. The exact formal model

    A=z, p=z-w^2-2t^5,
    F'=A*p+t^10=(z-t^5)^2-z*w^2

has smooth root `z=w^2` on `E`, simple base multiplier `z`, and a
singular curve `w=0,z=t^5`. Thus squarefreeness on the base alone
does not establish local normality. This model is not a global
sextic in the permitted coefficient space.

At a node with a simple base multiplier there are further local
escapes. Put

    R=(z-t)^2*(z-t^8),
    F'=z*w^2-R,
    p=(F'-t^10)/z.

The last expression is regular because `R(0,t)=-t^10`. Then
`F'=z*p+t^10`, the exceptional root is `w^2-z^2=0`, and the
singular curve `w=0,z=t` leaves `E`. This verifies why the case
where a base multiplier vanishes at a node needs its own analysis.

None of these formal constructions supplies actual global
`k`-coefficients of `F6,G16`, and the original literal normal-degree
budget of the sextic is still binding. They are countermodels to
missing local hypotheses, not counterexamples to the global
conditional exclusion sought by the user.

The separate conductor-ramification note develops a stronger route
through a Gorenstein surface with trivial dualizing sheaf. Applying
it here requires an independently justified contraction to such a
surface; the bare local bridge does not supply that contraction.
Until that bridge and the local conductor arguments are reviewed,
section 3 is the exact independently checked global exclusion.


---

## 2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus

# Conditional (2,12;6,16;2): geometric audit and an exact exceptional locus

Date: 2026-10-21. Author: `incidence_audit` worker.

Status: **independent review PASS for the normal-strict-sextic
exclusion; ampleness and nodal scope extension independently
reviewed PASS by `surface_bound`, with separate root reconstruction.**
No canonical record is edited. The configuration remains unresolved
on the explicit degree-52 exceptional locus in section 6. Sections
3--4 retain the weaker smooth-root step from which it was derived.

## 1. Exact scope and reviewed dependencies

The field is algebraically closed of characteristic zero,
`C=C0=[s^4:s^3t:st^3:t^4]`, and the hypothetical actual homogeneous
pair has degrees `6,16`, sole reduced support `C`, FULL generic
coprime ordinary initial CI `(2,12)`, and ACTUAL saturated
movement-two first relation. Let `B=Bl_C(P3)`, let `E` be the
exceptional divisor, and put `H=pi^*O(1)`.

The promoted inputs are
[R-0010](../results/saturated_first_relation_normal_flatness.md) and
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md).
The finite singular-root bridge is a separately reviewed but
unpromoted dependency in
[the October 20 singular-root note](2026-10-20-conditional-2-12-singular-gluing.md).
It gives common order-two transforms with local ideal `(p,t^10)`
at every full root point. The full root `Z=(f)` is reduced of class
`(2,2)` on `E`, and `Z->C` is finite flat of degree two.

This review concerns
[the strict-surface proposal](CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-surface-bound)
and [the forced-norm proposal](CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-geometric-continuation).
Inherited chart, normal-flatness and root-obstruction verifiers were
not rerun. The normal-surface argument below was independently
reconstructed from its geometric inputs.

## 2. Normal strict sextics: independent review PASS

Write `D=(F6)'`, of class `6H-2E`. At a zero of `alpha|Z`, the
other original symbol coefficient `beta` is a unit. After choosing
`p=G16/t^2` up to a unit, the actual generator change gives

    F6/t^2=A*p+t^10*U,             U a unit,

and the divisor of `A|Z` equals that of `alpha|Z`. The ideal
`(A,p,t)` is a parameter ideal in the regular three-dimensional
ambient ring, hence a regular sequence. Differentiation gives the
ordinary Jacobian containment

    J_(F6/t^2) subset (A,p,t^9).

For an isolated singularity its Milnor number is therefore at
least `9*length O/(A,p,t)`. This works at multiple zeros and
singular root points: it uses a complete-intersection length, not
smooth local coordinates. Since `length div_Z(alpha)=2*8=16`, a
normal `D` would have

    sum mu_x(D) >= 144.                                    (1)

The blowup intersection calculations were independently checked:

    H^3=1, H^2 E=0, H E^2=-4, E^3=-14,
    K_B=-4H+E,
    c2(B).H=10, c2(B).E=16,
    D^3=40, c1(B).D^2=40, c2(B).D=28.

For example a general plane transform is `Bl_4(P2)`, with Euler
number seven, giving `c2(B).H=7+3=10`. On `E=P1 x P1`, the normal
bundle is `O(7,-1)`, giving `c2(B).E=4+(2,2).(7,-1)=16`.
Adjunction yields `K_D=(2H-E)|D`, `K_D^2=-4`, and smooth-member
Euler number `28`.

The seven cubics `q*x0,...,q*x3,A,B0,D0` generate `I_C(3)`.
On `Q`, the last three are the local equation of `C` multiplied
by the basepoint-free first-ruling quadratics `a^2,ab,b^2`.
Together with `q` this proves sheaf generation, including along
`C`. Thus `L=3H-E` and `2L=6H-2E` are basepoint free; their general
members are smooth by Bertini. This supplies a smoothing in the
same linear system.

Connectedness of `D` follows from `H1(O_B(-D))=0`. By Serre
duality this is `H2(O_B(2H-E))=0`; the strict quadric sequence
reduces it to the acyclic bundle `O_Q(1,-1)` and the rational
threefold `B`. Hence a normal `D` is connected and integral.

For a projective resolution `S->D`, the pullback plane class `h`
is nef and big, with square six. A general plane avoids the finite
singular-point images, and its strict curve is smooth and
irreducible. Adjunction computes genus

    1+(6+4)/2=6.

The nef-and-big Kawamata--Viehweg theorem applies to the integral
divisor `h` on the smooth projective `S`, so
`H1(K_S+h)=0`. Serre duality and the restriction sequence inject
`H1(O_S)` into the genus-six curve's `H1`, proving `q(S)<=6`.
The relevant theorem was checked directly in
[Fujino's statement, Theorem 0.1](https://www.math.kyoto-u.ac.jp/~fujino/kawamata--viehweg2.pdf);
there is no fractional boundary in this application.

The exceptional curves of `S->D` have negative-definite
intersection matrix, so their `H2` classes inject into `H2(S,Q)`.
The contraction exact sequence then gives `b3(D)=b3(S)<=12`.
Connected fibers give `b1(D)<=b1(S)<=12`. With `b0=b4=1` and
`b2>=0`, this gives `e(D)>=-22`. The isolated hypersurface
smoothing formula gives

    sum mu_x(D)=28-e(D)<=50,                                (2)

contradicting (1). No assertion `b1(D)=0`, crepant resolution, or
classification of K3 singularities is needed. Over a general
algebraically closed characteristic-zero field, the finite-type
data descend to a finitely generated field embedded in `C`;
geometric normality and the actual hypotheses persist. This
proves the claimed exclusion with its exact normality assumption.

**Review outcome:** PASS. The threshold `144>50` includes all
multiplier multiplicities and all retained root types. The proof
does not apply directly to positive-dimensional singular loci.

## 3. Ampleness extends the exclusion to a whole root open

The seven cubic generators give a closed graph embedding

    B -> P3 x P6,

with `H` and `L=3H-E` the restrictions of the two hyperplane
classes. This follows from the Rees-algebra construction of the
blowup, after twisting the ideal by `O(3)`. Consequently the
strict mate divisor

    G' =16H-2E=10H+2L

is the restriction of `O(10,2)` and is **ample**. This argument
uses positive coefficients on both graph factors and does not
claim that `L` itself is ample.

The actual common-transform intersection has reduced support
exactly `Z`. Off `E` this follows from sole reduced support of the
original pair; on `E` it follows from the jointly generating
coefficient pair `(alpha,beta)`.

Assume now that `Z` is smooth and that `div_Z(alpha)` is reduced.
At a point of `Z` with `alpha!=0`, the strict sextic is smooth,
because its exceptional restriction is a unit times the smooth
root equation. At a zero, `(A,p,t)` are regular local coordinates
and the equation is `A*p+t^10*unit`, an isolated `A9` singularity.
Thus the singular locus of `D` is zero-dimensional in a
neighborhood of `Z`.

If the global singular locus of `D` had a curve component
`Gamma`, then ampleness of `G'` would force `Gamma` to meet `G'`.
A contained curve would itself lie in `Z`; otherwise its
intersection is nonempty and lies in `Z`. Both alternatives
contradict local zero-dimensionality of the singular locus at
every point of `Z`. Hence `Sing D` is finite. A hypersurface is
Cohen--Macaulay, and finiteness of its singular locus gives
regularity in codimension one; Serre's criterion makes `D`
normal. Section 2 then contradicts existence.

**New consequence:** an actual pair in this conditional
configuration cannot have both a smooth full root and a reduced
divisor `div_Z(alpha)`. This uses actual support and global
ampleness; a bare root incidence point does not supply them.

## 4. First polynomial exceptional locus (strengthened in section 6)

In the fixed original coefficient coordinates put

    Delta=b^2-4ac,
    tau=(z^2/4)a-(z/2)b+c,
    alpha proportional Ncomp(tau).

The last identity and `tau!=0` are the universal norm lemma of
the October 20 geometric note. That lemma was independently
reconstructed and reviewed PASS by the separate `surface_bound`
worker; its local contact proof, including ramified fibers and
collision multiplicities, is recorded there. No new self-audit
status is assigned to that authored lemma here.

For a finite flat quadratic root in characteristic zero,

    Z smooth iff Disc_4(Delta)!=0.

When `Z` is smooth, the pulled-back divisor of the base binary
octic `alpha` is reduced precisely when `alpha` is squarefree and
its zero divisor avoids the branch divisor `Delta`. The exceptional
closed condition from the smooth-root step is therefore

    E(f)=Disc_4(Delta)
           *Disc_8(Ncomp(tau))
           *Res_(8,4)(Ncomp(tau),Delta)=0.                 (3)

Here every discriminant and resultant is homogeneous; zero or
infinite affine roots are retained. The degrees in the nine
coefficients of `f` are respectively `12,28,24`, so `E` has
degree `64`. The open `tau!=0`, the reduced doubly finite root
open, the exact Picard gluing condition and all earlier ambient
and global coefficient conditions remain in force.

Equation (3) is necessary for an actual global pair. It does not
say that its zero locus has actual pairs, or that it is empty
after the other equations. It retains the singular-root strata,
multiple multiplier zeros, and collisions between multiplier
zeros and branch points.

## 5. Why the exceptional strata cannot be silently discarded

The local bridge alone permits a positive-dimensional singular
locus when the multiplier has a multiple zero. For example

    A=z^2, p=x, F'=x*z^2+t^10

has `U=1` and finite `(A,p,t)` but is singular along `z=t=0`.
That is a whole exceptional-fiber direction, not an isolated
Milnor singularity.

Even squarefreeness on the base is insufficient at ramification.
Take a smooth root `p mod t=z-w^2`, the simple base multiplier
`alpha=z`, and

    A=z+t^5, p=z-w^2-t^5,
    F'=A*p+t^10=z^2-z*w^2-w^2*t^5.

The singular locus contains `z=w=0`, with `t` arbitrary. Thus
the root is smooth and `alpha` is squarefree on the base, but its
pullback divisor is not reduced and the normality conclusion
fails. The resultant factor in (3) is justified. These are local
countermodels to an omitted hypothesis; neither is asserted to
come from a global sextic with the permitted degree budget.

At a multiple base zero `c` of `alpha`, the first cubic matching
condition says, on the exceptional fiber,

    F3(c,u,v)=f(c,u,v)*(ell(c)u+m(c)v).

The entire fiber can be singular only if `ell(c)=m(c)=0`, since
`f(c,u,v)` is a nonzero polynomial. If the quotient linear form
is nonzero, only its finite zeros and the root points can be
singular on that fiber. This gives a further exact local test;
it is not by itself a criterion excluding singular curves that
leave the exceptional divisor through one of those points.

The remaining task is to combine this exceptional locus with
the actual cubic and higher global sextic lifts, or control its
normalization and conductor. The isolated Milnor bound does not
dispose of these loci, and the present note makes no conditional
emptiness claim on them.

## 6. Nodal extension: only a nonreduced multiplier divisor remains

The smoothness hypothesis on `Z` in section 3 can be removed.
After the full Picard torsion test, the only retained roots are
smooth integral, integral nodal, and two `(1,1)` components meeting
at two transverse nodes. In particular `Z` has at most two
ordinary nodes. Cusps and tangent-component roots are already
excluded by the torsion-free additive Picard argument; this
extension does not reopen them.

**Claim.** Every actual pair in the exact conditional configuration
has a nonreduced divisor `div_Z(alpha)`.

**Proof.** Suppose that divisor is reduced. Then every base zero
of `alpha` is simple, and its inverse image consists of two
distinct smooth unramified root points. In particular `alpha`
does not vanish at a node: a Cartier function vanishing at an
ordinary node cannot cut out a reduced point there. The elementary
double-cover equation also shows that every multiplier zero avoids
the discriminant divisor `Delta`.

We describe `Sing D` along the entire exceptional surface, not
only along `Z`:

* Outside `Z` and the fibers over multiplier zeros, `D` does not
  meet `E`.
* On a multiplier fiber away from `Z`, the derivative of
  `alpha*f` in the base direction is nonzero, since the multiplier
  zero is simple and `f` is a unit. Thus `D` is smooth there.
* At a smooth root point with `alpha!=0`, the nonzero root
  derivative makes `D` smooth.
* At a multiplier zero on `Z`, the simple intersection gives the
  isolated `A9` singularity of section 3.

It remains to examine a node of `Z`, where `alpha` is a unit.
Use `t=0` as the exceptional equation, and two tangential
coordinates on `E`. The restriction of `F6/t^2` has an ordinary
node, so its Hessian in the two tangential variables is
nondegenerate. The analytic Morse lemma with parameter `t`, or
its characteristic-zero formal version, puts the local equation
in the form

    x*y+h(t),

by a coordinate change preserving `t`. If `h` is not identically
zero, the surface is smooth or has an isolated `A_n` singularity
and is normal. If `h` is identically zero, the local singular
locus is the unique smooth curve `x=y=0`, transverse to `E`.
It has intersection multiplicity one with `E`. These statements
also hold over an arbitrary algebraically closed
characteristic-zero field after completion or descent to `C`.

Suppose `D` is not normal. Its hypersurface singular locus then
has positive dimension, hence contains an integral projective
curve `Sigma`. (A two-dimensional component is already impossible:
its intersection with the ample mate would give a curve in `Z`
where `D` is generically smooth.) The preceding local description
shows that no such curve is contained in `E`, and every point of
`Sigma intersect E` is one of the at most two nodes, with local
intersection multiplicity one. Hence

    d=H.Sigma is a positive integer,
    e=E.Sigma is an integer with 0<=e<=2.                    (4)

There are no intersections of `Sigma` with the strict mate outside
`Z`, by actual sole support. At each possible node contact
`alpha` is a unit, so choose the finite-bridge generator to be
`p=F6/t^2`. The other original generator then satisfies

    G16/t^2=C*p+t^10*V,           V a unit.

Restricting to the smooth branch of `Sigma` gives exactly order
ten at each of its transverse exceptional contacts. In particular
the strict mate cannot contain `Sigma`, and its intersection
degree is `10e`. On the other hand its divisor class gives

    16d-2e = G'.Sigma = 10e,
    4d=3e.                                                    (5)

Since `d>0` and `d,e` are integers, (5) forces `d>=3` and
`e>=4`, contradicting (4). This rules out all singular curves.
Therefore `D` is normal, and the normal-strict-sextic exclusion
in section 2 gives the final contradiction. The claim follows.

Consequently the exact exceptional closed condition strengthens
(3) to

    E_reduced_alpha(f)
       =Disc_8(Ncomp(tau))
           *Res_(8,4)(Ncomp(tau),Delta)=0.                    (6)

Its degree in the nine original root coefficients is `28+24=52`.
There is no factor `Disc_4(Delta)`: nodal full roots with a reduced
multiplier divisor have been excluded by the transverse-node
argument, so singular roots are not retained merely for being
singular. On the retained reduced double-cover locus, (6) says
exactly that `div_Z(alpha)` is nonreduced. The full finite-flat
root, homogeneous roots at infinity, and every earlier open and
gluing equation remain in force.

This is a necessary actual-global-pair obstruction. It is not a
proof that the zero scheme of (6), after the other global lifting
conditions, is empty. The remaining loci include multiple base
zeros of the forced norm multiplier and collisions of its zeros
with branch or node fibers. The local countermodels in section 5
explain why the normality argument cannot simply discard them.

**Independent review.** The separate `surface_bound` worker
reconstructed the exceptional-surface cases, parameter-preserving
Morse argument, unique transverse node branch, and divisor
identity `16d-2e=10e`, and reported PASS. The root agent separately
checked the same argument, including smoothness outside `Z` on
simple multiplier fibers. These are review records for a new
conditional proposal, not canonical promotion.

## 7. Where a remaining singular curve must meet the root

There is a further conditional classification useful for the
exceptional locus. Suppose the actual strict sextic is normal in
a neighborhood of `Z intersect {alpha=0}`. If a singular curve
`Sigma` remains, its contacts with `Z` are all nodes where
`alpha` is a unit. The parameter-Morse argument gives at most
two such contacts, each transverse to `E`. Write their number
as `n<=2`, and put `d=H.Sigma`, `e=E.Sigma`.

There can now be EXTRA contacts with `E` outside `Z`, on multiple
multiplier fibers; these must be retained. In particular it is
not valid to replace `e` by `n`. The actual mate has zeros on
`Sigma` only at its `Z` contacts, and its local order there is
ten. Thus the correct degree identity is

    16d-2e=10n.                                             (7)

If `Sigma` is not contained in the strict quadric `Q'`,
effectivity of `Q'=2H-E` gives `e<=2d`. Hence `12d<=10n<=20`.
For `d>=2` this is impossible. For `d=1`, the inequality forces
`n=2`, but (7) would give `e=-2`, also impossible. Thus every
remaining singular curve under the displayed normality
assumption is contained in `Q'`.

Since `D intersect Q'=R` has class `(4,0)`, such a curve is a
ruling line. It has `d=1`, `e=3`, and (7) gives `n=1`. It passes
through precisely one node of the full root, in the quadric
direction. Moreover `D` being singular along the line forces
its multiplicity in `R` to be at least two. The norm identity
then forces the corresponding multiplicities in `tau` and
multiple multiplier zeros at the other ruling-orbit points.
The ruling cannot be a branch fiber of `pi3`: such a line has
its entire length-three intersection with `C` at zero or
infinity, contradicting the transverse multiplicity one at
the node. Thus its three curve-intersection points are distinct.

Consequently an actual remaining pair must exhibit at least one
of the following concrete phenomena:

* The strict sextic is nonnormal at a root point where
  `alpha=0`.
* It is singular along a trisecant ruling line on `Q`, meeting
  the full root at an ordinary node in the quadric direction,
  with the forced residual-line and multiplier multiplicities
  above.

This is a classification under the stated local normality
alternative, not an exclusion of either phenomenon. The
`conductor_budget` worker independently checked (7), the need
to retain the extra exceptional contacts, the `Q'` inequality,
and the ruling-line conclusion. It reported the numeric
argument sound. Full conductor analysis of the two alternatives
remains open in this note.


---

## 2026-10-21-conditional-2-12-surface-audit-cont2

# Conditional (2,12;6,16;2): cubic-model and conductor continuation audit

Date: 2026-10-21. Reviewer: `surface_bound`.

Status: **independent review PASS for the cubic-model interface and the
ramified simple-multiplier exclusion; one incorrect normalization claim
in the separate nodal example is explicitly rejected below**. All results
are reviewed proposals rather than promoted records. No actual pair or
full emptiness result is asserted.

## 1. Scope and reviewed files

The exact actual-pair scope is `C0`, algebraically closed characteristic
zero, degrees `(6,16)`, sole reduced support `C0`, FULL generic coprime
ordinary initial CI `(2,12)`, and ACTUAL saturated movement-two first
relation. The reviewed inputs are:

* [the cubic-image and conductor interface](CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface);
* [the conductor-ramification proposal](CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-conductor-ramification), sections 1--6;
* [the normality and ampleness audit](#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus),
  whose nodal extension was independently reconstructed in
  [the surface continuation](#2026-10-21-conditional-2-12-surface-bound-continuation).

The singular-root finite bridge remains an explicit reviewed but
unpromoted dependency. The canonical lower-carrier input was read in
[R-0001](../results/quartic_carrier_exclusion.md), including its
**Consequences** paragraph, which expressly includes the earlier
plane/quadric/cubic exclusions and factor reduction. No inherited
carrier proof was rerun.

## 2. Exact cubic model: independent review PASS

I reran

    /opt/homebrew/bin/M2 --script research/computations/conditional_2_12_cubic_image_2026_10_21.m2

with exit code zero. The output verifies dimension four and degree five
for the homogeneous ring, projective smoothness by the Jacobian ideal,
the resolution with ranks `(1,5,5,1)` and shifts `(0,2,3,5)`, and vanishing
of the five displayed quadratic equations after substituting the seven
cubics. The computation is an exact check over `QQ`; it is not an
existence computation for `(F6,G16)`.

The resolution is Cohen--Macaulay of type one and gives
`omega_V=O_V(-2)`. Arithmetic Cohen--Macaulayness also gives connected
`Proj`; smoothness and connectedness imply integrality. The source
cubic map is birational on `q!=0`, where its first four coordinates
recover the original projective point. Its closed three-dimensional
image therefore equals this integral `V`.

On `V`, the four coordinates `y0,...,y3` cut out exactly the smooth conic
`Gamma` with equation `y4*y6-y5^2=0`. The inverse rational projection to
`P3` has this base IDEAL, not just this set-theoretic base locus. Thus
its graph closure is `Bl_Gamma(V)`. The Rees graph embedding of
`Bl_C0(P3)` has the same graph on the dense open, and both closures
are integral reduced schemes; hence they agree scheme-theoretically.
The common pullback divisor of `y0,...,y3` is exactly
`Q'=2H-E=L-H`, because the four remaining factors `x_i` have no common
zero. Consequently the contraction is an isomorphism off `Q'`, and
its contracted curves are precisely the appropriate ruling fibers.

The 23-dimensional sextic source consists of quadratic products of
the seven cubics. Equivalently `h0(V,O_V(2))=28-5=23` matches the full
source. Therefore every actual strict sextic descends as
`D=phi^*T`, with `T in |O_V(2)|`, and adjunction gives `omega_T=O_T`.
The quadric-factor exclusion says `D` has no `Q'` component, so `T`
does not contain the center conic.

The integrality step also passes. If an irreducible factor of `F`
did not contain `C0`, its intersection with the positive-degree mate
would produce a curve outside `C0`. Every factor is thus itself a
supported carrier. R-0001's stated consequences put its degree at
least five. Since `deg F=6`, only one factor with multiplicity one
is possible. Thus `F`, `D`, and `T` are integral under the ACTUAL
supported-pair hypotheses.

**Verdict: PASS.** This supplies the previously unresolved contraction
and descent hypotheses in section 3 of the conductor-ramification
proposal, within its exact actual-pair scope.

## 3. Full conductor duality and component genus: independent review PASS

Let `Y` normalize the integral Gorenstein `T` with `omega_T=O_T`.
Finite duality identifies `omega_Y` with the conductor ideal `I`
inside `O_Y`. Strictly, the `Hom_T` expression is a sheaf on `T`
and equals the pushforward of this `O_Y`-module; the module
identification itself is exact. Normal surface `Y` is Cohen--Macaulay.
The canonical ideal is depth two, so `C=V(I)` is a pure
Cohen--Macaulay curve (unless empty).

Apply `Hom_Y(-,omega_Y)` to
`0->I->O_Y->O_C->0`. Since `End_Y(omega_Y)=O_Y`, the resulting
cokernel is `O_Y/I`; codimension-one duality identifies it with
`omega_C`. Thus `omega_C=O_C`, even when `Y` is not Gorenstein
and the conductor is nonreduced.

For an irreducible reduced conductor component `R` of generic
multiplicity one, finite closed-immersion duality gives
`omega_R=Hom_C(O_R,O_C)=Ann(I_R)`. Its map into `O_R` is
generically nonzero and is injective because the canonical module
of an integral curve is torsion free. Its cokernel is finite;
Euler characteristics yield `2p_a(R)-2<=0`. Nilpotents on other
components do not affect this argument.

The map between the normalizations of `D` and `T` exists by the
universal property of normalization and is proper birational. A
conductor component not contracted by `phi` maps nonconstantly
and properly onto an integral conductor component, hence finitely.
It is birational because the ambient map is an isomorphism off
`Q'`. Therefore arithmetic genus can only increase in its image.
This remains true when the particular singular point lies on `Q'`.

**Verdict: PASS.** No assumption that the whole conductor is reduced,
or that the normalization is Gorenstein, has been inserted.

## 4. Ramified simple-base zeros: independent review PASS

At a smooth ramification point with a simple base zero of `alpha`,
both `A` and `p` are regular in the base coordinate `z`. Factoring
them by their unique roots in `z` and applying the parameter
Morse lemma gives exactly

    F'=x^2-B(w,t),
    B=s(w,t)^2-t^10*u(w,t),    s(w,0)=unit*w^2, u a unit.

The critical section in the centered `z` variable is divisible
by `t^10`; this verifies that the coefficient of `t^10` in the
critical value remains a UNIT. Therefore

    B=(s-t^5*sqrt(u))*(s+t^5*sqrt(u)).

The factors are coprime and each is Weierstrass of degree two in
`w`. Nonnormality forces precisely one to have a double linear
factor `e*d^2`, with `d=w-phi(t)`; the other cannot also be a
square, because its restriction to `d=0` has odd valuation five.

Here the finite normalization calculation IS valid: the double
cover is MONIC in `x`, and its normalization is
`R+R*y`, with `y^2=B_other` and original ring `R+d*R*y`.
The exact conductor is `d*(R+R*y)`. Its curve germ is
`y^2=t^5*unit`, reduced and irreducible, with delta two and
generic multiplicity one. A noncontracted global conductor
component would have arithmetic genus at least two, contradicting
section 3.

If the corresponding singular curve is contracted, it is a ruling
fiber `W` of `Q'`. Its normal bundle is `O+O(-1)` and `D|W=O`.
The nonzero discriminant of the global quadratic normal cone is
then a section of `O_W(2)`. The exact local normal form makes it
vanish to order five at the point, impossible. The parameter `t`
is indeed a uniformizer on `W=(x,d)`.

**Verdict: PASS.** Together with section 2, this removes the
conditional contraction hypothesis from the ramified simple-base
zero exclusion for ACTUAL pairs. It does not establish normality
at repeated base zeros or at nodes where `alpha` vanishes.

## 5. Strengthened exact exceptional locus

Assume `alpha` is squarefree on the base and does not vanish at
a root node. The ramified-simple-zero result removes the only
additional singular-curve contacts beyond the earlier nodal
argument. Every singular curve must then meet `E` solely in the
at most two root nodes, where `alpha` is a unit and the parameter
Morse form is `xy+h(t)`. A singular curve there is unique and
transverse to `E`. Writing `d=H.Sigma>0`, `n=E.Sigma<=2`, actual
support gives `G'.Sigma=10n`, whereas its class gives
`16d-2n=10n`, impossible. Thus `D` is normal and the reviewed
`144>50` obstruction applies.

Every actual pair must therefore satisfy at least one of:

    alpha has a multiple zero on the BASE;
    alpha vanishes at a NODE of the full root.

For smooth full roots, the new necessary equation is simply
`Disc_8(Ncomp(tau))=0`, degree 28 in the original root coefficients.
For nodal strata retain the actual node incidence
`alpha(c)=0, f(c,w)=0, df(c,w)=0`. These are necessary global
realization conditions. Their intersections with the full first,
second, torsion, and actual global sextic lifting conditions
have not been proved empty here.

## 6. Rejected finite-normalization assertion in the nodal caution

Section 7 of the conductor-ramification proposal correctly gives
the local equation

    F=z*w^2-(z-t^3)^2*(z-t^4)=z*p+t^10

and its nonnormal curve. Its subsequent claimed normalization
`y=w/(z-t^3)`, `z*(y^2-1)=-t^4` is NOT finite over the original
surface: at `z=t=w=0` its fiber contains the affine `y`-line.
Thus the assertions there that the finite conductor has two
smooth branches and that the displayed surface is the finite
normalization are rejected. A warning was added above that
historical paragraph rather than deleting it.

A potentially correct finite extension instead adjoins

    v=z*w/(z-t^n),         v^2=z*(z-t^m),
    z*w=(z-t^n)*v,
    v*w=(z-t^n)*(z-t^m),         2n+m=10.

The new generator is integral because its quadratic equation
is monic. Normality and the exact conductor of this extension
require their own verification. They are not assumed in the
exclusions of sections 2--5. In particular, the defective nodal
example supplies no evidence that the remaining global node
stratum survives the conductor test.


---

## 2026-10-21-cont2-free-orbit-global-sextic-exclusion

# Free cube-orbit endpoint chart: exact global sextic exclusion

Date: 2026-10-21, continuation 2. Status: **new exact conditional
exclusion, independently checked; not promoted to a canonical result**.

Work over an algebraically closed field of characteristic zero with
`C0=[s^4:s^3t:st^3:t^4]`, the accepted balanced conormal frame, and the
conditional `(r,s;a,b;epsilon)=(2,12;6,16;2)` configuration. This note
excludes the following precise structured incidence:

1. the moving quadratic root `f` satisfies the accepted first ambient
   incidence `K1`;
2. the sextic multiplier is the canonical cube norm of its quadric-line
   restriction, up to a nonzero scalar;
3. both endpoints of that restriction are nonzero and no root is carried
   to another root by multiplication by a primitive cube root of unity;
4. an actual global sextic has second symbol `alpha*f` and matches the
   canonical first cubic lift.

The incidence is empty as a scheme. The argument stops at the cubic
sextic obstruction. It needs neither a global mate nor a degree-twelve
standard-basis construction, because the required sextic already fails.
Applying the conclusion to actual supported complete intersections also
uses the separately proposed quadric-cycle norm argument. That scope
bridge is a dependency; this note does not promote it by implication.

## Inputs and evidence

The accepted first incidence and ambient chart are inputs from
[STCI-R-0007](../results/quadratic_root_obstruction_model.md). The actual
saturated-first-relation application uses the hypotheses of
[STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) and
the separately supplied finite singular-root bridge. The new global
source map is the previously recorded
[exact sextic symbol calculation](CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-symbol-map).

The exact new computations are:

- [four-parameter family exporter](../computations/conditional_2_12_cubic_reduction_2026_10_21_family.py),
  [Macaulay2 input](../computations/conditional_2_12_cubic_reduction_2026_10_21_family.m2),
  and [metadata](../computations/conditional_2_12_cubic_reduction_2026_10_21_family.json);
- [full global C3 specialization](../computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.py),
  [its exact equations](../computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.m2),
  and [all sixteen nonzero specialized equations](../computations/conditional_2_12_cubic_reduction_2026_10_21_candidates.json);
- [lightweight exact certificate](../computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2)
  and [successful output record](../computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.json);
- [independent rational-arithmetic reconstruction](../computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py)
  and [independent PASS record](../computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.json).

The lightweight certificate runs with
`M2 --script research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2`.
It checks both exact ideal containments and then checks the final unit
identity by literal polynomial multiplication. It does not rely on a
unit marker from an interrupted large elimination. The older large
coefficient lifts are preserved at
[the archived exact lift matrices](../computations/conditional_2_12_cubic_reduction_2026_10_21_family_lifts.m2),
but are unnecessary for this lightweight replay.

## The norm-symbol equations collapse to a symmetric family

Put

```text
l=u+(z/2)v,
g=f(z,-z/2,1),
D=4g=d0+d1*z+d2*z^2+d3*z^3+d4*z^4.
```

On `d0*d4!=0`, projective scaling of `f` and the actual `C0` torus give
a finite cover on which `d0=d4=1`. This normalization preserves the
accepted chart: its weights are `wt(z,u,v)=(1,4,3)`.

For a primitive cube root `omega`, let

```text
U=1+d3*z^3, V=d1*z+z^4, W=d2*z^2,
alpha=U^2+V^2+W^2-U*V-U*W-V*W.
```

Thus `alpha=D(omega*z)*D(omega^2*z)`, and `D*alpha=N(z^3)` for a
quartic `N`. Multiplying `alpha` by a nonzero scalar does not change
the existence question.

Use the coordinates

```text
a=(d2+2y1-4y3, d3+2y2, 1),
b=(y0,y1,y2),
c=(1/4,d1/4+y0/2,y3).
```

Eight of the eleven global second-symbol equations vanish identically
under the norm substitution. The remaining three are linear in
`(y0,T=y1-4y3,y2)`. After nonzero constant row rescaling their matrix is

```text
J = [ d2-d1^2          -d1                  1          ]
    [ -2d1+d2*d3      -1-d1*d3+d2^2        2d3-d1*d2  ].
    [ 1                d3                  d2-d3^2    ]
```

Its determinant has the exact interpretation

```text
det J = Res_z(z^3-omega^2*d2*z+d1,
              -omega*d2*z^2+omega^2*d2*d3*z+1-d1*d3).
```

The resultant vanishes exactly when `D(z)` and `D(omega*z)` have a
common root in this endpoint chart. No condition that `D` itself be
squarefree is imposed. The identity is checked by the determinant of
the five-by-five Sylvester matrix over `QQ[omega]/(omega^2+omega+1)`.

The Cramer numerators are exactly
`(-d1/4,-d2/2,-d3/4)*det J`. Hence on `det J!=0` the second-symbol
condition is equivalent to

```text
y0=-d1/4, T=-d2/2, y2=-d3/4.
```

Writing `t=y3`, this gives the four-parameter root family

```text
a=(4t,d3/2,1),
b=(-d1/4,4t-d2/2,-d3/4),
c=(1/4,d1/8,t).
```

It is useful to see the geometry of the compression. With `w=-2u/v`,

```text
8*f(z,-w/2,1)
 =(8t+d3*z+2z^2)w^2
  +(d1+(2d2-16t)z+d3*z^2)w
  +(2+d1*z+8t*z^2)
```

is symmetric in `z,w`, restricts on the diagonal to `2D(z)`, and its
`t` term is `8t(z-w)^2`.

## First compatibility and the quadric part of C3 leave four points

Let `G0` be the accepted canonical first cubic correction over `K1`, and
put `G(z)=G0(z,-z/2,1)`. For a global sextic, restriction to the fixed
quadric gives

```text
F|Q=v^2 R(z^3+v).
```

Consequently the norm-symbol and actual cubic matching conditions imply

```text
D | Nprime_T(z^3)-4*alpha*G.
```

Since `D0=1` and `det J!=0`, both `z` and `alpha` are units modulo `D`.
Differentiating `N(z^3)=D*alpha` therefore makes this exactly equivalent
to the four remainder equations

```text
rem_D(Dprime-12*z^2*G)=0.
```

Eight accepted first-incidence equations eliminate
`h0,...,h3,h8,...,h11` without denominators on `d0=d4=1`. Substitute
the symmetric root family. In

```text
QQ[d1,d2,d3,t,h4,h5,h6,h7]
```

the remaining eight `K1` equations and these four q-line cubic equations
generate exactly the following triangular ideal:

```text
h6=0, h5=0, h4=-2h7, d3=0, d1=0,
t=(27/4)h7^3+(15/32)h7,
d2=108h7^3-(9/2)h7,
648h7^4+45h7^2-4=0.
```

Both ideal containments are verified over `QQ`, and the independent
audit reconstructs the same ideal from its own first/C3 construction.
Thus this step is an exact scheme calculation, not a sample. It has
dimension zero and degree four. Writing `h=h7`, one also has
`24th=1` and `d2=16t-12h`. The four points obey

```text
h^2=(-5+3sqrt(17))/144  or  (-5-3sqrt(17))/144.
```

They satisfy `det J!=0`: here `det J=(d2^2-1)^2` and
`d2^2=216h^2-11`, which is never one on the displayed quartic. This
observation is a consistency check; the exact ideal computation was
performed on a closed enlargement and did not discard the determinant
boundary during its calculation.

## Full global sextic C3 gives a two-line unit certificate

The actual degree-six second-symbol map has kernel exactly `k*q^3`.
Consequently every global sextic with second symbol `alpha*f` has the
fixed rational `k`-linear source splitting plus one coefficient `eta`
of `q^3`. The full cubic comparison is

```text
F3-alpha*G0+eta*q1^3 = f*(ell*u+m*v).
```

Its necessary polynomial syzygy equations are obtained from the actual
global source matrices. They retain the coefficient `eta`; no generic
`k(C0)` coefficients or hidden splitting of a second relation are used.
At the four-point scheme, two of those exact equations are

```text
E4=(3/4)eta+(369/16)h-(891/2)h^3,
E8=(1/8)eta+(27/32)h-(81/4)h^3.
```

Their difference is

```text
E4-6E8=18h-324h^3.
```

Let `p=648h^4+45h^2-4`. The following is a literal identity in
`QQ[h,eta]`:

```text
1 = ((162h^2-1)/4)*p
    +(81h^3+(77/8)h)*(E4-6E8).
```

The independent standard-library rational verifier reconstructs the
specialized full C3 equations from a separate source construction,
matches the equation directions, and checks this identity without a
Groebner basis. Therefore all four candidates fail actual global
sextic C3, and the free-orbit endpoint incidence is empty.

## Precisely what remains outside this result

The conclusion excludes every root in the stated chart, including
singular full roots whenever the accepted/proposed necessity bridges
apply. It does not require a smooth root or reduced diagonal divisor
`D`. It does not cover `d0*d4=0` or `det J=0`.

On the orbit-collision boundary, cancellation by `alpha` is invalid.
The exact retained condition is the multiplication of the four simple
remainders by the four-by-four multiplication matrix of `alpha` on
`k[z]/(D)`. Its determinant is exactly `81*(det J)^2`, as recorded in
the [all-strata q-line exporter](../computations/conditional_2_12_cubic_reduction_2026_10_21.json).
The collision and endpoint strata remain separate work; this proof
does not silently saturate them away.

No unrestricted STCI conclusion or full decision of the conditional
configuration follows from this chart exclusion alone. No global pair
has been realized.
