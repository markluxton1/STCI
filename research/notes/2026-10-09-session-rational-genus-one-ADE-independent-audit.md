# Independent audit: rational sectional-genus-one normalizations

Date: 2026-10-09. Auditor: `normal_global_adversarial`. Status:
**PROVED HERE / independently accepted**. This is the bounded
structural lemma proposed by root; it does not itself exclude mates.
No canonical frontier records were edited.

Binding owner source, subsequently read in full:
[Genus-one del Pezzo reduction](2026-10-09-session-genus-one-delpezzo-reduction.md),
sections 1--5. Its canonical-form representative argument agrees
with the independent proof below. Its proposed lattice filter is
explicitly a separate obligation, not promoted by this audit.

## Statement

Let S be a normal projective rational surface over an algebraically
closed field of characteristic zero, with an ample globally generated
Cartier divisor H of square four. Suppose a general member has genus
one. Let sigma:M->S be its minimal resolution and L=sigma^*H. Then

    K_M~ -L,       K_S~ -H,

S is a Gorenstein del Pezzo surface of degree four with only Du Val
singularities, and sigma is crepant. In particular M is a weak del
Pezzo surface of degree four with anticanonical divisor L. No mate
is required for this reduction.

## 1. The adjoint section is effective exceptional

Rationality gives chi(O_M)=1. Adjunction to a general genus-one
hyperplane section, disjoint from the exceptional locus, gives
K_M.L=-4 and L^2=4. Kawamata--Viehweg vanishing for the nef and big
L gives Hi(K_M+L)=0 for i>0. Riemann--Roch therefore gives

    h0(K_M+L)=1+(K_M+L).L/2=1.

Choose the effective divisor D of this nonzero section. Since
D~K_M+L, one has L.D=0. Every component of an effective divisor has
nonnegative L-degree, and any component mapping to a curve on S has
strictly positive degree because H is ample. Thus every component
of D is sigma-exceptional. This conclusion does not presuppose
Cartierness of K_S or a discrepancy formula.

## 2. Minimality and negative definiteness force D=0

For each integral exceptional prime E, negative definiteness gives
E^2<0. A minimal resolution has no exceptional smooth rational
(-1)-curve. Adjunction on M gives

    K_M.E=2p_a(E)-2-E^2>=0.

Indeed, if p_a(E)=0 it is smooth P1 and E^2<=-2; if p_a(E)>=1,
the expression is positive. Thus D.E=K_M.E+L.E=K_M.E>=0 for every
exceptional prime. If D=sum d_i E_i were nonzero, effectiveness
would give

    D^2=sum d_i(D.E_i)>=0,

contradicting negative definiteness of the exceptional intersection
form. Therefore D=0, and the adjoint section is nowhere vanishing.
This proves K_M~ -L exactly as a linear equivalence. It is stronger
than merely finding an effective representative of a discrepancy
class, and avoids any ambiguity in that interpretation.

## 3. Canonical representatives and the crepant conclusion

Choose a Cartier divisor A representing H. Since K_M+sigma^*A~0,
choose a rational canonical differential theta on the common function
field with

    div_M(theta)=-sigma^*A.

Pushing that same differential down defines the compatible canonical
Weil divisor div_S(theta)=-A. Hence K_S is Cartier and

    div_M(theta)=sigma^*div_S(theta).

This is an actual crepant equality with compatible representatives,
not an inference that an arbitrary effective divisor linearly
equivalent to K_M+L is the discrepancy divisor. Normal surfaces are
Cohen--Macaulay, so Cartier K_S makes the dualizing sheaf invertible;
S is Gorenstein. Since -K_S~H is ample with square four, it is a
degree-four del Pezzo surface.

The crepant-resolution criterion identifies its singularities as
Du Val. A primary author's formulation is
[Reid, The Du Val singularities, Theorem 2.1(2)](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
The standard algebraic criterion applies in characteristic zero.
The exceptional-curve calculation is also intrinsic over the stated
field: K_M.E=0 implies E^2=2p_a(E)-2<0, hence every exceptional prime
is smooth rational with square -2. Negative definiteness makes the
intersection graphs the finite ADE graphs. No quartic slc table is
used to establish these singularity hypotheses.

## 4. Accepted scope and unfinished work

Together with the separately audited nonrational reduction, this
establishes that the entire sectional-genus-one normalization lane
for nonnormal quartics containing C0 is a Gorenstein degree-four
del Pezzo model with an ADE minimal resolution. Consequently the
scoped weak-del-Pezzo/ADE and D5 lattice task has its geometric
hypotheses established. Its lattice proof, enumeration, and remaining
curve and mate hypotheses still require their own acceptance.
This lemma is a hypothesis reduction, not a new conclusion that
all such carriers have no mate.

Rational sectional-genus-two normalizations, their singular points
and conductors, and higher carrier degrees remain outside it. The
unrestricted C0 and universal STCI problems remain open.

`git diff --check` passed. No children were spawned; work froze after
saving this bounded proof and the companion nonrational audit.
