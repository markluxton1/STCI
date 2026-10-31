# Smooth quartic scrolls: the actual conductor schemes

Let an integral quartic X over an algebraically closed characteristic-zero
field have finite normalization S=F0 or F2 polarized by H=C+(e/2+2)f.
The entire conductor is a Cartier anticanonical divisor upstairs and a pure
ACM cubic scheme downstairs. These full-scheme facts, the classification
below and the explicit twisted-cubic normalization are structural inputs,
not a mate exclusion by themselves. The companion
[reduced](QUARTIC_SCROLL_REDUCED_CONDUCTORS.md) and
[nonreduced](QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md) proofs complete this
normalization class for fixed C0. No singular-normalization case is folded
into a smooth-scroll hypothesis.

## 1. Finite duality and the full conductor

### 1.1. A general smooth-scroll conductor lemma

Let nu:S->X be a finite normalization of an integral quartic in P3,
where S is a smooth rational quartic scroll and H=nu*O_X(1). Let I be
the actual conductor on X and Gamma_cond=V(I). Finite absolute duality
gives, as in section 2 of the criterion,

    I=nu_*omega_S,  O_S(-D)=omega_S,
    H^2=4, K_S.H=-6, chi(O_S)=1.

At a closed point of X, a system of parameters of its local ring A is
a system of parameters in each regular local ring of the finite
semilocal normalization B above it. That system is a regular sequence
on B and on the invertible B-module I. Hence I is a maximal
Cohen--Macaulay A-module. The depth lemma in

    0 -> I -> A -> A/I -> 0

shows that Gamma_cond is a pure Cohen--Macaulay curve: its local rings
at closed points have depth at least one. This excludes isolated and
embedded conductor components downstairs as well as the Cartier
argument excluding them upstairs.

Riemann--Roch on S gives

    chi(I(m))=chi(O_S(K_S+mH))=2m^2-3m+1.

The quartic hypersurface sequence gives chi(O_X(m))=2m^2+2. Therefore
the actual downstairs conductor has Hilbert polynomial

    chi(O_Gamma_cond(m))=3m+1.

This calculation includes its entire scheme structure. In particular,
if its support is a smooth twisted cubic Gamma, then its degree already
equals deg Gamma. Its generic multiplicity is therefore one. Its
nilradical, if nonzero, would be a finite-support submodule, contrary
to the depth-one Cohen--Macaulay property. Thus

    Gamma_cond=Gamma as schemes.

The actual upstairs D is Cartier, hence Cohen--Macaulay and pure. Each
of its components maps onto Gamma under the finite map. A nonzero local
parameter of the smooth Gamma therefore avoids every associated prime
of D. Thus p_*O_D is torsionfree over every local DVR of Gamma, hence
p:D->Gamma is finite flat. Its rank is

    (H.D)/(deg O_Gamma(1))=6/3=2.

This proves the exact entire-conductor, smooth-base, rank-two hypotheses
from smooth-scroll normalization plus smooth twisted-cubic nonnormal
support. It needs no assumption that D is reduced or nodal.

There is also a useful intrinsic variant: if the actual Gamma_cond is
integral, its polynomial 3m+1 gives arithmetic genus zero. Normalizing
it gives p_a=g(normalization)+length(normalization quotient), so both
nonnegative terms vanish. It is a smooth rational degree-three curve.
It cannot be planar, since a plane cubic has arithmetic genus one;
hence it is a smooth twisted cubic. The same criterion applies. This
variant does not assert that Gamma_cond is always integral.

## 2. The ACM cubic and its resolution

### 2.1. The ideal sequence and its entire scheme scope

The conductor sequence in the ambient projective space is

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0.

Its first term is the equation of the integral quartic X; the quotient
is exactly I, not the ideal of the reduced conductor support. Since
both H1 and H2 of every line bundle on P3 vanish, twisting gives

    H1(P3,J_Gamma(m)) = H1(S,K_S+mH)

