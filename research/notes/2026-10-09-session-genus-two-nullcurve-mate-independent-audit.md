# Independent audit: exceptional curves and the two genus-two mate strata

Date: 2026-10-09. Auditor: `genus_two_adjoint_audit`. Status:
**PROVED HERE / independently accepted as bounded structural
reductions**. This extends the [independent adjoint audit](2026-10-09-session-genus-two-adjoint-independent-audit.md).
No canonical frontier file was edited. The genus-two mate problem
remains open.

Keep the characteristic-zero hypotheses and notation of that audit.
Thus M is a smooth rational minimal resolution of the normal
quartic normalization S, L is the pulled-back ample hyperplane,
L^2=4, K.L=-2, K^2=0, h0(L)=4, and

    f=K+L

is the class of a connected rational conic-fibration fiber. Its
complete |L| map is birational onto the actual integral quartic X.

## 1. A useful numerical-to-linear and quadratic-product lemma

If N is a numerically trivial integral divisor class on M, then
chi(N)=1 and h2(N)=h0(K-N)=0: (K-N).L=-2 excludes an effective
representative. Thus h0(N)>=1. Its effective representative is
numerically zero, so ample intersection forces it to be zero.
Consequently N~0. This direct argument establishes every
numerical-to-linear upgrade below without relying on an incomplete
Picard torsion-freeness assertion.

If L~2B+T for an integral divisor class B with h0(B)>=2 and an
effective divisor T, two independent sections u,v of B give three
independent sections s_T u^2,s_T uv,s_T v^2 of L. Independence
follows by dividing at the generic point by s_T v^2 and using that
u/v is nonconstant and transcendental over the algebraically closed
ground field. Extending them to a basis of H0(L) imposes the
nonzero relation X0X2-X1^2=0 on the actual quartic image. This is
impossible. Fixed components of B or T and common zeros of u,v
do not invalidate a global identity of sections.

In particular L is not divisible by two in Pic(M). If L~2B, then
B^2=1, K.B=-1, and

    chi(B)=1+(B^2-K.B)/2=2,
    h2(B)=h0(K-B)=0

because (K-B).L=-4. Hence h0(B)>=2 and the preceding contradiction
applies.

## 2. Exceptional primes are vertical (-2)-curves or horizontal (-3)-sections

Let E be an integral sigma-exceptional prime. Then L.E=0 and
E^2<0. Relative minimality and adjunction give K.E>=0 as in the
genus-one audit. Put

    d=f.E=K.E>=0,     Q=K+L/2.

The rational numerical class Q belongs to L-perpendicular and has
Q^2=-1. The Hodge pairing is negative definite on this
perpendicular space. Cauchy--Schwarz for its negative gives

    d^2=(Q.E)^2 <= -E^2.

Adjunction gives -E^2=d+2-2p_a(E), so

    d^2 <= d+2-2p_a(E).

For d=0, negative self-intersection and adjunction force p_a(E)=0
and E^2=-2. Thus E is a smooth rational vertical (-2)-curve.

For d>0 the inequality gives d<=2. If d=1, the restriction of the
adjoint ruling to E is a finite degree-one map E->P1. It is an
isomorphism since the target is normal and both curves are
integral. Thus E is a smooth rational section and E^2=-3.

If d=2, the inequality forces p_a(E)=0, E^2=-4, and equality in
Cauchy--Schwarz. Consequently E is numerically -2Q=-2K-L.
The numerical-to-linear lemma upgrades this to E~-2K-L, or

    L~2f+E.

Here E is effective and h0(f)=2, so the quadratic-product lemma
excludes this case. Therefore every exceptional prime is either
a vertical smooth rational (-2)-curve or a horizontal smooth
rational (-3)-section.

## 3. There are at most two horizontal exceptional sections, and they are disjoint

Let E1,E2 be distinct horizontal exceptional sections and t=E1.E2.
Distinct curves on smooth M give t>=0. Their sum T satisfies

    Q.T=2,     T^2=-6+2t.

Cauchy--Schwarz gives 4<=6-2t, so t<=1. If t=1, equality gives
T numerically -2Q. The same numerical-to-linear upgrade yields

    L~2f+T,

contradicting the quadratic-product lemma. Thus t=0: all
horizontal exceptional sections are pairwise disjoint. This is
stronger than the preliminary bound t<=1.

