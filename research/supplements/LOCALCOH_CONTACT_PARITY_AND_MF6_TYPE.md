# Local cohomology contact, parity, and MF6 type geometry

Topical preservation of source mathematics, including qualifications and independent audits. No theorem promotion.

---

## 2026-10-06-localcoh-mixed-contact-pole

# A coprime mixed constant-direction contact pair fails the target equations

Date: 2026-10-06. Status: **PROVED / EXACT COMPUTATION** for the explicit
quartic pair only. The finite all-stage reduction depends on the existing
characteristic-zero quartic local-cohomology bound. This does not exclude
all mixed constant directions.

The exact companion `verify_localcoh_direction_contact_survivor.py` constructs
explicit ambient-coprime quartics \(F,G\) with balanced first symbols
\((2h_F,h_F)\), \((2h_G,h_G)\). Their common scalar divisor is

\[
D(t)=t^4-t^3-3t^2-t+1.
\]

It verifies \(\gcd(F,G)=1\) and the second-contact identity
\(h_F b_G-h_G b_F=0\), where \(b_F,b_G\) are the quadratic normal
coefficients along the kernel of the common first direction. Thus this pair
passes both first-conormal rank and generic length-at-least-three tests.
Its degree-four common scalar divisor also kills the P-010 obstruction class
\(h_{1/2}\), as checked independently by
`verify_localcoh_constant_direction_apolar.py`.

The complete target-specific generic inverse-system equations are finite.
An order-four ancestor has the ten inverse-monomial coefficients with
\(i+j\le3\), for monomials \(U^{-i-1}V^{-j-1}\). Multiplication by the
two quartics gives twelve linear equations over \(\mathbf Q(t)\), with
socle right sides \(1,t^2\). These are the actual balanced-frame
representatives of \(u,v\), since the first normal determinant of \((q,B)\)
relative to \((U,V)\) is \(t^3\).

The exact linear solution forces its four highest inverse coefficients to be

\[
(8,-4,2,-1)\,C(t),\qquad
C(t)=\frac{(t+1)D(t)(2t^6-3t^5+2t^4-3t^3-2t+1)}
 {5t^4-2t^3+6t^2-2t+5}.
\]

The lower principal-part freedom does not affect this coefficient. The
script now explicitly asserts that the displayed numerator and denominator
are coprime and that the denominator has degree four; earlier Oct5 output
merely printed the fractions. Therefore \(C(t)\) has finite poles over
the algebraic closure. A global highest symbol is a regular section of
\(O(7)^4\) in the fixed balanced frame, and cannot have these poles.

Thus this pair has no global quartic common ancestor for the two fixed
targets. The finite principal-part bound makes the exclusion apply at every
direct-limit stage. The lesson is concrete: rank-one first symbols, valid
second contact, and a permitted scalar pole divisor can all hold while the
target-specific highest ancestor coefficient still has forbidden poles.


---

## 2026-10-06-localcoh-parity-dual

# A corrected polynomial-dual exclusion for the normalized parity family

Date: 2026-10-06. Status: **PROVED BY AN EXACT POLYNOMIAL IDENTITY** over QQ,
hence over every characteristic-zero extension. This is a family exclusion
inside the finite quartic local-cohomology problem for C0. It does not
resolve the full quartic incidence or the general projective STCI question.

## The family and statement

In the balanced normal frame, take the degree2 normal-dual direction

    nu=(1+t²,c t),

with pure cubic top symbol coefficient h=1. For c≠0 its homogeneous pair
(s²+t²,c st) is coprime and has primitive degree2. The calculation also
includes c=0 as a boundary specialization. The unique nonzero top-lift line
has h constant: the top-image obstruction to h=t has a nonzero constant
component, independent of c. This is checked uniformly by the verifier.

Let a(c,lambda) be the chosen polynomial top lift plus an arbitrary multiple
lambda of the unique T3[-7] section. Every ancestor with this normalized top
symbol has this form. Let L(a) be the74×18 actual quartic multiplication
matrix from the exact tensor, whose target columns are e72 and e73.

There is a polynomial row vector n(c,lambda) over QQ[c,lambda] such that

    n(c,lambda)^T L(a(c,lambda)) = 0,
    n(c,lambda)^T e72 = 1.

Consequently **no quartic multiplier produces u at any point of this
family**, even over an algebraic closure. In particular this family has no
common quartic ancestor for u,v. The assertion includes every lower T3
coefficient and every c; it has no exceptional parameter locus. A nonzero
scalar multiple of the top coefficient is absorbed by scaling the ancestor
and the multiplier, so the h=1 normalization loses no nonzero top lift.

