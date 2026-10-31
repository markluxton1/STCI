# Finite Veronese projections and their mate obstructions

Work over an algebraically closed field of characteristic zero. An integral
quartic in P3 normalized by the Veronese surface P2 with H=O(2) has no
set-theoretic mate for a smooth rational degree-four curve in any mate
degree. The projection center is derived from its actual four sections.
The proof classifies its symmetric pencil and retains whole conductor
jets, not merely the reduced double locus. It is the independently accepted
Veronese component of the [quartic-carrier proof](../synthesis/quartic_carrier_proof.md).

A subsidiary classification is also retained: if X has ordinary double
crossings in codimension one, it is projectively equivalent to the Roman
surface; the Jordan forms below violate that condition. The application
to semi-log-canonical surfaces uses only the ordinary-normal-crossing
necessary condition in [Fujino, Definition2.3](https://www.math.kyoto-u.ac.jp/~fujino/fund-slc5.pdf),
not a sufficient test for semi-log-canonicity.

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

## 5. Every-member-singular pencils

The complete kernel-degree and matrix-normal-form proof is in Section10
below. Its projection has generic degree two and quadric image, so it
cannot be the finite birational normalization of an integral quartic.

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
[independent Roman argument](OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-nonnormal-structural-progressmd).

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



## 10. Complete singular-pencil classification

The trace pairing convention of Section1 is used only when two is
invertible. For the characteristic-two formulas in this singular-pencil
argument, use the explicit six-entry coefficient pairing:
\((P_{11},P_{12},P_{22},P_{13},P_{23},P_{33})\) paired once with
\((x^2,xy,y^2,xz,yz,z^2)\). No off-diagonal coefficient is counted twice.
The coordinate kernel and degree-two projection calculations below use
that interpretation, not a degenerate trace pairing in characteristic two.

### 10.1. The kernel map has degree one

Work in the unique factorization domain `R=k[s,t]`. Choose a nonzero column of
the adjugate matrix and divide its entries by their homogeneous greatest
common divisor. The resulting kernel vector `v` is primitive and homogeneous,
with all nonzero entries of the same degree `e`. Since the pencil has rank two
over the fraction field, every column of its adjugate is a rational multiple
of `v`. Such a multiple is polynomial: the denominator of a rational scalar
in lowest terms would divide every component of `v`, contradicting
primitivity. Thus `adj(M)=v p^T` for a polynomial vector `p`.

The adjugate is symmetric. Its symmetry gives `v_i p_j=v_j p_i`, so `p` is
a rational scalar multiple of `v`; the same primitive-vector argument makes
that scalar polynomial. Consequently

`adj(M)=h(s,t) v(s,t) v(s,t)^T`.

The entries of the adjugate have degree two, hence `deg(h)=2-2e`.
Primitivity of a homogeneous vector over `k[s,t]` means that its entries have
no common zero in projective one-space: a common zero would supply a common
linear factor. Since every member has rank two, the adjugate is nonzero at
every point of projective one-space. Therefore the homogeneous polynomial
`h` has no projective zero. Algebraic closedness forces `h` to be a nonzero
constant. It follows that `e=1`.

Write `v=s u+t w`. The vectors `u,w` are linearly independent, for otherwise
all entries of `v` would have a common linear factor. A constant change of
basis puts the kernel vector in the form `(s,t,0)^T`.

### 10.2. The complete matrix normal form

The identity `M(s,t)(s,t,0)^T=0` gives

`A e_1=0`, `B e_2=0`, and `A e_2+B e_1=0`.

Symmetry then forces

`M(s,t)=[[0,0,-b*t],[0,0,b*s],[-b*t,b*s,c*s+d*t]]`.

Here `b` is nonzero: otherwise every member would have rank at most one.
Rescaling and reparametrizing the pencil yields the normal form

`M(s,t)=[[0,0,t],[0,0,s],[t,s,alpha*s+beta*t]]`.                 (1)

This form is valid in every characteristic. In characteristic different
from two, replacing the third basis vector by itself plus a suitable linear
combination of the first two removes `alpha,beta`. Thus the usual singular
Kronecker pencil is the only congruence class in that characteristic.
In characteristic two the displayed diagonal terms need not be removable;
no assertion of a single congruence class is being made there.

For reference, the adjugate of (1) is

`-[s,-t,0]^T [s,-t,0]`,

and a nonzero `(s,t)` gives rank two. Both identities remain valid in
characteristic two, with the usual interpretation of the minus signs.

### 10.3. The projection has degree two and a quadric image

The line (1) in the six ambient Veronese coordinates is

`[0:0:0:t:s:alpha*s+beta*t]`.

Its four-dimensional annihilator therefore gives the projection

`[x:y:z] -> [x^2:xy:y^2:z^2-beta*x*z-alpha*y*z]`.              (2)

This map is basepoint-free. Its first three coordinates can vanish
simultaneously only when `x=y=0`, in which case the fourth is `z^2 != 0`.
The image satisfies the quadric equation `ac=b^2` in coordinates
`[a:b:c:d]`.

On `x != 0`, put `u=y/x` and `v=z/x`. Formula (2) becomes

`[1:u:u^2:w]`, where `w=v^2-(beta+alpha*u)*v`.

The induced extension `k(u,w) subset k(u,v)` has degree two. Indeed
`T^2-(beta+alpha*u)*T-w` is irreducible over `k(u,w)`: in
`k(u)[T,w]` it is linear and monic up to sign in `w`, its quotient is the
domain `k(u)[T]`, and Gauss's lemma applies when it is regarded as a primitive
polynomial over `k(u)[w]`. Thus the image is the entire quadric surface and
the generic degree is two.

The morphism is finite. The pullback of the hyperplane line bundle is
`O_P2(2)`, an ample line bundle, so no curve can be contracted. Alternatively,
the affine formula above is a monic quadratic finite map, and the analogous
`y != 0` chart together with the single preimage of the quadric vertex covers
all fibers.

In characteristic different from two, completing the square in the fourth
coordinate and adding a linear combination of the first three coordinates
reduces (2) to `[x^2:xy:y^2:z^2]`. In characteristic two, (2) is generically
separable if `(alpha,beta) != (0,0)`, and purely inseparable of degree two
otherwise. The image has degree two in either case.

**Consequence.** A basepoint-free projection of the Veronese surface whose
center is an identically singular symmetric pencil cannot have an integral
quartic surface as its image, and cannot realize the normalization map of
such a quartic surface. This disposes of the entire singular-pencil stratum;
it is not an argument about nonsingular determinant pencils.

## Reproduction

`research/computations/verify_session_veronese_singular_pencil.py` checks the
generic symbolic adjugate, the rank-two minors, the annihilator coordinates,
the target quadric equation, and the coordinate change in characteristic
different from two. The degree and exhaustiveness arguments above are
mathematical proofs, not consequences of a sampling computation.


## Characteristic and review scope

The [regular-pencil and full-conductor-jet checker](../computations/verify_session_veronese_pencils.py)
retains the exact normal-form, annihilator and arbitrary-power identities.
The singular-pencil companion checks its explicit matrix calculations.
Their existing recorded executions are reused; no fresh run is claimed.

The regular-pencil linear algebra uses algebraic closure and invertibility
of two; its Gram-chain adjustments divide by two and otherwise need no
characteristic-zero hypothesis. The Roman six-point contradiction and
the size-two Jordan singleton/transversality argument likewise extend to
odd characteristic under the same actual finite-map and full-support
hypotheses. The size-three involution-jet calculation is valid in odd
characteristic, but its contradiction for a mate power of degree b needs
b nonzero in the field: characteristic p dividing b kills that first jet.
Section10 separately interprets the singular-pencil coefficient pairing
in characteristic two. These are precise extensions of mechanisms, not
a positive-characteristic all-mate exclusion. The fixed curve has a
quartic-carrier STCI in every positive characteristic.

The characteristic-zero classification and all three obstructions had
separate independent source reviews and their faithful consolidated
replacement has been independently reconstructed. No inherited exact
checker was rerun merely for this transfer.
