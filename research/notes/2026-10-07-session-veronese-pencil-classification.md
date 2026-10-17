# Finite Veronese projections: no quartic mate in any degree

Date: 2026-10-07; strengthened on 2026-10-08. Status: **PROVED HERE,
with independent adversarial audit accepted**. Exact normal-form
and descent identities have passed the
companion verifier. Exhaustiveness is proved by the linear-algebra
argument below, not by a parameter search. No canonical state is edited
by this note, and no novelty claim is made.

The [independent Oct8 audit](2026-10-08-session-veronese-allmate-independent-audit.md)
checks the classification, full inverse support, exceptional fibers,
global constant multiplier and arbitrary-degree first conductor jet.

## Statement and scope

Let k be algebraically closed of characteristic zero. Let nu:P2->X be
a finite birational morphism onto an integral quartic in P3, with
nu*O_X(1)=O_P2(2). If C is a smooth rational curve of degree four on X,
there is **no homogeneous form G of any positive degree b** such that
X intersect V(G) has set-theoretic support C.

This excludes every quartic carrier with this normalization and
polarization, including its non-slc degenerations. It does not classify
all nonnormal quartics and does not extend to singular normalizations.
No novelty claim is made. The earlier slc consequence survives as a
subsidiary classification: if X has ordinary double crossings in
codimension one, it is projectively equivalent to the Roman surface.

