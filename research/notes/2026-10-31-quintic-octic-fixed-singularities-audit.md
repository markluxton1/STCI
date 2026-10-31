# Independent audit: quintic–octic fixed singularities

This audit covers the original fixed-singularity investigation and the
reduced-symbol even-set continuation. The later
[ADE exclusion and its separate review](2026-10-31-quintic-octic-ade-exclusion-audit.md)
remove the reduced-symbol hypothesis using additional arguments; that stronger
scope is not inferred from the earlier proof audited here.

Date: 2026-10-31. Reviewer: fresh mathematical-review subagent, working
independently of the proposing agent; no nested delegation.

**Disposition: accepted as reviewed provisional mathematics at the stated
scopes. No canonical promotion and no exclusion of the entire (5,8) pair.**
The final disposition includes the even-set continuation in proposal
section 4.2: the entire subclass with reduced full quintic first-symbol
divisor and globally ADE quintic is excluded. The original rank-stage
review below is preserved, with its former surviving row superseded by
the continuation review at the end.

## Reviewed state and premises

Reviewed [the proposal](2026-10-31-quintic-octic-fixed-singularities.md),
sections 1–8, including its homogeneous residual-support control (11)–(12)
and the corrected section 6 weighted sums
`192,204;180,192,204;168,180,192`. The precise hypothetical object is a
proper sole-supported complete intersection of degrees five and eight on
the fixed quartic `[s^4:s^3t:st^3:t^4]`, over an algebraically closed field
of characteristic zero, with generic curvilinear length ten.
The final review also covers the added characteristic-zero descent and
complex embedding sentence in section 4 and the explicit section 6 scope
`tau<=length(B)`; both changes correctly qualify the arguments.

Read the project index, mathematical map and contribution checklist first.
Accepted premises, rather than freshly rerun proofs, are R-0001 and its
recorded factor/lower-degree reduction, R-0020, R-0034 and its
[source proof](2026-10-14-generalization-normal-index-socle-theorem.md),
and the reviewed ordinary-layer/lattice arguments in sections 2–5 of the
[normal-torsion note](2026-10-26-normal-torsion-spectral-genus-budget.md).
The [multiplicity-three note](2026-10-26-44-multiplicity-three-forces.md),
sections 4–5, supplies a related local argument, without transferring its
degree-four conclusions. I also checked the exact scope of
[R-0033](../results/constant_first_relation_lifting.md).

## Independent reconstruction

1. **First symbols and torsion support.** From `det E=O(-14)` and
   `E -> O(-q)`, the saturated kernel is `O(q-14)`; the scalar degrees are
   `q+6` and `q+18`. A second-order quintic restricts on the smooth quadric
   to a section containing `2C` of type `(2,6)`, impossible in `(5,5)`
   unless the restriction is zero. Division by Q then proves (2) as a
   statement about sheaf powers. The accepted factor reduction makes the
   quintic and every octic mate integral, so the quintic symbol is nonzero.
   The first torsion is exactly `M/M(-B)`. Outside B, a smooth carrier
   gives the actual ideal `(x,y^10)`; hence every ordinary torsion layer
   vanishes there. Conversely T1 is nonzero at every point of B. The
   positive total torsion therefore forces B nonempty. This proves support
   equality, not equality of B with the total torsion divisor or with a
   filtered-equation comparison defect.

2. **General octics.** Cubic restrictions span every monomial of degree
   twelve on the parameter line. Removing the gcd gives a basepoint-free
   system; its general affine member has simple zeros outside the finite
   forbidden set. This also covers `b=0`. Thus the moving count is exactly
   `q+18-beta`, at least twelve. At each moving zero the actual primitive
   ideal and invertibility of its two-generator matrix give
   `S=xA+y^10 U`, with U a unit and a simple curve zero of A, hence pair
   type `A9^1`. Bertini off C and the finite first-symbol divisor on C
   give isolated singularities and normality for a general octic. No ADE
   assertion at an arbitrary fixed point follows yet.

3. **Reduced B.** At a fixed simple zero the nonzero `tx` quadratic term
   gives Hessian rank at least two. Formal splitting gives `A_(r-1)`;
   an identically zero remaining term would give a curve of singularities,
   already excluded. The standard smooth-curve classification, with
   first-symbol order one, makes the pair `A_(r-1)^1`. Its local Cartier
   index is r, and its actual mate divisor `10C` forces `r|10`. In the
   normal local ring it is exactly `(tu-w^r,u^k)`, `rk=10`, up to units
   and changing generators. The lattice basis `u^i w^j` and identity
   `w^(ri+j)=t^i u^i w^j` give torsion `rk(k-1)/2=5(k-1)`.
   The top-power/socle comparison gives defect `k-1`. Excluding the smooth
   case and the case where the mate is smooth leaves only `(r,k)=(2,5)`
   or `(5,2)`, with defects four or one. This proves the eight-row table
   from `4u+v=9q-38` and `u+v<=q+6`, including the node-only conclusion.

