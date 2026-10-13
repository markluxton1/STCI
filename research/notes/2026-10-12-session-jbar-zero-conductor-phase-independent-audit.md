# Independent audit: Jbar-zero coprime conductor phase bound

Date: 2026-10-12. Auditor:
`oct11_endpoint_a_nonzero_support/a_nonzero_three_common_roots`.

Status: **PASS, independent mathematical audit of the all-mate exclusion
under the stated geometric hypotheses.** The argument uses an actual
normalization fiber, finite module generation, the entire conductor divisor,
full Artinian membership and purity. It does not infer rank from average
degrees or bound the phases of an algebra that remains split.

The audited owner is
[Jbar-zero coprime conductor phase bound](2026-10-12-session-jbar-zero-coprime-conductor-phase-bound.md),
as read with SHA-256
`5749a82f42bce56842c826fc18b8972f85bfc6f4e21276754f7c80a066e3f23a`.
This audit binds its mathematical sections 1--6. At that version its final
section promises forthcoming verifier bindings; their later addition is
not needed as a premise of this proof. Owner, old notes, canonical records,
sealed files and Git were left unchanged by the auditor.

## 1. Precise scope and retained exceptional cases

Work over an algebraically closed field of characteristic zero in the
accepted nonendpoint genus-one quintic A4 pair. Retain arbitrary
`delta != 0,a,b,g,d`, actual center avoidance and finite birational
normalization `nu:S -> X`. The lifted c maps isomorphically to fixed C0.
Write

\[
\bar J=d-2g+2b-a=0,\qquad E=g-3b+2a.
\]

Assume the corrected degree-three homogeneous conormal forms Ph,Jh are
coprime, including their roots at infinity. Every supposed mate pulls
back to a scalar Q^k, where Q is an actual section of 4H with divisor
5c, and forces the full reduced inverse support to be c.

The two cubic leading coefficients both equal E on this hypersurface.
Thus E=0 is incompatible with homogeneous coprimality. The case
E=-3delta^2 is exactly the previously audited entire-line ramification
locus, since its second equation equals twice the first on Jbar=0.
Its separate characteristic-zero derivation obstruction excludes every
positive power. The rest of this proof assumes
`E(E+3delta^2) != 0`. It does not claim the following length-two fiber
calculation on the removed ramified-line locus.

Under a hypothetical mate, coprimality and the actual opposite target
frame give cotangent surjectivity at every finite point of c, including
r=0. Full support leaves one normalization point over each such image.
The finite local Nakayama lemma therefore makes nu a local isomorphism
there. The conductor divisor misses all finite points of c.

## 2. The actual A4 fiber and finite generation

Use the accepted A4 source chart

\[
B=k[\alpha,\beta,\chi]/
  (\beta(\alpha^2-\chi)-\alpha\chi^2),\quad
h=\beta+\chi,\quad d_Z=\alpha\beta-\chi^2,\quad
e_Z=\beta^2-\alpha\beta\chi+\chi^3.
\]

The actual target maximal ideal pulls back, after invertible row
operations and the unit X0, to

\[
f_1=\delta\alpha+(b-a)h,\quad
f_2=Eh+3\delta^2\chi-\delta^3d_Z,\quad
f_3=\delta^4e_Z-2\delta^3d_Z.
\]

These are exact section identities. The first two eliminate alpha,chi
formally, with nonzero linear determinant `3 delta^3`. Their leading
solution is

\[
\alpha=-(b-a)h/\delta+O(h^2),\quad
\chi=-Eh/(3\delta^2)+O(h^2),\quad
\beta=(1+E/(3\delta^2))h+O(h^2).
\]

The source equation then has nonzero leading coefficient
`E(E+3delta^2)/(9delta^4)` on h^2. It therefore generates `(h^2)`
in the one-variable completed ring. The third target generator has
order at least two and cannot remove its surviving first-order h.
The completed fiber is exactly `k[[h]]/(h^2)`, of length two.
Completion preserves this finite length.

Full inverse support implies that p is the only point above y=nu(p).
Consequently the normalization algebra at y is local, finite over
O_X,y, and is the actual source local ring used in that calculation.
Its fiber dimension two makes it a two-generated O_X,y-module by
Nakayama. The two generators extend to a surjection from O_U^2 on
some open neighborhood U of y. This is local module generation,
not flatness or a claim that all conductor algebras have length two.

Each conductor prime D_i meets c. It is not c, since the conductor
misses finite c. The nonzero restricted section Q|D_i has positive
line-bundle degree `4H.D_i`, so it has a zero on this complete integral
curve. Every such zero lies on c, and finite c was excluded. Hence
D_i contains p; its image curve contains y, and its generic point
belongs to U. The two-generator bound therefore applies at every
generic conductor point.

