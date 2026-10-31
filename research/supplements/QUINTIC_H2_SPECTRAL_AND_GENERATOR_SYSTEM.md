# Quintic h=2: spectral operators, determinant generators, and actual coefficient units

## Integration guide: spectral acceleration versus existence

The spectral accelerator, generator equations, and rank conditions are **different presentations of constrained incidence calculations**, conditional on the same quintic h=2 setup. Compare [the monic ODE/open derivation](QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md) for the underlying action equations and [the degree-five incidence frontier](QUINTIC_H2_INCIDENCE_AND_LOCALCOH_FRONTIER.md) for the proposed global elimination step. A vanishing determinant, an exact generator identity, or an open-chart incidence computation does not by itself prove that the required homogeneous mate exists or that all residual support disappears. Retain the individual exact certificates and audits.

---


The three complete proofs below are the independently reconstructed spectral, determinant, and actual-unit arguments. Their strongest exact forms replace duplicate proposals; the exporter section concerns representation of the same fixed polynomials and establishes no incidence result. Work in characteristic zero on each declared actual inverse-map domain unless a universal identity is explicitly separated.

---

## 2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit

# Independent audit: one eta spectral accelerator for the shared ODE

Date: 2026-10-15.

Status: **PASS. The proposed single spectral polynomial belongs to
the localized shared ODE ideal, with exact scheme-theoretic scope,
including nonreduced parameter rings.** The accepted ODE presentation,
coefficient unimodularity, derived degree equation and degree-six
Hamiltonian characteristic polynomial are premises and were not
replayed.

This note audits only the new degree-five spectral input and its
combination with the accepted shared ODE. It gives no actual-parameter
emptiness or conductor-descent conclusion.

The reviewed proposal is
[the unified spectral-accelerator note](QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit).

## 1. Ring, sign conventions and the proposed polynomial

Let A be the actual coefficient ring on the accepted localized finite
inverse-map domain, and let

    B=A[d,u]/I_ODE

be the shared ODE quotient, with any previously appended equations
already proved to belong to the same ideal. In particular, over this
characteristic-zero field algebra,

    h=x^2+vx+w,       h*q'=(dx+u)q,
    (q5,q6)=B,
    (d-5)(d-6)=0.                                     (1)

The q_i are the captured sextic coefficients. All original actual-map
and projection conditions remain. No domain or support statement
outside that localization is inferred here.

Put

    eta=dv-2u,       Delta=v^2-4w,
    P6(T)=T*(T^2-4Delta)*(T^2-16Delta)*(T^2-36Delta),
    P5(T)=(T^2-Delta)*(T^2-9Delta)*(T^2-25Delta).

The new accelerator is the one polynomial

    P=(d-5)*P6(eta)+(6-d)*P5(eta).                    (2)

The sign of eta corresponds to D_H=H_t partial_s-H_s partial_t,
with H=t^2+vst+ws^2. Reversing that derivation would reverse the
eigenvalue sign; no such convention change is made here.

## 2. The new degree-five characteristic polynomial

For H=t^2+vst+ws^2, the Hamiltonian action D_H on a degree-n
form with coefficient vector a=(a0,...,an) is the matrix A_n with

    (A_n a)_i=(n-2i)v*a_i+(2n-2i+2)a_(i-1)
                         -2(i+1)w*a_(i+1).              (3)

In particular the new degree-five matrix is

    A5 = [ 5v  -2w    0    0    0     0 ]
         [ 10   3v  -4w    0    0     0 ]
         [  0    8    v  -6w    0     0 ]
         [  0    0    6   -v  -8w     0 ]
         [  0    0    0    4  -3v  -10w ]
         [  0    0    0    0    2    -5v ].


On the degree-one coordinate basis (s,t), the coefficient matrix of
D_H is

    M=[ v   -2w ]
      [ 2    -v ],       M^2=Delta*Id.

Over the universal ring QQ[v,w], on the dense locus Delta nonzero
and after adjoining a square root rho of Delta, the eigenvalues on
the two-dimensional representation are rho and -rho. On degree-five
binary forms the derivation therefore has eigenvalues

    5rho, 3rho, rho, -rho, -3rho, -5rho.

