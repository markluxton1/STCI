# Independent audit: one global monic h2 ODE incidence

Date: 2026-10-16.

Status: **PASS for the new global monic cover, original-parameter
coefficient assembly, and transfer of the accepted ODE/spectral
algebra to the domain delta*E*Delta1 nonzero.** The seventeen
equations in nine variables retain the finite inverse-map boundary.
This is a necessary incidence for every remaining actual h2 mate
candidate, not an emptiness or mate-existence theorem.

The reviewed proposal is
[the global monic incidence note](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md).
Accepted conormal forms, the actual octic, the global h2 conductor
factor, previous mate closures, the Delta1 open, and ODE/spectral
proofs are premises. No accepted proof or verifier was replayed.
This audit uses written coefficient calculations and read-only
source/artifact/hash inspection. No CAS was run during completion
of this audit, and no model assembly or elimination was repeated.

## 1. Monic coverage and exact homogeneous gcd degree

For any remaining actual h2 mate candidate, a common factor at source
infinity would force G=j=0 by the accepted leading-coefficient
equations. The accepted mate closure excludes that lane. Thus the
complete degree-two homogeneous gcd has nonzero t^2 coefficient,
and its unique monic representative is

    H(x)=x^2+v*x+w,       x=r/delta=t/s.

This monic chart is therefore global for the remaining h2 mate
candidates. It imposes no distinct-root hypothesis. It also does
not normalize delta to one.

Write the literal normalized cubics as

    P=G*x^3+P2*x^2+P1*x-2a,
    Jc=(G+2j)*x^3+J2*x^2+J1*x-a-B,

where

    P2=6B+delta^2-3delta,       P1=3a-3B+2delta,
    J2=6B+3G+5delta^2-3delta,   J1=3a+3B+delta-delta^2.

Set A=G, Bc=P2-vG, C=G+2j, Dc=J2-v(G+2j). The leading two
coefficients of (Ax+Bc)H and (Cx+Dc)H match the cubics identically.
Their remaining coefficients match precisely when

    -2a-w*Bc=0,       P1-v*Bc-w*A=0,
    -a-B-w*Dc=0,      J1-v*Dc-w*C=0.                  (1)

These are exactly the four saved cover equations, with no coefficient
system inverted. Direct expansion gives

    E=A*Dc-Bc*C
     =G*(3G+4delta^2)-2j*(6B+delta^2-3delta).          (2)

The terms involving v cancel. The unit E is the determinant of the
two homogeneous linear cofactors A*t+Bc*s and C*t+Dc*s. At field
points they are independent exactly when they are coprime, so (1)
and E nonzero give complete homogeneous gcd degree two. This
includes affine degree drops of either cubic. A zero cubic or a
proportional cofactor pair instead has E=0 and is correctly outside
the exact-h2 domain.

## 2. Fixed-degree octic reversal and monic division

For the accepted actual Fdet(p,1)=sum_(i=0)^8 f_i*p^i, reciprocal
source coordinates give Fsrc(1,x)=sum f_i*x^(8-i). Put q7=q8=0
and define downward

    q_i=f_(6-i)-v*q_(i+1)-w*q_(i+2),    i=6,...,0.

For the coefficient of x^(i+2) in H*Q, this is exactly
q_i+v*q_(i+1)+w*q_(i+2)=f_(6-i). Therefore all coefficients
of degree at least two match, and the remaining two coefficients
are exactly

    r0=f8-w*q0,
    r1=f7-v*q0-w*q1,
    Fsrc=H*Q+r1*x+r0.                                (3)

The two explicit equations r0=r1=0 are retained. The accepted
geometric factor theorem supplies them for every actual h2
projection; this assembly does not promote that theorem to an
unproved divisibility assertion over an arbitrary nonreduced
conormal-cover base. After the equations are imposed, (3) is an
exact ring identity on the incidence.

Monic division introduces no parameter denominator. Fixed degree
eight reversal and degree six quotient retain all coefficient drops
and the source point at infinity. In particular q6=f0 and
q5=f1-v*q6 have the intended A4 interpretation.

## 3. The new global domain does not invert Delta or K

The domain is exactly

    delta*E*Delta1 nonzero,
    Delta1=G(G+3delta^2)(G+delta^2+2B)
      +j[(delta^2-5B)G-3B(delta^2+3B)]-B*j^2.         (4)

Delta1 is necessary for all remaining mate candidates by the accepted
closures and A4 support argument. Delta=v^2-4w and
K=v^2+6vw+6w^2+2w are not factors of the declared unit product.
Thus the repeated finite-root boundary and the failed rational
inverse-map boundary remain represented by the original equations.
An accepted inconsistency on part of that boundary may be used as
a theorem, but no such locus is silently cancelled from this model.