The same saved dual has n^T e73 equal to a linear polynomial in c. The one
dual therefore proves the common-ancestor exclusion through u; it should
not be represented as separately excluding v at that linear polynomial's
root. Separate one-target Groebner runs in the companion research lane
returned the unit ideal for both targets, but that additional v assertion
is not needed for this certificate.

## Exact certificate and verification

The complete polynomial coefficients are saved in
`../computations/localcoh-incidence-parity-dual-2026-10-06.json`. There are24
terms in the30 ancestor-coordinate polynomials and173 terms in the74 dual
entries. Terms are stored as rational coefficients with their c and lambda
exponents, so the identity is portable and inspectable.

Run from the repository root:

    python3 research/computations/localcoh-incidence-parity-dual-2026-10-06.py

This uses only Python's standard library. It checks coordinate-file hashes,
source-basis agreement, the top symbol and its h=t obstruction, contracts
all540 actual quartic products, multiplies the polynomial dual, and verifies
all18 zero identities plus the constant1 target identity. It contains no
Groebner call and no sampling.

The exact discovery/reproduction script is
`../computations/localcoh-incidence-parity-dual-2026-10-06.m2`. Its polynomial
ring has only c,lambda. For the74×18 matrix L it computes the kernel of
transpose L, evaluates its generators on e72, verifies that this evaluated
ideal is the unit ideal, and lifts1 through those generators. The resulting
polynomial dual is also saved in a readable text file with the same basename.
This is a small polynomial module calculation, rather than the unfinished
66-variable full bilinear Groebner attempt. The independent Python identity
check is the mathematical certificate.

## Extension to the nondegenerate unnormalized parity family

The curve has the ambient torus automorphism

    (x,y,z,w) -> (x,l y,l³ z,l⁴ w),     l≠0.

For the balanced normal coordinates U=w-(3/2)tz+(1/2)t⁴ and V=z-t³,
these coordinates scale by l⁴ and l³. Thus the geometric pushforward of a
normal-dual direction (p(t),r(t)) is

    (l⁴ p(t/l), l³ r(t/l)),

up to the immaterial common nonzero scalar used to describe its projective
direction. For p=a0+a2 t² and r=b1 t with a0 a2≠0, divide this pair by
l²a2 and choose l²=a2/a0. The result is

    (1+t²,(b1/a2)t).

Such l exists over an algebraically closed characteristic-zero field. The
pure-top coefficient h remains constant up to a nonzero scalar. Both target
classes are torus eigenvectors (their pullback factors are l^-7 and l^-5),
so existence of an ancestor is preserved up to nonzero target and multiplier
scalings. Therefore the normalized identity excludes the whole primitive
parity family with a0 a2 b1≠0. Cases with a0 a2=0 require separate handling
and are not obtained by this normalization argument.

## Audit provenance and limits

The earlier saved parity monomial-functional script used only the first row
of `basis(4,I)` as if it were the quartic basis. In Macaulay2 that row records
coefficients of one ideal generator, so those products had the wrong degree.
Its asserted vanishing of degree17 coefficients was vacuous. The present
certificate is a corrected proof: it uses the tensor whose quartic columns
sum all four ideal-generator contributions and whose full product span has
exact dimension74=dim E3[-3]. The older faulty script is not part of this
proof.

Validation on Oct6: the complete actual tensor and basis regenerated
byte-identically; Macaulay2 1.26.06 reran the two-variable module calculation;
the standard-library Python verifier checked the polynomial identity. The
remaining degree0/1/2 direction strata and the complete finite quartic
incidence remain separate research tasks.


---

## 2026-10-06-mf6-type3-independent-audit

# Independent audit of the MF6 degree-three nonregular exclusion

Date: 2026-10-06. One bounded audit of
`2026-10-05-mf6-further-audit.md` and
`../computations/verify_mf6_type3.py`. Scope: characteristic zero, the
monomial quartic C0, constant quotient degree e=0, and a hypothetical
(4,6) defining pair with (deg D2,deg D3)=(3,6). No new global candidate is
constructed. No shared report or verifier was edited.

**Verdict:** the stated exclusion of the entire nonregular branch passes.
No mathematical gap was found in the cubic-pole argument. Its conclusion is
that the first-normal ratio must be regular; it does not exclude existence
of the remaining regular member or an STCI representation in other types.

## 1. Why the DVR computation uses the actual quotient