4. **Quintic bound.** The two extra assumptions in section 4 are retained:
   the quintic scalar divisor is reduced and the quintic has only rational
   double points everywhere. At B, simple vanishing makes h a unit in
   `F=epsilon*u^k+h*S`; absorbing the extra term into t proves the same
   `A1/A4` pair type on F. The other scalar zeros are `A9`. Thus its
   exceptional rank above C is `9q+54-8u-5v`. For a globally ADE quintic,
   crepant resolution and the hypersurface invariants give `h11=45`.
   The hyperplane class has positive square and is orthogonal to the
   negative definite exceptional configurations, so their total rank is
   at most 44. The listed ranks are correct, leaving only `q=7,u=4,v=9`
   with rank 40. This argument would not justify that bound for arbitrary
   uncontrolled quintic singularities away from C.

5. **Octic weighted sums.** Independently enumerated all nonnegative
   solutions using exact rational arithmetic in an ephemeral Python call.
   The row counts, beta values, moving counts, quintic ranks, and corrected
   weighted octic sums all agree with the note. Under the established ADE
   description of the reduced-B general octic, the weight of an `An`
   point is `(n+1)-1/(n+1)`. All eight sums are below `784/3`.
   This is a non-exclusion check, not realization evidence.

## Actual homogeneous control

Independently reconstructed section 7 rather than treating it as a formal
local model. Both A and Q in (11) are irreducible; neither divides F, so
`gcd(F,A^2 Q)=1` and the global pair is proper. The stated affine change
of coordinates is a polynomial automorphism and gives (12) exactly.

The coefficient `t(t+y^2)` and constant term `y^2(t^4+y)` of F as a
linear polynomial in x are coprime: neither t nor `t+y^2` divides the
constant term. Gauss's lemma gives affine irreducibility. The homogeneous
F has no x0 factor, so it is integral globally. The lowest terms at p are
`t^2 x+y^3` and `x^2 y`; all octic mates therefore have multiplicity at
least three at p and cannot be rational double points there. Their fixed
first-symbol divisor has local order two.

At infinity, expansion of A in the stated coordinates gives exactly
`2c^5 X-3c^6 Y` to first order. Together with the finite chart this gives
saturation degree `-12+5=-7`, and quotient `O(-7)`. This proves the
claimed q=7 direction, without imposing length ten. Over `k(t)`, solving F
gives `x=-t^2 y^2+O(y^3)`, so `G=x^2 y` has leading term `t^4 y^5` and
generic intersection length five. Properness and Bezout then give residual
degree twenty. The line `x1=x3=0` lies in both surfaces and passes through
p, explicitly confirming residual support. Thus this control cannot be
used as a sole-supported counterexample or as a multiplicity-ten defect
model. These polynomial checks were reconstructed algebraically; no CAS
certificate or computational search is claimed.

## External sources, findings and limits