Their characteristic polynomial is exactly P5(T). Both the matrix
characteristic polynomial and this displayed expression are
polynomial in v,w, so equality on the dense locus is a universal
polynomial identity. It specializes under every coefficient-ring
map, including Delta=0 and nonreduced bases. In particular, using
P5 does not require a discriminant inversion beyond those already
present in the actual coefficient chart.

The analogous degree-six characteristic polynomial P6 is an accepted
premise. The new proof does not rerun its computation or its audit.
Cayley--Hamilton applies to each of these operator matrices over
every commutative coefficient ring.

## 3. The two weights are combined by exact central idempotents

In B define

    e6=d-5,       e5=6-d.

Equation (1) gives

    e6+e5=1,       e6*e5=0,
    e6^2=e6,       e5^2=e5,
    d*e6=6e6,      d*e5=5e5.                          (3)

These are identities in the full quotient, not decompositions only
of its reduced point set. They therefore apply if B has nilpotents.
They supply a proof of the one polynomial (2); they do not require
running separate parameter or factor computations.

In the component ring e6*B, the ODE degree is six. Homogenizing and
using Euler's identity in degree six gives

    s D_H Q=6H_tQ-2H Q_t
           =[(6v-2u)s+2(6-d)t]Q.

Here d=6, so cancellation of the polynomial variable s gives

    D_H Q=eta Q            in the e6 component.        (4)

The variable s is not a zero divisor in a polynomial ring over any
base; this cancellation makes no reducedness assumption.

In e5*B, the top ODE equation E7=(6-d)q6 gives q6=0. Thus the
homogeneous sextic is s*Q5, with

    Q5=sum_(i=0)^5 q_i*s^(5-i)*t^i.

After cancellation of s, its ODE is H*(Q5)_t=(us+5t)Q5. Euler's
identity in degree five now gives

    D_H Q5=(5v-2u)Q5=eta Q5.                           (5)

There is no missing eigenvalue shift: Q5 has degree five, while the
original degree-six form retains its additional factor s. In this
component q6 is zero, and q5, rather than q6, is a unit by (1).

## 4. Cayley--Hamilton gives scalar membership, not just annihilation

Apply the accepted degree-six Cayley--Hamilton identity to (4).
It gives P6(eta) times every coefficient of Q equal to zero in e6*B.
The coefficients q5,q6 generate the unit ideal in that component,
because their unit-ideal relation in (1) survives multiplication by
e6. Hence

    e6*P6(eta)=0.                                     (6)

Apply the new degree-five identity to (5). It gives P5(eta) times
every coefficient of Q5 equal to zero in e5*B. Here q6=0 and
(q5,q6) is the unit ideal, so q5 is a unit. Therefore

    e5*P5(eta)=0.                                     (7)

Adding (6)-(7) proves P=0 in B. Equivalently,

    P belongs to I_ODE in the declared localized ring. (8)

No radical or reduced quotient is used in this conclusion. The
unimodularity is essential: a polynomial annihilating a coefficient
vector would not generally have to vanish as a scalar if that
vector's coefficient ideal were proper. Here (1) supplies precisely
the additional input needed for exact ideal membership.

The argument never divides by j, chooses a root of H, or discards
the intrinsic A4 allowance. The single accelerator (2) retains both
parts of the shared ODE, including its entire retained j=0 locus.
Adding it to a polynomial computation with the declared domain
inverse leaves the localized ideal and scheme unchanged. Adding it
without enforcing that domain would be a different claim.

## 5. New exact capture and prepared actual run

The [universal source](../computations/generalization_quintic_h2_unified_spectral_accelerator_2026_10_15.m2) verifies the degree-five determinant/Cayley–Hamilton identity and the idempotent/projected-residual identities. It computes no degree-six characteristic polynomial or degree-six Cayley–Hamilton product; that accepted theorem remains a separate premise.

The projected residual formulas have the correct extra boundary
term. For b_i=2q_(i-1)+v*q_i and Dpoly=(d-5)(d-6), the degree-six
residual is

    e6*(A6-eta*Id)q6vec=-2e6*E6vec-Dpoly*b6vec.

