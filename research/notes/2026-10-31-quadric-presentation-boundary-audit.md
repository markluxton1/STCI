# Independent audit: actual quadric columns and normal-action defects

Date: 2026-10-31. Reviewer: `matrix_boundary_strategy_review`, independent
of both producers. No nested delegation. Scope: §§1–4 of
[the source note](2026-10-31-quadric-presentation-boundary.md), including
the actual ideal embedding, all-order defect formulas, operation invariant,
rank-zero challenge, literature hypotheses and stopping assessment.

**Outcome: scoped PASS.** No material mathematical correction was required
in the reviewed draft. The rank-zero reset is an independent challenge
that materially limits the operation invariant; it is retained in §3,
rather than dismissed as a hypothetical escape. These are reviewed
provisional calculations, with no canonical promotion, new residual-degree
bound, successful equation pair or unrestricted exclusion.

Final reviewed source SHA-256:
`3bdddebaa4898335325485ba327ed34e5b0d42c349ba78ac499a2b6b9a4e8d13`.
The source's pending-review heading was replaced by its reviewed
provisional status and the link to this audit; the mathematical body
was unchanged. This hash identifies those final reviewed source bytes.

## 1. Actual ideal and all-order restriction

The exact hypotheses are the fixed smooth quartic C of class (1,3) on
the smooth quadric Q over an algebraically closed characteristic-zero
field, and a proper homogeneous CI Y with reduced support exactly C.
The integer N is the least exponent with q^N in the actual ideal (F,G).

The row (-G,F) identifies coker Φ with (F,G)/(q^N), using regularity
of F,G to identify its kernel. Thus the presentation retains an actual
ideal in O_(NQ), not just an abstract MCM module. The injective split
resolution proves the ACM and local MCM assertions. Off C its ideal is
the whole structure sheaf, proving generic rank one.

Neither F nor G can vanish identically on Q: otherwise the other
restriction would be a nonzero balanced effective divisor supported only
on the irreducible unbalanced curve C. Both restrictions therefore have
common divisor exactly rC, r≥1. After its removal, f,g are nonzero with
no common divisor. Their simultaneous zeros form a finite local CI T,
possibly empty, supported on C. The intersection product independently
gives

    (a-r)(b-3r)+(a-3r)(b-r)
      =2ab-4r(a+b)+6r².

This allows zero entries in a local trivialization and constant residual
sections; no positivity of this length is silently imposed. The r=1
arithmetic is already present in §4 of the linked
[blowup residual audit](2026-10-28-blowup-residual-audit.md).

The saturated image line of (f,g) has determinant
L=O_Q(-a-b+r,-a-b+3r), with quotient I_T O_Q(-r,-3r).
The second reduced column factors through L off T, and its scalar extends
over T by regularity on the smooth surface. This proves the global
factorization (2), with the stated twist of h.

Minimality of N prevents both A,B from being divisible by q. Since f
and g are both nonzero on the integral Q, either reduced entry of the
second column vanishing identically would force h=0 and hence both
entries to vanish. Thus h is nonzero. Removing the common divisor eC
from the row (c^r,h) leaves a row without a common divisor. Its Koszul
syzygy remains a line bundle even at its finite base scheme. The kernel
is consequently O_Q(-2N-k,-2N-3k), k=r-e, as stated.

Tensoring the presentation by O_Q gives this kernel as
Tor_1(M,O_Q)=Ann_M(q)(-2,-2). This checks the (2,2) shift in (3).
In the actual ideal embedding, the annihilator is a line subideal of
O_Q(2-2N,2-2N), equal to it away from C. Its effective divisor is
therefore precisely kC, not a divisor plus an undetected punctual ideal.
Multiplication by q^(N-1) gives c^r I_T in the same ambient line,
proving (4) and the quotient (5) as actual inclusions.

If k=0, that line subideal contains q^(N-1)O_(NQ), so q^(N-1) belongs
to the ideal sheaf of Y. The homogeneous CI ideal is saturated: its
coordinate ring has depth two. Therefore q^(N-1) belongs to (F,G),
contradicting minimality. This checks k≥1 without assuming generic
freeness along C. The case N=1 is not an exception to the argument.

The exact sequence for O_Q/(c^e I_T) follows by quotienting the inclusion
c^e I_T⊂(c^e)⊂O_Q. It preserves the finite subsheaf O_T(-eC)
even when e>0, and gives O_T when e=0. The image filtration
im Φbar⊂L⊂H|_Q proves (6), so no torsionfree-reduction assumption enters.

Geometrically, (5) measures the failure of the top q-multiple of the
ideal to generate its q-annihilator. It can be generically nonzero
along C and also have a finite contribution. It does not identify
another curve downstairs or provide a positive residual-degree estimate.

## 2. Invariant and its explicit failure across a reset

