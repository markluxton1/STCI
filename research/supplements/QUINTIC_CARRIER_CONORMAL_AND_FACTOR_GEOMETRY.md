# Quintic carriers: conormal, factorization, residual divisors and low-pole spaces

## Integration guide: carrier structure is not mate existence

The conormal, factorization, residual-divisor, and low-pole-space analyses impose **necessary restrictions on a quintic carrier**. They do not automatically produce or exclude a homogeneous mate. The [endpoint jet/power-descent proofs](QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md), [endpoint residual-support calculations](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md), and [intrinsic A4 conductor/sextic incidence](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md) test additional compatibility conditions. The normalization, factorization, and mate-existence steps have distinct hypotheses; retain their separate computations and counterexamples.

---


Permanent mathematical supplement. The following five complete analyses retain their exact hypotheses, arguments, computations, limitations and corrections. Their constituent proofs are organized by subject rather than by chronological authority; no conditional result is promoted by inclusion.

---

## 1. quintic conormal and delpezzo audit

# Quintic carriers: conormal, Gorenstein and genus-one structural audit

Date: 2026-10-11. Author: `quintic_conormal_audit`, delegated by
`oct11_quintic_structural_frontier`.

Status: **DIRECT PROOF AUDIT; NECESSARY STRUCTURAL REDUCTIONS**. No
quintic-carrier exclusion is claimed. No canonical frontier file was edited.
The scope is the fixed smooth curve

    C=C0=[s^4:s^3t:st^3:t^4] in P3,

over an algebraically closed field of characteristic zero. We use the
accepted conormal calculation `N_C^*=O_P1(-7)^2`, P-005/P-006/P-011/P-015
in [the research record](../RESEARCH_RECORD.md), and, when explicitly stated,
the separately audited exclusion of all integral quartic carriers. The
unrestricted C0 and universal STCI questions remain open.

## 1. Generic order, compressed degree and the missing double divisor

Let X be an integral quintic occurring in a defining pair, and let the
other equation have degree b. P-011 proves that X has generic normal order
one along C; otherwise its equation is divisible by the unique quadric and
cannot be a successful carrier. The complete intersection has generic
multiplicity `r=5b/4`, so `b=4k` and `r=5k` for an integer k>0.

If the all-quartic exclusion is accepted, k=1 is impossible. Thus b>=8,
and the first degree pair to investigate is `(5,8)`, with multiplicity ten.
If X is a minimum integral carrier in a hypothetical presentation,
P-015 gives an actual compressed relation `eC~nH` on X, with

    5 divides e,   n=4e/5>=5,   e>=25/4.

Consequently e>=10 and n>=8. This does not prove that every quintic mate
compresses to degree eight: local Cartier orders and conductor descent can
force a larger value.

Let nu:S->X be the normalization and H=nu^*O_X(1). The unique prime c
over the generic point of C maps isomorphically to the entire smooth C.
Indeed c->C is finite birational, and its coordinate rings are integral
subalgebras of k(C) over the integrally closed rings of C. Hence they equal
those rings. We have `H^2=5` and `H.c=4`.

There is no actual relation `2c~mH` with integer m: intersecting with H
would give `8=5m`. More generally `jc~mH` requires `5|j` and `m=4j/5`.
The quartic normalization double-ribbon construction therefore cannot be
copied literally to degree five. Added resolution exceptional curves have
H-degree zero and do not repair the equation `8=5m`.

## 2. A ribbon obstruction that survives singularities, and its limit

Suppose more generally that a normal surface S carries an actual effective
Cartier divisor R with Weil divisor 2c, where c is smooth. Normal surfaces
are Cohen--Macaulay, so R is a CM curve. Its nilradical J has generic rank
one, and J^2 vanishes generically. The latter is a finite-support subsheaf
of O_R and must be zero by Cohen--Macaulayness. The same argument removes
torsion in J. Thus R is an entire ribbon, including every singular point
of S, and J is a line bundle on c.

If R->P3 reduces to the embedding of C and is an immersion at the generic
point, the pullback of I_C induces a generically nonzero map

    N_C^* -> J.

Therefore `deg J>=-7`; for `deg J<-7` the Hom space is zero. Global
immersion of R is unnecessary. This is the direct proof used in the
accepted [quartic weighted-ribbon audit](2026-10-10-session-weighted-ribbon-conormal-independent-audit.md).

If S is Gorenstein in a neighborhood of R, Cartier adjunction and ribbon
duality give

    deg J=-2-deg((omega_S tensor O_S(R))|c).

Consequently a generically immersed Cartier double would require
`deg(omega_S|c)+R.c<=5`. The use of an actual Cartier double is essential.
For arbitrary S, neither its dualizing sheaf nor a numerical double class
may be silently treated as an invertible sheaf. In the quintic relation
`2c~mH` considered in Section 1, degree already prohibits the hypothesis.