The degree-five residual is

    e5*(A5-eta*Id)q5vec=-2e5*E5vec+Dpoly*b5vec
                          +12w*E7*last_basis_vector.

The last term accounts precisely for q6 occurring in E5 but not
in the degree-five matrix. It vanishes in the ODE quotient because
E7=e5*q6. Thus the new universal exact checks agree with the
independent homogeneous proof in sections 3-4.

The prepared shared actual prospect uses eta in place of u. Its
coefficients are exactly twice (8) of the accepted ODE audit after
the invertible substitution u=(dv-eta)/2:

    2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                          +2(i-1-d)q_(i-1).

It adds the one polynomial (2), the accepted derived degree and
retained-j equations, and the previously necessary norm product.
It retains the original domain product and introduces no root,
norm-factor or j partition. This audit approves the mathematical
equivalence of that prepared presentation; it records no result
from its actual-parameter computation.

The remaining mathematical obligation is still actual-parameter
incidence and full conductor descent. This spectral identity alone
does not prove an empty locus, and agreement in finite characteristic
would not by itself prove characteristic-zero emptiness.


---

## 2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit

# Independent audit: twelve generators and equality on the candidate open

Date: 2026-10-15.

Status: **PASS for the new reduction from seventy-seven rank minors
to twelve generators. The two systems define equal ideal sheaves on
D(q5) union D(q6), including over nonreduced coefficient bases.** This
is an equality on the declared open, not equality of the global
unsaturated ideals and not a quintic exclusion.

The reviewed proposal is
[the twelve-generator support-system note](QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit).
The accepted h2 conductor factor, reciprocal coordinates, sextic
quotient, A4 bounds and closed mate lanes are premises. Their proofs
and computations were not replayed. This audit checks only the new
Hamiltonian column operation and determinantal-ideal reduction.

## 1. Scope, raw matrices and the twelve generators

In the actual application the quadratic has been normalized as

    H=t^2+v*s*t+w*s^2.

This is the monic finite chart, so H does not vanish at the intrinsic
A4 point s=0. The accepted previous closures justify this chart and
the candidate open below for surviving mate candidates. They must not
be silently assumed for arbitrary coefficient tuples.

Write a nonzero homogeneous sextic Q and its degree-six Hamiltonian
image R (which may be zero):

    Q=sum_(i=0)^6 q_i*s^(6-i)*t^i,
    R=D_H Q=sum_(i=0)^6 r_i*s^(6-i)*t^i,
    W=D_(sH)Q,
    D_K=K_t partial_s-K_s partial_t.

The full system consists of the twenty-one minors of [Q,jR] and the
fifty-six minors of [sQ,tQ,W], where coefficient vectors are understood.
For the universal matrix calculation, r0 through r6 can be independent
formal variables; dependence on the actual Hamiltonian action is only
needed for the column replacement in section 2 and the explicit
first-generator formula in section 5.

Put q_i=r_i=0 outside 0 through 6, and set

    C=[sQ,tQ,sR],
    row_i(C)=(q_i,q_(i-1),r_i),     0<=i<=7,
    M_ik=q_i*r_k-q_k*r_i,
    B_ikl=det(row_i(C),row_k(C),row_l(C)),

with the determinant oriented in the stated row order. Define

    I_full=I_3(C)+(j*M_ik : 0<=i<k<=6),

and the raw twelve-generator ideal

    I_small=(j*M56,
             B_056,B_156,B_256,B_356,B_456,
             B_067,B_167,B_267,B_367,B_467,B_567).       (1)

Each fixed pivot pair supplies six possible three-row determinants.
Pairs (5,6) and (6,7) share exactly the triple (5,6,7), so the displayed
list contains eleven distinct cubic minors and one first-matrix minor.
The candidate open is

    U=D(q5) union D(q6).                                (2)

It retains points where either coefficient vanishes. It must not be
replaced by D(q5*q6).

## Explicit universal determinant witnesses

For any indices, put d_ik=q_i*q_(k-1)−q_k*q_(i-1), retaining the displayed determinant row orientation. The full cubic minors satisfy

    B_ikl=−q_(i-1)M_kl+q_(k-1)M_il−q_(l-1)M_ik,
    B_ik7=−q6*M_ik.

