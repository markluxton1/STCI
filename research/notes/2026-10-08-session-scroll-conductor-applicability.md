# Entire conductor verification for the smooth twisted-cubic quartic class

Date: 2026-10-08. Status: **PROVED structural applicability**, with one
small exact linear-algebra certificate. No semi-log-canonical assumption
is made. This note does not classify every nonnormal quartic.

**Theorem.** Over an algebraically closed characteristic-zero field,
an integral quartic surface singular along a smooth twisted cubic cannot
be a carrier in a set-theoretic complete-intersection presentation of
C0=[s^4:s^3t:st^3:t^4], in any mate degree.

The proof verifies the precise hypotheses of the
[conductor compression criterion](2026-10-08-session-irreducible-conductor-compression.md).
It includes reduced, reducible, nodal, and nonreduced upstairs conductor
schemes inside this class. It does not infer a classification from
Ducat's semi-log-canonical Table 3.

## 1. A general smooth-scroll conductor lemma

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

## 2. The smooth twisted-cubic quartic equation, without slc

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

## 3. A smooth finite normalization of every such integral quartic

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

## 4. What remains outside this theorem

No assertion is made here that every smooth normalized quartic scroll
has smooth twisted-cubic nonnormal support. A reducible, nonnormal, or
nonreduced downstairs conductor remains outside this application. A
singular normalization also remains outside the argument, as do the
line/conic conductor classes with other sectional genera and possible
lifted curves meeting normalization singularities. The theorem proves
an entire explicit nonnormal class has no mate for C0; it does not
resolve the unrestricted STCI problem or exhaust all quartic carriers.

Independent checks: the Hilbert/CM conductor-scheme argument and the
rank-two descent criterion were separately checked by the
normal-global-adversarial agent. The equation-space certificate is
reproducible by the companion verifier, whose exact determinant is
recorded above. Its finite matrix verifies only that equation-space
step; the all-degree mate exclusion is the structural conductor proof.
