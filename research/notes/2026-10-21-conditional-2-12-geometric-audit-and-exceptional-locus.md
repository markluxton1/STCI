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
[the strict-surface proposal](2026-10-20-conditional-2-12-surface-bound.md)
and [the forced-norm proposal](2026-10-20-conditional-2-12-geometric-continuation.md).
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