At such a point eta, the finite normalization fiber is an Artinian
k(eta)-algebra whose residue-field degrees sum to at most its dimension,
and that dimension is at most two. This bounds the sum of the reduced
field degrees. It does **not** bound the length of B/I: arbitrary
higher generic conductor exponents remain possible.

## 3. Complete low-degree prime classification

The normal complement S minus ell is A2 with r,t, where
`T=t+r^2` and `v=t^2-r^3`. The complete pole-order-five space is
`span(1,r,t,r^2,rt,v)`, by the already proved valuation filtration.
For a prime D_i other than ell, its affine generator f is irreducible,
and its only possible additional divisor is the boundary ell.
Thus `div(f)=D_i-n ell`, where intersection with H identifies
`n=H.D_i` as its exact pole order.

Avoidance of finite c says that f(r,-r^2) is a nonzero constant.
Writing

\[
f=A_0v+A_1rt+A_2r^2+A_3t+A_4r+A_5
\]

gives

\[
f|_c=A_0r^4+(-A_0-A_1)r^3+(A_2-A_3)r^2+A_4r+A_5.
\]

Constancy forces `A0=A1=A4=0,A2=A3`. A nonconstant prime therefore
has equation `A3 T+A5`, with both coefficients nonzero, and exact
degree four. This proves that among degrees at most five the only
allowed prime other than ell has degree four. It includes singular
projective primes and repeated occurrences of a prime in the conductor.

## 4. Excluding ell over the nonclosed generic residue field

The line ell maps isomorphically to a target line L: its four actual
sections are `(u-1,u-1+delta,u-1+3delta,u-1+4delta)`, which span
the full degree-one system. Its generic residue field is
`K=k(L)=k(u)`, not the algebraically closed constant field.

The required generic cotangent argument can be proved by an actual
target equation, avoiding any residue-field shortcut. In the target
X0 chart let

\[
\ell_2=X_2/X_0-3X_1/X_0+2.
\]

It vanishes on L. Its actual numerator is
`3delta^2 U2-delta^3 U1+E h`. In the fourth source chart,

\[
U_2=x(1+xu),\quad U_1=x^3(1+xu)^2,\quad
h=x(1+xu)+x^2(1+xu)^2,\quad X_0|_{x=0}=u-1.
\]

Consequently

\[
\ell_2=x\frac{E+3\delta^2}{u-1}+O(x^2).
\]

Its ell valuation is exactly one on the retained locus. If ell is
the sole normalization branch over generic L, the finite local
normalization ring B_eta is a DVR with residue K, equal to the
residue field of A_eta. The element ell_2 belongs to m_A and generates
the maximal ideal of B_eta up to a unit. Hence `m_A B=n_B`.
Residue equality gives `B=A+n_B=A+m_A B`; Nakayama on the finite
A-module B/A gives A=B. Thus a sole branch cannot be a conductor
branch. This proof works over K and requires neither an algebraically
closed residue field nor an inverse-function theorem.

If another branch exists, the actual two-generator fiber bound leaves
at most one additional branch and forces its residue-field degree to
be one. Its distinct source prime D' has
`H.D'=degree(map)*degree(L)=1`, contradicting uniqueness of ell.
All branches over a generic conductor point occur in the conductor:
I is proper in the target local ring, so its extension is proper in
each normalization maximal ideal. Thus no uncounted additional
branch can escape this argument. Ell is excluded.

## 5. Split reduced algebras are excluded by degree accounting

Now every conductor prime has degree at least four, and none has
degree five. If a generic full conductor algebra T has split reduction,
the field-degree bound makes it exactly `K x K`. Its two distinct
source primes D1,D2 map birationally onto the same image curve, so
their H-degrees equal its degree e. They occur with positive integer
coefficients in the actual Cartier divisor Dc of total degree ten.
Hence `2e<=10`, and the preceding prime classification forces e=4.

Their minimum contribution is eight; increasing either integer
coefficient makes it at least twelve. Minimum coefficients leave
degree two, which cannot be supplied by any remaining prime now that
ell and all primes of degree two or three have been excluded.
Therefore no split reduced generic conductor occurs.

This accounting does not replace nonreduced conductor schemes by
their reductions: the integer coefficients explicitly retain them.
The possible full generic Artinian algebra has one residue field
L/K of degree one or two. Its nilpotent length is unrestricted by
this field-degree statement.

## 6. Full arbitrary-power membership forces Q squared membership

Trivialize the actual downstairs line bundle O_X(4) at each generic
conductor point. The residue q of Q in T=B/I is a unit, because its
upstairs divisor 5c has no conductor prime. The supposed mate gives
full membership `q^k in R=A/I`, not only a tensor equalizer or reduced
membership.

