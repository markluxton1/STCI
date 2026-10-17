# Independent audit of smooth-root formal nonexistence

Date: 2026-10-15. Author: `new_logarithmic_review`.

Status: **PASS: the smooth movement-two nonexistence theorem holds for
every balanced smooth rational space curve of degree e>=4 and every
r>=2, with the stated embedded-Cartier interpretation.** The generalized
numerical criterion and its new quadratic consequence also pass, with
the rational-base and numerical hypotheses retained. Combined with the
accepted finite tower, this gives an existential uniform finite empty
stage for each fixed r on the entire smooth-root open, and the precise
bounded-gap consequence below. It does not exclude all actual complete
intersections in that open.

The target is the live
[formal-nonexistence note](2026-10-15-generalization-smooth-root-formal-nonexistence.md),
including the clarification of connectedness, the whole-curve gluing
argument, the direct plane-adjunction argument, and equation (3a) added
during review. This audit inspected the primary algebraicity and
high-self-intersection sources. Accepted root-functor, finite-tower,
actual-CI bridge, and prior CAS/class computations are premises and were
not replayed. The existing
[focused branch/ruled review](2026-10-15-formal-branch-ruled-model-degree-bound-review.md)
is an input; the additional work here checks the algebraicity hypotheses,
global branch selection, multiplicity/genus passage, all-r numerical
scope, and the finite-cutoff conclusion.

## 1. Exact formal object and the whole smooth root

Throughout, C is a smooth rational curve embedded in P3 over an
algebraically closed field k of characteristic zero. Its balanced normal
bundle is O_(P1)(lambda)^2, with lambda=2e-1 and deg C=e. The accepted
blowup convention gives

    B=Bl_C(P3), E=P1 x P1,
    O_E(-E)=O_E(-lambda,1).

For the general numerical criterion, Z is a smooth connected divisor of
class (epsilon,r), finite over C of degree r. The elementary product
intersection and adjunction formulas give

    g(Z)=(epsilon-1)(r-1),
    deg O_Z(a,b)=a*r+b*epsilon.

For epsilon=2 and r>=2, connectedness and finiteness do not need to be
added as hidden hypotheses to the main theorem. The divisor exact
sequence and Kunneth give H^1(E,O_E(-2,-r))=0, hence H^0(Z,O_Z)=k.
A smooth proper curve with this property is connected, and its smooth
irreducible components cannot meet. Thus it is integral. An integral
curve of class (2,r) is not a fiber of E->C; its proper nonconstant map
to C is finite, of degree r. The generalized criterion retains
connectedness and finiteness explicitly for other classes.

The accepted inverse-limit functor supplies an embedded effective
Cartier formal divisor Vhat in B-hat_E, reducing to exactly Z. Locally
let E=(u), let a lift f cut out Z modulo u, and write its formal
equation as g=f+u a. Smoothness of Z means that f has nonzero
differential on E. Consequently the full completed local ring of Vhat
at every point of Z is k[[t,u]], and u is a regular parameter transverse
to Z. In particular Vhat is a smooth formal surface along its entire
scheme of definition, not only at the generic point of Z.

There is also a needed change-of-completion check. Inside Vhat,

    I_Z O_Vhat=(u,f)O_Vhat=(u)=I_E O_Vhat.

Its exceptional topology is therefore already the induced Z-adic
topology. Completion transitivity gives a closed formal immersion
Vhat -> B-hat_Z, as required by the algebraicity theorem. No global
equation, formal line-bundle descent, or algebraic surface is assumed
at this stage.

The normal line of Z in this formal surface is

    N_(Z/Vhat)=O_Z(E)=O_Z(lambda,-1),
    deg N_(Z/Vhat)=lambda*r-epsilon=nu.                 (A)

Under nu>4g+5 it is ample, since an invertible sheaf on a smooth proper
curve is ample exactly when its degree is positive.

## 2. Primary algebraicity theorem: all hypotheses match

