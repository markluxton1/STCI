# Smooth normalized quartic scrolls: conductor descent and mate compression

Date: 2026-10-08. Status: **PROVED conditional structural exclusion**,
independently audited from the proposed conductor argument. The result
uses the actual entire conductor scheme, a smooth twisted-cubic
downstairs conductor, and a finite flat cover of rank two. It is not a
classification of all nonnormal quartic carriers. No canonical frontier
file is edited here, and no novelty claim is made.

The initial assigned target was an integral reduced upstairs conductor.
Sections 1--5 prove that target, including nodal conductors. Section 6
audits the reduced reducible extension. Section 7 records a separately
audited rank-two nonreduced extension, whose restrictive hypotheses
must remain attached to it.

## 1. Exact statement and support hypotheses

Work over an algebraically closed field of characteristic zero. Let
X be an integral quartic hypersurface in P3. Let nu:S->X be its finite
normalization, with S a smooth rational quartic scroll and
H=nu*O_X(1). In particular,

    H^2=4, K_S.H=-6, and Pic(S) has no torsion.

Let I be the actual conductor ideal, let Gamma=V(I) on X, and let
D=V(I O_S) on S. Assume:

1. Gamma, with this exact scheme structure, is a smooth twisted cubic;
2. p=nu|D:D->Gamma is finite flat of rank two;
3. initially, D is integral and reduced.

Then X cannot occur in a set-theoretic complete-intersection
presentation of

    C0=[s^4:s^3t:st^3:t^4] in P3,

with a mate of any positive degree. The same conclusion holds if D is
reduced reducible (section 6), or nonreduced under these unchanged
rank-two finite-flat hypotheses (section 7).

The exact conductor is necessary: replacing it by its reduced support
can discard compatibility conditions required for descent. The
smoothness and rank assumptions on Gamma and p are also substantive.

The normalization is an isomorphism off Gamma. Since C0 has degree
four and Gamma has degree three, C0 is not contained in Gamma, so X is
regular at the generic point of C0. If a mate G of degree n exists,
its pullback is a nonzero effective Cartier divisor on the smooth
surface S. The full support of that divisor is (nu^-1 C0)_red. There
is a unique curve component c, finite birational over C0, and it is
isomorphic to C0 since C0 is normal. A principal divisor on a smooth
surface cannot have isolated support points. Therefore

    (nu^-1 C0)_red=c,

and every normalization fiber above C0 consists of exactly one point.
This is a full-fiber condition, not merely a statement about the
generic fiber along C0. It is the same support argument as in the
[earlier normalization note](2026-10-07-session-nonnormal-structural-progress.md).

If div(nu*G)=m c, intersection with H gives 4m=4n, so m=n. Since c
is Cartier and Pic(S) has no torsion, n(c-H)~0 implies c~H. Choose
f in H0(S,O_S(H)) with div(f)=c. Then

    nu*G=lambda f^n,  lambda in k*,

because their quotient has neither zeros nor poles on the projective
integral surface S. This global constant-unit conclusion is stronger
than a local affine-unit statement.

## 2. The actual upstairs conductor has no isolated defects

For completeness, the conductor is an invertible ideal on the smooth
normalization in this setting. This does not require the normalization
morphism itself to be flat.

Locally let A be a domain and B its finite normalization in the same
function field. Every A-linear homomorphism B->A becomes multiplication
by a scalar after tensoring with that function field. Evaluation at 1
therefore identifies

    Hom_A(B,A)={a in A : aB subset A}=I.

Finite absolute duality identifies Hom_A(B,omega_A) with the canonical
module of B. On the present surfaces, both are Cohen--Macaulay, X is
Gorenstein, and the dualizing sheaves have the same absolute dimension
shift. Thus, globally as an O_S-module,

    I O_S = omega_S tensor nu*(omega_X)^(-1).

Since X is a quartic hypersurface in P3, omega_X=O_X. Hence

    I O_S is isomorphic to omega_S,
    O_S(-D) is isomorphic to omega_S,  and D~-K_S.

In particular the actual conductor is an effective Cartier divisor
on S; there is no residual isolated or embedded zero-dimensional
conductor ideal upstairs. Reducedness of its support alone still does
not prove that this Cartier divisor is reduced.