At a support point, choose a lifted support parameter t and complete.
The ambient ring is k[[t,m,y]], where y maps to a generator of E1 and
m lies in N2. The finite-flat length-six algebra B is generated over
R=k[[t]] by m,y: nilpotence turns the ambient formal series into finite
polynomials. Since N4 is saturated, B/N4 is R-free, and it embeds in its
generic algebra K[y]/(y^4). Its image is exactly R[m,y], not an arbitrarily
selected sublattice of that generic algebra.

Modulo y^4 the generic image is

    m=f2*y^2+f3*y^3.

The complete list of necessary generating words is

    1,y,y^2,y^3,m,ym,

because m^2=my^2=y^4=0. In particular no later normal coefficient or
extra word supplied by the sextic can enlarge the degree-three lattice.
The quotient need not itself be Gorenstein; its generation and saturation
are the relevant inputs.

If f2 is regular, subtract f2*y^2 from m, using an allowed R-coefficient
change of generator. Then N3 has coefficient ideal R+R*f3 in the y^3
line, proving

    ord D2=0, ord D3=max(0,-val f3).

If val f2=-a<0, use m as the degree-two pivot. To cancel its y^2
coefficient, an integral combination c*m+d*y^2 must have
d=-c*f2 in R, which forces c into f2^-1 R. Consequently all remaining
degree-three vectors are generated by

    y^3, f2*y^3=ym, (f3/f2)*y^3=f2^-1*m-y^2.

Conversely all three displayed vectors belong to the actual lattice. Thus
its degree-three coefficient ideal is exactly

    R+R*f2+R*(f3/f2),

with minimum valuation min(0,-a,val f3+a), giving

    ord D2=a, ord D3=max(a,-a-val f3).

This is an equality proved over the DVR, not a pole-count heuristic or a
sampling result. Changing to another regular ambient normal frame would
change the displayed f2,f3 but not the resulting canonical defect divisor.
The computation uses the stated local frames on each chart throughout.

## 2. Exhaustion of the triple and quartic parameter spaces

For degree three, I independently recomputed the killing-matrix nullspaces
from the quadratic cocycle already derived by the defect12 verifier.
For every theta!=0 the finite-chart kernel is

    (d0,d1,d2,d3)=(0,2theta,1,0).

At theta=0 it is the span of z^2,z^3; at the missing quotient point it is
the span of 1,z. The latter two families have an unavoidable additional
homogeneous linear factor common to delta,gamma, hence are not flat
triples. This includes the case where that factor vanishes at infinity.
For theta!=0 the corrections gamma_U=3/8 and gamma_V=6theta^4 are units;
the triple is flat. The torus action permits theta=1 without discarding
any nonzero quotient direction.

The verifier builds the full I_C(4) space and imposes both the proportional
first-normal condition and the quadratic triple-membership condition.
The resulting pencil is therefore an ambient quartic pencil, not a list
of abstract first-normal coefficients. Its first-normal map is injective:
the unique ambient first-normal kernel is q^2, which does not contain the
triple. Thus no missing quartic can preserve the prescribed first forms
while changing the cubic coefficient.

The verifier was rerun successfully with

    /private/tmp/stci-cas-venv/bin/python research/computations/verify_mf6_type3.py

It also reruns the complete degree-one and degree-two exclusions.

## 3. Independent extraction of the cubic coefficients

I checked the formal-root coefficients using a different extraction from
the expanded quartic. Express a local jet in m,y as

    F=h*m+c20*y^2+c11*m*y+c30*y^3+terms of higher relevant order.

Then

    f2=-c20/h, f3=-(c11*f2+c30)/h.

Terms in m^2 or m*y^2 have order at least four after substitution, so they
cannot affect this calculation. Applying these identities directly to
the complete quartics F0,F1 reproduces

    delta=z(z+2),
    P=alpha*z^2(z+2)^2+beta*(z^2+4)(z^4+16),
    N=alpha*z(z+2)(z+4)
      +beta*(z^5+2z^4+16z^2-16z+96),
    h=-2*delta*P,
    f2=3/(8*delta), f3=-N/(16*delta^2*P).

The generic quartic coefficient h is nonzero for every nonzero pencil
member. Thus its formal root is forced in the actual generic sextuple,
and the local lemma applies to the canonical quotient B/N4.

## 4. The resultant and every exceptional cancellation

The exact resultant is

    Res(P,N)=2^34*beta^10*(alpha+4beta).

For beta!=0 the denominator P is a degree-six section, nonzero at
0,-2,infinity. If alpha+4beta!=0, the numerator and denominator are
coprime and its full six zero units produce poles off D2. The local
lattice lemma then gives deg D3>=6+3=9.