For the unscaled actual quotient, the accepted A4 coefficients give

    q6=-3j*Delta1,
    q5=-2(G+3delta^2)*Delta1 modulo j.                (5)

There is no captured inverse-map scalar here. The accepted automatic
open proof now applies with kappa=1: the explicit Delta1-square
membership, or its equivalent quotient-ring argument, gives
(q5,q6)=1 after (4). This is an exact ideal equality and includes
nonreduced bases. It needs neither Delta nor K to be a unit.

The previous ODE and spectral proofs use monic H, (5), the Delta1
unit, coefficient unimodularity and field scalars 2,3. They therefore
apply unchanged to this original-parameter ring before any rational
inverse of the four cover equations. Their earlier actual use on a
smaller inverse-map chart does not limit this algebraic transfer.

## 4. The seventeen-equation system and its precise meaning

Using eta=dv-2u, the eight ODE coefficients are exactly

    2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                         +2(i-1-d)q_(i-1),
    i=0,...,7.                                        (6)

These are twice the coefficients of H*q'-(dx+u)q. The change from
u to eta is invertible. The accepted globally unique ODE-witness
argument applies by (5), so (6) is the same shared rank/support
incidence on this domain, including its j=0 allowance.

There are four equations (1), two equations (3) and eight equations
(6), making fourteen. The three accepted derived equations

    (d-5)(d-6),       j(d-6),
    (d-5)P6(eta)+(6-d)P5(eta)

bring the saved presentation to seventeen equations in the nine
variables delta,a,B,G,j,v,w,d,eta. They belong to the same localized
ODE ideal, so appending them changes no scheme on (4). The temporary
variables p and x used in assembly are not additional model variables.

On actual admissible h2 projections, this incidence expresses the
accepted restricted-conductor support obligation. Every remaining
actual h2 mate candidate lies in it. The model does not impose center
avoidance or all original fiber conditions, and it does not establish
full inverse support or nonlinear conductor descent. An algebraic
survivor is therefore not automatically a projection or a mate.

## 5. Source, failure lineage and completed-output bindings

I read the current and frozen
[assembly source](../computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2),
the attempt-02 record and streams, the
[completion source](../computations/generalization_quintic_h2_global_monic_ode_completion_2026_10_15.py),
and the
[attempt-04 completion record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-04-completion/execution-record.json).
The assembly source uses the literal accepted octic, the reversed
coefficients and recurrence above, the four cover equations, (2),
the eight ODE equations, the three accelerators and precisely (4).
It writes all groups and seven q_i, asserts (2) and (3), then writes
the degree list before the final informational print.

The attempt-02 process exits one: its error is at that final
equation-count print, after stdout records the quotient/remainder
and cofactor assertions passing and after all data files were
written. This remains a failed process and is not relabelled a
fully passing CAS run. Its complete outputs are the bound inputs
to the separate Python completion; the earlier protected-name and
path/shape failures remain preserved as separate attempts.

The completion strips only boundary whitespace when reading the
expanded matrix entries, checks the exact four-group concatenation
4+2+8+3=17, checks a seven-entry Q vector, and copies the saved
model artifacts. It does not reread the primitive octic, reconstruct
the model, or run any CAS. Its record reports exit zero and empty
stderr.

On October 16 I independently checked, read-only: both current and
frozen assembly source hashes; the current completion-source hash;
the assembly's primitive-input hash; all seventeen completion-input
hashes; byte equality of all four copied model artifacts; exact
group/whole-vector equality; and all seven individual q_i files
against the completed Q vector. Every check passed. The completion
stderr is empty. This verifies current artifact bindings without
rerunning the mathematical assembly.

The new currently runnable
[load-only input](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
reads the completed seventeen-equation row and domain polynomial
over QQ in the stated nine-variable order. It asserts the ring,
matrix shape and nonzero domain polynomial, and retains the objects
h2GlobalRing, h2GlobalEquations, h2GlobalIdeal and
h2GlobalDomainUnit. It constructs no coefficient map and calls no
Groebner basis or saturation operation. The domain polynomial is
loaded as data for a future localization; the load-only script does
not itself localize or prove the domain nonempty.

I also read the
[attempt-05 load-only record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-05-load-only/execution-record.json),
its input-binding metadata and streams. The record has exit zero
and empty stderr. A read-only check confirmed the current and frozen
input-source hashes, both current completed-data hashes, and both
output-stream hashes against that record. This successful load is
distinct from attempt-02's failed final print and attempt-04's
successful non-CAS completion. No CAS was invoked by this audit.

The one global future target is therefore the saved seventeen-equation
incidence localized at (4). No Gröbner basis, saturation, resultant
or emptiness computation for this global model is certified here.
A result restricted to Delta*K nonzero cannot close this larger
incidence. The unrestricted quintic and STCI questions remain outside
the conclusion of this audit.