For either pivot pair (a,b), the exact Schur determinant identity is

    d_ab*B_ikl=d_kl*B_iab−d_il*B_kab+d_ik*B_lab.

The retained-j absorption has direct polynomial witnesses

    d56*j*M_i6=(q5*q_i−q6*q_(i-1))*j*M56−j*q6*B_i56,
    q6*M_i5=q5*M_i6−q_i*M56,
    q5*M_i5=−B_i56−q_(i-1)*M56+q4*M_i6.

They hold before choosing an invertible pivot and retain nilpotents and j. In particular j times every cubic minor belongs to the first-minor ideal. These formulas supplement the localized-solve proof below; they do not cancel j or require both q5 and q6 nonzero.

## 2. The Hamiltonian column operation has the stated sign and scalar

The product rule gives D_(sH)=s D_H+H D_s and D_s=-partial_t.
Euler identities in degrees two and six give

    W=sR-H Q_t,
    sR=H_t(6Q-tQ_t)-sH_s Q_t=6H_tQ-2H Q_t.

Consequently

    W=(3/2)sR-3H_tQ
     =(3/2)sR-3v(sQ)-6(tQ).                            (3)

The scalar 3/2 is a unit in characteristic zero. This is an invertible
column operation. Thus the full cubic determinantal ideal for
[sQ,tQ,W] equals I_3(C); the equality is valid over any coefficient
algebra in which 2 and 3 are units. It is stronger than equality of
the associated geometric rank loci.

## 3. The two pivot opens cover U over arbitrary coefficient rings

The determinants in the first two columns of C at the two pivot pairs
are

    A=q5^2-q4*q6,       B=q6^2.                         (4)

They satisfy the polynomial identity

    q5^4=A*(q5^2+q4*q6)+q4^2*B.                        (5)

Since A,B belong to ideal(q5,q6), while (5) and q6^2=B put q5 and
q6 in radical(A,B), one has

    radical(A,B)=radical(q5,q6),
    D(A) union D(B)=U.                                 (6)

This is an equality of opens in the prime spectrum and remains true
for a nonreduced coefficient ring. It does not radicalize either of
the determinantal ideals under comparison.

On D(A), the first two columns at rows (5,6) give an invertible
two-by-two matrix. Solving those two rows expresses the third column
uniquely as alpha times the first plus beta times the second. Each
remaining row satisfies that same relation if and only if its cubic
minor with pivot rows (5,6) vanishes. The five minors B_i56 for i=0
through 4 and B567 supply precisely all six remaining rows, with a
harmless orientation sign for row 7.

On D(B), the same argument uses pivot rows (6,7) and the six minors
B_i67 for i=0 through 5. Hence the eleven selected minors generate
the same ideal sheaf as I_3(C) on U. This pivot elimination is valid
in the localized coefficient ring modulo the selected ideal; it
does not assume that ring is a field or reduced.

## 4. The single retained-j minor absorbs all twenty-one first minors

Work first on D(A), modulo I_small. Section 3 gives the column
identity

    sR=alpha*sQ+beta*tQ.                               (7)

For coefficient rows 0 through 6, this means

    r_i=alpha*q_i+beta*q_(i-1).

It follows exactly, in the localized quotient ring, that

    M_ik=beta*(q_i*q_(k-1)-q_k*q_(i-1)),
    M56=beta*A.                                       (8)

Because A is a unit, j*M56=0 forces j*beta=0. Every j*M_ik then
vanishes by (8). This inference keeps j as a variable and applies
equally when j is zero, nonzero or nilpotent.

On D(B), q6 is a unit because q6^2 is a unit. Section 3 again gives
(7), but row 7 is (0,q6,0), so it gives beta*q6=0. Thus beta=0 and
R=alpha*Q coefficientwise. Every M_ik already vanishes, independently
of j.

All generators of I_small belong to I_full. The arguments on the
cover (6) prove the opposite ideal inclusion locally. Therefore

    I_small O_U = I_full O_U.                          (9)

For the universal polynomial coefficient ring, or any of the
Noetherian parameter rings in the actual application, this is
equivalently the exact saturation equality

    I_small : (q5,q6)^infinity
       = I_full : (q5,q6)^infinity.                    (10)