The finite absolute-duality step is supported by the
[Stacks finite-map dualizing-complex lemma](https://stacks.math.columbia.edu/tag/0AX0)
and its [Cohen--Macaulay concentration criterion](https://stacks.math.columbia.edu/tag/0AWQ).
These are used for absolute dualizing complexes; no formula requiring
a flat Cohen--Macaulay morphism is applied to nu.

Also H.D=6, whereas H.c=4, so c is not D in the integral case. In the
rank-two reducible or nonreduced cases, each reduced component maps
isomorphically to Gamma and has H-degree three; c is not any such
component either. Consequently f|D is generically nonzero on every
reduced component used below.

## 3. The double-cover involution remains exact at nodes

Because 2 is invertible and p is finite flat of rank two, trace splits
the algebra as

    p_*O_D=O_Gamma direct-sum L,

where L is its trace-zero line bundle. Cayley--Hamilton for multiplication
by a trace-zero local generator eta gives eta^2=Delta in O_Gamma.
The map sigma(eta)=-eta, sigma(1)=1 is an algebra involution. Its fixed
algebra is exactly O_Gamma, including at branch points and nodal points
of D. This equality is scheme-theoretic; it is not inferred just from
the behavior on closed points.

The restricted hyperplane bundle is canonically

    O_S(H)|D=p*O_Gamma(1).

Here O_Gamma(1)=O_P1(3), since Gamma is a twisted cubic. The pullback
line bundle has the canonical sigma action. Projection formula and the
trace splitting show that its invariant sections, and those of every
tensor power, are exactly the sections pulled back from Gamma.

For integral reduced D, the same fixed-ring conclusion also follows
from normality of Gamma: an invariant section belongs to k(Gamma), is
integral over O_Gamma, and hence belongs to O_Gamma. The trace-algebra
proof makes explicit why a node upstairs introduces no additional
descent obstruction under the stated smooth-base hypotheses.

## 4. Integral reduced D forces a quadratic descended mate

The section nu*G descends from X, so its restriction to D is sigma
invariant. Thus, in the function field of the integral reduced curve D,

    (sigma(f|D)/(f|D))^n=1.

The roots of T^n-1 lie in k. A field element satisfying this polynomial
is one of those constants, so sigma(f|D)=zeta f|D for zeta in k*. Applying
sigma twice gives zeta^2=1. It follows that (f|D)^2 is sigma invariant.

An equality of rational sections of a line bundle on an integral
reduced curve is an equality of global regular sections when both
sides are regular: the line bundle is torsionfree. Thus this argument
is valid when D is nodal; it neither deletes the nodes nor replaces D
by its normalization. Consequently f^2|D is the pullback of a section

    t_Gamma in H0(Gamma,O_Gamma(2)).

If zeta=1, f itself descends by the same argument, yielding the even
stronger impossible hyperplane in section 6. The quadratic compression
works uniformly for zeta=1 and zeta=-1.

## 5. Entire-conductor gluing and the C0 contradiction

The conductor square is exact for every finite normalization. Locally,
with I its conductor,

    A = B fiber-product_(B/I) (A/I).

Indeed an element of B whose residue is in A/I differs from an element
of A by an element of I subset A. Twisting the sheaf identity by the
invertible O_X(2) gives the kernel sequence

    0 -> O_X(2) -> nu_*O_S(2H) direct-sum O_Gamma(2)
      -> nu_*O_D(2H).

The matching pair (f^2,t_Gamma) therefore gives a global section t_X of
O_X(2). This is direct gluing by a kernel equality, so no H1 vanishing
on the conductor or normalization is needed. Its pullback is f^2.

The hypersurface sequence

    0 -> O_P3(-2) -> O_P3(2) -> O_X(2) -> 0

and H1(P3,O(-2))=0 lift t_X to an ambient quadric Q. Finiteness and
surjectivity of nu, together with div(f^2)=2c, show

    (X intersect V(Q))_red=C0.

This contradicts the elementary quadric geometry of C0. Substituting
its displayed parametrization into the ten quadratic monomials gives
nine distinct degree-eight monomials, with the sole coincidence
x0*x3=x1*x2. Thus the unique quadric containing C0 is

    q=x0*x3-x1*x2,

which is smooth. On q=P1xP1, C0 has bidegree (1,3), after choosing the
order of the two factors. The restriction of an integral quartic X to
q is nonzero and has divisor class (4,4). A divisor supported only on
C0 would have class m(1,3), which cannot equal (4,4) for any positive
integer m. Hence the descended quadric cannot exist.

## 6. Reduced reducible D: contact prevents unequal eigenvalues

Retain all hypotheses except integrality, and now suppose D is
reduced reducible. Since D~-K_S, its arithmetic genus is one, so
chi(O_D)=0. For the trace splitting over Gamma=P1 this gives

    L=O_P1(-2),  eta^2=Delta,
    Delta in H0(P1,O(4)).

Reduced reducibility makes Delta a nonzero square in k(P1). Its divisor
is even; hence Delta=q^2 for a nonzero q in H0(P1,O(2)), up to a scalar
square absorbed over k. Thus D consists of two smooth copies D+ and
D- of Gamma, eta=+q and eta=-q, meeting at the zeros of q. At a zero
of multiplicity m their intersection multiplicity is m, where m=1 or 2.

Write f|D=a+eta b, where a is a section of O(3) and b a section of
O(1). The mate descent gives

    (a+q b)^n=(a-q b)^n.

Both sides are generically nonzero. In the function field of Gamma,
there is therefore a constant root of unity zeta with

    a-q b=zeta(a+q b).

If zeta=1, then b=0 and f itself is an invariant section. Entire
conductor gluing in degree one yields an ambient hyperplane containing
C0, impossible since its four coordinate forms are independent.

Suppose zeta!=1. Solving the displayed identity shows that both branch
restrictions are nonzero scalar multiples of q ell, with ell a nonzero
section of O(1). The section ell has exactly one simple zero on P1.
If that zero were not a zero of q, then f would vanish at two distinct
normalization points over the same point of Gamma. Both would belong
to c, contradicting the full singleton-fiber condition in section 1.
Therefore ell vanishes at a zero of q of multiplicity m. At their
common point, the restrictions of f to both D+ and D- have order m+1.

Here is the exact local smoothness contradiction. Two smooth branches
on a smooth surface with contact m can be written formally as

    D+:w=0,  D-:w=u(t)t^m,  u(0)!=0.

Their restrictions of f have order >m, hence >1. The first branch
therefore gives f_t(0)=0; smoothness of c=V(f) gives f_w(0)!=0. Taylor
expansion then gives

    f(t,u(t)t^m)-f(t,0)
       =u(0) f_w(0) t^m + terms of higher order.

Its order is exactly m, while the difference of the two restrictions
of order >m must have order >m. This is a contradiction. Thus no
zeta!=1 is possible. The reduced reducible case is excluded without
assuming its conductor nodes are ordinary pinch points.

## 7. A rank-two nonreduced addendum

This addendum was proposed and independently audited by the separate
normal-global-adversarial agent. It retains the exact entire conductor,
smooth Gamma, and finite flat rank-two assumptions; it is not a claim
about arbitrary nonreduced conductors.

In characteristic zero, a rank-two algebra eta^2=Delta is generically
reduced when Delta is not identically zero. Flatness over the smooth
curve prevents nilpotents supported only at finitely many points.
Hence a nonreduced D under these hypotheses has Delta=0 and

    p_*O_D=O direct-sum O(-2),  eta^2=0.

Writing f|D=a+eta b as above, a is generically nonzero because c is not
the reduced conductor component. The equality that f^n descends is

    f^n=a^n+n a^(n-1)b eta,
    n a^(n-1)b=0.

The tracefree summand is a line bundle on the integral smooth Gamma,
so is torsionfree. Since n!=0 and a is nonzero generically, b=0.
Thus f itself descends to an ambient hyperplane, again impossible.
This handles all conductor scheme structures inside the specified
smooth-base, flat-rank-two class.

## 8. Boundaries and continuation information

The resulting criterion excludes every smooth normalized rational
quartic scroll whose actual downstairs conductor is a smooth twisted
cubic and whose entire upstairs conductor is finite flat of rank two
over it. It requires no ordinary-pinch assumption. Its applicability to
a literature-defined class still requires verification of these exact
conductor-scheme hypotheses, not merely a picture of its double curve.

It does not settle cases where Gamma is nonnormal, reducible,
nonreduced, or has additional conductor scheme structure; where the
finite conductor map has another rank or is not flat; where S is
singular; or where c meets singularities of S. On a nonnormal Gamma,
the invariant ring may be its normalization rather than O_Gamma, and
an invariant section need not descend through the actual conductor
square. On a higher-rank or nonflat nonreduced conductor, the simple
rank-two nilpotent argument is insufficient.

The proof uses global homogeneous sections and the actual conductor,
so arbitrary affine units, omitted isolated inverse-image points, or
normalization of D cannot silently change its hypotheses. The local
contact and trace-algebra identities have a self-contained exact
[companion verifier](../computations/verify_session_scroll_conductor_compression.py).
The verifier is an identity check; the all-degree proofs are the
field-root, Taylor-order, and torsionfree arguments above.
