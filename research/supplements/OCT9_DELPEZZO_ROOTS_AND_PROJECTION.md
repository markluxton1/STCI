# October 9 historical mathematics

Full original source text preserved. Hypotheses, counterexamples, unsuccessful arguments, and open questions retain their source status; no new independent audit or theorem promotion.

---

## Source: 2026-10-09-session-A3-two-A1-projection-family.md

# A uniformly excluded A3+2A1 family containing fixed C0

Date: 2026-10-09. Author: `normal_global_adversarial`.
Status: **PROVED HERE for the displayed family**, characteristic zero.
Every member below is an integral quartic containing fixed C0 with
normalization singularity type A3+2A1, and admits no mate of any degree.
The family does not exhaust every pair or middle-coordinate projection
in this ADE stratum. No canonical frontier file is edited.

## 1. The normal anticanonical model

In P4[a:b:c:d:e], let

    S=V(ab-c^2, cd-e^2).

The two equations form a complete intersection. On c nonzero it is
integral: a,b are nonzero, b=c^2/a and d=e^2/c. The closed set c=0
has also e=0 and ab=0, and has affine-cone dimension two, smaller
than the three-dimensional complete intersection. Thus no component
is contained there. The complete intersection has no embedded
components and is generically reduced, so its ring is a domain.

The Jacobian drops rank exactly at the three coordinate vertices a,b,d.
On the a chart the local equation is cd=e^2, an A1 point; the b chart
is identical. On d=1, eliminate c=e^2 and obtain ab=e^4, an A3 point.
All singularities are isolated, so the complete intersection is normal
by S2 and R1. Its degree is four and its dualizing sheaf is O_S(-1).

## 2. A rational normal quartic and the actual coordinate change

Choose parameters alpha,beta,gamma,delta with

    gamma delta Delta nonzero,       Delta=alpha delta-beta gamma.

Set D0=gamma s+delta t and N0=alpha s+beta t. The five binary quartics

    a=s^2 D0^2,       b=t^2 D0^2,       c=st D0^2,
    d=st N0^2,        e=-st D0 N0

satisfy both equations of S. Their coefficient matrix in the basis
(s^4,s^3t,s^2t^2,st^3,t^4) has determinant

    gamma^2 delta^2 Delta^3.

It is invertible, so the curve is a rational normal quartic. Explicitly
the projective coordinate change from Y0,...,Y4 is

    a=gamma^2 Y0+2gamma delta Y1+delta^2 Y2,
    b=gamma^2 Y2+2gamma delta Y3+delta^2 Y4,
    c=gamma^2 Y1+2gamma delta Y2+delta^2 Y3,
    d=alpha^2 Y1+2alpha beta Y2+beta^2 Y3,
    e=-alpha gamma Y1-(alpha delta+beta gamma)Y2-beta delta Y3.

At t=0 the curve meets the a A1 vertex, at s=0 the b A1 vertex, and
at D0=0 it meets the d A3 vertex. These are three distinct parameters
by gamma delta Delta nonzero. Deleting Y2 projects the curve to exactly

    C0=[s^4:s^3t:st^3:t^4].

## 3. Finite birational quartic projection and every extra fiber

Let p be the projection center Y2. In the a,b,c,d,e coordinates,

    p=(delta^2,gamma^2,2gamma delta,2alpha beta,-M),
    M=alpha delta+beta gamma.

For Q1=ab-c^2 and Q2=cd-e^2,

    Q1(p)=-3gamma^2 delta^2,       Q2(p)=-Delta^2.

In particular p lies outside S, and the projection is finite. Let
T_i be the derivative of Q_i in the omitted Y2 direction, restricted
to the rational normal quartic. Direct expansion gives

    T1=D0^2(gamma^2 s^2-4gamma delta st+delta^2 t^2),
    T2=-2Delta^2 s^2t^2.

The member Q1(p)Q2-Q2(p)Q1 has zero Y2^2 coefficient and linear
coefficient along the curve

    L_c=Q1(p) T2-Q2(p) T1
       =Delta^2 P4,
    P4=gamma^4 s^4-2gamma^3 delta s^3t
       -2gamma delta^3 st^3+delta^4 t^4.

This is nonzero, so the projection is birational on the nonempty
linear-coefficient open. Its integral image has degree four by the
hyperplane degree formula, and S is its finite normalization.

The endpoint coefficients of P4 are nonzero. Every zero therefore has
st nonzero, where T2 is nonzero. At such a point the projection-line
equations have, besides the displayed curve point, a distinct second
point of S: simultaneous coincidence would require T1=T2=0.
Equivalently, on the line c(s,t)+lambda p the restrictions are

    Q_i=lambda T_i+lambda^2 Q_i(p),

and L_c=0 supplies the common root
lambda=-T2/Q2(p)=-2s^2t^2, which is nonzero. Since the first curve
point projects isomorphically onto C0, this second point lies off it.

In fact P4 has four distinct roots. With r=gamma s/(delta t), its
affine polynomial is r^4-2r^3-2r+1, of discriminant -1728. The
four distinct extra points occur in four distinct fibers. Generic
uniqueness above C0 means no second curve component lies over C0;
these are isolated extra points of the full reduced inverse image.

A pulled-back mate section would have zero support exactly that
inverse image. On the integral surface its nonzero local equations
cannot have isolated zeros, so this is impossible. Every displayed
quartic is excluded for every positive mate degree.

## 4. Scope and exact control

Alpha or beta may be zero; only gamma delta Delta is required nonzero.
The determinant and all projection calculations are universal in these
parameters. They are checked in the independent
[uniform projection checker](../computations/verify_session_genus_one_projection_2026_10_09.py)
and its [JSON record](../scratch/session-genus-one-projection-checks-2026-10-09.json).

This construction binds one three-parameter family of pairs to the
specific deleted-middle-coordinate projection. It does not identify
every admissible projection of an A3+2A1 pair. Parameter changes moving
the three singular passages also transform the projection center;
see the [uniform adversarial note](2026-10-09-session-genus-one-uniform-projection-adversarial.md).
The global C0 problem and the complete A3+2A1 projection stratum remain
open at this record's scope.


---

## Source: 2026-10-09-session-a1-singular-conductor-parity-shield.md

# An A1 point invalidates smooth-conductor valuation parity

Date: 2026-10-09. Author: `singular_local_lift`.
Status: **PROVED HERE**, local/affine only. This is not a projective
mate for the fixed C0 and does not resolve the global STCI problem.
It protects the entire ADE conductor lane against applying the
smooth elliptic-conductor parity proof at an ADE point.

Work over an algebraically closed field of characteristic zero. Put

    B=k[l,x,z]/(x^2+lx-z^2),
    w=lx,
    A=k[l,z,w]/(F),
    F=w^2+l^2w-l^2z^2.

The discriminant of F as a polynomial in w is l^2(l^2+4z^2), which
is nonsquare in k(l,z). Thus A is an integral affine hypersurface
of polynomial degree four. The ring B is a quadric cone with its
only singular point at the origin: the gradient of its equation is
(x,2x+l,-2z). It is Cohen--Macaulay and regular in codimension one,
hence normal, and the nondegenerate quadratic singularity is A1.

The map A->B is finite, since x^2=z^2-w and B=A[x]. It is
birational, since x=w/l in the common fraction field. Normality
therefore makes B exactly the normalization of A.

The actual conductor can be calculated without a support guess.
As an A-module B has generators 1,x and the complete presentation

    [ -w       l(z^2-w) ]
    [  l          -w   ].

To see completeness, first impose the monic relation x^2=z^2-w,
then generate the ideal of lx-w in the free basis 1,x. Its two
coefficient columns are exactly those displayed. The determinant
is F. Modulo the submodule generated by 1 this gives

    B/A=A/(l,w),
    Ann_A(B/A)=(l,w).

Thus the downstairs conductor is the entire smooth affine line
Gamma=Spec k[z], and upstairs its ideal is (l,w)B=(l). The actual
upstairs conductor is

    D=Spec k[x,z]/(x^2-z^2).

It is a node with two branches, passing through the A1 point of B.
The map D->Gamma is finite flat of degree two: its algebra is free
over k[z] with basis 1,x and x^2=z^2. Its global trace involution
fixes z and sends x to -x.

Let c=V_B(x,z). It is a smooth affine line with coordinate l and
passes through the A1 point. Its image is the smooth embedded line
C=V_A(z,w), also with coordinate l, and c->C is an isomorphism.
At the generic point of c, l is a unit and

    x=z^2/(x+l),

so the Weil divisor of Q=x is exactly 2c. There is no other prime
in its zero support because B/(x)=k[l,z]/(z^2).

The curve c is non-Cartier at the origin: the ideal (x,z) has two
independent degree-one generators modulo the maximal ideal times
that ideal. Its local divisor class has exact order two.

On D, the section q=Q|D is anti-invariant under the actual trace
involution. On its two normalized branches x=z and x=-z, its
vanishing order is one in both cases. This does not contradict
div_B(Q)=2c, because c is non-Cartier at the A1 point where D meets
it. A local equation for c whose square represents Q does not
exist there. The smooth-surface parity argument cannot be applied.

Indeed the square does descend and even supplies an affine mate:

    G=z^2-w in A,       pullback G=x^2,
    div_B(pullback G)=4c.

Restricting F to G=0 gives F|w=z^2=z^4. Hence F=G=0 has reduced
support exactly C. The full reduced inverse image of C is c:
in B, z=0 and lx=0 imply x^2=0 and therefore x=0 set-theoretically.
The restricted morphism remains immersive on c, including the A1
point, because its ambient parametrization is (l,z,w)=(t,0,0).