Semi-log-canonical varieties require ordinary normal crossings in
codimension one; see
[Fujino, Fundamental theorems for semi log canonical pairs, Definition 2.3](https://www.math.kyoto-u.ac.jp/~fujino/fund-slc5.pdf).
Only this necessary condition is used to reject the Jordan cases.

## 1. Precise tensor and pencil convention

Let V=k^3. The quadratic Veronese is [v]->[v v^T] in P(Sym^2 V)=P5.
A quadratic form q(v)=v^T Q v is a covector on Sym^2 V by the pairing
trace(P Q). Off-diagonal coefficients of the symmetric matrix Q are
half the coefficients of the corresponding cross terms of q.

The four independent quadratic sections defining nu span a
four-dimensional space W of covectors. Its annihilator L=W^perp is
two-dimensional in Sym^2 V. The projection center is the line P(L).
Choose a basis of L and write its symmetric matrix pencil M(s,t)=sA+tB.
Basepoint freeness says that P(L) misses the Veronese: **no nonzero pencil
member has rank one**. Rank-one symmetric matrices over k are precisely
the nonzero scalar multiples of v v^T. The finite normalization is
basepoint free, so this condition holds here.

Changing coordinates of P2 acts on the center matrices by congruence.
Changing the pencil basis makes a linear substitution in (s,t).
Changing the basis of W is an ambient projective coordinate change.
We keep all three permitted operations explicit below.

## 2. The regular pencil: self-adjoint Jordan possibilities

Suppose some pencil member A is invertible. The operator T=A^(-1)B
is self-adjoint for the nondegenerate symmetric form g with matrix A.
Generalized eigenspaces for distinct eigenvalues are orthogonal and
nondegenerate. Indeed the relatively prime powers of (T-lambda) and
(T-mu) give the orthogonality by self-adjointness; the direct-sum
decomposition and nondegeneracy of g give nondegeneracy on each summand.

There are only the Jordan partitions of a three-dimensional space.
If T is diagonalizable, choose an orthogonal eigenbasis and scale its
vectors to obtain A=I and B diagonal. If two eigenvalues coincide,
B-lambda A has rank one, unless B=lambda A makes L one-dimensional.
Both possibilities are forbidden. Therefore the diagonalizable case
has three distinct eigenvalues.

In this case W contains the three cross quadrics xy,xz,yz. Its remaining
diagonal quadric has coefficients proportional to

    (lambda2-lambda3, lambda3-lambda1, lambda1-lambda2).

Every coefficient is nonzero. Rescaling the three source coordinates
by square roots and rescaling the ambient basis gives exactly

    [x:y:z] -> [yz:zx:xy:x^2+y^2+z^2],

the standard Roman normalization.

For a Jordan block of size two, choose v with Nv=e, where N is the
nilpotent part. Then g(e,e)=0 and g(e,v)!=0. Scale the chain and replace
v by v-g(v,v)e/(2g(e,v)) to make its Gram matrix the antidiagonal
two-by-two matrix. The one-dimensional distinct-eigenvalue summand can
be scaled to Gram value one. If its eigenvalue equals that of the
Jordan block, B-lambda A has rank one and is forbidden. If the eigenvalues
are distinct, a pencil basis change moves them to zero and one. Swapping
the two chain coordinates if needed gives the following center matrices.
If that pencil change rescales the nonzero nilpotent coefficient, a
chain congruence diag(c,c^(-1)) preserves the antidiagonal Gram matrix
and removes that coefficient using a square root in k:

    A2=[[0,1,0],[1,0,0],[0,0,1]],
    B2=[[1,0,0],[0,0,0],[0,0,1]].

Their annihilator is spanned by

    q2=[y^2,xz,yz,z^2-xy-x^2].

For a single Jordan block of size three, put e0=N^2v,e1=Nv,e2=v.
Self-adjointness gives

    g(e0,e0)=g(e0,e1)=0,
    g(e0,e2)=g(e1,e1)=gamma!=0.

The nonzero gamma follows from nondegeneracy: otherwise e0 would be
orthogonal to the whole space. Write delta=g(e1,e2), epsilon=g(e2,e2).
Replacing v by v+a Nv+b N^2v changes delta to delta+2a gamma and epsilon
to epsilon+2a delta+(a^2+2b)gamma. Choose a,b to kill both and rescale
gamma to one. Thus the Gram matrix is the antidiagonal three-by-three
matrix, while T is the single Jordan block. Subtracting its eigenvalue
times A from B gives

    A3=[[0,0,1],[0,1,0],[1,0,0]],
    B3=[[0,0,0],[0,0,1],[0,1,0]].

The annihilator is spanned by

    q3=[x^2,xy,z^2,y^2-xz].

These are all regular-pencil cases. The chain changes just supplied
prove the small-dimensional self-adjoint normal forms directly.

## 3. Jordan size two: a doubled conductor

The q2 forms have no common zero: y=0 from y^2, then xz=0, and
z^2-x^2 excludes either coordinate vertex. Therefore their map is finite.
On y z!=0 its coordinates recover x/y=b/c and z/y=c/a, so it is
birational. Substitution gives the irreducible image equation

    F2=c^4-a d c^2-a^2bc-a^2b^2=0.

It is primitive linear in d, hence irreducible. The line Gamma:a=c=0
is singular. At its generic point take b=1 and d=D, with coefficient
field k(D). The transverse equation has lowest homogeneous part -a^2.
An ordinary node has a quadratic initial form with two distinct lines
after algebraic closure of the coefficient field. A square initial
form cannot become such a node. Thus this image fails the necessary
codimension-one normal-crossing condition for slc.

One can see the conductor multiplicity directly. Put a=eta c^2+...
in the transverse equation. The first coefficient is

    1-D eta-eta^2=0.

At the generic point its two roots are distinct, since D^2+4!=0.
Hensel expansion gives two smooth branches a=f_+(c),a=f_-(c), whose
difference has order two. The completed curve ring over the algebraic
closure of k(D) sits in k(D)^alg[[c]]^2 as pairs congruent modulo
c^2. Its normalization conductor is c^2 on each branch. Equivalently
the upstairs conductor has generic multiplicity two on y=0.

This is not a nonordinary isolated point with a reduced generic
conductor: the whole generic double curve is non-slc.

## 4. Jordan size three: a tripled conductor

The q3 forms have no common zero: x=0 leaves z^2 and y^2. On x!=0
they recover y/x=b/a and z/x=(b/a)^2-d/a, so the map is finite and
birational. The irreducible image equation is

    F3=(b^2-a d)^2-a^3 c=0,

primitive linear in c. Its singular line Gamma:a=b=0 has, on c=1,d=D,
transverse initial form D^2a^2, again a square at the generic point.
It is not an ordinary double crossing.

For its conductor, expand

    a=b^2/D+epsilon b^3+... .

The first nontrivial coefficient is

    D^2 epsilon^2-D^(-3)=0.

The two roots are distinct and nonzero generically. The two smooth
branches have difference of order three in b. Their normalization
conductor is b^3 on each branch; upstairs it has generic multiplicity
three on x=0. Hence this image is also non-slc along a curve.

The pair-congruence conductor calculation used in these two cases is
elementary: for two graph branches a=f_+(b),a=f_-(b), the image of the
quotient by their product in the direct sum of the two branch rings
consists of pairs whose difference belongs to (f_+-f_-). Its conductor
on either branch is that ideal. Higher-order coefficients do not change
the exponents two and three found above.

The full upstairs conductor divisors in these coordinates are

    D2=2{y=0}+{z=0},        D3=3{x=0}.                       (4.1)

Here is also a global check of the multiplicities. A quartic hypersurface
has omega_X=O_X. Finite duality identifies Hom_X(nu_*O_P2,O_X)
with nu_*omega_P2, so the conductor upstairs is the invertible ideal
O_P2(-3). The Hom module is indeed the conductor: in the common
function field an O_X-linear map is multiplication by a rational
function h, and its image lies in O_X precisely when h O_P2 lies
in O_X. The finite-duality input is recorded in
[Stacks, finite morphisms](https://stacks.math.columbia.edu/tag/0FKW)
and [normalized finite-map duality](https://stacks.math.columbia.edu/tag/0A7M),
Lemma 47.16.1. The inverse in section 3 is an isomorphism away from
y z=0, whose images are lines; both those lines have generically
two normalization preimages. The multiplicity two on y=0 leaves
multiplicity one on z=0 because the total degree is three.
Section 4's inverse is an isomorphism away from x=0, so its
single conductor support has multiplicity three. The no-mate
arguments below require only the first conductor jet of D3.

## 5. Every-member-singular pencil: direct Kronecker reduction

Now assume det M(s,t) is identically zero. Every nonzero member has
rank exactly two by the center condition. The adjugate is a nonzero
rank-one symmetric matrix of homogeneous quadratic polynomials.
Over the UFD k[s,t], it can be written

    adj M=h(s,t) v(s,t) v(s,t)^T,

where the entries of v are homogeneous of a common degree r and have
no common polynomial factor, and h is polynomial of degree 2-2r.
For completeness, start with a nonzero column, divide its entry gcd
to obtain v, and use rank one to express all columns as polynomial
multiples of v. The multiples are polynomial because a denominator
would divide every entry of primitive v. Symmetry makes the multiplier
row proportional to v, and the same denominator argument makes the
factor h polynomial.

The adjugate never vanishes at a point of P1, since rank M is always two.
Therefore h is nowhere zero, hence has degree zero. It follows that
r=1. The two coefficient vectors of v are independent; otherwise its
entries would share a linear factor. A source coordinate change gives
v=(s,t,0). Write M=sA+tB. The identity Mv=0 gives

    Ae1=0, Be2=0, Ae2=-Be1.

Symmetry forces

    M=[[0,0,-kappa t],[0,0,kappa s],
       [-kappa t,kappa s,alpha s+beta t]],

with kappa!=0, since otherwise its rank would be at most one. Rescale
kappa to one, then replace the third basis vector by itself plus
(beta/2)e1-(alpha/2)e2. This removes the lower diagonal entry.
Permuting coordinates gives the Kronecker pencil

    [[0,s,t],[s,0,0],[t,0,0]].

Its annihilator is [x^2,y^2,yz,z^2]. The image lies on the quadric
bd-c^2=0 and the map has generic degree two, via x->-x. It is not
birational onto a quartic and cannot be the normalization under study.
The reduction therefore has no omitted singular-pencil stratum.

## 6. A mate would pull back to a power of one conic

The three birational quartic types above have singular loci supported
on lines, as follows directly from their equations or inverses. A smooth
integral degree-four curve C cannot be contained in such a locus. Thus
nu is an isomorphism at the generic point of C. Its inverse image has
one reduced curve component c mapping finitely and birationally to C.
Because C is normal, this finite birational map is an isomorphism:
locally a finite ring between O_C and its fraction field is O_C.

If a mate G exists, nu*G is a nonzero section of O_P2(2b). Its zero
set is the full inverse image of C. A principal divisor on the smooth
surface P2 has no isolated components. Hence the full reduced inverse
image is c, with no additional isolated points. Every normalization
fiber over C is a singleton, because c->C is an isomorphism. Write
div(nu*G)=m c. The degree of nu*O_C(1)=O_P2(2)|c equals four, so c
has plane degree two. Comparing degrees then gives m=b. In homogeneous
coordinates this means

    nu*G = constant * f^b,

where f is the irreducible quadratic equation of the smooth conic c.
This is a full-support assertion, not just a statement about the
strict transform of C. It is what permits the following fiber and
descent tests.

## 7. Roman type: the six allowed points cannot lie on a conic

For [yz:zx:xy:x^2+y^2+z^2], each coordinate axis maps two-to-one to
a conductor line. The only singleton fibers on these axes are

    [0:1:+/-1], [1:0:+/-1], [1:+/-1:0].

The three coordinate vertices have a common image and cannot belong
to c. At each listed point, the derivative in the axis direction
vanishes and the derivative normal to the axis is nonzero. Since the
embedded image C is smooth, c must meet each axis transversely there.
Consequently its two intersections with each axis are that axis's
two listed points. A conic would have to contain all six.

For a quadratic form A x^2+B y^2+C z^2+D xy+E xz+F yz, evaluation
at these six points gives D=E=F=0 and A+B=A+C=B+C=0. In
characteristic zero all six coefficients vanish. This contradicts
the nonzero equation f. This also reproduces the
[independent Roman argument](2026-10-07-session-nonnormal-structural-progress.md).

## 8. Jordan size two: only one allowed point on one conductor line

Use the q2 coordinates fixed in section 2. On the line z=0 and the
chart y=1, writing r=x/y, the projection is

    r -> [1:0:0:-r-r^2].

Its fiber involution is r->-1-r; the only finite singleton is
p=[-1/2:1:0]. The point at infinity [1:0:0] has the same image
[0:0:0:1] as [0:0:1], so its full normalization fiber is not a
singleton either. The mate's full support therefore forces
c intersect {z=0} to have support only p.

Near p, put y=1, x=-1/2+v. In the a=1 target chart the map becomes

    (v,z) -> ((-1/2+v)z, z, z^2+1/4-v^2).

Its derivative at p depends only on the z derivative. Smoothness of
the embedded image C forces z to be a local parameter on c, hence
the intersection with z=0 is transverse and has multiplicity one.
But a conic not containing that line has total intersection degree
two. There is no other allowed point and no second multiplicity at p.
This excludes the Jordan-size-two carrier in every mate degree,
without a semi-log-canonical assumption.

## 9. Jordan size three: the first conductor jet forbids a conic power

For q3=[x^2:xy:z^2:y^2-xz], the line x=0 maps by
[y:z]->[z^2:y^2]. Its only singleton fibers are
p=[0:0:1] and q=[0:1:0]. At p the z=1 affine map is

    (x,y) -> (x^2, xy, y^2-x),

whose differential is nonzero only in the x direction. At q, use
y=1 and the target chart d=1-xz: the derivative of b/d=x/(1-xz)
is nonzero only in the x direction; the other two chart coordinates
have zero differential. Smoothness of C again forces transverse
intersection of c with x=0 at either point. Degree two and the
singleton fiber condition therefore force c to pass through both.

It follows that the homogeneous equation of c has the form

    f=alpha x^2+beta xy+gamma xz+delta yz, with delta!=0.       (9.1)

Indeed the coefficients of y^2 and z^2 vanish at q and p, and
delta=0 would make f divisible by x, contradicting irreducibility.
On z=1 put B=k[x,y], and let

    A=k[x^2,xy,y^2-x] subset B

be the affine target ring. The mate's pullback is a nonzero constant
multiple of f^b and must belong to A. We show it cannot, using only
the first infinitesimal neighborhood of the generic conductor line.

In the ring R=k(y)[x]/(x^2), define the involution

    iota(x)=-x, iota(y)=-y+x/y.                              (9.2)

Substitution gives iota^2=identity and fixes x^2,xy,y^2-x modulo
x^2. Thus the image of every element of A in R is iota-invariant.
For (9.1) on z=1,

    f = delta y+x(beta y+gamma)                    modulo x^2,
    iota(f) = -delta y+x(delta/y+beta y-gamma)      modulo x^2.

Comparing the constant term of f^b and iota(f)^b forces b even,
since delta!=0 and the characteristic is zero. For positive even b,
comparison of the x coefficients gives

    b(delta y)^(b-1) * (2 beta y+delta/y)=0 in k(y).

The prefactor is nonzero. Therefore 2 beta y^2+delta would vanish
identically, forcing beta=delta=0. This contradicts delta!=0.
No power f^b descends, so this carrier also has no mate in any degree.

This uses an actual conductor jet; the reduced fiber condition alone
would allow the conic through p and q. It does not assert that an
arbitrary ramification scheme lies on c. Characteristic zero is
essential here: when the exponent is divisible by the positive
characteristic, the displayed derivative comparison loses its force.

## 10. Conclusion and continuation boundary

The pencil classification exhausts all finite birational quartic maps
from (P2,O(2)). The Roman and Jordan-size-two cases are excluded by
the full normalization fibers and smooth conic intersections. The
Jordan-size-three case additionally uses the first conductor jet.
Thus all three cases are excluded in every mate degree. The independent
audit linked above accepts the complete scope and proof.

The subsidiary slc classification remains valid: its only possible
type is Roman, because the Jordan cases have nonreduced conductors
**generically**. The stronger no-mate proof does not rely on slc.
It does not repair the false general R subset c implication:
the [local slc counterexample](2026-10-07-session-ramification-scheme-counterexample.md)
still stands for other normalized surfaces. Other nonnormal quartic
classes and singular normalizations remain outside this theorem.

The [exact verifier](../computations/verify_session_veronese_pencils.py)
checks the tensor annihilator convention, canonical center determinants,
image equations and dense rational inverses, generic square tangent
cones, conductor branch-separation exponents, singleton-fiber and
transversality controls, and the first-jet involution and coefficient
obstruction. Exhaustiveness and
the no-mate deduction are the arguments above, not consequences of a
PASS line alone.