for every integer m. Finite pushforward has no higher cohomology
correction. The separate MCM/depth proof makes Gamma a pure
Cohen--Macaulay curve, and its Hilbert polynomial is 3m+1. Thus no
isolated or embedded conductor component is silently discarded.

### 2.2. Cohomology on both smooth quartic scrolls, for all integers

Write S=F_e with e=0 or 2, minimal section C of square -e,
fiber f, H=C+a f with a=e/2+2, and
K_S=-2C-(e+2)f. Let pi:S->P1 be its ruling.

For a divisor kC+beta f with k>=0, ruling pushforward is

    pi_*O_S(kC+beta f)=sum_(j=0)^k O_P1(beta-j e),
    R1 pi_*O_S(kC+beta f)=0.

The formula has the minimal-section convention C^2=-e; no sign change
between the F0 and F2 calculations is hidden. If k=-1, both direct
images vanish, since every fiber has O_P1(-1) cohomology zero.

For m>=2, K_S+mH has k=m-2 and beta=ma-e-2. Its smallest ruling
summand degree is

    ma-e-2-(m-2)e = m(a-e)+e-2.

This is 2m-2 on F0 and m on F2. All summands therefore have H1=0,
and the higher ruling pushforward vanishes. At m=1 the fiber degree
is -1, so both direct images vanish. For m<=0, surface Serre duality
reduces H1(K_S+mH) to the dual of H1((-m)H). Writing n=-m>=0,
the latter pushforward has degrees na-j e, 0<=j<=n, whose minimum
is n(a-e)>=0; its higher pushforward vanishes. This includes n=0.

Thus H1(J_Gamma(m))=0 for every integer m. Together with purity and
saturation, this proves that the entire conductor coordinate ring is
arithmetically Cohen--Macaulay, not only that the conductor is locally
Cohen--Macaulay.

### 2.3. Minimal generators and the full graded resolution

The same sequence gives H0(J_Gamma(1))=0: K_S+H has fiber degree -1.
At m=2 its pushforward is O_P1(2), so H0(J_Gamma(2)) has dimension
three. There are also no degree-zero generators.

Let R be the saturated homogeneous coordinate ring of Gamma. Its
Krull dimension is two and it is Cohen--Macaulay. Two general linear
forms are an R-regular sequence over the infinite field k. An
Artinian reduction A has length deg Gamma=3. Its initial Hilbert
entries are A0=1 and A1=2, since J_Gamma has no linear forms. These
already sum to its length, so its h-vector is exactly (1,2).

Consequently A is k[u,v]/(u,v)^2. Its three quadratic generators
lift to the three independent quadrics of J_Gamma. Because the two
linear forms are R-regular, the Koszul Tor groups vanish and reduction
identifies J_Gamma/(ell1,ell2)J_Gamma with that reduced ideal. Graded
Nakayama therefore proves that the three quadrics generate the entire
ideal; higher-degree generators are not being guessed from the first
few Hilbert-function values.

Auslander--Buchsbaum gives projective dimension two for R and one
for its ideal. Its Hilbert series is

    Hilb_R(z)=(1+2z)/(1-z)^2,
    Hilb_J(z)=(3z^2-2z^3)/(1-z)^4.

With exactly three degree-two generators, the minimal first syzygy
module is therefore O_P3(-3)^2. This establishes

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

The matrix is a 3-by-2 matrix of linear forms, and Hilbert--Burch
identifies its three maximal minors with the conductor quadrics.
The argument does not assume Gamma integral, reduced or Gorenstein.

### 2.4. What the resolution does not imply

The rank-two cover arguments for a smooth Gamma cannot be applied
merely because Gamma has this resolution. At a non-Gorenstein
conductor point its canonical module is not invertible. The upstairs
conductor algebra need not be locally free of rank two over Gamma;
the retained ordinary triple-line generic algebra is a concrete
warning. An involution on reduced component fields also does not
automatically provide descent through the entire conductor scheme.

