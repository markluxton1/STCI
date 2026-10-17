# Independent audit: twelve generators and equality on the candidate open

Date: 2026-10-15.

Status: **PASS for the new reduction from seventy-seven rank minors
to twelve generators. The two systems define equal ideal sheaves on
D(q5) union D(q6), including over nonreduced coefficient bases.** This
is an equality on the declared open, not equality of the global
unsaturated ideals and not a quintic exclusion.

The reviewed proposal is
[the twelve-generator support-system note](2026-10-15-generalization-quintic-h2-twelve-generator-support-system.md).
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

The first universal identity execution was read and preserves a
failure at the final Hamiltonian coefficient-extraction assertion,
after successful checks of the cubic expansions, both pivot
identities and retained-j absorption identities. The repaired
[attempt-02 source and execution](../validation/2026-10-15-quintic-h2-twelve-generator-reduction/attempt-02/execution-record.json)
were also read. The repair places the formal q,r,j,v,w parameters in
the coefficient ring and s,t in the subsequent polynomial ring, so
the final coefficient extraction uses the intended variable split.
Its exit code is zero, stderr is empty, and its stdout records all
four groups of exact identity checks passing. Attempt-01 remains a
failed run; attempt-02 supplies the passing arithmetic evidence.
The written proof above establishes the ideal-sheaf reduction
independently. Neither that identity check nor the actual-coefficient
size probe is an elimination or saturated-unit-ideal certificate.

The accepted norm product may be appended to both equivalent ideals
without changing (9), with its original domain retained. Nothing in
this audit proves the resulting actual-parameter locus empty,
establishes full inverse support from the rank conditions, or proves
nonlinear conductor descent.
