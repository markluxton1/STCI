# Continuation checkpoint after the October 8 batch, reconciled October 9

Date: 2026-10-08. The universal STCI problem and the unrestricted
characteristic-zero C0 problem remain **OPEN**. Read the reconciled
[audited state](../AUDITED_STATE_2026-10-07.md) first. This checkpoint
preserves incomplete work as well as accepted progress.

## Accepted changes to the frontier

1. Every integral quartic normalized by (P2,O(2)) is excluded as a
   carrier of a smooth rational degree-four curve in characteristic
   zero, in every mate degree, including the non-slc Jordan forms.
2. Every integral quartic singular along a smooth twisted cubic is
   excluded as a carrier of fixed C0 in characteristic zero, in every
   mate degree. Its finite smooth-scroll normalization and whole
   conductor hypotheses are proved, rather than assumed.
3. The first rational primitive e=2,h=t endpoint ancestor family is
   fully excluded, including all 23 generic-dual exceptions and every
   affine lower lift. The second family has a generic exclusion with
   26 retained primitive geometric parameter points.
4. Both algebraic e=1,d2=4 ancestor directions are excluded for every
   homogeneous defect section, including repeated and infinity roots.
   The principal and obstruction-nonzero directions remain open.
5. The generator-bundle splitting criterion, all-defect quadric
   direction and six defect-one endpoint ancestor exclusions are
   accepted separately from their STCI-carrier counterparts.

The new scroll and defect-four results are reviewed in the
[root acceptance record](2026-10-08-session-new-results-acceptance.md).
The [late acceptance record](2026-10-08-session-late-results-acceptance.md)
supersedes the former incomplete contact and degenerate-conductor
boundaries. It accepts the entire e=1,d2=1 ancestor lane, every smooth
rational quartic-scroll carrier with unrestricted conductor schemes,
and both second-family quadratic exceptions. The second family now
retains 22 points in degree3,4,15 factors with their full lift fibres.
The previous all-normal-quartic and primitive e=1,D2=0 carrier theorems
remain accepted with their recorded antecedents. None of these results
is an exclusion of every quartic or every defining degree.

## Principal e=1,d2=1: an elliptic direction curve and finite contact locus

**PROVED equation reduction:** the saved principal chart equation H is
geometrically integral and has genus-one normalization. Put x=r+1/2,
W=(p+2-4x)/x^2, A=-W^3+8W^2-12W+72 and
C=2(W^2-6W+36). The exact identity is

    H(-2+4x+W*x^2,x-1/2)=-8*x^4*(A*x^2-2C*x+C).

Setting Y=(A*x-C)/W gives

    Y^2=2(W-6)(W^2-6W+36).

On the dense open where x,W,A are nonzero, the inverse is
x=(C+W*Y)/A, r=x-1/2, p=-2+4x+W*x^2. The Weierstrass form is

    YE^2=XE^3+96XE-448,
    XE=2(W-4), YE=2Y,
    discriminant=-143327232, j=2048/3.

The quadratic discriminant in x is a square factor times a cubic with
three distinct roots, so it is not a square even after extending the
constant field to an algebraic closure. The original H has no component
x=0, since H(p,-1/2)=8p(p+2)^2 is not the zero polynomial. This proves
geometric integrality and the genus statement. The
[self-contained identity source](../computations/verify_session_mf6_principal_elliptic_2026_10_08.py)
passed in a separate source-byte snapshot. Root compared its literal H
with the saved contact reconstruction. This is a reduction of that
candidate direction curve; it is not a full stratum exclusion.

**PROVED complete principal ancestor exclusion:** the following saved
data have now been reconstructed and exhausted in the complete open
and all projective boundary charts. The agent saved
the full first-normal/contact reconstruction and seven contact cofactors:

- [Complete contact data](../scratch/session-mf6-e1-principal-contact-2026-10-08.json)
  and [reconstruction source](../scratch/session-mf6-e1-principal-contact-2026-10-08.py).
- [Reduced six-by-seven contact matrix and seven cofactors](../scratch/session-mf6-e1-principal-minors-2026-10-08.json)
  and [source](../scratch/session-mf6-e1-principal-minors-2026-10-08.py).
- [Independent raw-cofactor factors](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.json),
  [source](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.py)
  and [completed printed output](../scratch/audit-mf6-e1-principal-raw-minors-2026-10-08.out).

The reduced matrix retains declared units and column frame factors.
Its seven maximal minors have full rank six on the declared open,
including the retained nonunit S branch. The complete first-normal
frame has an explicit nonzero free-row determinant. Two residual norms
and an exact quadratic-field gcd remove the possible rank drops.
Fresh all-35-column calculations exhaust the r=1/2, alternative defect
section at infinity and projective b0=0 charts. The node p=2,r=1/2
has dimension four with a fixed cubic times all linear forms; every
other valid principal fibre has dimension one. The node reduces to
P-037 rather than being discarded by a uniform dimension assertion.
See the [independent completeness proof](2026-10-08-session-principal-e1-d1-independent-completeness-audit.md)
and [frozen audit record](../validation/2026-10-08-principal-e1-d1-audit/audit-manifest.json).
Together with the accepted endpoints and primitive-point finite-flat
obstruction, this closes the entire e=1,d2=1 ancestor lane.

The principal unique-carrier problem is separate. The complement
carriers are all excluded in every mate degree, including the actual
nonreduced p=8,r=1/2 conductor. The remaining nonnormal carrier locus
is a finite proper closed subset of the integral parameter curve;
its exact enumeration remains OPEN. Saved weighted degree9,9,10
polynomial kernel generators are leads for this next step; inspect
their current completed audit status before relying on them.