Suppose that three such sections E1,E2,E3 exist. Their disjoint
sum T has T^2=-9 and Q.T=3. Equality in Cauchy--Schwarz gives

    T numerically -3Q,
    2T numerically -6K-3L.

The integral divisor 2T+6K+3L is numerically trivial and therefore
linearly trivial. Rearranging gives

    L~2(-3K-T-L).

This contradicts the nondivisibility of L proved in section 1.
There are consequently at most two horizontal exceptional
(-3)-sections, and they are disjoint.

## 4. The correct mate identity retains two different strata

Assume now that an ambient mate of degree b exists. The accepted
[full-support and smooth-lift identities](2026-10-09-session-normalization-sectional-genus-zero.md)
give a smooth embedded curve c in S isomorphic to the degree-four
rational C and an effective pullback divisor on M

    div_M((nu sigma)^*G)=b c# + W ~ bL,

where W is supported on the sigma-exceptional locus and c# is the
smooth strict transform. Put Z=W/b, an effective rational
exceptional divisor, so c# is numerically L-Z and L.Z=0. Define

    q=-Z^2,     lambda=K.Z.

Here q>0 by negative definiteness. Also lambda>=0 by section 2,
and lambda is an integer since it equals K.(L-c#). Adjunction
to c# gives the actual general relation

    -2=c#^2+K.c#=(4-q)+(-2-lambda),
    q+lambda=4.

In particular one must not assert q=4 before proving lambda=0.
The noncrepant horizontal (-3)-curves make the distinction
material. As Q.Z=lambda, Cauchy--Schwarz gives lambda^2<=q.
Together with q+lambda=4 and integral lambda>=0 this leaves
exactly

    lambda=0, q=4, c#^2=0, f.c#=2;
    lambda=1, q=3, c#^2=1, f.c#=1.

The first stratum has a rational bisection c# and Z supported
only on vertical (-2)-curves. For any horizontal exceptional
section E, effectivity gives Z.E>=0, while

    Z.E=(L-c#).E=-c#.E<=0.

Thus c#.E=Z.E=0 in the first stratum: the bisection and the
support of its correction avoid the horizontal exceptional
sections.

The second stratum has a rational section c#. The sum of the
coefficients of horizontal exceptional sections in Z equals one;
vertical correction components can still occur. Section 3 shows
there are at most two such horizontal primes. No argument here
excludes this section stratum.

The auditor initially sent an unsaved informal proposal that
started from Z^2=-4 in all genus-two cases. The owner and root
immediately identified the omitted K.Z term. That proposal was
retracted before any record promotion. The two-stratum identity
above is the corrected accepted assertion; this audit preserves
the surviving noncrepant section case explicitly.

## 5. A smooth embedded lift meets an exceptional fiber transversely at one prime

The curve c is smooth and the proper birational map c#->c is
finite and hence an isomorphism. Therefore above each point p of
c, the strict transform has one point P.

If p is singular on S, choose a local function a in m_(S,p)
whose restriction to c is a uniformizer. Such a function exists
because O_(S,p)->O_(c,p) is surjective. Its pullback to M vanishes
with positive integral coefficient along every exceptional prime
above p. The smooth local ring O_(M,P) is factorial. Restriction
of the pullback to c# has order exactly one at P, whereas its
order is at least the sum of the local intersection
multiplicities of c# with all exceptional local branches through
P. Every such multiplicity is positive. It follows that:

* exactly one exceptional prime passes through P;
* that prime is smooth at P and meets c# transversely;
* c# meets no other point of the same exceptional fiber.

In particular c#.E is zero or one for every exceptional prime E,
and there is at most one positive intersection in each connected
exceptional fiber. This constraint uses the smooth embedded lift,
not a Cartier assumption on c. It can be applied to both mate
strata, but alone it is not a classification of the exceptional
intersection graph or a proof that lambda=1 is impossible.

## 6. Accepted boundary

Sections 1--5 are exact divisor and local-ring arguments. They do
not assume that S has ADE singularities or that the adjoint
ruling descends to S. They do not identify the conductor or prove
that every possible normalization fiber has been exhausted. The
vertical (-2) exceptional configurations and their integral
saturation, the noncrepant section stratum, and descent of a
hypothetical mate all remain separate obligations. No numerical
or computational enumeration is asserted here.