[Bost, Theorem 3.5 and Corollary 3.8, printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27)
apply here with quasiprojective ambient variety, smooth connected
projective center, smooth formal subscheme admitting that center as
scheme of definition, and ample normal bundle. The conclusion is an
algebraic subvariety of the same dimension containing the formal
subscheme along the whole center; the closure is integral. The printed
dimension hypothesis is **at least one**, despite the web extraction's
apparent greater-than-one sign. These geometric results impose no
arithmetic or convergence hypothesis.

Here the data are X=B, center Z, formal dimension two, and the positive
normal line (A). Thus the Zariski closure W is an integral algebraic
surface in B, and Vhat is an embedded formal branch of W along all of Z.
This gives formal containment, not equality with every branch of
W-hat_Z. Other branches and other components of W cap E are allowed.

The directly verified attribution is Bost's geometric algebraicity
theorem, obtained there from Hartshorne's formal-function results.
The proof does not depend on a broader historical attribution.

## 3. Why the selected branch glues on the normalization

The focused review establishes the local normalization/completion
mechanism. Here its input follows from the primary algebraicity
conclusion: B is smooth of dimension three, W is an integral Cartier
surface, and the chosen full completed quotient at every z in Z is a
regular two-dimensional ring. It is consequently a minimal completed
branch. Excellence makes normalization finite and identifies the
completed normal factors with the normalizations of the completed
branches. The selected factor is already regular and normal. See
[Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C2E).

Local factor selection alone should not substitute for the global
argument. That argument is available here. On a normal-domain formal
chart Spf R over an affine Spec A in W, the map A->R is injective:
locally it maps into a minimal completed branch, whose contraction to
the algebraic domain is zero. Map the finite integral closure Abar
first into Frac(R). Its elements are integral over R, so they belong
to R because R is normal. These maps are unique and agree on overlaps.
They define a morphism Vhat->Wnu to the algebraic normalization.

Reducing this morphism modulo the ideal of definition gives a closed
immersion Z->Wnu over the original Z->W. Its image Znu is isomorphic
to Z. At every point of Znu, the full local completion of Wnu is
the regular selected branch. Hence Wnu is regular along Znu. The
lifted closed immersion Vhat->(Wnu)-hat_Znu is an isomorphism: its
coherent kernel is zero after faithfully flat full local completion
at every point of Znu. This proves the whole-curve formal-neighborhood
identification needed below. It does not identify the other branches
of W with this neighborhood.

Bost's printed p. 186 normalization observation concerns point germs.
It is an appropriate illustration of the local mechanism; the unique
normal-ring lift just given supplies the additional whole-curve gluing.

Take a projective resolution T->Wnu preserving this regular open set.
The same smooth curve Z in T then has

    Z^2=nu, genus(Z)=g.                                  (B)

This is the normal-bundle degree of the selected algebraic branch,
unchanged by resolution away from Z.

## 4. Ruled model and numerical degree: correct for general g,nu,h

The exact primary theorem is
[Hartshorne, Theorem 4.1, printed p. 122, with the definition on p. 111](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=13).
For a smooth curve on a smooth proper surface, the strict inequality
Z^2>4g+5 gives equivalence to a section of a geometrically ruled
surface. In this paper equivalence is a birational map that is an
isomorphism on an open neighborhood of the curve. The result applies
for every genus here, and the strict inequality avoids its boundary
exception. It is stronger than merely being birationally ruled.

The algebraic closure W is not E: on Vhat the exceptional parameter u
is nonzero and regular. Let S be its image in P3. It is an integral
surface, and W is its strict transform because B->P3 is an isomorphism
off E. The morphism T->S is birational. If H is the pullback of a
hyperplane and d=deg S, then

    H is nef, H^2=d>0, H.Z=deg O_C(1)*deg(Z->C)=e*r=h.   (C)

No isomorphism from a neighborhood of Z to P3 is used; the map
Z->C usually has degree r. The neighborhood isomorphism used in the
degree argument is the one to the ruled model.