This example verifies all the local issues simultaneously: an actual
finite flat double conductor, its global involution, a smooth lifted
curve with a non-Cartier order-two class, an anti-invariant section
with doubled Weil divisor, and a descended positive power. Therefore
the entire del Pezzo conductor reduction needs a global obstruction
when D meets an ADE point; smooth-conductor parity alone is
insufficient.

The displayed affine line has degree one and its projective
homogenization is not asserted to provide the fixed degree-four
C0 or a projective mate. The computational companion
`computations/verify_a1_singular_conductor_parity_shield_2026_10_09.py`
checks the literal equations, finite relation, resultant, complete
presentation determinant, node factorization, branch orders, and
descended-square identity. The proofs above establish normality,
the actual conductor equality and the divisor claims.

The checker returned exit 0 and `status: PASS` on 2026-10-09.
Its source SHA256 is
`326a5fd0f0d445cb4e51e2c3e53e447529c2c079caca8d45be8ac766d34eacc6`.
The output is
`research/scratch/session-a1-singular-conductor-parity-shield-2026-10-09.json`,
with SHA256
`dd6696a4945b6f6d5b573d6ea6908bfccee7f4e3a6f4959337fd46e83bf7ce3b`.
Normality uses the primary
[Stacks Project Serre criterion](https://stacks.math.columbia.edu/tag/031S).


---

## Source: 2026-10-09-session-delpezzo-D5-root-independent-audit.md

# Root's independent reconstruction of the D5 torsion filter

Date: 2026-10-09. Auditor: root, separate from the construction owner
`delpezzo_d5_torsion_filter`. Status: **PROVED HERE / accepted at the
stated geometric and lattice scopes**. A further worker audit was
interrupted by the weekly usage limit before its final written record;
it is not counted as a completed audit. The argument below and the
separate signed-partition check supply this acceptance.

Audited source: [D5 torsion filter](#source-2026-10-09-session-delpezzo-d5-torsion-filtermd).
The separate [genus-one reduction](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
and [its independent ADE audit](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-rational-genus-one-ade-independent-auditmd)
establish its weak-del-Pezzo/ADE hypotheses for every sectional-genus-one
normalization of an integral nonnormal quartic containing fixed C0.
This audit does not exclude mates in both surviving singularity types.

## 1. The geometric class lies outside the exceptional lattice

On the minimal resolution M, L=-K_M is nef and big with L^2=4.
The hypothetical mate supplies a smooth reduced curve c on S,
isomorphic to C0, with b c~bH. Its strict transform c# is also smooth
P1 and L.c#=4. Adjunction gives c#^2=2. Hence the integral class

    Z=L-c#,       L.Z=0,       Z^2=-2

is a root in the anticanonical orthogonal lattice. Pullback of the
actual effective Cartier divisor b c expresses b Z as a nonnegative
integral combination of exceptional curves, so Z belongs to their
rational span and to its integral saturation. It has Z.E<=0 on each
exceptional prime because c#.E>=0.

The owner correctly retains that c is smooth downstairs, not only
that its abstract strict transform is smooth. If Z were an integral
exceptional combination, the quotient
Cl(S)=Pic(M)/<exceptional curves> would give c~H as Weil divisors.
This makes c Cartier. At a point of c, its regular one-dimensional
quotient local ring, together with one defining equation, gives at
most two generators of the surface maximal ideal. A two-dimensional
surface local ring there must consequently be regular. Thus c avoids
all singular points of S, and c# avoids every exceptional curve.
Then Z.E=0 on the entire exceptional lattice, so its negative-definite
intersection form forces Z=0, contradicting Z^2=-2. Therefore

    Z in sat(R) minus R.

This is the required missing-root condition. It fails if one drops
downstairs smoothness, so the geometric premise is material.

## 2. The entire integral orthogonal lattice is D5

A weak del Pezzo surface of degree four is the blowup of five points
of P2, allowing infinitely near points and using total exceptional
transforms. The primary author-hosted source is
[Dolgachev, Classical Algebraic Geometry, section 8.1.3](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf).
Its definition and ensuing statement after Definition 8.1.18 give
the weak del Pezzo blowup model; the degree rules out F0 and F2
without blowups. The Picard group is free with intersection form
diag(1,-1,-1,-1,-1,-1), and L=3h-sum e_i is primitive of square four.
The orthogonal complement therefore has discriminant four.

The displayed five Picard roots in the owner note have negative
D5 Gram matrix, also of discriminant four. Their lattice consequently
equals the whole integral orthogonal complement. This discriminant
step rules out an unrecorded finite-index enlargement. Dolgachev's
Proposition 8.2.7 gives the same forty roots explicitly; root checked
both primary passages. A geometric effective ADE exceptional basis
generates a reflection-closed root subsystem of this forty-root system.

## 3. Reconstruction by signed connected components

Use the Euclidean pairing and D5={v in Z^5: sum v_i even}, reversing
the geometric intersection sign. For a coordinate-connected root
component, choose a spanning tree and switch signs so its tree roots
are differences u_i-u_j. Their reflections are transpositions along
a connected graph and generate every permutation of that block.
Consequently the subsystem contains all differences on the block.

If every other edge also becomes a difference, the block is A_(m-1)
with rational span sum epsilon_i v_i=0. If an edge becomes a sum,
permuting its coordinates produces all sums as well, giving the full
D_m block. This includes D2=2A1 and D3=A3. No third connected type
can occur in this coordinate-root model.

An integer vector in a balanced A block satisfying its signed-sum
equation belongs to that A root lattice. Its ordinary sum is even,
since signs have no effect modulo two. Each D block spans all its
coordinates rationally and has an independent even-sum condition
in the root lattice. The ambient D5 instead imposes just the total
even sum across all D blocks. With t nonempty D blocks the index
is 2^(t-1) when t>=1, and one when t=0.

A missing ambient root in the rational span cannot lie inside a
block: those roots are already present. If its two coordinates lie
in separate blocks, any balanced block gives a nonzero signed sum,
which excludes rational-span membership. Thus a missing root joins
two D blocks, and conversely every such root violates both separate
parities while satisfying the ambient total parity.

Each D block has at least two coordinates. On five coordinates two
blocks have sizes only (2,2) or (2,3). A further nontrivial block
cannot fit. These are exactly 4A1 and A3+2A1, with saturation D4
and D5 respectively, both index two. This is a direct completeness
proof, independent of the program's enumerated count.

## 4. Chamber, correction and parity

For the effective geometric exceptional roots, the inequalities are
z.alpha_i=-Z.E_i=c#.E_i>=0. In a D2 block with simple roots
u1-u2 and u1+u2, only +u1 among signed coordinate vectors satisfies
both inequalities. In a D3 block with simple roots u1-u2, u2-u3,
u2+u3, only +u1 does so. Therefore a missing root joining the two
blocks has exactly one dominant choice.

For 4A1 it is u1+u3, giving

    Z=(E1+E2+E3+E4)/2,       c#.Ei=1 for all four.

For A3+2A1 it is u1+u4. Here u1-u2 is the middle A3 root; the
other two D3 roots are its ends. This gives

    Z=E_mid+(E_left+E_right+F1+F2)/2,
    (c#.E_mid,c#.E_left,c#.E_right,c#.F1,c#.F2)=(1,0,0,1,1).

All coefficients are nonnegative, as required by the actual divisor
pullback. These corrections are the nonzero order-two classes in
sat(R)/R. Since b Z belongs to R, every hypothetical mate degree b
is even. This does not show that any even degree works.

## 5. Independent finite control and evidence boundary

The owner enumerates reflection closures and checks integer-lattice
membership with Hermite normal form. Root wrote a separate
[signed-partition countercheck](../validation/2026-10-09-D5-root-audit/countercheck.py)
using all 52 set partitions of five coordinates and all balanced
sign assignments or full D blocks. It uses neither reflection
closure nor Hermite normal form. It obtains the same 428 embedded
subsystems and checks rational-span membership and the separate
parities of every one of the forty ambient roots. Exactly fifteen
embeddings are 4A1 and ten are A3+2A1; their missing-root counts
are sixteen and twenty-four. Every other embedding is saturated.

Its terminal isolated execution passed in 0.091 seconds. The frozen
owner source also completed its separate isolated replay with exit
zero in 3.059 seconds. The terminal statuses, source snapshots, logs
and output hashes are in
[replay-manifest.json](../validation/2026-10-09-D5-root-audit/replay-manifest.json).
The written signed-component proof establishes the theorem; these
controls check its finite arithmetic representation. Neither process
remains running.

## 6. Combined accepted conclusion

Combining this lattice proof with the separately audited rationality
and genus-one del Pezzo reductions, every hypothetical quartic mate
for fixed C0 in the normalization sectional-genus-one lane requires
exactly one of the two complete exceptional types above, and an even
mate degree. All other ADE types in that lane are excluded. The
explicit four-A1 family has an additional all-degree exclusion by
full fibers, but other four-A1 projections and A3+2A1 remain OPEN.
Rational genus-two normalizations and higher carrier degrees also
remain OPEN. No unrestricted C0 or universal STCI conclusion follows.


---

## Source: 2026-10-09-session-delpezzo-D5-torsion-filter.md

# The D5 root-saturation filter for degree-four ADE del Pezzo normalizations

Date: 2026-10-09. Owner: `delpezzo_d5_torsion_filter`.
Status: **PROVED HERE, independently accepted within the stated
weak-del-Pezzo/ADE hypotheses**; the exhaustive exact lattice checker
has terminal PASS. The [written independent proof audit](#source-2026-10-09-session-delpezzo-d5-torsion-independent-auditmd)
accepts sections 2--5 without corrections. This note does not classify all sectional-genus-one
normalizations, construct a mate, or resolve the STCI problem.

This follows the [sectional-genus reduction](2026-10-09-session-normalization-sectional-genus-zero.md)
and complements the [explicit four-A1 family](OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-delpezzo-four-a1-familymd).
The latter realizes the first surviving lattice pattern and then excludes
its displayed projections by an additional normalization-fiber argument.
That family is not assumed to exhaust the four-A1 lattice pattern.

## 1. Precisely scoped geometric conclusion

Work over an algebraically closed field of characteristic zero. Suppose
an integral quartic carrier X has finite normalization nu:S->X with
an ample Cartier polarization H=nu*O_X(1), H^2=4. Assume that S has
only ADE singularities and its minimal resolution sigma:M->S satisfies

    L=sigma*H=-K_M.

Thus M is a weak del Pezzo surface of degree four. Let c be the
embedded smooth P1 supplied by a hypothetical mate for the smooth
rational quartic C0, so that

    H.c=4,       div_S(nu*G)=b c ~ b H,

for a positive integer b. The full support and smooth lift are required
geometric inputs; smoothness of an abstract strict transform alone
does not suffice for the argument below.

Let E_1,...,E_r be all exceptional (-2) curves, and let R be the
lattice they generate in Pic(M). Their intersection graph is a
disjoint union of ADE diagrams. Then the complete exceptional type
is necessarily one of

    4A1,       A3+2A1.

In either case b is even. More precisely the unique possible exceptional
correction in the effective chamber is as follows:

| Exceptional type | Correction Z in L=c# + Z | Intersections of c# with exceptional curves |
| --- | --- | --- |
| 4A1 | (E1+E2+E3+E4)/2 | Once with each of the four curves |
| A3+2A1 | E_mid+(E_left+E_right+F1+F2)/2 | Once with the middle A3 curve and each F_i; zero with the A3 ends |

Here the A3 chain is E_left--E_mid--E_right and F1,F2 are its two
disjoint A1 components. All these assertions are necessary conditions.
Neither surviving type is claimed to admit a mate.

## 2. Why an actual mate produces a missing integral root

The strict transform c# is isomorphic to c. Indeed its map to c is
proper and birational and has finite fibers: an integral strict transform
cannot contain a positive-dimensional fiber without being exceptional.
It is therefore finite, and a finite birational map onto the normal
curve c is an isomorphism. In particular c# is a smooth P1.

Adjunction and L.c#=H.c=4 give

    c#^2+K_M.c#=-2,       c#^2=2.

Define the integral Picard class Z=L-c#. Its numerical identities are

    L.Z=0,       Z^2=4+2-2*4=-2.

Pulling back the effective Cartier divisor b c gives

    sigma*(b c)=b c# + sum_i n_i E_i ~ b L,
    n_i>=0.

Consequently b Z belongs to R. The exceptional intersection form is
negative definite; thus the rational exceptional class of Z has the
unique expression sum_i(n_i/b)E_i. Its coefficients are nonnegative,
although the coefficients need not be integral. Moreover

    Z.E_i=-c#.E_i<=0.

The integral class Z therefore lies in the saturation

    sat(R) = (R tensor Q) intersect Pic(M),

has square -2, and is anti-nef on the exceptional curves.

It is essential that Z is **not** in R. Here is the global descent
argument, which also identifies exactly where downstairs smoothness
enters. For a resolution of a normal surface, pushing Weil divisors
down gives the exact quotient

    Cl(S)=Pic(M)/<classes of the exceptional prime curves>.

Surjectivity uses strict transforms; the kernel assertion uses the
common rational function field and the fact that a divisor with
zero pushdown is exceptional. If Z belongs to R, pushing its class
down shows H-c~0 in Cl(S). Thus c is Cartier, since H is Cartier.

An embedded smooth curve which is Cartier through a point P of a
surface forces P to be regular. Locally its ideal is (f), and R_P/(f)
is regular of dimension one. Lifting a generator of its maximal ideal
together with f gives at most two generators of the maximal ideal
of the two-dimensional local ring R_P. Its embedding dimension is
therefore two, so R_P is regular. Consequently c avoids Sing(S).
Its strict transform is then disjoint from every E_i. Since Z lies
in their rational span and Z.E_i=0 for all i, negative definiteness
gives Z=0, contrary to Z^2=-2. This proves Z not in R.

The same argument also shows that c must meet Sing(S), without
assuming that conclusion from the sectional-genus-zero record.
If one retained only c# smooth, the implication Z not in R would be
false: the abstract class c#=L-E for an A1 root has the required
adjunction numbers but Z=E belongs to R; contraction can make its
image singular. That is not the smooth lifted c required by a mate.

## 3. The ambient root lattice, with its signs fixed

A weak degree-four del Pezzo surface has a geometric Picard marking
by the total transforms h,e1,...,e5 from five successive blowups of
P2. Its intersection form and anticanonical class are

    diag(1,-1,-1,-1,-1,-1),       L=3h-e1-e2-e3-e4-e5.

The negative definite lattice L-perp is the D5 root lattice. For
an explicit identification, the five Picard roots

    e1-e2, e2-e3, e3-e4, e4-e5, h-e1-e2-e3

have minus the Gram matrix of the standard Euclidean D5 simple roots

    u1-u2, u2-u3, u3-u4, u4-u5, u4+u5.

Both lattices have discriminant four, so this identifies the entire
integral orthogonal complement, not merely a finite-index sublattice.
Equivalently its forty square-minus-two vectors are precisely

    +/- (ei-ej),       +/- (h-ei-ej-ek).

The standard Euclidean model, with the sign of the pairing reversed
from the geometric intersection form, is

    D5 = {v in Z^5 : sum_i v_i is even},
    Phi(D5) = {+/- u_i +/- u_j : i<j}.

The checker binds these two models by their actual Gram matrices and
all forty roots. No choice of a root-system table is needed for the
saturation proof that follows. The familiar Picard marking and ADE
exceptional-lattice input can be checked in [Dolgachev, Classical
Algebraic Geometry](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf),
sections 8.1.3, 8.2.3 and 8.2.7; section 8.6.3 supplies a consistency
check against the quartic del Pezzo singularity list. The signed-coordinate
saturation argument in sections 4 and 5 is proved directly here.

## 4. All embedded root subsystems by signed coordinate components

Let Psi be the root subsystem generated by a simple ADE basis of R.
It is closed under negation and under reflections in its roots. Form
a graph with vertices the five coordinates: the support of a root
on coordinates i,j supplies an edge, recording the signs of its two
nonzero coefficients. Different connected coordinate components use
disjoint supports and hence are orthogonal. Ignore unused coordinates.

For a connected coordinate component on m vertices, switch coordinate
signs so that the edges of a spanning tree have the form u_i-u_j.
Their reflections are transpositions and generate the permutations
of its m coordinates. Reflection closure therefore contains every
difference +/- (u_i-u_j).

There are exactly two possibilities:

* **Balanced signs.** Every original edge becomes a difference.
  Its entire reflection closure is the A_(m-1) root system of
  differences. In unswitched coordinates its rational span is one
  hyperplane sum_i epsilon_i v_i=0, with epsilon_i in {+1,-1}.
* **Unbalanced signs.** Some original edge becomes u_i+u_j up to
  overall sign. Permuting coordinates now gives every sum root as
  well as every difference. The reflection closure is D_m, and its
  rational span is the whole coordinate block. Its integral root
  lattice consists of integer vectors with even coordinate sum.

This includes the small cases D2=2A1 and D3=A3. In particular two
orthogonal A1 components can share the same pair of coordinates;
grouping by coordinate connectivity handles this case correctly.
The sign switching is an ambient lattice isometry, since changing
coordinate signs preserves the even-sum condition. Only a lattice
classification is asserted here; no extra claim about Weyl orbits
of geometric markings is needed.

For a balanced block, an integer vector satisfying its signed-sum
equation belongs to its A lattice. Its ordinary coordinate sum is
even, because signed and ordinary sums agree modulo two. A D block
has no linear equation but imposes its own even-sum constraint in R.
Thus, if the number of D blocks is t, the saturation in D5 replaces
their t separate parity constraints by their single total parity
constraint. It follows that

    [sat(R):R] = 1 if t=0,
    [sat(R):R] = 2^(t-1) if t>=1.

There is a particularly direct root-level version. A root in the
rational span of R is either supported within one coordinate block,
or joins two blocks. Roots inside a balanced block are precisely
its signed differences; roots inside a D block are already its D
roots. A cross-block root has a nonzero signed sum in any balanced
block it touches, so cannot lie in that block's rational span. It
can therefore be a missing root only if it joins two D blocks.
Conversely every root joining two D blocks is in sat(R) and violates
both separate parities, so is outside R.

Every D block uses at least two coordinates. With five coordinates,
two such blocks can only have sizes

    (2,2),       (2,3).

There is no room for another root block in either case. These are
exactly

    R=4A1,       sat(R)=D4,       index two;
    R=A3+2A1,   sat(R)=D5,       index two.

The first case has sixteen missing roots, the second twenty-four.
All other embedded ADE root sublattices of D5 are saturated. This
proves the proposed filter, including its completeness, without
assuming that a computational sample exhausted embeddings.

## 5. The effective chambers determine the corrections uniquely

The positive Euclidean model has z.alpha_i=-Z.E_i=c#.E_i>=0 for
the effective simple roots alpha_i. This fixes the chamber.

For 4A1 choose

    alpha1=u1-u2, alpha2=u1+u2,
    alpha3=u3-u4, alpha4=u3+u4.

The missing roots join {1,2} to {3,4}. The inequalities on alpha1
and alpha2 permit only +u1 in the first block, and the inequalities
on alpha3 and alpha4 permit only +u3 in the second. Hence the unique
missing root in this chamber is

    z=u1+u3=(alpha1+alpha2+alpha3+alpha4)/2.

Its scalar product with each simple root is one. Translating back
gives the first row of section 1.

For A3+2A1 choose

    alpha1=u1-u2, alpha2=u2-u3, alpha3=u2+u3,
    alpha4=u4-u5, alpha5=u4+u5.

Here alpha1 is the middle of the A3 chain, with ends alpha2 and
alpha3. A missing root joins {1,2,3} to {4,5}. Chamber inequalities
force +u1 and +u4 respectively, so its unique value is

    z=u1+u4=alpha1+(alpha2+alpha3+alpha4+alpha5)/2.

Its scalar products with the five simple roots are (1,0,0,1,1).
This gives the second row of section 1. Other choices of simple
roots are carried to these by changing the chamber inside each
root subsystem; the uniqueness statement is relative to the actual
effective exceptional basis.

In both cases Z represents the nonzero order-two coset in sat(R)/R.
Since b Z belongs to R, b is necessarily even. This also describes
the order-two exceptional correction at every singularity met by
c: all four A1 points in the first case, or the A3 middle and the two
A1 points in the second. The zero intersections with the A3 end
curves follow numerically and are not extra geometric assumptions.

## 6. Exact exhaustive control and provenance

The standalone [checker](../../computations/verify_delpezzo_D5_torsion_filter_2026_10_09.py)
constructs the forty roots, precomputes their exact integer reflections,
and enumerates every embedded reflection-closed subsystem by adding
one root and taking reflection closure, starting from the empty
subsystem. Completeness follows inductively: any subsystem can be
generated by its roots in a finite sequence, and every intermediate
closure is contained in it. It obtains **428** embedded subsystems.

For each one, it independently takes the Hermite normal form of the
matrix of all its roots. Rational orthogonal projection and integral
coordinates in that integer-lattice basis determine the ambient roots
in its rational span and in its integral lattice. These results are
then compared with the signed-block classification. Gcds of maximal
minors check the saturation index, with the ambient D5 even-sum
condition retained. The computation verifies all 428 cases, not just
one representative per abstract ADE type, and verifies both chamber
formulas.

The only nonprimitive embedded subsystems are the fifteen 4A1
embeddings and the ten A3+2A1 embeddings. Their indices are two and
their missing-root counts are sixteen and twenty-four respectively.
The source run completed with terminal exit zero and PASS; its exact
source SHA256 is

    fdbb9bdddd0c7b6b20140835662b3526ba800aa814d3d71c5de91085097e3a7e

The [JSON report](../scratch/session-delpezzo-D5-torsion-filter-2026-10-09.json)
preserves all type counts, the lattice profiles, both root bases,
both correction vectors and their intersections. It explicitly records
that the checker does not classify all sectional-genus-one normalizations
and does not claim to settle STCI.

One preliminary enumeration reconstructed the same 428 reflection-closed
subsystems before the checker was written. No mathematical conjecture
in the scoped filter failed. An initial independent auditor confirmed
the signed-coordinate classification and highlighted the necessary
downstairs smoothness in section 2, then hit the account usage limit
before saving a final audit note. Its message is a useful audit lead,
not a completed independent acceptance record. The verification owner's
[bounded written audit](#source-2026-10-09-session-delpezzo-d5-torsion-independent-auditmd)
subsequently accepted the frozen proof without corrections. The present
revision changes only this acceptance status and its links; the audited
mathematical statements and checker source are unchanged.

## 7. Continuation boundary

The filter excludes every other exceptional ADE configuration under
the exact polarization L=-K_M. It leaves two concrete torsion patterns,
and restricts any mate degree there to even integers. The existing
four-A1 projection family meets the first pattern but its displayed
members fail full inverse support. Whether another projection of a
four-A1 pair, or a pair of type A3+2A1, can satisfy all mate conditions
is not resolved here.

No implication from arbitrary pi=1 normalizations to this weak degree-four
del Pezzo/ADE model has been used in the lattice proof. The separately
accepted [genus-one model-coverage theorem](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
now supplies those hypotheses for rational genus-one quartic normalizations
containing C0; combining the two theorems is justified by that separate
record. Sectional genus two, higher carrier degrees,
other normalizations, and the universal STCI question remain outside
this note's conclusion. No canonical frontier file has been edited
by this owner.


---

## Source: 2026-10-09-session-delpezzo-D5-torsion-independent-audit.md

# Independent proof audit of the D5 missing-root filter

Date: 2026-10-09. Auditor: `verification`. Status: **ACCEPTED / PROVED HERE**, with the weak degree-four del Pezzo and ADE hypotheses stated below. This is a proof audit, not a duplicate run of the exhaustive lattice checker.

The frozen owner note [D5 torsion filter](#source-2026-10-09-session-delpezzo-d5-torsion-filtermd) was read in full at SHA256 `b4f4e4bb5a44c01022ce0e7d342bb1ce74127d0d3575aa227b3a18050e5d5919`. Its checker source, read/hash bound but not rerun here, is `computations/verify_delpezzo_D5_torsion_filter_2026_10_09.py`, SHA256 `fdbb9bdddd0c7b6b20140835662b3526ba800aa814d3d71c5de91085097e3a7e`.

## Exact accepted scope

Let S be an ADE normal surface with ample Cartier H of square four. Its minimal resolution sigma:M->S is assumed to satisfy L=sigma^*H=-K_M, so M is a weak del Pezzo surface of degree four. A mate supplies an embedded smooth c=P1 with H.c=4 and b c~b H. Let R be the lattice of all exceptional prime curves. Then necessarily

    R has type 4A1 or A3+2A1,
    [sat(R):R]=2,
    b is even.

The anti-nef correction Z=L-c# is respectively half the sum of the four A1 curves, or the middle A3 curve plus half its two ends and half the two isolated A1 curves. These are necessary conditions only. The theorem does not assert that either type admits a mate. Coverage of other normalization hypotheses is a separate theorem and is not proved by the lattice filter.

## Missing integral root and the essential downstairs smoothness

The map from the integral strict transform c# to the smooth curve c is proper birational with finite fibers, hence finite and therefore an isomorphism. Adjunction gives (c#)^2=2. Thus Z=L-c# is an integral class with L.Z=0 and Z^2=-2. Pulling back the effective Cartier divisor b c shows bZ is an effective integral exceptional divisor; in particular Z is in sat(R), its rational exceptional coefficients are nonnegative, and Z.E_i=-c#.E_i<=0.

The proof that Z is outside R is correct and substantive. Pushdown of Weil divisors gives Cl(S)=Pic(M)/R. If Z were in R, c would be linearly equivalent to the Cartier H and hence itself Cartier. At a point of c, quotienting the two-dimensional surface local ring by its Cartier equation gives the regular one-dimensional ring of the embedded smooth curve. A lift of its parameter together with that equation generates the surface maximal ideal, so the surface local ring is regular. Thus c avoids Sing(S), its strict transform is disjoint from all exceptional curves, and Z is orthogonal to R. Negative definiteness then forces Z=0, contrary to its square minus two. Smoothness of c# alone would not justify this conclusion.

The standard degree-four weak del Pezzo Picard marking identifies L-perp with the negative D5 lattice. The displayed five Picard roots have exactly the claimed Gram matrix; the primitive anticanonical class has square four, so its orthogonal complement has discriminant four. The root basis therefore gives the entire lattice, rather than a proper finite-index copy. Switching to positive pairing makes z a norm-two root in D5 outside R but inside its rational span.

## Signed-coordinate completeness, without computational exhaustion

In the model D5={v in Z^5:sum v_i even}, every root has exactly two nonzero coordinates. Form the signed support graph of the reflection-closed root system generated by R. On each connected block, switch signs so a spanning tree consists of differences. Their reflections generate all coordinate permutations in that block, hence all differences.

If all edges become differences, the block is A_(m-1), with rational span the signed-sum-zero hyperplane and integral lattice all integer vectors in that hyperplane. If any sum edge remains, permutation closure gives all sums as well, so the block is D_m with full rational coordinate span and an even-sum integral lattice. This includes D2=2A1 and D3=A3. Distinct coordinate blocks are orthogonal. Sign switching preserves the ambient even-sum lattice, so it does not change the saturation question.

A root supported inside one block is already in its root lattice. A root meeting a balanced A block in just one coordinate cannot satisfy that block's span equation. Therefore a missing norm-two root must join two D blocks. Conversely such a root belongs to the rational span and to D5 but violates each block's separate even-sum constraint, so is missing. Two D blocks each require at least two coordinates. The budget five permits only sizes (2,2) and (2,3), with no further nontrivial root block. These give exactly 4A1 and A3+2A1.

Their saturation replaces two separate parity constraints with the one total parity constraint; the index is two. This independently proves both completeness and the index claim. It also proves the stronger assertion in the owner note that every other embedded ADE root sublattice is saturated. The owner's enumeration of 428 reflection-closed subsystems is supporting exact evidence, not the proof of exhaustion used here.

## Chamber corrections and mate parity

For 4A1 take roots u1-u2,u1+u2,u3-u4,u3+u4. A missing root joins the two pairs. Nonnegative pairing with all four simple roots forces it to be u1+u3, half the sum of those four roots. Its pairings are all one.

For A3+2A1 take u1-u2,u2-u3,u2+u3,u4-u5,u4+u5. The first root is the middle A3 curve. A missing root joins the two blocks, and nonnegative simple-root pairings force u1+u4. Its coefficients are (1,1/2,1/2,1/2,1/2) and its pairings are (1,0,0,1,1). Translating back to negative geometric pairing gives exactly the owner correction and intersection tables. Choosing the actual effective simple basis fixes the chamber; no additional geometric Weyl-orbit claim is needed.

In either case the correction is the nonzero coset of the index-two saturation quotient. Since bZ is in R, b must be even. The conclusion survives this independent audit with no correction to the frozen proof.

No canonical frontier file was changed and no new mathematical computation was run for this bounded audit.


---

## Source: 2026-10-09-session-delpezzo-entire-conductor-independent-audit.md

# Independent audit: the entire ADE del Pezzo conductor

**Accepted as a conditional structural theorem in characteristic zero.**
The audited proof is
[2026-10-09-session-delpezzo-entire-conductor.md](#source-2026-10-09-session-delpezzo-entire-conductormd).
No canonical files were edited and no additional agents were used.

The hypotheses are a finite normalization `nu:S -> X` of an integral quartic
surface in `P3`, with `S` a rational normal degree-four del Pezzo surface
having only ADE singularities, and
`H=nu^*O_X(1)=-K_S` ample Cartier, `H^2=4`. Every conductor scheme mentioned
below is the actual scheme defined by the conductor ideal, including its
nilpotents.

**Canonical modules and the actual Cartier conductor.** The Gorenstein
quartic has `omega_X` isomorphic to `O_X`. After choosing this trivialization,
finite absolute duality identifies `nu_*omega_S` with
`Hom_OX(nu_*O_S,O_X)`, compatibly with the normalization algebra action.
Locally every such homomorphism is multiplication by a fraction `r`; the
condition `1 in B` forces `r in A`, and its defining condition is precisely
`rB subset A`. This is the actual conductor ideal `I`, which is also an ideal
of `B` and satisfies `IB=I`. Since `omega_S=O_S(-H)` is invertible, its
embedding in `O_S` defines an effective Cartier divisor `D~H`, including at
ADE points. Here `I O_S` means the extended ideal, not an assertion that the
unmodified tensor pullback has no torsion.

**Vanishing and arithmetic Cohen--Macaulayness.** On the crepant rational
resolution `mu:M -> S`, put `A_M=mu^*H`. It is nef and big and
`K_M=-A_M`. For every `n>=0`, Kawamata--Viehweg vanishing applies to
`nA_M=K_M+(n+1)A_M`. Rational resolution and projection formula transfer the
vanishing to `S`. Gorenstein Serre duality transfers it to every negative
integer as well, giving `H1(S,O_S(nH))=0` for all integers `n`. The proof uses
the standard characteristic-zero vanishing theorem; this audit does not
claim a newly verified publisher full-text source.

The preimage ideal sequence
`0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0` is exact for the actual
conductor. Vanishing of both intermediate line-bundle cohomology groups on
`P3` therefore gives `H1(P3,J_Gamma(m))=0` for every integer `m`.

**Purity and classification of the entire downstairs scheme.** The
normalization and its canonical module are maximal Cohen--Macaulay over the
local hypersurface ring: parameters from that ring remain parameters at the
finite normalization points. Hence `I` has depth two at each closed point of
`X`. The depth lemma for `0 -> I -> O_X -> O_Gamma -> 0` forces every nonzero
conductor quotient at a closed point to have depth at least one. Its
dimension is at most one, so there are no embedded or isolated
zero-dimensional components. The Hilbert polynomial computed below ensures
that the curve is nonempty. Thus `Gamma` is pure Cohen--Macaulay, and the
all-twist ideal vanishing makes its saturated coordinate ring ACM.

Riemann--Roch on the rational resolution gives
`chi(O_S(nH))=1+2n(n+1)`. Consequently
`chi(O_Gamma(m))=(2m^2+2)-(1+2(m-1)m)=2m+1`. An Artinian reduction of the
ACM coordinate ring has a nonnegative Hilbert function with sum two and
weighted sum one, hence exactly `h=(1,1)`. Its degree-one coordinate piece
has dimension three, so precisely one independent plane equation belongs
to the ideal. Within that plane its coordinate ring is Cohen--Macaulay of
codimension one in a polynomial ring of dimension three. Auslander--Buchsbaum
makes its ideal a free graded rank-one module, hence principal; the Hilbert
series gives a degree-two generator. Therefore the actual saturated ideal is
a complete intersection `(ell,Q2)`. This proves that `Gamma` is a smooth
conic, two meeting distinct lines, or the plane double-line scheme, rather
than a classification merely of its reduced support. Adjunction gives
`omega_Gamma=O_Gamma(-1)`.

**Duality and finite flatness on the entire schemes.** Over a Gorenstein
local surface ring `A`, MCM duality gives
`I=Hom_A(B,A)`, `Hom_A(I,A)=B`, and the requisite positive Ext vanishing.
Applying the dual to `0 -> I -> A -> A/I -> 0` identifies the natural
quotient `B/A` with the codimension-one canonical module. Globalizing gives
`nu_*O_S/O_X=omega_Gamma` (with the fixed trivialization of `omega_X`). Since
`I` is the same ideal in both rings, quotienting by it gives

\[
0\longrightarrow O_\Gamma\longrightarrow p_*O_D
\longrightarrow \omega_\Gamma\longrightarrow0.
\]

The right-hand module is invertible, so this sequence splits locally as
modules even at a nodal or nonreduced point. Its middle module is locally
free of rank two. The finite morphism `p` is therefore finite flat of degree
two without assuming reducedness or smoothness of either conductor scheme.

**The trace involution includes nilpotents.** Trace of multiplication by
`1` is two, so in characteristic zero the algebra has the canonical module
decomposition `p_*O_D=O_Gamma direct_sum N`, with
`N=ker(trace)` isomorphic to `omega_Gamma`. For a local generator `z` of
`N`, Cayley--Hamilton makes `z^2` a scalar in `O_Gamma`. Thus the map fixing
the scalar algebra and negating `N` is an algebra involution; changes of
trace-zero generator show that these local maps glue. This calculation is
valid over arbitrary nonreduced base rings. Its invariant algebra is exactly
`O_Gamma` because two is invertible.

**Upstairs data and the surviving boundary.** Cartier adjunction gives
`omega_D=O_D`. The all-twist vanishing applied to
`0 -> O_S(-H) -> O_S -> O_D -> 0` gives `H0(D,O_D)=k`, hence connectedness.
Its Hilbert polynomial is `4m`, so its arithmetic genus is one. These facts
do not imply that `D` is reduced, smooth, or disjoint from the ADE points.
The earlier ramification-parity argument for a smooth elliptic conductor
cannot be transferred to these singular or nonreduced cases without an
additional proof. The present theorem supplies the full conductor algebra
and involution, but by itself supplies no mate exclusion or quadratic
descent theorem.


---

## Source: 2026-10-09-session-delpezzo-entire-conductor.md

# The entire conductor of a rational ADE degree-four del Pezzo normalization

Date: 2026-10-09. Author: `singular_local_lift`, for
`singular_normalization_next_frontier`.

Status: **PROVED HERE, independently audited**, under the hypotheses in Section 1. This note
concerns the actual conductor schemes, including reducible and
nonreduced cases. It does not assume the upstairs conductor is smooth
or avoids the normalization singularities. No canonical files are
edited, and no mate or universal STCI conclusion follows from this
structural reduction alone.

## 1. Hypotheses and conclusions

Work over an algebraically closed field k of characteristic zero.
Let X be an integral quartic surface in P3, and let nu:S->X be its
finite normalization. Assume S is a rational normal degree-four del
Pezzo surface with only ADE singularities and

    H=nu^*O_X(1)=-K_S,
    H ample and Cartier,       H^2=4.

ADE is used through its precise properties: S is Cohen--Macaulay and
Gorenstein, and its minimal resolution mu:M->S is rational and
crepant, so R^i mu_*O_M=0 for i>0 and K_M=mu^*K_S. No list of ADE
types, including 4A1 or A3+2A1, is required in the proof.

Let I=Ann_OX(nu_*O_S/O_X) be the conductor. Define the actual schemes

    Gamma=V_X(I),       D=V_S(I O_S),       p:D->Gamma.

Then:

1. I O_S is invertible and isomorphic to O_S(-H). Consequently D
   is an effective Cartier divisor with D~H.
2. Gamma is pure Cohen--Macaulay of dimension one and arithmetically
   Cohen--Macaulay in P3, with Hilbert polynomial 2m+1. Its ideal is
   a complete intersection of degrees (1,2). Thus the entire Gamma
   is a plane conic: smooth, two distinct lines, or a double line.
3. There is an exact sequence on Gamma

       0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,

   and omega_Gamma=O_Gamma(-1) is invertible. Therefore p is finite
   flat of degree two, on the entire schemes.
4. Trace gives a canonical global involution sigma of the O_Gamma
   algebra p_*O_D, with decomposition

       p_*O_D = O_Gamma direct_sum N,
       N=ker(trace) isomorphic to omega_Gamma.

   Locally N has a generator z with z^2 in O_Gamma and sigma(z)=-z.
   These statements retain nilpotents when Gamma or D is nonreduced.
5. D is a connected Gorenstein anticanonical curve with
   omega_D=O_D, H^0(D,O_D)=k, and Hilbert polynomial 4m. Its
   arithmetic genus is one. Smoothness and reducedness are not
   asserted.

## 2. Finite absolute duality identifies the actual upstairs conductor

The quartic hypersurface X is Gorenstein with omega_X=O_X. Finite
absolute duality, together with Cohen--Macaulay concentration on
the equal-dimensional schemes, gives

    nu_*omega_S = Hom_OX(nu_*O_S,omega_X).

This is an identity of canonical modules, not a use of relative
duality requiring nu to be flat. Locally write A for the domain of
X, B for its finite birational normalization and K for their common
fraction field. Every A-linear homomorphism B->A is multiplication
by an element r in K, because it becomes multiplication after
tensoring with K. Since 1 belongs to B, such r belongs to A, and

    Hom_A(B,A)={r in A:rB subset A}=I.

This identifies the right side with the actual conductor ideal,
also as a B-module. Since S is Gorenstein and K_S=-H,

    I=nu_*omega_S,
    I O_S=omega_S=O_S(-H)

as B-ideals after using the duality identification. The inclusion
into O_S is a nonzero inclusion of an invertible sheaf into the
structure sheaf of an integral scheme. Its zero scheme is an
effective Cartier divisor D with O_S(-D)=I O_S. Therefore D~H.
This remains valid when D passes through an ADE point.

## 3. All twists have the required H1 vanishing

Put A_M=mu^*H. It is nef and big, and K_M=-A_M by crepancy. For
n>=0,

    n A_M-K_M=(n+1)A_M

is nef and big. Kawamata--Viehweg vanishing on the smooth resolution
therefore gives H^1(M,O_M(n A_M))=0. Rationality of the ADE
resolution and the projection formula identify this group with
H^1(S,O_S(nH)). Thus the latter vanishes for n>=0.

For n<=-1, Serre duality on the projective Gorenstein surface gives

    H^1(S,O_S(nH))^* = H^1(S,O_S((-n-1)H)).

The exponent on the right is nonnegative. Consequently

    H^1(S,O_S(nH))=0       for every integer n.

The exact conductor preimage sequence on P3 is

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0,

where J_Gamma is the ideal sheaf of the actual downstairs scheme.
After twist m, both intermediate cohomology groups H^1 and H^2 of
O_P3(m-4) vanish. The long exact sequence therefore identifies

    H^1(P3,J_Gamma(m)) = H^1(S,O_S((m-1)H)) = 0

for every integer m.

## 4. Purity, the Hilbert polynomial, and the entire plane conic

The conductor I is maximal Cohen--Macaulay as an O_X-module.
Locally this follows from its identification with the canonical
module of the finite Cohen--Macaulay normalization. More explicitly,
a system of parameters of the two-dimensional local ring A is a
system of parameters at all finite normalization points above it;
it is regular on their canonical modules. Hence depth_A(I)=2.
The depth lemma applied to

    0 -> I -> O_X -> O_Gamma -> 0

gives depth at least one for O_Gamma at its closed points. The
conductor is a nonzero rank-one ideal, so its quotient has dimension
at most one. It follows that Gamma is a pure Cohen--Macaulay curve;
there are no embedded or isolated zero-dimensional components.

Riemann--Roch on the rational crepant resolution, and rationality
of the resolution, give for every integer n

    chi(O_S(nH))=1+2n(n+1).

The quartic hypersurface sequence gives

    chi(O_X(m))=2m^2+2.

Using I=nu_*O_S(-H) in the conductor sequence yields

    chi(O_Gamma(m))
      =(2m^2+2)-(1+2(m-1)m)=2m+1.

Thus Gamma has degree two and arithmetic genus zero. The H^1
ideal vanishing from Section 3 makes its saturated homogeneous
coordinate ring Cohen--Macaulay of dimension two.

To retain the scheme classification, take an Artinian reduction
by two general regular linear forms. Its nonnegative Hilbert
function h has h0=1, sum h_i=degree(Gamma)=2, and
sum i h_i=1 from arithmetic genus zero. Thus h=(1,1). The degree-one
piece of the coordinate ring has dimension 2+1=3, so exactly one
linear form belongs to the ideal in P3. Gamma lies in a plane.
In degree two its coordinate ring has dimension five, while that
of the plane has dimension six. Thus a nonzero plane quadratic
equation Q_2 belongs to its ideal. The plane quotient by Q_2 and
Gamma have the identical Hilbert series (1+t)/(1-t)^2. Their graded
surjection is consequently an isomorphism in every degree. This
proves that the entire saturated ideal is

    I_Gamma=(ell,Q_2),       degrees (1,2).

This excludes extra embedded structures. Over k the equation is a
smooth conic, a product of
two distinct linear forms, or a square of a linear form. The double
line here is the actual plane double-line scheme, not an arbitrary
ribbon supported on a line. In every case Gamma is Gorenstein, and
adjunction gives omega_Gamma=O_Gamma(-1).

## 5. The quotient is the dualizing sheaf and forces finite flatness

Work again over a Gorenstein local surface ring A, with B its
normalization and I the conductor. The modules B and I are maximal
Cohen--Macaulay. Duality on that category gives

    I=Hom_A(B,A),       Hom_A(I,A)=B,
    Ext_A^j(B,A)=Ext_A^j(I,A)=0 for j>0.

Apply Hom_A(-,A) to 0->I->A->C->0, where C=A/I. Since A is a domain
and I contains a nonzero element, Hom_A(C,A)=0. The resulting
exact sequence is

    0 -> A -> B -> Ext_A^1(C,A) -> 0.

The last module is the canonical module of the pure codimension-one
Cohen--Macaulay scheme C. Globalizing with omega_X=O_X therefore
gives

    nu_*O_S/O_X = omega_Gamma.

Since the same conductor I is an ideal of both A and B, quotienting
the inclusion A subset B by I gives, on the actual conductor schemes,

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.

The right-hand line bundle is locally free of rank one over every
local ring of Gamma, including a node or a double-line point. The
sequence therefore splits as a sequence of modules locally: a
generator of omega_Gamma lifts, and the resulting middle module is
free of rank two. Because p is finite, this proves that p is finite
flat of degree two. No smoothness, generic reducedness or separate
flatness assertion has been inserted here.

## 6. Trace constructs an involution on the entire algebra

Let E=p_*O_D. It is a locally free O_Gamma algebra of rank two.
The trace of multiplication satisfies trace(1)=2. In characteristic
zero this gives the canonical splitting

    E=O_Gamma direct_sum N,       N=ker(trace).

The line bundle N maps isomorphically onto E/O_Gamma=omega_Gamma.
Locally choose a generator z of N. Its rank-two multiplication
matrix has trace zero. Cayley--Hamilton gives

    z^2=-det(multiplication_by_z) in O_Gamma.

Thus the O_Gamma-linear map fixing 1 and sending z to -z is an
algebra automorphism. It squares to the identity and is independent
of the trace-zero generator, so these maps glue to a global
involution sigma. Its invariant algebra is O_Gamma, and its
anti-invariant module is N=omega_Gamma.

These are statements about all sections of the entire schemes.
They remain true if the base conic is a double line, if D is
nonreduced, or if the local algebra has equation z^2=0. No branch
point, function-field sign ratio or decomposition into reduced
components is required to construct sigma.

For the later quadratic descent calculation, this gives an exact
description of the entire restriction space. Since O_D(H)=p^*O_Gamma(1),
the invariant and anti-invariant summands of p_*O_D(2H) are

    O_Gamma(2),       omega_Gamma tensor O_Gamma(2)=O_Gamma(1).

Their spaces of global sections have dimensions five and three,
respectively, for every plane conic scheme classified above. In a
local trace-zero generator, a quadratic restriction can be written
a+z h, with a an invariant degree-two section and h a degree-one
section in the anti-invariant summand. It descends exactly when the
entire anti-invariant component is zero. This is a full module
statement even for a double line, not a test at generic points.
The multiplication N tensor N->O_Gamma is equivalently a global
section of omega_Gamma^(-2)=O_Gamma(2), including when that section
defines a nonreduced or singular upstairs curve.

## 7. Upstairs arithmetic data and limits of this reduction

Since D is Cartier and S is Gorenstein,

    omega_D=(omega_S tensor O_S(D))|D=O_D.

The sequence 0->O_S(-H)->O_S->O_D->0, together with the all-twist
H^1 vanishing and H^0(S,O_S(-H))=0, gives H^0(D,O_D)=k. Thus D
is connected. Its Hilbert polynomial is

    chi(O_D(mH))
      =chi(O_S(mH))-chi(O_S((m-1)H))=4m.

In particular its arithmetic genus is one. The same formula follows
from p_*O_D=O_Gamma direct_sum omega_Gamma and chi(O_Gamma(m))=2m+1,
which provides an independent consistency check of the twists.

The structural reduction leaves the following possibilities in
scope: D may pass through an ADE point, have singularities, split
into components, or be nonreduced; Gamma may be two lines or a
double line. It supplies the global trace involution in all of those
cases. It does not by itself show that a section Q with divisor
2c is invariant under that involution, nor that such a section
descends to X. Arguments using a smooth elliptic conductor or a
simple ramification parameter must separately justify those
hypotheses before being applied to the entire lane.

## 8. Primary inputs and provenance

The independent scheme-theoretic audit is saved in
`research/notes/2026-10-09-session-delpezzo-entire-conductor-independent-audit.md`.
It accepts the canonical-module identifications, entire conic scheme
classification, finite flatness and trace involution, while retaining
the singular/nonreduced-D descent boundary. Independent agreement is
audit evidence; the proof is the argument above.

Finite absolute duality is the
[Stacks Project finite-ring dualizing lemma](https://stacks.math.columbia.edu/tag/0AX0),
combined with
[Cohen--Macaulay concentration](https://stacks.math.columbia.edu/tag/0AWQ).
The local conductor identification and the maximal-Cohen--Macaulay
dual sequence are written out above. The projective-space
cohomology vanishing is the
[Stacks Project computation](https://stacks.math.columbia.edu/tag/01XS).

The vanishing input is the standard characteristic-zero
Kawamata--Viehweg theorem, used on the smooth resolution with
(n+1)mu^*H nef and big. Its original primary reference is
[Kawamata, Mathematische Annalen 261 (1982), 43--46](https://link.springer.com/article/10.1007/BF01456407).
The publisher's bibliographic record was freshly inspected; its
full text is subscription-only. The author-hosted link to Viehweg's
1982 paper returned HTTP 410. No fresh full-text verification of
those original vanishing papers is claimed. The use and hypotheses
of the standard vanishing theorem are explicit in Section 3.

No symbolic test is used as a substitute for these scheme-theoretic
proofs. No classification or novelty claim is made.


---

## Source: 2026-10-09-session-dp4-projection-independent-audit.md

# Independent audit: singular degree-four del Pezzo projection

**PROVED for this carrier, in characteristic zero:** the integral quartic
surface described below contains the fixed smooth rational quartic `C0`, but
has no set-theoretic mate of any degree. This is a carrier exclusion, not a
resolution of the unrestricted `C0` or universal STCI problem.

## The normalization and projected image

Use coordinates `[r:p:z:q:t]` on `P4` and set

\[
Q_1=pq-z^2,\quad L=r-3p-6q+4t,
\]

\[
D=-p^2-2pq+6pt-4q^2+3qr+2rt,
\qquad Q_2=7Q_1+D+Lz.
\]

Let `S=V(Q1,Q2)`. The following independently reconstructed linear change
has determinant `2`, with the rows ordered as `a,b,c,d,e` and the original
columns as `r,p,z,q,t`:

\[
a=p+q+2z,\quad b=r+3p+2z,\quad c=p+2q+3z,
\]

\[
d=3q+2t+z,\qquad e=p+4q+4z.
\]

It gives the literal identities

\[
ae-c^2=Q_1,\qquad bd-c^2=Q_2.
\]

The affine cone on this intersection is integral. Its open set `c != 0` is
integral, while the set `c=0` has dimension two, too small to contain a
component of the three-dimensional complete intersection. The complete
intersection is generically reduced and has no embedded components. Its
singular locus consists of the four coordinate axes `a,b,d,e`; this has
codimension two. Thus the cone, and consequently `S`, is normal by `S2` and
`R1`. On `S` the corresponding four vertices have local equations of type
`xy-z^2=0`, hence are `A1` singularities.

The projection center `[0:0:1:0:0]` does not lie on `S` since `Q1=-1` there.
Deleting `z` therefore gives a finite morphism to `P3[r:p:q:t]`; algebraically
finiteness also follows from the monic equation `z^2=pq`. On `L != 0` its
inverse is `z=-D/L`, proving birationality. The image is the integral quartic

\[
X=V(F),\qquad F=D^2-pqL^2.
\]

To justify irreducibility without assuming it: the image is an integral
surface, the projection is birational, and its hyperplane pullback is the
hyperplane class on the degree-four complete intersection `S`. The image
therefore has degree four. Its prime equation divides the nonzero quartic
`F`, so it equals `F` up to scalar. The finite birational map from the normal
`S` is the normalization of `X`.

## Exact conductor calculation

Let `A=k[r,p,q,t]/(F)` and
`B=k[r,p,z,q,t]/(Q1,Q2)`. As an `A`-module, `B` is generated by `1,z`, with
relations given by the columns of

\[
\begin{pmatrix}D&pqL\\L&D\end{pmatrix}.
\]

Indeed, reducing modulo `z^2-pq` leaves the free module with generators
`1,z`; the remaining relation `D+Lz` and its multiple by `z` generate all
relations. The determinant is `F`, consistent with the image equation.
Quotienting by the embedded copy of `A` yields the exact graded formula

\[
B/A\simeq (A/(L,D))(-1).
\]

Consequently the conductor is exactly
`Ann_A(B/A)=(L,D)`. Its projective sheaf is the actual downstairs conductor,
not merely a candidate support ideal.

## Full inverse-image support excludes every mate

The rational normal quartic

\[
c:[u:v]\longmapsto [u^4:u^3v:u^2v^2:uv^3:v^4]
\]

lies on `S`. Its projection is exactly
`C0=[u^4:u^3v:uv^3:v^4]`. This restricted projection is an isomorphism:
on the chart `r != 0`, `p/r=v/u`, and near the opposite endpoint `q/t=u/v`.
These provide local inverses, including at both endpoints.

Along this curve,

\[
L|_c=(u^2-4uv+2v^2)(u^2+uv+2v^2),\qquad D|_c=-u^2v^2 L|_c.
\]

The two affine quadratic factors have discriminants `8` and `-7`, and
resultant `50`. They therefore have four distinct roots in characteristic
zero, none with `uv=0`. Above any one of the corresponding points of `C0`,
`L=D=0`, and the normalization fiber consists of the two distinct points

\[
z=\pm u^2v^2.
\]

Only the positive-sign point lies on `c`, because `c -> C0` is an
isomorphism. The negative-sign point cannot belong to a second curve in the
inverse-image support: a finite morphism maps every curve over `C0`
surjectively onto `C0`, whereas the inverse over its generic point is unique
and lies on `c` (`L != 0` there). Thus each negative-sign point is genuinely
isolated in `nu^{-1}(C0)`; it is not just an additional point on a hidden
component. The support is `c` together with these four isolated points.

Suppose a homogeneous mate `G` satisfied `V(F,G)=C0` set-theoretically.
Its pullback is a nonzero section of an invertible sheaf on the integral
surface `S`, with zero support exactly `nu^{-1}(C0)`. The section is nonzero
since a mate cannot vanish identically on `X`. Its zero scheme is an
effective Cartier divisor, whose support cannot have an isolated closed
point on a surface. The four isolated normalization points contradict that
requirement. Hence this `F` has no mate in any degree.

This identifies a necessary hypothesis in any argument that writes
`nu^*G` as a power of an equation for the lifted curve: the full inverse-image
support must be checked first. Smoothness and an isomorphism `c -> C0`
alone do not establish that hypothesis.

The coordinate-change identities, both substitutions on the rational normal
quartic, the factorization of `L`, the two discriminants, the resultant, and
the determinant `2` were independently checked with SymPy on 2026-10-09.
The literal four-distinct-roots statement also holds in characteristic not
`2,5,7`; the audit's accepted scope is characteristic zero.


---

## Source: 2026-10-09-session-dp4-projection-local-lift.md

# An exact quartic carrier of C0 with four A1 normalization points

Date: 2026-10-09. Author: `singular_local_lift`, working for
`singular_normalization_next_frontier`.

Status: **PROVED HERE**, with the exact identities below. This constructs
one integral quartic containing the fixed C0 and proves its finite
birational normalization has four isolated singularities on the lifted
curve. It also excludes every mate for this particular carrier by an
explicit fiber obstruction. The singular-normalization frontier as a
whole and the universal STCI problem remain open. No canonical files
are edited by this note.

## 1. The normal degree-four del Pezzo surface

Over an algebraically closed field k of characteristic zero, let

    S = V(ae-c^2, bd-c^2) in P4[a:b:c:d:e].

Its homogeneous coordinate ring is a domain. Indeed first form the
domain R0=k[a,b,d,e]/(ae-bd), whose fraction field is k(a,b,d), with
e=bd/a. The polynomial c^2-bd is irreducible over that fraction field:
bd has odd valuation at b and d and is not a square. Being monic,
it embeds R0[c]/(c^2-bd) into that quadratic field. This quotient is
exactly the coordinate ring of S.

The two equations form a complete intersection, so the surface is
Cohen--Macaulay, has degree four, and has dualizing sheaf O_S(-1).
The Jacobian has rank less than two at exactly the four coordinate
vertices corresponding to a,b,d,e. On c!=0, all of a,b,d,e are
nonzero and the two rows have rank two. On c=0, ae=bd=0: if two
coordinates are nonzero the rows again have rank two, while a
coordinate vertex has rank one. Thus there are exactly four isolated
singularities. In the chart a=1, eliminate e=c^2 and obtain
bd=c^2; this is an A1 singularity. The other vertices are symmetric.
Serre's criterion proves normality. The same argument proves the
homogeneous coordinate ring is normal: its singular locus has
codimension at least two in the affine cone. Hence S is the normal
four-A1 degree-four del Pezzo surface, polarized by H=O_S(1).

## 2. An invertible coordinate change and the exact projection

Put [r:p:z:q:t]=[Y0:Y1:Y2:Y3:Y4] and set

    a = p+4z+4q,
    b = -r-3p-2z,
    c = -p-3z-2q,
    d = -z-3q-2t,
    e = p+2z+q.

The five-by-five matrix has determinant 2, so this is a projective
coordinate change. In these coordinates the equations become

    Q1 = pq-z^2,
    Q2 = 7Q1+D+Lz,

where

    L = r-3p-6q+4t,
    D = -p^2-2pq+6pt-4q^2+3qr+2rt.

Project from the center [0:0:1:0:0], deleting z. At the center Q1=-1
and Q2=-7, so the center lies outside S. The projection is a morphism
on S, and it is finite: every fiber is the intersection of S with a
line through the center; a positive-dimensional intersection would
contain that whole line and hence the center, which is impossible.
The morphism is proper with finite fibers and therefore finite.

On the nonempty open L!=0 it has the inverse

    z = -D/L.

Consequently it is birational. Its image is an integral surface X in
P3[r:p:q:t]. Since the polarization is pulled back from O_X(1), the
degree formula gives deg(X)=H^2=4. Eliminating z gives the exact
quartic equation

    F = D^2-pq L^2 = 0.

Indeed this degree-four polynomial vanishes on the image. The
irreducible defining equation of the integral degree-four image must
have that same degree and hence equals F up to a scalar. In
particular the image is a quartic, not a quadric with a degree-two
map. Since S is normal and the morphism is finite and birational,
S is the normalization of X.

## 3. The lifted C0 passes through all four normalization singularities

The rational normal quartic

    c_tilde = [u^4:u^3v:u^2v^2:uv^3:v^4] in P4[r:p:z:q:t]

lies on S by literal substitution into Q1 and Q2. Its projection is
the fixed curve

    C0 = [u^4:u^3v:uv^3:v^4] in P3[r:p:q:t].

This is the standard smooth embedded rational quartic. The projection
restricts to an isomorphism from c_tilde onto C0. In a chart at either
endpoint, respectively p/r=v/u and q/t=u/v give local coordinates;
the remaining points are covered by r!=0 or t!=0, where the same
parameter recovery proves the isomorphism.

In a,b,c,d,e coordinates the lifted parametrization is

    a = uv(u+2v)^2,
    b = -u^2(u+v)(u+2v),
    c = -uv(u+v)(u+2v),
    d = -v^2(u+v)(u+2v),
    e = uv(u+v)^2.

Thus u=0, v=0, u+v=0 and u+2v=0 map respectively to the d,b,a,e
vertices. The smooth lifted curve meets all four A1 singularities.
Its ambient projection remains the smooth C0. This is an actual
degree-four C0 carrier demonstrating that smoothness of the curve
does not force smoothness of its normalization along that curve.

## 4. The actual conductor is a smooth plane conic

Let A=k[r,p,q,t]/(F) and

    B=k[r,p,z,q,t]/(z^2-pq,D+Lz).

As an A-algebra B is generated by z, with module generators 1,z.
To compute B/A completely, first use z^2=pq. Over the polynomial
ring R=k[r,p,q,t], this intermediate ring is free with basis 1,z.
Multiples of D+Lz have coefficient vectors generated by

    (D,L),       (pq L,D).

Thus B has that two-by-two module presentation. Quotienting by the
image of R generated by 1 leaves precisely

    B/A = (R/(L,D))(-1) = (A/(L,D))(-1).

The annihilator of B/A is therefore exactly J=(L,D), which is the
actual conductor ideal downstairs. This proves equality of schemes,
not only equality of supports or a proposed candidate conductor.
Sheafifying yields the actual projective conductor.

On L=0, substitute r=3p+6q-4t and obtain

    D|L = -p^2+7pq+14q^2+12pt-8t^2.

Its symmetric quadratic matrix has determinant -294, so Gamma=V(L,D)
is a smooth plane conic in characteristic zero. Pulling J to B gives
(L), since D=-Lz in B. The upstairs conductor is the Cartier
hyperplane curve E=V(L) on S. It is the degree-two cover of Gamma
given by z^2=pq. The cover has generic degree two and has four distinct
simple branch points, namely Gamma intersect {pq=0}. Those four
points are distinct because Gamma contains neither p=q=0 nor a
tangency to either coordinate line. Hence E is a smooth genus-one
curve. The four A1 vertices have L-values -14,-1,-2,-28, respectively,
so E avoids them.

This smooth-conic conductor is outside the smooth-scroll conductor
Hilbert-polynomial calculation. The normalization here is singular
and anticanonically polarized.

## 5. An actual quadric divisor 2 c_tilde on S

For completeness the original proposed torsion relation can be made
literal. In a,b,c,d,e coordinates take

    Q = ab+ad+be+4de+2ac+2bc+6c^2+4cd+4ce.

Under the finite degree-two map P1xP1->S

    [s0:s1],[h0:h1] |->
    [s0^2 h0^2:s0^2 h1^2:s0s1h0h1:s1^2 h0^2:s1^2 h1^2],

the pullback of Q is f^2, where

    f = s0^2 h0h1+s0s1 h0^2+s0s1 h1^2+2s1^2 h0h1.

The map is finite since the pullback polarization O(2,2) is ample;
its generic degree is two and its involution changes the signs of
s0 and h0 simultaneously. The polynomial f is irreducible: viewed
as a quadratic in h0/h1, its discriminant is s0^4+4s1^4, which has
four distinct roots and is not a square in k(s0/s1). It has no
vertical component. Consequently Q has one irreducible zero-support
curve on S. Direct substitution shows that curve contains c_tilde,
so its support is exactly c_tilde. The cover is unramified at its
generic point, and its pulled-back multiplicity is two. Therefore

    div_S(Q)=2 c_tilde,       2 c_tilde ~ 2H.

In Y coordinates the same quadric is

    Q = -6pq-2pt+pz-qr+2qz+6z^2.

Modulo the surface equation z^2=pq this becomes
(p+2q)z-2pt-qr. The divisor c_tilde is non-Cartier at all four A1
vertices by the smooth-Cartier criterion proved in the companion
singular-local-lift note. Thus the local class there has exact order
two. The torsion is real; a forced c_tilde~H or forced avoidance of
the vertices would be unjustified.

## 6. This particular projected carrier has no mate of any degree

The construction of Q on S does not give a projected mate. In fact
this explicit projection excludes every mate.

On C0 the conductor linear form is

    L|C0=(u^2-4uv+2v^2)(u^2+uv+2v^2).

The two quadratic factors have discriminants 8 and -7 and resultant
50 after v=1. They have four distinct zeros, all with uv!=0.
At each of the corresponding four points of C0, L=D=0 and
pq=(uv)^4 is nonzero. The finite normalization fiber therefore has
exactly the two distinct points

    z = +u^2v^2,       z = -u^2v^2.

Only the first is on c_tilde, because c_tilde->C0 is an isomorphism.
The second is an isolated point of the reduced full inverse image
of C0 off c_tilde. Indeed off L=0 the inverse is uniquely z=-D/L,
so every curve component above C0 must be c_tilde; the extra fibers
occur only at these four points.

If a homogeneous mate G existed, its pullback to the normal integral
surface S would be a nonzero section of O_S(nH) whose zero support
was exactly the full inverse image of C0. Such a section is a
nonzerodivisor and defines a Cartier divisor. It cannot have an
isolated zero off its curve components: every minimal prime of a
nonzero principal ideal in a local domain has height one. At the
second point in any displayed fiber this would require an additional
curve of zeros. Finiteness would map that curve onto C0, contradicting
the uniqueness of the curve component above C0. Thus no mate exists,
in any positive degree.

The explicit quadric also witnesses the descent failure. On the
second lift it takes the value

    -2 u^3v^3(u^2+2v^2),

which is nonzero at all four conductor crossings: the resultant of
L(u,1) with u^2+2 is 64. It vanishes on the first lift. Hence no
positive power of Q can descend as a section pulled back from X.
This last calculation is supplementary; the full fiber argument
already excludes every possible projected mate, not merely powers
of a chosen quadric.

## 7. Verification and scope

`computations/verify_dp4_projection_local_lift_2026_10_09.py` checks
the invertible coordinate change, exact quadrics and eliminant,
RNC parametrization, actual module relations, conductor conic,
vertex values, squared-cover quadric, and all conductor crossing
and opposite-fiber identities. The proofs above, rather than the
checker status alone, establish normality, integral degree-four
image, finite birationality, equality of the conductor scheme and
the all-mate obstruction.

The final replay returned exit 0 and `status: PASS` on 2026-10-09.
Output:
`research/scratch/session-dp4-projection-local-lift-2026-10-09.json`.
Source SHA256:
`9cf1ac1ff6d30f1f0415afe59a3b987de06631253dd8359ca6fd55e9040f0dc0`.
Output SHA256:
`eede2536db9da0af4c0d7295106ba25e5aa378a71951e3b3a6a985a8163fc1f2`.

The first replay failed at a SymPy structural-equality comparison of
two differently factored expressions for the same discriminant. The
expanded difference was exactly zero. The correction compares that
expanded difference with zero; it changes no mathematical identity.
The failed source bytes are preserved and hash-verified at
`research/scratch/session-dp4-projection-local-lift-2026-10-09-failed-01-source.py`,
with the failure record at the matching `failed-01.json` path. That
source SHA256 is
`a0101c34a7cbefd8fb12a4a6cf676134ff284094b981620dd4461202d3605e7a`.

An independent adversarial proof accepted the finite birational
normalization, actual conductor module and all-mate fiber obstruction;
it is saved in
`research/notes/2026-10-09-session-dp4-projection-independent-audit.md`.
Serre's criterion used above is the primary
[Stacks Project lemma](https://stacks.math.columbia.edu/tag/031S).

This is one verified excluded carrier. It does not exhaust the
singular degree-four del Pezzo normalization family, other singular
normalizations, or higher carrier degrees.
