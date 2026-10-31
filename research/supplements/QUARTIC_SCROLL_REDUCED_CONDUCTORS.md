# Smooth quartic scrolls: every reduced conductor excludes a mate

Use the [whole conductor structure](QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md).
A mate on an actual integral quartic with smooth F0/F2 normalization gives
a smooth lifted c~H, singleton full inverse support, and a descended power
of a section cutting c. The reduced ACM cubic conductor is either a smooth
twisted cubic, a conic plus a line, or three lines (including a concurrent
nongorenstein vertex). The following complete case proofs retain the
upstairs nonreduced schemes even though the downstairs conductor here is
reduced. The fixed curve is C0 in characteristic zero; the companion
[nonreduced proof](QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md) treats every
remaining actual conductor scheme.

## 1. Integral reduced conductor

### 1.1. Precise theorem accepted by this audit

Let k be algebraically closed of characteristic zero. Suppose X is an
integral quartic surface in P3, its finite normalization nu:S->X is a
smooth rational quartic scroll, and C0 is the fixed smooth rational
quartic [s^4:s^3t:st^3:t^4]. Assume X is regular at the generic point
of C0. Write H=nu*O_X(1).

Let I be the **actual entire conductor ideal**, and define

    Gamma=Spec_X(O_X/I),   D=Spec_S(O_S/I*O_S).

Assume Gamma is a smooth twisted cubic and the induced map
rho:D->Gamma is finite flat of degree two. Then **X admits no STCI
mate for C0 in any degree**. Reducedness of D is unnecessary under
these exact assumptions.