Checked [Ellia's actual paper](https://arxiv.org/html/1409.3801), including
Definition 8/Lemma 10, Theorem 12 and its proof, and the surface inequality
used in Proposition 14. The paper assumes a primitive CI for Theorem 12.
Here both actual generators are singular at B, so every local equation
of Y has zero linear term there. Its smooth-member premise fails, and
the incidence has fixed fibers. The note correctly reconstructs local
hypotheses separately before using an ADE bound; it does not extend
Ellia's primitive theorem to arbitrary fixed singularities.

The lead corrected the three q=6 weighted sums before final disposition;
the correction does not change the non-exclusion conclusion. No material
finding remains unresolved. The local examples refute the inequality
`tau<=length(B)`; they do not refute every possible bound involving B.

The surviving q=7 row is not excluded merely because its saturated first
direction is constant. R-0033 explicitly leaves positive-defect models
outside its exclusion. At a node of the survivor, even the symbolic triple
on the octic is nonprimitive, so the needed global primitive/next-relation
hypothesis has not been established. No inherited obstruction was rerun.

At the original rank-stage review, the accepted result was the scoped
fixed-defect description, reduced-B classification, and conditional rank
restriction, plus the verified residual-support control. At that stage
global realization of the rank-40 row remained undecided. Its disposition
is superseded by the following independent continuation; the earlier
mathematical checks are unchanged. No neighboring degree, unrestricted
STCI claim, canonical record, or promotion is covered.

## Continuation audit: integral parity and the forbidden cover

The user supplied a proposed elimination of the rank-40 row in the
October 31 continuation. Its report of an external independent review was
not accepted as evidence. I independently reconstructed the argument,
checked the primary external source, and then reviewed the integrated
proposal section 4.2 together with its revised sections 1, 4.1, 5 and 8.
This extension concerns precisely the two assumptions of section 4.1;
it does not classify repeated first-symbol zeros or other degrees.

**Integral Picard relation.** On the globally ADE quintic resolution X,
the actual octic divisor is `10C`, linearly equivalent to `8H`. This is
a Cartier linear equivalence before resolution, not a numerical relation.
At a node the correction to the rational pullback of C is `E/2`. For an
end-marked A4 chain it is `(4E1+3E2+2E3+E4)/5`: multiplication by the
negative Cartan intersection matrix gives `(-1,0,0,0)`. Thus the actual
pullback is

    10*Ctilde + 5*N + 2*A ~ 8*H.

Here N consists of exactly the four disjoint node curves and A is the
specified integral sum over the nine A4 chains. The explicit integral
divisor `D=4H-5*Ctilde-A-2*N` satisfies `2D~N`. This argument neither
divides in a numerical lattice nor assumes Picard torsion vanishes.
Exceptional curves over points off C have zero coefficient: the octic
divisor is locally a unit there. Their presence cannot change this parity
calculation.

**Existence, connectedness and invariants of the cover.** The line bundle
`O(D)` with its section of `O(2D)` cutting out N defines the algebra
`O_X direct_sum O_X(-D)` with the indicated multiplication. It is a finite
flat double cover, smooth because the branch curves are smooth and
disjoint. After any rational trivialization of the line bundle, the
defining rational function has odd valuation along each branch component;
it cannot be a square. The cover is therefore integral and connected,
not a disconnected pair of copies of X. The globally ADE assumption gives
`K_X~H`, `K_X^2=5`, and `chi(O_X)=5`. Since `N^2=-8` and `K_X.N=0`,
one has `D^2=-2` and `K_X.D=0`. Riemann–Roch and the direct-image algebra
give

    chi(O_Z) = 2*5 + (D^2 + D.K_X)/2 = 9,
    K_Z^2 = 2*(K_X+D)^2 = 6.

The sign of the D term in both formulas is correct: the nontrivial
direct-image summand is `O(-D)`, whereas the canonical class pulls back
`K_X+D`.

**Contraction and the global inequality.** The four ramification curves
map isomorphically to the node curves. From `f^*E_i=2R_i` their squares
are minus one, so they contract to a smooth projective surface W.
Contraction gives `chi(O_W)=9` and `K_W^2=10`. The tautological cover
section gives the actual line-bundle relation `R~f^*D`; hence

    sigma^*K_W ~ K_Z-R ~ f^*K_X = f^*H.

The last class is nef and big: H pulls back the ample hyperplane class
on the quintic and has positive square. Consequently `K_W` is nef and
big, W is minimal of general type, and Noether's inequality applies.
Since `p_g(W)=chi(O_W)-1+q(W)>=8`, it forces `K_W^2>=12`, contradicting
the computed value ten. Other ADE exceptional curves off C do not enter
the branch and do not disturb the nefness or the quintic invariants.

**External and field qualifications.** I checked Debarre's
[*Inégalités numériques pour les surfaces de type général*](https://www.numdam.org/item/10.24033/bsmf.1965.pdf):
the introduction, printed p. 320, states the classical Noether inequality
for minimal complex surfaces of general type; section 1.4, printed p. 322,
gives the double-cover data, canonical formula and cohomology splitting.
The Euler characteristic formula used here follows from that splitting
and Riemann–Roch. The mixed-configuration Picard implication and its STCI
application are reconstructed here, not attributed to that paper. I also
checked the [1983 addendum](https://www.numdam.org/item/10.24033/bsmf.1990.pdf):
it repairs the proof used for the stronger irregular-surface theorem 6.1,
which this argument does not use. The proposal's source qualification is
accurate. The given characteristic-zero descent is sufficient: descend
the finite hypothetical-pair data before resolving over the complex
numbers, or include the finite line-bundle, section and isomorphism data
if descending the constructed cover. No new assumption on the original
algebraically closed characteristic-zero field is required.

**Final disposition.** No material correction or unresolved condition was
found in the integrated continuation. The rank-40 row is eliminated under
exactly the two existing additional hypotheses: the full quintic
first-symbol divisor is reduced, and the quintic has only rational double
points everywhere. Therefore a hypothetical (5,8) STCI must instead have
a repeated zero of that full divisor or a quintic singularity outside the
ADE class somewhere, possibly away from C. This does not imply that B
is nonreduced. The same cover argument, without reference to C, also
excludes an even set consisting of exactly four exceptional node curves
on a globally ADE quintic resolution.

This is an independently reviewed provisional conditional exclusion.
It does not settle the entire (5,8) problem, establish a mechanism at the
remaining boundary, rerun inherited proofs, or canonically promote a result.
