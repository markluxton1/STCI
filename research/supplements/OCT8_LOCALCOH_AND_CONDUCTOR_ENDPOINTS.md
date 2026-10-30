# October 8 historical mathematical investigations

Full original source text is preserved below, including calculations, qualifications, counterexamples, and unresolved questions. This compilation does not independently audit or promote claims.

---

## Source: 2026-10-08-session-irreducible-conductor-compression.md

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


---

## Source: 2026-10-08-session-late-results-acceptance.md

# Root reconciliation of the late October 8 results

This is the completed October 8 batch record. The
[October 9 acceptance](OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-results-acceptancemd)
supersedes its remaining smooth-normalization language and gives
the rationality, genus-one del Pezzo/D5 reductions and 630-point
necessary principal mate bound. The historical 91/103 execution
count below is preserved; the current index has 97/110.

Date: 2026-10-08, America/New_York. Fixed C0 in characteristic zero.
The universal STCI question and unrestricted C0 question remain OPEN.
This note promotes completed proofs with their exact scopes; it does
not turn the principal ancestor exclusion into a carrier theorem.

## 1. The entire e=1,d2=1 common quartic ancestor lane

**PROVED under the accepted canonical-triple reduction and P-037.**
No common quartic ancestor of the two fixed independent targets has
e=1 and a genuine second defect of degree one.

The [independent principal completeness audit](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-principal-e1-d1-independent-completeness-auditmd)
exhausts the principal chart and its projective complement. On the
declared open the complete eighteen-dimensional quartic ideal space
has first/contact rank 17. The first-normal determinant, complete
seven-column frame, all seven cofactors, resultant gcd, quadratic-field
fibre and the retained nonunit S branch are checked exactly. The
alternative killing section at infinity is reconstructed in the actual
balanced chart. All three b0=0 conjugates are retained.

The sole dimension exception is (p,r)=(2,1/2): the complete quartic
space has dimension four, with a fixed cubic times every linear form.
It is excluded by division and P-037. Every other valid principal
fibre has quartic dimension one, so cannot produce independent targets.
A uniform dimension-one assertion on the whole lane would be false.