The focused review's intersection argument extends without change
from (g,nu,h)=(1,12,8) to (B)--(C). On a common resolution outside the
curve neighborhoods, push the nef pullback of H to a divisor D on
the ruled surface R. Negative definiteness gives d<=D^2, and D is
nef. Numerically D=a Z0+b f, where a=D.f is a nonnegative integer.
The case a=0 would give D^2=0, so a>=1. From D.Z0=h and Z0^2=nu,

    b=h-a*nu,
    d<=D^2=2ah-nu*a^2.

Thus the generalized upper bound is valid:

    d<=M:=max_(a integer,a>=1)(2ah-nu*a^2).              (D)

The maximum exists because nu>0. If nu>=h, the successive difference
2h-nu*(2a+1) is negative for every a>=1, so M=2h-nu. These conclusions
do not require descending the formal divisor or its line bundle to B.

## 5. Other branches do not weaken the actual multiplicity bound

Let m be the generic I_C-adic order of the equation of S. The strict
transform W is an effective Cartier divisor distinct from E. Its
restriction W|E is therefore an effective Cartier divisor. Over the
generic point of C, the ordinary blowup of the two-dimensional regular
normal local ring shows that W|E has degree m on the exceptional P1.
Equivalently, W is linearly equivalent to dH-mE, whose restriction has
direction degree m.

The crucial containment is embedded, not an abstract identification
with a formal surface. Vhat being a branch of W implies, on reducing
the formal containment modulo u,

    Z subset W|E

scheme-theoretically. On the smooth surface E, this says W|E-Z is
effective. Intersecting with the generic fiber of E->C gives

    m>=r.                                               (E)

Extra branches can contribute additional copies of Z or additional
effective components. They cannot subtract its degree. No equality
W|E=Z or equality m=r has been assumed.

## 6. General planes, integral sections, and the genus inequality