For the standard Cartier adjunction interface, this audit freshly checked
the primary [Stacks effective-Cartier duality section](https://stacks.math.columbia.edu/tag/0B4C)
and [Gorenstein criterion](https://stacks.math.columbia.edu/tag/0DW9).
The ribbon and generic conormal deductions above are written out directly.

## 3. Multiplicity ten without global primitivity or a regular ratio

The separately delegated [multiplicity-ten filtration audit](2026-10-11-session-multiplicity-ten-filtration-audit.md)
supplies a direct finite-flat Frobenius proof, read and checked by this
auditor. A hypothetical CI(5,8) is generically curvilinear by Section 1.
Its saturated graded pieces E_i are line bundles, even at nonprimitive
points, and their actual multiplication gives

    E_i tensor E_(9-i) = E_9,
    E_i=L^i(D_i),   D_0=D_1=0,
    D_i+D_j<=D_(i+j),   D_i+D_(9-i)=D_9.

Complete-intersection duality gives `E_9=O_P1(-38)`. The first quotient
`N_C^* ->> L` therefore leaves exactly

| deg L | direction degree deg L+7 | deg D_9 |
| --- | --- | --- |
| -7 | 0 | 25 |
| -6 | 1 | 16 |
| -5 | 2 | 7 |

An everywhere primitive multiplicity-ten structure is numerically
impossible: it would require `9 deg L=-38`. Genus gives the same socle
equation, not an additional independent restriction.

Writing A=D_2, B=D_3, C'=D_4 and T=D_9, all necessary defect data reduce to

    (0,0,A,B,C',T-C',T-B,T-A,T,T),

    0<=A<=B<=C', 2A<=C', 2C'<=T,
    A+B+C'<=T, 3B<=T.

All inequalities hold coefficientwise at every support point. P-010 also
forces A>0 when deg L=-7. The exact standard-library enumeration in the
linked child record leaves 198/97/13 necessary degree triples, 308 total.
Those are not 308 structures or a classification of higher normal jets.
This auditor did not execute a second copy of that enumeration and adds
no new execution count.

After replacing G8 by G8+HF5, with an ambient cubic H whose restriction to
C is nonzero, one may arrange that both equations have generic normal
order one without changing their ideal. Their saturated common kernel is
represented by a basepoint-free binary pair of degree e=deg L+7. In the
balanced frame their first normal forms can thus be written

    f_1=h ell,  deg h=13-e,
    g_1=k ell,  deg k=25-e.

This does not prove h divides k. The completed local pair

    F=t u+v^10,   G=u

has radical (u,v), is finite flat of rank ten over k[[t]], and has
first-normal ratio 1/t. It preserves the exact pole shield from P-026.
Nor may D_9 be equated with the first-normal Fitting divisor: the child's
rank-ten model `(t x-y^2,x^5)` has respective lengths four and one.

## 4. A global Gorenstein sectional-genus filter

Let pi be the genus of a general pulled-back hyperplane on S. Bertini
avoids the isolated singularities of normal S, and its image is a plane
quintic, so `0<=pi<=6`. A mate supplies `rc~bH`, hence
`c=(4/5)H` numerically as a rational Cartier divisor.

If K_S is Cartier, its intersection with the smooth c is an integer.
Adjunction on the general hyperplane gives `K_S.H=2pi-7`, so

    K_S.c=(4/5)(2pi-7) is an integer.

Thus `pi=1 or 6`. If X is nonnormal, its hypersurface S2 property makes
the nonnormal locus a nonempty curve. A general plane meets that curve,
and normalization reduces the plane-quintic arithmetic genus, so pi<=5.
In that case a Gorenstein normalization under a mate must have pi=1.

More generally, if a global Cartier index t for K_S is known, this gives
`5 divides t(2pi-7)`. No such filter is asserted when K_S is not known to
be rationally Cartier. Rational singularities alone do not supply the
Cartier hypothesis.

## 5. Low sectional genus: the ruled argument audited

For pi<=3, a minimal resolution sigma:M->S has nef and big
L=sigma^*H, with `K_M.L=2pi-7<0`. Thus M has Kodaira dimension minus
infinity and is rational or ruled. Suppose its minimal ruled model has
base genus g>=1. The smooth lifted P1 curve c# maps constantly to that
base, so it is a fiber component. If a is the total L-degree of a fiber,
then `a>=L.c#=4`.

The standard ruled intersection calculation gives

    5=(2g-2)a^2+(7-2pi)a+sum m_i(a-m_i),
    0<=m_i<=a,

with integer m_i supplied by the successive blowups. For pi<=2 its
right-hand side is at least 3a>=12, impossible. For pi=3 only g=1 and
a=4 or5 remain. At a=4 the sum must equal one, whereas each summand is
0,3 or4. At a=5 the sum vanishes, so every m_i is 0 or5. The L-degree of
every fiber component, computed using total transforms and proximity,
is then a multiple of five; it cannot equal four. Hence M is rational
throughout pi<=3. This is a geometric reduction, not a carrier exclusion.

## 6. Sectional genus one forces a single A4 normalization

At pi=1, rationality and surface Riemann--Roch produce an effective divisor
E linearly equivalent to K_M+L with L.E=0. For existence it is enough
that chi(K_M+L)=1 and h2(K_M+L)=h0(-L)=0. E is sigma-exceptional. Minimal
resolution has no exceptional smooth rational (-1) prime, and every
exceptional prime P has `K_M.P=2p_a(P)-2-P^2>=0`. Thus

    E^2=sum coeff_P(E) K_M.P>=0,

contradicting negative definiteness unless E=0. Consequently

    K_M=-L,  K_M^2=5.

The contraction is crepant, with ADE singularities, and S is a degree-five
Gorenstein del Pezzo surface with `K_S=-H`. This uses the same minimality
and negative-definiteness proof as the accepted
[genus-one quartic reduction](2026-10-09-session-genus-one-delpezzo-reduction.md).

In a rational degree-five del Pezzo marking, Pic(M) has basis h,e1,...,e4,
with L=3h-sum e_i. The roots P with L.P=0 and P^2=-2 are exactly
`e_i-e_j` and `+/- (h-e_i-e_j-e_k)`, 20 roots. Indeed writing
P=a h-sum b_i e_i gives sum b_i=3a, sum b_i^2=a^2+2; Cauchy forces
a=0,+/-1, and these equations give exactly the displayed list. Their root
system is A4. Its proper root subsystems are products of A_(r-1), where
the corresponding blocks partition five coordinates; none has a Cartan
matrix denominator divisible by five.

The smooth lift has `c#^2=2`. Write the pulled mate relation as

    c#+Z=(4/5)L,

where Z is its effective rational exceptional correction. Then
`-Z^2=6/5`. The exceptional intersection solution has denominator five,
so its graph must be the full A4, giving exactly one A4 singularity. Its
inverse Cartan matrix has diagonal `(4,6,6,4)/5`; a nonnegative integral
contact vector with norm6/5 is exactly the second or third unit vector.
Every contact vector with at least two positive entries has norm>=2.
Thus c# meets exactly vertex j=2 or3 once and transversely. For j=2,

    5Z=3E1+6E2+4E3+2E4;

the j=3 formula reverses the chain.

Because M is rational, numerical equality of divisor classes is linear
equality. The effective divisor `5c#+5Z` is therefore linearly equivalent
to 4L. Its section descends through `sigma_*O_M=O_S` to an actual section

    Q in H0(S,4H),  div(Q)=5c.

This proves the Cartier equivalence `5c~4H` by descent of an actual section;
it does not merely infer it from a rational numerical relation. Q cannot
be ambient if the quartic-carrier exclusion is accepted. Every mate of
degree b=4k pulls back to scalar Q^k: the actual divisor is 5kc, and the
quotient of two sections with that divisor is a global unit on normal
proper S. The unresolved question is whether any Q^k, k>=2, descends
through the entire conductor to X. No finite bound on k is proved.

## 7. The entire conductor in this genus-one quintic lane

Here `omega_X=O_X(H)` and `omega_S=O_S(-H)`. Finite duality identifies
the actual conductor ideal on S as

    I_S=O_S(-2H).

This is its actual invertible ideal in O_S, not only a numerical class;
its zero divisor D is Cartier in |2H|, with degree ten and arithmetic
genus six. Both reducible and nonreduced D are retained.

The respective Euler polynomials are

    chi(O_X(mH))=(5/2)m^2-(5/2)m+5,
    chi(O_S(mH))=(5/2)m^2+(5/2)m+1,
    chi(I_X(mH))=chi(O_S((m-2)H))
                 =(5/2)m^2-(15/2)m+6.

Consequently the entire downstairs conductor scheme Gamma satisfies

    chi(O_Gamma(mH))=5m-1,

so it has degree five and arithmetic genus two. I_X is MCM over the
Gorenstein hypersurface X, and the sequence
`0->I_X->O_X->O_Gamma->0` makes Gamma CM with no embedded or isolated
zero-dimensional components. MCM biduality gives
`Hom_X(I_X,O_X)=nu_*O_S`; dualizing that sequence therefore gives

    nu_*O_S/O_X=omega_Gamma(-H),

whose Euler polynomial is 5m-4. This retains the actual conductor scheme.
The degree comparison ten versus five does not establish that D->Gamma
is globally finite flat of rank two, or that Gamma is smooth or Gorenstein.
No replacement by a conductor line, branch polynomial, or reduced cover
has been made.

## 8. The unique line, complete restriction and tangent contact

In this degree-five del Pezzo setting the full anticanonical system embeds
S in P5, including its ADE points. On M, Riemann--Roch and characteristic-zero
Kawamata--Viehweg vanishing give h0(H)=6. The restriction to
`H0(c,O_P1(4))`, of dimension five, has a nonzero kernel.

The zero divisor of any kernel section is c+ell: the residual has H-degree
one, so ampleness makes it one reduced integral degree-one curve. Its
anticanonical image is a line, and hence ell is a smooth P1. Its strict lift
has self-intersection minus one by `K_M.ell#=-1` and adjunction. Numerically
`ell=(1/5)H`, so its exceptional correction again has norm6/5 and meets
A4 vertex2 or3 once.

Two distinct degree-one curves would have strict intersection
`1/5-(A4 inverse-Cartan cross entry)`. For these two allowed vertices,
the cross entry is at least4/5, making that intersection negative. There
is therefore exactly one degree-one curve ell on S. All kernel sections
have the same actual divisor c+ell, so their ratios are global units.
The restriction kernel has dimension one, and restriction to c is the
complete five-dimensional degree-four linear system.

The strict c and ell must meet opposite vertices: a common vertex gives
strict intersection `4/5-6/5<0`, while opposite vertices give
`4/5-4/5=0`. They are disjoint on M. The actual Cartier hyperplane divisor
c+ell is generically reduced and CM, hence reduced everywhere. Its
arithmetic genus is one. The union exact sequence gives

    0=chi(O_(c union ell))=1+1-length(c intersection ell),

so the entire intersection has length two, supported at the unique A4
point. Under the full anticanonical embedding, c spans a P4 as a rational
normal quartic, and ell is its tangent line at that point. This audit
does not infer a classification of all projections, uniqueness of the
carrier equation, or any power-descent obstruction from the tangent line.

## 9. The sectional-genus-zero exclusion also passes

Section 5 already proves rationality at pi=0. Restriction to a smooth
general hyperplane P1 of H-degree five gives h0(S,H)=7, since
h1(O_S)=h1(O_M)=0 and the section sequence has constants as its kernel.
The full system maps S finitely and birationally to a nondegenerate
degree-five surface in P6: finiteness follows from ampleness, and
birationality follows because the original four-dimensional subsystem
already maps birationally to X. Its image is a surface of minimal degree.
The surface classification in degree five gives exactly the scrolls
S(2,3), S(1,4), and the cone S(0,5). These normal images make the finite
birational complete map an isomorphism.

The two smooth scrolls contradict a mate because the smooth curve c is
Cartier while its numerical square must equal16/5. Resolve the cone by
F5, with negative section E and L=E+5f. A hypothetical lifted integral
curve of H-degree four has class aE+4f, with a>=0. If a=0, an integral
fiber component is a ruling of degree one. If a>=1, its intersection
with E is4-5a<0, forcing E as a component. A strict transform is not E,
so neither case permits this smooth quartic. The cone therefore cannot
contain the lift even before assuming a mate. This proves the pi=0
quintic-carrier exclusion in every mate degree, using the standard
minimal-degree classification already audited in the
[quartic genus-zero record](SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md).

## 10. Continuation boundary

The highest-value concrete genus-one quintic target is thus the actual
A4 del Pezzo normalization, its anticanonical projection to P3, the smooth
quartic meeting A4 vertex2/3, and descent of powers of its distinguished
nonambient quartic section through the CM degree-five genus-two conductor.
The general `(5,8)` target has three first-quotient directions and the
four-divisor filtration above, with nonregular-ratio strata retained.

Neither target is closed by this note. Higher sectional genera with
non-Gorenstein normalization, normal quintics, higher mate degrees,
carriers of degree at least six, and wholly thick presentations remain
outside any claimed exclusion here.


---

## 2. quintic endpoint factor independent audit

# Independent audit: the endpoint quintic quadric-factor and contact reduction

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit`.
Status: **DIRECT STRUCTURAL REDUCTION ACCEPTED**, under the actual
normalization and endpoint-projection hypotheses below. This is not a
quintic-carrier exclusion. No frozen note, canonical record or existing
integrity seal is edited by this audit.

The owner source is the [endpoint quadric-factor reduction](2026-10-11-session-quintic-endpoint-quadric-factor-reduction.md).
The geometric inputs are the [quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
its [independent conormal/del Pezzo audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md),
and the [explicit model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
The [intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
separately records the required distinction between endpoint and nonendpoint
projection centers. The present statement applies to the displayed endpoint
projection; it does not replace that distinction by a four-parameter global
exhaustion of all quintic carriers.

Work over an algebraically closed field of characteristic zero. Thus S is
the normal degree-five anticanonical del Pezzo model, its sole singular
point is A4, and the actual smooth lifted quartic c and unique line ell
satisfy

    H~c+ell~5ell,       5c~4H,       H^2=5,       H.c=4.

Its actual six anticanonical coordinates restrict on the dense U0-chart as

    U0=1, U1=r, U2=r^2, U3=r^3-rT,
    U4=r^4-(2r^2+r)T+T^2, h=T.

Here `div(h)=c+ell`, c is T=0 on this chart, ell is at infinity, and
the A4 point on ell is `[U3:U4]=[0:1]`. The endpoint projection is

    X0=U0+a h, X1=U1+b h, X2=U3+g h, X3=U4+d h,

with center disjoint from S. Sections 3--7 below additionally assume a!=0.

## 1. Finiteness, image degree and the actual factor

The four sections are independent: their restrictions to c are the four
independent literal monomials of C0. Center avoidance makes them globally
generated. A curve in a projection fiber would have H-degree zero, contrary
to ampleness. Hence the actual map pi:S->P3 is finite onto its integral
two-dimensional image X. Its degree times deg(X) is H^2=5. Generic degree
five would make X a plane and impose a nonzero linear relation between the
four sections; independence excludes that. Therefore pi is finite
birational and X is an integral degree-five hypersurface. Since S is normal,
it is the actual finite normalization of X.

On ell only U3,U4 are nonzero, so pi maps it isomorphically to
`ell'=V(X0,X1)`. This is the tangent trisecant ruling line at the parameter
infinity of the literal C0 and lies on the unique smooth quadric
`q=X0 X3-X1 X2`. In the convention `[C0]=(1,3)` it has class `(1,0)`.

An exact homogeneous identity on S is

    pi*q = h K,
    K=a U4-b U3-U2-(1+g)U1+d U0+(1+ad-bg)h.

For direct verification, `U0 U4-U1 U3=h(-U2-U1+h)`; expanding the four
projection sections gives the displayed formula. An identity on the dense
U0-chart is an identity of the actual sections on integral S. Alternatively
q vanishes on c and ell, so division by the actual Cartier divisor c+ell
has nonnegative valuation at every prime divisor; normality extends the
quotient to a regular section of H. Neither argument performs division
only at the level of numerical classes.

This factorization is special to the endpoint placement. The tangent line
at a nonendpoint of the literal C0 is not contained in q; the same division
cannot be imported to the extra nonendpoint-center parameter.

## 2. The index-five class-group argument, explicitly reconstructed

Use the actual smooth four-point blowup marking from the model audit:

    Pic(M)=Z h_plane + Z e1 + Z e2 + Z e3 + Z e4,
    L=3h_plane-e1-e2-e3-e4,
    E1=e1-e2, E2=e2-e3, E3=e3-e4,
    E0=h_plane-e1-e2-e3, ell#=e4.

The four E's are the entire exceptional A4 chain. Removing them identifies
the remaining open of M with S minus its singular point. Weil localization
therefore gives `Cl(S)=Pic(M)/sum Z E_i`. In this quotient the explicit
relations are

    e1=e2=e3=e4=ell,       h_plane=3ell.

There is no residual torsion relation. Thus

    Cl(S)=Z ell,       [H]=5ell.

For a Cartier divisor downstairs, its pullback is orthogonal to all four
exceptional roots. Write its integral pullback class as
`A h_plane+sum B_i e_i`. Orthogonality to the three differences gives
`B1=B2=B3=B4=B`; orthogonality to E0 gives `A+3B=0`. The pullback is
therefore `-B L`. Conversely every integral multiple of L is the pullback
of the corresponding multiple of H. Consequently the Cartier classes in
Cl(S) form exactly `5Z ell`, generated by H.

This proves the index-five assertion by actual integral relations; no
numerical cancellation or unspecified lattice saturation is needed. In
particular every effective prime avoiding A4 is Cartier everywhere and has
strictly positive H-degree divisible by five.

## 3. The residual divisor is integral, with arithmetic genus one

At A4 every coordinate except U4 vanishes, so `K(A4)=a U4`. If a!=0,
the effective Cartier divisor D=V_S(K) avoids the sole singular point.
Each prime in it is therefore Cartier. Write D as a sum of primes with
positive integral multiplicities. Each has positive H-degree at least five,
while `H.D=H^2=5`. There is exactly one prime, with multiplicity one. Since
D is a Cartier divisor on a Cohen--Macaulay surface, it has no embedded
points. It is integral and reduced.

Cartier adjunction on the Gorenstein S gives

    p_a(D)=1+(H.(H+K_S))/2=1.

This is arithmetic genus one, not a proof of smoothness or geometric genus
one. D can be singular even though the ambient S is smooth along it.

## 4. The restriction is birational and its image has Q-type (3,2)

The actual restricted map D->R=pi(D) is finite. Its degree times deg(R)
is `H.D=5`. Generic degree five would make R a line. But the restriction
kernel of `H0(S,H)->H0(D,H|D)` is exactly `k K`: this follows from
`0->O_S->O_S(H)->O_D(H)->0` and `H0(O_S)=k`. The four projection sections
therefore retain rank at least three on D, so their image cannot be a line.
Thus D->R is finite birational and R is integral of degree five.

Because pi*q=hK, R lies on Q. The actual quintic section X intersect Q
contains the distinct integral curves C0, ell' and R, of degrees four,
one and five. These account for all of its degree ten. As X does not
contain the quadric surface, its restriction is a Cartier divisor on smooth
Q. It is consequently exactly their sum with multiplicity one. Therefore

    [R]=(5,5)-(1,3)-(1,0)=(3,2),       p_a(R)=2.

The exact injection of integral curve rings globalizes to

    0 -> O_R -> pi_*O_D -> F -> 0.

Its cokernel has finite support because the curve map is finite birational.
Arithmetic genera give

    length(F)=chi(O_D)-chi(O_R)=0-(-1)=1.

This is the difference between these two actual curve models. If D is
singular, it is not its normalization, so length(F)=1 is not being called
the entire normalization defect of R.

## 5. The local intersection-length comparison survives singular curves

Let p belong to R intersect C0. Choose a local Cartier equation phi of
C0 on smooth Q at p. It is nonzero in the domain `A=O_(R,p)`, because R
and C0 are distinct integral curves. For the finite semilocal module
`B=(pi_*O_D)_p`, multiplication by its pullback is also injective. Indeed D
is integral and maps dominantly to R, so this function is nonzero in its
function field. Neither smoothness of R nor smoothness of D is required.

Apply multiplication by phi to `0->A->B->F_p->0`. The resulting exact
length comparison is

    0 -> ker(phi:F_p->F_p) -> A/phi A -> B/phi B
      -> coker(phi:F_p->F_p) -> 0.

On any finite-length module the kernel and cokernel of an endomorphism
have equal length. Hence

    length(A/phi A)=length(B/phi B).

Over the algebraically closed field the latter is the sum of the local
intersection lengths at all D-points over p. The phrase nonzerodivisor
belongs to the two integral curve rings A and B. It must not be interpreted
as injectivity on F_p: for example phi can annihilate F_p. The allowed
kernel is precisely what cancels the cokernel length. The owner has
clarified this wording while this bounded audit was in progress.

Summing over p proves that the total zero length of the pulled local
C0-equations on D is the actual intersection product

    R.C0=(3,2).(1,3)=11.

## 6. Scheme divisibility proves exactly seven excess lengths under a mate

Now additionally assume the actual full inverse-support condition of a
hypothetical mate, `(pi^(-1)(C0))_red=c`. Every D-point above R intersect C0
must then belong to D intersect c. Since D avoids A4 and A4 is the unique
c-point above the endpoint, R cannot pass through that endpoint. All
contacts under discussion are therefore on the smooth finite r-chart.

At a contact P in D intersect c, the ambient S is smooth and c has an
actual local Cartier equation t_c. Lift phi from Q to a regular function
on an ambient P3 chart. Its pullback to S vanishes scheme-theoretically on
c, since the actual restriction pi|c is the given embedding into C0.
Thus it belongs to `(t_c)` in O_(S,P), and on D it factors as

    phi|D = (t_c|D) v_P.

Two lifts of phi differ by the local equation q times a regular function;
on D its pullback is zero by `pi*q=hK`. Thus the induced function on D is
well-defined independently of the lift. Divisibility is supplied by this
scheme-theoretic morphism, not merely by set support.

Both factors in the displayed product are nonzero in the local integral
curve ring O_(D,P). They define finite-length quotients. The exact sequence

    0 -> O_D/(v_P) -- multiplication by t_c -->
      O_D/(t_c v_P) -> O_D/(t_c) -> 0

shows that the pulled contact length is the actual D-c intersection length
plus the nonnegative excess `length(O_D/(v_P))`. Full inverse support puts
all its zeros at the actual contacts; there are no other support points.
Since D is Cartier of class H and avoids the only surface singularity,
its ordinary local intersection lengths with c sum to `H.c=4`. Therefore

    sum_P length(O_D/(v_P))=11-4=7.

This establishes the owner's seven-excess reduction in full scheme length,
including singular D and singular R. The difference module of length one
does not bound these excess contacts: its kernel/cokernel contribution
has already canceled in Section 5. High contact between the two different
image curves can occur even when each image branch is smooth.

## 7. Projective scaling and a bounded first-normal support consequence

The actual affine projection coordinates are

    X0=1+aT, X1=r+bT,
    X2=r^3+(g-r)T, X3=r^4+(d-r-2r^2)T+T^2.

In the target X0-chart one must divide by X0. The target parameter along
C0 is `X1/X0=r+(b-ar)T+O(T^2)`. Subtracting its cube and fourth power from
X2/X0 and X3/X0 gives the first-normal coefficients

    U=g-r-3br^2+2ar^3,
    V=d-r-2r^2-4br^3+3ar^4.

This calculation includes projective scaling and agrees with the owner.
The cubic equation of C0 on Q in this chart is
`phi=(X0^2 X2-X1^3)/X0^3`. Its exact numerator pulls back as

    X0^2 X2-X1^3=T*(U+T P1+T^2 P2),
    P1=a^2 r^3+2a(g-r)-3b^2 r,
    P2=a^2(g-r)-b^3.

The restriction of K to c is

    W=a r^4-b r^3-r^2-(1+g)r+d=V-rU.

At every finite contact X0 is a unit, because X0|c=1. If U(r) is nonzero
at a root of W, the second factor in the exact numerator is a unit at that
contact, so the excess there is zero. Thus positive excess can occur only
at common roots of W and U. This is a necessary support condition, not a
bound on the order of the excess at a common root, a first-normal proof of
higher contact behavior, or a parameter exhaustion.

## 8. Exact evidence and remaining boundary

The delegated standard-library [sparse-polynomial checker](../validation/2026-10-11-quintic-endpoint-factor-audit/verify_polynomials.py)
supplies seven exact identities over `Z[r,T,a,b,g,d]`: q=hK, both first-normal
coefficients, W=K|c, W=V-rU, the full cubic residual factor and its relation
to the normalized quadric residual numerator. Its source SHA-256 is
`871099f080b3a69c58f15e6a6bd6a9475fd5cdfbba03008482ff7f23070de8ec`.
The actual [execution record](../validation/2026-10-11-quintic-endpoint-factor-audit/execution-record.json)
binds source, command, stdout and stderr; the observed run returned zero
with seven passing checks. This auditor read the entire checker and its
raw output. It is one original polynomial checker execution, not a
Macaulay2 run or a duplicate verifier count.

The delegated [algebra/contact audit](2026-10-11-session-quintic-endpoint-factor-contact-independent-audit.md)
independently reconstructed both length exact sequences and the projective
scaling calculation. Its final SHA-256 is
`f4e86e9c5e0b88e1bfb9d145e72e5226f884184463abee9928cbdda3bb37cca6`.
Its bounded corollary excludes coprime U,V under the same full-support and
a!=0 hypotheses; it does not bound excess lengths at a common root.

The direct geometric arguments above establish the class-group, integrality,
finite-birationality and intersection-length claims. Passing polynomial
identities do not establish those claims or any universal STCI quantifier.

This audit accepts the factor and, for a!=0, the integral arithmetic-genus-one
residual, Q-type (3,2), length-one curve-model difference and exact seven-excess
necessity. It supplies no contradiction to that necessary condition. The
a=0 boundary, all remaining endpoint contact and conductor jets, the extra
nonendpoint projection-center parameter, other normalization genera, normal
quintics and the unrestricted fixed-C0 and universal STCI questions retain
their separate status. No higher-degree result is inferred from the completed
quartic-carrier theorem.


---

## 3. quintic endpoint factor contact independent audit

# Endpoint quintic factor and seven-contact excess: independent audit

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit/degree_factor_audit`.
Status: **EXACT POLYNOMIAL CHECKS AND DIRECT LENGTH-PROOF AUDIT**.
The separately delegated `finite_curve_length_lemma` reconstructed both
local exact sequences without using the author's proof as a premise.
This note changes no frozen note or canonical frontier file.

Scope: the explicit endpoint projection in the
[factor reduction](2026-10-11-session-quintic-endpoint-quadric-factor-reduction.md),
with center disjoint from S and coefficient a!=0. The
[explicit-model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
and [intrinsic-pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
provide the actual degree-five A4 model and the endpoint-versus-nonendpoint
projection distinction. This audit does not extend the endpoint equations
to nonendpoint projection centers, does not treat a=0, and gives no
upper bound for an excess-contact order.

## 1. Actual quadric factor and projective normalization

Use the six actual anticanonical coordinates in the stated affine chart:

    U0=1, U1=r, U2=r^2,
    U3=r^3-rT, U4=r^4-(2r^2+r)T+T^2, h=T.

For the four projection sections

    X0=U0+aT, X1=U1+bT, X2=U3+gT, X3=U4+dT,

direct expansion in Z[r,T,a,b,g,d] gives

    X0*X3-X1*X2=T*K,
    K=aU4-bU3-U2-(1+g)U1+dU0+(1+ad-bg)T.

This proves the displayed actual-section identity, including its T^2
and T^3 terms. On c, the pullback X0 is one, so X0=1+aT is a unit
in a neighborhood of each finite contact. The genuine projective
affine coordinates there are X1/X0,X2/X0,X3/X0; omitting this
division would generally produce wrong first-normal coefficients.

After clearing the unit denominators, the cubic and quartic residuals
are

    (X2/X0)-(X1/X0)^3 = A_pull/X0^3,
    (X3/X0)-(X1/X0)^4 = quartic_pull/X0^4,
    A_pull=X0^2*X2-X1^3,
    quartic_pull=X0^3*X3-X1^4.

Their coefficients of T are exactly

    U(r)=g-r-3br^2+2ar^3,
    V(r)=d-r-2r^2-4br^3+3ar^4.

The projective normalization contributes no further factor to these
first coefficients because the residual constant terms vanish and
X0|c=1. Their full first-normal rank condition is therefore U=V=0.

The additional exact identities are

    W(r):=K(r,0)=ar^4-br^3-r^2-(1+g)r+d=V-rU,
    A_pull=T*(U+T*P1+T^2*P2),
    P1=a^2r^3+2a(g-r)-3rb^2,
    P2=a^2(g-r)-b^3.

They retain the actual transverse variable T. No replacement of
higher contact by first-normal vanishing is made.

## 2. Residual curves and genus comparison

The author's a!=0 hypothesis makes D_K avoid the sole A4 point,
because K restricts there to aU4. The root lattice is the full
orthogonal A4 in the unimodular plane-blowup Picard lattice; quotienting
gives Cl(S)=Z[ell], with H=5ell. A prime avoiding A4 is Cartier, and
the local class of ell has order five, so its positive H-degree is
a positive multiple of five. Since H.D_K=5, the Cartier divisor
D_K is a single prime with multiplicity one. Thus D_K is an
integral CM curve, possibly singular, and Cartier adjunction gives
arithmetic genus one.

The projection is finite and birational on S. On D_K its degree
divides five. The only alternative to degree one would give a line
image. The restriction kernel of H0(S,H) onto D_K is the single
span of K; hence the four projection sections retain rank at least
three, excluding a line image. Thus D_K->R is finite birational.

On Q the three distinct integral curves C0, pi(ell), R have total
degree 4+1+5=10. They exhaust the quintic section of Q with
multiplicity one. The line pi(ell) is the endpoint ruling, so the
residual class is (3,2), and its arithmetic genus is two. Consequently

    0 -> O_R -> pi_*O_D_K -> F -> 0

has finite cokernel of length one. This comparison remains valid for
singular D_K or R. None of these statements calls D_K a normalization.

## 3. Finite birational pullback preserves the local contact length

Let q be a point of R intersect C0. Set

    A=O_R,q, B=(pi_*O_D_K)_q, F=B/A.

The local Cartier equation phi of C0 on smooth Q is a nonzero element
on the distinct integral curve R. It is a nonzerodivisor on A and B.
Multiplication by phi in the exact sequence above gives

    0 -> ker(phi:F->F) -> A/(phi) -> B/(phi)
       -> coker(phi:F->F) -> 0.

Every endomorphism of a finite-length module has kernel and cokernel
of equal length. Therefore

    length A/(phi) = length B/(phi)
      = sum_(p over q) length O_D_K,p/(pi*phi).

The last equality has no residue-degree weights because k is
algebraically closed. It does not require either curve to be smooth.

**Wording clarification to the source.** Phi is a nonzerodivisor
on the two curve rings, not on the finite cokernel F. A nonunit
cannot act injectively on a nonzero finite-length module. The proof
correctly permits phi to kill part or all of F; kernel and cokernel
then cancel exactly. This clarification does not change the conclusion.

## 4. Scheme divisibility, nonnegative excess, and the exact total seven

Under the full inverse-support condition, every point above R intersect
C0 lies in D_K intersect c. Near such a point S is smooth, since
D_K avoids A4, and c has a local Cartier equation t.

Lift phi from Q to a local regular ambient function on P3, and pull
it back to S. The actual morphism c->C0 makes the pullback vanish
scheme-theoretically on c. It therefore belongs to I_c=(t), and
restriction to D_K gives

    pi*phi=t*v in B_p=O_D_K,p.

Different ambient lifts differ by a multiple of the quadric equation,
whose pullback vanishes on D_K, so the restricted function is well
defined. The actual morphism supplies ideal containment; full reduced
support alone would not. For example t=z^2 and phi=z have identical
zero support in k[[z]], but phi is not divisible by t.

The ring B_p is a one-dimensional domain. The three elements t,v,tv
are nonzero, and the supported quotients have finite length. Cancellation
proves exactness of

    0 -> B_p/(v) --times t--> B_p/(tv) -> B_p/(t) -> 0.

Thus each local excess

    length B_p/(pi*phi)-length B_p/(t)=length B_p/(v)

is nonnegative. Full inverse support ensures that every zero of the
pulled equation, including every zero of v, is among D_K intersect c.
Summing over all contacts and using section 3 gives

    sum contact lengths = R.C0=11,
    sum actual c-intersection lengths = D_K.c=4,
    sum excess lengths = 7.

This proves the claimed necessary reduction even with singular
residual curves. The finite cokernel's length one does not bound
the excess, and the result is not yet a contradiction.

## 5. A bounded first-normal consequence, without a jet-order bound

All D_K intersect c points are in the finite r-chart because D_K
avoids the A4 point, which is the sole point at infinity of c.
On Q in X0!=0 a local equation of C0 is

    (X2/X0)-(X1/X0)^3.

Section 1 therefore identifies v, up to a unit, with
U+T*P1+T^2*P2 on D_K. If U(r_p)!=0 then v is a unit and
the local excess is zero. A point with positive excess consequently
has W(r_p)=U(r_p)=V(r_p)=0. Since a!=0, U is a degree-three
polynomial, so at most three finite points can carry the excess.
In particular coprime U,V exclude a mate under the full-support
hypothesis in this endpoint a!=0 lane.

This does not bound the excess at a common root. Repeated roots,
singular D_K, tangential intersection with c and higher terms of
the actual projection remain relevant. A seven-versus-three point
count would be invalid: seven counts length, not distinct points.

## 6. Execution evidence

The independent standard-library
[source](../validation/2026-10-11-quintic-endpoint-factor-audit/verify_polynomials.py)
passes seven exact sparse-polynomial identities over
Z[r,T,a,b,g,d]. Its SHA-256 is
`871099f080b3a69c58f15e6a6bd6a9475fd5cdfbba03008482ff7f23070de8ec`.
The actual exit-zero execution, command, interpreter path, elapsed
time and raw stream hashes are preserved in the
[execution record](../validation/2026-10-11-quintic-endpoint-factor-audit/execution-record.json).
The recording wrapper is not an additional mathematical verifier.
The ring-length proofs above, rather than these polynomial checks,
supply the contact-length quantifiers.


---

## 4. quintic endpoint quadric factor reduction

# Endpoint quintic projections: quadric factor and residual genus-one curve

Date: 2026-10-11. Author: root.

Status: **DIRECT STRUCTURAL REDUCTION, pending separate proof audit**.
This note concerns only the endpoint placement of the A4 point on fixed
characteristic-zero C0. It neither excludes the whole endpoint family
nor treats the additional nonendpoint projection-center parameter.
The frozen [quintic frontier](2026-10-11-session-quintic-structural-frontier.md)
supplies the normal degree-five del Pezzo, single A4 point, smooth c,
unique line ell, and the actual relations H~c+ell~5ell, 5c~4H.
The explicit model below must be covered by the separately developed
intrinsic pair/projection classification before it is used globally.

## 1. Explicit affine model and endpoint projection

On the open set u!=0 of the anticanonical normalization S, put

    U0=1, U1=r, U2=r^2,
    U3=r^3-rT,
    U4=r^4-(2r^2+r)T+T^2, h=T.

The smooth lifted curve is c:T=0. The unique line ell is at infinity;
the full anticanonical coordinates on it have only U3,U4 nonzero,
with the A4 point equal to [U3:U4]=[0:1]. The endpoint projection is

    X0=U0+a h, X1=U1+b h,
    X2=U3+g h, X3=U4+d h.

Assume its center misses S. Ampleness makes the map finite. Its image
has degree five: the map degree divides H^2=5; degree five would give
a plane image, contrary to the four independent sections. It is thus
finite birational onto an integral quintic hypersurface X.

The image of ell is the ruling line X0=X1=0 on the smooth quadric
q=X0 X3-X1 X2. It is the tangent line at the endpoint of C0 and has
class (1,0) if C0 has class (1,3).

## 2. The pulled-back quadric factors into two anticanonical sections

An exact expansion gives

    pi*q = h K,
    K=a U4-b U3-U2-(1+g)U1+d U0+(1+ad-bg)h.

This is an equality of actual sections of 2H, not only divisor classes.
Equivalently, the vanishing of q on both c and ell implies division
by the actual Cartier hyperplane divisor c+ell; normality makes the
quotient a regular section of H.

This argument is special to endpoint placement. At a nonendpoint of
C0 its tangent line is not contained in the unique quadric, so division
by h cannot be imported into that lane.

## 3. When a!=0, the residual divisor is integral and avoids A4

Let D_K=V_S(K). At the A4 point K=a U4, so a!=0 makes D_K avoid
the only singular point of S.

In the plane-blowup marking, Pic(M) is unimodular of rank five and
the exceptional roots form the saturated orthogonal A4 lattice of H.
Consequently Cl(S) is free of rank one, generated by ell, and Pic(S)
maps to the subgroup generated by H=5ell. An effective prime avoiding
the A4 point is Cartier everywhere and has degree a positive multiple
of five. Since H.D_K=5, D_K has exactly one prime with multiplicity
one. Thus it is integral and reduced. Cartier adjunction gives

    p_a(D_K)=1+(H.(H+K_S))/2=1.

The induced map D_K->R=pi(D_K) is finite and birational. Its degree
divides five. If its degree were five, R would be a line. But the
restriction kernel H0(S,H)->H0(D_K,H) is precisely the one-dimensional
space generated by K, so the four projection sections retain rank at
least three. Their image cannot be a line.

## 4. The image has type (3,2) and normalization difference one

The quadric section X intersect Q contains C0, pi(ell), and R, three
distinct integral curves of degrees four, one, and five. These already
account for its entire degree ten, so its divisor on Q is their sum,
with multiplicity one. Therefore

    [R]=(5,5)-(1,3)-(1,0)=(3,2), p_a(R)=2.

The finite birational map of integral CM curves D_K->R has a finite
length cokernel in

    0 -> O_R -> pi_*O_(D_K) -> F -> 0.

The two arithmetic genera give length(F)=1. This conclusion is
unaffected by possible singularities of D_K or R. It is not a claim
that either curve is smooth.

## 5. A mate would require seven excess contact lengths

Under a hypothetical mate, the full reduced inverse image of C0 is c.
Thus every point of R intersect C0 must lift into D_K intersect c;
in particular R cannot meet C0 at the endpoint, since D_K avoids A4.
On the quadric and on S respectively,

    R.C0=(3,2).(1,3)=11,
    D_K.c=H.c=4.

The local equation of C0 on smooth Q pulls back on D_K to a function
vanishing on the actual intersection with c. It is a nonzerodivisor
on both integral curve rings. Multiplication by that function on the
finite-length cokernel may have a kernel; its kernel and cokernel have
equal length and cancel in the exact comparison. Hence the local
intersection lengths on R equal the lengths of the pulled functions
on D_K. Full inverse support would therefore require a total excess
of exactly seven above the actual four intersection lengths with c.

This is a necessary contact reduction, not yet a contradiction.
Tangential gluing through a singular projected surface can raise the
image contact even when R itself is smooth. The length-one quotient
of D_K->R does not alone bound that increase. First-normal common
zeros likewise do not by themselves bound higher contact orders.
An actual filtered/jet argument for this explicit projection remains
necessary.

## 6. Independent algebraic checks that remain bounded

The factor in Section 2 can be verified by polynomial expansion without
Gröbner elimination. On c in the X0-chart the two first-normal residuals
for the target cubic and quartic parametrization are

    U(r)=g-r-3br^2+2ar^3,
    V(r)=d-r-2r^2-4br^3+3ar^4.

Their common roots are projection-ramification points at finite r.
They do not classify the full inverse-image scheme or all conductor
jets. None of the computations in this note is a universal STCI
certificate, and no mathematical execution count is claimed here.


---

## 5. a4 low pole spaces

# Exact low pole spaces on the degree-five A4 normalization

Date: 2026-10-11. Owner: `oct11_nonendpoint_quadric_structure/nonendpoint_pole_spaces`.

Status: **DIRECT PROOF; PARENT REVIEW PENDING**. No mathematical CAS run is
claimed or required for the proof below. This note supplies the entire pole
filtration, its section spaces through degree six, and the possible degree
partitions of a residual divisor. It does not exclude any remaining projection
family or bound higher contact multiplicities.

Work over an algebraically closed field of characteristic zero. The normal
anticanonical degree-five surface S, its unique line ell, the complete smooth
quartic c, and the plane model are those of the
[intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
In particular H is ample, `H~5ell`, `c~4ell`, and the actual section U0 of H has
divisor 5ell. The
[explicit-model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
verifies the global model and its chart `U0!=0`.

## 1. The entire reflexive section filtration

The complement `S\ell={U0!=0}` is the affine plane with coordinates

    r=x/y, t=z/y=T-r^2.

All functions regular on this complement are consequently `k[r,t]`. Introduce

    v=t^2-r^3=Z0/U0.

At the generic point of ell, use the fourth blowup chart with coordinates
`x,u`, and set `A=1+xu`. The six anticanonical cubics, after the common base
factor has been removed, are exactly

    [Z0:Z1:Z2:Z3:Z4:Z5]
      =[u:A:x^2 A^2:x A:x^3 A^2:x^5 A^3].

Therefore the following are identities in the function field, not merely
first-order approximations:

    r=x^(-2) A^(-1),
    t=x^(-3) A^(-1),
    v=u x^(-5) A^(-3).                         (1)

In particular their exact pole orders along ell are 2,3,5. The last equality
follows from `t^2-r^3=x^(-6) A^(-3)(A-1)`. It records the cancellation that
a weight assignment to r and T alone would miss.

Every polynomial in `k[r,t]` has a unique expression as a finite k-linear
combination of monomials

    r^i t^j v^k,   i,k>=0, j in {0,1}.         (2)

Indeed the presentation

    k[r,t]=k[r,v,t]/(t^2-r^3-v)

is free with basis 1,t over `k[r,v]`, because its relation is monic quadratic
in t. The substitutions in (1) give exact pole weight

    w(i,j,k)=2i+3j+5k                         (3)

and leading coefficient `u^k`. In a sum of terms of maximal weight w, there
is at most one monomial with any fixed k: the equation
`2i+3j=w-5k`, with j equal to 0 or 1, determines j by parity and then i.
Consequently that sum has leading coefficient a nonzero polynomial
`sum a_k u^k` in the residue field k(u). No cancellation of the highest pole
weight is possible. Thus (3) computes the exact ell-valuation of every
polynomial written in its unique normal form (2).

For all n>=0, including n for which nell is not Cartier,

    H0(S,O_S(nell))
      = span_k{r^i t^j v^k : j in {0,1}, 2i+3j+5k<=n}.           (4)

Here `O_S(nell)` is the reflexive divisorial sheaf. To justify the global
equality, a section is a rational function f with `div(f)+nell>=0`. It is
regular on `S\ell`, hence lies in `k[r,t]`; conversely a polynomial with
ell-order at least -n has no negative coefficient at any prime divisor.
On a normal surface those codimension-one conditions are exactly the
definition of the reflexive divisorial sheaf. The A4 point on ell creates
no additional codimension-two extension condition.

## 2. The complete spaces through degree six

| n | Basis of H0(S,O_S(nell)) | Dimension |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | 1 | 1 |
| 2 | 1,r | 2 |
| 3 | 1,r,t | 3 |
| 4 | 1,r,t,r^2 | 4 |
| 5 | 1,r,t,r^2,rt,v | 6 |
| 6 | 1,r,t,r^2,rt,v,r^3 | 7 |

For comparison with the intrinsic anticanonical coordinates,

    U1/U0=r, U2/U0=r^2, U3/U0=-rt,
    U4/U0=v-rt, hsec/U0=r^2+t.                (5)

Thus the n=5 row recovers all six anticanonical sections, and the n=4 row
contains the function `T=r^2+t` defining c off ell.

## 3. Class group and possible residual component degrees

The localization sequence for Weil divisor classes gives

    Z[ell] -> Cl(S) -> Cl(S\ell)=Cl(A2)=0.

There is no nonzero relation on ell. If m ell were principal, intersection
with the ample Cartier divisor H would give `m(H.ell)=m=0`. Hence

    Cl(S)=Z[ell].                             (6)

For an integral prime P, write `[P]=m[ell]`. Then `H.P=m`, so m is its
positive projective degree. If m=1, P is linearly equivalent to ell and is
the divisor of a section of `O_S(ell)`. Since the n=1 row is one dimensional,
the only such effective prime is ell itself. Every other integral prime
therefore has degree at least two. This also directly proves uniqueness of
the degree-one prime from the pole calculation.

Suppose an actual quadric section q has

    div(q)=c+D, and ell is not a component of D.

Its residual divisor D has class `2H-c=6ell` and degree six. Formula (6)
and positivity restrict the multiset of prime degrees, with multiplicities,
to exactly

    6; 4+2; 3+3; 2+2+2.                     (7)

These are possible partitions, not assertions that every projection realizes
each partition. Multiplicities and coincidences remain included; for example
3+3 can be twice the same cubic prime, and 2+2+2 can contain repeated conics.
The assumption excluding ell must be checked for the projection under study.

The residual section has a particularly small exact normal form. Since
`div(hsec)=c+ell` and `div(U0)=5ell`, the rational function

    f=q/(hsec U0)

has divisor `D-6ell`. It belongs to the n=6 row and has exact pole order six
because D does not contain ell. Accordingly

    f=alpha r^3+beta v+gamma rt+delta r^2+epsilon t+zeta r+eta,
    alpha!=0.                               (8)

Equivalently, as a polynomial on the affine plane,

    f=beta t^2+gamma rt+epsilon t
        +(alpha-beta)r^3+delta r^2+zeta r+eta. (9)

The coefficient alpha, rather than either coefficient of t^2 or r^3 taken
separately, detects pole order six. This follows from the cancellation in
(1), and is essential on parameter strata where `alpha=beta`.

## 4. Exact forms of the low-degree prime components

The same normal form gives a useful exhaustive list for degrees two through
four. A prime of degree m other than ell is the closure of the affine zero
divisor of a polynomial with exact pole order m. There are no prime divisors
hidden solely at the singular point.

* Degree two: after scalar normalization the polynomial is `r-r0`. Its affine
  zero curve is a line in A2, integral and reduced, so its closure is the
  degree-two prime.
* Degree three: its polynomial is `t+B r+C`, again after scalar normalization.
  It is a graph, integral and reduced, and has exact pole order three.
* Degree four: its polynomial is `r^2+B t+C r+D`, after scalar normalization.
  It is an integral degree-four prime precisely when B is nonzero: then it is
  a graph over r. If B is zero, it factors over the algebraically closed field
  as a product of two polynomials `r-r0`, with repetition allowed, so is a sum
  of degree-two divisors instead.

Thus factoring the seven-dimensional form (8) decides the partitions in (7)
without treating either r or T as independent weighted variables. It supplies
no higher-contact bound at the singular point or at projection ramification
points.