No radicals of these ideals are taken. The reduction is thus valid
scheme-theoretically on U, including nonreduced coefficient bases.
This algebraic statement does not upgrade the previously established
field-valued root-support interpretation of the original rank
equations to a support or witness-lifting assertion over arbitrary
nonreduced bases.

## 5. The actual action agrees with the proposed compact generator

For the normalized H in section 1, direct differentiation gives

    r6=2q5-6v*q6,
    r5=4q4-4v*q5-12w*q6,

and therefore

    M56=2*(q5^2-v*q5*q6-2q4*q6+6w*q6^2).              (11)

The scalar two is a unit. Removing it yields exactly the proposed
compact first generator. If one specializes q6=0 and q5 is nonzero,
then M56=2q5^2, so j*M56=0 forces j=0 on that locally closed
stratum. This does not justify replacing j*M56 by j on the entire
q5-nonzero chart. The ideal proof in section 4 avoids that
specialization and therefore retains nilpotent parameters correctly.

The explicit formulas in (11) use the monic t^2 coefficient of H.
With a general unnormalized quadratic, that coefficient must be
carried through the formula. The abstract matrix reduction in
sections 3-4 does not require the Hamiltonian form of R at all, but
the actual application and its candidate-open justification retain
their declared normalization and previous geometric hypotheses.

## 6. Essential scope and computation boundary

The open restriction is necessary. For

    Q=s^6,       H=t^2,       R=12s^5t,       j=1,

one has sR=12tQ, so the full cubic rank is at most two. All eleven
selected minors and j*M56 vanish because their pivot rows are zero.
Yet M01=12 is nonzero, so [Q,jR] has rank two. This point has
q5=q6=0 and lies outside U. Thus neither a global unsaturated ideal
equality nor an unconditional twelve-equation support test follows.

For the actual rational coefficient capture, preserve delta nonzero,
the finite-cover factors Delta and K nonzero, the nonzero cofactor
determinant, all recorded denominator/content restrictions, and the
actual projection hypotheses. Replacing j by a recorded numerator
or removing parameter factors is valid only where the corresponding
comparison factors are units. The abstract reduction (9) introduces
no additional discriminant inversion. Its monic actual chart and
candidate open come from the accepted prior reductions, not from
discarding a repeated-root or j=0 stratum in this proof.

For the final Hamiltonian coefficient extraction, the formal q,r,j,v,w parameters belong to the coefficient ring and s,t to the subsequent polynomial ring. The written proof above establishes the ideal-sheaf reduction independently. Neither these universal identities nor the actual-coefficient size probe supply an elimination or saturated-unit-ideal certificate.

The accepted norm product may be appended to both equivalent ideals
without changing (9), with its original domain retained. Nothing in
this audit proves the resulting actual-parameter locus empty,
establishes full inverse support from the rank conditions, or proves
nonlinear conductor descent.


---

The direct universal support is [the original twelve-generator syzygy source](../computations/generalization_quintic_h2_twelve_generator_syzygies_2026_10_15.m2). It verifies formal coefficient identities, not the actual conductor coefficient map. The accepted necessary norm product is N12*N18; retain it as one equation on its declared domain, without splitting its factors.

## 2026-10-15-generalization-quintic-h2-eleven-generator-unit-independent-audit

# Independent audit: the remaining-mate Delta1 open and eleven generators

Date: 2026-10-15.

Status: **PASS for the new all-remaining-mate condition Delta1 nonzero,
and for exact redundancy of the twelfth generator after the verified
actual coefficient binding and the declared localization.** The
previous h2 factor, reciprocal coordinates, sextic quotient, A4 fiber
criterion, accepted mate closures and twelve-generator reduction are
premises; none was replayed.

This note reviews only the new common unit and its algebraic effect.
It does not claim the remaining incidence is empty, remove a factor
of j, or establish nonlinear conductor descent.

## 1. Delta1 is nonzero on every remaining mate candidate

Use the accepted nonendpoint quintic A4 family, with delta nonzero,
actual j=Jbar, and full inverse support SUP as a necessary condition
for a mate. If j is nonzero, the accepted complete A4 target-fiber
criterion states that Delta1=0 gives an actual off-c point. Therefore
SUP forces Delta1 nonzero in this stratum.