Choose a plane P general in the full dual projective space. Bertini
irreducibility applies to the integral surface S, even if S is
nonnormal. General reducedness follows by applying smooth Bertini
on the dense regular locus; the possible singular-locus intersection
is finite, and a plane hypersurface has no embedded components.
Thus Gamma=S cap P is integral. The relevant primary formulations are
[Stacks, Bertini irreducibility](https://stacks.math.columbia.edu/tag/0G4C)
and [smooth Bertini](https://stacks.math.columbia.edu/tag/0FD4).

The plane may simultaneously meet the smooth C transversely in e
distinct points q_i and avoid the finite complement of the dense open
where the equation of S lies in I_C^m. These are compatible nonempty
open conditions on the plane. At q_i, the restriction of I_C to the
transverse plane is its maximal ideal. Therefore the equation of
Gamma belongs to that maximal ideal to power m, and its actual
plane multiplicity n_i satisfies n_i>=m.

There is no need to assert that these singularities are ordinary.
Blow up P at the e distinct q_i. The integral strict transform of
Gamma has class d l-sum n_i E_i. Adjunction on this smooth plane
blowup gives

    p_a(Gamma')=((d-1)(d-2)-sum n_i(n_i-1))/2.

An integral proper curve has nonnegative arithmetic genus. Hence

    (d-1)(d-2)>=sum n_i(n_i-1)
                 >=e*m*(m-1)>=e*r*(r-1).               (F)

This is an independent proof of the lower bound, with arbitrary
higher contacts and all plane-curve branch types retained.

## 7. Movement two: every r>=2 contradicts (D)--(F)

For epsilon=2 and lambda=2e-1,

    g=r-1, nu=(2e-1)r-2, h=e*r,
    nu-(4g+5)=(2e-5)r-3>0,
    nu-h=(e-1)r-2>0

for e>=4 and r>=2. Thus both algebraicity positivity and the ruled
threshold hold, and (D) gives

    1<=d<=2h-nu=r+2.

For positive integers d<=r+2, (d-1)(d-2)<=r(r+1). Combining with
(F) would give r+1>=e(r-1). But

    e(r-1)-(r+1)=(e-1)r-e-1>=e-3>0.

This contradiction proves the main theorem for every normal order r
in one argument. For e=4,r=2 it specializes to the impossible pair
d<=4 and (d-1)(d-2)>=8, as claimed.

## 8. General numerical criterion and its finite-r corollary

The criterion (D)--(F) passes whenever the smooth rational-base setup,
smooth connected finite root, and nu>4g+5 all hold. For the actual
balanced rational curve in P3, lambda=2e-1. Its threshold is exactly

    (2e+3-4epsilon)r+3epsilon-9>0.

If also (e-1)r>=epsilon, then nu>=h and d<=r+epsilon. Substituting
this upper bound in (F) and expanding gives precisely

    (e-1)r^2-(e+2epsilon-3)r
      -(epsilon-1)(epsilon-2)<=0.                       (G)

For fixed epsilon with 2e-1>4(epsilon-1), the two preceding threshold
conditions hold for all sufficiently large r. The coefficient of r^2
in (G) is positive. Therefore only finitely many first normal orders
can support such a smooth all-orders root. This is a sufficient
structural exclusion; it says nothing about a root failing a threshold
or about singular/nonreduced/disconnected roots. The formula for g
here uses the rational base. It is not asserted for an arbitrary curve
with a balanced normal bundle.

## 9. Uniform finite empty stage and the exact actual-CI gap bound

Fix the actual embedding C subset P3 and r. On the accepted coefficient
open U for (epsilon,r)=(2,r), lambda=2e-1>=7>3epsilon. The
[accepted finite tower](2026-10-15-generalization-uniform-root-tower-finite-determinacy.md)
therefore supplies closed schemes K_m on this single finite-type U,
all-order uniqueness, and a finite index N with K_N=K_(N+1)=... .
Its stable scheme represents compatible formal embedded Cartier ideals.
Let U_sm be its smooth-root open.

The theorem above eliminates every geometric point of K_N cap U_sm.
A nonempty finite-type scheme over k has a geometric point, so

    K_N cap U_sm is the empty scheme.                   (H)

Nilpotents do not evade this conclusion. This N is a uniform finite
failure stage over the entire smooth-root family for the fixed r and
actual embedding. No explicit value, uniformity as r varies, or
emptiness on the singular-root boundary follows.

Finally retain every hypothesis of the accepted actual-CI bridge,
including its smooth actual root, saturated first relation, and jointly
generating leading symbols. If the generic normal initial regular
sequence has degrees (r,s), s>r, its strict ideal is locally
(h,u^(s-r)). With E_m=V(u^(m+1)), it gives the Cartier ideal (h) at
exactly the stages guaranteed by m<s-r. Thus the root lies in
K_(s-r-1). Equation (H) forces

    s-r<=N, equivalently s<=r+N.                        (I)

At equality s-r=N, the bridge only provides stage N-1; it does not
provide stage N. A gap N+1 would provide the empty stage N and is
excluded. This proves the requested existential bound on the actual
bridge gap, while preserving its strict indexing.

The accepted
[functor audit](2026-10-15-generalization-uniform-root-tower-functor-independent-audit.md)
already fixes this indexing and all-order compatibility; those proofs
were not replayed. Finite-gap actual pairs can introduce their second
relation before the empty stage, so (I) is not their exclusion.

## Disposition and remaining scope

The main theorem, the generalized criterion, equation (3a)/(G), and the
finite-cutoff/gap consequences (H)--(I) pass this audit. The owner
incorporated the smooth-root connectedness, whole-curve normalization,
and direct plane-adjunction clarifications during review. These clarify
existing valid steps rather than repair a counterexample.

This result excludes infinite embedded smooth movement-two formal
first-principal-ideal lifts. It gives neither an explicit N nor a claim
that K_1 or K_2 is empty. It does not apply automatically to singular or
nonreduced roots, coefficient base points, unsaturated first relations,
or actual complete intersections outside the accepted bridge. It does
not settle the unrestricted C0 or universal STCI problem.

No accepted verifier, first/second class computation, or CAS elimination
was replayed. No commit or memory write was performed.