A saturated rank-one subsheaf of a split bundle on the smooth Q has
torsionfree quotient; the depth lemma makes the subsheaf reflexive,
hence invertible. Its inclusion can still vanish in a finite fiber
scheme. A distinguished column with reduced zero support C gives a
nonzero section of L_P(a,a) with Cartier divisor νC. This independently
checks both coordinates of (7), and explains why the ruling difference
alone is weaker than the full requirement.

For the homogeneous rational target operation, h and v are polynomial
data and v is primitive at the prime q. If UP is polynomial, the
q-valuation-zero component of v and q∤h imply q^j divides every entry
of wP. Conversely that divisibility suffices. Since wU=w, both nonzero
generic rank-one reductions lie in the one-dimensional kernel of wbar.
Their generic image lines agree, hence their saturations agree in the
same target. This proves the invariant under its explicitly stated
stratum and bundle hypotheses. Invertible right operations preserve
the image, and target bundle automorphisms preserve its isomorphism class.

The independent challenge multiplies the displayed matrices directly:
P0 J^(-1)=qI-vw and (vw)^2=0, giving qI after the first pole operation.
The intermediate reduction is zero. Multiplication by q and the second
pole operation yield P'=q²I+v'w', det P'=q⁴, of homogeneous degree four.
Its reduced image saturates to O_Q(-2,0), because
v'=v0²(u0²,u1²) and u0,u1 have no common zero. Thus the difference
changes from zero to two. The stronger no-reset conclusion is false.

This is not a C-supported column: L_P'(4,4)=(2,4) is not any multiple
of (1,3). Furthermore the reduced matrix has the common factor v0⁴,
so its rank-zero locus contains the entire ruling v0=0. At a point of
that ruling all entries lie in the maximal ideal, and the cokernel
needs two generators, excluding freeness of rank one there. The ruling
is not contained in C. The construction gains image-class flexibility
while losing the actual divisor and support conditions; neither side
of that conclusion may be omitted.

## 3. Direct literature checks and disposition

The following PDFs were checked directly for the stated uses:

- [Hartshorne, Appendix, pp. 430–431](https://seminariomatematico.polito.it/rendiconti/64-4/419.pdf): the ACM/MCM and presentation dictionary supports the terminology, without supplying an exclusion or a classification here.
- [Kerner–Vinnikov, global paper](https://arxiv.org/pdf/0906.3012): its setup uses linear matrix entries. The reduced-kernel descent in §4.2, Definition–Proposition 4.4, requires generic maximal generation; arbitrary corank-one matrices on q^N do not acquire that hypothesis automatically.
- [Kerner–Vinnikov, local paper](https://arxiv.org/pdf/1009.2517): Corollary 3.3 requires maximal generation on the smooth reduced locus to factor the reduced equation. Theorem 3.4 requires relatively prime factors. Repeated q does not meet the latter hypothesis.
- [Ballico et al.](https://arxiv.org/pdf/1604.00866): the stated low-rank classification concerns the double plane. It does not classify the present multiple-quadric presentations.
- [Cohn, §7, p. 26](https://www.numdam.org/item/PMIHES_1966__30__5_0.pdf): the explicit determinant-one matrix over k[x,y] is not generated by elementary matrices. This is a warning about assuming generation, not a result about S[q^(-1)] or the operation class studied here.

The prime-boundary valuation argument generalizes as stated; the
divisor-class argument requires the smooth boundary and the specified
irreducible column support. Neither generalization gives exhaustiveness
of the chosen operations.

The stopping assessment passes with its explicit limitation: no larger-N
or seed classification is selected because no new residual comparison
or operation controlling the complete column divisor and boundary support
has been supplied. Asking merely for a successful determinant-q^N matrix
and C column restates the original problem; it is not a new research datum.
A special successful construction could settle existence, while these
special-operation exclusions need an additional exhaustive reduction to
settle nonexistence. Both possibilities remain live.

No computation campaign, canonical metadata change, inherited proof
rerun or universal obstruction is claimed by this audit.

## 4. Final strategy-assessment disposition

The reviewer also read the complete new
[strategy assessment §19](2026-10-31-unrestricted-strategy-assessment.md#19-actual-matrix-columns-normal-action-defects-and-the-limit-of-operation-invariants).
Its report of the present formulas, the invariant's nonzero-rank stratum,
the explicit reset, the failed full column class and the unwanted
nonfree ruling agrees with the reviewed source. Its decision to select
no new experiment is supported as a bounded allocation decision, without
a claim that all mathematical uses of the presentation are exhausted.

The requested next input is an operation or comparison with specified
additional geometric control; the assessment correctly rejects merely
asking again for the final successful matrix. It also preserves the
asymmetry that a successful special construction can settle existence,
whereas a special-family exclusion needs an exhaustive reduction to
settle nonexistence. The discussion of sextic corrections, Picard
lifting, punctual extensions and ribbon absorption is inherited context;
this review checks that §19 does not turn those source results into an
unrestricted conclusion and does not rerun their separate proofs.

**Final recommendation disposition: PASS at that scope.** Both bounded
assignments close, no larger-N or neighboring-seed campaign is selected,
and the unrestricted characteristic-zero question remains open.