If j=0, the accepted literal expression specializes to

    Delta1=G*(G+3delta^2)*(G+delta^2+2B).               (1)

The accepted G=j=0 mate closure removes the first zero factor. The
accepted entire-line mate closure removes G=-3delta^2,j=0, the second
zero factor. Finally, on G nonzero the accepted A4 target-fiber
criterion makes SUP imply

    L=G+delta^2+2B nonzero.

Indeed L=0 gives D0=delta^2/2+B=-G/2 nonzero and G=-2D0, exactly
the criterion for an off-c point. Thus every factor in (1) is nonzero
on a remaining j=0 mate candidate. This proves

    Delta1 nonzero on all remaining mate candidates,   (2)

for both values of j. This is a new common necessary open obtained
from the accepted closures. It is not asserted for every projection,
every support-incidence point before those closures, or an arbitrary
formal parameter tuple.

The accepted h2 infinity equations imply that H containing A4 forces
G=j=0. Hence H avoids A4 on the same surviving mate locus and may be
normalized as H=t^2+vst+ws^2. This monic normalization is an actual
scope condition, rather than an inversion justified for arbitrary H.

## 2. Actual and captured leading coefficients

In reciprocal source coordinates x=t/s and p=s/t, A4 is (s:t)=(0:1).
For the actual monic h2 factorization Fsrc=H Qactual, one has

    H(0,1)=1,
    Qactual(0,1)=Fsrc(0,1)=Fdet(0,1)=-3j Delta1.        (3)

Thus the actual coefficient of t^6 is -3j Delta1. On the open (2),
its ratio to j is a unit; this statement is the exact identity (3),
not a cancellation by j at field-valued points.

The previously captured Q differs from Qactual by the recorded
common scalar. The finite inverse-map capture clears commonDen and
removes coefficient content delta^4, so

    Qcaptured=(commonDen/delta^4)*Qactual,
    q6=-3*(commonDen/delta^4)*Delta1*j.                (4)

The commonDen is a unit on the original inverse-map denominator
open, and delta is a unit. After explicitly localizing at Delta1,
the entire scalar multiplying j in (4) is therefore a unit. Write

    q6=u*j,       u a unit in the localized ring.      (5)

In polynomial generator captures the retained scalar is often the
saved numerator jNum of actual j. Its denominator is an original
inverse-map unit, so (5) also says q6=uNum*jNum with uNum a unit
after the same localization. The numerator Delta1num represents
Delta1 up to its recorded denominator unit. Inverting Delta1num is
therefore exactly the new Delta1 open on that chart.

The exact unit-binding calculation gives the literal polynomial identity

    delta^4*q6=-3*jNum*Delta1num.                       (5a)

Its declared-unit stripping records exponents zero for q6, delta
exponent one for jNum and delta exponent three for Delta1num, with
no discriminant or K exponents. The remaining ratio is the nonzero
rational -3. Thus, writing Jprim=jNum/delta and
Tprim=Delta1num/delta^3, it also records the polynomial factorization
q6=-3*Jprim*Tprim. Both divisions here are exact polynomial divisions
recorded by the new capture; their factors are units on the original
delta-nonzero chart.

I read the new C source, its exit-zero record, stdout, ratio and
exponent files. It parses the three saved accepted coefficient
artifacts, strips only delta, the discriminant and K, checks the
remaining ratio is a nonzero rational, and then checks the literal
polynomial equality after multiplying negative declared-unit powers
to the other side. Current source and all three input digests agree
with its record. This is a new binding identity between saved
artifacts, not a reconstruction or rerun of any accepted verifier.

Merely knowing that Delta1 is nonzero at candidate field-valued
points would not justify cancelling it in the global polynomial
ring. The operation here is the declared localization on a necessary
candidate open, followed by an exact scalar identity in that ring.

## 3. The retained-j minor is already one of the eleven cubic minors

Retain the coefficient conventions of the accepted twelve-generator
reduction:

    C=[sQ,tQ,sR],       row_i=(q_i,q_(i-1),r_i),
    M_ik=q_i*r_k-q_k*r_i,
    B_ikl=det(rows i,k,l of C),