At alpha=-4beta, scale beta=1. Direct factorization gives

    P=(z-2)^2*(z^2+2z+4)^2,
    N=(z-2)*(z^4+4z^3+4z^2-48),
    gcd(P,N)=z-2.

Exactly one pole unit cancels, leaving polar degree five off D2 and
deg D3>=5+3=8. The other repeated-root parameters of P do not create
additional cancellations. An independent discriminant check gives

    disc(P)=-2^24*beta^3*(alpha+4beta)^3
            *(alpha^2+80alpha*beta-128beta^2)^2.

At the extra quadratic parameter values the resultant is nonzero, so
the repeated roots retain their full pole multiplicities. All pencil
members with beta!=0 therefore fail the required deg D3=6.

## 5. Direct infinity check for the remaining member

For beta=0 the finite-chart root has

    f3=-(z+4)/(16*z^3*(z+2)^3).

At 0 and -2, f2 has pole order one and f3 has pole order three; the
lattice lemma gives ord D3=2 at each point. There are no further finite
defect points.

I independently expanded the homogeneous F0 in the actual other ambient
chart, using

    x3=1, x2=w, x1=w^3+2U', x0=w^4+V'/2+3wU'.

This follows directly from U'=a'/2 and V'=-3w*a'+2b'; it does not freeze
the moving normal coordinate or substitute w=1/z off the reduced curve.
In m'=U'+V',y'=V', the coefficient-extraction identities in section 3
give

    h'=-2*w^3*(1+2w)^3,
    f2'=6/(w*(1+2w)),
    f3'=-8*(18w^2+8w-1)/(w^3*(1+2w)^3).

At infinity, w=0, both numerators needed for the valuation calculation
are units. Hence the third contribution is again ord D3=2. This proves
the actual divisor equalities

    D3=2D2, H=3D2,

where D2 consists of the three simple points 0,-2,infinity. There is no
inference of the infinity contribution solely from a total degree.

MF6 now gives A=3D2=H. The pole divisor of the first-normal quotient is
H-A, so it is zero. This establishes the claimed nonregular-branch
exclusion. The argument still permits the beta=0 regular member.

## 6. Scope and the retained degree-five caveat

The completed further-audit note correctly retains the degree-five pure
triple family

    delta_U=d0+z^2*r(z), deg r<=3,
    gamma_U=3r/8, gamma_V=-3d0/8.

If d0!=0, there is no common zero: at a finite common zero one would
have r=delta=0, implying d0=0, while gamma_V is a nonzero constant on
the other chart. In particular d0=1,r=0 is flat and the explicitly
recorded quartic -2x0^3x3+3x0^2x1x2-x1^4 passes its triple condition.
Thus the note does not accidentally promote the degree-three and
degree-four endpoint-flatness failures to a blanket pure-direction
exclusion.

No additional realization or exclusion follows from this audit. The
remaining regular member, the nonregular type (4,5), e=1, and higher
carrier degrees require their own arguments. The precise distinction
between saturated and ordinary powers from the pairing audit remains
essential at every stage.


---

## 2026-10-06-mf6-type4-incidence

# Remaining e=0 type (d2,d3)=(4,5): exact triple/quartic incidence

Date: 2026-10-06. Characteristic zero; monomial quartic C0. Status:
**proved parameter reduction; exact exploratory quartic and cubic data;
exceptional loci remain open.** No exclusion of this complete defect type
is claimed. The established low-defect and type-three exclusions are in
`2026-10-05-mf6-further-audit.md`, independently audited in
`2026-10-06-mf6-type3-independent-audit.md`.

## Every possible degree-four triple

The two pure constant quotient directions fail flatness for d2=4: their
killing section has an additional degree-two factor common to delta and
gamma. Thus normalize every possible mixed constant quotient to
`m=U+V,ell=V`, using the torus as in the type-three proof.

Multiplication of the exact h2 cocycle by a section delta of O(4) must
kill both Laurent coordinates of `H1(O(-3))`. Its complete kernel is

    delta=A(z^2+2z)+B(z^3-4z)+C(z^4+8z+16),
    gamma_U=3[A+B(z-2)+C(z^2-2z+4)]/8,
    gamma_V=6Aw+6B(1-2w)+48Cw^2.

If C=0, delta and gamma are the degree-three triple data multiplied by
the homogeneous linear section `A+B(z-2)`. That section has a zero,
including infinity if B=0, so the proposed triple is not flat.