Here R is Artinian local, Rred=K, and Tred=L is one field of degree
at most two. If alpha=qred belongs to K, its minimum reduced period
is one. Otherwise L/K has degree two and its nontrivial automorphism
sends alpha to zeta alpha, since alpha^k lies in K. All roots of unity
are already in K. Applying the automorphism twice gives zeta^2=1;
since alpha is not in K, zeta=-1. Thus alpha^2 belongs to K, the
minimum period is two, and k must be even. This is why odd successful
k cause no omitted parity case: they require period one.

The full nilpotent step is indispensable. Let d be this period, one
or two, choose a unit r in R lifting alpha^d, and put
`q^d/r=1+n` with n nilpotent in T. A successful k=dm implies
`(1+n)^m in R`. In characteristic zero the finite nilpotent logarithm
gives `m log(1+n) in R`; dividing by m and applying the finite
exponential gives `1+n in R`. Hence `q^d in R`, in every nilpotent
layer. Either value of d implies `q^2 in R`.

For comparison, the abstract split algebra `K x K` permits residues
`(1,zeta)` with arbitrary root-of-unity order; a two-branch bound alone
would not imply this conclusion. That algebra was excluded by the
actual geometry in section 5 before this power argument. Likewise,
two generators do not bound nilpotent conductor length: for
`A=K[[t^2,t^(2m+1)]]` inside `B=K[[t]]`, B has two generators over
A while the conductor quotient B/(t^(2m)) has length 2m. The proof
retains these potential nilpotent lengths rather than replacing T
by a quadratic reduced cover.

## 7. Purity, the actual ambient mate and the socle contradiction

The accepted entire quotient is
`nu_*O_S/O_X=omega_Gamma(-H)`, maximal Cohen--Macaulay on the
Cohen--Macaulay conductor curve, and hence pure of dimension one.
The obstruction class of Q^2 in this quotient twisted by O_X(8)
vanishes at every generic conductor point by full membership above.
Its generated coherent subsheaf would then have finite support;
purity makes it zero. Thus Q^2 descends globally to O_X(8), including
all special conductor points. Residue-only membership would not
justify this invocation of purity.

The quintic hypersurface sequence
`0 -> O_P3(3) -> O_P3(8) -> O_X(8) -> 0` and H1(O_P3(3))=0 lift
that section to an ambient degree-eight form G. Its pulled-back
zero divisor is 10c. Finite surjectivity of nu makes the zero support
of G on X exactly C0, so G is an actual degree-eight mate.

This mate gives a generically curvilinear CI(5,8), of multiplicity
ten. Coprimality fixes its first saturated quotient as
`L=O_P1(3-7)=O_P1(-4)`. Complete-intersection duality fixes the
top socle line as `E9=O_P1(-38)`. Generic curvilinear multiplication
gives a generically nonzero global map `L^9 -> E9`, but its Hom
space is H0(O_P1(-2))=0. Equivalently the effective top defect would
have degree -2. This is the accepted socle bound, now applied to an
actual forced mate rather than an assumed degree reduction.

The contradiction excludes every supposed mate power in this stratum.
Combined with the independently audited Jbar-nonzero obstruction, a
mate anywhere in this nonendpoint genus-one lane must satisfy the
complete homogeneous common-root condition `Res_h(Ph,Jh)=0`.
The common-root, higher-jet and full-conductor incidence remains open;
other quintic normalization genera and higher carriers are outside scope.

## 8. Exact supporting source and preserved failure

The independent
[supporting source](../computations/verify_session_jbar_zero_phase_audit_2026_10_12.m2)
has SHA-256
`946d697ec8dd208e0a02e7b150f9aa2500780d3539ad2a5adde1d1062ebcf70f`.
It passes twelve exact identities: three actual target generators,
cleared linear elimination, the cleared fiber quadratic coefficient,
absence of a third-generator linear term, ell section restriction,
its actual image-line equation and valuation-one numerator, the
ramified-line parameter exception, complete low-pole restriction,
and coincidence of the cubic leading coefficients.

The [captured execution record](../validation/2026-10-12-jbar-zero-phase-independent-audit/execution-record.json)
routes to two source snapshots with separate raw streams. Attempt 01
passes the first six identities and then fails because Macaulay2 has
no `substitute(List,List)` method. Attempt 02 changes only that list
operation to an elementwise apply and passes all twelve identities,
exit zero with empty stderr. The failed source and streams remain saved.
These are two executions of one source lineage; the snapshots are copies,
not additional independent implementations.

The twelve identities are supporting evidence for the written proof.
They do not computationally replace the finite local argument over K,
module propagation, all-prime classification, split accounting, full
nilpotent logarithm, purity or socle duality.