The original proposed theorem assumed D reduced. Both its integral
and reducible cases are accepted. The [nonreduced-conductor proof](QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md#4-why-the-reduced-conductor-is-insufficient) proves the remaining
nonreduced case. The characteristic-zero and rank-two assumptions
are used explicitly; the statement does not cover thicker conductor
algebras or a singular, reducible or nonreduced Gamma.

### 1.2. Whole support and the global section f

If a mate G of degree b exists, its pullback is a nonzero section of
O_S(bH) whose zero set is the entire inverse image of C0. Over the
generic point of C0 normalization is an isomorphism. There is therefore
one curve component c finite birational over C0. Since C0 is smooth,
this map is an isomorphism. Any additional inverse-image points would
be isolated components and cannot be the support of a nonzero Cartier
divisor on S. Thus the mate forces the entire inverse support to be c.

In particular every normalization fiber above a point of C0 has one
point, and c is a smooth embedded curve. If div(nu*G)=n*c, then
intersecting with H gives 4n=4b, so n=b. The Picard group of a smooth
rational scroll is free abelian. Consequently b(c-H)~0 implies c~H.
There is a section f in H0(S,O_S(H)) whose divisor is precisely c.
The ratio nu*G/f^b has zero divisor, hence is a nonzero constant on
the normal proper integral S. Rescale G to arrange nu*G=f^b.

This argument uses the whole inverse support. A section with support
c alone could not suffice if there were other isolated inverse-image
points. No numerical-equivalence cancellation on an arbitrary
nonnormal surface is used.

### 1.3. Actual conductor descent and the rank-two algebra

For a finite normalization A subset B with conductor I, one has

    A = B x_(B/I) (A/I).

Indeed an element of B whose reduction modulo I comes from A differs
from an element of A by an element of I, and therefore belongs to A.
This gives the exact conductor square on sheaves. After tensoring
with O_X(d), a section upstairs descends precisely when its restriction
to the entire D agrees with a section on Gamma. Passing to the
reduced support alone would not justify this step.

In the present Gorenstein quartic setting, finite duality identifies
the conductor as a B-module with omega_S: Hom_A(B,A) is the conductor
inside the common function field, and omega_X is trivial. Since S is
smooth, the conductor is invertible and D is an effective Cartier
divisor with D~-K_S. This also rules out an additional isolated
conductor defect on S. Adjunction gives p_a(D)=1, or equivalently
chi(O_D)=0. The rationality of S and the exact sequence
0->omega_S->O_S->O_D->0 give H0(O_D)=k.

Identify Gamma with P1. In characteristic zero the trace map splits
the finite flat rank-two algebra:

    rho_*O_D = O_Gamma + N,

where N is an invertible tracefree module. Euler characteristic gives
deg N=-2, so N=O_P1(-2). A tracefree local generator eta satisfies
eta^2=Delta, with Delta a global section of O_P1(4). The involution
fixes O_Gamma and negates eta. Because H|D=rho*O_Gamma(1) and Gamma
is a twisted cubic, restrictions of f are sections of rho*O_P1(3).

All identifications use the actual conductor map, not a chosen
parametrization with an unspecified descent subalgebra.

### 1.4. Integral reduced D: quadratic compression

The deck action on rho*O_P1(3) is canonical, coming from the downstairs
line bundle. Since f^b descends, it is invariant under this action.
The restriction of f to D is not zero: its divisor c does not contain
a conductor component, since C0 is generically regular on X.

On the integral D the quotient r=sigma(f)/f is a rational function
and r^b=1. Over algebraically closed k, the polynomial T^b-1 splits
into distinct linear factors; an element of the function field
satisfying it is a constant root of unity zeta. Applying sigma twice
gives zeta^2=1. Hence f^2 is invariant on all of D. The rational
equality extends as equality of regular sections because D is
integral and reduced; a nodal or cuspidal D creates no gap here.

The invariant algebra of the rank-two cover is O_Gamma, so f^2|D
comes from a section of O_P1(6). The conductor square therefore
descends f^2 to a section of O_X(2). The hypersurface restriction
sequence and H1(P3,O(-2))=0 lift it to an ambient quadric Q.
Finite surjectivity shows V(Q) on X has exactly support C0.

The fixed C0 lies on its unique smooth quadric q and has class (1,3)
up to swapping the rulings. Thus Q is q up to a scalar. The quartic
equation of X restricts to class (4,4) on q. A divisor supported
only on C0 would have class n(1,3), which cannot equal (4,4).
This is the required contradiction in every mate degree.

### 1.5. Reducible reduced D: the actual gluing modulus

Reducibility of the reduced double cover means its generic algebra
splits. Thus Delta is the square of a rational section of O_P1(2).
The square root has no poles, because Delta is regular, so

    Delta=q2^2,   q2 in H0(P1,O(2)), q2!=0.

The two components D1,D2 each map isomorphically to Gamma. Under
the branch maps eta=+q2 and eta=-q2, their local algebra is the pairs
of regular functions congruent modulo q2. This follows explicitly:

    a+b*eta |-> (a+b*q2, a-b*q2),

whose image is exactly those pairs with difference divisible by q2,
because 2 is invertible. Hence the two smooth branches meet at each
zero of q2 with intersection multiplicity m=ord(q2), either one or
two. No ordinary-pinch or reduced-ramification assumption is made.

Let the restrictions of f be s,t in H0(P1,O(3)). Neither is identically
zero. Descent of f^b implies s^b=t^b, so t=zeta*s for a constant
b-th root of unity zeta. If zeta=1, f|D itself descends and the
conductor square gives an ambient hyperplane containing C0, impossible.

If zeta!=1, the gluing condition forces

    s=q2*ell,   ell in H0(P1,O(1)), ell!=0.

The single zero a of ell must be a zero of q2. Otherwise f vanishes
at two distinct points of the normalization over the same point of
Gamma; both points lie on c, contradicting c->C0 being an isomorphism.
At a, each branch restriction of f has order m+1.

### 1.6. The local contact contradiction

Two smooth branches D1,D2 on a smooth surface with intersection
multiplicity m admit completed regular coordinates (t,w) in which
D1 is w=0 and D2 is w=t^m*u(t), with u(0)!=0. The parameter t
may be chosen as a lift of the common Gamma parameter, because
its restrictions to both branches are uniformizers.

Let f also denote a local equation of c. If f has order m+1 on
both branches, then f(0,0)=0 and f_t(0,0)=0, since m+1>=2.
Smoothness of c forces f_w(0,0)!=0. But Taylor expansion gives

    f(t,t^m*u(t))-f(t,0)
      =t^m*u(0)*f_w(0,0) + terms of order greater than m.

The left side has order at least m+1 and the right side has order
exactly m, a contradiction. Thus no smooth third branch can have
contact greater than m with both D1 and D2. This proves the claimed
local obstruction for both a node (m=1) and a tangency (m=2).

This lemma does not say that conductor contact is bounded for every
smooth image curve. The retained degenerate-cusp counterexample permits
large contact with one branch while contact with the other stays at
the mutual branch intersection multiplicity. The present argument
requires both branch contacts to increase simultaneously, as forced
by the global section pair (s,zeta*s).

## 2. Conic-plus-line support

### 2.1. The carrier class and exact conductor scheme

Work over an algebraically closed field of characteristic zero. Let
X be an integral quartic surface with finite normalization nu:S->X,
where S is a smooth rational quartic scroll polarized by
H=nu*O_X(1). Suppose its entire nonnormal support is the union of a
smooth conic A and a line B meeting in scheme length one.

Then **X cannot participate in an STCI presentation of fixed C0 in
any mate degree**. The hypotheses do not assume ordinary pinches,
reduced upstairs conductor, or semi-log-canonical singularities.

Let I be the actual conductor, Gamma=V(I) downstairs and D=V(I O_S)
upstairs. The audited ACM lemma gives Gamma pure Cohen--Macaulay with
Hilbert polynomial 3m+1. The support A union B has degree three,
so its generic multiplicities are one. Cohen--Macaulay purity rules
out a nilradical supported at finitely many points. Therefore the
actual Gamma is the reduced A union B, with no undisclosed thickening.
Its meeting is a node: B is outside the plane of A, and the two
smooth tangent directions are distinct. Gamma is Gorenstein.

Finite duality gives D~-K_S as an effective Cartier divisor, and

    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0,
    p=nu|D.

Here is a direct verification of the second sequence. Over the
Gorenstein X, I=Hom_X(nu_*O_S,O_X). Both modules are maximal
Cohen--Macaulay and double duality identifies Hom_X(I,O_X) with
nu_*O_S. Dualizing 0->I->O_X->O_Gamma->0 gives
0->O_X->nu_*O_S->omega_Gamma->0; the next Ext group of I vanishes.
Quotienting by the common conductor I gives the displayed sequence.

Since omega_Gamma is invertible, this extension makes p_*O_D locally
free of rank two. Thus p is finite flat, including at the node.
Trace in characteristic zero splits its algebra as O_Gamma plus an
invertible tracefree module L, with eta^2=Delta locally. The splitting
also identifies L with omega_Gamma. No flatness of nu:S->X itself is
assumed.

### 2.2. Curve support and every conductor prime

The mate hypothesis gives the entire inverse image of C0 with reduced
support one embedded smooth rational curve c isomorphic to C0. A
nonzero Cartier divisor upstairs cannot have extra isolated support.
Degree gives div(nu*G)=n*c for a degree-n mate. The scroll Picard
group is free, so c~H; choose f in H0(S,H) with div(f)=c. Rescaling
the mate gives nu*G=f^n.

On the rational S, every nonzero proper effective divisor E<D obeys

    H1(O_E)=H2(O_S(-E))=H0(O_S(E-D))^*=0.

The last equality follows because D-E is nonzero effective and its
negative ideal has no global section on the proper connected S.
Every conductor prime is proper: D maps onto both A and B, so D
cannot be an integral reduced single prime. Consequently every prime
of D is a smooth rational curve, even when other components of D
are nonreduced. Moreover H0(O_D)=k by the anticanonical sequence,
so its support is connected. Prime adjunction gives

    E.(D-E)=2.

At the generic point of A, the rank-two algebra has total length two.
Writing a_E for a conductor multiplicity and d_E for the degree of
the reduced prime's map to A, one has sum a_E*d_E=2. There are
exactly three possibilities: one reduced degree-two cover; two
distinct reduced degree-one components; or one doubled degree-one
component. The following sections exclude all three.

### 2.3. An irreducible degree-two conic cover

Suppose a prime E maps to A with degree two and multiplicity one.
It is P1 and its characteristic-zero map E->A=P1 is a separable
double cover. Riemann--Hurwitz gives exactly two simple ramification
points. Also H.E=2*deg A=4, hence c.E=4.

Every point of c intersecting E must be a ramification point of the
cover. At an unramified point there would be a second distinct
normalization point above the same point of A; the full inverse
support condition and c->C0 being an isomorphism forbid that.

At a ramification point, dnu annihilates the tangent line of E in
the ambient P3 because the derivative of E->A vanishes. The image
C0 is smooth and nu|c is an isomorphism, so dnu does not annihilate
the tangent line of c. These lines on the smooth surface S are
therefore different, and the intersection of c with E is transverse.
Each of the two possible points contributes one, giving c.E<=2,
contrary to c.E=4.

This derivative argument remains valid when the ramification point
also lies on other conductor components. It assumes no ordinary
pinch model and survives a triple meeting upstairs.

### 2.4. A pair of degree-one conic components

Suppose E and E' both map isomorphically to A and appear with
multiplicity one. Each has H-degree two. Descending f^n identifies
its two restrictions after these isomorphisms with A. Their quotient
in k(A) has n-th power one, so they are nonzero constant multiples
of one another. In particular their zero orders over each point of
A agree.

Every zero of f on E must lie on E intersection E'. Otherwise the
matching zero on E' would be a distinct point of c in the same
normalization fiber, impossible. At a common point let m be the
mutual branch intersection multiplicity and v the common zero order
of f. Both branches are smooth. The Taylor lemma in the conductor
audit shows v<=m: a smooth third branch cannot have contact greater
than m with both of them.

Summing gives

    2=c.E <= E.E' <= E.(D-E)=2.

Hence E.E'=2 and E has no intersection with any other component
of D. The symmetric equality for E' isolates the pair from the
remaining conductor. There must be remaining conductor above B,
contradicting connectedness of D. Multiplicities on those remaining
components cannot change this contradiction: every contribution to
E.(D-E) is nonnegative.

### 2.5. The doubled conic component

Suppose D contains 2E with E mapping isomorphically to A. Then
H.E=2. The two smooth rational quartic scrolls are

    F0: H=C+2f,   -K=2C+2f,
    F2: H=C_min+3f,   -K=2C_min+4f.

On F2 there is no irreducible H-degree-two curve. A prime different
from C_min with class alpha*C_min+beta*f satisfies beta>=2alpha
by nonnegative intersection with C_min, and H-degree alpha+beta.
If alpha>=1 this is at least three. If alpha=0, an effective divisor
is a sum of ruling fibers, and its only primes have degree one.
The prime C_min itself has degree one. Thus F2 is impossible here.

On F0 a degree-two prime is a section in class C: the alternatives
in 2alpha+beta=2 with alpha,beta nonnegative are C and 2f, and the
latter is not prime. Consequently D-2E has class 2f, and is either
F1+F2 for two distinct fibers or 2F for one fiber.

In the first case each Fi has H-degree one, maps isomorphically to B,
and intersects E in one point. The points E intersection F1 and
E intersection F2 are distinct, but both map into A intersection B,
the same node. This contradicts E->A being an isomorphism. Hence

    D=2E+2F.

The rank-two conductor algebra is generically nonreduced on both
components of the reduced Gamma. Its trace discriminant Delta
therefore vanishes generically on both and is identically zero.
Thus p_*O_D=O_Gamma plus L*eta with eta^2=0.

Write f|D=a+b*eta, with a a section of O_Gamma(1) and b a section
of L tensor O_Gamma(1). The section a is generically nonzero on
both components, since c is neither E nor F. It is therefore a
nonzerodivisor on the reduced Cohen--Macaulay Gamma. Descent of the
mate power gives

    (a+b*eta)^n=a^n+n*a^(n-1)*b*eta,
    n*a^(n-1)*b=0.

Characteristic zero and invertibility of L force b=0. Thus f itself
descends through the entire conductor square to O_X(1), and lifts
to an ambient hyperplane containing C0. This contradicts the
nondegeneracy of C0.

## 3. Three-line support

### 3.1. Exact theorem and inherited inputs

Let X be an integral quartic in P3 over an algebraically closed
characteristic-zero field with smooth rational quartic-scroll
normalization nu:S->X and H=nu*O_X(1). Suppose its actual entire
downstairs conductor Gamma is reduced and has three distinct lines
as its components. Then X has no STCI mate for fixed C0 in any degree.

The inherited structural inputs, proved in the separate audits, are:

    Gamma is pure ACM with Hilbert polynomial 3m+1;
    D~-K_S is the actual upstairs Cartier conductor;
    0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0;
    every proper conductor prime E<D is a smooth rational curve.

For the last input, the direct rational-surface cohomology proof is
H1(O_E)=H0(O_S(E-D))^*=0. It remains valid when D is nonreduced.
At each generic point of the reduced Gamma, its canonical module has
dimension one over its function field. Thus the exact sequence gives
the upstairs algebra dimension two there. If a conductor prime E
maps to that line with degree d and has multiplicity a in D, its
contribution is a*d and these contributions sum to two. In particular
H.E=d<=2. This generic statement does not assume local freeness at
a non-Gorenstein point of Gamma.

If a mate exists, the full inverse support is one smooth c isomorphic
to C0 and every normalization fiber over C0 is a singleton. Picard
torsionfreeness gives c~H and a global f with div(f)=c, whose mate
power f^n descends. Every conductor prime is different from c.

### 3.2. A split pair of ruling fibers is impossible before trace

Two distinct ruling fibers F,F' are disjoint and each has H-degree
one. If both map isomorphically to the same conductor line L,
descent of f^n makes their restrictions have equal n-th powers as
sections of O_L(n). Both restrictions are nonzero sections of O_L(1).
Their ratio is a constant root of unity, so they have the same zero
on L. Upstairs these zeros are two distinct points because F and F'
are disjoint. Both belong to c, contradicting the singleton-fiber
condition. This uses restrictions on L, and is valid even when Gamma
has a concurrent non-Gorenstein point.

### 3.3. F0 forces a chain and then too many intersections with one fiber

On F0 take H=C+2f and D~2C+2f. The only H-degree-one primes are
ruling fibers f; the only H-degree-two primes are sections in class C.
Indeed a prime class alpha*C+beta*f has alpha,beta nonnegative and
H-degree 2alpha+beta; a multiple of a fiber is not prime.

The coefficient two of C in D requires two distinct horizontal
sections C1,C2 with multiplicity one. A doubled section would have
generic cover contribution 2*2=4 over its image line, impossible.
Each Ci maps with degree two to a different base line Li. They
cannot cover the same line, which would likewise have total degree
four. The remaining divisor of class 2f is supported over the third
line L0. Section 2 rules out two distinct fibers, leaving

    D=C1+C2+2F.

The doubled F maps isomorphically to L0. The points Pi=Ci intersection
F are distinct, so their images pi on L0 are distinct. Thus the
three lines cannot be concurrent under the mate hypothesis. They
also cannot form a planar triangle, whose Hilbert polynomial is
3m rather than 3m+1. Hence L1 and L2 are disjoint, and Gamma is a
nodal chain with distinct junctions p1,p2.

Only now is the whole conductor algebra made locally free of rank
two: the chain is Gorenstein, so the extension by omega_Gamma is an
extension of invertible modules. Trace gives the local algebra
O_Gamma[eta]/(eta^2-Delta). Its discriminant vanishes generically on
L0, since the corresponding conductor component is 2F, hence
vanishes identically on that line and at both junctions. Its fiber
at either junction is k[eta]/(eta^2), supported at one point.

Consequently the degree-two cover Ci->Li is ramified at Pi; an
unramified cover would have a second distinct point in that fiber.
It has exactly two simple ramification points in characteristic
zero. Full inverse support places all c intersection Ci at those
points, and smoothness of C0 forces transverse intersection there:
dnu annihilates the tangent of Ci at a ramification point and cannot
annihilate the tangent of c. Since c.Ci=H.Ci=2, c must pass through
both ramification points, including Pi.

It follows that c intersects F at the two distinct points P1,P2,
giving c.F>=2, contrary to c.F=H.F=1. This excludes the F0 case.

### 3.4. F2 forces a chain and then a nilpotent descent contradiction

On F2 take H=C_min+3f and D~2C_min+4f. The only primes of
H-degree at most two are C_min and ruling fibers, all of degree
one. For any prime distinct from C_min with class alpha*C_min+beta*f,
nonnegative intersection with C_min gives beta>=2alpha. If alpha
is positive its H-degree alpha+beta is at least three; if alpha is
zero it is a fiber. There is no degree-two prime.

Therefore D contains 2C_min, mapping isomorphically to one base line
L0 with generic conductor multiplicity two. The remaining divisor
of class 4f is divided between the other two lines with generic
contribution two on each. Split fiber pairs are impossible by
section 2, so

    D=2C_min+2F1+2F2,

where F1,F2 are distinct fibers over distinct base lines L1,L2.
Their intersections with C_min are distinct, and C_min->L0 is an
isomorphism. The junctions on L0 are therefore distinct. As in
section 3, Gamma must be a nodal chain rather than concurrent lines
or a planar triangle.

The rank-two algebra is locally free on this Gorenstein chain, and
its trace discriminant vanishes generically on all three lines.
Because Gamma is reduced, Delta=0 globally. Thus its algebra is
O_Gamma plus an invertible tracefree nilpotent module L*eta,
eta^2=0. If f|D=a+b*eta, the section a is generically nonzero on
every component because c is not a conductor prime. It is a
nonzerodivisor on the reduced Cohen--Macaulay Gamma. Descent of f^n
forces n*a^(n-1)*b=0 and therefore b=0 in characteristic zero.

The entire conductor square descends f itself to O_X(1), producing
an ambient hyperplane containing C0. Its nondegeneracy gives the
contradiction. This excludes F2.

### 3.5. Corollary: all reduced downstairs conductors on smooth scrolls

Together with the separate smooth twisted-cubic and conic-plus-line
theorems, the three-line result yields:

> An integral quartic with smooth rational quartic-scroll normalization
> whose **actual downstairs conductor is reduced** admits no STCI
> mate for fixed C0 in characteristic zero, in any degree.

To see that the cases exhaust this reduced scope, Gamma has degree
three and arithmetic genus zero. If integral, normalization and the
genus formula force it smooth rational; it cannot be a plane cubic,
so it is a smooth twisted cubic. If reducible with two components,
their degrees are two and one, hence a smooth conic and a line. The
genus polynomial forces their intersection scheme length to be one.
If it has three components they are distinct lines, treated above.
There are no remaining positive degree partitions of three.

The corollary's reducedness assumption is **downstairs only**.
Upstairs multiplicities were retained in both scroll cases and in
the conic-plus-line proof. Nonreduced downstairs cubic schemes,
such as multiple-line conductor structures, remain outside it.
At their non-Gorenstein points the normalization algebra may not
be locally free of rank two. No involution or nilpotent-power
argument is transferred there without a separate proof.

## Characteristic boundary

Full inverse support and divisor classes are not the characteristic-zero
obstruction by themselves. These proofs use finite separable conductor
covers, trace/involution when two is invertible, and cancellation after
differentiating a mate power of degree nonzero in the field. Characteristic
p dividing that degree invalidates the cancellation, and Frobenius can
remove nilpotent phase obstructions. Thus no all-positive-characteristic
scroll or fixed-C0 exclusion is claimed. These exact characteristic-zero
case arguments reuse their independent reviews, independently confirmed for this consolidated replacement.