with q_i=r_i=0 outside 0 through 6. Expanding the row-seven determinant
gives the signed identity

    B_i67=-q6*M_i6,       0<=i<=5.

In particular

    B567=-q6*M56=-u*j*M56.                             (6)

B567 is among the eleven selected cubic minors. Since u is a unit,

    j*M56=-u^(-1)*B567.                               (7)

Let I11 be generated by B_i56 for i=0 through 4 and B_i67 for i=0
through 5. Equation (7) proves the exact ideal equality

    (I11,j*M56)=I11                                   (8)

in the actual localized parameter ring. It uses no division by j
and remains valid if j is zero, a zero divisor or nilpotent. It
needs neither a reduced ring nor a nonzerodivisor assumption on j.
The same proof applies with jNum in place of j.

Combined with the accepted twelve-generator equality on
U=D(q5) union D(q6), (8) identifies the eleven-generator ideal with
the original full rank system on U in this newly localized domain.
The direct redundancy (8) itself does not need U; the equivalence
to all original rank minors still retains U.

## 4. Dividing six cubic generators by Delta1num retains j

Write the more explicit localized identity as

    q6=vUnit*j*Delta1num,

where vUnit is a unit after the original denominator and delta
localizations. The six row-seven minors then satisfy

    B_i67=Delta1num*(-vUnit*j*M_i6).                   (9)

On the new Delta1num-nonzero chart, replacing these six generators
by their quotients by Delta1num preserves the ideal exactly: it
multiplies each generator by a unit. The five B_i56 remain unchanged.
The quotients retain j. In particular the 567 quotient is
-vUnit*j*M56 and still supplies the removed first-matrix minor.

If a polynomial quotient rather than a localized fraction is saved,
its literal divisibility must be checked by the new coefficient
capture. Localized factorization alone does not establish global
polynomial divisibility. Neither formulation permits division by j
or replacement of j*M56 by M56.

In particular, the full Delta1num has a delta^3 factor, whereas q6
has no delta factor. One should not assume global polynomial
divisibility of q6 by the unstripped Delta1num. Equation (5a) gives
a simpler polynomial presentation without that assumption:

    B_i67=(3*delta^(-4)*Delta1num)*(jNum*M_i6).

The parenthesized scalar is a unit on the declared domain. Hence a
polynomial eleven-generator ideal defining the same localized ideal
is

    (B_i56 : 0<=i<=4) + (jNum*M_i6 : 0<=i<=5).         (10)

Its last generator includes jNum*M56. Thus the previously separate
twelfth generator is supplied by the normalized row-seven group,
and the retained-j condition has not been cancelled. Replacing
jNum by Jprim in (10) is another multiplication of six generators
by the original unit delta^(-1).

All original finite inverse-map conditions remain: nonzero delta,
nonzero Delta*K, nonzero cofactor determinant, recorded content and
denominator units, actual projection hypotheses, and U for the full
rank-system comparison. The new Delta1 open is justified by (2).
The proof does not turn the finite inverse-map chart into coverage
of its repeated-root boundary. With raw actual coefficients, (3)
has no finite inverse-map denominator; the captured unit (4) is only
claimed on its original denominator open.

The new result is an eleven-generator presentation on this necessary
remaining-mate open. It supplies no incidence-emptiness certificate
and no implication from the rank equations to full conductor descent.


---

<a id="2026-10-15-generalization-quintic-h2-horner-input"></a>

## Exact generator representation

The [actual generator source](../computations/generalization_quintic_h2_unified_minors_flint_2026_10_15.c) constructs the twelve polynomials from the retained actual sextic coefficients and J numerator, divides only powers of the declared units, and checks the literal product identity after each division. Expanding a polynomial or writing it in Horner form preserves this incidence; the serialized forms need not both be retained. No serialization or import check establishes emptiness or conductor descent.

The actual/captured coefficient binding is implemented in [the exact A4 unit-binding source](../computations/generalization_quintic_h2_a4_unit_binding_2026_10_15.c); its scalar and localization scope are the ones in the eleven-generator proof. A representation change does not replace this actual-map identification.