If C!=0, normalize C=1 and write

    delta=A(z^2+2z)+B(z^3-4z)+z^4+8z+16,
    R=A+B(z-2)+z^2-2z+4, gamma_U=3R/8.

The elementary identity `delta=z(z+2)R+16` gives the exact resultant
`Res_z(delta,R)=256`, independent of A,B. Thus
there is no finite common zero. At infinity delta_V has value one, so
every point `(A,B)` gives a flat embedded triple. Its D2 divisor is the
degree-four zero divisor of delta and has no infinity component. This
exhausts the triple parameter space rather than selecting a generic chart.

## Complete quartic equation and its cubic-pole constraint

Let `F=sum c_i F_i` range over the complete eight-dimensional quartic
space with first normal form `h(U+V)`; the basis is derived from the
18-dimensional `I_C(4)` by the preceding verifiers. Write

    Q=coeff_y^2 F(m=0,y),
    E=coeff_my F(m,y), K=coeff_y^3 F(m,y).

Containing the specified triple requires exactly the quadratic identity

    delta Q+(3/8)R h=0.

The resulting coefficient matrix is 13 by 8, affine in A,B. It has rank
seven over Q(A,B), so its generic solution space is a unique quartic up
to scalar. The exact polynomial kernel vector, full coefficient matrix,
and the resulting polynomials S,T are preserved in
`research/scratch/mf6_type4_incidence.json`. The script
`research/scratch/explore_mf6_type4.py` derives these data using
fraction-free polynomial-domain operations and checks every kernel
equation exactly. Rank-drop parameter loci have not been classified;
the generic kernel must not be called the complete quartic family there.

Since delta and R are coprime, the quadratic identity forces `h=delta S`.
S is a section of O(5). The formal cubic coefficient of the quartic is

    f2=3R/(8delta),
    f3=-(3R E+8delta K)/(8delta^2 S)=-T/(8delta^2 S).

At every finite point the third-piece DVR lattice lemma from the preceding
note gives the exact coefficientwise formula

    ord(D3-D2)=max(0,ord S-ord T).

This also holds at finite multiple roots of delta, because R is a unit
there and its pole order in f2 is exactly ord delta. The target d3=5
permits only one total unit of this excess. Therefore every candidate
requires that all but at most one of the finite zeros of S cancel in T.
An additional infinity contribution must be calculated with the moving
second frame whenever S has an infinity zero. It cannot be guessed by
the affine polynomial degrees.

At A=B=0 the matrix has rank seven and its S polynomial, up to scale, is

    41z^5+28z^4+56z^3+176z^2-80z+704.

Its gcd with T is exactly one. Thus the local cubic calculation forces
at least five excess units and d3>=9, excluding this parameter. More
generally, rank seven, a nonzero leading coefficient of S, and coprimality
of S,T are open conditions. This exact point proves that the generic
degree-four triple/quartic incidence is excluded; the surviving possible
parameters lie in a proper algebraic exceptional locus. Additional exact
sample parameters also have gcd one but do not constitute a universal
exclusion.

## Continuation and failed computational shortcuts

The required next calculation is the rank-drop boundary together with
the subresultant conditions `deg gcd(S,T)>=deg S-1`, followed by the direct
infinity chart. Both boundaries are necessary: a generic nullspace vector
does not identify every special solution, and affine loss of degree in S
can hide an infinity pole.

Run

    /private/tmp/stci-cas-venv/bin/python research/scratch/explore_mf6_type4.py

to reconstruct the exact generic incidence. The optional `--resultant`
attempt computes `Res_z(S,T)` as a polynomial in A,B; it may be expensive
and is not required to reproduce the proved reductions. Initial direct
symbolic `Matrix.rank()/nullspace()` operations expanded rational
expressions unnecessarily; polynomial-domain `DomainMatrix.nullspace()`
gave the same exact kernel rapidly. The full generic resultant attempt
was interrupted after several minutes of coefficient growth; no resultant
answer is recorded or claimed. The exact S,T inputs are preserved. This
distinction affects computation cost, not the scope of the result.

`research/scratch/mf6_type4_resultant.m2` preserves the same exact S,T input
for an alternative Macaulay2 resultant attempt. That attempt was also
interrupted without a returned result. There is no pending computation
and no resultant output to treat as evidence. A more useful next attempt
may compute the high-gcd subresultant ideal directly, instead of expanding
the full degree-zero resultant.

The type `(4,5)` still contributes the nonregular coarse pole lengths
3 and 4. The e=1 types `(0,4),(1,3),(2,2)` still contribute pole lengths
4, 5, and 6 as detailed in the preceding note.
