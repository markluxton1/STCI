# Independent audit: all P2,O(2)-normalized quartic carriers

Date: 2026-10-08. Status: **PROVED by independent structural audit of
the supplied argument**. The audit includes non-slc Jordan projections;
no semi-log-canonical assumption is required. It does not exclude all
nonnormal quartic carriers: normalizations other than P2 with H=O(2)
remain outside its scope. No novelty claim is made.

**Theorem.** Over an algebraically closed characteristic-zero field,
let X be an integral quartic in P3 with finite normalization
nu:P2->X and nu*O_X(1)=O_P2(2). Then X cannot be a carrier in a
set-theoretic complete-intersection presentation of any smooth rational
quartic C in P3, regardless of mate degree or common singular points.

This note independently audits the strengthened argument developed in
[the pencil classification note](2026-10-07-session-veronese-pencil-classification.md).
That note is being upgraded from its earlier slc-only form; this audit
states the complete hypotheses and proof independently of edit timing.

## 1. Classification and its omitted-stratum checks

The normalization is defined by four independent sections of O_P2(2).
Its center line is a two-dimensional pencil of symmetric quadratic
tensors, using the pairing trace(P Q) against symmetric coefficient
matrices of the four quadrics. The off-diagonal coefficient convention
is essential: a cross-term coefficient is twice that matrix entry.
Basepoint freeness is equivalent to the center containing no rank-one
matrix. The center basis is independent, so no nonzero pencil parameter
gives the zero matrix.

I independently checked all cases of the direct three-dimensional
linear-algebra argument. If a center member A is invertible, the
operator A^(-1)B is self-adjoint for the nondegenerate symmetric form A.
Distinct generalized eigenspaces are orthogonal and nondegenerate.
The possible Jordan partitions are:

- Three distinct simple eigenvalues: after an orthogonal basis change,
  the annihilator contains xy,xz,yz and a diagonal quadric with all
  coefficients nonzero. Rescaling source coordinates gives the Roman
  map [yz:zx:xy:x^2+y^2+z^2].
- A repeated diagonalizable eigenvalue, or a size-two Jordan block with
  its size-one block sharing the same eigenvalue: subtracting that
  eigenvalue times A produces a rank-one center member, forbidden.
- A size-two Jordan block plus a distinct eigenvalue: chain rescaling
  and a pencil basis change give the map
  [y^2:xz:yz:z^2-xy-x^2].
- A single size-three Jordan block: its antidiagonal chain Gram matrix
  gives [x^2:xy:z^2:y^2-xz].

The chain Gram transformations in the classification note are exact:
for size three, replacing the cyclic vector v by v+a Nv+b N^2v changes
the two unwanted Gram entries by delta->delta+2a gamma and
epsilon->epsilon+2a delta+(a^2+2b)gamma, where gamma!=0. These operations
remove them without losing the Jordan chain. For size two the
corresponding isotropic chain has nonzero cross pairing, and its single
diagonal entry is removable. No diagonalizability assumption is made
for a symmetric matrix over an algebraically closed field.

For an identically singular center pencil, every member has rank two.
The primitive adjugate argument gives adj M=h vv^T, with deg h=2-2deg v.
No projective zero of adj M is possible, so h is constant and v is
linear with independent coefficient vectors. Putting v=(s,t,0) directly
forces the Kronecker pencil, up to removable diagonal terms. Its
projection has quadric image and generic degree two, contradicting the
finite birational quartic hypothesis. I checked this against the
[separate singular-pencil proof](2026-10-07-session-veronese-singular-pencil.md).

Thus Roman, Jordan2 and Jordan3 exhaust the hypotheses. The two Jordan
cases were previously discarded using slc; the arguments below exclude
their mates without that assumption.

## 2. A mate requires a smooth lifted conic, with full inverse support

Each of the three normal forms has singular support consisting of
lines. For Jordan2 the image equation is

    c^4-a d c^2-a^2bc-a^2b^2=0.

Its derivative with respect to d is -a c^2. If a=0, the equation forces
c=0; if c=0, it forces a=0 or b=0. Its singular support is the union
of the two lines a=c=0 and b=c=0. For Jordan3 the equation is

    (b^2-a d)^2-a^3c=0;

its derivative with respect to c forces a=0 at a singular point, then
the equation forces b=0. The Roman equation has three coordinate
double lines, as the derivative in the fourth coordinate forces the
product of its first three coordinates to vanish.

An integral degree-four C cannot be one of these lines. Hence the
normalization is an isomorphism at its generic point. Its dominant
curve preimage c is finite birational over the smooth C and therefore
isomorphic to C. A mate's nonzero pullback has full zero support equal
to the entire reduced inverse image. Its plane divisor cannot have an
isolated component. Thus the entire reduced inverse image is c, each
fiber over C has just one point, and the map c->C is injective and an
isomorphism.

The hyperplane pullback has degree 2 on a plane curve, whereas its
restriction to c has degree 4. Therefore c has plane degree 2. It is
a smooth integral conic, defined by an irreducible homogeneous form f.
If a mate G has degree n>0, the polynomial G(q0,q1,q2,q3) is homogeneous
of degree 2n, nonzero, and has support exactly V(f). Unique
factorization gives

    G(q0,q1,q2,q3)=c0 f^n, c0 in k*.