The exact sequence under investigation by the degenerate-conductor
agent is

    0 -> O_Gamma -> nu_*O_D -> omega_Gamma -> 0.

It follows by dualizing the conductor sequence on the Gorenstein X:
the conductor I and normalization nu_*O_S are MCM dual modules,
Ext1(O_Gamma,O_X)=omega_Gamma, and the next Ext group of I vanishes.
Modding the normalization sequence by I gives the displayed sequence.
When Gamma is Gorenstein this makes nu_*O_D locally free of rank two,
since an extension of two invertible modules is locally split. At
non-Gorenstein points this conclusion is unavailable.

### 2.5. A false reduced-graph shortcut and its precise obstruction

The naive propagation of constant roots of unity along conductor
components needs to distinguish separate attachment points from a
triple meeting. Consider the local base node R=k[[x,y]]/(xy) and
rank-two algebra

    R[eta]/(eta^2-x-y^2).

Eliminating x embeds D on the smooth (y,eta)-surface as
y*(eta^2-y^2)=0. Its three smooth branches meet at one point. The
branch y=0 covers x=eta^2; the exchanged branches eta=+y and eta=-y
map isomorphically to x=0. A smooth curve alpha*y+beta*eta=0 has
contact one with all three branches for generic coefficients. Its
two exchanged restrictions have constant ratio
(alpha-beta)/(alpha+beta), which may be any nonzero root of unity.
On the stable branch the deck eigenvalue is -1.

Thus zeros consumed by the mutual intersection of the exchanged
line pair can also occur at both attachments to the rest of D.
The claim that f is necessarily nonzero at those attachments is
false without additional geometric information. This local example
is an obstruction to that proof strategy, not an STCI example of C0
and not a claim of global realization by a quartic projection.

The subsequent conic-component argument uses global intersection
degrees and ramification, and survives this local triple meeting.
Its completion and the nonreduced cases are separate proof
obligations; they must not be inferred just from the ACM resolution.

## 3. Actual twisted-cubic singular carriers

### 3.2. The smooth twisted-cubic quartic equation, without slc

After a projective coordinate change write

    Gamma=[s^3:s^2t:st^2:t^3],
    xi1=x0*x2-x1^2,
    xi2=x0*x3-x1*x2,
    xi3=x1*x3-x2^2.

