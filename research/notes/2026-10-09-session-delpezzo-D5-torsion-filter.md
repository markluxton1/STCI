# The D5 root-saturation filter for degree-four ADE del Pezzo normalizations

Date: 2026-10-09. Owner: `delpezzo_d5_torsion_filter`.
Status: **PROVED HERE, independently accepted within the stated
weak-del-Pezzo/ADE hypotheses**; the exhaustive exact lattice checker
has terminal PASS. The [written independent proof audit](2026-10-09-session-delpezzo-D5-torsion-independent-audit.md)
accepts sections 2--5 without corrections. This note does not classify all sectional-genus-one
normalizations, construct a mate, or resolve the STCI problem.

This follows the [sectional-genus reduction](2026-10-09-session-normalization-sectional-genus-zero.md)
and complements the [explicit four-A1 family](2026-10-09-session-singular-delpezzo-four-A1-family.md).
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
[bounded written audit](2026-10-09-session-delpezzo-D5-torsion-independent-audit.md)
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
accepted [genus-one model-coverage theorem](2026-10-09-session-genus-one-delpezzo-reduction.md)
now supplies those hypotheses for rational genus-one quartic normalizations
containing C0; combining the two theorems is justified by that separate
record. Sectional genus two, higher carrier degrees,
other normalizations, and the universal STCI question remain outside
this note's conclusion. No canonical frontier file has been edited
by this owner.
