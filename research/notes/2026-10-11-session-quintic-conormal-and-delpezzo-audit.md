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
[quartic genus-zero record](2026-10-09-session-normalization-sectional-genus-zero.md).

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