Every quartic singular along Gamma is of the form F=Q(xi1,xi2,xi3)
for a ternary quadratic Q. This is the algebraic equation statement in
[Ducat, section 5.7, equations (5.2)--(5.3), pages 24--25](https://d-nb.info/1317691679/34).
We verify it independently below, so its use does not transfer the
paper's log-canonical classification assumptions.

Use the 35 degree-four exponent vectors in the order

    (e0,e1,e2,4-e0-e1-e2),
    e0=0..4, e1=0..4-e0, e2=0..4-e0-e1.

The derivative-restriction matrix M has 40 rows, indexed by (i,j)
with 0<=i<=3 and 0<=j<=9; j is the s-degree of the restricted
degree-nine derivative. For a column e and weights w=(3,2,1,0),

    M[(i,j),e]=e_i if j=sum(w_k e_k)-w_i, and zero otherwise.

It records the restrictions of all four partial derivatives to Gamma.
The [exact companion verifier](../computations/verify_session_scroll_conductor_compression.py)
exhibits a rank-29 minor with determinant 104509440. Using zero-based
indices, its rows are

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
    20,21,22,23,24,25,26,27,28,30

and its columns are

    0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,
    21,22,23,24,28,29,30,31,32,33,34.

The six products xi_i*xi_j, i<=j, are independent and lie in its kernel.
Thus rank is at most 29 and the displayed nonzero minor proves it is
exactly 29. They span the entire six-dimensional kernel. Since Euler's
identity also gives 4F=sum x_i F_i, the kernel is precisely the space
of quartics singular along Gamma. This is an exact finite-dimensional
proof, not a generic-rank sample.

If F is integral, Q cannot factor into linear factors: their substitutions
would give two nonzero quadratic factors, since the three xi_i are
independent. Therefore Q is a smooth plane conic over k.

### 3.3. A smooth finite normalization of every such integral quartic

The two syzygies are

    x2*xi1-x1*xi2+x0*xi3=0,
    x3*xi1-x2*xi2+x1*xi3=0.

Let Y subset P3 x P2 be the corresponding incidence variety. The matrix
in the P3 variables, at a point [xi1:xi2:xi3] of P2, is

    [xi3, -xi2,  xi1,   0],
    [  0,  xi3, -xi2, xi1].

It has rank two everywhere: if xi1!=0 its last column distinguishes
the rows; if xi1=0 and xi3!=0 its first column does; in the remaining
case xi2!=0 and the rows involve distinct coordinates. Thus Y is a
P1 bundle over P2, and is smooth. Its map sigma:Y->P3 is the blowup
of the smooth twisted cubic. In fact the matrix in the P2 variables is
[x2,-x1,x0; x3,-x2,x1], whose rank-two minors are xi3,-xi2,xi1.
It has rank two off Gamma and rank one everywhere on Gamma. Off Gamma
the syzygies therefore specify the unique point
[xi1(x):xi2(x):xi3(x)]; over Gamma their kernel is a projective line
embedded as a line in P2. Since the smooth P1 bundle Y is irreducible,
this graph over the dense open P3 minus Gamma is dense in Y. Thus Y is
the graph closure of the ideal-generated rational map, equivalently
the blowup, with no omitted incidence component.

Let S be the inverse image of the smooth conic Q under Y->P2. Then S
is a smooth P1 bundle over Q=P1. Off Gamma, sigma|S is an isomorphism
onto X=V(F). Over a point of Gamma, the exceptional fiber maps to a
line in P2, and a smooth conic contains no line. Its intersection with
Q has length two, including tangent intersections. Hence sigma|S is
proper with finite fibers, and is finite. It is birational, so it is
the normalization of the integral X.

Moreover X is smooth off Gamma, since there it is isomorphic to S.
Every point of Gamma is singular on X, as F=Q(xi) has all first
derivatives zero there. Since S is smooth, none of these singular
local rings can already be normal: a finite birational map to a normal
local ring would be an isomorphism. Thus the nonnormal support is
exactly Gamma, with no extra isolated points.

Write H=sigma*O_P3(1)|S and E for the exceptional divisor on Y. The
quadratic leading normal form of F along Gamma is the restriction of
Q to the line of normal directions. It is nonzero, since the smooth
Q contains no line. Thus F has order exactly two along Gamma, the
strict transform S has class 4H-2E, and

    K_Y=-4H+E,  K_S=-E|S.

Intersection gives H^2=4 and H.E|S=6, since H^2.E=0 and H.E^2=-3 on
the blowup of the degree-three curve. Consequently K_S.H=-6.
The finite map makes H ample, and each ruling fiber maps to a secant
line of Gamma, so H has degree one on that fiber. If S=F_e and
H=C_min+a f, then 2a-e=4 and ampleness gives a>e. Hence e is even and
e<4, so e=0 or 2. This is a smooth rational quartic scroll, with its
standard degree-four polarization and torsionfree Picard group.

The general lemma in section 1 now identifies the actual entire
conductor downstairs with this smooth Gamma, and the entire conductor
cover upstairs is finite flat of rank two. The criterion therefore
applies to all such integral quartics, including the non-slc cases.

## 4. The whole nongorenstein cubic schemes

### 4.1. Whole nongorenstein ACM cubic classification

For the 3-by-2 linear Hilbert--Burch matrix M, rank one at a point gives a unit entry and a local codimension-two complete intersection. Rank zero gives a minimal local resolution with last rank two and a canonical module with two generators. Thus the nongorenstein locus is exactly the common zero locus of the linear entries.

Let W be the span of the entries. Its dimension is at least two because the minors have height two. If dim W=4 there is no projective rank-zero locus, so the entire curve is locally Gorenstein and already excluded. If dim W=3, coordinates give W=<x,y,z> and the ideal is the cone, with vertex the w-point, over a length-three scheme Z in P2. The homogeneous ring k[x,y,z]/J is dimension one Cohen--Macaulay, hence J is saturated. Its Hilbert series is (1+2t)/(1-t), and J has no linear element. Saturation therefore makes Z noncollinear; merely knowing h0(O_Z(1))=3 would not suffice.

A length-three scheme on a smooth surface has three distinct points, one double point plus a distinct point, a curvilinear length-three point, or a length-three point with two-dimensional square-zero maximal ideal. Noncollinearity respectively means the points are noncollinear, the third point misses the double point's tangent line, or the curvilinear point has nonzero second-order departure from its tangent line. Projective coordinate changes and scaling give the four cone ideals

    (xy,xz,yz), (y^2,xy,xz), (x^2,xy,y^2-xz), (x^2,xy,y^2).

The first is reduced and already excluded. For the last case only two linear variables are needed. Conversely, if dim W=2, the three independent quadratic minors span Sym^2(W), giving exactly the final ideal. Independence follows from the Hilbert--Burch resolution and its three minimal quadratic generators. These arguments exhaust the whole nongorenstein ACM cubic schemes over the stated field.

## 5. A realizable cusp-plus-line control

### 5.6. Realizable cusp-plus-line projection: a shield against a false shortcut

The residual pattern is not excluded merely because its two reduced
primes map isomorphically to a line. There is a concrete finite birational
projection of F2 with H=C+3f:

    x0=Y a,
    x1=Y b+X(r a^3+s a^2 b),
    x2=X a b^2,
    x3=X b^3,                       r != 0.

Here the six full H-sections are Ya,Yb,Xa^3,Xa^2b,Xab^2,Xb^3.
These four sections have no base point. H is ample, so the morphism has
no contracted curve and is finite onto its image. On the dense open
x2*x3 !=0, b/a=x3/x2 and the remaining fiber coordinate is recovered;
the map is birational. Its integral quartic image has equation

    x1*x2*x3^2-x0*x3^3-r*x2^4-s*x2^3*x3=0.

Its actual conductor has not been asserted here solely from this equation.
The family is recorded to prevent the invalid claim that every such
projection must be immersive along the ruling fiber b=0. In the chart
a=Y=1, put t=b/a, u=Xa^2/Y. Then

    nu(t,u)=[1:t+u(r+s t):u t^2:u t^3].

Along t=0 its Jacobian has rank one at generic u: the u-derivative is
(r,0,0), and the t-derivative is (1+s u,0,0). This is precisely the
cuspidal differential addressed by section 5.

One can verify the power obstruction explicitly. A general H-section in
this chart is h=alpha+beta t+u(P+Qt+Rt^2+St^3). Full singleton zeros on
the two identified reduced primes force alpha=0. At fixed image line
coordinate rho=t+u(r+s t), write u=(rho-t)/(r+s t). The coefficient of t
in h is beta-P/r+rho*(Q/r-Ps/r^2). Every ambient mate has zero coefficient
of t, because x1=rho is held fixed and x2,x3 begin with t^2,t^3.
For h^n, its nonzero generic constant makes this coefficient vanish only
when P=beta*r and Q=beta*s. Then

    h=beta*x1+R*x2+S*x3

is itself a pulled-back ambient hyperplane, incompatible with C0. The
generic differential lemma is the invariant version of this calculation.

## Scope and characteristic

These structural proofs keep the actual conductor, not its reduction or
Jacobian scheme. The displayed integral models can be considered in other
characteristics, but their integrality, finite-birational map and generic
separability must be checked there. The duality and ACM calculations apply
under their stated geometric hypotheses; the characteristic-zero all-mate
conclusion also uses the separate descent and differential arguments.
The inherited full proofs had independent reviews; this thematic replacement was independently compared with its source
proofs and accepted before the duplicated blocks were removed.