This scalar is a genuine global constant. Arbitrary units from an
affine localization must not be inserted into this equality. These
facts are what permit the descent tests below.

## 3. Roman case

For [yz:zx:xy:x^2+y^2+z^2], the coordinate vertices have one common
image, so c avoids them. On each coordinate line the double-cover
involution interchanges the other two coordinates. Its only singleton
fibers are the two points with those coordinates equal or opposite.
At each such ordinary pinch a smooth embedded image requires transverse
passage through that coordinate line.

The conic must consequently contain all six points

    (0,1,+/-1), (1,0,+/-1), (1,+/-1,0).

Evaluating a general conic shows all three cross coefficients vanish
and its diagonal coefficients satisfy A+B=A+C=B+C=0. In characteristic
zero it is the zero form. This excludes Roman in every mate degree.
The direct no-conic certificate is retained in the
[structural verifier](../computations/verify_session_nonnormal_structural.py).

## 4. Jordan2: one available transverse point cannot supply degree two

Use q=[y^2:xz:yz:z^2-xy-x^2]; this is the source-coordinate swap of the
equivalent [x^2:xz:yz:z^2-xy-y^2] used in the other audit. Let L:z=0.
On its chart y=1, put r=x/y. Its image is

    [1:0:0:-r-r^2].

The two parameters r and -1-r have the same image. The only finite
singleton is r=-1/2. The point at infinity [1:0:0] has the same image
as [0:0:1], so it is not a singleton of the **full** normalization
fiber. Full support and injectivity of c->C therefore allow c to meet
L only at p=[-1/2:1:0].

Near p, with source coordinates (r,z), use the target chart q0=1. Its
three coordinates are

    (r z,z,z^2-r-r^2).

At p its differential annihilates the r direction and sends the z
direction to (-1/2,1,0), a nonzero vector. Since c->C is an isomorphism
and C is a smooth embedded curve, its differential must be nonzero.
Thus c is transverse to L at p, with intersection multiplicity one.
An integral conic not containing L has total intersection two with L.
Only one point of multiplicity one is available, a contradiction.

No ordinary-pinch or reduced-conductor assumption was used here. The
explicit normalization differential and the entire fiber count suffice.

## 5. Jordan3: first-order conductor descent excludes every power

Use q=[x^2:xy:z^2:y^2-xz] and L:x=0. The entire preimage of its
singular line is L, whose map is [y:z]->[z^2:y^2]. Its only singleton
fibers are p=[0:0:1] and p'=[0:1:0]. At p, on z=1, the differential
of (x^2,xy,y^2-x) is nonzero only in the x direction. At p', on y=1,
the analogous target chart has differential nonzero only in the x
direction. Therefore a smooth image curve passes transversely through
L at either singleton.

The conic has to meet both points once, so its equation has the form

    f=alpha x^2+beta xy+gamma xz+delta yz, delta!=0.

The absence of y^2,z^2 terms is exactly passage through p,p'; if
delta=0 the conic would contain L and be reducible.

On z=1, the image coordinate ring is

    A=k[x^2,xy,y^2-x] subset k[x,y].

Work in T=k[y,y^(-1),x]/(x^2). Define

    iota(x)=-x, iota(y)=-y+x/y.

The image of y is a unit, and direct substitution proves iota^2=id.
It fixes x^2, xy and y^2-x modulo x^2. Thus every original coordinate
function, including the restriction of G, is fixed by iota in T.
The global equality from section 2 requires f^n to be fixed as well.

Modulo x^2 one has

    f=delta y+x(beta y+gamma),
    iota(f)=-delta y+x(delta/y+beta y-gamma).

The constant term of f^n first forces (-1)^n=1, so n is even. Its
coefficient of x is then, after division by the nonzero scalar
n delta^(n-1)y^(n-1), incompatible with invariance unless

    2 beta y+delta/y=0,
    equivalently 2 beta y^2+delta=0 in k[y,y^(-1)].

This identity forces delta=0, a contradiction. The use of n!=0 is
precisely where characteristic zero matters. This is an argument for
all positive mate degrees, not a finite collection of power tests.

The involution is a first-order conductor descent test. It does not
assert scheme containment of nonreduced ramification in c, the general
claim refuted by the
[local counterexample](2026-10-07-session-ramification-scheme-counterexample.md).

## 6. Audit outcome and reproducibility

The strengthened theorem passes the full independent audit: center
classification, rank-one exclusion, singular-pencil boundary,
normalization maps, regularity at the generic point of C, full inverse
purity, smooth lifted conic, actual global units, all exceptional fibers,
endpoint differentials, and arbitrary-degree first-order descent have
all been checked. No slc assumption remains in the result.

The [independent exact verifier](../computations/verify_session_veronese_allmate_independent.py)
checks the Jordan2 fiber identity and differential, both Jordan3 endpoint
differentials, the actual order-two involution and its fixed generators,
and the normalized symbolic coefficient contradiction for all even n.
It also checks the gradient identities identifying the Jordan singular
supports. The source normal-form and singular-pencil verifiers cover
the classification identities; their PASS results do not replace the
proof of exhaustiveness given in section 1.