Root rechecked the antecedents: the six nonprincipal endpoint triples
are exhausted and excluded by their complete quartic spaces in the
[endpoint ancestor proof](#source-2026-10-08-session-localcoh-e1-d1-endpoint-ancestorsmd).
At the primitive obstruction-zero point, the only correction has no
additional H0(O(-3)) freedom; multiplication by a degree-one killing
section shares its zero, so it is not a genuine finite-flat positive
defect triple. The principal and endpoint pieces therefore exhaust
the degree-one ancestor lane. The surviving e=1 ancestor degrees are
d2=2,3,4, with the separately excluded quadric and algebraic directions
still removed.

Root's isolated open-proof replay exited zero in 83.978 seconds; its
[central transcript](../validation/2026-10-07-continuation/verify_session_mf6_principal_rank_open_2026_10_08.log)
binds source SHA256
2fbefebda6723b7d721f0034c0167a2c70a3b79eed01675b99baf453453a9ac8.
The independent auditor's four own executions, source snapshots and
input closure are in the
[principal audit manifest](../validation/2026-10-08-principal-e1-d1-audit/audit-manifest.json).
The copied owner replay is not counted as an auditor execution.

## 2. Smooth quartic scrolls: reduced or locally Gorenstein conductor

**PROVED:** if an integral quartic X has smooth rational quartic-scroll
normalization and its actual downstairs conductor Gamma is reduced
or locally Gorenstein, X has no mate supported only on C0, in any
positive degree. The theorem retains arbitrary upstairs conductor D.

The actual conductor is an ACM cubic with Hilbert polynomial 3m+1;
this is a scheme-level result, not a claim about the Jacobian radical.
The [ACM audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-acm-independent-auditmd)
and [owner proof](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-degenerate-conductormd)
derive its Hilbert--Burch presentation and the exact sequence
0 -> O_Gamma -> p_*O_D -> omega_Gamma -> 0.
The reduced theorem includes the smooth twisted cubic, conic plus line,
and all three-line configurations. The concurrent three-line case is
excluded geometrically before any flat-cover assertion. See the
[conic-plus-line audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-conic-line-independent-auditmd)
and [three-line audit](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-three-lines-independent-auditmd).

For locally Gorenstein Gamma the exact sequence makes p finite flat
of rank two even when Gamma is nonreduced. A locally Gorenstein triple
line is impossible: devissage makes the degree of every invertible
sheaf divisible by three, while deg(omega_Gamma)=-2. The doubled-line
generic Artin algebra gives only the partitions (a,r)=(4,1),(2,2),
or two (2,1), with a the upstairs nilpotent length and r the residue
extension degree. The F0/F2 anticanonical classes exhaust these cases.
Disjoint paired fibres and the global prime-exchange incidence
obstruction remove the exchanged-prime configurations. In the remaining
cases the involution preserves every conductor prime. The equation
sigma(f)^n=f^n then forces sigma(f)/f=+1 or -1 in each entire generic
Artin ring, with no nilpotent correction. Cohen--Macaulay purity extends
square invariance globally, and the conductor square descends f^2 to
the forbidden quadric mate. The
[independent Gorenstein audit](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-gorenstein-independent-auditmd)
accepts this scope. Root checked the thick-base partitions and the
prime-exchange qualification; reduced-fibre reasoning alone would not
justify them.

**Retained boundary at this intermediate acceptance:** an actual conductor that is
both nonreduced and not locally Gorenstein. Classification and an
actual differential obstruction are being independently audited; the
proposed extension is not a premise of the theorem accepted here.
Singular normalizations and higher carrier degrees remain separate.

## 3. The principal exceptional quartic (p,r)=(8,1/2)

**PROVED all-mate exclusion of this fixed carrier.** Its explicit
normalization is F0. In invertibly changed coordinates the equation is
(xL-8yz)^2-x^3(x-8y), L=96w+x-8y+4z. The entire downstairs conductor
is (x^2,xy,xL-8yz), a double line plus a line; its upstairs divisor is
2{U=0}+2{b=0}. The actual nonreduced conductor is locally Gorenstein,
so its complete finite flat algebra, including nilpotents, gives the
square compression in section 2.

The [owner proof](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-rhalf-scroll-conductormd)
and [independent audit](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-rhalf-scroll-independent-auditmd)
bind this equation to the unique actual boundary quartic. Root
independently derived the normalization-ring closure and all six
annihilator identities. Hilbert--Burch and the actual conductor Hilbert
polynomial prove equality of the entire ideal sheaves, not just their
support. A fresh isolated root replay of the
[checker](../computations/verify_session_mf6_rhalf_scroll_2026_10_08.py)
passed in 0.591 seconds, source SHA256
9d532c25c9f50f206e0d57c5ce7f35b9feb54707bf1b630fd622c0c473028aa2.
Its [transcript](../validation/2026-10-07-continuation/verify_session_mf6_rhalf_scroll_2026_10_08.log)
retains the command and source/log hashes.

The other complement carriers were already excluded as normal quartics
or quartics singular along smooth twisted cubics. The generic principal
carrier problem remains distinct. Its nonnormal locus is a proper
closed finite subset of the geometrically integral direction curve:
the unique quartic kernel gives a regular projective family away from
the treated node, and a normal b0=0 fibre makes the closed
positive-dimensional Jacobian-fibre locus proper. The exact finite
subset is not yet enumerated. See section 6 of the
[boundary proof](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-principal-boundary-auditmd).

## 4. Execution and continuation state

The original usage-limit interruption was followed by successful
resumptions. A later 7:59 PM reset was independently checked at
2026-10-09 01:01:59 UTC; current usage allowed ordinary work, and the
assigned agents resumed. An earlier root poll could not access another
agent's process 60266; its owner subsequently observed that process
terminal with exit zero. An unavailable root handle is not evidence
that the owner's observation failed. No root process is claimed live
from a source file or an intended command.

The [reconciled index](../validation/2026-10-08-continuation-index/index.json)
at this earlier checkpoint included 91 distinct latest-PASS top-level sources and 103
explicitly indexed executions, including the four actual independent
principal executions. The baseline was retained. Earlier failed checks
and the superseded Veronese source-byte retention limitation remain
explicit. These counts establish provenance and execution scope; they
do not substitute for the geometric proofs.

## 5. Final accepted extension: every smooth rational quartic scroll

**PROVED:** let X be an integral quartic with finite normalization S=F0,
H=C+2f, or S=F2,H=C+3f, over an algebraically closed characteristic-zero
field. No hypersurface of any positive degree has intersection with X
supported exactly on the fixed C0. Both actual conductor schemes are
unrestricted. This supersedes the intermediate conductor boundary in
section 2, while retaining singular normalizations and other polarized
normalization classes as separate work.

The [nongorenstein classification](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-nongorenstein-cubic-classificationmd)
uses the actual three-by-two linear Hilbert--Burch matrix. Its projective
rank-zero locus is a point or a line. The point case is a cone over a
noncollinear length-three scheme in P2; saturation and absence of linear
ideal forms, not merely h0(O_Z(1))=3, prove noncollinearity. The residual
nonreduced nongorenstein ideals are the double-line-plus-line,
curvilinear triple-line, and fat triple-line ideals. The locally
Gorenstein cases were already covered in section 2.

At a curvilinear triple line A=K[epsilon]/epsilon^3, B is free of rank
two. Multiplication by epsilon has K-rank four. Its truncated-DVR
factors have ranks bounded by two thirds of their lengths, so equality
forces every actual upstairs multiplicity divisible by three. This
contradicts the coefficient two of C in D=-K_S.

For a fat triple line A=K+N,N^2=0,dim N=2, the exact quotient B/A=omega_A
gives dim NB=3 and dim B=6. The finite product of truncated DVR factors
is Frobenius over K. Since (NB)^2=0, NB=Ann_B(NB); consequently every
conductor multiplicity is even. Thus D=2E with E=C+f on F0 or C+2f
on F2. A prime E has degree three over the supporting line and would
need three transverse totally ramified intersection points with c;
Riemann--Hurwitz permits at most two. A horizontal degree-two component
plus a degree-one fibre forces a double zero at one ramification point,
contradicting transversality of the smooth image. Distinct fibres give
two different normalization points above the same required zero. The
only remaining class is D=2C_min+4F on F2.

That final pattern has NB_F=(t^2) in its length-four factor. Ambient
normal coordinates to the support line therefore vanish to order at
least two along F, making d nu generically rank one there. The
[independent differential lemma](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-normalization-differential-independent-auditmd)
excludes it. Root checked the lemma directly: a unit Jacobian pivot
gives a regular kernel vector modulo the prime ideal of the conductor
component. Differentiating the full power identity in an ambient-unit
trivialization yields n f^(n-1)V(f)=0 on that integral component.
Cancellation takes place generically, followed by extension in the
domain; it does not divide by f at its zero. At an intersection with
the smooth c, its tangent is the kernel, contradicting immersion of
nu|c. The lemma also permits singular conductor primes. An isolated
differential rank-drop point does not satisfy its hypothesis.

Finally, the [exact Artin audit](OCT8_SCROLL_CONDUCTOR_AND_ACM.md#source-2026-10-08-session-scroll-artin-independent-auditmd)
completes double-line-plus-line conductors directly, including the
nongorenstein junction. Above the doubled line, free rank two over
K[epsilon]/epsilon^2 gives only (a,r)=(4,1),(2,2), or two (2,1).
Above the reduced line the patterns are (2,1),(1,2), or two (1,1).
The (4,1) and (2,1) single-prime cases have generic rank-one differential
and are excluded. On F0 the remaining doubled horizontal prime leaves
two distinct paired fibres. On F2 the remaining doubled minimal section
and fibre likewise leave paired fibres, or two doubled fibres leave an
impossible reduced-line component class. Every pattern is therefore
excluded. No global trace through a nongorenstein point is asserted.

This proof uses entire Artin rings and the whole mate equation. The
alternative transversal-plane delta argument is retained as a proposed
secondary route; it is not needed for the accepted theorem. The
independent Artin audit, differential audit, the
[complete independent scroll audit](OCT8_SCROLL_GORENSTEIN_AND_SINGULAR_AUDITS.md#source-2026-10-08-session-scroll-nongorenstein-independent-auditmd)
and root verification supply the promoted scope. No broad classification of all nonnormal quartic
surfaces is inferred from the classification of these ACM cubics.

## 6. Accepted second-family quadratic exceptions

Both factors k^2+1 and k^2-2k-1 are excluded at all four geometric roots
and for every lower parameter lambda. The
[owner proof](#source-2026-10-08-session-localcoh-family2-quadraticsmd)
and [independent audit](#source-2026-10-08-session-localcoh-family2-quadratic-independent-auditmd)
check polynomial duals with n^T L=0 and n^T u=1 on all eighteen actual
quartic columns. Separate exact-field arithmetic rederives the seeds,
directions, slopes, rank-29 top map and complete affine lift fibre.
A fresh Macaulay2 reconstruction binds all 540 products and both target
columns literally and proves equality with the complete next-stage Ext
image. The [aggregate manifest](../validation/2026-10-08-family2-quadratic-audit/audit-manifest.json)
retains all input/source hashes, isolated replay, countercheck and tensor
execution history, including two preparatory failures.

The remaining second-family locus is 22 geometric points from factors
of degrees 3,4,15, each retaining its entire lambda fibre OPEN. No
survivor or rank jump is inferred from being an exception to the old
generic dual. Other endpoint families and nonendpoint top zeros remain
open.


---

## Source: 2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md

# The six defective e=1 endpoint triples also exclude quartic ancestors

Date: 2026-10-08. Fixed `C0` in characteristic zero. Status:
**PROVED COROLLARY OF THE ACCEPTED COMPLETE QUARTIC FIBRES AND P-037.**
This is an ancestor-specific consequence; it uses no STCI mate, BF mate
bound or single-carrier cubic-pole inference.

Let quartics `F,G` and an ancestor alpha satisfy `F*alpha=u,G*alpha=v`.
Their canonical triple is contained in both multipliers. If it has
`e=1,d2=1` and is on the complete `a0=0` or `b1=0` boundary of the
defect-killed quadratic class, the actual torus normalization gives one
of the six triples from
[`2026-10-07-session-mf6-e1-d1-endpoints.md`](2026-10-07-session-mf6-e1-d1-endpoints.md):

```text
A=r*z, B=1+z, delta=z,
or A=1+r*z, B=1, delta=1,
with r=-1/2 or 12r^2+4r+3=0.
```

At each of the four algebraic direction fibres, the **complete** quartic
space has dimension one (rank 34 in all 35 ambient monomials). Hence
F and G are proportional. Their images u and v would then be
proportional, contradicting their linear independence.

At each of the two rational-root fibres, the complete quartic space is
`C*H0(P3,O(1))`, with the fixed nonzero cubic C equal to C_L or C_R
from the endpoint audit. Thus `F=C*F1,G=C*G1` for actual homogeneous
linear forms F1,G1, and

```text
F1*(C*alpha)=u, G1*(C*alpha)=v.
```

This is a common ancestor with degree-one multipliers, prohibited by
the all-stage P-037 theorem. Since u is nonzero, `C*alpha` is nonzero;
the passage does not annihilate the ancestor.

The only symmetry used to normalize the six triples is the actual
ambient torus preserving C0 (and the reversal for equivalent charts).
Under the torus `(x0,x1,x2,x3)->(x0,lambda*x1,lambda^3*x2,lambda^4*x3)`,
q and B have weights four and six and the target numerators have weights
three and five. Therefore u and v are eigenvectors of respective
weights -7 and -5. Nonzero scalings can be absorbed into F1,G1, so
P-037 remains applicable to the fixed targets. Coordinate reversal
preserves q, sends B to -B, and swaps the two target numerators;
it exchanges u and v with the same harmless nonzero sign.

All six endpoint triples are therefore excluded from the quartic-ancestor
problem. The principal `a0*b1!=0` portion of the d2=1 sextic remains
open, as do the positive-defect d2=2,3,4 ancestor strata. In particular
the d2=4 Gorenstein case remains; its elimination does not follow from
the STCI quartic bound.

More generally, the same exact argument excludes a candidate canonical
triple if its full quartic space has dimension at most one, or if every
quartic in that space has a fixed factor of degree one, two or three:
division gives multipliers of degree at most three, prohibited by P-037.
This is a useful first check before computing the unique conormal
socle quotient from the splitting criterion.

The complete ambient fibre ranks and fixed factors were independently
audited in the endpoint source. The MF6 auditor reconfirmed those ranks,
the actual torus weights and reversal on 2026-10-08. This proof depends
on those complete spaces; merely inspecting the displayed FL/FR forms
would not suffice.


---

## Source: 2026-10-08-session-localcoh-e1-d4-algebraic.md

# Two algebraic e=1 directions exclude d2=4 quartic ancestors for every defect section

Date: 2026-10-08. Fixed C0 in characteristic zero. Status:
**PROVED BY COMPLETE QUARTIC FIBRES AND A PARAMETER-COVERING RANK ARGUMENT;
accepted after independent and root review.** See the
[root acceptance record](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-new-results-acceptancemd).
This treats exactly the two
directions `A=r*z,B=1,12r^2+4r+3=0` with d2=4. Other positive-D2
directions and Gorenstein quadruples outside these fibres remain open.

## 1. Genuine degree-four defects and their complete linear incidence

These directions have zero primitive quadratic obstruction and unique
primitive correction gamma0=0. For a defect section delta in H0(O(4)),
every degree-four corrected triple has relation

```text
delta*m+theta*y^2=0,
m=U-r*z*V, y=V.
```

The extra global correction theta is a constant because its bundle is
O(-4+d2)=O(0). If theta=0, it shares every zero of delta, violating
finite-flatness of a genuine defect-four triple. Every nonzero homogeneous
quartic has a projective zero, including an infinity zero when its affine
degree drops. Thus theta is nonzero, and simultaneous scaling of delta
and theta normalizes theta=1. Delta is an arbitrary nonzero homogeneous
quartic; its repeated roots and infinity roots are retained.

Write the actual quartic jet on the canonical double as
`F=h*m+E*y^2+...`. It contains this triple if and only if

```text
h=delta*E.
```

An ancestor needs two linearly independent quartics because its target
classes u and v are independent. The proof below shows that this exact
linear containment system has dimension at most one for every delta.
No STCI mate or BF d2 bound is involved.

## 2. The complete seven-dimensional double-quartic space

The independent source reconstructs all 35 ambient degree-four monomials
and imposes both the curve restriction and the first normal coefficient
along `U=r*z*y,V=y`. Its exact matrix has rank 28 over the quadratic
field; all identities are reduced modulo `12r^2+4r+3`, so both roots
are covered. The complete seven-dimensional quartic space has two
primitive members with `(h,E)=(1,0),(z^8,0)`, and five other members
with

```text
(h,E)=(a_i*z^(i+2), z^i), i=0,1,2,3,4,
a0=3r-1/2,
a1=6r+2,
a2=0,
a3=4r-5/3,
a4=(66r+13)/18.
```

Their seven explicit ambient forms and the full rank verification are
stored in the standalone checker and its JSON. The five a_i are pairwise
distinct at either root: every difference is a unit modulo the defining
quadratic.

For a general member write `E=sum(e_i*z^i,i=0..4)`. Its h is

```text
h=A+B*z^8+sum(a_i*e_i*z^(i+2),i=0..4).
```

The free A and B match the constant and eighth coefficients of delta*E
uniquely. Thus the full quartic containment space is canonically the
kernel of the seven-by-five matrix obtained from coefficients z^1
through z^7 of

```text
delta*E-sum(a_i*e_i*z^(i+2),i=0..4).
```

## 3. Exact minors cover every defect section

Write `delta=d0+d1*z+d2*z^2+d3*z^3+d4*z^4` in its finite chart.

If d0 is nonzero, the rows z^1 through z^4 and columns e1 through e4
have determinant d0^4. Therefore the matrix has rank at least four
and kernel dimension at most one. Equivalently those low coefficients
determine e1,e2,e3,e4 successively from e0.

If d4 is nonzero, the rows z^4 through z^7 and columns e0 through e3
have determinant d4^4. The same conclusion follows from the high
coefficients, including infinity behavior.

It remains to retain the entire boundary d0=d4=0. There the first five
rows have determinant d1^5, and the last five rows have determinant
d3^5. If either d1 or d3 is nonzero, the matrix has full rank five.

The final boundary is `delta=d2*z^2`. The middle five rows are the
diagonal matrix

```text
diag(d2-a0,d2-a1,d2-a2,d2-a3,d2-a4).
```

Since the a_i are pairwise distinct, at most one entry can vanish.
Its rank is at least four. This final case includes the defect section
with double zeros at both endpoints; it is not discarded as a repeated
or pole stratum.

These cases cover every delta, and prove kernel dimension at most one
uniformly. Hence every genuine defect-four triple in either algebraic
direction has at most one independent containing quartic, and cannot
support the two independent multiplier equations of a common quartic
ancestor.

## 4. Exact evidence and retained scope

Run

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
 research/computations/verify_session_localcoh_e1_d4_algebraic_2026_10_08.py
```

The checker independently reconstructs the complete ambient space,
checks all seven explicit forms and their h/E coefficients, checks
pairwise differences in the exact field, and verifies all four minor
identities and the last diagonal case. It uses no discovery JSON as a
proof input. Its companion JSON records the full matrix and source hash.

The principal obstruction-zero direction `A=1+z,B=-2-8z` still needs its
defect-four rank incidence. Its complete double-quartic map is saved in
`explore_session_localcoh_e1_d4_quartic_map_2026_10_08.json`. The unique
quadric direction is already excluded for every D2 by the separate
double-divisor/P-037 proof. Directions with nonzero primitive quadratic
obstruction are not covered by this note. No claim eliminating an entire
d2=4 Gorenstein stratum follows.


---

## Source: 2026-10-08-session-localcoh-e1-d4-independent-audit.md

# Independent audit of the algebraic e1,d2=4 quartic exclusion

Date: 2026-10-08. Fixed C0, characteristic zero. Scope: exactly
`A=r*z,B=1,12r^2+4r+3=0`, genuine degree-four second defect. The audited
claim is in
[`2026-10-08-session-localcoh-e1-d4-algebraic.md`](#source-2026-10-08-session-localcoh-e1-d4-algebraicmd).

**ACCEPTED:** every genuine triple in either algebraic direction has a
complete space of containing ambient quartics of dimension at most one.
It therefore cannot be the canonical triple of a quartic common ancestor
with independent target classes u and v. This is uniform over every
defect section, including repeated roots and roots at infinity. It does
not eliminate the other directions or an entire Gorenstein stratum.

## Genuine triples and normalization

The previously audited defective-triple presentation is
`J=(delta*m+theta*y^2,m*y,m^2,y^3)`, up to the harmless sign convention
for the correction. For these obstruction-zero directions the primitive
correction is zero. The possible additional correction is a section of
`O(-4+d2)=O(0)`, so theta is a scalar.

The theta-zero branch is excluded by finite-flatness, rather than being
discarded to make the rank argument work. Near a zero of the nonzero
defect section, take a support DVR R. If theta is zero, the quotient has
R-module presentation

```text
R*1 + R*y + R*y^2 + (R/(delta))*m.
```

The last summand is nonzero torsion, inconsistent with finite-flatness
over R. Every nonzero homogeneous section of `O(4)` has a projective
zero over the algebraically closed field. This includes an infinity
zero when its finite polynomial has degree below four. Thus theta must
be nonzero. Dividing the relation by theta normalizes theta to one and
replaces delta by delta/theta, preserving the same triple and its defect
divisor. This retains every nonzero five-coefficient quartic delta; no
root separation or finite-support assumption is used.

With theta one, the quotient has free basis `1,y,m` and relation
`y^2=-delta*m`. Therefore an actual quartic jet
`F=h*m+E*y^2+...` vanishes on the triple exactly when `h=delta*E`.
The omitted terms lie in `(m*y,m^2,y^3)`. This also proves the containment
criterion at zeros of delta, rather than merely away from them.

## Complete ambient quartic space

The source enumerates all exponent quadruples of sum four: there are
`binomial(7,3)=35`, each occurring once. It substitutes the actual
finite-chart normal parameters and imposes the constant and first
normal coefficients of the canonical double. The resulting `31x35`
matrix has rank 28 over `QQ(sqrt(-2))`.

The defining polynomial has discriminant `-128` and is irreducible over
QQ. The chosen root is `(-1+2*sqrt(-2))/6`. Every entry is rational in
r; conjugation preserves rank, so the second root is also covered.
The source verifies seven independent homogeneous quartic forms in the
kernel. Rank-nullity shows that these span the complete ambient space,
rather than a selected pencil. Checking the dense finite chart suffices
for the global double conditions: the primitive double is finite-flat
over C0, so its structure sheaf has no support torsion at infinity.
The forms themselves are homogeneous global forms.

The normalized basis consists of two forms with `(h,E)=(1,0),(z^8,0)`
and five forms with

```text
(h,E)=(a_i*z^(i+2),z^i), i=0,...,4,
(a0,a1,a2,a3,a4)=(3r-1/2,6r+2,0,4r-5/3,(66r+13)/18).
```

All their normal coefficients are checked exactly modulo the quadratic.
Every pairwise difference `a_i-a_j` is a unit in the field.

For `E=sum(e_i*z^i)`, the two primitive basis coefficients determine
the constant and eighth coefficients of h freely. Containment determines
them uniquely as the corresponding coefficients of `delta*E`. The
remaining seven equations are the coefficients z through z^7 of
`delta*E-sum(a_i*e_i*z^(i+2))`. Hence the containing-quartic space is
isomorphic to the kernel of the displayed `7x5` operator. In particular,
E zero does not leave an extra primitive quartic: it forces h zero and
both primitive coefficients zero.

## Coverage of every defect section

The four minor identities provide an exhaustive case split:

1. If d0 is nonzero, the lower `4x4` triangular minor is d0^4.
2. If d4 is nonzero, the upper `4x4` triangular minor is d4^4.
3. With d0=d4=0, the first five-row determinant is d1^5, and the last
   five-row determinant is d3^5. A nonzero d1 or d3 gives rank five.
4. The entire remaining locus is `delta=d2*z^2`. Its middle five-row
   matrix is `diag(d2-a0,...,d2-a4)`. Since the a_i are pairwise distinct,
   at most one diagonal entry can vanish, so rank is at least four.

These are polynomial identities and field-unit statements, valid at
both roots of the quadratic. They prove rank at least four everywhere,
and kernel dimension at most one. The last case explicitly retains the
section with double zeros at both endpoints. A section with d4 zero has
an infinity zero; it is covered by the same coefficient split. Nothing
in the argument assumes reduced support.

If two quartics F,G gave `F*alpha=u,G*alpha=v`, both would contain the
canonical triple and would be proportional in this at-most-one-dimensional
space. Their images would be proportional, contrary to the independent
targets. This uses the accepted canonical-triple reduction for ancestors,
not an STCI mate bound or a further carrier classification.

## Fresh replay and provenance

The retained self-contained
[`source`](../computations/verify_session_localcoh_e1_d4_algebraic_2026_10_08.py)
was inspected and freshly replayed from an exact byte snapshot in an
isolated directory. It reads no discovery JSON or generated proof input.
The source SHA256 is

```text
ae88024f00b8216be727957930747001b44f457e532a0746e6a8e2a657850a02
```

The replay completed with exit code zero and all assertions passed. Its
source copy, generated complete matrix/basis JSON, output log, and hashes
are preserved under
[`2026-10-08-e1-d4-algebraic-audit`](../validation/2026-10-08-e1-d4-algebraic-audit/replay-manifest.json).
The generated JSON is byte-identical to the retained canonical generated
JSON; the original source and generated JSON were not modified. This
audit does not edit any canonical frontier file.


---

## Source: 2026-10-08-session-localcoh-family2-generic.md

# Second endpoint family: exact generic exclusion and retained exceptions

Date: 2026-10-08. Scope: characteristic zero, the fixed rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, primitive degree-two normal-dual directions,
pure cubic top `h=t`, and the second rational endpoint family. This note
does not address either `p(0)=0` boundary family or a nonendpoint top zero.

## Result and exact unresolved locus

**PROVED under the audited actual multiplication tensor and coordinate
bases:** the second rational endpoint family excludes target `u`, for
every lower-correction parameter `lambda`, away from the displayed
denominator roots. After removing chart poles and nonprimitive directions,
the following five square-free, pairwise-coprime factors retain exactly
26 primitive geometric parameter points:

```text
k^2+1
k^2-2k-1
3k^3+4k^2+9k-4
13k^4+10k^3+2k^2-42k-7
243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
 -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
 +1296458k^4+1345117k^3+811630k^2+285598k-610
```

Each retained parameter point still has its complete affine `lambda`
fibre. These are exceptions to this certificate, with no implication
that they support an ancestor or even an actual rank jump. No exceptional
field fibre was computed in this branch.

## Actual direction and complete affine family

The independently classified second family has

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

Its actual quartic lift is the complete affine line
`a*(k)+lambda*k0`, where the 32-by-30 pure-top map has rank 29 and `k0`
is its nonzero kernel vector. The clearing factors are

```text
B=2(k-1)^3(k+1)^3                  [direction denominator]
A=120(k-1)^9(k+1)^9               [ancestor denominator].
```

The certificate stores `alpha=A*(a*+lambda*k0)`, along with
`P=B*p` and `R=B*r`. Its standard-library verifier checks all four
rational direction formulas by polynomial cross-multiplication, the
rank-29 top map, and the coefficient of `lambda` in each of the thirty
ancestor coordinates. It verifies all 32 cleared pure-top identities

```text
B^3 * M(alpha) = A * coefficients(t*P^i*R^(3-i)), i=0,1,2,3.
```

Since `A` and `B` are nonzero on the retained chart, these checks prove
coverage of the entire affine lift fibre at every retained parameter.

## Exact polynomial dual

The saved full 74-by-18 module calculation over `QQ(k)[lambda]` returned
target evaluation ideal `(1)` and a complete polynomial left dual. The
cleared dual has 26 nonzero entries and degree at most two in `lambda`.
Its exact target value is

```text
D=89514547200*(k-1)^15*(k+1)^12*(k^2+1)^5*(k^2-2k-1)^5
 *(k^2+2k+3)^4*(3k^3+4k^2+9k-4)
 *(3k^4-2k^3-6k^2-18k-9)*(13k^4+10k^3+2k^2-42k-7)
 *(243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
   -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
   +1296458k^4+1345117k^3+811630k^2+285598k-610).
```

The verifier checks all eighteen actual tensor-column identities
`n^T L(alpha)=0` over `QQ[k,lambda]` and `n^T u=D`. It also checks
the actual target columns in the stored tensor are `e72,e73`.
Therefore target `u` cannot lie in the multiplier image wherever `D!=0`,
for every value of `lambda`.

A fixed four-by-four homogeneous Sylvester determinant gives

```text
Res_hom(p,r)=-8*(k^2+2k+3)*(3k^4-2k^3-6k^2-18k-9)
             /((k-1)^5*(k+1)^6).
```

Thus `k=+/-1` are chart poles, while the roots of `k^2+2k+3` and
`3k^4-2k^3-6k^2-18k-9` are nonprimitive. The independent verifier
reconstructs the full factorization of `D`; verifies the five remaining
factors are square-free and pairwise coprime; and verifies they are
coprime to both the chart factor and the homogeneous resultant numerator.
This establishes the precise count and scope of the retained 26 points.

## Reproduction, evidence, and terminal status

Recompute the generic module:

```sh
/opt/homebrew/bin/M2 --script \
  research/computations/session-localcoh-origin-family-2.m2
```

Regenerate its cleared certificate using SymPy:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/computations/verify_session_localcoh_family2_generic_2026_10_08.py --regenerate
```

Verify every saved identity and scope assertion with an ordinary Python:

```sh
python3 research/computations/verify_session_localcoh_family2_generic_2026_10_08.py
```

The M2 process was explicitly launched in tool session `55063` on
2026-10-08 and completed with exit code zero. Certificate regeneration
in session `18670` and strengthened default verification in session
`79082` also completed with exit code zero. No process from this branch
remains running. An auxiliary dense rational point-rank probe in session
`26885` was stopped with `KeyboardInterrupt` and exit code 130 after
the generic dual had completed; it produced no rank result, and none
is asserted here.

Full evidence is retained in
[`session-localcoh-origin-family-2-generic-dual.txt`](../computations/session-localcoh-origin-family-2-generic-dual.txt),
[`session-localcoh-origin-family-2-evaluations.txt`](../computations/session-localcoh-origin-family-2-evaluations.txt),
[`session_localcoh_family2_generic_dual_audit_2026_10_08.json`](../computations/session_localcoh_family2_generic_dual_audit_2026_10_08.json),
and the separate
[`verify_session_localcoh_family2_generic_2026_10_08.py`](../computations/verify_session_localcoh_family2_generic_2026_10_08.py).
The original generic verifier is imported as an unchanged standard-library
arithmetic helper; its exact file hash, all coordinate sources, the seed,
the full module input, raw dual, and evaluation output are bound to the
new certificate. The first family's sources and Q1/Q3 artifacts were
left unchanged.


---

## Source: 2026-10-08-session-localcoh-family2-quadratic-independent-audit.md

# Independent audit of both family2 quadratic exception fibres

Date: 2026-10-08. Scope: characteristic zero, the fixed rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, the second primitive degree-two endpoint
direction family, and all its lower correction parameters at the roots
of `k^2+1` and `k^2-2k-1`. Auditor: a separate agent from the coefficient
certificate producer. No original coefficient certificate, generation
source, or canonical frontier document was edited.

## Verdict

**PROVED under the previously audited local-cohomology interpretation:**
the two roots of each quadratic, four geometric direction parameters in
total, exclude target `u` for **every** affine lower correction `lambda`.
The producing verifier passed an isolated replay with all thirteen input
files frozen. A separate implementation using SymPy algebraic-number
domains passed all exact polynomial identities without importing the
producing verifier or regenerating its coefficient certificates.

Together with the previously accepted generic family2 certificate, these
exclusions reduce that certificate's retained primitive direction locus
from 26 points to 22 points, of degrees `3+4+15`. Each remaining point
retains its entire affine `lambda` fibre. These are unresolved certificate
exceptions; no surviving incidence or ancestor is inferred. The other
endpoint families, nonendpoint top zeros, unrestricted quartic incidence,
and the global STCI problem remain outside this conclusion.

## Actual forms, top map, and complete parameter fibre

The independent
[`countercheck.py`](../validation/2026-10-08-family2-quadratic-audit/countercheck.py)
parses the displayed stage-four ancestor numerators and quartic forms in
[`localcoh-incidence-bases.txt`](../computations/localcoh-incidence-bases.txt).
It verifies the quartics are the following **actual degree-four forms**:

```text
q=xw-yz, A=x^2z-y^3, B=xz^2-y^2w, C=yw^2-z^3;
q*(x^2,xy,xw,yz,zw,w^2),
A*(x,y,z,w), B*(x,y,z,w), C*(x,y,z,w).
```

They all vanish on `C0` and have independent coefficient vectors of rank
18. The restriction of the 35 degree-four monomials to `C0` has rank 17,
so the displayed forms span exactly the full degree-four ideal piece.
They are not four-coordinate generator rows mistaken for polynomial forms.

The checker independently substitutes `x=1,y=t,z=t^3+a,w=t^4+ta+q`
in every actual ancestor numerator. It extracts its normal-order-three
part, converts it to the previously audited balanced normal coordinates,
and computes all four degree-six residues. All thirty top columns match
the saved top map literally. The resulting `32x30` matrix has rank 29.
Its nonzero rational kernel vector is exactly the lower slope in the
family2 seed. Consequently every lift of the specified nonzero pure top
is the full affine line

```text
alpha(k,lambda)=a*(k)+lambda*k0.
```

At each quadratic field, all thirty constant seed coefficients and all
thirty slopes are compared directly to the rational family2 source, and
all six direction coefficients are compared to the same source. Every
source denominator is inverted only after checking it is a unit modulo
the defining quadratic. All 32 coefficients of the specified actual
normalization `t*p^i*r^(3-i)`, `i=0,1,2,3`, match the top of `alpha`.
Thus no lower parameter is lost through sampling or a generic-rank
argument. The projective limit with zero top is a different stratum,
not a lift of this fixed nonzero top.

The independent fixed-size homogeneous Sylvester determinant is nonzero
in each field even though `r` loses its quadratic coefficient there:

| Field | Chosen exact embedding | Homogeneous resultant |
|---|---|---|
| `QQ[k]/(k^2+1)` | `k=i` | `-8i` |
| `QQ[k]/(k^2-2k-1)` | `k=1+sqrt(2)` | `-96+68sqrt(2)` |

The second norm is `-32`, so neither conjugate resultant vanishes. Both
quadratics are coprime to the chart-pole factor and homogeneous
nonprimitive factors. These four parameters are admissible primitive
directions, not excluded chart or normalization points.

## Independent field and polynomial dual checks

The original verifier uses rational coefficient pairs and an AST parser.
The new countercheck instead uses SymPy's algebraic-number domains
`QQ(i)` and `QQ(1+sqrt(2))`, reducing rational source expressions by
polynomial remainders and extended inverses. It does not import any
helper from the original verifier. It also compares all 74 entries of
each raw Macaulay2 dual directly with the saved coefficient certificate.

In each field the dual has 27 nonzero entries and degree two in `lambda`.
The tensor is read as a sparse `74x542` matrix with header
`30 18 74 542`; its last two target columns are checked to be exactly
`e72,e73`. For each of the eighteen multiplier columns, the new checker
forms its image from **all thirty ancestor coordinates**, multiplies it
by the full dual, and verifies that every coefficient through degree
three in `lambda` is zero:

```text
n(lambda)^T L(alpha(lambda))=0,    n(lambda)^T u=1.
```

If `L(alpha)*x=u`, these exact identities would give `0=1` after left
multiplication by `n`. One valid dual is sufficient; correctness does
not depend on trusting a claim that the exported vector spans an entire
left kernel or that the producing module computation was exhaustive.
There are no `lambda` denominators, so specialization creates no
additional exceptional lower parameters.

The defining quadratics have discriminants `-4` and `8`; both are
irreducible and separable over `QQ`. The identities transport through
both embeddings into any algebraically closed characteristic-zero
field. Every inverted field unit remains nonzero under each embedding.
This establishes all four geometric roots, rather than just the two
chosen exact embeddings used by the independent arithmetic implementation.

## Durable execution record

The independent countercheck completed in tool session `19588` with exit
code zero. Its source, output, and full input hashes are in
[`countercheck-result.json`](../validation/2026-10-08-family2-quadratic-audit/countercheck-result.json)
and the retained
[`countercheck.log`](../validation/2026-10-08-family2-quadratic-audit/countercheck.log).
Its source SHA256 is

```text
88e8aa6072fd93074453a2fe6fbef710bc3b6a2273151f12d00320233c095334
```

The unchanged original verifier was copied with all its input closure
into a separate snapshot and ran with exit code zero in 0.082 seconds.
The snapshot's thirteen input hashes were unchanged after execution.
Reproduction and its terminal record are in
[`isolated-replay.py`](../validation/2026-10-08-family2-quadratic-audit/isolated-replay.py),
[`isolated-replay.log`](../validation/2026-10-08-family2-quadratic-audit/isolated-replay.log),
and
[`isolated-replay-manifest.json`](../validation/2026-10-08-family2-quadratic-audit/isolated-replay-manifest.json).
The replayed original verifier SHA256 is
`a1168854beed0d56838851710444a5d2d35ef835333f9ab179d2163f23739ea3`;
its output SHA256 is
`69a490fc61abf1fe30a932b6e84f5707470db7e47806aef71921fb4f10dd1aed`.

Reproduce the additional independent check from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-08-family2-quadratic-audit/countercheck.py
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-08-family2-quadratic-audit/isolated-replay.py
```

The producing agent's independent evidence and original process history
are retained in the
[quadratic proof note](#source-2026-10-08-session-localcoh-family2-quadraticsmd).
The absent parent-local handle for one producing process was not treated
as a failed computation or used to infer a live process. Acceptance here
comes from the exact identities and new terminal executions.

## Fresh reconstruction of the complete actual tensor

An additional independent Macaulay2 checker completed with exit code zero
in 0.840 seconds. Its
[`actual-tensor-reconstruction.m2`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2)
rebuilds the ancestor space from the Ext map, verifies that it has
dimension 30 and that the map is injective in degree `-7`, and sums all
four ideal-generator contributions to obtain actual quartic forms.
Every one of its thirty degree-thirteen ancestor polynomial entries and
eighteen quartic polynomial entries agrees literally with the frozen
displayed bases. It additionally verifies `I^4*h subset (q^4,B^4)` for
each ancestor and every generator of `I^4`.

All 540 actual ancestor-times-quartic product columns and the two target
columns are reduced modulo `(q^4,B^4)` afresh. Their full coefficient
matrix has rank 74, the product-only matrix already has rank 74, and
the independent compressed matrix is **literally equal** to the retained
`74x542` tensor. The union of the uncompressed coefficient rows and stored
rows also has rank 74. Thus no quotient equation or target row was lost
through compression. The entire degree `-3` stage-three Ext image is
independently reconstructed in the same quotient, its injection is
verified, and its union with the 540 product columns has rank 74. This
establishes actual equality with the complete next-stage image, beyond
merely matching its abstract dimension.

Its
[`actual-tensor-reconstruction.log`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.log),
[`terminal result`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction-result.json),
and
[`frozen input manifest`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-input-manifest.json)
retain the exact evidence. Source SHA256:

```text
b2c4722f6d9b5d9ece43d5bfd38348527ceec7577832c37747263a8a9b85c187
```

Log SHA256:

```text
31188e3f9f4940157ed8286c3c3a9ef5a0cc94fa8a95ca299ab6183ee17c4700
```

Two earlier checker scaffolding failures are preserved separately: an
M2 sequence-versus-list mismatch and comparison of differently graded
matrices rather than their polynomial entries. Neither reported a
disagreement of a displayed polynomial or tensor entry. The final
checker uses entrywise polynomial comparison for the graded ancestor
matrix and performs the literal rational tensor comparison successfully.
The first passing source, log, and terminal result are also retained as
`attempt03-pass` records; the final source strengthens that pass by
identifying the complete next-stage image explicitly. The full tensor
development record is in
[`actual-tensor-provenance.json`](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-provenance.json).

The combined
[`audit-manifest.json`](../validation/2026-10-08-family2-quadratic-audit/audit-manifest.json)
binds this note, the three successful final proof checks, their input
closures, the original generation history, and both retained scaffolding
failures. No process from this audit remains running.


---

## Source: 2026-10-08-session-localcoh-family2-quadratics.md

# Exact closure of both quadratic exceptions in endpoint family2

Date: 2026-10-08. Scope: characteristic zero, the fixed rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, the second primitive degree-two endpoint family,
and its complete affine line of lower quartic corrections. The pure top
is the actual saved `t*p^i*r^(3-i)` normalization. This note concerns the
two quadratic exceptions to the generic family2 dual, with no assertion
about the other endpoint families or a nonendpoint top zero.

## Result

**PROVED under the audited actual tensor and coordinate bases:** both
roots of `k^2+1` and both roots of `k^2-2k-1` exclude target `u` for every
`lambda`. These four geometric direction parameters are removed from the
generic family2 certificate's retained locus.

The remaining exceptions to that generic certificate are precisely the
22 geometric roots of the following three factors, each still retaining
its full affine `lambda` fibre:

```text
3k^3+4k^2+9k-4
13k^4+10k^3+2k^2-42k-7
243k^15+810k^14+2646k^13+990k^12-9465k^11-54222k^10
 -114414k^9-166406k^8-34359k^7+301686k^6+897946k^5
 +1296458k^4+1345117k^3+811630k^2+285598k-610
```

Their square-free, pairwise-coprime and primitive-chart status was checked
by the complete generic verifier. This branch does not assert they are
actual incidence survivors. No high-degree factor calculation was begun.

## Exact fields and independent coefficient reconstruction

The two computations use

```text
Kplus=QQ[k]/(k^2+1),       k^2=-1,       discriminant=-4;
Kminus=QQ[k]/(k^2-2k-1),  k^2=2k+1,     discriminant=8.
```

Both quadratics are irreducible over `QQ`, since their discriminants
are nonzero rational nonsquares. A single standard-library verifier
implements exact arithmetic in both fields with rational coefficient
pairs. For `k^2=c+d*k`, it inverts `a+b*k` by the explicit formula

```text
(a+b*k)^(-1) = (a+d*b-b*k)/(a^2+d*a*b-c*b^2).
```

Every rational source denominator is checked by this norm formula to
be a field unit. A restricted AST parser, with no `eval`, reconstructs
all source expressions directly in the quadratic field and its
polynomial ring in `lambda`. On every default verification run, it
rederives all thirty saved seed coefficients, all thirty lower slopes,
and the four direction coefficients from the family2 rational expressions.
It compares them exactly with the certificate; it does not merely trust
a previously reduced coefficient table or a point sample.

The explicit direction formulas checked are

```text
p=1+(k^2+3)/(2-2k^2)*t
     -(k^2+2k+3)/(2(k+1)^2)*t^2,
r=1+(k-3)(k^2+2k+3)/((k-1)^2(k+1))*t
     -2(k^2+1)(k^2-2k-1)(k^2+2k+3)/((k-1)^3(k+1)^3)*t^2.
```

In both fields the verifier checks all 32 actual pure-top identities,
the rank-29 top map, and that the coefficient of `lambda` in the lift
is the exact nonzero kernel vector. Thus the full affine lift fibre is
covered. Its fixed four-by-four Sylvester determinant confirms the
homogeneous direction is primitive, even though `r` loses its quadratic
coefficient at these parameter values.

## Full polynomial duals

Separate reduced 74-by-18 modules were generated from the actual tensor,
using the directly reconstructed field coefficients. In each field,
Macaulay2 computed the full polynomial left-kernel module over `K[lambda]`
and returned target evaluation ideal `(1)`. The resulting duals each have
27 nonzero entries and degree at most two in `lambda`.

The independent verifier checks every coefficient of all eighteen
identities `n^T L(a*+lambda*k0)=0`, and checks `n^T u=1`. It checks the
actual target columns in the tensor are `e72,e73`, so the target evaluation
is tied to the same actual multiplier incidence. Since the fields are
quadratic and separable in characteristic zero, these identities hold
through both embeddings of each field into an algebraic closure. No
specialization or generic-rank extrapolation enters the conclusion.

## Reproduction and terminal execution evidence

Generate both exact field modules without SymPy:

```sh
python3 research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py --generate
```

Run each separate M2 module:

```sh
/opt/homebrew/bin/M2 --script research/computations/session-localcoh-origin-family-2-exception-qplus.m2
/opt/homebrew/bin/M2 --script research/computations/session-localcoh-origin-family-2-exception-qminus.m2
```

Regenerate coefficient certificates and verify everything using only an
ordinary Python:

```sh
python3 research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py --regenerate
python3 research/computations/verify_session_localcoh_family2_quadratics_2026_10_08.py
```

The qplus M2 process was observed terminal with exit code zero in agent-local
tool session `60266`. Its complete output included matrix readiness,
full polynomial kernel completion, full evaluation-ideal export, and
complete polynomial dual export. A parent-local query could not resolve
that handle; the agent's terminal observation and saved outputs are
the evidence for completion. No replay was inferred necessary from the
parent's unavailable handle. The qminus run returned exit code zero
directly. Both coefficient-regeneration checks and the fresh combined
default verification passed. No process from these two branches remains
running.

Evidence is retained in the
[`standard-library generator and verifier`](../computations/verify_session_localcoh_family2_quadratics_2026_10_08.py),
the
[`qplus exact certificate`](../computations/session_localcoh_family2_qplus_audit_2026_10_08.json),
the
[`qminus exact certificate`](../computations/session_localcoh_family2_qminus_audit_2026_10_08.json),
the separate `.m2`, `-dual.txt` and `-evaluations.txt` files for each field,
and the frozen source/output hashes in
[`session_localcoh_family2_quadratics_execution_2026_10_08.json`](../computations/session_localcoh_family2_quadratics_execution_2026_10_08.json).
Canonical frontier documents were left to the root agent.


---

## Source: 2026-10-08-session-localcoh-quadric-direction.md

# Every quartic ancestor in the quadric quotient direction is excluded

Date: 2026-10-08. Fixed `C0=[s^4:s^3t:st^3:t^4]` in characteristic
zero. Status: **PROVED, conditional on the accepted ancestor-to-canonical-
triple reduction and P-037.** This removes a specific conormal direction
for **every** second-defect divisor. It does not remove an entire
positive-D2 degree stratum. The d2=4 Gorenstein possibility outside this
direction is retained.

Let `Q=(q=0)`, with `q=x0*x3-x1*x2`. It is the smooth Segre quadric.
Up to interchange of the two rulings, C0 has class `(1,3)` on Q:
its two projection degrees are three and one. In the balanced finite
normal frame

```text
V=x2-z^3, U=q-z*V/2,
```

the quotient direction `A=-z/2,B=1` is exactly the conormal quotient
of C0 inside Q, of degree -6. Indeed the transverse path
`U=-(z/2)*epsilon,V=epsilon` has q identically zero. Thus its canonical
double is the double divisor `2C0` on Q. This identification uses only
the first quotient; positive D2 and any higher degeneration do not
change the canonical double.

Suppose a common quartic ancestor exists in this direction. Both F and
G contain its canonical triple, hence contain this canonical double.
Their restrictions to Q therefore belong to

```text
H0(Q, O_Q(4,4)(-2C0))=H0(Q,O_Q(2,-2))=0.
```

The last equality follows from the product cohomology of P1 times P1:
a negative degree on either ruling has no global sections. Consequently
both quartics restrict to zero on Q and are divisible by q. Write
`F=q*F2,G=q*G2`. The original equations give

```text
F2*(q*alpha)=u, G2*(q*alpha)=v.
```

This contradicts the all-stage degree-two common-ancestor exclusion
P-037. The nonzero target u ensures `q*alpha` is nonzero. The proof
uses neither a mate supported on C0 nor a false assertion that F
annihilates the quadruple.

In particular the proof includes the otherwise retained `e=1,d2=d3=4`
Gorenstein boundary **when its first quotient is this quadric direction**.
It also includes quartics with zero first-normal symbol. No assumption
that the canonical triple is primitive is made.

The independent exact coefficient check
[`verify_session_localcoh_quadric_direction_2026_10_08.py`](../computations/verify_session_localcoh_quadric_direction_2026_10_08.py)
reconstructs all 35 ambient degree-four monomials and imposes both
vanishing on C0 and the first derivative along the actual Q path. The
combined matrix has rank 25. Its complete ten-dimensional kernel is
`q*H0(P3,O(2))`, checked against ten independent homogeneous quadratic
monomials. This matches the divisor proof and rules out any omitted
quartic first-symbol kernel member.

The rank check is a separate exact verification of the complete quartic
space; the global divisor proof supplies the defect-independent reason.
The two already excluded cubic-factor endpoint directions and four
one-dimensional endpoint fibres are recorded separately in
[`2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md`](#source-2026-10-08-session-localcoh-e1-d1-endpoint-ancestorsmd).
