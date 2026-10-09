# Independent audit: conic-plus-line conductors exclude every mate

Date: 2026-10-08. Status: **PROVED and independently audited**, using
the recorded scroll conductor duality, ACM and full-support inputs.
This result includes nonreduced upstairs conductors. It does not
classify every degenerate conductor of a smooth quartic scroll.

## 1. The carrier class and exact conductor scheme

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

## 2. Curve support and every conductor prime

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

## 3. An irreducible degree-two conic cover

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

## 4. A pair of degree-one conic components

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

## 5. The doubled conic component

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

## 6. Audit decision and boundary

The three possibilities over the conic exhaust generic rank two.
Their exclusions use full scheme-level conductor descent, proper-prime
cohomology, the exact scroll effective classes, and the smoothness of
the image curve. The nonreduced argument is genuinely scheme-level;
it does not replace D by its reduced support or assume a rank-two
cover over a non-Gorenstein base.

The all-D extension in section 5 was proposed in this audit and
separately checked by `scroll_degenerate_conductor`; the conic-cover
and paired-conic reductions were supplied by that agent and separately
checked here. The ACM/Hilbert--Burch audit is recorded in
`2026-10-08-session-scroll-acm-independent-audit.md`. No agreement
between agents is substituted for the supplied proofs.

Reduced three-line conductors, non-Gorenstein multiple-line schemes,
and other degenerations of an ACM cubic remain separate. This note
does not exclude every smooth-scroll normalization or every quartic
carrier, and does not resolve the unrestricted C0 or universal STCI
problem.