An earlier message and the first elliptic verifier incorrectly used
H(p,-1/2)=8(p+2)^3. Root direct substitution corrected it to
8p(p+2)^2. The failed source revision and log are retained, and the
corrected verifier passed. Neither form vanishes identically in p,
so the no-vertical-component argument and Weierstrass identities are
unchanged. Do not reuse the incorrect fiber factor.

The principal e=1,d2=4 intrinsic-extension derivation was saved as
[an exploratory source](../computations/derive_session_localcoh_e1_d4_principal_extension_2026_10_08.py).
No completed output or independent cocycle identification was established
before interruption. Its proposed equation and its intersection with the
full quartic-rank incidence remain **OPEN**.

## Smooth-scroll conductors: an additional structural reduction

**PROVED with a separate written independent audit.** For any
smooth rational quartic-scroll normalization S->X, the actual downstairs
conductor is an ACM cubic curve with Hilbert polynomial 3m+1, including
reducible and nonreduced cases. The
[independent ACM proof](2026-10-08-session-scroll-acm-independent-audit.md)
now verifies the entire cohomological route. Here is the root's
verification, retained as an additional derivation.

Let J_Gamma be the conductor's ideal in P3. Finite duality gives

    0 -> O_P3(-4) -> J_Gamma -> nu_*omega_S -> 0.

The intermediate cohomology of line bundles on P3 vanishes, so
H1(J_Gamma(m))=H1(S,K_S+mH). Write S=F_e, with e=0 or 2,
H=C_min+a f, a=e/2+2 and K_S=-2C_min-(e+2)f. For m>=2,
the ruling pushforward is a sum of line bundles of degrees

    ma-e-2-j e,  0<=j<=m-2.

The minimum is m(a-e)+e-2: it is 2m-2 for e=0 and m for e=2.
Every summand has vanishing H1, and fiber degree m-2>=0 makes R1
of the pushforward zero. For m=1, fiber degree is -1, so both direct
images vanish. For m<=0, Serre duality reduces the claim to
H1(S,(-m)H)=0; its ruling summands all have degree at least
(-m)(a-e)>=0. Thus H1(J_Gamma(m))=0 for every integer m.

Moreover H0(J_Gamma(1))=0 and H0(J_Gamma(2)) has dimension three.
The codimension-two ACM coordinate ring has Hilbert h-vector (1,2):
its degree is three, and its first two entries already sum to three.
An Artinian reduction is k[u,v]/(u,v)^2. Lifting its three quadratic
generators and applying graded Nakayama gives the Hilbert--Burch
resolution

    0 -> O_P3(-3)^2 -> O_P3(-2)^3 -> J_Gamma -> 0.

This establishes the determinantal starting point used by the now
completed smooth-scroll theorem. The nongorenstein rank-zero schemes
are classified; their entire generic canonical modules, Frobenius
annihilators and actual differential valuations exhaust the residual
nonreduced cases. The independently proved differential obstruction
uses the entire mate power, not an ordinary-pinch count or reduced-fibre
involution. See the [classification](2026-10-08-session-scroll-nongorenstein-cubic-classification.md),
[exact Artin audit](2026-10-08-session-scroll-artin-independent-audit.md)
and [full independent audit](2026-10-08-session-scroll-nongorenstein-independent-audit.md).
**PROVED:** every integral quartic with smooth rational quartic-scroll
normalization is excluded for fixed C0 in every mate degree. Singular
normalizations and other smooth polarization classes remain OPEN.

## Execution and provenance boundary

Research agents have ended with account usage-limit errors and later
resumed after verified resets. Completed
files survive; planned audits, unfinished calculations and absent output
files do not acquire completion status from the assignment. Root replay
handle 61220 completed with exit zero; the later literal-minor and repaired
elliptic root runs also completed. The principal raw-factor output ends
in DONE and has a complete JSON, but no root-observed terminal process
record was supplied for that agent run. Do not infer a live process from
its source or restart an overlapping calculation without checking handles.

The [reconciled validation index](../validation/2026-10-08-continuation-index/index.json)
contains 91 distinct top-level sources, all with a latest PASS record,
and 103 explicitly indexed executions. Of these, the continuation adds
28 distinct sources in 30 central records, a separate strengthened
Veronese revision, the independent first-family countercheck, four
independent principal executions, and three additional family2 sources
with six explicitly indexed executions including tensor checker repairs.
Nested imports and agent discovery commands are not inflated into
independent source or execution counts. The original 55-source baseline
was retained, not rerun merely because the date changed.

The two central continuation failures remain visible: the conormal
verifier lacked its provenance proof-note input, then passed with the
completed input closure; the first elliptic verifier had the false fiber
factor above, then passed in a separate repaired source snapshot.

The integrity audit also found that the former --add copier recopied
files absent from the *initial* manifest, even when they had already
been added. Consequently the superseded October 7 Veronese-classifier
source bytes were overwritten by the strengthened revision. Its original
hash, log and addition-manifest transition remain; its old source bytes
are **not** claimed retained. The current stronger source has a separate
snapshot, matching hash and fresh PASS. The copier now checks whether
the target already exists, preventing this repeated-copy behavior.
This loss is explicitly represented in the index, rather than hidden
behind an assertion of immutable historical snapshots.

At 2026-10-09 11:25:38 UTC the 2:01 AM local reset had passed, and live
usage allowed ordinary work. The finite principal-carrier and singular
normalization agents resumed; their assignments are not completed
results until the sources, outputs and scope are reconciled. The full
scroll and family2 quadratic audits already have durable final proofs.
No root process is claimed live from a saved script alone.

No Git commit or branch mutation was attempted. Current worktree files
and dated evidence, rather than the retained October 6 commit alone,
are the continuation state. No universal counterexample, unrestricted
two-form presentation of C0 or all-degree obstruction has been obtained.
