# Independent audit: nonrational quartic normalizations

Date: 2026-10-09. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted**, including the stronger
no-mate statement. Canonical frontier files were not edited.

Audited source:
[Nonrational quartic normalizations](2026-10-09-session-nonrational-quartic-normalizations.md),
sections 1--6. Work over an algebraically closed field of characteristic
zero. The hypothesis is that X is an integral **nonnormal** quartic
containing the smooth rational degree-four curve C0.

## 1. The rational curve exists without a mate

Automatic generic regularity along C0 was proved in the independent
genus-zero audit. Thus the closure c of the inverse image over the
regular open is one integral curve, finite birational over smooth
C0; normality of C0 makes this map an isomorphism. Other isolated
inverse-image points are irrelevant and need not be excluded.

On a smooth projective resolution sigma:M->S of the normalization,
the strict transform c# maps properly birationally to c. It is
quasi-finite, since a positive-dimensional fiber of a dominant map
of integral curves would be the entire curve. Hence it is finite
and an isomorphism. In particular c# is smooth P1.

For L=sigma^*nu^*O_X(1), the standard plane-section identities give

    L nef and big,       L^2=4,       L.c#=4,
    K_M.L=2pi-6,         0<=pi<=2.

The upper bound uses nonnormality of X; it is not valid for a normal
quartic, whose general plane section has genus three. No mate,
Cartierness of c, or purity of the entire inverse image is used here.

## 2. Ruled classification and cohomology

K_M.L<0 rules out every effective positive multiple of K_M, because
L is nef. Hence kappa(M)=-infinity. The standard characteristic-zero
surface classification makes M rational or birationally ruled.
If it is nonrational, its minimal model is P_B(V) for a smooth curve
B of genus g>=1, and h1(O_M)=g. The classification and minimal ruled
structure are stated in Theorems 3.4--3.5 of the primary author account
[Liedtke, Algebraic Surfaces in Positive Characteristic](https://cims.nyu.edu/~tschinke/books/simons12/lectures.pdf),
which also records their characteristic-zero validity. No nonnormal
quartic classification table is being imported.

Kawamata--Viehweg vanishing and Serre duality give H1(-L)=0. For a
general smooth hyperplane curve Y of genus pi, the exact sequence
0 -> O_M(-L) -> O_M -> O_Y -> 0 therefore injects H1(O_M) into
H1(O_Y), so 1<=g<=pi<=2. No rational-singularity assumption on S is
needed, because this calculation is on smooth M.

## 3. The infinitely near multiplicity bound is valid

Contract M to its minimal ruled model M0=P_B(V) by point blowdowns,
and let M_i be the intermediate surfaces. Push L down successively
to Cartier classes L_i. For a blowup tau_i with exceptional E_i,

    L_i=tau_i^*L_(i-1)-m_i E_i,
    m_i=L_i.E_i>=0.

Nefness descends at each step: for a curve A downstairs and its strict
transform A#, with multiplicity r_A at the center,

    L_(i-1).A=L_i.A#+m_i r_A>=0.

This induction applies at infinitely near centers as well. It does
not assert that all intermediate systems are basepoint-free.

Let a=L0.f be the degree of an entire ruling fiber, preserved at
every stage. It is a positive integer: L0 is nef of positive square,
and Hodge index excludes orthogonality to the nonzero isotropic
fiber class. At any blowup center, choose a component A of its
actual fiber cycle. Every component coefficient is a positive
integer, and intermediate nefness gives L_(i-1).A<=a. Also r_A>=1.
Nefness of its next strict transform gives

    m_i r_A<=L_(i-1).A<=a.

Thus 0<=m_i<=a at every blowup, including a center on an exceptional
component or an intersection of components of a reducible fiber.
This is the substantive issue in the proposed proof, and it passes.

## 4. The intersection identity and contradiction

Numerically write L0=aC+b f, C^2=-e, C.f=1, and
K_M0=-2C+(2g-2-e)f. On the final surface use total-transform
exceptional classes, which are orthogonal with square -1. Then

    4=a(2b-ae)-sum m_i^2,
    2pi-6=a(2g-2+e)-2b+sum m_i.

Elimination yields exactly

    4=(2g-2)a^2+(6-2pi)a+sum m_i(a-m_i).

All terms in the sum are nonnegative. Thus a<=1 for pi=1 and
a<=2 for pi=2. The total-transform convention is necessary here;
using strict exceptional curves would give incorrect intersection
and canonical formulas at infinitely near points.

Every map c#=P1->B is constant by characteristic-zero
Riemann--Hurwitz. The curve c# is therefore a component of one
effective fiber cycle F. Nefness and its positive multiplicity
give L.c#<=L.F=a<=2, contradicting L.c#=4.

**Accepted stronger theorem:** Every integral nonnormal quartic
containing C0 has a rational normalization. The proof applies to
any smooth rational degree-four curve in the surface and requires
no hypothetical mate. It does not apply to normal quartics.

The source's further section dimensions also pass: rationality gives
H1(O_S)=0 by Leray; a degree-four line bundle on the general curve
of genus pi=1 or 2 has H1=0. Restriction yields h0(H)=6-pi, namely
five or four. These dimensions alone imply neither an embedding nor
a classification of the remaining polarizations.

`git diff --check` passed. No children were spawned.
